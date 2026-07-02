ORIGINAL RESEARCH published: 23 February 2018 doi: 10.3389/fninf.2018.00005

# A Ternary Hybrid EEG-NIRS Brain-Computer Interface for the Classiﬁcation of Brain Activation Patterns during Mental Arithmetic, Motor Imagery, and Idle State

Jaeyoung Shin, Jinuk Kwon and Chang-Hwan Im*

Department of Biomedical Engineering, Hanyang University, Seoul, South Korea

The performance of a brain-computer interface (BCI) can be enhanced by simultaneously using two or more modalities to record brain activity, which is generally referred to as a hybrid BCI. To date, many BCI researchers have tried to implement a hybrid BCI system by combining electroencephalography (EEG) and functional near-infrared spectroscopy (NIRS) to improve the overall accuracy of binary classiﬁcation. However, since hybrid EEG-NIRS BCI, which will be denoted by hBCI in this paper, has not been applied to ternary classiﬁcation problems, paradigms and classiﬁcation strategies appropriate for ternary classiﬁcation using hBCI are not well investigated. Here we propose the use of an hBCI for the classiﬁcation of three brain activation patterns elicited by mental arithmetic, motor imagery, and idle state, with the aim to elevate the information transfer rate (ITR) of hBCI by increasing the number of classes while minimizing the loss of accuracy. EEG electrodes were placed over the prefrontal cortex and the central cortex, and NIRS optodes were placed only on the forehead. The ternary classiﬁcation problem was decomposed into three binary classiﬁcation problems using the “one-versus-one” (OVO) classiﬁcation strategy to apply the ﬁlter-bank common spatial patterns ﬁlter to EEG data. A 10 × 10-fold cross validation was performed using shrinkage linear discriminant analysis (sLDA) to evaluate the average classiﬁcation accuracies for EEG-BCI, NIRS-BCI, and hBCI when the meta-classiﬁcation method was adopted to enhance classiﬁcation accuracy. The ternary classiﬁcation accuracies for EEG-BCI, NIRS-BCI, and hBCI were 76.1 ± 12.8, 64.1 ± 9.7, and 82.2 ± 10.2%, respectively. The classiﬁcation accuracy of the proposed hBCI was thus signiﬁcantly higher than those of the other BCIs (p < 0.005). The average ITR for the proposed hBCI was calculated to be 4.70 ± 1.92 bits/minute, which was 34.3% higher than that reported for a previous binary hBCI study.

Edited by: Sung Chan Jun, Gwangju Institute of Science and Technology, South Korea

Reviewed by:

Dan Zhang, Tsinghua University, China

Yingchun Zhang, University of Houston, United States

*Correspondence:

Chang-Hwan Im ich@hanyang.ac.kr

Received: 28 July 2017 Accepted: 26 January 2018 Published: 23 February 2018

Citation: Shin J, Kwon J and Im C-H (2018) A

Ternary Hybrid EEG-NIRS Brain-Computer Interface for the

Classiﬁcation of Brain Activation Patterns during Mental Arithmetic,

Motor Imagery, and Idle State. Front. Neuroinform. 12:5. doi: 10.3389/fninf.2018.00005

Keywords: brain-computer interface, mental arithmetic, motor imagery, electroencephalography (EEG), near infrared spectroscopy (NIRS), pattern recognition

## INTRODUCTION

Brain-computer interfaces (BCIs) have recently attracted great attention as they have shown great potential as new modes of communication for individuals who have lost the ability for voluntary movements (Wolpaw et al., 2002; Allison et al., 2007; van Erp et al., 2012; Wolpaw and Wolpaw, 2012; Blankertz et al., 2016). BCIs can be implemented using a variety of neural signal recording methods, such as electroencephalography (EEG), magnetoencephalography, functional magnetic resonance imaging, near-infrared spectroscopy (NIRS), electrocorticography, and multiunit neural recording (Wolpaw et al., 2002). Since each brain-imaging modality has its own pros and cons, combining two or more neural signal recording modalities, which is generally referred to as hybrid BCI, might enhance the overall performance of BCI (Pfurtscheller et al., 2010a; Dähne et al., 2015; Fazli et al., 2015). Until now, a number of hybrid BCI studies have demonstrated the eﬀectiveness of the combinatory use of diﬀerent modalities or paradigms, e.g., combined use of P300 and steady-state visually evoked potential for EEG-BCI (Wang et al., 2015), hybrid EEG-electrooculogram (EOG) BCI (Wang et al., 2014), and hybrid EEG-NIRS BCI (hereafter denoted by hBCI) (Naseer and Hong, 2015).

Among the diﬀerent methods, hBCI has been actively studied because both modalities can be readily made portable and there is no signiﬁcant interference between the two signals. EEG records electrophysiological signal and NIRS measures hemodynamic variations in the brain. Since the origins of the two signals diﬀer from each other, the amount of available information that can be used for BCI is increased, which in turn leads to enhanced BCI performance. More importantly, the two modalities are complementary to each other in that EEG has superior temporal resolution to NIRS, but is more prone to contamination from EOG and electromyogram artifacts than NIRS. Indeed, recent studies reported successful application of NIRS-BCI for the communication of patients in completely locked-in state (CLIS) (Chaudhary et al., 2017); however, EEG-BCI has never been successful for the patients in CLIS (De Massari et al., 2013; Chaudhary et al., 2017). Therefore, the appropriate combination of these two modalities has the potential to enhance the overall BCI performance and it has been already veriﬁed in many previous studies (Fazli et al., 2012; Koo et al., 2015; Yin et al., 2015; Shin et al., 2016, 2017b). The recent release of an openaccess dataset for hBCI reﬂects the increasing attention that this type of hBCI has garnered (Shin et al., 2017a).

