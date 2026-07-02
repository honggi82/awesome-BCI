#### REVIEW ARTICLE

published: 24 September 2014 doi: 10.3389/fneng.2014.00038

# Challenges in clinical applications of brain computer interfaces in individuals with spinal cord injury

## Rüdiger Rupp*

Experimental Neurorehabilitation, Spinal Cord Injury Center, Heidelberg University Hospital, Heidelberg, Germany

Brain computer interfaces (BCIs) are devices that measure brain activities and translate them into control signals used for a variety of applications. Among them are systems for communication, environmental control, neuroprostheses, exoskeletons, or restorative therapies. Over the last years the technology of BCIs has reached a level of matureness allowing them to be used not only in research experiments supervised by scientists, but also in clinical routine with patients with neurological impairments supervised by clinical personnel or caregivers. However, clinicians and patients face many challenges in the application of BCIs. This particularly applies to high spinal cord injured patients, in whom artiﬁcial ventilation, autonomic dysfunctions, neuropathic pain, or the inability to achieve a sufﬁcient level of control during a short-term training may limit the successful use of a BCI. Additionally, spasmolytic medication and the acute stress reaction with associated episodes of depression may have a negative inﬂuence on the modulation of brain waves and therefore the ability to concentrate over an extended period of time. Although BCIs seem to be a promising assistive technology for individuals with high spinal cord injury systematic investigations are highly needed to obtain realistic estimates of the percentage of users that for any reason may not be able to operate a BCI in a clinical setting.

Edited by: Aleksandra Vuckovic, University of Glasgow, UK

Reviewed by: Christoph Guger, G.Tec Medical Engineering GmbH, Austria Aleksandra Vuckovic, University of Glasgow, UK

*Correspondence: Rüdiger Rupp, Experimental Neurorehabilitation, Spinal Cord Injury Center, Heidelberg University Hospital, Schlierbacher Landstrasse 200a, Heidelberg 69118, Germany e-mail: ruediger.rupp@med.uniheidelberg.de

Keywords: brain computer interface, spinal cord injury, complications, BCI performance, clinical application, neurorehabilitation

## INTRODUCTION

privacy almost completely, which results in a tremendous decrease in quality of life.

In Europe, an estimated number of 330,000 people are living with the consequences of spinal cord injury (SCI), with 11,000 new injuries occurring per year (Ouzký, 2002; van den Berg etal.,

MEDICAL CONSEQUENCES OF SCI IN THE ACUTE PHASE

- 2010). Numbers for the United States are in the same range (National Spinal Cord Injury Statistical Center, 2012). Despite marked regional differences across the globe, there has been a trend toward increasing prevalence rates of SCI over the past decades (Furlan etal., 2013). While the most frequent causes of SCI continue to be trafﬁc, work-related and sporting accidents, in industrial countries there is an ongoing trend toward a higher proportion of non-traumatic lesions (Exner, 2004). As a consequence, the average age of persons at the time of injury is steadily increasing (National Spinal Cord Injury Statistical Center, 2012). Depending on its severity the SCI leads to restrictions up to the complete loss of motor, sensory and autonomic functions below the level of injury. Currently, ∼55% of all individuals with an SCI are tetraplegic due to injuries of the cervical spinal cord with resulting life-long paralysis of the lower and upper extremities. The majority of tetraplegic patients (∼28%) have a neurological levelof lesionatC4andC5atthetimeof dischargefromacutecare to rehabilitation facilities (National Spinal Cord Injury Statistical Center, 2012). In lesions at the level of C5, ﬁnger function is typically impaired, while in most C4 lesions, hand function and elbow ﬂexion are additionally limited. About 8% of the patients have a neurological level rostral to C4 resulting in the loss of motor functions of both upper extremities including shoulder, elbow, and hand movements. These individuals lose their independence and

A SCI results in impairments of motor, sensory and autonomic functions below the lesion. The degree of initial impairment and the potential for neurological recovery is mainly determined by the severity and location of the lesion.

The ﬁrst weeks after the injury patients are in the phase of the spinal shock, i.e., that no tendon tap reﬂexes and ﬂaccid muscle tones are present. The spinal shock typically ends within the ﬁrst 2 weeks after onset of SCI with reappearing tendon reﬂexes and muscle tone. After spinal shock spasms, i.e., involuntarymusclecontractionsthatcannotbesuppressedorcontrolled by the patient, as clinical signs of spasticity slowly show up (Hiersemenzel etal., 2000). Spasticity may result in abnormal joint positions and later in joint contractures in particular if motor neurons of antagonistic muscles have been damaged. An example is a ﬁxed elbow joint in fully ﬂexed position after a C4 lesion with a hyperactive biceps and a completely paralyzed triceps muscle.

A variety of autonomic dysfunctions develop after an SCI including paralysis of the bladder and bowel and orthostatic hypotension due to venous pooling of the blood in the paralyzed legs. In individuals with lesions at or above the level of the fourth thoracic spinal segment additional cardiovascular complications such as low systolic and diastolic blood pressure, bradycardia, and autonomic dysreﬂexia (AD) are present. After spinal shock ends

control, or eye-tracking systems. In very high lesioned patients and particularly those depending on artiﬁcial ventilation the input devices for setup of an electronic user interface are in general very limited and may not work with a sufﬁcient level of performance over an extended period of time. Therefore, over the last decade BCIs have become an interesting option for end users who achieve only a moderate level of control with traditional input devices.

spastic activity may develop in the detrusor muscle restricting the bladder capacity to store urine and resulting in incontinence.

In very high cervical lesions above the level of C3 respiratory problems are present due to impaired voluntary control of the diaphragm. Thisappliesinparticulartopatientsintheacutephase, during which 6.5% of all patients are respirator dependent in the ﬁrst weeks after injury for at least some hours a day (National Spinal Cord Injury Statistical Center, 2012).

## BRAIN COMPUTER INTERFACES

Rehabilitation starts on the ﬁrst day after the injury. After cervical SCI patients are in need of assistive technology for control of devices such as computers, wheelchairs or environmental control systems. The therapeutic regimes applied in this early phase of rehabilitation mainly focus on restoration of impaired motor functions by inducing spinal and supraspinal neuroplasticity.

Brain computer interfaces (BCIs) are technical systems that provide a direct connection between the human brain and a computer (Wolpaw etal., 2002). These systems are able to detect thoughtmodulated changes in electrophysiological brain activity and transform the changes into control signals. A BCI system consists of four sequential components: (1) signal acquisition, (2) feature extraction, (3) feature translation, and (4) classiﬁcation output, which interfaces to an output device. These components are controlled by an operating protocol that deﬁnes the onset and timing of operation, the details of signal processing, the nature of the device commands, and the oversight of performance (Shih etal., 2012).

### PERSISTENT IMPAIRMENTS IN CHRONIC SCI

The highest degree of neurological recovery occurs within the ﬁrst 3 months after injury, while functional recovery is delayed to up to 6–12 months (Curt etal., 2008). People with an initial sensorimotor complete [ASIA Impairment Scale A (Waring etal., 2010)] lesion have the lowest potential for substantial neurological and functional recovery,while initially motor incomplete patients have a high probability to regain a relevant ambulatory function. The bilateral loss of the grasp function in individuals suffering from a cervical SCI severely limits the affected individuals’ ability to live independently and retain gainful employment post injury. Therefore, one of the main priorities of these patients is to improve a missing grasping and reaching function (Anderson, 2004; Snoek etal., 2004; Collinger etal., 2013). If there is sufﬁcient voluntary control of muscles distal to the elbow, surgical procedures such as muscle and tendon transfers, tenodesis and arthrodeses, can be successfully applied for regaining a meaningful grasp function (Hentz and Leclercq,2002; Keith and Peljovich,2012). However, if no voluntary motor functions distal to the elbow joint are present oranindividualisunwillingtoundergosurgerywiththeassociated extended post-surgical rehabilitation period, grasp neuroprostheses on the basis of functional electrical stimulation (FES) may represent a valid alternative for restoring upper extremity function (Rupp and Gerner, 2007). If motor impairments persist, they may lead to negative secondary complications that restrict the successful application of grasp neuroprosthesis. Immobility may lead to a reduction in the passive range of motion of affected joints, which may result in severe contractures with totally immobile joints due to calciﬁed joint capsules. Adequate physical therapy may prevent some of these negative side effects on the musculoskeletal body structures. If no voluntary movements are preserved in the upper extremities no restorative approaches are currently available. To compensate for the loss of motor function and to allow individuals with severe disabilities to participate in society,assistive devices are used enabling environmental control and computer, internet, and social media access. The latter is extremely important for end users with severe motor impairments, because in the virtual world persons with handicaps are on the same level than non-impaired people. Examples for assistive devices used for this purpose are – depending on the residual capabilities of the end user – joysticks for the hand or the chin, suck-and-puff control, voice

### TECHNOLOGY AND BRAIN SIGNALS OF BCI SYSTEMS FOR CLINICAL APPLICATIONS

Although, all implementations of BCIs build upon the same basic components, they differ substantially in regard to complexity of the technology for acquisition of brain signals, their basic mode of operation (cue-based, synchronous vs. asynchronous) and the underlying physiological mechanisms (Birbaumer etal., 2008; Riccio etal., 2012). For application in the clinical environment non-invasive, small scale systems represent the only realistic option. Most of the non-invasive BCI systems rely on brain signals thatarerecordedbyelectrodesonthescalp[electroencephalogram (EEG)]. Another option for practically usable BCIs are systems based on near-infrared spectroscopy (NIRS; Strait and Scheutz, 2014).

Near-infrared spectroscopy uses the fact that the transmission and absorption of near-infrared light in human body tissues contains information about hemoglobin concentration changes. When a speciﬁc area of the brain is activated, the localized blood volume in this area changes rapidly. Optical imaging can measure the location and activity of speciﬁc regions of the brain by continuously monitoring blood hemoglobin levels through the determination of optical absorption coefﬁcients.

In contrast to NIRS, EEG-based BCI systems can function in most environments with relatively inexpensive equipment and therefore offer the possibility of practical use in either the clinical setting or later in end users’ homes. A variety of EEG signals have been used as measures of brain activity: event-related potentials (ERPs; Farwell and Donchin, 1988; Sellers and Donchin, 2006a; Nijboer etal., 2008), frequency oscillations particularly the EEG sensorimotor rhythms (SMRs; Pfurtscheller and Lopes da Silva, 1999; Wolpaw etal., 2000), slow cortical potentials (SCPs; Birbaumer etal., 1999; Neumann etal., 2003), and steadystate responses (SSRs; Cheng etal., 2002). EEG-based BCIs can be categorized into endogenous, asynchronous and exogenous,

synchronous systems. Asynchronous BCIs depend on the users’ ability to voluntary modulate their electrophysiological activity such as the EEG amplitude in a speciﬁc frequency band. In asynchronous BCIs the time point for changes of the control signals is not predeﬁned by the system, but the user is free to initiate decisions at any time. These systems usually require a substantial amount of training. Examples for this class of BCIs are systems based on the detection of SMRs or SCPs. Synchronous BCIs depend on the electrophysiological activity evoked by external stimuli and do not require intensive training. The most common synchronous BCI is based on P300 ERPs. Although systems based on steady-state evoked potentials (SSEPs) such as steady-state visual evoked potentials (SSVEPs) or steady-state somatosensory evokedpotentials(SSSEPs)combinecomponentsof asynchronous and synchronous approaches, the introduction of cues improves their accuracy. Depending on the brain signals used for operation BCIs greatly vary in regard to the minimal and typically used numberof electrodes,trainingtimes,accuracies,andtypicalinformation transfer rates (for overview see Table 1; Birbaumer etal., 2003; Hinterberger etal., 2004; Guger etal., 2012a; Combaz etal.,

(8–12Hz)andbeta(18–26Hz)bandsandcanberecordedoverthe primarysensorimotorareasonthescalp. Theiramplitudetypically decreases during actual movement and similarly during mental rehearsal of movements [motor imagery (MI); Pfurtscheller and Lopes da Silva, 1999; Neuper etal., 2005]. Several studies have shown that people can learn to modulate the SMR amplitude by practicing MIs of simple movements, e.g., hand/foot movements (Kaiser etal., 2014; Toppi etal., 2014). This process occurs in a closed-loop, meaning that the system recognizes the SMR amplitude changes evoked by MI and these changes are instantaneously fed back to the users. This neurofeedback procedure and mutual human–machine adaptation enables BCI users to control their SMR activity and use these modulations to control output devices in an asynchronous manner (Pineda etal., 2003; Cincotti etal., 2008).

For a typical 2-class SMR-BCI different paradigms of MIs such as one hand vs. feet or left vs. right hand are used either in a switchbasedfashionbyintroductionof athresholdorinananalog manner by directly connecting the classiﬁer output to the output device. An often underestimated problem in practical applications of BCIs and in particular of SMR-based BCIs is the detection of a non-intention condition, during which a user does not want to send any command (zero-class). This so called zero-class problem is often handled in brain-switch implementations by deﬁning one MIclassastherestingclassortouselongMIstopauseorreactivate the system (Pfurtscheller etal., 2003; Rohm etal., 2013). However, this approach is not appropriate for all applications,which renders the zero-class problem as one of the major limiting factors for practical use of BCIs.

- 2013).

