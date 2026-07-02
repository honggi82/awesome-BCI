arXiv:2007.03746v3[eess.SP]22Jan2021

Transfer Learning for Motor Imagery Based Brain-Computer Interfaces: A Complete Pipeline

Dongrui Wua,b, Xue Jianga, Ruimin Penga, Wanzeng Kongb, Jian Huanga,∗, Zhigang Zenga,∗

aKey Laboratory of the Ministry of Education for Image Processing and Intelligent Control, School of Artiﬁcial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China

bZhejiang Key Laboratory for Brain-Machine Collaborative Intelligence, Hangzhou Dianzi University, Hangzhou 310018, China

[Figure 1]

Abstract

Transfer learning (TL) has been widely used in motor imagery (MI) based braincomputer interfaces (BCIs) to reduce the calibration effort for a new subject, and demonstratedpromising performance. While a closed-loopMI-based BCI system, after electroencephalogram (EEG) signal acquisition and temporal ﬁltering, includes spatial ﬁltering, feature engineering, and classiﬁcation blocks before sending out the control signal to an externaldevice, previousapproachesonly considered TL in one or two such components. This paper proposes that TL could be considered in all three components (spatial ﬁltering, feature engineering, and classiﬁcation) of MI-based BCIs. Furthermore, it is also very important to speciﬁcally add a data alignment component before spatial ﬁltering to make the data from different subjects more consistent, and hence to facilitate subsequential TL. Ofﬂine calibration experiments on two MI datasets veriﬁed our proposal. Especially, integrating data alignment and sophisticated TL approaches can signiﬁcantly improve the classiﬁcation performance, and hence greatly reduces the calibration effort.

Keywords: Brain-computer interface, EEG, transfer learning, Euclidean alignment, motor imagery

[Figure 2]

- 1. Introduction

A brain-computer interface (BCI) [16, 43] enables a user to communicate directly with an external device, e.g., a computer, using his/her brain signals, e.g., electroencephalogram (EEG). It can beneﬁt both patients [31] and able-bodied people [41, 27].

[Figure 3]

∗Corresponding authors

Email addresses: drwu@hust.edu.cn (Dongrui Wu), xuejiang@hust.edu.cn (Xue Jiang), rmpeng2019@hust.edu.cn (Ruimin Peng), kongwanzeng@hdu.edu.cn (Wanzeng Kong), huang_jan@hust.edu.cn (Jian Huang), zgzeng@hust.edu.cn (Zhigang Zeng)

Preprint submitted to Information Sciences November 15, 2022

Motor imagery (MI) [32] is a common paradigm in EEG-based BCIs, and also the focus of this paper. In MI-based BCIs, the user imagines the movements of his/her body parts, which activates different areas of the motor cortex of the brain, e.g., top-left for right-hand MI, top-right for left-hand MI, and top-central for feet MI. A classiﬁcation algorithm can then be used to decode the recorded EEG signals and map the corresponding MI to a command for the external device.

The ﬂowchart of a closed-loop EEG-based BCI system is shown in Figure 1. It consists of the following main components [50]:

[Figure 4]

Figure 1: A closed-loop EEG-based BCI system, using MI as an example.

- 1. Signal acquisition, which uses a headset to collect EEG signal from the scalp, while the user is performing MI tasks.
- 2. Signal processing [22]. Because EEG signals are weak, and easily contaminated by artifacts and interferences, e.g., muscle movements, eye blinks, heartbeats, powerline noise, etc., sophisticated signal processing approaches must be used to increase the signal-to-noise ratio. Both temporal ﬁltering and spatial ﬁltering are usually performed. Temporal ﬁltering may include notch ﬁltering to remove the 50Hz or 60Hz powerline interference, and then bandpassﬁltering, e.g., [8,30] Hz, to remove DC drift and high frequency noise. Spatial ﬁlters [45] include the basic ones, e.g., common average reference [40], Laplacian ﬁlters [15], principal component analysis [12], etc., and more sophisticated ones, e.g., independent component analysis [7], xDAWN [35], canonical correlation analysis [37], common spatial patterns (CSP) [33], etc.
- 3. Feature engineering, which includes feature extraction, and sometimes also feature selection. Time domain, frequency domain, time-frequency domain, Riemannian space [52], and/or topoplot features [18] could be used.
- 4. Classiﬁcation [23], which uses a machine learning algorithm to decode the EEG signal from the extracted features. Commonly used classiﬁers include linear discriminant analysis (LDA) and support vector machine (SVM).
- 5. Controller, which sends a command to an external device, e.g., a wheelchair, according to the decoded EEG signal.

Because of individualdifferencesand non-stationarity of EEG signals, an MI-based BCI usually needs a long calibration session for a new subject, from 20-30 minutes [38] to hours or even days. This lengthy calibration signiﬁcantly reduces the utility of BCI systems. Hence, many sophisticated signal processing and machine learning approaches have been proposed recently to reduce or eliminate the calibration [6, 9, 10, 11, 36, 42, 44, 50, 53, 54].

One of the most promising such approaches is transfer learning (TL) [28], which uses data/knowledge from source domains (existing subjects) to help the calibration in the target domain (new subject). However, previous TL approaches for BCIs usually considered only one or two components of the closed-loop system in Figure 1, particularly, classiﬁcation, as introduced in our latest survey [50]. For example, Jayaram et al. [11] proposed a multi-task learning (which is a subﬁeld of TL) framework for cross-subject MI classiﬁcation. To consider TL in spatial ﬁltering, Dai et al. [6] proposed transfer kernel CSP to integrate kernel CSP [1] and transfer kernel learning [21] for EEG trial ﬁltering. To consider TL in feature engineering, Chen et al. [4] extended ReliefF [13] and minimum redundancy maximum relevancy (mRMR) [29] feature selection approachesto Class-Separate and Domain-Fused (CSDF)-ReliefF and CSDF-mRMR, which optimized both the class separability and the domain similarity simultaneously. They then further integrated CSDF-ReliefF and CSDF-mRMR with an adaptation regularization-based TL classiﬁer [20].

In this paper, we claim that TL should be considered in as many components of a BCI system as possible, and propose a complete TL pipeline for MI-based BCIs, shown in Figure 2:

[Figure 5]

Figure 2: A complete TL pipeline for closed-loop MI-based BCI systems.

- 1. Temporal ﬁltering, where band-pass ﬁltering is performed on both the source and target domain data.
- 2. Data alignment, which aligns EEG trials from the source domains and the target domain so that their distributions are more consistent. This is a new component, which does not exist in Figure 1, but will greatly facilitate TL in sequential components, as shown later in this paper.
- 3. Spatial ﬁltering, where TL can be used to design better spatial ﬁlters, especially when the amount of target domain labeled data is small.
- 4. Feature engineering, where TL may be used to extract or select more informative features.
- 5. Classiﬁcation, where TL can be used to design better classiﬁers or regression models, especially when there are no or very few target domain labeled data.

We will introduce some representative TL approaches in data alignment, spatial ﬁltering, feature selection and classiﬁcation, and demonstrate using two MI datasets that incorporate TL in all these components can indeed achieve better classiﬁcation performance than not using TL, or using TL in only a subset of these components.

Our main contributions are:

- 1. We propose a complete TL pipeline for closed-loop MI-based BCI systems, as shown in Figure 2, and point out that explicitly including a data alignment component before spatial ﬁltering is very important to the TL performance, for both traditional machine learning and deep learning, both ofﬂine and online classiﬁcation, and both cross-subject and cross-session classiﬁcation.
- 2. We verify through experiments that usually considering TL in more components in Figure 2 can result in better classiﬁcation performance, and more sophisticated TL approaches are usually more beneﬁcial than simple TL approaches, or not using TL at all.

The remainder of this paper is organized as follows: Section 2 introduces some representative TL approaches at different components of a BCI system. Section 3 evaluates the performance of the complete TL pipeline in ofﬂine cross-subject MI classiﬁcation. Section 4 discusses the TL pipeline in ofﬂine cross-subject classiﬁcation using deep learning, online cross-subject classiﬁcation, and ofﬂine cross-session classiﬁcation. Finally, Section 5 draws conclusions and points out some future research directions.

- 2. TL Approaches

This section introduces the basic concepts of TL, and how TL could be used in data alignment, spatial ﬁltering, feature selection and classiﬁcation of an MI-based BCI system.

We consider ofﬂine binary classiﬁcation only, and would like to use labeled EEG trials from a source subject to help classify trials from a target subject. When there are multiple source subjects, we can combine data from all source subjects and then view that as a single source subject, or perform TL for each source subject separately and then aggregate them.

Assume the source subject has Ns labeled samples {Xsn,ysn}N

n=1, where Xsn ∈ Rc×t is the n-th EEG trial and ysn the corresponding class label, in which c is the number of EEG channels, and t the number of time domain samples. The target subject has Nl labeled samples {Xtn,ytn}N

s

n=1, and Nu unlabeled samples {Xtn}N

l+Nu

l

n=Nl+1. In ofﬂine calibration, the Nu unlabeled samples are also known to us, and we need to design a classiﬁer to obtain their labels.

- 2.1. TL

TL [28] uses data/knowledge from a source domain to help solve a task in a target domain. A domain consists of a feature space X and its associated marginal probability distribution P(X), i.e., {X,P(X)}, where X ∈ X. Two domains are different if they have different feature spaces, and/or different P(X). A task consists of a label space Y

and a prediction function f(X), i.e., {Y,f(X)}. Two tasks are different if they have different label spaces, and/or different conditional probability distributions P(y|X).

For BCI calibration, TL usually means to use labeled EEG trials from an existing subject to help the calibration for a new subject. This paper considers the scenario that both subjects have the same feature space and label space, i.e., the subjects wear the same EEG headset and perform the same types of MIs, but different P(X) and P(y|X). This is the most commonly encountered TL scenario in BCI calibration.

A very simple idea of TL in classiﬁer training is illustrated in Figure 3. Assume the target domain has only four training samples belonging to two classes (represented by different shapes), whereas the source domain has more. Without TL, we can build a classiﬁer in the target domain using only its own four training samples. Since the number of training samples is very small, this classiﬁer is usually unreliable. With TL, we can combine samples from the source domain with those in the target domain to train a classiﬁer. Since the two domains may not be completely consistent, e.g., the marginal probability distributions may be different, we may assign the source domain samples smaller weights than the target domain samples. If optimized properly, the resulting classiﬁer can usually achieve better generalization performance.

