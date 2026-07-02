# Online and Ofﬂine Domain Adaptation for Reducing BCI Calibration Effort

Dongrui Wu, Senior Member, IEEE DataNova, NY USA E-mail: drwu09@gmail.com

arXiv:1702.02897v1[cs.LG]9Feb2017

Abstract—Many real-world brain-computer interface (BCI) applications rely on single-trial classiﬁcation of event-related potentials (ERPs) in EEG signals. However, because different subjects have different neural responses to even the same stimulus, it is very difﬁcult to build a generic ERP classiﬁer whose parameters ﬁt all subjects. The classiﬁer needs to be calibrated for each individual subject, using some labeled subject-speciﬁc data. This paper proposes both online and ofﬂine weighted adaptation regularization (wAR) algorithms to reduce this calibration effort, i.e., to minimize the amount of labeled subjectspeciﬁc EEG data required in BCI calibration, and hence to increase the utility of the BCI system. We demonstrate using a visually-evoked potential oddball task and three different EEG headsets that both online and ofﬂine wAR algorithms signiﬁcantly outperform several other algorithms. Moreover, through source domain selection, we can reduce their computational cost by about 50%, making them more suitable for real-time applications.

Index Terms—Brain-computer interface, event-related potential, EEG, domain adaptation, transfer learning

I. INTRODUCTION

Many real-world brain-computer interface (BCI) applications rely on single-trial classiﬁcation of event-related potentials (ERPs) in EEG signals [5], [39]. For example, in a rapid serial visual presentation (RSVP) based BCI system, a sequence of images are shown to the subject rapidly (e.g. 210 Hz) [10], [36], and the subject needs to detect some target images in them. The target images are much less frequent than the non-target ones, so that they can elicit P300 ERPs in the oddball paradigm. The P300 ERPs can be detected by a BCI system [35], and the corresponding images are then triaged for further inspection. Research [33], [39], [54] has shown that these BCI systems enable the subject to detect targets in large aerial photographs faster and more accurately than traditional standard searches.

Unfortunately, because different subjects have different neural responses to even the same visual stimulus [6], [7], [21], it is very difﬁcult, if not impossible, to build a generic ERP classiﬁer whose parameters ﬁt all subjects. So, we need to calibrate the classiﬁer for each individual subject, using some labeled subject-speciﬁc data. Reducing this calibration effort, i.e., minimizing the amount of labeled subject-speciﬁc data required in the calibration, would greatly increase the utility of the BCI system. This is the research problem tackled in this paper.

More speciﬁcally, we distinguish between two types of calibration in BCI:

- 1) Ofﬂine calibration, in which a pool of unlabeled EEG epochs have been obtained a priori, and a subject is queried to label some of these epochs, which are then used to train a classiﬁer to label the remaining epochs in that pool. A potential application of ofﬂine calibration is personalized automatic game highlight detection, e.g., a subject’s EEG signals are recorded continuously while watching a football game; after the game, the subject manually labels a few highlights, which are then used to train an ERP classiﬁer to detect more highlights.
- 2) Online calibration, in which some labeled EEG epochs are obtained on-the-ﬂy, and then a classiﬁer is trained from them to classify future EEG epochs. A potential application of online calibration is the afore-mentioned RSVP image tagging problem: at the beginning of the task, the subject is asked to explicitly indicate it (e.g., press a button) every time he/she detects a target image, and that information is used to train a P300 ERP classiﬁer. After a certain number of calibration epochs, the performance of the classiﬁer can become reliable enough so that it can label further images using EEG epochs only.

One major difference between ofﬂine calibration and online calibration is that, in ofﬂine calibration, the unlabeled EEG epochs can be used to help design the ERP classiﬁer, whereas in online calibration there are no unlabeled EEG epochs. Additionally, in ofﬂine calibration we can query any epoch in the pool for the label (an optimal query strategy can hence be designed by using machine learning methods such as active learning [42], [48]), but in online calibration usually the sequence of the epochs is pre-determined and the subject has no control over which epoch he/she will see next.

Many signal processing and machine learning approaches have been proposed to reduce the BCI calibration effort [29], [30]. They may be grouped into ﬁve categories [29]:

- 1) Regularization, which is a very effective machine learning approach for constructing robust models [41], especially when the training data size is small. A popular regularization approach in BCI calibration is shrinkage [27], which gives a regularized estimate of the covariance matrices.
- 2) Transfer/multi-task learning, which uses relevant data from other subjects to help the current subject [19], [46]. The transfer learning (TL) [32] based approaches are particularly popular [1], [19], [20], [40], [46], [48],

- [49], [52], [53], because in many BCI applications we can easily ﬁnd legacy data from the same subject in the same task or similar tasks, or legacy data from different subjects in the same task or similar tasks. These data, which will be called auxiliary data in this paper, can be used to improve the learning performance of a new subject, or for a new task.
- 3) Adaptive learning, which reﬁnes the machine learning model as new (labeled or unlabeled) subject-speciﬁc data are available [23], [52], [53]. The main approach in this category is semi-supervised learning [9], which is often used for ofﬂine BCI calibration where unlabeled data are available. Semi-supervised learning ﬁrst constructs an initial model from the labeled training data and then applies it to the unlabeled test data. The newly labeled test data are then integrated with the groundtruth training data to retrain the model, and hence to improve it iteratively.
- 4) Active learning, which optimally selects the most informative unlabeled samples to label [22], [31], [48], [50]. There are many criteria to determine which unlabeled samples are the most informative [42]. The most popular, and probably also the simplest, approach for classiﬁcation is to select the samples that are closest to the current decision boundary, because the classiﬁer is most uncertain about them. Active learning has been mainly used for ofﬂine BCI calibration, where unlabeled samples are available. However, a closely related technique, active class selection [24], can be used for online BCI calibration [49]. Its idea is to optimize the classes from which the new training samples are generated.
- 5) A priori physiological information, which can be used to construct the most useful EEG features. For example, prior information on which EEG channels are the most likely to be useful was used in [28] as a regularizer to optimize spatial ﬁlters, and beamforming has been used in [16] to ﬁnd relevant features from prior regions of interest to reduce the calibration data requirement.

Interestingly, these ﬁve categories of approaches are not mutually exclusive: in fact they can be freely combined to further reduce the amount of subject-speciﬁc calibration data. An optimal spatial ﬁlters was designed in [28] for efﬁcient subjectto-subject transfer by combining regularization and a prior information on which channels are the most likely to be useful.

- A collaborative ﬁltering approach was developed in [49], which combined TL and active class selection to minimize the online calibration effort. An active TL approach was proposed in [48] for ofﬂine calibration, which combined TL and active learning to minimize the ofﬂine calibration effort. An active weighted adaptation regularization approach, which combines active learning, TL, regularization and semi-supervised learning, was proposed in [51] to facilitate the switching between different EEG headsets. All these approaches are for BCI classiﬁcation problems. However, recently researchers have also started to apply these techniques for regression problems in BCI calibration. For example, a domain adaptation with model fusion approach, which combines regularization and

TL, was developed in [47] to estimate driver’s drowsiness online continuously.

This paper presents a comprehensive overview and comparison of the ofﬂine and online weighted adaptation regularization with source domain selection (wARSDS) algorithms, which we proposed recently [52], [53]. The ofﬂine wARSDS algorithm, which combined TL, regularization, and semisupervised learning, was ﬁrst developed in [53] for ofﬂine single-trial classiﬁcation of ERPs in a visually-evoked potential (VEP) oddball task. It was later extended to online calibration in a RSVP task [52], which still includes TL and regularization but not semi-supervised learning because unlabeled samples are not available in online calibration. In this paper we use a VEP oddball task and three different EEG headsets to show that they have consistently good performance across subjects and headsets. We also compare the performances of the ofﬂine and online wARSDS algorithms in identical experimental settings to investigate the effect of semi-supervised learning, and show that it can indeed help improve the calibration performance.

The remainder of the paper is organized as follows: Section II introduces the details of the ofﬂine wARSDS algorithm. Section III introduces the online wARSDS (OwARSDS) algorithm. Section IV describes the experiment setup that is used to evaluate the performances of different algorithms. Section V presents performance comparison of different ofﬂine calibration algorithms. Section VI presents performance comparison of different online calibration algorithms. Section VII compares the performances of ofﬂine and online algorithms. Finally, Section VIII draws conclusions.

II. WEIGHTED ADAPTATION REGULARIZATION WITH SOURCE DOMAIN SELECTION (WARSDS)

This section describes the ofﬂine wARSDS algorithm [51], [53], which originates from the adaptation regularization – regularized least squares (ARRLS) algorithm in [25]. We made several major enhancements to ARRLS to better handle classimbalance and multiple source domains, and also to make use of labeled samples in the target domain. wARSDS ﬁrst uses source domain selection (SDS) to select the closest source domains for a given target domain, then uses weighted adaptation regularization (wAR) for each selected source domain to build individual classiﬁers, and ﬁnally performs model fusion. For simplicity, we only consider 2-class classiﬁcation.

