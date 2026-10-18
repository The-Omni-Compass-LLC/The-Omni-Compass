# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | The whole tower, every muscle once, 1,000 copies: native | The whole tower, every muscle once, 1,000 copies: omni | The four stacked, duplicates kept, 1,000 copies: native |
|---|---:|---:|---:|
| response time (ms), 95th percentile | 4104 | 203.8 | 5824 |
| response time (ms), 99th percentile | 6372 | 257.8 | 7974 |
| time over the response line (% of samples) | 64.02 | 0.1645 | 73.17 |
| failed requests (%) | 22.25 | 0 | 58.33 |
| HPA replicas, mean | 9.886 | 9.894 | 9.889 |
| pods started | 5 | 4.667 | 4 |
| worker nodes in service, mean | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 541.8 | 540.8 | 551.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 541.8 | 540.8 | 551.3 |
| CPU used with Omni's own (cores), mean | 4.263 | 4.188 | 4.932 |
| host CPU busy, the real machine under kind (%) | 69.33 | 69.92 | 78.57 |
| organism work | 5.629e+13 | 5.629e+13 | 1.067e+14 |
| organism energy (J) | 6.387e+13 | 6.375e+13 | 9.605e+13 |
| organism time over the line (% of steps) | 2.722 | 2.714 | 2.568 |
| organism work per energy | 0.8814 | 0.883 | 1.111 |
| organism behind its window (s) | 802.5 | 408.3 | 5584 |

## Each organism: omni against native, paired by repetition

### The whole tower, every muscle once, 1,000 copies: better on 6, worse on 1 (organism work), inside the noise on 5; OFF THE CLOCK in 1 of 3 repetitions (the organism ended up to 2,392 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

3 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4104 | 203.8 | -95.0% | -6804 to -996.3 | better |
| response time (ms), 99th percentile | 6372 | 257.8 | -96.0% | -8153 to -4075 | better |
| time over the response line (% of samples) | 64.02 | 0.1645 | -99.7% | -99.52 to -28.19 | better |
| failed requests (%) | 22.25 | 0 | -100.0% | -115.6 to +71.11 | better (inside the noise) |
| HPA replicas, mean | 9.886 | 9.894 | +0.1% | -0.01703 to +0.0345 | WORSE (inside the noise) |
| pods started | 5 | 4.667 | -6.7% | -1.768 to +1.101 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.779e-16 to +1.57e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 541.8 | 540.8 | -0.2% | -6.524 to +4.494 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 541.8 | 540.8 | -0.2% | -6.524 to +4.494 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 4.263 | 4.188 | -1.8% | -0.6641 to +0.5131 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.33 | 69.92 | +0.9% | -6.106 to +7.288 | shown, not judged (more or less is not better by itself) |
| organism work | 5.629e+13 | 5.629e+13 | -0.0% | -9.426e+07 to -9.426e+07 | WORSE |
| organism energy (J) | 6.387e+13 | 6.375e+13 | -0.2% | -1.168e+11 to -1.168e+11 | better |
| organism time over the line (% of steps) | 2.722 | 2.714 | -0.3% | -0.00788 to -0.00788 | better |
| organism work per energy | 0.8814 | 0.883 | +0.2% | +0.001614 to +0.001614 | better |
| organism behind its window (s) | 802.5 | 408.3 | -49.1% | -2104 to +1315 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 1,000 copies

No paired arms.

## Not in this run

- Compute / AI / Cloud
- Physics / Robotics / Autonomous
- Energy / Facility / Industrial
- Distribution / Specialized


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
