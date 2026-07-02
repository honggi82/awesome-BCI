eprints@whiterose.ac.uk
https://eprints.whiterose.ac.uk
Universities of Leeds, Sheffield and York
Deposited via The University of Leeds.
White Rose Research Online URL for this paper:
https://eprints.whiterose.ac.uk/id/eprint/164887/
Version: Accepted Version
Article:
Zhang, Y, Xie, SQ, Wang, H et al. (2021) Data Analytics in Steady-State Visual Evoked 
Potential-based Brain-Computer Interface: A Review. IEEE Sensors Journal, 21 (2). pp. 
1124-1138. ISSN: 1530-437X 
https://doi.org/10.1109/JSEN.2020.3017491
© 2020 IEEE. Personal use of this material is permitted. Permission from IEEE must be 
obtained for all other uses, in any current or future media, including reprinting/republishing 
this material for advertising or promotional purposes, creating new collective works, for 
resale or redistribution to servers or lists, or reuse of any copyrighted component of this 
work in other works. Uploaded in accordance with the publisher's self-archiving policy.
Reuse 
Items deposited in White Rose Research Online are protected by copyright, with all rights reserved unless 
indicated otherwise. They may be downloaded and/or printed for private study, or other acts as permitted by 
national copyright laws. The publisher or other rights holders may allow further reproduction and re-use of 
the full text version. This is indicated by the licence information on the White Rose Research Online record 
for the item. 
Takedown 
If you consider content in White Rose Research Online to be in breach of UK law, please notify us by 
emailing eprints@whiterose.ac.uk including the URL of the record and the reason for the withdrawal request. 

1
Data Analytics in Steady-State Visual Evoked
Potential-based Brain-Computer Interface: A Review
Yue Zhang, Shane Xie, Senior Member, IEEE, He Wang, Member, IEEE, Zhiqiang Zhang, Member, IEEE
Abstract—Electroencephalograph (EEG) has been widely ap-
plied for brain-computer interface (BCI) which enables paralyzed
people to directly communicate with and control of external
devices, due to its portability, high temporal resolution, ease of
use and low cost. Of various EEG paradigms, steady-state visual
evoked potential (SSVEP)-based BCI system which uses multiple
visual stimuli (such as LEDs or boxes on a computer screen)
ﬂickering at different frequencies has been widely explored in the
past decades due to its fast communication rate and high signal-
to-noise ratio. In this paper, we review the current research in
SSVEP-based BCI, focusing on the data analytics that enables
continuous, accurate detection of SSVEPs and thus high infor-
mation transfer rate. The main technical challenges, including
signal pre-processing, spectrum analysis, signal decomposition,
spatial ﬁltering in particular canonical correlation analysis and
its variations, and classiﬁcation techniques are described in this
paper. Research challenges and opportunities in spontaneous
brain activities, mental fatigue, transfer learning as well as hybrid
BCI are also discussed.
Index Terms—Brain-computer interface (BCI), steady state
visual evoked potential (SSVEP), healthcare application, data
analytics, canonical correlation analysis.
I. INTRODUCTION
Brain-computer interface (BCI) is a communication system
that enables paralyzed people to directly communicate with
and control of external devices without body movement via
analysing the user’s brain activities [1], [2], and it has been
widely explored in the past years, as illustrated by the fast
increment of the numbers of BCI related publications in the
Fig. 1. There are a wide variety of applications of BCI systems,
ranging from wheelchairs, robot and prosthetic arms control
to character spelling, games and entertainment [3]–[5].
BCI systems normally rely on different modalities of
functional neuro-imaging, such as electroencephalography
(EEG) [7], functional near-infrared spectroscopy (fNIRS) [8],
functional magnetic resonance imaging (fMRI) [9], and mag-
netoencephalography (MEG) [10]. Among the various modal-
ities, EEG is the most commonly employed one due to its
portability, high temporal resolution, ease of use and low cost
This work was supported in part by Engineering and Physical Sciences
Research Council (EPSRC) (Grant No. EP/S019219/1) and in part by China
Scholarship Council (CSC) (Grant No. 201906460007). (Corresponding au-
thor: Yue Zhang)
Yue Zhang and Zhiqiang Zhang are with Institute of Robotics, Au-
tonomous System and Sensing, School of Electrical and Electronic Engi-
neering, University of Leeds, LS2 9JT, UK. (e-mail: elyzh@leeds.ac.uk;
Z.Zhang3@leeds.ac.uk). Shane Xie is with the School of Electronic and Elec-
trical Engineering, University of Leeds, Leeds LS2 9JT, UK, and collaborates
with the Institute of Rehabilitation Engineering, Binzhou Medical University,
Yantai, China (email: S.Q.Xie@leeds.ac.uk). He Wang is with School of Com-
puting, University of Leeds, LS2 9JT, UK. (email:H.E.Wang@leeds.ac.uk).
Figure 1.
Cumulative number of publications referring to BCI indexed by
IEEE Xplore, Web of Science, PubMed and Scopus, and it is obvious the
research on BCI is increasing year by year.
Figure 2.
Distribution of published papers in subareas of EEG-based BCI
systems.
[11]–[14], as shown in the Table. I. Four typical paradigms in
the EEG signal, namely P300 event related potential (ERP),
slow cortical potential (SCP), sensorimotor rhythms (SMR),
and steady-state visual evoked potential (SSVEP) are used
to analyse brain activities [15], and Fig. 2 outlines a rapid
surge of interest in EEG-based BCI in recent years in terms of
the number of publications using different type of paradigms.

2
Table I
THE COMPARISON OF EEG AND THE OTHER NEURO IMAGING TECHNIQUES
Neuro imaging techniques
EEG
fNIRS
fMRI
MEG
SSVEP
P300 ERP
SMR
SCP
ITR (bits/min)
24.7∼325.33
4.47∼20.1
4.47∼17
N.A
3.18∼8.23
∼5
13.1∼19.6
SNR(dB)
8.97∼25
0.87∼8.18
-16∼5
17.5∼42.8
26.48∼31.93
1.07∼161.2
2∼35
Temporal resolution
millisecond
millisecond
second
millisecond
Spatial resolution
centimeter
millimeter
millimeter
millimeter
Cost
low
moderate
high
very high
(a) Scheme of the experimental paradigm.
(b) Stimulus design of the 40-target BCI system.
Figure 3. The redraw of the experimental paradigm and stimulus design in
[6], which represented the setting for one of the highest numbers of stimuli.
It is obvious that SSVEP-based BCI has received extensive
research interests in the past decades due to its fast commu-
nication rate and high signal-to-noise ratio (SNR).
The SSVEP-based BCI usually utilizes several visual os-
cillating stimuli, such as LEDs or boxes on a computer
screen, which are generally modulated at different frequencies
and phases [16], [17]. A typical experimental paradigm of a
SSVEP-based BCI system generally contains M blocks each
containing N trials corresponding to N visual stimuli which
ﬂicker at a random order. For example, Fig. 3(a) shows a
typical stimulated experiment in [6], which represented the
setting for one of the highest numbers of stimuli. The user
interface is a 5 × 8 matrix of visual stimuli including 40 targets
which were modulated by linearly increasing frequencies and
phases, as shown in Fig. 3(b). In each experimental block,
subjects were required to gaze at each visual stimulus for
0.5 s, and completed 40 trials corresponding to all 40 targets.
Each trial began with a 0.5 s visual cue that shows the target
stimulus produced by the stimulus program. During the target
cue period, users were required to shift their attention to the
ﬂickering target on the screen as quickly as possible. The
subjects rested for a few minutes between two consecutive
blocks to relieve visual and mental fatigue. Besides, to de-
crease artifacts generated by eye movements, subjects should
avoid eye blinks during the experimental period. SSVEPs are
periodic neural responses generated in occipital scalp areas
of the brain, and the stimulus frequency will determine the
response frequency content, which contains activities not only
at the stimulus frequency but also at its higher harmonics [18].
Signal processing algorithms are applied to analyze the charac-
teristics of SSVEP responses and identify the subject’s intent
to control the peripheral equipment. As a result, subjects can
output desired commands by gazing at different target stimuli
sequentially [16].
Recent surveys of the BCI system used in computer in-
terface spellers [19] [20], and hybrid BCI [21] [22] have
signiﬁed the importance of SSVEP-based technologies. These
surveys focus mainly on the various applications of SSVEP
rather than its technical novelty and challenges. In other
surveys, Zhu et al. [23] reported the different repetitive visual
stimulus choices in terms of rendering devices, properties
(e.g., frequency, color), and their potential effects on BCI
performance, user comfort and safety. Zerafa et al. [24]
compared the different training requirements of feature extrac-
tion methods for SSVEP-based BCIs. They divided SSVEP
feature extraction methods into three categories according to
training requirements, namely training-free, subject-speciﬁc
and subject-independent training approaches. Different to pre-
vious surveys, this review focuses on technical challenges
and developments in SSVEP data analytics including signal
pre-processing, spectrum analysis, signal decomposition, spa-
tial ﬁltering in particular canonical correlation analysis and
its variations, and classiﬁcation techniques. Three databases,
Google Scholar, IEEE Xplore and Web of Science, were used
for the literature search. A combination of keywords, such
as BCI, SSVEP, classiﬁcation, spatial ﬁltering and canonical
correlation analysis, were used as search terms. Publications
from 2010-2020 were preferred, but this range was extended
in some cases.
The remainder of this paper is organized as follows. Section
II brieﬂy introduces the typical healthcare applications of
SSVEP-based BCI system. Data analytics and signal pro-
cessing algorithms for SSVEP identiﬁcation are detailed in
Section III. Section IV presents some new emerging challenges
and opportunities of SSVEP. Discussion and conclusion are
provided in Section V and VI.

