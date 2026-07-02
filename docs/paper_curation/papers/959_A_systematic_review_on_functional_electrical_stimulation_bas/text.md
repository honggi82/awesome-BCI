TYPE Systematic Review PUBLISHED December DOI   .    /fneur.    .       

OPEN ACCESS

EDITED BY

Teresa Paolucci, University of Studies G. d’Annunzio Chieti and Pescara, Italy

REVIEWED BY

Jorge Mercado-Gutierrez, National Institute of Rehabilitation Luis Guillermo Ibarra Ibarra, Mexico Jimena Quinzaños, National Institute of Rehabilitation Luis Guillermo Ibarra Ibarra, Mexico

*CORRESPONDENCE

Muhammad Ahmed Khan

muhkhan@stanford.edu

RECEIVED August ACCEPTED November PUBLISHED December

CITATION

Khan MA, Fares H, Ghayvat H, Brunner IC, Puthusserypady S, Razavi B, Lansberg M, Poon A and Meador KJ (    ) A systematic review on functional electrical stimulation based rehabilitation systems for upper limb post-stroke recovery. Front. Neurol.   :       . doi:   .    /fneur.    .       

COPYRIGHT

© Khan, Fares, Ghayvat, Brunner, Puthusserypady, Razavi, Lansberg, Poon and Meador. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

# A systematic review on functional electrical stimulation based rehabilitation systems for upper limb post-stroke recovery

Muhammad Ahmed Khan , , *, Hoda Fares , Hemant Ghayvat , Iris Charlotte Brunner , Sadasivan Puthusserypady , Babak Razavi , Maarten Lansberg , Ada Poon and Kimford Jay Meador

Department of Neurology and Neurological Sciences, Stanford University, Palo Alto, CA, United States, Department of Electrical Engineering, Stanford University, Palo Alto, CA, United States, Department of

Health Technology, Technical University of Denmark, Lyngby, Denmark, Department of Electrical, Electronic, Telecommunication Engineering and Naval Architecture (DITEN), University of Genoa, Genoa, Italy, Department of Computer Science, Linnaeus University, Växjö, Sweden, Department of Clinical Medicine, Hammel Neurocenter, Aarhus University, Hammel, Denmark

Background: Stroke is one of the most common neurological conditions that often leads to upper limb motor impairments, signiﬁcantly a ecting individuals’ quality of life. Rehabilitation strategies are crucial in facilitating poststroke recovery and improving functional independence. Functional Electrical Stimulation (FES) systems have emerged as promising upper limb rehabilitation tools, o ering innovative neuromuscular reeducation approaches.

Objective: The main objective of this paper is to provide a comprehensive systematic review of the start-of-the-art functional electrical stimulation (FES) systems for upper limb neurorehabilitation in post-stroke therapy. More speciﬁcally, this paper aims to review di erent types of FES systems, their feasibility testing, or randomized control trials (RCT) studies.

Methods: The FES systems classiﬁcation is based on the involvement of patient feedback within the FES control, which mainly includes “Open-Loop FES Systems” (manually controlled) and “Closed-Loop FES Systems” (brain-computer interfaceBCI and electromyography-EMG controlled). Thus, valuable insights are presented into the technological advantages and e ectiveness of Manual FES, EEG-FES, and EMG-FES systems.

Results and discussion: The review analyzed studies and found that the use of FES-based rehabilitation systems resulted in favorable outcomes for the stroke recovery of upper limb functional movements, as measured by the FMA (Fugl-Meyer Assessment) (Manually controlled FES: mean di erence =  . ,   % CI ( .  ,  . ), P <  .   ; BCI-controlled FES: mean di erence =  .  ,   % CI ( . ,  . ), P <  .   ; EMG-controlled FES: mean di erence =   .  ,   % CI (  .  ,   . ), P <  .   ) and ARAT (Action Research Arm Test) (EMGcontrolled FES: mean di erence =   . ,   % CI ( . ,   . ), P <  .   ) scores. Furthermore, the shortcomings, clinical considerations, comparison to non-FES systems, design improvements, and possible future implications are also discussed for improving stroke rehabilitation systems and advancing post-stroke recovery. Thus, summarizing the existing literature, this review paper can help researchers identify areas for further investigation. This can lead to formulating research questions and developing new studies aimed at improving FES systems and their outcomes in upper limb rehabilitation.

KEYWORDS

stroke, rehabilitation, functional electrical stimulation (FES), upper limb neurorehabilitation, post-stroke therapy, stroke rehabilitation systems

## Introduction

Stroke occurs when blood ﬂow to the brain is acutely compromised, resulting in neural injuries and subsequently functional impairment and sometimes long-term disabilities (1, 2). This life-changing event can signiﬁcantly impair cognitive, emotional, and physical functions. Studies show that individuals convalescing from a stroke frequently experience feelings of frustration, helplessness, and social isolation, which can lead to a higher risk of depression and a reduced capability to perform daily activities (3, 4). A study estimated that in 2016, stroke caused approximately 5.5 million deaths and 116.4 million DALYs (disability-adjusted life-years) worldwide (5). Among stroke survivors, upper limb hemiparesis, i.e., weakness or lack of ability to move the upper limb on one side of the body is a common condition (6). Further, ∼55–75% of stroke patients with a hemiplegic arm still have a defective function in arm movements after 3 to 6 months of rehabilitation (7).

Post-stroke care primarily aims to rehabilitate patients to eﬀectively recover lost functions and help them in their daily activities. This allows them to have their independence and reintegrate into society. Among diﬀerent rehabilitation methods, occupational and physical therapies are the most common stroke rehabilitation methods for restoring motor functions (8). These approaches use task-speciﬁc and repetitive training to induce motor recovery, leveraging innate motor learning and neuroplasticity mechanisms. However, functional recovery is not always satisfactory, as only 20% of patients are fully able to resume their social life after physical rehabilitation (9). This shows a signiﬁcant gap in the overall eﬀectiveness of the rehabilitation and recovery processes, thus indicating the need for new approaches to restore patients’ functional mobility and ultimately improve their quality of life (10).

Advancements in science and technology have introduced diﬀerent stroke rehabilitation methods, among which the functional electrical stimulation (FES) is commonly being used (11). FES is a rehabilitation tool for restoring the motor skills of stroke survivors by applying electrical impulses through the skin surface to stimulate targeted nerves, thus instigating movements in paretic muscles (12–14). Electrical stimulation applied to the muscle is controlled so that the movement produced will provide a useful function and not a random trajectory. Depending on their mode of operation, FES systems fall into 2 major types: Open-loop FES and Closed-loop FES systems (Figure 1). In open-loop systems, FES is mainly applied by a therapist using preprogrammed patterns that cannot be controlled by the patient feedback to initiate the muscle activation (Figure 1A). Open-loop FES was ﬁrst introduced to hemiplegia patients by Moe and Post (15) and later improved by Kralj et al. to treat patients with neural disorders (16). Many studies have validated the eﬃcacy of open-loop FES in upper limb stroke rehabilitation application (17–24).

Rehabilitation therapies aim to restore brain connections that subserve motor recovery and function. Along with the therapist’s assistance, the patient’s active participation via feedback loop can further improve recovery outcomes. In this regard, closedloop FES systems play a substantial part, mainly including braincomputer interface (BCI) and electromyogram (EMG) controlled

FES systems (Figures 1B, C, respectively). In BCI-FES (also called electroencephalogram (EEG)-FES), motor imagery (MI) paradigms facilitate an eﬀective approach to neurorehabilitation (25–28). A BCI system provides a direct interaction channel between the brain and a peripheral device by translating the brain’s electrical activities (as captured by EEG) into control/command signals. For rehabilitation application, the MI training consists of representing imaginary movements of limbs without physically performing them. During rehabilitation, the MI activates the neural circuits involved in actual movements and could induce functional redistribution of neuronal circuits through neural plasticity (29– 31). An MI-BCI is a computer-based system that records the EEG signals and translates the user’s intention to perform the speciﬁc task based on MI events. Thus, the EEG signal is used to generate a muscle electrical stimulation pattern that matches the intended movements of user (the user imagines and tries to perform that movement). Such MI-BCI methods with FES systems have widely been used in stroke rehabilitation for motor and functional recovery (32–45).

Besides EEG, EMG-controlled FES has been proven to be an eﬃcient method for stroke rehabilitation. EMG signal measures the electrical currents generated in muscles during their contraction, representing neuromuscular activity (46). Using EMG as feedback in the EMG-FES device enables real-time analysis of muscle activity and adjusts the amount of FES stimulation based on the muscle’s requirement (47–49). Thus, the resulting movement and intrinsic multisensory activation are paired with the subject’s active attention and intention. Furthermore, the muscle contraction is modulated by the subjects themselves, hence, facilitating fast motor learning and recovery of lost function. Finally, EMG-controlled FES limits the chances of excess electrical stimulation of muscles, which otherwise can cause muscle cramps and fatigue (50). Diﬀerent studies have been performed to develop and test EMG-controlled FES systems for stroke rehabilitation applications (51–58).

To date, diﬀerent review papers have been published regarding stroke rehabilitation, which include FES in rehabilitation engineering (59), the usability of FES in upper limb stroke rehabilitation (60), the eﬀectiveness of upper limb FES after stroke (12), devices used in muscular electrical stimulation for stroke rehabilitation (61), EMG-triggered/controlled electrical stimulation for motor recovery of the upper limb (48), BCI systems for post-stroke rehabilitation (11, 62, 63), ﬂexible technology in stroke rehabilitation systems (64), home-based technologies for stroke rehabilitation (65), eﬃcacy of robotic exoskeleton for gait rehabilitation (66), game-based virtual reality system for upper limb rehabilitation (67), and diﬀerent techniques to stimulate upper extremity stroke recovery (68). However, no review article lists and discusses the diﬀerent types of FES systems for upper limb stroke rehabilitation. Hence, in this systematic review, we assessed the RCT, and feasibility testing studies related to diﬀerent FES-based rehabilitation systems to determine their impact on improving upper limb functional movements among stroke patients. By examining the eﬀectiveness and implications of various FES approaches, this review also provides a comprehensive overview of the potential beneﬁts and challenges associated with FES-based stroke rehabilitation, oﬀering insights into the future direction of this promising therapeutic modality.

|[Figure 1]<br><br>FIGURE<br><br>Types of FES based rehabilitation system for stroke recovery (A) Open-Loop FES System, (B) Closed-Loop FES System (BCI-FES), (C) Closed-Loop FES System (EMG-FES).|
|---|

## Methods

We followed the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines for the systematic review. Three researchers independently performed the search strategy, eligibility criteria, and data extraction of included studies.

 .  Search strategy

The review was conducted using four academic electronic databases including ScienceDirect, PubMed, Scopus, and IEEE databases using the keywords: stroke rehabilitation, functional electrical stimulation (FES), RCT, feasibility testing, upper limb functional movements, brain-computer interface (BCI), EMG-based rehabilitation, BCI-based rehabilitation, EEG-based rehabilitation, neurorehabilitation devices, upper limb rehabilitation, EMG-controlled FES, BCI-controlled FES, EEG-controlled FES. Figure 2 illustrates the PRISMA ﬂow chart of study selection. Initially, 923 research articles were found from a keyword search in the diﬀerent databases. Among them, 181 duplicates were removed. Then, the remaining 742 papers were evaluated, and based on their titles and abstract, 313 articles were excluded. Lastly, full-text screening was performed and only 25 manuscripts fulﬁlled the inclusion criteria and were included in this review paper. Of these, 8, 13, and 4 manuscripts involved open-loop FES, closed-loop BCI/EEG-FES, and closed-loop EMG-FES systems, respectively.

 .  Eligibility criteria

A systematic search was performed based on predeﬁned inclusion criteria (IC) and exclusion criteria (EC). In the ﬁnal stage, only those research papers were selected that met all the conditions listed below:

IC1: Written in English. IC2: Published on or after the year 2009. IC3: Related to FES-based stroke rehabilitation in terms of

“Manually operated” OR “BCI/EEG controlled” OR “EMG controlled”.

IC4: Focus on upper limb stroke rehabilitation. IC5: Have validated the system performance on stroke patients

(feasibility study OR RCTs). EC1: Application other than stroke. EC2: For lower limb stroke rehabilitation. EC3: Testing only on healthy individuals.

 .  Data extraction

