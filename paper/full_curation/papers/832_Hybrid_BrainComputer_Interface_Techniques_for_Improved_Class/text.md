July 2017  |  Volume 11  |  Article 35
1
Review
published: 24 July 2017
doi: 10.3389/fnbot.2017.00035
Frontiers in Neurorobotics  |  www.frontiersin.org
Edited by: 
Feihu Zhang, 
Northwestern Polytechnical 
University, China
Reviewed by: 
Yu Zhang, 
East China University of Science 
and Technology, China 
Yantao Li, 
Southwest University, China
*Correspondence:
Keum-Shik Hong 
kshong@pusan.ac.kr
Received: 24 April 2017
Accepted: 03 July 2017
Published: 24 July 2017
Citation: 
Hong K-S and Khan MJ (2017) 
Hybrid Brain–Computer Interface 
Techniques for Improved 
Classification Accuracy 
and Increased Number of 
Commands: A Review. 
Front. Neurorobot. 11:35. 
doi: 10.3389/fnbot.2017.00035
Hybrid Brain–Computer interface 
Techniques for improved 
Classification Accuracy and 
increased Number of Commands:  
A Review
Keum-Shik Hong1,2* and Muhammad Jawad Khan1
1 School of Mechanical Engineering, Pusan National University, Busan, South Korea, 2 Department of Cogno-Mechatronics 
Engineering, Pusan National University, Busan, South Korea
In this article, non-invasive hybrid brain–computer interface (hBCI) technologies 
for improving classification accuracy and increasing the number of commands are 
reviewed. Hybridization combining more than two modalities is a new trend in brain 
imaging and prosthesis control. Electroencephalography (EEG), due to its easy use and 
fast temporal resolution, is most widely utilized in combination with other brain/non-brain 
signal acquisition modalities, for instance, functional near infrared spectroscopy (fNIRS), 
electromyography (EMG), electrooculography (EOG), and eye tracker. Three main 
purposes of hybridization are to increase the number of control commands, improve 
classification accuracy and reduce the signal detection time. Currently, such combina-
tions of EEG + fNIRS and EEG + EOG are most commonly employed. Four principal 
components (i.e., hardware, paradigm, classifiers, and features) relevant to accuracy 
improvement are discussed. In the case of brain signals, motor imagination/movement 
tasks are combined with cognitive tasks to increase active brain–computer interface 
(BCI) accuracy. Active and reactive tasks sometimes are combined: motor imagination 
with steady-state evoked visual potentials (SSVEP) and motor imagination with P300. In 
the case of reactive tasks, SSVEP is most widely combined with P300 to increase the 
number of commands. Passive BCIs, however, are rare. After discussing the hardware 
and strategies involved in the development of hBCI, the second part examines the 
approaches used to increase the number of control commands and to enhance classifi-
cation accuracy. The future prospects and the extension of hBCI in real-time applications 
for daily life scenarios are provided.
Keywords: hybrid brain–computer interface, functional near infrared spectroscopy, electroencephalography, 
electrooculography, electromyography, classification accuracy
INTRODUCTION
Electroencephalography (EEG) and functional near infrared spectroscopy (fNIRS) endow brain–
computer interfaces (BCIs) with their essential and indispensable attributes of non-invasiveness, low 
cost, and portability. EEG- and fNIRS-based BCIs have enabled paralyzed patients to communicate 
and control external devices with their own brain functions. Unfortunately, classification accuracy 

2
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
in these modalities diminishes as the number of BCI commands 
increases. As a mean of overcoming the problem of the reduction 
of classification accuracy upon an increase in the number of con-
trol commands, the concept of hybrid brain–computer interface 
(hBCI) was introduced (Allison et al., 2010; Muller-Putz et al., 
2015; Banville and Falk, 2016).
The hBCI pursues the following three main objectives: 
(i) enhanced BCI classification accuracy, (ii) increased number 
of brain commands for control application, and (iii) shortened 
brain-command detection time. These benefits provide hBCI a 
clear advantage over any single brain signal acquisition modality. 
In this article, hBCI is meant to combine either (i) more than 
two modalities (of which at least one is a brain signal acquisi-
tion device) or (ii) more than two brain activities with a single 
modality, for example, the combination of P300 and steady-state 
visual evoked potential (SSVEP) with EEG (Allison et al., 2010; 
Pfurtscheller et  al., 2010; Kreilinger et  al., 2012; Muller-Putz 
et al., 2015).
First, classification accuracy can be improved by combin-
ing multiple signal features from different modalities/devices 
for the same brain activity. For example, EEG and fNIRS have 
been combined for the detection of finger tapping (Fazli et al., 
2012) and hand/arm movement (Buccino et al., 2016). In these 
specific cases, the feature of EEG (i.e., signal band power) was 
combined with oxy- and deoxy hemoglobin (HbO and HbR) 
features of fNIRS to increase the accuracy of the system. Second, 
classification accuracy can be improved by utilizing one device’s 
signal in the artifact removal in another device’s brain signal. For 
instance, the peak value of electrooculography (EOG) caused by 
an eye blink (i.e., a motion artifact) can be subtracted from EEG’s 
data, in which the eye blink (or muscular movement) induces 
a false-positive value (McFarland and Wolpaw, 2011; Daly et al., 
2015). The most common artifact removal means from brain 
signals are EOG (Bashashati et al., 2007; Jiang et al., 2014) and 
electromyography (EMG) (Fatourechi et al., 2007).
For proper operation of a BCI system, a certain number 
of control commands are required (Lafleur et al., 2013; Ramli 
et al., 2015). However, an increase in the number of commands 
in a BCI system will naturally diminish the classification accu-
racy (Vuckovic and Sepulveda, 2012; Naseer and Hong, 2015a). 
Hence, hBCI should have an advantage over a single modal-
ity in increasing the number of control commands without 
negatively impacting the accuracy. This is achieved by decoding 
multiple activities from different brain regions using different 
modalities. For instance, mental arithmetic (MA) tasks using 
fNIRS and motor-related tasks using EEG have been combined 
into an hBCI paradigm resulting in an improved classification 
accuracy (Khan et al., 2014). Researchers also tried to look for 
multiple brain regions to increase the number of commands. 
For example, SSVEPs were combined with event-related poten-
tials (ERPs) to create a hybrid paradigm for EEG. A typical 
example is the combination of SSVEP with P300 signals for 
hBCI (Panicker et  al., 2011; Li et  al., 2013; Xu et  al., 2013). 
Motor imagery (MI) also has been combined with SSVEP (Lim 
et al., 2015; Yu et al., 2015).
The detected brain signals can be categorized into three 
types (i.e., active, reactive, and passive) according to whether 
they were made intentionally, or reactively upon external 
stimulation, or unintentionally (Zander and Kothe, 2011). 
In the case of active BCI, an intentional brain task is used to 
generate the brain activity, for example, finger tapping, MA, 
MI, mental counting, and music imagery. In these tasks, a brain 
activity is generated objectively by the person without any 
external stimuli and hBCI can be made using the brain signals 
in association with the performed mental tasks (Power et al., 
2010). In the case of reactive BCI, external stimuli are provided 
to cause a brain activity. In this paradigm, the stimuli can be 
given in various forms, for instance, audio (Santosa et al., 2014; 
Hong and Santosa, 2016), video (Li et al., 2013; Zhang et al., 
2013, 2014), interrogative (Hu et al., 2012; Bhutta et al., 2015), 
and pain (Hong and Nguyen, 2014). The hBCI combining 
SSVEP and P300 in EEG is considered reactive. In the case of 
passive BCI, an arbitrary brain signal generated by the subject 
with no intention—for instance, a signal related to drowsiness, 
vigilance, and fatigue—can be used (Khan and Hong, 2015). 
With regard to drowsiness, EEG and EOG are simultaneously 
checked to create an hBCI paradigm for accident avoidance 
(Picot et al., 2012).
Herein, we present a review of the various hBCI technologies. 
The schemes of non-invasive methodology in enhancing the 
BCI accuracy are discussed first. Note, however, that the studies 
combining only features and algorithms to decode activities for 
a single modality are excluded. Also, the hybrid systems that are 
not specifically used for BCI are excluded.
Figure 1 breakdowns the contents of the entire paper. The 
first part of this article introduces the concept of hybrid system, 
which utilizes a combination of different hardware to enhance 
BCI accuracy and to increase the number commands. Section 
“Hardware Combination” describes different combinations 
of hardware appeared in the literature. Section “Combination 
of Brain Signals” evaluates the combination of brain signals 
decoded by a single brain signal acquisition modality. Section 
“Advantages of hBCI” discusses the applications of hBCI systems 
for healthy people as well as patients. Section “Applications” 
explains the advantages of hybrid systems over single-modality 
versions. This section also provides detailed tables on hBCIs 
in terms of active, reactive, and passive tasks. The last part of 
this article discusses the future prospects for, and the research 
directions of, hybrid systems in control and rehabilitation 
applications.
Abbreviations: BCI, brain–computer interface; CCA, canonical correlation analy-
sis; CP, cerebral palsy; EEG, electroencephalography; EOG, electrooculography; 
EMG, electromyography; ERD, event-related desynchronization; ERP, event-
related potentials; FDA, Fisher discriminant analysis; FLDA, Fisher LDA; FES, 
functional electrical stimulation; fMRI, functional magnetic resonance imaging; 
fNIRS, functional near infrared spectroscopy; GA, genetic algorithm; GUI, graphi-
cal user interface; hBCI, hybrid brain–computer interface; HbO, oxyhemoglobin; 
HbR, deoxyhemoglobin; HMM, Hidden Markov model; ICA, independent 
component analysis; LDA, linear discriminant analysis; LIS, locked-in syndrome; 
MA, mental arithmetic; MCS, minimally conscious state; MI, motor imagery; 
PSO, particle swarm optimization; SCI, spinal cord injury; SM, signal mean; SMR, 
sensory motor rhythm; SS, signal slope; SSSEP, steady-state somatosensory evoked 
potentials; SSVEP, steady-state evoked visual potentials; SVM, support vector 
machine; VS, vegetative state; SW-LDA, step-wise LDA; tDCS, transcranial direct 
current stimulation; rTMS, repetitive transcranial magnetic stimulation.

Figure 1 | Breakdowns of the paper.
3
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
HYBRID CONCEPT
Pfurtscheller et  al. (2010) explained that an hBCI system is 
similar to a simple BCI but that it needs additionally to fulfill the 
following four criteria: (i) the activity should be directly acquired 
from the brain; (ii) at least one of multiple brain signal acquisition 
modalities should be employed in acquiring such activity, which 
can be in electrical potential, magnetic field, or hemodynamic 
change form; (iii) the signals must be processed in real time/
online to establish communication between the brain and a 
computer for generation of control commands; and (iv) feedback 
describing the outcomes of the brain activity for communication 
and control must be provided.
Recent hBCIs based on these criteria have focused on improv-
ing the accuracy of activity detection and increasing the number 
of control commands to achieve better communication and 
control for healthy subjects as well as patients. This is especially 
true considering the fact that an hBCI consists of at least two 
modalities (one of which is a brain-based signal) working in 
concert with each other to produce better BCI functionality.
Six aspects (hardware, signal processing, brain activity, feature 
extraction, classification, and feedback) need to be considered in 
developing an hBCI: (i) the hardware should consist of at least one 
brain signal acquisition modality; (ii) the hybrid system should 
detect and process different physiological signals simultaneously; 
(iii) the paradigm should be able to acquire multiple brain activi-
ties simultaneously using multiple modalities; (iv) a number of 
features for classification should be acquired in real time/online 
for both accuracy enhancement and additional control-command 
generation; (v) the classified output should have a potential for 
interfacing with external devices (e.g., wheelchairs and robots); 
and (vi) it should also provide feedback to the user for rehabilita-
tion and control purposes (Nicolas-Alonso and Gomez-Gil, 2012; 
Ramadan and Vasilakos, 2017).
Figure 2 provides an example of an hBCI scheme. It indicates 
the following two things: (i) multiple activities are required for 
hBCI and (ii) a combination of brain and non-brain signal acqui-
sition modalities is overviewed. After detection, the activities are 
processed simultaneously for feature extraction and classifica-
tion; then, the classified results are used as feedback for the user’s 
rehabilitation and control applications.
HARDWARE COMBINATION
Hybrid brain–computer interface hardware can be configured 
in the following two ways: (i) combination of a brain signal 
acquisition modality with a non-brain signal acquisition modal-
ity (Fatourechi et al., 2007; Li et al., 2015; Yang et al., 2015) and 
(ii) combination of a brain signal acquisition modality with 
another brain signal acquisition modality (Kaiser et  al., 2014; 
Putze et  al., 2014). Brain and non-brain signal acquisition 
modalities are combined either to remove motion artifacts or to 
increase the number of commands in a BCI system. Two brain 
signal acquisition modalities are combined and positioned over 
the same brain region in order to enhance the classification 
accuracy, or, they are positioned in different regions to increase 
the number of control commands. In the case of portable devices, 
the following signals are used.
Neuronal Signals
These are measured as a difference in voltage between two dif-
ferent cerebral locations over time. The signal is recorded by 
EEG electrodes positioned on the scalp. The recorded potential 
difference is reflected as the postsynaptic potential in the cell 
membranes of cortical neurons (Olejniczak, 2006; Nguyen and 
Hong, 2013). These signals are most effective for BCI, as they are 
detected immediately (e.g., P300 signals are detected 300 ms after 
stimuli are given). These signals also contribute in the detection 
of brain drowsiness state (Qian et al., 2016, 2017).
Hemodynamic Signals
The hemodynamic response is a process in which the blood 
releases glucose to active neurons at a greater rate than inactive 
ones. The glucose with oxygen delivered through the blood stream 
results in a surplus of HbO in the veins of the active area as well as 
a distinguishable change of the ratio of local HbO to HbR. These 
changes are detected by functional magnetic resonance imaging 

Table 1 | Combinations of devices.
Modality combination
Sensor placement
Signal combination
Possible outcome
Electroencephalography 
(EEG) + electrooculography (EOG)
Brain and eyes
Electrophysiological + eye movement
Increase in control commands/increase in 
accuracy
EEG + electromyography (EMG)
Brain and muscles
Electrophysiological + electromyography
Increase in accuracy
EEG + functional near infrared spectroscopy 
(fNIRS)
Brain
Electrophysiological + hemodynamic
Increase in classification accuracy/increase in 
control commands
Figure 2 | Purposes of hybrid brain–computer interface: (i) increase the number of control commands by combining electroencephalography (EEG) with functional 
near infrared spectroscopy (fNIRS) [further electrooculography (EOG)] and (ii) improve the classification accuracy by removing motion artifacts.
4
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
(fMRI) and fNIRS (Boas et al., 1994, 2001, 2014; Huppert et al., 
2009, 2013; Nicolas-Alonso and Gomez-Gil, 2012). These signals 
have an inherent delay in hemodynamic response generation. 
However, the most recent discovery on initial dips makes the 
HbO signals a viable candidate for BCI (Hong and Naseer, 2016; 
Zafar and Hong, 2017).
Eye Blink/Eye Movement Signals
The eye can be modeled as a dipole, with its positive pole at the 
cornea and its negative pole at the retina. Assuming a stable 
corneo-retinal potential difference, the eye is the origin of a steady 
electric potential field. The electrical signals generated from this 
field are measured by EOG (Bulling et  al., 2011). Sometimes 
an eye tracker also is used for the detection of eye movements. 
Mostly, these signals are used for the investigation of vigilance 
and drowsiness activities.
EMG Signals
These signals are an indication of muscles’ electrical activity, 
which arises whenever there exists a voluntary or involuntary 
contraction (Chowdhury et al., 2013; Patil and Patil, 2014; Xie 
et  al., 2014). These signals are recorded by EMG electrodes, 
which are most widely used in neuro-prostheses (Ravindra and 
Castellini, 2014; Chadwell et al., 2016; Chen et al., 2016). Table 1 
summarizes possible combinations that can be used in the devel-
opment of hBCI hardware.
EEG + EOG
EOG-based BCIs are useful for people who have control over 
their eye movements, as by this means, multiple commands can 
simultaneously be generated. Combinations of eye movement 
signals (blink, wink, frown, etc.) with neuronal signals usually 
are utilized for hybrid EEG–EOG-based BCIs (Ma et al., 2015). 
In this section, we also include hybrid studies that have used 
eye-tracking with EEG to develop hybrid systems for BCI. We 
discuss EOG and eye tracker-based studies together, as both use 
eye movements for classification. For command generation, sig-
nals are decoded simultaneously, and for control of a BCI system, 
they are fused using a combined classifier (Jiang et al., 2014). 
Although EOG is used to remove ocular artifacts from EEG data 

Figure 3 | Electroencephalography (EEG)–electrooculography (EOG)-based brain–computer interface: the blink signals are used for switching between EEG- and 
EOG-based command generation, in which EEG and EOG generate P300-based commands and frown–wink–gaze-based commands, respectively.
5
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
(Li et al., 2015), drowsiness detection (Khushaba et al., 2011) and 
wheelchair control (Ramli et al., 2015) are also among the most 
common applications of EEG–EOG-based systems. Figure  3 
shows the method used to acquire simultaneous EEG and EOG 
data for analysis.
Artifact Removal
Eye blink signals influence brain signals by inducing artifacts in 
the data. Due to such ocular artifacts, false-positive signals appear 
in EEG data, which leads to misclassification and false-command 
generation (Trejo et al., 2006).
A pioneering study in Bashashati et  al. (2007) tested the 
performance of EEG-based self-paced BCI by investigating 
the effects of eye blink signals on data. The results showed that 
the removal of eye blink signals improves BCI performance. 
Another study (Fatourechi et al., 2007) reviewed ocular artifacts 
in EEG data and proposed that the EEG–EOG combination might 
result in better output than an individual modality. Hsu et al. 
(2012) performed a single-trial classification to evaluate accuracy 
differences between artifact-removed and non-artifact-removed 
data. Linear discriminant analysis (LDA) and support vector 
machine (SVM) have been used to classify the data obtained 
from the motor cortex region. The results showed that the average 
classification accuracy obtained by removing EOG artifacts was 
higher than that from non-artifact removal data. Using artifact-
removed features, the obtained accuracies were 84.4% for both 
LDA and SVM, whereas using the non-artifact-removed features, 
only 80.9 and 77.7% accuracies were achieved. This study reveals 
that, with EEG data, EOG artifacts have a decremental effect on 
classification accuracy. In similar studies, an automatic artifact 
correction that combines a regression analysis has been success-
fully implemented for MI tasks (Wang et al., 2012). Also, entailing 
the removal of EOG signals (using eye tracking), thresholding has 
been reported to increase classification accuracy [usingstep-wise 
LDA (SW-LDA)] from 44.7 to 73.1% in hBCI (Yong et al., 2012). 
Independent component analysis (ICA), genetic algorithm (GA), 
and particle swarm optimization for EOG artifact detection and 
removal also have been reported in the literature (Hsu, 2013a,b; 
Daly et al., 2015; Li et al., 2015; Yang et al., 2015). Bai et al. (2016) 
has recently proposed an ICA-based method to reduce the 
muscular/blink artifacts appearing in the prefrontal cortex after 
brain stimulation. The eye movement and muscle artifacts were 
detected using EEG. Ensemble empirical mode decomposition 
was used to decompose signal into multi-components, and then, 
the components were separated with artifact reduced by blind 
source separation method.
Control Commands
The combination of EEG and EOG is important to the improve-
ment of the classification accuracy of BCI systems by artifact 
removal (Zhang et al., 2010). This combination can also be used 
to increase the number of control commands. For this type of 
hBCI, eye blink and eye movement signals are used for command 
generation (Roy et al., 2014; Belkacem et al., 2015b).
Among such applications, early studies have proposed the 
control of wheelchairs using EEG and EOG signals (Kim et al., 
2006). This initial work used the hidden Markov model (HMM) 
to obtain an accuracy of 97.2% for wheelchair control. Eye gaze 
signals were later used to implement wheelchair control using 
SVM as a classifier, in which case, an accuracy of above 80% 
was achieved (Lamti et al., 2013). In another work, eyeball and 
eyelid movements were detected using EEG for wheelchair 
control (Aziz et al., 2014) and the features were extracted using 
eye opening, eye closing, and eye gaze directionality, thus achiev-
ing a 98% accuracy using HMM as a classifier. MI, P300, and 
eye blinking have also been applied for control of a wheelchair 
in four directions using SVM-based classification (Wang et al., 
2014), thereby obtaining an average accuracy of above 85%. In 
a similar work on hBCI, eye gaze and EEG signals were trained 
and tested for wheelchair control using a finite-state machine and 