BCIs based on slow cortical potentials

Slow cortical potentials are slow voltage changes generated on the cerebral cortex, with a duration varying between 300 ms and several seconds. Negative SCPs are typically associated with movement and other functions that imply cortical activity. It has been demonstrated that people are able to self-regulate these potentials and use these modulations for control of assistive devices like a spelling device (Rockstroh etal., 1984). By this, an alternative communication channel was provided to totally paralyzed patients. However, with SCP-based BCIs only a very low information transfer rate of typically less than one letter per 2 min can be achieved (Birbaumer etal., 1999). Additionally, a substantial amount of training, during which patients receive feedback about their EEG-activity, is necessary to achieve a sufﬁcient level of control. Therefore, SCP-based BCIs do not represent the ﬁrst choice for providing individuals with high SCI with a communication or control interface in the acute phase after the injury.

Motor imagery-brain computer interfaces offer further possibilities in the context of neurorehabilitation of spinal cord injured patients that go beyond the traditional use for control of assistive device. After a SCI substantial functional brain reorganization occurs that plays a critical role for functional recovery and may have pathological consequences (Nardone etal., 2013). The basis for a therapeutic use of BCIs is formed by the fact that the central nervous system shows a life-long ability for neural plasticity, which can be enhanced after a trauma or injury by task-speciﬁc training (Dietz and Fouad, 2014). The key elements for an effective neurorehabilitative training based on motor learning are voluntarily triggered movement intentions and a synchronized sensory and proprioceptive feedback of the limbs’ motor actions. BCIs hold promise to enable the detection of

BCIs based on sensorimotor rhythms

Another type of EEG-based BCI exploits the modulation of SMRs. These rhythms are oscillations in the EEG occurring in the alpha

Table 1 |Types of EEG-based BCIs suitable for application in patients in the acute phase after SCI together with their main characteristics.

Parameter BCI

Minimal (typical) number of electrodes

Training time Population with 90–100 (below 80) accuracy without training (%)

Typical rate of decisions/min

SMR (2-class) 4 (10) + 1 reference weeks to months 6 (81) 4 Bits/min SCP 1 (1) + 2 reference weeks to months 33 with accuracy above 70 <1 Bit/min P300 3 (9) + 1 reference minutes to <1 h 73 (11) 10 Bits/min SSVEP 6 + 1 reference minutes to <1 h 87 (4) 12 Bits/min

An overview of the most common practical types of BCIs together with their minimal number of electrodes, a qualitative estimation of typical training times and their typical accuracy and bit rate is provided. A common ground electrode, which is needed for all BCIs, is not explicitly mentioned.

trains with different beat frequencies on the left and right ear (Kim etal., 2011). The frequency of the tone, on which a user is putting attention to, can be registered in the EEG and further used to generateaswitchsignal. Nevertheless,BCIsbasedonvisualevoked potentialsarethepreferredchoiceinindividualswithSCIthathave unimpaired visual function, because the information transfer rate of ASSR-based BCIs is tenfold lower than of SSVEP-based systems (Baek etal., 2013).

intended movements, e.g., the hand, even in high spinal cord injured patients, making them an ideal tool for closed-loop neurorehabilitativetherapieswhenusedincombinationwithgrasping and reaching neuroprosthesis (Jackson and Zimmermann, 2012; Rupp etal., 2013; Savic etal., 2014). Additionally, by practicing feedback-controlled MI of paralyzed limbs the integrity of cortical neuronal connections may be preserved or neurological recovery of motor function may be even enhanced (Kaiser etal.,

The limitations of the placement of electrodes in the posterior region of the skull may be overcome in BCIs based on SSSEPs (Muller-Putz etal., 2006), which record EEG activity over the sensorimotor cortex of the midbrain. In SSSEP-based BCIs tactile stimulators on both hands are used to induce “resonance”-like frequencies in the somatosensory cortex. Users can be trained to modulate these SSSEPs, thereby generating binary control signals. Although they represent an exciting alternative to traditional BCI approaches,SSSEP-based BCIs are in general not applicable in patients with high SCI due to the impairment of sensory functions present in all limbs.

- 2014).

BCIs based on event-related potentials

Event-related potential-based BCIs make use of the fact that speciﬁc neural activity is triggered by and involved in the processing of speciﬁc events. These systems are implemented with an oddball paradigm, wherein a rare target (oddball event) is presented within frequent non-target events. These BCIs usually exploit an endogenous ERP component, known as P300, as input signal. The P300 is a positive deﬂection in the EEG occurring 200–500 ms afterthepresentationof therarevisual,auditoryorsomatosensory stimulus and is a reliable, easy to detect ERP (Sutton etal., 1965). By focusing attention on the rare target, e.g., by keeping a mental count of its occurrence, the P300 amplitude can be increased and therefore its detection and classiﬁcation improves (Kleih etal.,

HYBRID BCIs

A novel development in BCI research is the introduction of the hybrid BCI (hBCI) concept (Müller-Putz etal., 2011). A hBCI consists of a combination of several BCIs or a BCI with other input devices (Allison etal., 2012). These input devices may be based on the registration of biosignals other than brain signals, such as electromyographic activities. Using this approach, a user can generate a single command signal either by fusing different input signals or by simply selecting one of them (Müller-Putz etal.,2011). In the latter case, the input signals can be dynamically routed based on their reliability, i.e., continuously monitoring the quality, and the input channel with the most stable signal will then be selected (Kreilinger etal., 2011). In the case of signal fusion, each of the input signals contributes to the overall command signal with a dedicated weighting factor (Leeb etal., 2011). These factors are generally not static, but can be dynamically adjusted in accordance with their reliability, which is quantiﬁed by appropriate quality measures. The hBCI is fully compliant with the user-centered design concept (ISO, 2010). The key message of this approach is that the technology has to be adapted to the individual users’ ability and needs and not vice versa. Combining BCIs with established user interfaces may allow more end users to control assistive technology or may simplify the use of existing devices. However, this extension of the target population comeswiththedrawbackthatlongerpreparationtimesareneeded for setup of the additional components of the hBCI. From the users’ perspective it is important to carefully evaluate the design of the hBCI’s control scheme and not to cause additional mental workload. Control schemes based on a sequential control task of the different input signals are – at least at the beginning of the training – superior to those, for which a user must control different input signals simultaneously. With practice users might learn to perform multiple tasks, thereby making full use of the hBCI approach.

- 2011). In individuals with SCI eye-gaze is preserved and thus a visual rather than an auditory oddball paradigm is the preferred choice, because the information transfer rate and accuracy is substantially higher and perceived workload much lower in visual P300-based BCIs (Furdea etal., 2009; Halder etal., 2010; Kathner etal., 2013). The big advantage of P300 compared to SMR-based BCIsisthattheycanbeoperatedwithalmostnosetuptimein99% of the general population (Guger etal., 2009b). Although, P300BCIs basically work without electrodes on the occipital cortex, their performance can be improved, if electrodes on the posterior head region are used (Krusienski etal.,2008). Special care must be taken that these electrodes do not cause any discomfort in acute patients with high SCI lying in bed and resting their heads on a pillow or using a head-rest.

BCIs based on steady-state evoked potentials

Steady-state evoked potentials are stable oscillations that can be elicited by rapid repetitive (usually > 6 Hz) visual, auditory, and somatosensory stimuli. The most common type of SSEP-based BCI are the SSVEP-based BCIs, where screen objects ﬂickering at different frequencies are visually presented to subjects. Focusing their attention to the intended stimulus elicits enhanced SSVEP responses at the corresponding frequency, which can be detected, classiﬁed and translated into control commands (Vialatte etal., 2010). SSVEP-based BCIs have the advantages of a high information transfer rate, practically no training time, and they work in almost every user (Allison etal., 2010; Guger etal., 2012a). SSVEPs are recorded over occipital brain areas and the same caution has to be taken like in some P300-based systems to avoid any discomfort caused by electrodes on the back of the head.

In any case, the hBCI concept helps to overcome limitations inherent to a singular BCI system, e.g., false-positive, unintended decisions or the zero-class problem. In fact the second input

A relatively new approach in BCI is the use of auditory steadystate responses (ASSR), where the user can modulate the ASSR by selective attention to a speciﬁc sound source such as tone burst

that are highlighted in other rows or columns (non-target letters). Each time the target letter is highlighted, a P300 signal occurs in the frontoparietal brain region. Each target letter can be identiﬁed by a classiﬁer, which detects the occurrence a P300 signal every time the row and column of the intended letter is highlighted and selects the letter accordingly. In a recent study a new paradigm was recently introduced for enhancement of the P300 control (Kaufmann etal., 2013), in which a famous face – in this case the face of Albert Einstein is superimposed – on top of the matrix display. By the implementation of this paradigm persons formerly unable to control a traditional P300-based speller were enabled to successfully use this kind of communication interface.

signal can be effectively used to indicate an “idling” state or to introduce a context-speciﬁc correction mechanism. An example for demonstration of the superiority of this approach is an hBCI-controlled telepresence robot, where the user navigates to the left and right by imagination of movements of the left and right hand and stops/starts the movements of the robot by an electromyographic switch activated by a short muscle twitch (Carlson etal., 2013). In an hBCI controlled communication application based on two BCIs (P300 and SSVEP) SSVEP activity is used to assess whether the subject is focused on a spelling task. If no SSVEP activity is found, then the system assumes that the user is not paying attention to the spelling system and does not output any characters (Panicker etal., 2011). Another example is an hBCI-controlled reaching and grasping neuroprosthesis, in which the hBCI consists of an SMR-BCI combined with an analog shoulder joystick (Rohm etal., 2013). The neuroprosthesis is activated/deactivated by a long MI detected by an SMR-BCI and the degree of hand closing/elbow ﬂexion is controlled by shoulder movements. To prevent an unintended deactivation of the system several context-speciﬁc plausibility checks were implemented in the control concept, e.g., deactivation is not allowed, if the hand is closed or if the shoulder is moved. In another example of an hBCIcontrolled computer interface based on an SMR-BCI and a mouth mouse, a brain-switch simulating a double-click can only be generated while the mouse cursor is not moving (Faller etal., 2012). This comprehensive list of examples shows that the hBCI concept is a valuable extension of traditional BCI approaches and represents a big step forward toward the regular use of BCIs as assistive devices.

An alternative to P300 based spellers are SMR-based spelling systems such as the Hex-o-Spell paradigm (Blankertz etal., 2006). In the Hex-o-Spell paradigm hexagons ﬁlled with groups of letters or a single letter are arranged in a circular fashion with a pointing arrow in the center of the circle. The circle can be rotated by one type of MI,e.g.,right hand movements,and extended for selection with another MI, e.g., foot movements.

