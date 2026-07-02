## Brain-Computer Interface Controlled Robotic Gait Orthosis

An H. Do1, Po T. Wang2, Christine E. King2, Sophia N. Chun3, Zoran Nenadic2,4

### arXiv:1208.5024v3[cs.HC]26Aug2013

Abstract—Background: Excessive reliance on wheelchairs in individuals with tetraplegia or paraplegia due to spinal cord injury (SCI) leads to many medical co-morbidities, such as cardiovascular disease, metabolic derangements, osteoporosis, and pressure ulcers. Treatment of these conditions contributes to the majority of SCI health care costs. Restoring able-bodylike ambulation in this patient population can potentially reduce the incidence of these medical co-morbidities, in addition to increasing independence and quality of life. However, no biomedical solution exists that can reverse this loss of neurological function, and hence novel methods are needed. Brain-computer interface (BCI) controlled lower extremity prostheses may constitute one such novel approach.

Methods: One able-bodied subject and one subject with paraplegia due to SCI underwent electroencephalogram (EEG) recordings while engaged in alternating epochs of idling and walking kinesthetic motor imagery (KMI). These data were analyzed to generate an EEG prediction model for online BCI operation. A commercial robotic gait orthosis (RoGO) system (suspended over a treadmill) was interfaced with the BCI computer to allow for computerized control. The subjects were then tasked to perform ﬁve, 5-min-long online sessions where they ambulated using the BCI-RoGO system as prompted by computerized cues. The performance of this system was assessed with cross-correlation analysis, and omission and false alarm rates.

Results: The ofﬂine accuracy of the EEG prediction model averaged 86.30% across both subjects (chance: 50%). The cross-correlation between instructional cues and the BCI-RoGO walking epochs averaged across all subjects and all sessions was 0.812±0.048 (p-value<10−4). Also, there were on average 0.8 false alarms per session and no omissions.

Conclusion: These results provide preliminary evidence that restoring brain-controlled ambulation after SCI is feasible. Future work will test the function of this system in a population of subjects with SCI. If successful, this may justify the future development of BCI-controlled lower extremity prostheses for free overground walking for those with complete motor SCI. Finally, this system can also be applied to incomplete motor SCI, where it could lead to improved neurological outcomes beyond those of standard physiotherapy.

Index Terms—Brain computer interface, gait, walking, robotic gait orthosis, Lokomat.

I. INTRODUCTION

# I

Ndividuals with tetraplegia or paraplegia due to spinal cord injury (SCI) are unable to walk and most are wheelchair

- 1Department of Neurology, University of California, Irvine, CA, USA,

email: and@uci.edu

- 2Department of Biomedical Engineering, UCI, CA, USA
- 3Department of Spinal Cord Injury, Long Beach Veterans Affairs Medical

Center, Long Beach, CA, USA

- 4Department of Electrical Engineering and Computer Science, UCI, CA,

USA

bound. Decreased physical activity associated with prolonged wheelchair use leads to a wide range of co-morbidities such as metabolic derangements, heart disease, osteoporosis, and pressure ulcers [1]. Unfortunately, no biomedical solutions can reverse this loss of neurological function, and treatment of these co-morbidities contributes to the bulk of medical care costs for this patient population [1]. While commercially available lower extremity prostheses can help restore basic ambulation via robust manual control, their adoption among the SCI community remains low, likely due to cost, bulkiness, and energy expenditure inefﬁciencies. Hence, novel approaches are needed to restore able-bodied-like ambulation in people with SCI. If successful, these will improve the quality of life in this population, and reduce the incidence and cost of medical co-morbidities as well as care-giver burden.

A brain-computer interface (BCI) controlled lower extremity prosthesis may be one such novel approach. It can be envisioned that a combination of an invasive brain signal acquisition system and implantable functional electrical stimulation (FES) electrodes can potentially act as a permanent BCI prosthesis. However, for safety reasons, the feasibility of brain-controlled ambulation must ﬁrst be established using noninvasive systems.

