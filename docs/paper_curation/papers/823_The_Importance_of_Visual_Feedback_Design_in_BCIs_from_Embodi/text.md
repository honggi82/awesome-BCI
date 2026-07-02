[Figure 2]

a11111

[Figure 3]

OPEN ACCESS

Citation: Alimardani M, Nishio S, Ishiguro H (2016) The Importance of Visual Feedback Design in BCIs; from Embodiment to Motor Imagery Learning. PLoS ONE 11(9): e0161945. doi:10.1371/journal. pone.0161945

Editor: Dewen Hu, National University of Defense Technology College of Mechatronic Engineering and Automation, CHINA

Received: April 23, 2016 Accepted: August 15, 2016 Published: September 6, 2016 Copyright: © 2016 Alimardani et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. Data Availability Statement: All data files are accessible from the ATR-HIL database (http:// gemmyserv.atr.jp) and are available in the Supporting Information. Funding: This research was supported by KAKENHI (https://www.jsps.go.jp/english/e-grants/) (Grant-inAid for Scientific Research) grant number 25220004 to HI, 26540109 to SN and 15F15046 to MA. This research was also supported by ImPACT Program of Council for Science, Technology and Innovation (Cabinet Office, Government of Japan) to SN. The funders had no role in study design, data collection

RESEARCH ARTICLE

# The Importance of Visual Feedback Design in BCIs; from Embodiment to Motor Imagery Learning

Maryam Alimardani1*, Shuichi Nishio2, Hiroshi Ishiguro2,3

1 Department of General Systems Studies, Graduate School of Arts and Sciences, University of Tokyo, Tokyo, Japan, 2 Advanced Telecommunications Research Institute International (ATR), Kyoto, Japan, 3 Department of Systems Innovation, Graduate School of Engineering Science, Osaka University, Osaka, Japan

* maryam@ardbeg.c.u-tokyo.ac.jp

## Abstract

Brain computer interfaces (BCIs) have been developed and implemented in many areas as a new communication channel between the human brain and external devices. Despite their rapid growth and broad popularity, the inaccurate performance and cost of user-training are yet the main issues that prevent their application out of the research and clinical environment. We previously introduced a BCI system for the control of a very humanlike android that could raise a sense of embodiment and agency in the operators only by imagining a movement (motor imagery) and watching the robot perform it. Also using the same setup, we further discovered that the positive bias of subjects’ performance both increased their sensation of embodiment and improved their motor imagery skills in a short period. In this work, we studied the shared mechanism between the experience of embodiment and motor imagery. We compared the trend of motor imagery learning when two groups of subjects BCI-operated different looking robots, a very humanlike android’s hands and a pair of metallic gripper. Although our experiments did not show a significant change of learning between the two groups immediately during one session, the android group revealed better motor imagery skills in the follow up session when both groups repeated the task using the non-humanlike gripper. This result shows that motor imagery skills learnt during the BCIoperation of humanlike hands are more robust to time and visual feedback changes. We discuss the role of embodiment and mirror neuron system in such outcome and propose the application of androids for efficient BCI training.

Introduction

Brain computer interfaces (BCIs) are the new communication devices that translate brain signals into meaningful commands for control of external machines [1–3]. Among different types of BCIs, electroencephalography (EEG)-based BCIs are most commonly used due to their noninvasiveness, high temporal resolution, portability and reasonable cost. There are three main

and analysis, decision to publish, or preparation of the manuscript.

Competing Interests: The authors have declared that no competing interests exist.

brain activity patterns that are used to design an EEG-based BCI; event-related potentials (ERPs) such as P300 [4–6], steady state visual evoked potentials (SSVEP) [7–9] and eventrelated desynchornization/synchronization (ERD/ERS) [10, 11]. In recent years, motor related BCIs in which users imagine a movement (motor imagery) and the system detects the corresponding spatial distributions of EEG oscillations (ERD/ERS) have become very popular [12– 14]. The rapid improvement of motor imagery BCIs has made them an efficient platform for new developments in such areas as medicine, robotics and entertainment. Today, the BCI technology enables users move prostheses [15–17], navigate through virtual reality [18–20] and control telepresence robotic settings only by thought [21–25]. These advances are indebted to the much effort of BCI researchers who have produced powerful algorithm and high-accuracy classifiers that are responsible for decoding EEG signals. However, with the emerging potentials for using BCIs in various fields and promotion of their real-world application outside of laboratories, there is also a rising need to understand the human side of the interface and identify the opportunities and constraints for this interaction paradigm [26].

There are two major issues that challenge BCI researchers in regard to the human users. The first is user training; the operation of a BCI is not intuitive and users need to learn how to voluntarily control their neural activities [6, 27, 28]. Especially in case of motor imagery based BCIs, a rather long training period is required until the users gain skill in the imagery task and achieve optimal performance. Previous studies have sought various kinds of cognitive tasks and feedback techniques to propose an optimal training protocol [11, 29–31]. In a search for suitable mental task, Neuper et al. showed that motor imagery patterns were only recognizable when the participants used a strategy of kinesthetic motor imagery (first-person process) compared to when they formed a visual image of another’s action (third-person process) [32]. They also evaluated the effect of visual feedback in shape of a realistic moving hand versus an abstract moving bar, however they couldn’t find any significant difference between the two feedback designs [33]. In another study, the comparison of feedback modalities, such as haptic feedback vs. visual feedback, revealed no difference of improvement during BCI control [34]. Only, when both modalities were present and the sensorimotor feedback loop was closed, did the modulation of activities in motor cortex increase [35]. Probably among all the approaches that were taken for training optimization, those that challenged the bias of feedback accuracy were most effective. Although there are some inconsistencies between the results, several groups have shown that positive and negative bias of feedback can influence the performance level of users based on their initial skill levels [36–39].

The second challenging topic for the BCI researchers is in respect to the impact that brainsteered interfaces reflect on the user’s experience of self. In a motor BCI, where imagination of bodily movements (motor imagery) results into the motions of objects other than the user’s real body, the representations of one’s own body may change in a way that the feeling of body ownership and agency is reoriented from the real body toward the controlled device, producing the so-called sense of embodiment [21, 24, 40–42]. Understanding the mechanism of embodiment is particularly important because of the positive impacts it can extend on the BCI control and practicality. For instance, in the case of amputees with a neuro-prosthetic limb, the longterm and efficient usage of the limb depends on how well the patients accept the limb as an integrated part of their own body rather than a tool attached to them [43, 44]. Similarly in the case of BCI-control for a moving avatar or robot, the arousal of embodiment for the user is assumed to promote his involvement in the motor imagery task and enhance his skills in the navigation and operation. So far, studies with virtual reality setup [40, 41] and humanoid robots [21, 23] have investigated the conditions and cognitive process under which the BCI control of another body can elicit a sense of embodiment and ownership in the operators. Recently, Evans and Blanke took a step further and found shared neural underpinnings

between motor imagery and illusory body ownership [45]. However, none of the past works has explicitly evaluated the impact of embodiment on the performance of BCI users.

A quick review of the existing literature demonstrates that although research seeks solution to the above issues, user training and embodiment, these studies handle each of them separately and the combination of both is never discussed in any of them. Despite the current trends of merging BCIs with virtual reality and robotic setups [46] that has facilitated the human-interface interaction, surprisingly to our knowledge, there is no work that has explicitly assessed the impact of embodiment on motor imagery learning during BCI control.

In this paper, our approach aims at bridging these two problems, by introducing a potential relationship between the sense of embodiment during BCI-control and the improvement of user’s BCI performance. We previously proposed a BCI operational system for a very humanlike android robot (called Geminoid), which through its realistic appearance could induce a strong sense of body ownership transfer (BOT) in the operators [21]. We also demonstrated that by designing a suitable feedback paradigm and manipulating the subjects’ perception of BCI performance, operators could engage with the motor imagery task easier and optimize their regulation of brain activities for a better BCI control [36, 37]. However to what extent the BOT illusion and the match between the visual feedback from robot with one’s experience of body control contributed to the optimized learning of motor imagery remained undiscussed. In this work, we further compare the effect of feedback design on motor imagery learning between the android and a non-humanlike robot (a pair of metallic gripper), to seek the exact impact of robot’s appearance and discuss how the sense of embodiment and body ownership illusion can play an important role in the improvement of motor imagery skills.

### Methods Ethics statement

Experiments in this study were conducted in full accordance with the ethical guidelines of Advanced Telecommunications Research Institute International (ATR) and the Ethics Committee of the named institute specifically approved this study. (Approval number: 13-506-3).

### Participants

Thirty-eight healthy, right-handed subjects (17 male and 21 female, age M = 23.8, SD = 8.2) participated in this experiment. None of them had participated in our previous experiments and they were all beginners with BCI system. Participants received explanation prior to the experiment and signed a written consent form.

### BCI-Teleoperation

The teleoperational interface developed in this work consisted of a BCI system and two different robots.

The BCI system recorded 27 EEG channels over the primary sensori-motor cortex, referenced to the right ear and grounded to the forehead. Participants performed a motor imagery task for their own right and left hand while they watched through a head-mounted display (Vuzix iWear VR920) a first-person perspective image of the robot’s hands (Fig 1). Two balls were placed inside the robot’s hands. Each time the right or left ball was lighted, participants held an image of grasp for the corresponding hand. Cerebral activities were recorded by g. USBamp biosignal amplifiers (Guger Technologies) and the BCI classifier translated the motor imagery patterns into motion commands for the robot’s hands. The classification of recorded signals was conducted under Simulink/MATLAB (Mathworks) for offline and online

[Figure 7]

Fig 1. Experiment setup. 27 EEG electrodes recorded brain activities during a motor imagery task. Subjects watched first-person images of a robot’s hands through a head mounted display. A lighting ball in front of the robot’s hands gave motor imagery cue and subjects held images of a grasp for their own corresponding hand. Classifier detected two classes of results (right or left) and sent a motion command to the robot’s hand.

doi:10.1371/journal.pone.0161945.g001

parameter extraction. This process included bandpass filtering between 0.5 and 30 Hz, sampling at 128 Hz, cutting off artifacts by notch filter at 60 Hz, and adopting the Common Spatial Pattern (CSP) algorithm for discrimination of Event Related Desynchronization (ERD) and Event Related Synchronization (ERS) patterns associated with the motor imagery task [47]. Results were classified with weight vectors that weighed each electrode based on its importance for the discrimination task and suppressed the noise in individual channel by using the correlations between neighboring electrodes. During each right or left imagery movement, the decomposition of the associated EEG led to a new time series, which was optimal for discrimination of two populations. The patterns were designed such that the signal from the EEG filtering with CSP had maximum variance for the left trials and minimum variance for the right trials and vice versa. In this way, the difference between the left and right populations was maximized and the only information contained in these patters was where the EEG variance fluctuated the most during the comparisons between the two conditions. Finally when the discrimination between left and right imaginations was made, the classifier outputted a linear array signal in the range of [–1, 1], where -1 was commanded as a full left grasp and 1 was commanded as a full right grasp [21].

The robots used in this experiment, Geminoid and ArmRobot, are shown in Fig 2. During the visual feedback of motion, Geminoid used four fingers to grasp the lighted ball and ArmRobot used only the upper prong to clutch the ball. Identical blankets were laid on both the subjects’ legs and the robots’ legs to match the body background view. In this experiment, we used an edited video of the robot’s motions, however when at the end of the experiment, participants were questioned if they noticed anything unusual in the images or that the video they watched

[Figure 9]

Fig 2. Geminoid vs ArmRobot. Two different robots, a pair of very humanlike android hands versus a pair of robotic arms were used for BCI-teleoperation to evaluate the effect of humanlikeness and body ownership illusion on motor imagery learning.

doi:10.1371/journal.pone.0161945.g002

was not a real time video but a previously recorded and edited video, the response from all participants was negative.

### Procedure

After receiving instructions about the motor imagery task, participants sat in a chair and experimenter placed EEG electrodes. All participants performed one session of non-feedback calibration (for the setup of subject-specific classifier) and one session of training with a normal computer screen. Following to this, they wore head mounted display and performed another two sessions of BCI-teleoperation with the robots (Session 3 and Session 4).

All sessions included 40 trials, 20 trials per class left/right in a randomized order. Each trial lasted 7.5 seconds and included an acoustic warning at second 2 for the onset of imagery task. From second 3 to 4.25, a visual cue in form of an arrow on the screen during the training session or a lighting ball inside the robot’s hand during the teleoperational sessions was presented based on which the subjects had to hold an image of grasp for their right or left hand. From second 4.25 to 7, the feedback was presented to the subject. In the training session, the feedback was in form of a horizontal bar on the screen extending to right or left. In the teleoperational sessions, robot’s hands made a grasp based on the online result of the BCI classifier.

After completing the first and second non-operational sessions, participants were separated into two groups of nineteen members and each group used different robot for BCI-operation in Session 3 (Fig 2). In Session 4, again all of the participants used the same robot, ArmRobot, for BCI-operation. Therefore, the experimental conditions for each group can be summarized as below:

- 1. Geminoid group: Participants initially operated Geminoid’s hands in Session 3 and proceeded to operation of the ArmRobot in Session 4.
- 2. ArmRobot group: Participants BCI-operated only the robotic arms in both Session 3 and Session 4.

Similar to our previous work regarding the effect of biased feedback on the motor imagery leaning [36, 37], participants of both groups received a positive bias of feedback (90% correct) in the first half of Session 3. The goal here was to compare the impact of the same feedback design between two different looking robots. In Session 4 however, feedback accuracy was not conditioned and subjects received their real performance that was outputted from the classifier. The aim of designing Session 4 was to measure the robustness of the motor imagery skills learnt by each robot in Session 3 and estimate if optimized motor imagery patters sustain for BCI-operation of other robots, once they are learnt. An illustration of the experiment procedure is depicted on Fig 3.

At the end of each BCI-operational session participants responded orally to the BOT questionnaire (refer to Evaluation). Also participants commented about their performance in each session during an interview following the experiment termination. Particularly the Geminoid group was asked to compare the feasibility of motor imagery task between the two sessions with different robots.

### Evaluation

Since we examined the effect of body ownership illusion on the motor imagery learning during BCI-teleoperation, it was important to measure the subjective experience of BOT illusion for

[Figure 11]

- Fig 3. Experimental procedure. Subjects performed one session of non-feedback calibration (for the setup of subject-specific classifier) and one session of training with a normal computer screen. Then, they wore head-mounted display and prepared for BCI-teleoperation of the robots. Subjects were divided into two groups: (i) Geminoid group was first trained with a humanlike robot and then operated a pair of metallic gripper. (ii) ArmRobot group only used the metallic grippers for operation in both Sessions 3 and 4. All sessions included 40 trials. Subjects answered a questionnaire at the end of each teleopreational session.

- doi:10.1371/journal.pone.0161945.g003

each robot separately. Therefore evaluation was made by two methods: 1) questionnaire to measure the self-assessed BCI performance and level of BOT illusion, 2) offline analysis of brain activities for estimation of the motor imagery improvement.

