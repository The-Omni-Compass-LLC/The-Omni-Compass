#!/usr/bin/env python3
"""XPASS15 allocator-holdout four-arm tournament.

C1 HPA+CA, C3 HPA+Karpenter documented-behavior replica,
C6 broad action-surface proxy, C7 Omni CLAIM1.
No proprietary comparator product is executed.
"""
from __future__ import annotations
import argparse,csv,json,hashlib,math,sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from dataclasses import asdict
import numpy as np
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from k8s_fleet.plant import FleetConfig,Fleet,generate_workloads,TICK_S
from k8s_fleet.controllers import HPA,ClusterAutoscaler,Karpenter,RequestSizer,_fits_elsewhere,_pending_nodes
from k8s_fleet.benchmark import OmniFleetLaw,telemetry_obs
from omnicompass.adapter import Governor,AllocationLaw,AUTOPILOT

ARMS={
'C1_HPA_CA':'hpa70_ca',
'C3_HPA_KARPENTER_DOC_REPLICA':'hpa70_karpenter',
'C6_TURBO_ACTION_SURFACE_PROXY':'hpa70_karpenter_vpa',
'C7_OMNI_COMPASS_CLAIM1':'omni_full'}
PROVENANCE={
'C1_HPA_CA':{'class':'documented_behavior_model','claim':'Kubernetes HPA behavior plus repository Cluster Autoscaler model; not a managed-service product execution.'},
'C3_HPA_KARPENTER_DOC_REPLICA':{'class':'documented_behavior_model','claim':'Karpenter-style pending-capacity provisioning and consolidation feasibility replica; intentionally simpler than Karpenter.'},
'C6_TURBO_ACTION_SURFACE_PROXY':{'class':'action_surface_proxy','claim':'Aggressive resize plus horizontal scale plus capacity action surface. It is not IBM Turbonomic and contains no proprietary IBM optimizer.'},
'C7_OMNI_COMPASS_CLAIM1':{'class':'native_repository_controller','claim':'Current repository Omni fleet governor using canonical CLAIM1 evolution.'}}
DEFAULT_CE={'replica_change':1.0,'pod_move':1.0,'node_provision':8.0,'node_suspend':8.0,'resize':4.0,'reversal':6.0,'power_cap_travel':2.0}
CE_SWEEPS={
'balanced':DEFAULT_CE,
'node_heavy':{'replica_change':1,'pod_move':1,'node_provision':16,'node_suspend':16,'resize':4,'reversal':8,'power_cap_travel':2},
'replica_heavy':{'replica_change':4,'pod_move':1,'node_provision':8,'node_suspend':8,'resize':4,'reversal':8,'power_cap_travel':2},
'resize_heavy':{'replica_change':1,'pod_move':1,'node_provision':8,'node_suspend':8,'resize':12,'reversal':6,'power_cap_travel':2},
'uniform':{'replica_change':1,'pod_move':1,'node_provision':1,'node_suspend':1,'resize':1,'reversal':1,'power_cap_travel':1}}
METRICS=['energy_kwh','time_healthy','served_fraction','backlog_p95','node_starts','node_stops','evictions','request_changes','replica_change_units','replica_reversals','mean_nodes','peak_nodes','power_cap_travel','shield_blocks']
LOWER=set(METRICS)-{'time_healthy','served_fraction'}