This concept was explored in the authors’ prior work [2]– [4] in which subjects (both able-bodied and SCI) used an electroencephalogram (EEG) based BCI to control the ambulation of an avatar within a virtual reality environment. In these studies, subjects utilized idling and walking kinesthetic motor imagery (KMI) to complete a goal-oriented task of walking the avatar along a linear path and making stops at 10 designated points. In addition, two out of ﬁve subjects with SCI achieved BCI control that approached that of a manually controlled joystick. While these results suggest that accurate BCI control of ambulation is possible after SCI, the translation of this technology from virtual reality to a physical prosthesis has not been achieved. In this study, the authors report on the ﬁrst case of integrating an EEG-based BCI system with a robotic gait orthosis (RoGO), and its successful operation by both able-bodied and SCI subjects.

II. METHODS

To facilitate the development of a BCI-controlled RoGO, EEG data were recorded from subjects as they engaged in alternating epochs of idling and walking KMI. These data were then analyzed ofﬂine to generate an EEG prediction model for online BCI operation. A commercial RoGO system (suspended over a treadmill), was interfaced with the BCI computer to

allow for computerized control. In a series of ﬁve, 5-minlong online tests, the subjects were tasked to ambulate using the BCI-RoGO system when prompted by computerized cues. The performance of this system was assessed by calculating the cross-correlation and latency between the computerized cues and BCI-RoGO response, as well as the omission and false alarm rates.

- A. Training Data Acquisition

Ethical approval was obtained from the Institutional Review Board at the Long Beach Veterans Affairs Medical Center (LBVA) and the University of California, Irvine (UCI). Subjects were recruited from a population of able-bodied individuals, or those with chronic, complete motor paraplegia due to SCI (> 12 months post-injury). The exclusion criteria for subjects with SCI were severe spasticity, contractures, restricted range of motion, or fractures in the lower extremities, pressure ulcers, severe osteoperosis, or orthostatic hypotension. These criteria were ruled out in a safety screening evaluation consisting of an interview, a physical exam, lower extremity dual-energy x-ray absorptiometry (DEXA) scan and x-rays, and a tilt-table exam.

An actively shielded 64-channel EEG cap was ﬁrst mounted on the subjects’ head and impedances were reduced to <10 KΩ. EEG signals were acquired using 2 linked NeXus-32 bioampliﬁers (Mind Media, Roermond-Herten, The Netherlands) at a sampling rate of 256 Hz. The subjects were suspended into a treadmill-equipped RoGO (Lokomat, Hocoma, Volketswil, Switzerland) using partial weight unloading (see Figure 1). Note that unlike overground orthoses, this system facilitates safe and easy testing conditions for the early development of BCI-prostheses for ambulation. Finally, EEG data were collected as the subjects alternated between 30-sec epochs of idling and walking KMI for a total of 10 min, as directed by computer cues. This entails vivid imagination of walking during walking KMI cues, and relaxation during idling cues. During this procedure, the subjects stood still with their arms at their sides.

- B. Electromyogram and Leg Movement Measurement

Electromyogram (EMG) was measured to rule out BCI control by voluntary leg movements in able-bodied subjects. To this end, baseline lower extremity EMG were measured under 3 conditions: active walking (subject voluntarily walks while the RoGO servos are turned off); cooperative walking (subject walks synergistically with the RoGO); and passive walking (the subject is fully relaxed while the RoGO makes walking movements). Three pairs of surface EMG electrodes were placed over the left quadriceps, tibialis anterior, and gastrocnemius (Figure 1), and signals were acquired with a bioampliﬁer (MP150, Biopac, Goleta, CA), bandpass ﬁltered (0.1-1000 Hz), and sampled at 4 KHz. In addition, leg movements were measured by a gyroscope (Wii Motion Plus, Nintendo, Kyoto, Japan) with a custom wristwatch-like enclosure, strapped to the distal left lower leg (proximal to the ankle, see Figure 1) [5]. Approximately 85% body-weight unloading was necessary for proper RoGO operation. The walking velocity was set to 2 km/hr.

