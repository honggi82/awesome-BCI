# Graph Neural Networks on SPD Manifolds for Motor Imagery Classiﬁcation: A Perspective from the Time-Frequency Analysis

Ce Ju and Cuntai Guan Fellow, IEEE

arXiv:2211.02641v4[eess.SP]20Aug2023

Abstract—The motor imagery (MI) classiﬁcation has been a prominent research topic in brain-computer interfaces based on electroencephalography (EEG). Over the past few decades, the performance of MI-EEG classiﬁers has seen gradual enhancement. In this study, we amplify the geometric deep learningbased MI-EEG classiﬁers from the perspective of time-frequency analysis, introducing a new architecture called Graph-CSPNet. We refer to this category of classiﬁers as Geometric Classiﬁers, highlighting their foundation in differential geometry stemming from EEG spatial covariance matrices. Graph-CSPNet utilizes novel manifold-valued graph convolutional techniques to capture the EEG features in the time-frequency domain, offering heightened ﬂexibility in signal segmentation for capturing localized ﬂuctuations. To evaluate the effectiveness of Graph-CSPNet, we employ ﬁve commonly-used publicly available MI-EEG datasets, achieving near-optimal classiﬁcation accuracies in nine out of eleven scenarios. The Python repository can be found at github.com/GeometricBCI/Tensor-CSPNet-and-Graph-CSPNet.

Index Terms—Motor Imagery Classiﬁcation, Graph Neural Networks, Symmetric Positive Deﬁnite Manifolds, Geometric Deep Learning, Spectral Clustering.

I. INTRODUCTION

A brain-computer interface (BCI) is a technology that measures and analyzes the relevant information of a user’s brain activity and establishes a communication link between the brain and the external environment [1]. Electroencephalogram (EEG)-based BCIs are among the most widely used, portable, and cost-effective BCIs, and have led to numerous applications, such as post-stroke motor rehabilitation, control of a wheelchair system, and video gaming [2]. The control of these EEG-based BCI applications is accompanied by EEG rhythmic changes over the sensorimotor cortices, including the posterior frontal and anterior parietal regions, and a wealth of studies and evidence over the past thirty years has demonstrated that the sensorimotor rhythm changes associated with motor imagery (MI) are effective control signals for BCIs [3]–[5].

During the planning and execution of movement, the sensorimotor rhythms exhibit changes in amplitude that are referred to as event-related desynchronization (ERD) and eventrelated synchronization (ERS), corresponding to decreases and increases in rhythmic activity, respectively. These changes generate patterns that can be reliably and distinctly discerned, enabling the EEG signals to be accurately classiﬁed [6]. In an

Ce Ju and Cuntai Guan are with the S-Lab and School of Computer Science and Engineering, Nanyang Technological University, 50 Nanyang Avenue, Singapore (emails: {juce0001,ctguan}@ntu.edu.sg).

EEG-based motor imagery (MI) task, the individual mentally simulates physical movement, which activates the cortical sensorimotor systems [7] and primary sensorimotor areas [8], and an EEG device records EEG signals. Various machine learning classiﬁers are then utilized to decode an individual’s intentions [9].

Building on the ERD/ERS effect observed during a MI task, conventional MI-EEG classiﬁers adopt the time-spacefrequency principle to extract EEG signal patterns and rhythms. The essence of this principle lies in the analysis of EEG signals in terms of frequency, time, and space, allowing for the identiﬁcation of patterns across these dimensions based on the dominant frequencies of rhythmic activity, their periods of occurrence, and their distribution over the sensorimotor cortices. [10], [11] This principle has been generalized to capture patterns across frequency, time, and space in EEGs. However, the non-stationary nature of EEG spectral contents can hinder the effectiveness of conventional methods that rely on statistical stationarity assumptions [12], [13]. In these circumstances, traditional Fourier analysis proves to be ineffective. To address this challenge, the time-frequency analysis is employed to localize rhythmic components in real time, strengthening the MI-EEG classiﬁers [14]–[17]. Examples of such methods include the short-term frequency transform and the wavelet transform [18]–[20], which have been integrated into the CSP approach to creating novel wavelet-based classiﬁers such as the wavelet-CSP classiﬁer [21].

Motivated by the principles of Gabor’s time-frequency theory and Morlet’s wavelet theory [22]–[24], this study aims to enhance a geometric deep learning-based MI-EEG classiﬁer, namely Tensor-CSPNet [25], to facilitate a more effective exploration of local oscillatory components in EEGs. The proposed approach employs graph-based neural networks, Graph-CSPNet, to handle the MI-EEG classiﬁcation using EEG spatial covariance matrices. A notable characteristic of this neural network incorporates a novel graph BiMap layer, which replaces ﬁxed-length segmentation with a ﬂexible timefrequency resolution to capture localized ﬂuctuations, enabling simultaneous analysis in the time-frequency domain. Drawing inspiration from the Heisenberg-Gabor uncertainty principle, the graph BiMap layer strikes a balance by capturing signal information with high spectral resolution and low temporal resolution for low frequencies while adopting the opposite for high frequencies. Speciﬁcally, to create a time-frequency graph within the graph BiMap layer, each spatial covariance matrix obtained from an EEG segment serves as a graph node.

[Figure 1]

[Figure 2]

[Figure 3]

©2023 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works. DOI: 10.1109/TNNLS.2023.3307470

[Figure 4]

TABLE I: Comparison between Tensor-CSPNet and Graph-CSPNet. Geometric Classiﬁers Tensor-CSPNet Graph-CSPNet (Proposed) Network Input Tensorized Spatial Covariance Matrices. Time-Frequency Graph. Architecture BiMaps; CNNs. Graph-BiMaps. Distinctive Structure CNNs for Temporal Dynamics. Spectral Clustering for Time-Frequency Distributions. Training Optimizer Riemannian Optimization Riemannian Optimization. Underlying Space (S++, gAIRM). (S++, gAIRM). Methodology Heritage CSP. CSP; Riemannian-Based Approaches. Design Principle The Time-Space-Frequency Principle: The Time-Space-Frequency Principle and the Principle of Time-Frequency

[Figure 5]

[Figure 6]

[Figure 7]

Exploitation in the frequency, space, and time Analysis: Exploitation in the time-frequency domain simultaneously, and domains sequentially. then in the space domain.

[Figure 8]

The graph captures the local topology using a novel timeevolution method. The edge weight determines the similarity between neighboring nodes, computed using a Gaussian kernel applied to the Riemannian distance between two nodes on SPD manifolds. Consequently, the classiﬁcation problem of MI-EEG is transformed into a graph classiﬁcation problem involving a time-frequency distribution. Table I compares two geometric classiﬁers for MI-EEG classiﬁcation.

Due to the limited number of trials available for training, the subject-speciﬁc scenario poses a big challenge for MI-EEG classiﬁers. Hence, the proposed geometric classiﬁer will be evaluated on ﬁve publicly available MI-EEG datasets with two classic subject-speciﬁc scenarios: the 10-fold cross-validation and the holdout validation. The rest of the paper is structured as follows: Section II delves into the study history of MI-EEG classiﬁers and introduces SPD manifolds, graph convolutional networks, and existing neural networks on SPD manifolds. Section III outlines the architecture of Graph-CSPNet. The performance of Graph-CSPNet is then compared in a comprehensive set of experiments in Section IV, and several key issues are discussed in detail in Section V.

II. PRELIMINARY

In the early stages of MI-EEG classiﬁcation, feature extraction, and selection were commonly used. This involved handcrafted features based on time-domain and frequency-domain statistics, such as band power, magnitude-squared coherence, and phase-locking value [26]–[28]. Traditional machine learning approaches, including support vector machines and linear discriminant analysis, were then applied for classiﬁcation.

The dominant perspective in MI-EEG classiﬁcation has been the analysis in the time domain. Most methods utilize second-order statistics of EEG signals, speciﬁcally the spatial covariance matrix. The common spatial pattern (CSP) methods are widely used spatial ﬁltering techniques. These methods aim to obtain optimal spatial features by maximizing the variance of one class while minimizing the variance of the other [29]– [32].

This results in the following time-domain paradigm for EEG signal analysis. Let X ∈ RnC×nT be a segment of EEG signals, where nC is the number of EEG channels, and nT is the number of sampled points on an epoch duration, and segment X is assumed band-pass ﬁltered, centered, and scaled.

The linear classiﬁer that predicts the label for segment X can be written as follows,

f X;{wi,βi}Ni=1 =

N

βi log (wiXX⊤wi⊤) + β0,

i=1

where N is the number of spatial ﬁlters, {wi}Ni=1 ∈ RnC

are

spatial ﬁlters and {βi}Ni=1 ∈ R are biases. Signiﬁcant attempts have been made to identify more versatile and practical spatial ﬁlters for BCI scenarios [9].

Spatial covariance matrices possess a substantial amount of discriminative information. This includes the variance captured in the on-diagonal entries and the coherence between adjacent channels recorded in the off-diagonal entries [33]. This information is closely related to rhythmic oscillations, which can be quantiﬁed through frequency analysis techniques like power spectral density and magnitude-squared coherence to track the ERD/ERS effect in motor imagery tasks [5]. By focusing solely on the sensorimotor cortices and utilizing spectral power to assess zero-phase synchrony, classiﬁcation outcomes are comparable, if not superior, to those achieved using combinations of other spectral features, such as coherence and phaselocking value. This implies that the information embedded within spatial covariance matrices is adequate for MI-EEG classiﬁcation [27].

In 2011, Barachant ﬁrst utilized SPD manifolds for characterizing EEG spatial covariance matrices in a Riemannianbased classiﬁcation framework [34]. The discipline of SPD manifolds is ingrained with the afﬁne invariant Riemannian metric gAIRM. This approach referred to as the Riemannianbased approach, has since garnered increasing interest in the BCI community, with subsequent studies focusing on optimizing its framework [33]–[35] and applications to various BCI tasks [36]–[38]. The success of Riemannian-based approaches can be attributed to their ability to capture the discriminative power between task classes by utilizing Riemannian distances. The approach theoretically states in [39] that the Riemannian distance between class-related covariance matrices S+ and S− can be expressed as follows:

dgAIRM(S+,S−) =

[Figure 9]

nC

λi 1 − λi

log2(

), (1)

[Figure 10]

i=1

where each λi ∈ (0,1) is the eigenvalue of Equation 3 in Section II-B. This implies that a more signiﬁcant Riemannian distance between two EEG spatial covariance matrices indi-

cates a greater discriminative power, as their eigenvalues are more likely to be close to 1.

