[ﬁnal version to Proceedings of the IEEE: 01/04/2015 / 23:30]

# Towards Independence: A BCI Telepresence Robot for People with Severe Motor Disabilities

Robert Leeb, Member, IEEE, Luca Tonin, Martin Rohm, Lorenzo Desideri, Tom Carlson, Member, IEEE, Jos´ed.R. Mill´an, Senior Member, IEEE

Abstract—This paper presents an important step forward towards increasing the independence of people with severe motor disabilities, by using brain-computer interfaces (BCI) to harness the power of the Internet of Things. We analyze the stability of brain signals as end-users with motor disabilities progress from performing simple standard on-screen training tasks to interacting with real devices in the real world. Furthermore, we demonstrate how the concept of shared control —which interprets the user’s commands in context— empowers users to perform rather complex tasks without a high workload. We present the results of nine end-users with motor disabilities who were able to complete navigation tasks with a telepresence robot successfully in a remote environment (in some cases in a different country) that they had never previously visited. Moreover, these end-users achieved similar levels of performance to a control group of ten healthy users who were already familiar with the environment.

Index Terms—Brain-computer interface (BCI), electroencephalogram (EEG), motor imagery, application control, endusers with motor disabilities, telepresence, shared control, robotic device

I. INTRODUCTION

In recent years, the capability to directly use brain signals as a communication and control channel, via a so-called braincomputer interface (BCI) or brain-machine interface (BMI), has witnessed rapid progress and is becoming a key component in the assistive technology ﬁeld [1]. In this framework, one of the core areas targeted by BCIs is neuroprosthetics. This means being able to control robotic and prosthetic devices in order to perform activities of daily living, using brain signals as a possible alternative input modality. The eventual aim is to empower people with severe motor disabilities to (re–)gain a degree of independence.

Correspondence to R. Leeb (robert.leeb@epﬂ.ch) and J.d.R. Mill´an (jose.millan@epﬂ.ch).

R. Leeb, is with the Center for Neuroprosthetics, Ecole´ Polytechnique F´ed´erale de Lausanne, Station 19, CH-1015 Lausanne, Switzerland.

L. Tonin, is with the Intelligent Autonomous Systems Laboratory, Department of Information Engineering, University of Padua, via G. Gradenigo 6/A, I-35131 Padova, Italy.

- M. Rohm, is with the University of Heidelberg, Schlierbacher Landstraße

200a, D-69118 Heidelberg, Germany.

L. Desideri, is with AIAS Bologna onlus/Ausilioteca, Via Sant’ Isaia 90, I-40123 Bologna, Italy.

T. Carlson, is with the Aspire Centre for Rehabilitation Engineering and Assistive Technology, University College London, Royal National Orthopaedic Hospital, Stanmore, HA7 4LP, United Kingdom.

J.d.R. Mill´an, is with the Chair in Non-Invasive Brain-Machine Interface, Ecole´ Polytechnique F´ed´erale de Lausanne, Station 11, CH-1015 Lausanne, Switzerland.

In addition to high accuracy in decoding user intention, one of the most critical challenges currently faced is to design fast decision-making algorithms that are robust with respect to the split of attention between the mental task (the user must focus to deliver the desired command) and the external global task to be achieved, such that they allow the user to control complex robotic and prosthetic devices [2], [3]. Much evidence has demonstrated the feasibility of such braincontrolled devices, ranging from robotic arms [4], [5], [6] to hand orthoses [7], [8], [9]; from telepresence robots [10], [11] to wheelchairs [12], [13], [14]; and from quadcopters [15] to helicopters [16]. These works predominantly take spontaneous approaches, where the users learn to voluntarily modulate their sensorimotor brain activity. Such a paradigm seems to be an intuitive and natural way of controlling neuroprosthetic devices, since they free the visual and audio channels to perform other tasks, e.g., interaction, whilst using signals from the motor cortex. Nevertheless, BCIs based on exogenous stimulation, such as an evoked P300 signal, have been used to control wheelchairs as well. Thereby, the system ﬂashes the possible predeﬁned target destinations several times in a random order [13], [14]. The stimulus that elicits the largest P300 is chosen as the target and, then, the intelligent wheelchair reaches the selected target autonomously. Once there, it stops and the user can select another destination. Another possibility would be to ﬂash a video-overlapped visual grid to select left/right turns or to move one “step” forward [17].

Generally, the control of neuroprosthetic devices is achieved by analyzing the electrical activity from the brain, either via invasive implants in the motor cortex [6] or non-invasively from electrodes attached to the surface of the scalp. The electroencephalogram (EEG), being non-invasive, is a convenient, safe, and inexpensive method that promises to bring BCI technology to a large population of people with severe motor– impairments. However, the inherent properties of EEG signals limit the information transfer rate of EEG-based BCIs.

Nevertheless, complex robotic devices have been successfully and reliably controlled by such BCIs, by exploiting smart interaction designs, such as shared control [18], [19], [20]. The cooperation between a human and an intelligent device allows the user to focus the attention on the high-level route or ﬁnal destination and ignore low level problems related to the navigation task (e.g., obstacle avoidance). Researchers have explored two general approaches to shared control, namely autonomous and semi-autonomous. In the former, the user interacts with the robot just by indicating the ﬁnal destination

and the robot decides the best trajectory to reach it. Examples of such an approach are museum tour-guide robots [21] and some BCI-controlled wheelchairs [14]. People with disabilities, however, prefer to retain as much as control authority as possible [22]. Thus, for them, a semi-autonomous approach to BCI-controlled robots seems generally more suitable, where the intelligent system helps the human user to cope with problematic situations such as obstacle detection and avoidance [18], [20], [23].

In the case of neuroprosthetics, our group has pioneered the use of shared control, by taking the continuous estimation of the user’s intentions and providing appropriate assistance to execute tasks safely and reliably [10], [24], even for braincontrolled wheelchairs [2], [25]. A critical aspect of shared control for BCI is coherent feedback —the behavior of the robot should be intuitive to the user and the robot should unambiguously understand the user’s mental commands. Otherwise, people ﬁnd it difﬁcult to form mental models of the neuroprosthetic device. Furthermore, thanks to the mutual learning approach, where the user and the BCI are coupled together and adapt to each other, end-users are able to learn to operate brain–actuated devices relatively quickly (typically in a matter of hours spread across few days [3], [26]). Although the whole ﬁeld of neuroprosthetics target disabled people with motor impairments as end-users, all successful demonstrations of brain-controlled robots mentioned above, except [3], [6], [7], have actually been carried out with either healthy human subjects or non-human primates. Nevertheless, we want to point out that the BCI technology has been used by endusers also in other application ﬁelds [27], [28], since the same techniques, as applied in this paper, can be used also outside the area of robotic control, e.g. like in spelling applications [29]. Hence it is possible to transfer the technology from one application to another, and from healthy participants to end-users with disabilities [3].

In this paper, we explore a BCI-controlled mobile device for telepresence. Such a telepresence mobile robot could enable end-users, who are constrained to remain in bed because of their severe degree of paralysis, to join relatives and friends in order to participate in their activities. Here, we report the results of nine end-users with motor disabilities who mentally drove a telepresence robot from their clinic more than 100 km away and compare their performances to a set of ten healthy users carrying out the same tasks. We hypothesize that with the help of the shared control approach, end-users will attain a level of performance as good as the healthy control group.

II. METHODS

In this section, we ﬁrst describe our BCI system, the telepresence platform used and the shared control approach applied. Then we present the healthy participants and the end-users who tested the system. Finally, we describe the experimental protocol. In a nutshell, every participant began with some initial BCI screening upon which the user-speciﬁc BCI parameters were extracted. The resulting decoder was used to control a simple feedback in the case of the online test and was eventually used to steer the telepresence robot in the experiment.

