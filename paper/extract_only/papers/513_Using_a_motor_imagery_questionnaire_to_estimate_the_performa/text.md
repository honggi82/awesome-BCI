[Figure 1]

### Vuckovic, A., and Osuagwu, B.A. (2013) Using a motor imagery questionnaire to estimate the performance of a brain–computer interface based on object oriented motor imagery. Clinical Neurophysiology. ISSN 1388-2457

Copyright © 2013 International Federation of Clinical Neurophysiology

A copy can be downloaded for personal non-commercial research or study, without prior permission or charge

Content must not be changed in any way or reproduced in any format or medium without the formal permission of the copyright holder(s)

When referring to this work, full bibliographic details must be given

### http://eprints.gla.ac.uk/81528/

Deposited on: 26 June 2013

Enlighten – Research publications by members of the University of Glasgow http://eprints.gla.ac.uk

## Using a Motor Imagery Questionnaire to Predict the Performance of a Brain-Computer Interface Based on Object Oriented Motor Imagery

Aleksandra Vuckovic1, Bethel A. Osuagwu1 1School of Engineering, University of Glasgow

Aleksandra Vuckovic School of Engineering, James Watt building (south) University of Glasgow, G12 8QQ Glasgow, UK Email: aleksandra.vuckovic@glasgow.ac.uk tel: +44 (0)141 330 3251 fax: +44(0)141 330 4343

Keywords: Brain-Computer Interface, BCI illiteracy, goal oriented imagination, kinaesthetic imagery, visual imagery, Motor imagery questionnaire

Disclosure: There are no conflicts of financial interests

HIGHLIGHTS:

- 1. Motor imagery (MI) questionnaires can be used as simple method to detect Brain-Computer Interface (BCI) illiteracy in MI based BCI
- 2. ‘Good’ and ‘poor’ BCI candidates prefer different forms of motor imagery
- 3. Object oriented motor imagery is influenced by a physical presence of the imagined object, changing features of the BCI classifier

Abstract:

Objectives: The primary objective was to test whether motor imagery (MI) questionnaires can be used to detect BCI ‘illiterate’. The second objective was to compare BCI classification accuracy between two types of MI: in the physical presence of the goal of an action (goal oriented imagery GOI) and without the physical presence of the goal (simple imagery SI).

Methods: Kinaesthetic (KI) and visual (VI) motor imagery questionnaires were administered to thirty (twenty) healthy volunteers. Their EEG was recorded during a cue-based, SI and GOI tasks.

Results: The strongest correlation (Pearson r2=0.53, p=1.6e5) (Pearson 0.66, p=1.39e-5) was found between KI and SI, followed by a moderate correlation KI and GOI (r2=0.33, p=0.001) (r2= 0.46, p=0.001) and a weak correlation between VI and SI (r2=0.21, p=0.022) (r2=0.23, p= 0.03) and VI and GOI (r2=0.17, p=0.05) (r2=0.20, p=0.05). BCI classification accuracy was similar for SI (71.1±7.8%) (68.6 6.1%) and GOI (70.5±5.9%) (69.7 4.9%), but GOI improved the classification accuracy in ‘poor’ imagers and reduced the classification accuracy in ‘good’ imagers. Classification features used in SI and GOI were different in 70% (75%) of participants. People with the lowest KI scores had also the smallest reduction of the sensory-motor rhythm during MI.

Conclusion: The KI score can be used as a pre-test to predict the performance of a MI based BCI. The physical presence of the object of an action facilitates motor imagination in poor imagers. Significance: In BCI based on MI, in particular for assisted rehabilitation of the upper extremities.

- I. INTRODUCTION

Motor imagination (MI) is a dynamic state in which the presentation of a specific motor action is internally activated without a motor output [Mulder 2007]. MI activates the same brain area as real (overt) movements [Jeannerod 2001, Decety 1996], following the same dynamics described by temporal regularity, programming rules, and the encoding of biomechanical constraints.

A very important property of MI is that one can vividly imagine a motor action that he/she cannot perform. A MI has therefore been widely used for training purposes, with sportsmen and musicians [Hall et al. 1998, Hall 2001, Langheim et al. 2002, Lotze and Halsbrand 2006, Guillot et al. 2010a], and in the rehabilitation of patients who cannot perform active movements following stroke, spinal cord injury (SCI) or chronic intractable pain [Moseley 2004, Butler and Page 2006, Mulder 2007, Page et al. 2009, Grangeon et al. 2010, Malouin 2010]. In these studies patients were verbally guided to imagine some functional, object oriented task for which they could not produce a satisfactory overt movement, such as reaching or grasping an object. Patients achieved decreased reaching time, enhanced smoothness of a hand trajectory of their overt movements [Grangeon et al. 2010], increased Fugl-Meyer score and results of the Action Research Arm (ARA) test [Page et al.

- 2006] . Even though motor imagery can improve learning or re-learning of motor skills, it is much

dependant on a person’s ability to elicit mental images. This ability is characterised as a ‘vividness’ of imagery (i.e. clarity and richness) and its controllability, which depends on the person’s ability to perform the mental representation of an action (covert action) using the previous experience of an earlier overt action [Guillot et al. 2010b]. People vary greatly in their ability to imagine movements and this ability can be improved by practice [Hall 1985, Guillot et al. 2010b]. A recent study demonstrated that ‘poor’ and ‘good’ imagers recruit the corresponding anatomical substrates to a different extent, ‘good’ imagers recruiting only the cortico-striatal system while ‘poor’ imagers in addition recruiting the cortico-cerebellar system [Guillot et al. 2008].

Questionnaires have been commonly used to asses motor imagination ability [Isaac 1996, Malouin et al. 2008, Malouin et al. 2009, Hall et al. 2009]. Apart from questionnaires, autonomic system function measurements and mental chronometry are also considered a reliable measure of imagery ability [Decety et al. 1991, Malouin et al. 2008].

The most popular motor imagery questionnaire is Hall’s questionnaire [Hall and Pongrac 1983, Hall and Martin 1997]. The main problem in administering this questionnaire to patients is that it requires quite energetic movements, which need to be executed and subsequently imagined. For most patients with motor deficit, these tasks are impossible to perform and are also very hard to imagine. Therefore Malouin et al. [2007] developed a questionnaire adapted for people with motor

disabilities called ‘The Kinaesthetic and Visual Imagery Questionnaire’ (KVIQ), containing separate sets of questions for kinaesthetic and visual MI. All movements implemented in this questionnaire can be physically executed while sitting in a chair, thus additionally facilitating MI. KVIQ predicts a possibility that a part of the body can be paralysed (e.g. stroke and SCI patients) so it is a suitable questionnaire for BCI users [Malouin et al. 2008].

