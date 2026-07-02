[Figure 1] system based on auditory stream segregation_images/imageFile1.png>)

# Journal of Biomechanical Science and Engineering

Vol.5, No.1, 2010

## A Brain-Computer Interface (BCI) System Based on Auditory Stream Segregation∗

Shin’ichiro KANOH∗∗, Ko-ichiro MIYAMOTO∗∗ and Tatsuo YOSHINOBU∗∗,∗∗∗

∗∗ Graduate School of Engineering, Tohoku University Aoba-yama 6–6–05, Sendai, 980–8579, Japan E-mail: kanoh@ecei.tohoku.ac.jp (S.K.) ∗∗∗ Graduate School of Biomedical Engineering, Tohoku University Aoba-yama 6–6–05, Sendai, 980–8579, Japan

Abstract

An auditory brain-computer interface (BCI) which detects event-related potentials (ERPs) elicited by selective attention to one of the tone streams was proposed. Two frequency oddball tone sequences with diﬀerent tone frequency ranges were alternately presented to subjects, and were perceived by subjects as two kinds of segregated streams. Event-related potentials elicited by two kinds of deviant tones were classiﬁed by linear discriminant analysis (LDA) to ﬁnd the stream subjects paid selective attention to. Experiments with six subjects have shown that this system could realize binary selection from two tone streams.

Keywords: brain-computer interface (BCI), selective attention, event-related potential,

auditory stream segregation, pattern classiﬁcation

#### 1. Introduction

The brain-computer interface (BCI) is an eﬀective tool to provide a communication between disabled patients due to spiral cord injury or motor diseases like ALS. In this system, the signal corresponding to activation of the patient’s brain is measured and analyzed, and the intentions or “thoughts” are detected for controlling external devices(1).

One of the ways to realize BCI by EEG (electro-encephalogram) is to detect the ERP (event-related potential) elicited by sensory stimuli. The BCI-based spelling system to choose one of 36 characters by using visual ERP was proposed(2). In this system, a matrix of 6 by 6 characters was presented and one of each row or column blinked in random order. Users were requested to focus on one of the characters, and the P300, one of the ERP components, which was elicited by the highlight of focused characters, was analyzed and detected. But in such a system, users must watch and focus on the visual display when they want to use it. Hill et al(3) proposed an ERP-based BCI system in auditory domain. In this system, two kinds of tone sequences were presented to users on each ear asynchronously, and they were requested to attend to the sequence from one of the ears. In this system, more than thirty electrodes were used to measure ERP to achieve higher accuracy.

In the present study, the auditory BCI system based on auditory stream segregation is proposed to realize a two-alternative choice, and is tested by the experiments with two-channel EEG measurements. In this system, series of short tones with two frequency ranges were presented alternately to subject’s right ear, and subjects were requested to attend to one of the “streams” which were perceived to be segregated as higher and lower tone sequences.

#### 2. Background

∗Received 30 July, 2009 (No. 09-0393) [DOI: 10.1299/jbse.5.32]

##### Copyright c 2010 by JSME

2.1. Auditory Stream Segregation

Auditory illusions or other interesting perceptual (e.g. ﬁgure-ground perception or perceptual grouping) and behavioral (e.g. cocktail-party eﬀect) phenomena have been studied

[Figure 2] system based on auditory stream segregation_images/imageFile2.png>)

Fig. 1 The schematic diagram of tone stimuli used in the experiment.

in psychophysics to uncover the nature of computational theory of auditory information processing. Such studies, which are known as auditory scene analysis(4), have shown that a lot of interesting phenomena related to Gestalt psychology, and their neuronal correlates have been investigated. (e.g. reference(5))

When two kinds of tones with diﬀerent frequencies (A, B) are presented alternately in time (e.g. ABABAB...) with a short inter-stimulus interval, such a sequence can be perceived as two segregated tone streams (AAAAA ..., and BBBBB...). This phenomenon is called auditory stream segregation, and can be treated as one of the auditory illusions, in which similarity of tone frequency overcomes the factor of time continuity.

- 2.2. Event-Related Potentials Event-related potentials (ERPs) are EEG transient voltage shifts induced by internal

