###### METHODS ARTICLE

published: 28 April 2014 doi: 10.3389/fnhum.2014.00244

## HUMAN NEUROSCIENCE

# Decoding of four movement directions using hybrid NIRS-EEG brain-computer interface

### M. Jawad Khan1, Melissa Jiyoun Hong2 and Keum-Shik Hong1,3*

- 1 Department of Cogno-Mechatronics Engineering, Pusan National University, Busan, Republic of Korea
- 2 Department of Education Policy and Social Analysis, Columbia University, New York, NY, USA
- 3 School of Mechanical Engineering, Pusan National University, Busan, Republic of Korea

Edited by: Francesco Di Russo, University of Rome “Foro Italico,” Italy

Reviewed by: Mederic Descoins, NYU Langone Medical Center, USA Rodolphe J. Gentili, University of Maryland, USA

*Correspondence: Keum-Shik Hong, Department of Cogno-Mechatronics Engineering, Pusan National University, 2 Busandaehak-ro, Guemjeong-gu, Busan 609-735, Republic of Korea e-mail: kshong@pusan.ac.kr

The hybrid brain-computer interface (BCI)’s multimodal technology enables precision brain-signal classiﬁcation that can be used in the formulation of control commands. In the present study, an experimental hybrid near-infrared spectroscopy-electroencephalography (NIRS-EEG) technique was used to extract and decode four different types of brain signals. The NIRS setup was positioned over the prefrontal brain region, and the EEG over the left and right motor cortex regions. Twelve subjects participating in the experiment were shown four direction symbols, namely, “forward,” “backward,” “left,” and “right.” The control commands for forward and backward movement were estimated by performing arithmetic mental tasks related to oxy-hemoglobin (HbO) changes. The left and right directions commands were associated with right and left hand tapping, respectively. The high classiﬁcation accuracies achieved showed that the four different control signals can be accurately estimated using the hybrid NIRS-EEG technology.

Keywords: electroencephaelography, near-infrared spectroscopy, hybrid brain-computer interface, motor execution, arithmetic mental task, linear discriminant analysis

### INTRODUCTION

Brain-computer interface (BCI) is a methodology that correlates brain activities with external devices. The recent research and trend have demonstrated the enormous potential of the BCI approach (Matthews et al., 2008; Nicolas-Alonso and Gomez-Gil, 2012; Ortiz-Rosario and Adeli, 2013). The material advances in the cutting-edge technology, moreover, has reduced the cost of BCI equipment. The BCI domain comprehends both invasive and non-invasive methods. Invasive methods such as electrical-corticography (ECoG), though showing promising signal-acquisition results, are not recommended, as they entail very signiﬁcant risks. Non-invasive methods are much safer alternatives in this regard (Min et al., 2010).

The major non-invasive modalities include electroencephalography (EEG), magneto encephalography (MEG), functional magnetic resonance imaging (fMRI), and functional near-infrared spectroscopy (fNIRS). Each has its own strengths and limitations; the selection of one over another for brain-imaging applications will rely on the cost of the equipment as well as the spatial and temporal resolution required for the given objective (Min et al., 2010).

EEG is a medical imaging technique that gauges brain activity by measuring, via metal electrodes positioned on the scalp, the voltage ﬂuctuations on the scalp resulting from neurons’ action potentials (Niedermeyer and Lopes da Silva, 1999; Rehan and Hong, 2012). The drawback of EEG is the poor spatial resolution that does not allow an accurate localization, that is, identiﬁcation of the brain source signal (Ball et al., 2009).

NIRS is another non-invasive brain-imaging technique that alternatively utilizes the near-infrared (NIR) spectrum of light (wavelength 600–1000nm) to measure the hemodynamic

response represented by oxygenated hemoglobin (HbO), deoxygenated hemoglobin (HbR), cytochrome oxidase (CytOx) and water (H2O) concentration changes (Nagdyman et al., 2003; Irani et al., 2007; Bhutta et al., 2014). In most analyses, two hemodynamic variations due to brain activites are focused: increased oxygenation (resulting from the increased neural activity) and decreased deoxygenation (Matsuyama et al., 2009). Increased oxygen consumption in the course of performing increasingly difﬁcult mental tasks has been demonstrated (Verner et al., 2013). fNIRS has also shown the ability to detect the fast optical response (Hu et al., 2011), however the hemodynamic response is mostly used for analysis.

