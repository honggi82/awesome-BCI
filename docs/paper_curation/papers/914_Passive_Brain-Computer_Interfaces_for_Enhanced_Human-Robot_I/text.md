REVIEW published: 02 October 2020 doi: 10.3389/frobt.2020.00125

[Figure 1]

# Passive Brain-Computer Interfaces for Enhanced Human-Robot Interaction

Maryam Alimardani1* and Kazuo Hiraki2

1 Department of Cognitive Science and Artiﬁcial Intelligence, School of Humanities and Digital Sciences, Tilburg University, Tilburg, Netherlands, 2 Department of General Systems Studies, Graduate School of Arts and Sciences, The University of Tokyo, Tokyo, Japan

Brain-computer interfaces (BCIs) have long been seen as control interfaces that translate changes in brain activity, produced either by means of a volitional modulation or in response to an external stimulation. However, recent trends in the BCI and neurofeedback research highlight passive monitoring of a user’s brain activity in order to estimate cognitive load, attention level, perceived errors and emotions. Extraction of such higher order information from brain signals is seen as a gateway for facilitation of interaction between humans and intelligent systems. Particularly in the ﬁeld of robotics, passive BCIs provide a promising channel for prediction of user’s cognitive and affective state for development of a user-adaptive interaction. In this paper, we ﬁrst illustrate the state of the art in passive BCI technology and then provide examples of BCI employment in human-robot interaction (HRI). We ﬁnally discuss the prospects and challenges in integration of passive BCIs in socially demanding HRI settings. This work intends to inform HRI community of the opportunities offered by passive BCI systems for enhancement of human-robot interaction while recognizing potential pitfalls.

Edited by: Luca Tonin,

University of Padua, Italy Reviewed by: Muhammad Jawad Khan, National University of Sciences and Technology (NUST), Pakistan

Xiaogang Chen, Institute of Biomedical Engineering

Keywords: brain-computer interface (BCI), passive BCIs, human-robot interaction (HRI), cognitive workload estimation, error detection, emotion recognition, EEG, social robots

(CAMS), China Matteo Spezialetti,

University of L’Aquila, Italy *Correspondence:

## INTRODUCTION

Maryam Alimardani m.alimardani@uvt.nl

For generations, the idea of having intelligent machines that can read people’s minds and react without direct communication had captured human’s imagination. With recent advances in neuroimaging technologies and brain-computer interfaces (BCI), such images are ﬁnally turning into reality (Nam et al., 2018). BCIs are the systems that decode brain activity into meaningful commands for machines, thereby bridging the human brain and the outside world. BCIs are primarily developed as a non-muscular communication and control channel for patients suﬀering from severe motor impairments (Millán et al., 2010; Chaudhary et al., 2015; Lebedev and Nicolelis, 2017; Chen et al., 2019). For instance, a BCI-actuated wheelchair or exoskeleton can assist a patient with ALS or spinal cord injury to regain mobility (Kim et al., 2016; Benabid et al., 2019). Similarly, locked-in patients can be equipped with a BCI system in order to eﬀectively communicate with external world (Sellers et al., 2014; Hong et al., 2018; Birbaumer and Rana, 2019). Stroke patients have also demonstrated eﬀective restoration of motor functions and improvement of life quality after they were trained with a BCI-control task in a neurological rehabilitation session (Soekadar et al., 2015).

Specialty section: This article was submitted to Computational Intelligence in

Robotics, a section of the journal

Frontiers in Robotics and AI

Received: 05 March 2020 Accepted: 05 August 2020

Published: 02 October 2020 Citation:

Alimardani M and Hiraki K (2020) Passive Brain-Computer Interfaces for

Enhanced Human-Robot Interaction. Front. Robot. AI 7:125. doi: 10.3389/frobt.2020.00125

However, with the growing popularity of BCIs, new application corners outside of the medical ﬁeld have emerged for healthy users (Allison et al., 2012; Van Erp et al., 2012; Nam et al., 2018). One

of the mainstream applications is the integration of BCIs with other interactive technologies such as virtual reality (VR) and computer games (Lécuyer et al., 2008; Coogan and He, 2018). Several prototypes have already been developed that enable a user to either navigate through a virtual space or manipulate a digital object only by means of thoughts (Friedman, 2015). The combination of immersive technologies and BCIs entails a two-way beneﬁt for researchers in that the BCI system provides a new form of control channel over the environment, thus changing the user experience, and virtual environments serve as a suitable platform for BCI research as they oﬀer a safe, engaging, and cost-eﬀective tool for the design of BCI experiments and neurofeedback (Allison et al., 2012; Lotte et al., 2012).

In addition to immersive environments, BCIs have also been utilized in combination with physical robots in order to induce a sense of robotic embodiment and remote presence (Alimardani et al., 2013; Beraldo et al., 2018). In these setups, users control a humanoid robotic body and navigate through the physical space by means of their brain activity while they can see through the robot’s eyes. Such interactions often lead to a feeling of telepresence and the experience of losing boundary between the real body and the robot’s body (Alimardani et al., 2015), paving the way for research in cognitive neuroscience and neural prosthetics (Pazzaglia and Molinari, 2016).

In all the above-mentioned examples, the brain activity features extracted for the BCI classiﬁer are either voluntarily induced by the user (active control) or measured as a response to an external stimulus (reactive control). Such BCI systems that require users to get involved in a cognitive task and provide explicit commands are referred to as active BCIs (Zander and Kothe, 2011; Lightbody et al., 2014). On the other hand, BCIs that are event driven and measure brain responses to a visual, auditory or haptic stimulus are called reactive BCIs (Zander and Kothe, 2011). However, there is a third group of BCIs that drive their outputs from spontaneous brain activity without the need from the user to perform speciﬁc mental tasks or receive stimuli. These BCI systems, which normally monitor longer epochs of brain activity for detection of a cognitive state change or emotional arousal, are called passive BCIs (Zander and Kothe, 2011; Aricò et al., 2018). An example of this is a system that monitors a driver’s neural dynamics in real-time and alarms him/her in the case of drowsiness detection (Lin C. T. et al., 2010; Khan and Hong, 2015).

Passive BCIs primarily aim at detecting unintentional changes in a user’s cognitive state as an input for other adaptive systems (Zander et al., 2010; Aricò et al., 2016). For instance, in the driving example, the output of the BCI system that evaluates driver drowsiness can alternatively be used for administration of the temperature in the car or the volume of the sound system in order to increase alertness of the driver (Liu et al., 2013). Similarly, a BCI that extracts information about a user’s ongoing cognitive load and aﬀective states oﬀers numerous applications in the design of adaptive systems and social agents that would adjust their behavior to the user’s ongoing mental state, without distracting the user from the main task, thereby enriching the quality of interaction and performance (Szaﬁr and Mutlu, 2012;

Alimardani and Hiraki, 2017; Zander et al., 2017; Ehrlich and Cheng, 2018).

In this article, we mainly discuss passive BCIs in the context of human-computer and human-robot interaction. In section BCIs and Cognitive/Aﬀective State Estimation, we ﬁrst lay out the state of the art in passive BCIs by brieﬂy reviewing existing studies that attempted detection of cognitive and aﬀective state changes from brain responses. We restricted our literature search to studies that adopted electroencephalography (EEG) signals for development of the BCI classiﬁer. Given its mobility, high temporal resolution, and relatively low price, EEG is considered as a feasible noninvasive brain imaging technique that can be deployed into a wide variety of applications including human-robot interaction. In section BCIs and Human-Robot Interaction, we focus on passive BCI-robot studies that used cognitive and aﬀective state measures as a neurofeedback input for a social or mechanical robot, thereby optimizing their response and behavior in a closed-loop interaction. In the last section, we discuss the prospects and challenges that are faced in the employment of passive BCIs in real-world human-robot interaction.

BCIs AND COGNITIVE/AFFECTIVE STATE ESTIMATION

In neuroscientiﬁc literature, cognitive state estimation refers to the quantiﬁcation of neurophysiological processes that underlie attention, working-memory load, perception, reasoning, and decision-making, while aﬀective computing targets assessment of the emotional experience. BCI systems that decode covert information in the brain signals regarding these internal processes can establish an implicit communication channel for an adaptive human-technology interaction, presenting novel applications in the domains of education, entertainment, healthcare, marketing, etc. (Van Erp et al., 2012; Blankertz et al., 2016; Krol and Zander, 2017; Aricò et al., 2018). We identiﬁed three main directions for assessment of cognitive and aﬀective states in EEG-based passive BCIs; (1) detection of attention and mental fatigue, (2) detection of errors, and (3) detection of emotions. In the following, we describe the current state of the art in each of these domains, laying out a foundation for future employment of passive BCIs in human-robot interaction.

Detection of Attention and Mental Fatigue

As discussed in the drowsy driver example, monitoring realtime mental workload and vigilance is of particular importance in safety-critical environments (Lin C. T. et al., 2010; Khan and Hong, 2015; Aricò et al., 2017). Non-invasive BCIs that detect drops in attention level and increased mental fatigue can be utilized in a broad range of operational environments and application domains including aviation (Aricò et al., 2016; Hou et al., 2017) and industrial workspaces (Schultze-Kraft et al., 2012) where safety and eﬃciency are important, as well as educational and healthcare setups where the system can provide feedback from learners to a teacher (Ko et al.,

2017; Spüler et al., 2017), evaluate sustained attention in elearning platforms (Chen et al., 2017), and execute attention training for clinical patients who suﬀer from attention deﬁcit hyperactivity disorder (ADHD) (Lim et al., 2019). It is even suggested that detection of attention level can be employed in a hybrid BCI system in which an attention classiﬁer is integrated with other BCI algorithms in order to conﬁrm users’ focus on the BCI task and validate the produced response, thereby yielding a more reliable and robust performance (Diez et al., 2015).

