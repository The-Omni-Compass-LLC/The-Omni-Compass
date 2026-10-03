#!/usr/bin/env python3
import argparse,json,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from organism.breadth_ladder import catalog_count,breadth_ladder
TRIALS=(1000,10000,100000,1000000)
ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=24);ap.add_argument('--chunk',type=int,default=1024);ap.add_argument('--out',default='results/xpass22_dynamic_matrix');ap.add_argument('--max-seconds',type=float,default=0);a=ap.parse_args()
cat=ROOT/'muscles/FULL_TOWER_640.csv'; final=catalog_count(cat); breadths=breadth_ladder(final)
out=ROOT/a.out;out.mkdir(parents=True,exist_ok=True);status=[];t0=time.time()
contract={'schema':'omni.xpass22.dynamic_breadth.v1','catalog':str(cat.relative_to(ROOT)),'discovered_terminal_breadth':final,'breadth_ladder':list(breadths),'trial_ladder':list(TRIALS),'rule':'actual terminal muscle count replaces the immediately preceding ordinary breadth milestone','arms':['NATIVE','OMNI_OVER_NATIVE'],'simultaneous':True,'omni_core':'FROZEN'}
(out/'MATRIX_CONTRACT.json').write_text(json.dumps(contract,indent=2))
for m in breadths:
 for n in TRIALS:
  cell=out/f'm{m}_n{n}';cmd=[sys.executable,str(ROOT/'organism/xpass21_organism_lab.py'),'--breadth',str(m),'--trials',str(n),'--steps',str(a.steps),'--chunk',str(a.chunk),'--out',str(cell)]
  if a.max_seconds and time.time()-t0>a.max_seconds: status.append({'breadth':m,'trials':n,'status':'NOT_RUN_TIME_BUDGET'});continue
  try: subprocess.run(cmd,cwd=ROOT,check=True);status.append({'breadth':m,'trials':n,'status':'PASS'})
  except subprocess.CalledProcessError as e:status.append({'breadth':m,'trials':n,'status':'ERROR','returncode':e.returncode})
(out/'MATRIX_STATUS.json').write_text(json.dumps(status,indent=2));print(json.dumps({'contract':contract,'status':status},indent=2))
