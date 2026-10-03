# Four plants. One governor. Four receipts.

OmniCompass is the process. It is not the plant. A plant is covered only when this repo can read that plant's meter and write that plant's lever on one clock, then restore the lever.

| Plant | Host this repo can use | Lever | Meter | Status in this package |
|---|---|---|---|---|
| Compute | GitHub `gpu-t4` runner, Kind on that same box | GPU power limit, and replica count if the API answers | `nvidia-smi`, pods | Runnable. Not claimed until `ONE_BOX_RECEIPT.json` exists from a job that left the queue. |
| Facility | Rack PDU and cooling on a machine this process can read | Rack cap or fan/valve setpoint | kW, inlet temp | Not hosted. Receipt fails closed. |
| Machine | Servo or PLC on a machine this process can read | Speed, torque, or local setpoint | position, current, fault | Not hosted. Receipt fails closed. |
| Grid | Feeder meter or battery on a machine this process can read | Charge rate or feeder cap | volts, amps, state of charge | Not hosted. Receipt fails closed. |

A buyer in one industry reads the matching receipt. The compute receipt does not become a robot number or a feeder number.

Upload this tree onto `xpass25-referee-repair`. Commit message for the compute job: `four plants [onebox]`. The other three workflows record `NOT_HOSTED` and exit 0. They do not pretend a run.