The exploration of SPD manifolds traces its roots back to the 1970s, springing from the classical task of enhancing geodetic networks [45]. Since then, it has been assimilated into a multitude of disciplines, including but not limited to geometric statistics, signal processing, computer vision, and robotics [46]–[53]. The conceptualization of spatial covariance matrices as points on SPD manifolds represents a signiﬁcant advancement in the ﬁeld, going beyond its purely formalistic nature. This abstraction acknowledges the positive deﬁnite constraints and infuses new vitality into research by incorporating technical tools from theoretical mathematics and physics. For instance, the abstract formulation of SPD manifolds provides a natural framework for interpolating diffusion tensors and introduces a novel measure of anisotropy in diffusion tensor magnetic resonance imaging [54]. Moreover, applying optimal transport theory on SPD manifolds establishes a solid mathematical foundation for evaluating the variability between calibration-feedback phases in a BCI system [40], [55].

Recently, there has been a gradual shift in the trend of MI-EEG classiﬁers towards the adoption of deep learningbased approaches that operate in the time domain, allowing for the automatic extraction of features from the original EEG signals. In response to this trend, the ﬁrst novel geometric deep learning-based approach on SPD manifolds, known as Tensor-CSPNet, has been proposed to leverage the time-spacefrequency principle in capturing discriminative information from EEG spatial covariance matrices. This approach has demonstrated performance levels close to optimality, comparable to those achieved by convolutional neural networks-based approaches [56]–[59]. This approach is referred to as Geometric Classiﬁers in this paper. The success of this approach is attributed to the BiMap layer introduced in Section II-D, which maintains the Riemannian distances consistently during the learning process, as indicated by the afﬁne invariance property of gAIRM as follows,

dgAIRM(S1,S2) = dgAIRM(WS1W⊤,WS2W⊤), (2)

where S1,S2 ∈ S++ and weight matrix W of the bi-map transformation belongs to the general linear group. This preservation of Riemannian distances ensures the maintenance of discriminative power between task classes. Numerous recent studies have showcased the consistency and potential of this pathway in the realm of MI-EEG classiﬁcation tasks [41]–[44].

In summary, Table II presents the second-order statistics (EEG spatial covariance matrices) approaches for MI-EEG classiﬁers, with a more detailed discussion of time-domain statistics and frequency-domain statistics found in Section V-H. In the latter half of this section, we will brieﬂy overview the computational techniques related to the proposed method.

A. SPD Manifolds with Afﬁne Invariant Riemannian Metric

The spatial covariance matrice of an EEG segment X ∈ RnC×nT is denoted as S = XX⊤ ∈ S++, where S++ := {S ∈ RnC×nC : S = S⊤ and x⊤Sx > 0,∀x ∈ R/{0}} is the space of real nC ×nC symmetric and positive deﬁnite matrices. Equipped with the afﬁne invariant Riemannian metric

gPAIRM(v,w) := P−21vP−12,P−12wP−12 for each v and w on tangent space TPS++, the space of spatial covariance matrices becomes a Hadamard manifold, which refers to a Riemannian manifold that is complete and simply connected and has an everywhere non-positive sectional curvature. The Riemannian distance between two matrices S1 and S2 is given by dgAIRM(S1,S2) = ||log(S−

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

- 1

[Figure 15]

- 2

- 1

[Figure 16]

- 2

i SjS−

i )||F, where F is the Frobenius norm.

- B. Common Spatial Pattern

Let S+ and S− ∈ RnC×nC be the class-related estimates of spatial covariance matrices of segments in a two-class MI-EEG paradigm using the arithmetic mean, i.e., S+ =

1

[Figure 17]

|I+| l∈I+ XlXl⊤ and S− = |I1

[Figure 18]

−| l∈I− XlXl⊤, where I+ and I− are sets of segments in two classes respectively. The CSP method is given by a simultaneous diagonalization of S+ and S− as follows,

WS+/−W⊤ = Λ+/−,

where diagonal matrices Λ+ and Λ− ∈ RnC×nC hold an identity constraint Λ+ + Λ− = In

C

. Each column vector w ∈ Column(W) is called a spatial ﬁlter. It is equivalent to solving a generalized eigenvalue problem as follows,

(S+ + S−)−1S+/−w = λ+/−w. (3)

A set of discriminative powers consists of m spatial ﬁlters {wj}mj=1 from both ends of the spectrum, i.e., zj = log (wjXX⊤wj⊤), where 1 ≤ m ≤ nC.

- C. Graph Convolutional Networks

Given an undirected graph G(V,E) with N nodes {vi}Ni=1 ∈ V and edges {(vi,vj)}i =j ∈ E. Weighted adjacency matrix A ∈ RN×N of graph G records non-negative edge weights {aij ≥ 0}1≤i,j≤N.

The architecture of a multi-layer graph convolutional network model is given by the following layer-wise propagation rule:

H(l+1) ← σ (D¯−

- 1

[Figure 19]

- 2A¯D¯−

- 1

[Figure 20]

- 2)H(l)W(l) ,

where adjacency matrix with added self-connections A¯ := A + IN, diagonal matrix D¯ii := Nj=1 A¯ij, σ is an activation function, and W(l) is a trainable weight matrix. H(l) is the matrix of activations in the l-th layer, and H(0) is the input data. Theoretical analysis suggests that graph convolutional networks provide a localized ﬁrst-order approximation of spectral graph convolution [60].

- D. Neural Networks on SPD manifolds

The SPD matrix-valued network architecture in this section is derived from the following two studies.

TABLE II: MI-EEG classiﬁers using EEG spatial covariance matrices.

[Figure 21]

[Figure 22]

[Figure 23]

Category of Approach Initiation Time Principle Common Spatial Patterns ([29]–[32], etc.). 1999 [29] Search for a linear projection direction that maximizes the discriminative

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

information between classes through solving Eigenvalue Problem 3. Riemannian-Based Approaches ([33]–[35], etc.). 2011 [34] Compare the quantity (i.e., Riemannian distance) consisting of the entire spectrum information of Eigenvalue Problem 3, instead of directly solving it. Geometric Classiﬁers ([25], [40]–[43], etc.). 2022*[25] Search for a nonlinear projection direction that maximizes the discriminative information between classes using gradient descent.

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

* Please note that while the initial application of second-order neural networks for processing EEG spatial covariance matrices was proposed in 2020 [44], the systematic introduction of geometric classiﬁers in BCIs began with the publication of Tensor-CSPNet.

1) SPDNet [61]: SPDNet introduces network architectures that operate on SPD matrices, incorporating the following layers:

- • BiMap: This layer performs the bi-map transformation WSWT on spatial covariance matrix S = UΣUT. The transformation matrix W is typically required to have a full-row rank.
- • ReEig: This layer performs U max(ǫI,Σ)UT, where ǫ is a rectiﬁcation threshold, and I denotes the identity matrix.
- • LOG: This layer maps spatial covariance matrix S onto its tangent space at identity matrix I using U log(Σ)UT.

These layers are designed to ensure that the properties of symmetric and positive deﬁnite are maintained throughout the learning process.

- 2) Riemannian Batch Normalization [62]: This layer is

designed as a type of SPD matrix-valued network architecture that utilizes parallel transport for batch centering and biasing around the Riemannian barycenter. Typically, parallel transport serves as a means to connect local information between various points because manifolds are the local concept, where basic operations that are simple in Euclidean spaces become intricate, leading to a distinct calculus on manifolds. This layer has been demonstrated to improve classiﬁcation performance on EEGs, making it a valuable addition to the existing network architecture on SPD manifolds [25], [42].

III. METHODOLOGY

This section presents a novel geometric deep learning approach, Graph-CSPNet, for MI-EEG classiﬁcation. The architecture of Graph-CSPNet is depicted in Figure 1, and a table containing the parameters for each layer can be found in Section V-F.

A. Time-Frequency Distribution

A novel time-frequency distribution consisting of SPD matrices derived from EEG segments is constructed in the following way: given a segmentation plan on the time-frequency domain with or without overlapping {∆ti × ∆fi}i∈I, the time-frequency distribution consists of EEG spatial covariance matrices {S(∆ti ×∆fi)}i∈I, where S(∆ti ×∆fi) := X¯iX¯i⊤ is the covariance matrix of band-pass ﬁltered EEG signal X¯i ∈ RnC×∆ti within bandwidth ∆fi. The determination of a segmentation plan {∆ti × ∆fi}i∈I relies on changes in ongoing EEG activity, as evidenced by the appearance of the ERD/ERS effect that is induced by cognitive and motor processing. The ERD effect is characterized by a localized

decrease in amplitude, while the ERS effect is marked by an increase in rhythmic activity amplitude. Both of these effects are highly speciﬁc to the frequency band of the event. It is essential to consider the frequency discretization ∆f when working with traditional frequency bands, including δ (< 4 Hz), θ (4 ∼ 7 Hz), µ (8 ∼ 13 Hz), β (14 ∼ 30 Hz), and γ (> 30 Hz) activity, which aligns closely with neurophysiological mechanisms. Due to the subject/user-speciﬁc nature of eventrelated discrimination, the discretization of frequency bands and time intervals can vary depending on the experiment.

Remark. To provide a concrete example, in the case of hand movement imagination, a time resolution of ∆t = 125 ms is applicable to effectively capture the occurrence of the ERD/ERS effects that are speciﬁc to the µ and β frequency bands, which offer the most effective discrimination. Precise selection of the time resolution is essential to ensure that the neural activity corresponding to these frequency bands is accurately detected and properly analyzed [6], [63].

B. Time-Frequency Graph

To characterize the time-frequency distribution mentioned above, we construct a time-frequency graph denoted as G(V,E). The vertices of this graph represent EEG spatial covariance matrices in the time-frequency distribution. The edges of the time-frequency graph are created using a nonparametric statistical approach called the ǫ-neighborhoods approach. This approach involves connecting two vertices, Si and Sj, with an edge if dgAIRM(Si,Sj)2 < ǫ.

Expressly, we assume that brain activities generate a time evolution effect on the power spectrum of the EEG signals along the time axis. To capture this effect, we employ a modiﬁed ǫ-neighborhoods approach that establishes adjacency between two vertices, Si = S(∆ti × ∆fi) and Sj = S(∆tj × ∆fj), if they fall within a box Bǫ

1,ǫ2 in the time-frequency domain. This box is deﬁned by a box width ǫ1 ≥ 0 on the time axis and a box height ǫ2 ≥ 0 on the frequency axis. Therefore, Si and Sj ∈ Bǫ

1,ǫ2 must satisfy the following conditions: 0 ≤ mid(∆ti) − mid(∆tj) ≤ ǫ1;

|mid(∆fi) − mid(∆fj)| ≤ ǫ2,

where "mid" represents the midpoint value of an interval. Note that the time evolution in this study occurs in the forward time ﬂow direction, making it unnecessary to take the absolute value of the difference between the midpoints of ∆t in the above formula.

[Figure 38]