3
II. HEALTHCARE APPLICATIONS
In this section, we will use healthcare as the exemplar
to illustrate SSVEP-based BCI systems’ wide spectrum of
applications. Clinically, SSVEP-based BCI systems have been
applied for diagnosis of various diseases and health issues,
such as migraine [25], autism [26], cognitive aging [27],
as well as the abnormal nervous system in patients with
bipolar disorder [28] and schizophrenia [29], via comparing
differences between the patients and healthy people on certain
physiological indexes such as brain complexity described by
inherent fuzzy entropy and the amplitude/power of SSVEP
responses, when they look at certain visual stimuli. In addition
to the diagnostic applications, the SSVEP-based BCI systems
also show great potential in providing commands to control
rehabilitation or assistive devices for people with disability.
For patients with impaired mobility, restoring their lost abil-
ities, or at least helping them adapt to suffered disabilities,
is essential for them to live with dignity. The SSVEP-based
BCI system can output the patient’s desired commands and
control the external devices, which can thus restore/rebuild
the function of damaged muscles to efﬁciently accelerate the
rehabilitation procedure. For instance, the operation process
for rehabilitation is that BCI system analyses the SSVEP
responses generated from the scalp when the user looks at
different visual stimuli. Then, intentions are translated into
various commands to trigger the peripheral devices, e.g. upper
extremity rehabilitation [30], ankle rehabilitation robot [31],
which can stimulate impaired muscles to perform more precise
motion tasks that the patient cannot perform on his/her own.
Assistance applications have the same working principle with
rehabilitation equipment, but their output commands are used
to control aided peripheral experiment like wheelchair [4],
speller [5] or meal assistance robot [32].
SSVEP-based BCI systems also have made pragmatic
progress in the smart home scenarios, which provides
disabled people more direct interactions with the environment.
It performs mainly in two aspects, controlling household
appliances and undertaking housework. SSVEP-based BCI
offers people the possibility to recognize various commands
and
control
corresponding
devices
in
their
houses
by
watching different stimuli [33]. By means of the quick
response technology QR code, Abdul et al. [34] designed
an augmented reality smart glasses to control items in the
environment, such as lights, coffee machines and elevators,
by focusing on different SSVEP stimuli displayed on the
glasses. Similarly, based on SSVEP-based BCI technology, a
hand-free control smart home has been created in [35], which
can control six devices. The SSVEP-based BCI system also
assists in reducing domestic pressure and improving home
conditions by helping people accomplish heavy housework.
Shao et al. [36] designed a novel EEG-based intelligent
teleoperation system for a mobile wall-crawling cleaning
robot, which uses the crawler type instead of the traditional
wheel type for window or ﬂoor cleaning. The developments
of SSVEP-based BCI in smart environment ﬁeld may offer
the prospect of greatly improving the quality of life for
disabled people out clinics, and considerably increase their
independence, autonomy, mobility, and ability, which also
leads to reduced social costs.
III. DATA ANALYTICS FOR SSVEP IDENTIFICATION
The data analytics of a standard SSVEP-based BCI system
generally includes signal pre-processing and SSVEP recogni-
tion. The purpose of signal pre-processing is to improve the
quality of EEG signals by removing background noises, while
the SSVEP recognition is to make the characteristics contained
in the SSVEP responses emerge and then use them to identify
the stimuli. In this section, we will elaborate on the details of
signal pre-processing and SSVEP recognition.
A. Signal pre-processing
The EEG potentials gathered by electrodes are coming from
the brain, which can be easily contaminated by muscles acti-
vation, eyes movement and external artifacts [37]. Therefore,
it is necessary to pre-process the raw EEG signal to achieve
higher SNR before the SSVEP recognition step. Thus far, there
are mainly two types of pre-processing method: ﬁltering and
blind source separation (BSS).
Band pass and notch ﬁlter are the most common pre-
processing ﬁltering to remove the noises (i.e., eye move-
ment, head movement, power noise) whose frequencies are
not overlapped with SSVEP responses. The band pass is
utilized to retain the pertinent parts of the EEG signal, which
correspond to the stimulation frequencies as well as harmonics.
The SSVEP signal is divided into different frequency bands,
and just the sub-band signal in the given frequency can be
collected. Many works about SSVEP-based BCI have adopted
band pass as the signal pre-processing algorithm, such as [6],
[18], [38]. In most countries, the frequency of power frequency
interference is commonly concentrated near 50 Hz or 60 Hz
[39], [40]. The notch ﬁlter is utilized to eliminate power line
interference, but it is prone to induce waveform distortion [40].
Besides, these time-domain ﬁltering methods require that the
correlated and uncorrelated signals are in different frequency
bands, which are not suitable for overlapping.
BSS is a popular way to enhance SSVEP responses if
the frequency range of some artifacts (i.e., EMG) and the
EEG overlap to a high degree. The BSS represents a group
of methods that recover underlying useful signals and reject
harmful artifacts through exploring the statistical indepen-
dent criteria [41], [42]. For example, independent component
analysis (ICA) returns independent sources which form the
measured EEG signal under the assumption that they are
linearly mixed [41]. Therefore, it is ﬂexible to reconstruct
the EEG signal with non-artifact components to improve the
quality of signals, thus enhance the stimulation frequency
identiﬁcation accuracy [43].
B. SSVEP recognition and classiﬁcation
SSVEP-based BCIs are generally divided into two typical
classes, named frequency-coding and phase-coding, decided
by the modulation procedure and feature variable employed

4
for classiﬁcation [39]. Frequency coding system, which has
the same number of stimuli and targets, uses visual stimuli
with different frequencies and then examines the spectral
peaks in the recorded spectrum for recognizing targets [44],
[45]. Phase coding systems, designing visual stimuli with
the same frequency but different phases, compare phase lags
between SSVEP responses and reference ones to detect gazed
target [46], [47]. Thus far, the frequency coding is often
combined with phase coding to generate a high number
of commands. Recognizing the frequency and phase of the
SSVEP with superior accuracy in a short time window (TW)
is the main task for exploiting high performance BCI sys-
tems. Many frequently used SSVEP recognition algorithms,
such as Fourier transform-based spectrum analysis, signal
decomposition-based analytics, basic spatial ﬁltering methods
and CCA-based methods are all reported in this subsection.
The advantages and disadvantages of most techniques are
also discussed, as shown in the Table. II. Moreover, many
classiﬁers utilized in the context of SSVEP identiﬁcation are
also presented in this subsection.
1) Fourier transform-based spectrum analysis methods:
The simplest detection approach for SSVEP-based BCIs is
power spectral density analysis (PSDA) which is based on
the fast Fourier transform (FFT). By transforming the time
domain EEG signals to frequency domain, amplitudes and
phases information of each stimulation frequency are obtained
for further target identiﬁcation procedure [86]. Many works
[48], [49] about SSVEP-based BCIs employ Fourier transform
due to its small computation time and simplicity. Estimating
the phase of EEG signals is another fundamental issue of
SSVEP-based BCI systems. Currently, most phase estimators
are implemented based on the discrete Fourier transform
(DFT), which highly depend on the conclusion of frequency
estimation [87]. Many efforts are dedicated to compensating
above drawback, such as the work based on energy [88] or
based on interpolated FFT [89]. However, they all fail to
remove the bias produced by frequency acquisition, which will
bring uncertainty to the phase estimation [90]. To solve this
limitation, Huang et al. [51] present a novel idea to estimate
phases based on fully-traversed DFT which enables consider-
ing all possible truncated DFT spectra to achieve direct phase
extraction and extracts instantaneous phase information in high
accuracy without any correction process.
Most current Fourier-based analysis methods require a
long window length to obtain a sufﬁciently high frequency
resolution. Moreover, when DFT is used to estimate phase
information, the data length needs to contain an integer number
of cycles, which may limit practical applications. Furthermore,
the magnitude and distribution of SSVEPs are quite different
across subjects, leading to the problem that PSDA is not robust
to real-time BCIs [91]. Some efforts attempt to solve this
issue by optimizing parameter, such as electrode and time
length selection [92], [93], which may increase the additional
work. The FFT is a linear method based on a predeﬁned basis
function, which generally requires an assumption of stationary,
so it is unable to treat the highly complex EEG signals with
nonlinear and non-stationary features well [63].
The Fourier transform-based methods normally achieve
stimulus target recognition utilizing spectrum. To be speciﬁc,
since the SSVEP carries the frequency characteristics of visual
stimulation, the frequency corresponding to the peak of the
signal power spectrum obtained by Fourier transform is deter-
mined as the stimulation frequency that induces the SSVEP
response.
2) Signal decomposition-based analysis methods: Wavelet
transform (WT) can be regarded as FT with adjustable window
[52], which is good at dealing with non-stationary signals like
SSVEP responses. WT has gained many focuses due to its
ability to provide the information about frequency components
presented in the signal, and their occurrence time simultane-
ously. For example, Rejer et al. [53] employed wavelet analy-
sis to detect both frequency and time information of SSVEP re-
sponses through translation and dilation of the mother wavelet.
In many practical application scenarios, the discrete wavelet
transform (DWT) that uses discrete translations and scales is
generally employed to decompose the given signal into several
small components according to different frequency bands,
and then components with corresponding frequencies will be
extracted for further analysis [54], [55], [63]. In WT-based
methods, the wavelet coefﬁcients of sub-bands that contain
stimulation frequencies are frequently selected as the feature
vector and input to the classiﬁer for SSVEP recognition [56].
WT shows high quality in processing non-stationary signals,
but it is still hard to demonstrate excellent performance for
highly complex SSVEPs which show nonlinear dynamics and
chaos.
Huang [59] proposed the idea of Hilbert-Huang transform
(HHT), including Empirical mode decomposition (EMD) and
Hilbert transform (HT). EMD as a nonlinear technique is
appropriate to process dynamic and complicated signals. EMD
enables to adaptively decompose signals into a group of
intrinsic mode functions (IMFs) which show oscillation feature
in the non-stationary signals [39], satisfying the requirements
of HT. Besides, IMFs are analytical, self-constructed and well-
deﬁned functions with time-varying amplitudes and frequen-
cies, indicating that EMD is an entirely data-driven approach
because it is based on original features of the signal [60].
Currently, many studies have employed EMD successfully
to achieve frequency recognition and enhance classiﬁcation
accuracy in SSVEP-based BCIs, such as [57] and [61].
Besides, ensemble empirical mode decomposition (EEMD)
was employed to deal with the mode-mixing problem caused
by signal intermittences [62]. Considering another obstacle
in EMD technique named mode misalignment in multiple-
channel decompositions, Chen et al. [63] proposed multivari-
ate empirical mode decomposition (MEMD) to better align the
corresponding IMFs of multi-channel signals. Compared with
FFT and WT, HHT has better universality to handle nonlinear
and non-stationary signals. It not only absorbs the advantages
of multi-resolution of WT but also overcomes the difﬁculty
of selecting an appropriate wavelet base which is a key
issue of wavelet analysis. However, HHT requires complicated
calculations, thus the calculation time is increased.
In the EMD-based methods, target identiﬁcation requires
further analysis of IMFs. In [57], SSVEP-related IMFs are
selected through calculating the instantaneous frequency, and