Multiple algorithms have already been proposed to quantify the level of alertness and mental workload within EEG brain activity. A large number of these models rely on frequency domain features such as theta, alpha and beta band powers, for estimation of attention level and mental fatigue experienced by the user (Lin C. T. et al., 2010; Roy et al., 2013; Diez et al., 2015; Khan and Hong, 2015; Aricò et al., 2016; Lim et al., 2019). On the other hand, some studies have examined non-linear complexity measures of time series EEG signals such as entropy (Liu et al., 2010; Min et al., 2017; Mu et al., 2017), promoting a fast and less costly method for real-time processing. Although not very common, a few studies have also proposed the usage of event-related potentials (ERP), such as non-target P300, in development of passive classiﬁers given that such brain responses are aﬀected by both attention and fatigue and thus can provide a measure of target recognition processes (Kirchner et al., 2013; McDaniel et al., 2018).

In addition to spectral and temporal information carried by EEG signals, spatial features such as brain regions from which the signals were collected have been shown important in the detection of diﬀerent mental state changes (Myrden and Chau, 2017). Although reported results are not always consistent, there is a general consensus on the role of frontal lobe in discrimination of cognitive workload and task diﬃculty (Zarjam et al., 2015; Dimitrakopoulos et al., 2017), prefrontal and central lobes in detection of fatigue and drowsiness (Min et al., 2017; Ogino and Mitsukura, 2018), and posterior areas (particularly posterior alpha band) in estimation of visuospatial attention (Ko et al., 2017; Myrden and Chau, 2017). It is worth noting that functional connectivity between diﬀerent brain regions is also suggested in the literature as an index for estimation of engagement and attention (Dimitriadis et al., 2015; Dimitrakopoulos et al., 2017), although due to computational cost it poses limitations on realtime implementation.

Detection of Errors

Failures during technology usage and outputs that deviate from expectation can become a source of dissatisfaction and additional cognitive workload for the user. Unintentional mistakes made by the human or erroneous behavior presented by the system can generate user frustration and aggravate human-system interaction (Zander et al., 2010). Such negative repercussions can be prevented by automatic detection and feedback of errors, as perceived by the user, for online correction or adaptation of system characteristics while the user is still involved in the interaction (Zander et al., 2010; Chavarriaga et al., 2014; Krol and Zander, 2017).

When a user recognizes a mismatch from expectation, an error-related potential (ErrP) is generated in the EEG signals. A passive BCI system that extracts this information in real-time can be used in development of hybrid and adaptive systems that optimize the performance of the user either by removing the erroneous trials (Ferrez and Millán, 2008; Schmidt et al., 2012; Youseﬁ et al., 2019), or by modifying the classiﬁcation parameters through online learning of the BCI classiﬁer (Krol and Zander, 2017; Mousavi and de Sa, 2019), or by adjusting the task diﬃculty level to diﬀerent individuals in order to improve engagement and motivation (Mattout et al., 2015). For instance, Ferrez and Millán (2008) combined a motor imagery BCI with an error detection algorithm that looked for an ErrP immediately after each trial and ﬁltered out trials that contained an error-related response. Their results displayed a signiﬁcant improvement of BCI performance in real-time by reducing the classiﬁcation error rate from 30 to 7%. Similarly, Schmidt et al. (2012) combined online detection of ErrPs with a BCI speller and reported 49% improvement in the mean spelling speed. In a recent report, Dehais et al. (2019) presented a passive BCI classiﬁer for prediction of auditory attentional errors during a real ﬂight condition, proposing future smart cockpits that would adapt to pilots’ cognitive needs.

A unique feature of ErrPs is that they would arise in response to any form of discrepancy during interaction/task execution including when the user realizes a self-made error (response ErrP), when s/he is informed about the error through some type of feedback (feedback ErrP), and even when the user senses an error made by a third party (observation ErrP) (Ferrez and Millán, 2005; Gürkök and Nijholt, 2012; Vi et al., 2014). This permits detection and management of errors in any form and at any time during the interaction, promoting closed-loop passive BCIs not only as an eﬃcient and seamless tool for online evaluation of user performance but also as a secondary communication tool in multi-user collaborative environments such as emergency rooms (Vi et al., 2014) where agile and high-risk decision making is required (Poli et al., 2014).

Additionally, recent eﬀorts suggest that diﬀerent kinds of errors generate diﬀerent ErrPs, allowing discrimination of error severity and error types (Spüler and Niethammer, 2015; Wirth et al., 2019) based on temporal, spectral, and spatial information in the EEG waveforms. However, the downside of this approach is that, in most cases, the ErrP classiﬁer relies on an event-locked paradigm in which ErrPs can only be extracted within a ﬁxed window from a speciﬁed trigger. In real-world applications, the information regarding stimulus time or origin of the error is often unavailable and the latency of user responses may vary across individuals and tasks. Therefore, future integration of such passive BCIs with natural human-agent interactions calls for further developments on self-paced algorithms that make asynchronous error detection possible at any time during the interaction (Lightbody et al., 2014; Spüler and Niethammer, 2015; Youseﬁ et al., 2019).

Detection of Emotions

With advancement of commercially available wearable sensors, estimation of human emotions from ongoing biosignals has received increased attention in recent years (Al-Nafjan et al.,

2017; Shu et al., 2018; García-Martínez et al., 2019; Dzedzickis et al., 2020). Emotions are particularly important in the design of intelligent and socially interactive systems as they enable the digital agents to generate a well-suited behavior and establish an aﬀective loop with the human partner (Paiva et al., 2014; Ehrlich et al., 2017). Compared to conventional methods of social signal processing and aﬀective computing (such as voice and image processing), biosignals present the advantage of containing spontaneous and less controllable features of emotions. Emotions entail three aspects; physiological arousal, conscious experience of the emotion (subjective feeling) and behavioral expression (Alarcao and Fonseca, 2017). Voice and face recognition technologies can only capture the third aspect, i.e., overt behavioral expression of emotion, whereas brain activity can inform us about the neurophysiological and cognitive processes that generate and lead to such emotional states (Mühl et al., 2014a).

A major challenge in classiﬁcation of emotions from brain activity is that there is not a unique computational method for extraction and mapping of emotion-related features. There are two theories in the modeling of emotions; discrete model and dimensional model (Kim et al., 2013). The former deﬁnes emotions as a set of categorical aﬀective states that represent core emotions such as happiness, sadness, anger, disgust, fear, and surprise (Lin Y. P. et al., 2010; Jenke et al., 2014). The latter maps emotions on either a two-dimensional valencearousal space (Posner et al., 2005; Atkinson and Campos,

- 2016) or a three-dimensional valence-arousal-dominance space (Mehrabian, 1996; Reuderink et al., 2013). The discrete model is more popular among BCI developers as it reduces the problem of dimensionality, however it does not consider that the same emotion may manifest on diﬀerent scales of arousal, valence and dominance. The dimensional model provides continuity as it quantiﬁes emotions on each dimension (valence ranging from positive to negative, arousal ranging from calm to excited and dominance ranging from in-control to submission). Particularly, the 2D model has been previously used in multiple EEG studies (Liberati et al., 2015; Al-Nafjan et al., 2017; Mohammadi et al.,
- 2017), however in these studies, the dimensionality is often simpliﬁed again by means of clustering emotions across the valence-arousal coordinates (e.g., fear as negative valence, high arousal or happiness as positive valence, high arousal), which bears the risk of grouping diﬀerent emotions that share the same valence and arousal levels (e.g., anger and fear) in one cluster (Liberati et al., 2015).

Another challenge in the development of emotional BCIs is the diverse elicitation strategies that exist in the aﬀective computing literature. Multiple types of stimuli including aﬀective pictures, sounds, video fragments and music have been used in the past in order to induce emotional responses (Al-Nafjan et al., 2017). In addition to the lack of consistency among reported results and available EEG datasets, an inherent problem with these forms of stimuli is that there is no evidence whether the induced emotion is a natural aﬀective state or just a reactive response to the stimulus. To counter this issue, some studies have employed a self-induced strategy such as recall of autobiographical emotional memory (Chanel et al., 2009;

Iacoviello et al., 2015) or imagination of the emotion by means of verbal narratives (Kothe et al., 2013). This method entails other problems; the self-induced emotions are inevitably weaker than those induced by external stimuli, and users are prone to distraction during the task as it is diﬃcult to maintain mental imageries for a long period (Chanel et al., 2009).

It is worth mentioning that emotions are more than just an aﬀective state for social interaction and adaptive environments; they may also inﬂuence other cognitive functions. For instance, frustration can extend negative impacts on attention, decisionmaking, learning, and response accuracy. Indeed, past research has shown that aﬀective states such as stress, anxiety and frustration can inﬂuence BCI performance in estimation of mental workload and attention (Mühl et al., 2014b; Myrden and Chau, 2015; Lotte et al., 2018). Thus, it can be expected that an adaptive multimodal BCI system that identiﬁes users’ aﬀective states and regulates tasks accordingly would improve user performance and validity of the system in the long term (Gürkök and Nijholt, 2012).

To sum up, there have been several BCI algorithms proposed for detection of aﬀective state changes from EEG signals (Alarcao and Fonseca, 2017), however, automatic recognition of emotions during ecologically valid tasks and natural interactions remains a challenge, hindering deployment of aﬀective BCIs in other platforms such as human-robot interaction. Future research should attend currently existing issues such as insuﬃcient classiﬁcation accuracy, inconsistent computational and elicitation techniques, as well as development of BCI models that can extract emotions in an unobtrusive and asynchronous manner over a long period of time.