Although, the traditional matrix-based P300-based spellers are the most widespread type of BCIs used for communication purposes, alternative BCIs using different designs and signal modalities such as SSVEPs are developed to build a faster, more accurate, less mentally demanding, and more satisfying BCI (Combaz etal., 2013). Such systems are not only beneﬁcial in end users in a locked-in state, but may also enable basic communication in individuals with very high SCI, who are ventilator dependent. However, this needs to be proven in future clinical studies.

APPLICATION OF BCIs IN END USERS WITH MOTOR IMPAIRMENTS

BCIs for wheelchair and environmental control

Most of the results in BCI research have been obtained involving healthy subjects, in particular students working in research labs due to their easy availability and intrinsic motivation to participate in experiments designed and set up by their own (Moghimi etal., 2013). Only a low percentage (estimated <5%) of BCI studies involved end users with a real need for a BCI, most of them end users with amyotrophic lateral sclerosis (ALS) in the socalled locked-in-state with no motor functions preserved except eye movements (Pasqualotto etal., 2012). All BCI research in end userswithSCIwascarriedoutsofarwithindividualsinthechronic stage. Thismeans,thattheywereparticipatinginstudiesattheearliest 1 year after the onset of the injury in a stable neurological, psychological, and social state.

Being mobile is beside communication and manipulation an essential need of motor impaired end users. Wheelchairs represent a very important assistive device to enable mobility in individuals with SCI. Persons with severe motor disabilities are dependant on electrical wheelchairs controlled by hand- or chinoperated manual joysticks. If not enough residual movements are present, eye-gaze or suck-and-puff control units may serve as a wheelchair user interface. Suck-and-puff control is mainly based on four types of commands. If air is blown into/sucks from the device with high pressure/vacuum, the controller interprets this as a forward/backward drive signal. If a low pressure or vacuum is applied, the wheelchair drives right or left. With this rather simple control scheme users are able to perform most navigation tasks with their wheelchair. Though the thresholds for low/high pressure are individually calibrated, the end user must be able to reliably generate two different levels of air pressure/vacuum over a sustained period of time to achieve a good level of control. Since these prerequisites are not present in all very high lesioned spinal cord injured people, BCIs may represent an alternative control option.

BCIs for communication

Nowadays, researchers mostly work with the P300 signal for communication purposes. Numerous clinical studies conﬁrm the efﬁcacy of the P300-BCI in paralyzed patients with four choice responses, e.g., “Yes/No/Pass/End” (Sellers and Donchin, 2006b) or “Up/Down/Left/Right” for cursor movement (Piccione etal., 2006; Silvoni etal.,2009). With P300-spellers words could be composed letter by letter, which are arranged in a matrix fashion in rows and columns. One letter is selected by implementation of an oddball paradigm, in which rows and columns are highlighted randomly while the user focuses on one speciﬁc letter (target letter) she or he wishes to spell and tries to ignore all other letters

At the current state of the art all types of non-invasive BCIs are providing only a limited command rate and are insufﬁcient for dexterous control of complex applications. Thus, before the successful application of control interfaces with low command rates – including BCIs – in mobility devices intelligent control

mobilizationmaybedifﬁcultandotherwaystoprovidesomeform of independence and social inclusion need to be found. Access to computers in general and to the internet and social media in particular is an important goal for patients to communicate with their relatives and friends. For this purpose, P300-based BCIs may offer a quick way to setup an interface for assessing traditional social media like Twitter or moving avatars in virtual reality environments like Second Life (Fazel-Rezai etal., 2012). However, the preliminary results obtained in experiments with nonmotor impaired persons need to be conﬁrmed in paralyzed end users.

schemes have to be implemented. Ideally, the user only has to issue basic navigation commands such as left, right and forward, whichareinterpretedbythewheelchaircontrollerintegratingcontextual information obtained from environmental sensors. Based on these interpretations the wheelchair would perform intelligent maneuvers including obstacle avoidance and guided turnings. In conclusion,insuchacontrolschemetheresponsibilitiesareshared between the user, who gives high-level commands, and the system, which executes low-level interactions with more or less degree of autonomy. With this so called shared control principle researchers have demonstrated the feasibility of mentally controlling complex mobility devices by non-invasive BCIs, despite its slow information transfer rate (Flemisch etal.,2003;Vanhooydonck etal.,2003; Carlson and Demiris, 2008).

Another important issue is to allow severely paralyzed patients to control their environment independently, to which BCIscontrolled environment control systems may contribute significantly. First results in end users with handicaps show that environmental control by an asynchronous P300 BCI is possible. However, system testing also revealed that the minimum number of stimulation sequences needed for correct classiﬁcation had a higher intra-subject variability in end users with respect to what was previously observed in young, non-disabled controls (Aloise etal., 2011). Also special focus must be put on the design of the visual control interface to achieve high accuracy while keeping mental effort low (Carabalona etal., 2012). A major progress can be expected in respect to the availability of enhanced BCI-controlled computer and social media access and environmental control from the European projects BrainAble and BackHome.

Although asynchronous, spontaneous BCIs like SMR-based BCIs seem to be the most natural control option for wheelchairs, there are a few applications using synchronous BCIs (Iturrate etal., 2009; Rebsamen etal., 2010). Like in most communication applications these BCIs are based on the detection of the P300 potential evoked by concentrating on a ﬂashing symbol in a matrix. For wheelchair control the system ﬂashes a choice of predeﬁned target destinations several times in a random order and ﬁnally the stimulus that elicits the largest P300 is selected as the target. Afterward the intelligent wheelchair drives to the selected target autonomously. Once there it stops and the subject can select another destination. The fact that the selection of a target takes ∼10 s and that the user intent is only determined at predeﬁned time points takes the usability of cue-based BCIs for control of mobility devices into question.

BCIs for control of upper extremity neuroprosthesis

InBCI-controlledmobilitydevicesdevelopedintheframework of recent European projects MAIA and TOBI the users’ mental intent was estimated asynchronously and the control system provided appropriate assistance for wheelchair navigation. With this approach the driving performance of the BCI controlled device greatlyimprovedintermsof continuoushuman–machineinteractionandenhancedpracticability(Vanackeretal.,2007;Galánetal., 2008; Millán etal., 2009; Tonin etal., 2010). In the most recent approach of shared control the user asynchronously sends – with the help of a MI based BCI – high-level commands for turning left or right to reach the desired destination. Short-term lowlevel interaction for obstacle avoidance is done by the mobility device autonomously. In the applied shared control paradigm the wheelchair pro-actively slows down and turns for avoidance of obstacles as it approaches them. For provision of the latter functionality the wheelchair is equipped with proximity sensors and two webcams for obstacle detection (Borenstein and Koren, 1991; Carlson and Millán, 2013). Cheap webcams were used instead of an expensive laser range-ﬁnder to provide an affordable solution, in which the additional equipment for implementation of the shared control does not cost more than the wheelchair itself.

Today, the only possibility of restoring permanently restricted or lost functions to a certain extend in case of missing surgical options (Hentz and Leclercq, 2002) is the application of FES. Over the last 20 years FES systems with different level of complexity were developed and some of them introduced into the clinical environment (Popovic etal., 2002). These systems delivershortcurrentimpulseselicitingphysiologicalactionpotentials on the efferent nerves, which cause contractions of the innervated, yet paralyzed muscles of the hand and the forearm (van den Honert and Mortimer, 1979). On this basis FES artiﬁcially compensates for the loss of voluntary muscle control.

When using the FES in a compensatory setup at a very early stageof primaryrehabilitationtheeasiestwayof improvingaweak or lost grasp function is the application of multiple surface electrodes. With only seven surface electrodes placed on the forearm two grasp patterns, namely lateral grasp and palmar grasp, can be restored (Rupp etal., 2012). With the combination of surface electrodes and a ﬁnger synchronizing orthosis the difﬁculties with dailyreproductionof movementsandhugevariationsof grasppatterns depending on wrist rotation angle may be overcome (Leeb etal., 2010).

Through the last decade it has become obvious that the user interface of all current FES devices is not optimal in the sense of natural control, relying on either the movement or the underlying muscle activation from a non-paralyzed body part to control the coordinatedelectricalstimulationof musclesintheparalyzedlimb (Kilgore etal., 2008; Moss etal., 2011). In the case of individuals with a high,complete SCI and the associated severe disabilities not

Although a lot of literature is available on the technical speciﬁcationsof BCI-controlledwheelchairs,onlyafewstudiesinvolving endusersareavailable(Nguyenetal.,2013)andevenlessinvolving end users in real need of a BCI.

Intheearlyphaseof rehabilitationpatientswithacervicalspinal injury may not be cardiovascular stable. Therefore, wheelchair

CLINICAL APPLICATIONS OF BCIs

enough residual functions are preserved for control. This has been a major limitation in the development of a reaching neuroprostheses for individuals with a loss not only of hand and ﬁnger but also of elbow and shoulder function.

In the clinical setting the main focuses of BCIs in patients with an acute or subacute SCI in the ﬁrst months after injury are (1) the compensation of a temporarily or permanently impaired motor function, preferably if simpler techniques do not allow for a sufﬁcient control of assistive devices, and (2) the maintenance of cortical connectivity for avoidance of maladaptive plasticity with symptoms like neuropathic pain and enhancement of functional recovery by induction of beneﬁcial neuroplasticity (Grosse-Wentrup etal.,2011). Almost all patients with substantial motor impairments are potential candidates for neurofeedback, i.e., receiving feedback on neural cortical states, and neurorehabilitative therapies, e.g., BCI-controlled FES (Birbaumer etal., 2009). Unfortunately, the empirical evidence for a positive impact of BCI technology for therapeutic purposes is scarce and clinical studies are urgently needed to provide evidence for their added value.

Several BCI approaches mainly based on SSVEPs have been introducedasasubstitutefortraditionalcontrolinterfacesforcontrol of an abdominal FES system (Gollee etal., 2010), a wrist and hand orthosis (Ortner etal., 2011) or a hand and elbow prosthesis (Horki etal., 2010).

Apart from those simple approaches, BCIs have enormous implications providing natural control of a grasping and reaching neuroprosthesis control in particular in individuals with a high SCI by relying on volitional signals recorded from the brain directly involved in upper extremity movements.

In Pfurtscheller etal. (2003) a pioneering work showed for the ﬁrst time that a MI-BCI control of a neuroprosthesis based on surface electrodes is feasible. In this single case study the restoration of a lateral grasp was achieved in a tetraplegic subject, who suffers from a chronic SCI with completely missing hand and ﬁnger function. Theenduserwasabletomovethroughapredeﬁnedsequence of grasp phases by imagination of foot movements detected by a brain-switch with 100% accuracy. He reached this performance level already prior to the experiment by some months of training with the MI-BCI (Pfurtscheller etal., 2003) and has maintained it for almost a decade by regular continuation of the training (Enzinger etal., 2008).

For compensation of motor impairments the preferred target population is the group of high lesioned, tetraplegic patients with severe motor impairments in particular of the upper extremities, who may be temporarily ventilator dependent and have limited ability to speak due to the use of a tracheal tube. Most of the BCI research related to communication and control in end users with disabilities has been carried out with individuals in the chronic stage meaning that most of the people returned to their homes, wereinastableneurologicalandpsychologicalconditionandtheir familymembersorcaregiverswereproperlyinstructedtocorrectly setup and operate a BCI. In contrast to this the condition of the patients and the environment is very different in the clinical setting, which presumably affect the users’ (end users and caregiver) priorities (Huggins etal., 2011).

A second feasibility experiment has been performed, in which a short-term BCI-training has been applied in another individual with tetraplegia. This subject was using a Freehand system for several years. After 3 days of training the end user was able to control the grasp sequence of the implanted neuroprosthesis with a moderate, but sufﬁcient performance (Müller-Putz etal., 2005).

The aim of the following chapter is to provide an overview of factors that may limit the successful implementation of BCIs for controlof assistivedevicesorforneurorehabilitationintheclinical setting.