5
Table II
TARGET RECOGNITION METHODS FOR SSVEP-BASED BCI SYSTEMS
Categories
Methods
Description
Advantages
Disadvantages
Recognition/classiﬁcation
PSDA
[48], [49]
PSDA is based on the FFT. By
transforming the EEG signals from
time domain to frequency domain,
amplitudes and phases of each
stimulation frequency are obtained.
Simplicity
and
small
computation time.
It shows poor performance
on non-linear and unstable
signals.
Since the SSVEP
carries the frequency
features of visual
stimulation, the
frequency
corresponding to the
peak of the signal
power spectrum
obtained by Fourier
transform is used as the
stimulation frequency
that induces SSVEP
response.
Fourier
transform-
based
spectrum
analysis
methods
DFT [50]
Discrete Fourier transform. Most
phase estimators are implemented
based on the DFT, which highly
depend on the conclusion of fre-
quency estimation.
It achieves phase estima-
tion.
The
operation
time
of
DFT is longer than FFT.
Fully-
traversed
DFT [51]
Considering all possible truncated
sequences containing the center
sample,
spectral
leakage
in
corrected-phase
DFT
is
greatly
reduced and thus the instantaneous
phase information of the center
sample can be directly extracted.
It extracts instantaneous
phase
information
in
high accuracy without
correction process and
solves spectral leakage.
In current work, it em-
ployed two ﬂickers and
more targets may be ex-
plored in future studies.
WT [52],
[53]
WT can be regarded as FT with
adjustable window. It provides in-
formation about frequency compo-
nents and their occurrence time si-
multaneously.
It is good at dealing with
non-stationary signals.
However, it is still hard to
show an excellent perfor-
mance for nonlinear situa-
tions.
DWT
[54]–[56]
It generally decomposes the given
signal into several small compo-
nents according to different fre-
quency
bands
through
discrete
translations and scales.
Its computation is more
efﬁcient than WT.
Lack of phase informa-
tion.
In WT-based methods,
the wavelet coefﬁcients
of sub-bands that
contain stimulation
frequencies are
frequently selected as
the feature vector and
input to the classiﬁer
for SSVEP recognition
[56]. In EMD-based
methods, the frequency
of IMFs with the
maximum presence
probability and closest
to the stimulation
frequency is
determined as the
visual target [57]. The
peak frequency of
power spectra of IMFs
is also commonly
extracted and taken as
the target [58].
EMD
[58]–[60]
It can treat the highly complex
EEG signals with nonlinear and
non-stationary features better com-
pared with FFT.
It is suitable to han-
dle nonlinear and non-
stationary signals.
It faces the mode-mixing
problem caused by signal
intermittence.
Signal
decomposition-
based analysis
method
EMD
+rGZC
[57]
The
reﬁned
generalized
zero-
crossing (rGZC) method is used
to
calculate
the
instantaneous
frequencies in each IMF.
It helps EMD reduce
background noises.
The current study uses a
ﬁxed window, future re-
search may have a try on
adaptive epoch length.
EMD
+CCA
[61]
EMD and CCA are integrated to
enhance the classiﬁcation accuracy
of high-frequency SSVEPs, which
also improve the comfort level of
subjects in the experiment.
It improves the com-
fort level of users and
reduces the possibility
of inducing diseases like
epilepsy.
It may be also affected
by the problem of mode-
mixing.
EEMD
[62]
To deal with the mode-mixing
problem of EMD caused by signal
intermittences
To
reduce
mixing
of
modes and boundary ef-
fects.
It requires to set certain
initial parameters.
MEMD
[63]
MEMD
simultaneously
decomposes
multichannel
data
to
achieve
better
alignment
of
corresponding IMFs from different
channels.
It will beneﬁt narrow
band SSVEP detection
with broadband sponta-
neous EEG.
The optimization of refer-
ence signals in the whole
frequency band of training
data rather than a particu-
lar sub-band.
HHT [64]
HHT is composed of EMD de-
composition and Hilbert transfor-
mation.
It can handle nonlinear
and non-stationary sig-
nals well.
It requires more calcula-
tion time.
MEC
[65], [66]
MEC ﬁnds a spatial ﬁlter project-
ing the multi-channel signal to a
low-dimensional combined one to
weaken background noises.
Minimizing
the
back-
ground signals
It may lose useful in-
formation in EEG signals
during the linear transfor-
mation.
In MEC/MCC, the
SSVEP power
contained in the ﬁltered
EEG signal at different
frequencies are
estimated. The
frequency related to the
maximal power is
regarded as the target.
CSP is commonly used
with a single classiﬁer.
Basic spatial
ﬁltering
methods
MCC
[67]
MCC attempts to make the energy
in the SSVEP frequencies is max-
imized through the computation of
a weight matrix.
Maximizing the SNR
It may lose some useful
information in the EEG
signals.
CSP [68]
It aims to maximize the SNR of
SSVEP responses against the non-
stimulus situation.
Improving the distinc-
tion between EEG sig-
nals from the stimulus
and non-stimulus situa-
tions.
It is suitable for narrow
frequency bands, depends
on robust channel covari-
ance
matrix
estimations
and easy to overﬁtting.
Canonical
correlation
analysis-based
methods
CCA
[69], [70]
CCA tries to ﬁnd a pair of lin-
ear combinations of multi-channel
EEG signals and sine-cosine ref-
erence signals that have the max-
imum correlation with each other.
It is an effective way
to
compute
the
rela-
tion between two multi-
variable signals without
training.
The
artiﬁcial
reference
signals
lack
true
information of EEG data
and only the maximum
coefﬁcient is used.
Mway
CCA [71]
Calculating the correlation between
two multiway data arrays rather
than vector variables.
A reference signal opti-
mization step is added.
The computing time is in-
creasing.

6
L1-
Regularized
MCCA
[72]
L1-regularization is implemented
on trial-way array optimization of
MwayCCA .
Removing
obstruction
trials.
The increase in computing
time.
P-CCA
[73]
The SSVEP response phases are
estimated based on the physiologi-
cally apparent latency.
SSVEP response phase
is placed to the reference
signal as a constraint.
It improves the standard
CCA method in compli-
cated ways that may be
difﬁcult to understand and
implement in real practice.
MsetCCA
[74]
MsetCCA extracts common fea-
tures shared by the real EEG sig-
nals to optimize reference signals.
The
performance
are
better than MwayCCA
and CCA.
It may treat background
noises as common fea-
tures.
MCM
[18]
In order to avoid extracting the
background noise as common fea-
tures, the MCM adopts superiori-
ties of both CCA and MsetCCA.
It
further
improves
SSVEP
recognition
accuracy by designing
three-layer of correlation
maximization steps.
It shows relative poor per-
formance
with
a
short
time window.
Fuzzy
ensemble
system
[75]
The advantages and disadvantages
of the MLR and MsetCCA are in-
vestigated using expert knowledge,
and the rules are developed for
their strategic combination to im-
prove the overall performance.
It
can
become
2.5%
higher than the best re-
sponse
between
these
two methods in the best
condition
in
detecting
frequency.
A successful fuzzy ensem-
ble system needs sufﬁcient
and correct expert infor-
mation on the subsystem.
FBCCA
[76]
It includes three major steps: ﬁlter
bank analysis, CCA between sub-
band components and sinusoidal
reference signals, and target iden-
tiﬁcation.
It
incorporates
fundamental
and
harmonic
frequency
components together for
target detection.
The reference signals are
sine-cosine waves, which
may need further improve-
ment.
In the CCA-based
methods, correlation
coefﬁcients can be
calculated between a
SSVEP response and
reference signals at
each stimulus
frequency [18]. The
frequency related to the
maximal correlation
coefﬁcient is
determined as the
target.
Canonical
correlation
analysis-based
methods
FBCCA
+BF [77]
A combination of the training-free
feature extraction capabilities of
FBCCA with the accurate physio-
logical representation capability of
the spatiotemporal beamforming.
It
can
describe
the
variational
and
individually
different
physiological
SSVEP-
based BCIs better.
The stimulation time ef-
fects the experimental re-
sults. Too long or too
short stimulation time will
cause
ITR
to
become
worse.
IT-CCA
[78]
The reference signal is individ-
ual template acquired by averaging
multiple training trials.
It is proposed to de-
tect temporal features of
EEG signals.
The screen refresh rate in-
ﬂuences the system per-
formance.
A combi-
nation
method
of CCA
and
IT-CCA
[79], [80]
Three weight vectors are applied
as spatial ﬁlters which form four
correlation vectors as recognition
features.
It alleviates the interfer-
ence from spontaneous
background EEG activi-
ties by incorporating in-
dividual SSVEP training
data.
The ITCCA-based method
requires precise time syn-
chronization
between
a
stimulation program and
EEG recording.
KCCA
[81], [82]
The kernel is applied to project
the data to high-dimension space
to solve the problem that CCA is
infeasible for nonlinear relation ex-
isting in the real signals.
Linear
CCA-based
methods
may
be
insufﬁcient
given
the
complexity
of
EEG
signals. KCCA provides
a nonlinear method to
solve
the
frequency
detection problem.
How to choose the ap-
propriate
kernel
is
still
a question worth thinking
about.
DCCA
[83]
In DCCA, deep networks are used
to process input data before CCA
procedure.
DCCA
improves
the
performance of SSVEP-
based BCI with higher
SNR
and
detection
accuracy
compared
to
those of CCA.
DCCA
only
considers
the nonlinear correlation
between EEG signals and
reference templates rather
than
the
information
within the real signals.
DMCCA
[38]
It can extract more real informa-
tion within the EEG signals than
DCCA.
The
DMCCA-based
method
effectively
improves the accuracy
at short time windows.
The
background
noises
contained in the SSVEP
are also nonlinear, which
may be represented with
real useful information by
neural networks.
CORRCA
[84], [85]
CORRCA can calculate same spa-
tial ﬁlters for two multichannel sig-
nals.
It remedies the limita-
tion that standard CCA
method requires spatial
ﬁlters to be orthogonal.
It
requires
individual
training
data,
which
is
cumbersome
and
time-consuming.
TRCA
[6]
TRCA extracts task-related com-
ponents efﬁciently by maximizing
the reproducibility of time-locked
activities across trials.
TRCA has the potential
to eliminate the back-
ground unrelated activi-
ties from EEG.
It also needs training data,
which might resort to the
transfer learning method
to obtain the spatial ﬁl-
ters with existing datasets
from other subjects.