[Figure 6]

Figure 3: Illustration of simple TL in classiﬁcation.

Figure 3 illustrates maybe the simplest TL approach in classiﬁcation. Similar approaches may also be used in spatial ﬁltering and feature engineering components in Figure 2. We will introduce some of them next.

- 2.2. Euclidean Alignment (EA) Due to individual differences, the marginal probability distributions of the EEG

trials from different subjects are usually (signiﬁcantly) different; so, it is very beneﬁcial to perform data alignment to make different domains more consistent, before other operations in Figure 2.

Different EEG trial alignment approaches have been proposed recently [9, 10, 36, 53, 54]. A summary and comparison of them is given in [50]. Among them, Euclidean alignment (EA), proposed by He and Wu [10] and illustrated in Figure 4, is easy to perform and completely unsupervised (does not need any labeled data from any subject). So, it is used as an example in this paper.

For the source subject, EA ﬁrst computes

Ns

1 Ns

R¯s =

Xsn (Xsn)⊤ , (1)

[Figure 7]

n=1

[Figure 8]

Figure 4: EA for aligning EEG trials from different subjects (domains).

i.e., the Euclidean arithmetic mean of all spatial covariance matrices from the source subject, then performs the alignment by

X˜sn = R¯s−1/2Xsn. (2)

Similarly, for the target subject, EA computes the arithmetic mean of all Nl + Nu spatial covariance matrices and then performs the alignment.

After EA, the aligned EEG trials are whitened [54], and their mean spatial covariance matrix from each subject equals the identity matrix [10]; hence, the distributions of EEG trials from different subjects become more consistent. This will greatly beneﬁt TL in subsequent steps.

- 2.3. Pre-alignment Strategy (PS) Xu et al. [51] proposed an online pre-alignment strategy (PS) to match the dis-

tributions from different domains. When used in ofﬂine classiﬁcation, its formula is essentially identical to (2), except that the Riemannian mean [30] instead of the Euclidian mean is used in computing R¯s.

The Riemannian distance δ(R,Rn) between two symmetric positive-deﬁnite covariance matrices R ∈ Rc×c and Rn ∈ Rc×c is the minimum length of a curve connecting them on the Riemannian manifold, computed as [26]:

δ(R,Rn) = log R−1Rn F =

c

log2 λi

i=1

- 1

[Figure 9]

- 2

, (3)

where the subscript F denotes the Frobenius norm, and λi, i = 1,...,c, are the real eigenvalues of R−1Rn.

The Riemannian mean [30] of N covariance matrices is deﬁned as the matrix minimizing the sum of the squared Riemannian distances, i.e.,

N

R¯ = arg min

R

n=1

δ2(R,Rn). (4)

The Riemannian mean does not have a closed-form solution, but can be computed by an iterative gradient descent algorithm [8].

The characteristics of PS are almost identical to EA, i.e., it is completely unsupervised, and aligns the EEG trials directly, except that its computational cost is higher than EA, as the Riemannian mean does not have a closed-form solution.

- 2.4. CSP

CSP [3, 33] performs supervised spatial ﬁltering for EEG trials, aiming to ﬁnd a set of spatial ﬁlters to maximize the ratio of variance between two classes.

The traditional CSP uses data from the target subject only. For Class k ∈ {−1,1},

CSP tries to ﬁnd a spatial ﬁlter matrix Wk∗ ∈ Rc×f, where f is the number of spatial ﬁlters, to maximize the variance ratio between Class k and Class −k:

Wk∗ = arg max

W∈Rc×f

tr(W⊤C¯tkW) tr(W⊤C¯t−kW)

[Figure 10]

, (5)

where C¯tk ∈ Rc×c is the mean spatial covariance matrix of the Nl labeled EEG trials in Class k, and tr the trace of a matrix. The solution Wk∗ is the concatenation of the f leading eigenvectors of (C¯t−k)−1C¯tk.

Then, CSP concatenates the 2f spatial ﬁlters from both classes to obtain the complete ﬁlter matrix:

W∗ = W−∗1 W1∗ ∈ Rc×2f, (6) and computes the spatially ﬁltered Xtn by:

X˜tn = W∗⊤Xtn ∈ R2f×t. (7) Finally, the log-variances of X˜tn can be extracted as features xnt ∈ R1×2f in later

classiﬁcation:

xnt = log

  

diag X ˜tn X ˜tn

⊤

[Figure 11]

tr X ˜tn X ˜tn

⊤

  , (8)

where diag means the diagonal elements of a matrix, and log is the logarithm operator.

- 2.5. Combined CSP (CCSP)

Because the target subject has very few labeled samples, i.e., Nl is small, W∗ computed above may not be reliable. The source domain samples can be used to improve W∗.

In the combinedCSP (CCSP), we simply concatenate the Ns source domain labeled samples and Nl target domain labeled samples to compute W∗. Note that all samples have the same weight, i.e., source domain and target domain samples are treated equally.

CCSP may be the simplest TL-based CSP approach.

- 2.6. Regularized CSP (RCSP)

Regularized CSP (RCSP) [24] was speciﬁcally proposed to handle the problem that the target domain has very few labeled samples. Though the original paper did not mention TL, it actually used the idea of TL.

RCSP computes the regularized average spatial covariance matrix for Class k as: Cˆk(β,γ) = (1 − γ)Cˆk(β) +

γ c

[Figure 12]

tr(Cˆk(β))I, (9)

where β and γ are two parameters in [0,1], I ∈ Rc×c is an identity matrix, and

Cˆk(β) =

βNlC¯tk + (1 − β)NsC¯sk βNl + (1 − β)Ns

[Figure 13]

. (10)

Cˆk(β,γ) can then be used to replace C¯tk in (5) to compute the CSP ﬁlter matrix.

Note that when β = 1 and γ = 0, RCSP becomes the traditional CSP. When β = 0.5 and γ = 0, RCSP becomes CCSP.

- 2.7. ReliefF

ReliefF [13] is a classical feature selection approach. Next we introduce its basic idea for binary classiﬁcation.

Let xi be the i-th feature, whose importance w(xi) is initialized to 0. ReliefF randomly selects a sample x, and ﬁnds its k (k = 10 in this paper) nearest neighbors H = {hj}kj=1 in the same class, and also k nearest neighbors M = {mj}kj=1 in the other class. It then updates w(xi) by

w(xi) = w(xi) −

1 k

[Figure 14]

k

j=1

diﬀ(xi,x,hj) +

1 k

[Figure 15]

k

j=1

diﬀ(xi,x,mj), (11)

where diﬀ(xi,x,x′) denotes the difference between samples x and x′ in terms of feature xi. (11) is very intuitive: the importance of xi should be decreased with its ability to discriminate samples from the same class [diﬀ(xi,x,h)], and increased with its ability to discriminate samples from different classes [diﬀ(xi,x,m)].

In this paper, ReliefF terminates after 100 iterations, i.e., 100 randomly selected x were used to compute the ﬁnal w(xi). We then rank these w(xi) and select a few features corresponding to the largest w(xi).

- 2.8. Combined ReliefF (CReliefF)

The traditional ReliefF selects x, H and M from only the target domain labeled samples. We propose a very simple TL extension of ReliefF, combined ReliefF (CReliefF), by selecting x, H and M from labeled samples in both domains.

- 2.9. LDA

LDA is a popular linear classiﬁer for binary classiﬁcation. It assumes that the feature covariance matrices (not to be confused with the spatial covariance matrix of an EEG trial) from the two classes have full rank and are both equal to Σt. The classiﬁcation for a new input x is then

sign wx⊤ − θ , (12) where

w = Σ−t 1(x¯t,1 − x¯t,−1), (13) θ =

- 1

[Figure 16]

- 2

w(x¯t,1 + x¯t,−1), (14)

in which x¯t,−1 and x¯t,1 are the mean feature vector of Class −1 and Class 1 computed from the Nl target domain labeled samples, respectively.

- 2.10. Combined LDA (CLDA)

When Nl is small, the above LDA classiﬁer may not be reliable. The combined LDA (CLDA) is a simple TL approach, which concatenates labeled samples from both the source domain and the target domain to train an LDA classiﬁer. All samples from both domains are treated equally.

- 2.11. Weighted Adaptation Regularization (wAR)

Wu [44] proposed weighted adaptation regularization (wAR), a TL approach for ofﬂine cross-subject EEG classiﬁcation. Though the original experiments were conducted for event-related potential classiﬁcation, wAR can also be used for MI classiﬁcation.

wAR learns a classiﬁer f∗ by minimizing the following regularized loss function:

Ns

Nl

wsnℓ(f(xns),ysn) + wt

wtnℓ(f(xnt ),ytn)

f∗ = argmin

f

n=1

n=1

+ λ1 f 2K + λ2Df,K(Ps(xs),Pt(xt))

+ λ3Df,K(Ps(xs|ys),Pt(xt|yt)) (15)

where ℓ is the classiﬁcation loss, wt is the overall weight of samples from the target subject, wsn and wtn are the weights for the n-th sample from the source subject and the target subject, respectively, K is a kernel function, Ps(xs) and Pt(xt) are the marginal probability distribution of features from the source subject and the target subject, respectively, Ps(xs|ys) and Pt(xt|yt) are the conditional probability distribution from the source subject and the target subject, respectively, and λ1, λ2 and λ3 are non-negative regularization parameters.

Brieﬂy speaking, the ﬁve terms in (15) minimize the classiﬁcation loss for the source subject, the classiﬁcation loss for the target subject, the structural risk of the

classiﬁer, the distance between the marginal probability distributions of the two subjects, and the distance between the conditional probability distributions of the two subjects, respectively.

Although it looks complicated, (15) has a closed-form solution when the squared loss ℓ(f(x) − y) = (y − f(x))2 is used [44].

- 2.12. Online wAR (OwAR)

Wu [44] also proposed online wAR (OwAR), a TL approach for online crosssubject EEG classiﬁcation.

OwAR learns a classiﬁer f∗, also by minimizing the regularized loss function in (15). The only difference is that now the kernel matrix K can only be computed from the Ns labeled source domain samples and Nl labeled target domain samples, but not the Nu unlabeled target domain samples, which are unavailable in online classiﬁcation.

- 3. Experiments and Results

This section evaluates the ofﬂine cross-subject classiﬁcation performances of different combinations of TL approaches on two MI datasets.

- 3.1. MI Datasets

Two MI datasets from BCI Competition IV1 were used in this study. They were also used in our previous research [9, 10, 54].