BCIs AND HUMAN-ROBOT INTERACTION

With more integration of robots into our daily life, the necessity for them to function as social and assistive companions in realworld environments such as schools and healthcare facilities becomes eminent. In addition to human’s intentions and control commands, it is crucial for the robots to estimate the emotional states of a human partner in order to be socially responsive, engage longer with users and promote natural HRI (Ficocelli et al., 2015). More importantly, estimation of workload, anxiety and errors is crucial for ergonomic and safe human-robot collaboration in both domestic and industrial spaces (Ajoudani et al., 2018). In this section, we particularly discuss studies that have employed BCIs for passive detection of cognitive and aﬀective states of a human user in order to eﬀectively adapt the behavior of a robot in a closed-loop interaction with the human partner (Figure 1).

We restricted our literature search to only non-invasive BCI studies that passively extracted user’s cognitive and aﬀective states during interaction with a physical robot, therefore, articles that employed active BCIs for motion control (e.g., motor-imagery based robot operation) or reactive BCIs for intentional selection of behavior for a robotic interface (e.g., robot manipulation triggered by event-related P300 or Steady State Visually Evoked Potential SSVEP) were not included. Another inclusion criterion

|[Figure 2]<br><br>FIGURE 1 | Closed-loop human-robot interaction using passive BCIs.|
|---|

- TABLE 1 | The inclusion and exclusion criteria as used for the selection of BCI-HRI studies in section BCIs and Human-Robot Interaction. Parameters Inclusion criteria Exclusion criteria

Type of BCI Passive BCIs (hybrid with other BCI types acceptable)

Type of signal EEG (hybrid with other signal types acceptable)

Type of interaction Interaction with physical robots (e.g., social robots, arm robots)

Type of analysis Real-time classiﬁcation/ feedback to the robot

Active or reactive BCIs (e.g., motor imagery, ERP, SSVEP)

fNIRS, fMRI, MEG

Interaction with virtual avatars, computer games

Ofﬂine analysis of brain signals captured during HRI

was usage of AI-powered predictive models together with EEG signals in the study, where a passive BCI classiﬁer was used (or its development was attempted) during real-time interaction with a robot. Neuroscience research in which only brain oscillation patterns associated with robot interaction are reported were either excluded or already reported in section BCIs and Cognitive/Aﬀective State Estimation. Finally, the study should have reported a passive BCI interaction with a physical robot; interactions with virtual or simulated agents were excluded as the deﬁnition of a simulated agent is very board and incorporates human-computer interaction and game applications of passive BCIs. The inclusion and exclusion criteria deﬁned for review of BCI-HRI studies in this section are summarized in Table 1.

Our search resulted in a total of 10 studies as shown in Table 2. In the following, we brieﬂy describe the methodology and outcomes of each listed study.

Szaﬁr and Mutlu (2012) reported an interesting study in which a humanoid robot monitored students’ EEG signals during storytelling and gave them attention-evoking immediacy cues (either in verbal or non-verbal form) whenever engagement drops were detected. In doing so, they extracted EEG levels in alpha, beta and theta frequency bands and smoothed them into an engagement signal that would represent attention levels. Every

time the attention level went below a pre-deﬁned threshold, the robot displayed immediacy cues such as increased spoken volume, increased eye contact, and head-nodding. Their results showed that participants who experienced interaction with an adaptive BCI-driven robot had a signiﬁcantly better recall of the story details than those who participated in an interaction with randomly presented immediacy cues. In addition to this, female participants reported a more favorable evaluation of the robot behavior, in terms of improved motivation and rapport, in the BCI condition compared to the random condition. The results of this study highlight the beneﬁts of BCIs in interactive educational setups where real-time detection of user disengagement and attention drop can be compensated by means of an embodied social agent.

Kirchner et al. (2013) employed passive classiﬁcation of eventrelated potential P300 in an adaptive human-robot interaction. They reported a brain reading (BR) system that implicitly extracted p300 during teleoperation of an exoskeleton arm whenever an important stimulus was presented to the user. They used the evoked potential amplitude as an indicator of successful stimuli recognition by the user. If the response did not contain P300 or the potential was not strong enough, it implied that the user had missed the important information that was presented and thus the system repeated the stimuli. Authors found a reduced stress level in subjects when BR was embedded in the control interface, recommending their approach as a promising way to improve the functionality of interactive technical systems.

Ehrlich et al. (2014) proposed an EEG-based framework for detection of social cues such as gaze by a humanoid robot as a measure for social engagement. They instructed subjects to either wait for the robot to make eye-contact with them or to intentionally generate brain patterns for the robot to initiate eyecontact with them (inﬂuence the robot’s behavior). By extracting frequency band powers as discriminating features in an oﬄine analysis, they could ﬁnd high classiﬁcation performance between the two conditions. Such predictive model could be implemented in a human-robot interaction in order to enable the robot to estimate its social role and adapt its behavior to the expectations of the human partner.

Iturrate et al. (2015) introduced a reinforcement learning (RL) algorithm that learned optimal motor behavior of a robotic arm based on observation ErrPs carried in the brain signals of a human viewer. The BCI classiﬁer decoded reaching actions as erroneous whenever ErrPs were present. The non-ErrP trials were then employed as an online reward for the RL algorithm. Their approach improved the number of learned actions and control policies compared to random rewards. Authors suggest their algorithm for future application in neuroprosthetics in which implicit input from the patient can optimize the behavior of an artiﬁcial limb for goal-oriented movements.

Kim et al. (2017) conducted a study similar to Iturrate et al. (2015) in which they trained a RL algorithm based on the user’s ErrPs in a gesture recognition task. They prepared two scenarios; (1) when a simulated arm robot recognized and copied user’s gestures, and (2) when a real arm robot recognized and copied user’s gestures. In both scenarios, the ErrP classiﬁer used the correct mappings as a reward for the RL algorithm. They

- TABLE 2 | List of articles in the literature that used a passive BCI classiﬁer for extraction of user’s cognitive and affective state during interaction with a physical robot.

References EEG feature BCI classiﬁer output Adaptive HRI

Szaﬁr and Mutlu (2012) Spectral band powers Attention drops in user during storytelling by a robot The robot provided attention-evoking cues Kirchner et al. (2013) Absence of P300 Stimuli recognition during teleoperation of an

The robot controller repeated stimuli or changed response window if the user missed the stimuli

exoskeleton arm

Ehrlich et al. (2014) Spectral band powers User intention to initiate eye-contact with a robot None Iturrate et al. (2015) Error-related potential Erroneous motor behavior by an artiﬁcial robotic arm in a

The robot arm controller learned correct and incorrect behavior through reinforcement learning

reaching task

Kim et al. (2017) Error-related potential Wrong mapping between user’s gestures and robot’s action

The robot updated action-selection strategy and learned gesture meaning through reinforcement learning

Salazar-Gomez et al. (2017) Error-related potential Erroneous robot motion in a binary reaching task The robot switched trajectory based on the observer’s EEG response

- Ehrlich and Cheng (2018) Error-related potential Mismatch in gaze behavior The robot adapted gaze behavior based on decoded ErrPs
- Ehrlich and Cheng (2019) Error-related potential Erroneous robot head movement as a response to a directional key press by the user

None

Shao et al. (2019) Spectral asymmetry Emotional valence (positive vs. negative) during exercise with a robot coach

The robot provided verbal and non-verbal feedback based on the user’s affect and engagement level

Lopes-Dias et al. (2019) Error-related potential Erroneous arm robot movement when the robot should have imitated human hand movement.

The robot would give control to human again to correct his/her movement

showed that both simulated and real robots could eﬀectively learn gestures from the human instructor with a high online ErrP detection accuracy (90 and 91%, respectively). However, not surprisingly, the learning curve was diﬀerent across subjects based on the performance of ErrP classiﬁer. Past studies have shown that ERP-based BCI performance varies across individuals based on psycho-cognitive parameters (Sprague et al., 2016) suggesting that ErrP-based BCIs may require subject-speciﬁc calibration and training when integrated within an HRI setting.

Salazar-Gomez et al. (2017) introduced a closed-loop control interface for automatic correction of reaching behavior of a robotic arm. They recorded EEG signals from a human observer while the robot was performing a binary object selection task after a cue presentation. They used ErrP responses as a real-time feedback for the robot to switch trajectory if the selected choice was not compatible with the cue. Despite the sound methodology of this study, authors only reported classiﬁcation results from four subjects, which makes it diﬃcult to draw ﬁrm conclusions. Also, no reports were made regarding user perception of the interaction and attitude toward the robot in open-loop vs. closedloop HRI. However, an interesting ﬁnding in this study was the presence of a secondary ErrP in the closed-loop interaction when the human observed an incorrect interpretation of the feedback by the robot (robot not obeying the human or switching to the wrong trajectory due to misclassiﬁcation). This suggests the design of new BCI paradigms where secondary and further ErrPs can be incorporated in continuous interactions until an optimal behavior is achieved (Cruz et al., 2018).

