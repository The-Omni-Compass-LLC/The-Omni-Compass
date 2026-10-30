# Why the data stores read as they do on omni-v21: the causes, from their own files

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 30 October: "find out why they went one way or the other and tweak it and turn it and tune it to the
best possible way for an Omni Compass engine to interact with this as a system governor". The five data-store benchmarks
carry 33 of the 50 LOSS rows on the engine that stands (`docs/LOSS_LEDGER.md`). Every number below is printed from the raw
runs on the branch `raw` by `tools/store_causes.py` (its command is beside each table), and the model readings are class S,
our own model, never a benchmark result.

## 1. The verdict's gate refused the brain exactly when the store needed it

Each store's wire lets the compass move its knob only inside an allowance that a paired trial on the store has earned
(`tools/knob_verdict.py`, amendment 2 of 9 October). Two of the gate's rules met in every overload:

- The wall abandons every trial: at 95% of the line (the fail-up) every spend trial in progress ends unjudged.
- The fail-up is clamped to the allowance: "a fail-up never spends beyond the allowance".

A spend trial needs about ten seconds of holding at the old setting before it tries a new one. An overload reaches the wall
in about six. So the trial that would have earned the spend was always ended by the wall, and the wall's own reflex was then
held at the operator's setting by the allowance that trial never earned.

`python3 tools/store_causes.py gate run-40256717947 run-40279909158 run-40400868003 run-40254205224 run-40276907808 run-40400989005 run-40258018856 run-40281464587 run-40401032384`

| Store (the resource objective) | Seconds over its line, Omni-Compass's arms, three runs | Of them, the brain's own rule asked to go up and the verdict kept it from going there | Allowance at the end (the operator's setting first) |
|---|---:|---:|---|
| Kafka | 1,428 | 1,428 | 2 consumers in 29 of 36 arms; 3 or 4 in the rest |
| Redis | 4,581 | 4,426 | 64 MB in 12 of 36 arms; 72 or 80 MB in the rest |
| MySQL | 3,697 | 3,139 | 512 MB at the top in 24 of 45 arms; 640 MB in the rest |
| MongoDB | 32 | 21 | rarely over its line |
| PostgreSQL | 28 | 0 | rarely over its line |

How the trials ended (`python3 tools/store_causes.py trials RUN`): Kafka's run A, 12 of its 13 spend trials ended by the wall,
none allowed; Redis's run A, 62 of its 68 ended by the wall, 5 allowed. The service objective's runs show the same: Kafka
1,625 seconds over its line, every one refused. The objective is not the lock; the wall is.

## 2. Kafka: the hand-back gave back a consumer the load still needed

Each consumer change rebalances the whole group: every member stops until each has rejoined, and a member learns of a
rebalance at its next heartbeat (every 3 s, kafka-python's own default). Measured on every change made in calm
(`python3 tools/store_causes.py stalls .`):

| Change | Changes | The extra wait the messages saw (s) |
|---|---:|---|
| A consumer added | 41 | median 1.237 (quartiles 0.334 and 2.487; at most 3.346) |
| A consumer removed | 52 | median 2.578 (quartiles 1.598 and 2.858; at most 3.010) |

The hand-back of 25 October gives a consumer back 30 s after the last change once nothing waits beyond one poll round, with no
look at whether the members left can carry the arrivals. In the light workload the brain gave a consumer back, the removal's
2 to 3 s stall built a queue, the brain added it back 1 to 3 s later, and again 30 s on (run 40279909158, light, repetition 1:
removals at 310, 355, 413 and 444 s, each re-added within 3 s). That churn is where the light and heavy workloads' latency
LOSS rows come from.

## 3. Kafka: the keys land on six partitions, so a fourth consumer buys nothing

The harness's producer keys each message `str(seq % 8)`, and Kafka places a key by murmur2 (the model's own murmur2, on the branch v22-stores, checked
against Kafka's own test vectors). The eight keys land on six partitions: 6 and 7 two keys each, 2 and 5 none. Kafka's range
assignor then gives the members these shares of the load:

| Consumers | The busiest member's share | What the group sustains (μ, one member's rate) |
|---|---|---|
| 2 (native) | 5/8 | 1.6 μ: 792 a second at 2 ms of work; offered the burst's 880, the group serves 825 (the 5/8 member at μ, the 3/8 member its arrivals), as the runs read |
| 3 | 4/8 | 2.0 μ |
| 4 | 4/8 | 2.0 μ: no more than 3 |
| 5 to 8 | 2/8 | 4.0 μ |

A backlogged consumer serves 495 messages a second at 2 ms of work, 199 at 5 ms and 981 at 1 ms, in its own record
(`python3 tools/store_causes.py rate .`). The harness measured the group's "capacity" from a backlog it had filled first
(975 a second at 2 ms, which is 2 μ) and set each workload's peak at 90% of it. Under keyed arrivals two consumers keep up
with at most 1.6 μ (792 a second at 2 ms), so every peak offers about 111% of what the operator's two consumers keep up with. Both arms face the same peak: it is a fair
test of a governor, and the governor that adds the third consumer in time wins it. A wire that adds one consumer at a time
wastes the fourth, and the verdict's trials cannot tell why.

## 4. Five tables are two settings

Run C of all five resource-objective store tables (40400868003, 40401042132, 40400989005, 40400963499, 40401032384) ran at the
workflows' default of 20 s a notch; runs A and B at the counted 30 s (`scripts/reruns.txt`). A table mixing them is not one
benchmark run three times. Every store workflow's default is now the counted 30 s (`tests/test_audit_2026_10_30.py`), and on the
next engine every store table runs again at one setting.

## 5. Redis and MySQL: the cache was never allowed to grow

Redis's 95th percentile stands at 5.2 to 5.7 ms in both arms against its 2 ms line: a miss costs the trip to the store. Only a
larger cache cuts the misses, and the allowance held the cache at 64 to 80 MB (a mean of 62 to 66 MB held) while the working
set needs more than twice that. Under the resource objective a step must cut latency by more than the share of memory it adds;
on a cache's hit curve, which flattens as the cache grows, each step buys less than its share, so the trial refuses it even
when the trial is allowed to finish. MySQL's buffer pool shows the same gate (its allowance's top at 512 or 640 MB) while it
gives memory back where the service allows (the pool held down 4% to 22% in the burst and read-only workloads, GAIN).