1) Questionnaire. The questionnaire we asked from the subjects included two primary questions on the self-estimated performance and ownership illusion:

- Q1) Could you operate the robot’s hands according to your intentions?
- Q2) Did you feel as if the robot’s hands were your own hands?

Subjects scored the above questions on a 7-point Likert scale, 1 denoting “couldn’t operate / didn’t feel at all” and 7 denoting “could operate very well / felt very strongly”.

- 2) Motor imagery learning and robustness. We evaluated motor imagery learning based

on how well the subject could generate brain patterns discriminant for the two classes of right and left hand grasps during the operation. Since our BCI system used a previously setup classifier for the recognition task and did not use a learning algorithm, the online performance of the subjects could not serve as a reliable measure. Because the subjects may have consciously or unconsciously modified the generation of their brain activity patterns and in that case the classifier would fail to detect these changes. Therefore, we used the original brain signals and conducted an offline analysis of brain activities to extract the feature distribution of right and left motor imagery trials in each session. We then used Fisher’s discriminant criterion measures in a linear discriminant analysis to observe the distribution of the two classes’ feature vectors in a 4-dimential space (see details in Ref. [36, 37]). Fisher’s parameter J is defined as

jm~R m ~Lj2 ~s2R þ~s2L ð1Þ

J ¼

