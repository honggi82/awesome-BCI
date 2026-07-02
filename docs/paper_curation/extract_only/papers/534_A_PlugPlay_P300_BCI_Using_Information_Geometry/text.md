# A Plug&Play P300 BCI Using Information Geometry

Alexandre Barachant, Marco Congedo Team ViBS (Vision and Brain Signal Processing), GIPSA-lab, CNRS, Grenoble Universities. France. Email: alexandre.barachant@gmail.com

## arXiv:1409.0107v1[cs.LG]30Aug2014

Abstract—This paper presents a new classiﬁcation methods for Event Related Potentials (ERP) based on an Information geometry framework. Through a new estimation of covariance matrices, this work extend the use of Riemannian geometry, which was previously limited to SMR-based BCI, to the problem of classiﬁcation of ERPs. As compared to the state-of-the-art, this new method increases performance, reduces the number of data needed for the calibration and features good generalisation across sessions and subjects. This method is illustrated on data recorded with the P300-based game brain invaders. Finally, an online and adaptive implementation is described, where the BCI is initialized with generic parameters derived from a database and continiously adapt to the individual, allowing the user to play the game without any calibration while keeping a high accuracy.

Index Terms—ERP, BCI, Information geometry

I. INTRODUCTION

So far we have conceived a Brain-Computer Interface (BCI) as a learning machine where the classiﬁer is trained in a calibration phase preceding immediately the actual BCI use [1]. Depending on the BCI paradigm and on the efﬁciency of the classiﬁer, the calibration phase may last from a few to several minutes. Regardless the duration, the very necessity of a calibration session reduces drastically the usability and appealing of a BCI. This is true both for clinically-oriented BCI, where the cognitive skills of patients are often limited and are wasted in the calibration phase, and for healthy users where the plug&play operation is nowadays considered

- as a minimum requirement for any consumer interfaces and devices. Besides the essential considerations from the user perspective, it appears evident that training the BCI at the beginning of each session and discarding the calibration data
- at the end is a very inefﬁcient way to proceed. The problem we pose here is: can we design a ”plug&play” BCI? Of course, such a goal does not imply that the BCI is not calibrated. What we want to achieve is that the calibration is completely hidden to the user. One possible solution is to initialize the classiﬁcation algorithm with generic parameters derived from previous sessions and/or previous users and then to adapt continuously these parameters during the experiment in order to reach optimality for the current user in the current session. In order to do so our BCI must possess two key properties, namely:

1) good across-subject generalization and across-session generalization, so as to yield appropriate accuracy (albeit sub-optimal) at the beginning of each session and even for the very ﬁrst session of a BCI naive user.

2) fast convergence toward the optimal parameters, that is, the adaptation should be efﬁcient and robust (the adaptation is useless if it is effective only at the end of the session).

The two properties above are not trivial. On one hand, the methods involving spatial ﬁltering enjoy fast convergence, but show a bad generalisation since the subspace projection is very speciﬁc to each subject and session. On the other hand, the methods working directly with low level, high dimensional space or features selected space show good generalization but require a lot of data to avoid over-ﬁtting and therefore do not fulﬁl the property of fast convergence.

We have solved this problem before by working in the native space of covariance matrices and using Riemannian geometry [2]. So far this framework was limited to BCIs based on motor imagery and SSVEP since the regular covariance matrix estimation does not take into account the temporal structure of the signals, which is critical for ERP detection. Here we allow the use of our Riemannian geometry framework for ERP-based BCI by introducing a new smart way for building covariance matrices. We show experimentally that our new initialization/adaption BCI framework (based on Riemannian geometry) enjoys both properties 1) and 2). In addition, our method is rigorous, elegant, conceptually simple and computationally efﬁcient. As a by-product the implementation is easier, more stable and compatible with the time constraints of a system operating on-line. Finally, thanks to the advance here presented we are able to propose a universal framework for calibration-less BCIs, that is, the very same signal processing chain can be now applied with minor modiﬁcations to any currently existing types of BCI.

This paper is organized as follows. Section II introduce the metric, based on information geometry, that we are using in this work. Section III presents the classiﬁcation algorithm and the new covariance matrix estimation method dedicated to the classiﬁcation of ERPs. The method is illustrated on the P300 ERP. Results on three datasets are shown in section IV and compared to the state-of-the-art methods. Finally, we will conclude and discuss in section V.

Related work: Over the past years, several attempt to design ”plug&play” BCI have been made. In [3], a pure machinelearning solution has been used for this purpose. For each user in a database, a complete classiﬁcation chain (band-pass ﬁltering, CSP spatial ﬁltering, LDA classiﬁer) is trained and optimized. Then, for a new user, all these classiﬁers are applied and the results are combined (different solutions are proposed)

in order to build a single classiﬁcation result. In [4], [5], an unsupervised adaptation of a generic classiﬁer is proposed to deal with inter-session and inter-subject variability in the context of the P300 speller. The proposed solution makes the use of the P300 constraints and language model to adapt a bayesian classiﬁer and unsure the convergence toward the optimal classiﬁer. This solution is for now the most convincing approach for the P300 speller.

II. A DISTANCE FOR THE MULTIVARIATE NORMAL MODEL A. Motivation

Our goal is to use a method enjoying both properties of fast adaptation and generalisation across subjects and sessions in order to build an efﬁcient adaptive classiﬁcation chain. As we will see, none of the state-of-the-art methods fulﬁls these requirement, therefore we have to design a new classiﬁcation algorithm.

