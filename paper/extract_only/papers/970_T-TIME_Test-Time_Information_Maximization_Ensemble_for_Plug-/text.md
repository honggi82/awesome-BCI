# T-TIME: Test-Time Information Maximization Ensemble for Plug-and-Play BCIs

Siyang Li, Ziwei Wang, Hanbin Luo, Lieyun Ding, and Dongrui Wu

arXiv:2412.07228v1[cs.HC]10Dec2024

Abstract—Objective: An electroencephalogram (EEG)-based brain-computer interface (BCI) enables direct communication between the human brain and a computer. Due to individual differences and non-stationarity of EEG signals, such BCIs usually require a subject-speciﬁc calibration session before each use, which is time-consuming and user-unfriendly. Transfer learning (TL) has been proposed to shorten or eliminate this calibration, but existing TL approaches mainly consider ofﬂine settings, where all unlabeled EEG trials from the new user are available. Methods: This paper proposes Test-Time Information Maximization Ensemble (T-TIME) to accommodate the most challenging online TL scenario, where unlabeled EEG data from the new user arrive in a stream, and immediate classiﬁcation is performed. T-TIME initializes multiple classiﬁers from the aligned source data. When an unlabeled test EEG trial arrives, T-TIME ﬁrst predicts its labels using ensemble learning, and then updates each classiﬁer by conditional entropy minimization and adaptive marginal distribution regularization. Our code is publicized. Results: Extensive experiments on three public motor imagery based BCI datasets demonstrated that T-TIME outperformed about 20 classical and state-of-the-art TL approaches. Signiﬁcance: To our knowledge, this is the ﬁrst work on test time adaptation for calibration-free EEG-based BCIs, making plug-and-play BCIs possible.

Index Terms—Brain-computer interface, electroencephalogram, motor imagery, test-time adaptation, transfer learning

I. INTRODUCTION

A brain-computer interface (BCI) [1] enables direct communication between the human brain and a computer by neural activities of the user. It can assist, augment, or even repair human cognitive or sensory–motor functions [2]. In addition to rehabilitation for disabled people, BCIs have also found applications for able-bodied users in device control, education, gaming, and so on [3].

BCIs can be categorized into non-invasive, partially invasive, and invasive ones. Among them, non-invasive BCIs, which usually use electroencephalogram (EEG) as the input signal [4], are the most convenient. The three classic paradigms in EEG-based BCIs are event-related potentials [5], steady-state visual evoked potentials [6], and motor imagery

S. Li, Z. Wang and D. Wu are with the Ministry of Education Key Laboratory of Image Processing and Intelligent Control, School of Artiﬁcial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China. They are also with the Shenzhen Huazhong University of Science and Technology Research Institute, Shenzhen, China. S. Li is also with the Henan Key Laboratory of Brain Science and Brain Computer Interface Technology, School of Electrical and Information Engineering, Zhengzhou University.

H. Luo and L. Ding are with the School of Civil and Hydraulic Engineering, Huazhong University of Science and Technology, Wuhan 430074 China.

Corresponding Authors: Lieyun Ding (dly@hust.edu.cn) and Dongrui Wu (drwu@hust.edu.cn).

(MI) [7]. In an MI-based BCI, the user imagines the movement of his/her body parts (e.g., left hand, right hand, both feet, or tongue), which modulates different areas of the motor cortex of the brain [8]. These imageries are then mapped into speciﬁc commands for external device control.

Despite various advantages, such as noninvasiveness and low cost, EEG demonstrates signiﬁcant individual differences, i.e., for the same task, different users usually exhibit different EEG responses. The current solution requires a subject-speciﬁc calibration session before each use, which is time-consuming and user-unfriendly, hindering their broad real-world applications.

Transfer learning (TL) [4], [8], which utilizes knowledge from previous users (source domains) to facilitate the learning for a new user (target domain), is a promising solution to alleviate individual differences and hence to reduce or eliminate the calibration effort. There are three different TL scenarios when the target domain is completely unlabeled:

- 1) Unsupervised domain adaptation (UDA), where the labeled source data and the unlabeled target data are combined for ofﬂine learning.
- 2) Source-free UDA (SFUDA), where the source model, instead of the source data, is used in UDA, usually for source domain privacy protection.
- 3) Test-time adaptation (TTA), where the source model is updated online to the target domain, whose test samples are classiﬁed in real-time.

A comparison of these three settings is shown in Fig. 1.

Existing TL approaches mainly consider ofﬂine UDA or SFUDA settings, where all unlabeled target data are available. However, in real-world online TTA applications, such as MIbased wheelchair control, unlabeled EEG trials arrive in a stream, and immediate classiﬁcation is required.

This paper proposes Test-Time Information Maximization Ensemble (T-TIME) to accommodate the most challenging online TTA scenario for calibration-free EEG-based BCIs. TTIME initializes multiple classiﬁers from the aligned source data. When an unlabeled test EEG trial arrives, T-TIME ﬁrst predicts its labels using ensemble learning, and then updates each classiﬁer by conditional entropy minimization and adaptive marginal distribution regularization. Extensive experiments on three public MI-based BCI datasets demonstrated that T-TIME outperformed about 20 classical and stateof-the-art TL approaches. To our knowledge, this is the ﬁrst study on TTA for plug-and-play EEG-based BCIs. Our code is also publicized.

The remainder of this paper is organized as follows: Section II introduces related work. Section III proposes T-TIME.

feature alignment by minimizing the maximum mean discrepancies. Domain-adversarial neural network (DANN) [15] and conditional domain adversarial network (CDAN) [16] use adversarial training to reduce the feature discrepancies between the source and target domains.

3) Output space. Minimum class confusion (MCC) [17] utilizes a weighted prediction entropy to minimize the class confusion. Liang et al. [18] introduced an auxiliary classiﬁer to improve the quality of the target domain pseudo labels.

- (a)

[Figure 1]

[Figure 2]

- (b)

| | | | |
|---|---|---|---|

[Figure 3]

[Figure 4]

| | | | |
|---|---|---|---|

- (c)

- B. Source-free Unsupervised Domain Adaptation

SFUDA [19] uses the source model, instead of the source data, for UDA. It is appropriate for source domain privacy protection, but generally more challenging to implement.

Source HypOthesis Transfer (SHOT) [20] uses information maximization and self-supervised learning for feature extraction in the target domain. To explicitly consider class-imbalance, imbalanced source-free domain adaptation (ISFDA) [21] uses intra-class tightening and inter-class separation to form better decision boundaries.

SFUDA has also been used in EEG-based BCIs for privacy protection [22]. Li et al. [23] proposed a meta-learning strategy for multi-source model transfer. Zhang et al. considered lightweight SFUDA [24] and multi-source decentralized SFUDA [25] for privacy-preserving BCIs.

- C. Test-time Adaptation

Both UDA and SFUDA assume all unlabeled target data are available, i.e., they target at ofﬂine applications. On the contrast, TTA [26] focuses on online applications. In TTA, target data arrive in a stream, and a prediction must be immediately made for each coming sample. Thus, it is more challenging than UDA and SFUDA.

- Fig. 1. Three different TL settings, when the target domain is completely unlabeled. (a) Unsupervised domain adaptation (UDA); (b) source-free unsupervised domain adaptation (SFUDA); and, (c) test-time adaptation (TTA).

Section IV presents experimental results to demonstrate the performance of T-TIME. Finally, Section V draws conclusions and points out some future research directions.

Target domain pseudo-labels [27] can be used for model adaptation in TTA. For example, Chen et al. [28] combined contrastive learning with self-supervision on reﬁned online pseudo-labels, and test-time template adjuster (T3A) [29] efﬁciently integrates few-shot learning with pseudo-labeling.

II. RELATED WORKS

Entropy-based uncertainty reduction has also been employed in TTA. For example, test entropy minimization (Tent) [30] performs TTA on normalization layers, and marginal entropy minimization with one test point (MEMO) [31] utilizes self-supervised augmentations for marginal entropy minimization.

This section introduces related works on deep learning based TL.

A. Unsupervised Domain Adaptation

UDA [9] combines the labeled source data and the unlabeled target data for ofﬂine learning. The domain discrepancies can be reduced from three perspectives:

The literature has also considered more challenging and complex scenarios that general TTA approaches may fail. Sharpness-aware and reliable entropy minimization (SAR) [32] selects samples with smaller entropy losses and jointly minimizes the sharpness of the entropy and the entropy loss for a more reliable adaptation. Degradation-freE fuLly Test-time Adaptation (DELTA) [33] uses dynamic online reweighting (a momentum-updated class frequency) to weight each test sample in calculating the conditional entropy to cope with test-time class-imbalance.

