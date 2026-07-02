# Different Set Domain Adaptation for BrainComputer Interfaces: A Label Alignment Approach

He He and Dongrui Wu

arXiv:1912.01166v4[cs.HC]10Mar2020

Abstract—A brain-computer interface (BCI) system usually needs a long calibration session for each new subject/task to adjust its parameters, which impedes its transition from the laboratory to real-world applications. Domain adaptation, which leverages labeled data from auxiliary subjects/tasks (source domains), has demonstrated its effectiveness in reducing such calibration effort. Currently, most domain adaptation approaches require the source domains to have the same feature space and label space as the target domain, which limits their applications, as the auxiliary data may have different feature spaces and/or different label spaces. This paper considers different set domain adaptation for BCIs, i.e., the source and target domains have different label spaces. We introduce a practical setting of different label sets for BCIs, and propose a novel label alignment (LA) approach to align the source label space with the target label space. It has three desirable properties: 1) LA only needs as few as one labeled sample from each class of the target subject; 2) LA can be used as a preprocessing step before different feature extraction and classiﬁcation algorithms; and, 3) LA can be integrated with other domain adaptation approaches to achieve even better performance. Experiments on two motor imagery datasets demonstrated the effectiveness of LA.

Index Terms—Brain-computer interface, EEG, label alignment, Riemannian geometry, domain adaptation, transfer learning

I. INTRODUCTION

A brain-computer interface (BCI) system [1], [2] acquires the brain signal, decodes it, and then translates it into control commands for external devices, so that a user can interact with his/her surroundings using thoughts directly, bypassing the normal pathway of peripheral nerves and muscles. Electroencephalogram (EEG) may be the most popular BCI input signal due to its convenience, safety, and low cost. The pipeline for decoding EEG signals usually involves:

- 1) Signal processing, which includes band-pass ﬁltering and spatial ﬁltering. Bandpass ﬁltering reduces interferences and noise such as muscle artifacts, eye blinks, and DC drift. Spatial ﬁltering combines different EEG channels to increase the signal-to-noise ratio. Common spatial patterns (CSP) [3]–[6] may be the most frequently used spatial ﬁltering approach.
- 2) Feature extraction. Different features, e.g., time domain, frequency domain, time-frequency domain, Riemannian space, could be used.

He He and Dongrui Wu are with the Ministry of Education Key Laboratory of Image Processing and Intelligent Control, School of Artiﬁcial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan, China. Email: hehe91@hust.edu.cn, drwu@hust.edu.cn.

Dongrui Wu is the corresponding author.

3) Classiﬁcation. Popular classiﬁers include linear discriminant analysis (LDA) and support vector machine (SVM).

Recently, Barachant et al. [7] proposed a novel preprocessing and classiﬁcation pipeline in the Riemannian space, which integrated spatial ﬁltering and feature extraction into one single step. This Riemannian pipeline uses the covariance matrices of the EEG trials, which are symmetric positive deﬁnite and lie on a Riemannian manifold [8]. The covariance matrices encode spatial information of the brain activities, which are useful in many BCI tasks. A popular classiﬁer in the Riemannian space, minimum distance to mean [7], treats the covariance matrices as points on the Riemannian manifold, and uses their Riemannian distances to the class mean for classiﬁcation. Another more sophisticated approach maps the covariance matrices from the Riemannian space to a Euclidean tangent space (TS) around the Riemannian mean, where the Riemannian space covariance matrices are transformed into Euclidean space vectors, and then used in Euclidean space classiﬁers as features.

Motor imagery [9] is one of the most frequently used paradigms of BCIs. It is based on the voluntary modulation of the sensorimotor rhythm, which does not need any external stimuli. The imagined movements of different body parts (e.g., hands, feet, and tongue) cause modulations of brain rhythms in the involved cortical areas. So, they can be distinguished by decoding such brain rhythm modulations, and used to control external devices such as powered exoskeletons, wheelchairs, and robots.

Motor imagery-based BCIs were originally designed to help those with neuromuscular impairments [10]. Recent research has extended its application scope to able-bodied users [11], [12]. However, EEG signals are very weak, and easily contaminated by interferences and noise. Moreover, individual differences make it difﬁcult, if not impossible, to build a generic machine learning model optimal for all subjects. Usually a calibration session is needed to collect some subjectspeciﬁc data for a new subject, which is time-consuming and user-unfriendly.

Researchers have proposed many different approaches [13]– [20] to reduce this calibration effort. One of them is transfer learning [21], or domain adaptation (DA). Its main idea is to leverage the data from auxiliary subjects (called source subjects or source domains) to improve the learning performance for a new subject (called target subject or target domain). A popular idea in DA is to project the source domain and target domain data into low dimensional subspaces where the geometrical shift or/and distribution shift are reduced, such

as joint distribution adaptation (JDA) [22], joint geometrical and statistical alignment (JGSA) [23], and manifold embedded distribution alignment (MEDA) [24]. Computational intelligence techniques have also been used in transfer learning,

- as reviewed by Lu et al. [25]. In BCIs, Zanini et al. [26] proposed a Riemannian geometry framework to align EEG covariance matrices from different subjects in the Riemannian space. Recently, we [27] proposed a Euclidean alignment (EA) approach, which can be used as a preprocessing step before many Euclidean space feature extraction and pattern recognition algorithms.

However, most existing DA approaches assume that the source domains have the same feature space and label space as the target domain, which may not hold in many real-world applications. There have been some heterogenous feature space DA approaches [14], [28], [29], which address the problem that the source domains have different feature spaces from the target domain. For example, in BCIs, Wu et al. [14] performed transfer learning for heterogenous feature spaces: the source and target EEG trials are collected from different EEG headsets, with different numbers of channels and channel locations. Its main idea is to select the source domain channels closest to the target domain channels.

There have also been a few heterogeneous label space DA approaches [30]–[33], as shown in Fig. 1. Busto et al. [30] ﬁrst proposed the concept of open set DA, assuming the source and target domains have some known classes in common, and also some classes that are different and unknown. Saito et al. [31] considered the case that the target domain contains all classes in the source domain, plus an “unknown” class (different from [30], herein the source domain does not contain an “unknown” class). You et al. [33] proposed universal DA, which classiﬁes a target domain sample if it belongs to any known class in the source domain, or marks it as “unknown” otherwise. In summary, both open set DA and universal DA train a model to either classify a target domain sample into a known class which has appeared in the source domain, or mark it as “unknown”. An application scenario of open set DA and universal DA is face recognition, where some test samples may not appear in the training database and have to be marked

- as “unknown”. This paper considers different set DA in BCIs, i.e., the

source domains have different label spaces from the target domain, as shown in Fig. 1. For Motor imagery-based BCIs, this means the source subjects and the target subject perform different motor imagery tasks. To our knowledge, no one has studied this problem before.

To address this issue, we propose a label alignment (LA) approach to align EEG covariance matrices of the source subjects to those of the target subject. It ﬁrst matches each source domain label with a target domain label, then moves the per-class covariance matrices of each source subject to re-center them at the corresponding class means of the target subject. After LA, the distribution discrepancies between the source and the target subjects are reduced, so that a model trained on source subjects can classify each target trial into the category it actually belongs to, even though the source and target subjects have completely different label spaces.

[Figure 1]

Fig. 1. Different DA scenarios. A, B, ...,H represent different classes. Xs and Xt are unknown classes in the source domain and the target domain, respectively. In closed set DA, the source domain and target domain have the same classes. In partial DA, the target domain only contains a subset of the source domain classes. In open set DA considered in [30], the source and target domains contain some common classes, but each also contains an “unknown” class. In open set DA considered in [31], the source domain only contains a subset of the target domain classes. In universal DA [33], the target domain may contain some common classes as the target domain, but may also contain some unknown classes. In different set DA considered in this paper, the target domain contains partially or completely different classes from the source domain.

The main contributions of this paper are:

- 1) We introduce a practical setting of different set DA in BCIs: The source and target domains have known and different label sets; we need to classify each target trial into the category it actually belongs to, with the help of the source domain data. This setting is different from existing open set DA and universal DA. To our knowledge, it has not been studied before.
- 2) We propose an effective LA approach for different set DA in BCIs, which has three desirable properties: 1) It only needs as few as one labeled EEG trial from each class of the target subject; 2) It can be used as a preprocessing step in different feature extraction and classiﬁcation algorithms; and, 3) It can be integrated with other DA approaches to achieve even better performance.

The remainder of this paper is organized as follows: Section II introduces related background knowledge on the Riemannian space and the EA. Section III proposes the LA. Section IV introduces the datasets used in our experiments. Sections V compares the performance of LA with several other DA approaches. Finally, Section VI draws conclusions and points out some future research directions.

II. RELATED WORK

This section introduces some basic concepts of the Riemannian space and its TS, and the EA, a state-of-the-art data alignment approach for BCIs, which also motivated our proposed LA.

- A. Riemannian Distance

Each symmetric positive deﬁnite matrix can be viewed as a point on a Riemannian manifold. The Riemannian distance between two symmetric positive deﬁnite matrices P1 and P2 is the length of the geodesic, deﬁned as the minimum length curve connecting P1 and P2 on the Riemannian manifold:

δ(P1,P2) = log(P1−1P2) F=

R

r=1

log2 λr

- 1

[Figure 2]

- 2

, (1)

where the subscript F denotes the Frobenius norm, and λr (r = 1,2,...,R) are the real eigenvalues of P1−1P2.

δ(P1,P2) remains unchanged under linear invertible transformations:

δ(WTP1W,WTP2W) = δ(P1,P2), (2)

where W is an invertible matrix. This property, called congruence invariance, is useful in both EA and LA.

- B. Tangent Space (TS) Mapping

Most machine learning approaches are applicable only in the Euclidean space, and cannot be used in the Riemannian space. TS mapping maps the covariance matrices from the Riemannian space to a Euclidean TS, so that they can be used by a Euclidean space classiﬁer.