7
then the frequency with the maximum presence probability
and closest to the stimulation frequency is determined as the
visual target. Moreover, the power spectra of IMFs that contain
stimulation frequencies are also used for SSVEP recognition.
The peak frequency is commonly extracted and taken as the
target [58]. In addition, the EMD can also combine with CCA
where the IMFs contain almost all the energy are selected and
input into CCA for SSVEP detection [61].
3) Basic spatial ﬁltering methods: The combination of
signals collected from different electrodes is called spatial
ﬁltering [39]. In the past few years, multi-channel-based
frequency recognition methods have received much attention,
because they overcome inter-subject variations which cannot
be solved by single-channel SSVEPs [16], [69]. By optimizing
the combination of data from multiple electrodes with less
parameter optimizations, the algorithm’s anti-noise capability
is greatly enhanced than unipolar or bipolar systems. Minimum
energy combination (MEC) and maximum contrast combi-
nation (MCC) are two common spatial ﬁltering algorithms,
but they have different objective functions. The core idea
of MEC is to ﬁnd a spatial ﬁlter that projects the original
multi-channel signal to obtain a low-dimensional combined
one in order to weaken the noise and other artifact signals
[65], [66]. However, MCC approach attempts to make the
energy in SSVEP frequencies maximized through computing
a weight matrix [67]. Therefore, one advantage of spatial
ﬁlters is computational time reduction by combining signal
preprocessing and feature selection. For each reference signal,
MEC or MCC can obtain a spatial ﬁlter which is applied
over the original EEG data. And then the total SSVEP power
contained in the cleaned EEG signal at each stimulation
frequency is estimated. The target frequency should be the
frequency of the reference signal that maximizes the SSVEP
power [94].
Common spatial pattern (CSP) [68], [95] is another spatial
ﬁlter to improve the distinction between EEG signals from
stimulus and non-stimulus situations. There are two distri-
butions in a C-dimensional space where C is the number
of known channels, and CSP attempts to ﬁnd projections
minimizing the variance of one class but maximizing the
variance of the other one. In SSVEP-based BCIs, it aims
to maximize the SNR of SSVEP responses against the non-
stimulus situation [68]. CSP as a spatial ﬁltering method that
enhances the SSVEP is generally combined with the sepa-
rate feature extraction and classiﬁcation steps to distinguish
different stimulation frequencies [24]. For example, in [68],
the amplitude estimations of the ﬁltered SSVEPs at different
stimuli were extracted and then linear discriminant analysis
(LDA) performed classiﬁcation task.
The above three spatial ﬁlters reduce artifacts and noise
signals by extracting spatial features. However, for the algo-
rithms based on MEC and MCC, performance may decrease
due to some useful information contained in the signal also
eliminated during the linear transformation.
4) Canonical correlation analysis-based methods:
The
canonical correlation analysis (CCA) method is used to ﬁnd
the relationship between two sets of data, which can be used
as a feature extraction algorithm in SSVEP-based BCIs. The
CCA-based spatial ﬁlter, ﬁrst presented by Lin et al. [69],
has attracted many interests in recent years due to better
SNR, higher recognition accuracy, well usage of harmonic
frequencies, and lower inter-subject variability [24]. The CCA
attempts to ﬁnd a pair of linear combinations of the multi-
channel signals and the artiﬁcial reference signals, generally
sine and cosine waves, that have the correlation maximization
at each stimulus frequency. Then, the frequency related to
the maximal correlation coefﬁcient is determined as the target
[69], [70]. Nowadays, many improved CCA-based methods are
proposed due to higher requirements of performance indexes
such as SNR and ITR, or the drawbacks of CCA, e.g. the
artiﬁcial reference signals lack true information of EEG data,
and multi-channel signals are easily inﬂuenced by background
noise such as spontaneous EEG.
a) Multiway canonical correlation analysis (MwayCCA):
Before introducing MwayCCA, the concept of tensor should
be ﬁrstly referred. A tensor is a multiway array of data, and
its order is the number of dimensions, also called models or
ways [96]. Tensor CCA is a development of standard CCA,
which concentrates on calculate the correlation between two
multiway data arrays, rather than two sets of variables based on
vector [97]. Based on this concept, MwayCCA optimizes the
reference signals through maximizing the correlation between
third-order EEG data tensor (channel × time × trial) and
pre-constituted sine-cosine reference signal matrix (harmonic
× time) [71]. Then, target frequency can be recognized by
applying multiple linear regression (MLR) or CCA between
test EEG data and optimized reference signals [71]. In Mway-
CCA, EEG tensor is constructed by multiple trials where
some trials may contain more artifacts which generally have
negative contribution to the reference signal optimization.
Therefore, L1-regularization is implemented on trial-way array
optimization of MwayCCA to remove obstruction trials [72].
MwayCCA and its variation add a reference signal optimiza-
tion procedure, so that the reference signal is enriched with
more real information of EEG signals, thereby improving the
performance of standard CCA. The disadvantage is that the
consequent increase in computing time.
b) Phase constrained canonical correlation analysis (p-
CCA): Except the amplitude information, phases of SSVEPs
are also important for improving target frequency detection
accuracy [98], which have been used to add the number of
visual stimuli. Wang et al. [17] provided a benchmark SSVEP
dataset with a 40 targets BCI speller which was coded using
a JFPM method.
In study [73], phase constrained CCA (p-CCA) is proposed
for recognising the phase of SSVEP responses based on the
apparent latency L that means the delay of SSVEP responses
caused by the transfer time of visual pathway. L is ﬁxed for a
speciﬁc subject but unknown for all the stimulus frequencies
[99] and it can be estimated using SSVEP phases Φs, that is
deﬁned as the phase lag between the fundamental component
and the closest prior stimulus [73]. Then Φs is calculated
through the EEG training data of a subject, and L can be solved
through an exhaustive search process using the results of Φs
[24]. It is presented in [73] that for a speciﬁc subject, SSVEP
response phases Φr are derived from the apparent latency L

8
and proportional to the different stimulus frequencies. Finally,
Φr as a constraint condition is placed to the preconstructed
sine-cosine reference signals which is further used for calcu-
lating canonical correlation with test data.
The p-CCA optimizes the reference signal from the phase
perspective, and can distinguish SSVEP responses of different
phases at the same frequency, thereby increasing the diversity
of visual stimulus coding. Therefore, compared with ordinary
CCA, p-CCA is more universal and comprehensive.
c) Multiset canonical correlation analysis (MsetCCA):
The original constructed reference signals with sine-cosine
waves are generally short of real information of EEG data,
which go against SSVEP frequency recognition. Multiset
canonical correlation analysis (MsetCCA), proposed by Zhang
et al. [74], considers common features shared by EEG signals
may be more real and natural compared with predeﬁned
signals. For a speciﬁc subject, some common characteristics
contained in a set of trials at a certain stimulus frequency,
which can be used to construct optimal reference signals to
achieve a higher detection accuracy. To be speciﬁc, MsetCCA
learns multiple linear transforms that maximizes the overall
correlation among canonical variates from multiple sets of
random variables [74]. Therefore, in the SSVEP-based BCIs,
the optimal reference signals can be determined by MsetCCA
through the joint spatial ﬁltering of multiple sets of EEG
training dataset for each stimulus frequency [100]. Jiao et al.
[18] further presented a three-layer model based on MsetCCA,
named multilayer correlation maximization (MCM) which
adopts superiorities of both CCA and MsetCCA to avoid
extracting the background noise as common features. Ziafati et
al. [75] proposed a fuzzy ensemble system which encompasses
the beneﬁts of all the subsystems, i.e. multivariate linear
regression (MLR) and MsetCCA. The new SSVEP frequency
detection architecture shows more ﬂexibility in performance
compared with MLR and MsetCCA.
MsetCCA produces fully optimized reference signals based
on the EEG signal training set. It turns out that the averaged
classiﬁcation accuracy and ITR of MsetCCA are better than
them of MwayCCA and CCA [100]. However, one drawback
is that it may treat background noises as common features, so
it need to be used with other denoising algorithms.
d) Filter bank canonical correlation analysis (FBCCA):
Considering that harmonic SSVEP components are not be em-
ployed for frequency recognition, Chen et al. [76] incorporated
fundamental and harmonic frequency components to propose a
new method, called ﬁlter bank canonical correlation analysis
(FBCCA). The FBCCA method contains three steps, ﬁrstly,
a ﬁlter bank analysis implemented sub-band decomposition
from EEG signals with multiple ﬁlters that have different pass-
bands. And then, CCA is employed to calculate the correlation
between the sub-band components and the constructed refer-
ence signals with sine-cosine waves related to all stimulation
frequencies. Finally, a weighted sum of squares of the corre-
lation for all sub-band components are combined as the ﬁnal
feature for frequency identiﬁcation. In order to compensate the
deﬁciency that the reference signals are sine-cosine waves, Ge
et al. [77] proposed a bimodal decoding algorithm, absorbing
the advantages of the training-free recognition of FBCCA and
the data-driven adaptive features of spatiotemporal beamform-
ing (BF), which can describe the variational, complicated and
individually different physiological SSVEP-based BCIs better.
FBCCA was often combined with current innovative meth-
ods in [85], [101], thereby further optimizing them and achiev-
ing higher detection performance. It can be seen that FBCCA
is expected to become a new standard paradigm after CCA.
e) Individual template canonical correlation analysis-
based methods: The individual template based CCA (IT-CCA)
was ﬁrst proposed in [78] to optimize the reference signals
with sine-cosine waves by detecting temporal features of EEG
data. The IT-CCA calculates the canonical correlation between
test data and individual template signals acquired by averaging
multiple training trials. Nakanishi et al. [79], [80] developed
it and proposed a combination method of CCA and IT-CCA,
that applies three weight vectors as spatial ﬁlters for enhancing
the target detection, they are spatial ﬁlter between test data
and the individual template, spatial ﬁlter between test data
and preconstructed reference signals, and spatial ﬁlter between
the individual template and preconstructed reference signals,
respectively. Then four correlation vectors as recognition fea-
tures are obtained by above spatial ﬁlters, and an ensemble
classiﬁer is employed to combine four vectors to form a
weighted correlation coefﬁcient as the ﬁnal feature [100].
Two limitations of individual template-based SSVEP detec-
tion algorithms may need to be noticed and researched in the
future work [2]. The ﬁrst problem is that they require precise
time synchronization between a stimulation program and EEG
recording procedure in order to exert the superiority of JFPM
coding. Moreover, the stability of stimulus performance may
affect the outcome of the ITCCA-based methods.
f) Nonlinear extensions of CCA: The transformation of
CCA maximizes the mutual information between extracted
multi-dimension features, but it is infeasible to deal with non-
linear relations existing in real signals [93]. Considering the
kernel method used in SVM is applicable for linear situations,
Akaho et al. [81] proposed a kernel CCA (KCCA) method. For
asynchronous SSVEP-based BCIs, Zhang et al. [82] presented
a KCCA based idle-state detection method, which provided a
practicable way to extract nonlinear characteristics of multi-
dimension EEG signals. However, there are two limitations of
KCCA method, ﬁrstly, its representation is restricted by the
ﬁxed kernel, besides, its training time changes with the size
of training dataset. Andrew et al. [83] further developed deep
CCA (DCCA) which can compensate the above drawbacks of
nonlinear models. DCCA processes input data through deep
network before calculating their correlations. Liu et al. [38]
proposed an extension of DCCA, named deep multiset CCA
(DMCCA) for SSVEP frequency recognition, that extracts
the information within the real EEG signals to attain better
detection accuracy.
The above nonlinear frequency recognition algorithms are
more in line with the characteristics of original EEG signals,
leading to better results than the CCA. For KCCA, how to
choose the appropriate kernel is still a question worth think-
ing about. DMCCA achieved better recognition performance
by combining nonlinear method DCCA and linear method
MsetCCA, which provides us a potential research direction.

