# Why the stacks were late more often on 2026-10-02, and the knob that settles it

Model runs (evidence S), organism Compute / AI / Cloud (345 muscles), seeds 6000-6004, 240 steps, native against the
compass law on every muscle, handed back at 90%. Each change is Omni against native. Late: time over the service line
(lower is better). Energy: lower is better (less spent). Work: higher is better.

## The two knobs that moved between commit `c908054` (the first card run) and `2a9285d`

| Code | HPA target lever | Machine headroom (RELEASE_MARGIN) | Late (pp) | Energy | Work |
|---|---|---:|---:|---:|---:|
| `c908054` (first card run), seeds 6000-6002 | Omni may loosen it to 0.95 | none (1.0) | +0.25 (WORSE: late more often) | -0.34% (better) | same |
| today, the target lever put back alone | Omni may loosen it to 0.95 | 0.6 | +0.06 (WORSE) | -0.49% (better) | same |
| today, the headroom removed alone | held at the operator's | 1.0 | +0.16 (WORSE) | -0.28% (better) | same |
| **today (both)** | **held at the operator's** | **0.6** | **-0.03 (better: late less often)** | **-0.10% (better)** | same |

Both knobs traded time over the line for energy. Loosening the operator's HPA target runs fewer pods, so bursts
wait; handing a machine back with no headroom leaves the next burst to wait for a machine to boot.

## The headroom dial (target held at the operator's)

| RELEASE_MARGIN | Late, mean (pp) | Late, worst seed (pp) | Energy |
|---:|---:|---:|---:|
| 0.5 | -0.033 (better) | -0.019 (better) | -0.086% |
| **0.6** | **-0.030 (better)** | **-0.013 (better)** | **-0.099%** |
| 0.7 | -0.019 (better) | +0.002 (WORSE) | -0.129% |
| 0.8 | +0.012 (WORSE) | +0.037 (WORSE) | -0.173% |
| 0.9 | +0.059 (WORSE) | +0.081 (WORSE) | -0.229% |
| 1.0 | +0.160 (WORSE) | +0.198 (WORSE) | -0.275% |

0.6 is the setting that spends the least energy with no seed late more often than native (band first). From 0.7 up
at least one seed is late more often, which the founder's rule does not allow. The dial is the trade: every step
past 0.6 buys energy with lateness.

Reproduce: the scratch script in this file's commit message, or run `realms.compass_arm` with `RELEASE_MARGIN` set and
the HPA target lever on or off.
