## A Human-Centric Metaverse Enabled by Brain-Computer Interface: A Survey

Howe Yuan Zhu, Nguyen Quang Hieu, Dinh Thai Hoang, Diep N. Nguyen, and Chin-Teng Lin

### arXiv:2309.01848v1[cs.HC]4Sep2023

Abstract—The growing interest in the Metaverse has generated momentum for members of academia and industry to innovate toward realizing the Metaverse world. The Metaverse is a unique, continuous, and shared virtual world where humans embody a digital form within an online platform. Through a digital avatar, Metaverse users should have a perceptual presence within the environment and can interact and control the virtual world around them. Thus, a human-centric design is a crucial element of the Metaverse. The human users are not only the central entity but also the source of multi-sensory data that can be used to enrich the Metaverse ecosystem. In this survey, we study the potential applications of Brain-Computer Interface (BCI) technologies that can enhance the experience of Metaverse users. By directly communicating with the human brain, the most complex organ in the human body, BCI technologies hold the potential for the most intuitive human-machine system operating at the speed of thought. BCI technologies can enable various innovative applications for the Metaverse through this neural pathway, such as user cognitive state monitoring, digital avatar control, virtual interactions, and imagined speech communications. This survey first outlines the fundamental background of the Metaverse and BCI technologies. We then discuss the current challenges of the Metaverse that can potentially be addressed by BCI, such as motion sickness when users experience virtual environments or the negative emotional states of users in immersive virtual applications. After that, we propose and discuss a new research direction called Human Digital Twin, in which digital twins can create an intelligent and interactable avatar from the user’s brain signals. We also present the challenges and potential solutions in synchronizing and communicating between virtual and physical entities in the Metaverse. Finally, we highlight the challenges, open issues, and future research directions for BCI-enabled Metaverse systems.

Index Terms—Metaverse, brain-computer interface, human digital twin, non-invasive BCI, computer vision, AI, IoT, sensors, VR, machine learning.

I. INTRODUCTION AND MOTIVATIONS A. The Development of a Human-Centric Metaverse

# T

HE term “Metaverse” was first coined by Neal Stephenson in his science fiction novel “Snow Crash” in 1992.

In this book, Stephenson described the Metaverse as a parallel existence of the physical and virtual worlds where users can interact with each other through their avatars. Although the idea of the Metaverse emerged 30 years ago, the technology was not yet ready for it until recent years. Recently, a large number of research and innovation efforts have been put into developing virtual reality (VR), extended reality (XR), and

Howe Zhu, Nguyen Quang Hieu, Dinh Thai Hoang, Diep N. Nguyen, and CT Lin are with University of Technology Sydney, Ultimo, NSW 2007, AU (e-mail: howe.zhu@uts.edu.au, hieu.nguyen1@student.uts.edu.au, hoang.dinh@uts.edu.au, diep.nguyen@uts.edu.au, and chin-teng.lin@uts.edu.au).

computing services to bring the Metaverse closer to reality [1]. Previously, VR and XR technologies have developed the first building blocks for the Metaverse, such as 3D video games, VR games, and later mobile XR games like Pokemon Go. The development of the Metaverse beyond games and social media platforms has begun to realize it as the next generation of the Internet. Recent works and products have explored Metaverse applications, such as healthcare [2], e-commerce [3], entertainment, and education [4]. These ventures have shown great potential for revenue growth in the Metaverse, even though the Metaverse has not yet been fully realized.

As the Metaverse is still in its early stages, many ongoing parallel multifaceted research areas and challenges, including VR/XR, human-machine interfaces, and computing services, require substantial investment and development. Recent works and surveys have attempted to define architectures for the Metaverse based on these components. One particular area is exploring a human-centric design to enhance users’ experience in the Metaverse [5]. A human-centric design is a method of utilizing a user’s behavioral, psychological, physiological, and observation information to improve the performance and usability of a system [6]. In principle, a human-centric approach is to design an intuitive system by incorporating the user’s potential state and modes of interaction. However, current human interaction methods, such as computer mouse clicks and keyboards, may not be intuitive within the new Metaverse experience.

Specifically, in Metaverse, the users can explore their surrounding environments using the control and sensory feedback from their hands, eyes, or thoughts in an immersive virtual environment [5], [7]. Although a large body of work has been proposed recently, the human-machine interfaces are lagging compared to other aspects of the Metaverse. However, humanmachine interaction is the primary channel that links the human body, the center of the Metaverse, to machines, i.e., any supporting devices and infrastructures. Conventional sensing techniques such as radio sensing, cameras, and wireless sensors can be utilized to develop a human-machine interface in the Metaverse. For example, face tracking, eye tracking, photogrammetry, computer vision, and motion capture can be used to construct fully immersive avatars in the Metaverse [8]– [10]. In Fig. 1, we illustrate a human-centric design for the Metaverse in which we focus on the interaction aspect of the users between the physical world and the virtual world. For this, the virtual world can be enriched by using the cognitive interactions of the users. Such cognitive interactions can be collected through sensing techniques such as eye tracking, voice detection, and computer vision.

Human body sensing

Brain-computer interface

Metaverse

fNIRS sensor

EMG sensor

XR headset

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

XR headset

EEG sensor

[Figure 5]

ECG sensor

[Figure 6]

[Figure 7]

[Figure 8]

IMU sensor

[Figure 9]

[Figure 10]

[Figure 11]

GPS

[Figure 12]

[Figure 13]

Temperature sensor

Body Emotion movement

[Figure 14]

[Figure 15]

Cognition

Consciousness

Facial expression

Body movements

Emotional states

Physical states

Behaviours

Human digital twin

Avatar

Behaviours Interaction

- Fig. 1. An illustration of a human-centric design for the Metaverse. Users’ information can be collected using human body sensing techniques, e.g., heart rate sensors, VR headsets, inertial measurement units (IMUs), and motion capture systems. Human characteristics such as body shapes, facial expressions, behaviours, and health can be revealed by analyzing the collected data. Unlike conventional human body sensing approaches, BCI can provide an alternative method to create intelligent avatars from a singular data source, i.e., human digital twins. Additional information from human users, e.g., emotional state and motion sickness, can be transferred to their avatars through BCI.

Using cognitive interactions of the users, or biological signals of the users in general, has shown its potential in designing and developing human-centric VR applications. For example, eye movement and heart rate data have been widely used in several applications, ranging from healthcare to robotics and virtual reality control [11]. Early findings showed that brain signals are encoded with a higher fidelity of sensory information than conventional sensing techniques, such as heart rate measurement and eye tracking. Toward this vision, Brain-Computer Interfaces (BCIs) have been considered in such applications as a neural interface between users and applications. As an attractive research area for exploiting human cognition in enabling technologies, BCI is inevitably becoming a part of the Metaverse.

B. Towards a Human-Centric Metaverse using BCI

This paper aims to provide a comprehensive survey about using BCI to enable a human-centric design for the Metaverse and discuss its associated communications challenges and future research directions/opportunities. BCI offers the ability to monitor the state of a Metaverse user and facilitate intuitive modes of user interaction within the Metaverse. BCI research began in 1875, Richard Canton, a British physicist, discovered the existence of electrical signals in the brains of animals. Only four decades later, Han Berger, a psychiatrist, invented the first measurement device allowing humans to measure the brain’s electrical activity for the first time [12]. After decades of research, BCI technologies exceeded their original scope in clinical trials and started attracting attention from the industry. Since the re-emergence of the Metaverse, researchers and industry have early adopted BCI as an enabling technology for the Metaverse [1]. BCI can provide rich information from brain activity for building virtual environments and digital avatars beyond conventional sensing approaches such as eye movement tracking, touch, and audible sensors. We believe that BCI technology enables the following unique opportuni-

ties in Metaverse that would be unachievable with conventional sensing:

- • Direct communication to the brain: BCI devices offer the unique ability to bypass the peripheral motorsensory nervous/bodily systems to communicate directly with the brain. The brain is the complex motor-sensory control center of the body. The capability to interface with the brain enables the real-time reading of motor actions before execution and the response to sensory information, as it is processed within the brain [13]. This also enables the Metaverse users to send voluntary and directed commands for communication and control, adding additional channels that convey highly relevant information about the users’ intent [14]. BCI can enable Metaverse users to relay complex commands, such as locomotion, limb movement, speech, and planned actions, to the Metaverse.
- • Multimodal information encoded onto a singular sensor: The brain serves as the body’s central nexus for motor-sensory information. A distinctive aspect of BCI sensors is the ability to capture the brain’s complex neurological activity. The data acquired from these BCI sensors offer rich and multimodal motor-sensory information condensed into a singular sensor signal [13]. These signals can encompass various cognitive processes, sensory stimuli, emotions, and motor functions. Within a Metaverse BCI system, this information can be harnessed and translated across various brain activities, including perception, attention, memory, language processing, motor control, and emotional states.
- • Higher degrees of encoded information within the signal: The degree of encoded information is a crucial drawback of conventional peripheral biomonitor sensors, such as cardiovascular, electrodermal activity, and motion tracking [15]. These sensors can reliably detect discrete changes in cognitive, mental and emotional states. However, they are less sensitive to transient or subtle shifts

- [16]. In contrast, the neurological signals measured on BCI sensors possess a higher degree of encoded information that can be used to accurately measure subtle changes in cognitive, mental, and emotional states [17]. Additionally, BCI signals can enhance our understanding of complex neurological states that cannot be measured through conventional sensing methods [18]. This capability can significantly enrich the understanding of the cognitive, mental, and emotional state of Metaverse users and enhance their personal experiences.
- • Intuitive control and natural interaction: BCI can tap into the user’s intentions, thoughts, and cognitive states. Instead of relying on overt physical actions, such as pressing buttons on a controller or moving a mouse, BCI can interpret the user’s internal mental states. BCI can be a supportive mechanism to convey user intentions and desires without needing explicit external movements, resulting in a more intuitive and seamless control experience [19], [20]. This BCI application can benefit individuals with limited or impaired motor function [21]. BCI can aid these individuals to regain control and interact with their environment using intact brain activity. In the Metaverse, an intuitive/natural user interface can enable a Metaverse avatar that acts as the virtual prosthesis/extension of a Metaverse user.
- • Universal Access: A valuable aspect of BCI technology is the ability to restore/replace motor functions for individuals with motor impairments, such as paralysis or limb loss [21]. BCI technologies can bypass traditional motor pathways and allow individuals to directly interface with various assistive technologies to enable interaction with their environments using their brain activities. BCI has the potential to significantly enhance the quality of life and enable individuals to perform tasks that would otherwise be challenging or impossible. BCI can also be integrated with other assistive technologies or input modalities to create multimodal interfaces [22]. If actualized, BCI can enable universal access for Metaverse users with disabilities. Within the Metaverse, users can experience all the features of the virtual environment without restrictions on physical or mental capabilities.

While there are several advantages to BCI technology, there are also several challenges hindering the integration of BCI for Metaverse users. The first challenge in the Metaverse is the construction of virtual embodiments, which involve multi-sensory data from the Metaverse users. Conventional user embodiment and user interaction schemes require many wearable and external sensing devices, such as handheld controllers for user input, wearable trackers for body kinematics, wearable cameras on head-mounted devices as facial sensors, heart rate trackers for workload and emotion measurement, and pupil cameras for eye movement tracking. Each sensing technique requires specific hardware devices, sensors, and customized software to serve a particular application, limiting the scalability and synchronization of multi-sensory data sources. In this case, BCI can act as a neural interface that integrates multiple sensing modalities, such as limb movement,

intentions, emotion, and eye movement, into a single wearable signal source [23]–[25]. The second challenge is a lack of individualization for the Metaverse technology. The multiple sensing modalities of conventional technologies also raise significant concerns about utilizing multi-sensory data sources to tailor applications to individual needs. As the sensing data come from different sources, it is challenging to fully utilize, synchronize, and distil information from different modalities, such as emotion recognition and eye movement [26]. Unlike traditional approaches, BCI offers an information source that can be individualized and tailored to the experience of individuals. The third challenge is the real-time or near real-time processing, and communications of BCI signals in Metaverse [27]. A critical factor is the scalability of the computation load and power for the large user base within the Metaverse. The current communications and computing capabilities will be insufficient to actualize the full-scale of the Metaverse. The fourth challenge is our limited knowledge of virtual embodiment, as we have not been able to fully actualize a virtual being/avatar in the Metaverse world. To address this challenge, we discuss the potential of a human digital twin (HDT) solution to provide a viable solution and open emerging applications for the Metaverse using BCI.

C. Related Surveys and Our Contributions

Various surveys have been conducted on the Metaverse, covering architecture, applications, technologies, security, and privacy concerns. In [5], the authors discussed the potential architecture and applications for the Metaverse. In [1], the authors examined the enabling technologies for the Metaverse from a cloud/edge computing perspective. In [28], the authors analyzed the potential applications of machine learning and deep learning for the Metaverse. In [7], privacy and security issues of the Metaverse were discussed in detail. These existing surveys about the Metaverse focus on general issues and technologies, often overlooking the incorporation of human factors within the Metaverse. Although the authors in [28] and [7] discussed the idea of using BCI as a neural interface between users and the Metaverse, none of them examined the BCI techniques involved in decoding human behavior. In [29], the authors considered potential BCI applications for the Metaverse. However, the context of the work was limited to the surface of BCI and the Metaverse. For example, the authors did not address the applications, limitations, and challenges, such as synchronizing and communicating between entities, let alone applying them in the Metaverse. Overall, BCI was not discussed in detail in the aforementioned surveys. To the best of our knowledge, our survey is the first in the literature to comprehensively discuss BCI’s potential in the Metaverse.

In particular, in this survey, we aim to provide a comprehensive survey about BCI technologies and their potential for future development of the Metaverse. Furthermore, we propose and discuss a new concept of Human Digital Twin (HDT), a new approach to constructing human embodiment within the Metaverse using BCI. In summary, our main contributions are as follows:

• We provide the fundamental background and discuss the

Section I. Introduction and motivation

- I-A. Development of a

human-centric Metaverse

I-B. Towards a human-centric Metaverse using BCI

I-C. Paper organization

- II-A. The Metaverse

II-B. Brain-computer interface: sensor technology

II-C. Deployment of BCI within the Metaverse

- III-A. BCI emotional and cognitive state recognition

III-B. Anomalous and error-related behaviors detection

- IV-A. Decoding thoughts and intentions using BCI

IV-B. Social interaction using imagined speech

- V-A. Key technologies to enable human digital twin

Section II. Background

Section III. BCI-enhanced user immersion

Section IV. BCI-enhanced Metaverse user interactions

Section V. Human digital twin

V-C. Potential challenges for human digital twin

V-B. Human digital twin interaction

Section VI. Challenges, emerging applications, and research directions

VI-B. Emerging Applications and Future Research Directions

VI-A. Current challenges

Section VII. Conclusions

- Fig. 2. The organization of the survey.

current challenges of the Metaverse that conventional sensing approaches could not effectively address.

- • We provide the background of BCI, focusing mainly on non-invasive BCI, which is more suitable for commercial applications. We then describe how BCI technologies can enhance user embodiment within the Metaverse. We also review BCI-enabled interaction schemes for the Metaverse users and describe the differences between the BCI sensing technologies and the conventional sensing techniques.
- • We introduce the new concept of HDT. With HDT, we can develop individualized Metaverse applications and enhance our knowledge of virtual embodiment in the Metaverse. We further discuss potential challenges for integrating HDT in the Metaverse, such as realtime communications, synchronization, and interactions between HDTs.
- • We highlight the challenges, open issues, and future research directions of BCI technologies for the Metaverse. The ethics and security of using BCI for the Metaverse are also discussed. Alternatively, the potential applications, such as brain communications, are also discussed.

D. Paper Organization

As illustrated in Fig. 2, our paper is organized as follows. Section II provides the background of the Metaverse and BCI technologies. Section III provides more details about BCI technologies, including emotional and cognitive state recognition

for the Metaverse. This section further discusses the potential approaches to prevent error-related behaviors, such as VR motion sickness, stress, and fatigue, in the Metaverse. Section IV describes the potential interactions between the users and the Metaverse through BCI. This section also discusses VR-BCI user interface design paradigms for the Metaverse applications. In Section V, we propose a new concept of the HDT in which the digital twin is utilized to create twin entities for human users from their brain signals. We also discuss challenges in synchronizing and real-time communication between virtual and physical entities. In Section VI, we highlight the current challenges, open issues, and future research directions toward BCI-enabled Metaverse systems. This section also discusses ethics, security, privacy issues, and emerging applications, including hardware, software, and algorithm designs. Finally, Section VII concludes the paper. In addition, we provide a list of abbreviations and descriptions used in this paper in Table I.

II. BACKGROUND A. The Metaverse