A. wAR: Problem Deﬁnition

A domain [25], [32] D in TL consists of a multi-dimensional feature space X and a marginal probability distribution P(x), i.e., D = {X,P(x)}, where x ∈ X. Two domains Ds and Dt are different if Xs = Xt, and/or Ps(x) = Pt(x).

A task [25], [32] T in TL consists of a label space Y and a conditional probability distribution Q(y|x). Two tasks Ts and Tt are different if Ys = Yt, or Qs(y|x) = Qt(y|x).

Given a source domain Ds with n labeled samples, {(x1,y1),...,(xn,yn)}, and a target domain Dt with ml labeled samples {(xn+1,yn+1),...,(xn+m

)} and mu

,yn+m

l

l

l+mu}, domain adaptation (DA) TL learns a target prediction function f : xt  → yt with low expected error on Dt, under the assumptions Xs = Xt, Ys = Yt, Ps(x) = Pt(x), and Qs(y|x) = Qt(y|x).

unlabeled samples {xn+m

l+1,...,xn+m

For example, in single-trial classiﬁcation of VEPs, EEG epochs from the new subject are in the target domain, while EEG epochs from an existing subject (usually different from the new subject) are in the source domain. When there are multiple source domains, we perform DA for each of them separately and then aggregate the classiﬁers. A sample consists of the feature vector for an EEG epoch from a subject in either domain, collected as a response to a speciﬁc visual stimulus. Though usually the source and target domains employ the same feature extraction method, generally their marginal and conditional probability distributions are different, i.e., Ps(x) = Pt(x) and Qs(y|x) = Qt(y|x), because the two subjects usually have different neural responses to the same visual stimulus [6], [7], [21]. As a result, the auxiliary data from a source domain cannot represent the primary data in the target domain accurately, and must be integrated with some labeled target domain data to induce an accurate target domain classiﬁer.

- B. wAR: The Learning Framework Because

P(x,y) P(x)

f(x) = Q(y|x) =

[Figure 1]

Q(x|y)P(y) P(x)

, (1)

=

[Figure 2]

to use the source domain data in the target domain, we need to make sure Ps(xs) is close to Pt(xt), Qs(xs|ys) is close to Qt(xt|yt), and Ps(y) is also close to Pt(y). However, in this paper we focus only on the ﬁrst two requirements by assuming all subjects conduct similar VEP tasks [so Ps(y) and Pt(y) are intrinsically close]. Our future research will consider the more general case that Ps(y) and Pt(y) are different.

Let the classiﬁer be f(x) = wTφ(x), where w is the classiﬁer parameters, and φ : X  → H is the feature mapping function that projects the original feature vector to a Hilbert space H. As in [51], [53], the learning framework of wAR is formulated as:

n+ml

n

wt,iℓ(f(xi),yi)

ws,iℓ(f(xi),yi) + wt

f =argmin

f∈HK

i=n+1

i=1

+ σ f 2K + λ[Df,K(Ps,Pt) + Df,K(Qs,Qt)] (2) where ℓ is the loss function, K ∈ R(n+m

l+mu)×(n+ml+mu) is the kernel matrix with K(xi,xj) = φ(xi),φ(xj) , and σ and λ are non-negative regularization parameters. wt is the overall weight for target domain samples, which should be larger than 1 so that more emphasis is given to target domain samples than source domain samples1. ws,i and wt,i are the

1Generally the number of labeled samples in the source domain is much larger than that in the target domain in both ofﬂine and online calibration scenarios, i.e., n ≫ ml. However, eventually the learned classiﬁer will be applied to the target domain. So, the target domain should be emphasized. We choose wt > 1 so that the ml labeled target domain samples are less overwhelmed by the n source domain samples.

weight for the ith sample in the source domain and target domain, respectively, i.e.,

- ws,i =

1, xi ∈ Ds,1 n1/(n − n1), xi ∈ Ds,2

(3)

- wt,i =

1, xi ∈ Dt,1 m1/(ml − m1), xi ∈ Dt,2

(4)

in which Ds,c = {xi|xi ∈ Ds ∧ yi = c, i = 1,...,n} is the set of samples in Class c of the source domain, Dt,c = {xj|xj ∈ Dt ∧ yj = c, j = n + 1,...,n + ml} is the set of samples in Class c of the target domain, nc is the number of elements in Ds,c, and mc is the number of elements in Dt,c. The goal of ws,i (wt,i) is to balance the number of samples from difference classes in the source (target) domain. This is very important, because class imbalance is intrinsic to many applications [18], particularly BCI applications. In many cases the minority class is the one of particular interest (e.g., the VEP experiment presented in this paper), but it can be easily overwhelmed by the majority class if not properly weighted. Of course, there are many other approaches for handling class imbalance [18], [26], [37]. We used the weighting approach for its simplicity.

Brieﬂy speaking, the 1st term in (2) minimizes the loss on ﬁtting the labeled samples in the source domain, the 2nd term minimizes the loss on ﬁtting the labeled samples in the target domain, the 3rd term minimizes the structural risk of the classiﬁer, and the 4th term minimizes the distance between the marginal probability distributions Ps(xs) and Pt(xt), and also the distance between the conditional probability distributions Qs(xs|ys) and Qt(xt|yt).

According to the Representer Theorem [3], [25], the solution of (2) can be expressed as:

where

n+ml+mu

αiK(xi,x) = αTK(X,x) (5)

f(x) =

i=1

l+mu]T (6) and α = [α1,...,αn+m

X = [x1,...,xn+m

l+mu]T are coefﬁcients to be computed.

C. wAR: Loss Functions Minimization Let

l+mu]T (7)

y = [y1,...,yn+m

where {y1,...,yn} are known labels in the source domain, {yn+1,...,yn+m

} are known labels in the target domain, and {yn+m

l

l+mu} are pseudo labels for the unlabeled target domain samples, i.e., labels estimated using available sample information in both source and target domains.

l+1,...,yn+m

l+mu)×(n+ml+mu) as a diagonal matrix with

