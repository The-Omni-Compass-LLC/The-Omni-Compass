from fleet.harness import make_scenario
from fleet.sim import run
from omnicompass.adapter import mode_law
from dataclasses import replace
import numpy as np,json,csv
V=('web','multi','batch','gpu','gpu_always_on')
kw={'rho0': .7895443810698948,'rho_min':.6225850183568238,'kI':.08581008192001734,'kE':.07678218783820762,'kq':.9744622627083677,'down_band':4,'down_dwell':9,'down_after_add':12,'push_release':.06132989097496175,'margin':.11047447920962561,'U_gate':.47486096048869353,'up_max':2,'cap_min':.82,'guard_queue':.001}
law=replace(mode_law('throughput'),**kw)
metrics=('energy_kwh','work_completed','time_healthy','violation_backlog','violation_power','violation_heat','machines_started','machines_stopped','node_reversals')
out={'config':kw,'seed_base':610000,'seeds':30,'vessels':{}}; rows=[]
for v in V:
 B=[];O=[]
 for s in range(610000,610030):
  sc=make_scenario(v,s); b=run(sc,'k8s_hpa70_ca'); o=run(sc,'omni_single_throughput',omni_every=4,governor_law=law); B.append(b);O.append(o);rows += [b,o]
 bm={k:float(np.mean([x[k] for x in B])) for k in metrics};om={k:float(np.mean([x[k] for x in O])) for k in metrics}
 delta={k:om[k]-bm[k] for k in metrics}; out['vessels'][v]={'native':bm,'omni':om,'delta':delta}
 print(v,'E%',100*(om['energy_kwh']/bm['energy_kwh']-1),'Wpp',100*delta['work_completed'],'Hpp',100*delta['time_healthy'],'revD',delta['node_reversals'],flush=True)
open('XPASS6_WORK_PRESERVING_30.json','w').write(json.dumps(out,indent=2))
with open('XPASS6_WORK_PRESERVING_RUNS.csv','w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
