# arXiv:2407.20250v1[eess.SP]19Jul2024

## RIEMANNIAN GEOMETRY-BASED EEG APPROACHES: A LITERATURE REVIEW

A PREPRINT

Imad Eddine Tibermacine1 Samuele Russo2 Ahmed Tibermacine3

Abdelaziz Rabehi4 Bachir Nail4 Kamel Kadri5 Christian Napoli1,6,7

- 1Department of Computer, Automation and Management Engineering, Sapienza University of Rome, Rome, Italy {tibermacine@diag.uniroma1.it, cnapoli@diag.uniroma1.it}
- 2Department of Psychology, Sapienza University of Rome, Rome, Italy {samuele.russo@uniroma1.it}
- 3Department of Computer Science, University of Biskra, Biskra, Algeria {ahmed.tibermacine@univ-biskra.dz} 4Faculty of Science and Technology, University of Djelfa, Djelfa, Algeria {abdelaziz.rabehi@univ-djelfa.dz, bachir.nail@univ-djelfa.dz} 5Polytechnic Military School, Algiers, Algeria {dr.kadri.kamel@gmail.com } 6Institute for Systems Analysis and Computer Science, Italian National Research Council, Italy 7Department of Computational Intelligence, Czestochowa University of Technology, Poland

### ABSTRACT

The application of Riemannian geometry in the decoding of brain-computer interfaces (BCIs) has swiftly garnered attention because of its straightforwardness, precision, and resilience, along with its aptitude for transfer learning, which has been demonstrated through significant achievements in global BCI competitions. This paper presents a comprehensive review of recent advancements in the integration of deep learning with Riemannian geometry to enhance EEG signal decoding in BCIs. Our review updates the findings since the last major review in 2017, comparing modern approaches that utilize deep learning to improve the handling of non-Euclidean data structures inherent in EEG signals. We discuss how these approaches not only tackle the traditional challenges of noise sensitivity, non-stationarity, and lengthy calibration times but also introduce novel classification frameworks and signal processing techniques to reduce these limitations significantly. Furthermore, we identify current shortcomings and propose future research directions in manifold learning and riemannian-based classification, focusing on practical implementations and theoretical expansions, such as feature tracking on manifolds, multitask learning, feature extraction, and transfer learning. This review aims to bridge the gap between theoretical research and practical, real-world applications, making sophisticated mathematical approaches accessible and actionable for BCI enhancements.

Keywords EEG · Riemannian Geometry · Deep Learning · Classification

### 1 Introduction

Brain-computer interfaces [9] revolutionize the field of human-machine interactions by enabling direct communication pathways between the brain and external devices, bypassing traditional muscular outputs[1]. Predominantly, BCIs utilize electroencephalography (EEG) due to its cost-effectiveness and minimal computational demands[2]. EEG-based BCIs convert brain activity, measured through EEG signals, into computer commands, leveraging classification algorithms like the common spatial pattern (CSP) to recognize signal patterns associated with specific brain activities such as motor imagery[3]. Despite their promise, EEG-based BCIs face critical challenges including high signal variability, noise, non-stationarity, and the high dimensionality of data spaces[4].

The domain of BCI has expanded its utility beyond basic research, offering profound applications in rehabilitation, assistive technologies, and adaptive human-computer interfaces that respond to the user’s mental states[5]. Yet, despite these advancements, BCIs are predominantly still in the prototype stage, rarely deployed outside laboratory settings due to their low robustness and the extensive calibration required for each user[6]. Current BCIs suffer from poor reliability, often misinterpreting user commands, which significantly reduces accuracy and information transfer rates even under controlled conditions[7]. This sensitivity to environmental noise and the inherent non-stationarity of EEG signals further complicates their practical application[8].

In the rapidly evolving field of BCIs, deep learning has emerged as a transformative force, enabling sophisticated methods for classifying EEG data[10]. These advancements hold the promise of revolutionizing the interaction between humans and machines by interpreting neural activities directly through EEG signals[11]. Despite these advances, the development of BCIs faces significant challenges, notably the limited availability of large, annotated training datasets, which are crucial for training robust deep learning models[12]. In response, researchers have increasingly turned to generative modeling, a burgeoning area within machine learning, to augment existing datasets through the synthesis of synthetic EEG data[13]. This approach not only enhances the diversity of training examples but also addresses the gap caused by scarce data resources[14].

Achieving practical usability of BCIs requires that they be robust across different contexts, users, and over time, all while maintaining minimal calibration requirements[15][24]. Addressing these multifaceted challenges necessitates a comprehensive strategy: identifying new, reliable neurophysiological markers at the neuroscience level[16]; improving user training to stabilize EEG pattern generation at the human interaction level[17]; and advancing signal processing techniques to enhance feature extraction[18] and classifier robustness at the computational level[19][25]. Prominently, the application of Riemannian geometry[20] to handle EEG covariance matrices has shown considerable promise[21]. This geometric approach not only accommodates the non-Euclidean characteristics of EEG data but also leverages the intrinsic geometric properties of these data to enhance classification accuracy[22][23].

Traditional approaches like Fourier analysis[26] frequently fail due to the inherently nonstationary nature of EEG signals. This limitation has paved the way for the adoption of time-frequency analysis techniques, such as the wavelet transform, which are now being integrated with spatial filtering[27] methods like the CSP to improve the localizability of rhythmic EEG components. Such advancements are critical for enhancing the efficacy of motor imagery (MI) EEG classifiers, which are vital for real-time BCI applications[28].

Moreover, a significant aspect of reducing signal variability and enhancing classifier performance in BCIs[29] involves focusing on covariance matrices, typically handled as elements within Euclidean spaces. However, considering these matrices in their naturally occurring Riemannian manifold[30], which better reflects their symmetric and positive definite (SPD) properties[31], can substantially optimize the computational processes. Techniques such as Principal Components Analysis (PCA)[32] and Canonical Correlation Analysis (CCA)[33] have traditionally exploited covariance estimates for spatial filtering in BCIs[34]. By refining how these matrices are treated—acknowledging their Riemannian structure—we can significantly enhance the spatial and temporal resolution of EEG signal analysis[35].

This paper presents a detailed review focused on the applications of Riemannian Geometry and deep learning-based Riemannian geometry in the domains of BCIs and EEG. We explore how these advanced methodologies enhance BCI design by addressing core challenges inherent in traditional systems. Our discussion extends to the integration of geometric deep learning with generative modeling and sophisticated signal processing techniques. We propose new research directions and outline strategic advancements necessary for developing BCIs that are not only efficacious in controlled settings but also robust and accessible for practical, everyday applications.

### 2 Brain-Computer Interface

Brain-computer interfaces that utilize oscillatory neural activity are a significant branch of non-invasive systems for neurocommunication and control[36]. These interfaces typically leverage the modulation of brain rhythms captured via EEG, and are commonly employed in motor imagery-based BCIs[37]. Such BCIs extensively use the CSP algorithm combined with Linear Discriminant Analysis for signal classification, making them highly effective for decoding user intentions based on neural activity patterns[38].

The CSP algorithm is pivotal for maximizing the variance of signals from one mental state while simultaneously minimizing it for another[39]. This is achieved by designing spatial filters that enhance the discriminability between two contrasting classes of brain activity. Mathematically, the optimization of CSP filters, represented as column vectors w, is framed as an eigenvalue problem aimed at maximizing the following objective function:

wTC1w wTC2w

JCSP(w) =

(1)

Here, C1 and C2 are the averaged covariance matrices of the EEG signals filtered for two different classes, which are computed as:

Nj

Nj

1 Nj

1 Nj

Sij =

Zij(Zij)T (2)

Cj =

i=1

i=1

where Nj is the number of trials for class j, and Zij represents the i-th trial from class j matrix in a channel-filtered EEG dataset[40].

The CSP algorithm essentially reduces the multi-channel EEG data into a lower-dimensional space[41], where the spatial filters w corresponding to the largest (or smallest) eigenvalues capture the most (or least) discriminative features of the EEG signals.

Upon obtaining the optimal spatial filters, the transformed feature fi for each trial is calculated using:

fi = log(wTSiw) (3)

where Si is the covariance matrix of the current trial. These logarithmically transformed variances are then fed into an LDA classifier, which constructs a hyperplane to distinguish between the classes by solving:

- 1

- 2

a = C−1(µ1 − µ2), b = −

(µ1 + µ2)Ta (4)

where µ1 and µ2 are the mean feature vectors of each class, and C is the pooled covariance matrix of the features. LDA assumes Gaussian class conditional densities with equal covariance matrices for both classes[42], which simplifies the computation of the decision boundaries[43][44].

It is crucial to note that while CSP and LDA provide a robust framework for feature extraction and classification[45], their efficacy depends on accurately estimated covariance matrices, which require sufficient trial data to avoid overfitting. Moreover, the assumption of linear separability[46] by LDA may not always hold in complex brain activity patterns, suggesting the need for more sophisticated nonlinear classifiers or deep learning approaches in more advanced BCI systems[47][48].

The mathematical rigor involved in optimizing CSP and employing LDA classifiers in oscillatory activity-based BCIs[49] showcases the intricate balance between statistical assumptions and practical EEG data characteristics[50]. Enhancements in computational strategies and model robustness are continually evolving, aiming to improve the adaptability and accuracy of BCIs in real-world applications[51].

### 3 Riemannian Geometry Concepts

In this section, we introduce the mathematical notations and basic definitions fundamental to our study on EEG preprocessing. Scalars are denoted by lowercase letters (e.g., a), vectors by boldface lowercase (e.g., v), representing column vectors unless stated otherwise, matrices by boldface uppercase (e.g., M), and tensors of order three or higher by Euler script letters (e.g., T ). The space Rn represents the n-dimensional real vector space, and Rn×n denotes all n × n real matrices. Vector en, comprising all ones, belongs to Rn, and In denotes the identity matrix in Rn×n. For any vector x, the matrix diag(x) refers to a diagonal matrix with the elements of x on its main diagonal.

We denote by vec(A) the operation that converts a matrix A into a vector by stacking its columns. In the special case where A is symmetric, the vectorization vec(A) is defined such that it takes only the unique entries due to symmetry. The norms ∥ · ∥p and ∥ · ∥F correspond to the Lp and Frobenius norms of a vector or matrix, respectively.

- Definition 1.1. A matrix A ∈ Rn×n is deemed Symmetric Positive Definite (SPD) if it holds that A = AT and xTAx > 0 for all non-zero vectors x ∈ Rn. The eigenvalues of such a matrix A, denoted by λ(A), are guaranteed to be positive.
- Definition 1.2. A matrix A is considered orthogonal if its columns comprise an orthogonal unit vector set, implying ATA = In.
- Definition 1.3. The exponential and logarithmic functions of a matrix A ∈ Rn×n, denoted by exp(A) and log(A), are defined through its eigenvalue decomposition. If A is expressible as Udiag(λ1,...,λn)UT, where U is orthogonal and λi are the eigenvalues of A, then:

##### exp(A) = Udiag(exp(λ1),...,exp(λn))UT, (5) log(A) = Udiag(log(λ1),...,log(λn))UT. (6)