9
g) Correlated component analysis (CORRCA): The CCA
requires spatial ﬁlters to be orthogonal, however, it is an
impractical condition for EEG signals. In addition, CCA
distributes two projection vectors for two multi-dimension
signals, which contributes the number of free parameters
doubling, thus the detection performance is impaired [84].
Dmochowski et al. [102] proposed correlated components
analysis (CORRCA) that calculates same spatial ﬁlters for
two multichannel signals based on maximizing the linear
components of the two. In 2018, Zhang et al. [85] introduced
the CORRCA to learn spatial ﬁlters with multiple trials of
individual training data for SSVEP-based BCI systems, which
is a potential technique to reduce background EEG activities.
Zhang et al. [84] further developed CORRCA to a two-stage
architecture, that utilizes all the spatial ﬁlters obtained from
all stimulus frequencies to improve the approach accuracy.
Compared with CCA, CORRCA reduces the number of
parameters and improves the identiﬁcation accuracy. In order
to further improve performance, the two-stage CORRCA intro-
duced an ensemble spatial ﬁltering strategy. In a SSVEP-based
BCI system, the Nf visual stimuli generate Nf individual
training data, resulting in Nf spatial ﬁlters. These spatial ﬁlters
should be similar in ideal conditions, because the mixing
coefﬁcients from the source of SSVEP responses to the scalp
EEG signals can be considered similar in a narrow frequency
range [103], [104], which shows the possibility of further
development by assembling Nf spatial ﬁlters.
h) Task-related component analysis (TRCA): Many tech-
niques [105], [106] have been developed to extract task-related
source signals from scalp recordings based on the idea that
cortical source activities can be rebuilt through a weighted
linear summation of EEG signals from multiple electrodes.
Tanaka et al. [107], [108] proposed task-related component
analysis (TRCA) which achieves better performance com-
pared with other task-related methods due to maximize the
reproducibility of time-locked activities across trials. In 2017,
Nakanishi et al. [6] introduced TRCA-based analysis to EEG
study especially SSVEP-based BCI systems, which success-
fully enhanced the SNR of EEG signals through eliminating
the background noises and showed great capacity for dif-
ferent applications in communication and control. SSVEPs
are time-locked photic-driving responses related to repetitive
visual stimuli. Therefore, TRCA-based techniques have a great
possibility to achieve higher SNR of EEG signals [2], [16].
In the CCA-based methods, correlation coefﬁcients can be
calculated between a SSVEP response and reference signals
at each stimulus frequency [18]. The frequency related to the
maximal correlation coefﬁcient is determined as the target.
5) Traditional pattern recognition methods: In addition
to the aforementioned target identiﬁcation methods, some
traditional pattern recognition methods involving classic clas-
siﬁers such as LDA, SVM and k-nearest neighbour (kNN)
are also usually used for SSVEP classiﬁcation scheme [44],
[109]. Features corresponding to different visual stimuli are
regarded as the feature vector to train the classiﬁer based
on training data. Then, the experiment is conducted on the
testing data with the trained classiﬁer to determine targets.
For example, in [110], the power spectral density in all
possibly evoked frequency bands is extracted from the SSVEP
responses to facilitate the discrimination task. In this work,
three classiﬁers, namely LDA, SVM and extreme learning
machines (ELM) are performed at the target detection stage
and the ELM shows more promising classiﬁcation capacity
in the context of SSVEP. Therefore, it proves the good
generalization performance of neural network-based methods
for SSVEP classiﬁcation. The convolutional neural network
(CNN) is another popular classiﬁer for SSVEP-based BCIs.
For instance, Kwak et al. [111] explored a CNN architecture
with a spatial convolutional layer and a temporal one which
uses band power features from two EEG channels, resulting
in classiﬁcation rates of 99.28% and 94.03% in the static
and ambulatory scenario, respectively. With this background,
neural network-based classiﬁers seem to be more potential and
efﬁcient options to achieve higher accuracy with a mass of
EEG data. Meanwhile, it is worth noting that wider knowledge
and more time or more data are needed for adjusting related
parameters and training feasible models [112].
IV. CHALLENGES AND OPPORTUNITIES
Although signiﬁcant achievements in SSVEP data analytics
have been made in the past decades, some new emerging
issues need to be further explored, such as the pre-trained
model, the spontaneous EEG signals, mental fatigue, transfer
learning and hybrid BCIs. In this section, we brieﬂy describe
these directions and current development. The underlying
challenges and some potential ideas are also illustrated.
A. The pre-trained model for EEG classiﬁcation
The big data generated by the human brains maintains long
period neural recordings of a great number of subjects under
various conditions. Due to the considerable large volume
of data, the SSVEP-based BCI system requires an efﬁcient
method to compress, analyze and classify the collected
signals. Recently, data-driven methods based on deep learning
were applied in dealing with EEG signals. For example, Gao
et al. [113] designed a convolutional neural network with long
short-term memory (CNN-LSTM) architecture, which extracts
the spectral, spatial as well as temporal features of SSVEPs
in order to achieve the high classiﬁcation performance.
However, Ditthapron et al. [114] stated that it is complicated
and costly to collect a large number of EEG signals for
training CNN-LSTM architecture, so a pre-trained model
called event-related potential encoder network (ERPENet)
was proposed to classify the attended and unattended event.
Generally, the pre-trained model can be ﬁne-tuned and then
employed to a novel related scenario to solve insufﬁcient
data and detection accuracy problem [5]. For instance,
Embrandiri et al. [115] employed denoising autoencoder to
pre-train the network and then the network was trained by
back-propagation to maximize contrast/SNR, which proves
the feasibility of pre-trained model in SSVEP detection.
Therefore, the advanced ERPENet in [114] proposed for
ERP/P300 classiﬁcation may provide potential direction for
SSVEP-based BCI systems, which can ease the pressure of

10
store and analyze large-scale data.
B. The spontaneous EEG signals
According to the cited papers about CCA, we know that
many methods have considered the reference signal opti-
mization procedure, like MwayCCA, MsetCCA and MCM
[18], [71], [74]. With these approaches, the performance of
target detection in SSVEP-based BCI systems has been highly
enhanced compared with the CCA. MsetCCA and MCM
alleviate the interference from spontaneous brain activities
and improve the SNR of SSVEPs through incorporating real
information existing in EEG signals. The result of [6] also
indicates that TRCA increases the gap between target and non-
target feature by removing background EEG signals. However,
these researches have not paid enough attention to the correla-
tion between SSVEP responses and spontaneous EEG signals.
No matter how large or small the correlation coefﬁcient
is, it always has the special but meaningful implication for
frequency detection. Meanwhile, limited studies consider the
nature of spontaneous EEG [116], which may be a new view
for solving background noises issues.
C. Mental fatigue
The SSVEP-based BCI systems have been successfully
applied in many ﬁelds, but mental fatigue is still a tough
problem for both users and researchers. Most publications
mentioned focus on the performance of frequency recognition,
but the accuracy of classiﬁcation may be damaged due to the
appearance of fatigue symptoms in the operation [117]. The
fatigue can induce many severe problems, such as signal qual-
ity declining, recognition ability deterioration and even risk
of photosensitive epileptic seizures [118], pushing SSVEP-
based BCI systems to higher development [119]. Zhang et al.
[120] studied how much metal fatigue subjects have through
the change of oxygen saturation obtained by near-infrared
spectrum approach when they use an intelligent artiﬁcial limb.
Some researches [61], [121] attempted to reduce subjects
fatigue by employing visual stimuli in higher frequencies,
however, they cannot be adaptive according to the state of
mental fatigue. Recently, Talukdar et al. [122] proposed an
adaptive structure for the CSP based on the mental fatigue
of the subjects for motor-imagery BCI, which can adapt the
CSP through employing LDA, providing a potential solution
for SSVEP-based BCI systems.
D. Transfer learning
Another limitation of most methods in Section III is that
they need to collect training data from each subject and then
proceed a long calibration process. The reason is that high
dimensional EEG signals contain much background noises,
and they are highly non-stationary due to large variations
across the subject or within subjects psychological and mental
states, experimental circumstances [2]. Therefore, the trained
classiﬁer obtained from previous trials may show poor per-
formance on new trials or new subjects [123]. Many studies
have tried to short calibration time through transfer learning,
where data collected from existing users or trials can be used
to new ones [124]. Chiang et al. [123] proposed a cross-
subject transfer approach combined least-squares transforma-
tion (LST) and TRCA, which largely reduces the variability
of SSVEP signals across individuals. Unsupervised transfer
learning [125], [126]have also gained much attention, for
example, Waytowich et al. [125] presented a transfer approach
named spectral transfer using information geometry (STIG),
learning single-trial detection successfully in ERP-based BCI
without the existence of calibration data, which provides a
creative and practical idea for SSVEP-based BCIs.
E. Hybrid BCIs
One of the drawbacks of SSVEP-based BCI is the require-
ment of the constant attention to the light source, which may
be difﬁcult and annoyed for some patients. Hybrid BCIs that
improve the quality of BCIs systems with single modality
through combining two or more BCI paradigms could provide
potential solutions for this problem [127]. To be speciﬁc, in
hybrid paradigms, the number of control commands can be
increased through decoding the brain activities simultaneously
[128]. For example, in a Tetris game [129], rotating command
requires a continuous gaze of visual stimulus to evoke SSVEP
potentials. Meanwhile, the active motor imagery (MI) is em-
ployed to output two control commands, which are used to
move bricks toward left and right. This multi-modality system
avoids long gazing stimuli, which cause discomfort. Besides,
hybrid BCIs are capable of enhancing system classiﬁcation
accuracy. For instance, Wang et al. [130] designed a new
hybrid paradigm (shape-changing and ﬂickering-hybrid) based
on P300 and SSVEP, which improves performance for some
subjects. The works on the hybrid BCI are increasing in the
past few years, but the portable, wearable and low-cost related
products that can be employed for the public need further
commercialization [128]. Moreover, the target detection al-
gorithm adopted in many SSVEP-based hybrid systems is
standard CCA [129]–[131], which can be further improved
by the advanced signal analysis methods illustrated in Section
III in order to achieve higher performance.
V. DISCUSSION
In this review, we mainly targeted the SSVEP systems
that use frequency/phase to modulate visual oscillating stim-
uli. However, the stimuli patterns/colors may also affect the
SSVEP identiﬁcation accuracy. Besides, there are also some
systems using amplitude coding or without gazing. In this
section, we will provide a brief overview of these areas.
A. Stimulus design
In general, in addition to multiple target coding and target
identiﬁcation methods, the performance of an SSVEP-based
BCI is also attributed to the stimulus design [2], including
the choice of light source, stimulus color and the color of
background, etc. Zhu et al. [23] reported that the computer
screen and LED are the most frequently used stimulation