In essence, a classiﬁcation algorithm works by comparing data to each other or to a prototype of the different classes. The notion of comparison implies the ability to measure dissimilarity between the data, i.e., the deﬁnition of a metric. Obviously, the accuracy of the classiﬁcation is related to the ability of the metric to measure difference between classes for the problem at hand. The deﬁnition of the appropriate metric is not trivial and should be accomplished according to the intrinsic nature of the data. This problem is usually bypassed by the feature extraction process, which projects the raw data in a feature space where a well known metric (Euclidean distance, Mahalanobis distance, etc) is effective. When the feature extraction is not able to complete the task, the metric could be embedded within the classiﬁcation function by using a kernel trick, as in the Support Vector Machine (SVM) classiﬁer. Nevertheless, the problem of choosing the kernel is not obvious and is generally solved by trials and errors, that is, by benchmarking several predeﬁned kernel through a cross-validation procedure. However proceeding this way one loose generalization [1].

The recent BCI systems follow these approaches, by using a subspace separation [6] procedure and a selection of relevant dimensions [7] before applying the classiﬁer on the extracted features. In these approaches, the weakness of the chain is the subspace separation process, which rely on several assumptions that are more or less fulﬁlled, depending on the number of classes and the quality of the data. In addition, the subspace separation gives solutions that are not generalisable between session and subjects. To overcome these difﬁculties, the linear subspace separation could be embedded in the classiﬁer by working directly on the covariance matrices [8] and using a SVM kernel to classify them [9]. Again, the choice of the kernel and its parameters is done heuristically which is incompatible with adaptive implementations.

In this context, the deﬁnition of a metric adapted to the nature of EEG signals seems to be particularly useful. With such a metric, a very simple distance-based classiﬁer can be used, allowing efﬁcient adaptive implementations, reducing the amount of data needed for calibration (no cross-validation or feature selection) and offering better generalization between

subjects and sessions (no source separation or any other spatial ﬁltering).

- B. An Information geometry metric

Thanks to information geometry we are able to deﬁne a metric enjoying the sought properties. The information geometry is a ﬁeld of information theory where the probability distributions are taken as point of a Riemannian manifold. This ﬁeld has been popularised by S. Amari who has widely contributed to establish the theoretical background [10]. Information geometry has today reached its maturity and ﬁnd an increasing number of practical applications, such as radar image processing [11], diffusion tensor imaging [12] and image and video processing [13]. The strength of the information geometry is to give a natural choice for an informationbased metric according to the probability distribution family: the Fisher Information [10]. Therefore, each probability distribution belongs to a Riemannian manifold with a well established metric leading to the deﬁnition of a distance between probability distributions.

In this work, EEG signals are assumed to follow a multivariate normal distribution with a zero mean (this is the case for EEG signals that are high-pass ﬁltered), which is a common assumption [14]. More speciﬁcally, it has been shown that EEG signal are block stationary and can be purposefully modelled by second order statistics [15]. Let us denote by X ∈ RC×N an EEG trial1 , recorded over C electrodes and N time samples. We assume that this trial follow a multivariate normal model with zero mean and with a covariance matrix Σ ∈ RC×C, i.e.

X ∼ N(0,Σ) (1)

The application of information geometry to the multivariate model with zero mean provides us with a metric that can be used to compare directly covariance matrices of EEG segments.

- C. Distance

Let us denote two EEG trials X1 ∼ N(0,Σ1) and X2 ∼ N(0,Σ2). Their Riemannian distance according to information geometry is given by [11]

1/2

C

δR(Σ1,Σ2) = log Σ−1 1/2Σ2Σ−1 1/2 F =

log2 λc

### ,

c=1

(2) where λc,c = 1...C are the real eigenvalues of Σ−1 1/2Σ2Σ−1 1/2 and C the number of electrodes. Note that this distance is also called Afﬁne-invariant [16] when it is obtained through the algebraic properties of the spaces of symmetric positive deﬁnite matrices rather than through the information geometry work-ﬂow. This distance has two important properties of invariance. First, the distance is invariant by inversion, i.e.,

### δR(Σ1,Σ2) = δR(Σ−1 1,Σ−2 1). (3)

1An epoch of EEG signal we want to classify.

Second, the distance is invariant by congruent transformation, meaning that for any invertible matrix V ∈ Gl(C) we have

δR(Σ1,Σ2) = δR(VTΣ1V,VTΣ2V). (4)

This latter property has numerous consequences on EEG signal. The most remarkable can be formulated as it follows:

Any linear operation on the EEG signals that can be modelled by a C × C invertible matrix V has no effect on the Riemannian distance.

Such a class of transformations include rescaling and normalization of the signals, electrodes permutations, whitening, spatial ﬁltering or source separation, etc. In essence, manipulating covariance matrices with Eq.(2) is equivalent to working in the optimal source space of dimension C.

- D. Geometric mean

The Riemannian geometric mean of I covariance matrices (denoted by G(.)), also called Fr´echet mean, is deﬁned as the matrix minimizing the sum of the squared Riemannian distances [17], i.e.,

G(Σ1,...,ΣI) = arg min Σ∈P(n)

I

i=1

δR2 (Σ,Σi). (5)

There is no closed form expression for this mean, however a gradient descent in the manifold can be used in order to ﬁnd the solution [17]. A matlab implementation is provided in a Matlab toolbox2. Note that the geometric mean inherits the properties of invariance from the distance.

- E. Geodesic

The geodesic is deﬁned as the shortest curve between two points (in this work, covariance matrices) of the manifold [17]. The geodesic according to the Riemannian metric is given by

t

- 1

- 2

- 1

- 2

- 1

- 2

- 1

- 2

1 Σ2Σ−

1 Σ−

1 , (6)

Σ

Γ(Σ1,Σ2,t) = Σ

1

with t ∈ [0 : 1] a scalar. Note that the geometric mean of two points is equal to the geodesic at t = 0.5 [18], i.e.,

