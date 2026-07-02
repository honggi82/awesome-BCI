BRIEF RESEARCH REPORT published: 28 June 2022 doi: 10.3389/fnbot.2022.918001

[Figure 1]

# Shared Control of Bimanual Robotic Limbs With a Brain-Machine Interface for Self-Feeding

David A. Handelman1, Luke E. Osborn1, Tessy M. Thomas2†, Andrew R. Badger1, Margaret Thompson1, Robert W. Nickl3, Manuel A. Anaya3, Jared M. Wormley1, Gabriela L. Cantarero3, David McMullen4, Nathan E. Crone5, Brock Wester1, Pablo A. Celnik3, Matthew S. Fifer1 and Francesco V. Tenore1*

1 Department of Research and Exploratory Development, Johns Hopkins University Applied Physics Laboratory, Laurel, MD,

- United States, 2 Department of Biomedical Engineering, Johns Hopkins University School of Medicine, Baltimore, MD,
- United States, 3 Department of Physical Medicine and Rehabilition, Johns Hopkins Medicine, Baltimore, MD, United States,
- 4 National Institute of Mental Health, National Institutes of Health, Bethesda, MD, United States, 5 Department of Neurology, Johns Hopkins Medicine, Baltimore, MD, United States

Advances in intelligent robotic systems and brain-machine interfaces (BMI) have helped restore functionality and independence to individuals living with sensorimotor deﬁcits; however, tasks requiring bimanual coordination and ﬁne manipulation continue to remain unsolved given the technical complexity of controlling multiple degrees of freedom (DOF) across multiple limbs in a coordinated way through a user input. To address this challenge, we implemented a collaborative shared control strategy to manipulate and coordinate two Modular Prosthetic Limbs (MPL) for performing a bimanual selffeeding task. A human participant with microelectrode arrays in sensorimotor brain regions provided commands to both MPLs to perform the self-feeding task, which included bimanual cutting. Motor commands were decoded from bilateral neural signals to control up to two DOFs on each MPL at a time. The shared control strategy enabled the participant to map his four-DOF control inputs, two per hand, to as many as 12 DOFs for specifying robot end effector position and orientation. Using neurally-driven shared control, the participant successfully and simultaneously controlled movements of both robotic limbs to cut and eat food in a complex bimanual self-feeding task. This demonstration of bimanual robotic system control via a BMI in collaboration with intelligent robot behavior has major implications for restoring complex movement behaviors for those living with sensorimotor deﬁcits.

Edited by: Giacomo Valle,

ETH Zürich, Switzerland Reviewed by:

John E. Downey, The University of Chicago,

United States Solaiman Shokur, Swiss Federal Institute of Technology Lausanne, Switzerland

*Correspondence: Francesco V. Tenore

francesco.tenore@jhuapl.edu

†Present address:

Tessy M. Thomas, The University of Texas Health

Science Center at Houston, Houston, TX, United States

Received: 11 April 2022 Accepted: 25 May 2022

Published: 28 June 2022

Citation: Handelman DA, Osborn LE,

Keywords: human machine teaming, brain computer interface (BCI), bimanual control, robotic shared control, activities of daily living (ADL)

Thomas TM, Badger AR, Thompson M, Nickl RW, Anaya MA,

## INTRODUCTION

Wormley JM, Cantarero GL, McMullen D, Crone NE, Wester B, Celnik PA, Fifer MS and Tenore FV

Individuals living with sensorimotor impairments, such as a spinal cord injury, are faced with challenges in navigating their environments and completing daily tasks, including self-feeding. Brain-machine interfaces (BMI) have the potential to increase the independence of such individuals by providing control signals to prosthetic limbs and re-enabling activities of daily living (ADLs) (Collinger et al., 2013; Aﬂalo et al., 2015; Thomas et al., 2020).

(2022) Shared Control of Bimanual Robotic Limbs With a Brain-Machine

Interface for Self-Feeding. Front. Neurorobot. 16:918001. doi: 10.3389/fnbot.2022.918001

Cortical BMIs can be used to restore function by decoding neural signals for a variety of applications including handwriting (Willett et al., 2021), restoring speech (Moses et al., 2021), perceiving artiﬁcial stimulation (Armenta Salas et al., 2018; Fifer et al., 2022), controlling external robotic limbs with closedloop sensory feedback (Flesher et al., 2021), or combined with other assistive technologies (McMullen et al., 2014; Downey et al., 2016). Others have demonstrated the use of cortical BMIs for driving functional electrical stimulation to allow users to volitionally control their limb for completing tasks such as drinking (Ajiboye et al., 2017; Colachis et al., 2018).

As invasive cortical BMIs become more advanced, one challenge that remains is robust control of bimanual robotic limbs with high degrees of freedom (DOFs). Researchers have demonstrated bimanual control of virtual arms using neural signals from bilateral frontal and parietal cortical areas in nonhuman primates (Iﬀt et al., 2013). Prior work has demonstrated eﬀective control of seven (Collinger et al., 2013) and even up to 10 (Wodlinger et al., 2015) DOFs in individuals using an invasive cortical BMI to move anthropomorphic robotic limbs; however, despite these impressive advances the need for bimanual control of two robotic limbs for more complex tasks of daily living requires control over as many as 34 DOFs, if using highly dexterous robotic limbs (Johannes et al., 2020). To address this challenge, advanced strategies, such as shared control, could help signiﬁcantly reduce the required DOFs needed to eﬀectively complete tasks requiring two arms while using a BMI.

