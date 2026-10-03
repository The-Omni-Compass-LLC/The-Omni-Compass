# XPASS19 Collective Breadth x Population Lab

This overlay preserves the frozen scalar CLAIM1 engine and the historical 128-muscle artifacts. `muscles/FULL_TOWER_640.csv` adds the 640-contract qualification vocabulary. It does **not** relabel the 640 contracts as proven integrations.

## What this harness tests

One common coupled plant and one workload/disturbance seed are run under separate arms. The plant couples queue/load, resource pressure, network pressure, electrical pressure and thermal pressure so the score is system-level, not 640 unrelated toy scores.

Arms: native-only; Watch (Omni computes, zero writes); HPA+CA; documented Karpenter behavior replica; documented OpenShift autoscaling behavior replica; Turbonomic action-surface proxy; Borg policy behavior replica; Omni direct CLAIM1; Omni-over-native CLAIM1.

Comparator labels are intentionally narrow. The repository does not contain Google Borg, Red Hat OpenShift, IBM Turbonomic or Karpenter proprietary internals. Product names are not victory claims.

## Run

```bash
python collective/scale_lab.py --population 1000000 --steps 24 --out results/xpass19_1m
python collective/run_scale_ladder.py --populations 640,6400,64000,640000,1000000,2000000,10000000 --steps 24
```

There is no software maximum population. Memory/CPU/time are the practical boundary. A billion or trillion requested trajectories are not an achievement unless the run actually completes under the declared envelope.

## Evidence semantics

Simulation = E2. Kind/Kubernetes live software plant = E3. Physical NVIDIA = E4. Modeled resource index is not kWh. Live GPU joules require physical telemetry. Kind worker parking is not physical node-off.

## Collective pass criteria

Every arm reports successful work, model resource use, work/resource, health fraction, control effort, writes, authority violations, restoration, throughput, memory, final global queue and thermal state. Watch must issue zero writes. Omni authority violations must remain zero. Restoration must verify.