### G(Σ1,Σ2) = Γ(Σ1,Σ2,0.5) (7)

Moreover, the geodesic could be seen as a geometric interpolation between the two covariance matrices Σ1 and Σ2. Its Euclidean equivalent is the well known linear interpolation (1 − t)Σ1 + tΣ2.

III. METHOD A. Classiﬁcation of covariance matrices

Using the metric deﬁned by the information geometry we are now able to efﬁciently compare EEG trials using only their covariance matrices.

The direct classiﬁcation of covariance matrices has proved very useful for single trial classiﬁcation in the context of SMRbased BCI [2], [19], [9] and more generally in every EEG application where the relevant features are based on the spatial

2http://github.com/alexandrebarachant/covariancetoolbox

patterns of the signal. A similar approach, working on the power spectral density rather than the covariance matrix, has been developed for sleep state detection [20], [21].

According to the property of invariance of the distance, the Riemannian metric allows to bypass the source separation step by exploiting directly the spatial information contained in the covariance matrix. While the state-of-the-arts methods rely on the classiﬁcation of the log-variances in the source space, the Riemannian metric gives access to the same information in the sensor space, leading to a better generalization of the trained classiﬁer.

The Minimum Distance to Mean (MDM) algorithm is one of the simplest classiﬁcation algorithm based on distance comparison. Used with the Riemannian distance, it is a powerful and efﬁcient way to build a an online BCI system [22]. Given a training set of EEG trials Xi ∼ N(0,Σi) and the corresponding labels yi ∈ {1 : Nc}, the classiﬁer training consist in the estimation of a mean covariance matrix for each of the Nc classes,

Σ¯K = G(Σi|yi = K), (8)

where K ∈ [1 : Nc] is the class label and G(.) is the Riemannian geometric mean deﬁned in section II-D. In essence, the geometric mean represents the expected distribution that will follows a trial belonging to class K.

Then, the classiﬁcation of a new trial X ∼ N(0,Σ) of an unknown class y is simply achieved by looking at the minimun distance to each mean,

δR(Σ¯K,Σ). (9)

yˆ = arg min

K

Such a classiﬁer deﬁnes a set of vorono¨ı cells in the manifold. Alternatively, for binary classiﬁcation problems, the difference of the two distances could be used as a linear classiﬁcation score. The algorithm is extremely simple since it involve only a mean estimation and a distance computation for each class. The full algorithm is given in Algorithm 1.

Algorithm 1 Minimum Distance to Riemannian Mean

Input: a set of trials Xi of Nc different known classes and the corresponding labels yi ∈ {1 : K}. Input: X an EEG trial of unknown class. Output: yˆ the estimated class of test trial X.

- 1: Compute SCMs of Xi to obtain Σi.
- 2: Compute SCM of X to obtain Σ.
- 3: for K = 1 to Nc do
- 4: Σ¯K = G (Σi|yi = K), Riemannian geometric mean (5).
- 5: end for
- 6: yˆ = arg minK δR(Σ¯K, Σ), Riemannian distance (2).
- 7: return yˆ

B. Classiﬁcation of covariance matrices in P300-based BCI

The above procedure is not suitable for classiﬁcation of ERPs, where the discriminant information is given by the waveform of the potential rather than the spatial distribution of its variance. Indeed, the covariance matrix estimation does not take into account the time structure of the signal, and therefore using only the covariance matrix for the classiﬁcation leads to the loss of the information carried by the temporal structure of the ERP.

More generally, the prior knowledge of a reference signal, i.e., the expected waveform of the signal due to a physiological process (P300, ErrP, etc.) or induced by a stimulation pattern (SSEP), are rarely taken into account in the signal processing chain.

Our contribution stems from the deﬁnition of a speciﬁc way of building covariance matrices for ERP data embedding both the spatial and temporal structural information. This new deﬁnition, making use of a reference signal, allows the purposeful application of Riemannian geometry for ERP data. Let us deﬁne P1 ∈ RC×N the prototyped ERP response, obtained, for example, by averaging several single trial responses of one class, usually the target class, such as

1 |I| i∈I

Xi. (10)

P1 =

where I is the ensemble of indexes of the trial belonging to the target class. For each trial Xi ∈ RC×N, we build a super trial X˜ i ∈ R2C×N by concatenating P1 and Xi :

P1 Xi

X˜ i =

. (11)

These super trials are used to build the covariance matrices on which the classiﬁcation will be based. The covariance matrices are estimated using the Sample Covariance Matrix (SCM) estimator:

1 N − 1

X˜ iX˜ Ti . (12)

Σ˜i =

These covariances matrices can be decomposed in three different blocks : ΣP1 the covariance matrix of P1, Σi the covariance matrix of Xi and CP1,X

the cross-covariance matrix (non-symmetric) between P1 and Xi, that is,

i

Σ˜i =

ΣP1 CTP1,X

i

### CP1,X

Σi

i

. (13)

ΣP1 is the same for all the trials. This block is not useful for the discrimination between the different classes. Σi is the covariance matrix of the trial i. As explained previously, this block is not sufﬁcient to achieve a high classiﬁcation accuracy. However, it contains information that can be used in the classiﬁcation process. The cross-covariance matrix CP1,X

i

contains the major part of the useful information. If the trial contains an ERP in phase with ΣP1, the cross-covariance will be high for the corresponding channels. In other cases (absence of ERP or non phase locked ERP), the cross-covariance will be close to zero, leading to a particular covariance structure that can be exploited by the classiﬁcation algorithm.

Note that the property of invariance of the metric allows to use a reduced version of P1 after a source separation and a selection of relevant sources if desired.