Deﬁne E ∈ R(n+m

Eii =   

ws,i, 1 ≤ i ≤ n wtwt,i, n + 1 ≤ i ≤ n + ml 0, otherwise

(8)

We use the squared loss in this paper:

ℓ(f(xi),yi) = (yi − f(xi))2 (9) Substituting (5) and (9) into the ﬁrst two terms in (2), we

have

n+ml

n

wt,iℓ(f(xi),yi)

ws,iℓ(f(xi),yi) + wt

i=n+1

i=1

n+ml

n

wt,i(yi − f(xi))2

ws,i(yi − f(xi))2 + wt

=

i=n+1

i=1

n+ml+mu

Eii(yi − f(xi))2

=

i=1

=(yT − αTK)E(y − Kα) (10)

- D. wAR: Structural Risk Minimization

As in [25], we deﬁne the structural risk as the squared norm of f in HK, i.e.,

f 2K =

n+ml+mu

i=1

n+ml+mu

j=1

αiαjK(xi,xj) = αTKα (11)

- E. wAR: Marginal Probability Distribution Adaptation

As in [25], we compute Df,K(Ps,Pt) using the projected maximum mean discrepancy (MMD) between the source and target domains:

Df,K(Ps,Pt) =

1 n

[Figure 3]

n

i=1

f(xi) −

1 ml + mu

[Figure 4]

n+ml+mu

i=n+1

f(xi)

2

= αTKM0Kα (12) where M0 ∈ R(n+m

l+mu)×(n+ml+mu) is the MMD matrix:

(M0)ij =

 



1

[Figure 5]

n2, 1 ≤ i ≤ n,1 ≤ j ≤ n

1

[Figure 6]

(ml+mu)2, n + 1 ≤ i ≤ n + ml + mu,

n + 1 ≤ j ≤ n + ml + mu −1

[Figure 7]

n(ml+mu), otherwise

(13)

- F. wAR: Conditional Probability Distribution Adaptation

As in [25], we ﬁrst compute pseudo labels for the unlabeled target domain samples and construct the label vector y in (7). These pseudo labels can be computed using the classiﬁer built in the previous iteration if wAR is used iteratively, or estimated using another classiﬁer, e.g., a support vector machine (SVM) [45]. We then compute the projected MMD with respect to each class.

Let Ds,c = {xi|xi ∈ Ds ∧ yi = c, i = 1,...,n} be the set of samples in Class c of the source domain, Dt,c = {xj|xj ∈ Dt∧yj = c, j = n+1,...,n+ml+mu} be the set of samples in Class c of the target domain, nc be the number of elements in Ds,c, and mc be the number of elements in Dt,c. Then,

the distance between the conditional probability distributions in the two domains is computed as:

2

f(xj)

  1

2

1 mc x

f(xi) −

Df,K(Qs,Qt) =

[Figure 8]

[Figure 9]



nc x

c=1

i∈Ds,c

j∈Dt,c

(14)

Substituting (5) into (14), it follows that Df,K(Qs,Qt)

2

αTK(X,x)

  1

2

1 mc x

αTK(X,x) −

=

[Figure 10]

[Figure 11]



nc x

c=1

i∈Ds,c

j∈Dt,c

2

αTKMcKα = αTKMKα (15)

=

c=1

where

M = M1 + M2 (16) in which M1 and M2 are MMD matrices computed as:

1/n2c, xi,xj ∈ Ds,c 1/m2c, xi,xj ∈ Dt,c −1/(ncmc), xi ∈ Ds,c,xj ∈ Dt,c,

 

(17)

(Mc)ij =

or xj ∈ Ds,c,xi ∈ Dt,c 0, otherwise



- G. wAR: The Closed-Form Solution Substituting (10), (11), (12) and (15) into (2), we have

f = argmin

f∈HK

(yT − αTK)E(y − Kα)

+ σαTKα + λαTK(M0 + M)Kα (18)

Setting the derivative of the objective function above to 0 leads to the following closed-form solution for α:

α = [(E + λM0 + λM)K + σI]−1Ey (19)

- H. Source Domain Selection (SDS)

When there are multiple source domains, it is very timeconsuming to perform wAR for each source domain and then aggregate the results. Additionally, aggregating results from source domains that are outliers or very different from the target domain may also hurt the classiﬁcation performance. So, we introduce a source domain selection approach [53], which selects the closest source domains to reduce the computational cost, and also to (potentially) improve the classiﬁcation performance.

Assume there are Z different source domains. For the zth source domain, we ﬁrst compute mz,c (c = 1,2), the mean feature vector of each class. Then, we also compute mt,c, the mean feature vector of each target domain class, by making use of the ml known labels and the mu pseudo-labels. The distance between the two domains is then computed as:

2

d(z,t) =

c=1

mz,c − mt,c (20)

We next cluster these Z distances, {d(z,t)}z=1,...,Z, by kmeans clustering, and ﬁnally choose the cluster that has the smallest centroid, i.e., the source domains that are closest to the target domain. In this way, on average we only need to perform wAR for Z/k (k is the number of clusters in kmeans clustering) source domains, corresponding to a 50% computational cost saving if k = 2. A larger k will result in a larger saving; however, when k is too large, there may not be enough source domains selected for wAR, and hence the classiﬁcation performance may be unstable. So, there is a trade-off between computational cost saving and classiﬁcation performance. k = 2 was used in this paper, and it demonstrated satisfactory performance.

- I. The Complete wARSDS Algorithm

The pseudo code for the complete wARSDS algorithm is shown in Algorithm 1. It ﬁrst uses SDS to select the closest source domains, then performs wAR for each of them separately to build individual classiﬁers, and ﬁnally aggregates them using a weighted average, where the weights are the corresponding training accuracies.

- J. Discussions

As mentioned at the beginning of this section, the formulation and derivation of wAR closely resemble the ARRLS algorithm in [25]; however, there are several major differences:

- 1) wAR assumes a subject or an oracle is available to label a small number of samples in the target domain, whereas ARRLS assumes all target domain samples are unlabeled. As a result, wAR can be iterative, and the classiﬁer can be updated every time new labeled target domain samples are available.
- 2) wAR explicitly considers the class imbalance problem in both source and target domains by introducing the classdependent weights on samples. As it will be shown in Section IV, this makes a huge difference in the balanced classiﬁcation accuracy for the class imbalance problem, which is intrinsic in ERP-based BCI systems.
- 3) ARRLS also includes manifold regularization [3]. We investigated it but was not able to observe improved performance in our application, so it is not included in this paper.

Finally, when combined with SDS, wARSDS can effectively handle multiple source domains, whereas ARRLS only considers one source domain.

III. ONLINE WEIGHTED ADAPTATION REGULARIZATION WITH SOURCE DOMAIN SELECTION (OWARSDS)

This section introduces the OwARSDS algorithm [52], which extends the ofﬂine wARSDS algorithm to online BCI calibration. OwARSDS ﬁrst uses SDS to select the closest source domains, then performs online weighted adaptation regularization (OwAR) for each selected source domain to build individual classiﬁers, and ﬁnally aggregates them.

- A. OwAR: The Learning Framework

Using the notations introduced in the previous section, the learning framework of OwAR can still be formulated as (2). However, because in online calibration there are no unlabeled target domain samples, the kernel matrix Ko has dimensionality (n+ml)×(n+ml), instead of (n+ml+mu)×(n+ml+mu) in ofﬂine calibration. As a result, the solution of (2) admits a different expression:

fo(x) =

n+ml

i=1

αoiKo(xi,x) = (αo)TKo(Xo,x) (21) where

Xo = [x1,...,xn+m

l

]T (22) and αo = [α1,...,αn+m

l

]T are coefﬁcients to be computed.

It has been shown [52] that the closed-form solution for αo is:

αo = [(Eo + λM0o + λMo)Ko + σI]−1Eoyo (23) Next we brieﬂy introduce how the various terms in (23) are derived.

- B. OwAR: Loss Functions Minimization Deﬁne

yo = [y1,...,yn+m

l

]T (24)

where {y1,...,yn} are known labels in the source domain, and {yn+1,...,yn+m

l

} are known labels in the target domain. Deﬁne also Eo ∈ R(n+m

l)×(n+ml) as a diagonal matrix with

Eiio =

ws,i, 1 ≤ i ≤ n wtwt,i, n + 1 ≤ i ≤ n + ml

(25) Then, following the derivation in (10), we now have

n

i=1

ws,iℓ(fo(xi),yi) + wt

n+ml

i=n+1

wt,iℓ(fo(xi),yi)

=[(yo)T − (αo)TKo]Eo(yo − Koαo) (26)

- C. OwAR: Structural Risk Minimization Again, we deﬁne the structural risk as the squared norm of

fo in HK, i.e.,

fo 2K = (αo)TKoαo (27)

- D. OwAR: Marginal Probability Distribution Adaptation

We compute Dfo,Ko(Ps,Pt) using the projected MMD between the source and target domains:

2

n+ml

n

1 ml

1 n

fo(xi)

fo(xi) −

Dfo,Ko(Ps,Pt) =

[Figure 12]

[Figure 13]

i=n+1

i=1

= (αo)TKoM0oKoαo (28) where M0o ∈ R(n+m

l)×(n+ml) is the MMD matrix:

1

n2, 1 ≤ i ≤ n,1 ≤ j ≤ n

 

[Figure 14]

1

m2l , n + 1 ≤ i ≤ n + ml,

[Figure 15]

(M0o)ij =

(29)

n + 1 ≤ j ≤ n + ml −1



nml, otherwise

[Figure 16]

Algorithm 1. The ofﬂine wARSDS algorithm [51], [53].

[Figure 17]

Input: Z source domains, where the zth (z = 1, ..., Z) domain has nz labeled samples {xzi , yiz}i=1,...,nz; ml labeled target domain samples, {xtj, yjt}j=1,...,ml; mu unlabeled target domain samples, {xtj}j=ml+1,...,ml+mu; Parameters wt, σ and λ in (2); Parameter k in k-means clustering of SDS.

Output: The wARSDS classiﬁer f(x).

⊲ SDS starts

if ml == 0 then Retain all Z source domains; Compute pseudo-labels {yj}j=nz+ml+1,...,nz+ml+mu using

another classiﬁer, e.g., an SVM;

Go to wAR. else

Compute pseudo-labels {yj}j=nz+ml+1,...,nz+ml+mu using the wARSDS classiﬁer built from the previous iteration;

for z = 1, 2, ..., Z do

Compute d(z,t), the distance between the target domain

and the zth source domain, by (20). end for Cluster {d(z, t)}z=1,...,Z by k-means clustering; Retain the Z′ source domains that belong to the cluster with

the smallest centroid. end if

⊲ SDS ends; wAR starts Choose a kernel function K(xi, xj); for z = 1, 2, ..., Z′ do

Construct the feature matrix X in (6); Compute the kernel matrix Kz from X; Construct y in (7), E in (8), M0 in (13), and M in (16); Compute α by (19) and record it as αz; Use α to classify the nz +ml labeled samples and record the

accuracy, wz; end for

⊲ wAR ends; Aggregation starts return f(x) = Z

′

z=1 wzαzKz(X, x).

[Figure 18]

Algorithm 2. The online OwARSDS algorithm [52].

[Figure 19]

Input: Z source domains, where the zth (z = 1, ..., Z) domain has nz labeled samples {xzi , yiz}i=1,...,nz; ml labeled target domain samples, {xtj, yjt}j=1,...,ml;

Parameters wt, σ and λ in (2); Parameter k in k-means clustering of SDS.

Output: The OwARSDS classiﬁer fo(x).

⊲ SDS starts if ml == 0 then

Retain all Z source domains;

Go to OwAR. else

for z = 1, 2, ..., Z do

Compute d(z, t), the distance between the target domain

and the zth source domain, by (20). end for Cluster {d(z, t)}z=1,...,Z by k-means clustering; Retain the Z′ source domains that belong to the cluster with

