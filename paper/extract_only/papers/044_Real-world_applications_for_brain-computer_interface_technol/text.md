# Real-World Applications for Brain–Computer Interface Technology

Melody M. Moore

Abstract—The mission of the Georgia State University BrainLab is to create and adapt methods of human–computer interaction that will allow brain–computer interface (BCI) technologies to effectively control real-world applications. Most of the existing BCI applications were designed largely for training and demonstration purposes. Our goal is to research ways of transitioning BCI control skills learned in training to real-world scenarios. Our research explores some of the problems and challenges of combining BCI outputs with human–computer interface paradigms in order to achieve optimal interaction. We utilize a variety of application domains to compare and validate BCI interactions, including communication, environmental control, neural prosthetics, and creative expression. The goal of this research is to improve quality of life for those with severe disabilities.

Index Terms—Assistive technology, augmentive and assistive communication (AAC), brain–computer interface (BCI), direct-brain interface (DBI), environmental control, locked-in syndrome, neural prosthetics.

I. INTRODUCTION

Although significant progress has been made in researching brain–computer interface technologies in recent years, the applications controlled by these interfaces have largely been designed for training or demonstration purposes. The Georgia State University (GSU) BrainLab is devoted to researching and developing interaction techniques that will allow BCIs to be effective in real-world applications. To this end, we employ and compare a variety of underlying BCI signal-processing and translation techniques.

The overall goal of the GSU BrainLab is to determine which paradigms of human–computer interaction are optimal for direct control of a computer using brain signals. We aim to provide a significant quality-of-life improvement to users with severe disabilities as well as studying ways to utilize BCIs for able-bodied users. The BrainLab currently has ongoing projects in several BCI and assistive-technology areas: user interface control paradigms, subject training and biofeedback, creative expression, and quality-of-life applications including assistive communication and environmental control.

There are many challenges inherent in employing BCI control for real-world tasks. These challenges can be generalized into several categories.

- 1) Information transfer rate (“bandwidth”)—Even the best average information transfer rates for experienced subjects and well-tuned BCI systems are relatively low, in the vicinity of 24 b (roughly three characters)/min [1]. This is too slow for natural interactive conversation, so we are researching ways of optimizing selection techniques and incorporating prediction mechanisms to speed communication.
- 2) High error rate—A significant complicating factor in the slow information transfer rate of BCI users is the high probability of errors. Brain signals are highly variable, and this problem is exacerbated in severely disabled users by fatigue, medications, and

Manuscript received July 19, 2002; revised April 29, 2003. This work was supported in part by the National Science Foundation under Grants IIS-0205644 and IIS-0118917. Work on the invasive technique was supported by the National Institutes of Health (NINDS) under Grant Subcontract BLF34.

The author is with the GSU BrainLab, Computer Information Systems Department, Georgia State University, Atlanta, GA 30303-4013 USA (e-mail: melody@gsu.edu).

Digital Object Identifier 10.1109/TNSRE.2003.814433

medical conditions such as seizures or spasms. Self-reporting errors is also extremely difficult, particularly if the subject has little or no communication channel outside of the BCI system itself. Devising methods of quickly resolving or preventing errors is critical to successful BCI interaction.

- 3) Autonomy—Ideally, a communication system for a person with severe disabilities should be completely controlled by its user. Unfortunately BCI systems require extensive assistance from caretakers who need to apply electrodes or signal-receiving devices before a user can communicate. Furthermore, most BCI systems are system-initiated, meaning that the user cannot turn them on and off independently. This results in what is termed the “Midas touch” problem—the BCI system interprets all brain activity as input, so how can the user communicate the intent to control the system? A BCI user may be able to perform a selection to turn the BCI system off, but turning it back on again is an issue. We are exploring the possibility of hybrid systems, combinations of different BCI techniques, and other biometric interfaces to address this problem.
- 4) Cognitive load—Most BCI systems are tested in quiet laboratory environments, where users are able to concentrate on the task at hand with minimal distractions. BCI users in the real world have to deal with much more complex situations, including the cognitive load of the task being performed, emotional responses, interactions with other people, and possibly even safety considerations. We are studying the effects of cognitive load on the efficacy of BCI controls in order to determine whether BCI’s could be used for in-home everyday living situations.

II. BACKGROUND AND RELATED WORK