In these ﬁrst attempts the BCI was rather used as a substitute for the traditional neuroprosthesis control interface than as an extension. With the introduction of FES-hybrid orthoses it becomes more important to increase the number of independent control signals. With the recent implementation of the hBCI framework it became feasible to use a combination of input signals rather than BCI alone. In a ﬁrst single case study a combination of a MI-BCI and an analog shoulder position sensor is proposed (Rohm etal., 2013). By upward/downward movements of the shoulder the user can control the degree of elbow ﬂexion/extension or of hand opening/closing. The routing of the analog signal from the shoulder position sensor to the control of the elbow or the hand and the access to a pause state is determined by a digital signal provided by the MI-BCI. With a short imagination of a hand movement the user switches from hand to elbow control or vice versa. A longer activation leads to a pause state with stimulation turned off or reactivates the system from the pause state. With this setup a highly paralyzed end user, who had no preserved voluntary elbow, hand and ﬁnger movements, was able to perform several activities of daily living, among them eating a pretzel-stick, signing a document and eating an ice cone, which he was not able to perform without the neuroprosthesis.

## FACTORS LIMITING THE CLINICAL APPLICATION OF BCIs

A couple of aspects have prevented BCIs so far from being regularly used as a user interface for control of assistive devices or as an adjunct therapeutic tool in the clinical setting of the rehabilitation of acute spinal cord injured patients. These limiting factors are mainly related to three distinct domains: (1) Problems and limitations of the available technology for signal acquisition and processing,(2)user-speciﬁcfactorssuchasmedicationorpersonal user characteristics, and (3) infrastructure and health-care related constraints (Figure 1).

### HARDWARE AND TECHNOLOGY RELATED FACTORS

Today, commercial BCI systems are mainly based on gel electrodes placed inside an EEG cap. The correct montage of the cap and the electrode on the skull under the premise of a proper electrode contact are very time-consuming procedures taking in the case of eight electrodes an experienced therapist up to 15–20 min. With the use of more expensive active electrodes, which integrate the ampliﬁer in the electrode, the montage time can be substantially reduced. However, if electrode gel is used, the hair of the end user needs to be washed afterward. This puts additional burden

|[Figure 1]<br><br>FIGURE 1 | Overview of factors limiting the successful use of different clinical BCI applications.The “long and winding road” of clinical applications of BCI.The height of each barrier encodes its priority.|
|---|

interactions leading to an increase in cortical inefﬁciency (Roland etal., 2011). Although, no studies exist that quantify the impact of these cortical changes on the BCI performance, it can be assumed that general cognitive problems of the older population such as attention and concentration deﬁcits might negatively inﬂuence the ability to control or to learn how to operate a BCI.

on the caregivers and the patient. Therefore, a substantial effort needs to be taken to improve the practical applicability of BCIs in clinical routine. This is related in particular to the availability of dry electrodes, which can be quickly mounted and adapted to the individual needs of a patient. Although the ﬁrst technical implementations of dry or at least “one drop,” gel-less electrodes were introduced recently, it needs to be shown that they achieve the same level of signal acquisition quality in particular in an electrically noisy environment and that they do not cause any discomfort to the user (Grozea etal., 2011; Zander etal., 2011; Guger etal., 2012b).

Respiratory problems in high SCI

Particular in patients with high cervical lesions above C4 respiratory problems are present due to the dysfunctions of the voluntary innervation of the diaphragm and/or a thorax trauma. In the acute setting 6.5% of all patients are respirators dependent at least for some hours a day (National Spinal Cord Injury Statistical Center, 2012). 3.5% of the total population have permanent dysfunction of the respiratory function and need artiﬁcial ventilation (National Spinal Cord Injury Statistical Center, 2012). These patients are in a real need for a BCI, since other control options might not work satisfactorily. However, electrical artifacts generated by the artiﬁcial ventilator or muscular artifacts caused by shoulder elevation for voluntary ventilation support substantially decrease the quality of the EEG signals and might make a successful use of a BCI impossible.

Formosteffectiveuseof timeandpersonalresources,thenecessary action of the therapist should be limited to turning the system on and off. Efforts toward this goal have recently started by implementation of a “push-button” user interface without the need for technical experts to setup and calibrate the BCI system manually (Kaufmann etal., 2012). Further improvements in terms of a higher reliability can be expected from machine learning research in BCIs, as e.g., the transfer of classiﬁers between individuals bears the chance to circumvent the time-consuming calibration recordings for novel users (Fazli etal., 2009), and novel algorithmic counter-measures have recently been published to adaptively cope with the non-stationarity omnipresent in brain signals (Sannelli etal., 2011; Kindermans etal., 2012; Samek etal., 2012).

Spasmolytic medication

MEDICAL AND PERSONAL USER-RELATED FACTORS

After the period of a spinal shock spasticity evolves in the muscles in the areas of the body below the level of lesion. This inhibition of reﬂexes is not only apparent in skeletal muscles, but also in the detrusor muscle of the bladder resulting in episodes of incontinence. The standard medications for treatment of an overactive bladder in the ﬁrst months after the SCI are anticholinergics that inhibit the receptors for acetylcholine and thereby reducing detrusor muscle tone. It has been shown that anticholinergic effects in the central nervous system can

Personal factors

During the last decade in industrial countries the mean age at the onsetof SCIincreasedsigniﬁcantlyfrom 28.7 yearsbetween1973– 1979 to 42.6 years in 2010–2012 with an ongoing trend toward more patients above the age of 65 (National Spinal Cord Injury Statistical Center, 2012). There is some evidence that the spatiotemporal brain activation patterns alter during aging and that the aging process appears to more substantively alter thalamocortical

the successful use of a BCI-controlled neuroprosthesis either for therapeutic as well as for compensatory purposes.

have negative inﬂuence on vigilance and concentration. While the intake of Oxybutynin leads to signiﬁcant lower spectral power in all relevant frequency bands in the EEG, this effect can be avoided with Tolterodin, Trospiumchlorid, or Darifenacin (Pietzko etal., 1994; Todorova etal., 2001; Kay and Ebinger,

Acute stress reaction and episodes of depression after SCI

It is a well-known fact that motivational and emotional states have an inﬂuence on the BCI performance of individuals with and without motor impairments independent of the type of BCI used (SMR or P300; Kleih etal., 2010; Nijboer etal., 2010; Hammer etal., 2012). Although, there is nothing predictable about the psychological sequelae after SCI and the response is highly individual and is mediated by both pre-morbid individual characteristics and external factors, several psychological effects occur that might heavily interfere with the successful application of a BCI (North, 1999).

- 2008). Therefore, a careful selection of the anticholinergic medication for treatment of detrusor muscle overactivity is mandatory to prevent a detrimental effect on the performance of a BCI.

Beside anticholinergics also medication for treatment of spasticity of skeletal muscles such as baclofen, an agonist to GABA-β receptors, have an inﬂuence on the EEG spectral power distribution leading to an increase of slow brain waves (Seyfert and Straschill, 1982; Badr etal., 1983). Although systematic examinations on the inﬂuence of GABA agonists on the performance of BCI are missing, it can be assumed that the increase of slow waves and decrease of spectral components with higher frequencies will have a negative impact at least on SMR-based BCIs.

Intheacutephasepatientsreceiveahighdoseof medicationfor suppression of post-operative or trauma related nociceptive pain. A common adverse effect of this medication is its detrimental inﬂuence on attention, memory and concentration contributing to tiredness of end users. These effects alter signiﬁcantly the performance of a BCI (Schreuder etal., 2013).

Autonomic dysreﬂexia

Autonomic dysreﬂexia is a potentially dangerous clinical syndrome that develops in individuals with SCI, resulting in acute, uncontrolled hypertension. Brieﬂy, AD develops within the ﬁrst 6 months after injury in individuals with a neurologic level at or above the sixth thoracic level (T6). AD prevalence rates vary, but the generally accepted rate is 48–90% of all individuals with injuries at T6 and above. Patients with a sensorimotor complete injury have a much higher incidence of AD (91% with complete injury vs. 27% with incomplete injury; Curt etal., 1997). The occurrence of AD increases as the patient evolves out of spinal shock. With the return of sacral reﬂexes, the possibility of AD increases (Schottler etal.,

- 2009). Autonomic dysreﬂexia is caused by the damage of sympa-

The event of an SCI often occurs within minutes after a trauma or may evolve in non-traumatic causes like ischemia or infections over a few days. The affected persons are not able to slowly adapt to this novel situation, which normally results in an acute stress reaction. Generally speaking, an acute stress reaction is a transient condition that develops in response to a traumatic event. Symptoms occur within 1 month of the extreme stressor and resolves within a 4 week period. They may include a varying mixture of reduced levels of consciousness, withdrawal, anxiety symptoms, narrowing of attention, and disorientation. If the acute stress reaction persists longer than 4 weeks, an adjustment disorder may be present. Adjustment disorders may complicate the course of rehabilitation either by the decrease of compliance with the recommended medical regime resulting in an increased length of hospital stay. Common symptoms of an adjustment disorder include depressed mood, anxiety or worry, feeling unable to cope with life at present or plan ahead, stress-related physical symptoms such as headaches and interference with social functioning or performance of daily activities.

Although, results from systematic investigations on this issue are missing, an acute stress reaction negatively impacts the use of BCIs in patients during the very acute phase up to 4 weeks after the injury.

Additionally to the psychological complication mentioned so far, patients may experience episodes of depression already a few weeks after the injury. Depression is more common in the SCI population compared the general population. Estimated rates of depression among people with SCI range from 11 to 37% (Craig etal., 2014). Common emotional, behavioral, and physical symptoms of major depression are markedly depressed mood, loss of interest, reduced self-esteem and self- conﬁdence, feelings of guilt and worthlessness, reduced energy leading to fatigue, diminished activity, and reduced concentration. All of those symptoms may result in an unwillingness to participate in any kind of rehabilitative training including BCI therapy. Patients suffering from a major depression refuse to be provided with assistive technology in general.

thetic spinal ﬁbers and the resulting imbalanced innervation of the autonomous nervous system, which may – if not recognized and treated correctly – lead to long-term complications such as seizures, retinal complications, pulmonary edema, myocardial infarction, or cerebral hemorrhage.

Episodes of AD can be triggered by any painful, irritating, or even strong stimulus below the level of the injury many (Krassioukov etal., 2009). Mainly bladder distension or irritations due to a blocked or kinked catheter or failure of a timely intermittent catheterization program are responsible for 75–85% of the cases (Lindan etal., 1980). AD may also be triggered by electrical stimulation of the lower extremity (Ashley etal., 1993), but has also been seen by the author in very high lesioned patients during the application of a grasp neuroprosthesis.

There is also evidence that the P300 amplitude is decreased in individuals with major depression (Diner etal., 1985), which might contribute to the inability to achieve a sufﬁcient level of BCI performance. Theinabilityof BCIcontrolmightinturncontribute to an increase in the symptoms of depression. To avoid this vicious

Although a BCI does not triggerAD,its operation may be negatively inﬂuenced by episodes of AD. Additionally,AD may prevent

also for people with motor impairments such as spinal cord injuries.

circleathoroughneuropsychologicalassessmentisneededinacute patients to identify any signs of major depression.

In a recent study, a three-class MI screening (left hand, right hand, feet) was performed with a group of 10 able-bodied and 16 tetra- and paraplegic people with a complete SCI with the objective of determining what differences were present between the user groups and how they would impact upon the ability of these user groups to interact with a BCI. Although, the patient group was very heterogeneous in terms of time after trauma and age it is seen that both the tetraplegic and paraplegic patients have some signiﬁcant differences in event-related desynchronization strengths, exhibit signiﬁcant increases in synchronization and reach signiﬁcantly lower mean accuracies (66.1%) than the group of non-impaired subjects (85.1%; Müller-Putz etal., 2014).

SMR-based BCIs and neuropathic pain