[Figure 1]

Fig. 1. The experimental setup showing a subject suspended in the RoGO, while donning an EEG cap, surface EMG electrodes, and a gyroscope on the left leg. A monitor (not shown), placed in front of the subject at eye-level, presented instructional cues.

C. Ofﬂine Analysis

An EEG prediction model was generated using the methods described in Wang et al. [3], which are brieﬂy summarized here. First, the training EEG data were subjected to an automated algorithm to exclude those EEG channels with excessive artifacts. The EEG epochs corresponding to “idling” and “walking” states were then transformed into the frequency domain, and their power spectral densities (PSD) were integrated over 2-Hz bins. The data then underwent dimensionality reduction using a combination of classwise principal component analysis (CPCA) [6], [7] and approximate information discriminant analysis (AIDA) [8]. The resulting 1D spatio-spectral features were extracted by:

f = TAΦC(d) (1) where f ∈ R is the feature, d ∈ RB×C are single-trial spatiospectral EEG data (B-the number of frequency bins, C-the number of retained EEG channels), ΦC : RB×C → Rm is a piecewise linear mapping from the data space to the m-dimensional CPCA-subspace, and TA : Rm → R is an AIDA transformation matrix. Detailed descriptions of these techniques are found in [7], [8]. A linear Bayesian classiﬁer:

I, if P(I |f ) > P(W |f ) W, otherwise

(2)

f ∈

was then designed in the feature domain, where P(I |f ) and P(W |f ) are the posterior probabilities of “idling” and “walking” classes, respectively. The performance of the Bayesian classiﬁer (2), expressed as a classiﬁcation accuracy, was then assessed by performing stratiﬁed 10-fold cross-validation [9]. This was achieved by using 90% of the EEG data to train the parameters of the CPCA-AIDA transformation and the classiﬁer. The remaining 10% of the data then underwent the above transformation and classiﬁcation. This process was

repeated 10 times, each time using a different set of 9 folds for training and the remaining 1 fold for testing. Finally, the optimal frequency range [FL,FH] was found by increasing the lower and upper frequency bounds and repeating the above procedure until the classiﬁer performance stopped improving [10]. The parameters of the prediction model, including [FL,FH], the CPCA-AIDA transformation, and the classiﬁer parameters, were then saved for real-time EEG analysis during online BCI-RoGO operation. The above signal processing and pattern recognition algorithms were implemented in the BCI software and were optimized for real-time operation [10].

- D. BCI-RoGO Integration

To comply with the institutional restrictions that prohibit software installation, the RoGO computer was interfaced with the BCI using a pair of microcontrollers (Arduino, SmartProjects, Turin, Italy) to perform mouse hardware emulation. Microcontroller #1 relayed commands from the BCI computer to microcontroller #2 via an Inter-Integrated Circuit (I2C) connection. Microcontroller #2 then acted as a slave device programmed with mouse emulation ﬁrmware [11] to automatically manipulate the RoGO’s user interface. This setup enabled the BCI computer to directly control the RoGO idling and walking functions.

- E. Online Signal Analysis

During online BCI-RoGO operation, 0.75-sec segments of EEG data were acquired every 0.25 sec in a sliding overlapping window. The PSD of the retained EEG channels were calculated for each of these segments and used as the input for the signal processing algorithms described in Section II-C. The posterior probabilities of idling and walking classes were calculated using the Bayes rule, as explained in Section II-C.

- F. Calibration