EEG offers good temporal resolution (∼0.05s) but poor spatial resolution (∼10mm), while fNIRS provides only moderate temporal resolution (∼1s) and also moderately better spatial resolution (∼5mm) (Nicolas-Alonso and Gomez-Gil, 2012). Another advantage of fNIRS to EEG is its robustness to noise (Waldert et al., 2012). The objective of a hybrid BCI (Pfurtscheller et al., 2010) is either to improve the classiﬁcation accuracy or/and to generate more control commands than the case of a single modality. The reason why Fazli et al. (2012) could improve the classiﬁcation accuracy by using a hybrid EEG and fNIRS conﬁguration is that they used the union of two cases (i.e., detected by either EEG or fNIRS). This was possible because the window size for which the features are identiﬁed has been set to include both fNIRS and EEG data. Even for some cases that EEG could not detect, fNIRS could detect them. For motor execution, the average classiﬁcation accuracy by EEG alone was 90%, but EEG + HbR provided 93%, see Table 1 in Fazli et al. (2012). The previous studies on single modality have shown that the classiﬁcation accuracy for two commands using fNIRS was about 65% (Stangl et al.,

### METHODS

2013), and that for four commands using EEG (rotations and movements of the left/right wrists) was about 65% (Vuckovic and Sepulveda, 2012). The objective in this paper, however, is to generate more commands without losing the classiﬁcation accuracy. In this paper, four commands will be generated: two from the prefrontal cortex and two from the motor cortex by conﬁguring fNIRS and EEG in such a way that each control signal is generated from its associated brain region. In this way, a new command can be generated in every 0.6s and the achieved classiﬁcation accuracy was over 80%.

##### PARTICIPANTS AND EXPERIMENTAL PARADIGM

Twelve healthy volunteers (all male;10 right handed, two left handed; aged 24–34 years) participated in the experiment. The experiment was conducted under the declaration of Helsinki and consent was taken from the subjects priror to the start of experiment. The experiment was performed in a conﬁned room to reduce disturbance from the environment. The subjects were sat in a comfortable chair with their arms on arm rests and instructed to relax. A screen nearly 70cm away from the subjects was placed on which left, right, forward, and backward arrows were displayed. On display of each arrow, a time marker starts at the bottom of screen indicationg the start and end of stimulus. For right and left directions, the subjects were asked to tap their associated hands 10 times during the time period shown on the screen for 10s. For forward and backward directions, the subjects were

The BCI techniques to control a wheel chair are diverse: eye movement and blinking based (Gneo et al., 2011; Lin and Yang, 2012), emotions based (Fattouh et al., 2013), and event related and state control (Galán et al., 2008; Huang et al., 2012; Carlson and Millán, 2013). All these are reactive BCI, in which output from the brain is generated in reaction to an external stimulation. The novelty in this work is the proposition of a hybrid conﬁguration of EEG and fNIRS for active BCI, whose classiﬁcation accuracy is over 80%. Using four brain tasks (left/right motor execution, mental counting, and mental arithmetic), four commands were generated. In the proposed conﬁguration, EEG electrodes are placed on the motor cortex region and NIRS optodes on the prefrontal cortex region. The left and right directions were decoded by tapping of the left or the right hand, and the mental arithmetic and the mental counting was used to decode backward and forward directions. The classiﬁcation accuracies of the 12 subjects justify that the proposed conﬁguration is suiltable for BCI and direction decoding which can be used for the generation of control commands for movement executions for the patients suffering from lower-limb disorders.

|[Figure 1]<br><br>FIGURE 2 | Optode location for EEG and NIRS. (A) 8 EEG electrodes placement over the Cz of the brain, (B) 12 channel locations on the prefrontal brain region using three sources and eight detectors.|
|---|

|[Figure 2]<br><br>FIGURE 1 | Experimental paradigm. One complete data set over the span of a minute, consisting of four rest periods, two task periods detected by NIRS from the prefrontal brain region and two motor execution periods detected from C3 and C4 regions of brain using EEG.|
|---|

asked to do mental counting for 10s and arithmetic subtraction for 10s. A training session was performed before the start to make the subjects familier with the paradigm. The total duration of each experiment for each subject was 5min, divided into rest and activity periods. The time duration of each data sample was 60s. The initial 5s of the experiment was the rest period, after which the subjects were shown left or right direction symbols and requested to physically tap their left or right hand accordingly, at a frequency of 1Hz over a 10s interval. The subjects were also instructed to increase the strength of tap for left hand for better discrimination of signals. The next 5s was another rest period, subsequent to which the subjects were shown a forward or backward direction symbol for an interval of 10s. The subjects were instructed to perform arithmetic subtraction, on a task sheet placed 25cm away prior to the start of the experiment, upon the display of the backward direction symbol. For the mental arithmetic task, the subjects were asked to mentally perform a series of arithmetic calculations that were given on the sheet in a pseudorandom order. These calculations consisted of subtraction of a two-digit number (between 10 and 20) from a three-digit number throughout the task period with successive subtraction of a twodigit number from the result of the previous subtraction (e.g., 695-19, 706-12, 894-15, etc). This mental activation period was followed by a 5-s rest period, after which the subjects were again shown the left or right direction symbol and instructed, once again, to tap their hand at a 1Hz frequency over the time span of 10s. If in a previous case the subjects were shown the left direction symbol, the next time the indicated direction symbol was the opposite one. The directed hand activity was followed by 5s rest, which was followed in turn by 10s of mental activation. In this case as well, the next shown direction was reversed, according to which the subjects were asked to perform an arithmetic counting