6
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
neural-network-based classifier and six control commands were 
generated, achieving an accuracy of 97.8% (Ramli et al., 2015). 
Among other works on EEG–EOG-based BCI, 2D cursor control 
has been implemented, using kernel partial least square clas-
sification, with accuracies ranging between 80 and 100% (Trejo 
et al., 2006). EOG and EMG have also been combined with EEG 
to improve mental task classification using Fisher discriminant 
analysis (Zhang et al., 2010). Another study of Jiang et al. (2014) 
has shown that features selected based on different eye movement 
and gaze signals led to 89.3% accuracy using LDA as a classifier. 
Real-time video game control of Belkacem et  al. (2015a) and 
exoskeleton control of Witkowski et  al. (2014) have also been 
implemented in the form of hBCI using a thresholding scheme 
with the accuracies of 77.3 (for six commands) and 63.59% (for 
four commands), respectively. Additionally, robotic arm control 
(Hortal et al., 2015), mobile robot control (Ma et al., 2015), and 
quadcopter control (with eye tracking) (Kim et al., 2014) have 
been developed using EEG–EOG-based hBCI. Most recently, a 
gaze-based game using intentional and spontaneous eye move-
ments with EEG as a marker to control was developed (Shishkin 
et al., 2016): classification of intentional VS spontaneous fixations 
was based on amplitude features from 13 EEG channels using 
300 ms moving window. A 300 ms EOG moving window was 
used to remove the eye movement-related artifacts from the data. 
For the first fixations in the fixation triplets required to make 
moves in the game, LDA-based classification was used to achieve 
90% accurate results. Another interesting study has demonstrated 
the movement control of a turtle using human brain signals (Kim 
et  al., 2016). In this case, SSVEP-based tasks were combined 
with an eye-tracking device to control the turtle in real time. 
The system consists of a glass involving two flickering signals 
for SSVEP generation and direction arrows for detection using 
eye tracking. The movement commands were generated using 
canonical correlation analysis (CCA) in a 2 s window. Four com-
mands were generated using the scheme in which two (turn left/
right movements) commands were generated using SSVEP and 
other two commands (reset and idle) using eye tracking based 
on eye opening and closing. The circuit implanted in the brain 
of the turtle controlled its motion using human brain signals via 
Wi-Fi communication. The event-related desynchronization and 
SSVEP accuracies achieved were 88.3 and 92.7%, respectively.
Drowsiness Detection
Several EEG and EOG studies have investigated the detection of 
drowsiness (Dorokhov, 2003; Duta et al., 2004; Papadelis et al., 
2007; Virkkala et al., 2007a,b). Different feature extraction algo-
rithms have shown the effectiveness of individual EEG system for 
drowsiness detection (Qian et al., 2016, 2017), and the combina-
tion of EEG and EOG seems to be more effective (Sinha, 2008; 
Gharagozlou et al., 2015; Khemiri et al., 2015). For combined 
EEG–EOG signals, various strategies have been adopted. Among 
the recent works since 2010, fuzzy mutual-information-based 
wavelet transform has been used for drowsiness detection to a 
high (95–97%) accuracy (Khushaba et al., 2011). EOG signals and 
visual information have been utilized in the generation of warn-
ings for drowsy drivers (Picot et al., 2012; Akerstedt et al., 2013). 
Maximum overlap wavelet transform has been implemented with 
an accuracy of 96.06% to detect various stages of sleep (Khalighi 
et  al., 2013). Fuzzy neighborhood-preserving analysis showed 
a 93% accuracy for drowsiness detection (Khushaba et  al., 
2013), and a neural-network-based extreme learning algorithm 
obtained 95.6% accurate results for alertness and drowsiness 
signals (Chen et  al., 2015). The most recent work on drowsi-
ness/vigilance estimation using real-time brain monitoring has 
achieved 80.4% accurate results by combining EEG and EOG 
(Cao et al., 2016), in which the EEG bands (α, β, θ, and Δ) were 
combined together with EOG using LDA-based classification to 
develop a real-time drowsiness detection system for drivers.
EEG + EMG
Electromyography signals are generated and detected as a result of 
muscular movement (Trejo et al., 2003; Foldes and Taylor, 2010; 
Cler and Stepp, 2015). These act as an artifact in EEG signals, 
resulting in the false detection of brain signals (Fatourechi et al., 
2007; Bhattacharyya et al., 2013). The purpose behind a hybrid 
EEG–EMG-based hBCI is to combine EEG and EMG signals 
in hBCI. This incorporation of EMG signals is user specific and 
depends on the activity or task performed by that user. The appli-
cations of hybrid approaches vary from a simple game control 
application for an able-bodied person through to a prosthetic 
arm control application for an amputee. Figure 4 shows a typical 
strategy used for incorporating EEG and EMG signals into an 
hBCI system.
The applications of EEG–EMG-based hBCI are found in 
the control area of assistive devices (Leeb et al., 2011; Kiguchi 
et al., 2013). In the early work using EEG with EOG and EMG 
(Kennedy and Adams, 2003), the EMG signals were used to 
categorize different “locked-in” patient types. In their study, six 
types were defined, the first three of which were categorized using 
EMG as follows:
• Patients capable of movement (e.g., eye movement and finger 
movement).
• Patients incapable of movement but showing some detectable 
EMG activity due to partial muscle movements.
• Fully locked-in patients with no muscular activity detectable 
by EMG signals.
The remaining three types of patients were categorized using 
EOG and EEG signals. For EEG–EMG-based BCI, a neuro-
electric interface was developed for real-time applications (Trejo 
et al., 2003). In 2005, a BCI that removes EMG artifacts from EEG 
for mouse-cursor control was developed (McFarland et al., 2005). 
In 2007, a detailed survey on EMG artifacts in EEG signals was 
presented (Fatourechi et al., 2007). In 2010, a study by Brumberg 
et al. (2010) combined EEG and EMG for tetraplegic patients: 
their results showed that communication, however slow, can 
be achieved using EEG–EMG-based hBCI. In that same year, 
jaw muscle contraction and EEG signals were used to generate 
commands for an assistive neuro-prosthetic device (Foldes and 
Taylor, 2010). Also, the use of EMG with EEG was explored in a 
review article on the operation of robotic and prosthetic devices 
(McFarland and Wolpaw, 2010). In 2011, an investigation was 
conducted for the prediction of voluntary movements before 
their occurrence using hBCI (Bai et al., 2011). Vehicle steering 

Figure 4 | Electroencephalography–electromyography (EMG)-based brain–computer interface: one choice is selected using steady-state visual evoked potential 
(SSVEP) and muscle movement is used to change the selected option.
7
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
(Gomez-Gil et al., 2011) and determination of muscle fatigue levels 
(Leeb et al., 2011) using EEG–EMG-based BCI have also been 
reported in the literature. In 2012, simultaneous measurement of 
EEG–EMG signals led to the achievement of an assistive control 
of exoskeletons for locomotion (Cheron et al., 2012), wherein 
a surface-tactile stimulation device was used for the training 
of brain signals, and dynamic recurrent neural network-based 
classifiers were used for training and testing of brain signals. 
Single-trial decoding of reaching movement also was conducted 
using EEG–EMG-based signals (Demandt et al., 2012). A similar 
study (Kiguchi et al., 2013) in 2013 proposed EEG–EMG-based 
control of an artificial arm for above-elbow amputees. An 
EEG–EMG-based motion estimation method was proposed 
for the control of the forearm and the supination/pronation 
motion of the artificial arm. In 2014, signals produced by jaw 
clenching were removed from EEG signals for two-dimensional 
cursor control on a computer screen (Costa et al., 2014). This 
study was later extended to the control of a robotic arm in bi-
dimensional workspace. In 2015, EMG was used in rehabilitation 
applications for robot-assisted exercise tasks (Fels et al., 2015). In 
this case, neuro-feedback was used for intensive motor training 
and EEG–EMG was employed to predict the workload profiles 
for the experience of frustration. A review article by Rupp et al. 
(2015) also discussed the application of EMG for a hybrid neuro-
prosthesis, proposing the use of functional electrical stimulation 
(FES) for therapy. The scheme used EEG–EMG to record brain 
activity and to investigate, on that basis, recovery in muscles 
and the brain. Most recently, new work has been done, which 
combines SSVEP-based tasks with EMG for choice selection (Lin 
et al., 2016). A 60-target hybrid BCI speller was built in this study. 
A single trial was divided into the following two stages: a stimula-
tion stage and an output-selection stage. In the stimulation stage, 
SSVEP and EMG were used together. Every stimulus flickered 
at its given frequency to elicit SSVEP. CCA and mean filtering 
were used to classify SSVEP and EMG, respectively. In the result, 
81% of accurate results were obtained by hybridizing EMG with 
SSVEP activities.
EEG + fNIRS
The research completed on hybrid EEG–fNIRS is still very limited. 
This technology is used mostly to improve classification accuracy 
(Fazli et al., 2012) or increase the number of control commands 
(Khan et al., 2014) in a BCI system. Although the research has 
shown good results for the combination of fNIRS with bio-signals 
(Zimmermann et al., 2013), hybrid EEG–NIRS has shown the 
best results thus far for BCI. In this case, two brain signal acquisi-
tion modalities are combined using neuronal signals (recorded 
using EEG) and hemodynamic signals (recorded using NIRS). 
One important disadvantage of the use of hemodynamics (either 
fMRI or fNIRS), however, is the inherent delay in the response 
(Huppert et al., 2013), which renders the generation of commands 
slow in comparison to EEG. However, in the case of combined 
EEG–fNIRS, this kind of disadvantage can be removed. Also, the 
detection of initial dip (i.e., the phenomenon that HbO decreases 
and HbR increases with neural firing) instead of hemodynamics 
might lead to a better time window selection for the combined 
modalities. Figure  5 shows an approach used to combine the 
EEG–NIRS modalities for BCI.
The first study on hybrid EEG–NIRS for application to BCI 
appeared in 2012 (Fazli et al., 2012). It showed that the combi-
nation of fNIRS’s features (HbO and HbR) and EEG features 
increases the classification accuracy. In this case, a multi-class 
classifier that combined the NIRS and EEG features for classifica-
tion was used. The results showed that using EEG + HbR features, 
the average classification accuracy for motor execution tasks was 
improved from 90.8 to 93.2%. Similarly, for MI tasks, the average 
classification accuracy using EEG + HbO features was increased 
from 78.2 to 83.2%.

Figure 5 | Electroencephalography (EEG)-NIRS-based brain–computer interface: the figure shows a method of removal of false-positive motor imagery signals in 
EEG data using functional near infrared spectroscopy (fNIRS) (delayed decision).
8
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
In 2013, a study of Safaie et  al. (2013) analyzed the steps 
involved in the development of hardware for a hybrid EEG–NIRS 
system, among which was the design of a wireless wearable 
module for simultaneous decoding of brain activity. In 2014, an 
optimal time window for hybrid EEG–NIRS features selection 
was investigated using a SSVEP-based paradigm (Tomita et al., 
2014). The results showed that the optimal window for EEG and 
fNIRS is 10 s. Another study by Khan et al. (2014) showed that 
the number of control commands can be increased by simultane-
ously decoding the EEG and fNIRS activities from different brain 
locations, in which LDA was used as a classifier for both EEG 
and fNIRS, MA and mental-counting tasks were decoded using 
fNIRS, and left- and right-hand tapping were coded using EEG. 
An offline study on tetraplegia patients (Blokland et al., 2014) 
showed that combined EEG–NIRS can be used to decode motor 
attempts and imagined movement with high accuracies up to 
87 and 79%, respectively. A logistic regression classifier based 
on the Bayesian theorem was used for classification, specifically 
by obtaining the EEG data in a 0–15 s window and the fNIRS 
data for classification in a 3–18  s window. The study showed 
that the highest accuracy for tetraplegia patients was obtained 
by combining EEG with HbR. Kaiser et al. (2014) investigated 
the effect of training on cortical brain areas using EEG–NIRS 
with MI as a task. The study compared the subjects with high 
BCI performance (accuracy  >  70%) with those with low BCI 
performance (accuracy < 70%), employing LDA for acquisition 
of the classification accuracies. The results showed that training 
with MI-based BCI affects cortical activations, especially with 
those subjects showing a low BCI performance. In another work, 
hybrid EEG–NIRS showed higher classification accuracies in 
discriminating auditory and visual stimuli (Putze et al., 2014). 
In this work, SVM was used as a classifier to discriminate the 
visual and audio cues and, thus, to develop an hBCI; the accuracy 
achieved was as high as 94.6%.
In 2015, a study used threshold-based discrimination for 
fNIRS signals and SVM-based classification for EEG signals to 
achieve 88% accurate results for self-paced MI tasks (Koo et al., 
2015). In another work, a sensory motor rhythm-based paradigm 
was used to investigate the superiority of multi-modality for idle 
state detection (Lee et al., 2015). The LDA-based classification 
(achieving a 3.6% increase in the accuracy for MI tasks using the 
hybrid modality) showed that the NIRS signals contributed to the 
detection of the active/idle state as well as to the detection of active 
classes to confirm early activity detection. In two other similar 
studies, the MI of both the force and speed of hand clenching was 
decoded using hybrid EEG–NIRS (Yin et al., 2015b,c). In the first 
case, the extreme learning machine classifier was used to decode 
the responses associated with the force and speed imagery of the 
hand with an accuracy of 76.7%, whereas, for the second case (Yin 
et al., 2015c), the features of EEG and NIRS were combined and 
optimized using the joint mutual information selection criterion, 
again utilizing the extreme learning machines, in which case, the 
resulting average classification accuracy for the force and speed 
of hand clenching was 89%.
Several studies on the applications of hybrid EEG–NIRS have 
emerged in 2016, showing the trend of growing research in this 
area. The studies related to BCI applications were also discussed. 
In the case of active tasks, four motor tasks, namely right- and 
left-arm movement and right- and left-hand movement tasks, 
were decoded using the hybrid EEG–NIRS system (Buccino et al., 
2016). Employing the LDA-based classification, the features using 
common spatial patterns (CSP) were compared with the signal 
mean (SM) and signal slope (SS). In the rest-task classification, 
the SM–SS average accuracy was 94.2% and the CSP average 
accuracy was 86.2%. The SM and SS, meanwhile, also performed 
better for right–left classification. SM–SS achieved an average 
accuracy of 72.2%, whereas with CSP, only 67.1% was possible. In 
the case of arm-hand classification though, CSP showed a better 
performance (83.6% average accuracy) than SM–SS (79.9%). In 
the case of passive tasks, the neural and hemodynamic correlates 
were estimated to measure drivers’ mental fatigue levels (Ahn 
et al., 2016). An average accuracy of 75.9% was achieved using an 
LDA-based classifier combining EEG, fNIRS, and ECG modali-
ties. A new hybridization concept for combined EEG and fNIRS 
was introduced by Keles et al. (2016). In their study, different EEG 
bands (α, β, θ, and Δ) were estimated for the resting state. The 

9
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
correlation of an EEG band was convoluted with the modeled 
hemodynamic response (generated using two gamma functions) 
to generate the expected response with the incorporated neuronal 
activity for the hemodynamic signal. Since this was a pioneer 
study, its BCI-related role is yet to be investigated.
The most recent work on hybrid EEG–NIRS-based BCI 
demonstrates decoding of eight commands from the prefrontal 
and frontal cortices (Khan and Hong, 2017). In this work, four 
commands were decoded using EEG, in which two commands 
were generated using an eye blinking-based tasks and two com-
mands were decoded using eye movement tasks. The interesting 
part of this study was the decoding of fNIRS commands in a 2 s 
window. For the selection of an optimal window size, the differ-
ence between the baseline and the first trial was used for channel 
selection. The signal mean and minimum values of HbO were 
used to detect the brain activity in that window. Four commands 
were generated using MA, mental counting, word formation, and 
mental rotation-based tasks, respectively. An average accuracy of 
86% for EEG and that of 75.6% for fNIRS were achieved using 
an LDA-based classifier. This study was tested for the control of 
a drone, whose results showed the feasibility of using prefrontal-
based commands for BCI.
COMBINATION OF BRAIN SIGNALS
The paradigm selection criterion for an hBCI system depends on 
the type of detected activities. As discussed earlier in the Section 
“Introduction,” BCI tasks are categorized into active, passive, and 
reactive types. The respective selection criteria for these tasks 
are based solely on the designed paradigm. In the case of multi-
modality, the paradigm usually consists of the decoding of a single 
activity from the same brain region. Some hBCIs are designed by 
decoding multiple tasks using a single modality. For this purpose, 
usually SSVEP is combined with MI- or P300-based tasks using 
EEG-based signal detection. A study by Zhang et al. (2012) has 
demonstrated a combination of ERP-, N170-, and vertex-positive 
potential signals for EEG-based BCI. ERP-based tasks and evoked 
potential tasks are reactive, as they require external stimulation 
to generate the brain activity (Zander and Kothe, 2011). The 
MI- and MA-based tasks are considered active, as brain activity is 
generated by the user with internal brain activities. In this article, 
we briefly include the cases in which multiple tasks are detected 
simultaneously using a single modality, although the “hybrid” 
term is not used. This has been done in recent studies on fNIRS, 
wherein MI and MA tasks have been combined for the generation 
of multiple BCI commands (Hong et al., 2015; Naseer and Hong, 
2015a). The various signals used in hBCI are discussed below.
Signals Based on Audio and Visual 
Stimulation
These reactive signals are generated from either the occipital 
brain area or the temporal brain area by the provision of either 
visual stimuli (Liu and Hong, 2017) or auditory stimuli (Santosa 
et  al., 2014; Hong and Santosa, 2016). Although mostly such 
stimulations are intended for the generation of brain activity 
from the corresponding lobes (An et al., 2014; Tidoni et al., 2014; 
Wu et al., 2016; Xu et al., 2016), some audio/video stimuli are 
given to generate P300 signals (Rutkowski, 2016). For healthy 
individuals, these stimulations can be effective in generating 
multiple commands. However, they can also be beneficial for 
patients with no motor or eye movements.
SSVEP Signals
These signals are detected mostly in the occipital brain region. 
They are generated by gazing at a stimulus, which causes an 
increase in neural activity in the brain. VEPs are elicited by sud-
den visual stimuli, the repetition of which leads to a stable voltage 
oscillation pattern in EEG that is known as SSVEP. The stimulus 
used for these signals is light flickering at different frequencies 
(sometimes in the “checker board” pattern with changing colors). 
Using SSVEP signals, multiple reactive commands can be gener-
ated. The drawback of this activity is the need for the continuous 
focus on flashing light, which might not be possible or an inef-
fective approach for some patients (Muller-Putz et al., 2005). The 
signal detection time for these signals has been reduced to less 
than 1 s using spatio-temporal features with a reduced number 
of channels (Zhang et al., 2013, 2014; Chang et al., 2016; Wang 
et al., 2016).
P300 Signals
This signal is detected mostly from the parietal brain region. They 
are the ERPs that indicate the responses to specific cognitive, or 
sensory, or motor events. The presentation of a stimulus in an 
oddball paradigm can produce a positive peak in EEG signals. 
This peak appears 300 ms after the onset of the stimulus. The 
stimulus can be visual, auditory, or somatosensory. This evoked 
response in EEG is the P300 component of ERP. These, most 
widely utilized in speller applications, also can generate multiple 
commands for BCI. However, being reactive, these signals are 
mostly used only for healthy subjects (Bayliss et al., 2004; Piccione 
et al., 2006; Turnip et al., 2011; Turnip and Hong, 2012).
Prefrontal Signals
These signals are detected from the prefrontal and dorsolateral 
prefrontal brain regions. They are a good choice for BCI, as 
they require less training effort. In the case of fNIRS, they are 
especially suitable in that they incur fewer motion artifacts and 
less signal attenuation due to detector slippage in hair. Also, given 
their non-utilization of motor activities, they are more effective 
on patients with severe motor disabilities. MA, mental counting, 
and other tasks can be detected as active-type brain signals for 
BCI (Kim et al., 2012; Naseer et al., 2014, 2016a,b). The passive 
activity of drowsiness also can be detected from this cortex (Khan 
and Hong, 2015). Another research has reported the detection of 
music imagery, picture imagery, word generation, etc., from the 
prefrontal cortex (Naseer and Hong, 2015b; Ma et al., 2017). The 
most common task used for BCI purposes is MA.
Motor Signals
These signals are detected mostly from the primary and central 
brain regions (mostly the motor cortex). They are most suitable 
for active BCI applications, as they are natural means of provid-
ing BCI control over external devices (Naseer and Hong, 2013). 