The term “Metaverse” is a combination of the prefix “Meta” (meaning beyond) and the suffix “verse” (meaning universe). As its name suggests, the Metaverse is a universe of the next-generation Internet that allows the parallel existence of the physical world and shares 3D virtual worlds. The earliest concepts of the Metaverse can be found in classical MMO (Massively multiplayer online) games [30]. In these games, users are given a uniquely singular persistent virtual world as a medium for social and worldly interactions. The Metaverse shifts this paradigm by incorporating modern technology to generate a seamlessly immersive experience transitioning between the physical and virtual worlds. The envisioned Metaverse is where users can naturally (touch the environment with their hand or walk with their feet) move and interact with the virtual environment as though they are in the physical world [5]. Unlike conventional interactions in the current Internet, where we use devices such as a mouse, cursor, and keyboard, the Metaverse enables users to immerse applications and services through their digital avatars with supporting VR and XR technologies. As a result, users in the Metaverse can potentially eliminate Spatio-temporal barriers in how they work, live, and entertain. To this end, the Metaverse can be developed from the convergence of multiple supporting engines such as VR/XR, digital twin (DT), tactile Internet, artificial intelligence (AI), and blockchain-based economy [1].

To create an immersive Metaverse experience, various technologies must be integrated and coordinated. In the following, we highlight the essential technologies for human-centric Metaverse design, but emerging technologies are not limited to this discussion as the Metaverse is continually evolving. Considering the left side of Fig. 1 as an example, multiple technologies are used to create a virtual avatar, including wireless sensors, sensor fusion, interpretation with machine learning, 3D projection from data, and 3D view synthesis. Machine learning/deep learning algorithms can be utilized to fuse the data collected from the sensors effectively [8], [9]. These

TABLE I LIST OF COMMON ABBREVIATIONS USED IN THIS SURVEY

|Abbreviation<br><br>|Description|Abbreviation<br><br>|Description|
|---|---|---|---|

|HDT|Human Digital Twin<br><br>|VR<br><br>|Virtual Reality|
|---|---|---|---|
|XR|Extended Reality<br><br>|EEG|Electroencephalogram|
|DoF|Degree-of-Freedom<br><br>|AI<br><br>|Artificial Intelligence|
|IoT<br><br>|Internet of Things<br><br>|QoE|Quality-of-Experience|
|ECoG<br><br>|Electrocorticography|MEG<br><br>|Magnetoencephalogram|
|fNIRS<br><br>|Functional Near-Infrared Spectroscopy|fMRI<br><br>|Functional Magnetic Resonance Imaging|
|FOV|Field of View<br><br>|HMD|Head-mounted Display|
|ERN<br><br>|Error-related Negativity<br><br>|MI|Motor Imagery|
|SSVEP|Steady-State Visual Evoked Potential<br><br>|TDMA|Time Division Multiple Access|
|MISO|Multiple Input Single Output<br><br>|MIMO<br><br>|Multiple Input Multiple Output|
|SDMA<br><br>|Spatial Division Multiple Access<br><br>|NOMA|Non-Orthogonal Multiple Access|
|RSMA<br><br>|Rate-Splitting Multiple Access|MMO<br><br>|Massive Multiplayer Online (a video game genre)|

learning algorithms can further capture user data patterns, e.g., body shape, behaviours, poses, and expressions, and then prepare the data to be projected into the virtual environment. Finally, the virtual avatar is placed into the virtual scene (with VR) or mixed environment (with XR). The user’s experience in the VR/XR environment can be enhanced by optimizing the view, angle, resolution, and interaction within the scene [5]. Extra haptic feedback can also be utilized to generate realistic feelings about the virtual environment [25], [31]. Other necessary technologies include intelligent sensing, data compression, edge computing, and wireless multiple access to reduce latency and improve reliability [1].

Beyond gaming, governments and tech companies seek a presence in the Metaverse. Decentraland lets users create, explore, and interact with 3D virtual worlds owned and controlled by themselves [32]. Users buy virtual land as NFTs via MANA cryptocurrency, which uses the Ethereum blockchain. NVIDIA’s Omniverse introduces a computing platform for creating Metaverse applications such as 3D scene generation, art creation, and robotic control with supportive generative AI and physic-based simulation engines [33]. Microsoft’s Mesh brings a new toolset for users to create custom workplaces and tools harmonized with other applications in Microsoft’s ecosystem, such as Teams [34]. Other Metaverse apps focus on healthcare and education, such as Xirang [35] and Telemedicine [36].

Besides using conventional sensing and data collection techniques, integrating human physiological and psychological information is crucial for developing human-centric Metaverse applications. As motivated by the fact that the brain signals are encoded with rich information about human activities, in the following, we discuss the details of BCI technology and how BCI can offer multimodal, low latency, and high fidelity metrics for Metaverse user behavior [37].

- B. Brain-Computer Interface: Sensor Technology

The human brain is the most complex and adaptive organ within the human body [38]. It is the control center of human intelligence, sensory perception, and motor functions. Herculano-Houzel [39] estimated that the central brain might contain around 86 billion neurons. Each neuron is a node along trillions of neural pathways within the brain. Each neural pathway passes neuroelectric signals (neurotransmission) around the brain, forming a system that enables the brain

BCI

Invasive BCI

Semi-Invasive BCI

Non-Invasive BCI

Implanted electrodes between surface of cortex and skull

Implanted electrodes beneath skull and within cortex

Outer electrodes and/or sensing technologies

MEG, fNIRS, fMRI, EEG

ECoG

Fig. 3. Three types of BCI devices/sensors: invasive BCI, semi-invasive BCI, and non-invasive BCI.

to function by communicating with the nervous system. A broad definition of Brain-Computer Interface (BCI) is any device that measures, analyzes, and interprets the brain signal (neural pathways) and then relays information to a machine to respond. The story of BCI begins with a discovery made by the British physicist Richard Canton [12]. In 1875, Canton discovered the existence of electrical signals in the brain of animals. This discovery paved the way for the pursuit of electrically mapping brain signals and a better understanding of human neurophysiology. Four decades later, a psychiatrist named Han Berger invented the first measurement device, allowing humans to measure the brain’s electrical activity for the first time [12]. Berger created the tool and discovered the first neural oscillation frequency, the 8-12 Hz Berger (Alpha) wave. In modern times, researchers furthered these discoveries by developing various ways to measure the brain’s neural signals, learning new neurophysiological behaviors, and building autonomous systems. BCI refers to technologies that can create communication pathways from the brain’s activity to external devices, such as a computer or a machine [37]. BCI devices/sensors are delivered in one of three forms, invasive, semi-invasive, and non-invasive, as illustrated in Fig. 3.

Invasive BCI devices characterise electrodes implanted (through surgery) beneath the skull and within the cortex (direct signal acquisition from the brain). Invasive BCI systems are not in a mature stage of development to be safely used

[Figure 16]

Fig. 4. This figure presents the two types of non-invasive EEG-based BCI devices available on the market: (a) the Brain Products’ actiCAP active 64channel wet EEG electrodes system; (b) the Cognionics Quick-20 dry EEG electrodes system; and (c) the layout for both the 10/20 EEG channel layouts used in both systems. Pictures were taken from the Computational Intelligence and Brain-Computer Interface (CIBCI) lab at the University of Technology Sydney (UTS), Australia.

BCI systems

EEG MRI fNIRS ECoG MEG

Data processing

Observed effect

Document finding

Brain's neural pathways

or

[Figure 17]

Computation classifier

Repeat task to improve classifier

Output system

Fig. 5. An overview of the pipeline of BCI systems. The figure illustrates the acquisition of a signal through various types of BCI systems. Once a signal has been acquired, information can be extracted for observational purposes (monitoring or measuring a state) or classified into a specific behaviour (detecting intentions or tasks).

as consumer devices. Invasive BCI require longer dedicated research with animal populations before engaging in lowsample-sized human research studies [40]. Invasive BCI is often employed in extreme cases (e.g. severe motor disability) where the patient’s quality of life benefits from the BCI outweighs the risks [41]. Companies, such as Neuralink, are pursuing the goal of implantable BCI devices [42].

Semi-Invasive BCI devices are sensors that are implanted (through surgery) between the cortex (on the surface) and the skull [22]. Semi-invasive BCI systems commonly use an array of Electrocorticography (ECoG) electrodes to map a specific brain region. The surgical procedures and implant durability for semi-invasive BCI typically carry lower short to longterm risks when compared to invasive BCIs. Semi-invasive electrodes offer a higher-quality signal; however, similar to invasive BCI, the surgical risks outweigh the benefits of the device. Due to the risks of invasive and semi-invasive devices, non-invasive systems are more popular as a low-risk and more viable product for researchers and consumers. With further research, reduction in surgical risks, and improved robustness of implants, invasive and semi-invasive BCI devices will have great potential to enhance the user experience within the Metaverse dramatically.

Non-Invasive BCI devices encompass multiple technologies that can detect neurophysiological behaviours without any implanted electrodes; this includes technologies such as Magnetoencephalography (MEG), Functional Near-Infrared Spectroscopy (fNIRS), Functional Magnetic Resonance Imaging (fMRI), and Electroencephalography (EEG). Certain noninvasive BCI systems, such as fMRI and MEG, lack portability due to equipment size or complexity. These types of systems are not feasible as wearable devices for Metaverse users. EEG and fNIRS-based BCI systems are the primary feasible solution for a portable, wearable, and accurate device that can be used in a general consumer capacity [43]. Typically, EEG devices use wearable scalp electrodes (see Fig. 4) with a highly conductive material to measure the voltage (µV) fluctuations on the wearer’s scalp [44]. On the other hand, fNIRS electrodes utilize near-infrared spectroscopy to discern cortex neural activity [45]. Certain systems offer paired EEGfNIR electrodes within one system [46]. These types of electrodes will measure neural signals, which are then amplified and digitized for analysis. The resulting signal may contain

multiple components (depending on electrode placement), such as eye blinking, muscle movement, movement artifacts (from displaced channels), and other electrical activity. Most importantly, the signal will contain information on the brain’s electrical activity [47]. Through extensive repeated measure research and machine learning, common neurophysiological behaviors can be classified and used for various research applications, e.g., military, rehabilitation gaming, medicine, mental health, robotics and automation, and public services [48]. Therefore, wearable non-invasive EEG/fNIRs BCI devices are most suitable for researchers and consumers exploring the Metaverse.

EEG devices typically consist of two types, wet and dry (see Fig. 4) of electrode systems [49]. Wet electrodes refer to any electrode system that requires conductive gel or saline fluid to improve the contact connectivity between the electrode and the wearer’s scalp. In contrast, dry electrodes leverage optimized electrode shapes (often hair comb-like) to contact the scalp without needing gel/fluids. When comparing the two types, wet electrodes offer a better signal quality (less noise from impedance and external sources) but require preparation (applying gel/fluid) and a limited operation time due to the drying of the gel/fluid. Dry electrodes are generally larger than wet electrodes, limiting the total possible electrodes placed on the scalp, the overall signal quality (large electrodes are more susceptible to movement), and the user comfort when wearing the device [50]. Both types of EEG systems are limited by movement noise, device usability (user comfort and real-world practicality), and neurodiversity [47]. Unlike EEG, fNIRs do not require conductive gel as the sensors primarily use light [51]. The key drawback to consumer fNIRS devices is the requirement of paired sensors (a source and detector) to measure neural signals. A 64-channel system would require 128 fNIRS sensors compared to the 64 EEG electrodes. The current size of the fNIRS sensors makes the system unideal for consumer use, as dry EEG electrodes could achieve a similar result with fewer sensors. Therefore, given the realworld feasibility factors, EEG dry electrode BCI systems are currently ideal for Metaverse users. It is likely that with further improvement to signal processing techniques, machine learning algorithms, and hardware design, we will find that dry electrode EEG with fNIRS BCI devices will become the next popular consumer device.

Brain signals extraction

Local processing Communication channel & classification

[Figure 18]

[Figure 19]

Cloud/ Service provider

[Figure 20]

Internet access

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

Synchronising Metaverse avatars

Metaverse user

[Figure 26]

[Figure 27]

Adaptive environment rendering

[Figure 28]

Emotion/cognitive state

Imagined speech

Social interaction

[Figure 29]

Metaverse

[Figure 30]

Active BCI paradigm

User interaction

[Figure 31]

Digital Avatars

Error-related BCI

World management

Adapted visual/haptic settings

- Fig. 6. An illustration of the integration of BCI with the Metaverse. Through BCI, the Metaverse user’s brain signals can be extracted, processed, and communicated into the Metaverse. The figure outlines the types of information that can be obtained from the BCI device and integrated into the Metaverse.

Signal processing is another important aspect of BCI devices. Fig. 5 outlines the typical workflow of BCI-related research [52]. The two principal methodologies further enhance our knowledge of the neurophysiology of the brain to enhance BCI systems through signal feature recognition (built through observational information). The other is to develop real-time systems through classifiers (machine learning or AI). BCI research has expanded to many interdisciplinary research fields, studying behaviors such as cognitive states, emotional responses, pathology (neurology), mental health, pedagogy, ergonomics, and many other fields [53]. The current challenge for BCI systems is to develop a real-time “plug and play” system for consumer use [54].

- C. Deployment of BCI within the Metaverse

In Fig. 6, we illustrate a BCI-enabled Metaverse in which BCI plays a vital role as an interface to create adaptive virtual environments and intelligent avatars, supported by other technologies such as a digital twin and real-time communications. As illustrated in Fig. 6, a BCI-enabled Metaverse is a humancentered approach in which BCI and VR technologies can coexist and cooperate in a closed loop. Within the conventional BCI research field, there are many examples of VR-BCI integration [15], [55]–[57] through using a traditional wet electrode EEG cap (see Fig. 3(a) and Fig. 7) under XR/VR device. This method of VR-BCI integration is viable in a research context because of the importance of signal quality and spatial resolution from the BCI operating in a controlled environment. This VR-BCI set-up would not be feasible for a real-world consumer because the wet sensor would only provide limited usage as the gel would rapidly dry out. A commercially available option to enable VR-BCI is to use dry electrodes integrated into the VR/XR device, such as the Galea VR HMD [58]. A dry electrode system will enable a portable system with lower signal quality and spatial resolution.

The basic operation of the BCI-enabled Metavese may include the following steps. The VR-BCI interface extracts the users’ brain signals and processes the signals locally or remotely at a computing unit, e.g., a remote server. Brain signals extraction, processing, and classification are enabling processes for creating human-like digital avatars with unique characteristics of the users, e.g., emotional state, visual stimulus, and behaviors, from the human brain signals. The communication channels, such as wired and wireless channels, further enhance the scalability of the Metaverse system. The Internet-connected computing unit will update and synchronize the information into the Metaverse. By monitoring the brain activities of the users, the Metaverse platform can analyze or predict the users’ behaviors, attention, or emotional states and adjust VR settings to be transmitted back to the users. As such, the service provider can actively provide customized and personalized Metaverse applications for the users. Note that other users in the Metaverse also contribute to the dynamics of the above process. In addition, other supporting technologies, such as digital twins, integrated VRBCI devices, and real-time communications, can facilitate and improve the completeness of the system. BCI can be directly used to measure Emotion/Cognitive states of the Metaverse user and facilitate social, active, and passive interaction within the Metaverse.

III. BCI-ENHANCED USER IMMERSION

Immersion is the degree of realism for the congruence (between the real and virtual worlds) of the sensory input and motor output. Immersion plays an essential role in the Metaverse user experience. A fully immersed Metaverse user can seamlessly transition between the physical world and the Metaverse. Therefore, the modulation of the immersion levels of the environment can directly affect the believability and acceptance of the Metaverse. BCI can improve the immersion of the Metaverse user by altering the rendering of the virtual

[Figure 32]

- Fig. 7. An illustration of a VR user using a VR headset (HTC Vive Pro) with a BCI sensor cap (64 channel EEG, Liveamp system) worn under the headset. The user is experiencing a mixed reality environment where they are physically (through the platform) and virtually (through VR) elevated. The picture was taken from the Computational Intelligence and Brain-Computer Interface (CIBCI) lab at the University of Technology Sydney (UTS), Australia.

Stress Happiness

Calm Sadness

Emotional state

Workload Fatigue

[Figure 33]

Excited

Valance

Unpleasant Pleasant

Stressed

Depressed

Drowsy

Calm

Arousal

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

Cognitive state

Machine/Deep learning classifier

Russell circumplex model

Arousal frontal activity

Valence hemishpherical asymmetry

Workload/fatigue

BCI

[Figure 38]

Stressed Excited Depressed Calm

[Figure 39]

Virtual event

Metaverse

- Fig. 8. An illustration of the emotional and cognitive state measurements using BCI. These types of information can be utilised in the Metaverse to provide status indicators and improve the immersion of Metaverse users.