events. In the present study, the components called P300 and MMN (mismatch negativity) were focused on to detect the subject’s choice from multiple stimuli. P300 is a component related to selective attention, and its latency is about 300 ms(6). It is observed as a positive voltage shift which is widely distributed on the vertex or occipital area of the scalp. The MMN is a negative voltage shift whose latency is about 100∼200 ms. It is related to the function of change detection of the sensory memory system, and the source is located in the primary sensory cortex of the sensory domain used in the paradigm(7).

Therefore, it is expected that these two components are modulated by selective attention, i.e. the magnitude of these ERP components is changed with selective attention to the “target” tones. Thus, in this study, we tried to extract the feature of these components with/without the attention to speciﬁc auditory stimuli.

The oddball paradigm which is generally used to induce these ERP components consists of a set of frequently presented tones (standard stimuli), some of which are randomly replaced by infrequently presented tones (deviant stimuli).

- 3. Methods

In this experiment, two auditory oddball sequences, each of which consisted of tone bursts were presented to the subject in such a way that tones in two sequences were alternately delivered. Parameters (inter-stimulus interval and frequency of each tone) were set so that the presented tones were perceived by subjects as two segregated auditory streams. Subjects were required to pay attention to one of the two streams.

The EEG responses to the deviant tones in each stream were measured and were classiﬁed for detecting the stream to which the subject paid attention.

- 3.1. Tone Stimuli Tone stimuli were generated by DSP (System 3, Tucker-Davis Technologies) and were

presented to subjects by headphones (HDA200, Sennheiser) at a level of 60 dB SPL. The schematic diagram of the presented tone sequences is shown in Fig. 1. Two oddball sequences n (n = 1,2) were presented to subject’s right ear alternately. Each oddball sequence consisted of standard stimuli (Sn: p = 0.9) and deviant stimuli (Dn: p = 0.1).

[Figure 3] system based on auditory stream segregation_images/imageFile3.png>)

(c) Subject C (d) Subject D

(e) Subject E (f) Subject F

Fig. 2 Averaged responses to deviant stimuli D1 (electrode Cz) on all subjects when each subject paid attention to stream 1 (solid line) and stream 2 (dashed line). Note that solid line denotes the response to the deviant stimuli embedded in the attended stream. Filled boxes denote the period of tone presentation.

The presented tone sequences consisted of tone bursts (duration 40 ms, rise/fall time 10 ms), and their frequencies were set as follows. S1: 1000 Hz, D1: 700 Hz (stream 1), S2: 2000 Hz, D2: 2600 Hz (stream 2). SOA (stimulus onset asynchrony) was set so that the subject could segregate presented tone sequences into stream 1 and stream 2. (An SOA of 200 ms was used in the present experiments: auditory stream segregation can generally occur for shorter SOA, but we set it to 200 ms to avoid excess superposition of auditory evoked potentials.)

- 3.2. Measurement The experiments in this study were approved by the Ethics Committee on Clinical Inves-

tigation, Graduate School of Engineering, Tohoku University, and were performed in accordance with the policy of the Declaration of Helsinki.

Six male volunteers with normal hearing ability (22∼24 years old) participated in the experiment as subjects. Six-day experiments were carried out with each subject. Each day of experimentation consisted of two sessions, in each of which the subject was requested to attend to one of the streams and to count the number of deviant stimuli presented in the attended stream. Each session was about ﬁve minutes long.

[Figure 4] system based on auditory stream segregation_images/imageFile4.png>)

(c) Subject C (d) Subject D

(e) Subject E (f) Subject F

Fig. 3 Averaged responses to deviant stimuli D1 (electrode F3) on all subjects when each subject paid attention to stream 1 (solid line) and stream 2 (dashed line). Note that solid line denotes the response to the deviant stimuli embedded in the attended stream. Filled boxes denote the period of tone presentation.

The EEG signal was recorded with Ag-AgCl electrodes at two locations (Cz, F3), and referred to right earlobe with a forehead ground. These signals were ampliﬁed (gain 500), bandpass ﬁltered (0.15∼100 Hz) and acquired to a personal computer with sampling frequency of 1000 Hz and anti-aliasing ﬁlter at 200 Hz (ESI, NeuroScan).

- 3.3. Pre-processing The recorded data was bandpass ﬁltered (1∼40 Hz), and the responses to deviant stimuli