- 1) Input space. CORrelation ALignment (CORAL) [10] aligns the second-order statistics of different input distributions with a linear transformation. For multi-channel EEG signals, Riemannian geometry-based approach [11] and Euclidean alignment (EA) [12] have demonstrated outstanding performance.
- 2) Feature space. Deep adaptation network (DAN) [13] and joint adaptation network (JAN) [14] perform

Continual TTA handles test data ﬂow with continually changing distribution. Continual test-time adaptation (CoTTA) [34] utilizes pseudo-labels that are both weightaveraged and augmentation-averaged for adaptation in a teacher-student model. Lange et al. [35] proposed a pseudoprototypical proxy loss to encourage inter-class variance and reduce intra-class variance with a class-balanced data replay strategy for continual learning.

III. TEST-TIME INFORMATION MAXIMIZATION ENSEMBLE (T-TIME)

We focus on closed set domain adaptation, i.e., the source and target domains have identical input and label spaces but different marginal and conditional probability distributions.

- A. Problem Setup

Assume the K-class classiﬁcation problem involves L source subjects, and the l-th (l = 1,...,L) source subject has ns,l labeled EEG trials {(Xs,li ,ys,li )}ni=1s,l, where Xs,li ∈ Rch×ts is the i-th EEG trial (ch is the number of EEG channels, and ts the number of time samples), and ys,li the corresponding label. nt test EEG trials {Xti}n

t

i=1 from the target subject arrive online sequentially, and the goal is to predict their labels {yti}n

t

i=1 in a completely unsupervised and online manner. More speciﬁcally, at test time a, only the source data and {Xti}ai=1 can be used to make the prediction yˆta for Xta.

Our proposed T-TIME, shown in Fig. 2, uses the source model predictions on the test data to calibrate the target model, without using any labeled target data.

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| |
|---|

| |
|---|

| | |
|---|---|
| | |

| |
|---|

| | |
|---|---|
| | |

[Figure 5]

[Figure 6]

[Figure 7]

| | |
|---|---|
| | |

[Figure 8]

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

Fig. 2. Flowchart of the proposed T-TIME.

- B. Source Model Training

We perform Euclidean alignment (EA) [12] on each source subject individually to reduce the individual differences, and then combine all aligned EEG trials from the L source subjects into a single source domain to train M source models.

For the l-th (l = 1,...,L) source subject, EA computes the arithmetic mean of all covariance matrices of his/her EEG trials [12]:

ns,l

1 ns,l

R¯s,l =

Xs,li (Xs,li )⊤, (1)

[Figure 9]

i=1

and then performs the alignment by

X˜s,li = R¯s,l−1/2Xs,li , i = 1,...,ns,l. (2) All

{X˜s,li }ni=1s,l are then assembled into {X˜si}n

s

i=1 and

l=1,...,L

viewed as a single source domain, where ns = Ll=1 ns,l. The labels are accordingly assembled into {ysi}n

s

i=1.

M EEGNet [36] models {fm}Mm=1, each with random initialization, can then be independently trained from {(X˜si,ysi)}n

s

i=1 by minimizing the classic cross-entropy loss. C. Incremental EA (IEA) on Target Data

The target EEG trials arrive online one by one, so we perform incremental EA on them.

More speciﬁcally, when Xta arrives, we ﬁrst update: R¯ta =

a

1 a

Xti(Xti)⊤, (3)

[Figure 10]

i=1

and then perform EA on {Xti}ai=1 using: X˜ti = R ¯ta −1/2Xti, i = 1,...,a. (4)

{X˜ti}ai=1 then replace {Xti}ai=1 as the input to {fm}Mm=1 for classiﬁcation.

D. Target Label Prediction

The M TTA models {fm}Mm=1 are initialized from the M source models trained above, and updated after the arrival of each Xti, using the procedure introduced in the next subsection.

Assume {fm}Mm=1 have been updated up to Xta−1. When the next test EEG trial Xta arrives, it is transformed into X˜ta using incremental EA introduced in the previous subsection,

input into each fm for classiﬁcation, and then the M probability vectors {fm(X˜ta)}Mm=1 are combined using ensemble learning to obtain the predicted label yˆta :

- 1) When a ≤ M, the individual probability vectors

{fm(X˜ta)}Mm=1 are averaged, and yˆta is the class with the largest average probability.

- 2) When a > M, the spectral meta-learner (SML) [37]

is used to weighted average {fm(X˜ta)}Mm=1. SML constructs a meta-classiﬁer, more accurate than most, if not all, of the individual classiﬁers, using only their predictions on the unlabeled test data. The original SML was proposed for binary classiﬁcation with 0/1 predictions. To accommodate the TTA setting, we use it for multi-class classiﬁcation with continuous prediction probabilities.

⊤

Let Fk(X˜ti) = δk f1(X˜ti) ;...;δk fM(X˜ti)

be the predicted probabilities of all M models for class k, where δk is the k-th element of the softmax output of fm(X˜ti). SML ﬁrst computes the sample covariance matrix, Qk ∈ RM×M, of the M classiﬁers [37]:

a

1 a − 1

Fk(X˜ti) − E[Fk(X˜t)]

Qk =

[Figure 11]

i=1

⊤

· Fk(X˜ti) − E[Fk(X˜t)]

. (5)

Qk approximates a rank-one matrix, and the entries of its principal eigenvector vk are proportional to the balanced classiﬁcation accuracies of the M models [37]. A meta-learner can then be constructed by a weighted combination of the M prediction probabilities:

2) Adaptive Marginal Distribution Regularization: Only minimizing the conditional entropy above may result in two undesirable outcomes: 1) a trivial solution that all test data are classiﬁed into a single class; or, 2) a wrong classiﬁcation becomes overly conﬁdent. For remedy, we further add withinbatch marginal label distribution regularization.

M

Speciﬁcally, the average prediction probability p¯k (also with temperature factor T) for class k in the sliding batch is:

δk fm(X˜ta) · vk,m, (6)

yˆta = argmax

k

m=1

a

fm(X˜ti) T

where vk,m is the m-th element of vk.

1 B

p¯k =

. (9)

δk

[Figure 12]

[Figure 13]

i=a−B+1

E. Target Model Update

The entropy sum of p¯k evaluated on each target batch was used in [20] as a diversity loss for regularizing LCEM in SFUDA, also known as the information maximization (IM) loss, assuming the target domain is class-balanced. Such an assumption may be true on simple ofﬂine tasks with a large batch size, but could lead to biased optimization towards the dominant class [33] for online TTA with class-imbalance and small batch size [32], [39].

The target models are updated using a sliding batch with size B. When there are not enough target data, i.e., a < B, the target models are ﬁxed to be {fm}Mm=1. They are updated for every Xta when a ≥ B.

When Xta arrives, {Xti}ai=a−B+1 are ﬁrst transformed into {X˜ti}ai=a−B+1 through incremental EA, and then the loss function for updating fm is:

Thus, we propose adaptive label marginal distribution regularization for class-imbalanced test batches. During adaptation, the target domain class-frequency is estimated using pseudolabeling with conﬁdence threshold on the test data. Speciﬁcally, the estimated target class-frequency zk for class k at test time a is:

Lm =LCEM(fm;{X˜ti}ai=a−B+1)

+ LMDR(fm;{X˜ti}ai=a−B+1), (7)

where LCEM and LMDR account for conditional entropy minimization and adaptive marginal distribution regularization, respectively, as illustrated in Fig. 3 and detailed next.

zk = {Xti | i ∈ [a − B + 1,a],δk fm(X˜ti) ≥ τ} , (10)

[Figure 14]

| | |
|---|---|
| | |

| | | | | |
|---|---|---|---|---|
|[Figure 15]| | | | |
| | | | | |
|[Figure 16]| | | | |
| | | | | |

where τ ∈ [0.5,1.0) is a hyper-parameter of pseudo-labeling conﬁdence threshold.

| | |
|---|---|

| | |
|---|---|
| | |

| | |
|---|---|
| | |

The average prediction probability p¯k is recalibrated as: qk =

[Figure 17]

p¯k c + zk

, (11)

[Figure 18]

| | |
|---|---|

| | | |
|---|---|---|
| | | |

where c is a small integer to avoid dividing by zero, and also to make sure qk is neither too big nor too small at the beginning of the test phase.

- Fig. 3. Conditional entropy minimization and adaptive marginal distribution regularization in target model update.

The normalized qk, i.e., qˆk =

1) Conditional Entropy Minimization: Conditional entropy minimization suppresses the within-sample prediction uncertainty, i.e., it forces the adapted model to have high prediction conﬁdence on the test data.

qk K i=1 qi

, (12)

[Figure 19]

is then used in adaptive marginal distribution regularization:

We ﬁne-tune all parameters of fm, instead of only the normalization layers [30], which is unstable and may fail under hard cases [32]. Speciﬁcally, our loss function uses Shannon entropy to measure the conditional entropy of the predicted probabilities:

K

LMDR(fm;{X˜ti}ai=a−B+1) =

qˆk · log qˆk. (13)

k=1

This recalibration prevents falsely penalizing the model for skewed label distribution under observed class-imbalance.

LCEM(fm;{X˜ti}ai=a−B+1)

F. The Complete T-TIME Algorithm

a

K

fm(X˜ti) T

fm(X˜ti) T

1 B

= −

· log δk

.

δk

The pseudo-code of T-TIME is given in Algorithm 1. Note that {fm}Mm=1 are independently initialized and updated in both training and adaptation, consistent with the conditional independence assumption of SML [37]. Note also that for each arriving Xta, its prediction is ﬁrst made, and then {fm}Mm=1 are updated. The implication for deploying the algorithm in real-world BCI applications is that the algorithm would ﬁrst make target label prediction, and then conduct target model

[Figure 20]

[Figure 21]

[Figure 22]

i=a−B+1

k=1

(8)

Note that temperature scaling [38] with factor T is used to recalibrate the model’s prediction conﬁdence on the target data. LCEM forces fm to have a high prediction probability towards one speciﬁc class on each test sample, resulting in clearer class boundaries in the target domain.

update in parallel with downstream task execution. The preinference computation time only involves model inference, which should be fast. The post-inference computation time is slightly longer but still compatible with current BCI applications. More discussions on the computational cost will be given in Section IV-H.

The three main components of T-TIME consider information from three different granularity:

- 1) Conditional entropy minimization considers each test EEG trial in the sliding batch individually.
- 2) Adaptive marginal distribution regularization views the batch as a whole to accommodate class-imbalance.
- 3) SML aggregates different classiﬁers, which have incorporated information from both the source domain and all available target data.

[Figure 23]

Algorithm 1 Test-Time Information Maximization Ensemble (T-TIME).

[Figure 24]

Input: L source domains, each with labeled data {(Xs,li ,ys,li )}ni=1s,l, l = 1,...,L; Streaming target data {Xti}ai=1; M, the number of base classiﬁers; B, the sliding batch size; T, the temperature rescaling factor in (8) and (9); τ, the conﬁdence threshold in (10); c, the small integer in (11);

Output: The classiﬁcation yˆta for Xta. // Source Model Training for l = 1 : L do

Perform EA on {Xs,li }ni=1s,l by (1) and (2) to obtain {X˜s,li }ni=1s,l;

end for Assemble all

{X˜s,li }ni=1s,l into {X˜si}n

s

i=1, and construct the corresponding {ysi}n

l=1,...,L

s

i=1. Train M models {fm}Mm=1 independently on {(X˜si,ysi)}n

s

i=1;

// Target Lata Prediction Initialize zk = 0, k = 1,...,K; Perform incremental EA on {Xti}ai=1 by (3) and (4) to obtain {X˜ti}ai=1; if a ≥ M then

Calculate Qk on {X˜ti}ai=1 by (5); Calculate vk of Qk; Calculate yˆta for X˜ta by (6);

else Calculate yˆta, which is k that maximizes the averaged Fk(X˜ta);

end if // Target Model Update if a ≥ B then

for m = 1 : M do Calculate LCEM on {X˜ti}ai=(a−B+1) by (8); Calculate LMDR on {X˜ti}ai=(a−B+1) by (9)-(13); Calculate L by (7) and update fm;

end for end if

[Figure 25]

IV. EXPERIMENTS

Extensive experiments were performed to validate the superior performance of T-TIME.

- A. Datasets

Three EEG-based MI benchmark datasets from MOABB [40] were used in our experiments. Their characteristics are summarized in Table I. For BNCI2014001, only two classes (left/right hand imaginations) were used. For all three datasets, only data from the ﬁrst session of each subject were used for training and test. The standard preprocessing steps in MOABB, including notch ﬁltering, band-pass ﬁltering, etc., were used to ensure the reproducibility.

- B. Algorithms

We compared T-TIME with about 20 classical and stateof-the-art algorithms, including traditional machine learning approaches, end-to-end deep neural networks, and UDA/SFUDA/TTA approaches:

- 1) CSP [41], which ﬁrst used the source domain labeled data to design Common Spatial Pattern (CSP) ﬁlters, and then performed feature extraction and linear discriminant analysis classiﬁcation.
- 2) EEGNet [36], a popular end-to-end Convolutional Neural Network (CNN) for EEG signal decoding. We used its latest version-4 implementation with a default crosssubject setting, which has two blocks of CNN layers and a fully-connected classiﬁcation layer.
- 3) UDA approaches, including DAN [13], JAN [14], DANN [15], CDAN+E [16], MDD [42], and MCC [17], all with EEGNet backbone.
- 4) SFUDA approaches, including SHOT [20], SHOTIM [20], and ISFDA [21], all with EEGNet backbone. Source models in SFUDA were the same as the EEGNet baseline.
- 5) TTA approaches, including BN-adapt [43], Tent [30], PL [27], T3A [29], CoTTA [34], SAR [32], DELTA [33], and T-TIME, all with EEGNet backbone. All TTA approaches used sliding batches in optimization. Source models in TTA were also the same as the EEGNet baseline.

For a fair comparison, the performance of T-TIME with and without the ensemble is separately listed. T-TIME (5) refers to the complete conﬁguration with SML (Section III-D) using 5 independently trained EEGNets with different random seeds.

EA [12] was applied before all approaches except otherwise explicitly stated. Each source subject was aligned independently using (1) and (2). For the target subject, ofﬂine algorithms performed EA using all target data, whereas online algorithms performed incremental using (3) and (4).

Leave-one-subject-out cross-validation was considered, i.e., each subject in the corresponding dataset was treated as the unlabeled test subject once, with all remaining subjects combined as the source domain. The source models were trained using the combined source domain, and the performance was tested

TABLE I SUMMARY OF THE THREE MI EEG DATASETS.

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

Number of Number of Sampling Trial Length Number of Number of Trials Types of Subjects Channels Rate (Hz) (seconds) Sessions in the First Session Imaginations

Dataset

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

- BNCI2014001 9 22 250 4 2 144 left hand, right hand

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

- BNCI2014002 14 15 512 5 2 100 right hand, both feet BNCI2015001 12 13 512 5 2 or 3 200 right hand, both feet

[Figure 49]

[Figure 50]

[Figure 51]

[Figure 52]

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

on the left-out target domain (the test data arrived sequentially one-by-one in the online setting). All experiments on deep neural networks were repeated ﬁve times to accommodate randomness. The average results on each subject, and the entire dataset, were reported.

The source EEGNet models were trained with batch size 32, learning rate 10−3, and 100 epochs using the Adam optimizer. UDA used the same settings and batch size for the target domain. SFUDA and TTA used the same learning rate and optimizer, but test batch size 8. Temperature scaling factor T = 2 was used to recalibrate the target model’s prediction conﬁdence. More discussions on the hyperparameters of TTIME are given in Section IV-F. Other hyperparameters of the baselines were set according to the recommendations in their original publications.

All algorithms were implemented in PyTorch, and the source code is available on GitHub1.

- C. Classiﬁcation Accuracies on Balanced Classes

This subsection considers the simplest setting, i.e., the test domain is class-balanced. The classiﬁcation accuracies are shown in Tables II-IV for the three datasets, respectively. Observe that:

- 1) The baselines without EA and TL did not work well for a new subject.
- 2) EA signiﬁcantly improved the classiﬁcation performance of CSP and EEGNet in both ofﬂine and online TL, and hence should be an essential data pre-processing step in TL.
- 3) Ofﬂine TL algorithms generally outperformed their online counterparts, which is intuitive, since ofﬂine TL had access to all test data.
- 4) End-to-end deep neural networks outperformed manual feature extraction approaches.
- 5) Overly complicated algorithms, e.g., CoTTA, deteriorated the classiﬁcation performance, possibly due to inadequate training data. T3A used a ﬁxed source model, and its performance indicated that building class prototypes with high dimensionality is difﬁcult. BN-adapt and Tent only updated the batch-normalization layers, which seemed insufﬁcient for our applications.
- 6) Sophisticated entropy-based approaches focusing on output-space TL, i.e., MCC, SHOT-IM, SAR and TTIME, generally performed well. MCC had the best overall performance in ofﬂine TL.

1https://github.com/sylyoung/DeepTransferEEG

7) Our proposed T-TIME performed the best among all online TL algorithms, and its performance was comparable with the best ofﬂine TL approach.

- D. Classiﬁcation Performance Under Class-Imbalance

To simulate test-time class-imbalance, half of the Class 1 samples were randomly removed from the target data, leading to a class-imbalance ratio of 2:1. The source data were still balanced.