for indicated forward direction. For the mental counting task, the subjects were asked to mentally count down from number “99” backwards. For “Stop” the subjects were asked not to perform any activity. A check on EEG and NIRS data values was placed to distinguish the activation and resting state by deﬁning the baseline and activity. The movement command can only be produced if there is activity in any one of the four brain regions else the state should be termed as “Stop” state. Figure 1 shows one complete sample process; the second sample was taken immediately after the obtainment of the ﬁrst.

##### SENSOR CONFIGURATION

Eight EEG electrodes were placed on the motor cortex region on the scalp and 12 channel NIRS was placed on the prefrontal brain region. The reason for using NIRS on the prefrontal cortex is because it can discriminate between two activities from the prefrontal region with high classiﬁcation accuracies (Naito et al., 2007; Power et al., 2010; Verner et al., 2013; Naseer et al., 2014) whereas the same cannot be done using EEG (Knyazev, 2013). Meanwhile NIRS signals are affected by dense hairs (Gervain et al., 2011) making EEG a better option for the detection of brain activities from the motor cortex region. Furthermore, if both modalities are positioned at the same brain location, they induce noise in each other thus reducing the strength of obtained signals for BCI (Safaie et al., 2013). Using the current setup, four signals were obtained thus enhancing the performance of NIRS by combining with EEG setup.

##### DATA ACQUISITION

#### The brain activities related to the mental tasks and motor executions were measured from the NIRS and EEG, respectively. Eight Ag/AgCl EEG electrodes were placed on C3, C4, T3, T4,

|[Figure 3]<br><br>FIGURE 3 | System block diagram. The complete process from signal acquisition to control commands generation.|
|---|

P3, P4, F3, and F4 locations according to the International 10–20 system (Homan et al., 1987; Pivick et al., 1993; Jurcak et al., 2007), and the data were recorded by g-MOBIlab+ biosignal acquisition device (Christoph Guger, Austria) at a sampling rate of 256Hz. The NIRS-System (DYNOT, NIRx Medical Technologies, USA) was used in this experiment with wave length of 760 and 830nm, respectively. A total of three sources and eight detectors forming a combinational pair of 12 channels were used in the experiment. This assembly was placed on Fp1 and Fp2 regions of the brain and the optodes were placed in the way that they cover the whole prefrontal area in order to maximize the probability of locating the activated region of brain. The sampling frequency used for the acquisition of NIRS signals was 1.81Hz. Figure 2 shows the source-detector locations for the optode placement for EEG and NIRS.

##### DATA ANALYSIS

The fNIRS signals were obtained using the modiﬁed Beer-Lambert law (Coyle et al., 2007; Hu et al., 2010, 2012;

Kamran and Hong, 2013; Naseer and Hong, 2013).

Iin (λ) Iout (t;λ) = α(λ) × c (λ) × l × d (λ) + η, (1)

A(t;λ) = ln

−1

- A(t;λ1)
- A(t;λ2)

cHbO(t) cHbR(t) =

- αHbO (λ1) αHbR (λ1)
- αHbO (λ2) αHbR (λ2)

1 l × d(λ)

·

, (2)

where A is the absorbance of light (optical density), Iin is the incident intensity of light, Iout is the detected intensity of light, α is the speciﬁc extinction coefﬁcient in μM−1cm−1, c is the absorber concentration in μM, l is the distance between the source and detector in cm, d is the differential path-length factor, and η is the loss of light due to scattering. In order to remove noise from the hemodynamic response, different techniques are used (Santosa et al., 2013). In the present study, respiration- and pulse-related

|[Figure 4]<br><br>FIGURE 4 | Brain-signal acquisition: Each spike from the left or right motor cortex represents a hand tapping with the right or left hand, respectively. The concentration change in the prefrontal brain region reﬂects the change from rest to mental counting (“forward”) and mental subtraction (“backward”).|
|---|

noises were removed from the data using Gaussian low-pass ﬁltering and wavelet transform (Ye et al., 2009; Hu et al., 2013). The β-band falling within the 12–30Hz range was obtained by online band-pass ﬁltering of the EEG signals (Zaepffel et al., 2013; Kaiser et al., 2014). The epochs lasting 10s were estimated by segmenting the recordings from +1 to +11s relative to the onset of the tapping stimulus, thus yielding ﬁve epochs for each left and right hand activity (Delorme and Makeig, 2004; Subasi and Gursoy, 2010; Turnip et al., 2011; Turnip and Hong, 2012). Linear discriminant analysis was used as the classiﬁer. The features in the case of EEG were the mean values of peak amplitudes of channels C3 and C4 whereas in the case of NIRS, the mean values of HbO and HbR were used (Lotte et al., 2007; Zhang et al., 2013; Naseer et al., 2014). An online analysis was performed on the data by downsampling EEG data to 1.82Hz to synchronize with the NIRS sampling rate. For both modalities, one data sample was obtained approximately after 0.5s, which was then processed at 250Hz to obtain the control command. Figure 3 shows the complete process for control command genereation for BCI.