Both covert and overt motor actions modulate Sensory-Motor Rhythms (SMR), and cause a phenomenon known as ‘Event related synchronisation/desynchronisation’ (ERS/ERD). The ERS/ERD describes changes in the energy level of certain frequency bands of EEG signal as compared to a period before the motor task [Pfurtscheller and Aranibar 1977]. The ERS/ERD is closely related to a decrease in the peak of the power amplitude of the SMR, which has been suggested as an indicator of motor imagination ability [Blankertz et al 2010]. Intensity of ERS/ERD has also been related to MI, and has been seen to improve with practice [Neuper et al. 2009]. Injuries to the CNS may influence execution of both covert and overt movements [Malouin et al. 2008, Malouin et al. 2009, Maulouin and Richards 2010, Butler and Page 2006] that are accompanied with changes in the ERS/ERD response [Pfurtscheller et al. 1980, Enzinger et al. 2008, Silvoni et al. 2011, Vuckovic et al. 2011].

MI has often been used in Brain Computer Interface (BCI) paradigms to provide voluntary change of SMR which serves as a basis for generating control signals [Wolpaw et al. 2002, Pfurtscheller et al. 2000, Pfurtscheller et al. 2006b, Leeb et al. 2007, Erzinger et al. 2008]. This type of BCI typically relies on MI of different limbs, to utilise a spatially distinctive activation of the sensory-motor cortex. Therefore, ultimately, BCI classifiers rely on differences in ERS/ERD over different sites of the cortex, not only on ERS/ERD itself. Inherently this is related to the intensity of the power amplitude of the SMR in a relaxed state and a person’s ability to produce ERS/ERD during MI.

It is however an open question whether poor imagers (as defined by MI questionnaires) would also have a poor performance when using a MI-based BCI. The latter are often called BCI ‘illiterate’ [Guger et al. 2003, Blankertz et al. 2006]. BCI ‘illiteracy’ is a common problem in BCI not restricted to MI paradigms [Daum et al. 1993, Guger et al. 2003, Guger et al. 2009, Allison et al. 2010]. Each type of BCI systems has its own ‘illiterates’ and approaches to analyse the problem of ‘illiteracy’ depends on the underlying neurophysiologic phenomena. Here we focus only on MI based BCI systems. There have been several studies attempting to define suitable candidates for MI based BCI.

Blankertz et al. [2010] suggested recording a brief EEG session in a relaxed state with eyes open, to detect power amplitude of SMR in the ‘idle’ state. They showed good correlation between the power amplitude and subsequent BCI classification accuracy in subjects performing cue-based

imagination with feedback. The same group suggested a simpler method for detecting BCI ‘illiteracy’, using a questionnaire based on ‘locus of control of reinforcement’ to detect persons who have a positive attitude towards technology and therefore have a better chance to learn how to use an on-line BCI [Burde and Blankertz 2006]. This questionnaire does not however directly deal with imagination ability, but it assumes that users can achieve sufficient off-line classification accuracy. Visual motor imagery questionnaires have been used to detect correlations between visual imagery and the brain activity recorded by fMRI [Cui et al. 2007]. Although a good correlation was found between a visual imagery and the degree of activation of the occipital area, both the type of imagery and the recording technique are not very practical for BCI. In a study by Neuper at al. [2009] participants were tested with a ‘Vividness of mental imagery questionnaire’ but correlation between the results of the questionnaire and BCI classification was not found.

Although BCI has initially been developed to assist communication in severely disabled persons, MI based BCI has a potentially wider application in motor rehabilitation [Pfurtscheller and Neuper 2006, Dobkin 2007]. While the exact mental strategy is less important for BCI used for communication purposes, the type of MI is relevant for BCI used for motor rehabilitation. The MI used in rehabilitation is goal oriented imagination such as grasping an object. Control of rehabilitation devices or neural prostheses with the aid of BCI differs from a general purpose BCI because the user can simultaneously observe his/her own limb and the goal of an action (e.g. a mug on a table). BCI used in rehabilitation of the upper extremities in people with an injury to the Central Nervous System (CNS) serves a dual function: to provide a feedback on the quality of imagination, promoting neurorehabilitation, and to provide control of devices such as an electrical muscle stimulator or a robot used in hand and arm therapy. BCI based on goal oriented imagination has already been demonstrated in chronic SCI patients for controlling neural prostheses [Pfurtscheller et al. 2000, Encinger et al. 2008]. It was also shown that better classification accuracy can be achieved with realistic goal oriented feedback (spatial navigation) than with an abstract alternative (e.g. a smiley) [Leeb et al. 2007]. However a study by Neuper et al. [2009] showed that there is no difference between controlling an abstract object (an arrow) and the highly realistic presentation of a hand (a hand reaching for a mug). In that study patients were controlling an object on a screen so it more likely that they applied visual rather than kinaesthetic imagery. Kinaesthetic imagery would be easier to experience from the first person perspective, when one imagines movements of one’s own hand. In [Pichiorri et al. 2011] two smaller groups of able-bodied volunteers were compared, one training imaginary fist clenching and the other imagining some goal oriented action of the hand. Larger Motor Evoked Potential (MEP) amplitude evoked by Transcranial Magnetic Stimulation (TMS), during MI pre- and post-training was noticed in the latter group, accompanied with a larger muscle map volume of the thumb muscle opponens pollicis.

This demonstrates the importance of goal (object) oriented MI for activation of the motor cortex, which is relevant for rehabilitation of movements.

In all of these studies the goal of an action was either imagined or presented as an image. It is to be expected that the presence of a real, physical goal would provide extra sensory cues and improve goal oriented imagination by improving the controllability of the imagined task (e.g. precision and timing). To our best knowledge, there are no studies investigating how different forms of presentation of the goal of an action (imaginary or real) influence MI. The presence of a real physical goal (e.g. a mug on a table) would make a MI based BCI suitable for rehabilitation, otherwise the BCI would be a more general one commonly used for communication and control.

In this study we aim to address two hypotheses. The first hypothesis is that there is a correlation between BCI classification accuracy and the outcomes of a questionnaire for visual and kinaesthetic motor imagery, because they should test the same phenomena. If such a correlation exists, then questionnaires could be used as a pre-test for detecting ‘very good’ or ‘very poor’ candidates for BCI. The second hypothesis is that there is a measurable difference in EEG in two MI paradigms: motor imagination towards a physically present goal of the action (neurorehabilitation) and motor imagination without a physically present goal of the action (communication and control). The presence of an object should improve the vividness of kinaesthetic imagery and result in increased accuracy of the BCI classifier. Results of this study might be relevant for motor rehabilitation of upper extremities, based on BCI assisted motor imagination.

