#!/usr/bin/env python3
import argparse,csv,json,subprocess,sys,time
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('--muscle-ladder',default='1,10,100,500,640'); ap.add_argument('--population-ladder',default='1000,10000,100000,1000000'); ap.add_argument('--steps',type=int,default=24); ap.add_argument('--seed',type=int,default=20260930); ap.add_argument('--out',default='results/xpass20_matrix'); ap.add_argument('--stop-on-fail',action='store_true'); a=ap.parse_args()
root=Path(__file__).resolve().parents[1]; out=root/a.out; out.mkdir(parents=True,exist_ok=True); records=[]
for m in [int(x) for x in a.muscle_ladder.split(',')]:
  for n in [int(x) for x in a.population_ladder.split(',')]:
    d=out/f'm{m}_n{n}'; t=time.time(); cmd=[sys.executable,str(root/'collective/xpass20_matrix_lab.py'),'--muscles',str(m),'--population',str(n),'--steps',str(a.steps),'--seed',str(a.seed),'--out',str(d)]
    rc=subprocess.call(cmd,cwd=root); rec={'muscles':m,'population':n,'returncode':rc,'wall_s':time.time()-t,'status':'PASS' if rc==0 else 'FAIL'}; records.append(rec); print(rec,flush=True)
    if rc and a.stop_on_fail: break
  if records[-1]['returncode'] and a.stop_on_fail: break
(out/'MATRIX.json').write_text(json.dumps({'schema':'omni.xpass20.matrix.v1','muscle_ladder':a.muscle_ladder,'population_ladder':a.population_ladder,'paired_arms':['NATIVE','OMNI_OVER_NATIVE'],'cells':records,'rule':'Every cell activates all requested muscles concurrently on one shared simulation clock. Native and Omni-over-native use the same seed/workload. Only completed cells count.'},indent=2))
with (out/'MATRIX.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=records[0].keys());w.writeheader();w.writerows(records)
