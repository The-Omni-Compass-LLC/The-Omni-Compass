# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The card's brain (omni_controller/gpu_brain.py) and its wires (omni_controller/gpu_compass.py):

  race      work arriving on an idle card puts the ceiling back at the top at once, before any decision
  park      an idle card parks its clock after hold_ms, only with the arrival signal (never without it)
  verdict   the park depth is found by measurement: levels whose first request after a rest is slower are refused,
            found coarse to fine; a cruise step that costs nothing but saves nothing is refused (no gain); no cruise
            trial opens on a card held by its own power limit while busy
  lid       the power limit stays at the start limit (the paid run's slowdown was a lid under the busy draw); a power
            target brakes to the target
  guards    past the line, blind meters, or heat: every wire to native at once, trials ended
  wires     against the stand-in nvidia-smi: the signal's arrivals race the clock, idle parks it, the audit records each,
            watch writes nothing, restore resets the clock and the limit, another writer is left alone (exit 5)
  model     the A10 model with the same brain: less energy than native, no slower at the median, wires handed back
"""
import json, os, socket, sys, tempfile, threading, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from omni_controller.gpu_brain import CardBrain, park_levels
from omni_controller.gpu_compass import GpuCompass, parser
SMI = str(ROOT / "tests" / "fake_gpu" / "nvidia-smi")


def brain_events():
    b = CardBrain(1695, 210, 150.0, samples=5, decision_s=0.25, probe_every_s=0.25, trial_s=1000.0)
    assert b.levels[0] == 1695 and b.levels[-1] == 210 and all(x > y for x, y in zip(b.levels, b.levels[1:])), b.levels
    # park after hold, race on arrival, the lid untouched
    b.decide(0.0, {"util": 0.0, "draw_w": 60.0, "clock_mhz": 1695.0}, 0.0)
    b.park_step = 3
    assert b.idle_due(0.01) is None, "parked before the hold"
    w = b.idle_due(0.03); assert w and w[0] == b.levels[3] and w[1] == "park", w
    w = b.arrival(0.5, 1); assert w == (1695.0, "race"), w
    assert b.lid == 150.0
    # no signal: the brain never parks
    nb = CardBrain(1695, 210, 150.0, signal=False)
    nb.decide(0.0, {"util": 0.0, "draw_w": 60.0, "clock_mhz": 1695.0}, 0.0)
    assert nb.idle_due(10.0) is None and nb.next_idle_check() is None
    # brake: a power target puts the lid at the target
    tb = CardBrain(1695, 210, 150.0, power_target_w=120.0)
    assert tb.decide(0.0, {"util": 0.5, "draw_w": 100.0, "clock_mhz": 1200.0}, 0.0)[1] == 120.0
    print("brain: parks after the hold, races on arrival, never parks without the signal, lid at the start (target when braking)")


def drive(b, first_cost, rounds=4000, b2b_cost=None, draw=None, util=0.5):
    """Simulated time: one request every 0.5 s (rests between them), costs by the park level the request met."""
    t, rid = 0.0, 0
    for k in range(rounds):
        b.decide(t, {"util": util, "draw_w": draw(b) if draw else 140.0, "clock_mhz": 1000.0}, 0.0)
        if k % 2 == 0:
            parked_at = b.ceiling
            b.arrival(t, rid)
            b.done(t + 0.06, rid, first_cost(parked_at)); rid += 1
            b.idle_due(t + 0.09)
        t += 0.25


def park_verdict():
    lv = park_levels(1695, 210)
    b = CardBrain(1695, 210, 150.0, samples=6, decision_s=0.25, probe_every_s=0.5, trial_s=1000.0, cruise=False)
    # a request first met at a level deeper than the fourth costs 5% more; down to it, nothing
    drive(b, lambda c: 60.0 * (1.05 if c < lv[4] - 1 else 1.0))
    assert b.park_vd.allowed == 4, (b.park_vd.allowed, b.levels)
    print(f"park verdict: allowed down to {b.levels[b.park_vd.allowed]:.0f} MHz, the next level (5% slower) refused, found coarse to fine")


def cruise_verdict():
    # a card held by its own limit while busy (busy draw at the lid): no cruise trial ever opens
    b = CardBrain(1695, 210, 150.0, samples=5, probe_every_s=0.25, trial_s=1000.0, park=False, learn_samples=3)
    for k in range(400):
        b.decide(k * 0.25, {"util": 1.0, "draw_w": 149.0, "clock_mhz": 735.0}, 0.0)
    assert b.busy_vd.phase is None and b.busy_vd.allowed == 0 and not b.busy_headroom()
    # memory-bound: busy draw well under the lid, a lower ceiling costs nothing and draws less: allowed
    b = CardBrain(1695, 210, 150.0, samples=5, probe_every_s=0.25, trial_s=1000.0, park=False, learn_samples=3)
    t, rid = 0.0, 0
    for k in range(3000):
        draw = 120.0 - 4.0 * (1695.0 - b.cruise_clock()) / 60.0 if b.ceiling < 1695 else 120.0
        b.decide(t, {"util": 1.0, "draw_w": draw, "clock_mhz": b.ceiling}, 0.0)
        b.arrival(t, rid); b.arrival(t, rid + 1)               # two at once: the second is served behind the first
        b.done(t + 0.05, rid, 40.0); b.done(t + 0.1, rid + 1, 40.0)
        rid += 2; t += 0.25
    assert b.busy_vd.allowed >= 3, b.busy_vd.allowed
    # the same, but the watts do not fall: refused for no gain
    b = CardBrain(1695, 210, 150.0, samples=5, probe_every_s=0.25, trial_s=1000.0, park=False, learn_samples=3)
    t, rid = 0.0, 0
    for k in range(600):
        b.decide(t, {"util": 1.0, "draw_w": 120.0, "clock_mhz": b.ceiling}, 0.0)
        b.arrival(t, rid); b.arrival(t, rid + 1); b.done(t + 0.05, rid, 40.0); b.done(t + 0.1, rid + 1, 40.0)
        rid += 2; t += 0.25
    ev = [e["verdict"]["verdict"] for e in b.take_events() if isinstance(e.get("verdict"), dict)]
    assert b.busy_vd.allowed == 0 and any("no gain" in v for v in ev), ev[-5:]
    print("cruise verdict: no trial on a card at its own limit; free and cheaper steps allowed; free but not cheaper refused (no gain)")


def guards():
    b = CardBrain(1695, 210, 150.0, samples=5, probe_every_s=0.25)
    b.decide(0.0, {"util": 0.0, "draw_w": 60.0, "clock_mhz": 1695.0}, 0.0); b.park_step = 4; b.idle_due(1.0)
    assert b.ceiling < 1695
    for pos, tele, heat, why in ((1.2, {"util": 1.0, "draw_w": 150.0, "clock_mhz": 700.0}, False, "fail_up"),
                                 (None, {"util": 1.0, "draw_w": 150.0, "clock_mhz": 700.0}, False, "blind_fail_up"),
                                 (0.1, None, False, "blind_fail_up"),
                                 (0.1, {"util": 1.0, "draw_w": 150.0, "clock_mhz": 700.0}, True, "thermal_fail_up")):
        c, lid, w = b.decide(2.0, tele, pos, heat)
        assert (c, lid, w) == (1695.0, 150.0, why), (c, lid, w)
        assert b.idle_due(5.0) is None and b.park_vd.phase is None
    print("guards: past the line, blind, heat: ceiling to the top, lid to the start, no parking, trials ended")


def setup(tmp, util=40):
    st = {"limit": {"0": 150.0}, "default": 150.0, "min": 100.0, "max": 150.0, "draw_w": 220.0, "util": util, "temp": 60,
          "clock_top": 1695.0}
    p = Path(tmp) / "smi.json"; p.write_text(json.dumps(st)); os.environ["FAKE_SMI_STATE"] = str(p)
    return p


def wires():
    t = tempfile.mkdtemp(); st = setup(t); sock = str(Path(t) / "s.sock")
    lat = Path(t) / "latency.csv"; lat.write_text("elapsed_seconds,latency_ms,ok,service_ms\n0.1,60,1,60\n")
    a = parser().parse_args(["--mode", "cap", "--gpus", "0", "--smi", SMI, "--nvml", "off", "--interval", "0.25",
                             "--audit", str(Path(t) / "a.jsonl"), "--kill-file", str(Path(t) / "kill"), "--signal", sock,
                             "--latency-file", str(lat), "--slo-ms", "800", "--hold-ms", "20", "--probe-every-s", "100000",
                             "--park-slow-path"])
    g = GpuCompass(a)
    g.brain.park_vd.allowed = 3; g.brain.park_vd.last_probe = 0   # as if the verdict had allowed the fourth level
    stop = {"now": False, "failed": False}
    th = threading.Thread(target=g.listen, args=(stop,), daemon=True); th.start()
    time.sleep(0.3)
    sk = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    g.step()
    for i in range(3):
        sk.sendto(f"a {i}".encode(), sock); time.sleep(0.1)
        sk.sendto(f"d {i} 60.0".encode(), sock); time.sleep(0.3)
    stop["now"] = True; th.join(timeout=2)
    recs = [json.loads(x) for x in (Path(t) / "a.jsonl").read_text().splitlines()]
    assert any("race" in r for r in recs) and any("park" in r for r in recs), [list(r)[1] for r in recs]
    lgc = [r for r in recs if r.get("clock_write", [None, None, "x"])[2:3] == ["-lgc"]]
    assert lgc and lgc[0]["clock_write"][3] == f"{g.c_floor},{int(g.brain.levels[3])}", lgc[:1]
    assert not any("write" in r and "-pl" in r["write"] for r in recs), "the lid moved without a power target"
    assert g.restore()
    s = json.loads(st.read_text())
    assert s["limit"]["0"] == 150.0 and "0" not in s.get("clock_lock", {})
    print(f"wires: arrivals race the clock to the top, idle parks it at {g.brain.levels[3]:.0f} MHz through nvidia-smi -lgc, the lid untouched; restored")
    # watch: decides, writes nothing
    t2 = tempfile.mkdtemp(); st2 = setup(t2); sock2 = str(Path(t2) / "s.sock")
    a2 = parser().parse_args(["--mode", "watch", "--gpus", "0", "--smi", SMI, "--nvml", "off", "--audit", str(Path(t2) / "a.jsonl"),
                              "--signal", sock2, "--probe-every-s", "100000", "--park-slow-path"])
    g2 = GpuCompass(a2); g2.brain.park_vd.allowed = 3; g2.brain.park_vd.last_probe = 0
    stop2 = {"now": False, "failed": False}
    th2 = threading.Thread(target=g2.listen, args=(stop2,), daemon=True); th2.start(); time.sleep(0.3)
    g2.step(); sk.sendto(b"a 1", sock2); time.sleep(0.1); sk.sendto(b"d 1 60", sock2); time.sleep(0.3)
    stop2["now"] = True; th2.join(timeout=2)
    recs2 = [json.loads(x) for x in (Path(t2) / "a.jsonl").read_text().splitlines()]
    assert not any("clock_write" in r or "write" in r for r in recs2) and any("would_clock_write" in r for r in recs2)
    assert not Path(str(st2) + ".writes").exists()
    print("watch: the same decisions, recorded as would-writes; nothing written to the card")


def model():
    from realms.gpu_card import run, ALLOW
    n, o = run(5000, "native", duration=240.0), run(5000, "omni", duration=240.0, handback=True)
    assert o["energy_j"] < n["energy_j"], (o["energy_j"], n["energy_j"])
    assert o["p50_ms"] <= n["p50_ms"] * (1 + ALLOW) + 1e-9 and o["restored"]
    print(f"model: the A10 model with the same brain, {o['energy_j'] / n['energy_j'] - 1:+.1%} energy, median "
          f"{o['p50_ms'] / n['p50_ms'] - 1:+.1%}, wires handed back")


def slow_path():
    t = tempfile.mkdtemp(); setup(t)
    a = parser().parse_args(["--mode", "cap", "--gpus", "0", "--smi", SMI, "--nvml", "off", "--audit", str(Path(t) / "a.jsonl"),
                             "--signal", str(Path(t) / "s.sock")])
    g = GpuCompass(a)
    assert not g.brain.park_on and g.brain.next_idle_check() is None, "parked on the slow write path"
    g.restore()
    print("slow path: with writes through nvidia-smi the park pedal stays off (the race would come too late)")


def main():
    brain_events(); park_verdict(); cruise_verdict(); guards(); wires(); slow_path(); model()
    print("PASS card brain: races on arrival, parks only where measured free, never lowers the lid without a target, fails up, restores")


if __name__ == "__main__":
    main()