For each point P on the Riemannian manifold, the TS can be deﬁned by a set of tangent vectors at P. Each tangent vector Si is deﬁned as the derivative at t = 0 of the geodesic between P and the exponential mapping Pi = ExpP(Si):

ExpP(Si) = Pi = P The inverse mapping is given by the logarithmic mapping:

- 1

[Figure 3]

- 2 exp(P−

- 1

[Figure 4]

- 2SiP−

- 1

[Figure 5]

- 2 )P

- 1

[Figure 6]

- 2. (3)

LogP(Pi) = Si = P

- 1

[Figure 7]

- 2 log(P−

- 1

[Figure 8]

- 2PiP−

- 1

[Figure 9]

- 2)P

- 1

[Figure 10]

- 2. (4)

TS mapping converts each 2D EEG trial into a 1D feature vector, so that many machine learning algorithms can be used.

- C. Euclidean Alignment (EA)

EA [27], [34] is a state-of-the-art DA approach for BCIs, which reduces the individual differences by aligning the EEG covariance matrices.

Some DA approaches [14], [22] ﬁrst ﬁnd a proper discrepancy measure between different distributions, then learn a shared subspace where the distribution discrepancy is explicitly minimized. Maximum mean discrepancy [35] is a popular distribution discrepancy measure, which is deﬁned as the distance between the mean feature embeddings of different distributions.

Similar to these maximum mean discrepancy based DA approaches, EA views the covariance matrices as the feature embeddings of different EEG trials, and ﬁnds projections to minimize the distance between the mean covariance matrices of different subjects.

For a subject with N trials {Xi}Ni=1 (each row of Xi is an EEG channel), EA ﬁrst computes the individual covariance matrices

Ci = XiXiT, i = 1,2,...,N (5)

and the mean covariance matrix

N

1 N

C¯ =

[Figure 11]

i=1

Ci. (6)

The projection matrix for the subject is then

R = C¯−1/2. (7) Finally, EA performs the following projection for each trial:

X˜i = RXi, i = 1,2,...,N. (8)

After EA, the mean covariance matrix of the subject becomes an identity matrix:

N

N

1 N

1 N

X˜iX˜iT =

RXiXiTR

[Figure 12]

[Figure 13]

i=1

i=1

N

1 N

XiXiT C ¯−1/2

= C¯−1/2

[Figure 14]

i=1

= C¯−1/2C¯C¯−1/2 = I. (9)

After performing EA for all subjects, they share the same mean covariance matrix, i.e., the distances between the mean covariance matrices of different subjects are minimized (they become zero), and hence data distributions from different subjects become more similar.

We can also understand EA as a correction of data shift. If we view each EEG covariance matrix as a point on a Riemannian manifold, then individual differences cause shifts of these points, although they may entail more than just a simple displacement [26]. In order to correct this shift, EA moves the covariance matrices of each subject to center them at the identity matrix. The congruence invariance property makes sure that the distances among the within-subject covariance matrices remain unchanged. So, EA makes the data distributions from different subjects closer, while preserving the local distance information of each subject.

III. LABEL ALIGNMENT (LA) FOR DIFFERENT SET DA

This section introduces our proposed LA for different set DA, and discusses its relationship with EA and CORAL [36].

A. LA

Generally, there are three types of data shift in transfer learning:

- 1) Covariate shift [37], [38]: the distributions of the inputs (features) are different.
- 2) Prior probability shift: the distributions of the output are different.
- 3) Concept shift [39]: the relationships between the inputs and the output are different.

EA considers only the covariate shift but ignores the other two. Although it has been shown to signiﬁcantly improve the cross-subject classiﬁcation performance in [27], it only aligns the data in the feature space, and may not work well when the source subjects and the target subject have different label spaces.

This section proposes LA, which extends EA to different label spaces, by simultaneously considering multiple types of data shift. Its main idea is to independently move the per-class covariance matrices of each source subject, to re-center them

- at the corresponding class center of the target subject. More speciﬁcally, for an M-class classiﬁcation problem, we

assume the source and target subjects have the same number of classes, but their class labels are partially or completely different. Our goal is to use the source data to help the classiﬁcation of the target trials. LA seeks a transformation matrix Am for the trials of the m-th class (m = 1,2,··· ,M) from the source subject, such that the distance between the mean covariance matrices of the corresponding class in different domains are minimized:

||AC¯S,mAT − C¯T,m||2F, m = 1,2,··· ,M.

Am = arg min

A

(10)

where C¯S,m is the mean covariance matrix of the m-th class of the source subject, and C¯T,m the mean covariance matrix of the m-th class of the target subject. In this paper, we use the Log-Euclidean mean [40], which is frequently used for symmetric positive deﬁnite matrices and much easier to compute than the Riemannian mean.

We adopt the optimization approach in [36] to solve for Am in (10):

- 1

[Figure 15]

- 2

- 1

[Figure 16]

- 2

T,mC¯−

Am = C¯

S,m, m = 1,2,··· ,M. (11) Then, each trial Xj of the source subject is transformed to:

X˜j = AmXj, if Xj ∈ Class m (12)

The difference between the mean covariance matrices of the corresponding class between the transformed source subject and the target subject becomes

1 2

- 1

[Figure 17]

- 2

- 1

[Figure 18]

- 2

1 2

S,mC¯S,mC¯−

T,mC¯−

S,mC¯

T,m − C¯T,m

AC¯S,mAT − C¯T,m = C¯

[Figure 19]

[Figure 20]

- 1

[Figure 21]

- 2

- 1

[Figure 22]

- 2

T,m − C¯T,m = 0, (13) where 0 is an all-zero matrix, i.e., the objective function in

T,mIC¯

= C¯

(10) is minimized.

- A key question in LA is how to obtain C¯T,m, which

requires some labeled target domain samples. We consider the following ofﬂine classiﬁcation scenario: we have access to the unlabeled EEG trials (the same assumption is also used in EA), and we can label a few of them to estimate C¯T,m. To have a good estimate of C¯T,m from only a few labeled trials, we need to select these trials very carefully. In this paper, we perform kmedoids clustering based on the Riemannian distances among the target EEG trials, label the k cluster centers, and then estimate C¯T,m from them. In the rare case that the k centers had fewer than M different labels, we use EA to replace LA.

Another question is how we match the source labels with the target labels. When the source and target label sets partially overlap, for the labels in common, we match each source label with the same target label, and then randomly match each remaining source label with a remaining target label. For example, if the source label set is {A,B,C} and the target label set is {A,D,E}, then we match source label A with

target label A, source label B with target label D (or E), and source label C with target label E (or D). If the source and target label sets are completely different, we randomly match the source and target labels.

The pseudo-code of LA is shown in Algorithm 1. We perform LA for each source subject separately if there are multiple source subjects. After LA, the source domain and the target domain have the same label set, and the trials in the same class are aligned. Then, trials from the two domains can be combined directly for feature extraction and classiﬁcation. Or, an additional DA approach can be applied after LA to further improve the transfer learning performance, as shown in Section V.

[Figure 23]

Algorithm 1: LA for different set domain adaptation. Input: {Xj,yj}N

[Figure 24]

S

j=1, labeled source domain trials;

- {yS,m}Mm=1, label set of the source domain;

{Xi}N

T

i=1, unlabeled target domain trials;

- {yT,m}Mm=1, label set of the target domain; k, number of target domain trials to be labeled.

Output: { Xj, yj}N

S

j=1, aligned source domain trials. Compute the target domain covariance matrices {Ci}N

T

i=1

by (5); Perform k-medoids clustering on {Ci}N

T

i=1 using the

Riemannian distance; Label the k medoids; Compute C¯T,m (m = 1,2,...,M), the mean covariance matrix of each target domain class from the k labeled medoids;

Compute C¯S,m (m = 1,2,··· ,M), the mean covariance matrix of each source domain class; Match each source domain label with a target domain label; assume yS,m is matched with yT,m;

for m = 1,2,...,M do Compute Am by (11); Compute { Xj}N

[Figure 25]

j=1 by (12) and set yj = yT,m, ∀jyj = yS,m;

S

end Return { Xj, yj}N

S

j=1

[Figure 26]

B. LA versus EA

The difference between LA and EA is illustrated in Fig. 2. For clarity, binary classiﬁcation is used, but both EA and LA can be easily extended to multi-class classiﬁcation, as shown later in this paper. In Fig. 2, each EEG trial is represented by its covariance matrix, as a point on a Riemannian manifold. The source domain (blue points) and target domain (black points) represent two different subjects, who have trials from different motor imagery tasks (indicated by different shapes of the points. Note that the shapes in the target domain are only used to help understand our approach, but not to suggest that we need to know all target labels). Initially, the source and target domains scatter far away from each other, due to the domain gap and also the category gap. If we build a classiﬁer on the source domain (indicated by the red dashed line) and

apply it directly to the target domain, it may not work at all. EA and LA alleviate this problem by reducing the gaps between the two domains before classiﬁcation:

[Figure 27]

- Fig. 2. Illustration of EA and LA.

- 1) EA focuses on the domain gap but ignores the category gap completely. It ﬁrst computes the mean covariance matrix of each domain (indicated by the red stars), from which a transformation matrix of each domain is computed. Using the transformation matrix, EA then recenters each domain at the identity matrix, and makes the source and target domains overlap with each other, i.e., the domain gap between them is reduced. If we build a classiﬁer in the source domain (the red dashed line) and apply it to the target domain, the classiﬁcation performance would be improved.
- 2) LA considers the domain gap and the category gap simultaneously. It ﬁrst computes the mean covariance matrix of each source domain class (indicated by the red circle and the red diamond), and estimates the mean covariance matrix of each target domain class (indicated by the red triangle and the red square). Then, LA recenters each source domain class at the corresponding estimated class mean of the target domain. If we build a classiﬁer in the source domain (the red dashed line) and apply it to the target domain, the classiﬁcation performance would be further improved.

C. LA versus CORrelation ALignment (CORAL)

Sun et al. [36] proposed an unsupervised DA approach, CORrelation ALignment (CORAL), to minimize the domain shift by aligning the second-order statistics of different distributions.