Ehrlich and Cheng (2018, 2019) reported two consecutive studies in which they used ErrP signals for detection of mismatch between user’s intended gaze and actual robot’s gaze (Ehrlich

and Cheng, 2018) and user’s intended head movement and actual robot’s head movement (Ehrlich and Cheng, 2019). In the former study, they used a closed-loop interaction (adaptive behavior by the robot) where the user ﬁrst guessed the direction of robot gaze from three available choices and then the robot performed a random gaze behavior which was followed by an updated behavior based on the ErrP classiﬁer outcome. Using a learning paradigm for the robot’s gaze policy, they showed that a mutual adaptation between the human and robot’s behavior emerged, leading to a relatively high classiﬁcation performance and more eﬃcient interaction. In the latter study (Ehrlich and Cheng, 2019), authors again used a guessing game to compare the observability and decodeability of ErrP responses to two experimental stimuli; an incongruent robot movement vs. an incongruent curser movement. In the ﬁrst condition, participants guessed the robot head movement from three possible directions (left, right, up) using arrow key-presses, and watched the robot perform a random action. In the second condition, they again guessed a possible direction but watched a curser moving either toward or away from that direction on a computer screen. Although they found a satisfactory classiﬁcation accuracy (69%) in the HRI scenario, they observed that the classiﬁcation accuracy for ErrP responses was signiﬁcantly higher in the cursor scenario (90%), indicating more sensitivity of ErrPs to visually simple cues compared to contextual robot actions.

Shao et al. (2019) used a low-cost EEG (InteraXon Muse 2016) together with heart rate and motion sensors during interaction with a health coach humanoid robot. They extracted EEG frequency band powers in order to classify the emotional valence of the user during exercise with the robot. The robot then presented an online positive or negative feedback (happy,

interested, worried, and sad) based on the user’s aﬀect (positive or negative) and engagement level (engaged or not engaged). The participants of their study reported a high acceptance and perceived usability for the robot, however the robot was tested in a non-controlled experiment (no other condition was compared with the above scenario) and the classiﬁcation results for the aﬀect recognition model was not particularly high (71%), therefore it is possible that the reported results were merely due to the novelty eﬀect caused by the robot presence, and not emotional awareness and adaptive feedback during the interaction.

Finally, Lopes-Dias et al. (2019) attempted asynchronous decoding of ErrPs during online control of an arm robot. Participants had to move their own hand according to a binary stimuli on the screen and using a motion capture system, the robot was expected to copy the same movement in the physical world. In case the hand movement was not detected correctly, an ErrP signal was detected and the robot allowed the user to correct the error. The major ﬁnding of this study was the possibility of asynchronous detection of ErrPs using a sliding window during online robot operation. Authors do not discuss their results in the context of human-robot interaction and a possible embodiment eﬀect (Alimardani et al., 2013), however similar to Salazar-Gomez et al. (2017), they observed secondary ErrPs in some participants which conﬁrms the applicability of these later potentials in improvement of robot performance.

Although, this section only focused on EEG-based passive BCIs for the purpose of HRI, it is worth mentioning the potential of other brain imaging techniques such as fNIRS (Canning and Scheutz, 2013) in passive evaluation of user responses during robot interaction, for instance, detection of cognitive workload during multitasking with two robots (Solovey et al., 2012) or detection of aﬃnity and eeriness in robot appearance (Strait and Scheutz, 2014). Additionally, insights can be driven from passive BCI studies with simulated agents and teleoperated robots (Esfahani and Sundararajan, 2011; Cavazza et al., 2015; Aranyi et al., 2016; Zander et al., 2017) to further inform the HRI community of the possible exploitation avenues.

Altogether, passive BCIs show promise in the design of optimal robot behavior by means of indirect communication from the human partner. Our literature review shows that detection of erroneous robot behavior using ErrP signals is the most popular paradigm for integration of passive BCIs in HRI settings. Contrary to our expectation, there were very few studies that employed detection of mental workload or emotions for adaptive social behavior in HRI. This conﬁrms that despite the great eﬀort of AI community in developing several classiﬁcation models for EEG-based emotion and cognitive state prediction, real-time incorporation of these models in a closedloop interaction with physical robots are yet not adequately explored. This gap should be addressed by BCI and HRI researchers in the future, thereby creating a synergy between the two domains for promotion of socially intelligent and adaptive robots.

## PROSPECTS AND CHALLENGES

As discussed in previous sections, passive BCIs oﬀer a promising means to objectively monitor cognitive and aﬀective states of a technology user either as an oﬄine evaluation metric of the user’s performance or as a communication modality for closed-loop adaptive interaction. This puts forward application of passive BCIs in neuroergonomic HRI (Lotte and Roy, 2019) where potential mental overload, attention drops, negative emotions, and human errors can be prevented or managed in an online and unobtrusive manner, thereby increasing the interactivity between the user and the robot and facilitating their collaboration (Krol et al., 2018). Meanwhile, more research is required in the ﬁeld of HRI to formulate appropriate design principles for contextaware alignment of the robot behavior with human expectations, needs and conventions, once such higher order information from the user is available (Rossi et al., 2017; Sciutti et al., 2018).

Another direction toward future collaboration between passive BCI and HRI research could be development of social robots that assist neurofeedback training for augmented cognition or sustenance of a desirable psychological state (Anzalone et al., 2016; Alimardani and Hiraki, 2017; Alimardani et al., 2018, 2020; Tsiakas et al., 2018; Cinel et al., 2019). One of the main problems with the traditional neurofeedback training paradigms is that the changes in brain features are usually presented to the users through auditory or visual feedback. This lacks engagement with the interface, which makes the training after a short while tedious. Recent works have replaced the old protocol with interactive computer games (Mishra et al., 2016) and immersive virtual environments (Kosunen et al., 2016). However, these applications require steady visual attention toward a computer screen or placement of a head-mounted display over the EEG electrodes that can be intrusive to the user and cause cybersickness. A social robot on the other hand, induces a feeling of co-presence, mind perception, and emotional support (Alimardani and Qurashi, 2019), which can positively inﬂuence performance, motivation, and social interaction during a training program (Wiese et al., 2017; Sinnema and Alimardani, 2019; Alimardani et al., 2020). Past research has shown that the physical embodiment of an agent generates a more natural, eﬃcient, and joyful communication during elderly cognitive training (Tapus et al., 2009) as well as a higher learning gain during tutoring interactions (Leyzberg et al., 2012). Therefore, it is expected that a robot-guided cognitive training would extend similar beneﬁts compared to previous non-social environments (Pino et al., 2019).

Although passive BCIs provide substantial opportunity for optimization of performance and interactivity in HRI, their advantages are often mitigated by several limitations with respect to real-world implementation. One of the general challenges in the usage of BCIs in real-world conditions is the high cost and long preparation time that is required for the hardware setup (electrode placement) and software tuning (individualized calibration). Recent development of wireless EEG caps and lowcost commercial headsets has substantially reduced the setup

time for real-world recordings, however they often come at the cost of precision and reliability. Also, there have been attempts in reducing calibration time by means of machine learning techniques and adaptive classiﬁers that extract common features among all users (Lotte, 2015), known as inter-subject associativity (Saha and Baumert, 2019). On the other hand, deep learning methods have been suggested for automatic learning of representations in the brain activity, thereby reducing the pre-processing and manual feature extraction that is required for BCI classiﬁer training (Nagel and Spüler, 2019; Tanveer et al., 2019). For BCI technology to become mainstream and be employed by non-experts in other research domains, we must reduce the cost of equipment use while improving the quality of recording and precision of algorithms. Hence, further advancement in wearable sensor technology as well as progress in signal processing techniques and computational modeling of brain activity is required for the BCIs to be ﬁnally deployed in every-day use.

Another constraint in employing BCIs in real-world scenarios is vulnerability of BCI output to external noise (Minguillon et al., 2017). In most BCI studies, participants are instructed to relax during the recording and avoid unnecessary movements; nevertheless the online performance of these systems is yet far from ideal due to uncontrolled concomitant stimulus in the environment and diverse neurophysiological dynamics across individuals. In the case of passive BCIs, this is an even more severe issue as the user’s involvement in another task or integration of the BCI system with other types of technology introduces new artifacts from the environment resulting in undesirable outcome (Zander et al., 2010). Such misclassiﬁcations can become particularly critical in the HRI scenarios, as poor performance from the system will produce unwanted behavior from the robot, thereby harming the interaction quality and diminishing the expected eﬀects. A proposed solution for this problem is combination of multiple brain imaging modalities, such as fNIRS and EEG, to develop hybrid BCIs that beneﬁt from both high temporal and high spatial resolution and hence can provide better accuracy and process more commands from the user (Hong and Khan, 2017; Dehais et al., 2018). Similarly, combination of brain signals with other physiological data such as electromyography (EMG) or electrooculography (EOG) can help detect and reduce the eﬀect of noise and increase the number of control commands necessary for multi-task control (Hong and Khan, 2017; Zhang et al., 2019).

In the same vein, care must be taken when collecting data for development of passive BCIs models in complex environments where alternative sources of cognitive and aﬀective stimuli are available. Mappings between target mental states and brain activity should clearly be deﬁned and investigated with careful consideration of confounding factors that might aﬀect neurophysiological variables (Brouwer et al., 2015). For instance, when developing an aﬀective BCI classiﬁer for detection of human emotions during interaction with a robot, the BCI model should be trained and tested in an ecologically valid HRI setting rather than with a set of aﬀective visual stimuli. Such new experimental paradigms may lead to unsuccessful or inconsistent results compared to prior neuroscience studies, however, this should not demotivate researchers from reporting

their ﬁndings as the BCI ﬁeld is still in its infancy and the report of negative results is equally valuable for its further progress (Lotte et al., 2020).

Yet, another challenge with respect to integration of passive BCIs in human-robot interaction studies is the high demand for computational resources and data storage, which are indispensible to real-time processing of brain activity as well as real-time conﬁguration of the robot controller. This means that in practice, the two interfaces are often operated on diﬀerent computers/environments and hence need to communicate with one another through proxy solutions (Müller-Putz et al., 2011). In order to integrate BCIs and robots eﬃciently, future developments is required to provide cost-eﬀective BCI modules that can be compiled and implemented in multiple environments without requiring extensive programming and adaptation.