[Figure 1]

Figure 1: The SPD Manifold pipeline[76]

A manifold, in the simplest terms, refers to a space that, at a local level, resembles the Euclidean space of dimension n, known as Rn. This property of local similarity to Rn qualifies it as a topological manifold [52]. When such a space is equipped with a differential structure, it ascends to become a differentiable manifold, thereby enabling the attachment of a tangent space at any point [53]. The tangent space encapsulates all potential vectors that are tangential to any conceivable curve passing through that point on the manifold.

Within the manifold paradigm, a Riemannian manifold stands out as a differentiable manifold that is further enhanced with a smoothly varying inner product on its tangent spaces, constituting the Riemannian metric tensor [54]. This metric tensor facilitates the measurement of angles between vectors within the same tangent space, the magnitude of vectors, and the distance between vectors. It allows for the calculation of curve lengths on the manifold, including the geodesic distance which is the shortest distance between two points on the manifold determined by the paths of curves [55].

Considering M as a Riemannian manifold and TXM as its tangent space at point X, for any two vectors V,W ∈ TXM, the Riemannian metric gX(V,W) provides the inner product [56]. When discussing the manifold of SPD matrices, our focus is particularly on the tangent space TXM and the Riemannian metric at that point.

For a smooth curve γ : [0,1] → M, parametrized with respect to a metric on M, there are numerous ways to describe its trajectory, each with a different speed of traversal. Of particular interest are those curves that are parametrized by arc length, termed naturally parametrized curves [57]. These curves progress with a uniform rate and are defined in relation to the Riemannian metric. The curve’s length from γ(0) to γ(1) is computed by integrating the metric-induced velocity along the curve.

For two distinct points X1,X2 ∈ M, and a naturally parametrized curve γ that connects these points with γ(0) = X1 and γ(1) = X2, the length L(γ) of this curve is expressed by the integral[52]:

L(γ) =

1

0

gγ(t)(˙γ(t),γ˙(t))dt (7)

The optimal path on a manifold that minimizes the distance between two points is called a geodesic. While geodesics represent the paths of least distance, they are uniquely characterized by a uniform rate of traversal and are not necessarily the shortest paths for manifolds that are not simply connected. These paths, particularly on a spherical surface, might have multiple representations, such as the numerous geodesics connecting the poles [55]. The distance along a geodesic, known as the Riemannian distance between two points X1 and X2, is essential in determining the manifold’s completeness. Here, we concentrate on manifolds that are geometrically complete [54].

The tangent space at point X on a manifold M, denoted TXM, acts as a local linear approximation to M within a specific region around X, usually within a certain radius allowing for a bijection via the exponential map [58]. For every point X′ within this neighborhood, the exponential map is the bridge connecting X′ to X through a unique geodesic.

For any smooth scalar function f defined on M, the Riemannian gradient at X is given as ∇f(X) in the direction that maximizes the rate of increase of f. If γ is a geodesic with γ(0) = X and γ˙(0) = V , then ∇f ◦ γ describes the change of f along γ, and ∇f(X) is that vector in TXM such that the inner product ⟨V,∇f(X)⟩ equals the derivative of f along the curve at t = 0, defined as[58]:

⟨V,∇f(X)⟩ =

d dt

f(γ(t))

. (8)

t=0

The Riemannian gradient facilitates the computation of directional derivatives on manifolds, linking classical differential calculus to the geometry of the manifold. The exponential map, denoted as ExpX : TXM → M, projects a tangent vector at X onto M, and conversely, the logarithm map, or LogX, maps points back to TXM, providing a method to traverse between a tangent space and its manifold [59].

Assigning a set M of square matrices the structure of a Riemannian manifold incorporates a local Euclidean geometry, thereby enriching it with a rigorous mathematical underpinning. Suppose we have M′ ∈ M, a manifold of dimension K, and ξM′ = M′ − M representing a tangent vector at M. This vector is part of a higher-dimensional tangent space TMM associated with M.

The inner product defined by the Riemannian metric on TMM × TMM → R induces a norm on the tangent space, given by ∥ξM′∥M = ⟨ξM′,ξM′⟩M, and facilitates the computation of geodesic distances d(M,M′) on M [59]. These distances enable the formulation of mean values of points on the manifold as:

Mean({M1,...,MN}) = arg min

M∈M

N

d(M,Mi)2. (9)

i=1

The exponential mapping at M in M, denoted as ExpM, and its inverse, the logarithm mapping LogM, are both essential in preserving the manifold’s structure, especially when mapping to and from the tangent space. ExpM(ξM) approximates M′ when ξM is small, and the distance between M and M′ is given by the norm of ξM in RK via LogM. This relationship allows the introduction of vectorization for M, PM : M → RK, defined as PM(M′) = ϕ(LogM(M′)) [59].

For a compact subset of M where the matrices {Mi} lie, the mean M can be approximated, resulting in a simplified geodesic distance expression:

d(M,M′) ≈ ∥PM(M) − PM(M′)∥. (10)

In the realm of regression on manifolds, the vectorization PM is pivotal for leveraging machine learning algorithms. It adapts matrix points in M onto RK, facilitating their use in regression techniques that typically assume a Euclidean

data structure. For instance, with a collection {Mi} and corresponding response variables {yi}, one first computes the mean of the samples M and applies vectorization to obtain {vi}. Linear regression methods, such as ridge regression, can then be applied, presupposing a linear relationship yi ≈ viTβ, with β representing the regression coefficients [60].

#### 3.1 The Covariance Matrix of EEG

Consider X ∈ RM×T, representing an EEG signal that has undergone band-pass filtering, where M denotes the number of channels and T represents the number of temporal samples. To analyze the statistical properties of the EEG signal, we construct the covariance matrix P as follows:

1 T − 1

#### XXT (11)

P =

This matrix P is not only symmetric but also empirically confirmed to be SPD, encapsulating important statistical information about the EEG signals. The symmetry of P arises because (XXT)T = XXT, and it attains its positivedefiniteness under the condition that X has full row rank, which is typically satisfied if T > M and the EEG data are sufficiently diverse [61].

Properties of Symmetric Positive-Definite Matrices: A matrix A ∈ Rn×n is deemed positive-definite if for any non-zero vector v ∈ Rn, it holds that:

vTAv > 0 (12) Applying this to our covariance matrix P[62], we observe:

1 T − 1

1 T − 1∥XTv∥2 > 0 (13)

vTPv = vT

XXT v =

where ∥XTv∥ represents the Euclidean norm of XTv, which is greater than zero unless v is orthogonal to all rows of X. This ensures that P retains all the characteristics of an SPD matrix, including its utility in defining a metric space on the manifold of such matrices [63].

Geometric Interpretation in EEG Analysis: As an element of the manifold of SPD matrices, P can be further analyzed using tools of Riemannian geometry. The diagonal elements of P represent the variance of the filtered EEG signal at each channel, indicating the power spectrum. The off-diagonal elements provide a measure of covariance between different channels, reflecting how signal components vary together over time—a crucial aspect for understanding functional connectivity in the brain [64]. Distances between such matrices, computed via geodesic paths on this manifold, offer a natural measure of similarity between different EEG states or conditions, enhancing applications like classification and clustering in brain-computer interfaces [63].

Incorporating these mathematical insights enriches our understanding of how the covariance matrix functions within EEG signal analysis and underscores the significance of employing a Riemannian framework to advance analytical capabilities.

#### 3.2 Riemannian Metrics on SPD Manifolds

The choice of Riemannian metric on the manifold of SPD matrices significantly influences the analysis and processing of data represented by these matrices, such as EEG signals. The Log-Euclidean Metric (LEM) and the Affine-Invariant Metric (AIM) are two predominant metrics used in this context [63, 65].

Log-Euclidean Metric (LEM): The Log-Euclidean Metric (LEM) offers an efficient and robust computational method for handling the manifold of SPD matrices. This metric is particularly valued for preserving the bi-invariance property within the Lie group structure of SPD matrices, making it suitable for various applications, including image processing and medical imaging analysis, where maintaining the structure of data during transformations is crucial [65].

Under the LEM, the geodesic distance between two points P1 and P2 on the manifold of SPD matrices is defined as:

δL(P1,P2) = ∥Log(P1) − Log(P2)∥F, (14)

where Log denotes the matrix logarithm, transforming matrices to a space where the Euclidean tools can be applied. The norm ∥ · ∥F represents the Frobenius norm, which measures matrix entries’ absolute differences, thus providing a natural distance metric in the logarithmic domain [65].

The Log-Euclidean mean of a set of matrices, crucial for statistical analysis on manifolds, is calculated using:

G = Exp

k

1 k

Log(Pi) , (15)

i=1

This formulation allows the mean of matrices to be computed efficiently and without the convergence issues that may arise with other Riemannian metrics. Additionally, when considering a weighted mean where each matrix Pi is assigned a weight wi, fulfilling the conditions ki=1 wi = 1 and wi > 0, the weighted mean is given by:

G = Exp

k

wi Log(Pi) . (16)

i=1

Affine-Invariant Metric (AIM): The AIM is another highly regarded metric for SPD manifolds, especially valued for its invariant properties under affine transformations. The geodesic distance under this metric between P1 and P2 is computed as:

δA(P1,P2) = Log(P1−1/2P2P1−1/2)

, (17)

F

reflecting the minimal invariant distance under congruent transformations [63]. The mean under AIM, often used for central tendency estimation in statistics on manifolds, does not have a closed-form solution and is typically computed numerically [66].

#### Other Important Riemannian Metrics:

- 1. Fisher-Rao Metric: Originally developed in the context of information geometry, the Fisher-Rao metric has been adapted to the geometry of SPD manifolds. It provides a statistical interpretation of the distance, correlating with the intrinsic curvature of the data space, making it suitable for probabilistic interpretations of data [67].
- 2. Cholesky Decomposition-based Metric: This metric leverages the Cholesky decomposition of SPD matrices, enabling an alternative parametrization of the manifold. It simplifies certain computational procedures, particularly in optimization contexts, by linearizing the manifold using lower triangular matrices [68].
- 3. Procrustes Metric: Focused on shape analysis, the Procrustes metric measures the similarity between shapes after transformations like translation, scaling, and rotation. When adapted to SPD matrices, it helps analyze shape changes in data structures characterized by these matrices [60].

Each of these metrics offers unique advantages depending on the specific requirements of the application, such as computational efficiency, robustness to transformations, or interpretability in statistical analysis. Choosing the appropriate metric is crucial for effectively analyzing and interpreting the geometric structure of data residing on SPD manifolds.

#### 3.3 Tangent Space at a Point on a Manifold

The concept of tangent space is central to understanding the local geometry of manifolds and plays a critical role in the analysis of data that lie on these manifolds, such as covariance matrices of EEG signals. A tangent space at a point on a manifold provides a linear approximation of the manifold near that point, facilitating operations like vector addition and scalar multiplication which are not inherently defined on the manifold itself [52].

Let M be a smooth manifold and p a point on M. The tangent space to M at p, denoted as TpM, is a vector space consisting of the tangent vectors to all possible curves through p on the manifold. Formally, if γ : (−ϵ,ϵ) → M is a smooth curve with γ(0) = p, then the derivative γ′(0), which represents the velocity vector of γ at p, is a tangent vector at p [53].