Using this new estimation, the MDM algorithm can be applied in the exact same manner, using X˜ i Eq.(11) instead of Xi in Algorithm 1. In the case of ERP, only two classes are used, target for trials containing an ERP and non-target for the others, leading to the estimation of two mean covariance matrices, denoted Σ¯T and Σ¯T¯, respectively. For this binary

classiﬁcation task, the classiﬁcation score for each trial is given by the difference of the Riemannian distance to each class, i.e.,

s = δR(Σ¯T¯,Σ) − δR(Σ¯T,Σ). (14)

C. An adaptive implementation

We employ here a simple adaptation scheme. When new data from the current subject is available, the two subjectspeciﬁc intra-class mean covariance matrices Σ¯sT and Σ¯sT¯ are estimated and combined with the two generic ones (computed on a database) Σ¯gT and Σ¯gT¯ using a geodesic interpolation:

Σ¯K = Γ(Σ¯gK,Σ¯sK,α), (15)

where Γ is the geodesic from Σ¯gK to Σ¯sK given in Eq.(6), with K denoting T (T¯) for the target (non-target) class and with

α ∈ [0 : 1] a parameter settings the strength of the adaptation evolving from 0 at the beginning of the session to 1 at the end of the session. This combination is the Riemannian equivalent to (1 − α)Σ¯gK + αΣ¯sK in the euclidean space. The combined matrices are then used for the classiﬁcation in replacement of the standard mean covariances matrices in Algorithm 1. A similar approach has been presented for the adaptation of spatial ﬁlters in [23].

The adaptation is supervised, i.e., the classes of the trials have to be known. This not a limitation in applications where the target is chosen by the interface itself and not by the user. For other ERP-based BCI such as a P300 speller, adaptation will be somehow slower since only past symbols (that the user has conﬁrmed) can be used. However, an unsupervised adaptation is also possible using clustering of covariance matrices in Riemannian space. Preliminary results (not shown here) show that this approach is equivalent to the supervised one.

IV. RESULTS

- A. Material

The presented method is illustrated through the detection of P300 evoked potentials on three datasets. These datasets are recorded using the P300-based game Brain Invaders [24]. Brain invaders is inspired from the famous vintage game Space invaders. The goal is to destroy a target alien in a grid of non-target alien using the classical P300 paradigm. After each repetition, i.e., ﬂash of the 6 rows and 6 columns, the most probable alien is destroyed according to the single trial classiﬁcation scores of the 12 ﬂashes. If the target alien is destroyed, the game switch to the next level. If not, a new repetition begins and its classiﬁcation scores will be averaged with the scores of the previous repetitions. Therefore, the goal of the game is to complete all levels in a minimum number of repetitions.

- B. Preprocessing and State-of-the-art methods

Motivate the Choice Reference methods For each method and dataset, signals are bandpass ﬁltered by a 5th order butterworth ﬁlter between 1 and 20 Hz. Filtered signal are then downsampled to 128 Hz and segmented in

epochs of 1s starting at the time of the ﬂash. Two state of the art methods have been implemented for comparison with the proposed method. The ﬁrst is named XDAWN and is composed by a spatial ﬁltering using the xDAWN method [25] and a regularized LDA [26] for classiﬁcation. After the estimation of spatial ﬁlters, the two best spatial ﬁlters are applied on the epochs. The spatially ﬁltered epoch are then downsampled by a factor four and the time sample are aggregated to build a feature vector of size 32 × 2 = 64. These feature vectors are then classiﬁed using a regularized LDA.

The second method is name SWLDA and is composed by a single classiﬁcation stage using a stepwise LDA [26]. First the signals were downsampled by a factor four and aggregated to build a feature vector of size 32×C. These feature vectors are classiﬁed using a stepwise LDA [26]. The stepwise LDA performs a stepwise model selection before applying a regular linear discriminant analysis, reducing the number of features used for classiﬁcation.

The MDM method is directly applied on the epochs of signal, with no other preprocessing besides the frequency band-pass ﬁltering and downsampling.

C. Dataset I

Dataset I was recorded in laboratory conditions using 10 silver/silver-chloride electrodes (T7-Cz-T8-P7-P3-PZ-P4-P8O1-O2) and a Nexus ampliﬁer (TMSi, The Netherlands). The signal was sampled at 512 Hz. 23 subjects participated to this experiment for one session composed of a calibration phase of 10 minutes and a test phase of 10 minutes. This dataset is used to evaluate ofﬂine performances of the methods in the canonical training-test paradigm.

1) Canonical performances: In this section, performances will be evaluated using the classical training-test paradigm. Algorithms are calibrated on the data recorded during the training phase, and applied on the data recorded during the test phase (online). The Area Under ROC Curve (AUC), estimated on the classiﬁcation scores Eq.(14) will be used as criterion to evaluate the effectiveness of the trained classiﬁer. Table I reports these AUC for the 23 subjects and the three evaluated methods.

The MDM method offers the best performances among the three methods. Even if the mean improvement is small, the difference is signiﬁcant (t-test for paired sample; MDM vs. XDAWN : t(22) = 4.001, p = 0.0006 ; MDM vs. SWLDA : t(22) = 4.482, p = 0.0002). On the contrary, there is no signiﬁcant difference between the two reference methods (ttest for paired sample; XDAWN vs. SWLDA : t(22) = 1.172, p = 0.26). We can also note that the improvement is higher for subjects with low performances (0.75 < AUC < 0.9, e.g., subjects 4, 9, 18, 19 and 21). Overall, the proposed method exhibits an excellent classiﬁcation accuracy, despite its simplicity.

2) Effect of the size of the training set on performances:

The size of the calibration data-set is usually a critical parameter inﬂuencing dramatically the results. To evaluate this

effect on the MDM algorithm, we calibrate the algorithm using an increasing number of trials from the training set. Figure 1 shows the results of this test.