Given a source domain DS ∈ RNS×d and a target domain DT ∈ RNT×d, where NS and NT are the number of trials in the source domain and the target domain, respectively, and d the feature dimensionality. CORAL ﬁrst computes the feature covariance matrix CS ∈ Rd×d in the source domain and CT ∈ Rd×d in the target domain. Then, it ﬁnds a linear transformation matrix A ∈ Rd×d for the source domain features, so that the Frobenius norm of the difference between the covariance matrices of the two domains is minimized, i.e.,

||ATCSA − CT||2F (14)

min

A

Although (14) seems similar to the objective function of LA in (10), they are different:

- 1) CORAL uses 1D features, and each domain has only one feature covariance matrix, which measures the covariances between different pairs of individual features. LA uses 2D features (EEG trials), and each EEG trial has a covariance matrix, which measures the covariances between different pairs of EEG channels. So, the covariance matrices in CORAL and LA have different meanings.
- 2) CORAL minimizes the distance between the covariance matrices in different domains, whereas LA minimizes the distance between the mean covariance matrices of the corresponding class in different domains.
- 3) CORAL works when the source domain has the same class labels as the target domain, and it ﬁnds one transformation matrix for each source domain. LA considers the case that the source and target domains have different class labels (of course, it also works when the two domains have the same class labels), and it ﬁnds one transformation matrix for each class of the source domain.

In summary, LA and CORAL have different inputs, different optimization objectives, and also different application scenarios. When the source and target domains have the same class labels, each 2D EEG trial can be mapped from the Riemannian manifold to the tangent space to obtain a 1D feature vector, and hence be plugged into CORAL. However, CORAL cannot be used when the source and target domains have different labels.

IV. DATASETS

This section describes and visualizes the two motor imagery datasets used in our experiments.

A. Datasets and Preprocessing

Both datasets were from BCI Competition IV1, and were collected in a cue-based setting. In each experiment, the subject was sitting in front of a computer and performed motor imagery tasks at the prompt of visual cues, as shown in Fig. 3. Each trial began when a ﬁxation cross appeared on the black screen (t = 0), which prompted the subject to be prepared. After a short period, an arrow pointing to a certain direction was displayed as the visual cue (t = 2). The cue was displayed for a few seconds, during which the subject was instructed to perform the desired motor imagery task according to the direction of the arrow. The subject stopped the motor imagery when the visual cue disappeared (t = 6). A short break followed, until the next trial began (t = 8).

The ﬁrst dataset2 (Dataset 1 [41]) was recorded from seven healthy subjects by 59 EEG channels at 100 Hz. Each subject was instructed to perform two classes of motor imagery tasks, which were selected from three options: left hand, right hand, and feet. The recording of each subject was divided into three sessions: calibration, evaluation, and special feature. This

- 1http://www.bbci.de/competition/iv/.
- 2http://www.bbci.de/competition/iv/desc 1.html.

[Figure 28]

[Figure 29]

shows two examples when the ﬁrst two subjects were used as the target subjects, respectively. The red and black dots are trials of Labels 2 and 3 from the target subject, respectively. The blue and green dots are trials of Labels 1 and 4 from the source subjects, respectively. The ﬁrst column shows the trials without alignment, the second column shows the trials after EA, and the third after LA.

- Fig. 3. Timing scheme of the motor imagery tasks.

paper only used the calibration data, because they included complete label information. Each subject had 100 trials from each class.

| |
|---|

The second dataset3 (Dataset 2a) was recorded from nine healthy subjects by 22 EEG channels and 3 EOG channels

- -40
- -20

0

20

Subject 1, raw

-40 -20 0 20

| |
|---|

- -40
- -20

0

20

Subject 1, after EA

-40 -20 0 20

| |
|---|

- -40
- -20

0

20

Subject 1, after LA

-20 0 20 40

| |
|---|

- -20

- at 250 Hz (we downsampled it to 100 Hz, to be consistent with Dataset 1). Each subject was instructed to perform four classes of motor imagery tasks: left hand, right hand, both feet, and tongue, which were represented by labels 1, 2, 3 and 4, respectively. A training session and an evaluation session were recorded on different days for each subject. We only used the 22-channel EEG data in the training session, which included complete label information. Each subject had 72 trials from each class, and 288 trials in total.

-40 -20 0 20

##### Subject 2, raw

##### Subject 2, after EA

##### Subject 2, after LA

40

40

40

| |
|---|

| |
|---|

20

20

20

0

0

0

-20

-20

-20 0 20 40

-20 0 20 40

For both datasets, the EEG signals were preprocessed using the Matlab EEGLAB toolbox [42], following the guideline in [43]. First, a causal band-pass ﬁlter (20-order linear phase Hamming window FIR ﬁlter designed by Matlab function ﬁr1, with 6dB cut-off frequencies at [8, 30] Hz) was applied to remove muscle artifacts, line-noise contamination and DC drift. Next, we extracted EEG signals between [0.5,3.5] seconds after the cue appearance as our trials.

Fig. 4. t-SNE visualization when the ﬁrst two subjects were used as the target subjects, respectively. Red dots: trials of Label 2 from the target subject; black dots: trials of Label 3 from the target subject; blue dots: trials of Label 1 from the source subjects; green dots: trials of Label 4 from the source subjects. The ﬁrst column shows the trials without alignment, the second column shows the trials after EA, and the third after LA.

Observe that trials from the source subjects (blue and green dots) are scattered far away from those of the target subject (red and black dots), when no alignment is performed. However, the target and source trials overlap with each other after EA, since their centers are now identical. After LA, the target and source trials are further aligned according to their labels. It’s clear that different classes are more distinguishable after LA.

Table I summaries the characteristics of the two datasets.

TABLE I SUMMARY OF THE TWO MOTOR IMAGERY DATASETS.

[Figure 30]

[Figure 31]

[Figure 32]

Number of Channels Time samples Subjects Classes Trials/class

[Figure 33]

[Figure 34]

[Figure 35]

- Data 1 59 300 7 2 100

[Figure 36]

[Figure 37]

- Data 2a 22 300 9 4 72

[Figure 38]

V. EXPERIMENTS AND RESULTS

[Figure 39]

- B. Data Visualization

In order to intuitively show how EA and LA reduce the distribution discrepancies between the target and source subjects, we ﬁrst projected the EEG covariance matrices from the Riemannian manifold into the tangent space, then used the 1D tangent vectors as features to represent the EEG trials, as introduced in Section II-B. Finally, we used t-stochastic neighbor embedding (t-SNE) [44], a technique for dimensionality reduction and high-dimensional dataset visualization, to display the EEG trials (tangent vectors) before and after EA/LA in 2D.

More speciﬁcally, we ﬁrst divided Dataset 2a into two datasets with different label spaces: the source dataset consisted of trials with Labels 1 and 4, and the target dataset with Labels 2 and 3. Then, we picked one subject from the target dataset as the target subject, and the remaining eight subjects from the source dataset as the source subjects. Fig. 4

3http://www.bbci.de/competition/iv/desc 2a.pdf.

[Figure 40]

This section presents performance comparisons of LA with other approaches on the two datasets. The code is available at https://github.com/hehe91/LA.

A. Domain Adaptation (DA) Scenarios

We investigated the problem that the source and target subjects have different label spaces, and considered the following ﬁve DA scenarios:

- 1) Scenario I-a: The source and target subjects have the same feature space and partially overlapping label spaces (binary classiﬁcation).
- 2) Scenario I-b: The source and target subjects have the same feature space and partially overlapping label spaces (multi-class classiﬁcation).
- 3) Scenario II-a: The source and target subjects have the same feature space and completely different label spaces (binary classiﬁcation).
- 4) Scenario II-b: The source and target subjects have the same feature space and completely different label spaces (multi-class classiﬁcation).

5) Scenario III: The source and target subjects have different feature spaces and also different label spaces.

For Scenarios I-a, I-b, II-a and II-b, in each experiment we divided Dataset 2a into two sub-datasets, a source dataset and a target dataset, such that they had the same feature space and different label spaces. Each sub-dataset was named by its label space, for example, sub-dataset “1, 2” consisted of trials with Labels 1 and 2 only, and sub-dataset “3, 4” consisted of trials with Labels 3 and 4 only. Then, “1, 2→3, 4” denotes the experiment that Sub-dataset “1, 2” was used as the source dataset and Sub-dataset “3, 4” the target dataset.

Then, the datasets used in the ﬁve DA scenarios were:

- 1) Scenario I-a: We divided Dataset 2a into a source subdataset and a target sub-dataset, ensuring they had one identical label and one different label. There were 24 such sub-dataset combinations in total, e.g., “1, 2→1, 3” and “1, 2→3, 2”.
- 2) Scenario I-b: We divided Dataset 2a into a source subdataset and a target sub-dataset, ensuring they had two identical labels and a different label. There were 12 such combinations in total, e.g., “1, 2, 3→1, 2, 4” and “1, 2, 3→1, 4, 3”.
- 3) Scenario II-a: We divided Dataset 2a into a source sub-dataset and a target sub-dataset, ensuring they had completely different labels. There were six such combinations in total, e.g., “1, 2→3, 4” and “2, 3→1, 4”.
- 4) Scenario II-b: We used the same sub-dataset combinations as in Scenario I-b, but mismatched the labels between the target and source subjects, e.g., “1, 2, 3→2, 1, 4” and “1, 2, 4→2, 1, 3”.
- 5) Scenario III: We used Dataset 1 as the source dataset and sub-dataset “3, 4” of Dataset 2a as the target dataset, so that they had different feature spaces (their EEG channels were different) and also different label spaces.

Once a dataset choice was made, each time we picked one subject from the target dataset as the target subject, and the remaining subjects from the source dataset as the source subjects. As the target dataset always had nine subjects, we had nine sub-experiments for each dataset combinations. Table II summaries the characteristics of all scenarios, where k is the number of labeled target subject trials.