In each experiment, the subject sat in front of a computer and performed visual cue based MI tasks, as shown in Figure 5. A ﬁxation cross on the black screen (t = 0) prompted the subject to be prepared, and marked the start of a trial. After two seconds, a visual cue, which was an arrow pointing to a certain direction, was displayed for four seconds, during which the subject performed the instructed MI task. The visual cue disappeared at t = 6 second, and the MI also stopped. After a two-second break, the next trial started.

[Figure 17]

Figure 5: Timing scheme of the MI tasks.

The ﬁrst dataset2 (Dataset 1 [2]) consisted of seven healthy subjects. Each subject performed two types of MIs, selected from three classes: left-hand, right-hand, and

[Figure 18]

- 1http://www.bbci.de/competition/iv/.
- 2http://www.bbci.de/competition/iv/desc 1.html.

[Figure 19]

foot. We used the 59-channel EEG data collected from the calibration phase, which included complete marker information. Each subject had 100 trials per class.

The second MI dataset3 (Dataset 2a) included nine heathy subjects. Each subject performed four different MIs: left-hand, right-hand, both feet, and tongue. We used the 22-channel EEG data and two classes of MIs (left-hand and right-hand) collected from the training phase. Each subject had 72 trials per class.

EEG data preprocessing steps were identical to those in [10]. A causal [8, 30] Hz band-pass ﬁlter was used to remove muscle artifacts, powerline noise, and DC drift. Next, we extracted EEG signals between [0.5,3.5] seconds after the cue onset as our trials for both datasets.

- 3.2. Algorithms

We mainly compare the following 18 different algorithms, with various different conﬁgurations of TL components:

- 1. CSP-LDA, which uses only the target domain labeled data to design the CSP ﬁlters, and then trains an LDA classiﬁer on the target domain labeled data. No source data is used at all, i.e., no TL is used at all.
- 2. CSP-CLDA, which uses only the target domain labeled data to design the CSP ﬁlters, and then trains a CLDA classiﬁer by using labeled data from both domains, i.e., only the classiﬁer uses a simple TL approach.
- 3. CSP-wAR, which uses only the target domain labeled data to design the CSP ﬁlters, and then trains a wAR classiﬁer by using data from both domains, i.e., only the classiﬁer uses a sophisticated TL approach.
- 4. CCSP-LDA, which concatenates labeled data from both domains to design the CCSP ﬁlters, and then trains an LDA classiﬁer on target domain labeled data only, i.e., only spatial ﬁltering uses a simple TL approach.
- 5. CCSP-CLDA, which concatenates labeled data from both domains to design the CCSP ﬁlters, and then trains a CLDA classiﬁer also from the concatenated data, i.e., both spatial ﬁltering and classiﬁcation use a simple TL approach.
- 6. CCSP-wAR, which concatenates labeled data from both domains to design the CCSP ﬁlters, and then trains a wAR classiﬁer also from the concatenated data, i.e., spatial ﬁltering uses a simple TL approach, whereas classiﬁcation uses a sophisticated TL approach.
- 7. RCSP-LDA, which uses labeled data from both domains to design the RCSP ﬁlters, and then trains an LDA classiﬁer from the target domain labeled data only, i.e., spatial ﬁltering uses a sophisticated TL approach, whereas classiﬁcation does not use TL at all.
- 8. RCSP-CLDA, which uses labeled data from both domains to design the RCSP ﬁlters, and then trains a CLDA classiﬁer also from this concatenated data, i.e., spatial ﬁltering uses a sophisticated TL approach, whereas classiﬁcation uses a simple TL approach.

[Figure 20]

3http://www.bbci.de/competition/iv/desc 2a.pdf.

[Figure 21]

- 9. RCSP-wAR, which uses labeled data from both domains to design the RCSP ﬁlters, and then trains a wAR classiﬁer from this concatenated data, i.e., both spatial ﬁltering and classiﬁcation use a sophisticated TL approach.
- 10. EA-CSP-LDA, which performs EA before CSP-LDA.
- 11. EA-CSP-CLDA, which performs EA before CSP-CLDA, i.e., only the classiﬁer uses a simple TL approach, after EA.
- 12. EA-CSP-wAR, which performsEA before CSP-wAR, i.e., only the classiﬁer uses a sophisticated TL approach, after EA.
- 13. EA-CCSP-LDA, which performs EA before CCSP-LDA, i.e., only spatial ﬁltering uses a simple TL approach, after EA.
- 14. EA-CCSP-CLDA, which performs EA before CCSP-CLDA, i.e., both spatial ﬁltering and classiﬁcation use a simple TL approach, after EA.
- 15. EA-CCSP-wAR, which performs EA before CCSP-wAR, i.e., spatial ﬁltering uses a simple TL approach, whereas classiﬁcation uses a sophisticated TL approach, after EA.
- 16. EA-RCSP-LDA, which performs EA before RCSP-LDA, i.e., only spatial ﬁltering uses a sophisticated TL approach, after EA.
- 17. EA-RCSP-CLDA, which performs EA before RCSP-CLDA, i.e., spatial ﬁltering uses a sophisticated TL approach, whereas classiﬁcation uses a simple TL approach, after EA.
- 18. EA-RCSP-wAR, which performs EA before RCSP-wAR, i.e., both spatial ﬁltering and classiﬁcation use a sophisticated TL approach, after EA.

Additionally, there were nine PS based approaches, which replace EA in the nine EA based approaches by PS, respectively. A summary of the 27 algorithms is shown in Table 1.

Six (a typical number [34]) spatial ﬁlters were used in all CSP algorithms. β = γ = 0.1 were used in RCSP. wt = 10, λ1 = 0.1, λ2 = λ3 = 10 were used in wAR, as in [44, 48], except that wt was increased from 2 to 10 because the combined source domain has much more labeled samples than the target domain. The source code is available at https://github.com/drwuHUST/TLBCI.

By comparing between different pairs of the above algorithms, we can individually study the effect of TL in different components of Figure 2.

- 3.3. Experimental Settings and Results

For each dataset, we sequentially selected one subject as the target subject and all remaining ones as the source subjects, i.e., we performed cross-subject evaluations. As in [10], we combined all source subjects as a single source domain, and performed the corresponding TL. This procedure was repeated for each subject, so that each one became the target subject once.

The number of randomly selected labeled samples in the target domain (Nl) increased from zero to 20, with a step of 4. Because there was randomness involved, we repeated this process 30 times and report the average results.

Note that for algorithms whose spatial ﬁltering component did not involve TL, e.g., those with CSP-, when Nl = 0, no CSP ﬁlters can be trained, and hence no model can

Table 1: Summary of the 27 algorithms with various degrees of TL.

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

Data Spatia Filtering Classiﬁer Algorithm Alignment Simple TL Sophisticated TL Simple TL Sophisticated TL CSP-LDA – – – – –

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

CSP-CLDA – – – – CSP-wAR – – – – CCSP-LDA – – – –

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

CCSP-CLDA – – – CCSP-wAR – – – RCSP-LDA – – – –

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

[Figure 51]

[Figure 52]

[Figure 53]

[Figure 54]

[Figure 55]

RCSP-CLDA – – – RCSP-wAR – – –

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

EA-CSP-LDA – – – – EA-CSP-CLDA – – –

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

EA-CSP-wAR – – – EA-CCSP-LDA – – –

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

EA-CCSP-CLDA – – EA-CCSP-wAR – – EA-RCSP-LDA – – –

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

EA-RCSP-CLDA – – EA-RCSP-wAR – –

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

PS-CSP-LDA – – – – PS-CSP-CLDA – – –

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

PS-CSP-wAR – – – PS-CCSP-LDA – – –

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

PS-CCSP-CLDA – – PS-CCSP-wAR – – PS-RCSP-LDA – – –

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

PS-RCSP-CLDA – PS-RCSP-wAR – –

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

be built. All other algorithms used TL in CSP, and hence the source domain labeled data can be used to train the CSP ﬁlters even when Nl = 0. Similarly, for algorithms whose classiﬁer did not involve TL, e.g., those with -LDA, when Nl = 0, no LDA classiﬁer can be trained.

Note also that since we consider ofﬂine classiﬁcation, all unlabeled samples in the target domain are known, and can be used in EA, PS and wAR. There is no data leakage here.

The cross-subject classiﬁcation accuracies, averaged over 30 random runs, are shown in Figure 6. The average performances over all subjects are shown in the last panel of each subﬁgure. To ensure that the curves are distinguishable, we omitted the curves from the nine PS based algorithms, which were very similar to their EA counterparts.

- 3.4. The General Effect of TL In Figure 6, by comparing CSP-LDA, which did not use TL at all, with the other

17 algorithms, which used simple or sophisticated TL in one or more components of Figure 2, we can see that when Nl was small, TL almost always resulted in better performance, no matter how much TL was used. However, when Nl increased, CSP-LDA gradually outperformed certain simple TL approaches, e.g., CSP-CLDA and CCSPCLDA, whereas sophisticated TL approaches, e.g., EA-RCSP-wAR, almost always outperformed CSP-LDA. These results suggest that sophisticated TL may always be beneﬁcial.

To quantitatively study the general effect of TL, we computed the mean classiﬁcation accuracies of the 27 approaches when Nl increased from 4 to 20 (we did not use Nl = 0 because certain approaches did not work in this case), and compared them with that of CSP-LDA. The results are shown in Table 2. We also performed paired t-tests to verify if the performance improvements over CSP-LDA were statistically signiﬁcant (α = 0.05), and marked the insigniﬁcant ones by an underline. Table 2 conﬁrms again that generally more sophisticated TL approaches achieved larger performance improvements.

- 3.5. The Effect of Data Alignment In Figure 6, comparing algorithms without EA and their counterparts with EA, e.g.,

CSP-CLDA and EA-CSP-CLDA, we can observe that every EA version almost always signiﬁcantly outperformed its non-EA counterpart. Similar observations can also be made for PS. These results suggest that a data alignment approach such as EA or PS should always be included as a TL preprocessing step in a BCI system.

To quantitatively verify the above conclusion, we also show the mean classiﬁcation accuracies of algorithms without and with EA/PS in Table 3. Clearly, EA and PS signiﬁcantly improved the classiﬁcation accuracies when TL is used in at least one component of spatial ﬁltering and classiﬁcation, especially on Dataset 1.

