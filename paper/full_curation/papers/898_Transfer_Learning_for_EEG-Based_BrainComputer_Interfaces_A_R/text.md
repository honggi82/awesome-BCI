arXiv:2004.06286v4  [cs.HC]  3 Jul 2020
1
Transfer Learning for EEG-Based Brain-Computer
Interfaces: A Review of Progress Made Since 2016
Dongrui Wu, Yifan Xu and Bao-Liang Lu
Abstract—A brain-computer interface (BCI) enables a user
to communicate with a computer directly using brain signals.
The most common non-invasive BCI modality, electroencephalo-
gram (EEG), is sensitive to noise/artifact and suffers between-
subject/within-subject non-stationarity. Therefore, it is difﬁcult to
build a generic pattern recognition model in an EEG-based BCI
system that is optimal for different subjects, during different
sessions, for different devices and tasks. Usually, a calibration
session is needed to collect some training data for a new subject,
which is time-consuming and user unfriendly. Transfer learning
(TL), which utilizes data or knowledge from similar or relevant
subjects/sessions/devices/tasks to facilitate learning for a new sub-
ject/session/device/task, is frequently used to reduce the amount
of calibration effort. This paper reviews journal publications on
TL approaches in EEG-based BCIs in the last few years, i.e.,
since 2016. Six paradigms and applications – motor imagery,
event-related potentials, steady-state visual evoked potentials,
affective BCIs, regression problems, and adversarial attacks –
are considered. For each paradigm/application, we group the
TL approaches into cross-subject/session, cross-device, and cross-
task settings and review them separately. Observations and
conclusions are made at the end of the paper, which may point
to future research directions.
Index Terms—Brain-computer interfaces, EEG, transfer learn-
ing, domain adaptation, affective BCI, adversarial attacks
I. INTRODUCTION
A brain-computer interface (BCI) enables a user to commu-
nicate with a computer using his/her brain signals directly [1],
[2]. The term was ﬁrst coined by Vidal in 1973 [3], although
it had been studied previously [4], [5]. BCIs were initially
proposed for disabled people [6], but their current application
scope has been extended to able-bodied users [7], in gaming
[8], emotion recognition [9], mental fatigue evaluation [10],
vigilance estimation [11], [12], etc.
There are generally three types of BCIs [13]:
1) Non-invasive BCIs, which use non-invasive brain signals
measured outside of the brain, e.g., electroencephalo-
grams (EEGs) and functional near-infrared spectroscopy
(fNIRS).
2) Invasive BCIs, which require surgery to implant sensor
arrays or electrodes within the grey matter under the
D. Wu and Y. Xu are with the Ministry of Education Key Laboratory of
Image Processing and Intelligent Control, School of Artiﬁcial Intelligence
and Automation, Huazhong University of Science and Technology, Wuhan
430074, China. Email: drwu@hust.edu.cn, yfxu@hust.edu.cn.
B.-L. Lu is with the Center for Brain-Like Computing and Machine Intel-
ligence, Department of Computer Science and Engineering, Key Laboratory
of Shanghai Education Commission for Intelligent Interaction and Cognitive
Engineering, Brain Science and Technology Research Center, and Qing Yuan
Research Institute, Shanghai Jiao Tong University, 800 Dong Chuan Road,
Shanghai 200240, China. Email: bllu@sjtu.edu.cn.
scalp to measure and decode brain signals (usually
spikes and local ﬁeld potentials).
3) Partially invasive (semi-invasive) BCIs, in which the
sensors are surgically implanted inside the skull but
outside the brain rather than within the grey matter.
This paper focuses on non-invasive BCIs, particularly EEG-
based BCIs, which are the most popular type of BCIs due to
their safety, low cost, and convenience.
A closed-loop EEG-based BCI system, shown in Fig. 1,
consists of the following components:
Fig. 1. Flowchart of a closed-loop EEG-based BCI system.
1) Signal acquisition [14], which uses an EEG device to
collect EEG signals from the scalp. In the early days,
EEG devices used wired connections and gel to increase
conductivity. Currently, wireless connections and dry
electrodes are becoming increasingly popular.
2) Signal processing [15], which usually includes tempo-
ral ﬁltering and spatial ﬁltering. The former typically
uses a bandpass ﬁlter to reduce interference and noise,
such as muscle artefacts, eye blinks, and DC drift.
The latter combines different EEG channels to increase
the signal-to-noise ratio. Popular spatial ﬁlters include
common spatial patterns (CSP) [16], independent com-
ponent analysis (ICA) [17], blind source separation [18],
xDAWN [19], etc.
3) Feature extraction, for which time domain, frequency
domain [20], time-frequency domain, Riemannian space
[21] and/or functional brain connectivity [22] features
could be used.
4) Pattern recognition. Depending on the application, a
classiﬁer or regression model is used.
5) Controller, which outputs a command to control an
external device, e.g., a wheelchair or a drone, or to alter
the behaviour of an environment, e.g., the difﬁculty level

2
of a video game. A controller may not be needed in
certain applications, e.g., BCI spellers.
When deep learning is used, feature extraction and pattern
recognition can be integrated into a single neural network,
and both components are optimized simultaneously and auto-
matically.
EEG signals are weak, easily contaminated by interference
and noise, non-stationary for the same subject, and varying
across different subjects and sessions. Therefore, it is challeng-
ing to build a universal machine learning model in an EEG-
based BCI system that is optimal for different subjects, during
different sessions, for different devices and tasks. Usually, a
calibration session is needed to collect some training data for
a new subject, which is time-consuming and user unfriendly.
Therefore, reducing this subject-speciﬁc calibration is critical
to the market success of EEG-based BCIs.
Different machine learning techniques, e.g., transfer learn-
ing (TL) [23] and active learning [24], have been used for
this purpose. Among them, TL is particularly promising
because it can utilize data or knowledge from similar or
relevant subjects/sessions/devices/tasks to facilitate learning
for a new subject/session/device/task. Moreover, it may also be
integrated with other machine learning techniques, e.g., active
learning [25], [26], for even better performance. This paper
focuses on TL in EEG-based BCIs.
There are three classic classiﬁcation paradigms in EEG-
based BCIs, which will be considered in this paper:
1) Motor imagery (MI) [27], which can modify neuronal
activity in primary sensorimotor areas, is similar to a real
executed movement. As different MIs affect different
regions of the brain, e.g., the left (right) hemisphere for
right-hand (left-hand) MI and centre for feet MI, a BCI
can decode MI from the EEG signals and map it to a
speciﬁc command.
2) Event-related potentials (ERP) [28], [29], which are
any stereotyped EEG responses to a visual, audio, or
tactile stimulus. The most frequently used ERP is P300
[30], which occurs approximately 300 ms after a rare
stimulus.
3) Steady-state visual evoked potentials (SSVEP) [31]. The
EEG oscillates at the same (or multiples of) frequency
of the visual stimulus at a speciﬁc frequency, usually
between 3.5 and 75 Hz [32]. This paradigm is frequently
used in BCI spellers [33], as it can achieve a very high
information transfer rate.
EEG-based affective BCIs (aBCIs) [34]–[37], which detect
affective states (moods, emotions) from EEGs and use them in
BCIs, have become an emerging research area. There are also
some interesting regression problems in EEG-based BCIs, e.g.,
driver drowsiness estimation [38]–[40] and user reaction time
estimation [41]. Additionally, recent research [42], [43] has
shown that BCIs also suffer from adversarial attacks, where
deliberately designed tiny perturbations are added to benign
EEG trials to fool the machine learning model and cause
dramatic performance degradation. This paper also considers
aBCIs, regression problems, and adversarial attacks of EEG-
based BCIs.
Although TL has been applied in all of the above EEG-
based BCI paradigms and applications, to our knowledge, there
is no comprehensive and up-to-date review on it. Wang et al.
[44] performed a short review in a conference paper in 2015.
Jayaram et al. [45] gave a brief review in 2016, considering
only cross-subject and cross-session transfers. Lotte et al. [46]
provided a comprehensive review of classiﬁcation algorithms
for EEG-based BCIs between 2007 and 2017. Again, they only
considered cross-subject and cross-session transfers. Azab
et al. [47] performed a review of four categories of TL
approaches in BCIs in 2018: 1) instance-based TL; 2) feature-
representation TL; 3) classiﬁer-based TL; and 4) relational-
based TL.
However, all the aforementioned reviews considered only
cross-subject and cross-session TL of the three classic
paradigms of EEG-based BCIs (MI, ERP and SSVEP) but did
not mention the more challenging cross-device and cross-task
transfers, aBCIs, regression problems and adversarial attacks.
To ﬁll these gaps and to avoid overlapping too much with
previous reviews, this paper reviews journal publications of TL
approaches in EEG-based BCIs in the last few years, i.e., since
2016. Six paradigms and applications are considered: MI, ERP,
SSVEP, aBCI, regression problems, and adversarial attacks.
For each paradigm/application, we group the TL approaches
into cross-subject/session (because these two concepts are
essentially the same), cross-device, and cross-task settings and
review them separately, unless no TL approaches have been
proposed for that category. Some TL approaches may cover
more than two categories, e.g., both cross-subject and cross-
device transfers were considered. In this case, we introduce
them in the more challenging category, e.g., cross-device TL.
When there are multiple TL approaches in each category, we
generally introduce them according to the years in which they
were proposed, unless there are intrinsic connections among
several approaches.
The remainder of this paper is organized as follows: Sec-
tion II brieﬂy introduces some basic concepts of TL. Sec-
tions III-VIII review TL approaches in MI, ERP, SSVEP, aB-
CIs, regression problems, and adversarial attacks, respectively.
Section IX makes observations and conclusions, which may
point to some future research directions.
II. TL CONCEPTS AND SCENARIOS
This section introduces the basic deﬁnitions of TL, some
related concepts, e.g., domain adaptation and covariate shift,
and different TL scenarios in EEG-based BCIs.
In machine learning, a feature vector is usually denoted by
a bold symbol x. To emphasize that each EEG trial is a 2D
matrix, this paper denotes a trial by X ∈RE×T , where E is
the number of electrodes and T is the number of time domain
samples. Of course, X can also be converted into a feature
vector x.
A. TL Concepts
Deﬁnition 1: A domain [23], [48] D consists of a feature
space X and its associated marginal probability distribution
P(X), i.e., D = {X, P(X)}, where X ∈X.