The area under the receiver operating characteristic curve (AUC) was used as the performance measure on the classimbalanced data. The pseudo-labeling threshold τ = 0.7 and c = 4 (half the test batch size) were used in adaptive marginal distribution regularization. All other settings were the same as those in the previous subsection. The results are shown in Table V. Observe that:

- 1) Without explicitly considering test-time class-imbalance, MCC, the best-performing ofﬂine TL approach in the previous subsection, had the worst performance.
- 2) Our proposed T-TIME outperformed all approaches, including ISFDA and DELTA, which speciﬁcally consider test-time class-imbalance.

- E. Different Ensemble Strategies

A comparison of different ensemble strategies is shown in Fig. 4. With different random seeds and training batch splits, multiple EEGNet source models were trained and updated with T-TIME. Averaging and Voting are classic ensemble strategies. SML-hard and SML-soft used binary predictions and continuous prediction probabilities, respectively (SMLsoft is used in our proposed T-TIME). All strategies used identical source models and all experiments were repeated 10 times.

Fig. 4 shows that Averaging always outperformed Voting, and also generally outperformed SML-hard in binary classiﬁcation. However, our proposed SML-soft almost always achieved the best performance, and it can be used for both binary and multi-class classiﬁcations.

- F. Ablation and Parameter Sensitivity Analysis

Ablation analysis was conducted to check if each strategy used in T-TIME was effective and necessary. For target model update, the three main components were LCEM (CEM), LMDR (MDR), and temperature rescaling (TR) with factor T = 2. The results are given in Table VI, which shows that every strategy improved the performance, and using all three together achieved the best performance.

TABLE II

- CROSS-SUBJECT CLASSIFICATION ACCURACIES (%) ON BNCI2014001. THE BEST ACCURACIES IN OFFLINE TL ARE MARKED WITH *. THE BEST ACCURACIES IN ONLINE TL ARE MARKED IN BOLD, AND THE SECOND BEST BY AN UNDERLINE.

[Figure 64]

Setting Approach S0 S1 S2 S3 S4 S5 S6 S7 S8 Avg. Baselines

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

CSP (w/o EA) 82.64 50.69 69.44 66.67 47.22 62.50 71.53 88.19 68.06 67.44 EEGNet (w/o EA) 73.61 55.69 81.67 64.44 51.25 75.00 58.19 90.28 81.53 70.19±1 87

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

Ofﬂine TL

[Figure 100]

CSP 83.33 52.08 97.92 75.00* 56.25 67.36 72.22* 88.19 71.53 73.77 EEGNet 83.19 60.28 92.08 67.92 57.22 72.50 64.86 86.11 79.44 73.73±1 11 DAN 76.67 63.89* 94.44 70.42 59.31 75.69 63.75 84.72 80.83 74.41±1 05 JAN 81.94 63.89* 90.97 71.94 60.56 72.64 68.33 83.89 83.06 75.25±1 34

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

DANN 82.64 60.97 91.39 68.89 63.47* 79.31* 65.42 84.31 82.36 75.42±0 79

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

CDAN-E 80.14 63.33 92.36 71.11 57.92 74.03 68.33 87.78 87.36 75.82±0 66 MDD 79.31 57.64 94.44 70.42 57.92 73.33 65.97 84.03 86.25 74.37±1 50 MCC 86.81* 62.36 98.47* 73.19 58.61 72.64 66.94 94.17* 96.39* 78.84*±0 82 SHOT 81.39 61.25 93.47 64.31 60.97 75.28 65.56 85.14 86.94 74.92±0 74

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

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

[Figure 185]

[Figure 186]

[Figure 187]

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

SHOT-IM 84.44 63.33 94.31 70.83 61.67 75.28 70.42 87.64 86.81 77.19±1 41

[Figure 200]

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

Online TL

[Figure 211]

CSP 80.56 53.47 96.53 72.22 54.86 63.89 72.92 88.19 72.22 72.76 EEGNet 82.22 60.56 92.50 67.78 56.39 72.64 64.17 85.28 80.14 73.52±1 14 BN-adapt 80.83 59.72 92.78 69.44 57.64 72.08 67.08 84.86 86.39 74.54±1 70

[Figure 212]

[Figure 213]

[Figure 214]

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

[Figure 219]

[Figure 220]

[Figure 221]

[Figure 222]

[Figure 223]

[Figure 224]

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

[Figure 238]

[Figure 239]

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

Tent 78.89 58.75 92.92 69.03 57.22 72.36 67.78 85.28 86.67 74.32±1 43

[Figure 247]

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

PL 78.75 57.64 94.44 66.53 59.44 72.36 69.86 88.61 88.33 75.11±0 89 T3A 82.50 51.53 93.19 55.28 49.72 58.06 57.78 84.17 81.81 68.23±1 19

[Figure 258]

[Figure 259]

[Figure 260]

[Figure 261]

[Figure 262]

[Figure 263]

[Figure 264]

[Figure 265]

[Figure 266]

[Figure 267]

[Figure 268]

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

[Figure 275]

[Figure 276]

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

CoTTA 75.69 59.31 91.94 66.81 55.56 71.67 62.78 84.44 80.14 72.04±0 56 SAR 83.47 57.50 95.28 67.08 54.72 71.53 63.19 89.72 90.69 74.80±0 48

[Figure 281]

[Figure 282]

[Figure 283]

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

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

[Figure 302]

T-TIME 84.03 60.56 95.69 67.64 57.22 73.33 67.22 91.25 90.97 76.44±0 55 T-TIME (5) 84.93 63.54 96.88 70.83 62.78 77.22 71.81 92.22 93.47 79.30±0 82

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

[Figure 316]

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

[Figure 322]

[Figure 323]

[Figure 324]

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

TABLE III

- CROSS-SUBJECT CLASSIFICATION ACCURACIES (%) ON BNCI2014002. THE BEST ACCURACIES IN OFFLINE TL ARE MARKED WITH *. THE BEST ACCURACIES IN ONLINE TL ARE MARKED IN BOLD, AND THE SECOND BEST BY AN UNDERLINE.

[Figure 333]

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

[Figure 339]

[Figure 340]

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

[Figure 345]

[Figure 346]

[Figure 347]

[Figure 348]

[Figure 349]

Setting Approach S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 Avg. Baselines

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

[Figure 354]

[Figure 355]

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

[Figure 360]

[Figure 361]

[Figure 362]

[Figure 363]

[Figure 364]

[Figure 365]

[Figure 366]

CSP (w/o EA) 57.00 75.00 95.00 72.00 54.00 64.00 68.00 55.00 75.00 71.00 50.00 56.00 50.00 42.00 63.14 EEGNet (w/o EA) 50.00 53.00 51.60 51.60 50.80 50.00 63.20 50.80 91.60 50.00 50.00 50.00 51.00 50.00 54.54±2 31

[Figure 367]

[Figure 368]

[Figure 369]

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

[Figure 395]

[Figure 396]

[Figure 397]

[Figure 398]

[Figure 399]

CSP 62.00 82.00 98.00 76.00 79.00 70.00 84.00 67.00 94.00* 72.00 68.00 63.00 59.00 44.00 72.71 EEGNet 65.00 80.00 83.00 80.20 74.20 68.20 88.80 54.60 91.20 75.00 81.00 72.00 59.80 51.40 73.17±0 59 DAN 67.80 79.40 87.00 82.40 74.80 67.80 85.40 64.80 89.80 75.20 80.80 72.60 56.20 50.80 73.91±0 60 JAN 71.20 78.20 89.20 87.80 83.80* 67.20 84.80 69.40 86.80 75.80 81.80 74.40 53.80 54.40 75.61±1 36

[Figure 400]

[Figure 401]

[Figure 402]

[Figure 403]

[Figure 404]

[Figure 405]

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

[Figure 425]

[Figure 426]

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

[Figure 431]

[Figure 432]

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

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

[Figure 463]

DANN 68.00 80.60 89.20 72.80 77.40 63.60 87.20 61.00 87.60 75.00 82.80 73.60 59.00 56.80* 73.90±0 86

Ofﬂine TL

[Figure 464]

[Figure 465]

[Figure 466]

[Figure 467]

[Figure 468]

[Figure 469]

[Figure 470]

[Figure 471]

[Figure 472]

[Figure 473]

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

[Figure 479]

CDAN-E 74.60* 81.60 94.60 85.00 81.80 62.60 88.20 66.20 88.60 75.20 83.80 75.80 57.80 53.60 76.39±0 53 MDD 68.60 80.20 85.00 81.80 77.00 67.00 88.80 61.40 91.20 73.80 82.80 76.00 63.60* 54.40 75.11±0 31 MCC 70.80 82.80* 99.00* 94.60* 83.80* 72.60* 89.00 79.00* 89.60 79.80* 87.60* 82.80* 56.80 53.00 80.09*±0 96 SHOT 65.40 79.40 85.00 82.80 75.40 65.20 83.00 63.40 87.80 72.60 82.40 73.20 59.00 50.40 73.21±1 00

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

