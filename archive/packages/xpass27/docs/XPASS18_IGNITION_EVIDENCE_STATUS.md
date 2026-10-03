# XPASS18 Ignition / Evidence Status

## Canonical boundary
The six-state/eight-line CLAIM1 engine is frozen. XPASS18 does not introduce a new law. The live engineering chain remains CLAIM1 held-u -> admissibility -> bounded muscle directive -> writer -> readback -> attribution -> work/SLO -> restoration receipt.

## Fresh merged simulator execution
The public four-arm entrypoint now executes the XPASS18 merged allocator, not the older XPASS14 C7 path. C7 retains the XPASS15 request-sizer-off finding and cap envelope and adds the XPASS18 braking policy: down dwell 8 and a 10% voluntary-down budget. No proprietary comparator product is executed.

Fresh 30-scenario execution used seeds 20260929..20260958 on the frozen common software plant.

| Arm | modeled energy kWh | healthy | balanced CE | starts | stops |
|---|---:|---:|---:|---:|---:|
| C1 HPA+CA model | 1.8352 | 0.98984 | 501.7 | 16.4 | 18.0 |
| C3 Karpenter-doc replica | 1.4936 | 0.99229 | 665.2 | 18.7 | 22.9 |
| C6 action-surface proxy | 0.9429 | 0.99169 | 9617.1 | 114.7 | 121.9 |
| C7 Omni CLAIM1 merged | 1.6762 | 0.99595 | 298.6 | 7.1 | 9.7 |

C7 minus C3 paired bootstrap 95% intervals:
- modeled energy +0.18251 [0.10458, 0.28286]: adverse for C7
- healthy +0.003657 [0.001273, 0.006366]: favorable for C7
- balanced CE -366.67 [-461.16, -276.12]: favorable for C7
- node starts -11.67 [-15.67, -8.30]: favorable for C7
- node stops -13.20 [-17.53, -9.33]: favorable for C7

C7 minus C1: modeled energy, health, CE, starts and stops all had favorable non-zero paired intervals in this 30-scenario population.

C7 minus C6: C7 used more modeled energy but had better health and dramatically lower motion/CE.

This is a simulator result only. Energy is a declared plant model, not a meter reading. C3 is a documented-behavior replica, not the Karpenter product. C6 is not IBM Turbonomic. No global superiority claim follows.

## 500-scenario confirmation
Attempted on this environment. It exceeded the available execution window and produced no completed result. Status: OPEN_TIMEOUT_NOT_A_RESULT. Do not infer 500-run performance from the 30-run table.

## Kind CLAIM1-23
Kind is E3 software-plant evidence. It is a real Kubernetes API/scheduler/HPA/metrics-server environment on container workers, not physical node power evidence. Its energy score is modeled. Kind-23 can test API-loop behavior, Watch zero-write discipline, restoration, SLO/p95, audit claim_mode=CLAIM1, and controller overhead. It cannot establish hardware kWh or a win over Karpenter-the-product.

Required entrypoint:
`REP=23 bash scripts/kind_claim1_paired.sh`

Acceptance hygiene:
- every Omni audit record identifies CLAIM1
- Watch write count = 0
- restoration clean
- p95/SLO and controller CPU published
- modeled power explicitly labeled
- Set22 remains historical pre-canonical-evolve evidence

Status: OPEN_EXTERNAL_SOFTWARE_PLANT.

## NVIDIA physical
NVIDIA is E4 device evidence only when preflight qualifies the card and requested/enforced authority, attribution, device joules, useful work, SLO and restoration are all receipted. `nvidia-smi -pl` is board power authority, not node power and not wall power. flock is one-writer protection; watchdog restores the snapshot.

Status: OPEN_EXTERNAL_PHYSICAL_PLANT.

## Evidence classes
E0 formal specification; E1 deterministic/unit/parity; E2 common-plant simulation; E3 independent software plant; E4 independent physical plant/meter. Evidence never auto-promotes across classes.