Similar to the authors’ prior work [2]–[4], [10], [12], [13], the BCI-RoGO system is modeled as a binary state machine with “idling” and “walking” states. This step is necessary to reduce noise in the online BCI operation and minimize the mental workload of the subject. To this end, the posterior probability was averaged over 2 sec of EEG data, P¯(W|f ), and compared to two thresholds, TI and TW, to initiate state transitions. Speciﬁcally, the system transitioned from “idling” to “walking” state (and vice versa) when P¯ > TW (P¯ < TI), respectively. Otherwise, the system remained in the current state.

The values of TI and TW were determined from a short calibration procedure. Speciﬁcally, the system was set to run in the online mode (with the RoGO walking disabled) as the subject alternated between idling or walking KMI for ∼5 min. The values of P¯ were plotted in a histogram to empirically determine the values of TI and TW. A brief familiarization online session with feedback was used to further ﬁne-tune these threshold values.

- G. Online Evaluation

In an online evaluation, the subjects, while mounted in the RoGO, used idling/walking KMI to elicit 5 alternating 1-min epochs of BCI-RoGO idling/walking, as directed by static, textual computer cues (see Additional Files for videos). Ideally, during walking KMI, the underlying EEG changes should initiate and maintain BCI-RoGO walking until walking KMI stops. The subjects were instructed to make no voluntary movements and to keep their arms still at their side. Left leg EMG and movements were measured as described in Section II-B. This online test was performed 5 times in a single experimental day.

Online performance was assessed using the following metrics [10], [12], [13]:

- 1) Cross-correlation between the cues and BCI-RoGO walking
- 2) Omissions (OM)—failure to activate BCI-RoGO walking during the “Walk” cues
- 3) False Alarms (FA)—initiation of BCI-RoGO walking during the “Idle” cues

For able-bodied subjects, analysis of EMG and leg movement data was performed to ascertain whether RoGO walking was entirely BCI controlled. First, to demonstrate that covert movements were not used to initiate BCI-RoGO walking, gyroscope and rectiﬁed EMG data (in the 40-400 Hz band) were compared to the BCI decoded “walking” states in each session. Ideally, the initiation of these states should precede EMG activity and leg movements. Then, to establish whether voluntary movements were used to maintain BCI-RoGO walking, EMG during these epochs were compared to the baselines (see Section II-B). To this end, EMG data were segmented by individual steps based on the leg movement pattern [5], as measured by the gyroscope. The PSD of these EMG segments were then averaged and compared to those of the baseline walking conditions. Ideally, the EMG power during BCIRoGO walking should be similar to that of passive walking and different from those of active and cooperative walking.

- H. Controls

To determine the signiﬁcance of each online BCI-RoGO session’s performance, a nonlinear auto-regressive model was created:

Xk+1 = αXk + βWk, X0 ∼ U(0,1) (3) Yk = h(Xk) (4)

where Xk is the state variable at time k, Wk ∼ U (0,1) is uniform white noise, Yk is the simulated posterior probability, and h is a saturation function that ensures Yk ∈ [0,1]. Let Pk := P(W|f k) be a sequence of online posterior probabilities calculated in Section II-C. Assuming the sequence {Pk} is wide-sense stationary with mean µ and variance σ2, the coefﬁcients α and β can be determined from:

α = ρ (5) αµ +

β 2

= µ (6)

TABLE I DEMOGRAPHIC DATA OF THE STUDY SUBJECTS. ASIA = AMERICAN SPINAL INJURY ASSOCIATION.

|Subject<br><br>|Age<br><br>|Gender<br><br>|Prior BCI Experience|SCI Status|
|---|---|---|---|---|
|1|42|Male<br><br>|∼5 hours|N/A|
|2<br><br>|25|Male<br><br>|∼3 hours|T6 ASIA B|

where ρ is the correlation coefﬁcient between Pk+1 and Pk. Using these coefﬁcients, 10,000 Monte Carlo trials were performed for each online session. Each sequence of simulated posteriors, {Yk}, was then processed as in Section II-F above, and the cross-correlation between the cues and simulated BCI-RoGO state sequence was calculated. An empirical pvalue was deﬁned as a fraction of Monte Carlo trials whose maximum correlation was higher than that of the online session.