TABLE II SUMMARY OF THE FOUR DA SCENARIOS, WHERE k IS THE NUMBER OF LABELED TARGET SUBJECT TRIALS.

[Figure 41]

[Figure 42]

No. of dataset No. of sub- No. of No. of combinations experiments training trials test trials

[Figure 43]

[Figure 44]

- Scenario I-a 24 24 × 9 144 × 8 + k 144 − k

[Figure 45]

- Scenario I-b 12 12 × 9 216 × 8 + k 216 − k

[Figure 46]

- Scenario II-a 6 6 × 9 144 × 8 + k 144 − k

[Figure 47]

- Scenario II-b 12 12 × 9 216 × 8 + k 216 − k Scenario III 1 9 1400 + k 144 − k

[Figure 48]

[Figure 49]

[Figure 50]

- B. Experimental Settings

We ﬁrst divided the BCI classiﬁcation pipeline into three stages:

- 1) Preprocessing, which ﬁrst temporally ﬁlters the EEG data, then epochs the continuous EEG signals into trials, as described in Section IV-A.
- 2) Alignment, which selectively performs different alignments.
- 3) Classiﬁcation, which extracts features and trains classiﬁers.

In order to emphasize the effect of LA, the algorithms to be compared consisted of the same preprocessing and classiﬁcation stages, but different alignments. More speciﬁcally, three alignment approaches were compared:

- 1) Raw, which did not perform any alignment.
- 2) EA, which performed EA.
- 3) LA, which performed LA.

In each scenario, the experiments were designed to answer the following two questions:

- Question 1: Can LA be used as an effective preprocessing step before different feature extraction and classiﬁcation algorithms?
- Question 2: Can LA be integrated with other DA approaches to further improve the classiﬁcation performance?

For Question 1, we used two feature extraction and classiﬁcation pipelines:

- 1) CSP-LDA: It spatially ﬁltered the EEG data by CSP, computed the log-variance as features, and then used them in an LDA classiﬁer.
- 2) TS-SVM: It extracted the Riemannian TS features, as introduced in Section II-B, then used them in an SVM classiﬁer.

Combining these two pipelines with the three alignment approaches (Raw, EA, LA), we had 2 × 3 = 6 algorithms to be compared. Our goal was to verify whether LA performs the best in both pipelines.

For Question 2, we ﬁrst extracted the Riemannian TS features, and then used different DA approaches in classiﬁcation stage (because they need 1D features):

- 1) BL (baseline), which directly applied an SVM classiﬁer to the TS features, without any additional DA approach.
- 2) JDA, which applied JDA to the TS features, and then used them in an SVM classiﬁer.
- 3) JGSA, which applied JGSA to the TS features, and then used them in an SVM classiﬁer.
- 4) MEDA, which applied MEDA to the TS features.

Combining these four approaches with the three alignments (Raw, EA, LA), we had 4 × 3 = 12 algorithms to be compared. Our goal was to verify whether “LA+JDA/JGSA/MEDA>LA+BL>Raw+JDA/JGSA/MEDA”, where “>” means “outperform”. For example, “LA+BL>Raw+JDA/JGSA/MEDA” means LA outperforms classical DA approaches such as JDA, JGSA and MEDA, and “LA+JDA/JGSA/MEDA>LA+BL” means the performance could be further improved by integrating LA with other DA approaches, i.e., LA is compatible with and complementary to other DA approaches.

- C. Scenario I-a: Same Feature Space and Partially Overlapping Label Spaces in Binary Classiﬁcation

This subsection considers the binary classiﬁcation scenario that the source and target subjects have the same feature space and partially overlapping label spaces. As introduce in Section V-A, we had 24 sub-dataset combinations to be tested.

Because in Scenario I-a the source subjects had one identical label and one different label from the target subject, we ﬁrst matched the identical label, then the remaining labels. For example, in the combination “1, 2 → 1, 3”, we matched source Label 1 with target Label 1, and source Label 2 with target Label 3. For algorithms without LA, we directly assigned Label 3 to the source trials with Label 2. For algorithms with LA, we ﬁrst aligned the source Label 1 trials with the target Label 1 trials, then aligned the source Label 2 trials with the target Label 3 trials, and assigned Label 3 to the source trials of Label 2.

For algorithms involving LA, we considered k ∈ {2,4,...,20} in k-medoids clustering of LA in Section III. In the rare case that the labeled target trials came from the same class, we cannot perform LA as there was not enough information to estimate the two class means of the target subject; thus, we performed EA instead of LA. No matter whether the labeled target trials were used in the alignment or not, they were always combined with the labeled source trials for feature extraction and classiﬁcation. All labeled target subject trials were excluded from the test set, so all algorithms had the same training set and test set.

- Question 1: Can LA be used as an effective preprocess-

ing step before different feature extraction and classiﬁcation algorithms?

We compared Raw, EA, and LA in the two classiﬁcation pipelines to answer this question. Fig. 5 shows the performances of the six algorithms on the 24 different subdataset combinations, where each subﬁgure shows the average accuracies across the nine subjects (each as the target subject once). The last subﬁgure shows the average performances across the 24 experiments. Observe that:

- 1) EA-CSP-LDA outperformed Raw-CSP-LDA on 20 out of the 24 experiments, and EA-TS-SVM outperformed Raw-TS-SVM on 14 out of the 24 experiments. On average EA-CSP-LDA outperformed Raw-CSP-LDA, and EA-TS-SVM outperformed Raw-TS-SVM. This suggests EA was generally effective, but not always, when the source and target label spaces were different.
- 2) When k became large, LA-CSP-LDA outperformed Raw-CSP-LDA in all 24 experiments, and LA-TS-SVM also outperformed Raw-TS-SVM in all 24 experiments. These suggest that LA was able to cope well with partially different label spaces.
- 3) When k became large, LA-CSP-LDA outperformed EACSP-LDA on all 24 experiments, and LA-TS-SVM also outperformed EA-TS-SVM on all 24 experiments. This suggests LA was more effective and robust than EA.
- 4) Generally, the classiﬁcation accuracies of LA-CSP-LDA and LA-TS-SVM increased when there were more labeled target trials for estimating the class means, which

is intuitive.

We also performed statistical tests to determine if the differences between the LA-based algorithms and others were statistically signiﬁcant. We ﬁrst deﬁned an aggregated performance measure called the area under the curve (AUC). For a particular algorithm on a particular subject, the AUC was the area under its accuracy curve when the number of labeled target subject trials increased from 2 to 20. Subjects from all 24 experiments were concatenated, so we had 24 × 9 = 216 subjects in total. Each algorithm had 216 AUCs. We then performed paired t-tests on these AUCs. The null hypothesis was that the difference between the paired samples has zero mean, which was rejected if p < α, where α = 0.05 was used. The results are shown in Table III, where the statistically signiﬁcant ones are marked in bold. LA-CSP-LDA signiﬁcantly outperformed EA-CSP-LDA, and LA-TS-SVM signiﬁcantly outperformed EA-TS-SVM. These results echo the observations from Fig. 5 and answer Question 1: LA can be used as an effective preprocessing step before different feature extraction and classiﬁcation algorithms.

TABLE III SCENARIO I-A: p-VALUES OF PAIRED t-TESTS ON THE AUCS OF THE CLASSIFICATION ACCURACY CURVES IN FIG. 5. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 51]

[Figure 52]

EA-CSP-LDA EA-TS -SVM LA-CSP-LDA 0.0000

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

LA-TS-SVM 0.0000

[Figure 57]

Question 2: Can LA be integrated with other DA approaches to further improve the clssiﬁcation performance?

As introduced in previous subsection, we had 12 algorithms to be compared. We used the same target and source subjects as introduced in Question 1, which resulted in 24 experiments again. Fig. 6 shows the performances of the 12 algorithms in the 24 experiments, where each subﬁgure shows the average accuracies across the nine subjects, and the last subﬁgure shows the average performances across the 24 experiments.

Observe that:

- 1) When k was large, LA-BL always outperformed RawBL and EA-BL, LA-JDA always outperformed RawJDA and EA-JDA, LA-JGSA always outperformed RawJGSA and EA-JGSA, and LA-MEDA always outperformed Raw-MEDA and EA-MEDA. These suggest that LA was effective regardless of whether additional DA approaches were used or not.
- 2) LA-BL always outperformed Raw-JDA and RawMEDA, and outperformed Raw-JGSA in 23 out of 24 experiments. These suggest that LA can outperform classical DA approaches such as JDA, JGSA and MEDA.
- 3) Both LA-JDA and LA-MEDA always outperformed LABL, and LA-JGSA outperformed LA-BL in 23 out of the 24 experiments. These suggest that it may be advantageous to integrate other DA approaches with LA.

We also performed paired t-tests on the AUCs in Fig. 6. The results are shown in Table IV, which indicate that the algorithms involving LA (i.e., LA-BL, LA-JDA, LA-JGSA, LA-MEDA) signiﬁcantly outperformed those involving EA

80

80

80

80

80

| |
|---|

| |
|---|

| |
|---|

70

70

70

70

70

60

60

60

60

60

50

50

50

50

50

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

80

80

80

80

80

| |
|---|

| |
|---|

| |
|---|

70

70

70

70

70

60

60

60

60

60

50

50

50

50

50

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

80

80

80

80

80

| |
|---|

| |
|---|

| |
|---|

70

70

70

70

70

60

60

60

60

60

50

50

50

50

50

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

80

80

80

80

80

| |
|---|

| |
|---|

| |
|---|

70

70

70

70

70

60

60

60

60

60

50

50

50

50

50

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

#### Average

75

80

80

80

80

| |
|---|

| |
|---|

| |
|---|

70

70

70

70

70

65

60

60

60

60

60

50

50

50

50

55

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

2 8 14 20

|Raw-CSP-LDA Raw-TS-SVM EA-CSP-LDA EA-TS-SVM LA-CSP-LDA LA-TS-SVM<br><br>|
|---|

- Fig. 5. Average classiﬁcation accuracies (%) in Scenario I-a. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