Fig. 1: Illustration of Architecture of Graph-CSPNet: The EEG signal is divided into multiple segments in the time-frequency domain. The spatial covariance matrices obtained from these segments serve as the vertices of the time-frequency graph, which is constructed using a novel nonparametric statistical approach. Once the time-frequency graph is built, we employ an SPD matrix-valued graph convolutional network, consisting of the Graph BiMap layer and the Riemannian Batch Normalization layer, to extract relevant classiﬁcation information while maintaining discriminative power between different task classes. Subsequently, we apply a logarithmic mapping (LOG) layer to transform the SPD matrices onto the tangent space, which are then fed into the cross-entropy loss function for further computation.

The adjacency matrix A of G(V,E) is used to store the similarities between pairs of vertices and is deﬁned as follows,

2

e−d

gAIRM(Si,Sj)/t, if Si and Sj are adjacent; 0, others.

 

A =



where preset Gaussian kernel width t > 0. These similarities are computed using the radial basis function kernel, which considers the Riemannian distance between adjacent vertices. If two vertices are not adjacent, the similarity is set to zero. In other words, if Si and Sj are non-adjacent, the similarity value is assigned as zero. The pseudocode for generating adjacency matrix A refers to Section V-B.

This approach is referred to as the Local Graph Topology (LGT) method, as it effectively captures the local relationships within the time-frequency distribution. By utilizing the LGT method, we gain a more comprehensive understanding of the intricate connections between EEG spatial covariance matrices within the time-frequency distribution.

Remark. 1). Edge Weights: The weight of the edge in the timefrequency graph is calculated using a radial basis function kernel with Riemannian distance, as the discriminative power between task classes is closely related to the Riemannian distance.

2). Connected Components: According to the LGT approach,

each frequency component (θ,µ,β, and γ bands) forms a connected component in the adjacency matrix A of the time-

frequency graph, as shown in Table IV,

  

Aθ

A =

Aµ

Aβ

  .

Aγ

C. Graph BiMap Layer

This section introduces an SPD matrix-valued graph neural network that aims to extract discriminative information from the time-frequency graph. To address this, we construct the layer-wise propagation rule for this SPD matrix-valued graph neural network as follows:

H(l+1) ← RBN ReEig W(l)(D¯−1A¯(l))H(l)W(l)⊤ ,

where A¯(l) := A(l) + IN, D¯ii := j A¯(ijl), and W(l) is a trainable transformation matrix with the full-row rank. The

RBN (Riemannian batch normalization) and ReEig layers are introduced in Section II-D. H(l) ∈ R|V|×n

2

C is a node function in the lth layer. In particular, H(0) := (S1,··· ,SN), A(0) is the time-frequency graph, and A¯(l) := IN, for l ≥ 1.

The proposed layer-wise propagation rule is structurally similar to the classical rule in graph convolutional network architectures. The original linear mapping is replaced with the BiMap mapping, which enables operations on SPD matrices. BiMap ensures that Riemannian distances are consistently preserved during the learning process while maintaining symmetric positive deﬁniteness. This is crucial for MI-EEG classiﬁcation tasks. Furthermore, instead of using D¯−

- 1

[Figure 39]

- 2 A¯(l)D¯−

- 1

[Figure 40]

- 2, we

employ row-normalized D¯−1A¯(l) because we aim to perform normalization only in the time direction. Additionally, we utilize the non-linear operator ReEig, which drops the smallest eigenvalues, as described in Section V-E, to prevent matrix degeneracy.

However, the proposed rule still differs from the classical one. In the following, we will discuss these differences in detail, speciﬁcally focusing on their relevance to our application. A perturbation analysis for the spectrum change induced by transformation D¯−1A¯(l) is presented as follows,

Theorem 1. Given a time-frequency graph G(V,E). For the lth graph BiMap layer, let A(l) be its |V| × |V| adjacency matrix. For i ∈ {1,...,|V|}, the perturbated spatial covariance matrix S¯i ∈ RnC×nC on (S++,gAIRM) is wtitten in to the original spatial covariance matrix Si and a graph-based perturbation term, i.e., S¯i = Si +∆Si, where ∆Si := A(l)[i,: ](S1,··· ,S|V|)⊤. Then, the spectrum of the spatial covariance matrix has a perturbation ratio as follows,

λ(S¯i) λ(Si)

1 − NiCi ≤

≤ 1 + NiCi , (4)

[Figure 41]

where Ci = max(i,j)∈E{exp(λij)}, Ni = {j (i,j) ∈ E} , and λij is largest eigenvalue of log(S−

- 1

[Figure 42]

- 2

- 1

[Figure 43]

- 2

i SjS−

i ).

It is imperative that we initially establish the subsequent Lemma to prove Theorem 1. Lemma 2. Let {Si}Ni=1 be a set of SPD matrices. Then, any linear combination Ni=1 αiSi is still SPD for αi > 0. Proof. The symmetry is obtained by ( Ni=1 αiSi)⊤ =

N i=1 αiSi⊤ = Ni=1 αiSi, and the positive deﬁnite is

achieved by v⊤( Ni=1 αiSi)v = Ni=1 αi(v⊤Siv) > 0, for any v = 0. This concludes the proof.

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

Proof of Theorem 1. Consider the perturbation ∆Si on each

- node Si (1 ≤ i ≤ |V|), which is taken as a linear combination of adjacent nodes as Si + ∆Si = Si + (i,j)∈E aijSj, where

aij := e−d

2

gAIRM(Si,Sj)/t ≤ 1 with a large t is the similarity value for the edge between node Si and Sj in adjacency matrix A(l). Each Si + ∆Si remains symmetric positive and deﬁnite according to Lemma 2.

The Riemannian distance between node Si and its adjacent

- node Sj is dgAIRM(Si,Sj) := ||log(S−

- 1

[Figure 48]

- 2

- 1

[Figure 49]

- 2

i SjS−

i )||F. Notice that |log(S−

- 1

[Figure 50]

- 2

- 1

[Figure 51]

- 2

i SjS−

i ) is a nC × nC symmetric matrix and bounded by an inequality according to the Rayleigh-Ritz theorem [64] as −λijI log(S−

1 2

- 1

[Figure 52]

- 2

i SjS−

[Figure 53]

i ) λijI, where λij is the largest Rayleigh quotient of log(S−

- 1

[Figure 54]

- 2

- 1

[Figure 55]

- 2

i SjS−

i ). Since

- 1

[Figure 56]

- 2

- 1

[Figure 57]

- 2

exp(λij) is the eigenvalue of S−

i SjS−

i according to the definition of exponential matrix and exp is monotone increasing, we have − exp(λij)I S−

- 1

[Figure 58]

- 2

1 2

i SjS−

[Figure 59]

i exp(λij)I.

Note that the pertubation Si+∆Si = Si+ (i,j)∈E aijSj = S

- 1

[Figure 60]

- 2

- 1

[Figure 61]

- 2

- 1

[Figure 62]

- 2

- 1

[Figure 63]

- 2

i (i,j)∈E aijSj S−

i I + S−

i S

i . Then, we have 1 −

NiCi Si Si + (i,j)∈E aijSj 1 + NiCi Si, where Ni = |{j|(i,j) ∈ E}| and Ci = max(i,j)∈E{exp(λij)}. Lastly, the spectrum perturbation ratio in Equation 4 can be obtained using Weyl’s monotonicity theorem [65].

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

Theorem 1 provides both a rough estimated upper and lower bounds for spectrum change ratio λ(S¯i)/λ(Si), for 1 ≤ i ≤ N. This ratio depends solely on the node degree and spectrum between vertices in the time-frequency graph. As the depth of graph BiMap layers increases, the spectrum change ratio increases accordingly.

To maintain the lowest possible spectrum change ratio, it is necessary to set the depth of the graph BiMap layer to one, i.e., a choice is to put A¯(l) := IN, for l > 1, following the ﬁrst layer. The visualization of the impact of spectrum changes, as stated in Theorem 1, is discussed in detail in Section IV-G.

- D. LOG Layer

After the graph BiMap layers, the resulting SPD matrices are mapped onto the tangent space using the logarithm mapping with the identity matrix as the base point, as explained in the LOG layer in Section II-D. In particular, this logarithm mapping is well-deﬁned and applicable to any SPD matrix with the same dimension.

- E. Loss Function For the sake of simplicity, the cross-entropy loss is adopted

- as the loss function for Graph-CSPNet.

IV. EXPERIMENTS A. Evaluation Datasets and Scenarios

As part of the evaluation, we employed ﬁve widely-used MI-EEG datasets. This section offers a concise overview of these datasets. The data of these datasets cannot be accessed via the MOABB 1 or BNCI Horizon 2020 2. All digital signals underwent ﬁltering using Chebyshev Type II ﬁlters with 4 Hz intervals. The ﬁlters were speciﬁcally designed

- 1 The MOABB package comprises a benchmark dataset for state-of-the-

art decoding algorithms encompassing 12 open access datasets and over 250 subjects. This package is accessible at https://github.com/NeuroTechX/moabb.

- 2 The datasets within BNCI Horizon 2020 project is accessible

- at http://bnci-horizon-2020.eu/database/data-sets.

- TABLE III: Brief introductions to the ﬁve selected datasets, with the original settings speciﬁed in parentheses. The textual descriptions in the following text have been modiﬁed from the original settings to suit our purposes better.

[Figure 68]

Dataset Subjects Channels Classes Trials/Session Length Imagery Period Sampling Rate Sessions

[Figure 69]

KU 54 20 (62) 2: left/right hand 200 2.5 s 1 to 3.5 s 1000 Hz 2 Cho2017 49 (52) 20 (64) 2: left/right hand 200 3 s 3 to 6 s 512 Hz 1

- BNCI2014001 9 22 4: left/right hand,feet,tongue 288 4 s 2 to 6 s 250 Hz 2
- BNCI2014002 14 15 2: right hand,feet 160 5 s 3 to 8 s 512 Hz 1 BNCI2015001 12 13 2: right hand,feet 200 5 s 3 to 8 s 512 Hz 2 (2 or 3)

[Figure 70]

- TABLE IV: A non-overlapping and non-uniform segmentation plan for Graph-CSPNet. The table provided lists each frequency band’s time-window length (seconds) as a distinct entity.

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

θ band µ band β band γ band Dataset/Freq Band (Hz) 4 ∼ 8 8 ∼ 12 12 ∼ 16 16 ∼ 20 20 ∼ 24 24 ∼ 28 28 ∼ 32 32 ∼ 36 36 ∼ 40 KU/Cho2017 0.5 0.5 0.5 0.5 0.5 0.5 0.25 0.25 0.25 BNCI2014001 0.25 0.25 0.25 0.25 0.25 0.25 0.125 0.125 0.125 BNCI2014002/2015001 1 1 1 1 1 1 0.5 0.5 0.5

[Figure 75]

[Figure 76]

[Figure 77]