### RESULTS

The signals extracted from the left and right brain hemispheres (the C3 and C4 regions) and the frontal brain hemisphere (the Fp1 and Fp2 regions) are shown in Figure 4. The signal from the motor cortex region reﬂects the action potential generated due to the ﬁring of neurons when an motor execution task was performed. The signal from the prefrontal region is the hemodynamic change of HbO from the rest to mental execution period.

The association between movement and rest state was developed by taking the common rest state as “Stop” indication. This is also beneﬁcial as using this methodology only one command can be generated at one time and thus reduces the chance of missclassiﬁcation. The movement command can only be produced if there is activity in any one of the four brain regions else the state should be termed as “Stop” state as shown in Figure 5 and Table 1.

The left- and right-signal classiﬁcations are shown in Figure 6. Similary forward and backward mental tasks are represented in Figure 7. Figures 5, 6 show changes of state of data with respect to time. The results indicate a signiﬁcant difference between the

|[Figure 5]<br><br>FIGURE 5 | Stop condition: Common rest state of the three signals is selected as stop command. The “Stop” command can only be generated if absolute rest is detected from three brain regions.|
|---|

states. Table 2 lists the classiﬁcation accuracies for all trials of the 12 subjects.

### DISCUSSION

The ﬁrst objective of this study, which was achieved, was to detect four different classes of signal for generation of control commands for movement estimation suitable for BCI purposes. Two classes of signal were obtained by EEG using motor execution from the left and right motor cortex regions, and two classes are

- Table 1 | Brain activities of EEG and NIRS for different control commands.

Brain activity Command EEG NIRS

Left hand tapping Rest Left Right hand tapping Rest Right Rest Mental arithmetic Back Rest Mental counting Forward Rest Rest Stop

obtained by NIRS from the prefrontal brain region using mental counting and arithmetic. These two tasks are simple tasks that are very easy to perform and can be detected from the prefrontal cortex. For the decoding application they serve their purpose well and have already been used in several BCI studies (Naito et al., 2007; Power et al., 2012; Naseer et al., 2014). Figure 4 clearly shows that each tap recorded from the left and right brain hemispheres due to the motor execution was recorded as a signal spike from the reference position. The time interval between each tap was maintained consistent at approximately 1 s. In order to differentiate between the left- and right-executed signals, each trial was separated by a time interval of 20s. It was observed that the HbO concentration changes during the mental task began to increase 2s after the subjects were prompted, and that the HbO level required almost 12s to settle after the termination of that signal. Accordingly, the time gap between the two NIRS tasks was set at 20s.

The classiﬁcation of left and right hand tapping is performed by increasing the magnitude of left hand tapping from the right hand tapping. It has been reported in Jochumsen et al. (2013) and Robinson et al. (2013) that the neuronal

|[Figure 6]<br><br>FIGURE 6 | EEG data classiﬁcation for left and right control commands. (A) Shows the classiﬁcation of trials for “Left” and “Stop” command signals for Subject 7, (B) Shows the classiﬁcation of trials for “Right” and “Stop” command signals for Subject 6.|
|---|

|[Figure 7]<br><br>FIGURE 7 | NIRS data classiﬁcation for forward and backward control commands. (A) Shows the classiﬁcation of trials for “Forward” and “Stop” command signals for Subject 3, (B) Shows the classiﬁcation of trials for “Backward” and “Stop” command signals for Subject 7.|
|---|

response due to fast and slow movement is different and can be distinguished with high classiﬁcation accuracy. Figures 6, 7 show clearly that the four corresponding signals are separable and, thus, utilizable for generation of BCI control commands.

The observed classiﬁcation accuracies for the 12 subjects signiﬁcantly show that the proposed research is suitable for BCI purpose. In comparison to other studies in which two control commands are generated based on motor and arithmetic tasks with low classiﬁcation accuracies results (Stangl et al., 2013), the results have shown potential for control command generation with high classiﬁcation accuracy. Moreover four stage classiﬁer is required if only one modality is used for four signals acquisition which may results in signiﬁcant decrease in accuracy (Vuckovic and Sepulveda, 2012). Using the current setup, the same results with better accuracy are achieved: The accuracies of “Forward vs. Stop” and “Backward vs. Stop” trials were 80.2% and 83.6%, respectively, due to the selection of oxy-hemoglobin (HbO) as a classiﬁcation feature for both control commands. This is the ﬁrst

time that four intended movements are decoded using a hybrid BCI. Wolpaw and McFarland (2004) and the previous two hybrid EEG-NIRS studies (Fazli et al., 2012; Kaiser et al., 2014) have shown discrimination of two signals that can be used to generate two control commands whereas in this paper four control commands have been generated.