Pain is a major problem after SCI and most of the patients report to have pain. In the acute phase after an SCI it is mainly nociceptive pain due to trauma or spams (Finnerup, 2013). Usually within the ﬁrst year after the injury neuropathic pain develops in about 40–50% of the patients and tends to become chronic (Siddall etal., 2003). Beside the general negative effects of pain on the quality of life of the affected persons, pain leads to deﬁcits in concentration and attention – both having negative impact on the BCI performance. A recent study showed that the EEG activity of spinal cord injured patients with chronic neuropathic pain differs to that of spinal cord injured patients with no pain and also to that of able-bodied people (Vuckovic etal., 2014). Frequency-speciﬁc EEG signatures were identiﬁed that may be used to monitor the development of neuropathic pain. However, it is not clear if the evolvement of these EEG patterns have a detrimental effect on BCI control.

In another study, authors compared the BCI performance of 15 end users with complete SCI, eight of them paraplegic and seven tetraplegic (Pfurtscheller etal., 2009). It was found that ﬁve of the paraplegic individuals had a mean accuracy above 70% but only one tetraplegic person achieved this performance level. The reason for this observation is still unclear. It can be speculated that the missing sensory loop restricts the vividness of the imagined movements and therefore the performance. This statement is supported by (Alkadhi etal., 2005), who showed the positive correlation of cortical activation and vividness of the imagined movement.

For operation of an SMR-based BCI users have to imagine movements from different, also paralyzed parts of the body. The inﬂuence of MI on neuropathic pain is still an issue of debate and it is not entirely clear, if MI training is lowering or increasing the perceived pain level. It was shown in patients with a chronic thoracic SCI that imagination of foot movements three times a day for a period of 7 days increases neuropathic pain (Gustin etal., 2008). In contrast to this, preliminary studies suggest that neurofeedback has the potential to help patients with otherwise refractory chronic pain (Jensen etal.,2013a). Recent ﬁndings indicate that certain EEG activity patterns may be associated with more pain or a vulnerability to experience chronic pain in persons with SCI. Research examining the extent to which changes in this EEG activity may result in pain relief is warranted (Jensen etal., 2013b).

It is a well-accepted statement in the BCI community, that training is expected to improve the performance of SMR-BCIs. Data on the course and performance of long-term MI-BCI training in individuals with chronic high-level SCI is sparse. In one study, two C4, three C6 and four C7 end users were trained to operate an MI-BCI with the goal of controlling a robotic arm (Onose etal., 2012). The average performance of all subjects was quite moderate, determined as 70.5%. In three of the subjects the online performance was up to 20% worse (in a two-class task) than the ofﬂine performance. Unfortunately, the authors did not explicitly state how many ofﬂine runs were used for classiﬁer training, so it is possible that their classiﬁers were trained too intensively on the same dataset. This may result in overﬁtting and therefore suggesting a far higher ofﬂine performance than actually achieved during online trials. Furthermore, online experiments are more demanding, which may also affect the performance. One of the study subjects fell asleep during the training, which indicates a high physical and mental workload during the operation of the BCI.

Insummary,theuseof neurofeedbackforpreventionof chronic neuropathic pain is still controversial. Clinical studies are urgently needed to reveal if BCIs represent a promising tool to prevent the development of neuropathic pain in SCI.

Inability for BCI control

While BCIs based on the registration of P300 (Guger etal., 2009a) and SSVEPs (Guger etal., 2012a) can be operated by a vast majority of users, it is well-known that SMR-BCIs are not suitable for all users. In up to one third of the non-motor-impaired participants the BCI is unable to detect classiﬁable task related EEG patterns (Guger etal., 2003). Consequently, these subjects cannot quickly be provided with a BCI-controlled application or need at least a substantial amount of training for sufﬁcient operation of a BCI. The causes for this inability for controlling a BCI (other synonyms are BCI-“inefﬁciency,” BCI-aptitude) have not yet been satisfactorily described. The few studies that explicitly investigated the predictive value of user- and BCI-related factors on BCI performance have been performed with subjects without motor impairments (Kübler etal., 2004; Blankertz etal., 2010; Halder etal., 2011; Holz etal., 2011; Kaufmann etal., 2013). Thus, it is not known, in how far these results are representative

In the framework of a single case study, in which an individual with a lesion of the upper cervical spinal cord was provided with a BCI-controlled upper extremity neuroprosthesis, no training effects occurred over a training time of more than 6 months. Even after 415 MI-BCI runs, the end user’s average performance did not show any trend toward improvement, but remained at about 70% with large day-to-day variances. This moderate average performance may be explained by the signiﬁcant differences in movement-related ß-band modulations found in subjects with SCI as compared to non-injured individuals (Gourab and Schmit, 2010). In detail, a correlation seems to exist between decreased ERS amplitude and the severity of the impairment of the limb

P300-based BCI systems are the ﬁrst choice, because almost all persons are able to achieve a sufﬁcient level of control with only a small amount of training. MI based BCIs providing a feedback on the modulation of SMRs of the primary motor cortex may evolve to an exciting adjunct to conventional neurorehabilitative therapies aiming at enhancement of motor function by guidance of neural plasticity. This approach is particularly promising, if combined with neuroprotheses of the upper extremity providing a strong proprioceptive feedback. However, clinical studies need to show that no detrimental effects like an increase of neuropathic pain occur during this type of training.

in which the movement was attempted. This supports the view that in high-level tetraplegic subjects, an extensive BCI training period does not necessarily lead to superior results. Although, this statement has to be validated in future studies with a larger population, it must be clearly communicated to patients with an acute SCI. It is entirely possible that only low to moderate performance will be achieved with the danger of causing additional sadness or depression and generating a higher stress level, because severely motor impaired persons may get the impression that in addition to their body even their brains do not work properly.

On a more general level,a couple of factors are limiting the successful use of BCIs, among them technology related, user speciﬁc and infrastructure dependent factors. The major limitations in the technological domain are the need for gel electrodes with their time-consuming and non-user friendly handling and the need for technical experts for setup and supervision of the BCI. Additionally, user related issues such as spasmolytic and other medication, acute stress syndromes, or episodes of depression may have a negative impact on the BCI performance with the risk of causing additional frustration and sadness. Limited personnel and time resources are a general problem for successful implementation of any kind of novel therapeutic approach in the clinical setting. These may be overcome by regular reimbursement of BCI therapies in the clinical setting. However, to achieve this large scale clinical trials need to be performed, which prove the efﬁcacy and additional beneﬁt of BCIs.

### INFRASTRUCTURE AND HEALTH-CARE SYSTEM RELATED FACTORS

Beside BCI and user-related factors there are factors associated to thetypicalinfrastructureinclinicsandtothehealth-caresystemin general, which form major barriers for the successful integration of BCIs into clinical routine. Patients rehabilitated in industrial countries take part in normally two sessions of physio- and one session of occupational therapy of a length of 30 min each. With the currently available BCI technology a BCI session takes at least 1 hour to setup the BCI, perform a supervised training/operation and remove the gel from the hair of the patients. Additionally, a BCI needs to be set up and adapted to each individual user, which takes even more time in particular during the ﬁrst sessions. This means that patients will at least miss two out of three daily sessions of conventional therapy, which is neither accepted by the clinical staff nor by the patients themselves. Therefore, BCIs are likely to be used as adjunct rehabilitative tools with the need for additional personnel or therapy slots. However, these BCI application sessions are not separately reimbursed by the health service or insurances and need to be covered by the budget of the clinics themselves.

Studies involving individuals with isolated injuries of the spinal cord may provide preliminary information on the feasibility of BCI-based neurorehabilitative approaches in other neurological patient groups like stroke survivors or patients with traumatic brain injury. The challenges and general problems seen in studies with individuals with SCI in the clinical environment are likely to occur also in other patient groups and help to realistically estimate the number of potential end user of BCI technology.

The major problem in the ﬁeld of BCIs is that randomized controlled trials providing clear evidence for their superiority compared to traditional approaches are missing completely (Kübler etal., 2013). In particular, the relationship between the investments in terms of personnel,time and money and the degree of improvement in patient outcomes needs to be determined. This information is mandatory to initiate a dialog with health service payers with the aim of reimbursement of BCI applications during the inpatient rehabilitation phase and later on in the chronic stage also at home.

## ACKNOWLEDGMENTS

TheauthorwouldliketothankM.Schneidersforhiscontributions to the graphical design of the ﬁgure.

## REFERENCES

At this point it must be emphasized that general recommendations on the integration of novel therapies such as the BCI into clinical routine cannot be made due to huge differences in the length of primary rehabilitation between health systems of different countries and in the modes of reimbursement in particular in different European countries.

Alkadhi, H., Brugger, P., Boendermaker, S. H., Crelier, G., Curt,A., Hepp-Reymond, M. C., etal. (2005). What disconnection tells about motor imagery: evidence from paraplegic patients. Cereb. Cortex 15, 131–140. doi: 10.1093/cercor/bhh116

Allison, B., Luth, T., Valbuena, D., Teymourian, A., Volosyak, I., and Gräser, A. (2010). BCI demographics: how many (and what kinds of) people can use an SSVEP BCI? IEEE Trans. Neural Syst. Rehabil. Eng. 18, 107–116. doi: 10.1109/TNSRE.2009.2039495

Allison, B. Z., Leeb, R., Brunner, C., Müller-Putz, G. R., Bauernfeind, G., Kelly, J. W., etal. (2012). Toward smarter BCIs: extending BCIs through hybridization and intelligent control. J. Neural Eng. 9:013001. doi: 10.1088/1741-2560/9/1/013001

## CONCLUSION AND OUTLOOK

In the context of rehabilitation of individuals with SCI in the acute and subacute stage non-invasive BCIs represent a valuable adjunct totraditionalcompensatoryandrestorativeapproachesintheclinical setting. The main focus of their application is the use as an additional or alternative channel for operation of assistive devices enabling communication and environmental control in patients with very high lesions of the spinal cord. For this application

Aloise, F., Schettini, F., Arico, P., Salinari, S., Guger, C., Rinsma, J., etal. (2011). Asynchronous P300-based brain-computer interface to control a virtual environment: initial tests on end users. Clin. EEG Neurosci. 42, 219–224. doi: 10.1177/155005941104200406

Anderson, K. D. (2004). Targeting recovery: priorities of the spinal cord-injured population. J. Neurotrauma 21, 1371–1383. doi: 10.1089/neu.2004.21.1371

Ashley, E. A., Laskin, J. J., Olenik, L. M., Burnham, R., Steadward, R. D., Cumming, D. C.,etal. (1993). Evidence of autonomic dysreﬂexia during functional electrical

stimulation in individuals with spinal cord injuries. Paraplegia 31, 593–605. doi: 10.1038/sc.1993.95

Diner, B. C., Holcomb, P. J., and Dykman, R. A. (1985). P300 in major depressive disorder. Psychiatry Res. 15, 175–184. doi: 10.1016/0165-1781(85)90074-5

Enzinger, C., Ropele, S., Fazekas, F., Loitfelder, M., Gorani, F., Seifert, T., etal. (2008). Brain motor system function in a patient with complete spinal cord injury following extensive brain-computer interface training. Exp. Brain Res. 190, 215–223. doi: 10.1007/s00221-008-1465-y

Badr, G. G., Matousek, M., and Frederiksen, P. K. (1983). A quantitative EEG analysis of the effects of baclofen on man. Neuropsychobiology 10, 13–18. doi: 10.1159/000117978

Baek, H. J., Kim, H. S., Heo, J., Lim, Y. G., and Park, K. S. (2013). Brain-computer interfaces using capacitive measurement of visual or auditory steady-state responses. J. Neural Eng. 10:024001. doi: 10.1088/1741-2560/10/2/024001

Exner, G. (2004). The working group “paraplegy” of the federation of commercial professional associations in Germany. Facts, ﬁgures and prognoses. Trauma Berufskr. 6, 147–151. doi: 10.1007/s10039-004-0877–876

Birbaumer, N., Ghanayim, N., Hinterberger, T., Iversen, I., Kotchoubey, B., Kübler, A., etal. (1999). A spelling device for the paralysed. Nature 398, 297–298. doi: 10.1038/18581