Three authors independently extracted the following information of each included study: type of used rehabilitation system, experimental and control groups, application as RCT/feasibility study, upper limb targeted areas, total number of therapy sessions, therapy session time and outcome measures/performance evaluation. Any disagreement during the process of data extraction were resolved through discussion among three authors.

|[Figure 2]<br><br>FIGURE<br><br>PRISMA ﬂow chart of study selection.|
|---|

 .  Quality assessment

 .  Statistical analysis

The methodological quality and risk of bias of the included studies were assessed using validated tools. For randomized controlled trials, the Risk of Bias 2 (ROB2) tool was used to evaluate potential bias across ﬁve domains–randomization, deviations from intervention, missing outcome data, outcome measurement, and selection of reported results (69). The quality of observational case series studies was appraised using the NIH Quality Assessment tool, which contains 9 items assessing aspects like study objective, population description, intervention clarity, outcome validity, and follow-up (70). Finally, the included case reports were critically appraised using the Joanna Briggs Institute (JBI) checklist for case reports (71). This tool evaluates key domains such as patient demographics, clinical history, diagnosis assessment, intervention details, and outcome measures.

Continuous data was analyzed using OpenMetaAnalyst software. A ﬁxed eﬀect model calculated mean diﬀerences (MD) with 95% conﬁdence intervals (CI) for continuous outcomes. Statistical homogeneity and heterogeneity were assessed using the I2 statistic. An I2 value >50% was considered indicative of substantial heterogeneity.

## Results

 .  Risk of bias in included studies

Among a total of 25 included studies, the quality of the 9 RCTs (17, 32–36, 51, 55, 56) was assessed using the “Risk of Bias 2 (ROB2)” tool (Supplementary Figures S1, S2). Overall, most

studies were rated as having a low risk of bias in terms of the randomization process, missing outcome data, and measurement of the outcome. However, in 4 studies (17, 32, 33, 35), some concerns were identiﬁed regarding deviations from intended interventions, resulting in a rating of “some concerns.” The remaining ﬁve studies (34, 36, 51, 55, 56) were found to have an overall “low risk” of bias.

The quality of the 11 observational case series studies (18–22, 24, 41, 43–45, 58) was assessed using the “NIH Quality Assessment” tool. Based on the assessment, 7 studies were determined to be of “good quality”, while 4 studies were evaluated as “fair quality” (Supplementary Table S1). In addition, ﬁve case reports (23, 37, 38, 40, 42) were included and appraised using the “Joanna Briggs Institute (JBI) Critical Appraisal” tool. The overall quality of each case report was “good” based on the JBI checklist (Supplementary Table S2).

###  .  Included studies regarding types of FES-based stroke rehabilitation systems

 . .  Open-loop FES system: pre-deﬁned FES for stroke rehabilitation

An open-loop FES system comprises of a manually controlled device, which is operated by a therapist. During the therapy session, the therapist manually administers electrical stimulation to the speciﬁc muscles of the patient, using patient-speciﬁc predetermined stimulation parameters such as stimulation intensity, time duration, and ON/OFF cycle.

Numerous studies have been conducted utilizing open-loop FES systems for stroke rehabilitation to regain upper limb motor functions. Experimenting with the eﬀectiveness of FES, Nakipoglu Yuzer et al. (17) applied FES (two channels and four surface electrodes) to the spastic muscles of 30 patients (an RCT), and the improvement of clinical scores indicates that FES eﬀectively reduces wrist ﬂexor spasticity. In (18), Makowski et al. showed that FES produces functional hand opening when the patient is relaxed, but it is overpowered by ﬁnger ﬂexor coactivation when the patient voluntarily exerts eﬀort to reach/open the hand. For that, their study proves that the amount of hand opening grows signiﬁcantly (3.2–8.8cm) when including FES for both reaching and hand opening muscles even in the presence of submaximal or zero eﬀort. Moreover, Meadmore et al. (19) investigated FES of shoulder, elbow, and wrist muscles: ﬁve patients underwent 18 sessions and completed FMA (Fugl-Meyer Assessment) and ARAT (Action Research Arm Test) assessments. The study showed an improvement of 4.4, providing evidence that the integration of low-cost hardware with advanced FES controllers can reduce upper limb impairment. Sun et al. (20) reported the FES for upper limb functional activity practice, used by 9 therapists to set 8 sessions activities with 22 stroke patients. Among them, 17 patients showed a session completion rate >90%, demonstrating its capability of delivering high-intensity therapy compared to traditional face-to-face therapy. Also, Niu et al. (21) illustrated a technique for creating FES patterns based on muscle synergies of a normal subject (three patients–adjusted for each participant and task) using a programmable FES device. Followed by 5day sessions of intervention using synergy-based FES delivery

to another three patients. The outcome of the new technology was measured by improvement in FMA scores (28.6% ± 13.7%). In Chou et al. (22), made use of the latter in the design and test of an automated synergy-based FES system to match electrically induced movements to assist residual movements of patients. Results based on changes in FMA scores indicate that the synchronization produced more consistent compound movements with reduced RMS (root mean square) errors under diﬀerent triggering conditions. Martín-Odriozola et al. (23) developed the Fesia Grasp device used for hand dexterity rehabilitation of a 69yearold post-ischemic stroke woman. Following their ﬁrst study (21), Niu et al. (24) conducted a TOT (Task-oriented training) protocol with repeated forward and lateral reaching movements assisted by synergy-based FES on 16 patients, divided into FES (EG) and Sham (CG) groups over 5-days. Findings of higher FMA than Sham indicate eﬃcacy of open-loop FES system in post-stroke rehabilitation. A detailed overview of research studies regarding open-loop FES rehabilitation is provided in Table 1.

 . .  Closed-loop FES system: BCI controlled FES for stroke rehabilitation

According to Hebb’s principle “cells that ﬁre together wire together” (72, 73), suggesting that the coordination of cortical and physical activities during the rehabilitation therapies could lead to an eﬀective improvement of the impaired motor function (74–77). Therefore, a more eﬀective approach may be to interface the FES rehabilitation device with an external system that could enhance the simultaneous activation of the motor cortex during the rehabilitation sessions. In this regard, MI-based BCI systems are an optimum choice, which allows the rehabilitation system to perform the required task based on the patient’s imagination of intended motion, allowing more active participation of brain throughout the stroke therapy (78).

A BCI-FES rehabilitation system mainly comprises of a BCI unit (containing EEG element), BCI-FES interface component, and FES module. Some BCI-FES systems also incorporate a virtual reality (VR) paradigm as a part of their setup (Figure 3). In such systems, ﬁrstly, the patient is provided the VR environment (on screen or the headset) that contains the pre-programmed therapy session of targeted motion e. g., hands extension/ﬂexion (Figure 3A). The patient will be asked to imagine the task execution displayed in the virtual environment. Each task imagination generates a speciﬁc EEG signal, which will be acquired and processed by the BCI unit (Figure 3B). Depending on the imagination, the BCI-FES interface generates a trigger command to control the ON/OFF state of FES stimulation and will also control the stimulation parameters (Figure 3C). Lastly, the FES device provides electrical stimulation to the impaired muscles and hence, facilitate performing the required movements (Figure 3D). To make the strategy eﬀective, the user typically undergoes training to establish a connection between their brain signals and speciﬁc motor tasks. This training involves practicing mental tasks or visualizing movements to generate distinct brain patterns that the BCI can recognize and translate into commands for the FES device.

BCI-FES systems are widely used for stroke rehabilitation and several randomized controlled trial (RCT) studies have been

TABLE Research studies and their outcomes for open-loop FES neurorehabilitation systems.

|Open-loop FES systems for upper limb stroke rehabilitation<br><br>| | | | |
|---|---|---|---|---|
|Study|Commercial/ customized open-loop FES rehabilitation system<br><br>|Experimental group (EG) and control group (CG)|i. Upper limb targeted areas<br>ii. Total sessions<br>iii. Therapy time/session<br>|Outcome measures/ performance evaluation/other comments<br><br>|
|Nakipoglu Yuzer et al.<br><br>(17)|Customized<br><br>|RCT EG and CG: 30 post-stroke hemiplegic patients were randomly divided into EG and CG. FES was only applied to EG.|i. Wrist and ﬁnger extensors for wrist ﬂexor spasticity<br>ii. 20<br>iii. 30 min<br><br><br>|BI (EG) = 6.34 ± 1.06 BI (CG) = 3 ± 1.02 RMA (EG) = 0.66 ± 0.2 RMA (CG) = 0.34 ± 0.31 UEFT (EG) = 0.4 ± 0.28 UEFT (CG) = 0.2 ± 0.08 AROM (EG) = 6.73 ± 0.56 AROM (CG) = 2.47 ± 0.62 MAS3 (EG) = 80%-46.7% = 33.3% MAS3 (CG) = 46.7%-40% = 6.7%<br><br>A signiﬁcant diﬀerence was found in favor of EG|
|Makowski et al. (18)<br><br>|Customized|Feasibility study EG: 5 at least 6-months post-stroke patients.<br><br>|i. Reaching and hand opening muscles<br>ii. At least 3 sessions per patient<br>iii. N/A<br><br><br>|Hand opening average of participants increased signiﬁcantly when including FES for reaching and hand opening in the presence of partial or zero reaching eﬀort: (“+” sign shows the combination of two states) HE + RE = 3cm (no stimulation) HE + RES = 3.2 cm RES + HES = 6.5 cm RES + HS = 8 cm RS + HS (0 eﬀort - relaxed) = 8.8 cm|
|Meadmore et al. (19)|Customized (feasibility study)<br><br>|Feasibility study EG: 5 stroke patients with hemiplegia CG: the same 5 patients completed 5 un-assisted tasks.|i. Shoulder, elbow and wrist muscle groups.<br>ii. 18 sessions<br>iii. 1 h<br>|The FMA and ARAT were completed 1-6 days pre and post-intervention. Improvement was signiﬁcant for both tests (Mean Results):<br><br>FMA (EG) = 23.2-18.8 = 4.4 ARAT (EG) = 7-2.6 = 4.4|
|Sun et al. (20)|Commercial FES-UPP ﬂexible system (5 channels—FSM controller—feedback software)<br><br>|Feasibility study EG: 22 patients with impaired upper limbs<br><br>|i. Upper limb muscles<br>ii. 8 tailored sessions per participant<br>iii. N/A<br>|Mean eﬃciency and mean number of successful repetitions of activities (NSR) in: Session 1: 12% Eﬃciency and 13 NSR Session 7: 34% Eﬃciency and 45 NSR 17 of 22 participants had a therapy completion rate >90%<br><br>|
|Niu et al. (21)|Customized (Synergy based FES Device)<br><br>|Feasibility study EG: 6 (3 pattern adjustment and 3 synergy-based FES testing)|i. Upper limb muscles<br>ii. 5<br>iii. 1 h<br><br><br>|Mean value of the change in FMA scores pre and post treatment indicate the improvement in functional movement.<br><br>FMA = 5.7 ± 2.5 (28.6% ± 13.7% change)|
|Chou et al.<br><br>(22)<br><br>|Customized (Automated FES System based on synergy FES)|Feasibility study EG: 5 patients (4 ischemic and 1 hemorrhagic all >MAS2) to test the system and 4 healthy patients to adjust the patterns<br><br>|i. Upper limb muscles<br>ii. 5<br>iii. 1 h<br>|The lowest RMS errors of subjects (S0) under diﬀerent trigger levels (TL) in each task (Forward or Lateral Reaching):<br><br>S02 (TL 0.3) FR: 0.796 ± 0.290<br>S03 (TL 0.5) FR: 0.511 ± 0.190<br>S04 (TL 0.2) FR: 0.499 ± 0.227<br>S05 (TL 0.2) LR: 0.810 ± 0.372<br>S06 (TL 0.5) LR: 0.732 ± 0.213<br>|
|MartínOdriozola et al. (23)<br><br>|Commercial (multi-ﬁeld fesia grasp system FES)|Feasibility study EG: 69-year-old post ischemic stroke woman|i. Left hand dexterity.<br>ii. 12<br>iii. 1 hour<br>|AROM (thumb) = +27◦ AROM (index) = +8◦ AROM (wrist) = +24◦ GS = 2.9 kg<br><br>|
|Niu et al. (24)<br><br>|Customized<br><br>|Feasibility study 16 patients with post-stroke hemiparesis EG: 9 FES CG: 7 Sham|i. 7 upper extremity muscles of elbow and shoulder<br>ii. 5<br>iii. 1 h<br><br><br>|FMA-UE scores of patients receiving FES increased by 6.67 ± 5.20 (28.13 ± 21.41%) FMA-UE scores of patients receiving Sham changed by 2.00 ± 2.38 (7.32 ± 16.11%)|

