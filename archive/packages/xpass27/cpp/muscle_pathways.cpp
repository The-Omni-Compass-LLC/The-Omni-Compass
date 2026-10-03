#include "omnicompass/muscle_pathways.hpp"
#include <algorithm>
#include <cmath>
namespace omnicompass {
static std::string organ_for(const std::string& f){if(f=="kubernetes_scale"||f=="container_resources")return "pods";if(f=="node_fleet"||f=="placement"||f=="vm_cloud"||f=="cluster_policy")return "nodes";if(f=="host_cpu"||f=="runtime")return "cpufreq";if(f=="gpu_accelerator"||f=="ai_hpc")return "gpu";if(f=="network")return "routing";if(f=="thermal_power")return "power";if(f=="work_admission")return "routing";return "pods";}
PathwayDecision route_muscle(const MuscleCapability& c,const State&s,double u,const Authority&a){PathwayDecision d{};d.organ=organ_for(c.family);double coherence=std::clamp((s.U+1.0)/2.0,0.0,1.0);double stress=std::clamp(std::abs(s.E)+std::max(0.0,s.S),0.0,1.0);double ctrl=std::clamp(std::abs(u)/U_AUTHORITY,0.0,1.0);d.drive=std::clamp(.45*coherence+.35*ctrl+.20*(1.0-stress),0.0,1.0);d.expanding=u>=0;double req=d.expanding?(.5+.5*d.drive):(.5-.5*d.drive);d.normalized_request=std::clamp(req,0.0,1.0);auto it=a.organs.find(d.organ);bool organ_ok=it==a.organs.end()?a.execute:(it->second.contract||d.expanding);d.permitted=a.execute&&!a.security_hold&&organ_ok;d.reason=d.permitted?"canonical_engine_to_muscle":"authority_or_security_hold";return d;}
}