environment based on the user’s emotional and cognitive state. Previous works explored this concept [59] using passive BCI techniques to adaptively change the game environment’s lighting and Field of View (FOV), thus enhancing the user’s immersion. Passive BCI refers to using BCI to detect and measure changes in a user’s unintentional cognitive and emotional state [60]. In this section, we explore two potential methods of using BCI to enhance the user’s immersion in the Metaverse. Specifically in Section III-A, we explore the user’s emotional (including happiness, sadness, stress, calmness, anxiety, and uneasiness) and cognitive state (mental workload, fatigue, and attention) as shown in Fig. 8. After that, in Section III-B, we present the potential of using anomalous and error-related neurological behaviors to enhance immersion by correcting anomalies within the Metaverse.

A. BCI Emotional and Cognitive State Recognition Applied to the Metaverse

A person’s emotional state is commonly quantified by a scale of valance (pleasant to unpleasant) and arousal (alertness to drowsy). This mode of mapping a person’s emotional

spectrum is known as the Russell Circumplex model of affects [61]. Fig. 9(a) presents the Russell Circumplex models and shows the spectrum of emotional states quantified by the arousal and valance level. This understanding was furthered by the Yorkes-Dodson law [62] (see Fig. 9(b)) that found a direct correlation between human emotional arousal and cognitive performance. Therefore, the ability to quantify and measure human emotional states can play an essential role in understanding an individual cognitive state. The BCI classification of emotional states involves extracting specific EEG features for arousal and valance from the EEG signal for a machine learning classifier to detect [63]. Arousal is detected through the changes in the brainwaves in the brain’s frontal region. Brainwaves are common oscillations in the brain’s electrical activity that correlate to various neural activities. The brainwaves are broken down into the Gamma (>35 Hz), Beta (12-35 Hz), Alpha (8-12 Hz), Theta (4-8 Hz), and Delta (0.5-4 Hz) wave. Studies [64]–[66] found a strong correlation between an individual’s arousal level and the frontal Beta, Alpha, and Theta power. The ratio between Beta and Alpha activity is commonly used to measure arousal level. Typically, the Beta brainwave would indicate an active mental state.

Arousal Performance

Stressed

Excited

Unpleasant Pleasant

Valance

Calm

Depressed

Drowsy

Stress/arousal

(a) (b)

- Fig. 9. This figure presents (a) the Russell Circumplex model of Affects, which is used to measure emotional states on a spectrum between arousal and valence; and (b) the Yorkes-Dodson Law dictates the relationship between emotional arousal/stress and cognitive performance.

Conversely, the Alpha brainwave suggests a relaxed and restful state. Therefore, heightened arousal can be measured by a frontal region increase in Beta power and a decrease in Alpha power. An individual’s valence level is measured through the brain’s hemispherical symmetry/asymmetry. Hemispherical symmetry refers to an equal/similar activation (neuron firing) state between the brain’s left and right cortex. Hemispherical asymmetry occurs when one cortex has significantly more activity than the other. Studies [67]–[69] showed that valence correlates to the degree of hemispherical symmetry with a strong hemispherical asymmetry exhibited when in a negative valance (unpleasant) state. Works by [70] and [71] used BCI and machine learning to classify the dimensions of an individual’s arousal and valence levels, which indicate their emotional state.

- A person’s cognitive or mental state refers to their mental

well-being and the ability to think or process information. A Metaverse user’s mental and cognitive state can significantly impact their experience within the Metaverse. A high workload (complex or challenging to navigate environment) or sensoryloaded (high noise or colour intensive) environment can trigger negative mental states, reducing the user’s immersive in Metaverse. Factors such as the current emotional state, experience of mental workload, fatigue level, and attention level can directly affect a person’s cognitive state. Like emotional states, cognitive state features are extracted by evaluating the brainwaves of specific brain regions. The theta activity in the frontal cortex often determines mental workload. Studies by [72] and [73] asserted that as the difficulty of a task (higher workload) increases, the theta activity in the frontal cortex will increase.

Interestingly, the inclusion of multimodal data sources such as cardiovascular (changes in heart rate) and pupillary activity (changes in pupil dilation) can improve the accuracy of the workload classification [17]. Mental fatigue resulted in the increase in theta and alpha activity and the decrease of beta activity in the frontal cortex [74]. Studies on attention discovered that a distracted (unfocused) individual would exhibit a decrease in beta power in the frontal region, an increased theta and delta power in the central region, and a decrease in alpha power in the parietal region [75], [76].

Fig. 10 depicts using passive BCI to create an adaptive Metaverse display to enhance the user’s immersion. Using

passive BCI to gauge a user’s emotional and cognitive state is a well-researched area with multiple reliable classifiers to enable the technology. When introduced to the Metaverse, passive BCI can dynamically adjust the user’s surrounding environment and render display to improve the user’s immersion. An example of this was the adaptive virtual reality environment by [77]. By measuring the VR user’s emotions, the system created a feedback loop that used the virtual environment to modulate the user’s emotional state. Similarly, the works by [78] and [59] explored limiting and adjusting an environment’s complexity to improve the user’s cognitive state. These works would use adjustable lighting and fog to moderate the amount of the visible virtual environment to reduce the user’s workload and visual fatigue. These practices could be applied to the Metaverse through an integrated BCI VR device to create a feedback system that adaptively adjusts the rendered environment. This solution is very close to realization with the recent innovations such as the workload measurement integration in the HP G2 Reverb VR HMD [79] and the dry electrode BCI integrated Galea VR HMD [58].

B. Anomalous and Error-related Behaviours to Improve User Immersion

Another unique functionality of passive BCI is the ability to detect potential adverse events before consciously recognising the event. Adverse and anomalous events can hinder user immersion by creating a disassociation between the expected real-world and the Metaverse. Examples of this could be events such as the onset of VR sickness, loss of balance/falling, or environmental errors. The real-time detection of these events allows the implementation of safety and preventative measures to improve the user’s longevity within the Metaverse. Through extensive studies, each adverse event’s unique EEG signal features can be reliably extracted and classified.

VR sickness refers to the sensation and experience of symptoms such as headaches, nausea, vomiting, drowsiness, and disorientation when using VR [80]. This is relevant for Metaverse applications, where users often spend prolonged periods in virtual environments. When VR sickness occurs, users often disengage from the virtual environment to alleviate the symptoms. In extreme cases, it may result in fainting, falling (due to loss of balance), or severe nausea. These types of adverse events will negatively affect the user’s sense of immersion and reduce the longevity of the Metaverse user to stay within the Metaverse. Certain VR Studies [81]–[83] have successfully used EEG signals to classify and detect when a person is experiencing VR/motion sickness. They found a significant correlation between VR/motion sickness and theta and delta bands activity within the occipital lobe (attributed to the sensory perception of motion). They also observed a decrease in alpha activity in the parietal and motor regions. The loss of balance or falling is another significant risk for VR Metaverse users [56]. Studies by [84] and [85] show that the beta and theta band activity in the parietal/motor cortex is closely related to losing balance and falling. These VR sickness and falling indicators can be trained through an AI classifier to detect anomalous events in real time

Adaptive display Alter environment appearance

Emotional state (stress, meditation, uneasiness)

[Figure 40]

| | |
|---|---|
| | |

BCI-VR user

| | |
|---|---|
| | |

[Figure 41]

Modulate environment complexity

| | |
|---|---|
| | |

[Figure 42]

Highlight specific areas

Cognitive state (mental workload, fatigue, attention)

Enhance Metaverse user immersion

- Fig. 10. This figure shows using passive BCI to detect the Metaverse user’s emotional and cognitive state. Then using, the measured information to modulate different factors of the Metaverse display to enhance the user’s immersion. The picture was taken from the Computational Intelligence and Brain-Computer Interface (CIBCI) lab at the University of Technology Sydney (UTS), Australia.

during a Metaverse experience. The ability to effectively detect VR sickness and falling can allow the implementation of preventative techniques such as reducing the motion of the virtual environment and turning on VR see-through mode [56].

In the continuity of the Metaverse, errors and visual bugs are inevitable factors that will appear within the virtual environment. Erroneous artifacts or system glitches can hinder a user’s immersion. Therefore, it is essential to have a system in place to detect and correct these errors. One proposed method that BCI could solve this issue through error-related negativity (ERN) detection (see Fig. 11). ERN is a signal response that occurs when a person observes incongruent or erroneous stimuli within a task or environment [86]. ERN is characterized by a negative potential around 50-250 ms after the error [87]. Previous studies [57], [88] have successfully classified the ERN response as an error correction method within a VR environment. Due to the simplicity of ERN, it can be reliably implemented to detect potential errors that Metaverse users may observe. This solution would enable a more efficient (compared to manual user reporting) method of detecting and correcting potential errors within the Metaverse environment.

These BCI solutions can improve the safety and longevity of a Metaverse user. By incorporating the outlined BCI techniques, the Metaverse system can become more reactive to adverse events and use an appropriate strategy to prevent or correct the problem. There are two critical challenges to the implementation of this system. The first challenge is ensuring the ability to accurately detect the onset of the adverse event before the occurrence or conscious recognition of the event. The system would not be valid if it cannot prevent the adverse event from occurring. The second challenge is the explore practical strategies for preventative and corrective methods. The current methods of prevention or correction involve removing the user from the virtual environment and breaking their immersion. Better methods are required that do not require the removal of the user from the Metaverse.

Intended behaviors Unintended behaviors

[Figure 43]

[Figure 44]

Anomalous state detection

Attention levels

Lost of balance

[Figure 45]

[Figure 46]

VR sickness

Pathological problems

Situational awareness

Virtual event

Falling

Fig. 11. This picture illustrated the use of BCI to detect anomalous states and error-related behaviors. Using the BCI signal (e.g. ERN), the system can detect and correct adverse events, such as when the user is about to fall due to VR sickness.

IV. BCI-ENHANCED METAVERSE USER INTERACTIONS

An important aspect of the Metaverse is to deliver a platform to facilitate meaningful user interaction. A Metaverse user must be able to interact with the environment (pick up objects and locomotion) and socially with other Metaverse users. Active BCI offers the potential to generate more intuitive modes of user interaction within the Metaverse. In contrast to passive BCI, active BCI refers to the user of BCI performing specific tasks through intentional, conscious thought. This section will explore the ways BCI can be used for users to interact with their environment (Section IV-A) and the potential of using BCI for social interaction through brainto-text (Section IV-B).

A. Decoding Thoughts and Intentions Using BCI to Improve Metaverse Interactions

Understanding human thoughts and intentions is a commonly sought-after goal in the BCI research field [89]. Tradi-

[Figure 47]

- Fig. 12. This figure presents the common BCI paradigms used for designing user interfaces and the potential of using brain-to-text for social interactions.

tional systems rely on tactile manipulators, such as controllers, buttons, joysticks, levers, and keyboards, to allow users to convey their intentions to a system [90]. Other works explored voice recognition, gesture control, and AI to develop more intuitive methods of understanding user intention [91]. BCI offers the potential for direct translation between human thought and intention, which could result in an intuitive and responsive system. The underlying challenge in understanding human intention is the complex multilevelled nature of the human mind [92]. Human intention ranges from low-level cognitive decisions based on sensory perception (reacting to events, bodily movements, or simple choices) to complex high-level decisions requiring observation, planning, mental stimulation, and multistep execution. Based on this challenge, researchers have designed reliable active BCI paradigms to capture specific behaviors that are exhibited across the human population. When designing an active BCI system, one typically selects a reliable BCI paradigm to translate intentional thought into a classifiable EEG signal. We will highlight three of the most common paradigms used for active BCI control (as shown in Fig. 12); these are P300, Motor Imagery (MI), and Steady-State Visual Evoked Potential (SSVEP).

P300: The P300 wave is the oldest and potentially the most well-known EEG response out of the three paradigms. As described by [93], the P300 wave is a positive peak human event-related potential that occurs around 300ms after a ‘target’ stimuli are perceived. This P300 peak can be observed across the brain’s frontal, central, and parietal regions. The stimuli used for P300 paradigms can be both visual and auditory. Typically, P300 paradigms feature an oddball design where the user has a target and several non-target stimuli. A signal classifier can discern whether the user observes a target stimuli by detecting the positive peak amplitude. The P300 speller [94] is a successful example of using a P300 wave to create a user interface. In this paradigm, the user will decide their target or intended letter to type; then, multiple visual letter stimuli will sequentially appear to the user. The classifier will detect the P300 response within the EEG signal and input the letter that appeared 300ms before the peak as the user’s choice. Generally, P300 paradigms provide a reliable signal response for detection; the primary drawback is the speed of stimuli presentation (slow rate of input) and the dependency on user focus on the target stimuli (difficult to use in complex

environments).

MI: An MI paradigm utilizes the thought of left and right motor action to create a simple control paradigm [95]. MI involves the extensive training of a classifier that detects left and right motor actions (participants will clench their left or right hand) within the motor cortex. The classifier model relies on the hemispherical activations between the left and righthand actions. Once sufficient training is complete, the user will train the classifier using the thought of left and right motor actions. Previous studies [95]–[97] found that the mere thought or representation of a motor action can trigger a response in neurological pathways for actual motor action. This results in a reliable and detectable signal for left and right control without the need for ’real’ motor action (not even tensing). MI’s primary benefit is the lack of need for visual or auditory stimuli. However, MI requires extensive training individualized for each user and is more susceptible to noise if the user is mobile.

SSVEP: The SSVEP paradigm is popular with multiple visual flashing stimuli that flicker at specific frequencies. SSVEP BCI studies [98], [99] show that when a person observes flickering/flashing visual stimuli, a synchronized frequency activity can be observed in the occipital region of the brain. In essence, if multiple flickering input control options are presented to the user, the frequency of the occipital region’s activity can be used to determine which control option the user is focused on or targeting. SSVEP offers the advantage of not requiring extensive training while being a reliable paradigm for detection. The main drawback of the SSVEP paradigm is the argument that the stimuli require too much attention, as flickering visual stimuli will likely distract or block out the surrounding environment.

Basic interactions and low-level intentions can be translated through active BCI paradigms such as P300, MI, and SSVEP. High-level decisions present are far more challenging to decode. Many works explored various areas of the hierarchy of executive decision-making [100]. One example of a higherlevel decision-making process is active spatial navigation [18]. The work investigated the use of BCI during active spatial navigation to understand the neurophysiological behaviors of a user when processing spatial information when navigating complex environments. The authors observed that the retrosplenial complex (RSC, a cortical region of the brain) theta

Emotion/cognitive Imagined speech state indicator

[Figure 48]

Happy/tired How are you?

[Figure 49]

Thought handwriting How are you

Translated text How are you

- Fig. 13. An illustration of using imagined speech enabled by BCI to perform thought-based social interactions. The figure depicts an example of how EEG data can be decoded into handwriting and then text to be used for imagined speech communication.