The generated commands can be used for those people who cannot perform motor imagery (Vidaurre and Blankertz, 2010) or in such cases that the patient cannot touch any machine directly, for instance, prosthetic legs, working with remote controlled devices, etc. Naseer et al. (2014) have shown binary decision decoding for rehabilitation, whereas in this research the four control commands can be associated to four different decisions. Moreover, the previous hybrid EEG based researches for rehabilitation have shown the use of P300 and steady state visual evoked potentials (Li et al., 2013; Xu et al., 2013) to generate four control commands based on reactive tasks. As motor imagery and motor execution activate the same brain area (Beisteiner et al., 1995; Porro et al., 1996), the same goal can be achived by this

###### Table 2 | Classiﬁcation accuracies: four control command accuracies of 12 subjects for left vs. stop, right vs. stop, forward vs. stop, and backward vs. stop.

Subject Left vs. Right vs. Forward vs. Back vs. Stop (%) Stop (%) Stop (%) Stop (%)

- 1 98.4 98.7 81.1 86.5
- 2 99.8 99.2 79.1 84.1
- 3 93.2 94.7 81.2 85.4
- 4 97.7 96.5 80.1 80.8
- 5 98.1 88.2 81.2 86.9
- 6 91.1 99.5 84.2 86.6
- 7 99.2 98.1 77.2 81.1
- 8 98.0 98.2 83.1 87.1
- 9 91.2 90.4 80.2 83.1
- 10 85.0 84.1 74.1 76.3
- 11 94.5 95.2 82.8 86.1
- 12 90.1 94.0 78.2 79.3 Mean 94.7 ± 4.6 94.7 ± 4.8 80.2 ± 2.7 83.6 ± 3.5

research using active tasks. Also, it is known that fNIRS can decode multiple signals from the same brain area: for instance, mental counting and music imagery (Power et al., 2012) and picture imagery and mental arithmetic (Naito et al., 2007) from the same prefrontal cortex. Therefore, there is a potential that the total number of commands in the current EEG and fNIRS conﬁguration can be increased to up to seven. Further research can be carried out using advanced adaptive ﬁltering techniques (Rehan and Hong, 2013), optimal feature sets, and/or combined EEGNIRS features to achieve better classiﬁcation results that can be used by patients with lower limb disorder to control wheelchair or prostheses.

### CONCLUSION

In this research, a hybrid fNIRS and EEG conﬁguration for decoding four movment commands was proposed. The NIRS setup was used to decode the prefrontal activities based on hemodynamic changes of HbO using mental arithmetic and mental counting as tasks. The EEG response detected from the motor cortex region was used to decode other two direction commands. Both modalities were synchronized to obtain control commands at the same time. The results of classiﬁcation accuracies were highly encouraging and certainly will prove fruitfully applicable to BCI systems and purposes. The use of wirelss systems and translation of the control commands into machine codes will enable effective control of a robotic system suitable for rehabilitation purposes.

### AUTHOR CONTRIBUTIONS

M. Jawad Khan has conducted all the experiments and carried out the data processing. Melissa J. Hong has examined the data and participated in revising the manuscript. Keum-Shik Hong has suggested the theoretical aspects of the current study and supervised all the process from the beginning. All the authors have approved the ﬁnal manuscript.

### ACKNOWLEDGMENTS

This work was supported by the National Research Foundation of Korea funded by the Ministry of Education, Science and Technology, Korea (grant no. MEST-2012-R1A2A2A0 1046411).

### REFERENCES

Ball, T., Kern, M., Mutschler, I., Aertsen, A., and Schulze-Bonhage, A. (2009). Signal quality of simultaneously recorded invasive and noninvasive EEG. Neuroimage 46, 708–716. doi: 10.1016/j.neuroimage. 2009.02.028

Beisteiner, R., Höllinger, P., Lindinger, G., Lang, W., and Berthoz, A. (1995). Mental representations of movements. Brain potentials associated with imagination of hand movements. Electroencephalogr. Clin. Neurophysiol. 96, 183–193. doi: 10.1016/0168-5597(94)00226-5

Bhutta, M. R., Hong, K.-S., Kim, B.-M., Hong, M.-J., Kim, Y.-H., and Lee, S.-H. (2014). Note: three wavelengths near-infrared spectroscopy system for compensating the light absorbance by water. Rev. Sci. Instrum. 85, 1–3. doi: 10.1063/1.4865124

Carlson, T., and Millán, J. R. (2013). Brain-controlled wheelchairs: a robotic architecture. IEEE Robot. Automat. Mag. 20, 65–73. doi: 10.1109/MRA.2012. 2229936

Coyle, S. M., Ward, T. E., and Markham, C. M. (2007). Brain-computer interface using a simpliﬁed functional near-infrared spectroscopy system. J. Neural Eng. 3, 219–226. doi: 10.1088/1741-2560/4/3/007