HE, Max Hand Opening Eﬀort; RE, Max Reaching Eﬀort; RS, Reaching Stimulation; HS, Hand Opening Stimulation; RES, Partial Reaching Eﬀort and Stimulation; HES, Partial Hand Opening Eﬀort and Stimulation; FMA, Fugl-Meyer Assessment; ARAT, Action Research Arm Test; BI, Barthel Index; RMA, Rivermead Motor Assessment; UEFT, Upper Extremity Functional Index; AROM, Active Range of Motion; MAS, Motor Assessment Scale; NSR, Number of Successful Repetitions of Activities; RMS, Root Mean Square; FR, Forward Reaching; LR, Lateral Reaching; UE, Upper Extremity; GS, Grip Strength.

|[Figure 3]<br><br>FIGURE<br><br>Overall representation of BCI-FES neurorehabilitation system (main components: EEG unit for BCI, BCI-FES interface, and FES module. Optional component: VR display/headset).|
|---|

performed to investigate the eﬃciency of BCI-FES systems (32–36). In (32), Cincotti et al. performed an (RCT) to restore hand grasping movements. To assess post-stroke motor recovery, the FMA, MRC (Medical Research Council), and ESS (European Stroke Scale) scores were used. The results showed that the group with BCI-FES therapy achieved better motor recovery than the conventional FES group. Likewise, Li et al. (33) targeted stroke survivors with severe upper extremity paralysis. The study compared the eﬃciency of the BCI-FES system in comparison to the conventional FES system. The result showed a motor imagery task classiﬁcation accuracy of 77%, along with a substantial improvement in the rehabilitation outcome scores within the BCI-FES group. In (34), Kim et al. accomplished an RCT to investigate the positive inﬂuence of the BCI-FES system on the motor recovery of upper extremities in stroke survivors. The measured outcomes validated the enhanced recovery via a BCI-based system compared to physical training. Additionally, in Miao et al. and Chen et al. (35, 36), the clinical application of the BCI-FES stroke rehabilitation system has been proposed to promote and improve upper extremity movements, along with motor activity restoration.

In addition to RCT, diﬀerent feasibility studies for exploring the applicability of BCI-FES systems have also been carried out (37–45). In Daly et al. (37), Daly et al. performed a pilot study in which they tested a customized BCI-FES system on a stroke survivor having a joint extension problem in the index ﬁnger. During the ﬁrst rehabilitation session, results showed a higher classiﬁcation accuracy of 97% and 83% for “attempted movement” and “imagined movements” respectively. With every session, the muscle movement was gradually improving and by the end of nine sessions, the ﬁnger extension motion was completely recovered. Additionally, Mukaino et al. (38) developed a BCIcontrolled neuromuscular electrical stimulator and conducted a case study on a stroke survivor (ﬁnger movement) to examine the eﬀectiveness of BCI in stroke therapy. The results indicated

that rehabilitation training with a BCI-controlled FES induces cortical plasticity and promotes functional recovery. Apart from customized BCI-FES stroke rehabilitation systems, “RecoveriX from g.tec” is commercially available stroke rehab systems (39). The RecoveriX system classiﬁes the right and left wrist motion intention and is only meant for the wrist dorsiﬂexion rehabilitation paradigm. Hence, to validate the eﬃcacy of RecoveriX system, Sabathiel et al. (40), Irimia et al. (41), Cho et al. (42), Qiu et al. (43), and Sebastián-Romagosa et al. (44) have conducted experiments on a set of stroke survivors for arm function restoration. Their results showed that the system depicts a classiﬁcation accuracy of up to 95%. Furthermore, signiﬁcant improvements of upper limb motor function scores suggest the post-stroke motor recovery. A detailed overview of research studies regarding BCI-FES rehabilitation is provided in Table 2.

 . .  Closed-loop FES system: EMG controlled FES for stroke rehabilitation

EMG provides information on the neural activity of muscles and can detect physical movement intentions. A method has been previously studied to engage a user during FES therapy by triggering the stimulation when a speciﬁc level of muscle activity is detected (79–83). In the “EMG triggered FES system”, the EMG signal acts as a switch to trigger the delivery of FES stimulation at a predetermined level when the EMG magnitude reaches a certain threshold. However, this approach only uses the user’s muscle activity to trigger FES and has not been conclusively proven advantageous over the open-loop FES method (79–83). Thus, another system, an “EMG controlled FES system” has been adopted that among with an FES trigger, also modulates the FES intensity in proportion to the real-time EMG signal (84).

EMG-controlled FES system mainly comprises of an EMG sensing unit, EMG-FES interface component, and FES module

TABLE Research studies and their outcomes for BCI-FES neurorehabilitation systems.

|BCI controlled FES systems for upper limb stroke rehabilitation (closed-loop system)<br><br>| | | | | | |
|---|---|---|---|---|---|---|
|Study<br><br>|Commercial/ customized BCI-FES rehabilitation system<br><br>|EEG device channels conﬁguration|Experimental group (EG) and control Group (CG)<br><br>|Therapy per participant (i. Total sessions,<br><br>ii. Runs/session,<br>iii. Trials/run or Trials/session)<br><br><br>|i. Upper limb targetedareas<br>ii. Therapytime/ session<br>|Outcome measures/ performance evaluation/ other comments|
|Cincotti et al.<br><br>(32)|Customized<br><br>|32 channels<br><br>|RCT: EG: 08 stroke patients CG (with conventional FES therapy): 08 stroke patients|i. 12<br>ii. 4<br>iii. 20 (per run)<br>|i. Hand grasping movement (FES to paralyzed hand) ii. N/A<br><br>|FMA, MRC and ESS score show a good recovery of hand function with BCI system as compared to the control group. Exact values of these scores have not been reported|
|Li et al.<br><br>(33)<br><br>|Customized<br><br>|16 channels (G.tec Guger Technologies, Graz, Austria)<br><br>|RCT: EG: 08 stroke patients CG (with conventional FES therapy): 07 stroke patients (Stroke Severity: subacute of severe level)|i. 24<br>ii. N/A<br>iii. 20 (per session)<br><br><br>|i. Upper extremity movements (FES stimulated the aﬀected hand)<br>ii. 1–1.5 h<br><br><br>|FMA and ARAT score shows signiﬁcant motor improvement.<br><br>FMA (EG) = 12.7, FMA (CG) = 6.7, ARAT (EG) = 18.0; ARAT (CG) = 7.6|
|Kim et al. (34)|Customized<br><br>|16 channels (PolyG-I by Laxtha Inc., Daejeon, Korea)<br><br>|RCT: EG: 15 stroke patients CG (with conventional physical therapy): 15 stroke patients (Stroke Severity: Chronic of moderate level)|i. 20<br>ii. N/A<br>iii. N/A<br>|i. Shoulder and wrist movement (FES stimulated the aﬀected hand) ii. 30 minutes<br><br>|Improvement in FMA, MAL, MBI, and ROM was found.<br><br>FMA (EG) = 7.9, FMA (CG) = 2.9|
|Miao et al. (35)|Commercial RecoveriX (g.tec GmbH, Austria)<br><br>|16 channels (g.tec GmbH, Austria)<br><br>|RCT: EG: 8 stroke patients CG (with conventional physical therapy): 8 stroke patients (Stroke Severity: Chronic of diﬀerent levels)|i. 3<br>ii. 2<br>iii. 60 (per run)<br>|i. Left or right wrist dorsiﬂexion (FES applied to both hands) ii. N/A|Average imagined task classiﬁcation accuracy of 72.9%. Improvement in FMA score was found.<br><br>FMA (EG) = 3.5; FMA (CG) = 0.9|
|Chen et al.<br><br>(36)|Customized<br><br>|32 channels (Neuroscan, USA)<br><br>|RCT: EG: 16 stroke patients CG (with neuromuscular stimulation): 16 stroke patients (Stroke Severity: Chronic phase)|i. 11<br>ii. As much as possible (depending on each patient)<br>iii. 10 (per run)<br>|i. Left or right wrist extension<br>ii. 40 minutes<br><br><br>|FMA and Kendall MMT scores of the BCI-FES group was signiﬁcantly higher than that in the control group.|
|Daly et al. (37)<br><br>|Customized|58 channels (SynAmps, Compumedics, El Paso, TX)|Feasibility study EG: 01 stroke patient CG: N/A (Stroke Severity: 10 months post-stroke: Chronic of moderate to severe level)<br><br>|i. 9<br>ii. N/A<br>iii. 150 (per session)<br><br><br>|i. Index ﬁnger joint extension (FES provided to isolated index ﬁnger extension)<br>ii. 1.6 h<br>|High accuracy in imagined movements (83%) and attempted movements (97%). Participants were able to execute 26 degrees of isolated index ﬁnger metacarpophalangeal joint extension|
|Mukaino et al.<br><br>(38)<br><br>|Customized<br><br>|N/A|Feasibility study EG: 01 stroke patient CG (with conventional FES therapy): Same patient (Stroke Severity: Chronic of severe level)<br><br>|(Total there are 4 phases)<br><br>i. 10 (for each phase)<br>ii. N/A<br>iii. 600 (for each phase) (per session)<br><br><br>|i. Finger movement (FES applied to the paralyzed ﬁnger)<br>ii. 1 h<br><br><br>|BCI-FES system eﬃcacy reported via FMA and MAS score.<br><br>FMA (EG) = 3.5; FMA (CG) = 0.5|

(Continued)

TABLE (Continued)

|BCI controlled FES systems for upper limb stroke rehabilitation (closed-loop system)<br><br>| | | | | | |
|---|---|---|---|---|---|---|
|Study<br><br>|Commercial/ customized BCI-FES rehabilitation system|EEG device channels conﬁguration|Experimental group (EG) and control Group (CG)<br><br>|Therapy per participant (i. Total Sessions,<br><br>ii. Runs/Session,<br>iii. Trials/Run or Trials/Session)<br>|i. Upper limb targetedareas<br>ii. Therapytime/ session<br><br><br>|Outcome measures/ performance evaluation/ other comments|
|Sabathiel et al.<br><br>(40)<br><br>|Commercial RecoveriX (g.tec GmbH, Austria) (39)|24 channels (g.Hiamp device by g.tec GmbH, Austria)<br><br>|Feasibility study EG: 02 stroke patients CG: N/A (Stroke Severity: Chronic of severe level)<br><br>|i. 24 (patient 1) and 10 (patient 2)<br>ii. N/A<br>iii. N/A<br>|i. Wrist dorsiﬂexion (FES applied to both aﬀected and unaﬀected hands)<br>ii. N/A<br><br><br>|Higher classiﬁcation accuracy obtained. Moreover, Nine-Hole Peg Test (9-HPT) is performed only of patient 1 and result shows steady improvement over about three months|
|Irimia et al.<br><br>(41)<br><br>|Commercial RecoveriX (g.tec GmbH, Austria)|45 channels (g.tec GmbH, Austria)|Feasibility study EG: 03 stroke patients CG: N/A (Stroke Severity: Chronic of severe level)<br><br>|i. 24<br>ii. 6<br>iii. 40 (per run)<br>|i. 120 left and 120 right hand movements (FES applied to both aﬀected and unaﬀected hands)<br>ii. N/A<br><br><br>|High accuracy in task execution achieved (95% in at least one session) and Nine-Hole Peg Test (9-HPT) shows improved motor function.|
|Cho et al. (42)<br><br>|Commercial RecoveriX (g.tec GmbH, Austria)<br><br>|16 channels (g.LADYbird by g.tec GmbH, Austria)|Feasibility study EG: 02 stroke patients CG: N/A (Stroke Severity: Chronic of severe level)<br><br>|i. 25<br>ii. 4<br>iii. N/A<br><br><br>|i. Left or right wrist dorsiﬂexion (FES applied to both hands) ii. 25 60-min|Improved performance observed via FMA score (pre and post BCI)<br><br>Patient 1: FMA = 21.0<br>Patient 2: FMA = 11.0<br>|
|Qiu et al. (43)|Commercial RecoveriX (g.tec GmbH, Austria)|16 channels (g.tec GmbH, Austria)<br><br>|Feasibility study EG: 10 stroke patients CG: N/A (Stroke Severity: Chronic of diﬀerent levels)|i. 12<br>ii. 2<br>iii. 30 (per run)<br><br><br>|i. Left or right wrist dorsiﬂexion (FES applied to both hands) ii. N/A|System accuracy of more than 95%. FMA score shows enhanced motor function recovery among 5 patients (pre and post BCI)|
|SebastiánRomagosa et al. (44)<br><br>|Commercial RecoveriX (g.tec GmbH, Austria)<br><br>|16 channels (g.tec GmbH, Austria)|Feasibility study EG: 51 stroke patients CG: N/A (Stroke Severity: 45 Chronic and 6 subacute phase)<br><br>|i. 25<br>ii. 3<br>iii. 80 (per run)<br><br><br>|i. Left or right wrist dorsiﬂexion (FES applied to both hands)<br>ii. 1 h<br><br><br>|Signiﬁcant increase in the motor function of aﬀected upper limb ( FMA = 4.68) Reduction of the spasticity in the wrist and ﬁngers ( MAS-wrist = −0.72<br><br>MAS-ﬁngers = −0.63)|
|Choi et al. (45)<br><br>|Customized|32 channels (G.tec Guger Technologies, Graz, Austria)<br><br>|Feasibility study EG: 08 stroke patients CG: N/A (Stroke Severity: Chronic phase)|i. 5<br>ii. N/A<br>iii. 24 (per session)<br><br><br>|i. Diﬀerent tasks from right/left hand (FES applied to the aﬀected hand) ii. 1 h|Average imagined task classiﬁcation accuracy of 71.25%.|

