# The 945 muscles, realm by realm

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

Generated from `realms/catalog.csv` (rules: `tools/realms_catalog.py`; the v2 build: `tools/realms_catalog_v2.py`). Every realm's organism is its own families plus the **shared spine** (the infrastructure every real stack runs on), so the realm counts add to more than the tower. Each muscle is followed by the one knob Omni may hold on it.

## The shared spine: 257 muscles, in all four realms

### Cloud VM & Capacity (21; plant: compute_pool, node)
vm_count [capacity], vm_size [capacity], vm_start_stop [capacity], vm_migrate [capacity], instance_family [capacity], asg_min [capacity], asg_max [capacity], spot_mix [capacity], reservation_mix [capacity], zone_selection [capacity], region_selection [capacity], architecture_selection [capacity], accelerator_selection [capacity], boot_disk_class [capacity], placement_group [capacity], interruption_response [capacity], target_tracking_policy [setpoint], scaling_cooldown_warmup [capacity], vm_cpu_cap_by_priority [admission], predictive_scaling [capacity], instance_refresh [capacity]

### Container Resources (23; plant: compute_pool, server)
cpu_request [capacity], cpu_limit [capacity], memory_request [capacity], memory_limit [capacity], ephemeral_storage [capacity], hugepages [capacity], io_weight [setpoint], pids_limit [capacity], memory_high [capacity], memory_reclaim [capacity], swap_limit [capacity], cgroup_io_max [capacity], cpu_weight [setpoint], cpu_quota [admission], cpuset [capacity], runtime_class [capacity], in_place_resize [capacity], namespace_quota [admission], default_limits [capacity], memory_hard_limit [capacity], memory_protection [capacity], io_latency_target [setpoint], freeze [admission]

### Cooling, Chillers & Thermodynamics (18; plant: thermal_zone, data_hall)
supply_air_temperature [setpoint], return_air_target [setpoint], coolant_supply_temperature [setpoint], coolant_flow [capacity], pump_speed [capacity], fan_speed [capacity], chiller_setpoint [setpoint], compressor_authority [power], cooling_tower_fan [capacity], cooling_capacity [capacity], rack_thermal_budget [power], gpu_thermal_envelope [setpoint], cpu_thermal_envelope [setpoint], thermal_workload_migrate [admission], thermal_load_shed [admission], server_fan_speed [capacity], economiser [capacity], chiller_plant_supervisory_control_rl_with_safety_layer [capacity]

### Host CPU & Memory (23; plant: compute_pool, cpu_host)
cpufreq_min [power], cpufreq_max [power], rapl_package_power [power], uncore_frequency [power], energy_perf_preference [power], cpu_idle_policy [power], memory_bandwidth [capacity], numa_balance [capacity], irq_affinity [capacity], llc_allocation [capacity], memory_pressure_gate [admission], page_reclaim_rate [capacity], transparent_hugepages [capacity], core_online_offline [capacity], thermal_throttle_policy [power], host_power_profile [power], frequency_governor [power], turbo_boost [capacity], dram_power_limit [power], swappiness_reclaim [capacity], core_packing [capacity], per_pod_cpu_frequency_range_and_c_state_access [power], uncore_frequency_per_node [power]

### Kubernetes Placement & Scheduling (20; plant: compute_pool, server)
node_selector [capacity], node_affinity [capacity], pod_anti_affinity [capacity], topology_spread [capacity], numa_placement [capacity], gpu_topology [capacity], storage_locality [capacity], network_locality [capacity], taint_toleration [setpoint], priority_class [admission], preemption_policy [admission], device_claim [capacity], failure_domain_spread [capacity], scheduler_backoff [admission], gang_admission [admission], deschedule [capacity], scheduler_scoring_strategy [capacity], scheduler_plugin_weights [setpoint], scheduling_gates [admission], cpu_manager [capacity]

