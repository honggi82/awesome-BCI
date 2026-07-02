## INTEGRATING EEG AND MEG SIGNALS TO IMPROVE MOTOR IMAGERY CLASSIFICATION IN BRAIN-COMPUTER INTERFACE

# arXiv:1711.07258v2[q-bio.NC]26Mar2018

MARIE-CONSTANCE CORSI Inria Paris, Aramis project-team, 75013, Paris, France Sorbonne Universit´es, UPMC Univ Paris 06, Inserm, CNRS, Institut du cerveau et la moelle (ICM) - Hˆopital Piti´e-Salpˆetri`ere, Boulevard de l'hˆopital, F-75013, Paris, France

MARIO CHAVEZ CNRS UMR7225, Hˆopital Pitie´-Salpeˆtri`ere, Paris, France

DENIS SCHWARTZ, LAURENT HUGUEVILLE Centre de NeuroImagerie de Recherche - CENIR, Centre de Recherche de l’Institut du Cerveau et de la Moelle Epin`ere, Universit´e Pierre et Marie Curie-Paris 6 UMR-S975, Inserm U975, CNRS UMR7225, Groupe Hospitalier Piti´e-Salpˆetri`ere, Paris, France

ANKIT N. KHAMBHATI Department of Bioengineering, University of Pennsylvania, Philadelphia, PA, 19104, USA

DANIELLE S. BASSETT Department of Bioengineering, University of Pennsylvania, Philadelphia, PA, 19104, USA Department of Electrical and Systems Engineering, University of Pennsylvania, Philadelphia, PA, 19104, USA Department of Physics, University of Pennsylvania, Philadelphia, PA, 19104, USA Department of Neurology, University of Pennsylvania, Philadelphia, PA, 19104, USA

