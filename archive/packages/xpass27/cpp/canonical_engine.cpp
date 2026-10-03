#include "omnicompass/canonical_engine.hpp"
#include <algorithm>
#include <cmath>
namespace omnicompass {
static State add_scaled_ce(const State&a,const State&b,double s) noexcept{return {a.E+s*b.E,a.U+s*b.U,a.I_U+s*b.I_U,a.S+s*b.S,a.B+s*b.B,a.B_dot+s*b.B_dot};}
static State combine_ce(const State&s,const State&a,const State&b,const State&c,const State&d,double h) noexcept{return {s.E+h*(a.E+2*b.E+2*c.E+d.E)/6,s.U+h*(a.U+2*b.U+2*c.U+d.U)/6,s.I_U+h*(a.I_U+2*b.I_U+2*c.I_U+d.I_U)/6,s.S+h*(a.S+2*b.S+2*c.S+d.S)/6,s.B+h*(a.B+2*b.B+2*c.B+d.B)/6,s.B_dot+h*(a.B_dot+2*b.B_dot+2*c.B_dot+d.B_dot)/6};}
RK4Trace canonical_microstep(const State&s,const Parameters&p,double t,int target) noexcept{
 RK4Trace q{}; q.t=t;q.h=MICRO_DT; q.uncontrolled_u=derivatives(s,p,t,0).U; q.raw_command=-q.uncontrolled_u+KP*(double(target)-s.U); q.u_hold=std::clamp(q.raw_command,-U_AUTHORITY,U_AUTHORITY);
 q.k1=derivatives(s,p,t,q.u_hold);q.k2=derivatives(add_scaled_ce(s,q.k1,.5*MICRO_DT),p,t+.5*MICRO_DT,q.u_hold);q.k3=derivatives(add_scaled_ce(s,q.k2,.5*MICRO_DT),p,t+.5*MICRO_DT,q.u_hold);q.k4=derivatives(add_scaled_ce(s,q.k3,MICRO_DT),p,t+MICRO_DT,q.u_hold);q.accepted=combine_ce(s,q.k1,q.k2,q.k3,q.k4,MICRO_DT);return q;
}
CanonicalTrace canonical_run(const InputCase&in) noexcept{CanonicalTrace out{};out.initial=in.initial;out.target_sign=nearest_basin_sign(in.initial.U);State s=in.initial;double t=0;for(int m=0;m<MACRO_STEPS;m++){auto &mt=out.macro[m];mt.macro=m+1;for(int j=0;j<MICRO_STEPS;j++){auto q=canonical_microstep(s,in.p,t,out.target_sign);mt.micro[j]=q;mt.actuator_abs_integral+=std::abs(q.u_hold)*MICRO_DT;mt.actuator_peak=std::max(mt.actuator_peak,std::abs(q.u_hold));mt.saturated+=std::abs(q.raw_command)>U_AUTHORITY+EPS;s=q.accepted;t+=MICRO_DT;}mt.accepted=s;}out.final=s;return out;}
Parameters canonical_reference_parameters() noexcept{Parameters p{};p.alpha=4.2;p.alpha_E=4.2;p.alpha_U=4.2;p.beta_int=.5;p.beta_ext=.5;p.k=1.7;p.sigma_1=.38;p.delta=.505;p.gamma_1=1.35;p.gamma_c=1.0;p.lambda_0=0;p.lambda_1=1.55;p.lambda_2=1.0;p.c=2.75;p.E_max=5.5;p.omega_B=2.55;p.Q_B=5.25;p.alpha_s=.15;p.beta_s=.15;p.mu=4.0;p.lambda_I=1.25;p.lambda_U=.25;return p;}
}