### Kubernetes Workload Scaling (31; plant: compute_pool, server)
replicas [capacity], hpa_cpu_target [setpoint], hpa_memory_target [setpoint], hpa_custom_target [setpoint], vpa_apply [capacity], scale_to_zero [capacity], keda_threshold [admission], rollout_rate [capacity], max_surge [capacity], max_unavailable [capacity], deployment_pause_resume [admission], rollout_abort [admission], pod_eviction [admission], pdb_policy [capacity], scheduler_queue_priority [admission], api_priority_fairness [admission], hpa_min_replicas [capacity], hpa_max_replicas [capacity], hpa_scale_down_stabilisation_window [setpoint], hpa_scale_up_stabilisation_window [setpoint], hpa_scaling_rate_policies [capacity], hpa_policy_selection [capacity], hpa_tolerance [capacity], hpa_sync_period [capacity], vpa_minmax_allowed_resources [capacity], keda_polling_interval [setpoint], rollout_progress_deadline [admission], rollout_readiness_delay [capacity], unhealthy_pod_eviction_policy [admission], graceful_termination [capacity], probes [capacity]

### NVIDIA GPU Hardware (19; plant: compute_pool, gpu)
gpu_allocate [capacity], gpu_power_limit [power], gpu_sm_clock [power], gpu_memory_clock [power], gpu_persistence_mode [capacity], gpu_compute_mode [capacity], mig_mode [capacity], mig_geometry [capacity], gpu_timeslice [capacity], gpu_mps [capacity], gpu_quarantine [admission], gpu_reset [capacity], gpu_thermal_limit [power], gpu_ecc_response [capacity], gpu_job_power_budget [admission], application_clocks [power], gpu_temperature_target [setpoint], sync_boost [capacity], target_clocks [power]

### Network Routing & Switching (19; plant: compute_pool, network)
lb_weight [setpoint], route_weight [setpoint], rate_limit [admission], bandwidth_limit [capacity], qos_class [capacity], connection_limit [admission], failover_route [capacity], nic_rate_limit [admission], nic_queue_count [capacity], queue_discipline [capacity], congestion_control [capacity], egress_budget [admission], ingress_budget [admission], ecmp_weight [setpoint], path_selection [capacity], network_isolation [admission], nic_interrupt_coalescing [capacity], nic_ring_size [capacity], port_link_power [power]

### Node Fleet & Karpenter-Class Control (24; plant: compute_pool, node)
node_desired [capacity], node_pool_min [capacity], node_pool_max [capacity], node_provision [capacity], node_cordon [admission], node_drain [admission], node_consolidate [capacity], node_replace [capacity], node_shutdown [capacity], node_power_on [capacity], nodepool_weight [setpoint], disruption_budget [admission], consolidation_policy [capacity], consolidate_after [capacity], expire_after [capacity], capacity_class [capacity], scale_down_utilisation_threshold [admission], scale_down_unneeded_time [capacity], scale_down_delay_after_add [capacity], expander [capacity], node_pool_limits [capacity], kubelet_eviction_thresholds [admission], kubelet_reserved_resources [capacity], max_pods_per_node [capacity]

### Observability & Telemetry (9; plant: compute_pool, server)
collector_memory_limit [capacity], export_concurrency [admission], cardinality_budget [admission], retention_window [setpoint], remote_write_queue [capacity], telemetry_shed [admission], metric_scrape_interval [setpoint], batching [capacity], per_pod_energy_attribution [capacity]

### PDU, UPS & Electrical Distribution (18; plant: energy_storage, ups)
server_power_cap [power], rack_power_cap [power], pdu_branch_power_limit [power], pdu_outlet_control [capacity], ups_operating_mode [capacity], ups_charge_rate [power], ups_discharge_rate [power], phase_balance [capacity], load_transfer [admission], reactive_power_target [setpoint], voltage_target [setpoint], generator_dispatch [capacity], electrical_isolation [admission], breaker_trip_gate [admission], ups_shutdown_battery_test [capacity], hierarchical_power_budget_row_pdu_switchboard_controllers [power], priority_aware_capping_throttle_low_priority_first [power], power_oversubscription_with_prediction [power]

### Reliability, Security & Recovery (12; plant: compute_pool, server)
restart [capacity], rollback [capacity], traffic_divert_recovery [capacity], degraded_mode [capacity], actuator_freeze [admission], workload_isolate [admission], credential_rotation_gate [admission], policy_enforcement [capacity], rate_abuse_gate [admission], fault_domain_isolate [admission], backup_trigger [capacity], kill_switch [admission]

### Storage Block/File/Object (20; plant: compute_pool, storage)
volume_size [capacity], iops_limit [capacity], throughput_limit [capacity], replica_count [capacity], storage_tier [capacity], volume_placement [capacity], snapshot_trigger [capacity], rebalance [capacity], recovery_rate [capacity], backfill_rate [capacity], compaction_pressure [capacity], cache_allocation [capacity], object_replication [capacity], erasure_code_profile [capacity], storage_admission [admission], degraded_storage_gate [admission], scrub_schedule [capacity], io_scheduler [capacity], disk_power_spin_down [power], lifecycle_tiering [capacity]

