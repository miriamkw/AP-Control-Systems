# AP Systems Review

Now that we have established knowledge about glucose dynamics and some common control philosophies, we will take a look at current available AP systems. We will discuss their advantages and disadvantages. Lastly we will compare different AP systems and review their performance.


## Usage of Insulin Pump and CGM Therapy
Even though systems of diabetes therapies are getting more advanced, it still takes time for patients to translate to the systems. Some patients keep using their old equipment, even when they are offered to translate. This might be because of fear of change, postponements because they do not feel like they have time to learn something new or that they are pleased with the equipment they already use. Some might also prefer not having to permanently have something on their body. However, there is a clear positive trend for insulin pump and CGM therapy. {numref}`pump_sensor_evolution` shows the evolution of the percentage of diabetes type 1 patients using insulin pumps and CGMs from 1995 to 2017. As we can see it is not until quite recently (~2016) that the usage of both insulin pumps and CGMs exploded, allowing for advanced systems for automated insulin delivery. 

``` {figure} img/pump_sensor_evolution.jpg
---
name: pump_sensor_evolution
width: 600px
---
The evolution of use of insulin pumps and CGMs in patients with diabetes type 1. (A) Percentage of patients with insulin pump therapy. (B) Percentage of patients with any CGM use. Inherited from {cite}`van_den_boom_temporal_2019`.

```

## One-hormonal AP Systems

One-hormonal AP systems are the most common control systems commercially available today. These systems deliver only one hormone, insulin. There are several such systems commercially available. In this section we will go in depth into two examples of commercially available systems, which are the newest models of the providers that are used in Norway today (Medtronic AS and NordicInfu Care AB {cite}`anbud`), as well as open source systems.  

### MiniMed™ 780G and OmniPod 5

MiniMed™ 780G and OmniPod 5 are hybrid-loop system meaning that the system will automatically increase insulin injections when the patient is above range, and stop insulin infusion when glucose levels are about to get low. The systems both have a module that will automatically adjust the basal rate. Also, there is a function allowing for a bolus dose reccommendation based on a carbohydrate estimate before a meal. The MiniMed insulin pumps with automated insulin delivery through a tube with a patch attached to the body in the end, along with the Guardian™ 4-sensor ({numref}`minimed780G`). OmniPod 5 is a tubeless insulin pump that works together with a Dexcom G6 sensor.

``` {figure} img/minimed780G.jpeg
---
name: minimed780G
width: 600px
---
 Inherited from [the Medtronic website](https://www.medtronic-diabetes.com/no-NO/insulinpumpebehandling/minimed-780g-systemet).

```

Advantages:
- Automatically tuning of basal rates
- Bolus dose reccomendations before a meal based on carbohydrate estimates
- OmniPod 5 can be managed by a smartphone and is tubeless

Disadvantages:
- The patient must manually tune carbohydrate ratio, insulin sensitivity factor as well as fallback values for the basal rates
- The patient must manually enter a carbohydrate estimate before a meal
- Since the control system is solemnly based on historical data of insulin injections and glucose levels, it is not able to pick up anomalies such as illness, which may disturb the control system
- Because of the delay of onset of insulin and the amount of time insulin stays in the body, it will often fail to avoid hyper- or hypoglycemia

### "Do It Yourself" (DIY) Systems

Medical technology is strictly restricted, and commersialization of such technology takes years. That means that sometimes, the patients or relatives takes the development of the systems in their own hands. This is what happend in the T1D community: several "do it yourself" (DIY) systems are created. They require the users to build the apps themselves from open source repositories, because they are not commercially available. When patients are eating, excercising or experiencing other changes in insulin needs, they need to manually initiate changes in the app. However, these algorithms are programmed to automatically adjust insulin doses, especially during sleep. 