(i.e., EA-JDA, EA-JGSA, EA-MEDA), and the algorithms combining LA and additional DA approaches (i.e., LA-JDA, LA-JGSA, LA-MEDA) signiﬁcantly outperformed LA-BL. These results echo the observations from Fig. 6 and answer

- Question 2: LA can not only outperform EA and classical DA approaches, but the classiﬁcation performance can be further improved when integrated with other DA approaches.

- D. Scenario I-b: Same Feature Space and Partially Overlapping Label Spaces in Multi-Class Classiﬁcation

This subsection considers the multi-class classiﬁcation scenario that the source and target subjects have the same feature

TABLE IV SCENARIO I-A: p-VALUES OF PAIRED t-TESTS ON THE AUCS OF THE CLASSIFICATION ACCURACY CURVES IN FIG. 6. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 58]

[Figure 59]

LA-BL EA-JDA EA-JGSA EA-MEDA LA-BL 0.0000 0.0000 0.0000

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

LA-JDA 0.0000 0.0000 LA-JGSA 0.0001 0.0000 LA-MEDA 0.0000 0.0000

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

space and partially overlapping label spaces. As introduced in Section V-A, we had 12 sub-dataset combinations to be tested.

| |
|---|

80

80

80

80

80

60

60

60

60

60

40

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

| |
|---|

| |
|---|

| |
|---|

80

80

80

80

80

60

60

60

60

60

40

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

| |
|---|

| |
|---|

| |
|---|

| |
|---|

80

80

80

80

80

60

60

60

60

60

40

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

| |
|---|

80

80

80

80

80

60

60

60

60

60

40

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

## Average

| |
|---|

75

80

80

80

80

70

60

60

60

60

65

60

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

5 10 15 20

|Raw-BL<br><br>Raw-JDA<br><br>Raw-JGSA<br><br>Raw-MEDA<br><br>EA-BL<br><br>EA-JDA<br><br>EA-JGSA<br><br>EA-MEDA<br><br>LA-BL<br><br>LA-JDA<br><br>LA-JGSA<br><br>LA-MEDA|
|---|

- Fig. 6. Average classiﬁcation accuracies (%) in Scenario I-a, when additional DA approaches were used after LA. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

Question 1: Can LA be used as an effective preprocessing step before different feature extraction and classiﬁcation algorithms?

Again, we compared Raw, EA, and LA in the two classiﬁcation pipelines to answer this question. CSP ﬁltering was extended from binary classiﬁcation to multi-class classiﬁcation by the one-versus-the-rest approach [45]. As we had three class centers of the target subject to be estimated in LA, we considered k ∈ {3,6,...,30} in k-medoids clustering.

Fig. 7 shows the performances of the six algorithms on the 12 different sub-dataset combinations, where each subﬁgure

shows the average classiﬁcation accuracies across the nine subjects (each as the target subject once). The last subﬁgure shows the average performances across the 12 experiments. LA-CSP-LDA always outperformed Raw-CSP-LDA and EACSP-LDA, and LA-TS-SVM always outperformed Raw-TSSVM and EA-TS-SVM. These suggest that LA was effective with different feature extraction and classiﬁcation algorithms.

Paired t-tests on the AUCs in Fig. 7 were also performed to check if the differences between different algorithms were statistically signiﬁcant. Here the AUC was the area under the accuracy curve when the number of labeled target subject trials

70

70

70

70

70

| |
|---|

| |
|---|

| |
|---|

| |
|---|

60

60

60

60

60

50

50

50

50

50

40

40

40

40

40

10 20 30

10 20 30

10 20 30

10 20 30

10 20 30

70

70

70

70

70

| |
|---|

| |
|---|

| |
|---|

60

60

60

60

60

50

50

50

50

50

40

40

40

40

40

10 20 30

10 20 30

10 20 30

10 20 30

10 20 30

### Average

70

70

| |
|---|

| |
|---|

| |
|---|

60

|Raw-CSP-LDA<br><br>Raw-TS-SVM EA-CSP-LDA EA-TS-SVM<br><br>LA-CSP-LDA<br><br>LA-TS-SVM|
|---|

60

60

55

50

50

50

45

40

40

40

10 20 30

10 20 30

10 20 30

- Fig. 7. Average classiﬁcation accuracies (%) in Scenario I-b. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

increased from 3 to 30. Each algorithm had 12 × 9 = 108 AUCs. The results are shown in Table V, which indicate that LA-CSP-LDA signiﬁcantly outperformed EA-CSP-LDA, and LA-TS-SVM signiﬁcantly outperformed EA-TS-SVM.

TABLE V SCENARIO I-B: p-VALUES OF PAIRED t-TESTS ON THE AUCS OF THE CLASSIFICATION ACCURACY CURVES IN FIG. 7. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 69]

[Figure 70]

EA-CSP-LDA EA-TS-SVM LA-CSP-LDA 0.0196

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

LA-TS-SVM 0.0010

[Figure 75]

Question 2: Can LA be integrated with other DA approaches to further improve the classiﬁcation performance?

Again, we combined Raw, EA, LA with different DA approaches and obtained 12 algorithms to be compared. Fig. 8 shows their performances on the 12 sub-dataset combinations, and the average across the 12 experiments. Observe that:

- 1) When k was large, LA-BL always outperformed RawBL and EA-BL, LA-JDA always outperformed RawJDA and EA-JDA, LA-JGSA always outperformed RawJGSA and EA-JGSA, and LA-MEDA always outperformed Raw-MEDA. These suggest that LA was effective regardless of whether additional DA approaches were used or not.
- 2) When k was large, LA-BL outperformed Raw-JDA, Raw-JGSA and Raw-MEDA in all 12 experiments, sug-

gesting that LA can outperform classical DA approaches such as JDA, JGSA and MEDA.

3) Generally, LA-JDA, LA-JGSA and LA-MEDA outperformed LA-BL, suggesting that it may be advantageous to integrate additional DA approaches with LA.

Table VI shows the results of paired t-tests on the AUCs in Fig. 8. The conclusions in binary classiﬁcation still hold in multi-class classiﬁcation: LA signiﬁcantly outperformed EA and classical DA approaches, and its performance can be further signiﬁcantly improved when integrated with other DA approaches.

TABLE VI SCENARIO I-B: p-VALUES OF PAIRED t-TESTS ON THE AUCS IN FIG. 8. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 76]

[Figure 77]

LA-BL EA-JDA EA-JGSA EA-MEDA LA-BL 0.0000 0.0000 0.0000

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

LA-JDA 0.0000 0.0000 LA-JGSA 0.0295 0.0000 LA-MEDA 0.0000 0.0000

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

E. Scenario II-a: Same Feature Space and Completely Different Label Spaces in Binary Classiﬁcation

This subsection considers the scenario that the source and target subjects have the same feature space but completely different label spaces. As introduced in Section V-A, we had six such sub-dataset combinations to be tested. k ∈ {2,4,...,20}

| |
|---|

| |
|---|

60

60

60

60

60

50

50

50

50

50

40

40

40

40

40

10 20 30

10 20 30

10 20 30

10 20 30

10 20 30

| |
|---|

60

60

60

60

60

50

50

50

50

50

40

40

40

40

40

10 20 30

10 20 30

10 20 30

10 20 30

10 20 30

### Average

65

|Raw-BL<br><br>Raw-JDA<br><br>Raw-JGSA<br><br>Raw-MEDA<br><br>EA-BL<br><br>EA-JDA<br><br>EA-JGSA<br><br>EA-MEDA<br><br>LA-BL<br><br>LA-JDA<br><br>LA-JGSA<br><br>LA-MEDA|
|---|

| |
|---|

| |
|---|

60

60

60

55

50

50

50

40

40

45

10 20 30

10 20 30

10 20 30

- Fig. 8. Average classiﬁcation accuracies (%) in Scenario I-b, when other DA approaches were used after LA. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

in k-medoids clustering of LA in binary classiﬁcation was used.

Because in Scenario II-a the source subjects had completely different labels from the target subject, the source labels and the target labels were randomly matched for LA. For example, in the experiment “1, 2→3, 4”, we could align the trials of Label 1 with those of Label 3, and the trials of Label 2 with those of Label 4. We could also align the trials of Label 2 with those of Label 3, and the trials of Label 1 with those of Label 4. Our experiments showed that LA was effective in both alignment strategies.

Question 1: Can LA be used as an effective preprocessing step before different feature extraction and classiﬁcation algorithms?

We compared Raw, EA, and LA in the two classiﬁcation pipelines. Fig. 9 shows the performances of the six algorithms on the six sub-dataset combinations, and the average. Observe that:

- 1) LA-CSP-LDA always outperformed Raw-CSP-LDA and EA-CSP-LDA, and LA-TS-SVM always outperformed Raw-TS-SVM and EA-TS-SVM. This suggests LA was effective in different feature extraction and classiﬁcation algorithms.
- 2) Comparing the last subﬁgure in Fig. 5 with the last one in Fig. 9, we can observe that the performances of Raw-CSP-LDA and Raw-TS-SVM were lower in Fig. 9, which is intuitive, because the label spaces in

Scenario II-a had larger discrepancies. However, the performances of LA-CSP-LDA and LA-TS-SVM did not change much, suggesting that LA can cope well with large label space discrepancies.

For the most extreme case that only one labeled target subject trial from each class is available, the average classiﬁcation accuracies across the nine subjects in the nine experiments are given in Table VII. LA achieved the best performances in all six experiments, regardless of which feature extraction and classiﬁcation algorithm was used.

TABLE VII SCENARIO II-A: AVERAGE CLASSIFICATION ACCURACIES (%) ACROSS THE NINE SUBJECTS WHEN ONLY ONE LABELED TARGET SUBJECT TRIAL FROM EACH CLASS IS AVAILABLE.

[Figure 87]

[Figure 88]

[Figure 89]

Experiment Approach Raw EA LA

[Figure 90]

- 1, 2 → 3, 4

[Figure 91]

CSP-LDA 55.48 56.42 58.84

[Figure 92]