Interestingly, when CSP-LDA was used, i.e., no TL was used at all in spatial ﬁltering and classiﬁcation, EA/PS slightly reduced the classiﬁcation performance. We were not able to ﬁnd an explanation for this; however, when no TL will be performed, there is no point to align EEG trials from different subjects. So, this negative transfer will not happen in practice, and should not be a concern.

- 55

60

65

70

75

Subject 1

0 4 8 12 16 20

50

55

60

65

70

75

Subject 2

0 4 8 12 16 20

50

55

60

65

70

75

Subject 3

0 4 8 12 16 20

50

55

60

65

70

75

80

85

Subject 4

0 4 8 12 16 20

55

60

65

70

75

80

85

90

Subject 5

0 4 8 12 16 20

60

65

70

75

80

Subject 6

0 4 8 12 16 20

55

60

65

70

75

80

85

Subject 7

0 4 8 12 16 20

55

60

65

70

75

80

Average

|CSP-LDA<br><br>CSP-CLDA<br><br>CSP-wAR<br><br>CCSP-LDA<br><br>CCSP-CLDA<br><br>CCSP-wAR RCSP-LDA RCSP-CLDA<br><br>RCSP-wAR<br><br>EA-CSP-LDA<br><br>EA-CSP-CLDA<br><br>EA-CSP-wAR<br><br>EA-CCSP-LDA<br><br>EA-CCSP-CLDA<br><br>EA-CCSP-wAR EA-RCSP-LDA EA-RCSP-CLDA<br><br>EA-RCSP-wAR|
|---|

(a)

0 4 8 12 16 20

60

- 65

70

75

80

85

Subject 1

0 4 8 12 16 20

- 49
- 50
- 51
- 52
- 53
- 54
- 55
- 56
- 57
- 58

Subject 2

0 4 8 12 16 20

70

75

80

85

90

95

Subject 3

0 4 8 12 16 20

55

60

65

70

75

Subject 4

0 4 8 12 16 20

- 47
- 48
- 49
- 50
- 51
- 52
- 53
- 54
- 55

Subject 5

0 4 8 12 16 20

52

54

56

58

60

62

64

66

68

Subject 6

0 4 8 12 16 20

54

56

58

60

62

64

- 66

50

0 4 8 12 16 20

## Subject 7

## Subject 8

## Subject 9

## Average

95

74

68

80

90

72

|CSP-LDA<br><br>CSP-CLDA<br><br>CSP-wAR<br><br>CCSP-LDA<br><br>CCSP-CLDA<br><br>CCSP-wAR RCSP-LDA RCSP-CLDA<br><br>RCSP-wAR<br><br>EA-CSP-LDA<br><br>EA-CSP-CLDA<br><br>EA-CSP-wAR<br><br>EA-CCSP-LDA<br><br>EA-CCSP-CLDA<br><br>EA-CCSP-wAR EA-RCSP-LDA EA-RCSP-CLDA<br><br>EA-RCSP-wAR|
|---|

70

85

75

68

66

80

70

64

75

62

65

60

70

58

0 4 8 12 16 20

0 4 8 12 16 20

0 4 8 12 16 20

(b)

- Figure 6: Ofﬂine cross-subject classiﬁcation accuracies (vertical axis) on the MI datasets, with different Nl (horizontal axis). (a) Dataset 1; (b) Dataset 2a.

- Table 2: Ofﬂine cross-subject classiﬁcation accuracies (mean±std) of different TL approaches, and their improvements over CSP-LDA. Performance improvements not statistically signiﬁcant (α = 0.05) are marked with an underline.

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

Dataset 1 Dataset 2a Accuracy Improvement Accuracy Improvement

[Figure 120]

[Figure 121]

[Figure 122]

Algorithm

[Figure 123]

[Figure 124]

(%) (%) (%) (%) CSP-LDA 59.75±6.74 – 62.54±4.88 – CSP-CLDA 63.27±4.37 5.91 64.59±1.67 3.27

[Figure 125]

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

CSP-wAR 64.88±4.65 8.60 66.43±2.12 6.22 CCSP-LDA 63.54±5.52 6.35 65.91±3.67 5.39

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

CCSP-CLDA 59.45±1.48 -0.49 68.44±0.51 9.43 CCSP-wAR 64.95±2.18 8.72 70.32±1.08 12.44 RCSP-LDA 64.28±5.01 7.59 65.76±3.65 5.15 RCSP-CLDA 67.60±1.29 13.15 70.54±0.63 12.78

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

RCSP-wAR 70.22±1.49 17.54 71.78±0.68 14.77 EA-CSP-LDA 59.57±6.72 -0.29 62.43±4.89 -0.18

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

EA-CSP-CLDA 69.46±4.91 16.27 70.46±1.62 12.66

[Figure 151]

[Figure 152]

EA-CSP-wAR 70.87±5.43 18.61 70.76±1.76 13.14 EA-CCSP-LDA 69.09±6.32 15.64 66.97±4.28 7.08 EA-CCSP-CLDA 79.97±0.17 33.85 73.84±0.10 18.07 EA-CCSP-wAR 80.37±0.30 34.52 74.19±0.50 18.62 EA-RCSP-LDA 68.24±5.31 14.21 68.64±3.99 9.75 EA-RCSP-CLDA 79.51±0.08 33.08 74.76±0.55 19.54

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

EA-RCSP-wAR 80.45±0.35 34.66 75.10±0.54 20.08 PS-CSP-LDA 59.58±6.73 -0.28 62.47±4.90 -0.12 PS-CSP-CLDA 71.51±5.26 19.69 70.49±1.59 12.71

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

PS-CSP-wAR 71.89±5.17 20.33 70.85±1.70 13.29 PS-CCSP-LDA 67.59±5.72 13.13 66.48±4.17 6.29 PS-CCSP-CLDA 78.35±0.18 31.14 73.87±0.14 18.11 PS-CCSP-wAR 79.15±0.14 32.48 74.67±0.47 19.39 PS-RCSP-LDA 68.92±5.25 15.36 68.02±3.89 8.77 PS-RCSP-CLDA 79.15±0.13 32.48 74.22±0.66 18.68

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

PS-RCSP-wAR 79.56±0.17 33.17 74.68±0.70 19.40

[Figure 185]

- Table 3: Ofﬂine cross-subject classiﬁcation accuracies (mean±std) of algorithms without and with EA/PS, and the improvements of the latter over the former. Performance improvements not statistically signiﬁcant (α = 0.05) are marked with an underline.

[Figure 186]

[Figure 187]

[Figure 188]

[Figure 189]

w/o EA w/ EA Imp. w/o PS w/ PS Imp. Dataset Algorithm (%) (%) (%) (%) (%) (%)

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

- 1

[Figure 194]

CSP-LDA 59.75±6.74 59.57±6.72 -0.29 59.75±6.74 59.58±6.73 -0.28 CSP-CLDA 63.27±4.37 69.46±4.91 9.79 63.27±4.37 71.51±5.26 13.02

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

[Figure 200]

CSP-wAR 64.88±4.65 70.87±5.43 9.22 64.88±4.65 71.89±5.17 10.80 CCSP-LDA 63.54±5.52 69.09±6.32 8.74 63.54±5.52 67.59±5.72 6.37 CCSP-CLDA 59.45±1.48 79.97±0.17 34.51 59.45±1.48 78.35±0.18 31.78 CCSP-wAR 64.95±2.18 80.37±0.30 23.74 64.95±2.18 79.15±0.14 21.86 RCSP-LDA 64.28±5.01 68.24±5.31 6.16 64.28±5.01 68.92±5.25 7.22 RCSP-CLDA 67.60±1.29 79.51±0.08 17.61 67.60±1.29 79.15±0.13 17.08

[Figure 201]

[Figure 202]

[Figure 203]

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

[Figure 212]

[Figure 213]

[Figure 214]

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

- RCSP-wAR 70.22±1.49 80.45±0.35 14.56 70.22±1.49 79.56±0.17 13.29

[Figure 219]

[Figure 220]

[Figure 221]

2a

[Figure 222]

CSP-LDA 62.54±4.88 62.43±4.89 -0.18 62.54±4.88 62.47±4.90 -0.12 CSP-CLDA 64.59±1.67 70.46±1.62 9.09 64.59±1.67 70.49±1.59 9.14

[Figure 223]

[Figure 224]

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

CSP-wAR 66.43±2.12 70.76±1.76 6.52 66.43±2.12 70.85±1.70 6.66 CCSP-LDA 65.91±3.67 66.97±4.28 1.60 65.91±3.67 66.48±4.17 0.86

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

CCSP-CLDA 68.44±0.51 73.84±0.10 7.89 68.44±0.51 73.87±0.14 7.93 CCSP-wAR 70.32±1.08 74.19±0.50 5.49 70.32±1.08 74.67±0.47 6.18 RCSP-LDA 65.76±3.65 68.64±3.99 4.38 65.76±3.65 68.02±3.89 3.44

[Figure 238]

[Figure 239]

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

RCSP-CLDA 70.54±0.63 74.76±0.55 5.99 70.54±0.63 74.22±0.66 5.22

[Figure 247]

[Figure 248]

[Figure 249]

- RCSP-wAR 71.78±0.68 75.10±0.54 4.62 71.78±0.68 74.68±0.70 4.03

[Figure 250]

[Figure 251]

[Figure 252]

- 3.6. The Effect of TL in Spatial Filtering

In Figure 6, comparing algorithms without TL in spatial ﬁltering (CSP), with simple TL in spatial ﬁltering (CCSP), and with sophisticated TL in spatial ﬁltering (RCSP), e.g., CSP-CLDA, CCSP-CLDA and RCSP-CLDA, we can observe that simple TL in spatial ﬁltering may not always work (e.g., CCSP-CLDA had worse performance than CSP-CLDA on Dataset 1, but better performance on Dataset 2a), but sophisticated TL in spatial ﬁltering was almost always beneﬁcial (e.g., RCSP-CLDA outperformed both CSP-CLDA and CCSP-CLDA on both datasets). So, sophisticated TL approaches, such as RCSP, should be used in spatial ﬁltering in a BCI system.

To quantitatively verify the above conclusion, we also show the mean classiﬁcation accuracies of algorithms without and with TL in spatial ﬁltering in Table 4. Clearly, RCSP (sophisticated TL in spatial ﬁltering) always outperformed the corresponding CSP (no TL in spatial ﬁltering) and CCSP (simple TL in spatial ﬁltering) versions.