the smallest centroid. end if

⊲ SDS ends; OwAR starts Choose a kernel function Ko(xi, xj) ; for z = 1, 2, ..., Z′ do

Construct the feature matrix Xo in (22); Compute the kernel matrix Kzo from Xo; Construct yo in (24), Eo in (25), M0o in (29), Mo in (30); Compute αo by (19) and record it as αoz; Use αoz to classify the nz + ml labeled samples and record

the accuracy, wzo; end for

⊲ OwAR ends; Aggregation starts return fo(x) = Z

′

z=1 wzoαozKzo(Xo, x).

[Figure 20]

- E. OwAR: Conditional Probability Distribution Adaptation

In ofﬂine calibration, to minimize the discrepancy between the conditional probability distributions in the source and target domains, we need to ﬁrst compute the pseudo-labels for the mu unlabeled target domain samples. In online calibration, because there are no unlabeled target domain samples, this step is skipped. Following the derivation of (15), we still have:

Dfo,Ko(Qs,Qt) = (αo)TKoMoKoαo (30) where Mo is still computed by (16), but using only the n source domain samples and ml target domain samples.

- F. Source Domain Selection (SDS)

The SDS procedure in OwARSDS is almost identical to that in wARSDS. The only difference is that the latter also makes use of the mu unlabeled target domain samples in computing mt,c in (20), whereas the former only uses the ml labeled target domain samples, because there are no unlabeled target domain samples in online calibration.

- G. The Complete OwARSDS Algorithm

The pseudo code for the complete OwARSDS algorithm is described in Algorithm 2. It ﬁrst uses SDS to select the

closest source domains, then performs OwAR for each of them separately to build individual classiﬁers, and ﬁnally aggregates them using a weighted average, where the weights are the corresponding training accuracies. Observe that OwARSDS is very similar to wARSDS, the major difference being that no unlabeled target domain samples are available for use in OwARSDS.

IV. THE VEP ODDBALL EXPERIMENT

This section describes the setup of the VEP oddball experiment, which is used in the following three sections to evaluate the performances of different algorithms.

A. Experiment Setup

A two-stimulus VEP oddball task was used [38]. In this task, participants were seated in a sound-attenuated recording chamber, and image stimuli were presented to them at a rate of 0.5 Hz (one image every two seconds). The images (152×375 pixels), presented for 150 ms at the center of a 24 inch Dell P2410 monitor at a distance of approximately 70 cm, were either an enemy combatant [target; an example is shown in Fig. 1(a)] or a U.S. Soldier [non-target; an example is shown

in Fig. 1(b)]. The subjects were instructed to maintain ﬁxation on the center of the screen and identify each image as being target or non-target with a unique button press as quickly and accurately as possible2. A total of 270 images were presented to each subject, among which 34 were targets. The experiments were approved by U.S. Army Research Laboratory (ARL) Institutional Review Board. The voluntary, fully informed consent of the persons used in this research was obtained as required by federal and Army regulations [43], [44]. The investigator has adhered to Army policies for the protection of human subjects.

removed epochs with incorrect button press responses3. The ﬁnal numbers of epochs from the 14 subjects are shown in Table I. Observe that there is signiﬁcant class imbalance for every subject; that’s why we need to use ws,i and wt,i in (2) to balance the two classes in both domains.

Each [0, 0.7] second epoch contains hundreds of raw EEG magnitude samples (e.g., 64 × 0.7 × 21 = 924 for BioSemi). To reduce the dimensionality, we performed a simple principal component analysis (PCA) to take the scores on the ﬁrst 20 principal components as features. We then normalized each feature dimension separately to [0,1].

[Figure 21]

[Figure 22]

(a) (b)

- Fig. 1. Example images of (a) a target; (b) a non-target.

18 subjects participated the experiments, which lasted on average 15 minutes. Signals for each subject were recorded with three different EEG headsets, including a 64-channel 512Hz BioSemi ActiveTwo system, a 9-channel 256Hz Advanced Brain Monitoring (ABM) X10 system, and a 14channel 128Hz Emotiv EPOC headset. However, due to some exceptions at the experiment, data were correctly recorded for only 16 subjects for ABM, 15 subjects for BioSemi, and 15 subjects for Emotiv. There were 14 subjects whose data were correctly recorded for all three headsets, so we used only these 14 subjects in this study.

B. Preprocessing and Feature Extraction

The preprocessing and feature extraction method for all three headsets was the same, except that for ABM and Emotiv headsets we used all the channels, but for the BioSemi headset we only used 21 channels (Cz, Fz, P1, P3, P5, P7, P9, PO7, PO3, O1, Oz, POz, Pz, P2, P4, P6, P8, P10, PO8, PO4, O2) mainly in the parietal and occipital areas, as in [48].

EEGLAB [12] was used for EEG signal preprocessing and feature extraction. For each headset, we ﬁrst band-passed the EEG signals to [1, 50] Hz, then downsampled them to 64 Hz, performed average reference, and next epoched them to the [0,0.7] second interval timelocked to stimulus onset. We removed mean baseline from each channel in each epoch and

2In the traditional oddball paradigm, subjects are only asked to respond to the target (oddball) stimuli. In our experiment we asked the subjects to respond to both types of stimuli so that we can remove epochs with incorrect responses from our analysis. Additionally, the experimental data will enable other analyses including the response time to different types of stimuli. Similar experimental settings have been used in [11], [17].

C. Performance Measure

Let m+ and m− be the true number of epochs from the target and non-target class, respectively. Let mˆ + and mˆ − be the number of epochs that are correctly classiﬁed by an algorithm as target and non-target, respectively. Then, we compute

mˆ − m−

mˆ + m+

, a− =

a+ =

[Figure 23]

[Figure 24]

where a+ is the classiﬁcation accuracy on the target class, and a− is the classiﬁcation accuracy on the non-target class.

The following balanced classiﬁcation accuracy (BCA) was then used as the performance measure in this paper:

a+ + a− 2

. (31) V. PERFORMANCE EVALUATION OF OFFLINE CALIBRATION ALGORITHMS

BCA =

[Figure 25]

This selection presents performance comparison of wARSDS with several other ofﬂine calibration algorithms. A. Calibration Scenario

Although we knew the labels of all EEG epochs for all 14 subjects in the VEP experiment, we simulated a realistic ofﬂine calibration scenario: we had labeled EEG epochs from 13 subjects, and also all epochs from the 14th subject, but initially none of them was labeled. Our goal was to iteratively label epochs from the 14th subject and build a classiﬁer so that his/her remaining unlabeled epochs can be reliably classiﬁed.

The ﬂowchart for the simulated ofﬂine calibration scenario is shown in Fig. 2(a). Assume the 14th subject has m sequential epochs in the VEP experiment, and we want to label p epochs in each iteration, starting from zero. We ﬁrst generate a random number m0 ∈ [1,m], representing the starting position in the VEP sequence. Then, in the ﬁrst iteration, we use the m unlabeled epochs from the 14th subject and all labeled epochs from the other 13 subjects to build different classiﬁers and compute their BCAs on the m unlabeled epochs. In the second iteration, we obtain labels for Epochs4 m0, m0 +1, ...,

- 3Button press responses were not recorded for most subjects using the ABM headset, so we used all 270 epochs for them.
- 4For ofﬂine calibration, the labeled epochs need not to be sequential: they can be randomly selected from the m epochs. However, the labeled epochs are always sequential in online calibration. To facilitate the comparison between ofﬂine and online algorithms, we used sequential sampling in both ofﬂine and online calibrations. But note that there is no statistic difference between random sampling and sequential sampling in ofﬂine calibration.

TABLE I NUMBER OF EPOCHES FOR EACH SUBJECT AFTER PREPROCESSING. THE NUMBERS OF TARGET EPOCHS ARE GIVEN IN THE PARENTHESES.

Subject 1 2 3 4 5 6 7 8 9 10 11 12 13 14 BioSemi 241 (26) 260 (24) 257 (24) 261 (29) 259 (29) 264 (30) 261 (29) 252 (22) 261 (26) 259 (29) 267 (32) 259 (24) 261 (25) 269 (33) Emotiv 263 (28) 265 (30) 266 (30) 255 (23) 264 (30) 263 (32) 266 (30) 252 (22) 261 (26) 266 (29) 266 (32) 264 (33) 261 (26) 267 (31) ABM 270 (34) 270 (34) 235 (30) 270 (34) 270 (34) 270 (34) 270 (34) 270 (33) 270 (34) 239 (30) 270 (34) 270 (34) 251 (31) 270 (34)

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

m0 + p − 1 from the 14th subject, build different classiﬁers, and compute their BCAs on the remaining m − p unlabeled epochs. We iterate until the maximum number of iterations is reached. When the end of the VEP sequence is reached during the iteration, we rewind to the beginning of the sequence, e.g., if m0 = m, then Epoch m0 + 1 is the 1st epoch in the VEP sequence, Epoch m0 + 2 is the 2nd, and so on.