3
A source domain Ds and a target domain Dt are different if
they have different feature spaces, i.e., Xs̸ = Xt, and/or differ-
ent marginal probability distributions, i.e., Ps(X)̸ = Pt(X).
Deﬁnition 2: Given a domain D, a task [23], [48] T consists
of a label space Y and a prediction function f(X), i.e., T =
{Y, f(X)}.
Let y ∈Y. Then, f(X) = P(y|X) is the conditional
probability distribution. Two tasks Ts and Tt are different if
they have different label spaces, i.e., Ys̸ = Yt, and/or different
conditional probability distributions, i.e., Ps(y|X)̸ = Pt(y|X).
Deﬁnition 3: Given a source domain Ds = {(Xi
s, yi
s)}N
i=1
and
a
target
domain
Dt
with
Nl
labelled
samples
{(Xi
t, yi
t)}Nl
i=1 and Nu unlabelled samples {Xi
t}Nl+Nu
i=Nl+1, trans-
fer learning (TL) aims to learn a target prediction function
f : Xt 7→yt with low expected error on Dt under the general
assumptions that Xs̸ = Xt, Ys̸ = Yt, Ps(X)̸ = Pt(X), and/or
Ps(y|X)̸ = Pt(y|X).
In inductive TL, the target domain has some labelled
samples, i.e., Nl > 0. For most inductive TL scenarios
in BCIs, the source domain samples are labelled, but they
could also be unlabelled. When the source domain samples
are labelled, inductive TL is similar to multi-task learning
[49]. The difference is that multi-task learning tries to learn
a model for every domain simultaneously, whereas inductive
TL focuses only on the target domain. In transductive TL, the
source domain samples are all labelled, but the target domain
samples are all unlabelled, i.e., Nl = 0. In unsupervised TL,
no samples in either domain are labelled.
Domain adaptation is a special case of TL, or more specif-
ically, transductive TL:
Deﬁnition 4: Given a source domain Ds and a target domain
Dt, domain adaptation aims to learn a target prediction
function f : xt 7→yt with low expected error on Dt, under the
assumptions that Xs = Xt and Ys = Yt, but Ps(X)̸ = Pt(X)
and/or Ps(y|X)̸ = Pt(y|X).
Covariate shift is a special and simpler case of domain
adaptation:
Deﬁnition 5: Given a source domain Ds and a target
domain Dt, covariate shift occurs when Xs = Xt, Ys = Yt,
Ps(y|X) = Pt(y|X), but Ps(X)̸ = Pt(X).
B. TL Scenarios
According to the variations between the source and the
target domains, there can be different TL scenarios in EEG-
based BCIs:
1) Cross-subject TL. Data from other subjects (the source
domains) are used to facilitate the calibration for a new
subject (the target domain). Usually, the task and EEG
device are the same across subjects.
2) Cross-session TL. Data from previous sessions (the
source domains) are used to facilitate the calibration of
a new session (the target domain). For example, data
from previous days are used in the current calibration.
Usually, the subject, task and EEG device are the same
across sessions.
3) Cross-device TL. Data from one EEG device (the source
domain), is used to facilitate the calibration of a new
device (the target domain). Usually, the task and subject
are the same across EEG devices.
4) Cross-task TL. Labelled data from other similar or
relevant tasks (the source domains) is used to facilitate
the calibration for a new task (the target domain). For
example, data from left- and right-hand MI are used
in the calibration of feet and tongue MI. Usually, the
subject and EEG device are the same across tasks.
Since cross-subject TL and cross-session TL are essentially
the same, this paper combines them into one category: cross-
subject/session TL. Generally, cross-device TL and cross-task
TL are more challenging than cross-subject/session TL; hence,
they were less studied in the literature.
The above simple TL scenarios could also be mixed to form
more complex TL scenarios, e.g., cross-subject and cross-
device TL [26], cross-subject and cross-task TL [50], etc.
III. TL IN MI-BASED BCIS
This section reviews recent progress in TL for MI-based
BCIs. Many of them used the BCI Competition datasets1.
Assume there are S source domains, and the s-th source
domain has Ns EEG trials. The n-th trial of the s-th source
domain is denoted by Xn
s ∈RE×T , where E is the number
of electrodes and T is the number of time domain samples
from each channel. The corresponding covariance matrix is
Cn
s ∈RE×E, which is symmetric and positive deﬁnite (SPD)
and lies on a Riemannian manifold. For binary classiﬁcation,
the label for Xn
s is yn
s ∈{−1, 1}. The n-th EEG trial in the
target domain is denoted by Xn
t , and the covariance matrix
is denoted by Cn
t . These notations are used throughout the
paper.
A. Cross-Subject/Session Transfer
Dai et al. [51] proposed the transfer kernel common spatial
patterns (TKCSP) method, which integrates kernel common
spatial patterns (KCSP) [52] and transfer kernel learning
(TKL) [53] for EEG trial spatial ﬁltering in cross-subject
MI classiﬁcation. It ﬁrst computes a domain-invariant kernel
by TKL and then uses it in the KCSP approach, which
further ﬁnds the components with the largest energy difference
between two classes. Note that TL was used in EEG signal
processing (spatial ﬁltering) instead of classiﬁcation.
Jayaram et al. [45] proposed a multi-task learning frame-
work for cross-subject/session transfers, which does not need
any labelled data in the target domain. The linear decision rule
is y = sign(µT
αXµw), where µα ∈RC×1 are the channel
weights and µw ∈RT ×1 are the feature weights. µα and µw
are obtained by minimizing
min
αs,ws
"
1
λ
S
X
s=1
Ns
X
n=1
αT
s Xn
s ws −yn
s
2
+
S
X
s=1
Ω(ws; µw, Σw) +
S
X
s=1
Ω(αs; µα, Σα)
#
,
(1)
1http://www.bbci.de/competition/

4
where αs ∈RC×1 are the channel weights for the s-th
source subject, ws ∈RT ×1 are the feature weights, λ is
a hyperparameter, and Ω(ws; µw, Σw) is the negative log
prior probability of ws given the Gaussian distribution pa-
rameterized by (µw, Σw). µw and Σw (µα and Σα) are the
mean vector and covariance matrix of {ws}S
s=1 ({αs}S
s=1),
respectively.
In (1), the ﬁrst term requires αs and ws to work well
for the s-th source subject; the second term ensures that the
divergence of ws from the shared (µw, Σw) is small, i.e., all
the source subjects should have similar ws values; and the
third term ensures that the divergence of αs from the shared
(µα, Σα) is small. µα and µw can be viewed as the subject-
invariant characteristics of stimulus prediction and hence used
directly by a new subject. Jayaram et al. demonstrated that
their approach worked well on cross-subject transfers in MI
classiﬁcation and cross-session transfers for one patient with
amyotrophic lateral sclerosis.
Azab et al. [54] proposed weighted TL for cross-subject
transfers in MI classiﬁcation as an improvement of the above
approach. They assumed that each source subject has plenty
of labelled samples, whereas the target subject has only a
few labelled samples. They ﬁrst trained a logistic regression
classiﬁer for each source subject by using a cross-entropy
loss function with an L2 regularization term. Then, a logistic
regression classiﬁer for the target subject was trained so that
the cross-entropy loss of the few labelled samples in the
target domain is minimized, and its parameters are close to
those of the source subjects. The mean vector and covariance
matrix of the classiﬁer parameters in the source domains were
computed in a similar way to that in [45], except that for each
source domain, a weight determined by the Kullback-Leibler
divergence between it and the target domain was used.
Hossain et al. [55] proposed an ensemble learning approach
for cross-subject transfers in multi-class MI classiﬁcation. Four
base classiﬁers were used, all constructed using TL and active
learning: 1) multi-class direct transfer with active learning
(mDTAL), a multi-class extension of the active TL approach
proposed in [56]; 2) multi-class aligned instance transfer
with active learning, which is similar to mDTAL except that
only the source domain samples correctly classiﬁed by the
corresponding classiﬁer are transferred; 3) most informative
and aligned instances transfer with active learning, which
transfers only the source domain samples correctly classiﬁed
by its classiﬁers and near the decision boundary (i.e., the
most informative samples); and 4) most informative instances
transfer with active learning, which transfers only source
domain samples close to the decision boundary. The four
base learners were ﬁnally stacked to achieve a more robust
performance.
Since the covariance matrices of EEG trials are SPD and
lie on a Riemannian manifold instead of in Euclidean space,
Riemannian approaches [21] have become popular in EEG-
based BCIs. Different TL approaches have also been proposed
recently.
Zanini et al. [57] proposed a Riemannian alignment (RA)
approach to centre the EEG covariance matrices {Cn
k }Nk
n=1 in
the k-th domain with respect to a reference covariance matrix
Rk speciﬁc to that domain. More speciﬁcally, RA computes
ﬁrst the covariance matrices of some resting trials in the k-
th domain, in which the subject is not performing any task,
and then calculates their Riemannian mean Rk. Rk is next
used as the reference matrix to reduce the inter-subject/session
variation:
eCn
k = R
−1
2
k
Cn
k R
−1
2
k
,
(2)
where eCn
k is the aligned covariance matrix for Cn
k . Equation
(2) centres the reference state of different subjects/sessions at
the identity matrix. In MI, the resting state is the time window
during which the subject is not performing any task, e.g., the
transition window between two MI tasks. In ERP, the non-
target stimuli are used as the resting state, requiring that some
labelled trials in the target domain must be known. Zanini et al.
also proposed improvements to the minimum distance to the
Riemannian mean (MDRM) [58] classiﬁer and demonstrated
the effectiveness of RA and the improved MDRM in both MI
and ERP classiﬁcations.
Yair et al. [59] proposed a domain adaptation approach
using the analytic expression of parallel transport (PT) on
the cone manifold of SPD matrices. The goal was to ﬁnd
a common tangent space such that the mappings of Ct and
Cs are aligned. It ﬁrst computes the Riemannian mean Rk of
the k-th domain and then the Riemannian mean ˆR of all Rk.
Then, each Rk is moved to ˆR by PT ΓRk→ˆ
R, and Cn
k , the
n-th covariance matrix in the k-th domain, is projected to
Log

ˆR−1
2 ΓRk→ˆ
R (Cn
k ) ˆR−1
2

= Log

R
−1
2
k
Cn
k R
−1
2
k

. (3)
After the projection step, the covariance matrices in different
domains are mapped to the same tangent space, so a classiﬁer
built in a source domain can be directly applied to the
target domain. Equation (3) is essentially identical to RA in
(2), except that (3) works in the tangent space, whereas (2)
works in the Riemannian space. Yair et al. demonstrated the
effectiveness of PT in cross-subject MI classiﬁcation, sleep
stage classiﬁcation, and mental arithmetic identiﬁcation.
To make RA more ﬂexible, faster, and completely unsu-
pervised, He and Wu [60] proposed a Euclidean alignment
(EA) approach to align EEG trials from different subjects in
Euclidean space. Mathematically, for the k-th domain, EA
computes the reference matrix Rk =
1
N
PN
n=1 Xn
k (Xn
k )T,
i.e., Rk is the arithmetic mean of all covariance matrices in
the k-th domain (it can also be the Riemannian mean, which
is more computationally intensive than the arithmetic mean),
then performs the alignment by e
Xn
k = R
−1
2
k
Xn
k . After EA, the
mean covariance matrices of all domains become the identity
matrix. Both Euclidean space and Riemannian space feature
extraction and classiﬁcation approaches can then be applied
to e
Xn
k . EA can be viewed as a generalization of Yair et al.’s
parallel transport approach because the computation of Rk in
EA is more ﬂexible, and both Euclidean and Riemannian space
classiﬁers can be used after EA. He and Wu demonstrated that
EA outperformed RA in both MI and ERP classiﬁcations in
both ofﬂine and simulated online applications.
Rodrigues et al. [61] proposed Riemannian Procrustes anal-
ysis (RPA) to accommodate covariant shifts in EEG-based