The general intent of most BCIs is to operate a device or application by detecting small differences in brain signals. Therefore, almost every BCI system includes a set of tasks or capabilities that a user can influence by changing aspects of selected brain signals or from evoked responses. Typical tasks intended for subject training include positioning a cursor, tracking a moving object, or selecting a target. Once these skills are acquired, the subject can progress to applications that perform real-world tasks such as communication, controlling the environment, or moving prosthetic limbs.

A. Communication

Restoring communication is a top priority for people with severe disabilities such as locked-in syndrome, in which the person is completely paralyzed and unable to speak. Consequently, BCI researchers have experimented with several methods of assistive communication, ranging from simple binary (yes/no) capabilities [2] and iconic selection applications such as TalkAssist [3], to virtual keyboards that support spelling. Several approaches to spelling have been developed. Birbaumer et al. [4], [5] describe a binary speller, dividing the alphabet in successive halves until the desired letter is selected. This speller has been used by a locked-in person to compose letters in a real-world home environment. Wolpaw et al. [2] describe a similar speller, dividing the alphabet into successive fourths instead of halves. Donchin et al. [6] have developed a method based on the P300 component of event-related potentials, which allows the user to select a letter by flashing rows and columns of a two-dimensional (2-D) alphabet grid to determine the desired letter. Kennedy et al. have provided locked-in subjects with 2-D cursor navigation to select letters from a WiViK virtual keyboard [3]. Although each of these spellers has been shown to work, communication is still slow,

1534-4320/03$17.00 © 2003 IEEE

averaging three letters per minute. The spellers have largely been used for training by providing prepared words or phrases for the subject to spell, called copy-spelling. Several of these spellers have also been used for free-spelling, although measuring the accuracy of BCI output is difficult and relies on user self-reporting.

- B. Environmental Control and Virtual Worlds

Virtual reality has been employed in BCI training systems because of its relative safety and motivational factors. Bayless [7] describes a virtual driving environment that tested P300 responses when subjects encountered a stoplight. Later work includes a virtual apartment which allows the user to interact with virtual people and objects. Birch and Mason [8] have used the LS-AFD device to allow users to navigate a maze by making turning decisions at intersections. Virtual reality can provide a safe environment for training and tuning neurally controlled interfaces to real-world devices, such as a power wheelchair. More experimentation is necessary to determine if skills learned in a virtual-reality setting transfer to real-world scenarios.

- C. Neural Prosthetics

Another key application for BCI technology is restoring movement for people with motor disabilities. Cortical signals have been used to control a hand orthosis [9], essentially restoring the connection from the brain to a paralyzed arm. A locked-in subject has also used neural signals to control a virtual hand [3] in the hopes that simulation would provide clues to potentially incorporating functional electrical stimulation (FES) into a BCI system to restore movement.

III. METHODS

To answer the challenge of adapting BCI technologies for real-world applications, the GSU BrainLab focuses on studying and creating new human–computer interaction techniques to improve BCI system performance. The BrainLab currently supports a variety of projects in the areas of control paradigms, communication and environmental control, subject training and biofeedback, creative expression, and internet access.

A. Neural Screen Navigation—New User Interface Control Paradigms

The aim of this research is to explore the field human–computer interactions and to identify possibilities for alternate paradigms of navigating a computer screen using brain signals, in addition to traditional 2-D spatial navigation (such as cursor movement controlled by a mouse). One option for increasing accuracy and reducing errors is logical control, which is movement between targets triggered by a discrete control signal. We implemented logical control with signals from a neurotrophic-electrode that had been implanted in the cortex of a patient [3]. This control was based on frequency thresholding, or “nudge-and-shove” control [10], which allows several discrete control signals to be generated from the more or less continuous neural signal using thresholding. In this scheme, a small increase in frequency generates one control signal, which may move to the next icon in a choice list (a “nudge”), whereas a large increase in frequency generates a different control signal that could move to a completely different menu or application component (a “shove”). Fig. 1 shows an offline analysis visualization of neural firing rates during a several nudges Fig. 1(a) and a shove Fig. 1(b). The axis represents time, and the axis represents increases in the frequency of neural firing rate by the length of the bar. The light and dark colors represent two different signal firing patterns.

[Figure 1]

- (a)

[Figure 2]

- (b)

Fig. 1. (a) Small frequency increases (“nudge”). (b) Large frequency increase (“shove”).