to have a maximum passband loss of 3 dB and a minimum stopband attenuation of 30 dB. The selection criteria for the ﬁve evaluation datasets from MOABB and BNCI Horizon 2020 requires each training session to have more than 150 trial instances, with at least 70 trials for each category. Table III summarizes the ﬁve evaluation datasets.

- 1). KU (also known as Lee2019_MI, from MOABB): It

comprises EEG signals obtained from 54 subjects participating in a binary class EEG-MI task. The EEG signals were captured at 1,000 Hz using 62 electrodes. For evaluation, 20 electrodes in the motor cortex region were selected, i.e., FC-5/3/1/2/4/6, C-5/3/1/z/2/4/5, and CP-5/3/1/z/2/4/6. The dataset was divided into two sessions, S1 and S2, each composed of two phases: training and testing. Each phase consisted of 100 trials balanced between right and left-hand imagery tasks, resulting in 21,600 trials available for evaluation. The EEG signals were epoched from the ﬁrst second to 3.5 seconds in reference to the stimulus onset, resulting in a total duration of 2.5 seconds.

- 2). Cho2017 (from MOABB): It conducted a BCI experi-

ment with 52 subjects involving motor imagery movement (MI movement) of the left and right hands. The EEG data were collected using 64 Ag/AgCl active electrodes, with a 64-channel montage based on the international 10-10 system to record the EEG signals at a sampling rate of 512 Hz. The recording commenced at second 0, following the prompt, and continued for 3 seconds until the conclusion of the cross period. For evaluation, 20 electrodes were selected from the motor cortex region, comprising FC-5/3/1/2/4/6, C-5/3/1/z/2/4/5, and CP5/3/1/z/2/4/6. It is worth noting that the EEG data of subjects No.32, No.46, and No.49 were omitted, reducing the total number of subjects to 49.

- 3). BNCI2014001 (also known as BCIC-IV-2a, from BNCI

Horizon 2020): Its studies involved 9 participants who executed a motor imagery task comprising four classes: left hand, right hand, feet, and tongue. The task was recorded using 22 Ag/AgCl electrodes and three EOG channels at a sampling rate of 250 Hz. The recorded data were ﬁltered between 0.5 and 100 Hz, with a 50 Hz notch ﬁlter applied. The study was conducted in two sessions on separate days, with each participant completing 288 trials in total (six runs of 12 cuebased trials for each class). The EEG signals were epoched from the cue’s onset at Second 2 to the end of the motor imagery period at Second 6, resulting in a total duration of 4 seconds.

4). BNCI2014002 (from BNCI Horizon 2020): 13 participants were tasked with carrying out sustained 5-second kinaesthetic MI of their right hand and feet, as directed by the cue. The session comprised eight runs consisting of 80 trials for each class, amounting to 160 trials per participant.

EEG measurement was conducted using a biosignal ampliﬁer and active Ag/AgCl electrodes with a sampling rate of 512 Hz.

- A total of 15 electrodes were placed. The EEGs were epoched from the cue onset at second 3 to the end of the motor imagery period at second 8, resulting in a total duration of 5 seconds.

5). BNCI2015001(from BNCI Horizon 2020): It involved 12 subjects who performed a sustained right-hand versus both feet imagery task. Most of the study was composed of two sessions, conducted on consecutive days, with each participant completing 100 trials for each class, amounting to 200 trials per participant. Four subjects participated in a third session, but the evaluation did not include these data. The data were acquired at a sampling rate of 512 Hz, utilizing a bandpass ﬁlter ranging from 0.5 to 100 Hz and a notch ﬁlter at 50 Hz. The recording began at Second 3 with the prompt and continued until the end of the cross period at Second 8, with a total duration of 5 seconds.

We typically evaluate datasets containing two sessions, namely KU, BNCI2014001, and BNCI2015001, using two distinct scenarios. The ﬁrst is known as 10-Fold Cross Validation (CV), whereby we divide each subject’s data into ten equally sized class-balanced folds, with nine used for training and one used for testing, and this process is repeated ten times. The second scenario is called Holdout, where we employ the ﬁrst session for training and the second for testing. Given that the EEG data for the two sessions is usually gathered on different days, there may be considerable variability. For the KU dataset, we utilize the ﬁrst 100 trials of the second session for validation, with the remaining trials used for testing. In contrast, datasets featuring only one session, such as BNCI2014002 and Cho2017, are evaluated solely using the 10-fold CV scenario.

- B. Evaluated Segmentation Plans

This study presents an example of non-overlapping and non-uniform segmentation plans, as shown in Table IV, to evaluate the proposed approach. The term "non-overlapping" indicates no overlap between time windows, while "nonuniform" implies that the size of the time windows varies within the frequency band. We considered the commonly used method of segmenting signals in the time domain into units of seconds, half-seconds, or quarter-seconds, which BCI researchers have widely adopted in the past years, but it is not based on extensive neurophysiological considerations. In Table IV, there are 60 segments of EEG signals in the KU/BNCI2014002/BNCI2015001datasets (i.e., 60 segments = 5 windows × 6 frequency bands + 10 windows × 3 frequency bands), 48 segments in the BNCI2014001 dataset (i.e., 48 segments = 4 windows × 6 frequency bands + 8 windows ×

- 3 frequency bands), and 33 segments in the Cho2017 dataset (33 segments = 3 windows × 6 frequency bands + 5 windows × 3 frequency bands).

C. Evaluation Baselines

This study will compare the proposed approach with a range of baseline methods, including FBCSP, FBCNet, and Tensor-CSPNet. The three selected baselines are representative algorithms utilizing the ERD/ERS effect for the MI-EEG classiﬁcation during an MI process through various technological periods.

- 1) FBCSP [66]: This approach is a prominent method within the CSP family, which utilizes the CSP algorithm to extract sub-band scores from EEG signals and subsequently employs classiﬁcation algorithms such as Support Vector Machines (SVMs) on the selected features.
- 2) FBCNet [59]: This approach is a convolutional neural networks-based classiﬁer designed to classify EEG signals by analyzing EEG patterns within the space-timefrequency domain. Speciﬁcally, FBCNet performs on sub-frequency bands of EEGs and is highly skilled at capturing complex EEG patterns.
- 3) Tensor-CSPNet: This approach represents the ﬁrst geometric deep learning approach to MI-EEG classiﬁcation, capable of exploiting EEG patterns sequentially across the frequency, space, and time domains by leveraging existing deep neural networks on SPD manifolds.

It is worth noting that comparison with other prevalent MIEEG classiﬁers, such as the convolutional neural networksbased approaches and Riemannian-based approaches, is not deemed necessary as previous studies [25] have established that FBCNet and Tensor-CSPNet exhibit superior performance on the subject-speciﬁc scenarios of datasets KU and

- BNCI2014001 under evaluation. Furthermore, while the proposed method is referred to as graph neural networks, it should be noted that it fundamentally differs from utilizing EEG device channels as graph nodes to construct a graph neural network in the context of MI-EEG classiﬁers. The method outlined in the text is the most suitable for comparison with the proposed method. Therefore, other graph-based MI-EEG classiﬁers will not be considered or adopted for this study.

D. Conﬁgurations of Network Architecture

For the deep learning methodology, the choice of neural network conﬁguration plays a crucial role in the performance. Hence, we will present neural network conﬁgurations for all deep learning-based approaches used in the evaluation.

For baseline FBCNet, it has relatively few neural network hyperparameters that can be tuned. We used the same nine frequency sub-bands as FBCSP and set 16 parallel spatial convolution blocks for all datasets. For the geometric classiﬁers, we have adopted simple yet effective network architectures for different scenarios as follows:

• Tensor-CSPNet: The network architecture consists of a two-layer BiMap block (BiMap layer + ReEig layer + RBN layer), with input/output dimensions varying across

different datasets. The frequency segmentation for all datasets is performed in 4 Hz bandwidth increments from 4 Hz to 40 Hz without any overlap. The time segmentation, however, varies for each dataset, as follows: 1). For the KU dataset, the BiMap block transforms the input dimension from 20 to 30 and then back to an output dimension of 20. The network employs three temporal segmentations: 0 to 1.5 seconds, 0.5 to 2 seconds, and

- 1 to 2.5 seconds. 2). In the Cho2017 dataset, the BiMap block converts the input dimension from 20 to 30 and then reverts it to an output dimension of 20. The network is divided into three temporal segments: 0 to 1 second, 1 to
- 2 seconds, and 2 to 3 seconds. 3). For the BNCI2014001 dataset, the BiMap block transforms the input dimension from 22 to 36 and then back to an output dimension of 22. This network has two temporal segmentations: 0 to 0.75 seconds and 0.25 to 1 second. 4). For the BNCI2014002 dataset, the BiMap block increases the input dimension from 15 to 30 and then reduces it back to an output dimension of 15. This network employs ﬁve temporal segmentations: 0 to 1 second, 1 to 2 seconds, 2 to 3 seconds, 3 to 4 seconds, and 4 to 5 seconds. 5). For the BNCI2015001 dataset, the BiMap block expands the input dimension from 13 to 30 and then reduces it to an output dimension of 13. This network utilizes ﬁve different temporal segmentations: 0 to 1 second, 1 to 2 seconds, 2 to 3 seconds, 3 to 4 seconds, and 4 to 5 seconds.

• Graph-CSPNet: Graph-CSPNet shares the same neural network architecture as Tensor-CSPNet across all scenarios. However, it employs a different segmentation approach for frequency and time. The speciﬁc timefrequency segmentation plan for Graph-CSPNet is outlined in Table IV. In addition, we typically set the forward time ﬂow to half their maximum possible value, as discussed in Section IV-F.

E. Classiﬁcation Performance

The evaluation is conducted using subject-speciﬁc scenario settings. Two datasets, namely KU and BNCI2014001, have been reinitialized with cross-validation indices, employing different network architectures than those utilized in our previous study [25]. Consequently, the classiﬁcation accuracies of each baseline may slightly vary from the earlier results within an acceptable range of approximately 1%. The remaining three datasets are being utilized for the ﬁrst time in our study. For each scenario, we select the best result among multiple runs.

The time-space-frequency principle is fundamental to all three MI-EEG classiﬁcation algorithms: FBCNet, TensorCSPNet, and Graph-CSPNet. Despite differences in network architectures, they all effectively utilize discriminative information from the time, space, and frequency domains. The segmentation technique employed by Tensor-CSPNet and GraphCSPNet contributes to their superior performance over FBCNet in the three holdout scenarios. This technique breaks down EEG signals into short, quasi-stationary intervals, thereby reducing distribution shifts. Among the algorithms, GraphCSPNet demonstrates a slight advantage in nine out of the

- TABLE V: Average accuracies and corresponding standard deviations derived from subject-speciﬁc analyses of the KU, Cho2017, BNCI2014001,

