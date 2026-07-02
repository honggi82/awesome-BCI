REVIEW published: 06 August 2018 doi: 10.3389/fnhum.2018.00312

# EEG-Based BCI Control Schemes for Lower-Limb Assistive-Robots

Madiha Tariq, Pavel M. Trivailo and Milan Simic*

School of Engineering, RMIT University Melbourne, Melbourne, VIC, Australia

Over recent years, brain-computer interface (BCI) has emerged as an alternative communication system between the human brain and an output device. Deciphered intents, after detecting electrical signals from the human scalp, are translated into control commands used to operate external devices, computer displays and virtual objects in the real-time. BCI provides an augmentative communication by creating a muscle-free channel between the brain and the output devices, primarily for subjects having neuromotor disorders, or trauma to nervous system, notably spinal cord injuries (SCI), and subjects with unaffected sensorimotor functions but disarticulated or amputated residual limbs. This review identiﬁes the potentials of electroencephalography (EEG) based BCI applications for locomotion and mobility rehabilitation. Patients could beneﬁt from its advancements such as wearable lower-limb (LL) exoskeletons, orthosis, prosthesis, wheelchairs, and assistive-robot devices. The EEG communication signals employed by the aforementioned applications that also provide feasibility for future development in the ﬁeld are sensorimotor rhythms (SMR), event-related potentials (ERP) and visual evoked potentials (VEP). The review is an effort to progress the development of user’s mental task related to LL for BCI reliability and conﬁdence measures. As a novel contribution, the reviewed BCI control paradigms for wearable LL and assistive-robots are presented by a general control framework ﬁtting in hierarchical layers. It reﬂects informatic interactions, between the user, the BCI operator, the shared controller, the robotic device and the environment. Each sub layer of the BCI operator is discussed in detail, highlighting the feature extraction, classiﬁcation and execution methods employed by the various systems. All applications’ key features and their interaction with the environment are reviewed for the EEG-based activity mode recognition, and presented in form of a table. It is suggested to structure EEG-BCI controlled LL assistive devices within the presented framework, for future generation of intent-based multifunctional controllers. Despite the development of controllers, for BCI-based wearable or assistive devices that can seamlessly integrate user intent, practical challenges associated with such systems exist and have been discerned, which can be constructive for future developments in the ﬁeld.

Edited by:

Mikhail Lebedev, Duke University, United States

Reviewed by:

Vera Talis, Institute for Information Transmission

Problems (RAS), Russia

Yuri Levik, Institute for Information Transmission

Problems (RAS), Russia *Correspondence:

Milan Simic milan.simic@rmit.edu.au

Received: 03 May 2018 Accepted: 16 July 2018

Published: 06 August 2018

Citation: Tariq M, Trivailo PM and Simic M

(2018) EEG-Based BCI Control Schemes for Lower-Limb Assistive-Robots.

Keywords: brain-computer interface (BCI), electroencephalography (EEG), spinal cord injury (SCI), exoskeletons, orthosis, assistive-robot devices

Front. Hum. Neurosci. 12:312. doi: 10.3389/fnhum.2018.00312

## INTRODUCTION

The ﬁeld of assistive technologies, for mobility rehabilitation, is ameliorating by the introduction of electrophysiological signals to control these devices. The system runs independent of physical, or muscular interventions, using brain signals that reﬂect user’s intent to control devices/limbs (Millán et al., 2010; Lebedev and Nicolelis, 2017), called brain-computer interface (BCI). Commonly used non-invasive modality to record brain signals is electroencephalography (EEG). EEG signals are deciphered to control commands in order to restore communication between the brain and the output device when the natural communication channel i.e., neuronal activity is disrupted. Recent reviews on EEG-BCI for communication and rehabilitation of lower-limbs (LL) could be found in (Cervera et al., 2018; Deng et al., 2018; He et al., 2018a; Lazarou et al., 2018; Semprini et al., 2018; Slutzky, 2018).

About ﬁve decades ago, EEG-BCIs used computer cursor movements to communicate user intents for patient-assistance in various applications (Vidal, 1973; Wolpaw et al., 2002; Lebedev and Nicolelis, 2017). The applications are now widespread, as machine learning has become one essential component of BCI, functional in diﬀerent ﬁelds of neurorobotics and neuroprosthesis. For lower extremity, applications include human locomotion assistance, gait rehabilitation, and enhancement of physical abilities of able-bodied humans (Deng et al., 2018). Devices for locomotion, or mobility assistance, vary from wearable to (non-wearable) assistive-robot devices. Wearable devices such as exoskeletons, orthosis, prosthesis, and assistive-robot devices including wheelchairs, guiding humanoids, telepresence and mobile robots for navigation are the focus of our investigation.

Control schemes, oﬀered by these systems, rely on the inputs derived from electrophysiological signals, electromechanical sensors from the device, and the deployment of ﬁnite state controller that attempts to implicate user’s motion intention, to generate correct walking trajectories with wearable robots (Duvinage et al., 2012; Jimenez-Fabian and Verlinden, 2012; Herr et al., 2013; Contreras-Vidal et al., 2016). Input signals are typically extracted from the residual limb/muscles i.e., amputated or disarticulated lower-limbs (LL), via electromyography (EMG), from users with no cortical lesion or intact cognitive functions. Such solutions consequently preclude patient groups whose injuries necessitate direct cortical input to the BCI controller, for instance users with neuromotor disorders such as spinal cord injury (SCI) and stroke, or inactive eﬀerent nerves/synergistic muscle groups. In this case direct cortical inputs from EEG could be the central-pattern-generators (CPG) that generate basic motor patterns at the supraspinal or cortical level (premotor and motor cortex); or the LL kinesthetic motor imagery (KMI) signals (Malouin and Richards, 2010). The realization of BCI controllers solely driven by EEG signals, for controlling LL wearable/assistive devices, is therefore possible (Lee et al., 2017). Several investigations reinstate that CPG with less supraspinal control is involved in the control of bipedal locomotion (Dimitrijevic et al., 1998; Beloozerova et al., 2003; Tucker et al., 2015). This provides the basis for the development of controllers, directly driven from

cortical activity in correlation to the user intent for volitional movements (Nicolas-Alonso and Gomez-Gil, 2012; Angeli et al., 2014; Tucker et al., 2015; Lebedev and Nicolelis, 2017) instead of EMG signals. Consequently, controllers with EEG-based activity mode recognition for portable assistive devices, have become an alternative to get seamless results (Presacco et al., 2011b). However, when employing EEG signals as input to the BCI controller, there necessitates a validation about the notion that EEG signals from the cortex can be useful for the locomotion control.