FMA, Fugl-Meyer Assessment; MRC, Medical Research Council; ESS, European Stroke Scale; ARAT, Action Research Arm Test; MAS, Modiﬁed Ashworth Scale; MAL, Motor Activity Log; MBI, Modiﬁed Barthel Index; ROM, Range of Motion; MMT, Manual Muscle Testing.

(Figure 4). Certain EMG-FES systems also integrate a virtual reality (VR) component into their conﬁguration. In these systems, the initial phase entails immersing the patient in a VR environment, which can be presented on a screen or through a headset (Figure 4A). This VR environment includes a pre-programmed therapy session focused on speciﬁc movements, such as hand extension or ﬂexion. Before the start of a therapy session, the system is calibrated for setting the EMG threshold level and required maximum FES stimulation (varies across subjects). The subject tries to perform the required task (for instance, wrist extension) and the intended motion is physically detected by the EMG sensing unit via analyzing the muscle activity (Figure 4B).

The acquired EMG signal is processed by the EMG-FES interface and once the myoelectric activity reaches the pre-deﬁned threshold level, the interface unit sends the trigger command to start the FES (Figure 4C). The applied stimulation activates the targeted muscle (or group of muscles) and helps the subject to achieve the desired motion (Figure 4D). In EMG-FES controlled system, the amount of stimulation does not stay constant and automatically adjusts throughout the therapy sessions proportional to real-time muscle activity.

Shindo et al. (51) performed an RCT to test the eﬃcacy of the myoelectrical controlled electrical stimulator developed by Muraoka (52). The therapy sessions were performed for ﬁnger

|[Figure 4]<br><br>FIGURE<br><br>Overall representation of EMG-FES neurorehabilitation system (main components: EMG sensing unit, EMG-FES interface, and FES module. Optional component: VR display/headset).|
|---|

extension rehabilitation (i.e., a functional opening of the hand) which lasted for 3 weeks (5 days/week). The EMG electrodes were placed on the paretic extensor digitorum communis muscles and based on the muscle activities the amount of applied stimulation was controlled. After completion of rehabilitation sessions, pre, and post-performance was evaluated via diﬀerent clinical score metrics (FMA and ARAT). They found that the EMG-controlled FES was able to induce a greater level of improvement as compared to the control group. In (53, 54), an EMG-controlled FES system, “MeCFES” has been developed by Thorsen’s group for upper limb stroke rehabilitation, which was tested via RCT on 11 stroke survivors (55). In the experimental group, the EMG electrodes were placed on wrist and ﬁnger extensors and their recorded muscle activity was used to control the applied electrical stimulation for wrist and ﬁnger extension. The clinical evaluation was performed through the ARAT, and results showed that the participants treated with MeCFES had a signiﬁcant improvement in upper limb motor function. In (56), Thorsen’s group conducted another RCT in which they tested the MeCFES for task-oriented therapy (TOT). This was the ﬁrst large RCT (68 stroke survivors) in which multiple rehabilitation centers validated the performance of MeCFES-assisted TOT against standard TOT. In the end, promising results were obtained in terms of MeCFES functioning, and no adverse events were reported in any of the centers. They concluded that MeCFES is a safe and eﬃcient myo-controlled FES system for the motor recovery of upper extremities among stroke survivors. Recently (57), they developed an updated version of MecFES, named “FITFES”, which is wearable and portable in an ambulatory setting and best suitable for TOT applications. Thus far, only a working prototype has been tested on a single subject and no clinical evaluation has been performed. Moreover, Hara et al. (58) investigated the relationship between brain cortical perfusion (BCP) changes in the sensory-motor cortex (SMC) area and arm function improvement. A near-infrared spectroscopy (NIRS) approach was adopted to analyze BCP changes. It was

found that EMG-FES rehabilitation improved FMA and GS (grip strength) scores. Also, NIRS showed increased SMC activation during therapy, conﬁrming the functional improvement due to the EMG-FES system. A detailed overview of research studies using EMG-FES rehabilitation is provided in Table 3.

 .  Meta-analysis interpretation

 . .  Change in fugl-meyer assessment (FMA) score

Among open-loop FES systems, the pooled analysis of 3 studies (19, 21, 24) including 17 stroke patients showed a signiﬁcant increase in FMA score [MD = 5.6, 95% CI (3.77, 7.5), P < 0.001], and the data were found to be homogenous (I2 = 0, P = 0.657) (Supplementary Figure S3).

For BCI-controlled FES, the meta-analysis of 6 studies (33– 36, 38, 44) with a total of 99 patients exhibited an improvement in FMA score [MD = 5.37, 95% CI (4.2, 6.6), P < 0.001], along with the homogeneity in data (I2 = 0, P = 0.198)

- (Supplementary Figure S3). Finally, after analyzing the data from 3 EMG-controlled FES

studies (51, 56, 58) involving 60 patients, it was found that EMGFES rehabilitation led to a signiﬁcant increase in FMA score [MD = 14.14, 95% CI (11.72, 16.6), P < 0.001], and the data were homogenous (I2 = 0, P = 0.006) (Supplementary Figure S3).

 . .  Change in action research arm test (ARAT) score

The meta-analysis of 3 EMG-based FES studies (51, 55, 56) including 49 patients indicated a statistically signiﬁcant increase in the ARAT score [MD = 11.9, 95% CI (8.8, 14.9), P < 0.001], and the data demonstrated homogeneity (I2 = 0, P = 0.534)

- (Supplementary Figure S4).

TABLE Research studies and their outcomes for open-loop FES neurorehabilitation systems.

|EMG Controlled FES systems for upper limb stroke rehabilitation (closed-loop system)<br><br>| | | | |
|---|---|---|---|---|
|Study|Commercial/ customized EMG-FES rehabilitation system<br><br>|Experimental group (EG) and control group (CG)|i. Upper limb targeted areas<br>ii. Total sessions<br>iii. Therapy time/session<br>|Outcome measures/ performance evaluation/other comments<br><br>|
|Shindo et al.<br><br>(51)|Customized (two channels EMG) (52)<br><br>|RCT: EG: 12 stroke patients CG (physical and occupational therapy without FES): 12 stroke patients (Stroke Severity: stroke within 60 days of onset: Subacute level)<br><br>|i. Fingers extension<br>ii. 15<br>iii. N/A<br><br><br>|Diﬀerent clincal scores show signiﬁcant motor improvement.<br><br>FMA (EG) = 12.2 ± 5.3; FMA (CG) = 5.5 ± 6.0 ARAT (EG) = 13.2 ± 7.6; ARAT (CG) = 8.3 ± 8.1|
|Thorsen et al.<br><br>(55)|Customized MeCFES (53, 54) (multi-channel EMG)<br><br>|RCT: EG: 5 stroke patients CG (conventional FES without EMG): 6 stroke patients<br><br>|i. Wrist and ﬁnger extension<br>ii. 25<br>iii. 45 min<br>|Improvement in ARAT score<br><br>ARAT (EG) = 9.0; ARAT (CG) = 2.0<br><br>|
|Jonsdottir et al. (56)|Customized MeCFES (53, 54) (multi-channel EMG)|RCT: EG: 32 stroke patients CG (task oriented standard therapy without FES): 36 stroke patients (Stroke Severity: Chronic and subacute level)<br><br>|i. Task-oriented arm rehabilitation<br>ii. 25<br>iii. 45 min<br><br><br>|Improvement in clinical scores FMA (EG) = 4.5; FMA (CG) = 3.5 ARAT (EG) = 3.0; ARAT (CG) = 2.0|
|Hara et al. (58)<br><br>|Commercial PAS System GD601 (t–wo channels EMG) (OG GIKEN Company, Okayama, Japan)|Feasibility study EG: 16 stroke patients CG: N/A (Stroke Severity: Chronic with moderate residual hemiparesis)<br><br>|i. Supination and pronation, ﬂexion and extension of individual ﬁngers. Flexion and extension of the wrist. Flexion and extension of the elbow. Adduction and abduction of the shoulder.<br>ii. 20-40 sessions<br>iii. 40 min<br><br><br>|Diﬀerence in pre and post rehabilitation scores show a good recovery of physical functions.<br><br>FMA = 20.0; GS = 5.5 ± 11.0|

FMA, Fugl-Meyer Assessment; ARAT, Action Research Arm Test; GS, Grip Strength.

## Discussion

FES-based stroke rehabilitation systems have been increasingly used as a therapeutic tool to restore physical movements with post-stroke motor impairment. The rehabilitation outcomes may vary depending on the type of FES administered (open-loop or closed-loop). In either case (open-loop/closed-loop), the patient is instructed to actively attempt the required task, hence ensuring the cortical involvement during the training that plays a vital role in motor recovery. This review paper provides an in-depth literature review of open-loop and closed-loop FES systems for upper limb rehabilitation in terms of their design, advantages, and clinical stroke application (including RCTs and feasibility studies). We conducted a meta-analysis of the included studies to assess the eﬀectiveness of diﬀerent FES-based upper limb rehabilitation systems (Pre-deﬁned FES, BCI-FES, and EMG-FES). Firstly, we performed the quality assessment of the included articles to ensure the high quality of the provided information. As a result, it was found that most of the articles come under the “Good” quality category. Additionally, all the studies in our analysis exhibited homogeneous data. Data homogeneity in metaanalysis suggests that the ﬁndings from individual studies are

consistent with each other, thereby enhancing the reliability of drawing conclusions from the aggregated data. Moreover, the statistical analysis was performed individually on each study within sub-groups of “Pre-deﬁned FES, BCI-controlled FES, and EMGcontrolled FES”. The meta-analysis results showed that each FESbased rehabilitation system signiﬁcantly improved upper limb motor function in stroke patients, as measured by FMA and ARAT scores (Supplementary Figures S3, S4). Despite comprehensive search strategies, there is a possibility of having the following limitations in our review process:

- • Incomplete Retrieval of Studies: It is possible to miss relevant studies, especially if they are published in non-indexed journals, not available in electronic databases, or written in languages not included in the search criteria.
- • Reporting Bias: In some cases, relevant data is incomplete or unavailable. For instance, some studies have not reported the outcome measures that are used to assess the eﬀectiveness of interventions and track the progress of individuals recovering from a stroke. Hence, incomplete reporting of outcomes can lead to reporting bias, aﬀecting the completeness and accuracy of the data available for analysis.