For practical computation, particularly in applications involving SPD matrices, we express tangent vectors in coordinates. If M is parameterized locally around p by a coordinate system ϕ : U ⊂ Rn → M, where U is an open set in Rn, the tangent vectors can be expressed as:

n

∂ ∂xi p

vi

(18)

v =

i=1

[52].

where vi are components of v in the coordinate basis ∂x ∂i

p

In the context of SPD matrices, which form an open subset of the space of symmetric matrices, the tangent space at any point P ∈ SPD(n) can be identified with the space of symmetric matrices. If P is an SPD matrix and S is a symmetric matrix, then a curve on SPD(n) passing through P with direction S at t = 0 can be represented as:

γ(t) = P1/2 exp(tP−1/2SP−1/2)P1/2 (19)

where exp denotes the matrix exponential. The derivative of this curve at t = 0 gives a tangent vector at P, which is precisely S [63].

Understanding the tangent space of SPD matrices is crucial for developing algorithms in EEG signal processing. For example, the process of projecting EEG covariance matrices onto the tangent space allows for the linearization of the manifold structure, simplifying computations such as averaging or classification. This projection involves mapping SPD matrices to their tangent spaces at a chosen reference point, usually the mean covariance matrix, and performing linear operations in this vector space before projecting back to the manifold [69].

#### 3.4 Geodesic Distances on Riemannian Manifolds

An SPD matrix of size M × M resides on a manifold denoted as P(M), characterized by its smooth and curved structure. On such Riemannian manifolds, the concept of geodesics plays a crucial role in understanding and quantifying the intrinsic geometric properties of the space [70].

[Figure 2]

Figure 2: Illustration of the gradient descent algorithms on the Riemannian product manifold[125].

Geodesics are the generalization of "straight lines" to Riemannian manifolds and represent the shortest path between two points on the manifold. Mathematically, a geodesic γ(t) on a manifold M satisfies the geodesic equation:

∇γ˙(t)γ˙(t) = 0, (20)

where ∇ denotes the Levi-Civita connection associated with the manifold’s Riemannian metric, and γ˙(t) is the tangent vector to γ at t. This equation ensures that the acceleration of γ is zero, signifying that the path has no deviation other than what is necessary to remain on the manifold [54].

To compute a geodesic path under the Log-Euclidean framework, one uses the exponential and logarithmic maps. For matrices P1 and P2, the geodesic connecting them can be parameterized as:

γ(t) = Exp((1 − t)Log(P1) + tLog(P2)) (21)

for t ∈ [0,1], where Exp is the matrix exponential. This expression provides an explicit parametric form for the geodesic, connecting two points on the manifold in a manner that respects the curvature and topological constraints [65].

The curvature of the manifold, which affects the shape of geodesics, can be quantified through the Riemann curvature tensor R, defined by:

R(X,Y )Z = ∇X∇Y Z − ∇Y ∇XZ − ∇[X,Y ]Z (22) for vector fields X,Y, and Z. The curvature informs us about how the metric space bends locally and impacts geodesic deviation [70].

The ability to measure and analyze distances between EEG covariance matrices using geodesics[71] is invaluable for tasks such as classification and clustering within brain-computer interfaces[72]. Understanding the manifold’s geometric structure[73] allows for more nuanced insights into brain connectivity patterns and functional dynamics, facilitating advanced neuroscientific analyses[74][75].

### 4 Riemannian Geometry-Based EEG Approaches

This article presents a synthesis of discoveries from a meticulously curated collection of 42 publications, manually chosen based on their pertinence to the fusion of Riemannian geometry and deep learning in brain-computer interfaces (BCIs). The selection of articles was made through a focused exploration conducted on Google Scholar and PubMed. The exploration, executed with the objective of encompassing the most recent and pertinent research up to May 3rd, 2024, utilized a search query formulated as: (“Riemannian geometry” OR “manifold learning” Or “SPD Manifolds”) AND (“brain computer interface” OR “EEG”). This curation procedure encompassed both peer-reviewed publications and preprints, ensuring a thorough incorporation of the newest advancements and dialogues in the domain.

To furnish a structured and comprehensive analysis of the vast body of literature concerning the utilization of Riemannian geometry in brain-computer interfaces, the chosen studies have been classified into five distinct domains: Feature Extraction, Classification, Manifold Learning, Tangent Space Methods, and Transfer Learning. This classification was selected to mirror the foundational phases of BCI signal processing and the specific obstacles that each phase poses. The core elements of BCI systems are encapsulated in feature extraction and classification, with a focus on extracting meaningful patterns from raw EEG data and subsequently utilizing these patterns for making predictions or decisions. Manifold learning and tangent space methods are segregated due to their significance in addressing the intrinsic non-Euclidean nature of EEG data, enabling a more intricate examination of how Riemannian geometry can enhance these procedures. Notably, transfer learning is delineated as a distinct category owing to its escalating importance in augmenting the adaptability and efficiency of BCIs across various subjects and sessions, showcasing the pragmatic implications of Riemannian techniques in real-world scenarios.

Table 1: Overview of the reviewed related works Category Papers Feature Extraction [104],[109],[90],[117] Classification Approaches [94],[80],[79],[98],[85],[123],[122],[77],[102],[101],[91],[116],[113] Manifold Learning [83],[82],[86],[87],[96],[86],[97] ,[115],[124],[100],[99],[106] Tangent Space Approaches [108],[93],[92],[95],[81],[119],[78] Transfer Learning Approaches [84],[110],[107],[89],[114]

#### 4.1 Feature Extraction Methods

Feature extraction is a SOTA necessary step after collecting EEG data. It allows reducing the dimensionality of the data and making it more comprehended by machine learning and deep learning models. Various studies have explored the use of Riemannian geometry for feature extraction and discriminant analysis in EEG-based BCIs. In [104], the authors used Covariance Matrices as EEG Signal Descriptors and exploring various dissimilarity metrics on SPD matrices and introducing a novel feature, HORC, which combines different relevance matrices under a tensor framework for improved classification accuracy. A Riemannian Spatial Pattern (RSP) method was proposed in [109] to extract spatial patterns from Riemannian classification for motor imagery tasks. The RSP method uses a backward channel selection procedure and compares it with the Common Spatial Pattern (CSP) approach. The RSP method provides precise mapping and clustering of imagined motor movements, which is especially useful in differentiating finger flexions. The spatial pattern extraction can be described using:

N

1 N

xixTi (23)

C =

i=1

where C is the covariance matrix, and xi represents the EEG signals.

Huang et al. [90] introduce the Common Amplitude-Phase Measurement (CAPM) method, designed to simultaneously analyze the amplitude and phase information of EEG signals on a Riemannian manifold. This dual consideration promises to enhance classification accuracy for BCI applications significantly. The initial step involves extracting the amplitude and phase from EEG signals using the wavelet transform, specifically applying a complex Morlet wavelet. The transformation is mathematically represented as:

xˆc(t,f) = xc(t) ∗ ψ(t,f) = ac(f,t)eiθ

c(f,t) (24)

- where xˆc(t,f) denotes the complex signal representation at channel c, time t, and frequency f. Here, ac(f,t) is the amplitude, θc(f,t) represents the phase, and ψ(t,f) is the Morlet wavelet function. To dimensionally reduce while preserving discriminative features, the authors devise a Riemannian graph embedding technique. The adjacency matrix S, based on the Riemannian distance between the SPD covariance matrices of EEG trials, is defined by:

exp −δ

σ , if Yn ∈ Cz(Yr) and Yr ∈ Cz(Yn) 0, otherwise

nr

(25) where δnr is the Riemannian distance between covariance matrices Pn and Pr:

snr =

δnr = δR(Pn,Pr) = log(Pn−1Pr) =

L

log2 βl

l=1

1/2

(26)

The low-dimensional data Yˆn is used to compute a new covariance matrix Pˆn = WHPnW. Classification is performed using the Minimum Distance to Riemannian Mean (MDRM):

 

1/2  (27)

1/2

M

M

log2 ηm

log2 ρm

zn = sign

−

m=1

m=1

where ηm and ρm are the eigenvalues of Pˆ−−11Pˆn and Pˆ+1−1Pˆn respectively. A regularized linear regression model is then applied to optimize the classification parameter b:

- 1

- 2 ∥z − Db∥2 + λ(1 − α)∥b∥22 + λα ∥b∥1 (28)

min

b

where D is the matrix of input vectors dn and z is the corresponding label vector.

The CAPM method effectively captures the intrinsic amplitude and phase information of EEG signals, optimizing the spatial-spectral filters and enhancing classification performance through Riemannian geometry-based regularization. Experimental results demonstrate significant improvements in classification accuracy on BCI competition datasets.

Gurve et al. [117] proposed a framework for classifying motor imagery EEG data using covariance matrices as descriptors and investigating various dissimilarity metrics on the manifold of SPD matrices. The study compares the performance of Log-Euclidean distance, Stein divergence, Kullback–Leibler divergence, and Von Neumann divergence for classification. Additionally, the paper introduces a new feature, Heterogeneous Orders Relevance Composition (HORC), combining different relevance matrices (Covariance, Mutual Information, or Kernel Matrix) under a tensor framework and multiple kernel fusion. The framework is further refined using Neighborhood Component Feature Selection (NCFS) to optimize the feature subset.

- [117] also introduced a method to improve MI classification performance by employing Non-negative Matrix Factorization (NMF) for EEG channel selection and using the Riemannian geometry of covariance matrices for feature extraction. The method reduces the dimensionality of the EEG data, mitigates overfitting, and enhances classification accuracy by selecting subject-specific channels. The NMF is used to decompose the covariance matrix as follows:

##### C ≈ WH (29)

where C is the covariance matrix, and W and H are non-negative matrices. The neighborhood component feature selection (NCFS) algorithm is then applied to select the most important features, further refined by:

Dw(fi,fj) = wk2|fik − fjk| (30)

where wk is the weighting vector for the k-th feature. These studies collectively advance the application of Riemannian geometry in EEG feature extraction and discriminant analysis, offering improved accuracy, robustness, and computational efficiency in BCI systems.

#### 4.2 Classficiation Approaches

Recent approaches of BCI classification have notably shifted from traditional Euclidean metrics to employing Riemannian geometry, better reflecting the complex data structures. [94] and [80] demonstrated the use of Riemannian distance-based kernels within SVMs to significantly enhance classification accuracy for motor imagery tasks, surpassing traditional methods without extensive spatial filtering. Similarly, [79] documents substantial performance improvements in steady-state visually evoked potential (SSVEP) classification by aligning methods more closely with intrinsic data geometry. The integration of Riemannian geometry with decision tree frameworks in [98] improves classification by capturing non-linear data relationships. Additionally, [85] introduces an expectation-maximization algorithm for robust covariance estimation in the presence of incomplete EEG data, outperforming traditional imputation techniques. Furthermore, [123] develops new Riemannian geometry-based metrics to monitor and enhance user performance during BCI training, ensuring a more accurate and reliable progress assessment.