5
BCIs. It is semi-supervised and requires at least one labelled
sample from each target domain class. RPA ﬁrst matches
the statistical distributions of the covariance matrices of the
EEG trials from different domains, using simple geometrical
transformations, namely, translation, scaling, and rotation, in
sequence. Then, the labelled and transformed data from both
domains are concatenated to train a classiﬁer, which is next ap-
plied to the transformed and unlabelled target domain samples.
Mathematically, it transforms each target domain covariance
matrix Cn
t into
eCn
t = M
1
2
s
h
U T 
f
M
−1
2
t
Cn
t f
M
−1
2
t
p
U
i
M
1
2
s ,
(4)
where
• f
M
−1
2
t
is the geometric mean of the labelled target domain
samples, which centres the target domain covariance
matrices at the identity matrix.
• p = (d/ ˜d)
1
2 stretches the target domain covariance
matrices so that they have the same dispersion as the
source domain, in which d and ˜d are the dispersions
around the geometric mean of the source domain and
the target domain, respectively.
• U is an orthogonal rotation matrix to be optimized, which
minimizes the distance between the class means of the
source domain and the translated and stretched target
domain.
• M
−1
2
s
is the geometric mean of the labelled source
domain samples, which ensures that the geometric mean
of eCn
t is the same as that in the source domain.
Note that the class label information is only needed in com-
puting U. Although f
M
−1
2
t
, p and M
−1
2
s
are also computed
from the labeled samples, they do not need the speciﬁc class
labels.
Clearly, RPA is a generalization of RA. Rodrigues et al.
[61] showed that RPA can achieve promising results in cross-
subject MI, ERP and SSVEP classiﬁcation.
Recently, Zhang and Wu [62] proposed a manifold embed-
ded knowledge transfer (MEKT) approach, which ﬁrst aligns
the covariance matrices of the EEG trials in the Riemannian
manifold, extracts features in the tangent space, and then per-
forms domain adaptation by minimizing the joint probability
distribution shift between the source and the target domains
while preserving their geometric structures. More speciﬁcally,
it consists of the following three steps [62]:
1) Covariance matrix centroid alignment (CA). Align the
centroid of the covariance matrices in each domain,
i.e., eCn
s
= R
−1
2
s
Cn
s R
−1
2
s
and eCn
t
= R
−1
2
t
Cn
t R
−f 1
2
t
,
where Rs (Rt) can be the Riemannian mean, the Eu-
clidean mean, or the Log-Euclidean mean of all Cn
s
(Cn
t ). This is essentially a generalization of RA [57].
The marginal probability distributions from different
domains are brought together after CA.
2) Tangent space feature extraction. Map and assemble all
eCn
s ( eCn
t ) into a tangent space super matrix e
Xs ∈Rd×Ns
( e
Xt ∈Rd×Nt), where d = E(E + 1)/2 is the dimen-
sionality of the tangent space features.
3) Mapping matrices identiﬁcation. Find the projection
matrices A ∈Rd×p and B ∈Rd×p, where p ≪d is the
dimensionality of the shared subspace, such that AT e
Xs
and BT e
Xt are similar.
After MEKT, a classiﬁer can be trained on (AT e
Xs, ys) and
applied to BT e
Xt to estimate their labels.
MEKT can cope with one or more source domains and still
be efﬁcient. Zhang and Wu [62] also used domain transferabil-
ity estimation (DTE) to identify the most beneﬁcial source
domains, in case there are too many of them. Experiments
in cross-subject MI and ERP classiﬁcation demonstrated that
MEKT outperformed several state-of-the-art TL approaches,
and DTE can reduce the computational cost to more than half
of when the number of source domains is large, with little
sacriﬁce of classiﬁcation accuracy.
A comparison of the afore-mentioned EEG data alignment
approaches, and a new approach [50] introduced later in this
section, is given in Table I.
Singh et al. [63] proposed a TL approach for estimating the
sample covariance matrices, which are used by the MDRM
classiﬁer, from a very small number of target domain samples.
It ﬁrst estimates the sample covariance matrix for each class
by a weighted average of the sample covariance matrix of
the corresponding class from the target domain and that in
the source domain. The mixed sample covariance matrix is
the sum of the per-class sample covariance matrices. Spatial
ﬁlters are then computed from the mixed and per-class sample
covariance matrices. Next, the covariance matrices of the
spatially ﬁltered EEG trials are further ﬁltered by Fisher
geodesic discriminant analysis [64] and used as features in
the MDRM [58] classiﬁer.
Deep learning, which has been very successful in image
processing, video analysis, speech recognition and natural
language processing, has also started to ﬁnd applications
in EEG-based BCIs. For example, Schirrmeister et al. [65]
proposed two convolutional neural networks (CNNs) for EEG
decoding, and showed that both outperformed ﬁlter bank
common spatial patterns (FBCSP) [66] in cross-subject MI
classiﬁcation. Lawhern et al. [67] proposed EEGNet, a com-
pact CNN architecture for EEG classiﬁcation. It can be applied
across different BCI paradigms, be trained with very limited
data, and generate neurophysiologically interpretable features.
EEGNet achieved robust results in both the within-subject and
cross-subject classiﬁcation of MIs and ERPs.
Although the above approaches achieved promising cross-
subject classiﬁcation performance, they did not explicitly use
the idea of TL. Currently, a common TL technique for deep
learning-based EEG classiﬁcation [68], [69] is based on ﬁne-
tuning with new data from the target session/subject. Unlike
concatenating target data with existing source data, the ﬁne-
tuning process is established on a pre-trained model and
performs iterative learning on a relatively small amount of
target data. Although the training data involved is exactly the
same as using data concatenation, the prediction performance
can be improved signiﬁcantly.
More speciﬁcally, Wu et al. [70] proposed a parallel mul-
tiscale ﬁlter CNN for MI classiﬁcation. It consisted of three
layers: a CNN to extract both temporal and spatial features
from EEG signals, a feature reduction layer with square and
log non-linear functions followed by pooling and dropout, and

6
TABLE I
COMPARISON OF DIFFERENT EEG DATA ALIGNMENT APPROACHES.
RA [57]
PT [59]
PTA [61]
EA [60]
CA [62]
LA [50]
Applicable Paradigm
MI, ERP
MI
MI, ERP, SSVEP
MI, ERP
MI, ERP
MI
Online or Ofﬂine
Both
Both
Both
Both
Both
Ofﬂine
Need Labeled Target
Domain Trials
No for MI,
Yes for ERP
No
Yes
No
No
Yes
What to Align
Riemannian space
covariance matrices
Riemannian Tangent
space features
Riemannian space
covariance matrices
Euclidean space
EEG trials
Riemannian space
covariance matrices
Euclidean space
EEG trials
Reference Matrix
Calculation
Riemannian mean
of resting state
covariance matrices
in each domain
Riemannian mean
of all covariance
matrices in
each domain
Riemannian mean
of all labeled
covariance
matrices in
each domain
Euclidean mean
of all covariance
matrices in
each domain
Riemannian,
Euclidean, or
Log-Euclidean
mean of all
covariance
matrices in
each domain
Log-Euclidean
mean of labeled
covariance matrices
in each class
of each domain
Classiﬁer
Riemannian
space only
Euclidean
space only
Riemannian
space only
Riemannian or
Euclidean space
Riemannian or
Euclidean space
Riemannian or
Euclidean space
Handle Class
Mismatch between
Domains
No
No
No
No
No
Yes
Computational Cost
High
High
High
Low
Low
Low
a dense classiﬁcation layer ﬁne-tuned on a small amount of
calibration data from the target subject. They showed that
ﬁne-tuning achieved improved performance in cross-subject
transfers.
B. Cross-Device TL
Xu et al. [71] studied the performance of deep learning
in cross-dataset TL. Eight publicly available MI datasets were
considered. Although the different datasets used different EEG
devices, channels and MI tasks, they only selected three
common channels (C3, CZ, C4) and the left-hand and right-
hand MI tasks. They applied an online pre-alignment strategy
to each EEG trial of each subject by recursively computing
the Riemannian mean online and using it as the reference
matrix in the EA approach. They showed that online pre-
alignment signiﬁcantly increased the performance of deep
learning models in cross-dataset TL.
C. Cross-Task TL
Both RA and EA assume that the source domains have the
same feature space and label space as the target domain, which
may not hold in many real-world applications, i.e., they may
not be used in cross-task transfers. Recently, He and Wu [50]
also proposed a label alignment (LA) approach, which can
handle the situation that the source domains have different
label spaces from the target domain. For MI-based BCIs, this
means the source subjects and the target subject can perform
completely different MI tasks (e.g., the source subject may
perform left-hand and right-hand MI tasks, whereas the target
subject may perform feet and tongue MIs), but the source
subjects’ data can still be used to facilitate the calibration for
a target subject.
When the source and target domain devices are different,
LA ﬁrst selects the source EEG channels that are the most
similar to the target EEG channels. Then, it computes the mean
covariance matrix of each source domain class and estimates
the mean covariance matrix of each target domain class. Next,
it re-centres each source domain class at the corresponding
estimated class mean of the target domain. Both Euclidean
space and Riemannian space feature extraction and classiﬁca-
tion approaches can next be applied to aligned trials. LA only
needs as few as one labelled sample from each target domain
class, can be used as a pre-processing step before different
feature extraction and classiﬁcation algorithms, and can be
integrated with other TL approaches to achieve an even better
performance. He and Wu [50] demonstrated the effectiveness
of LA in simultaneous cross-subject, cross-device and cross-
task TL in MI classiﬁcation.
An illustration of the difference between LA and EA is
shown in Fig. 2. To our knowledge, LA is the only cross-task
TL work in EEG-based BCIs and the most complicated TL
scenario (simultaneous cross-subject, cross-device and cross-
task TL) considered in the literature so far.
Fig. 2. Illustration of EA and LA [50].

7
IV. TL IN ERP-BASED BCIS
This section reviews recent TL approaches in ERP-based
BCIs. Many approaches introduced in the previous section,
e.g., RA, EA, RPA and EEGNet, can also be used here. To
avoid duplication, we only include approaches not introduced
in the previous section here. Because there were no publica-
tions on cross-task TL in ERP-based BCIs, we do not have a
“Cross-Task TL” subsection.
A. Cross-Subject/Session TL
Waytowich et al. [72] proposed unsupervised spectral trans-
fer method using information geometry (STIG) for subject-
independent ERP-based BCIs. STIG uses a spectral meta-
learner [73] to combine predictions from an ensemble of
MDRM classiﬁers on data from individual source subjects.
Experiments on single-trial ERP classiﬁcation demonstrated
that STIG signiﬁcantly outperformed some calibration-free ap-
proaches and traditional within-subject calibration approaches
when limited data were available in both ofﬂine and online
ERP classiﬁcations.
Wu
[74]
proposed
weighted
adaptation
regularization
(wAR) for cross-subject transfers in ERP-based BCIs in both
online and ofﬂine settings. Mathematically, wAR learns the
following classiﬁer directly:
argmin
f
Ns
X
n=1
wn
s ℓ(f(Xn
s ), yn
s ) + wt
Nl
X
n=1
wn
t ℓ(f(Xn
t ), yn
t )
+ σ∥f∥2
K + λP Df,K(Ps(Xs), Pt(Xt))
+ λQDf,K(Ps(Xs|ys), Pt(Xt|yt))
(5)
where ℓis a loss function, wt is the overall weight of target
domain samples, K is a kernel function, and σ, λP and λQ
are non-negative regularization parameters. wn
s and wn
t are
the weights for the n-th sample in the source domain and the
target domain, respectively, to balance the number of positive
and negative samples in the corresponding domain.
Brieﬂy, the ﬁve terms in (5) minimize the ﬁtting loss in
the source domain, the ﬁtting loss in the target domain,
the structural risk of the classiﬁer, the distance between the
marginal probability distributions Ps(Xs) and Pt(Xt), and
the distance between the conditional probability distributions
Ps(Xs|ys) and Pt(Xt|yt). Experiments on single-trial visual
evoked potential classiﬁcation demonstrated that both online
and ofﬂine wAR algorithms were effective. Wu [74] also
proposed a source domain selection approach, which selects
the most beneﬁcial source subjects for transferring. It can
reduce the computational cost of wAR by ∼50% without
sacriﬁcing the classiﬁcation performance.
Qi et al. [75] performed cross-subject TL on a P300 speller
to reduce the calibration time. A small set of ERP epochs
from the target subject was used as a reference to compute
the Riemannian distance to each source ERP sample from an
existing data pool. The most similar ones were selected to
train a classiﬁer and were applied to the target subject.
Jin et al. [76] used a generic model set to reduce the
calibration time in P300-based BCIs. Filtered EEG data from
116 participants were assembled into a data matrix, principal
component analysis (PCA) was used to reduce the dimension-
ality of the time domain features, and then the 116 participants
were clustered into 10 groups by k-means clustering. A
weighted linear discriminant analysis (WLDA) classiﬁer was
then trained for each cluster. These 10 classiﬁers formed the
generic model set. For a new subject, a few calibration samples
were acquired, and an online linear discriminant (OLDA)
model was trained. The OLDA model was matched to the
closest WLDA model, which was then selected as the model
for the new subject.
Deep learning has also been used in ERP classiﬁcation.
Inspired by generative adversarial networks (GANs) [77],
Ming et al. [78] proposed a subject adaptation network (SAN)
to mitigate individual differences in EEGs. Based on the
characteristics of the application, they designed an artiﬁcial
low-dimensional distribution and forced the transformed EEG
features to approximate it. For example, for two-class visual
evoked potential classiﬁcation, the artiﬁcial distribution is
bimodal, and the area of each modal is proportional to the
number of samples in the corresponding class. Experiments
on cross-subject visual evoked potential classiﬁcation demon-
strated that SAN outperformed a support vector machine
(SVM) and EEGNet.
B. Cross-Device TL
Wu et al. [26] proposed active weighted adaptation reg-
ularization (AwAR) for cross-device TL. It integrates wAR
(introduced in Section IV-A), which uses labelled data from
the previous device and handles class imbalance, and active
learning [24], which selects the most informative samples from
the new device to label. Only the common channels were used
in wAR, but all the channels of the new device can be used in
active learning to achieve better performance. Experiments on
single-trial visual evoked potential classiﬁcation using three
different EEG devices with different numbers of electrodes
showed that AwAR can signiﬁcantly reduce the calibration
data requirement for a new device in ofﬂine calibration.
To our knowledge, this is the only study on cross-device
TL in ERP-based BCIs.
V. TL IN SSVEP-BASED BCIS
This section reviews recent TL approaches in SSVEP-based
BCIs. Because there were no publications on cross-task TL
in SSVEP-based BCIs, we do not have a “Cross-Task TL”
subsection. Overall, many fewer TL studies on SSVEPs have
been performed compared with MI tasks and ERPs.
A. Cross-Subject/Session TL
Waytowich et al. [79] proposed Compact-CNN, which is
essentially the EEGNet [67] approach introduced in Sec-
tion III-A, for 12-class SSVEP classiﬁcation without the need
for any user-speciﬁc calibration. It outperformed state-of-
the-art hand-crafted approaches using canonical correlation
analysis (CCA) and Combined-CCA.
Rodrigues et al. [61] proposed RPA, which can also be used
in cross-subject transfer of SSVEP-based BCIs. Since it has
been introduced in Section III-A, it is not repeated here.

