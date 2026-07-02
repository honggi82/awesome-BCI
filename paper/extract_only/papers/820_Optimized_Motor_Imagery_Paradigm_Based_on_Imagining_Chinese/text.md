## Optimized motor imagery paradigm based on imagining Chinese characters writing movement

zhaoyang Qiu, Brendan Z. Allison, Jing Jin, Member, IEEE, Yu Zhang, Member, IEEE, Xingyu Wang, Wei Li, Andrzej Cichocki, Fellow, IEEE



Abstract—Background: Motor imagery (MI) is a mental representation of motor behavior that has been widely used as a control method for a brain–computer interface (BCI), allowing communication for the physically impaired. The performance of MI based BCI mainly depends on the subject’s ability to self-modulate EEG signals. Proper training can help naive subjects learn to modulate brain activity proficiently. However, training subjects typically involves abstract motor tasks and is time-consuming. Methods: To improve the performance of naive subjects during motor imagery, a novel paradigm was presented that would guide naive subjects to modulate brain activity effectively. In this new paradigm, pictures of the left or right hand were used as cues for subjects to finish the motor imagery task. Fourteen healthy subjects (11 male, aged 22–25 years, mean 23.6±1.16) participated in this study. The task was to imagine writing a Chinese character. Specifically, subjects could imagine hand movements following the sequence of writing strokes in the Chinese character. This paradigm was meant to find an effective and familiar action for most Chinese people, to provide them with a specific, extensively practiced task and help them modulate brain activity. Results: Results showed that the writing task paradigm yielded significantly better performance than the traditional arrow paradigm (p<0.001). Questionnaire replies indicated that most subjects thought the new paradigm was easier and more comfortable. Conclusions: The proposed new motor imagery paradigm could guide subjects to help them modulate brain activity effectively. Results showed that there were significant improvements using new paradigm, both in classification accuracy and usability.

### Index Terms—motor imagery, brain-computer interface (BCI), CSP, paradigm.

This work was supported in part by the Grant National Natural Science Foundation of China, under Grant Nos. 61573142, 61203127, 91420302 and 61305028. This work was also supported by the 13 Fundamental Research Funds for the Central Universities (WG1414005, WH1314023, and WH1516018) and Shanghai Chenguang Program under Grant 14CG31. Z. Qiu, Yu Zhang, *X. Wang and *J. Jin are with the Key Laboratory of Advanced Control and Optimization for Chemical Processes, Ministry of Education, East China University of Science and Technology, Shanghai, P.R. China (*correspondence e-mail: xywang@ecust.edu.cn, jinjingat@gmail.com).

- B.Z. Allison is with Guger Technologies OG, 8020 Graz, Austria. W. Li is with Shenyang Institute of Automation, Chinese Academy of Sciences, Shenyang 110016, China, with the School of Electrical Engineering and Automation, Tianjin University, Tianjin 300072, China, and also with the Department of Computer & Electrical Engineering and Computer Science, California State University, Bakersfield, California 93311, USA (corresponding author, e-mail: wli@csub.edu). A. Cichocki is with Laboratory for Advanced Brain Signal Processing, Brain Science Institute, RIKEN, Wako-shi, 351-0198, Japan and Systems Research Institute of Polish Academy of Science, Warsaw, Poland.

I. INTRODUCTION

# B

rain-computer interface systems (BCIs) can translate brain activities into commands that could be used to control

external devices [1-3]. BCIs provide a new communication channel for people, which is different from communication channels that rely on the conventional neuromuscular pathways of peripheral nerves and muscles [4]. Many BCIs are based on the EEG recorded noninvasively via electrodes placed on the scalp. While various different neural activities can be used as features in electroencephalogram (EEG) based BCIs, most BCI systems rely on motor imagery [5, 6], event-related potential [7-10] or visual evoked potentials [11-14].

It has been well established that imagination of limb movement could result in event-related desynchronization (ERD) [5] and event-related synchronization (ERS) [6]. Specifically, movement imagery (MI) affects the mu (8-12Hz) and beta waves (13-30Hz) in the EEG. Movement imagery produces significant ERD over the contralateral central area during imagination of right and left hand movement [15]. The basic principle of an MI based BCI entails translating ERD phenomena into control commands [16, 17]. However, the differences are often not sufficient to provide reliable control signals in practical applications [18-20]. It has been reported that about 20% of MI BCI users do not attain sufficient accuracy to control an application [18]. This phenomenon was initially called “BCI illiteracy”, although other terms such as “BCI inefficiency” [21] have also been used.