The work [122] explores the application of graph neural networks (GNNs) on SPD manifolds to classify motor imagery EEG signals. This approach leverages the time-frequency characteristics of EEG data, which are represented on SPD manifolds. The mathematical formulation involves constructing a graph where each node represents an EEG channel,

and edges are weighted by a function of the Riemannian distance between SPD matrices. The SPD matrices are derived from the covariance of time-frequency representations of the EEG signals, capturing both spatial and spectral information.

The key mathematical components include the computation of the Riemannian distance between two SPD matrices Σ1 and Σ2:

δR(Σ1,Σ2) = log(Σ−1 1/2Σ2Σ−1 1/2)

, (31)

F

where log denotes the matrix logarithm and ∥·∥F is the Frobenius norm. This distance metric is crucial for defining the weights of the edges in the graph neural network, ensuring that the intrinsic geometry of the data is preserved.

The GNN model processes the SPD matrices using graph convolutional layers specifically designed for manifold-valued data. Let G = (V,E) be a graph with vertices V corresponding to EEG channels and edges E weighted by the Riemannian distance. The signal at each vertex v is represented by an SPD matrix Σv. The graph convolution operation on SPD manifolds is defined as:

##### H(l+1) ← RBN ReEig W(l) D ˜−1A˜ H(l)W(l)T (32)

where H(l) is the feature matrix at layer l, W(l) is the trainable weight matrix, N(v) denotes the neighbors of vertex v, and σ is a non-linear activation function. This operation ensures that the convolution respects the manifold structure of the data.

[113] describes a method that combines Independent Component Analysis (ICA) with Riemannian geometry to enhance emotion recognition from EEG signals; this involves projecting covariance matrices onto the Riemannian manifold and integrating these features into a deep learning model, resulting in superior performance compared to traditional methods. Similarly, [77] applies Riemannian geometry decoding algorithms to large-scale EEG datasets, where the baseline minimum distance to Riemannian mean approach yields the highest classification accuracy for motor imagery and execution tasks, underscoring the scalability of these methods. Additionally, [102] explores the feasibility of imagined speech classification using EEG signals, employing covariance matrix descriptors on the Riemannian manifold with a relevance vector machine classifier to achieve high accuracy, revealing promising potential for BCI applications in speech imagery.

In the paper [101] the authors propose a novel brain-ventilator interface (BVI) framework that detects patient-ventilator disharmony from EEG signals. This work leverages the spatial covariance matrices of EEG signals and utilizes Riemannian geometry to classify different respiratory states. The approach is robust against the non-stationarity and noise inherent in EEG signals. Mathematically, the framework involves calculating the spatial covariance matrix C for the EEG signals, which is SPD. The Riemannian mean Ck of these matrices is computed using:

Ck = argC min

Ci∈Sk

d(C,Ci) (33)

The features are then projected onto the tangent space using the logarithmic map:

logQ(P) = SQ = Q1/2logm(Q−1/2PQ1/2)Q1/2 (34) These features are used in a classifier to detect respiratory states, thus enabling the BVI system.

The work on [91] introduces an innovative method combining Riemannian geometry with sparse optimization and Dempster-Shafer theory for enhanced motor imagery classification. The method, known as RSODSF, extracts features by first calculating the covariance matrices from segmented EEG signals, projecting them into Riemannian tangent space, and applying sparse optimization:

- 1

- 2 ∥y − Fw∥22 + λ∥w∥1 (35)

w = arg min

w

where F is the matrix of features, y is the label vector, w is the weight vector, and λ is the regularization parameter. The probabilistic outputs of a support vector machine (SVM) classifier are fused using Dempster-Shafer theory to improve classification accuracy:

EB∩EC=EA m1(EB)×m2(EC)

1− EB∩EC=∅ m1(EB)×m2(EC) if EA ̸= ∅ 0 if EA = ∅

(36)

m1,2(EA) =

The proposed method demonstrates significant accuracy improvements on BCI competition datasets.

The paper [116] suggested an expansion of the generalized learning vector quantization (GLVQ) to the curved Riemannian manifold of SPD matrices. The scholars introduce a technique known as Generalized Learning Riemannian Space Quantization (GLRSQ), which adjusts the GLVQ framework to operate within the suitable Riemannian metric, thereby notably improving classification accuracy for tasks involving EEG-based motor imagery. The cost function for GLRSQ on a Riemannian manifold is given by:

m

ϕ(µ(Xi,W)) (37)

E(W) =

i=1

where ϕ is a monotonically increasing function, and µ(Xi,W) is defined as:

δ(Xi,WJ) − δ(Xi,WK) δ(Xi,WJ) + δ(Xi,WK)

(38)

µ(Xi,W) =

with WJ and WK being the closest correct and incorrect prototypes, respectively. The gradients of the cost function with respect to the prototypes are derived as:

- ∆WJ = −α(t)∇WJ

E = −α(t)ϕ′

4δK (δJ + δK)2

LogW

J

(Xi),

- ∆WK = α(t)∇WK

(39)

4δJ (δJ + δK)2

E = α(t)ϕ′

LogW

(Xi),

K

where α(t) is the learning rate, ϕ′ is the derivative of ϕ, and LogW

(Xi) denotes the logarithmic map of Xi at WJ. The exponential and logarithmic maps are used to update the prototypes on the SPD manifold:

J

ExpW(V ) = W1/2 exp(W−1/2V W−1/2)W1/2, LogW(X) = W1/2 log(W−1/2XW−1/2)W1/2.

(40)

The update rules for the prototypes WJ and WK are given by:

- WJ ← ExpW

J

(−α(t)∇WJ

E),

- WK ← ExpW

(41)

(−α(t)∇WK

E).

K

This innovative approach ensures that the prototypes remain within the SPD manifold, leveraging the geometric properties of the manifold to enhance classification performance. The experimental results demonstrate that GLRSQ significantly outperforms traditional Euclidean-based GLVQ methods and shows competitive performance with state-ofthe-art techniques in EEG classification for motor imagery tasks.

#### 4.3 manifold learning

Integration of deep learning with Riemannian geometry-based methods was a tren in recent years. In [83], the proposed EEG-SPDNet incorporates Riemannian geometry into deep network architectures, enhancing the decoding by exploiting the physiological plausibility of frequency regions. Concurrently, [82] introduces a method for robust representation of EEG signals through spatial covariance matrices, capturing homogeneous segments effectively. Furthermore,

- [86] develops a model that optimizes subject-specific frequency band selection for motor imagery classification by constructing multiple Riemannian graphs and applying advanced graph embedding and fusion techniques, tailoring the approach to individual variations in EEG signal patterns.
- [87] introduces a novel method to address the limitations of existing SPD matrix-based Riemannian networks. They propose Riemannian Embedding Banks (REB), which partition the problem of learning common spatial patterns into multiple subproblems, each modeled separately and then combined within SPD neural networks. The REB method utilizes the SPDNet framework, which includes layers such as BiMap and ReEig for transformation and feature extraction. The BiMap layer performs a bilinear mapping to generate more discriminative and compact SPD matrix features. The transformation is given by:

Xk = WsXs−1WsT, (42) where Ws is the transformation matrix ensuring the output Xk remains in the form of an SPD matrix. Similar to the ReLU layer in traditional neural networks, the ReEig layer rectifies SPD matrices with small positive eigenvalues:

Xs = Us−1 max(ϵI,Σs−1)UsT−1, (43)

where Us−1 and Σs−1 are obtained from the eigenvalue decomposition Xs−1 = Us−1Σs−1UsT−1, and ϵ is a threshold parameter. The REB approach optimizes the embedding by assigning features to clusters and ensuring that the samples within each cluster are informative. The clustering is achieved by minimizing:

δR2 (Xi,Xj), (44)

LA(Xi;fp) =

Xj∈fp(Xi)

δR2 (Xi,Xj), (45)

LP(Xi,yi;fp) = −

Xj∈fp(Xi),yj=yi

and