8
B. Cross-Device TL
Nakanishi et al. [80] proposed a cross-device TL algorithm
for reducing the calibration effort in an SSVEP-based BCI
speller. It ﬁrst computes a set of spatial ﬁlters by channel
averaging, CCA, or task-related component analysis and then
concatenates them to form a ﬁlter matrix W. The average trial
of Class c of the source domain is computed and ﬁltered by
W to obtain Zc. Let Xt be a single trial to be classiﬁed in the
target domain. Its spatial ﬁlter matrix Wc is then computed by
Wc = argmin
W
Zc −W TXt
2
2 ;
(6)
i.e., Wc = (XtXT
t )−1XtZT
c . Then, Pearson’s correlation
coefﬁcients between W T
c Xt and Zc are computed as r(1)
c , and
canonical correlation coefﬁcients between Xt and computer-
generated SSVEP models Yc are computed as r(2)
c . The two
feature values are combined as
ρc =
2
X
i=1
sign

r(i)
c

·

r(i)
c
2
,
(7)
and the target class is identiﬁed as argmax
c
ρc.
To our knowledge, this is the only study on cross-device
TL in SSVEP-based BCIs.
VI. TL IN ABCIS
Recently, there has been a fast-growing research interest
in aBCIs [34]–[37]. Emotions can be represented by discrete
categories [81] (e.g., happy, sad, and angry) and by continuous
values in the 2D space of arousal and valence [82] or the
3D space of arousal, valence, and dominance [83]. Therefore,
there can be both classiﬁcation and regression problems in
aBCIs. However, the current literature focused exclusively on
classiﬁcation problems.
Most studies used the publicly available DEAP [84] and
SEED [9] datasets. DEAP consists of 32-channel EEGs
recorded by a BioSemi ActiveTwo device from 32 subjects
while they were watching minute-long music videos, whereas
SEED consists of 62-channel EEGs recorded by an ESI
NeuroScan device from 15 subjects while they were watching
4-minute movie clips. By using SEED, Zheng et al. [85]
investigated whether stable EEG patterns exist over time
for emotion recognition. Using differential entropy features,
they found that stable patterns did exhibit consistency across
sessions and subjects. Thus, it is possible to perform TL in
aBCIs.
This section reviews the latest progress on TL in aBCIs.
Because there were no publications on cross-task TL in aBCIs,
we do not have a “Cross-Task TL” subsection.
A. Cross-Subject/Session TL
Chai et al. [86] proposed adaptive subspace feature match-
ing (ASFM) for cross-subject and cross-session transfer in
ofﬂine and simulated online EEG-based emotion classiﬁcation.
Differential entropy features were used. ASFM ﬁrst performs
PCA of the source domain and the target domain separately.
Let Zs (Zt) be the d leading principal components in the
source (target) domain, which form the corresponding sub-
space. Then, ASFM transforms the source domain subspace
to ZsZT
s Zt and projects the source data into it. The target
data are projected directly into Zt. In this way, the marginal
distribution discrepancy between the two domains is reduced.
Next, an iterative pseudo-label reﬁnement strategy is used to
train a logistic regression classiﬁer using the labelled source
domain samples and pseudo-labelled target domain samples,
which can be directly applied to unlabelled target domain
samples.
Lin and Jung [87] proposed a conditional TL (cTL) frame-
work to facilitate positive cross-subject transfers in aBCIs.
Five differential laterality features (topoplots), corresponding
to ﬁve different frequency bands, from each EEG channel are
extracted. The cTL method ﬁrst computes the classiﬁcation
accuracy by using the target subject’s data only and performs
transfer only if that accuracy is below the chance level. Then, it
uses ReliefF [88] to select a few of the most emotion-relevant
features in the target domain and calculates their correlations
with the corresponding features in each source domain to
select a few of the most similar (correlated) source subjects.
Next, the target domain data and the selected source domain
data are concatenated to train a classiﬁer.
Lin et al. [89] proposed a robust PCA (RPCA)-based [90]
signal ﬁltering strategy and validated its performance in cross-
day binary emotion classiﬁcation. RPCA decomposes an input
matrix into the sum of a low-rank matrix and a sparse matrix.
The former accounts for the relatively regular proﬁles of the
input signals, whereas the latter accounts for its deviant events.
Lin et al. showed that the RPCA-decomposed sparse signals
ﬁltered from the background EEG activity contributed more to
the inter-day variability and that the predominately captured
the EEG oscillations of emotional responses behaved relatively
consistently across days.
Li et al. [91] extracted nine types of time-frequency do-
main features (the peak-to-peak mean, mean square, variance,
Hjorth activity, Hjorth mobility, Hjorth complexity, maximum
power spectral frequency, maximum power spectral density,
power sum) and nine types of non- linear dynamical system
features (the approximate entropy, C0 complexity, correlation
dimension, Kolmogorov entropy, Lyapunov exponent, permu-
tation entropy, singular entropy, Shannon entropy, spectral
entropy) from EEG measurements. Through automatic and
manual feature selection, they veriﬁed the effectiveness and
performance of the upper bounds of those features in cross-
subject emotion classiﬁcation on DEAP and SEED. They
found that L1-norm penalty-based feature selection achieved
robust performance on both datasets, and the Hjorth mobility
in the beta rhythm achieved the highest mean classiﬁcation
accuracy.
Liu et al. [92] performed cross-day EEG-based emo-
tion classiﬁcation. Seventeen subjects watched 6-9 emotional
movie clips on ﬁve different days over one month. Spectral
powers of the delta, theta, alpha, beta, low and high gamma
bands were computed for each of the 60 channels as initial
features, and then recursive feature elimination was used for
feature selection. In cross-day classiﬁcation, the data from a
subset of the ﬁve days were used by an SVM to classify

9
the data from the remaining days. They showed that EEG
variability could impair the emotion classiﬁcation performance
dramatically, and using data from more days during training
could signiﬁcantly improve the generalization performance.
Yang et al. [93] studied cross-subject emotion classiﬁcation
on DEAP and SEED. Ten linear and non-linear features (the
Hjorth activity, Hjorth mobility, Hjorth complexity, standard
deviation, PSD alpha, PSD beta, PSD gamma, PSD theta,
sample entropy, and wavelet entropy) were extracted from each
channel and concatenated. Then, sequential backward feature
selection and signiﬁcance test were used for feature selection,
and an RBF SVM was used as the classiﬁer.
Li et al. [94] considered cross-subject EEG emotion clas-
siﬁcation for both supervised (the target subject has some
labelled samples) and semi-supervised (the target subject has
some labelled samples and unlabelled samples) scenarios.
We brieﬂy introduce only their best-performing supervised
approach here. Multiple source domains are assumed. They
ﬁrst performed source selection by training a classiﬁer in
each source domain and compute its classiﬁcation accuracy
on the labelled samples in the target domain. These accuracies
were then sorted to select the top few source subjects. A
style transfer mapping was learned between the target and
each selected source. For each selected source subject, they
performed SVM classiﬁcation on his/her data, removed the
support vectors (because they are near the decision boundary
and hence uncertain), performed k-means clustering on the
remaining samples to obtain the prototypes, and mapped each
target domain labelled sample feature vector xn
t to the nearest
prototype in the same class by the following mapping:
min
A,b
n
X
i=1
∥Axn
t + b −dn∥2
2 + β∥A −I∥2
F + γ∥b∥2
2,
(8)
where dn is the nearest prototype in the same class of the
source domain, and β and γ are hyperparameters. A new,
unlabelled sample in the target domain is ﬁrst mapped to
each selected source domain and then classiﬁed by a classiﬁer
trained in the corresponding source domain. The classiﬁcation
results from all source domains were then weighted averaged,
where the weights were determined by the accuracies of the
source domain classiﬁers.
Deep learning has also been gaining popularity in aBCI.
Chai et al. [95] proposed a subspace alignment autoencoder
(SAAE) for cross-subject and cross-session transfer in EEG-
based emotion classiﬁcation. First, differential entropy features
from both domains were transformed into a domain-invariant
subspace using a stacked autoencoder. Then, kernel PCA,
graph regularization and maximum mean discrepancy were
used to reduce the feature distribution discrepancy between
the two domains. After that, a classiﬁer trained in the source
domain can be directly applied to the target domain.
Yin and Zhang [96] proposed an adaptive stacked denoising
autoencoder (SDAE) for cross-session binary classiﬁcation of
mental workload levels from EEG. The weights of the shallow
hidden neurons of the SDAE were adaptively updated during
the testing phase using augmented testing samples and their
pseudo-labels.
Zheng et al. [97] presented EmotionMeter, a multi-modal
emotion recognition framework that combines brain waves
and eye movements to classify four emotions (fear, sadness,
happiness, and neutrality). They adopted a bimodal deep
autoencoder to extract the shared representations of both EEGs
and eye movements. Experimental results demonstrated that
modality fusion combining EEG and eye movements with
multi-modal deep learning can signiﬁcantly enhance emotion
recognition accuracy compared with a single modality. They
also investigated the complementary characteristics of EEGs
and eye movements for emotion recognition and the stability
of EmotionMeter across sessions. They found that EEGs and
eye movements have important complementary characteristics,
e.g., EEGs have the advantage of classifying happy emotion
(80%) compared with eye movements (67%), whereas eye
movements outperform EEGs in recognizing fear emotion
(67% versus 65%).
Fahimi et al. [98] performed cross-subject attention clas-
siﬁcation. They ﬁrst trained a CNN by combining EEG data
from the source subjects and then ﬁne-tuned it by using some
calibration data from the target subject. The inputs were raw
EEGs, bandpass ﬁltered EEGs, and decomposed EEGs (delta,
theta, alpha, beta and gamma bands).
Li et al. [99] proposed R2G-STNN, which consists of
spatial and temporal neural networks with regional-to-global
hierarchical feature learning, to learn discriminative spatial-
temporal EEG features for subject-independent emotion clas-
siﬁcation. To learn the spatial features, a bidirectional long
short-term memory (LSTM) network was used to capture the
intrinsic spatial relationships of EEG electrodes within and
between different brain regions. A region-attention layer was
also introduced to learn the weights of different brain regions.
A domain discriminator working corporately with the classiﬁer
was used to reduce domain shift between training and testing.
Li et al. [100] further proposed an improved bi-hemisphere
domain adversarial neural network (BiDANN-S) for subject-
independent emotion classiﬁcation. Inspired by the neuro-
science ﬁndings that the left and right hemispheres of the
human brain are asymmetric to the emotional response,
BiDANN-S uses a global and two local domain discriminators
working adversarially with a classiﬁer to learn discriminative
emotional features for each hemisphere. To improve the gen-
eralization performance and to facilitate subject-independent
EEG emotion classiﬁcation, it also tries to reduce the possible
domain differences in each hemisphere between the source and
target domains and ensure that the extracted EEG features are
robust to subject variations.
Li et al. [101] proposed a neural network model for cross-
subject/session EEG emotion recognition, which does not
require label information in the target domain. The neural
network was optimized by minimizing the classiﬁcation error
in the source domain while making the source and target
domains similar in their latent representations. Adversarial
training was used to adapt the marginal distributions in the
early layers, and association reinforcement was performed to
adapt the conditional distributions in the last few layers. In
this way, it achieved joint distribution adaptation [102].
Song et al. [103] proposed a dynamical graph convolutional