Though cortical sites encode movement intents, the kinetic and kinematic changes necessary to execute the intended movement, are essential factors to be considered. Studies indicate that the selective recruitment of embedded “muscle synergies” provide an eﬃcient means of intent-driven, selective movement, i.e., these synergies, stored as CPGs, specify spatial organization of muscle activation and characterize diﬀerent biomechanical subtasks (Chvatal et al., 2011; Chvatal and Ting, 2013). According to Maguire et al. (2018), during human walking, Chvatal and Ting (2012) identiﬁed diﬀerent muscle synergies for the control of muscle activity and coordination. According to Petersen et al. (2012), the swing-phase was more inﬂuenced by the central cortical control, i.e., dorsiﬂexion in early stance at heel strike, and during pre-swing and swing phases for energy transfer from trunk to leg. They also emphasized the importance of cortical activity during steady unperturbed gait for the support of CPG activity. Descending cortical signals communicate with spinal networks to ensure that accurate changes in limb movement have appropriately integrated into the gait pattern (Armstrong, 1988). The subpopulations of motor-cortical neurons activate sequentially amid the step cycle particularly during the initiation of pre-swing and swing (Drew et al., 2008). The importance of cortical activation upon motor imagery (MI) of locomotor tasks has been reported in Malouin et al. (2003) and Pfurtscheller et al. (2006b). Similarly, the conﬁrmation of electrocortical activity coupled to gait cycle, during treadmill walking or LL control, for applications as EEG-BCI exoskeletons and orthotic devices, has been discerned by (He et al., 2018b, Gwin et al. (2010, 2011), Wieser et al. (2010), Presacco et al. (2011a), Presacco et al. (2011b), Chéron et al. (2012), Bulea et al. (2013), Bulea et al. (2015), Jain et al. (2013), Petrofsky and Khowailed (2014), Kumar et al. (2015), and Liu et al. (2015). This provides the rationale for BCI controllers that incorporate cortical signals for high-level commands, based on user intent to walk/bipedal locomotion or kinesthetic motor imagery of LL.

While BCIs may not require any voluntary muscle control, they are certainly dependent on brain response functions therefore the choice of BCI depends on the user’s sensorimotor lesion and adaptability. Non-invasive types of BCI depend on EEG signals used for communication, which elicit under speciﬁc experimental protocols. Deployed electrophysiological signals that we investigate, include oscillatory/sensorimotor rhythms (SMR), elicited upon walking intent, MI or motor execution (ME) of a task, and evoked potentials as event-related potentials (ERP/P300) and visual evoked potentials (VEP). Such BCI functions as a bridge to bring sensory input into the brain, bypassing damages sight, listening or sensing abilities. Figure 1

|[Figure 1]<br><br>FIGURE 1 | Generic concept/function diagram of BCI controlled assistive LL devices based on motor imagery.|
|---|

shows a schematic description of a BCI system based on MI, adapted from He et al. (2015). The user performs MI of limb(s), which is encoded in EEG reading; features representing the task are deciphered, processed and translated to commands in order to control assistive-robot device.

Reviewed control schemes deployed by wearable LL and assistive-robots are presented in a novel way, i.e., in form of a general control framework ﬁtting in hierarchical layers. It shows the informatic interactions, between the user, the BCI operator, the shared controller, and the robot device with environment. The BCI operator is discussed in detail in the light of the feature extraction, classiﬁcation and execution methods employed by all reviewed systems. Key features of present stateof-the-art EEG-based BCI applications and its interaction with the environment are presented and summarized in the form of a table. Proposed BCI control framework can cater similar systems based on fundamentally diﬀerent classes. We expect a progress in the incorporation of the novel framework for the improvement of user-machine adaptation algorithms in a BCI.

The reviewed control schemes indicated that the MI/ME of LL tasks, as aspects of SMR-based BCI have not been extensively used compared to upper limbs (Tariq et al., 2017a,b, 2018). This is due to the small representation area of LL, in contrast to upper limbs, located inside the interhemispheric ﬁssure of the sensorimotor cortex (Penﬁeld and Boldrey, 1937). The review is an eﬀort to progress the development of user’s mental task related to LL for BCI reliability and conﬁdence measures.

Challenges presently faced by EEG-BCI controlled wearable and assistive technology, for seamless control in real-time, to regain natural gait cycle followed by a minimal probability of non-volitional commands, and possible future developments in these applications, are discussed in the last section.

GENERAL CONTROL FRAMEWORK FOR BCI WEARABLE LOWER-LIMB AND ASSISTIVE-ROBOT DEVICES

In order to structure the control architecture adopted by various BCI wearable LL and assistive robot-devices, a general framework is presented in Figure 2. This framework was extended from Tucker et al. (2015) applicable to a range of EEG-BCI controlled devices for LL assistance, including portable exoskeletons, orthosis, prosthesis, and assistive-robots (wheelchairs, humanoids, and navigation/telepresence robots).

Figure 2 reﬂects the generalized control framework, where electrophysiological and transduced signal interactions, along the feedforward and feedback loops, are shown for motion intent recognition, during activity mode. Integral parts of the framework include a user of the assistive robot-device, the assistive-robot device itself, a BCI operator structure with sublevel controls, shared control, communication protocol and the interaction with environment. The BCI operator structure constitutes of three sub-layers which are the feature extraction, translation and execution layer, respectively. As a precaution to ensure human-robot interaction safety, safety layers are used

|[Figure 2]<br><br>FIGURE 2 | Generalized framework in BCI controlled wearable LL and assistive devices for rehabilitation.|
|---|

with the user and the robotic device parts of the framework. The control framework is in a generalized form applicable to all brain-controlled assistive robots.

BCI control is driven from the recognition of user’s motion intentions; therefore we begin from the point of origin where motion intentions arise (cortical levels). The ﬁrst step involves how to perceive and interpret the user’s physiological state (i.e., MI/ME or ERP) acquired via EEG. Following this, the status of physical interaction between the user and the environment (and vice versa), and the robotic device and the environment (and vice versa) are checked. The assistive-robot’s state is determined via electromechanical sensors. The user and assistiverobot status inputs to the BCI operator and shared controller, respectively.

Raw signals from the user and assistive LL device pass through the communication protocol which directs them to the connected client i.e., BCI operator via pre-processing and shared control module. Real-time signal acquisition and operating software could be used to assign event markers to the recorded data e.g., OpenViBE, BioSig, BCI++, BCI2000 etc. (Schalk et al., 2004; Mellinger and Schalk, 2007; Renard et al., 2010). The streaming connection can be made using TCP (when the time synchronization requirements do not need accuracy <100ms) or LSL which incorporates built-in network and synchronization capabilities (with accuracy of 1ms) recommended for applications based on ERPs.

Under the control framework components, BCI operator is the core part comprising of three sub layers, described in detail in section BCI Operator.

At feature extraction layer (intent recognition), user’s intent of activities related to LL movements are perceived, discerned and interpreted. Signal features associated to user’s kinesthetic intent/execution of motor task (in case of SMR) are encoded

in form of feature vector (Lotte, 2014). The activity-mode recognition for ERP, against displayed oddball menu for speciﬁc location, uses frequency, or time domain features. It is the user’s direct volitional control that lets voluntarily manipulate the state of the device (e.g., joint position, speed, velocity and torque).

Translation layer (weighted class) takes account of the translation of extracted signal features to manipulate the robotic device, via machine understandable commands, which carry the user’s intent. This is done by supervised, or unsupervised learning (classiﬁcation algorithm) which essentially estimates the weighted class, represented by the feature vector, and identiﬁes the cognitive patterns for mapping to the desired state (unique command).

The desired state of user intent is carried to the execution layer (commands for device-speciﬁc control) where an error approximation is done with reference to current state. The state of the device is also sent to the execution layer via shared controller, as a feedforward control, in order to comply with the execution layer. The execution layer sends control commands to the actuator(s) of the device and visual feedback to the user via shared control unit in order to minimize the possible error. The feedback control plays a vital role in achieving the required output (usually accounts for the kinematic or kinetic properties of the robot-device).

This closes the overall control loop and the robotic device actuates to perform the required task(s). As the wearable assistive-robot is physically placed in close contact with the user, and that the powered device is likely to generate output force, safety mechanisms are kept into consideration with the user and hardware in the control framework. Inter-networking between subsystems of the generalized control architecture relies on the exchange of information sent at signal-level as well as physical-level.

USER ADAPTABILITY AND EEG SIGNAL ACQUISITION

time for the visual stimulus to travel from the eye to occipital cortex.

Users can generally be grouped based on their physical and mental state, for instance locked-in patients with intact eye muscles, can communicate via ERP signals, whereas patients with motor complete but sensory incomplete SCI can utilize SMR signals based on MI. Figure 3 shows the electrophysiological signals that are extensively employed by BCI system for communication; however EEG signals employed by the wearable LL and assistive devices are highlighted for this study.

The type of BCI is directed based on the user’s lesion level and extent of adaptability to adhere with the speciﬁc BCI protocol.

User Adaptability

In order for the portable LL wearable-BCI controllers to be compliant with residual neuromusculoskeletal structures, the sensorimotor control loop of human locomotion is taken into account, since the volitional and reﬂex-dependent modulation of these locomotion patterns emerges at the cortical levels (Armstrong, 1988; Kautz and Patten, 2005; Bakker et al., 2007; Zelenin et al., 2011; Pons et al., 2013; Angeli et al., 2014; Marlinski and Beloozerova, 2014; Capogrosso et al., 2016). This may essentially preclude the direct control of LL via neural activity alone, while keeping a balance and orientation during dynamic tasks. However, the sole employment of cortical activity is still useful for providing high-level commands to the controller of the device to execute volitional movements (Carlson and Millan, 2013; Contreras-Vidal and Grossman, 2013; Kilicarslan et al.,

Deployed Oscillatory Rhythms

For assistive devices, the two commonly used SMR acquired from the motor cortex are mu (8–11Hz) and beta (12–30Hz) rhythms, which elicit upon ME/MI tasks. The ME task is based on the physical motion of the user’s limbs that activate the motor cortex; this includes the development of muscular tension, contraction or ﬂexion. The MI is a covert cognitive process based on the kinesthetic imagination of the user’s own limb movement with no muscular activity also termed “kinesthetic motor imagery” (KMI) (Mokienko et al., 2013). Motor tasks can generally be upper or lower limb related (Malouin et al., 2008). The upper limb motor tasks activate hand area (Vasilyev et al., 2017) and LL motor tasks activate foot representation area of the cortex respectively (Wolpaw and Wolpaw, 2012). The advantage with MI signals is that they are free of proprioceptive feedback unlike ME tasks.

- 2013), for patients whose injuries necessitate a direct input from cortex to the robotic device controller. Therefore, the critical aspect for a functional portable LL device is the lesion measure and the physiological constraints based on which the user can adapt to the BCI protocol. The physiological constraints in such cases can be compensated through assistance, like shared control.

EEG Signal Acquisition

The neuronal activity can be divided into spikes and ﬁeld potentials. Spikes show action potentials of neurons individually and are detected via invasive microelectrodes. Field potentials on the other hand can be measured by EEG and they reﬂect the combined synaptic, axonal and neuronal activity of the neuron groups (Yang et al., 2014; He, 2016).

The communication components in EEG activity useful for BCI include, the oscillatory activity comprising of delta, theta, alpha/mu, beta and gamma rhythms; the ERP (P300), the VEP, and slow cortical potentials (SCP). Oscillatory rhythms ﬂuctuate according to the states of brain activity; some rhythms are distinguished depending on these states (Semmlow and Griﬀel,

- 2014). The Mu and beta rhythms are also termed SMR. The SMR elicit event-related desynchronization (ERD) or event-related synchronization (ERS) which are directly related to proportional power decrease upon ME/MI of limb(s) movement or power increase in the signal upon rest, respectively; they are nonphase locked signals (Kalcher and Pfurtscheller, 1995). Evoked potentials on the other hand are phase-locked. A BCI system employs evoked potentials when requiring less or no training from the user i.e., a system based on stimulus-evoked EEG signals that provides task-relevant information (Baykara et al., 2016), useful for locked-in or multiple sclerosis patients. This involves the presentation of an odd-ball paradigm in case of P300 or multiple visual stimuli ﬂashing, e.g., letters, digits on screen in case of VEP. The P300 is derived from user response that evokes approximately 300ms after stimulus triggering and corresponds to positive voltage peak (Lazarou et al., 2018). VEP measures the

It was suggested by Wolpaw and Mcfarland (2004), that the use of mu and beta rhythms could give similar results as those presented by invasive methods for motor substitution. A non-invasive BCI could clinically support medical device applications (as discussed in section Lower-Limb Assistive-Robot Applications in Diﬀerent Environments). The BCIs for control of medical device applications are reported in Allison et al. (2007); Daly and Wolpaw (2008), and Frolov et al. (2017). It was observed that BCI employed by assistive-robot devices for control purposes was focused on upper limb MI (Belda-Lois et al.,

|[Figure 3]<br><br>FIGURE 3 | Electrophysiological signals used in BCI controlled wearable LL and assistive-robot devices.|
|---|

2011) such as hand and ﬁngers, for applications including BCI hand orthotics and exoskeleton (Schwartz et al., 2006; Soekadar et al., 2015). This is because the foot representation area is near the mantelkante, which is situated deep within interhemispheric ﬁssure of the human sensorimotor cortex (Penﬁeld and Boldrey, 1937). However, it never withheld progress into this direction. Research on LL, precisely the foot MI/ME for controlling assistive robots, is in progress (Pfurtscheller et al., 2006a; Hashimoto and Ushiba, 2013; Tariq et al., 2017b, 2018). It was proved that the induction of beta ERS in addition to mu-beta ERD, improved the discrimination between left and right foot imagery and stepping tasks, as accurate as hand MI (Pfurtscheller et al., 2005, 2006a; Pfurtscheller and Solis-Escalante, 2009; Hashimoto and Ushiba, 2013; Liu et al., 2018) which provides a basis for research in BCI controlled foot neuroprosthesis. To our knowledge no literature on explicit employment of knee or hip KMI tasks in any BCI experimental protocol is available except for (Tariq et al., 2017a).

Besides the KMI of LL, cortical signals arising from the sensorimotor control loop of human locomotion intent is taken into account, for the portable LL wearable-BCI controllers to be compliant with the residual neuromusculoskeletal structures (La Fougere et al., 2010) suggested that brain areas underlying walking MI overlie the supplementary motor area and prefrontal cortex. The idea of walking from thought based on foot imagery has also been presented in Pfurtscheller et al. (2006b). A novel way of therapy that earlier provided limited grade of motor-function recovery for chronic gait function impaired subjects due to foot-drop was described (Do et al., 2011, 2012). They integrated EEG-based BCI with non-invasive functional electrical stimulation (FES) system. It resulted in enabling the brain-control of foot dorsiﬂexion directly in healthy individuals. Takahashi et al. (2009, 2012) validated the feasibility of shortterm training by employing ERD and FES based on dorsiﬂexion of paralyzed ankle experiments. Beta corticomuscular coherence (CMC) gave a measure of communication amid sensorimotor cortex and muscles. García-Cossio et al. (2015) demonstrated the possibility to decode walking intentions from cortical patterns. Raethjen et al. (2008) found coherence in EEG at stepping frequency and electromyography (EMG) anterior tibial muscles pattern for rhythmic foot movements.

Work on analyzing EEG signals for detection of unexpected obstacles during walking was presented recently (Salazar-Varas et al., 2015). Observation of electrocortical activity related to walking gait-cycle and balancing experiments has been reported in Presacco et al. (2011b). Electrocortical activity resulting from gait-like movements and balancing with treadmill, Erigo R tilt table, and customized stationary bicycle with rigid reclined backboard (as pedaling device) have been discussed in Wieser

- et al. (2010), Gwin et al. (2011), Presacco et al. (2011a), Jain et al. (2013), Petrofsky and Khowailed (2014), Bulea et al. (2015), Kumar et al. (2015), and Liu et al. (2015).

Deployed Event-Related and Evoked Potentials

ERPs have successfully been deployed in ambulatory and motor conditions without aﬀecting the recorded EEG data. P300 showed to improve the performance of an EEG-based BCI system

during ambulatory conditions or foot dorsiﬂexion/plantarﬂexion condition (Lotte et al., 2009; Castermans et al., 2011b; Duvinage et al., 2012). They used similar experimental protocol i.e., oddball paradigm while subjects were physically walking or moving feet in dorsiﬂexion or plantar-ﬂexion direction. In addition to this, the somatosensory evoked potentials (SEP) were deployed in assistive technologies. These potentials commonly elicit by bipolar transcutaneous electrical stimulation applied on the skin over the trajectory of peripheral nerves of the upper limb (the median nerve) or LL (the posterior tibial nerve), and then recorded from the scalp (Sczesny-Kaiser et al., 2015). In addition to the wearable devices, assistive technologies as EEG-BCI controlled wheelchairs and humanoid robots have successfully deployed the P300 (Rebsamen et al., 2007, 2010; Pires et al., 2008; Iturrate et al., 2009b; Palankar et al., 2009; Lopes et al., 2011; Kaufmann et al., 2014) and VEP signals (Bell et al., 2008). However, the only drawback, with employment of ERP and VEP signals in a BCI for the control of assistive devices precisely wearables, is the presence of visual stimulus set-up within the device that makes it less convenient for portable applications.

## COMMUNICATION PROTOCOL

Like a basic communication system, the BCI for control of assistive devices has an input, an output, translation components for converting input to output, and a protocol responsible for the real-time operation onset, oﬀset and timing.

Acquired EEG signals are transferred to the BCI operator via a communication protocol. Similarly sensor output from the robot device is directed to the shared control unit via communication protocol, Figure 2. Communication protocol could be a transmission control/internet protocol (TCP/IP), a suite of communication protocols used to interconnect network devices on the internet or a private network. For instance, in EEG-BCI controlled humanoids, the data (visual feedback images from the humanoid monocular camera and motion commands from the BCI system) were transmitted using wireless TCP/IP communication between the humanoid and other systems (Chae et al., 2011a,b, 2012).

An alternate approach is the lab streaming layer (LSL), which allows synchronization of the streaming data across devices. Information can be streamed over the network from “Presentation to the LSL” (Iturrate et al., 2009b; Renard et al., 2010; Kothe and Makeig, 2013; Gramann et al., 2014). Recent assistive applications (Galán et al., 2008; Millán et al., 2009) such as wheelchairs, and mobile robots, use controller area network (CAN) bus which is a robust vehicle bus standard. It is designed to allow microcontrollers and devices to communicate in applications without a host computer and follows a messagebased protocol. It is a low cost, fault tolerant communication system, with the data transfer rates in the range of 40 Kbit/s to 1 Mbit/s.

## BCI OPERATOR

After passing through the communication protocol, acquired EEG signals are directed to connected

client, i.e., the BCI operator, but are pre-processed ﬁrst.

Preprocessing

The acquired raw EEG signals are pre-processed, as they are susceptible to noise and artifacts. It could be hardware/environmental noise, experimental error or physiological artifact. As hardware and environmental noise are not brain-related, it is best to remove them before converting raw EEG to signal features.

Removal of Noise

Hardware noise in the EEG signal usually occurs due to instrument degradation, electrode wear, mains interference (AC power lines), electromagnetic wave sources as computers, mobile phones, notebooks, wireless routers or other electronic equipment. High noise frequencies in the signal can be removed by notch ﬁlters (50 or 60Hz for power lines). To block electromagnetic waves, electromagnetic shields could be used.

Removal of Artifacts

EEG artifacts arise due to physiological activities such as skin impedance ﬂuctuations, electrooculography activity, eye blinks, electrocardiographic activity, facial/body muscle EMG activity and respiration. As the frequency ranges, for the aforementioned physiological signals are typically known, the bandpass ﬁlter can be an eﬀective preprocessing tool. Most EEG-based BCI systems for assistive technologies have shown the successful implementation of simple low-pass, high-pass, or bandpass ﬁlters to remove physiological artifacts. Other methods for artifact removal include temporal ﬁltering, spatial ﬁltering, independent component analysis (ICA) (Viola et al., 2009), principal component analysis (PCA), linear regression, blind source separation (BSS) (Ferdousy et al., 2010), wavelet transform, autoregressive moving average, nonlinear adaptive ﬁltering, source dipole analysis (Fatourechi et al., 2007) or thresholding of meaningful parameters (e.g., channel variance) based on a prior statistical analysis (Nolan et al., 2010).

Feature Extraction Layer

After preprocessing of data, diﬀerent brain activities are classiﬁed based on their selected features.

Band Power Features

The band power features, usually used, are the time-frequency components of ERD/ERS. After bandpass ﬁltering, resulting signal is squared to obtain its power p[t] = x2 [t], where x is the ﬁltered single band EEG signal amplitudes and p is the resulting band-power values. To smooth-out (average) the signal, a wsized smoothing window operation is used. This is followed by a logarithm of the processed signal sample, using Equation 1:

p[n] = ln

w

1 w

p[n − k] (1)

k=0

where p[n] are the smoothed band-power values, and w is the smoothing window size. In their work (Presacco et al., 2011b; Contreras-Vidal and Grossman, 2013), the feature extraction

method employed by EEG-BCI lower exoskeleton, for neural decoding of walking pattern, included power spectral density (PSD) analysis of the kinematic data and adaptive Thompson’s multitaper for each channel of EEG recorded, during rest and walking tasks. Decoding method employed a time-embedded linear Wiener ﬁlter, independently designed and cross-validated for each extracted gait pattern. Parameters of the model were calculated with Gaussian distribution method. This ensured the feasibility of successfully decoding human gait patterns with EEG-BCI LL exoskeleton. Similarly, the results tested a on paraplegic subject for BCI controlled lower exoskeleton (Kilicarslan et al., 2013) reﬂect the method of decoding closed loop implementation structure of user intent with evaluation accuracy of 98%. Data was ﬁltered in delta band (0.1–2Hz) using 2nd order Butterworth ﬁlter. The ﬁltered data was standardized and separate channels were used, to create feature matrix to extract delta band features.

In 2012 (Noda et al., 2012) proposed an exoskeleton robot that could assist user stand-up movements. For online decoding they used 9th order Butterworth ﬁlter for 7–30Hz band. After down-sampling, Laplace ﬁlter and common average subtraction were applied for voltage bias removal. The covariance matrix of the processed data was used as input variable for the twoclass classiﬁer; the results were productive. Other EEG-BCI lower exoskeletons (Gancet et al., 2011, 2012) considered employing steady-state VEP (SSVEP) for motion intention recognition. Proprioceptive artifacts removal (during walk) is aimed to be removed using ICA. Other recent work on LL exoskeleton controlled via SSVEP includes (Kwak et al., 2015). In the SEPcontrolled LL exoskeleton (Sczesny-Kaiser et al., 2015), SEP signals were sampled at 5kHz and bandpass ﬁltered between 2 and 1,000Hz. In total 800 evoked potentials were recorded in epochs from 30 before to 150ms after the stimulus, and then averaged. Paired-pulse suppression was expressed as a ratio of the amplitudes of second and ﬁrst peaks, which was the primary outcome parameter. For correlation analysis, they calculated the diﬀerence of mean amplitude ratios.

For a BCI controlled robotic gait orthosis (Do et al., 2011, 2013) an EEG prediction model was generated to exclude EEG channels with excessive artifacts. The EEG epochs corresponding to idling and walking states were then transformed into frequency domain, their PSD were integrated over 2Hz bins, followed by dimensionality reduction using class-wise principal component analysis (CPCA). The results established feasibility of the application.

BCI and shared control wheelchairs, based on MI signals to ensure interference free navigation protocol, was presented in Millán et al. (2009) and Carlson and Millan (2013). They estimated PSD in the 4–48Hz band with a 2Hz resolution. ERD was observed in the mu band power 8–13Hz. These changes were detected by estimating the PSD features every 16 times/s using Welch method with ﬁve overlapped (25%) Hanning windows of 500ms. In order to select subject-speciﬁc features, that maximize the separability between diﬀerent tasks (based on training data cross validation) the canonical variate analysis (CVA) was used. In a similar work presented by Galán et al. (2008) for BCI controlled wheelchair, feature selection

was done by picking stable frequency components. The stability of frequency components was assessed using CVA one per frequency component on the training set.

Time-Domain Parameters

The time-domain parameters compute time-varying power of the ﬁrst k derivatives of the signal; pi (t) = didtx(it) where i = 0, 1,..., k and x is the initial EEG signal. Resulting derivatives are smoothed using exponential moving average and logarithm, used in feature vector generation, as given in Equation 2:

pi [n] = ln upi [n] − (1 − u)pi [n − 1] (2)

where p is the smoothed signal derivatives, u is the moving average parameter, u ∈ [0;1].

EEG-BCI for control of LL orthosis (Taylor et al., 2001; Duvinage et al., 2012) combined a human gait model based on a CPG and a classic but virtual P300 to decipher user’s intent for four diﬀerent speeds. P300 was used to control the CPG model and the orthosis device by sending high-level commands. The frequency band for P300 were high-pass ﬁltered (temporal) at 1Hz cut oﬀ frequency using 4th order Butterworth ﬁlter. This was followed by designing of an xDAWN-based spatial ﬁlter, by linearly combining EEG channels. When EEG signals were projected into this subspace, P300 detection was enhanced. The resulting signal was epoched using time window that started after stimulus, averaged and sent to the classiﬁer. In another related work (Lotte et al., 2009), the epoching of P300 signal was done by selection of related time window, followed by bandpass ﬁltering in 1–12Hz range using 4th order Butterworth ﬁlter. Post this; winsorizing for each channel was done by replacing values within 5% most extreme values by most extreme values from remaining 95% samples from that window. A subset of the features was selected using the sequential forward ﬂoating (SFFS) feature selection algorithm that ensured the maximization of performance of the BCI system.

The EEG-BCI for foot orthosis reported in Xu et al. (2014), employed bandpass ﬁltering (0–3Hz). The system was based on the detection of movement-related cortical potentials (MRCP). The data between 0.5 and before 1.5s, after the movements, were extracted as the “signal intervals” while others were extracted as the “noise intervals.” The measure analysis of variance, ANOVA, was used for statistical analysis.

The P300-BCI wheelchair incorporated bandpass ﬁltering between 0.5 and 30Hz and characterized the P300 signal in the time domain. For each EEG channel, 1-s sample recordings were extracted after each stimulus onset and ﬁltered using the moving average technique. The resulting data segments for each channel selected were concatenated, creating a single-feature vector (Iturrate et al., 2009a,b).

Common Spatial Patterns

The common spatial pattern (CSP) features are sourced from a preprocessing technique (ﬁlter) used to separate a multivariate signal into subcomponents that have maximum diﬀerences in variance (Müller-Gerking et al., 1999). The diﬀerence allows

simple signal classiﬁcation. Generally, the ﬁlter can be described as a spatial coeﬃcient matrix W, as shown in Equation 3:

### S=WTE (3)

where S is the ﬁltered signal matrix, E is the original EEG signal vector. Columns of W denote spatial ﬁlters, while WT are the spatial patterns of EEG signal. In their work (Choi and Cichocki, 2008) used SMR to control wheelchair. For pre-processing they employed the second order BSS algorithm using a modiﬁed and improved real-time AMUSE algorithm that enabled a rapid and reliable estimation of independent components with automatic ranking (sorting) according to their increasing frequency contents and/or decreased linear predictability. The AMUSE algorithm worked as 2 consecutive PCAs; one applied to the input data and the second applied to the time-delayed covariance matrix of the output from the previous stage. For feature extraction, CSP ﬁlter was used that distinguish each data group optimally from the multichannel EEG signals.

SMR-based humanoid robots used the KMI of left hand, right hand, and foot as control signals (Chae et al., 2011b, 2012). Sampled EEG signals were spatially ﬁltered with large Laplacian ﬁlter. During the overall BCI protocols, Laplacian waveforms were subjected to an autoregressive spectral analysis. For amplitude features extraction, every 250ms observation segment was analyzed by the autoregressive algorithm, and the square root of power in 1Hz wide frequency bands within 4– 36Hz was calculated.

Translation Layer

After passing through the feature extraction layer, the feature vector is directed to the translation layer to identify user intent brain signals, and manipulate the robotic device via machine understandable commands for interfacing. Diﬀerent classiﬁcation techniques for distinct features are used. Classiﬁcation algorithms, calibrated via supervised or unsupervised learning, during training phase, are able to detect brain-signal patterns during the testing stage. This essentially estimates the weighted class, represented by the feature vector for mapping to the desired state (unique command). A recent review on most commonly used classiﬁcation algorithms for EEG-BCIs has been reported by (Lotte et al., 2018). Some of the commonly used classiﬁcation methods in EEG-BCI controllers for LL assistance are LDA, SVM, GMM, and ANN (Delorme et al., 2010, 2011).

Linear Discriminant Analysis

One of the most extensive and successfully deployed classiﬁcation algorithms, in EEG-BCI for assistive technologies is the linear discriminant analysis (LDA). The method employs discriminant hyper-plane(s) in order to separate data representing two or more classes. Since it has low computational requirements, it is most suitable for online BCI systems. A feature a can be projected onto a direction deﬁned by a unit vector ωˆ, resulting in a scalar projection b, given by Equation 4:

b = ⇀a · ωˆ 2 (4)

The aim of LDA classiﬁcation is to ﬁnd a direction ωˆ, such that, when projecting the data onto ωˆ it maximizes the distance between the means and minimizes the variance of the two classes (dimensionality reduction). It assumes a normal data distribution along with an equal covariance matrix for both classes (Lotte et al., 2007). LDA minimizes the expression given by Equation 5:

mφ − m 2 s2φ + s2

(5)

where mφ and m are the means and sφ and s are the standard deviations of the two respective classes, after projecting the features onto ωˆ. EEG-BCI lower exoskeletons used LDA for the reduction of data dimensionality (Kilicarslan et al., 2013). EEG-BCI lower orthosis employed a 12-fold LDA using voting rule for decision making in selection of speed (Lotte et al., 2009; Duvinage et al., 2012). Dimensionality reduction, using CPCA and approximate information discriminant analysis (AIDA), were used in the robotic gait orthosis system (Do et al., 2011, 2013). The BCI-driven orthosis (Xu et al., 2014) used the manifold based non-linear dimensionality reduction method, called locality preserving projection (LPP), along with LDA, to detect MRCPs. EEG-BCI wheelchairs successfully deployed LDA (Galán et al., 2008; Iturrate et al., 2009a,b). LDA was successfully used for translation of EEG signal into movement commands in humanoids (Chae et al., 2011a,b, 2012).

Support Vector Machine

The goal of SVM classiﬁer is to maximize the distance between the separating hyper plane and the nearest training point(s) also termed support vectors. The separating hyper plane in the 2D feature space is given by the Equation 6:

y =ωTx +b (6)

where ω, x ∈ R2 and b ∈ R1. The hyper plane (also called the decision border) divides the feature space into two parts. Classiﬁed results depend on which side of the hyper plane the example is located. In SVM, the distances between a hyper plane and the nearest examples are called margins.

Though SVM is a linear classiﬁer, it can be made with nonlinear decision boundaries using non-linear kernel functions, such as Gaussian or radial basis functions (known as RBF). The non-linear SVM oﬀers a more ﬂexible decision boundary, resulting in an increase in classiﬁcation accuracy. The kernel functions, however, could be computationally more demanding. EEG-BCI wheelchairs have successfully used linear SVM for dynamic feature classiﬁcation (Bell et al., 2008; Choi and Cichocki, 2008; Ferreira et al., 2008; Rebsamen et al., 2010; Belluomo et al., 2011). It was also successfully implemented in EEG-BCI humanoid (Bell et al., 2008) and mobile robots (Ferreira et al., 2008; Belluomo et al., 2011).

Gaussian Mixture Model

The GMM is an unsupervised classiﬁer. This implies that the training samples of a classiﬁer are not labeled to show their class. More precisely, what makes GMM unsupervised is that during

the training of the classiﬁer, estimation is done for the underlying probability density functions of the observations (Scherrer, 2007). Several EEG-BCI applications utilized the GMM as a feature classiﬁer, such as lower exoskeletons, wheelchairs and mobile robots (Galán et al., 2008; Millán et al., 2009; Carlson and Millan, 2013; Kilicarslan et al., 2013).

Artiﬁcial Neural Network

The ANNs are non-linear classiﬁers inspired by human’s nervous system ability to adaptively react to changes in surroundings. They are commonly used in pattern recognition problems, due to their post-training capability to recognize sets of training-data-related patterns. ANNs comprise of assemblies of artiﬁcial neurons that allow the drawing of non-linear decision boundaries. They can be used in diﬀerent algorithms including multilayer perception, Gaussian classiﬁer, learning vector quantization, RBF neural networks, etc. (Anthony and Bartlett, 2009). In their proposed model for lower exoskeleton (Gancet et al., 2011, 2012), they aim at adopting processing method as dynamic recurrent neural network (DRNN).

Execution Layer

Once classiﬁed, the desired state of user intent is carried to the execution layer for an error approximation. The approximation in reference to the present state of the device is used to drive the actuator for reducing any error. The execution layer of control is highly device-speciﬁc. It could rely on feedforward or feedback loops (Tucker et al., 2015).

Feedforward control needs some model to predict the system’s future state, based on the past and present set of inputs and the device state. Aforementioned control inputs can be eﬀective for reducing the undesired interaction forces, that could occur due to the added mass, inertia and friction of the device (Murray and Goldfarb, 2012). On the contrary feedback controllers do not require a model of the system, but require an estimate of the current state. The controller compares current state with the desired state of the device and modulates the power input to the device accordingly (Millán et al., 2009; Duvinage et al., 2012; Noda et al., 2012; Contreras-Vidal and Grossman, 2013; Do et al., 2013; Kilicarslan et al., 2013; Xu et al., 2014; Contreras-Vidal et al., 2016).

## SHARED CONTROL

Shared control is used to couple the user’s intelligence, i.e., cognitive signals with precise capabilities of the robotic device given the context of surroundings, resulting in reduced workload for the user to continuously deliver commands to drive the robotic device. Inputs to the shared control module are sensory readings of the robotic device and output of the BCI operator (classiﬁed signal). The classiﬁed signal is combined with the robot’s precise parameter e.g., velocity to generate smoother driving output. Several assistive technologies for motor impairment have successfully employed shared controllers for navigational assistance to maneuver the assistive devices in diﬀerent directions, independently and safely (Galán et al., 2008;

Millán et al., 2009; Tonin et al., 2010, 2011; Carlson and Millan, 2013).

This refers to the idea of switching between operators, i.e., if the user needs no navigational assistance he will be granted full control over the robotic device; otherwise, sole mental commands will be used and modiﬁed by the system. One key aspect of shared control is the two-way communication between the human and the robot. The shared control is beneﬁcial primarily for navigational directions. In the case of robots with only three possible steering mental commands such as forward, left, and right, there is a need of assistance by the device for ﬁne maneuvering. Secondly, the cognitive commands might not always be perfect, i.e., could be vague. In the case of errors, an extra navigational safety is required by the system to interpret the meaning of the command. In this way the system would be able to perceive any new environment.

LOWER-LIMB ASSISTIVE-ROBOT APPLICATIONS IN DIFFERENT ENVIRONMENTS

The last integral part, of the control framework, is the robotic device, as observed in Figure 2. In this section, the current stateof-the-art EEG-based activity mode recognition in a BCI for control of LL assistive devices is summarized in Table 1.

BCI Exoskeletons

In order to control a LL robotic exoskeleton (NeuroRex), Contreras-Vidal and Grossman (2013) and Kilicarslan et al. (2013) decoded neural data for human walking from Presacco

- et al. (2011b). They evaluated the degree of cognitive-motor-body adaptations while using portable robot. Their results proved that NeuroRex can be regarded as an augmented system of locomotor therapy (LT) by reviewing its initial validation in a paraplegic patient having SCI. They also performed comprehensive clinic assessments for user safety protection.

The MINDWALKER (Gancet et al., 2011, 2012) is another project where researchers proposed a novel idea of presenting the SCI patients with intact brain capabilities. The facility of crutchless assistive LL exoskeleton is based on brain neural-computer interface (BNCI) control for balanced walking patterns. It also evaluated the potential eﬀects of Virtual Reality (VR) based technology that could support patient/user training for reaching a high conﬁdence level for controlling the exoskeleton virtually before the real transition. Other brain controlled exoskeletons are reported in Noda et al. (2012), Kwak et al. (2015), Sczesny-Kaiser et al. (2015), and Lee et al. (2017).

BCI Orthosis

EEG-based activity mode recognition for orthotic devices has been investigated by Duvinage et al. (2012). They proved the concept of considering user’s intent by combining CPG-based human gait model and classic P300-BCI for ﬁve diﬀerent states; three speed variations, a stop state and a non-control state. Using unnatural P300 command by augmented reality eyewear (from Vuzix, Rchester, USA) decision was sent to

the Virtual Reality Peripheral Network (VRPN) server to be exploited while wearing LL orthosis. This was based on the pilot study carried by Lotte et al. (2009), where a solution to the constraints, such as deterioration of signals (during ambulation), was avoided by using slow P300 for control during sitting, walking and standing. Authors of Castermans et al. (2011a) used an experimental protocol to limit movement artifacts present in EEG signals compared to real walk on treadmill. They suggested that rhythmic EEG activity could be exploited for driving a user intent-based foot-ankle orthosis built on PCPG algorithm. Similar investigation was conducted by Raethjen et al. (2008).

In their work, Do et al. (2013) proposed a novel approach of BCI controlled lower extremity orthotics to restore LL ambulation for partially and complete SCI subjects suﬀering from cardiovascular disease, osteoporosis, metabolic derangements and pressure ulcers. They developed an EEG prediction model to operate the BCI online and tested the commercial robotic gait orthosis system (RoGO) for two states, idling and walking KMI. Similarly, testing for intuitive and self-paced control of ambulation was also done with an avatar in a virtual reality environment (VRE) (Wang et al., 2012; King et al., 2013). Other similar investigations are reported in Wang et al. (2010) and Do et al. (2011).

The BCI driven motorized ankle-foot orthoses, known as (BCI-MAFO), intended for stroke rehabilitation was presented in Xu et al. (2014). Their system was able to detect imaginary dorsiﬂexion movements (for walking gait) within a short latency, by analyzing MRCPs. Upon each detection, the MAFO was triggered to elicit passive dorsiﬂexion, hence, providing the user a binary control of robotic orthosis. The MEP was elicited by transcranial magnetic stimulation (TMS); the results reﬂected an eﬀective way to induce cortical plasticity for motor function rehabilitation.

BCI Wheelchairs, Humanoids, and Mobile Robots

Assistive technologies such as wheelchairs controlled via EEGBCI have extensively been researched. In their work, Carlson and Millan (2013) proposed the idea of combining a commercial wheelchair and BCI with a shared control protocol. The paradigm was based on KMI of left/right hand, both feet, or in idle state; each against three distinct tasks as move left/right or forward by avoiding obstacles. Modiﬁcations in the commercial mid-wheel drive model (by Invacare Corporation) were directly controlled by a laptop. An interface module, based on remote joystick, was used between the laptop and wheelchair’s CANBUSbased control network. Wheel-encoders were added for motion feedback alongside sonar sensors and webcams for environment feedback to the controller using cheap sensors compared to other systems. Previous solution required continuous commands from the user, in order to drive the wheelchair, that ended up in high user workload (Millán et al., 2009). Other similar systems were proposed by Vanacker et al. (2007) and Galán et al. (2008).

Research on the challenges faced during fully control automated wheelchairs with BCI was done by Rebsamen et al. (2007, 2010). Their results proved that if synchronous evoked

Gancetetal.,2011,2012;Kwak

Contreras-VidalandGrossman,

2013;Kilicarslanetal.,2013

Lotteetal.,2009;Duvinage

Sczesny-Kaiseretal.,2015

Nodaetal.,2012;

applications References

etal.,2015

etal.,2012

onuserintentcontrolforwalking

Aﬁve-statefootlifterorthosisfor

forSCIpatientswithintactbrain

bodyweightsupportedtreadmill

Lowerbodyexoskeletonbased

walkingfunctioninSCIpatients

empowering(dynamicbalance)

independentlyforsubjectswith

stateforstrokepatientsunable

sitting,standingandwalkingat

training(BWSTT)forimproving

fourspeeds&anon-control

®HALexoskeleton-assisted

tolifttheirfeetorfootdrop

paraplegia,strokeandSCI

problemsPilotstudyfor

Crutch-lessassistiveLL

paraparesis,complete

(%) KeyﬁndingsTypeofsupportand

exoskeletonforwalk

ambulatoryBCI

capabilities

P300basedBCItoconsider

walkingpatternandpaceas

backing,turning,ascending

-,-,92.6%(online)Exploitationofmotorcortex

imaginedbyuserdeploying

widelyusedinroboticsand

self-balancing,walkingand

augmentedrealityeyewear

robotic-assistedBWSTTin

Norequiredtrainingbythe

EEGsignalsforgenerating

SEPBandpassﬁlter-Signiﬁcantimprovementin

inducingcorticalplasticity

SCIpatientsiscapableof

usertomanagetheP300

followinghighlyrepetitive,

patientscomparedtothe

automaticallygeneratea

anglescorrespondingto

activelocomotiveuseof

combiningahumangait

paired-pulseSEPinSCI

LocomotorTherapy(LT)

(walking) Proofoftheconceptof

TABLE1|KeyfeaturesofEEG-basedactivitymoderecognitionexoskeletons,orthosis,wheelchairsandassistiverobotsforrehabilitation.

pattern/behaviorofthe

patientandhisdesired

Anaugmentedformof

anddescendingstairs

paradigmprovidedby

onlinelegskinematics

followingtraining.The

modelbasedonCPG

ThisCPGallowedto

forexternalstimulus

controlsatbaseline

PSDanalysis GMM,LDA-,90(GMM),-Forstanding-up,>

presentation.

user’sintent.

applications.

periodicgait

pareticlegs.

speed.

VR

fordecisionmaking) 8315.5%(walking)75%±

