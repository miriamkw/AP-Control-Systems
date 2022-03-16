# Introduction and background

First intro:
-	Summary of the whole report/section

TO DO!!
Add references correctly

## What is diabetes mellitus type 1?

Diabetes mellitus type 1 (T1D) is a metabolic disorder where the pancreas stops to produce and secrete insulin [2]. Followingly, insulin must be externally administered. This is traditionally done through subcutaneous infusion (SI). The disease can develop at any age, but the peak age for the diagnosis is 13 or 14 years old. According to the World Health Organization, there were 9 million people in the world diagnosed with T1D in 2017 [3]. The cause and how to prevent it is still unknown.

In non-diabetics, blood glucose concentration (BGC) lies steadily between around 4-9 mmol/l. Due to the high level of intra- and interpersonal variability in glucose-insulin dynamics it is nearly impossible to achieve the same level of stability in BGC for patients with T1D. The external factors of major impact on BGC are meals, physical activity (exercise), sleep and psychological stress (MESS), in descending order. 

T1D patients must continuously estimate their insulin demands. When over- or underestimations occur, this may lead to hypo- or hyperglycemia respectively. Hypoglycemia (BGC≤ 3.9 mmol/l) is an acute state that is symptomized by among others dizziness and can in worst case lead to diabetic coma or death. The treatment is intake of fast acting carbohydrates or glucagon injection. Hyperglycemia, on the other hand, causes long-term damage to the vascular system and increased risk of several health-related complications. Hyperglycemia is treated by insulin injections.    

## Historical background
Diabetes was already described in an Egyptian papyrus in 1550. Years went by where it remained an untreatable diagnosis. Arestaeus of Cappadocia painted the following horrific picture of the disease in the 2nd century:

“Life is short, unpleasant and painful […]. If for a while they abstain from drinking, their mouth becomes parched and their body dry; the viscera seem scorched up, the patients are affected by nausea, restlessness and a burning thirst and within a short time, they expire.” (Adapted from [4]).

Thankfully, diabetes patients must no longer face such a destiny. After years and years of experimentation and research, insulin was successfully extracted from animals in 1920 and proved efficient in regulating the BGC. 

The traditional approach for injecting insulin was using insulin pens for delivering discrete amounts of insulin. Later came the insulin pump for continuous glucose management which as of today is a common treatment method for patients with T1D. BGC measurements evolved from using a drop of blood for a single measurement to continuous glucose monitoring (CGM) systems. Recent technology for diabetes management has opened doors to create artificial pancreas (AP) systems. In 2017 the first hybrid closed-loop AP was released by Medtronic, named MiniMed 670G. This system has automated insulin delivery (AID) but require at least manual meal and exercise information.

The development of a fully closed-loop AP will require further research. Major challenges today consist of the slow dynamics of SI of insulin, delay in glucose measurements and the high level of individuality in glucose-insulin dynamics. Potential improvements that are being researched are dual hormone systems [5] (continuous infusion of both insulin and glucagon) and intraperitoneal (IP) injection of insulin. Companies are also collecting patient data to perform data analysis to determine insulin demands. These are just some of many initiatives that might contribute to achieving fully AID AP systems in the future. 

## Artificial Pancreas Control Systems
In this section we will describe the components of hybrid-loop AP systems and how they currently are working. Figure 1 illustrate how the components work together. A CGM is measuring BGC and sending the values to an AP control system. The AP control system can run inside of for example a smart phone. The patient must manually enter carbohydrate estimates for their meal intakes and make other corrections whenever necessary. Inputs could be extended to include other biometric sensor values to detect exercise or other disturbances on BGC, but such systems are currently not commercially available. The AP system calculates estimated insulin demands and performs insulin withdrawal or injections in the insulin pump. The example brands used in this section is based on the national agreement in Norway 2022 for equipment available for T1D patients [6].

``` {figure} img/Illustration_description.png
Model of an artificial pancreas system. (A) External factors like meals, exercise, stress and sleep (MESS) impact the BGC of a (B) T1D patient. (C) A CGM measures the BGC and sends it to the (E) AP control system. The control system calculates the estimated insulin requirement and provokes an injection in the (D) insulin pump.

```

### Continuous Glucose Monitor
Continuous glucose monitors are injected under the skin and is attached to the body. Depending on the manufacturer the patient must switch the injection site every 10-14 days. In commercially available products today, new readings are typically available every 5 minutes. There is a delay between actual BGC and the glucose concentration measured by the CGM in the interstitial fluid of approximately 3-12 minutes. The accuracy of the readings varies between brands, but here we will be using Dexcom G6 as an example. This CGM has an overall MARD  of 9%, and 83.3% of the readings are within ±15%  [7].

### Insulin Pump
There are two types of insulin pumps: Traditional pumps have the injection site attached to the body, following with a tube of 40-120 cm with the insulin pump filled with insulin in the end. This insulin pump has buttons and a screen so that the patient can manage insulin injections. Some of these pumps are sensor augmented, meaning that they can directly communicate with a CGM of a specific brand. The other type of insulin pump is called a patch pump. Patch pumps have the insulin reservoir and pump mechanism directly attached to the body. Insulin must be managed by an external device that wirelessly communicated with the insulin pump. Injection sites should always be switched every third day to avoid inflammation. 

Insulin pump settings are managed by the patients with the help from a doctor if necessary. Patients must manually inform the device of meal intakes or other necessary corrections. For meals or high BGC levels, a bolus dose is injected. A bolus dose is a discrete amount of insulin, and the symbol of the unit is defined as [U]. The following settings in insulin pumps are used as baseline values for AP:

### Basal rates
Basal rates are the minimum amount of insulin needed even if the patient is fasting. They are defined in units of insulin per hour, and in diurnal patterns.

Example:
| Time | Basal rate [U/h] |
| --- | --- |
| 00:00 | 1.0 |
| 04:00 | 1.2 |
| 07:00 | 1.4 |
| 12:00 | 1 |
| 17:00 | 0.8 |

### Insulin Sensitivity Factors (ISF)
Insulin sensitivities refer to drop in glucose expected from one unit of insulin. They are defined in delta glucose per unit of insulin, and in diurnal patterns.

### Carbohydrate Ratios
A carbohydrate ratio is the number of grams of carbohydrates covered by one unit of insulin. They are defined in grams per unit of insulin, and in diurnal patterns.

### Controller
The controller of an AP system is managing personalized settings, control algorithm and device communication. Hybrid-loop systems have automatic control of basal rates, but manual inputs are required to compensate for meals, exercise or other significant disturbances. Security measures must be well though through. For example, BGC values might not be available for a while, or they might be faulty. The higher complexity of a system, the more aspects might fail.
