A. Asynchronous BCI System

To drive our telepresence robot, participants use an asynchronous spontaneous BCI where mental commands are delivered at any moment without the need for any external stimulation and/or cue [10], [26]. To do so users have to go through a number of steps to learn to voluntarily modulate their EEG oscillatory rhythms by executing two motor imagery (MI) tasks. Furthermore, the BCI system has to learn what the user-speciﬁc patterns are. In our case, all participants start by imagining left hand, right hand and feet movements during a number of calibration recordings. Afterwards, the EEG data is analyzed and a classiﬁer is then built for each pair of MI tasks that the user has rehearsed. The pair of tasks which shows highest separability (e.g., right hand vs. left hand or right hand vs. feet), is used as the user-speciﬁc input for the BCI system in the online experiments [3]. In this manner, every subject only uses a sub-set of two motor imagery tasks for the online BCI control.

Brain activity is acquired via 16 active EEG channels over the sensorimotor cortex: Fz, FC3, FC1, FCz, FC2, FC4, C3, C1, Cz, C2, C4, CP3, CP1, CPz, CP2 and CP4 according to the international 10-20 system with reference on the right ear and ground on AFz. The EEG is recorded using a 16channel g.USBamp (g.tec medical engineering, Schiedelberg, Austria) system at 512Hz, band-pass ﬁltered between 0.1Hz and 100Hz and a notch ﬁlter is set at the power line frequency of 50Hz. Each channel is then spatially ﬁltered with a Laplacian derivation before estimating its power spectral density (PSD) in the band 4–48Hz with 2Hz resolution over the last second. The PSD is computed every 62.5ms (i.e., 16 times per second) using the Welch method with 5 overlapped (25%) Hanning windows of 500ms. The input to the classiﬁer embedded in the BCI is a subset of those features (16 channels x 23 frequencies). We use canonical variate analysis (CVA) to select the user–speciﬁc features that best reﬂect the motor–imagery task for each user and use these to train a Gaussian classiﬁer [26]. Evidence about the task being executed is accumulated using an exponential smoothing probability integration framework, as reported in Eq. 1:

## p(yt) = ↵ ⇥ p(yt|xt) + (1   ↵) ⇥ p(yt 1) (1)

where p(yt|xt) is the probability distribution, p(yt 1) the previous distribution and ↵ the integration parameter. Thus, probabilities are integrated until a class reaches a certainty threshold about the user’s intent to deliver a command in order, for instance, to change the robot’s direction. At this moment the mental command is delivered and the probabilities are reset to a uniform distribution. Such an evidence accumulation (or integration) framework yields smooth and predictable feedback, thus helping user training by avoiding confusing and frustrating ﬂuctuations.

This evidence accumulation framework also plays a crucial role in preventing users from delivering arbitrary commands when their attention is shifted temporarily to some other task, thanks to the smooth convergence to the user’s true intention. This property has another beneﬁt, namely supporting intentional non-control (INC) —i.e., the ability to intentionally

not deliver any mental command if the user does not want to change the behavior of the neuroprosthesis. For our telepresence robot, this means that if no mental command is delivered, it will continue moving forward or remain stationary (in the case that it is stopped in front of a target). Intentional noncontrol translates into a third driving command that should not require any direct cognitive effort for the user.

- As part of the BCI screening, all participants (healthy

and end-users) perform several online experiments with the standard horizontal bar-graph feedback on a screen to train their BCI performance and to reﬁne the system’s calibration. During two consecutive sessions it is necessary to achieve an accuracy of more than 70% before being able to move the telepresence robot application test. More details about the used BCI are given in [3].

[Figure 1]

- Fig. 1. (left) End-user at a clinic while operating the BCI. (right) The telepresence robot equipped with infrared sensors for obstacle detection and the SkypeTM connection on top.

- B. Telepresence Robot

Our telepresence robot is based upon the RobotinoTM platform by FESTO, a small circular mobile platform (diameter 38cm, height 23cm) with three holonomic wheels (Figure 1, right side). It is equipped with nine infrared sensors capable of detecting obstacles up to ⇠15cm (depending on light condition) and a webcam that can also be used for obstacle detection, although for the experiments reported in this paper we only use the infrared sensors. For telepresence purposes, we have added a notebook with an integrated camera: the BCI user can see the environment through the notebook camera and can be seen by others in the notebook screen. The video/audio communication between the telepresence robot and the user’s PC is achieved by means of commercial VoIP (SkypeTM). This conﬁguration allows the BCI user to interact remotely with people.

- C. Shared Control

Driving a mobile platform remotely in a natural environment can be a complex and frustrating task. The driver has to deal with many difﬁculties starting from variations in an unknown remote environment to the reduced situational awareness, due to the visual ﬁeld of the control camera. Moreover, with an uncertain control channel such as a BCI, the user has to keep a high attention level in order to deliver the correct mental

command at the correct time. In this scenario, the role of the shared control is two–fold. On the one hand, facilitating the navigation task, by taking care of the low-level details (i.e., obstacle detection and avoidance for safety reasons), and on the other hand, trying to interpret the user’s intentions by reaching possible targets in the environment.

Furthermore, the concept of obstacles or targets is not absolute, it changes according to the user’s will. For instance, a chair in the path has to be considered an obstacle if the user manifests the intent of avoiding it. Conversely, it might be the target if the goal is to talk to somebody sitting on it. The shared control system deals with these kinds of situations by weighting possible targets or obstacles in the most appropriate way in the context of the current interaction.

