REVIEW
published: 31 January 2018
doi: 10.3389/fnhum.2018.00014
Edited by:
Mikhail Lebedev,
Duke University, United States
Reviewed by:
Minkyu Ahn,
Handong Global University,
South Korea
Filippo Brighina,
Università degli Studi di Palermo, Italy
*Correspondence:
Ioulietta Lazarou
iouliettalaz@iti.gr;
iouliettalaz@hotmail.com
Received: 12 December 2016
Accepted: 12 January 2018
Published: 31 January 2018
Citation:
Lazarou I, Nikolopoulos S,
Petrantonakis PC, Kompatsiaris I and
Tsolaki M (2018) EEG-Based
Brain–Computer Interfaces for
Communication and Rehabilitation of
People with Motor Impairment: A
Novel Approach of the 21st Century.
Front. Hum. Neurosci. 12:14.
doi: 10.3389/fnhum.2018.00014
EEG-Based Brain–Computer
Interfaces for Communication and
Rehabilitation of People with Motor
Impairment: A Novel Approach of the
21st Century
Ioulietta Lazarou1,2,3*, Spiros Nikolopoulos1, Panagiotis C. Petrantonakis1,
Ioannis Kompatsiaris1 and Magda Tsolaki1,2,3
1 Information Technologies Institute, Centre for Research and Technology Hellas, Thessaloniki, Greece, 2 1st Department of
Neurology, University Hospital “AHEPA”, School of Medicine, Aristotle University of Thessaloniki, Thessaloniki, Greece,
3 Greek Association of Alzheimer’s Disease and Related Disorders, Thessaloniki, Greece
People with severe neurological impairments face many challenges in sensorimotor
functions and communication with the environment; therefore they have increased
demand for advanced, adaptive and personalized rehabilitation. During the last several
decades, numerous studies have developed brain–computer interfaces (BCIs) with the
goals ranging from providing means of communication to functional rehabilitation. Here
we review the research on non-invasive, electroencephalography (EEG)-based BCI
systems for communication and rehabilitation. We focus on the approaches intended
to help severely paralyzed and locked-in patients regain communication using three
different BCI modalities: slow cortical potentials, sensorimotor rhythms and P300
potentials, as operational mechanisms. We also review BCI systems for restoration of
motor function in patients with spinal cord injury and chronic stroke. We discuss the
advantages and limitations of these approaches and the challenges that need to be
addressed in the future.
Keywords: brain–computer interfaces (BCI), electroencephalogram (EEG), slow cortical potentials (SCP),
sensorimotor rhythms (SMR), P300, communication, rehabilitation, neuromuscular disorders (NMD)
INTRODUCTION
Vidal (1973, p. 157), in his seminal work, raised the question: “Can observable electrical brain
signals be put to work as carriers of information in person–computer communication or for
the purpose of controlling devices such as prostheses?”. Since then, we have come a long way
investigating whether people with motor disabilities can repurpose brain activity from inner neural
signals to tangible controls that attribute the user’s intent to interact with devices or adjust their
Abbreviations: A-CM, Arnold-Chiari malformation; ALS, amyotrophic lateral sclerosis; BCI, brain–computer interface;
CA, classiﬁcation accuracy; CBP, checkerboard paradigm; CCD, cortical current density; CLIS, complete locked-in state; CP,
cerebral palsy; CRR, correct response rate; DMD, Duchenne muscular dystrophy; EEG, electroencephalogram; ERD, event-
related de-synchronization; ERP, event-related potential; ERS, event-related synchronization; ITR, information transfer rate;
LC, corresponding laterality coeﬃcient; LIS, locked-in state; MI, motor imagery; MS, multiple sclerosis; NMD, neuromuscular
disorders; RCP, row–column paradigm; SCI, spinal cord injury; SCPs, slow cortical potentials; SMA II/III, spinal muscular
atrophy type II/III; SMR, sensorimotor rhythms; Spastic CP, spastic cerebral palsy; TBI, traumatic brain injury; TTD, thought
translation device; VE, virtual environment.
Frontiers in Human Neuroscience | www.frontiersin.org
1
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
environment (Shih et al., 2012; Lebedev and Nicolelis, 2017).
Nowadays, several advancements in the ﬁelds of clinical
neurophysiology and computational neuroscience have led to
the development of promising approaches based on non-invasive
BCIs that pave the way for reliable communication and eﬀective
rehabilitation of people with disabilities.
In this review, we focus on non-invasive BCI applications
geared toward alternative communication and restoration of
movement to paralyzed patients. We consider several milestone
studies on EEG-based BCIs that contributed to the systems
that improve everyday life and activity of people with motor
disabilities in the 21st century. We review EEG-based BCI
technologies for communication and control based on three
diﬀerent EEG signals (SCP, SMR and P300), and discuss their
limitations and advantages. In addition, we examine and analyze
the BCI methods for inducing brain plasticity and restoring
functions in impaired patients. An overview of the study
framework is presented in Figure 1.
The paper is structured as follows. We ﬁrstly review the
advantages of the BCI approach compared to other strategies for
communication in people with motor impairment. In section 3,
we present BCI realizations based on diﬀerent approaches for
brain activity recording, and elaborate on three EEG-based
modalities: SCP, SMR, and P300. Subsequently, we provide
an elaborate overview of the milestone studies, published
mainly during the last two decades, on the BCI systems
for communication and rehabilitation in patients with motor-
impairments. Finally, we discuss advantages and shortfalls of
these BCIs, point out their limitations and comment on the future
perspectives in this ﬁeld.
WHY BRAIN–COMPUTER INTERFACES?
In most cases of NMD, there is gradual loss of muscle activity
that aﬀects speaking, walking and execution of ﬁne motor tasks
and results in the deterioration of quality of life. Although the
symptoms of the diseases are easier to cope with during their
early stages, they become much more severe in the late stages.
Thus, speciﬁc priorities must be set forth in order to develop
systems that will be deployable for each stage of the disease,
even for late stages. The majority of people with NMD indicate
a preference for portable solutions, such as a tablet or a laptop
(Mackenzie et al., 2016). Nevertheless, one common issue that
may arise of these devices, is their inability to adapt to patient’s
need, especially at late stages of the disease where many abilities
have deteriorated. Even though many technological adaptive
devices are currently utilized, such as “SmartNav1” and eye gaze
technology, they require extensive user training and have several
limitations (Mackenzie et al., 2016). For example, the gaze-based
technology has been found to be erroneous for selecting small
objects/icons, burdensome and diﬃcult to be operated, diﬃcult
to be adjusted and calibrated, as well as costly (Ball et al., 2010).
In addition, current technological assistive solutions using eye
trackers enable people with motor disabilities to communicate
1https://www.naturalpoint.com/smartnav/
and control devices at home. The abovementioned systems result
in a very low workload (Calvo et al., 2008), whereas participants
with ALS have responded positively to using them on a daily
basis (Gibbons and Beneteau, 2010). Nevertheless, the main
problem of using eye trackers as an assistive technology (AT),
is the so-called “Midas touch problem” (Majaranta and Räihä,
2002). In essence, the direction of gaze in many cases does not
coincide with the focus of attention and consequently the ﬁnal
selections are diﬀerent from the users’ intention (Majaranta and
Räihä, 2002; Karat and Vanderdonckt, 2009; Nicolas-Alonso and
Gomez-Gil, 2012; Pasqualotto et al., 2015; Ordikhani-Seyedlar
et al., 2016). Other systems (e.g., “Eye-Go”) utilize eye-tracking
methods for wheelchair maneuvering (Gajwani and Chhabria,
2010). Nevertheless, there are still several limitations regarding
both the ability to alter or change seating position and the
capacity of maneuvering the wheelchair to a speciﬁc direction by
using eye movement, which poses requirements for both system
software and for eye-tracking technology (Wastlund et al., 2015).
Besides gaze-based interaction, there are also speech-based
interfaces like the Dragon Dictate Speech (DDS) recognition
system (Zimmer et al., 1991). The system learns a user’s
vocabulary and mode of speaking by analyzing language and
responds to natural language instead of limited phrases and
words. However, it needs many adaptations, such as microphone
positioning, and training, so it is not useful for people at
late stages of NMD who have totally lost their ability to
speak. Furthermore, speech-driven interfaces are limited by the
number of supported languages. Although English is extensively
supported, this is not the case for less popular languages (e.g.,
Greek).
Other solutions utilize robotic assistive devices for motor
disabled people (Corke, 2007). The usability of such devices is
still doubtful due to the necessity of residual motor ability for
their operation (e.g., limb, head and/or eye movements, speech
etc.) (Cincotti et al., 2008b). For people in extreme pathological
conditions (e.g., those who are in CLIS without any remaining
muscle control), the use of such systems may not be possible.
Additionally, recent studies have underlined the importance of
BCI systems in rehabilitation and restoration of motor function.
For instance, the Personalized Self-Managed rehabilitation
System (PSMrS), is a prototype system integrated with an insole
sensor technology (“intelligent shoe”) (Mawson et al., 2016).
It has been developed to enable people who survived stroke
to self-manage their rehabilitation by encouraging achievement
of personal and adaptive functional goals and performance of
speciﬁc motor activities within those goals. However, people who
participated in this study and used this technology reported a
number of limitations such as the lack of feedback and lack
of motivation of the user (Mawson et al., 2016). Other studies
focus on the use of technical solutions for the rehabilitation of
participants with motor disabilities (e.g., MS), by using KINECT
and augmented reality (AR) for rehabilitation of gait (Lozano-
Quilis, 2013; McMullen et al., 2014), or the use of natural user
interfaces (NUIs) for rehabilitation of participants with reduced
motor skills (Fulk, 2005; Baram and Miller, 2006; Lozano-Quilis
et al., 2014). Systems for motor rehabilitation of MS participants
were tested with patient in the mild stages of the disease (they
Frontiers in Human Neuroscience | www.frontiersin.org
2
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
FIGURE 1 | Overview of the review framework.
were capable to move their limbs), but their eﬀectiveness in the
late stages (e.g., LIS) has not been documented.
Brain–computer
interface
systems
promise
to
oﬀer
a
unique and multimodal solution for both communication and
rehabilitative therapy that will overcome the shortfalls of the
abovementioned approaches (Chaudhary et al., 2016). In general,
BCI is a computer-based system which translates brain signals
into commands that are passed onto an external application or
appliance so as to facilitate user’s intention. As a result people
can communicate with the environment, although they do
not use their peripheral nervous system and muscles (Wolpaw
et al., 2000). The idea of operating an external device with
one’s thoughts is a highly promising option for people whose
functions such as speech or motion are impaired. Many clinical
studies on BCI research ﬁeld have highlighted not only the
potential utility and integration of these innovative technological
approaches into life of people with motor impairment, but also
the positive impact occurring by translating scientiﬁc knowledge
and experimental design into clinical beneﬁts by enabling
a novel real-time communication between the user and the
external world (Bowsher et al., 2016). In terms of utility, BCI
technology gives the opportunity to individuals who are not
able to speak and/or use their limbs not only to communicate
and interact with others, but also to operate such appliances as
domestic devices, computers, speech synthesizers and assistive
deployments, or even control neural prosthetics for walking
and manipulating objects (Wolpaw et al., 2002); even in CLIS
(Chaudhary et al., 2017). Nevertheless, many BCI systems have
also some drawbacks, since users might need long periods of
training to learn to control their brain rhythms (Pires et al.,
2012) or have problems to conveniently operate the BCI system
such as problems with switching it oﬀand on (“Midas touch”
problem) (Nicolas-Alonso and Gomez-Gil, 2012). Nevertheless,
BCI systems could improve the quality of life (QoL) of people
with motor impairment as a result of social inclusion (Sellers
et al., 2010; Holz et al., 2015), even in CLIS (Liu et al., 2011).
Indeed, communication ability is of high priority in improving
QoL of people with motor impairments (Bach, 1993; Kubler
et al., 2005).
BCI SYSTEMS
There are various techniques and operational mechanisms
that are used in order to record brain activity and extract
useful signals. BCI systems are based on invasive recordings,
Frontiers in Human Neuroscience | www.frontiersin.org
3
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
i.e., implantable electrodes or grid recordings from the cortex
(ECoG) (Bleichner et al., 2016), local ﬁeld potentials (LFPs)
(Jerbi et al., 2009), multi-unit activity (MUA) or single-unit
activity (SUA) (Watanabe, 2011), as well as non-invasive methods
such as EEG, magnetoencephalography (MEG) (Ahn et al.,
2013), functional magnetic resonance imaging (fMRI) (Zich
et al., 2015), and near-infrared spectroscopy (NIRS) (Hosseini
et al., 2016). Other approaches concerning combinations of
aforementioned recording techniques with additional electrical
stimulation have also been proposed, such as electrical/magnetic
stimulation (Daly et al., 2009; Ang et al., 2015; Hanselmann
et al., 2015). From all the abovementioned approaches for BCI
system realization, EEG recordings have been more thoroughly
studied and used (Hinterberger et al., 2003; Klobassa et al., 2009;
Corralejo et al., 2014) due to their eﬀective implementations,
non-invasiveness, and portable and adaptable manifestation,
(Remsik et al., 2016). Thus, this review concerns only EEG-
based BCI systems. Moreover, diﬀerent BCI applications will
be reviewed and evaluated qualitatively and quantitatively using
two measures: CA, i.e., the percentage of correctly classiﬁed BCI
controls when the user operates a BCI system and ITR, i.e.,
the ITR, given in bits per selection or bits/min. In the case of
CA we will use the terms Low or High performance, with Low
performance referring to CA lower than 90% (Huggins et al.,
2011).
EEG-BCI Neurophysiological Input
There are diﬀerent types of EEG-based BCI systems for
promoting communication (Wolpaw et al., 1991), environmental
control and rehabilitation depending on diﬀerent modalities of
the EEG, namely SCPs, SMR, P300 event related potentials and
Steady State Visual Evoked Potentials (SSVEPs).
Slow Cortical Potential
An EEG-based BCI can rely on SCPs, which allow anatomically
speciﬁc
voluntary
activation
of
diﬀerent
brain
areas.
Neurophysiologically, SCPs are the result of intracortical or
thalamocortical inputs to diﬀerent cortical layers; they arise
from simultaneous polarization of large cohorts of apical
dendrites of pyramidal neurons (Kübler and Birbaumer, 2008).
Depolarization of cortical cell assemblies reduces their excitation
threshold, and ﬁring of neurons in regions responsible for
motor or cognitive tasks is facilitated (Birbaumer et al., 1990).
In normal brain function, negative SCPs accompany preparatory
depolarization of the underlying cortical network, whereas
positive SCPs are thought to reﬂect cortical disaﬃliation or
inhibition. With substantial training, control of SCPs to produce
positive or negative voltage shifts can be learnt and used for basic
word processing and other tasks (Leeb et al., 2015). However,
SCP-BCI systems need long training periods, professional
attention and continuous technical support, while not all patients
can gain full control of their SCPs.
Sensorimotor Rhythms
Apart from SCP, there are many EEG-based BCI systems that rely
on SMRs (Neuper et al., 2003; Wolpaw, 2007; Sellers et al., 2010).
SMRs correspond to rhythms extracted from EEG signals that are
recorded exclusively over sensorimotor areas (i.e., µ-rhythm and
β-rhythm) and allow anatomically speciﬁc voluntary regulation.
Typically they are movement-modulated rhythms, i.e., there is a
change either while someone performing a movement or during
MI or movement execution. Results from BCI studies have shown
that people can learn to self-regulate µ-rhythm or β-rhythm
amplitudes in the absence of any movement or sensation, and
subsequently to move a cursor to a speciﬁc position of the
computer screen, to select letters, or to operate an orthotic device
(Wolpaw and McFarland, 2004). In general, SMR-based control is
achieved through activation and deactivation of the central motor
areas and no external (e.g., visual) stimuli is necessary, since the
oscillatory EEG components are modulated by speciﬁc mental
strategies (e.g., MI of left hand) (Pfurtscheller and Neuper, 2001).
There are two distinct power changes in SMRs: (i) ERD or
power decrease seen in both alpha and beta bands that occur
up to 2 s before movement (Pfurtscheller et al., 1998; Bai et al.,
2005), and (ii) ERS or power increase, usually seen in the beta
band and referred to as post-movement beta synchronization,
occurring after the end of a movement (Pfurtscheller, 1988). It has
been demonstrated that SMR–based BCI systems are possible to
enable people with motor disabilities to operate an environmental
control system or a simple word-processor faster than SCP-EEG
based BCI systems (Wolpaw and McFarland, 2004; Kübler et al.,
2005), while, it has been also proposed as a potential solution for
motor rehabilitation (Pfurtscheller et al., 2000; Ono et al., 2014).
On the contrary, the need for extensive training sessions that are
necessary to gain suﬃcient SMR regulation control, comprise the
main shortfall of this approach. Finally, another drawback of the
SMR approach is the discrimination capacity of SMR features that
correspond to diﬀerent imaginary movements that in some cases
results in ineﬀective communication (Karat and Vanderdonckt,
2009).
Evoked Potentials
P300 is an ERP and is one of the most commonly used EEG-based
modalities (Donchin, 1987). The P300 is evoked approximately
300 ms after a triggering stimulus; it corresponds to a positive
voltage peak (Li et al., 2010). P300-based BCIs capitalize on
discriminating this voltage peak from background signal noise,
and associating the desired signal with an event. ERPs are
associated with a stimuli that provides task-relevant information
(Baykara et al., 2015). P300 has been popular in BCI research
due to its ease of evocation and consistency (Duncan et al.,
2009). It requires little initial training of the subject (Piccione
et al., 2006; Sellers and Donchin, 2006; Fazel-Rezai et al., 2012).
Nevertheless, in a recent meta-analysis (Marchetti et al., 2014),
accumulated evidence from recent studies of P300-speller BCIs
with ALS participants, showed that the estimated CA was of
the order of 74%, much lower than 90% that has been set as
the acceptable threshold for ALS participants (Huggins et al.,
2011). Moreover, it has been shown that P300-based BCI systems
could be aﬀected by overall clinical severity (Piccione et al.,
2006; Sellers and Donchin, 2006; Hoﬀmann et al., 2008) and
worse BCI performance can be detected in motor impaired
ALS patients due to habituation or fatigue eﬀects (Sellers and
Donchin, 2006). Recent studies suggested that P300-based BCIs
Frontiers in Human Neuroscience | www.frontiersin.org
4
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
could be useful for ALS patients (Nijboer et al., 2008; Corralejo
et al., 2014). Finally, some studies reported as main disadvantage
the low ITR of P300-based BCIs, especially for people with motor
impairments (Mugler et al., 2010; Mauro et al., 2011; Nam et al.,
2012; Holz et al., 2013). Nevertheless, higher ITRs have also been
reported (Kaufmann et al., 2013) using appropriately selected
stimuli (e.g., faces).
Steady State Visual Evoked Potentials are evoked by an
oscillating stimulus modulated at a ﬁxed frequency and occur
as an increase in EEG activity at the stimulation frequency
(Valbuena et al., 2010). The typical SSVEP-based BCI application
utilizes multiple visual ﬂashing stimuli, such as digits or letters
on a screen, while the user looks at one of the symbols
and focuses his attention on it (Lesenfants et al., 2014).
When the users concentrate their attention on one of the
stimuli, the stimulus evokes an increased SSVEP response at
the corresponding frequency over the occipital area of the
brain. Thus, the user has to keep eye ﬁxation. This type of
BCI depends on attentional capacity and vision to be intact,
and both are often compromised in patients with advanced
and severe neurological disease (Chaudhary et al., 2016).
Therefore, SSVEPs are not suitable for patients in advanced
stages of Amyotrophic Lateral Sclerosis (ALS-LIS) or with
uncontrollable eye movements (Nicolas-Alonso and Gomez-
Gil, 2012). A number of SSVEP-based BCI systems have been
developed and applied to operating a prosthesis (Muller-Putz
and Pfurtscheller, 2008) or controlling an avatar in a virtual
reality environment (Faller et al., 2010) by healthy individuals.
The conventional SSVEP-based BCI systems described above
commonly require the basic assumption that the users have
normal oculomotor function and are thus able to maintain
gaze at a given visual stimulus consistently (Lim et al., 2013).
However, as already mentioned, it has been reported that some
patients suﬀering from serious NMDs have diﬃculty controlling
their eyes (Donaghy et al., 2010), while many ALS patients
have oculomotor impairments (Sharma et al., 2011) causing
abnormal visual perception. These patients would not be able
to open their eyes and continuously ﬁxate a visual stimuli.
A recent study used SSVEP-BCI in ALS patients with LIS and
only one out of four was able to communicate online. This
low success rate was attributed to symptoms accompanied with
clinical conditions of these patients: fatigue, persistent nystagmus
preventing eﬀective perception of the stimuli (Lesenfants et al.,
2014). This represents an important limitation for patients
with loss of gaze control and other clinical issues. For all the
aforementioned drawbacks, in this work we exclude the SSVEP
studies as we intend to discuss approaches concerning users with
motor impairments.
EEG-BASED BCI SYSTEMS FOR
PEOPLE WITH MOTOR-IMPAIRMENT
Electroencephalography-based BCI systems show great potential
for widespread clinical use. Over the past two decades, many
studies have been published presenting non-invasive approaches
for severely or partially paralyzed people reacquiring basic
forms of controlling neuroprostheses, wheelchairs and electrical
appliances. The purpose of using BCIs can be distinguished
in two main categories: (a) Communication and Control and
(b) Rehabilitation. By communication and control we refer
to the ability of BCIs to enable communication with such
devices as speech synthesizers, word processors, computer email
applications, wheelchairs, prosthetic robotic arms, or orthotic
devices. (Control of a device can be considered as a means of
communication with the environment, and thus we consider the
term “communication” in its generic meaning in this review).
Finally, by rehabilitation we refer to therapies that use BCI
systems for regaining the lost motor control for people suﬀering
from neurological disorders (e.g., stroke). Below, we elaborate on
these concepts.
Communication and Control
BCI Systems Using Slow Cortical Potentials (SCP)
The TTD system
Slow cortical potentials-EEG-based BCI systems require users’
training to shift the polarity (positive or negative) of their SCPs.
The ﬁrst seminal study on EEG-BCI with two patients in LIS ALS
using SCP was conducted almost two decades ago (Birbaumer
et al., 1999). The patients were trained to voluntarily generate
SCPs, lasting 2–4 s, and during the response period, the subjects
were required to produce either negativity or positivity greater
than a speciﬁc amplitude. In a subsequent work (Birbaumer
et al., 2000) a TTD was developed. TTD trains participants at
LIS to self-regulate their SCPs in order to select letters, words
or pictograms in a computerized language support program.
This was one of the ﬁrst studies to show potential usefulness
and crucial role of TTD system in everyday life while great
improvement was shown regarding self-regulation and correct
responses after long period of training of ﬁve participants (LIS).
Kubler et al. (2001) expanded the previous TTD system by
introducing for the ﬁrst time “feedback training” by testing two
male participants at late ALS stage. The participants underwent a
training procedure which enabled them to communicate verbally,
by self-controlling their SCPs within the “Language Support
system” (Birbaumer et al., 2000), i.e., a system where the alphabet
is split into halves (letter-banks) which are presented successively
at the bottom of the screen for several seconds. If the subject
selects the letter-bank being shown by generating an SCP shift,
the letter bank is then split into two new halves and so on,
until each of the two letter-banks has only one letter in it.
After a training procedure of several months severely paralyzed
participants were able to communicate verbally. Moreover in
another work (Hinterberger et al., 2003), they trained an ALS
patient to use TTD for over 1 year so as to use this device in
order to communicate by spelling words. Also, they compared
diﬀerent EEG classiﬁcation algorithms of the three phases of
training in two sets (Set 1:“feedback training” phase by rewarding
the patient for producing cortical shifts in a requested direction,
Set 2: “copy-spelling mode” by requiring the participant to copy a
text, and “free-spelling mode” by self-selecting letters and words).
The patient’s average CRRs in the on-line training were 83 and
72% for the Set 1 and Set 2, respectively.
Frontiers in Human Neuroscience | www.frontiersin.org
5
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
In another work, ﬁve ALS participants were trained on how
to use their SCPs for eﬀective communication. Particularly, the
procedure included a training phase while during the copy
spelling and free spelling mode, participants had to select a
letter by producing positive SCP amplitude shifts or to reject
a letter by producing negative SCP amplitude shifts (Neumann
and Birbaumer, 2003). After several training sessions, they
measured the CRR and found that the more the participants
attended training sessions the higher was the accuracy and
correct response of each individual (except for one subject who
stopped the training). In essence, it was demonstrated that
the performance in SCP self-regulation after several sessions of
training can be predicted from an initial performance.
Another approach investigated the potential use of SCPs
as a control mechanism in order to promote communication
of an ALS patient by providing visual feedback of his actual
SCP amplitude (Neumann et al., 2003). More speciﬁcally the
experiment contained two training phases: (i) basic training: the
participant was trained in order to regulate his SCP amplitude
to exceed or to remain below a certain threshold in the cursor
movement time of the active phase, while in (ii) letter production
training: the participant had to “select” or “reject” letters by
self-regulating his SCPs. In general, this was a strategy for the
participants with motor impairment to learn how to write a text
based on his mental strategies to move the cursor (basic training).
After 6-months of training, the participant managed to self-
regulate his SCP by producing two diﬀerent brain responses. At
the end he managed to produce 454 words in German language
even though the speller yielded one letter per minute (a complete
text written by the participant using self-regulation of SCPs is
presented in the published article). Nevertheless, the participant
responded positively regarding the system’s use (Neumann et al.,
2003).
Web browsers
Another approach to using TTD system for handling a Web
Browser, namely “Descartes,” was ﬁrstly introduced in Karim
et al. (2006). The embedded system was tested with only one
ALS patient. Descartes provided feedback of SCP amplitude time-
locked manner after several sessions of training. To select a
command, the participant had to produce positive SCP alteration
(above a threshold of 7 µV) and move the cursor downward,
while for discarding a command, the participant had to generate
negative SCP and thus move the cursor upward. This was
the ﬁrst study to show that an EEG-controlled Web browser,
which is based on SCPs self-regulation, could be eﬃciently
and successfully operated by a severely paralyzed patient. It
was possible to access internet via the “Descartes” system but
there was great diﬃculty as regards to selecting an icon or a
picture on a Web page or selecting from an alphabetically sorted
decision tree. These disadvantages raised some issues regarding
the everyday use of such systems. Although the training phase of
the aforementioned study may be a proper procedure in order
to support patients so as to take advantage of BCIs and foster
communication, the participant had to exceed or to remain below
a certain threshold (7.7 µV) for operating the system and this
containment may not be suitable for everyday use.
BCIs Using Sensorimotor Rhythm (SMR)
People with NMDs can also learn to modulate their SMR
generated when a speciﬁc movement is executed or simply
imagined (MI).
Graz BCI system
One of the most highlighted SMR-BCI studies, namely the
“Graz-BCI” was tested on a severely paralyzed participant with
CP, who had totally lost the ability to communicate (Neuper
et al., 2003). After 80 trials the participant was able to select
letters and to copy words by using self-regulation of his SMR.
This study showed that “Graz-BCI” could eﬀectively decode
changes in SMR due to MI with a CA of 70% in the task
of letter selection. Nevertheless, the spelling rate was very low
(one letter per minute) and many adaptations of the classiﬁer
were necessary. On the other hand, SMR was also successful in
many cases with good CA (above 70%) but extensive training
and system adaptations were needed in almost all cases (Neuper
et al., 2003). Moreover, “Graz-BCI” was also used to enable four
paraplegic participants to communicate by using a MI task that
also incorporated a feedback module. More speciﬁcally, the task
in this study was a right-hand movement imagination, the so-
called “Basket-paradigm” with feedback, where the participants
had to move the ball into the correct “basket” (Krausz et al.,
2003). One aspect that should be highlighted in this study was
that the participants achieved high CA and an ITR between 8 and
17 bits/min without participants having any experience with the
BCI system before. This proved that the “Gratz-BCI” paradigm
can be easily learnt even by people who are not skilled at these
applications.
Cursor movement systems
Similarly, Wolpaw and McFarland (2004) developed an EEG-
BCI system based on SMR regulations. In this study the target
location was block-randomized (eight blocks) while the cursor
was presented in the middle of the screen. The cursor movement
was a weighted combination of the amplitudes in a mu (8–12 Hz)
or beta (18–26 Hz) rhythm over the right and left sensorimotor
cortices. Their results indicated that people can learn to use
scalp-recorded EEG rhythms to control movement of a cursor
in two dimensions, while this control is developing gradually
over training sessions. This study demonstrated that performance
gradually improved over the training sessions while participants
gradually gained better control over the rhythm amplitudes that
controlled the cursor.
In another study (Kübler et al., 2005), four ALS participants
were trained to move the cursor steadily across the screen with its
vertical movement controlled by SMR amplitude. After a training
period of 3–7 months, it was possible by MI to reduce rhythm
amplitude and, thus, to move the cursor down, while no-imagery
state did the opposite. Their results showed that over the initial 20
sessions of training, all four participants acquired SMR control,
proving that a SMR–based BCI might help participants with
ALS to maintain an acceptable quality of life with appropriate
communication systems (Kübler et al., 2005).
To exploring the feasibility and accuracy of the SMR
approach, one recent study (Cincotti et al., 2008a) applied
Frontiers in Human Neuroscience | www.frontiersin.org
6
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
high-resolution electroencephalographic (HREEG) techniques
that estimated cortical activity by using appropriate models of
volume conduction and neuro-electrical sources. In this study,
the authors examined 5 able-bodied participants and one with
a traumatic stabilized lesion located at the dorsal level. All
of them underwent a series of EEG acquisition sessions, in
which they were trained to gain control of their SMR, while
they were instructed to concentrate on kinesthetic imagination
of upper or lower limb movement in order to move the
cursor up-right and down-right, respectively. In this study,
the lateralization of electrical activity, which is expected to be
contralateral to the imaginary movement, is more evident on
the estimated CCD than in the scalp potentials and showed
that subjects who underwent training could utilize voluntary
modulation of estimated CCDs for accurate on-line control of a
cursor.
Furthermore,
McFarland
et
al.
(2008)
demonstrated
remarkable results as people with severe motor disabilities could
use brain signals for sequential multidimensional movement,
selection with two-dimensional cursor movement and target
selection through self-regulation of their SMR. This is one of the
ﬁrst and most highlighted studies which showed that people with
motor impairment can learn to use scalp-recorded EEG rhythms
so as to move a cursor in two dimensions to reach a target and
then to select the target.
Game applications
A noteworthy study tried to address the problem of long training
periods needed for people with motor impairment to learn how
to operate an EEG-BCI system. A game experiment that could
achieve a successful BCI operation in less than 30 min was
proposed (Kauhanen et al., 2007). More speciﬁcally, 6 tetraplegic
participants were asked to move a circle (which appeared on
the center of the screen) left or right by choosing one of the
movements of the upper limbs (e.g., ﬁst closing) and use them
(imagery task) during the experiment. Their results indicated that
three out of six subjects learned to control a BCI after training
and hit the target with rates 2.2–3.8 hits/min, with accuracy of
94, 67, and 57%, respectively, and an ITR of 8 bits/min. They
concluded that subjects could improve their performance after
more training since they could learn to produce more distinctive
brain activations during the attempted movements.
Similarly, Bai et al. (2008) investigated the role of extensive
training in the ability to control SMR. This is one of the
few studies where people with motor impairment showed
equal performance, in terms of CA, with able-bodied ones.
It was underlined that the reduced training time may be
particularly beneﬁcial for patient populations who have diﬃculty
in sustaining the mental eﬀort and concentration needed for
controlling SMR. In particular, a new BCI method was proposed
where subjects were asked to sustain motor execution (ERD) or
stop movement/imagery (ERS) in a binary cursor-control game.
Two motor impaired participants (one with stroke and one with
ALS) and nine healthy subjects participated and it was found that
by using MI, subjects were able to operate the proposed system
with good accuracy and with fast transfer rates (10–12 bits/min)
while, in terms of CA, average accuracy was, for motor execution
93.1% (healthy), 83% (Stroke), MI 80% (Stroke) and for ALS:
motor execution 90%, MI 90%.
Another study (Holz et al., 2013) developed a diﬀerent
approach for self-control of SMR rhythms throughout a game,
namely the “Connect-Four.” The proposed system exhibited low
eﬀectiveness, as compared to eﬀectiveness achieved by end-users
in other SMR-based BCI systems (70–100%) (Kauhanen et al.,
2007).
Although some of the abovementioned studies tried to address
SMR based BCI systems by reducing the time needed for training,
their results revealed low ITR 2.2–3.8 hits/min and showed that
participants’ performance improved with longer training periods
(Kauhanen et al., 2007; Jeon and Shin, 2015). This comes to add
in the great body of the literature suggesting that training is
necessary to gain successful self-control of SMR.
Virtual environments
Another study explored how a tetraplegic subject, sitting in
a wheelchair, could control his movements in a VE with a
self-paced (asynchronous) BCI system (Leeb et al., 2007). The
usage of the VE framework with talking avatars ensured that
the experiment is novel and engaging and contains enough
distractions as it would be in a real street environment. After four
runs, the subject was able to reach accuracy of 100%. This work
was the ﬁrst study which included avatars and VE and introduced
new ways of interaction and control of applications for people
with motor impairment in a VE by using MI. The fact that after
only four runs, the subject reached a successful performance of
100% shows that motivation induced by responses of the avatars
and more realistic conditions enables the participant to achieve
better performance (Leeb et al., 2007).
Control of external devices
There are also many studies which have highlighted the
importance of EEG-BCI for controlling external devices. In
Cincotti et al. (2008b) it was shown that people with severe NMDs
can acquire and maintain control over detectable patterns of
brain signals, and use this in order to control devices. Subjects
were asked to execute or to imagine movements of their hands or
feet upon the appearance of respective target. This study showed
for the ﬁrst time that an EEG-based BCI system can be integrated
into an environmental control system. If the user was not able
to master any of the devices, a training procedure followed.
Users needed to learn to modulate their SMR to achieve more
robust control than a simple imagination of limb movements
can produce. Over the 10 sessions of training, subjects acquired
brain control with an average classiﬁcation higher than 75% in
a binary selection task. Nevertheless, it should be stressed out
that only four out of 14 participants managed to achieve the
abovementioned accuracy.
In another study the potential use of SMR in control
of external domestic devices was investigated. As far as the
experimental procedure is concerned, initially, a rectangular
target appeared on the right side of the screen (up-right or down-
right). Afterward a cursor appeared in the middle of the left
side of the screen and moved at a constant horizontal speed
to the right. During the training sessions, subjects were asked
Frontiers in Human Neuroscience | www.frontiersin.org
7
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
to imagine the same kinesthetic movement during the visual
session. Four out of six participants with DMD were able to
control several electronic devices in the domestic context with the
BCI system, with a percentage of correct responses averaging over
63% whereas healthy subjects achieved rates of 70–80%.
Another study (Conradi et al., 2009), introduced the “one-
dimensional feedback task,” i.e., moving a cursor from the center
of a monitor to a randomly indicated horizontal direction. In
the second stage of the experiment, the feedback signal was
provided only at the end of each trial. Four out of seven
subjects were able to operate the BCI system via attempted (not
imagined) movements with their impaired limbs (both foot and
hand) with up to 84% CA. Moreover, it was highlighted that
the foot movements were more easily discriminated that hand
movements in the majority of the participants.
Furthermore, a recent study demonstrated the potential use
of a telepresence robot, which is remotely controlled by a BCI
system during a navigation task. In this task the participants
with motor impairment achieved similar CA to ten able-bodied
participants who were already familiar with the environment
(Leeb et al., 2015). The robot starts at a speciﬁc position, and
there were four target positions to be reached. The user’s task
was to drive the robot along one of three possible paths and then
back again to the starting position. Some end-users were able to
press speciﬁc buttons on a modiﬁed keyboard while others were
using “head switches” by imagining left hand, right hand and
feet movements during calibration recordings. However, people
with motor impairment needed more time in comparison with
healthy participants to complete the path. It is noteworthy that
the environment of the experiment contained natural obstacles
as in a real-life environment.
BCIs Using P300
An EEG modality that is very frequently used for operating a
BCI system is the widely known P300 component, which is a
late positive component evoked in response to an external task-
relevant stimulus. In particular the P300 component has been
used in order to control devices, such as wheelchairs, operate real
and VEs, and allow the user to use paint interfaces or browse the
Internet.
Speller systems
Speller systems are the main BCI applications that use the
P300 modality. One seminal work (Sellers and Donchin, 2006)
investigated whether P300-BCI could be used as an alternative
EEG-based BCI modality for communication in ALS population.
They evaluated the eﬀectiveness of a BCI system by detecting
P300 elicited by one of four randomly presented stimuli (i.e.,
YES, NO, PASS, END) and by testing this to both able-bodied
and ALS participants. The participant’s task was to attend one
stimulus (audio, visual, or in both) and reject the others. For
instance, one task was to focus on the target stimulus (i.e.,
YES or NO as deﬁned by the experimenter at the beginning of
each run), while the other task was to focus on the stimulus
(YES or NO) that correctly answered a question provided by
the experimenter. In terms of CA, groups’ performances were
similar, which suggests that a P300-based BCI can be considered
as a powerful and cost-eﬀective, non-muscular communication
tool both for ALS and non-ALS, able-bodied users. However,
the ITR (bits/selection) in this study ranged from 0.43 to 1.80
which is considered rather low compared to other similar, more
recent P300-based BCI studies (Mugler et al., 2010). In addition,
the most severely impaired ALS participants had the worse
CA compared with other participants, which reﬂects also the
incapability of P300 to be an eﬀective communication solution
for more severe impairments.
In this vein, another study (Hoﬀmann et al., 2008) developed
a P300-based BCI system tested on ﬁve people with motor
impairment with separate pathologies and four able-bodied
subjects. The experimental protocol simulated an environment-
control paradigm where images including objects (four electrical
devices a door and a window) were ﬂashed in random sequences.
Four out of the ﬁve disabled participants and two out of the
four healthy subjects achieved 100% oﬄine accuracy. Similarly,
Nijboer et al. (2008) tested severely disabled ALS individuals on
a P300-based BCI system for writing text by using a two-phase
experimental procedure. Initially, the subjects had to copy-spell
a letter and then free-spell letters by using ‘Space’ button on
conclusion/end of a word, ‘Backspace’ button to delete the most
recent character selected, and ‘End’ button to ﬁnish the run. In
copy-spelling sessions, the computer prompts the user with text
to copy character by character within 10 sessions by using a
matrix-spelling task, where 36 squares contain the alphabet and
the numerals 0–9. Then, in Phase II, each subject completed at
least 10 free-spelling sessions (choose characters at will). It was
shown that ERP response remained stable for several months (no
statistical decrease of amplitude or latency of P300 over time).
Moreover, CA improved during free-spelling phase.
In another study (Kübler et al., 2009), 4 ALS participants who
had already been involved in similar studies, operated a 5 × 5
spelling matrix (all letters of the alphabet, except for letter Z)
with auditory feedback. To select one target letter, the participants
had to ﬁrst attend to the number that coded the rows (1–5)
and columns (6–10). This study showed extremely low selection
and CA (4% for selection accuracy and 20% for CA), which
demonstrates that it is exceptionally troublesome for participants
to focus and maintain their attention on the numbers, and that
the “visual support matrix” is ultimately essential. Another study
(Nam et al., 2012) used P300 Speller Paradigm with 7 × 7
matrix of alphanumeric characters, where two types of stimuli
are presented with diﬀerent probability (infrequent target stimuli
and frequent non-target stimuli). People with motor impairment
exhibited lower CA (i.e., 36%) compared to the able-bodied group
(88%). Moreover, the ITR was also lower for the motor disability
group (0.65 bits/min) than the able-bodied group (1.96 bits/min).
A more recent approach (Kaufmann et al., 2013) compared
the “Classic Flashing (CF)” P300-Speller paradigm, in which rows
and columns are highlighted randomly (as in common P300-
Spellers) and the “Face Flashing (FF),” in which characters (letter
and numbers) are overlaid with faces so as to investigate eﬀects
of face familiarity on spelling accuracy. Two motor-impaired
participants were not able to communicate with more than 40%
CA with CF whereas in FF case same participants spelled with
an average accuracy of approximately 82%. These ﬁndings show
Frontiers in Human Neuroscience | www.frontiersin.org
8
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
the beneﬁts of the FF case to such a degree that motor-impaired
participants’ performance did not signiﬁcantly diﬀer from motor-
able participants. On the other hand, low ITR and CA reported
in a study that examined 10 SCI participants with a P300-based
BCI system. In this study, participants had to spell the 5-character
word “SPINE” by using a 36-character matrix (6 × 6 matrix
layout) after 10 min of training (Jeon and Shin, 2015).
A recent study (Scherer et al., 2015) introduced a thought-
based, row-column ﬁltering correspondence board, emulating
user-centered conﬁguration standard for individuals with CP.
More speciﬁcally, the left side of the screen contained the grid,
while on the right side, feedback on the selected item was
presented. Each row (item) was highlighted with a red-color box
for certain time period. In the meantime the selection of a row
(item) was visually reported back to the user by showing an
animation sequence of the row (item) dissolving. Rows (items)
were highlighted for 4 s with a 2-s break between the markers.
It was shown that users became gradually more capable to
communicate by using the proposed system.
Another study evaluated the possibility and usability of an
assistive model operated by a P300-based BCI system in order to
promote communication and environmental control of domestic
appliances and applications to users with ALS (Schettini et al.,
2015). Their results of the three experimental conditions [i.e.,
(i) P300-based BCI Speller, which contained a 6 × 6 matrix with
36 alphanumeric characters; (ii) the AT prototype operated by a
conventional/alternative input device tailored to the speciﬁc end-
user’s residual motor abilities; (iii) the AT prototype operated by
a P300- based BCI] demonstrated that the eﬀectiveness, adequacy
and the end-user’s fulﬁllment did not vary within those three
experimental states. However, the AT P300-based BCI system was
less eﬃcient and longer time was needed for correct selection.
Moreover, in terms of the CA the participants’ performance was
not satisfying.
In this vein, another study (Riccio et al., 2015) evaluated
the impact of a hybrid control of a P300-based BCI technology
(using both EEG and Electromyography) that was developed
to operate an AT software. This study examined both able-
bodied and people with motor impairment to assess eﬀective
communication and interaction with the environment. It was
found that hybrid BCI might enable end-users to take advantage
of some remaining muscular activity, which may not be fully
reliable for properly controlling an AT device. Moreover, McCane
et al. (2015) introduced also a 6 × 6 matrix where the participant
had to “copy-spell” (35 letters) or “text–to–spell.” It is noteworthy
that this study concluded that there is no signiﬁcant correlation
between level of severity and CA.
Finally, a combined approach tested a heterogeneous group of
ALS participants in a study of a P300-BCI with an MI task and
demonstrated for the ﬁrst time that the quality of the control
signals depend on the cognitive function of the participants
and that behavioral dysfunction negatively aﬀects P300 speller
performance (Geronimo et al., 2016).
Web browsers
Another approach refers to BCI systems for Internet access. More
recently a new solution of internet access, the “true web access,”
was proposed by Mugler et al. (2010) where internet surﬁng could
be successfully executed through a P300BCI browser. It was the
ﬁrst study to use real-life scenario for internet access by using
the open-source technology of Mozilla’s Firefox. The browser was
controlled by commands sent from the 6 × 6 P300 Speller system,
while characters in the matrix could be used to select links in the
browser window, to write emails or ﬁll out forms. Their results
showed that participants with ALS achieved a CA of 73% whilst
healthy subjects 90% CA, and ITRs of 8.6 and 14.3, respectively.
However, the positive response and acceptance of this useful tool
was outlined by the ALS participants.
A recent work assessed the eﬀectiveness, eﬃciency and user
satisfaction in two spelling tasks, an email sending and an internet
browsing task (Zickler et al., 2011) by testing a commercial
“AT-software QualiWORLD” (QW) controlled by the P300 BCI
with four end-users and three AT-experts. BCI stimulation was
superimposed on the QW-interface thereby allowing the use of all
functions of QW including an internet browser. The stimulation
of the QW-interface and the web pages was performed by dots
appearing directly next to the icon or link. Performance was high
in all tasks and always above 70% accuracy. More importantly
it was reported that the users were rather satisﬁed with the
eﬀectiveness of the device and did not mention any problems
with the system’s performance.
Paint application
A diﬀerent direction of a P300-BCI system is toward supporting
users to paint (Münßinger et al., 2010). More speciﬁcally,
the “Brain Painting” (color matrix and white-black matrix)
included cells of a 6 × 8 matrix with symbols indicating
color, objects, grid size, object size, transparency, zoom, and
cursor movement. The experiment included three diﬀerent tasks:
spelling a preset sentence (copy-spelling), painting a preset
picture (copy-painting), and painting an individual picture (free-
painting). Despite the low ITR (ALS: 5.8, able-bodied: 8.57),
the CA of both people with motor impairment and able-bodied
was high (ALS: 79%, able-bodied: 92%). Moreover, the patients
found the application extremely useful (Münßinger et al., 2010).
However, this study showed that P300 amplitudes may be aﬀected
by illness severity as has been already mentioned in previous
studies.
In addition, another P300-based BCI system used a “paint”
application, achieving high performance levels (80% accuracy)
in both free painting and copy painting conditions, whereas
ITRs were rather low (4.47–6.65 bits/min) compared to other
P300 applications. In this study it was stressed out that BCI-
based painting is enhanced by using more symbols in the
application interface, such as cursor movement, grid size, object
shape, object size, color, transparency of color, zoom, undo/redo.
The users reported that they were satisﬁed with the BCI Brain
Painting application. In general, P300 Brain Painting application
was eﬀective and the end users with severe motor paralysis
declared that they might utilize the suggested application in
their everyday routine (Zickler et al., 2013). A recent study
(Holz et al., 2015) reported the use of Brain Painting of 6 × 8
matrix including 48 tools for painting combined with a home-
use P300-BCI application. After approximately 2 years of training
Frontiers in Human Neuroscience | www.frontiersin.org
9
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
a high accuracy of 70–90% was accomplished, while, most
importantly, the end-users were highly satisﬁed with the BCI-
Brain Painting system. This study highlighted the potential
of using a BCI application independently by the users while
promoting satisfaction and enjoyment to people with motor
impairment.
Control of external devices
Another communication mode of P300-based systems is to
control external devices. A recent study (Piccione et al., 2006)
developed a BCI system that was tested by two groups of
participants, where they had to select a speciﬁc path for a virtual
object to reach the goal-point by using the P300 activity. They
found diﬀerences between people with motor impairment and
able-bodied regarding the P300 amplitudes, whereas without
any training session both groups achieved quickly a successful
trial and no improvement was found after training. As for the
most impaired participants, their performance was worse than
others, which indicates that P300 is aﬀected when there is great
impairment. On the other hand, it must be stressed out that
the participants’ group was not homogenous since the authors
examined ﬁve paralyzed participants with various impairments.
It is worth noting that this is one of the few studies which have
deployed such a system to people with motor impairment other
than the common diseases (e.g., ALS and stroke). This study
also highlights the fact that correct response without training by
using P300 modulation is feasible as an endogenous response to
a stimulus.
Furthermore, Mauro et al. (2011) compared two interfaces
for controlling the movement of a virtual cursor on a monitor,
and found that online CA was more than 70% both for able-
bodied and ALS participants. Moreover, their results showed
that ALS participants with residual motor abilities were able
to maintain their attention, by controlling the movement of a
virtual cursor on a monitor, similar to the able-bodied ones.
Also, it was stressed that ALS participants could improve their
performance and communication response with a P300-guided
BCI. Another approach evaluated diﬀerent visual P300 BCI
systems with individuals with severe disabilities and their results
revealed that P300-based BCI operation may be aﬀected by the
severity of the disease, whereas long periods of BCI execution
revealed tiredness symptoms and a decrease in performance rates
(Pires et al., 2012).
A recent work on this ﬁeld tested a P300-based BCI system
on participants with diﬀerent motor and cognitive limitations,
aiming at managing eight real domestic devices by means of
113 control commands (Corralejo et al., 2014). Ten out of
15 participants were able to properly execute the suggested
apparatus for precision higher than 75%. Eight of them reached
accuracy above 95%. Moreover, high ITRs, up to 20.1 bit/min
were reached. As in McCane et al. (2015), it was suggested that
the degree of motor impairment and the level of disease severity
is not related to successful operation of a P300-based BCI tool
(Corralejo et al., 2014).
In another study a BCI system decodes the user’s intentions
and
facilitates
navigation,
exploration
and
bidirectional
communication with a robotic system that is remotely controlled
(Escolano et al., 2010). More speciﬁcally, the system is consisted
of a user station (patient environment) and a robot station
(placed anywhere in the world), both remotely located and
through the Internet to promote communication. Although the
ITR was signiﬁcantly low (7 bits/min) the CA was interestingly
high (90–100%).
Rehabilitation and Training Using
EEG-Based BCI
One of the most signiﬁcant and innovative applications for
BCI technology concern rehabilitation systems that aim to
support people with motor impairments to regain the lost
motor control. To address the increasing challenge to deal with
acquired disability, it is imperative that eﬀective rehabilitation
and treatment methodologies being developed for addressing
each stage of after stroke recovery.
Many clinical BCI studies showed evidence for the feasibility
and positive eﬀect of MI-based BCI systems in combination with
physiotherapy and robotic assistive orthotic devices for motor
post–stroke recovery (Pfurtscheller et al., 2000; Grosse-Wentrup
et al., 2011; Kasashima-Shindo et al., 2015; Nicolas-Alonso et al.,
2015; Arvaneh et al., 2016). It is conjectured (Grosse-Wentrup
et al., 2011; Ramos-Murguialday et al., 2013; Kasashima-Shindo
et al., 2015; Nicolas-Alonso et al., 2015; Chaudhary et al., 2016)
that this eﬃcacy of BCI systems on motor rehabilitation is
due to the underling mechanism of synaptic plasticity (Morris,
1999). In particular, the process of synaptic plasticity enables
“the learning of new information and the acquisition of new
skills, while the human brain is able to restore normal brain
function, by aﬀecting motor learning, for instance, by demanding
close attention to a motor task or by requiring the activation
or deactivation of speciﬁc brain signals” (Daly and Wolpaw,
2008). Various recent studies have shed light in the BCI-based
rehabilitation training and motor retraining through real, virtual
(Leeb et al., 2007) and augmented approaches and have managed
to identify the characteristics of a MI- based BCI system for
rehabilitation.
In this vein, it is suggested that there are two ways for
paralyzed people to regain motor abilities by using BCI systems:
(i) train patients to produce more reliable motor brain signals,
and (ii) train patients to activate a device that assists movement
by improving the motor function (Remsik et al., 2016). Even
though people with acquired motor impairment often exhibit
damaged cortex or disrupted motor connection integrity, (EEG)-
based BCI methods are still capable of identifying meaningful
improvement and gradual change. By relying on the capacity
of residual motor neurons to trigger and facilitate appliance
control, BCIs help to train persisting cortical connections to
execute motor output of the motor-impaired limb (e.g., hand). In
general, EEG-BCI has implications for the potential of recovery
while it can be considered as an assistive solution to traditional
physiotherapeutic approaches. The combined approach of BCI
systems together with traditional physiotherapy appears to be
very eﬀective. A recent systematic review has demonstrated the
beneﬁts and the clinical eﬃcacy of BCI systems in motor recovery
of post-stroke patients during stroke rehabilitation process, in
Frontiers in Human Neuroscience | www.frontiersin.org
10
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
combination with traditional physiotherapy and robotic assistive
orthotic devices (Remsik et al., 2016).
In another work, a tetraplegic participant gained control of a
hand orthosis in order to improve his functionality of residual
muscle activity and restore “hand grasp function” of the upper
limb. This was achieved by regulating his SMR through motor
imaging of his foot movement (Pfurtscheller et al., 2000). More
speciﬁcally, MI of the hand movements (right or left) yielded
generally moderate classiﬁcation rates, whereas in the case of
MI of foot movement, the classiﬁcation performance increased
gradually and signiﬁcantly over time. Following the training
procedure the participant was capable for a successful operation
of the orthosis by closing the hand orthosis while imaging
both-feet-movement and by opening the orthosis by imaging
right-hand-movement, nearly error-free with CA close to 100%.
This was achieved mainly by the ability to induce voluntarily
speciﬁc beta oscillations close to the foot area. Since a stable
performance of above 90% correct responses was reached, the
patient started to practically use the orthosis to lift light-weighted
objects.
Another study, evaluated the results of daily BCI training to
beneﬁcial eﬀects of physiotherapy in patients with severe paresis
(Ramos-Murguialday et al., 2013). During BCI−training patients
were instructed to desynchronize SMR by imagining moving
their severely impaired upper limb. Successful SMR control
resulted in concurrent movements of the arm and hand orthoses
in the experimental group, while in the control group participants
received sham feedback, i.e., random movements of the robotic
orthoses (not related with the ipsilesional SMR oscillations).
This was the ﬁrst study to present SMR-BCI intervention as a
rehabilitative approach for a relatively large number (N = 32) of
stroke survivors.
A recent study (Pichiorri et al., 2015) highlighted the
importance of the currently used BCI technology in assisting MI
practice, which notably contributes to improvement of motor
functionality in subacute stroke patients with severe motor
disabilities. More speciﬁcally, they used BCIs which can support
rapid measure of brain activity generated by MI. The BCI-
monitored MI practice as an additional intervention strategy to
common rehabilitation care in 28 subacute stroke patients with
severe motor deﬁcits proved to be successful. The importance of
this study lies in the fact that it was a randomized controlled trial
and the ﬁrst to demonstrate a clinical, pre–post improvement
of the subacute stroke patients with detailed report about the
underlying neurobiology.
Moreover, a recent study suggested to enhance motor recovery
in people who survived a stroke through passive movement (PM)
with a haptic robot and MI (Arvaneh et al., 2016). This approach
included 3 runs of 40 trials each. More speciﬁcally, a cue was
given for 2 s and the command to take action for 4 s, respectively,
while the movement of the chosen hand was performed using
the haptic knob robot (Passive Movement, PM) or Imaging
movement of the paralyzed (left/right) hand (MI). The results
revealed similar CA for both healthy participants and participants
with motor impairment after stroke with hemiparesis. Moreover
better CA of stroke participants (75%) than able-bodied (67.7%)
was observed.
Finally, another study demonstrated the potential application
of a MI task as a mechanism for stroke rehabilitation. They
classiﬁed the participants into three sub-groups based on the
diﬀerent lesion locations in order to perform three diﬀerent
motor tasks (MI, passive motion, and active motion). The
Motor Tasks included active movements, where grasping and
supination movements with the aﬀected hand were performed
and passive movements, where a robotic device performed the
movement. The MI was executed by imaging a movement, but
the participants did not perform the physical movement. They
found diﬀerent β band EEG patterns in each patient group while
two groups showed positive laterality coeﬃcient (LC) values (LC
of the ERD/ERS power of stroke patients is aﬀected by brain
damage) in the active and MI tasks. In these groups, the motor
cortex was not directly damaged, therefore, a level of brain
activation similar to that in able-bodied group was observed (Park
et al., 2016). Thus, motor rehabilitation period diﬀered depending
on lesion location and these changes produced diﬀerent patterns
of neural activation in patients with chronic stroke on diﬀerent
lesion locations.
Tabulated Overview of EEG-Related
Studies
Table 1 lists the reviewed works included in section “EEG-
Based BCI Systems for People with Motor-Impairment” and
summarizes the number of participants, the speciﬁc disease, the
EEG-BCI application, and the EEG-BCI modalities used in each
one of them. The studies are tabulated in chronological order for
each one of the EEG-BCI modalities.
DISCUSSION
The aim of this review is to identify and synthesize ﬁndings on the
grounds of non-invasive EEG-based BCI systems. We presented
published studies which promote communication and control of
appliances for people with motor impairment and approaches
which applied adaptable rehabilitation strategies concerning
the modern restorative physiotherapy. We overviewed evidence
regarding the eﬀective use, modalities and useful applications of
non-invasive EEG-BCI systems from studies including people
with motor impairment. In particular, BCI systems of studies
published the last two decades were reviewed, discussing the
added value of this novel technology and highlighting the
important role of BCIs in life of people with motor impairment.
These studies involved applications of BCI systems in ﬁelds
such as medical and clinical applications, control of wheelchair,
games and entertainment (e.g., painting), communication,
rehabilitation and environmental control.
Diﬀerent control mechanisms have been used to assess the
CA and ITR of the system and the ability of the user to
modulate brain patterns. However, contextual factors that can
inﬂuence the performance in real-life scenarios have not been
discussed thoroughly. The majority of the studies have recruited
participants with adult-onset ALS, while most of them were
at severe level of paralysis such as LIS. In studies focusing on
rehabilitation, the majority of participants were tetraplegic with
Frontiers in Human Neuroscience | www.frontiersin.org
11
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
TABLE 1 | Summary of EEG-BCI studies for communication, control and rehabilitation involving people with motor impairment.
Study
Participants
Disease
EEG-BCI
application
EEG-based
neurophysiological
input
Birbaumer et al., 1999
Two participants
ALS
TTD system
SCP
Birbaumer et al., 2000
Five participants
ALS
TTD system
SCP
Kubler et al., 2001
Two participants
ALS
TTD system
SCP
Hinterberger et al., 2003
One participant
ALS
TTD system
SCP
Neumann and Birbaumer, 2003
Five participants
ALS
TTD system
SCP
Neumann et al., 2003
One participant
ALS
Visual feedback
SCP
Karim et al., 2006
One participant
ALS
Web browsers
SCP
Pfurtscheller et al., 2000
One participant
SCI
Rehabilitation
Motor imagery and
SMR
Neuper et al., 2003
One participant
CP
Graz-BCI
Motor imagery and
SMR
Krausz et al., 2003
Four participants
Paraplegia
Graz-BCI
Motor imagery and
SMR
Wolpaw and McFarland, 2004
Four participants (two people with
motor impairment and two able-bodied)
SCI
Cursor movement
systems
Motor imagery and
SMR
Kübler et al., 2005
Four participants
ALS
Cursor movement
systems
Motor imagery and
SMR
Kauhanen et al., 2007
Six participants
Five SCI, one G-B
Game application
Motor imagery and
SMR
Leeb et al., 2007
One participant
SCI
Virtual
environments
Motor imagery and
SMR
Bai et al., 2008
11 participants (nine able-bodied and
two people with motor impairment)
One Stroke, one ALS
Game application
Motor imagery and
SMR
Cincotti et al., 2008a
Six participants (ﬁve able-bodied and
one people with motor impairment)
SCI
Cursor movement
systems
Motor imagery and
SMR
Cincotti et al., 2008b
28 participants (14 able-bodied 14
people with motor impairment )
Eight with SMA II/III, six
with DMD
Control of external
devices
Motor imagery and
SMR
McFarland et al., 2008
Six participants (four able-bodied two
people with motor impairment)
SCI
Cursor movement
systems
Motor imagery and
SMR
Babiloni et al., 2009
20 participants (14 able-bodied and six
people with motor impairment)
DMD
Control of external
devices
Motor imagery and
SMR
Conradi et al., 2009
Seven people with motor impairment
participants
SCI
Control of external
device
Motor imagery and
SMR
Holz et al., 2013
Four participants
One tetra paresis, one
CP, two cerebral bleeding
Game applications
Motor imagery and
SMR
Ramos-Murguialday et al., 2013
32 participants
Stroke
Rehabilitation
Motor imagery and
SMR
Leeb et al., 2015
29 participants (9 people with motor
impairment participants and 10
able-bodied)
Six SCI, two myopathy,
one DMD
Control of external
devices
Motor imagery and
SMR
Pichiorri et al., 2015
28 participants (14 BCI MI training
group and 14 no-BCI MI training group)
Stroke
Rehabilitation
Motor imagery and
SMR
Geronimo et al., 2016
40 participants (25 people with motor
impairment and 15 able-bodied)
ALS
Control of external
device
Motor imagery, SMR,
and P300
Arvaneh et al., 2016
22 participants (six people with motor
impairment and 16 able-bodied)
Stroke
Rehabilitation
Motor imagery and
SMR
Park et al., 2016
32 participants (20 people with motor
impairment and 12 able-bodied)
Stroke
Rehabilitation
Motor imagery and
SMR
Sellers and Donchin, 2006
Six participants (three able-bodied and
three people with motor impairment)
ALS
Speller systems
P300
Piccione et al., 2006
12 participants (ﬁve people with motor
impairment and seven able-bodied)
ALS, MS, GB, Stroke,
SCI
Control of external
devices
P300
Hoffmann et al., 2008
Nine participants (ﬁve people with
motor impairment and four able-bodied)
CP, MS, ALS, TBI-SCI,
Post-anoxic
encephalopathy
Speller systems
P300
(Continued)
Frontiers in Human Neuroscience | www.frontiersin.org
12
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
TABLE 1 | Continued
Study
Participants
Disease
EEG-BCI
application
EEG-based
neurophysiological
input
Nijboer et al., 2008
Six participants
ALS
Speller systems
P300
Kübler et al., 2009
Four participants
ALS
Speller systems
P300
Kaufmann et al., 2013
25 participants (16 able-bodied and 9
motor-impaired)
Two SMA II, four ALS, two SBMA, one
MD
Speller systems
P300
Escolano et al., 2010
One participant
ALS
Web browsers
P300
Mugler et al., 2010
13 participants (10 able-bodied and 3
people with motor impairment
participants)
ALS
Web browsers
P300
Münßinger et al., 2010
26 participants (20 able-bodied and
three people with motor impairment)
ALS
Paint application
P300
Mauro et al., 2011
Eight participants (four able-bodied and
four people with motor impairment)
ALS
Control of external
devices
P300
Nam et al., 2012
18 participants (nine able-bodied and
nine people with motor impairment)
Three ALS, six CP
Speller systems
P300
Pires et al., 2012
14 participants
Five CP, one DMD, one SCI, seven ALS
Control of external
devices
P300
Zickler et al., 2011
Seven participants (four people with
motor-impairment and 3 AT experts)
One ALS, one SMA III, three DMD
Web browsers
P300
Zickler et al., 2013
Four participants
Two ALS, one stroke, one DMD
Paint application
P300
Corralejo et al., 2014
15 participants
Six Spastic CP, one A-CM, two SCI,
three TBI, one MS, one
Neuroﬁbromatosis and severe
kyphoscoliosis, one Extrapyramidal
syndrome, dystonia and parkinsonism
Control of external
devices
P300
Scherer et al., 2015
14 participants
Dystonic/Spastic CP
Speller systems
P300
Holz et al., 2015
Two participants
ALS
Paint application
P300
Jeon and Shin, 2015
Ten participants
SCI
Speller systems
P300
Schettini et al., 2015
Eight people with motor impairment
participants
ALS
Speller systems
P300
Riccio et al., 2015
11 participants (eight able-bodied and
three people with motor impairment )
Two Stroke, one ALS
Speller systems
P300
McCane et al., 2015
28 participants (14 people with motor
impairment and 14 able-bodied)
ALS
Speller systems
P300
SCI at cervical vertebrae. The most signiﬁcant goals that have
driven BCI research over the last decades have been stressed
within the studies. From the reviewed studies it is evident that
each one of the three EEG-based modalities (i.e., SCP, SMR, and
P300), used in non-invasive BCIs, comprise a promising solution
for EEG-BCI system realization.
Moreover, many studies have successfully addressed the
problem of user’s training duration, which has been essentially
decreased and has led to additional broad BCI systems deployed
in the everyday routine of people with motor impairment, such as
word processing, use of browsers, sending and reading of emails
(Zickler et al., 2011), control of devices, such as wheelchair and
domestic appliances. In Holz et al. (2013) a SMR based BCI
for entertainment purposes, the so-called “Connect-Four,” which
is a strategic game with two competitive players demonstrated
that despite the low eﬀectiveness of participants compared with
similar P300 BCI systems, such entertainment applications are
greatly accepted by the end-users.
Moreover, SMR-based games (Kauhanen et al., 2007; Bai et al.,
2008) indicated that people with motor impairment show reliable
performance and a successful BCI operation. In Kauhanen et al.
(2007) three out of six subjects learned to control a BCI after
training, where a great advantage was that participants received
feedback and could change their strategy in response to the
feedback. In Bai et al. (2008) both patients were able to use
the proposed SMR-BCI game system with high performance as
well. Both studies are highlighting the adaptability of the systems
and the general acceptance of game applications by people
with motor impairment. However, in SMR BCI applications a
main disadvantage is that although ERD/ERS is observed in the
majority of participants, some subjects (even able-bodied) may
have no detectable ERD/ERS components (on the contrary P300
component is always observed). Initially, these BCI approaches
for entertainment were typically not at high priority in the ﬁeld of
BCI research due to the fact that BCI research has mainly focused
on applications to address communication and independency
through assistive technological ways (i.e., spelling devices, control
of external devices). Nevertheless, game oriented solutions seem
to be really promising since they use additional assistive tools
while enhancing participant’s motivation.
Frontiers in Human Neuroscience | www.frontiersin.org
13
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
Despite high performance rates in some reviewed studies there
are various others that showed extremely low performance in
terms of both CA and ITR. Moreover, reported BCI studies
involving both able-bodied individuals and those with severe
disabilities have pointed delays in reaction time, low ITR and
worse CA of people with motor-impairment (Bai et al., 2008;
Escolano et al., 2010; Mugler et al., 2010; Nam et al., 2012; Pires
et al., 2012; Holz et al., 2013; Jeon and Shin, 2015). Moreover, low
ITRs of current BCI systems do not allow for general conclusions
regarding the eﬀective use of BCI on a daily basis. Also, except for
few cases (Vansteensel et al., 2016), the majority of BCI systems
and applications are mainly used in a research environment
(research laboratory etc.) and cannot be successfully utilized in
patients homes for continuous and everyday use, as they need
adaptation and ﬁxation during the operation.
P300 exhibits higher ITRs and does not need training but
is greatly aﬀected by the level of severity of the disease.
Nevertheless, many studies have also shown that even patients in
the LIS can use a P300 BCI for long term periods (Sellers et al.,
2010; Holz et al., 2015). However, in terms of ITR, able-bodied
group reached higher maximum bit rates than disabled subjects
in almost all studies of P300-BCI (Escolano et al., 2010; Mugler
et al., 2010; Mauro et al., 2011; Vaughan et al., 2011; Nam et al.,
2012; Pires et al., 2012). Moreover, in some studies the patients
did not even complete the experimental process (Mauro et al.,
2011). In addition, in most cases the most severely paralyzed
participants seem not to be able to operate successfully the EEG
based BCI system (Pires et al., 2012; Pasqualotto et al., 2015).
These results indicate that (i) P300 may be aﬀected by level
of severity, (ii) participants have worse performance during the
sessions due to a “habitual eﬀect” (Ravden and Polich, 1998, 1999;
Kececi et al., 2006).
The reviewed articles largely focused on individuals with
adult-onset disabilities. It is unclear if the ﬁndings of these studies
could be generalized to individuals with congenital disabilities,
who often have never experienced any terms of communication
or motion. For example, to the best of our knowledge, BCI
systems which use SMR for system operation rely on MI of
upper and lower limbs and have not been tested with individuals
who never experienced voluntary control of their movements
(Moghimi et al., 2013).
Albeit slow, in the majority of the studies SCP speller (namely
the TTD) was around 1 letter per minute and satisﬁed the
requirements for a successful BCI system, (Birbaumer et al., 2000;
Hinterberger et al., 2003). Although the course of the SCP shifts
of participants who used the TTD remained stable over time, a
huge disadvantage of BCIs that demand “self-control” of an EEG
component is that the user must undergo long-term preparation
and extensive training for several weeks so as to gain the level of
CA needed to utilize, e.g., “brain-controlled cursor movement”
for communication (Birbaumer et al., 2000; Hinterberger et al.,
2003).
One limitation of our review is that we do not provide a
comparison of the performances of diﬀerent P300, SMR, and
SCP classiﬁers for healthy and people with motor impairment
and thus do not investigate to what extent this fact plays a key
role in BCI research as other studies and systematic reviews have
already reported (Manyakov et al., 2011; Abdulkader et al., 2015).
Thus, since a classiﬁer comparison has never been performed
on participants, it remains an open question what might be the
best classiﬁer in each case. This is deﬁnitely a critical inquiry
since the brain activation and responses from people with motor
impairment and able-bodied participants might be diﬀerent
(Nam et al., 2012).
Future and on-going studies should try to address the fact
that EEG patterns change based on the user’s learning ability
and multiple adjustments of the classiﬁers can result in better
communication performance. This suggests the development of
parameter estimation processes and the development of adaptive
classiﬁcation frameworks. Thus, a technical expert who will
adjust the BCI system’s parameters is essential to be on-site. The
practical problem is that it is not possible for the ‘BCI-expert,’ to
visit repeatedly the user for training sessions. Also as EEG signals
reﬂect the dynamics of the interaction between the user and the
BCI systems, error-related potentials (Chavarriaga et al., 2014)
may be a useful solution as an auto-correction strategy.
Moreover, a development of a BCI technology that does
not replace but complement existing therapies is a novel and
promising ﬁeld. Studies in stroke patients have shown that, with
a motor relearning intervention, EEG features change in parallel
with improvement in motor function and that sensorimotor
rehabilitation using BCI training and MI may improve motor
function after central nervous system injury. Taking into account
all the above mentioned pieces of evidence, there is a strong
assumption that BCIs can eventually promote the independence
through novel communication techniques and promote motor
rehabilitation of patients with NMD.
CONCLUSION AND FUTURE
PERSPECTIVES
The most recent progress alongside BCI research suggest that
novel and innovative multimodal developments or combined
solutions using EEG- BCI and other assistive technologies
together (e.g., eye-trackers) might be made imminent in the
close future (EU Horizon 2020 project MAMEM, No. 644780:
Multimedia Authoring and Management using your Eyes and
Mind under contract, Coordinator: CERTH, 2015–20182)3.
These accomplishments and the possibility of new BCI systems
have clearly provided with a noteworthy “boost” of BCI
research including a large number of researchers from diﬀerent
disciplines, e.g., neuroscientists, physicians, electrical engineers,
and clinical rehabilitation professionals, among others. Research
interest in the ﬁeld of BCI systems is expected to increase and
BCI design and development and will most probably continue to
bring beneﬁts to the daily lives of people with motor impairment.
In the near future, BCI systems may therefore become a new
mode of human–machine interaction with levels of everyday use
2http://www.mamem.eu/
3MAMEM’s goal is to integrate motor-impaired people back into society by
increasing their potential for communication and exchange in leisure (e.g., social
networks) and non-leisure context (e.g., workplace) by using EEG-based BCI
approach.
Frontiers in Human Neuroscience | www.frontiersin.org
14
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
that are similar to other current interfaces (Corke, 2007; Gajwani
and Chhabria, 2010). Moreover to address the issue of extensive
training for self-regulation of SMR, more enjoyable solutions
such as Virtual Reality or Painting (Holz et al., 2015) could
be used. These approaches re-enable patients to be creatively
active and consequently promote feelings of happiness, self-
esteem and well-being, and promote better QoL. Also, as the goal
of future studies should be the demonstration of a long-term
beneﬁcial impact of BCI technology on functional recovery and
motor rehabilitation, extensive randomized controlled trials are
required.
The development of novel BCIs raises new hopes for the
motor rehabilitation of people with motor impairment (Daly
and Wolpaw, 2008). Therefore, combination of MI to improve
eﬃcacy of physiotherapy in stroke rehabilitation will be a
promising solution. However, the majority of current published
works are basically proof of concept studies with no clinical based
evidence of daily use by people with motor impairment. Thus, the
acceptability and usability of future developed EEG-BCI systems
might be two important issues depending on the size, complexity
of the EEG device and successful operation that should be taken
into consideration in the future. Nevertheless, BCI systems have
already demonstrated their eﬃcacy and reliability. In sum, as was
reported in Wolpaw et al. (2002): “non-muscular communication
and control is no longer merely speculation while at the same
time, the reality does not yet match the fantasy.”
AUTHOR CONTRIBUTIONS
IL wrote, formatted, and submitted the paper. SN wrote,
formatted, and corrected it. PP formatted the paper and made
comments and corrections. IK made comments and corrections
and approved the paper. MT made the ﬁnal correction and
approved the paper.
ACKNOWLEDGMENTS
This work was supported by EU Horizon 2020 Project MAMEM:
Multimedia Authoring and Management using your Eyes and
Mind under contract no. 644780 (http://www.mamem.eu/).
REFERENCES
Abdulkader, S. N., Atia, A., and Mostafa, M.-S. M. (2015). Brain computer
interfacing: applications and challenges. Egypt. Informatics J. 16, 213–230.
doi: 10.1016/j.eij.2015.06.002
Ahn, M., Ahn, S., Hong, J. H., Cho, H., Kim, K., Kim, B. S., et al. (2013). Gamma
band activity associated with BCI performance: simultaneous MEG/EEG study.
Front. Hum. Neurosci. 7:848. doi: 10.3389/fnhum.2013.00848
Ang, K. K., Guan, C., Phua, K. S., Wang, C., Zhao, L., Teo, W. P., et al.
(2015). Facilitating eﬀects of transcranial direct current stimulation on
motor imagery brain–computer interface with robotic feedback for stroke
rehabilitation. Arch. Phys. Med. Rehabil. 96, S79–S87. doi: 10.1016/j.apmr.2014.
08.008
Arvaneh, M., Guan, C., Ang, K. K., Ward, T. E., Chua, K. S. G., Kuah, C. W. K.,
et al. (2016). Facilitating motor imagery-based brain–computer interface for
stroke patients using passive movement. Neural Comput. Appl. 28, 3259–3272.
doi: 10.1007/s00521-016-2234-7
Babiloni, F., Cincotti, F., Marciani, M., Salinari, S., Astolﬁ, L., Aloise, F., et al.
(2009). On the use of brain–computer interfaces outside scientiﬁc laboratories
toward an application in domotic environments. Int. Rev. Neurobiol. 86,
133–146. doi: 10.1016/S0074-7742(09)86010-8
Bach, J. R. (1993). Amyotrophic lateral sclerosis. Communication status and
survival with ventilatory support. Am. J. Phys. Med. Rehabil. 72, 343–349.
doi: 10.1097/00002060-199312000-00002
Bai, O., Lin, P., Vorbach, S., Floeter, M. K., Hattori, N., and Hallett, M.
(2008). A high performance sensorimotor beta rhythm-based brain–computer
interface associated with human natural motor behavior. J. Neural Eng. 5,
24–35. doi: 10.1088/1741-2560/5/1/003
Bai, O., Mari, Z., Vorbach, S., and Hallett, M. (2005). Asymmetric spatiotemporal
patterns of event-related desynchronization preceding voluntary sequential
ﬁnger movements: a high-resolution EEG study. Clin. Neurophysiol. 116,
1213–1221. doi: 10.1016/j.clinph.2005.01.006
Ball, L. J., Nordness, A. S., Fager, S. K., Kersch, K., Mohr, B., Pattee, G. L.,
et al. (2010). Eye-gaze access to AAC technology for people with amyotrophic
lateral sclerosis. J. Med. Speech Lang. Pathol. 18, 11–23. doi: 10.1177/
1545968315575611
Baram, Y., and Miller, A. (2006). Virtual reality cues for improvement of gait in
patients with multiple sclerosis. Neurology 66, 178–181. doi: 10.1212/01.wnl.
0000194255.82542.6b
Baykara, E., Ruf, C. A., Fioravanti, C., Käthner, I., Simon, N., Kleih, S. C., et al.
(2015). Eﬀects of training and motivation on auditory P300 brain–computer
interface performance. Clin. Neurophysiol. 127, 379–387. doi: 10.1016/j.clinph.
2015.04.054
Birbaumer, N., Elbert, T., Canavan, A. G., and Rockstroh, B. (1990). Slow potentials
of the cerebral cortex and behavior. Physiol. Rev. 70, 1–41. doi: 10.1152/physrev.
1990.70.1.1
Birbaumer, N., Ghanayim, N., Hinterberger, T., Iversen, I., Kotchoubey, B.,
Kübler, A., et al. (1999). A spelling device for the paralysed. Nature 398,
297–298. doi: 10.1038/18581
Birbaumer, N., Kübler, A., Ghanayim, N., Hinterberger, T., Perelmouter, J.,
Kaiser, J., et al. (2000). The thought translation device (TTD) for completely
paralyzed patients. IEEE Trans. Rehabil. Eng. 8, 190–193. doi: 10.1109/86.
847812
Bleichner, M. G., Freudenburg, Z. V., Jansma, J. M., Aarnoutse, E. J., Vansteensel,
M. J., and Ramsey, N. F. (2016). Give me a sign: decoding four complex
hand gestures based on high-density ECoG. Brain Struct. Funct. 221, 203–216.
doi: 10.1007/s00429-014-0902-x
Bowsher, K., Civillico, E. F., Coburn, J., Collinger, J., Contreras-Vidal, J. L.,
Denison, T., et al. (2016). Brain–computer interface devices for patients
with paralysis and amputation: a meeting report. J. Neural Eng. 13:23001.
doi: 10.1088/1741-2560/13/2/023001
Calvo, A., Chio, A., Castellina, E., Corno, F., Farinetti, L., Ghiglione, P., et al. (2008).
“Eye tracking impact on quality-of-life of ALS patients,” in Proceedings of the
11th International Conference on Computers Helping People with Special Needs,
Linz, 70–77. doi: 10.1007/978-3-540-70540-6_9
Chaudhary, U., Birbaumer, N., and Ramos-murguialday, A. (2016). Brain–
computer interfaces for communication and rehabilitation. Nat. Rev. Neurol.
12, 513–525. doi: 10.1038/nrneurol.2016.113
Chaudhary, U., Xia, B., Silvoni, S., Cohen, L. G., and Birbaumer, N. (2017). Brain–
computer interface–based communication in the completely locked-in state.
PLOS Biol. 15:e1002593. doi: 10.1371/journal.pbio.1002593
Chavarriaga, R., Sobolewski, A., Millán, J., and del, R. (2014). Errare machinale est:
the use of error-related potentials in brain-machine interfaces. Front. Neurosci.
8:208. doi: 10.3389/fnins.2014.00208
Cincotti, F., Mattia, D., Aloise, F., Bufalari, S., Astolﬁ, L., De Vico Fallani, F.,
et al. (2008a). High-resolution EEG techniques for brain–computer interface
applications. J. Neurosci. Methods 167, 31–42. doi: 10.1016/j.jneumeth.2007.
06.031
Cincotti, F., Mattia, D., Aloise, F., Bufalari, S., Schalk, G., Oriolo, G., et al. (2008b).
Non-invasive brain–computer interface system: towards its application as
assistive technology. Brain Res. Bull. 75, 796–803. doi: 10.1016/j.brainresbull.
2008.01.007
Frontiers in Human Neuroscience | www.frontiersin.org
15
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
Conradi, J., Blankertz, B., Tangermann, M., Kunzmann, V., and Curio, G. (2009).
brain–computer interfacing in tetraplegic patients with high spinal cord injury.
Int. J. Bioelectromagn. 11, 65–68.
Corke, P. (2007). Field and Service Robotics: Springer Tracts in Advanced Robotics.
Berlin: Springer, 129–140.
Corralejo, R., Nicolas-Alonso, L. F., Alvarez, D., and Hornero, R. (2014). A P300-
based brain–computer interface aimed at operating electronic devices at home
for severely disabled people. Med. Biol. Eng. Comput. 52, 861–872. doi: 10.1007/
s11517-014-1191-5
Daly, J. J., Cheng, R., Rogers, J., Litinas, K., Hrovat, K., and Dohring, M. (2009).
Feasibility of a new application of noninvasive Brain Computer Interface (BCI):
a case study of training for recovery of volitional motor control after stroke.
J. Neurol. Phys. Ther. 33, 203–211. doi: 10.1097/NPT.0b013e3181c1fc0b
Daly, J. J., and Wolpaw, J. R. (2008). brain–computer interfaces in neurological
rehabilitation. Lancet Neurol. 7, 1032–1043. doi: 10.1016/S1474-4422(08)
70223-0
Donaghy, C., Thurtell, M. J., Pioro, E. P., Gibson, J. M., and Leigh, R. J. (2010).
Eye movements in amyotrophic lateral sclerosis and its mimics: a review with
illustrative cases. J. Neurol. Neurosurg. Psychiatry 82, 110–116. doi: 10.1136/
jnnp.2010.212407
Donchin, E. (1987). The P300 as a metric for mental workload. Electroencephalogr.
Clin. Neurophysiol. Suppl. 39, 338–343.
Duncan, C. C., Barry, R. J., Connolly, J. F., Fischer, C., Michie, P. T., Naatanen, R.,
et al. (2009). Event-related potentials in clinical research: guidelines for
eliciting, recording, and quantifying mismatch negativity, P300, and N400. Clin.
Neurophysiol. 120, 1883–1908. doi: 10.1016/j.clinph.2009.07.045
Escolano, C., Murguialday, A. R., Matuz, T., Birbaumer, N., and Minguez, J.
(2010). “A telepresence robotic system operated with a P300-based brain–
computer interface: initial tests with ALS patients,” in Proceedings of the 32nd
Annual International Conference of the IEEE Engineering in Medicine and
Biology Society, Buenos Aires, AR, 4476–4480. doi: 10.1109/IEMBS.2010.562
6045
Faller, J., Müller-Putz, G., Schmalstieg, D., and Pfurtscheller, G. (2010). An
application framework for controlling an avatar in a desktop-based virtual
environment via a software SSVEP brain–computer interface. Presence 19,
25–34. doi: 10.1162/pres.19.1.25
Fazel-Rezai, R., Allison, B. Z., Guger, C., Sellers, E. W., Kleih, S. C., and Kübler, A.
(2012). P300 brain computer interface: current challenges and emerging trends.
Front. Neuroeng. 5:14. doi: 10.3389/fneng.2012.00014
Fulk, G. D. (2005). Locomotor training and virtual reality-based balance training
for an individual with multiple sclerosis: a case report. J. Neurol. Phys. Ther. 29,
34–42. doi: 10.1097/01.NPT.0000282260.59078.e4
Gajwani, P. S., and Chhabria, S. A. (2010). Eye motion tracking for wheelchair
control. Int. J. Inf. Technol. Knowl. Manag. 2, 185–187.
Geronimo, A., Simmons, Z., and Schiﬀ, S. J. (2016). Performance predictors
of brain–computer interfaces in patients with amyotrophic lateral sclerosis.
J. Neural Eng. 13:26002. doi: 10.1088/1741-2560/13/2/026002
Gibbons, C., and Beneteau, E. (2010). Functional performance using eye control
and single switch scanning by people With ALS. Perspect. Augment. Altern.
Commun. 19, 64–69. doi: 10.1044/aac19.3.64
Grosse-Wentrup, M., Mattia, D., and Oweiss, K. (2011). Using brain–computer
interfaces to induce neural plasticity and restore function. J. Neural Eng.
8:25004. doi: 10.1088/1741-2560/8/2/025004
Hanselmann, S., Schneiders, M., Weidner, N., and Rupp, R. (2015). Transcranial
magnetic stimulation for individual identiﬁcation of the best electrode position
for a motor imagery-based brain–computer interface. J. Neuroeng. Rehabil.
12:71. doi: 10.1186/s12984-015-0063-z
Hinterberger, T., Kübler, A., Kaiser, J., Neumann, N., and Birbaumer, N. (2003).
A brain–computer interface (BCI) for the locked-in: comparison of diﬀerent
EEG classiﬁcations for the thought translation device. Clin. Neurophysiol. 114,
416–425. doi: 10.1016/S1388-2457(02)00411-X
Hoﬀmann, U., Vesin, J. M., Ebrahimi, T., and Diserens, K. (2008). An eﬃcient
P300-based brain–computer interface for disabled subjects. J. Neurosci.
Methods 167, 115–125. doi: 10.1016/j.jneumeth.2007.03.005
Holz, E. M., Botrel, L., and Kübler, A. (2015). Independent home use of brain
painting improves quality of life of two artists in the locked-in state diagnosed
with amyotrophic lateral sclerosis. Brain Comput. Interfaces 2, 117–134.
doi: 10.1080/2326263X.2015.1100048
Holz, E. M., Höhne, J., Staiger-Sälzer, P., Tangermann, M., and Kübler, A. (2013).
brain–computer interface controlled gaming: evaluation of usability by severely
motor restricted end-users. Artif. Intell. Med. 59, 111–120. doi: 10.1016/j.
artmed.2013.08.001
Hosseini, S. M. H., Pritchard-Berman, M., Sosa, N., Ceja, A., and Kesler, S. R.
(2016). Task-based neurofeedback training: a novel approach toward training
executive functions. Neuroimage 134, 153–159. doi: 10.1016/j.neuroimage.2016.
03.035
Huggins, J. E., Wren, P. A., and Gruis, K. L. (2011). What would brain–
computer interface users want? Opinions and priorities of potential users
with amyotrophic lateral sclerosis. Amyotroph. Lateral Scler. 12, 318–324.
doi: 10.3109/17482968.2011.572978
Jeon, H., and Shin, D. A. (2015). Experimental set up of P300 based brain
computer interface using a bioampliﬁer and BCI2000 system for patients with
spinal cord injury. Korean J. Spine 12, 119–123. doi: 10.14245/kjs.2015.12.
3.119
Jerbi, K., Freyermuth, S., Minotti, L., Kahane, P., Berthoz, A., and Lachaux,
J.-P. (2009). Watching brain TV and playing brain ball exploring novel
BCI strategies using real-time analysis of human intracranial data. Int. Rev.
Neurobiol. 86, 159–168. doi: 10.1016/S0074-7742(09)86012-1
Karat, J., and Vanderdonckt, J. (2009). Human-Computer Interaction Series. Cham:
Springer International Publishing. doi: 10.1007/978-1-84996-272-8
Karim, A. A., Hinterberger, T., Richter, J., Mellinger, J., Neumann, N., Flor, H.,
et al. (2006). Neural internet: web surﬁng with brain potentials for the
completely paralyzed. Neurorehabil. Neural Repair 20, 508–515. doi: 10.1177/
1545968306290661
Kasashima-Shindo, Y., Fujiwara, T., Ushiba, J., Matsushika, Y., Kamatani, D.,
Oto, M., et al. (2015). brain–computer interface training combined with
transcranial direct current stimulation in patients with chronic severe
hemiparesis: proof of concept study. J. Rehabil. Med. 47, 318–324. doi: 10.2340/
16501977-1925
Kaufmann, T., Schulz, S. M., Köblitz, A., Renner, G., Wessig, C., and Kübler, A.
(2013). Face stimuli eﬀectively prevent brain–computer interface ineﬃciency
in patients with neurodegenerative disease. Clin. Neurophysiol. 124, 893–900.
doi: 10.1016/j.clinph.2012.11.006
Kauhanen, L., Jylänki, P., Lehtonen, J., Rantanen, P., Alaranta, H., and Sams, M.
(2007). EEG-based brain–computer interface for tetraplegics. Comput. Intell.
Neurosci. 2007:23864. doi: 10.1155/2007/23864
Kececi, H., Degirmenci, Y., and Atakay, S. (2006). Habituation and dishabituation
of P300. Cogn. Behav. Neurol. 19, 130–134. doi: 10.1097/01.wnn.0000213911.
80019.c1
Klobassa, D. S., Vaughan, T. M., Brunner, P., Schwartz, N. E., Wolpaw, J. R.,
Neuper, C., et al. (2009). Toward a high-throughput auditory P300-based brain–
computer interface. Clin. Neurophysiol. 120, 1252–1261. doi: 10.1016/j.clinph.
2009.04.019
Krausz, G., Scherer, R., Korisek, G., and Pfurtscheller, G. (2003). Critical decision
speed and information transfer in the “Graz-brain computer interface”. Appl.
Psychophysiol. Biofeedback 28, 223–240. doi: 10.1023/A:1024637331493
Kübler,
A.,
and
Birbaumer,
N.
(2008).
Brain–Computer
Interfaces
and
communication
in
paralysis:
extinction
of
goal
directed
thinking
in
completely
paralysed
patients?
Clin.
Neurophysiol.
119,
2658–2666.
doi: 10.1016/j.clinph.2008.06.019
Kübler, A., Furdea, A., Halder, S., Hammer, E. M., Nijboer, F., and Kotchoubey, B.
(2009). A brain–computer interface controlled auditory event-related potential
(p300) spelling system for locked-in patients. Ann. N. Y. Acad. Sci. 1157,
90–100. doi: 10.1111/j.1749-6632.2008.04122.x
Kubler, A., Neumann, N., Kaiser, J., Kotchoubey, B., Hinterberger, T., and
Birbaumer, N. P. (2001). brain–computer communication: self-regulation of
slow cortical potentials for verbal communication. Arch. Phys. Med. Rehabil.
82, 1533–1539. doi: 10.1053/apmr.2001.26621
Kübler, A., Nijboer, F., Mellinger, J., Vaughan, T. M., Pawelzik, H., Schalk, G.,
et al. (2005). Patients with ALS can use sensorimotor rhythms to operate
a brain–computer interface. Neurology 64, 1775–1777. doi: 10.1212/01.WNL.
0000158616.43002.6D
Kubler, A., Winter, S., Ludolph, A. C., Hautzinger, M., and Birbaumer, N.
(2005). Severity of depressive symptoms and quality of life in patients
with amyotrophic lateral sclerosis. Neurorehabil. Neural Repair 19, 182–193.
doi: 10.1177/1545968305276583
Frontiers in Human Neuroscience | www.frontiersin.org
16
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
Lebedev, M. A., and Nicolelis, M. A. L. (2017). Brain-machine interfaces: from basic
science to neuroprostheses and neurorehabilitation. Physiol. Rev. 97, 767–837.
doi: 10.1152/physrev.00027.2016
Leeb, R., Friedman, D., Müller-Putz, G. R., Scherer, R., Slater, M., and
Pfurtscheller, G. (2007). Self-paced (asynchronous) BCI control of a wheelchair
in virtual environments: a case study with a tetraplegic. Comput. Intell. Neurosci.
2007:79642. doi: 10.1155/2007/79642
Leeb, R., Tonin, L., Rohm, M., Carlson, T., and Millan, J. D. R. (2015).
Towards independence: a BCI telepresence robot for people with severe motor
disabilities. Proc. IEEE 103, 969–982. doi: 10.1109/JPROC.2015.2419736
Lesenfants, D., Habbal, D., Lugo, Z., Lebeau, M., Horki, P., Amico, E., et al.
(2014). An independent SSVEP-based brain–computer interface in locked-in
syndrome. J. Neural Eng. 11:35002. doi: 10.1088/1741-2560/11/3/035002
Li, Y., Nam, C. S., Shadden, B. B., and Johnson, S. L. (2010). A P300-based
brain–computer interface: eﬀects of interface type and screen size. Int. J. Hum.
Comput. Interact. 27, 52–68. doi: 10.1080/10447318.2011.535753
Lim, J.-H., Hwang, H.-J., Han, C.-H., Jung, K.-Y., and Im, C.-H. (2013).
Classiﬁcation of binary intentions for individuals with impaired oculomotor
function: “eyes-closed” SSVEP-based brain–computer interface (BCI). J. Neural
Eng. 10:26021. doi: 10.1088/1741-2560/10/2/026021
Liu, Y., Paajanen, T., Zhang, Y., Westman, E., Wahlund, L.-O., Simmons, A., et al.
(2011). Combination analysis of neuropsychological tests and structural MRI
measures in diﬀerentiating AD, MCI and control groups–the AddNeuroMed
study. Neurobiol. Aging 32, 1198–1206. doi: 10.1016/j.neurobiolaging.2009.
07.008
Lozano-Quilis, J. (2013). “Virtual reality system for multiple sclerosis rehabilitation
using KINECT,” in Proceedings of the 7th International Conference on
Pervasive Computing Technologies for Healthcare and Workshops, Venice, 4–7.
doi: 10.4108/icst.pervasivehealth.2013.252208
Lozano-Quilis, J.-A., Gil-Gomez, H., Gil-Gomez, J.-A., Albiol-Perez, S., Palacios-
Navarro, G., Fardoun, H. M., et al. (2014). Virtual rehabilitation for multiple
sclerosis using a Kinect-based system: randomized controlled trial. J. Med.
Internet Res. 16, 1–8. doi: 10.2196/games.2933
Mackenzie, L., Bhuta, P., Rusten, K., Devine, J., Love, A., and Waterson, P. (2016).
Communications technology and motor neuron disease: an Australian survey
of people with motor neuron disease. JMIR Rehabil. Assist. Technol. 3:e2.
doi: 10.2196/rehab.4017
Majaranta, P., and Räihä, K.-J. (2002). “Twenty years of eye typing: systems and
design issues,” in Proceedings of the 2002 Symposium on Eye Tracking Research
& Applications, Vol. 1, New Orleans, LA, 15–22. doi: 10.1145/507072.507076
Manyakov, N. V., Chumerin, N., Combaz, A., and Van Hulle, M. M. (2011).
Comparison of classiﬁcation methods for P300 brain–computer interface on
disabled subjects. Comput. Intell. Neurosci. 2011:519868. doi: 10.1155/2011/
519868
Marchetti, M., Priftis, K., Avenio, G. D., and Superiore, I. (2014). Eﬀectiveness of
the P3-speller in brain–computer interfaces for amyotrophic lateral sclerosis
patients: a systematic review and meta-analysis. Front. Neuroeng. 7:12.
doi: 10.3389/fneng.2014.00012
Mauro, M., Francesco, P., Stefano, S., Luciano, G., and Konstantinos, P. (2011).
“Spatial attention orienting to improve the eﬃcacy of a brain–computer
interface for communication,” in Proceedings of the 9th ACM SIGCHI Italian
Chapter International Conference on Computer-Human Interaction: Facing
Complexity, Alghero, 114–117. doi: 10.1145/2037296.2037325
Mawson, S., Nasr, N., Parker, J., Davies, R., Zheng, H., and Mountain, G. (2016).
A personalized self-management rehabilitation system with an intelligent shoe
for stroke survivors: a realist evaluation. JMIR Rehabil. Assist. Technol. 3:e1.
doi: 10.2196/rehab.5079
McCane, L. M., Heckman, S. M., McFarland, D. J., Townsend, G., Mak, J. N., Sellers,
E. W., et al. (2015). P300-based brain–computer interface (BCI) event-related
potentials (ERPs): people with amyotrophic lateral sclerosis (ALS) vs. age-
matched controls. Clin. Neurophysiol. 126, 2124–2131. doi: 10.1016/j.clinph.
2015.01.013
McFarland, D. J., Krusienski, D. J., Sarnacki, W. A., and Wolpaw, J. R. (2008).
Emulation of computer mouse control with a noninvasive brain–computer
interface. J. Neural Eng. 5, 101–110. doi: 10.1088/1741-2560/5/2/001
McMullen, D. P., Hotson, G., Katyal, K. D., Wester, B. A., Fifer, M. S., McGee,
T. G., et al. (2014). Demonstration of a semi-autonomous hybrid brain-machine
interface using human intracranial EEG, eye tracking, and computer vision to
control a robotic upper limb prosthetic. IEEE Trans. Neural Syst. Rehabil. Eng.
22, 784–796. doi: 10.1109/TNSRE.2013.2294685
Moghimi, S., Kushki, A., Marie Guerguerian, A., and Chau, T. (2013). A review
of EEG-based brain–computer interfaces as access pathways for individuals
with severe disabilities. Assist. Technol. 25, 99–110. doi: 10.1080/10400435.2012.
723298
Morris, R. G. (1999). D.O. Hebb: the organization of behavior, Wiley: New York;
1949. Brain Res. Bull. 50:437. doi: 10.1016/S0361-9230(99)00182-3
Mugler, E. M., Ruf, C. A., Halder, S., Bensch, M., and Kubler, A. (2010). Design
and implementation of a P300-based brain–computer interface for controlling
an internet browser. IEEE Trans. Neural Syst. Rehabil. Eng. 18, 599–609.
doi: 10.1109/TNSRE.2010.2068059
Muller-Putz, G. R., and Pfurtscheller, G. (2008). Control of an electrical prosthesis
with an SSVEP-based BCI. IEEE Trans. Biomed. Eng. 55, 361–364. doi: 10.1109/
TBME.2007.897815
Münßinger, J. I., Halder, S., Kleih, S. C., Furdea, A., Raco, V., Hösle, A., et al.
(2010). Brain painting: ﬁrst evaluation of a new brain–computer interface
application with ALS-patients and healthy volunteers. Front. Neurosci. 4:182.
doi: 10.3389/fnins.2010.00182
Nam, C. S., Woo, J., and Bahn, S. (2012). Severe motor disability aﬀects functional
cortical integration in the context of brain–computer interface (BCI) use.
Ergonomics 55, 581–591. doi: 10.1080/00140139.2011.647095
Neumann, N., and Birbaumer, N. (2003). Predictors of successful self control
during brain–computer communication. J. Neurol. Neurosurg. Psychiatry 74,
1117–1121. doi: 10.1136/jnnp.74.8.1117
Neumann, N., Kuebler, A., Kaiser, J., Hinterberger, T., and Birbaumer, N.
(2003). Conscious perception of brain states: mental strategies for brain–
computer communication. Neuropsychologia 41, 1028–1036. doi: 10.1016/
S0028-3932(02)00298-1
Neuper, C., Müller, G. R., Kübler, A., Birbaumer, N., and Pfurtscheller, G. (2003).
Clinical application of an EEG-based brain–computer interface: a case study
in a patient with severe motor impairment. Clin. Neurophysiol. 114, 399–409.
doi: 10.1016/S1388-2457(02)00387-5
Nicolas-Alonso, L. F., Corralejo, R., Gomez-Pilar, J., Alvarez, D., Hornero, R.,
King, C. E., et al. (2015). The feasibility of a brain–computer interface
functional electrical stimulation system for the restoration of overground
walking after paraplegia. J. Neuroeng. Rehabil. 12:80. doi: 10.1186/s12984-015-
0068-7
Nicolas-Alonso, L. F., and Gomez-Gil, J. (2012). Brain computer interfaces, a
review. Sensors 12, 1211–1279. doi: 10.3390/s120201211
Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., et al.
(2008). A P300-based brain–computer interface for people with amyotrophic
lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916. doi: 10.1016/j.clinph.2008.
03.034
Ono, T., Tomita, Y., Inose, M., Ota, T., Kimura, A., Liu, M., et al. (2014).
Multimodal sensory feedback associated with motor attempts alters BOLD
responses to paralyzed hand movement in chronic stroke patients. Brain
Topogr. 28, 340–351. doi: 10.1007/s10548-014-0382-6
Ordikhani-Seyedlar, M., Lebedev, M. A., Sorensen, H. B. D., and Puthusserypady, S.
(2016). Neurofeedback therapy for enhancing visual attention: state-of-
the-art and challenges. Front. Neurosci. 10:352. doi: 10.3389/fnins.2016.
00352
Park, W., Kwon, G. H., Kim, Y.-H., Lee, J.-H., and Kim, L. (2016). EEG response
varies with lesion location in patients with chronic stroke. J. Neuroeng. Rehabil.
13:21. doi: 10.1186/s12984-016-0120-2
Pasqualotto, E., Matuz, T., Federici, S., Ruf, C. A., Bartl, M., Olivetti
Belardinelli, M., et al. (2015). Usability and workload of access technology
for people with severe motor impairment: a comparison of brain–computer
interfacing and eye tracking. Neurorehabil. Neural Repair 29, 950–957.
doi: 10.1177/1545968315575611
Pfurtscheller, G. (1988). Mapping of event-related desynchronization and type of
derivation. Electroencephalogr. Clin. Neurophysiol. 70, 190–193. doi: 10.1016/
0013-4694(88)90119-8
Pfurtscheller, G., Guger, C., Müller, G., Krausz, G., and Neuper, C. (2000). Brain
oscillations control hand orthosis in a tetraplegic. Neurosci. Lett. 292, 211–214.
doi: 10.1016/S0304-3940(00)01471-3
Pfurtscheller, G., and Neuper, C. (2001). Motor imagery and direct brain- computer
communication. Proc. IEEE 89, 1123–1134. doi: 10.1109/5.939829
Frontiers in Human Neuroscience | www.frontiersin.org
17
January 2018 | Volume 12 | Article 14

Lazarou et al.
Non-invasive EEG-BCI for Motor-Impaired People
Pfurtscheller, G., Zalaudek, K., and Neuper, C. (1998). Event-related beta
synchronization after wrist, ﬁnger and thumb movement. Electroencephalogr.
Clin. Neurophysiol. 109, 154–160. doi: 10.1016/S0924-980X(97)00070-2
Piccione, F., Giorgi, F., Tonin, P., Priftis, K., Giove, S., Silvoni, S., et al. (2006).
P300-based brain computer interface: reliability and performance in healthy
and paralysed participants. Clin. Neurophysiol. 117, 531–537. doi: 10.1016/j.
clinph.2005.07.024
Pichiorri, F., Morone, G., Petti, M., Toppi, J., Pisotta, I., Molinari, M., et al.
(2015). brain–computer interface boosts motor imagery practice during stroke
recovery. Ann. Neurol. 77, 851–865. doi: 10.1002/ana.24390
Pires, G., Nunes, U., and Castelo-Branco, M. (2012). Evaluation of brain–computer
interfaces in accessing computer and other devices by people with severe motor
impairments. Proc. Comput. Sci. 14, 283–292. doi: 10.1016/j.procs.2012.10.032
Ramos-Murguialday, A., Broetz, D., Rea, M., Läer, L., Yilmaz, O., Brasil, F. L., et al.
(2013). Brain-machine-interface in chronic stroke rehabilitation: a controlled
study. Ann. Neurol. 74, 100–108. doi: 10.1002/ana.23879
Ravden, D., and Polich, J. (1998). Habituation of P300 from visual stimuli. Int. J.
Psychophysiol. 30, 359–365. doi: 10.1016/S0167-8760(98)00039-7
Ravden, D., and Polich, J. (1999). On P300 measurement stability: habituation,
intra-trial block variation, and ultradian rhythms. Biol. Psychol. 51, 59–76.
doi: 10.1016/S0301-0511(99)00015-0
Remsik, A., Young, B., Vermilyea, R., Kiekoefer, L., Abrams, J., Evander Elmore, S.,
et al. (2016). A review of the progression and future implications of brain–
computer interface therapies for restoration of distal upper extremity motor
function after stroke. Expert Rev. Med. Devices 13, 445–454. doi: 10.1080/
17434440.2016.1174572
Riccio, A., Holz, E. M., Arico, P., Leotta, F., Aloise, F., Desideri, L., et al. (2015).
Hybrid P300-based brain–computer interface to improve usability for people
with severe motor disability: electromyographic signals for error correction
during a spelling task. Arch. Phys. Med. Rehabil. 96, S54–S61. doi: 10.1016/j.
apmr.2014.05.029
Scherer, R., Billinger, M., Wagner, J., Schwarz, A., Hettich, D. T., Bolinger, E.,
et al. (2015). Thought-based row-column scanning communication board
for individuals with cerebral palsy. Ann. Phys. Rehabil. Med. 58, 14–22.
doi: 10.1016/j.rehab.2014.11.005
Schettini, F., Riccio, A., Simione, L., Liberati, G., Caruso, M., Frasca, V., et al.
(2015). Assistive device with conventional, alternative, and brain–computer
interface inputs to enhance interaction with the environment for people with
amyotrophic lateral sclerosis: a feasibility and usability study. Arch. Phys. Med.
Rehabil. 96, S46–S53. doi: 10.1016/j.apmr.2014.05.027
Sellers, E. W., and Donchin, E. (2006). A P300-based brain–computer interface:
initial tests by ALS patients. Clin. Neurophysiol. 117, 538–548. doi: 10.1016/j.
clinph.2005.06.027
Sellers, E. W., Vaughan, T. M., and Wolpaw, J. R. (2010). A brain–computer
interface for long-term independent home use. Amyotroph. Lateral Scler. 11,
449–455. doi: 10.3109/17482961003777470
Sharma, R., Hicks, S., Berna, C. M., Kennard, C., Talbot, K., and Turner,
M. R. (2011). Oculomotor dysfunction in amyotrophic lateral sclerosis: a
comprehensive review. Arch. Neurol. 68, 857–861. doi: 10.1001/archneurol.
2011.130
Shih, J. J., Krusienski, D. J., and Wolpaw, J. R. (2012). brain–computer interfaces in
medicine. Mayo Clin. Proc. 87, 268–279. doi: 10.1016/j.mayocp.2011.12.008
Valbuena, D., Volosyak, I., and Graser, A. (2010). sBCI: fast detection of steady-
state visual evoked potentials. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2010,
3966–3969. doi: 10.1109/IEMBS.2010.5627990
Vansteensel, M. J., Pels, E. G. M., Bleichner, M. G., Branco, M. P., Denison, T.,
Freudenburg, Z. V., et al. (2016). Fully implanted brain–computer interface in
a locked-in patient with ALS. N. Engl. J. Med. 375, 2060–2066. doi: 10.1056/
NEJMoa1608085
Vaughan, T. M., Wolpaw, J. R., Sellers, E. W., and Marie, S. S. (2011). A novel
P300-based brain–computer interface stimulus presentation paradigm: moving
beyond rows and columns. Clin. Neurophysiol. 121, 1109–1120. doi: 10.1016/j.
clinph.2010.01.030.A
Vidal, J. J. (1973). Toward direct brain–computer communication. Annu.
Rev.
Biophys.
Bioeng.
2,
157–180.
doi:
10.1146/annurev.bb.02.060173.
001105
Wastlund, E., Sponseller, K., Pettersson, O., and Bared, A. (2015). Evaluating gaze-
driven power wheelchair with navigation support for persons with disabilities.
J. Rehabil. Res. Dev. 52, 815–826. doi: 10.1682/JRRD.2014.10.0228
Watanabe, K. (2011). Systems neuroscience and rehabilitation. Neuroscience 3,
117–129. doi: 10.1007/978-4-431-54008-3
Wolpaw, J. R. (2007). brain–computer interfaces as new brain output pathways.
J. Physiol. 579, 613–619. doi: 10.1113/jphysiol.2006.125948
Wolpaw, J. R., Birbaumer, N., Heetderks, W. J., Mcfarland, D. J., Peckham, P. H.,
Schalk, G., et al. (2000). brain–computer interface technology?: a review of the
ﬁrst international meeting. IEEE Trans. Rehabil. Eng. 8, 164–173. doi: 10.1109/
TRE.2000.847807
Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan,
T. M. (2002). brain–computer interfaces for communication and control. Clin.
Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3
Wolpaw, J. R., and McFarland, D. J. (2004). Control of a two-dimensional
movement signal by a noninvasive brain–computer interface in humans.
Proc. Natl. Acad. Sci. U.S.A. 101, 17849–17854. doi: 10.1073/pnas.040350
4101
Wolpaw, J. R., McFarland, D. J., Neat, G. W., and Forneris, C. A. (1991). An EEG-
based brain–computer interface for cursor control. Electroencephalogr. Clin.
Neurophysiol. 78, 252–259. doi: 10.1016/0013-4694(91)90040-B
Zich, C., Debener, S., Kranczioch, C., Bleichner, M. G., Gutberlet, I., and De Vos, M.
(2015). Real-time EEG feedback during simultaneous EEG-fMRI identiﬁes the
cortical signature of motor imagery. Neuroimage 114, 438–447. doi: 10.1016/j.
neuroimage.2015.04.020
Zickler, C., Halder, S., Kleih, S. C., Herbert, C., and Kübler, A. (2013). Brain
painting: usability testing according to the user-centered design in end users
with severe motor paralysis. Artif. Intell. Med. 59, 99–110. doi: 10.1016/j.artmed.
2013.08.003
Zickler, C., Riccio, A., Leotta, F., Hillian-Tress, S., Halder, S., Holz, E., et al. (2011).
A brain–computer interface as input channel for a standard assistive technology
software. Clin. EEG Neurosci. 42, 236–244. doi: 10.1177/155005941104200409
Zimmer, C. A., Devlin, P. M., Werner, J. L., Stamp, C. V., Bellian, K. T., Powell,
D. M., et al. (1991). Adaptive communication systems for patients with
mobility disorders. J. Burn Care Rehabil. 12, 354–360. doi: 10.1097/00004630-
199107000-00014
Conﬂict of Interest Statement: The authors declare that the research was
conducted in the absence of any commercial or ﬁnancial relationships that could
be construed as a potential conﬂict of interest.
Copyright © 2018 Lazarou, Nikolopoulos, Petrantonakis, Kompatsiaris and Tsolaki.
This is an open-access article distributed under the terms of the Creative Commons
Attribution License (CC BY). The use, distribution or reproduction in other forums
is permitted, provided the original author(s) and the copyright owner are credited
and that the original publication in this journal is cited, in accordance with accepted
academic practice. No use, distribution or reproduction is permitted which does not
comply with these terms.
Frontiers in Human Neuroscience | www.frontiersin.org
18
January 2018 | Volume 12 | Article 14
