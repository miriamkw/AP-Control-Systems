#!/usr/bin/env python
# coding: utf-8

# # PID Controller
# 
# PID control is one of the common approaches to creating artificial pancreas systems. It is simple to implement because it only requires one input and one output value. In this section we are looking at highly simplified implementations of such systems. We have assumed no meal intake, a constant set point and have ignored delay in the system. Lastly we reflect on the advantages and disadvantages to the PID approach in the artificial pancreas problem. 

# ## Proportional Only (P-Only) Controller
# 
# The first term of a PID controller is the proportional term. Here we will give an example where we only use this term in the control system.
# 
# $$
# u(t) = u_{bias} + K_C (SP - PV) = u_{bias} + K_C e(t)
# $$
# 
# u(t) is the controller output {cite}`P-only-control`. In our example this means the amount of insulin to be delivered at that time and state. $u_{bias}$ will be our basal rate. Basal rate means the default insulin amount to be delivered when glucose level is already at target. SP is an abbreviation for set point, and is out target BGC. The process variable (PV) is the BGC measurement value. K_C is the proportional error constant, in our case the insulin sensitivity factor.
# 
# ### Tuning 
# 
# With empirical data it is common to tune a P-only controller with ITAE (Integral of Time-weighted Absolute Error), and curve fitting to obtain parameters. 

# In[1]:


# Imports
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


# Define constants
SP = 6.0 # Set point
ISF = 2 # Insulin sensitivity factor, mmol/L/U
basal_rate = 1.0 # Unit: U/hr, u_bias


# In[3]:


# Plots:
# 1) The insulin injections the P-only control system would do
# 2) A set of example glucose measurement values, as well as the target glucose level

# time
t = np.linspace(0,60,101)

# step functions
s1 = np.zeros(101); s1[11:] = 1.0
s2 = np.zeros(101); s2[51:] = 1.0

# solution to non-integrating system
# taup * dy/dt = -y + Kp * u
du=2; Kp=1; taup=10
# SP 
y1 = np.linspace(SP,SP,101)

# Blood glucose measurements
y2 = np.sin(t*0.2)*2 + SP

plt.figure(1)

# First plot
plt.subplot(2,1,1)
plt.plot(basal_rate + -ISF*(SP - y2),'k-',lw=2,label='Impulse (u)')
plt.grid(); plt.legend(); plt.ylabel('u(t)')

# Second plot
plt.subplot(2,1,2)
plt.plot(t,y2,'b-', lw=2,  label=r'Blood glucose measurements [mmol/L]')
plt.plot(t,y1,'r--',lw=2,  label=r'Set Point (SP)')
plt.legend(); plt.grid(); plt.xlabel('Time [min]'); plt.ylabel('y(t)')

plt.show()


# ### Observations
# 
# #### Negative insulin injections
# It is not possible to deliver negative amounts of insulin. Negative output is a result of our simple example above. We could program the system to not be able to deliver negative amounts of insulin. However, this would lead to overdelivery of insulin in total. This clearly illustrate the need for the integral term for the regulation system, which would take into account past actions and compensate for that in the output.
# 
# #### Insulin effect on system
# For the regulation system to work properly, we will need a (Refer to chapter 2 equation for insulin curve). The assumed response in this example is far from how the system is responding in reality.

# ## Proportional Integral (PI) Controller
# 
# As we could see in the last section, it is useful to do retrospective correction of our output. In a PI controller, the integral term does exactly this. A PI controller can be expressed as: 
# 
# $$
# e(t) = SP - PV
# $$
# $$
# u(t) = u_{bias} + K_C e(t) + \frac{K_C}{\tau_I} \int_0^t e(t)\,dx
# $$
# 
# The added term ${\tau_I}$ in addition to the excisting terms from the P only system, is the integral time constant {cite}`PI-control`.
# 

# In[4]:


# Plots:
# 1) The insulin injections the P-only control system would do
# 2) A set of example glucose measurement values, as well as the target glucose level

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# specify number of steps
ns = 1200
# define time points
t = np.linspace(0,ns,ns+1)

# Define Set Point
sp = np.zeros(ns+1)  # set point
sp[:] = SP
Kc = -1/ISF
tauI = 10.0