Table 2 | Combinations of brain signals.
Task 1
Task 2
Sensor placement
Modalities 
Activity type
Steady-state visual evoked 
potential (SSVEP)
P300
Occipital and parietal
Electroencephalography(EEG)
Reactive
SSVEP
Motor signals
Occipital and motor
EEG
Combination of reactive and active
Motor signals
P300
Parietal and motor
EEG
Combination of active and reactive
P300
Eye movement
Parietal, motor and eyes
EEG + electrooculography (EOG)
Reactive
Prefrontal signals
Motor signals
Prefrontal and motor
EEG + functional near infrared spectroscopy 
(fNIRS) (fNIRS individual in some cases)
Active for both individual fNIRS and fNIRS 
combined with EEG
10
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
These signals are also targeted for the investigation of motor 
recovery or neuro-rehabilitation. They have wide applications in 
both EEG- and fNIRS-based BCI systems. Two different types of 
brain signals detected from the motor cortex are motor execu-
tion and MI. Motor execution is performed by the movement of 
muscles (mostly in hands or feet). Also, some eye-movement-
related activities stimulate the motor region. Some BCIs use 
motor execution for the generation of commands, whereas in 
other cases, these signals are removed from EEG signals using 
EMG/EOG for better detection of MI. Motor imaging can be 
defined as a covert cognitive process of kinesthetic imagining 
of the movement of one’s own body without the involvement 
of muscular tension, contraction, or flexion (Naseer and Hong, 
2015b). The MI signal is weak relative to the motor execution 
task. Also, not all subjects can perform this activity for BCI. In 
fact, since this activity is generated by the imagining of hand or 
foot movements, it is best suited for active-type BCI. A list of the 
different activities that can be used with a hybrid paradigm is 
provided in Table 2.
SSVEP and MI
The simultaneous decoding of SSVEP and MI signals constitutes 
a hybrid system consisting of active (based on MI) and reactive 
(based on SSVEP) commands. Although only a few relevant 
studies have appeared, they have successfully demonstrated the 
significance of the hybrid paradigm for control (Horki et al., 2011; 
Cao et al., 2014; Li et al., 2014) and rehabilitation applications 
(Daly et al., 2013; Yu et al., 2015).
Control Applications
The early work in this area demonstrated the control of a 2-DoF 
artificial limb using combined MI- and SSVEP-based tasks (Horki 
et al., 2011). The objective of this study was to operate the elbow 
and grasp movements of the artificial limb using BCI for spinal 
cord injury (SCI) patients. In this case, MI was used to control 
the grasp movements, whereas SSVEP was used to operate the 
elbow movements. According to their data, 87% of accuracy 
was achieved for the MI-based tasks and 91% of accuracy was 
achieved for SSVEP using LDA classification.
The control of a wheelchair using MI and SSVEP has been pro-
posed in two studies (Cao et al., 2014; Li et al., 2014). In the first 
case (Cao et al., 2014), MI was used for the chair’s left and right 
turning and SSVEP was used for the speed control (three com-
mands). An SVM-based classifier resulted in 90.6% of accurate 
control using the hybrid protocol. In the second case (Li et al., 
2014), six commands were used to operate the wheelchair. Two 
commands were generated using MI (left and right rotations), 
and the remaining four commands (start, stop, forward, and 
backward movements) were generated using SSVEP.
In 2015, a study by Duan et al. (2015) demonstrated the control 
of a robot by combining SSVEP and MI tasks: SSVEP was used 
to generate three commands to make the robot move forward, 
turn left, and turn right, while MI was utilized to control the 
grasp motion of the robot. Meanwhile, CCA was used for SSVEP 
classification and power spectrum was employed to estimate the 
motor-imagery-related rhythms. The results suggested that the 
β-band was significant in MI. Overall, 80% accurate results were 
obtained for three subjects.
In terms of command generation, a study in 2016 proposed 
an improved tensor-based multi-class multi-modal scheme 
especially for EEG analysis in hybrid BCI (Ji et al., 2016). It com­
bined SSVEP- and MI-based tasks for command generation. As 
per their method, the data need not be divided into individual 
groups and fed into separate processing procedures; rather, SVM 
was extended to multi-class classification for hybrid tasks. 
Applications in three datasets suggest that the proposed scheme 
not only can identify the different changes in the dynamics of 
brain oscillations induced by different types of tasks but also can 
capture the interactive effects of simultaneous tasks.
Motor Training
In the case of motor training, an initial investigation of hybrid 
MI-SSVEP was performed with cerebral palsy (CP) patients 
(Daly et al., 2013). The goal was to investigate the use of MI and 
SSVEP for CP. Six patients among 14 were able to exercise con-
trol via MI-based tasks, and three patients were able to exercise 
control via the SSVEP-based paradigm. The results served to 
demonstrate the potentiality of MI–SSVEP-based tasks for CP 
patients.
A recent study reported on MI training using SSVEP-based 
tasks with continuous feedback for an hBCI (Yu et al., 2015). 
During the initial training sessions, the subjects focused on 
the flickering buttons to evoke SSVEPs as they performed MI 
tasks. As the training progressed, the subjects were allowed 
to decrease their visual attention on the flickering buttons, 
provided that the feedback remained effective. The feedback 
was based mainly on motor imagery-based tasks. The results 
demonstrated that the subjects could generate distinguishable 
brain patterns of hand MI after only five training sessions last-
ing approximately 1.5 h each. An average accuracy of 89.03% 
was obtained after training using the hybrid paradigm with the 
LDA-based classifier.

11
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
SSVEP and P300
The combination of SSVEP and P300 signals results in a reactive 
hBCI. These brain activities are simultaneously recorded from the 
occipital and parietal brain areas. This paradigm is used repeat-
edly in several control and rehabilitation applications.
Strategies for Signal Detection and Control
The initial step of hBCI can be established when multiple brain 
activities are simultaneously decoded for the detection of the 
patient’s intention (Panicker et al., 2011). In 2013, an hBCI was 
used for humanoid robot navigation using combined SSVEP 
and P300 signals (Choi and Jo, 2013). The data in this case were 
recorded from the motor, parietal, and visual cortices. The results 
of this experiment showed that a hybrid SSVEP–P300-based 
BCI can be used to navigate a robot with ease. In later works 
(Combaz and Van Hulle, 2015; Wang et al., 2015), simultaneous 
detection of SSVEP–P300 has been reported for oddball as well 
as shape- and color-changing paradigms. In 2014, the hybrid 
SSVEP–P300-based paradigm was used in the development of 
speed- and direction-based cursor control (Bi et al., 2014). In this 
case, the stimuli for P300 were distributed at the top and bottom 
edges of the screen, whereas the stimuli (accessed by turning 
control knobs clockwise or counter-clockwise) for detection of 
the SSVEP signals were shown on the left and right sides of the 
screen. Their SVM-based classification showed an accuracy of 
above 90% for hBCI.
Awareness of the patients with consciousness disorders has 
also been detected using the combined paradigm of SSVEP and 
P300 (Pan et al., 2014). In this case, two photos were presented to 
each patient: one was the patient’s own photo and the other was 
unfamiliar ones. The patients were instructed to focus either on 
their own or on the unfamiliar photo. The BCI system determined 
which photo the patient focused on by using both P300 and 
SSVEP features. Eight patients [four in a vegetative state (VS), 
three in a minimally conscious state (MCS), and one in a locked-
in syndrome (LIS) state] participated in the experiment. Using 
SVM-based classification, one of the four VS patients, one of the 
three MCS patients, and the LIS patient were able to selectively 
attend to their own or unfamiliar photos (classification accuracy, 
66–100%). Two additional patients (one VS and one MCS) failed 
to attend to unfamiliar photos (50–52%) but achieved significant 
accuracies for their own photos (64–68%). Finally, the other three 
patients failed to show any significant response to the commands 
(46–55%). These results strongly support the necessity to use 
an hBCI paradigm for patients. In another study (Allison et al., 
2014), a four-choice selection scheme was developed resulting in 
an improved accuracy using P300 and SSVEP. In order to gener-
ate P300 signals, the subjects had to focus on one of the four boxes 
that were displayed on the screen. The shown boxes change their 
color from red to white (one box at a time) for 100 ms with a 
25 ms delay for the next flash. A 4 s trial was used to record P300 
signals. To generate SSVEP, the boxes were flickered instead of 
being flashed for 4 s. The flickering frequency was 6, 8, 9, and 
10 Hz. The subjects were asked to focus on one box and count 
the number of flickers to simultaneously generate the hybrid 
signals. LDA was used for P300 signal classification, while CCA 
was used to classify SSVEP signals. When classified separately in 
their hybrid paradigm, the average accuracy for p300 was about 
99.9%; however, the accuracy for SSVEP was 67.2%.
The importance of the reactive task has been shown in a 
comparative study of telepresence-robot and humanoid robot 
control (Zhao et al., 2015). Four-class SSVEP and six-class P300 
achieved an average accuracy of 90.3 and 91.3%, respectively, 
using LDA as a classifier. For wheelchair control, the hybrid 
SSVEP–P300 study (Li et al., 2013) used buttons flickering in 
a graphical user interface (GUI). The movement options were 
selected by focusing on the selected direction of the GUI. The 
SVM-based classification resulted in high accuracy (>  80%), 
thus demonstrating the importance of the hBCI paradigm for 
wheelchair control. In another work (Wang et al., 2014), blink 
signals (EOG) were also added as a part of hBCI for wheelchair 
control.
Most recently, a new scheme that uses the steady-state soma-
tosensory evoked potentials (SSSEPs) has emerged (Breitwieser 
et al., 2016; Pokorny et al., 2016). The hBCI in these cases combines 
SSSEPs and P300 potentials evoked by twitches randomly embed-
ded into the streams of tactile stimuli. The twitches are given 
in the form of stimulation to the left-/right-hand index finger. 
Both of the mentioned studies have used LDA for classification. 
Pokorny et al. (2016) showed that the accuracies of SSSEP and 
P300 were 48.6 and 50.7%, respectively. However, combining the 
features of SSSEP and P300 resulted in 55.5% average accuracy for 
the twitching task. Hybridization related to SSSEP-based tasks is 
relatively new, and its full potential is yet to be determined.
Hybrid Strategies for Spellers
A speller paradigm is based on a combination of rows and 
columns displayed and flickered for command generation. The 
first study on a hybrid SSVEP–P300-based speller paradigm 
(Xu et al., 2013) used the combination of SSVEP and P300 fea-
tures. Its aim was to distinguish the SSVEP and P300 activities 
in the brain by monitoring the data from the motor, parietal, 
and occipital brain regions. The results showed that during a 
non-target phase, SSVEP activity was evident, but after the 
target stimuli were given, it was replaced by P300 potentials. 
SSVEP-B (sub-signals in the absence of SSVEP) mostly appears 
in the occipital region (Oz), which can be compared with P300 
activity in the motor region (Cz). Another work (Yin et al., 2013) 
employed random flashing and periodic flickering to evoke 
P300 and SSVEP simultaneously. This was done to increase the 
differences between the row and column symbols. A SW-LDA 
was used to achieve an average accuracy of 93.85%. Another 
study of using such SW-LDA (Xu et al., 2014) achieved an aver-
age accuracy of 96.8% for P300 and 95.7% for SSVEP. In this 
case, the SSVEP–P300 activities were decoded in parallel. Four 
flashing patterns were used to detect the SSVEP, and the speller 
characters were divided into four blocks. A block was selected 
using SSVEP, and the characters were selected using P300.
A high accuracy (>90%) was obtained using SW-LDA in a 
speedy hBCI spelling approach (Yin et al., 2014). To evoke the 
P300 and SSVEP potentials simultaneously, this study used flash-
pattern mechanisms composed of random flashings and periodic 
flickering. The random flashings were created by highlighting 
items using orange crosses in a pseudorandom sequence, and 

12
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
the periodic flickering was achieved using white rectangular 
objects alternately appearing on and disappearing from a black 
background. The use of the speller-based paradigm in the form 
of a hybrid SSVEP/P300 system for the selection of 64 options 
(64 control-command generations) in BCI has been reported 
(Yin et  al., 2015a). In this study, for SSVEP classification and 
SW-LDA for P300 signals, the canonical cross-correlation approach 
was used. Also, maximum probability estimation was utilized for 
data fusion, which resulted in a 95.18% average accuracy.
In an attempt to navigate a vehicle to its destination, the use 
of the SSVEP–P300-based speller paradigm above has been 
reported (Fan et al., 2015). Specifically, the speller was used for 
entering the destination location and flickering “checker board” 
stimuli (12 Hz and 13 Hz) were used for destination selection 
and deselection, in which LDA-based classification achieved an 
average accuracy of 98.09% for real-driving conditions.
MI and P300
The MI- and P300-related tasks have been widely designed for 
applications in real-world environment (Li et al., 2010; Su et al., 
2011; Long et al., 2012a,b; Yu et al., 2012, 2013; Bhattacharyya 
et al., 2014; Naito et al., 2014; Kee et al., 2015; Zhang et al., 2016a). 
The corresponding signals are obtained by positioning electrodes 
around the motor and parietal brain regions. In the work of 
Li et al. (2010), MI and P300 were combined for the control of a 
cursor on the screen using SVM as a classifier (90.75% average 
accuracy). In the work of Long et al. (2012b), target selection or 
rejection (mouse-clicking) features were added resulting in the 
average accuracy of 92.8%.
Navigation and target selection in a virtual environment was 
demonstrated in Su et al. (2011) using the hybrid MI–P300-based 
paradigm. In their work, MI was used for navigation and P300 for 
target selection (three control buttons). Overall, five commands 
were generated using Fisher LDA- and SVM-based classification 
(84.5% for MI and 81.7% for P300).
In the work of Long et al. (2012a), the same hybrid paradigm 
was used to control the direction and the speed of a simulated and 
afterward a real wheelchair. The turning (left and right directions) 
controls were associated with left- and right-hand imageries. The 
wheelchair was decelerated using a foot-movement imagery. The 
acceleration was represented using P300 signals. In this case, 
the LDA-based classification resulted in 71.6% accuracy for MI and 
80.4% for P300. Another study of Yu et al. (2012) demonstrated 
the utility of hybrid MI–P300 for cursor-controlled on-screen 
feature selection-based Internet surfing. In that study, SVM- 
based classification resulted in an average accuracy of 93.2%.
In 2013, a real-time electronic mail communication system 
was implemented to enable clients/users to receive, write, and 
attach files to their email (Yu et al., 2013). According to their 
hybrid MI–P300 paradigm, the SVM-based classifier yielded a 
high accuracy (average: >90%) for the system.
In 2014, robot arm movement control for rehabilitation was 
implemented using the hybrid method (Bhattacharyya et  al., 
2014). Arm movement was controlled by MI signals, while P300 
was used to detect the stopping intention. A 95% success rate 
was achieved in the SVM-based classification. The recent work 
on this paradigm has focused on optimal feature selection and 
simultaneous classification methods (Naito et al., 2014; Kee et al., 
2015). Also, the use of optimal feature selection for the enhance-
ment of output accuracy was another issue in Naito et al. (2014).
In 2015, GA-based strategy was proposed for the optimization 
of channel selection in the process of simultaneous recording of 
MI and P300 (Kee et al., 2015). A recent contribution of 2016 
proposed an autonomous wheelchair navigation system that 
acquires the destination and waypoint based on the existing 
environment (Zhang et al., 2016a). In this case, the BCI module 
selects and determines the destination using MI and P300, 
respectively.
Mental and Motor Tasks
For mental VS motor task purposes, paradigms are designed to 
obtain the brain activities from the prefrontal and motor corti-
ces. Both EEG and fNIRS have provided good results for these 
tasks. In these cases, mostly a working memory-related task 
is combined with a motor task to achieve the BCI system. For 
the localization of neuronal sources, EEG was applied using six 
cognitive tasks (arithmetic, navigation imagery, auditory recall, 
phone imagery, and MI of the left and right hands) and compared 
against the idle state to localize the brain location (Dyson et al., 
2010). The spatial areas suggested a clear discrimination between 
the arithmetic- and auditory-related tasks, while the MI-related 
tasks were discriminated according to the baseline.
As for fNIRS, MA has been combined with music imagery 
for simultaneous decoding of brain activity (Power et al., 2010, 
2011; Stangl et al., 2013). In this case, however, the prefrontal 
channels were averaged and the activities were differentiated 
using an HMM-based classification method. MA and MI have 
also been reported to be combined in the case of fNIRS. Four 
commands have been generated by simultaneous decoding of 
mental counting-, arithmetic-, and imagery-related tasks (Hong 
et al., 2015; Naseer and Hong, 2015a). In these cases, LDA-based 
classification was used to decode the activities from the prefrontal 
and motor cortices.
In a multi-modality case, meanwhile, four commands were 
generated by decoding mental tasks (MA and mental counting) 
using fNIRS and motor tasks (left- and right-hand tapping) using 
EEG for hBCI (Khan et al., 2014). This work was later extended for 
the decoding of eight commands using eye movement and mental 
tasks (Khan and Hong, 2017). In this case, EEG was employed to 
decode two and three eye blinks and left- and right-eye move-
ments, whereas fNIRS was used to decode mental arithmetic-, 
mental counting-, word formation-, and mental rotation-based 
tasks. The decoded eight commands were used to operate a 
quadcopter in the 3D space.
Hybrid Audio–Visual Tasks
In this category, there is not much hybrid research. In one work 
(Putze et al., 2014), hybrid EEG–NIRS was used to discriminate 
the auditory and visual stimuli. The details on this study can be 
found in the above “EEG + NIRS” section. Tidoni et al. (2014) 
used audio feedback to improve the performance of the BCI 
system. Six commands were generated using SSVEP-based tasks 
for a robot’s pick-up and placing tasks. It is found that audio–
visual synchrony between footstep sounds and actual humanoid 

