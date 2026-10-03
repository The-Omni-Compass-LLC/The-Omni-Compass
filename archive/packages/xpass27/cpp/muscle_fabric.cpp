#include "omnicompass/muscle_fabric.hpp"
#include <algorithm>
#include <cmath>
#include <stdexcept>
namespace omnicompass {
MuscleObservation SimulatedMuscle::observe(){ return {value_,0.0,1.0,std::isfinite(value_)}; }
MuscleCommand SimulatedMuscle::execute(double requested,bool global_execute,bool security_hold){ MuscleCommand c; c.muscle_id=cap_.id;c.requested=requested;c.bounded=std::clamp(requested,cap_.minimum,cap_.maximum); c.permitted=global_execute && !security_hold && cap_.mode==AutomationMode::Automatic; if(c.permitted){value_=c.bounded;c.landed=true;c.reason="executed";} else {c.reason=security_hold?"security_hold":(!global_execute?"global_execute_false":"mode_not_automatic");} c.realized=value_; return c;}
bool SimulatedMuscle::restore(double native){value_=std::clamp(native,cap_.minimum,cap_.maximum);return std::abs(value_-native)<=cap_.resolution;}
void MuscleRegistry::add(MuscleAdapter& a){adapters_[a.capability().id]=&a;}
MuscleAdapter* MuscleRegistry::get(const std::string& id) const {auto it=adapters_.find(id);return it==adapters_.end()?nullptr:it->second;}
std::vector<std::string> MuscleRegistry::ids() const {std::vector<std::string> v;for(auto& kv:adapters_)v.push_back(kv.first);return v;}
MuscleReceipt transact(MuscleAdapter& a,double requested,bool global_execute,bool security_hold){auto before=a.observe();double native=a.snapshot_native();auto c=a.execute(requested,global_execute,security_hold);double rb=a.readback();MuscleReceipt r; r.muscle_id=a.capability().id;r.observed=before.value;r.requested=requested;r.bounded=c.bounded;r.realized=rb;r.residual=rb-c.bounded;r.shield_ok=!security_hold;r.readback_ok=std::isfinite(rb)&&(!c.landed||std::abs(rb-c.bounded)<=a.capability().resolution);r.restore_ok=a.restore(native);r.reason=c.reason;return r;}
std::vector<MuscleCapability> full_tower_catalog(){std::vector<MuscleCapability> v;v.reserve(128);
  v.push_back(MuscleCapability{"work_admission.api_concurrency","work_admission","api_concurrency","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"work_admission.queue_concurrency","work_admission","queue_concurrency","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"work_admission.queue_backpressure","work_admission","queue_backpressure","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"work_admission.job_admission","work_admission","job_admission","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"work_admission.batch_admission","work_admission","batch_admission","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"work_admission.inference_batch","work_admission","inference_batch","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"work_admission.load_shed","work_admission","load_shed","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"work_admission.priority_gate","work_admission","priority_gate","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.replicas","kubernetes_scale","replicas","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.hpa_cpu_target","kubernetes_scale","hpa_cpu_target","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.hpa_memory_target","kubernetes_scale","hpa_memory_target","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.hpa_custom_target","kubernetes_scale","hpa_custom_target","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.vpa_apply","kubernetes_scale","vpa_apply","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.scale_to_zero","kubernetes_scale","scale_to_zero","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.keda_threshold","kubernetes_scale","keda_threshold","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"kubernetes_scale.rollout_rate","kubernetes_scale","rollout_rate","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.cpu_request","container_resources","cpu_request","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.cpu_limit","container_resources","cpu_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.memory_request","container_resources","memory_request","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.memory_limit","container_resources","memory_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.ephemeral_storage","container_resources","ephemeral_storage","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.hugepages","container_resources","hugepages","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.io_weight","container_resources","io_weight","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"container_resources.pids_limit","container_resources","pids_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.node_selector","placement","node_selector","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.node_affinity","placement","node_affinity","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.pod_anti_affinity","placement","pod_anti_affinity","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.topology_spread","placement","topology_spread","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.numa_placement","placement","numa_placement","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.gpu_topology","placement","gpu_topology","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.storage_locality","placement","storage_locality","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"placement.network_locality","placement","network_locality","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_desired","node_fleet","node_desired","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_pool_min","node_fleet","node_pool_min","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_pool_max","node_fleet","node_pool_max","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_provision","node_fleet","node_provision","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_cordon","node_fleet","node_cordon","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_drain","node_fleet","node_drain","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_consolidate","node_fleet","node_consolidate","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"node_fleet.node_replace","node_fleet","node_replace","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.cpufreq_min","host_cpu","cpufreq_min","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.cpufreq_max","host_cpu","cpufreq_max","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.rapl_package_power","host_cpu","rapl_package_power","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.uncore_frequency","host_cpu","uncore_frequency","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.cpuset","host_cpu","cpuset","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.cpu_weight","host_cpu","cpu_weight","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.cpu_quota","host_cpu","cpu_quota","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"host_cpu.energy_perf_preference","host_cpu","energy_perf_preference","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.gpu_allocate","gpu_accelerator","gpu_allocate","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.gpu_power_limit","gpu_accelerator","gpu_power_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.gpu_clock_limit","gpu_accelerator","gpu_clock_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.mig_mode","gpu_accelerator","mig_mode","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.mig_geometry","gpu_accelerator","mig_geometry","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.gpu_timeslice","gpu_accelerator","gpu_timeslice","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.gpu_mps","gpu_accelerator","gpu_mps","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"gpu_accelerator.gpu_quarantine","gpu_accelerator","gpu_quarantine","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.model_replicas","ai_hpc","model_replicas","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.model_route_weight","ai_hpc","model_route_weight","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.model_load","ai_hpc","model_load","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.model_unload","ai_hpc","model_unload","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.training_workers","ai_hpc","training_workers","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.gang_size","ai_hpc","gang_size","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.checkpoint_trigger","ai_hpc","checkpoint_trigger","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"ai_hpc.job_preempt","ai_hpc","job_preempt","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.lb_weight","network","lb_weight","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.route_weight","network","route_weight","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.rate_limit","network","rate_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.bandwidth_limit","network","bandwidth_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.qos_class","network","qos_class","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.connection_limit","network","connection_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.circuit_breaker","network","circuit_breaker","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"network.failover_route","network","failover_route","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.volume_size","storage","volume_size","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.iops_limit","storage","iops_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.throughput_limit","storage","throughput_limit","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.replica_count","storage","replica_count","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.storage_tier","storage","storage_tier","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.volume_placement","storage","volume_placement","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.snapshot_trigger","storage","snapshot_trigger","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"storage.rebalance","storage","rebalance","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.vm_count","vm_cloud","vm_count","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.vm_size","vm_cloud","vm_size","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.vm_start_stop","vm_cloud","vm_start_stop","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.vm_migrate","vm_cloud","vm_migrate","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.instance_family","vm_cloud","instance_family","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.asg_min","vm_cloud","asg_min","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.asg_max","vm_cloud","asg_max","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"vm_cloud.spot_mix","vm_cloud","spot_mix","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.db_replicas","database","db_replicas","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.db_connections","database","db_connections","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.db_memory","database","db_memory","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.db_cache","database","db_cache","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.query_concurrency","database","query_concurrency","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.read_route","database","read_route","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.shard_placement","database","shard_placement","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"database.db_failover","database","db_failover","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.worker_count","runtime","worker_count","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.thread_pool","runtime","thread_pool","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.jvm_heap","runtime","jvm_heap","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.gc_budget","runtime","gc_budget","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.connection_pool","runtime","connection_pool","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.cache_size","runtime","cache_size","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.runtime_memory","runtime","runtime_memory","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"runtime.async_concurrency","runtime","async_concurrency","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.restart","reliability_security","restart","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.rollback","reliability_security","rollback","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.quarantine","reliability_security","quarantine","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.traffic_divert","reliability_security","traffic_divert","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.degraded_mode","reliability_security","degraded_mode","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.actuator_freeze","reliability_security","actuator_freeze","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.workload_isolate","reliability_security","workload_isolate","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"reliability_security.restore_native","reliability_security","restore_native","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.server_power","thermal_power","server_power","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.rack_power","thermal_power","rack_power","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.pdu_power","thermal_power","pdu_power","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.site_power","thermal_power","site_power","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.cpu_thermal","thermal_power","cpu_thermal","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.gpu_thermal","thermal_power","gpu_thermal","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.cooling_setpoint","thermal_power","cooling_setpoint","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"thermal_power.thermal_migrate","thermal_power","thermal_migrate","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.namespace_quota","cluster_policy","namespace_quota","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.resource_quota","cluster_policy","resource_quota","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.priority_class","cluster_policy","priority_class","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.preemption_policy","cluster_policy","preemption_policy","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.pdb_policy","cluster_policy","pdb_policy","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.taint_toleration","cluster_policy","taint_toleration","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.fair_share","cluster_policy","fair_share","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
  v.push_back(MuscleCapability{"cluster_policy.multi_cluster_dispatch","cluster_policy","multi_cluster_dispatch","normalized",0.0,1.0,0.01,1.0,1.0,30.0,0.0,5.0,true,true,true,MuscleStatus::Specified,AutomationMode::Recommend});
 return v;}
}