III. RESULTS

Two subjects (one able-bodied and one with paraplegia due to SCI) were recruited for this study and provided their informed consent to participate. Their demographic data are described in Table 1 below. Subject 2, who was affected by paraplegia due to SCI, underwent the screening evaluation and met all study criteria. All subjects successfully underwent the training EEG procedure. Their EEG prediction models were generated as described in Section II-C based on training EEG data (Section II-A). This ofﬂine analysis resulted in a model classiﬁcation accuracy of 94.8±0.8% and 77.8±2.0% for Subjects 1 and 2, respectively (chance: 50%). The EEG feature extraction maps are shown in Figure 2. After the calibration procedure (Section II-F), a histogram of posterior probabilities was plotted (Figure 3). Based on this histogram and a familiarization trial, the respective values of TI and TW were set at 0.04 and 0.65 for Subject 1, and 0.50 and 0.90 for Subject 2.

The performances from the 5 online sessions for both subjects are summarized in Table 2. The average cross-correlation between instructional cues and the subjects’ BCI-RoGO walking epochs was 0.812±0.048. As a control, the maximum cross-correlation between the instructional cues and simulated BCI operation using 10,000 Monte Carlo trials were 0.438 and 0.498 for Subjects 1 and 2, respectively. This indicates that all of the cross-correlations in Table 2 were signiﬁcant with an empirical p-value < 10−4. Also, there were no omissions for either subject. The false alarm rate averaged 0.8 across all sessions and both subjects. While the duration of these false alarm epochs averaged 7.42±2.85 sec, much of this time can be attributed to the RoGO’s locked-in startup sequence (∼5 sec). In addition, each subject managed to achieve 2 sessions with no false alarms. Videos of a representative online session for the able bodied subject (Subject 1) and for the subject with SCI (Subject 2) are provided as downloadable supplemental media. Alternatively, online versions can be found at: http://www.youtube.com/watch?v=W97Z8fEAQ7g, and http://www.youtube.com/watch?v=HXNCwonhjG8.

For Subject 1, the EMG and leg movement data from online sessions were analyzed as described in Section II-G. EMG

[Figure 2]

- Fig. 2. The CPCA-AIDA feature extraction maps for both subjects. Since feature extraction is piecewise linear, there is one map for each of the 2 classes. Brain areas with values close to +1 or -1 are most salient for distinguishing between idling and walking classes at this frequency. The most salient features were in the 8-10 Hz bin for Subject 1 and the 10-12 Hz bin for Subject 2.

[Figure 3]

- Fig. 3. A representative histogram of averaged posterior probabilities, P¯(W|f ) for both subjects.

and gyroscope measurements indicated that no movement occurred prior to the initiation of BCI decoded “walking” states (see Figure 4). When compared to the baselines, the EMG during online BCI-RoGO walking in all 3 muscle groups were statistically different from those of active or cooperative walking conditions (p < 10−13), and were not different from those of passive walking (p = 0.37). These results conﬁrm that the BCI-RoGO system was wholly BCI controlled. Note that passive walking is known to generate EMG activity [14], hence a similar level of activity during BCI-RoGO walking (Figure 5) is expected. Furthermore, since Subject 2 does not have any voluntary motor control of the lower extremities, there was no

TABLE II CROSS-CORRELATION BETWEEN THE BCI-ROGO WALKING AND CUES AT SPECIFIC LAGS, NUMBER OF OMISSIONS AND FALSE ALARMS, AND THE AVERAGE DURATION OF FALSE ALARM EPOCHS.