(D1 and D2) were extracted (−100 ∼ 500 ms from the stimulus onset). The extracted data was referred to the mean amplitudes in the pre-stimulus baseline (−50 ∼ 0 ms) and was classiﬁed for detection. EEG epochs in which recorded amplitudes exceeded ± 50 µV or the normalized band power of alpha range exceeded 20% were excluded from further analysis to avoid the inﬂuences of artifacts.

- 3.4. Classiﬁcation and Detection The pre-processed data of the responses to deviant stimuli was classiﬁed by LDA (linear

discriminant analysis(8)) by the following method. The discriminant coeﬃcient matrix was calculated by using sample data set to discriminate “whether the subject paid attention to the

[Figure 5] system based on auditory stream segregation_images/imageFile5.png>)

(c) Subject C (d) Subject D

(e) Subject E (f) Subject F

Fig. 4 Averaged responses to deviant stimuli D2 (electrode Cz) on all subjects when each subject paid attention to stream 1 (dashed line) and stream 2 (solid line). Note that solid line denotes the response to the deviant stimuli embedded in the attended stream. Filled boxes denote the period of tone presentation.

stream n” by classifying the response to Dn in the test data set.

Two classiﬁers were designed independently to judge whether stream 1 and stream 2 were attended, respectively. The pre-processed epoch data taken from two electrodes was concatenated and was provided to the LDA classiﬁer as a vector (600 samples ×2 = 1200 dimensions).

For practical application of the present system, it would be reasonable that the user is presented tone sequences for a certain period of time, and the intention to attend to one of the streams is detected by using all the responses to the deviant stimuli during the period. To simulate such an application, the data was divided into 10 s blocks, and LDA was applied to all the responses to the deviant stimuli in each block. Finally, the attended stream was judged on the basis of decision by majority.

#### 4. Results

The averaged responses to the deviant stimuli D1 and D2 (deviant stimulus embedded in stream 1 and 2) measured from two electrode locations were shown in Figs. 2, 3, 4, and 5, where the subjects attended to one of the streams (stream 1 or stream 2) . It was shown that P300 and MMN components were elicited by the deviant stimuli.

[Figure 6] system based on auditory stream segregation_images/imageFile6.png>)

(c) Subject C (d) Subject D

(e) Subject E (f) Subject F

Fig. 5 Averaged responses to deviant stimuli D2 (electrode F3) on all subjects when each subject paid attention to stream 1 (dashed line) and stream 2 (solid line). Note that solid line denotes the response to the deviant stimuli embedded in the attended stream. Filled boxes denote the period of tone presentation.

In the auditory oddball paradigm, the response waveform usually contains auditory evoked potential. To evaluate ERP components, the averaged response to standard stimuli is usually subtracted from those to deviant stimuli (diﬀerence response). But the activities of such evoked potential are known to be smaller for a shorter SOA. It was shown by the present experiments that the evoked potentials were much smaller than ERPs. Thus in this study, responses to deviant stimuli were analyzed without subtracting the averaged response to standard stimuli.

The peak amplitudes of P300 and MMN were generally larger on location Cz and F3, respectively. And the averaged responses to the same deviant stimuli diﬀered according to which stream the subject attended to. (Note that D1 and D2 are embedded in stream 1 and stream 2, respectively.) And on some subjects, the attention-related responses were also observed with longer latencies (300∼400 ms).

The butterﬂy plot of the responses to all deviant stimuli D1 and D2, and their averaged waveform were shown in Fig. 6 (subject F, attended to stream 1, location Cz). The P300 and MMN were observed also in the raw waveforms.

Within this time window, two additional tones were presented at time 200 and 400 ms. But the evoked potentials by these two tones as well as the target deviant tone were quite small

[Figure 7] system based on auditory stream segregation_images/imageFile7.png>)

- (a) Responses to D1

- (b) Responses to D2

Fig. 6 An example of single shot responses to deviant stimuli D1 (a) and D2 (b) and their averaged waveform (subject F, attended to stream 1, location Cz). Filled boxes denote the period of tone presentation.

and negligible.

