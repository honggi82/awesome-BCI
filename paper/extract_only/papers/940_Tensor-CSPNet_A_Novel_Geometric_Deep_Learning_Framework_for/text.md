# Tensor-CSPNet: A Novel Geometric Deep Learning Framework for Motor Imagery Classiﬁcation

Ce Ju and Cuntai Guan Fellow, IEEE

arXiv:2202.02472v3[eess.SP]23Sep2022

Abstract—Deep learning (DL) has been widely investigated in a vast majority of applications in electroencephalography (EEG)based brain-computer interfaces (BCIs), especially for motor imagery (MI) classiﬁcation in the past ﬁve years. The mainstream DL methodology for the MI-EEG classiﬁcation exploits the temporospatial patterns of EEG signals using convolutional neural networks (CNNs), which have remarkably succeeded in visual images. However, since the statistical characteristics of visual images depart radically from EEG signals, a natural question arises whether an alternative network architecture exists apart from CNNs. To address this question, we propose a novel geometric deep learning (GDL) framework called Tensor-CSPNet, which characterizes spatial covariance matrices derived from EEG signals on symmetric positive deﬁnite (SPD) manifolds and fully captures the temporospatiofrequency patterns using existing deep neural networks on SPD manifolds, integrating with experiences from many successful MI-EEG classiﬁers to optimize the framework. In the experiments, Tensor-CSPNet attains or slightly outperforms the current state-of-the-art performance on the cross-validation and holdout scenarios in two commonlyused MI-EEG datasets. Moreover, the visualization and interpretability analyses also exhibit the validity of Tensor-CSPNet for the MI-EEG classiﬁcation. To conclude, in this study, we provide a feasible answer to the question by generalizing the DL methodologies on SPD manifolds, which indicates the start of a speciﬁc GDL methodology for the MI-EEG classiﬁcation.

Index Terms—Symmetric Positive Deﬁnite Manifolds, Geometric Deep Learning, Electroencephalography-based BCIs, Motor Imagery Classiﬁcation

I. INTRODUCTION

- A brain-computer interface (BCI) is a direct communication

pathway between a user’s brain and an external device by measuring and analyzing the behaviorally relevant information of brain activities. [1] The non-invasive electroencephalogram (EEG)-based BCI is one of the most common BCIs, employing portable, non-invasive electrodes on the scalp for instantaneously measuring electrical changes in neurons. It allows brain-derived communication between patients with amyotrophic lateral sclerosis and motor control restoration after stroking and spinal cord injury. [2] However, decoding mental states from EEG-based BCI is challenging for various reasons, such as low signal-to-noise ratio (SNR), artifacts, and high inter/intra-subject variabilities (a.k.a, nonstationarity changes) in EEG signals. [3]

In the paradigm of traditional EEG analysis, spatial patterns of EEG signals are crafted by a preprocessing algorithm to have more strong discrimination between mental states and afterward classiﬁed using machine-learning classiﬁers, such

Ce Ju and Cuntai Guan are with the S-Lab, Nanyang Technological University, 50 Nanyang Avenue, Singapore (emails: {juce0001,ctguan}@ntu.edu.sg).

as the support vector machine (SVM) and linear discriminant analysis (LDA). [4] Many spatial ﬁlterings such as common spatial pattern (CSP) and its variants [5]–[8] are widely used as such preprocessing algorithms to increase the SNR of signals and, therefore, enhance oscillatory brain electrical activities before feature extraction. However, the validness of the analysis is limited to the capacity of feature extraction for complex event-related and event-unrelated (resting state) neural oscillations. [9]

To remedy this limitation, the architecture of CNNs has been broadly adopted as an emerging tool in BCIs [9]–[14]. Technically, the scheme of these CNN classiﬁers is designed to automatically capture the temporospatiofrequency features of neural signals in end-to-end learning without the experience of human engineers. It has been proven effective for the MI-EEG classiﬁcation in literature [4], [13]. Compared with the previous non-DL approaches, CNN is making signiﬁcant advances in the incredible power of representation with multiple levels of abstraction, end-to-end learning, and causal contributions of patterns on brain topography. [10] However, the essential difference in the underlying structure between images and EEG signals discernibly weakens the feature expression of CNNs in BCI tasks. Speciﬁcally, several prior assumptions in computer vision require the underlying structure of visual images to be stationary, translation invariant, translation equivariant, and stable with respect to local deformations, conceptually characterized as the Euclidean nature, which enables CNNs to effectively extract local features from local statistics. [15]–[17] In contrast, the underlying structure of EEG signals might not embody the Euclidean nature according to electrophysiological studies and (nonlinear) dynamical neuroscience [18], [19]. To illustrate, a prominent example is that EEG signals are nonstationary, and their local statistics are variant to the location of spatially distributed regions. Consequently, a natural question arises whether an alternative network architecture exists apart from CNNs for efﬁcient feature extraction in the MI-EEG classiﬁcation.

In the history of the MI-EEG classiﬁcation study, such an alternative discipline has been raised, which uses a graph convolutional neural network to learn the graph signal representations of EEG rhythmic components [20]. Apart from their approach, in this study, we set off a novel discipline in terms of spatial covariance matrice (SCM) derived from EEG signals, which is the inherent correlation between neighbor channels, a second statistics in the spatial domain, and have been developed in CSP for over 30 years [5], [21]. We aim to formulate SCMs using Riemannian geometry for an in-depth analysis of the non-Euclidean nature as many existing Riemannian geometry-based modelings in engineering disciplines such as

[Figure 1]

[Figure 2]

[Figure 3]

©2022 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works. DOI: 10.1109/TNNLS.2022.3172108

[Figure 4]

diffusion tensor imaging and geometric mechanics [22]–[24]. The Riemannian-based BCI classiﬁer that characterizes EEG signals using the geometric information of SCMs emerged about a decade ago. [25]–[27] It has gained growing interest from the BCI community, and various follow-ups were proposed to optimize the structure [28]–[30]. Technically, SCMs derived from EEG signals are inherently symmetric positive deﬁnite (SPD). The space of SPD matrices is formulated as a Riemannian manifold called the SPD manifold, provided with a speciﬁc metric. Then, the geodesic distance on SPD manifolds between two SCMs is encoded as a high-level feature for the machine-learning classiﬁer.

The most fruitful part of the Riemannian-based BCI classiﬁer is the conceptual importance of using SPD manifolds to characterize EEG signals. However, there are many practical drawbacks to the Riemannian-based BCI classiﬁer. Firstly, hand-crafted feature extraction is outdated and inefﬁcient in complex scenarios such as feature expression for nonhomogeneous BCI sensor data. Secondly, the neurophysiological interpretation of existing hand-crafted features such as geodesic distance on SPD manifolds has not yet been fully understood [31]. To cope with these practical drawbacks, more recently, a novel classiﬁer on SPD manifolds [32] is probably a promising solution, which investigates the low-level features of SCMs for the EEG classiﬁcation using SPDNet [33], an existing Riemannian-based network architecture, to capture the spatial patterns of EEG rhythmic components. Architecture SPDNet is a DL architecture that preserves the SPD structure of matrices across layers and exhibits competitive performance compared with the current state-of-the-art approaches using CNNs on an increasing number of computer vision tasks. [34], [35] Its perspective generally originates from an emerging subﬁeld geometric deep learning (GDL) [17], which aims to generalize the DL models to the non-Euclidean domain as graphs and manifolds.

In this paper, we propose a novel GDL framework, TensorCSPNet, that generalizes the DL methodology for the MI-EEG classiﬁcation. To this end, we build a network architecture upon the principle that largely exploits the temporospatiofrequency patterns of EEG signals. Each structure in our architecture aims to capture features from either of the temporospatiofrequency domains. Firstly, tensor stacking segments EEG signals and stacks them into the temporospatiofrequency tensors according to hand-crafted technical and neurological experience. Each tensor is in an SPD-matrix representation that encodes the inherent correlation between neighbor channels with respect to the time and frequency information, which is also a rough estimation of the brain connectivity between spatially segregated areas [36]. Secondly, the spatial patterns and temporal dynamics behind EEG signals are extracted by deep neural networks on SPD manifolds and CNNs on the tangent space sequentially and respectively. Signiﬁcantly, the combination of the depthwise BiMap layer and ReEig consists of a nonlinear spatial ﬁlter that enhances the feature expression of spatial patterns. Finally, the classiﬁcation stage classiﬁes the extracted temporospatiofrequency patterns using fully-connected neural networks.

In the experiments, Tensor-CSPNet is investigated on sev-

eral motor imagery (MI) tasks of EEG-based BCIs, including stationary and non-stationary scenarios. Typically, an MI task refers to an experiment where the individual mentally simulates a physical action. In neurophysiology, since MI of motor actions produces replicable and discriminable patterns (i.e., synchronization/desynchronization) over the primary sensory and motor areas, the signals are discernible to be a classiﬁcation task. [37], [38] In addition, the visualization and interpretability analyses are conducted on two MI datasets to double verify the validity of Tensor-CSPNet.

The remainder of this paper is organized as follows: Section II introduces the paradigm of traditional EEG analysis and elaborates on the mathematical background of CSP and SPDNet. The subsequent section III is the methodology for Tensor-CSPNet. The performance of Tensor-CSPNet is then compared on a broad set of experiments in Section IV, and cautious discussions of nonstationarity and contrasts with other mainstreams are in Section V. In Appendix, we discuss the prior assumptions for CNNs, a brief overview of SPD manifolds, the strategy of ﬁxed-interval segmentation, and an ablation study on BCIC-IV-2a.

II. PRELIMINARY

- A. Notations Let Sn := { S ∈ Rn×n : S = S⊤ } be a set of n × n real

symmetric matrices and S++n := S ∈ Sn : x⊤Sx > 0,∀x ∈ Rn/{0} be a set of n×n real SPD matrices. The Frobenius inner product and norm on m × n matrices A and B are deﬁned as A,B F := Tr(A⊤B) and ||A||2F := A,A F respectively.

- B. Paradigm of Traditional EEG Analysis

Let X ∈ RC×T be a short segment (trail) of EEG signals, where C is the number of EEG channels (electrodes), and T is the number of sampled points on epoch durations. This paper assumes that trail X is already band-pass ﬁltered, centered, and scaled. A linear classiﬁer that predicts the label of trail X is typically written as f(X;{wi}Ni=1,{βi}Ni=1) =