where the quantity jm~R m ~Lj2 is the distance between the two classes’ means and the quantity ~s2R þ~s2L indicates the within-class scatter. When performing motor imagery, a larger J corre-

sponds to a closer dispersion of feature vectors per each class and a further distance between two class means, which represents a more discriminant distribution of feature vectors within the feature space and therefore the better execution of motor imagery task by subject.

The trend of motor imagery learning in Session 3 was defined as the ratio between the class separability in the second 20 test trials (J2) and the first 20 biased trials (J1). Therefore ΔJ = J2/J1 was selected as a measure of motor imagery (MI) learning due to the elicit of BOT illusion.

J2 J1 ð2Þ

DJMI learning ¼

In addition, J parameter was compared between Session 3 and Session 4 to estimate the robustness of the online motor imagery skills in Session 4, once they are acquired due to the feedback bias and BOT illusion in Session 3. The class separability was calculated for the 40 trials in Session 4 (J4) and for the 40 trials in Session 3 (J3). The ratio between these two parameters

J4 J3 ð3Þ

DJMI robustness ¼

was selected as the measure of motor imagery durability and robustness when the illusion was shattered and subjects proceeded to the BCI-teleoperation of another robot in a different paradigm.

### Results

Subjects’ answers to the questionnaire and the results of motor imagery learning measure ΔJ is provided in the following two sections.

### 1) Questionnaire

Participants’ responses to the questionnaire for both Gemionid and ArmRobot group were averaged and compared between the two sessions, Session 3 and Session 4. The mean value, standard deviation, and p-value for each group are depicted on Fig 4.

For both Q1 and Q2, the responses from both Geminoid and ArmRobot group showed a higher mean value in Session 3 compared to Session 4. Since the Likert scores are of ordinal nature, we used a non-parametric statistical test to analyze our results (S1 Table). For the Geminoid group, a Wilcoxon signed-rank test on scores of Q1, which asked about the operators’ self-evaluated performance during the session, showed a significant difference between Session 3 (M = 4.58, SD = 1.17) and Session 4 (M = 3.05, SD = 0.97); [Session 3 > Session 4, Z = 3.45, p < 0.001]. The same test on Q1 scores from ArmRobot group revealed a significantly higher score in Session 3 (M = 4.47, SD = 1.22) than Session 4 (M = 3.21, SD = 1.23); (Session

- 3 > Session 4, Z = 3.48, p < 0.001).