- Table 4: The effect of TL in spatial ﬁltering. Performance improvements not statistically signiﬁcant (α = 0.05) are marked with an underline.

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

[Figure 258]

[Figure 259]

No TL Simple TL Sophisticated TL CSP CCSP

[Figure 260]

[Figure 261]

[Figure 262]

[Figure 263]

[Figure 264]

Dataset Algorithm

Imp. (%)

Imp. (%)

RCSP

[Figure 265]

- 1

[Figure 266]

CSP-LDA 59.75±6.74 63.54±5.52 6.35 64.28±5.01 7.59 CSP-CLDA 63.27±4.37 59.45±1.48 -6.04 67.60±1.29 6.84

[Figure 267]

[Figure 268]

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

CSP-wAR 64.88±4.65 64.95±2.18 0.11 70.22±1.49 8.23 EA-CSP-LDA 59.57±6.72 69.09±6.32 15.98 68.24±5.31 14.55

[Figure 275]

[Figure 276]

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

EA-CSP-CLDA 69.46±4.91 79.97±0.17 15.12 79.51±0.08 14.46 EA-CSP-wAR 70.87±5.43 80.37±0.30 13.41 80.45±0.35 13.53 PS-CSP-LDA 59.58±6.73 67.59±5.72 13.44 68.92±5.25 15.68

[Figure 284]

[Figure 285]

[Figure 286]

[Figure 287]

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

[Figure 294]

[Figure 295]

PS-CSP-CLDA 71.51±5.26 78.35±0.18 9.56 79.15±0.13 10.68 PS-CSP-wAR 71.89±5.17 79.15±0.14 10.10 79.56±0.17 10.66

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

[Figure 302]

[Figure 303]

- 2a

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

CSP-LDA 62.54±4.88 65.91±3.67 5.39 65.76±3.65 5.15 CSP-CLDA 64.59±1.67 68.44±0.51 5.96 70.54±0.63 9.21

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

CSP-wAR 66.43±2.12 70.32±1.08 5.86 71.78±0.68 8.06 EA-CSP-LDA 62.43±4.89 66.97±4.28 7.28 68.64±3.99 9.95

[Figure 316]

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

[Figure 322]

[Figure 323]

EA-CSP-CLDA 70.46±1.62 73.84±0.10 4.80 74.76±0.55 6.11 EA-CSP-wAR 70.76±1.76 74.19±0.50 4.84 75.10±0.54 6.13 PS-CSP-LDA 62.47±4.90 66.48±4.17 6.42 68.02±3.89 8.90

[Figure 324]

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

[Figure 333]

[Figure 334]

[Figure 335]

PS-CSP-CLDA 70.49±1.59 73.87±0.14 4.79 74.22±0.66 5.29 PS-CSP-wAR 70.85±1.70 74.67±0.47 5.39 74.68±0.70 5.40

[Figure 336]

[Figure 337]

[Figure 338]

[Figure 339]

[Figure 340]

- 3.7. The Effect of TL in Feature Selection

Assume 2f spatial ﬁlters are needed. Then, as introduced in Section 2.4, in traditional CSP, f of them are the leading eigenvectors of (C¯N)−1C¯P, and the other f are the leading eigenvectors of (C¯P)−1C¯N, where C¯P and C¯N are the mean covariance matrices of the positive and negative classes, respectively. f = 3 is typically used in the literature.

In this subsection, in order to show the effect of TL in feature selection, we use f = 10 to extract 20 CSP ﬁlters, compute the 20 correspondingfeatures in (8), and then use different versions of ReliefF to select the best six among them. More speciﬁcally, without data alignment, we compared the following algorithms:

- 1. CSP6-LDA, which is identical to CSP-LDA in previous subsections. Here we add ‘6’ to emphasize that it uses six CSP ﬁlters, obtained from the leading eigenvectors.
- 2. CSP20-ReliefF6-LDA, which uses the traditional CSP algorithm to extract 20 spatial ﬁlters, compute the 20 corresponding features in (8), and then use ReliefF to select the best six from them. ReliefF uses the target domain labeled data only, i.e., no TL is used.
- 3. CSP20-CReliefF6-LDA, which uses the traditional CSP to extract 20 ﬁlters, compute the 20 correspondingfeatures in (8), and then use CReliefF to select the best six from them. CReliefF uses labeled data from both domains, so there is TL.

LDA above can also be replaced by wAR, and CSP by RCSP. So, there could be 12 different conﬁgurations. Additionally, EA can also be added before each algorithm. So, there are a total of 24 different algorithms.

The cross-subject classiﬁcation results of the 24 algorithms are shown in Table 5. When CReliefF was used to select the best six spatial ﬁlters from the 20 candidates (CSP20→CReliefF6), the resulting classiﬁcation performance was generally better than using ReliefF directly (CSP20→ReliefF6), i.e., TL could be helpful in feature selection. However, using the six leading eigenvectors in CSP (CSP6) generally gave the best performance, justifying the common practice in the literature.

In summary, we have shown that if feature selection must be performed, then using TL may improve the performance; however, when CSP ﬁlters are used, using the leading eigenvectors is good enough, and we can safely omit feature selection.

- 3.8. The Effect of TL in the Classiﬁer

In Figure 6, comparing algorithms with simple and sophisticated TL in the classiﬁer, e.g., CCSP-CLDA and CCSP-wAR, we can observe that sophisticated TL in the classiﬁer almost always outperformed simple TL, regardless of whether TL was used in other components or not. So, sophisticated TL approaches, such as wAR, should be used in the classiﬁer in a BCI system.

To quantitatively verify the above conclusion, we also show the mean classiﬁcation accuracies of algorithms without and with TL in the classiﬁer in Table 6. Clearly, on average wAR (sophisticated TL in the classiﬁer) always outperformed CLDA (simple TL in the classiﬁer).

- Table 5: The effect of TL in feature selection. Performance improvements not statistically signiﬁcant (α = 0.05) are marked with an underline.

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

[Figure 345]

No TL TL CSP6 CSP20→ReliefF6 CSP20→CReliefF6 Imp. (%)

[Figure 346]

[Figure 347]

[Figure 348]

[Figure 349]

[Figure 350]

Dataset Algorithm

[Figure 351]

- 1

[Figure 352]

CSP-LDA 59.91±6.72 58.91±6.47 59.74±6.23 1.40 CSP-wAR 64.21±5.14 61.20±5.54 63.86±5.22 4.36

[Figure 353]

[Figure 354]

[Figure 355]

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

[Figure 360]

RCSP-LDA 64.74±5.36 61.38±5.97 63.89±5.50 4.09 RCSP-wAR 70.85±1.08 64.67±3.55 70.71±0.96 9.35

[Figure 361]

[Figure 362]

[Figure 363]

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

[Figure 368]

EA-CSP-LDA 59.79±6.61 58.02±5.79 60.75±6.69 4.71 EA-CSP-wAR 70.48±5.66 65.68±5.93 71.26±6.35 8.50

[Figure 369]

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

EA-RCSP-LDA 69.52±5.25 63.51±5.89 68.11±6.10 7.24 EA-RCSP-wAR 81.63±0.91 72.78±3.88 81.45±1.01 11.92

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

- 2a

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

CSP-LDA 62.32±5.63 61.86±5.51 62.82±4.98 1.55 CSP-wAR 66.21±2.50 64.72±3.12 65.29±2.49 0.89

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

[Figure 395]

[Figure 396]

RCSP-LDA 65.35±4.11 62.97±5.12 64.78±4.17 2.88 RCSP-wAR 71.58±0.73 68.08±2.40 70.79±0.98 3.98

[Figure 397]

[Figure 398]

[Figure 399]

[Figure 400]

[Figure 401]

[Figure 402]

[Figure 403]

[Figure 404]

EA-CSP-LDA 62.28±5.66 61.24±5.70 61.43±4.60 0.31 EA-CSP-wAR 70.50±2.38 69.11±3.11 68.13±1.67 -1.42

[Figure 405]

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

EA-RCSP-LDA 68.50±4.13 64.19±4.68 62.37±3.94 -2.83 EA-RCSP-wAR 75.00±0.59 72.42±1.63 69.55±0.38 -3.96

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

Interestingly, when EA or PS was used, the performance improvement of wAR over CLDA became smaller, because EA or PS reduced the discrepancy between the source and target domain data, and hence made classiﬁcation easier.

- Table 6: The effect of TL in the classiﬁer. Performance improvements not statistically signiﬁcant (α = 0.05) are marked with an underline.

[Figure 419]

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

[Figure 425]

No TL Simple TL Sophisticated TL LDA CLDA Imp. (%) wAR Imp. (%)

[Figure 426]

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

Dataset Algorithm

[Figure 431]

- 1

[Figure 432]

CSP-LDA 59.75±6.74 63.27±4.37 5.91 64.88±4.65 8.60 CCSP-LDA 63.54±5.52 59.45±1.48 -6.43 64.95±2.18 2.23 RCSP-LDA 64.28±5.01 67.60±1.29 5.17 70.22±1.49 9.25 EA-CSP-LDA 59.57±6.72 69.46±4.91 16.61 70.87±5.43 18.96 EA-CCSP-LDA 69.09±6.32 79.97±0.17 15.74 80.37±0.30 16.33 EA-RCSP-LDA 68.24±5.31 79.51±0.08 16.51 80.45±0.35 17.90

[Figure 433]

[Figure 434]

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

[Figure 440]

[Figure 441]

[Figure 442]

[Figure 443]

[Figure 444]

[Figure 445]

[Figure 446]

[Figure 447]

[Figure 448]

[Figure 449]

[Figure 450]

[Figure 451]

[Figure 452]

[Figure 453]

[Figure 454]

[Figure 455]

[Figure 456]

[Figure 457]

PS-CSP-LDA 59.58±6.73 71.51±5.26 20.02 71.89±5.17 20.67 PS-CCSP-LDA 67.59±5.72 78.35±0.18 15.92 79.15±0.14 17.11 PS-RCSP-LDA 68.92±5.25 79.15±0.13 14.84 79.56±0.17 15.44

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

[Figure 463]

[Figure 464]

[Figure 465]

[Figure 466]

[Figure 467]

[Figure 468]

[Figure 469]

- 2a

[Figure 470]

[Figure 471]

[Figure 472]

[Figure 473]

