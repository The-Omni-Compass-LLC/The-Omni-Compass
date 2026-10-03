#!/usr/bin/env python3
"""Public-policy comparator tournament for Omni-Compass.

IMPORTANT: comparator names ending *_PUBLIC_POLICY_REPLICA are behavioral replicas
built only from public documentation plus explicitly declared approximations. They
are NOT executions of proprietary products and MUST NOT be presented as such.
"""
from __future__ import annotations
import argparse,csv,json,sys,hashlib
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from k8s_fleet.benchmark import simulate, OmniFleetLaw
from k8s_fleet.plant import FleetConfig

# Existing frozen plant arms are reused rather than cloning the plant.
ARMS={
 "KUBERNETES_HPA_CA": "hpa70_ca",
 "OPENSHIFT_AUTOSCALE_PUBLIC_POLICY_REPLICA": "hpa70_ca",
 "KARPENTER_PUBLIC_POLICY_REPLICA": "hpa70_karpenter",
 "STORMFORGE_PUBLIC_POLICY_REPLICA": "hpa70_karpenter_vpa",
 "TURBONOMIC_ACTION_SURFACE_PROXY": "hpa70_karpenter_vpa",
 "OMNI_COMPASS_CLAIM1": "omni_full",
}
# Honesty metadata is part of the result, not prose added later.
PROVENANCE={
 "KUBERNETES_HPA_CA": {"class":"documented_behavior_model","notes":"HPA ratio/tolerance/stabilization + repository CA model"},
 "OPENSHIFT_AUTOSCALE_PUBLIC_POLICY_REPLICA": {"class":"stack_proxy","notes":"Uses same HPA+CA mechanics; does not reproduce Red Hat implementation internals"},
 "KARPENTER_PUBLIC_POLICY_REPLICA": {"class":"documented_behavior_model","notes":"Provision pending capacity + consolidation feasibility; repository Karpenter-lite is intentionally simpler than Karpenter"},
 "STORMFORGE_PUBLIC_POLICY_REPLICA": {"class":"action_surface_proxy","notes":"Request sizing + horizontal scaling coordination proxy; proprietary ML is NOT reproduced"},
 "TURBONOMIC_ACTION_SURFACE_PROXY": {"class":"action_surface_proxy","notes":"Resize/capacity action-surface proxy only; IBM proprietary decision engine is NOT reproduced"},
 "OMNI_COMPASS_CLAIM1": {"class":"native_repository_controller","notes":"Current repository Omni fleet governor"},
}
METRICS=["energy_kwh","time_healthy","served_fraction","backlog_p95","node_starts","node_stops","evictions","request_changes","mean_nodes","peak_nodes","power_cap_travel","shield_blocks"]
LOWER={"energy_kwh","backlog_p95","node_starts","node_stops","evictions","request_changes","mean_nodes","peak_nodes","power_cap_travel","shield_blocks"}

def ci_delta(rows, base, cand, metric, rng):
    a={r['seed']:r[metric] for r in rows if r['controller']==base}; b={r['seed']:r[metric] for r in rows if r['controller']==cand}
    d=np.array([b[k]-a[k] for k in sorted(a)],dtype=float)
    boot=d[rng.integers(0,len(d),(4000,len(d)))].mean(axis=1)
    lo,hi=np.percentile(boot,[2.5,97.5]);
    if metric in LOWER: verdict='better' if hi<0 else 'worse' if lo>0 else 'not_proven'
    else: verdict='better' if lo>0 else 'worse' if hi<0 else 'not_proven'
    return {'metric':metric,'mean_delta':float(d.mean()),'ci95':[float(lo),float(hi)],'verdict':verdict}

def run(n,seed0,out):
    cfg=FleetConfig(); law=OmniFleetLaw(); rows=[]
    for i in range(n):
      seed=seed0+i
      for label,arm in ARMS.items():
        r=simulate(seed,arm,cfg,law); r['controller']=label; r['implementation_arm']=arm; rows.append(r)
    out.mkdir(parents=True,exist_ok=True)
    with (out/'RUNS.csv').open('w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    means={c:{m:float(np.mean([r[m] for r in rows if r['controller']==c])) for m in METRICS} for c in ARMS}
    rng=np.random.default_rng(20260929); paired={}
    for c in ARMS:
      if c!='OMNI_COMPASS_CLAIM1': paired[f'OMNI_vs_{c}']=[ci_delta(rows,c,'OMNI_COMPASS_CLAIM1',m,rng) for m in METRICS]
    summary={'schema':'omni.public_policy_tournament.v1','scenarios':n,'seed0':seed0,'plant':'k8s_fleet frozen common plant','provenance':PROVENANCE,'means':means,'paired':paired,
      'claim_limits':['No proprietary comparator product was executed.','Proxy equality does not imply product equality.','All energy values are modeled, not physical kWh.','No global superiority claim is authorized by this tournament.']}
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2))
    seal={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [out/'RUNS.csv',out/'SUMMARY.json']}; (out/'SHA256.json').write_text(json.dumps(seal,indent=2))
    return summary

def main():
 p=argparse.ArgumentParser();p.add_argument('--scenarios',type=int,default=30);p.add_argument('--seed',type=int,default=20260929);p.add_argument('--out',default='results/public_policy_tournament');a=p.parse_args();s=run(a.scenarios,a.seed,Path(a.out))
 for c,m in s['means'].items(): print(c, 'energy',round(m['energy_kwh'],3),'healthy',round(m['time_healthy'],4),'p95q',round(m['backlog_p95'],2),'starts/stops',round(m['node_starts'],2),round(m['node_stops'],2))
if __name__=='__main__': main()
