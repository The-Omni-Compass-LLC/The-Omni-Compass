#!/usr/bin/env python3
"""XPASS20 breadth x population collective benchmark.

Primary scientific comparison:
  NATIVE: the declared active muscle set drives one coupled plant using native specialist feedback.
  OMNI_OVER_NATIVE: the exact same muscles remain the actuators; frozen CLAIM1 supervises their
  authority/targets. Omni is never treated as a replacement actuator stack.

Breadth and population are independent axes. Every active muscle is represented concurrently on
one simulation clock. All trajectories interact through shared power, queue, network and thermal
pressures. A paired cell uses identical seed, initial conditions and disturbances for both arms.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,resource,time,sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import numpy as np
from omnicompass.batch_claim1 import macro

ARMS=("NATIVE","OMNI_OVER_NATIVE")
MUSCLE_LADDER=(1,10,100,500,640)
POPULATION_LADDER=(1_000,10_000,100_000,1_000_000)

def load_catalog(root:Path):
    with (root/'muscles/FULL_TOWER_640.csv').open(newline='') as f: rows=list(csv.DictReader(f))
    if len(rows)!=640: raise RuntimeError(f'expected 640 catalog rows, got {len(rows)}')
    return rows

def assignment(population:int,muscle_count:int):
    if not 1<=muscle_count<=640: raise ValueError('muscle_count must be 1..640')
    if population<muscle_count: raise ValueError('population must be >= muscle_count so every active muscle is represented')
    # Round-robin guarantees every active muscle is concurrently represented.
    ids=np.arange(population,dtype=np.int32)%muscle_count
    counts=np.bincount(ids,minlength=muscle_count)
    if len(counts)!=muscle_count or np.any(counts==0): raise AssertionError('inactive requested muscle')
    return ids,counts

def muscle_parameters(ids):
    """Deterministic heterogeneous actuator/plant coefficients derived from canonical IDs.
    These are declared E2 plant semantics, not claims about proprietary product internals."""
    fam=ids//16; slot=ids%16
    response=.72+.015*(fam%9)+.006*(slot%7)
    resource=.82+.018*(fam%11)+.004*(slot%5)
    disturbance=.88+.025*(fam%7)+.008*(slot%3)
    slo=.16+.006*(fam%6)
    return response,resource,disturbance,slo

def run_arm(arm,population,muscle_count,steps,seed):
    ids,counts=assignment(population,muscle_count)
    response,rescoef,distcoef,sloq=muscle_parameters(ids)
    rng=np.random.default_rng(seed)
    demand=np.clip(rng.lognormal(-.15,.35,population)*distcoef,.10,2.8)
    initial_demand=demand.copy()
    cap=np.clip(rng.normal(1,.08,population),.55,1.35); native_start=cap.copy()
    queue=np.zeros(population); thermal=np.full(population,.30)
    # One independent six-state CLAIM1 trajectory per governed plant instance.
    x=np.column_stack((np.full(population,.12),np.full(population,.82),np.zeros(population),np.zeros(population),np.zeros(population),np.zeros(population)))
    target=np.ones(population)
    work=resource_sum=effort=0.; health_steps=0; violations=0; writes=0; peak_u=0.; sats=0
    muscle_work=np.zeros(muscle_count); muscle_resource=np.zeros(muscle_count); muscle_health=np.zeros(muscle_count)
    t0=time.perf_counter()
    for k in range(steps):
        # One common simulation clock. Global shock is shared; local noise is deterministic per paired seed.
        wave=.18*math.sin(2*math.pi*k/max(8,steps)); shock=(.45 if k==steps//3 else 0.)-(.25 if k==2*steps//3 else 0.)
        demand=np.clip(.94*demand+.06*(initial_demand*(1+wave+shock)+rng.normal(0,.12,population)*distcoef),.05,3.)
        served=np.minimum(demand,cap*response); queue=np.clip(.82*queue+np.maximum(0,demand-cap*response),0,4)
        util=np.clip(demand/np.maximum(cap*response,1e-9),0,2.2)
        power=np.clip((.23+.60*np.minimum(util,1)+.13*cap)*rescoef,0,1.7)
        gp=float(power.mean()); gq=float(queue.mean()); net=float(np.quantile(util,.90)/2)
        thermal=np.clip(.91*thermal+.09*(.18+.58*power+.18*gp+.06*net),0,1.6)
        healthy=(queue<sloq)&(thermal<1.0)&(util<1.25)
        health_steps+=int(healthy.sum()); work+=float(served.sum()); resource_sum+=float(power.sum())
        muscle_work += np.bincount(ids,weights=served,minlength=muscle_count)
        muscle_resource += np.bincount(ids,weights=power,minlength=muscle_count)
        muscle_health += np.bincount(ids,weights=healthy.astype(float),minlength=muscle_count)
        # Native specialist command remains the actual actuator in BOTH arms.
        native_target=np.clip(demand/np.maximum(.76*response,.1),.42,1.55)
        if arm=='NATIVE': cmd=native_target
        elif arm=='OMNI_OVER_NATIVE':
            bint=np.clip(.58*queue+.42*np.maximum(0,util-.75),0,1); bext=np.clip(.33*power+.27*thermal+.20*net,0,1)
            eobs=np.clip(.25*queue+.18*np.maximum(0,util-.85)+.16*power+.13*thermal+.10*net,0,1.5)
            uobs=np.clip(1-(.27*queue+.18*power+.16*thermal+.12*net),0,1)
            sobs=np.clip(.36*thermal+.28*power+.18*net-.20*queue,-1,1); bobs=np.clip(.52*power+.26*thermal,-1,1.5)
            a=.339; x[:,0]=(1-a)*x[:,0]+a*eobs; x[:,1]=(1-a)*x[:,1]+a*uobs; x[:,2]=(1-a)*x[:,2]+a*np.clip(queue,0,2); x[:,3]=(1-a)*x[:,3]+a*sobs; x[:,4]=(1-a)*x[:,4]+a*bobs
            x,u,pk,st=macro(x,k*.1,bint,bext,target); peak_u=max(peak_u,float(pk.max())); sats+=int(st.sum())
            # CLAIM1 supervises the native target/envelope; it does not replace the muscle.
            rho=np.clip(.914-.252*x[:,2]-.297*x[:,0],.627,.914)
            supervised=np.clip(demand/np.maximum(rho*response,.1),.42,1.55)
            cmd=.58*native_target+.42*supervised
            # Shared facility pressure can narrow expansion only when backlog is already safe.
            if gp>.98 and gq<.05: cmd=np.minimum(cmd,cap*.985)
        else: raise ValueError(arm)
        delta=np.clip(cmd-cap,-.06,.08); effort+=float(np.abs(delta).sum()); writes+=int(np.count_nonzero(np.abs(delta)>1e-12)); cap=np.clip(cap+delta,.4,1.6)
        violations+=int(np.count_nonzero((cap<.4)|(cap>1.6)|~np.isfinite(cap)))
    cap=native_start.copy(); restored=bool(np.array_equal(cap,native_start))
    elapsed=time.perf_counter()-t0; rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    active=int(np.count_nonzero(counts)); per_health=muscle_health/(counts*steps)
    return dict(arm=arm,muscles_requested=muscle_count,muscles_active=active,population=population,steps=steps,seed=seed,
      elapsed_s=elapsed,updates_per_s=population*steps/max(elapsed,1e-12),rss_kb=rss,healthy_fraction=health_steps/(population*steps),
      successful_work=work,resource_index=resource_sum,work_per_resource=work/max(resource_sum,1e-12),control_effort=effort,writes=writes,
      authority_violations=violations,restore_verified=restored,peak_abs_u=peak_u,controller_saturations=sats,
      worst_muscle_health=float(per_health.min()),best_muscle_health=float(per_health.max()),
      muscles_with_zero_work=int(np.count_nonzero(muscle_work<=0)),muscles_with_zero_resource=int(np.count_nonzero(muscle_resource<=0)),
      final_global_queue=float(queue.mean()),final_global_thermal=float(thermal.mean()))

def seal(out:Path, files):
    d={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}; (out/'SHA256.json').write_text(json.dumps(d,indent=2)); return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--muscles',type=int,default=640); ap.add_argument('--population',type=int,default=10000); ap.add_argument('--steps',type=int,default=24); ap.add_argument('--seed',type=int,default=20260930); ap.add_argument('--out',required=True); a=ap.parse_args()
    root=Path(__file__).resolve().parents[1]; catalog=load_catalog(root); out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    rows=[run_arm(arm,a.population,a.muscles,a.steps,a.seed) for arm in ARMS]
    summary={'schema':'omni.xpass20.breadth_population.v1','catalog_contracts':len(catalog),'simultaneous_active_muscles':a.muscles,'population':a.population,'paired_arms':list(ARMS),'same_seed_same_workload':True,'collective':True,'omni_role':'supervisory only; native muscles remain actuators','coupling':['queue','network','power','thermal'],'rows':rows,'evidence_class':'E2_SIMULATION','limits':['Resource index is model-defined, not physical kWh.','Population is simulated governed trajectories, not physical machines.','This benchmark does not emulate proprietary competitor algorithms.','A pass establishes only the declared tested envelope.']}
    sj=out/'SUMMARY.json'; sj.write_text(json.dumps(summary,indent=2)); csvp=out/'RUNS.csv'
    with csvp.open('w',newline='') as f: w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    seal(out,[sj,csvp]);
    for r in rows: print(r['arm'], 'muscles',r['muscles_active'],'population',r['population'],'health',f"{r['healthy_fraction']:.6f}",'work/resource',f"{r['work_per_resource']:.6f}",'updates/s',f"{r['updates_per_s']:.0f}")
if __name__=='__main__': main()