Shared control systems, where the BMI user and a semiautonomous robot combine eﬀorts to accomplish tasks, can further increase user independence in a variety of ways. One method is a form of supervisory shared control where the robot knows how to perform tasks and the BMI user provides target goals for the robot (Katyal et al., 2013; McMullen et al., 2014; Tang and Zhou, 2017). In this case, an “inner loop” control system drives robot movement and the BMI user provides “outer loop” control, such as telling the robot which object to pick up. The approach we describe here is a form of collaborative shared control, in which a subset of the robot DOFs are controllable by the BMI user at select task-speciﬁc times, or through mode-switches initiated by the user. The BMI user and robot share the main control loop and the intent is to leverage the limited command signals provided by the BMI to enable the user to customize robot behavior. A third approach could be to combine supervisory and collaborative shared control, where for a given task some subtasks are performed by the robot given target goals (supervisorye.g., BMI user indicates which glass to pick up) whereas other subtasks involve real time input from the BMI user (collaborative—e.g., user controls how quickly to pour contents of glass).

Here, we describe an experimental setup aimed at testing a collaborative shared control approach in which a BMI user controlling up to four combined bilateral degrees-of-freedom completes a bimanual self-feeding task similar to Task 1 of the Arm Motor Ability Test [AMAT (Kopp et al., 1997)] (Figure 1A).

METHODS Human Participant Testing and Regulatory Information

The participant recruited for this study was a 49 year old male who suﬀered from a C5 sensory /C6 motor spinal cord injury ≈30 years prior to this testing. The injury was categorized as a B (incomplete) on the American Spinal Cord Injury Association Impairment Scale. In particular, the participant retained some movement in shoulder and elbow, partial movement of wrist (extension only), and minimal to no movement of ﬁngers. The participant was implanted with six NeuroPort electrode arrays (Blackrock Neurotech; Salt Lake City, UT) in the motor and somatosensory cortices of both brain hemispheres. Additional details can be found in McMullen et al. (2021) and Fifer et al. (2022). Brieﬂy, two 96 channel arrays (10 × 10 layout spanning 4 × 4mm) were placed in the dominant (left) primary motor cortex and two 32 channel arrays (within a 6 × 10 layout spanning 4 × 2.5mm) were placed in the somatosensory cortex. In the non-dominant (right) hemisphere, one 96 channel array and one 32 channel array were located in the primary motor and somatosensory cortices, respectively (Figure 1B). The arrays notionally covered neural regions representing both the left and right limbs as reported in previous studies (Thomas et al., 2020; Christie et al., 2021; McMullen et al., 2021; Osborn et al., 2021a,b; Fifer et al., 2022).

This study was conducted under an approved Food and Drug Administration (FDA) Investigational Device Exemption (G170010). This study was registered on ClinicalTrials.gov (NCT03161067) and was reviewed and approved by the Johns Hopkins Institutional Review Board (IRB). Surgical explantation of the investigational device occurred approximately a year after this testing.

Neural Decoding

Neural signals were recorded from the implanted microelectrode arrays using a wired connection from the implants to three 128 channel Neuroport Neural Signal Processors (Blackrock Neurotech). Before each experiment session began, voltage thresholds for each electrode were set to −3.25 times the rootmean-square (RMS) voltage of the neural signal during a resting state. Neural spikes from the implanted arrays were recorded at 30kHz and the ﬁring rate for each electrode was calculated using 30ms bins. Spiking activity in each channel, speciﬁcally the square-root of the ﬁring rate, was normalized at each time point using a streaming z-score calculation (using the channel-speciﬁc mean and standard deviation) over the preceding 60s (Downey et al., 2017; Colachis et al., 2018).

For this study, our team leveraged a gesture-based 2D control strategy, wherein each direction was mapped to a gesture: up (open hand), down (2-ﬁnger pinch), toward midline (wrist ﬂex), away from midline (wrist extend), and no movement (hand rest). This mapping was familiar to the participant prior to this study. This control strategy was chosen due to limited directional tuning of spiking signals, and resulting poor performance of classical continuous direction-based velocity control. The participant performed a target-reach training task at the beginning of the

|[Figure 2]<br><br>FIGURE 1 | System diagram for BMI-based shared control of bimanual robotic limbs. (A) Movements are decoded from neural signals through the brain-machine interface and mapped to two external robotic limbs while using a collaborative shared human-machine teaming control strategy to complete a self-feeding task requiring simultaneous bimanual manipulations. (B) NeuroPort electrode arrays (Blackrock Neurotech) implanted in the motor and somatosensory regions of the left and right hemispheres record neural activity. (C) Neural data is streamed from the cortical implants and processed before being decoded. Decoded gestures are passed to the shared control strategy for mapping onto robot degrees of freedom depending on the current state of the task. Autonomous portions of the task are performed by the robot while semi-autonomous steps are controlled in part by the participant using attempted gestures to modulate a subset of robotic limb end effector degrees of freedom using the current DOF mapping. The degrees of freedom controlled via BMI are based on a task library accessed by the robot.|
|---|