Many researchers have endeavored to develop algorithms to improve performance [22, 23]. Channel selection methods have been widely used in MI based BCIs to enhance performance by removing task irrelevant and redundant channels [24-26]. Some advanced machine learning algorithms were set up to improve the performance of BCI [27, 28]. These classifiers could yield high classification accuracy. In addition, various feature extraction methods have been proposed to detect ERD/ERS patterns, which could discriminate different mental states effectively [29-31]. However, no matter how outstanding the algorithms are, BCIs cannot obtain good performance if subjects cannot modulate brain activity as required by the BCI [16].

To help users modulate brain activity proficiently, many feedback training methods have been proposed to improve the performance of MI-based BCIs. Feedback can help subjects master effective strategies to modulate brain activity by providing them the information about EEG changes. In [32], Neuper et al. compared realistic feedback and abstract feedback

for the same task. Results showed that there was not much difference in training performance. Blankertz et al. proposed the Berlin Brain-Computer Interface (BBCI), in which feedback was provided by a discrete form [33]. The BBCI could exhibit effective performance quickly in untrained subjects. Yue et al. (2012) presented an EEG-based real-time control paradigm with visual feedback, in which the external device was a simulated inverted pendulum [34]. With suitable training procedures, subjects would learn to control unstable devices through BCI. [35] investigated the effect of static and dynamic visual representations of target movements during the BCI neurofeedback training. Other work introduced an auditory feedback method, and the results showed that the auditory feedback was a suitable substitute for the visual equivalent [36]. However, it has been reported that feedback can have both inhibitory and facilitative effects on EEG control [37]. Each normal feedback training session should begin with a calibration run without feedback. The calibration data are employed to construct the classifier for the next feedback runs. Hence, feedback performance largely depends on the initial model, and the calibration data may not be sufficiently discriminable. If subjects were unfamiliar with the system and failed at MI tasks at the initial state, the feedback training session could frustrate subjects [38].

At the beginning of training process, naive subjects may try various motor imagery strategies. If the MI based BCI system can provide subjects a proper cue that instructs them to do motor imagery the right way, it will save training time and reduce frustration. Therefore, it is necessary to set up a suitable paradigm for subjects, which will help them to perform the MI tasks effectively.

In most paradigms, only visual or auditory cues were used to instruct subjects to perform the corresponding classes of MI tasks (such as left hand movement, right hand movement or foot movement) [34, 39]. But these cues could not instruct subjects how to perform the imagination. The type of movement imagery can have a major effect on BCI performance, for example, [40] found that subjects who relied on visual imagination of hand movement performed worse than subjects who focused on the kinesthetic aspect of the same task.

- [41] found that subjects could attain better performance by imagining familiar actions.

The strategy of motor imagery in [41] was effective for a small group of people who had formal musical training and had played and practiced piano regularly. Since different subjects were familiar with different actions, the purpose of this paper was to find a familiar action that can be accepted by most Chinese people. Therefore, we developed a novel paradigm to guide subjects to imagine Chinese characters writing movements with their right or left hand.

In this paradigm, a picture of a hand was used as a cue for subjects to focus on one of their hands. A Chinese character shown on the screen was used to guide subjects regarding what kind of motor imagery task they should perform. Subjects imagined moving the chosen hand to follow the strokes of the shown Chinese character. In other words, the subjects imagined that they were writing on the blackboard using the right or left

hand. This paradigm would give subjects a specific MI task instruction: moving from left to right, moving from top to bottom, drawing an oblique line or a point, etc. The task of writing a Chinese character can make people focus more attention on motor imagery. We compared this task to a traditional approach in which an arrow cue stimulus was used.

II. METHOD

- A. Subjects Fourteen healthy subjects (11 male, aged 22-25 years, mean

23.6±1.16) participated in the motor imagery experiment. All subjects signed a written consent form prior to this experiment and were paid for their participation. The local ethics committee approved the consent form and experimental procedure before any subjects participated. All subjects were right handed with no clinical history of neurological disorders, according to self-reports. All subjects’ native language was Mandarin Chinese. None of them had experience with any MI based BCI before this study.

- B. Experimental paradigms

After being prepared for EEG recording, the subjects were seated in a comfortable chair about 80cm from a standard 24 inch LED monitor (60 Hz refresh rate, 1920×1080 screen resolution) in a shielded room. The cues were presented in the middle of the screen. During data acquisition, subjects were asked to relax and avoid unnecessary movement.

Two different types of paradigms were utilized and compared in this study: (1) the traditional arrow paradigm, (2) the writing task paradigm.

[Figure 1]