Delorme, A., and Makeig, S. (2004). EEGlab: an open source toolbox for analysis of single trail EEG dynamics. J. Neurosci. Methods 134, 9–21. doi: 10.1016/j.jneumeth.2003.10.009

Fattouh, A., Horn, O., and Bourhis, G. (2013). Emotional BCI control of a smart wheelchair. Int. J. Comput. Sci. 10, 32–36.

Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Müller, K.-R., et al. (2012). Enhanced performance by a hybrid NIRS-EEG brain computer interface. Neuroimage 59, 512–529. doi: 10.1016/j.neuroimage. 2011.07.084

Galán, F., Nuttin, M., Lew, E., Ferrez, P. W., Vanacker, G., Philips, J., et al. (2008). A brain-actuated wheelchair: asynchronous and non-invasive brain-computer interfaces for continuos control of robots. Clin. Neurohysiol. 119, 2159–2169. doi: 10.1016/j.clinph.2008.06.001

Gervain, J., Mehler, J., Werker, J. F., Nelson, C. A., Csibra, G., LloydFox, S., et al. (2011). Near-infrared spectroscopy: a report from the McDonnell infant methodology consortium. Dev. Cogn. Neurosci. 1, 22–46. doi: 10.1016/j.dcn.2010.07.004

Gneo, M., Severini, G., Conforto, S., Schmid, M., and D’Alessio, T. (2011). Towards a brain-activated and eye-controlled wheel chair. Int. J. Bioeletromagn. 13, 44–45.

Homan, R. W., Herman, J., and Purdy, P. (1987). Cerebral location of international 10-20 system electrode placement. Electroencephalogr. Clin. Neurophysiol. 66, 376–382. doi: 10.1016/0013-4694(87)90206-9

- Hu, X.-S., Hong, K.-S., and Ge, S. S. (2011). Recognition of stimulus-evoked neuronal optical response by identifying chaos levels of near-infrared spectroscopy time series. Neurosci. Lett. 504, 115–120. doi: 10.1016/j.neulet. 2011.09.011
- Hu, X.-S., Hong, K.-S., and Ge, S. S. (2012). fNIRS-based online deception decoding. J. Neural Eng. 9:2. doi: 10.1088/1741-2560/9/2/026012
- Hu, X.-S., Hong, K.-S., and Ge, S. S. (2013). Reduction of trail-to-trial variability in functional near-infrared spectroscopy signals by accounting for restingstate functional connectivity. J. Biomed. Opt. 18, 1–9. doi: 10.1117/1.JBO.18. 1.017003

Hu, X.-S., Hong, K.-S., Ge, S. S., and Jeong, M.-Y. (2010). Kalman estimatorand general linear model-based on-line brain activation mapping by near-infrared spectroscopy. Biomed. Eng. Online 9:82. doi: 10.1186/1475925X-9-82

Huang, D., Qian, K., Fei, D.-Y., Jia, W., Chen, X., and Bai, O. (2012). Electroencephalography (EEG)-based brain-computer interface (BCI): a 2-D virtual wheelchair control based on event-related desynchornization/synchronization and state control. IEEE Trans. Neural Syst. Rehabil. Eng. 20, 379–388. doi: 10.1109/TNSRE.2012.2190299

Irani, F., Platek, S. M., Bunce, S., Ruocco, A. C., and Chute, D. (2007). Functional near-infrared spectroscopy (fNIRS): an emerging neuroimaging technology with important applications for the study of brain disorders. Neuropsychologist 21, 9–37. doi: 10.1080/138540406009 10018

Jochumsen, M., Niazi, I. K., Mrachacz-Kersting, N., Farina, D., and Dremstrup, K. (2013). Detection and classiﬁcation of movement-related cortical potentials associated with task forece and speed. J. Neural Eng. 10, 5, 1–9. doi: 10.1088/1741-2560/10/5/056015

Jurcak, V., Tsuzuki, D., and Dan, I. (2007). 10/20, 10/10, and 10/5 system revisited: their validity as head-surface-based positioning system. Neuroimage 34, 1600–1611. doi: 10.1016/j.neuroimage.2006.09.024

Kaiser, V., Bauernfeind, G., Kreilinger, A., Kaufmann, T., Kubler, A., Neuper, C., et al. (2014). Cortical effects of user training in a motor imagery based braincomputer interface measured by fNIRS and EEG. Neuroimage 85, 432–444. doi: 10.1016/j.neuroimage.2013.04.097

Kamran, M. A., and Hong, K.-S. (2013). Linear parameter varying model and adaptive ﬁltering technique for detecting neuronal activities: an fNIRS study. J. Neural Eng. 10:5. doi: 10.1088/1741-2560/10/5/056002

Knyazev, G. G. (2013). EEG correlates of self-referential processing. Front. Hum. Neurosci. 7:264. doi: 10.3389/fnhum.2013.00264