activity correlates when a user engages in active spatial navigation (identifying spatial locations around the user). These biomarkers can provide an indication of whether a user is lost within a complex Metaverse environment. Other works explored the use of AI to build training models which observe specific behaviours/interactions of the user and attempt to decode the neurological behaviours (such as robotic systems interaction [101]–[103]. In conjunction with other multimodal information and more advanced AI modelling, BCIs can be used to infer and decode many complex thoughts or intentions. These mechanisms can be applied to the Metaverse to understand the user better and facilitate a more intuitive user experience.

- B. Social Interaction Using Imagined Speech

The ability to input semantic information is an essential form of communication in human society. In the digital era, the keyboard has become a ubiquitous tool that enables a human to translate written language into a digital form that can be communicated between humans and computers. A key challenge in the Metaverse is to provide effective communication methods for social interaction. The straightforward approaches are to use a virtual keyboard [31] or use a microphone for direct speech [104]. In the traditional line of thought, BCI can offer keyboard and letter selection solutions through P300 [94], MI [105], and SSVEP [106]. However, it could be argued that these methods would be inherently less efficient than traditional ones. We believe that the more significant application of BCI for communication is the potential of creating a new communication medium called ‘imagined speech’. By decoding human thoughts, semantic comprehension, and emotions, BCI could allow individuals to communicate through their thoughts alone [107], [108].

A recent innovation is the research by [109], which explores decoding brain activity into text. This offers the ability for the Metaverse user to interact socially by thought alone. Various works achieved this feat [109]–[111] in which ECoG, an implanted electrode grid, provides spinal cord injury patients with the ability to generate text through thought. This technique decodes the brain’s motor cortex region to interpret the thought or representation of the handwriting motor action (similar to MI). Then, the handwritten text is translated via deep learning into digitized signals. As suggested by [112],

this technology enables imagined speech communication between the Metaverse and real-world users. In principle, the finding from the ECoG results can be applied to EEG BCI devices. Fig. 13 illustrates an example of using EEG signals to classify imagined speech for social interactions. The critical ongoing challenge is translating this work from ECoG to EEG. The semi-invasive BCI system (ECoG) is a direct form of brain activity sensing with minimal noise. In contrast, a noninvasive EEG BCI system may produce significantly worse signal quality. Another challenge is that neurodiversity and the requirement of extensive participant training will hinder the realization of imagining speech technology.

The outlined BCI paradigms offer the potential to build a more intuitive user interface and social interaction for Metaverse use. The ongoing challenge is to develop a reliably detected paradigm in an EEG signal, which requires minimal training, does not unnecessarily distract the user, and can be used by various users. These ongoing challenges indicate the need for further research and exploration into BCI to create a technology used for the Metaverse user.

V. HUMAN DIGITAL TWIN

Sociality is a key factor in the Metaverse [27]. The Metaverse must facilitate a social environment with continuity and a stable population of users. A challenge within the Metaverse is an unstable user base and the discontinuity of interaction when a Metaverse user exits the interfacing device (XR/AR/VR or a smartphone). This section examines the potential solution for this problem by developing a Human Digital Twin(HDT) in the Metaverse using BCI and Digital Twin (DT) technology. DT is a computer-based model that simulates and emulates physical entities, such as objects, humans, or human-related features, with their digital counterparts [113]. While DT has been applied in various areas, such as manufacturing, healthcare, and the Internet of Things (IoT), the concept of HDT remains largely unexplored. A few works [114], [115] attempted to define HDT paradigms. Still, these primarily focus on using conventional IoT sensors to collect human information, similar to DT approaches in healthcare, such as fitness management [116] and disease diagnosis [114]. To our knowledge, no work has considered using human brain signals to construct HDT avatars.

We propose the development of an HDT as the ultimate Metaverse BCI prosthesis (see Fig. 15). The HDT will create a stable population of Metaverse users that maintain continuity between the Metaverse and the real-world. Using real-time data metrics, such as EEG, smartphone, and smartwatch data, the HDT will behave in the Metaverse as an extension of the user in the real-world (when the user is not present in the Metaverse). The HDT will interact with the Metaverse, other Metaverse users, and other HDT. The user can replace the HDT by accessing and entering the Metaverse. In this section, we will outline the wearable technologies required to achieve HDT (Section V-A), the potential applications of HDT within the Metaverse (Section V-B, and the potential challenges for the development of HDT in the Metaverse (Section V-C).

EEG sensor

[Figure 50]

EMG sensor

XR headset

[Figure 51]

HDT

[Figure 52]

[Figure 53]

[Figure 54]

ECG sensor

[Figure 55]

IMU sensor

[Figure 56]

Emotion Cognition Thoughts Body movement

[Figure 57]

GPS

[Figure 58]

[Figure 59]

Stress Calm Workload Fatigue Imagined

Temperature sensor

Pose Muscle

speech

Human body sensing Human digital twin Human digital twin mapping

Digital twin states

- Fig. 14. An outline of the key technologies and information involved in mapping the Human digital twin from human body sensing (with BCI and other supporting technologies). The graph model illustrates the human digital states containing real-time information of the human user.

- A. Key Technologies to Enable the Human Digital within the Metaverse

Fig. 14 outlines the core components of creating the human digital twin. In this survey, we identify several technologies enabling HDT within the Metaverse. Technologies such as BCI, wearable biosensors (heart rate, muscle, IMU, and temperature), smartphones, and AI, can be integrated into the Metaverse to formulate the HDT to replicate life-like representation of the user’s cognition, emotions, thoughts, and movements.

1) Wearable Brain-Computer Interface: One clear advantage of using human brain signals to construct HDT avatars in the Metaverse is the potential reduction of the number of sensors and wearable devices required for users, leading to lower production costs and increased mobility and creativity. The brain signals contain a wealth of information about physical and mental health, such as the ability of EEG to complement electrocardiograms in predicting and diagnosing indicators of pathological perturbations, as demonstrated in brain-heart interaction studies [117]. As a result, the number of electrocardiogram sensors may be reduced or eliminated. Using BCI to control prosthetic devices, as described in [118], opens the door to potential BCI applications such as performing activities of daily living. Other BCI approaches can translate motor imagery and prosthetic limb movements into control of virtual avatars, eliminating the need for external sensors on the body [119]. With the advancement of technology, we can expect future BCI-enabled Metaverse systems to feature lightweight, highly mobile BCI devices for interaction with Metaverse applications.

One of the central challenges in deploying HDT in the Metaverse is ensuring high accuracy in the data measured by integrated VR-BCI headsets, compared with data collected from conventional sensors. To address this challenge, future research may need to investigate the correlations and connections between brain signals and other human biological signals, such as the electrocardiogram (ECG) and electromyogram (EMG) [117]. Another challenge is real-time synchronization and communication between HDT avatars and the Metaverse users, which is essential for maintaining high-quality data within the Metaverse. These challenges are discussed further in Section V-C, respectively.

Once the correlations and relationships between signals among different brain lobes and the human’s biological signals, e.g., ECG and EMG, are recognized, a wide range of applications for the Metaverse can emerge. Multimodal machine learning techniques, which recently advanced in processing large amounts of data from various sources or distributions [120], [121], can be a central component in a range of the Metaverse applications. In [122], the authors proposed an MIBCI control framework that can work with multimodal signals, i.e., EEG and fNIRS. In particular, the proposed multimodal classifier based on a Convolutional Neural Network (CNN) can extract spatial and temporal features of both EEG signals and fNIRS images, thus resulting in higher classification accuracy. In [123], the authors proposed an interactive social platform that integrates eye gaze, EEG signals and peripheral psychophysiological signals of children with Autism Spectrum Disorders (ASD) in a VR setting. The aim of the study in [123] is to understand the underlying factors that affect ASD children through emotion recognition tasks in a VR environment. As a result, potential future works can improve the emotion recognition abilities and eventual social functioning of children with ASD.

Although the works mentioned earlier achieved adequate performance with multimodal data in VR environments, incorporating such approaches into the Metaverse is still a significant research gap. The main difference between conventional VR settings and the Metaverse is that multiple HDT avatars are involved in the Metaverse, yielding more complicated interactive social systems between the HDT avatars. In other words, multiple ‘brains’ of different individuals would be synchronized in the Metaverse. To fully understand the social connections and interactions between such HDT avatars, conventional approaches considering a single deep learning/machine learning classifier for an individual may fail to apply in a social HDT avatars setting [26]. To address these challenges, transfer learning [124] and meta-learning [125] can be applied. The transfer learning and meta-learning techniques share the same interest in utilizing underlying transferable features of the input signals, e.g., EEG, among different individuals. Once the learning models are trained, they can be transferred or directly applied to different HDT avatars with minimal fine-tuning processes. As a result, the Metaverse applications

can only maintain a small number of learning models while guaranteeing high prediction accuracy of different tasks, e.g., emotion recognition and seizure prediction, compared with conventional machine learning approaches. This can reduce the maintenance, deployment, and scalability costs for the Metaverse applications.

- 2) Wearable Sensors Technologies: Wearable and portable

technology has become ubiquitous in the current digital era. BCI technology can unlock a wide array of human sensing capabilities for a life-like HDT and can be further enhanced through additional wearable sensors. There are many platforms for wearable sensors such as smartphones, smartwatches, and smart clothing/jewellery [126]. These platforms utilise multiple types of sensors, such as pulse oximetry, electrodermal activity, global positioning system (GPS), inertial measurement unit (IMU), microphones, cameras, and temperature sensors (thermometers or thermistors). AI personalization and IoT data sharing can enhance the interpretation of these sensor measurements. These multimodal measurements and advanced technology culminate into a sensory information mapping system for emotions, cognitions, thoughts, and body movements.

Smartphones are carried as an essential technology for everyday life. Over 80% of the world’s population is estimated to own a smartphone [127]. Smartphones offer a portable platform for high-performing processing, network connectivity, and various onboard (or attached) sensors [128]. Additionally, smartphones can be the gateway device for users to enter and interact with the Metaverse [129]. For the HDT-based Metaverse interaction, the smartphone can measure physical (steps and calendar/schedule logging), locational (GPS location and IoT geographical data), and social activity (AI personalisation and IoT social data) [130]. This information can be used to formulate the activities and location of the HDT as a representation of the user in the Metaverse.

Smartwatches is an emerging technology that is growing in popularity in daily life. A smartwatch is a wrist-worn computing device that is capable of communicating with other smartphones and computer devices [131]. Smartwatches are often used as a monitor fitness, an extension of a smartphone (phone calls, messaging, payment, and music), and as an assistive technology. Typically, smartwatches (such as Fitbit, Garmin, Apple, or Samsung watches) will carry a range of integrated sensors such as pulse oximetry, ECG, EMG, temperature, and IMU [132]. These sensors can actively measure physical exercise, basic emotional state (meditation and stress), health metrics (cardiovascular), and longitudinal activity (sleep, steps, and location) [133]. Within the Metaverse, the HDT can utilise metrics to accurately represent real-world users’ current bodily/mental state and physical activity.

- B. Human Digital Twin Interaction within the Metaverse

Fig. 15 represents the different interaction scenarios we envision the HDT will engage within the Metaverse. The lifecycle of the HDT begins with the user leaving the Metaverse (Scenario 1: User-HDT synchronization). The HDT will replace the user’s avatar and become of representation of the user when the user is present in the real-world. The HDT will

continuously synchronize with the user state through various wearable technologies outlined in Fig. 14. Within the Metaverse, the HDT can interact with the avatars of other Metaverse (Scenario 2: HDT-Avatar Interaction). The HDT will use technology, such as natural language models, to simulate a life-like interaction between an HDT and a Metaverse user. Alternatively, if two real-world users interact, their HDT will also interact (Scenario 3: HDT-HDT Interaction). This interaction will centre around the transference/sharing of information and ensuring that real-world users can inform each other with up-to-date information, similar to using social media. HDT’s lifecycle ends when the real-world user enters the Metaverse (Scenario 4: User-HDT replacement). The Metaverse user’s avatar would replace the HDT, and all of the HDT’s activities would be synchronized with the Metaverse user.

- 1) User-HDT Synchronization: The HDT addresses the

key problem of discontinuity of a Metaverse user once they exit the Metaverse. In this scenario, when a user exits the Metaverse, the HDT will be activated to replace the user. As outlined in Section V-A, the HDT can leverage several technologies, such as BCI, smartphones, smartwatches, and AI, to create a life-like extension and representation of the user within the Metaverse [115]. Through AI personalization and behaviour recognition, the HDT can interact with other avatars of users and HDTs within the Metaverse. The HDT can represent the current status of the real-world user through health and biometric tracking technology [113], [116], [134]. The HDT can accurately reflect the real-world user’s current status, activities, and interactions within the Metaverse.

- 2) HDT-Avatar Interaction: Social life-likeness is impor-

tant when an HDT interacts with other Metaverse users’ controlled avatars. While the HDT will likely have a unique status/identity within the Metaverse, the HDT must be lifelike to supplement the user base of the Metaverse (similar to non-playable characters in video games) [135]. An HDTto-avatar interaction can provide a naturalistic interface for Metaverse users to be informed on the status, activities, and locations of other users in the real-world [136]. By utilising natural language models, such as ChatGPT, the HDT can engage in authentic social conversations with Metaverse users [137], [138]. This technology can further personalized natural language models by analysing imagined speech [112] and prior social engagements (social media or messaging) [139]. Overall, the HDT will act as a representation of the realworld user that is capable of engaging in meaningful social interactions with other Metaverse users.

- 3) HDT-HDT Interaction: HDT-to-HDT interaction is an-

other distinctive form of interaction within the Metaverse. This type of interaction occurs when two real-world users interact within the real-world at the same location/area. In this situation, the HDTs will communicate in an esoteric manner to share information and update the real-world user on various life events, similar to social media information sharing [140]. This type of interaction shares similarities to the spatial location functions of the Snapchat social platform [141]. Within the Snapchat app, the spatial location of the users is visualised on a map with Bitmoji avatar representation. This spatial map is used to relay information, news, and other

|[Figure 60]<br><br>Human Digital Twin<br><br>Location<br><br>Status<br><br>[Figure 61]<br><br>[Figure 62]<br><br>Emotion<br><br>[Figure 63]<br><br>Scenario 1: User-HDT synchronization|Social interaction<br><br>HDT Avatar<br><br>Self operate Human control<br><br>[Figure 64]<br><br>[Figure 65]<br><br>[Figure 66]<br><br>[Figure 67]<br><br>[Figure 68]<br><br>Scenario 2: HDT-Avatar interaction<br><br>[Figure 69]|[Figure 70]<br><br>[Figure 71]<br><br>Self operate Self operate<br><br>[Figure 72]<br><br>[Figure 73]<br><br>HDT HDT<br><br>Scenario 3: HDT-HDT interaction<br><br>[Figure 74]|[Figure 75]<br><br>[Figure 76]<br><br>Human control<br><br>[Figure 77]<br><br>[Figure 78]<br><br>Scenario 4: User-HDT replacement<br><br>HDT<br><br>Avatar<br><br>[Figure 79]|
|---|---|---|---|
|[Figure 80]<br><br>[Figure 81]<br><br>Wearable EEG & XR<br><br>Smart Phone<br><br>Smart Watch<br><br>Metaverse User<br><br>Continuously Synchronised Digital Twin<br><br>[Figure 82]<br><br>[Figure 83]<br><br>|[Figure 84]<br><br>[Figure 85]<br><br>Smart Phone<br><br>[Figure 86]<br><br>Notification<br><br>[Figure 87]<br><br>[Figure 88]<br><br>[Figure 89]<br><br>[Figure 90]<br><br>Another location<br><br>[Figure 91]|[Figure 92]<br><br>[Figure 93]<br><br>[Figure 94]<br><br>[Figure 95]<br><br>Different people in the same location Their HDTs will interact in the Metaverse|Real<br><br>[Figure 96]<br><br>HDT replaced user avatar|

Metaverse

by

World

- Fig. 15. An illustration of the different scenarios where the Human Digital Twin (HDT) interacts with the Metaverse user, other avatars of Metaverse users, and other HDTs. Each scenario depicts the types of interactions that the HDT can engage in and the supporting technology to enable the interaction.

social events to groups of users occupying the same spatial area [141], [142]. BCI and other wearable technologies can further enrich the behavior of HDT and shared information by measuring the thoughts and well-being of the users. With the growing usage of social media, HDT-to-HDT interaction can be a useful tool for the expedient social transference of information between two people.

4) User-HDT Replacement: The end of the HDT’s lifecycle is when the real-world user re-enters the Metaverse (through smartphone, VR/AR/XR, or other devices). In this scenario, the user’s avatar will replace the HDT and the Metaverse user can return to interacting within the Metaverse. During this scenario, the HDT can provide highlights and narratives akin to social media stories [143]. Creating a narrative can enhance the acceptance of HDT as they are essential to informing and continuing the user’s interaction/connection to the Metaverse [135]. Furthermore, the process of updating the user of the HDT’s activities provides an incentive for other Metaverse users to interact with the HDT. The importance of the avatar’s replacement of the HDT (over the HDT co-existing with the user) is to maintain the HDT’s identity as an extension of the user. If the user co-exists with its own HDT in the Metaverse, it may create a sense of disembodiment or detachment between the HDT and the user [144]. Therefore, the process of a user-controlled avatar replacing the HDT is paramount in facilitating a sense of embodiment and continuity for the user.

- C. Potential Challenges for the Development of the Human Digital Twin in the Metaverse

Another critical challenge in enabling the Metaverse applications with BCI is real-time synchronization and communication between the Metaverse users and their HDTs. In the following, we focus on the communication aspect based on the two main perspectives that are (i) communications between BCI headsets and other infrastructures in the physical world and (ii) communications between human avatars and other

avatars or technologies/virtual services in the Metaverse. The first type of real-time communication is in the physical world, while the latter is in the Metaverse. Real-time communications in the physical world aim to provide robust and reliable connectivity for users with equipped VR/BCI headsets. The transmission of the brain signals over the network systems should meet low latency and error requirements. On the other hand, real-time communications in the Metaverse mainly occur between the users or their avatars with the environment, objects, or other avatars within the Metaverse. As a result, the requirement of real-time communications in the Metaverse is to achieve the continuity of user experience in the Metaverse where there is a parallel presence between the Metaverse and the real-world.