| |Session<br><br>|Cross-correlation (lag in sec)|Omissions<br><br>|False Alarms (avg. duration in sec)|
|---|---|---|---|---|
|Subject 1<br><br>|1|0.771 (10.25)|0<br><br>|1 (12.00)|
| |2<br><br>|0.741 (4.50)|0|2 (5.50±0.00)|
| |3|0.804 (3.50)|0<br><br>|1 (5.30)|
| |4|0.861 (4.50)<br><br>|0<br><br>|0|
| |5|0.870 (12.00)|0<br><br>|0|
| |Avg.|0.809±0.056 (6.95±3.89)|0|0.8 (7.08±3.28)|
|Subject 2<br><br>|1<br><br>|0.781 (6.25)|0<br><br>|1 (8.80)|
| |2|0.878 (6.75)<br><br>|0|0|
| |3<br><br>|0.782 (6.25)|0<br><br>|0|
| |4<br><br>|0.851 (14.25)|0|1 (5.50)|
| |5|0.785 (5.75)<br><br>|0|2 (8.40±4.10)|
| |Avg.<br><br>|0.815±0.046 (7.85±3.60)<br><br>|0|0.8 (7.76±2.80)|
| |Overall Avg.<br><br>|0.812±0.048 (7.40±3.56)<br><br>|0<br><br>|0.8 (7.42±2.85)|

[Figure 4]

- Fig. 4. Results from a representative online session for each subject, showing epochs of idling and BCI-RoGO walking determined from the gyroscope trace (green blocks). The red trace represents the decoded BCI states, while the blue trace represents the instructional cues. The thick/thin blocks indicate walking/idling. Corresponding EMG (gold: quadriceps; teal: tibialis anterior; purple: gastrocnemius) are also shown. Note that EMG was not measured for Subject 2.

[Figure 5]

- Fig. 5. Representative EMG PSD of the quadriceps for Subject 1, demonstrating that EMG during BCI-RoGO walking are different from active or cooperative walking baseline conditions, and are similar to passive walking.

need to perform EMG measurements and analysis.

IV. DISCUSSION AND CONCLUSION

The results of this study demonstrate that BCI-controlled lower extremity prostheses for walking are feasible. Both subjects gained purposeful and highly accurate control of the BCI-RoGO system on their ﬁrst attempt. It is particularly

notable that the subject with paraplegia due to SCI (Subject 2) was able to accomplish this with minimal prior BCI experience and after only a brief 10 min training data acquisition session. To the best of the authors’ knowledge, this represents the ﬁrstever demonstration of a person with paraplegia due to SCI regaining brain-driven basic ambulation and completing a goaloriented walking task.

The EEG prediction models for both subjects in this study had a high ofﬂine classiﬁcation accuracy. In the case of Subject 1, the performance was higher than his performances in prior BCI walking avatar studies (Subject 1 in [2], and Subject A1 in [3]). Note that the gain in performance was achieved despite the subject being suspended in the RoGO (as opposed to being seated as in [2], [3]). Examination of the prediction models also revealed that the salient brain areas underlying walking KMI varied from subject to subject (Figure 2). Collectively, these areas likely overlie the pre-frontal cortex, supplementary motor, and the leg and arm sensorimotor representation areas, and are consistent with those previously reported. For example, activation of the pre-frontal cortex and supplementary motor area during walking motor imagery has been described in functional imaging studies [15]. Similarly, involvement of the leg and bilateral arm areas during walking KMI have been reported in [3], [4] and may be associated with leg movement and arm swing imagery. This EEG prediction model was further validated by generating highly separable posterior probability distributions (Figure 3) and facilitating highly accurate online BCI-RoGO control. Finally, since it was generated through a data-driven procedure, the modeling approach is subject speciﬁc and may accommodate for the neurophysiological variability across subjects [2]–[4].

Both subjects attained highly accurate online control of the BCI-RoGO system. This was achieved immediately on each subjects’ ﬁrst attempt and generally improved through the course of the 5 online sessions. The average online crosscorrelation between the computer cues and BCI response (0.812) was higher than those achieved with lower (0.67) and upper (0.78) extremity BCI-prostheses [10], [12], despite EEG being acquired under more hostile (ambulatory) conditions. Furthermore, not only did the subject with paraplegia attain immediate BCI-RoGO control, but he also had a higher average online performance than the able-bodied subject. This

