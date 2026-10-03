# Audit V1 source basis

Audit V1 distinguishes plant authority from telemetry and benchmark/evidence machinery. Historical FULL_TOWER_640.csv remains frozen as provenance.

Official-source spot checks used to validate missing authority classes include Kubernetes Dynamic Resource Allocation (device claims, allocation, sharing, binding conditions, health and device taints); NVIDIA BlueField QoS/rate controls; O-RAN near-real-time RIC control/admission/traffic steering; Linux powercap hierarchy; OpenDSS capacitor/distribution controls; and NVIDIA Jetson power/clock/thermal controls.

Admission remains contract based: observe, normalize, compute, command, actuate, read back, attribute, measure, compare, restore, seal, reproduce. An API name, sensor, parameter value, or duplicate alias is not a new muscle by itself.