## Realm 1: Compute / AI / Cloud: 173 own muscles + the spine = 430 in its organism

### AI Inference Serving (24; plant: compute_pool, gpu)
model_replicas [capacity], model_route_weight [setpoint], model_load [capacity], model_unload [capacity], model_instance_count [capacity], continuous_batching [capacity], max_batch_size [capacity], batch_queue_delay [capacity], inference_concurrency [admission], inference_max_tokens [capacity], kv_cache_budget [admission], prefix_cache_budget [admission], speculative_decode_budget [admission], model_precision [power], inference_priority [admission], inference_slo_gate [admission], autoscaling_target_concurrency_qps [admission], scale_to_zero_panic_window [setpoint], request_priority_levels [admission], kv_cache_swap_space [capacity], chunked_prefill [capacity], tensor_parallel_degree [capacity], disaggregated_prefill_decode [capacity], lora_adapter_load [capacity]

### AI Training (18; plant: compute_pool, gpu_batch)
training_workers [capacity], global_batch_size [capacity], microbatch_size [capacity], gradient_accumulation [capacity], data_parallelism [capacity], tensor_parallelism [capacity], pipeline_parallelism [capacity], expert_parallelism [capacity], checkpoint_interval [setpoint], checkpoint_trigger [capacity], training_preempt [admission], training_gang_size [capacity], elastic_worker_count [capacity], straggler_mitigation [capacity], training_precision [power], compute_comm_overlap [capacity], activation_checkpointing [capacity], dataloader_workers [capacity]

### Cross-Cluster, Multi-Region & Edge (15; plant: compute_pool, node)
multi_cluster_dispatch [capacity], region_dispatch [capacity], zone_dispatch [capacity], edge_dispatch [capacity], cloud_capacity_class [capacity], workload_migrate_region [capacity], data_residency_gate [admission], latency_region_gate [admission], cost_region_gate [admission], carbon_region_gate [admission], global_failover [capacity], federation_quota [admission], cross_cluster_replication [capacity], edge_offload [capacity], global_admission [admission]

### DPU SmartNIC & Programmable IO (12; plant: compute_pool, fabric)
dpu_pf_tx_rate [capacity], dpu_vf_tx_rate [capacity], dpu_sf_tx_rate [capacity], dpu_bandwidth_share [capacity], dpu_qos_group [capacity], sriov_vf_count [capacity], smartnic_flow_steering [capacity], smartnic_offload_enable [capacity], dpu_cpu_budget [admission], dpu_memory_budget [admission], dpu_service_placement [capacity], dpu_failover [capacity]

### Distributed Cluster Managers (15; plant: compute_pool, batch)
task_admission [admission], task_priority [admission], resource_reservation [capacity], cluster_quota [admission], task_preemption [admission], binpack_pressure [capacity], spread_pressure [capacity], gang_schedule [capacity], worker_allocation [capacity], maintenance_evacuation [capacity], oversubscription [capacity], resource_reclaim [capacity], queue_fairness [admission], deadline_pressure [admission], scheduler_retry [admission]

### GPU Fabric & RDMA (18; plant: compute_pool, fabric)
nvlink_placement [capacity], nvswitch_route [capacity], gpu_fabric_quarantine [admission], rdma_bandwidth [capacity], rdma_route [capacity], nic_affinity [capacity], collective_concurrency [admission], collective_algorithm [capacity], collective_chunk_size [capacity], rank_placement [capacity], gpudirect_policy [capacity], congestion_response [capacity], rail_selection [capacity], fabric_failover [capacity], communication_priority [admission], fabric_isolation [admission], collective_protocol [capacity], nic_hca_selection [capacity]

### HPC & Distributed Compute (19; plant: compute_pool, batch)
job_slots [capacity], mpi_ranks [capacity], rank_mapping [capacity], node_allocation [capacity], job_walltime [capacity], job_priority [admission], job_preemption [admission], checkpoint_restart [capacity], parallel_io_budget [admission], collective_budget [admission], accelerator_share [capacity], cpu_gpu_ratio [setpoint], memory_per_rank [capacity], scratch_budget [admission], scheduler_fair_share [admission], backfill_policy [capacity], node_power_saving [power], cpu_frequency_per_job [power], partition_limits [capacity]