- 4) TLSDS, which also performs SDS before the above TL algorithm.
- 5) ARRLS, which was proposed in [25] (manifold regularization was removed), and is also the wAR algorithm introduced in Algorithm 1, by setting wt = ws,i = wt,i = 1.
- 6) wAR, which excludes the SDS part in Algorithm 1.

To obtain statistically meaningful results, the above process was repeated 30 times for each subject, each time with a random starting point m0. We repeated this procedure 14 times so that each subject had a chance to be the “14th” subject.

Weighted libSVM [8] with RBF kernel was used as the classiﬁer in BL1, BL2, TL and TLSDS. The optimal RBF parameter was found by cross-validation. We chose wt = 2, σ = 0.1, and λ = 10, following the practice in [25], [51], [53].

|m unlabeled epochs from the 14th subject| |
|---|---|
| | |

|No epochs from the 14th subject| |
|---|---|
| | |

C. Experimental Results

|Set ; Generate a random number m0 [1,m]<br><br>i 0| |
|---|---|
| | |

|Set ; Generate a random number m0 [1,m]<br><br>i 0| |
|---|---|
| | |

The BCAs of the seven algorithms, averaged over the 30 runs and across the 14 subjects, are shown in Fig. 3 for the three headsets. Observe that:

| |Labeled epochs from the other 13 subjects|
|---|---|
| | |

| |Labeled epochs from the other 13 subjects|
|---|---|
| | |

|Train an offline classifier| |
|---|---|
| | |

|Train an online classifier| |
|---|---|
| | |

|Compute BCA on the<br><br>unlabeled epochs from the 14th subject<br><br>m i p| |
|---|---|
| | |

|Compute BCA on the<br><br>unlabeled epochs from the 14th subject<br><br>m i p| |
|---|---|
| | |

0.9

0.9

0.8

0.8

i i max

i i max

## BCA

## BCA

Yes Label p epochs

Yes Generate p labeled epochs

0.7

0.7

m 0 i p,m0 i p 1, ,

0.6

0.6

m 0 i p,m0 i p 1, ,

from the 14th subject;

from the 14th subject;

m 0 i 1 p 1

m 0 i 1 p 1

0.5

0.5

i i 1

i i 1

0 20 40 60 80 100

0 20 40 60 80 100

(a)

(b)

ml

ml

- Fig. 2. Flowcharts of the calibration scenarios. (a) ofﬂine; (b) online.

(a)

### (b)

|BL1 BL2 TL<br><br>TLSDS ARRLS wAR<br><br>wARSDS|
|---|

0.9

B. Algorithms

0.8

BCA

We compared the performance of wARSDS with six other algorithms [53]:

0.7

0.6

- 1) BL1, a baseline approach in which we assume we know labels of all samples from the new subject, and use 5fold cross-validation and SVM to ﬁnd the highest BCA. This represents an upper bound of the BCA we can get, by using the data from the new subject only.
- 2) BL2, which is a simple iterative procedure: in each iteration we randomly select ﬁve unlabeled samples from the new subject to label, and then train an SVM classiﬁer by 5-fold cross-validation. We iterate until the maximum number of iterations is reached.
- 3) TL, which is the TL algorithm introduced in [48]. It simply combines the labeled samples from the new subject with samples from each existing subject and train an SVM classiﬁer. The ﬁnal classiﬁer is a weighted average of all individual classiﬁers, and the weights are the corresponding cross-validation BCAs. Note that this algorithm can be used both online and ofﬂine, because it does not use any information from the unlabeled epochs.

0.5

0 20 40 60 80 100

ml

(c)

Fig. 3. Average BCAs of the seven ofﬂine algorithms across the 14 subjects, using different EEG headsets. (a) BioSemi; (b) ABM; (c) Emotiv.

- 1) Generally the performances of all algorithms (except BL1, which is not iterative) increased as more labeled subject-speciﬁc samples were available, which is intuitive.
- 2) BL2 cannot build a classiﬁer when there were no labeled subject-speciﬁc samples at all (observe that the BCA

for ml = 0 on the BL2 curve in Fig. 3 was always 0.5, representing random guess), but all TL/DA based algorithms can, because they can make use of information from other subjects. Moreover, without any labeled

###### BL2

###### TL

###### TLSDS

###### ARRLS

###### wAR

###### wARSDS

subject-speciﬁc samples, wAR and wARSDS can build a classiﬁer with a BCA of 68.20% for BioSemi, 61.45% for ABM, and 64.17% for Emotiv, much better than random guess.

40

200

40

20

20

20

20

100

20

0

0

0

0

0

0

0.6 0.8

0.6 0.8

0.6 0.7 0.8

0.5 0.6

0.6 0.8

0.6 0.8

###### BL2

###### TL

###### TLSDS

###### ARRLS

###### wAR

###### wARSDS

50

50

40

40

50

100

20

20

- 3) Generally the performance of TL was worse than BL2, suggesting that it cannot cope well with large individual differences among the subjects5.
- 4) TLSDS always outperformed TL. This is because TL used a very simple way to combine the labeled samples from the new and existing subjects, and hence an existing subject whose ERPs are signiﬁcantly different from the new subject’s would have a negative impact on the ﬁnal BCA. SDS can identify and remove (some of) such subjects, and hence beneﬁted the BCA.
- 5) ARRLS demonstrated the worst BCA, because all other algorithms explicitly handled class-imbalance using weights, whereas ARRLS did not. For our dataset, the non-target class had seven times more samples than the target class, so many times ARRLS simply classiﬁed all samples as non-target, resulting in a BCA of 0.5.
- 6) wAR and wARSDS signiﬁcantly outperformed BL2, TL, TLSDS and ARRLS. This is because a sophisticated DA approach was used in wAR and wARSDS, which explicitly considered class imbalance, and was optimized not only for high classiﬁcation accuracy, but also for small structural risk and close feature similarity between the two domains.
- 7) wARSDS and wAR had very similar performance, but instead of using 13 auxiliary subjects, wARSDS only used on average 6.84 subjects for BioSemi, 6.03 subjects for ABM, and 6.85 subjects for Emotiv, corresponding to 47.38%, 53.62% and 47.31% computational cost saving, respectively.

0

0

0

0

0

0

0.5 0.6 0.7

0.5 0.6 0.7

0.5 0.6 0.7

0.5 0.55

0.4 0.6 0.8

0.4 0.6 0.8

###### BL2

###### TL

###### TLSDS

###### ARRLS

###### wAR

wARSDS

100

20

20

20

20

20

50

10

10

0

0

0

0

0

0

0.6 0.8

0.6 0.8

0.5 0.6 0.7

0.5 0.51 0.52

0.6 0.8

0.6 0.8

Fig. 4. Histograms of the AUPCs of the six algorithms on the three headsets. Top: BioSemi; middle: ABM; bottom: Emotiv.

We treated the algorithm type (BL2, TL, TLSDS, ARRLS, wAR, wARSDS) as the column effects, with subjects as the row effects. Each combination of algorithm and subject had 30 values corresponding to 30 runs performed. Friedman’s test showed statistically signiﬁcant differences among the six algorithms for each headset (df = 5, p = 0.00).

Then, non-parametric multiple comparison tests using Dunn’s procedure [13], [14] was used to determine if the difference between any pair of algorithms was statistically signiﬁcant, with a p-value correction using the false discovery rate method [4]. The results showed that the performances of wAR and wARSDS were statistically signiﬁcantly different from BL2, TL, TLSDS and ARRLS for each headset (p = 0.0000 for all cases, except p = 0.0031 for ABM wAR vs BL2, and p = 0.0004 for ABM wARSDS vs BL2). There was no statistically signiﬁcant performance difference between wAR and wARSDS (p = 0.2602 for BioSemi, p = 0.2734 for ABM, and p = 0.4365 for Emotiv).

In summary, we have demonstrated that given the same number of labeled subject-speciﬁc training samples, wAR and wARSDS can signiﬁcantly improve the ofﬂine calibration performance. In other words, given a desired classiﬁcation accuracy, wAR and wARSDS can signiﬁcantly reduce the number of labeled subject-speciﬁc training samples. For example, in Fig. 3(a), the average BCA of BL2 is 71.14%, given 100 labeled subject-speciﬁc training samples. However, to achieve that BCA, on average wAR and wARSDS only need 5 samples, corresponding to 95% saving of the labeling effort. Moreover, Fig. 3(a) also shows that, without using any labeled subject-speciﬁc samples, wAR and wARSDS can achieve similar performance as BL2 which uses 65 samples. Similar observations can also be made for the ABM and Emotiv headsets.

As in [51], [53], we also performed comprehensive statistical tests to check if the performance differences among the six algorithms (BL1 was not included because it is not iterative) were statistically signiﬁcant. We used the area-underperformance-curve (AUPC) [31], [51], [53] to assess overall performance differences among these algorithms. The AUPC is the area under the curve of the BCAs obtained at each of the 30 runs, and is normalized to [0,1]. A larger AUPC value indicates a better overall classiﬁcation performance.