Our implementation of shared control is based on the dynamical system concept coming from the ﬁelds of robotics and control theory [30], [31]. Two dynamical systems have been created which control two independent motion parameters: the angular and translation velocities of the robot. The systems can be perturbed by adding attractors or repellors in order to generate the desired behaviors. In our case the evolution of the systems is deﬁned by Eqs. 2 and 3 for the angular ('˙) and translation (v) velocity, respectively.

2 i

XN

  '

2 2

i (2)

'˙ego =

 i'ie

i=1

2K 1 + e⌧V (t)

(3)

v =

- In Eq. 2, '˙ego represents the current device angular incre-

ment and 'i the angular position at which the target-attractors ( i > 0) and the obstacle-repellors ( i < 0) are located. The locations of the attractors and repellors are locally deﬁned with respect to the ﬁxed position of the infrared sensors on the robot. The strength of  i deﬁnes the virtual force, which determines how fast the system tries to avoid the obstaclerepellors or reach the target-attractors. The range  i deﬁnes the basin of attraction or repulsion for each entry of the system.

- In Eq. 3, K is the maximum velocity the robot can reach,

modulated by the function V (and the time constant ⌧) representing the free space near the robot (Eq. 4).

V (t) = PN

k=1  k(t) k PN

(4)

i=1  i(t)

!2 k

 k = e 

2 2 (5)

In our case, we have N = 9 sensors;  k represents the value recorded by the k-sensor and !k is the angular direction of the k-sensor as shown in Figure 2. Each  k value recorded by the sensors is normalized with a Gaussian shape, having maximum value at the front of the robot, in the forward direction.

The two dynamical systems (Eq. 2 and 3) are independent and their outputs are applied directly to the motor controller of the robot. Figure 3 shows the force-ﬁelds of the instant angular and translation velocity based on these two dynamical systems for three example obstacles (repellors).

[Figure 2]

- Fig. 2. Schema of the position of the infrared sensors on the robot. The angular direction of the sensors is always referred to the direction of the robot.

From theory to practice, the dynamical system implements the following navigation modality. The default device behavior is to move forward at a constant speed. If repellors or attractors are added to the system, the motion of the device changes in order to avoid the obstacles or reach the targets. At the same time, the velocity is determined according to the proximity of the repellors that are surrounding the robot.

[Figure 3]

- Fig. 3. Force ﬁelds representing the instant angular (vector direction) and translation (vectors length) velocity for one frontal repellor placed at three different distances. The x-axis represents the positions (in degrees, with respect to the frontal direction) of the repellor. The y-axis represents the current velocity of the robot.

In this framework, if the shared control is disabled, no repellors (  < 0) are added to the system that controls the orientation of the robot (Eq. 2). The robot is changing direction only according to the user commands (attractors,   > 0). Therefore, if an obstacle is detected, the device will stop in front of it, waiting for the next mental command.

Otherwise, if the shared control is enabled, its role is to decide what has to be considered an attractor or a repellor by changing the   sign. The strength of   is related to the value read by the sensors (obstacle-repellors,   < 0) and to the commands delivered by the user directly (target-attractors,   >

- 0). Then, the robot will move smoothly, in the environment, continuously seeking the best direction/velocity according to the location of repellors/attractors.

In the next sections, we are going to use these two behaviors (with shared control, without shared control) in order to quantify the beneﬁts of shared control in a BCI-based telepresence application.

- D. Participants and end-users

Ten healthy volunteers participated in our experiments (aged 30.9±5.6, 1 female). Although some of the users were already trained in BCI, they did not have any prior experience with

the telepresence robot. In addition, users H3, H4, H9 and H10 were BCI beginners.

Nine end-users aged 40.7±11.8 years (1 female) were trained at various out-of-the-lab locations (either at clinics, assistive technology support centers or users’ homes in Switzerland, Germany and Italy), without BCI experts present and were able to control a MI-based BCI (Figure 1, left side). They trained once or twice a week (sometimes only every other week) for up to 3 hours per day, with a maximum number of 10 sessions (recording days). These nine end-users are part of a larger study involving 24 volunteers with motor disabilities who were trained to achieve BCI control before operating several BCI prototypes (speller, assistive mobility or telepresence). These requirements imposed end-users to achieve an online BCI performance better than 70% for two consecutive sessions within a maximum number of training sessions. Details of this training study and lessons learned, together with a short report of the results with the prototypes, are discussed in [3]. A thorough description of the speller and its clinical evaluation has appeared in [29]. In this work we provide a full description of the telepresence robot experiments with the end-users and compare their performances to ten healthy subjects who performed the same task. The endusers were affected by different levels of myopathy, spinal cord injury, tetraplegia, amputation, spino-cerebellar ataxia or multiple sclerosis, but none of the participants had cognitive deﬁcits. Details for each end-user are given in Table I.

All experiments were conducted according to the declaration of Helsinki and the study was approved by the corresponding local ethics review boards of the cantons of Vaud and Valais in Switzerland, and of the regional government in Bologna in Italy. All participants were asked to give written informed consent before participating in the study. Furthermore, they were explicitly instructed that they could leave the study at any time without giving any reason.

E. Experimental paradigm

The experimental environment was a natural working space with different rooms and corridors (shown in Figure 4). This map was also shown to the end-users before the experiment to explain the setup, since they never had visited this space, in contrast to the healthy users who were already familiar with the environment. The robot started from position R, and there were four target positions T1, T2, T3, T4, physically marked with white triangles on the ﬂoor. The user’s task was to drive the robot along one of three possible paths (P1, P2, P3, marked in different colors in the map), each consisting of two targets and driving back to the start position. The experimental space contains natural obstacles (i.e., desks, chairs, furniture) but also people working in this ofﬁce space were moving round, thus replicating a daily life situation where the end-user might want to drive the mobile robot to different rooms of their apartment.

During a trial, the user needed to drive the robot along one of the paths. Users were asked to perform the task as quickly and efﬁciently as possible. A trial was considered successful if the robot traveled to the two target positions and back to

TABLE I DETAILS OF END-USERS WHO PARTICIPATED IN THE EXPERIMENT, INCLUDING GENDER, MEDICAL CONDITION, TIME SINCE THE INJURY OR DIAGNOSIS AND THEIR AGE, BOTH IN YEARS. PARTICIPANTS WHOSE TIME SINCE THE INJURY IS MARKED BY “—” ARE CONGENITAL-HEREDITARY. END-USER P2 AND P7 WERE SEVERELY DISABLED AND P1 MODERATELY DISABLED. THE DISTANCE BETWEEN THE PARTICIPANTS AND THE ROBOT IS GIVEN IN KILOMETERS, EXCEPT WHEN THEY WERE ON THE SAME SITE AND LOCATED ONLY IN A DIFFERENT ROOM (DISTANCE OF 15 M, LIKE ALL THE HEALTHY PARTICIPANTS). FURTHERMORE, THE MOTOR IMAGERY (MI) PAIR USED BY EACH END-USER IS GIVEN WHEREBY “L” REPRESENTS LEFT HAND, “R” RIGHT HAND AND “F” FEET MOTOR IMAGERY.

ID Gender Medical condition Time Age Distance MI used

- P1 F Myopathy — 36.8 ⇠100km F-R
- P2 M Myopathy: spinal amyotrophy-type 2 — 32.2 ⇠100km L-F
- P3 M Tetraplegia C4 10.8 33.4 ⇠440km L-F
- P4 M Tetraplegia C6 11.8 61.2 ⇠100km L-F
- P5 M Tetraplegia C5–C6 24.5 45.8 ⇠15m L-F
- P6 M Tetraplegia C6 25.8 43.6 ⇠100km L-R
- P7 M Muscular Dystrophy (Duchenne) — 19.9 ⇠100km L-R
- P8 M Tetraplegia C3 4.7 43.8 ⇠100km L-F
- P9 M Tetraplegia C6 23.9 49.2 ⇠100km F-R

[Figure 4]

- Fig. 4. The experimental environment. The ﬁgure shows the four target positions (T1, T2, T3, T4), the robot start position (R). The three different paths are marked in blue P1, red P2 and green P3.

the start position within a limited amount of time (maximum 12min).

To control the robot, the user asynchronously sent highlevel commands for turning to the left or right with the help of two mental tasks identiﬁed by BCI. When a BCI command was delivered an attractor was placed in the shared control framework to initiate a turn towards 30 . Furthermore, in the applied shared control paradigm, low-level interaction for obstacle avoidance was undertaken by the robot, which proactively slowed down and turned to avoid obstacles as it approached them. Interestingly, if no mental command was delivered, the robot moved forward, thus implicitly executing a third driving command.

During the experiment the participants (healthy or endusers) spoke with the operator via the SkypeTM connection. The operator informed the participants when they had reached the target, since the webcam offered only a limited ﬁeld of view. Especially when the robot was very close to the target, the mark on the ﬂoor moved out of the view, and the participants could only guess for how long they had to continue the current movement of the robot to reach the target. Nevertheless, we instructed the participants to be quiet during

TABLE II FOUR EXPERIMENTAL CONDITIONS WERE TESTED: WITH OR WITHOUT SHARED CONTROL IN COMBINATION WITH BCI OR MANUAL CONTROL.

shared control activated

yes no BCI

BCI shared ctrl BCI no shared ctrl triggered Bsh Bno

turn by manual manual shared ctrl manual no shared ctrl button Msh Mno

the active control time, to avoid any artifacts in the EEG.

- 1) Telepresence experiment 1 – healthy participants: Since