Last but not least, we should not lose sight on the emerging ethical issues in real-world employment of passive BCIs such as management of user expectation and sensitive data (Burwell et al., 2017). Obviously, the idea of continuous monitoring and access to someone’s thoughts is dreadful, particularly when this information is collected and processed by a humanlike entity such as a robot. Especially, in the case of aﬀective BCIs, there are unique challenges with respect to user autonomy as they entail the risk of manipulation or inducement of aﬀective states without the user’s consent (Steinert and Friedrich, 2020). Therefore, it is of high importance to scrutinize the ethical implications of BCI-driven robots and develop educational programs that communicate ethical guidelines to potential users before such technologies are released into the wild.

## CONCLUSION

Passive BCI technology holds promise in extracting aﬀective and cognitive states for an optimized human-technology interaction. In this paper, we laid out the current state of the art in passive BCIs and illustrated their implications for realworld applications. We particularly reviewed their possible employment in human-robot interaction with the intention to inform the HRI community of the promises and challenges of passive BCI technology. Future work should continue to advance the synergy between the two domains and further explore the impact and eﬀectiveness of BCI-driven robots during closed-loop interactions with humans.

## AUTHOR CONTRIBUTIONS

MA wrote the manuscript with subsequent input from KH. All authors contributed to the article and approved the submitted version.

## FUNDING

This research was supported by Grant-in-Aid for JSPS Research Fellow 15F15046, ImPACT Program of Council for Science, Technology and Innovation (Cabinet Oﬃce, Government of Japan) and CREST-JST (No. 200800000003).

Frontiers in Robotics and AI | www.frontiersin.org 8 October 2020 | Volume 7 | Article 125

## REFERENCES

Ajoudani, A., Zanchettin, A. M., Ivaldi, S., Albu-Schäﬀer, A., Kosuge, K., and Khatib, O. (2018). Progress and prospects of the human–robot collaboration. Auton. Robots 42, 957–975. doi: 10.1007/s10514-017-9677-2

Alarcao, S. M., and Fonseca, M. J. (2017). Emotions recognition using EEG signals: a survey. IEEE Trans. Aﬀect. Comput. 10, 374–393. doi: 10.1109/TAFFC.2017.2714671

Alimardani, M., and Hiraki, K. (2017). “Development of a real-time braincomputer interface for interactive robot therapy: an exploration of EEG and EMG features during hypnosis,” in World Academy of Science, Engineering and Technology, International Journal of Computer, Electrical, Automation, Control and Information Engineering, Vol. 11, 187–195.

Alimardani, M., Kemmeren, L., Okumura, K., and Hiraki, K. (2020). Robotassisted mindfulness practice: analysis of neurophysiological responses and aﬀective state change,” in Proceeding of 29th IEEE International Conference on Robot and Human Interactive Communication (Ro-Man 2020) (Naples).

Alimardani, M., Keshmiri, S., Sumioka, H., and Hiraki, K. (2018). “Classiﬁcation of EEG signals for a hypnotrack BCI system,” in 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (Madrid: IEEE), 240–245. doi: 10.1109/IROS.2018.8594136

Alimardani, M., Nishio, S., and Ishiguro, H. (2013). Humanlike robot hands controlled by brain activity arouse illusion of ownership in operators. Sci. Rep. 3:2396. doi: 10.1038/srep02396

Alimardani, M., Nishio, S., and Ishiguro, H. (2015). “BCI-teleoperated androids; a study of embodiment and its eﬀect on motor imagery learning,” in 2015 IEEE 19th International Conference on Intelligent Engineering Systems (INES) (Bratislava: IEEE), 347–352. doi: 10.1109/INES.2015.7329753

Alimardani, M., and Qurashi, S. (2019). “Mind perception of a sociable humanoid robot: a comparison between elderly and young adults,” in Iberian Robotics Conference (Cham: Springer), 96–108. doi: 10.1007/978-3-030-36150-1_9

Allison, B. Z., Dunne, S., Leeb, R., Millán, J. D. R., and Nijholt, A. (Eds.). (2012). Towards Practical Brain-Computer Interfaces: Bridging the Gap From Research to Real-World Applications. Springer Science and Business Media. doi: 10.1007/978-3-642-29746-5

Al-Nafjan, A., Hosny, M., Al-Ohali, Y., and Al-Wabil, A. (2017). Review and classiﬁcation of emotion recognition based on EEG brain-computer interface system research: a systematic review. Appl. Sci. 7:1239. doi: 10.3390/app7121239

Anzalone, S., Tanet, A., Pallanca, O., Cohen, D., and Chetouani, M. (2016). “A humanoid robot controlled by neurofeedback to reinforce attention in autism spectrum disorder,” in Proceedings of the 3rd Italian Workshop on Artiﬁcial Intelligence and Robotics (Genova).

Aranyi, G., Pecune, F., Charles, F., Pelachaud, C., and Cavazza, M. (2016). Aﬀective interaction with a virtual character through an fNIRS brain-computer interface. Front. Comput. Neurosci. 10:70. doi: 10.3389/fncom.2016.00070

Aricò, P., Borghini, G., Di Flumeri, G., Colosimo, A., Bonelli, S., Golfetti, A., et al. (2016). Adaptive automation triggered by EEG-based mental workload index: a passive brain-computer interface application in realistic air traﬃc control environment. Front. Hum. Neurosci. 10:539. doi: 10.3389/fnhum.2016.00539

Aricò, P., Borghini, G., Di Flumeri, G., Sciaraﬀa, N., and Babiloni, F. (2018). Passive BCI beyond the lab: current trends and future directions. Physiol. Measur. 39:08TR02. doi: 10.1088/1361-6579/aad57e

Aricò, P., Borghini, G., Di Flumeri, G., Sciaraﬀa, N., Colosimo, A., and Babiloni, F. (2017). Passive BCI in operational environments: insights, recent advances, and future trends. IEEE Trans. Biomed. Eng. 64, 1431–1436. doi: 10.1109/TBME.2017.2694856

Atkinson, J., and Campos, D. (2016). Improving BCI-based emotion recognition by combining EEG feature selection and kernel classiﬁers. Expert Syst. Appl. 47, 35–41. doi: 10.1016/j.eswa.2015.10.049

Benabid, A. L., Costecalde, T., Eliseyev, A., Charvet, G., Verney, A., Karakas, S., et al. (2019). An exoskeleton controlled by an epidural wireless brain–machine interface in a tetraplegic patient: a proof-of-concept demonstration. Lancet Neurol. 18:1112. doi: 10.1016/S1474-4422(19)30321-7

Beraldo, G., Antonello, M., Cimolato, A., Menegatti, E., and Tonin, L. (2018). “Brain-computer interface meets ROS: a robotic approach to mentally drive telepresence robots,” in 2018 IEEE International Conference on Robotics and Automation (ICRA) (Brisbane, QLD: IEEE), 1–6. doi: 10.1109/ICRA.2018.8460578

Birbaumer, N., and Rana, A. (2019). “Brain–computer interfaces for communication in paralysis,” in Casting Light on the Dark Side of Brain Imaging (Academic Press), 25–29. doi: 10.1016/B978-0-12-816179-1.00003-7

Blankertz, B., Acqualagna, L., Dähne, S., Haufe, S., Schultze-Kraft, M., Sturm, I., et al. (2016). The Berlin brain-computer interface: progress beyond communication and control. Front. Neurosci. 10:530. doi: 10.3389/fnins.2016.00530

Brouwer, A. M., Zander, T. O., Van Erp, J. B., Korteling, J. E., and Bronkhorst, A. W. (2015). Using neurophysiological signals that reﬂect cognitive or aﬀective state: six recommendations to avoid common pitfalls. Front. Neurosci. 9:136. doi: 10.3389/fnins.2015.00136

Burwell, S., Sample, M., and Racine, E. (2017). Ethical aspects of brain computer interfaces: a scoping review. BMC Med. Ethics 18:60. doi: 10.1186/s12910-017-0220-y

Canning, C., and Scheutz, M. (2013). Functional near-infrared spectroscopy in human-robot interaction. J. Hum. Robot Interact. 2, 62–84. doi: 10.5898/JHRI.2.3.Canning

Cavazza, M., Charles, F., Gilroy, S. W., Porteous, J., Aranyi, G., Cordry, J., et al.

(2015). Virtual agents in brain-computer interfaces. Int. J. Virtual Real. 15, 48–60. doi: 10.20870/IJVR.2015.15.1.2868

Chanel, G., Kierkels, J. J., Soleymani, M., and Pun, T. (2009). Short-term emotion assessment in a recall paradigm. Int. J. Hum. Comput. Stud. 67, 607–627. doi: 10.1016/j.ijhcs.2009.03.005

Chaudhary, U., Birbaumer, N., and Curado, M. R. (2015). Brain-machine interface (BMI) in paralysis. Ann. Phys. Rehabil. Med. 58, 9–13. doi: 10.1016/j.rehab.2014.11.002

Chavarriaga, R., Sobolewski, A., and Millán, J. D. R. (2014). Errare machinale est: the use of error-related potentials in brain-machine interfaces. Front. Neurosci. 8:208. doi: 10.3389/fnins.2014.00208

Chen, C. M., Wang, J. Y., and Yu, C. M. (2017). Assessing the attention levels of students by using a novel attention aware system based on brainwave signals. Br. J. Educ. Technol. 48, 348–369. doi: 10.1111/bjet. 12359