Faller, J., Torrellas, S., Miralles, F., Holzner, C., Kapeller, C., Guger, C., etal. (2012). Prototype of an auto-calibrating, context-aware, hybrid brain-computer interface. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2012, 1827–1830. doi: 10.1109/EMBC.2012.6346306

Birbaumer, N., Hinterberger, T., Kübler, A., and Neumann, N. (2003). The thought-translation device (TTD): neurobehavioral mechanisms and clinical outcome. IEEE Trans. Neural Syst. Rehabil. Eng. 11, 120–123. doi: 10.1109/TNSRE.2003.814439

Farwell, L. A., and Donchin, E. (1988). Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalogr. Clin. Neurophysiol. 70, 510–523. doi: 10.1016/0013-4694(88)90149-6

Birbaumer, N., Murguialday, A. R., and Cohen, L. (2008). Braincomputer interface in paralysis. Curr. Opin. Neurol. 21, 634–638. doi: 10.1097/WCO.0b013e328315ee2d

Fazel-Rezai, R., Allison, B. Z., Guger, C., Sellers, E. W., Kleih, S. C., and Kübler, A.

(2012). P300 brain computer interface: current challenges and emerging trends. Front. Neuroeng. 5:14. doi: 10.3389/fneng.2012.00014

Birbaumer, N., Ramos Murguialday, A., Weber, C., and Montoya, P. (2009). Neurofeedback and brain-computer interface clinical applications. Int. Rev. Neurobiol. 86, 107–117. doi: 10.1016/S0074-7742(09)86008-X

Fazli, S., Popescu, F., Danoczy, M., Blankertz, B., Müller, K. R., and Grozea, C.

(2009). Subject-independent mental state classiﬁcation in single trials. Neural Netw. 22, 1305–1312. doi: 10.1016/j.neunet.2009.06.003

Blankertz, B., Dornhege, G., Krauledat, M., Müller, K. R., Kunzmann, V., Losch, F., etal. (2006). The berlin brain-computer interface: EEG-based communication without subject training. IEEE Trans. Neural Syst. Rehabil. Eng. 14, 147–152. doi: 10.1109/TNSRE.2006.875557

Finnerup, N. B. (2013). Pain in patients with spinal cord injury. Pain 1, S71–S76. doi: 10.1016/j.pain.2012.12.007

Flemisch, O., Adams, A., Conway, S. R., Goodrich, K. H., Palmer, M. T., and Schutte, P. C. (2003). The H-Metaphor as a Guideline for Vehicle Automation and Interaction. Hampton: NASA.

Blankertz, B., Sannelli, C., Halder, S., Hammer, E. M., Kübler, A., Müller, K. R., etal. (2010). Neurophysiological predictor of SMR-based BCI performance. Neuroimage 51, 1303–1309. doi: 10.1016/j.neuroimage.2010.03.022

Furdea, A., Halder, S., Krusienski, D. J., Bross, D., Nijboer, F., Birbaumer, N., etal.

(2009).Anauditoryoddball(P300)spellingsystemforbrain-computerinterfaces. Psychophysiology 46, 617–625. doi: 10.1111/j.1469-8986.2008.00783.x

Borenstein, J., and Koren, Y. (1991). The vector ﬁeld histogram – fast obstacle avoidance for mobile robots. IEEE Trans. Robot. Autom. 7, 278–288. doi: 10.1109/70.88137

Furlan, J. C., Sakakibara, B. M., Miller, W. C., and Krassioukov, A. V. (2013). Global incidence and prevalence of traumatic spinal cord injury. Can. J. Neurol. Sci. 40, 456–464.

Carabalona,R.,Grossi,F.,Tessadri,A.,Castiglioni,P.,Caracciolo,A.,andDeMunari, I. (2012). Light on! Real world evaluation of a P300-based brain-computer interface (BCI) for environment control in a smart home. Ergonomics 55, 552–563. doi: 10.1080/00140139.2012.661083

Galán, F., Nuttin, M., Lew, E., Ferrez, P. W., Vanacker, G., Philips, J., etal. (2008). A brain-actuated wheelchair: asynchronous and non-invasive Brain-computer interfaces for continuous control of robots. Clin. Neurophysiol. 119, 2159–2169. doi: 10.1016/j.clinph.2008.06.001

Carlson, T., and Demiris, Y. (2008). “Human-wheelchair collaboration through prediction of intention and adaptive assistance,” in Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), Pasadena, CA.

Gollee, H., Volosyak, I., Mclachlan, A. J., Hunt, K. J., and Gräser, A. (2010). An SSVEP-based brain-computer interface for the control of functional electrical stimulation. IEEE Trans. Biomed. Eng. 57, 1847–1855. doi: 10.1109/TBME.2010.2043432

Carlson,T.,andMillán,J.D.R.(2013). Brain-controlledwheelchairs:aroboticarchitecture. IEEE Robot. Autom. Mag. 20, 65–73. doi: 10.1109/MRA.2012.2229936 Carlson, T., Tonin, L., Perdikis, S., Leeb, R., and del R Millán, J. (2013). A hybrid BCI for enhanced control of a telepresence robot. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2013, 3097–3100. doi: 10.1109/EMBC.2013.6610196

Gourab, K., and Schmit, B. D. (2010). Changes in movement-related beta-band EEG signals in human spinal cord injury. Clin. Neurophysiol. 121, 2017–2023. doi: 10.1016/j.clinph.2010.05.012

Cheng, M., Gao, X., Gao, S., and Xu, D. (2002). Design and implementation of a brain-computer interface with high transfer rates. IEEE Trans. Biomed. Eng. 49, 1181–1186. doi: 10.1109/TBME.2002.803536

Grosse-Wentrup, M., Mattia, D., and Oweiss, K. (2011). Using brain-computer interfacestoinduceneuralplasticityandrestorefunction. J.NeuralEng. 8:025004. doi: 10.1088/1741-2560/8/2/025004

Cincotti, F., Mattia, D., Aloise, F., Bufalari, S., Schalk, G., Oriolo, G., etal. (2008). Non-invasivebrain-computerinterfacesystem: towardsitsapplicationasassistive technology. Brain Res. Bull. 75, 796–803. doi: 10.1016/j.brainresbull.2008.01.007

Grozea, C., Voinescu, C. D., and Fazli, S. (2011). Bristle-sensors – low-cost ﬂexible passive dry EEG electrodes for neurofeedback and BCI applications. J. Neural Eng. 8:025008. doi: 10.1088/1741-2560/8/2/025008

Collinger, J. L., Boninger, M. L., Bruns, T. M., Curley, K., Wang, W., and Weber, D. J. (2013). Functional priorities, assistive technology, and brain-computer interfaces after spinal cord injury. J. Rehabil. Res. Dev. 50, 145–160. doi: 10.1682/JRRD.2011.11.0213

Guger, C., Allison, B. Z., Grosswindhager, B., Pruckl, R., Hintermüller, C., Kapeller, C., etal. (2012a). How Many people could use an SSVEP BCI? Front. Neurosci. 6:169. doi: 10.3389/fnins.2012.00169

Guger, C., Krausz, G., Allison, B. Z., and Edlinger, G. (2012b). Comparison of dry and gel based electrodes for p300 brain-computer interfaces. Front. Neurosci. 6:60. doi: 10.3389/fnins.2012.00060

Combaz, A., Chatelle, C., Robben, A., Vanhoof, G., Goeleven, A., Thijs, V., etal. (2013). A comparison of two spelling brain-computer interfaces based on visual P3 and SSVEP in Locked-In Syndrome. PLoS ONE 8:e73691. doi: 10.1371/journal.pone.0073691

Guger, C., Daban, S., Sellers, E., Holzner, C., Krausz, G., Carabalona, R., etal. (2009a). How many people are able to control a P300-based brain-computer interface (BCI)? Neurosci. Lett. 462, 94–98. doi: 10.1016/j.neulet.2009.06.045

Craig, A., Rodrigues, D., Tran, Y., Guest, R., Bartrop, R., and Middleton, J. (2014). Developing an algorithm capable of discriminating depressed mood in people with spinal cord injury. Spinal Cord 52, 413–416. doi: 10.1038/sc.2014.25

Guger, C., Daban, S., Sellers, E., Holzner, C., Krausz, G., Carabalona, R., etal. (2009b). How many people are able to control a P300-based brain-computer interface (BCI)? Neurosci. Lett. 462, 94–98. doi: 10.1016/j.neulet.2009.06.045

Curt, A., Nitsche, B., Rodic, B., Schurch, B., and Dietz, V. (1997). Assessment of autonomic dysreﬂexia in patients with spinal cord injury. J. Neurol. Neurosurg. Psychiatry 62, 473–477. doi: 10.1136/jnnp.62.5.473

Guger, C., Edlinger, G., Harkam, W., Niedermayer, I., and Pfurtscheller, G. (2003). How many people are able to operate an EEG-based brain-computer interface (BCI)? IEEE Trans. Neural Syst. Rehabil. Eng. 11, 145–147. doi: 10.1109/TNSRE.2003.814481

Curt,A.,VanHedel,H.J.,Klaus,D.,andDietz,V.(2008). Recoveryfromaspinalcord injury: signiﬁcance of compensation,neural plasticity,and repair. J. Neurotrauma 25, 677–685. doi: 10.1089/neu.2007.0468

Gustin, S. M.,Wrigley, P. J., Gandevia, S. C., Middleton, J. W., Henderson, L. A., and Siddall,P.J.(2008). Movementimageryincreasespaininpeoplewithneuropathic

Dietz, V., and Fouad, K. (2014). Restoration of sensorimotor functions after spinal cord injury. Brain 137, 654–667. doi: 10.1093/brain/awt262

pain following complete thoracic spinal cord injury. Pain 137, 237–244. doi: 10.1016/j.pain.2007.08.032

Kilgore, K. L., Hoyen, H. A., Bryden, A. M., Hart, R. L., Keith, M. W., and Peckham, P. H. (2008). An implanted upper-extremity neuroprosthesis using myoelectric control. J. Hand Surg. Am. 33, 539–550. doi: 10.1016/j.jhsa.2008.01.007

Halder, S., Agorastos, D., Veit, R., Hammer, E. M., Lee, S., Varkuti, B., etal. (2011). Neural mechanisms of brain-computer interface control. Neuroimage 55, 1779–

Kim, D. W., Hwang, H. J., Lim, J. H., Lee, Y. H., Jung, K. Y., and Im, C. H. (2011). Classiﬁcation of selective attention to auditory stimuli: toward vision-free brain-computer interfacing. J. Neurosci. Methods 197, 180–185. doi: 10.1016/j.jneumeth.2011.02.007

1790. doi: 10.1016/j.neuroimage.2011.01.021 Halder, S., Rea, M., Andreoni, R., Nijboer, F., Hammer, E. M., Kleih, S. C., etal.

(2010). An auditory oddball brain-computer interface for binary choices. Clin. Neurophysiol. 121, 516–523. doi: 10.1016/j.clinph.2009.11.087

Kindermans, P. J., Verstraeten, D., and Schrauwen, B. (2012). A bayesian model for exploiting application constraints to enable unsupervised training of a P300based BCI. PLoS ONE 7:e33758. doi: 10.1371/journal.pone.0033758

Hammer, E. M., Halder, S., Blankertz, B., Sannelli, C., Dickhaus, T., Kleih, S., etal. (2012). Psychological predictors of SMR-BCI performance. Biol. Psychol. 89, 80–86. doi: 10.1016/j.biopsycho.2011.09.006

Kleih, S. C., Kaufmann, T., Zickler, C., Halder, S., Leotta, F., Cincotti, F., etal. (2011). Outof thefryingpanintotheﬁre–theP300-basedBCIfacesreal-worldchallenges. Prog. Brain Res. 194, 27–46. doi: 10.1016/B978-0-444-53815-4.00019-4

Hentz, V. R., and Leclercq, C. (2002). Surgical Rehabilitation of the Upper Limb in Tetraplegia (London: W. B. Saunders).