10
neural network (DGCNN) for subject-dependent and subject-
independent emotion classiﬁcation. Each EEG channel was
represented as a node in the DGCNN, and differential entropy
features from ﬁve frequency bands were used as inputs. After
graph ﬁltering, a 1 × 1 convolution layer learned the dis-
criminative features among the ﬁve frequency bands. A ReLU
activation function was adopted to ensure that the outputs of
the graph ﬁltering layer are non-negative. The outputs of the
activation function were sent to a multilayer dense network
for classiﬁcation.
Appriou et
al. [104] compared several modern ma-
chine learning algorithms on subject-speciﬁc and subject-
independent cognitive and emotional state classiﬁcation, in-
cluding Riemannian approaches and a CNN. They found
that the CNN performed the best in both subject-speciﬁc
and subject-independent workload classiﬁcation. A ﬁlter bank
tangent space classiﬁer (FBTSC) was also proposed. It ﬁrst
ﬁlters an EEG into several different frequency bands. For each
band, it computes the covariance matrices of the EEG trials,
projects them onto the tangent space at their mean, and then
applies a Euclidean space classiﬁer. FBTSC achieved the best
performance in subject-speciﬁc emotion (valance and arousal)
classiﬁcation.
B. Cross-Device TL
Lan et al. [105] considered cross-dataset transfers between
DEAP and SEED, which have different numbers of subjects,
and were recorded using different EEG devices with different
numbers of electrodes. They used only three trials (one posi-
tive, one neutral, and one negative) from 14 selected subjects
in DEAP and only the 32 common channels between the
two datasets. Five differential entropy features in ﬁve different
frequency bands (delta, theta, alpha, beta, and gamma) were
extracted from each channel and concatenated as features. Ex-
periments showed that domain adaptation, particularly transfer
component analysis [106] and maximum independence do-
main adaptation [107], can effectively improve the classiﬁ-
cation accuracies compared to the baseline.
Lin [108] proposed RPCA-embedded TL to generate a
personalized cross-day emotion classiﬁer with less labelled
data while obviating intra- and inter-individual differences.
The source dataset consists of 12 subjects using a 14-channel
Emotiv EPOC device, and the target dataset consists of 26
different subjects using a 30-channel Neuroscan Quik-Cap.
Twelve of the 26 channels of Quik-Cap were ﬁrst selected
to align with 12 of the 14 selected channels from the EPOC
device. The Quik-Cap EEG signals were also down-sampled
and ﬁltered to match those of the EPOC device. Five frequency
band (delta, theta, alpha, beta, gamma) features from each
of the six left-right channel pairs (e.g., AF3-AF4, F7-F8),
four fronto-posterior pairs (e.g., AF3-O1, F7-P7) and the 12
selected channels were extracted, resulting in a 120D feature
vector for each trial. Similar to [89], the sparse RPCA matrix
of the feature matrix was used as the ﬁnal feature. The
Riemannian distance between the trials of each source subject
and the target subject was computed as a dissimilarity measure
to select the most similar source subjects, whose trials were
combined with the trials from the target subject to train an
SVM classiﬁer.
Zheng et al. [109] considered an interesting cross-device (or
cross-modality) and cross-subject TL scenario in which the
target subject’s eye tracking data were used to enhance the
performance of cross-subject EEG-based affect classiﬁcation.
It is a 3-step procedure. First, multiple individual emotion
classiﬁers are trained for the source subjects. Second, a re-
gression function is learned to model the relationship between
the data distribution and classiﬁer parameters. Third, a target
classiﬁer is constructed using the target feature distribution
and the distribution-to-classiﬁer mapping. This heterogeneous
TL approach achieved comparable performance with homoge-
neous EEG-based models and scanpath-based models. To our
knowledge, this is the ﬁrst study that transfers between two
different types of signals.
Deep learning has also been used in cross-device TL in
aBCIs. EEG trials are usually transformed to some sort of
images before input to the deep learning model. In this way,
EEG signals from different devices can be made consistent.
Siddharth et al. [110] performed multimodality (e.g., EEG,
ECG, face, etc.) cross-dataset emotion classiﬁcation, e.g.,
training on DEAP and testing on the MAHNOB-HCI database
[111]. We only brieﬂy introduce their EEG-based deep learn-
ing approach here, which works for datasets with different
numbers and placements of electrodes, different sampling
rates, etc. The EEG power spectral densities (PSDs) in the
theta, alpha and beta bands were used to plot three topogra-
phies for each trial. Then, each topography was considered a
component of a colour image and weighted by the ratio of
alpha blending to form the colour image. In this way, one
colour image representing the topographic PSD was obtained
for each trial, and the images obtained from different EEG
devices can be directly combined or compared. A pre-trained
VGG-16 network was used to extract 4,096 features from each
image, whose number was later reduced to 30 by PCA. An
extreme learning machine was used as the classiﬁer for ﬁnal
classiﬁcation.
Cimtay and Ekmekcioglu [112] used a pre-trained state-
of-the-art CNN model, Inception-ResNet-v2, for cross-subject
and cross-dataset transfers. Since Inception-ResNet-v2 re-
quires the input data size to be (N1, N, 3), where N1 ≥75 is
the number of EEG channels and N ≥75 is the number of
time domain samples, when the number of EEG channels is be
less than 75, they increased the number of channels by adding
noisy copies of them (Gaussian random noise was used) to
reach N1 = 80. This process was repeated three times so that
each trial became a 80 × 300 × 3 matrix, which was then used
as the input to Inception-ResNet-v2. They also added a global
average pooling layer and ﬁve dense layers after Inception-
ResNet-v2 for classiﬁcation.
VII. TL IN BCI REGRESSION PROBLEMS
There are many important BCI regression problems, e.g.,
driver drowsiness estimation [38]–[40], vigilance estimation
[11], [12], [113], and user reaction time estimation [41],
which were not adequately addressed in previous reviews. This

11
section ﬁlls this gap. Because there were no publications on
cross-device and cross-task TL in BCI regression problems,
we do not have subsections on them.
A. Cross-Subject/Session TL
Wu et al. [40] proposed a novel online weighted adaptation
regularization for regression (OwARR) algorithm to reduce
the amount of subject-speciﬁc calibration data in EEG-based
driver drowsiness estimation and a source domain selection
approach to save approximately half of its computational cost.
OwARR minimizes the following loss function, similar to
wAR [26]:
min
f
Ns
X
n=1
(yn
s −f(Xn
s ))2 + wt
Nl
X
n=1
(yn
t −f(Xn
t ))2
+ λ [d(Ps(Xs), Pt(Xt)) + d(Ps(Xs|ys), Pt(Xt|yt))]
−γ˜r2(y, f(X))
(9)
where λ and γ are non-negative regularization parameters
and wt is the overall weight for target domain samples.
˜r2(y, f(X)) approximates the sample Pearson correlation
coefﬁcient between y and f(X). Fuzzy sets were used to
deﬁne fuzzy classes so that d(Ps(Xs|ys), Pt(Xt|yt)) can be
efﬁciently computed. The ﬁve terms in (9) minimize the
ﬁtting error in the source domain, the ﬁtting error in the
target domain, the distance between the marginal probability
distributions, the distance between the conditional probability
distributions, and the estimated sample Pearson correlation
coefﬁcient between y and f(X). Wu et al. [40] showed
that OwARR and OwARR with source domain selection can
achieve signiﬁcantly smaller estimation errors than several
other cross-subject TL approaches.
Jiang et al. [39] further extended OwARR to multi-view
learning, where the ﬁrst view included theta band powers from
all channels, and the second view converted the ﬁrst view into
dBs and removed some bad channels. A TSK fuzzy system
was used as the regression model, optimized by minimizing (9)
for both views simultaneously and adding an additional term to
enforce the consistency between the two views (the estimation
from one view should be close to that from the other view).
They demonstrated that the proposed approach outperformed
a domain adaptation with a model fusion approach [114] in
cross-subject TL.
Wei et al. [115] also performed cross-subject driver drowsi-
ness estimation. Their procedure consisted of three steps: 1)
Ranking. For each source subject, it computed six distance
measures (Euclidean distance, correlation distance, Cheby-
shev distance, cosine distance, Kullback-Leibler divergence,
and transferability-based distance) between his/her own alert
baseline (the ﬁrst 10 trials) power distribution and all other
source subjects’ distributions and the cross-subject model
performance (XP), which is the transferability of other source
subjects on the current subject. A support vector regression
(SVR) model was then trained to predict XP from the distance
measures. In this way, given a target subject with a few calibra-
tion trials, the XP of the source subjects can be computed and
ranked. 2) Fusion: a weighted average was used to combine
the source models, where the weights were determined from
a modiﬁed logistic function optimized on the source subjects.
3) Re-calibration: the weighted average was subtracted by an
offset, estimated as the median of the initial 10 calibration
trials (i.e., the alert baseline) from the target subject. They
showed that this approach can result in a 90% calibration time
reduction in driver drowsiness index estimation.
Chen et al. [116] integrated feature selection and an adapta-
tion regularization-based TL (ARTL) [48] classiﬁer for cross-
subject driver status classiﬁcation. The most novel part is
feature selection, which extends the traditional ReliefF [88]
and minimum redundancy maximum relevancy (mRMR) [117]
to class separation and domain fusion (CSDF)-ReliefF and
CSDF-mRMR, which consider both the class separability and
the domain similarity, i.e., the selected feature subset should si-
multaneously maximize the distinction among different classes
and minimize the difference among different domains. The
ranks of the features from different feature selection algorithms
were then fused to identify the best feature set, which was used
in ARTL for classiﬁcation.
Deep learning has also been used in BCI regression prob-
lems.
Ming et al. [118] proposed a stacked differentiable neural
computer and demonstrated its effectiveness in cross-subject
EEG-based mind load estimation and reaction time estimation.
The original long short-term memory network controller in
differentiable neural computers was replaced by a recurrent
convolutional network controller, and the memory-accessing
structures were also adjusted for processing EEG topographic
data.
Cui et al. [38] proposed a subject-independent TL approach,
feature weighted episodic training (FWET), to completely
eliminate the calibration requirement in cross-subject transfers
in EEG-based driver drowsiness estimation. It integrates fea-
ture weighting to learn the importance of different features and
episodic training for domain generalization. Episodic training
considers the conditional distributions P(ys|f(Xs)) directly
and trains a regression network f that aligns P(ys|f(Xs))
in all the source domains, which usually generalizes well to
the unseen target domain Dt. It ﬁrst establishes a subject-
speciﬁc feature transformation model fθs and a subject-
speciﬁc regression model fψs for each source subject to
learn the domain-speciﬁc information, then trains a feature
transformation model fθ that makes the transformed features
from Subject s still perform well when applied to a regressor
fψj trained on Subject j (j̸ = s). The overall loss function of
episodic training, when Subject s’s data are fed into Subject j’s
regressor, is:
ℓs,j =
Ns
X
n=1
ℓ(yn
s , fψ(fθ(Xn
s )))
+ λ
Ns
X
n=1
ℓ(yn
s , f ψj(fθ(Xn
s ))),
(10)
where fψj means that fψj is not updated during backpropaga-
tion. Once the optimal fψ and fθ are obtained, the prediction
for Xt is ˆyt = fψ(fθ(Xt)).