N i=1 βi log (wiXX⊤wi⊤)+β0, where N is the number of spatial ﬁlters, {wi}Ni=1 ∈ RC are spatial ﬁlters and {βi}Ni=1 ∈ R are biases. At many physiological and anatomical levels in the brain, the lognormal distributions are fundamental to structural and functional brain organization because the distribution of numerous parameters is strongly skewed with a heavy tail. [39] Hence, the logarithm of the power/variance of the projected signal wiXX⊤wi⊤ is considered in the classiﬁer.

- C. Common Spatial Pattern Let Σ+,Σ− ∈ RC×C be the estimates of covariance

matrices of trails {Xi}i=1 in a 2-class MI -EEG paradigm, i.e., Σc = |I1

Xc ·Xc⊤, where Ic (c ∈ {+,−}) is the set of indices of trails of one class. The CSP algorithm is given by a simultaneous diagonalization of covariance matrices Σ+ and Σ− in two equations such as W · Σ+ · W⊤ = Λ+ and W · Σ− · W⊤ = Λ−, where each column vector wi ∈ col(W) is a spatial ﬁlter in CSP. The diagonal matrices Λ+,Λ− ∈

c| · i∈I

[Figure 5]

c

[Figure 6]

[Figure 7]

3

[Figure 8]

Fig. 1: Illustration of Architecture of Tensor-CSPNet: The network architecture is built upon the principle that fully exploits the temporospatiofrequency patterns behind EEG signals. Hence, each structure in the architecture aims to capture features from either of the temporospatiofrequency domains. In Line 1, EEG signals are segmented into the temporospatiofrequency tensors in the tensor stacking stage. Frequency information has been unfolded in this stage. In Line 2, the CSP stage is designed to capture spatial information from tensors using the depthwise BiMap layer, Riemannian BN layer, and the ReEig layer. In Line 3, we capture the temporal information on the tangent space using 2D CNNs. Fully connected neural networks with cross-entropy loss are used for the MI-EEG classiﬁcation.

RC×C hold an identity constraint, i.e., Λ+ + Λ− = I. The problem of the above simultaneous diagonalization is mathematically equivalent to solve a generalized eigenvalue problem as follows: (Σ+w) = λ · (Σ−w). Feature vectors z := log (wXX⊤w⊤) consisting of eigenvectors w ∈ col(W) from both ends of the eigenvalue spectrum are commonly used in the EEG analysis.

- • BiMap: This layer transforms the covariance matrix S using the bi-map operator W · S · WT. Transformation matrix W is required to be full row rank.
- • ReEig: This layer is analogous to ReEig in classical deep neural networks that introduces the non-linearity on SPD manifolds using U·max(ǫI,Σ)·UT, where singular value decomposition S = U · Σ · UT, and ǫ is a rectiﬁcation threshold and I is an identity matrix.
- • LOG: This layer is to map elements on SPD manifolds on its tangent space using U ·log (Σ)·UT, where singular value decomposition S = U · Σ · UT.

- D. Riemannian Batch Normalization

Riemannian Batch Normalization (BN) is a generalization of the classic batch normalization on Riemannian manifolds. [40]. Formally, the weighted Riemannian barycenter on SPD manifolds Barw({B}) utilizes the parallel transport Γ to connect any sample Si with the identity matrix Id according to formulas ΓB →I

d

(Si) := B− ΓI

- 1

[Figure 9]

- 2 · Si · B−

- 1

[Figure 10]

- 2 and

d →G(Si) := G12 ·Si ·G12 , where each mini batch B of SPD matrices {Si}i=1, the biasing parameter of G acquired by the matrix backpropagation in the training is directly applied in the inference. The deﬁnition of the parallel transport and the weighted Riemannian barycenter refers to Appendix B.

[Figure 11]

[Figure 12]

- E. SPDNet

III. METHODOLOGY

In this section, we propose a novel GDL framework TensorCSPNet for non-invasive EEG-based BCIs, consisting of four stages: the tensor stacking stage, the common spatial pattern stage, the temporal convolutional stage, and the classiﬁcation stage. The architecture of Tensor-CSPNet is illustrated in Figure 1.

A. Stage One: Tensor Stacking Stage

In the ﬁrst stage, EEG signals will be segmented into the temporospatiofrequency tensors concerning the theory of neurophysiology, electrophysiology, and signal processing.

Architecture SPDNet is a deep neural network architecture fed with SPD matrices that preserves the SPD structure of matrices across layers during non-linearly learning. [33] Analogous to convolutional neural networks, the basic layers in SPDNet are designed to include the following layers:

1) frequency Segmentation: We use a well-known ﬁlterbank technique in the EEG-BCI classiﬁcation [6] for frequency segmentation, which employs a bank of bandpass ﬁlters to

decompose the raw oscillatory EEG signals into multiple frequency passbands using the causal Chebyshev Type II ﬁlter.

2) Riemannian BN: Riemannian BN is used to de-correlate a batch of sample-based spatial covariance matrix estimation towards to an identity by ΓB →I

(Sij) := B−21 · Sij · B−21 , which equalizes the variance in all directions and removes the batch effects. The behind statistical mechanism has been exhibited in CSP’s variant, Regularized-CSP [8], in which a shrinkage is performed towards the identity on the regularized estimate for each class as S¯ij := (1 − γ) · S¯ij + γ · Id, where S¯ij is the regularized estimate of Sij, γ is a user-deﬁned parameter.

- 2) Temporal Segmentation: The temporal segmentation aims to divide EEG signals into small segments on the time domain with or without overlapping. Generally, the signals should be segmented according to the characteristics of EEGbased BCI tasks, for instance, dynamic changes in very short durations in many cognitive tasks. For those signals that we are not familiar with their characteristics, we propose a ﬁxed-interval segmentation strategy in Appdendix C that EEG signals are initially subdivided into ﬁxed short equal-length intervals without overlapping. We require that the length of the time window ω (time resolution) is limited by Garbor’s uncertainty principle [41] that time and frequency resolutions cannot be at a high level simultaneously.
- 3) Tensor Stacking: After two segmentations, we stack elementary information cells to the four-dimensional temporospatiofrequency tensors X˜ ∈ RW×F×C×ω, where W, F, C and ω are the number of window slices, the number of ﬁlter banks, the number of channels and window length respectively. As a consequence, the input tensors of Tensor-CSPNet are spatial covariance matrices Sij := X˜[i,j,:,:]·X˜[i,j,:,:]⊤ for i ∈ windows slices W and j ∈ ﬁlter banks F. The pseudocode of tensor stacking refers to Algorithm 1.

[Figure 13]

[Figure 14]

d

- 3) ReEig: ReEig in SPDNet is used to consist of a nonlinear

spatial ﬁlter. In contrast with the traditional EEG analysis in which spatial ﬁlters are linear, this layer enables TensorCSPNet to have a richer feature expression of spatial information.

- 4) LOG: LOG in SPDNet is adopted to log-project the

transformed SPD matrices onto the tangent space for the logpower/variance. It is consistent with a step in the standard paradigm of EEG analysis, refer to Section II-B.

C. Stage Three: Temporal Convolutional Stage

In this stage, we aim to capture temporal dynamics on tangent space using CNNs. We ﬁrst ﬂatten the outputs of the CSP stage on the frequency and space domains called the Spatial-frequency Flattening. Then, we concatenate the ﬂattened tensors along the time domain called the Temporal Concatenation. After the spatial-frequency ﬂattening and the temporal concatenation, the temporospatiofrequency tensor becomes a 2-dimensional tensor in RW×(Fo

[Figure 15]

Algorithm 1: Tensor Stacking Stage Input : X ∈ RF×C×T, window length ω, stride s,

[Figure 16]

and padding value p) Output: X˜ ∈ R⌊

T +2p−1

s +1⌋×F×C×ω. for i ← 0 to⌊T+2sp−1 + 1⌋ do

[Figure 17]

2) without SPD structure anymore, where F is the number of ﬁlter banks and o is the output dimension of the CSP stage, as illustrated in Figure 2. Finally, we use 2-dimensional (2D) CNN with po2width (p = 1 or F) and q-height (1 ≤ q ≤ W) to capture the temporal dynamics of EEG signals.

[Figure 18]

[Figure 19]

for j ← 0 to F do

X˜[i,j,:,:] ← X[j,:,is : is + ω] end

[Figure 20]

end

[Figure 21]

Remark. 1). The tensor stacking stage is a data preprocessing stage, which is not included in the network architecture.

Space-Frequancy Domain

F

2). In frequency segmentation, we adopt a widely used portfolio of ﬁlter banks {4 ∼ 8 Hz, 8 ∼ 12 Hz, ···, 36 ∼ 40 Hz}, which has exhibited the best competition results in the BCI Competition IV 2a 1 It is a well-known and widely used dataset in the MI-EEG classiﬁers. There are also many pieces of literature to exploit different combinations of frequency ranges, but this one is the most straightforward.

| | | | | | | | |
|---|---|---|---|---|---|---|---|

| | | | |
|---|---|---|---|

…

TimeDomain

1 × o2 1 × o2 1 × o2

. . .

W

| | | | | | | | |
|---|---|---|---|---|---|---|---|

| | | | |
|---|---|---|---|

…

1 × o2 1 × o2 1 × o2

Fig. 2: Illustration of Temporal Convolutional Stage: F blocks of 1 × o2 rectangles ﬂattened and W lines concatenated. To illustrate, in the case of 5-CSPNet employed on MI-KU, F = 9, o = 20, and W = 5. Thus, each line is a 1 × 3600 ﬂattened tensor, and the shape of the whole rectangle is 5 × 3600.

- B. Stage Two: Common Spatial Pattern Stage

In the second stage, we modify and employ the architectures of SPDNet to capture the spatial patterns of EEG signals.

1) Depthwise BiMap: The BiMap layer in SPDNet [33] will be ﬁrst modiﬁed to the depthwise BiMap layer that does not take a channel-wise summation after the bi-multiplication and then employed in the CSP stage. Preserving the SPD structure, it will transform spatial covariance matrices in each channel by right-multiplying a full column-rank matrix W and leftmultiplying its transpose simultaneously, i.e., W · Sij · W⊤.

Remark. 1). In Stage Three, the use of 2D CNN for extracting temporal dynamics is because, in principle, the tangent space at a point on a Riemannian manifold is a vector space isomorphic to Euclidean space with the same dimension and thus always ﬂat. Hence, after LOG, the classiﬁcation problem returns to one in the (ﬂat) Euclidean domain. The geometric neural networks, developed to deal with problems in the curved space, are not necessary to apply.

1 The results of BCI competition IV can be found in the ofﬁcial website http://www.bbci.de/competition/iv/results/.

2). The width of 2D CNN is set at a multiple of o2 because we hope to alleviate the inﬂuence of different spatial locations of EEG electrodes on the scalp. Two possible multiple p = 1 and F mean that each frequency band in the portfolio can independently and equally contribute to the model performance.