Hiersemenzel, L. P., Curt, A., and Dietz, V. (2000). From spinal shock to spasticity: neuronal adaptations to a spinal cord injury. Neurology 54, 1574–1582. doi: 10.1212/WNL.54.8.1574

Kleih, S. C., Nijboer, F., Halder, S., and Kübler,A. (2010). Motivation modulates the P300 amplitude during brain-computer interface use. Clin. Neurophysiol. 121, 1023–1031. doi: 10.1016/j.clinph.2010.01.034

Hinterberger, T., Schmidt, S., Neumann, N., Mellinger, J., Blankertz, B., Curio, G., etal. (2004). Brain-computer communication and slow cortical potentials. IEEE Trans. Biomed. Eng. 51, 1011–1018. doi: 10.1109/TBME.2004.827067

Krassioukov, A., Warburton, D. E., Teasell, R., and Eng, J. J. (2009). A systematic review of the management of autonomic dysreﬂexia after spinal cord injury. Arch. Phys. Med. Rehabil. 90, 682–695. doi: 10.1016/j.apmr.2008.10.017

Holz, E. M., Kaufmann, T., Desideri, L., Malavasi, M., Hoogerwerf, E. J., and Kübler, A. (2011). User centred design in BCI development. Biol. Med. Phys. Biomed. Eng. 2013:22.

Kreilinger,A.,Kaiser,V.,Breitwieser,C.,Williamson,J.,Neuper,C.,and Müller-Putz, G. R. (2011). Switching between manual control and brain-computer interface using long term and short term quality measures. Front. Neurosci. 5:147. doi: 10.3389/fnins.2011.00147

Horki,P.,Neuper,C.,Pfurtscheller,G.,andMüller-Putz,G.R.(2010).Asynchronous steady-state visual evoked potential based BCI control of a 2-DoF artiﬁcial upper limb. Biomed. Tech. 55, 367–374. doi: 10.1515/BMT.2010.044

Krusienski, D. J., Sellers, E. W., Mcfarland, D. J., Vaughan, T. M., and Wolpaw, J. R. (2008). Toward enhanced P300 speller performance. J. Neurosci. Methods 167, 15–21. doi: 10.1016/j.jneumeth.2007.07.017

Huggins, J. E., Wren, P. A., and Gruis, K. L. (2011). What would braincomputer interface users want? Opinions and priorities of potential users with amyotrophic lateral sclerosis. Amyotroph Lateral Scler. 12, 318–324. doi: 10.3109/17482968.2011.572978

Kübler, A., Mattia, D., Rupp, R., Tangermann, M. (2013). Facing the challenge: bringing brain-computer interfaces to end-users. Artif. Intell. Med. 59, 55–60. doi: 10.1016/j.artmed.2013.08.002

ISO. (2010). ISO 9241:2010 Ergonomics of Human-System Interaction Part 210: Human-Centred Design for Interactive Systems. Geneva: International Organization for Standardization.

Kübler, A., Neumann, N., Wilhelm, B., Hinterberger, T., and Birbaumer, N. (2004). Predictability of brain-computer communication. Int. J. Psychophysiol. 18, 121–

129. doi: 10.1027/0269-8803.18.23.121

Iturrate, I., Antelis, J. M., Kübler, A., and Minguez, J. (2009). A noninvasive brain-actuatedwheelchairbasedonaP300neurophysiologicalprotocolandautomated navigation. IEEE Trans. Robot. 25, 614–627. doi: 10.1109/TRO.2009.20 20347

Leeb, R., Gubler, M., Tavella, M., Miller, H., and Del Millan, J. R. (2010). On the road to a neuroprosthetic hand: a novel hand grasp orthosis based on functional electrical stimulation. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2010, 146–149. doi: 10.1109/IEMBS.2010.5627412

Jackson, A., and Zimmermann, J. B. (2012). Neural interfaces for the brain and spinal cord – restoring motor function. Nat. Rev. Neurol. 8, 690–699. doi: 10.1038/nrneurol.2012.219

Leeb, R., Sagha, H., Chavarriaga, R., and Millán, J. D. R. (2011). A hybrid brain-computer interface based on the fusion of electroencephalographic and electromyographic activities. J. Neural. Eng. 8:025011. doi: 10.1088/17412560/8/2/025011

Jensen, M. P., Gertz, K. J., Kupper, A. E., Braden, A. L., Howe, J. D., Hakimian, S., etal. (2013a). Steps toward developing an EEG biofeedback treatment for chronic pain. Appl. Psychophysiol. Biofeedback 38, 101–108. doi: 10.1007/s10484-013-9 214-9

Lindan, R., Joiner, E., Freehafer, A. A., and Hazel, C. (1980). Incidence and clinical features of autonomic dysreﬂexia in patients with spinal cord injury. Paraplegia 18, 285–292. doi: 10.1038/sc.1980.51

Jensen, M. P., Sherlin, L. H., Gertz, K. J., Braden, A. L., Kupper, A. E., Gianas, A., etal. (2013b). Brain EEG activity correlates of chronic pain in persons with spinal cord injury: clinical implications. Spinal Cord 51, 55–58. doi: 10.1038/sc. 2012.84

Millán, J. D. R., Galán, F., Vanhooydonck, D., Lew, E., Philips, J., and Nuttin, M. (2009). Asynchronous non-invasive brain-actuated control of an intelligent wheelchair. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2009, 3361–3364. doi: 10.1109/IEMBS.2009.5332828

Kaiser, V., Bauernfeind, G., Kreilinger, A., Kaufmann, T., Kübler, A., Neuper, C., etal. (2014). Cortical effects of user training in a motor imagery based braincomputer interface measured by fNIRS and EEG. Neuroimage 1, 432–444. doi: 10.1016/j.neuroimage.2013.04.097

Moghimi, S., Kushki, A., Guerguerian, A. M., and Chau, T. (2013). A review of EEG-based brain-computer interfaces as access pathways for individuals with severe disabilities. Assist. Technol. 25, 99–110. doi: 10.1080/10400435.2012.7 23298

Kathner, I., Ruf, C. A., Pasqualotto, E., Braun, C., Birbaumer, N., and Halder, S.

Moss, C. W., Kilgore, K. L., and Peckham, P. H. (2011). A novel command signal for motor neuroprosthetic control. Neurorehabil. Neural Repair 25, 847–854. doi: 10.1177/1545968311410067

(2013). A portable auditory P300 brain-computer interface with directional cues. Clin. Neurophysiol. 124, 327–338. doi: 10.1016/j.clinph.2012.08.006

Kaufmann, T., Schulz, S. M., Koblitz, A., Renner, G., Wessig, C., and Kübler, A. (2013). Face stimuli effectively prevent brain-computer interface inefﬁciency in patients with neurodegenerative disease. Clin. Neurophysiol. 124, 893–900. doi: 10.1016/j.clinph.2012.11.006

Müller-Putz, G. R., Breitwieser, C., Cincotti, F., Leeb, R., Schreuder, M., Leotta, F., etal. (2011). Tools for brain-computer interaction: a general concept for a hybrid BCI. Front. Neuroinform. 5:30. doi: 10.3389/fninf.2011.00030

Müller-Putz, G. R., Daly, I., and Kaiser,V. (2014). Motor imagery-induced EEG patterns in individuals with spinal cord injury and their impact on brain-computer interface accuracy. J. Neural Eng. 11:035011. doi: 10.1088/1741-2560/11/3/0 35011

Kaufmann, T., Volker, S., Gunesch, L., and Kübler, A. (2012). Spelling is just a click away – a user-centered brain-computer interface including auto-calibration and predictive text entry. Front. Neurosci. 6:72. doi: 10.3389/fnins.2012. 00072

Muller-Putz, G. R., Scherer, R., Neuper, C., and Pfurtscheller, G. (2006). Steady-state somatosensory evoked potentials: suitable brain signals for braincomputer interfaces? IEEE Trans. Neural Syst. Rehabil. Eng. 14, 30–37. doi: 10.1109/TNSRE.2005.863842

Kay, G. G., and Ebinger, U. (2008). Preserving cognitive function for patients with overactive bladder: evidence for a differential effect with darifenacin. Int. J. Clin. Pract. 62, 1792–1800. doi: 10.1111/j.1742-1241.2008.01849.x

Keith, M. W., and Peljovich, A. (2012). Surgical treatments to restore function control in spinal cord injury. Handb. Clin. Neurol. 109, 167–179. doi: 10.1016/B978-0-444-52137-8.00010-3

Müller-Putz, G. R., Scherer, R., Pfurtscheller, G., and Rupp, R. (2005). EEG-based neuroprosthesis control: a step towards clinical practice. Neurosci. Lett. 382, 169–

174. doi: 10.1016/j.neulet.2005.03.021

Nardone, R., Holler, Y., Brigo, F., Seidl, M., Christova, M., Bergmann, J., etal. (2013). Functional brain reorganization after spinal cord injury: systematic review of animal and human studies. Brain Res. 1504, 58–73. doi: 10.1016/j.brainres.2012.12.034

Popovic, M. R., Popovic, D. B., and Keller, T. (2002). Neuroprostheses for grasping. Neurol. Res. 24, 443–452. doi: 10.1179/016164102101200311

Rebsamen, B., Guan, C., Zhang, H., Wang, C., Teo, C., Ang, M. H., etal. (2010). A brain controlled wheelchair to navigate in familiar environments. IEEE Trans. Neural Syst. Rehabil. Eng. 18, 590–598. doi: 10.1109/TNSRE.2010.20 49862

National Spinal Cord Injury Statistical Center. (2012). The 2012 Annual Statistical Report for the Model Spinal Cord Injury Care System. National SCI Statistical Center. Available at: www.uab.edu/NSCISC [accessed August 7, 2014].

Riccio, A., Mattia, D., Simione, L., Olivetti, M., and Cincotti, F. (2012). Eye-gaze independent EEG-based brain-computer interfaces for communication. J. Neural Eng. 9:045001. doi: 10.1088/1741-2560/9/4/045001

Neumann, N., Kübler, A., Kaiser, J., Hinterberger, T., and Birbaumer, N. (2003). Conscious perception of brain states: mental strategies for braincomputer communication. Neuropsychologia 41,1028–1036. doi: 10.1016/S00283932(02)00298-1

Rockstroh, B., Birbaumer, N., Elbert, T., and Lutzenberger, W. (1984). Operant control of EEG and event-related and slow brain potentials. Biofeedback Self Regul. 9, 139–160. doi: 10.1007/BF00998830

Neuper, C., Scherer, R., Reiner, M., and Pfurtscheller, G. (2005). Imagery of motor actions: differential effects of kinesthetic and visual-motor mode of imagery in single-trial EEG. Brain Res. Cogn. Brain Res. 25, 668–677. doi: 10.1016/j.cogbrainres.2005.08.014

Rohm, M., Schneiders, M., Müller, C., Kreilinger, A., Kaiser, V., Müller-Putz, G. R., etal. (2013). Hybrid brain-computer interfaces and hybrid neuroprostheses for restoration of upper limb functions in individuals with high-level spinal cord injury. Artif. Intell. Med. 59, 133–142. doi: 10.1016/j.artmed.2013.07.004

Nguyen, J. S., Su, S. W., and Nguyen, H. T. (2013). Experimental study on a smart wheelchair system using a combination of stereoscopic and spherical vision. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2013, 4597–4600. doi: 10.1109/EMBC.2013.6610571

Roland, J., Miller, K., Freudenburg, Z., Sharma, M., Smyth, M., Gaona, C., etal. (2011). The effect of age on human motor electrocorticographic signals and implications for brain-computer interface applications. J. Neural Eng. 8:046013. doi: 10.1088/1741-2560/8/4/046013

Nijboer, F., Birbaumer, N., and Kübler, A. (2010). The inﬂuence of psychological state and motivation on brain-computer interface performance in patients with amyotrophic lateral sclerosis – a longitudinal study. Front. Neurosci. 4:55. doi: 10.3389/fnins.2010.00055