12
VIII. TL IN ADVERSARIAL ATTACKS OF EEG-BASED
BCIS
Adversarial attacks of EEG-based BCIs represent one of
the latest developments in BCIs. It was ﬁrst studied by Zhang
and Wu [42]. They found that adversarial perturbations, which
are deliberately designed tiny perturbations, can be added
to normal EEG trials to fool the machine learning model
and cause dramatic performance degradation. Both traditional
machine learning models and deep learning models, as well
as both classiﬁers and regression models in EEG-based BCIs,
can be attacked.
Adversarial attacks can target different components of a
machine learning model, e.g., training data, model parameters,
test data, and test output, as shown in Fig. 3. To date,
only adversarial examples (benign examples contaminated by
adversarial perturbations) targeting the test inputs have been
investigated in EEG-based BCIs, so this section only considers
adversarial examples.
Fig. 3. Attack strategies to different components of a machine learning model.
A more detailed illustration of the adversarial example
attack scheme is shown in Fig. 4. A jamming module is
injected between signal processing and machine learning to
generate adversarial examples.
Fig. 4. Adversarial example generation scheme [42].
Table II shows the three attack types in EEG-based BCIs.
White-box attacks know all information about the victim
model, including its architecture and parameters, and hence are
the easiest to perform. Black-box attacks know nothing about
the victim model but can only supply inputs to it and observe
its output and hence are the most challenging to perform.
A. Cross-Model Attacks
Different from the cross-subject/session/device/task TL sce-
narios considered in the previous ﬁve sections, adversarial
TABLE II
SUMMARY OF THE THREE ATTACK TYPES IN EEG-BASED BCIS [42].
Victim Model
White-Box
Grey-Box
Black-Box
Information
Attacks
Attacks
Attacks
Know its architecture
✓
×
×
Know its parameters θ
✓
×
×
Know its training data
−
✓
×
Can observe its response
−
−
✓
attacks in BCIs so far mainly considered cross-model attacks2,
where adversarial examples generated from one machine learn-
ing model are used to attack another model. This assumption
is necessary in grey-box and black-box attacks because the
victim model is unknown, and the attacker needs to construct
its own model (called the substitute model) to approximate the
victim model.
Interestingly, cross-model attacks can be performed without
explicitly considering TL. They are usually achieved by mak-
ing use of the transferability of adversarial examples [119],
i.e., adversarial examples generated by one machine learning
model may also be used to fool a different model. The
fundamental reason behind this property is still unclear, but
it does not hinder people from making use of it.
For example, Zhang and Wu [42] proposed unsupervised
fast gradient sign methods, which can effectively perform
white-box, grey-box and black-box attacks on deep learning
classiﬁers. Two BCI paradigms, i.e., MI and ERP, and three
popular deep learning models, i.e., EEGNet, Deep ConvNet
and Shallow ConvNet, were considered. Meng et al. [43]
further showed that the transferability of adversarial examples
can also be used to attack regression models in BCIs; e.g.,
adversarial examples designed from a multi-layer perceptron
neural network can be used to attack a ridge regression model,
and vice versa, in EEG-based user reaction time estimation.
IX. CONCLUSIONS
This paper has reviewed recently proposed TL approaches
in EEG-based BCIs, according to six different paradigms and
applications: MI, ERP, SSVEP, aBCI, regression problems,
and adversarial attacks. TL algorithms are grouped into cross-
subject/session, cross-device and cross-task approaches and
introduced separately. Connections among similar approaches
are also pointed out.
The following observations and conclusions can be made,
which may point to some future research directions:
1) Among the three classic BCI paradigms (MI, ERP and
SSVEP), SSVEP seems to receive the least amount of
attention. Very few TL approaches have been proposed
recently. One reason may be that MI and ERP are very
similar, so many TL approaches developed for MI can
2Existing publications [42], [43] also considered cross-subject attacks, but
the meaning of cross-subject in adversarial attacks is different from the cross-
subject TL setting in previous sections: in adversarial attacks, cross-subject
means that the same machine learning model is used by all subjects, but the
scheme for generating adversarial examples is designed on some subjects and
applied to another subject. It assumes that the victim machine learning model
works well for all subjects.

13
be applied to ERPs directly or with little modiﬁcation,
e.g., RA, EA, RPA and EEGNet, whereas SSVEP is a
quite different paradigm.
2) Two new applications of EEG-based BCIs, i.e., aBCI
and regression problems, have been attracting increasing
research interest. Interestingly, both of them are passive
BCIs [120]. Although both classiﬁcation and regression
problems can be formulated in aBCIs, existing research
has focused almost exclusively on classiﬁcation prob-
lems.
3) Adversarial attacks, one of the latest developments in
EEG-based BCIs, can be performed across different
machine learning models by utilizing the transferability
of adversarial examples. However, explicitly considering
TL between different domains may further improve the
attack performance. For example, in black-box attacks,
TL can make use of publicly available datasets to reduce
the number of queries to the victim model or, in other
words, to better approximate the victim model given the
same number of queries.
4) Most TL studies focused on cross-subject/session trans-
fers. Cross-device transfers have started to attract atten-
tion, but cross-task transfers remain largely unexplored.
To our knowledge, there has been only one such study
[50] since 2016. Effective cross-device and cross-task
transfers would make EEG-based BCIs much more
practical.
5) Among various TL approaches, Riemannian geometry
and deep learning are emerging and gaining momentum,
each of which has a group of approaches proposed.
6) Although most research on TL in BCIs has focused
on classiﬁers or regression models, i.e., at the pattern
recognition stage, TL in BCIs can also be performed in
trial alignment, e.g., RA, EA, LA and RPA, in signal
ﬁltering, e.g., transfer kernel common spatial patterns
[51], and in feature extraction/selection, e.g., CSDF-
ReliefF and CSDF-mRMR [116]. Additionally, these
TL-based individual components can also be assembled
into a complete machine learning pipeline to achieve
even better performance. For example, EA and LA data
alignment schemes have been combined with TL clas-
siﬁers [50], [60], and CSDF-ReliefF and CSDF-mRMR
feature selection approaches have also been integrated
with TL classiﬁers [116].
7) TL can also be integrated with other machine learning
approaches, e.g., active learning [24], for improved
performance [25], [26].
REFERENCES
[1] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and
T. M. Vaughan, “Brain-computer interfaces for communication and
control,” Clinical Neurophysiology, vol. 113, no. 6, pp. 767–791, 2002.
[2] B. J. Lance, S. E. Kerick, A. J. Ries, K. S. Oie, and K. McDowell,
“Brain-computer interface technologies in the coming decades,” Proc.
of the IEEE, vol. 100, no. 3, pp. 1585–1599, 2012.
[3] J. J. Vidal, “Toward direct brain-computer communication,” Annual
Review of Biophysics and Bioengineering, vol. 2, no. 1, pp. 157–180,
1973.
[4] E. E. Fetz, “Operant conditioning of cortical unit activity,” Science,
vol. 163, no. 3870, pp. 955–958, 1969.
[5] J. M. R. Delgado, Physical control of the mind: Toward a psychocivi-
lized society. New York City: World Bank Publications, 1969, vol. 41.
[6] G. Pfurtscheller, G. R. M¨uller-Putz, R. Scherer, and C. Neuper, “Reha-
bilitation with brain-computer interface systems,” Computer, vol. 41,
no. 10, pp. 58–65, 2008.
[7] J. van Erp, F. Lotte, and M. Tangermann, “Brain-computer interfaces:
Beyond medical applications,” Computer, vol. 45, no. 4, pp. 26–34,
2012.
[8] D. Marshall, D. Coyle, S. Wilson, and M. Callaghan, “Games, game-
play, and BCI: the state of the art,” IEEE Trans. on Computational
Intelligence and AI in Games, vol. 5, no. 2, pp. 82–99, 2013.
[9] W. Zheng and B. Lu, “Investigating critical frequency bands and chan-
nels for EEG-based emotion recognition with deep neural networks,”
IEEE Trans. on Autonomous Mental Development, vol. 7, no. 3, pp.
162–175, 2015.
[10] T. G. Monteiro, C. Skourup, and H. Zhang, “Using EEG for mental
fatigue assessment: A comprehensive look into the current state of the
art,” IEEE Trans. on Human-Machine Systems, vol. 49, no. 6, pp. 599–
610, 2019.
[11] W.-L. Zheng and B.-L. Lu, “A multimodal approach to estimating vig-
ilance using EEG and forehead EOG,” Journal of Neural Engineering,
vol. 14, no. 2, p. 026017, 2017.
[12] L.-C. Shi and B.-L. Lu, “EEG-based vigilance estimation using extreme
learning machines,” Neurocomputing, vol. 102, pp. 135–143, 2013.
[13] R. P. Rao, Brain-Computer Interfacing: An Introduction.
New York,
NY: Cambridge University Press, 2013.
[14] L.-D. Liao, C.-T. Lin, K. McDowell, A. Wickenden, K. Gramann,
T.-P. Jung, L.-W. Ko, and J.-Y. Chang, “Biosensor technologies for
augmented brain-computer interfaces in the next decades,” Proc. of the
IEEE, vol. 100, no. 2, pp. 1553–1566, 2012.
[15] S. Makeig, C. Kothe, T. Mullen, N. Bigdely-Shamlo, Z. Zhang, and
K. Kreutz-Delgado, “Evolving signal processing for brain-computer
interfaces,” Proc. of the IEEE, vol. 100, no. Special Centennial Issue,
pp. 1567–1584, 2012.
[16] H. Ramoser, J. Muller-Gerking, and G. Pfurtscheller, “Optimal spatial
ﬁltering of single trial EEG during imagined hand movement,” IEEE
Trans. on Rehabilitation Engineering, vol. 8, no. 4, pp. 441–446, 2000.
[17] S. Makeig, A. J. Bell, T.-P. Jung, and T. J. Sejnowski, “Independent
component analysis of electroencephalographic data,” in Advances in
Neural Information Processing Systems, Denver, CO, Dec. 1996, pp.
145–151.
[18] T.-P. Jung, S. Makeig, C. Humphries, T.-W. Lee, M. J. Mckeown,
V. Iragui, and T. J. Sejnowski, “Removing electroencephalographic
artifacts by blind source separation,” Psychophysiology, vol. 37, no. 2,
pp. 163–178, 2000.
[19] B. Rivet, A. Souloumiac, V. Attina, and G. Gibert, “xDAWN algorithm
to enhance evoked potentials: application to brain-computer interface,”
IEEE Trans. on Biomedical Engineering, vol. 56, no. 8, pp. 2035–2043,
2009.
[20] X.-W. Wang, D. Nie, and B.-L. Lu, “Emotional state classiﬁcation
from EEG data using machine learning approach,” Neurocomputing,
vol. 129, pp. 94–106, 2014.
[21] F. Yger, M. Berar, and F. Lotte, “Riemannian approaches in brain-
computer interfaces: a review,” IEEE Trans. on Neural Systems and
Rehabilitation Engineering, vol. 25, no. 10, pp. 1753–1762, 2017.
[22] X. Wu, W.-L. Zheng, and B.-L. Lu, “Identifying functional brain
connectivity patterns for EEG-based emotion recognition,” in Proc.
9th Int’l IEEE/EMBS Conf. on Neural Engineering, San Francisco,
CA, Mar. 2019, pp. 235–238.
[23] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans.
on Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345–1359,
2010.
[24] B. Settles, “Active learning literature survey,” University of Wisconsin–
Madison, Computer Sciences Technical Report 1648, 2009.
[25] D. Wu, B. J. Lance, and T. D. Parsons, “Collaborative ﬁltering for
brain-computer interaction using transfer learning and active class
selection,” PLoS ONE, 2013.
[26] D. Wu, V. J. Lawhern, W. D. Hairston, and B. J. Lance, “Switching
EEG headsets made easy: Reducing ofﬂine calibration effort using
active wighted adaptation regularization,” IEEE Trans. on Neural
Systems and Rehabilitation Engineering, vol. 24, no. 11, pp. 1125–
1137, 2016.
[27] G. Pfurtscheller and C. Neuper, “Motor imagery and direct brain-
computer communication,” Proc. of the IEEE, vol. 89, no. 7, pp. 1123–
1134, 2001.
[28] T. C. Handy, Ed., Event-related potentials: A methods handbook.
Boston, MA: The MIT Press, 2005.