D. Stage Four: Classiﬁcation Stage and Loss Function

In the ﬁnal stage, single-layer or multi-layer neural networks are utilized for the ﬁnal classiﬁcation. The loss function in our approach is cross-entropy for the sake of simplicity.

IV. EXPERIMENTS

- A. Evaluation Dataset

We investigate the proposed approach on two MI datasets, including Korea University Dataset (MI-KU) [42] and the BCI Competition IV 2a (BCIC-IV-2a) [43].

- 1) Korea University Dataset (MI-KU): In the MI paradigm

of the MI-KU dataset, 54 subjects performed a binary class MI task. The signals were collected with 62 Ag/AgCl electrodes where 20 electrodes in the motor cortex region were selected (FC-5/3/1/2/4/6, C-5/3/1/z/2/4/5, and CP-5/3/1/z/2/4/6) and recorded with a sampling rate of 1,000 Hz for our evaluation of each classiﬁer. The MI-KU dataset has two sessions (S1 and S2), each with 200 trials per subject.

2) BCI Competition IV 2a (BCIC-IV-2a): BCIC-IV-2a is a cue-based BCI paradigm with four-class MI-EEG motor imagery tasks including left hand, right hand, feet, and tongue recorded in 22 Ag/AgCl EEG electrodes and three monopolar EOG channels with a sampling rate of 250 Hz from 9 subjects. The BCIC-IV-2a dataset has the training session (T), and the evaluation session (E) recorded on different days. Each subject performed six runs of 12 cue-based trials for each of the four classes in either training or evaluation sessions, yielding 288 trials per subject.

- B. Evaluation Baselines

The proposed approach is compared with the following diverse baselines the CSP approach FBCSP, the Riemannianbased approaches (MDM/TSM), and the DL approaches (ConvNet/EEGNet/FBCNet/SPDNet).

- 1) FBCSP: FBCSP employs CSP on each sub-bands of EEG signals to acquire sub-band scores and then deploy the classiﬁcation algorithms on selected features. FBCSP attained the best result in BCIC-IV-2a in 2008 and is the most representative among the CSP variants. The repository of the Python toolbox refers to publicly available FBCSP Toolbox https://fbcsptoolbox.github.io/.
- 2) Riemannian-based Approaches: Minimum Distance to Riemannian Mean (MDM) and Tangent Space Mapping (TSM) [25] utilize the geodesic distances and distances of projected SPD matrices on tangent space of on

S++n , AIRM for the EEG classiﬁcation, respectively.

For multiclass classiﬁcation, we modify it using the one-versus-rest (OVR) strategy. The repository of the Python toolbox refers to publicly available pyRiemann https://github.com/pyRiemann/pyRiemann.

3) Deep Learning Approaches: Apart from SPDNet, several CNN architectures are selected as baselines. ConvNet [10] is the ﬁrst CNN approach to extract the temporospatial patterns from EEG signals whose architecture consists of convolution-max-pooling blocks with a unique ﬁrst convolutional layer for temporal information, standard convolution-max-pooling blocks, and a dense softmax classiﬁcation layer; EEGNet [9] was published soon after ConvNet, which modiﬁed CNNs concerning the properties of EEG signals, consisting of the DepthwiseConv2D layer and the SeparableConv2D layer. Inﬂuenced by FBCSP, FBCNet [13] uses modiﬁed CNNs on each sub-bands of EEG signals to capture the temporospatiofrequency features and achieves state-ofthe-art performance on several primary MI-EEG datasets; The repository of the Python toolbox refers to the publicly available package on GitHub https://github.com/ravikiranmane/FBCNet.

C. Naming Conventation for Hyper-parameters

To further analyze Tensor-CSP, we introduce notations of its hyper-parameters. Formally, w-CSPNet(m,n,l) represents the Tensor-CSPNet with w window slices, m banks for ﬁlters, n blocks of the CSP layer, and l-layer neural networks in the perception layer. The number of banks m is set to F, and the speciﬁc frequency ranges refer to Section III-A2. The depth of the fully-connected layer l has two options {1,3}. The output dimension of the depthwise BiMap is denoted as o, where o ∈ {4, 8, 12, 16, 20, 22, 24, 28, 32, 36}. The hyperparameters in the temporal convolutional stage are a portfolio @(p,q,r), where the triple is the width, the height, and the number of channels of 2D CNNs, respectively. The summary of the notations refers to Table IV.

- D. Evaluation Scenarios

We will evaluate Tensor-CSPNet on two scenarios of the subject-speciﬁc analysis. The subject-speciﬁc analysis refers to the training and testing datasets from the same subject.

- 1) Cross-Validation Scenario (Stationary Scenario): This scenario uses a standard evaluation setting of 10-fold crossvalidation (with a shufﬂe data index) for each subject.
- 2) Holdout Scenario (Non-stationary Scenario): The holdout scenario is a cross-session scenario in which the model is trained in one session and evaluated in another session. Figure 3 illustrates the holdout scenario on two datasets. Note that the two-session signals of each dataset are collected on different days. Hence, there is typically a drift of statistical distributions between two sessions (i.e. the non-stationary phenomenon), as illustrated in Figure 6 (a).

- E. Performance Comparison

In this section, we evaluate Tensor-CSPNet on MI-KU and BCIC-IV-2a. Each dataset has three scenarios, including two 10-fold-cross-validation (CV) scenarios and one holdout scenario.

- TABLE I: Conﬁgurations of Temporal Segments: In this paper, there are three kinds of temporal segments without overlapping on MI-KU, and there are four kinds of temporal segments with overlapping on BCIC-IV-2a that are adopted from [44].

[Figure 22]

MI-KU Temporal Segments (sec.)

[Figure 23]

- (a). 1-CSPNet {1.0 ∼ 3.5}
- (b). 5-CSPNet {1.0 ∼ 1.5, 1.5 ∼ 2.0, 2.0 ∼ 2.5, 2.5 ∼ 3.0, 3.0 ∼ 3.5}
- (c). 10-CSPNet {1.00 ∼ 1.25, 1.25 ∼ 1.50, 1.50 ∼ 1.75, 1.75 ∼ 2.00, 2.00 ∼ 2.25, 2.25 ∼ 2.50, 2.50 ∼ 2.75, 2.75 ∼ 3.00, 3.00 ∼ 3.25, 3.25 ∼ 3.50}

[Figure 24]

BCIC-IV-2a Temporal Segments (sec.)

[Figure 25]

- (a). 1-CSPNet {0 ∼ 4}
- (b). 3-CSPNet {0 ∼ 2, 1 ∼ 3, 2 ∼ 4}
- (c). 5-CSPNet {0.0 ∼ 2.0, 0.5 ∼ 2.5, 1.0 ∼ 3.0, 1.5 ∼ 3.5, 2.0 ∼ 4.0}
- (d). 7-CSPNet {0.0 ∼ 1.0, 0.5 ∼ 1.5, 1.0 ∼ 2.0, 1.5 ∼ 2.5, 2.0 ∼ 3.0, 2.5 ∼ 3.5, 3.0 ∼ 4.0}

[Figure 26]

- TABLE II: Average accuracies and standard deviations for the subject-speciﬁc analysis of MI-KU (a total of 54 Subjects) and BCIC-IV-2a (a total of 9 Subjects). Each result in the table is denoted as average accuracy (standard deviation). The best-performing number for each analysis is highlighted in boldface.

[Figure 27]

[Figure 28]

MI-KU (20 channels, 2 classes) BCIC-IV-2a (22 channels, 4 classes) CV (S1) % CV (S2) % Holdout (S1→ S2) % CV (T) % CV (E) % Holdout (T → E) %

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

FBCSP 64.41 (16.28) 66.47 (16.53) 59.67 (14.32) 73.57 (15.13) 72.46 (16.02) 65.79 (14.21) MDM 50.47 (8.63) 51.93 (9.79) 52.33 (6.74) 62.96 (14.01) 59.49 (16.63) 50.74 (13.80) TSM 54.59 (8.94) 54.97 (9.93) 51.65 (6.11) 68.71 (14.32) 63.32 (12.68) 49.72 (12.39) SPDNet 57.88 (8.68) 58.88 (8.68) 60.41 (12.13) 65.91 (10.31) 61.16 (10.50) 55.67 (9.54) EEGNet 63.35 (13.20) 64.86 (13.05) 63.28 (11.56) 69.26 (11.59) 66.93 (11.31) 60.31 (10.52) ConvNet 64.21 (12.61) 62.84 (11.74) 61.47 (11.22) 70.42 (10.43) 65.89 (12.13) 57.61 (11.09) FBCNet 74.16 (12.60) 73.81(13.99) 67.83 (14.34) 77.26 (14.82) 76.58 (13.09) 72.71 (14.67) Tensor-CSPNet 74.95 (15.27) 75.92 (14.63) 69.65 (14.97) 75.98 (14.26) 74.92 (14.63) 72.96 (14.98)

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

- Fig. 3: Illustrations for Experimental Settings of the holdout scenarios on two datasets: (a). MI-KU; (b). BCIC-IV-2a.

The conﬁgurations for Tensor-CSPNet are a little different in each scenario. We require the output dimension of the depthwise BiMap layer to be o = 20 and 22, respectively, on two datasets. The reason for picking such a hyper-parameter is discussed in Appdenix D. For the CV scenarios of both datasets, Tensor-CSPNet adopts a shallow neural network 5CSPNet(9,1,1) because the amount of trials for training is small (i.e., 90 trial/class on MI-KU and 65 trial/class on BCIC-IV-

- 2a), which yields the over-ﬁtting for an extensive neural network. For the holdout scenario of both datasets, we also adopt shallow neural networks but with ﬁnner temporal segmentation 10-CSPNet(9,1,1)@(9,5,2) and 5-CSPNet(9,1,1)@(9,5,4), respectively. Because ﬁnner temporal segmentation is much helpful to the performance against the nonstationarity, cautiously discussed in Section V-A.

In EEG-based BCIs, the performance of a classiﬁer typically varies widely in different data preparation, such as the segment length of signals, number of electrodes, and electrode placements, even in the same experimental scenario. FBCSP is always regarded as the most stable and convincing baseline

in most cases. From Table II, we notice that the Riemannianbased approaches, MDM and TSM, perform like a random guess on MI-KU but a bit better on BCIC-IV-2a. It exhibits the limited effectiveness of using geometric quantities on SPD manifolds as the high-level features for classiﬁcation.

The mainstream DL methodology in the MI-EEG classiﬁcation exploits EEG signals’ temporospatiofrequency features. Hence, we will categorize the ﬁve DL approaches in Table II into three groups,

