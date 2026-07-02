# Manifold Embedded Knowledge Transfer for Brain-Computer Interfaces

Wen Zhang and Dongrui Wu

arXiv:1910.05878v2[cs.HC]29Feb2020

Abstract—Transfer learning makes use of data or knowledge in one problem to help solve a different, yet related, problem. It is particularly useful in brain-computer interfaces (BCIs), for coping with variations among different subjects and/or tasks. This paper considers ofﬂine unsupervised cross-subject electroencephalogram (EEG) classiﬁcation, i.e., we have labeled EEG trials from one or more source subjects, but only unlabeled EEG trials from the target subject. We propose a novel manifold embedded knowledge transfer (MEKT) approach, which ﬁrst aligns the covariance matrices of the EEG trials in the Riemannian manifold, extracts features in the tangent space, and then performs domain adaptation by minimizing the joint probability distribution shift between the source and the target domains, while preserving their geometric structures. MEKT can cope with one or multiple source domains, and can be computed efﬁciently. We also propose a domain transferability estimation (DTE) approach to identify the most beneﬁcial source domains, in case there are a large number of source domains. Experiments on four EEG datasets from two different BCI paradigms demonstrated that MEKT outperformed several stateof-the-art transfer learning approaches, and DTE can reduce more than half of the computational cost when the number of source subjects is large, with little sacriﬁce of classiﬁcation accuracy.

Index Terms—Brain-computer interfaces, electroencephalogram, Riemannian manifold, transfer learning

I. INTRODUCTION

A brain-computer interface (BCI) provides a direct communication pathway between a user’s brain and a computer [1],

- [2]. Electroencephalogram (EEG), a multi-channel time-series, is the most frequently used BCI input signal. There are three common paradigms in EEG-based BCIs: motor imagery (MI)
- [3], event-related potentials (ERPs) [4], and steady-state visual evoked potentials [2]. The ﬁrst two are the focus of this paper.

In MI tasks, the user needs to imagine the movements of his/her body parts, which causes modulations of brain rhythms in the involved cortical areas. In ERP tasks, the user is stimulated by a majority of non-target stimuli and a few target stimuli; a special ERP pattern appears in the EEG response after the user perceives a target stimulus. EEG-based BCI systems have been widely used to help people with disabilities, and also the able-bodied [1].

A standard EEG signal analysis pipeline consists of temporal (band-pass) ﬁltering, spatial ﬁltering, and classiﬁcation [5]. Spatial ﬁlters such as common spatial patterns (CSP) [6]

W. Zhang and D. Wu are with the Ministry of Education Key Laboratory of Image Processing and Intelligent Control, School of Artiﬁcial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China. Email: wenz@hust.edu.cn, drwu@hust.edu.cn.

Dongrui Wu is the corresponding author.

are widely used to enhance the signal-to-noise ratio. Recently, there is a trend to utilize the covariance matrices of EEG trials, which are symmetric positive deﬁnite (SPD) and can be viewed as points on a Riemannian manifold, in EEG signal analysis [7]–[9]. For MI tasks, the discriminative information is mainly spatial, and can be directly encoded in the covariance matrices. On the contrary, the main discriminative information of ERP trials is temporal. A novel approach was proposed in [10] to augment each EEG trial by the mean of all target trials that contain the ERP, and then their covariance matrices are computed. However, Riemannian space based approaches are computationally expensive, and not compatible with Euclidean space machine learning approaches.

A major challenge in BCIs is that different users have different neural responses to the same stimulus, and even the same user can have different neural responses to the same stimulus at different time/locations. Besides, when calibrating the BCI system, acquiring a large number of subjectspeciﬁc labeled training examples for each new subject is timeconsuming and expensive. Transfer learning [11]–[15], which uses data/information from one or more source domains to help the learning in a target domain, can be used to address these problems. Some representative applications of transfer learning in BCIs can be found in [16]–[21]. Many researchers [19]–[21] attempted to seek a set of subject-invariant CSP ﬁlters to increase the signal-to-noise ratio. Another pipeline is Riemannian geometry based. Zanini et al. [22] proposed a Riemannian alignment (RA) framework to align the EEG covariance matrices from different subjects. He and Wu [23] extended RA to Euclidean alignment (EA) in the Euclidean space, so that any Euclidean space classiﬁer can be used after it.

To utilize the excellent properties of the Riemannian geometry and avoid its high computational cost, as well as to leverage knowledge learned from the source subjects, this paper proposes a manifold embedded knowledge transfer (MEKT) framework, which ﬁrst aligns the covariance matrices of the EEG trials in the Riemannian manifold, then performs domain adaptation in the tangent space by minimizing the joint probability distribution shift between the source and the target domains, while preserving their geometric structures, as illustrated in Fig. 1. Additionally, we propose a domain transferability estimation (DTE) approach to select the most beneﬁcial subjects in multi-source transfer learning. Experiments on four datasets from two different BCI paradigms (MI and ERP) veriﬁed the effectiveness of MEKT and DTE.

The remainder of this paper is organized as follows: Section II introduces related work on spatial ﬁlters, Riemannian

Source Domain 2

Source Domain 1

Centroid

Alignment

Target Domain

Tangent

Space

Learned Subspace

Tangent

Feature Extraction

Riemannian Manifold

Space

Fig. 1. Illustration of our proposed MEKT. Squares and circles represent examples from different classes. Different colors represent different domains. All domains are ﬁrst aligned on the Riemannian manifold, and then mapped onto a tangent space. A and B are projection matrices of the source and the target domains, respectively.

geometry, tangent space mapping, RA, EA, and subspace adaptation. Section III describes the details of the proposed MEKT and DTE. Section IV presents experiments to compare the performance of MEKT with several state-of-the-art data alignment and transfer learning approaches. Finally, Section V draws conclusions.

II. RELATED WORK

This section introduces background knowledge on spatial ﬁlters, Riemannian geometry, tangent space mapping, RA, EA, and subspace adaptation, which will be used in the next section.

- A. Spatial Filters

Spatial ﬁltering can be viewed as a data-driven dimensionality reduction approach that promotes the variance difference between two conditions [24]. It is common in MI-based BCIs to use CSP ﬁlters [25] to simultaneously diagonalize the two intra-class covariance matrices.

Consider a binary classiﬁcation problem. Let (Xi,yi) be the ith labeled training example, where Xi ∈ Rc×t, in which c is the number of EEG channels, and t the number of time domain samples. For Class k (k = 0,1), CSP ﬁnds a spatial ﬁlter matrix Wk∗ ∈ Rc×f, where f is the number of spatial ﬁlters, to maximize the variance difference between Class k and Class 1 − k:

tr(W⊤Σ¯kW) tr[W⊤Σ¯1−kW]

Wk∗ = arg max

, (1)

[Figure 1]

W∈Rc×f

where Σ¯k is the mean covariance matrix of all EEG trials in Class k, and tr is the trace of a matrix. The solution Wk∗ is the concatenation of the f leading eigenvectors of the matrix (Σ¯1−k)−1Σ¯k.

Finally, we concatenate the 2f spatial ﬁlters from both classes to obtain the complete CSP ﬁlters:

W∗ = [W0∗,W1∗] ∈ Rc×2f (2) and compute the spatially ﬁltered Xi by:

Xi′ = (W∗)⊤Xi ∈ R2f×t (3)

The log-variances of the ﬁltered trial X′ can be extracted:

diag(X′X′⊤) tr(X′X′⊤)

x = log

(4) and used as input features in classiﬁcation.

[Figure 2]

- B. Riemannian Geometry

All SPD matrices P ∈ Rc×c form a differentiable Riemannian manifold. Riemannian geometry is used to manipulate them. Some basic deﬁnitions are provided below.

The Riemannian distance between two SPD matrices P1 and P2 is:

δ (P1,P2) = log P1−1P2 F , (5) where · F is the Frobenius norm, and log donates the logarithm of the eigenvalues of P1−1P2.