the goal of this work was to evaluate the contribution of shared control for a BCI telepresence robot, the experiment with the healthy participants was run under four conditions: BCI control with shared control Bsh, BCI control without shared control Bno, manual control with shared control Msh and manual control without shared control Mno, respectively, (see Table II). In the case of manual control the user drove the robot by delivering manual commands through a keyboard (left, right arrows) and traveled each path once. In the case of BCI control the users drove the robot along each path twice. Paths were chosen in a pseudorandom order and BCI control always preceded manual control to avoid any learning effect. For each trial we recorded the total time, the number of commands sent by the user (manual or mental), and the number of commands delivered by the obstacle avoidance module (in the shared control condition). Users were instructed to generate paths as fast and as short as possible. All experimental parameters and their values are given in Table III.

- 2) Telepresence experiment 2 – end-users: Since exper-

iments with end-users are much more demanding and the results with the healthy participants in experiment 1 (see section III-B) determined the beneﬁcial role of shared control for a brain-control telepresence robot, we reduced the conditions to the two main ones: (i) BCI with shared control Bsh (ii) and, as a baseline, the normal manual control without shared control Mno. Some end-users were able to press buttons on a modiﬁed keyboard and others were using head switches.

Generally, we used whatever residual motion they were capable of producing. The number of trials, targets, paths and the extracted parameters were the same as in experiment 1 (see Table III).

TABLE III EXPERIMENTAL PARAMETERS FOR THE TELEPRESENCE TESTS.

|Number of control commands| |2|
|---|---|---|
|Number of targets per path| |2|
|Number of paths| |3|
|Number of conditions| |4|
|Number of trials per path under manual control| |1|
|Number of trials per path under BCI control| |2|
|Total number of trials| |18|
|Timeout| |12 min|

F. Subjective measures

At the end of the conditions Mno and Bsh we asked the healthy participants to subjectively rate their performance and workload via the NASA TLX (task load index) questionnaire [32], in order to evaluate which condition was preferred. Generally, the NASA-TLX is a multi-dimensional rating procedure that derives an overall subjective workload score based on a weighted average of ratings on six subscales, which include mental demands, physical demands, temporal demands, performance, effort and frustration Such an evaluation was already used and suggested in the literature to assess the usability and efﬁciency of several BCI controlled applications [27], [33].

III. RESULTS

In this section we ﬁrst present the EEG features identiﬁed for the end-users and their online BCI control during the training sessions, before presenting the experimental results for healthy participants and end-users.

A. EEG features and BCI performance

All participants started by imagining left hand, right hand and feet movements during calibration recordings. The best 2class classiﬁer was used to drive the robot in the experiments. The MI pair mostly used by the healthy group was left versus right hand (LR, 6 times), followed by feet versus right hand (FR, 3 times) and left hand versus feet (LF, once). For the end-users it was left hand versus feet (LF, 5 times), followed by feet versus right hand (FR, twice) and left versus right hand (LR, once), see in more detail in Table I.

In general, the selected features were dominantly in the alpha band (around 10Hz) and in the beta band (around 22Hz), which is consistent with the literature [34], [35], [36]. Figure 5 shows the histogram of the selected features and the corresponding electrode locations for the end-users. Features were mostly chosen around Cz and C4, which is in line with the fact that most participants used left hand MI versus feet

- MI to control the BCI.

[Figure 5]

- Fig. 5. Histogram of the selected electrode locations (top) and the selected power spectral density (bottom) for the participating end-users. Most of the features were chosen from the ↵ or   range, and were located over C4 (left hand area) and Cz (foot area).

Figure 6 shows the accuracy of all online BCI runs from the end-users. Each end-user needed a different number of sessions to learn to control the BCI. A maximum of 9 training sessions (days) were possible. Two end-users started already with a very high performance and tested the robot already after two days and another one after three sessions. End-user P2, who was one of the early participants, reported that he lost motivation since the pure BCI training was becoming boring for him and improved again when he was ﬁnally allowed to test the robot. Participants P1 and P4 had a holiday break in between the recordings, which yielded a drop of performance. Although we notice that the ﬂuctuations over the different training sessions are quite large, a general improving trend is visible for all participants (see grand average in dashed in Figure 6).

[Figure 6]

- Fig. 6. Performance values (trial accuracy) of all online training runs averaged per session for each end-user before they participated in the telepresence experiment. The mean over all end-users (dashed line) shows a slowly increasing trend.

B. Telepresence experiment 1 – healthy participants

The primary result of our experiment is that all users succeeded in all the trials for all conditions. Regarding the incorporation of shared control, it boosted the performance for both manual and BCI control in all trials for all users.

1) Time of the experiment: The ﬁrst four healthy participants (H1–H4) tested all four conditions, and the remaining six tested only the two main conditions (Bsh and Mno, same as the end-users with motor disabilities). The top part of Figure 7 shows the time needed for the four users to drive the robot along the three paths. The average time to ﬁnish the task manually was between 250 and 270s, but in the condition BCI without shared control, Bno, more than 465s were needed. This implies that this condition was very difﬁcult and demanding, which could be reduced by the shared control in Bsh to 310s. Even in the case of manual control (ﬁrst two bars in the graphs, Mno and Msh), shared control reduced the time to perform the task: user H1, 10.9±8.8%; user H2,

- 1.5±5.6%; user H3, 12.7±8.6% user H4, -1.8±2.8%. The beneﬁt of shared control becomes more evident when users drove the robot mentally (last two bars in Figure 7, Bno and Bsh): user H1, 39.3±8.1%; user H2, 12.0±9.1%; user H3, 41.2±10.8%; user H4, 28.6±7.7%.

A remarkable result of experiment 1 is that shared control allowed all the healthy users to mentally drive the telepresence robot, Bsh, almost as fast as when they did the task manually, without the support of the shared control, Mno. The average time ratio for all paths of Bsh vs. Mno and subjects was 115.15±10.32% (see also the top part of Figure 8). Note that participant H6 had a larger ratio of 1.38 than all other participants (average of 1.12), since his brain control degraded momentarily on the way to target T3 in path 3 in condition Bsh and he had to make four U-turns to reach the destination. Without this trial his ratio would drop to 1.25. Nevertheless, we left the full data in the analysis, as it reﬂects the actual use of the brain-controlled robot, and the BCI, as well as the BCI community, has to learn to deal with exactly these ﬂuctuations of performance in end-users.

2) Number of commands: Shared control also helped users to reduce the number of commands (manual or mental) that they needed to deliver to achieve the task (Figure 7, bottom). In the case of mental control, shared control led to a strong decrease (last two bars in Figure 7, Bno and Bsh): user H1, 27.6±11.1%; user H2, 34.6±10.4%; user H3, 51.4±6.3%; user H4, 32.8±20.8%. It is clearly visible that in the condition without shared control (mental Bno or manual Mno) more commands were required to reach the targets. This was expected since every obstacle had to be maneuvered around and any deviation from the path had to be corrected.

Averaging the data across the four participants, we can see a high correlation (⇢ = 0.49, p < 0.05) between the number of commands delivered by the users without or with shared control and the time needed to reach a target. This correlation was even higher for mental control (⇢ = 0.56, p < 0.05) when all 10 participants were taken into account. For all targets we observe the same general trend: shared control allowed the users to deliver signiﬁcantly fewer commands and reach the target faster.

C. Telepresence experiment 2 – end-users

As a benchmark of task complexity, the average time for healthy participants to complete a single path in the manual

[Figure 7]

Fig. 7. Time (top) and number of commands (bottom) necessary to drive the robot along the three paths (average over all 3 paths is given) for each healthy participant. The grand average with standard deviation is given in the last column. Mno stands for manual control without shared control –our reference condition for experiment 2–, Msh for manual control with shared control, Bno for BCI control without shared control, and Bsh for the most important condition BCI with shared control. Shared control (for manual and BCI control) reduced the time and the number of commands needed to achieve the task, which is an indicator of a reduced workload. Most importantly BCI with shared control Bsh was almost as good as manual control Mno.

