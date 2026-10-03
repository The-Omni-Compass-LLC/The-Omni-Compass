#!/usr/bin/env python3
import argparse,json,subprocess,sys,time
from pathlib import Path
B=(1,10,100,500,640); T=(1000,10000,100000,1000000)
ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=24);ap.add_argument('--chunk',type=int,default=1024);ap.add_argument('--out',default='results/xpass21_matrix');ap.add_argument('--max-seconds',type=float,default=0);a=ap.parse_args()
root=Path(__file__).resolve().parents[1]; out=root/a.out;out.mkdir(parents=True,exist_ok=True); status=[]; t0=time.time()
for m in B:
 for n in T:
  cell=out/f'm{m}_n{n}'; cmd=[sys.executable,str(root/'organism/xpass21_organism_lab.py'),'--breadth',str(m),'--trials',str(n),'--steps',str(a.steps),'--chunk',str(a.chunk),'--out',str(cell)]
  if a.max_seconds and time.time()-t0>a.max_seconds: status.append({'breadth':m,'trials':n,'status':'NOT_RUN_TIME_BUDGET'});continue
  try: subprocess.run(cmd,cwd=root,check=True); status.append({'breadth':m,'trials':n,'status':'PASS'})
  except subprocess.CalledProcessError as e: status.append({'breadth':m,'trials':n,'status':'ERROR','returncode':e.returncode})
(out/'MATRIX_STATUS.json').write_text(json.dumps(status,indent=2))
print(json.dumps(status,indent=2))