- BNCI2014002, and BNCI2015001 dataset. Each result in the table is expressed as the average accuracy and its corresponding standard deviation. Notably, the optimal outcome for each analysis is highlighted in boldface, thus providing an enhanced visual representation of the best-performing metrics.

[Figure 78]

[Figure 79]

[Figure 80]

Dataset Scenario FBCSP FBCNet Tensor-CSPNet Graph-CSPNet

[Figure 81]

[Figure 82]

[Figure 83]

KU 10-Fold CV (S1) % 64.33 (15.43) 73.36 (13.71) 73.28 (15.10) 72.51 (15.31) 10-Fold CV (S2) % 66.20 (16.29) 73.68 (14.97) 74.16 (14.50) 74.44 (15.52) Holdout (S1 → S2) % 59.67 (14.32) 67.74 (14.52) 69.50 (15.15) 69.69 (14.72)

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

Cho2017 10-Fold CV % 61.75 (13.26) 65.34 (11.14) 67.30 (12.94) 67.51 (12.89)

[Figure 91]

- BNCI2014001 10-Fold CV (T) % 71.29 (16.20) 75.48 (14.00) 75.11 (12.68) 77.55 (15.63) (BCIC-IV-2a) 10-Fold CV (E) % 73.39 (15.55) 77.16 (12.77) 77.36 (15.27) 78.82 (13.40)

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

Holdout (T → E) % 66.13 (15.54) 71.53 (14.86) 73.61 (13.98) 71.95 (13.36)

[Figure 97]

[Figure 98]

- BNCI2014002 10-Fold CV % 76.07 (13.29) 79.64 (12.77) 80.58 (11.87) 81.65 (11.74)

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

BNCI2015001 10-Fold CV (A) % 79.46 (14.16) 82.62 (13.11) 81.29 (14.78) 84.62 (12.38) 10-Fold CV (B) % 81.96 (11.14) 84.92 (10.30) 85.29 (10.54) 88.00 (7.87) Holdout (A → B) % 73.46 (14.09) 74.50 (16.01) 79.04 (14.67) 79.75 (14.63)

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

eleven scenarios listed in Table V. This is attributed to its reﬁned time-frequency segmentation technique, which provides a more precise characterization of EEG signals.

- F. Hyperparameters in Graph-CSPNet

We will investigate the inﬂuence of hyperparameters in the time-frequency graph, such as ǫ in the LGT method, on the performance of Graph-CSPNet. This analysis is depicted in Figure 2. To streamline the evaluation process, the network conﬁguration of Graph-CSPNet will be simpliﬁed to include a depth-1 graph BiMap layer with input and output dimensions set to 20.

- 1) The utilization of graph topology enables Graph-CSPNet to learn discriminative patterns from the time-frequency graph effectively. This is evident from the signiﬁcant improvements observed in other time-frequency graph conﬁgurations compared to the "non-graph" case, i.e., Time Direction (0,0,0,0) in Figure 2. The "non-graph" case refers to the similarity matrix A(0) := IN.
- 2) Among different time directions, Time Direction (2,2,2,4) yields the best performance, as demonstrated in Figure 2. The corresponding transformed spectral distributions can be found in Figure 4 (c). Additionally, Time Direction (2,2,2,4) showed statistical signiﬁcance in the 10-fold CV experiments of the two groups. However, it did not exhibit signiﬁcance in the holdout experiment. Statistical significance was determined using the one-tailed Wilcoxon signed-rank test [67] with Bonferroni-Holm correction, with a signiﬁcance level of α = 0.05. Therefore, in all of our experiments, we generally set the forward time ﬂow to the nearest integer values, which is the closest approximation to half-values.

- G. Spectrum Distribution Shift

The proposed LGT method serves as a nonparametric statistical approach for initializing the topology of the timefrequency graph. According to Theorem 1, both approaches will introduce changes in the distribution of the spectrum power of spatial covariance matrices.

[Figure 109]

- Fig. 2: The classiﬁcation performance of Graph-CSPNet with multiple time and frequency directions is evaluated on the BNCI2014001 (BCIC-IV-2a) dataset. The forward time direction encompasses the intervals 0 ≤ xθ ≤ 4, 0 ≤ xµ ≤ 4, 0 ≤ xβ ≤ 4, and 0 ≤ xγ ≤ 8. The frequency direction is ﬁxed at Time Direction (1, 1, 4, 3).

[Figure 110]

- Fig. 3: Spectrum Distribution Shift: A two-dimensional projection of Subject No. 1 in the KU dataset using t-SNE is depicted. Each session for the subject consists of a total of 200 trials. The bright red point in each subﬁgure represents the 200th trial in that session, while the 199 green points represent the ﬁrst 199 trials. These points have undergone dimensionality reduction from 20 × 20-dimensional EEG spatial covariance matrices using t-SNE. Furthermore, the 60 dark red points represent the spatial covariance matrices obtained from 60 EEG segments, as speciﬁed in the segmentation plan outlined in Table IV, from the last trial (represented by the bright red point). The 11,940 (= 199×60) blue points also correspond to the spatial covariance matrices derived from the remaining 199 trials.

In this section, we visually examine the extent of these changes by plotting a two-dimensional projection of the transformed spatial covariance matrices using the LGT method. This allows us to observe the shifts in their spectrum distributions.

In Figure 3 (a), the spatial covariance matrices of the 200th

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

(a) Discrete Spectrogram (b) Time Direction (1,1,1,2). (c) Time Direction (2,2,2,4).

- Fig. 4: Discrete Spectrograms of Variant Conﬁguration Time-Frequency Graphs: The LGT method has four "time direction" numbers representing the forward steps in the components of θ, µ, β, and γ. The "frequency direction" numbers are always set to Time Direction (1, 1, 4, 3).

The discrete spectrograms, ranging from (a) to (c), are calculated by evaluating the lower frequency band’s spectrum power on the grids (4 ∼ 16 Hz) across every ﬁve grids on the time axis, with a grid width of 500 ms and a height of 4 Hz. The higher frequency band (16 ∼ 40 Hz) is calculated across each grid, with a grid width of 250 ms and a height of 4 Hz. Spectrogram (a) represents the original spectrum distribution of Subject No. 1 in the KU dataset, while spectrograms (b) and (c) are the spectrum distributions after the LGT method on (a).

[Figure 117]

(a) Time Direction (1,1,1,2). (b) Time Direction (2,2,2,4).

[Figure 118]

[Figure 119]

- Fig. 5: Variant Conﬁgurations of Time-frequency Graphs: The time-frequency graphs (a) and (b), which are derived from spectrograms (b) and (c), respectively, in Figure 4, contain 60 nodes and 390 edges. Each node represents a grid or a couple of grids, with low time resolution for the low frequency (4 to 16 Hz) and high time resolution for the high frequency (16 to 40 Hz). The spectrum of a node evaluates adjacent nodes along the time axis and consists of four graph components corresponding to four frequency bands, i.e., θ, µ, β, and γ. The edge weight of each two adjacent nodes is the geodesic distance

of each group of points are closer together compared to the centers depicted in Figure 3 (a).

H. Variant Parameter Conﬁgurations of Time-frequency Graphs

We will investigate the spectrum distribution and resulting time-frequency graphs generated by different parameter conﬁgurations in the LGT method.

Figure 4 illustrates that the spectrum distribution, transformed by the LGT method, exhibits a localized forward diffusion from left to right along the forward time direction. This diffusion occurs independently in the θ,µ,β, and γ components due to the separation of these frequency bands in the generation Algorithm 1.

Additionally, Figure 5 presents the corresponding timefrequency graphs. Nodes belonging to different frequency bands are not connected. When selecting a larger scale for the forward time ﬂow, the number of edges in the time-frequency graph will increase according to the construction rule. For instance, the time-frequency graph in Figure 5 (b) exhibits more connected edges compared to the one in Figure 5 (a).

V. DISCUSSIONS

between the two points on (S++, gAIRM) and is reconstructed using the multidimensional scaling algorithm.

- A. Preset Edge Weights

The edge weights of the graph are determined by calculating the average Riemannian distances between EEG segments across all samples in the training set. In a 10-fold CV scenario, adjacency matrix A is initialized ten times, with slight differences between each fold. As a result, the adjacency matrix A is speciﬁc to each individual, and consequently, the architecture of Graph-CSPNet that it generates is also individual-speciﬁc.

- B. Pseudocodes of Adjacency Matrix Generation

trial (represented by the bright red point) are located at the center of the cluster formed by the spatial covariance matrices of the ﬁrst 199 trials (depicted in green). However, the segmented spatial covariance matrices of the 200th trial (shown in dark red) are relatively uniformly distributed within the space occupied by the segmented spatial covariance matrices of the ﬁrst 199 trials (illustrated in blue).

In contrast, Figure 3 (b) demonstrates signiﬁcant changes in the distributions of the spatial covariance matrices’ spectrum. The LGT method averages each point with its neighboring points based on the graph topology. As a result, the centers

This section provides the pseudocode to generate an adjacency matrix A of the time-frequency graph. A lattice vector is employed to acquire the average EEG spectral covariance

matrices within an assigned time and frequency interval in the training set.

Taking the example of the BNCI2014001 dataset, with a 1000 ms signal and non-overlapping segmentations of 250 ms and 125 ms, we obtain 4 and 8 windows, respectively, as shown in Table IV. As a result, there are 48 EEG segments (= 4 time windows × 6 frequency bands + 8 time windows × 3 frequency bands), representing the nodes in the timefrequency graph. The lattice vector is a tensor with Dimension = (48,22,22), where 22 is the number of electrodes. The 48 averaged spatial covariance matrices correspond to the second and third dimensions of the tensors (i,22,22), where 1 ≤ i ≤ 48.

The Riemannian distances in Algorithm 1 are calculated using the lattice vector. Speciﬁcally, the adjacency between two nodes is determined by a time-evolution mechanism. As shown in Table IV, the frequency bands are grouped into the θ,µ,β, and γ components, with 4, 4, 16, and 24 nodes, respectively.

The generation algorithm takes into account the time and frequency directions in the θ,µ,β, and γ components. For example, given Time Direction (1,1,1,2) and Frequency Direction (1,1,4,3), spatial covariance matrices evolve by one step, one step, one step, and two steps on the θ,µ,β, and γ components, respectively, along the forward time direction, and one step, one step, four steps, and three steps along the frequency direction.