log(min(10−4,Q(D(Xi,Xm))), (46)

LN(Xi;fp) =

Xm∈fp(Xi),ym̸=yi

where Q(D) is a distribution function ensuring negative samples are uniformly distributed based on their distances. The final embedding is constructed by concatenating the sub-embeddings produced by individual learners:

f = [fd(Xi;f1),fd(Xi;f2),...,fd(Xi;fK)], (47) and the loss function for training is given by:

Lk = λ1

Xi∈Ck

##### LC

(Xi;fp) + λ2

k

Xi∈Ck

##### (Xi;fk). (48)

Lf

k

The experimental results on public EEG datasets demonstrate the superiority of the proposed REB approach in learning common spatial patterns of EEG signals, increasing convergence speed, and maintaining generalization despite the non-stationary nature of the data.

The paper [96] leverages the graph structure of EEG trials, incorporating node influence properties and an ensemble of semantic graphs into the neural structured learning framework. This approach improves classification performance by capturing the complex relationships between EEG trials and integrating manifold regularities into the learning process. The optimization equation includes supervised and neighbor loss functions:

D

loss =

L(yi,yˆi) + α

i=1

D

LN(yi,xi,N(xi)), (49)

i=1

where L(yi,yˆi) is the supervised loss, LN(yi,xi,N(xi)) is the neighbor loss, and α is the graph regularization parameter.

- [118] presents a novel approach using geodesic correlation on the SPD manifold. The geodesic correlation measure G(X,Y ) for two SPD matrices X and Y is given by:

G(X,Y ) =

d

log2 λi (50)

i=1

where λi are the generalized eigenvalues of the pair (X,Y ). This framework enhances geodesic correlation for multi-view, self-supervised learning.

[86] proposes the MRGF model to optimize frequency band selection and extract spatial and spectral features from EEG signals. The framework constructs multiple Riemannian graphs and employs graph embedding and fusion techniques. The bilinear mapping W for dimensionality reduction is optimized by preserving distance structures between the high-dimensional manifold and low-dimensional embedding:

δR(Pi,Pj) − δR(WPiWT,WPjWT) (51)

min

W

Pi,Pj∈C

where δR is the Riemannian distance, and C is the experimental dataset.

[97] proposes a novel manifold attention module designed to handle SPD matrices. This network employs bilinear mappings to convert input SPD matrices into query, key, and value matrices while retaining their SPD structure. Specifically, for a given input x˜i, the query, key, and value mappings are formulated as follows:

qi = hq(˜xi;Wq) = Wqx˜iWqT (52)

ki = hk(˜xi;Wk) = Wkx˜iWkT (53)

vi = hv(˜xi;Wv) = Wvx˜iWvT (54)

where Wq, Wk, and Wv are transformation matrices ensuring that the output remains in the SPD manifold. The similarity between qi and kj is computed using the Log-Euclidean distance:

1 1 + log(1 + δ1(qi,kj))

sim(qi,kj) =

:= αij (55)

Here, δ1 denotes the Log-Euclidean distance. The attention matrix A = [αij]m×m is normalized using the softmax function, and the final output vi′ is computed as:

vi′ = Exp

m

αilLog(vl) (56)

l=1

The backward procedure for gradient descent parameter updating on the Riemannian manifold involves projecting Euclidean gradients onto the tangent space using Stiefel gradients and retraction operations. The Stiefel gradient ∇WvL is computed as:

∇WvL = ∇WvL − πN(∇WvL) (57)

∇WvL = ∇WvL − Wv

Finally, the weight update is performed as:

WvT∇WvL + (∇WvL)TWv 2

(58)

Wv(new) = Γ(Wv − λ ∇WvL) (59) where Γ is the retraction operation.

In [115], the authors propose a novel method for modeling EEG covariance matrix distributions using Riemannian spectral clustering (RiSC). The framework allows for both unimodal and multimodal distributions on the SPD manifold, facilitating outlier detection and robust classification. The core of the method involves clustering EEG data points based on the Affine-Invariant Riemannian Metric (AIRM). For classification, the authors introduce the multimodal classifier mcRiSC, which computes the distance of a new observation P to cluster centroids and assigns it to the nearest cluster. The prediction is formulated as:

ˆb = arg min

δR P,P¯(b) , (60)

b∈{1,...,B}

where P¯(b) denotes the centroid of cluster b. This method allows flexible application without prior knowledge of the data distribution, significantly enhancing classification performance.

The study on [124] demonstrates how projecting covariance matrices onto the Riemannian manifold, followed by their integration into a deep learning model, can yield superior performance compared to traditional methods. Similarly, the research on [100] investigates the application of geometric neural networks, leveraging phase space representations of EEG signals to improve classification accuracy. Furthermore, [99] employs a manifold-based GCN diffusion model to effectively capture complex spatial-temporal dynamics in EEG data, thereby enhancing the robustness and accuracy of BCI systems. Lastly, the work on [106] introduces an ensemble learning framework that combines Riemannian geometric features with machine learning classifiers, which significantly improves cross-session motor imagery classification accuracy.

These manifold learning approaches collectively advance the field of EEG signal processing by leveraging the mathematical properties of Riemannian manifolds to provide more effective and robust tools for feature extraction, data representation, and classification.

#### 4.4 Tangent Space Approaches

Recent advancements in tangent space approaches for EEG signal processing have introduced innovative methods to enhance feature extraction and classification in BCIs. These methods leverage the properties of Riemannian geometry to map covariance matrices into the tangent space, allowing for effective manipulation and analysis of EEG data. [108] introduced a feature extraction method combining filter banks and Riemannian tangent space for multi-category MI classification, addressing frequency variance and noise interference. [93] revisited Riemannian geometry-based EEG decoding through approximate joint diagonalization, simplifying Riemannian geometry concepts and reducing computational complexity. [92] proposed a Riemannian distance-based channel selection and feature extraction method combining discriminative time-frequency bands and Riemannian tangent space for MI-BCIs. [95] presented a spatiotemporal EEG representation learning framework on Riemannian manifold and Euclidean space, combining spatial and temporal information for improved classification performance.

[81] proposed a method for motor imagery classification that utilizes Riemannian geometry with a median absolute deviation (MAD) strategy. This approach involves calculating the average sample covariance matrices (SCMs) to select optimal reference metrics in a tangent space mapping (TSM)-based MI-EEG framework. The features are extracted using TSM, where the data from SCMs are projected according to a reference matrix representing the feature vector. Principal component analysis (PCA) and analysis of variance (ANOVA) are then applied to reduce dimensions and select optimal features for classification using linear discriminant analysis (LDA). The mathematical formulation of the Riemannian distance is given by:

dR(Ci,Cj) = ∥log(Ci) − log(Cj)∥F (61)

where dR represents the Riemannian distance, Ci and Cj are covariance matrices, and ∥·∥F denotes the Frobenius norm. Miah et al. demonstrated that this method provides better accuracy compared to more sophisticated methods.

- [119] introduced a manifold regression approach to predict from MEG/EEG signals without source modeling. This method uses the Riemannian geometry of rank-reduced covariance matrices and vectorizes them through projection into a tangent space. The Wasserstein distance and affine-invariant geometric distance are employed to handle rank-reduced data and improve prediction accuracy. The experimental results showed that this method outperforms sensor-space estimators and approaches the performance of source-localization models. In detail, the covariance matrices of EEG signals are first computed as:

N

1 N

xi(t)xi(t)T (62)

Ci =

t=1

where Ci is the covariance matrix for the i-th trial, N is the number of time samples, and xi(t) is the EEG signal at time t.

These covariance matrices are then mapped to the tangent space of the Riemannian manifold. For a reference point C0 on the manifold, the tangent space projection is given by:

ϕ(Ci) = log(C0−1/2CiC0−1/2) (63)

where log is the matrix logarithm, and ϕ(Ci) represents the projected covariance matrix in the tangent space. For regression, the features are vectorized:

##### ϕ(Ci) = vec log(C0−1/2CiC0−1/2) (64)

where vec denotes the vectorization operation. The regression model is formulated as:

yˆ = W · ϕ(C) (65)

- where yˆ is the predicted value, W is the weight matrix, and ϕ(C) represents the feature vector obtained by projecting the covariance matrix C into the tangent space.

[78] explored the use of multiple tangent space projections for motor imagery EEG classification. The method involves projecting covariance matrices from their native Riemannian space to multiple class-dependent tangent spaces, enhancing the information provided to the classifier. This approach significantly improves model accuracy by utilizing different projections tailored to specific classes. The study demonstrated that multiple tangent space projections could effectively capture the discriminative features for better classification performance. The tangent space projection is mathematically expressed as:

ϕ(C) = vec(log(C) − log(C0)) (66)

where ϕ(C) is the feature vector, log(C) is the matrix logarithm of the covariance matrix C, and C0 is the reference matrix.

These studies collectively advance the field of tangent space approaches for EEG signal processing, offering innovative solutions to enhance feature extraction, reduce dimensionality, and improve classification accuracy in BCIs.

#### 4.5 Transfer Learning Approaches

Transfer learning approaches in EEG signal processing have made significant strides in reducing calibration time and improving classification accuracy by leveraging data from multiple subjects. These methods utilize Riemannian geometry and tangent space alignment to handle the variability between subjects and sessions effectively.

[84] proposed the Riemannian Geometric Instance Filtering (RGIF) framework to address the challenge of inter-subject variability in EEG signals. The framework includes two core components: a stable inter-subject similarity metric based on Riemannian geometry and a convolutional neural network for feature extraction. The similarity metric measures the similarity between a few trials from the target subject and abundant trials from source subjects, focusing on removing data from significantly different subjects. The geodesic distance between two SPD matrices P1 and P2 is defined as:

δR(P1,P2) = log(P1−1P2) F =

n

log2 λi(P1−1P2)

i=1

1/2

(67)

where λi are the eigenvalues of P1−1P2. The Riemannian mean matrix Gk for the target subject is computed as:

Nk

Gk = arg min

G

δR2 (G,Pi) (68)

i=1

This framework significantly reduces calibration time while maintaining high classification accuracy by combining data from similar subjects and the powerful feature extraction capabilities of CNNs.

[110] introduced supervised and semi-supervised manifold embedded knowledge transfer (sMEKT and ssMEKT) algorithms to handle inter-session/subject variability in MI EEG signals. These algorithms perform domain adaptation by preserving source domain discriminability and target domain geometric structure. After Riemannian alignment and tangent space mapping , both sMEKT and ssMEKT minimize the joint probability distribution shift between the source and target domains. The alignment process is given by:

##### ϕ(Ci) = log(C0−1/2CiC0−1/2) (69)

where ϕ(Ci) represents the projected covariance matrix in the tangent space. The optimization for minimizing the distribution shift is formulated as:

L(θ) =

Ns

Nt

ℓ(fθ(ϕ(Cis)),yis) + λ

i=1

ℓ(fθ(ϕ(Cit)),yit) (70)

i=1

where ℓ is the loss function, fθ is the classifier, Cis and Cit are source and target domain samples, respectively, and λ is a regularization parameter. These algorithms demonstrate significant improvements in classification accuracy with

fewer labeled samples from the target domain.

Other notable contributions in transfer learning approaches include Xu et al. [89], who proposed a selective cross-subject transfer learning approach based on Riemannian tangent space for motor imagery BCI, using Riemannian alignment to bring covariance matrices from different subjects closer and extracting Riemannian tangent space features for classification. Cai et al. [107] introduced a framework for motor imagery EEG decoding using manifold embedded transfer learning, aligning covariance matrices on the SPD manifold and extracting features from both SPD and Grassmann manifolds, demonstrating superior performance in transfer tasks. Additionally, [114] presented a tangent space alignment method for transfer learning in BCIs, aligning EEG data from different subjects in the tangent space of the positive definite matrices Riemannian manifold, showing improved classification accuracy.

These studies collectively advance the field of transfer learning approaches for EEG signal processing, offering innovative solutions to enhance feature extraction, reduce calibration time, and improve classification accuracy in BCIs.

### 5 Discussion and Challenges

The integration of Riemannian geometry in EEG-based BCI systems has significantly progressed feature extraction, classification, and transfer learning within the respective fields. However, despite these advancements, various persistent challenges hinder the widespread adoption and efficacy of these methodologies. A primary obstacle lies in the computational intricacies associated with managing intricate manifold embeddings and high-dimensional transformations, particularly problematic in time-sensitive applications where swift data processing is essential. Furthermore, these approaches often struggle with generalization across diverse tasks and populations, given the variability in EEG patterns among individuals presents a notable hurdle. Additionally, the efficacy of Riemannian geometry-based techniques heavily relies on the quality of the input EEG data. Factors such as artifacts, noise, and non-stationarity can notably deteriorate performance, necessitating advanced preprocessing methods that may not always be practical in real-world scenarios. Another significant constraint is the lack of interpretability in these sophisticated mathematical transformations, which can impede clinical acceptance and further development of the methodologies. Moreover, there exists a noticeable gap in integrating these approaches with other modalities like fMRI or MEG, which could potentially enhance diagnostic and therapeutic capabilities but also introduce additional complexity in data fusion and analysis. Concentrated efforts in various crucial areas are imperative. Subsequent research endeavors should prioritize the

[Figure 3]

Figure 3: Classification tasks presented in the current literature

enhancement of computational algorithms to achieve higher efficiency, thereby reducing the temporal and resource demands of existing methodologies, potentially through the utilization of emerging technologies like GPU acceleration. Additionally, there exists an urgent requirement for the creation of adaptive models capable of accommodating the inter-individual variabilities and cognitive state differences present across a heterogeneous population. Enhancements in managing noise and artifacts within the Riemannian framework have the potential to notably augment the quality of EEG

data before further processing. The amalgamation of Riemannian geometry with alternative machine learning strategies in hybrid models could represent a significant advancement in enhancing both the efficacy and interpretability of these approaches. Furthermore, broadening the application of these methodologies to synergize with other neurological data modalities could offer a more comprehensive insight into brain function. Lastly, the establishment of open-source platforms and collaborative frameworks could expedite innovation and standardize practices in the field, thus rendering these sophisticated techniques more accessible and adaptable across various applications.

#### 5.1 Future Directions in Research

To address the computational complexity of Riemannian geometry-based methods, future research should focus on optimizing algorithms for faster computation. This includes developing efficient numerical methods for calculating Riemannian distances and means, as well as exploring alternative representations of EEG signals that retain critical information with lower dimensionality. One potential direction is the use of approximation techniques or dimensionality reduction methods that preserve the geometric properties of the data.

Enhancing the scalability of graph neural networks on SPD manifolds is a critical area for prospective investigation. This task entails the creation of scalable GNN structures capable of effectively managing extensive EEG datasets. The exploration of hybrid models amalgamating the merits of conventional machine learning approaches and deep learning methodologies could contribute to tackling the scalability challenge. Moreover, delving into parallel computation and distributed processing methodologies might further amplify the scalability of these frameworks.

Adapting manifold learning strategies to render them more suitable for real-time applications holds paramount importance. This objective can be realized through the formulation of models that are both computationally efficient and facile to deploy. Subsequent research endeavors should prioritize the simplification of these models’ intricacy while upholding their efficacy. Potential strategies may encompass the utilization of approximation methodologies, streamlined mathematical representations, or innovative model structures customized for real-time computations.

Improving transfer learning frameworks to effectively manage inter-subject variability and decrease the requirement for substantial labeled data presents a significant challenge. Subsequent investigations ought to delve into resilient transfer learning methodologies capable of functioning efficiently with limited labeled data. Such endeavors may encompass the formulation of unsupervised or semi-supervised learning strategies, along with the utilization of domain adaptation techniques tailored for EEG data. Moreover, the exploration of more efficient approaches for aligning data across diverse subjects and sessions within the tangent space of the Riemannian manifold could contribute to enhancing the efficacy of transfer learning strategies.

To summarize, tackling computational intricacies, enhancing scalability, streamlining models for practical implementation, and refining transfer learning frameworks constitute pivotal domains for prospective studies. These endeavors are poised to facilitate the advancement of more effective, precise, and user-friendly Brain-Computer Interfaces (BCIs) that can find widespread utility in both clinical and non-clinical environments.

### 6 Conclusion

This study offers an extensive examination of the fusion of Riemannian geometry with deep learning methodologies within the domain of brain-computer interfaces. The unique amalgamation of these sophisticated mathematical strategies has illustrated substantial potential in augmenting the decoding capabilities of EEG signals in BCIs. Specifically, Riemannian geometry has played a pivotal role in the accurate and resilient management of the non-Euclidean data structures inherent in EEG data, an area where conventional Euclidean methods often prove inadequate. Our analysis has refreshed the landscape of EEG signal processing by presenting recent progressions that exploit deep learning to tackle and alleviate traditional BCI obstacles like sensitivity to noise, non-stationarity, and prolonged calibration periods. Through the perspective of Riemannian geometry, a shift has been observed in the utilization of covariance matrices, transitioning from fundamental manipulations to sophisticated metric learning and optimization for EEG classification.

This transition not only enhances existing subspace techniques but also indicates a shift towards directly manipulating and categorizing covariance matrices, potentially circumventing traditional methodologies altogether. Nevertheless, despite the advancements, this analysis also highlights the necessity for further investigation to surmount the persisting constraints of BCIs. The infusion of Riemannian geometry into BCI design necessitates novel EEG representations that are more resilient and classifiers capable of effectively managing outliers and non-stationarity. Prospective avenues should also contemplate the formulation of adaptive techniques capable of dynamically adapting to the user’s cognitive status and environmental variations. Additionally, delving into the possibilities of Riemannian geometry for multitask learning, feature extraction, and transfer learning within BCIs could yield substantial enhancements in both efficacy and

usability. In summary, the convergence of Riemannian geometry and deep learning harbors significant potential for the trajectory of BCIs.

As this domain progresses, it is imperative that sustained endeavors are channeled towards not only refining these mathematical frameworks but also rendering these sophisticated methodologies more accessible for pragmatic BCI implementations. We anticipate that the advancements expounded in this analysis will pave the way for more intuitive, efficient, and user-friendly BCI systems, setting a new benchmark for EEG signal classification and further bridging the chasm between theoretical exploration and real-world applications.

### References

- [1] M. Teplan and others, “Fundamentals of EEG measurement,” Measurement science review, vol. 2, no. 2, pp. 1–11, 2002.
- [2] I. Iturrate, J. Antelis, and J. Minguez, “Synchronous EEG brain-actuated wheelchair with automated navigation,” in 2009 IEEE International Conference on Robotics and Automation, pp. 2318–2325, IEEE, 2009.
- [3] D. P. Subha, P. K. Joseph, R. U. Acharya, and C. M. Lim, “EEG signal analysis: a survey,” Journal of medical systems, vol. 34, pp. 195–212, Springer, 2010.
- [4] Z. T. Al-Qaysi, B. B. Zaidan, A. A. Zaidan, and M. S. Suzani, “A review of disability EEG based wheelchair control system: Coherent taxonomy, open challenges and recommendations,” Computer methods and programs in biomedicine, vol. 164, pp. 221–237, Elsevier, 2018.
- [5] Y.-T. Wang, M. Nakanishi, Y. Wang, C.-S. Wei, C.-K. Cheng, and T.-P. Jung, “An online brain-computer interface based on SSVEPs measured from non-hair-bearing areas,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 1, pp. 14–21, IEEE, 2016.
- [6] K. K. Ang, K. S. G. Chua, K. S. Phua, C. Chuanchu, Z. Y. Chin, C. W. K. Kuah, W. Low, and C. Guan, “A randomized controlled trial of EEG-based motor imagery brain-computer interface robotic rehabilitation for stroke,” Clinical EEG and neuroscience, vol. 46, no. 4, pp. 310–320, SAGE Publications Sage CA: Los Angeles, CA, 2015.
- [7] J. Mladenovi´c, J. Frey, S. Pramij, J. Mattout, and F. Lotte, “Towards identifying optimal biased feedback for various user states and traits in motor imagery BCI,” IEEE Transactions on Biomedical Engineering, vol. 69, no. 3, pp. 1101–1110, IEEE, 2021.
- [8] F. Dehais, S. Ladouce, L. Darmet, T.-V. Nong, G. Ferraro, J. Torre Tresols, S. Velut, and P. Labedan, “Dual passive reactive brain-computer interface: A novel approach to human-machine symbiosis,” Frontiers in Neuroergonomics, vol. 3, 824780, Frontiers, 2022.
- [9] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain–computer interfaces for communication and control,” Clinical neurophysiology, vol. 113, no. 6, pp. 767–791, Elsevier, 2002.
- [10] M. Clerc and L. Bougrain, “Brain–Computer Interfaces 2,” Wiley Online Library.
- [11] J. J. Vidal, “Toward direct brain-computer communication,” Annual review of Biophysics and Bioengineering, vol. 2, no. 1, pp. 157–180, Annual Reviews 4139 El Camino Way, PO Box 10139, Palo Alto, CA 94303-0139, USA, 1973.
- [12] G. Pfurtscheller, G. R. Müller-Putz, R. Scherer, and C. Neuper, “Rehabilitation with brain-computer interface systems,” Computer, vol. 41, no. 10, pp. 58–65, IEEE, 2008.
- [13] J. R. Wolpaw, D. J. McFarland, G. W. Neat, and C. A. Forneris, “An EEG-based brain-computer interface for cursor control,” Electroencephalography and clinical neurophysiology, vol. 78, no. 3, pp. 252–259, Elsevier, 1991.
- [14] D. Coyle, J. Principe, F. Lotte, and A. Nijholt, “Guest Editorial: Brain/neuronal-Computer game interfaces and interaction,” IEEE Transactions on Computational Intelligence and AI in games, vol. 5, no. 2, pp. 77–81, IEEE, 2013.
- [15] A. Buttfield, P. W. Ferrez, and Jd R. Millan, “Towards a robust BCI: error potentials and online learning,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 14, no. 2, pp. 164–168, IEEE, 2006.
- [16] C. Vidaurre, C. Sannelli, K.-R. Müller, and B. Blankertz, “Co-adaptive calibration to improve BCI efficiency,” Journal of neural engineering, vol. 8, no. 2, 025009, IOP Publishing, 2011.
- [17] M. Sebastián-Romagosa, E. Udina, R. Ortner, J. Dinarès-Ferran, W. Cho, N. Murovec, C. Matencio-Peralba, S. Sieghartsleitner, B. Z. Allison, and C. Guger, “EEG biomarkers related with the functional state of stroke patients,” Frontiers in neuroscience, vol. 14, 582, Frontiers Media SA, 2020.

- [18] R. Janapati, V. Dalal, and R. Sengupta, “Advances in modern EEG-BCI signal processing: A review,” Materials Today: Proceedings, vol. 80, pp. 2563–2566, Elsevier, 2023.
- [19] A. Roman-Gonzalez, “EEG signal processing for BCI applications,” Human–computer systems interaction: backgrounds and applications, vol. 2, pp. 571–591, Springer, 2012.
- [20] M. Congedo, A. Barachant, and R. Bhatia, “Riemannian geometry for EEG-based brain-computer interfaces; a primer and a review,” Brain-Computer Interfaces, vol. 4, no. 3, pp. 155–174, Taylor & Francis, 2017.
- [21] F. Yger, M. Berar, and F. Lotte, “Riemannian approaches in brain-computer interfaces: a review,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 10, pp. 1753–1762, IEEE, 2016.
- [22] S. Russo, I. E. Tibermacine, A. Tibermacine, D. Chebana, A. Nahili, J. Starczewscki, and C. Napoli, “Analyzing EEG patterns in young adults exposed to different acrophobia levels: a VR study,” Frontiers in Human Neuroscience, vol. 18, 1348154, Frontiers Media SA, 2024.
- [23] I. E. Tibermacine, A. Tibermacine, W. Guettala, C. Napoli, and S. Russo, “Enhancing sentiment analysis on seed-IV dataset with vision transformers: a comparative study,” in Proceedings of the 2023 11th International Conference on Information Technology: IoT and Smart City, pp. 238–246, 2023.
- [24] N. Boutarfaia, S. Russo, A. Tibermacine, and I. E. Tibermacine, “Deep Learning for EEG-Based Motor Imagery Classification: Towards Enhanced Human-Machine Interaction and Assistive Robotics,” life, vol. 2, no. 3, pp. 4, 2023.
- [25] I. Naidji, A. Tibermacine, W. Guettala, and I. E. Tibermacine, “Semi-mind controlled robots based on Reinforcement Learning for Indoor Application,” in ICYRIME, pp. 51–59, 2023.
- [26] D. A. Kaiser, “Basic principles of quantitative EEG,” Journal of Adult Development, vol. 12, pp. 99–104, Springer, 2005.
- [27] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K.-R. Müller, “Optimizing spatial filters for robust EEG single-trial analysis,” IEEE Signal processing magazine, vol. 25, no. 1, pp. 41–56, IEEE, 2007.
- [28] C. Guger, H. Ramoser, and G. Pfurtscheller, “Real-time EEG analysis with subject-specific spatial patterns for a brain-computer interface (BCI),” IEEE transactions on rehabilitation engineering, vol. 8, no. 4, pp. 447–456, IEEE, 2000.
- [29] P. Shenoy, M. Krauledat, B. Blankertz, R. P. N. Rao, and K.-R. Müller, “Towards adaptive classification for BCI,” Journal of neural engineering, vol. 3, no. 1, R13, IOP Publishing, 2006.
- [30] J. M. Lee, Introduction to Riemannian manifolds, vol. 2, Springer, 2018.
- [31] Z. Huang and L. Van Gool, “A riemannian network for spd matrix learning,” in Proceedings of the AAAI conference on artificial intelligence, vol. 31, no. 1, 2017.
- [32] A. Ma´ckiewicz and W. Ratajczak, “Principal components analysis (PCA),” Computers & Geosciences, vol. 19, no. 3, pp. 303–342, Elsevier, 1993.
- [33] A. Guisan, S. B. Weiss, and A. D. Weiss, “GLM versus CCA spatial modeling of plant species distribution,” Plant ecology, vol. 143, pp. 107–122, Springer, 1999.
- [34] Y.-J. Suh and B. H. Kim, “Riemannian embedding banks for common spatial patterns with EEG-based SPD neural networks,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, no. 1, pp. 854–862, 2021.
- [35] X. Wang, W. Yang, W. Qi, Y. Wang, X. Ma, and W. Wang, “STaRNet: A spatio-temporal and Riemannian network for high-performance motor imagery decoding,” Neural Networks, 106471, Elsevier, 2024.
- [36] M. Esghaei, S. Treue, and T. R. Vidyasagar, “Dynamic coupling of oscillatory neural activity and its roles in visual attention,” Trends in Neurosciences, vol. 45, no. 4, pp. 323–335, Elsevier, 2022.
- [37] A. Keutayeva and B. Abibullaev, “Exploring the potential of attention mechanism-based deep learning for robust subject-independent motor-imagery based BCIs,” IEEE Access, IEEE, 2023.
- [38] Z. Xiao, H. Zhang, H. Tong, and X. Xu, “An efficient temporal network with dual self-distillation for electroencephalography signal classification,” in 2022 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), pp. 1759–1762, IEEE, 2022.
- [39] N. Robinson, A. P. Vinod, K. K. Ang, K. P. Tee, and C. T. Guan, “EEG-based classification of fast and slow hand movements using wavelet-CSP algorithm,” IEEE Transactions on Biomedical Engineering, vol. 60, no. 8, pp. 2123–2132, IEEE, 2013.
- [40] N. Schaworonkow and B. Voytek, “Enhancing oscillations in intracranial electrophysiological recordings with data-driven spatial filters,” PLOS Computational Biology, vol. 17, no. 8, e1009298, Public Library of Science San Francisco, CA USA, 2021.

