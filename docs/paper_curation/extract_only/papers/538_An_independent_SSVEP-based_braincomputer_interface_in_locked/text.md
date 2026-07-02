Journal of Neural Engineering
J. Neural Eng. 11 (2014) 035002 (8pp)
doi:10.1088/1741-2560/11/3/035002
An independent SSVEP-based
brain–computer interface in locked-in
syndrome
D Lesenfants1, D Habbal1, Z Lugo1,3, M Lebeau1, P Horki2, E Amico1,
C Pokorny2, F G´omez1,4, A Soddu1,5, G M¨uller-Putz2, S Laureys1,6
and Q Noirhomme1,6
1 Coma Science Group, Cyclotron Research Centre and Neurology department, University of Li`ege,
Li`ege, Belgium
2 Laboratory of Brain-Computer Interfaces, Institute for Knowledge Discovery, Graz University of
Technology, Graz, Austria
3 Department of Psychology I, Institute for Psychology, University of W¨urzburg, W¨urzburg, Germany
4 Combios Laboratory, Computer Science Department, Universidad Central, Bogot´a, Colombia
5 Brain & Mind Institute, Physics & Astronomy Department, University of Western Ontario, London
ON, Canada
E-mail: Damien.Lesenfants@doct.ulg.ac.be
Received 9 January 2014, revised 18 March 2014
Accepted for publication 21 March 2014
Published 19 May 2014
Abstract
Objective. Steady-state visually evoked potential (SSVEP)-based brain–computer interfaces
(BCIs) allow healthy subjects to communicate. However, their dependence on gaze control
prevents their use with severely disabled patients. Gaze-independent SSVEP-BCIs have been
designed but have shown a drop in accuracy and have not been tested in brain-injured patients.
In the present paper, we propose a novel independent SSVEP-BCI based on covert attention
with an improved classiﬁcation rate. We study the inﬂuence of feature extraction algorithms
and the number of harmonics. Finally, we test online communication on healthy volunteers
and patients with locked-in syndrome (LIS). Approach. Twenty-four healthy subjects and six
LIS patients participated in this study. An independent covert two-class SSVEP paradigm was
used with a newly developed portable light emitting diode-based ‘interlaced squares’
stimulation pattern. Main results. Mean ofﬂine and online accuracies on healthy subjects were
respectively 85 ± 2% and 74 ± 13%, with eight out of twelve subjects succeeding to
communicate efﬁciently with 80 ± 9% accuracy. Two out of six LIS patients reached an ofﬂine
accuracy above the chance level, illustrating a response to a command. One out of four LIS
patients could communicate online. Signiﬁcance. We have demonstrated the feasibility of
online communication with a covert SSVEP paradigm that is truly independent of all
neuromuscular functions. The potential clinical use of the presented BCI system as a
diagnostic (i.e., detecting command-following) and communication tool for severely
brain-injured patients will need to be further explored.
Keywords: SSVEP-BCI, locked-in Syndrome, gaze-independent, feature extraction, harmonic
1. Introduction
Brain–computer interfaces (BCIs) [1] translate measures of
brain activity into messages or commands and provide a direct
6 Both authors contributed equally.
connection between the human brain and a computer. The
most favorable noninvasive brain imaging method employed
in BCI is electroencephalography (EEG), in which electrical
signals of high temporal resolution are recorded from the
scalp. The existing EEG-based BCI designs rely on a variety
of different EEG signal features, for example slow cortical
1741-2560/14/035002+08$33.00
1
© 2014 IOP Publishing Ltd
Printed in the UK