- II METHODS

- 2.1 Questionnaires

Thirty (Twenty) right handed subjects (11 females, 19 males, mean age 25.3±8.4) (8 females, 12 males, mean age 27.9 7.1) participated in the study, approved by the College of Life Sciences, Glasgow University Ethical Committee.

Before starting the EEG experimental session, the participants were tested for their handedness using ‘the Edinburgh Handedness Inventory’ [Oldfiled 1970] and for their level of visual and kinaesthetic motor imagery using the KVIQ questionnaire [Malouin et al. 2007].

KVIQ is divided into tests of visual and of kinaesthetic motor imagery. Visual and Kinaesthetic imagery tests contained 17 questions each. A specific movement was presented verbally and participants were asked to perform a real movement first and subsequently to visualise the same movement from the first person perspective (visual imagery VI) or to imagine the proprioceptive sensation of a movement (kinaesthetic imagery KI). There were five grades to describe imagination,

ranging from ‘no image’ to ‘image as clear as seeing’ for VI, i.e. ‘no sensation’ to ‘as intense as executing the action’ for KI. In this paper, these five grades were called ‘No Imagery’=1; ‘Poor’=2; ‘Moderate=3’; ‘Good’=4 and ‘Excellent’=5.

- 2.2. The Experimental Paradigm

Participant were comfortably seated by a desk, their nose tips approximately 1.5 m from the computer screen. The front side of the desk was in a V shape so that the participants could keep their forearms on the desk on the side of their body and their hands in front of them. Participants were instructed to look at the centre of a computer screen in front of them, to follow the cue and to minimise eye movement artefacts. Therefore they had their hands in their filed of the peripheral vision. At t=0s a blank screen was presented on a computer screen in front of the participant (Fig.

- 1). At t=2s a warning sign (a cross) was presented in the centre of the computer screen, and remained until the end of the 7th second. At t=3s an arrow, pointing to the left or to the right, corresponding to hand grasp of the left or the right hand, appeared on the screen and stayed there for 1.25s. Participants were asked to perform real or imaginary movements of their hands from t=3s until the cross disappeared from the screen at t=7s, that is 4s in total. The next warning sign (a cross) appeared at a random interval 3-5s after the previous cross disappeared.

[Figure 1 about here] Real and imagined movements were divided into separate smaller runs. During a real movement run participants were asked to perform a lateral grasp of mugs placed beside the left and the right hands (Fig 2a). They were asked to repeat opening and closing of their hands (without moving them away from the mug) rather then performing one sustained grasp for 4 sec.

Participants performed MI under two conditions separated into different runs, here called ‘simple imagination’ (SI) and ‘goal-oriented imagination’ (GOI). In both cases participants were instructed to perform kinaesthetic imagery (Fig. 2).

Under GOI condition participants were asked to imagine the lateral grasp while the mugs were on the table close to the participant’s hands (Fig. 2b). Their hands were on the desk with palms down, on the desk. Although this was not the same position of the hands as during the real movements, it was chosen because participants were often tempted to perform real movements when their palms were facing the mug.

Under the SI condition, the mugs were removed and participants were asked to repeat the imagination. Again, their hands were on the desk with their palms down (Fig. 2c).

Each run of real movements comprised 15 trials for the left and 15 trials for the right hand. Each trial of the MI comprised 10 trials for the left and 10 trials for the right hand. There were in total three runs for real movements, eight runs for SI and eight runs for GOI. The order of different types

of trials (real, SI and GOI) was randomised. The purpose of real movement runs was to calculate ERS/ERD maps [Pfurtscheller and Aranibar 1977] and to compare them with ERS/ERD maps during the two MI tasks. A smaller number of real movement runs was chosen to reduce the overall duration of the experiment. Real movements were not used for classification purposes.

[Figure 2. about there]

- 2.3. EEG Recording

EEG was recorded using a 16 channel g.USBamp (Guger technologies, Austria). EEG was recorded from 3 sites bipolarly CF4-CP4, CFz-CPz and CF3-CP3, covering the sensory-motor cortex of both hands and legs. These recording sites are often used for BCI classification of right and left hand movements [Pfurtscheller et al. 2000, Pfurtscheller and Neuper 2006, Neuper et al. 2009]. The impedance was kept below 5 k . Sampling frequency was 256 samples/s, and EEG was filtered between 0.5 and 30 Hz (plus notch filter at 50 Hz). Vertical and horizontal right eye movements (EOG) and bipolar muscular activity (EMG) from the left and the right hand extensor muscles were recorded for the purpose of artefact detection. Due to bipolar EEG recording from the central area of the cortex there were typically only a few EOG contaminated epochs per subject. Likewise, unintentional hand movements were minimised by stabilising the forearms and the palms on the desk.

- 2.4. Feature Extraction and Classification

In order to keep a clear correlation between the features and the underlying neurophysiological processes, the chosen features were extracted from the following frequency bands: [0.5-2], [0.5-4], [2-4], [4-8], [8-10], [10-12], [8-12], [12-14], [14-16], [12-16], [16-20], [20-24], [16-24], [24-30] and [20-30] Hz. Frequency bands were chosen based on experience, avoiding two neurophysiological rhythms within one band and choosing a larger frequency band on the higher frequencies to compensate for the lower energy of the signal [Pfurtscheller and Lopes da Silva 1999].

Features chosen for classification were extracted from the logarithmic band powers for a chosen frequency band. The band powers were calculated using a FIR Butterworth filter or the 5th order. Features were the values of band powers calculated over a 1s window shifted for 7/8s over a whole 4s period during MI. This gave 31 overlapping 1s long windows, for each frequency band, from which features were extracted. Classification was performed for each time window and the best one was chosen (though the actual time of the window is not presented). For each person and each experimental condition, two frequency bands giving the best classification accuracy were found by

testing combinations for each of two (non-overlapping) frequency bands. The combination of the two best frequency bands was common for all three channels. That provided 2*3= 6 features in total used to build a BCI classifier.

In addition BCI classification was performed using features from one frequency band, chosen from all frequency bands and common for all three channels (3 features in total). Results are presented for the frequency band that achieved the best classification accuracy. This was used to compare whether there is a difference between the ‘best’ frequency bands for SI and GOI. For 80 trials and 2 classes, a ‘chance’ level of 60% was adopted [Mueller-Putz 2008]. Classification accuracy above the chance level would provide a valid comparison of ‘the best’ single frequency between SI and GOI.

