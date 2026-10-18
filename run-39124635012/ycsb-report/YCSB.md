# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,894 | -0.1% | -4.24 to 0.0775 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% | -3.78 to -0.0276 | LOSS |
| latency, 95th percentile (ms) | 0.32 | 0.324 | +1.1% | -0.00807 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.495 | 0.501 | +1.3% | -0.00964 to 0.0223 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.2 | +0.9% | -0.00644 to 0.0102 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -17.5 to 5.48 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 416 | -0.7% | -17.3 to 11.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 712,771 | 722,465 | +1.4% | -18,203 to 37,591 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.188 | -1.4% | -0.0997 to 0.0946 | EVEN, no difference beyond the noise |
| host CPU-seconds | 331 | 325 | -1.8% | -211 to 199 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.248 | 0.244 | -1.8% | -0.158 to 0.149 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -12.8 to 11.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,894 | -0.0% | -10.5 to 9.28 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.514 | 0.509 | -0.9% | -0.0147 to 0.00537 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.681 | 0.675 | -1.0% | -0.0468 to 0.0335 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.232 | -1.2% | -0.00757 to 0.00175 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -16.5 to -2.86 | GAIN |
| bytes in the cache, mean (MB) | 403 | 393 | -2.5% | -23.2 to 3.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 265,838 | 273,648 | +2.9% | -12,225 to 27,843 | shown, not judged |
| host CPU busy (share of the run) | 0.17 | 0.155 | -8.9% | -0.0838 to 0.0535 | EVEN, no difference beyond the noise |
| host CPU-seconds | 115 | 103 | -10.3% | -66.5 to 42.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.194 | -10.3% | -0.126 to 0.0811 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,918 | 2,918 | +0.0% | -5.64 to 6.06 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,921 | +0.0% | -5.43 to 5.88 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.23 | 0.228 | -0.9% | -0.00697 to 0.00297 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.391 | 0.391 | -0.1% | -0.00659 to 0.00592 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.151 | 0.15 | -0.6% | -0.022 to 0.0202 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -4.45 to 0.169 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 415 | -1.0% | -18.5 to 10.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 688,929 | 716,978 | +4.1% | -101,180 to 157,277 | shown, not judged |
| host CPU busy (share of the run) | 0.169 | 0.13 | -22.9% | -0.127 to 0.0493 | EVEN, no difference beyond the noise |
| host CPU-seconds | 311 | 229 | -26.5% | -269 to 104 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.171 | -26.5% | -0.201 to 0.0776 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,614 | 5,653 | +0.7% | -141 to 220 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,631 | 5,671 | +0.7% | -141 to 222 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.325 | +0.4% | -0.00154 to 0.0042 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.509 | 0.509 | +0.1% | -0.0196 to 0.0203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.21 | -2.6% | -0.0162 to 0.00521 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -24.7 to 9.68 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 409 | -1.1% | -20.5 to 11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 676,402 | 686,695 | +1.5% | -68,773 to 89,360 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.235 | +3.7% | -0.0449 to 0.0616 | EVEN, no difference beyond the noise |
| host CPU-seconds | 406 | 424 | +4.3% | -102 to 138 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.157 | 0.162 | +3.4% | -0.0399 to 0.0505 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `8b902df8d857`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,931 | 2,929 | -0.1% | -3.69 to 0.665 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,935 | -0.1% | -3.46 to 0.278 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.225 | 0.23 | +2.2% | -0.0147 to 0.0247 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.395 | 0.398 | +0.6% | -0.0259 to 0.0306 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.105 | 0.104 | -1.3% | -0.00592 to 0.00324 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -18.8 to 5.55 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 414 | -0.9% | -14.5 to 6.56 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 688,175 | 701,871 | +2.0% | -11,949 to 39,342 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.13 | -10.0% | -0.0567 to 0.0278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 266 | 235 | -11.8% | -123 to 60.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.199 | 0.176 | -11.8% | -0.0921 to 0.0452 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