Fig. 1. Timing of a trial of the traditional arrow paradigm. Each trial consisted of task and rest periods. Subjects started to execute MI tasks while the arrow appeared on the screen. The time segment between seconds 3 and 7 was used for feature extraction.

Throughout both paradigms, motor imagery was performed without feedback. The subjects were told to focus on motor imagery during the experiment. For each subject, two classes of motor imagery were performed: left hand and right hand. These tasks were pseudo randomly distributed throughout the run. Each experimental paradigm included two runs, and each run is comprised of 50 single trials. A total of 100 trials of EEG measurements were performed (half for each class of MI).

(1) The traditional arrow paradigm: This paradigm used an arrow pointing to the left or right, which has been widely used [42, 43]. As illustrated in Fig. 1, at the beginning of a trial (t=0s), a fixation cross appeared on the black screen. After two seconds (t=2s), an arrow cue was shown that pointed either the

left or the right (corresponding to one of the two classes of MI tasks: left hand or right hand). The subjects had 6s to imagine the movement of either their left or right hand, as indicated by the cue arrow. In this paradigm, each subject was asked to imagine a hand movement which they felt was easiest for them, and so the exact types of motor imagery were not consistent across subjects. A short break followed, during which the screen was black.

(2) The writing task paradigm: Fig. 2 presented the writing task paradigm. Unlike the traditional arrow paradigm, a static photograph of a Chinese character and a forearm was displayed on the black screen. Before the motor imagery (t=0s), a fixation cross was shown on the black screen instructing subjects to get ready. After two seconds (t=2s), the fixation cross was replaced by a picture of the forearm and Chinese character. The picture of the forearm was used as a cue to tell subjects which hand movement they should imagine. The Chinese character was to instruct the subjects what kind of the writing movement they should imagine. Each subject had 6s to perform the MI task. During this period, the subjects were asked to imagine hand movements that followed the strokes of the Chinese character on the screen. It was as though the subject was writing the character on the blackboard with the right or left hand. A short break (2s) followed, during which the screen was black. Each Chinese character used in this paper contains 5 strokes.

[Figure 2]

- Fig. 2. Timing of a trial of the writing task paradigm. Each trial consisted of task and rest periods. Subjects started to execute MI tasks while the character and a forearm appeared on the screen. The time segment between seconds 3 and 7 was used for feature extraction.

C. EEG acquisition

- Fig. 3. The electrode distribution used in this study. All channels were used for signal recording and analysis.

[Figure 3]

EEG signals were sampled at 250 Hz through the Neuro Scan amplifier (high-pass and low-pass filters: 0.1 Hz and 50 Hz, with the mains power supply (50Hz) filtered out) using a 32-channel cap following the 10-20 international system (Fig. 3). All channels were used for signal recording and analysis, which were referenced to electrode A1 located over the right mastoid with a forehead ground (GND). All impedances were below 5 k ohms. The sequence of the two paradigms in this experiment was counterbalanced.

- D. Feature extraction procedure

For motor imagery feature extraction, the 30 channels shown in Fig. 3 were used without further channel selection. The EEG data were band-pass filtered using a fifth order Butterworth band pass filter from 8 to 30 Hz, since this frequency band included the range of frequencies that were mainly involved in performing motor imagery.

The CSP algorithm is an efficient feature extraction algorithm, which has been widely used in MI based BCI systems [44-47]. CSP is based on the simultaneous diagonalization of two covariance matrices. It finds a spatial filter to maximize variance for one class and minimize variance for another class at the same time to improve classification.

- E. Classification scheme

A support vector machine (SVM) is a machine learning method proposed in the 1990s [48]. It is mainly proposed for two class pattern recognition problems. For a given data set

ARd from two classes that can be divided by a hyperplane linearly, the hyperplane is expressed as: WAb  0 . W  Rd is weight vector and bis the intercept (scalar). The problem is transformed into finding the optimal hyperplane as follows:

 

2

(

1 )

- 1

min , || || ε , 0

- 2

. . i( T i ) 1 i, 0, (1, )

n

i i

i

W W c c s t y W A b i n



            





(10)

The optimization problem is a convex quadratic programming problem [49]. Where A(i) is a feature vector of a training

sample, yi is the category with labels {-1, 1} which A(i) belongs to. W is the hyperplane coefficients vector. The

parameter i is called slack variables and c is regularization parameter. c is used to control the trade-off between the model complexity and empirical risk [50]. 10*10-fold cross validations accuracy of the data were used for each subject.

- F. Subjective report

After completing each session, each subject was asked a question about the paradigm: Was this paradigm hard? The question could be answered on a 1-5 Likert scale indicating strong disagreement, moderate disagreement, neutrality, moderate agreement, or strong agreement.

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

