#!/usr/bin/env python3
import argparse,json,pathlib,sys
p=argparse.ArgumentParser(); p.add_argument('--rep',required=True); p.add_argument('--arms',default='native watch omni'); p.add_argument('--expected-mode',default='CLAIM1'); a=p.parse_args()
out={'schema':'omni.kind.e3.validation.v1','rep':a.rep,'expected_mode':a.expected_mode,'arms':{},'valid':True,'claim_limits':['Kind is E3 software-plant evidence.','Energy is a declared model, not metered electricity.','No Karpenter/Turbonomic/StormForge/CAST product comparison is established.']}
for arm in a.arms.split():
 d=pathlib.Path(f'bench-{arm}-{a.rep}'); r={'folder':str(d),'errors':[]}
 if not d.is_dir(): r['errors'].append('missing_folder')
 else:
  c=d/'run_contract.json'
  if not c.exists(): r['errors'].append('missing_run_contract')
  else:
   x=json.loads(c.read_text()); r['contract']=x
   if x.get('evidence_class')!='E3_SOFTWARE_PLANT': r['errors'].append('wrong_evidence_class')
   if x.get('energy_semantics')!='DECLARED_KIND_POWER_MODEL_NOT_METERED_KWH': r['errors'].append('wrong_energy_semantics')
   if arm!='native' and x.get('claim_mode')!=a.expected_mode: r['errors'].append('wrong_claim_mode')
  if arm=='watch':
   f=d/'omni_writes.txt'
   if not f.exists(): r['errors'].append('missing_watch_write_receipt')
   elif 'writes executed: 0' not in f.read_text(): r['errors'].append('watch_executed_write')
  if arm!='native':
   aud=d/'audit.jsonl'
   if not aud.exists(): r['errors'].append('missing_audit')
   else:
    modes=[]
    for line in aud.read_text(errors='replace').splitlines():
     try: z=json.loads(line)
     except: continue
     dd=z.get('decision') if isinstance(z.get('decision'),dict) else z.get('directive') if isinstance(z.get('directive'),dict) else None
     if dd and dd.get('claim_mode'): modes.append(dd['claim_mode'])
    r['audit_claim_modes']=sorted(set(modes))
    if not modes or set(modes)!={a.expected_mode}: r['errors'].append('audit_claim_mode_not_uniform')
 if r['errors']: out['valid']=False
 out['arms'][arm]=r
print(json.dumps(out,indent=2,sort_keys=True))
sys.exit(0 if out['valid'] else 3)