experiment where they attempted gesture-based control while watching two virtual Modular Prosthetic Limbs (vMPL) (Ravitz et al., 2013; Wester et al., 2020) move to targets located on vertical and horizontal axes. The target locations were displayed for 0.5–1s before the vMPLs began to move to the targets. vMPL movement initiation was signaled by an audio cue, which instructed the participant to start attempting the gestures corresponding to the movement direction. The participant was instructed to attempt to perform the gestures, i.e., without inhibiting movement of ﬁngers or wrist. The gestures were attempted and held continuously until the vMPL reached its target. The gesture-direction mapping was mirrored between the two hands, and the participant was presented with 16 repetitions of each unimanual and bimanual (parallel and anti-parallel directions) movement combination (256 total training trials). Speciﬁcally, there were 16 unimanual and bimanual gesture combinations that were trained: four unimanual movements (hand open, pinch, wrist extend/ﬂex) with the right arm and four with the left arm; two bimanual parallel movements in the horizontal directions (i.e., right wrist ﬂex with left wrist

extend and vice versa) and two bimanual anti-parallel horizontal movements (i.e., right wrist ﬂex with left wrist ﬂex and right wrist extend with left wrist extend); two bimanual parallel vertical movements (i.e., right open hand with left open hand and right pinch with left pinch) and two bimanual anti-parallel vertical movements (i.e., right open hand with left pinch and vice versa). Oﬄine decoding accuracy was determined using 10fold cross-validation. The normalized neural ﬁring rates from each hemisphere were segmented from the training data and used to train a linear discriminant analysis (LDA) classiﬁer for decoding intended gestures from the contralateral hand to enable simultaneous classiﬁcation of bimanual movements (Thomas et al., 2020). To generate the training samples for the neural decoder, the normalized neural signals were split into 240ms windows with a 90ms shift. The average activity was taken for each window and labeled with the corresponding attempted hand gesture to create a training sample.

Online performance of these gesture classiﬁers was tested using the same target-reach task. But rather than the vMPLs being controlled by the computer, their movement direction was

determined by the gestures predicted by the decoding model. Online decoding was achieved by binning the incoming neural signal and averaging the normalized ﬁring rates from each electrode across a 240ms buﬀer. A gesture prediction from the neural signal was made every 30ms and the output was transmitted using a custom software interface to send control commands to the robot control system controlling the MPL (Johannes et al., 2020).

Shared Control Strategy

In our shared control strategy, the participant and the bimanual manipulators are viewed as a human-robot team, and the goal is to enable the human to control a minimal set of key DOF to maximize task performance while minimizing human workload. It is a form of adjustable autonomy in which the robot nominally knows how to perform a task, and human input is used to guide and customize robot behavior (Handelman et al., 1990, 2022; National Academies of Sciences, Engineering, and Medicine, 2022).

For bimanual manipulation, the shared control system must maneuver the two MPL end eﬀectors (i.e., the anthropomorphic robot hands) to achieve desired task goals. A total of 12 DOFs3D position and 3D orientation (pose) of both end eﬀectorsneed to be controlled at all times by either the user or the system. Each MPL uses seven joints (three in the shoulder, one in the elbow and three in the wrist) to position and orient the end eﬀector, and we use inverse kinematics to compute commanded joint angles for a desired end eﬀector pose (Handelman et al., 2018).

In this study, the human was positioned between the robot arms and in front of a table with a plate of food (Figure 1A). The robot hands held utensils and the ﬁngers of each robot hand remained ﬁxed relative to the wrist. The shared control strategy was to dynamically partition the 12 controllable DOFs (position and orientation of each robot hand) into BMIcontrolled and system-controlled DOF (Figure 1C). Complex tasks were manually divided into task steps. During each task step up to four DOFs were controlled by the BMI (i.e., up to two DOF on each side), and the remaining DOF were controlled by the robot control system. The active mapping of participant twoDOF input (north-south or east-west) to end eﬀector six-DOF movement for each hand (left-right, forward-back, up-down, yaw left-right, pitch up-down, and roll left-right) was announced verbally by the robot during task execution. The overall goal was to let the robot do the majority of a task but allow the participant to take control of a subset of DOF to shape task performance to their liking. In the case of self-feeding, for example, given a plate with a variety of foods on it, we want the participant to be able to choose which food to eat, where to cut (if necessary), and the size of the piece to eat (Figure 2).

The robot end eﬀector DOFs available to the participant were those considered most useful for the active task step. This made the shared control system easy to use, robust, and safe in its behavior, operating within a constrained task-speciﬁc envelope of motion. Sometimes the participant could control only one DOF of one end eﬀector in one direction (“move right hand down”), sometimes two bidirectional DOFs of one end eﬀector (“move

right hand forward, back, left, right”), and sometimes three DOFs total, one associated with one eﬀector and two associated with the other (“move left hand down, move right hand back and right”).

In this type of collaborative control strategy, where the robot is performing the majority of a multi-step task (e.g., “cut and eat food”) but the BMI user controls a subset of DOF during certain task steps, the robot must be able to estimate when the BMI user is satisﬁed with their input (and current robot state) and is done with the active step so that the robot can move on to the next step. For a task step where the user is providing input, the robot waits for the user to provide initial BMI input (gestures), then waits for the user to stop providing input, then moves on to the next step.

