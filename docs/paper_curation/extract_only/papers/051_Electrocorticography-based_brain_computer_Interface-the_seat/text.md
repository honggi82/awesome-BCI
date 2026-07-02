# Electrocorticography-Based Brain Computer Interface—The Seattle Experience

Eric C. Leuthardt, Kai J. Miller, Gerwin Schalk, Rajesh P. N. Rao, and Jeffrey G. Ojemann

Abstract—Electrocorticography (ECoG) has been demonstrated to be an effective modality as a platform for brain–computer interfaces (BCIs). Through our experience with ten subjects, we further demonstrate evidence to support the power and ﬂexibility of this signal for BCI usage. In a subset of four patients, closed-loop BCI experiments were attempted with the patient receiving online feedback that consisted of one-dimensional cursor movement controlled by ECoG features that had shown correlation with various real and imagined motor and speech tasks. All four achieved control, with ﬁnal target accuracies between 73%–100%. We assess the methods for achieving control and the manner in which enhancing online control can be accomplished by rescreening during online tasks. Additionally, we assess the relevant issues of the current experimental paradigm in light of their clinical constraints.

Index Terms—Brain–computerinterface(BCI),brain–machine interface (BMI), neuroprosthetics.

I. INTRODUCTION

Various signal modalities have been utilized for brain–computer interfaces (BCIs). BCIs can use noninvasive or invasive methods. Noninvasive BCIs mainly use electroencephalographic activity (EEG) recorded from the scalp [1]–[6]. They are easy to use, but they have relatively low spatial resolution [7], [8], are susceptible to artifacts such as electromyographic (EMG) signals, and often require extensive user training. Invasive BCIs use single-neuron activity recorded within the brain [9]–[12]. While they have higher spatial resolution and might allow for many degrees of freedom, they require that tens or hundreds of small electrodes be implanted in the brain and are, as a result, subject to tissue response which can impair their long-term stability [13].

An alternate BCI methodology has been studied in epilepsy patients undergoing invasive monitoring for seizure localization. Electrocorticography (ECoG), which is recorded from electrodes placed on the surface of the brain, has been shown to be a powerful and practical alternative to these other modalities. ECoG has higher spatial resolution than EEG[8],broaderbandwidth,higheramplitude,andfarlessvulnerability to artifacts such as EMG [7], [8], [14]. At the same time, because ECoG is recorded by subdural electrode arrays and thus does not require cortical penetration, it entails less clinical risk andis likelyto have greater long-term stability than single-neuron recording. Leuthardt et al. demonstrated that a high level of control was achieved with minimal training using various real and imagined motor and speech tasks [15].

Manuscript received August 15, 2005; revised March 24, 2006. This work was supported by the National Institute of Health under Grant NIH NS007144 and by JGO-NS41272.

E. C. Leuthardt and J. G. Ojemann are with the Department of Neurological Surgery, School of Medicine, University of Washington, Seattle, WA 98104 USA (e-mail: ericleuhardt@sbcglobal.net).

K. J. Miller is with the Department of Physics, University of Washington, Seattle, WA 98195 USA.

G. Schalk is with the Wadsworth Center, Albany, NY 12201 USA and also with the Electrical, Computer, and Systems Engineering Department, Rensselaer Polytechnic Institute, Troy, NY 12202 USA.

R. P. N. Rao is with the Department of Computer Science, University of Washington, Seattle, WA 98195 USA.

Digital Object Identiﬁer 10.1109/TNSRE.2006.875536

At the University of Washington, our group has further explored the use of ECoG as a signal modality for a BCI platform. We studied patients in whom subdural electrode arrays were implanted in preparation for surgery to remove an epileptic focus. We identiﬁed the locations and frequency bands of ECoG sensorimotor rhythms associated with speciﬁc movements or speech or with imagery of those actions. Subjects could quickly learn to use the ECoG activity associated with either overt motor movement or motor imagery to control a cursor. Because brain signals associated with these tasks often changed once the subject used them for cursor control, we further improved the translation of the subjects’ control over those signals into cursor movement by readjusting locations and frequencies following initial cursor control attempts. These results indicate that by using ECoG, accurate one-dimensional (1-D) BCI control can be rapidly achieved by patients with epilepsy.

II. METHODS

## A. Subjects and Experimental Paradigms

The subjects in this study were ten patients with intractable epilepsy who underwent temporary placement of intracranial electrode arrays to localize seizure foci prior to surgical resection. All gave informed consent. The study was approved by the Human Studies Committee of the University of Washington Medical Center. Prior to this study, these patients had not been trained on a BCI system.