J. Neural Eng. 11 (2014) 035002
D Lesenfants et al
potentials [2], mu rhythms [3], P300 potentials [4] and steady-
state visually evoked potentials (SSVEPs) [5, 6]. In SSVEP-
based BCIs, one or more stimuli oscillating at different
constant frequencies are presented to the subject. When the
subject focuses his attention on the stimulus, EEG activity
is detected at the corresponding frequency over occipital
areas [7]. The SSVEP-based BCI has many advantages over
other EEG-based BCI systems, including (i) a high signal-to-
noise ratio , (ii) a high information transfer rate [8], (iii) less
susceptibility to eye movements and blink artifacts [9] as well
as to electromyographic artifacts [10], and (iv) they require
very little training since the SSVEP is an inherent response of
the brain.
BCIs have been proposed as a diagnostic tool for the
detection of consciousness and/or a communication tool for
severely brain-injured patients, and especially patients with
locked-in syndrome (LIS) [11, 12]. Following a brainstem
lesion, these patients often remain comatose for some days
or weeks, needing artiﬁcial respiration, and then gradually
wake up but remain paralyzed and voiceless. In acute LIS, the
difﬁculty to recognize unambiguous signs of consciousness,
the extreme motor disabilities, the apparent similarity with the
vegetative state/unresponsive wakefulness syndrome (i.e., eyes
opening and motor immobility without signs of awareness)
[13] and the ﬂuctuations of arousal levels [14] often result
in the diagnosis being delayed or even missed [15]. In the
chronic stage, computer-based communication could improve
a patient’s quality of life and increase interaction with their
environment.
Current BCIs relying on VEPs depend on gaze control
[16, 17] and thus fall into the category of dependent BCIs [1].
Therefore, these BCIs are not applicable to those whose severe
disabilities extend to impaired or nonexistent ocular motor
control, such as LIS patients in which (i) eye movements may
be inconsistent, very small and easily exhausted in the acute
stage and (ii) deteriorated or nonexistent oculomotor control
could be observed in the chronic stage. Independent SSVEP-
BCIs based on covert attention have been proposed [18–20]
but have shown a drop in robustness in healthy subjects and
have never been tested on patients.
The SSVEPs have the same fundamental frequency (ﬁrst
harmonic) as the stimulating frequency, but usually they also
include higher [21] and/or sub-harmonic frequencies [22].
Previous SSVEP-based BCIs were implemented on the basis
of the ﬁrst [7] or on the ﬁrst and second harmonic detection
[5, 6, 23]. Recent research studied the impact of harmonic
frequency components in the classiﬁcation accuracy and
showed that the use of higher harmonics positively inﬂuence
classiﬁcation in overt SSVEP [16]. The inﬂuence of harmonics
in covert SSVEP has never been studied.
The aim of the present work was to develop a novel covert
SSVEP-BCI with an improved classiﬁcation rate enabling
functional communication. To achieve this goal, we have: (i)
proposed a new portable covert stimulation pattern enabling a
better discrimination between two stimuli, (ii) tested different
feature extraction algorithms, (iii) studied the inﬂuence of the
number of harmonics (which has never been tested in covert
SSVEP), and (iv) developed and tested on 12 healthy subjects
an online covert SSVEP-BCI which allows synchronous
communication without ocular motor control. The potential
use of the system as an ofﬂine diagnostic tool and/or online
communication system for the disabled was then assessed in
six patients with LIS.
2. Materials and methods
2.1. Subjects
Twelve healthy subjects (ﬁve men; age range 22–43 years;
mean ± SD: 28.2 ± 5.7), hereinafter called group A,
participated in the ofﬂine study. Analysis on group A was
used to determine the best feature extraction algorithm and to
study the inﬂuence of parameters (i.e. the automatic channel
selection algorithm (ACSA), the number of harmonics and the
classiﬁers). Then, the parameters deﬁned from group A were
applied online to a second group, hereinafter called group
B, composed of 12 different healthy subjects (two men; age
range 21–30 years; 24.1 ± 3.0) and six LIS patients (four men;
age range 23–74 years; 49.0 ± 19.7; see table 3). None had
prior experience with BCI. The study was approved by the
ethical committee of the University Hospital of Li`ege and all
participants or their legal representatives provided informed
consent.
2.2. Data collection
EEG signals were recorded from 12 Ag/AgCl ring electrodes
at locations P3, P1, P2, P4, PO7, PO3, POz, PO4, PO8, O1,
Oz and O2, referenced to Pz, based on the international 10–20
electrode system. A ground electrode was placed behind the
right mastoid. All impedances were kept below 5 kÄ. Eye
movements were monitored with four electrodes: two on the
left and right temples; the remaining two over and under the
supra-orbital ridge respectively. The electroencephalograms
were recorded using a BrainVision V-Amp ampliﬁer with a
band pass ﬁlter set between 0.01 and 100 Hz and a sampling
frequency of 250 Hz.
2.3. Paradigms
2.3.1. Group A.
The visual stimulation was delivered via
a custom made stimulation unit, which can be decomposed
into a control unit and a stimulation panel, based on the
paradigm introduced in [24]. The panel, placed at 30 cm
from subject’s head, is a 7 × 7 cm2 ‘interlaced square’ made
of red and yellow 1 × 1 cm2 light emitting diode (LED)-
squares with a white ﬁxation cross in the middle (see ﬁgure 1).
The interlaced square pattern showed a 10% improvement
in accuracy in comparison with a ‘line’ pattern [19]. The
control unit is an electronic embedded system used for precise
control of red and yellow ﬂickering frequencies, which can be
varied independently between 1 and 99 Hz by a programmable
integrated circuit microcontroller. During the experiments, the
yellow and red squares were programmed to ﬂicker at 10 Hz
and 14 Hz respectively (duty cycle = 0.5). This stimulation
system has the advantages of being small, portable and easy
to use at the patient’s bedside. Each subject underwent a total
2

J. Neural Eng. 11 (2014) 035002
D Lesenfants et al
Figure 1. Electronic visual stimulation unit. The yellow squares
(represented by white squares here) ﬂicker at the frequency of 10 Hz.
The red squares (represented by gray squares here) ﬂash at 14 Hz.
Figure 2. Overt block pattern. The yellow square (represented by the
white square) ﬂashes at 10 Hz. The red square (represented by the
gray square) ﬂashes at 14 Hz.
of six runs, each lasting about 5 min. Each run contained ten
7 s trials [24], separated by 23 s periods (7 s of rest and 16 s of
auditory instructions delivered via headphones). During a run,
the interlaced squares pattern was continuously ﬂashing and
an equal number of both stimuli was presented in a random
order. The subject was instructed to ﬁx his/her gaze on the
white cross in the middle and to focus attention on one of
the ﬂashing colors. The inter-run rest periods were left at the
discretion of the subject and lasted between 2 to 10 min.
2.3.2. Group B.
Previous to the training session, three
healthy subjects and four LIS patients from group B performed
an overt session. The subjects were seated about 30 cm from
a block pattern (see ﬁgure 2), containing a yellow and a red
stimulus ﬂashing at f1 = 10 Hz and f2 = 14 Hz (duty cycle
= 0.5) respectively. This pattern was composed of two 2 × 2
cm2 blocks made of 1 × 1 cm2 LED squares separated by
12 cm with a white ﬁxation cross in between. Then, the
subjects had a training session identical to group A. After
a short break to train the classiﬁer, they performed an online
communication session. Thirty-three yes/no questions were
asked synchronously to the subject (e.g. ‘is your name Paul ?’,
‘are you 25 years old ?’). Answers needed to be unambiguous
and were known a priori. The subjects had to focus their
attention over 7 s on the yellow ﬂashes to answer ‘yes’ or on
the red for ‘no’. The stimulation panel was activated during
the question/response time only to avoid tiredness.
2.4. Data analysis
EEG signals were preprocessed with a Butterworth fourth-
order low-pass ﬁlter with a cutoff frequency of 60 Hz and
a Butterworth fourth-order high-pass ﬁlter with a cutoff
frequency of 5 Hz. An IIR notch ﬁlter (fc = 50 Hz, Q =
35) was also applied to the data. Epochs of 7 s were used as a
unique window.
For group A, frequency features were extracted from each
epoch with four state-of-the-art feature extraction algorithms
proposed in the literature: (1) discrete-time Fourier transform
(DFT), (2) multitapers spectral analysis (PMTM) [25, 26],
(3) canonical correlation analysis (CCA) [8] and (4) lock-
in analyzer system (LAS) [16, 17, 27]. The ﬁrst, second
and third harmonics of each stimulation frequency were
extracted. Several feature sets were tested with one, two or all
harmonics. An ACSA based on distinction sensitive learning
vector quantization (DSLVQ) [28] selected an optimal channel
set speciﬁc to each subject. Inside the classiﬁcation process,
this algorithm ﬁrst computed the relevance of the monopolar
input channels for all points in time during the course of a
trial. If the mean classiﬁcation accuracy inside the DSLVQ
system was greater than random [29], the time series of
relevance values were scaled and combined into one single
relevance value for each channel. If this mean accuracy was at
chance level, a subset of channels could not be extracted from
the complete set of channels. Finally, channels with the highest
relevance were automatically selected and features associated
to these channel subsets were extracted for classiﬁcation.
Classiﬁcation performances were computed with a linear
discriminant analysis (LDA) or a linear support vector machine
(SVM, linear kernel), and assessed with a 10 × 10 fold cross
validation. A SVM classiﬁer was used to study the inﬂuence
of the number of harmonics. Note that increasing the number
of features to process with a constant number of training
trials prevented the use of LDA with three harmonics. The
signiﬁcance of the change in classiﬁcation accuracy with the
different approaches was assessed with a paired permutation
test (results were considered signiﬁcant at p < 0.05) [30].
Optimal parameters deﬁned ofﬂine in group A were
applied online in group B. For group B, the classiﬁer was
trained on features extracted with PMTM on the ﬁrst harmonic
at channels selected by ACSA. A real-time auditory feedback
‘the response to your question is YES/NO’ was presented to
the subject after each question.
Mean power spectra from O2 during the 10 Hz 7 s trials
were extracted ofﬂine with multitaper spectral analysis to
illustrate typical SSVEP responses for healthy subjects and
LIS patients during overt and covert conditions (see ﬁgure 3).
All analyses were done with custom-made codes using Matlab
and Graz DSLVQ toolbox (Laboratory of Brain–Computer
Interfaces, Institute for Knowledge Discovery, Graz University
of Technology, Austria). BCI2000 software package [31] and
Fieldtrip Toolbox [32] were used for data acquisition and
presentation of the auditory instructions.
3

J. Neural Eng. 11 (2014) 035002
D Lesenfants et al
Figure 3. Mean power spectra, estimated with multitaper spectral analysis, recorded in a healthy subject (upper) and a patient with locked-in
syndrome (lower) from electrode O2 during an ‘overt’ run using a block pattern (left) and a ‘covert’ run using an ‘interlaced squares’ pattern
(right). Power spectrum obtained when the subject passively looked at the pattern (full line) and when the subject actively focussed attention
on the target stimulus (dotted line). Note the attentional modulation in the control subject and the LIS patient in the two conditions (block
and interlaced squares).
3. Results
Assessment of the electrooculogram did not show any eye
movement during the covert trials for both groups. A binomial
test [33] evaluated the chance level at 63% (α = 0.05, 60 trials).
An online correct response rate (CRR) of 70% was considered
the lowest rate of performance necessary to achieve efﬁcient
communication in a BCI with binary choice [37].
3.1. Overt versus covert conditions
Figure 3 (upper) shows typical overt and covert power spectra
for a healthy subject. When a subject overtly focused on a
stimulus, the power at the stimulation frequency and its second
harmonic were clearly increased (see ﬁgure 3, left). In the
‘covert’ condition (see ﬁgure 3, right), the power at the target’s
harmonic was smaller and could not be differentiated from
surrounding frequencies. A peak at the non-target frequency
could be observed with an amplitude close to the target
amplitude. The same frequency behavior could be observed
in patients with LIS (see ﬁgure 3, lower).
3.2. The inﬂuence of frequency feature extraction algorithm,
automatic channel selection algorithm, number of harmonics
and classiﬁers
The impact of the feature extraction algorithms was evaluated
in ten out of 12 subjects from group A. Subjects SC11A and
SC12A were rejected as all analyses showed classiﬁcation
accuracies at chance level (see tables 1 and 2). Signiﬁcant
differences were assessed with a two-tailed permutation test
(1000 permutations).
First, we compared the results obtained by the feature
extraction methods using all channels and a single harmonic.
PMTM obtained the maximum accuracy of 77.0 ± 3.4%
averaged among subjects, while LAS produced a not
signiﬁcantly different mean accuracy of 74.4 ± 3.2% (see
tables 1 and 2). DFT and CCA gave signiﬁcantly worse results
than PMTM and LAS with respectively 69.4 ± 3.4% and
58.4 ± 3.9%.
Second, we compared the results obtained by the feature
extraction methods using the ACSA and a single harmonic.
PMTM and LAS produced signiﬁcantly greater accuracy than
DFT and CCA, with an accuracy of 84.7 ± 2.0% and 83.1 ±
2.3% respectively. DFT obtained a 79.3± 2.7% accuracy. CCA
reached 72.4 ± 1.6% but in only ﬁve out of the ten subjects (the
electrodes subset could not be extracted in the ﬁve remaining
healthy subjects). The performance with and without ACSA
could therefore not be compared with CCA. Using the ACSA
signiﬁcantly increased the accuracy with PMTM, LAS and
DFT. For a single harmonic, we obtained a signiﬁcant mean
accuracy increase of 7.8% for PMTM, 7.9% for LAS and 7.6%
for DFT (see ﬁgure 4).
Studying the inﬂuence of the number of harmonics
(Nharm), LDA showed a decrease of accuracy when tested
on all electrodes, and a stable accuracy with ACSA (maximal
deviation of 2.4%). LDA without ACSA could not compute
the classiﬁcation accuracy with three harmonics. With an SVM
classiﬁer, adding the second and the third harmonics resulted
in no signiﬁcant difference (two-tailed permutation test, 1000
permutations) and classiﬁcation accuracies were similar to
those previously described with LDA. Then, we analyzed the
results obtained with the second and the third harmonics alone
(i.e. without including preceding harmonics). Results showed
4

J. Neural Eng. 11 (2014) 035002
D Lesenfants et al
Table 1. Mean and standard deviation of classiﬁcation accuracy (in percent) obtained with the Thomson multitaper method (PMTM) for
different numbers of harmonics with (ACSA) and without (AC) the use of automatic channel selection algorithm.
Nharm = 1
Nharm = 2
Nharm = 3
Subject
AC
ACSA
AC
ACSA
AC
ACSA
SC1A
78.4 ± 3.4
85.7 ± 1.8
73.9 ± 4.7
94.3 ± 1.8
/
94.4 ± 2.2
SC2A
92.3 ± 2.4
94.8 ± 1.0
76.5 ± 4.9
91.3 ± 1.6
/
92.6 ± 1.1
SC3A
78.4 ± 3.4
84.4 ± 2.1
73.9 ± 4.7
84.9 ± 2.6
/
80.6 ± 3.0
SC4A
67.8 ± 3.5
76.0 ± 2.3
51.7 ± 4.7
76.7 ± 3.7
/
78.6 ± 3.2
SC5A
62.4 ± 3.9
78.9 ± 2.3
51.6 ± 4.8
77.4 ± 2.4
/
70.5 ± 3.2
SC6A
71.6 ± 3.8
85.8 ± 2.6
62.6 ± 5.0
81.9 ± 3.3
/
85.6 ± 2.9
SC7A
89.5 ± 2.4
94.5 ± 1.4
76.0 ± 3.9
92.8 ± 2.4
/
92.6 ± 1.9
SC8A
82.7 ± 3.3
89.2 ± 2.3
77.3 ± 4.3
94.4 ± 1.9
/
87.2 ± 1.7
SC9A
91.1 ± 2.3
94.6 ± 1.6
84.0 ± 4.3
91.7 ± 1.1
/
91.8 ± 1.3
SC10A
56.6 ± 4.4
63.5 ± 1.8
58.3 ± 4.7
67.5 ± 3.0
/
68.4 ± 2.4
SC11A
57.0 ± 3.8
/
43.1 ± 5.0
/
/
/
SC12A
44.5 ± 3.8
/
43.2 ± 5.8
/
/
/
Total
77.0 ± 3.4
84.7 ± 2.0
68.6 ± 4.6
85.3 ± 2.5
/
84.2 ± 2.4
Table 2. Mean and standard deviation of classiﬁcation accuracy (in per cent) obtained with the lock-in analyzer system (LAS) for different
numbers of harmonics with (ACSA) and without (AC) the use of automatic channel selection algorithm.
Nharm = 1
Nharm = 2
Nharm = 3
Subject
AC
ACSA
AC
ACSA
AC
ACSA
SC1A
76.7 ± 3.1
85.0 ± 1.9
73.2 ± 4.9
93.9 ± 1.8
/
94.7 ± 1.2
SC2A
86.5 ± 2.1
93.5 ± 0.8
74.8 ± 5.2
95.4 ± 0.9
/
95.0 ± 1.7
SC3A
76.7 ± 3.1
82.5 ± 2.7
73.2 ± 4.9
79.4 ± 2.7
/
74.6 ± 2.6
SC4A
61.0 ± 4.2
73.6 ± 3.5
58.3 ± 4.5
73.6 ± 2.2
/
77.6 ± 1.9
SC5A
69.7 ± 2.9
80.2 ± 2.4
54.2 ± 4.6
76.1 ± 2.8
/
72.8 ± 1.9
SC6A
61.4 ± 3.6
76.2 ± 2.0
60.8 ± 4.7
79.0 ± 2.2
/
77.7 ± 3.3
SC7A
85.2 ± 2.8
90.0 ± 2.2
76.5 ± 4.7
91.2 ± 2.4
/
94.0 ± 2.4
SC8A
83.0 ± 2.9
87.4 ± 2.2
75.9 ± 4.4
94.3 ± 2.2
/
91.5 ± 2.6
SC9A
90.5 ± 2.4
92.9 ± 1.7
75.9 ± 4.2
90.9 ± 2.1
/
91.5 ± 1.8
SC10A
53.7 ± 3.8
70.1 ± 2.4
61.7 ± 4.7
70.9 ± 3.0
/
71.4 ± 2.9
SC11A
57.8 ± 4.3
/
48.5 ± 5.1
/
/
/
SC12A
49.7 ± 4.3
/
54.0 ± 5.0
/
/
/
Total
74.4 ± 3.2
83.1 ± 2.8
68.4 ± 4.7
84.5 ± 2.3
/
84.1 ± 2.3
Table 3. Demographic and clinical data of patients with locked-in syndrome.
Gender
Age
Etiology
Interval (years)
MRI
Communication code
LIS1
M
23
Traumatic
Right cerebellar, right frontal and left
Yes (looks right) and no
brainstem
lenticular lesions. Diffuse axonal injury in
no (eyes closure)
lesion
frontal and parietal lobes and the lenticular
communication.
capsula. Global cerebral atrophy with
quadriventriculaire hydrocephalus.
LIS2
F
56
Brainstem
15
Ponto-mesencephalic, middle cerebellar and
Yes-no head movements
stroke
occipital lesions.
communication
(nystagmus).
LIS3
M
64
Brainstem
12
Pontine/diffuse peri-ventricular lesions.
Yes-no head
stroke
movements
communication.
LIS4
F
30
Stroke
9
Cerebellar and brainstem lesions.
Yes (eyes closure) and
no (looks up) communication
(nystagmus).
LIS5
M
47
Brainstem
3
Cerebellar and ponto-mesencephalic lesions.
Verbalization via
stroke
tracheostomy.
LIS6
M
74
Brainstem
3
Ponto-mesencephalic and occipital lesions.
Yes (head movement) and
stroke
no (eyes closure)
communication.
5

J. Neural Eng. 11 (2014) 035002
D Lesenfants et al
Figure 4. Recognition accuracies on 10 healthy subjects for
different feature extraction algorithms and all channels (AC, white)
or automatic channel selection algorithm (ACSA, gray).
a global decrease in accuracies when using the second (10%
for H1 to H2) or third harmonic (5% for H2 to H3) alone, in
comparison with the ﬁrst harmonic, and this with and without
ACSA.
3.3. Online communication
Optimal parameters deﬁned ofﬂine in group A were applied
online to group B. For real-time communication, a PMTM
feature extraction algorithm was used to retrieve the amplitude
of the ﬁrst harmonic at channels selected on the training set
by ACSA. The mean ofﬂine training accuracy on all subjects
of group B was 77.7 ± 2.4%. Results showed online accuracy
greater than chance level for eight out of 12 healthy volunteers
of group B (see ﬁgure 5). The mean online accuracy on all
subjects of group B was 74.0 ± 12.5%. Considering only the
eight subjects with an online accuracy higher than 70%, the
mean online accuracy was 80.3 ± 8.6%. In particular, control
SC5B could answer correctly 32 questions out of 33. The
patients LIS5 and LIS6 preferred to stop the assessment after
the training session due to fatigue. Ofﬂine accuracy of these
patients were 70.5 ± 3.9% and 58.0 ± 5.5% respectively.
Patient LIS3 answered successfully 70% of the questions.
Patient LIS2 reached 64%. Two patients (LIS1 and LIS4)
achieved accuracy below chance level with a score of 52%
(see ﬁgure 5).
4. Discussion
Eight out of the twelve healthy subjects succeeded in reaching
a communication accuracy higher than the 70% CRR required
for an efﬁcient communication. In particular, one healthy
subject achieved 32 out of 33 correct responses. Mean online
accuracy on healthy subjects able to communicate was 80.3 ±
8.6%. Ofﬂine analysis showed that healthy subjects succeeded
in reaching an average accuracy of 85% (with three subjects
out of ten reaching more than 94%), which exceeds accuracies
of previous covert SSVEP-based BCIs [18–20]. Moreover,
the proposed ‘interlaced squares’ stimulation pattern is small,
portable, easy to use and adapted for bedside use with patients,
features which are not shared by other covert stimulation
devices requiring a cathode ray tube screen. Four out of the
twenty-nine subjects involved in previous [24] and present
studies showed performance at chance level. This illustrates
that covert SSVEP-BCI systems may not be used by all
subjects, as previously reported [34]. In group A, LAS
and PMTM feature extraction algorithms obtained higher
accuracies than classical Fourier transform, in accordance with
previous observations [17]. CCA did not work when used
in conjunction with ACSA. The achievement of this feature
extraction algorithm depended on the input (all the channels
together versus each channel separately), which could explain
the decreased performance. We here suggest the use of an
ACSA based on DSLVQ which leads to an 8% increase of
accuracy.
While the use of higher harmonics has been shown
to positively inﬂuence classiﬁcation in overt SSVEP [16],
adding the second and/or third harmonic did not improve the
classiﬁcation accuracy in our covert SSVEP paradigm. For
healthy subjects and patients with LIS, the study of overt and
covert power spectra illustrated the difference between the two
conditions and the difﬁculties associated with covert SSVEP.
We observed a decrease of the power at the target stimulation
frequency, at the target’s harmonic (at the level of intrinsic
activity) and the presence of a peak at the non-target frequency
with an amplitude close to the target amplitude (see ﬁgure 3).
Therefore, adding harmonics did not add extra information.
In patients with LIS, two out of six obtained accuracies
above chance level in the training session and one out of four
was able to functionally communicate online. This low success
rate can be partly explained by the clinical conditions of these
patients: two patients stopped the test due to fatigue ; two
other patients had a persistent nystagmus preventing effective
perception of the stimuli. Concerning the ergonomics of the
system, the patients LIS1, LIS2, LIS3 and LIS5 expressed
that the system was easy to use and did not report visual or
attentional problems (patients LIS4 and LIS6 expressed that
the training part was too long). Future studies are needed to
further assess the clinical pertinence of a fully independent
system based on covert SSVEP in the LIS population. Our
system should also be tested in a broader population of
patients, including total LIS patients. The learning effect
on communication performances, mental workload and user
satisfaction should also be part of future researches. The
accuracies obtained in patients are lower than those presented
by (1) Parini et al [35] on patients with Duchenne muscular
dystrophy using a four-class overt SSVEP-BCI and (2)
Combaz et al [36] using an overt SSVEP speller in patients
with incomplete LIS. K¨ubler and Birbaumer tested a visual
P300 speller with patients [37]. Two out of ﬁve LIS patients
were able to communicate with the system. However, all
these systems were gaze-dependent, hence excluding patients
without gaze control. This represents an important limitation
for patients in which (1) a loss of gaze control is often observed
in the chronic setting [38] and (2) eye movements in the acute
setting may be inconsistent, very small and easily exhausted
[15]. P300-based BCI have been studied to enable motor-
independence. K¨ubler et al tested an auditory P300-speller
in three patients with LIS [39]. While nine of the fourteen
healthy subjects achieved spelling accuracy above 70%, the
patient’sperformancewaspoor. Anauditoryfour-choiceP300-
speller BCI was proposed by Lul´e et al and was tested in two
6

J. Neural Eng. 11 (2014) 035002
D Lesenfants et al
Figure 5. Recognition accuracy for healthy subjects (group B) and LIS patients. Dark gray represents online accuracy and light gray the,
training accuracy. The horizontal full line represents the chance level for the training set.
patients with LIS [40]. One of the two patients showed an
ofﬂine accuracy higher than chance level but neither of them
showed an online performance higher than 70%. K¨ubler and
Birbaumer [37] also used slow cortical potential (SCP) and
sensorimotor rhythms (SMR) as independent modalities. After
a training period of a few months to years, three out of four
classical LIS patients reached the 70% criterion level with
SCP-BCI while none of the six complete LIS patients could
communicate. Only one classical LIS and one complete LIS
patient tried the SMR-BCI; the ﬁrst reached a 77% accuracy
and the second remained at chance level. Limitations of these
BCIs are the long user training required and the long sustained
attention times needed for answering the questions. With a
few seconds of focussed attention (7 s in our system) and none
or little user training required, SSVEP-BCI could be a more
adapted solution for clinical use than SMR and SCP-BCIs.
It is important to stress that SSVEP-based BCIs could
evoke seizures. To avoid this potential risk, we here monitored
EEG signals during each assessment in real-time. An EEG
expert was present during all sessions to detect abnormal
paroxystic electrical activity. We recorded no seizures in the
present study. Using higher stimulation frequencies (i.e. 30–
60 Hz) are less epileptogenic but reduce SSVEP amplitudes
[41].
5. Conclusion
We here demonstrated the feasibility of online communication
with a covert SSVEP paradigm that is truly independent
of neuromuscular function and gaze control [1]. We could
functionally communicate with eight out of twelve healthy
subjects. One out of four LIS patients could answer questions
with the SSVEP-BCI system. The short sustained attention
time (7 s), the concise training period and the robustness
of our method could also make it a diagnostic tool
for detecting command-following in severely brain-injured
patients. Future studies should focus on improving patient
accuracy and implementing an automated user-friendly online
and asynchronous version of these novel BCI technologies.
Acknowledgments
The authors would like to thank all the patients for their
collaboration. Steven Laureys is Research Director at the
Fonds de la Recherche Scientiﬁque (FRS). This work was
supported by FEDER fund RADIOMED 930549, James
McDonnell Foundation and French Speaking Community
Concerted Research Action. The text reﬂects solely the views
of its authors. The funders are not liable for any use that may
be made of the information contained therein.
References
[1] Wolpaw J R, Birbaumer N, McFarland D J, Pfurtscheller G
and Vaughan T M 2002 Brain-computer interfaces for
communication and control Clin. Neurophysiol. 113 767–91
[2] Birbaumer N, K¨ubler A, Ghanayim N, Hinterberger T,
Perelmouter J, Kaiser J, Iversen I, Kotchoubey B,
Neumann N and Flor H 2000 The thought translation device
(ttd) for completely paralyzed patients IEEE Trans. Neural
Syst. Rehabil. Eng. 8 190–3
[3] Wolpaw J R, McFarland D J, Neat G W and Forneris C A
1991 An EEG-based brain-computer interface for cursor
control Electroencephalogr. Clin. Neurophysiol. 78 252–9
[4] Farwell L A and Donchin E 1988 Talking off the top of your
head: Toward a mental prosthesis utilizing event-related
brain potentials Electroencephalogr. Clin. Neurophysiol.
70 510–23
[5] Cheng M, Gao X, Gao S and Xu D 2002 Design and
implementation of a brain-computer interface with high
transfer rates IEEE Trans. Biomed. Eng. 49 1181–6
7

J. Neural Eng. 11 (2014) 035002
D Lesenfants et al
[6] Lalor E, Kelly S P, Finucane C, Burke R, Reilly R B
and McDarby G 2004 Brain-computer interface based on
the steady-state VEP for immersive gaming control Biomed.
Tech. 49 63–64
[7] Middendorf M, McMillan G, Calhoun G and Jones K S 2000
Brain-computer interfaces based on the steady-state
visual-evoked response IEEE Trans. Rehabil. Eng. 8 211–4
[8] Bin G, Gao X, Yan Z, Hong B and Gao S 2009 An online
multi-channel ssvep-based brain-computer interface using a
canonical correlation analysis method J. Neural Eng.
6 46002–8
[9] Perlstein W M, Cole M A, Larson M, Kelly K, Seignourel P
and Keil A 2003 Steady-state visual evoked potentials
reveal frontally-mediated working memory activity in
humans Neurosci. Lett. 342 191–5
[10] Gray M, Kemp A H, Silberstein R B and Nathan P J 2003
Cortical neurophysiology of anticipatory anxiety: an
investigation utilizing steady state probe topography (sspt)
Neuroimage 20 975–86
[11] American Congress of Rehabilitation Medicine 1995
Recommendations for use of uniform nomenclature
pertinent to patients with severe alterations of
consciousness Arch. Phys. Med. Rehabil. 76 205–9
[12] Chatelle C, Chennu S, Noirhomme Q, Cruse D, Owen A
and Laureys S 2012 Brain-computer interfacing in disorders
of consciousness Brain Inj. 26 1510–22
[13] The Multi-Society Task Force on PVS 1994 Medical aspects
of the persistent vegetative state New Engl. J. Med.
330 1499–508
[14] Majerus S, Gill-Thwaites H, Andrews K and Laureys S 2005
Behavioral evaluation of consciousness in severe brain
damage Prog. Brain Res. 150 397–413
[15] Laureys S et al 2005 The locked-in syndrome: What is it like
to be conscious but paralyzed and voiceless? Prog. Brain
Res. 150 495–511
[16] M¨uller-Putz G R, Scherer R, Brauneis C and Pfurtscheller G
2005 Steady-state visual evoked potential (ssvep)-based
communication : impact of harmonic frequency
components J. Neural Eng. 2 123–30
[17] M¨uller-Putz G R, Eder E, Wriessnegger S C
and Pfurtscheller G 2008 Comparison of dft and lock-in
ampliﬁer features and search for optimal electrode positions
in ssvep-based bci J. Neurosci. Methods 168 174–81
[18] Kelly S P, Lalor E C, Reilly B and Foxe J J 2005 Visual spatial
attention tracking using high-density ssvep data for
independent brain–computer communication IEEE Trans.
Neural Syst. Rehabil. Eng. 13 172–8
[19] Allison B Z, McFarland D J, Schalk G, Zheng S D,
Jackson M M and Wolpaw J R 2008 Towards an
independent brain–computer interface using steady state
visual evoked potentials Clin. Neurophysiol. 119 399–408
[20] Zhang D, Maye A, Gao X, Hong B, Engel A K and Gao S
2010 An independent brain-computer interface using covert
non-spatial visual selective attention J. Neural Eng.
7 16010–21
[21] Regan D 1989 Human Brain Electrophysiology: Evoked
Potentials and Evoked Magnetic Fields in Science and
Medicine (New York: Elsevier)
[22] Herrmann C S 2001 Eeg responses to 1–100 hz ﬂicker:
resonance phenomena in visual cortex and their potential
correlation to cognitive phenomena Exp. Brain Res.
137 346–53
[23] Gao X, Xu D, Cheng M and Gao S 2003 A bci-based
environmental controller for the motiondisabled IEEE
Trans. Neural Syst. Rehabil. Eng. 11 137–40
[24] Lesenfants D, Partoune N, Soddu A, Lehembre R,
M¨uller-Putz G R, Laureys S and Noirhomme Q 2011
Design of a covert ssvep-based BCI Proc. 5th Int.
Brain-Computer Interface Conf. (Graz, Austria) pp 216–219
[25] Thomson D J 1982 Spectrum estimation and harmonic
analysis Proc. IEEE 70 1055–96
[26] Hoogenboom N, Schoffelen J M, Oostenveld R, Parkes L M
and Fries P 2006 Localizing human visual gamma-band
activity in frequency, time and space Neuroimage
29 764–73
[27] M¨uller-Putz G R, Scherer R, Neuper C and Pfurtscheller G
2006 Steady-state somatosensory evoked potentials:
Suitable brain signals for brain–computer interfaces? IEEE
Trans. Neural Syst. Rehabil. Eng. 14 30–7
[28] Pregenzer M, Pfurtscheller G and Flotzinger D 1996
Automated feature selection with a distinction
sensitive learning vector quantizer Neurocomputing
11 19–29
[29] Pregenzer M 1998 Dslvq—Distinct Sensitive Learning Vector
Quantization (Aachen: Shaker Verlag)
[30] Nichols T E and Holmes A P 2002 Nonparametric
permutation tests for functional neuroimaging: a primer
with examples Hum. Brain Mapp. 15 1–25
[31] Schalk G, McFarland D J, Hinterberger T, Birbaumer N
and Wolpaw J R 2004 Bci2000: a general-purpose
brain–computer interface (bci) system IEEE Trans. Biomed.
Eng. 51 1034–43
[32] Oostenveld R, Fries P, Maris E and Schoffelen J-M 2011
Fieldtrip: Open source software for advanced analysis of
MEG, EEG, and invasive electrophysiological data Comput.
Intell. Neurosci. 2011 156869
[33] M¨uller-Putz G R, Scherer R, Brunner C, Leeb R
and Pfurtscheller G 2008 Better than random? a closer look
on bci results Int. J. Bioelectromagnetism 10 52–55
[34] Chen Y, Seth A K, Gally J A and Edelman G M 2003 The
power of human brain magnetoencephalographic signals
can be modulated up or down by changes in an attentive
visual task Proc. Natl Acad. Sci. 6 3501–6
[35] Parini S, Maggi L, Turconi A C and Andreoni G 2009 A
robust and self-paced BCI system based on a four class
ssvep paradigm: algorithms and protocols for a
high-transfer-rate direct brain communication Comput.
Intell. Neurosci. 2009 864564
[36] Combaz A, Chatelle C, Robben A, Vanhoof G, Goeleven A,
Thijs V, Van Hulle M and Laureys S 2009 A comparison of
two spelling brain-computer interfaces based on visual p3
and ssvep in locked-in syndrome Plos One 8 e73691
[37] K¨uebler A and Birbaumer N 2008 Brain-computer interfaces
and communication in paralysis: extinction of goal directed
thinking in completely paralysed patients? Clin.
Neurophysiol. 119 2658–66
[38] Alexandre M F, Challe G, Pradat-Dieh P and Le Hoang P
2012 Locked-in syndrome et vision : `a propos de 13 cas
Rev. Neurologique 168 A76
[39] K¨ubler A, Furdea A, Halder S, Hammer E M, Nijboer F
and Kotchoubey B 2009 A brain–computer interface
controlled auditory event-related potential (p300) spelling
system for locked-in patients Ann. NY Acad. Sci.
1157 90–100
[40] Lul´e D et al 2013 Probing command following in patients with
disorders of consciousness using a brain-computer interface
Clin. Neurophysiol. 124 101–6
[41] Bakardjian H, Tanaka T and Cichockia A 2010 Optimization
of ssvep brain responses with application to eight-command
brain–computer interface Neurosci. Lett. 469 34–8
8