The Riemannian mean of {Pi}ni=1 is:

MR = arg min

P

n

i=1

δ2(P,Pi), (6)

The Euclidean mean is:

ME =

1 n

[Figure 3]

n

i=1

Pi, (7)

The Log-Euclidean mean [7] is:

ML = exp

n

i=1

wi log Pi , (8)

where wi is usually set to n1.

[Figure 4]

- C. Tangent Space Mapping Tangent space mapping is also known as the logarithmic

mapping, which maps a Riemannian space SPD matrix Pi to a Euclidean tangent space vector xi around an SPD matrix M, which is usually the Riemannian or Euclidean mean:

xi = upper (logM (MrefPiMref)), (9)

where upper takes the upper triangular part of a c × c SPD matrix and forms a vector xi ∈ R1×c(c+1)/2, and Mref is a reference matrix. To obtain a tangent space locally homomorphic to the manifold, Mref = M−1/2 is needed [24].

Congruent transform and congruence invariance [26] are two important properties in the Riemannian space:

M (FP1F,FP2F) = F · M(P1,P2) · F, (10) δ G⊤P1G,G⊤P2G = δ (P1,P2), (11)

where M is the Euclidean or Riemannian mean operation, F is a nonsingular square matrix, and G ∈ Rc×c is an invertible symmetric matrix. (11) suggests that the Riemannian distance between two SPD matrices does not change, if both are left and right multiplied by an invertible symmetric matrix.

- D. Riemannian Alignment (RA) RA [22] ﬁrst computes the covariance matrices of some

resting (or non-target) trials, {Pi}ni=1, in which the subject is not performing any task (or not performing the target task),

and then the Riemannian mean MR of these matrices, which is used as the reference matrix to reduce the inter-session or inter-subject variations, by the following transformation:

Pi′ = MR−1/2PiMR−1/2, (12)

where Pi is the covariance matrix of the i-th trial, and Pi′ the corresponding aligned covariance matrix. Then, all Pi′ can be classiﬁed by a minimum distance to mean (MDM) classiﬁer [8].

- E. Euclidean Alignment (EA)

Although RA-MDM has demonstrated promising performance, it still has some limitations [23]: 1) it processes the covariance matrices in the Riemannian space, whereas there are very few Riemannian space classiﬁers; 2) it computes the reference matrix from the non-target stimuli in ERP-based BCIs, which requires some labeled trials from the new subject.

EA [23] extends RA and solves the above problems by transforming an EEG trial Xi in the Euclidean space:

Xi′ = ME−1/2Xi, (13)

where ME is the Euclidean mean of the covariance matrices of all EEG trials, computed by (7).

However, EA only considers the marginal probability distribution shift, and works best when the number of EEG channels is small. When there are a large number of channels, computing ME−1/2 may be numerically unstable.

- F. Subspace Adaptation

Tangent space vectors usually have very high dimensionality, so they cannot be used easily in transfer learning. An intuitive approach is to align them in a lower dimensional subspace. Pan et al. [11] proposed transfer component analysis (TCA) to learn the transferable components across domains in a reproducible kernel Hilbert space using maximum mean discrepancy (MMD) [27]. Joint distribution adaptation (JDA)

[14] improves TCA by considering the conditional distribution shift using pseudo label reﬁnement. Joint geometrical and statistical alignment (JGSA) [15] further improves JDA by adding two regularization terms, which minimize the withinclass scatter matrix and maximize the between-class scatter matrix.

III. MANIFOLD EMBEDDED KNOWLEDGE TRANSFER (MEKT)

This section proposes the MEKT approach. Its goal is to use one or multiple source subjects’ data to help the target subject, given that they have the same feature space and label space. For the ease of illustration, we focus on a single source domain ﬁrst.

Assume the source domain has nS labeled instances {(XS,i,yS,i)}n

i=1, where XS,i ∈ Rc×t is the i-th feature matrix, and yS,i ∈ {1,...,l} is the corresponding label, in which c, t and l denote the number of channels, time domain samples, and classes, respectively. Let yS = [yS,1;··· ;yS,n

S

] ∈ RnS×1 be the label vector of the source domain. Assume also the target domain has nT unlabeled feature matrices {XT,i}n

S

T

i=1, where XT,i ∈ Rc×t.

MEKT consists of the following three steps:

- 1) Covariance matrix centroid alignment (CA): Align the

centroids of the covariance matrices of {XS,i}n

S

i=1 and {XT,i}n

T

i=1, so that their marginal probability distributions are close.

- 2) Tangent space feature extraction: Map the aligned covariance matrices to a tangent space feature matrix

XS ∈ Rd×nS

, and XT ∈ Rd×nT

, where d = c(c +1)/2 is the dimensionality of the tangent space features.

- 3) Mapping matrices identiﬁcation: Find projection matrices A ∈ Rd×p and B ∈ Rd×p, where p ≪ d is the dimensionality of a shared subspace, such that A⊤XS and B⊤XT are close.

After MEKT, a classiﬁer can be trained on (A⊤XS,yS) and applied to B⊤XT to obtain the target pseudo labels yˆT.

Next, we describe the details of the above three steps.

A. Covariance Matrix Centroid Alignment (CA)

CA serves as a preprocessing step to reduce the marginal probability distribution shift of different domains, and enables transfer from multiple source domains.

Let PS,i = XS,iXS,i⊤ be the i-th covariance matrix in the source domain, and Mref = M−1/2, where M can be the Riemannian mean in (6), the Euclidean mean in (7), or the Log-Euclidean mean in (8). Then, we align the covariance matrices by

PS,i′ = MrefPS,iMref, i = 1,...,nS (14) Likewise, we can obtain the aligned covariance matrices

{PT,i′ }n

T

i=1 of the target domain. CA has two desirable properties:

- 1) Marginal probability distribution shift minimization. From the properties of congruent transform and congruence invariance, we have

M(Mref⊤P1Mref,...,Mref⊤Pn

S

Mref)

= Mref⊤M(P1,...,Pn

S

)Mref = Mref⊤MMref = I,

(15)

i.e., if we choose M as the Riemannian (or Euclidean) mean, then different domains’ geometric (or arithmetic) centers all equal the identity matrix. Therefore, the marginal distributions of the source and the target domains are brought closer on the manifold.

- 2) EEG trial whitening. In the following, we show that each aligned covariance matrix is approximately an identity matrix after CA. If we decompose the reference matrix as Mref =

w1,...,wc , then the (m,n)-th element of PS,i′ is:

PS,i′ (m,n) = wm⊤PS,iwn, (16) From (15) we have

wm⊤M(P1,...,Pn

S

)wn =

1, m = n 0, m = n

. (17)

The above equation holds no matter whether M is the Riemannian mean, or the Euclidean mean. For CA using the Euclidean mean, the average of the m-th diagonal element of {PS,i′ }n

S

i=1 is 1 nS

nS

PS,i′ (m,m) = wm⊤M(P1,...,Pn

)wm = 1,

[Figure 5]

S

i=1

(18) Meanwhile, for each diagonal element, we have PS,i′ (m,m) = XS,i⊤ wm 22 > 0, therefore the diagonal elements of PS,i′ are around 1. Similarly, the off-diagonal elements of PS,i′ are around 0. Thus, PS,i′ is approximatively an identify matrix, i.e., the aligned EEG trials are approximated whitened. CA with the Riemannian mean is an iterative process initialized by the Euclidean mean. CA with the LogEuclidean mean is an approximation of CA with the Riemannian mean, with reduced computational cost [7]. So, (18) also holds approximately for these two means. This whitening effect will also be experimentally demonstrated in Section IV-E.

- B. Tangent Space Feature Extraction

After covariance matrix CA, we map each covariance matrix to a tangent space feature vector in Rd×1:

xS,i = upper log PS,i′ , i = 1,...,nS (19) xT,i = upper log PT,i′ , i = 1,...,nT (20)