0.9

0.85

0.8

0.75

MeanAUC

0.7

0.65

0.6

MDM

0.55

SWLDA XDAWN

0.5

1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58 61

Number of repetition used for calibration

Figure 1. Performances of the three methods as a function of the number of trials used for the calibration. 1 repetition = 12 trials, 2 target and 10 non-target.

As expected, the three methods converge to their optimal value. The SWLDA is the method with the slowest convergence; due to the high dimension of the feature space, the model selection needs a lot of data to reach efﬁciency. On the contrary, the XDAWN method reduces the feature space and therefore needs less data for calibration. Finally, the MDM method shows the best results and the fastest convergence. Thus, the MDM method could be used either to achieve higher performance or to reduce the time spent in the calibration phases, while keeping the same accuracy. As example, in order to obtain a mean AUC of 0.85, only 13 repetitions are needed for the MDM, 22 for XDAWN and 52 for the SWLDA.

3) Effect of the latency and jitter of the evoked potential on performances: The correct detection of the evoked potentials relies on the fact that the evoked response is perfectly synchronized with the stimulus, i.e., it occurs always at the same time after each stimulus. In practice, a variable delay (jitter) and a ﬁxed delay (latency) is observed, due to technical factors ( Hardware / Software Trigger, screen rendering) as well as physiological factors (fatigue, stress, mental workload).

The different classiﬁcation methods are more or less robust to theses nuisances. These factors are simulated by adding artiﬁcial delays on the test data. To test the effect of latency, the triggers of the test data are shifted with a ﬁxed delay from -55ms to 55 ms. Results are reported in Figure 2. Performances are normalized with the AUC obtained with a zero delay and subjects 7 and 8 where removed; because of their low performances, close to the chance level, delays have almost no effects on theses two subjects.

In Figure 3, the effect of the jitter is studied by adding a random delay for each triggers of the test data. This delay is drawn from a normal distribution with a zero mean and standard deviation from 0ms to 55ms.

In both cases, the loss of performance induced by the delay is less important for the MDM than for the other methods. Because of the model selection, the SWLDA method is the

Table I AUC ON TEST DATA FOR THE 23 SUBJECTS OF THE DATASET I FOR THE 3 EVALUATED METHODS.

|Methdod<br><br>|1 2 3 4 5 6 7 8 9 10 11 12|
|---|---|
|MDM SWLDA XDAWN|0.89 0.93 0.97 0.88 0.95 0.90 0.65 0.65 0.87 0.97 0.94 0.86 0.84 0.90 0.97 0.81 0.90 0.91 0.55 0.69 0.79 0.96 0.89 0.84 0.89 0.90 0.97 0.85 0.91 0.90 0.56 0.66 0.79 0.95 0.83 0.86<br><br>|
| |13 14 15 16 17 18 19 20 21 22 23 mean (std)|
|MDM SWLDA XDAWN|0.88 0.92 0.93 0.91 0.98 0.84 0.78 0.97 0.90 0.95 0.96 0.89 (0.09)<br><br>0.87 0.91 0.91 0.90 0.95 0.76 0.73 0.95 0.84 0.93 0.97 0.86 (0.10)<br><br>0.88 0.90 0.93 0.91 0.96 0.77 0.74 0.96 0.84 0.92 0.96 0.86 (0.10)<br><br><br>|

105

| | | | | | | | | | | | | | |MD SW|M LDA|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | |XD|AWN|
| | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | |

100

95

Percentageofno−delayAUC

90

85

80

75

70

65

60

55

50

−54.7 −46.9 −39.1 −31.2 −23.4 −15.6 −7.8 0.0 7.8 15.6 23.4 31.2 39.1 46.9 54.7

Delay in ms

- Figure 2. Effect of the latency on the performances.

0.0 7.8 15.6 23.4 31.2 39.1 46.9 54.7

65

70

75

80

85

90

95

100

105

Std of delay in ms

PercentageofnodelayAUC

MDM

SWLDA XDAWN

- Figure 3. Effect of the jitter on the performances.

most sensitive method to the delay.

4) Effect of P1 on performances: The estimation of the super-covariance matrices explained in section III-B is supervised and requires the average P300 matrix P1. Therefore, it is interesting to see how sensitive the method is regarding to the parameter P1. To do so, we apply the same test described in section IV-C1, but replacing the subject speciﬁc estimation of P1 by the grand average P300 evoked response estimated on other users or using data from another experiment (data from Dataset II).

Results show that there is no statistical difference when a cross-subject P1 (CSP1) or a cross-experiment P1 (CEP1) is used compared to the subject speciﬁc P1 ( t-test for paired samples, P1 vs. CSP1 : t(22) = −0.776 , p = 0.45 ; P1 vs. CEP1 : t(22) = 0.175 , p = 0.86 ). These results, particularly meaningful, demonstrate that the critical parameters of the algorithm are the intra-class mean covariance matrices rather than the prototyped evoked responses. Interestingly, it is possible to use an evoked response from another experiment

without loss of performances, even if the electrode montage is different. This effect comes from the property of invariance by congruent projection of the Riemannian metric. Thus, the matrix P1 could be estimated in the sources space, with a different electrodes montage or electrodes permutation, and any kind of scaling factor could be applied. We will come back to this interesting property in the discussion section.

5) Cross-subjects performances: Results from the previous section show that the supervised estimation of the covariance matrices can be done in an unsupervised way by using the P300 average response from other subjects without loss of performances. However, calibration data are still required for the estimation of the intra-classe mean covariance matrices. Nevertheless, it is possible to use data from other subjects to estimate the mean covariance matrices as well. Table II report performances of the different methods for each subject when calibration is done using data from other subjects, according to a leave-one-out procedure.