11
types. Furthermore, compared with systems using computer
screens, the SSVEP-based BCIs that employ LED for stimulus
design have higher bit rates. Besides, LEDs can be controlled
by waveform generators which are easy to create various
frequencies, so LEDs are preferable in most applications.
Meanwhile, the color of visual stimuli is also an important
factor that affects the SSVEP system. Chu et al. [132] investi-
gated the inﬂuence of 10 stimulus colors on SSVEPs and found
that colors with a longer wavelength, such as red and orange,
have better SSVEP responses. However, the choice of color
depends not only on the SNR value or the accuracy of BCI, but
also on the comfort of the subject. Through parallel analysis
of SNR and comfort, Jukiewicz et al. [133] presented that
green is perceived the most friendly color for users. Another
factor is the background color. The selection rule is that higher
contrast between the stimulus color and background color
invokes higher potentials, visibility and brightness. The most
employed background color is black [134], but it is known
that the dynamic scene condition may be inevitable in most
practical usages. Therefore, how to choose the appropriate
stimulus color and light source, while compensating for the
performance degradation caused by the dynamic scene, is a
problem that requires to be considered in future research.
B. Amplitude modulation
In general, SSVEP-based BCI systems are designed based
on frequency-coding and phase-coding, but many works fo-
cused on amplitude modulation [135], [136]. It is widely
useful and critical for a SSVEP-based BCI system to predict
various modes of amplitude modulations, especially for stable
control of future neural rehabilitation tasks. Autthasan et al.
[137] pointed out that the SSVEP amplitude changes as a
function of stimulus luminance contrast and then proposed an
integrated architecture to predict the frequency and contrast-
related amplitude modulations of the SSVEP signal simulta-
neously. Moreover, except for luminance contrast, attention
generally enhances rhythmic brain responses at the frequency
of the stimulus. For example, Gulbinaite et al. [138] explored
the effect of attention on the amplitude of SSVEPs in a wide
range of temporal frequencies (3-80 Hz). The research results
showed that such inﬂuence is frequency-dependent, namely
different ﬂicker frequency bands like theta, gamma and alpha
have various relationships with amplitudes. However, there
are still some limitation of current amplitude coding related
works, such as the eye fatigue effect in [137]. An amplitude-
modulated visual stimulation for reducing eye fatigue proposed
by Chang et al. [136] that achieved a similar manner to high-
frequency stimuli may provide a ﬂexible way to solve this
issue. To further conﬁrm this investigative idea, online/real-
time experiments are required.
C. SSVEP-based BCI without gazing
SSVEP-based BCIs generally require the subject changing
his/her gaze direction to focus on different target stimuli,
which is difﬁcult for those patients with severe motor impair-
ment, because they are unable to control gaze optionally [23].
Therefore, it is essential to design gaze-independent BCIs in
order to satisfy more users’ need. The BCI in [139] utilized
visual spatial attention mechanisms to classify binary trials
as left-attended or right-attended. Except for spatial attention,
people can modify the energy of the evoked response without
gazing at the stimulus with the aid of selective attention. A
SSVEP-based BCI design was proposed in [140], in which the
energy difference between SSVEP responses induced under
attend and ignore conditions was maximized, resulting in
higher classiﬁcation accuracy. Moreover, a visual stimulus
used in [141] combined these two designs, where visual
selectivity through the perception and neural mechanism of
spatial attention was conﬁrmed. Although the SSVEP-based
BCI system without gazing is more robust and friendly in
the face of individual differences, there is still a complicated
problem that hinders its development, namely the limited
targets. For example, there are only two targets in [140] and
[141]. Further research may focus on increasing the number of
targets by employing spatial attention and selective attention
together.
VI. CONCLUSION
This study performed a comprehensive review of the
SSVEP-based BCI system, mainly focusing on signal ana-
lytics. The healthcare application of the SSVEP-based BCI
system was also brieﬂy introduced. The state-of-the-art devel-
opments of data pre-processing, spectrum analysis, classiﬁer,
spatial ﬁltering such as CCA and its extensions as well as
their limitations were presented in order to provide feasible
references for future research. Besides, some novel emerg-
ing directions of SSVEPs including the pre-trained model,
spontaneous EEG signals, mental fatigue, transfer learning and
hybrid BCIs were also introduced. Finally, this work discussed
some innovative and unconventional aspects including ampli-
tude modulation, SSVEP-BCIs without gazing and stimulus
design.
ACKNOWLEDGMENT
This work was supported in part by Engineering and
Physical Sciences Research Council (EPSRC) (Grant No.
EP/S019219/1) and in part by China Scholarship Council
(CSC) (Grant No. 201906460007).
REFERENCES
[1] L. F. Nicolas-Alonso and J. Gomez-Gil, “Brain computer interfaces, a
review,” Sensors, vol. 12, no. 2, pp. 1211–1279, 2012.
[2] T. Tanaka and M. Arvaneh, Signal processing and machine learning for
brain-machine interfaces.
Institution of Engineering & Technology,
2018.
[3] U. Chaudhary, N. Birbaumer et al., “Brain–computer interfaces for
communication and rehabilitation,” Nat. Rev. Neurol., vol. 12, no. 9, p.
513, 2016.
[4] X. Deng, Z. L. Yu et al., “A bayesian shared control approach for
wheelchair robot with brain machine interface,” IEEE Trans. Neural
Syst. Rehabil. Eng., 2019.
[5] J. J. Podmore, T. P. Breckon et al., “On the relative contribution of deep
convolutional neural networks for SSVEP-based bio-signal decoding
in BCI speller applications,” IEEE Trans. Neural Syst. Rehabil. Eng.,
vol. 27, no. 4, pp. 611–618, 2019.
[6] M. Nakanishi, Y. Wang et al., “Enhancing detection of SSVEPs for a
high-speed brain speller using task-related component analysis,” IEEE
Trans. Biomed. Eng., vol. 65, no. 1, pp. 104–112, 2017.

12
[7] F. Lotte, L. Bougrain et al., “A review of classiﬁcation algorithms for
EEG-based brain–computer interfaces: a 10 year update,” J. Neural
Eng., vol. 15, no. 3, p. 031005, 2018.
[8] N. Naseer and K.-S. Hong, “fNIRS-based brain-computer interfaces: a
review,” Front. Hum. Neurosci., vol. 9, p. 3, 2015.
[9] M. L¨uhrs, B. Sorger et al., “Automated selection of brain regions for
real-time fMRI brain–computer interfaces,” J. Neural Eng., vol. 14,
no. 1, p. 016004, 2016.
[10] Y.-H. Chen, J. Saby et al., “Magnetoencephalography and the infant
brain,” NeuroImage, 2019.
[11] F. Wallois, M. Mahmoudzadeh et al., “Usefulness of simultaneous eeg–
nirs recording in language studies,” Brain and language, vol. 121, no. 2,
pp. 110–123, 2012.
[12] T. Liu, M. Pelowski et al., “Near-infrared spectroscopy as a tool for
driving research,” Ergonomics, vol. 59, no. 3, pp. 368–379, 2016.
[13] T. J. Sejnowski, P. S. Churchland et al., “Putting big data to good use
in neuroscience,” Nature neuroscience, vol. 17, no. 11, pp. 1440–1441,
2014.
[14] P. Sawangjai, S. Hompoonsup et al., “Consumer grade EEG measuring
sensors as research tools: A review,” IEEE Sensors Journal, vol. 20,
no. 8, pp. 3996–4024, 2019.
[15] I. Lazarou, S. Nikolopoulos et al., “EEG-based brain–computer in-
terfaces for communication and rehabilitation of people with motor
impairment: a novel approach of the 21st century,” Front. Hum.
Neurosci., vol. 12, p. 14, 2018.
[16] F.-B. Vialatte, M. Maurice et al., “Steady-state visually evoked po-
tentials: focus on essential paradigms and future perspectives,” Prog.
Neurobiol., vol. 90, no. 4, pp. 418–438, 2010.
[17] Y. Wang, X. Chen et al., “A benchmark dataset for SSVEP-based
brain–computer interfaces,” IEEE Trans. Neural Syst. Rehabil. Eng.,
vol. 25, no. 10, pp. 1746–1752, 2016.
[18] Y. Jiao, Y. Zhang et al., “A novel multilayer correlation maximization
model for improving CCA-based frequency recognition in SSVEP
brain–computer interface,” Int. J. Neural Syst., vol. 28, no. 04, p.
1750039, 2018.
[19] A. Rezeika, M. Benda et al., “Brain–computer interface spellers: A
review,” Brain. Sci., vol. 8, no. 4, p. 57, 2018.
[20] F. Masood, M. Hayat et al., “A review of brain computer interface
spellers,” in Proc. IEEE Int. Conf. Emerg. Trends. Smart. Nanotechnol.,
2020, pp. 1–6.
[21] S. Amiri, R. Fazel-Rezai et al., “A review of hybrid brain-computer
interface systems,” Advances in Human-Computer Interaction, vol.
2013, 2013.
[22] I. Choi, I. Rhiu et al., “A systematic review of hybrid brain-computer
interfaces: Taxonomy and usability perspectives,” PloS one, vol. 12,
no. 4, p. e0176674, 2017.
[23] D. Zhu, J. Bieger et al., “A survey of stimulation methods used in
SSVEP-based BCIs,” Comput. Intel. Neurosc., vol. 2010, 2010.
[24] R. Zerafa, T. Camilleri et al., “To train or not to train? A survey
on training of feature extraction methods for SSVEP-based BCIs,” J.
Neural Eng., vol. 15, no. 5, p. 051001, 2018.
[25] Z. Cao, C.-T. Lin et al., “Extraction of SSVEPs-based inherent fuzzy
entropy using a wearable headband EEG in migraine patients,” IEEE
Trans. Fuzzy Syst., vol. 28, no. 1, pp. 14–27, 2019.
[26] A. Spiegel, J. Mentch et al., “Slower binocular rivalry in the autistic
brain,” Current Biology, vol. 29, no. 17, pp. 2948–2953, 2019.
[27] S. Sridhar and V. Manian, “Assessment of Cognitive Aging Using
an SSVEP-Based Brain–Computer Interface System,” Big Data and
Cognitive Computing, vol. 3, no. 2, p. 29, 2019.
[28] F. Alimardani, J.-H. Cho et al., “Classiﬁcation of bipolar disorder
and schizophrenia using steady-state visual evoked potential based
features,” IEEE Access, vol. 6, pp. 40 379–40 388, 2018.
[29] M. R. Goldstein, M. J. Peterson et al., “Topographic deﬁcits in alpha-
range resting EEG activity and steady state visual evoked responses in
schizophrenia,” Schizophrenia research, vol. 168, no. 1-2, pp. 145–152,
2015.
[30] X. Zhao, Y. Chu et al., “SSVEP-based brain–computer interface
controlled functional electrical stimulation system for upper extremity
rehabilitation,” IEEE T. Syst. Man.Cy-S., vol. 46, no. 7, pp. 947–956,
2016.
[31] X. Zeng, G. Zhu et al., “A feasibility study of SSVEP-based passive
training on an ankle rehabilitation robot,” J. Healthc. Eng., vol. 2017,
2017.
[32] C. J. Perera, I. Naotunna et al., “SSVEP based BMI for a meal
assistance robot,” in Proc. IEEE Int. Conf. Syst. Man. Cybern., 2016,
pp. 002 295–002 300.
[33] Q. Gao, X. Zhao et al., “Controlling of smart home system based on
brain-computer interface,” Technol. Health. Care., vol. 26, no. 5, pp.
769–783, 2018.
[34] A. Saboor, A. Rezeika et al., “SSVEP-based BCI in a smart home
scenario,” in Proc. Int. Work-Conf. Artif. Neural. Netw., 2017, pp. 474–
485.
[35] M. Adams, M. Benda et al., “Towards an SSVEP-BCI controlled smart
home,” in Proc. IEEE Int. Conf. Syst. Man. Cybern., 2019, pp. 2737–
2742.
[36] L. Shao, L. Zhang et al., “EEG-controlled wall-crawling cleaning robot
using SSVEP-based brain-computer interface,” J. Healthc. Eng., vol.
2020, 2020.
[37] M. Kołodziej, A. Majkowski et al., “Comparison of EEG signal
preprocessing methods for SSVEP recognition,” in Proc. 39th Int. Conf.
Telecommun. Signal.
IEEE, 2016, pp. 340–345.
[38] Q. Liu, Y. Jiao et al., “Efﬁcient representations of EEG signals for
SSVEP frequency recognition based on deep multiset CCA,” Neuro-
computing, vol. 378, pp. 36–44, 2020.
[39] Q. Liu, K. Chen et al., “Recent development of signal processing
algorithms for SSVEP-based brain computer interfaces,” J. Med. Biol.
Eng., vol. 34, no. 4, pp. 299–309, 2014.
[40] Q. Ai, Q. Liu et al., Advanced rehabilitative technology: neural
interfaces and devices.
Academic Press, 2018.
[41] H. Ji, B. Chen et al., “Functional source separation for EEG-fMRI
fusion: Application to steady-state visual evoked potentials,” Front.
Neurorobotics., vol. 13, p. 24, 2019.
[42] F.-B. Vialatte, M. Maurice et al., “Analyzing steady state visual evoked
potentials using blind source separation,” in Proc. 2nd. APSIPA. Annu.
Summit. Conf., 2010, pp. 578–582.
[43] I. Rejer and Ł. Cieszy´nski, “Independent component analysis for a low-
channel SSVEP-BCI,” Pattern. Anal. Appl., vol. 22, no. 1, pp. 47–62,
2019.
[44] Z. ˙Is¸can and V. V. Nikulin, “Steady state visual evoked potential
(SSVEP) based brain-computer interface (BCI) performance under
different perturbations,” PloS one, vol. 13, no. 1, p. e0191673, 2018.
[45] Z. Li, K. Liu et al., “Spatial fusion of maximum signal fraction
analysis for frequency recognition in SSVEP-based BCI,” Biomed.
Signal. Proces., vol. 61, p. 102042, 2020.
[46] L. Jiang, Y. Wang et al., “A four-class phase-coded SSVEP BCI at
60hz using refresh rate,” in Proc. 41st Annu. Int. Conf. IEEE Eng.
Medicine. Biol. Soc. (EMBC).
IEEE, 2019, pp. 6331–6334.
[47] X. Mao, W. Li et al., “Improve the classiﬁcation efﬁciency of high-
frequency phase-tagged SSVEP by a rRecursive Bayesian-based ap-
proach,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 28, no. 3, pp.
561–572, 2020.
[48] S.-C. Chen, Y.-J. Chen et al., “A single-channel SSVEP-based BCI
with a fuzzy feature threshold algorithm in a maze game,” Int. J. Fuzzy.
Syst., vol. 19, no. 2, pp. 553–565, 2017.
[49] Y.-J. Chen, A. R. A. See et al., “SSVEP-based BCI classiﬁcation using
power cepstrum analysis,” Electron. Lett., vol. 50, no. 10, pp. 735–737,
2014.
[50] R. Ortner, B. Z. Allison et al., “An SSVEP BCI to control a hand or-
thosis for persons with tetraplegia,” IEEE Trans. Neural Syst. Rehabil.
Eng., vol. 19, no. 1, pp. 1–5, 2010.
[51] X. Huang, J. Xu et al., “A novel instantaneous phase detection ap-
proach and its application in SSVEP-based brain-computer interfaces,”
Sensors, vol. 18, no. 12, p. 4334, 2018.
[52] V. Pukhova, E. Gorelova et al., “Time-frequency representation of
signals by wavelet transform,” in Proc. IEEE Conf. Russian. Young.
Researchers. Elect. Electron. Eng., 2017, pp. 715–718.
[53] I. Rejer, “Wavelet transform in detection of the subject speciﬁc frequen-
cies for SSVEP-based BCI,” in Proc. Int. Multi-Conf. Adv. Comput.
Syst., 2016, pp. 146–155.
[54] H. Heidari and Z. Einalou, “SSVEP extraction applying wavelet
transform and decision tree with bays classiﬁcation,” International
Clinical Neuroscience Journal, vol. 4, no. 3, pp. 91–97, 2017.
[55] Y. Bian, H. Li et al., “Research on steady state visual evoked potentials
based on wavelet packet technology for brain-computer interface,”
Procedia Engineering, vol. 15, pp. 2629–2633, 2011.
[56] R. K. Singla, A. Khosla et al., “Inﬂuence of stimuli colour on feature
classiﬁcation for BCI applications,” Int. J. Biomed. Eng. Technol.,
vol. 15, no. 1, pp. 82–93, 2014.
[57] C.-H. Wu, H.-C. Chang et al., “Frequency recognition in an SSVEP-
based brain computer interface using empirical mode decomposition
and reﬁned generalized zero-crossing,” J. Neurosci. Methods., vol. 196,
no. 1, pp. 170–181, 2011.