[Figure 93]

TS-SVM 54.38 53.13 56.42 3, 4 → 1, 2

[Figure 94]

[Figure 95]

[Figure 96]

CSP-LDA 50.70 56.81 58.37 TS-SVM 52.19 54.77 58.53

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

- 1, 3 → 2, 4

[Figure 101]

CSP-LDA 53.99 60.02 62.44

[Figure 102]

[Figure 103]

TS-SVM 60.09 66.67 68.78 2, 4 → 1, 3

[Figure 104]

[Figure 105]

[Figure 106]

CSP-LDA 53.29 61.50 62.21 TS-SVM 56.49 60.49 64.79

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

- 1, 4 → 2, 3

[Figure 111]

[Figure 112]

CSP-LDA 52.35 57.75 61.50

[Figure 113]

- TS-SVM 55.87 60.17 65.81

[Figure 114]

[Figure 115]

2, 3 → 1, 4

[Figure 116]

CSP-LDA 51.10 64.01 69.95

[Figure 117]

[Figure 118]

- TS-SVM 56.65 64.32 71.75

[Figure 119]

[Figure 120]

We also performed paired t-tests on the AUCs in Fig. 9. Each algorithm had 6 × 9 = 54 AUCs. The p-values are

geous to integrate an additional DA approach with LA.

80

80

80

| |
|---|

| |
|---|

| |
|---|

70

70

70

80

80

80

60

60

60

70

70

70

50

50

50

2 8 14 20

2 8 14 20

2 8 14 20

60

60

60

80

80

80

50

50

50

| |
|---|

| |
|---|

5 10 15 20

5 10 15 20

5 10 15 20

70

70

70

| |
|---|

| |
|---|

80

80

80

60

60

60

70

70

70

50

50

50

2 8 14 20

2 8 14 20

2 8 14 20

60

60

60

###### Average

80

50

50

50

| |
|---|

|Raw-CSP-LDA<br><br>Raw-TS-SVM EA-CSP-LDA EA-TS-SVM<br><br>LA-CSP-LDA<br><br>LA-TS-SVM|
|---|

5 10 15 20

5 10 15 20

5 10 15 20

###### Average

70

| |
|---|

75

|Raw-BL<br><br>Raw-JDA<br><br>Raw-JGSA<br><br>Raw-MEDA<br><br>EA-BL<br><br>EA-JDA<br><br>EA-JGSA<br><br>EA-MEDA<br><br>LA-BL<br><br>LA-JDA<br><br>LA-JGSA<br><br>LA-MEDA|
|---|

60

70

65

50

2 8 14 20

60

55

- Fig. 9. Average classiﬁcation accuracies (%) in Scenario II-a. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

5 10 15 20

Fig. 10. Average classiﬁcation accuracies (%) in Scenario II-a, when additional DA approaches were used after LA. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

shown in Table VIII, where the statistically signiﬁcant ones are marked in bold. LA-CSP-LDA signiﬁcantly outperformed EA-CSP-LDA, and LA-TS-SVM signiﬁcantly outperformed EA-TS-SVM.

The results of paired t-tests on the AUCs in Fig. 10 are shown in Table IX, which are consistent with those in the last two subsections: LA signiﬁcantly outperformed EA and classical DA approaches, and the classiﬁcation performance can be further signiﬁcantly improved when LA was integrated with other DA approaches.

TABLE VIII SCENARIO II-A: p-VALUES OF PAIRED t-TESTS ON THE AUCS OF THE CLASSIFICATION ACCURACY CURVES IN FIG. 9. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 121]

[Figure 122]

EA-CSP-LDA EA-TS-SVM LA-CSP-LDA 0.0000

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

LA-TS-SVM 0.0000

[Figure 127]

TABLE IX SCENARIO II-A: p-VALUES OF PAIRED t-TESTS ON THE AUCS IN FIG. 10. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

Question 2: Can LA be integrated with other DA approaches to further improve the classiﬁcation performance?

Again, we considered the case when there were additional DA approaches after LA. The results are shown in Fig. 10. Observe that:

- 1) LA-BL always outperformed Raw-BL and EA-BL, LAJDA always outperformed Raw-JDA and EA-JDA, LAJGSA always outperformed Raw-JGSA and EA-JGSA, and LA-MEDA always outperformed Raw-MEDA and EA-MEDA. These suggest that LA was effective regardless of whether an additional DA approach was used or not.
- 2) LA-BL outperformed Raw-JDA, Raw-JGSA and RawMEDA in all six experiments, suggesting that LA can outperform classical DA approaches such as JDA, JGSA and MEDA.
- 3) Generally, LA-JDA, LA-JGSA, LA-MEDA outperformed LA-BL, suggesting again that it may be advanta-

[Figure 128]

[Figure 129]

LA-BL EA-JDA EA-JGSA EA-MEDA LA-BL 0.0000 0.0000 0.0000

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

LA-JDA 0.0109 0.0000 LA-JGSA 0.0116 0.0000 LA-MEDA 0.0009 0.0000

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

F. Scenario II-b: Same Feature Space and Completely Different Label Spaces in Multi-Class Classiﬁcation

This subsection considers the multi-class classiﬁcation scenario that the source and the target subjects have the same feature space but completely different label spaces.

Ideally, if Dataset 2a has six or more different classes, we can perform studies like “1,2,3 → 4,5,6” in multi-class classiﬁcation. Unfortunately, Dataset 2a only has four classes. So, we mismatched the labels between the target and the source subjects, to simulate completely different label spaces in multi-class classiﬁcation.

Assume the labels of the source subjects are ‘1’, ‘2’ and ‘3’, and the labels of the target subject are ‘1’, ‘2’ and ‘4’. Then, we match ‘1’ of the source subjects with ‘2’ of the target subject, ‘2’ of the source subjects with ‘1’ of the target subject, and ‘3’ of the source subjects with ‘4’ of the target subject, i.e., ‘1,2,3 → 2,1,4. A potential application scenario of this setting is that for the source subjects we know which trials belong to the same class, but do not know the speciﬁc class labels. So, we randomly match them to the labels of the target subject.

Question 1: Can LA be used as an effective preprocessing step before different feature extraction and classiﬁcation algorithms?

Again, we compared Raw, EA, and LA in the two classiﬁcation pipelines to answer this question. Fig. 11 shows the performances of the six algorithms on 12 different subdataset combinations, where each subﬁgure shows the average classiﬁcation accuracies across the nine subjects (each as the target subject once). The last subﬁgure shows the average performances across the 12 experiments. The title of each subﬁgure shows the sub-datasets used, and also how we matched the labels between the two sub-datasets. Observe that:

- 1) LA-CSP-LDA always outperformed Raw-CSP-LDA and EA-CSP-LDA, and LA-TS-SVM always outperformed Raw-TS-SVM and EA-TS-SVM. This suggests that was effective in different feature extraction and classiﬁcation algorithms.
- 2) LA in Fig. 11 achieved much larger performance improvements over Raw and EA than those in Fig. 7. When the labels mismatched, the algorithms without LA (i.e., Raw-CSP-LDA, Raw-TS-SVM, EA-CSP-LDA and EA-TS-SVM) performed very poorly. However, the performances of LA-CSP-LDA and LA-TS-SVM were very consistent, suggesting that LA can cope well with large label space discrepancies.

Paired t-tests on the AUCs in Fig. 11 were also performed to check if the differences between different algorithms were statistically signiﬁcant. The results are shown in Table X, which indicate that LA-CSP-LDA signiﬁcantly outperformed EA-CSP-LDA, and LA-TS-SVM signiﬁcantly outperformed EA-TS-SVM.

TABLE X SCENARIO II-B: p-VALUES OF PAIRED t-TESTS ON THE AUCS OF THE CLASSIFICATION ACCURACY CURVES IN FIG. 11. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 139]

[Figure 140]

EA-CSP-LDA EA-TS-SVM LA-CSP-LDA 0.0000

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

LA-TS-SVM 0.0000

[Figure 145]

Question 2: Can LA be integrated with other DA approaches to further improve the classiﬁcation performance?

Again, we combined Raw, EA, LA with different DA approaches and obtained 12 algorithms to be compared. Fig. 12 shows their performances on the 12 sub-dataset combinations, and the average across the 12 experiments. Observe that:

- 1) LA-BL always outperformed Raw-BL and EA-BL, LAJDA always outperformed Raw-JDA and EA-JDA, LAJGSA always outperformed Raw-JGSA and EA-JGSA,

and LA-MEDA always outperformed Raw-MEDA and EA-MEDA. These suggest that LA was effective regardless of whether additional DA approaches were used or not.

- 2) LA-BL always outperformed Raw-JDA, Raw-JGSA and Raw-MEDA, suggesting that LA can outperform classical DA approaches such as JDA, JGSA and MEDA.
- 3) Generally, LA-JDA, LA-JGSA and LA-MEDA outperformed LA-BL, suggesting that it may be advantageous to integrate additional DA approaches with LA.
- 4) When the labels were mismatched, the algorithms without LA performed very poorly. However, the algorithms with LA performed consistently good, suggesting that LA can cope well with large label space discrepancies.

Table XI shows the results of paired t-tests on the AUCs in Fig. 12. The conclusions in binary classiﬁcation still hold in multi-class classiﬁcation: LA signiﬁcantly outperformed EA and classical DA approaches, and its performance can be further signiﬁcantly improved when integrated with other DA approaches.

TABLE XI SCENARIO II-B: p-VALUES OF PAIRED t-TESTS ON THE AUCS IN FIG. 12. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 146]

[Figure 147]

LA-BL EA-JDA EA-JGSA EA-MEDA LA-BL 0.0000 0.0000 0.0000

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

LA-JDA 0.0000 0.0000 LA-JGSA 0.0009 0.0000 LA-MEDA 0.0000 0.0000

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

G. Scenario III: Different Feature Spaces and Different Label Spaces

