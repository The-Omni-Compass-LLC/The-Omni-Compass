"""Vectorized executable-equivalent CLAIM1 kernel for scale qualification.
Same equations, same bounded FF+P law, same held-u RK4 semantics as omnicompass.core.
This module exists so population tests do not change the canonical scalar source.
"""
from __future__ import annotations
import numpy as np
from .adapter import STACK_PARAMS
from .core import KP,U_AUTHORITY
P=STACK_PARAMS

def deriv(x,t,u,bint,bext):
    E,U,I,S,B,Bd=(x[:,i] for i in range(6))
    v=np.cos(.5*P.omega_B*t)*P.c*np.tanh(P.lambda_0+P.lambda_1*(U-.5)+P.lambda_2*S)
    dE=-P.alpha_E*E+bint+bext+v
    dU=P.mu*U*(1-U*U)-dE/P.E_max-P.lambda_U*U+u
    dI=(1-U)-P.sigma_1*E-P.delta*S-P.lambda_I*I
    dS=P.delta-P.alpha_s*S-.75*P.beta_s*S*S
    dBd=P.gamma_c*P.delta*S-(P.omega_B/P.Q_B)*Bd-P.omega_B**2*B
    return np.column_stack((dE,dU,dI,dS,Bd,dBd))

def step(x,t,bint,bext,target,h=.01):
    drift=deriv(x,t,np.zeros(len(x)),bint,bext)[:,1]
    raw=-drift+KP*(target-x[:,1]); u=np.clip(raw,-U_AUTHORITY,U_AUTHORITY)
    k1=deriv(x,t,u,bint,bext); k2=deriv(x+.5*h*k1,t+.5*h,u,bint,bext)
    k3=deriv(x+.5*h*k2,t+.5*h,u,bint,bext); k4=deriv(x+h*k3,t+h,u,bint,bext)
    return x+(h/6)*(k1+2*k2+2*k3+k4),u,raw

def macro(x,t,bint,bext,target,micro=10):
    peak=np.zeros(len(x)); sat=np.zeros(len(x),dtype=np.int32); last=np.zeros(len(x)); h=.1/micro
    for j in range(micro):
        x,last,raw=step(x,t+j*h,bint,bext,target,h); peak=np.maximum(peak,np.abs(last)); sat+=(np.abs(raw)>U_AUTHORITY)
    return x,last,peak,sat