First, we checked the normality of our data to see if parametric ANOVA tests can be used. The histograms of the 30 × 14 = 420 AUPCs for each of the six algorithms on the three headsets are shown in Fig. 4. Observe that most of them are not even close to normal. So, parametric ANOVA tests cannot be applied.

D. Parameter Sensitivity Analysis

As a result, we used Friedman’s test [15], a two-way non-parametric ANOVA where column effects are tested for signiﬁcant differences after adjusting for possible row effects.

In this subsection we study the sensitivity of wAR and wARSDS to parameters σ and λP (λQ). To save space, we only show the BCA results for the BioSemi headset. Similar results were obtained from the other two headsets.

5Note that this does not conﬂict with the observation in [48], which said TL was better than BL2. This is because different datasets were used in the two studies: [48] downsampled the non-target class to balance the two classes before testing the performances of different algorithms, whereas classimbalance was preserved in this paper. Moreover, [48] only considered the BioSemi headset, and showed that TL outperformed BL2, but the performance difference between TL and BL2 decreased as ml increases. This is also the case in Fig. 3(a), when ml is small.

The average BCAs of wAR and wARSDS for different σ (λP and λQ were ﬁxed at 10) are shown in Fig. 5(a), and for different λP and6 λQ (σ was ﬁxed at 0.1) are shown

6We always assigned λP and λQ identical value because they are conceptually close.

in Fig. 5(b). Observe from Fig. 5(a) that both wAR and wARSDS achieved good BCAs for σ ∈ [0.0001,1], and from

- Fig. 5(b) that both wAR and wARSDS achieved good BCAs for λP ∈ [10,100] and λQ ∈ [10,100]. Moreover, σ, λP and λQ have more impact to the BCA when ml is small. As ml increases, the impact diminishes. This is intuitive, as the need for transfer diminishes as the amount of labeled target domain data increases.

##### wAR

##### wARSDS

0.85

0.85

0.8

0.8

BCA

BCA

0.75

0.75

0.7

0.7

0.65 100

0.65 100

80

80

102

102

60

60

100

100

40

40

20 10-2 0 10-4

20 10-2 0 10-4

ml

ml

σ

σ

### (a)

##### wAR

##### wARSDS

0.85

0.85

###### BCA

###### BCA

0.8

0.8

0.75

0.75

0.7 100

100

80

80

102

102

60

60

100

100

40

40

20 10-2 0 10-4

20 10-2 10-4

ml

ml

λP (λQ)

λP (λQ)

(b)

- Fig. 5. Average BCAs of wAR and wARSDS for different parameters for the BioSemi headset. (a) σ; and, (b) λP and λQ.

VI. PERFORMANCE EVALUATION OF ONLINE CALIBRATION ALGORITHMS

This selection compares the performance of OwARSDS with several other online calibration algorithms.

A. Online Calibration Scenario

Although we knew the labels of all EEG epochs for all 14 subjects in the experiment, we simulated a realistic online calibration scenario: we had labeled EEG epochs from 13 subjects, but initially no epoch from the 14th subject; we generated labeled epochs from the 14th subject iteratively and sequentially on-the-ﬂy, which were used to train a classiﬁer to label the remaining epochs from that subject.

The ﬂowchart for the simulated online calibration scenario is shown in Fig. 2(b). Compared with the ofﬂine calibration scenario in Fig. 2(a), the main difference is that ofﬂine calibration has access to all m unlabeled samples from the 14th subject, but online calibration does not.

More speciﬁcally, assume the 14th subject has m sequential epochs in the VEP experiment, and we want to label p epochs in each iteration, starting from zero. We ﬁrst generate a random number m0 ∈ [1,m], representing the starting position in the VEP sequence. Then, in the ﬁrst iteration, we use all labeled epochs from the other 13 subjects to build different classiﬁers, and compute their BCAs on the m unlabeled epochs. In the second iteration, we generated labeled Epochs m0, m0+1, ..., m0 + p − 1 from the 14th subject, build different classiﬁers,

and compute their BCAs on the remaining m − p unlabeled epochs. We iterate until the maximum number of iterations is reached. To obtain statistically meaningful results, the above process was repeated 30 times for each subject, each time with a random starting point m0. The whole process was repeated 14 times so that each subject had a chance to be the “14th” subject.

- B. Online Calibration Algorithms

We compared the performances of OwARSDS with ﬁve other algorithms:

- 1) BL1 in Section V-B.
- 2) BL2 in Section V-B, using different PCA features.
- 3) TL in Section V-B, using different PCA features.
- 4) TLSDS, which is the above TL algorithm with SDS.
- 5) OwAR, which uses all existing subjects, instead of performing SDS.

Again, weighted libSVM [8] with RBF kernel was used as the classiﬁer in BL1, BL2, TL and TLSDS. We chose wt = 2, σ = 0.1, and λ = 10.

Note that the online algorithms still used PCA features, but they were computed differently from those in ofﬂine calibration. In ofﬂine calibration we had access to the ml labeled samples plus the mu unlabeled samples, so the PCA bases can be pre-computed from all ml+mu samples and kept ﬁxed in each iteration. However, in online calibration, we only had access to the ml labeled samples, so the PCA bases were computed from the ml samples only, and we updated them in each iteration as ml changed.

- C. Experimental Results

The BCAs of the six algorithms, averaged over the 30 runs and across the 14 subjects, are shown in Fig. 6 for different EEG headsets. The observations made in Section V-C for ofﬂine calibration still hold here, except that ARRLS was not included in online calibration. Particularly, both OwAR and OwARSDS achieved much better performance than BL2, TL and TLSDS. However, instead of using 13 auxiliary subjects in OwAR, OwARSDS only used on average 6.51 subjects for BioSemi, 6.01 subjects for ABM, and 7.09 subjects for Emotiv, corresponding to 49.92%, 53.77% and 45.46% computational cost saving, respectively.

Friedman’s test showed statistically signiﬁcant performance differences among the ﬁve algorithms (excluding BL1, which is not iterative) for each headset (df = 4, p = 0.00). Dunn’s procedure showed that the BCAs of OwAR and OwARSDS are statistically signiﬁcantly different from BL2, TL, and TLSDS for each headset (p = 0.0002 for ABM OwARSDS vs BL2, p = 0.0001 for ABM OwARSDS vs TLSDS, and p = 0.0000 in all other cases). There was no statistically signiﬁcant performance difference between OwAR and OwARSDS (p = 0.0682 for BioSemi, p = 0.1929 for ABM, and p = 0.3554 for Emotiv).

In summary, we have demonstrated that given the same number of labeled subject-speciﬁc training samples, OwAR and OwARSDS can signiﬁcantly improve the online calibration performance. In other words, given a desired classiﬁcation

and it was wired, which means better signal quality. The ABM headset had the least number of channels, and was wireless. Moreover, epochs with incorrect button presses were ﬁltered out for BioSemi and Emotiv headsets, but not for most subjects for the ABM headset. So, the epochs in ABM were noisier.

0.9

0.9

0.8

0.8

BCA

BCA

0.7

0.7

0.6

0.6

0.5

0.5

We also performed statistical tests to check if the performance differences among the four algorithms were statistically signiﬁcant. Friedman’s test showed statistically signiﬁcant differences among the four algorithms for BioSemi (df = 3, p = 0.00) and Emotiv (df = 3, p = 0.04), but not ABM (df = 3, p = 0.38). Dunn’s procedure showed that for BioSemi the BCAs of wAR and OwAR were statistically signiﬁcantly different (p = 0.0043), so were BCAs of wARSDS and OwARSDS (p = 0.0000). For ABM and Emotiv the performance differences between online and ofﬂine algorithms were not statistically signiﬁcant (p = 0.5043 for ABM wAR vs OwAR, p = 0.1959 for ABM wARSDS vs OwARSDS, p = 0.0838 for Emotiv wAR vs OwAR, and p = 0.0514 for Emotiv wARSDS vs OwARSDS).

0 20 40 60 80 100

0 20 40 60 80 100

ml

ml

(a)

(b)

|BL1 BL2 TL<br><br>TLSDS<br><br>OwAR<br><br>OwARSDS|
|---|

0.9

0.8

BCA

0.7

0.6

0.5

0 20 40 60 80 100

ml

(c)

- Fig. 6. Average BCAs of the six online algorithms across the 14 subjects, using different EEG headsets. (a) BioSemi; (b) ABM; (c) Emotiv.

In conclusion, we have shown that generally the ofﬂine wAR and wARSDS algorithms, which include a semisupervised learning component, can achieve better calibration performance than the corresponding online OwAR and OwARSDS algorithms, i.e., semi-supervised learning is effective.

accuracy, OwAR and OwARSDS can signiﬁcantly reduce the number of labeled subject-speciﬁc samples. For example, in

