# Grok patch on XPASS14 — what Claude/ChatGPT must not flatten

Parent: XPASS14_REFEREE_HARVEST_READY (SHA 11ea011f…).
This overlay does **not** close Kind-23 or NVIDIA.

## Code that landed here

1. `omnicompass/disruption_budget.py` — Karpenter-shaped voluntary down cap.
2. `adapter.py` — budget window on `node_delta < 0`; `FLEET_MODE.down_dwell` **1 → 8** (the 1 was a churn gun).
3. `scripts/gpu_paired.sh` — `pl_set` + `flock /var/lock/omni-gpu-pl` around every `-pl`.
4. `omnicompass/ce_score.py` — five CE sweeps, no single trophy.

## What the 30-run already proved (do not overwrite)

C7 beats C3 on modeled energy/health and **loses CE**. Fix is dwell+budget, not a new ODE.
C6 is a **stress proxy**, not IBM.

## Still OPEN

```
python tournament/frozen_four_arm_tournament.py --scenarios 500 --seed 20260929 --out results/four_arm_500
REP=23 bash scripts/kind_claim1_paired.sh
sudo bash scripts/gpu_paired.sh
```

Re-run **four_arm_30** after this dwell/budget change. If CE still >> C3, raise `disrupt_budget_pct` down or `disrupt_when_empty_only=True`. If health CI dies, you over-braked.

## Claim hygiene (frozen)

No “best governor in the world.” No promotion E2 → E4.