- Fig.4. This figure displays the averaged spectra of 100 trials recorded at C3 and C4 for each subject in the writing task paradigm (blue: right hand, black: left hand). Lines in the map have been smoothed. S1-S10 refers to subjects 1-10.
- Fig.5. This figure displays the averaged spectra of two different paradigms at C3 and C4 (blue: right hand, black: left hand). For each paradigm, the maps are averaged across all ten subjects.

[Figure 8]

[Figure 9]

III. RESULTS

Different articles have presented different thresholds for BCI “efficiency” [51]. Since we used subjects who were new to motor imagery BCIs, we used a low threshold. Four subjects attained accuracies less than 60% in both paradigms. These subjects were not selected for further analysis. Ultimately, results from ten subjects are shown below.

A. EEG results

To illustrate the differences between two classes of motor imagery in the writing task paradigm, power spectral densities (PSDs) were calculated from the average data, plotted in Fig.4. Each map was based on 100 averaged trials (50 left hand motor imagery trials and 50 right hand motor imagery trials) after being filtered by 8-30 Hz band pass filter.

Fig. 5 presents the PSDs averaged across all ten subjects from two different paradigms at C3 and C4. For the writing task paradigm, the energy from right hand motor imagery was lower than left hand motor imagery at C3, and the energy from left hand motor imagery was lower than right hand motor imagery at C4. In the beta band, signals from right hand motor imagery were higher than left hand motor imagery at both channels. For the traditional arrow paradigm, signals from right hand motor imagery were higher than left hand motor imagery at C3, while there was no significant difference of two classes of MI tasks at C4.

In CSP method, W is the projection matrix, and W-1 is the inverse matrix of W. The columns of W-1 are the time invariant vectors of EEG source distribution vectors called common spatial patterns [52]. The first and last common spatial patterns are shown in Fig. 6. The first pattern was obtained by maximizing the variance of the right hand motor imagery, which was associated with the ERD phenomenon over the area of the left sensorimotor area of the cortex. Accordingly, the ERD phenomenon over the right motor area was associated

with the last pattern, corresponding to the left hand motor imagery.

Results in Fig. 6 show that, for the writing task paradigm, spatial discriminability of right and left hand motor imagery was apparent. Maps also indicated that areas around channel C3 and C4 were associated with the left and right hand motor imageries, which was consistent with the neurophysiology phenomenon reported in [53-54]. Results of the traditional arrow paradigm did not show clear pattern from the contra lateral hemisphere for left and right motor imagery. ERS phenomena were also observed during left hand motor imagery in the writing task paradigm.

B. Classification Performance Comparison

For each of the two paradigms, a 10×10-fold cross-validation was implemented to evaluate the classification performance. The classification accuracies of all ten subjects from both paradigms are shown in Fig. 7. Results showed that the classification accuracies of the new writing task paradigm were better than the traditional arrow paradigm for all subjects. The average classification accuracy of writing task paradigm was

[Figure 10]

[Figure 11]

- Fig. 6. The topographic maps of the first and last spatial patterns extracted by the CSP method. The patterns were extracted from averages of 100 trials of the two different paradigms.
- Fig. 7. Classification accuracies of all ten subjects from the writing task paradigm and traditional arrow paradigm.

[Figure 12]

TABLE I TEN SUBJECTS' RESPONSES TO QUESTIONS ABOUT THE TWO PARADIGMS

S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 Average The normal arrow paradigm 2 4 5 2 4 3 3 4 5 4 3.6±1.1

The writing task paradigm 2 3 4 1 1 3 2 2 4 2 2.4±1.1

imagining the same movement every time would make them bored and tired, and could cause them to lose focus. Performing different tasks could reduce boredom. However, some subjects thought that it would be difficult to imagine different movements in different trials. In the writing task paradigm, different characters were displayed in different trials. This task was also very simple and highly practiced: imagining writing. Subjects' responses to the questionnaires indicated that they thought that the writing task paradigm could help them focus their attention and reduce fatigue. Table 1 shows that the subject S5 considered the new paradigm much easier and more comfortable. Concordantly, S5 exhibited the greatest difference between the two paradigms (26%), shown in Fig. 7. Table 1 indicates that S4 thought that both paradigms are easy, and he performed well in both paradigms (89% in the writing task paradigm and 77% in the traditional arrow paradigm).

79.8%, which was 14.7% higher than traditional arrow paradigm (65.1%). Among all ten subjects, S5 achieved the greatest improvement by using the writing task paradigm (increased by 26%).