Detection of this “intentional” user activity is complicated by the nature of the BMI-generated gestures signals. Occasionally a short-lived gesture “spike” occurs that does not necessarily imply intended sustained robot arm movement by the BMI user. In order to handle this situation, we compute a cmd_moving_raw signal as the sum of the absolute values of the incoming active DOF, where each degree of freedom has a gesture-based value of −1, 0, or 1. This cmd_moving_raw signal is passed through a second-order ﬁlter (damping ratio 0.8, settling time 0.5s) to provide cmd_moving_ﬁltered. If cmd_moving_ﬁltered is greater than or equal to cmd_moving_threshold value of 0.125 it is assumed that the BMI user is actively providing input, otherwise it is assumed the user is not providing input. This ﬁlter enables “noisy” gesture spikes to be ignored by the system while enabling sustained gestures to be interpreted as intentional activity. The robot control system monitors these values at a rate of 40Hz, the nominal robot control system update rate.

User gestures are mapped to robot end eﬀector velocity for the active DOF through a velocity scaling factor. This scaling factor needs to be tuned so that it is not too slow as to be tedious to control by the user but not so fast as to induce overshoot and oscillations. For each task step where user input is expected, the robot detects initial movement (cmd_moving_ﬁltered ≥ cmd_moving_threshold), then looks for a lack of input activity (cmd_moving_ﬁltered < cmd_moving_threshold for >1.1s (cmd_moving_wait_reset), at which point it considers the current step done. The robot also considers the current step done if the user BMI input switches from inactive to active at least 13 times (cmd_moving_count_max). Another feature of the system is to keep the robot end eﬀector within a bounded region (bounding box) relative to a task step reference point, such as where the robot positions the fork over the food, the knife over the food, and the food in front of the user’s mouth in the self-feeding task. In some task steps the step is considered done when the edge of the bounding box is reached, such as when moving the fork down to stab food, moving the knife down to cut food, and when moving food into the user’s mouth.

Self-Feeding Task

To demonstrate shared control of bimanual robotic limbs, a decadent dessert pastry was placed on a table in front of two

|[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>FIGURE 2 | Bimanual self-feeding task ﬂowchart. The collaborative shared control strategy enables the participant to control a minimum set of DOFs while still maximizing task performance.|
|---|

MPLs mounted on a stand. The participant was instructed to use neural control to guide the robotic limbs in order to cut a piece of the pastry and bring it to his mouth (Figure 1A). Consuming the pastry was optional, but the participant elected to do so given that it was delicious.

A fork and a knife were attached to the right and left MPLs, respectively. The participant controlled a subset of the position and orientation DOF of each MPL using the decoded neural signal commands and the self-feeding task was stepped through using various DOF modes to contribute to the overall feeding task as described above. Figure 2 presents the shared control self-feeding task ﬂowchart. Trials were considered successful if the participant was able to cut the pastry using bimanual neural control and complete the self-feeding portion of the task using the MPLs.

RESULTS Neural Decoding

Global oﬄine gesture decoding accuracy from the neural signals for the left and right hands was 63.5 and 67.6%, respectively (chance accuracy: 20%; see Figure 3). These oﬄine accuracies are similar to previously reported results by our team using similar methods during simultaneous bimanual movements (Thomas et al., 2020). During online testing with the target-reach task, the participant was successful in 17 out of 20 trials (85%), indicating usability of the neural decoder for controlling the external robotic limbs in the self-feeding task.

Bimanual Self-Feeding Task

Calibration and testing of the collaborative shared control strategy for self-feeding was performed in one session with

|rest open<br><br>pi<br><br>nch<br><br>wrist ex<br><br>tend<br><br>Predicted<br><br>|84%|5%|0%|2%|10%|
|---|---|---|---|---|
|12%|75%|4%|5%|4%|
|8%|4%|83%|1%|4%|
|20%|7%|2%|62%|9%|
|36%|8%|5%|18%|34%|
<br><br>rest<br><br>open<br><br>pinch<br><br>wrist extend<br><br>Actual<br><br>Left Hand<br><br>Gesture Decoding Accuracy<br><br>Right Hand<br><br>|82%|9%|1%|2%|5%|
|---|---|---|---|---|
|24%|44%|10%|19%|2%|
|15%|5%|77%|2%|0%|
|13%|11%|2%|69%|6%|
|34%|3%|2%|17%|45%|
<br><br>rest open pinch<br><br>w<br><br>ristex<br><br>tend<br><br>Predicted<br><br>rest<br><br>open<br><br>pinch<br><br>wrist extend<br><br>Actual<br><br>[Figure 6]<br><br>0%<br><br>20%<br><br>40%<br><br>60%<br><br>80%<br><br>100%<br><br>FIGURE 3 | Ofﬂine decoding performance for the left and right hands during simultaneous attempted gestures (including “rest”). Contralateral neural signals were<br><br>used to decode each hand (i.e., left motor and somatosensory cortex signals were used to decode right hand movements). On each hand, there were 48 instances for each of the movement classes (open, pinch, wrist ﬂex, wrist extend) and 64 for the “rest” condition. Of the movements, “pinch” gestures were decoded with the highest accuracy for both left and right hands, while “wrist extend” was notably more difﬁcult to decode (45 and 34% for left and right hands, respectively).|
|---|

Actual

Actual

the participant. Development of robot task behaviors and preliminary tuning of system parameters was done using simulation prior to the session.

In the current experimental setup, the robot had a priori knowledge of the approximate locations of the plate, of the food on the plate, and of the participant’s mouth. Robot motion segments involving the robot moving the tip of the fork and the blade of the knife to the food, and moving the piece of food to the participant’s mouth, were calibrated during testing using end eﬀector position and orientation reference points. As noted previously, when the participant was controlling an end eﬀector DOF, bounding box limits were placed on how far the end eﬀector could move from the default position (reference point). This kept the robot from wandering too far from a practical pose for the active task step, helping to minimize participant eﬀort, and kept the robot within a safe envelope relative to the participant, such as when placing food within the participant’s mouth. These bounding box limits for various task steps were also calibrated during testing.

Calibration of the end eﬀector velocity scaling factor was critical. Improper calibration would cause the robot arm to either move frustratingly slowly, requiring a great deal of participant eﬀort (many gestures to move the robot arm a small distance), or too quickly, causing the fork or knife to overshoot the desired location. Calibration of user activity monitoring parameters cmd_moving_threshold, cmd_moving_wait_reset, and cmd_moving_count_max was also important to properly interpret when intended user activity had begun and when it had ended. Improper setting of these parameters caused task steps to end sooner than desired, before the fork or knife had been positioned as desired.

Once the shared control system was tuned, the participant could perform the self-feeding task, cutting oﬀ a reasonably

sized piece of food using simultaneous bimanual commands and bringing it to his mouth without dropping it (Figure 4, Supplementary Movie 1). The test session included 37 trials, most of which involved calibration of the aforementioned parameters due to inconsistencies between the robot simulation and physical hardware. Ultimately, seven successful trials were demonstrated where the participant was able to cut oﬀ a reasonably sized piece of food and bring it to his face without dropping it using simultaneous bimanual commands (Supplementary Movie 1). While the size of the cut food was subjectively determined by the participant’s preference, we note that in one of those seven trials the piece of food cut was too large to be reasonably consumed in one bite and in another one of those seven trials the cut food was much smaller. In seven partially successful trials the participant was able to cut the food but the food fell oﬀ the fork. In a total of 26 out of the 37 trials the participant performed bimanual control by employing the knife and fork in the self-feeding task, and the remaining 11 trials were halted and bimanual control was not achieved because the fork did not make contact with the food.

## DISCUSSION

The collaborative approach to shared control presented here is intended as an exploratory proof of concept into how BMI signals might be blended with robot autonomy to enable a user to perform complex bimanual tasks that can be customized using limited BMI signals, such as which food on the plate to eat and how big a piece to cut. The ultimate goal is adjustable autonomy that leverages whatever BMI signals are available to their maximum eﬀectiveness, enabling the human to control the few DOFs that most directly impact the qualitative performance of a task while the robot takes care of the rest. An important

|[Figure 7]<br><br>FIGURE 4 | Select screenshots of self-feeding task performance. The robot holds a fork in right hand and a knife in left hand. (A) Step 1: Participant initiates task by moving robot right hand forward. (B) Step 3: Participant repositions fork horizontally to align with desired piece of food. (C) Step 6: Participant repositions knife horizontally to select cut point. (D) Step 7: Participant moves knife down and fork back and right to cut food. (E) Step 10: Robot moves food to default position in front of participant’s mouth. (F) Step 12: Participant places food in mouth.|
|---|

objective is to accommodate a wide range of BMI signal quantity and quality, both high-ﬁdelity continuous/proportional signals and event-based/bang-bang signals such as the BMIbased gestures reported here, as well as BMI signals that might degrade over time.

As opposed to low-autonomy, task-independent approaches to BMI-driven manipulation that provide generalized capabilities for low-level behaviors such as grasping, reaching and transporting objects (Katyal et al., 2013; McMullen et al., 2014, 2020; Downey et al., 2016), this work focuses on the higher end of the autonomy spectrum, where the robot is assumed to be capable of nominally accomplishing complex bimanual tasks requiring sequential and simultaneous multi-step actions (including ADLs such as eating and getting dressed) and we want to enable BMI-based task customization. As robotics technology continues to advance, we want to leverage these new capabilities while maintaining human control and customization via BMI. The limitation of our current approach to collaborative shared control is that it is task dependent and assumes signiﬁcant competency on the part of the robot, but the

strength is that it enables BMI users to personalize task behavior with minimal eﬀort.

In the current study, the participant was able to use a BMIbased shared controller to successfully maneuver two MPLs to perform a bimanual ADL (Figure 4, Supplementary Movie 1). In our shared control strategy, the BMI commands provided by the participant were augmented by the robot controller to enable self-feeding (Supplementary Movie 1). The robot system took inputs from the neural decoder with global oﬄine decoding accuracy of the neural signal at 67.6% (Figure 3), and online target-reach performance of 85%. These are relatively low decoding accuracies in absolute terms, but proved suﬃcient to meaningfully customize task performance. While higher oﬄine decoding accuracies could possibly contribute to improved performance during the bimanual self-feeding task, it is important to highlight the value of online performance metrics, such as task completion, when evaluating BMI systems for improving function. These demonstrations highlight the value of using neural decoders within an intelligent system, rather than requiring the user to directly control all movements.

While the participant used signals from both hemispheres of the brain to perform the bimanual task, with each robotic arm being controlled by the contralateral hemisphere, recent research suggests the representations of both ipsilateral and contralateral arm movements within the same hemisphere (Ames and Churchland, 2019; Downey et al., 2020). It is possible to control bimanual limbs using neural signals from the motor cortex in one hemisphere, although control of the ipsilateral limb is not always as proﬁcient as the contralateral limb (Downey et al., 2020). Importantly though, the shared control approach presented here could be leveraged for BMI systems that rely on motor recordings from the same hemisphere.

Despite the unequal number of electrodes contributing to gesture decoding of each hand, we achieved comparable accuracies across the two hands. However, the SUA and MUA yield from the arrays in the motor cortex was comparatively lower than from the arrays in the sensory cortex, as described in our previous publication (Thomas et al., 2020). A higher yield in the motor arrays may have resulted in a higher classiﬁcation accuracy. In addition, when extracting features to train the decoder, we used multiple training samples corresponding to the diﬀerent phases of the gesture attempt, including movement initiation, sustained movement attempt, and movement release. This approach allowed us to maximize the number of trials used to train the decoder and to ensure that the decoder does not overﬁt to any single phase of gesture execution. However, this also resulted in more variance among the training samples. Nevertheless, the classiﬁers were still able to distinguish between several of the gestures with accuracies ranging between 70 and 85% accuracy.

In our approach, the decoder was trained on attempted execution of gestures rather than imagined execution of gestures, which may have resulted in small muscle activations. Given the participant’s injury level, imagined gestures would have required active inhibition to avoid any physical movements. BMI users with a complete spinal cord injury would not need to inhibit movement while attempting movement control. As such, training on attempted gestures ensured that the decoder did not learn or depend on neural activity corresponding to inhibitory movement control, which provided a better sense of the performance that can be expected from our motor control approach.

We believe that the shared control technique reported here could be applied to a wide range of ADLs. However, a number of challenges remain. In this study, the positions of target objects were known to the system. This design choice was made to simplify systems integration and focus on shared BMI control for this initial demonstration. Robot perception algorithms are becoming increasingly performant and available (Billard and Kragic, 2019). Future iterations of this system would ideally dynamically estimate the position and orientation of target objects in the environment (e.g., utensils, food, the participant’s mouth) via cameras co-registered to the robot’s coordinate system to provide obstacle avoidance and visual servoing. Additionally, this system utilized multiple shared control parameters (e.g., motion start/end poses, number of DOFs controlled by the user, BMI input activity ﬁltering), which were manually tuned in this study but would ideally be

automatically calibrated to increase robustness and scalability to other tasks. Depending on user preference, the robot’s verbal interface announcing available DOFs could also be augmented or replaced with a small display. Finally, the robot needs to have knowledge of how to perform a range of tasks and an ability to perform them safely and reliably under the proper context.

This work demonstrates important progress in neurorobotic systems for improving user independence and functionality. In particular, this shared control approach enables user input over many of the steps in the self-feeding task while simultaneously reducing the required DOF to eﬀective complete the task (Figure 2). Compared to other semi-autonomous control approaches for reducing DOF control in assistive technologies (Katyal et al., 2013; McMullen et al., 2014, 2020; Downey et al., 2016), the shared control approach with the human-machine team oﬀers unique advantages in that it provides the user with additional control over individual DOFs and allows for modulation (i.e., relative positioning along varies DOF) during the task. The reduced DOF in a complex, bimanual task is a critical component for allowing a broad range of BMI users, for whom high DOF control signals may not be possible, to beneﬁt from this approach. In essence, the shared control strategy provides better scalability for a variety of BMI users.

Although preliminary, these results mark a critical step in demonstrating the use of an intelligence-assisted BMI for completing necessary, yet sometimes complex, activities of daily living such as cutting and eating food by providing users with shared control of high-DOF bimanual robotic systems.

## DATA AVAILABILITY STATEMENT

Data supporting the conclusions of this article will be made available upon request by the authors, without undue reservation.

## ETHICS STATEMENT

The studies involving human participants were reviewed and approved by Johns Hopkins Institutional Review Board. The patients/participants provided their written informed consent to participate in this study. Written informed consent was obtained from the individual(s) for the publication of any potentially identiﬁable images or data included in this article.

## AUTHOR CONTRIBUTIONS

DH, AB, MF, and FT: designed the study. DH, AB, TT, MT, RN, and FT: performed the experiments and analysis. MA, DM, GC, PC, MF, and FT: supervised the study. DH, LO, FT, TT, and BW: prepared ﬁgures and the manuscript. All authors contributed to editing and revising the manuscript.

## FUNDING

This work was developed with internal research funding from the Johns Hopkins University Applied Physics Laboratory and National Institutes of Health grant 1R01NS088606. Previous

funding from the Defense Advanced Research Projects Agency (DARPA) Revolutionizing Prosthetics program (N66001-10-C4056) supported implantation surgery, development of the MPLs and of the neural decoding architecture.

## ACKNOWLEDGMENTS

The authors thank the participant for their time and contribution to this work. The Modular Prosthetic Limbs were developed

with support from DARPA through the Revolutionizing Prosthetics program.

## SUPPLEMENTARY MATERIAL

The Supplementary Material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fnbot. 2022.918001/full#supplementary-material

## REFERENCES

Aﬂalo, T., Kellis, S., Klaes, C., Lee, B., Shi, Y., Pejsa, K., et al. (2015). Decoding motor imagery from the posterior parietal cortex of a tetraplegic human. Science 348, 906–910. doi: 10.1126/science.aaa5417

Ajiboye, A. B., Willett, F. R., Young, D. R., Memberg, W. D., Murphy, B. A., Miller, J. P., et al. (2017). Restoration of reaching and grasping movements through brain-controlled muscle stimulation in a person with tetraplegia: a proof-of-concept demonstration. Lancet 389, 1821–1830. doi: 10.1016/S0140-6736(17)30601-3

Ames, K. C., and Churchland, M. M. (2019). Motor cortex signals for each arm are mixed across hemispheres and neurons yet partitioned within the population response. eLife 8, e46159. doi: 10.7554/eLife.46159

Armenta Salas, M., Bashford, L., Kellis, S., Jafari, M., Jo, H., Kramer, D., et al. (2018). Proprioceptive and cutaneous sensations in humans elicited by intracortical microstimulation. eLife 7, e32904. doi: 10.7554/eLife.32904

Billard, A., and Kragic, D. (2019). Trends and challenges in robot manipulation. Science 364, eaat8414. doi: 10.1126/science.aat8414

Christie, B., Osborn, L. E., McMullen, D. P., Pawar, A. S., Bensmaia, S. J., Celnik, P. A., et al. (2021). Perceived timing of cutaneous vibration and intracortical microstimulation of human somatosensory cortex. medRxiv. doi: 10.1101/2021.12.28.21268447

Colachis, S. C., Bockbrader, M. A., Zhang, M., Friedenberg, D. A., Annetta, N. V., Schwemmer, M. A., et al. (2018). Dexterous control of seven functional hand movements using cortically-controlled transcutaneous muscle stimulation in a person with tetraplegia. Front. Neurosci. 12:208. doi: 10.3389/fnins.2018.00208

Collinger, J. L., Wodlinger, B., Downey, J. E., Wang, W., Tyler-Kabara, E. C., Weber, D. J., et al. (2013). High-performance neuroprosthetic control by an individual with tetraplegia. Lancet 381, 557–564. doi: 10.1016/S0140-6736(12)61816-9

Downey, J. E., Brane, L., Gaunt, R. A., Tyler-Kabara, E. C., Boninger, M. L., and Collinger, J. L. (2017). Motor cortical activity changes during neuroprosthetic-controlled object interaction. Sci. Rep. 7, 16947. doi: 10.1038/s41598-017-17222-3

Downey, J. E., Quick, K. M., Schwed, N., Weiss, J. M., Wittenberg, G. F., Boninger, M. L., et al. (2020). The motor cortex has independent representations for ipsilateral and contralateral arm movements but correlated representations for grasping. Cereb. Cortex 30, 5400–5409. doi: 10.1093/cercor/bhaa120

Downey, J. E., Weiss, J. M., Muelling, K., Venkatraman, A., Valois, J.-S., Hebert, M., et al. (2016). Blending of brain-machine interface and vision-guided autonomous robotics improves neuroprosthetic arm performance during grasping. J. NeuroEng. Rehabil. 13, 28. doi: 10.1186/s12984-016-0134-9

Fifer, M. S., McMullen, D. P., Osborn, L. E., Thomas, T. M., Christie, B., Nickl, R. W., et al. (2022). Intracortical somatosensory stimulation to elicit ﬁngertip sensations in an individual with spinal cord injury. Neurology 98, e679–e687. doi: 10.1212/WNL.0000000000013173

Flesher, S. N., Downey, J. E., Weiss, J. M., Hughes, C. L., Herrera, A. J., Tyler-Kabara, E. C., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. Science 372, 831–836. doi: 10.1126/science.abd0380

Handelman, D. A., Lane, S. H., and Gelfand, J. J. (1990). Integrating neural networks and knowledge-based systems for intelligent robotic control. IEEE Control Syst. Mag. 10, 77–87. doi: 10.1109/37.55128

Handelman, D. A., Rivera, C. G., St. Amant, R., Holmes, E. A., Badger, A. R., and Yeh, B. R. (2022). “Adaptive human-robot teaming through integrated symbolic and subsymbolic artiﬁcial intelligence: preliminary results,” in Proceedings of the Society of Photo-Optical Instrumentation Engineers (SPIE), 12113. doi: 10.1117/12.2618686

Handelman, D. A., Wormley, J. M., Dohopolski, C. J., Johannes, M. S., Rimando, R., Young, R. F., et al. (2018). “Telerobotic control of dexterous dual-arm robots for D&D operations,” in Proceedings of the 2018 Waste Management Conference (WM2018), 18622.

Iﬀt, P. J., Shokur, S., Li, Z., Lebedev, M. A., and Nicolelis, M. A. L. (2013). A brain-machine interface enables bimanual arm movements in monkeys. Sci. Transl. Med. 5, 210ra154. doi: 10.1126/scitranslmed.300 6159

Johannes, M. S., Faulring, E. L., Katyal, K. D., Para, M. P., Helder, J. B., Makhlin, A., et al. (2020). “The modular prosthetic limb,” in Wearable Robotics, eds J. Rosen, and P. W. Ferguson (Cambridge, MA: Academic Press), 393–444. doi: 10.1016/B978-0-12-814659-0.00021-7

Katyal, K. D., Johannes, M. S., McGee, T. G., Harris, A. J., Armiger, R. S., Firpi, A. H., et al. (2013). “HARMONIE: a multimodal control framework for human assistive robotics,” in 2013 6th International IEEE/EMBS Conference on Neural Engineering (NER), 1274–1278.

Kopp, B., Kunkel, A., Flor, H., Platz, T., Rose, U., Mauritz, K.-H., et al. (1997). The arm motor ability test: reliability, validity, and sensitivity to change of an instrument for assessing disabilities in activities of daily living. Arch. Phys. Med. Rehabil. 78, 615–620. doi: 10.1016/S0003-9993(97)90427-5

McMullen, D. P., Fifer, M. S., Katyal, K. D., Armiger, R., Hotson, G., Beaty, J. D., et al. (2020). Design and preliminary evaluation of an augmented reality interface control system for a robotic arm. Johns Hopkins APL Tech. Dig. 35, 220–230.

McMullen, D. P., Hotson, G., Katyal, K. D., Wester, B. A., Fifer, M. S., McGee, T. G., et al. (2014). Demonstration of a semi-autonomous hybrid brain–machine interface using human intracranial EEG, eye tracking, and computer vision to control a robotic upper limb prosthetic. IEEE Trans. Neural Syst. Rehabil. Eng. 22, 784–796. doi: 10.1109/TNSRE. 2013.2294685

McMullen, D. P., Thomas, T. M., Fifer, M. S., Candrea, D. N., Tenore, F. V., Nickl, R. W., et al. (2021). Novel intraoperative online functional mapping of somatosensory ﬁnger representations for targeted stimulating electrode placement: technical note. J. Neurosurg. 35, 1493–1500. doi: 10.3171/ 2020.9.JNS202675

Moses, D. A., Metzger, S. L., Liu, J. R., Anumanchipalli, G. K., Makin, J. G., Sun, P. F., et al. (2021). Neuroprosthesis for decoding speech in a paralyzed person with anarthria. N. Engl. J. Med. 385, 217–227. doi: 10.1056/ NEJMoa2027540

National Academies of Sciences, Engineering, and Medicine (2022). Human-AI Teaming: State-of-the-Art and Research Needs. Washington, DC: The National Academy Press. doi: 10.17226/26355

Osborn, L. E., Christie, B. P., McMullen, D. P., Nickl, R. W., Thompson, M. C., Pawar, A. S., et al. (2021a). “Intracortical microstimulation of somatosensory cortex enables object identiﬁcation through perceived sensations,” in Presented at the 2021 43rd Annual International Conference of the IEEE Engineering in Medicine Biology Society (EMBC), 6259–6262. doi: 10.1109/EMBC46164.2021.9630450

Osborn, L. E., McMullen, D. P., Christie, B. P., Kudela, P., Thomas, T. M., Thompson, M. C., et al. (2021b). “Intracortical microstimulation of somatosensory cortex generates evoked responses in motor cortex,” in Presented at the 2021 10th International IEEE/EMBS Conference on Neural Engineering (NER), 53–56. doi: 10.1109/NER49283.2021. 9441123

Ravitz, A. D., McLoughlin, M. P., Beaty, J. D., Tenore, F. V., Johannes, M. S., Swetz, S. A., et al. (2013). Revolutionizing prosthetics - Phase 3. Johns Hopkins APL Tech. Dig. 31, 366–376.

Tang, J., and Zhou, Z. (2017). “A shared-control based BCI system: for a robotic arm control,” in Presented at the 2017 First International Conference on Electronics Instrumentation Information Systems (EIIS), 1–5. doi: 10.1109/EIIS.2017.8298767

Thomas, T. M., Nickl, R. W., Thompson, M. C., Candrea, D. N., Fifer, M. S., McMullen, D. P., et al. (2020). Simultaneous classiﬁcation of bilateral hand gestures using bilateral microelectrode recordings in a tetraplegic patient. medRxiv. doi: 10.1101/2020.06.02.20116913

Wester, B. A., Badger, A. R., Fifer, M. S., Buckley, E. D., Portwood, D. M., Beaty, J. D., et al. (2020). CONVEY: connecting STEM outreach now using VIE education for youth. Johns Hopkins APL Tech. Dig. 35, 259–266.

Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M., and Shenoy, K. V. (2021). High-performance brain-to-text communication via handwriting. Nature 593, 249–254. doi: 10.1038/s41586-02103506-2

Wodlinger, B., Downey, J. E., Tyler-Kabara, E. C., Schwartz, A. B., Boninger, M. L., and Collinger, J. L. (2015). Ten-dimensional anthropomorphic

arm control in a human brain–machine interface: diﬃculties, solutions, and limitations. J. Neural Eng. 12, 016011. doi: 10.1088/1741-2560/ 12/1/016011

Conﬂict of Interest: DH is inventor on intellectual property pertaining to robotic manipulation.

The remaining authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Publisher’s Note: All claims expressed in this article are solely those of the authors and do not necessarily represent those of their aﬃliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2022 Handelman, Osborn, Thomas, Badger, Thompson, Nickl, Anaya, Wormley, Cantarero, McMullen, Crone, Wester, Celnik, Fifer and Tenore. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