ClassiﬁerClassiﬁ-cationaccuracy

LDA(usingvotingrule

SSVEP*ICADRNNChéronetal.,

2011,KNN

etal.,2009,epoch

DevicesBrainactivityPre-processing

spatialﬁlterRivet

averaging,SFFS

rhythms Bandpassﬁlter,

high-passﬁlter,

xDAWN-based

andfeature

extraction

P300*Temporal

NeuroRexOscillatory

skeleton

WALK-

MIND-

®HAL

State

Lifter

Five-

Exo-

Foot

ER

Piresetal.,2008;Iturrateetal.,

2009a,b;Palankaretal.,2009;

etal.,2008;Millánetal.,2009;

Rebsamenetal.,2007,2010;

Lopesetal.,2011;Kaufmann

Vanackeretal.,2007;Galán

Wangetal.,2010;Doetal.,

CarlsonandMillan,2013

Xuetal.,2014

applications References

2011,2013

etal.,2014

BCIRoboticgaitorthosisforSCI,

experienced/inexperiencedusers

houseishighlightedbystandard

BCI-drivenmotorizedankle-foot

orthosis(MAFO).Anambulatory

patientstoimproveneurological

surroundingsas,toilet,kitchen,

BCIwheelchairforlocked-inor

Brain-actuatedwheelchairfor

standardtherapytoimprove

bedroomandlivingroomin

rehabilitation-toolforstroke

operatewithevencomplex

outcomesbeyondthoseof

tetraplegia,andparaplegia

tocontinuouslyandsafely

userswithseveremobility

navigationindependently

wheelchairwhereknown

impairment.Suitablefor

IntelligentandsafeBCI

(%) KeyﬁndingsTypeofsupportand

oddballparadigm.

ALSpatients.

ambulation

patients

sharedcontrol,comparedto

forwardandavoidobstacles

LPPandLDA7310.3%.Efﬁcientinductionofcortical±

lowinformationtransferrate

andpredictabletrajectories.

peoplesufferingfromavery

tousertomoveleft,rightor

ofrestoringbrain-controlled

binarycontroloftherobotic

nowaitingforexternalcues

Incorporationof(amu/beta

automaticallybyperceiving

Spontaneouscontrolgiven

predictionmodelbasedon

resultsreﬂectthefeasibility

comparedtosynchronous

usingvirtualguidingpaths

usingtheP300paradigm,

Preliminaryevidencefrom

surroundingenvironment,

selectionfrompredeﬁned

Basedoncombinationof

interventionprocedureto

environmentalfeedback.

neuroplasticityinhealthy

providingcontrollerwith

Provisionofdestination

useself-pacedBCIfor

protocolcoupledwith

idlingandKMIstates.

localitiesinthemenu.

Successfullytargeted

classiﬁer 85%,-,-DevelopmentofEEG>

subjectswithashort

workloadduetoBCI

cheapersensorsfor

80% Reducedcognitive

fasterBCI)tostop

previoussystems.

walkingafterSCI.

P300protocol.

wheelchair.

orthosis.

ClassiﬁerClassiﬁ-cationaccuracy

LDA 100%,100%,94%,≈≈≥

- 94%,100%,100%,≥
- 95%,85.8%≥≥

Gaussianmodel,LDA90%,-,80%,≥≥

SVM,Gaussianmodel,

rhythms** FFT,PSD,CPCAAIDA,linearBayesian

rhythms Spatialﬁlter(CAR),

DevicesBrainactivityPre-processing

movingaverage

MAFO MRCP***Bandpassﬁlter,

Bandpassﬁlter,

P300,ERPBandpassﬁlter,

largeLaplacian

Laplacianﬁlter,

method),CVA,