condition Mno was 255±36 seconds, whereas for end-users it was 264±74 seconds (no statistical difference, p > 0.1, two-sampled t-test). Concerning the number of commands in this condition, healthy participants used an average 23±11 commands, compared to 24±8 for end-users (no statistical difference, p > 0.5, two-sampled t-test). These values can be considered as the reference baseline.

Due to personal reasons, end-user P2 was unable to ﬁnish the experiments and voluntarily left the study. For him, only the data from the ﬁrst path was recorded and was used in the analysis. During the second path of the experiment Bsh, enduser P1 delivered a number of incorrect mental commands, believing that the target was elsewhere. Hence it took some time and additional commands to bring the robot back to the correct target and path. Therefore, this data point can be considered an anomaly and was excluded from our analysis.

All end-users succeeded to mentally control the telepresence robot as efﬁciently as the healthy participants or even slightly better (see Figure 8). First, the mean ratio of time to complete the task for the BCI condition compared with the manual condition was only 109.2±11.1% for the end-users, as compared to 115.1±10.3% for the healthy participants (no statistical difference, p > 0.1, two-sampled t-test), see also Figure 8, top. This indicates a reduced BCI handicap for end-users. Second, the mean ratio of the number commands required to complete the task for the BCI condition compared with manual condition was only 92.8±37.9% for the end-users as opposed to 106.5±30.8% for the healthy participants (no statistical difference, p > 0.4, two-sampled t-test), see also Figure 8, bottom.

When controlling neuroprosthetic devices it is of interest to see how much of the BCI performance can be transferred from the standard on-screen BCI training sessions directly to

[Figure 8]

- Fig. 8. (top) Ratio between the time required to complete the task when using BCI and when using the manual input device. (bottom) The ratio of the number of commands required to complete the task between the BCI and the manual condition. (both) Healthy participants are plotted in blue and end-users in red. On the right hand side the grand average and standard deviation is given for each group population. The most striking result is that end-users succeeded in controlling the telepresence robot just as well as the healthy participants.

the control of applications. Therefore, in Figure 9, we made a correlation between the online BCI performance during the training runs (data taken from Figure 6) and the number of delivered commands during the telepresence experiment (data taken from Figure 8). A positive correlation of ⇢ = 0.46 (p < 0.05) can be found between them, indicating that endusers who have a better BCI performance tend to deliver more commands in the robot control. A positive trend, although lower, was also observed for healthy subjects.

[Figure 9]

- Fig. 9. Ability to control applications for healthy participants (H) and endusers with motor disabilities (P). The averaged online BCI performance (on the y-axis) for each end-user is plotted over the number of commands (on the x-axis) delivered in telepresence experiment. A positive linear trend is visible for both groups, indicating that the higher the BCI performance the more commands will be issued.

D. Subjective measures

Considering the overall task, there was a signiﬁcant increase in the NASA TLX (p < 0.05) when using BCI control (condition Bsh) compared to manual control (condition Mno). The subjective data of the healthy participants are given in Figure 10 (N=9, data of H2 were corrupted). Since the task did not differ, the same TLX weights were used for both conditions. Therefore, the main contributing factors to the change in TLX were the users’ perceived increase in mental workload (p < 0.01) and effort (p < 0.05), as can also clearly be seen in Figure 10. Increasing trends, but no statistical differences, can be observed in the temporal demand, perceived performance and frustration. A signiﬁcant decrease (opposite trend to above) was rated for the physical demand (p < 0.05).

[Figure 10]

Fig. 10. The NASA TLX: perception of the overall task for the two main conditions (manual control without shared control Mno and BCI with shared control Bsh) in healthy participants. Each bar represents the 25th to 75th percentiles and the central mark is the median value, the tiny lines extend to the most extreme data points not considering outliers, which are plotted individually. Statistical signiﬁcant differences are marked (* p < 0.05, ** p < 0.01). Note: For all factors (user-perceived performance included) a lower score is better (i.e., a score of 0 would be the best).

IV. DISCUSSION

The experimental results reported in this paper demonstrate that: (i) end-users with motor disabilities can mentally control a telepresence robot via a BCI. Controlling such a telepresence robot is a rather complex task as the robot is continuously moving and the user must control it for a long period of time (well over 6 minutes without breaks) to move along the whole path and reach the targets. (ii) The proposed shared control approach allows users to achieve similar performances with the BCI as would have been possible under direct manual control of a robotic device. Our shared control implementation only deals with low-level obstacle detection and avoidance, but leaves the high-level decisions to the user. It is important to note that only with a semi-autonomous approach is the user able to maintain the ﬁnal control authority over the device all the time. (iii) End-users could improve their BCI performance and modulate their brain patterns better with practice. (iv) Participants can transfer the skill of mental control, from the standard on-screen BCI training sessions directly to the control of applications, in our case the telepresence robot. Good BCI performance is an indicator for successful application control and good BCI users tend to pro-actively deliver more commands as to keep a more direct control. (v) Finally, the most striking result is that no performance difference was found between end-users with motor disabilities and healthy participants in controlling the telepresence robot. This is even more so when considering that the healthy participants were familiar with the environment, while end-users were not.

Interestingly, good BCI users, such as end-user P7 and P8 or healthy participant H8, deliver many more mental commands than the other users. This behavior actually reﬂects a voluntary will to be in full control of the telepresence robot, which is permitted by the semiautonomous shared control system [22]. On the other hand, it is obvious that end-users who have a lower BCI performance and therefore difﬁculties in ﬁne control of the robot, trust the shared control system more, to avoid obstacles or to correct path deviations. Therefore, they prefer to wait and assess how the system is assisting them and only then they start interacting via the BCI.

The implemented shared control approach allowed each participant to complete a rather complex task in shorter times and with fewer commands independently of mental or manual control. Given that the number of commands to complete the task can be considered an indirect measure of workload, we argue that shared control reduces the users’ cognitive workload, which is in line with the anecdotal statement of the participants. Shared control assists them in coping with low-level navigation issues (such as obstacle avoidance) and helps BCI users to maintain attention for longer periods of time, resulting in delivering fast commands.

A reduction in workload for the Bsh, although still higher than in the Mno condition, is also supported by the subjective results we acquired with the NASA TLX questionnaire in healthy participants. These results are in line with the expected outcome, namely that BCI control is mentally more demanding (using brain control versus ﬁnger activity) and needs a higher effort (focused activity on the BCI versus automated button

presses) than manual control (which is the only condition with some physical action, therefore receiving a small but higher rating in the physical demand). Nevertheless, no difference was reported in the performance or frustration level.

We also observed that, to drive a brain-controlled robot, users do not only need to have a rather good BCI performance, but they also need to be fast in delivering the appropriate mental command at the correct time —otherwise they will miss key maneuvers to achieve the task efﬁciently (e.g., turning to pass a doorway or enter a corridor). In our experience, fast decision making is critical and it depends on the proﬁciency of the users as well as on their attention level. Along the same lines, another maybe even more critical ability that BCI users must exhibit is intentional non-control, which allows them to rest while the neuroprosthesis is in a state they do not want to change (e.g., moving straight along a corridor). The evidence accumulation framework applied in our BCI implicitly supports INC by tackling the uncertainty of the single-sample classiﬁer output, thus providing a smooth and informative feedback, while eliminating false positives.