In these circumstances, the MDM method offers the best performances with a mean AUC of 0.82. On the other hand, the XDAWN method displays a really poor performance. This is not surprising since the estimation of spatial ﬁlters are known to be very subject speciﬁc. Even if the performances of SWLDA are signiﬁcantly lower than those obtained with the MDM (t(22) = 1.76,p = 0.04), regarding to its subject speciﬁc performances, the SWLDA offers a good generalization across subjects.

We can also notice that for subject 7 the cross subject calibration offers better results as compared to the subject speciﬁc calibration. This is generally the case when the calibration data are of low quality, pointing to a general merit of generic initialization.

D. Dataset II

For a BCI game such brain invaders where the session are generally short (less than 10 minutes) it is not acceptable for the user to do a calibration phase before each game. The second dataset has been recorded to study the generalization of parameters across different sessions. Dataset II was recorded in realistic conditions using 16 golden-plated dry electrodes (Fp1-Fp2-F5-AFz-F6-T7-Cz-T8-P7-P3-Pz-P4P8-O1-Oz-O2) and a USBamp ampliﬁer (Guger Technologies, Graz, Austria). The signal was sampled at 512 Hz. 4 subjects participated to this experiment and made 6 sessions recorded on different days. Each session was composed of a single test phase, without any calibration phase, using cross subjects

Table II AUC ON TEST DATA FOR THE 23 SUBJECTS OF THE DATASET I IN A SUBJECT SPECIFIC AND CROSS SUBJECT (CS) MANNER.

| |1 2 3 4 5 6 7 8 9 10 11 12|
|---|---|
|MDM CS MDM|0.89 0.93 0.96 0.88 0.95 0.90 0.65 0.65 0.87 0.97 0.94 0.86 0.71 0.92 0.82 0.80 0.90 0.72 0.73 0.64 0.87 0.80 0.88 0.86<br><br>|
|SWLDA CS SWLDA<br><br>|0.84 0.90 0.96 0.81 0.90 0.91 0.55 0.69 0.79 0.96 0.89 0.84 0.71 0.84 0.93 0.72 0.82 0.77 0.76 0.67 0.74 0.86 0.79 0.75|
|XDAWN CS XDAWN<br><br>|0.89 0.90 0.96 0.85 0.91 0.90 0.56 0.66 0.79 0.95 0.83 0.86 0.60 0.86 0.86 0.77 0.73 0.79 0.75 0.64 0.67 0.77 0.76 0.70|
| |13 14 15 16 17 18 19 20 21 22 23 mean (std)|
|MDM CS MDM<br><br>|0.88 0.92 0.93 0.91 0.98 0.84 0.78 0.97 0.90 0.95 0.96 0.89 (0.09)<br>0.89 0.77 0.91 0.89 0.95 0.72 0.77 0.84 0.76 0.85 0.84 0.82 (0.08)<br>|
|SWLDA CS SWLDA|0.87 0.91 0.91 0.90 0.95 0.76 0.73 0.95 0.84 0.93 0.97 0.86 (0.10) 0.86 0.72 0.86 0.86 0.94 0.67 0.79 0.87 0.74 0.84 0.83 0.80 (0.08)<br><br>|
|XDAWN CS XDAWN|0.88 0.90 0.93 0.91 0.96 0.77 0.74 0.96 0.84 0.92 0.96 0.86 (0.10) 0.88 0.64 0.83 0.85 0.89 0.64 0.77 0.86 0.73 0.72 0.74 0.76 (0.09)<br><br>|

parameters for the ﬁrst session and cross sessions parameters for the next sessions. Ofﬂine results are reported in Fig. 4. We study ﬁrst the cross-subject performance by initializing the classiﬁer with all the data of the other subjects. Results of number of sessions ”0” represent the grand average AUC across all subjects and all sessions. Then we study the crosssession performance by initializing the classiﬁer of each subject with an increasing number of his/her own sessions and testing on the remaining sessions. For any n number of sessions used for calibration (x-axis), results represent the grand average AUC obtained on all combinations of the remaining 6 − n sessions for all subjects.

Mean AUC in function of the number of calibration sessions

Cross− subject

0.9

MeanAUC

0.85

0.8

Cross−session

0.75

MDM

XDAWN SWLDA

0.7

0 1 2 3 4 5

Number of sessions used for calibration

- Figure 4. Individual performances accross session for the 4 subjects when an increasing number of sessions are used for calibration.

First, the cross subject classiﬁcation gives a similar trend as the results obtained on the ﬁrst dataset. Here the MDM clearly outperform the reference methods. We could also notice that despite we have only four subjects in the database, the cross subject performances are surprisingly good. Second, the MDM methods shows better cross sessions performances as compared to SWLDA and XDAWN. In this experiment, the sessions are short and contain a small number of trial. For this reason, the SWLDA has difﬁculty to achieve a high AUC when the number of training sessions is small. On the average, the same performance could be obtained with only two sessions for the MDM and ﬁve sessions for the SWLDA.

E. Dataset III

Results on dataset I and II demonstrate the good properties of adaptation and generalization of the proposed method. These properties are necessary to obtain an efﬁcient adaptive use of the algorithm.

Dataset III was recorded in real-life conditions, using the same electrode montage and ampliﬁer as the Dataset II. Sessions were recorded during a live demonstration at the g.tec Workshop, held in our laboratory in Grenoble on March 5th 2013. Five subjects external to our laboratory played the Brain Invaders game for the ﬁrst time in their life in a noisy environment. They made a single session without calibration using the online adaptive implementation of the MDM described in section III-C. Figure 5 reports online results. The performance is reported in terms of number of repetitions needed to destroy the target alien for each of nine levels of the game. The adaptive MDM, implemented in python within the open source software OpenVibe [27], was initialized with parameters extracted using the data from the dataset II. As

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