13
[58] L. Huang, X. Huang et al., “Empirical mode decomposition improves
detection of SSVEP,” in Proc. 35th Annu. Int. Conf. IEEE Eng.
Medicine. Biol. Soc. (EMBC).
IEEE, 2013, pp. 3901–3904.
[59] N. E. Huang, Z. Shen et al., “The empirical mode decomposition
and the hilbert spectrum for nonlinear and non-stationary time series
analysis,” P. Roy. Soc. Lond. A-Math. Phy. Eng. Sci., vol. 454, no. 1971,
pp. 903–995, 1998.
[60] R. M. Tello, S. M. T. M¨uller et al., “Comparison of new techniques
based on EMD for control of a SSVEP-BCI,” in Proc. IEEE 23rd Int.
Symp. Ind. Electron., 2014, pp. 992–997.
[61] W. Liu, L. Zhang et al., “A method for recognizing high-frequency
steady-state visual evoked potential based on empirical modal decom-
position and canonical correlation analysis,” in Proc. IEEE 3rd Inf.
Technol. Netw. Electron. Automat. Control. Conf., 2019, pp. 774–778.
[62] P.-L. Lee, H.-C. Chang et al., “A brain-wave-actuated small robot car
using ensemble empirical mode decomposition-based approach,” IEEE
Trans. Syst., Man, Cybern. A, vol. 42, no. 5, pp. 1053–1064, 2012.
[63] Y.-F. Chen, K. Atal et al., “A new multivariate empirical mode
decomposition method for improving the performance of SSVEP-based
brain–computer interface,” J. Neural Eng., vol. 14, no. 4, p. 046028,
2017.
[64] L. Zhao, P. Yuan et al., “Research on SSVEP feature extraction based
on HHT,” in Proc. 7th Int. Conf. Fuzzy. Syst. Knowl. Discovery., vol. 5.
IEEE, 2010, pp. 2220–2223.
[65] I. Volosyak, “SSVEP-based Bremen–BCI interface boosting informa-
tion transfer rates,” J. Neural Eng., vol. 8, no. 3, p. 036020, 2011.
[66] H. Cecotti, “A self-paced and calibration-less SSVEP-based brain–
computer interface speller,” IEEE Trans. Neural Syst. Rehabil. Eng.,
vol. 18, no. 2, pp. 127–133, 2010.
[67] G. K. Kumar and M. R. Reddy, “Constructing an exactly periodic
subspace for enhancing SSVEP based BCI,” Adv. Eng. Inform., vol. 44,
p. 101046, 2020.
[68] S. Parini, L. Maggi et al., “A robust and self-paced BCI system based
on a four class SSVEP paradigm: algorithms and protocols for a high-
transfer-rate direct brain communication,” Comput. Intel. Neurosc., vol.
2009, 2009.
[69] Z. Lin, C. Zhang et al., “Frequency recognition based on canonical
correlation analysis for SSVEP-based BCIs,” IEEE Trans. Biomed.
Eng., vol. 53, no. 12, pp. 2610–2614, 2006.
[70] B. Thompson, “Canonical correlation analysis,” Encyclopedia of statis-
tics in behavioral science, 2005.
[71] Y. Zhang, G. Zhou et al., “Multiway canonical correlation analysis for
frequency components recognition in SSVEP-based BCIs,” in Proc.
Int. Conf. Neural. Inf. Process., 2011, pp. 287–295.
[72] Y. Zhang, G. Zhou et al., “L1-regularized multiway canonical correla-
tion analysis for SSVEP-based BCI,” IEEE Trans. Neural Syst. Rehabil.
Eng., vol. 21, no. 6, pp. 887–896, 2013.
[73] J. Pan, X. Gao et al., “Enhancing the classiﬁcation accuracy of steady-
state visual evoked potential-based brain–computer interfaces using
phase constrained canonical correlation analysis,” J. Neural Eng.,
vol. 8, no. 3, p. 036027, 2011.
[74] Y. Zhang, G. Zhou et al., “Frequency recognition in SSVEP-based
BCI using multiset canonical correlation analysis,” Int. J. Neural Syst.,
vol. 24, no. 04, p. 1450013, 2014.
[75] A. Ziafati and A. Maleki, “Fuzzy ensemble system for SSVEP stimu-
lation frequency detection using the MLR and MsetCCA,” J. Neurosci.
Methods., p. 108686, 2020.
[76] X. Chen, Y. Wang et al., “Filter bank canonical correlation analysis for
implementing a high-speed SSVEP-based brain–computer interface,” J.
Neural Eng., vol. 12, no. 4, p. 046008, 2015.
[77] S. Ge, Y. Jiang et al., “Training-free steady-state visual evoked potential
brain–computer interface based on ﬁlter bank canonical correlation
analysis and spatiotemporal beamforming decoding,” IEEE Trans.
Neural Syst. Rehabil. Eng., vol. 27, no. 9, pp. 1714–1723, 2019.
[78] G. Bin, X. Gao et al., “A high-speed BCI based on code modulation
VEP,” J. Neural Eng., vol. 8, no. 2, p. 025015, 2011.
[79] M. Nakanishi, Y. Wang et al., “A high-speed brain speller using steady-
state visual evoked potentials,” Int. J. Neural Syst., vol. 24, no. 06, p.
1450019, 2014.
[80] Y. Wang, M. Nakanishi et al., “Enhancing detection of steady-state
visual evoked potentials using individual training data,” in Proc. 36th
Ann. Int. Conf. IEEE Eng. Med. Biol. Soc., 2014, pp. 3037–3040.
[81] S. Akaho, “A kernel method for canonical correlation analysis,” arXiv
preprint cs/0609071, 2006.
[82] Z. M. Zhang and Z. D. Deng, “A kernel canonical correlation analysis
based idle-state detection method for SSVEP-based brain-computer
interfaces,” in Advanced Materials Research, vol. 341, 2012, pp. 634–
640.
[83] G. Andrew, R. Arora et al., “Deep canonical correlation analysis,” in
Proc. Int. Conf. Mach. Learn., 2013, pp. 1247–1255.
[84] Y. Zhang, E. Yin et al., “Two-stage frequency recognition method based
on correlated component analysis for SSVEP-based BCI,” IEEE Trans.
Neural Syst. Rehabil. Eng., vol. 26, no. 7, pp. 1314–1323, 2018.
[85] Y. Zhang, D. Guo et al., “Correlated component analysis for enhancing
the performance of SSVEP-based brain-computer interface,” IEEE
Trans. Neural Syst. Rehabil. Eng., vol. 26, no. 5, pp. 948–956, 2018.
[86] P. F. Diez, V. A. Mut et al., “Asynchronous BCI control using high-
frequency SSVEP,” J. Neuroeng. Rehabil., vol. 8, no. 1, p. 39, 2011.
[87] C. Liguori, A. Paolillo et al., “Estimation of signal parameters in
the frequency domain in the presence of harmonic interference: A
comparative analysis,” IEEE Instrum. Meas. Mag., vol. 55, no. 2, pp.
562–569, 2006.
[88] C. Offelli and D. Petri, “A frequency-domain procedure for accurate
real-time signal parameter measurement,” IEEE Trans. Instrum. Meas.,
vol. 39, no. 2, pp. 363–368, 1990.
[89] D. Agrez, “Weighted multipoint interpolated DFT to improve amplitude
estimation of multifrequency signal,” IEEE Instrum. Meas. Mag.,
vol. 51, no. 2, pp. 287–292, 2002.
[90] M. Novotny, D. Slepicka et al., “Uncertainty analysis of the RMS value
and phase in the frequency domain by noncoherent sampling,” IEEE
Instrum. Meas. Mag., vol. 56, no. 3, pp. 983–989, 2007.
[91] G. K. Kumar and M. R. Reddy, “Latent common source extraction via a
generalized canonical correlation framework for frequency recognition
in SSVEP based brain–computer interfaces,” J. Neural Eng., vol. 16,
no. 4, p. 046004, 2019.
[92] Y. Wang, R. Wang et al., “A practical VEP-based brain-computer
interface,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 14, no. 2, pp.
234–240, 2006.
[93] G. Bin, X. Gao et al., “An online multi-channel SSVEP-based brain–
computer interface using a canonical correlation analysis method,” J.
Neural Eng., vol. 6, no. 4, p. 046002, 2009.
[94] I. Rejer, “Multichannel spatial ﬁlters for enhancing SSVEP detection,”
in Proc. Int. Multi-Conf. Adv. Comput. Syst.
Springer, 2018, pp. 481–
492.
[95] O. Falzon, K. Camilleri et al., “Complex-valued spatial ﬁlters for
SSVEP-based BCIs with phase coding,” IEEE Trans. Biomed. Eng.,
vol. 59, no. 9, pp. 2486–2495, 2012.
[96] A. Cichocki, R. Zdunek et al., Nonnegative matrix and tensor factor-
izations: applications to exploratory multi-way data analysis and blind
source separation.
John Wiley & Sons, 2009.
[97] T.-K. Kim and R. Cipolla, “Canonical correlation analysis of video
volume tensors for action categorization and detection,” IEEE Trans.
Pattern Anal. Mach. Intell., vol. 31, no. 8, pp. 1415–1428, 2008.
[98] J. J. Wilson and R. Palaniappan, “Augmenting a SSVEP BCI
through single cycle analysis and phase weighting,” in Proc. 4th Int.
IEEE/EMBS Conf. Neural. Eng., pp. 371–374.
[99] M. John and T. Picton, “Human auditory steady-state responses to
amplitude-modulated tones: phase and latency measurements,” Hear.
Res., vol. 141, no. 1-2, pp. 57–79, 2000.
[100] M. Nakanishi, Y. Wang et al., “A comparison study of canonical
correlation analysis based methods for detecting steady-state visual
evoked potentials,” PloS one, vol. 10, no. 10, 2015.
[101] K. K. GR and R. Reddy, “Designing a sum of squared correlations
framework for enhancing SSVEP-based BCIs,” IEEE Trans. Neural
Syst. Rehabil. Eng., vol. 27, no. 10, pp. 2044–2050, 2019.
[102] J. P. Dmochowski, P. Sajda et al., “Correlated components of ongo-
ing EEG point to emotionally laden attention–a possible marker of
engagement?” Front. Hum. Neurosci., vol. 6, p. 112, 2012.
[103] R. Srinivasan, F. A. Bibi et al., “Steady-state visual evoked potentials:
distributed local sources and wave-like dynamics are sensitive to ﬂicker
frequency,” Brain. Topogr., vol. 18, no. 3, pp. 167–187, 2006.
[104] J. M. Ales and A. M. Norcia, “Assessing direction-speciﬁc adaptation
using the steady-state visual evoked potential: Results from EEG source
imaging,” J. Vision., vol. 9, no. 7, pp. 8–8, 2009.
[105] A. Delorme, T. Sejnowski et al., “Enhanced detection of artifacts in
EEG data using higher-order statistics and independent component
analysis,” NeuroImage, vol. 34, no. 4, pp. 1443–1449, 2007.
[106] T.-P. Jung, S. Makeig et al., “Removing electroencephalographic arti-
facts by blind source separation,” Psychophysiology, vol. 37, no. 2, pp.
163–178, 2000.
[107] H. Tanaka, T. Katura et al., “Task-related component analysis for
functional neuroimaging and application to near-infrared spectroscopy
data,” NeuroImage, vol. 64, pp. 308–327, 2013.