Feature classification was performed using a Fisher’s Linear Discriminate Analysis (LDA) [Duda et al. 2001]. A 10x10 cross validation procedure was adopted. This means that in each run a BCI classifier was trained on up to 72 features and tested on 8 features for each hand (this was the maximum number in case no trial was removed because of noise). A true positive rate (a ratio of correctly classified trials compared to total number of trials) was adopted as a measure of the classification accuracy. A mean value of true positive rate for the right and the left hand was presented Signal processing was performed using rtsBCI [Scherer 2005] and the BioSig Open source toolboxes in Matlab (Mathworks Inc, USA).

- 2.5 Off-line Analysis

ERS/ERD spectra [Pfurtscheller and Aranibar 1977, Pfurtscheller and Lopes da Silva 1999] were calculated based on FFT, and the reference period was a 1s long, from 0.5s to 1.5s prior to the warning sign. Statistical significance of the ERS/ERD values was determined by applying a tpercentile bootstrap algorithm [Graimann et al 2002] with a significance level =0.05.

Power spectral density PSD was obtained for the period t=0.5-1.5s (reference period) and for t=3-5s (movement imagination) and was averaged over trials for display and analysis purposes. The PSD has a characteristic ‘peak’ in the alpha frequency range that corresponds to the SMR. The peak is prominent in the relaxed state (reference period) while it drops during MI.

- 2.6 Statistical analysis

A Shapiro-Wilk test [Shapiro and Wilk 1965] of normality was performed, confirming normal distribution for kinaesthetic and visual imagery scores, classification accuracy for SI and GOI and a degree of handedness (p=0.05). To test the hypothesis of equality of means of the two groups, a paired t-test was performed.

Linear regression analysis Y K1 K 2 X was preformed to find the best fit curve between the classification accuracy and KI/VI score. A linear correlation between the two independent variables was calculated using the parametric Pearson test. All calculations were performed in Matlab.

- III RESULTS

- 3.1. 1. Kinaesthetic and Visual Imagery Scores

The mean value of the KI score across 30 (20) subjects was 3.4±0.8 (3.3 0.6) and for the VI score was 3.5±0.6 (3.4 0.6). This means, that on average, participants had moderate visual and kinaesthetic imagery. Participants’ individual imagery ability ranged from poor (KI 2) to good/excellent (KI=4.5) (Fig. 3, x axis). Only one participant had a VI score under 2, and none had a KI score under 2 because such a score (no imagination) is very rare among able-bodied people with intact proprioception [Malouin et al. 2007]. A paired t-test showed that there was no statistically significant difference between VI and KI (p=0.4) (p=0.5) In addition, results of the whole KI test were compared with the KI6 (scores for the left and the right hand only) and no statistically significant difference of means was found (paired t-test p=0.7) (paired t-test p=0.9).

- 3.1. 2. BCI classification accuracy for SI and GOI

The mean classification accuracy for SI between the left and the right hand, based on the two best frequency bands was 71.1±7.8% (68.6 6.1%) and the corresponding classification accuracy for GOI was 70.5±5.9% (69.7 4.9%). There was no statistically significant significance between SI and GOI (paired t test p=0.8) (paired t test p=0.26).

When only one frequency band (3 features) was used, the classification accuracy for SI was 68.9 6.8% and for GOI was 67.7 8%, and hence greater than just by the chance.

The mean level of handedness was 89.2 7.1% (81.8 16.1%), (almost 20 out of 30 participants were 100% right handed) so no correlation was found between the level of handedness and the classification accuracy.

3.1.3. Correlation Between QVKI Scores and Classification Accuracy

The highest correlation between imagination ability and classification accuracy was found between the KI score and BCI classifier based on SI, (Pearson r2=0.56 p=2.9e-5) (Pearson r2= 0.66 1.39e-5), which means that 56% (66%) of the variance in classification accuracy could be explained by each participant’s MI ability. The slope of the linearly fitting curve was K2=8.2 (7.6) (Fig. 3a, solid line). To test whether it was sufficient to test imagery ability for the upper limbs only, correlation was

calculated between SI and KI6. This correlation coefficients was moderate (Pearson r2=0.41, p=0.001) (Pearson r2=0.459, p=0.001), showing that administering the whole KI test gives more complete results.

A moderate correlation was also found between the KI score and the BCI classifier based on GOI (Pearson, r2=0.35, p=0.0014) (Pearson, r2=0.42, p=0.0018) The slope of the linearly fitting curve for this correlation K2=4.8 (4.9) was smaller than the slope of the linearly fitting curve for the correlation between KI and SI (Figure 3a, dashed-dot line).

A weak correlation existed between the VI score and SI (Pearson, r2=0.21, p=0.022), (Pearson, r2=0.23, p=0.03), K2=5.1 and between the VI score and GOI (Pearson, r2=0.17, p=0.05) (Pearson, r2=0.20, p=0.05), K2=3.3 (Fig 3b).

[Figure 3 about here]

- 3.2 Relationship Between PSD and Kinaesthetic Imagery.

The PSD of the EEG signal was calculated for the reference period and for a period of motor imagination. In participants with moderate and good imagery, a drop of SMR peak during MI could be observed over all three electrode sites. In participants with poor KI, as in the one shown in Fig.4, there was no clear difference between PSD in the reference period and during MI, over some of the recording sites. Seven (five) participants with the lowest classification accuracy had a barely recognisable alpha peak over the sensory-motor area of the right or the left hemisphere both during the reference period and during imagination of movement (lack of ‘peak’ SMR in the PSD), as shown in graphs on the left in Fig.4. In the other two electrode locations the alpha peak is visible but is similar during the reference period and MI.

A lack of change in SMR effectively resulted in very weak ERD upon MI. A lack of ERD over CF4-CP4 in the alpha band resulted in larger similarity in MI of the left and the right hand (as ERD was different over the other two locations only) and lower classification accuracy. Thus persons with low SMR peak and small SMR reduction had the lowest classification accuracy for the BCI system.

[Figure 4 about here]

- 3.3 Simple vs. Goal-Oriented Imagination

The classification accuracy was similar for SI and GOI. Therefore based on this result, at the group level, it was not possible to draw conclusions about the influence of the physical target on imagination. However, from the linear interpolations in Fig.3a it can be seen that the GOI

interpolation has a smaller slope, because the GOI improved a classification accuracy in persons with a low KI score, while in persons with a higher KI score the classification accuracy decreased.

