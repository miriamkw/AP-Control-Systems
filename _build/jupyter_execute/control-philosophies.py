#!/usr/bin/env python
# coding: utf-8

# # Other Control Philosophies
# 
# In the previous sections we have described the most used control philosophies in artificial pancreas systems. The artificial pancreas with no manual input is yet an unsolved challenge, and there is room for creativity to come up with new solutions. In this section we will highlight some control philosophies with potential: Adaptive control, fuzzy-logic, dual hormone systems and multi variable systems. 

# ## Adaptive Control
# 
# In adaptive control, the controller is continuously adapting to the control system by tuning parameters. Diabetes has, as mentioned earlier, inter- and intrapersonal variations, and adaptive control is a potential method to take this into account. Adaptive control in an artificial pancreas has several degrees of freedom, like which parameters to tune, which optimization technique to use, and how frequent the adaptation should be. 
# 
# ### Advantages and Challenges
# Adaptive control is the control method used by a controller which must adapt to a controlled system with parameters which vary, or are initially uncertain. The advantage of this method is that it can adapt to changes. Insulin demands might change both long- and short term for a patient, due to changes in the body or environment. As mentioned eralier, the frequency of adaptions can vary. If they are very frequent, like every fourth hour, they adapt to environmental and temporary changes. They could also happen every three months, to adapt to more permanent variations. Some challenges are related to adaptive control is the computational load. Specifically to the AP control problem, the slow insulin-glucose responses is a challenge. Say something like a flu is triggering increased insulin demand for a couple of days, and the system adapts to this and tunes parameters based on this temporary condition. The following days when the patient is better, the system might deliver too much insulin.  
# 
# ### Example of Adaptive Control in AP Systems
# Practical examples of adaptive control in AP systems is the Autotune {cite}`autotune` and Autosense {cite}`autosense` feature in the open source system OpenAPS {cite}`openAPS`. The Autotune feature adjusts parameters like basal rate and insulin sensitivity factors due to long term changes, while Autosense is only observing data from the last 24 hours, trying to determine whether there are some short term divergence because of factors like excersise or insulin occlusions. Unfortunately, since these systems are open source they can not properly be compared to commercial products since they are not tested due to official standards. Also, some technical knowledge is required to use this system. 
# 

# ## Fuzzy Logic Control 
# 
# Fuzzy logic is a rule- and knowledge based system. This means that, for different scenareos different insulin reaction rules are implemented. After the rules are implemented, a defuzzification method is required to make the system friendly for the patient. This method allows for many situations to be taken into consideration when injecting insulin. However, when insulin demands change, it is a lot to maintain if the rules are many. Also, it might require expert help to implement the rules in the system. 
# 

# ## Dual-Hormone AP Systems
# 
# Dual-hormone AP systems are systems that deliver both insulin and glucagon. Glucagon has a countereffect to insulin, which makes it easier to prevent hyper- and hypoglycemia. However, it will also make the AP system more complex. We will not go into detail of such systems in this report, but they are worth mentioning. 

# ## Multi-Input AP Systems
# 
# Multi-Input AP Systems (MAPS) are artificial pancreas systems that are augmented with the use of several sensors as input. These sensors are often wearable sensors that you can find in smart watches or similar {cite}`hettiarachchi_integrating_2022`. These systems might give more informed advice, or even make decisions that are not only based on CGM measurements. That means that they might better tackle challenges in occurance of large disturbances such as meals on the glucose levels.
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




