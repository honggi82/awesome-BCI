TYPE Original Research
PUBLISHED 14 March 2023
DOI 10.3389/fnhum.2023.1117670
OPEN ACCESS
EDITED BY
Aleksandar Miladinovi´c,
Institute for Maternal and Child Health IRCCS
“Burlo Garofolo”, Italy
REVIEWED BY
Miloš Ajcevic,
University of Trieste, Italy
Giovanni Furlanis,
Azienda Sanitaria Universitaria Integrata di
Trieste, Italy
*CORRESPONDENCE
Chen Li
lichen@tmu.edu.cn
SPECIALTY SECTION
This article was submitted to
Brain-Computer Interfaces,
a section of the journal
Frontiers in Human Neuroscience
RECEIVED 06 December 2022
ACCEPTED 28 February 2023
PUBLISHED 14 March 2023
CITATION
Liao W, Li J, Zhang X and Li C (2023) Motor
imagery brain–computer interface
rehabilitation system enhances upper limb
performance and improves brain activity
in stroke patients: A clinical study.
Front. Hum. Neurosci. 17:1117670.
doi: 10.3389/fnhum.2023.1117670
COPYRIGHT
© 2023 Liao, Li, Zhang and Li. This is an
open-access article distributed under the terms
of the Creative Commons Attribution License
(CC BY). The use, distribution or reproduction
in other forums is permitted, provided the
original author(s) and the copyright owner(s)
are credited and that the original publication in
this journal is cited, in accordance with
accepted academic practice. No use,
distribution or reproduction is permitted which
does not comply with these terms.
Motor imagery brain–computer
interface rehabilitation system
enhances upper limb
performance and improves brain
activity in stroke patients: A
clinical study
Wenzhe Liao1, Jiahao Li1, Xuesong Zhang2 and Chen Li3*
1State Key Laboratory of Reliability and Intelligence of Electrical Equipment, School of Artiﬁcial
Intelligence, Hebei University of Technology, Tianjin, China, 2Department of Neurosurgery, The Second
Hospital of Hebei Medical University, Shijiazhuang, Hebei, China, 3Tianjin Key Laboratory
of Environment, Nutrition and Public Health, Department of Occupational and Environmental Health,
School of Public Health, Tianjin Medical University, Tianjin, China
This study compared the efﬁcacy of Motor Imagery brain-computer interface
(MI-BCI) combined with physiotherapy and physiotherapy alone in ischemic
stroke before and after rehabilitation training. We wanted to explore whether
the rehabilitation effect of MI-BCI is affected by the severity of the patient’s
condition and whether MI-BCI was effective for all patients. Forty hospitalized
patients with ischemic stroke with motor deﬁcits participated in this study. The
patients were divided into MI and control groups. Functional assessments were
performed before and after rehabilitation training. The Fugl-Meyer Assessment
(FMA) was used as the primary outcome measure, and its shoulder and elbow
scores and wrist scores served as secondary outcome measures. The motor
assessment scale (MAS) was used to assess motor function recovery. We used
non-contrast CT (NCCT) to investigate the inﬂuence of different types of
middle cerebral artery high-density signs on the prognosis of ischemic stroke.
Brain topographic maps can directly reﬂect the neural activity of the brain,
so we used them to detect changes in brain function and brain topological
power response after stroke. Compared the MI group and control group after
rehabilitation training, better functional outcome was observed after MI-BCI
rehabilitation, including a signiﬁcantly higher probability of achieving a relevant
increase in the Total FMA scores (MI = 16.70 ± 12.79, control = 5.34 ± 10.48),
FMA shoulder and elbow scores (MI = 12.56 ± 6.37, control = 2.45 ± 7.91),
FMA wrist scores (MI = 11.01 ± 3.48, control = 3.36 ± 5.79), the MAS scores
(MI = 3.62 ± 2.48, control = 1.85 ± 2.89), the NCCT (MI = 21.94 ± 2.37,
control = 17.86 ± 3.55). The ﬁndings demonstrate that MI-BCI rehabilitation
training could more effectively improve motor function after upper limb motor
dysfunction after stroke compared with routine rehabilitation training, which
veriﬁes the feasibility of active induction of neural rehabilitation. The severity of
the patient’s condition may affect the rehabilitation effect of the MI-BCI system.
KEYWORDS
MI-BCI, upper limb, motor function rehabilitation, stroke rehabilitation, incurable patient
Frontiers in Human Neuroscience
01
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
1. Introduction
Ischemic stroke refers to the necrosis of brain tissue caused
by stenosis or occlusion of the feeding arteries of the brain
(carotid artery and vertebral artery) and insuﬃcient blood supply
to the brain. Brain tissue damage leads to the rupture of the
brain nerve pathways that control movement, language, and other
functions, resulting in hemiplegia and even disability. According
to the World Health Organization, stroke is the main cause
of disability and mortality in China. In 2019, the number of
stroke deaths reached 2.19 million, and there were 3.94 million
new stroke cases. The number of stroke patients in China
has maintained a sharp upward trend in recent years (China
National Health Commission, 2021). Stroke patients have diﬃculty
taking care of themselves because of motor dysfunction, which
seriously aﬀects their physical and mental health (Lee et al., 2021).
Recovery of motor function in stroke patients has become an
important topic in the ﬁeld of rehabilitation. BCI methods are
among the most eﬀective tools for the design of rehabilitation
systems. Quantitative electroencephalography (QEEG) can assist
in detecting or predicting stroke evolution of stroke (Simon et al.,
2007). An electroencephalogram (EEG) can assess the severity of
stroke and can be used as a supplementary tool in the monitoring
of acute ischemic stroke (Ajˇcevi´c et al., 2021a). Non-invasive
EEG can use the neurophysiological biomarkers obtained in the
early stage before treatment as a prognostic parameter, which
can help improve rehabilitation treatment (Ajˇcevi´c et al., 2021b).
With advances in brain science and computer technology, many
BCI studies have focused on decoding EEG signals associated
with whole-body kinematics/kinetics, motor imagery, various
senses, and neuroprosthetic and neurorehabilitation devices (Abiri
et al., 2019). Virtual reality (VR) can increase the eﬃciency
of BCI rehabilitation systems. Functional electrical stimulation,
robotic assistance, and Hybrid VR based models are the main
BCI approaches for designing stroke rehabilitation systems
(Muhammad et al., 2020). Stroke rehabilitation is based on
plasticity of the nervous system. Repeated feedback stimulation
during learning and training can strengthen the connections
between neuronal synapses, thus helping to gradually repair,
compensate, and reconstruct the cerebral cortex and other
rehabilitation eﬀects (Morioka et al., 2018). The MI-BCI is an
active interaction mode (Jessica et al., 2018). When the human
body performs motion imagination but the real limb has no
obvious action, the sensorimotor cortex of the brain is in an active
state (Alexandra et al., 2021). Compared with passive stimulation,
active participation in the imagination process has a stronger
inducing eﬀect on the plasticity of the central nervous system.
MI-BCI can promote reorganization of damaged brain regions
and neural pathways by recruiting and enhancing the activity of
undamaged neurons. Motor imagery has the potential to induce
plasticity in the brain cells. It can accelerate the repair of neural
functional connections between the external limbs and brain.
The motor imaging brain–computer interface (MI-BCI) based
on motor imagination converts the neural activity signals of the
brain into control signals of computers or external devices. It can
not only help people with limb movement disorders eﬀectively
control external devices but also provide a new strategy for
rehabilitation treatment of stroke patients (Ana et al., 2021). The
use of BCIs has signiﬁcant immediate eﬀects on the improvement
of hemiparetic upper extremity function in patients after stroke,
however, the limited number of studies does not support its long-
term eﬀects. BCIs combined with functional electrical stimulation
may be better for functional recovery than other types of neural
feedback (Bai et al., 2020). BCI–FES rehabilitation training can
induce clinically signiﬁcant improvements in motor function in
chronic stroke patients. It can improve the functional integration
and separation of brain networks and boost compensatory activity
in the contralesional hemisphere to a certain extent (Zhan et al.,
2022). MI-BCI can not only help patients with Limb Dyskinesia to
eﬀectively control external devices but also provide a new strategy
for rehabilitation treatment (Kamal et al., 2021).
In this study, we designed an MI-BCI rehabilitation application
system using EEG and visual, auditory, and electromyographic
stimulation feedback. Forty stroke patients will be randomly
divided into MI and control groups. The MI group will receive
routine treatment and MI-BCI treatment, whereas the control
group will only receive routine treatment. The feasibility and
eﬀectiveness of the MI-BCI system in the upper limb rehabilitation
of stroke patients were veriﬁed by comparing the clinical scale,
NCCT, and EEG between the two groups. By comparing the
rehabilitation of motor function of patients in the MI group before
and after treatment, we preliminarily explored whether the severity
of the disease aﬀects the use of MI-BCI and whether MI-BCI can be
used by all patients.
2. Materials and methods
2.1. General information
During the rehabilitation process, patients with stroke were
selected from a hospital between February 2019 and May 2020.
(1) Inclusion criteria:  those who met the diagnostic criteria of
the Chinese guidelines for the diagnosis and treatment of acute
ischemic stroke 2019 (formulated and issued by the cerebrovascular
disease group of the neurology branch of the Chinese Medical
Association) and had upper limb dysfunction and were responsible
lesions;  The patient had the ﬁrst onset and was in the
recovery period of ischemic stroke;  Age 35–70 years old,
without obvious cognitive dysfunction and in good mental state;
 Before the clinical trial, they did not receive formal motor