The dominant frequency band used to classify left vs. right hand was compared between the SI and the GOI strategy (Fig.5). Only 30 % (25%) participants had the same dominant frequency for both SI and GOI, and they were mostly in the ‘very good’ imagers group (graph on the right in Fig. 3a). Participants with the worst imaginary ability (‘poor’ imagers, on the left) had different dominant frequency bands for SI and GOI. It is interesting that ‘good’ imagers who had the same dominant frequency band for SI and GOI had worse classification results for GOI than for SI (Figure3a). In contrast, ‘poor’ imagers achieved better classification accuracy for GOI than for SI.

On the level of the whole group, there was no clear tendency towards an increase or a decrease in the dominant frequency when SI was compared with the GOI, probably because of different tendencies in ‘poor’ and ‘good’ imagers. In 9 participants (6 participants) the dominant frequency was lower for GOI than for SI, in 9 (8) it was higher, in 4 participants (2 participants) the dominant frequencies for SI and GOI partially overlapped, and in 8 participants (5 participants) they were identical for SI and GOI.

The width of the dominant frequency band was also compared between SI and GOI. In 11 participants (9 participants) participants the width of the dominant frequency band for GOI was smaller than for SI (typically reduced from the 4Hz bandwidth to the 2Hz bandwidth), in 15 participants (9 participants) it stayed the same and only in 4 participants (2 participants) (13% participants) it was larger for GOI.

- [Figure 5 about here]

In addition, when the best features of the GOI classifier were used for the SI classifier, the classification accuracy decreased on average for 5.0% (4.5%). A paired t-test between these two results, for the SI classifier, showed a statistically significant difference p=0.009 (p=0.012).

- [Figure 6 about here]

Individual ERS/ERD maps of two representative participants, one with a high KI score (4.5) and the other with a low KI score (2.1) over the electrode location CF3-CP3, during various motor tasks of the right hand, are shown in Fig 6. For a person with a low KI score (Fig. 6a) a wide spread ERD of the sensory-motor rhythms (alpha and beta) is visible during the overt (executed) movement. During SI, the ERD can be seen in the delta and the theta bands only. With the GOI, the ERD is visible in the SMR, which was not sustained but existed only during the first second (the task was to imagine a lateral grasp repeatedly for 4s). The ERD in the lowest frequency range (<5Hz) is less intense than in the SI case. Fig 6b shows ERS/ERD for the same tasks as in Fig. 6a but for a person

with the highest KI score (KI=4.5). During movement execution a well defined ERD over 10-15 Hz range can be seen. During SI, the ERD can be seen in two distinctive bands, in the alpha and the beta range. For the GOI, the ERD is less intensive and less sustained in the beta frequency range than for SI. While GOI seemed to facilitate MI in a person with low KI score, it seemed to cause distraction and less sustained ERD in person with a high KI score.

- IV DISUCSSION AND CONCLUSIONS

The results of this study showed that a motor imagery questionnaire can be used as a preliminary test to differentiate between ‘good’ and ‘poor’ candidates for a MI based BCI, and to decide on the best MI strategy.

Correlation between questionnaires and BCI was tested for two types of motor imagery (visual VI and kinaesthetic KI) and for two types of MI: simple (SI) and goal oriented (GOI). A strong correlation between the outcomes of the motor imagery questionnaire and the BCI classifier was found for the KI score and the classifier based on the SI while a medium correlation was found between the KI score and the classifier based on the GOI. There was a weak correlation between the VI score and both the SI and the GOI based classifier. It was unsurprising that KI showed a higher correlation with BCI because participants were instructed to perform kinaesthetic rather than visual imagery.

A somewhat unexpected result was that the physical presence of the goal of an imagined action had the opposite effect with ‘good’ compared to ‘poor’ imagers. While it helped ‘poor’ imagers to focus on the imagined action, resulting in an increase in classification accuracy, it ‘disturbed’ good imagers reducing their classification accuracy. As a result, the correlation between the BCI classifier and the KI score was lower for the GOI task than for the SI task. A possible explanation might be that very ‘good’ imagers already had good kinaesthetic imagination and the presence of an object diverted them from kinaesthetic to a visual imagery, which activated different areas of the cortex [Neuper et al. 2005, Guillot et al. 2009]. This hypothesis was supported by the results of the analysis of the ERS/ERD maps of participants with the worst and best KI during SI and GOI. While the GOI caused facilitation of the SMR in people with a low KI score, it caused a reduction in the ERD intensity of the SMR in people with a high KI score. This might be related to how ‘good’ imagers (e.g. sportsmen) and ‘poor’ imagers (e.g. stroke patients) practice motor imagery. Sportsmen, e.g. tennis player, do not need to look at a tennis ball to imagine a forehand. On the contrary, practicing a reaching task after stroke is often facilitated by the physical presence of the object [Page et al. 2009] or its representation in virtual reality [Gaggioli et al.2009].

In a study by Neuper et al [2009] no correlation was found between the ‘Vividness of Mental Imagery Questionnaire’ [Isaac et al. 1996] and classification of the BCI. The questionnaire used in

that study favoured visual imagery by asking patients to perform complex tasks (e.g. sliding on ice, throwing a stone into the water). The questionnaire was adequate for that particular study because the MI task was visual (to move an abstract or realistic image of a hand on the computer screen). In our study participants had to imagine movements of their own limbs, concentrating on kinaesthetic imagery and the questionnaire differentiated between kinaesthetic and visual imagery. Because of different MI strategies it was not possible to directly compare results of Neuper et al. study and the current one. However results of Neuper et al. study are not in disagreement with the current study as we also found only moderate correlation between a visual imagery scores and the output of the BCI classifier.

Although a high classification accuracy is in general desirable in any BCI system, from a rehabilitation point of view, it is more important to increase the intensity of the SMR because motor imagery can be practiced with one hand at a time. However improved BCI classification accuracy (in e.g. patients with stroke) should indicate proper activation of the contra-lateral cortex, that may also serve as an indication of recovery. BCI can be used for motor rehabilitation of the other groups of patients with injuries to the Central Nervous System. Incomplete Spinal Cord injured (SCI) patients could also benefit from BCI based motor therapy. MI-based BCI can be used in SCI patients to enable patient-controlled functional electrical therapy to restore hand function early after the injury [Vuckovic at al. 2011b] or for controlling a permanent hand orthoses [Enzinger et al. 2008].