A paired samples T-Test was used to show the classification accuracy differences between the writing task paradigm and traditional arrow paradigm (p<0.001). It showed the classification accuracy was increased significantly by using our new paradigm compared to the traditional paradigm.

C. Subjective report

Ten subjects’ responses to the question about task difficulty are shown in Table 1. The replies are based on a 1-5 Likert scale to indicate strong disagreement, moderate disagreement, neutrality, moderate agreement, or strong agreement. In the comparison of difficulty, significant differences were found between the two paradigms (p=0.0026).

Although this study involving 10 subjects yielded good performance using a novel motor imagery paradigm in a BCI, further work is needed. After the experiment, some subjects said that imagining writing with the left hand made them feel awkward (all subjects were right handed). Some other subjects said that they imagined writing the strokes in a different sequence when they wrote with the left hand. They prefer to imagine the characters as abstract symbols and copy them. Although this did not appear to affect their task performance, it will be interesting to find the differences in brain patterns for these different subject states.

IV. DISCUSSION

The primary goal of this study was to investigate whether the new paradigm presented in this paper could help subjects in a motor imagery (MI) BCI. Two paradigms were compared in our experiment. The results showed that the writing task paradigm yielded significantly better performance than the traditional arrow paradigm.

Fig.4 displays the averaged spectra of the two motor imagery tasks in the writing task paradigm. Several points stand out: (1) For channel C3, the power during right hand motor imagery was lower than left hand motor imagery in the band around 8-12 Hz. (2) For channel C4, the power during left hand motor imagery was lower than right hand motor imagery in the band around 8-12 Hz. Activity in the alpha-band (8-12 Hz) is called the Mu rhythm, which is recorded at rest and attenuated by voluntary movements. Research initially suggested that the Mu rhythm is an ‘‘idling’’ rhythm in the motor cortex [55, 56]. However, Mu rhythm activation has been also reported during the execution of different tasks. As reported in [43], the Mu-rhythm is task sensitive, and can change based on motor imagery in the motor cortex.

Future work could also explore the comparison between user-selected imagery and experimenter-defined imagery. While the approach used by Wolpaw and colleagues encourages subjects to explore different mental strategies for control, the approach from Pfurtscheller and colleagues adopted by other groups generally does not. Future work could further study the relative merits of these two approaches to motor imagery for different users.

V. CONCLUSIONS

In this study, we introduced a new motor imagery based BCI paradigm using Chinese characters as visual cues, which we hypothesized would help subjects perform two MI tasks: writing the character with the right or left hand. Experimental results based on ten healthy subjects demonstrated that this new paradigm yielded significantly better classification accuracies than the conventional paradigm using arrows as visual cues (p<0.001). Furthermore, most subjects thought that the new paradigm was easier, based on their questionnaire responses. Future work will focus on simplifying the characters to shorten the time required to complete the imagined task, and experiments with online feedback.

The traditional arrow paradigm instructs subjects to perform a corresponding MI tasks, and subjects imagined a movement they prefer. Subject S1, S2, S4, S5, S8 and S9 reported that they imagined grasping an object using the left or right hand in this paradigm. Subjects S3 and S10 imagined lifting a dumbbell. Subject S6 imagined shaking hands with other people. Subject S7 imagined boxing. Hence, the user-selected imagery was not consistent across the ten subjects in the traditional arrow paradigm. Many subjects reported that they thought that

REFERENCES

- [1] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain–computer interfaces for communication and control,” Clin Neurophysiol, vol. 113, no. 6, pp. 767-791, Jun. 2002.

- [2] J. Jin, B. Z. Allison, E. W. Sellers, C. Brunner, P. Horki, X. Wang, and C. Neuper, “An adaptive P300-based control system,” J Neural Eng, vol. 8, no. 3, pp. 036006, Apr. 2011.

- [3] B. V. D. Laar, D. P. Bos, B. Reuderink B, and M. poel, “How Much Control Is Enough? Influence of Unreliable Input on User Experience,” IEEE Trans. Cybern, vol. 43, no. 6, pp. 1584-1592, Dec. 2013.

- [4] J. N. Mak and J. R. Wolpaw. “Clinical applications of brain–computer interfaces: current state and future prospects,” IEEE Rev Biomed Eng, vol. 2, pp. 187-199, May 2010.

- [5] G. Pfurtscheller, “Graphical display and statistical evaluation of event-related desynchronization (ERD),” Electroencephalogr Clin Neurophysiol , vol.43, no. 5, pp. 757-760, Nov. 1977.