CSP-LDA 62.54±4.88 64.59±1.67 3.27 66.43±2.12 6.22 CCSP-LDA 65.91±3.67 68.44±0.51 3.83 70.32±1.08 6.69 RCSP-LDA 65.76±3.65 70.54±0.63 7.26 71.78±0.68 9.16 EA-CSP-LDA 62.43±4.89 70.46±1.62 12.86 70.76±1.76 13.35 EA-CCSP-LDA 66.97±4.28 73.84±0.10 10.26 74.19±0.50 10.77 EA-RCSP-LDA 68.64±3.99 74.76±0.55 8.92 75.10±0.54 9.41

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

[Figure 479]

[Figure 480]

[Figure 481]

[Figure 482]

[Figure 483]

[Figure 484]

[Figure 485]

[Figure 486]

[Figure 487]

[Figure 488]

[Figure 489]

[Figure 490]

[Figure 491]

[Figure 492]

[Figure 493]

[Figure 494]

[Figure 495]

[Figure 496]

[Figure 497]

PS-CSP-LDA 62.47±4.90 70.49±1.59 12.85 70.85±1.70 13.42 PS-CCSP-LDA 66.48±4.17 73.87±0.14 11.12 74.67±0.47 12.32 PS-RCSP-LDA 68.02±3.89 74.22±0.66 9.11 74.68±0.70 9.78

[Figure 498]

[Figure 499]

[Figure 500]

[Figure 501]

[Figure 502]

[Figure 503]

[Figure 504]

[Figure 505]

[Figure 506]

- 4. Discussion

The section discusses the TL pipeline in ofﬂine cross-subject MI classiﬁcation using deep learning, online cross-subject classiﬁcation, and ofﬂine cross-session classiﬁcation.

- 4.1. Ofﬂine Cross-Subject Classiﬁcation Using Deep Learning

The previous section veriﬁed the effectiveness of TL in a traditional machine learning pipeline. Deep learning has made signiﬁcant breakthroughs in many ﬁelds, including EEG-based BCIs. This subsection considers the TL pipeline in ofﬂine cross-subject MI classiﬁcation using deep learning models.

Two popular convolutional neural network (CNN) classiﬁers, EEGNet [17] and ShallowCNN [39], were used in our experiments. EEGNet is a compact convolutional network with only about 1,000 parameters (the number may change slightly according to the nature of the task) for EEG-based BCIs. It introduces depthwise and separable convolutions into the construction of EEG-speciﬁc CNNs, which encapsulate well-known EEG feature extraction concepts and simultaneously reduce the number of model parameters. ShallowCNN has a very shallow architecture, consisting of a convolutional block and a classiﬁcation block. The convolutional block is specially designed to handle EEG signals.

Because CNN models perform simultaneously spatial ﬁltering, feature engineering and classiﬁcation, and their computational cost is much higher than traditional machine learning models, we only compared the performanceswith and without EA in Figure 2. More speciﬁcally, we considered ofﬂine unsupervised cross-subject classiﬁcation, i.e., all samples from the target subject were unlabeled (Nl = 0), and all samples from the source subjects were combined and partitioned into 80% training and 20% validation (for early stopping). We used Adam optimizer, cross entropy loss, and batch size 32. The experiments were repeated 15 times for each target subject.

The results are shown in Table 7. Clearly, using EA can improve the classiﬁcation performance of both deep learning models, especially on Dataset 1. These results are consistent with a more comprehensive study in [14], which shows that EA generally beneﬁts deep learning classiﬁcation of movement and motor imagery, P300, and error related negativity.

- Table 7: The effect of EA in deep learning. Performance improvements not statistically signiﬁcant (α = 0.05) are marked with an underline.

[Figure 507]

[Figure 508]

[Figure 509]

Dataset Model w/o EA (%) w/ EA (%) Improvement (%)

[Figure 510]

- 1

[Figure 511]

EEGNet 59.35±4.80 70.00±8.14 17.94 ShallowCNN 62.85±7.47 73.92±8.48 17.61

[Figure 512]

[Figure 513]

[Figure 514]

[Figure 515]

- 2a

[Figure 516]

[Figure 517]

EEGNet 72.71±3.62 75.84±4.61 4.30 ShallowCNN 68.00±3.43 73.46±1.76 3.59

[Figure 518]

[Figure 519]

[Figure 520]

[Figure 521]

- 4.2. Online Cross-Subject Classiﬁcation

All previous results considered ofﬂine cross-subject MI classiﬁcation. It is also interesting to study if the TL pipeline in Figure 2 can be used in online cross-subject MI classiﬁcation.

To this end, we make sure EA and PS use only the available labeled target domain samples in computing the reference matrix and performing data alignment in the target domain. We also replace wAR by OwAR [44], which does not make use of ofﬂine unlabeled samples in the target domain in classiﬁer training.

The online cross-subject classiﬁcation results are shown in Figure 7 and Table 8. Generally, all observations made from ofﬂine cross-subject classiﬁcation in the previous section, e.g., considering TL in more components of Figure 2 beneﬁts the perfor-

mance more, and data alignment is very important to subsequent TL, still hold in online cross-subject classiﬁcation.

Comparing Tables 2 and 8 shows that the ofﬂine classiﬁcation performances were generally slightly better than their online counterparts, which is intuitive, as ofﬂine classiﬁcation makes use of the unlabeled target domain samples, which provides extra information in EA, PS and wAR.

- 4.3. Ofﬂine Cross-Session Classiﬁcation It is well-known that EEG signals are non-stationary [19], i.e., EEG responses to

the same stimulus from the same subject in different sessions are usually varying. This subsection evaluates how the proposed TL pipeline can be used to handle EEG nonstationarity in cross-session classiﬁcation.

In Dataset 2a, each of the nine subjects had two sessions (training and evaluation), collected on different days. For each subject, we used the training session as the source domain, and the evaluation session as the target domain. Other experimental settings were identical to those in previous subsections, except that we used wt = 2 in wAR, as in cross-session TL the number of labeled source domain samples was much smaller than that in cross-subject TL.

The results are shown in Figure 8. Some subjects, e.g., Subjects 1, 3, 7, 8 and 9, demonstrated very stable classiﬁcation performance when Nl increased, indicating that their EEG signals were quite stationary, at least in the two experimental sessions. However, the remaining four subjects’s EEG signals were more non-stationary, and hence the classiﬁcation performance had large variations.

The average classiﬁcation results are shown in Table 9. EA-CCSP-wAR, which integrates data alignment and TL in two components (spatial ﬁltering and classiﬁcation), achieved the best average performance. EA-RCSP-wAR, which was the best performer in cross-subject transfers in the previoussection, was slightly worse, but still better than the other 16 approaches with or without TL. On average, almost all approaches with EA outperformed their counterparts without EA, suggesting again the importance and necessity of explicitly adding a data alignment block before TL.

In summary, TL is also effective in handling non-stationarity of EEG signals in cross-session MI classiﬁcation, and considering TL in more components of the classiﬁcation pipeline is generally more beneﬁcial.

- 5. Conclusions and Future Research

Transfer learning has been widely used in MI-based BCIs to reduce the calibration effortfor a new subject, and demonstratedpromising performance. While a closed-loop MI-based BCI system, after EEG signal acquisition and temporal ﬁltering, includes spatial ﬁltering, feature engineering, and classiﬁcation blocks before sending out the control signal to an external device, previous approaches only considered TL in one or two such components.

This paper proposes that TL could be considered in all three components, and it is also very important to speciﬁcally add a data alignment component before spatial ﬁltering to make the source domain and target domain data more consistent. Ofﬂine and online classiﬁcation experiments on two MI datasets veriﬁed that:

## Subject 1

## Subject 2

## Subject 3

## Subject 4

## Subject 5

75

75

90

75

85

85

70

70

80

70

80

75

65

65

65

75

70

70

60

60

60

65

65

60

55

55

55

60

55

50

55

50

4 8 12 16 20

4 8 12 16 20

4 8 12 16 20

4 8 12 16 20

4 8 12 16 20

- 55

60

65

70

75

Subject 6

4 8 12 16 20

55

60

65

70

75

80

85

Subject 7

4 8 12 16 20

55

60

65

70

75

80

Average

|CSP-LDA<br><br>CSP-CLDA CSP-OwAR CCSP-LDA<br><br>CCSP-CLDA CCSP-OwAR RCSP-LDA<br><br>RCSP-CLDA RCSP-OwAR<br><br>EA-CSP-LDA<br><br>EA-CSP-CLDA EA-CSP-OwAR EA-CCSP-LDA<br><br>EA-CCSP-CLDA EA-CCSP-OwAR EA-RCSP-LDA<br><br>EA-RCSP-CLDA EA-RCSP-OwAR<br><br>|
|---|

(a)

4 8 12 16 20

60

- 65

70

75

80

Subject 1

4 8 12 16 20

- 48
- 49
- 50
- 51
- 52
- 53
- 54
- 55
- 56
- 57

Subject 2

4 8 12 16 20

70

75

80

85

90

95

Subject 3

4 8 12 16 20

55

60

65

70

Subject 4

4 8 12 16 20

- 47
- 48
- 49
- 50
- 51
- 52
- 53
- 54

Subject 5

4 8 12 16 20

52

54

56

58

60

62

64

66

Subject 6

4 8 12 16 20

52

- 54

56

58

60

62

- 64

- 66

4 8 12 16 20

## Subject 7

## Subject 8

## Subject 9

## Average

74

68

80

72

78

90

|CSP-LDA<br><br>CSP-CLDA CSP-OwAR CCSP-LDA<br><br>CCSP-CLDA CCSP-OwAR RCSP-LDA<br><br>RCSP-CLDA RCSP-OwAR<br><br>EA-CSP-LDA<br><br>EA-CSP-CLDA EA-CSP-OwAR EA-CCSP-LDA<br><br>EA-CCSP-CLDA EA-CCSP-OwAR EA-RCSP-LDA<br><br>EA-RCSP-CLDA EA-RCSP-OwAR<br><br>|
|---|

70

76

85

74

68

72

66

80

70

64

68

75

62

66

60

64

70

58

62

4 8 12 16 20

4 8 12 16 20

4 8 12 16 20

(b)

- Figure 7: Online cross-subject classiﬁcation accuracies (vertical axis) on the MI datasets, with different Nl (horizontal axis). (a) Dataset 1; (b) Dataset 2a.

- Table 8: Online cross-subject classiﬁcation accuracies (mean±std) of different TL approaches, and their improvements over CSP-LDA. Performance improvements not statistically signiﬁcant (α = 0.05) are marked with an underline.

[Figure 522]

[Figure 523]

