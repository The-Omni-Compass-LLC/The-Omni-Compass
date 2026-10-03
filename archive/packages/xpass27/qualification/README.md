# XPASS25 E3/E4 Qualification

This directory is the execution boundary for tomorrow's real plant. It never promotes evidence automatically.

E3 Kubernetes: preflight -> baseline/native -> WATCH(no writes) -> CLAIM1 -> write/readback -> workload/SLO -> restore/readback -> seal.

E4 NVIDIA: identify GPU -> capability preflight -> capture original power limit -> baseline workload -> CLAIM1 requested cap -> nvidia-smi write -> independent readback -> sample power.draw/util/temp -> integrate joules -> workload/SLO -> restore original cap -> restore readback -> seal.

A missing capability is OPEN/UNSUPPORTED, never simulated into a physical PASS.