13
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
walking reduces the time required for steering the robot. This 
demonstrates the possibility of using auditory feedback congru-
ent with humanoid actions to improve the motor decisions of the 
BCI. An et al. (2014) used six auditory stimuli for the selection of 
36 visual symbols using EEG recording for a gaze-independent 
BCI. When a subject focuses on a sound, a selection screen con-
sisting of six symbols is shown. The subject can then choose one 
from the six visual symbols for choice selection. This paradigm 
increased mental fatigue, as the user has to focus on the audio 
cues. An LDA-based scheme was used, and 87.7% of accurate 
results were generated. In another work of Barbosa et al. (2016), 
in contrast to An et al. (2014), a P300-based BCI was used for 
combining visual and audio stimuli. In this case, the audio stimuli 
were natural spoken words, which reduced the mental work load. 
The average online accuracy for their hybrid approach was 85.3%, 
which represents an improvement of 32% relative to independent 
audio or visual stimuli.
ADVANTAGES of hBCI
Although the combination of two modalities increases the sys-
tem cost, its efficiency is significantly improved. Since most BCI 
systems are designed for the purpose of rehabilitation or commu-
tation (of patients), hBCI is a better mean in achieving this goal. 
A complete BCI that can be used by patients is yet to be designed. 
However, the combination of the modalities can provide the first 
step toward the goal. Each hBCI has different advantages and 
applications. The use of EEG–EOG and EEG–EMG systems, 
for example, are viable for patients capable of minor eye and 
muscular movements, whereas a different approach is required 
for completely locked-in patients. In this regard, hybrid EEG–
fNIRS might provide better results. In other words, whereas the 
advantages of hBCI vary with the combination of modalities, the 
main goal remains the same.
Minimization of False Signal Detection
The BCI research has demonstrated the use of EEG in several 
communication and control applications. In most cases, MI was 
used to generate the commands for communication (Machado 
et  al., 2010; Bi et  al., 2013; Hwang et  al., 2013; Ahn and Jun, 
2015; Maria Alonso-Valerdi et al., 2015). However, it is difficult 
for patients to perform an MI activity. Also, the detection of MI 
signals requires extensive processing, and false detection can 
result in severe consequences in real environments. Long-term 
use of SSVEP and P300 can also increase visual fatigue of the 
subjects, thereby incurring a false detection of signals for BCI. 
Thus, proper measures are required to increase the accuracy 
of the system by minimizing the false detection rate. This can 
be achieved by combining multiple modalities. In such a case, 
simultaneous feature decoding results in a better system accuracy. 
The most common example is the hybrid EEG–fNIRS.
Greater Suitability for BCI
The number of active commands used for system control is a 
central issue for BCIs. The main problem in EEG-based BCI sys-
tems is the loss of accuracy resulting from an increased number 
of (active) commands. Although the number of commands can 
be increased using reactive tasks, it is difficult to make the patient 
concentrate on reactive tasks for a long duration. Although strat-
egies are being designed to overcome this problem, the results 
have not yet been proved sufficiently effective for BCI adoption 
(Lesenfants et al., 2014). In this context, the hBCI plays an impor-
tant role in providing the potential for an increased number of 
commands without undo-influence on classification accuracy. 
The approach most widely employed in the brain signal-based 
control of wheelchairs is to increase the number of commands by 
decoding the features from two modalities separately.
Tables 3–5 list all of the important studies from 2010 to 2016 
that have combined two modalities to decrease false detection 
and enhance classification accuracy for BCI. The tables show 
the relevant hBCI studies for the enhancement of accuracy and 
increase in control commands. Ideas on increasing accuracy and 
the total number of commands can be deduced from them. We 
divided the tables into active, passive, and reactive BCI categories. 
This information can be helpful to the selection of brain signal 
acquisition modalities based on the types of activities. Also, we 
have incorporated the classifier and window size information 
in each table, which might be helpful to prospective researchers 
looking a method to enhance classification accuracy and increase 
the number of commands.
APPLICATIONS
In recent years, significant progress has been made in hBCI 
research. Although some studies have demonstrated a success 
in wheelchair (and other devices) controls, most of them have 
involved healthy subjects. The true potentials of those modes of 
control, then, cannot be considered to have been fully discovered. 
An hBCI increases the classification accuracy (e.g., EEG + fNIRS), 
but this results in slower command generation. In cases where the 
number of commands is increased (e.g., EEG + EOG), a uniform 
window for command generation is needed. These are additional 
drawbacks of hBCI that have yet to be addressed. Also, most 
hBCIs were tested in a controlled laboratory environment where 
the user can comfortably concentrate on mental tasks, whereas in 
real situations, a high performance of concentration-dependent 
mental tasks (e.g., MI and MA) is much more challenging.
Hybrid BCI for Patients
The ultimate goal of a BCI system is to provide assistance to 
patients (Kim et al., 2011). This assistance can be in the form of 
formulating a methodology that can be used to communicate 
with the environment. The patient should be able to express 
his/her thoughts through the use of the BCI system. Regarding 
rehabilitation, a BCI system has the capacity to distinguish 
improvement from non-improvement as a result of therapy and 
brain stimulation. Detection of seizures (Nguyen et  al., 2012, 
2013), epilepsy (Peng et al., 2014; Pouliot et al., 2014; Visani et al., 
2015), and estimation of improvement in motor functions after 
stroke (Das et al., 2016) are such examples pursuing hBCI for 
patients. The current BCI system, however, lacks the potential 
to provide detailed functions. In fact, an hBCI can be a more 
powerful tool than a single-modality BCI, as it can provide more 
reliable information for control and rehabilitation applications 

Table 3 | Important active hybrid brain–computer interface studies with applications to increased accuracy and number of commands for brain–computer interface studies (BCI) (from 2010 to 2016).
Reference
Brain area 
Activity
Modality
Application
Analysis 
type
Classifier
Commands
Accuracy
Window size
Li  
et al. (2010)
Whole brain
Motor imagery 
(MI) and P300
Electroencephalography 
(EEG) + electrooculography 
(EOG)
Cursor control in 2D
Online
Support 
vector 
machine 
(SVM)
4
92.8%
0–600 ms after 
button flashes on 
the screen for 8 s
Allison  
et al. (2010)
Motor and 
occipital 
regions
MI and 
steady-state 
visual evoked 
potential 
(SSVEP)
EEG
Option selection from the 
screen
Offline
Linear 
discriminant 
analysis 
(LDA)
4
74.8% for MI, 76.9% for SSVEP, 
and 81% for hybrid
3–5 s window
Zhang  
et al. (2010)
Motor, parietal, 
and occipital 
regions
Mental task
EEG + EOG + electromyography 
(EMG)
Application to devices 
control
Offline
Fisher 
discriminant 
analysis 
combined 
with 
Mahalanobis 
distance
4
75.3% average for two-class and 
54.1% for four-class
0–1 s
Su  
et al. (2011)
Whole brain
MI and P300
EEG 
Virtual environment control
Online
SVM and 
fisher LDA
5
84.5% for MI and 81.7% for 
P300
0–2 s for MI and 
0.7 s for P300
Leeb  
et al. (2011)
Motor cortex
Motor 
execution
EEG + EMG
Application to patient 
motor training 
Online
Bayesian
2
87% for individual and 91% for 
hybrid case
0.5 s for EEG and 
0.3 s for EMG
Long  
et al. (2012a)
Frontal, central, 
parietal, and 
occipital 
regions
P300 and MI
EEG
Direction and speed 
control for wheelchair
Online
LDA
5
75.4% for hybrid task
1 s
Yong  
et al. (2012)
Motor cortex
Hand and eye 
movement
EEG + EOG (eye tracker)
Artifact removal for choice 
selection
Online
SW-LDA
2
True positive rate increases from 
44.7 to 73.1% (in 1 s)
1 s
Fazli  
et al. (2012)
Frontal, motor, 
and parietal 
cortex
MI and Motor 
execution
EEG + functional near infrared 
spectroscopy (fNIRS)
Application to control
Offline
LDA
2
93.2% (motor execution) and 
83.2% (MI)
0.75 s for EEG, 6 s 
prior to stimulus 
onset and up to 15 s 
after stimulus onset 
using 1 s sliding 
window for fNIRS
Choi and Jo 
(2013)
Whole brain
SSVEP, MI, and 
P300
EEG
Humanoid robot 
navigation and recognition
Real time
CCA
6
84.6% for P300 and 84.04%  
for SSVEP
2 s
Cao  
et al. (2014)
Frontal, central, 
parietal and 
occipital cortex
SSVEP and MI
EEG
Brain-actuated switch for 
wheelchair control
Online
SVM
8
90.6%
–
Wang  
et al. (2014)
Whole brain
MI, P300 and 
eye blinking
EEG + EOG
Asynchronous wheelchair 
control
Online
SVM
7
91, 93, 89, and 92% for forward, 
backward, stop with special 
threshold, and stop with optimal 
threshold, respectively
4 s 
(Continued)
14
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35

Reference
Brain area 
Activity
Modality
Application
Analysis 
type
Classifier
Commands
Accuracy
Window size
Khan  
et al. (2014)
Prefrontal and 
motor cortex
Mental 
arithmetic, 
mental counting 
and motor 
execution
EEG + fNIRS
Application to wheelchair 
control
Online
LDA
4
94.7% for left and right 
movement commands (EEG) and 
80.2 and 83.6% for forward and 
backward using fNIRS
0–10 s for fNIRS and 
0–1 s for EEG
Kim  
et al. (2014)
Complete brain
Eye movement
EEG + Eye tracker
Quadcopter control
Real time
SVM
8
91.67%
5 s 
Jiang  
et al. (2014)
Motor cortex
MI and eye 
movement
EEG + EOG
Application to BCI control
Online
LDA
4
90.4% for MI, 91.1% for relax, 
96.4% for gaze left, and 97.3% 
for gaze right
3 s
Kaiser  
et al. (2014)
Motor cortex
MI
EEG + fNIRS
Application to brain 
monitoring
Online
LDA
1
3.6% increase in accuracy by 
hybrid modality
3–7 s
Lorenz  
et al. (2014)
Whole brain
ERP and MI
EEG
BCI driven 
neuro-prosthesis
Online
LDA
6
Maximum selection accuracy 
of 98.46% and maximum 
confirmation accuracy of 96.26%
1 s
Blokland  
et al. (2014)
Motor cortex
MI and motor 
execution
EEG + fNIRS
Application to tetraplegia 
patients
Offline
–
2
87% for motor attempt and 79% 
for MI in tetraplegia patients
3–15 s for fNIRS and 
0–15 s for EEG
Bai  
et al. (2015)
Whole brain
MI and P300
EEG
Opening, closing, 
selection of files on 
explorer
Online
SVM
9 (can achieve 
50)
>90%
4 s window for MI 
and 600 m for P300
Hortal  
et al. (2015)
Motor and 
parietal cortex
Mental 
imagination
EEG + EOG
Robotic arm control for 
pick and place task
Real time
SVM
6
Task 1: 71.13% and Task 2: 
61.51%
0.5 s to synchronize 
output to BMI
Hong  
et al. (2015)
Prefrontal and 
motor cortex
Mental 
arithmetic and 
MI
fNIRS
Applications to three 
choice selection
Offline
LDA
3
75.6%
2–7 s
Naseer and 
Hong (2015a)
Prefrontal and 
motor cortex
Mental 
arithmetic, 
mental counting 
and MI
fNIRS
Decoding answers to four-
choice questions
Offline
LDA
4
RMI, LMI, MA, and MC were 
correctly classified as 72.9, 64.2, 
65.1, and 71.0%, respectively
2–7 s
Yin  
et al. (2015c)
Motor cortex
MI task
EEG + fNIRS
Increase in accuracy for 
BCI
Online
ELM
2
88%
0.5 s for EEG and 
0–12 s for fNIRS
Koo  
et al. (2015)
Motor cortex
Self-paced MI
EEG + fNIRS
Application to device 
control
Online
SVM
2
88% average accuracy
10 s for fNIRS 
and three 5 s time 
windows with step 
size of 2.5 s for EEG
Buccino  
et al. (2016)
Motor cortex
Arm and hand 
movement 
EEG + fNIRS
Hand movement 
discrimination
Online
LDA
2 commands 
simultaneously
94.2% (for rest-task 
classification)
0~6 s hybrid
Shishkin  
et al. (2016)
Whole brain
Eye gaze
EEG + EOG
Game control
Offline
LDA
–
90%
0.3 s for EEG and 
0.2–0.5 s for EOG
Khan and Hong 
(2017)
Frontal
Mental task and 
eye movement
NIRS + EEG
Applications to 
quadcopter control
Online
LDA
8
76.5% for NIRS and 86% for 
EEG 
1 s for EEG and 2 s 
for NIRS
TABLE 3 | Continued
15
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35

Table 4 | Important reactive hybrid brain–computer interface studies (from 2010 to 2016).
Reference
Brain area
Activity
Modality
Application
Analysis 
type
Classifier
Commands
Accuracy
Window size
Yin  
et al. (2013)
Parietal and 
occipital cortex
P300 and steady-
state visual evoked 
potential (SSVEP)
 Electroencephalography 
(EEG)
Speller
Online
SW-LDA
Up to 36
93.85% using 
hybrid paradigm
All rows and columns 
were flashed in 2.88 s
Zimmermann  
et al. (2013)
Motor cortex
Isometric finger-
pinching task
fNIRS + bio-signals (ECG)
Feasibility for BCI
Offline
Hidden 
Markov model 
(HMM)
1
88.5%
5–20 s
Li  
et al. (2013)
Whole brain
SSVEP and P300
EEG
Wheelchair control
Online
Support 
vector 
machine 
(SVM)
6
>80%
0–0.6 s after a button 
flash complete for P300 
and 3.2 s for SSVEP
Xu  
et al. (2013)
Whole brain
SSVEP and P300
EEG
BCI speller for target selection
Online
SW-LDA
9
93.3% for 
P300 + SSVEP-B
0–0.8 s after the onset
Bi  
et al. (2014)
Parietal and 
occipital cortex
P300 and SSVEP
EEG
Speed and direction for cursor 
control
Online
SVM
4
>90
4 s
Aziz  
et al. (2014)
Frontal and 
occipital
Eye movements
EEG + electrooculography 
(EOG)
Automated wheelchair navigation
Online
SVM, HMM
5
98%
0.5 s
Li  
et al. (2014)
Motor and 
occipital
Motor imagery and 
SSVEP
EEG
Wheelchair control
Real time
SVM
6
−
−
Witkowski  
et al. (2014)
Motor cortex
Hand-grasping 
motion assisted with 
exoskeleton
EEG + EOG
Assistive rehabilitation 
applications
Online
Sensitivity 
index
4
Average accuracy 
62.28% for two 
conditions
5 s
Putze  
et al. (2014)
Auditory and 
visual cortex
Visual and auditory 
stimuli
EEG + functional near 
infrared spectroscopy 
(fNIRS)
Application to patient choice 
selection
Online
Linear 
discriminant 
analysis (LDA), 
SVM
2
94.7% average
Four window sizes 1, 2, 4, 
8, and 16 s
Tomita  
et al. (2014)
Visual cortex
SSVEP-based task
EEG + fNIRS
Optimal window selection for 
hybrid EEG–NIRS
Offline
−
1
85% average 
accuracy (in 10 sec 
optimal window)
0–10 s
Fan  
et al. (2015)
Parietal and 
occipital
SSVEP and P300
EEG
Vehicle destination selection 
system
Online
LDA
11
99%
0–0.51 sec from onset for 
P300 and 8 s for SSVEP
Ma  
et al. (2015)
Parietal and 
occipital
P300 and eye blink
EEG + EOG
Mobile robot control
Real time
LDA
9
87.3% for average 
of five trials
~1.6 s
Combaz and  
Van Hulle (2015)
Whole brain
P300 and SSVEP
EEG
Applications to locked-in patients 
option selection
Online
SVM
12
Maximum 
achieved > 95%
200 ms before stimulation 
to 800 ms after stimulation 
for experiment 1
Wang  
et al. (2015)
Whole brain
P300 and SSVEP 
(shape changing and 
flickering-hybrid)
EEG
Development of new paradigm 
with application to devices 
control
Online
canonical 
correlation 
analysis 
(CCA), 
Bayesian LDA
4
Overall 20% 
increase in SSVEP 
classification, 100% 
for P300
Flash start to the flash end 
for SSVEP, single flashes 
lasting 0.8 s for P300
(Continued)
16
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35

Reference
Brain area
Activity
Modality
Application
Analysis 
type
Classifier
Commands
Accuracy
Window size
Ramli  
et al. (2015)
Motor and 
occipital
Eye gaze
EEG + EOG
Application to BCI applications 
(wheelchair control)
Online
Finite-state 
machine 
(FSM)
6
97.88%
0.5 s
Yin  
et al. (2015a)
Parietal and 
occipital cortex
P300 and SSVEP
EEG
Speller paradigm with 
applications to BCI systems 
control
Online
SW-LDA for 
P300, CCA for 
SSVEP
Up to 64
95.18%
0.8 s epochs after 
stimulation
Kim  
et al. (2016)
Occipital
SSVEP and eye 
movement
EEG + EOG
Turtle movement control
Online
CCA
4
83% for 
event-related 
desynchronization 
(ERD) and 92.7% 
for SSVEP
2 s
Lin  
et al. (2016)
Occipital
SSVEP
EEG + EMG
Choice selection
Online
CCA
2
81%
0.5–5 s
TABLE 4 | Continued
17
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
for patients. Indeed, the recent hybrid combinations have shown 
successes. The hBCI can be more successful for patients in the 
following areas.
Neuro-Rehabilitation
Hybrid brain–computer interface systems can be used to restore 
some of the lost motor and/or cognitive functions for individuals 
with stroke and SCI. Neuro-feedback is required to train indi-
viduals to self-regulate the brain activity (Weyand et al., 2015). 
Although fNIRS has demonstrated the effectiveness for brain 
activity monitoring (Kassab et al., 2015), the use of both EEG 
(Gruzelier, 2014) and fMRI (Laconte, 2011; Weiskopf, 2012) 
has been more widely reported. EEG is employed due its high 
temporal resolution, whereas fMRI is preferred due to its high 
spatial resolution. However, EEG suffers from the limitations 
of imprecise localization and the inaccessibility of subcortical 
areas, while fMRI is slower in the detection of hemodynamic 
activity. Hybrid EEG–NIRS-based hBCI, then, is most suited for 
these cases. Indeed, the spatial and temporal issues are resolved 
by the combination of the two modalities. Also, it provides the 
advantage of simultaneous monitoring of electrophysiological 
and hemodynamic signal monitoring. For neuro-rehabilitation 
purposes moreover, hybrid EEG–NIRS’s use of neuro-feedback in 
MI-based tasks has been successfully demonstrated (Kaiser et al., 
2014). Most recently, fNIRS–EEG study has shown its contribu-
tion for refractory epilepsy patients (Vannasing et al., 2016). This 
case study demonstrated the potential of NIRS to contribute 
favorably to the localization of language functions in children 
with epilepsy and cognitive or behavioral problems and showed, 
moreover, its potential advantages over fMRI in pre-surgical 
assessment.
Communication and Control
The major role of BCI is to serve as a mean of communication for 
patients with motor disorders (e.g., LIS and SCI). For this pur-
pose, different approaches have been demonstrated using hBCI. 
FES and EEG have been combined with brain signal acquisition 
systems for motor restoration (Rohm et al., 2013). In this case, the 
patients were trained using FES- and MI-based tasks. One year of 
training resulted in 70.5% accuracy of MI tasks for SCI patients. 
Lim et al. (2013) developed a system that allows users to express 
their binary intention without need to open their eyes. A pair 
of glasses with two light emitting diodes flickering at different 
frequencies was used to present visual stimuli to participants 
with their eyes closed. The binary commands were generated 
using SSVEP. This system showed 80% accurate results for ALS 
patients. An alternative use of EEG–fNIRS as a brain switch has 
also been reported for tetraplegia patients (see the “EEG + NIRS” 
section for details). Blokland et al. (2014) decoded two “yes/no” 
responses from tetraplegia patients. Although the command 
generation time was slow, this study showed the significance of 
using hybrid EEG–NIRS for patients. Hybrid SSVEP–P300-based 
paradigms for the investigation of consciousness disorder in 
patients have been reported (see the “SSVEP and P300” section 
for details). Also, gaze-independent hBCI using visual and audi-
tory stimuli with P300-based tasks has been proposed for LIS 
patients (Barbosa et al., 2016).