[Figure 498]

[Figure 499]

[Figure 500]

[Figure 501]

[Figure 502]

[Figure 503]

[Figure 504]

[Figure 505]

[Figure 506]

[Figure 507]

[Figure 508]

[Figure 509]

[Figure 510]

[Figure 511]

[Figure 512]

[Figure 513]

[Figure 514]

[Figure 515]

[Figure 516]

[Figure 517]

[Figure 518]

[Figure 519]

[Figure 520]

[Figure 521]

[Figure 522]

[Figure 523]

[Figure 524]

[Figure 525]

[Figure 526]

[Figure 527]

[Figure 528]

[Figure 529]

[Figure 530]

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

[Figure 543]

SHOT-IM 73.40 80.40 94.00 84.40 81.80 70.60 90.80* 65.60 88.00 76.00 84.20 74.40 63.60* 50.80 77.00±0 70

[Figure 544]

[Figure 545]

[Figure 546]

[Figure 547]

[Figure 548]

[Figure 549]

[Figure 550]

[Figure 551]

[Figure 552]

[Figure 553]

[Figure 554]

[Figure 555]

[Figure 556]

[Figure 557]

[Figure 558]

[Figure 559]

[Figure 560]

CSP 65.00 81.00 96.00 75.00 80.00 72.00 88.00 64.00 90.00 75.00 73.00 66.00 58.00 41.00 73.14 EEGNet 65.80 79.80 82.60 78.60 70.20 67.60 87.80 55.20 89.60 75.20 79.20 72.60 58.40 54.00 72.61±0 53 BN-adapt 67.60 77.80 83.20 84.60 72.00 68.60 84.20 61.60 88.20 74.20 80.60 68.80 56.00 55.60 73.07±0 60

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

[Figure 592]

[Figure 593]

[Figure 594]

[Figure 595]

[Figure 596]

[Figure 597]

[Figure 598]

[Figure 599]

[Figure 600]

[Figure 601]

[Figure 602]

[Figure 603]

[Figure 604]

[Figure 605]

[Figure 606]

[Figure 607]

[Figure 608]

[Figure 609]

Tent 65.20 78.60 82.80 83.60 69.20 68.20 83.40 61.20 87.00 73.20 81.40 69.20 54.80 54.20 72.29±0 74

[Figure 610]

[Figure 611]

[Figure 612]

[Figure 613]

[Figure 614]

[Figure 615]

[Figure 616]

[Figure 617]

[Figure 618]

[Figure 619]

[Figure 620]

[Figure 621]

[Figure 622]

[Figure 623]

[Figure 624]

[Figure 625]

PL 69.20 80.20 89.20 90.00 78.60 70.00 84.80 61.40 88.60 77.60 82.20 71.20 58.40 56.20 75.54±0 34 T3A 51.00 62.00 77.20 67.80 52.60 55.40 79.40 49.80 94.00 56.80 79.60 67.20 48.20 50.40 63.67±3 01

[Figure 626]

[Figure 627]

[Figure 628]

[Figure 629]

[Figure 630]

[Figure 631]

[Figure 632]

[Figure 633]

[Figure 634]

[Figure 635]

[Figure 636]

[Figure 637]

[Figure 638]

[Figure 639]

[Figure 640]

[Figure 641]

Online TL

[Figure 642]

[Figure 643]

[Figure 644]

[Figure 645]

[Figure 646]

[Figure 647]

[Figure 648]

[Figure 649]

[Figure 650]

[Figure 651]

[Figure 652]

[Figure 653]

[Figure 654]

[Figure 655]

[Figure 656]

[Figure 657]

CoTTA 65.40 76.80 83.00 79.60 72.40 67.60 87.80 59.60 87.60 74.80 77.80 71.40 56.80 52.00 72.33±0 78

[Figure 658]

[Figure 659]

[Figure 660]

[Figure 661]

[Figure 662]

[Figure 663]

[Figure 664]

[Figure 665]

[Figure 666]

[Figure 667]

[Figure 668]

[Figure 669]

[Figure 670]

[Figure 671]

[Figure 672]

[Figure 673]

SAR 70.60 80.80 93.40 91.80 84.60 74.20 89.60 66.80 86.20 78.20 84.00 76.60 55.20 53.40 77.53±0 45 T-TIME 70.00 82.60 93.60 91.80 83.60 75.20 89.40 65.60 87.00 78.80 82.80 80.80 59.80 54.60 78.26±0 50

[Figure 674]

[Figure 675]

[Figure 676]

[Figure 677]

[Figure 678]

[Figure 679]

[Figure 680]

[Figure 681]

[Figure 682]

[Figure 683]

[Figure 684]

[Figure 685]

[Figure 686]

[Figure 687]

[Figure 688]

[Figure 689]

[Figure 690]

[Figure 691]

[Figure 692]

[Figure 693]

[Figure 694]

[Figure 695]

[Figure 696]

[Figure 697]

[Figure 698]

[Figure 699]

[Figure 700]

[Figure 701]

[Figure 702]

[Figure 703]

[Figure 704]

[Figure 705]

[Figure 706]

[Figure 707]

[Figure 708]

[Figure 709]

[Figure 710]

[Figure 711]

[Figure 712]

[Figure 713]

T-TIME (5) 74.80 83.50 94.20 93.30 86.30 74.40 89.10 69.50 87.70 79.00 83.60 83.50 63.00 55.40 79.81±0 49

[Figure 714]

[Figure 715]

[Figure 716]

[Figure 717]

[Figure 718]

[Figure 719]

Parameter sensitivity analysis was also conducted to validate that a wide range of hyperparameter values in T-TIME could be used to obtain satisfactory performance. Speciﬁcally, the two main hyper-parameters, the temperature rescaling factor T and the pseudo-labeling conﬁdence threshold τ, were studied. The results are shown in Fig. 5. T ∈ {2,3,4,5} and τ ∈ [0.6,0.8] worked well on all three datasets.

G. Extension to Continual TTA

It is well-known that EEG signals are non-stationary, and EEG responses to the same stimulus vary in different sessions from even the same subject [44]. Thus, it is interesting to investigate continual TTA in unsupervised cross-subject BCIs: after the source model is adapted to the test subject’s ﬁrst session, can it be applied to following sessions from the same test subject?

Four approaches were compared in our experiments:

1) Source: a model trained in the source domain was di-

TABLE IV CROSS-SUBJECT CLASSIFICATION ACCURACIES (%) ON BNCI2015001. THE BEST ACCURACIES IN OFFLINE TL ARE MARKED WITH *. THE BEST ACCURACIES IN ONLINE TL ARE MARKED IN BOLD, AND THE SECOND BEST BY AN UNDERLINE.

[Figure 720]

[Figure 721]

[Figure 722]

[Figure 723]

[Figure 724]

[Figure 725]

[Figure 726]

[Figure 727]

[Figure 728]

[Figure 729]

[Figure 730]

[Figure 731]

[Figure 732]

[Figure 733]

[Figure 734]

Setting Approach S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 Avg. Baselines

[Figure 735]

[Figure 736]

[Figure 737]

[Figure 738]

[Figure 739]

[Figure 740]

[Figure 741]

[Figure 742]

[Figure 743]

[Figure 744]

[Figure 745]

[Figure 746]

[Figure 747]

[Figure 748]

[Figure 749]

CSP (w/o EA) 53.00 67.50 50.00 73.00 77.50 51.50 49.00 50.00 57.50 50.50 50.00 51.50 56.75 EEGNet (w/o EA) 52.80 84.00 53.00 84.80 71.70 66.00 68.50 65.70 64.00 57.90 50.60 54.90 64.49±0 94

[Figure 750]

[Figure 751]

[Figure 752]

[Figure 753]

[Figure 754]

[Figure 755]

[Figure 756]

[Figure 757]

[Figure 758]

[Figure 759]

[Figure 760]

[Figure 761]

[Figure 762]

[Figure 763]

[Figure 764]

[Figure 765]

[Figure 766]

[Figure 767]

[Figure 768]

[Figure 769]

[Figure 770]

[Figure 771]

[Figure 772]

[Figure 773]

[Figure 774]

[Figure 775]

[Figure 776]

[Figure 777]

[Figure 778]

CSP 93.50 93.50 86.50 85.00 79.00 62.00 65.00 59.00 59.50 65.00 59.50 56.50* 72.00 EEGNet 91.50 95.00 75.70 85.90 81.30 68.60 65.20 64.30 63.00 66.50 57.50 55.20 72.48±0 52 DAN 94.20 93.60 86.70 86.00 82.00 67.00 68.40 63.50 63.70 69.10 59.80 55.60 74.13±0 76 JAN 90.70 90.20 88.50 84.00 86.00 66.20 71.70 65.90 64.80 67.70 62.60 55.70 74.50±0 35