1) Real-time Communications in the Physical World: To achieve reliable and robust real-time communication between BCI headsets and other devices, the infrastructures that support wired/wireless communications play an essential role. In conventional BCI systems, e.g., BCI2000 [145], real-time communications usually refer to scenarios where user brain signals are acquired with wired connections. Thanks to hardware development, wired connections are getting replaced by wireless connections with increasing mobility and reliability. Early research works in wireless BCI utilize Bluetooth for shortrange communication between BCI headset and the processing unit, i.e., a computer [146]–[149]. Although Bluetooth shows its capability in real-time communication, the communication range of Bluetooth is relatively short, i.e., from a few meters up to a range of ten meters. Further efforts to increase the communication range of the wireless BCI systems are reported in [146], [150]–[153]. With significant increases in communication range [146], [150], [151] and joint computingresource allocation [153], wireless BCI shows its potential for enabling real-time communications between BCI headsets and other infrastructures in real-time at large scale.

As mentioned earlier, several works successfully investi-

gated wireless BCI systems’ connectivity and reliability. However, when large-scale systems include heterogeneous wireless devices and medium access schemes, the radio resources should be efficient management [154]. Specifically, Bluetooth and fiber connections may not always be available for BCI users because of coverage problems of such technologies. Such problems require new wireless access methods, radio resource allocation schemes, and broader bandwidth. In the following, we discuss the potential solutions for the problems mentioned above in wireless BCI systems.

To handle multiple requests and transmission of not only brain signals but also VR content over the wireless environment, Time Division Multiple Access (TDMA) can be an efficient solution. With TDMA, the time horizon is divided into multiple time slots, and the BCI users can communicate with the service providers or to each other in reserved time slots [155]. However, using time domain division also brings scheduling and data packet collision problems, thus making the TDMA-based systems hard to scalable. Recent advances in antenna design can enable many BCI users to use Multiple Input Single Output (MISO) and Multiple Input Multiple Output (MIMO) communications. For example, in MISO systems, the service provider can be a multi-antenna transmitter that can serve multiple users or multiple groups of users via Spatial Division Multiple Access (SDMA) [156]. Advanced multiple-access methods can utilize the power domain to transmit VR applications and brain signals. For example, Nonorthogonal Multiple Access (NOMA) [157] and Rate-splitting Multiple Access (RSMA) [158], [159] can be used to enhance data transmission rate, thus increasing the quality of service for the users. Besides advanced multiple access methods, 6G systems can utilize broadband communication techniques such as millimeter wave (mmWave) and Terahertz to enhance data transmission rate further. In such 6G systems, the data transmission rate is envisioned to be ten times faster than that of the 5G systems, making seamless experiences for datademanded applications such as BCI-enabled Metaverse.

The techniques above and methods in wireless communications are promising for BCI-enabled Metaverse applications. However, the underlying theory behind such techniques and methods is based on Shannon’s theory of wireless channel capacity. In other words, the data transmission rate of such methods cannot exceed the Shannon bound. Recent advances in machine learning and wireless communication techniques enable the transmission beyond Shannon bound with semantic compression and semantic communication [160]. Unlike conventional data compression techniques, such as ShannonFano and Huffman coding, semantic compression is designed especially for machine-based communications in which intelligent machines only need specific semantic information to encode/decode the data successfully. On the other hand, semantic communication refers to using language and other symbolic systems to convey meaning between individuals or groups. Semantic communication involves transmitting words or signals and interpreting those words or signals within specific contexts for their intended meaning. Considering the brain signals as information that needs to be transmitted, we need further investigations on the semantic meaning of the

brain signals, e.g., semantic reasoning of EEG signals [161], to design effective semantic communication frameworks for BCI-enabled Metaverse applications.

2) Real-time Communications for the Human Digital Twin in The Metaverse: Unlike real-time communications in the BCI/VR systems, real-time communications in the Metaverse refer to the scenario where users can interact with the Metaverse environment and their digital avatars in real-time. For this, the Metaverse applications should be able to provide highly user-driven embedded facilities such as real-time recommendations and individual support for the users through the virtual environment and digital avatars. For example, digital avatars can give valuable suggestions to users based on the analyzed brain signals. On the other hand, the quality of immersion of users in the Metaverse through VR/XR should also be highly considered. Our discussion about imagined speech communications [162], adaptive VR/XR environment rendering [59], error-related behaviors detection [60], and HDT in the previous section can also be applied in this context. The embodiment of the human digital avatars, i.e., HDT, can be further enhanced by using a digital twin. With a digital twin, the human digital avatars can actively mirror their real-world counterparts through sensory data [163]. In addition, digital twin avatars can simulate or predict potential user anomalous behaviors with reinforcement learning and deep learning in real-time [164], [165]. This functionality can also support other Metaverse-related interactions such as user collaboration, conferencing, presentations, and educational training/demonstrations [166].

VI. CHALLENGES, EMERGING APPLICATIONS, AND FUTURE RESEARCH DIRECTIONS

Despite the success in clinical trials and healthcare applications, there are still debates on using BCI technologies for commercial products. We discuss the open issues regarding the usability of BCI for the Metaverse, ethics, and security. We also review potential research directions of BCI toward a human-centric design for the Metaverse.

A. Current Challenges

1) Hardware Development: The first challenge comes from brain signal extraction for BCI applications. Although the portability and mobility of non-invasive BCI technologies enable commercial products, the brain signals extracted with such non-invasive BCI technologies through either dry or wet sensors usually come with a low signal-to-noise ratio (SNR) compared with the invasive methods. The reason is that the external sensors in non-invasive methods are further away from neuronal sources, plus noise, muscle contraction artifacts, and other tissue-related interference, making signals extracted less effective. On the contrary, invasive methods with the implanted electrode grids under the skull can provide less noisy and more reliable readings. However, the usability of invasive methods still faces critics and ethics concerns.

The hardware and software capabilities remain open challenges toward the two distinct directions of the BCI methods. The invasive BCI research and development may focus on

designing microchips and grids that can be effectively implanted under the skull. The recently funded companies such as NeuralLink 1 and BrainGate 2 are operating toward this vision. However, such companies still develop their products based on clinical trials for patients with paralysis or animals. Apart from this direction, other companies such as Neurable

- 3 and OpenBCI 4 focusing on non-invasive BCI methods aim to develop portable, highly mobile BCI devices for daily use. Moreover, OpenBCI’s Galea headset is a VR-BCI device that allows users to play games and interact with virtual environments through thoughts. We can expect potential Metaverse applications based on VR-BCI technology in the near future. However, the software development must be further developed due to the noisy nature of non-invasive BCI signals. The wearable weight and comfort of such devices should also be considered in design and development.

- 2) Software Development: The software development for

BCI may heavily focus on extracting and monitoring brain signals. Understanding an individual’s brain signals is yet a challenging task, let alone the neurodiversity among the population, age, race, and health. For example, the EEG signals from an individual may almost differ from the others in terms of amplitudes of the signals and the delayed responses to external events. As a result, one software or algorithm does not always fit all. Dealing with the neurodiversity between populations is still an open research issue [26]. Few research works attempted to address this problem, but the existing methods are still limited to a few research participants [153], [167]–[169]. The common approaches of the above studies are additional feature extractions techniques [167], feature representation [168], multimodal machine learning [169], and meta-learning [153]. The main goal of these works is to ensure that the trained machine-learning models can be applied to a new BCI subject without further user-specific training or calibration. Thus, this can significantly enhance the scalability and interoperability of the system. For the large-scale BCIenabled Metaverse systems, besides developing accurate signal processing schemes, resolving the neurodiversity of brain signals should be further investigated.

- 3) Security and Privacy: Recent studies showed that ana-

lyzing resting-state fMRI data [170] and local field potentials [171] of the users with BCI can early reveal diseases such as Parkinson’s and Alzheimer, respectively. In BCI-enabled Metaverse applications, the BCI headsets connected to the Internet also expose the users to potential privacy issues such as hackers, corporations, or government agencies that can track or even manipulate an individual’s mental experience [172]. Specifically, the advertisement-based applications in the Metaverse can gather BCI data from users to tailor their ads that target suitable individuals. Similar to privacy issues of existing social media platforms such as Facebook and Twitter, in which the user data is the product of the social media platforms, the users’ information can be sold to advertisement companies. To address this challenge, a decentralized Metaverse with a

- 1https://neuralink.com/
- 2https://www.braingate.org/
- 3https://neurable.com/about
- 4https://openbci.com/about

transparent consensus mechanism, e.g., blockchain [173], can prevent the data manipulation problems of a firm/company in a centralized Metaverse.

4) Ethics: Thanks to the rapid growth of machine learning and deep learning algorithms, much research has shown that using machine learning and deep learning enables highly accurate predictions and classifications on different BCI settings [26]. Although such algorithms successfully achieved high performance, they are usually tricky or impossible to comprehend [174], [175]. As a result, this introduces an unknown and unaccountable process between the neural pathways within the brain and the external technologies within the Metaverse [176]. For example, the deep learning-aided auto-correction mechanism in imagined speech communication [112] may send unintended messages that the user is possessive about. To void this issue, implementing a BCI-enabled Metaverse system needs to prioritize “how” and “when” to send and/or collect imagined speech of the users. Toward an ethical solution for this, a collaborative project named BrainCom [177], funded by the European Union, is developing speech synthesizers with BCI technologies. Such technologies aim to vocalize the users’ thoughts with ethical concerns accurately.

B. Emerging Applications and Future Research Directions

Although BCI has a long development history, integrating BCI into the Metaverse is still in its infancy. Thus, we expect that the interest of the industry and academy on this topic will expand in the following years. In this section, we discuss the emerging applications of BCI toward the Metaverse. Furthermore, we present several potential research directions.

1) Integrated VR-BCI Devices: Recent development of hardware and software for BCI applications in VR and XR enables the reduction in sizes and costs of the integrated VRBCI devices. There are start-ups that are developing headsets allowing users to control the VR environment by using their EEG signals. For example, Galea5 and Cognixion ONE6 are the headsets developed by OpenBCI and Cognixion, respectively, use from 6 to 8 dry EEG electrodes, in combination with transmission module, e.g., Bluetooth and WiFi, and eye tracking module. Galea is a VR-based headset, while Cognition ONE is an AR-based one, so these devices function very differently. Galea focuses on translating EEG signals into digital commands for VR games and applications. On the other hand, Cognixion ONE uses a combination of EEG signals, eye movement, and facial expressions to control digital devices and interact with augmented environments. Overall, both Galea and Cognixion ONE are innovative and exciting products that are pushing the boundaries of brain-computer interface technology. However, they have different strengths and applications, so their choice will depend on the user’s needs and preferences. For example, Galea is more promising for gaming applications in the BCI-enabled Metaverse, where the users can control their players by thoughts, and Cognition ONE is more appropriate for healthcare Metaverse applications.

- 5https://galea.co/
- 6https://one.cognixion.com/

- 2) Multitasking in the Metaverse: Most of the current ma-

chine learning and deep learning approaches for BCI applications are task-specific, meaning that a machine learning model is associated with an individual, given a specific demand, e.g., emotional detection and seizure prediction [26]. This approach is suitable for the classifiers to be deployed at the user site, e.g., a pre-installed software in the headset. However, when it comes to multitasking applications, e.g., combined imagined speech and emotional recognition, the task-specific classifier/software may fail or downgrade the performance. For example, in some Metaverse applications such as virtual fighting, fitness, and dance gaming, the multisensory data from EEG, facial expression, and emotional states can be jointly exploited to enable secure imagined conversations between groups of users and reduce potential motion sickness induced by fast-moving scenes. To fully exploit the multisensory data in such scenarios, multimodal machine learning approaches, which we described in Section V-A, can be a suitable approach. With multimodal machine learning, we can expect only one machine learning model to assist the user in various tasks, from emotional recognition to imagined speech communication, without requiring changes or upgrades in software and hardware.

- 3) Potential Research Directions: Regarding the technical

challenges and usability of the BCI-enabled Metaverse concept, different aspects of this new concept must be further investigated and studied. The following discusses the potential research directions for the BCI-enabled Metaverse systems. Machine Learning for processing heterogeneous datasets: In recent years, the notable trend in BCI is applying advanced machine learning techniques for analyzing brain signals. Similarly, machine learning techniques will be a significant component in the BCI-enabled Metaverse system. Unlike conventional problems in BCI research, which extensively focus on designing highly accurate classifiers for specific tasks [26], the integration of BCI into Metaverse brings new challenges. One of the most notable is addressing the complexity of the system processing multiple sources of human brain signals. As shown in early findings [153], [167], [169], the participation of multiple users in a task yields a degraded performance for the classifier due to the neurodiversity among the users. The neurodiversity suggests that the brain signals such as EEG or fMRI are highly individual and different among users based on gender, age, and other factors [178]. As a result, a classifier trained with one dataset, e.g., EEG, of a person does not work well with one another.

Conventional approaches with machine learning require different classifiers for different people, thus resulting in inefficient computing and poor usability. To address this problem, further analysis on the brain signals [167], [169] or advanced machine learning algorithm, e.g., meta-learning [153], can be applied. As a result, only one classifier can be used across the users without degrading the performance. Although a few early works address the neurodiversity problem, the large number of data generated from human activities, including human brain signals, poses new challenges. The virtual environments in the Metaverse also raise technical concerns about combining virtual environments’ constraints, e.g., motion sickness and delay,

into creating effective machine learning models. The multiple modalities of the data sources make it hard to understand and analyze the informative features. The multimodal machine learning techniques we discussed in the previous sections can be a potential solution. Apart from multimodal approaches, the success of attention-based machine learning models, e.g., Transformer [179], in understanding complex problems, ranging from visual scenes to language understanding, make it a potential candidate for tacking the multiple modalities of the evolved data in the Metaverse. The attention-based mechanisms with designed attention vectors make the machine learning models can pay attention to the most valuable parts of the data, thus making the data extraction process more effective. In addition, the applications across the virtual worlds in the Metaverse can share similar features, e.g., user behaviors in applications such as e-commerce. Therefore, we can better exploit the valuable features and optimize the machine learning models by learning transferable features of the virtual worlds. In such scenarios, transfer learning techniques are commonly used [124].

Human Digital Twin for Maintaining Continuity in the Metaverse: As discussed in Section V, HDT will play a key role in helping us better understand the virtual embodiment of the human body in the Metaverse. In future Metaverse applications, HDT should provide intelligent interfaces for digital avatars by using the brain signals and leveraging 3D visual effects of the human body, e.g., facial expression and body pose, to construct individual avatars. As a result, the continuity of the Metaverse can be maintained in which the HDT can auto-generate or self-operate in the virtual environment with less control from humans. The human users can join the Metaverse and replace the HDT by their avatars when wearing VR/XR headsets (see Fig. 15). To this end, the brain signals can be mixed with other human data such as body motion with physical engines [8], [9], and facial expression [10] to construct the most realistic and personalized HDT in the Metaverse. This can be a new research area that lies at the intersection of neuroscience, e.g., using human biological data, and 3D avatar construction, e.g., using facial expression, limb movement, and kinematics study of the human body.

VII. CONCLUSION

This survey provides an in-depth overview of non-invasive BCI technologies and their potential applications in the Metaverse. With BCI-enabled applications, the Metaverse is expected to be highly personalized and customized to individual needs. Furthermore, the users can interact with the virtual environments with a limited number of sensors, such as kinematics sensors and handheld devices. We also discussed a novel concept of HDT, where the twin representations of the users in the virtual worlds can be developed using a digital twin. Lastly, we discussed the open issues, including security, privacy, hardware and software capability. The potential research directions were also covered. Alternatively, the survey outlines the initial steps for the potential research area evolved at the intersection of BCI and the Metaverse technologies, e.g., VR/XR, 3D environment construction, and real-time communication and synchronization.

REFERENCES