FABRIZIO DE VICO FALLANI Inria Paris, Aramis project-team, 75013, Paris, France Sorbonne Universit´es, UPMC Univ Paris 06, Inserm, CNRS, Institut du cerveau et la moelle (ICM) - Hˆopital Piti´e-Salpˆetri`ere, Boulevard de l'hˆopital, F-75013, Paris, France E-mail: fabrizio.devicofallani@gmail.com

We adopted a fusion approach that combines features from simultaneously recorded electroencephalographic (EEG) and magnetoencephalographic (MEG) signals to improve classiﬁcation performances in motor imagery-based brain-computer interfaces (BCIs). We applied our approach to a group of 15 healthy subjects and found a signiﬁcant classiﬁcation performance enhancement as compared to standard single-modality approaches in the alpha and beta bands. Taken together, our ﬁndings demonstrate the advantage of considering multimodal approaches as complementary tools for improving the impact of non-invasive BCIs.

Keywords: classiﬁer fusion; EEG; MEG; brain-computer interface; motor imagery.

1

2

### 1. Introduction

performance.

Brain-computer interfaces (BCIs) exploit the ability of subjects to modulate their brain activity through intentional mental eﬀort, such as in motor imagery (MI). BCIs are increasingly used for control and communication,1–11 and for the treatment of neurological disorders.12–17

2. Materials and Methods

- 2.1. Simultaneous E/MEG recordings

Fifteen healthy subjects (aged 28.13 ± 4.10 years, 7 women), all right-handed, participated in the study. None presented with medical or psychological disorders. According to the declaration of Helsinki, written informed consent was obtained from subjects after explanation of the study, which was approved by the ethical committee CPP-IDF-VI of Paris. All participants received ﬁnancial compensation at the end of their participation. MEG and EEG data were simultaneously recorded with, respectively, an Elekta Neuromag TRIUX® machine (which includes 204 planar gradiometers and 102 magnetometers) and with a 74 EEG-channel system. The EEG electrodes positions on the scalp followed the standard 10-10 montage. EEG signals were referenced to mastoid signals, with the ground electrode located at the left scapula, and impedances were kept lower than 20 kOhms. On average, 1.5 hours was needed for subjects preparation (i.e. explaining the protocol, placing the electrodes, registering the EEG sensor positions and checking the impedances). M/EEG data were recorded in a magnetically shielded room with a sampling frequency of 1 kHz and a bandwidth of 0.01-300 Hz. The subjects were seated in front of a screen at a distance of 90 cm. To ensure the stability of the position of the hands, the subjects laid their arms on a comfortable support, with palms facing upward. We also recorded electromyogram (EMG) signals from the left and right arm of subjects. Expert bioengineers visually inspected EMG activity to ensure that subjects were not moving their forearms during the recording sessions. We carried out BCI sessions with EEG signals transmitted to the BCI2000 toolbox46 via the Fieldtrip buﬀer.47

- 2.2. BCI protocol

Despite their societal and clinical impact, many engineering challenges remain, from the optimization of the control features to the identiﬁcation of the best mental strategy to code the user's intent.18 Furthermore, between 15 and 30 % of the users are aﬀected by a phenomenon called “BCI illiteracy”19 which consists in not being able to control properly a BCI even after several training sessions. BCI illiteracy particularly concerns MI-based BCIs because of the inherent diﬃculty to produce distinguishable brain activity patterns.20

These challenges critically aﬀect the usability of MI-based BCIs21 and have motivated, on the one hand, a deeper understanding of mechanisms associated with MI,22–25 and on the other hand the research of new features to enhance BCI performance for both healthy subjects and patients.26–29 In the latter case, hybrid and multimodal approaches adding respectively diﬀerent type of biosignals27,30 and neuroimaging data, such as near-infrared spectroscopy (NIRS)31–34 and functional magnetic resonance imaging (fMRI),35 have been proven to increase the overall performance.

Here, we consider magnetoencephalography (MEG), which carries complementary information in terms of source depth36 and conductivity37–40 sensitivities, but also radially/tangentially oriented dipole detection.41,4243 While previous studies have demonstrated the feasibility of BCI44 and neurofeedback,45 based on MEG activity, the potential beneﬁt of the combination with EEG signals has been poorly explored. Indeed, such integration might have practical consequences in the light of the recent development of portable MEG sensors, based on optically pumped magnetometers.43

We used the one-dimensional, two-target, rightjustiﬁed box task,48 where subjects had to perform a sustained MI (grasping) of the right hand to hit uptargets, while remaining at rest to hit down-targets. Each run consisted of 32 trials with up and down targets, consisting of a grey vertical bar displayed on the right portion of the screen, equally and randomly distributed across trials.

To address this gap in knowledge, we considered high-density EEG and MEG signals simultaneously recorded in a group of healthy subjects during a MIbased BCI task. We then propose a matching-score fusion approach to test the ability to improve the classiﬁcation of motor-imagery associated with BCI

3

The experiment was divided into two phases:

end, we used a multi-taper frequency transformation based on discrete prolate spheroidal sequences (Slepian sequences51) considered as tapers through the use of the Fieldtrip toolbox.47 A ± 0.5 Hz spectral smoothing through multi-tapering was applied.

- (i) Training: The training phase consisted of ﬁve consecutive runs without any feedback. For a given trial, the ﬁrst second corresponded to the inter-stimulus interval (ISI), where a black screen was presented to the subject. The target appeared and persisted on the screen during subsequent ﬁve seconds (from 1 s to 6 s). During this period subjects had to perform the instructed mental tasks.
- (ii) Testing: The testing phase consisted of six runs with a visual feedback. For a given trial, the ﬁrst second corresponded to the ISI, while the target was presented throughout the subsequent ﬁve seconds, with the same modalities just as in the training phase. In the last three seconds (from 3 s to 6 s), subjects received a visual feedback to control an object that consists of a cursor (a ball here) that starts from the left-middle part of the screen and moves to the right part of the screen with ﬁxed velocity. This gave a ﬁxed of communication rate of 20 commands/minute. Only vertical position was controlled by the subject’s brain activity and it was updated every 28 ms. The aim is to hit the target with the ball according to the instructed mental tasks, i.e. MI for up-targets; resting for down-targets.

At this stage, each epoch was characterized by

- a feature matrix Mi, containing the power spectrum values for every couple of sensor and frequency bin, and whose dimension was 74 × 36, 102 × 36 and 204 × 36, respectively for i = EEG,MAG,GRAD.

We adopted a semi-automatic procedure to extract the most relevant features from the matrices Mi in the training phase. First, we focused on sensors in the motor area contralateral to the movement (see Appendix A.1). In this way, the size of the feature matrices became 8 × 36, 11 × 36 and 22 × 36 respectively for EEG, MAG, and GRAD. Second, for each selected sensor and frequency bin, we performed a non-parametric cluster-based permutation t-test between the power spectrum values of the MI and rest epochs.2,52 To this end, we set a statistical threshold of p < 0.05, false-discovery rate corrected for multiple comparisons, and 500 permutations.

We ﬁnally extracted the Nf most discriminant features within the standard frequency bands

- b = theta (4−7 Hz), alpha (8−13 Hz), beta (14− 29 Hz), gamma (30 − 40 Hz). This allowed us to identify, for each modality i and band b, the best (sensor, frequency bin) couples to be used in the testing phase to compute the features mˆ . Hence, the ﬁnal feature vectors used for the classiﬁcation are given by:

- 2.3. Signal processing and features extraction

We considered both EEG and MEG activity, the latter consisting of magnetometer (MAG) and gradiometer (GRAD) signals which, given their physical properties, can be processed separately.49

ζi,b = [ ˆm1i,b,...,mˆ Ni,bf], (1)

where Nf = 1...,10. The maximal limit of 10 was chosen based on the actual number of features (between 4 and 6) that we used in the recording sessions, conforming to the guidelines associated with similar MI-based BCI and EEG montages.46

As a preliminary step, temporal Signal Space Separation (tSSS)50 was performed using MaxFilter (Elekta Neuromag) to remove environmental noise from MEG activity. All signals were downsampled to 250 Hz and segmented into epochs of ﬁve seconds corresponding to the target period. To simulate online scenarios, no artifact removal method was applied. Expert bioengineers visually inspected the recorded traces to ensure that no major artifacts (e.g. MEG jumps, EEG pops) were present. After veriﬁcation, we then kept all the available epochs.

2.4. Classiﬁcation, fusion, and performance evaluation

We performed a separate classiﬁcation for each value of Nf. Given the relatively small number of features, we used a ﬁve-fold cross-validation in a linear discriminant analysis-based (LDA) classiﬁcation.53,54 LDAs are particularly suited for two-class MI-based BCIs.55

We computed for each sensor the power spectrum between 4 and 40 Hz, with a 1 Hz frequency bin resolution, for both MI and rest epochs. To this

4

To integrate the information from diﬀerent modalities we used a Bayesian fusion approach based on the weighted average method.56–58 Similar to what has been proposed for hybrid-BCI systems,30 we linearly combined the posterior probabilities pi, obtained from the classiﬁcation of each modality i, weighted by the parameter λi:

### 3. Results

Figure 2 shows the grand-average time-frequency maps of the event-related de/synchronization (ERD/S) computed from the MI trials in the testing phase:62 ERD/S = 100 ×

xtarget − µbase

µbase where xtarget was the time-frequency energy of a sensor’s signal for the target period (1−6)s and µbase was the corresponding time-averaged energy in the baseline (0 − 1)s.

pi pEEG + pMAG + pGRAD

λi =

. (2)

In this manner, a higher weight was assigned to the modality that best classiﬁed the data (see Figure 1).

[Figure 1]

[Figure 2]

- Figure 1. Classiﬁer fusion approach for a given fre-

quency bin. The variables pi and λi stand for the posterior probability and the weight parameter associated with the modality i, respectively.

- Figure 2. Grand-average time-frequency maps of ERD/S. Top panels illustrate the visual stimulus that appeared during the target period. Dashed lines mark the start of the target presentation and the feedback periods (see section 2.2, testing phase). The time-frequency decomposition of the signals was obtained through Morlet wavelets between 4 and 40 Hz, with a central frequency of 1 Hz associated with a time resolution of 3 s via the Brainstorm toolbox.63 Positive ERD/S values indicate percentage increases (i.e. neural activity synchronization), while negative values stand for percentage decreases (i.e. neural activity desynchronization)

.

In all modalities, we observed signiﬁcant changes for the alpha (ERD −100%) and beta band (ERD

−60%).64–66 ERDs started to appear just after the target appearance (t = 1 s) and became stronger during the feedback period (t = 3-6 s). Notably, ERDs tended to appear early in the MEG signals as compared to the EEG signals.

- Figure 3 illustrates the candidate features that were selected through the semi-automatic procedure for each modality in the training phase. Features ob-

To assess the classiﬁer performance, we measured the area under the receiver operating characteristic (ROC) curve (AUC) of the computed values of the false positive rate versus the true positive rate. AUC values typically range between one-half (chance level) and one (perfect classiﬁcation).59 We evaluated our fusion approach with respect to the results obtained in each single modality separately (EEG, MAG, GRAD). In addition, we tested the eﬀect of including an increasing number of most signiﬁcant features.

To statistically compare the results, we input the corresponding AUC values into a nonparametric permutation-based ANOVA with two factors: modality (EEG, MAG, GRAD, Fusion) and features (Nf = 1,2,...,10). A statistical threshold of p < 0.05 and 5000 permutations were ﬁxed. We ﬁnally used a Tukey-Kramer method60 to perform a post-hoc analysis with a statistical threshold of p < 0.05. This analysis was performed using routines available in the standard MATLAB and the EEGLAB toolboxes.61

5

tained from MEG signals tended to be more focused both in space (around the primary motor areas of the hand) and in frequency (mostly in the alpha band). This ﬁnding was in line with the fact that lower ERDs were observed in the beta band (see

cept for theta and gamma bands for which we did not observe signiﬁcant improvements with respect to EEG. The highest classiﬁcation performance was obtained in the alpha band (Figure 4), for which we also reported here a signiﬁcant interaction eﬀect between modality and number of features (ANOVA, p = 0.0069). In this case, the AUC values with the fusion were signiﬁcantly higher than those obtained with EEG, MAG, or GRAD separately (TukeyKramer post-hoc, p = 4.3 × 10−9,3.9 × 10−7, and 0.012). To evaluate the classiﬁcation performance in every subject, we considered for each modality the optimal number of features Nf and the best frequency band associated with the highest AUC. Results showed that in thirteen subjects, the fusion led to a better performance as compared to single modalities, with AUC values ranging from 0.55 to 0.85, and relative increments ranging from 1.3% to 50.9% (with an average of 12.8 ± 6%). In only three subjects, the fusion gave equivalent performance (see Table 1). More speciﬁcally, if we compared the performances obtained with the fusion with those resulting from the best single modality, the average improvement was of 4±3%. Noteworthy, this value was of 15±17% when we compared the fusion with EEG, the modality that is the most used during BCI experiments.67,68

- Figure 2).

[Figure 3]

- Figure 3. Spatial and frequency distribution of the features selected for classiﬁcation in each modality. On the left side, the color of the nodes identiﬁes the frequency band (blue for alpha band and red for beta band). The size of the circles is proportional to the number of subjects exhibiting that speciﬁc sensor as the best feature. On the right, the histograms detail the occurrences in every frequency bin for the sensor that was most frequently selected.

Interestingly, the contribution of the diﬀerent modalities to the fusion's performance was highly variable across subjects, as illustrated by the weights associated to the parameter λi (see Figure 5).

[Figure 4]

Fusion improves classiﬁcation performance

In all frequency bands, the type of modality signiﬁcantly aﬀected the AUC values (ANOVA, p < 10−3), whereas the number of features did not have a signiﬁcant impact (p > 0.05). The AUC values obtained with the fusion approach were signiﬁcantly higher than those obtained with any other modality (Tukey-Kramer post-hoc, p < 0.016), ex-

Figure 4. AUC distributions across the 15 subjects, for diﬀerent modalities (EEG, MAG, GRAD, Fusion) and for diﬀerent number of features Nf in the alpha band. White circles represent the associated median values.

6

##### Table 1. Individual performances overview across modalities. In bold, the best AUC obtained for a given subject.

S01 S02 S03 S04 S05 S06 S07 S08 S09 S10 S11 S12 S13 S14 S15 Band alpha alpha beta alpha alpha alpha beta beta alpha alpha alpha alpha beta alpha beta EEG 0.53 0.55 0.48 0.56 0.57 0.55 0.57 0.50 0.60 0.66 0.53 0.55 0.70 0.73 0.60 MAG 0.47 0.48 0.53 0.51 0.50 0.55 0.52 0.62 0.57 0.58 0.69 0.76 0.59 0.64 0.71

GRAD 0.54 0.50 0.55 0.50 0.54 0.55 0.49 0.65 0.64 0.63 0.72 0.62 0.71 0.72 0.85 Fusion 0.55 0.55 0.56 0.57 0.58 0.59 0.57 0.67 0.66 0.70 0.80 0.77 0.76 0.79 0.85

### 4. Discussion

siﬁers (Table 1), suggesting a viable alternative to indirectly reduce the illiteracy phenomenon in noninvasive BCIs.71,72

Improving performance remains one of the most challenging issues of non-invasive BCI systems.55 High classiﬁcation performance would allow eﬀective control of the BCI and feedback to the subject that is crucial to establish an optimal interaction usermachine.19,67,68 BCI performance depends on several human and technological factors, including the ability of subjects to generate distinguishable brain features,3 as well as the robustness of signal processing and classiﬁcation algorithms.55

In this study, we also explored features from other frequency bands such as the gamma band (3040 Hz). However, the obtained results gave marginal improvements as compared to alpha and beta bands. While gamma activity from intracranial recordings or local-ﬁeld potentials is in general related to the initiation of motor/sensory function,25,73–77 the paucity of results in the gamma band could be here partly explained by the low signal-to-noise ratios and volume conduction eﬀects that typically aﬀect scalp EEG and MEG activity.78–80

To this end, we recorded simultaneous EEG and MEG signals in a group of healthy subjects performing a motor imagery-based BCI task. Both EEG and MEG exhibit a high temporal resolution and the sensory motor-related changes are well known in the literature, as is their utility in standard BCI applications.19,44

The core of our approach consisted in weighting automatically the contribution of each modality in an eﬀort to optimize performance. This is an important aspect as the discriminant power of features could suddenly change depending on many factors, such as impedance ﬂuctuations or the presence of artifacts (e.g. isolated EEG electrode pops or MEG jumps). In this case, our fusion approach would take into account such transient ﬂuctuations by silencing the aﬀected modality through a lower weight λi in the classiﬁcation. Slower changes could be related to the increasing ability of individuals to accurately control the BCI.55,67,81–83 In this case, our approach would progressively favor the spatio-temporal features of the modality that better capture those neural plasticity phenomena.

Notably, EEG and MEG signals are closely related but still they are respectively diﬀerent in terms of sensitivity to radial and tangential currents, as well as to extracellular and intracellular currents.40 These complementary properties could be simultaneously exploited by our fusion approach to better identify ERD mechanisms used here to control the BCI.

Results show that independently from the modality and the number of features, the best AUCs were obtained in alpha and (in a more limited way) beta bands, which is consistent with motor imagery's being associated with oscillations in the alpha and beta band.69,70 The proposed fusion approach showed that combining the most signiﬁcant features in each modality led, in a large majority of subjects, to a reduction in the subjects' mental state misclassiﬁcations (see Table 1). By optimizing the choice of the features in each individual, we obtained an average classiﬁcation improvement of 12.8 % as compared to separate EEG, MAG and GRAD clas-

Interestingly, we noticed a high inter-subject variability in the attributed weights (Figure 5). While, this could be associated with the ability of each modality to detect diﬀerent properties of the underlying ERD, further analysis, possibly in the source space,84 is needed to elucidate this aspect and identify the neurophysiological correlates of such variability.

While the average AUC values were relatively low, we noticed that they are highly variable across

7

subject-speciﬁc time-frequency characteristics,88 can be further evaluated to exploit their power in practical applications.

individuals (Table 1) and that they are close to those typically obtained in similar experiment settings.27 Furthermore, it is important to mention that subjects were BCI-na¨ıve and that no preprocessing was applied, with the goal of simulating real-life scenarios. Thus, while a proper pre-processing was likely.

Finally, it is important to note that we tested our fusion approach oﬄine by analyzing previously recorded data. To evaluate the feasibility in online applications, we estimated that for an epoch of 500 ms the time necessary to compute the features, perform the classiﬁcation, and determine the parameter of the fusion, was approximately of 20 ms when Nf = 5. This value is actually compatible with current on-line settings using similar time windows and updating the feedback every 28 ms.46

[Figure 5]

### 5. Conclusions

Our results showed that integrating information from simultaneous EEG and MEG signals improves BCI performance. E/MEG multimodal BCIs may turn out to be an eﬀective approach to enhance the reliability of brain-machine interactions, but much of the progress will depend on the miniaturization of MEG scanners, which currently require a magnetic shielding room (MSR) and sensors cooled via a cryogenic system. Recent eﬀorts proposing miniaturized and cryogenic-free MEG sensors43,89 and avoiding the use of MSRs90 will hopefully oﬀer practical solutions to increase MEG portability and boost the development of multimodal BCIs.

| |
|---|

Figure 5. Contribution of diﬀerent modalities to the individual performance. Pie-diagrams show the λi values (in percentage) obtained for each modality via the fusion approach.

### 6. Acknowledgements

We would like to thank the anonymous reviewers for their constructive comments and suggestions. This work was partially supported by French program “Investissements d'avenir” ANR-10-IAIHU-06; “ANRNIH CRCNS” ANR-15-NEUC-0006-02 and by Army Research Oﬃce (W911NF-14-1-0679). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

to improve the accuracy in each single modality, our aim was rather to assess an improvement in the worst condition. Eventually, thirteen of our ﬁfteen subjects presented a performance improvement with the classiﬁer fusion.

Taken together, these results prove the potential advantage of using simultaneous E/MEG signals to enhance BCI performance. By using a rather simple classiﬁer (LDA), we could include in the classiﬁcation a reduced number of speciﬁc features involved in the motor-related neural mechanisms such as ERD in alpha and beta bands.

### References

- 1. J. J. Vidal, Toward Direct Brain-Computer Communication, Annual Review of Biophysics and Bioengineering 2(1) (1973) 157–180.
- 2. S. Bozinovski, M. Sestakov and L. Bozinovska, Using EEG alpha rhythm to control a mobile robot, Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society, November 1988, pp. 1515–1516 vol.3.

More sophisticated approaches using the whole feature space, such as support vector machines85 and Riemannian geometry,86 as well as alternative fusion strategies, such as boosting, voting, or stacking strategies,55 but also classiﬁcation in source space to improve spatial resolution42,87 and identiﬁcation of

8

- 26(12) (2012) 1510–1522.
- 16. S. Kim and N. Birbaumer, Real-time functional MRI neurofeedback: a tool for psychiatry, Current Opinion in Psychiatry 27 (September 2014) 332–336.
- 17. A. Burns, H. Adeli and J. A. Buford, Brain-computer interface after nervous system injury, Neuroscientist 20 (December 2014) 639–651.
- 18. C. Guger, B. Allison and J. Ushiba, Brain-Computer Interface Research, springer science & business media edn. (Springer Science & Business Media, 2013).
- 19. C. Vidaurre and B. Blankertz, Towards a Cure for BCI Illiteracy, Brain Topography 23(2) (2010) 194– 198.
- 20. B. Z. Allison and C. Neuper, Could Anyone Use a BCI?, Brain-Computer Interfaces, eds. D. S. Tan and A. Nijholt, Human-Computer Interaction Series (Springer London, 2010), pp. 35–54.
- 21. C. Zickler, V. Di Donna, V. Kaiser, A. Al-Khodairy, S. Kleih, A. Kbler, M. Malavasi, D. Mattia, S. Mongardi, C. Neuper, M. Rohm, R. Rupp, P. StaigerSlzer and E. J. Hoogerwerf, BCI applications for people with disabilities: Deﬁning user needs and user requirements, Assistive Technology Research Series, Assistive Technology Research Series 25 2009, pp. 185–189.
- 22. J. Toppi, M. Risetti, L. R. Quitadamo, M. Petti, L. Bianchi, S. Salinari, F. Babiloni, F. Cincotti, D. Mattia and L. Astolﬁ, Investigating the eﬀects of a sensorimotor rhythm-based BCI training on the cortical activity elicited by mental imagery, Journal of Neural Engineering 11 (June 2014) p. 035010.
- 23. V. Kaiser, G. Bauernfeind, A. Kreilinger, T. Kaufmann, A. Kbler, C. Neuper and G. R. Mller-Putz, Cortical eﬀects of user training in a motor imagery based brain-computer interface measured by fNIRS and EEG, NeuroImage 85 Pt 1 (January 2014) 432– 444.
- 24. S. Perdikis, R. Leeb and J. d. R. Milln, Subjectoriented training for motor imagery brain-computer interfaces, Conf Proc IEEE Eng Med Biol Soc 2014

(2014) 1259–1262.

- 25. J. D. Wander, T. Blakely, K. J. Miller, K. E. Weaver, L. A. Johnson, J. D. Olson, E. E. Fetz, R. P. N. Rao and J. G. Ojemann, Distributed cortical adaptation during learning of a braincomputer interface task, Proceedings of the National Academy of Sciences of the United States of America 110 (June

2013) 10818–10823.

- 26. C. Vidaurre, C. Sannelli, K. R. Mller and B. Blankertz, Co-adaptive calibration to improve BCI eﬃciency, Journal of Neural Engineering 8 (April 2011) p. 025009.
- 27. G. Pfurtscheller, B. Z. Allison, C. Brunner, G. Bauernfeind, T. Solis-Escalante, R. Scherer, T. O. Zander, G. Mueller-Putz, C. Neuper and N. Birbaumer, The hybrid BCI, Frontiers in Neuroscience 4 (2010) p. 30.
- 28. F. Pichiorri, F. D. V. Fallani, F. Cincotti, F. Ba-

- 3. J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller and T. M. Vaughan, Braincomputer interfaces for communication and control, Clinical Neurophysiology 113 (June 2002) 767–791.
- 4. M. S. Fifer, G. Hotson, B. A. Wester, D. P. McMullen, Y. Wang, M. S. Johannes, K. D. Katyal, J. B. Helder, M. P. Para, R. J. Vogelstein, W. S. Anderson, N. V. Thakor and N. E. Crone, Simultaneous neural control of simple reaching and grasping with the modular prosthetic limb using intracranial EEG, IEEE Trans Neural Syst Rehabil Eng 22 (May

2014) 695–705.

- 5. T. Carlson and J. d. R. Millan, Brain-Controlled Wheelchairs: A Robotic Architecture, IEEE Robotics Automation Magazine 20 (March 2013) 65–73.
- 6. K. LaFleur, K. Cassady, A. Doud, K. Shades, E. Rogin and B. He, Quadcopter control in three-dimensional space using a noninvasive motor imagery-based brain-computer interface, Journal of Neural Engineering 10 (August 2013) p. 046003.
- 7. J. Jin, B. Z. Allison, T. Kaufmann, A. Kbler, Y. Zhang, X. Wang and A. Cichocki, The changing face of P300 BCIs: a comparison of stimulus changes in a P300 BCI involving faces, emotion, and movement, PloS One 7(11) (2012) p. e49688.
- 8. H.-J. Hwang, J.-H. Lim, Y.-J. Jung, H. Choi, S. W. Lee and C.-H. Im, Development of an SSVEPbased BCI spelling system adopting a QWERTYstyle LED keyboard, Journal of Neuroscience Methods 208 (June 2012) 59–65.
- 9. K. Kashihara, A brain-computer interface for potential non-verbal facial communication based on EEG signals related to speciﬁc emotions, Frontiers in Neuroscience 8 (2014) p. 244.
- 10. L. Naci, R. Cusack, V. Z. Jia and A. M. Owen, The brain’s silent messenger: using selective attention to decode human thought for brain-based communication, J. Neurosci. 33 (May 2013) 9385–9393.
- 11. A. Ortiz-Rosario and H. Adeli, Brain-computer interface technologies: from signal to action, Rev Neurosci 24(5) (2013) 537–552.
- 12. J. J. Daly and J. R. Wolpaw, Braincomputer interfaces in neurological rehabilitation, The Lancet Neurology 7 (November 2008) 1032–1043.
- 13. G. Prasad, P. Herman, D. Coyle, S. McDonough and J. Crosbie, Applying a brain-computer interface to support motor imagery practice in people with stroke for upper limb recovery: a feasibility study, Journal of Neuroengineering and Rehabilitation 7 (December

2010) p. 60.

- 14. C. E. King, P. T. Wang, L. A. Chui, A. H. Do and Z. Nenadic, Operation of a brain-computer interface walking simulator for individuals with spinal cord injury, Journal of Neuroengineering and Rehabilitation 10 (July 2013) p. 77.
- 15. C. Chatelle, S. Chennu, Q. Noirhomme, D. Cruse, A. M. Owen and S. Laureys, Brain-computer interfacing in disorders of consciousness, Brain Injury

9

- theory, instrumentation, and applications to noninvasive studies of the working human brain, Reviews of Modern Physics 65 (April 1993) 413–497.
- 41. C. C. Wood, D. Cohen, B. N. Cuﬃn, M. Yarita and T. Allison, Electrical sources in human somatosensory cortex: identiﬁcation by combined magnetic and potential recordings, Science (New York, N.Y.) 227 (March 1985) 1051–1053.
- 42. D. Sharon, M. S. Hmlinen, R. B. H. Tootell, E. Halgren and J. W. Belliveau, The advantage of combining MEG and EEG: Comparison to fMRI in focally stimulated visual cortex, NeuroImage 36 (July 2007) 1225–1235.
- 43. E. Boto, S. S. Meyer, V. Shah, O. Alem, S. Knappe, P. Kruger, T. M. Fromhold, M. Lim, P. M. Glover, P. G. Morris, R. Bowtell, G. R. Barnes and M. J. Brookes, A new generation of magnetoencephalography: Room temperature measurements using optically-pumped magnetometers, NeuroImage 149(Supplement C) (2017) 404 – 414.
- 44. J. Mellinger, G. Schalk, C. Braun, H. Preissl, W. Rosenstiel, N. Birbaumer and A. Kbler, An MEG-based brain-computer interface (BCI), NeuroImage 36(3) (2007) 581–593.
- 45. H.-L. Halme and L. Parkkonen, Comparing Features for Classiﬁcation of MEG Responses to Motor Imagery, PLOS ONE 11 (December 2016) p. e0168766.
- 46. G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer and J. R. Wolpaw, BCI2000: a generalpurpose brain-computer interface (BCI) system, IEEE transactions on bio-medical engineering 51 (June 2004) 1034–1043.
- 47. R. Oostenveld, P. Fries, E. Maris and J.-M. Schoﬀelen, FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data, FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data, Computational Intelligence and Neuroscience, Computational Intelligence and Neuroscience 2011, 2011 (December

2010) p. e156869.

- 48. J. R. Wolpaw, D. J. McFarland, T. M. Vaughan and G. Schalk, The Wadsworth Center brain-computer interface (BCI) research and development program, IEEE transactions on neural systems and rehabilitation engineering: a publication of the IEEE Engineering in Medicine and Biology Society 11 (June

2003) 204–207.

- 49. P. C. Hansen, M. L. Kringelbach and R. Salmelin, MEG: An introduction to Methods, oxford university press edn. 2010.
- 50. S. Taulu and J. Simola, Spatiotemporal signal space separation method for rejecting nearby interference in MEG measurements, Phys Med Biol 51 (April

2006) 1759–1768.

- 51. D. Slepian, Prolate spheroidal wave functions, fourier analysis, and uncertainty #x2014; V: the discrete case, The Bell System Technical Journal 57

biloni, M. Molinari, S. C. Kleih, C. Neuper, A. Kbler and D. Mattia, Sensorimotor rhythm-based braincomputer interface training: the impact on motor cortical responsiveness, Journal of Neural Engineering 8(2) (2011) p. 025020.

- 29. F. Pichiorri, G. Morone, M. Petti, J. Toppi,

I. Pisotta, M. Molinari, S. Paolucci, M. Inghilleri, L. Astolﬁ, F. Cincotti and D. Mattia, Braincomputer interface boosts motor imagery practice during stroke recovery, Annals of Neurology 77 (May 2015) 851–865.

- 30. G. Mller-Putz, R. Leeb, M. Tangermann, J. Hhne, A. Kbler, F. Cincotti, D. Mattia, R. Rupp, K. R. Mller and J. d. R. Milln, Towards Noninvasive Hybrid Brain-Computer Interfaces: Framework, Practice, Clinical Application and Beyond, Proceedings of the IEEE 103(6) (2015) 926–943.
- 31. R. Sitaram, A. Caria and N. Birbaumer, Hemodynamic braincomputer interfaces for communication and rehabilitation, Neural Networks 22 (November

2009) 1320–1328.

- 32. S. Fazli, J. Mehnert, J. Steinbrink, G. Curio, A. Villringer, K. Mller and B. Blankertz, Enhanced performance by a hybrid NIRSEEG brain computer interface, NeuroImage 59 (January 2012) 519–529.
- 33. Y. Tomita, F.-B. Vialatte, G. Dreyfus, Y. Mitsukura, H. Bakardjian and A. Cichocki, Bimodal BCI using simultaneously NIRS and EEG, IEEE transactions on bio-medical engineering 61 (April 2014) 1274– 1284.
- 34. A. P. Buccino, H. O. Keles and A. Omurtag, Hybrid EEG-fNIRS Asynchronous Brain-Computer Interface for Multiple Motor Tasks, PloS One 11(1)

- (2016) p. e0146610.

35. L. Perronnet, A. Lcuyer, M. Mano, E. Bannier, F. Lotte, M. Clerc and C. Barillot, Unimodal Versus Bimodal EEG-fMRI Neurofeedback of a Motor Imagery Task, Frontiers in Human Neuroscience 11

- (2017).

- 36. B. N. Cuﬃn and D. Cohen, Comparison of the magnetoencephalogram and electroencephalogram, Electroencephalography and Clinical Neurophysiology 47 (August 1979) 132–146.
- 37. C. D. Geisler and G. L. Gerstein, The surface EEG in relation to its sources, Electroencephalography and Clinical Neurophysiology 13 (December 1961) 927– 934.
- 38. M. R. Delucchi, B. Garoutte and R. B. Aird, The scalp as an electroencephalographic averager, Electroencephalography and Clinical Neurophysiology 14 (April 1962) 191–196.
- 39. R. Cooper, A. L. Winter, H. J. Crow and W. G. Walter, Comparison of subcortical, cortical and scalp activity using chronically indwelling electrodes in man, Electroencephalography and Clinical Neurophysiology 18 (February 1965) 217–228.
- 40. M. Hmlinen, R. Hari, R. J. Ilmoniemi, J. Knuutila and O. V. Lounasmaa, Magnetoencephalography-

10

- 68. M. Clerc, L. Bougrain and F. Lotte, Brain-Computer Interfaces 2: Technology and Applications, wiley edn. (Wiley, 2016).
- 69. G. Pfurtscheller, C. Neuper, D. Flotzinger and M. Pregenzer, EEG-based discrimination between imagination of right and left hand movement, Electroencephalogr Clin Neurophysiol 103 (December

1997) 642–651.

- 70. G. Pfurtscheller and C. Neuper, Motor imagery and direct brain-computer communication, Proceedings of the IEEE 89 (July 2001) 1123–1134.
- 71. D. J. McFarland and J. R. Wolpaw, Brain-Computer Interfaces for Communication and Control, Communications of the ACM 54(5) (2011) 60–66.
- 72. J. v. Erp, F. Lotte and M. Tangermann, BrainComputer Interfaces: Beyond Medical Applications, Computer 45 (April 2012) 26–34.
- 73. C. Tallon-Baudry and O. Bertrand, Oscillatory gamma activity in humans and its role in object representation, Trends in Cognitive Sciences 3 (April

1999) 151–162.

- 74. E. Rodriguez, N. George, J.-P. Lachaux, J. Martinerie, B. Renault and F. J. Varela, Perception’s shadow: long-distance synchronization of human brain activity, Nature 397 (February 1999) p. 430.
- 75. R. T. Canolty, E. Edwards, S. S. Dalal, M. Soltani, S. S. Nagarajan, H. E. Kirsch, M. S. Berger, N. M. Barbaro and R. T. Knight, High Gamma Power Is Phase-Locked to Theta Oscillations in Human Neocortex, Science 313 (September 2006) 1626–1628.
- 76. D. Cheyne, S. Bells, P. Ferrari, W. Gaetz and A. C. Bostan, Self-paced movements induce highfrequency gamma oscillations in primary motor cortex, NeuroImage 42 (August 2008) 332–342.
- 77. S. D. Muthukumaraswamy, Functional Properties of Human Primary Motor Cortex Gamma Oscillations, Journal of Neurophysiology 104 (September 2010) 2873–2885.
- 78. M. Grosse-Wentrup, B. Schlkopf and J. Hill, Causal inﬂuence of gamma oscillations on the sensorimotor rhythm, NeuroImage 56 (May 2011) 837–842.
- 79. M. Grosse-Wentrup and B. Schlkopf, High -power predicts performance in sensorimotor-rhythm braincomputer interfaces, J Neural Eng 9 (August 2012) p. 046001.
- 80. C. Jeunet, B. N’Kaoua, S. Subramanian, M. Hachet and F. Lotte, Predicting Mental Imagery-Based BCI Performance from Personality, Cognitive Proﬁle and Neurophysiological Patterns, PLoS ONE 10(12)

(2015) p. e0143962.

- 81. E. A. Curran and M. J. Stokes, Learning to control brain activity: A review of the production and control of EEG components for driving braincomputer interface (BCI) systems, Brain and Cognition 51 (April 2003) 326–336.
- 82. B. H. Dobkin, Braincomputer interface technology as a tool to augment plasticity and outcomes for neurological rehabilitation, The Journal of Physiology 579

(May 1978) 1371–1430.

- 52. S. Bozinovski, Controlling Robots Using EEG Signals, Since 1988, ICT Innovations 2012, Advances in Intelligent Systems and Computing (Springer, Berlin, Heidelberg, 2013), pp. 1–11.
- 53. K. Fukunaga, Introduction to Statistical Pattern Recognition (2Nd Ed.) (Academic Press Professional, Inc., San Diego, CA, USA, 1990).
- 54. R. O. Duda, P. E. Hart and D. G. Stork, Pattern Classiﬁcation (2Nd Edition) (Wiley-Interscience, 2000).
- 55. F. Lotte, M. Congedo, A. Lcuyer, F. Lamarche and B. Arnaldi, A review of classiﬁcation algorithms for EEG-based brain-computer interfaces, Journal of Neural Engineering 4 (June 2007) R1–R13.
- 56. D. Ruta and B. Gabrys, An Overview of Classiﬁer Fusion Methods, Computing and Information Systems 7 (February 2000) 1–10.
- 57. F. Roli and G. Fumera, Analysis of Linear and Order Statistics Combiners for Fusion of Imbalanced Classiﬁers, Multiple Classiﬁer Systems, Lecture Notes in Computer Science, (Springer, Berlin, Heidelberg, June 2002), pp. 252–261.
- 58. F. Roli, Multiple Classiﬁer Systems, Encyclopedia of Biometrics, eds. S. Z. Li and A. Jain (Springer US, 2009), pp. 981–986.
- 59. I. Witten, E. Frank, M. Hall and C. Pal, Data Mining

- 4th Edition, morgan kaufmann edn., 2016).

- 60. J. Zar, Biostatistical analysis, pearson education edn. 1999.
- 61. A. Delorme and S. Makeig, EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis, J. Neurosci. Methods 134 (March 2004) 9–21.
- 62. G. Pfurtscheller and F. H. Lopes da Silva, Eventrelated EEG/MEG synchronization and desynchronization: basic principles, Clinical Neurophysiology 110 (November 1999) 1842–1857.
- 63. F. Tadel, S. Baillet, J. Mosher, D. Pantazis and R. Leahy, Brainstorm: A User-Firendly Application for MEG/EEG Analysis, Computational Intelligence and Neuroscience 2011 (January 2011).
- 64. C. Neuper and G. Pfurtscheller, Event-related dynamics of cortical rhythms: frequency-speciﬁc features and functional correlates, Int J Psychophysiol 43 (December 2001) 41–58.
- 65. C. Neuper, R. Scherer, M. Reiner and G. Pfurtscheller, Imagery of motor actions: Diﬀerential eﬀects of kinesthetic and visualmotor mode of imagery in single-trial EEG, Cognitive Brain Research 25 (December 2005) 668–677.
- 66. G. Pfurtscheller, C. Brunner, A. Schlgl and F. H. Lopes da Silva, Mu rhythm (de)synchronization and EEG single-trial classiﬁcation of diﬀerent motor imagery tasks, NeuroImage 31 (May 2006) 153–159.
- 67. M. Clerc, L. Bougrain and F. Lotte, Brain-Computer Interfaces 1: Methods and Perspectives, wiley edn. (Wiley, 2016).

11

- zler, G. Deuschl and J. Raethjen, Beamformer source analysis and connectivity on concurrent EEG and MEG data during voluntary movements, PloS One 9(3) (2014).
- 88. Y. Yang, S. Chevallier, J. Wiart and I. Bloch, Time-frequency optimization for discrimination between imagination of right and left hand movements based on two bipolar electroencephalography channels, EURASIP Journal on Advances in Signal Processing 2014(1) (2014) p. 38.
- 89. R. Jimnez-Martnez and S. Knappe, Microfabricated Optically-Pumped Magnetometers, High Sensitivity Magnetometers, Smart Sensors, Measurement and Instrumentation (Springer, Cham, 2017), pp. 523– 551.
- 90. A. R. Sorbo, G. Lombardi, L. La Brocca, G. Guida, R. Fenici and D. Brisinda, Unshielded magnetocardiography: Repeatability and reproducibility of automatically estimated ventricular repolarization parameters in 204 healthy subjects, Ann Noninvasive Electrocardiol (December 2017).

(March 2007) 637–642.

- 83. M. Grosse-Wentrup, D. Mattia and K. Oweiss, Using braincomputer interfaces to induce neural plasticity and restore function, J. Neural Eng. 8(2) (2011) p. 025004.
- 84. J. Gross, S. Baillet, G. R. Barnes, R. N. Henson, A. Hillebrand, O. Jensen, K. Jerbi, V. Litvak, B. Maess, R. Oostenveld, L. Parkkonen, J. R. Taylor, V. van Wassenhove, M. Wibral and J.-M. Schoﬀelen, Good practice for conducting and reporting MEG research, Neuroimage 65 (January 2013) 349–363.
- 85. T. Lai, M. Schrder, T. Hinterberger, J. Weston, M. Bogdan, N. Birbaumer and B. Schlkopf, Support vector channel selection in BCI, IEEE Transactions on Biomedical Engineering 51(6) (2004) 1003–10.
- 86. A. Barachant, S. Bonnet, M. Congedo and C. Jutten, Classiﬁcation of covariance matrices using a Riemannian-based kernel for BCI applications, Neurocomputing 112 (July 2013) 172–178.
- 87. M. Muthuraman, H. Hellriegel, N. Hoogenboom, A. R. Anwar, K. G. Mideksa, H. Krause, A. Schnit-

12

### Appendix A

[Figure 6]

Figure A.1. Pre-selected EEG and MEG sensors (left motor area).