[Figure 779]

[Figure 780]

[Figure 781]

[Figure 782]

[Figure 783]

[Figure 784]

[Figure 785]

[Figure 786]

[Figure 787]

[Figure 788]

[Figure 789]

[Figure 790]

[Figure 791]

[Figure 792]

[Figure 793]

[Figure 794]

[Figure 795]

[Figure 796]

[Figure 797]

[Figure 798]

[Figure 799]

[Figure 800]

[Figure 801]

[Figure 802]

[Figure 803]

[Figure 804]

[Figure 805]

[Figure 806]

[Figure 807]

[Figure 808]

[Figure 809]

[Figure 810]

[Figure 811]

[Figure 812]

[Figure 813]

[Figure 814]

[Figure 815]

[Figure 816]

[Figure 817]

[Figure 818]

[Figure 819]

[Figure 820]

[Figure 821]

[Figure 822]

[Figure 823]

[Figure 824]

[Figure 825]

[Figure 826]

[Figure 827]

[Figure 828]

[Figure 829]

[Figure 830]

[Figure 831]

[Figure 832]

[Figure 833]

[Figure 834]

DANN 94.00 94.20 83.90 84.90 87.00 69.30 72.10 64.50 63.10 64.90 52.10 50.80 73.40±0 54

Ofﬂine TL

[Figure 835]

[Figure 836]

[Figure 837]

[Figure 838]

[Figure 839]

[Figure 840]

[Figure 841]

[Figure 842]

[Figure 843]

[Figure 844]

[Figure 845]

[Figure 846]

[Figure 847]

[Figure 848]

CDAN-E 95.20 94.50 90.70 85.70 86.90 69.20 82.90* 64.80 66.10 66.90 61.20 53.50 76.47±0 69 MDD 96.70 95.00 86.20 87.60 85.00 68.70 70.30 68.70* 64.30 67.80 62.50 55.80 75.72±1 34 MCC 97.90* 95.40* 95.00* 89.80* 94.30* 67.30 81.30 65.90 68.90* 69.50* 68.70* 52.20 78.85*±0 41 SHOT 94.10 94.20 87.90 84.70 81.80 72.20* 69.40 65.00 63.60 66.70 62.40 55.40 74.78±0 69

[Figure 849]

[Figure 850]

[Figure 851]

[Figure 852]

[Figure 853]

[Figure 854]

[Figure 855]

[Figure 856]

[Figure 857]

[Figure 858]

[Figure 859]

[Figure 860]

[Figure 861]

[Figure 862]

[Figure 863]

[Figure 864]

[Figure 865]

[Figure 866]

[Figure 867]

[Figure 868]

[Figure 869]

[Figure 870]

[Figure 871]

[Figure 872]

[Figure 873]

[Figure 874]

[Figure 875]

[Figure 876]

[Figure 877]

[Figure 878]

[Figure 879]

[Figure 880]

[Figure 881]

[Figure 882]

[Figure 883]

[Figure 884]

[Figure 885]

[Figure 886]

[Figure 887]

[Figure 888]

[Figure 889]

[Figure 890]

[Figure 891]

[Figure 892]

[Figure 893]

[Figure 894]

[Figure 895]

[Figure 896]

[Figure 897]

[Figure 898]

[Figure 899]

[Figure 900]

[Figure 901]

[Figure 902]

[Figure 903]

[Figure 904]

SHOT-IM 96.60 94.30 90.80 86.80 91.20 71.30 72.90 67.40 65.00 69.20 58.60 54.60 76.56±0 74

[Figure 905]

[Figure 906]

[Figure 907]

[Figure 908]

[Figure 909]

[Figure 910]

[Figure 911]

[Figure 912]

[Figure 913]

[Figure 914]

[Figure 915]

[Figure 916]

[Figure 917]

[Figure 918]

[Figure 919]

CSP 96.50 95.00 86.50 85.50 81.50 64.00 69.50 54.50 57.50 62.50 57.00 56.50 72.21 EEGNet 88.80 95.50 72.40 85.80 79.60 69.80 66.00 62.30 64.50 65.90 54.10 55.50 71.68±0 72 BN-adapt 96.00 94.60 90.50 84.20 82.80 71.00 69.10 62.70 62.90 66.10 61.30 54.20 74.62±0 80

[Figure 920]

[Figure 921]

[Figure 922]

[Figure 923]

[Figure 924]

[Figure 925]

[Figure 926]

[Figure 927]

[Figure 928]

[Figure 929]

[Figure 930]

[Figure 931]

[Figure 932]

[Figure 933]

[Figure 934]

[Figure 935]

[Figure 936]

[Figure 937]

[Figure 938]

[Figure 939]

[Figure 940]

[Figure 941]

[Figure 942]

[Figure 943]

[Figure 944]

[Figure 945]

[Figure 946]

[Figure 947]

[Figure 948]

[Figure 949]

[Figure 950]

[Figure 951]

[Figure 952]

[Figure 953]

[Figure 954]

[Figure 955]

[Figure 956]

[Figure 957]

[Figure 958]

[Figure 959]

[Figure 960]

[Figure 961]

[Figure 962]

[Figure 963]

Tent 95.40 92.60 89.80 81.40 77.60 65.90 67.80 60.10 58.20 62.70 59.00 54.00 72.04±0 88

[Figure 964]

[Figure 965]

[Figure 966]

[Figure 967]

[Figure 968]

[Figure 969]

[Figure 970]

[Figure 971]

[Figure 972]

[Figure 973]

[Figure 974]

[Figure 975]

[Figure 976]

[Figure 977]

PL 97.20 94.20 92.60 87.20 86.50 68.80 72.70 55.90 60.50 66.90 61.70 54.40 74.88±0 52 T3A 75.40 73.60 69.40 66.60 71.20 68.00 67.90 59.60 58.70 55.00 62.90 50.20 64.88±2 90

[Figure 978]

[Figure 979]

[Figure 980]

[Figure 981]

[Figure 982]

[Figure 983]

[Figure 984]

[Figure 985]

[Figure 986]

[Figure 987]

[Figure 988]

[Figure 989]

[Figure 990]

[Figure 991]

[Figure 992]

Online TL

[Figure 993]

[Figure 994]

[Figure 995]

[Figure 996]

[Figure 997]

[Figure 998]

[Figure 999]

[Figure 1000]

[Figure 1001]

[Figure 1002]

[Figure 1003]

[Figure 1004]

[Figure 1005]

[Figure 1006]

CoTTA 93.10 93.70 85.90 81.40 75.90 67.90 65.80 57.20 62.30 67.70 60.00 54.80 72.14±1 31 SAR 96.70 95.30 94.10 88.40 88.00 68.90 81.50 55.20 56.00 64.80 54.40 52.40 74.64±1 15

[Figure 1007]

[Figure 1008]

[Figure 1009]

[Figure 1010]

[Figure 1011]

[Figure 1012]

[Figure 1013]

[Figure 1014]

[Figure 1015]

[Figure 1016]

[Figure 1017]

[Figure 1018]

[Figure 1019]

[Figure 1020]

[Figure 1021]

[Figure 1022]

[Figure 1023]

[Figure 1024]

[Figure 1025]

[Figure 1026]

[Figure 1027]

[Figure 1028]

[Figure 1029]

[Figure 1030]

[Figure 1031]

[Figure 1032]

[Figure 1033]

[Figure 1034]

T-TIME 97.50 95.40 94.80 89.10 89.30 66.90 83.60 68.80 66.60 65.20 59.60 56.20 77.75±0 67 T-TIME (5) 97.60 94.40 94.80 88.85 90.95 67.40 85.55 68.20 65.80 67.20 60.60 57.00 78.20±0 20

[Figure 1035]

[Figure 1036]

[Figure 1037]

[Figure 1038]

[Figure 1039]

[Figure 1040]

[Figure 1041]

[Figure 1042]

[Figure 1043]

[Figure 1044]

[Figure 1045]

[Figure 1046]

[Figure 1047]

[Figure 1048]

[Figure 1049]

[Figure 1050]

[Figure 1051]

[Figure 1052]

[Figure 1053]

[Figure 1054]

[Figure 1055]

[Figure 1056]

[Figure 1057]

[Figure 1058]

[Figure 1059]

[Figure 1060]

TABLE V AVERAGE AUCS (%) ON THE THREE MI DATASETS UNDER TEST-TIME

CLASS-IMBALANCE. THE BEST AUCS ARE MARKED IN BOLD, AND THE SECOND BEST BY AN UNDERLINE.

[Figure 1061]

[Figure 1062]

[Figure 1063]

[Figure 1064]

Approach BNCI2014001 BNCI2014002 BNCI2015001 EEGNet 78.85±1 23 80.01±1 05 81.26±0 32