Li, Y. Q., Pan, J. H., Wang, F., and Yu, Z. (2013). A hybrid BCI system combining P300 and SSVEP and its application to wheel chair control. IEEE Trans. Biomed. Eng. 60, 3156–3166. doi: 10.1109/TBME.2013.2270283

Lin, J.-S., and Yang, J.-S. (2012). Wireless brian-computer interface for electric wheelcahirs with EEG and eye-blinking signals. Int. J. Innovat. Comput. Inform. Control 8, 6011–6024.

Lotte, F., Congedo, M., Lécuyer, A., Lamarche, F., and Arnaldi, B. (2007). A review of classiﬁcation algorithms for EEG-based brain-computer interfaces. J. Neural Eng. 4:2. doi: 10.1088/1741-2560/4/2/R01

Matsuyama, H., Asama, H., and Otake, M. (2009). “Design of differential nearinfrared spectroscopy based brain machine interface,” in IEEE International Symposium on Robot and Human Interactive Communication, (Toyama), 775–780. doi: 10.1109/ROMAN.2009.5326215

Matthews, F., Pearlmutter, B. A., Ward, T. E., Soraghan, C., and Markham, C.

(2008). Hemodynamics for brain computer interfaces. IEEE Signal Process. Mag. 25, 87–94. doi: 10.1109/MSP.2008.4408445

Min, B. K., Marzelli, M. J., and Yoo, S.-S. (2010). Neuroimaging-based approaches in brain-computer interface. Trends Biotechnol. 28, 552–560. doi: 10.1016/j.tibtech.2010.08.002

Nagdyman, N., Fleck, T. P. K., Ewert, P., Abdul-Khaliq, H., Redlin, M., and Lange, P. E. (2003). Cerebral oxygenation measured by near-infrared spectroscopy during circulatory arrest and cardiopulmonary resuscitation. Br. J. Anesth. 91, 438–442. doi: 10.1093/bja/aeg181

Naito, M., Michioka, Y., Ozawa, K., Ito, Y., Kiguchi, H., and Kanazaw, T. (2007). A communication means for totally locked-in ALS patients based on changes in cerebral blood volume measured with near-infrared light. IEICE Trans. Infrom. Syst. 90, 1028–1037. doi: 10.1093/ietisy/ e90-d.7.1028

Naseer, N., and Hong, K.-S. (2013). Classiﬁcation of functional near-infrared spectroscopy signals corresponding to right- and left-wrist motor imagery for development of a brain-computer interface. Neurosci. Lett. 553, 84–89. doi: 10.1016/j.neulet.2013.08.021

Naseer, N., Hong, M. J., and Hong, K.-S. (2014). Online binary decision decoding using functional near-infrared spectroscopy for the development of braincomputer interface. Exp. Brain Res. 232, 555–564. doi: 10.1007/s00221-0133764-1

Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain-computer interfaces, a review. Sensors 12, 1211–1279. doi: 10.3390/s120201211

Niedermeyer, E., and Lopes da Silva, F. H. (1999). Electroencephalography: Basic Principles, Clinical Applications and Related Fields. Philadelphia, PA: Lippincott William and Wilkins.

Ortiz-Rosario, A., and Adeli, H. (2013). Brain-computer interface technologies: from signal to action. Rev. Neurosci. 24, 537–552. doi: 10.1515/revneuro-20130032

Pfurtscheller, G., Allison, B. Z., Brunner, C., Bauernfeind, G., Solis-Escalante, T., Scherer, R., et al. (2010). The hybrid BCI. Front. Neurosci. 4:30. doi: 10.3389/fnpro.2010.00003

Pivick, R. T., Broughton, R. J., Coppola, R., Davidson, R. J., Fox, N., and Nuwer, M. R. (1993). Guidelines for recording and quantitative analysis of electroencephalographic activity in research contexts. Psychophysiology 30, 547–558. doi: 10.1111/j.1469-8986.1993.tb02081.x

Porro, C. A., Francescato, M. P., Cettolo, V., Diamond, M. E., Baraldi, P., Zuiani, C., et al. (1996). Primay motor and sensory cortex activation during motor performance and motor imagery: a functional magnetic resonance imaging study. J. Neurosci. 16, 7688–7698.

Power, S. D., Falk, T. H., and Chau, T. (2010). Classiﬁcation of prefrontal activity due to mental arithmetic and music imagery using hidden Markov models and frequency domain near-infrared spectroscopy. J. Neural Eng. 7:2. doi: 10.1088/ 1741-2560/7/2/026002

Power, S. D., Khushki, A., and Chau, T. (2012). Automatic single-trial discrimination of mental arithmetic, mental singing and no-control state form the prefrontal activity: towards the three state NIRS-BCI. BMC Res. Notes 5:141. doi: 10.1186/1756-0500-5-141