ﬁlter,ANOVA

andfeature

PSD(Welch

extraction

ﬁlter

FFT

RoGO Oscillatory

Oscillatory

TABLE1|Continued

Wheel-

Wheel-

P300

chair

chair

BCI-

BCI-

BCI

BCI

TABLE1|Continued

applications References

(%) KeyﬁndingsTypeofsupportand

ClassiﬁerClassiﬁ-cationaccuracy

DevicesBrainactivityPre-processing

andfeature

extraction

ChoiandCichocki,2008

BCIwheelchairbasedonMI

protocolformotorimpaired

patients.

Millanetal.,2004;Toninetal.,

- 2010,2011;Chaeetal.,
- 2011a,b,2012

Escolanoetal.,2012;DeVenuto

Belletal.,2008;Ferreiraetal.,

2008;Belluomoetal.,2011;

etal.,2017

BCIbasedtelepresencerobotfor

movementofphysicallyimpaired

left/rightsteeringviaimagination

navigationassistanceaswellas

Controlnavigationofhumanoid

navigationinrequireddirection

formotordisabilityassistance.

BCIcontrolledhumanoidfor

BCIcontrolledmobileand

transportationofobjects.

ofleft/righthandorfeet

telepresencerobotsfor

robotviaMI.

people.

complextasksinsametime

75.6%,-,-≥ Allowsubjectstocomplete

SVM-Effectivefeedbacktraining

commandsasrequiredby

andwithsamenumberof

controllingwithajoystick

methodresultinginmulti

DOFs/freelycontrolling

wheelchairparallelto

manualcontrol

model 74%,75.6%,81%,≥

StatisticalGaussian

mobilerobotmovementsvia

humanoidforsophisticated

manipulationandtransport

environment,involvingnot

cortex,wasusedtoallow

twoEEGsignals(imagery

SuccessfulcontrolofBCI

interactiveBCIsystemto

relaxationstatesofvisual

controltwincoordinated

operatortosuccessfully

onlynavigationbutalso

controlarobotwithout

Theconcentrationand

interactionwiththe

SVM95%,-,95%,93%,80.5%Developmentofan≥

left-rightarm).

usinghands.

ofobjects.

ﬁlter,Bandpass

algorithm,CSP

rhythms* 2ndorderBSS

withAMUSE

Oscillatory

wheel-

chair

BMI

rhythms Bandpassﬁlter,

Laplacianﬁlter,

PSD(Welch

method)

ﬁlter

Oscillatory

robot/humanoid

mobile

BCI

Bandpassﬁlter

temporalﬁlter,

SMR,ERP,P300*Spatialﬁlter,

robot/humanoid

mobile

BCI

- *TheyusedcombinedEEGandEMGmodalitiesintheirsystem.
- **TheyusedcombinedEEG,FES,andEMGmodalitiesintheirBCIorthosis.
- ***TheyusedcombinedEEGandTMSmodalitiesforbrainsignalacquisitionandforclassiﬁcationpurposes,theyusedadditionalfeaturesfromEMGintheirBCIorthosis.

P300 signals are used for mobile commands, and oscillatory rhythms are used for stop command, the system is eﬃcient and safe enough to drive the real-time wheelchair in possible directions. They used Yamaha JW-I power wheelchair with two optical rotary encoders attached to glide-wheels for odometry, a bar code scanner for global positioning and a proximity sensor mounted in front of the wheelchair for collision avoidance. User could reach the destination, by selecting amongst a list of pre-deﬁned locations. This was primarily for patients with lost voluntary muscle control, but intact cognitive behavior who could use a BCI, such as LL amputees.

Other P300-BCI wheelchairs’ research include work done by Iturrate et al. (2009a,b) where the system relied on synchronous stimulus-driven protocol. The work done by Palankar et al. (2009) focused on, completely and partially locked-in patients, and provided them with an eﬀective model of a 9-DOF wheelchair-mounted robotic arm (WMRA) system. Pires et al. (2008) and Lopes et al. (2011) contributed in visual P300 based BCI for steering wheelchair assisted by shared-control. Kaufmann et al. (2014) validated the feasibility of a BCI based on tactually-evoked ERP for wheelchair control. Other wheelchairs controlled via EEG-based BCI include (Choi and Cichocki, 2008; Tsui et al., 2011; Huang et al., 2012; De Venuto et al., 2017).

In their report (Tonin et al., 2010, 2011) presented a BMI-controlled telepresence robot for people with motor impairment that could allow them completion of complex tasks, in similar time as that consumed by healthy subjects. They were able to steer RobotinoTM (by FESTO), via asynchronous KMI of left/right hand and feet. The system incorporated shared control for obstacle avoidance, safety measures and for interpreting user intentions to reach goal autonomously. A similar project was earlier presented by Millan et al. (2004) for mobile robot control in indoor environment via EEG. In order to recognize environment situations, a multilayer perception was implemented. Sensory readings were mapped to 6 classes of environmental states: forward movement, turn left, follow left wall, right turn, follow right wall and stop. These environmental states were generated against mental tasks as relax, KMI of left/right hand, cube rotation imagery, subtraction and word association. Research for control of two coordinated mobile robots, via SMR and ERP, that could be useful for motor impaired people, is done by Belluomo et al. (2011). Similarly mobile robot (Pioneer 2-DX) control based on mu ERD/ERS was done by Ferreira et al. (2008).

As per our knowledge, reﬂected from the literature, there is no viable active prosthetic ankle-foot, or prosthetic LL device, controlled via EEG-BCI for amputees.

## PRACTICAL CHALLENGES

In order to design a controller for an assistive-robot device there is a need of a seamless integration between the BCI operator, and the execution of required tasks from the output device with minimal cognitive disruption. However, there are challenges associated to the real-time implementation of the system, when

dealt with motor impaired population. Some open problems and challenges associated to wearable systems have recently been summarized in (Deng et al., 2018; Lazarou et al., 2018; Semprini et al., 2018). The following sections discuss in detail practical challenges associated to EEG-BCI wearable and assistive technologies.

Wearable Lower-Limb Device Challenges

A critical need for reliable EEG-BCI is required that could interpret user intent and make context-based decisions from the user’s present internal state. This would allow a direct and voluntary operation of the wearable LL devices beyond the user’s aﬀected physical, cognitive or sensory capabilities. With wearable LL devices it is observed that they did not embed shared controllers. The system should involve the development of reliable discrete classiﬁers, combined with continuous (modelbased) neural interfaces, to predict the subject’s intent without needing continuous supervisory control, but an “assist-asneeded” control from the BCI. Wearable LL technologies should embed features such as, self-calibration, self-analysis (with backward-forward failure attribution analysis) and errorcorrection. This is followed by adopting appropriate behavioral testing methods for performance evaluations of the system.

Clinical evaluation of wearables needs standardized safety and tolerability assessment of important factors such as cardiometabolic, musculoskeletal, skin, and biomechanical risks, followed by the assessment of cognitive-behavioral discrepancies that deﬁne the user proﬁle. Cardiorespiratory safety is of principal importance as individuals with stroke and SCI may have autonomic instability that can alter the pressure of blood-ﬂow. Their heart rates may not respond correctly to increased cardiorespiratory demands, depending on the lesion intensity. The cardiorespiratory demands of supported BCIexoskeleton/orthosis usage must primarily be assessed and carefully monitored also for reasons as: (1) the mean peak heart ﬁtness levels after SCI vary considerably depending on the lesion characteristics, but are generally much lower than normal; and (2) the skeletal muscle after SCI (or any central-nervous system injury) shifts in a shortfall severity from slow to a fast jerk molecular composition. Patients with abnormal gait biomechanics and ﬁtness levels must show adequate cardiorespiratory tolerance based on subject perceived exertion scales, and objective monitoring of metabolic proﬁles. This metabolic surveillance, along with careful clinical measures, to assess muscle injury, is inevitable for validating the cardiorespiratory, metabolic, and muscle safety during exoskeleton/orthosis use.

During rehabilitation, the wearable robotics may impose unusual joint kinetics and kinematics that could potentially injure bone or skin, particularly in stroke or SCI patients that usually have osteoporosis, unusual spasticity patterns, or contractures. For safe utilization a standard screening for assessment of bone health using dual X-ray absorptiometry and identiﬁcation of abnormal torque or impulses ahead of time, could retain from injury. There should be a careful consideration between engineers, clinicians, and subjects with neurological disability to rightly apply this new technology.

Substantial research and understanding of the cortical representations, for the perception of bipedal locomotion, is vital for evaluating changes in cortical dynamics when wearing closedloop BCI portable devices, and gauging on how these changes are correlated with gait adaptation. As the BCI wearable devices are designed to be stable, they have to ﬁnish one complete cycle of gait before stopping, resulting in a slow time-response compared to the model’s output. This is why in some systems the subject has to keep standing, as long as he can, after stopping the robot for continuously recording the model’s output state.

With P300-wearable LL devices, the decision time is relatively slow for real-time applications such as walking. The solution could involve implementation of more complex pipelines that include artifact removal techniques speciﬁc to gait-artifacts, followed by a better management of stimulus presentation duration. The P300 pipeline does not allow working asynchronously, which is an important aspect for the patient’s comfort (can be tiring). Following this, the poor experimental paradigm that usually includes a screen on a treadmill is not applicable for street walking; accordingly, an augmented reality eyewear seems to be indispensable.

Assistive-Robot Challenges

Clinical evaluations revealed that subjects with poor BCI performance require an extra need for assistance while maneuvering assistive-robots during complex path plans such as narrow corridors, despite the arduous BCI training.

The use of adaptive assistance with BCI wheelchairs increases the task performance of the user; however, the ﬁxed activation levels of the system do not integrate the user’s performance. This is due to the varying fatigue and hormone levels of the user, due to which the shared controller may not oﬀer constant level of assistance. Consequently, similar system behavior is always activated when the activation threshold is reached, even though an experienced user might still be able to recover from the disorientation on its own. System performance could be increased, if a user model is built at runtime, and the level of experience to determine the thresholds is estimated when the system behavior is activated.

Various customized ﬁltering approaches have been deployed by researchers during diﬀerent states of wheelchair use, for instance, the regular on and oﬀ switching of ﬁlter in between sessions of start and stop. Given in Kwak et al. (2015), when the ﬁlter was switched on or oﬀ, the subject was required to use another mental mode (or at least adapt its existing one) as the driving system was diﬀerent when the ﬁltering was applied. This resulted in a confusion mode which is a common problem in shared control systems. When the subject’s acquired strategies are built up using one driving system (i.e., without ﬁltering) and applied to the other situation (i.e., with ﬁltering), it ends up in a weak performance, leading to a situation where the environmental ﬁlter is actually working against the user’s intention. With present BCI-wheelchairs that incorporate shared controllers, if the activation levels of the system do not integrate the user’s performance, it could lead to degradation or loss of function.

Reportedly P300-wheelchairs were too slow to stop in real-time, after the selection of a sub-goal from menu, the user has to focus on a validation option, due to which the wheelchair stops and waits for the next command (followed by validation) from the user. Consequently this ends up in more stationary positions than actually moving to speciﬁc destinations.

## CONCLUSIONS

In this paper, we have presented a comprehensive review of the state-of-the-art EEG-BCI controlled wearable and assistive technologies for users having neuromotor disorder, SCI, stroke, disarticulation or amputation of residual LL. All reviewed applications are presented in the form of a generalized BCI control framework. The control framework is inclusive of the user, the BCI operator, the shared controller, and the robot device with the environment. Each element of the control framework was discussed in detail. The BCI operator is based on sublayers, each of which is highlighting the feature extraction, classiﬁcation and execution methods respectively, employed by each application. The reviewed applications comprised of oscillatory rhythms, event-related and evoked potentials as input signals. The EEG-BCI based portable and assistive device applications included exoskeletons, orthosis, wheelchairs, mobile/navigation robots and humanoids. Key features from each application were discussed and presented in the Table 1.

Based on the review we concluded that LL tasks, such as knee, or hip joint movements, have never been explicitly employed as MI or ME tasks in any BCI experimental protocol. Only foot or upper limb kinesthetic tasks are deployed. Additionally, it is observed that the EEG-based activity mode recognition, used to control wearable LL devices, only comprise of exoskeletons and orthosis. No viable prosthetic ankle-foot, or prosthetic LL device, employing EEG signals, for activity mode recognition, is currently available.

In most applications based on P300, strong output signals were observed that resulted in accurate command functions. It was followed by a slow performance pace and a loss in the user concentration due to stimulus presentation. On the contrary, applications employing SMR, where no stimulus protocol is involved, reﬂected a faster performance speed, followed by a weaker output signal during asynchronous mode.

Performance of EEG-based BCI, deployed by assistive technologies, is constrained due to the design of non-invasive modalities, compared to invasive ones and due to the limited size of features employed. In the case of complex movements more sets of parameters are required to execute a seamless output. This is still one of the challenging problems that require expertise to develop eﬃcient and robust algorithms to apprehend user’s motion intention.

In the most of the reviewed applications, there is a lack of quantitative performance indicators for the algorithms’ evaluations. There is no explicit signal classiﬁcation, percentage given. Error measurements between expected and real system trajectories are missing. There is no indication about the

measurements of the user-energy consumption, the walking endurance and the system costs. Finally, an important issue of carrying tests under realistic conditions, with patients having LL pathologies, needs special attention, provided the observations make the comparison of the dynamic behavior of each application diﬃcult.

## AUTHOR CONTRIBUTIONS

MT devised, drafted, structured, analyzed, and coordinated reading and writing of this review. She contributed text throughout, generated the ﬁgures and developed the structure of the generalized control framework and provided ﬁnal approval of the manuscript. PT contributed to analysis, critical revision,

provided feedback and ﬁnal approval on the manuscript. MS contributed to the Figure 1, analyzed, critically revised, provided feedback and ﬁnal approval on the manuscript. All authors read and approved the ﬁnal version of the manuscript. All authors agree to be accountable for all aspects of the work in ensuring that questions related to the accuracy or integrity of any part of the work are appropriately investigated and resolved.

## ACKNOWLEDGMENTS

Authors acknowledge the ﬁnancial support received for this research provided by RMIT University Ph.D. International Scholarship (RPIS).

## REFERENCES

Allison, B. Z., Wolpaw, E. W., and Wolpaw, J. R. (2007). Brain–computer interface systems: progress and prospects. Expert Rev. Med. Devices 4, 463–474. doi: 10.1586/17434440.4.4.463

Angeli, C. A., Edgerton, V. R., Gerasimenko, Y. P., and Harkema, S. J. (2014). Altering spinal cord excitability enables voluntary movements after chronic complete paralysis in humans. Brain 137, 1394–1409. doi: 10.1093/brain/awu038

Anthony, M., and Bartlett, P. L. (2009). Neural Network Learning: Theoretical Foundations. London: Cambridge University Press. Armstrong, D. M. (1988). The supraspinal control of mammalian locomotion. J. Physiol. 405, 1–37. doi: 10.1113/jphysiol.1988.sp017319

Bakker, M., Verstappen, C., Bloem, B., and Toni, I. (2007). Recent advances in functional neuroimaging of gait. J. Neural Transm. 114, 1323–1331. doi: 10.1007/s00702-007-0783-8

Baykara, E., Ruf, C. A., Fioravanti, C., Käthner, I., Simon, N., Kleih, S. C., et al. (2016). Eﬀects of training and motivation on auditory P300 brain-computer interface performance. Clin. Neurophysiol. 127, 379–387. doi: 10.1016/j.clinph.2015.04.054

Belda-Lois, J.-M., Mena-Del Horno, S., Bermejo-Bosch, I., Moreno, J. C., Pons, J. L., Farina, D., et al. (2011). Rehabilitation of gait after stroke: a review towards a top-down approach. J. Neuroeng. Rehabil. 8, 66. doi: 10.1186/1743-00 03-8-66

Bell, C. J., Shenoy, P., Chalodhorn, R., and Rao, R. P. (2008). Control of a humanoid robot by a noninvasive brain–computer interface in humans. J. Neural Eng. 5,

214. doi: 10.1088/1741-2560/5/2/012

Belluomo, P., Bucolo, M., Fortuna, L., and Frasca, M. (2011). “Robot control through brain computer interface for patterns generation,” in AIP Conference Proceedings (Halkidiki), 1031–1034.

Beloozerova, I. N., Sirota, M. G., and Swadlow, H. A. (2003). Activity of diﬀerent classes of neurons of the motor cortex during locomotion. J. Neurosci. 23, 1087–1097. doi: 10.1523/JNEUROSCI.23-03-01087.2003

Bulea, T. C., Kilicarslan, A., Ozdemir, R., Paloski, W. H., and Contreras-Vidal, J. L. (2013). Simultaneous scalp electroencephalography (EEG), electromyography (EMG), and whole-body segmental inertial recording for multi-modal neural decoding. J. Vis. Exp. 77:e50602. doi: 10.3791/50602

Bulea, T. C., Kim, J., Damiano, D. L., Stanley, C. J., and Park, H.-S. (2015). Prefrontal, Posterior parietal and sensorimotor network activity underlying speed control during walking. Front. Hum. Neurosci. 9:247. doi: 10.3389/fnhum.2015.00247

Capogrosso, M., Milekovic, T., Borton, D., Wagner, F., Moraud, E. M., Mignardot, J.-B., et al. (2016). A brain–spine interface alleviating gait deﬁcits after spinal cord injury in primates. Nature 539, 284–288. doi: 10.1038/nature 20118

Carlson, T., and Millan, J. D. R. (2013). Brain-controlled wheelchairs: a robotic architecture. IEEE Rob. Autom. Mag. 20, 65–73. doi: 10.1109/MRA.2012.2229936

Castermans, T., Duvinage, M., Hoellinger, T., Petieau, M., Dutoit, T., and Cheron, G. (2011a). “An analysis of EEG signals during voluntary rhythmic foot movements,” in 2011 5th International IEEE/EMBS Conference on the Neural Engineering (NER) (Cancún), 584–588.

Castermans, T., Duvinage, M., Petieau, M., Hoellinger, T., De Saedeleer, C., Seetharaman, K., et al. (2011b). “Optimizing the performances of a P300based brain–computer interface in ambulatory conditions,” in IEEE Journal on Emerging and Selected Topics in Circuits and Systems, Vol. 1 (New York, NY), 566–577.

Cervera, M. A., Soekadar, S. R., Ushiba, J., Millán, J. D. R., Liu, M., Birbraumer, N., et al. (2018). Brain-computer interfaces for post-stroke motor rehabilitation: a meta-analysis. Ann. Clin. Transl. Neurol. 5, 651–663. doi: 10.1002/acn3.544

- Chae, Y., Jeong, J., and Jo, S. (2011a). “Noninvasive brain-computer interfacebased control of humanoid navigation,” in 2011 IEEE/RSJ International Conference on the Intelligent Robots and Systems (IROS) (San Francisco, CA), 685–691.
- Chae, Y., Jeong, J., and Jo, S. (2012). Toward brain-actuated humanoid robots: asynchronous direct control using an EEG-based BCI. IEEE Trans. Rob. 28, 1131–1144. doi: 10.1109/TRO.2012.2201310

Chae, Y., Jo, S., and Jeong, J. (2011b). “Brain-actuated humanoid robot navigation control using asynchronous brain-computer interface,” in 2011 5th International IEEE/EMBS Conference on the Neural Engineering (NER) (Cancún), 519–524.

Chéron, G., Duvinage, M., Castermans, T., Leurs, F., Cebolla, A., Bengoetxea, A., et al. (2011). “Toward an integrative dynamic recurrent neural network for sensorimotor coordination dynamics,” in Recurrent Neural Networks for Temporal Data Processing, Vol. 5, ed H. Cardot (Rijeka: InTech), 67–80.

Chéron, G., Duvinage, M., De Saedeleer, C., Castermans, T., Bengoetxea, A., Petieau, M., et al. (2012). From spinal central pattern generators to cortical network: integrated BCI for walking rehabilitation. Neural Plast. 2012:375148. doi: 10.1155/2012/375148

Choi, K., and Cichocki, A. (2008). Control of a wheelchair by motor imagery in real time. Intell. Data Eng. Autom. Learn. 2008, 330–337. doi: 10.1007/978-3-540-88906-9_42

- Chvatal, S. A., and Ting, L. H. (2012). Voluntary and reactive recruitment of locomotor muscle synergies during perturbed walking. J. Neurosci. 32, 12237–12250. doi: 10.1523/JNEUROSCI.6344-11.2012
- Chvatal, S. A., and Ting, L. H. (2013). Common muscle synergies for balance and walking. Front. Comput. Neurosci. 7:48. doi: 10.3389/fncom.2013.00048

Chvatal, S. A., Torres-Oviedo, G., Safavynia, S. A., and Ting, L. H. (2011). Common muscle synergies for control of center of mass and force in nonstepping and stepping postural behaviors. J. Neurophysiol. 106, 999–1015. doi: 10.1152/jn.00549.2010

Contreras-Vidal, J. L., Bhagat, N. A., Brantley, J., Cruz-Garza, J. G., He, Y., Manley, Q., et al. (2016). Powered exoskeletons for bipedal locomotion after spinal cord injury. J. Neural Eng. 13:031001. doi: 10.1088/1741-2560/13/3/031001

Contreras-Vidal, J. L., and Grossman, R. G. (2013). “NeuroRex: A clinical neural interface roadmap for EEG-based brain machine interfaces to a lower body

robotic exoskeleton,” in 2013 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Osaka), 1579–1582.