[Figure 1065]

[Figure 1066]

[Figure 1067]

[Figure 1068]

[Figure 1069]

[Figure 1070]

[Figure 1071]

MCC 72.94±2 44 77.32±2 34 78.40±1 70 SHOT-IM 74.84±1 00 78.48±0 92 78.60±0 89 BN-adapt 79.14±1 35 79.86±0 80 80.84±1 01

[Figure 1072]

[Figure 1073]

[Figure 1074]

[Figure 1075]

[Figure 1076]

[Figure 1077]

[Figure 1078]

[Figure 1079]

[Figure 1080]

PL 79.93±1 05 82.24±1 50 83.08±1 24

[Figure 1081]

[Figure 1082]

[Figure 1083]

SAR 79.13±0 77 83.44±1 72 82.27±0 49 ISFDA (IM) 79.58±0 79 83.38±0 99 82.75±0 44 DELTA (IM) 79.66±1 00 83.38±0 94 82.89±0 48

[Figure 1084]

[Figure 1085]

[Figure 1086]

[Figure 1087]

[Figure 1088]

[Figure 1089]

[Figure 1090]

[Figure 1091]

[Figure 1092]

T-TIME 81.65±1 39 85.28±1 04 84.02±1 17 T-TIME (5) 82.72±1 27 86.01±0 79 84.68±0 52

[Figure 1093]

[Figure 1094]

[Figure 1095]

[Figure 1096]

[Figure 1097]

[Figure 1098]

[Figure 1099]

adapted to the ﬁrst session in the target domain, and then further adapted to and tested on the second session of the target domain.

The results are given in Table VII, which shows that:

TABLE VII CLASSIFICATION ACCURACIES (%) ON THE SECOND SESSION OF THE THREE MI DATASETS.

[Figure 1100]

[Figure 1101]

[Figure 1102]

[Figure 1103]

Approach BNCI2014001 BNCI2014002 BNCI2015001 Source 73.78±1 85 74.24±1 26 72.52±0 98

[Figure 1104]

[Figure 1105]

[Figure 1106]

[Figure 1107]

- TTA1 75.21±1 01 80.93±1 15 76.85±0 54

[Figure 1108]

[Figure 1109]

[Figure 1110]

[Figure 1111]

- TTA2 77.41±1 23 77.67±0 51 77.19±0 47

[Figure 1112]

[Figure 1113]

[Figure 1114]

[Figure 1115]

[Figure 1116]

[Figure 1117]

[Figure 1118]

TTA1+2 77.08±0 85 81.60±0 92 77.60±0 49

[Figure 1119]

[Figure 1120]

TABLE VI ABLATION STUDY RESULTS (%). THE BEST ACCURACIES ARE MARKED IN BOLD. Strategy

[Figure 1121]

[Figure 1122]

BNCI2014001 BNCI2014002 BNCI2015001 Avg. CEM MDR TR

[Figure 1123]

[Figure 1124]

[Figure 1125]

[Figure 1126]

[Figure 1127]

[Figure 1128]

[Figure 1129]

[Figure 1130]

× × × 73.52±1 14 72.61±0 53 71.68±0 72 72.60

[Figure 1131]

[Figure 1132]

[Figure 1133]

× × 73.90±0 95 76.44±0 71 75.25±1 21 75.20 × × 73.72±0 79 74.19±0 56 74.68±1 01 74.20 × × / / / / × 73.72±0 91 74.18±0 38 74.19±0 89 74.03

[Figure 1134]

[Figure 1135]

[Figure 1136]

[Figure 1137]

[Figure 1138]

[Figure 1139]

[Figure 1140]

[Figure 1141]

[Figure 1142]

[Figure 1143]

[Figure 1144]

[Figure 1145]

× 74.44±0 77 77.16±0 51 74.84±1 26 75.48 × 76.17±1 18 77.43±0 25 77.27±1 47 76.96 76.44±0 55 78.26±0 50 77.75±0 67 77.48

[Figure 1146]

[Figure 1147]

[Figure 1148]

[Figure 1149]

[Figure 1150]

[Figure 1151]

[Figure 1152]

rectly tested on the second session in the target domain.

- 2) TTA1: a model trained in the source domain was adapted to the ﬁrst session in the target domain, and then tested directly on the second session of the target domain.
- 3) TTA2: a model trained in the source domain was adapted to and tested on the second session in the target domain.
- 4) TTA1+2: a model trained in the source domain was

- 1) TTA1 outperformed Source, indicating that the two sessions from the same target subject indeed had some similarity, thus knowledge learned from the ﬁrst session helped classify the second session.
- 2) TTA2 outperformed Source, which is intuitive and consistent with the observations in previous subsections.
- 3) TTA1+2 generally achieved the best performance, suggesting the necessity to always adapt to the new session, and it is beneﬁcial to make use of more history data from the same subject.

H. Computational Cost

The computation time of T-TIME on an Intel Core i5 CPU was recorded. Pre-inference target label prediction consists of IEA and SML, which took about 5.3 ms and 0.3 ms on average, respectively. Post-inference target model update took about 34/61/55 ms on average (worst case 63/89/87 ms) for a single EEGNet model on the three datasets. The model update can be carried out in the background until the next test trial

[Figure 1153]

- (a)

[Figure 1154]

- (b)

- Fig. 4. Performance of different ensemble strategies on BNCI2014001 as the number of EEGNet base models varies. (a) binary classiﬁcation (left/right hand); and, (b) 4-class classiﬁcation.

ﬁnishes (which usually take seconds) and queries for model inference again, as illustrated in Fig. 6. The speciﬁc number of models in the ensemble can vary based on the between-trial time of the speciﬁc BCI application. Therefore, T-TIME can cope well with real-world BCI applications.

V. CONCLUSIONS

This paper has proposed T-TIME for unsupervised and online TTA to a new BCI user, making plug-and-play EEGbased BCIs possible. T-TIME initializes multiple classiﬁers from the aligned source data. When an unlabeled test EEG trial arrives, T-TIME ﬁrst predicts its labels using spectral metalearner, and then updates each classiﬁer by conditional entropy minimization and adaptive marginal distribution regularization. Extensive experiments on three public MI-based BCI datasets demonstrated that T-TIME outperformed about 20 classical and state-of-the-art TL approaches. To our knowledge, this is the ﬁrst study on TTA for calibration-free EEG-based BCIs.

The following directions will be considered in our future research:

[Figure 1155]

- (a)

[Figure 1156]

- (b)

- Fig. 5. Performance of T-TIME w.r.t. different hyperparameter values. (a) Temperature scaling factor T; and, (b) pseudo-labeling conﬁdence threshold τ.

| |
|---|

| |
|---|

- Fig. 6. Two portions of computation time of T-TIME. The computation time of model inference is the prediction delay, whereas model update can be performed before the next complete test arrives, which usually take seconds.

- 1) We have only considered MI-based BCIs. It is interesting to study whether other BCI paradigms, e.g., eventrelated potentials and affective BCIs, are also applicable.
- 2) This paper assumes the source subject is willing to provide his/her classiﬁer to the target subject. For privacy protection, the source subject may encapsulate his/her model as an API, instead of sharing all the details. Privacy-preserving TTA needs to be investigated.
- 3) In real-world applications of MI-based BCIs, the classiﬁer may not explicitly know the start and end time of each MI trial. How to perform TTA in this challenging situation is another interesting research problem.

REFERENCES