- 1) SPDNet: It only exploits the spatial patterns of EEG signals and achieves the worst performance among all the DL approaches in Table II.
- 2) EEGNet and ConvNet: They exploit the temporospatial patterns, and their performances are close to FBCSP. Note that FBCSP extracts the temporospatiofrequency patterns. The similar performance shows that combining any two components nearly contributes to the classiﬁcation.
- 3) FBCNet and Tensor-CSPNet: They exploit the temporospatiofrequency patterns and outperform EEGNet and ConvNet in all scenarios, attributed to bandpass ﬁlters that embody the frequency information. Tensor-CSPNet performs slightly better than FBCNet on MI-KU but somewhat worse on BCIC-IV-2a, except for its holdout scenario. We brieﬂy discuss why it performs well on both holdout scenarios in Section V-A.

F. Interpretability Analysis

In this section, we investigate the interpretability of extracted temporospatiofrequency patterns of Tensor-CSPNet using Deep Learning Important FeaTures (DeepLIFT) [45], which is a gradient-based interpretation method widely employed in the BCI classiﬁcation [9], [13].

[Figure 43]

- Fig. 4: Illustration of the heatmap of the relevance patterns of 5-CSPNet(9,1,1): The experiment is conducted on Subject No.2 of MI-KU with a testing accuracy of over 0.9. The relevance pattern after DeepLIFT has an output shape (5, 9, 20, 20). We ﬂatten the relevance pattern into ﬁve rectangles with a height of 20 grids (20 channels) and a width of 9 grids (9 frequency bands). Each rectangle represents the spatial-frequency information within a time window of {1.0 ∼ 1.5 s, 1.5 ∼ 2.0 s, 2.0 ∼ 2.5 s, 2.5 ∼ 3 s, 3.0 ∼ 3.5 s}. The rectangle column records the main diagonal of the relevance pattern’s 20 × 20 covariance matrix. The value in each cell on the heatmap is normalized in [0, 1] and smoothed by a Gaussian ﬁlter.

To interpret the extracted features, we propose a simple visualized approach to ﬂatten the four-dimensional relevant pattern of DeepLIFT to a two-dimensional rectangle, illustrated in Figure 4. Subject No.2 is selected from the MI-KU dataset for interpretation, whose testing accuracy is over 0.9. The upper and lower rows in the heatmap represent the right-hand and left-hand MI, respectively, and are interpreted as follows,

- (a) The right-hand MI: Patterns with 8∼28 Hz highlights around C3 in 1.0∼1.5 sec and 2.5∼3.0 sec.
- (b) The left-hand MI: Patterns with 24∼28 Hz highlights around C4 in 1.0∼1.5 sec and 2.5∼3.0 sec.

The above-interpreted temporospatiofrequency information is consistent with the existing practical frequency components of the left and right-hand MI [46] that the alpha band 9∼14

Hz and beta bands 18∼26 Hz perform more signiﬁcantly on C3 and C4 of the primary motor cortex, or M1. Two active time windows indicate the change of band power event-related desynchronization (ERD) and the event-related synchronization (ERS) occurring during MI [47].

G. Visualization

In this section, we plot the 2-dimensional projections for outputs of each intermediate layer in Tensor-CSPNet using tdistributed Stochastic Neighbor Embedding (t-SNE) [48]. The t-SNE algorithm is a widely used technique of non-linear dimensionality reduction to visualize high-dimensional data. Speciﬁcally, we will investigate the mechanism of TensorCSPNet via visualizing the outputs of each intermediate layer

[Figure 44]

- Fig. 5: Illustration of outputs of each intermediate stage in 5-CSPNet(9,1,1) with o = 22 on Subject No.28 of MI-KU: The time windows for the model are 1 ∼ 1.5 s, 1.5 ∼ 2.0 s, 2.0 ∼ 2.5 s, 2.5 ∼ 3.0 s, and 3.0 ∼ 3.5 s. (a). 5-Temporal Segmentation of Subject No.28: This ﬁgure is the same as Fig. 6, but there is a rotation due to the ﬁgure scale. (b). Features after CSP layer (Stage 2): Blue and yellow/green have ﬁve segments because of the ﬁve temporal segmentation. We name each data cluster as the temporal segment in this paper. (c). Features after TC layer (Stage 3): Segments of either blue or yellow/green aggregates. The yellow/green one lies in the middle of two blue parts. (d). Features after TC layer (Class Label): Draw the points with label information. Two classes are almost evenly distributed on both sides of the decision boundary.

in the holdout scenario of MI-KU. Subject No.28 in MI-KU is chosen for visualizing because Tensor-CSP attains a good performance on this subject with an accuracy of 0.92. Attributed to the tensor stacking stage, the training set is mixed up with the validation and test sets, as illustrated in Figure 5 (a). The CSP stage centralizes the data shape in each temporal segment of the training, validation, and test sets, respectively, so that there are ﬁfteen segments (= 5 × the training/validation/test sets.) in Figure 5 (b). The temporal concentration and 2D CNN in the TC stage concentrate temporal segments of either the training, validation, or test sets along the time domain, as illustrated in Figure 5 (c). The Figure 5 (d) records the labelwise projections in which we can distinguish the different class of labeled data. In addition, we notice that data with Class 1 and Class 2 lies on the bottom and upper sides of the decision boundary, respectively. More examples and visualization of BCIC-IV-2a are illustrated in Appendix.

V. DISCUSSION

In the discussion, we ﬁrst provide evidence of why Tensor-CSPNet outperforms the other approaches in the nonstationary scenarios. Then, we will discuss the relationship between Tensor-CSPNet and other existing mainstreams of the MI-EEG classiﬁers.

A. Evidence of Temporal Segmentation against Nonstationarity

Early electrophysiological studies show that large-scale patterns of synchronized neuronal activity exhibit considerable variability over time, e.g., alpha-blocking with eyes opening, the transition from wakefulness to drowsiness, etc. The variability was termed as the nonstationarity nature of EEG signals [49] and mainly caused the drift in statistical distribution between different sessions and subjects. To determine TensorCSPNet’s good performance in non-stationary scenarios, we pick Subject No.28 of MI-KU because Tensor-CSPNet’s accuracy of this subject is 0.3 higher than FBCSP’s. Figure 6

exhibits a noticeable trend that the more reﬁned temporal segmentation yields a more extensive crossover region of the training, validation, and test sets in the statistical distribution space. In the view of statistics, temporal segmentation ﬁxes the nonstationarity, which is the rediscovery of a four-decadeago theory called segmentation techniques for nonstationary EEGs [50]. In the view of neural signals, the ﬁxed-interval temporal segmentation breaks down EEG signals into many short piecewise quasi-stationary intervals. Therefore, the drift between different sessions disappears in the numerical aspect, which is helpful to classiﬁcation performance when using the statistical classiﬁer.

B. Tensor-CSPNet VS. Other BCI Classiﬁers

- 1) DL: Most of the DL approaches in the MI-EEG classiﬁ-

cation are designed to exploit the temporospatial information from EEG signals using CNNs. In contrast, Tensor-CSPNet formulates EEG signals on SPD manifolds, uses existing layers in SPDNet on SPD manifolds to exploit the spatial patterns from SCMs, and uses CNNs to capture the temporal dynamics of EEG signals on the tangent space.

- 2) CSP: Attributed to the BiMap layer, Tensor-CSP per-

forms like a CSP-like approach. The weight update using the data-driven approach improves the knowledge that the most appropriate projection matrix W can be entirely determined by label data rather than using the rule of simultaneous diagonalization. Moreover, Riemannian BN performs a regularization in Tensor-CSPNet similar to the Regularized-CSP approach [8], and ReEig leverages the linear spatial ﬁlter to a non-linear one.

3) Riemannian-Based Approaches: Both Tensor-CSPNet and the Riemannian-based approach characterize EEG signals on SPD manifolds. The Riemannian-based approach uses geodesic distance on SPD manifolds as a high-level feature for the MI-EEG classiﬁcation. In contrast, Tensor-CSPNet uses the low-level feature expressions of SMCs captured by a neural network-based approach for classiﬁcation.

[Figure 45]

- Fig. 6: 2-dimensional Projection of Subject No.28 in MI-KU using t-SNE: There are two sessions for each subject in the MI-KU dataset. S1 is for the training set, and two halves of S2 are for the validation and test sets. The lengths of time windows are (a).2500 ms, (b).500 ms, (c).250 ms, and (d).125 ms. There is no overlapping between time windows. Each 2-dimensional color point is dimensionality reduced from a 9×20×20-dimensional point, where it has 20 electrodes in the motor cortex region and nine frequency bands. This is the input format for Tensor-CSPNet.

4) Manifold Learning: Manifold learning [51] is a theoretical dimensionality reduction setting in which the samples are assumed to be on or near a low-dimensional submanifold embedding in high-dimensional space. It aims to acquire a low-dimensional geometric representation of high-dimensional data retaining a meaningful property. Architecture SPDNet can be regarded as a new class of manifold learning for the supervised learning setting because it is a neural-networkbased transformation from one SPD manifold to another, and so is Tensor-CSPNet. However, the studies in Appendix D-A exhibit that expanding the dimension, rather than reducing it, yields a better classiﬁcation performance in some cases.

VI. CONCLUSIONS

In this work, we propose a novel GDL framework called Tensor-CSPNet to exploit the temporospatiofrequency features of EEG signals for a general EEG-BCI classiﬁcation paradigm. To achieve this goal, the framework is inspired by a growing interest in formulating EEG signals on SPD manifolds and uses existing network architectures on SPD manifolds to exploit the patterns. Tensor-CSPNet exhibits better classiﬁcation performance in the experiments than the current state-of-the-art approach. In addition, we investigate how each layer in Tensor-CSPNet works and how temporal segmentation improves the Tensor-CSPNet’s performance in the cross-session scenario and gives an interpretability analysis of the extracted patterns. The current experimental results demonstrate the validity of Tensor-CSPNet for the MI-EEG classiﬁcation. Despite the validity, Tensor-CSPNet also has

the following appealing upsides to existing CNN classiﬁers: 1). SPD-matrix representation for encoding spatial patterns is typically compact and robust to noise. 2). Speciﬁc Architecture on SPD manifolds to enhance feature extraction. For example, It preserves the SPD structure of matrices across layers and essentially maintains more encoding information of SCM. In addition, the combination of the depthwise BiMap layer and ReEig improve the feature expression of spatial patterns. 3). Tensor stacking for well-performing against nonstationarity.

VII. ACKNOWLEDGMENT