- [1] M. Xu, W. C. Ng, W. Y. B. Lim, J. Kang, Z. Xiong, D. Niyato, Q. Yang, X. Shen, and C. Miao, “A full dive into realizing the edgeenabled metaverse: Visions, enabling technologies, and challenges,” IEEE Communications Surveys & Tutorials, vol. 25, no. 1, pp. 656– 700, 2023.
- [2] X. Yu, D. Owens, and D. Khazanchi, “Building socioemotional environments in metaverses for virtual teams in healthcare: A conceptual exploration,” in International Conference on Health Information Science. Springer, Apr. 2012, pp. 4–12.
- [3] H. Jeong, Y. Yi, and D. Kim, “An innovative e-commerce platform incorporating metaverse to live commerce,” International Journal of Innovative Computing, Information and Control, vol. 18, no. 1, pp. 221–229, Feb. 2022.
- [4] W. C. Ng, W. Y. B. Lim, J. S. Ng, S. Sawadsitang, Z. Xiong, and D. Niyato, “Optimal stochastic coded computation offloading in unmanned aerial vehicles network,” in 2021 IEEE Global Communications Conference (GLOBECOM). IEEE, Dec. 2021, pp. 1–6.
- [5] L.-H. Lee, T. Braud, P. Zhou, L. Wang, D. Xu, Z. Lin, A. Kumar, C. Bermejo, and P. Hui, “All one needs to know about metaverse: A complete survey on technological singularity, virtual ecosystem, and research agenda,” arXiv preprint arXiv:2110.05352, Oct. 2021.
- [6] M. Morrissey, “Human-centric design,” Mechanical Engineering, vol. 120, no. 07, pp. 60–62, Jul. 1998.
- [7] Y. Wang, Z. Su, N. Zhang, R. Xing, D. Liu, T. H. Luan, and X. Shen, “A survey on metaverse: Fundamentals, security, and privacy,” IEEE Communications Surveys & Tutorials, vol. 25, no. 1, pp. 319–352, 2023.
- [8] A. Winkler, J. Won, and Y. Ye, “Questsim: Human motion tracking from sparse sensors with simulated avatars,” in SIGGRAPH Asia 2022 Conference Papers, Nov. 2022, pp. 1–8.
- [9] X. Yi, Y. Zhou, M. Habermann, S. Shimada, V. Golyanik, C. Theobalt, and F. Xu, “Physical inertial poser (pip): Physics-aware real-time human motion tracking from sparse inertial sensors,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022, pp. 13167–13178.
- [10] A. Raj, M. Zollhofer, T. Simon, J. Saragih, S. Saito, J. Hays, and S. Lombardi, “Pixel-aligned volumetric avatars,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2021, pp. 11733–11742.
- [11] G. Tieri, G. Morone, S. Paolucci, and M. Iosa, “Virtual reality in cognitive and motor rehabilitation: Facts, fiction, and fallacies,” Expert Review of Medical Devices, vol. 15, no. 2, pp. 107–117, Feb. 2018.
- [12] L. F. Haas, “Hans berger (1873-1941), richard caton (1842-1926), and electroencephalography,” Journal of Neurology, Neurosurgery & Psychiatry, vol. 74, no. 1, pp. 9–9, Jan. 2003.
- [13] M. Ienca and P. Haselager, “Hacking the brain: brain-computer interfacing technology and the ethics of neurosecurity,” Ethics and Information Technology, vol. 18, pp. 117–129, Jun. 2016.
- [14] T. O. Zander and C. Kothe, “Towards passive brain-computer interfaces: Applying brain-computer interface technology to humanmachine systems in general,” Journal of Neural Engineering, vol. 8, no. 2, p. 025005, Mar. 2011.
- [15] H. Y. Zhu, H.-T. Chen, and C.-T. Lin, “The effects of a stressful physical environment during virtual reality height exposure,” in 2021 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW), Mar. 2021, pp. 468–469.
- [16] H. Y. Zhu, “The effects of physiological stress on brain-computer interface systems,” Ph.D. dissertation, University of Technology Sydney, 2022.
- [17] A. R. John, A. K. Singh, T.-T. N. Do, A. Eidels, E. Nalivaiko, A. M. Gavgani, S. Brown, M. Bennett, S. Lal, and A. M. Simpson, “Unraveling the physiological correlates of mental workload variations in tracking and collision prediction tasks,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 770–781, Mar. 2022.
- [18] T.-T. N. Do, C.-T. Lin, and K. Gramann, “Human brain dynamics in active spatial navigation,” Scientific Reports, vol. 11, no. 1, p. 13036, Jun. 2021.
- [19] S. Aldini, A. Akella, A. K. Singh, Y.-K. Wang, M. Carmichael, D. Liu, and C.-T. Lin, “Effect of mechanical resistance on cognitive conflict in physical human-robot collaboration,” in 2019 International Conference on Robotics and Automation (ICRA). IEEE, 2019, pp. 6137–6143.
- [20] A. K. Singh, S. Aldini, D. Leong, Y.-K. Wang, M. G. Carmichael, D. Liu, and C.-T. Lin, “Prediction error negativity in physical human-

- robot collaboration,” in 2020 8th International Winter Conference on Brain-Computer Interface (BCI). IEEE, 2020, pp. 1–6.
- [21] C.-T. Lin, C.-Y. Chiu, A. K. Singh, J.-T. King, L.-W. Ko, Y.-C. Lu, and Y.-K. Wang, “A wireless multifunctional ssvep-based brain– computer interface assistive system,” IEEE Transactions on Cognitive and Developmental Systems, vol. 11, no. 3, pp. 375–383, 2018.
- [22] K. J. Panoulas, L. J. Hadjileontiadis, and S. M. Panas, “Brain-computer interface (bci): Types, processing perspectives and applications,” Multimedia Services in Intelligent Environments: Integrated Systems, pp. 299–321, Jan. 2010.
- [23] E. Tidoni, P. Gergondet, A. Kheddar, and S. M. Aglioti, “Audio-visual feedback improves the bci performance in the navigational control of a humanoid robot,” Frontiers in Neurorobotics, vol. 8, p. 20, Jun. 2014.
- [24] N. Cheng, K. S. Phua, H. S. Lai, P. K. Tam, K. Y. Tang, K. K. Cheng, R. C.-H. Yeow, K. K. Ang, C. Guan, and J. H. Lim, “Braincomputer interface-based soft robotic glove rehabilitation for stroke,” IEEE Transactions on Biomedical Engineering, vol. 67, no. 12, pp. 3339–3351, 2020.
- [25] H. Wu, S. Liang, W. Hang, X. Liu, Q. Wang, K.-S. Choi, and J. Qin, “Evaluation of motor training performance in 3d virtual environment via combining brain-computer interface and haptic feedback,” Procedia Computer Science, vol. 107, pp. 256–261, 2017.
- [26] X. Zhang, L. Yao, X. Wang, J. Monaghan, D. Mcalpine, and Y. Zhang, “A survey on deep learning-based non-invasive brain signals: recent advances and new frontiers,” Journal of Neural Engineering, vol. 18, no. 3, p. 031002, Mar. 2021.
- [27] H. Ning, H. Wang, Y. Lin, W. Wang, S. Dhelim, F. Farha, J. Ding, and M. Daneshmand, “A survey on the metaverse: The state-of-the-art, technologies, applications, and challenges,” IEEE Internet of Things Journal, May 2023.
- [28] T. Huynh-The, Q.-V. Pham, X.-Q. Pham, T. T. Nguyen, Z. Han, and D.-S. Kim, “Artificial intelligence for the metaverse: A survey,” Engineering Applications of Artificial Intelligence, vol. 117, p. 105581, Jan. 2023.
- [29] S. L. Bernal, M. Q. P´erez, E. T. M. Beltr´an, G. M. P´erez, and A. H. Celdr´an, “When brain-computer interfaces meet the metaverse: Landscape, demonstrator, trends, challenges, and concerns,” arXiv preprint arXiv:2212.03169, Dec. 2022.
- [30] K. J. Nevelsteen, “Virtual world, defined from a technological perspective and applied to video games, mixed reality, and the metaverse,” Computer Animation and Virtual Worlds, vol. 29, no. 1, p. e1752, Jan. 2018.
- [31] C.-M. Wu, C.-W. Hsu, T.-K. Lee, and S. Smith, “A virtual reality keyboard with realistic haptic feedback in a fully immersive virtual environment,” Virtual Reality, vol. 21, pp. 19–29, Mar. 2017.
- [32] Decentraland, “Decentraland land—what drives long term value.” Accessed: Aug. 15, 2023. [Online]. Available: https://decentral.games/ blog/decentraland-land-what-drives-long-term-value
- [33] NVIDIA, “Nvidia omniverse,” Accessed: Aug. 15, 2023. [Online]. Available: https://www.nvidia.com/en-au/omniverse/
- [34] Microsoft, “Microsoft mesh.” Accessed: Aug. 15, 2023. [Online]. Available: https://www.microsoft.com/en-us/mesh
- [35] L. Jiaxing, “Baidu launches xirang metaverse environment.” Accessed: Aug. 15, 2023. [Online]. Available: https://kr-asia.com/ baidu-launches-xirang-metaverse-environment
- [36] M. Bernard, “The amazing possibilities of healthcare in the metaverse.” Accessed: Aug. 15, 2023. [Online]. Available: https://www.forbes.com/sites/bernardmarr/2022/02/ 23/the-amazing-possibilities-of-healthcare-in-the-metaverse/?sh= 4191889f9e5c
- [37] B. Blankertz, K.-R. Muller, D. J. Krusienski, G. Schalk, J. R. Wolpaw, A. Schlogl, G. Pfurtscheller, J. R. Millan, M. Schroder, and N. Birbaumer, “The bci competition iii: Validating alternative approaches to actual bci problems,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 14, no. 2, pp. 153–159, Jun. 2006.
- [38] L. G. Ungerleider and J. V. Haxby, “‘what’and ‘where’ in the human brain,” Current Opinion in Neurobiology, vol. 4, no. 2, pp. 157–165, Jan. 1994.
- [39] S. Herculano-Houzel, “The remarkable, yet not extraordinary, human brain as a scaled-up primate brain and its associated cost,” Proceedings of the National Academy of Sciences, vol. 109, no. supplement 1, pp. 10661–10668, Jun. 2012.

- [40] S. Waldert, “Invasive vs. non-invasive neuronal signals for brainmachine interfaces: will one prevail?” Frontiers in Neuroscience, vol. 10, p. 295, Jun. 2016.
- [41] T. Anitha, N. Shanthi, R. Sathiyasheelan, G. Emayavaramban, and T. Rajendran, “Brain-computer interface for persons with motor

- disabilities-a review,” The Open Biomedical Engineering Journal, vol. 13, no. 1, Dec. 2019.
- [42] B. Fiani, T. Reardon, B. Ayres, D. Cline, S. R. Sitto, T. K. Reardon, B. R. Ayres, and D. D. Cline, “An examination of prospective uses and future directions of neuralink: The brain-machine interface,” Cureus, vol. 13, no. 3, Mar. 2021.
- [43] J. R. Wolpaw, N. Birbaumer, W. J. Heetderks, D. J. McFarland, P. H. Peckham, G. Schalk, E. Donchin, L. A. Quatrano, C. J. Robinson, and T. M. Vaughan, “Brain-computer interface technology: A review of the first international meeting,” IEEE Transactions on Rehabilitation Engineering, vol. 8, no. 2, pp. 164–173, Jun. 2000.
- [44] B. Kerous, F. Skola, and F. Liarokapis, “Eeg-based bci and video games: A progress report,” Virtual Reality, vol. 22, pp. 119–135, Jun. 2018.
- [45] T. Wilcox and M. Biondi, “fnirs in the developmental sciences,” Wiley Interdisciplinary Reviews: Cognitive Science, vol. 6, no. 3, pp. 263– 283, May 2015.
- [46] J. Uchitel, E. E. Vidal-Rosas, R. J. Cooper, and H. Zhao, “Wearable, integrated eeg–fnirs technologies: A review,” Sensors, vol. 21, no. 18, p. 6106, Sep. 2021.
- [47] J. Minguillon, M. A. Lopez-Gordo, and F. Pelayo, “Trends in eeg-bci for daily-life: Requirements for artifact removal,” Biomedical Signal Processing and Control, vol. 31, pp. 407–418, Jan. 2017.
- [48] D. Marshall, D. Coyle, S. Wilson, and M. Callaghan, “Games, gameplay, and bci: The state of the art,” IEEE Transactions on Computational Intelligence and AI in Games, vol. 5, no. 2, pp. 82–99, May 2013.
- [49] M. A. Lopez-Gordo, D. Sanchez-Morillo, and F. P. Valle, “Dry eeg electrodes,” Sensors, vol. 14, no. 7, pp. 12847–12870, Jul. 2014.
- [50] W. D. Hairston, K. W. Whitaker, A. J. Ries, J. M. Vettel, J. C. Bradford, S. E. Kerick, and K. McDowell, “Usability of four commerciallyoriented eeg systems,” Journal of Neural Engineering, vol. 11, no. 4, p. 046018, Jul. 2014.
- [51] G. Cay, “Design of a wearable fnirs neuroimaging device with an internet-of-things architecture,” Ph.D. dissertation, University of Rhode Island, 2017.
- [52] E. P. Torres, E. A. Torres, M. Hern´andez-Alvarez,´ and S. G. Yoo, “Eegbased bci emotion recognition: A survey,” Sensors, vol. 20, no. 18, p. 5083, Sep. 2020.
- [53] S. K. Mudgal, S. K. Sharma, J. Chaturvedi, and A. Sharma, “Brain computer interface advancement in neurosciences: Applications and issues,” Interdisciplinary Neurosurgery, vol. 20, p. 100694, Jun. 2020.
- [54] S. Saha, K. A. Mamun, K. Ahmed, R. Mostafa, G. R. Naik, S. Darvishi, A. H. Khandoker, and M. Baumert, “Progress in brain computer interface: Challenges and opportunities,” Frontiers in Systems Neuroscience, vol. 15, p. 578875, 2021.
- [55] H. Y. Zhu, H.-T. Chen, and C.-T. Lin, “The effects of virtual and physical elevation on physiological stress during virtual reality height exposure,” IEEE Transactions on Visualization and Computer Graphics, vol. 29, no. 4, pp. 1937–1950, Apr. 2023.
- [56] C. A. T. Cortes, H.-T. Chen, D. L. Sturnieks, J. Garcia, S. R. Lord, and C.-T. Lin, “Evaluating balance recovery techniques for users wearing head-mounted display in vr,” IEEE Transactions on Visualization and Computer Graphics, vol. 27, no. 1, pp. 204–215, Jan. 2021.
- [57] A. K. Singh, K. Gramann, H.-T. Chen, and C.-T. Lin, “The impact of hand movement velocity on cognitive conflict processing in a 3d object selection task in virtual reality,” NeuroImage, vol. 226, p. 117578, Feb. 2021.
- [58] G. Bernal, N. Hidalgo, C. Russomanno, and P. Maes, “Galea: A physiological sensing system for behavioral research in virtual environments,” in 2022 IEEE Conference on Virtual Reality and 3D User Interfaces (VR), Mar. 2022, pp. 66–76.
- [59] O.-H. Cho and W.-H. Lee, “Bci sensor based environment changing system for immersion of 3d game,” International Journal of Distributed Sensor Networks, vol. 10, no. 5, p. 620391, May 2014.
- [60] P. Arico, G. Borghini, G. Di Flumeri, N. Sciaraffa, A. Colosimo, and F. Babiloni, “Passive bci in operational environments: insights, recent advances, and future trends,” IEEE Transactions on Biomedical Engineering, vol. 64, no. 7, pp. 1431–1436, Apr. 2017.
- [61] J. A. Russell, “A circumplex model of affect.” Journal of Personality and Social Psychology, vol. 39, no. 6, p. 1161, Dec. 1980.
- [62] P. L. Broadhurst, “Emotionality and the yerkes-dodson law.” Journal of Experimental Psychology, vol. 54, no. 5, p. 345, Nov. 1957.
- [63] A. Al-Nafjan, M. Hosny, Y. Al-Ohali, and A. Al-Wabil, “Review and classification of emotion recognition based on eeg brain-computer interface system research: A systematic review,” Applied Sciences, vol. 7, no. 12, p. 1239, Dec. 2017.