Daly, J. J., and Wolpaw, J. R. (2008). Brain–computer interfaces in neurological rehabilitation. Lancet Neurol. 7, 1032–1043. doi: 10.1016/S1474-4422(08)70223-0

Delorme, A., Kothe, C., Vankov, A., Bigdely-Shamlo, N., Oostenveld, R., Zander, T. O., et al. (2010). MATLAB-Based Tools for BCI Research. London: Springer, Brain-computer interfaces.

Delorme, A., Mullen, T., Kothe, C., Acar, Z. A., Bigdely-Shamlo, N., Vankov, A., et al. (2011). EEGLAB, SIFT, NFT, BCILAB, and ERICA: new tools for advanced EEG processing. Comput. Intell. Neurosci. 2011:10. doi: 10.1155/2011/1 30714

Deng, W., Papavasileiou, I., Qiao, Z., Zhang, W., Lam, K.-Y., and Han, S. (2018). Advances in automation technologies for lower-extremity neurorehabilitation: a review and future challenges. IEEE Rev. Biomed. Eng. 11, 289–305. doi: 10.1109/RBME.2018.2830805

De Venuto, D., Annese, V. F., and Mezzina, G. (2017). “An embedded system remotely driving mechanical devices by P300 brain activity,” in Proceedings of the Conference on Design, Automation & Test in Europe, European Design and Automation Association (Lausanne), 1014–1019.