Table 5 | Important passive hybrid brain–computer interface studies for drowsiness detection (from 2010 to 2016).
Reference
Brain area 
Modality
Application
Analysis 
type
Classifier
Commands
Accuracy 
(%)
Window 
size (s)
Khushaba  
et al. (2011)
Frontal and 
occipital
Electroencephalography 
(EEG) + electrooculography 
(EOG) + ECG
Driver drowsiness 
detection
Online
Linear discriminant analysis 
(LDA), support vector 
machine (SVM), K-nearest 
neighbor, and kernel SVM
1
95−97
10
Chen  
et al. (2015)
Frontal and 
occipital
EEG + EOG
Automatic detection of 
drowsiness
Online
ELM
2 (single 
command for 
drowsiness)
97.3
8
Ahn  
et al. (2016)
Whole brain
EEG + NIRS
Mental fatigue level 
estimation
Online
LDA
1
75.9
60
18
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
Motor Therapy and Recovery
The monitoring of the brain state during brain stimulation is an 
important application of hBCI systems. Transcranial magnetic 
stimulation and transcranial direct current stimulation (tDCS) 
are used to stimulate the brain for therapy. The electrical brain 
activity for motor recovery estimation was monitored using EEG 
(Zaghi et  al., 2010; Schestatsky et  al., 2013; Sale et  al., 2015). 
Also, the hemodynamic response was monitored using fNIRS 
(Faress and Chau, 2013; Khan et al., 2013; Ishikuro et al., 2014). 
Combined EEG–fNIRS provides an edge over the individual 
modalities in that electrical and hemodynamic responses can be 
monitored simultaneously (Dutta, 2015; Dutta et al., 2015; Jindal 
et  al., 2015). This application, certainly, can facilitate medical 
diagnoses for the purposes of motor therapy and recovery. A lot 
of research has been carried out in this area for stroke patients. 
The most recent work in this context has used EEG–NIRS joint 
imaging for the measurement of the brain recovery of stroke 
patients after tDCS stimulation (Das et al., 2016; Guhathakurta 
and Dutta, 2016; Sood et al., 2016).
Infants Brain Monitoring
The monitoring of brain development is essential for infants. It 
helps in avoiding several brain disorders in developing children. 
Although, a single brain imaging technique may help to monitor 
autism spectrum disorder, attention-deficit hyper-activity dis-
order, and speech and language impairments (Aslin et al., 2015; 
Sperdin and Schaer, 2016), hybrid systems may provide a better 
diagnosis for such disorders. Also, the brain development of 
neonates can be better understood by simultaneously measuring 
neuronal and hemodynamic brain activities.
Hybrid BCI for Healthy Individuals
As per the above discussion, it seems that hBCI/BCI is more suited 
to patients; however, most studies have used healthy subjects for 
experimentation in a lab environment. This might be due to the 
fact that hBCI is still in its developmental phase. However, in our 
opinion, hBCI has several aspects that are most suited to healthy 
people. The following are the three major applications of hBCI.
Control Applications
The hBCI can be useful in environment control settings for 
healthy individuals. Environment control is very helpful for 
those who need to do multiple tasks utilizing several devices 
(e.g., remote control and light control). Using brain signals, a 
person can perform these tasks remotely, for which operations, 
high accuracy is required; thus, in such scenarios, hBCIs can be 
effective. Also, using hBCI schemes, a robot can be controlled 
remotely to perform several tasks. For amputees, an hBCI, 
relative to a single modality, can be a more effective and reliable 
communication tool for the control of prosthetic devices, as it 
can achieve higher accuracy. For example, Hwang et al. (2012) 
developed a mental spelling system based on SSVEP, adopting 
a QWERTY style layout keyboard with 30 LEDs flickering with 
different frequencies. The mental spelling system allows the users 
to spell one target character per each target selection. A total of 
87.58% accurate results were achieved by their study.
Entertainment
Recently, BCIs also have been employed for healthy individuals’ 
entertainment purposes (Ahn et al., 2014; Bai et al., 2015; Li et al., 
2016), though this is not the main priority of BCI research. In 
any case, the feasibility of brain-controlled video games has been 
demonstrated using EEG-BCI; however, no actual hBCI applica-
tion has been introduced to date yet. In any event, it should be 
emphasized that for training purposes, such games might be 
useful in generating desired brain activities that can be decoded 
using hBCI modalities.
Safety
Perhaps hBCI’s main application is safety. Indeed, first and 
foremost, it can be useful in monitoring the vigilance levels of 
pilots and drivers. For a pilot confronting an emergency landing, 
the monitoring of the exact mental status of the pilot can con-
tribute to a safe landing. Although commercial systems that can 
monitor brain activity and alert drowsy drivers do not yet exist, 
hBCI might nonetheless contribute to the development of such a 
commercial system. In the case of tele-operated robots, hBCI can 
be very effective in monitoring the anxiety levels of doctors. This 
could be a useful approach, especially for complicated surgeries.
Neuro-ergonomics
Neuro-ergonomics is the study of human brain in relation to per-
formance at work and everyday setting. EEG is most widely used 
in measuring the passive brain states (Qian et al., 2016, 2017). 
Most recently, fNIRS has also proven to be a viable candidate for 
passive brain activities detection (Ayaz et al., 2012, 2013; Khan and 
Hong, 2015). Hybrid BCI systems may give better information 

Figure 8 | Hybrid brain–computer interface paradigms combining different 
brain signals (2009–2016).
Figure 7 | Hybrid brain–computer interface using electroencephalography 
(EEG) in combination with other modalities (2009–2016).
Figure 6 | Trend in electroencephalography (EEG)/functional near infrared 
spectroscopy (fNIRS)-based hybrid brain–computer interface (BCI).
19
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
about the physical fatigue, cognitive functions, mental workload, 
vigilance, and mental fatigue of a person. This can be helpful to 
the person to avoid extreme workloads and loss of vigilance.
FUTURE PERSPECTIVES
The research on hBCI has begun to increase in recent years. 
Although the hBCI scheme emerged before 2010, a major accel-
eration in the derivation of developmental strategies has been 
observed only in the previous 2 years. Most hybridization strate-
gies that have been introduced are applicable to EEG-based BCI; 
yet, further improvement of fNIRS-based BCI systems is needed. 
Figure 6 shows the recent trend in EEG- and fNIRS-based hBCIs.
The major hBCI emphasis is the EEG–EOG-based hBCI. Most 
of these studies have combined, or are combining, two modalities 
for eye movement artifact removal and additional BCI commands. 
EEG–EMG-based hBCIs have limited applications and are used 
only in muscular-artifact removal from brain data for enhanced 
classification accuracy. Meanwhile, only very limited research has 
been done on EEG–fNIRS-based BCI applications. Moreover, the 
works done have focused mostly on an improvement of classifica-
tion accuracy, with very little attention having been paid to the 
issue of command-number increase. A breakdown of the hBCI 
application approaches introduced from 2009 to 2016 is provided 
in Figure 7.
Most of the work on brain activity combination hBCIs has 
been based on SSVEP- and P300-based paradigms. Although 
both are reactive tasks, the most widely observed applications 
have been in the area of speller and wheelchair control. In relation 
to the combination of MI with P300 or SSVEP, the applications 
are widely used in neuro-rehabilitation and control settings. Only 
a very small portion of hBCI research has targeted prefrontal 
and motor-based hBCI. This strategy is useful in increasing 
the number of commands for both fNIRS alone and combined 
EEG–fNIRS. A breakdown of the paradigms employed between 
2009 and 2016 is shown in Figure 8.
The hBCI can enhance the classification accuracy and increase 
the number of commands of a BCI system without influencing 
either of those two factors. The trend in hBCI (see Figure  6) 
suggests the high potential of research in this field. Although 
the early BCI (i.e., single modality) problems were dealt with by 
combining modalities, there are still several research issues that 
remain untouched.
Although window smoothing techniques are available in 
literature (Qi et al., 2012), one of the most important questions in 
the development of hBCIs is the selection of window size. Several 
researchers have worked on the problem of an optimal window 
size for BCI; however, the literature still lacks any conclusive work 
on standardized window selection for simultaneous decoding of 
brain activates. In hybrid systems, different windows that were 
optimized for individual modalities are naturally used for feature 
extraction (Ma et al., 2015; Buccino et al., 2016; Khan and Hong, 
2017). This will result in a delay in making a final decision until 
the data from a bigger window are processed. Therefore, a new 
decision making scheme suitable for hybrid systems needs to be 
developed. To the best of the authors’ knowledge, an algorithm 
that can simultaneously extract/classify features even for simple 
EEG–fNIRS dual modalities applied to the same brain area has 
not been developed yet. Especially, in the case of combined EEG–
fNIRS, the reported optimal window size is 10 s (Tomita et al., 
2014), which might not be appropriate for the control of external 
devices. Further improvement should be achieved, for example, 
by using initial dip detection (Jasdzewski et al., 2003; Yoshino 
and Kato, 2012; Hong and Naseer, 2016) instead of relying on the 
hemodynamic response of fNIRS together with EEG signals in 
the reduction of window size. For this particular purpose, a recent 
study has shown the feasibility of initial dip detection for applica-
tion to BCI (Hong and Naseer, 2016). In terms of classification, 
two studies (Khan and Hong, 2017; Zafar and Hong, 2017) have 

Figure 9 | The proposed hybrid electroencephalography (EEG)–NIRS using hemodynamic and initial dip features for simultaneous activity detection and 
classification.
20
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
reported the classification of prefrontal fNIRS signals within a 2 s 
window. However, in those studies, the EEG and fNIRS signals 
were not simultaneously decoded for a single task but recorded 
from two different tasks. A significant amount of research is 
needed to decode EEG–fNIRS signals simultaneously for 
enhanced accuracy without influencing the EEG signal detection 
time. Developments in this area can produce fruitful results by 
which the hybrid window size can be reduced (less than 1 s). The 
use of a fast optical response (Hu et al., 2011), furthermore, also 
could help to reduce the window size. Perhaps the use of multi-
wavelength system (Bhutta et al., 2014) combined with adaptive 
signal processing algorithms (Hu et al., 2010, 2013; Santosa et al., 
2013; Ren et al., 2014; Zhang et al., 2016b; Zhou et al., 2016) will 
significantly contribute to the eventual reduction of the inherent 
delay in the hemodynamic response. Figure 9 shows the proposed 
hybrid EEG–fNIRS model for window reduction.
Another important aspect that requires a focus with respect 
to hBCI is the selection of active control commands. The reactive 
commands can be increased by changing the flickering stimuli 
for BCI. In fact, using reactive tasks, more than 50 commands 
can be achieved (see Table 4). A BCI using active commands 
is more desirable than one based on reactive commands. After, 
at most, three or four active commands, the accuracy severely 
drops, making it difficult to control an external device with a 
further increased number of commands. The current need is 
such strategies that can be used to achieve active control of BCI 
systems without impacting negatively on accuracy. In this regard, 
the hBCI can play an important role. Future research in this area 
will provide a solution to the problems related to the increase in 
the number of active commands.
Besides the issues of the number of commands, classification 
accuracy, and detection time, the following challenging issues 
need to be investigated: (i) how to predict the desired feature from 
a slow-modality signal in synchronizing the classification time to 
a fast-modality signal, (ii) development of a general meta-feature 
model covering the multiple modalities considered, (iii) devel-
opment of multiple interactive models switching based on their 
computed probabilities, (iv) optimization of a brain region for 
hybrid modalities, (v) optimization of the number of sensors (i.e., 
electrodes and optodes) needed for BCI, (vii) finding of the best 
combination of local brain regions for hybrid imaging, (viii) how 
to synchronize brain and non-brain signals if the hybridization is 
extended beyond the brain, (ix) how to fuse multiple information 
to single out one definitive decision, and (x) how to deliver the 
information obtained from one modality to others.
The current need is the development of a portable, wearable, 
and low-cost hBCI system that can be used for both healthy 
persons and patients. Furthermore, motion artifacts should 
be minimized, and there should be the capacity to enhance 
accuracy and increase the number of commands as needed. 
Moreover, the hBCI should be designed from the application 
point of view. Currently, however, no such hBCI systems are 
commercially available. If such system exists, its combination 
with a haptic device (Nam et al., 2014, 2015) may provide bet-
ter assistance to patients in movement and sensing. Whereas 
EMG/EOG combined with EEG can be used for control 
applications (e.g., wheelchair control), the most significant 
breakthrough in hBCI is the design of hybrid EEG–NIRS that 
can simultaneously decode electrical and hemodynamic brain 
activities. Considering the fact that fMRI has high spatial but 
low temporal resolution, further research in hybrid EEG–NIRS 
might be a more promising brain-diagnostic endeavor. In the 
near future, this can be made possible with a breakthrough by 
combining real-time EEG rhythmic cortical activity monitoring 

21
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
(Im et  al., 2007) with fNIRS directional coupling estimation 
(Im et al., 2010) and bundled optodes based 3D imaging tech-
niques (Nguyen and Hong, 2016; Nguyen et  al., 2016). Such 
advances, enabling the utilization of non-invasive methods, will 
allow for a much better understanding of the brain.
CONCLUSION
In this article, we have reviewed the state-of-the-art research 
on hBCI technologies. We have discussed the hardware and 
methodologies adopted by researchers for the development of 
the pertinent hBCI systems. The most recent work related to the 
hardware combinations and strategies adopted for several brain 
signal acquisition modalities have been discussed as well.
The issue of hBCI hardware is addressed in light of the employed 
combinations of EEG with fNIRS, EOG, and EMG. EEG and 
fNIRS are combined to enhance classification accuracy and to 
increase the number of control commands for BCI systems. The 
brain activity features are combined and simultaneously decoded 
to improve the BCI performance. The combination of EEG with 
EOG has a similar end, EOG being used to increase the number 
of commands or to remove motion artifacts for an improved 
accuracy. EMG, meanwhile, is used to remove motion artifacts 
and, thereby, improve the classification accuracy.
Multi-modality improves classification accuracy and increases 
the number of control commands: the number of commands can 
be increased by simultaneously decoding the brain activities in 
hybrid paradigms. In this case, we have discussed the increase 
in the number of commands using steady-state visual evoked 
potentials (SSVEP) and ERP. Also, the combination of motor and 
prefrontal tasks for the development of hBCI paradigms has been 
discussed.
Although the hBCI issues span both the increase in the 
number of active commands and the improvement in classifica-
tion accuracy, some additional concerns remain: the selection 
of optimal features and windows for activity detection, for 
example, is still relatively neglected. In any case, it is clear that 
there is much room for future hBCI research, particularly, in its 
applications. The field is still young. For example, there is as yet 
no commercially available hBCI system, notwithstanding the 
several communication and control strategies that have already 
been introduced. Doubtless several control and rehabilitation 
application breakthroughs are at hand.
AUTHOR CONTRIBUTIONS
KSH conceived the topic. MJK conducted the literature survey 
and wrote a preliminary version. KSH finalized the paper.
FUNDING
This work was supported by the National Research Foundation 
of Korea under the Ministry of Science, ICT and Future Plan­
ning, Korea (grant no. NRF-2014 -R1A2A1A10049727).
REFERENCES
Ahn, M., and Jun, S. C. (2015). Performance variation in motor imagery 
brain–computer interface: a brief review. J. Neurosci. Methods 243, 103–110. 
doi:10.1016/j.jneumeth.2015.01.033 
Ahn, M., Lee, M., Choi, J., and Jun, S. C. (2014). A review of brain–computer 
interface games and an opinion survey from researchers, developers and users. 
Sensors (Basel) 14, 14601–14633. doi:10.3390/s140814601 
Ahn, S., Nguyen, T., Jang, H., Kim, J. G., and Jun, S. C. (2016). Exploring neuro- 
physiological correlates of drivers’ mental fatigue caused by sleep deprivation 
using simultaneous EEG, ECG, and fNIRS data. Front. Hum. Neurosci. 10:219. 
doi:10.3389/fnhum.2016.00219 
Akerstedt, T., Hallvig, D., Anund, A., Fors, C., Schwarz, J., and Kecklund, G. 
(2013). Having to stop driving at night because of dangerous sleepiness – 
awareness, physiology and behaviour. J. Sleep Res. 22, 380–388. doi:10.1111/
jsr.12042 
Allison, B. Z., Brunner, C., Kaiser, V., Muller-Putz, G. R., Neuper, C., and 
Pfurtscheller, G. (2010). Toward a hybrid brain–computer interface based 
on imagined movement and visual attention. J. Neural Eng. 7, 026007. 
doi:10.1088/1741-2560/7/2/026007 
Allison, B. Z., Jin, J., Zhang, Y., and Wang, X. Y. (2014). A four-choice hybrid P300/
SSVEP BCI for improved accuracy. Brain Comput. Interfaces 1, 17–26. doi:10.1
080/2326263X.2013.869003 
An, X. W., Hohne, J., Ming, D., and Blankertz, B. (2014). Exploring combinations 
of auditory and visual stimuli for gaze-independent brain–computer interfaces. 
PLoS ONE 9:e0157284. doi:10.1371/journal.pone.0157284 
Aslin, R. N., Shukla, M., and Emberson, L. L. (2015). Hemodynamic correlates 
of cognition in human infants. Annu. Rev. Psychol. 66, 349–379. doi:10.1146/
annurev-psych-010213-115108 
Ayaz, H., Onarai, B., Izzetoglu, K., Shewokis, P. A., McKendrick, R., and 
Parasuraman, R. (2013). Continuous monitoring of brain dynamics with 
functional near infrared spectroscopy as a tool for neuroergonomic research: 
empirical examples and a technological development. Front. Hum. Neurosci. 
7:871. doi:10.3389/fnhum.2013.00871 
Ayaz, H., Shewokis, P. A., Bunce, S., Izzetoglu, K., Willems, B., and Onari, B. 
(2012). Optical brain monitoring for operator training and mental workload 
assessment. Neuroimage 59, 36–47. doi:10.1016/j.neuroimage.2011.06.023 
Aziz, F., Arof, H., Mokhtar, N., and Mubin, M. (2014). HMM based automated 
wheelchair navigation using EOG traces in EEG. J. Neural Eng. 11, 056018. 
doi:10.1088/1741-2560/11/5/056018 
Bai, L. J., Yu, T. Y., and Li, Y. Q. (2015). A brain computer interface-based explorer. 
J. Neurosci. Methods 244, 2–7. doi:10.1016/j.jneumeth.2014.06.015 
Bai, O., Rathi, V., Lin, P., Huang, D. D., Battapady, H., Fei, D. Y., et al. (2011). 
Prediction of human voluntary movement before it occurs. Clin. Neurophysiol. 
122, 364–372. doi:10.1016/j.clinph.2010.07.010 
Bai, Y., Wan, X., Zeng, K., Ni, Y., Qiu, L., and Li, X. (2016). Reduction 
hybrid artifacts of EMG–EOG in electroencephalography evoked by 
prefrontal transcranial magnetic stimulation. J. Neural Eng. 13, 066016. 
doi:10.1088/1741-2560/13/6/066016 
Banville, H., and Falk, T. H. (2016). Recent advances and open challenges in hybrid 
brain–computer interfacing: a technological review of non-invasive human 
research. Brain Comput. Interfaces 3, 9–46. doi:10.1080/2326263X.2015.1134958 
Barbosa, S., Pires, G., and Nunes, U. (2016). Toward a reliable gaze-independent 
hybrid BCI combining visual and natural auditory stimuli. J. Neurosci. Methods 
261, 47–61. doi:10.1016/j.jneumeth.2015.11.026 
Bashashati, A., Nouredin, B., Ward, R. K., Lawrence, P., and Birch, G. E. (2007). 
Effect of eye-blinks on a self-paced brain interface design. Clin. Neurophysiol. 
118, 1639–1647. doi:10.1016/j.clinph.2007.03.020 
Bayliss, J. D., Inverso, S. A., and Tentler, A. (2004). Changing the P300 brain com-
puter interface. Cyberpsychol. Behav. 7, 694–704. doi:10.1089/cpb.2004.7.694 
Belkacem, A. N., Saetia, S., Zintus-Art, K., Shin, D., Kambara, H., Yoshimura, N., 
et al. (2015a). Real-time control of a video game using eye movements and 
two temporal EEG sensors. Comput. Intell. Neurosci. 2015, 653639. doi:10.1155/ 
2015/653639 
Belkacem, A. N., Shin, D., Kambara, H., Yoshimura, N., and Koike, Y. (2015b). 
Online classification algorithm for eye-movement-based communication 
systems using two temporal EEG sensors. Biomed. Signal Process. Control 16, 
40–47. doi:10.1016/j.bspc.2014.10.005 