[Figure 14]

- Fig 4. Questionnaire results. Median values and interquartile ranges for Q1 (self-evaluated performance) and Q2 (body ownership illusion) at the end of Session 3 and Session 4.

- doi:10.1371/journal.pone.0161945.g004

On the other hand, Wilcoxon signed-rank test on responses from Geminoid group to Q2, which directly asked the intensity of BOT over the operated hands, displayed significantly higher score in Session 3 (M = 4.36, SD = 1.38) than Session 4 (M = 2.53, SD = 1.17) [Session 3 > Session 4, Z = 3.74, p < 0.001], whereas the responses from ArmRobot group to Q2 in Session 3 (M = 4.0, SD = 1.11) and Session 4 (M = 3.53, SD = 1.61) did not reveal a significant difference [Z = 1.46, p = 0.18], although it was comparatively higher in Session 3, perhaps due to the effect of positive bias during the first half of Session 3.

### 2) Motor imagery learning and robustness

For each group of participants, the results of ΔJMI learning and ΔJMI robustness are demonstrated in Fig 5.

We used the Shapiro-Wilk test to evaluate whether the data (S2 Table) were normally distributed. The results from this test for the J2/J1 data (W = 0.94, p = 0.25), and J4/J3 data

[Figure 16]

Fig 5. Results for EEG offline analysis. ΔJ (a measure of right/left class separation in the feature space during the motor imagery task) was calculated between two halves of Session 3 to evaluate the trend of motor imagery learning due to the BOT illusion. Also, ΔJ was compared between Session 3 and Session 4 to estimate the robustness of motor imagery skills learnt through each robot. Median values and interquartile ranges are depicted on each graph.

doi:10.1371/journal.pone.0161945.g005

(W = 0.98, p = 0.96) did not reject the null hypothesis that the data are normally distributed. Therefore, assuming normal distribution, two-sample t-test was used to compare the results between the two groups of participants.

The comparison of ΔJMI learning during Session 3 (ratio J2/J1) did not show a significant difference between the two Geminoid group (M = 1.31, SD = 0.97) and ArmRobot group (M = 1.48, SD = 1.05) [t(36) = -0.11, p = 0.91]. Whereas, the comparison of ΔJMI robustness between Session 3 and Session 4 (ratio J4/J3) showed a significantly higher mean value for the Geminoid group (M = 1.08, SD = 0.7) than the ArmRobot group (M = 0.68, SD = 0.42);

[Geminoid > ArmRobot, t(36) = 2.15, p < 0.05], however the mean value for J4/J3 ratio was approximately 1 for Geminoid group and it dropped to less than 1 for the ArmRobot group, indicating a decreasing effect on J parameter.

### Discussion

The present study was particularly conducted to investigate the impact of visual feedback and sense of embodiment on the motor imagery skills acquired during BCI-control. Two groups of novice subjects BCI-operated different looking robots; one group operated a very humanlike android robot (Geminoid) in the first session and then a pair of metallic gripper (ArmRobot) in the second session. The other group practiced operation with only ArmRobot in both sessions. The results did not show a significant improvement in motor imagery learning immediately in the first operational session, however they revealed a significant robustness of motor imagery skills in the following session for only the Geminoid group, who reported a significantly stronger sense of embodiment for the android robot compared to the metallic gripper.

A comparison between the motor imagery performance calculated by our J parameter in Session 3 and Session 4 showed that for subjects who first BCI-operated android hands in one session and then proceeded to the operation with robotic arms, the ΔJMI robustness remained significantly higher than the other group who practiced motor imagery only with the robotic arms in both sessions. This result suggests that the motor imagery skills learnt during a biased training session with a humanlike robot could sustain for the following BCI session with a different robot, even though the feeling of embodiment for the new robot (Q2 scores in Fig 4) dropped significantly. However, the same training paradigm with a less humanlike robot did not show such robustness and a mean value of less than 1 for the ratio J4/J3 indicates a decrease in motor imagery performance for the ArmRobot group.

The significant decline of performance in Session 4 may initially appear unusual, however it can be explained as following based on the conditioning of the operational sessions; In Session 3, subjects received positively biased visual feedback in the first half and then continued to the unbiased (real performance) trials. In Session 4 on the other hand, subjects performed all trials under unbiased condition, which means they received visual feedback of their real performance as it was outputted from the BCI classifier. Since in an unbiased BCI-control, the unsuccessful imagery attempt of subjects for the target hand was presented as an opposite grasp for the robot’s other hand, the interference between observation and self-imagined movements could intensely disturb the motor imagery task and drop the level of confidence and concentration in subjects. This effect could be also confirmed for both Geminoid and ArmRobot group as their scores to Q1 dropped significantly from Session 3 to Session 4 (Fig 4). Hence, a suppression of J parameter was obviously expected in both groups due to the change of performance accuracy in visual feedback. Nevertheless, Geminoid group could resist the decline of J and hold on their skills for operation even in an unbiased session.

The reason for this effect could be discussed based on the mechanism under which motor imagery is practiced and the changes it reflects on the motor circuitry and cortical excitability

during the process of learning. Motor imagery is defined as a dynamic state during which representations of a certain motor act are internally rehearsed in the working memory without motor action [48–50]. Several studies have provided evidence that motor imagery can produce changes, as powerful as those produced by motor execution, at both behavioral and neural level [13, 51–55]. Ehrsson et al. showed that during motor imagery, the content of mental image is reflected on the cortical activation and imagery of certain body parts such as toe, finger, and tongue could result into the activation of different areas in the primary motor cortex [56]. Another work has shown that perspective and posture of imagery task can also generate a difference, that is, the first-person perspective imagery leads to a stronger activation in the motorrelated structures [57]. In addition to these evidences for the effect of imagery content on the cortical activity, the content of visual feedback during the performance of motor imagery has also been shown to interact with motor processes, thereby modulating the excitability in the motor cortex. In an assessment of how visual feedback about posture affects the level of activation during hand motor imagery, Mercier et al. showed that looking at a hand posture compatible with the imagined movement resulted in an increase of cortico-spinal excitability, facilitation of motor representations in memory and regulation of central motor imagery processes [58]. Similarly, the works on mirror therapy for patients who suffer from hemiplegia or phantom pain has shown that watching the unaffected hand in a mirror assisted the motor imagery of the affected hand and resulted in a significant increase of the motor evoked potentials compared to the motor imagery without mirror [59].