Dimitrijevic, M. R., Gerasimenko, Y., and Pinter, M. M. (1998). Evidence for a spinal central pattern generator in humans. Ann. N. Y. Acad. Sci. 860, 360–376. doi: 10.1111/j.1749-6632.1998.tb09062.x

Do, A. H., Wang, P. T., King, C. E., Abiri, A., and Nenadic, Z. (2011). Braincomputer interface controlled functional electrical stimulation system for ankle movement. J. Neuroeng. Rehabil. 8:49. doi: 10.1186/1743-0003-8-49

Do, A. H., Wang, P. T., King, C. E., Chun, S. N., and Nenadic, Z. (2013). Brain-computer interface controlled robotic gait orthosis. J. Neuroeng. Rehabil. 10:111. doi: 10.1186/1743-0003-10-111

Do, A. H., Wang, P. T., King, C. E., Schombs, A., Cramer, S. C., and Nenadic, Z. (2012). “Brain-computer interface controlled functional electrical stimulation device for foot drop due to stroke,” in 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (San Diego, CA), 6414–6417.

Drew, T., Kalaska, J., and Krouchev, N. (2008). Muscle synergies during locomotion in the cat: a model for motor cortex control. J. Physiol. 586, 1239–1245. doi: 10.1113/jphysiol.2007.146605

Duvinage, M., Castermans, T., Jiménez-Fabián, R., Hoellinger, T., De Saedeleer, C., Petieau, M., et al. (2012). “A ﬁve-state P300-based foot lifter orthosis: Proof of concept,” in Biosignals and Biorobotics Conference (BRC), 2012 ISSNIP (Manaus: IEEE), 1–6.

Escolano, C., Antelis, J. M., and Minguez, J. (2012). A telepresence mobile robot controlled with a noninvasive brain–computer interface. IEEE Trans. Syst. Man Cybern. B Cybern. 42, 793–804. doi: 10.1109/TSMCB.2011.21 77968

Fatourechi, M., Bashashati, A., Ward, R. K., and Birch, G. E. (2007). EMG and EOG artifacts in brain computer interface systems: a survey. Clin. Neurophysiol. 118, 480–494. doi: 10.1016/j.clinph.2006.10.019

Ferdousy, R., Choudhory, A. I., Islam, M. S., Rab, M. A., and Chowdhory, M. E. H. (2010). “Electrooculographic and electromyographic artifacts removal from EEG,” in 2010 2nd International Conference on the Chemical, Biological and Environmental Engineering (ICBEE) (Cairo), 163–167.

Ferreira, A., Celeste, W. C., Cheein, F. A., Bastos-Filho, T. F., SarcinelliFilho, M., and Carelli, R. (2008). Human-machine interfaces based on EMG and EEG applied to robotic systems. J. Neuroeng. Rehabil. 5:10. doi: 10.1186/1743-0003-5-10

Frolov, A. A., Mokienko, O., Lyukmanov, R., Biryukova, E., Kotov, S., Turbina, L., et al. (2017). Post-stroke rehabilitation training with a motor-imagery-based brain-computer interface (BCI)-controlled hand exoskeleton: a randomized controlled multicenter trial. Front. Neurosci. 11:400. doi: 10.3389/fnins.2017.00400

Galán, F., Nuttin, M., Lew, E., Ferrez, P. W., Vanacker, G., Philips, J., et al. (2008). A brain-actuated wheelchair: asynchronous and non-invasive brain–computer interfaces for continuous control of robots. Clin. Neurophysiol. 119, 2159–2169. doi: 10.1016/j.clinph.2008.06.001

Gancet, J., Ilzkovitz, M., Cheron, G., Ivanenko, Y., Van Der Kooij, H., Van Der Helm, F., et al. (2011). “MINDWALKER: a brain controlled lower limbs exoskeleton for rehabilitation. Potential applications to space,” in 11th