Nevertheless, an explicit start/stop or on/off functionality would be preferable. Especially, to facilitate the interaction aspect that underpins the notion of telepresence, users must be able to voluntarily and reliably stop the robot at any moment, not just drive from point to point. In the given example the participants were only able to stop the robot when the shared control system determined that they wished to dock to a particular target. Then, to remain stationary, they had to actively maintain the INC condition, which has proven to be demanding (high workload). A solution to this limitation is to adopt the hybrid BCI principle [28], [37], [38]. Thereby, a complementary channel (which can be reliable but not constantly used) is added to the EEG-based BCI to enable the user to start/stop the robot. This has been recently demonstrated in healthy participants [39] exploiting the user’s residual muscular activity. The same principle was also shown for a hybrid text-entry system in end-users [29]. This hybrid approach increases the accuracy, whilst simultaneously reducing the workload, and was the preferred control paradigm of all the participants.

The work reported here highlights how critical it is to include the individual end-users in the whole design process of a BCI, as it is customary in the ﬁeld of assistive technologies. The BCI and the application have to be tailored to every participant, to adapt to their performance, needs and preferences. Therefore, a user-centered design (UCD) approach should be followed [40], which focuses on the usability for the end-users –i.e., how well a speciﬁc technology suits their purposes, and meets their needs and requirements. An UCD has been shown to be of key importance for end-users to actually utilize a BCI application [27].

In the current paper, shared control only deals with lowlevel obstacle avoidance and it relies on very simple infrared sensors (as opposed to sophisticated and expensive laser range ﬁnders on the wheelchairs). The next implementation of shared control will incorporate simple vision modules for obstacle avoidance and, even more important, recognition of natural targets (such as humans and tables) that will increase the

operational range of the robot. The applied and tested shared control protocols and experimental paradigm of this work can be easily transferred to other BCI controlled neuroprosthetic devices, such as brain-controlled wheelchairs [12], upper limb orthoses [9] or lower limb exoskeletons [41]. Shared control will be also combined with our approach to support idle states so that users can deliver commands only when they wish to do so [8], thus enlarging users’ telepresence experience.

In our work we used self-paced induced activity of the motor cortex to asynchronously control the movements of the robot. Nevertheless, other BCI paradigms and brain signals have also been used to control a telepresence robot, or other robotic devices. Evoked activity like P300 has been used to either select ﬁnal targets that the robot reaches autonomously [14] or to select the next forward or left/right turning [17], [42]. Another alternative is covert visuospatial attention measured by fMRI, so that the healthy participants only had to focus their attention on the spatially distributed commands around the screen [43]. Nevertheless, the speed of control is reduced for fMRI-based systems (e.g., every 16 seconds in [43]). Similarly, a P300-based system needed quite some time for the target selection (stimulus round time plus interstimulus interval times the number of ﬂashing repetitions), so that in [17] the robot was waiting half of the time for the BCI decoding. This resulted in 4 selections per minute, but of course with a higher number of commands than in our experiment. In our opinion, depending on the setup, several options exist: the selection of targets out of a large list, which can then be autonomously reached is perfect for such a P300 approach, but if the user wants to interact more directly and have a personalized degree of control, approaches based on spontaneous activity like MI will be preferred. Since this paper focused only on brain control for end-users, we will not discuss any muscle or eye-tracking controlled robotic devices.

Moreover, smart interface designs and hybrid approaches, which have been shown to help overcome existing shortcomings in BCI [9], [28], [37], will be increasingly used for robotic control and will push the boundaries of performance. We are beginning to see examples of robot control with hybrid systems [39], [44], extensions to multi-class control of robotic devices via a smaller set of control signals [15], [45], and even full control in three-dimensional space [16], which demonstrates the potential of brain-controlled physical devices for healthy participants.

Compared to all these works above, a major novelty of our work is the evaluation with a larger number of endusers and not only with healthy participants. Nevertheless, it is difﬁcult to compare our work effectively with other end-user or patient works, since (i) the control tasks were different or (ii) the paper mentioned only the achieved navigation task, but neither reported a control condition (like our manual keyboard control condition) nor the chance level performance, or (iii) did not compare the performance of their end-users with healthy participants to see the task complexity. Such comparisons would be very useful for the future of this research ﬁeld.

V. CONCLUSIONS

In this work we have discussed and evaluated the role of shared control in a BCI-based telepresence framework: driving a mobile robot via a BCI might improve the quality of life of people suffering from severe physical disabilities. By means of a bidirectional audio/video connection to a robot, the BCI user would be able to interact actively with relatives and friends located in different rooms. However, direct control of such robots through an uncertain channel such as a BCI is complicated and exhausting. Shared control can facilitate the operation of brain-controlled telepresence robots, as demonstrated by the experimental results reported here. In fact, it allowed all users (healthy and motor-disabled) to complete a rather complex task —driving the robot in a natural environment along a path with several targets and obstacles— in shorter times and with fewer mental commands, than without the help of shared control. Thus, we argue that shared control reduces the user’s cognitive workload. Yet, as we have seen, the shared control provides enough ﬂexibility that very good BCI users were able to wield a much higher level of control authority, by delivering more mental commands than those who relied more upon the assistance of the shared control system. Finally, the end-users with motor disabilities were able to complete the remote navigation tasks successfully and just as well as healthy participants.

ACKNOWLEDGMENT

This research was supported by the European ICT Programme Project FP7-224631 (TOBI) and the Swiss National Science Foundation through the NCCR Robotics. The ﬁnal phase of this work was also supported by the Swiss canton of Valais-Wallis and by the City of Sion. This paper only reﬂects the author’s views and funding agencies are not liable for any use that may be made of the information contained herein. The authors would like to thank all patients and endusers for their participation, and all therapists, caregivers and employees working on the different recording sites (Clinique Romande de R´eadaptation-Suvacare, Switzerland; Klinik f¨ur Paraplegiologie, Universit¨atsklinikum Heidelberg, Germany; Associazione Italiana per l’Assistenza agli Spastici, Bologna, Italy) for their supporting work.

REFERENCES

- [1] S. Moghimi, A. Kushki, A. Marie Guerguerian, and T. Chau, “A review of EEG-based brain-computer interfaces as access pathways for individuals with severe disabilities,” Assistive Technology, vol. 25, no. 2, pp. 99–110, 2013.
- [2] F. Gal´an, M. Nuttin, E. Lew, P. W. Ferrez, G. Vanacker, J. Philips, and J. d. R. Mill´an, “A brain-actuated wheelchair: Asynchronous and noninvasive brain-computer interfaces for continuous control of robots.” Clin Neurophysiol, vol. 119, no. 9, pp. 2159–2169, 2008.
- [3] R. Leeb, S. Perdikis, L. Tonin, A. Biasiucci, M. Tavella, A. Molina, A. Al-Khodairy, T. Carlson, and J. d. R. Mill´an, “Transferring braincomputer interfaces beyond the laboratory: Successful application control for motor-disabled users,” Artif Intell Med, vol. 59, no. 2, pp. 121– 132, 2013.
- [4] M. Velliste, S. Perel, M. C. Spalding, A. S. Whitford, and A. B. Schwartz, “Cortical control of a prosthetic arm for self-feeding.” Nature, vol. 453, no. 7198, pp. 1098–1101, 2008.