## 6. The fix, the next version's, through the model gate first

**Kafka** (a candidate written on the study branch v22-stores: the wire's `Brain`, and the closed-loop model kafka_model.py,
every input set from these runs' own files; neither is on main until the model gate reads no LOSS):

- **The rate twin**: each partition's arrivals (the topic's log-end offsets, read from the broker once a second) placed on the
  members by the range assignor; one member's rate learned from a second in which the queue grew (the group consumed
  Σ min(load, μ), solved for μ); a change's own stall learned the same way, the heartbeat interval its bound before one is seen.
- **The reflex**: when the twin says the count cannot carry the arrivals and the backlog (its own and the one a change's stall
  would add) at nine tenths of a member's rate, the count goes at once to the smallest one that can, up to the partitions:
  never clamped by the allowance, which keeps judging the compass's own moves.
- **The hold**: handed back only to a count that carries the last 60 s's arrival peak at seven tenths of its rate, 30 s after
  the last change, in calm, in one move (one rebalance); never below the operator's count; the immune system's hand-back to
  native when Omni-Compass's count redlines, stuck, and native's twin reads lower (`omnicompass/immune.py`).

In the model, against omni-v21's own loop on the same seeds (class S):

| Notches | Seeds | Every workload |
|---|---|---|
| 30 s, the counted setting | development 101 to 108, and untouched 201 to 208 | no LOSS row; work inside the line GAIN (up 16% to 21%), the 95th percentile GAIN (down 92% to 98%), the 99th GAIN (down 57% to 81%), the most messages waiting at once GAIN (down 19% to 43%), consumers power given (up 42% to 71%) |
| 20 s, run C's setting | untouched 201 to 208 | one LOSS row: the burst's most messages waiting at once, up 30.6% inside the seeds' spread; every other row GAIN or power given |

The 20 s row is the physics of a change, not a tuning to be hidden: native's peak is the queue one notch grows (about 55 a
second, 1,100 in 20 s and 1,650 in 30 s); any added consumer costs one rebalance's worth of arrivals (880 a second × 1.24 s
median, about 1,100). It is on the next version's list with its cause.

**Redis and MySQL**: the same reflex principle (the wall never clamped by the allowance; a hold that never shrinks the cache
into the working set it carries), each through a closed-loop cache model set from its runs' own files before it lands.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