Symposium on Advanced Space Technologies in Robotics and Automation (Noordwijk), 12–14.

Gancet, J., Ilzkovitz, M., Motard, E., Nevatia, Y., Letier, P., De Weerdt, D., et al. (2012). “MINDWALKER: going one step further with assistive lower limbs exoskeleton for SCI condition subjects,” in 2012 4th IEEE RAS & EMBS International Conference on the Biomedical Robotics and Biomechatronics (BioRob) (Rome), 1794–1800.

García-Cossio, E., Severens, M., Nienhuis, B., Duysens, J., Desain, P., Keijsers, N., et al. (2015). Decoding sensorimotor rhythms during robotic-assisted treadmill walking for brain computer interface (BCI) applications. PLoS ONE 10:e0137910. doi: 10.1371/journal.pone.0137910

Gramann, K., Ferris, D. P., Gwin, J., and Makeig, S. (2014). Imaging natural cognition in action. Int. J. Psychophysiol. 91, 22–29. doi: 10.1016/j.ijpsycho.2013.09.003

- Gwin, J. T., Gramann, K., Makeig, S., and Ferris, D. P. (2010). Removal of movement artifact from high-density EEG recorded during walking and running. J. Neurophysiol. 103, 3526–3534. doi: 10.1152/jn.00105.2010
- Gwin, J. T., Gramann, K., Makeig, S., and Ferris, D. P. (2011). Electrocortical activity is coupled to gait cycle phase during treadmill walking. Neuroimage 54, 1289–1296. doi: 10.1016/j.neuroimage.2010.08.066

Hashimoto, Y., and Ushiba, J. (2013). EEG-based classiﬁcation of imaginary left and right foot movements using beta rebound. Clin. Neurophysiol. 124, 2153–2160. doi: 10.1016/j.clinph.2013.05.006

He, B. (2016). Neural Engineering. New York, NY: Springer, U. S. He, B., Baxter, B., Edelman, B. J., Cline, C. C., and Wenjing, W. Y. (2015).

Noninvasive brain-computer interfaces based on sensorimotor rhythms. Proc. IEEE 103, 907–925. doi: 10.1109/JPROC.2015.2407272

He, Y., Eguren, D., Azorín, J. M., Grossman, R. G., Luu, T. P., and ContrerasVidal, J. L. (2018a). Brain-machine interfaces for controlling lower-limb powered robotic systems. J. Neural Eng. 15:021004. doi: 10.1088/1741-2552/a aa8c0

He, Y., Luu, T. P., Nathan, K., Nakagome, S., and Contreras-Vidal, J. L. (2018b). A mobile brain-body imaging dataset recorded during treadmill walking with a brain-computer interface. Sci. Data 5:180074. doi: 10.1038/sdata.2018.74

Herr, H. M., Weber, J. A., Au, S. K., Deﬀenbaugh, B. W., Magnusson, L. H., Hofmann, A. G., et al. (2013). Powered Ankle-Foot Prothesis. Google Patents No. 60/934,223. Cambridge, MA: Massachusetts Institute of Technology.

Huang, D., Qian, K., Fei, D.-Y., Jia, W., Chen, X., and Bai, O. (2012). Electroencephalography (EEG)-based brain–computer interface (BCI): a 2-D virtual wheelchair control based on event-related desynchronization/synchronization and state control. IEEE Trans. Neural Syst. Rehabil. Eng. 20, 379–388. doi: 10.1109/TNSRE.2012.2 190299

Iturrate, I., Antelis, J., and Minguez, J. (2009a). “Synchronous EEG brain-actuated wheelchair with automated navigation,” in IEEE International Conference on the Robotics and Automation ICRA’09 (Kobe), 2318–2325.

Iturrate, I., Antelis, J. M., Kubler, A., and Minguez, J. (2009b). A noninvasive brain-actuated wheelchair based on a P300 neurophysiological protocol and automated navigation. IEEE Trans. Rob. 25, 614–627. doi: 10.1109/TRO.2009.2020347

Jain, S., Gourab, K., Schindler-Ivens, S., and Schmit, B. D. (2013). EEG during pedaling: evidence for cortical control of locomotor tasks. Clin. Neurophysiol. 124, 379–390. doi: 10.1016/j.clinph.2012.08.021

Jimenez-Fabian, R., and Verlinden, O. (2012). Review of control algorithms for robotic ankle systems in lower-limb orthoses, prostheses, and exoskeletons. Med. Eng. Phys. 34, 397–408. doi: 10.1016/j.medengphy.2011. 11.018

Kalcher, J., and Pfurtscheller, G. (1995). Discrimination between phase-locked and non-phase-locked event-related EEG activity. Electroencephalogr. Clin. Neurophysiol. 94, 381–384. doi: 10.1016/0013-4694(95)00040-6

Kaufmann, T., Herweg, A., and Kübler, A. (2014). Toward brain-computer interface based wheelchair control utilizing tactually-evoked event-related potentials. J. Neuroeng. Rehabil. 11:7. doi: 10.1186/1743-0003-11-7

Kautz, S. A., and Patten, C. (2005). Interlimb inﬂuences on paretic leg function in poststroke hemiparesis. J. Neurophysiol. 93, 2460–2473. doi: 10.1152/jn.00963.2004

Kilicarslan, A., Prasad, S., Grossman, R. G., and Contreras-Vidal, J. L. (2013). “High accuracy decoding of user intentions using EEG to control a

lower-body exoskeleton,” in 2013 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Osaka), 5606–5609.

King, C. E., Wang, P. T., Chui, L. A., Do, A. H., and Nenadic, Z. (2013). Operation of a brain-computer interface walking simulator for individuals with spinal cord injury. J. Neuroeng. Rehabil. 10:77. doi: 10.1186/1743-0003-10-77

Kothe, C. A., and Makeig, S. (2013). BCILAB: a platform for brain–computer interface development. J. Neural Eng. 10:056014. doi: 10.1088/1741-2560/10/5/056014

Kumar, D., Aggarwal, G., Sehgal, R., Das, A., Lahiri, U., and Dutta, A. (2015). “Engagement-sensitive interactive neuromuscular electrical therapy system for post-stroke balance rehabilitation-a concept study,” in 2015 7th International IEEE/EMBS Conference on the Neural Engineering (NER) (Montpellier), 190–193.

Kwak, N.-S., Müller, K.-R., and Lee, S.-W. (2015). A lower limb exoskeleton control system based on steady state visual evoked potentials. J. Neural Eng. 12:056009. doi: 10.1088/1741-2560/12/5/056009

La Fougere, C., Zwergal, A., Rominger, A., Förster, S., Fesl, G., Dieterich, M., et al.

(2010). Real versus imagined locomotion: a [18F]-FDG PET-fMRI comparison. Neuroimage 50, 1589–1598. doi: 10.1016/j.neuroimage.2009.12.060

Lazarou, I., Nikolopoulos, S., Petrantonakis, P. C., Kompatsiaris, I., and Tsolaki, M. (2018). EEG-based brain-computer interfaces for communication and rehabilitation of people with motor impairment: a novel approach of the 21st century. Front. Hum. Neurosci. 12:14. doi: 10.3389/fnhum.2018.00014

Lebedev, M. A., and Nicolelis, M. A. (2017). Brain-machine interfaces: from basic science to neuroprostheses and neurorehabilitation. Physiol. Rev. 97, 767–837. doi: 10.1152/physrev.00027.2016

Lee, K., Liu, D., Perroud, L., Chavarriaga, R., and Millán, J. D. R. (2017). Endogenous Control of Powered Lower-Limb Exoskeleton. Basel: Springer: Wearable Robotics: Challenges and Trends.

Liu, Y.-H., Lin, L.-F., Chou, C.-W., Chang, Y., Hsiao, Y.-T., and Hsu, W.-C. (2018). Analysis of electroencephalography event-related desynchronisation and synchronisation induced by lower-limb stepping motor imagery. J. Med. Biol. Eng. 4, 1–16. doi: 10.1007/s40846-018-0379-9

Liu, Y.-H., Zhang, B., Liu, Q., Hsu, W.-C., Hsiao, Y.-T., Su, J.-Y., et al. (2015). “A robotic gait training system integrating split-belt treadmill, footprint sensing and synchronous EEG recording for neuro-motor recovery,” in 2015 37th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Milan), 3573–3577.

Lopes, A. C., Pires, G., Vaz, L., and Nunes, U. (2011). “Wheelchair navigation assisted by human-machine shared-control and a P300-based brain computer interface,” in 2011 IEEE/RSJ International Conference on the IEEE Intelligent Robots and Systems (IROS) (San Francisco, CA), 2438–2444.

Lotte, F. (2014). A Tutorial on EEG Signal-Processing Techniques for MentalState Recognition in Brain–Computer Interfaces. London: Springer, Guide to Brain-Computer Music Interfacing.

Lotte, F., Bougrain, L., Cichocki, A., Clerc, M., Congedo, M., Rakotomamonjy, A., et al. (2018). A review of classiﬁcation algorithms for EEG-based brain-computer interfaces: a 10 year update. J. Neural Eng. 15:031005. doi: 10.1088/1741-2552/aab2f2

Lotte, F., Congedo, M., Lécuyer, A., Lamarche, F., and Arnaldi, B. (2007). A review of classiﬁcation algorithms for EEG-based brain–computer interfaces. J. Neural Eng. 4:R1. doi: 10.1088/1741-2560/4/2/R01

Lotte, F., Fujisawa, J., Touyama, H., Ito, R., Hirose, M., and Lécuyer, A. (2009). “Towards ambulatory brain-computer interfaces: A pilot study with P300 signals,” in Proceedings of the International Conference on Advances in Computer Enterntainment Technology, (Athens: ACM), 336–339.

Maguire, C. C., Sieben, J. M., and De Bie, R. A. (2018). Movement goals encoded within the cortex and muscle synergies to reduce redundancy pre and poststroke. The relevance for gait rehabilitation and the prescription of walkingaids. A literature review and scholarly discussion. Physiother. Theory Pract. 5, 1–14. doi: 10.1080/09593985.2018.1434579

Malouin, F., and Richards, C. L. (2010). Mental practice for relearning locomotor skills. Phys. Ther. 90, 240–251. doi: 10.2522/ptj.20090029

Malouin, F., Richards, C. L., Durand, A., and Doyon, J. (2008). Clinical assessment of motor imagery after stroke. Neurorehabil. Neural Repair. 22, 330–340. doi: 10.1177/1545968307313499

Malouin, F., Richards, C. L., Jackson, P. L., Dumas, F., and Doyon, J. (2003). Brain activations during motor imagery of locomotor-related tasks: a PET study. Hum. Brain Mapp. 19, 47–62. doi: 10.1002/hbm.10103

Marlinski, V., and Beloozerova, I. N. (2014). Burst ﬁring of neurons in the thalamic reticular nucleus during locomotion. J. Neurophysiol. 112, 181–192. doi: 10.1152/jn.00366.2013

Mellinger, J., and Schalk, G. (2007). BCI2000: A General-Purpose Software Platform for BCI Research. Cambridge, MA: Towards Brain-Computer Interfacing.

Millán, J. D. R., Galán, F., Vanhooydonck, D., Lew, E., Philips, J., and Nuttin, M. (2009). “Asynchronous non-invasive brain-actuated control of an intelligent wheelchair,” in Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Minneapolis, MN), 3361–3364.

Millán, J. D. R., Rupp, R., Müller-Putz, G. R., Murray-Smith, R., Giugliemma, C., Tangermann, M., et al. (2010). Combining brain–computer interfaces and assistive technologies: state-of-the-art and challenges. Front. Neurosci. 4:161. doi: 10.3389/fnins.2010.00161

Millan, J. R., Renkens, F., Mourino, J., and Gerstner, W. (2004). Noninvasive brainactuated control of a mobile robot by human EEG. IEEE Trans. Biomed. Eng. 51, 1026–1033. doi: 10.1109/TBME.2004.827086

Mokienko, O., Chervyakov, A., Kulikova, S., Bobrov, P., Chernikova, L., Frolov, A., et al. (2013). Increased motor cortex excitability during motor imagery in brain-computer interface trained subjects. Front. Comput. Neurosci. 7:168. doi: 10.3389/fncom.2013.00168

Müller-Gerking, J., Pfurtscheller, G., and Flyvbjerg, H. (1999). Designing optimal spatial ﬁlters for single-trial EEG classiﬁcation in a movement task. Clin. Neurophysiol. 110, 787–798. doi: 10.1016/S1388-2457(98)00038-8

Murray, S., and Goldfarb, M. (2012). “Towards the use of a lower limb exoskeleton for locomotion assistance in individuals with neuromuscular locomotor deﬁcits,” in 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), (San Diego, CA: IEEE), 1912–1915.

Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a review. Sensors 12, 1211–1279. doi: 10.3390/s120201211

Noda, T., Sugimoto, N., Furukawa, J., Sato, M.-A., Hyon, S.-H., and Morimoto, J. (2012). “Brain-controlled exoskeleton robot for BMI rehabilitation,” in 2012 12th IEEE-RAS International Conference on Humanoid Robots (Humanoids) (Osaka: IEEE), 21–27.