- Fig. 6(a), the average BCA of BL2 was 72.34%, given 100 labeled subject-speciﬁc training samples. However, to achieve that BCA, on average OwAR only needed 15 samples, and OwARSDS only needed 20 samples, corresponding to 85% and 80% saving of labeling effort, respectively. Moreover, Fig. 6(a) also shows that, without using any labeled subjectspeciﬁc samples, OwAR and OwARSDS can achieve similar BCA as BL2 which used 60 labeled subject-speciﬁc samples. Similar observations can also be made for the ABM and Emotiv headsets.

| |
|---|

| |
|---|

0.8

0.8

## BCA

## BCA

0.7

0.7

0.6

0.6

0 20 40 60 80 100

0 20 40 60 80 100

ml

ml

VII. COMPARISON OF OFFLINE AND ONLINE ALGORITHMS

(a)

### (b)

|OwAR<br><br>wAR<br><br>OwARSDS<br><br>wARSDS|
|---|

| |
|---|

0.8

This section compares the performances of wARSDS and OwARSDS (wAR and OwAR). Intuitively, we expect the performances of the ofﬂine calibration algorithms to be better than their online counterparts, because: 1) ofﬂine calibration uses all ml + mu EEG epochs to compute the PCA bases, whereas online calibration only uses ml epochs, so the PCA bases in ofﬂine calibration should be more representative; and, 2) ofﬂine calibration also uses the mu unlabeled epochs in the optimization, whereas online calibration does not, so ofﬂine calibration makes use of more information. In other words, ofﬂine calibration makes use of semi-supervised learning whereas online calibration does not.

BCA

0.7

0.6

0 20 40 60 80 100

ml

(c)

Fig. 7. Average BCAs of wAR, wARSDS, OwAR and OwARSDS across the 14 subjects, using different EEG headsets. (a) BioSemi; (b) ABM; (c) Emotiv.

The average performances of wAR, wARSDS, OwAR and OwARSDS across the 14 subjects are shown in Fig. 7. Observe that the results were consistent with our expectation: for all three headsets, the ofﬂine algorithms (wAR and wARSDS) achieved better BCAs than their online counterparts (OwAR and OwARSDS). Additionally, Fig. 7 shows that the algorithms had best performance using the BioSemi headset, and worst performance using the ABM headset. This is not surprising, as BioSemi used the most number of channels,

VIII. CONCLUSIONS

Single-trial classiﬁcation of ERPs in EEG signals is used in many BCI applications. However, because different subjects have different neural responses to even the same stimulus, it is very difﬁcult to build a generic ERP classiﬁer whose parameters ﬁt all subjects. So, the classiﬁer needs to be calibrated for each individual subject, using some labeled subjectspeciﬁc data. Reducing this calibration effort, i.e., minimizing

the number of labeled subject-speciﬁc data required in the calibration, would greatly increase the utility of a BCI system. This paper introduced both online and ofﬂine wAR algorithms for this purpose. We have demonstrated using a VEP oddball task and three different EEG headsets that both algorithms can cope well with the class-imbalance problem, which is intrinsic in many real-world BCI applications, and they also signiﬁcantly outperformed several other algorithms. We also compared the performances of the online and ofﬂine wAR algorithms in identical experimental settings and showed that the ofﬂine wAR algorithm, which includes an extra semisupervised component than the online wAR algorithm, can achieve better calibration performance, i.e., semi-supervised learning is effective in BCI calibration. Moreover, we further proposed a source domain selection approach, which can reduce the computational cost of both online and ofﬂine wAR algorithms by about 50%.

We expect our algorithms to ﬁnd broad applications in various BCI calibration scenarios, and beyond. The most intuitive BCI calibration scenario, as described in this paper, is to reduce the subject-speciﬁc calibration data requirement by making use of relevant data from other subjects. Another scenario is to make use of the same subject’s data from previous usages to facilitate a new calibration. For example, the subject may need to work on the same BCI task at different locations using different EEG headsets (ofﬁce, home, etc.), or may upgrade a BCI game with a new EEG headset. In such applications, wAR can be used to make use of the data obtained from a previous EEG headset to facilitate the calibration for the new headset, as introduced in [51]. Of course, the above two scenarios can also be combined: auxiliary data from other subjects and from the subject himself/herself can be integrated to expedite the calibration. Furthermore, because of human-machine mutual adaptation and non-stationarity, a well-calibrated BCI system may degrade gradually. The proposed wAR algorithms can be used to re-calibrate it from time to time. Additionally, EEGs, together with many other body signals (facial expressions, speech, gesture, galvanic skin response, etc.), are also frequently used in affective computing [34], “computing that relates to, arises from, or deliberately inﬂuences emotion or other affective phenomena.” The wAR algorithms can also be used to handle individual differences and non-stationarity in such applications.

Finally, we need to point out that the current wAR algorithms still have some limitations, which will be improved in our future research. First, we will develop incremental updating rules to reduce their computational cost. Second, we will develop criteria to determine when a negative transfer may occur, and hence use subject-only calibration data in such cases. Third, although wAR can map the features to a new kernel space to make them more consistent across the source and target domains, it still relies on good initial features. Simple PCA features were used in this paper. In our future research we will consider more sophisticated and robust features, e.g., the information geometry [2].

ACKNOWLEDGEMENT

The author would like to thank Scott Kerick, Jean Vettel, Anthony Ries, and David W. Hairston at the U.S. Army Research Laboratory (ARL) for designing the experiment and collecting the data, and Brent J. Lance and Vernon J. Lawhern from the ARL for helpful discussions.

Research was sponsored by the U.S. Army Research Laboratory and was accomplished under Cooperative Agreement Numbers W911NF-10-2-0022 and W911NF-10-D-0002/TO 0023. The views and the conclusions contained in this document are those of the authors and should not be interpreted as representing the ofﬁcial policies, either expressed or implied, of the U.S. Army Research Laboratory or the U.S Government.

REFERENCES

- [1] M. Alamgir, M. Grosse-Wentrup, and Y. Altun, “Multitask learning for brain-computer interfaces,” in Proc. 13th Int’l Conf. on Artiﬁcial Intelligence and Statistics (AISTATS), Sardinia, Italy, May 2010, pp. 17–24.
- [2] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Multiclass braincomputer interface classiﬁcation by Riemannian geometry,” IEEE Trans. on Biomedical Engineering, vol. 59, no. 4, pp. 920–928, 2012.
- [3] M. Belkin, P. Niyogi, and V. Sindhwani, “Manifold regularization: A geometric framework for learning from labeled and unlabeled examples,” Journal of Machine Learning Research, vol. 7, pp. 2399–2434, 2006.
- [4] Y. Benjamini and Y. Hochberg, “Controlling the false discovery rate: A practical and powerful approach to multiple testing,” Journal of the Royal Statistical Society, Series B (Methodological), vol. 57, pp. 289– 300, 1995.
- [5] N. Bigdely-Shamlo, A. Vankov, R. Ramirez, and S. Makeig, “Brain activity-based image classiﬁcation from rapid serial visual presentation,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 16, no. 5, pp. 432–441, 2008.
- [6] D. Bottger, C. S. Herrmann, and D. Y. von Cramon, “Amplitude differences of evoked alpha and gamma oscillations in two different age groups,” International Journal of Psychophysiology, vol. 45, pp. 245–251, 2002.
- [7] K. B. Bulayeva, T. A. Pavlova, and G. G. Guseynov, “Visual evoked potentials: Phenotypic and genotypic variability,” Behavior Genetics, vol. 23, no. 5, pp. 443–447, 1993.
- [8] C.-C. Chang and C.-J. Lin, “LIBSVM: A library for support vector machines,” ACM Trans. on Intelligent Systems and Technology, vol. 2, no. 3, pp. 27:1–27:27, 2011, software available at http://www.csie.ntu.edu.tw/$\sim$cjlin/libsvm.
- [9] O. Chapelle, B. Scholkopf, and A. Zien, Semi-supervised learning. Boston, MA: The MIT Press, 2006.
- [10] M. M. Chun and M. C. Potter, “A two-stage model for multiple target detection in rapid serial visual presentation,” Journal of Experimental Psychology: Human Perception and Performance, vol. 21, no. 1, pp. 109–127, 1995.
- [11] S. Crottaz-Herbette and V. Menon, “Where and when the anterior cingulate cortex modulates attentional response: Combined fMRI and ERP evidence,” Journal of Cognitive Neuroscience, vol. 18, no. 5, pp. 766–780, 2006.
- [12] A. Delorme and S. Makeig, “EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis,” Journal of Neuroscience Methods, vol. 134, pp. 9–21, 2004.
- [13] O. Dunn, “Multiple comparisons among means,” Journal of the American Statistical Association, vol. 56, pp. 62–64, 1961.
- [14] O. Dunn, “Multiple comparisons using rank sums,” Technometrics, vol. 6, pp. 214–252, 1964.
- [15] M. Friedman, “A comparison of alternative tests of signiﬁcance for the problem of m rankings,” The Annals of Mathematical Statistics, vol. 11, no. 1, pp. 86–92, 1940.
- [16] M. Grosse-Wentrup, C. Liefhold, K. Gramann, and M. Buss, “Beamforming in noninvasive brain computer interfaces,” IEEE Trans. on Biomedical Engineering, vol. 56, no. 4, pp. 1209–1219, 2009.
- [17] S. A. Huettel and G. McCarthy, “What is odd in the oddball task? Prefrontal cortex is activated by dynamic changes in response strategy,” Neuropsychologia, vol. 42, pp. 379–386, 2004.