def calc_response(t,Kc,tauI,sp):
    # t = time points
    # specify number of steps
    ns = len(t)-1

    delta_t = t[1]-t[0]

    # storage for recording values
    op = np.zeros(ns+1)  # controller output
    #pv = np.zeros(ns+1)  # process variable
    pv = np.sin(t*0.01)*2 + SP
    e = np.zeros(ns+1)   # error
    ie = np.zeros(ns+1)  # integral of the error
    dpv = np.zeros(ns+1) # derivative of the pv
    P = np.zeros(ns+1)   # proportional
    I = np.zeros(ns+1)   # integral

    # Upper and Lower limits on OP
    op_hi = 10.0
    op_lo = 0.0

    # loop through time steps    
    for i in range(0,ns):
        e[i] = sp[i] - pv[i]
        if i >= 1:  # calculate starting on second cycle
            dpv[i] = (pv[i]-pv[i-1])/delta_t
            ie[i] = ie[i-1] + e[i] * delta_t
        P[i] = Kc * e[i]
        I[i] = Kc/tauI * ie[i]
        op[i] = basal_rate + P[i] + I[i]
        if op[i] > op_hi:  # check upper limit
            op[i] = op_hi
            ie[i] = ie[i] - e[i] * delta_t # anti-reset windup
        if op[i] < op_lo:  # check lower limit
            op[i] = op_lo
            ie[i] = ie[i] - e[i] * delta_t # anti-reset windup
        # implement time delay
        iop = max(0,i)
    op[ns] = op[ns-1]
    ie[ns] = ie[ns-1]
    P[ns] = P[ns-1]
    I[ns] = I[ns-1]
    return (pv,op)

def plot_response(n,t,pv,op,sp):
    # plot results
    plt.figure(n)

    plt.subplot(2,1,1)
    plt.plot(t,sp,'k-',linewidth=2,label='Set Point (SP)')
    plt.plot(t,pv,'b--',linewidth=3,label='Process Variable (PV)')
    plt.legend(loc='best')
    plt.ylabel('Process Output')

    plt.subplot(2,1,2)
    plt.plot(t,op,'r:',linewidth=3,label='Controller Output (OP)')
    plt.legend(loc='best')
    plt.ylabel('Process Input')

    plt.xlabel('Time')

# PI control
(pv,op) = calc_response(t,Kc,tauI,sp)

plot_response(2,t,pv,op,sp)

plt.show()


# ### Observations
# 
# #### Countinous vs. Discrete
# In the examples we have used countinous curves for insulin delivery and glucose measurements. In reality these are discrete amounts with a given time interval.
# 
# #### Tuning
# Tuning might result complex if diurnal variations of insulin demand is significant. In this case, the tuning techniques can not simply be implemented without adjustments.

# ## Proportional Integral Derivative (PID) Controller
# 
# As we could see in the last section, it is useful to do retrospective correction of our output. In a PI controller, the integral term does exactly this. A PI controller can be expressed as: 
# 
# $$
# e(t) = SP - PV
# $$
# $$
# u(t) = u_{bias} + K_C e(t) + \frac{K_C}{\tau_I} \int_0^t e(t)\,dx - K_C \tau_D \frac{d(PV)}{dt}
# $$
# 
# The PID controller has three tuning variables: $K_C$, the integral time constant, $τ_I$, and the derivative time constant, $τ_D$ {cite}`PID-control`. The pupose of the additional derivative term is to pick up on the rate of error and hence receive a stronger response if the error is quickly rising.  

# ## Advantages and Disadvantages
# 
# ### Advantages
# 
# PID control systems have the advantage of being a simple input-output algorithm. Common methods used to tune parameters makes it possible to exclude complex modelling of the system. 
# 
# 
# ### Disadvantages
# 
# The shortcomings of PID control in artificial pancreases is that, to work well i practice it  requires additional adjustments. This is caused by the slow dynamics of glucose-insulin dynamics. Safety restrictions on insulin delivery and glucose level predicitons are examples of such additional adjustments. Still with adjustments the system relies on human expertise, to provide safe initial values for an individual patient {cite}`chee`. 

# ## Related literature
# 
# Several attempts have been done on implementing PID control to create artificial pancreases, and here we are only going to mention a few. Steil et al. implemented an end to end system {cite}`pid_2006` that was later commercialised in a MiniMed artificial pancreas. Further implementations have added future BGC estimates to improve the controller {cite}`pid_2013`. The performance in clinical trials is promising, but insufficient for fully closed loop systems {cite}`review_2021`. Manual inputs such as carbohydrate counting and overrides during excersise is common.  
# 