[Figure 524]

[Figure 525]

Dataset 1 Dataset 2a Accuracy Improvement Accuracy Improvement

[Figure 526]

[Figure 527]

[Figure 528]

Algorithm

[Figure 529]

[Figure 530]

(%) (%) (%) (%) CSP-LDA 59.46±5.75 – 63.02±5.09 – CSP-CLDA 64.87±4.03 9.10 64.33±2.11 2.08 CSP-OwAR 65.16±4.45 9.59 64.90±2.16 2.98 CCSP-LDA 63.35±5.37 6.55 65.96±4.90 4.66

[Figure 531]

[Figure 532]

[Figure 533]

[Figure 534]

[Figure 535]

[Figure 536]

[Figure 537]

[Figure 538]

[Figure 539]

[Figure 540]

[Figure 541]

[Figure 542]

CCSP-CLDA 59.95±1.87 0.83 68.48±0.58 8.66 CCSP-OwAR 63.48±1.98 6.76 69.10±0.72 9.66

[Figure 543]

[Figure 544]

[Figure 545]

[Figure 546]

[Figure 547]

RCSP-LDA 65.11±4.38 9.50 65.61±4.00 4.12 RCSP-CLDA 68.31±0.96 14.89 70.27±0.81 11.51 RCSP-OwAR 69.35±0.86 16.64 70.76±0.69 12.29

[Figure 548]

[Figure 549]

[Figure 550]

[Figure 551]

[Figure 552]

[Figure 553]

[Figure 554]

EA-CSP-LDA 59.22±5.37 -0.41 62.73±5.20 -0.47 EA-CSP-CLDA 70.58±5.00 18.70 68.26±2.49 8.31 EA-CSP-OwAR 70.66±5.51 18.83 68.32±2.56 8.41 EA-CCSP-LDA 68.09±5.43 14.52 66.69±4.61 5.83 EA-CCSP-CLDA 76.13±1.38 28.03 72.25±1.07 14.64 EA-CCSP-OwAR 76.36±1.39 28.43 72.26±1.02 14.66 EA-RCSP-LDA 66.10±5.43 11.16 68.20±4.67 8.23 EA-RCSP-CLDA 77.55±2.33 30.42 73.04±1.22 15.90 EA-RCSP-OwAR 77.80±2.41 30.84 73.03±1.27 15.89

[Figure 555]

[Figure 556]

[Figure 557]

[Figure 558]

[Figure 559]

[Figure 560]

[Figure 561]

[Figure 562]

[Figure 563]

[Figure 564]

[Figure 565]

[Figure 566]

[Figure 567]

[Figure 568]

[Figure 569]

[Figure 570]

[Figure 571]

[Figure 572]

[Figure 573]

[Figure 574]

PS-CSP-LDA 59.23±5.53 -0.38 62.75±5.23 -0.43 PS-CSP-CLDA 71.45±4.84 20.17 69.04±2.32 9.55 PS-CSP-OwAR 71.26±5.33 19.84 68.96±2.48 9.43 PS-CCSP-LDA 67.14±5.22 12.91 67.04±3.66 6.39 PS-CCSP-CLDA 76.25±1.13 28.23 72.47±1.10 14.99 PS-CCSP-OwAR 76.73±1.16 29.05 72.54±1.15 15.10 PS-RCSP-LDA 67.60±5.10 13.69 67.40±4.15 6.95 PS-RCSP-CLDA 76.62±1.16 28.86 72.69±1.33 15.34 PS-RCSP-OwAR 77.02±1.07 29.54 72.75±1.30 15.44

[Figure 575]

[Figure 576]

[Figure 577]

[Figure 578]

[Figure 579]

[Figure 580]

[Figure 581]

[Figure 582]

[Figure 583]

[Figure 584]

[Figure 585]

[Figure 586]

[Figure 587]

[Figure 588]

[Figure 589]

[Figure 590]

[Figure 591]

- Table 9: Ofﬂine cross-session classiﬁcation accuracies (mean±std) of different TL approaches, and their improvements over CSP-LDA. All performance improvements were statistically signiﬁcant (α = 0.05).

[Figure 592]

[Figure 593]

Algorithm Accuracy (%) Improvement (%) CSP-LDA 62.30±5.03 –

[Figure 594]

[Figure 595]

[Figure 596]

CSP-CLDA 69.03±2.30 10.81

[Figure 597]

CSP-wAR 70.01±2.24 12.38 CCSP-LDA 67.87±3.39 8.95 CCSP-CLDA 72.44±0.18 16.27 CCSP-wAR 74.10±0.17 18.95 RCSP-LDA 66.14±3.18 6.16 RCSP-CLDA 72.68±0.45 16.66

[Figure 598]

[Figure 599]

[Figure 600]

[Figure 601]

[Figure 602]

[Figure 603]

RCSP-wAR 72.80±0.34 16.85 EA-CSP-LDA 62.00±5.13 -0.48

[Figure 604]

[Figure 605]

[Figure 606]

EA-CSP-CLDA 70.98±2.00 13.93

[Figure 607]

EA-CSP-wAR 71.22±2.04 14.32 EA-CCSP-LDA 67.88±3.79 8.95 EA-CCSP-CLDA 74.87±0.17 20.17 EA-CCSP-wAR 75.56±0.05 21.29 EA-RCSP-LDA 67.44±3.18 8.26 EA-RCSP-CLDA 74.10±0.48 18.94

[Figure 608]

[Figure 609]

[Figure 610]

[Figure 611]

[Figure 612]

[Figure 613]

EA-RCSP-wAR 75.17±0.24 20.66

[Figure 614]

## Subject 1

## Subject 2

## Subject 3

## Subject 4

## Subject 5

## Subject 6

95

90

68

- 50
- 51
- 52
- 53
- 54
- 55
- 56
- 57
- 58
- 59

60

66

85

70

90

64

58

80

62

85

65

56

60

75

80

58

54

60

70

56

75

52

54

- 65

55

52

70

50

60

50

0 4 8 12 16 20

0 4 8 12 16 20

0 4 8 12 16 20

0 4 8 12 16 20

0 4 8 12 16 20

0 4 8 12 16 20

## Subject 7

## Subject 8

## Subject 9

## Average

80

74

80

95

72

75

|CSP-LDA<br><br>CSP-CLDA<br><br>CSP-wAR<br><br>CCSP-LDA<br><br>CCSP-CLDA<br><br>CCSP-wAR RCSP-LDA RCSP-CLDA<br><br>RCSP-wAR<br><br>EA-CSP-LDA<br><br>EA-CSP-CLDA<br><br>EA-CSP-wAR<br><br>EA-CCSP-LDA<br><br>EA-CCSP-CLDA<br><br>EA-CCSP-wAR EA-RCSP-LDA EA-RCSP-CLDA<br><br>EA-RCSP-wAR|
|---|

90

70

75

70

68

85

70

66

65

80

64

65

62

60

75

60

60

70

- 55

58

56

0 4 8 12 16 20

0 4 8 12 16 20

0 4 8 12 16 20

0 4 8 12 16 20

- Figure 8: Ofﬂine cross-session classiﬁcation accuracies (vertical axis) on Dataset 2a, with different Nl (horizontal axis).

- 1. Generally, using TL in different components of Figure 2 can achieve better classiﬁcation performance than not using it, in both cross-subject and cross-session classiﬁcation, for both online and ofﬂine classiﬁcation.
- 2. Generally, a more sophisticated TL approach outperforms a simple one.
- 3. Data alignment is a very important preprocessing step in TL. It beneﬁts both traditional machine learning and deep learning.
- 4. TL in different components of Figure 2 could be complementary to each other, so integrating them can further improve the classiﬁcation performance.

The following directions will be considered in our future research:

- 1. Compared with other components, not enough attention has been paid to TL in feature engineering of BCI systems. We will develop more sophisticated TL approaches for feature engineering in the future, and also other components in Figure 2.
- 2. This paper considers only binary MI classiﬁcation problems in BCIs. We will extend the analysis to other BCI classiﬁcation paradigms, e.g., event-related potentials and steady-state visual evoked potentials, and also BCI regression problems, e.g., driver drowsiness estimation [5, 47] and user reaction-time estimation [49]. Furthermore, we will also consider TL in multi-class classiﬁcation.
- 3. It has been shown [46, 48] that integrating TL with active learning [25] in the classiﬁer can further improve the ofﬂine classiﬁcation performance. It is interesting to study if TL and active learning can be integrated in other components of the BCI system, e.g., spatial ﬁltering and feature engineering.

References

- [1] H. Albalawi, X. Song, A study of kernel CSP-based motor imagery brain computer interface classiﬁcation, in: Proc. IEEE Signal Processing in Medicine and Biology Symposium, New York City, NY, 1–4, 2012.
- [2] B. Blankertz, G. Dornhege, M. Krauledat, K. R. Muller, G. Curio, The noninvasive Berlin Brain-Computer Interface: Fast acquisition of effective performance in untrained subjects, NeuroImage 37 (2) (2007) 539–550.
- [3] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, K. R. Muller, Optimizing Spatial ﬁlters for Robust EEG Single-Trial Analysis, IEEE Signal Processing Magazine 25 (1) (2008) 41–56.
- [4] L.-L. Chen, A. Zhang, X.-G. Lou, Cross-subject driver status detection from physiological signals based on hybrid feature selection and transfer learning, Expert Systems with Applications 137 (2019) 266–280.
- [5] Y. Cui, Y. Xu, D. Wu, EEG-Based Driver Drowsiness Estimation Using Feature Weighted Episodic Training, IEEE Trans. on Neural Systems and Rehabilitation Engineering 27 (11) (2019) 2263–2273.
- [6] M. Dai, D. Zheng, S. Liu, P. Zhang, Transfer kernel common spatial patterns for motor imagery brain-computer interface classiﬁcation, Computational and Mathematical Methods in Medicine 2018.
- [7] A. Delorme, S. Makeig, EEGLAB: an open source toolbox for analysis of singletrial EEG dynamics including independent component analysis, Journal of Neuroscience Methods 134 (2004) 9–21.
- [8] P. T. Fletcher, S. Joshi, Principal geodesic analysis on symmetric spaces: Statistics of diffusion tensors, Lecture Notes in Computer Science 3117 (2004) 87–98.
- [9] H. He, D. Wu, Different Set Domain Adaptation for Brain-Computer Interfaces: A Label Alignment Approach, IEEE Trans. on Neural Systems and Rehabilitation Engineering 28 (5) (2020) 1091–1108.
- [10] H. He, D. Wu, Transfer Learning for Brain-Computer Interfaces: A Euclidean Space Data Alignment Approach, IEEE Trans. on Biomedical Engineering 67 (2)