- Rehan, M., and Hong, K.-S. (2012). Robust synchronization of delayed chaotic FitzHugh-Nagumo neurons under external electrical stimulation. Comput. Math. Method Med. 2012, 1–11. doi: 10.1155/2012/ 230980
- Rehan, M., and Hong, K.-S. (2013). Modeling and automatic feedback control of tremor: adaptive estimation of deep brain stimulation. PLoS ONE 8:e62888. doi: 10.1371/journal.pone.0062888

Robinson, N., Vinod, A. P., Ang, K. K., Tee, K. P., and Guan, C. T. (2013). EEG-based classiﬁcation of fast and slow hand movements using wavelet-CSP algorithm. IEEE Trans. Biomed. Eng. 60, 2123–2132. doi: 10.1109/TBME.2013.2248153

Safaie, J., Grebe, R., Moghaddam, H. A., and Wallois, F. (2013). Towards a fully integrated wearable EEG-NIRS bimodal acquisition system. J. Neural Eng. 10:5. doi: 10.1088/1741-2560/10/5/056001

Santosa, H., Hong, M. J., Kim, S.-P., and Hong, K.-S. (2013). Noise reduction in functional near-infrared spectroscopy signals by independent component analysis. Rev. Sci. Instrum. 84:7. doi: 10.1063/1.4812785

Stangl, M., Bauernfeind, G., Kurzmann, J., Scherer, R., and Neuper, C. (2013). A heamodynamic brain-computer interface based on real-time classiﬁcation of near infrared spectroscopy signals during motor imagery and mental arithmetic. J. Near Infrared Spectrosc. 21, 157–171. doi: 10.1255/ jnirs.1048

Subasi, A., and Gursoy, M. I. (2010). EEG signal classiﬁcation using PCA, ICA, LDA and support vector machines. Expert Syst. Appl. 37, 8659–8666. doi: 10.1016/j.eswa.2010.06.065

Turnip, A., and Hong, K.-S. (2012). Classifying mental activities from EEG-P300 signals using adaptive neural network. Int. J. Innovat. Comput. Inform. Control 8, 6429–6443.

Turnip, A., Hong, K.-S., and Jeong, M.-Y. (2011). Real-time feature extraction of EEG-based P300 using adaptive nonlinear principal component analysis. Biomed. Eng. Online 10:83. doi: 10.1186/1475-925X-10-83

Verner, M., Herrmann, M. J., Troche, S. J., Robers, C. M., and Rammsyaer, T. M. (2013). Cortical oxygen consumption in mental arithmetic as a function task difﬁculty: a near-infrared spectroscopy approach. Front. Hum. Neurosci. 7:217. doi: 10.3389/fnhum.2013.00217

Vidaurre, C., and Blankertz, B. (2010). Towards a cure for BCI illiteracy. Brain Topogr. 23, 194–198. doi: 10.1007/s10548-009-0121-6

Vuckovic, A., and Sepulveda, F. (2012). A two-stage four-class BCI based on imagenary movements of the left and right wrist. Med. Eng. Phys. 34, 964–971. doi: 10.1016/j.medengphy.2011.11.001

Waldert, S., Tüshaus, L., Kaller, C. P., Aertsen, A., and Mehring, C. (2012). fNIRS exhibits weak tuning to hand movement direction. PLoS ONE 7:e49266. doi: 10.1371/journal.pone.0049266

Wolpaw, J. R., and McFarland, D. J. (2004). Control of two-dimensional movement signal by a noninvasive brain-comuter interface in humans. Proc. Natl. Acad. Sci. U.S.A. 101, 17849–17852. doi: 10.1073/pnas.0403504101

Xu, M. P., Qi, H. Z., Wan, B. K., Yin, T., Liu, Z. P., and Ming, D. (2013). A hybrid BCI speller paradigm combining P300 potential and SSVEP blocking feature. J. Neural Eng. 10:2. doi: 10.1088/1741-2560/10/2/026001

Ye, J. C., Tak, S., Jang, K. E., Jung, J., and Jang, J. (2009). NIRS-SPM: statistical parametric mapping for near-infrared spectroscopy. Neuroimage 44, 428–447. doi: 10.1016/j.neuroimage.2008.08.036

Zaepffel, M., Trachel, R., Kilavik, B. E., and Brochier, T. (2013). Modulation of EEG beta power during planning and execution of grasping movements. PLoS ONE 8:e60060. doi: 10.1371/journal.pone.0060060

Zhang, R., Xu, P., Guo, L., Zhang, Y., Li, P., and Yao, D. (2013). Z-score linear discriminant analysis for EEG based brain-computer interfaces. PLoS ONE 8:e74433. doi: 10.1371/journal.pone.0074433

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 13 November 2013; accepted: 03 April 2014; published online: 28 April 2014. Citation: Khan MJ, Hong MJ and Hong K-S (2014) Decoding of four movement directions using hybrid NIRS-EEG brain-computer interface. Front. Hum. Neurosci. 8:244. doi: 10.3389/fnhum.2014.00244 This article was submitted to the journal Frontiers in Human Neuroscience. Copyright © 2014 Khan, Hong and Hong. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