The easiest way to increase the information transfer rate (ITR) of a BCI system is to increase the number of classes, while minimizing the loss of accuracy, because ITR is determined by both classiﬁcation accuracy and the number of available commands; however, most hBCI studies have focused only on enhancing the classiﬁcation performance of binary BCI. Until now, hBCI has been studied to improve the classiﬁcation performance of binary BCI (Shin et al., 2017b) or to simply increase the number of available commands (Khan et al., 2014; Khan and Hong, 2017). Khan et al. (2014, 2015) recorded EEG and NIRS simultaneously but they used the two types of data independently. Here we propose the use of a multi-class hBCI

that classiﬁes three brain activation patterns recorded during motor imagery (MI), mental arithmetic (MA), and idle state (IS: staying relaxed without performing any cognitive task). MI has been the most widely used mental task for EEG-BCI, while MA has been frequently used as a popular BCI task for NIRS-BCI (Power et al., 2011, 2012a,b). Brain activation elicited by MI can be measured mainly around the central area, while that elicited by MA can be measured primarily in the forehead covering the prefrontal cortex (PFC). Therefore, we hypothesized that ternary classiﬁcation (MA vs. MI. vs. IS) would be suitable for implementation of ternary hBCI. In contrast to EEG, which can record brain activity from both the frontal and central areas relatively easily, NIRS sometimes has diﬃculty in measuring signals around the central areas due to the attenuation of light intensity by hair, without applying a time-consuming hair preparation process or using specially designed brush type optodes (Khan et al., 2012). In this study, we implement an hBCI using EEG signals recorded at both the frontal and central areas and NIRS signals recorded only from the frontal area to improve the practicality and usability of the system by avoiding time-consuming (hair) preparatory work. The performance of our hBCI was validated using experiments with 18 healthy participants.

MATERIALS AND METHODS Participants

Eighteen healthy participants (10men and 8 women, 23.8 ± 2.5 years of age) voluntarily participated in this study. None of the participants reported a history of neurological, psychiatric, or other severe diseases that might have inﬂuenced the experimental results. The experimental procedure was fully explained to each participant before the experiment. The participants signed written consent forms before the experiment. After the experiment, monetary reimbursement was provided. The experiment was conducted with approval from the Institutional Review Board committee of Hanyang University and according to the Declaration of Helsinki.

Apparatus

Figure 1 shows the placement of the EEG electrodes and NIRS optodes. EEG data were recorded at a sampling rate of 2,048Hz using an Active-Two ampliﬁer (Biosemi; Amsterdam, the Netherlands) with 21 active electrodes placed on both frontal [5 unlabeled (non-standard), Fz, F1, F2, F3, and F4] and central (FC3, FC4, Cz, C1, C2, C3, C4, C5, C6, CP3, and CP4) areas. The reference and ground electrodes were attached at the left and right mastoids, respectively. Two additional electrodes were located above and below the left eye to measure the vertical EOG. NIRS data were collected using a portable NIRS system (LIGHTNIRS; Shimadzu Corp.; Kyoto, Japan) at a sampling rate of 13.3Hz. Six sources and six detectors were placed on the forehead over the PFC. There were 16 NIRS channels in total. Each of these channels consisted of a source and detector pair placed 30mm away from each other. To synchronize the two signals, trigger signals were delivered to both the EEG and NIRS

|[Figure 1]<br><br>FIGURE 1 | Placement of EEG electrodes (blue) and NIRS optodes (red: sources, green: detectors) on frontal (Left) and central (Right) areas.|
|---|

systems simultaneously using StimTracker (Cedrus Corp.; San Pedro, USA).

Experimental Paradigm

The participants were seated on a comfortable chair 70cm away from a 26-inch liquid crystal display monitor and followed instructions appearing on the monitor. Figure 2 shows the experimental paradigm. A single trial was composed of instruction (−2 to 0s), task (0–10s), and inter-trial break (10 to 26–28s) periods. In the introduction period, a right-hand MI, MA, or IS was randomly selected. For the right-hand MI, a right arrow was presented, and for the MA, “a three-digit number minus a one-digit number (between 6 and 9)” was randomly provided. For IS, a ﬁxation cross was displayed at the center of the monitor. In the task period, the participants performed the designated task. For the right-hand MI, the participants imagined complex ﬁnger tapping (tapping the second, third, fourth, ﬁfth, fourth, third, second, etc. ﬁngers to the thumb) at a rate of approximately 2Hz. For MA, the participants were instructed to continuously subtract a one-digit number (between 6 and 9) from the result of a former calculation as fast as possible (e.g., 789–7 = 782, 782–7 = 775, 775–7 = 768). For IS, the participants stayed relaxed without performing any speciﬁc mental imagery task. The participants performed the three types of tasks 30 times each (90 times in total). Note that a number of NIRS-BCI and hBCI studies have adopted IS as one of the main BCI tasks (Power et al., 2011; Schudlo et al., 2013; Schudlo and Chau, 2015). Before the experiment, all participants were pre-trained to produce appropriate MIrelated brain activation patterns with the aid of a visual feedback system. For the visual-feedback-based MI training, three EEG electrodes (Cz, C3, and C4) were selected to monitor the motorrelated EEG signal changes. At ﬁrst, task-related event-related synchronization/desynchronization (ERS/ERD) changes at the three electrodes were displayed on the monitor as simple bar graphs, which were updated in real-time while participants performed actual ﬁnger tapping. Once the participants got used to the task, they performed kinesthetic MI, not visual