There are three central DIY-systems {cite}`open_source_2019`:
- [Loop](https://loopkit.github.io/loopdocs/) (iOS)
- [OpenAPS/FreeAPS X](https://openaps.readthedocs.io/en/latest/) (Android/iOS)
- [AndroidAPS](https://androidaps.readthedocs.io/en/latest/) (Android)

They are compatible with several commercial insulin pumps and CGMs. In addition it is required to buy a bluetooth bridge to make communication with the insulin pump possible. It is not known exactly how many users such systems have, but there are at least several thousands {cite}`open_source_2019`. Determining the quality of glucose control of such systems is more difficult than commercially available systems because there are not the same processes for reporting problems. However, there is only one report of two severe hypoglycemic events.  

Advantages:
- You can control insulin from the phone or a smart watch, making it very seamless to use
- The algorithms are open source and completely transparent
- An expert user can customize the algorithm and optimize it for the individual 
- The algorithms can quickly and incrementally improve, in contrast to commercial products that have to test and verify all their changes with a strict approval process
- Glucose prediction

Disadvantages:
- Legal concern {cite}`open_source_2019`
    - Practicioners can not reccomend the systems
    - No one has the formal responsibility if something goes wrong
- Technical knowledge is an advantage
- It is not guaranteed that the systems will be maintained because it is driven by volunteers
- The patient has to manually tune basal rates, carbohydrate factors and insulin sensitivity factor (unless they are using [Autotune](https://autotuneweb.azurewebsites.net/))
- It can cause problems if the system gets hacked (this also includes commercially available systems, obviously, but since they are not publicly regulated they might be more volunerable)


## Bi-Hormonal AP Systems

One-hormonal AP systems come to short during hypoglycemia, since insulin can only make glucose levels decrease. That is why someone developed the bi-hormonal systems, extending the system with glucagon. Two research groups have obtained CE or US FDA approval on such systems, namely Beta Bionics and Inreda, although they are not yet  available in Norway {cite}`review_2021`. Several studies have shown that bi-hormonal systems can perform better than one-hormonal AP systems {cite}`review_2021`.

Advantages:
- Have a hormone to avoid hypoglycemia
- The algorithm can be more agressive with the insulin and hence avoid hyperglycemia
- Might mitigate or reduce the need for manual inputs from the patients

Disadvantages: 
- Increased complexity of the systems means that more things can go wrong
- The current formula existing of glucagon is not as stable as insulin, and should only be used for 24 hours after mixed with water
- There are not established good models for the effect of glucagon yet
%- one can use all the glucose storage


## Muti-Input AP Systems

There are several studies on creating multi-input AP systems, however none of them are commercially available {cite}`hettiarachchi_integrating_2022`. The inputs used consist of inputs from wearables, such as accelerometer, heart rate and galvanic skin response. Invasive inputs such as lactate and adrenaline was incorporated in one of the studies. 2 patents of MAPS are created by a research group at Illinois Institute of Technology.

Advantages:
- Make more informed advice or choices for the patient
- Might mitigate or reduce the need for manual inputs from the patients

Disadvantages: 
- Increased complexity of the systems means that more things can go wrong
- Simulators today are not complex enough to include biometric or other variables, which means that testing has to be either purely theoretical, or in vivo


## Comparison

All the systems have in common that they require meal anouncement and individual tuning. All though there exists components that are supposed to compensate for unannounced meals and tuning, they can usually not be used as a fully-closed loop system.

In the table below we have used results from the most recent clinical trials of the systems, and are inherited from {cite}`review_2021` and {cite}`lum_real-world_2021` for commercial and open source systems respectively.

| Insulin Pump | Algorithm | Year | Age | Duration | Time in Range (70-180 mg/dL) |
| --- | --- | --- | --- | --- | --- |
| Minimed 780G | PID | 2021 | 7-80 | 4 weeks | 70.4% |
| OmniPod 5 | MPC | 2021 | ≥6 | 2 weeks | 75.1% |
| Loop | MPC | 2021 | ≥6 | 6 months | 73% |
| Bihormonal iLet | MPC (insulin), PD (glucagon) | 2021 | ≥18 | 7 days | 79% |
| Inreda Diabetic AP | PID | 2021 | ≥18 | 2 weeks | 86.6% |



## Discussion

Comparing AP systems is not simple. First and foremost, commercial providers keep their algorithms closed from the public. Consequently, one can not externally verify and compare the algorithms with an FDA approved simulator for example. Common metrics to measure the performance of an AP system are HbA1c, time in range (TIR) and time below range (TBR). These metrics give an indication of the performance, but do not contain all the relevant information. Different experiments differ in duration, the number of research subjects, the distribution of research subjects and the environment that the experiments are performed in. Hence they can not blindly be compared. 

User satisfaction with the system is also cruicial. If there is no demand for the product, it does not matter how well it performs on the glucose levels. User satisfaction can be affected by factors such as usage comfort, user interface, design and usability. Last but not least, how many manual interactions does the patient have to have with the system? How long is the period to adapt the parameters optimally, and how often are they required to tune the parameters? Are the alarms too intrusive?  




