Each patient had a grid and/or strip electrodes placed subdurally on the cortical surface. In some subjects, electrode coverage included sensorimotor or speech cortex areas. The electrodes had an exposed diameter of 2 mm and an interelectrode distance of 1 cm. Grid and strip placements were based solely on the requirements of the clinical evaluation, without any consideration of this study. Following placement of the subdural grid/strips, each patient had postoperative radiographs to verify the location of the electrodes.

## B. Data Collection

Each patient studied was in a sitting position (semi-recumbent), approximately 75 cm from a video screen. In all experiments, we recorded ECoG from up to 64 electrodes from a combination of grids and strips using the general-purpose BCI system BCI2000 [16]. All electrodes were referenced to a scalp electrode, ampliﬁed, bandpass ﬁltered (0.1–220 Hz), digitized at 1000 Hz, and stored. The amount of data obtained varied from patient to patient and depended on the patient’s physical state and willingness to continue.

## C. Signal Identiﬁcation

In order to identify brain signals that might be used for BCI control (i.e., screening procedure), we ﬁrst asked subjects to perform paired blocks of repetitive hand/tongue, foot/shoulder movements, or repetitive speaking of the word “move.” The imagined execution was performed in the same manner as the motor task execution. From spectral analysis of the data gathered with each of the various tasks, we identiﬁed the locations and frequency bands in which amplitude was different between the task and rest. For these analyses, the time-series ECoG data were converted into the frequency domain using an autoregressive model. Those electrodes and frequency bins with the most signiﬁcant task-related amplitude changes (i.e., the highest values of ) were identiﬁed as features to be used to control cursor movement in the subsequent online BCI experiments. Please see Leuthardt et al. [15] for a more in-depth description of the technique.

1534-4320/$20.00 © 2006 IEEE

TABLE I ACTIONS AND IMAGINED ACTIONS, ECoG FREQUENCY BANDS, AND ANATOMIC LOCATIONS USED FOR ECoG CONTROL OF 1-D CURSOR MOVEMENT AND FINAL ACCURACIES OF THAT CONTROL. ACCURACY IS CALCULATED AS NUMBER OF CORRECT TARGETS HIT WITH CURSOR FROM TOTAL NUMBER OF TARGETS PRESENTED DURING FINAL RUN OF SESSION INVOLVING PARTICULAR ACTION

[Figure 1]

## D. ECoG Control of Vertical Cursor Movement Online

In a subset of patients, closed-loop BCI experiments were attempted with the patient receiving online feedback that consisted of 1-D cursor movement controlled by ECoG features that had shown correlation with tasks during the screening procedure. The accuracy expected in the absence of any control was 50%.

The cursor moved vertically every 40 ms, controlled by a translation algorithm based on a weighted linear summation of the amplitudes in the identiﬁed frequency bands from the identiﬁed electrodes for the previous 280 ms (as developed for EEG-based control [17], [18]). The weights were chosen so that this translation algorithm moved the cursor up with task execution (e.g., imagining tongue protrusion) and down with rest. This relationship was explained to the patient prior to the experiments. Please see Leuthardt et al. [15] for a more in-depth description of the technique.

## E. Adjustment of Signal Features

Subsequent to initial real-time experiments, data were subject to the same analysis procedure that was performed during the screening procedure. Although we used signal features that we identiﬁed during the screening procedure in response to particular tasks, and we advised the subject to use the same tasks (i.e., imagined motor or speech) to control the cursor, those signal features might change in response to the online feedback that was provided to the subject. In one patient, in whom anatomic location and frequencies changed compared to the screening procedure, BCI2000 parameters were updated to take advantage of those signal features in subsequent closed-loop experiments.

## F. Anatomical and Functional Mapping

Radiographs were used to identify the stereotactic coordinates of each grid electrode [19], and cortical areas were deﬁned using Talairach’s Co-Planar Stereotaxic Atlas of the Human Brain [20].

III. RESULTS A. Patient Characteristics

Four patients attempted closed-loop BCI control and all rapidly acquired 1-D control. Logistical or technical reasons prevented BCI experiments in other patients. The remaining six did not participate in the actual closed-loop portion of the experiment due to: 1) technical issues

(one patient); 2) clinical constraints (two patients); or 3) the subjects declined further participation (three patients).

## B. Screening Procedure

In all patients, we identiﬁed signal features that strongly changed with task execution. Motor and language tasks (real and imagined) and even sensory tasks produced focal responses in different locations and frequencies. Transformation to stereotactic coordinates demonstrated colocalization of prominent features with expected areas of the brain (e.g., motor activity in motor cortex). Covert tasks generally colocalized withovert taskswith less prominent, butotherwise similar, signals.