Numberofrepetitions

- 0.5
- 1

- 1.5
- 2

2.5

3

- 3.5
- 4

1 2 3 4 5 6 7 8 9 Level of Brain Invaders

Figure 5. Mean and sd of the number of repetitions needed to destroy the target.

expected, the adaptation improves the performance (t-test for slope< 0: t(7) = −3.82,p = 0.007). On average players needed 2.5 repetitions at the beginning of the game session and only 1.5 for the last level. In addition, the variability decreases, and typically for the last two levels less than two repetitions only sufﬁce to destroy the target. This is a very good result as compared to the state-of-the-art.

V. CONCLUSION

We have proposed a new classiﬁcation method for ERPbased BCI that increases performance, reduces the number of data needed for the calibration and features good generalisation across sessions and subjects. In addition, this new method proves more robust against ﬁxed and variable delays on the trigger signals as compared to state-of-the-art methods. An adaptive implementation has been deployed on our real-life experiments allowing the user to play without any calibration (plug&play) while keeping a high accuracy. The Brain Invaders and the OpenViBE scenarios we use are open-source and available for download3.

VI. DISCUSSION

In this work a very simple classiﬁer (MDM) has been used in order to facilitate the adaptive implementation. In our previous works on motor imagery more sophisticated classiﬁcation algorithms has been developed, leading to higher performances as compared to the MDM. In [28], a geodesic ﬁltering was applied before the MDM in order to improve class separability. In [19], a SVM-kernel dedicated to covariance matrices was deﬁned and another way of dealing with intersession variability was proposed. These methods give promising results but show less stability in a cross-subject context. In future works we will investigate whether more complex classiﬁcation methods based on information geometry can be used in an adaptive context.

With the new deﬁnition of covariances matrices proposed in this article the Riemannian geometry framework can now be applied on all the three main BCI paradigms (SMR, ERP, SSEP) with only minor modiﬁcations. A single implementation of the classiﬁcation method can be used for the different paradigms, which is very convenient in terms of software development and maintenance. Besides the Riemannian frameworks, the new proposed estimation of covariance matrix for ERP brings permeability between states-of-the-art methods since the wide majority of signal processing alorithms for SMR-based BCIs rely on the manipulation of covariance matrices. For example, the well known CSP spatial ﬁltering and all its variations can now be applied for ERPs.

Finally, the property of invariance of the metric gives great freedom in the choice of the prototyped ERP matrix P1. This matrix could be drawn by hand, or generated with a wavelets basis, allowing, for example, to adapt the system to different sampling frequency.

However, this approach shows some limitations when the number of channels increase. If the number of channel is greater than the number of time sample in the trial, the covariance matrix is ill-conditioned and the computation of the Riemannian distance becomes impossible. In this context, a regularized estimate of the covariance matrix must be used, or if it is possible, a higher sampling frequency. In addition, if the number of channel is too big (> 64), the estimation of the mean covariance matrices might not converge. In this case, consider to use a smaller number of channel or apply a

3http://code.google.com/p/openvibe-gipsa-extensions/

subspace reduction (PCA) to decrease the dimensionality of the problem.

REFERENCES

- [1] F. Lotte, M. Congedo, A. L´ecuyer, F. Lamarche, B. Arnaldi et al., “A review of classiﬁcation algorithms for eeg-based brain–computer interfaces,” Journal of neural engineering, vol. 4, 2007.
- [2] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Multiclass Brain-Computer interface classiﬁcation by riemannian geometry,” IEEE Transactions on Biomedical Engineering, vol. 59, no. 4, pp. 920–928, 2012.
- [3] S. Fazli, C. Grozea, M. Danoczy, B. Blankertz, F. Popescu, and K.-r. M¨uller, “Subject independent eeg-based bci decoding,” in Advances in Neural Information Processing Systems, 2009, pp. 513–521.
- [4] P.-J. Kindermans, D. Verstraeten, and B. Schrauwen, “A bayesian model for exploiting application constraints to enable unsupervised training of a p300-based bci,” PloS one, vol. 7, no. 4, p. e33758, 2012.
- [5] P.-J. Kindermans, H. Verschore, D. Verstraeten, and B. Schrauwen, “A p300 bci for the masses: Prior information enables instant unsupervised spelling,” in Advances in Neural Information Processing Systems 25, 2012, pp. 719–727.
- [6] C. Gouy-Pailler, M. Congedo, C. Brunner, C. Jutten, and G. Pfurtscheller, “Nonstationary brain source separation for multiclass motor imagery,” Biomedical Engineering, IEEE Transactions on, vol. 57, no. 2, pp. 469–478, 2010.
- [7] M. Grosse-Wentrup and M. Buss, “Multiclass common spatial patterns and information theoretic feature extraction,” Biomedical Engineering, IEEE Transactions on, vol. 55, no. 8, pp. 1991–2000, 2008.
- [8] J. Farquhar, “A linear feature space for simultaneous learning of spatiospectral ﬁlters in BCI,” Neural Networks, vol. 22, no. 9, pp. 1278–1285, 2009.
- [9] B. Reuderink, J. Farquhar, M. Poel, and A. Nijholt, “A subjectindependent brain-computer interface based on smoothed, second-order baselining,” in Engineering in Medicine and Biology Society,EMBC, 2011 Annual International Conference of the IEEE, 2011, pp. 4600 – 4604.
- [10] S. Amari, H. Nagaoka, and D. Harada, Methods of information geometry. American Mathematical Society, 2000.
- [11] F. Barbaresco, “Innovative tools for radar signal processing based on cartan’s geometry of SPD matrices & information geometry,” in IEEE Radar Conference, 2008.
- [12] P. T. Fletcher and S. Joshi, “Principal geodesic analysis on symmetric spaces: Statistics of diffusion tensors,” in Computer Vision and Mathematical Methods in Medical and Biomedical Image Analysis, 2004, pp. 87–98.
- [13] O. Tuzel, F. Porikli, and P. Meer, “Pedestrian detection via classiﬁcation on Riemannian manifolds,” vol. 30, no. 10, pp. 1713–1727, 2008.
- [14] M. Congedo, C. Gouy-Pailler, and C. Jutten, “On the blind source separation of human electroencephalogram by approximate joint diagonalization of second order statistics,” Clinical Neurophysiology, vol. 119, no. 12, pp. 2677–2686, 2008.
- [15] P. Comon and C. Jutten, Handbook of Blind Source Separation: Independent component analysis and applications. Academic press, 2010.
- [16] V. Arsigny, P. Fillard, X. Pennec, and N. Ayache, “Geometric means in a novel vector space structure on symmetric positive-deﬁnite matrices,” SIAM journal on matrix analysis and applications, vol. 29, no. 1, pp. 328–347, 2007.
- [17] X. Pennec, P. Fillard, and N. Ayache, “A riemannian framework for tensor computing,” International Journal of Computer Vision, vol. 66, no. 1, pp. 41–66, 2006.
- [18] M. Moakher, “A differential geometric approach to the geometric mean of symmetric Positive-Deﬁnite matrices,” SIAM J. Matrix Anal. Appl., vol. 26, no. 3, pp. 735–747, 2005.
- [19] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Classiﬁcation of covariance matrices using a Riemannian-based kernel for bci applications,” Neurocomputing, vol. 112, pp. 172–178, 2013.
- [20] Y. Li, K. M. Wong, and H. DeBruin, “Eeg signal classiﬁcation based on a riemannian distance measure,” in Science and Technology for Humanity (TIC-STH), 2009 IEEE Toronto International Conference. IEEE, 2009, pp. 268–273.
- [21] Y. Li, K. Wong, and H. Bruin, “Electroencephalogram signals classiﬁcation for sleepstate decision-a riemannian geometry approach,” Signal Processing, IET, vol. 6, no. 4, pp. 288–299, 2012.