Altogether, the above literature suggest that motor imagery includes a visuo-spatial representation regulated by working memory and similar to motor action it can produce changes in brain plasticity [60]. During the performance of motor imagery, the content of both selfinduced image and the visual feedback can affect the activation level of motor cortex and induction of neural pathways. In this study, the difference revealed by the two groups’ performance in the second part of the experiment therefore suggests a difference in the level of cortical excitations each group experienced. The Geminoid group who watched a humanlike hand with a more detailed appearance and compatible action may have experienced a higher excitation of motor processes that induced efficient connectivity and significant changes in neural plasticity, which thus resulted facilitation in learning. Therefore, one can assume that even in the absence of the humanlike robot, the Geminoid group recalled more vivid and explicit representations of the imagery task and performed better on the BCI-operation.

A rather unexpected result was obtained in the first part of this experiment, where the comparison of ΔJMI learning did not reveal a significant improvement in motor imagery learning between the two groups. A main reason that may have yielded this outcome is probably our failure in the estimation of humanlikeness for the ArmRobot and underestimating its potential in inducing the ownership illusion. We initially developed ArmRobot as a non-humanlike robot to be compared versus Geminoid as an android with an extremely humanlike appearance. However, the experiment results contradicted our assumption. The obtained Q2 scores (Fig 4) for the ArmRobot group (who did not experience operational sessions with Geminoid) showed surprisingly high effect in Session 3 in terms of embodiment (almost same as Geminoid group in Session 3) and this effect did not change significantly in Session 4. Whereas, the Q2 score obtained from the Geminoid group (who initially observed Geminoid and then proceeded to the operation of the ArmRobot) had a significant decrease from Session 3 to Session

4. Thus, we can recognize that the perception of humanlikeness and body ownership illusion was relative in this case, based on the subjects’ previous experience of robots. In other words, those who already operated the Geminoid, found the ArmRobot significantly less humanlike and reported weaker embodiment, whereas the second group who did not have the chance to

make a comparison between the robots’ appearances could experience a strong embodiment for the moving ‘metallic hands’.

It has been previously shown that such ownership illusions as rubber hand illusion [61] that are raised by multisensory integration can only be induced for humanlike body parts and not the non-corporeal objects [62]. However, in the case of motion and voluntary action, body ownership is not the only component that contributes to the mechanism of self-recognition and embodiment. The sense of agency, which is the feeling of being the generator of the action, can also play a major role in establishing the sense of embodied self. In the present study, beside the anthropomorphic kinematics, the matching of goal and timing of the ArmRobot motions with the subject’s intention raised a high sense of agency that could lead to a strong embodiment in the operators of the ArmRobot.

Another cause for the indifferent results between the two groups could be the impact of action observation and strong firing of mirror neurons in both conditions [63]. The BCI classifier monitors the suppression of sensorimotor brain rhythms in order to recognize the left and right classes. However, in this design there are two components that produce the suppression of brain activities; one is the motor imagery task or mental simulation of hand grasp, the other is viewing the action of robot and activation of the mirror neurons system [64, 65]. There is evidence that mirror neurons are more sensitive to some motions than others, for instance observation of a hand precision grasp can cause greater suppression of mu rhythm than observation of a flat-hand extension [66]. Moreover, the presence of an object (here the ball inside robot’s hand), indicating the goal of action, increases the mu rhythm suppression as compared to meaningless motions [67]. Therefore, the overlapping activity of motor imagery and action observation during experiment may have generated ERD patterns in sensorimotor area that are not necessarily distinguishable.

Another reason for the lack of significant difference in the learning progress of the two groups could be the inadequate training. Learning to modulate brain activities to control a BCI is a difficult task that requires attention, motivation and above all practice [6, 27]. In the present study, we recruited novice BCI users who had their first encounter with a BCI system and performed only one training session (Session 2) before the test sessions. For these subjects, the unfamiliarity of the motor imagery task and the tension or stress caused by the experimental environment may have been the psychological factors that influenced the subjects’ learning potentials, causing the reduced impact of the embodiment parameter on the learning progress. Larger number of training sessions, performed in regular intervals, would customize the inexperienced users with a BCI experiment and therefore optimize their capacity for learning [33].

Summing up, the use of a humanlike robot for the BCI control of hand grasps could generate a strong sense of embodiment and induce long-term and robust motor imagery skills. These findings are supported by the outcome of (1) questionnaire, where the users self-rated their performance and feeling of body ownership, and (2) analysis of EEG activities and motor patterns where the segregation of EEG features for each motor imagery class was measured. Our results can further provide evidence for a close linkage between the visual and the motor processes, especially under conditions in which no movement occurs. Visual inputs are recognized as the more effective source for motor learning compared to proprioceptive feedback [68], particularly in the early stages of learning [69]. Therefore, it is speculated that during motor imagery where the sense of proprioception is absent, the role of visual feedback in facilitation or inhibition of motor representation becomes further dominant [58]. Hence, taking into account the importance of visual feedback design is critical in the development of efficient training protocols for motor imagery based BCIs.

### Conclusions

In this work, we combined an EEG-based BCI with two types of different looking robots to investigate the shared mechanism of embodiment and motor imagery. We hypothesized that the learning of motor imagery task for the BCI-control can be enhanced if the visual feedback is aligned with our every day experience of human body. We recruited two groups of subjects who BCI-controlled a pair of very humanlike android hands versus a pair of metallic gripper. Our aim was to purposefully create different levels of body ownership illusion and therefore examine the effect of stronger embodiment on the operator’s motor imagery learning.