Note that this is different from the original tangent space mapping in (9), in that (9) uses the same reference matrix Mref for all subjects, whereas our approach uses a subject-speciﬁc Mref for each different subject.

] and XT = [xT,i,...,xT,n

Next, we form new feature matrices XS = [xS,i,...,xS,n

S

].

T

C. Mapping Matrices Identiﬁcation

CA does not reduce the conditional probability distribution discrepancies. We next ﬁnd projection matrices A,B ∈ Rd×d

′

,

which map XS and XT to lower dimensional matrices A⊤XS and B⊤XT, with the following desirable properties:

1) Joint probability distribution shift minimization. In traditional domain adaptation [11], [14], MMD is frequently used to reduce the marginal and conditional probability distribution discrepancies between the source and the target domains, i.e.,

DS,T ≈ D (Q (XS),Q (XT))

+ D (Q (yS|XS),Q (yˆT|XT))

2

nS

nT

1 nT

1 nS

A⊤xS,i −

B⊤xT,j

=

[Figure 6]

[Figure 7]

i=1

j=1

F

2

nkS

nkT

l

1 nkS

1 nkT

A⊤xkS,i −

B⊤xkT,j

+

,

[Figure 8]

[Figure 9]

i=1

j=1

k=1

F

(21)

where xkS,i and xkT,j are the tangent space vectors in the k-th (k = 1,...,l) class of the source domain and

the target domain, respectively, and nkS and nkT are the number of examples in the k-th class of the source domain and the target domain, respectively. Next, we propose a new measure, joint probability MMD, to quantify the probability distribution shift between the source and the target domains, by considering the joint probability directly, instead of the marginal and the conditional probabilities separately. Then, the joint probability MMD between the source and the target domains is:

DS,T′ = D (Q (XS,yS) ,Q (XT,yˆT))

= D (Q (XS|yS)Q(yS),Q (XT|yˆT)Q(yˆT))

nkS

nkT

l

P(yˆTk ) nkT

P(ySk) nkS

A⊤xkS,i −

B⊤xkT,j

≈

[Figure 10]

[Figure 11]

i=1

j=1

k=1

2

nkS

nkT

l

1 nS

1 nT

A⊤xkS,i −

B⊤xkT,j

=

,

[Figure 12]

[Figure 13]

i=1

j=1

k=1

F

(22) Let the one-hot encoding matrix of the source domain label vector1 yS be YS, and the one-hot encoding matrix of the predicted target label vector yˆT be YˆT. (22) can be simpliﬁed as

DS,T′ = NS⊤XS⊤A − NT⊤XT⊤B 2F , (23) where

YˆT nT

YS nS

, NT =

. (24)

NS =

[Figure 14]

[Figure 15]

2

F

 1For example, for binary classiﬁcation with two classes 1 and 2, if yS = 

 

 , then YS =

 .

2

- 0 1
- 1 0 0 1

- 1
- 2

The joint probability MMD is based on the joint probability rather than the conditional probability, which in theory can handle more probability distribution shifts.

- 2) Source domain discriminability. During subspace mapping, the discriminating ability of the source domain can be preserved by:

min

A

tr(A⊤SwA) s.t. A⊤SbA = I, (25)

where Sw = lk=1 n

k S

i=1(xkS,i)⊤xkS,ihk is the withinclass scatter matrix, in which hk = 1 − n1

[Figure 16]

k S

, and

Sb = lk=1 nk ( ¯mk − m¯ )( ¯mk − m¯ )⊤ is the betweenclass scatter matrix, in which m¯ k is the mean of samples from Class k, and m¯ is the mean of all samples.

- 3) Target domain locality preservation. We also introduce a graph-based regularization term to preserve the local structure in the target domain. Under the manifold

assumption [28], if two samples xT,i and xT,j are close in the original target domain, then they should also be close in the projected subspace. Let S ∈ RnT×nT be a similarity matrix:

Sij =

 



e

− xT,i−xT,j

2 2

[Figure 17]

2σ2

, if xT,i ∈ Np(xT,j)

or xT,j ∈ Np(xT,i) 0, otherwise

, (26)

where Np(xT,i) is the set of the p-nearest neighbors of xT,i, and σ is a scaling parameter, which usually equals 1 [29]. Using the normalized graph Laplacian matrix L = I − D−1/2SD−1/2, where D is a diagonal matrix with Dii = nj=1T Sij, graph regularization is expressed as:

nT

i,j=1

B⊤xT,i − B⊤xT,j 22Sij = tr(B⊤XTLXT⊤B),

(27)

To remove the scaling effect, we add a constraint on the target embedding [30]:

min

B

tr(B⊤XTLXT⊤B) s.t. B⊤XTHXT⊤B = I,

(28)

where H = I − n1

[Figure 18]

T

1n

T

is the centering matrix, in which 1n

T

∈ RnT×nT is an all-one matrix.

- 4) Parameter transfer and regularization. Since the source and the target domains have the same feature space, and CA has brought their probability distributions closer, we want the projection matrix B to be similar to the projection matrix A learned in the source domain. Additionally, for better generalization performance, we want to ensure that A and B do not include extreme values. Thus, we have the following constraints on the projection matrices:

min

A,B

B − A 2F + B 2F . (29)

- D. The Overall Loss Function of MEKT

Integrating all regularization and constraints above, the formulation of MEKT is:

min

A,B

αtr(A⊤SwA) + β tr(B⊤XTLXT⊤B) + DS,T′

+ ρ( B − A 2F + B 2F) s.t. B⊤XTHXT⊤B = I, A⊤SbA = I

(30)

where α, β and ρ are trade-off parameters to balance the importance of the source domain discriminability, the target domain locality, and the parameter regularization, respectively.

Let W = [A;B]. Then, the Lagrange function is J = tr W⊤(αP + βL + ρU + R)W + η(I − W⊤V W)

(31) where

P =

Sw 0 0 0

, L =

0 0 0 XTLXT⊤

, (32)

U =

I −I −I 2I

, V =

Sb 0 0 XTHXT⊤

, (33)

R =

XSNSNS⊤XS⊤ −XSNSNT⊤XT⊤ −XTNTNS⊤XS⊤ XTNTNT⊤XT⊤

, (34)

Setting the derivative ∇WJ = 0, we have (αP + βL + ρU + R)W = ηV W (35)

(35) can be solved by generalized eigen-decomposition, and W consists of the p trailing eigenvectors. Since YˆT is needed in NT [see (24)], and hence R, we use a general expectationmaximization like pseudo label reﬁnement procedure [14] to reﬁne the estimation, as shown in Algorithm 1.

Note that for the clarity of explanation, Algorithm 1 only considers one source domain. When there are multiple source domains, we perform CA and compute the tangent space

feature vectors XS(i) ∈ Rd×n

(i)

S for each source domain separately, and then assemble their feature vectors into a single source domain feature matrix XS = [XS(1),...,XS(z)] ∈ Rd×n

∗

,

where nS(i) is the number of trails in the i-th source domain, z is the number of source domains, and n∗ = zi=1 n(Si).

- E. Kernelization Analysis

Nonlinear MEKT can be achieved through kernelization in a Reproducing Kernel Hilbert Space [15].

Let the kernel function be φ : x  → φ(x). Deﬁne Φ(X) = [φ(x1),..,φ(xn)] ∈ Rd×n, where n = nS + nT. We use the Representer Theorem [31] A = Φ(X)A and B = Φ(X)B to kernelize MEKT, where X = [XS,XT], and A ∈ Rn×p and B ∈ Rn×p are two projection matrices to be optimized.

Let KS = Φ(X)⊤Φ(XS) and KT = Φ(X)⊤Φ(XT). Then, all x are replaced by φ(x), XS by Φ(XS), and XT by Φ(XT), in the above derivations. The optimization problem becomes

α tr(A⊤SwA) + β tr(B⊤KTLKT⊤B)