### Kubernetes Dynamic Device Allocation (8; plant: compute_pool, gpu)
dra_device_class_selection [capacity], dra_claim_capacity [capacity], dra_claim_sharing [capacity], dra_device_taint [capacity], dra_device_eviction [admission], dra_binding_readiness [capacity], dra_binding_failure_response [capacity], dra_device_configuration [setpoint]

### OpenShift & Machine API (9; plant: compute_pool, node)
machine_remediation [capacity], machine_health_gate [admission], mcp_pause [admission], mcp_max_unavailable [capacity], node_config_rollout [capacity], operator_reconcile_budget [admission], cluster_version_pacing [capacity], infra_machine_admission [admission], machine_failure_domain [capacity]

### Quantum Computing Control Simulation (16; plant: compute_pool, qpu)
qubit_mapping [capacity], circuit_admission [admission], shot_allocation [capacity], circuit_scheduling [admission], gate_scheduling [capacity], pulse_amplitude [capacity], pulse_duration [setpoint], pulse_phase [capacity], pulse_frequency [power], coupling_control [capacity], reset_scheduling [capacity], measurement_scheduling [capacity], dynamical_decoupling [capacity], noise_aware_routing [capacity], error_mitigation_budget [admission], quantum_queue_priority [admission]

### Work Admission & Demand Shaping (19; plant: compute_pool, server)
api_concurrency [admission], queue_concurrency [admission], queue_backpressure [admission], job_admission [admission], batch_admission [admission], inference_admission [admission], load_shed [admission], priority_gate [admission], tenant_admission [admission], burst_limit [admission], deadline_admission [admission], work_budget [admission], request_queue_limit [admission], retry_admission [admission], background_work_gate [admission], maintenance_work_gate [admission], request_concurrency_limit [admission], adaptive_concurrency_limit [admission], priority_request_queue_under_limit [admission]

## Realm 2: Physics / Robotics / Autonomous: 119 own muscles + the spine = 376 in its organism

### Automotive EV & Mobile Powertrain (14; plant: motion_axis, ev_traction)
traction_torque_limit [power], regen_braking_level [power], battery_charge_limit [power], battery_discharge_limit [power], battery_thermal_target [power], motor_thermal_limit [power], vehicle_speed_envelope [capacity], energy_recovery_target [power], auxiliary_power_budget [power], fast_charge_current [power], fast_charge_voltage [power], vehicle_safe_state [admission], state_of_charge_limits [power], smart_charging_schedule [admission]

### Aviation & Autonomous Flight (20; plant: motion_axis, flight_axis)
throttle_envelope [power], attitude_target [capacity], attitude_rate_target [capacity], velocity_target [capacity], altitude_target [capacity], waypoint_authority [capacity], flight_hold [admission], return_to_home [admission], land_action [admission], mission_admission [admission], geofence_response [admission], failsafe_selection [admission], battery_reserve_threshold [admission], actuator_saturation_envelope [capacity], flight_mode_transition [admission], flight_termination_safe_state [admission], attitude_rate_gains [capacity], horizontal_speed_limit [power], vertical_speed_limits [power], acceleration_jerk_limits [power]

### Elevators & Vertical Transport (12; plant: motion_axis, elevator_hoist)
hoist_speed_target [capacity], acceleration_limit [capacity], regen_drive_mode [power], standby_power_mode [admission], destination_dispatch_schedule [admission], car_parking_mode [admission], door_dwell_hold [admission], escalator_speed_target [capacity], group_capacity_mode [admission], motor_thermal_derate [power], brake_test_schedule [admission], fire_recall_mode [admission]

### Marine Propulsion & Vessel Automation (12; plant: motion_axis, marine_propulsion)
shaft_speed_target [capacity], propeller_pitch_limit [power], shaft_power_limit [power], bow_thruster_duty [power], ballast_pump_mode [admission], engine_load_sharing_setpoint [capacity], slow_steaming_speed_target [capacity], auxiliary_engine_staging [capacity], shore_power_mode [admission], hotel_load_budget [power], trim_target [capacity], rudder_rate_limit [power]