- [64] D. P.-O. Bos, “Eeg-based emotion recognition the influence of visual and auditory stimuli,” Ph.D. dissertation, University of Twente, 2007.
- [65] R. Jenke, A. Peer, and M. Buss, “Feature extraction and selection for emotion recognition from eeg,” IEEE Transactions on Affective Computing, vol. 5, no. 3, pp. 327–339, Jul. 2014.
- [66] G. Stenberg, “Personality and the eeg: Arousal and emotional arousability,” Personality and Individual Differences, vol. 13, no. 10, pp. 1097–1113, Oct. 1992.
- [67] G. Prete, V. Tommasi, and L. Tommasi, “Right news, good news! the valence hypothesis and hemispheric asymmetries in auditory imagery,” Language, Cognition and Neuroscience, vol. 35, no. 4, pp. 409–419, May 2020.
- [68] G. Gainotti, “Emotions and the right hemisphere: Can new data clarify old models?” The Neuroscientist, vol. 25, no. 3, pp. 258–270, Jul. 2018.
- [69] M. Mneimne, A. S. Powers, K. E. Walton, D. S. Kosson, S. Fonda, and J. Simonetti, “Emotional valence and arousal effects on memory and hemispheric asymmetries,” Brain and Cognition, vol. 74, no. 1, pp. 10–17, Oct. 2010.
- [70] J. Atkinson and D. Campos, “Improving bci-based emotion recognition by combining eeg feature selection and kernel classifiers,” Expert Systems with Applications, vol. 47, pp. 35–41, Apr. 2016.
- [71] Z. He, Z. Li, F. Yang, L. Wang, J. Li, C. Zhou, and J. Pan, “Advances in multimodal emotion recognition based on brain–computer interfaces,” Brain Sciences, vol. 10, no. 10, p. 687, Sep. 2020.
- [72] W. K. So, S. W. Wong, J. N. Mak, and R. H. Chan, “An evaluation of mental workload with frontal eeg,” PloS One, vol. 12, no. 4, p. e0174949, Apr. 2017.
- [73] C. Berka, D. J. Levendowski, M. N. Lumicao, A. Yau, G. Davis, V. T. Zivkovic, R. E. Olmstead, P. D. Tremoulet, and P. L. Craven, “Eeg correlates of task engagement and mental workload in vigilance, learning, and memory tasks,” Aviation, Space, and Environmental Medicine, vol. 78, no. 5, pp. B231–B244, May 2007.
- [74] B. T. Jap, S. Lal, P. Fischer, and E. Bekiaris, “Using eeg spectral components to assess algorithms for detecting fatigue,” Expert Systems with Applications, vol. 36, no. 2, pp. 2352–2359, Mar. 2009.
- [75] C.-T. Lin, Y. Tian, Y.-K. Wang, T.-T. N. Do, Y.-L. Chang, J.-T. King, K.-C. Huang, and L.-D. Liao, “Effects of multisensory distractor interference on attentional driving,” IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 8, pp. 10395–10403, Mar. 2022.
- [76] W. Klimesch, M. Doppelmayr, H. Russegger, T. Pachinger, and J. Schwaiger, “Induced alpha band power changes in the human EEG and attention,” Neuroscience Letters, vol. 244, no. 2, pp. 73–76, Mar. 1998.
- [77] S. B. i Badia, L. V. Quintero, M. S. Cameirao, A. Chirico, S. Triberti, P. Cipresso, and A. Gaggioli, “Toward emotionally adaptive virtual reality for mental health applications,” IEEE Journal of Biomedical and Health Informatics, vol. 23, no. 5, pp. 1877–1887, Oct. 2018.
- [78] M. P. Wo´zniak, P. Sikorski, M. Wr´obel-Lachowska, N. Bartłomiejczyk, J. Dominiak, K. Grudzie´n, and A. Romanowski, “Enhancing in-game immersion using bci-controlled mechanics,” in Proceedings of the 27th ACM Symposium on Virtual Reality Software and Technology, Dec. 2021, pp. 1–6.
- [79] HP, “Hp reverb g2 omnicept edition,” Accessed: Aug. 15, 2023. [Online]. Available: https://www.hp.com/us-en/vr/ reverb-g2-vr-headset-omnicept-edition.html
- [80] C. A. Tirado Cortes, H.-T. Chen, and C.-T. Lin, “Analysis of vr sickness and gait parameters during non-isometric virtual walking with large translational gain,” in Proceedings of the 17th International Conference on Virtual-Reality Continuum and its Applications in Industry, Nov. 2019, pp. 1–10.
- [81] C. A. Tirado Cortes, “Providing safer virtual reality experiences with the help of brain-computer interfaces,” Ph.D. dissertation, University of Technology Sydney, 2020.
- [82] Y.-C. Chen, J.-R. Duann, S.-W. Chuang, C.-L. Lin, L.-W. Ko, T.-P. Jung, and C.-T. Lin, “Spatial and temporal EEG dynamics of motion sickness,” NeuroImage, vol. 49, no. 3, pp. 2862–2870, Feb. 2010.
- [83] C. A. T. Cortes, C.-T. Lin, T.-T. N. Do, and H.-T. Chen, “An eegbased experiment on vr sickness and postural instability while walking in virtual environments,” in 2023 IEEE Conference Virtual Reality and 3D User Interfaces (VR), Mar. 2023, pp. 94–104.
- [84] A. R. Sipp, J. T. Gwin, S. Makeig, and D. P. Ferris, “Loss of balance during balance beam walking elicits a multifocal theta band electrocortical response,” Journal of Neurophysiology, vol. 110, no. 9, pp. 2050–2060, Nov. 2013.
- [85] V. F. Annese, M. Crepaldi, D. Demarchi, and D. De Venuto, “A digital processor architecture for combined eeg/emg falling risk prediction,” in

- 2016 Design, Automation & Test in Europe Conference & Exhibition (DATE), Mar. 2016, pp. 714–719.
- [86] N. Yeung, M. M. Botvinick, and J. D. Cohen, “The neural basis of error detection: Conflict monitoring and the error-related negativity.” Psychological Review, vol. 111, no. 4, pp. 931–959, Oct. 2004.
- [87] A. K. Singh, H.-T. Chen, Y.-F. Cheng, J.-T. King, L.-W. Ko, K. Gramann, and C.-T. Lin, “Visual appearance modulates prediction error in virtual reality,” IEEE Access, vol. 6, pp. 24617–24624, May 2018.
- [88] H. Si-Mohammed, C. Lopes-Dias, M. Duarte, F. Argelaguet, C. Jeunet, G. Casiez, G. R. M¨uller-Putz, A. L´ecuyer, and R. Scherer, “Detecting system errors in virtual reality using eeg through error-related potentials,” in 2020 IEEE Conference on Virtual Reality and 3D User Interfaces (VR), Mar. 2020, pp. 653–661.
- [89] T. Hinterberger, A. K¨ubler, J. Kaiser, N. Neumann, and N. Birbaumer, “A brain/computer interface (BCI) for the locked-in: comparison of different EEG classifications for the thought translation device,” Clinical Neurophysiology, vol. 114, no. 3, pp. 416–425, Mar. 2003.
- [90] F. Balagtas-Fernandez, J. Forrai, and H. Hussmann, “Evaluation of user interface design and input methods for applications on mobile touch screen devices,” in Human-Computer Interaction – INTERACT 2009. Springer Berlin Heidelberg, Aug. 2009, pp. 243–246.
- [91] C. Nehaniv, K. Dautenhahn, J. Kubacki, M. Haegele, C. Parlitz, and R. Alami, “A methodological approach relating the classification of gesture to identification of human intent in the context of human-robot interaction,” in ROMAN 2005. IEEE International Workshop on Robot and Human Interactive Communication, 2005. IEEE, Aug. 2005.
- [92] S.-J. Blakemore and J. Decety, “From the perception of action to the understanding of intention,” Nature Reviews Neuroscience, vol. 2, no. 8, pp. 561–567, Aug. 2001.
- [93] T. W. Picton, “The p300 wave of the human event-related potential,” Journal of Clinical Neurophysiology, vol. 9, no. 4, pp. 456–479, Oct. 1992.
- [94] D. Krusienski, E. Sellers, D. McFarland, T. Vaughan, and J. Wolpaw, “Toward enhanced p300 speller performance,” Journal of Neuroscience Methods, vol. 167, no. 1, pp. 15–21, Jan. 2008.
- [95] M. Lotze and U. Halsband, “Motor imagery,” Journal of PhysiologyParis, vol. 99, no. 4-6, pp. 386–395, Jun. 2006.
- [96] D. J. Crammond, “Motor imagery: never in your wildest dream,” Trends in Neurosciences, vol. 20, no. 2, pp. 54–57, Feb. 1997.
- [97] J. Decety, “The neurophysiological basis of motor imagery,” Behavioural Brain Research, vol. 77, no. 1-2, pp. 45–52, May 1996.
- [98] Z. Wu, Y. Lai, Y. Xia, D. Wu, and D. Yao, “Stimulator selection in SSVEP-based BCI,” Medical Engineering & Physics, vol. 30, no. 8, pp. 1079–1088, Oct. 2008.
- [99] G. R. Muller-Putz and G. Pfurtscheller, “Control of an electrical prosthesis with an ssvep-based bci,” IEEE Transactions on Biomedical Engineering, vol. 55, no. 1, pp. 361–364, Jan. 2008.
- [100] E. Tidoni, P. Gergondet, G. Fusco, A. Kheddar, and S. M. Aglioti, “The role of audio-visual feedback in a thought-based control of a humanoid robot: A BCI study in healthy and spinal cord injured people,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 6, pp. 772–781, Jun. 2017.
- [101] D. Zhang, L. Yao, K. Chen, S. Wang, X. Chang, and Y. Liu, “Making sense of spatio-temporal preserving representations for EEG-based human intention recognition,” IEEE Transactions on Cybernetics, vol. 50, no. 7, pp. 3033–3044, Jul. 2020.
- [102] L. Yue, H. Shen, S. Wang, R. Boots, G. Long, W. Chen, and X. Zhao, “Exploring BCI control in smart environments,” ACM Transactions on Knowledge Discovery from Data, vol. 15, no. 5, pp. 1–20, Oct. 2021.
- [103] C. Neuper and G. Pfurtscheller, “Neurofeedback training for BCI control,” in Brain-Computer Interfaces. Springer Berlin Heidelberg, 2009, pp. 65–78.
- [104] D. Maloney, G. Freeman, and D. Y. Wohn, “Talking without a voice,” Proceedings of the ACM on Human-Computer Interaction, vol. 4, no. CSCW2, pp. 1–25, Oct. 2020.
- [105] B. Obermaier, G. Muller, and G. Pfurtscheller, ““virtual keyboard” controlled by spontaneous EEG activity,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 11, no. 4, pp. 422–426, Dec. 2003.
- [106] H.-J. Hwang, J.-H. Lim, Y.-J. Jung, H. Choi, S. W. Lee, and C.-H. Im, “Development of an SSVEP-based BCI spelling system adopting a QWERTY-style LED keyboard,” Journal of Neuroscience Methods, vol. 208, no. 1, pp. 59–65, Jun. 2012.
- [107] W. Wang, A. D. Degenhart, G. P. Sudre, D. A. Pomerleau, and E. C. Tyler-Kabara, “Decoding semantic information from human electrocorticographic (ECoG) signals,” in 2011 Annual International

- Conference of the IEEE Engineering in Medicine and Biology Society. IEEE, Aug. 2011.
- [108] Q. Rabbani, G. Milsap, and N. E. Crone, “The potential for a speech brain–computer interface using chronic electrocorticography,” Neurotherapeutics, vol. 16, no. 1, pp. 144–165, Jan. 2019.
- [109] F. R. Willett, D. T. Avansino, L. R. Hochberg, J. M. Henderson, and K. V. Shenoy, “High-performance brain-to-text communication via handwriting,” Nature, vol. 593, no. 7858, pp. 249–254, May 2021.
- [110] C. Herff, D. Heger, A. de Pesters, D. Telaar, P. Brunner, G. Schalk, and T. Schultz, “Brain-to-text decoding spoken phrases from phone representations in the brain,” Frontiers in Neuroscience, vol. 9, Jun. 2015.
- [111] C. Herff, A. de Pesters, D. Heger, P. Brunner, G. Schalk, and T. Schultz, “Towards continuous speech recognition for BCI,” in SpringerBriefs in Electrical and Computer Engineering. Springer International Publishing, 2017, pp. 21–29.
- [112] S.-H. Lee, Y.-E. Lee, and S.-W. Lee, “Toward imagined speech based smart communication system: Potential applications on metaverse conditions,” in 2022 10th International Winter Conference on BrainComputer Interface (BCI). IEEE, Feb. 2022, pp. 1–4.
- [113] B. R. Barricelli, E. Casiraghi, and D. Fogli, “A survey on digital twin: Definitions, characteristics, applications, and design implications,” IEEE Access, vol. 7, pp. 167653–167671, Nov. 2019.
- [114] B. R. Barricelli, E. Casiraghi, J. Gliozzo, A. Petrini, and S. Valtolina, “Human digital twin for fitness management,” IEEE Access, vol. 8, pp. 26637–26664, Feb. 2020.
- [115] W. Shengli, “Is human digital twin possible?” Computer Methods and Programs in Biomedicine Update, vol. 1, p. 100014, Jan. 2021.
- [116] R. Martinez-Velazquez, R. Gamez, and A. El Saddik, “Cardio twin: A digital twin of the human heart running on the edge,” in 2019 IEEE International Symposium on Medical Measurements and Applications (MeMeA). IEEE, Jun. 2019, pp. 1–6.
- [117] A. Lin, K. K. Liu, R. P. Bartsch, and P. C. Ivanov, “Delay-correlation landscape reveals characteristic time delays of brain rhythms and heart interactions,” Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, vol. 374, no. 2067, p. 20150182, May 2016.
- [118] K. D. Katyal, M. S. Johannes, S. Kellis, T. Aflalo, C. Klaes, T. G. McGee, M. P. Para, Y. Shi, B. Lee, and K. Pejsa, “A collaborative bci approach to autonomous control of a prosthetic limb system,” in 2014 IEEE International Conference on Systems, Man, and Cybernetics (SMC). IEEE, 2014, pp. 1479–1482.
- [119] P. T. Wang, C. E. King, L. A. Chui, A. H. Do, and Z. Nenadic, “Selfpaced brain-computer interface control of ambulation in a virtual reality environment,” Journal of Neural Engineering, vol. 9, no. 5, p. 056016, Sep. 2012.
- [120] J. Zhang, Z. Yin, P. Chen, and S. Nichele, “Emotion recognition using multi-modal data and machine learning techniques: A tutorial and review,” Information Fusion, vol. 59, pp. 103–126, Jul. 2020.
- [121] D. Wen, B. Liang, Y. Zhou, H. Chen, and T.-P. Jung, “The current research of combining multi-modal brain-computer interfaces with virtual reality,” IEEE Journal of Biomedical and Health Informatics, vol. 25, no. 9, pp. 3278–3287, Dec. 2020.
- [122] T. Kar´acsony, J. P. Hansen, H. K. Iversen, and S. Puthusserypady, “Brain computer interface for neuro-rehabilitation with deep learning classification and virtual reality feedback,” in Proceedings of the 10th Augmented Human International Conference 2019, Mar. 2019, pp. 1–8.
- [123] E. Bekele, J. Wade, D. Bian, J. Fan, A. Swanson, Z. Warren, and N. Sarkar, “Multimodal adaptive social interaction in virtual environment (masi-vr) for children with autism spectrum disorders (asd),” in 2016 IEEE virtual reality (VR). IEEE, 2016, pp. 121–130.
- [124] M. Hajinoroozi, Z. Mao, Y.-P. Lin, and Y. Huang, “Deep transfer learning for cross-subject and cross-experiment prediction of image rapid serial visual presentation events from eeg data,” in International Conference on Augmented Cognition. Springer, Jul. 2017, pp. 45–55.
- [125] D. Li, P. Ortega, X. Wei, and A. Faisal, “Model-agnostic meta-learning for eeg motor imagery decoding in brain-computer-interfacing,” in 2021 10th International IEEE/EMBS Conference on Neural Engineering (NER). IEEE, May 2021, pp. 527–530.
- [126] Y. Wang, S. Cang, and H. Yu, “A survey on wearable sensor modality centred human activity recognition in health care,” Expert Systems with Applications, vol. 137, pp. 167–190, Dec. 2019.
- [127] A. Berenguer, J. Goncalves, S. Hosio, D. Ferreira, T. Anagnostopoulos, and V. Kostakos, “Are smartphones ubiquitous?: An in-depth survey of smartphone adoption by seniors,” IEEE Consumer Electronics Magazine, vol. 6, no. 1, pp. 104–110, Dec. 2016.