In pseudocode, "(N,w,x,y) ∈ [θ,µ,β,γ]" indicates the selection of one combination from the four frequency bands (θ,µ,β,γ). For example, if θ is chosen, the combination can be represented as (Nθ,wθ,xθ,yθ) with the θ component. To facilitate readability, we have omitted the subscripts. The "Number of Nodes (Nθ,Nµ,Nβ,Nγ)" refers to the number of graph nodes belonging to a speciﬁc frequency component. The "Length of Time Horizon (wθ,wµ,wβ,wγ)" corresponds to the number of time windows in the respective frequency component, with each frequency component having different time resolutions, resulting in varying window counts. The inclusion of the maximum forward steps, denoted as T, is necessary because sometimes the distance to the rightmost position (the maximum time step) is less than one forward time step. The expression "i%w" represents the remainder when i is divided by w. When assigning values to the time and frequency directions, the usual convention is to ﬁrst ﬁx the frequency and move along the positive time direction. Then, within the same frequency band, higher frequencies are considered. Please refer to our GitHub repository mentioned in the abstract for speciﬁc code examples.

C. Spectral Clustering and Laplacian

Graph-CSPNet employs an SPD matrix-valued graph convolutional network to capture time-frequency information simultaneously. Within the graph convolutional network, a technique known as spectral clustering is utilized. Spectral clustering is a multivariate statistical clustering technique that leverages the spectrum of the data’s similarity matrix [68]. As outlined in Section III-B, the adjacency matrix A of the time-frequency

[Figure 120]

Algorithm 1: Adjacency Matrix Generation

[Figure 121]

Input : Number of Nodes (Nθ,Nµ,Nβ,Nγ); Length of Time Horizon (wθ,wµ,wβ,wγ); Time Direction (xθ,xµ,xβ,xγ); Frequency Direction (yθ,yµ,yβ,yγ).

Output: Adjacency Maxtrix A[i∗,j∗]. Initialization of the lattice vector and start node s ← 1; for (N,w,x,y) ∈ [θ,µ,β,γ] do

[Figure 122]

for i ← {1,...,N} do /* Initialize the first

[Figure 123]

coordinate for A. */ i∗ ← s + i;

/* Compute the largest forward

time step. */ T ← min{w − i%w − 1,x};

/* The time direction. */ if j ∈ {i + 1,...,i + T + 1} then

j∗ ← s + j; A[i∗,j∗] ← exp(−d2gAIRM(Si∗,Sj∗)/t);

[Figure 124]

[Figure 125]

/* The frequency direction. */ if j ∈ {i + wy,...,i + wy + T + 1} then

j∗ ← s + j; A[i∗,j∗] ← exp(−d2gAIRM(Si∗,Sj∗)/t);

[Figure 126]

[Figure 127]

[Figure 128]

A[j∗,i∗] ← A[i∗,j∗]; s ← s + N.

[Figure 129]

[Figure 130]

graph is constructed inspired by classical ǫ-neighborhood neighbor methods from spectral clustering and with considerations speciﬁc to the application. Spectral clustering enables the computation of the average spectral power across the timefrequency domain, effectively highlighting regions of interest in EEG signals for classiﬁcation.

In image processing, the Laplacian operator is used to calculate the second-order derivative of an image and is effective in highlighting areas of rapid intensity changes or edges in the image. Similarly, in the context of spectral clustering in the time-frequency graph, we have a similar interpretation. By employing an overlapping segmentation approach instead of a non-overlapping one, we are able to capture more detailed local information. As the number of segments increases, spectral clustering places greater emphasis on regions of signiﬁcant intensity changes on the SPD manifold, which is constructed based on statistical measures in the time-frequency domain.

Speciﬁcally, given an inﬁnity segmentation plan that spatial covariance matrices {Si}Ni=1 ∈ Sn

C

++ of the time-frequency graph around test trial S¯ are uniformly Gaussian distributed on SPD manifolds given in [51], the discrete graph Laplacian LM = I − A of the time-frequency graph on networks-based

function f will converge to the continuous Laplacian ∆M(f) with the bias term, established by many studies [69]–[71], as

follows, Nj=1 LMf(Si)/ǫ = 12∆Mf(S¯) + O(ǫ1/2).

[Figure 131]

speaking, the choice of different magnitudes does not have a signiﬁcant impact on the performance in the presented scenarios.

- D. Geometric Deep Learning

Geometric deep learning constitutes a subﬁeld of machine learning that focuses on developing algorithms and models which are able to process non-Euclidean structured data, in particular, data represented as graphs and manifolds [72].

Graph Neural Networks (GNNs) are widely recognized as a primary category in geometric deep learning and have been extensively applied to solve a broad range of problems in various domains, such as trafﬁc networks, graph-based recommender systems, molecule design, etc [73]. While the network architectures for these applications are typically designed in Euclidean spaces, there has been growing interest in GNNs in non-Euclidean spaces, or alternatively referred to as manifoldvalued GNNs [74]–[76].

Our scenario precisely ﬁts into the category of GNN problems in a non-Euclidean space, as each node corresponds to an EEG spatial covariance matrix, naturally represented as points on SPD manifolds. The key aspect of our problem lies in the utilization of the BiMap layer in neural networks, which incorporates the BiMap transformation to preserve the discriminative power between task classes, as characterized by the Riemannian distance (see Equation 1, 2, and Table II). Additionally, the graph structure provides a neural networkbased framework for propagating information from different time-frequency EEG segments concurrently, guided by principles from neurophysics.

- E. The ReEig Layer Let S be a real symmetric d × d matrix with eigenvalues

λ1 ≥ λ2 ≥ ··· ≥ λd and corresponding orthonormal eigenvectors {ui}di=1. Then, the spectral decomposition of S is given as S = di=1 λiuiu⊤i . To handle the nonnegative eigenvalues in symmetric matrices, we introduce the following lemma, an essential technique in convex optimization [77].

Lemma 3. Projection S† := di=1 max{λi,0}uiu⊤i on the positive semideﬁnite cone is the extremum of the minimization

problem ||S − S†||22 subject to S 0.

Proof. Without loss of generality, let λd < 0 and deﬁne the projection S† := di=1 max{λi,0}uiu⊤i . It follows that ||S − S†||2 = −λd. To prove this lemma, it sufﬁces to demonstrate that ||S − S†||2 ≥ −λd. Since we have ||S||2 = max{λ1,−λd} = max {u⊤1 Su1,−u⊤d Sud} = max{sup||u||

2=1 −u⊤Su}, then it yields that ||S−S†||2 ≥ sup||u||

2=1 u⊤Su,inf||u||

2=1 u⊤(S−S†)u ≥ u⊤d (S−S†)ud ≥ −u⊤d Sud ≥ −λd.

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

By Lemma 3, we obtain a means to eliminate the insignificant eigenvalues of SPD matrices. In practical applications, we establish a lower bound, β, with a value greater than 0 to ensure that all eigenvalues are not less than β, i.e., S† := di=1 max{λi,β}uiu⊤i . In the implementation, we consistently set the small eigenvalue as β = 1e − 6. Roughly

- F. Architecture of Graph-CSPNet

Table VI summarizes the layers and learnable network parameters in Graph-CSPNet. The total number of learnable network parameters is No2(o1+o3)+(cN+1)o23. For instance, in the case of BNCI2014001, the network conﬁguration is given by N = 48, c = 4, o1 = 22,o2 = 36, and o3 = 22, where o1 and o2 are the input and output dimensions for the ﬁrst graph BiMap layer respectively, o2 and o3 are the input and output dimensions for the second graph BiMap layer. N is the number of the time-frequency graph nodes, and c is the number of classes. The total number of learnable network parameters is 169,444 parameters. Compared to Tensor-CSPNet, this amount is six times the parameters in 1-CSPNet(9,1,1) (27,104 parameters) and almost two-thirds of the parameters in 5-CSPNet(9,3,1) (232,360 parameters).

- G. Optimization on Smooth Manifolds

Due to the parameterization of neural networks in both geometric classiﬁers involving manifolds, specialized optimizers that operate on manifolds are employed to enhance performance. Speciﬁcally, the BiMap and graph BiMap layers have parameters deﬁned on Stiefel manifolds, while the Riemannian Batch Normalization utilizes parameters deﬁned on SPD manifolds. To address the issue of local minima, ﬁrst-order stochastic optimization methods, such as Adam and AdaGrad, which are commonly used in the Euclidean domain, need to be adapted to the corresponding Riemannian manifolds to accommodate the manifold constraints. This is crucial because the deep learning approach exhibits high nonconvexity throughout its domain [78].

To meet this requirement, specialized ﬁrst-order Riemannian adaptive optimization methods have been developed to optimize networks with manifold-valued data [79]. The generalization of adaptive optimization methods involves two essential operators: retraction and parallel transport, which are established within the framework of Riemannian optimization [80]. Riemannian optimization is a ﬁeld of mathematical optimization that deals with optimization problems subject to manifold constraints, i.e., minx∈M f(x), where M is a Riemannian manifold and f : M → R is a smooth function. Retraction is a ﬁrst-order approximation of the exponential map in the manifold space, while parallel transport refers to transporting vectors along smooth curves in manifolds equipped with an afﬁne connection. These two operators, within the manifold domain, enable neural networks to perform gradient descent with improved precision in each update iteration.

- H. Time-Domain Statistics and Frequency-Domain Statistics

In this section, we focus on exploring the similarities and differences between the statistical characteristics of EEG signals in the time and frequency domains. Typically, the analysis of EEG signals involves extracting statistical features through

TABLE VI: Parameters in a two-layer Graph-CSPNet with input tensor shape (N, o1, o1). Layer Type of Parameters Shape of Outputs Number of Parameters Graph BiMap Layer (1st) Stiefel manifolds (N, o1, o2) No1o2 Graph BiMap Layer (2nd) Stiefel manifolds (N, o2, o3) No2o3 Riemannian Batch Normalization SPD manifolds (N, o3, o3) o23 LOG / (N, o3, o3) / Linear Euclidean c cNo23 Total Number of Parameters / / N(o1 + o3)o2 + (cN + 1)o23

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

spatial, temporal, and spectral analyses, either individually or in combination. A survey paper [81] classiﬁes these features into three categories: spatial, frequency (time-frequency), and similarity. These categories encompass various statistical measures obtained from both the time and frequency domains.

- • Spatial Features: These features primarily involve timedomain statistics and can be obtained through supervised methods such as principal component analysis, independent component analysis, and common spatial patterns or through unsupervised methods like the common-average reference and surface Laplacian spatial ﬁlters.
- • Frequency Features: These features focus on frequencydomain statistics and include measures such as band power, fast Fourier transform, and wavelet analysis.
- • Similarity Features: This category encompasses features that capture the similarity between EEG signals, with some of these features being frequency-domain statistics. Examples of similarity features include phase-locking value and magnitude-squared

This section aims to demonstrate the equivalence between timedomain statistics, represented by spatial covariance matrices, and certain frequency-domain statistics, such as band power and magnitude-squared coherence. We argue that classiﬁers utilizing spatial covariance matrices in MI-EEG classiﬁcation can capture information comparable to that obtained from other sources, including phase locking value and magnitudesquared coherence.