Nolan, H., Whelan, R., and Reilly, R. (2010). FASTER: fully automated statistical thresholding for EEG artifact rejection. J. Neurosci. Methods 192, 152–162. doi: 10.1016/j.jneumeth.2010.07.015

Palankar, M., De Laurentis, K. J., Alqasemi, R., Veras, E., Dubey, R., Arbel, Y., et al. (2009). “Control of a 9-DoF wheelchair-mounted robotic arm system using a P300 brain computer interface: Initial experiments,” in 2008 IEEE International Conference on Robotics and Biomimetics, ROBIO (Bangkok: IEEE), 348–353. doi: 10.1109/ROBIO.2009.4913028

Penﬁeld, W., and Boldrey, E. (1937). Somatic motor and sensory representation in the cerebral cortex of man as studied by electrical stimulation. Brain 60, 389–443. doi: 10.1093/brain/60.4.389

Petersen, T. H., Willerslev-Olsen, M., Conway, B. A., and Nielsen, J. B. (2012). The motor cortex drives the muscles during walking in human subjects. J. Physiol. 590, 2443–2452. doi: 10.1113/jphysiol.2012.227397

Petrofsky, J. S., and Khowailed, I. A. (2014). Postural sway and motor control in trans-tibial amputees as assessed by electroencephalography during eight balance training tasks. Med. Sci. Monit. 20: 2695–2704. doi: 10.12659/MSM.891361

Pfurtscheller, G., Brunner, C., Schlögl, A., and Da Silva, F. L. (2006a). Mu rhythm (de) synchronization and EEG single-trial classiﬁcation of diﬀerent motor imagery tasks. Neuroimage 31, 153–159. doi: 10.1016/j.neuroimage.2005.12.003

Pfurtscheller, G., Leeb, R., Keinrath, C., Friedman, D., Neuper, C., Guger, C., et al. (2006b). Walking from thought. Brain Res. 1071, 145–152. doi: 10.1016/j.brainres.2005.11.083

Pfurtscheller, G., Neuper, C., Brunner, C., and Da Silva, F. L. (2005). Beta rebound after diﬀerent types of motor imagery in man. Neurosci. Lett. 378, 156–159. doi: 10.1016/j.neulet.2004.12.034

Pfurtscheller, G., and Solis-Escalante, T. (2009). Could the beta rebound in the EEG be suitable to realize a “brain switch”? Clin. Neurophysiol. 120, 24–29. doi: 10.1016/j.clinph.2008.09.027

Pires, G., Castelo-Branco, M., and Nunes, U. (2008). “Visual P300-based BCI to steer a wheelchair: a Bayesian approach,” in 2008 30th Annual International Conference of the IEEE Engineering in Medicine and Biology Society EMBS (Vancouver, BC: IEEE), 658–661.

Pons, J., Moreno, J., Torricelli, D., and Taylor, J. (2013). “Principles of human locomotion: a review,” in 2013 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Osaka: IEEE), 6941–6944.

Presacco, A., Forrester, L., and Contreras-Vidal, J. L. (2011a). “Towards a noninvasive brain-machine interface system to restore gait function in humans,” in 2011 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBC (Boston, MA: IEEE), 4588–4591.

Presacco, A., Goodman, R., Forrester, L., and Contreras-Vidal, J. L. (2011b). Neural decoding of treadmill walking from noninvasive electroencephalographic signals. J. Neurophysiol. 106, 1875–1887. doi: 10.1152/jn.00104.2011

Raethjen, J., Govindan, R., Binder, S., Zeuner, K. E., Deuschl, G., and Stolze, H.

(2008). Cortical representation of rhythmic foot movements. Brain Res. 1236, 79–84. doi: 10.1016/j.brainres.2008.07.046

Rebsamen, B., Burdet, E., Guan, C., Zhang, H., Teo, C. L., Zeng, Q., et al. (2007). Controlling a wheelchair indoors using thought. IEEE Intell. Syst. 22, 18–24. doi: 10.1109/MIS.2007.26

Rebsamen, B., Guan, C., Zhang, H., Wang, C., Teo, C., Ang, M. H., et al. (2010). A brain controlled wheelchair to navigate in familiar environments. IEEE Trans. Neural Syst. Rehabil. Eng. 18, 590–598. doi: 10.1109/TNSRE.2010.20 49862

Renard, Y., Lotte, F., Gibert, G., Congedo, M., Maby, E., Delannoy, V., et al. (2010). Openvibe: an open-source software platform to design, test, and use brain–computer interfaces in real and virtual environments. Presence 19, 35–53. doi: 10.1162/pres.19.1.35

Rivet, B., Souloumiac, A., Attina, V., and Gibert, G. (2009). xDAWN algorithm to enhance evoked potentials: application to brain–computer interface. IEEE Trans. Biomed. Eng. 56, 2035–2043. doi: 10.1109/TBME.2009.20 12869

Salazar-Varas, R., Costa, Á., Iáñez, E., Úbeda, A., Hortal, E., and Azorín, J.

(2015). Analyzing EEG signals to detect unexpected obstacles during walking. J. Neuroeng. Rehabil. 12, 101. doi: 10.1186/s12984-015-0095-4

Schalk, G., Mcfarland, D. J., Hinterberger, T., Birbaumer, N., and Wolpaw, J. R. (2004). BCI2000: a general-purpose brain-computer interface (BCI) system. IEEE Trans. Biomed. Eng. 51, 1034–1043. doi: 10.1109/TBME.2004.8 27072

Scherrer, B. (2007). Gaussian Mixture Model Classiﬁers. Lecture Notes, February. Schwartz, A. B., Cui, X. T., Weber, D. J., and Moran, D. W. (2006). Brain-controlled

interfaces: movement restoration with neural prosthetics. Neuron 52, 205–220. doi: 10.1016/j.neuron.2006.09.019

Sczesny-Kaiser, M., Höﬀken, O., Aach, M., Cruciger, O., Grasmücke, D., Meindl, R., et al. (2015). HAL R exoskeleton training improves walking parameters and normalizes cortical excitability in primary somatosensory cortex in spinal cord injury patients. J. Neuroeng. Rehabil. 12, 68. doi: 10.1186/s12984-0150058-9

Semprini, M., Laﬀranchi, M., Sanguineti, V., Avanzino, L., De Icco, R., De Michieli, L., et al. (2018). Technological approaches for neurorehabilitation: from robotic devices to brain stimulation and beyond. Fronti. Neurol. 9:212. doi: 10.3389/fneur.2018.00212

Semmlow, J. L., and Griﬀel, B. (2014). Biosignal and Medical Image Processing. Cambridge, MA: CRC press.

Slutzky, M. W. (2018). Brain-machine interfaces: powerful tools for clinical treatment and neuroscientiﬁc investigations. Neuroscientist. doi: 10.1177/1073858418775355. [Epub ahead of print].

Soekadar, S. R., Witkowski, M., Vitiello, N., and Birbaumer, N. (2015). An EEG/EOG-based hybrid brain-neural computer interaction (BNCI) system to control an exoskeleton for the paralyzed hand. Biomed. Tech. (Berl) 60, 199–205. doi: 10.1515/bmt-2014-0126

Takahashi, M., Gouko, M., and Ito, K. (2009). “Fundamental research about electroencephalogram (EEG)-functional electrical stimulation (FES) rehabilitation system,” in 2009 IEEE International Conference on, IEEE Rehabilitation Robotics, (2009) ICORR (Kyoto), 316–321.

Takahashi, M., Takeda, K., Otaka, Y., Osu, R., Hanakawa, T., Gouko, M., et al. (2012). Event related desynchronization-modulated functional electrical

stimulation system for stroke rehabilitation: a feasibility study. J. Neuroeng. Rehabil. 9, 56. doi: 10.1186/1743-0003-9-56

- Tariq, M., Trivailo, P. M., and Simic, M. (2017a). “Detection of knee motor imagery by Mu ERD/ERS quantiﬁcation for BCI based neurorehabilitation applications,” in 2017 11th Asian Control Conference (ASCC), (Gold Coast, QLD), 2215–2219.
- Tariq, M., Trivailo, P. M., and Simic, M. (2018). Event-related changes detection in sensorimotor rhythm. Int. Rob. Autom. J. 4, 119–120. doi: 10.15406/iratj.2018.04.00105

Tariq, M., Uhlenberg, L., Trivailo, P., Munir, K. S., and Simic, M. (2017b). “Mu-beta rhythm ERD/ERS quantiﬁcation for foot motor execution and imagery tasks in BCI applications,” in 2017 8th IEEE International Conference on Cognitive Infocommunications (CogInfoCom) (Debrecen), 000091–000096.

Taylor II, R. M., Hudson, T. C., Seeger, A., Weber, H., Juliano, J., and Helser, A. T. (2001). “VRPN: a device-independent, network-transparent VR peripheral system,” in Proceedings of the ACM Symposium on Virtual Reality Software and Technology, (Baniﬀ, AB: ACM), 55–61.

Tonin, L., Carlson, T., Leeb, R., and Millán, J. D. R. (2011). “Brain-controlled telepresence robot by motor-disabled people,” in 2011 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBC (Boston, MA: IEEE), 4227–4230.

Tonin, L., Leeb, R., Tavella, M., Perdikis, S., and Millán, J. D. R. (2010). “The role of shared-control in BCI-based telepresence,” in 2010 IEEE International Conference on Systems Man and Cybernetics, (Istanbul: IEEE), 1462–1466.

Tsui, C. S. L., Gan, J. Q., and Hu, H. (2011). A self-paced motor imagery based brain-computer interface for robotic wheelchair control. Clin. EEG Neurosci. 42, 225–229. doi: 10.1177/155005941104200407

Tucker, M. R., Olivier, J., Pagel, A., Bleuler, H., Bouri, M., Lambercy, O., et al.

(2015). Control strategies for active lower extremity prosthetics and orthotics: a review. J. Neuroeng. Rehabil. 12, 1. doi: 10.1186/1743-0003-12-1

Vanacker, G., Del R Millán, J., Lew, E., Ferrez, P. W., Moles, F. G., Philips, J., et al.

(2007). Context-based ﬁltering for assisted brain-actuated wheelchair driving. Comput. Intell. Neurosci. 2007, 3–3. doi: 10.1155/2007/25130

Vasilyev, A., Liburkina, S., Yakovlev, L., Perepelkina, O., and Kaplan, A. (2017). Assessing motor imagery in brain-computer interface training: psychological and neurophysiological correlates. Neuropsychologia 97, 56–65. doi: 10.1016/j.neuropsychologia.2017.02.005

Vidal, J. J. (1973). Toward direct brain-computer communication. Annu. Rev. Biophys. Bioeng. 2, 157–180. doi: 10.1146/annurev.bb.02.060173.00 1105

Viola, F. C., Thorne, J., Edmonds, B., Schneider, T., Eichele, T., and Debener, S. (2009). Semi-automatic identiﬁcation of independent components representing EEG artifact. Clin. Neurophysiol. 120, 868–877. doi: 10.1016/j.clinph.2009.01.015

Wang, P. T., King, C., Chui, L. A., Nenadic, Z., and Do, A. (2010). “BCI controlled walking simulator for a BCI driven FES device,” in Proceedings of RESNA Annual Conference, (Arlington: VA: RESNA).

Wang, P. T., King, C. E., Chui, L. A., Do, A. H., and Nenadic, Z. (2012). Self-paced brain–computer interface control of ambulation in a virtual reality environment. J. Neural Eng. 9:056016. doi: 10.1088/1741-2560/9/5/0 56016

Wieser, M., Haefeli, J., Bütler, L., Jäncke, L., Riener, R., and Koeneke, S. (2010). Temporal and spatial patterns of cortical activation during assisted lower limb movement. Exp. Brain Res. 203, 181–191. doi: 10.1007/s00221-010-2 223-5

Wolpaw, J., and Wolpaw, E. W. (2012). Brain-Computer Interfaces: Principles and Practice, New York, NY: Oxford University Press.

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Wolpaw, J. R., and Mcfarland, D. J. (2004). Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans. Proc. Natl. Acad. Sci. U.S.A. 101, 17849–17854. doi: 10.1073/pnas.04035 04101

Xu, R., Jiang, N., Mrachacz-Kersting, N., Lin, C., Prieto, G. A., Moreno, J. C., et al. (2014). A closed-loop brain–computer interface triggering an active ankle–foot orthosis for inducing cortical neural plasticity.

IEEE Trans. Biomed. Eng. 61, 2092–2101. doi: 10.1109/TBME.2014.23 13867

Yang, Z., Wang, Y., and Ouyang, G. (2014). Adaptive neuro-fuzzy inference system for classiﬁcation of background EEG signals from ESES patients and controls. ScientiﬁcWorldJournal 2014:140863. doi: 10.1155/2014/1 40863

Zelenin, P. V., Deliagina, T. G., Orlovsky, G. N., Karayannidou, A., Dasgupta, N. M., Sirota, M. G., et al. (2011). Contribution of diﬀerent limb controllers to modulation of motor cortex neurons during locomotion. J. Neurosci. 31, 4636–4649. doi: 10.1523/JNEUROSCI.6511-10.2011

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2018 Tariq, Trivailo and Simic. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