- [41] W. Wu, Z. Chen, X. Gao, Y. Li, E. N. Brown, and S. Gao, “Probabilistic common spatial patterns for multichannel EEG analysis,” IEEE transactions on pattern analysis and machine intelligence, vol. 37, no. 3, pp. 639–653, IEEE, 2014.
- [42] S. Bhattacharyya, A. Khasnobish, S. Chatterjee, A. Konar, and D. N. Tibarewala, “Performance analysis of LDA, QDA and KNN algorithms in left-right limb movement classification from EEG data,” in 2010 International conference on systems in medicine and biology, pp. 126–131, IEEE, 2010.
- [43] R. Das, M. Zaheer, and C. Dyer, “Gaussian LDA for topic models with word embeddings,” in Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 795–804, 2015.
- [44] W. Zheng, J.-H. Lai, and S. Z. Li, “1D-LDA vs. 2D-LDA: When is vector-based linear discriminant analysis better than matrix-based?,” Pattern Recognition, vol. 41, no. 7, pp. 2156–2172, Elsevier, 2008.
- [45] G. Mai, N. Lao, Y. He, J. Song, and S. Ermon, “Csp: Self-supervised contrastive spatial pre-training for geospatialvisual representations,” in International Conference on Machine Learning, pp. 23498–23515, PMLR, 2023.
- [46] J. Zhao, L. H. Philip, L. Shi, and S. Li, “Separable linear discriminant analysis,” Computational Statistics & Data Analysis, vol. 56, no. 12, pp. 4290–4300, Elsevier, 2012.
- [47] X. Zhang, L. Yao, X. Wang, J. Monaghan, D. Mcalpine, and Y. Zhang, “A survey on deep learning based brain computer interface: Recent advances and new frontiers,” arXiv preprint arXiv:1905.04149, vol. 66, May, 2019.
- [48] Z. Khademi, F. Ebrahimi, and H. Montazery Kordy, “A review of critical challenges in MI-BCI: From conventional to deep learning methods,” Journal of Neuroscience Methods, vol. 383, 109736, Elsevier, 2023.
- [49] F. Lotte, “Signal processing approaches to minimize or suppress calibration time in oscillatory activity-based brain–computer interfaces,” Proceedings of the IEEE, vol. 103, no. 6, pp. 871–890, IEEE, 2015.
- [50] A. Ravi, J. Lu, S. Pearce, and N. Jiang, “Enhanced system robustness of asynchronous BCI in augmented reality using steady-state motion visual evoked potential,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 85–95, IEEE, 2022.
- [51] L. Meng, X. Jiang, and D. Wu, “Adversarial robustness benchmark for EEG-based brain–computer interfaces,” Future Generation Computer Systems, vol. 143, pp. 231–247, Elsevier, 2023.
- [52] J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Springer, 2013.
- [53] L. W. Tu, An Introduction to Manifolds, 2nd ed., Springer, 2010.
- [54] M. P. Do Carmo, Riemannian Geometry, Birkhäuser, 1992.
- [55] P. Petersen, Riemannian Geometry, Springer, 2006.
- [56] S. Gallot, D. Hulin, and J. Lafontaine, Riemannian Geometry, 3rd ed., Springer, 2004.
- [57] B. O’Neill, Semi-Riemannian Geometry With Applications to Relativity, Academic Press, 1983.
- [58] J. M. Lee, Manifolds and Differential Geometry, American Mathematical Society, 2009.
- [59] X. Pennec, P. Fillard, and N. Ayache, “A Riemannian Framework for Tensor Computing,” International Journal of Computer Vision, vol. 66, no. 1, pp. 41–66, 2006.
- [60] I. L. Dryden and K. V. Mardia, Statistical Shape Analysis, John Wiley & Sons, 1998.
- [61] J. S. Bendat and A. G. Piersol, Random Data: Analysis and Measurement Procedures, 4th ed., Wiley-Interscience, 2010.
- [62] R. Bhatia, Positive Definite Matrices, Princeton University Press, 2007.
- [63] X. Pennec, “Statistical Computing on Manifolds for Computational Anatomy,” International Journal of Computer Vision, vol. 66, no. 1, pp. 1–35, 2006.
- [64] S. Sanei and J. A. Chambers, EEG Signal Processing, Wiley, 2007.
- [65] V. Arsigny, P. Fillard, X. Pennec, and N. Ayache, “Log-Euclidean Metrics for Fast and Simple Calculus on Diffusion Tensors,” Magnetic Resonance in Medicine, vol. 56, no. 2, pp. 411–421, 2006.
- [66] P. T. Fletcher, C. Lu, S. M. Pizer, and S. Joshi, “Principal Geodesic Analysis for the Study of Nonlinear Statistics of Shape,” IEEE Transactions on Medical Imaging, vol. 23, no. 8, pp. 995–1005, 2004.
- [67] C. R. Rao, “Information and the Accuracy Attainable in the Estimation of Statistical Parameters,” Bulletin of the Calcutta Mathematical Society, vol. 37, no. 3, pp. 81–91, 1945.
- [68] M. Pourahmadi, High-Dimensional Covariance Estimation, John Wiley & Sons, 2011.