min

A,B

+ NS⊤KS⊤A − NT⊤KT⊤B 2F + ρ(W⊤UW) s.t. B⊤KTHKT⊤B = I, A⊤SbA = I

(36)

[Figure 19]

Algorithm 1: Manifold Embedded Knowledge Transfer (MEKT)

[Figure 20]

Input: nS source domain samples {(XS,i,yS,i)}n

S

i=1, where XS,i ∈ Rc×t and yS,i ∈ {1,...,l};

nT target domain feature matrices {XT,i}n

T

i=1,

where XT,i ∈ Rc×t; Number of iterations N; Weights α, β, ρ; Dimensionality of the shared subspace, p.

Output: yˆT ∈ RnT×1, the labels for {XT,i}n

T

i=1. Calculate the covariance matrices {PS,i}n

S

i=1 and their mean matrix M in the source domain, using (6), (7), or

(8); Calculate {PS,i′ }n

S

i=1 using (14); Map each PS,i′ to a tangent space feature vector

xS,i ∈ Rd×1 using (19) (d = c(c + 1)/2); Repeat the above procedure to get xT,i ∈ Rd×1 using

(20); Form XS = [xS,1,...,xS,n

];

] and XT = [xT,1,...,xT,n

T

S

Construct P, L, U, V and R in (32)-(34); for n = 1,...,N do

Solve (35), and construct W ∈ R2d×p as the p trailing eigenvectors; Construct A as the ﬁrst d rows in W, and B as the last d rows; Train a classiﬁer f on (A⊤XS,yS) and apply it to

[Figure 21]

B⊤XT to update yˆT; Update R in (34).

end return yˆT.

[Figure 22]

where Sw = lk=1 KSkHSk(KSk)⊤, in which KSk is the part of KS from Class k only, and HSk = I − n1

1 the centering matrix. The Laplacian matrix L is constructed in the original data space. In Sb, m¯ k is the mean of KSk, and m¯ the mean of K = [KS,KT]. U is obtained by replacing I in (33) with K.

[Figure 23]

k S

(36) can be optimized in a similar way as (30).

F. Domain Transferability Estimation (DTE)

When there are a large number of source domains, estimating domain transferability can advise which domains are more important, and also reduce the computational cost. In BCIs, DTE can be used to ﬁnd subjects which have low correlations to the tasks and hence may cause negative transfer. Although source domain selection is important, it is very challenging, and hence very few publications can be found in the literature [4], [13], [32], [33].

Next, we propose an unsupervised DTE strategy. Assume there are z labeled sources domains Si = {XS(i),yS(i)}zi=1, where XS(i) is the feature matrix of the ith source domain, yS(i) is the corresponding label vector. Assume also there is a target domain T with unlabeled feature matrix XT. Let Sb be the between-class scatter matrix, similar to Sb in (25), and SS

i,T

b be the scatter matrix between the source and the target domains. We deﬁne the discriminability of the i-th source domain as DIS(Si) = SS

i

b 1, and the

difference between the source domain and the target domain as DIF(Si,T) = SS

i,T

b 1.

Then, the transferability of Source Domain Si is computed as:

DIS(Si) DIF(Si,T)

r(Si,T) =

(37) We then select z∗ ∈ (1,z) source subjects with the highest

[Figure 24]

r(Si,T).

IV. EXPERIMENTS

In this section, we evaluate our method for both singlesource to single-target (STS) transfers and multi-source to single-target (MTS) transfers. The code is available online2.

A. Datasets

We used two MI datasets and two ERP datasets in our experiments. Their statistics are summarized in Table I.

TABLE I STATISTICS OF THE TWO MI AND TWO ERP DATASETS.

[Figure 25]

[Figure 26]

Number of Number of Number of Trails per ClassSubjects Channels Time Samples Subject Imbalance

Dataset

[Figure 27]

[Figure 28]

[Figure 29]

MI1 7 59 300 200 No MI2 9 22 750 144 No

[Figure 30]

[Figure 31]

RSVP 11 8 45 368-565 Yes ERN 16 56 260 340 Yes

[Figure 32]

[Figure 33]

For both MI datasets, a subject sat in front of a computer screen. At the beginning of a trial, a ﬁxation cross appeared on the black screen to prompt the subject to be prepared. Shortly after, an arrow pointing to a certain direction was presented as a visual cue for a few seconds, during which the subject performed a speciﬁc MI task. Then, the visual cue disappeared, and the next trial started after a short break. EEG signal was recorded during the experiment, and used to classify which MI the user was performing. Usually, EEG shortly after the visual cue onset is highly related to the MI task.

Visual Cue: Motor Imagery

Break Next Trial

Fixation Cross

0 1 2 3 4 5 6 7 8 t (s)

Fig. 2. Timing scheme of the motor imagery tasks in the ﬁrst two datasets.

For the ﬁrst MI dataset3 (MI1), 59-channel EEGs were recorded at 100 Hz from seven healthy subjects, each with 100 left hand MIs and 100 right hand MIs. For the second MI dataset4 (MI2), 22-channel EEGs were recorded at 250 Hz from nine heathy subjects, each with 72 left hand MIs and 72 right hand MIs. Both datasets were used for two-class classiﬁcation.

- 2https://github.com/chamwen/MEKT
- 3http://www.bbci.de/competition/iv/desc 1.html.

[Figure 34]

- 4http://www.bbci.de/competition/iv/desc 2a.pdf.

[Figure 35]

The ﬁrst ERP dataset5 contained 8-channel EEG recordings from 11 healthy subjects in a rapid serial visual presentation (RSVP) experiment. The images were presented at different rates (5, 6, and 10 Hz) in three different experiments. We only used the 5 Hz version. The goal was to classify from EEG if the subject had seen a target image (with airplane) and non-target image (without airplane). The number of images for different subjects varying between 368 and 565, and the target to non-target ratio was around 1:9. The sampling rate was 2048 Hz, and the RSVP data had been band-pass ﬁltered to 0.15-28 Hz.

The second ERP dataset6 was recorded from a feedback error-related negativity (ERN) experiment [34], which was used in a Kaggle competition for two-class classiﬁcation. It was collected from 26 subjects and partitioned into training set (16 subjects) and test set (10 subjects). We only used the 16 subjects in the training set as we do not have access to the test set. The average target to non-target ratio was around 1:4. The 56-channel EEG data had been downsampled to 200 Hz.

B. EEG Data Preprocessing

EEG signals from all datasets were preprocessed using the EEGLAB toolbox [35]. We followed the same preprocessing procedures in [23], [36].

For the two MI datasets, a causal 50-order 8-30 Hz7 ﬁnite impulse response (FIR) band-pass ﬁlter was used to remove muscle artifacts and direct current drift, and hence to obtain cleaner MI signals. Next, EEG signals between [0.5,3.5] seconds after the cue onsets were extracted as trials. The RSVP signal was downsampled to 64 Hz to reduce the computational cost, and epoched to 0.7s intervals immediately after the stimulus onsets as trials. The ERN signal was bandpass ﬁltered to 1-40 Hz, and epoched to 1.3s intervals immediately after the feedbacks (which contained the ERP associated with the user’s response to the feedback event) as trials.

MI1 had 59 EEG channels, which were not easy to manipulate. Thus, we reduced the number of its tangent space features to the number of source domain samples (200), according to their F values in one-way ANOVA. For the ERN dataset, we used xDAWN [38] to reduce the number of channels from 56 to 6.

The dimensionalities of different input spaces are shown in Table II. ni is the number of samples in the i-th domain, and c the number of selected channels for the two ERP datasets. Speciﬁcally, for RSVP, c = 8 and ni varies from 368 to 565; for ERN, c = 6 and ni = 340. Augmented covariance matrices [10] were used in the Riemannian space for ERP, so they had dimensionality of 2c × 2c. Only the c × c upper right block of the augmented covariance matrix contains temporal information [10], so these c2 elements were selected as the tangent space features.

Next, we describe how the Euclidean space features were determined. For the two MI datasets, six log-variance features

- 5https://www.physionet.org/physiobank/database/ltrsvp/.
- 6https://www.kaggle.com/c/inria-bci-challenge. 7We bandpass ﬁltered the EEG signal to 8-30 Hz because MI is mainly

indicated by the change of the mu rhythm (about 813 Hz) and the beta (about 1430 Hz) rhythm [37].

TABLE II INPUT SPACE DIMENSIONALITIES IN DIFFERENT STS TASKS.

[Figure 36]

[Figure 37]

MI1 MI2 ERP (RSVP and ERN) Euclidean 6×200 6×144 20×ni

[Figure 38]

[Figure 39]

Tangent 200×200 253×144 c2 × ni Riemannian 59×59×200 22×22×144 2c × 2c × ni

[Figure 40]

[Figure 41]

[Figure 42]

of the CSP ﬁltered trials [see (4)] were used as features. For the two ERP datasets, after spatial ﬁltering by xDAWN, we assembled each EEG trail (which is a matrix) into a vector, performed principal component analysis on all vectors from the source subjects, and extracted the scores for the ﬁrst 20 principal components as features.

C. Baseline Algorithms

We compared our MEKT approaches (MEKT-R: the Riemannian mean is used as the reference matrix; MEKT-E: the Euclidean mean is used as the reference matrix; MEKT-L: the Log-Euclidean mean is used as the reference matrix) with seven state-of-the-art baseline algorithms for BCI classiﬁcation. According to the feature space type, these baselines can be divided into three categories:

- 1) Euclidean space approaches:

- a) CSP-LDA (linear discriminant analysis) [39] for MI, and CSP-SVM (support vector machine) [40] for ERP.
- b) EA-CSP-LDA for MI, and EA-xDAWN-SVM for ERP, i.e., we performed EA [23] as a preprocessing step before spatial ﬁltering and classiﬁcation.

- 2) Riemannian space approach: RA-MDM [22] for MI, and xDAWN-RA-MDM for ERP.
- 3) Tangent space approaches, which were proposed for computer vision applications, and have not been used in BCIs before. CA was used before each of them. In each learned subspace, the sLDA classiﬁer [41] was used for MI, and SVM for ERP.

- a) CA (centroid alignment).
- b) CA-CORAL (correlation alignment) [12].
- c) CA-GFK (geodesic ﬂow kernel) [13].
- d) CA-JDA (joint distribution adaptation) [14].
- e) CA-JGSA (joint geometrical and statistical alignment) [15].

Hyper-parameters of all baselines were set according to the recommendations in their corresponding publications. For MEKT, T = 5, α = 0.01, β = 0.1, ρ = 20, and d = 10 were used.

D. Experimental Settings

We evaluated unsupervised STS and MTS transfers. In STS, one subject was selected as the target, and another as the source. Let z be the number of subjects in a dataset. Then, there were z(z − 1) different STS tasks. In MTS, one subject was used as the target, and all others as the sources, so there were z different MTS tasks. For example, MI1 included seven subjects, so we had 7 × 6 = 42 STS tasks, e.g., S2→S1

(Subject 2 as the source, and Subject 1 as the target), S3→S1, S4→S1, S5→S1, S6→S1, S7→S1, ... S6→S7, and seven MTS tasks, e.g., {S2, S3, S4, S5, S6, S7}→S1, ..., {S1, S2, S3, S4, S5, S6}→S7.

domain samples and the target domain samples consistent, but also samples from the same class in the two domains close, which should beneﬁt the classiﬁcation.

The balanced classiﬁcation accuracy (BCA) was used as the performance measure:

| | |
|---|---|
| | |

l

tpk nk

1 l

, (38)

BCA =

[Figure 43]

[Figure 44]

k=1

where tpk and nk are the number of true positives and the number of samples in Class k, respectively.

- -20 -10 0 10 20
- -10

0

10

20

Raw

-5 0 5 10 15

| |
|---|

- -20
- -15
- -10
- -5

0

CA

-10 -5 0 5 10

- -20
- -15
- -10
- -5

E. Visualization

### CA-GFK

### CA-JDA

10

As explained in Section III-A, CA makes the aligned covariance matrices approximate the identity matrix, no matter whether the Riemannian mean, or the Euclidean mean, or the Log-Euclidean mean, is used as the reference matrix. To demonstrate that, Fig. 3 shows the raw covariance matrix of the ﬁrst EEG trial of Subject 1 in MI2, and the aligned covariance matrices using different references. The raw covariance matrix is nowhere close to identity, but after CA, the covariance matrices are approximately identity, and hence the corresponding EEG trials are approximately whitened.

0

5

0

| | | |
|---|---|---|
| | | |

| | |
|---|---|
| | |

- -10 0 10 20

| |
|---|

- -15
- -10
- -5

### MEKT-R

30

| | |
|---|---|
| | |

|[Figure 45]|
|---|

|[Figure 46]|
|---|

|Source Class 1<br><br>Source Class 2<br><br><br>Target Class 1<br><br>Target Class 2<br>|
|---|

|[Figure 47]|
|---|

|[Figure 48]|
|---|

- 0

- 0.5
- 1

- 1.5

20

20

5

5

10

10

10

15

15

15

10

0

20

20

-10 -5 0 5 10

5 10 15 20

5 10 15 20

Fig. 4. t-SNE visualization of the data distributions before and after CA, and with different transfer learning approaches, when transferring Subject 2’s data (source) to Subject 1 (target) in MI2.

|[Figure 49]|
|---|

|[Figure 50]|
|---|

|[Figure 51]|
|---|

|[Figure 52]|
|---|

- 0

- 0.5
- 1

- 1.5

5 10 15 20

5

- 0.5
- 1

10

F. Classiﬁcation Accuracies

The means and standard deviations of the BCAs on the four datasets with STS and MTS transfers are shown in Tables III and IV, respectively. All MEKT-based approaches achieved the best (in bold) or the second best (underlined) performance in all scenarios in contrast to the baselines.

15

0

20

5 10 15 20

5 10 15 20

- Fig. 3. The raw covariance matrix (Trial 1, Subject 1, MI2), and those after CA using different reference matrices.

Next, we used t-SNE [42] to reduce the dimensionality of the EEG trials to two, and visualize if MEKT can bring the data distributions of the source and the target domains together.

- Fig. 4 shows the results on transferring Subject 2’s data to Subject 1 in MI2, before and after different data alignment approaches. Before CA, the source domain and target domain samples do not overlap at all. After CA, the two sets of samples have identical mean, but different variances. CA-GFK and CA-JDA make the variance of the source domain samples and the variance of the target domain samples approximately identical, but different classes are still not well separated. MEKT-R not only makes the overall distributions of the source

Fig. 5 shows the BCAs of all tangent space based approaches when different reference matrices were used in CA. The Riemannian mean obtained the best BCA in four out of the six approaches, and also the best overall performance.

We also performed paired t-tests on the BCAs to check if the performance improvements of MEKT-R over others were statistically signiﬁcant. Before each t-test, we performed a Lilliefors test [43] to verify that the null hypothesis that the data come from a normal distribution cannot be rejected. Then, we performed false discovery rate corrections [44] by a linearstep up procedure under a ﬁxed signiﬁcance level (α = 0.05) on the paired p-values of each task.

The false discovery rate adjusted p-values (q-values) are shown in Table V. MEKT-R signiﬁcantly outperformed all

70

68

TABLE III MEAN (%) AND STANDARD DEVIATION (%; IN PARENTHESIS) OF THE BCAS IN STS TRANSFERS. FOR THE CA-BASED APPROACHES, THE SLDA CLASSIFIER WAS USED FOR MI, AND SVM FOR ERP.

## BCA(%)

66

64

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

MI1 MI2 Avg

[Figure 57]