To conclude the discussion on FES-based upper limb stroke rehabilitation systems, it is important to address some key questions related to the current level of implementation, design feasibility, practical credibility, clinical considerations, and future interpretation. These questions will help clarify the current state of these systems and inform their future development.

###  .  Are FES based therapies more e ective than non-FES conventional therapies for stroke rehabilitation?

Several studies have compared FES and non-FES upper limb stroke rehabilitation (17, 34, 35, 51, 56). In (17), a study of 30 stroke survivors (experimental FES and non-FES control group) demonstrated improvement in clinical scores, suggesting that FES reduces wrist ﬂexor spasticity as compared to non-FES. Kim et al. (34) and Miao et al. (35) in an RCT investigated the inﬂuence of the BCI-FES system on the motor recovery of upper extremities in stroke survivors. The measured outcomes validated enhanced recovery via BCIbased system as compared to physical training. Similarly, Shindo et al. (51) and Jonsdottir et al. (56) in an RCT tested the performance of a EMG-controlled FES against non-FES conventional therapies. Following the completion of the rehabilitation sessions, the pre- and post-performance of participants were evaluated using various clinical scores such as FMA and ARAT. EMG-FES induced a greater level of improvement in comparison to the non-FES control group. In addition to EMG-controlled FES, EMG-triggered FES also shows promising results when compared with non-FES rehabilitation therapies (85–88).

###  .  What are the main clinical considerations for the use of electrical stimulation?

###  .  Based on the reported studies, which FES neurorehabilitation system can be considered the best among all?

There is no so-called “BEST” system, as every FES system has pros and cons, and its selection depends on the required stroke application. For instance, open-loop FES and BCI-FES can be used by stroke survivors with no muscle activity, whereas EMG-FES can only be used by the ones having residual muscle activity. However, regardless of their encouraging results, the reported FES-based rehabilitation studies contain certain limitations and shortcomings.

 . .  No RCT is conducted

Numerous studies did not conduct randomized controlled trials; instead, they just conducted feasibility studies within the stroke population (18–24, 37–45, 58). Such studies included no control group and only performed the rehabilitation protocols on the experimental group. A control group provides a baseline against which the treatment group can be compared. Without a control group, assessing whether any observed changes are greater or diﬀerent from what would naturally occur without the intervention is challenging. Also, it may be challenging to generalize the study’s ﬁndings to a broader population or to other settings because there is no comparison to determine whether the eﬀects are consistent across diﬀerent contexts.

 . .  Small sample size

Reported RCTs (17, 32–36, 51, 55, 56) and feasibility studies (19, 21, 23, 24, 38, 42, 44, 58) claimed statistical signiﬁcance results; however, their sample size is not large enough (lies between 1 and 51 stroke patients in one group). According to Kaptein (94), a conventional RCT requires a group size of at least 64 individuals in each group to obtain statistically signiﬁcant results. Hence, a small sample size questions the credibility and reliability of studies. It indicates that further investigation or a larger sample size may be needed to establish a more deﬁnitive relationship.

To ensure the safe use of FES in clinical applications, it is important to consider some key precautions and factors that may aﬀect its delivery beyond the targeted muscle, leading to unexpected consequences. In (89), Marquez-Chin et al. give a complete list of clinical considerations that include:

- • Pregnancy: The eﬀect of FES on pregnancy or the fetus is not known and therefore, should be avoided to use (90).
- • Lesions: The application of FES should be avoided on open skin lesions, as it can increase irritation and further damage the existing lesion (90).
- • Cardiac pacemakers: Electrical stimulation may interfere with the electrical signals from pacemakers, potentially aﬀecting their functioning (91).
- • Congestive heart failure conditions: The cardiovascular demand resulting from the muscle contractions produced by the FES may require special attention before and during the delivery of stimulation (92, 93).

 . .  Lack of follow-up data

Also, there was no mention of the follow-up data to determine whether the improvement was retained or not (17–24, 32–45, 58). The absence of follow-up data in rehabilitation can impede the assessment of long-term outcomes, the identiﬁcation of relapses, and the ability to make informed decisions about treatment eﬀectiveness and planning. It is crucial for both clinical practice and research to include follow-up assessments to ensure that the beneﬁts of rehabilitation are sustained and optimized over time.

 . .  Lack of neuroplasticity validation

When an individual experiences functional improvement, such as regaining motor skills after a stroke rehabilitation, the brain can reorganize its neural circuits and establish new connections or strengthen existing ones to support improved function (95, 96). These neuronal changes can be determined by diﬀerent techniques, which mainly include electroencephalography (EEG)/evoked

potentials (ERPs), structural and functional magnetic resonance imaging (MRI), and transcranial magnetic stimulation (TMS) (97). Studies (17, 19, 21, 23, 24, 32–36, 38, 42, 44, 51, 55, 56) have shown that the diﬀerent FES-based rehabilitation causes functional improvement among stroke patients, but none of them has validated their ﬁndings by presenting the neuroplasticity outcomes. Thus, it remains uncertain to what extent neuroplasticity has occurred due to open/closed-loop FES rehabilitation.

Hence, it is hard to conclude which speciﬁc FES system is best. However, many research studies showed that closed-loop FES is more eﬀective than open-loop FES for motor recovery (32–35, 38, 55). Among closed-loop FES, which system is more eﬃcient (either BCI-FES or EMG-FES) remains unknown, as currently, no RCT has been conducted to directly compare their eﬃcacy in neurorehabilitation. Furthermore, from the clinical implementation point of view, an open-loop FES has been widely used clinically for many years (for stroke rehabilitation), whereas closed-loop FES is mainly applied in the laboratory as a research protocol (especially BCI-FES). As per our knowledge, “RecoveriX from g.tec” (39) is the only commercially available BCI-FES system for stroke rehabilitation, which is also in its initial phases to be adopted by clinicians/therapists.

 .  Can the e ectiveness of FES systems be further enhanced by combining them with other systems/paradigm?

To enhance the performance of FES rehabilitation, it can either be combined with other rehabilitation systems (like robotic systems and exoskeletons) or any additional paradigm (like virtual reality), hence, developing a “Hybrid FES Rehabilitation System”.

 . .  Hybrid with other rehabilitation systems (robotics system and exoskeleton)

In (98), the integration of electrical stimulation with robotic arm training resulted in signiﬁcant improvements in the range of motion for shoulder and elbow movements in subacute stroke survivors, compared to conventional robotic training. Meadmore et al. (99) developed a new rehabilitative system, featuring FES, robotic support, and voluntary eﬀort. The results demonstrated improvements in arm impairment among ﬁve stroke survivors. Another study (100) tested an EMG-driven FES-robotic system on 11 chronic stroke survivors to rehabilitate ﬁnger, wrist, and elbow movement. Signiﬁcant improvement in physical functions and arm impairment has been obtained. Qian et al. (101) used the same FES-robotic system on 24 sub-acute stroke survivors, which showed higher motor outcomes at the distal joints than the control group (conventional therapy). Although there are potential advantages in using hybrid FES robotic systems for upper limb rehabilitation, a review study has revealed that only a limited number of hybrid systems have undergone testing with stroke survivors (102). This could be due to challenges associated with integrating both rehabilitation technologies or the absence of integrated platforms that could be user-friendly and easy to set up.

Ambrosini et al. (103) developed a novel hybrid neurorehabilitation system that integrated a passive exoskeleton

(named RETRAINER) with an EMG-triggered FES unit. In (103), they tested the feasibility and functionality of the hybrid system in a clinical environment. Later, they performed a pilot study (104) and RCT (105) to test the performance of the developed system for upper limb recovery. The pilot study was implemented on seven post-acute stroke survivors. Preliminary results conﬁrmed that the hybrid FES exoskeleton system can be used for stroke rehabilitation, positively impacting arm functional recovery (104). In (105), an RCT involving 72 stroke survivors validated the performance of a hybrid system compared to advanced conventional therapy (ACT) for task-oriented arm training. The ﬁndings showed that the hybrid FES exoskeleton system achieved a signiﬁcantly better improvement in upper limb functionality.

 . .  Hybrid with additional paradigm (virtual reality)

During the FES-based rehabilitation therapy, the participants started losing interest, and it became diﬃcult for them to maintain the training motivation. This decline in the level of engagement could be attributed to the extended duration of the sessions, the repetitive exercises involved, and the clinical environment in which the rehabilitation took place (106). Therefore, physical therapists increasingly turn to virtual reality (VR) paradigms and incorporate VR into their neurorehabilitation protocols (107). By providing a virtual environment with thrilling, stimulating, and entertaining tasks, VR can keep participants more focused and motivated during rehab exercises, potentially engaging additional neural circuits to restore motor functions more eﬀectively. Hence, the RecoveriX system combines VR with FES and commercially introduced hybrid VR-based BCI-FES stroke rehabilitation systems (39). Diﬀerent studies (40–44) suggested that the RecoveriX system caused the improvement in upper extremity movements via stroke rehabilitation.

However, as VR is a newly adopted method in neurorehabilitation, initial testing has mostly been performed on small populations. Furthermore, low-quality VR may cause simulator sickness in stroke survivors, thus necessitating highquality VR that replicates actual environments as realistically as possible. Thus, more research is needed to investigate the practical implementation and feasibility of hybrid VR-based FES systems for neurorehabilitation.

 .  As ﬂexible electronics (FE) is nowadays being integrated within the healthcare system, what is the emerging potential of FE combined with FES and other technologies for stroke rehabilitation?

Regarding the future of FES-based neurorehabilitation systems, it is highly likely that “Flexible Electronics” (FE) will be integrated into this ﬁeld. FE is an innovative technology that oﬀers a ﬂexible hardware platform to perform signal ampliﬁcation, precise sensing, and delivery of FES (64). Modern FES devices typically employ a pair of large gel electrodes, which generate multiple current paths, hence stimulating various muscles. This results in an inability to

activate speciﬁc muscles selectively and can lead to muscle fatigue (108). To address this issue and enable selective stimulation, a ﬂexible multiple-electrode array has been created, which can be conveniently applied to curved surfaces and cover several targeted areas at a single location (109–113). This array allows for individual electrode activation, providing selective stimulation to targeted muscles. Moreover, research has demonstrated that distributing the stimulation spatially across multiple electrodes can also delay the occurrence of muscle fatigue (114–116).

De Marchis et al. (109) used an FE array comprising 27 electrodes to administer FES. Eight healthy participants were tested using the system to execute various wrist and ﬁnger movements of the left arm. The ﬁndings indicate that the electrode array can deliver precise stimulation to speciﬁc muscles, making it a viable option for stroke rehabilitation. In (110), a ﬂexible 24-electrode array named “e-sleeve” was built for an FES rehabilitation device. The performance of the e-sleeve was evaluated on eight stroke patients with upper limb disability for executing “hand opening and pointing” actions. Similarly, Yang et al. (111) and Loitz et al. (112) developed screen-printed fabric electrode arrays (FEAs) for a wearable FES device. The ﬁndings indicate that the FEAs can successfully facilitate desired movements, such as “open hand,” “pinch,” and “pointing” gestures. Another ﬂexible FES electrode array was designed by Maleševic et al. (113), called “Intelligent FES (INTFES)”. It was tested on three stroke survivors to produce grasping movements. The outcomes demonstrated that INTFES activates the appropriate electrode conﬁguration (thus, muscles) and successfully achieves grasping movements while maintaining wrist stabilization.

EEG and EMG acquisition systems are also a key part of FES rehabilitation systems, underscoring the need for ﬂexible EEG/EMG electrodes to support advanced solutions for acquiring brain and muscle signals. FE electrodes are recommended over conventional electrodes because they can be placed on curved body surfaces and also incorporated into wearable devices of various shapes. FE electrodes enable the design of portable systems and optimize the overall compactness (117). This makes them feasible for everyday use and enables patients to carry out long-lasting rehabilitation therapies with greater ease and comfort (118). Several studies have developed and tested ﬂexible EEG (119, 120) and EMG (121–123) electrodes for signal acquisition. Moreover, in 2019, research was published in “Nature Machine Intelligence,” in which Mahmood et al. designed a fully portable, ﬂexible, and wireless BCI system for EEG data acquisition (124).