This relationship has been previously explored in the literature, as discussed in [27]. It has been observed that various frequency-domain features often reﬂect the same underlying neurophysiological phenomenon during a task. However, this fundamental fact has yet to be explicitly emphasized in previous works, and its recognition is crucial for the successful implementation of geometric classiﬁers.

Suppose a wide-sense stationary real-valued random process Xt with zero mean E(Xt) = 0. The auto-correlation function RX(τ) of Xt is deﬁned as RX(τ) := E(Xt⊤Xt+τ), and the expected (band) power PX of Xt is given by PX := E|Xt|2 = RX(0) = R SX(ω)dω, where SX(ω) is the power spectral density. Hence, the variance of zero-centered Xt is σX2 := E|Xt − E(Xt)|2 = PX. This argument applies to each channel’s time series Xc in multichannel EEG data. Thus, the diagonal entries of the spatial covariance matrices correspond to the variance σX2

, which is equivalent to the geometric classiﬁers expected (band) power PX

c

of that channel c. Using a similar line of reasoning based on the autocovariance function, it can be demonstrated that the off-diagonal entries of the spatial covariance matrices are equivalent to

c

the magnitude-squared coherence without normalization. In practice, implementing a neural network-based approach using non-zero-centered time series yields satisfactory classiﬁcation performance, and there is no need to preprocess the time series by zero-centering them.

VI. CONCLUSIONS

The primary objective of this study is to enhance the geometric classiﬁers in MI-EEG classiﬁcation from a time-frequency analysis perspective, aiming to capture the time-frequency information of signals more effectively. Furthermore, this paper formally introduces the term geometric classiﬁers as the name for this category for the ﬁrst time. To achieve this goal, we present a novel network architecture called GraphCSPNet based on an SPD matrix-valued time-frequency graph. In Graph-CSPNet, we extend graph convolutional networks to SPD manifolds equipped with gAIRM and utilize them to locate EEG rhythmic components in the time-frequency domain precisely. In the graph BiMap layer, we utilize preset graph weights calculated using Riemannian distances to effectively preserve discriminative information of different time-frequency spatial covariance matrices, allowing GraphCSPNet to inherit the characteristics and advantages of several well-known MI-EEG classiﬁers.

In sum, the study’s contribution is twofold, providing both theoretical and practical advances as follows: Theoretically, Graph-CSPNet signiﬁes an improvement in the feasibility of existing models, approached from the fundamental principle of time-frequency analysis in signal processing. Moreover, the potential value of this study lies in proposing a category of methods called Geometric Classiﬁers that have a foundation in differential geometry within the era of deep learning. These geometric classiﬁers are more capable of capturing the characteristics of signal covariance matrices and offer greater possibilities associated with advanced mathematical and physical tools. By incorporating concepts from differential geometry, these methods provide a promising avenue for advancing the understanding and analysis of complex neurophysiological data, such as EEG spatial covariance matrix and fMRI functional connectivity matrix, within the framework of geometric deep learning; Practically, Graph-CSPNet provides enhanced ﬂexibility in handling variable time-frequency resolution for signal segmentation and capturing localized ﬂuctuations. It performs well on ﬁve widely-used MI-EEG datasets, utilizing 10-fold cross-validation and subject-speciﬁc holdout scenarios. In nine out of eleven scenarios, Graph-CSPNet achieves nearoptimal results, showcasing improved classiﬁer performance and offering valuable practical advancements.

ACKNOWLEDGMENTS

This study is ﬁnancially supported by the RIE2020 Industry Alignment Fund–Industry Collaboration Projects (IAF-ICP) Funding Initiative, as well as cash and in-kind contributions from industry partner(s). The study is also supported by the RIE2020 AME Programmatic Fund under Singapore grant No. A20G8b0102.

REFERENCES

- [1] J. R. Wolpaw, N. Birbaumer, W. J. Heetderks, D. J. McFarland, P. H. Peckham, G. Schalk, E. Donchin, L. A. Quatrano, C. J. Robinson, T. M. Vaughan et al., “Brain-computer interface technology: a review of the ﬁrst international meeting,” IEEE transactions on rehabilitation engineering, vol. 8, no. 2, pp. 164–173, 2000.
- [2] H. Yuan and B. He, “Brain–computer interfaces using sensorimotor rhythms: current state and future perspectives,” IEEE Transactions on Biomedical Engineering, vol. 61, no. 5, pp. 1425–1435, 2014.
- [3] G. Pfurtscheller and F. L. Da Silva, “Event-related eeg/meg synchronization and desynchronization: basic principles,” Clinical neurophysiology, vol. 110, no. 11, pp. 1842–1857, 1999.
- [4] G. Pfurtscheller and C. Neuper, “Motor imagery and direct braincomputer communication,” Proceedings of the IEEE, vol. 89, no. 7, pp. 1123–1134, 2001.
- [5] G. PFURTSCHELLER and D. J. McFarland, “13| bcis that use sensorimotor rhythms,” Brain-computer interfaces: principles and practice, p. 227, 2012.
- [6] G. Pfurtscheller, C. Neuper, D. Flotzinger, and M. Pregenzer, “Eeg-based discrimination between imagination of right and left hand movement,” Electroencephalography and clinical Neurophysiology, vol. 103, no. 6, pp. 642–651, 1997.
- [7] M. Jeannerod, “The representing brain: Neural correlates of motor intention and imagery,” Behavioral and Brain sciences, vol. 17, no. 2, pp. 187–202, 1994.
- [8] R. Beisteiner, P. Höllinger, G. Lindinger, W. Lang, and A. Berthoz, “Mental representations of movements. brain potentials associated with imagination of hand movements,” Electroencephalography and Clinical Neurophysiology/Evoked Potentials Section, vol. 96, no. 2, pp. 183–193, 1995.
- [9] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotomamonjy, and F. Yger, “A review of classiﬁcation algorithms for eegbased brain–computer interfaces: a 10 year update,” Journal of neural engineering, vol. 15, no. 3, p. 031005, 2018.
- [10] L. Qin, B. Kamousi, Z. Liu, L. Ding, and B. He, “Classiﬁcation of motor imagery tasks by means of time-frequency-spatial analysis for brain-computer interface applications,” in Conference Proceedings. 2nd International IEEE EMBS Conference on Neural Engineering, 2005. IEEE, 2005, pp. 374–376.
- [11] T. C. Ferree, M. R. Brier, J. Hart Jr, and M. A. Kraut, “Space–time– frequency analysis of eeg data using within-subject statistical tests followed by sequential pca,” Neuroimage, vol. 45, no. 1, pp. 109–121, 2009.
- [12] D. P. Allen and C. D. MacKinnon, “Time–frequency analysis of movement-related spectral power in eeg during repetitive movements: A comparison of methods,” Journal of neuroscience methods, vol. 186, no. 1, pp. 107–115, 2010.
- [13] S. Sanei and J. A. Chambers, EEG signal processing. John Wiley & Sons, 2013.
- [14] S. Blanco, R. Q. Quiroga, O. Rosso, and S. Kochen, “Time-frequency analysis of electroencephalogram series,” Physical review E, vol. 51, no. 3, p. 2624, 1995.
- [15] B. J. Roach and D. H. Mathalon, “Event-related eeg time-frequency analysis: an overview of measures and an analysis of early gamma band phase locking in schizophrenia,” Schizophrenia bulletin, vol. 34, no. 5, pp. 907–926, 2008.
- [16] A. T. Tzallas, M. G. Tsipouras, and D. I. Fotiadis, “Epileptic seizure detection in eegs using time–frequency analysis,” IEEE transactions on information technology in biomedicine, vol. 13, no. 5, pp. 703–710, 2009.
- [17] S. Morales and M. E. Bowers, “Time-frequency analysis methods and their application in developmental eeg data,” Developmental Cognitive Neuroscience, vol. 54, p. 101067, 2022.
- [18] H. Adeli, Z. Zhou, and N. Dadmehr, “Analysis of eeg records in an epileptic patient using wavelet transform,” Journal of neuroscience methods, vol. 123, no. 1, pp. 69–87, 2003.

- [19] A. Subasi, “Eeg signal classiﬁcation using wavelet feature extraction and a mixture of expert model,” Expert Systems with Applications, vol. 32, no. 4, pp. 1084–1093, 2007.
- [20] H. Adeli, S. Ghosh-Dastidar, and N. Dadmehr, “A wavelet-chaos methodology for analysis of eegs and eeg subbands to detect seizure and epilepsy,” IEEE Transactions on Biomedical Engineering, vol. 54, no. 2, pp. 205–211, 2007.
- [21] N. Robinson, A. P. Vinod, K. K. Ang, K. P. Tee, and C. T. Guan, “Eegbased classiﬁcation of fast and slow hand movements using waveletcsp algorithm,” IEEE Transactions on Biomedical Engineering, vol. 60, no. 8, pp. 2123–2132, 2013.
- [22] D. Gabor, “Theory of communication. part 1: The analysis of information,” Journal of the Institution of Electrical Engineers-part III: radio and communication engineering, vol. 93, no. 26, pp. 429–441, 1946.
- [23] J. Morlet, G. Arens, E. Fourgeau, and D. Glard, “Wave propagation and sampling theory—part i: Complex signal and scattering in multilayered media,” Geophysics, vol. 47, no. 2, pp. 203–221, 1982.
- [24] J. Morlet, G. Arens, E. Fourgeau, and D. Giard, “Wave propagation and sampling theory—part ii: Sampling theory and complex waves,” Geophysics, vol. 47, no. 2, pp. 222–236, 1982.
- [25] C. Ju and C. Guan, “Tensor-cspnet: A novel geometric deep learning framework for motor imagery classiﬁcation,” IEEE Transactions on Neural Networks and Learning Systems, pp. 1–15, 2022.
- [26] N. Brodu, F. Lotte, and A. Lécuyer, “Comparative study of band-power extraction techniques for motor imagery classiﬁcation,” in 2011 IEEE symposium on computational intelligence, cognitive algorithms, mind, and brain (CCMB). IEEE, 2011, pp. 1–6.
- [27] D. J. Krusienski, D. J. McFarland, and J. R. Wolpaw, “Value of amplitude, phase, and coherence features for a sensorimotor rhythmbased brain–computer interface,” Brain research bulletin, vol. 87, no. 1, pp. 130–134, 2012.
- [28] J.-P. Lachaux, E. Rodriguez, J. Martinerie, and F. J. Varela, “Measuring phase synchrony in brain signals,” Human brain mapping, vol. 8, no. 4, pp. 194–208, 1999.
- [29] J. Müller-Gerking, G. Pfurtscheller, and H. Flyvbjerg, “Designing optimal spatial ﬁlters for single-trial eeg classiﬁcation in a movement task,” Clinical neurophysiology, vol. 110, no. 5, pp. 787–798, 1999.
- [30] H. Ramoser, J. Muller-Gerking, and G. Pfurtscheller, “Optimal spatial ﬁltering of single trial eeg during imagined hand movement,” IEEE transactions on rehabilitation engineering, vol. 8, no. 4, pp. 441–446, 2000.
- [31] R. Tomioka, K. Aihara, and K.-R. Müller, “Logistic regression for single trial eeg classiﬁcation,” Advances in neural information processing systems, vol. 19, 2006.
- [32] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K.-R. Muller, “Optimizing spatial ﬁlters for robust eeg single-trial analysis,” IEEE Signal processing magazine, vol. 25, no. 1, pp. 41–56, 2007.
- [33] F. Yger, “A review of kernels on covariance matrices for bci applications,” in 2013 IEEE International Workshop on Machine Learning for Signal Processing (MLSP). IEEE, 2013, pp. 1–6.
- [34] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Multiclass brain–computer interface classiﬁcation by riemannian geometry,” IEEE Transactions on Biomedical Engineering, vol. 59, no. 4, pp. 920–928, 2011.
- [35] M. Congedo, A. Barachant, and R. Bhatia, “Riemannian geometry for eeg-based brain-computer interfaces; a primer and a review,” BrainComputer Interfaces, vol. 4, no. 3, pp. 155–174, 2017.
- [36] A. Barachant and S. Bonnet, “Channel selection procedure using riemannian distance for bci applications,” in 2011 5th International IEEE/EMBS Conference on Neural Engineering. IEEE, 2011, pp. 348– 351.
- [37] D. Sabbagh, P. Ablin, G. Varoquaux, A. Gramfort, and D. A. Engemann, “Manifold-regression to predict from meg/eeg brain signals without source modeling,” Advances in Neural Information Processing Systems, vol. 32, pp. 7323–7334, 2019.
- [38] C. Larzabal, V. Auboiroux, S. Karakas, G. Charvet, A.-L. Benabid, S. Chabardes, T. Costecalde, and S. Bonnet, “The riemannian spatial pattern method: mapping and clustering movement imagery using riemannian geometry,” Journal of Neural Engineering, vol. 18, no. 5, p. 056014, 2021.
- [39] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Common spatial pattern revisited by riemannian geometry,” in 2010 IEEE International Workshop on Multimedia Signal Processing. IEEE, 2010, pp. 472–476.
- [40] C. Ju and C. Guan, “Deep optimal transport for domain adaptation on spd manifolds,” arXiv preprint arXiv:2201.05745, 2022.
- [41] C. Ju, R. J. Kobler, and C. Guan, “Score-based data generation for eeg spatial covariance matrices: Towards boosting bci performance,”