- CSP-LDA 57.23 (10.56) 58.7 (11.58) 57.97 EA-CSP-LDA 66.85 (10.56) 65.00 (14.06) 65.93 RA-MDM 64.98 (10.37) 66.60 (12.60) 65.79 CA 66.17 (9.93) 66.02 (13.14) 66.10 CA-CORAL 67.69 (10.68) 67.26 (13.34) 67.48 CA-GFK 66.62 (10.53) 65.54 (13.56) 66.08 CA-JDA 66.01 (12.55) 66.59 (15.28) 66.30 CA-JGSA 65.81 (13.06) 65.90 (16.73) 65.85 MEKT-E 69.19 (12.84) 68.34 (15.51) 68.77 MEKT-L 70.74 (12.28) 68.56 (15.66) 69.65 MEKT-R 70.99 (12.46) 68.73 (15.73) 69.86

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

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

RSVP ERN Avg

[Figure 97]

[Figure 98]

[Figure 99]

- CSP-LDA 58.58 (7.98) 54.34 (5.87) 56.46 EA-CSP-LDA 58.76 (7.51) 55.57 (6.26) 57.17 RA-MDM 60.37 (8.05) 56.22 (6.89) 58.30 CA 58.34 (6.98) 56.97 (7.06) 57.66 CA-CORAL 58.45 (6.84) 57.04 (7.00) 57.75 CA-GFK 59.93 (7.61) 57.24 (7.34) 58.59 CA-JDA 60.27 (7.75) 57.56 (7.63) 58.92 CA-JGSA 55.23 (6.74) 57.17 (7.72) 56.20

62

CACA-CORALCA-GFK CA-JDACA-JGSA MEKT

Fig. 5. Average BCAs (%) of the tangent space approaches on the four datasets, when different reference matrices were used in CA.

baselines in almost all STS transfers. The performance improvements became less signiﬁcant when there were multiple source domains, which is reasonable, because generally in machine learning the differences between different algorithms diminish as the amount of training data increases.

[Figure 100]

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

TABLE V FALSE DISCOVERY RATE ADJUSTED p-VALUES IN PAIRED t-TESTS (α = 0.05).

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

MEKT-E 61.08 (8.59) 58.01 (7.76) 59.55 MEKT-L 61.15 (8.44) 57.91 (7.74) 59.53 MEKT-R 61.24 (8.36) 57.85 (7.75) 59.55

[Figure 129]

[Figure 130]

MEKT-R vs MI1 MI2 RSVP ERN

[Figure 131]

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

CSP-LDA .0000 .0000 – – xDAWN-SVM – – .0002 .0000 EA-CSP-LDA .0030 .0003 – – EA-xDAWN-SVM – – .0000 .0000 RA-MDM .0003 .0340 .0412 .0004 CA .0000 .0006 .0000 .0010 CA-CORAL .0005 .0340 .0000 .0014 CA-GFK .0000 .0001 .0016 .0130 CA-JDA .0003 .0183 .0386 .2627 CA-JGSA .0021 .0006 .0000 .0241

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

[Figure 152]

STS

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

TABLE IV MEAN (%) AND STANDARD DEVIATION (%; IN PARENTHESIS) OF THE BCAS IN MTS TRANSFERS.

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

CSP-LDA .0329 .1140 – – xDAWN-SVM – – .2077 .0306 EA-CSP-LDA .2808 .1636 – – EA-xDAWN-SVM – – .5733 .2632 xDAWN-RA-MDM .0824 .1636 .5347 .0632 CA .0329 .1260 .4727 .8380 CA-CORAL .0897 .1636 .3477 .9914 CA-GFK .0824 .1260 .5347 .9117 CA-JDA .2379 .1636 .0349 .0632 CA-JGSA .1344 .1636 .0323 .0018

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

MI1 MI2 Avg

[Figure 172]

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

CSP-LDA 59.71 (12.93) 67.75 (12.92) 63.73 EA-CSP-LDA 79.79 (6.57) 73.53 (15.96) 76.66 RA-MDM 73.29 (9.25) 72.07 (9.88) 72.68 CA 76.29 (9.66) 71.84 (13.89) 74.07 CA-CORAL 78.86 (8.73) 72.38 (13.38) 75.62 CA-GFK 76.79 (12.57) 72.99 (15.82) 74.89 CA-JDA 81.07 (11.19) 74.15 (15.77) 77.61 CA-JGSA 76.79 (12.35) 73.07 (16.33) 74.93

[Figure 178]

[Figure 179]

[Figure 180]

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

MTS

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

[Figure 211]

We also considered linear and radial basis function (RBF; kernel width 0.1) kernels in MEKT-R, and repeated the above experiments. The results are shown in Table VI, where Primal denotes the primal MEKT-R without kernelization. The primal MEKT-R achieved the best (in bold) or the second best (underlined) performance in all scenarios. However, the differences among the three approaches were very small.

[Figure 212]

[Figure 213]

[Figure 214]

[Figure 215]

MEKT-E 81.29 (10.18) 76.00 (17.61) 78.65 MEKT-L 83.07 (9.30) 76.54 (16.72) 79.81 MEKT-R 83.42 (9.55) 76.31 (16.76) 79.87

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

RSVP ERN Avg

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

CSP-LDA 65.36 (9.32) 61.87 (4.51) 63.62 EA-CSP-LDA 69.07 (9.05) 64.63 (5.86) 66.85 RA-MDM 67.29 (8.38) 62.90 (6.79) 65.10 CA 67.35 (7.52) 65.89 (7.30) 66.62 CA-CORAL 66.94 (7.46) 66.17 (7.74) 66.56 CA-GFK 67.75 (7.48) 66.03 (7.50) 66.89 CA-JDA 66.06 (6.18) 64.64 (6.50) 65.35 CA-JGSA 64.57 (5.79) 57.68 (8.04) 61.13

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

[Figure 247]

G. Computational Cost

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

This subsection empirically checked the computational cost of different algorithms, which were implemented in Matlab 2018a on a laptop with i7-8550U CPU@2.00GHz, 8GB memory, running 64-bit Windows 10 Education Edition.

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

MEKT-E 67.92 (6.70) 66.70 (8.00) 67.31 MEKT-L 68.40 (6.40) 65.98 (7.94) 67.19 MEKT-R 68.38 (6.36) 66.17 (7.68) 67.28

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

For simplicity, we only selected one transfer task in each dataset. For STS transfer, the ﬁrst subject in each dataset

TABLE VI AVERAGE BCAS(%) OF THE PROPOSED MEKT UNDER DIFFERENT KERNELS.

[Figure 268]

[Figure 269]

Primal Linear RBF

[Figure 270]

[Figure 271]

[Figure 272]

MI1 70.99 70.99 70.37 MI2 68.73 68.73 68.37

[Figure 273]

[Figure 274]

STS

[Figure 275]

[Figure 276]

RSVP 61.24 60.49 61.78 ERN 57.85 57.44 58.45

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

MI1 83.42 83.36 78.21 MI2 76.31 76.31 76.08

[Figure 284]

[Figure 285]

MTS

[Figure 286]

[Figure 287]

RSVP 68.38 68.41 68.22 ERN 66.17 66.02 65.49 Avg 69.14 68.97 68.37

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

TABLE VIII AVERAGE BCAS (%) WHEN DS,T IN (21) OR DS,T′ IN (22) WAS USED IN (30).

[Figure 294]

[Figure 295]

DS,T DS,T′

[Figure 296]

[Figure 297]

[Figure 298]

MI1 65.33 70.99 MI2 66.78 68.73

[Figure 299]

[Figure 300]

STS

[Figure 301]

[Figure 302]

RSVP 61.11 61.24 ERN 58.62 57.85

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

MI1 73.86 83.42 MI2 74.23 76.31

[Figure 307]

[Figure 308]

MTS

[Figure 309]

[Figure 310]

RSVP 69.33 68.38 ERN 65.59 66.17 Avg 66.86 69.14

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

