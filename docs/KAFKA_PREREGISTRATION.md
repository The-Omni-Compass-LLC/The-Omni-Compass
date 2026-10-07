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

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA.