22
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
Bhattacharyya, S., Biswas, A., Mukherjee, J., Majumdar, A. K., Majumdar, B., 
Mukherjee, S., et al. (2013). Detection of artifacts from high energy bursts in 
neonatal EEG. Comput. Biol. Med. 43, 1804–1814. doi:10.1016/j.compbiomed. 
2013.07.031 
Bhattacharyya, S., Konar, A., and Tibarewala, D. N. (2014). Motor imagery, P300 and 
error-related EEG-based robot arm movement control for rehabilitation pur-
pose. Med. Biol. Eng. Comput. 52, 1007–1017. doi:10.1007/s11517-014-1204-4 
Bhutta, M. R., Hong, K.-S., Kim, B. M., Hong, M. J., Kim, Y. H., and Lee, S. H. 
(2014). Note: three wavelengths near-infrared spectroscopy system for 
compensating the light absorbance by water. Rev. Sci. Instrum. 85, 026111. 
doi:10.1063/1.4865124 
Bhutta, M. R., Hong, M. J., Kim, Y.-H., and Hong, K.-S. (2015). Single-trial lie 
detection using a combined fNIRS-polygraph system. Front. Psychol. 6:709. 
doi:10.3389/fpsyg.2015.00709 
Bi, L., Fan, X.-A., and Liu, Y. (2013). EEG-based brain-controlled mobile 
robots: a survey. IEEE Trans. Hum. Mach. Syst. 43, 161–176. doi:10.1109/
TSMCC.2012.2219046 
Bi, L. Z., Lian, J. L., Jie, K., Lai, R., and Liu, Y. L. (2014). A speed and direction-based 
cursor control system with P300 and SSVEP. Biomed. Signal Process. Control 14, 
126–133. doi:10.1016/j.bspc.2014.07.009 
Blokland, Y., Spyrou, L., Thijssen, D., Eijsvogels, T., Colier, W., Floor-Westerdijk, M., 
et al. (2014). Combined EEG-fNIRS decoding of motor attempt and imagery for 
brain switch control: an offline study in patients with tetraplegia. IEEE Trans. 
Neural Syst. Rehabil. Eng. 22, 222–229. doi:10.1109/TNSRE.2013.2292995 
Boas, D. A., Brooks, D. H., Miller, E. L., DiMarzio, C. A., Kilmer, M., Gaudette, R. 
J., et al. (2001). Imaging the body with diffuse optical tomography. IEEE Signal 
Process. Mag. 18, 57–75. doi:10.1109/79.962278 
Boas, D. A., Elwell, C. E., Ferrari, M., and Taga, G. (2014). Twenty years of functional 
near-infrared spectroscopy: introduction for the special issue. Neuroimage 85, 
1–5. doi:10.1016/j.neuroimage.2013.11.033 
Boas, D. A., Oleary, M. A., Chance, B., and Yodh, A. G. (1994). Scattering of dif-
fuse photon density waves by spherical inhomogeneities within turbid media: 
anaytic solution and applications. Proc. Natl. Acad. Sci. U.S.A. 91, 4887–4891. 
doi:10.1073/pnas.91.11.4887 
Breitwieser, C., Pokorny, C., and Muller-Putz, G. R. (2016). A hybrid three-class 
brain–computer interface system utilizing SSSEPs and transient ERPs. J. Neural 
Eng. 13, 066015. doi:10.1088/1741-2560/13/6/066015 
Brumberg, J. S., Nieto-Castanon, A., Kennedy, P. R., and Guenther, F. H. (2010). 
Brain–computer interfaces for speech communication. Speech Commun. 52, 
367–379. doi:10.1016/j.specom.2010.01.001 
Buccino, A. P., Keles, H. O., and Omurtag, A. (2016). Hybrid EEG-fNIRS 
asynchronous brain–computer interface for multiple motor tasks. PLoS ONE 
11:e0146610. doi:10.1371/journal.pone.0146610 
Bulling, A., Ward, J. A., Gellersen, H., and Troester, G. (2011). Eye movement 
analysis for activity recognition using electrooculography. IEEE Trans. Pattern 
Anal. Mach. Intell. 33, 741–753. doi:10.1109/TPAMI.2010.86 
Cao, L., Li, J., Ji, H. F., and Jiang, C. J. (2014). A hybrid brain computer interface 
system based on the neurophysiological protocol and brain-actuated switch 
for wheelchair control. J. Neurosci. Methods 229, 33–43. doi:10.1016/j.
jneumeth.2014.03.011 
Cao, L., Li, J., Xu, Y. F., Zhu, H. P., and Jiang, C. J. (2016). A hybrid vigilance 
monitoring study for mental fatigue and its neural activities. Cogn. Comput. 8, 
228–236. doi:10.1007/s12559-015-9351-y 
Chadwell, A., Kenney, L., Thies, S., Galpin, A., and Head, J. (2016). The reality of 
myoelectric prostheses: understanding what makes these devices difficult for 
some users to control. Front. Neurorobot. 10:7. doi:10.3389/fnbot.2016.00007 
Chang, M. H., Lee, J. S., Heo, J., and Park, K. S. (2016). Eliciting dual-frequency 
SSVEP using a hybrid SSVEP-P300 BCI. J. Neurosci. Methods 258, 104–113. 
doi:10.1016/j.jneumeth.2015.11.001 
Chen, B. J., Feng, Y. G., and Wang, Q. N. (2016). Combining vibrotactile feedback 
with volitional myoelectric control for robotic transtibial prostheses. Front. 
Neurorobot. 10:8. doi:10.3389/fnbot.2016.00008 
Chen, L. L., Zhao, Y., Zhang, J., and Zou, J. Z. (2015). Automatic detection of 
alertness/drowsiness from physiological signals using wavelet-based nonlinear 
features and machine learning. Expert Syst. Appl. 42, 7344–7355. doi:10.1016/j.
eswa.2015.05.028 
Cheron, G., Duvinage, M., De Saedeleer, C., Castermans, T., Bengoetxea, A., 
Petieau, M., et al. (2012). From spinal central pattern generators to cortical 
network: integrated BCI for walking rehabilitation. Neural. Plast. 2012, 375148. 
doi:10.1155/2012/375148 
Choi, B. J., and Jo, S. H. (2013). A low-cost EEG system-based hybrid brain– 
computer interface for humanoid robot navigation and recognition. PLoS 
ONE 8:e74583. doi:10.1371/journal.pone.0074583 
Chowdhury, R. H., Reaz, M. B. I., Ali, M. A., Bakar, A. A., Chellappan, K., and 
Chang, T. G. (2013). Surface electromyography signal processing and classifi-
cation techniques. Sensors (Basel) 13, 12431–12466. doi:10.3390/s130912431 
Cler, M. J., and Stepp, C. E. (2015). Discrete versus continuous mapping of facial 
electromyography for human-machine interface control: performance and 
training effects. IEEE Trans. Neural Syst. Rehabil. Eng. 23, 572–580. doi:10.1109/
TNSRE.2015.2391054 
Combaz, A., and Van Hulle, M. M. (2015). Simultaneous detection of P300 and 
steady-state visually evoked potentials for hybrid brain–computer interface. 
PLoS ONE 10:e0121481. doi:10.1371/journal.pone.0121481 
Costa, A., Hortal, E., Ianez, E., and Azorin, J. M. (2014). A supplementary system 
for a brain–machine interface based on jaw artifacts for the bidimensional con-
trol of a robotic arm. PLoS ONE 9:e112352. doi:10.1371/journal.pone.0112352 
Daly, I., Billinger, M., Laparra-Hernandez, J., Aloise, F., Garcia, M. L., Faller, J., 
et al. (2013). On the control of brain–computer interfaces by users with cerebral 
palsy. Clin. Neurophysiol. 124, 1787–1797. doi:10.1016/j.clinph.2013.02.118 
Daly, I., Scherer, R., Billinger, M., and Muller-Putz, G. (2015). FORCe: fully online 
and automated artifact removal for brain–computer interfacing. IEEE Trans. 
Neural Syst. Rehabil. Eng. 23, 725–736. doi:10.1109/TNSRE.2014.2346621 
Das, A., Guhathakurta, D., Sengupta, R., and Dutta, A. (2016). EEG-NIRS 
joint-imaging based assessment of neurovascular coupling in stroke: a novel 
technique for brain monitoring. Int. J. Stroke 11, 271–272. 
Demandt, E., Mehring, C., Vogt, K., Schulze-Bonhage, A., Aertsen, A., and Ball, T. 
(2012). Reaching movement onset- and end-related characteristics of EEG spec-
tral power modulations. Front. Neurosci. 6:65. doi:10.3389/fnins.2012.00065 
Dorokhov, V. B. (2003). Alpha bursts and K-complex: phasic activation pattern 
during spontaneous recovery of correct psychomotor performance at different 
stages of drowsiness. Zhurnal Vyss. Nervn. Deyatelnosti Im. I P Pavlov. 53, 
503–512. 
Duan, F., Lin, D. X., Li, W. Y., and Zhang, Z. (2015). Design of a multimodal EEG-
based hybrid BCI system with visual servo module. IEEE Trans. Auton. Ment. 
Dev. 7, 332–341. doi:10.1109/TAMD.2015.2434951 
Duta, M., Alford, C., Wilson, S., and Tarassenko, L. (2004). Neural network anal-
ysis of the mastoid EEG for the assessment of vigilance. Int. J. Hum. Comput. 
Interact. 17, 171–195. doi:10.1207/s15327590ijhc1702_4 
Dutta, A. (2015). Bidirectional interactions between neuronal and hemodynamic 
responses to transcranial direct current stimulation (tDCS): challenges 
for brain-state dependent tDCS. Front. Syst. Neurosci. 9:107. doi:10.3389/
fnsys.2015.00107 
Dutta, A., Jacob, A., Chowdhury, S. R., Das, A., and Nitsche, M. A. (2015). EEG-
NIRS based assessment of neurovascular coupling during anodal transcranial 
direct current stimulation – a stroke case series. J. Med. Syst. 39, 36. doi:10.1007/
s10916-015-0205-7 
Dyson, M., Sepulveda, F., and Gan, J. Q. (2010). Localisation of cognitive tasks 
used in EEG-based BCIs. Clin. Neurophysiol. 121, 1481–1493. doi:10.1016/j.
clinph.2010.03.011 
Fan, X. A., Bi, L. Z., Teng, T., Ding, H. S., and Liu, Y. L. (2015). A brain– 
computer interface-based vehicle destination selection system using P300 
and SSVEP signals. IEEE Trans. Intell. Transp. Syst. 16, 274–283. doi:10.1109/
TITS.2014.2330000 
Faress, A., and Chau, T. (2013). Towards a multimodal brain–computer interface: 
combining fNIRS and fTCD measurements to enable higher classification 
accuracy. Neuroimage 77, 186–194. doi:10.1016/j.neuroimage.2013.03.028 
Fatourechi, M., Bashashati, A., Ward, R. K., and Birch, G. E. (2007). EMG and EOG 
artifacts in brain computer interface systems: a survey. Clin. Neurophysiol. 118, 
480–494. doi:10.1016/j.clinph.2006.10.019 
Fazli, S., Mehnert, J., Steinbrink, J., Curio, G., Villringer, A., Muller, K. R., et al. 
(2012). Enhanced performance by a hybrid NIRS-EEG brain computer inter-
face. Neuroimage 59, 519–529. doi:10.1016/j.neuroimage.2011.07.084 
Fels, M., Bauer, R., and Gharabaghi, A. (2015). Predicting workload profiles of 
brain–robot interface and electromygraphic neurofeedback with cortical 
resting-state networks: personal trait or task-specific challenge? J. Neural Eng. 
12, 046029. doi:10.1088/1741-2560/12/4/046029 

23
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
Foldes, S. T., and Taylor, D. M. (2010). Discreet discrete commands for assistive 
and neuroprosthetic devices. IEEE Trans. Neural Syst. Rehabil. Eng. 18, 236–244. 
doi:10.1109/TNSRE.2009.2033428 
Gharagozlou, F., Saraji, G. N., Mazloumi, A., Nahvi, A., Nasrabadi, A. M., 
Foroushani, A. R., et  al. (2015). Detecting driver mental fatigue based on 
EEG alpha power changes during simulated driving. Iran J. Public Health 44, 
1693–1700. 
Gomez-Gil, J., San-Jose-Gonzalez, I., Nicolas-Alonso, L. F., and Alonso-Garcia, S.  
(2011). Steering a tractor by means of an EMG-based human-machine inter-
face. Sensors 11, 7110–7126. doi:10.3390/s110707110 
Gruzelier, J. H. (2014). EEG-neurofeedback for optimising performance. I: 
A review of cognitive and affective outcome in healthy participants. Neurosci. 
Biobehav. Rev. 44, 124–141. doi:10.1016/j.neubiorev.2013.09.015 
Guhathakurta, D., and Dutta, A. (2016). Computational pipeline for NIRS-EEG 
joint imaging of tDCS-evoked cerebral responses an application in ischemic 
stroke. Front. Neurosci. 10:261. doi:10.3389/fnins.2016.00261 
Hong, K.-S., and Naseer, N. (2016). Reduction of delay in detecting initial dips 
from functional near-infrared spectroscopy signals using vector-based phase 
analysis. Int. J. Neural Syst. 26, 1650012. doi:10.1142/S012906571650012X 
Hong, K.-S., Naseer, N., and Kim, Y. H. (2015). Classification of prefrontal and 
motor cortex signals for three-class fNIRS-BCI. Neurosci. Lett. 587, 87–92. 
doi:10.1016/j.neulet.2014.12.029 
Hong, K.-S., and Nguyen, H.-D. (2014). State-space models of impulse hemody-
namic responses over motor, somatosensory, and visual cortices. Biomed. Opt. 
Express 5, 1778–1798. doi:10.1364/BOE.5.001778 
Hong, K.-S., and Santosa, H. (2016). Decoding four different sound-categories in 
the auditory cortex using functional near-infrared spectroscopy. Hear. Res. 333, 
157–166. doi:10.1016/j.heares.2016.01.009 
Horki, P., Solis-Escalante, T., Neuper, C., and Muller-Putz, G. (2011). Combined 
motor imagery and SSVEP based BCI control of a 2 DoF artificial upper limb. 
Med. Biol. Eng. Comput. 49, 567–577. doi:10.1007/s11517-011-0750-2 
Hortal, E., Ianez, E., Ubeda, A., Perez-Vidal, C., and Azorin, J. M. (2015). 
Combining a brain–machine interface and an electrooculography interface 
to perform pick and place tasks with a robotic arm. Robot. Auton. Syst. 72, 
181–188. doi:10.1016/j.robot.2015.05.010 
Hsu, W. Y. (2013a). Application of quantum-behaved particle swarm optimi-
zation to motor Imagery EEG classification. Int. J. Neural Syst. 23, 1350026. 
doi:10.1142/S0129065713500263 
Hsu, W. Y. (2013b). Independent component analysis and multiresolution asym-
metry ratio for brain–computer interface. Clin. EEG Neurosci. 44, 105–111. 
doi:10.1177/1550059412463660 
Hsu, W. Y., Lin, C. H., Hsu, H. J., Chen, P. H., and Chen, I. R. (2012). Wavelet-
based envelope features with automatic EOG artifact removal: application 
to single-trial EEG data. Expert Syst. Appl. 39, 2743–2749. doi:10.1016/j.
eswa.2011.08.132 
Hu, X.-S., Hong, K.-S., and Ge, S. S. (2011). Recognition of stimulus-evoked neu-
ronal optical response by identifying chaos levels of near-infrared spectroscopy 
time series. Neurosci. Lett. 504, 115–120. doi:10.1016/j.neulet.2011.09.011 
Hu, X.-S., Hong, K.-S., and Ge, S. S. (2012). fNIRS-based online deception decod-
ing. J. Neural Eng. 9, 026012. doi:10.1088/1741-2560/9/2/026012 
Hu, X.-S., Hong, K.-S., and Ge, S. S. (2013). Reduction of trial-to-trial variability 
in functional near-infrared spectroscopy signals by accounting for resting- 
state functional connectivity. J. Biomed. Opt. 18, 017003. doi:10.1117/1.JBO. 
18.1.017003 
Hu, X.-S., Hong, K.-S., Ge, S. S., and Jeong, M.-Y. (2010). Kalman estimator- and 
general liner model-based on-line brain activation mapping by near-infrared 
spectroscopy. Biomed. Eng. Online 9, 82. doi:10.1186/1475-925X-9-82 
Huppert, T. J., Diamond, S. G., Franceschini, M. A., and Boas, D. A. (2009). HomER: 
a review of time-series analysis methods for near-infrared spectroscopy of the 
brain. Appl. Opt. 48, D280–D298. doi:10.1364/AO.48.00D280 
Huppert, T. J., Schmidt, B., Beluk, N., Furman, J., and Sparto, P. (2013). Measurement 
of brain activation during an upright stepping reaction task using functional 
near-infrared spectroscopy. Hum. Brain Mapp. 34, 2817–2828. doi:10.1002/
hbm.22106 
Hwang, H.-J., Kim, S., Choi, S., and Im, C.-H. (2013). EEG-based brain–computer 
interfaces: a thorough literature survey. Int. J. Hum. Comput. Interact. 29, 
814–826. doi:10.1080/10447318.2013.780869 
Hwang, H. J., Lim, J. H., Jung, Y. J., Choi, H., Lee, S. W., and Im, C.-H. 
(2012). Development of an SSVEP-based BCI spelling system adopting a 
QWERTY-style LED keyboard. J. Neurosci. Methods 208, 59–65. doi:10.1016/j.
jneumeth.2012.04.011 
Im, C.-H., Hwang, H.-J., Che, H., and Lee, S. (2007). An EEG-based real-time 
cortical rhythmic activity monitoring system. Physiol. Meas. 28, 1101–1113. 
doi:10.1088/0967-3334/28/9/011 
Im, C.-H., Jung, Y.-J., Lee, S., Koh, D., Kim, D.-W., and Kim, B.-M. (2010). 
Estimation of directional coupling between cortical areas using near-infrared 
spectroscopy (NIRS). Opt. Express 18, 5730–5739. doi:10.1364/OE.18.005730 
Ishikuro, K., Urakawa, S., Takamoto, K., Ishikawa, A., Ono, T., and Nishijo, H. 
(2014). Cerebral functional imaging using near-infrared spectroscopy during 
repeated performances of motor rehabilitation tasks tested on healthy subjects. 
Front. Hum. Neurosci. 8:292. doi:10.3389/fnhum.2014.00292 
Jasdzewski, G., Strangman, G., Wagner, J., Kwong, K. K., Poldrack, R. A., and 
Boas, D. A. (2003). Differences in the hemodynamic response to event-related 
motor and visual paradigms as measured by near-infrared spectroscopy. 
Neuroimage 20, 479–488. doi:10.1016/S1053-8119(03)00311-2 
Ji, H. F., Li, J., Lu, R. R., Gu, R., Cao, L., and Gong, X. L. (2016). EEG classification 
for hybrid brain–computer interface using a tensor based multiclass multi-
modal analysis scheme. Comput. Intell. Neurosci. 2016, 1732836. doi:10.1155/ 
2016/1732836 
Jiang, J., Zhou, Z. T., Yin, E. W., Yu, Y., and Hu, D. W. (2014). Hybrid brain– 
computer interface (BCI) based on the EEG and EOG signals. Bio Med. Mater. 
Eng. 24, 2919–2925. doi:10.3233/BME-141111 
Jindal, U., Sood, M., Dutta, A., and Chowdhury, S. R. (2015). Development of 
point of care testing device for neurovascular coupling from simultaneous 
recording of EEG and NIRS during anodal transcranial direct current stimu-
lation. IEEE J. Trans. Eng. Health Med. 3, 2000112. doi:10.1109/ITEHM.2015. 
2389230 
Kaiser, V., Bauernfeind, G., Kreilinger, A., Kaufmann, T., Kubler, A., Neuper, C., 
et al. (2014). Cortical effects of user training in a motor imagery based brain–
computer interface measured by fNIRS and EEG. Neuroimage 85, 432–444. 
doi:10.1016/j.neuroimage.2013.04.097 
Kassab, A., Le Lan, J., Vannasing, P., and Sawan, M. (2015). Functional near- 
infrared spectroscopy caps for brain activity monitoring: a review. Appl. Opt. 54, 
576–586. doi:10.1364/AO.54.000576 
Kee, C. Y., Ponnambalam, S. C., and Loo, C. K. (2015). Multi-objective genetic 
algorithm as channel selection method for P300 and motor imagery data set. 
Neurocomputing 161, 120–131. doi:10.1016/j.neucom.2015.02.057 
Keles, H. O., Barbour, R. L., and Omurtag, A. (2016). Hemodynamic correlates 
of spontaneous neural activity measured by human whole-head resting state 
EEG+fNIRS. Neuroimage 138, 78–87. doi:10.1016/j.neuroimage.2016.05.058 
Kennedy, P. R., and Adams, K. D. (2003). A decision tree for brain–computer inter-
face devices. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 148–150. doi:10.1109/
TNSRE.2003.814420 
Khalighi, S., Sousa, T., Pires, G., and Nunes, U. (2013). Automatic sleep staging: 
a computer assisted approach for optimal combination of features and 
polysomnographic channels. Expert Syst. Appl. 40, 7046–7059. doi:10.1016/j.
eswa.2013.06.023 
Khan, B., Hodics, T., Hervey, N., Kondraske, G., Stowe, A. M., and Alexandrakis, G. 
(2013). Functional near-infrared spectroscopy maps cortical plasticity 
underlying altered motor performance induced by transcranial direct current 
stimulation. J. Biomed. Opt. 18, 116003. doi:10.1117/1.JBO.18.11.116003 
Khan, M. J., and Hong, K.-S. (2015). Passive BCI based on drowsiness detec-
tion: an fNIRS study. Biomed. Opt. Express 6, 4063–4078. doi:10.1364/
BOE.6.004063 
Khan, M. J., and Hong, K.-S. (2017). Hybird EEG-fNIRS-based eight command 
decoding for BCI: application to quadcopter control. Front. Neurorobot. 11:6. 
doi:10.3389/fnbot.2017.00006 
Khan, M. J., Hong, M. J., and Hong, K.-S. (2014). Decoding of four movement 
directions using hybrid NIRS-EEG brain–computer interface. Front. Hum. 
Neurosci. 8:244. doi:10.3389/fnhum.2014.00244 
Khemiri, S., Aloui, K., and Naceur, M. S. (2015). Paradoxical sleep stages detection 
using somnographic EOG signal for obese and no-obese patients. Int. J. Signal 
Imag. Syst. Eng. 8, 4–10. doi:10.1504/IJSISE.2015.067064 
Khushaba, R. N., Kodagoda, S., Lal, S., and Dissanayake, G. (2011). Driver drows-
iness classification using fuzzy wavelet-packet-based feature-extraction algo-
rithm. IEEE Trans. Biomed. Eng. 58, 121–131. doi:10.1109/TBME.2010.2077291 
Khushaba, R. N., Kodagoda, S., Lal, S., and Dissanayake, G. (2013). Uncorrelated 
fuzzy neighborhood preserving analysis based feature projection for 