imagery therapy; (2) Exclusion criteria:  in the ﬁrst aid, the
patient is not out of danger and the vital signs are not stable;
 Having various primary malignant tumors, serious heart, liver,
lung, kidney, endocrine, hematopoietic, immune system and other
serious diseases (including but not limited to tumor, heart, lung,
endocrine, blood and immune system diseases);  The patient has
arthritis, rheumatoid, fracture and other diseases or symptoms that
aﬀect the motor function of the upper limb;  Patients who are
mentally abnormal or relatively resistant to treatment;  Patients
or their family members cannot sign the informed consent form
and cannot cooperate to insist on treatment.
First, the data were collected from 47 patients. During the
initial MI-BCI data collection process, three patients were excluded
because the accuracy of EEG collection was lower than the
standard, and four patients voluntarily withdrew for personal
reasons. According to the random distribution method and
personal will, the patients were divided into the MI group (20
Frontiers in Human Neuroscience
02
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
cases) and the control group (20 cases) (and the other 7 cases were
added to the control group with the consent of themselves and
their families, and they were given routine medical rehabilitation
treatment instead of EEG-related rehabilitation training). Finally, a
total of 20 stroke patients participated in the entire MI-BCI upper-
limb rehabilitation training and voluntarily participated in the
trial. They or their families signed an informed consent form and
were able to adhere to treatment and examination. This study was
reviewed and approved by the hospital ethics committee (approval
number: Hebuthmec 2019002). The purpose of the experiment was
to perform scene EEG acquisition and upper-limb rehabilitation
training for stroke patients. This is a non-invasive experiment that
will not cause harm to subjects and protect patients’ privacy. After
initial treatment, patients regain basic mobility and then undergo
rehabilitation in community hospitals; therefore, follow-up after 3–
6 months is diﬃcult to perform. The project team collected data
before and after rehabilitation in a stroke hospital.
2.2. Research methods
All treatments in the MI and control groups were performed
in accordance with “Chinese Guidelines for Stroke Prevention
and Treatment (2021 edition).” The entire rehabilitation system
consists of a mobile portable host, 64 channel EEG systems,
myoelectric stimulation system, and motion imagination software.
The repair of upper-limb motor neuron injury is completed
through two categories of motor imagination. The patient imagines
left- or right-hand movements, and the EEG ampliﬁer transmits
the patient’s EEG to the BCI online system. The online system
analyses the EEG to obtain an output command, and the functional
myoelectric stimulation equipment stimulates the limbs to provide
feedback to the nervous system. Another external nerve pathway
was built through the MI-BCI and myoelectric stimulation systems.
Data Collection and Preprocessing: As shown in Figure 1, the
EEG data were collected from 64 electrodes positioned according
to the international extended 10–20 system. In the evaluation
process, the EEG data was selected from 28 (“FPZ,” “FZ,” “FCZ,”
“CZ,” “TP7,” “CP5,” “CP3,” “CP1,” “CPZ,” “CP2,” “CP4,” “CP6,” “P7,”
“P5,” “P3,” “P1,” “PZ,” “P2,” “P4,” “P6,” “P8,” “PO7,” “POZ,” “PO4,”
“PO8,” “O1,” “OZ,” “O2”) electrodes. EEG signals were sampled
at 1000 Hz (SynAmps2, Neuroscan, USA). All 28 channels were
grounded between the Fpz and Fz channels, and referenced to the
binaural mastoid.
Surface EMG data were recorded using Pico EMG sensors
(Cometa Italy2) from 16 muscles collected in a bipolar fashion:
extensor digitorum, ﬂexor digitorum superﬁcialis, lateral head of
the triceps muscle, long head of the biceps brachii muscle, pectoralis
major, lateral deltoid, anterior deltoid, and upper trapezius on both
sides. The EMG sensors were placed according to the guidelines
reported by Barbero et al. (2012).
2.2.1. MI group
MI group received MI-BCI rehabilitation training and routine
rehabilitation training.
(1) MI-BCI rehabilitation training: The patient sat on a
comfortable chair, 70 cm away from the monitor, the visual
interface was located in the center of the 22 inch LCD, the
resolution was 1920 × 1080 pixels, the screen refresh rate was
60 Hz, and the EEG sampling frequency was 1000 Hz (the
electrodes were arranged according to the International 10–
20 Standard Guide System). After sitting down, the patient
began rehabilitation. The patient was relaxed and looked
directly at the monitor. Based on the rehabilitation process
of stroke patients, we built a set of MI-BCI visual and
auditory stimulation systems using E-Prime 3.0 software
(which can present a combination of multiple stimuli). Play
a set daily motion animation of the upper limbs on the
screen (including but not limited to grasping, placing, lifting,
lowering, rotating, and other actions). The asynchronous
amplitude (SOA) at the beginning of stimulation was set to 5 s
to ensure that the patient understood the visual stimulation.
This 5 s includes displaying a slow-moving image for 3.5 s
and then masking the image for 1.5 s. One process included
12 image appearance processes, and the patients were allowed
to rest for 1 min between processes. Complete rehabilitation
training was repeated the whole process 50 times. During
rehabilitation, the EEG acquisition system recognizes the
signals of patients. The EEG signals were then converted
into motion commands. The motor command controls the
myoelectric stimulation system to stimulate the limb muscles
of the patient. In the entire process of rehabilitation treatment,
professional rehabilitation physiotherapists assist patients
FIGURE 1
Motor imagery brain-computer interface (MI-BCI) upper limb rehabilitation system. (A) Ideal MI-BCI system. (B) Actual usage diagram.
Frontiers in Human Neuroscience
03
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
in completing their movements. During the rehabilitation
process, the patient tries to avoid non-subjective movements
(including, but not limited to, itching, coughing, yawning,
blinking, etc.). The patient will be treated for 3 weeks, 5 days a
week, for 45–60 m a day.
(2) Routine rehabilitation training, balance training, standing
training, standing and sitting balance training, center of
gravity transfer training, bed and chair transfer training,
walking training, brace and auxiliary Walker training, and
daily living ability training (grooming, mobility, dressing, and
toilet). Physiotherapists will adjust the rehabilitation plan in
a timely manner according to the patient’s condition, and
evaluate the training eﬀect.
2.2.2. Control group
The control group only completed routine rehabilitation
training. Training time, frequency, and content were the same as
those in the MI group.
2.3. Functional assessment
After 21 days of rehabilitation training, the staﬀassessed the
patients’ exercise abilities and physical status. All assessments were
performed by the same trained staﬀwho were blinded to the
patient’s rehabilitation.
(1) FMA motor function score: The fugl-meyer assessment
(FMA) was used to assess the upper limb motor function of
patients in the MI and control groups, ignoring the upper limb
sensory, passive joint mobility and pain sections of the table,
and the reﬂexes section; only the 33 items in the upper limb
section were used for this assessment, with a total score of 0–2
for individual items and 0–66 for the total score, based on 34
points for shoulder and elbow, 22 points for wrist and hand,
and 10 points for motor coordination, with higher overall
scores indicating better upper limb motor function.
(2) MAS motor function score: The motor assessment scale
(MAS) was used to assess the comprehensive motor function
and muscle tension of the body, which can eﬀectively observe
the curative eﬀect and recovery of sensory movement on
the aﬀected side, ignoring the ﬁve functions of posture
change and walking in the scale. This assessment used only
four items: upper limb function, hand function, and general
muscle tension. The individual score was 0–6 points, and the
total score was 0–24 points. A higher score indicated better
comprehensive motor function of the upper limb.
(3) Hyperdense middle cerebral artery sign (HMCAS): On non-
contrast CT (NCCT) examination, the diseased cerebral artery
presents a high-density signal compared to the contralateral
one. It has been suggested that cerebral artery occlusion
occurs in acute cerebral infarction in the cerebral artery-
supplying area. NCCT can distinguish between cerebral
hemorrhage and cerebral ischemia based on density changes
in the visible vascular running area. A high density may lead
to acute thrombosis, resulting in slow blood ﬂow, stagnation,
and even arterial occlusion.
(4) Clinical eﬃcacy: Neurological deﬁcit scores of Chinese
patients with stroke were used as the criteria for determining
eﬃcacy. The functional impairment scores included the FMA,
MAS, and HMCAS. When two of the three scores were
met, patients were included at this level. Full rehabilitation:
disability level 0 with 91% to 100% reduction in functional
impairment score; signiﬁcant rehabilitation: disability level
1–2 with 46% to 90% reduction in functional impairment
score; general rehabilitation: disability level 3–4 with 18%
to 45% reduction in functional impairment score; no
change: no improvement in disease; deterioration (including
death): increased functional impairment score compared
to pre-rehabilitation. After rehabilitation training, general
rehabilitation, signiﬁcant rehabilitation, and full rehabilitation
can be considered eﬀective rehabilitation; no change or
deterioration can be considered invalid rehabilitation.
(5) Brain topographic map: A plane graph of the spherical
scalp represented by diﬀerent colors of power values in each
frequency band of the brain wave. When a certain region of
the cerebral cortex is activated by various factors, the blood
ﬂow and metabolic activity in this region change with an
increase in the activation intensity. As the stimulus increases,
the eﬀect of brain information modulation decreases and
the amplitude of the EEG signal in the alpha and beta
frequency bands decreases, which is called event-related
desynchronization (ERD). That is, the event-induced spectral
component was lower than the spontaneous spectral value,
which was identiﬁed as negative in event-related spectral
perturbation (ERSP). In contrast, the eﬀect of information
modulation in the brain is improved in the resting state,
and the phenomenon of EEG signal spectrum amplitude is
called event-related synchronization (ERS), which indicates
that the event-induced EEG spectrum component is higher
than the spontaneous EEG spectrum value, and it is identiﬁed
as positive in ERSP.
2.4. Statistical analysis
Statistical software (SPSS 26.0) was used for the data
analysis. The diﬀerence was considered statistically signiﬁcant
when
the
bilateral
p-value
was
<0.05.
The
Shapiro–Wilk
test was used to test the normality of quantitative data.
(x
±
s)
was
used
to
represent
the
measurement
data
conforming
to
the
normal
distribution.
Qualitative
data
were explained by the number of cases and the component
ratio (n [%]). The t-test was used to compare diﬀerences in
continuous variables. χ2 test and comparison of diﬀerences in
categorical variables.
3. Results and discussion
3.1. Comparison of patients
As shown in Table 1, in the MI group, there were 8 males
and 12 females; the age range was 40–72 years, with a mean of
Frontiers in Human Neuroscience
04
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
TABLE 1 Basic patient information.
Information
MI group
Control group
P-values
Gender
Male
8
9
Female
12
11
Age
61.5 ± 3.8
61.0 ± 3.7
0.90
Course of disease (day)
20.1 ± 2.2
20.6 ± 2.4
0.31
Aﬀected side
Left
9
8
0.46
Right
11
12
Cerebral vascular disease
Yes
20
18
0.87
No
0
2
Coronary heart disease
Yes
17
14
0.68
No
3
6
Diabetes
Yes
6
7
0.74
No
14
13
History of hypertension
Yes
19
18
0.87
No
1
2
Hyperlipidemia
Yes
5
3
0.69
No
15
17
Drinking
Yes
6
7
0.75
No
14
13
Exercise habits
3 times a week or more
3
6
0.83
Twice a week or less
10
10
None
7
4
Total FMA scores
18.50 ± 6.46
18.70 ± 6.23
0.35
FMA shoulder and elbow scores
9.80 ± 3.51
9.50 ± 3.25
0.27
FMA wrist scores
5.65 ± 2.15
6.10 ± 2.14
0.15
MAS scores
6.00 ± 2.22
5.95 ± 2.68
0.24
Brain NCCT
83.65 ± 5.93
82.45 ± 5.70
0.79
TABLE 2 Comparison of total FMA scores between the MI and control group.
Total FMA scores
Groups
Before rehabilitation training
After rehabilitation training
Difference
t
p
MI group
18.50 ± 6.46
40.80 ± 14.92
16.70 ± 12.79
−3.141
0.003
Control group
18.70 ± 6.23
30.15 ± 15.06
5.34 ± 10.48
−4.759
0.004
Diﬀerence
1.31 ± 0.73
11.45 ± 6.90
p
0.35
0.003
FMA shoulder and elbow scores
MI group
9.80 ± 3.51
20.85 ± 7.76
12.56 ± 6.37
−3.078
0.004
Control group
9.50 ± 3.25
15.30 ± 7.77
2.45 ± 7.91
−2.527
0.005
Diﬀerence
0.83 ± 0.51
6.21 ± 2.12
p
0.27
0.005
FMA wrist scores
MI group
5.65 ± 2.15
13.00 ± 5.11
11.01 ± 3.48
−2.938
0.006
Control group
6.10 ± 2.14
9.75 ± 5.15
3.36 ± 5.79
−2.271
0.007
Diﬀerence
0.42 ± 0.12
4.27 ± 1.43
p
0.15
0.007
Frontiers in Human Neuroscience
05
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
(61.5 ± 3.8) years; the duration of illness was 14–38 days, with
a mean of (20.1 ± 2.2) days. In the control group, there were 9
males and 11 females; the age range was 38–67 years, with a mean
of (61.0 ± 3.7) years; the duration of illness was 16–40 days, with
a mean of (20.6 ± 2.4) days. The diﬀerences between the MI and
control groups were not statistically signiﬁcant (P > 0.05).
3.2. Comparison of affected side FMA
scores between the MI and control group
As shown in Table 2, after rehabilitation training, the total FMA
score, shoulder and elbow score and wrist score of all patients
improved signiﬁcantly, and the diﬀerences were statistically
signiﬁcant (P < 0.05). All diﬀerences in the FMA scores were
signiﬁcantly higher in the MI group than in the control group
after rehabilitation.
3.3. Comparison of affected side MAS
score of between the MI and control
group
As shown in Table 3, after rehabilitation training, the MAS
scores of both groups were higher than before treatment, and
the MAS scores of the MI group were signiﬁcantly higher than
those of the control group after treatment, and the diﬀerence was
statistically signiﬁcant (P < 0.05).
3.4. Comparison of brain status between
the MI and control group
As shown in Table 4, hyperdense middle cerebral artery sign
is an indirect sign of cerebral infarction caused by occlusion
of the cerebral artery. The high-density component represents
blood clots, thrombi, or emboli in the cerebral artery lumen.
The CT value of ﬂowing blood is approximately 40Hu, which
is linearly correlated with the hemoglobin concentration. Before
rehabilitation treatment, the arterial high-density sign of NCCT
TABLE 5 Comparison of the clinical efﬁcacy between the MI
and control group.
Clinical efﬁcacy
MI group
Control group
Full rehabilitation
3 (15%)
1 (5%)
Signiﬁcant rehabilitation
10 (50%)
7 (35%)
General rehabilitation
6 (30%)
7 (35%)
No change
1 (5%)
5 (25%)
Deterioration
0
0
Eﬀective rehabilitation
19 (95%)
15 (75%)
was relatively high, and after rehabilitation training treatment, the
NCCT arterial high-density sign values of the two groups were
lower than those before rehabilitation treatment, and those of the
MI group were lower than those of the control group, and the
diﬀerence was statistically signiﬁcant (P < 0.05).
3.5. Comparison of clinical efﬁcacy
between the MI and control group
As
shown
in
Table
5,
full
rehabilitation,
signiﬁcant
rehabilitation, and general rehabilitation can be considered
eﬀective rehabilitation; no change or deterioration can be
considered invalid rehabilitation. The total eﬀective rate of the MI
group was 95% (19/20), which was higher than that of the control
group (75%, 15/20).
3.6. Comparison of brain topographic
between the MI and control group
The average power spectral density (PSD) of each channel
was calculated according to the spatial spectral characteristics
of EEG signals under tactile stimulation feedback. Finally, the
PSD value was mapped to the topographic map to determine
the spatial spectral characteristics of brain oscillations. The event-
related spectral perturbation power of all subjects in typical
frequency bands of 8–30 Hz (alpha:8–13 Hz, beta:14–29 Hz)
TABLE 3 Comparison of MAS scores on the affected side between the MI and control group.
Groups
Before rehabilitation training
After rehabilitation training
Difference
t
p
MI group
6.00 ± 2.22
13.6 ± 5.18
3.62 ± 2.48
−3.50
0.001
Control group
5.95 ± 2.68
10.75 ± 5.51
1.85 ± 2.89
0.157
0.002
Diﬀerence
0.59 ± 0.13
3.98 ± 1.28
p
0.24
0.006
TABLE 4 Comparison of the affected brain NCCT between the MI and control group.
Groups
Before rehabilitation training
After rehabilitation training
Difference
t
p
MI group
83.65 ± 5.93
60.70 ± 11.71
21.94 ± 2.37
3.216
0.003
Control group
82.45 ± 5.70
72.10 ± 13.21
17.86 ± 3.55
−10.99
0.003
Diﬀerence
3.27 ± 0.97
15.76 ± 3.21
p
0.79
0.002
Frontiers in Human Neuroscience
06
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
(Pfurtscheller and Da Silva, 1999; Graimann et al., 2002) was
extracted, and a brain topographic map was drawn.
As shown in Figure 2, after 3 weeks of training, compared
with passive routine rehabilitation, the rehabilitation process with
MI-BCI, EMG stimulation, and feedback had signiﬁcantly higher
ERD at–8–30 Hz (alpha band and beta band). This phenomenon
indicates that the brain actively participates in physical activity. By
comparing PSD, the ERD characteristic sensory pattern of motor-
related areas in the full rehabilitation MI group was signiﬁcantly
enhanced, but the regularity of enhancement was diﬀerent, and
the power distribution area was relatively scattered. In addition,
it was found that during motor imagery, the PSD topographic
maps of both limbs were similar and the bilateral sensory cortex
areas were activated. Comparing the brain topography of the
two groups before and after rehabilitation, the full rehabilitation
patients had the strongest response to the MI-BCI stimulation; the
signiﬁcant rehabilitation patients had a more obvious response to
the stimulation, the general rehabilitation patients had no obvious
response to the stimulation, and the no change patients had no
response to the stimulation. Compared with the two groups, the
response of the MI group patients with full rehabilitation and
signiﬁcant rehabilitation to MI-BCI stimulation was completely
stronger than that of the control group patients. However, the
responses of the two groups of general rehabilitation and no change
in patients to stimulation were similar to those of patients, and
there was no signiﬁcant diﬀerence. This shows that the active and
participatory MI-BCI and FES upper limb rehabilitation system
can eﬀectively mobilize patients’ multi-sensors to participate in
rehabilitation treatment at the same time, and the rehabilitation
eﬀect is signiﬁcantly better than that of passive routine treatment.
As shown in Figure 2, some subjects (full rehabilitation
and signiﬁcant rehabilitation) showed obvious changes in the
distribution of brain topological power induced by rehabilitation
training. General Rehabilitation changed, but some patients did not
respond to rehabilitation. This also conﬁrmed our view that the MI-
BCI rehabilitation system can promote the rehabilitation of stroke
patients, however, not all patients have a therapeutic eﬀect. Due
to the special condition of the brain of stroke patients, we believe
that the patient’s attention concentration may aﬀect the use of BCI
devices, resulting in some patients being unable to use BCI in the
early stage of rehabilitation treatment. Poor motor function, speech
disorder, and spasm during rehabilitation may be adverse factors
aﬀecting the rehabilitation of upper-limb motor function in stroke
patients.
3.7. Discussion
This study used multisensory MI-BCI and FES feedback to
verify the neural plasticity of stroke patients (Wolpaw, 2007;
Biasiucci et al., 2018; Cervera et al., 2018). Exploring the related
brain electrical activity provides roadmaps for brain research
and clinical diagnosis. EEG studies have revealed secrets of
brain cognitive functions and neural disorders (Luo et al.,
2022).
Neuromotor
rehabilitation
promotes
neuroplasticity,
favoring functional recovery of the ipsilesional hemisphere
and activation of anatomically and functionally related brain
areas in both hemispheres to compensate for damaged tissue
(Tavazzi et al., 2022).
Based
on
brain-machine-
muscle-brain
closed-loop feedback, a closed-loop neural feedback path is
constructed between patients and rehabilitation equipment (Ang
et al., 2015). Many studies have shown that BCI combined with
EMG and exoskeletons can eﬀectively promote rehabilitation of
limb motor function. EEG studies have shown the importance of
physical activity in promoting learning, and the eﬀects of inactivity
or microgravity on cortical reorganization to cope with absent or
altered sensorimotor stimuli. Changes in power bands in diﬀerent
cortical areas occur with fatigue and in response to training stimuli,
FIGURE 2
Brain topographic of MI group and control group.
Frontiers in Human Neuroscience
07
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
leading to learning processes (Manganotti et al., 2022). Biasiucci
et al. (2018) built a BCI-FES upper-limb rehabilitation system
for stroke. According to the observation after 6–12 months of
follow-up, Biasiucci used the Fugl-Meyer clinical scale to verify
the eﬀectiveness of the BCI-FES rehabilitation system in restoring
motor function and stimulating nerve rehabilitation (Biasiucci
et al., 2018). For the analysis of EEG, previous studies have
shown that patients with stroke can elicit ERD/ERS during motor
imagining (Pfurtscheller and Aranibar, 1979; Neuper et al., 2006).
In this study, ERD and ERS were used to characterize the change
in feature level induced by rehabilitation training. For the patients
with eﬀective rehabilitation (34/40), the FMA, MAS, HMCAS,
and PSD scores in the MI group were signiﬁcantly higher than
those in the control group, which showed that the MI-BCI upper
limb rehabilitation system based on closed-loop feedback could
promote the recovery of the motor function of the aﬀected side
and induce changes in the brain nerves. The results validated that
after MI training, the activation degree of the motor cortex and
the connection level of the related cortical functional network in
patients with stroke were signiﬁcantly improved (Mueller-Putz
et al., 2014; Delorme et al., 2019; Wang et al., 2019). In this
study, active evoked stimulation of the brain, muscles, and nerves
was achieved through motor imagination and FES. For routine
rehabilitation training, patients’ limb movement rehabilitation is
mainly passive muscle movement and nerve stimulation, ignoring
the command role of the brain in the human body; therefore,
the recovery eﬃciency is far lower than that of active induction.
There was a problem with the length of the rehabilitation. The MI
group used two rehabilitation methods, leading to a longer period
of rehabilitation than the control group, which would aﬀect the
scoring. The experiment did not remove this inﬂuence; therefore,
this will be a matter of our follow-up research.
4. Conclusion
For upper limb motor function rehabilitation in stroke patients,
BCI combined with external devices may be more eﬀective
than conventional rehabilitation strategies, but there is a lack
of comprehensive evaluation of motor function rehabilitation in
patients. In this study, MI-BCI was combined with FES to perform
multisensory stimulus feedback, including visual, auditory, and
tactile stimuli, and an upper limb rehabilitation system based on
MI-BCI was established. We used the clinical scales FMA, MAS,
and NCCT to comprehensively evaluate the rehabilitation eﬀect
of MI-BCI. Clinical scale results showed that FMA, MAS, and
NCCT scores signiﬁcantly improved after Mi-BCI rehabilitation
treatment, and the scores of patients in the MI group were
signiﬁcantly higher than those in the control group. These results
indicate that MI-BCI rehabilitation training can eﬀectively improve
motor function in stroke patients, which is consistent with the
results of previous studies. In this study, we used an EEG-
based brain topographic map to comprehensively study the brain
activity of stroke patients after rehabilitation therapy with MI-
BCI. According to the analysis of the brain topographic map,
the brain ERD of patients with full rehabilitation and signiﬁcant
rehabilitation in the MI group was signiﬁcantly higher than that in
the control group, however, there was no signiﬁcant diﬀerence in
ERD between patients with general rehabilitation and no change in
the two groups, indicating that if patients actively participate in the
rehabilitation of MI-BCI, the feedback of myoelectric stimulation
induced by FES could eﬀectively promote nerve remodeling and
improve the eﬀect of rehabilitation. The total eﬀective rate of the MI
group was 95% (19/20), which was higher than that of the control
group (75%, 15/20). The results of this study prove that MI-BCI
rehabilitation therapy is both eﬀective and feasible. However, there
was one patient in the MI group whose condition did not change,
and three patients were excluded because the accuracy of EEG
collection was lower than the standard, which was probably caused
by adverse factors such as brain damage, poor motor function,
speech disorders, and spasms in stroke patients.
Data availability statement
The raw data supporting the conclusions of this article will be
made available by the authors, without undue reservation.
Ethics statement
The studies involving human participants were reviewed and
approved by the Biomedical Ethics Committee of Hebei University
of Technology. The patients/participants provided their written
informed consent to participate in this study.
Author contributions
WL and CL conceived the study. WL and JL collected the
data and wrote the manuscript. JL conducted the experiments. XZ
performed the EEG data processing. CL reviewed and edited the
manuscript. All authors have reviewed the manuscript, agreed to
its submission, read, and approved the ﬁnal manuscript.
Funding
This
research
was
funded
by
the
S&T
Program
of
Hebei (19277752D).
Conﬂict of interest
The authors declare that the research was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construed as a potential conﬂict of interest.
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsed by the publisher.
Frontiers in Human Neuroscience
08
frontiersin.org