Although our results did not show a significant improvement of motor imagery skills between two groups during the first biased session, in a follow-up session when all participants operated the robotic gripper, the group who initially practiced motor imagery task with the android’s hands showed significantly higher BCI controlling skills than the group who only experienced the operation of robotic gripper. This shows that motor imagery skills learnt during the BCI-operation of humanlike hands are robust to time and visual feedback changes. Future experiment should re-challenge these findings with a completely non-humanlike robot to investigate the effect of BOT illusion on motor imagery learning in an online session.

Altogether, by suggesting a positive interaction between the inducement of embodiment and improvement of subjects’ motor imagery skills, our findings reveal the promising nature of BCI-teleoperation for an efficient interaction through android robots and furthermore the application of such system in the future BCI training paradigms.

### Supporting Information

- S1 Table. Questionnaire responses. Raw data collected from the subjects to Q1 and Q2. (PDF)
- S2 Table. J values in each session. (PDF)

### Acknowledgments

This research was supported by Grants-in-Aid for Scientific Research 25220004, 26540109 and 15F15046 and also by ImPACT Program of Council for Science, Technology and Innovation (Cabinet Office, Government of Japan).

### Author Contributions

Conceptualization: MA SN. Formal analysis: MA. Funding acquisition: HI SN MA. Investigation: MA. Methodology: MA SN. Project administration: SN HI. Software: MA. Supervision: SN HI. Validation: SN.

Writing – original draft: MA. Writing – review & editing: SN HI.

### References

- 1. Fabiani GE, McFarland DJ, Wolpaw JR, Pfurtscheller G. Conversion of EEG activity into cursor movement by a brain-computer interface (BCI). Neural Systems and Rehabilitation Engineering, IEEE Transactions on. 2004 Sep; 12(3):331–8.
- 2. Dal Seno B, Matteucci M, Mainardi L. Online detection of P300 and error potentials in a BCI speller. Computational intelligence and neuroscience. 2010 Jan 1; 2010:11.
- 3. Cecotti H. Spelling with non-invasive Brain–Computer Interfaces–Current and future trends. Journal of Physiology-Paris. 2011 Jun 30; 105(1):106–14.
- 4. Jin J, Sellers EW, Zhou S, Zhang Y, Wang X, Cichocki A. A P300 brain–computer interface based on a modification of the mismatch negativity paradigm. International journal of neural systems. 2015 May; 25(03):1550011.
- 5. Yin E, Zhou Z, Jiang J, Chen F, Liu Y, Hu D. A novel hybrid BCI speller based on the incorporation of SSVEP into the P300 paradigm. Journal of neural engineering. 2013 Feb 21; 10(2):026012. doi: 10. 1088/1741-2560/10/2/026012 PMID: 23429035
- 6. Guger C, Daban S, Sellers E, Holzner C, Krausz G, Carabalona R, et al. How many people are able to control a P300-based brain–computer interface (BCI)?. Neuroscience letters. 2009 Sep 18; 462(1):94–

8. doi: 10.1016/j.neulet.2009.06.045 PMID: 19545601

- 7. Muller-Putz GR, Pfurtscheller G. Control of an electrical prosthesis with an SSVEP-based BCI. IEEE Transactions on Biomedical Engineering. 2008 Jan; 55(1):361–4. doi: 10.1109/TBME.2007.897815 PMID: 18232384
- 8. Yin E, Zhou Z, Jiang J, Yu Y, Hu D. A dynamically optimized SSVEP brain–computer interface (BCI) speller. IEEE Transactions on Biomedical Engineering. 2015 Jun; 62(6):1447–56. doi: 10.1109/TBME. 2014.2320948 PMID: 24801483
- 9. Ortner R, Allison BZ, Korisek G, Gaggl H, Pfurtscheller G. An SSVEP BCI to control a hand orthosis for persons with tetraplegia. IEEE Transactions on Neural Systems and Rehabilitation Engineering. 2011 Feb; 19(1):1–5. doi: 10.1109/TNSRE.2010.2076364 PMID: 20875978
- 10. Pfurtscheller G, Neuper C. Future prospects of ERD/ERS in the context of brain–computer interface (BCI) developments. Progress in brain research. 2006 Dec 31; 159:433–7. PMID: 17071247
- 11. Pfurtscheller G, Brunner C, Schlögl A, Da Silva FL. Mu rhythm (de) synchronization and EEG singletrial classification of different motor imagery tasks. Neuroimage. 2006 May 15; 31(1):153–9. PMID: 16443377
- 12. Neuper C, Müller-Putz GR, Scherer R, Pfurtscheller G. Motor imagery and EEG-based control of spelling devices and neuroprostheses. Progress in brain research. 2006 Dec 31; 159:393–409. PMID: 17071244
- 13. Pfurtscheller G, Neuper C. Motor imagery and direct brain-computer communication. Proceedings of the IEEE. 2001 Jul; 89(7):1123–34.
- 14. Townsend G, Graimann B, Pfurtscheller G. Continuous EEG classification during motor imagery-simulation of an asynchronous BCI. Neural Systems and Rehabilitation Engineering, IEEE Transactions on. 2004 Jun; 12(2):258–65.
- 15. Guger C, Harkam W, Hertnaes C, Pfurtscheller G. Prosthetic control by an EEG-based brain-computer interface (BCI). InProc. aaate 5th european conference for the advancement of assistive technology 1999 Nov 3 (pp. 3–6).
- 16. Jackson A, Moritz CT, Mavoori J, Lucas TH, Fetz EE. The Neurochip BCI: towards a neural prosthesis for upper limb function. Neural Systems and Rehabilitation Engineering, IEEE Transactions on. 2006 Jun; 14(2):187–90.
- 17. Horki P, Solis-Escalante T, Neuper C, Müller-Putz G. Combined motor imagery and SSVEP based BCI control of a 2 DoF artificial upper limb. Medical & biological engineering & computing. 2011 May 1; 49

(5):567–77.

- 18. Pfurtscheller G, Leeb R, Keinrath C, Friedman D, Neuper C, Guger C, et al. Walking from thought. Brain research. 2006 Feb 3; 1071(1):145–52. PMID: 16405926
- 19. Leeb R, Friedman D, Müller-Putz GR, Scherer R, Slater M, Pfurtscheller G. Self-paced (asynchronous) BCI control of a wheelchair in virtual environments: a case study with a tetraplegic. Computational intelligence and neuroscience. 2007 Sep 10;2007.