### Rail Traction & Train Control (14; plant: motion_axis, rail_traction)
traction_effort_limit [power], regenerative_braking_share [power], coasting_speed_target [capacity], dwell_time_schedule [admission], hvac_duty_cycle [power], train_auxiliary_power_budget [power], platform_approach_speed [capacity], acceleration_rate_setpoint [capacity], wheel_slip_protection_mode [admission], traction_motor_thermal_derate [power], catenary_voltage_limit [power], timetable_recovery_margin [admission], headway_target [capacity], door_release_hold [admission]

### Robotics Fleet & Warehouse Automation (15; plant: compute_pool, robot_fleet)
robot_dispatch [capacity], task_assignment [capacity], traffic_reservation [capacity], robot_route [capacity], charging_dispatch [capacity], battery_reserve [capacity], elevator_request [capacity], door_request [capacity], conveyor_speed [capacity], agv_speed [capacity], warehouse_zone_admission [admission], robot_quarantine [admission], fleet_failover [capacity], human_safe_stop [capacity], fleet_concurrency [admission]

### Robotics Motion Control (18; plant: motion_axis, robot_joint)
joint_position [capacity], joint_velocity [capacity], joint_acceleration [capacity], joint_effort [power], cartesian_velocity [capacity], trajectory_speed [capacity], trajectory_acceleration [capacity], jerk_limit [capacity], collision_margin [capacity], force_limit [power], gripper_force [power], locomotion_speed [capacity], steering_angle [capacity], braking_force [power], balance_correction [capacity], trajectory_tolerances [capacity], velocity_acceleration_scaling [capacity], controller_update_rate [capacity]

### Spacecraft & Flight Software (14; plant: motion_axis, reaction_wheel)
space_command_admission [admission], flight_task_schedule [admission], space_mode_transition [admission], payload_duty_cycle [power], communication_allocation [capacity], space_power_budget [power], space_thermal_command [power], attitude_command_envelope [capacity], reaction_wheel_allocation [capacity], rcs_authority [power], safe_mode_transition [admission], watchdog_recovery [admission], instrument_activation [capacity], fault_isolation [admission]

## Realm 3: Energy / Facility / Industrial: 213 own muscles + the spine = 470 in its organism

### Agriculture & Irrigation (14; plant: process_loop, irrigation)
irrigation_pump_speed [capacity], mainline_pressure_setpoint [setpoint], soil_moisture_target [setpoint], pivot_speed_setpoint [setpoint], fertigation_dose [power], greenhouse_temperature_setpoint [setpoint], greenhouse_co2_target [setpoint], vent_position_setpoint [setpoint], grain_dryer_temperature_setpoint [setpoint], cold_storage_temperature_setpoint [setpoint], barn_ventilation_rate [capacity], milking_vacuum_level_setpoint [setpoint], well_drawdown_level_target [setpoint], drip_zone_dispatch [admission]

### Building & Critical Environment HVAC (15; plant: thermal_zone, building)
zone_temperature_target [setpoint], zone_airflow [capacity], ahu_fan_speed [capacity], damper_position [capacity], economizer_position [capacity], boiler_setpoint [setpoint], heat_pump_mode [admission], humidity_target [setpoint], occupancy_ventilation [admission], building_demand_limit [power], thermal_storage_dispatch [capacity], hvac_emergency_mode [admission], setpoint_reset_trim_and_respond [setpoint], duct_static_pressure_setpoint [setpoint], optimal_start_stop [capacity]

### District Heating & Cooling (13; plant: process_loop, district_heat)
supply_temperature_setpoint [setpoint], return_temperature_target [setpoint], differential_pressure_setpoint [setpoint], network_pump_speed [capacity], heat_pump_staging [capacity], chp_dispatch [admission], thermal_storage_level_target [setpoint], peak_boiler_heater_output [power], substation_flow_limit [capacity], peak_demand_shed [admission], outdoor_reset_setpoint [setpoint], cooling_network_supply_temperature [setpoint], cooling_storage_level_target [setpoint]

### Energy Storage & Microgrid (19; plant: energy_storage, microgrid)
battery_charge_power [power], battery_discharge_power [power], battery_soc_reserve [setpoint], grid_import_limit [power], grid_export_limit [power], pv_curtailment [power], ev_charge_power [power], heat_pump_power [power], electrolyzer_power [power], microgrid_demand_limit [power], peak_shaving [capacity], time_of_use_schedule [setpoint], energy_load_shed [admission], flex_load_admission [admission], storage_dispatch [capacity], microgrid_emergency_reserve [setpoint], volt_var [capacity], volt_watt [capacity], constant_power_factor_reactive_power [power]