Another approach that we have combined with the nudge-and-shove paradigm to decrease target selection time and error rate is area cursors [11]. A large translucent cursor is moved over the screen, and selection is accomplished when the target is within the boundaries of the cursor. If more than one target is selected, the area under the cursor is magnified and the cursor can then be moved to the appropriate target. We have tested area-cursor navigation with offline data and brain-signal emulation, and the next step is to test it in real time.

- B. Aware ’Chair—Communication and Environmental Control

The quality of life of locked-in patients can substantially improve if they are provided with a way to communicate with friends, family, and medical personnel, as well as control devices in their environment, such as the television and radio. In addition to the WiViK keyboard and the TalkAssist iconic voice synthesis program described in Kennedy et al. [3], we are exploring the possibilities of prediction to enhance performance of BCI-controlled applications. The Aware ’Chair is a context-aware intelligent power wheelchair which integrates environmental control, communication, and multilevel prediction based on context and user history. The communication and environmental control systems are informed by environmental sensors, user history, time of day, medical status, and other information in order to predictively narrow the selection space, thereby improving user performance. Fig. 2 shows the environmental control interface from the Aware ’Chair, adapted for nudge-and-shove neural control.

We are currently adapting the Aware ’Chair for neural control and incorporating word, sentence, and life-event prediction algorithms.

- C. BrainTrainer—Subject Training

The BrainTrainer project researches the most effective ways of teaching a person the brain-signal control needed to interact with a device. The BrainTrainer toolset allows researchers to compose trials by providing simple tasks, such as targeting, navigation, selection, and timing, that can be combined to produce an appropriate-level task for a particular subject. It also allows the researcher to incorporate different forms of visual and auditory biofeedback. BrainTrainer automatically instruments the resulting application for data recording such as error rates, speed, and accuracy of task performance. We are working with the Neil Squire Foundation [8] on a survey and study to determine the atomic tasks, benchmarks, and standardized data formats that BrainTrainer will support.

[Figure 3]

- Fig. 2. Aware ’Chair control interface.

[Figure 4]

- Fig. 3. Neurally controlled web browser.

- D. Neural Art—Biofeedback

The Neural Art project explores different methods of representing brain signals, both for biofeedback and training purposes and for creative expression and recreation. The Neural Music program we have developed translates brain signal and brain-signal patterns directly to musical instrument device interface (MIDI), allowing for a tonal representation of the signal. This has been tested in offline analysis with single unit brain-signal recordings from neurotrophic electrode patients, mapping the signal frequency to tone. It has also been ported to Wadsworth’s BCI2000 [12], and we are preparing to test it with noninvasive (EEG) recording techniques, mapping amplitude changes in the mu rhythm to tonal changes. We have also incorporated a signal visualizer, which allows the brain signal to be represented graphically according to configurable signal characteristics.

- E. Neural Internet

Access to the internet opens a myriad of opportunities for those with severe disabilities, including shopping, entertainment, education, and possibly evenemployment.Neuralcontrol userscannot controla cursor with a great degree of precision, so, therefore, the challenge of adapting a web browser for neural control is in making links—which are spatially organized—accessible. The University of Tuebingen developed a web browser controller to be used with their thought translation device [5], but it requires the user to select from an alphabetized list of links,

causing problems if the link names are identical. We have developed a neurally controlled web browser that serializes the spatial internet interface and allows logical control of a web application [13], [14]. Fig. 3 shows the GSU BrainLab implementation of a neurally controlled web browser.

IV. CONCLUSION AND FUTURE WORK

The key to moving BCI technology beyond the demonstration stage is to determine which methods of interaction are the most effective and to incorporate these into real-world applications. All of the applications and interaction techniques described have been tested with brain-signal emulation and offline data, which is sufficient for assuring correct functionality but not sufficient to draw conclusions about the efficacy of the user interface paradigms. Previously, we worked with invasive technique (neurotrophic electrode) locked-in patients [3], but their availability is very low due to illnesses and rapid fatigue. Therefore, we have expanded our research agenda to include noninvasive techniques, which will allow us to include other subject populations with disabilities and also able-bodied subjects. Together with the Wolpaw group, we have begun to study porting these applications to the BCI2000 system [2] in order to support the use of signals recorded with noninvasive techniques,e.g., mu and relatedbeta rhythms. We are also collaborating with researchers at the Neil Squire Foundation to perform experiments with Mason’s LF-ASD switch [8]. We are in the process of addressing the following research questions.

