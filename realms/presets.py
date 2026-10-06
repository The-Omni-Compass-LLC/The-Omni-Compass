# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Parameter sets of the realm plants, fixed before any confirmation run (docs/REALMS_PREREGISTRATION.md).

One set per preset named in realms/catalog.csv. Each muscle runs its family's set at its own size: the work scale
(request rate, IT load, site load, process demand) is multiplied by 0.6 to 1.4, drawn from the muscle id, so the 16
muscles of a family are 16 differently sized plants. Values are round engineering figures for the class of machine,
not measurements of any product.

Two clocks:
  single     each plant on its own natural decision period and horizon (STEPS_SINGLE)
  organism   every plant on one shared 15 s decision clock for 240 steps (one hour), so they can be coupled
"""
from __future__ import annotations

import hashlib

STEPS_SINGLE = {"compute_pool": 720, "thermal_zone": 720, "energy_storage": 720, "motion_axis": 360,
                "process_loop": 720}
ORGANISM_DT = 15.0
ORGANISM_STEPS = 240
CAL_SEED = 999          # the calibration seed: sets declared power budgets from native draw; never a result seed

_CP = dict(dt=15.0, mu=50.0, slo_s=0.5, startup_steps=4, n0=6, n_min=2, n_max=80, p_idle=60.0, p_dyn=140.0,
           target=0.70, lam0=200.0, diurnal=0.35, period_steps=720, noise=0.08, burst_p=0.01, burst_max=1.0,
           queue_limit_s=30.0, stab_steps=20, calm=0.914, stress=0.627)

PRESETS = {
    # compute_pool -------------------------------------------------------------------------------------------
    "server": dict(_CP),
    "node": dict(_CP, ca=1, ca_unneeded_steps=40, mu=80.0, slo_s=1.0, startup_steps=12, p_idle=120.0, p_dyn=230.0, lam0=320.0),
    "cpu_host": dict(_CP, power_organ="cpufreq", mu=60.0, p_idle=80.0, p_dyn=170.0, lam0=240.0),
    "gpu": dict(_CP, power_organ="gpu", mu=8.0, slo_s=2.0, startup_steps=8, p_idle=60.0, p_dyn=240.0, lam0=40.0, n0=6),
    "gpu_batch": dict(_CP, power_organ="gpu", pausable=1, mu=8.0, slo_s=600.0, startup_steps=8, p_idle=60.0, p_dyn=240.0, lam0=40.0, diurnal=0.1,
                      burst_p=0.005, queue_limit_s=3600.0),
    "batch": dict(_CP, pausable=1, mu=20.0, slo_s=300.0, startup_steps=8, lam0=80.0, diurnal=0.2, queue_limit_s=3600.0),
    "fabric": dict(_CP, mu=100.0, slo_s=0.2, startup_steps=1, p_idle=20.0, p_dyn=30.0, lam0=400.0, network=1),
    "robot_fleet": dict(_CP, mu=0.05, slo_s=120.0, startup_steps=2, n0=8, n_max=60, p_idle=50.0, p_dyn=300.0,
                        lam0=1.0, queue_limit_s=1800.0),
    "qpu": dict(_CP, pausable=1, mu=2.0, slo_s=60.0, startup_steps=20, n0=3, n_min=1, n_max=12, p_idle=600.0, p_dyn=200.0,
                lam0=6.0, queue_limit_s=1800.0),
    "network": dict(_CP, mu=1000.0, slo_s=0.05, startup_steps=2, p_idle=15.0, p_dyn=10.0, lam0=4000.0, network=1),
    "storage": dict(_CP, mu=200.0, slo_s=0.05, startup_steps=2, p_idle=8.0, p_dyn=4.0, lam0=800.0),
    "database": dict(_CP, mu=30.0, slo_s=0.2, startup_steps=20, n0=4, p_idle=100.0, p_dyn=150.0, lam0=120.0),
    "commerce": dict(_CP, slo_s=1.0, startup_steps=6, burst_p=0.02, burst_max=1.5),
    "workflow": dict(_CP, pausable=1, mu=0.5, slo_s=60.0, lam0=4.0, queue_limit_s=1800.0),
    "ran": dict(_CP, mu=100.0, slo_s=0.05, startup_steps=4, n0=6, n_min=2, n_max=12, p_idle=300.0, p_dyn=500.0,
                lam0=350.0, diurnal=0.6, network=1),
    # thermal_zone --------------------------------------------------------------------------------------------
    "data_hall": dict(dt=60.0, sub=12, c_j_k=2.0e6, ua=500.0, q_it_w=150e3, it_amp=0.15, noise=0.03, units=6,
                      q_unit_w=40e3, p_unit_w=1.5e3, t_set=24.0, t_limit=27.0, calm=26.0, stress=22.0, t_out=25.0,
                      t_out_amp=7.0, start_frac=0.25, eta=0.45, approach=8.0, kp=40e3, ki=200.0),
    "building": dict(dt=60.0, sub=12, c_j_k=8.0e6, ua=2000.0, q_it_w=60e3, it_amp=0.4, noise=0.05, units=4,
                     q_unit_w=35e3, p_unit_w=0.8e3, t_set=22.0, t_limit=25.0, calm=24.0, stress=21.0, t_out=30.0,
                     t_out_amp=6.0, start_frac=0.25, eta=0.40, approach=10.0, kp=15e3, ki=60.0),
    # energy_storage ------------------------------------------------------------------------------------------
    "microgrid": dict(dt=120.0, e_wh=400e3, p_batt_w=100e3, eta_rt=0.90, load_w=120e3, load_amp=0.4, peak_h=19.0,
                      pv_w=150e3, p_lim_w=140e3, reserve=0.2, calm=0.5, stress=0.1, flex=0.15, soc0=0.5,
                      start_h=0.0, noise=0.05),
    "ups": dict(dt=120.0, e_wh=50e3, p_batt_w=200e3, eta_rt=0.92, load_w=150e3, load_amp=0.1, peak_h=15.0,
                pv_w=0.0, p_lim_w=180e3, reserve=0.6, calm=0.8, stress=0.5, flex=0.05, soc0=0.9, start_h=0.0,
                noise=0.03, backup=True),   # a UPS reserve is held for an outage, not for a peak: never Omni's lever
    "facility": dict(dt=120.0, e_wh=1000e3, p_batt_w=300e3, eta_rt=0.90, load_w=400e3, load_amp=0.25, peak_h=17.0,
                     pv_w=200e3, p_lim_w=450e3, reserve=0.2, calm=0.5, stress=0.1, flex=0.10, soc0=0.5,
                     start_h=0.0, noise=0.04),
    # motion_axis ---------------------------------------------------------------------------------------------
    "robot_joint": dict(dt_dec=1.0, dt=0.004, J=0.05, b=0.02, kt=0.5, R=0.8, tau_max=12.0, p_idle=20.0, D=1.5,
                        v_max=3.0, a_max=15.0, dwell=0.2, tol=0.01, e_max=0.05, c_th=300.0, r_th=1.2, t_amb=30.0,
                        t_lim=90.0, kp=400.0, kd=8.0, ki=100.0, i_max=0.05, task_rate=0.6, dist=2.0,
                        load_bias=0.0, regen=0.0, deadline_s=30.0),
    "flight_axis": dict(dt_dec=2.0, dt=0.01, J=2.0, b=0.5, kt=0.53, R=0.15, tau_max=40.0, p_idle=30.0, D=10.0,
                        v_max=3.0, a_max=2.0, dwell=2.0, tol=0.1, e_max=0.5, c_th=400.0, r_th=0.2, t_amb=25.0,
                        t_lim=80.0, kp=30.0, kd=12.0, ki=10.0, i_max=0.5, task_rate=0.05, dist=4.0,
                        load_bias=19.6, regen=0.0, deadline_s=120.0),
    "reaction_wheel": dict(dt_dec=10.0, dt=0.02, J=50.0, b=0.01, kt=0.05, R=2.0, tau_max=0.2, p_idle=5.0, D=0.5,
                           v_max=0.02, a_max=0.004, dwell=5.0, tol=0.002, e_max=0.01, c_th=100.0, r_th=5.0,
                           t_amb=20.0, t_lim=70.0, kp=12.5, kd=40.0, ki=0.5, i_max=0.01, task_rate=0.01,
                           dist=0.002, load_bias=0.0, regen=0.0, deadline_s=600.0),
    "ev_traction": dict(dt_dec=5.0, dt=0.02, J=1600.0, b=25.0, kt=40.0, R=0.05, tau_max=6000.0, p_idle=300.0,
                        D=400.0, v_max=14.0, a_max=2.0, dwell=10.0, tol=1.0, e_max=3.0, c_th=5000.0, r_th=0.05,
                        t_amb=25.0, t_lim=120.0, kp=800.0, kd=1800.0, ki=20.0, i_max=5.0, task_rate=1.0 / 60.0,
                        dist=300.0, load_bias=0.0, regen=0.6, deadline_s=300.0),
    # process_loop --------------------------------------------------------------------------------------------
    "process": dict(dt=10.0, sub=10, tau=120.0, K=1.0, theta=5.0, sp=0.6, mid=0.6, half=0.2, calm=0.5, stress=0.6,
                    u_max=2.0, aff=3.0, p_max_w=30e3, kp=2.0, ki=0.02, d_mean=0.3, d_amp=0.3, noise=0.02),
    "water": dict(dt=10.0, sub=10, tau=30.0, K=1.0, theta=3.0, sp=1.0, mid=1.0, half=0.15, calm=0.92, stress=1.0,
                  u_max=3.0, aff=3.0, p_max_w=75e3, kp=1.5, ki=0.05, d_mean=0.6, d_amp=0.4, noise=0.03),
    "chamber": dict(dt=10.0, sub=10, tau=300.0, K=1.0, theta=10.0, sp=1.0, mid=1.0, half=0.02, calm=0.995,
                    stress=1.0, u_max=3.0, aff=1.0, p_max_w=20e3, kp=6.0, ki=0.02, d_mean=0.5, d_amp=0.05,
                    noise=0.002),
    "feeder_voltage": dict(dt=10.0, sub=10, tau=5.0, K=1.0, theta=1.0, sp=1.0, mid=1.0, half=0.05, calm=0.97,
                           stress=1.0, u_max=2.0, aff=1.0, p_max_w=500e3, kp=1.0, ki=0.5, d_mean=0.1, d_amp=0.5,
                           noise=0.005),
    # Omni v2, wave 4 of the realm study (docs/REALMS_PREREGISTRATION.md): thirteen new families, one preset each. Round
    # engineering figures for the class of machine, as above; none is a measurement of any product.
    # thermal_zone: a hospital's critical rooms (tighter band, smaller plant than a data hall)
    "hospital": dict(dt=60.0, sub=12, c_j_k=6.0e6, ua=1500.0, q_it_w=80e3, it_amp=0.25, noise=0.04, units=4,
                     q_unit_w=40e3, p_unit_w=1.0e3, t_set=21.0, t_limit=24.0, calm=22.5, stress=20.5, t_out=28.0,
                     t_out_amp=6.0, start_frac=0.25, eta=0.40, approach=10.0, kp=20e3, ki=80.0),
    # compute_pool: clinical systems (imaging archives, records, interface engines: a strict line, a daytime swing)
    "clinical": dict(_CP, mu=40.0, slo_s=1.0, startup_steps=6, n0=4, p_idle=80.0, p_dyn=150.0, lam0=120.0, diurnal=0.5,
                     burst_p=0.015, burst_max=1.2),
    # compute_pool: a container terminal's cranes and vehicles taking moves from a queue (a move is a job; pausable)
    "port": dict(_CP, pausable=1, mu=0.02, slo_s=1800.0, startup_steps=2, n0=8, n_min=2, n_max=40, p_idle=15e3,
                 p_dyn=150e3, lam0=0.1, diurnal=0.3, burst_p=0.01, burst_max=1.0, queue_limit_s=7200.0),
    # process_loop: pumps and pressure in a field or a greenhouse (a daily cycle, a fast loop)
    "irrigation": dict(dt=10.0, sub=10, tau=60.0, K=1.0, theta=5.0, sp=1.0, mid=1.0, half=0.2, calm=0.9, stress=1.0,
                       u_max=3.0, aff=3.0, p_max_w=90e3, kp=1.2, ki=0.03, d_mean=0.5, d_amp=0.5, noise=0.03),
    # process_loop: a pipeline segment (line pack is slow, compressor power goes as the cube)
    "pipeline": dict(dt=30.0, sub=10, tau=600.0, K=1.0, theta=30.0, sp=1.0, mid=1.0, half=0.1, calm=0.95, stress=1.0,
                     u_max=2.5, aff=3.0, p_max_w=5e6, kp=1.5, ki=0.005, d_mean=0.5, d_amp=0.3, noise=0.02),
    # process_loop: a grinding and flotation circuit (mill power goes roughly as the square of the drive setting)
    "mill": dict(dt=10.0, sub=10, tau=120.0, K=1.0, theta=10.0, sp=1.0, mid=1.0, half=0.15, calm=0.93, stress=1.0,
                 u_max=2.0, aff=2.0, p_max_w=10e6, kp=2.0, ki=0.02, d_mean=0.5, d_amp=0.25, noise=0.03),
    # process_loop: a district heating network (half an hour of thermal inertia, a strong daily swing)
    "district_heat": dict(dt=60.0, sub=10, tau=1800.0, K=1.0, theta=120.0, sp=1.0, mid=1.0, half=0.15, calm=0.9,
                          stress=1.0, u_max=2.0, aff=2.0, p_max_w=20e6, kp=1.0, ki=0.001, d_mean=0.5, d_amp=0.6,
                          noise=0.02),
    # process_loop: a generating unit's steam, speed or gate loop (fast, tight band, near-linear fuel-to-power)
    "turbine": dict(dt=5.0, sub=10, tau=20.0, K=1.0, theta=2.0, sp=1.0, mid=1.0, half=0.05, calm=0.97, stress=1.0,
                    u_max=2.0, aff=1.2, p_max_w=300e6, kp=3.0, ki=0.2, d_mean=0.4, d_amp=0.3, noise=0.01),
    # process_loop: a plant of grid-support inverters or turbines (very fast, the resource itself the disturbance)
    "inverter": dict(dt=5.0, sub=10, tau=2.0, K=1.0, theta=0.2, sp=1.0, mid=1.0, half=0.05, calm=0.97, stress=1.0,
                     u_max=1.5, aff=1.0, p_max_w=5e6, kp=2.0, ki=1.0, d_mean=0.3, d_amp=0.5, noise=0.02),
    # process_loop: a GMP batch reactor, fermenter or food process (slow, very tight band, small disturbance)
    "batch_reactor": dict(dt=10.0, sub=10, tau=600.0, K=1.0, theta=20.0, sp=1.0, mid=1.0, half=0.05, calm=0.98,
                          stress=1.0, u_max=3.0, aff=1.0, p_max_w=200e3, kp=4.0, ki=0.01, d_mean=0.5, d_amp=0.1,
                          noise=0.005),
    # motion_axis: a train's traction axis (the EV axis scaled tenfold in inertia, torque and gains; the same dynamics)
    "rail_traction": dict(dt_dec=5.0, dt=0.02, J=16000.0, b=250.0, kt=400.0, R=0.005, tau_max=60000.0, p_idle=3000.0,
                          D=2500.0, v_max=12.0, a_max=1.0, dwell=20.0, tol=2.0, e_max=5.0, c_th=50000.0, r_th=0.01,
                          t_amb=25.0, t_lim=150.0, kp=8000.0, kd=18000.0, ki=50.0, i_max=10.0, task_rate=1.0 / 300.0,
                          dist=3000.0, load_bias=0.0, regen=0.7, deadline_s=600.0),
    # motion_axis: a ship's propulsion shaft (large inertia, heavy drag, a standing hull load)
    # (Omni v3: twelve speed changes an hour of 200 rad instead of four of 600, so a one-hour run holds enough moves for a
    # count; a move of 126 s plus 30 s of dwell at one every 300 s is a duty of 0.52)
    "marine_propulsion": dict(dt_dec=10.0, dt=0.05, J=50000.0, b=3000.0, kt=2000.0, R=0.005, tau_max=500000.0,
                              p_idle=50000.0, D=200.0, v_max=10.0, a_max=0.05, dwell=30.0, tol=2.0, e_max=5.0,
                              c_th=50000.0, r_th=0.002, t_amb=30.0, t_lim=120.0, kp=25000.0, kd=56000.0, ki=100.0,
                              i_max=50.0, task_rate=1.0 / 300.0, dist=50000.0, load_bias=10000.0, regen=0.0,
                              deadline_s=1200.0),
    # motion_axis: an elevator hoist (a stiff position loop, a counterweighted load, regeneration on the way down)
    "elevator_hoist": dict(dt_dec=1.0, dt=0.005, J=20.0, b=2.0, kt=8.0, R=0.3, tau_max=2500.0, p_idle=300.0, D=60.0,
                           v_max=8.0, a_max=1.5, dwell=8.0, tol=0.02, e_max=0.2, c_th=2000.0, r_th=0.3, t_amb=30.0,
                           t_lim=110.0, kp=3000.0, kd=500.0, ki=50.0, i_max=1.0, task_rate=1.0 / 40.0, dist=100.0,
                           load_bias=0.0, regen=0.5, deadline_s=120.0),
}

# the parameter that sets each plant's size
SCALE_KEY = {"compute_pool": ("lam0",), "thermal_zone": ("q_it_w", "q_unit_w", "c_j_k", "ua", "kp", "ki", "p_unit_w"), "energy_storage": ("load_w", "pv_w"),
             "motion_axis": ("task_rate",), "process_loop": ()}


def muscle_scale(muscle_id: str) -> float:
    h = int(hashlib.sha256(muscle_id.encode()).hexdigest()[:8], 16) / 0xFFFFFFFF
    return 0.6 + 0.8 * h


def params_for(row: dict, organism: bool = False) -> dict:
    """The parameter set one muscle's plant runs with."""
    P = dict(PRESETS[row["preset"]])
    s = muscle_scale(row["muscle_id"])
    for key in SCALE_KEY[row["template"]]:
        P[key] = P[key] * s
    if row["template"] == "compute_pool":
        P["n0"] = max(P["n_min"], int(round(P["n0"] * s)))
    if row["template"] == "energy_storage":
        P["p_lim_w"] *= s
        P["e_wh"] *= s
        P["p_batt_w"] *= s
    if row["template"] == "process_loop":
        P["p_max_w"] *= s
    if organism:
        if row["template"] in ("compute_pool", "thermal_zone", "energy_storage", "process_loop"):
            ratio = ORGANISM_DT / P["dt"]
            P["dt"] = ORGANISM_DT
            if "sub" in P:
                P["sub"] = max(1, int(round(P["sub"] * ratio)))
            if "startup_steps" in P:
                P["startup_steps"] = max(1, int(round(P["startup_steps"] / ratio)))
                P["stab_steps"] = max(1, int(round(P["stab_steps"] / ratio)))
                if "ca_unneeded_steps" in P:
                    P["ca_unneeded_steps"] = max(1, int(round(P["ca_unneeded_steps"] / ratio)))
                P["period_steps"] = ORGANISM_STEPS * 4
            if row["template"] == "energy_storage":
                P["start_h"] = P["peak_h"] - 0.5                   # the hour around the site's peak
        else:
            P["dt_dec"] = ORGANISM_DT
    return P