This study is supported under the RIE2020 Industry Alignment Fund–Industry Collaboration Projects (IAF-ICP) Funding Initiative, as well as cash and in-kind contributions from the industry partner(s). This study is also supported by the RIE2020 AME Programmatic Fund, Singapore (No. A20G8b0102).

REFERENCES

- [1] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain–computer interfaces for communication and control,” Clinical neurophysiology, vol. 113, no. 6, pp. 767–791, 2002.
- [2] S. Machado, F. Araújo, F. Paes, B. Velasques, M. Cunha, H. Budde, L. F. Basile, R. Anghinah, O. Arias-Carrión, M. Cagy et al., “Eeg-based brain-computer interfaces: an overview of basic concepts and clinical applications in neurorehabilitation,” Reviews in the Neurosciences, vol. 21, no. 6, pp. 451–468, 2010.
- [3] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K.-R. Muller, “Optimizing spatial ﬁlters for robust eeg single-trial analysis,” IEEE Signal processing magazine, vol. 25, no. 1, pp. 41–56, 2007.
- [4] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotomamonjy, and F. Yger, “A review of classiﬁcation algorithms for eegbased brain–computer interfaces: a 10 year update,” Journal of neural engineering, vol. 15, no. 3, p. 031005, 2018.
- [5] Z. J. Koles, M. S. Lazar, and S. Z. Zhou, “Spatial patterns underlying population differences in the background eeg,” Brain topography, vol. 2, no. 4, pp. 275–284, 1990.
- [6] K. K. Ang, Z. Y. Chin, H. Zhang, and C. Guan, “Filter bank common spatial pattern (fbcsp) in brain-computer interface,” in 2008 IEEE International Joint Conference on Neural Networks (IEEE World Congress on Computational Intelligence). IEEE, 2008, pp. 2390–2397.
- [7] H. Lu, H.-L. Eng, C. Guan, K. N. Plataniotis, and A. N. Venetsanopoulos, “Regularized common spatial pattern with aggregation for eeg classiﬁcation in small-sample setting,” IEEE transactions on Biomedical Engineering, vol. 57, no. 12, pp. 2936–2946, 2010.
- [8] F. Lotte and C. Guan, “Regularizing common spatial patterns to improve bci designs: uniﬁed theory and new algorithms,” IEEE Transactions on biomedical Engineering, vol. 58, no. 2, pp. 355–362, 2010.
- [9] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces,” Journal of neural engineering, vol. 15, no. 5, p. 056013, 2018.
- [10] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for eeg decoding and visualization,” Human brain mapping, vol. 38, no. 11, pp. 5391–5420, 2017.
- [11] S. Sakhavi, C. Guan, and S. Yan, “Learning temporal information for brain-computer interface using convolutional neural networks,” IEEE transactions on neural networks and learning systems, vol. 29, no. 11, pp. 5619–5629, 2018.
- [12] J.-S. Bang, M.-H. Lee, S. Fazli, C. Guan, and S.-W. Lee, “Spatiospectral feature representation for motor imagery classiﬁcation using convolutional neural networks,” IEEE Transactions on Neural Networks and Learning Systems, 2021.
- [13] R. Mane, E. Chew, K. Chua, K. K. Ang, N. Robinson, A. P. Vinod, S.-W. Lee, and C. Guan, “Fbcnet: A multi-view convolutional neural network for brain-computer interface,” arXiv preprint arXiv:2104.01233, 2021.
- [14] J. Stieger, S. Engel, D. Suma, and B. He, “Beneﬁts of deep learning classiﬁcation of continuous noninvasive brain-computer interface control,” Journal of Neural Engineering, 2021.

- [15] J. Bruna and S. Mallat, “Invariant scattering convolution networks,” IEEE transactions on pattern analysis and machine intelligence, vol. 35, no. 8, pp. 1872–1886, 2013.
- [16] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” nature, vol. 521, no. 7553, pp. 436–444, 2015.
- [17] M. M. Bronstein, J. Bruna, Y. LeCun, A. Szlam, and P. Vandergheynst, “Geometric deep learning: going beyond euclidean data,” IEEE Signal Processing Magazine, vol. 34, no. 4, pp. 18–42, 2017.
- [18] J. Moehlis, “Dynamical systems in neuroscience: The geometry of excitability and bursting,” 2008.
- [19] E. M. Izhikevich, Dynamical systems in neuroscience. MIT press, 2007.
- [20] S. Jang, S.-E. Moon, and J.-S. Lee, “Eeg-based video identiﬁcation using graph signal modeling and graph convolutional neural network,” in 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2018, pp. 3066–3070.
- [21] J. Müller-Gerking, G. Pfurtscheller, and H. Flyvbjerg, “Designing optimal spatial ﬁlters for single-trial eeg classiﬁcation in a movement task,” Clinical neurophysiology, vol. 110, no. 5, pp. 787–798, 1999.
- [22] X. Pennec, P. Fillard, and N. Ayache, “A riemannian framework for tensor computing,” International Journal of computer vision, vol. 66, no. 1, pp. 41–66, 2006.
- [23] X. Pennec, “Manifold-valued image processing with spd matrices,” in Riemannian geometric statistics in medical image analysis. Elsevier, 2020, pp. 75–134.
- [24] P. Libermann and C.-M. Marle, Symplectic geometry and analytical mechanics. Springer Science & Business Media, 2012, vol. 35.
- [25] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Multiclass brain–computer interface classiﬁcation by riemannian geometry,” IEEE Transactions on Biomedical Engineering, vol. 59, no. 4, pp. 920–928, 2011.
- [26] M. Congedo, A. Barachant, and A. Andreev, “A new generation of brain-computer interface based on riemannian geometry,” arXiv preprint arXiv:1310.8115, 2013.
- [27] F. Yger, M. Berar, and F. Lotte, “Riemannian approaches in braincomputer interfaces: a review,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 10, pp. 1753–1762, 2016.
- [28] X. Xie, Z. L. Yu, H. Lu, Z. Gu, and Y. Li, “Motor imagery classiﬁcation based on bilinear sub-manifold learning of symmetric positive-deﬁnite matrices,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 6, pp. 504–516, 2016.
- [29] M. Congedo, A. Barachant, and R. Bhatia, “Riemannian geometry for eeg-based brain-computer interfaces; a primer and a review,” BrainComputer Interfaces, vol. 4, no. 3, pp. 155–174, 2017.
- [30] D. Sabbagh, P. Ablin, G. Varoquaux, A. Gramfort, and D. A. Engemann, “Manifold-regression to predict from meg/eeg brain signals without source modeling,” Advances in Neural Information Processing Systems, vol. 32, pp. 7323–7334, 2019.
- [31] R. J. Kobler, J.-I. Hirayama, L. Hehenberger, C. Lopes-Dias, G. R. Müller-Putz, and M. Kawanabe, “On the interpretation of linear riemannian tangent space model parameters in m/eeg,” in 2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 2021, pp. 5909–5913.
- [32] C. Ju, D. Gao, R. Mane, B. Tan, Y. Liu, and C. Guan, “Federated transfer learning for eeg signal classiﬁcation,” in 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 2020, pp. 3040–3045.
- [33] Z. Huang and L. Van Gool, “A riemannian network for spd matrix learning,” in Proceedings of the AAAI Conference on Artiﬁcial Intelligence, vol. 31, no. 1, 2017.
- [34] Z. Huang, R. Wang, S. Shan, X. Li, and X. Chen, “Log-euclidean metric learning on symmetric positive deﬁnite manifold with application to image set classiﬁcation,” in International conference on machine learning. PMLR, 2015, pp. 720–729.
- [35] Z. Huang, C. Wan, T. Probst, and L. Van Gool, “Deep learning on lie groups for skeleton-based action recognition,” in Proceedings of the IEEE conference on computer vision and pattern recognition, 2017, pp. 6099–6108.
- [36] M. Dai, Z. Zhang, and A. Srivastava, “Analyzing dynamical brain functional connectivity as trajectories on space of covariance matrices,” IEEE Transactions on Medical Imaging, vol. 39, no. 3, pp. 611–620, 2020.
- [37] G. Pfurtscheller and C. Neuper, “Motor imagery and direct braincomputer communication,” Proceedings of the IEEE, vol. 89, no. 7, pp. 1123–1134, 2001.
- [38] C. Neuper, R. Scherer, M. Reiner, and G. Pfurtscheller, “Imagery of motor actions: Differential effects of kinesthetic and visual–motor mode