## C. Control

Those subjects that performed BCI control completed one to eight 3-min runs separated by 1-min breaks. Over these short training periods (3–24 min), reliable cursor control was achieved (73%–100% accuracy; see Table I).

Notably, in one case (Patient D, see Table I), control was achieved from an electrode overlying the dura using an 80-Hz signal. In this case, the dura was adherent to the brain during surgery and a portion of the electrode array was directly over cortex, with another portion epidural. Online BCI operation was achieved using signal features from an electrode in the epidural space.

Consistently, signal features during closed-loop BCI control differed from those identiﬁed during screening. This was noted on all four subjects in each independent online session for which there was a total of nine. The manner in which these signals differed, however, was variable. In one scenario, when compared against the screening task, there was a general anatomic extension of the signal alteration in which the cortical region demonstrating signal change was of a higher signiﬁcance following online attempts and more spatially spread out in adjacent cortex (see Fig. 1). This occurred in ﬁve of the nine online closed-loop sessions. Alternatively, a markedly different set of signals that might have overlapped only somewhat with the screening features was seen in another case (see Fig. 2). Although the subject was able to acquire BCI control using the originally selected electrode and frequency, many other features changed prominently with the task but were not present during the initial screening. In this case, reassessing early control attempts for better features was critical for success. Accuracy for this subject immediately improved from 71% (i.e., 30 of 42

[Figure 2]

- Fig. 1. Topographic representation of subject’s spectral ECoG signal change during motor task. Figure demonstrates signal changes for task during screening procedure and also during cursor control. Both show difference for signals at 80 Hz. Note that although subject was instructed to use same imagined strategy for both, signal changes are augmented in closed-loop control.

[Figure 3]

[Figure 4]

- Fig. 2. values as function of electrode location and frequency. Note difference between signal features manifested in initial screening (left feature plot) to prominent features found in initial post hoc online analysis and ﬁnal online analysis (center and right feature plots, respectively). Differences emphasize importance of reanalyzing data from online attempts to achieve ECoG control as feature changes during online control may differ from initial features identiﬁed during screening.

[Figure 5]

targets correct) to 94% (49 out of 52) in the runs immediately before and after feature reassessment, respectively. This alteration in optimal signal was seen in four of the nine closed-loop sessions.

Of particular interest was the presence of both focal and widespread signal alterations in the same patient for achieving cursor control (see

- Fig. 3). In this case, BCI was performed on separate occasions using two different signals. In one case [Fig. 3(a)], focal signal change of the signal occurred during BCI; in the other case [Fig. 3(b)], spatially diffuse signal alteration was present during BCI compared to screening.

this study as compared to the original work by Leuthardt et al., the clinical aspects of this experimental paradigm are also better understood; namely, the constraints placed by patient care needs, patient characteristics, and time limitations.

The signiﬁcant ﬁnding of signal alteration between online analysis and initial screening reveals the dynamic nature of the ECoG signal in online BCI usage. Not seen in previous studies, this series of patients demonstrates that by complementing the initial screening procedure with analysis of initial online BCI data helps to conﬁrm the most relevant signals utilized for control and better allows for system adjustment. It can thus enhance the subjects’ subsequent online performance. The difference between screening and control signal characteristics will be an area of future investigation along with any evidence of signal alteration over prolonged online control. The factors underlying these differences are likely to involve a mixture of perceptual, motor, and psychological factors in the user.

IV. DISCUSSION

This paper further conﬁrms that ECoG activity is an effective modality for real-time closed-loop BCI control. All subjects achieved a high level of control with only a few minutes of training. In one subject, control was achieved (accuracy greater than chance alone, or 50%) with more than one task. These ﬁndings provide additional results to demonstrate the efﬁcacy and effectiveness of ECoG as a BCI platform as originally demonstrated by Leuthardt et al. This paper goes beyond that initial demonstration by showing that supplementing the initial screening with a rescreening of initial online data can provide substantive information to improving ﬁnal performance. Also, since a greater number of subjects was available for participation in

While ECoG appears to be a highly effective modality for BCI control, current studies are constrained by the parameters of epilepsy surgery. ECoG is only recorded in patients with intractable epilepsy who are sometimes cognitively impaired due to various pain/sedating medications or frequent seizures. Furthermore, electrode placement is solely determined by the requirements of epilepsy surgery. In addition, between recovery of the patient from electrode implantation

[Figure 6]