- [5] J. M. Carmena, M. A. Lebedev, R. E. Crist, J. E. O’Doherty, D. M. Santucci, D. F. Dimitrov, P. G. Patil, C. S. Henriquez, and M. A. L. Nicolelis, “Learning to control a brain-machine interface for reaching and grasping by primates.” PLoS Biol, vol. 1, no. 2, p. E42, 2003.
- [6] J. L. Collinger, B. Wodlinger, J. E. Downey, W. Wang, E. C. TylerKabara, D. J. Weber, A. J. C. McMorland, M. Velliste, M. L. Boninger, and A. B. Schwartz, “High-performance neuroprosthetic control by an individual with tetraplegia.” Lancet, vol. 381, no. 9866, pp. 557–564, 2013.
- [7] G. M¨uller-Putz, R. Scherer, G. Pfurtscheller, and R. Rupp, “EEG-based neuroprosthesis control: A step towards clinical practice,” Neurosci Lett, vol. 382, pp. 169–174, 2005.
- [8] M. Tavella, R. Leeb, R. Rupp, and J. d. R. Mill´an, “Towards natural non-invasive hand neuroprostheses for daily living,” in Conf Proc IEEE Eng Med Biol Soc, 2010, pp. 126–129.
- [9] M. Rohm, M. Schneiders, C. M¨uller, A. Kreilinger, V. Kaiser, G. R. M¨uller-Putz, and R. Rupp, “Hybrid brain-computer interfaces and hybrid neuroprostheses for restoration of upper limb functions in individuals with high-level spinal cord injury,” Artif Intell Med, vol. 59, no. 2, pp. 133 – 142, 2013.
- [10] J. d. R. Mill´an, F. Renkens, J. Mouri˜no, and W. Gerstner, “Noninvasive brain-actuated control of a mobile robot by human EEG,” IEEE Trans Biomed Eng, vol. 51, no. 6, pp. 1026–1033, 2004.
- [11] L. Tonin, T. Carlson, R. Leeb, and J. d. R. Mill´an, “Brain-controlled telepresence robot by motor-disabled people,” in Conf Proc IEEE Eng Med Biol Soc, 2011, pp. 4227–4230.
- [12] T. Carlson and J. d. R. Mill´an, “Brain–controlled wheelchairs: A robotic architecture,” IEEE Robot Automat Mag, vol. 20, no. 1, pp. 65–73, 2013.
- [13] I. Iturrate, J. Antelis, A. K¨ubler, and J. Minguez, “A noninvasive brainactuated wheelchair based on a P300 neurophysiological protocol and automated navigation,” IEEE Trans Robot, vol. 25, no. 3, pp. 614–627, 2009.
- [14] B. Rebsamen, G. Cuntai, Z. Haihong, W. Chuanchu, T. Cheeleong, M. H. Ang, and E. Burdet, “A brain controlled wheelchair to navigate in familiar environments,” IEEE Trans Neural Syst Rehab Eng, vol. 18, no. 6, pp. 590 –598, 2010.
- [15] K. LaFleur, K. Cassady, A. Doud, K. Shades, E. Rogin, and B. He, “Quadcopter control in three-dimensional space using a noninvasive motor imagery-based brain-computer interface,” J Neural Eng, vol. 10, no. 4, p. 046003, 2013.
- [16] A. J. Doud, J. P. Lucas, M. T. Pisansky, and B. He, “Continuous threedimensional control of a virtual helicopter using a motor imagery based brain-computer interface,” PLoS ONE, vol. 6, no. 10, p. e26322, 10 2011.
- [17] C. Escolano, J. Antelis, and J. Minguez, “A telepresence mobile robot controlled with a noninvasive brain-computer interface,” IEEE Trans Syst Man Cybern B, vol. 42, no. 3, pp. 793–804, June 2012.
- [18] T. Carlson and Y. Demiris, “Collaborative control for a robotic wheelchair: Evaluation of performance, attention, and workload,” IEEE Trans Syst Man Cybern B, vol. 43, no. 3, pp. 876–888, 2012.
- [19] O. Flemisch, A. Adams, S. Conway, K. Goodrich, M. Palmer, and P. Schutte, “The H-Metaphor as a guideline for vehicle automation and interaction,” NASA, Tech. Rep. NASA/TM–2003-212672, 2003.
- [20] D. Vanhooydonck, E. Demeester, M. Nuttin, and H. Van Brussel, “Shared control for intelligent wheelchairs: An implicit estimation of the user intention,” in Conf Proc Advances Service Robot, 2003, pp. 176–182.
- [21] W. Burgard, A. Cremers, D. Fox, D. H¨ahnel, G. Lakemeyer, D. Schulz, W. Steiner, and S. Thrun, “Experiences with an interactive museum tourguide robot,” Artiﬁ Intell, vol. 114, pp. 3–55, 1999.
- [22] P. Nisbet, “Who’s intelligent? Wheelchair, driver or both?” in Conf Proc IEEE Control Applicat, Glasgow, Scotland, U.K., September 2002.
- [23] K. Tahboub, “A semi-autonomous reactive control architecture,” J Intell Robot Syst, vol. 32, pp. 445–459, 2001.
- [24] L. Tonin, R. Leeb, M. Tavella, S. Perdikis, and J. d. R. Mill´an, “The role of shared-control in BCI-based telepresence,” in Conf Proc IEEE Conf Syst Man Cybern, 2010, pp. 1462–1466.
- [25] J. Philips, J. d. R. Mill´an, G. Vanacker, E. Lew, F. Gal´an, P. Ferrez, H. Van Brussel, and M. Nuttin, “Adaptive Shared Control of a BrainActuated Simulated Wheelchair,” in Conf Proc IEEE Conf Rehabil Robot, 2007, pp. 408–414.
- [26] J. d. R. Mill´an, P. W. Ferrez, F. Gal´an, E. Lew, and R. Chavarriaga, “Non-invasive brain-machine interaction,” Int J Pattern Recogn, vol. 22, no. 5, pp. 959–972, 2008.
- [27] A. K¨ubler, E. Holz, A. Riccio, C. Zickler, T. Kaufmann, S. Kleih, P. Staiger-S¨alzer, L. Desideri, E. Hoogerwerf, and D. Mattia, “The user-

