# XPASS 4: canonical brain -> nervous pathway -> muscle fabric

The authoritative source is `reference/OMNI-COMPASS_CONTROL_CORE_ENGINE_ORIGINAL_TOC_NEW_FULLBLEED_COVER_FIXED-2.py` (SHA-256 `c527df2d...c531d52`).

XPASS 4 freezes the Python-generated draw stream rather than asking C++ to imitate NumPy's RNG. This is deliberate: mechanism parity is tested on identical inputs, so RNG implementation differences cannot masquerade as dynamics differences.

Pipeline:

`Python source -> exact state/parameter fixtures -> C++ eight-line derivatives -> FF+P bounded ZOH command -> RK4 k1/k2/k3/k4 -> 10 microsteps -> macro state -> nervous authority -> muscle pathway -> bounded simulated endpoint -> readback -> receipt -> restore`

The parity executable compares 500 final trajectories and, for the first 20 trajectories, every pre-state, raw command, held command, four RK4 derivative vectors, and accepted post-state at all 4,000 microsteps.

The full-tower endpoint layer remains simulated. This is intentional. Mathematical identity and connector/physical evidence are separate gates.