implies that future BCI-prostheses for restoring overground walking after SCI may be feasible. Additionally, all of the subjects’ online BCI-RoGO sessions were purposeful with a 100% response rate (no omissions). Although Subject 1 had no false alarms by the end of the experiment, Subject 2 still experienced false alarms in the ﬁnal session. Although few in number and short in duration, false alarms carry the risk of bodily harm, and this problem must be addressed in the development of future BCI-prostheses for overground walking. Table 2 also shows that the maximum correlation is attained at an average lag of 7.4 sec. Most of this lag can be attributed to the RoGO’s locked-in power-down sequence (∼5 sec). Minor sources of delay include a combination of user response time and the 2-sec long posterior probability averaging window (see Section II-F). This delay can potentially be minimized with additional user training in a controlled environment. Also, reducing the averaging window may eliminate some of the delay, but this would be at the expense of increasing the false alarm and omission rates. This trade-off will be examined in future studies.

With no more than ∼5 hr of relevant BCI experience (operating the BCI walking avatar as described in [2]–[4]), both subjects attained a high-level of control of the BCIRoGO system after undergoing a series of short procedures (i.e. 10 min training data acquisition, 5 min calibration, 5 min familiarization). This indicates that a data-driven EEG prediction model as well as prior virtual reality training may have facilitated this rapid acquisition of BCI control. In addition, this model enables BCI operation using an intuitive control strategy, i.e. walking KMI to induce walking and idling KMI to stop. This is in contrast to requiring subjects to undergo months of training in order to acquire a completely new skill of modulating pre-selected EEG signal features as frequently done in operant conditioning BCI studies. However, it remains unclear whether applying an EEG decoding model generated from idling/walking KMI will be robust enough against EEG perturbations caused by other simultaneous cognitive and behavioral processes common during ambulation (e.g. talking, head turning). Anecdotally, no disruption of BCI operation was observed in this study and related previous BCI studies [3], [4] when the subjects engaged in brief conversations or hand and arm gestures during the familiarization session. Formalized testing of this hypothesis would require additional studies to be performed.

Based on the above observations, this data-driven BCI approach may be necessary for future intuitive and practical BCI-controlled lower extremity prostheses for people with SCI. This approach would enable subjects with SCI to use intuitive BCI control strategies such as KMI of walking or attempted (albeit ineffective) walking. Similar to Subject 2 in this study, this can potentially be accomplished with minimal user training and supervision from the experiment operator. Finally, this approach may enhance the appeal and practicality of future BCI-controlled lower extremity prostheses for ambulation by reducing the time burden and associated costs.

In conclusion, these results provide convincing evidence that BCI control of ambulation after SCI is possible, which warrants future studies to test the function of this system in

a population of subjects with SCI. Since participants with SCI were able to operate the BCI-walking simulator [3], [4], it is expected that they can readily transfer these skills to the BCI-RoGO system, similar to Subject 2. If successful, such a system may justify the future development of BCIcontrolled lower extremity prostheses for free overground walking for those with complete motor SCI. This includes addressing issues such as additional degrees of freedom (e.g. turning, velocity modulation, transitioning between sitting and standing), as well as appropriate solutions for signal acquisition (e.g. invasive recordings). Finally, the current BCI-RoGO system can also be applied to gait rehabilitation in incomplete motor SCI. It can be hypothesized that coupling the behavioral activation of the supraspinal gait areas (via the BCI) and spinal cord gait central pattern generators (feedback driving via the RoGO) may provide a unique form of Hebbian learning. This could potentially improve neurological outcomes after incomplete SCI beyond those of standard gait therapy.

ACKNOWLEDGMENT