- 2023 45rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), 2023.
- [42] R. Kobler, J.-i. Hirayama, Q. Zhao, and M. Kawanabe, “Spd domainspeciﬁc batch normalization to crack interpretable unsupervised domain adaptation in eeg,” Advances in Neural Information Processing Systems, vol. 35, pp. 6219–6235, 2022.
- [43] Y.-T. Pan, J.-L. Chou, and C.-S. Wei, “Matt: a manifold attention network for eeg decoding,” Advances in Neural Information Processing Systems, vol. 35, pp. 31116–31 129, 2022.
- [44] C. Ju, D. Gao, R. Mane, B. Tan, Y. Liu, and C. Guan, “Federated transfer learning for eeg signal classiﬁcation,” in 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 2020, pp. 3040–3045.
- [45] E. W. Grafarend, “Optimization of geodetic networks,” The Canadian Surveyor, vol. 28, no. 5, pp. 716–723, 1974.
- [46] X. Pennec, “Statistical computing on manifolds: from riemannian geometry to computational anatomy,” in LIX Fall Colloquium on Emerging Trends in Visual Computing. Springer, 2008, pp. 347–386.
- [47] ——, “Manifold-valued image processing with spd matrices,” in Riemannian geometric statistics in medical image analysis. Elsevier, 2020, pp. 75–134.
- [48] N. Jaquier and S. Calinon, “Gaussian mixture regression on symmetric positive deﬁnite matrices manifolds: Application to wrist motion estimation with semg,” in 2017 IEEE/RSJ international conference on intelligent robots and systems (IROS). IEEE, 2017, pp. 59–64.
- [49] S. Calinon, “Gaussians on riemannian manifolds: Applications for robot learning and adaptive control,” IEEE Robotics & Automation Magazine, vol. 27, no. 2, pp. 33–45, 2020.
- [50] M. Arnaudon, F. Barbaresco, and L. Yang, “Riemannian medians and means with applications to radar signal processing,” IEEE Journal of Selected Topics in Signal Processing, vol. 7, no. 4, pp. 595–604, 2013.
- [51] S. Said, L. Bombrun, Y. Berthoumieu, and J. H. Manton, “Riemannian gaussian distributions on the space of symmetric positive deﬁnite matrices,” IEEE Transactions on Information Theory, vol. 63, no. 4, pp. 2153–2170, 2017.
- [52] O. Tuzel, F. Porikli, and P. Meer, “Region covariance: A fast descriptor for detection and classiﬁcation,” in European conference on computer vision. Springer, 2006, pp. 589–600.
- [53] H. Tabia, H. Laga, D. Picard, and P.-H. Gosselin, “Covariance descriptors for 3d shape matching and retrieval,” in Proceedings of the IEEE conference on computer vision and pattern recognition, 2014, pp. 4185– 4192.
- [54] P. T. Fletcher and S. Joshi, “Riemannian geometry for the statistical analysis of diffusion tensor data,” Signal Processing, vol. 87, no. 2, pp. 250–262, 2007.
- [55] C. Bonet, B. Malézieux, A. Rakotomamonjy, L. Drumetz, T. Moreau, M. Kowalski, and N. Courty, “Sliced-wasserstein on symmetric positive deﬁnite matrices for m/eeg signals,” in International Conference on Machine Learning. PMLR, 2023, pp. 2777–2805.
- [56] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for eeg decoding and visualization,” Human brain mapping, vol. 38, no. 11, pp. 5391–5420, 2017.
- [57] S. Sakhavi, C. Guan, and S. Yan, “Learning temporal information for brain-computer interface using convolutional neural networks,” IEEE transactions on neural networks and learning systems, vol. 29, no. 11, pp. 5619–5629, 2018.
- [58] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces,” Journal of neural engineering, vol. 15, no. 5, p. 056013, 2018.
- [59] R. Mane, E. Chew, K. Chua, K. K. Ang, N. Robinson, A. P. Vinod, S.-W. Lee, and C. Guan, “Fbcnet: A multi-view convolutional neural network for brain-computer interface,” arXiv preprint arXiv:2104.01233, 2021.
- [60] T. N. Kipf and M. Welling, “Semi-supervised classiﬁcation with graph convolutional networks,” in International Conference on Learning Representations (ICLR), 2017.
- [61] Z. Huang and L. Van Gool, “A riemannian network for spd matrix learning,” in Thirty-First AAAI Conference on Artiﬁcial Intelligence, 2017.
- [62] D. Brooks, O. Schwander, F. Barbaresco, J.-Y. Schneider, and M. Cord, “Riemannian batch normalization for spd neural networks,” Advances in Neural Information Processing Systems, vol. 32, 2019.
- [63] G. Pfurtscheller, “Functional brain imaging based on erd/ers,” Vision research, vol. 41, no. 10-11, pp. 1257–1260, 2001.
- [64] J. W. Demmel, Applied numerical linear algebra. SIAM, 1997.

- [65] R. A. Horn, R. A. Horn, and C. R. Johnson, Topics in matrix analysis. Cambridge university press, 1994.
- [66] K. K. Ang, Z. Y. Chin, H. Zhang, and C. Guan, “Filter bank common spatial pattern (fbcsp) in brain-computer interface,” in 2008 IEEE international joint conference on neural networks (IEEE world congress on computational intelligence). IEEE, 2008, pp. 2390–2397.
- [67] J. Demšar, “Statistical comparisons of classiﬁers over multiple data sets,” The Journal of Machine learning research, vol. 7, pp. 1–30, 2006.
- [68] U. Von Luxburg, “A tutorial on spectral clustering,” Statistics and computing, vol. 17, no. 4, pp. 395–416, 2007.
- [69] M. Hein, J.-Y. Audibert, and U. v. Luxburg, “From graphs to manifolds– weak and strong pointwise consistency of graph laplacians,” in International Conference on Computational Learning Theory. Springer, 2005, pp. 470–485.
- [70] A. Singer, “From graph to manifold laplacian: The convergence rate,” Applied and Computational Harmonic Analysis, vol. 21, no. 1, pp. 128– 134, 2006.
- [71] M. Belkin and P. Niyogi, “Towards a theoretical foundation for laplacianbased manifold methods,” Journal of Computer and System Sciences, vol. 74, no. 8, pp. 1289–1308, 2008.
- [72] M. M. Bronstein, J. Bruna, Y. LeCun, A. Szlam, and P. Vandergheynst, “Geometric deep learning: going beyond euclidean data,” IEEE Signal Processing Magazine, vol. 34, no. 4, pp. 18–42, 2017.
- [73] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and S. Y. Philip, “A comprehensive survey on graph neural networks,” IEEE transactions on neural networks and learning systems, vol. 32, no. 1, pp. 4–24, 2020.
- [74] I. Chami, Z. Ying, C. Ré, and J. Leskovec, “Hyperbolic graph convolutional neural networks,” Advances in neural information processing systems, vol. 32, 2019.
- [75] S. Zhu, S. Pan, C. Zhou, J. Wu, Y. Cao, and B. Wang, “Graph geometry interaction learning,” Advances in Neural Information Processing Systems, vol. 33, pp. 7548–7558, 2020.
- [76] J. Dai, Y. Wu, Z. Gao, and Y. Jia, “A hyperbolic-to-hyperbolic graph convolutional network,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2021, pp. 154–163.
- [77] S. Boyd, S. P. Boyd, and L. Vandenberghe, Convex optimization. Cambridge university press, 2004.
- [78] G. Bécigneul and O.-E. Ganea, “Riemannian adaptive optimization methods,” International Conference on Learning Representations, 2018.
- [79] M. Kochurov, R. Karimov, and S. Kozlukov, “Geoopt: Riemannian optimization in pytorch,” 2020.
- [80] P.-A. Absil, R. Mahony, and R. Sepulchre, “Optimization algorithms on matrix manifolds,” in Optimization Algorithms on Matrix Manifolds. Princeton University Press, 2009.
- [81] D. J. Krusienski, D. J. McFarland, J. C. Principe, and E. Wolpaw, “Bci signal processing: feature extraction,” Brain-Computer Interfaces: Principles and Practice, eds JR Wolpaw and EW Wolpaw (New York, NY: Oxford University Press), pp. 123–146, 2012.

