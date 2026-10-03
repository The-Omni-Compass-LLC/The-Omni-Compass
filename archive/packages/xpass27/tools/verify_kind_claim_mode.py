#!/usr/bin/env python3
"""Fail closed if an Omni Kind audit does not prove the requested claim mode.
This verifies provenance only; it does not turn Kind's modeled energy into physical kWh.
"""
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser(); p.add_argument('audit'); p.add_argument('--expected',default='CLAIM1'); a=p.parse_args()
path=Path(a.audit); total=matched=missing=wrong=0
for no,line in enumerate(path.read_text().splitlines(),1):
    if not line.strip(): continue
    try: r=json.loads(line)
    except Exception: continue
    d=r.get('directive') or (r.get('decision') or {}).get('directive') or r.get('decision')
    if not isinstance(d,dict): continue
    # Only controller decisions/directives carrying u or demand are relevant.
    if not any(k in d for k in ('u_hold','demand','power_cap','claim_mode')): continue
    total+=1; m=d.get('claim_mode') or r.get('claim_mode')
    if m is None: missing+=1
    elif str(m).upper()!=a.expected.upper(): wrong+=1
    else: matched+=1
print(json.dumps({'audit':str(path),'expected':a.expected,'controller_records':total,'matched':matched,'missing':missing,'wrong':wrong},sort_keys=True))
if total==0 or missing or wrong or matched!=total: raise SystemExit(3)