### Facility & Grid Optimization (15; plant: energy_storage, facility)
facility_power_budget [power], utility_demand_limit [power], demand_response [admission], electricity_price_gate [admission], carbon_intensity_gate [admission], renewable_dispatch [capacity], generator_start_stop [capacity], site_battery_dispatch [capacity], pue_target [setpoint], cooling_power_budget [power], it_power_budget [power], rack_power_allocation [power], facility_peak_guard [capacity], grid_frequency_response [admission], facility_islanding [admission]

### Grid Transmission & Distribution (12; plant: process_loop, feeder_voltage)
capacitor_bank_switch [capacity], voltage_regulator_tap [setpoint], transformer_tap [setpoint], inverter_real_power [power], inverter_reactive_power [power], feeder_voltage_target [setpoint], feeder_load_transfer [capacity], distribution_storage_dispatch [admission], demand_response_dispatch [admission], frequency_droop_setpoint [setpoint], grid_protection_mode [admission], grid_restoration_sequence [admission]

### Healthcare Critical Environments (13; plant: thermal_zone, hospital)
operating_room_air_change_setpoint [setpoint], isolation_room_pressure_target [setpoint], patient_room_temperature_setpoint [setpoint], surgical_suite_humidity_target [setpoint], ahu_supply_air_temperature [setpoint], pharmacy_cold_room_setpoint [setpoint], sterile_storage_humidity_setpoint [setpoint], imaging_suite_cooling_capacity [capacity], chiller_plant_staging [capacity], exhaust_fan_capacity [capacity], ward_night_setback_mode [admission], medical_gas_plant_demand_limit [power], emergency_power_load_shed [admission]

### Industrial PLC & Process Automation (18; plant: process_loop, process)
plc_cycle_authority [admission], machine_cell_admission [admission], valve_position [setpoint], pump_flow [capacity], compressor_speed [capacity], heater_power [power], furnace_setpoint [setpoint], pressure_setpoint [setpoint], temperature_setpoint [setpoint], mass_flow_setpoint [setpoint], tank_level_target [setpoint], conveyor_rate [capacity], feed_rate [capacity], purge_vent_action [admission], controller_mode [capacity], alarm_limits [capacity], safety_interlock_trip [capacity], opc_ua_writes [capacity]

### Mining & Mineral Processing (14; plant: process_loop, mill)
sag_mill_load_setpoint [setpoint], mill_speed_target [setpoint], crusher_gap_setpoint [setpoint], flotation_aeration_rate [power], cyclone_feed_pressure_target [setpoint], thickener_underflow_density_target [setpoint], reagent_dose [power], conveyor_speed_setpoint [setpoint], dewatering_pump_level_target [setpoint], ventilation_on_demand_airflow [capacity], stockpile_level_target [setpoint], slurry_pump_speed [capacity], tailings_discharge_shutdown [admission], ore_blend_dispatch [admission]

### Oil & Gas Pipelines (14; plant: process_loop, pipeline)
compressor_discharge_pressure_setpoint [setpoint], pump_station_suction_pressure_target [setpoint], line_pack_target [setpoint], pipeline_flow_setpoint [setpoint], compressor_unit_staging [capacity], vfd_pump_speed [capacity], terminal_tank_level_target [setpoint], leak_detection_shutdown [admission], batch_interface_dispatch [admission], heater_outlet_temperature_setpoint [setpoint], drag_reducing_agent_dose [power], valve_position_target [setpoint], cathodic_protection_voltage [setpoint], pressure_protection_priority [admission]

### Pharmaceutical & Food Manufacturing (14; plant: process_loop, batch_reactor)
reactor_temperature_setpoint [setpoint], agitator_speed_setpoint [setpoint], fermenter_dissolved_oxygen_target [setpoint], ph_setpoint [setpoint], pasteurizer_holding_temperature_setpoint [setpoint], freezer_tunnel_temperature_setpoint [setpoint], cip_cycle_dispatch [admission], cleanroom_pressure_cascade_setpoint [setpoint], lyophilizer_shelf_temperature_setpoint [setpoint], chromatography_flow_setpoint [setpoint], steam_sterilizer_cycle_priority [admission], oven_zone_temperature_setpoint [setpoint], refrigerant_compressor_authority [admission], batch_hold_quarantine [admission]