Another result from this study, namely that people with a lower KI score have a lower intensity of the SMI peak, is in accordance with a study by Blankertz et al. [2010]. In that study correlation between the power amplitude of the SMR over the C3+C4 area of the cortex and the classification accuracy of a BCI classifier based on ERS/ERD was demonstrated, showing that people with a lower SMR in a relaxed state exhibit worse BCI performance. These people would to some extent correspond to poor imagers in our study, as they would have lower C3 and/or C4 SMR than good imagers. This study was based on an off-line classification while a study by [Blankertz et al. 2010] was based on an on-line task with feedback. However Burde and Blankertz [2006] demonstrated that feedback performance depends on the person’s ‘locus of control’ which is a confounding factor of an on-line study.

The results of the current study also showed that the optimal features chosen for the classifier could be modified by changes in the MI strategy. Swapping the ‘optimal’ features of the classifiers based on SI and GOI caused a significant decrease in classification accuracy. The effect of changes in the MI paradigm on classification accuracy was previously noticed in studies where off-line chosen features were used for on-line BCI with feedback [Vidaurre et al. 2010] or when simple on-

line feedback was replaced with a Virtual Reality environment [Pfurtscheller at al.2006b, Leeb et al.

- 2007]. The experimental setup to investigate a GOI was not ideal because the hand and mug were in the

peripheral visual field, due to a cue-based task. The palm was not facing the mug but faced down on the desk, to suppress unintentional hand movements. The ideal setup for this kind of experiment would be asynchronous BCI but that would require extensive training of a large number of participants. In addition off-line classification results in ‘poor’ imagers were too low (close to classification accuracy by chance) to be used as initial features for on-line training.

To some extent, GOI exhibits similarities to ‘quasi movements’ [Nikulin et al. 2008] in which persons have to suppress their muscle activity to a level that cannot be detected by EMG. Quasi movements elicit stronger ERD compared to imagination.

In current study a very simple classification algorithm was used because the main focus of the study was not on the classification algorithm, but rather on the experimental paradigms. Using more sophisticated algorithms or additional recording sites would lead to improved classification accuracy [Blankertz et al. 2008, Pfurtscheller et al. 2008, Vidaure and Blanertz 2010]. Even so, a classification accuracy of 71.1% for GOI and 70.5% for SI (69.7% GOI and 68.6% SI) is in agreement with results from studies performed on a larger number of untrained subjects [Guger et al. 2003].

- V SIGNIFICANCE This study demonstrates that the KVIQ scores could be helpful to find the best MI strategy for

any particular individual for a BCI, as a first step before testing BCI performance.

The motor imagery paradigm influences imagination ability and modifies the optimal parameters chosen for the BCI classifier. The physical presence of the goal of imagined action improves the classification accuracy of BCI in ‘poor’ imagers. Results of this study might be relevant for patients receiving BCI based hand therapy as they are likely to have reduced ability to imagine movements of their impaired limbs.

- VI REFERENCES

Allison B, Luth T, Valbuena D, Teymourian A, Volosyak I, Graser A. BCI Demographics: How Many (and What Kinds of) People Can Use an SSVEP BCI? EEE Trans Neural Syst Rehabil Eng. 2010 Apr;18(2):107-16

Birbaumer N. Kübler A, Ghanayim N, Hinterberger T, Perelmouter J, Kaiser J, et al. .The thought translation device (ttd) for completely paralyzed patients. IEEE Transactions on Rehabilitation Engineering, 8(2):190–193, 2000.

Blankertz B, Losch F, Krauledat M, Dornhege G, Curio G, Müller KR. The Berlin Brain--Computer Interface: accurate performance from first-session in BCI-naïve subjects. IEEE Trans Biomed Eng. 2008; Oct;55(10):2452-62.

Blankertz B, Sannelli C, Halder S, Hammer EM, Kübler A, Müller KR, et al. Neurophysiological predictor of SMR-based BCI performance. Neuroimage. 2010; 51: 1303-1309

Burde W, Blankertz B. Is the locus of control or reinforcement a predictor of brain-computer interface performace? Proc of 3rd Intern Brain-Computer interface workshop , Graz, Austria. Ed Muller-Putz 2006; 76-77.

Butler AJ, Page SJ. Mental practice with motor imagery: evidence for motor recovery and cortical reorganization after stroke. Arch Phys Med Rehabil. 2006 Dec; 87(12 Suppl 2):S2-11.

Cui X, Jeter CB, Yang D, Montague PR, Eagleman DM. Vividness of mental imagery: individual variability can be measured objectively. Vision Res. 2007 Feb;47(4):474-8.

Daum I, Rockstroh B, Birbaumer N, Elbert T, Canavan A, Lutzenberger W. Behavioural treatment of slow cortical potentials in intractable epilepsy: neuropsychological predictors of outcome. J Neurol Neurosurg Psychiatry. 1993 Jan;56(1):94-7.

Decety J, Jeannerod M, Germain M, Pastene J. Vegetative response during imagined movement is

proportional to mental effort. Behav Brain Res. 1991 Jan; 31;42(1):1-5. Decety J.The neurophysiological basis of motor imagery.Behav Brain Res. 1996 May;77(1-2):45-52 Dobkin BH. Brain-computer interface technology as a tool to augment plasticity and outcomes for

neurological rehabilitation. J Physiol. 2007 Mar 15;579(Pt 3):637-42. Duda RO, Hart PE, Stork DG. Pattern Classification. A Wiley-Interscience Publication. 2nd edition 2001. Enzinger C, Ropele S, Fazekas F, Loitfelder M, Gorani F, Seifert T, et al. . Brain motor system function in a

patient with complete spinal cord injury following extensive brain-computer interface training. Exp Brain Res. 2008 Sep;190(2):215-23.

Gaggioli A, Morganti F, Meneghini A, Pozzato I, Greggio G, Pigatto M, et al. . Computer-guided mental practice in neurorehabilitation. Stud Health Technol Inform. 2009;145:195-208.

Graimann B, Huggins JE, Levine SP, Pfurtscheller G. Visualization of significant ERS/ERDpatterns in multichannel EEG and ECoG data. Clin Neurophysiol. 2002 Jan;113(1):43-7.

Grangeon M, Guillot A, Sancho PO, Picot M, Revol P, Rode G, et al. Rehabilitation of the elbow extension with motor imagery in a patient with quadriplegia after tendon transfer. Arch Phys Med Rehabil. 2010 Jul;91(7):1143-6.

Guger C, Edlinger G, Harkam W, Niedermayer I, Pfurtscheller G. How many people are able to operate an EEG-based brain-computer interface (BCI)? IEEE Trans Neural Syst Rehabil Eng. 2003 Jun;11(2):145-7.

Guger C, Daban S, Sellers E, Holzner C, Krausz G, Carabalona R, et al. . How many people are able to control a P300-based brain-computer interface (BCI)? Neurosci Lett. 2009 Oct 2;462(1):94-8.