- of imagery in single-trial eeg,” Cognitive brain research, vol. 25, no. 3, pp. 668–677, 2005.
- [39] G. Buzsáki and K. Mizuseki, “The log-dynamic brain: how skewed distributions affect network operations,” Nature Reviews Neuroscience, vol. 15, no. 4, pp. 264–278, 2014.
- [40] D. Brooks, O. Schwander, F. Barbaresco, J.-Y. Schneider, and M. Cord, “Riemannian batch normalization for spd neural networks,” arXiv preprint arXiv:1909.02414, 2019.
- [41] D. Gabor, “Theory of communication. part 1: The analysis of information,” Journal of the Institution of Electrical Engineers-Part III: Radio and Communication Engineering, vol. 93, no. 26, pp. 429–441, 1946.
- [42] M.-H. Lee, O.-Y. Kwon, Y.-J. Kim, H.-K. Kim, Y.-E. Lee, J. Williamson, S. Fazli, and S.-W. Lee, “Eeg dataset and openbmi toolbox for three bci paradigms: an investigation into bci illiteracy,” GigaScience, vol. 8, no. 5, p. giz002, 2019.
- [43] C. Brunner, R. Leeb, G. Müller-Putz, A. Schlögl, and G. Pfurtscheller, “Bci competition 2008–graz data set a,” Institute for Knowledge Discovery (Laboratory of Brain-Computer Interfaces), Graz University of Technology, vol. 16, pp. 1–6, 2008.
- [44] Y. Zhang, C. S. Nam, G. Zhou, J. Jin, X. Wang, and A. Cichocki, “Temporally constrained sparse group spatial patterns for motor imagery bci,” IEEE transactions on cybernetics, vol. 49, no. 9, pp. 3322–3332, 2018.
- [45] A. Shrikumar, P. Greenside, and A. Kundaje, “Learning important features through propagating activation differences,” in International Conference on Machine Learning. PMLR, 2017, pp. 3145–3153.
- [46] G. Pfurtscheller, C. Neuper, D. Flotzinger, and M. Pregenzer, “Eeg-based discrimination between imagination of right and left hand movement,” Electroencephalography and clinical Neurophysiology, vol. 103, no. 6, pp. 642–651, 1997.
- [47] G. Pfurtscheller and F. L. Da Silva, “Event-related eeg/meg synchronization and desynchronization: basic principles,” Clinical neurophysiology, vol. 110, no. 11, pp. 1842–1857, 1999.
- [48] L. Van der Maaten and G. Hinton, “Visualizing data using t-sne.” Journal of machine learning research, vol. 9, no. 11, 2008.
- [49] A. Y. Kaplan, A. A. Fingelkurts, A. A. Fingelkurts, S. V. Borisov, and B. S. Darkhovsky, “Nonstationary nature of the brain activity as revealed by eeg/meg: methodological, practical and conceptual challenges,” Signal processing, vol. 85, no. 11, pp. 2190–2212, 2005.
- [50] J. S. Barlow, “Methods of analysis of nonstationary eegs, with emphasis on segmentation techniques: a comparative review.” Journal of clinical neurophysiology: ofﬁcial publication of the American Electroencephalographic Society, vol. 2, no. 3, pp. 267–304, 1985.
- [51] M. Belkin and P. Niyogi, “Laplacian eigenmaps and spectral techniques for embedding and clustering.” in Nips, vol. 14, no. 14, 2001, pp. 585– 591.
- [52] L. T. Skovgaard, “A riemannian geometry of the multivariate normal model,” Scandinavian journal of statistics, pp. 211–223, 1984.
- [53] P. Petersen, S. Axler, and K. Ribet, Riemannian geometry. Springer, 2006, vol. 171.
- [54] R. Bhatia, Positive deﬁnite matrices. Princeton university press, 2009.
- [55] J. Burbea and C. R. Rao, “Entropy differential metric, distance and divergence measures in probability spaces: A uniﬁed approach,” Journal of Multivariate Analysis, vol. 12, no. 4, pp. 575–596, 1982.
- [56] P. T. Fletcher and S. Joshi, “Riemannian geometry for the statistical analysis of diffusion tensor data,” Signal Processing, vol. 87, no. 2, pp. 250–262, 2007.
- [57] M. Fréchet, “Les éléments aléatoires de nature quelconque dans un espace distancié,” in Annales de l’institut Henri Poincaré, vol. 10, no. 4, 1948, pp. 215–310.
- [58] M. Bacák, “Computing medians and means in hadamard spaces,” SIAM Journal on Optimization, vol. 24, no. 3, pp. 1542–1566, 2014.
- [59] B. He, A. Sohrabpour, E. Brown, and Z. Liu, “Electrophysiological source imaging: a noninvasive window to brain dynamics,” Annual review of biomedical engineering, vol. 20, pp. 171–196, 2018.
- [60] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proceedings of the IEEE conference on computer vision and pattern recognition, 2016, pp. 770–778.

APPENDIX A PRIOR ASSUMPTIONS FOR CNNS

In this section, we brieﬂy introduce the prior assumptions on the data domain with which the CNN-type architecture can effectively extract the local statistics from data. For a more

in-depth review of these assumptions, we refer the readers to [15], [17] and references therein. Technically, suppose a signal φ(x) ∈ L2(Ω), where x ∈ Ω ⊂ Rd. The goal of the supervised learning setting is to train a statistical model f :

- X  → Y, where X is the space of representations φ(x) and
- Y is typically a discrete set of labels. We say model f is translation invariant and translation equivariant with respect to any φ ∈ L2(Ω) and any v ∈ Ω if f φ(x − v) = f φ(x) and f φ(x − v) = f φ(x) − v respectively. Many tasks in computer vision are assumed to be translation invariant and translation equivariant and required to be stable with respect to local deformations that is deﬁned as a Lipschitz continuity condition as follows,

||f φ(x − τ(x)) − f φ(x) || ≤ C · ||φ||L2 · sup|∇τ(x)|,

where C is constant, τ(x) is a smooth displacement ﬁeld that deforms the signal, and ∇τ(x) is the deformation gradient tensor.

APPENDIX B SPD MAINFOLDS

In this section, we give a brief overview of SPD manifolds with respect to the afﬁne invariant Riemannian metric (AIRM) [22], [52] and the weighted Riemannian barycenter. For a more in-depth review of the geometry of the space of S++n , we refer the reader to [53], [54] and references therein.

- A. Riemannian Geometry of SPD Matrices

The space of S++n is a Riemannian manifold if endowed with a Riemannian metric. AIRM, a widely-used class of the Riemannian metric for the space of S++n , was put forward independently from information science in the 1980s [55] and engineering disciplines [22], [56] after 2005. Formally, AIRM is deﬁned as gP(v,w) := P− each v and w on tangent space TPS++n . Riemannian manifold

- 1

[Figure 46]

- 2vP−

- 1

[Figure 47]

- 2,P−

- 1

[Figure 48]

- 2wP−

- 1

[Figure 49]

- 2 F, for

S++n , AIRM is a Hadamard that is simply connected and complete with everywhere non-positive sectional curvature. It holds many nice properties, for example, there is an unique geodesic2 γ(t) : [0,1]  −→ S++n between any two SPD matrices P1 and P2 of S++n such that γ(0) := P1, γ(1) := P2 and γ(t) := P

- 1

[Figure 50]

- 2

1 · (P−

- 1

[Figure 51]

- 2

1 · P2 · P−

- 1

[Figure 52]

- 2

1 )t · P

- 1

[Figure 53]

- 2

1 with the arc-length Lg(γ) = ||log(P1−1/2·P2·P1−1/2)||F. In addition, the geodesic distance on S++n , AIRM is invariant under any congruence transformations ΓW, i.e., Lg ΓW ◦ γ = Lg(γ). A parallel transport on S++n , AIRM ΓP

1→P2 : TP

1

S++n  −→ TP

2

S++n is given by ΓP

1→P2(v) := (P2P1−1)12v(P2P1−1)21 , where P1,P2 ∈ S++n and v ∈ TP

[Figure 54]

[Figure 55]

1

S++n .

- B. Weighted Riemannian Barycenter

The weighted Riemannian barycenter is a generalization of weighted barycenter on Riemannian manifolds. In our study, the Riemannian-based BCI classiﬁer and Riemannian BN have been used in the computation procedure. Formally,

2 The geodesic on Riemannian manifolds (M, g) with respect to the LeviCivita connection ∇ is deﬁned as a curve γ(t) such that ∇γ˙ γ˙ = 0.

given a batch B of N SPD matrices {Pi}Ni=1, the weighted Riemannian barycenter (a.k.a. Frechet´ mean [57]) on S++n , AIRM is given as the solution to the following optimization problem [58]:

Barw(B) := arg min

M∈S++n

N

wi · Lg(M,Pi)2,

i=1

where weights wi ≥ 0 (i = 1,...,N) and 1≤i≤N wi = 1.

APPENDIX C FIXED-INTERVAL SEGMENTATION AND Q VALUE

In this section, we propose a strategy for those signals that we are not familiar with their temporal characteristics. We call this strategy to be ﬁxed-interval segmentation. Technically, this strategy means that the EEG signals are initially subdivided into ﬁxed, short equal-length intervals or segments without overlapping. In the main paragraph, this strategy is used for the evaluation of the MI-KU dataset in which we require that the length of each time window can divide by the length of EEG signals for simplicity, and therefore, we employ two conﬁgurations, 5-CSPNet, and 10-CSPNet, whose length of time windows is 500 ms and 250 ms, respectively on MIKU. Furthermore, we conclude that the best q value under the strategy of the ﬁxed-interval segmentation is equal to width W. (q is the height of 2D CNN in the TC stage.) This is because the model performance monotonically increases as the q value increases in Table III. It is also consistent with the neurobiological fact that a wider window size yields a higher probability of examining event-related desynchronization/synchronization during motor imagery tasks.

TABLE III: The results in the hold-out scenario of MI-KU with different q values in the TC stage of 5-CSPNet and 10-CSPNet. q is the height of 2D CNN in the TC stage.

[Figure 56]

5-CSPNet q=1 q=2 q=3 q=4 q=5 Acc. 0.635 0.651 0.660 0.668 0.676 10-CSPNet q=6 q=7 q=8 q=9 q=10 Acc. 0.668 0.674 0.678 0.672 0.684

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

APPENDIX D ABLATION STUDY ON BCIC-IV-2A

This section investigates the effects of each layer and hyper-parameter of Tensor-CSPNet on the training session of BCIC-IV-2a. We will have an in-depth analysis of its mechanism using visualization and discuss the computational efﬁciency of the Tensor-CSPNet. For ease of communication, we summarize the naming conventions for hyper-parameters in Tensor-CSPNet in Table IV. Primarily, we put a symbol BN at the end of each conﬁguration of Tensor-CSPNet to indicate if it has Riemannian BN in the CSP stage.

A. Output Dimension o of the Depthwise BiMap Layer

We investigate the output dimension o in the depthwise BiMap layer. The average accuracies and standard deviations for evaluation are summarized in Table V, and their quartiles

- TABLE IV: Notations for Hyper-Parameters in w-CSPNet(m,n,l) @(p, q, r). The different conﬁgurations of temporal segments on two datasets refer to Table I.

[Figure 61]

Hyper-Parameters Meaning Portfolio of Pre-set Parameters w The number of time window slices. w ∈ {1, 5, 10} in MI-KU, and w ∈ {1, 3, 5, 7} in BCIC-IV-2a.

[Figure 62]

[Figure 63]

- m The number of bandpass ﬁlters. m = 9.
- n The number of the CSP stages. n ∈ {1, 3}. l Depth of the fully-connected networks in the classiﬁcation stage. l ∈ {1, 3}.

[Figure 64]

- o The output dimension o of the CSP stage. o ∈ {4, 8, 12, 16, 20, 22, 24, 28, 32, 36}. (p, q, r) The width, height, and output channels in 2D CNN of the TC stage. p ∈ {1, 9}.

[Figure 65]

are box-plotted in Figure 7. Based on the table and quartile, we have the following observations:

- 1) Observation One (O1): The average accuracy monotonically increases as the output dimension o increases. In Table V, the Dimension of 36 has statistically signiﬁcantly better accuracies than other output dimensions across four architectures (p<0.05, Wilcoxon signed-rank test). When the output dimension is over half the channel dimension, the average accuracy is not statistically signiﬁcantly different from the FBCSPs across four architectures (p>0.3, Wilcoxon signed-rank test). But, it is statistically significantly lower than FBCSP when the output dimension is less than half across four architectures (p<0.01, Wilcoxon signed-rank test).
- 2) Observation Two (O2): The expansion yields slightly better average accuracy than FBCSP, which might improve a speciﬁc subject. Dimension of 32 and 36 of both 1CSPNet(9,1,1) and 1-CSPNet(9,1,1)_BN have an improvement on average accuracies by almost 1 ∼ 2% than FBCSP. Particularly, Dimension of 36 of 1-CSPNet(9,1,1) achieves 0.64 for Subject No.2, whereas FBCSP has 0.52 (p=0.074, Wilcoxon signed-rank test).
- 3) Observation Three (O3): The architecture with a multilayer statistically signiﬁcantly performs worse than the single layer when the output dimension o is over 22 (average p<0.05, Wilcoxon signed-rank test).

