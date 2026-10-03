#!/usr/bin/env python3
import argparse,json,subprocess,sys,time
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--populations',default='640,6400,64000,640000,1000000');ap.add_argument('--steps',type=int,default=24);ap.add_argument('--out',default='results/xpass19_scale_ladder');ap.add_argument('--max-seconds',type=float,default=0);a=ap.parse_args()
root=Path(__file__).resolve().parents[1]; out=root/a.out;out.mkdir(parents=True,exist_ok=True); rows=[]
for s in a.populations.split(','):
 n=int(s); d=out/str(n); t=time.time(); rc=subprocess.call([sys.executable,str(root/'collective/scale_lab.py'),'--population',str(n),'--steps',str(a.steps),'--out',str(d)],cwd=root); elapsed=time.time()-t
 rows.append({'population':n,'returncode':rc,'wall_s':elapsed,'status':'PASS' if rc==0 else 'FAIL'})
 if rc!=0 or (a.max_seconds and elapsed>a.max_seconds): break
(out/'LADDER.json').write_text(json.dumps({'requested':a.populations,'steps':a.steps,'runs':rows,'rule':'stop on execution failure or optional declared wall-time boundary; last completed population is measured envelope, never extrapolate as achieved'},indent=2))