Guillot A, Collet C, Nguyen VA, Malouin F, Richards C, Doyon J. Functional neuroanatomical networks associated with expertise in motor imagery. Neuroimage. 2008 Jul 15;41(4):1471-83.

Guillot A, Collet C, Nguyen VA, Malouin F, Richards C, Doyon J. Brain activity during visual versus kinesthetic imagery: an fMRI study. Hum Brain Mapp. 2009 Jul;30(7):2157-72

Guillot A, Debarnot U, Louis M, Hoyek N, Collet C. Motor imagery and motor performance: evidence from the sport science literature. In The neuropsyhological foundations of mental and motor imagery. Guillo A and Collet C. Editors, Oxford University Press, 2010a: 215-226.

Guillot A, Louis M, Collet C. Neurophysiological substrates of motor imagery ability. In The neuropsyhological foundations of mental and motor imagery. Guillo A and Collet C. Editors, Oxford University Press, 2010b: 109-126.

Hall CR, Pongrac J. Movement Imagery Questionnaire. London (Canada): The University of Western Ontario, Faculty of PhysicalEducation; 1983.

Hall CR. Individual differences in the mental practice and imagery of motor skill performance. Can J Appl Sport Sci. 1985 Dec;10(4):17S-21S

Hall CR, Martin KA. Measuring movement imagery abilities: a revision of the Movement Imagery Questionnaire. J Ment Imagery 1997;21:143–54.

Hall, C, Mack, D, Paivio, A, Hausenblas, H. Imagery use by athletes: Development of the Sport Imagery Questionnaire. International Journal of Sport Psychology, 1998; 29: 73–89

Hall, CR,. Imagery in sport and exercise. In R. N. Singer, H. A. Hausenblas, & C. M. Janelle editors . Handbook of sport psychology. New York: Wiley, 2001: 529-549

Hall CR, Munroe-Chandler KJ, Cumming J, Law B, Ramsey R, Murphy L. Imagery and observational learning use and their relationship to sport confidence. Sports Sci. 2009 Feb 15;27(4):327-37.

Isaac IA Marks DF, Russell DG. An instrument for assessing imagery of movement: The Vividness of Movement Imagery Questionnaire (VMIQ). J Ment Imagery 1986;10:23–30.

Jeannerod M. Neural simulation of action: a unifying mechanism for motor cognition. Neuroimage. 2001 Jul;14(1 Pt 2):S103-9.

Kotchoubey B, Busch S, Strehl U, Birbaumer N. Changes in EEG power spectra during biofeedback of slow cortical potentials in epilepsy. Appl Psychophysiol Biofeedback. 1999 Dec;24(4):213-33.

Langheim, FJP, Callicott, JH, Mattey, VS, Duyn, JH, Weinberger, DR. Cortical systems associated with covert musical rehearsal. Neuroimage 2002; 16: 901–908.

Leeb R, Lee F, Keinrath C, Scherer R, Bischof H, Pfurtscheller G. Brain-computer communication: motivation, aim, and impact of exploring a virtual apartment. IEEE Trans Neural Syst Rehabil Eng. 2007 Dec;15(4):473-82

Lotze M, Halsband U. Motor imagery. J Physiol Paris. 2006 Jun;99(4-6):386-95. Malouin F, Richards CL, Durand A, Doyon J. Clinical assessment of motor imagery after stroke.

Neurorehabil Neural Repair. 2008 Jul-Aug;22(4):330-40.

Malouin F, Richards CL, Jackson PL, Lafleur MF, Durand A, Doyon J. The Kinaesthetic and Visual Imagery Questionnaire (KVIQ) for assessing motor imagery in persons with physical disabilities: a reliability and construct validity study. J Neurol Phys Ther. 2007 Mar;31(1):20-9.

Malouin F, Richards CL, Durand A, Descent M, Poiré D, Frémont P, Pelet S, Gresset J, Doyon J. Effects of practice, visual loss, limb amputation, and disuse on motor imagery vividness. Neurorehabil Neural Repair. 2009 Jun;23(5):449-63

Malouin F, Richards CL. Mental practice for relearning locomotor skills. Phys Ther. 2010 Feb;90(2):240-51. Moseley GL. Graded motor imagery is effective for long-standing complex regional pain syndrome: a

randomised controlled trial. Pain. 2004 Mar;108(1-2):192-8. Mueller-Putz G.R, Scherer R, Brunner C, Leeb R, Pfurtscheller G. Better than random? A closer look at BCI results. Int Journ of Electromagnetism. 2008; 10:52-55.

Mulder T. Motor imagery and action observation: cognitive tools for rehabilitation. J Neural Transm. 2007;114(10):1265-78.

Neuper C, Scherer R, Reiner M, Pfurtscheller G. Imagery of motor actions: differential effects of kinesthetic and visual-motor mode of imagery in single-trial EEG. Brain Res Cogn Brain Res. 2005 Dec;25(3):66877

Neuper C, Scherer R, Wriessnegger S, Pfurtscheller G. Motor imagery and action observation: modulation of sensorimotor brain rhythms during mental control of a brain-computer interface. Clin Neurophysiol. 2009 Feb;120(2):239-47.

Nikulin VV, Hohlefeld FU, Jacobs AM, Curio G. Quasi-movements: a novel motor-cognitive phenomenon. Neuropsychologia. 2008 Jan 31;46(2):727-42.

Oldfield RC. The assessment and analysis of handedness: the Edinburgh inventory. Neuropsychologia. 1971 Mar;9(1):97-113.

Page SJ, Szaflarski JP, Eliassen JC, Pan H, Cramer CS, Cortical Plasticity Following Motor Skill Learning During Mental Practice in Stroke. Neurorehabil Neural Repair. 2009 May ; 23(4): 382–388

Pichiorri F, De Vico Fallani F, Cincotti F, Babiloni F, Molinari M, Kleih SC, et al.. Sensorimotor rhythmbased brain-computer interface training: the impact on motor cortical responsiveness. J Neural Eng. 2011 Apr;8(2):025020

Pfurtscheller G, Aranibar A. Event-related cortical desynchronization detected by power measurements of scalp EEG. Electroencephalogr Clin Neurophysiol. 1977 Jun;42(6):817-26.

Pfurtscheller G, Aranibar A, Wege W. Changes in central EEG activity in relation to voluntary movement. II. Hemiplegic patients. Prog Brain Res. 1980;54:491-5.

Pfurtscheller G, Lopes da Silva FH. Event-related EEG/MEG synchronisation and desynchronisation: basic principles. Clin Neurophysiol. 1999;110:1842-57.