1-CSPNet(9, 1, 1)

1.0

StatisticsofAccuraciesonCross-validation

StatisticsofAccuraciesonCross-validation

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

D4 D8 D12 D16 D20 D22 D24 D28 D32 D36 FBCSP OutPut Dimension of Depth Riemannian BiMap

1-CSPNet(9, 1, 3)

1.0

StatisticsofAccuraciesonCross-validation

StatisticsofAccuraciesonCross-validation

- 0.2

- 0.3

- 0.4

- 0.5

- 0.6

- 0.7

- 0.8

- 0.9

D4 D8 D12 D16 D20 D22 D24 D28 D32 D36 FBCSP OutPut Dimension of Depth Riemannian BiMap

1-CSPNet(9, 1, 1)_BN

1.0

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

D4 D8 D12 D16 D20 D22 D24 D28 D32 D36 FBCSP OutPut Dimension of Depth Riemannian BiMap

1-CSPNet(9, 1, 3)_BN

1.0

0.9

0.8

0.7

0.6

0.5

0.4

0.3

0.2

D4 D8 D12 D16 D20 D22 D24 D28 D32 D36 FBCSP OutPut Dimension of Depth Riemannian BiMap

- Fig. 7: Box Plots for Output Dimension of the depthwise BiMap: Box plots of the statistics of outputs for 1-CSPNet(9,1,1), 1-CSPNet(9,1,1)_BN, 1CSPNet(9,1,3) and 1-CSPNet(9,1,3)_BN for various output dimensions {4, 8, 12, 16, 20, 22, 24, 28, 32, 36} of the depthwise BiMap on BCIC-IV-2a. Baseline (FBCSP) is in dark blue and 22 ( = channel dimension) is in pink.

Remark. From Table V, Tensor-CSPNet reveals an interesting

phenomenon: the accuracy will improve when we lift the output dimension of the depthwise BiMap. The map from a small input to a large output is like a volume-conduction problem reconstructing EEG sources. It is evident that many latent variables exist in the EEG signals because the number of current sources is signiﬁcantly greater than measurements in the 3-dimensional brain volume of the electrophysiological source imaging in neurophysiology. [59]

- B. Validity of the Riemannian BN

The Riemannian BN is after depthwise BiMap and before ReEig inspired by the position of BN in ResNet [60]. According to Table V, we have Observation Four (O4), that Riemannian BN relieves overﬁtting and improves up to 1% on the average accuracy in many pairs. Notice that the average accuracy and standard deviation across all the output dimensions 0.7123 and 0.1305 are both better than the ones of 1-CSPNet(9,1,1), respectively, so with the pair of 1-CSPNet(9,1,3)_BN and 1CSPNet(9,1,3). However, the improvement has no statistical signiﬁcance, i.e., average p>0.4 across 20 top-bottom pairs in Table V, Wilcoxon signed-rank test. Figure 7 exhibits this statistical result that the shapes of quartiles for both kinds of architecture are similar.

- C. Depth of Architecture

For the sake of brevity, the output dimension o of each depthwise BiMaps is set 22 in a 3-block CSP layer, i.e.

- o1,o2,o3 = 22. In Table VI, the shallow model (top) statistically signiﬁcantly outperforms the deep one (down) in each top-down pair (average p<0.05 across top-down pairs, Wilcoxon signed-rank test). Apart from the effect of the depth of architecture, we notice that the average accuracy
- of 1-CSPNet(9,1,1) and 1-CSPNet(9,3,1) (Column One) are statistically signiﬁcantly better than ones of 1-CSPNet(9,1,3) and 1-CSPNet(9,3,3) (Column Three), respectively in Table V (average p<0.02 across top-down pairs, Wilcoxon signed-rank test), so with Column Two and Four (average p<0.05 across top-down teams, Wilcoxon signed-rank test). Thus, we have Observation Five (O5), that the shallow model statistically signiﬁcantly outperforms the deep one, and the single-layer statistically greatly exceeds the multilayer (average p<0.05, Wilcoxon signed-rank test).

- D. Time-Frequency Resolution

The frequency resolution is ﬁxed at 4 Hz as the sub-band approach for brevity. In particular, although period 0.0 ∼ 1.0

- TABLE V: Experiments on the Output Dimension o of the Depthwise BiMap Layer: Average accuracy (Acc.) and standard deviation (Std.) under 1CSPNet(9,1,1), 1-CSPNet(9,1,1)_BN, 1-CSPNet(9,1,3), and 1-CSPNet(9,1,3)_BN for a variety of output dimensions in the depthwise BiMap layer on BCICIV-2a. In this case, the accuracy and standard of FBCSP are 0.7357 and 0.1513, respectively. The best-performing method for each analysis is highlighted in boldface.

[Figure 66]

Algorithm/Dimension Metric 4 8 12 16 20 22 24 28 32 36 Avg. 1-CSPNet(9,1,1) Acc. 0.5793 0.6559 0.7023 0.7246 0.7316 0.7304 0.7385 0.7326 0.7408 0.7496 0.7086

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

Std. 0.1572 0.1296 0.1218 0.1225 0.1387 0.1306 0.1303 0.1365 0.1343 0.1294 0.1331 1-CSPNet(9,1,1)_BN Acc. 0.6400 0.6671 0.7041 0.7214 0.7172 0.7383 0.7331 0.7096 0.7413 0.7508 0.7123

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

Std. 0.1241 0.1324 0.1331 0.1288 0.1430 0.1276 0.1284 0.1231 0.1321 0.1329 0.1305 1-CSPNet(9,1,3) Acc. 0.5739 0.6351 0.6814 0.7159 0.7034 0.7181 0.7191 0.6889 0.6927 0.6823 0.6811

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

Std. 0.1339 0.1405 0.1469 0.1448 0.1559 0.1443 0.1369 0.1577 0.1496 0.1603 0.1471 1-CSPNet(9,1,3)_BN Acc. 0.6116 0.6493 0.6975 0.7134 0.7287 0.7277 0.7124 0.7011 0.7023 0.6972 0.6941

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

Std. 0.1205 0.1371 0.1444 0.1454 0.1356 0.1258 0.1387 0.1429 0.1385 0.1527 0.1381

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

- TABLE VI: Experiments on Effectiveness of Riemannian BN: Average accuracy (Acc.) and standard deviation (Std.) under four pairs of CSPNets with the CSPNet(9,1,1) or the CSPNet(9,3,1) on BCIC-IV-2a. The best-performing method for each analysis is highlighted in boldface.

[Figure 99]

1-CSPNet(9,1,1) 1-CSPNet(9,1,1) _BN 1-CSPNet(9,1,3) 1-CSPNet(9,1,3) _BN

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

Acc. 0.7304 0.7383 0.7181 0.7277 Std. 0.1306 0.1276 0.1443 0.1258

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

1-CSPNet(9,3,1) 1-CSPNet(9,3,1) _BN 1-CSPNet(9,3,3) 1-CSPNet(9,3,3) _BN

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

Acc. 0.7292 0.7327 0.6945 0.7241 Std. 0.1341 0.1267 0.1408 0.1381

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

- TABLE VII: Experiments on Time-Frequency Resolution: Average accuracy (Acc.) and standard deviation (Std.) of Tensor-CSPNet under four conﬁgurations of the time windows of 1-CSPNets(9,1,1)_BN without the temporal convolutional stage on BCIC-IV-2a. The best-performing method for each analysis is highlighted in boldface.

[Figure 122]

Sub./Architecture 1-CSPNets(9,1,1)_BN 3-CSPNets(9,1,1)_BN 5-CSPNets(9,1,1)_BN 7-CSPNets(9,1,1)_BN Acc. 0.7383 0.7238 0.7334 0.6821 Std. 0.1276 0.1309 0.1320 0.1357

[Figure 123]

[Figure 124]

s after the cue is an imagination preparation stage and period 3.5 ∼ 4.0 s is a post imagination stage in BCIC-IV-2a, the ﬁrst window slice begins at 0.0 s. In the experiments, we pick architecture 1-CSPNets(9,1,1)_BN with output dimension o = 22, but the temporal convolutional stage is removed to get rid of the effects of the temporal dynamic behavior. Instead, we concatenate the extracted features for the classiﬁcation stage. Hence, we have Observation Six (O6) that the preset temporal segmentation has no statistically signiﬁcant improvement in the average accuracy (p>0.1 for 3-/5-CSPNet except 7-CSPNet, Wilcoxon signed-rank test), but it statistically signiﬁcantly improves the performance of a speciﬁc subject. Speciﬁcally, 3-CSPNets(9,1,1)_BN, 5-CSPNets(9,1,1)_BN, and 7-CSPNets(9,1,1)_BN statistically signiﬁcantly improve almost

- 10% on Subject No.9 from Table VII (p<0.02, Wilcoxon signed-rank test). In addition, the inappropriate segmentation, for instance, 7-CSPNets(9,1,1)_BN, has a clear drop of 5% in the average accuracy.

E. Hyper-parameters in the Temporal Convolutional Stage

In the temporal convolutional stage, there are three hyperparameters in a portfolio @(p,q,r), where width p (p = 1 or F) and height q (1 ≤ q ≤ W), and output channels r for 2D CNN. According to the analysis in the previous subsection, we pick 5-CSPNets(9,1,1)_BN with output dimension o = 22 in this experiment. The height q is set at 2 in all the cases. The width p has two options from {1,9}, and the number

TABLE VIII: Experiments on Hyper-parameters in the Temporal Convolutional Stage: Average accuracy (Acc.) and standard deviation (Std.) of various hyper-parameter portfolios of the temporal convolutional stage for 5-CSPNets(9,1,1)_BN on BCIC-IV-2a. The portfolio @(p, q, r) represents (Width, Height, Number of the Output Channels) in the temporal convolutional stage. The best-performing result is highlighted in boldface.

[Figure 125]

Portfolio @(9, 2, 1) @(9, 2, 10) @(9, 2, 20) Acc. 0.5526 0.6896 0.7173 Std. 0.1497 0.1295 0.1357

[Figure 126]

[Figure 127]