The result of detection whether the subject attended to stream 1 or 2 was judged by the majority of all the classiﬁcation results in the time windows of 10 s. The correct detection rate and its bit transfer rate are shown in Fig. 7. All the measured responses were used as both sample and test data, and LDA was designed for each subject. More than 95% correct detection rate and bit transfer rate of about 5 bit/min (one judgment in every 10 seconds, maximum 6 bit/min) were achieved.

#### 5. Conclusions and Further Works

In this study, the BCI system using selective attention to the segregated tone stream (auditory stream segregation) was proposed and demonstrated. This system detected which tone stream presented to one ear was the target of selective attention. The detection accuracy of two-channel data of the response to deviant stimuli by using LDA classiﬁer with decision by majority was investigated. It was shown that the present paradigm could be used for BCI.

In the previous study on auditory BCI, the two independent tone sequences were presented to both ears and detected to which ear the target (attended) sequences were presented, so the choice on one detection was limited to 1 bit (left or right)(3). But in the proposed system, the auditory stream segregation of tone sequences presented to one ear was utilized and

[Figure 8] system based on auditory stream segregation_images/imageFile8.png>)

- (a) Correct Detection Rate

- (b) Bit Transfer Rate

Fig. 7 Detection accuracy on all subjects. Correct detection rate (a) and bit transfer rate (b) are shown. Black and gray bars denote the rate when stream 1 and stream 2 were attended, respectively.

can be extended to many-to-one choice BCI by increasing the number of tone streams to be segregated.

The correct detection rate tested for all individual responses to deviant stimuli (i.e. without judging on the basis of decision by majority within 10-second time window) by 10-fold cross-validation was 60∼70%. The non-stationality of the measured EEG signal, day-by-day diﬀerences in ERPs due to the mental and physical state of subjects, and low S/N ratio of the measured EEG data are thought to be the reasons for the 10-fold cross-validation shown above. To increase the accuracy, pre-processing methods for artifact reduction and increasing the stability of classiﬁcation (e.g. down-sampling, ﬁltering) and feature selection/extraction techniques should be improved.

#### Acknowledgments

The authors would like to thank Mr. Tomohisa Yamagishi for his support for the experiments. Part of the present study was supported by Grants-in-Aid for Scientiﬁc Research (#19560414), Ministry of Education, Culture, Sports, Science and Technology, Japan.

[Figure 9] system based on auditory stream segregation_images/imageFile9.png>)

#### References

- ( 1 ) Wolpaw, J.R., Birbaumer, N., Heetderks, W.J., McFarland, D.J., Peckham, P.H., Schalk, G., Donchin, L.A., Robinson, C.J. and Vaughan, T.M., Brain-computer interface technology: A review of the ﬁrst international meeting, IEEE Transactions on Rehabilitation Engineering, Vol. 8, No. 2 (2000), pp.164–173.
- ( 2 ) Donchin, E., Spencer, K.M. and Wijesinghe, R., The mental prosthesis: Assessing the speed of a P300-based brain-computer interface, IEEE Transactions on Rehabilitation Engineering, Vol. 8, No. 2 (2000), pp.174–179.
- ( 3 ) Hill, N.J., Lal, N., Bierig, K., Birbaumer, N. and Scholkof, B., An auditory paradigm for brain-computer interfaces, Advances in Neural Information Processing Systems, Vol. 17

(2005), pp.569–576.

- ( 4 ) Bregman, A.S., Auditory scene analysis: The perceptual organization of sound, (1990), The MIT Press.
- ( 5 ) Kanoh, S., Futami, R. and Hoshimiya, N., Sequential grouping of tone sequence as reﬂected by the mismatch negativity, Biological Cybernetics, Vol. 91, No. 6 (2004), pp.388–395.
- ( 6 ) Sutton, S., Braren, M., Zubin, J. and John E.R., Evoked-potential correlates of stimulus uncertainty, Science, Vol. 150, No.3700 (1965), pp.1187–1188.
- ( 7 ) N¨a¨atanen, R., Tervaniemi, M., Sussman, E., Paavilainen, P. and Winkler, I., ‘Primitive intelligence’ in the auditory cortex, Trends in Neurosciences, Vol. 24, No. 5 (2001), pp.283–288.
- ( 8 ) Duda, R.O., Hart, P.E. and Stork, D.G., Pattern Classiﬁcation, 2nd Edition, (2000), Wiley Interscience Publication.

