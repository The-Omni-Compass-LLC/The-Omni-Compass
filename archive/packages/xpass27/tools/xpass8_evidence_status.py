#!/usr/bin/env python3
from pathlib import Path
import json, shutil
ROOT=Path(__file__).resolve().parents[1]
items=[]
def add(name,status,evidence,paths,note):
    items.append(dict(name=name,status=status,evidence=evidence,paths=paths,note=note))
add('authenticated_python_cpp_core','PASS','V', ['cpp/src/canonical_engine.cpp','fixtures/CANONICAL_500_CASES.csv','fixtures/CANONICAL_500_EXPECTED.csv'], 'Frozen parity gate; see XPASS receipts.')
add('live_governor_canonical_evolution','IMPLEMENTED','L-code',['omnicompass/adapter.py','cpp/src/governor.cpp'], 'Live state evolution now uses bounded canonical FF+P microsteps rather than u=0.')
add('kubernetes_connector','IMPLEMENTED','L-code',['omni_controller/controller.py'], 'kubectl read/write, HPA target and node-pool hooks; execution evidence remains result-specific.')
add('cpu_frequency_connector','IMPLEMENTED','P-capable',['omni_controller/muscles.py','hardware/cpufreq.py','scripts/cpufreq_ceiling.sh'], 'Real sysfs/command connector with restore; physical energy claim requires hardware run.')
add('nvidia_power_connector','IMPLEMENTED','P-capable',['omni_controller/gpu_governor.py','scripts/gpu_paired.sh'], 'Real nvidia-smi power-limit path; physical paired evidence still OPEN unless a valid hardware result exists.')
physical=list((ROOT/'results/gpu').glob('github-*')) if (ROOT/'results/gpu').exists() else []
add('physical_gpu_paired_evidence','PASS' if physical else 'OPEN','P',[str(p.relative_to(ROOT)) for p in physical], 'No synthetic result is promoted to physical evidence.')
add('full_tower_128','PASS-SIMULATED','S',['muscles/FULL_TOWER_128.csv','cpp/src/muscle_fabric.cpp'], '128 contracts/pathways; not 128 production APIs.')
out={'schema':'xpass8-evidence-status-v1','items':items,'tools':{'kubectl':bool(shutil.which('kubectl')),'nvidia-smi':bool(shutil.which('nvidia-smi'))}}
print(json.dumps(out,indent=2))