This subsection considers the most challenging scenario: the source and target subjects have different feature spaces and also completely different label spaces. We chose “Classes 3, 4” (“feet” and “tongue”) from Dataset 2a as the target dataset, and Dataset 1 as the source dataset. Each time we picked one subject from “Classes 3, 4” as the target subject, and all seven subjects from Dataset 1 as the source subjects. In this scenario, the source dataset and target dataset were collected from different EEG headsets with different numbers of channels at different locations, so they had different feature spaces. In addition, for Dataset 1, Subjects 1 and 6 performed “left hand” and “feet” tasks, whereas other subjects performed “left hand” and “right hand” tasks. So, the source and target subjects also had partially or completely different label spaces.

Question 1: Can LA be used as an effective preprocessing step before different feature extraction and classiﬁcation algorithms?

We selected the source EEG channels as those closest to the target EEG channels [14], and compared different algorithms. Fig. 13 shows the experimental results when LA was used before different feature extraction and classiﬁcation algorithms, and Table XII shows the p-values of paired t-tests on the AUCs. LA-CSP-LDA signiﬁcantly outperformed EACSP-LDA, and LA-TS-SVM signiﬁcantly outperformed EATS-SVM. These suggest that LA was effective in different feature extraction and classiﬁcation algorithms.

70

70

70

70

70

| |
|---|

| |
|---|

| |
|---|

| |
|---|

60

60

60

60

60

50

50

50

50

50

40

40

40

40

40

30

30

30

30

30

20

20

20

20

20

10 20 30

10 20 30

10 20 30

10 20 30

10 20 30

70

70

70

70

70

| |
|---|

| |
|---|

| |
|---|

60

60

60

60

60

50

50

50

50

50

40

40

40

40

40

30

30

30

30

30

20

20

20

20

20

10 20 30

10 20 30

10 20 30

10 20 30

10 20 30

Average

70

70

60

| |
|---|

| |
|---|

|Raw-CSP-LDA<br><br>Raw-TS-SVM EA-CSP-LDA EA-TS-SVM<br><br>LA-CSP-LDA<br><br>LA-TS-SVM|
|---|

60

60

50

50

50

40

40

40

30

30

30

20

20

10 20 30

10 20 30

10 20 30

- Fig. 11. Average classiﬁcation accuracies (%) in Scenario II-b. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

10 20 30

20

30

40

50

60

10 20 30

20

30

40

50

60

10 20 30

| |
|---|

20

30

40

50

60

10 20 30

20

30

40

50

60

10 20 30

| |
|---|

20

30

40

50

60

10 20 30

| |
|---|

20

30

40

50

60

10 20 30

| |
|---|

20

30

40

50

60

10 20 30

20

30

40

50

60

10 20 30

20

30

40

50

60

10 20 30

| |
|---|

20

30

40

50

60

10 20 30

| |
|---|

20

30

40

50

60

10 20 30

20

30

40

50

60

10 20 30

30

40

50

60

Average

|Raw-BL<br><br>Raw-JDA<br><br>Raw-JGSA<br><br>Raw-MEDA<br><br>EA-BL<br><br>EA-JDA<br><br>EA-JGSA<br><br>EA-MEDA<br><br>LA-BL<br><br>LA-JDA<br><br>LA-JGSA<br><br>LA-MEDA|
|---|

- Fig. 12. Average classiﬁcation accuracies (%) in Scenario II-b, when other DA approaches were used after LA. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

###### Subject 1

###### Subject 2

###### Subject 3

###### Subject 1

###### Subject 2

###### Subject 3

100

100

100

| |
|---|

| |
|---|

80

80

80

80

80

80

60

60

60

60

60

60

40

40

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

2 8 14 20

2 8 14 20

2 8 14 20

###### Subject 4

###### Subject 5

###### Subject 6

###### Subject 4

###### Subject 5

###### Subject 6

100

100

100

| |
|---|

80

80

80

80

80

80

60

60

60

60

60

60

40

40

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

2 8 14 20

2 8 14 20

2 8 14 20

###### Subject 7

###### Subject 8

###### Subject 9

###### Subject 7

###### Subject 8

###### Subject 9

100

100

100

| |
|---|

| |
|---|

| |
|---|

| |
|---|

| |
|---|

80

80

80

80

80

80

60

60

60

60

60

60

40

40

40

40

40

40

5 10 15 20

5 10 15 20

5 10 15 20

2 8 14 20

2 8 14 20

2 8 14 20

###### Average

###### Average

|Raw-CSP-LDA<br><br>Raw-TS-SVM EA-CSP-LDA EA-TS-SVM<br><br>LA-CSP-LDA<br><br>LA-TS-SVM|
|---|

| |
|---|

70

| |
|---|

|Raw-BL<br><br>Raw-JDA<br><br>Raw-JGSA<br><br>Raw-MEDA<br><br>EA-BL<br><br>EA-JDA<br><br>EA-JGSA<br><br>EA-MEDA<br><br>LA-BL<br><br>LA-JDA<br><br>LA-JGSA<br><br>LA-MEDA|
|---|

70

60

60

50

50

5 10 15 20

2 8 14 20

Fig. 14. Average classiﬁcation accuracies (%) in Scenario III, when additional DA approaches were used after LA. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

- Fig. 13. Average classiﬁcation accuracies (%) in Scenario III. The horizontal axis indicates the number of labeled target subject trials (k in k-medoids clustering in Section III), and the vertical axis the classiﬁcation accuracies.

TABLE XII SCENARIO III: p-VALUES OF THE PAIRED t-TESTS ON THE AUCS OF THE ACCURACY CURVES IN FIG. 13. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 157]

[Figure 158]

EA-CSP-LDA EA-TS-SVM LA-CSP-LDA 0.0082

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

LA-TS-SVM 0.0006

[Figure 163]

Question 2: Can LA be integrated with other DA approaches to further improve the classiﬁcation performance?

Fig. 14 shows the experimental results with and without additional DA approaches. Generally, LA was effective regardless of whether additional DA approaches were used or not. Table XIII shows the p-values of paired t-tests on the AUCs in Fig. 14. LA-BL signiﬁcantly outperformed EA-JDA and EA-MEDA, LA-JDA signiﬁcantly outperformed EA-JDA, and LA-MEDA signiﬁcantly outperformed EA-MEDA. However, unlike before, the integration of LA with other DA approaches did not signiﬁcantly outperform LA-BL. Nevertheless, LA did not degrade the performance of these DA approaches, either.

TABLE XIII SCENARIO III: p-VALUES OF THE PAIRED t-TESTS ON THE AUCS OF THE ACCURACY CURVES IN FIG. 14. THE NULL HYPOTHESIS WAS REJECTED IF p < α, WHERE α = 0.05.

[Figure 164]

[Figure 165]

LA-BL EA-JDA EA-JGSA EA-MEDA LA-BL 0.0017 0.1335 0.0011

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

LA-JDA 0.3733 0.0026 LA-JGSA 0.8449 0.0691 LA-MEDA 0.9777 0.0012

[Figure 170]

[Figure 171]

[Figure 172]

[Figure 173]

[Figure 174]

TS-SVM. The platform was a Lenovo ThinkPad laptop with Intel Core i5-6200U CPU@2.30GHz, 4GB memory, and 190 GB SSD, running 64-bit Windows 10 and Matlab 2018b. The results are shown in Table XIV, which were averaged across different numbers of labeled target trials (from 2 to 20) and nine target subjects. LA only increased the computing time very slightly.

H. Computational Complexity of LA

The time complexity of LA is O(NT2), where NT is the number of target domain trials. The most time-consuming operation in LA is k-medoids clustering.

We also empirically evaluated the computational cost of LA in Scenario III, by comparing Raw-TS-SVM and LA-

TABLE XIV THE COMPUTING TIME (SECONDS) OF RAW-TS-SVM AND LA-TS-SVM IN SCENARIO III.

[Figure 175]

[Figure 176]

mean std

[Figure 177]

[Figure 178]

Raw-TS-SVM 2.1963 0.1492 LA-TS-SVM 2.3669 0.3469

[Figure 179]

[Figure 180]

[Figure 181]

VI. CONCLUSIONS AND FUTURE RESEARCH

Transfer learning, or domain adaptation, has been successfully used to reduce the subject-speciﬁc calibration effort in BCIs. However, most existing DA approaches require the source subjects share the same feature space and also the same label space as the target subject, which may not always hold in real-world applications. This paper has proposed a simple yet effective LA approach to cope with different label spaces. Our experiments demonstrated that: 1) LA only needs as few as one labeled sample from each class of the target subject;

- 2) LA can be used as a preprocessing step before different feature extraction and classiﬁcation algorithms; and, 3) LA can be integrated with other DA approaches to achieve even better classiﬁcation performance.

The current LA may still have some limitations, which will be addressed in our future research:

- 1) The estimation of each class mean in the target domain is very important to the performance of LA. Currently LA uses k-medoids clustering to select a few trials to label, which could be improved.
- 2) LA copes well with different labels spaces, but does not pay special attention to different feature spaces (although it can also be used in this case). This may explain why there were relatively less performance improvements when integrated with other DA approaches in Scenario III. We will speciﬁcally consider different feature spaces in the future.
- 3) The current LA approach was speciﬁcally designed for EEG trials, and uses 2D covariance matrices as the input features. We will extend it to 1D features so that it can have broader applications in other domains.

ACKNOWLEDGMENT

This research was supported by the National Natural Science Foundation of China under Grant 61873321 and Hubei Technology Innovation Platform under Grant 2019AEA171.

REFERENCES