def simulate(seed, arm, cfg, olaw):
    wls=generate_workloads(cfg,seed); f=Fleet(cfg,wls)
    site_limit=f.cfg.max_nodes*(cfg.node_vcpu*1.2+cfg.node_gib*.392)*cfg.pue*.5
    hpa=HPA(.7); ca=ClusterAutoscaler() if arm=='hpa70_ca' else None
    kp=Karpenter() if arm in ('hpa70_karpenter','hpa70_karpenter_vpa') else None
    full=arm=='omni_full'; sizer=RequestSizer() if arm=='hpa70_karpenter_vpa' else None
    # XPASS15 finding: coordinated request sizing was the dominant C7 churn amplifier.
    # It is removed from the C7 allocation path rather than hidden behind a favorable CE weight.
    gov=Governor(law=AllocationLaw(push_release=olaw.push_release),evolve=True) if full else None
    if gov: gov.set_mode(AUTOPILOT)
    thermal=.3; last_prov=last_cons=-10**9; converged=True; rho=.7
    healthy=0; served_sum=demand_sum=0.; backlogs=[]; nodes_hist=[]; shield_blocks=0; cap_travel=0.
    replica_units=0; reversals=0; last_dir={k:0 for k in f.w}
    original_set=f.set_replicas
    def tracked_set(name,r):
        nonlocal replica_units,reversals
        old=f.w[name].replicas; new=max(f.w[name].min_replicas,min(f.w[name].max_replicas,r)); d=new-old
        if d:
            replica_units+=abs(d); s=1 if d>0 else -1
            if last_dir[name] and last_dir[name]!=s: reversals+=1
            last_dir[name]=s
        return original_set(name,r)
    f.set_replicas=tracked_set
    for tick in range(cfg.ticks):
        tel=f.step(tick); demand_sum+=tel['demand']; served_sum+=min(tel['served'],tel['demand']+1e9)
        healthy+=int(tel['worst_served']>=cfg.healthy_served and tel['pending']==0); backlogs.append(tel['backlog']); nodes_hist.append(tel['nodes'])
        thermal=.9*thermal+.1*min(1.5,tel['power_w']/site_limit)
        if gov is not None and tick%olaw.period_ticks==0:
            obs=telemetry_obs(tel,site_limit,thermal); gov.current_cap=float(np.mean([n.cap for n in f.nodes])) if f.nodes else 1.; gov.nodes=len(f.nodes)
            d=gov.step(obs,0); rho=float(d['demand']); converged=gov.last_push<=olaw.push_release
        if full: hpa.target=float(np.clip(rho,olaw.target_lo,olaw.target_hi))
        hpa.step(f,tick)
        if sizer: sizer.step(f,tick,allow=(converged if full else True),hpa_target=(hpa.target if full else 0.0))
        if ca: ca.step(f,tick)
        if kp: kp.step(f,tick)
        if full:
            k=_pending_nodes(f,tick)
            if k>0: f.add_nodes(k,tick,cfg.karpenter_boot_s); last_prov=tick
            elif tick%olaw.period_ticks==0 and len(f.nodes)>cfg.min_nodes:
                ready=[n for n in f.nodes if n.ready_at<=tick]; req_total=sum(f.requested(n) for n in f.nodes)
                want=converged and tick-max(last_prov,last_cons)>=olaw.consolidate_dwell_ticks and req_total<=(len(f.nodes)-1)*cfg.node_allocatable*olaw.pack
                if want:
                    cand=sorted(ready,key=lambda n:f.requested(n)); ok=f.pending=={} and tel['backlog']<=olaw.shield_backlog*max(1e-9,tel['capacity'])
                    victim=next((n for n in cand if tick-n.added_at>=300//TICK_S and _fits_elsewhere(f,n,tick)),None)
                    if ok and victim is not None: f.remove_node(victim); f.schedule(tick); last_cons=tick
                    else: shield_blocks+=1
            use=getattr(f,'node_use',{})
            for n in f.nodes:
                old=n.cap
                if tel['backlog']>olaw.shield_backlog*max(1e-9,tel['capacity']) or last_prov==tick: new=max(old,1.0) if tel['backlog']>olaw.shield_backlog*max(1e-9,tel['capacity']) else old
                else: new=float(np.clip(use.get(id(n),0.)/cfg.node_vcpu*(1.+olaw.cap_margin),olaw.cap_min,1.))
                cap_travel+=abs(new-old); n.cap=new
    return {'seed':seed,'arm':arm,'energy_kwh':f.energy_wh/1000.,'time_healthy':healthy/cfg.ticks,'served_fraction':min(1.,served_sum/max(1e-9,demand_sum)),'backlog_p95':float(np.percentile(backlogs,95)),'node_starts':f.starts,'node_stops':f.stops,'evictions':f.evictions,'request_changes':sizer.changes if sizer else 0,'replica_change_units':replica_units,'replica_reversals':reversals,'mean_nodes':float(np.mean(nodes_hist)),'peak_nodes':max(nodes_hist),'power_cap_travel':cap_travel,'shield_blocks':shield_blocks}

def ce(r,w): return (w['replica_change']*r['replica_change_units']+w['pod_move']*r['evictions']+w['node_provision']*r['node_starts']+w['node_suspend']*r['node_stops']+w['resize']*r['request_changes']+w['reversal']*r['replica_reversals']+w['power_cap_travel']*r['power_cap_travel'])
def delta_ci(rows,base,cand,metric,rng):
    A={r['seed']:r[metric] for r in rows if r['controller']==base};B={r['seed']:r[metric] for r in rows if r['controller']==cand}; d=np.array([B[k]-A[k] for k in sorted(A)])
    bs=d[rng.integers(0,len(d),(4000,len(d)))].mean(axis=1);lo,hi=np.percentile(bs,[2.5,97.5]); lower=metric in LOWER or metric.startswith('ce_')
    verdict='better' if (hi<0 if lower else lo>0) else 'worse' if (lo>0 if lower else hi<0) else 'not_proven'
    return {'metric':metric,'mean_delta':float(d.mean()),'ci95':[float(lo),float(hi)],'verdict':verdict}
def _one(job):
    seed,label,arm=job; cfg=FleetConfig(); law=OmniFleetLaw(cap_min=0.45, cap_margin=0.02); r=simulate(seed,arm,cfg,law); r['controller']=label; r['implementation_arm']=arm
    for name,w in CE_SWEEPS.items(): r['ce_'+name]=ce(r,w)
    return r

def run(n,seed0,out):
    cfg=FleetConfig(); law=OmniFleetLaw(); jobs=[(seed0+i,label,arm) for i in range(n) for label,arm in ARMS.items()]
    with ProcessPoolExecutor(max_workers=4) as ex: rows=list(ex.map(_one,jobs,chunksize=4))
    out.mkdir(parents=True,exist_ok=True)
    with (out/'RUNS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    allm=METRICS+['ce_'+k for k in CE_SWEEPS]
    means={c:{m:float(np.mean([r[m] for r in rows if r['controller']==c])) for m in allm} for c in ARMS}
    rng=np.random.default_rng(20260929); paired={}
    for c in ARMS:
        if c!='C7_OMNI_COMPASS_CLAIM1':paired['C7_vs_'+c]=[delta_ci(rows,c,'C7_OMNI_COMPASS_CLAIM1',m,rng) for m in allm]
    summary={'schema':'omni.public_policy_tournament.xpass15.v1','scenarios':n,'seed0':seed0,'seed_last':seed0+n-1,'plant':'k8s_fleet frozen common plant','xpass15_allocator_policy':{'request_sizer':'disabled for C7','cap_min':0.45,'cap_margin':0.02,'core_equations_changed':False,'reason':'development-seed ablation isolated request sizing as dominant churn amplifier; power envelope then retuned on development seeds only'},'arms':ARMS,'provenance':PROVENANCE,'ce_definition':{'formula':'weighted sum of replica-change units, pod moves/evictions, node provisions, node suspensions, request resizes, replica-direction reversals, and power-cap travel','weights':CE_SWEEPS,'warning':'CE is an experiment-defined control-effort index, not a universal physical quantity. Conclusions must be checked across weight sweeps.'},'means':means,'paired':paired,'claim_limits':['No proprietary comparator product was executed.','C6 is an action-surface stress proxy, not IBM Turbonomic.','All energy values are modeled plant energy, not physical meter readings.','No global superiority claim is authorized.','Kind-23 and physical NVIDIA evidence remain separate external evidence classes.']}
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2));
    seals={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out/'RUNS.csv',out/'SUMMARY.json')};(out/'SHA256.json').write_text(json.dumps(seals,indent=2))
    return summary

def main():
    p=argparse.ArgumentParser();p.add_argument('--scenarios',type=int,default=30);p.add_argument('--seed',type=int,default=20260929);p.add_argument('--out',required=True);a=p.parse_args();s=run(a.scenarios,a.seed,Path(a.out))
    for c,m in s['means'].items():print(c,'energy',round(m['energy_kwh'],4),'healthy',round(m['time_healthy'],5),'CE',round(m['ce_balanced'],1),'starts/stops',round(m['node_starts'],1),round(m['node_stops'],1))
if __name__=='__main__':main()