- [69] M. Moakher, “A Differential Geometric Approach to the Geometric Mean of Symmetric Positive-Definite Matrices,” SIAM Journal on Matrix Analysis and Applications, vol. 26, no. 3, pp. 735–747, 2005.
- [70] J. Jost, Riemannian Geometry and Geometric Analysis, 5th ed., Springer, 2008.
- [71] G. S. Russell, K. J. Eriksen, P. Poolman, P. Luu, and D. M. Tucker, “Geodesic photogrammetry for localizing sensor positions in dense-array EEG,” Clinical Neurophysiology, vol. 116, no. 5, pp. 1130–1140, Elsevier, 2005.
- [72] A. Yamin, M. Dayan, L. Squarcina, P. Brambilla, V. Murino, V. Diwadkar, and D. Sona, “Analysis of dynamic brain connectivity through geodesic clustering,” in Image Analysis and Processing–ICIAP 2019: 20th International Conference, Trento, Italy, September 9–13, 2019, Proceedings, Part II 20, pp. 640–648, Springer, 2019.
- [73] S. C. Joshi, M. I. Miller, and U. Grenander, “On the geometry and shape of brain sub-manifolds,” IJPRAI, vol. 11, no. 8, pp. 1317–1343, Citeseer, 1997.
- [74] M. Banerjee, R. Chakraborty, E. Ofori, D. Vaillancourt, and B. C. Vemuri, “Nonlinear regression on Riemannian manifolds and its applications to neuro-image analysis,” in Medical Image Computing and Computer-Assisted Intervention–MICCAI 2015: 18th International Conference, Munich, Germany, October 5-9, 2015, Proceedings, Part I 18, pp. 719–727, Springer, 2015.
- [75] S. Falciglia, F. Betello, S. Russo, and C. Napoli, “Learning visual stimulus-evoked EEG manifold for neural image classification,” Neurocomputing, vol. 588, 127654, Elsevier, 2024.
- [76] M. Congedo, A. Barachant, and R. Bhatia, “Riemannian geometry for EEG-based brain-computer interfaces; a primer and a review,” Brain-Computer Interfaces, vol. 4, no. 3, pp. 155–174, Taylor & Francis, 2017.
- [77] Z. Shuqfa, A. N. Belkacem, and A. Lakas, “Decoding multi-class motor imagery and motor execution tasks using Riemannian geometry algorithms on large EEG datasets,” Sensors, vol. 23, no. 11, p. 5051, 2023.
- [78] S. Omari, A. Omari, and M. Abderrahim, “Multiple tangent space projection for motor imagery EEG classification,” Applied Intelligence, vol. 53, no. 18, pp. 21192–21200, 2023.
- [79] E. K. Kalunga, S. Chevallier, Q. Barthélemy, K. Djouani, Y. Hamam, and E. Monacelli, “From Euclidean to Riemannian means: Information geometry for SSVEP classification,” in Geometric Science of Information: Second International Conference, GSI 2015, Palaiseau, France, October 28-30, 2015, Proceedings 2, pp. 595–604, Springer International Publishing, 2015.
- [80] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “BCI signal classification using a Riemannian-based kernel,” in ESANN 2012-20th European Symposium on Artificial Neural Networks, Computational Intelligence and Machine Learning, pp. 97–102, Michel Verleysen, April 2012.
- [81] A. S. M. Miah, M. A. Rahim, and J. Shin, “Motor-imagery classification using riemannian geometry with median absolute deviation,” Electronics, vol. 9, no. 10, p. 1584, 2020.
- [82] K. Sadatnejad, S. S. Ghidary, R. Rostami, and R. Kazemi, “EEG Representation Using Multi-instance Framework on The Manifold of Symmetric Positive Definite Matrices for EEG-based Computer Aided Diagnosis,” arXiv preprint arXiv:1702.02655, 2017.
- [83] D. Wilson, R. T. Schirrmeister, L. A. W. Gemein, and T. Ball, “Deep riemannian networks for eeg decoding,” arXiv preprint arXiv:2212.10426, 2022.
- [84] Q. Hui, X. Liu, Y. Li, S. Xu, S. Zhang, Y. Sun, and D. Zheng, “Riemannian Geometric Instance Filtering for Transfer Learning in Brain-Computer Interfaces,” in Proceedings of the 20th ACM Conference on Embedded Networked Sensor Systems, pp. 1162–1167, November 2022.
- [85] A. Hippert-Ferrer, A. Mian, F. Bouchard, and F. Pascal, “Riemannian classification of EEG signals with missing values,” in 2022 30th European Signal Processing Conference (EUSIPCO), pp. 842–846, IEEE, August 2022.
- [86] X. Xie, X. Zou, T. Yu, R. Tang, Y. Hou, and F. Qi, “Multiple graph fusion based on Riemannian geometry for motor imagery classification,” Applied Intelligence, vol. 52, no. 8, pp. 9067–9079, 2022.
- [87] Y. J. Suh and B. H. Kim, “Riemannian embedding banks for common spatial patterns with EEG-based SPD neural networks,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, no. 1, pp. 854–862, May 2021.
- [88] D. Sabbagh, P. Ablin, G. Varoquaux, A. Gramfort, and D. A. Engemann, “Manifold-regression to predict from MEG/EEG brain signals without source modeling,” Advances in Neural Information Processing Systems, vol. 32, 2019.
- [89] Y. Xu, X. Huang, and Q. Lan, “Selective cross-subject transfer learning based on riemannian tangent space for motor imagery brain-computer interface,” Frontiers in Neuroscience, vol. 15, article 779231, 2021.