- [1] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain-computer interfaces for communication and control,” Clinical Neurophysiology, vol. 113, no. 6, pp. 767–791, 2002.
- [2] B. J. Lance, S. E. Kerick, A. J. Ries, K. S. Oie, and K. McDowell, “Brain-computer interface technologies in the coming decades,” Proc. of the IEEE, vol. 100, no. 3, pp. 1585–1599, 2012.
- [3] Z. J. Koles, M. S. Lazar, and S. Z. Zhou, “Spatial patterns underlying population differences in the background EEG,” Brain Topography, vol. 2, no. 4, pp. 275–284, 1990.
- [4] J. Mu¨ller-Gerking, G. Pfurtscheller, and H. Flyvbjerg, “Designing optimal spatial ﬁlters for single-trial EEG classiﬁcation in a movement task,” Clinical Neurophysiology, vol. 110, no. 5, pp. 787–798, 1999.
- [5] H. Ramoser, J. Muller-Gerking, and G. Pfurtscheller, “Optimal spatial ﬁltering of single trial EEG during imagined hand movement,” IEEE Trans. on Rehabilitation Engineering, vol. 8, no. 4, pp. 441–446, 2000.
- [6] H. He and D. Wu, “Spatial ﬁltering for brain computer interfaces: A comparison between the common spatial pattern and its variant,” in Proc. IEEE Int’l. Conf. on Signal Processing, Communications and Computing, Qingdao, China, Sep. 2018, pp. 1–6.
- [7] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Multiclass braincomputer interface classiﬁcation by Riemannian geometry,” IEEE Trans. on Biomedical Engineering, vol. 59, no. 4, pp. 920–928, 2012.
- [8] F. Yger, M. Berar, and F. Lotte, “Riemannian approaches in braincomputer interfaces: a review,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 25, no. 10, pp. 1753–1762, 2017.

- [9] B. He, B. Baxter, B. J. Edelman, C. C. Cline, and W. W. Ye, “Noninvasive brain-computer interfaces based on sensorimotor rhythms,” Proc. of the IEEE, vol. 103, no. 6, pp. 907–925, 2015.
- [10] G. Pfurtscheller, G. R. Mu¨ller-Putz, R. Scherer, and C. Neuper, “Rehabilitation with brain-computer interface systems,” Computer, vol. 41, no. 10, pp. 58–65, 2008.
- [11] L. F. Nicolas-Alonso and J. Gomez-Gil, “Brain computer interfaces, a review,” Sensors, vol. 12, no. 2, pp. 1211–1279, 2012.
- [12] J. van Erp, F. Lotte, and M. Tangermann, “Brain-computer interfaces: Beyond medical applications,” Computer, vol. 45, no. 4, pp. 26–34, 2012.
- [13] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, and M. GrosseWentrup, “Transfer learning in brain-computer interfaces,” IEEE Computational Intelligence Magazine, vol. 11, no. 1, pp. 20–31, 2016.
- [14] D. Wu, V. J. Lawhern, W. D. Hairston, and B. J. Lance, “Switching EEG headsets made easy: Reducing ofﬂine calibration effort using active weighted adaptation regularization,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 24, no. 11, pp. 1125–1137, 2016.
- [15] D. Wu, V. J. Lawhern, S. Gordon, B. J. Lance, and C.-T. Lin, “Driver drowsiness estimation from EEG signals using online weighted adaptation regularization for regression (OwARR),” IEEE Trans. on Fuzzy Systems, vol. 25, no. 6, pp. 1522–1535, 2017.
- [16] D. Wu, “Online and ofﬂine domain adaptation for reducing BCI calibration effort,” IEEE Trans. on Human-Machine Systems, vol. 47, no. 4, pp. 550–563, 2017.
- [17] D. Wu, “Active semi-supervised transfer learning (ASTL) for ofﬂine BCI calibration,” in Proc. IEEE Int’l. Conf. on Systems, Man and Cybernetics, Banff, Canada, October 2017.
- [18] H. He and D. Wu, “Transfer learning enhanced common spatial pattern ﬁltering for brain computer interfaces (BCIs): Overview and a new approach,” in Proc. 24th Int’l. Conf. on Neural Information Processing, Guangzhou, China, November 2017.
- [19] H. Kang, Y. Nam, and S. Choi, “Composite common spatial pattern for subject-to-subject transfer,” Signal Processing Letters, vol. 16, no. 8, pp. 683–686, 2009.
- [20] F. Lotte and C. Guan, “Learning from other subjects helps reducing brain-computer interface calibration time,” in Proc. IEEE Int’l. Conf. on Acoustics Speech and Signal Processing, Dallas, TX, March 2010.
- [21] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans. on Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345–1359, 2010.
- [22] M. Long, J. Wang, G. Ding, J. Sun, and P. S. Yu, “Transfer feature learning with joint distribution adaptation,” in Proc. IEEE Int’l. Conf. on Computer Vision, Sydney, Australia, Dec. 2013, pp. 2200–2207.
- [23] J. Zhang, W. Li, and P. Ogunbona, “Joint geometrical and statistical alignment for visual domain adaptation,” in Proc. IEEE Conf. on Computer Vision and Pattern Recognition, Honolulu, HI, Jul. 2017, pp. 1859–1867.
- [24] J. Wang, W. Feng, Y. Chen, H. Yu, M. Huang, and P. S. Yu, “Visual domain adaptation with manifold embedded distribution alignment,” in Proc. 26th ACM Int’l Conf. on Multimedia, Seoul, South Korea, Oct. 2018, pp. 402–410.
- [25] J. Lu, V. Behbood, P. Hao, H. Zuo, S. Xue, and G. Zhang, “Transfer learning using computational intelligence: a survey,” Knowledge-Based Systems, vol. 80, pp. 14–23, 2015.
- [26] P. Zanini, M. Congedo, C. Jutten, S. Said, and Y. Berthoumieu, “Transfer learning: a Riemannian geometry framework with applications to braincomputer interfaces,” IEEE Trans. on Biomedical Engineering, vol. 65, no. 5, pp. 1107–1116, 2018.
- [27] H. He and D. Wu, “Transfer learning for brain-computer interfaces: A Euclidean space data alignment approach,” IEEE Trans. on Biomedical Engineering, vol. 67, no. 2, pp. 399–410, 2020.
- [28] O. Day and T. M. Khoshgoftaar, “A survey on heterogeneous transfer learning,” Journal of Big Data, vol. 4, no. 1, p. 29, 2017.
- [29] F. Liu, J. Lu, and G. Zhang, “Unsupervised heterogeneous domain adaptation via shared fuzzy equivalence relations,” IEEE Trans. on Fuzzy Systems, vol. 26, no. 6, pp. 3555–3568, 2018.
- [30] P. P. Busto and J. Gall, “Open set domain adaptation,” in Proc. IEEE Int’l Conf. on Computer Vision, Venice, Italy, Oct. 2017, pp. 754–763.
- [31] K. Saito, S. Yamamoto, Y. Ushiku, and T. Harada, “Open set domain adaptation by backpropagation,” in Proc. European Conf. on Computer Vision, Munich, Germany, Sep. 2018, pp. 153–168.
- [32] Z. Fang, J. Lu, F. Liu, J. Xuan, and G. Zhang, “Open set domain adaptation: Theoretical bound and algorithm,” arXiv preprint arXiv:1907.08375, 2019.

- [33] K. You, M. Long, Z. Cao, J. Wang, and M. I. Jordan, “Universal domain adaptation,” in Proc. IEEE Conf. on Computer Vision and Pattern Recognition, Long Beach, CA, Jun. 2019, pp. 2720–2729.
- [34] H. He and D. Wu, “Channel and trials selection for reducing covariate shift in EEG-based brain-computer interfaces,” in 2019 IEEE Int’l Conf. on Systems, Man and Cybernetics, Bari, Italy, Oct. 2019, pp. 3635–3640.
- [35] A. Gretton, K. Borgwardt, M. Rasch, B. Scho¨lkopf, and A. J. Smola, “A kernel method for the two-sample-problem,” in Proc. Advances in Neural Information Processing Systems, Vancouver, Canada, Dec. 2007, pp. 513–520.
- [36] B. Sun, J. Feng, and K. Saenko, “Return of frustratingly easy domain adaptation,” in Proc. 30th AAAI Conf. on Artiﬁcial Intelligence, vol. 6, no. 7, Phoenix, AZ, Feb. 2016, pp. 2058–2065.
- [37] H. Shimodaira, “Improving predictive inference under covariate shift by weighting the log-likelihood function,” Journal of Statistical Planning and Inference, vol. 90, no. 2, pp. 227–244, 2000.
- [38] M. Sugiyama, S. Nakajima, H. Kashima, P. von Bu¨nau, and M. Kawanabe, “Direct importance estimation with model selection and its application to covariate shift adaptation,” in Proc. 21th Annual Conf. on Neural Information Processing Systems, Vancouver, Canada, Dec. 2007, pp. 1433–1440.
- [39] P. E. Utgoff, Machine learning: An artiﬁcial intelligence approach. CA: Morgan Kaufmann, 1986, vol. 2, ch. Shift of bias for inductive concept learning, pp. 107–148.
- [40] V. Arsigny, P. Fillard, X. Pennec, and N. Ayache, “Geometric means in a novel vector space structure on symmetric positive-deﬁnite matrices,” SIAM Journal on Matrix Analysis and Applications, vol. 29, no. 1, pp. 328–347, 2007.
- [41] B. Blankertz, G. Dornhege, M. Krauledat, K. R. Muller, and G. Curio, “The non-invasive Berlin brain-computer interface: Fast acquisition of effective performance in untrained subjects,” NeuroImage, vol. 37, no. 2, pp. 539–550, 2007.
- [42] A. Delorme and S. Makeig, “EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis,” Journal of Neuroscience Methods, vol. 134, pp. 9–21, 2004.
- [43] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K. R. Muller, “Optimizing spatial ﬁlters for robust EEG single-trial analysis,” IEEE Signal Processing Magazine, vol. 25, no. 1, pp. 41–56, 2008.
- [44] L. van der Maaten and G. Hinton, “Visualizing data using t-SNE,” Journal of Machine Learning Research, vol. 9, pp. 2579–2605, 2008.
- [45] G. Dornhege, G. C. B. Blankertz, and K.-R. Muller, “Boosting bit rates in non-invasive EEG single-trial classiﬁcations by feature combination and multi-class paradigms,” IEEE Trans. on Biomedical Engineering, vol. 51, no. 6, pp. 993–1002, 2004.

