import numpy as np
from omnicompass.batch_claim1 import macro
from omnicompass.core import State,macro_step
from omnicompass.adapter import STACK_PARAMS

def test_batch_matches_scalar_claim1():
    x=np.array([[.12,.82,0.,0.,0.,0.],[.2,.4,.1,.2,.1,-.1]],dtype=float); bi=np.array([.2,.7]); be=np.array([.1,.3]); target=np.array([1.,1.])
    xb,u,_,_=macro(x.copy(),0.,bi,be,target)
    for i in range(2):
        p=type(STACK_PARAMS)(**vars(STACK_PARAMS)); p.beta_int=float(bi[i]); p.beta_ext=float(be[i])
        xs,st=macro_step(State(*x[i]),p,0.,1)
        assert np.max(np.abs(xb[i]-np.array(xs.as_tuple()))) < 1e-12
        assert abs(u[i]-st['last_u']) < 1e-12