- [90] S. Huang, G. Cai, T. Wang, and T. Ma, “Amplitude-phase information measurement on riemannian manifold for motor imagery-based bci,” IEEE Signal Processing Letters, vol. 28, pp. 1310–1314, 2021.
- [91] J. Jin, T. Qu, R. Xu, X. Wang, and A. Cichocki, “Motor imagery EEG classification based on Riemannian sparse optimization and dempster-shafer fusion of multi-time-frequency patterns,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 58–67, 2022.
- [92] T. Qu, J. Jin, R. Xu, X. Wang, and A. Cichocki, “Riemannian distance based channel selection and feature extraction combining discriminative time-frequency bands and Riemannian tangent space for MI-BCIs,” Journal of Neural Engineering, vol. 19, no. 5, article 056025, 2022.
- [93] F. P. Kalaganis, N. A. Laskaris, V. P. Oikonomou, S. Nikopolopoulos, and I. Kompatsiaris, “Revisiting Riemannian geometry-based EEG decoding through approximate joint diagonalization,” Journal of Neural Engineering, vol. 19, no. 6, article 066030, 2022.
- [94] F. Yacine, H. Salah, K. Amar, and K. Ahmad, “A novel ANN adaptive Riemannian-based kernel classification for motor imagery,” Biomedical Physics & Engineering Express, vol. 9, no. 1, article 015010, 2022.
- [95] G. Zhang and A. Etemad, “Spatio-temporal EEG representation learning on Riemannian manifold and Euclidean space,” IEEE Transactions on Emerging Topics in Computational Intelligence, 2023.
- [96] V. Gupta, L. Behera, and T. Sandhan, “Graph Based Semantic Ensemble of Riemannian Neural Structured Learning for BCI-EEG Signal Classification,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5, June 2023.
- [97] Y. T. Pan, J. L. Chou, and C. S. Wei, “MAtt: A manifold attention network for EEG decoding,” Advances in Neural Information Processing Systems, vol. 35, pp. 31116–31129, 2022.
- [98] S. Guan, K. Zhao, and S. Yang, “Motor imagery EEG classification based on decision tree framework and Riemannian geometry,” Computational intelligence and neuroscience, 2019.
- [99] M. Hanik, G. Steidl, and C. von Tycowicz, “Manifold GCN: Diffusion-based Convolutional Neural Network for Manifold-valued Graphs,” arXiv preprint arXiv:2401.14381, 2024.
- [100] I. Carrara, B. Aristimunha, M. C. Corsi, R. Y. de Camargo, S. Chevallier, and T. Papadopoulo, “Geometric Neural Network based on Phase Space for BCI decoding,” arXiv preprint arXiv:2403.05645, 2024.
- [101] X. Navarro-Sune, A. L. Hudson, F. D. V. Fallani, J. Martinerie, A. Witon, P. Pouget, and M. Chavez, “Riemannian geometry applied to detection of respiratory states from EEG signals: the basis for a brain–ventilator interface,” IEEE Transactions on Biomedical Engineering, vol. 64, no. 5, pp. 1138–1148, 2016.
- [102] C. H. Nguyen, G. K. Karavas, and P. Artemiadis, “Inferring imagined speech using EEG signals: a new approach using Riemannian manifold features,” Journal of neural engineering, vol. 15, no. 1, article 016002, 2017.
- [103] X. Li, Y. Qiao, L. Duan, and J. Miao, “EEG classification based on Grassmann manifold and matrix recovery,” Biomedical Signal Processing and Control, vol. 87, article 105491, 2024.
- [104] C. H. Nguyen and P. Artemiadis, “EEG feature descriptors and discriminant analysis under Riemannian Manifold perspective,” Neurocomputing, vol. 275, pp. 1871–1883, 2018.
- [105] X. Kan, Z. Li, H. Cui, Y. Yu, R. Xu, S. Yu, and C. Yang, “R-mixup: Riemannian mixup for biological networks,” in Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 1073–1085, August 2023.
- [106] L. Pan, K. Wang, L. Xu, X. Sun, W. Yi, M. Xu, and D. Ming, “Riemannian geometric and ensemble learning for decoding cross-session motor imagery electroencephalography signals,” Journal of Neural Engineering, vol. 20, no. 6, article 066011, 2023.
- [107] Y. Cai, Q. She, J. Ji, Y. Ma, J. Zhang, and Y. Zhang, “Motor imagery EEG decoding using manifold embedded transfer learning,” Journal of Neuroscience Methods, vol. 370, article 109489, 2022.
- [108] H. Fang, J. Jin, I. Daly, and X. Wang, “Feature extraction method based on filter banks and Riemannian tangent space in motor-imagery BCI,” IEEE journal of biomedical and health informatics, vol. 26, no. 6, pp. 2504–2514, 2022.
- [109] C. Larzabal, V. Auboiroux, S. Karakas, G. Charvet, A. L. Benabid, S. Chabardes, and S. Bonnet, “The Riemannian spatial pattern method: mapping and clustering movement imagery using Riemannian geometry,” Journal of Neural Engineering, vol. 18, no. 5, article 056014, 2021.
- [110] Y. Xu, H. Yin, W. Yi, X. Huang, W. Jian, C. Wang, and R. Hu, “Supervised and Semisupervised Manifold Embedded Knowledge Transfer in Motor Imagery-Based BCI,” Computational Intelligence and Neuroscience, 2022.

- [111] S. Chevallier, E. K. Kalunga, Q. Barthélemy, and E. Monacelli, “Review of Riemannian distances and divergences, applied to SSVEP-based BCI,” Neuroinformatics, vol. 19, no. 1, pp. 93–106, 2021.
- [112] C. Gao, H. Uchitomi, and Y. Miyake, “Cross-Sensory EEG Emotion Recognition with Filter Bank Riemannian Feature and Adversarial Domain Adaptation,” Brain Sciences, vol. 13, no. 9, article 1326, 2023.
- [113] M. Wu, S. Hu, B. Wei, and Z. Lv, “A novel deep learning model based on the ICA and Riemannian manifold for EEG-based emotion recognition,” Journal of Neuroscience Methods, vol. 378, article 109642, 2022.
- [114] A. Bleuzé, J. Mattout, and M. Congedo, “Tangent space alignment: Transfer learning for Brain-Computer Interface,” Frontiers in Human Neuroscience, vol. 16, article 1049985, 2022.
- [115] M. S. Yamamoto, K. Sadatnejad, T. Tanaka, M. R. Islam, F. Dehais, Y. Tanaka, and F. Lotte, “Modeling complex EEG data distribution on the Riemannian manifold toward outlier detection and multimodal classification,” IEEE Transactions on Biomedical Engineering, 2023.
- [116] F. Tang, M. Fan, and P. Tiˇno, “Generalized learning Riemannian space quantization: A case study on Riemannian manifold of SPD matrices,” IEEE Transactions on Neural Networks and Learning Systems, vol. 32, no. 1, pp. 281–292, 2020.
- [117] D. Gurve, D. Delisle-Rodriguez, T. Bastos, and S. Krishnan, “Motor Imagery Classification with Covariance Matrices and Non-Negative Matrix Factorization,” in 2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pp. 3083–3086, July 2019.
- [118] C. Ju, R. J. Kobler, L. Tang, C. Guan, and M. Kawanabe, “Deep Geodesic Canonical Correlation Analysis for Covariance-Based Neuroimaging Data,” in The Twelfth International Conference on Learning Representations, October 2023.
- [119] D. Sabbagh, P. Ablin, G. Varoquaux, A. Gramfort, and D. A. Engemann, “Manifold-regression to predict from MEG/EEG brain signals without source modeling,” Advances in Neural Information Processing Systems, vol. 32, 2019.
- [120] Y. T. Pan, J. L. Chou, and C. S. Wei, “MAtt: A manifold attention network for EEG decoding,” Advances in Neural Information Processing Systems, vol. 35, pp. 31116–31129, 2022.
- [121] S. Chevallier, E. K. Kalunga, Q. Barthélemy, and E. Monacelli, “Review of Riemannian distances and divergences, applied to SSVEP-based BCI,” Neuroinformatics, vol. 19, no. 1, pp. 93–106, 2021.
- [122] C. Ju and C. Guan, “Graph Neural Networks on SPD Manifolds for Motor Imagery Classification: A Perspective From the Time–Frequency Analysis,” IEEE Transactions on Neural Networks and Learning Systems, 2023.
- [123] N. Ivanov and T. Chau, “Riemannian geometry-based metrics to measure and reinforce user performance changes during brain-computer interface user training,” Frontiers in Computational Neuroscience, vol. 17, article 1108889, 2023.
- [124] Y. Gao, X. Sun, M. Meng, and Y. Zhang, “EEG emotion recognition based on enhanced SPD matrix and manifold dimensionality reduction,” Computers in biology and medicine, vol. 146, 105606, 2022.
- [125] J. Li, G. Liao, Y. Huang, Z. Zhang, and A. Nehorai, “Riemannian geometric optimization methods for joint design of transmit sequence and receive filter on MIMO radar,” IEEE Transactions on Signal Processing, vol. 68, pp. 5602–5616, 2020.