### Power Generation & Turbine Control (14; plant: process_loop, turbine)
turbine_speed_droop_setpoint [setpoint], unit_load_setpoint [setpoint], boiler_steam_pressure_setpoint [setpoint], feedwater_level_target [setpoint], agc_participation_limit [capacity], excitation_voltage_setpoint [setpoint], hydro_gate_position_target [setpoint], combustion_air_ratio_setpoint [setpoint], cooling_water_flow_setpoint [setpoint], inlet_guide_vane_position [setpoint], reserve_dispatch_priority [admission], turbine_ramp_rate_limit [capacity], emissions_shutdown [admission], nuclear_rod_position_target [setpoint]

### Renewable Generation & Inverter Control (13; plant: process_loop, inverter)
inverter_volt_var_setpoint [setpoint], inverter_volt_watt_setpoint [setpoint], active_power_curtailment [power], plant_reactive_power_target [setpoint], wind_turbine_yaw_offset [capacity], pitch_angle_limit [capacity], rotor_speed_setpoint [setpoint], inverter_frequency_droop_setpoint [setpoint], ramp_rate_limit [capacity], tracker_stow_mode [admission], string_mppt_voltage_setpoint [setpoint], noise_mode_schedule [admission], ice_detection_shutdown [admission]

### Semiconductor Fab & Precision Manufacturing (13; plant: process_loop, chamber)
tool_job_dispatch [admission], wafer_route [capacity], chamber_recipe_selection [admission], chamber_temperature [setpoint], chamber_pressure [setpoint], gas_flow [capacity], rf_power [power], vacuum_pump_speed [capacity], robot_transfer_rate [capacity], lot_priority [admission], tool_quarantine [admission], run_to_run_control [capacity], idle_sleep_mode [capacity]

### Water Wastewater & Pumping (12; plant: process_loop, water)
pump_speed_water [capacity], valve_position_water [setpoint], reservoir_level_target [setpoint], line_pressure_target [setpoint], flow_target_water [setpoint], aeration_rate [power], chemical_dose_rate [power], filtration_backwash [admission], lift_station_dispatch [admission], leak_isolation [admission], water_demand_shed [admission], water_emergency_shutdown [admission]

## Realm 4: Distribution / Specialized: 183 own muscles + the spine = 440 in its organism

### Cache & Memory Services (16; plant: compute_pool, server)
cache_size [capacity], cache_ttl [setpoint], cache_eviction_policy [admission], cache_replicas [capacity], cache_sharding [capacity], cache_prefetch [capacity], cache_writeback_rate [capacity], cache_admission [admission], hot_key_isolation [admission], cache_connection_limit [admission], cache_memory_limit [capacity], cache_compression [capacity], cache_warmup [capacity], cache_failover [capacity], cache_flush_rate [capacity], memory_size_threads [capacity]

### Commerce & Payment Systems (15; plant: compute_pool, commerce)
payment_admission [admission], payment_concurrency [admission], payment_retry [admission], payment_timeout [admission], fraud_review_gate [admission], authorization_route [capacity], processor_route_weight [setpoint], transaction_queue_limit [admission], idempotency_window [setpoint], order_reservation [capacity], inventory_hold [admission], checkout_load_shed [admission], refund_queue_rate [capacity], settlement_batch [capacity], payment_failover [capacity]

### Data Analytics & ETL (15; plant: compute_pool, batch)
executor_size [capacity], dynamic_allocation_min [capacity], dynamic_allocation_max [capacity], shuffle_partitions [capacity], shuffle_bandwidth [capacity], etl_concurrency [admission], stage_parallelism [capacity], query_slots [capacity], spill_threshold [admission], cache_fraction [setpoint], batch_interval [setpoint], stream_backpressure [admission], data_locality_wait [capacity], speculation_policy [capacity], analytics_admission [admission]

### Database & Transactions (19; plant: compute_pool, database)
db_replicas [capacity], db_memory [capacity], db_cache [capacity], query_concurrency [admission], read_route [capacity], shard_placement [capacity], db_failover [capacity], replication_lag_gate [admission], db_write_throttle [admission], db_pool_resize [capacity], transaction_concurrency [admission], lock_timeout [admission], checkpoint_rate [capacity], vacuum_compaction_rate [capacity], parallel_workers [capacity], background_writer [capacity], synchronous_replication [capacity], buffer_pool [capacity], io_capacity [capacity]