24
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
driver drowsiness recognition. Fuzzy Sets Syst. 221, 90–111. doi:10.1016/j.
fss.2012.12.003 
Kiguchi, K., Lalitharatne, T. D., and Hayashi, Y. (2013). Estimation of forearm 
supination/pronation motion based on EEG signals to control an artificial 
arm. J. Adv. Mech. Des. Syst. Manuf. 7, 74–81. doi:10.1299/jamdsm.7.74 
Kim, B. H., Kim, M., and Jo, S. (2014). Quadcopter flight control using a low-cost 
hybrid interface with EEG-based classification and eye tracking. Comput. Biol. 
Med. 51, 82–92. doi:10.1016/j.compbiomed.2014.04.020 
Kim, C. H., Choi, B., Kim, D. G., Lee, S., Jo, S., and Lee, P. S. (2016). Remote nav-
igation of turtle by controlling instinct behavior via human brain–computer 
interface. J. Bionic. Eng. 13, 491–503. doi:10.1016/S1672-6529(16)60322-0 
Kim, K. H., Yoo, J. K., Kim, H. K., Son, W., and Lee, S. Y. (2006). A practical 
biosignal-based human interface applicable to the assistive systems for people 
with motor impairment. IEICE Trans. Inf. Syst. E 89d, 2644–2652. doi:10.1093/
ietisy/e89-d.10.2644 
Kim, S.-P., Kang, J.-H., Choe, S.-H., Jeong, W. J., Kim, T. H., Yun, K. S., et al. 
(2012). Modulation of theta phase synchronization in the human EEG 
during a recognition memory task. Neuroreport 23, 637–641. doi:10.1097/
WNR.0b013e328354afed 
Kim, S.-P., Simeral, J. D., Hochberg, L. R., Donoghue, J. P., Friehs, G. M., and 
Black, M. J. (2011). Point-and-click cursor control with an intracortical neural 
interface system in humans with tetraplegia. IEEE Trans. Neural Syst. Rehabil. 
Eng. 19, 193–203. doi:10.1109/TNSRE.2011.2107750 
Koo, B., Lee, H. G., Nam, Y., Kang, H., Koh, C. S., Shin, H. C., et al. (2015). A hybrid 
NIRS-EEG system for self-paced brain computer interface with online motor 
imagery. J. Neurosci. Methods 244, 26–32. doi:10.1016/j.jneumeth.2014.04.016 
Kreilinger, A., Kaiser, V., Breitwieser, C., Williamson, J., Neuper, C., and Muller-
Putz, G. R. (2012). Switching between manual control and brain–computer 
interface using long term and short term quality measures. Front. Neurosci. 
6:147. doi:10.3389/fnins.2011.00147 
Laconte, S. M. (2011). Decoding fMRI brain states in real-time. Neuroimage 56, 
440–454. doi:10.1016/j.neuroimage.2010.06.052 
Lafleur, K., Cassady, K., Doud, A., Shades, K., Rogin, E., and He, B. (2013). 
Quadcopter control in three-dimensional space using a noninvasive motor 
imagery-based brain–computer interface. J. Neural Eng. 10, 046003. doi:10.1088/ 
1741-2560/10/4/046003 
Lamti, H. A., Ben Khelifa, M. M., Gorce, P., and Alimi, A. M. (2013). A brain 
and gaze-controlled wheelchair. Comput. Methods Biomech. Biomed. Eng. 16, 
128–129. doi:10.1080/10255842.2013.815940 
Lee, M. H., Fazli, S., Mehnert, J., and Lee, S. W. (2015). Subject-dependent classi-
fication for robust idle state detection using multi-modal neuroimaging and 
data-fusion techniques in BCI. Pattern Recognit. 48, 2725–2737. doi:10.1016/j.
patcog.2015.03.010 
Leeb, R., Sagha, H., Chavarriaga, R., and Millan, J. D. (2011). A hybrid brain– 
computer interface based on the fusion of electroencephalographic and 
electromyographic activities. J. Neural Eng. 8, 025011. doi:10.1088/1741-2560/ 
8/2/025011 
Lesenfants, D., Habbal, D., Lugo, Z., Lebeau, M., Horki, P., Amico, E., et al. (2014). 
An independent SSVEP-based brain–computer interface in locked-in syn-
drome. J. Neural Eng. 11, 035002. doi:10.1088/1741-2560/11/3/035002 
Li, J., Ji, H. F., Cao, L., Zang, D., Gu, R., Xia, B., et al. (2014). Evaluation and appli-
cation of a hybrid brain computer interface for real wheelchair parallel control 
with multi-degree of freedom. Int. J. Neural Syst. 24, 1450014. doi:10.1142/
S0129065714500142 
Li, M. G., Guo, S. D., Zuo, G. Y., Sun, Y. J., and Yang, J. F. (2015). Removing ocular 
artifacts from mixed EEG signals with FastKICA and DWT. J. Intell. Fuzzy Syst. 
28, 2851–2861. doi:10.3233/IFS-151564 
Li, Y. Q., Long, J. Y., Yu, T. Y., Yu, Z. L., Wang, C. C., Zhang, H. H., et al. (2010). 
An EEG-based BCI system for 2-D cursor control by combining Mu/
Beta rhythm and P300 potential. IEEE Trans. Biomed. Eng. 57, 2495–2505. 
doi:10.1109/TBME.2010.2055564 
Li, Y. Q., Pan, J. H., Wang, F., and Yu, Z. L. (2013). A hybrid BCI system combining 
P300 and SSVEP and its application to wheelchair control. IEEE Trans. Biomed. 
Eng. 60, 3156–3166. doi:10.1109/TBME.2013.2270283 
Li, Y. T., Zhou, G., Graham, D., and Holtzhauer, A. (2016). Towards an EEG-based 
brain–computer interface for online robot control. Multimed. Tools Appl. 75, 
7999–8017. doi:10.1007/s11042-015-2717-z 
Lim, J. H., Hwang, H. J., Han, C. H., Jung, K. Y., and Im, C.-H. (2013). Classification 
of binary intentions for individuals with impaired oculomotor function: 
‘eyes-closed’ SSVEP-based brain–computer interface (BCI). J. Neural Eng. 10, 
026021. doi:10.1088/1741-2560/10/2/026021 
Lim, J. H., Lee, J. H., Hwang, H. J., Kim, D. H., and Im, C.-H. (2015). Development 
of a hybrid mental spelling system combining SSVEP-based brain–computer 
interface and webcam-based eye tracking. Biomed. Signal Process. Control 21, 
99–104. doi:10.1016/j.bspc.2015.05.012 
Lin, K., Cinetto, A., Wang, Y. J., Chen, X. G., Gao, S. K., and Gao, X. R. (2016). 
An online hybrid BCI system based on SSVEP and EMG. J. Neural Eng. 13, 
026020. doi:10.1088/1741-2560/13/2/026020 
Liu, X., and Hong, K.-S. (2017). Detection of primary RGB colors projected 
on a screen using fNIRS. J. Innov. Opt. Health Sci. 10, 6. doi:10.1142/
S1793545817500067 
Long, J. Y., Li, Y. Q., Wang, H. T., Yu, T. Y., Pan, J. H., and Li, F. (2012a). A hybrid 
brain computer interface to control the direction and speed of a simulated or 
real wheelchair. IEEE Trans. Neural Syst. Rehabil. Eng. 20, 720–729. doi:10.1109/
TNSRE.2012.2197221 
Long, J. Y., Li, Y. Q., Yu, T. Y., and Gu, Z. H. (2012b). Target selection with hybrid 
feature for BCI-based 2-D cursor control. IEEE Trans. Biomed. Eng. 59, 132–140. 
doi:10.1109/TBME.2011.2167718 
Lorenz, R., Pascual, J., Blankertz, B., and Vidaurre, C. (2014). Towards a holistic 
assessment of the user experience with hybrid BCIs. J. Neural Eng. 11:035007. 
doi:10.1088/1741-2560/11/3/035007
Ma, J. X., Zhang, Y., Cichocki, A., and Matsuno, F. (2015). A novel EOG/EEG 
hybrid human-machine interface adopting eye movements and ERPs: appli-
cation to robot control. IEEE Trans. Biomed. Eng. 62, 876–889. doi:10.1109/
TBME.2014.2369483 
Ma, T., Li, H., Deng, L., Yang, H., Lv, X., Li, P., et  al. (2017). The hybrid BCI 
system for movement control by combining motor imagery and moving onset 
visual evoked potential. J. Neural. Eng. 14, 026015. doi:10.1088/1741-2552/
aa5d5f 
Machado, S., Araujo, F., Paes, F., Velasques, B., Cunha, M., Budde, H., et  al. 
(2010). EEG-based brain–computer interfaces: an overview of basic concepts 
and clinical applications in neurorehabilitation. Rev. Neurosci. 21, 451–468. 
doi:10.1515/REVNEURO.2010.21.6.451 
Maria Alonso-Valerdi, L., Antonio Salido-Ruiz, R., and Ramirez-Mendoza, R. A. 
(2015). Motor imagery based brain–computer interfaces: an emerging technol-
ogy to rehabilitate motor deficits. Neuropsychologia 79, 354–363. doi:10.1016/j.
neuropsychologia.2015.09.012 
McFarland, D. J., Sarnacki, W. A., Vaughan, T. M., and Wolpaw, J. R. (2005). Brain–
computer interface (BCI) operation: signal and noise during early training 
sessions. Clin. Neurophysiol. 116, 56–62. doi:10.1016/j.clinph.2004.07.004 
McFarland, D. J., and Wolpaw, J. R. (2010). Brain–computer interfaces for the oper-
ation of robotic and prosthetic devices. Adv. Comput. 79, 169–187. doi:10.1016/
S0065-2458(10)79004-5 
McFarland, D. J., and Wolpaw, J. R. (2011). Brain–computer interfaces for commu-
nication and control. Commun. ACM 54, 60–66. doi:10.1145/1941487.1941506 
Muller-Putz, G., Leeb, R., Tangermann, M., Hohne, J., Kubler, A., Cincotti, F., et al. 
(2015). Towards noninvasive hybrid brain–computer interfaces: framework, 
practice, clinical application, and beyond. Proc. IEEE 103, 926–943. doi:10.1109/
JPROC.2015.2411333 
Muller-Putz, G. R., Scherer, R., Brauneis, C., and Pfurtscheller, G. (2005). 
Steady-state visual evoked potential (SSVEP)-based communication: 
impact of harmonic frequency components. J. Neural Eng. 2, 123–130. 
doi:10.1088/1741-2560/2/4/008 
Naito, G., Yoshida, L., Numata, T., Ogawa, Y., Kotani, K., and Jimbo, Y. (2014). 
Simultaneous classification of multiple motor imagery and P300 for increase 
in output information of brain–computer interface. Electr. Commun. Jpn. 98, 
47–54. doi:10.1002/ecj.11622 
Nam, C. S., Richard, P., Yamaguchi, T., and Bahn, S. (2014). Does touch matter? 
The effects of haptic visualization on human performance, behavior and 
perception. Int. J. Hum. Comput. Interact. 30, 839–841. doi:10.1080/1044731
8.2014.941270 
Nam, C. S., Whang, M., Liu, S. J., and Moore, M. (2015). Wayfinding of users with 
visual impairments in haptically enhanced virtual environments. Int. J. Hum. 
Comput. Interact. 31, 295–306. doi:10.1080/10447318.2015.1004151 
Naseer, N., and Hong, K.-S. (2013). Classification of functional near-infrared 
spectroscopy signals corresponding to the right- and left-wrist motor imagery 
for development of a brain–computer interface. Neurosci. Lett. 553, 84–89. 
doi:10.1016/j.neulet.2013.08.021 

25
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
Naseer, N., and Hong, K.-S. (2015a). Decoding answers to four-choice questions 
using functional near infrared spectroscopy. J. Near Infrared Spectrosc. 23, 
23–31. doi:10.1255/jnirs.1145 
Naseer, N., and Hong, K.-S. (2015b). fNIRS-based brain–computer interfaces: 
a review. Front. Hum. Neurosci. 9:3. doi:10.3389/fnhum.2015.00003 
Naseer, N., Hong, M. J., and Hong, K.-S. (2014). Online binary decision decoding 
using functional near-infrared spectroscopy for the development of brain– 
computer interface. Exp. Brain Res. 232, 555–564. doi:10.1007/s00221-013-3764-1 
Naseer, N., Noori, F. M., Qureshi, N. K., and Hong, K.-S. (2016a). Determining 
optimal feature-combination for LDA classification of functional near-infrared 
spectroscopy signals in brain–computer interface application. Front. Hum. 
Neurosci. 10:237. doi:10.3389/fnhum.2016.00237 
Naseer, N., Qureshi, N. K., Noori, F. M., and Hong, K.-S. (2016b). Analysis of 
different classification techniques for two-class functional near-infrared 
spectroscopy-based brain–computer interface. Comput. Intell. Neurosci. 2016, 
5480760. doi:10.1155/2016/5480760 
Nguyen, D. K., Tremblay, J., Pouliot, P., Vannasing, P., Florea, O., Carmant, L., 
et al. (2012). Non-invasive continuous EEG-fNIRS recording of temporal lobe 
seizures. Epilepsy Res. 99, 112–126. doi:10.1016/j.eplepsyres.2011.10.035 
Nguyen, D. K., Tremblay, J., Pouliot, P., Vannasing, P., Florea, O., Carmant, L., et al. 
(2013). Noninvasive continuous functional near-infrared spectroscopy com-
bined with electroencephalography recording of frontal lobe seizures. Epilepsia 
54, 331–340. doi:10.1111/epi.12011 
Nguyen, H.-D., and Hong, K.-S. (2016). Bundled-optode implementation for 3D 
imaging in functional near-infrared spectroscopy. Biomed. Opt. Express 7, 
3491–3507. doi:10.1364/BOE.7.003491 
Nguyen, H.-D., Hong, K.-S., and Shin, Y.-I. (2016). Bundled-optode method in 
functional near-infrared spectroscopy. PLoS ONE 11:e0165146. doi:10.1371/
journal.pone.0165146 
Nguyen, L. H., and Hong, K.-S. (2013). Adaptive synchronization of two coupled 
chaotic Hindmarsh-Rose neurons by controlling the membrane potential of a 
slave neuron. Appl. Math. Model. 37, 2460–2468. doi:10.1016/j.apm.2012.06.003 
Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a 
review. Sensors 12, 1211–1279. doi:10.3390/s120201211 
Olejniczak, P. (2006). Neurophysiologic basis of EEG. J. Clin. Neurophysiol. 23, 
186–189. doi:10.1097/01.wnp.0000220079.61973.6c 
Pan, J. H., Xie, Q. Y., He, Y. B., Wang, F., Di, H. B., Laureys, S., et al. (2014). Detecting 
awareness in patients with disorders of consciousness using a hybrid brain– 
computer interface. J. Neural Eng. 11, 056007. doi:10.1088/1741-2560/11/5/056007 
Panicker, R. C., Puthusserypady, S., and Sun, Y. (2011). An asynchronous P300 
BCI with SSVEP-based control state detection. IEEE Trans. Biomed. Eng. 58, 
1781–1788. doi:10.1109/TBME.2011.2116018 
Papadelis, C., Chen, Z., Kourtidou-Papadeli, C., Bamidis, P. D., Chouvarda, L., 
Bekiaris, E., et al. (2007). Monitoring sleepiness with on-board electrophys-
iological recordings for preventing sleep-deprived traffic accidents. Clin. 
Neurophysiol. 118, 1906–1922. doi:10.1016/j.clinph.2007.04.031 
Patil, S. M., and Patil, C. G. (2014). An approach for human machine interaction 
using electromyography. J. Med. Imaging Health Inform. 4, 71–75. doi:10.1166/
jmihi.2014.1224 
Peng, K., Nguyen, D. K., Tayah, T., Vannasing, P., Tremblay, J., Sawan, M., et al. 
(2014). fNIRS-EEG study of focal interictal epileptiform discharges. Epilepsy 
Res. 108, 491–505. doi:10.1016/j.eplepsyres.2013.12.011 
Pfurtscheller, G., Allison, B. Z., Brunner, C., Bauernfeind, G., Solis-Escalante, T., 
Scherer, R., et al. (2010). The hybrid BCI. Front. Neurosci. 4:30. doi:10.3389/
fnpro.2010.00003 
Piccione, F., Giorgi, F., Tonin, P., Priftis, K., Giove, S., Silvoni, S., et al. (2006). 
P300-based brain computer interface: reliability and performance in healthy 
and paralysed participants. Clin. Neurophysiol. 117, 531–537. doi:10.1016/j.
clinph.2005.07.024 
Picot, A., Charbonnier, S., and Caplier, A. (2012). On-line detection of drowsiness 
using brain and visual information. IEEE Trans. Syst. Man Cybern. A Syst. Hum. 
42, 764–775. doi:10.1109/TSMCA.2011.2164242 
Pokorny, C., Breitwieser, C., and Muller-Putz, G. R. (2016). The role of transient 
target stimuli in a steady-state somatosensory evoked potential-based brain–
computer interface setup. Front. Neurosci. 10:152. doi:10.3389/fnins.2016.00152 
Pouliot, P., Tran, T. P. Y., Birca, V., Vannasing, P., Tremblay, J., Lassonde, M., et al. 
(2014). Hemodynamic changes during posterior epilepsies: an EEG-fNIRS 
study. Epilepsy Res. 108, 883–890. doi:10.1016/j.eplepsyres.2014.03.007 
Power, S. D., Falk, T. H., and Chau, T. (2010). Classification of prefrontal activity 
due to mental arithmetic and music imagery using hidden Markov models 
and frequency domain near-infrared spectroscopy. J. Neural Eng. 7, 026002. 
doi:10.1088/1741-2560/7/2/026002 
Power, S. D., Kushki, A., and Chau, T. (2011). Towards a system-paced near- 
infrared spectroscopy brain–computer interface: differentiating prefrontal 
activity due to mental arithmetic and mental singing from the no-control state. 
J. Neural Eng. 8, 066004. doi:10.1088/1741-2560/8/6/066004 
Putze, F., Hesslinger, S., Tse, C. Y., Huang, Y. Y., Herff, C., Guan, C. T., et al. (2014). 
Hybrid fNIRS-EEG based classification of auditory and visual perception 
processes. Front. Neurosci. 8:373. doi:10.3389/fnins.2014.00373 
Qi, X., Zhou, G., Li, Y. T., and Peng, G. (2012). “RadioSense: exploiting wireless 
communication patterns for body sensor network activity recognition,” in IEEE 
33rd Real-Time Systems Symposium (San Juan), 95–104.
Qian, D., Wang, B., Qing, X. Y., Zhang, T., Zhang, Y., Wang, X. Y., et al. (2016). 
Bayesian nonnegative CP decomposition based feature extraction algorithm 
for drowsiness detection. IEEE Trans. Neural Syst. Rehabil. Eng. doi:10.1109/
TNSRE.2016.2618902 
Qian, D., Wang, B., Qing, X. Y., Zhang, T., Zhang, Y., Wang, X. Y., et al. (2017). 
Drowsiness detection by Bayesian-copula discriminant classifier based on 
EEG signals during daytime short nap. IEEE Trans. Biomed. Eng. 64, 743–754. 
doi:10.1109/TBME.2016.2574812 
Ramadan, R. A., and Vasilakos, A. V. (2017). Brain computer interface: control 
signals review. Neurocomputing 223, 26–44. doi:10.1016/j.neucom.2016.10.024 
Ramli, R., Arof, H., Ibrahim, F., Mokhtar, N., and Idris, M. Y. I. (2015). Using finite 
state machine and a hybrid of EEG signal and EOG artifacts for an asynchro-
nous wheelchair navigation. Expert Syst. Appl. 42, 2451–2463. doi:10.1016/j.
eswa.2014.10.052 
Ravindra, V., and Castellini, C. (2014). A comparative analysis of three non- 
invasive human-machine interfaces for the disabled. Front. Neurorobot. 8:24. 
doi:10.3389/fnbot.2014.00024 
Ren, Z., Qi, X., Zhou, G., and Wang, H. N. (2014). Exploiting the data sensitivity 
of neurometric fidelity for optimizing EEG sensing. IEEE Internet Things J. 1, 
243–254. doi:10.1109/JIOT.2014.2322331 
Rohm, M., Schneiders, M., Mueller, C., Kreilinger, A., Kaiser, V., Mueller-
Putz, G. R., et  al. (2013). Hybrid brain–computer interfaces and hybrid 
neuroprostheses for restoration of upper limb functions in individuals with 
high-level spinal cord injury. Artif. Intell. Med. 59, 133–142. doi:10.1016/j.
artmed.2013.07.004 
Roy, R. N., Charbonnier, S., and Bonnet, S. (2014). Eye blink characterization 
from frontal EEG electrodes using source separation and pattern recognition 
algorithms. Biomed. Signal Process. Control 14, 256–264. doi:10.1016/j.
bspc.2014.08.007 
Rupp, R., Rohm, M., Schneiders, M., Kreilinger, A., and Muller-Putz, G. R. (2015). 
Functional rehabilitation of the paralyzed upper extremity after spinal cord 
injury by noninvasive hybrid neuroprostheses. Proc. IEEE 103, 954–968. 
doi:10.1109/JPROC.2015.2395253 
Rutkowski, T. M. (2016). Robotic and virtual reality BCIs using spatial tactile 
and auditory Oddball paradigms. Front. Neurorobot. 10:20. doi:10.3389/
fnbot.2016.00020 
Safaie, J., Grebe, R., Moghaddam, H. A., and Wallois, F. (2013). Toward a fully 
integrated wireless wearable EEG-NIRS bimodal acquisition system. J. Neural 
Eng. 10, 056001. doi:10.1088/1741-2560/10/5/056001 
Sale, M. V., Mattingley, J. B., Zalesky, A., and Cocchi, L. (2015). Imaging 
human brain networks to improve the clinical efficacy of non-invasive 
brain stimulation. Neurosci. Biobehav. Rev. 57, 187–198. doi:10.1016/j.
neubiorev.2015.09.010 
Santosa, H., Hong, M. J., and Hong, K.-S. (2014). Lateralization of music processing 
auditory cortex: an fNIRS study. Front. Behav. Neurosci. 8:418. doi:10.3389/
fnbeh.2014.00418 
Santosa, H., Hong, M. J., Kim, S. P., and Hong, K.-S. (2013). Noise reduction in 
functional near-infrared spectroscopy signals by independent component 
analysis. Rev. Sci. Instrum. 84, 073106. doi:10.1063/1.4812785 
Schestatsky, P., Morales-Quezada, L., and Fregni, F. (2013). Simultaneous 
EEG monitoring during transcranial direct current stimulation. J. Vis. Exp. 
(76):e50426. doi:10.3791/50426 
Shishkin, S. L., Nuzhdin, Y. O., Svirin, E. P., Trofimov, A. G., Fedorova, A. A., 
Kozyrskiy, B. L., et al. (2016). EEG negativity in fixations used for gaze-based 

