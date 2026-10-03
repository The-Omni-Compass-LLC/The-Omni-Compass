# XPASS20: Breadth x Population Collective Qualification

Primary comparison: **NATIVE** versus **OMNI_OVER_NATIVE**. Omni is supervisory. It does not replace the declared muscles.

Default breadth ladder: `1,10,100,500,640` simultaneously active canonical muscle contracts.
Default population ladder: `1000,10000,100000,1000000` concurrent governed trajectories.

Each matrix cell runs every requested muscle concurrently on one shared simulation clock. At breadth 640, all 640 canonical contracts are represented at the same time. Trajectories share queue, network, electrical/resource and thermal pressures so the system result is collective, not a post-hoc sum of isolated scores.

For each paired cell, NATIVE and OMNI_OVER_NATIVE start from the same deterministic seed, initial conditions, workload and disturbance stream. The native specialist command is the actuator in both arms. In the Omni arm, frozen CLAIM1 supervises native targets/authority envelopes.

Run:

    ./RUN_XPASS20_GITHUB.sh

Or custom scale:

    python collective/run_xpass20_matrix.py --muscle-ladder 1,10,100,500,640 --population-ladder 1000,10000,100000,1000000 --steps 24

Evidence semantics: E2 simulation. Resource index is modeled, not physical kWh. Population is simulated governed trajectories, not physical machines. Only completed cells count. Existing Kind E3 and NVIDIA E4 harnesses remain separate physical/software-plant evidence lanes in the master repository.