Fig. 3. Subject C’s topologies of signal alteration of given task at given frequency (77–83 Hz for column A and 97–103 Hz for column B) used in screening (top row) and corresponding signal alteration of same tasks used in closed-loop control (bottom row). Topologies are superimposed upon lateral skull radiograph with corresponding strip electrodes. Task for column A involved hand movement while task for column B was tongue movement. What is notable is different manner in which subject altered his signal with regard to closed-loop feedback. In column A with hand movement, subject focally tunes signal alteration in response to feedback; while in column B with tongue movement, he diffusely alters his frequency amplitude to accomplish same levels of accuracy.

and electrode removal there is often very limited time, and sometimes limited patient interest, to perform BCI experiments. These limitations must be taken into consideration when designing experiments for invasively monitored subjects such that they will be appropriate to the subjects clinical needs, their given cognitive status, and the time available to perform the study.

Though less invasive than BCI methods that rely on electrodes that penetrate the brain, the practical utility of ECoG still remains limited by the need for subdural installation and a craniotomy. The ﬁndings within this study that BCI control was accomplished using epidural electrodes, though a single instance for which general conclusions cannot yet be drawn, provide exciting data for further study that an epidural derived signal may be similarly effective as BCI control using subdural electrodes. If ECoG can be recorded from small epidural contacts, ECoG could serve as a BCI method that is not only powerful but also clinically practical.

REFERENCES

- [1] J. J. Vidal, “Real-time detection of brain events in EEG,” IEEE Proc. Special Issue Biological Signal Processing Analysis, vol. 65, pp. 633–664, 1977.
- [2] E. E. Sutter, “The brain response interface: communication through visually-induced electrical brain responses,” J. Microcomp. Applicat., vol. 15, pp. 31–45, 1992.
- [3] T. Elbert, B. Rockstroh, W. Lutzenberger, and N. Birbaumer, “Biofeedback of slow cortical potentials,” Electroencephalogr. Clin. Neurophysiol., vol. 48, pp. 293–301, 1980.

- [4] L.A. FarwellandE. Donchin,“Talking offthetopofyourhead:Toward a mental prosthesis utilizing event-related brain potentials,” Electroencephalogr. Clin. Neurophysiol., vol. 70, pp. 510–523, 1988.
- [5] J. R. Wolpaw, D. J. McFarland, G. W. Neat, and C. A. Forneris, “An EEG-based brain-computer interface for cursor control,” Electroencephalogr. Clin. Neurophysio., vol. 78, pp. 252–259, 1991.
- [6] G. Pfurtscheller, D. Flotzinger, and J. Kalcher, “Brain-computer interface—A new communication device for handicapped persons,” J. Microcomp. Applicat., vol. 16, pp. 293–299, 1993.
- [7] W. J. Freeman, M. D. Holmes, B. C. Burke, and S. Vanhatalo, “Spatial spectra of scalp EEG and EMG from awake humans,” Clin. Neurophysiol., vol. 114, pp. 1053–1068, 2003.
- [8] R. Srinivasan, P. L. Nunez, and R. B. Silberstein, “Spatial ﬁltering and neocortical dynamics: Estimates of EEG coherence,” IEEE Trans. Biomed. Eng., vol. 45, no. 4, pp. 814–826, Dec. 1998.
- [9] P. R. Kennedy and R. A. Bakay, “Restoration of neural output from a paralyzed patient by a direct brain connection,” Neurorep., vol. 9, pp. 1707–1711, 1998.
- [10] A. P. Georgopoulos, A. B. Schwartz, and R. E. Kettner, “Neuronal population coding of movement direction,” Science, vol. 233, pp. 1416–1419, 1986.
- [11] M. Laubach and J. Wessberg, “Cortical ensemble activity increasingly predicts behavior outcomes during learning of a motor task,” Nature, vol. 405, pp. 567–571, 2000.
- [12] D. M. Taylor, S. I. Tillery, and A. B. Schwartz, “Direct cortical control of 3D neuroprosthetic devices,” Science, vol. 296, pp. 1829–1832, 2002.
- [13] W. Shain et al., “Controlling cellular reactive responses around neural prosthetic devices using peripheral and local intervention strategies,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 11, pp. 186–188, 2003.