Thus, it is clear that FE technology is rapidly growing in healthcare; however, its neurorehabilitation application is still in its infancy as very little testing is performed on stroke survivors (mainly done on healthy subjects). In the future, there is a high chance that ﬂexible technology will become mature enough to be largely used for designing ﬂexible and portable stroke rehabilitation systems.

rehabilitation: Manual FES, BCI-FES, and EMG-FES. A metaanalysis has been performed that validated the eﬀectiveness of FES-based systems for upper limb stroke rehabilitation. Among the feasibility tests and RCTs for stroke application, it provides a comprehensive understanding of the design, eﬀectiveness, and limitations. The article also discusses some of the hybrid approaches, including robotics systems and virtual reality, which can contribute to enhancing the eﬃcacy of FES-based rehabilitation systems. Thus, this review article will help researchers to: (1) identify the new research gaps in stroke rehabilitation; (2) assess the possibility of integrating ﬂexible electronics and hybrid approaches while developing new FES systems in the future; (3) consider the shortcomings of previous clinical studies while designing the new rehabilitation protocols; (4) determine the usefulness of diﬀerent types of FES rehabilitation approaches and perform diﬀerent RCTs to compare their performance.

## Data availability statement

The original contributions presented in the study are included in the article/Supplementary material, further inquiries can be directed to the corresponding author.

## Author contributions

MK: Conceptualization, Funding acquisition, Methodology, Writing – original draft, Writing – review & editing, Visualization. HF: Writing – original draft. HG: Writing – original draft. IB: Writing – review & editing. SP: Supervision, Writing – review & editing. BR: Supervision, Writing – review & editing. ML: Supervision, Writing – review & editing. AP: Supervision, Writing – review & editing. KM: Supervision, Writing – review & editing.

## Funding

The author(s) declare ﬁnancial support was received for the research, authorship, and/or publication of this article. This project has been supported by Novo Nordisk Foundation, Denmark (Grant No. 0066957).

## Conﬂict of interest

The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

## Conclusion

This systematic review provides a comprehensive overview of three types of FES systems used for post-stroke upper limb

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of

their aﬃliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fneur.2023. 1272992/full#supplementary-material

## References

- 1. Grefkes C, Fink GR. Recovery from stroke: current concepts and future

perspectives. Neurological Res Pract. 2:1. doi: 10.1186/s42466-020-00060-6

- 2. Cramer SC, Wolf SL, Adams HP, Chen D, Dromerick AW, Dunning K, et al.

Stroke recovery and rehabilitation research: issues, opportunities, and the NIH StrokeNet. Stroke. (2017) 48:813–9. doi: 10.1161/STROKEAHA.116.015501

- 3. Robinson RG, Jorge RE. Post-stroke depression: a review. Am J Psychiatry. (2016)

173:221–31. doi: 10.1176/appi.ajp.2015.15030363

- 4. Khedr EM, Abdelrahman AA, Desoky T, Zaki, Gamea AF. Post-stroke

depression: frequency, risk factors, and impact on quality of life among 103 stroke patients—hospital-based study. Egypt J Neurol Psychiat Neurosurg. (2020) 56:1. doi: 10.1186/s41983-020-00199-8

- 5. Johnson CO, Nguyen M, Roth GA, Nichols E, Alam T, Abate D, et al.

Global, regional, and national burden of stroke, 1990–2016: a systematic analysis for the Global Burden of Disease Study 2016. Lancet Neurol. (2019) 18:439– 58. doi: 10.1016/S1474-4422(19)30034-1

6. Page SJ, Levine P, Sisto S, Johnston MV. A randomized eﬃcacy and feasibility study of imagery in acute stroke. Clin Rehabil. (2001) 15:233–

40. doi: 10.1191/026921501672063235

- 7. Hendricks HT, van Limbeek J, Geurts AC, Zwarts MJ. Motor recovery after

stroke: a systematic review of the literature. Arch Phys Med Rehabil. (2002) 83:1629–

37. doi: 10.1053/apmr.2002.35473

- 8. Claﬂin ES, Krishnan C, Khot SP. Emerging treatments for motor rehabilitation

after stroke. Neurohospitalist. (2014) 5:77–88. doi: 10.1177/1941874414561023

- 9. Di Carlo A. Human and economic burden of stroke. Age Ageing. (2009) 38:4–

5. doi: 10.1093/ageing/afn282

- 10. Caramenti M, Bartenbach V, Gasperotti L, Oliveira da. Fonseca L, Berger TW,

Pons JL. Challenges in nerurorehabilitation and neural engineering In: Pons JL, Raya R, González J, editors. Emerging Therapies in Neurorehabilitation II Switzerland. Cham: Springer International Publishing. (2016).

11. Khan MA, Das R, Iversen HK, Puthusserypady S. Review on motor imagery based BCI systems for upper limb post-stroke neurorehabilitation: from designing to application. Comp Biol Med. (2020)

- 123:103843. doi: 10.1016/j.compbiomed.2020.103843

- 12. Eraifej J, Clark W, France B, Desando S, Moore D. Eﬀectiveness of upper limb

functional electrical stimulation after stroke for the improvement of activities of daily living and motor function: a systematic review and meta-analysis. Systematic Rev.

- (2017) 6:1. doi: 10.1186/s13643-017-0435-5

- 13. Jaqueline da Cunha M, Rech KD, Salazar AP, Pagnussat AS. Functional electrical

stimulation of the peroneal nerve improves post-stroke gait speed when combined with physiotherapy. A systematic review and meta-analysis. Ann Phys Rehabilitat Med.

- (2020) 64:1. doi: 10.1016/j.rehab.2020.03.012

- 14. Khan A, Abdullah M, Serpelloni S, Sardini E. Design of FES based muscle

stimulator device using EMG and insole force resistive sensors for foot drop patients. Adv Mater Lett. (2018) 9:776–80. doi: 10.5185/amlett.2018.2170

- 15. Moe JH, Post HW. Functional electrical stimulation for ambulation in

hemiplegia. J Lancet. (1962) 82:285–8.

- 16. Kralj A, Bajd T, Turk R. Enhancement of Gait Restoration in Spinal Injured

Patients by Functional Electrical Stimulation. Clini Orthop Related Res. (1988) 233:34–

43. doi: 10.1097/00003086-198808000-00006

17. Nakipoglu Yuzer GF, Köse Dönmez B, Özgirgin N. A randomized controlled study: eﬀectiveness of functional electrical stimulation on wrist and ﬁnger ﬂexor spasticity in hemiplegia. J Stroke Cerebrovas Dis. (2017) 26:1467–71. doi: 10.1016/j.jstrokecerebrovasdis.2017.03.011

- 18. Makowski NS, Knutson JS, Chae J, Crago PE. Functional electrical stimulation

to augment poststroke reach and hand opening in the presence of voluntary eﬀort. Neurorehabil Neural Repair. (2013) 28:241–9. doi: 10.1177/1545968313505913

- 19. Meadmore KL, Exell TA, Hallewell E, Hughes A-M, Freeman CT, Kutlu M, et al.

The application of precisely controlled functional electrical stimulation to the shoulder, elbow and wrist for upper limb stroke rehabilitation: a feasibility study. J NeuroEng Rehabilitat. (2014) 11:105. doi: 10.1186/1743-0003-11-105

- 20. Sun M, Smith C, Howard D, Kenney L, Luckie H, Waring K, et al. FES-UPP:

A Flexible Functional Electrical Stimulation System to Support Upper Limb Functional Activity Practice. (2018). p. 12.

- 21. Niu CM, Bao Y, Zhuang C, Li S, Wang T, Cui L, et al. Synergy-based FES for post-

stroke rehabilitation of upper-limb motor functions. IEEE Trans Neural Syst Rehabilitat Eng. (2019) 27:256–64. doi: 10.1109/TNSRE.2019.2891004

- 22. Chou CH, Wang T, Sun X, Niu CM, Hao M, Xie Q, et al. Automated

functional electrical stimulation training system for upper-limb function recovery in poststroke patients. Med Eng Phys. (2020) 84:174–83. doi: 10.1016/j.medengphy.2020. 09.001

- 23. Martín-Odriozola A, -de-Pablo R, Zabaleta-Rekondo H. Hand dexterity

rehabilitation using selective functional electrical stimulation in a person with stroke. BMJ Case Rep. (2021) 14:8. doi: 10.1136/bcr-2021-242807

- 24. Niu CM, Chou CH, Bao Y, Wang T, Gu L, Zhang X, et al. A pilot study of

synergy-based FES for upper-extremity poststroke rehabilitation. Neurosci Lett. (2022) 780:136621. doi: 10.1016/j.neulet.2022.136621

- 25. Machado TC, Carregosa AA, Santos MS, Ribeiro NM, Melo A. Eﬃcacy of motor

imagery additional to motor-based therapy in the recovery of motor function of the upper limb in post-stroke individuals: a systematic review. Top Stroke Rehabilitat. (2019) 16:1–6. doi: 10.1080/10749357.2019.1627716

- 26. Johnson SH, Sprehn G, Saykin AJ. Intact motor imagery in chronic upper limb

hemiplegics: evidence for activity-independent action representations. J Cogn Neurosci.

(2002) 14:841–52. doi: 10.1162/089892902760191072

- 27. Sharma N, Pomeroy VM, Baron J-C. Motor imagery. Stroke. (2006) 37:1941–

52. doi: 10.1161/01.STR.0000226902.43357.fc

- 28. Das R, Lopez PS, Khan MA, Iversen S, Puthusserypady HK. FBCSP and

Adaptive Boosting for Multiclass Motor Imagery BCI Data Classiﬁcation: A Machine Learning Approach.

- 29. Braun S, Kleynen M, van Heel T, Kruithof N, Wade, Beurskens DA. The eﬀects of

mental practice in neurological rehabilitation; a systematic review and meta-analysis. Front Human Neurosci. (2013) 7:390. doi: 10.3389/fnhum.2013.00390

- 30. Uyanik C, Khan MA, Brunner IC, Hansen JP, Puthusserypady S. Machine

Learning for Motor Imagery Wrist Dorsiﬂexion Prediction in Brain-Computer Interface Assisted Stroke Rehabilitation. In: 44th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). Glasgow, UK: IEEE. (2022). p. 11–15.

- 31. Voinas AE, Das R, Khan MA, Brunner I, Puthusserypady S. Motor imagery EEG

signal classiﬁcation for stroke survivors rehabilitation. In: 10th International Winter Conference on Brain-Computer Interface (BCI). Gangwon-do, Korea: IEEE. (2022). p. 21–23. doi: 10.1109/BCI53720.2022.9734837

- 32. Cincotti F, Pichiorri F, Arico P, Aloise F, Leotta F, de Vico Fallani F, et al. EEG-

based Brain-Computer Interface to support post-stroke motor rehabilitation of the upper limb. In: 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society. San Diego, USA: IEEE. (2012).

- 33. Li M, Liu Y, Wu Y, Liu S, Jia J, Zhang L. Neurophysiological substrates of stroke

patients with motor imagery-based brain-computer interface training. Int J Neurosci.

(2014) 124:403–15. doi: 10.3109/00207454.2013.850082

34. Kim T, Kim S, Lee B. Eﬀects of action observational training plus brain-computer interface-based functional electrical stimulation on paretic arm motor recovery in patient with stroke: a randomized controlled trial. Occup Ther Int. (2016) 23:39– 47. doi: 10.1002/oti.1403

- 35. Miao Y, Chen S, Zhang X, Jin J, Xu R, Daly I, et al. BCI-based rehabilitation on

the stroke in sequela stage. Neural Plast. (2020). doi: 10.1155/2020/8882764

- 36. Chen L, Gu B, Wang Z, Zhang L, Xu M, Liu S, et al. EEG-controlled functional

electrical stimulation rehabilitation for chronic stroke: system design and clinical application. Front Med. (2021) 15:740–9. doi: 10.1007/s11684-020-0794-5

- 37. Daly JJ, Cheng R, Rogers J, Litinas K, Hrovat K, Dohring M. Feasibility of

a new application of noninvasive brain computer interface (BCI): a case study of training for recovery of volitional motor control after stroke. J Neurol Phys Ther. (2009) 33:203–11. doi: 10.1097/NPT.0b013e3181c1fc0b

- 38. Mukaino M, Ono T, Shindo K, Fujiwara T, Ota T, Kimura A, et al. Eﬃcacy