|[Figure 2]<br><br>FIGURE 2 | Timing sequence of a single trial. A random task was assigned to the participant in the Introduction section (−2 to 0s). After the presentation of a short beep, the participants continued performing the assigned task while looking at a ﬁxation cross during the task period (0–10s). The participants stopped performing the task after a second short beep was presented and a “STOP” sign was displayed on the screen for 2s. During the random-length inter-trial break period (12 to 26–28s), the participants relaxed without any particular thoughts.|
|---|

MI (Neuper et al., 2005), to make ERS/ERD patterns similar to those generated during actual ﬁnger tapping. If they could reproduce consistent task-related ERS/ERD patterns, data recording commenced. The eﬀectiveness of the MI training (MI proﬁciency) was evaluated based on the elapsed training time (good: < 5min, normal: < 20min, poor: < 30min). The total training time was limited to at most 30min considering participants’ attentional deterioration and fatigue, but most participants of this study ﬁnished the MI training session within 20min (normal MI proﬁciency).

Preprocessing

All data processing was performed using MATLAB, 2013b (MathWorks; Natick, MA). Functions implemented in EEGLAB (https://sccn.ucsd.edu/eeglab/index.php) and BBCI1 toolbox (https://github.com/bbci/bbci_public) were used for EEG and NIRS data processing and classiﬁcation (Delorme and Makeig, 2004; Blankertz et al., 2016). EEG data were downsampled to 200Hz to reduce the computational complexity and band-pass

1BBCI toolbox [Online]. Available: https://github.com/bbci/bbci_public/

ﬁltered with a passband of 0.1–50Hz to remove direct current drift and 60Hz alternating current noise. The vertical EOG was eliminated using an automatic ocular artifact rejection method based on a blind source separation algorithm (Gomez-Herrero et al., 2006). For NIRS, the detected optical densities (ODs) were converted to hemodynamic variations (concentration change in reduced hemoglobin HbR and concentration change in oxidized hemoglobin HbO) using the following formula (Matcher et al., 1995):

HbR HbO

=

1.8545 −0.2394 −1.0947 −1.4887 0.5970 1.4847

 

 (mM · cm)

OD780 OD805 OD830

In the equation above, OD is the change in the detected OD at the wavelength provided in the subscript (780, 805, or 830nm). The converted HbR and HbO values were band-pass ﬁltered (6th-order Butterworth zero-phase ﬁlter) with a passband of

- 0.01–0.09Hz to remove physiological noise.

Classiﬁcation

Figure 3 shows the procedure used for data processing and classiﬁcation. EEG data were segmented into epochs from −5 to 25s. To apply the ﬁlter-bank common spatial pattern (FBCSP) ﬁlter, EEG data in the time period 0–10s (i.e., task period) were selected and a ﬁlter bank (6th-order zero-phase Butterworth) with multiple passbands for the θ (4–8Hz), α (8–13Hz), and β (13–30Hz) bands was applied to the selected EEG data. EEG epochs were partitioned into training and test sets. The ternary classiﬁcation problem was decomposed into three binary classiﬁcation problems (i.e., MA vs. MI, MA vs. IS, and MI vs. IS) in order to apply the “one-versus-one” (OVO) classiﬁcation strategy (Müller-Gerking et al., 1999; Dornhege et al., 2004), in which the classiﬁcation was performed for all possible binary combinations of classes and the ﬁnal estimate was decided by majority voting (Lei et al., 2009). EEG feature vectors {dimension: 18 × 60 [(number of CSP components × number of passbands) × number of trials]} were constructed using the log-variance of the ﬁrst three and last three CSP components selected using the typical eigenvalue score (Blankertz et al., 2008) after FBCSP ﬁltering.

NIRS data were segmented into epochs from −5 to 25s. Baseline correction was performed by subtracting the temporal mean value between −1 and 0s from each NIRS epoch. NIRS feature vectors {dimension: 64 × 60 [(number of channels × number of NIRS chromophores × number of temporal windows) × number of trials]} were constructed using the temporal mean values of HbR and HbO in the 5–10 and 10–15s temporal windows in NIRS epochs from all channels, considering the inherent hemodynamic delay. Note that we also tried other feature candidates such as slope and variance but the use of features other than the temporal mean values did not improve the classiﬁcation performance. In addition, the two separated intervals (5–10 and 10–15s) yielded higher classiﬁcation accuracy than a single interval (5–15s). In the same

|[Figure 3]<br><br>FIGURE 3 | Data processing ﬂow. EEG and NIRS data were separately processed at the unimodal stage and were combined at the hybrid stage. OVO, FBCSP, and sLDA indicate “one-versus-one” strategy, ﬁlter-bank common spatial pattern, and shrinkage linear discriminant analysis, respectively. After OVO, the ternary classiﬁcation problem was decomposed into three binary classiﬁcation problems.|
|---|

manner as that described for EEG data above, NIRS epochs were partitioned to training and test sets, and the OVO classiﬁcation strategy was applied. We adopted the OVO approach because the OVO strategy makes CSP, known to yield high performance in ERS/ERD-based BCI, be applied to the present ternary classiﬁcation problem.

A 10 × 10-fold cross-validation was performed using shrinkage linear discriminant analysis (sLDA) for each of the three binary classiﬁcation problems. The sLDA can be used to eﬀectively mitigate the negative eﬀect (degradation of classiﬁcation accuracy) resulting from the use of highdimensional feature vectors when compared to the number of trials by replacing the empirical covariance matrix with (1 − λ) + λI, where λ and I are the regularization parameter and identity matrix, respectively (Friedman, 1989; Shin et al., 2016, 2017a,b). The optimal λ was estimated based on the literature (Ledoit and Wolf, 2004; Schäfer and Strimmer, 2005). sLDA classiﬁers were trained by EEG and NIRS data separately for three binary classiﬁcation problems each, and the outputs of EEG and NIRS classiﬁers were then combined to construct new feature vectors for the meta-classiﬁer (Fazli et al., 2012). The ﬁnal class was then estimated using majority voting for the results of the three binary classiﬁcation problems.

## RESULTS

Figure 4 shows the results of the time-frequency analysis, which is used to assess task-related EEG spectral power changes over the frontal and central areas relative to the baseline value, which is the average spectral power between −4 and −3s. Red and blue colors indicate increases and decreases in EEG spectral power, respectively. The spectral power changes were averaged over the frontal and central channels separately. A red dotted vertical line in each graph indicates the task onset time (0s). For MA, power decreases in the δ- (1–4Hz) and low α-bands (8–10Hz) were observed over frontal and central areas during the task period. Power increases in the high α-band (10–13Hz) were commonly seen in the early stages of the task period (0–5s). Power decrease

|[Figure 4]<br><br>FIGURE 4 | Time-frequency analysis results for MA, MI, and IS on frontal and central areas (unit: dB). Red dashed lines represent the task onset. A color bar indicates the range of the EEG spectral power variation in dB. Red (positive) and blue (negative) indicate, respectively, spectral power increases and decreases relative to the baseline value (average spectral power between −4 and −3s).|
|---|

in the high β-band (20–30Hz) appeared more distinctly in the frontal area than in the central area. For MI, prominent power decreases in the δ- and θ-bands were observed over both frontal and central areas during the task period. Similar spectral power changes in the frontal area during MI was observed in previous studies (Yamawaki et al., 2006; Ahn et al., 2013). In addition, a power decrease in the high α-band was observed in the central area. For IS, no distinct power change was observed during the task period, except for a weak power increase around 10Hz, which might have been due to the relaxation of the participants (Lagopoulos et al., 2009). Regardless of the task type, power increases commonly appeared throughout the frontal and central areas after the end of the task period. The power increase in the δ-band might be the remaining (not completely eliminated by ICA) EOG components due to eye blinking right after the task period. Note that this δ-band power increase did not aﬀect the BCI performance because frequency bands higher than θ-band were used for the BCI classiﬁcation. The ERS in the α frequency band seems to be the post-stimulus ERS frequently observed after performing a given task (Pfurtscheller et al., 2006; Solis-Escalante et al., 2010; Shin et al., 2017b).

Figure 5 shows the grand average of hemodynamic variations due to MA and MI over time. The left and right panels represent data for HbR and HbO, respectively. Channels (Chs.) 3 and 14 are located in the middle of the forehead. For MA, the decrease in HbR appeared at center-right channels (Chs. 7, 8, and 13) 5s after task onset. After 10s, an increase in HbR was observed at the center-left-lower (Chs. 14 and 15) and rightmost (Ch. 6) channels. At 15s, the amount of increase in HbR was reduced. For MI, minor variations in HbR were observed until 5s after task onset. After 10s, an increase in HbR was observed in the

left lower channel (Ch. 15), but the variation was not prominent when compared to that observed for MA. At 15s, the amount of increase in HbR was reduced. For both MA and MI, the trend of HbO variation was opposite to that observed for HbR, and the variation of HbO was greater than that of HbR. After 10s, a sudden drop of HbO was observed on the left-middle area (chs. 9, 14, 15), which might seem unusual; however, note that some previous studies also reported similar phenomena during mental arithmetic task (Pfurtscheller et al., 2010b; Shin et al., 2017a). The grand averaged HbR and HbO waveforms at three diﬀerent task conditions can be found at https://doi.org/10.6084/m9.ﬁgshare. 5844813.v1.

Figure 6 shows the individual ternary classiﬁcation accuracies for EEG-BCI, NIRS-BCI, and hBCI (denoted by HYB in Figure 6). A red dotted horizontal line denotes the theoretical chance level (1/3 = 0.333). As shown in the graph, we were able to use the “HYB” to obtain the best classiﬁcation accuracies for 14 out of the 18 participants. The average classiﬁcation accuracies for EEG, NIRS, and “HYB” were 76.1 ± 12.7, 64.1 ± 9.7, and 82.2 ± 10.2% (mean ± standard deviation), respectively. The average classiﬁcation accuracy of hBCI was statistically signiﬁcantly higher than those of EEG-BCI and NIRS-BCI (Friedman test: p < 0.001; post-hoc: Wilcoxon signed rank sum test with Bonferroni correction; EEG vs. HYB: corrected p = 0.0046 and NIRS vs. HYB: corrected p = 0.0002).

## DISCUSSION

The results of our study show, for the ﬁrst time, the feasibility of the combined use of EEG and NIRS to enhance the performance of ternary BCI classiﬁcation. The proposed ternary hBCI was

|[Figure 5]<br><br>FIGURE 5 | Grand average of hemodynamic variation in response to MA (Top), MI (Middle), and IS (Bottom) over time. The left and right panels present data for HbR and HbO, respectively. The color bars below the ﬁgures indicate the range of the concentrations of HbR (left 3 panels) and HbO (right 3 panels) in mM·cm. Note that the ranges of the concentrations are different.|
|---|

used to classify MA-, MI-, and IS-related brain activation patterns successfully with higher classiﬁcation accuracy than EEG-BCI and NIRS-BCI. The MA-related brain activation and the MIrelated activation are mainly produced in diﬀerent brain regions, and thereby NIRS optodes and EEG electrodes were arranged on the forehead over the PFC to record MA-related brain activation, while additional EEG electrodes were placed on the central area to record MI-related brain activation. It is noteworthy that the ternary classiﬁcation accuracy was even higher than the threshold for eﬀective binary BCI (>70% classiﬁcation accuracy) (Blankertz et al., 2009; Vidaurre and Blankertz, 2010).

The implementation of a multi-class NIRS-BCI is challenging. No previous study has successfully implemented a multi-class NIRS-BCI using only hemodynamic variations recorded from the PFC. The accuracy of our ternary classiﬁcation using NIRS supports this argument. Although the average ternary NIRS

classiﬁcation accuracy exceeded the theoretical chance level (33.3%), a practically usable level was unreachable. To implement ternary NIRS-BCI, Hong et al. (2015) and Schudlo and Chau (2015) placed more NIRS optodes on central areas and the parietal cortex, respectively, in addition to the PFC. However, time-consuming preparation is generally inevitable to acquire high-quality signals if optodes are attached onto hairy scalp areas. On the other hand, although EEG-BCI resulted in a fairly high classiﬁcation accuracy exceeding 70%, the classiﬁcation accuracies for 9 out of the 18 participants were further improved by more than 5% using the hybrid approach.

Successful implementation of a multi-class hBCI is beneﬁcial for improving the ITR given by 60/τ · [log2N + plog2(p) + (1 − p)log2((1 − p)/(N − 1))] where τ, N, p and are trial length, the number of classes, and classiﬁcation accuracy, respectively (Dornhege et al., 2007). According to a previous study (Hong

|[Figure 6]<br><br>FIGURE 6 | Individuation classiﬁcation accuracy of EEG (blue), NIRS (red), and HYB (green), and the average for all participants. The horizontal dashed line indicates the theoretical chance level (33.3%). Errorbars indicate the standard deviation. ***p < 0.005.|
|---|

et al., 2015), an average ITR of 3.29 ± 0.72 bits/min could be achieved using the ternary NIRS-BCI. The average ITR of 3.50 ± 1.23 bits/min was achieved using the binary hBCI based on MA (Shin et al., 2017a). We achieved an average ITR of 4.70 ±

- 1.92 bits/min, which reﬂects 42.9 and 34.3% improvements in ITR when compared to a ternary NIRS-BCI (Hong et al., 2015) and a binary hBCI (Shin et al., 2017a), respectively. Multi-class classiﬁcation may generally degrade classiﬁcation accuracy when compared to binary classiﬁcation, although it can increase the number of available commands. In this study, we demonstrated that hBCI can mitigate the degradation of classiﬁcation accuracy, thereby further improving the ITR. Although it might be thought that some EEG-BCI paradigms such as steady-state visual evoked potential (SSVEP)-BCI and P300 BCI can provide higher ITR (Ming et al., 2002; Hwang et al., 2012), they rely on exogenous paradigms requiring external visual stimulus (Faller et al., 2010). Therefore, they cannot be used for patients with oculomotor impairment or those in CLIS.

We selected MI and MA as two mental tasks producing distinct response, as they have been widely used in previous EEGBCI or NIRS-BCI studies (Zhang et al., 2017; Dutta et al., 2018). However, in previous BCI studies, many other types of mental tasks (e.g., word association, mental singing, three-dimensional object rotation, mental navigation, and face imagery) were considered in order to ﬁnd an optimal combination of BCI tasks (Friedrich et al., 2012; Hwang et al., 2014; Banville et al., 2017). It is expected that larger ITRs would be achieved if the optimal task combination and the optimal task length are established.

The main drawback of the current hBCI is the high complexity of the system, which might make it diﬃcult to apply in practical

BCI applications. To reduce the system complexity, we attached EEG electrodes only around frontal and central areas based on a previous hBCI study that used the same mental tasks as the present study (Shin et al., 2017a). Therefore, it is necessary to minimize the system complexity using an optimal channel selection method and by manufacturing a uniﬁed EEG-NIRS recording system. No commercial hybrid recording system able to collect EEG and NIRS data simultaneously in a single unit is available (von Lühmann et al., 2017). Overcoming this drawback would enable advancements in hBCI research in the future.

## AUTHOR CONTRIBUTIONS

This study was designed by JS and C-HI. The preliminary and main experiments and data analyses were conducted by JS and JK. The manuscript was written by JS and C-HI. All of the authors have reviewed and approved the ﬁnal manuscript.

## FUNDING

This work was supported in part by the Institute for Information & communications Technology Promotion (IITP) grant funded by the Korea government (MSIT) (2017-0-00432, Development of non-invasive integrated BCI SW platform to control home appliances and external devices by user’s thought via AR/VR interface), in part by the Brain Research Program through the National Research Foundation of Korea (NRF) funded by the Ministry of Science and ICT (NRF-2015M3C7A1031969), and in part Basic Science Research Program through NRF funded by the Ministry of Education (No. 2017R1A6A3A01003543).

## REFERENCES

Ahn, M., Cho, H., Ahn, S., and Jun, S. C. (2013). High theta and low alpha powers may be indicative of BCI-illiteracy in motor imagery. PLoS ONE 8:e80886. doi: 10.1371/journal.pone.0080886

Allison, B. Z., Wolpaw, E. W., and Wolpaw, J. R. (2007). Brain-computer interface systems: progress and prospects. Expert Rev. Med. Devices 4, 463–474. doi: 10.1586/17434440.4.4.463

Banville, H., Gupta, R., and Falk, T. H. (2017). Mental task evaluation for hybrid NIRS-EEG brain-computer interfaces. Comput. Intell. Neurosci. 2017:3524208. doi: 10.1155/2017/3524208

Blankertz, B., Acqualagna, L., Dähne, S., Haufe, S., Kraft, M. S., Sturm, I., et al.

(2016). The Berlin brain-computer interface: progress beyond communication and control. Front. Neurosci. 10:530. doi: 10.3389/fnins.2016.00530

Blankertz, B., Sanelli, C., Halder, S., Hammer, E., Kübler, A., Müller, K.-R., et al.

(2009). Predicting BCI performance to study BCI illiteracy. BMC Neurosci. 10(Suppl. 1):P84. doi: 10.1186/1471-2202-10-S1-P84

Blankertz, B., Tomioka, R., Lemm, S., Kawanabe, M., and Müller, K.-R. (2008). Optimizing spatial ﬁlters for robust EEG single-trial analysis. IEEE Signal Process. Mag. 25, 41–56. doi: 10.1109/MSP.2008.4408441

Chaudhary, U., Xia, B., Silvoni, S., Cohen, L. G., and Birbaumer, N. (2017). Brain– computer interface–based communication in the completely locked-in state. PLoS Biol. 15:e1002593. doi: 10.1371/journal.pbio.1002593

Dähne, S., Bießmann, F., Samek, W., Haufe, S., Goltz, D., Gundlach, C., et al. (2015). Multivariate machine learning methods for fusing multimodal functional neuroimaging data. Proc. IEEE 103, 1507–1530. doi: 10.1109/JPROC.2015.2425807

Delorme, A., and Makeig, S. (2004). EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. J. Neurosci. Meth. 134, 9–21. doi: 10.1016/j.jneumeth.2003.10.009

De Massari, D., Ruf, C. A., Furdea, A., Matuz, T., van der Heiden, L., Halder, S., et al. (2013). Brain communication in the locked-in state. Brain 136(Pt 6), 1989–2000. doi: 10.1093/brain/awt102

Dornhege, G., Blankertz, B., Curio, G., and Muller, K. R. (2004). Boosting bit rates in noninvasive EEG single-trial classiﬁcations by feature combination and multiclass paradigms. IEEE Trans. Biomed. Eng. 51, 993–1002. doi: 10.1109/TBME.2004.827088

Dornhege, G., Millán, J. R., Hinterberger, T., McFarland, D., and Müller, K.-R.

(2007). Toward Brain-Computer Interfacing. Cambridge, MA: MIT Press.

Dutta, S., Singh, M., and Kumar, A. (2018). Classiﬁcation of non-motor cognitive task in EEG based brain-computer interface using phase space features in multivariate empirical mode decomposition domain. Biomed. Signal Process. Control 39, 378–389. doi: 10.1016/j.bspc.2017.08.004

Faller, J., Muller-Putz, G., Schmalstieg, D., and Pfurtscheller, G. (2010). An application framework for controlling an avatar in a desktop-based virtual environment via a software SSVEP brain-computer interface. Presence Teleop. Virt. 19, 25–34. doi: 10.1162/pres.19.1.25

Fazli, S., Dähne, S., Samek, W., Bießmann, F., and Müller, K.-R. (2015). Learning from more than one data source: data fusion techniques for sensorimotor rhythm-based brain–computer interfaces. Proc. IEEE 103, 891–906. doi: 10.1109/JPROC.2015.2413993

Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Müller, K.-R., et al. (2012). Enhanced performance by a hybrid NIRS-EEG brain computer interface. Neuroimage 59, 519–529. doi: 10.1016/j.neuroimage.2011.07.084 Friedman, J. H. (1989). Regularized discriminant analysis. J. Am. Stat. Assoc. 84,

165–175. doi: 10.1080/01621459.1989.10478752

Friedrich, E. V. C., Scherer, R., and Neuper, C. (2012). The eﬀect of distinct mental strategies on classiﬁcation performance for brain-computer interfaces. Int. J. Psychophysiol. 84, 86–94. doi: 10.1016/j.ijpsycho.2012.01.014

Gomez-Herrero, G., De Clercq, W., Anwar, H., Kara, O., Egiazarian, K., Van Huﬀel, S., et al. (2006). “Automatic removal of ocular artifacts in the EEG without an EOG reference channel,” in 7th Nordic Signal Processing Symposium (NORSIG) (Reykjavik), 130–133.

Hong, K.-S., Naseer, N., and Kim, Y. H. (2015). Classiﬁcation of prefrontal and motor cortex signals for three-class fNIRS-BCI. Neurosci. Lett. 587, 87–92. doi: 10.1016/j.neulet.2014.12.029

Hwang, H.-J., Lim, J.-H., Jung, Y.-J., Choi, H., Lee, S. W., and Im, C.-H. (2012). Development of an SSVEP-based BCI spelling system

adopting a QWERTY-style LED keyboard. J. Neurosci. Meth. 208, 59–65. doi: 10.1016/j.jneumeth.2012.04.011

Hwang, H.-J., Lim, J.-H., Kim, D.-W., and Im, C.-H. (2014). Evaluation of various mental task combinations for near-infrared spectroscopy-based braincomputer interfaces. J. Biomed. Opt. 19:077005. doi: 10.1117/1.JBO.19.7.077005

Khan, B., Wildey, C., Francis, R., Tian, F. H., Delgado, M. R., Liu, H. L., et al. (2012). Improving optical contact for functional near-infrared brain spectroscopy and imaging with brush optodes. Biomed. Opt. Express 3, 878–898. doi: 10.1364/BOE.3.000878

Khan, M. J., and Hong, K.-S. (2017). Hybrid EEG–fNIRS-based eight-command decoding for BCI: application to quadcopter control. Front. Neurorobot. 11:6. doi: 10.3389/fnbot.2017.00006

Khan, M. J., Hong, M. J., and Hong, K.-S. (2014). Decoding of four movement directions using hybrid NIRS-EEG brain-computer interface. Front. Hum. Neurosci. 8:244. doi: 10.3389/fnhum.2014.00244

Khan, M. J., Hong, K. S., Naseer, N., and Bhutta, M. R. (2015). “Hybrid EEGNIRS based BCI for quadcopter control,” in 2015 54th Annual Conference of the Society of Instrument and Control Engineers of Japan (SICE) (Hangzhou), 1177–1182.

Koo, B., Lee, H.-G., Nam, Y., Kang, H., Koh, C. S., Shin, H.-C., et al. (2015). A hybrid NIRS-EEG system for self-paced brain computer interface with online motor imagery. J. Neurosci. Meth. 244, 26–32. doi: 10.1016/j.jneumeth.2014.04.016

Lagopoulos, J., Xu, J., Rasmussen, I., Vik, A., Malhi, G. S., Eliassen, C. F., et al.

(2009). Increased theta and alpha EEG activity during nondirective meditation. J. Altern. Complement. Med. 15, 1187–1192. doi: 10.1089/acm.2009.0113

Ledoit, O., and Wolf, M. (2004). A well-conditioned estimator for largedimensional covariance matrices. J. Multivar. Anal. 88, 365–411. doi: 10.1016/S0047-259X(03)00096-4

Lei, X., Yang, P., and Yao, D. Z. (2009). An empirical Bayesian framework for brain-computer interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 17, 521–529. doi: 10.1109/TNSRE.2009.2027705

Matcher, S. J., Elwell, C. E., Cooper, C. E., Cope, M., and Delpy, D. T. (1995). Performance comparison of several published tissue near-infrared spectroscopy algorithms. Anal. Biochem. 227, 54–68. doi: 10.1006/abio.1995.1252

Ming, C., Xiaorong, G., Shangkai, G., and Dingfeng, X. (2002). Design and implementation of a brain-computer interface with high transfer rates. IEEE Trans. Biomed. Eng. 49, 1181–1186. doi: 10.1109/TBME.2002.803536

Müller-Gerking, J., Pfurtscheller, G., and Flyvbjerg, H. (1999). Designing optimal spatial ﬁlters for single-trial EEG classiﬁcation in a movement task. Clin. Neurophysiol. 110, 787–798. doi: 10.1016/S1388-2457(98)00038-8

Naseer, N., and Hong, K.-S. (2015). fNIRS-based brain-computer interfaces: a review. Front. Hum. Neurosci. 9:3. doi: 10.3389/fnhum.2015.00003

Neuper, C., Scherer, R., Reiner, M., and Pfurtscheller, G. (2005). Imagery of motor actions: diﬀerential eﬀects of kinesthetic and visual-motor mode of imagery in single-trial EEG. Brain Res. Cogn. Brain Res. 25, 668–677. doi: 10.1016/j.cogbrainres.2005.08.014

Pfurtscheller, G., Allison, B. Z., Brunner, C., Bauernfeind, G., Solis-Escalante, T., Scherer, R., et al. (2010a). The hybrid BCI. Front. Neurosci. 4:42. doi: 10.3389/fnpro.2010.00003

Pfurtscheller, G., Bauernfeind, G., Wriessnegger, S. C., and Neuper, C. (2010b). Focal frontal (de)oxyhemoglobin responses during simple arithmetic. Int. J. Psychophysiol. 76, 186–192. doi: 10.1016/j.ijpsycho.2010.03.013

Pfurtscheller, G., Brunner, C., Schlögl, A., and Lopes da Silva, F. H. (2006). Mu rhythm (de)synchronization and EEG single-trial classiﬁcation of diﬀerent motor imagery tasks. Neuroimage 31, 153–159. doi: 10.1016/j.neuroimage.2005.12.003

- Power, S. D., Kushki, A., and Chau, T. (2011). Towards a system-paced nearinfrared spectroscopy brain–computer interface: diﬀerentiating prefrontal activity due to mental arithmetic and mental singing from the no-control state. J. Neural Eng. 8:066004. doi: 10.1088/1741-2560/8/6/066004
- Power, S. D., Kushki, A., and Chau, T. (2012a). Automatic single-trial discrimination of mental arithmetic, mental singing and the no-control state from prefrontal activity: toward a three-state NIRS-BCI. BMC Res. Notes 5:141. doi: 10.1186/1756-0500-5-141

Power, S. D., Kushki, A., and Chau, T. (2012b). Intersession consistency of singletrial classiﬁcation of the prefrontal response to mental arithmetic and the

no-control state by NIRS. PLoS ONE 7:e37791. doi: 10.1371/journal.pone. 0037791

Schäfer, J., and Strimmer, K. (2005). A shrinkage approach to large-scale covariance matrix estimation and implications for functional genomics. Stat. Appl. Genet. Mol. Biol. 4:32. doi: 10.2202/1544-6115.1175

Schudlo, L. C., and Chau, T. (2015). Towards a ternary NIRS-BCI: single-trial classiﬁcation of verbal ﬂuency task, Stroop task and unconstrained rest. J. Neural Eng. 12:066008. doi: 10.1088/1741-2560/12/6/066008

Schudlo, L. C., Power, S. D., and Chau, T. (2013). Dynamic topographical pattern classiﬁcation of multichannel prefrontal NIRS signals. J. Neural Eng. 10:046018. doi: 10.1088/1741-2560/10/4/046018

Shin, J., Müller, K.-R., and Hwang, H.-J. (2016). Near-infrared spectroscopy (NIRS) based eyes-closed brain-computer interface (BCI) using prefrontal cortex activation due to mental arithmetic. Sci. Rep. 6:36203. doi: 10.1038/srep36203

Shin, J., Müller, K.-R., Schmitz, C. H., Kim, D.-W., and Hwang, H.-J. (2017b). Evaluation of a compact hybrid brain-computer interface system. Biomed Res. Int. 2017:6820482. doi: 10.1155/2017/6820482

Shin, J., von Lühmann, A., Blankertz, B., Kim, D.-W., Jeong, J., Hwang, H.-J., et al. (2017a). Open access dataset for EEG+NIRS single-trial classiﬁcation. IEEE Trans. Neural Syst. Rehabil. Eng. 25, 1735–1745. doi: 10.1109/TNSRE.2016.2628057

Solis-Escalante, T., Müller-Putz, G., Brunner, C., Kaiser, V., and Pfurtscheller, G. (2010). Analysis of sensorimotor rhythms for the implementation of a brain switch for healthy subjects. Biomed. Signal Process. Control. 5, 15–20. doi: 10.1016/j.bspc.2009.09.002

van Erp, J. B. F., Lotte, F., and Tangermann, M. (2012). Brain-computer interfaces: beyond medical applications. Computer 45, 26–34. doi: 10.1109/MC.2012.107 Vidaurre, C., and Blankertz, B. (2010). Towards a cure for BCI illiteracy. Brain Topogr. 23, 194–198. doi: 10.1007/s10548-009-0121-6

von Lühmann, A., Wabnitz, H., Sander, T., and Müller, K.-R. (2017). M3BA: a mobile, modular, multimodal biosignal acquisition architecture for miniaturized EEG-NIRS based hybrid BCI and monitoring. IEEE Trans. Biomed. Eng. 64, 1199–1210. doi: 10.1109/TBME.2016.2594127

Wang, H., Li, Y., Long, J., Yu, T., and Gu, Z. (2014). An asynchronous wheelchair control by hybrid EEG–EOG brain–computer interface. Cogn. Neurodyn. 8, 399–409. doi: 10.1007/s11571-014-9296-y

Wang, M. J., Daly, I., Allison, B. Z., Jin, J., Zhang, Y., Chen, L. L., et al. (2015). A new hybrid BCI paradigm based on P300 and SSVEP. J. Neurosci. Meth. 244, 16–25. doi: 10.1016/j.jneumeth.2014.06.003

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Wolpaw, J. R., and Wolpaw, E. W. (2012). Brain-Computer Interfaces: Principles and Practice. New York, NY: Oxford University Press.

Yamawaki, N., Wilke, C., Zhongming, L., and Bin, H. (2006). An enhanced time-frequency-spatial approach for motor imagery classiﬁcation. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 250–254. doi: 10.1109/TNSRE.2006.875567

Yin, X. X., Xu, B. L., Jiang, C. H., Fu, Y. F., Wang, Z. D., Li, H. Y., et al. (2015). A hybrid BCI based on EEG and fNIRS signals improves the performance of decoding motor imagery of both force and speed of hand clenching. J. Neural Eng. 12:036004. doi: 10.1088/1741-2560/12/3/036004

Zhang, S., Zheng, Y. C., Wang, D. F., Wang, L., Ma, J. N., Zhang, J., et al. (2017). Application of a common spatial pattern-based algorithm for an fNIRSbased motor imagery brain-computer interface. Neurosci. Lett. 655, 35–40. doi: 10.1016/j.neulet.2017.06.044

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2018 Shin, Kwon and Im. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