- [6] G. Pfurtscheller, “Event-related synchronization (ERS): an electrophysiological correlate of cortical areas at rest,” Electroencephalogr Clin Neurophysiol, vol. 83, no.1, pp. 62-69, Jul. 1992.

- [7] B. Z. Allison, E. W. Wolpaw, and J. R. Wolpaw. “Brain-computer interface systems: progress and prospects,” Expert Rev Med Devices, vol. 4, no. 4, pp. 463-474, Jul. 2007.
- [8] J. Jin, B. Z. Allison, E. W. Sellers, C. Brunner, P. Horki, X. Wang, and C. Neuper. “Optimized stimulus presentation patterns for an event-related potential EEG-based brain computer interface,” Medical & Biological Engineering & Computing, vol. 49, no. 2, pp. 181-191, Feb. 2011.
- [9] J. Jin, E. W. Sellers, S. Zhou, Y. Zhang, X. Wang, and A. Cichocki. “A P300 brain computer interface based on a modification of the mismatch negative paradigm,” International Journal of Neural Systems, vol. 25, no.3, pp. 595-599 Feb. 2015.

- [10] J. Jin, I. Daly, Y. Zhang, X. Wang, and A. Cichocki, “An optimized ERP brain–computer interface based on facial expression changes,” J Neural Eng, vol. 11, no. 3, pp. 036004, Jun. 2014.

- [11] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao, “Hig hspeed spelling with a noninvasive brain-computer interface,” Proc. Natl

. Acad. Sci. USA, vol. 112, no. 44, pp. E6058-67, Nov. 2015.

- [12] Y. Li, J. Pan, J. Long, T. Yu, F. Wang, Z. Yu, and W. Wu, “Multimodal BCIs: Target Detection, Multi-dimensional Control, and Awareness Evaluation in Patients with Disorder of Consciousness, ” Proc of the IEEE, vol. 104, no. 2, pp. 332-352, Feb. 2016.

- [13] D. Zhang, B. Hong, X. Gao, S. Gao, and B. Röder. “Exploring steady-state visual evoked potentials as an index for intermodal and crossmodal spatial attention, ” Psychophysiology, vol. 48, no. 5, pp. 665-75, May. 2011.

- [14] B. Z. Allison, D. J. McFarland, G. Schalk, S. D. Zheng, M. M. Jackson, and J. R. Wolpaw. “Towards an independent brain-computer interface using steady state visual evoked potentials,” Clin Neurophysiol, vol. 119, no. 2, pp. 399-408, Feb. 2008.

- [15] G. Pfurtscheller, C. Neuper, D. Flotzinger, and M. Pregenzerb, “EEG-based discrimination between imagination of right and left hand movement,” Electroencephalogr Clin Neurophysiol, vol. 103, no. 6, pp. 642-651, Dec. 1997.

- [16] B. Xia, Q. Zhang, H. Xie, and J. Li, “A neurofeedback training paradigm for motor imagery based Brain-Computer Interface,” Neural Networks (IJCNN), The 2012 International Joint Conference on, vol.20, pp.1-4, Jun. 2012.
- [17] R. Liu, Y. Wang, and L. Zhang, “An FDES-Based Shared Control Method for Asynchronous Brain-Actuated Robot,” IEEE Trans. Cybern, no. 99, , pp. 1, Sep. 2015.
- [18] B. Blankertz, C. Sannelli, S. Halder, E. M. Hammer, A. Kubler, K. R. Muller, G. Curio, and T. Dickhaus, “Neurophysiological predictor of SMR-based BCI performance,” Neuroimage, vol. 51, no. 4, pp. 1303–9, Mar. 2010.
- [19] C. Guger, G. Edlinger, W. Harkam, I. Niedermayer, and G. Pfurtscheller, “How many people are able to operate an EEG-based brain-computer interface (BCI)?,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 11, no. 2, pp. 145–7, Jun. 2003.
- [20] B. Blankertz, F. Losch, M. Krauledat, G. Dornhege, G. Curio, and K. R. Muller, “The berlin brain–computer interface: accurate performance from first-session in bci-naive subjects,” IEEE Trans Biomed Eng, vol. 55, no. 10, pp. 2452–62, Oct. 2008.
- [21] T. Kaufmann, S. M. Schulz, A. Köblitz A, G. Renner, C. Wessig, and A. Kubler, “Face stimuli effectively prevent brain-computer interface