Rupp,R.,andGerner,H.J.(2007). Neuroprostheticsof theupperextremity–clinical application in spinal cord injury and challenges for the future. Acta Neurochir. Suppl. 97, 419–426. doi: 10.1007/978-3-211-33079-1_55

Rupp, R., Kreilinger, A., Rohm, M., Kaiser, V., and Müller-Putz, G.R. (2012). Development of a non-invasive, multifunctional grasp neuroprosthesis and its evaluation in an individual with a high spinal cord injury. Conf. Proc. IEEE Eng. Med. Biol. Soc. 2012, 1835–1838. doi: 10.1109/EMBC.2012.6346308

Nijboer, F., Sellers, E. W., Mellinger, J., Jordan, M. A., Matuz, T., Furdea, A., etal. (2008). A P300-based brain-computer interface for people with amyotrophic lateral sclerosis. Clin. Neurophysiol. 119, 1909–1916. doi: 10.1016/j.clinph.2008.03.034

Rupp, R., Rohm, M., Schneiders, M., Weidner, N., Kaiser, V., Kreilinger, A., etal.

North, N. T. (1999). The psychological effects of spinal cord injury: a review. Spinal Cord 37, 671–679. doi: 10.1038/sj.sc.3100913

(2013). Think2grasp – BCI-controlled neuroprosthesis for the upper extremity. Biomed. Tech. (Berl.) doi: 10.1515/bmt-2013-4440 [Epub ahead of print].

Onose, G., Grozea, C., Anghelescu, A., Daia, C., Sinescu, C. J., Ciurea, A. V., etal. (2012). On the feasibility of using motor imagery EEG-based brain-computer interfaceinchronictetraplegicsforassistiveroboticarmcontrol: aclinicaltestand long-term post-trial follow-up. Spinal Cord 50, 599–608. doi: 10.1038/sc.2012.14

Samek, W., Vidaurre, C., Muller, K. R., and Kawanabe, M. (2012). Stationary common spatial patterns for brain-computer interfacing. J. Neural Eng. 9:026013. doi: 10.1088/1741-2560/9/2/026013

Sannelli, C., Vidaurre, C., Müller, K. R., and Blankertz, B. (2011). CSP patches: an ensembleof optimizedspatialﬁlters.Anevaluationstudy. J.NeuralEng. 8:025012. doi: 10.1088/1741-2560/8/2/025012

Ortner, R., Allison, B. Z., Korisek, G., Gaggl, H., and Pfurtscheller, G. (2011). An SSVEP BCI to control a hand orthosis for persons with tetraplegia. IEEE Trans. Neural Syst. Rehabil. Eng. 19, 1–5. doi: 10.1109/TNSRE.2010.2076364

Savic, A. M., Malesevic, N. M., and Popovic, M. B. (2014). Feasibility of a hybrid brain-computer interface for advanced functional electrical therapy. ScientiﬁcWorldJournal 2014:797128. doi: 10.1155/2014/797128

Ouzký, M. (2002). Towards Concerted Efforts for Treating and Curing Spinal Cord Injury, Report of the Social, Health and Family Affairs Committee of the Council of Europe, Doc. 9401. Available at: http://assembly.coe.int/ASP/Doc/XrefViewHTML.asp?FileID=9680&Language= en (accessed September 17, 2014).

Schottler, J.,Vogel, L., Chafetz, R., and Mulcahey, M. J. (2009). Patient and caregiver knowledge of autonomic dysreﬂexia among youth with spinal cord injury. Spinal Cord 47, 681–686. doi: 10.1038/sc.2009.12

Panicker, R. C., Puthusserypady, S., and Sun, Y. (2011). An asynchronous P300 BCI with SSVEP-based control state detection. IEEE Trans. Biomed. Eng. 58, 1781–1788. doi: 10.1109/TBME.2011.2116018

Schreuder, M., Riccio, A., Risetti, M., Dahne, S., Ramsay, A., Williamson, J., etal.

(2013). User-centered design in brain-computer interfaces-a case study. Artif. Intell. Med. 59, 71–80. doi: 10.1016/j.artmed.2013.07.005

Pasqualotto, E., Federici, S., and Belardinelli, M. O. (2012). Toward functioning and usable brain-computer interfaces (BCIs): a literature review. Disabil. Rehabil. Assist. Technol. 7, 89–103. doi: 10.3109/17483107.2011.589486

- Sellers, E. W., and Donchin, E. (2006a). A P300-based brain-computer interface: initial tests by ALS patients. Clin. Neurophysiol. 117, 538–548. doi: 10.1016/j.clinph.2005.06.027
- Sellers, E. W., and Donchin, E. (2006b). A P300-based brain-computer interface: initial tests by ALS patients. Clin. Neurophysiol. 117, 538–548. doi: 10.1016/j.clinph.2005.06.027

Pfurtscheller, G., Linortner, P., Winkler, R., Korisek, G., and Müller-Putz, G. (2009). Discrimination of motor imagery-induced EEG patterns in patients with complete spinal cord injury. Comput. Intell. Neurosci. 2009:104180. doi: 10.1155/2009/104180

Seyfert, S., and Straschill, M. (1982). [Electroencephalographic changes induced by baclofen]. EEG EMG Z. Elektroenzephalogr. Elektromyogr. Verwandte Geb. 13, 161–166.

Pfurtscheller, G., and Lopes da Silva, F. H. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol. 110, 1842–1857. doi: 10.1016/S1388-2457(99)00141-8

Shih, J. J., Krusienski, D. J., and Wolpaw, J. R. (2012). Brain-computer interfaces in medicine. Mayo Clin. Proc. 87, 268–279. doi: 10.1016/j.mayocp.2011.12.008

Pfurtscheller, G., Müller, G. R., Pfurtscheller, J., Gerner, H. J., and Rupp, R. (2003). ‘Thought’ – control of functional electrical stimulation to restore hand grasp in a patient with tetraplegia. Neurosci. Lett. 351, 33–36. doi: 10.1016/S03043940(03)00947-9

Siddall, P. J., Mcclelland, J. M., Rutkowski, S. B., and Cousins, M. J. (2003). A longitudinal study of the prevalence and characteristics of pain in the ﬁrst 5 years following spinal cord injury. Pain 103, 249–257. doi: 10.1016/S03043959(02)00452-9

Piccione, F., Giorgi, F., Tonin, P., Priftis, K., Giove, S., Silvoni, S., etal. (2006). P300-based brain computer interface: reliability and performance in healthy and paralysed participants. Clin. Neurophysiol. 117, 531–537. doi: 10.1016/j.clinph.2005.07.024

Silvoni, S., Volpato, C., Cavinato, M., Marchetti, M., Priftis, K., Merico, A., etal. (2009). P300-based brain-computer interface communication: evaluation and follow-up in amyotrophic lateral sclerosis. Front. Neurosci. 3:60. doi: 10.3389/neuro.20.001.2009

Pietzko, A., Dimpfel, W., Schwantes, U., and Topfmeier, P. (1994). Inﬂuences of trospium chloride and oxybutynin on quantitative EEG in healthy volunteers. Eur. J. Clin. Pharmacol. 47, 337–343. doi: 10.1007/BF00191165

Snoek, G. J., Mj, I. J., Hermens, H. J., Maxwell, D., and Biering-Sorensen, F. (2004). Survey of the needs of patients with spinal cord injury: impact and priority for improvement in hand function in tetraplegics. Spinal Cord 42, 526–532. doi: 10.1038/sj.sc.3101638

Pineda, J. A., Silverman, D. S., Vankov, A., and Hestenes, J. (2003). Learning to control brain rhythms: making a brain-computer interface possible. IEEE Transactions. Neural Syst. Rehabil. Eng. 11, 181–184. doi: 10.1109/TNSRE.2003.814445

Strait,M.,and Scheutz,M. (2014). What we can and cannot (yet) do with functional near infrared spectroscopy. Front. Neurosci. 8:117. doi: 10.3389/fnins.2014.00117

Vuckovic, A., Hasan, M. A., Fraser, M., Conway, B. A., Nasseroleslami, B., and Allan, D. B. (2014). Dynamic oscillatory signatures of central neuropathic pain in spinal cord injury. J. Pain 15, 645–655. doi: 10.1016/j.jpain.2014.02.005

Sutton, S., Braren, M., Zubin, J., and John, E. R. (1965). Evoked-potential correlates of stimulus uncertainty. Science 150, 1187–1188. doi: 10.1126/science.150.3700.1187

Waring, W. P. III, Biering-Sorensen, F., Burns, S., Donovan, W., Graves, D., Jha, A., etal. (2010).2009 review and revisions of the international standards for the neurological classiﬁcation of spinal cord injury. J. Spinal Cord Med. 33, 346–352.

Todorova, A., Vonderheid-Guth, B., and Dimpfel, W. (2001). Effects of tolterodine, trospium chloride, and oxybutynin on the central nervous system. J. Clin. Pharmacol. 41, 636–644. doi: 10.1177/00912700122010528

Wolpaw, J. R., Birbaumer, N., Mcfarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Tonin, L., Leeb, R., Tavella, M., Perdikis, S., and Millán, J. D. R. (2010). “The role of shared-control in BCI-based telepresence,” in Proceedings of 2010 IEEE International Conference on Systems, Man and Cybernetics, Istanbul, 1462–1466. doi: 10.1109/ICSMC.2010.5642338

Wolpaw,J.R.,Mcfarland,D.J.,andVaughan,T.M.(2000). Brain-computerinterface research at the Wadsworth Center. IEEE Trans. Rehabil. Eng. 8, 222–226. doi: 10.1109/86.847823

Toppi, J., Risetti, M., Quitadamo, L. R., Petti, M., Bianchi, L., Salinari, S., etal. (2014). Investigating the effects of a sensorimotor rhythm-based BCI training on the cortical activity elicited by mental imagery. J. Neural Eng. 11:035010. doi: 10.1088/1741-2560/11/3/035010

Zander, T. O., Lehne, M., Ihme, K., Jatzev, S., Correia, J., Kothe, C., etal. (2011). A dry EEG-system for scientiﬁc research and brain-computer interfaces. Front. Neurosci. 5:53. doi: 10.3389/fnins.2011.00053

Conflictof InterestStatement:Theauthordeclaresthattheresearchwasconducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

van den Berg, M. E., Castellote, J. M., Mahillo-Fernandez, I., and De PedroCuesta, J. (2010). Incidence of spinal cord injury worldwide: a systematic review. Neuroepidemiology 34, 184–192; discussion 192. doi: 10.1159/000279335

van den Honert, C., and Mortimer, J. T. (1979). The response of the myelinated nerve ﬁber to short duration biphasic stimulating currents. Ann. Biomed. Eng. 7, 117–125. doi: 10.1007/BF02363130

Received: 01 July 2014; accepted: 08 September 2014; published online: 24 September 2014. Citation: Rupp R (2014) Challenges in clinical applications of brain computer interfaces in individuals with spinal cord injury. Front. Neuroeng. 7:38. doi: 10.3389/fneng.2014.00038 This article was submitted to the journal Frontiers in Neuroengineering. Copyright©2014Rupp. Thisisanopen-accessarticledistributedunderthetermsof the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) or licensor are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

Vanacker, G., Millán, J. D. R., Lew, E., Ferrez, P. W., Galán, F., Philips, J., etal. (2007). Context-based ﬁltering for assisted brain-actuated wheelchair driving. Comput. Intell. Neurosci. 2007:25130. doi: 10.1155/2007/25130

Vanhooydonck, D., Demeester, E., Nuttin, M., and Van Brussel, H. (2003). “Shared control for intelligent wheelchairs: an implicit estimation of the user intention,” in Proceedings of the 1st International Workshop Advances in Service Robot (ASER ’03), Bardolino, 176–182.

Vialatte, F. B., Maurice, M., Dauwels, J., and Cichocki, A. (2010). Steady-state visually evoked potentials: focus on essential paradigms and future perspectives. Prog. Neurobiol. 90, 418–438. doi: 10.1016/j.pneurobio.2009.11.005