- 1) What existing human-computer interaction paradigms are most adaptable for brain-signal control? Are there new paradigms that are even more effective?
- 2) What are the best mappings for control signals to interaction techniques or devices?
- 3) How can we compare the performance of different BCI systems for use with real-world applications? Can we develop benchmark applications?
- 4) What are the best methods of feedback for neural control in a real-world scenario?
- 5) To what extent can assistive techniques such as prediction be incorporated into a BCI to increase performance?
- 6) How do we assess the usability of a BCI? What factors affect usability?

Together with our collaborators, we hope to make significant progress on these questions in the coming years.

REFERENCES

- [1] Wolpaw et al., “Brain-computer interfaces for communication and control,” Clin. Neurophysiol., vol. 113, p. 767, 2002.
- [2] J. R. Wolpaw, D. McFarland, and T. M. Vaughan, “Brain-computer interface research at the wadsworth center,” IEEE Trans. Rehab. Eng., vol. 8, pp. 222–226, June 2000.
- [3] P. R. Kennedy, R. A. E. Bakay, M. M. Moore, K. Adams, and J. Goldthwaite, “Direct control of a computer from the human central nervous system,” IEEE Trans. Rehab. Eng., vol. 8, June 2000.
- [4] J. Perelmouter and N. Birbaumer, “A binary spelling interface with random errors,” IEEE Trans. Rehab. Eng., vol. 8, pp. 227–232, June 2000.
- [5] N. Birbaumer, A. Kubler, N. Ghanayim, T. Hinterberger, J. Perelmouter, J. Kaiser, I. Iversen, B. Kotchoubey, N. Neumann, and H. Flor, “The thought translation device (TTD) for completely paralyzed patients,” IEEE Trans. Rehab. Eng., vol. 8, pp. 190–193, June 2000.
- [6] E. Donchin, K. Spencer, and R. Wijesinghe, “The mental prosthesis: Assessing the speed of a-Based brain-computer interface,” IEEE Trans. Rehab. Eng., vol. 8, pp. 174–179, June 2000.
- [7] J. D. Bayliss and D. H. Ballard, “Recognizing evoked potentials in a virtual environment,” Adv. Neural Inform. Process. Syst., vol. 12, 2000.
- [8] G. Birch and S. Mason, “Brain-Computer interface research at the neil squire foundation,” IEEE Trans. Rehab. Eng., vol. 8, June 2000.

- [9] G. Pfurtscheller, C. Guger, G. Muller, G. Krausz, and C. Neuper, “Brain oscillations control hand orthosis in a tetraplegic,” Neurosci. Lett., vol. 292, no. 3, pp. 211–4, 2000.
- [10] M. Moore, J. Mankoff, E. Mynatt, and P. Kennedy, “Nudge and shove: Frequency thresholding for navigation in direct brain-computer interfaces,” in Proc. SIGCHI 2001 Conf. Human Factors in Computing Systems, Seattle, WA, Mar. 31–Apr. 5, 2001.
- [11] A. Worden, N. Walker, K. Bharat, and S. Hudson, “Making computers easier for older adults to use: Area cursors and sticky icons,” in Proc. CHI ’97, Atlanta, GA, pp. 266–271.
- [12] (2002) BCI2000. Wadsworth Center. [Online]. Available: http://www.bciresearch.org/BCI2000/bci20000.html
- [13] J. Mankoff, M. Moore, and U. Batra, “Web accessibility for low bandwidthinput,” in Proc.ASSETS2002, Edinburgh, U.K.,July10–12, 2002.
- [14] M. Moore and O. Tomori, “The neurally controllable web browser (BrainBrowser),” in Proc. SIGCHI 2003, Fort Lauderdale, FL, Apr. 2003.

# Linear and Nonlinear Methods for Brain–Computer Interfaces

Klaus-Robert Müller, Charles W. Anderson, and Gary E. Birch

Abstract—At the recent Second International Meeting on Brain–Computer Interfaces (BCIs) held in June 2002 in Rensselaerville, NY, a formal debate was held on the pros and cons of linear and nonlinear methods in BCI research. Specific examples applying EEG data sets to linear and nonlinear methods are given and an overview of the various pros and cons of each approach is summarized. Overall, it was agreed that simplicity is generally best and, therefore, the use of linear methods is recommended wherever possible. It was also agreed that nonlinear methods in some applications can provide better results, particularly with complex and/or other very large data sets.