was selected as the target domain, and the second subject as the source domain. For MTS transfer, the ﬁrst subject as the target domain, and all other subjects as the source domains. we repeated the experiment 20 times, and show the average computing time in Table VII. In summary, EA was the most efﬁcient. RA-MDM, CA-JDA and MEKT-R had similar computational cost. MEKT-L and MEKT-E had comparable classiﬁcation performance with MEKT-R (Tables III and IV), but much less computational cost. MEKT-L achieved the best compromise between the classiﬁcation accuracy and the computational cost.

TABLE VII COMPUTING TIME (SECONDS) OF DIFFERENT APPROACHES IN STS AND MTS TRANSFERS.

[Figure 316]

[Figure 317]

RA-MDM EA CA-JDA MEKT-E MEKT-L MEKT-R

[Figure 318]

[Figure 319]

[Figure 320]

MI1 5.49 0.44 5.45 2.53 2.75 5.42 MI2 0.48 0.27 0.54 0.43 0.47 0.60

[Figure 321]

[Figure 322]

[Figure 323]

STS

[Figure 324]

[Figure 325]

[Figure 326]

RSVP 0.42 0.05 0.45 0.23 0.27 0.43 ERN 0.54 0.47 0.53 0.38 0.42 0.53

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

[Figure 333]

MI1 13.61 0.94 9.24 11.06 11.48 12.96 MI2 1.01 0.69 1.35 1.13 1.20 1.29

[Figure 334]

[Figure 335]

[Figure 336]

MTS

[Figure 337]

[Figure 338]

[Figure 339]

RSVP 3.13 1.08 8.64 5.61 5.98 6.74 ERN 5.49 7.95 14.92 10.39 10.74 11.95

[Figure 340]

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

- H. Effectiveness of the Joint Probability MMD

To validate the superiority of the joint probability MMD over the traditional MMD, we replaced the joint probability MMD term DS,T′ in (30) by the traditional MMD term DS,T in (21), and repeated the experiments. The results are shown in Table VIII. The joint probability MMD outperformed the traditional MMD in six out of the eight tasks. We expect that the joint probability MMD should also be advantageous in other applications that the traditional MMD is now used.

- I. Effectiveness of DTE

This subsection validates our DTE strategy on MTS tasks to select the most beneﬁcial source subjects.

Table IX shows the BCAs when different source domain selection approaches were used: RAND randomly selected round[(z −1)/2] source subjects [because there was randomness, we repeated the experiment 20 times, and report the

mean and standard deviation (in the parentheses)], ROD was the approach proposed in [13], and ALL used all z source subjects. Table X shows the computational cost of different algorithms.

Tables IX and X shows that the proposed DTE outperformed RAND and ROD in terms of the classiﬁcation accuracy. Although its BCAs were generally slightly worse than those of ALL, its computational cost was much lower than ALL, especially when z became large, i.e., when z ≫ 1, it can save over 50% computational cost.

TABLE IX AVERAGE BCAS (%) WITH DIFFERENT SOURCE DOMAIN SELECTION APPROACHES. RAND, ROD AND DTE EACH SELECTED round[(z − 1)/2] SOURCE SUBJECTS. ALL USED ALL SOURCE SUBJECTS.

[Figure 345]

[Figure 346]

z RAND ROD DTE ALL

[Figure 347]

[Figure 348]

[Figure 349]

MI1 7 81.53 (1.19) 81.86 82.14 83.42 MI2 9 75.05 (1.06) 74.38 76.23 76.31

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

[Figure 354]

[Figure 355]

RSVP 11 67.48 (0.31) 67.79 68.70 68.38 ERN 16 65.31 (0.52) 65.36 65.51 66.17

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

[Figure 360]

TABLE X COMPUTING TIME (SECONDS) OF DIFFERENT SOURCE DOMAIN SELECTION APPROACHES. RAND, ROD AND DTE EACH SELECTED round[(z − 1)/2] SOURCE SUBJECTS. ALL USED ALL SOURCE SUBJECTS.

[Figure 361]

[Figure 362]

z RAND ROD DTE ALL

[Figure 363]

[Figure 364]

[Figure 365]

MI1 7 11.55 12.46 11.77 12.84 MI2 9 0.90 1.11 0.94 1.24

[Figure 366]

[Figure 367]

[Figure 368]

[Figure 369]

[Figure 370]

[Figure 371]

RSVP 11 3.08 3.22 3.10 6.80 ERN 16 6.27 6.42 6.29 11.57

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

V. CONCLUSIONS

Transfer learning is popular in EEG-based BCIs to cope with variations among different subjects and/or tasks. This paper has considered ofﬂine unsupervised cross-subject EEG classiﬁcation, i.e., we have labeled EEG trials from one or more source subjects, but only unlabeled EEG trials from the target subject. We proposed a novel MEKT approach, which has three steps: 1) align the covariance matrices of the EEG trials in the Riemannian manifold; 2) extract tangent space features; and, 3) perform domain adaptation by minimizing the joint probability distribution shift between the source

and the target domains, while preserving their geometric structures. An optional fourth step, DTE, was also proposed to identify the most beneﬁcial source domains, and hence to reduce the computational cost. Experiments on four EEG datasets from two different BCI paradigms demonstrated that MEKT outperformed several state-of-the-art transfer learning approaches. Moreover, DTE can reduce more than half of the computational cost when the number of source subjects is large, with little sacriﬁce of classiﬁcation accuracy.

REFERENCES

- [1] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain-computer interfaces for communication and control,” Clinical Neurophysiology, vol. 113, no. 6, pp. 767–791, Jun. 2002.
- [2] R. P. Rao, Brain-computer interfacing: an introduction. Cambridge, England: Cambridge University Press, 2013.
- [3] B. He, B. Baxter, B. J. Edelman, C. C. Cline, and W. W. Ye, “Noninvasive brain-computer interfaces based on sensorimotor rhythms,” Proc. of the IEEE, vol. 103, no. 6, pp. 907–925, May 2015.
- [4] D. Wu, “Online and ofﬂine domain adaptation for reducing BCI calibration effort,” IEEE Trans. on Human-Machine Systems, vol. 47, no. 4, pp. 550–563, Sep. 2017.
- [5] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotomamonjy, and F. Yger, “A review of classiﬁcation algorithms for EEGbased brain–computer interfaces: a 10 year update,” Journal of Neural Engineering, vol. 15, no. 3, p. 031005, Apr. 2018.
- [6] Z. J. Koles, M. S. Lazar, and S. Z. Zhou, “Spatial patterns underlying population differences in the background EEG,” Brain Topography, vol. 2, no. 4, pp. 275–284, Jun. 1990.
- [7] V. Arsigny, P. Fillard, X. Pennec, and N. Ayache, “Fast and simple calculus on tensors in the log-Euclidean framework,” in Proc. Int’l Conf. on Medical Image Computing and Computer-Assisted Intervention, Palm Springs, CA, Oct. 2005, pp. 115–122.
- [8] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Multiclass braincomputer interface classiﬁcation by Riemannian geometry,” IEEE Trans. on Biomedical Engineering, vol. 59, no. 4, pp. 920–928, Apr. 2012.
- [9] F. Yger, M. Berar, and F. Lotte, “Riemannian approaches in braincomputer interfaces: a review,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 25, no. 10, pp. 1753–1762, Nov. 2017.
- [10] L. Korczowski, M. Congedo, and C. Jutten, “Single-trial classiﬁcation of multi-user P300-based Brain-Computer Interface using riemannian geometry,” in Proc. 37th Annu. Int’l Conf. IEEE Eng. Med. Biol. Soc., Milan, Italy, Aug. 2015, pp. 1769–1772.
- [11] S. J. Pan, I. W. Tsang, J. T. Kwok, and Q. Yang, “Domain adaptation via transfer component analysis,” IEEE Trans. on Neural Networks, vol. 22, no. 2, pp. 199–210, Feb. 2011.
- [12] B. Sun, J. Feng, and K. Saenko, “Return of frustratingly easy domain adaptation,” in Proc. 30th AAAI Conf. on Artiﬁcial Intell., Arizona, Feb. 2016.
- [13] B. Gong, Y. Shi, F. Sha, and K. Grauman, “Geodesic ﬂow kernel for unsupervised domain adaptation,” in Proc. IEEE Conf. on Computer Vision and Pattern Recognition, Providence, RI, Jun. 2012, pp. 2066– 2073.
- [14] M. Long, J. Wang, G. Ding, J. Sun, and P. S. Yu, “Transfer feature learning with joint distribution adaptation,” in Proc. IEEE Int’l Conf. on Computer Vision, Sydney, Australia, Dec. 2013, pp. 2200–2207.
- [15] J. Zhang, W. Li, and P. Ogunbona, “Joint geometrical and statistical alignment for visual domain adaptation,” in Proc. IEEE Conf. on Computer Vision and Pattern Recognition, Hawaii, Jul. 2017, pp. 1859– 1867.
- [16] D. Wu, B. J. Lance, and T. D. Parsons, “Collaborative ﬁltering for braincomputer interaction using transfer learning and active class selection,” PLOS One, vol. 8, no. 2, p. e56624, Feb. 2013.
- [17] D. Wu, V. J. Lawhern, W. D. Hairston, and B. J. Lance, “Switching EEG headsets made easy: Reducing ofﬂine calibration effort using active wighted adaptation regularization,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 24, no. 11, pp. 1125–1137, Mar. 2016.
- [18] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, and M. GrosseWentrup, “Transfer learning in brain-computer interfaces,” IEEE Comput. Intell. Mag., vol. 11, no. 1, pp. 20–31, Jan. 2016.
- [19] H. Kang, Y. Nam, and S. Choi, “Composite common spatial pattern for subject-to-subject transfer,” IEEE Signal Processing Letters, vol. 16, no. 8, pp. 683–686, Aug. 2009.