14
[29] S. Lees, N. Dayan, H. Cecotti, P. McCullagh, L. Maguire, F. Lotte, and
D. Coyle, “A review of rapid serial visual presentation-based brain–
computer interfaces,” Journal of Neural Engineering, vol. 15, no. 2, p.
021001, 2018.
[30] S. Sutton, M. Braren, J. Zubin, and E. John, “Evoked-potential corre-
lates of stimulus uncertainty,” Science, vol. 150, no. 3700, pp. 1187–
1188, 1965.
[31] O. Friman, I. Volosyak, and A. Graser, “Multiple channel detection
of steady-state visual evoked potentials for brain-computer interfaces,”
IEEE Trans. on Biomedical Engineering, vol. 54, no. 4, pp. 742–750,
2007.
[32] F. Beverina, G. Palmas, S. Silvoni, F. Piccione, S. Giove et al.,
“User adaptive BCIs: SSVEP and P300 based interfaces.” PsychNology
Journal, vol. 1, no. 4, pp. 331–354, 2003.
[33] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao,
“High-speed spelling with a noninvasive brain-computer interface,”
Proc. National Ccademy of Eciences, vol. 112, no. 44, pp. E6058–
E6067, 2015.
[34] C. Muhl, B. Allison, A. Nijholt, and G. Chanel, “A survey of affective
brain computer interfaces: principles, state-of-the-art, and challenges,”
Brain-Computer Interfaces, vol. 1, no. 2, pp. 66–84, 2014.
[35] A. Al-Nafjan, M. Hosny, Y. Al-Ohali, and A. Al-Wabil, “Review and
classiﬁcation of emotion recognition based on EEG brain-computer
interface system research: a systematic review,” Applied Sciences,
vol. 7, no. 12, p. 1239, 2017.
[36] Y.-W. Shen and Y.-P. Lin, “Challenge for affective brain-computer
interfaces: Non-stationary spatio-spectral EEG oscillations of emotional
responses,” Frontiers in Human Neuroscience, vol. 13, 2019.
[37] S. M. Alarcao and M. J. Fonseca, “Emotions recognition using EEG
signals: A survey,” IEEE Trans. on Affective Computing, vol. 10, no. 3,
pp. 374–393, 2019.
[38] Y. Cui, Y. Xu, and D. Wu, “EEG-based driver drowsiness estimation
using feature weighted episodic training,” IEEE Trans. on Neural
Systems and Rehabilitation Engineering, vol. 27, no. 11, pp. 2263–
2273, 2019.
[39] Y. Jiang, Y. Zhang, C. Lin, D. Wu, and C.-T. Lin, “EEG-based driver
drowsiness estimation using an online multi-view and transfer TSK
fuzzy system,” IEEE Trans. on Intelligent Transportation Systems,
2020, in press.
[40] D. Wu, V. J. Lawhern, S. Gordon, B. J. Lance, and C.-T. Lin,
“Driver drowsiness estimation from EEG signals using online weighted
adaptation regularization for regression (OwARR),” IEEE Trans. on
Fuzzy Systems, vol. 25, no. 6, pp. 1522–1535, 2017.
[41] D. Wu, V. J. Lawhern, B. J. Lance, S. Gordon, T.-P. Jung, and C.-
T. Lin, “EEG-based user reaction time estimation using Riemannian
geometry features,” IEEE Trans. on Neural Systems and Rehabilitation
Engineering, vol. 25, no. 11, pp. 2157–2168, 2017.
[42] X. Zhang and D. Wu, “On the vulnerability of CNN classiﬁers in
EEG-based BCIs,” IEEE Trans. on Neural Systems and Rehabilitation
Engineering, vol. 27, no. 5, pp. 814–825, 2019.
[43] L. Meng, C.-T. Lin, T.-P. Jung, and D. Wu, “White-box target attack for
EEG-based BCI regression problems,” in Proc. Int’l Conf. on Neural
Information Processing, Sydney, Australia, Dec. 2019.
[44] P. Wang, J. Lu, B. Zhang, and Z. Tang, “A review on transfer learning
for brain-computer interface classiﬁcation,” in Proc. 5th Int’l Conf. on
Information Science and Technology, Changsha, China, April 2015.
[45] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, and M. Grosse-
Wentrup, “Transfer learning in brain-computer interfaces,” IEEE Com-
putational Intelligence Magazine, vol. 11, no. 1, pp. 20–31, 2016.
[46] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rako-
tomamonjy, and F. Yger, “A review of classiﬁcation algorithms for
EEG-based brain-computer interfaces: a 10 year update,” Journal of
Neural Engineering, vol. 15, no. 3, p. 031005, 2018.
[47] A. M. Azab, J. Toth, L. S. Mihaylova, and M. Arvaneh, “A review
on transfer learning approaches in brain–computer interface,” in Sig-
nal Processing and Machine Learning for Brain-Machine Interfaces,
T. Tanaka and M. Arvaneh, Eds.
The Institution of Engineering and
Technology, 2018, pp. 81–98.
[48] M. Long, J. Wang, G. Ding, S. J. Pan, and P. S. Yu, “Adaptation
regularization: A general framework for transfer learning,” IEEE Trans.
on Knowledge and Data Engineering, vol. 26, no. 5, pp. 1076–1089,
2014.
[49] Y. Zhang and Q. Yang, “An overview of multi-task learning,” National
Science Review, vol. 5, no. 1, pp. 30–43, 2018.
[50] H. He and D. Wu, “Different set domain adaptation for brain-computer
interfaces: A label alignment approach,” IEEE Trans. on Neural Sys-
tems and Rehabilitation Engineering, vol. 28, no. 5, pp. 1091–1108,
2020.
[51] M. Dai, D. Zheng, S. Liu, and P. Zhang, “Transfer kernel common
spatial patterns for motor imagery brain-computer interface classiﬁ-
cation,” Computational and Mathematical Methods in Medicine, vol.
2018, 2018.
[52] H. Albalawi and X. Song, “A study of kernel CSP-based motor
imagery brain computer interface classiﬁcation,” in Proc. IEEE Signal
Processing in Medicine and Biology Symposium, New York City, NY,
Dec. 2012, pp. 1–4.
[53] M. Long, J. Wang, J. Sun, and S. Y. Philip, “Domain invariant transfer
kernel learning,” IEEE Trans. on Knowledge and Data Engineering,
vol. 27, no. 6, pp. 1519–1532, 2015.
[54] A. M. Azab, L. Mihaylova, K. K. Ang, and M. Arvaneh, “Weighted
transfer learning for improving motor imagery-based braincomputer
interface,” IEEE Trans. on Neural Systems and Rehabilitation Engi-
neering, vol. 27, no. 7, pp. 1352–1359, 2019.
[55] I. Hossain, A. Khosravi, I. Hettiarachchi, and S. Nahavandi, “Multiclass
informative instance transfer learning framework for motor imagery-
based brain-computer interface,” Computational Intelligence and Neu-
roscience, vol. 2018, 2018.
[56] D. Wu, B. J. Lance, and V. J. Lawhern, “Transfer learning and
active transfer learning for reducing calibration data in single-trial
classiﬁcation of visually-evoked potentials,” in Proc. IEEE Int’l Conf.
on Systems, Man, and Cybernetics, San Diego, CA, October 2014.
[57] P. Zanini, M. Congedo, C. Jutten, S. Said, and Y. Berthoumieu, “Trans-
fer learning: a Riemannian geometry framework with applications to
brain-computer interfaces,” IEEE Trans. on Biomedical Engineering,
vol. 65, no. 5, pp. 1107–1116, 2018.
[58] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Multiclass
brain-computer interface classiﬁcation by Riemannian geometry,” IEEE
Trans. on Biomedical Engineering, vol. 59, no. 4, pp. 920–928, 2012.
[59] O. Yair, M. Ben-Chen, and R. Talmon, “Parallel transport on the cone
manifold of SPD matrices for domain adaptation,” IEEE Trans. on
Signal Processing, vol. 67, no. 7, pp. 1797–1811, 2019.
[60] H. He and D. Wu, “Transfer learning for brain-computer interfaces: A
Euclidean space data alignment approach,” IEEE Trans. on Biomedical
Engineering, vol. 67, no. 2, pp. 399–410, 2020.
[61] P. L. C. Rodrigues, C. Jutten, and M. Congedo, “Riemannian procrustes
analysis: Transfer learning for braincomputer interfaces,” IEEE Trans.
on Biomedical Engineering, vol. 66, no. 8, pp. 2390–2401, 2019.
[62] W. Zhang and D. Wu, “Manifold embedded knowledge transfer for
brain-computer interfaces,” IEEE Trans. on Neural Systems and Reha-
bilitation Engineering, vol. 28, no. 5, pp. 1117–1127, 2020.
[63] A. Singh, S. Lal, and H. W. Guesgen, “Small sample motor imagery
classiﬁcation using regularized Riemannian features,” IEEE Access,
vol. 7, pp. 46 858–46 869, 2019.
[64] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Riemannian
geometry applied to BCI classiﬁcation,” in Proc. Int’l Conf’ on Latent
Variable Analysis and Signal Separation, St. Malo, France, Sep. 2010,
pp. 629–636.
[65] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter,
K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball,
“Deep learning with convolutional neural networks for EEG decoding
and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391–
5420, 2017.
[66] K. K. Ang, Z. Y. Chin, H. Zhang, and C. Guan, “Filter bank common
spatial pattern (FBCSP) in brain-computer interface,” in Proc. IEEE
World Congress on Computational Intelligence, Hong Kong, June 2008,
pp. 2390–2397.
[67] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung,
and B. J. Lance, “EEGNet: a compact convolutional neural network for
EEG-based brain-computer interfaces,” Journal of Neural Engineering,
vol. 15, no. 5, p. 056013, 2018.
[68] Y.-X. Wang, D. Ramanan, and M. Hebert, “Growing a brain: Fine-
tuning by increasing model capacity,” in Proc. IEEE Conf. on Computer
Vision and Pattern Recognition, Honolulu, HI, Jul. 2017, pp. 2471–
2480.
[69] C.-S. Wei, T. Koike-Akino, and Y. Wang, “Spatial component-wise
convolutional network (SCCNet) for motor-imagery EEG classiﬁca-
tion,” in Proc. 9th IEEE/EMBS Int’l Conf. on Neural Engineering, San
Francisco, CA, Mar. 2019, pp. 328–331.
[70] H. Wu, F. Li, Y. Li, B. Fu, G. Shi, M. Dong, and Y. Niu, “A parallel
multiscale ﬁlter bank convolutional neural networks for motor imagery
EEG classiﬁcation,” Frontiers in Neuroscience, vol. 13, p. 1275, 2019.