26
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
control: toward converting intentions into actions with an eye–brain–computer 
interface. Front. Neurosci. 10:528. doi:10.3389/fnins.2016.00528 
Sinha, R. K. (2008). Artificial neural network and wavelet based automated detec-
tion of sleep spindles, REM sleep and wake states. J. Med. Syst. 32, 291–299. 
doi:10.1007/s10916-008-9134-z 
Sood, M., Besson, P., Muthalib, M., Jindal, U., Perrey, S., Dutta, A., et al. (2016). 
NIRS-EEG joint imaging during transcranial direct current stimulation: online 
parameter estimation with an autoregressive model. J. Neurosci. Methods 274, 
71–80. doi:10.1016/j.jneumeth.2016.09.008 
Sperdin, H. F., and Schaer, M. (2016). Aberrant development of speech processing 
in young children with autism: new insights from neuroimaging biomarkers. 
Front. Neurosci. 10:393. doi:10.3389/fnins.2016.00393 
Stangl, M., Bauernfeind, G., Kurzmann, J., Scherer, R., and Neuper, C. (2013). 
A haemodynamic brain–computer interface based on real-time classification 
of near infrared spectroscopy signals during motor imagery and mental arith-
metic. J. Near Infrared Spectrosc. 21, 157–171. doi:10.1255/jnirs1048 
Su, Y., Qi, Y., Luo, J. X., Wu, B., Yang, F., Li, Y., et al. (2011). A hybrid brain– 
computer interface control strategy in a virtual environment. J. Zhejiang Univ. 
Sci. C 12, 351–361. doi:10.1631/jzus.C1000208 
Tidoni, E., Gergondet, P., Kheddar, A., and Aglioti, S. M. (2014). Audio-visual feed-
back improves the BCI performance in the navigational control of a humanoid 
robot. Front. Neurorobot. 8:20. doi:10.3389/fnbot.2014.00020 
Tomita, Y., Vialatte, F. B., Dreyfus, G., Mitsukura, Y., Bakardjian, H., and Cichocki, A. 
(2014). Bimodal BCI using simultaneously NIRS and EEG. IEEE Trans. 
Biomed. Eng. 61, 1274–1284. doi:10.1109/TBME.2014.2300492 
Trejo, L. J., Rosipal, R., and Matthews, B. (2006). Brain–computer interfaces for 1-D 
and 2-D cursor control: designs using volitional control of the EEG spectrum 
or steady-state visual evoked potentials. IEEE Trans. Neural Syst. Rehabil. Eng. 
14, 225–229. doi:10.1109/TNSRE.2006.875578 
Trejo, L. J., Wheeler, K. R., Jorgensen, C. C., Rosipal, R., Clanton, S. T., Matthews, B., 
et  al. (2003). Multimodal neuroelectric interface development. IEEE Trans. 
Neural Syst. Rehabil. Eng. 11, 199–204. doi:10.1109/TNSRE.2003.814426 
Turnip, A., and Hong, K.-S. (2012). Classifying mental activities from EEG-P300 
signals using adaptive neural networks. Int. J. Innov. Comp. Inf. Control 8, 
6429–6443. 
Turnip, A., Hong, K.-S., and Jeong, M. Y. (2011). Real-time feature extraction 
of P300 component using adaptive nonlinear principal component analysis. 
Biomed. Eng. Online 10, 83. doi:10.1186/1475-925X-10-83 
Vannasing, P., Cornaggia, I., Vanasse, C., Tremblay, J., Diadori, P., Perreault, S., 
et al. (2016). Potential brain language reorganization in a boy with refractory 
epilepsy; an fNIRS-EEG and fMRI comparison. Epilepsy Behav. Case Rep. 5, 
34–37. doi:10.1016/j.ebcr.2016.01.006 
Virkkala, J., Hasan, J., Varri, A., Himanen, S. L., and Harma, M. (2007a). The use of 
two-channel electro-oculography in automatic election of unintentional sleep 
onset. J. Neurosci. Methods 163, 137–144. doi:10.1016/j.jneumeth.2007.02.001 
Virkkala, J., Hasan, J., Varri, A., Himanen, S. L., and Muller, K. (2007b). Automatic 
sleep stage classification using two-channel electro-oculography. J. Neurosci. 
Methods 166, 109–115. doi:10.1016/j.jneumeth.2007.06.016 
Visani, E., Canafoglia, L., Gilioli, I., Sebastiano, D. R., Contarino, V. E., Duran, D., 
et  al. (2015). Hemodynamic and EEG time-courses during unilateral hand 
movement in patients with cortical myoclonus. An EEG-fMRI and EEG- 
TD-fNIRS study. Brain Topogr. 28, 915–925. doi:10.1007/s10548-014-0402-6 
Vuckovic, A., and Sepulveda, F. (2012). A two-stage four-class BCI based on imag-
inary movements of the left and the right wrist. Med. Eng. Phys. 34, 964–971. 
doi:10.1016/j.medengphy.2011.11.001 
Wang, D., Miao, D. Q., and Blohm, G. (2012). Multi-class motor imagery EEG 
decoding for brain–computer interfaces. Front. Neurosci. 6:151. doi:10.3389/
fnins.2012.00151 
Wang, H. Q., Zhang, Y., Waytowich, N. R., Krusienski, D. J., Zhou, G. X., Jin, J., 
et al. (2016). Discriminative feature extraction via multivariate linear regression 
for SSVEP-Based BCI. IEEE Trans. Neural Syst. Rehabil. Eng. 24, 532–541. 
doi:10.1109/TNSRE.2016.2519350 
Wang, H. T., Li, Y. Q., Long, J. Y., Yu, T. Y., and Gu, Z. H. (2014). An asynchronous 
wheelchair control by hybrid EEG-EOG brain–computer interface. Cogn. 
Neurodynamics 8, 399–409. doi:10.1007/s11571-014-9296-y 
Wang, M. J., Daly, I., Allison, B. Z., Jin, J., Zhang, Y., Chen, L. L., et al. (2015). 
A new hybrid BCI paradigm based on P300 and SSVEP. J. Neurosci. Methods 
244, 16–25. doi:10.1016/j.jneumeth.2014.06.003 
Weiskopf, N. (2012). Real-time fMRI and its application to neurofeedback. 
Neuroimage 62, 682–692. doi:10.1016/j.neuroimage.2011.10.009 
Weyand, S., Takehara-Nishiuchi, K., and Chau, T. (2015). Weaning off mental tasks 
to achieve voluntary self-regulatory control of a near-infrared spectroscopy 
brain–computer interface. IEEE Trans. Neural Syst. Rehabil. Eng. 23, 548–561. 
doi:10.1109/TNSRE.2015.2399392 
Witkowski, M., Cortese, M., Cempini, M., Mellinger, J., Vitiello, N., and 
Soekadar, S. R. (2014). Enhancing brain–machine interface (BMI) control of 
a hand exoskeleton using electrooculography (EOG). J. Neuroeng. Rehabil. 11, 
165. doi:10.1186/1743-0003-11-165 
Wu, Y. Y., Li, M., and Wang, J. (2016). Toward a hybrid brain–computer interface 
based on repetitive visual stimuli with missing events. J. Neuroeng. Rehabil. 13, 
66. doi:10.1186/s12984-016-0179-9 
Xie, H.-B., Guo, T., Bai, S., and Dokos, S. (2014). Hybrid soft computing systems 
for electromyographic signals analysis: a review. Biomed. Eng. Online 13, 8. 
doi:10.1186/1475-925X-13-8 
Xu, M. P., Chen, L., Zhang, L. X., Qi, H. Z., Ma, L., Tang, J. B., et al. (2014). A visual 
parallel-BCI speller based on the time-frequency coding strategy. J. Neural Eng. 
11, 026014. doi:10.1088/1741-2560/11/2/026014 
Xu, M. P., Qi, H. Z., Wan, B. K., Yin, T., Liu, Z. P., and Ming, D. (2013). A hybrid BCI 
speller paradigm combining P300 potential and the SSVEP blocking feature. 
J. Neural Eng. 10, 026001. doi:10.1088/1741-2560/10/2/026001 
Xu, M. P., Wang, Y. J., Nakanishi, M., Wang, Y. T., Qi, H. Z., Jung, T. P., et al. (2016). 
Fast detection of covert visuospatial attention using hybrid N2pc and SSVEP 
features. J. Neural Eng. 13, 066003. doi:10.1088/1741-2560/13/6/066003 
Yang, B. H., He, L. F., Lin, L., and Wang, Q. (2015). Fast removal of ocular 
artifacts from electroencephalogram signals using spatial constraint inde-
pendent component analysis based recursive least squares in brain–computer 
interface. Front. Inform. Technol. Elect. Eng. 16:486–496. doi:10.1631/FITEE. 
1400299 
Yin, E., Zhou, Z., Jiang, J., Chen, F., Liu, Y., and Hu, D. (2013). A novel hybrid BCI 
speller based on the incorporation of SSVEP into the P300 paradigm. J. Neural 
Eng. 10, 026012. doi:10.1088/1741-2560/10/2/026012 
Yin, E. W., Zeyl, T., Saab, R., Chau, T., Hu, D. W., and Zhou, Z. T. (2015a). A hybrid 
brain–computer interface based on the fusion of P300 and SSVEP scores. 
IEEE Trans. Neural Syst. Rehabil. Eng. 23, 693–701. doi:10.1109/TNSRE.2015. 
2403270 
Yin, X. X., Xu, B. L., Jiang, C. H., Fu, Y. F., Wang, Z. D., Li, H. Y., et al. (2015b). 
Classification of hemodynamic responses associated with force and speed 
imagery for a brain–computer interface. J. Med. Syst. 39, 53. doi:10.1007/
s10916-015-0236-0 
Yin, X. X., Xu, B. L., Jiang, C. H., Fu, Y. F., Wang, Z. D., Li, H. Y., et al. (2015c). 
A hybrid BCI based on EEG and fNIRS signals improves the performance of 
decoding motor imagery of both force and speed of hand clenching. J. Neural 
Eng. 12, 036004. doi:10.1088/1741-2560/12/3/036004 
Yin, E. W., Zhou, Z. T., Jiang, J., Chen, F. L., Liu, Y. D., and Hu, D. W. (2014). 
A speedy hybrid BCI spelling approach combining P300 and SSVEP. IEEE 
Trans. Biomed. Eng. 61, 473–483. doi:10.1109/TBME.2013.2281976 
Yong, X. Y., Fatourechi, M., Ward, R. K., and Birch, G. E. (2012). Automatic artifact 
removal in a self-paced hybrid brain–computer interface system. J. Neuroeng. 
Rehabil. 9, 50. doi:10.1186/1743-0003-9-50 
Yoshino, K., and Kato, T. (2012). Vector-based phase classification of initial dips 
during word listening using near-infrared spectroscopy. Neuroreport 23, 
947–951. doi:10.1097/WNR.0b013e328359833b 
Yu, T. Y., Li, Y. Q., Long, J. Y., and Gu, Z. H. (2012). Surfing the internet with a BCI 
mouse. J. Neural Eng. 9, 036012. doi:10.1088/1741-2560/9/3/036012 
Yu, T. Y., Li, Y. Q., Long, J. Y., and Li, F. (2013). A hybrid brain–computer inter-
face-based mail client. Comput. Math. Method Med. 2013:750934. doi:10.1155/ 
2013/750934 
Yu, T. Y., Xiao, J., Wang, F. Y., Zhang, R., Gu, Z. H., Cichocki, A., et al. (2015). 
Enhanced motor imagery training using a hybrid BCI with feedback. IEEE 
Trans. Biomed. Eng. 62, 1706–1717. doi:10.1109/TBME.2015.2402283 
Zafar, A., and Hong, K.-S. (2017). Detection and classification of three class initial 
dips from prefrontal cortex. Biomed. Opt. Express 8, 367–383. doi:10.1364/
boe.8.000367 
Zaghi, S., Acar, M., Hultgren, B., Boggio, P. S., and Fregni, F. (2010). Noninvasive 
brain stimulation with low-intensity electrical currents: putative mechanisms 
of action for direct and alternating current stimulation. Neuroscientist. 16, 
285–307. doi:10.1177/1073858409336227 
Zander, T. O., and Kothe, C. (2011). Towards passive brain–computer interfaces: 
applying brain–computer interface technology to human-machine systems in 
general. J. Neural Eng. 8, 025005. doi:10.1088/1741-2560/8/2/025005 

27
Hong and Khan
Hybridization in BCI
Frontiers in Neurorobotics  |  www.frontiersin.org
July 2017  |  Volume 11  |  Article 35
Zhang, L., He, W., He, C. H., and Wang, P. (2010). Improving mental task classi-
fication by adding high frequency band information. J. Med. Syst. 34, 51–60. 
doi:10.1007/s10916-008-9215-z 
Zhang, R., Li, Y. Q., Yan, Y. Y., Zhang, H., Wu, S. Y., Yu, T. Y., et al. (2016a). Control 
of a wheelchair in an indoor environment based on a brain–computer interface 
and automated navigation. IEEE Trans. Neural Syst. Rehabil. Eng. 24, 128–139. 
doi:10.1109/TNSRE.2015.2439298 
Zhang, Y., Zhou, G. X., Jin, J., Zhao, Q. B., Wang, X. Y., and Cichocki, A. 
(2016b). Sparse Bayesian classification of EEG for brain–computer inter-
face. IEEE Trans. Neural Netw. Learn. Syst. 27, 2256–2267. doi:10.1109/
TNNLS.2015.2476656 
Zhang, Y., Zhao, Q. B., Jin, J., Wang, X. Y., and Cichocki, A. (2012). A novel BCI 
based on ERP components sensitive to configural processing of human faces. 
J. Neural Eng. 9, 026018. doi:10.1088/1741-2560/9/2/026018 
Zhang, Y., Zhou, G. X., Jin, J., Wang, M. J., Wang, X. Y., and Cichocki, A. (2013). 
L1-regularized multiway canonical correlation analysis for SSVEP-based 
BCI. IEEE Trans. Neural Syst. Rehabil. Eng. 21, 887–896. doi:10.1109/TNSRE. 
2013.2279680 
Zhang, Y., Zhou, G. X., Jin, J., Wang, X. Y., and Cichocki, A. (2014). Frequency 
recognition in SSVEP-based BCI using multiset canonical correlation analysis. 
Int. J. Neural Syst. 24, 1450013. doi:10.1142/S0129065714500130 
Zhao, J., Li, W., and Li, M. F. (2015). Comparative study of SSVEP- and P300-
based models for the telepresence control of humanoid robots. PLoS ONE 
10:e0142168. doi:10.1371/journal.pone.0142168 
Zhou, G. X., Zhao, Q. B., Zhang, Y., Adali, T., Xie, S. L., and Cichocki, A. (2016). 
Linked component analysis from matrices to high-order tensors: applications to 
biomedical data. Proc. IEEE 104, 310–331. doi:10.1109/JPROC.2015.2474704 
Zimmermann, R., Marchal-Crespo, L., Edelmann, J., Lambercy, O., Fluet, M. C., 
Riener, R., et al. (2013). Detection of motor execution using a hybrid fNIRS- 
biosignal BCI: a feasibility study. J. Neuroeng. Rehabil. 10, 4. doi:10.1186/1743- 
0003-10-4 
Conflict of Interest Statement: The authors declare that the research was con-
ducted in the absence of any commercial or financial relationship that could be 
construed as a potential conflict of interest.
Copyright © 2017 Hong and Khan. This is an open-access article distributed under the 
terms of the Creative Commons Attribution License (CC BY). The use, distribution or 
reproduction in other forums is permitted, provided the original author(s) or licensor 
are credited and that the original publication in this journal is cited, in accordance 
with accepted academic practice. No use, distribution or reproduction is permitted 
which does not comply with these terms.