- 20. Anatole L, Lotte F, Reilly RB, Leeb R, Hirose M, Slater M. Brain-computer interfaces, virtual reality, and videogames. Computer. 2008 Oct 1(10):66–72.
- 21. Alimardani M, Nishio S, Ishiguro H. Humanlike robot hands controlled by brain activity arouse illusion of ownership in operators. Scientific reports. 2013 Aug 9; 3.
- 22. Kishore S, González-Franco M, Hintemüller C, Kapeller C, Guger C, Slater M, et al. Comparison of SSVEP BCI and eye tracking for controlling a humanoid robot in a social environment. PRESENCE: Teleoperators and Virtual Environments. 2014 Oct 1; 23(3):242–52.
- 23. Thobbi A, Kadam R, Sheng W. Achieving remote presence using a humanoid robot controlled by a non-invasive BCI device. International Journal on Artificial Intelligence and Machine Learning. 2010; 10:41–5.
- 24. Petit D, Gergondet P, Cherubini A, Kheddar A. An integrated framework for humanoid embodiment with a BCI. InRobotics and Automation (ICRA), 2015 IEEE International Conference on 2015 May 26 (pp. 2882–2887). IEEE.
- 25. Cohen O, Druon S, Lengagne S, Mendelsohn A, Malach R, Kheddar A, et al. fMRI-based robotic embodiment: Controlling a humanoid robot by thought using real-time fMRI. PRESENCE: Teleoperators and Virtual Environments. 2014 Oct 1; 23(3):229–41.
- 26. Lotte F, Larrue F, Mühl C. Flaws in current human training protocols for spontaneous brain-computer interfaces: lessons learned from instructional design.
- 27. Curran EA, Stokes MJ. Learning to control brain activity: a review of the production and control of EEG components for driving brain–computer interface (BCI) systems. Brain and cognition. 2003 Apr 30; 51

(3):326–36. PMID: 12727187