Chen, X., Zhao, B., Wang, Y., and Gao, X. (2019). Combination of high-frequency SSVEP-based BCI and computer vision for controlling a robotic arm. J. Neural Eng. 16:026012. doi: 10.1088/1741-2552/aaf594

Cinel, C., Valeriani, D., and Poli, R. (2019). Neurotechnologies for human cognitive augmentation: current state of the art and future prospects. Front. Hum. Neurosci. 13:13. doi: 10.3389/fnhum.2019.00013

Coogan, C. G., and He, B. (2018). Brain-computer interface control in a virtual reality environment and applications for the internet of things. IEEE Access 6, 10840–10849. doi: 10.1109/ACCESS.2018.2809453

Cruz, A., Pires, G., and Nunes, U. J. (2018). Double ErrP detection for automatic error correction in an ERP-based BCI speller. IEEE Trans. Neural Syst. Rehabilit. Eng. 26, 26–36. doi: 10.1109/TNSRE.2017.2 755018

Dehais, F., Dupres, A., Di Flumeri, G., Verdiere, K., Borghini, G., Babiloni, F., et al. (2018). “Monitoring pilot’s cognitive fatigue with engagement features in simulated and actual ﬂight conditions using an hybrid fNIRS-EEG passive BCI,” in 2018 IEEE International Conference on Systems, Man, and Cybernetics (SMC) (Miyazaki: IEEE), 544–549. doi: 10.1109/SMC.2018.00102

Dehais, F., Rida, I., Roy, R. N., Iversen, J., Mullen, T., and Callan, D. (2019). “A pBCI to predict attentional error before it happens in real ﬂight conditions,” in 2019 IEEE International Conference on Systems, Man and Cybernetics (SMC) (Bari: IEEE), 4155–4160. doi: 10.1109/SMC.2019.8 914010

Diez, P. F., Correa, A. G., Orosco, L., Laciar, E., and Mut, V. (2015). Attention-level transitory response: a novel hybrid BCI approach. J. Neural Eng. 12:056007. doi: 10.1088/1741-2560/12/5/056007

Dimitrakopoulos, G. N., Kakkos, I., Dai, Z., Lim, J., deSouza, J. J., Bezerianos, A., et al. (2017). Task-independent mental workload classiﬁcation based upon common multiband EEG cortical connectivity. IEEE Trans. Neural Syst. Rehabilit. Eng. 25, 1940–1949. doi: 10.1109/TNSRE.2017.2 701002

Dimitriadis, S. I., Sun, Y. U., Kwok, K., Laskaris, N. A., Thakor, N., and Bezerianos, A. (2015). Cognitive workload assessment based on the tensorial treatment of EEG estimates of cross-frequency phase interactions. Ann. Biomed. Eng. 43, 977–989. doi: 10.1007/s10439-014-1143-0

Dzedzickis, A., Kaklauskas, A., and Bucinskas, V. (2020). Human emotion recognition: review of sensors and methods. Sensors 20:592. doi: 10.3390/s20030592

Ehrlich, S., Guan, C., and Cheng, G. (2017). “A closed-loop brain-computer music interface for continuous aﬀective interaction,” in 2017 International Conference on Orange Technologies (ICOT) (Singapore: IEEE), 176–179. doi: 10.1109/ICOT.2017.8336116

Ehrlich, S., Wykowska, A., Ramirez-Amaro, K., and Cheng, G. (2014). “When to engage in interaction—And how? EEG-based enhancement of robot’s ability to sense social signals in HRI,” in 2014 14th IEEE-RAS International Conference on Humanoid Robots (Humanoids) (Madrid: IEEE), 1104–1109. doi: 10.1109/HUMANOIDS.2014.7041506

- Ehrlich, S. K., and Cheng, G. (2018). Human-agent co-adaptation using errorrelated potentials. J. Neural Eng. 15:066014. doi: 10.1088/1741-2552/aae069
- Ehrlich, S. K., and Cheng, G. (2019). A feasibility study for validating robot actions using eeg-based error-related potentials. Int. J. Soc. Robot. 11, 271–283. doi: 10.1007/s12369-018-0501-8

Esfahani, E. T., and Sundararajan, V. (2011). Using brain–computer interfaces to detect human satisfaction in human–robot interaction. Int. J. Hum. Robot. 8, 87–101. doi: 10.1142/S0219843611002356

Ferrez, P. W., and Millán, J. D. R. (2005). “You are wrong!—automatic detection of interaction errors from brain waves,” in Proceedings of the 19th International Joint Conference on Artiﬁcial Intelligence (No. EPFL-CONF83269) (Edinburgh).

Ferrez, P. W., and Millán, J. D. R. (2008). “Simultaneous real-time detection of motor imagery and error-related potentials for improved BCI accuracy,” in Proceedings of the 4th International Brain-Computer Interface Workshop and Training Course (No. CNBI-CONF-2008-004) (Graz), 197–202.

Ficocelli, M., Terao, J., and Nejat, G. (2015). Promoting interactions between humans and robots using robotic emotional behavior. IEEE Trans. Cybern. 46, 2911–2923. doi: 10.1109/TCYB.2015.2492999

Friedman, D. (2015). “Brain-computer interfacing and virtual reality,” in Handbook of Digital Games and Entertainment Technologies, eds R. Nakatsu, M. Rauterberg, and P. Ciancarini (Singapore: Springer), 1–22. doi: 10.1007/978-981-4560-52-8_2-1

García-Martínez, B., Martinez-Rodrigo, A., Alcaraz, R., and Fernández-Caballero, A. (2019). “A review on nonlinear methods using electroencephalographic recordings for emotion recognition,” in IEEE Transactions on Aﬀective Computing. doi: 10.1109/TAFFC.2018.2890636

Gürkök, H., and Nijholt, A. (2012). Brain–computer interfaces for multimodal interaction: a survey and principles. Int. J. Hum. Comput. Interact. 28, 292–307. doi: 10.1080/10447318.2011.582022

Hong, K. S., and Khan, M. J. (2017). Hybrid brain–computer interface techniques for improved classiﬁcation accuracy and increased number of commands: a review. Front. Neurorobot. 11:35. doi: 10.3389/fnbot.2017.00035

Hong, K. S., Khan, M. J., and Hong, M. J. (2018). Feature extraction and classiﬁcation methods for hybrid fNIRS-EEG brain-computer interfaces. Front. Hum. Neurosci. 12:246. doi: 10.3389/fnhum.2018.00246

Hou, X., Trapsilawati, F., Liu, Y., Sourina, O., Chen, C. H., Mueller-Wittig, W., et al. (2017). “EEG-based human factors evaluation of conﬂict resolution aid and tactile user interface in future Air Traﬃc Control systems,” in Advances in Human Aspects of Transportation (Cham: Springer), 885–897. doi: 10.1007/978-3-319-41682-3_73

Iacoviello, D., Petracca, A., Spezialetti, M., and Placidi, G. (2015). A real-time classiﬁcation algorithm for EEG-based BCI driven by selfinduced emotions. Comput. Methods Programs Biomed. 122, 293–303. doi: 10.1016/j.cmpb.2015.08.011

Iturrate, I., Chavarriaga, R., Montesano, L., Minguez, J., and Millán, J. D. R.

(2015). Teaching brain-machine interfaces as an alternative paradigm to neuroprosthetics control. Sci. Rep. 5:13893. doi: 10.1038/srep13893

Jenke, R., Peer, A., and Buss, M. (2014). Feature extraction and selection for emotion recognition from EEG. IEEE Trans. Aﬀect. Comput. 5, 327–339. doi: 10.1109/TAFFC.2014.2339834

Khan, M. J., and Hong, K. S. (2015). Passive BCI based on drowsiness detection: an fNIRS study. Biomed. Opt. Express 6, 4063–4078. doi: 10.1364/BOE.6. 004063

Kim, K. T., Suk, H. I., and Lee, S. W. (2016). Commanding a brain-controlled wheelchair using steady-state somatosensory evoked potentials. IEEE Trans.

Neural Syst. Rehabilit. Eng. 26, 654–665. doi: 10.1109/TNSRE.2016.25 97854

Kim, M. K., Kim, M., Oh, E., and Kim, S. P. (2013). A review on the computational methods for emotional state estimation from the human EEG. Comput. Math. Methods Med. 2013:573734. doi: 10.1155/2013/573734

Kim, S. K., Kirchner, E. A., Stefes, A., and Kirchner, F. (2017). Intrinsic interactive reinforcement learning–Using error-related potentials for real world human-robot interaction. Sci. Rep. 7:17562. doi: 10.1038/s41598-01717682-7

Kirchner, E. A., Kim, S. K., Straube, S., Seeland, A., Wöhrle, H., Krell, M. M., et al. (2013). On the applicability of brain reading for predictive human-machine interfaces in robotics. PLoS ONE 8:e81732. doi: 10.1371/journal.pone.00 81732

Ko, L. W., Komarov, O., Hairston, W. D., Jung, T. P., and Lin, C. T. (2017). Sustained attention in real classroom settings: An EEG study. Front. Hum. Neurosci. 11:388. doi: 10.3389/fnhum.2017.00388

Kosunen, I., Salminen, M., Järvelä, S., Ruonala, A., Ravaja, N., and Jacucci, G. (2016). “RelaWorld: neuroadaptive and immersive virtual reality meditation system,” in Proceedings of the 21st International Conference on Intelligent User Interfaces (Sonoma), 208–217. doi: 10.1145/2856767.2856796