of brain-computer interface-driven neuromuscular electrical stimulation for chronic paresis after stroke. J Rehabilitat Med. (2014) 46:378–82. doi: 10.2340/16501977-1785

- 39. Irimia D, Sabathiel N, Ortner R, Poboroniuc M, Coon W, Allison C, Guger

BZ. recoveriX: a new BCI-based technology for persons with stroke. In: 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). Orlando, USA: IEEE. (2016).

- 40. Sabathiel N, Irimia DC, Allison BZ, Guger C, Edlinger G. (2016). Paired

Associative Stimulation with Brain-Computer Interfaces: A New Paradigm for Stroke Rehabilitation. p. 261–272.

- 41. Irimia DC, Poboroniuc M, Ortner R, Allison C, Guger BZ. Preliminary results

of testing a BCI-controlled FES system for post-stroke rehabilitation. In: 7th Graz Brain-Computer Interface Conference. (2017) p. 18–22.

- 42. Cho W, Heilinger A, Xu R, Zehetner M, Schobesberger S, Murovec N,

et al. Hemiparetic stroke rehabilitation using avatar and electrical stimulation based on non-invasive brain computer interface. Int J Phys Med Rehabilitat. (2017) 05:04. doi: 10.4172/2329-9096.1000411

- 43. Qiu Z, Chen S, Daly I, Jia J, Wang J, Jin X. BCI-based strategies on stroke rehabilitation with avatar and FES feedback. ArXiv. (2018). doi: 10.48550/arXiv.1805.04986
- 44. Sebastián-Romagosa M, Cho W, Ortner R, Murovec N, Von Oertzen T, Kamada K, et al. Brain computer interface treatment for motor rehabilitation of upper extremity of stroke patients—a feasibility study. Front Neurosci. (2020)

- 14. doi: 10.3389/fnins.2020.591435

- 45. Choi I, Kwon GH, Lee CS, Nam S. Functional electrical stimulation controlled by motor imagery brain-computer interface for rehabilitation. Brain Sci. (2020) 10:512. doi: 10.3390/brainsci10080512
- 46. Abdullah S, Khan AM, Serpelloni E, Sardini M. Hybrid EEG-EMG based brain computer interface (BCI) system for real-time robotic arm control. Adv Mat Lett.

- (2018) 10:35–40. doi: 10.5185/amlett.2019.2171

- 47. Piyus CK, Cherian S, Nageswaran VA. EMG based FES for post-stroke rehabilitation. In: IOP Conference Series: Materials Science and Engineering. (2017). p. 263.
- 48. Monte-Silva K, Piscitelli D, Norouzi-Gheidari N, Batalla MAP, Archambault P, Levin MF. Electromyogram-related neuromuscular electrical stimulation for restoring wrist and hand movement in poststroke hemiplegia: a systematic review and meta-analysis. Neurorehabil Neural Repair. (2019) 33:96–111. doi: 10.1177/1545968319826053
- 49. Hara Y. Rehabilitation with functional electrical stimulation in stroke patients.

Int J Phys Med Rehabilitat. (2013) 01:06. doi: 10.4172/2329-9096.1000147

- 50. Karu ZZ, Durfee WK, Barzilai AM. Reducing muscle fatigue in FES applications

by stimulating with N-let pulse trains. IEEE Trans Biomed Eng. (1995) 42:809–

- 17. doi: 10.1109/10.398642

- 51. Shindo K, Fujiwara T, Hara J, Oba H, Hotta F, Tsuji T, et al. Eﬀectiveness of hybrid

assistive neuromuscular dynamic stimulation therapy in patients with subacute stroke. Neurorehabil Neural Repair. (2011) 25:830–7. doi: 10.1177/1545968311408917

- 52. Muraoka Y. Development of an EMG recording device from stimulation

electrodes for functional electrical stimulation. Front Med Biol Eng. (2001) 11:323–

33. doi: 10.1163/156855701321138969

- 53. Thorsen R. An artefact suppressing fast-recovery myoelectric ampliﬁer. IEEE

Trans Biomed Eng. (1999) 46:764–6. doi: 10.1109/10.764955

- 54. Thorsen R, Ferrarin M. Battery powered neuromuscular stimulator circuit for use during simultaneous recording of myoelectric signals. Med Eng Phys. (2009) 31:1032–7. doi: 10.1016/j.medengphy.2009.06.006
- 55. Thorsen R, Cortesi M, Jonsdottir J, Carpinella I, Morelli D, Casiraghi A, et al. Myoelectrically driven functional electrical stimulation may increase motor recovery of upper limb in poststroke subjects: a randomized controlled pilot study. J Rehabil Res Dev. (2013) 50:785–94. doi: 10.1682/JRRD.2012.07.0123
- 56. Jonsdottir J, Thorsen R, Aprile I, Galeri S, Spannocchi G, Beghi E, et al. Arm rehabilitation in post stroke subjects: A randomized controlled trial on the eﬃcacy of myoelectrically driven FES applied in a task-oriented approach. PLoS ONE. (2017) 12:e0188642. doi: 10.1371/journal.pone.0188642
- 57. Crepaldi M, Thorsen R, Jonsdottir J, Scarpetta S, De Michieli L, Salvo MD,

et al. FITFES: A wearable myoelectrically controlled functional electrical stimulator designed using a user-centered approach. IEEE Trans Neural Syst Rehabilitat Eng. (2021) 29:2142–52. doi: 10.1109/TNSRE.2021.3120293

- 58. Hara Y, Obayashi S, Tsujiuchi K, Muraoka Y. The eﬀects of electromyography-

controlled functional electrical stimulation on upper extremity function and cortical perfusion in stroke patients. Clini Neurophysiol. (2013)

- 124:2008–15. doi: 10.1016/j.clinph.2013.03.030

59. Zhang D, Guan TT, Widjaja F, Ang WT. Functional electrical stimulation in rehabilitation engineering: A survey. In: 1st International Convention on Rehabilitation Engineering and Assistive Technology: in Conjunction with 1st Tan Tock Seng Hospital Neurorehabilitation Meeting. (2007).

- 60. Sousa AS, Moreira J, Silva C, Mesquita I, Macedo R, Silva A, Santos R. Usability

of functional electrical stimulation in upper limb rehabilitation in post-stroke patients: a narrative review. Sensors. (2022) 22:4. doi: 10.3390/s22041409

- 61. Takeda K, Tanino G, Miyasaka H. Review of devices used in neuromuscular

electrical stimulation for stroke rehabilitation. Med Dev (Auckland, NZ). (2017)

- 10:207–13. doi: 10.2147/MDER.S123464

- 62. Angerhöfer C, Colucci A, Vermehren M, Hömberg SR, Soekadar V. Poststroke Rehabilitation of Severe Upper Limb Paresis in Germany – Toward Long-Term Treatment With Brain-Computer Interfaces. Front Neurol. (2021) 12:772199. doi: 10.3389/fneur.2021.772199
- 63. Cervera MA, Soekadar SR, Ushiba J, Millán J, del R, Liu M, et al. Brain-computer interfaces for post-stroke motor rehabilitation: a meta-analysis. Ann Clini Translat Neurol. (2018) 5:651–63. doi: 10.1002/acn3.544
- 64. Khan MA, Saibene M, Das R, Brunner S, Puthusserypady I. Emergence of

ﬂexible technology in developing advanced systems for post-stroke rehabilitation: a comprehensive review. J Neural Eng. (2021) 18:6. doi: 10.1088/1741-2552/ac36aa

- 65. Chen Y, Abel KT, Janecek JT, Chen Y, Zheng K, Cramer SC. Home-based

technologies for stroke rehabilitation: a systematic review. Int J Med Inform. (2019) 123:11–22. doi: 10.1016/j.ijmedinf.2018.12.001

- 66. Calaﬁore D, Negrini F, Tottoli N, Ferraro F, Ozyemisci-Taskiran O. Eﬃcacy of

robotic exoskeleton for gait rehabilitation in patients with subacute stroke: a systematic review. Eur J Phys Rehabil Med. (2022) 58:1. doi: 10.23736/S1973-9087.21.06846-5

- 67. Wang L, Chen JL, Wong AM, Liang KC, Tseng KC. Game-based

virtual reality system for upper limb rehabilitation after stroke in a clinical environment: systematic review and meta-analysis. Games Health J. (2022)

- 11:277–97. doi: 10.1089/g4h.2022.0086

68. Hatem SM, Saussez G, Della Faille M, Prist V, Zhang X, Dispa D, et al. Rehabilitation of motor function after stroke: a multiple systematic review focused on techniques to stimulate upper extremity recovery. Front Hum Neurosci. (2016) 10:442. doi: 10.3389/fnhum.2016.00442

- 69. Ma LL, Wang YY, Yang ZH, Huang D, Weng H, Zeng XT. Methodological quality

(risk of bias) assessment tools for primary and secondary medical studies: what are they and which is better? Military Med Res. (2020) 7:1–11. doi: 10.1186/s40779-020-00 238-8

- 70. National heart lung and blood institute. Quality Assessment Tool for Case Series

Studies. Available online at: https://www.nhlbi.nih.gov/health-topics/study-qualityassessment-tools (accessed November 8, 2023).

71. Joanna Briggs Institute (JBI). Joanna Briggs Institute (JBI) Checklist for Case Reports. Available online at: https://jbi.global/critical-appraisal-tools (accessed November 8, 2023).

- 72. Morris RGM, Hebb DO. The organization of behavior, Wiley: New York; 1949.

Brain Res Bullet. (1999) 50:437. doi: 10.1016/S0361-9230(99)00182-3

- 73. Shatz CJ. The developing brain. Sci Am. (1992) 267:60–

7. doi: 10.1038/scientiﬁcamerican0992-60

- 74. Stefan K. Induction of plasticity in the human motor cortex by paired associative

stimulation. Brain. (2000) 123:572–84. doi: 10.1093/brain/123.3.572

- 75. Taylor JL, Martin PG. Voluntary motor output is altered by spike-timing-

dependent changes in the human corticospinal pathway. J Neurosci. (2009) 29:11708–

16. doi: 10.1523/JNEUROSCI.2217-09.2009

- 76. McPherson JG, Miller RR, Perlmutter SI. Targeted, activity-dependent spinal

stimulation produces long-lasting motor recovery in chronic cervical spinal cord injury. Proc Nat Acad Sci. (2015) 112:12193–8. doi: 10.1073/pnas.1505383112

- 77. Bunday, Karen L. and Perez, Monica A. Motor recovery after spinal cord injury

enhanced by strengthening corticospinal synaptic transmission. Curr Biol. (2012) 22:2355–61. doi: 10.1016/j.cub.2012.10.046

- 78. Mrachacz-Kersting N, Kristensen SR, Jamil D, Farina M. Precise

temporal association between cortical potentials evoked by motor imagination and aﬀerence induces cortical plasticity. J Physiol. (2012) 590:1669–82. doi: 10.1113/jphysiol.2011.222851

- 79. Bolton DAE, Cauraugh JH, Hausenblas HA. Electromyogram-triggered

neuromuscular stimulation and stroke motor recovery of arm/hand functions: a meta-analysis. J Neurol Sci. (2004) 223:121–7. doi: 10.1016/j.jns.2004.05.005

- 80. De Kroon J, IJzerman M, Chae J, Lankhorst G, Zilvold G. Relation between

stimulation characteristics and clinical outcome in studies using electrical stimulation to improve motor control of the upper extremity in stroke. J Rehabilitat Med. (2005) 37:65–74. doi: 10.1080/16501970410024190

- 81. De Kroon JR, IJzerman MJ. Electrical stimulation of the upper extremity

in stroke: cyclic versus EMG-triggered stimulation. Clin Rehabil. (2008) 22:690–

7. doi: 10.1177/0269215508088984

- 82. Meilink A, Hemmen B, Seelen H, Kwakkel G. Impact of EMG-triggered

neuromuscular stimulation of the wrist and ﬁnger extensors of the paretic hand after stroke: a systematic review of the literature. Clin Rehabil. (2008) 22:291– 305. doi: 10.1177/0269215507083368

83. Wilson RD, Page SJ, Delahanty M, Knutson JS, Gunzler DD, Sheﬄer LR, et al. Upper-limb recovery after stroke. Neurorehabil Neural Repair. (2016) 30:978–