- [20] F. Lotte and C. Guan, “Learning from other subjects helps reducing brain-computer interface calibration time,” in Proc. IEEE Int’l Conf. on Acoustics Speech and Signal Processing, Dallas, TX, Mar. 2010, pp. 614–617.
- [21] Y. Jin, M. Mousavi, and V. R. de Sa, “Adaptive CSP with subspace alignment for subject-to-subject transfer in motor imagery brain-computer interfaces,” in Proc. 6th Int’l Conf. on Brain-Computer Interface (BCI), GangWon, South Korea, Jan. 2018, pp. 1–4.
- [22] P. Zanini, M. Congedo, C. Jutten, S. Said, and Y. Berthoumieu, “Transfer learning: a Riemannian geometry framework with applications to braincomputer interfaces,” IEEE Trans. on Biomedical Engineering, vol. 65, no. 5, pp. 1107–1116, Aug. 2018.
- [23] H. He and D. Wu, “Transfer learning for brain-computer interfaces: A Euclidean space data alignment approach,” IEEE Trans. on Biomedical Engineering, vol. 67, no. 2, pp. 399–410, 2020.
- [24] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Classiﬁcation of covariance matrices using a riemannian-based kernel for BCI applications,” Neurocomputing, vol. 112, pp. 172–178, Jul. 2013.
- [25] H. Ramoser, J. Muller-Gerking, and G. Pfurtscheller, “Optimal spatial ﬁltering of single trial EEG during imagined hand movement,” IEEE Trans. on Rehabilitation Engineering, vol. 8, no. 4, pp. 441–446, Dec. 2000.
- [26] R. Bhatia, Positive Deﬁnite Matrices. New Jersey: Princeton University Press, 2009.
- [27] A. Gretton, K. M. Borgwardt, M. J. Rasch, B. Scho¨lkopf, and A. Smola, “A kernel two-sample test,” Journal of Machine Learning Research, vol. 13, no. 3, pp. 723–773, Mar. 2012.
- [28] M. Belkin and P. Niyogi, “Semi-supervised learning on Riemannian manifolds,” Machine Learning, vol. 56, no. 1-3, pp. 209–239, Jul. 2004.
- [29] D. Cai, X. He, and J. Han, “Document clustering using locality preserving indexing,” IEEE Trans. on Knowledge and Data Engineering, vol. 17, no. 12, pp. 1624–1637, Oct. 2005.
- [30] M. Belkin and P. Niyogi, “Laplacian eigenmaps for dimensionality reduction and data representation,” Neural Computation, vol. 15, no. 6, pp. 1373–1396, Jun. 2003.
- [31] M. Belkin, P. Niyogi, and V. Sindhwani, “Manifold regularization: A geometric framework for learning from labeled and unlabeled examples,” Journal of Machine Learning Research, vol. 7, no. Nov., pp. 2399–2434, 2006.
- [32] D. Wu, V. J. Lawhern, S. Gordon, B. J. Lance, and C.-T. Lin, “Driver drowsiness estimation from EEG signals using online weighted adaptation regularization for regression (OwARR),” IEEE Trans. on Fuzzy Systems, vol. 25, no. 6, pp. 1522–1535, Nov. 2017.
- [33] C.-S. Wei, Y.-P. Lin, Y.-T. Wang, T.-P. Jung, N. Bigdely-Shamlo, and C.T. Lin, “Selective transfer learning for EEG-based drowsiness detection,” in Proc. IEEE Int’l Conf. on Systems, Man and Cybernetics, Hong Kong, Oct. 2015, pp. 3229–3232.
- [34] P. Margaux, M. Emmanuel, D. Sbastien, B. Olivier, and M. Jrmie, “Objective and subjective evaluation of online error correction during P300-based spelling,” Advances in Human-Computer Interaction, vol. 2012, p. 4, Dec. 2012.
- [35] A. Delorme and S. Makeig, “EEGLAB: An open source toolbox for analysis of single-trial EEG dynamics including independent component analysis,” Journal of Neuroscience Methods, vol. 134, no. 1, pp. 9–21, Mar. 2004.
- [36] X. Zhang and D. Wu, “On the vulnerability of CNN classiﬁers in EEG-based BCIs,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 27, no. 5, pp. 814–825, Apr. 2019.
- [37] Q. Ai, Q. Liu, W. Meng, and S. Q. Xie, Advanced Rehabilitative Technology. Academic Press, 2018.
- [38] B. Rivet, A. Souloumiac, V. Attina, and G. Gibert, “xDAWN algorithm to enhance evoked potentials: application to brain-computer interface,” IEEE Trans. on Biomedical Engineering, vol. 56, no. 8, pp. 2035–2043, Aug. 2009.
- [39] C. M. Bishop, Pattern Recognition and Machine Learning. New York, NY: Springer, 2006.
- [40] C.-C. Chang and C.-J. Lin, “LIBSVM: A library for support vector machines,” ACM Trans. on Intell. Systems and Technol., vol. 2, no. 3, p. 27, Apr. 2011.
- [41] R. Peck and J. Van Ness, “The use of shrinkage estimators in linear discriminant analysis,” IEEE Trans. on Pattern Analysis and Machine Intell., vol. 4, no. 5, pp. 530–537, May 1982.
- [42] L. v. d. Maaten and G. Hinton, “Visualizing data using t-SNE,” Journal of Machine Learning Research, vol. 9, no. Nov., pp. 2579–2605, 2008.
- [43] H. W. Lilliefors, “On the Kolmogorov-Smirnov test for normality with mean and variance unknown,” Journal of the American statistical Association, vol. 62, no. 318, pp. 399–402, Jun. 1967.

[44] Y. Benjamini and Y. Hochberg, “Controlling the false discovery rate: a practical and powerful approach to multiple testing,” Journal of the Royal statistical society: series B (Methodological), vol. 57, no. 1, pp. 289–300, Jan. 1995.