Kothe, C. A., Makeig, S., and Onton, J. A. (2013). “Emotion recognition from EEG during self-paced emotional imagery,” in 2013 Humaine Association Conference on Aﬀective Computing and Intelligent Interaction (ACII) (Geneva: IEEE), 855–858. doi: 10.1109/ACII.2013.160

Krol, L. R., Andreessen, L. M., Zander, T. O., Nam, C. S., Nijholt, A., and Lotte, F. (2018). “Passive brain-computer interfaces: a perspective on increased interactivity,” in Brain-Computer Interfaces Handbook: Technological and Theoretical Advances, eds F. Lotte, A. Nijholt, and C. S. Nam (Oxford: Taylor & Francis Group), 69–86. doi: 10.1201/9781351231954-3

Krol, L. R., and Zander, T. O. (2017). “Passive BCI-based neuroadaptive systems,” in Proceedings of the 7th Graz Brain-Computer Interface Conference 2017 (Graz: GBCIC). doi: 10.3217/978-3-85125-533-1-46

Lebedev, M. A., and Nicolelis, M. A. (2017). Brain-machine interfaces: from basic science to neuroprostheses and neurorehabilitation. Physiol. Rev. 97, 767–837. doi: 10.1152/physrev.00027.2016

Lécuyer, A., Lotte, F., Reilly, R. B., Leeb, R., Hirose, M., and Slater, M. (2008). Braincomputer interfaces, virtual reality, and videogames. Computer 41, 66–72. doi: 10.1109/MC.2008.410

Leyzberg, D., Spaulding, S., Toneva, M., and Scassellati, B. (2012). “The physical presence of a robot tutor increases cognitive learning gains,” in Proceedings of the Annual Meeting of the Cognitive Science Society, Vol. 34 (Sapporo).

Liberati, G., Federici, S., and Pasqualotto, E. (2015). Extracting neurophysiological signals reﬂecting users’ emotional and aﬀective responses to BCI use: a systematic literature review. NeuroRehabilitation 37, 341–358. doi: 10.3233/NRE-151266

Lightbody, G., Galway, L., and McCullagh, P. (2014). “The brain computer interface: barriers to becoming pervasive,” in Pervasive Health (London: Springer), 101–129. doi: 10.1007/978-1-4471-6413-5_5

Lim, C. G., Poh, X. W. W., Fung, S. S. D., Guan, C., Bautista, D., Cheung, Y. B., et al. (2019). A randomized controlled trial of a brain-computer interface based attention training program for ADHD. PLoS ONE 14:e0216225. doi: 10.1371/journal.pone.0216225

Lin, C. T., Chang, C. J., Lin, B. S., Hung, S. H., Chao, C. F., and Wang, I. J. (2010). A real-time wireless brain–computer interface system for drowsiness detection. IEEE Trans. Biomed. Circuits Syst. 4, 214–222. doi: 10.1109/TBCAS.2010.2046415

Lin, Y. P., Wang, C. H., Jung, T. P., Wu, T. L., Jeng, S. K., Duann, J. R., et al. (2010). EEG-based emotion recognition in music listening. IEEE Trans. Biomed. Eng. 57, 1798–1806. doi: 10.1109/TBME.2010.2048568

Liu, J., Zhang, C., and Zheng, C. (2010). EEG-based estimation of mental fatigue by using KPCA–HMM and complexity parameters. Biomed. Signal Process. Control 5, 124–130. doi: 10.1016/j.bspc.2010.01.001

Liu, N. H., Chiang, C. Y., and Hsu, H. M. (2013). Improving driver alertness through music selection using a mobile EEG to detect brainwaves. Sensors 13, 8199–8221. doi: 10.3390/s130708199

Lopes-Dias, C., Sburlea, A. I., and Müller-Putz, G. R. (2019). Online asynchronous decoding of error-related potentials during the continuous control of a robot. Sci. Rep. 9:17596. doi: 10.1038/s41598-019-54109-x

Lotte, F. (2015). Signal processing approaches to minimize or suppress calibration time in oscillatory activity-based brain–computer interfaces. Proc. IEEE 103, 871–890. doi: 10.1109/JPROC.2015.2404941

Lotte, F., Faller, J., Guger, C., Renard, Y., Pfurtscheller, G., Lécuyer, A., et al. (2012). “Combining BCI with virtual reality: towards new applications and improved BCI,” in Towards Practical Brain-Computer Interfaces (Berlin; Heidelberg: Springer), 197–220. doi: 10.1007/978-3-642-29746-5_10

Lotte, F., Jeunet, C., Chavarriaga, R., Bougrain, L., Thompson, D. E., Scherer, R., et al. (2020). Turning negative into positives! Exploiting ‘negative’results in Brain–Machine Interface (BMI) research. Brain Comput. Interfaces 6, 178–189. doi: 10.1080/2326263X.2019.1697143

Lotte, F., Jeunet, C., Mladenovi´c, J., N’Kaoua, B., and Pillette, L. (2018). “A BCI challenge for the signal processing community: considering the user in the loop,” in Signal Processing and Machine Learning for Brain-Machine Interfaces (IET), 1–33.

Lotte, F., and Roy, R. N. (2019). “Brain–computer interface contributions to neuroergonomics,” in Neuroergonomics (Academic Press), 43–48. doi: 10.1016/B978-0-12-811926-6.00007-5

Mattout, J., Perrin, M., Bertrand, O., and Maby, E. (2015). Improving BCI performance through co-adaptation: applications to the P300speller. Ann. Phys. Rehabil. Med. 58, 23–28. doi: 10.1016/j.rehab.2014. 10.006

McDaniel, J. R., Gordon, S. M., Solon, A. J., and Lawhern, V. J. (2018). “Analyzing p300 distractors for target reconstruction,” in 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (Honolulu: EMBC) (IEEE), 2543–2546. doi: 10.1109/EMBC.2018.85 12854

Mehrabian, A. (1996). Pleasure-arousal-dominance: a general framework for describing and measuring individual diﬀerences in temperament. Curr. Psychol. 14, 261–292. doi: 10.1007/BF02686918

Millán, J. D. R., Rupp, R., Mueller-Putz, G., Murray-Smith, R., Giugliemma, C., Tangermann, M., et al. (2010). Combining brain–computer interfaces and assistive technologies: state-of-the-art and challenges. Front. Neurosci. 4:161. doi: 10.3389/fnins.2010.00161

Min, J., Wang, P., and Hu, J. (2017). Driver fatigue detection through multiple entropy fusion analysis in an EEG-based system. PLoS ONE 12:e0188756. doi: 10.1371/journal.pone.0188756

Minguillon, J., Lopez-Gordo, M. A., and Pelayo, F. (2017). Trends in EEG-BCI for daily-life: Requirements for artifact removal. Biomed. Signal Process. Control 31, 407–418. doi: 10.1016/j.bspc.2016.09.005

Mishra, J., Anguera, J. A., and Gazzaley, A. (2016). Video games for neurocognitive optimization. Neuron 90, 214–218. doi: 10.1016/j.neuron.2016.04.010

Mohammadi, Z., Frounchi, J., and Amiri, M. (2017). Wavelet-based emotion recognition system using EEG signal. Neural Comput. Appl. 28, 1985–1990. doi: 10.1007/s00521-015-2149-8

Mousavi, M., and de Sa, V. R. (2019). Spatio-temporal analysis of error-related brain activity in active and passive brain–computer interfaces. Brain Comput. Interfaces 6, 118–127. doi: 10.1080/2326263X.2019.1671040

Mu, Z., Hu, J., and Min, J. (2017). Driver fatigue detection system using electroencephalography signals based on combined entropy features. Appl. Sci. 7:150. doi: 10.3390/app7020150

Mühl, C., Allison, B., Nijholt, A., and Chanel, G. (2014a). A survey of aﬀective brain computer interfaces: principles, state-of-the-art, and challenges. Brain Comput. Interfaces 1, 66–84. doi: 10.1080/2326263X.2014.912881

Mühl, C., Jeunet, C., and Lotte, F. (2014b). EEG-based workload estimation across aﬀective contexts. Front. Neurosci. 8:114. doi: 10.3389/fnins.2014.00114

Müller-Putz, G. R., Breitwieser, C., Cincotti, F., Leeb, R., Schreuder, M., Leotta, F., et al. (2011). Tools for brain-computer interaction: a general concept for a hybrid BCI. Front. Neuroinform. 5:30. doi: 10.3389/fninf.2011.00030

Myrden, A., and Chau, T. (2015). Eﬀects of user mental state on EEG-BCI performance. Front. Hum. Neurosci. 9:308. doi: 10.3389/fnhum.2015.00308 Myrden, A., and Chau, T. (2017). A passive EEG-BCI for single-trial detection of changes in mental state. IEEE Trans. Neural Syst. Rehabilit. Eng. 25, 345–356. doi: 10.1109/TNSRE.2016.2641956

Nagel, S., and Spüler, M. (2019). World’s fastest brain-computer interface: Combining EEG2Code with deep learning. PLoS ONE 14:e0221909. doi: 10.1371/journal.pone.0221909

Nam, C. S., Nijholt, A., and Lotte, F. (Eds.). (2018). Brain–Computer Interfaces Handbook: Technological and Theoretical Advances. CRC Press. doi: 10.1201/9781351231954

Ogino, M., and Mitsukura, Y. (2018). Portable drowsiness detection through use of a prefrontal single-channel electroencephalogram. Sensors 18:4477. doi: 10.3390/s18124477

Paiva, A., Leite, I., and Ribeiro, T. (2014). “Emotion modeling for social robots,” in The Oxford Handbook of Aﬀective Computing, eds R. Calvo, S. D’Mello, J. Gratch, and A. Kappas 296–308. doi: 10.1093/oxfordhb/9780199942237.001.0001