- [22] A. Barachant, S. Bonnet, M. Congedo, C. Jutten et al., “A brain-switch using riemannian geometry,” in Proceedings of the 5th International BCI Conference 2011, 2011, pp. 64–67.
- [23] F. Lotte and C. Guan, “Regularizing common spatial patterns to improve bci designs: uniﬁed theory and new algorithms,” Biomedical Engineering, IEEE Transactions on, vol. 58, no. 2, pp. 355–362, 2011.
- [24] M. Congedo, M. Goyat, N. Tarrin, G. Ionescu, L. Varnet, B. Rivet, R. Phlypo, N. Jrad, M. Acquadro, and C. Jutten, “”Brain Invaders”: a prototype of an open-source P300- based video game working with the OpenViBE platform,” in Proceedings of the 5th International BrainComputer Interface Conference 2011, Graz, Autriche, 2011, pp. 280– 283.
- [25] B. Rivet, A. Souloumiac, V. Attina, and G. Gibert, “xdawn algorithm to enhance evoked potentials: application to brain–computer interface,” Biomedical Engineering, IEEE Transactions on, vol. 56, no. 8, pp. 2035– 2043, 2009.
- [26] D. J. Krusienski, E. W. Sellers, F. Cabestaing, S. Bayoudh, D. J. Mcfarland, T. M. Vaughan, and J. R. Wolpaw, “A comparison of classiﬁcation techniques for the P300 speller,” Journal of Neural Engineering, vol. 3, no. 4, pp. 299–305, Oct. 2006.
- [27] Y. Renard, F. Lotte, G. Gibert, M. Congedo, E. Maby, V. Delannoy, O. Bertrand, and A. L´ecuyer, “Openvibe: an open-source software platform to design, test, and use brain-computer interfaces in real and virtual environments,” Presence: teleoperators and virtual environments, vol. 19, no. 1, pp. 35–53, 2010.
- [28] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Riemannian geometry applied to bci classiﬁcation,” in Latent Variable Analysis and Signal Separation. Springer, 2010, pp. 629–636.

Alexandre Barachant was born in Chateauroux, France, in 1985. In 2012, he recieved the Ph.D. degree in signal processing from the Grenoble University, Grenoble, France. He has worked at CEALETI during his Ph.D. on the topic of brain computer interfaces. He his actually a post-doc fellow at the Centre National de la Recherche Scientique (CNRS) in the GIPSA Laboratory, Grenoble, France. His current research interest include statistical signal processing, Riemannian geometry and classiﬁcation of neurophysiological recordings with applications

[Figure 1]

to brain computer interfaces.

Marco Congedo obtained the Ph.D. degree in Biological Psychology with a minor in Statistics from the University of Tennessee, Knoxville, in 2003. From 2003 to 2006 he has been a post-doc fellow at the French National Institute for Research in Informatics and Control (INRIA) and at France Telecom R&D, in France. Since 2007 Dr. Congedo is a Research Scientist at the ”Centre National de la Recherche Scientiﬁque” (CNRS) in the GIPSA Laboratory, Grenoble, France. Dr. Congedo has been the recipient of several awards, scholarships and re-

[Figure 2]

search grants. He is interested in basic human electroencephalography (EEG) and magnetoencephalography (MEG), real-time neuroimaging (neurofeedback and brain-computer interface) and multivariate statistical tools useful for EEG and MEG such as inverse solutions, blind source separation and Riemannian geometry. Currently he is Academic Editor of journal PLoS ONE.