- [14] Boulton, G. B. Baker, and C. H. Vanderwolf, Neurophysiological Techniques, II: Applications to Neural Systems. Totowa, NJ: Humana, 1990, pp. 277–312.
- [15] E. C. Leuthardt, G. Schalk, J. W. Wolpaw, J. G. Ojemann, and D. W. Moran, “A brain computer interface using electrocorticographic signals in humans,” J. Neural Eng., vol. 1, no. 2, pp. 63–62, 2004.
- [16] G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw, “BCI2000:Developmentofageneralpurposebrain-computer interface (BCI) system,” IEEE Trans. Biomed. Eng., vol. 51, no. 8, pp. 1034–1043, Aug. 2001.
- [17] H. Ramoser, J. R. Wolpaw, and G. Pfurtscheller, “EEG-based communication: Evaluation of alternative signal prediction methods,” Biomed. Tech. (Berl), vol. 42, pp. 226–233, 1997.
- [18] D. J. McFarland and J. R. Wolpaw, “EEG-based communication and control: speed-accuracy relationships,” Appl. Psychophysiol Biofeedback, vol. 28, pp. 217–223, 2003.
- [19] P. T. Fox, J. S. Perlmutter, and M. E. Raichle, “A stereotactic method of anatomical localization for positron emission tomography,” J. Comput. Assist. Tomogr., vol. 9, pp. 141–153, 1985.
- [20] J. Talairach and P. Tournoux, Co-Planar Sterotaxic Atlas of the Human Brain. New York: Thieme, 1988.

# Could Cortical Signals Control Intraspinal Stimulators? A Theoretical Evaluation

Vivian K. Mushahwar, Lisa Guevremont, and Rajiv Saigal

Abstract—In this paper, we examine the control signals that are required to generate stepping using two different intraspinal microstimulation (ISMS) paradigms and discuss the theoretical feasibility of controlling ISMS-evoked stepping using a brain computer interface. Tonic (constant amplitude) and phasic (modulated amplitude) ISMS protocols were used to produce stepping in the hind limbs of paralyzed cats. Low-amplitude tonic ISMS activated a spinal locomotor-like network that resulted in bilateral stepping of the hind limbs. Phasic ISMS generated coordinated stepping by simultaneously activating ﬂexor synergies in one limb coupled with extensor synergies in the other. Using these ISMS paradigms, we propose that one or two independent cortical signals will be adequate for controlling ISMS-induced stepping after SCI.

Index Terms—Functional electrical stimulation, intraspinal microstimulation, locomotion, spinal cord injury.

I. INTRODUCTION

Spinal cord injury (SCI), stroke, and neurodegenerative diseases such as amyotrophic lateral sclerosis (ALS) often result in paralysis, leaving an individual without the ability to perform normal motor functions. The development of brain–computer interface (BCI) systems has allowed otherwise incapacitated individuals to control external devices through the use of volitionally-generated cortical signals [1]–[9]. A single isolated cortical signal has been shown to be sufﬁcient for basic tasks such as controlling a light switch [1], and even more complex tasks including moving a computer cursor [2], spelling out messages [3], or controlling an upper extremity grasping neuroprosthesis [4].

Wolpaw and McFarland [5] demonstrated that two signiﬁcantly different control signals could be extracted from EEG activity recorded from human subjects. In a more recent study, they were able to achieve electroencephalogram (EEG)-based two-dimensional control of a computer cursor, with results comparable to those obtained from monkeys implanted with multiple cortical recording electrodes [10]. The ability to extract two independent cortical control signals could conceivably lead to the use of EEG to control advanced systems with multiple degrees-of-freedom. If a single control signal can currently be used to generate a grasping movement, a more complete reaching task (including elbow and wrist movements) may be achieved by using as few as six independent control signals [2] obtained through a high-resolution BCI system.

In this paper, we discuss the feasibility of extending the use of BCIs to include the control of lower-limb functional electrical stimulation (FES) systems aimed at restoring locomotion in individuals with complete SCI. Intraspinal microstimulation (ISMS) has been suggested as a potential FES technique for restoring standing and walking after SCI [11], [12]. The lumbar enlargement (5 cm long in humans), is the target region for implantation and contains motoneurons innervating all lower

Manuscript received October 17, 2005; revised March 15, 2006; March 20, 2006. This work was supported in part by the Alberta Heritage Foundation for Medical Research, in part by the Canadian Institutes for Health Research and in part by the National Institutes of Health.

V. K. Mushahwar is with the Department of Biomedical Engineering and Centre for Neuroscience, University of Alberta, Edmonton, AB, T6G 2S2 Canada (e-mail: Vivian.mushahwar@ualberta.ca).

L.Guevremontiswith theDepartment ofBiomedicalEngineering,University of Alberta, Edmonton, AB, T6G 2S2 Canada (e-mail: lg@ualberta.ca).

R. Saigal is with the Division of Health Sciences and Technology, HarvardMIT, Cambridge, MA 201390 USA (e-mail: rsaigal@mit.edu).

Digital Object Identiﬁer 10.1109/TNSRE.2006.875532

1534-4320/$20.00 © 2006 IEEE