- inefficiency in patients with neurodegenerative disease,” Clinical Neurophysiology Official Journal of the International Federation of Clinical Neurophysiology, vol. 124, no. 5, pp. 893–900, May. 2013.
- [22] D. Coyle D, G. Prasad, and T. M. Mcginnity, “Faster self-organizing fuzzy neural network training and a hyperparameter analysis for a brain-computer interface,”. IEEE Trans. Syst., Man, Cybern. B, Cybern, vol. 39, no. 6, pp. 1458-71, Sep. 2009.
- [23] D. Iacoviello, A. Petracca, M. Spezialetti, and G. placidi, “A Classification Algorithm for Electroencephalography Signals by Self-Induced Emotional Stimuli,” IEEE Trans. Cybern, no. 99, pp. 1-10, Nov.2015.

- [24] A. Al-Ani and A. Al-Sukker, “Effect of feature and channel selection on EEG classification,” in Conf Proc IEEE Eng Med Biol Soc, pp. 2171-2174, 2006.

- [25] D. Garrett, D. A. Peterson, C. W. Anderson, and M.H Thaut, “Comparison of linear, nonlinear, and feature selection methods for EEG signal classification,” IEEE Trans Neural Syst Rehabil Eng, vol.11, no. 2, pp. 141-144, Jun. 2003.

- [26] T. N. Lal, M. Schroder, T. Hinterberger, J. Weston, M. Bogdan, N. Birbaumer, Scholkopf, and Bernhard, “Support vector channel selection in BCI,” IEEE Trans Biomed Eng, vol. 51, no. 6, pp.1003-1010, Jun. 2004.

- [27] K. R. Muller, M. Krauledat, G. Dornhege, G. Curio, and B. Blankertz, “Machine learning and applications for brain-computer interfacing,” in Proc of the 2007 Conf on Human interface: Part I, pp. 705-714. 2007.
- [28] K. R. Muller, M. Tangermann, G. Dornhege, M. Krauledat, G. Curio, and B. Blankertz, “Machine learning for real-time single-trial EEG-analysis: From brain-computer interfacing to mental state monitoring,” J Neuro Meth, vol. 167, no. 1, pp.82-90, Jan. 2008.
- [29] S. Lemm, B. Blankertz, G. Curio, and K. Muller, “Spatio-spectral filters for improving the classification of single trial EEG,” IEEE Trans Biomed Eng, vol. 52, no. 9, pp. 1541-1548, Sep. 2005.
- [30] G. Dornhege, B. Blankertz, M. Krauledat, F. Losch, G. Curio, and K. Muller, “Combined optimization of spatial and temporal filters for improving brain-computer interfacing,” IEEE Trans Biomed Eng, vol. 53, no. 11, pp. 2274-2281, Dec. 2006.
- [31] Q. Novi, C. Guan, T. H. Dat, and P. Xue, “Sub band common spatial pattern for brain-computer interface,” In Proc. 3rd Int. Conf. Neural Eng. IEEE Eng. Med. Biol. Soc. (EMBS), pp. 204-207, 2007.
- [32] C. Neuper, R. Scherer, S. Wriessnegger, and G. Pfurtscheller. “Motor imagery and action observation: modulation of sensorimotor brain rhythms during mental control of a brain-computer interface,” Clinical neurophysiology, vol. 120, no. 2, pp. 239-247, Feb. 2009.
- [33] B. Blankertz, G. Dornhege, M. Krauledat, K. R. Muller, and G. Curio. “The non-invasive berlin brain-computer interface: Fast acquisition of effective performance in untrained subjects,” NeuroImage, vol. 37, no. 2, pp. 539-550, 2007.
- [34] J. Yue, Z. Zhou, J. Jiang, Y. Liu, and D. Hu, “Balancing a simulated inverted pendulum through motor imagery: an EEG-based real-time control paradigm,” Neuroscience Letters, vol. 524, no. 2, pp. 95-100, Aug. 2012.
- [35] T. Kondo, M. Saeki, Y. Hayashi, K. Nakayashiki, and Y. Takata, “Effect of instructive visual stimuli on neurofeedback training for motor imagery-based brain-computer interface,” Human Movement Science, vol. 43, pp. 239-249, Oct. 2015.
- [36] K. A. Mccreadie, D. H. Coyle, and G.Prasad, “Is sensorimotor BCI performance influenced differently by mono, stereo, or 3-D auditory feedback?” IEEE Trans. Neural Syst. Rehabil. Eng, vol. 22, no. 3, pp. 431-440, May. 2014.
- [37] D. J. McFarland, L. M. McCane, and J. R. Wolpaw, “EEG-based communication and control: short-term role of feedback,” IEEE Trans. Rehabil. Eng., vol. 6, no. 1, pp. 7–11, Mar. 1998.
- [38] T. Yu, J. Xiao, F. Wang F, R. Zhang, Z. Gu, A. Cichocki, and Y. Li, “Enhanced motor imagery training using a hybrid BCI with feedback,” IEEE Trans on Biomed Eng, vol. 62, no. 7, pp. 1706-1717, Jul. 2015.