Pazzaglia, M., and Molinari, M. (2016). The embodiment of assistive devices—from wheelchair to exoskeleton. Phys. Life Rev. 16, 163–175. doi: 10.1016/j.plrev.2015.11.006

Pino, O., Palestra, G., Trevino, R., and De Carolis, B. (2019). The humanoid robot nao as trainer in a memory program for elderly people with mild cognitive impairment. Int. J. Soc. Robot. 12, 21–33. doi: 10.1007/s12369-01900533-y

Poli, R., Valeriani, D., and Cinel, C. (2014). Collaborative braincomputer interface for aiding decision-making. PLoS ONE 9:e102693. doi: 10.1371/journal.pone.0102693

Posner, J., Russell, J. A., and Peterson, B. S. (2005). The circumplex model of aﬀect: an integrative approach to aﬀective neuroscience, cognitive development, and psychopathology. Dev. Psychopathol. 17, 715–734. doi: 10.1017/S0954579405050340

Reuderink, B., Mühl, C., and Poel, M. (2013). Valence, arousal and dominance in the EEG during game play. Int. J. Auton. Adapt. Commun. Syst. 6, 45–62. doi: 10.1504/IJAACS.2013.050691

Rossi, S., Ferland, F., and Tapus, A. (2017). User proﬁling and behavioral adaptation for HRI: a survey. Pattern Recognit. Lett. 99, 3–12. doi: 10.1016/j.patrec.2017.06.002

Roy, R. N., Bonnet, S., Charbonnier, S., and Campagne, A. (2013). “Mental fatigue and working memory load estimation: interaction and implications for EEG-based passive BCI,” in Engineering in Medicine and Biology Society (EMBC), 2013 35th Annual International Conference of the IEEE (Osaka: IEEE), 6607–6610. doi: 10.1109/EMBC.2013.6611070

Saha, S., and Baumert, M. (2019). Intra-and inter-subject variability in EEG-based sensorimotor brain computer interface: a review. Front. Comput. Neurosci. 13:87. doi: 10.3389/fncom.2019.00087

Salazar-Gomez, A. F., DelPreto, J., Gil, S., Guenther, F. H., and Rus, D. (2017). “Correcting robot mistakes in real time using eeg signals,” in 2017 IEEE International Conference on Robotics and Automation (ICRA) (Singapore: IEEE), 6570–6577. doi: 10.1109/ICRA.2017.7989777

Schmidt, N. M., Blankertz, B., and Treder, M. S. (2012). Online detection of errorrelated potentials boosts the performance of mental typewriters. BMC Neurosci. 13:19. doi: 10.1186/1471-2202-13-19

Schultze-Kraft, M., Gugler, M., Curio, G., and Blankertz, B. (2012). “Towards an online detection of workload in industrial work environments,” in 34th Annual International Conference of the IEEE EMBS (San Diego, CA), 4792–4795.

Sciutti, A., Mara, M., Tagliasco, V., and Sandini, G. (2018). Humanizing human-robot interaction: on the importance of mutual understanding. IEEE Technol. Soc. Magaz. 37, 22–29. doi: 10.1109/MTS.2018.27 95095

Sellers, E. W., Ryan, D. B., and Hauser, C. K. (2014). Noninvasive brain-computer interface enables communication after brainstem stroke. Sci. Transl. Med. 6:257re7. doi: 10.1126/scitranslmed.3007801

Shao, M., Alves, S. F. D. R., Ismail, O., Zhang, X., Nejat, G., and Benhabib, B. (2019). “You are doing great! Only one rep left: an aﬀect-aware social robot for exercising,” in 2019 IEEE International Conference on Systems, Man and Cybernetics (SMC) (IEEE), 3811–3817. doi: 10.1109/SMC.2019.8 914198

Shu, L., Xie, J., Yang, M., Li, Z., Li, Z., Liao, D., et al. (2018). A review of emotion recognition using physiological signals. Sensors 18:2074. doi: 10.3390/s18072074

Sinnema, L., and Alimardani, M. (2019). “The attitude of elderly and young adults towards a humanoid robot as a facilitator for social interaction,” in International Conference on Social Robotics (Cham: Springer), 24–33. doi: 10.1007/978-3-030-35888-4_3

Soekadar, S. R., Birbaumer, N., Slutzky, M. W., and Cohen, L. G. (2015). Brain–machine interfaces in neurorehabilitation of stroke. Neurobiol. Dis. 83, 172–179. doi: 10.1016/j.nbd.2014.11.025

Solovey, E., Schermerhorn, P., Scheutz, M., Sassaroli, A., Fantini, S., and Jacob, R. (2012). “Brainput: enhancing interactive systems with streaming fnirs brain input,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (ACM), 2193–2202. doi: 10.1145/2207676.2 208372

Sprague, S. A., McBee, M. T., and Sellers, E. W. (2016). The eﬀects of working memory on brain–computer interface performance. Clin. Neurophysiol. 127, 1331–1341. doi: 10.1016/j.clinph.2015.10.038

Spüler, M., Krumpe, T., Walter, C., Scharinger, C., Rosenstiel, W., and Gerjets, P. (2017). “Brain-computer interfaces for educational applications,” in Informational Environments (Cham: Springer), 177–201. doi: 10.1007/978-3-319-64274-1_8

Spüler, M., and Niethammer, C. (2015). Error-related potentials during continuous feedback: using EEG to detect errors of diﬀerent type and severity. Front. Hum. Neurosci. 9:155. doi: 10.3389/fnhum.2015.00155

Steinert, S., and Friedrich, O. (2020). Wired emotions: ethical issues of aﬀective brain–computer interfaces. Sci. Eng. Ethics 26, 351–367. doi: 10.1007/s11948-019-00087-2

Strait, M., and Scheutz, M. (2014). Using near infrared spectroscopy to index temporal changes in aﬀect in realistic human-robot interactions. PhyCS 14, 385–392. doi: 10.5220/0004902203850392

Szaﬁr, D., and Mutlu, B. (2012). “Pay attention!: designing adaptive agents that monitor and improve user engagement,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Austin: ACM), 11–20. doi: 10.1145/2207676.2207679

Tanveer, M. A., Khan, M. J., Qureshi, M. J., Naseer, N., and Hong, K. S. (2019). Enhanced drowsiness detection using deep learning: an fNIRS study. IEEE Access 7, 137920–137929. doi: 10.1109/ACCESS.2019.29 42838

Tapus, A., Tapus, C., and Mataric, M. (2009). “The role of physical embodiment of a therapist robot for individuals with cognitive impairments,” in RO-MAN 2009-The 18th IEEE International Symposium on Robot and Human Interactive Communication (Toyama: IEEE), 103–107. doi: 10.1109/ROMAN.2009.53 26211

Tsiakas, K., Abujelala, M., and Makedon, F. (2018). Task engagement as personalization feedback for socially-assistive robots and cognitive training. Technologies 6:49. doi: 10.3390/technologies6020049

Van Erp, J., Lotte, F., and Tangermann, M. (2012). Brain-computer interfaces: beyond medical applications. Computer 45, 26–34. doi: 10.1109/MC. 2012.107

Vi, C. T., Jamil, I., Coyle, D., and Subramanian, S. (2014). “Error related negativity in observing interactive tasks,” In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Toronto, ON: ACM), 3787–3796.

Wiese, E., Metta, G., and Wykowska, A. (2017). Robots as intentional agents: using neuroscientiﬁc methods to make robots appear more social. Front. Psychol. 8:1663. doi: 10.3389/fpsyg.2017.01663

Wirth, C., Dockree, P. M., Harty, S., Lacey, E., and Arvaneh, M. (2019). Towards error categorisation in BCI: single-trial EEG classiﬁcation between diﬀerent errors. J. Neural Eng. 17:016008. doi: 10.1088/1741-2552/ab53fe

Youseﬁ, R., Sereshkeh, A. R., and Chau, T. (2019). Development of a robust asynchronous brain-switch using ErrP-based error correction. J. Neural Eng. 16:066042. doi: 10.1088/1741-2552/ ab4943

Zander, T. O., and Kothe, C. (2011). Towards passive brain–computer interfaces: applying brain–computer interface technology to human–machine systems in general. J. Neural Eng. 8:025005. doi: 10.1088/1741-2560/8/2/025005

Zander, T. O., Kothe, C., Jatzev, S., and Gaertner, M. (2010). “Enhancing human-computer interaction with input from active and passive braincomputer interfaces,” in Brain-Computer Interfaces (London: Springer), 181–199. doi: 10.1007/978-1-84996-272-8_11

Zander, T. O., Shetty, K., Lorenz, R., Leﬀ, D. R., Krol, L. R., Darzi, A. W., et al. (2017). Automated task load detection with electroencephalography: towards passive brain–computer interfacing in robotic surgery. J. Med. Robot. Res. 2:1750003. doi: 10.1142/S2424905X17500039

Zarjam, P., Epps, J., and Lovell, N. H. (2015). Beyond subjective self-rating: EEG signal classiﬁcation of cognitive workload. IEEE Trans. Auton. Ment. Dev. 7, 301–310. doi: 10.1109/TAMD.2015.2441960

Zhang, J., Wang, B., Zhang, C., Xiao, Y., and Wang, M. Y. (2019). An EEG/EMG/EOG-based multimodal human-machine interface to real-time control of a soft robot hand. Front. Neurorobot. 13:7. doi: 10.3389/fnbot.2019.00007

Conﬂict of Interest: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Copyright © 2020 Alimardani and Hiraki. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