- centered design as novel perspective for evaluating the usability of BCIcontrolled applications,” PLoS One, vol. 9, no. 12, p. e112392, 2014.
- [28] J. d. R. Mill´an, R. Rupp, G. M¨uller-Putz, R. Murray-Smith, C. Giugliemma, M. Tangermann, C. Vidaurre, F. Cincotti, A. K¨ubler, R. Leeb, C. Neuper, K. M¨uller, and D. Mattia, “Combining braincomputer interfaces and assistive technologies: State-of-the-art and challenges,” Front Neurosci, vol. 4, p. 161, 2010.
- [29] S. Perdikis, R. Leeb, J. Williamson, A. Ramsay, M. Tavella, L. Desideri, E.-J. Hoogerwerf, A. Al-Khodairy, R. Murray-Smith, and J. d. R. Mill´an, “Clinical evaluation of BrainTree, a motor imagery hybrid BCI speller,” J Neural Eng, vol. 11, no. 3, p. 036003, 2014.
- [30] A. Steinhage and G. Schoner, “The dynamic approach to autonomous robot navigation,” Conf Proc IEEE Ind Electron, vol. 1, p. SS7, 1997.
- [31] G. Sch¨oner, M. Dose, and C. Engels, “Dynamics of behavior: Theory and applications for autonomous robot architectures,” Robot Autonomous Syst, vol. 16, pp. 213–245, 1995.
- [32] S. Hart and L. Staveland, “Development of NASA-TLX (task load index): Results of empirical and theoretical research,” in Human Mental Workload, P. Hancock and N. Meshkati, Eds. North-Holland, 1988, pp. 139–83.
- [33] T. Carlson, R. Leeb, R. Chavarriaga, and J. d. R. Mill´an, “Online modulation of the level of assistance in shared control systems,” in Proceedings of the IEEE International Conference on Systems Man and Cybernetics (SMC 2012), 2012, pp. 3321–3326.
- [34] G. Pfurtscheller and F. H. Lopes da Silva, “Event-related EEG/MEG synchronization and desynchronization: Basic principles,” Clin Neurophysiol, vol. 110, pp. 1842–1857, 1999.
- [35] J. Decety, “The neurophysiological basis of motor imagery.” Behav Brain Res, vol. 77, no. 1-2, pp. 45–52, 1996.
- [36] J. Wolpaw, N. Birbaumer, D. McFarland, G. Pfurtscheller, and T. Vaughan, “Brain-computer interfaces for communication and control.” Clin Neurophysiol, vol. 113, no. 6, pp. 767–791, 2002.
- [37] G. Pfurtscheller, B. Allison, G. Bauernfeind, C. Brunner, T. Solis Escalante, R. Scherer, T. Zander, G. M¨uller-Putz, C. Neuper, and N. Birbaumer, “The hybrid BCI,” Front Neurosci, vol. 4, p. 42, 2010.
- [38] R. Leeb, H. Sagha, R. Chavarriaga, and J. d. R. Mill´an, “A hybrid braincomputer interface based on the fusion of electroencephalographic and electromyographic activities.” J Neural Eng, vol. 8, no. 2, p. 025011, 2011.
- [39] T. Carlson, L. Tonin, S. Perdikis, R. Leeb, and J. d. R. Mill´an, “A hybrid BCI for enhanced control of a telepresence robot,” in Conf Proc IEEE Eng Med Biol Soc, October 2013, pp. 1044–1049.
- [40] ISO 9241-210 (2008) Ergonomics of human system interaction - Part 210: Human-centred design for interactive systems (formerly known as 13407), International Organization for Standardization (ISO) Std.
- [41] J. L. Contreras-Vidal and R. G. Grossman, “Neurorex: a clinical neural interface roadmap for EEG-based brain machine interfaces to a lower body robotic exoskeleton.” Conf Proc IEEE Eng Med Biol Soc, vol. 2013, pp. 1579–1582, 2013.
- [42] T. Kaufmann, A. Herweg, and A. Kubler, “Toward brain-computer interface based wheelchair control utilizing tactually-evoked event-related potentials,” J Neuroeng Rehabil, vol. 11, no. 1, p. 7, 2014.
- [43] P. Andersson, J. Pluim, M. Viergever, and N. Ramsey, “Navigation of a telepresence robot via covert visuospatial attention and real-time fMRI,” Brain Topogr, vol. 26, no. 1, pp. 177–185, 2013.
- [44] A. Finke, B. Rudgalwis, H. Jakusch, and H. Ritter, “Towards multi-user brain-robot interfaces for humanoid robot control,” in Conf Proc IEEE Humanoid Robot, Nov 2012, pp. 532–537.
- [45] V. Gandhi, G. Prasad, D. Coyle, L. Behera, and T. McGinnity, “EEGbased mobile robot control through an adaptive brain-robot interface,” IEEE Trans Syst Man Cybern B, vol. 44, no. 9, pp. 1278–1285, Sept 2014.

Robert Leeb (M’03) is scientist and chief-engineer at the Center for Neuroprosthetics at Ecole´ Polytechnique F´ed´erale de Lausanne (EPFL) in Sion in Switzerland, where he works on the transfer of brain-computer interface (BCI) technology towards its clinical partner at the Clinique Romande de R´eadaptation (SUVA) in Sion. Furthermore, he is senior post-doctoral researcher at the Chair in NonInvasive Brain-Machine Interface at EPFL, where he works on hybrid BCI and the application of BCI technology towards patients. He holds a M.Sc.

[Figure 11]

degree in electrical and biomedical engineering from Graz University of Technology, Austria, and received his Ph.D. in Computer Science from Graz University of Technology, Austria. His research interests include brain-computer interfaces (BCI) systems, neuro-rehabilitation devices, neurotechnology, biosignal processing, hybrid BCI approaches, multi-modal human computer interaction and virtual reality systems.

Tom Carlson (M’06) received the M.Eng. (2006) in electronic engineering and the Ph.D. (2010) in intelligent robotics, under the supervision of Dr. Y. Demiris at Imperial College London, U.K.. He then pursued 3.5 years of postdoctoral research in Prof. J.d.R. Mill´an’s lab (CNBI) at the Ecole´ Polytechnique F´ed´erale de Lausanne (EPFL), Switzerland. Since 2013, Tom has held a Lectureship in the Aspire Centre for Rehabilitation Engineering and Assistive Technology at University College London. He co-founded the IEEE SMC Technical Committee

[Figure 12]

on Shared Control in 2012, which he co-chaired for three years. His primary research interests include human-robot interaction, shared control systems and assistive and rehabilitative technologies.

Luca Tonin received his Ph.D. at the Ecole´ Polytechnique F´ed´erale de Lausanne (EPFL, Lausanne, Switzerland) in 2013. Since October 2013 is working as Post-Doc at the Intelligent Autonomous System laboratory (IAS-Lab) in the University of Padua, Italy. In March 2014 he was co-founder and board member of EXiMotion s.r.l., a start-up company focused on research and development of Assistive Technology. His research is currently focused in exploring novel applications of Brain-Computer Interfaces for control and rehabilitation purposes. In

[Figure 13]

particular, he is investigating the role of BCI in the framework of cognitive rehabilitation from spatial neglect syndrome in post-stroke patients. Furthermore, his research interests include assistive technology, neurorehabilitation devices, biosignal processing and mobile robots

Martin Rohm received the diploma degree in electrical engineering from the Technical University of Darmstadt, Germany, in 2008. Since 2008, he is employed in the research group “Experimental Neurorehabilitation” (Dr.-Ing. R. Rupp) of the Spinal Cord Injury Center (Prof. N. Weidner) of Heidelberg University Hospital, Germany. He is author of more than 25 journal and conference contributions. His research is dedicated to the ﬁeld of rehabilitation engineering for individuals with spinal cord injury. This includes Functional Electrical Stimulation

[Figure 14]

mainly of the upper extremity, application of Brain-Computer Interfaces and the use of impedance tomography for determining the human bladder volume.

Lorenzo Desideri was born in Bologna, Italy, in 1983. He received the Master’s degree (with honors) in Applied Cognitive Psychology and the 2nd level specialization degree in Health Psychology from the University of Bologna, Bologna, Italy, in 2007 and 2014 respectively. He is currently a Ph.D. student at CAPHRI - School for Public Health and Primary Care, University of Maastricht, Maastricht, Netherlands, and works as researcher at Ausilioteca Living Lab at Corte Roncati Center for Disabilities – Az. USL Bologna, Bologna, Italy. With a multidisci-

[Figure 15]

plinary background in applied cognitive psychology, cognitive and behavioral psychotherapy, assistive technology, and health services research, he has working experience in EU funded research projects, academia and public health sector. His research interests are digital technology supporting the cognitive and social development of people with intellectual, language and speciﬁc learning disabilities

Jos´e del R. Mill´an is the Deﬁtech Professor at the Ecole´ Polytechnique F´ed´erale de Lausanne (EPFL) where he explores the use of brain signals for multimodal interaction and, in particular, the development of brain-controlled robots and neuroprostheses. In this multidisciplinary research effort, Dr. Mill´an is bringing together his pioneering work on the two ﬁelds of brain-machine interfaces and adaptive intelligent robotics. He received his Ph.D. in computer science from the Univ. Polit`ecnica de Catalunya (Barcelona, Spain) in 1992. He was a research scien-

[Figure 16]

tist at the Joint Research Centre of the European Commission in Ispra (Italy), a senior researcher at the Idiap Research Institute in Martigny (Switzerland), and a visiting scholar at the Universities of Stanford and Berkeley as well as at the International Computer Science Institute in Berkeley. His research on brainmachine interfaces was nominated ﬁnalist of the European Descartes Prize 2001 and he has been named Research Leader 2004 by the journal Scientiﬁc American for his work on brain-controlled robots. He is the recipient of the IEEE Nobert Wiener Award 2011 for his seminal and pioneering contributions to non-invasive brain-machine interfaces. Dr. Mill´an has coordinated a number of European projects on brain-machine interfaces.