Index Terms—Feature spaces, Fisher’s discriminant, linear methods, mathematical programming machines, support vector machines (SVMs).

I. INTRODUCTION

At the First International Meeting on Brain-Computer Interfaces (BCIs) held in June 1999 in Rensselaerville, NY [26], there was a significant amount of discussion around the relative advantages and disadvantages of using linear and nonlinear methods in the development of BCI systems. Therefore, at the recent Second International

Manuscript received September 4, 2002; revised May 24, 2003. The work of K.-R. Müller was supported in part by the Deutsche Forschungsgemeinschaft (DFG) under contracts JA 379/9-1 and JA 379/7-1 and in part by the Bundesministerium fuer Bildung und Forschung (BMBF) under contract FKZ 01IBB02A. The work of C. Anderson was supported in part by the National Science Foundation under Grant 9202100. The work of G. Birch was supported in part by the National Sciences and Engineering Research Council of Canada (NSERC) under Grant 90278-2002.

K.-R. Müller is with Fraunhofer FIRST.IDA, 12489 Berlin, Germany, and also with the Department of Computer Science, the University of Potsdam, 14482 Potsdam, Germany (e-mail: klaus@first.fhg.de).

C. W. Anderson is with the Department of Computer Science, Colorado State University, Fort Collins, CO, 80523 USA (e-mail: anderson@cs.colostate.edu).

G. E. Birch is with the Neil Squire Foundation, Burnaby, BC V5M3Z3 Canada and also with the University of British Columbia, Department of Electrical and Computer Engineering, Vancouver, BC V6T1Z4 Canada.

Digital Object Identifier 10.1109/TNSRE.2003.814484

[Figure 5]

Fig. 1. Simplified functional model of a BCI System adapted from [14].

Meeting on BCIs held in June 2002 in Rensselaerville, NY, a 45-min debate was held on linear versus nonlinear methods in BCI research. The debate format involved a moderator and two discussants. K.-R. Müller from Fraunhofer FIRST.IDA, Berlin, Germany, was the first discussant and he was assigned the task of representing the point of view that linear methods should be used. The other discussant, C. W. Anderson from Colorado State University, Fort Collins, CO, was assigned the counter position that nonlinear approaches should be favored.

The Moderator, G. E. Birch from the Neil Squire Foundation, Vancouver, BC, Canada, started the debate by making a few contextual observations. In particular, the discussants were asked to clarify which aspect or component of the BCI system they were referring to when discussing the pros and cons of a particular method. For instance, in the simplified model of a BCI system given in Fig. 1, it should be clear whether a given method was to be used in the feature extractor or the feature classifier. For instance, an autoregressive (AR) modeling method might be used in the process of extracting features from the electroencephalogram (EEG) signal (for example, see [20]). On the other hand, a nearest neighbor classifier method could be applied in the feature classification process (for example, see [15]). Whichever the case, the context in which a given method is being used should be clearly understood.

In the following two sections, a summary of the discussion related to the use of linear and nonlinear methods in BCI systems is provided.

II. LINEAR METHODS FOR CLASSIFICATION

In BCI research, it is very common to use linear classifiers and this section argues in favor of them. Although linear classification already uses a very simple model, things can still go terribly wrong if the underlying assumptions do not hold, e.g. in the presence of outliers or strong noise which are situations very typically encountered in BCI data analysis. We will discuss these pitfalls and point out ways around them.

Let us first fix the notation and introduce the linear hyperplane classification model upon which we will rely mostly in the following (cf. Fig. 2, see e.g. [7]). In a BCI setup, we measure samples

, where are some appropriate feature vectors in dimensional space. In the training data, we have a class label, e.g. 1 for each sample point . To obtain a linear hyperplane classifier

(1)

we need to estimate the normal vector of the hyperplane and a threshold from the training data by some optimization technique [7]. On unseen data , i.e., in a BCI session, we fix the parameters ( , ) and compute a projection of the new data sample onto the direction of the normal via (1), thus determining what class label should be given to according to our linear model.

1534-4320/03$17.00 © 2003 IEEE