Pfurtscheller G, Guger C, Müller G, Krausz G, Neuper C. Brain oscillations control hand orthosis in a tetraplegic. Neurosci Lett. 2000 Oct 13;292(3):211-4

Pfurtscheller G, Neuper C. Future prospects of ERS/ERDin the context of brain-computer interface (BCI) developments. Prog Brain Res. 2006;159:433-7

Pfurtscheller G, Leeb R, Keinrath C, Friedman D, Neuper C, Guger C et al.. Walking from thought. Brain Res. 2006b Feb 3;1071(1):145-52.

Pfurtscheller G, Scherer R, Mueller-Putz GR , and Lopes da Silva FH, Short-lived brain state after cued motor imagery in naive subjects, European Journal of Neuroscience, 2008; 28: 1419–1426

Scherer R. rtsBCI – a collection of methods and functions for real-time data acquisition, storage, signal processing and visualization based on Matlab/Simulink. Available online: http://biosig.sf.net (accessed April 2012).

Silvoni S, Ramos-Murguialday A, Cavinato M, Volpato C, Cisotto G, Turolla A et al.. Brain-computer interface in stroke: a review of progress. Clin EEG Neurosci. 2011 Oct;42(4):245-52.

Shapiro, S. S. and Wilk, M. B. An analysis of variance test for normality (complete samples), Biometrika, 1965;52 (3/4): 591-611

Vidaurre C, Blankertz B. Towards a cure for BCI illiteracy. Brain Topogr. 2010 Jun;23(2):194-8.

Vuckovic, A, Hasan, MA, Nasseroleslami, B, Conway, BA, Allan, DB, and Fraser, M. Motor imagery in spinal cord injury with neuropathic pain. In: 4th International Symposium on Applied Sciences in Biomedical and Communication Technologies, doi:10.1145/2093698.2093866 26-29 Oct 2011, Barcelona, Spain.

Vuckovic A, Wallace L, Allan D.B. Hybrid BCI controlled FES for rehabilitation of the hand in acute tetraplegic patients UKIERI Workshop Fusion of Brain-Computer Interface and Assistive Robotics, University of Ulster, July 2011 (accessed 26.10.20120) abstract: http://eprints.ulster.ac.uk/23285/1/Proceedings_BCI-AR_2011_Workshop.pdf.

Wolpaw JR, Birbaumer N, McFarland DJ, Pfurtscheller G, Vaughan TM. Brain-computer interfaces for communication and control. Clin Neurophysiol. 2002 Jun;113(6):767-91.

#### FIGURE LEGENDS:

- Figure 1. The experimental paradigm. At t=0s a blank screen was presented followed by a warning sign at t=2s. The warning sign stayed until t=5s. At t=3s a cue appeared on the screen and stayed there for 1.25 s. Classification features were extracted from the period t=3s till t=7s.

- Figure 2. Three different tasks: (a) Real lateral grasp of a mug; (b) Imagination of a lateral grasp of a mug laying on a desk, called Goal Oriented Imagination (GOI); (c) Imagination of a lateral grasp with the mug being removed from the desk, called Simple Imagery (SI).

- Figure 3. (a) Classification accuracy as a function of KI score. Asterisks are for SI and diamonds for GOI. Asterisk and diamonds on the same KI scale correspond to the same person. Straight lines show linear interpolation of results for SI (solid) and for GOI (dashed); (b) Classification accuracy of SI as a function of VI score; straight lines show linear interpolation of results for SI (solid) and for GOI (dashed).

- Figure 4. A logarithmic power spectral density for a reference period (solid line) and during a simple motor imagination (dashed line) over three central electrode sites, Subject 4, KI score 2.7 (KI 2: Poor, 3: Moderate) Upper graphs are for left hand imagination and the lower graphs are for right hand imagination.
- Figure 5. The frequency value of the dominant frequency band as a function of KI score during SI (solid lines) and GOI (dashed lines). Values on the upper x axis show the absolute score (summation of scores across all 17 questions) while the lower x axis shows the normalised score (divided by 17, the total number of questions). A dashed and a solid line on the same scale (in a direction of the y axis) represent results from the same participant. In cases where frequency bands for SI and GOI imagination were identical or overlapping, they were presented with solid and dashed lines, close to each other, with the dashed line being on the right.
- Figure 6. ERS/ERD maps for right hand movements over the contraleteral hemisphere (CF3-CP3). The left column ‘REAL’ is for real movements, the middle column ‘SI’ is for simple imagery and the right column ‘GOI’ for goal oriented imagery. The upper row (a) is for a participant with the lowest KI score (‘poor’ imager, KI=2.1) and the lower row (b) is for a participant with the highest KI score (‘good’ imager KI=4.5).

TARGET

3-5 s

| |WARNING| |
|---|---|---|
| | | |

WARNING

Time (s)

0 2 4 6 7

5

- 1 3

FIGURE 1

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

# a b c

FIGURE 2

ClassificationAccuracy[%]

85

80

75

70

65

60

55

- 2 2.5 3 3.5 4 4.5

Poor Moderate Good

[KI]

(a)

ClassificationAccuracy[%]

85

80

75

70

65

60

[KI]

55

1.5 2 2.5 3 3.5 4 4.5

Poor Moderate Good

LEFT HAND SI

PSD [dB]

CF4-CP4 CFz-CPz CF3-CP3

10

0

[Hz]

0 0 0

20 40 20 40 20 40

RIGHT HAND SI

CF4-CP4 CFz-CPz CF3-CP3

PSD [dB]

10

0

[Hz]

20 40

0 20 40 0 20 40 0

FIGURE 4

[Hz] 30

25

20

15

10

5

0

35 40 45 50 55 60 65 70 75 80

[KI] 3 MODERATE

2 POOR

4 GOOD

5 [KI] EXCELLENT

FIGURE 5

30

30

30

[Figure 11]

1.5

[Figure 12]

[Figure 13]

[Figure 14]

[Hz]

25

##### REAL SI GOI

25

25

20

20

20

15

15

15

10

10

10

5

5

5

- -1.5

- 0

[Figure 15]

- 1.5

- -1.5

1 2 3 4 5 6 7 [s]

[s] [s]

1 2 3 4 5 6 7

1 2 3 4 5 6 7

- (a)
- (b)

30

30

[Figure 16]

30

[Figure 17]

[Figure 18]

[Hz]

25

25

25

REAL SI

GOI

20

20

20

0

15

15

15

10

10

10

5

5

5

1 2 3 4 5 6 7 [s] 1 2 3 4 5 6 7 [s] 1 2 3 4 5 6 7 [s]

FIGURE 6