87. doi: 10.1177/1545968316650278

84. Osuagwu BAC, Whicher R, Shirley E. Active proportional electromyogram controlled functional electrical stimulation system. Scient Rep. (2020) 10:1. doi: 10.1038/s41598-020-77664-0

- 85. Cauraugh J, Light K, Kim S, Thigpen M, Behrman A. Chronic motor dysfunction

after stroke: recovering wrist and ﬁnger extension by electromyography-triggered neuromuscular stimulation. Stroke. (2000) 31:1360–4. doi: 10.1161/01.STR.31.6.1360

- 86. Cauraugh JH, Kim S. Two coupled motor recovery protocols are better than

one: electromyogram-triggered neuromuscular stimulation and bilateral movements. Stroke. (2002) 33:1589–94. doi: 10.1161/01.STR.0000016926.77114.A6

- 87. Francisco G, Chae J, Chawla H, Kirshblum S, Zorowitz R, Lewis G, et al.

Electromyogram-triggered neuromuscular stimulation for improving the arm function of acute stroke survivors: a randomized pilot study. Arch Phys Med Rehabil. (1998) 79:570–5. doi: 10.1016/S0003-9993(98)90074-0

- 88. Hara Y, Ogawa S, Tsujiuchi K, Muraoka Y. A home-based rehabilitation

program for the hemiplegic upper extremity by power-assisted functional electrical stimulation. Disabil Rehabil. (2008) 30:296–304. doi: 10.1080/096382807012 65539

- 89. Marquez-Chin MR, Popovic C. Functional electrical stimulation therapy for

restoration of motor function after spinal cord injury and stroke: a review. BioMedical Eng OnLine. (2020) 19:1. doi: 10.1186/s12938-020-00773-4

- 90. Alon G. Functional electrical stimulation (FES): transforming clinical trials to

neuro-rehabilitation clinical practice-a forward perspective. J Nov Physiother. (2013) 3:2. doi: 10.4172/2165-7025.1000176

- 91. Crevenna R, Mayr W, Keilani M, Pleiner J, Nuhr M, Quittan M, et al. Safety of a

combined strength and endurance training using neuromuscular electrical stimulation of thighs muscles in patients with heart failure and bipolar sensing cardiac pacemakers. Wiener Klinische Wochenschrift. (2003) 115:710–4. doi: 10.1007/BF03040887

- 92. Nuhr MJ, Pette D, Berger R, Quittan M, Crevenna R, Huelsman M,

et al. Beneﬁcial eﬀects of chronic low-frequency stimulation of thigh muscles in patients with advanced chronic heart failure. Eur Heart J. (2004) 25:136– 43. doi: 10.1016/j.ehj.2003.09.027

- 93. Deley G, Kervio G, Verges B, Hannequin A, Petitdant MF, Grassi B,

et al. Neuromuscular adaptations to low-frequency stimulation training in a patient with chronic heart failure. Am J Phys Med Rehabilitat. (2008) 87:502– 9. doi: 10.1097/PHM.0b013e318174e29c

- 94. Kaptein M. A practical approach to sample size calculation for ﬁxed populations.

Contemp Clini Trials Commun. (2019) 14: 100339. doi: 10.1016/j.conctc.2019.100339

- 95. Birbaumer N, Ruiz S, Sitaram R. Learned regulation of brain metabolism. Trends

Cogn Sci. (2013) 17:295–302. doi: 10.1016/j.tics.2013.04.009

- 96. Ruiz Ruiz S, Buyukturkoglu K, Rana M, Birbaumer N, Sitaram R. Real-time

fMRI brain computer interfaces: self-regulation of single brain regions to networks. Biol Psychol. (2014) 95:4–20. doi: 10.1016/j.biopsycho.2013.04.010

- 97. Van Ombergen A, Laureys S, Sunaert S, Tomilovskaya E, Parizel PM, Wuyts FL.

Spaceﬂight-induced neuroplasticity in humans as measured by MRI: what do we know so far? Npj Microgravity. (2017) 3:2. doi: 10.1038/s41526-016-0010-8

- 98. Miyasaka H, Orand A, Ohnishi H, Tanino G, Takeda S, Sonoda K. Ability of electrical stimulation therapy to improve the eﬀectiveness of robotic training for paretic upper limbs in patients with stroke. Stroke. (2016) 38:1172– 5. doi: 10.1016/j.medengphy.2016.07.010
- 99. Meadmore KL, Hughes A-M, Freeman CT, Cai Z, Tong D, Burridge E, Rogers JH. Functional electrical stimulation mediated by iterative learning control and 3D robotics reduces motor impairment in chronic stroke. J NeuroEng Rehabilitat. (2012) 9:32. doi: 10.1186/1743-0003-9-32
- 100. Rong W, Li W, Pang M, Hu J, Wei X, Yang B, et al. A Neuromuscular Electrical Stimulation (NMES) and robot hybrid system for multi-joint coordinated upper limb rehabilitation after stroke. J NeuroEng Rehabilitat. (2017) 14:1. doi: 10.1186/s12984-017-0245-y
- 101. Qian Q, Hu X, Lai Q, Ng SC, Zheng W, Poon Y. Early stroke rehabilitation

of the upper limb assisted with an electromyography-driven neuromuscular electrical stimulation-robotic arm. Front Neurol. (2017) 8:447. doi: 10.3389/fneur.2017.00447

- 102. Resquín F, Cuesta Gómez A, Gonzalez-Vargas J, Brunetti F, Torricelli D, Molina

Rueda F, et al. Hybrid robotic systems for upper limb rehabilitation after stroke: a review. Med Eng Phys. (2016) 38:1279–88. doi: 10.1016/j.medengphy.2016.09.001

- 103. Ambrosini E, Ferrante S, Zajc J, Bulgheroni M, Baccinelli W, d’Amico E, et al.

The combined action of a passive exoskeleton and an EMG-controlled neuroprosthesis for upper limb stroke rehabilitation: First results of the RETRAINER project. In: IEEE International Conference on Rehabilitation Robotics (ICORR) London, UK: IEEE, 56–61. (2017).

- 104. Ambrosini E, Russold M, Gfoehler M, Puchinger M, Weber M, Becker S,

et al. A hybrid robotic system for arm training of stroke survivors: concept and ﬁrst

evaluation. IEEE Trans Biomed Eng. (2019) 66:3290–300. doi: 10.1109/TBME.2019.29 00525

105. Ambrosini E, Gasperini G, Johannes Zajc, Immick N, Augsten A, Rossini M, et al. A Robotic System with EMG-Triggered Functional Eletrical Stimulation for Restoring Arm Functions in Stroke Survivors. Neurorehabilitat Neural Repair. 35:334–45. doi: 10.1177/1545968321997769

- 106. Kenah K, Bernhardt J, Cumming T, Spratt N, Luker J, Janssen H. Boredom in

patients with acquired brain injuries during inpatient rehabilitation: a scoping review. Disabil Rehabil. (2017) 40:2713–22. doi: 10.1080/09638288.2017.1354232

- 107. Laver K, George S, Thomas S, Deutsch JE, Crotty M. Virtual reality for stroke

rehabilitation: an abridged version of a Cochrane review. Eur J Phys Rehabil Med.

(2015) 51:497–506. doi: 10.1002/14651858.CD008349.pub3

- 108. Ferrante S, Schauer T, Ferrigno G, Raisch J, Molteni F. The eﬀect

of using variable frequency trains during functional electrical stimulation cycling. Neuromodulation. (2008) 11:216–26. doi: 10.1111/j.1525-1403.2008.0 0169.x

- 109. De Marchis C, Santos Monteiro T, Simon-Martinez C, Conforto A,

Gharabaghi S. (2016). Multi-contact functional electrical stimulation for hand opening: electrophysiologically driven identiﬁcation of the optimal stimulation site. J NeuroEng Rehabilitat. 13:1. doi: 10.1186/s12984-016-0129-6

- 110. Yang K, Meadmore K, Freeman C, Grabham N, Hughes A-M., Wei Y, et al.

Development of user-friendly wearable electronic textiles for healthcare applications. Sensors. (2018) 18:8. doi: 10.3390/s18082410

- 111. Yang K, Freeman C, Torah R, Beeby S, Tudor J. Screen printed fabric electrode

array for wearable functional electrical stimulation. Sensors Actuators A: Phys. (2014) 213:108–15. doi: 10.1016/j.sna.2014.03.025

- 112. Loitz JC, Reinert A, Neumann A-K, Quandt F, Schroeder D, Krautschneider

WH. A ﬂexible standalone system with integrated sensor feedback for multi-pad electrode FES of the hand. Curr Direct Biomed Eng. (2016) 2:391–4. doi: 10.1515/cdbme-2016-0087

- 113. Maleševi´c NM, Maneski LZP, Ili´c V, Jorgovanovi´c N, Bijeli´c G, Keller DB,

Popovi´c T. A multi-pad electrode based functional electrical stimulation system for restoration of grasp. J NeuroEng Rehabilitat. (2012) 9:66. doi: 10.1186/1743-0 003-9-66

- 114. Maleševi´c NM, Popovi´c LZ, Schwirtlich L, Popovi´c DB. Distributed

low-frequency functional electrical stimulation delays muscle fatigue compared to conventional stimulation. Muscle and Nerve. (2010) 42:556–62. doi: 10.1002/mus.21736

115. Sayenko DG, Nguyen R, Popovic MR, Masani K. Reducing muscle fatigue during transcutaneous neuromuscular electrical stimulation by spatially and sequentially distributing electrical stimulation sources. Eur J Appl Physiol. (2014) 114:793–804. doi: 10.1007/s00421-013-2807-4

- 116. Nguyen R, Masani K, Micera S, Morari M, Popovic MR. Spatially

distributed sequential stimulation reduces fatigue in paralyzed triceps surae muscles: a case study. Artif Organs. (2011) 35:1174–80. doi: 10.1111/j.1525-1594.2010.0 1195.x

- 117. Lee JW, Golgouneh L, Dunne A. Comparative assessment of wearable

surface EMG electrode conﬁgurations for biomechanical applications. In: 49th International Conference on Environmental Systems. Boston, USA: IEEE. (2019).

- 118. Salvo P, Raedt R, Carrette E, Schaubroeck D, Vanﬂeteren J, Cardon L. A 3D printed dry electrode for ECG/EEG recording. Sens Actuators A: Physical. (2012) 174:96–102. doi: 10.1016/j.sna.2011.12.017
- 119. Ren L, Xu S, Gao J, Lin Z, Chen Z, Liu B, Liang L, Jiang L. Fabrication of ﬂexible microneedle array electrodes for wearable bio-signal recording. Sensors. (2018) 18:1191. doi: 10.3390/s18041191
- 120. Grozea C, Voinescu S, Fazli CD. Bristle-sensors—low-cost ﬂexible passive dry EEG electrodes for neurofeedback and BCI applications. J Neural Eng. (2011) 8:025008. doi: 10.1088/1741-2560/8/2/025008
- 121. Duente T, Pfeiﬀer M, Rohs M. On-skin technologies for muscle sensing and actuation. In: ACM Int. Joint Conf. on Pervasive and Ubiquitous Computing: Adjunct. New York, USA: IEEE. (2016)
- 122. Xu B, Akhtar A, Liu Y, Chen H, Yeo W-H, Park SS, et al. An epidermal

stimulation and sensing platform for sensorimotor prosthetic control, management of lower back exertion, and electrical muscle activation. Adv Mater. (2016) 28:4462– 71. doi: 10.1002/adma.201504155

- 123. Fall C, Roudjane M, Ghafouri S, Mascret Q, Bielmann M, Tam S,

et al. Non-Invasive and Flexible Electrodes Based on Multimaterial Fiber for sEMG Signal Detection. In: IEEE Life Sciences Conf. (LSC). Montreal, Canada: IEEE. (2018).

124. Musa Mahmood M, Mzurikwao D, Kim Y-S, Lee Y-K, Mishra S, Herbert RD, et al. Fully portable and wireless universal brain–machine interfaces enabled by ﬂexible scalp electronics and deep learning algorithm. Nat Mach Intell. (2019) 1:412–22. doi: 10.1038/s42256-019-0091-7