This project was funded by the Long Beach Veterans Affairs Southern California Institute for Research and Education (SCIRE) Small Projects Grant, the Long Beach Veterans Affairs Advanced Research Fellowship Grant, the American Brain Foundation, the National Institutes of Health (Grant UL1 TR000153), and the National Science Foundation (Award: 1160200).

REFERENCES

- [1] R. L. Johnson, C. A. Brooks, and G. G. Whiteneck. Cost of traumatic spinal cord injury in a population-based registry. Spinal Cord, 34(8):470–480, 1996.
- [2] P. T. Wang, C. E. King, L. A. Chui, Z. Nenadic, and A. H. Do. BCI controlled walking simulator for a BCI driven FES device. In Proc of RESNA Ann Conf, 2010.
- [3] Po T Wang, Christine E King, Luis A Chui, An H Do, and Zoran Nenadic. Self-paced brain–computer interface control of ambulation in a virtual reality environment. Journal of Neural Engineering, 9(5):056016, 2012.
- [4] Christine E King, Po T Wang, Luis A Chui, An H Do, and Zoran Nenadic. Operation of a brain-computer interface walking simulator for individuals with spinal cord injury. Journal of Neuroengineering and Rehabilitation, 10: 77(1), 2013.
- [5] K. Aminian, B. Najaﬁ, C. B¨ula, P. F. Leyvraz, and Ph. Robert. Spatiotemporal parameters of gait measured by an ambulatory system using miniature gyroscopes. J Biomech, 35(5):689–699, 2002.
- [6] K. Das, S. Osechinskiy, and Z. Nenadic. A classwise PCA-based recognition of neural data for brain-computer interfaces. In Proc IEEE Eng Med Biol Soc, pages 6519–6522, 2007.
- [7] K. Das and Z. Nenadic. An efﬁcient discriminant-based solution for small sample size problem. Pattern Recogn, 42(5):857–866, 2009.
- [8] K. Das and Z. Nenadic. Approximate information discriminant analysis: A computationally simple heteroscedastic feature extraction technique. Pattern Recogn, 41(5):1548–1557, 2008.
- [9] R. Kohavi. A study of cross-validation and bootstrap for accuracy estimation and model selection. In Int Joint C Art Int, pages 1137– 1145, 1995.
- [10] A. H. Do, P. T. Wang, A. Abiri, C. E. King, and Z. Nenadic. Braincomputer interface controlled functional electrical stimulation system for ankle movement. J Neuroeng Rehabil, 8(49), 2011.
- [11] Arduino UNO Mouse HID version 0.1, Mar 2011. http://hunt.net.nz/users/darran/.
- [12] C. E. King, P. T. Wang, M. Mizuta, D. J. Reinkensmeyer, A. H. Do, S. Moromugi, and Z. Nenadic. Noninvasive brain-computer interface driven hand orthosis. In Proc 33rd Ann Int Conf of the IEEE Eng in Med and Biol Soc, pages 5786–5789, 2011.

- [13] A. H. Do, P. T. Wang, C. E. King, A. Schombs, S. C. Cramer, and Z. Nenadic. Brain-computer interface controlled functional electrical stimulation device for foot drop due to stroke. In Proc 34th Ann Int Conf of the IEEE Eng in Med and Biol Soc (accepted), 2012.
- [14] S. Mazzoleni, G. Stampacchia, E. Cattin, E. Bradaschia, M. Tolaini, B. Rossi, and M. C. Carrozza. Effects of a robot-mediated locomotor training on EMG activation in healthy and SCI subjects. In Proc IEEE Int Conf Rehab Robotics, pages 378–382, 2009.
- [15] Christian La Foug`ere, Andreas Zwergal, Axel Rominger, Stefan F¨orster, Gunther Fesl, Marianne Dieterich, Thomas Brandt, Michael Strupp, Peter Bartenstein, and Klaus Jahn. Real versus imagined locomotion: a [18F]-FDG PET-fMRI comparison. Neuroimage, 50(4):1589–1598, 2010.

