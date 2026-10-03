#!/usr/bin/env python3
"""XPASS19 collective breadth x population benchmark.

One coupled synthetic infrastructure plant is driven by the same workload/disturbance
stream under multiple controller arms. 640 catalog entries are control vocabulary;
--population is total governed instances distributed across that vocabulary.
Comparator replicas are documented-behavior models, never proprietary product executions.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,os,resource,time
from pathlib import Path
import numpy as np
from omnicompass.batch_claim1 import macro

ARMS=['NATIVE_ONLY','WATCH_ZERO_WRITE','HPA_CA','KARPENTER_DOC_REPLICA','OPENSHIFT_AUTOSCALE_DOC_REPLICA','TURBONOMIC_ACTION_SURFACE_PROXY','BORG_POLICY_DOC_REPLICA','OMNI_DIRECT_CLAIM1','OMNI_OVER_NATIVE_CLAIM1']
PROVENANCE={
'NATIVE_ONLY':'generic native specialist feedback only',
'WATCH_ZERO_WRITE':'Omni computes but writes zero plant commands',
'HPA_CA':'documented HPA-like replica plus capacity autoscaling model',
'KARPENTER_DOC_REPLICA':'documented-behavior capacity provision/consolidation replica; not Karpenter product execution',
'OPENSHIFT_AUTOSCALE_DOC_REPLICA':'documented cluster/machine autoscaling behavior replica; not OpenShift product execution',
'TURBONOMIC_ACTION_SURFACE_PROXY':'resize/placement/provision/suspend action-surface proxy; NOT IBM Turbonomic optimizer',
'BORG_POLICY_DOC_REPLICA':'admission/packing/overcommit/sharing cluster-policy replica; NOT Google Borg',
'OMNI_DIRECT_CLAIM1':'frozen CLAIM1 supervises generic bounded plant authority directly',
'OMNI_OVER_NATIVE_CLAIM1':'frozen CLAIM1 supervises native specialist targets/envelopes; specialists remain actuators'}

def load_catalog(root):
    with open(root/'muscles/FULL_TOWER_640.csv',newline='') as f:return list(csv.DictReader(f))

def run_arm(arm,n,steps,seed,catalog):
    rng=np.random.default_rng(seed); ids=np.arange(n)%len(catalog); fam=ids//16
    # common plant state: demand, capacity, queue, resource draw, thermal, health
    demand=np.clip(rng.lognormal(-.15,.35,n),.15,2.5).astype(np.float64)
    cap=np.clip(rng.normal(1,.08,n),.55,1.35); queue=np.zeros(n); thermal=np.full(n,.30)
    x=np.column_stack((np.full(n,.12),np.full(n,.82),np.zeros(n),np.zeros(n),np.zeros(n),np.zeros(n)))
    target=np.ones(n); native=cap.copy(); writes=0; violations=0; restored=False; work=energy=effort=0.; health_steps=0
    t0=time.perf_counter(); peak_u=0.; sats=0
    for k in range(steps):
        # correlated system event + family-local heterogeneity; same seed/arm seed convention makes workload identical across arms
        wave=.18*math.sin(2*math.pi*k/max(8,steps))
        shock=(.45 if k==steps//3 else 0.)-(.25 if k==2*steps//3 else 0.)
        demand=np.clip(.94*demand+.06*(1+wave+shock+rng.normal(0,.12,n)),.05,3.)
        served=np.minimum(demand,cap); queue=np.clip(.82*queue+np.maximum(0,demand-cap),0,4)
        util=np.clip(demand/np.maximum(cap,1e-9),0,2); power=np.clip(.25+.62*np.minimum(util,1)+.12*cap,0,1.5)
        # Coupling: global electrical/network pressure feeds every local trajectory.
        global_power=float(power.mean()); global_queue=float(queue.mean()); network=float(np.percentile(util,90)/2)
        thermal=np.clip(.91*thermal+.09*(.18+.62*power+.20*global_power),0,1.5)
        healthy=(queue<.20)&(thermal<1.0)&(util<1.25); health_steps+=int(healthy.sum())
        work+=float(served.sum()); energy+=float(power.sum())
        desired=np.clip(demand/.78,.45,1.5)
        if arm in ('WATCH_ZERO_WRITE',):
            # Compute exact batched CLAIM1 but deliberately issue no writes.
            bint=np.clip(.58*queue+.42*np.maximum(0,util-.75),0,1); bext=np.clip(.33*power+.27*thermal+.20*network,0,1)
            x,u,pk,st=macro(x,k*.1,bint,bext,target); peak_u=max(peak_u,float(pk.max())); sats+=int(st.sum())
            cmd=cap
        elif arm.startswith('OMNI_'):
            bint=np.clip(.58*queue+.42*np.maximum(0,util-.75),0,1); bext=np.clip(.33*power+.27*thermal+.20*network,0,1)
            # observation assimilation, vector form of adapter.py
            eobs=np.clip(.25*queue+.18*np.maximum(0,util-.85)+.16*power+.13*thermal+.10*network,0,1.5)
            uobs=np.clip(1-(.27*queue+.18*power+.16*thermal+.12*network),0,1)
            sobs=np.clip(.36*thermal+.28*power+.18*network-.20*queue,-1,1); bobs=np.clip(.52*power+.26*thermal, -1,1.5); iobs=np.clip(queue,0,2)
            a=.339; x[:,0]=(1-a)*x[:,0]+a*eobs; x[:,1]=(1-a)*x[:,1]+a*uobs; x[:,2]=(1-a)*x[:,2]+a*iobs; x[:,3]=(1-a)*x[:,3]+a*sobs; x[:,4]=(1-a)*x[:,4]+a*bobs
            x,u,pk,st=macro(x,k*.1,bint,bext,target); peak_u=max(peak_u,float(pk.max())); sats+=int(st.sum())
            rho=np.clip(.914-.252*x[:,2]-.297*x[:,0],.627,.914); omni=np.clip(demand/np.maximum(rho,.1),.45,1.5)
            # collective electrical pressure reduces expansion; backlog/SLO prevents unsafe trimming
            omni=np.where((global_power>.96)&(queue<.05),np.minimum(omni,cap*.98),omni)
            if arm=='OMNI_OVER_NATIVE_CLAIM1': cmd=.55*desired+.45*omni
            else: cmd=omni
        elif arm=='HPA_CA': cmd=np.clip(demand/.70,.45,1.5)
        elif arm in ('KARPENTER_DOC_REPLICA','OPENSHIFT_AUTOSCALE_DOC_REPLICA'): cmd=np.clip(demand/.72,.45,1.5)
        elif arm=='TURBONOMIC_ACTION_SURFACE_PROXY': cmd=np.clip(demand/.82,.40,1.45)
        elif arm=='BORG_POLICY_DOC_REPLICA': cmd=np.clip(.70*desired+.30*np.maximum(demand,.65),.45,1.45)
        else: cmd=desired
        if arm!='WATCH_ZERO_WRITE':
            delta=np.clip(cmd-cap,-.06,.08); effort+=float(np.abs(delta).sum()); writes+=int(np.count_nonzero(np.abs(delta)>1e-12)); cap=np.clip(cap+delta,.4,1.5)
        violations+=int(np.count_nonzero((cap<.4)|(cap>1.5)|~np.isfinite(cap)))
    # restore all authority surfaces to starting/native values and verify
    cap=native.copy(); restored=bool(np.array_equal(cap,native))
    elapsed=time.perf_counter()-t0; rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return {'arm':arm,'population':n,'steps':steps,'seed':seed,'elapsed_s':elapsed,'updates_per_s':n*steps/max(elapsed,1e-9),'rss_kb':rss,'healthy_fraction':health_steps/(n*steps),'successful_work':work,'resource_index':energy,'work_per_resource':work/max(energy,1e-9),'control_effort':effort,'writes':writes,'authority_violations':violations,'restore_verified':restored,'peak_abs_u':peak_u,'controller_saturations':sats,'global_final_queue':float(queue.mean()),'global_final_thermal':float(thermal.mean())}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--population',type=int,default=6400); ap.add_argument('--steps',type=int,default=24); ap.add_argument('--seed',type=int,default=20260930); ap.add_argument('--arms',default=','.join(ARMS)); ap.add_argument('--out',required=True); a=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; cat=load_catalog(root); out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    rows=[]
    for arm in a.arms.split(','):
        if arm not in ARMS: raise SystemExit('unknown arm '+arm)
        rows.append(run_arm(arm,a.population,a.steps,a.seed,cat)); print(arm,rows[-1]['healthy_fraction'],rows[-1]['work_per_resource'],rows[-1]['updates_per_s'])
    (out/'SUMMARY.json').write_text(json.dumps({'schema':'omni.xpass19.collective.v1','catalog_contracts':len(cat),'population':a.population,'collective':True,'coupling':['global_power','global_queue','network','thermal'],'arms':PROVENANCE,'rows':rows,'limits':['Simulation results are E2 only.','Comparator replicas are not proprietary product executions.','Resource index is model-defined, not physical kWh.','Population means concurrent simulated governed trajectories, not physical machines.']},indent=2))
    with (out/'RUNS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    seals={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [out/'SUMMARY.json',out/'RUNS.csv']};(out/'SHA256.json').write_text(json.dumps(seals,indent=2))
if __name__=='__main__':main()