@(1, 2, 1) @(1, 2, 10) @(1, 2, 20)

[Figure 128]

Acc. 0.6166 0.7308 0.7412 Std. 0.1512 0.1375 0.1374

[Figure 129]

of output channels r have three options from {1,10,20}. The more reﬁned segmentation of hyper-parameters in the temporal convolutional stage yields a higher dimension of the output vector. For instance, for a 5-CSPNets(9,1,1), the dimension of the concatenated vector after a 2D CNN with @(p,q,r) = (1,2,20) is 720 = 9 × (5 − 1) × 20 . From Table VIII, we have Observation Seven (O7) that the performance statistically signiﬁcantly monotonically improves as the number of output channels increases and the width of 2D CNN decreases (p<0.05, Wilcoxon signed-rank test).

F. Visualization

We investigate the visualization of BCIC-IV-2a using t-SNE. The well-learned and badly-learned cases are considered in the

comparison, where the well-learned and badly-learned cases are with the average accuracy over 0.80 or under 0.50 under both Tensor-CSPNet and the FBCSP, respectively. The ﬁrst line of Figure 8 is the well-learned case upon Fold 2 of Subject 1. The left subplot is the projection from the original data set. We concatenate 22 × 22 SMCs derived from 9 band-pass signals as a 9 × 22 × 22-dimensional vector and project them via the t-SNE method. The four colors in the resulting cross together, and the middle subplot is the projection from the outputs after the depth BiMap, Riemannian BN, and ReEig. We notice that the four-color points are more separated than those in the left subplot and stacked in a sequence where the same color points concentrate on a speciﬁc location in the ﬁgure. The right subplot is the projection from the outputs after LOG, and it is more concentrated for each color and, after that, more accessible for classiﬁcation. However, we observe that the conﬁguration of the proposed approach is still hard to distinguish between two pairs, such as the pair of the Tongue (red) and the Feet (green) and the pair of Hand (L) and Hand (R). It is consistent with the statistics in the confusion matrix of Table 9 that both FN (False-Negative) and FP (False-positive) for the tongue and feet are 2.6% and 2.9%, respectively. Both FN and FP for the hand (L) (blue) and hand (R) (yellow) are 2.5% and 3.0%, respectively. The second line of the three subplots is the projections on the badly-learned case. All color points cross together from the ﬁrst ﬁgure to the last one, and there is no clear statistical pattern in shape.

[Figure 130]

- Fig. 8: Illustration of 2-dimensional projection for outputs of each intermediate stage in Tensor-CSPNet, including the well-learned case (Subject No.1 in BCIC-IV-2a, Upper three Figures) and the badly-learned case (Subject No.6 in BCIC-IV-2a, Bottom three Figures) using t-SNE. Each subﬁgure has 288 points with four colors. 1-CSPNet(9,1,1)_BN with o = 22 achieves 0.864 and 0.483 average accuracy in two cases, respectively.

G. Computational Efﬁciency

This subsection investigates the computational efﬁciency of the Tensor-CSPNet. The experiments are conducted on an Intel (R) Xeon (R) CPU @ 2.20 GHz with one socket, two cores per socket, and two threads per core. There are two subtopics

### FBCSP

[Figure 131]

474 18.3%

74 2.9%

49 1.9%

51 2.0%

Hand(L)

60 2.3%

502 19.4%

39 1.5%

47 1.8%

Hand(R)

Truelabel

47

Feet

- 1.8%

55 2.1%

469 18.1%

77 3.0%

52

- 2.0%

462 17.8%

46 1.8%

88 3.4%

Tongue

Hand(L) Hand(R) Feet Tongue Predicted label

500

[Figure 132]

[Figure 133]

481 18.6%

79 3.0%

34 1.3%

54 2.1%

Hand(L)

400

66 2.5%

499 19.3%

35 1.4%

48 1.9%

Hand(R)

Truelabel

300

488 18.8%

76 2.9%

47 1.8%

37 1.4%

Feet

200

506 19.5%

42 1.6%

32 1.2%

68 2.6%

100

Tongue

Hand(L) Hand(R) Feet Tongue Predicted label

500

[Figure 134]

400

300

200

100

- Fig. 9: Unnormalized Confusion Matrices for FBCSP and Tensor-CSPNet in the CV scenario of BCIC-IV-2a: 4-class labels include Hand (L), Hand (R), Feet, and Tongue. The total number of trials for both matrices is 2610 ( = 29 trails in test dataset × 10 folds × 9 subjects). The quantities in each cell include the number of the corresponding class (top) and its percentage (%) over the total number of trails (bottom).

to discuss in this subsection, including the operation time per iteration and calibration time per subject.

1) Operation Time per Iteration: We pick three speciﬁc groups of different conﬁgurations of Tensor-CSPNet in Figure 10. Each group has three curves, and one color represents one group. The operation time per iteration increases as the output dimension o of the depthwise BiMap layer increases. The architecture without Riemannian BN (green) is the shortest operation time per iteration, the one with Riemannian BN (red) is in second place, and the one with both the Riemannian BN and a multi-layer classiﬁcation stage (blue) is the longest. In addition, the operation time per iteration of the group of 5-CSPNet rapidly increases 6 ∼ 8 times that of the group of 1-CSPNet. The operation time per iteration of the group of 5-CSPNet(9,1,1)_BN@(1,2,20) is slightly longer than the ones of the group of 5-CSPNet.

5 10 15 20 25 30 35 Output Dimensions of the Depth Riemannian BiMap

0

10

20

30

40

50

60

OperationTimeperInteration(s)

[Figure 135]

- Fig. 10: Illustration of the relation between the operation time per iteration and the output dimension of the depthwise BiMap layer.

2) Calibration Time per Subject: Many training parameters in the DL approaches will affect the calibration time, such as learning rate, batch size, epochs, etc. We ﬁx batch size equivalent to the test set size 28 for training and validation, and the initial learning rate is 0.01 with decay. The total number of training epochs is default 60, and an early stopping strategy with 15 patience is adopted. The average accuracy and standard deviation of the calibration time are shown in Table XI. The average calibration time per subject for nonDL approaches is around 1 min. However, the calibration

TABLE IX: Table for Architecture of 1-CSPNet(9,1,1) with o = 22 on BCIC-IV-2a.

[Figure 136]

Stage Layer Output Shape Parameters Tensor Stacking 9 × 22 × 22 /

[Figure 137]

Depthwise BiMap 9 × 22 × 22 9 × 22 × 22

CSP Riemannian BN 9 × 22 × 22 1 × 22 × 22 ReEig 9 × 22 × 22 / LOG 9 × 22 × 22 /

Classiﬁcation Linear Network 4 4 × 9 × 22 × 22 Total 27,104

[Figure 138]

[Figure 139]

TABLE X: Table for Architecture of 5-CSPNet(9,3,1) @(9, 5,10) with o1, o2, o3 = 22 on BCIC-IV-2a. Stage Layer Output Shape Parameters Tensor Stacking 5 × 9 × 22 × 22 /

[Figure 140]

[Figure 141]

Depthwise BiMap 5 × 9 × 22 × 22 9 × 22 × 22

- CSP (1st) Riemannian BN 5 × 9 × 22 × 22 1 × 22 × 22 ReEig 5 × 9 × 22 × 22 / LOG 5 × 9 × 22 × 22 / Depthwise BiMap 5 × 9 × 22 × 22 9 × 22 × 22
- CSP (2nd) Riemannian BN 5 × 9 × 22 × 22 1 × 22 × 22 ReEig 5 × 9 × 22 × 22 / LOG 5 × 9 × 22 × 22 / Depthwise BiMap 5 × 9 × 22 × 22 9 × 22 × 22
- CSP (3rd) Riemannian BN 5 × 9 × 22 × 22 1 × 22 × 22 ReEig 5 × 9 × 22 × 22 / LOG 5 × 9 × 22 × 22 /

Temporal Convolutional 2D CNN (9 − 9 + 1) × (5 − 5 + 1) × 10 10 × 5 × 9 × 22 × 22 Classiﬁcation Linear Network 4 4 × 10

[Figure 142]

Total 232,360

[Figure 143]

TABLE XI: Experiments on Calibration Time per Subject: Average accuracy (Acc.) and standard deviation (Std.) for the calibration time (s) per subject of baselines and Tensor-CSPNet on BCIC-IV-2a. The output dimension of the CSP stage is 22 for the three conﬁgurations of Tensor-CSPNet.

[Figure 144]

Avg. Times Approx.

[Figure 145]

MDM 53.24 sec / FBCSP 55.88 sec / TSM 60.45 sec /

[Figure 146]

FBCNet 353.14 sec 5.89 min EEGNet 500.03 sec 8.33 min SPDNet 593.32 sec 9.89 min ConvNet 1542.61 sec 25.71 min

[Figure 147]

1-CSPNet(9,1,1)_BN 1997.23 sec 33.29 min 5-CSPNet(9,1,1)@(1,2,20) 7650.99 sec 2.13 hr 5-CSPNet(9,1,1)_BN@(1,2,20) 8860.63 sec 2.46 hr

[Figure 148]

H. Architecture of Tensor-CSPNet We provide the detailed architecture of 1-CSPNet(9,1,1) with

- o = 22 and 5-CSPNet(9,3,1) @(1,2,20) with o1,o2,o3 = 22
- on BCIC-IV-2a. Table IX and X exhibit the total parameters of two conﬁgurations are 27104 and 232360, respectively. Table XII exhibits the numbers of parameters of different architecture as follows, The numbers of ConvNet and EEGNet refers to Table 3 [9]. From Table XII, we notice that EEGNet has a tiny size of parameters. In contrast with ConvNet and EEGNet, the architecture of Tensor-CSPNet needs large-scale parameters to preserve the geometric information of SCMs.

time per subject for the DL approaches is much longer, especially 5-CSPNet(9,1,1)_BN@(1,2,20) is the longest. Three conﬁgurations in Tensor-CSPNet are adopted for comparison. Firstly, 1-CSPNet(9,1,1)_BN is the simplest without temporal segmentation, and it has a longer calibration time than other DL approaches. Because 9-time input size and bigger size of architecture extend the calibration time. Secondly, for 5CSPNet(9,1,1)@(1,2,20), the input size of both algorithms is ﬁve times that of 1-CSPNet(9,1,1)_BN. Hence, there is no doubt that both have over two hours of calibration time.

TABLE XII: Table of number of parameters in network architecture. Shallow Deep

[Figure 149]

[Figure 150]

EEGNet 796 1,716 ConvNet 40,644 152,219 Tensor-CSPNet 27,104 232,360

[Figure 151]