15
[71] L. Xu, M. Xu, Y. Ke, X. An, S. Liu, and D. Ming, “Cross-dataset
variability problem in EEG decoding with deep learning,” Frontiers in
Human Neuroscience, vol. 14, p. 103, 2020.
[72] N. R. Waytowich, V. J. Lawhern, A. W. Bohannon, K. R. Ball, and B. J.
Lance, “Spectral transfer learning using Information Geometry for a
user-independent brain-computer interface,” Frontiers in Neuroscience,
vol. 10, p. 430, 2016.
[73] F. Parisi, F. Strino, B. Nadler, and Y. Kluger, “Ranking and combining
multiple predictors without labeled data,” Proc. National Academy of
Science, vol. 111, no. 4, pp. 1253–1258, 2014.
[74] D. Wu, “Online and ofﬂine domain adaptation for reducing BCI
calibration effort,” IEEE Trans. on Human-Machine Systems, vol. 47,
no. 4, pp. 550–563, 2017.
[75] H. Qi, Y. Xue, L. Xu, Y. Cao, and X. Jiao, “A speedy calibration method
using Riemannian geometry measurement and other-subject samples
on a P300 speller,” IEEE Trans. on Neural Systems and Rehabilitation
Engineering, vol. 26, no. 3, pp. 602–608, 2018.
[76] J. Jin, S. Li, I. Daly, Y. Miao, C. Liu, X. Wang, and A. Cichocki,
“The study of generic model set for reducing calibration time in P300-
based braincomputer interface,” IEEE Trans. on Neural Systems and
Rehabilitation Engineering, vol. 28, no. 1, pp. 3–12, 2020.
[77] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial nets,” in
Proc. Advances in Neural Information Processing Systems, Montreal,
Canada, Dec. 2014, pp. 2672–2680.
[78] Y. Ming, D. Pelusi, W. Ding, Y.-K. Wang, M. Prasad, D. Wu, and C.-T.
Lin, “Subject adaptation network for EEG data analysis,” Applied Soft
Computing, vol. 84, p. 105689, 2019.
[79] N. Waytowich, V. J. Lawhern, J. O. Garcia, J. Cummings, J. Faller,
P. Sajda, and J. M. Vettel, “Compact convolutional neural networks for
classiﬁcation of asynchronous steady-state visual evoked potentials,”
Journal of Neural Engineering, vol. 15, no. 6, p. 066031, 2018.
[80] M. Nakanishi, Y. Wang, C. Wei, K. Chiang, and T. Jung, “Facilitating
calibration in high-speed BCI spellers via leveraging cross-device
shared latent responses,” IEEE Trans. on Biomedical Engineering,
vol. 67, no. 4, pp. 1105–1113, 2020.
[81] P. Ekman and W. Friesen, “Constants across cultures in the face and
emotion,” Journal of Personality and Social Psychology, vol. 17, pp.
124–129, 1971.
[82] J. Russell, “A circumplex model of affect,” Journal of Personality and
Social Psychology, vol. 39, no. 6, pp. 1161–1178, 1980.
[83] A. Mehrabian, Basic Dimensions for a General Psychological Theory:
Implications for Personality, Social, Environmental, and Developmental
Studies.
Oelgeschlager, Gunn & Hain, 1980.
[84] S. Koelstra, C. Muhl, M. Soleymani, J. S. Lee, A. Yazdani, T. Ebrahimi,
T. Pun, A. Nijholt, and I. Patras, “DEAP: A database for emotion anal-
ysis using physiological signals,” IEEE Trans. on Affective Computing,
vol. 3, no. 1, pp. 18–31, 2012.
[85] W. Zheng, J. Zhu, and B. Lu, “Identifying stable patterns over time for
emotion recognition from EEG,” IEEE Trans. on Affective Computing,
vol. 10, no. 3, pp. 417–429, 2019.
[86] X.
Chai,
Q.
Wang,
Y.
Zhao,
Y.
Li,
D.
Liu,
X.
Liu,
and
O. Bai, “A fast, efﬁcient domain adaptation technique for cross-
domain electroencephalography(eeg)-based emotion recognition,” Sen-
sors, vol. 17, no. 5, p. 1014, 2017.
[87] Y.-P. Lin and T.-P. Jung, “Improving EEG-based emotion classiﬁcation
using conditional transfer learning,” Frontiers in Human Neuroscience,
vol. 11, p. 334, 2017.
[88] I. Kononenko, “Estimating attributes: Analysis and extensions of RE-
LIEF,” in Proc. European Conf. on Machine Learning, Catania, Italy,
Apr. 1994, pp. 171–182.
[89] Y.-P. Lin, P.-K. Jao, and Y.-H. Yang, “Improving cross-day EEG-based
emotion classiﬁcation using robust principal component analysis,”
Frontiers in Computational Neuroscience, vol. 11, p. 64, 2017.
[90] E. J. Candes, X. Li, Y. Ma, and J. Wright, “Robust principal component
analysis?” Journal of the ACM, vol. 58, no. 3, 2011.
[91] X. Li, D. Song, P. Zhang, Y. Zhang, Y. Hou, and B. Hu, “Explor-
ing EEG features in cross-subject emotion recognition,” Frontiers in
Neuroscience, vol. 12, p. 162, 2018.
[92] S. Liu, L. Chen, D. Guo, X. Liu, Y. Sheng, Y. Ke, M. Xu, X. An,
J. Yang, and D. Ming, “Incorporation of multiple-days information
to improve the generalization of EEG-based emotion recognition over
time,” Frontiers in Human Neuroscience, vol. 12, p. 267, 2018.
[93] F. Yang, X. Zhao, W. Jiang, P. Gao, and G. Liu, “Multi-method fusion
of cross-subject emotion recognition based on high-dimensional EEG
features,” Frontiers in Computational Neuroscience, vol. 13, 2019.
[94] J. Li, S. Qiu, Y. Shen, C. Liu, and H. He, “Multisource transfer
learning for cross-subject EEG emotion recognition,” IEEE Trans. on
Cybernetics, 2020, in press.
[95] X. Chai, Q. Wang, Y. Zhao, X. Liu, O. Bai, and Y. Li, “Unsupervised
domain adaptation techniques based on auto-encoder for non-stationary
EEG-based emotion recognition,” Computers in Biology and Medicine,
vol. 79, pp. 205–214, 2016.
[96] Z. Yin and J. Zhang, “Cross-session classiﬁcation of mental workload
levels using EEG and an adaptive deep learning model,” Biomedical
Signal Processing and Control, vol. 33, pp. 30–47, 2017.
[97] W.-L. Zheng, W. Liu, Y. Lu, B.-L. Lu, and A. Cichocki, “Emotion-
Meter: A multimodal framework for recognizing human emotions,”
IEEE Trans. on Cybernetics, vol. 49, no. 3, pp. 1110–1122, 2019.
[98] F. Fahimi, Z. Zhang, W. B. Goh, T.-S. Lee, K. K. Ang, and C. Guan,
“Inter-subject transfer learning with an end-to-end deep convolutional
neural network for EEG-based BCI,” Journal of Neural Engineering,
vol. 16, no. 2, p. 026007, 2019.
[99] Y. Li, W. Zheng, L. Wang, Y. Zong, and Z. Cui, “From regional
to global brain: A novel hierarchical spatial-temporal neural network
model for EEG emotion recognition,” IEEE Trans. on Affective Com-
puting, 2020, in press.
[100] Y. Li, W. Zheng, Y. Zong, Z. Cui, T. Zhang, and X. Zhou, “A bi-
hemisphere domain adversarial neural network model for EEG emotion
recognition,” IEEE Trans. on Affective Computing, 2020, in press.
[101] J. Li, S. Qiu, C. Du, Y. Wang, and H. He, “Domain adaptation for
EEG emotion recognition based on latent representation similarity,”
IEEE Trans. on Cognitive and Developmental Systems, 2020, in press.
[102] M. Long, J. Wang, G. Ding, J. Sun, and P. S. Yu, “Transfer feature
learning with joint distribution adaptation,” in Proc. IEEE Int’l Conf.
on Computer Vision, Sydney, Australia, Dec. 2013, pp. 2200–2207.
[103] T. Song, W. Zheng, P. Song, and Z. Cui, “Eeg emotion recognition
using dynamical graph convolutional neural networks,” IEEE Trans.
on Affective Computing, 2020, in press.
[104] A. Appriou, A. Cichocki, and F. Lotte, “Modern machine learning algo-
rithms to classify cognitive and affective states from electroencephalog-
raphy signals,” IEEE Systems, Man and Cybernetics Magazine, 2020.
[105] Z. Lan, O. Sourina, L. Wang, R. Scherer, and G. R. Muller-Putz,
“Domain adaptation techniques for EEG-based emotion recognition: A
comparative study on two public datasets,” IEEE Trans. on Cognitive
and Developmental Systems, vol. 11, no. 1, pp. 85–94, 2019.
[106] S. J. Pan, I. W. Tsang, J. T. Kwok, and Q. Yang, “Domain adaptation
via transfer component analysis,” IEEE Trans. on Neural Networks,
vol. 22, no. 2, pp. 199–210, 2010.
[107] K. Yan, L. Kou, and D. Zhang, “Learning domain-invariant subspace
using domain features and independence maximization,” IEEE Trans.
on Cybernetics, vol. 48, no. 1, pp. 288–299, 2018.
[108] Y. Lin, “Constructing a personalized cross-day EEG-based emotion-
classiﬁcation model using transfer learning,” IEEE Journal of Biomed-
ical and Health Informatics, 2020, in press.
[109] W.-L. Zheng, Z.-F. Shi, and B.-L. Lu, “Building cross-subject EEG-
based affective models using heterogeneous transfer learning,” Chinese
Journal of Computers, vol. 43, no. 2, pp. 177–189, 2020, in Chinese.
[110] S. Siddharth, T. Jung, and T. J. Sejnowski, “Utilizing deep learning to-
wards multi-modal bio-sensing and vision-based affective computing,”
IEEE Trans. on Affective Computing, 2020, in press.
[111] M. Soleymani, J. Lichtenauer, T. Pun, and M. Pantic, “A multimodal
database for affect recognition and implicit tagging,” IEEE Trans. on
Affective Computing, vol. 3, no. 1, pp. 42–55, 2012.
[112] Y. Cimtay and E. Ekmekcioglu, “Investigating the use of pretrained
convolutional neural network on cross-subject and cross-dataset EEG
emotion recognition,” Sensors, vol. 20, no. 7, p. 2034, 2020.
[113] W.-L. Zheng, K. Gao, G. Li, W. Liu, C. Liu, J.-Q. Liu, G. Wang,
and B.-L. Lu, “Vigilance estimation using a wearable EOG device in
real driving environment,” IEEE Trans. on Intelligent Transportation
Systems, vol. 21, no. 1, p. 170184, 2020.
[114] D. Wu, C.-H. Chuang, and C.-T. Lin, “Online driver’s drowsiness
estimation using domain adaptation with model fusion,” in Proc. Int’l
Conf. on Affective Computing and Intelligent Interaction, Xi’an, China,
September 2015, pp. 904–910.
[115] C.-S. Wei, Y.-P. Lin, Y.-T. Wang, C.-T. Lin, and T.-P. Jung, “A subject-
transfer framework for obviating inter-and intra-subject variability in
EEG-based drowsiness detection,” NeuroImage, vol. 174, pp. 407–419,
2018.
[116] L.-L. Chen, A. Zhang, and X.-G. Lou, “Cross-subject driver status
detection from physiological signals based on hybrid feature selection
and transfer learning,” Expert Systems with Applications, vol. 137, pp.
266–280, 2019.

16
[117] H. Peng, F. Long, and C. Ding, “Feature selection based on mu-
tual information criteria of max-dependency, max-relevance, and min-
redundancy,” IEEE Trans. on Pattern Analysis and Machine Intelli-
gence, vol. 27, no. 8, pp. 1226–1238, 2005.
[118] Y. Ming, D. Pelusi, C.-N. Fang, M. Prasad, Y.-K. Wang, D. Wu,
and C.-T. Lin, “EEG data analysis with stacked differentiable neural
computers,” Neural Computing and Applications, 2018.
[119] C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. J.
Goodfellow, and R. Fergus, “Intriguing properties of neural networks,”
in Proc. Int’l Conf. on Learning Representations, Banff, Canada, Apr.
2014.
[120] P. Aric`o, G. Borghini, G. Di Flumeri, N. Sciaraffa, and F. Babiloni,
“Passive BCI beyond the lab: current trends and future directions,”
Physiological Measurement, vol. 39, no. 8, p. 08TR02, 2018.