- [1] B. Graimann, B. Allison, and G. Pfurtscheller, “Brain-computer interfaces: A gentle introduction,” Brain-Computer Interfaces, pp. 1–27, 2009.
- [2] M. O. Krucoff, S. Rahimpour, M. W. Slutzky, V. R. Edgerton, and D. A. Turner, “Enhancing nervous system recovery through neurobiologics, neural interface training, and neurorehabilitation,” Frontiers in Neuroscience, vol. 10, p. 584, 2016.
- [3] J. van Erp, F. Lotte, and M. Tangermann, “Brain-computer interfaces: Beyond medical applications,” Computer, vol. 45, no. 4, pp. 26–34, 2012.
- [4] D. Wu, Y. Xu, and B.-L. Lu, “Transfer learning for EEG-based brain–computer interfaces: A review of progress made since 2016,” IEEE Trans. Cognitive and Developmental Systems, vol. 14, no. 1, pp. 4–19, 2022.
- [5] S. Sutton, M. Braren, J. Zubin, and E. John, “Evoked-potential correlates of stimulus uncertainty,” Science, vol. 150, no. 3700, pp. 1187–1188, 1965.
- [6] O. Friman, I. Volosyak, and A. Graser, “Multiple channel detection of steady-state visual evoked potentials for brain-computer interfaces,” IEEE Trans. Biomedical Engineering, vol. 54, no. 4, pp. 742–750, 2007.
- [7] G. Pfurtscheller and C. Neuper, “Motor imagery and direct braincomputer communication,” Proc. IEEE, vol. 89, no. 7, pp. 1123–1134, 2001.
- [8] D. Wu, X. Jiang, and R. Peng, “Transfer learning for motor imagery based brain-computer interfaces: A tutorial,” Neural Networks, vol. 153, pp. 235–253, 2022.
- [9] G. Wilson and D. J. Cook, “A survey of unsupervised deep domain adaptation,” ACM Trans. Intelligent Systems and Technology, vol. 11, no. 5, pp. 1–46, 2020.
- [10] B. Sun, J. Feng, and K. Saenko, “Return of frustratingly easy domain adaptation,” in Proc. AAAI Conf. Artiﬁcial Intelligence, Phoenix, AZ, Feb. 2016, pp. 2058–2065.
- [11] P. Zanini, M. Congedo, C. Jutten, S. Said, and Y. Berthoumieu, “Transfer learning: A Riemannian geometry framework with applications to brain–computer interfaces,” IEEE Trans. Biomedical Engineering, vol. 65, no. 5, pp. 1107–1116, 2018.
- [12] H. He and D. Wu, “Transfer learning for brain-computer interfaces: A Euclidean space data alignment approach,” IEEE Trans. Biomedical Engineering, vol. 67, no. 2, pp. 399–410, 2020.
- [13] M. Long, Y. Cao, J. Wang, and M. I. Jordan, “Learning transferable features with deep adaptation networks,” in Proc. Int’l Conf. Machine Learning, Lille, France, Jul. 2015, pp. 97–105.
- [14] M. Long, H. Zhu, J. Wang, and M. I. Jordan, “Deep transfer learning with joint adaptation networks,” in Proc. Int’l Conf. Machine Learning, Sydney, Australia, Aug. 2017, pp. 2208–2217.
- [15] Y. Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle, F. Laviolette, M. Marchand, and V. Lempitsky, “Domain-adversarial training of neural networks,” Journal of Machine Learning Research, vol. 17, no. 1, pp. 2096–2030, 2016.
- [16] M. Long, Z. Cao, J. Wang, and M. I. Jordan, “Conditional adversarial domain adaptation,” in Proc. Advances Neural Information Processing Systems, Montreal, Canada, Dec. 2018, pp. 1640–1650.
- [17] Y. Jin, X. Wang, M. Long, and J. Wang, “Minimum class confusion for versatile domain adaptation,” in Proc. European Conf. Computer Vision, Glasgow, UK, Aug. 2020, pp. 464–480.
- [18] J. Liang, D. Hu, and J. Feng, “Domain adaptation with auxiliary target domain-oriented classiﬁer,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, Nashville, TN, Jun. 2021, pp. 16 632–16 642.

- [19] Y. Fang, P.-T. Yap, W. Lin, H. Zhu, and M. Liu, “Source-free unsupervised domain adaptation: A survey,” arXiv preprint arXiv:2301.00265, 2022.
- [20] J. Liang, D. Hu, Y. Wang, R. He, and J. Feng, “Source data-absent unsupervised domain adaptation through hypothesis transfer and labeling transfer,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 44, no. 11, pp. 8602–8617, 2022.
- [21] X. Li, J. Li, L. Zhu, G. Wang, and Z. Huang, “Imbalanced source-free domain adaptation,” in Proc. ACM Int’l Conf. Multimedia, Chengdu, China, Oct. 2021, pp. 3330–3339.
- [22] K. Xia, W. Duch, Y. Sun, K. Xu, W. Fang, H. Luo, Y. Zhang, D. Sang, X. Xu, F.-Y. Wang, and D. Wu, “Privacy-preserving brain–computer interfaces: A systematic review,” IEEE Trans. Computational Social Systems, early access, 2022.
- [23] S. Li, H. Wu, L. Ding, and D. Wu, “Meta-learning for fast and privacy-preserving source knowledge transfer of EEG-based BCIs,” IEEE Computational Intelligence Magazine, vol. 17, no. 4, pp. 16–26, 2022.
- [24] W. Zhang and D. Wu, “Lightweight source-free transfer for privacypreserving motor imagery classiﬁcation,” IEEE Trans. Cognitive and Developmental Systems, early access, 2022.
- [25] W. Zhang, Z. Wang, and D. Wu, “Multi-source decentralized transfer for privacy-preserving BCIs,” IEEE Trans. Neural Systems and Rehabilitation Engineering, vol. 30, pp. 2710–2720, 2022.
- [26] J. Liang, R. He, and T. Tan, “A comprehensive survey on test-time adaptation under distribution shifts,” arXiv preprint arXiv:2303.15361, 2023.
- [27] D.-H. Lee, “Pseudo-label: The simple and efﬁcient semi-supervised learning method for deep neural networks,” in Proc. Int’l Conf. Machine Learning Workshops, Atlanta, GA, Jun. 2013, pp. 1322–1333.
- [28] D. Chen, D. Wang, T. Darrell, and S. Ebrahimi, “Contrastive test-time adaptation,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, New Orleans, LA, Jun. 2022, pp. 295–305.
- [29] Y. Iwasawa and Y. Matsuo, “Test-time classiﬁer adjustment module for model-agnostic domain generalization,” in Proc. Advances Neural Information Processing Systems, Virtual, Dec. 2021, pp. 2427–2440.
- [30] D. Wang, E. Shelhamer, S. Liu, B. Olshausen, and T. Darrell, “Tent: Fully test-time adaptation by entropy minimization,” in Proc. Int’l Conf. Learning Representations, Vienna, Austria, May. 2021.
- [31] M. M. Zhang, S. Levine, and C. Finn, “MEMO: Test time robustness via adaptation and augmentation,” in Proc. Advances Neural Information Processing Systems, New Orleans, LA, Nov. 2022, pp. 38 629–38 642.
- [32] S. Niu, J. Wu, Y. Zhang, Z. Wen, Y. Chen, P. Zhao, and M. Tan, “Towards stable test-time adaptation in dynamic wild world,” in Proc. Int’l Conf. Learning Representations, Kigali, Rwanda, May. 2023.
- [33] B. Zhao, C. Chen, and S.-T. Xia, “DELTA: degradation-free fully testtime adaptation,” in Proc. Int’l Conf. Learning Representations, Kigali, Rwanda, May. 2023.
- [34] Q. Wang, O. Fink, L. Van Gool, and D. Dai, “Continual test-time domain adaptation,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, New Orleans, LA, Jun. 2022, pp. 7201–7211.
- [35] M. De Lange and T. Tuytelaars, “Continual prototype evolution: Learning online from non-stationary data streams,” in Proc. IEEE/CVF Int’l Conf. Computer Vision, Montreal, Canada, Oct. 2021, pp. 8250–8259.
- [36] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: A compact convolutional neural network for EEG-based brain-computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018.
- [37] F. Parisi, F. Strino, B. Nadler, and Y. Kluger, “Ranking and combining multiple predictors without labeled data,” Proc. National Academy of Sciences, vol. 111, no. 4, pp. 1253–1258, 2014.
- [38] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, “On calibration of modern neural networks,” in Proc. Int’l Conf. Machine Learning, Sydney, Australia, Aug. 2017, pp. 1321–1330.
- [39] M. Boudiaf, R. Mueller, I. Ben Ayed, and L. Bertinetto, “Parameter-free online test-time adaptation,” in Proc. IEEE/CVF Conf. Computer Vision and Pattern Recognition, New Orleans, LA, Jun. 2022, pp. 8344–8353.
- [40] V. Jayaram and A. Barachant, “MOABB: trustworthy algorithm benchmarking for BCIs,” Journal of Neural Engineering, vol. 15, no. 6, p. 066011, 2018.
- [41] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K.-r. Muller, “Optimizing spatial ﬁlters for robust EEG single-trial analysis,” IEEE Signal Processing Magazine, vol. 25, no. 1, pp. 41–56, 2008.
- [42] Y. Zhang, T. Liu, M. Long, and M. Jordan, “Bridging theory and algorithm for domain adaptation,” in Proc. Int’l Conf. Machine Learning, Long Beach, CA, Jun. 2019, pp. 7404–7413.

- [43] S. Schneider, E. Rusak, L. Eck, O. Bringmann, W. Brendel, and M. Bethge, “Improving robustness against common corruptions by covariate shift adaptation,” in Proc. Advances Neural Information Processing Systems, Vancouver, Canada, Dec. 2020, pp. 11 539–11 551.
- [44] S. R. Liyanage, C. Guan, H. Zhang, K. K. Ang, J. Xu, and T. H. Lee, “Dynamically weighted ensemble classiﬁcation for non-stationary EEG processing,” Journal of Neural Engineering, vol. 10, no. 3, p. 036007, 2013.