- [128] M. A. Case, H. A. Burwick, K. G. Volpp, and M. S. Patel, “Accuracy of smartphone applications and wearable devices for tracking physical activity data,” Jama, vol. 313, no. 6, pp. 625–626, Feb. 2015.
- [129] L. Petrigna and G. Musumeci, “The metaverse: A new challenge for the healthcare system: A scoping review,” Journal of Functional Morphology and Kinesiology, vol. 7, no. 3, p. 63, Aug. 2022.
- [130] X. Su, H. Tong, and P. Ji, “Activity recognition with smartphone sensors,” Tsinghua Science and Technology, vol. 19, no. 3, pp. 235– 249, Jun. 2014.
- [131] M. E. Cecchinato, A. L. Cox, and J. Bird, “Smartwatches: The good, the bad and the ugly?” in Proceedings of the 33rd Annual ACM Conference Extended Abstracts on Human Factors in Computing Systems, Apr. 2015, pp. 2133–2138.
- [132] H. Motahari Nezhad, F. Zare, H. Akbari, and A. Sadeghdaghighi, “Health outcomes of fitbit, garmin or apple watch-based interventions,” Baltic Journal Of Health And Physical Activity, vol. 14, no. 4, 2022.
- [133] C. E. King and M. Sarrafzadeh, “A survey of smartwatches in remote health monitoring,” Journal of Healthcare Informatics Research, vol. 2, pp. 1–24, Jun. 2018.
- [134] S. D. Okegbile, J. Cai, C. Yi, and D. Niyato, “Human digital twin for personalized healthcare: Vision, architecture and future directions,” IEEE Network, Jul. 2022.
- [135] M. Y. Lim, J. Dias, R. Aylett, and A. Paiva, “Creating adaptive affective autonomous npcs,” Autonomous Agents and Multi-Agent Systems, vol. 24, pp. 287–311, Mar. 2012.
- [136] H. Duan, J. Li, S. Fan, Z. Lin, X. Wu, and W. Cai, “Metaverse for social good: A university campus prototype,” in Proceedings of the 29th ACM International Conference on Multimedia, Oct. 2021, pp. 153–161.
- [137] V. Taecharungroj, ““what can chatgpt do?” analyzing early reactions to the innovative ai chatbot on twitter,” Big Data and Cognitive Computing, vol. 7, no. 1, p. 35, Feb. 2023.
- [138] L. Rydell, “Predictive algorithms, data visualization tools, and artificial neural networks in the retail metaverse,” Linguistic and Philosophical Investigations, no. 21, pp. 25–40, 2022.
- [139] A. Hodorog, I. Petri, and Y. Rezgui, “Machine learning and natural language processing of social media data for event detection in smart cities,” Sustainable Cities and Society, vol. 85, p. 104026, Oct. 2022.
- [140] B. Osatuyi, “Information sharing on social media sites,” Computers in Human Behavior, vol. 29, no. 6, pp. 2622–2631, Nov. 2013.
- [141] L. Juh´asz and H. H. Hochmair, “Analyzing the spatial and temporal dynamics of snapchat,” in AnaLysis, Integration, Vision, Engagement (VGI-ALIVE) Workshop, Jun. 2018.
- [142] R. Wilken and L. Humphreys, “Placemaking through mobile social media platform snapchat,” Convergence, vol. 27, no. 3, pp. 579–593, Jun. 2021.
- [143] D. A. Parry, J. T. Fisher, H. Mieczkowski, C. J. Sewall, and B. I. Davidson, “Social media and well-being: A methodological perspective,” Current Opinion in Psychology, vol. 45, p. 101285, Jun. 2022.
- [144] A. Mottelson, A. Muresan, K. Hornbæk, and G. Makransky, “A systematic review and meta-analysis of the effectiveness of body ownership illusions in virtual reality,” ACM Transactions on Computer-Human Interaction, 2023.
- [145] G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw, “Bci2000: a general-purpose brain-computer interface (bci) system,” IEEE Transactions on Biomedical Engineering, vol. 51, no. 6, pp. 1034–1043, May 2004.
- [146] C.-T. Lin, Y.-C. Chen, T.-Y. Huang, T.-T. Chiu, L.-W. Ko, S.-F. Liang, H.-Y. Hsieh, S.-H. Hsu, and J.-R. Duann, “Development of wireless brain computer interface with embedded multitask scheduling and its application on real-time driver’s drowsiness detection and warning,” IEEE Transactions on Biomedical Engineering, vol. 55, no. 5, pp. 1582–1591, Apr. 2008.
- [147] W. He, Y. Zhao, H. Tang, C. Sun, and W. Fu, “A wireless bci and bmi system for wearable robots,” IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 46, no. 7, pp. 936–946, Dec. 2015.
- [148] S. R. A. Jafri, T. Hamid, R. Mahmood, M. A. Alam, T. Rafi, M. Z. Ul Haque, and M. W. Munir, “Wireless brain computer interface for smart home and medical system,” Wireless Personal Communications, vol. 106, no. 4, pp. 2163–2177, Jun. 2019.
- [149] C.-T. Lin, C.-J. Chang, B.-S. Lin, S.-H. Hung, C.-F. Chao, and I.J. Wang, “A real-time wireless brain-computer interface system for drowsiness detection,” IEEE Transactions on Biomedical Circuits and Systems, vol. 4, no. 4, pp. 214–222, Apr. 2010.
- [150] A. I. N. Alshbatat, P. J. Vial, P. Premaratne, and L. C. Tran, “Eeg-based brain-computer interface for automating home appliances,” Journal of Computers, 2014.

- [151] J. Rosenthal, A. Sharma, E. Kampianakis, and M. S. Reynolds, “A 25 mbps, 12.4 pj/b dqpsk backscatter data uplink for the neurodisc brain–computer interface,” IEEE Transactions on Biomedical Circuits and Systems, vol. 13, no. 5, pp. 858–867, Aug. 2019.
- [152] K. F. Navarro, “Wearable, wireless brain computer interfaces in augmented reality environments,” in International Conference on Information Technology: Coding and Computing, 2004. Proceedings. ITCC 2004., vol. 2. IEEE, Apr. 2004, pp. 643–647.
- [153] N. Q. Hieu, D. T. Hoang, D. N. Nguyen, and E. Dutkiewicz, “Enabling immersion and presence in the metaverse with over-the-air braincomputer interface,” arXiv preprint arXiv:2303.10577, 2023.
- [154] R. C. Moioli, P. H. Nardelli, M. T. Barros, W. Saad, A. Hekmatmanesh, P. E. G. Silva, A. S. de Sena, M. Dzaferagic, H. Siljak, and W. Van Leekwijck, “Neurosciences and wireless networks: The potential of brain-type communications and their applications,” IEEE Communications Surveys & Tutorials, vol. 23, no. 3, pp. 1599–1621, 2021.
- [155] C. Perfecto, M. S. Elbamby, J. Del Ser, and M. Bennis, “Taming the latency in multi-user vr 360°: A qoe-aware deep learning-aided multicast framework,” IEEE Transactions on Communications, vol. 68, no. 4, pp. 2491–2508, Jan. 2020.
- [156] X. Wei, C. Yang, and S. Han, “Prediction, communication, and computing duration optimization for vr video streaming,” IEEE Transactions on Communications, vol. 69, no. 3, pp. 1947–1959, Nov. 2020.
- [157] P. Xiang, H. Shan, Z. Zhang, L. Yu, and T. Q. Quek, “Noma based vr video transmissions exploiting user behavioral coherence,” in 2020 IEEE Wireless Communications and Networking Conference (WCNC). IEEE, May 2020, pp. 1–6.
- [158] N. Q. Hieu, D. N. Nguyen, D. T. Hoang, and E. Dutkiewicz, “When virtual reality meets rate splitting multiple access: A joint communication and computation approach,” IEEE Journal on Selected Areas in Communications, vol. 41, no. 5, pp. 1536–1548, Jan. 2023.
- [159] Y. Mao, O. Dizdar, B. Clerckx, R. Schober, P. Popovski, and H. V. Poor, “Rate-splitting multiple access: Fundamentals, survey, and future research trends,” IEEE Communications Surveys & Tutorials, Jul. 2022.
- [160] Z. Qin, X. Tao, J. Lu, and G. Y. Li, “Semantic communications: Principles and challenges,” arXiv preprint arXiv:2201.01389, 2021.
- [161] W. Klimesch, H. Schimke, and J. Schwaiger, “Episodic and semantic memory: an analysis in the eeg theta and alpha band,” Electroencephalography and clinical Neurophysiology, vol. 91, no. 6, pp. 428– 441, Dec. 1994.
- [162] S.-H. Lee, M. Lee, and S.-W. Lee, “Neural decoding of imagined speech and visual imagery as intuitive paradigms for bci communication,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 28, no. 12, pp. 2647–2659, Nov. 2020.
- [163] M. Kritzler, M. Funk, F. Michahelles, and W. Rohde, “The virtual twin: Controlling smart factories using a spatially-correct augmented reality representation,” in Proceedings of the Seventh International Conference on the Internet of Things, Oct. 2017, pp. 1–2.
- [164] B. Moya, A. Bad´ıas, I. Alfaro, F. Chinesta, and E. Cueto, “Digital twins that learn and correct themselves,” International Journal for Numerical Methods in Engineering, vol. 123, no. 13, pp. 3034–3044, Jul. 2022.
- [165] L. U. Khan, W. Saad, D. Niyato, Z. Han, and C. S. Hong, “Digitaltwin-enabled 6g: Vision, architectural trends, and future directions,” IEEE Communications Magazine, vol. 60, no. 1, pp. 74–80, Jan. 2022.
- [166] M. Dunleavy and C. Dede, “Augmented reality teaching and learning,” Handbook of Research on Educational Communications and Technology, pp. 735–745, 2014.
- [167] X. Zhang, L. Yao, D. Zhang, X. Wang, Q. Z. Sheng, and T. Gu, “Multi-person brain activity recognition via comprehensive eeg signal analysis,” in Proceedings of the 14th EAI International Conference on Mobile and Ubiquitous systems: Computing, Networking and Services, Nov. 2017, pp. 28–37.
- [168] M. J. Eugster, T. Ruotsalo, M. M. Spap´e, I. Kosunen, O. Barral, N. Ravaja, G. Jacucci, and S. Kaski, “Predicting term-relevance from brain signals,” in Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval, Jul. 2014, pp. 425–434.
- [169] H. Ji, J. Li, R. Lu, R. Gu, L. Cao, and X. Gong, “Eeg classification for hybrid brain-computer interface using a tensor based multiclass multimodal analysis scheme,” Computational Intelligence and Neuroscience, vol. 2016, Jan. 2016.
- [170] R. Ju, C. Hu, and Q. Li, “Early diagnosis of alzheimer’s disease based on resting-state brain networks and deep learning,” IEEE/ACM Transactions on Computational Biology and Bioinformatics, vol. 16, no. 1, pp. 244–257, 2017.

- [171] A. Mohammed, M. Zamani, R. Bayford, and A. Demosthenous, “Toward on-demand deep brain stimulation using online parkinson’s disease prediction driven by dynamic detection,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 12, pp. 2441–2452, Jul. 2017.
- [172] R. Yuste, S. Goering, G. Bi, J. M. Carmena, A. Carter, J. J. Fins, P. Friesen, J. Gallant, J. E. Huggins, and J. Illes, “Four ethical priorities for neurotechnologies and ai,” Nature, vol. 551, no. 7679, pp. 159–163, Nov. 2017.
- [173] Z. Zheng, S. Xie, H. Dai, X. Chen, and H. Wang, “An overview of blockchain technology: Architecture, consensus, and future trends,” in 2017 IEEE International Congress on Big Data (BigData congress). IEEE, Jun. 2017, pp. 557–564.
- [174] C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow, and R. Fergus, “Intriguing properties of neural networks,” in 2nd International Conference on Learning Representations, ICLR 2014, Jan. 2014.
- [175] A. B. Arrieta, N. D´ıaz-Rodr´ıguez, J. Del Ser, A. Bennetot, S. Tabik, A. Barbado, S. Garc´ıa, S. Gil-L´opez, D. Molina, and R. Benjamins, “Explainable artificial intelligence (xai): Concepts, taxonomies, opportunities and challenges toward responsible ai,” Information Fusion, vol. 58, pp. 82–115, 2020.
- [176] L. Drew, “The ethics of brain-computer interfaces,” Nature, vol. 571, no. 7766, pp. S19–S19, Jul. 2019.
- [177] Braincom, “High-density cortical implants for cognitive neuroscience and rehabilitation of speech using brain-computer interfaces,” Accessed: Aug. 15, 2023. [Online]. Available: http://www.braincom-project.eu/about/
- [178] X. Meng, R. Jiang, D. Lin, J. Bustillo, T. Jones, J. Chen, Q. Yu, Y. Du, Y. Zhang, and T. Jiang, “Predicting individualized clinical measures by a generalized prediction framework and multimodal fusion of mri data,” Neuroimage, vol. 145, pp. 218–229, 2017.
- [179] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in Neural Information Processing Systems, vol. 30, 2017.

Dinh Thai Hoang (M’16, SM’22) is currently a faculty member at the School of Electrical and Data Engineering, University of Technology Sydney, Australia. He received his Ph.D. in Computer Science and Engineering from the Nanyang Technological University, Singapore 2016. His research interests include emerging wireless communications and networking topics, especially machine learning applications in networking, edge computing, and cybersecurity. He has received several precious awards, including the Australian Research Council

[Figure 97]

Discovery Early Career Researcher Award, IEEE TCSC Award for Excellence in Scalable Computing for Contributions on “Intelligent Mobile Edge Computing Systems” (Early Career Researcher), IEEE Asia-Pacific Board (APB) Outstanding Paper Award 2022, and IEEE Communications Society Best Survey Paper Award 2023. He is currently an Editor of IEEE TMC, IEEE TWC, IEEE TCCN, IEEE TVT, and IEEE COMST.

Howe Yuan Zhu received his Ph.D. degree in computer science at the University of Technology Sydney in 2022. He received his BSc in Biomedical Engineering at the University of Sydney in 2017. He is currently a research associate at the University of Technology Sydney and a core GrapheneXUTS Human-centric Artificial Intelligence Centre (HAI) member. His current research interests are XR/VR/AR, brain-computer interfaces, robotics, artificial intelligence in robotics, and human-computer interaction. He is actively exploring translational

[Figure 98]

applications of wearable XR technologies for medical applications and understanding human factors for assistive technologies.

[Figure 99]

Nguyen Quang Hieu received the B.E. degree in Hanoi University of Science Technology, Vietnam in 2018. He is currently a Ph.D. student at School of Electrical and Data Engineering, University of Technology (UTS), Sydney, Australia. Before joining UTS, he was a research assistant at School of Computer Science and Engineering, Nanyang Technological University, Singapore. His research interests include wireless communications, network optimization, reinforcement learning, and deep learning..

Diep N. Nguyen (Senior Member, IEEE) received the M.E. degree in electrical and computer engineering from the University of California at San Diego (UCSD), La Jolla, CA, USA, in 2008, and the Ph.D. degree in electrical and computer engineering from The University of Arizona (UA), Tucson, AZ, USA, in 2013. He is currently a faculty member with the Faculty of Engineering and Information Technology, University of Technology Sydney (UTS), Sydney, NSW, Australia. Before joining UTS, he was a DECRA Research Fellow with Macquarie University,

[Figure 100]

Macquarie Park, NSW, Australia, and a Member of the Technical Staff with Broadcom Corporation, San Jose, CA, USA, and ARCON Corporation, Boston, MA, USA, and consulting the Federal Administration of Aviation, Washington, DC, USA, on turning detection of UAVs and aircraft, and the U.S. Air Force Research Laboratory, USA, on anti-jamming. His research interests include computer networking, wireless communications, and machine learning application, with emphasis on systems’ performance and security/privacy. Dr. Nguyen received several awards from LG Electronics, UCSD, UA, the U.S. National Science Foundation, and the Australian Research Council. He has served on the Editorial Boards of the IEEE Transactions on Mobile Computing, IEEE Communications Surveys & Tutorials (COMST), IEEE Open Journal of the Communications Society, and Scientific Reports (Nature’s).

Distinguished Professor Chin-Teng Lin received a Bachelor’s of Science from National Chiao-Tung University (NCTU), Taiwan in 1986, and holds Master’s and PhD degrees in Electrical Engineering from Purdue University, USA , received in 1989 and 1992, respectively.

[Figure 101]

He is currently a distinguished professor and Co-Director of the Australian Artificial Intelligence Institute within the Faculty of Engineering and Information Technology at the University of Technology Sydney, Australia. He is also an Honorary Chair Pro-

fessor of Electrical and Computer Engineering at NCTU. For his contributions to biologically inspired information systems, Prof Lin was awarded Fellowship with the IEEE in 2005, and with the International Fuzzy Systems Association ( IFSA) in 2012. He received the IEEE Fuzzy Systems Pioneer Award in 2017. He has held notable positions as editor-in-chief of IEEE Transactions on Fuzzy Systems from 2011 to 2016; seats on Board of Governors for the IEEE Circuits and Systems (CAS) Society (2005-2008), IEEE Systems, Man, Cybernetics (SMC) Society (2003-2005), IEEE Computational Intelligence Society (20082010); Chair of the IEEE Taipei Section (2009-2010); Chair of IEEE CIS Awards Committee (2022, 2023); Distinguished Lecturer with the IEEE CAS Society (2003- 2005) and the CIS Society (2015-2017); Chair of the IEEE CIS Distinguished Lecturer Program Committee (2018-2019); Deputy Editor-inChief of IEEE Transactions on Circuits and Systems-II (2006-2008); Program Chair of the IEEE International Conference on Systems, Man, and Cybernetics (2005); and General Chair of the 2011 IEEE International Conference on Fuzzy Systems.

Prof Lin is the co-author of Neural Fuzzy Systems (Prentice-Hall) and the author of Neural Fuzzy Control Systems with Structure and Parameter Learning (World Scientific). He has published more than 425 journal papers including about 200 IEEE journal papers in the areas of neural networks, fuzzy systems, brain-computer interface, multimedia information processing, cognitive neuro-engineering, and human-machine teaming, that have been cited more than 34,000 times. Currently, his h-index is 90, and his i10-index is 401.