Liao et al.
10.3389/fnhum.2023.1117670
References
Abiri, R., Borhani, S., Sellers, E., Yang, J., and Zhao, X. (2019). A comprehensive
review of EEG-based brain–computer interface paradigms. J. Neural Eng. 16:1. doi:
10.1088/1741-2552/aaf12e
Ajˇcevi´c, M, Furlanis, G, Miladinovi, A, Stella, A. B., Caruso, P, Ukmar, M,
et al. (2021a). Early EEG alterations correlate with CTP hypoperfused volumes and
neurological deﬁcit: A wireless EEG study in hyper-acute ischemic stroke. Ann.
Biomed. Eng. 49, 2150–2158. doi: 10.1007/s10439-021-02735-w
Ajˇcevi´c, M, Furlanis, G, Naccarato, M, Miladinovi, A, Stella, A. B., Caruso, P,
et al. (2021b). Hyper-acute EEG alterations predict functional and morphological
outcomes in thrombolysis-treated ischemic stroke: A wireless EEG study. Med. Biol.
Eng. Comput. 59, 121–129. doi: 10.1007/s11517-020-02280-z
Alexandra, R., Galina, I., and Boriset, P. (2021). Improving of the eﬀectiveness
of motor-imagery training with BCI technology in hand exoskeleton in post-stroke
rehabilitation. Int. J. Psychophysiol. 168, S124. doi: 10.1016/J.IJPSYCHO.2021.07.360
Ana, P. G., Carmen, M. T., and Miguel, G. M. (2021). The association between
mental motor imagery and real movement in stroke. Healthcare 9:11. doi: 10.3390/
HEALTHCARE9111568
Ang, K. K., Guan, C., Phua, K. S., Wang, C., Zhao, L., and Teo, W. P. (2015).
Facilitating eﬀects of transcranial direct current stimulation on motor imagery brain-
computer interface with robotic feedback for stroke rehabilitation. Arch. Phys. Med.
Rehabil. 96, S79–S87. doi: 10.1016/j.apmr.2014.08.008
Bai, Z, Fong, K. N. K., Zhang, J. J., Chan, J, and Ting, K. H. (2020). Immediate and
long-term eﬀects of BCI-based rehabilitation of the upper extremity after stroke: A
systematic review and meta-analysis. J. Neuro Eng. Rehabil. 17:57. doi: 10.1186/s12984-
020-00686-2
Barbero, M., Merletti, R., and Rainoldi, A. (2012). Atlas of muscle innervation
zones: Understanding surface electromyography and its applications. Mailand: Springer-
Verlag.
Biasiucci, A., Leeb, R., Iturrate, I., Perdikis, S., Ai-Khodairy, A., and Corbet, T.
(2018). Brain-actuated functional electrical stimulation elicits lasting arm motor
recovery after stroke. Nat. Commun. 9:2421. doi: 10.1038/s41467-018-04673-z
Cervera, M. A., Soekadar, S. R., Ushiba, J., Millán, J. D. R., Liu, M., and Birbaumer,
N. (2018). Brain-computer interfaces for post-stroke motor rehabilitation: A meta-
analysis. Ann. Clin. Transl. Neurol. 5, 651–663. doi: 10.1002/acn3.544
China National Health Commission (2021). Chinese guidelines for stroke prevention
and treatment, 2021 Edn. Beijing: China National Health Commission.
Delorme, M., Vergotte, G., Perrey, S., Froger, J., and Laﬀﬀont, I. (2019). Time course
of sensorimotor cortex reorganization during upper extremity task accompanying
motor recovery early after stroke: An fNIRS study. Restor. Neurol. Neurosci. 37,
207–218. doi: 10.3233/RNN-180877
Graimann, B., Huggins, J. E., Levine, S. P., and Pfurtscheller, G. (2002). Visualization
of signiﬁﬁcant ERD/ERS patterns in multichannel EEG and ECoG data. Clin.
Neurophysiol. 113, 43–47. doi: 10.1016/S1388-2457(01)00697-6
Jessica, C. N., Ruben, C. E., Paul, C. M., and David, E. V. (2018). Motor
imagery-based brain-computer interface coupled to a robotic hand orthosis aimed
for neurorehabilitation of stroke patients. J. Healthc. Eng. 2018:1624637. doi: 10.1155/
2018/1624637
Kamal, N., Alkareem, A. Z. A., and Hameed, A. K. (2021). EEG feature fusion
for motor imagery: A new robust framework towards stroke patients rehabilitation.
Comput. Biol. Med. 137:104799. doi: 10.1016/J.COMPBIOMED.2021.104799
Lee, Y., Nicholas, M., and Connor, L. (2021). Identifying emotional contributors to
participation post-stroke. Topics Stroke Rehabil. 30, 180–192. doi: 10.1080/10749357.
2021.2008597
Luo, C, Li, F, Li, P, Yi, C, Li, C, Tao, Q, et al. (2022). A survey of brain network analysis
by electroencephalographic signals. Cogn. Neurodyn. 16, 17–41. s11571-021-09689-8
doi: 10.1007/
Manganotti, P., Ajˇcevi´c, M., and Alex, B. S. (2022). EEG as a marker of brain
plasticity in clinical applications. Handb. Clin. Neurol. 184, 91–104. doi: 10.1016/B978-
0-12-819410-2.00029-1
Morioka, S., Osumi, M., Sakauchi, S., and Ishibashi, R. (2018). Relationship between
motor imagery ability and motor function of hemiplegic upper limbs and their use in
stroke patients. Ann. Phys. Rehabil. Med. 61:e178. doi: 10.1016/j.rehab.2018.05.407
Mueller-Putz, G. R., Daly, I., and Kaiser, V. (2014). Motor imagery-induced EEG
patterns in individuals with spinal cord injury and their impact on brain–computer
interface accuracy. J. Neural Eng. 11:035011. doi: 10.1088/1741-2560/11/3/035011
Muhammad, A. K., Rig, D., and Helle, K. I. (2020). Review on motor imagery
based BCI systems for upper limb post-stroke neurorehabilitation: From designing to
application. Comput. Biol. Med. 123:103843. doi: 10.1016/j.compbiomed.2020.103843
Neuper, C., Wrtz, M., and Pfurtscheller, G. (2006). ERD/ERS patterns reﬂecting
sensorimotor activation and deactivation. Prog. Brain Res. 159, 211–222. doi: 10.1016/
S0079-6123(06)59014-4
Pfurtscheller,
G.,
and
Aranibar,
A.
(1979).
Evaluation
of
event-related
desynchronization (ERD) preceding and following voluntary selfpaced movement.
Electroencephalogr. Clin. Neurophysiol. 46, 138–146. doi: 10.1016/0013-4694(79)
90063-4
Pfurtscheller,
G.,
and
Da
Silva,
F.
L.
(1999).
Event-related
EEG/MEG
synchronization
and
desynchronization:
Basic
principles.
Clin.
Neurophysiol.
110, 1842–1857. doi: 10.1016/S1388-2457(99)00141-8
Simon, P. F., Michael, W., Stephen, E. R., and Jonathan, B. C. (2007). Quantitative
EEG indices of sub-acute ischaemic stroke correlate with clinical outcomes. Clin.
Neurophysiol. 118, 2525–2532. doi: 10.1016/j.clinph.2007.07.021
Tavazzi, E., Bergsland, N., Pirastru, A., Cazzoli, M., Blasi, V., and Baglio, F. (2022).
MRI markers of functional connectivity and tissue microstructure in stroke-related
motor rehabilitation: A systematic review. Neuroimage 33:102931. 2021.102931 doi:
10.1016/j.nicl
Wang, Z., Zhou, Y., Chen, L., Gu, B., Yi, W., and Liu, S. (2019). BCI monitor
enhances electroencephalographic and cerebral hemodynamic activations during
motor training. IEEE Trans. Neural Syst. Rehabil. Eng. 27, 780–787. doi: 10.1109/
TNSRE.2019.2903685
Wolpaw, J. R. (2007). Brain-computer interfaces as new brain output pathways.
J. Physiol. 579, 613–619. doi: 10.1113/jphysiol.2006.125948
Zhan, G., Chen, S., Ji, Y., Xu, Y., Song, Z., Wang, J., et al. (2022). EEG-based brain
network analysis of chronic stroke patients after BCI rehabilitation training. Front.
Hum. Neurosci. 16:909610. doi: 10.3389/fnhum.2022.909610
Frontiers in Human Neuroscience
09
frontiersin.org