14
[108] H. Tanaka, T. Katura et al., “Task-related oxygenation and cerebral
blood volume changes estimated from nirs signals in motor and
cognitive tasks,” NeuroImage, vol. 94, pp. 107–119, 2014.
[109] S. F. Anindya, H. H. Rachmat et al., “A prototype of SSVEP-based
BCI for home appliances control,” in Proc. 1st Int. Conf. Biomed. Eng.
IEEE, 2016, pp. 1–6.
[110] S. N. Carvalho, T. B. Costa et al., “Comparative analysis of strategies
for feature extraction and classiﬁcation in SSVEP BCIs,” Biomed.
Signal. Proces., vol. 21, pp. 34–42, 2015.
[111] N.-S. Kwak, K.-R. M¨uller et al., “A convolutional neural network for
steady state visual evoked potential classiﬁcation under ambulatory
environment,” PloS one, vol. 12, no. 2, p. e0172578, 2017.
[112] S. Zavala, J. L´opez et al., “Review of steady state visually evoked
potential brain-computer interface applications: technological analysis
and classiﬁcation,” Journal of Engineering and Applied Sciences,
vol. 15, pp. 659–678, 2019.
[113] Z. Gao, T. Yuan et al., “A deep learning method for improving the
classiﬁcation accuracy of SSMVEP-based BCI,” IEEE Trans. Circuits
Syst. II, 2020.
[114] A. Ditthapron, N. Banluesombatkul et al., “Universal joint feature
extraction for P300 EEG classiﬁcation using multi-task autoencoder,”
IEEE Access, vol. 7, pp. 68 415–68 428, 2019.
[115] S. S. Embrandiri and M. R. Reddy, “Maximum contrastive networks for
multi-channel SSVEP detection,” in Proc. 7th Int. IEEE/EMBS Conf.
Neural. Eng.
IEEE, 2015, pp. 992–995.
[116] Z. Zhang, C. Wang et al., “Spectrum and phase adaptive CCA for
SSVEP-based brain computer interface,” in Proc. IEEE 40th Ann. Int.
Conf. IEEE Eng. Med. Biol. Soc., 2018, pp. 311–314.
[117] J. Xie, G. Xu et al., “Effects of mental load and fatigue on steady-state
evoked potential based brain computer interface tasks: a comparison
of periodic ﬂickering and motion-reversal based visual attention,” PloS
one, vol. 11, no. 9, 2016.
[118] T. Cao, F. Wan et al., “Objective evaluation of fatigue by EEG spectral
analysis in steady-state visual evoked potential-based brain-computer
interfaces,” Biomed. Eng. Online., vol. 13, no. 1, p. 28, 2014.
[119] Z. Gao, K. Zhang et al., “An adaptive optimal-Kernel time-frequency
representation-based complex network method for characterizing fa-
tigued behavior using the SSVEP-based BCI system,” Knowl-Based.
Syst., vol. 152, pp. 163–171, 2018.
[120] Y. Zhang, J. Yang et al., “A research about the mental fatigue of using
an intelligent artiﬁcial limb based on functional near infrared spectrum
technique,” in Proc. IEEE Int. Conf. Intell. Saf. Robot., 2018, pp. 500–
503.
[121] H. Hu, J. Zhao et al., “Telepresence control of humanoid robot via
high-frequency phase-tagged SSVEP stimuli,” in Proc. IEEE 14th Int.
Workshop. Adv. Motion. Control.
IEEE, 2016, pp. 214–219.
[122] U. Talukdar, S. M. Hazarika et al., “Adaptation of common spatial
patterns based on mental fatigue for motor-imagery BCI,” Biomed.
Signal. Proces., vol. 58, p. 101829, 2020.
[123] K.-J. Chiang, C.-S. Wei et al., “Cross-subject transfer learning improves
the practicality of real-world applications of brain-computer interfaces,”
in Proc. 9th Int. IEEE/EMBS Conf. Neural. Eng., 2019, pp. 424–427.
[124] P. Wang, J. Lu et al., “A review on transfer learning for brain-computer
interface classiﬁcation,” in Proc. IEEE 5th Int. Conf. Inf. Sci. Technol.,
2015, pp. 315–322.
[125] N. R. Waytowich, V. J. Lawhern et al., “Spectral transfer learning using
information geometry for a user-independent brain-computer interface,”
Front. Neurosci-Switz, vol. 10, p. 430, 2016.
[126] N. R. Waytowich, J. Faller et al., “Unsupervised adaptive transfer
learning for steady-state visual evoked potential brain-computer inter-
faces,” in Proc. IEEE Int. Conf. Syst. Man. Cybern., 2016, pp. 004 135–
004 140.
[127] H. Banville and T. Falk, “Recent advances and open challenges in
hybrid brain-computer interfacing: a technological review of non-
invasive human research,” Brain-Computer Interfaces, vol. 3, no. 1,
pp. 9–46, 2016.
[128] K.-S. Hong and M. J. Khan, “Hybrid brain–computer interface tech-
niques for improved classiﬁcation accuracy and increased number of
commands: a review,” Front. Neurorobotics., vol. 11, p. 35, 2017.
[129] Z. Wang, Y. Yu et al., “Towards a hybrid BCI gaming paradigm based
on motor imagery and SSVEP,” Int. J. Hum-Comput. Int., vol. 35, no. 3,
pp. 197–205, 2019.
[130] M. Wang, I. Daly et al., “A new hybrid BCI paradigm based on P300
and SSVEP,” J. Neurosci. Methods., vol. 244, pp. 16–25, 2015.
[131] S. Jalilpour, S. H. Sardouie et al., “A novel hybrid BCI speller based
on RSVP and SSVEP paradigm,” Comput. Meth. Prog. Bio., vol. 187,
p. 105326, 2020.
[132] L. Chu, J. Fern´andez-Vargas et al., “Inﬂuence of stimulus color on
steady state visual evoked potentials,” in Proc. Int. Conf. Intell. Auton.
Syst.
Springer, 2016, pp. 499–509.
[133] M. Jukiewicz and A. Cysewska-Sobusiak, “Stimuli design for SSVEP-
based brain computer-interface,” International Journal of Electronics
and Telecommunications, vol. 62, 2016.
[134] E. P. Zambalde et al., “SSVEP-based BCI with visual stimuli from LCD
screen applied for wheelchair control: ofﬂine and online investigations,”
2018.
[135] K. Sharma and S. Kar, “Extracting multiple commands from a single
SSVEP ﬂicker using eye-accommodation,” Biocybern. Biomed. Eng.,
vol. 39, no. 3, pp. 914–922, 2019.
[136] M. H. Chang, H. J. Baek et al., “An amplitude-modulated visual
stimulation for reducing eye fatigue in SSVEP-based brain–computer
interfaces,” Clin. Neurophysiol., vol. 125, no. 7, pp. 1380–1391, 2014.
[137] P. Autthasan, X. Du et al., “A single-channel consumer-grade EEG
device for brain–computer interface: enhancing detection of SSVEP
and its amplitude modulation,” IEEE Sensors Journal, vol. 20, no. 6,
pp. 3366–3378, 2019.
[138] R. Gulbinaite, D. H. Roozendaal et al., “Attention differentially mod-
ulates the amplitude of resonance frequencies in the visual cortex,”
NeuroImage, vol. 203, p. 116146, 2019.
[139] J. M. Egan, G. M. Loughnane et al., “A gaze independent hybrid-BCI
based on visual spatial attention,” J. Neural Eng., vol. 14, no. 4, p.
046006, 2017.
[140] M. Lopez-Gordo, F. Pelayo et al., “A high performance SSVEP-BCI
without gazing,” in Proc. Int. Joint. Conf. Neural. Netw.
IEEE, 2010,
pp. 1–5.
[141] R. M. Tello, S. M. M¨uller et al., “An independent-BCI based on SSVEP
using Figure-Ground Perception (FGP),” Biomed. Signal. Proces.,
vol. 26, pp. 69–79, 2016.