- [39] M. Pregenzer and G. Pfurtscheller, “Frequency component selection for an EEG-based brain to computer interface”, IEEE Trans Rehabil Eng, vol. 7, no.4, pp. 413-419, Dec. 1999.

- [40] C. Neuper, R. Scherer, M. Reiner, and G. Pfurtscheller, “Imagery of motor actions: Differential effects of kinesthetic and visual-motor mode of imagery in single-trial EEG”. Cognitive Brain Research, vol. 25, no. 3, pp. 668-77, Dec. 2005.

- [41] R. M. Gibson, C. Srivas, A. M. Owen, and D. Cruse, “Complexity and familiarity enhance single-trial detectability of imagined movements with

electroencephalography”, Clinical Neurophysiology, 2014, vol. 125, no. 8, pp. 1556-1567, Aug. 2014.

- [42] K. Choi, “Electroencephalography (EEG)-based neurofeedback training for brain-computer interface (BCI),” Experimental Brain Research, vol. 231, no. 3, pp. 351-365, Sep. 2013.

- [43] L. Catalina, R. Manuel, R. S. Clara, M. Ingrid, and S. Magdalen, “Mu-rhythm changes during the planning of motor and motor imagery actions,” Neuropsychologia, vol. 51, no. 6, pp. 1019-1026, 2013.
- [44] L. He, Z. H. Gu, Y. Q. Li, and Z. L. Yu, “Classifying Motor Imagery EEG Signals by Iterative Channel Elimination according to Compound Weight,” Artificial Intelligence and Computational Intelligence Springer Berlin Heidelberg, pp. 71-78, 2010.
- [45] B. Nasihatkon, R. Boostani, and M. Z. Jahromi, “An efficient hybrid linear and kernel CSP approach for EEG feature extraction,” Neurocomputing, vol. 73, no. 1-3, pp. 432-437, Dec. 2009.
- [46] K. K. Ang, Z. Y. Chin, H. H. Zhang, and C.T. Guan, “Robust filter bank common spatial pattern (RFBCSP) in motor-imagery-based brain-computer interface,” Conf Proc IEEE Eng Med Biol Soc, pp.578-581, 2009.
- [47] C. Liu, H. B. Zhao, C. S. Li, and H. Wang, “Classification of ECoG motor imagery tasks based on CSP and SVM,” BMEI 3rd Int Conf on IEEE, pp.804-807, 2010.
- [48] V. N. Vapnik and V. Vapnik. (1998. Sep 16). Statistical learning theory, vol. 2, New York: Wiley.
- [49] J. Nocedal, S. J. Wright. (2006). Numerical Optimization, Springer New York.

- [50] Y. Yang, J. Wang, and Y. Yang, “Improving SVM classifier with prior knowledge in microcalcification detection1,” in Image Processing (ICIP), 19th IEEE International Conference on, pp. 2837-2840, 2012.

- [51] A. Kübler, B. Kotchoubey, J. Kaiser, J. R. Wolpaw, J, and N. Birbaumer, “Brain-computer communication: unlocking the locked-in,” Psychological Bulletin, vol.127, no. 3, pp. 358-375, May. 2001.

- [52] L. Wang, X. Zhang, X. Zhong, and Y. Zhang, “Analysis and classification of speech imagery EEG for BCI,” Biomed Sign Proc & Contr, vol. 8, no. 6, pp. 901-908, Nov. 2013.

- [53] G. Pfurtscheller and F. H. Lopes da Silva, “Event-related EEG/MEG synchronization and desynchronization: basic principles,” Clin Neurophysiol, vol. 110, no.11, pp. 1842-1857, Nov. 1999.

- [54] S. Ge, R. M. Wang, and D. C. Yu, “Classification of Four-Class Motor Imagery Employing Single-Channel Electroencephalography,” PLoS ONE, vol. 9, no. 6, pp. 1-7, Jun. 2014.
- [55] W. N. Kuhlman, “EEG feedback training: Enhancement of somatosensory cortical activity,” Electroencephalography and Clinical Neurophysiology, vol. 45, no. 2, pp. 290-294. Aug. 1978.
- [56] G. Pfurtscheller, A. Stancak Jr, and C. Neuper, “Event-related synchronization (ERS) in the alpha band–an electrophysiological correlate of cortical idling: A review,” International Journal of Psychophysiology, vol. 24, no. 1-2, pp. 39-46, Nov. 1996.