### Medical Imaging & Clinical Systems (12; plant: compute_pool, clinical)
pacs_archive_tier_target [setpoint], dicom_router_concurrency [admission], ehr_application_replicas [capacity], hl7_interface_queue_limit [admission], fhir_api_rate_limit [admission], reconstruction_gpu_workers [capacity], modality_worklist_timeout [admission], patient_monitoring_gateway_capacity [admission], lab_analyzer_batch_window [admission], telehealth_session_admission [admission], clinical_backup_window [admission], imaging_prefetch_priority [admission]

### Messaging & Streaming (18; plant: compute_pool, server)
partition_count [capacity], partition_placement [capacity], producer_quota [admission], consumer_quota [admission], broker_io_quota [admission], message_retention [capacity], queue_depth_limit [admission], consumer_concurrency [admission], producer_batch_size [capacity], fetch_batch_size [capacity], rebalance_rate [capacity], replication_factor [capacity], retry_backoff [admission], dead_letter_divert [capacity], stream_priority [admission], broker_failover [capacity], prefetch [capacity], memory_disk_alarm [capacity]

### Ports & Maritime Logistics (12; plant: compute_pool, port)
quay_crane_allocation [capacity], yard_crane_fleet_size [capacity], berth_window_admission [admission], truck_gate_rate_limit [admission], horizontal_transport_fleet_size [capacity], reefer_plug_power_budget [power], shore_power_connection_capacity [capacity], rail_mounted_gantry_dispatch [capacity], container_dwell_priority [admission], vessel_arrival_pacing [admission], stacking_height_target [setpoint], equipment_charging_window [admission]

### Runtime & Application (17; plant: compute_pool, server)
worker_count [capacity], thread_pool [capacity], jvm_heap [capacity], gc_budget [admission], connection_pool_runtime [capacity], application_cache_size [capacity], runtime_memory [capacity], async_concurrency [admission], event_loop_workers [capacity], process_count [capacity], request_timeout [admission], background_workers [capacity], runtime_cpu_budget [admission], runtime_io_budget [admission], runtime_restart [capacity], go_runtime [capacity], keepalive_connection_reuse [capacity]

### Search, Indexing & Vector DB (16; plant: compute_pool, server)
index_workers [capacity], index_refresh_rate [capacity], segment_merge_rate [capacity], search_concurrency [admission], search_timeout [admission], shard_count [capacity], shard_replication [capacity], shard_rebalance [capacity], vector_search_k [capacity], vector_batch_size [capacity], embedding_workers [capacity], index_memory_budget [admission], query_route [capacity], hot_shard_isolation [admission], search_admission [admission], circuit_breakers [admission]

### Service Mesh & API Reliability (16; plant: compute_pool, server)
circuit_breaker [admission], retry_budget [admission], service_timeout [admission], service_concurrency [admission], connection_pool [capacity], traffic_divert [capacity], traffic_mirror [capacity], canary_weight [setpoint], outlier_ejection [admission], health_threshold [admission], dns_traffic_weight [setpoint], session_affinity [capacity], request_hedging [capacity], fault_injection_gate [admission], service_failover [capacity], load_balancing_policy [capacity]

### Telecom RAN & Edge Radio (12; plant: compute_pool, ran)
ran_connection_admission [admission], ran_ue_handover [capacity], ran_cell_traffic_steering [capacity], ran_slice_resource_budget [admission], ran_prb_allocation [capacity], ran_scheduler_weight [setpoint], ran_tx_power [power], ran_antenna_tilt [capacity], ran_carrier_enable [capacity], ran_cell_sleep [capacity], ran_du_cu_placement [capacity], ran_fronthaul_budget [admission]

### Workflow, Logistics & Fulfillment (15; plant: compute_pool, workflow)
workflow_admission [admission], workflow_worker_rate [capacity], task_queue_rate [capacity], workflow_retry [admission], workflow_backoff [admission], workflow_timeout [admission], inventory_allocation [capacity], fulfillment_route [capacity], warehouse_queue [capacity], carrier_selection [capacity], dispatch_priority [admission], shipment_batch [capacity], route_replan [capacity], sla_escalation [capacity], compensation_action [capacity]

## Organism 5: the four stacked, every duplicate kept, 1,716 muscles

## Organism 6: the whole tower, all 945 muscles once

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE` and `NOTICE` at the root of
this repository.*
