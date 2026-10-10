# Kafka: Omni-Compass on top of a consumer group's operator-set size, preregistered

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE`.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

Written 2026-10-07, before any counted run. The rules below were set on the tuning workload (run on one machine, never
counted) and are then applied unchanged to the untouched workloads; every row is reported, losses included; the readings
are the three-run readings of `docs/OMNI_V1.md`. The runner is `tools/run_kafka.py`, the workflow
`.github/workflows/kafka.yml`, the three-run table `tools/kafka_abc.py`. This is register row 26 (messaging).

## Why this benchmark

Kafka carries the messages between the services of most large systems. A consumer group reads a topic; how many consumers
it runs is a number an operator sets once, and it stays at that number through every quiet hour and every rush, spending
machines when there is nothing to read and falling behind when there is too much. That fixed number is the native
controller here, and Omni sits on top of it.

## What is someone else's

- **Apache Kafka 3.9.1** (the Apache Software Foundation, Apache License 2.0), one KRaft broker on the machine, its
  `server.properties` as shipped but for the log directory, fetched from Apache's archive and checked against Apache's
  own SHA-512; a topic of **8 partitions**, replication factor 1 (one broker).
- **kafka-python-ng** (the client, Apache License 2.0): the producer and the consumers; the group's own rebalance and
  offset commit, as shipped.
- **The machine:** a GitHub Actions runner (4 cores): broker, producer and consumers share it, as a small deployment
  does. There is no watt-meter on it.

Nothing here models a message system. Omni starts and stops consumers of the group, which is what an operator does, and
reads what the consumers themselves record.

## Arms

- **native:** the consumer group at the operator's count, **2 consumers**, for the whole run.
- **omni:** the same group, with the compass law (`omnicompass/compass_law.py`) on **one knob, the consumer count**,
  inside the cover [1, 8]: never under one consumer, never more consumers than partitions (an idle consumer by Kafka's own
  rule). Everything else is native's.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the group's own end-to-end latency: the mean, over the messages consumed in the last
  second, of the time from a message's production to the end of its handling. A second with nothing consumed while
  messages wait reads as the line (someone is waiting and no one is taking); nothing consumed and nothing waiting reads
  as calm (0).
- **Band.** From 0 to the response line, **500 ms**. The compass pulls the reading to 40% of the line (200 ms), the
  service profile of the Kubernetes adapter, with its usual gains (kp 1.0, response time 3 s because a consumer added or
  removed shows only after the group rebalances, smoothing 0.5, one decision a second).
- **Direction.** A positive force (the service slow) with messages waiting adds ceil(force / 0.10) consumers (full
  force adds ten, capped by the cover). A negative force (calm) with no message waiting gives back **one idle consumer a
  second** (a consumer that read nothing in the last second), and only after a five-second dwell since the last change.
- **Cushion.** A force inside ±0.05 moves nothing.
- **Fail up.** At 95% of the line every consumer the topic can use (8) is started at once; the compass then resumes.
- **One writer.** The consumers are the harness's own processes; nothing else starts or stops them.
- **Reset.** At the end of every omni arm the count is handed back to the operator's (2) and read back; the report says
  whether every arm was handed back.

Disclosed: a consumer added or removed makes the group rebalance, during which no partition is read for a moment; Omni
pays that cost every time it moves the knob, and the gauges below include it.

## The load

A producer offers messages at a rate stepping one notch at a time, **1 2 3 2 3 4 5 6 5 4 3 2 1 2 1**, 20 s a notch,
300 s an arm; the burst workload steps **1 6 1 8 1 6**. The base rate is set **once per workload before the counted
repetitions, in native mode**: 20 s of messages offered faster than the operator's two consumers can take give native's
capacity, and the peak notch offers nine tenths of it, so native is at its knee and not past it. Each message carries its
production time and a sequence number; its handling is a declared **service time of CPU** (the work the message is for:
1, 2 or 5 ms by workload), spent by the consumer before the message counts as handled. Both arms start from the operator's
two consumers after an 8 s settling period and alternate order between repetitions.

## Gauges (from the consumers' records, the group's lag, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: messages a second handled within 500 ms of production | **higher is better** (the product number) |
| throughput (messages a second) | higher is better |
| end-to-end latency p95, p99, median, mean | lower is better |
| consumer lag, most and mean messages waiting | lower is better |
| messages produced and never consumed | **any increase is WORSE** |
| consumers running, mean and most at once (the resources held) | lower is better (Omni will often hold more under load, and that reads WORSE) |
| host CPU busy share, CPU-seconds, CPU-seconds per 1,000 messages inside the line (the compass's own cost included) | lower is better |
| consumer changes written (the knob's moves) | shown, not judged |

Energy is not claimed beyond the host's CPU seconds (evidence class L: real software, no meter).

## Workloads

- **Tuning workload:** 2 ms of work a message, 256-byte messages, the standard steps. The band, the direction rule, the
  dwell and the reading above were set on it; nothing else is tuned. It is run and shown, and not counted.
- **Untouched workloads:** **light** (1 ms, 128 B, standard steps), **heavy** (5 ms, 1,024 B, standard steps), **burst**
  (2 ms, 256 B, steps 1 6 1 8 1 6).

## Runs

Each workload: three paired repetitions in one GitHub Actions job, the per-message records, the audit and the broker log
archived with the code. Three separate runs on the frozen engine (A, B, C); the table (`tools/kafka_abc.py`) reads
confirmed better or WORSE when all three runs move the same way with every 95% interval clear of zero, no difference
beyond the noise when a run's interval includes zero, and the runs disagree when clear runs point different ways.
`tests/test_run_kafka.py` and `tests/test_kafka_abc.py`, run by `verify.py`, prove the rules without a broker.

## What the tuning workload showed on one machine, said before the counted runs

One short repetition (5 s a notch) on the development machine: native's two consumers at their knee held a p95 of 429 ms
with up to 329 messages waiting; omni held a p95 of 12 ms with at most 45 waiting, handled 3% more messages inside the
line, and did so with a mean of 5.8 consumers against 2, at slightly fewer host CPU-seconds (117 against 123: idle consumers
polling cost CPU too). The expected shape of the counted result is therefore: latency and lag much better, consumers held
worse, CPU about even, and every arm handed back. The counted runs will show whatever they show.

## Amendment 2 (2026-10-09, declared before any run on it): the brain's own verdict on the group's size

**Why, and when.** Written after the counted set was read (`results/live/V3_KAFKA.md`: work inside the line +16% to +21%, p95 1.6 s
→ 9 to 14 ms, consumers 2 → 6 to 8 confirmed worse, host CPU worse on the light workload), at the founder's order of 9 October:
Omni need not be wired into every muscle; a knob that cannot prove it pays stays native and Omni only reads it. The brain must
decide that on the muscle itself, in real time, by a measurement.

The rule, the same in the five live harnesses (`tools/knob_verdict.py`, a wrapper around the frozen engine's own
verdict, `omnicompass/verdict.py`, which is unchanged: the engine stays Omni v3): **the knob starts in watch**, one wire out
and nothing written, and the compass's moves are clamped to the allowance a paired trial on the stack itself has earned. Two
directions from the operator's setting, each with its own allowance: **spend** (more of the resource) and **give back**
(less). A trial is one notch past the deepest step already allowed: the reference phase holds the knob at that deepest step
(the operator's setting at first) until 8 one-second samples are in, then the trial phase holds it one notch further for 8
more; the first 6 s after any change are not sampled. The judge is the engine's: the trial's median cost no higher
than the reference's within 2%, and no higher than the cost first measured at the operator's setting. The cost is one sample
a second from the stack's own readings: under the **resource objective** (the Omni index's preregistered reading, the
default) cost = the consumers running × the host's CPU busy share × the mean end-to-end latency of the messages consumed in the last second / the messages consumed inside the 500 ms line in the last second, so a step passes only if the service gained
outweighs the resource and CPU spent by the index's own arithmetic; under the **service objective** (`--objective service`)
cost = the mean end-to-end latency of the messages consumed in the last second / the messages consumed inside the 500 ms line in the last second, the resources shown and not judged. A spend step is tried only while the compass asks to spend
and messages are waiting (the lag is above zero); a give-back step only while the service is calm and a consumer is idle and nothing is waiting. A trial once started runs on until its
samples are in unless the service swings to the other direction's condition, when it is abandoned; a refused step is not
tried again for 60 s; a trial is started at most every 20 s. During a trial the knob stands at the phase's value whatever
the compass asks; between trials the compass moves it by its own law inside the allowance. The fail-up rule (every consumer at once at the wall) is clamped to the allowance like every other move. The settle after a change is 6 s, two of the group's time constants, because a consumer that joins rebalances the group before it consumes. Restoring the
operator's setting is always free. Every trial, allowance, refusal and abandonment is written to the audit (`cost`,
`cpu_share`, `verdict_phase`, `verdict_direction`, `allowed_low`, `allowed_high` on every line) and summed in the arm's
record (`verdict`: the objective, the state, the allowance, the counts, the events); the three-run table prints the
brain's verdict per workload and run. The counted runs on this amendment will use 30 s a notch (a whole trial inside one
notch of traffic), declared here; the native arm runs the same ladder. Nothing is typed in; the rule is in the code the
runs execute.

**Expected before the runs.** Under the resource objective the first consumer added under a queue pays: the queue drains, the
latency of the messages consumed falls by far more than one consumer in two costs, and the step is allowed; the next steps are
allowed while each still shortens the queue by more than it costs. The group is expected to reach 3 to 5 consumers at the peak
notches against 6 to 8 before, one notch a trial; p95 confirmed better but by less than 1.6 s → 10 ms, the lag confirmed better,
the consumers running confirmed worse by less than before, the host's CPU inside the noise. Under the service objective a
step or two more. Both readings are run: three runs each. The counted set stays in `docs/history` as the result of the rule
before this amendment.

**Dispatched (2026-10-10 01:28 and 01:29 UTC, commit `3aac0ab7`, Omni v3 by `tools/omni_version.py --commit`).** At the founder's order of
10 October that every benchmark be run again on the current code, native and omni, the counted runs on this amendment were
dispatched with `workloads=all`, `reps=3`, `step_s=30`: under the resource objective runs 38013300872 (A), 38013304929 (B) and 38013309420 (C), 01:28:23 to 01:28:31 UTC; under the service objective runs 38013371103 (A), 38013376137 (B) and 38013380640 (C), 01:29:31 to 01:29:40 UTC. The whole day's dispatch, run by run, is
`docs/RERUN_2026-10-10.md`. The expectation above stands as written before the runs; when they land the table is read from them
(`tools/kafka_abc.py`), the index, the wiring page and the benefit sheet are read again, and the set this one supersedes goes whole to
`docs/history`.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA.