(2020) 399–410.

- [11] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, M. Grosse-Wentrup, Transfer learning in brain-computer interfaces, IEEE Computational Intelligence Magazine 11 (1) (2016) 20–31.
- [12] I. Jolliffe, Principal Component Analysis, Wiley Online Library, 2002.
- [13] I. Kononenko, Estimating attributes: Analysis and extensions of RELIEF, in: Proc. European Conf. on Machine Learning, Catania, Italy, 171–182, 1994.

- [14] D. Kostas, F. Rudzicz, Thinker invariance: enabling deep neural networks for BCI across more people, Journal of Neural Engineering 17 (5) (2020) 056008.
- [15] T. D. Lagerlund, F. W. Sharbrough, N. E. Busacker, Spatial Filtering of Multichannel Electroencephalographic Recordings Through Principal Component Analysis by Singular Value Decomposition, Journal of Clinical Neurophysiology 14 (1) (1997) 73–82.
- [16] B. J. Lance, S. E. Kerick, A. J. Ries, K. S. Oie, K. McDowell, Brain-Computer Interface Technologies in the Coming Decades, Proc. of the IEEE 100 (3) (2012) 1585–1599.
- [17] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, B. J. Lance, EEGNet: a compact convolutional neural network for EEG-based braincomputer interfaces, Journal of Neural Engineering 15 (5) (2018) 056013.
- [18] C.-T. Lin, C. Chuang, Y. Hung, C. Fang, D. Wu, Y.-K. Wang, A Driving Performance Forecasting System Based on Brain Dynamic State Analysis Using 4-D Convolutional Neural Networks, IEEE Trans. on Cybernetics In press.
- [19] S. R. Liyanage, C. Guan, H. Zhang, K. K. Ang, J. Xu, T. H. Lee, Dynamically weighted ensemble classiﬁcation for non-stationary EEG processing, Journal of Neural Engineering 10 (3) (2013) 036007.
- [20] M. Long, J. Wang, G. Ding, S. J. Pan, P. S. Yu, Adaptation Regularization: A General Framework for Transfer Learning, IEEE Trans. on Knowledge and Data Engineering 26 (5) (2014) 1076–1089.
- [21] M. Long, J. Wang, J. Sun, S. Y. Philip, Domain invariant transfer kernel learning, IEEE Trans. on Knowledge and Data Engineering 27 (6) (2015) 1519–1532.
- [22] F. Lotte, Signal Processing Approaches to Minimize or Suppress Calibration Time in Oscillatory Activity-Based Brain-Computer Interfaces, Proc. of the IEEE 103 (6) (2015) 871–890.
- [23] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotomamonjy, F. Yger, A review of classiﬁcation algorithms for EEG-based brain-computer interfaces: a 10 year update, Journal of Neural Engineering 15 (3) (2018) 031005.
- [24] H. Lu, H.-L. Eng, C. Guan, K. N. Plataniotis, A. N. Venetsanopoulos, Regularized common spatial pattern with aggregation for EEG classiﬁcation in small-sample setting, IEEE Trans. on Biomedical Engineering 57 (12) (2010) 2936–2946.
- [25] A. Marathe, V. Lawhern, D. Wu, D. Slayback, B. Lance, Improved neural signal classiﬁcation in a rapid serial visual presentation task using active learning, IEEE Trans. on Neural Systems and Rehabilitation Engineering 24 (3) (2016) 333–343.
- [26] M. Moakher, A differential geometric approach to the geometric mean of symmetric Positive-Deﬁnite matrices, SIAM Journal on Matrix Analysis and Applications 26 (3) (2005) 735–747.

- [27] L. F. Nicolas-Alonso, J. Gomez-Gil, Brain computer interfaces, a review, Sensors 12 (2) (2012) 1211–1279.
- [28] S. J. Pan, Q. Yang, A survey on transfer learning, IEEE Trans. on Knowledge and Data Engineering 22 (10) (2010) 1345–1359.
- [29] H. Peng, F. Long, C. Ding, Feature selection based on mutual information criteria of max-dependency,max-relevance, and min-redundancy,IEEE Trans. on Pattern Analysis and Machine Intelligence 27 (8) (2005) 1226–1238.
- [30] X. Pennec, P. Fillard, N. Ayache, A Riemannian framework for tensor computing, International Journal of Computer Vision 66 (1) (2006) 41–66.
- [31] G. Pfurtscheller, G. R. Mu¨ller-Putz, R. Scherer, C. Neuper, Rehabilitation with brain-computer interface systems, Computer 41 (10) (2008) 58–65.
- [32] G. Pfurtscheller, C. Neuper, Motor imagery and direct brain-computer communication, Proc. of the IEEE 89 (7) (2001) 1123–1134.
- [33] H. Ramoser, J. Muller-Gerking, G. Pfurtscheller, Optimal spatial ﬁltering of single trial EEG during imagined hand movement, IEEE Trans. on Rehabilitation Engineering 8 (4) (2000) 441–446.
- [34] R. P. Rao, R. Scherer, Chapter 10 - Statistical Pattern Recognition and Machine Learning in Brain-Computer Interfaces, in: K. G. Oweiss (Ed.), Statistical Signal Processing for Neuroscience and Neurotechnology, Academic Press, Oxford, 335–367, 2010.
- [35] B. Rivet, A. Souloumiac, V. Attina, G. Gibert, xDAWN algorithm to enhance evoked potentials: application to brain-computer interface, IEEE Trans. on Biomedical Engineering 56 (8) (2009) 2035–2043.
- [36] P. L. C. Rodrigues, C. Jutten, M. Congedo, Riemannian Procrustes Analysis: Transfer Learning for Brain–Computer Interfaces, IEEE Trans. on Biomedical Engineering 66 (8) (2019) 2390–2401.
- [37] R. N. Roy, S. Bonnet, S. Charbonnier, P. Jallon, A. Campagne, A comparison of ERP spatial ﬁltering methods for optimal mental workload estimation, in: Proc. 37th Annual Int’l Conf. of the IEEE Engineeringin Medicine and Biology Society (EMBC), 7254–7257, 2015.
- [38] S. Saha, K. I. U. Ahmed, R. Mostafa, L. Hadjileontiadis, A. Khandoker, Evidence of Variabilities in EEG Dynamics During Motor Imagery-Based Multiclass Brain–Computer Interface, IEEE Trans. on Neural Systems and Rehabilitation Engineering 26 (2) (2018) 371–382.
- [39] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, T. Ball, Deep learning with convolutional neural networks for EEG decoding and visualization, Human Brain Mapping 38 (11) (2017) 5391–5420.

- [40] M. Teplan, Fundamentals of EEG measurement, Measurement Science Review 2 (2) (2002) 1–11.
- [41] J. van Erp, F. Lotte, M. Tangermann, Brain-Computer Interfaces: Beyond Medical Applications, Computer 45 (4) (2012) 26–34, ISSN 0018-9162.
- [42] P. Wang, J. Lu, B. Zhang, Z. Tang, A Review on Transfer Learning for BrainComputer Interface Classiﬁcation, in: Proc. 5th Int’l Conf. on Information Science and Technology, Changsha, China, 2015.
- [43] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, T. M. Vaughan, Brain-computer interfaces for communication and control, Clinical Neurophysiology 113 (6) (2002) 767–791.
- [44] D. Wu, Online and Ofﬂine Domain Adaptation for Reducing BCI Calibration Effort, IEEE Trans. on Human-Machine Systems 47 (4) (2017) 550–563.
- [45] D. Wu, J.-T. King, C.-H. Chuang, C.-T. Lin, T.-P. Jung, Spatial Filtering for EEGBased Regression Problems in Brain-Computer Interface (BCI), IEEE Trans. on Fuzzy Systems 26 (2) (2018) 771–781.
- [46] D. Wu, B. J. Lance, V. J. Lawhern, Transfer Learning and Active Transfer Learning for Reducing Calibration Data in Single-Trial Classiﬁcation of VisuallyEvoked Potentials, in: Proc. IEEE Int’l Conf. on Systems, Man, and Cybernetics, San Diego, CA, 2014.
- [47] D. Wu, V. J. Lawhern, S. Gordon, B. J. Lance, C.-T. Lin, Driver Drowsiness Estimation from EEG Signals Using Online Weighted Adaptation Regularization for Regression (OwARR), IEEE Trans. on Fuzzy Systems 25 (6) (2017) 1522– 1535.
- [48] D. Wu, V. J. Lawhern, W. D. Hairston, B. J. Lance, Switching EEG headsets made easy: Reducing ofﬂine calibration effort using active wighted adaptation regularization, IEEE Trans. on Neural Systems and Rehabilitation Engineering 24 (11) (2016) 1125–1137.
- [49] D. Wu, V. J. Lawhern, B. J. Lance, S. Gordon, T.-P. Jung, C.-T. Lin, EEGBased User Reaction Time Estimation Using Riemannian Geometry Features, IEEE Trans. on Neural Systems and Rehabilitation Engineering 25 (11) (2017) 2157–2168.
- [50] D. Wu, Y. Xu, B.-L. Lu, Transfer Learning for EEG-Based Brain-Computer Interfaces: A Review of Progress Made Since 2016, IEEE Trans. on Cognitive and Developmental Systems In press.
- [51] L. Xu, M. Xu, Y. Ke, X. An, S. Liu, D. Ming, Cross-dataset Variability Problem in EEG Decoding with Deep Learning, Frontiers in Human Neuroscience 14 (2020) 103.

- [52] F. Yger, M. Berar, F. Lotte, Riemannian approaches in brain-computer interfaces: a review, IEEE Trans. on Neural Systems and Rehabilitation Engineering 25 (10)

(2017) 1753–1762.

- [53] P. Zanini, M. Congedo, C. Jutten, S. Said, Y. Berthoumieu, Transfer Learning: a Riemannian geometry framework with applications to Brain-Computer Interfaces, IEEE Trans. on Biomedical Engineering 65 (5) (2018) 1107–1116.
- [54] W. Zhang, D. Wu, Manifold Embedded Knowledge Transfer for Brain-Computer Interfaces, IEEE Trans. on Neural Systems and Rehabilitation Engineering 28 (5)

(2020) 1117–1127.

