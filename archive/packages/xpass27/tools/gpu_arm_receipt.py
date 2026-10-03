#!/usr/bin/env python3
"""Build one machine-readable physical-arm receipt from independent bench files.
It summarizes evidence; it does not decide the cross-repetition scientific verdict."""
import argparse,csv,json,math,pathlib
from gpu_reps import arm as parse_arm

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('dir'); ap.add_argument('--arm',required=True,choices=['native','watch','omni']); ap.add_argument('--gpu',type=int,default=0); ap.add_argument('--slo-ms',type=float,required=True); ap.add_argument('--start-limit-w',type=float,required=True); a=ap.parse_args(); d=pathlib.Path(a.dir)
 g,c=parse_arm(d,[a.gpu]); req=list(csv.DictReader(open(d/'requests.csv'))); ok=[float(r['latency_ms']) for r in req if r.get('ok')=='1']; p95=sorted(ok)[min(len(ok)-1,int(.95*len(ok)))] if ok else math.nan
 cpu=float((d/'omni_cpu_seconds.txt').read_text()) if (d/'omni_cpu_seconds.txt').exists() else 0.0
 audit=[]
 if (d/'audit.jsonl').exists():
  for line in (d/'audit.jsonl').read_text().splitlines():
   try: audit.append(json.loads(line))
   except Exception: pass
 uvals=[x.get('directive',{}).get('u_hold') for x in audit if isinstance(x.get('directive'),dict) and x.get('directive',{}).get('u_hold') is not None]
 acts=[x.get('actuator') for x in audit if isinstance(x.get('actuator'),dict)]
 enforced_match=bool(acts) and all((a0.get('enforced_w') is not None and a0.get('requested_w') is not None and abs(float(a0['enforced_w'])-float(a0['requested_w'])) <= 1.0) for a0 in acts if a0.get('rc',0)==0)
 health={'foreign_writer':any('foreign_writer' in x for x in audit),'thermal_slowdown':any(x.get('thermal_hold') or x.get('health',{}).get('thermal_slowdown') for x in audit),'hw_power_brake':any(x.get('health',{}).get('hw_power_brake') for x in audit),'application_clocks_conflict':False}
 work=len(ok); gpu_j=g['energy, GPU device counter (J)']; integrated_j=g['energy, GPU (J)']; wall_j=g['energy, whole machine at the wall (J)']
 energy=gpu_j if not math.isnan(gpu_j) else integrated_j
 r={'schema':'omnicompass.gpu_arm_receipt.v1','arm':a.arm,'work_unit':'served_request','work_units':work,'slo_ms':a.slo_ms,'p95_ms':p95,'slo_ok':bool(ok and p95<=a.slo_ms),
    'energy_device_j':None if math.isnan(gpu_j) else gpu_j,'energy_integrated_draw_j':None if math.isnan(integrated_j) else integrated_j,'energy_wall_j':None if math.isnan(wall_j) else wall_j,
    'energy_cpu_package_j':None if math.isnan(g['energy, CPU package (J)']) else g['energy, CPU package (J)'],'omni_cpu_seconds':cpu,
    'work_per_kj':work/(energy/1000.0) if energy and energy>0 else None,'watch_pl_writes':c['writes'] if a.arm=='watch' else 0,'omni_pl_writes':c['writes'] if a.arm=='omni' else 0,
    'restore_ok':bool(c['restored']),'limits_seen_w':c['limits_seen'],'enforced_seen_w':c['enforced_seen'],'start_limit_w':a.start_limit_w,
    'actuator':{**(c.get('actuator',{}) or {}),'enforced_matches_requested':enforced_match},'health':{**(c.get('health',{}) or {}),**health},'samples':c.get('samples',0),
    'canonical_u_provenance':{'present':bool(uvals),'samples':len(uvals),'last_u_hold':uvals[-1] if uvals else None}}
 (d/'ARM_RECEIPT.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n'); print(json.dumps({'arm':a.arm,'receipt':str(d/'ARM_RECEIPT.json'),'slo_ok':r['slo_ok'],'restore_ok':r['restore_ok']}))
if __name__=='__main__': main()