- 28. Schuster C, Hilfiker R,Amft O, Scheidhauer A, Andrews B, Butler J, et al. Best practice for motor imagery: a systematic literature review on motor imagery training elements in five different disciplines. BMC medicine. 2011 Jun 17; 9(1):1.
- 29. Kaiser V, Kreilinger A, Müller-Putz GR, Neuper C. First steps toward a motor imagery based stroke BCI: new strategy to set up a classifier. Front Neurosci. 2011 Jul 5; 5:86. doi: 10.3389/fnins.2011. 00086 PMID: 21779234
- 30. Neuper C, Schlögl A, Pfurtscheller G. Enhancement of left-right sensorimotor EEG differences during feedback-regulated motor imagery. Journal of Clinical Neurophysiology. 1999 Jul 1; 16(4):373–82. PMID: 10478710
- 31. Neumann N, Kübler A. Training locked-in patients: a challenge for the use of brain-computer interfaces. Neural Systems and Rehabilitation Engineering, IEEE Transactions on. 2003 Jun; 11(2):169–72.
- 32. Neuper C, Scherer R, Reiner M, Pfurtscheller G. Imagery of motor actions: Differential effects of kinesthetic and visual–motor mode of imagery in single-trial EEG. Cognitive Brain Research. 2005 Dec 31; 25(3):668–77. PMID: 16236487
- 33. Neuper C, Scherer R, Wriessnegger S, Pfurtscheller G. Motor imagery and action observation: modulation of sensorimotor brain rhythms during mental control of a brain–computer interface. Clinical neurophysiology. 2009 Feb 28; 120(2):239–47. doi: 10.1016/j.clinph.2008.11.015 PMID: 19121977
- 34. Kauhanen L, Palomäki T, Jylänki P, Aloise F, Nuttin M, Millán JD. Haptic feedback compared with visual feedback for BCI. In Proceedings of the 3rd International Brain-Computer Interface Workshop & Training Course 2006 2006 (No. LIDIAP-CONF-2006-022).
- 35. Gomez-Rodriguez M, Peters J, Hill J, Schölkopf B, Gharabaghi A, Grosse-Wentrup M. Closing the sensorimotor loop: haptic feedback facilitates decoding of motor imagery. Journal of neural engineering. 2011 Apr 8; 8(3):036005. doi: 10.1088/1741-2560/8/3/036005 PMID: 21474878
- 36. Alimardani M, Nishio S, Ishiguro H. Effect of biased feedback on motor imagery learning in BCI-teleoperation system. Frontiers in systems neuroscience. 2013 Dec; 8:52–.
- 37. Alimardani M, Shuichi N, Ishiguro H. The effect of feedback presentation on motor imagery performance during BCI-teleoperation of a humanlike robot. InBiomedical Robotics and Biomechatronics (2014 5th IEEE RAS & EMBS International Conference on 2014 Aug 12 (pp. 403–408). IEEE.
- 38. Barbero Á, Grosse-Wentrup M. Biased feedback in brain-computer interfaces. Journal of neuroengineering and rehabilitation. 2010 Jul 27; 7(1):1.
- 39. González-Franco M, Yuan P, Zhang D, Hong B, Gao S. Motor imagery based brain-computer interface: a study of the effect of positive and negative feedback. In Engineering in Medicine and Biology Society, EMBC, 2011 Annual International Conference of the IEEE 2011 Aug 30 (pp. 6323–6326). IEEE.
- 40. Perez-Marcos D, Slater M, Sanchez-Vives MV. Inducing a virtual hand ownership illusion through a brain–computer interface. Neuroreport. 2009 Apr 22; 20(6):589–94. PMID: 19938302
- 41. Cohen O, Koppel M, Malach R, Friedman D. Controlling an avatar by thought using real-time fMRI. Journal of neural engineering. 2014 May 19; 11(3):035006. doi: 10.1088/1741-2560/11/3/035006 PMID: 24834973

- 42. Leonardis D, Frisoli A, Barsotti M, Carrozzino M, Bergamasco M. Multisensory feedback can enhance embodiment within an enriched virtual walking scenario. PRESENCE: Teleoperators and Virtual Environments. 2014 Oct 1; 23(3):253–66.
- 43. Abbott A. Neuroprosthetics: in search of the sixth sense. Nature. 2006 Jul 13; 442(7099):125–7. PMID: 16837993
- 44. Spence C. The Cognitive Neuroscience of Incorporation: Body Image Adjustment and Neuroprosthetics. In Clinical Systems Neuroscience 2015 (pp. 151–168). Springer Japan.
- 45. Evans N, Blanke O. Shared electrophysiology mechanisms of body ownership and motor imagery. Neuroimage. 2013 Jan 1; 64:216–28. doi: 10.1016/j.neuroimage.2012.09.027 PMID: 22995776
- 46. Lotte F, Faller J, Guger C, Renard Y, Pfurtscheller G, Lécuyer A, et al. Combining BCI with virtual reality: towards new applications and improved BCI. In Towards Practical Brain-Computer Interfaces 2012 (pp. 197–220). Springer Berlin Heidelberg.
- 47. Guger C, Ramoser H, Pfurtscheller G. Real-time EEG analysis with subject-specific spatial patterns for a brain-computer interface (BCI). Rehabilitation Engineering, IEEE Transactions on. 2000 Dec; 8

(4):447–56.

- 48. Decety J. The neurophysiological basis of motor imagery. Behavioural brain research. 1996 May 31; 77

(1):45–52.

- 49. Jeannerod M. Mental imagery in the motor context. Neuropsychologia. 1995 Nov 30; 33(11):1419–32. PMID: 8584178
- 50. Annett J. Motor imagery: perception or action?. Neuropsychologia. 1995 Nov 30; 33(11):1395–417. PMID: 8584177
- 51. Jeannerod M, Decety J. Mental motor imagery: a window into the representational stages of action. Current opinion in neurobiology. 1995 Dec 31; 5(6):727–32. PMID: 8805419
- 52. De Vries S, Mulder T. Motor imagery and stroke rehabilitation: a critical discussion. Journal of Rehabilitation Medicine. 2007 Jan 5; 39(1):5–13. PMID: 17225031
- 53. Lotze M, Montoya P, Erb M, Hülsmann E, Flor H, Klose U, et al. Activation of cortical and cerebellar motor areas during executed and imagined hand movements: an fMRI study. Journal of cognitive neuroscience. 1999 Sep; 11(5):491–501. PMID: 10511638
- 54. Miller KJ, Schalk G, Fetz EE, den Nijs M, Ojemann JG, Rao RP. Cortical activity during motor execution, motor imagery, and imagery-based online feedback. Proceedings of the National Academy of Sciences. 2010 Mar 2; 107(9):4430–5.
- 55. Munzert J, Lorey B, Zentgraf K. Cognitive motor processes: the role of motor imagery in the study of motor representations. Brain research reviews. 2009 May 31; 60(2):306–26. doi: 10.1016/j.brainresrev. 2008.12.024 PMID: 19167426
- 56. Ehrsson HH, Geyer S, Naito E. Imagery of voluntary movement of fingers, toes, and tongue activates corresponding body-part-specific motor representations. Journal of neurophysiology. 2003 Nov 1; 90

(5):3304–16. PMID: 14615433

- 57. Lorey B, Bischoff M, Pilgramm S, Stark R, Munzert J, Zentgraf K. The embodied nature of motor imagery: the influence of posture and perspective. Experimental Brain Research. 2009 Apr 1; 194(2):233–

43. doi: 10.1007/s00221-008-1693-1 PMID: 19139856

- 58. Mercier C, Aballea A, Vargas CD, Paillard J, Sirigu A. Vision without proprioception modulates corticospinal excitability during hand motor imagery. Cerebral Cortex. 2008 Feb 1; 18(2):272–7. PMID: 17517681
- 59. Fukumura K, Sugawara K, Tanabe S, Ushiba J, Tomita Y. Influence of mirror therapy on human motor cortex. International Journal of Neuroscience. 2007 Jan 1; 117(7):1039–48. PMID: 17613113
- 60. Lacourse MG, Turner JA, Randolph-Orr E, Schandler SL, Cohen MJ. Cerebral and cerebellar sensorimotor plasticity following motor imagery-based mental practice of a sequential movement. Journal of rehabilitation research and development. 2004 Jul 1; 41(4):505. PMID: 15558380
- 61. Botvinick M, Cohen J. Rubber hands 'feel' touch that eyes see. Nature. 1998 Feb 19; 391(6669):756–. PMID: 9486643
- 62. Tsakiris M, Carpenter L, James D, Fotopoulou A. Hands only illusion: multisensory integration elicits sense of ownership for body parts but not for non-corporeal objects. Experimental Brain Research. 2010 Jul 1; 204(3):343–52. doi: 10.1007/s00221-009-2039-3 PMID: 19820918
- 63. Rizzolatti G, Craighero L. The mirror-neuron system. Annu. Rev. Neurosci. 2004 Jul 21; 27:169–92. PMID: 15217330
- 64. Gazzola V, Rizzolatti G, Wicker B, Keysers C. The anthropomorphic brain: the mirror neuron system responds to human and robotic actions. Neuroimage. 2007 May 1; 35(4):1674–84. PMID: 17395490

- 65. Oberman LM, McCleery JP, Ramachandran VS, Pineda JA. EEG evidence for mirror neuron activity during the observation of human and robot actions: Toward an analysis of the human qualities of interactive robots. Neurocomputing. 2007 Aug 31; 70(13):2194–203.
- 66. Muthukumaraswamy SD, Johnson BW. Changes in rolandic mu rhythm during observation of a precision grip. Psychophysiology. 2004 Jan 1; 41(1):152–6. PMID: 14693010
- 67. Muthukumaraswamy SD, Johnson BW, McNair NA. Mu rhythm modulation during observation of an object-directed grasp. Cognitive Brain Research. 2004 Apr 30; 19(2):195–201. PMID: 15019715
- 68. Adams JA, Gopher D, Lintern G. The effects of visual and proprioceptive feedback on motor learning. In Proceedings of the Human Factors and Ergonomics Society Annual Meeting 1975 Oct 1 (Vol. 19, No. 2, pp. 162–165). SAGE Publications.
- 69. Fleishman EA, Rich S. Role of kinesthetic and spatial-visual abilities in perceptual-motor learning. Journal of Experimental Psychology. 1963 Jul; 66(1):6.