- [18] N. Japkowicz and S. Stephen, “The class imbalance problem: A systematic study,” Intelligent Data Analysis, vol. 6, no. 5, pp. 429–449, 2002.
- [19] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, and M. GrosseWentrup, “Transfer learning in brain-computer interfaces,” IEEE Computational Intelligence Magazine, vol. 11, no. 1, pp. 20–31, 2016.
- [20] P.-J. Kindermans, H. Verschore, D. Verstraeten, and B. Schrauwen, “A P300 BCI for the masses: Prior information enables instant unsupervised spelling,” in Proc. Neural Information Processing Systems (NIPS), Lake Tahoe, NV, December 2012.
- [21] M. Kuba, J. Kremlacek, J. Langrova, Z. Kubova, J. Szanyi, and F. Vt, “Aging effect in pattern, motion and cognitive visual evoked potentials,” Vision Research, vol. 62, no. 1, pp. 9–16, 2012.
- [22] V. J. Lawhern, D. J. Slayback, D. Wu, and B. J. Lance, “Efﬁcient labeling of EEG signal artifacts using active learning,” in Proc. IEEE Int’l Conf. on Systems, Man and Cybernetics, Hong Kong, October 2015.
- [23] Y. Li and C. Guan, “Joint feature re-extraction and classiﬁcation using an iterative semi-supervised support vector machine algorithm,” Machine Learning, vol. 71, no. 1, pp. 33–53, 2008.
- [24] R. Lomasky, C. E. Brodley, M. Aernecke, D. Walt, and M. Friedl, “Active class selection,” in Proc. 18th European Conference on Machine Learning, Warsaw, Poland, September 2007, pp. 640–647.
- [25] M. Long, J. Wang, G. Ding, S. J. Pan, and P. S. Yu, “Adaptation regularization: A general framework for transfer learning,” IEEE Trans. on Knowledge and Data Engineering, vol. 26, no. 5, pp. 1076–1089, 2014.
- [26] R. Longadge, S. S. Dongre, and L. Malik, “Class imbalance problem in data mining: Review,” Int’l J. of Computer Science and Network, vol. 2, no. 1, 2013.
- [27] F. Lotte and C. Guan, “Learning from other subjects helps reducing brain-computer interface calibration time,” in Proc. IEEE Int’l. Conf. on Acoustics Speech and Signal Processing (ICASSP), Dallas, TX, March 2010.
- [28] F. Lotte and C. Guan, “Regularizing common spatial patterns to improve BCI designs: Uniﬁed theory and new algorithms,” IEEE Trans. on Biomedical Engineering, vol. 58, no. 2, pp. 355–362, 2011.
- [29] F. Lotte, “Signal processing approaches to minimize or suppress calibration time in oscillatory activity-based brain-computer interfaces,” Proc. of the IEEE, vol. 103, no. 6, pp. 871–890, 2015.
- [30] S. Makeig, C. Kothe, T. Mullen, N. Bigdely-Shamlo, Z. Zhang, and K. Kreutz-Delgado, “Evolving signal processing for brain-computer interfaces,” Proc. of the IEEE, vol. 100, no. 3, pp. 1567–1584, 2012.
- [31] A. Marathe, V. Lawhern, D. Wu, D. Slayback, and B. Lance, “Improved neural signal classiﬁcation in a rapid serial visual presentation task using active learning,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 24, no. 3, pp. 333–343, 2016.
- [32] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans. on Knowledge and Data Engineering, vol. 22, no. 10, pp. 1345–1359, 2010.
- [33] L. Parra, C. Christoforou, A. Gerson, M. Dyrholm, A. Luo, M. Wagner, M. Philiastides, and P. Sajda, “Spatiotemporal linear decoding of brain state,” IEEE Signal Processing Magazine, vol. 25, no. 1, pp. 107–115, 2008.
- [34] R. Picard, Affective Computing. Cambridge, MA: The MIT Press, 1997.
- [35] E. A. Pohlmeyer, J. Wang, D. C. Jangraw, B. Lou, S.-F. Chang, and P. Sajda, “Closing the loop in cortically-coupled computer vision: a brain-computer interface for searching image databases,” Journal of Neural Engineering, vol. 8, no. 3, 2011.
- [36] M. C. Potter, “Short-term conceptual memory for pictures,” Journal of Experimental Psychology: Human Learning and Memory, vol. 2, no. 5, pp. 509–522, 1976.
- [37] F. Provost, “Machine learning from imbalanced data sets 101,” Tech. Rep. AAAI Technical Report WS-00-05, 2000.
- [38] A. J. Ries, J. Touryan, J. Vettel, K. McDowell, and W. D. Hairston, “A comparison of electroencephalography signals acquired from conventional and mobile systems,” Journal of Neuroscience and Neuroengineering, vol. 3, no. 1, pp. 10–20, 2014.
- [39] P. Sajda, E. Pohlmeyer, J. Wang, L. Parra, C. Christoforou, J. Dmochowski, B. Hanna, C. Bahlmann, M. Singh, and S.-F. Chang, “In a blink of an eye and a switch of a transistor: Cortically coupled computer vision,” Proc. of the IEEE, vol. 98, no. 3, pp. 462–478, 2010.
- [40] W. Samek, F. Meinecke, and K.-R. Muller, “Transferring subspaces between subjects in brain-computer interfacing,” IEEE Trans. on Biomedical Engineering, vol. 60, no. 8, pp. 2289–2298, 2013.
- [41] B. Scholkopf and A. J. Smola, Learning with kernels: support vector machines, regularization, optimization, and beyond. Cambridge, MA: MIT Press, 2001.

- [42] B. Settles, “Active learning literature survey,” University of Wisconsin– Madison, Computer Sciences Technical Report 1648, 2009.
- [43] US Department of Defense Ofﬁce of the Secretary of Defense, “Code of federal regulations protection of human subjects,” Government Printing Ofﬁce, no. 32 CFR 19, 1999.
- [44] US Department of the Army, “Use of volunteers as subjects of research,” Government Printing Ofﬁce, no. AR 70-25, 1990.
- [45] V. Vapnik, Statistical Learning Theory. New York, NY: Wiley Press, 1998.
- [46] P. Wang, J. Lu, B. Zhang, and Z. Tang, “A review on transfer learning for brain-computer interface classiﬁcation,” in Prof. 5th Int’l Conf. on Information Science and Technology (IC1ST), Changsha, China, April 2015.
- [47] D. Wu, C.-H. Chuang, and C.-T. Lin, “Online driver’s drowsiness estimation using domain adaptation with model fusion,” in Proc. Int’l Conf. on Affective Computing and Intelligent Interaction, Xi’an, China, September 2015.
- [48] D. Wu, B. J. Lance, and V. J. Lawhern, “Active transfer learning for reducing calibration data in single-trial classiﬁcation of visually-evoked potentials,” in Proc. IEEE Int’l Conf. on Systems, Man, and Cybernetics, San Diego, CA, October 2014.
- [49] D. Wu, B. J. Lance, and T. D. Parsons, “Collaborative ﬁltering for braincomputer interaction using transfer learning and active class selection,” PLoS ONE, 2013.
- [50] D. Wu, V. J. Lawhern, S. Gordon, B. J. Lance, and C.-T. Lin, “Ofﬂine EEG-based driver drowsiness estimation using enhanced batch-mode active learning (EBMAL) for regression,” in Proc. IEEE Int’l Conf. on Systems, Man and Cybernetics, Budapest, Hungary, October 2016.
- [51] D. Wu, V. J. Lawhern, W. D. Hairston, and B. J. Lance, “Switching EEG headsets made easy: Reducing ofﬂine calibration effort using active weighted adaptation regularization,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, 2016, in press.
- [52] D. Wu, V. J. Lawhern, and B. J. Lance, “Reducing BCI calibration effort in RSVP tasks using online weighted adaptation regularization with source domain selection,” in Proc. Int’l Conf. on Affective Computing and Intelligent Interaction, Xi’an, China, September 2015.
- [53] D. Wu, V. J. Lawhern, and B. J. Lance, “Reducing ofﬂine BCI calibration effort using weighted adaptation regularization with source domain selection,” in Proc. IEEE Int’l Conf. on Systems, Man and Cybernetics, Hong Kong, October 2015.
- [54] T. O. Zander and C. Kothe, “Towards passive brain-computer interfaces: applying brain-computer interface technology to human-machine systems in general,” Journal of Neural Engineering, vol. 8, no. 2, 2011.

