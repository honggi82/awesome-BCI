# arXiv:2206.01323v2[cs.LG]12Oct2022

## SPD domain-speciﬁc batch normalization to crack interpretable unsupervised domain adaptation in EEG

Reinmar J. Kobler1,2, Jun-ichiro Hirayama1, Qibin Zhao1, Motoaki Kawanabe1,2 1RIKEN Center for Advanced Intelligence Project (RIKEN AIP), Tokyo, Japan 2Advanced Telecommunications Research Institute International (ATR), Kyoto, Japan kobler.reinmar@gmail.com, qibin.zhao@riken.jp jun-ichiro.hirayama@a.riken.jp, kawanabe@atr.jp

### Abstract

Electroencephalography (EEG) provides access to neuronal dynamics noninvasively with millisecond resolution, rendering it a viable method in neuroscience and healthcare. However, its utility is limited as current EEG technology does not generalize well across domains (i.e., sessions and subjects) without expensive supervised re-calibration. Contemporary methods cast this transfer learning (TL) problem as a multi-source/-target unsupervised domain adaptation (UDA) problem and address it with deep learning or shallow, Riemannian geometry aware alignment methods. Both directions have, so far, failed to consistently close the performance gap to state-of-the-art domain-speciﬁc methods based on tangent space mapping (TSM) on the symmetric, positive deﬁnite (SPD) manifold. Here, we propose a machine learning framework that enables, for the ﬁrst time, learning domain-invariant TSM models in an end-to-end fashion. To achieve this, we propose a new building block for geometric deep learning, which we denote SPD domain-speciﬁc momentum batch normalization (SPDDSMBN). A SPDDSMBN layer can transform domain-speciﬁc SPD inputs into domain-invariant SPD outputs, and can be readily applied to multi-source/-target and online UDA scenarios. In extensive experiments with 6 diverse EEG brain-computer interface (BCI) datasets, we obtain state-of-the-art performance in inter-session and -subject TL with a simple, intrinsically interpretable network architecture, which we denote TSMNet. Code: https://github.com/rkobler/TSMNet

### 1 Introduction

Electroencephalography (EEG) measures multi-channel electric brain activity from the human scalp with millisecond precision [1]. Transient modulations in the rhythmic brain activity can reveal cognitive processes [2], affective states [3] and a person’s health status [4]. Unfortunately, these modulations exhibit low signal-to-noise ratio (SNR), domain shifts (i.e., changes in the data distribution) and have low speciﬁcity, rendering statistical learning a challenging task - particularly in the context of brain-computer interfaces (BCI) [5] where the goal is to predict a target from a short segment of multi-channel EEG data in real-time.

Under domain shifts, domain adaptation (DA), deﬁned as learning a model from a source domain that performs well on a related target domain, offers principled statistical learning approaches with theoretical guarantees [6, 7]. DA in the BCI ﬁeld mainly distinguishes inter-session and -subject transfer learning (TL) [8]. In inter-session TL, domain shifts, are expected across sessions mainly due to mental drifts (low speciﬁcity) as well as differences in the relative positioning of the electrodes and their impedances. Inter-subject TL is more difﬁcult, as domain shifts are additionally driven by structural and functional differences in brain networks as well as variations in the performed task [9].

36th Conference on Neural Information Processing Systems (NeurIPS 2022).

[Figure 1]

- Figure 1: Visualization of the proposed framework around (a) SPD domain-speciﬁc momentum batch normalization (SPDDSMBN) that (b) learns parameters Θ = {θ,φ,ψ} of typical tangent space mapping (TSM) models end-to-end to crack multi-source/-target unsupervised domain adaptation

on SD+ for EEG data (c, illustrative example). For EEG data, we propose a simple, intrinsically interpretable parametrization of f and g, denoted TSMNet, and obtain SoA performance.

These domain shifts are traditionally circumvented by recording labeled calibration data and ﬁtting domain-speciﬁc models [10, 11]. As recording calibration data is costly, models that are robust to scarce data with low SNR perform well in practice. Currently, tangent space mapping (TSM) models [12, 13] operating with symmetric, positive deﬁnite (SPD) covariance descriptors of preprocessed data are considered state-of-the-art (SoA) [10, 14, 15]. They are well suited for EEG data as they exhibit invariances to linear mixing of latent sources [16], and are consistent [13] and intrinsically interpretable [17] estimators for generative models that encode label information with a log-linear relationship in source power modulations.

Competitive, supervised calibration-free methods are one of the long-lasting grand challenges in EEG neurotechnology research [5, 10, 18, 19, 15]. Among the applied transfer learning techniques, including multi-task learning [20] and domain-invariant learning [21–23], unsupervised domain adaptation (UDA) [24] is considered as key to overcome this challenge [10, 19]. Contemporary methods cast the problem as a multi source and target UDA problem and address it with deep learning [25–28] or shallow, Riemannian geometry aware alignment methods [29–32]. Successful methods must cope with notoriously small and heterogeneous datasets (i.e., dozens of domains with a few dozens observations per domain and class). In a recent, relatively large scale inter-subject and -dataset TL competition with few labeled examples per target domain [19], deep learning approaches that aligned the ﬁrst and second order statistics either in input [33, 27] or latent space [34] obtained the highest scores. Whereas, in a pure UDA competition [15] with a smaller dataset, Riemannian geometry aware approaches dominated. With the increasing popularity of geometric deep learning [35], Ju and Guan [36] proposed an architecture based on SPD neural networks [37] to align SPD features in latent space and attained SoA scores. Despite the tremendous advances in recent years, the ﬁeld still lacks methods that can consistently close the performance gap to state-of-the-art domain-speciﬁc methods.

To close this gap, we propose a machine learning framework around domain-speciﬁc batch normalization on the SPD manifold (Figure1). The proposed framework is used to implement domain-speciﬁc TSM (Figure1a), which requires tracking the domains’ Fréchet means in latent space as they are changing during training a typical TSM model in an end-to-end fashion (Figure1b). After reviewing some preliminaries in section 2, we extend momentum batch normalization (MBN) [32] to SPDMBN that controls the Fréchet mean and variance of SPD data in section 3. In a theoretical analysis, we show under reasonable assumptions that SPDMBN can track and converge to the data’s true Fréchet mean, enabling, for the ﬁrst time, end-to-end learning of feature extractors, TSM and tangent space classiﬁers. Building upon this insight, we combine SPDMBN with domain-speciﬁc batch normalization (DSBN) [38] to form SPDDSMBN (Figure1a). A SPDDSMBN layer can transform domain-speciﬁc SPD inputs into domain-invariant SPD outputs (Figure1c). Like DSBN, SPDDSMBN easily extends to multi-source, multi-target and online UDA scenarios. In section 4, we brieﬂy review the generative model of EEG, before the proposed methods are combined in a simple, intrinsically interpretable network architecture, denoted TSMNet (Figure1b). We obtain state-of-theart performance in inter-session and -subject UDA on small and large scale EEG BCI datasets, and show in an ablation study that the performance increase is primarily driven by performing DSBN on the SPD manifold.

### 2 Preliminaries

Multi-source multi-target unsupervised domain adaptation Let X denote the space of input features, Y a label space, and Id ⊂ N an index set that contains unique domain identiﬁers. In the multi-source, multi-target unsupervised domain adaptation scenario considered here, we are given a set T source = {Ti|i ∈ Idsource ⊂ Id} with |Idsource| = N domains. Each domain Ti = {(Xij,yij)}Mj=1 ∼ PXYi contains M observations of feature (X ∈ X) and label (y ∈ Y) tuples sampled from a joint distribution PXYi .1 While the joint distributions can be different (but related) across domains, we assume that the class priors are the same (i.e., PYi = PY ). The goal is to learn a predictive function h : X × Id → Y that, once ﬁtted to T source, can generalize to unseen target domains T target = {Tl|l ∈ Idtarget ⊂ Id,Idtarget ∩ Idsource = ∅} merely based on unsupervised adaptation of h to each target domain Tl once its label l and features {Xlj}Mj=1 ∼ PXl are revealed.

Riemannian geometry on SD+ We start with recalling notions of geometry on the space of real D × D symmetric positive deﬁnite (SPD) matrices SD+ = {Z ∈ RD×D : ZT = Z,Z 0}. The space SD+ forms a cone shaped Riemannian manifold in RD×D [39]. A Riemannian manifold M is a smooth manifold equipped with an inner product on the tangent space TZM at each point Z ∈ M. Tangent spaces have Euclidean structure with easy to compute distances TZM×TZM → R+ which locally approximate Riemannian distances on M induced by an inner product [40]. Logarithmic LogZ : M → TZM and exponential ExpZ : TZM → M mappings project points to and from tangent spaces.

Using the inner product S1,S2 Z = Tr(Z−1S1Z−1S2) for points S1,S2 in the tangent space TZSD+ (i.e., the space of real symmetric D × D matrices) results in a globally deﬁned afﬁne invariant

Riemannian metric on SD+ [41, 39], which can be computed in closed form:

- 1

- 2

- 1

- 2

δ(Z1,Z2) = ||log(Z−

1 Z2Z−

##### 1 )||F (1)

where Z1 and Z2 are two SPD matrices, log(·) denotes the matrix logarithm2, || · ||F the Frobenius norm, and Tr(·) in the inner product the trace operator. Due to afﬁne invariance, we have

δ(AZ1AT,AZ2AT) = δ(Z1,Z2) for any invertible D × D transformation matrix A. The exponential and logarithmic mapping are also globally deﬁned in closed form as

- 1

- 2 log(Z−

- 1

- 2Z1Z−

- 1

- 2 )Z

LogZ(Z1) = Z

- 1

- 2 (2)

- 1

- 2 exp(Z−

- 1

- 2 S1Z−

- 1

- 2 )Z

ExpZ(S1) = Z

- 1

- 2 (3)

For a set of SPD points Z = {Zj ∈ SD+}j≤M, we will use the notion of Fréchet mean GZ ∈ SD+ and Fréchet variance νZ2 ∈ R+. The Fréchet mean is deﬁned as the minimizer of the average squared distances

M

1 M

δ2(G,Zj) (4)

GZ = arg min

G∈SD+

j=1

For M = 2, there is a closed form solution expressed as

- 1

- 2

- 1

- 2

- 1

- 2

1 Z−

1 Z2Z−

GZ(γ) = Z1#γZ2 = Z

1

γ

- 1

- 2

1 (5)

Z

with weight γ = 0.5. Choosing γ ∈ [0,1] computes weighted means along the geodesic (i.e., the shortest curve) that connects both points. For M > 2, (4) can be solved using the Karcher ﬂow algorithm [42], which iterates between projecting the data to the tangent space (2) at the current estimate, arithmetic averaging, and projecting the result back (3) to obtain a new estimate. The Fréchet variance νZ2 is deﬁned as the attained value at the minimizer GZ:

M

1 M

νZ2 = VarZ(GZ) =

δ2(GZ,Zj) (6)

j=1

- 1For ease of notation, although not required by our method, we assume that M is the same for each domain.
- 2For SPD matrices, powers, logarithms and exponentials can be computed via eigen decomposition.

- Table 1: Overview and differences of relevant batch normalization algorithms. The last column, denoted normalization, sumarizes which statistics are used to normalize the batch data during training.

Acronym SD+ domain-speciﬁc momentum γ normalization MBN [32] no no adaptive running stats SPDBN [46] yes no ﬁxed running stats SPDMBN (algorithm 1) proposed yes no adaptive running stats DSBN [38] no yes ﬁxed batch stats SPDDSMBN (18) proposed yes yes adaptive running stats

To shift a set of tangent space points to vary around a parametrized mean Gφ, parallel transport on SD+ can be used [43]:

- 1

- 2 (7)

Z→Gφ(S) = ETSE , E = (G−Z1Gφ)

ΓG

While, parallel transport is generally deﬁned for tangent space vectors S [40], on SD+ the same operations also apply directly to points on the manifold (i.e., Z ∈ Z) [31, 44].

### 3 Domain-speciﬁc batch normalization on SD+

In this section, we review relevant batch normalization (BN) [45] variants with a focus on SD+. We then present SPDMBN and show in a theoretical analysis that the running estimate converges to the

true Fréchet mean under reasonable assumptions. At last, we combine the idea of domain-speciﬁc batch normalization (DSBN) [38] with SPDMBN to form a SPDDSMBN layer. Table1 provides a brief overview of related and proposed methods.

Batch normalization Batch normalization (BN) [45] is a widely used training technqiue in deep learning as BN layers speed up convergence and improve generalization via smoothing of the engery landscape [47, 32]. A standard BN layer applies slightly different transformations during training and testing to independent and identically distributed (iid) observations xj ∈ Rd within the k-th minibatch Bk of size M drawn from a dataset T . During training, the data are normalized using the batch mean bk and variance s2k, and then scaled and shifted to have a parametrized mean gφ and variance σ2φ. Internally, the layer updates running estimates of the dataset’s statistics (gk,σ2k) during each training step k; the updates are computed via exponential smoothing with momentum parameter γ. During testing, the running estimates are used.

Using batch statistics to normalize data during training rather than running estimates introduces noise whose level depends on the batch size [32]; smaller batch sizes raise the noise level. The introduced noise regularizes the training process, which can help to escape poor local minima in initial learning but also lead to underﬁtting. Momentum BN (MBN) [32] allows small batch sizes while avoiding underﬁtting. Like batch renormalization [48], MBN uses running estimates during training and testing. The key difference is that MBN keeps two sets of running statistics; one for training and one for testing. The latter are updated conventionally, while the former are updated with momentum parameter γtrain(k) that decays over training steps k. MBN can, therefore, quickly escape poor local minima during initial learning and avoid underﬁtting at later stages [32].

Batch normalization on SD+ It is intractable to compute the Fréchet mean GB

for each minibatch

k

Bk = {Zj ∈ SD+}Mj=1, as there is no efﬁcient algorithm to solve (4). Brooks et al. [44] proposed Riemannian Batch Normalization (RBN) as a tractable approximation. RBN approximateley solves

(4) by aborting the iterative Karcher ﬂow algorithm after one iteration. To transform Zj ∈ Bk with estimated mean Bk to vary around Gφ, parallel transport (7) is used. The RBN input output transformation is then expressed as

- 1

- 2 , ∀Zj ∈ Bk (8)

k→Gφ(Zj) = ETZjE , E = (B−k 1Gφ)

RBN(Zj;Gφ,γ) = ΓB

Using (5), the running estimate of the dataset’s Fréchet mean can be updated in closed form

Gk = Gk−1#γBk (9)

In [46] we proposed an extension to RBN, denoted SPD batch renormalization (SPDBN) that controls both Fréchet mean and variance. Like batch renormalization [48], SPDBN uses running estimates Gk and νk2 during training and testing. To transform Zj ∈ Bk to vary around Gφ with variance νφ2, each

Algorithm 1: SPD momentum batch normalization (SPDMBN) Input :batch Bk = {Zj ∈ SD+}Mj=1 at training step k,

running mean G¯ k−1, G¯ 0 = I and variance ν¯k2−1, ν¯02 = 1 for training, running mean G˜ k−1, G˜ 0 = I and variance ν˜k2−1, ν˜02 = 1 for testing, learnable parameters (Gφ, νφ), and momentum for training and testing γtrain(k), γ ∈ [0, 1]

Output:normalized batch {Z˜j = SPDMBN(Zj) ∈ SD+ | Zj ∈ Bk} if training then

Bk = karcher_flow (Bk, steps = 1); // approx. solve problem (4) G¯ k = G¯ k−1#γtrain(k)Bk; // update running stats for training ν¯k2 = (1 − γtrain(k))¯νk2−1 + γtrain(k)VarBk(G¯ k)

G˜ k = G˜ k−1#γBk; // update running stats for testing ν˜k2 = (1 − γ)˜νk2−1 + γVarBk(G˜ k)

end (Gk, νk2) = (G¯ k, ν¯k) if training else (G˜ k, ν˜k2) Z˜j = ΓI→Gφ ◦ ΓGk→I(Zj)

νφ

νk+ε ; // use (10) to whiten, rescale and rebias

observation is ﬁrst transported to vary around the identity matrix I, rescaled via computing matrix powers and ﬁnally transported to vary around Gφ. The sequence of operations can be expressed as

νφ νk+ε

SPDBN(Zj;Gφ,νφ2,ε,γ) = ΓI→G

, ∀Zj ∈ Bk (10) The standard backpropagation framework with extensions for structured matrices [49] and manifoldconstrained gradients [40] can be used to propagate gradients through RBN and SPDBN layers and learn the parameters (Gφ,νφ).

φ ◦ ΓG

k→I(Zj)

Momentum batch normalization on SD+ SPDBN [46] suffers from the same limitations as batch renormalization [48]. Consequently, we propose to extend MBN [32] to SD+. We list the pseudocode of our proposed extension, which we denote SPDMBN, in algorithm 1. SPDMBN uses approximations of batch-speciﬁc Fréchet means to update two sets of running estimates of the dataset’s Fréchet mean. As MBN [32], we decay γtrain(k) with a clamped exponential decay schedule

1 K−1 max(K−k,0) min + γmin (11)

γtrain(k) = 1 − γ

where K deﬁnes the training step at which γmin ∈ [0,1] should be attained.

The running mean in SPDMBN converges to the Fréchet mean Here, we consider models that apply a SPDMBN layer to latent representations generated by a feature extractor fθ : X → SD+ with learnable parameters θ.

We deﬁne a dataset that contains the latent representations generated with feature set θk as Zθk

= {fθ

(x)|x ∈ T }, and a minibatch of M iid samples at training step k as Bk. We denote the Fréchet mean of Zθk

k

, the estimated Fréchet mean, deﬁned in (9), as Gk, and the estimated batch mean as Bk. Since the batches are drawn randomly, we consider the batch and running means as random variables.

#### as Gθ

k

We assume that the variance Varθ

)} of the previous batch mean Bk−1 with respect to the current Fréchet mean Gθ

(Bk−1) = EB

k−1{δ2(Bk−1,Gθ

k

k

is bounded by the current variance Varθ

(Bk) and the norm of the difference in the parameters

k

k

(Bk) (12) That is, across training steps k the parameter updates are required to change the ﬁrst and second order moments of the distribution of Zθk

(Bk−1) ≤ (1 + ||θk − θk−1||)Varθ

Varθ

k

k

gradually so that the expected distance between Gθ

and the

k

previous batch mean Bk−1 is bounded. We conjecture that this is the case for feature extractors fθ that are smooth in the parameters and small learning rates, but leave the proof for future work.

Proposition 1 (Error bound for Gk). Consider the setting deﬁned above, and assumption (12) holds true. Then, the variance of the running mean Varθ

(Gk) is bounded by Varθ

k

(Bk) (13) over training steps k if

(Gk) ≤ Varθ

k

k

1 − γ2 (1 − γ)2 − 1 (14)

||θk − θk−1|| ≤

holds true.

The proof is provided in appendix A.1 of the supplementary material and relies on the proof of the geometric law of large numbers [50].

Proposition 1 states that if (12) and (14) are met, the expected distance between the true Fréchet mean and the running mean is less or equal to the one of the batch mean. Consequently, the introduced noise level of SPDBN (equation 10) and SPDMBN (algorithm 1), which use Gk to normalize batches during training, is smaller or equal to RBN (equation 8), which uses Bk.

Since γ controls the adaptation speed of Gk, proposition 1 also states that if γ converges to zero (=no adaptation), the parameter updates are required to converge to zero as well (=no learning). Hence, for a ﬁxed γ ∈ (0,1), as in the case of SPDBN (equation 10), proposition 1 is fulﬁlled, if the learning rate for the parameters θ is chosen sufﬁciently small. This can substantially slow down initial learning for standard choices of γ (e.g., 0.1 or 0.01). As a remedy, SPDMBN (algorithm 1) uses an adaptive momentum parameter, which allows larger parameter updates during initial training steps.

If we consider a late stage of learning, and in particular assume that after a certain number of iterations κ the parameters stay in a small ball with radius ρ around θ∗ (i.e., ||θk − θ∗|| ≤ ρ ∀ k > κ) and the feature extractor is L-smooth in the parameters (i.e., δ(fθ(x),fθ˜(x)) ≤ L||θ − θ˜|| ∀x ∈ T , ∀θ,θ˜) then the distances are bounded δ(fθ

(x),fθ∗(x)) ≤ ρL.

k

Remark 1 (Convergence of Gk for SPDMBN). If ρL is neglibile compared to the dataset’s variance, then the Fréchet mean and variance can be considered ﬁxed, and the theorem of large numbers on

SD+ [50] applies directly. That is, if the momentum parameter is decayed exponentially ∀k > κ the running mean Gk converges to the Fréchet mean Gθ∗ in probability as k → ∞.

Taken together, Proposition 1 and Remark 1 provide guidelines to update Gk in SPDMBN so that the introduced estimation error is bounded during initial fast learning (large γ) and decays towards zero in late learning (small γ).

SPDMBN to learn tangent space mapping at Fréchet means Typical TSM models for classiﬁcation [12] and regression [13] ﬁrst use (2) to project Z ∈ T ⊂ SD+ to the tangent space at the Fréchet mean GT , then use (7) to transport the result to vary around I, and ﬁnally extract elements in the upper triangular part3 to reduce feature redundancy. The invertible mapping PG

: SD+ → RD(D+1)/2 is expressed as:

T

- 1

- 2

1 2

T ZG−

(Z) = upper(log(G−

T )) (15)

#### PG

(Z) = upper ◦ ΓG

T →I ◦ LogG

T

T

We propose to use a SPDMBN layer followed by a LogEig layer [37] to compute a similar mapping mφ (Figure1a). A LogEig layer simply computes the matrix logarithm and vectorizes the result so that the norm is preserved. If the parametrized mean of SPDMBN is ﬁxed to the identify matrix (Gφ = I), the composition computes

νφ νk+ε

mφ(Z) = LogEig ◦ SPDMBN(Z) = upper ◦ log ◦ ΓG

k→I(Z)

νφ νk + ε

- 1

- 2

- 1

- 2

log G−

k ZG−

k (16)

= upper

where (Gk,νk2) are the estimated Fréchet mean and variance of the dataset T at training step k, and φ = {νφ} the learnable parameters. According to remark 1 Gk converges to GT and, in turn, mφ to a scaled version of PG

, since upper is linear.

T

The mapping mφ offers several advantageous properties. First, the features are projected to a Euclidean vector space where standard layers can be applied and distances are cheap to compute. Second, distances between the projected features locally approximate δ and, therefore, inherit its invariance properties (e.g., afﬁne mixing) [41]. This improves upon a LogEig layer [37] which projects features to the tangent space at the identity matrix. As a result, distances between LogEig projected features correspond to distances measured with the log-Euclidean Riemannian metric (LERM) [51] which is not invariant to afﬁne mixing. Third, controlling the Fréchet variance in (16) empirically speeds up learning and improves generalization [46].

3To preserve the norm, the off diagonal elements are scaled by √2.

Domain-speciﬁc batch normalization on SD+ Considering a multi-source UDA scenario, Chang et al. [38] proposed a domain-speciﬁc BN (DSBN) layer which simply keeps multiple parallel BN

layers and distributes observations according to the associated domains. Formally, we consider minibatches Bk that form the union of NB

k ≤ |Id| domain-speciﬁc minibatches Bki drawn from distinct domains i ∈ IBk ⊆ Id. As before, each Bki contains j = 1,...,M/NB

iid observations xj. A DSBN layer mapping Rd × Id → Rd can then be expressed as

k

,ε,γ) , ∀xj ∈ Bki , ∀i ∈ IBk

(17)

DSBN(xj,i) = BNi(xj;gφ

,sφ

i

i

In practice, the batch size M is typically ﬁxed. The particular choice is inﬂuenced by resource availability and the desired noise level introduced by minibatch based stochastic gradient descent. A drawback of DSBN is that for a ﬁxed batch size M and an increasing number of source domains NB

, the effective batch size declines for the BN layers within DSBN. Since small batch sizes increase the noise level introduced by BN, increasing the number of domains per batch can lead to underﬁtting [32]. To alleviate this effect, we use the previously introduced SPDMBN layer. The proposed domain-speciﬁc BN layer on SD+ is then formally deﬁned as

k

,ε,γ,γtrain(k)) , ∀Zj ∈ Bki ⊂ SD+ , ∀i ∈ IBk

SPDDSMBN(Zj,i) = SPDMBNi(Zj;Gφ

,νφ

i

i

(18) The layer can be readily adapted to new domains, as new SPDMBN layers can be added on the ﬂy. If the entire data of a domain becomes available, the domain-speciﬁc Fréchet mean and variance can be estimated by solving (4), otherwise, the update rules in algorithm 1 can be used.

### 4 SPDDSMBN to crack interpretable multi-source/-target UDA for EEG data

With SPDDSMBN introduced in the previous section, we focus on a speciﬁc application domain, namely, multi-source/-target UDA for EEG-based BCIs and propose an intrinsically interpretable architecture which we denote TSMNet.

Generative model of EEG EEG signals x(t) ∈ RP capture voltage ﬂuctuations on P channels. An EEG record (=domain) is uniquely identiﬁed by a subject and session identiﬁer. After standard pre-processing steps, each domain i contains j = 1,...,M labeled observations with features Xij ∈ X ⊂ RP×T where T is the number of temporal samples. Due to linearity of Maxwell’s equations and Ohmic conductivity of tissue layers in the frequency ranges relevant for EEG [52], a domain-speciﬁc linear instantaneous mixture of sources model is a valid generative model:

Xij = AiSij + Nij (19)

where Sij ∈ RQ×T represents the activity of Q latent sources, Ai ∈ RP×Q a domain-speciﬁc mixing matrix and Nij ∈ RP×T additive noise. Both Ai and Sij are unknown which demands making assumptions on Ai (e.g., anatomical prior knowledge [53]) and/or Sij (e.g., statistical independence [54]) to extract interesting sources.

Interpretable multi-source/-target UDA for EEG data As label information is available for the source domains, our goal is to identify discriminative oscillatory sources shared across domains. Our approach relies on TSM models with linear classiﬁers [12], as they are consistent [13] and intrinsically interpretable [17] estimators for generative models with log-linear relationships between

the target yij and variance Var{s(ijk)(t)} of k = 1,...,K ≤ Q discriminative sources:

K

bklog Var{s(ijk)(t)} + εij (20)

yij =

k=1

where bk ∈ R summarizes the coupling between the target yij and the variance of the encoding source, and εij additive noise. In [17] we showed that the encoding sources’ coupling and their patterns4 (columns of Ai) can be recovered via solving a generalized eigenvalue problem between the Fréchet mean GT

and classiﬁer patterns [55] that were back projected to SD+ with PG−1Ti. The

i

4Here, we use the entire dataset’s Fréchet mean instead of the domain-speciﬁc ones to compute patterns for the average domain.

resulting eigenvectors are the patterns and the eigenvalues λk reﬂect the relative source contribution ck:

ck = max(λk,λ−k 1) , λk = exp(bk/||b||22) (21) To beneﬁt from the intrinsic interpretability of TSM models, we constrain our hypothesis class H to functions h : X × Id → Y that can be decomposed into a composition of a shared linear feature extractor with covariance pooling fθ : X → SD+, domain-speciﬁc tangent space mapping mφ : SD+ × Id → RD(D+1)/2, and a shared linear classiﬁer gψ : RD(D+1)/2 → Y with parameters Θ = {θ,φ,ψ}.

TSMNet with SPDDSMBN Unlike previous approaches which learn fθ,mφ,gψ sequentially [29, 31, 13, 30], we parametrize h = gψ ◦ mφ ◦ fθ as a neural network and learn the entire model in an end-to-end fashion (Figure1b). Details of the proposed architecture, denoted TSMNet, are provided in appendix A.2.5. In a nutshell, we parametrize fθ as the composition of the ﬁrst two linear convolutional layers of ShConvNet [56], covariance pooling [57], BiMap [37], and ReEig [37] layers. A BiMap layer applies a linear subspace projection, and a ReEig layer thresholds eigenvalues of symmetric matrices so that the output is SPD. We used the default threshold (10−4) and found that it was never active in the trained models. Hence, after training, fθ fulﬁlled the hypothesis class constraints. In order for mφ to align the domain data and compute TSM, we use SPDDSMBN (18) with shared parameters (i.e., Gφ

= νφ) in (16). Finally, the classiﬁer gψ was parametrized as a linear layer with softmax activations. We use the standard-cross entropy loss as training objective, and optimized the parameters with the Riemannian ADAM optimizer [58].

= Gφ = I,νφ

i

i

### 5 Experiments with EEG data

In the following, we apply our method to classify target labels from short segments of EEG data. We consider two BCI applications, namely, mental imagery [59, 5] and mental workload estimation [60]. Both applications have high potential to aid society in rehabilitation and healthcare [61, 62, 18] but have, currently, limited practical value because of poor generalization across sessions and subjects [19, 15].

Datasets and preprocessing The considered mental imagery datasets were BNCI2014001 [63] (9 subjects/2 sessions/4 classes), BNCI2015001 [64] (12/2-3/2), Lee2019 [65] (54/2/2), Lehner2020 [66] (1/7/2), Stieger2021 [67] (62/4-8/4) and Hehnberger2021 [68] (1/26/4). For mental workload estimation, we used a recent competition dataset [69] (12/2/3). A detailed description of the datasets is provided in appendix A.2.1. Altogether, we analyzed a total of 603 sessions of 158 human subjects whose data was acquired in previous studies that obtained the subjects’ informed consent and the right to share anonymized data. The python packages moabb [14] and mne [70] were used to preprocess the datasets. The applied steps comprise resampling the EEG signals to 250/256 Hz, applying temporal ﬁlters to extract oscillatory EEG activity in the 4 to 36 Hz range (spectrally resolved if required by a method) and ﬁnally extract short segments (≤ 3s) associated to a class label (details provided in appendix A.2.2).

Evaluation We evaluated TSMNet against several baseline methods implementing direct transfer or multi-source (-target) UDA strategies. They can be broadly categorized as component based [71, 68], Riemannian geometry aware [12, 17, 30, 72] or deep learning [56, 73, 25]. All models were ﬁt and evaluated with a randomized leave 5% of the sessions (inter-session TL) or subjects (inter-subject TL) out cross-validation (CV) scheme. For inter-session TL, the models were only provided with data of the associated subject. When required, inner train/test splits (neural nets) or CV (shallow methods) were used to optimize hyper parameters (e.g., early stopping, regularization parameters). The dataset Hehenberger2021 was used to ﬁt the hyper parameters of TSMNet, and is, therefore, omitted in the presented results. Balanced accuracy (i.e., the average recall across classes) was used as scoring metric. As the discriminability of the data varies considerably across subjects, we decided to report the results in the ﬁgures relative to the score of a SoA domain-speciﬁc Riemannian geometry aware method [17], which was ﬁtted and evaluated in a 80%/20% chronological train/test split (for details see appendix A.2.4).

Soft- and hardware We either used publicly available python code or implemented the methods in python using the packages torch [74], scikit-learn [75], skorch [76], geoopt [77], mne [70], pyriemann [78], pymanopt [79]. We ran the experiments on standard computation PCs equipped with 32 core CPUs with 128 GB of RAM and used up to 1 GPU (24 GRAM). Depending on the dataset size, ﬁtting and evaluating TSMNet varied from a few seconds to minutes.

[Figure 2]

- Figure 2: Mental imagery results (5 datasets). BCI test set score (balanced accuracy) for inter-session/subject transfer learning methods relative to a SoA domain-speciﬁc reference model (80%/20% chronological train/test split; for details see appendix A.2.4). a, Barplots summarize the grand average (573 sessions, 138 subjects) results. Errorbars indicate bootstrapped (1e3 repetitions) 95% conﬁdence intervals (over subjects). b, Box and scatter plots summarize the dataset-speciﬁc results for selected methods from each category. Datasets are ordered according to the training set size. Each dot summarizes the score for one subject. Lehner2021 is not displayed as it contains only 1 subject.

#### 5.1 Mental imagery

TSMNet closes the gap to domain-speciﬁc methods Figure2 summarizes the mental imagery results. It displays test set scores of the considered TL methods relative to the score of a SoA domain-speciﬁc reference method. Combining the results of all subjects across datasets (Figure2a), it becomes apparent that TSMNet is the only method that can signiﬁcantly reduce the gap to the reference method (inter-subject) or even exceed its performance (inter-session). Figure 2b displays the results resolved across datasets (for details see appendix A.3.1). We make two important observations. First, concerning inter-session TL, TSMNet meets or exceeds the score of the reference method consistently across datasets. Second, concerning inter-subject TL, we found that all considered methods tend to reduce the performance gap as the dataset size (# subjects) increases, and that TSMNet is consistently the top or among the top methods. As a ﬁtted TSMNet corresponds to a typical TSM model with a linear classiﬁer, we can transform the ﬁtted parameters into interpretable patterns [17]. Figure3a displays extracted patterns for the BNCI2015001 dataset (inter-subject TL). It is clearly visible that TSMNet infers the target label from neurophysiologically plausible sources (rows in Figure3a). As expected [2], the source with highest contribution has spectral peaks in the alpha and beta bands, and originates in contralateral and central sensorimotor cortex.

DSBN on SD+ drives the success of TSMNet Since TSMNet combines several advances, we present the results of an ablation study in Table2. It summarizes the grand average inter-session TL

test scores relative to TSMNet with SPDDSMBN for n = 138 subjects. We observed three signiﬁcant effects. The largest effect can be attributed to SD+, as we observed the largest performance decline if the architecture would be modiﬁed5 to omit the SPD manifold (4.5% with DSBN, 3% w/o DSBN). The performance gain comes at the cost of a 2.6x longer time to ﬁt the parameters. The second largest effect can be attributed to DSBN; without DSBN the performance dropped by 3.9% (with SD+) and 2.4% (w/o SD+). The smallest, yet signiﬁcant effect can be attributed to SPDMBN.

#### 5.2 Mental workload estimation

Compared to the baseline methods, TSMNet obtained the highest average scores of 54.7% (7.3%) and 52.4% (8.8%) in inter-session and -subject TL (for details see appendix A.3.1). Interestingly, the inter-session TL score of TSMNet matches the score (54.3%) of the winning method in last year’s competition [15]. To shed light on the sources utilized by TSMNet, we show patterns for a ﬁtted model in Figure3b. For the low mental workload class, the top contributing source’s activity peaked in the theta band and originated in pre-frontal areas. The second source’s activity originated in occipital cortex with non-focal spectral proﬁle. Our results agree with the ﬁndings of previous research, as both areas and the theta band have been implicated in mind wandering and effort withdrawal [60].

5We replaced the covariance pooling, BiMap, ReEig, SPD(DS)MBN, LogEig layers with variance pooling, elementwise log activations followed by (DS)MBN. Note that the resulting architecture is similar to ShConvNet.

[Figure 3]

- Figure 3: Model interpretation results. Patterns extracted from a TSMNet. a, Motor imagery dataset (BNCI2015001, inter-subject TL). The top, left panel lists the contribution, deﬁned in (21), for each extracted source k = 1,...,20 (x-axis) to the target class. Panels in the left column summarize the spectral patterns of extracted sources. For visualization purposes, only the 2 most discriminative sources are displayed. Panels in the top row summarize the frequency proﬁle of each spectral channel

(output of 4 temporal convolution layers in fθ). Topographic plots summarize how the source activity is projected to regions covered by the EEG channels (rows correspond to the source index; columns to spectral channels). EEG channels at darker blue or red areas capture more source activity and are, therefore, more discriminative. b, As in a for the mental workload estimation dataset and class low.

- Table 2: Ablation study. Grand average (5 mental imagery datasets, 138 subjects, inter-session TL) score for the test data relative to the proposed method, and training ﬁt time (50 epochs). Standarddeviation is used to report the variability across subjects. Permutation t-tests (1e4 perms, df=137, 4 tests with t-max adjustment) were used to identify signiﬁcant effects.

∆ balanced accuracy (%) ﬁt time (s)

mean (std) t-val (p-val) mean (std) SD+ DSBN BN method

yes yes SPDMBN (algo. 1) (proposed) - - 16.9 ( 1.0) yes SPDBN [46] -1.6 ( 2.2) -7.8 (0.0001) 20.3 ( 1.6) no SPDMBN (algo. 1) -3.9 ( 4.4) -10.7 (0.0001) 11.3 ( 0.5)

no yes MBN [32] -4.5 ( 3.8) -10.1 (0.0001) 6.6 ( 0.2) no MBN [32] -6.9 ( 4.8) -13.4 (0.0001) 4.4 ( 0.1)

- 6 Discussion In this contribution, we proposed a machine learning framework around (domain-speciﬁc) momentum

batch normalization on SD+ to learn tangent space mapping (TSM) and feature extractors in an end-to-end fashion. In a theoretical analysis, we provided error bounds for the running estimate of

the Fréchet mean as well as convergence guarantees under reasonable assumptions. We then applied the framework, to a multi-source multi-target unsupervised domain adaptation problem, namely, inter-session and -subject transfer learning for EEG data and obtained or attained state-of-the art performance with a simple, intrinsically interpretable model, denoted TSMNet, in a total of 6 diverse BCI datasets (138 human subjects, 573 sessions). In the case of mental imagery, we found that TSMNet signiﬁcantly reduced (inter-subject TL) or even exceeded (inter-session TL) the performance gap to a SoA domain-speciﬁc method.

Although our framework could be readily extended to online UDA for unseen target domains, we limited this study to ofﬂine evaluations and leave actual BCI studies to future work. A limitation of our framework, and also any other method that involves eigen decomposition, is the computational complexity, which limits its application to high-dimensional SPD features (e.g., fMRI connectivity matrices with ﬁne spatial granularity). Altogether, the presented results demonstrate the utility of our framework and in particular TSMNet as it not only achieves highly competitive results but is also intrinsically interpretable. While we do not foresee any immediate negative societal impacts, we provide direct contributions towards the scalability and acceptability of EEG-based healthcare [1, 5] and consumer [18, 60] technologies. We expect future works to evaluate the impact of the proposed methods in clinical applications of EEG like sleep staging [80, 81], seizure [82] or pathology detection [83, 84].

### Acknowledgments and Disclosure of Funding

This work was supported by the JSPS KAKENHI (Grants-in-Aid for Scientiﬁc Research) grants 20H04249, 20H04208, 21H03516 and 21K12055.

### References

- [1] Donald L. Schomer and Fernando H. Lopes da Silva. Niedermeyer’s Electroencephalography: basic principles, clinical applications, and related ﬁelds. Lippincott Williams & Wilkins, 7 edition, 2018. ISBN 978-0-19-022848-4. doi: 10.1212/WNL.0b013e31822f0490.
- [2] G Pfurtscheller and F H Lopes. Event-related EEG / MEG synchronization and. Clinical Neurophysiology, 110:10576479, 1999.
- [3] Josef Faller, Jennifer Cummings, Sameer Saproo, and Paul Sajda. Regulation of arousal via online neurofeedback improves human performance in a demanding sensory-motor task. Proceedings of the National Academy of Sciences, 116(13):6482–6490, 2019. doi: 10.1073/ pnas.1817207116.
- [4] Yu Zhang, Wei Wu, Russell T. Toll, Sharon Naparstek, Adi Maron-Katz, Mallissa Watts, Joseph Gordon, Jisoo Jeong, Laura Astolﬁ, Emmanuel Shpigel, Parker Longwell, Kamron Sarhadi, Dawlat El-Said, Yuanqing Li, Crystal Cooper, Cherise Chin-Fatt, Martijn Arns, Madeleine S. Goodkind, Madhukar H. Trivedi, Charles R. Marmar, and Amit Etkin. Identiﬁcation of psychiatric disorder subtypes from functional connectivity patterns in resting-state electroencephalography. Nature Biomedical Engineering, 5(4):309–323, 2021. doi: 10.1038/s41551-020-00614-8.
- [5] Jonathan R Wolpaw, Niels Birbaumer, Dennis J McFarland, Gert Pfurtscheller, and Theresa M Vaughan. Brain-computer interfaces for communication and control. Clinical neurophysiology : ofﬁcial journal of the International Federation of Clinical Neurophysiology, 113:767–791,

2002. doi: doi:10.1016/s1388-2457(02)00057-3.

- [6] Shai Ben-David, John Blitzer, Koby Crammer, Alex Kulesza, Fernando Pereira, and Jennifer Wortman Vaughan. A theory of learning from different domains. Machine Learning, 79 (1-2):151–175, 2010. doi: 10.1007/s10994-009-5152-4.
- [7] Judy Hoffman, Mehryar Mohri, and Ningshan Zhang. Algorithms and theory for multiplesource adaptation. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018.
- [8] Dongrui Wu, Yifan Xu, and Bao-Liang Lu. Transfer Learning for EEG-Based Brain-Computer Interfaces: A Review of Progress Made Since 2016. IEEE Transactions on Cognitive and Developmental Systems, pages 1–1, 2020. doi: 10.1109/TCDS.2020.3007453.
- [9] Christa Neuper, Reinhold Scherer, Miriam Reiner, and Gert Pfurtscheller. Imagery of motor actions: Differential effects of kinesthetic and visual–motor mode of imagery in single-trial EEG. Cognitive Brain Research, 25(3):668–677, 2005. doi: 10.1016/j.cogbrainres.2005.08.014.
- [10] F Lotte, L Bougrain, A Cichocki, M Clerc, M Congedo, A Rakotomamonjy, and F Yger. A review of classiﬁcation algorithms for EEG-based brain–computer interfaces: a 10 year update. Journal of Neural Engineering, 15(3):031005, 2018. doi: 10.1088/1741-2552/aab2f2.
- [11] Karina Statthaler, Andreas Schwarz, David Steyrl, Reinmar J. Kobler, Maria Katharina Höller, Julia Brandstetter, Lea Hehenberger, Marvin Bigga, and Gernot Müller-Putz. Cybathlon experiences of the Graz BCI racing team Mirage91 in the brain-computer interface discipline. Journal of NeuroEngineering and Rehabilitation, 14(1):129, 2017. doi: 10.1186/s12984-017-0344-9.
- [12] Alexandre Barachant, Stéphane Bonnet, Marco Congedo, and Christian Jutten. Multiclass braincomputer interface classiﬁcation by Riemannian geometry. IEEE transactions on bio-medical engineering, 59(4):920–928, 2012. doi: 10.1109/TBME.2011.2172210.
- [13] David Sabbagh, Pierre Ablin, Gaël Varoquaux, Alexandre Gramfort, and Denis A Engemann. Manifold-regression to predict from MEG/EEG brain signals without source modeling. In Advances in Neural Information Processing Systems, pages 7323–7334, 2019.

- [14] Vinay Jayaram and Alexandre Barachant. MOABB: trustworthy algorithm benchmarking for BCIs. Journal of Neural Engineering, 15(6):066011, 2018. doi: 10.1088/1741-2552/aadea0.
- [15] Raphaëlle N. Roy, Marcel F. Hinss, Ludovic Darmet, Simon Ladouce, Emilie S. Jahanpour, Bertille Somon, Xiaoqi Xu, Nicolas Drougard, Frédéric Dehais, and Fabien Lotte. Retrospective on the First Passive Brain-Computer Interface Competition on Cross-Session Workload Estimation. Frontiers in Neuroergonomics, 3:838342, 2022. doi: 10.3389/fnrgo.2022.838342.
- [16] Marco Congedo, Alexandre Barachant, and Rajendra Bhatia. Riemannian geometry for EEGbased brain-computer interfaces; a primer and a review. Brain-Computer Interfaces, 4(3): 155–174, 2017. doi: 10.1080/2326263X.2017.1297192.
- [17] Reinmar J. Kobler, Jun-Ichiro Hirayama, Lea Hehenberger, Catarina Lopes-Dias, Gernot MüllerPutz, and Motoaki Kawanabe. On the interpretation of linear Riemannian tangent space model parameters in M/EEG. In Proceedings of the 43rd Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC). IEEE, 2021. doi: 10.1109/EMBC46164. 2021.9630144.
- [18] Stephen H. Fairclough and Fabien Lotte. Grand Challenges in Neurotechnology and System Neuroergonomics. Frontiers in Neuroergonomics, 1:602504, 2020. doi: 10.3389/fnrgo.2020. 602504.
- [19] Xiaoxi Wei, A. Aldo Faisal, Moritz Grosse-Wentrup, Alexandre Gramfort, Sylvain Chevallier, Vinay Jayaram, Camille Jeunet, Stylianos Bakas, Siegfried Ludwig, Konstantinos Barmpas, Mehdi Bahri, Yannis Panagakis, Nikolaos Laskaris, Dimitrios A. Adamos, Stefanos Zafeiriou, William C. Duong, Stephen M. Gordon, Vernon J. Lawhern, Maciej Sliwowski,´ Vincent Rouanne, and Piotr Tempczyk. 2021 BEETL Competition: Advancing Transfer Learning for Subject Independence & Heterogenous EEG Data Sets. arXiv:2202.12950 [cs, eess], 2022.
- [20] Vinay Jayaram, Morteza Alamgir, Yasemin Altun, Bernhard Scholkopf, and Moritz GrosseWentrup. Transfer Learning in Brain-Computer Interfaces. IEEE Computational Intelligence Magazine, 11(1):20–31, 2016. doi: 10.1109/MCI.2015.2501545.
- [21] Siamac Fazli, Florin Popescu, Márton Danóczy, Benjamin Blankertz, Klaus-Robert Müller, and Cristian Grozea. Subject-independent mental state classiﬁcation in single trials. Neural Networks, 22(9):1305–1312, 2009. doi: 10.1016/j.neunet.2009.06.003.
- [22] Wojciech Samek, Motoaki Kawanabe, and Klaus Robert Müller. Divergence-based framework for common spatial patterns algorithms. IEEE Reviews in Biomedical Engineering, 7:50–72,

2014. doi: 10.1109/RBME.2013.2290621.

- [23] O-Yeon Kwon, Min-Ho Lee, Cuntai Guan, and Seong-Whan Lee. Subject-Independent Brain–Computer Interfaces Based on Deep Convolutional Neural Networks. IEEE Transactions on Neural Networks and Learning Systems, 31(10):3839–3852, 2020. doi: 10.1109/ TNNLS.2019.2946869.
- [24] Sicheng Zhao, Bo Li, Colorado Reed, Pengfei Xu, and Kurt Keutzer. Multi-source Domain Adaptation in the Deep Learning Era: A Systematic Survey, 2020.
- [25] Ozan Ozdenizci, Ye Wang, Toshiaki Koike-Akino, and Deniz Erdogmus. Learning Invariant Representations From EEG via Adversarial Inference. IEEE Access, 8:27074–27085, 2020. doi: 10.1109/ACCESS.2020.2971600.
- [26] Lichao Xu, Zhen Ma, Jiayuan Meng, Minpeng Xu, Tzyy-Ping Jung, and Dong Ming. Improving Transfer Performance of Deep Learning with Adaptive Batch Normalization for Brain-computer Interfaces *. In 2021 43rd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), pages 5800–5803, Mexico, 2021. IEEE. ISBN 978-1-72811-179-7. doi: 10.1109/EMBC46164.2021.9629529.
- [27] Lichao Xu, Minpeng Xu, Yufeng Ke, Xingwei An, Shuang Liu, and Dong Ming. Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. Frontiers in Human Neuroscience, 14:103, 2020. doi: 10.3389/fnhum.2020.00103.

- [28] Ravikiran Mane, Efﬁe Chew, Karen Chua, Kai Keng Ang, Neethu Robinson, A. P. Vinod, Seong-Whan Lee, and Cuntai Guan. FBCNet: A Multi-view Convolutional Neural Network for Brain-Computer Interface. arXiv:2104.01233 [cs, eess], 2021.
- [29] Paolo Zanini, Marco Congedo, Christian Jutten, Salem Said, and Yannick Berthoumieu. Transfer Learning: A Riemannian Geometry Framework With Applications to Brain–Computer Interfaces. IEEE Transactions on Biomedical Engineering, 65(5):1107–1116, 2018. doi: 10.1109/TBME.2017.2742541.
- [30] Pedro Luiz Coelho Rodrigues, Christian Jutten, and Marco Congedo. Riemannian Procrustes Analysis: Transfer Learning for Brain–Computer Interfaces. IEEE Transactions on Biomedical Engineering, 66(8):2390–2401, 2019. doi: 10.1109/TBME.2018.2889705.
- [31] Or Yair, Mirela Ben-Chen, and Ronen Talmon. Parallel Transport on the Cone Manifold of SPD Matrices for Domain Adaptation. IEEE Transactions on Signal Processing, 67(7):1797–1811,

2019. doi: 10.1109/TSP.2019.2894801.

- [32] Hongwei Yong, Jianqiang Huang, Deyu Meng, Xiansheng Hua, and Lei Zhang. Momentum Batch Normalization for Deep Learning with Small Batch Size. In Andrea Vedaldi, Horst Bischof, Thomas Brox, and Jan-Michael Frahm, editors, Computer Vision – ECCV 2020, volume 12357, pages 224–240. Springer International Publishing, Cham, 2020. ISBN 978-3030-58609-6 978-3-030-58610-2. doi: 10.1007/978-3-030-58610-2_14.
- [33] He He and Dongrui Wu. Transfer Learning for Brain–Computer Interfaces: A Euclidean Space Data Alignment Approach. IEEE Transactions on Biomedical Engineering, 67(2):399–410,

2020. doi: 10.1109/TBME.2019.2913914.

- [34] Stylianos Bakas, Siegfried Ludwig, Konstantinos Barmpas, Mehdi Bahri, Yannis Panagakis, Nikolaos Laskaris, Dimitrios A. Adamos, and Stefanos Zafeiriou. Team Cogitat at NeurIPS 2021: Benchmarks for EEG Transfer Learning Competition, 2022.
- [35] Michael M. Bronstein, Joan Bruna, Yann LeCun, Arthur Szlam, and Pierre Vandergheynst. Geometric Deep Learning: Going beyond Euclidean data. IEEE Signal Processing Magazine, 34(4):18–42, 2017. doi: 10.1109/MSP.2017.2693418.
- [36] Ce Ju and Cuntai Guan. Deep Optimal Transport on SPD Manifolds for Domain Adaptation. arXiv:2201.05745 [cs, eess], 2022.
- [37] Zhiwu Huang and Luc Van Gool. A Riemannian Network for SPD Matrix Learning. In Proceedings of the Thirty-First AAAI Conference on Artiﬁcial Intelligence, AAAI’17, pages 2036–2042. AAAI Press, 2017.
- [38] Woong-Gi Chang, Tackgeun You, Seonguk Seo, Suha Kwak, and Bohyung Han. DomainSpeciﬁc Batch Normalization for Unsupervised Domain Adaptation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019.
- [39] Rajendra Bhatia. Positive deﬁnite matrices. Princeton university press, 2009. ISBN 978-0-69116825-8.
- [40] P-A Absil, Robert Mahony, and Rodolphe Sepulchre. Optimization algorithms on matrix manifolds. Princeton University Press, 2009.
- [41] Xavier Pennec, Pierre Fillard, and Nicholas Ayache. A Riemannian framework for tensor computing. International Journal of computer vision, 66(1):41–66, 2006.
- [42] Hermann Karcher. Riemannian center of mass and molliﬁer smoothing. Communications on pure and applied mathematics, 30(5):509–541, 1977.
- [43] Shun-ichi Amari. Information geometry and its applications, volume 194. Springer, Tokyo, 1 edition, 2016. ISBN 978-4-431-55978-8.
- [44] Daniel Brooks, Olivier Schwander, Frederic Barbaresco, Jean-Yves Schneider, and Matthieu Cord. Riemannian batch normalization for SPD neural networks. In Advances in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019.

- [45] Sergey Ioffe and Christian Szegedy. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In International conference on machine learning, pages 448–456. PMLR, 2015.
- [46] Reinmar J. Kobler, Jun-ichiro Hirayama, and Motoaki Kawanabe. Controlling The Fréchet Variance Improves Batch Normalization on the Symmetric Positive Deﬁnite Manifold. In ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 3863–3867, Singapore, 2022. IEEE. ISBN 978-1-66540-540-9. doi: 10.1109/ ICASSP43922.2022.9746629.
- [47] Shibani Santurkar, Dimitris Tsipras, Andrew Ilyas, and Aleksander Ma˛dry. How Does Batch Normalization Help Optimization? In Proceedings of the 32nd International Conference on Neural Information Processing Systems, NIPS’18, pages 2488–2498, Red Hook, NY, USA,

2018. Curran Associates Inc.

- [48] Sergey Ioffe. Batch Renormalization: Towards Reducing Minibatch Dependence in BatchNormalized Models. In Proceedings of the 31st International Conference on Neural Information Processing Systems, NIPS’17, pages 1942–1950, Red Hook, NY, USA, 2017. Curran Associates Inc. ISBN 978-1-5108-6096-4.
- [49] Catalin Ionescu, Orestis Vantzos, and Cristian Sminchisescu. Matrix Backpropagation for Deep Networks with Structured Layers. In 2015 IEEE International Conference on Computer Vision (ICCV), pages 2965–2973, Santiago, Chile, 2015. IEEE. ISBN 978-1-4673-8391-2. doi: 10.1109/ICCV.2015.339.
- [50] Jeffrey Ho, Guang Cheng, Hesamoddin Salehian, and Baba Vemuri. Recursive Karcher Expectation Estimators And Geometric Law of Large Numbers. In Carlos M. Carvalho and Pradeep Ravikumar, editors, Proceedings of the Sixteenth International Conference on Artiﬁcial Intelligence and Statistics, volume 31 of Proceedings of Machine Learning Research, pages 325–332, Scottsdale, Arizona, USA, 2013. PMLR.
- [51] Vincent Arsigny, Pierre Fillard, Xavier Pennec, and Nicholas Ayache. Geometric Means in a Novel Vector Space Structure on Symmetric Positive-Deﬁnite Matrices. SIAM Journal on Matrix Analysis and Applications, 29(1):328–347, 2007. doi: 10.1137/050637996.
- [52] Paul L. Nunez and Ramesh Srinivasan. Electric Fields of the Brain. Oxford University Press,

2006. ISBN 978-0-19-505038-7. doi: 10.1093/acprof:oso/9780195050387.001.0001.

- [53] Christoph M. Michel, Micah M. Murray, Göran Lantz, Sara Gonzalez, Laurent Spinelli, and Rolando Grave De Peralta. EEG source imaging. Clinical Neurophysiology, 115(10), 2004. doi: 10.1016/j.clinph.2004.06.001.
- [54] A. Hyvärinen and E. Oja. Independent component analysis: algorithms and applications. Neural Networks, 13(4-5):411–430, 2000. doi: 10.1016/S0893-6080(00)00026-5.
- [55] Stefan Haufe, Frank Meinecke, Kai Görgen, Sven Dähne, John Dylan Haynes, Benjamin Blankertz, and Felix Bießmann. On the interpretation of weight vectors of linear models in multivariate neuroimaging. NeuroImage, 87:96–110, 2014. doi: 10.1016/j.neuroimage.2013.10. 067.
- [56] Robin Tibor Schirrmeister, Jost Tobias Springenberg, Lukas Dominique Josef Fiederer, Martin Glasstetter, Katharina Eggensperger, Michael Tangermann, Frank Hutter, Wolfram Burgard, and Tonio Ball. Deep learning with convolutional neural networks for EEG decoding and visualization: Convolutional Neural Networks in EEG Analysis. Human Brain Mapping, 38

(11):5391–5420, 2017. doi: 10.1002/hbm.23730.

- [57] Dinesh Acharya, Zhiwu Huang, Danda Pani Paudel, and Luc Van Gool. Covariance Pooling for Facial Expression Recognition. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, 2018.
- [58] Gary Becigneul and Octavian-Eugen Ganea. Riemannian Adaptive Optimization Methods. In International Conference on Learning Representations, 2019.

- [59] G. Pfurtscheller and C. Neuper. Motor imagery and direct brain-computer communication. Proceedings of the IEEE, 89(7):1123–1134, 2001. doi: 10.1109/5.939829.
- [60] Frédéric Dehais, Alex Lafont, Raphaëlle Roy, and Stephen Fairclough. A Neuroergonomics Approach to Mental Workload, Engagement and Human Performance. Frontiers in Neuroscience, 14:268, 2020. doi: 10.3389/fnins.2020.00268.
- [61] Ana R. C. Donati, Solaiman Shokur, Edgard Morya, Debora S. F. Campos, Renan C. Moioli, Claudia M. Gitti, Patricia B. Augusto, Sandra Tripodi, Cristhiane G. Pires, Gislaine A. Pereira, Fabricio L. Brasil, Simone Gallo, Anthony A. Lin, Angelo K. Takigami, Maria A. Aratanha, Sanjay Joshi, Hannes Bleuler, Gordon Cheng, Alan Rudolph, and Miguel A. L. Nicolelis. LongTerm Training with a Brain-Machine Interface-Based Gait Protocol Induces Partial Neurological Recovery in Paraplegic Patients. Scientiﬁc Reports, 6(1):30383, 2016. doi: 10.1038/srep30383.
- [62] Domen Novak, Roland Sigrist, Nicolas J. Gerig, Dario Wyss, René Bauer, Ulrich Götz, and Robert Riener. Benchmarking Brain-Computer Interfaces Outside the Laboratory: The Cybathlon 2016. Frontiers in Neuroscience, 11:756, 2018. doi: 10.3389/fnins.2017.00756.
- [63] Michael Tangermann, Klaus-Robert Müller, Ad Aertsen, Niels Birbaumer, Christoph Braun, Clemens Brunner, Robert Leeb, Carsten Mehring, Kai J Miller, Gernot Müller-Putz, Guido Nolte, Gert Pfurtscheller, Hubert Preissl, Gerwin Schalk, Alois Schlögl, Carmen Vidaurre, Stephan Waldert, and Benjamin Blankertz. Review of the BCI Competition IV. Frontiers in Neuroscience, 6, 2012.
- [64] Josef Faller, Carmen Vidaurre, Teodoro Solis-Escalante, Christa Neuper, and Reinhold Scherer. Autocalibration and recurrent adaptation: towards a plug and play online ERD-BCI. Neural Systems and Rehabilitation Engineering, IEEE Transactions on, 20(3):313–319, 2012.
- [65] Min-Ho Lee, O-Yeon Kwon, Yong-Jeong Kim, Hong-Kyung Kim, Young-Eun Lee, John Williamson, Siamac Fazli, and Seong-Whan Lee. EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy. GigaScience, 8(5):giz002, 2019. doi: 10.1093/gigascience/giz002.
- [66] Rea Lehner, Neethu Robinson, Tushar Chouhan, Mihelj Mihelj, Ernest, Kratka Kratka, Paulina, Frédéric Debraine, Cuntai Guan, and Nicole Wenderoth. Design considerations for long term non-invasive Brain Computer Interface training with tetraplegic CYBATHLON pilot: CYBATHLON 2020 Brain-Computer Interface Race Calibration Paradigms. 2020. doi: 10. 3929/ETHZ-B-000458693. URL http://hdl.handle.net/20.500.11850/458693.
- [67] James R. Stieger, Stephen A. Engel, and Bin He. Continuous sensorimotor rhythm based brain computer interface learning in a large population. Scientiﬁc Data, 8(1):98, 2021. doi: 10.1038/s41597-021-00883-1.
- [68] Lea Hehenberger, Reinmar J. Kobler, Catarina Lopes-Dias, Nitikorn Srisrisawang, Peter Tumfart, John B. Uroko, Paul R. Torke, and Gernot R. Müller-Putz. Long-term mutual training for the CYBATHLON BCI Race with a tetraplegic pilot: a case study on inter-session transfer and intrasession adaptation. Frontiers in Human Neuroscience, 2021. doi: 10.3389/fnhum.2021.635777.
- [69] Marcel F. Hinss, Ludovic Darmet, Bertille Somon, Emilie Jahanpour, Fabien Lotte, Simon Ladouce, and Raphaëlle N. Roy. An EEG dataset for cross-session mental workload estimation: Passive BCI competition of the Neuroergonomics Conference 2021. 2021. doi: 10.5281/ ZENODO.5055046.
- [70] Alexandre Gramfort. MEG and EEG data analysis with MNE-Python. Frontiers in Neuroscience, 7, 2013. doi: 10.3389/fnins.2013.00267.
- [71] Kai Keng Ang, Zhang Yang Chin, Haihong Zhang, and Cuntai Guan. Filter Bank Common Spatial Pattern (FBCSP) in Brain-Computer Interface. In 2008 IEEE International Joint Conference on Neural Networks (IEEE World Congress on Computational Intelligence), pages 2390–2397, Hong Kong, China, 2008. IEEE. ISBN 978-1-4244-1820-6. doi: 10.1109/IJCNN. 2008.4634130.

- [72] Or Yair, Felix Dietrich, Ronen Talmon, and Ioannis G. Kevrekidis. Domain Adaptation with Optimal Transport on the Manifold of SPD matrices. arXiv:1906.00616 [cs, stat], 2020.
- [73] Vernon J Lawhern, Amelia J Solon, Nicholas R Waytowich, Stephen M Gordon, Chou P Hung, and Brent J Lance. EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces. Journal of Neural Engineering, 15(5):056013, 2018. doi: 10.1088/ 1741-2552/aace8c.
- [74] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan, Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, Alban Desmaison, Andreas Kopf, Edward Yang, Zachary DeVito, Martin Raison, Alykhan Tejani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang, Junjie Bai, and Soumith Chintala. PyTorch: An Imperative Style, High-Performance Deep Learning Library. In H. Wallach, H. Larochelle, A. Beygelzimer, F. d’ Alché-Buc, E. Fox, and R. Garnett, editors, Advances in Neural Information Processing Systems 32, pages 8024–8035. Curran Associates, Inc., 2019.
- [75] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12:2825–2830, 2011.
- [76] Marian Tietz, Thomas J. Fan, Daniel Nouri, Benjamin Bossan, and skorch Developers. skorch: A scikit-learn compatible neural network library that wraps PyTorch. 2017. URL https: //skorch.readthedocs.io/en/stable/.
- [77] Max Kochurov, Rasul Karimov, and Serge Kozlukov. Geoopt: Riemannian Optimization in PyTorch, 2020. _eprint: 2005.02819.
- [78] Barachant Alexandre. pyRiemann, 2022. URL https://github.com/pyRiemann/ pyRiemann.
- [79] James Townsend, Niklas Koep, and Sebastian Weichwald. Pymanopt: A python toolbox for optimization on manifolds using automatic differentiation. Journal of Machine Learning Research, 17(137):1–5, 2016.
- [80] Ian G. Campbell. EEG Recording and Analysis for Sleep Research. Current Protocols in Neuroscience, 49(1):10.2.1–10.2.19, 2009. doi: 10.1002/0471142301.ns1002s49.
- [81] Hubert Banville, Omar Chehab, Aapo Hyvärinen, Denis-Alexander Engemann, and Alexandre Gramfort. Uncovering the structure of clinical EEG signals with self-supervised learning. Journal of Neural Engineering, 2020. doi: 10.1088/1741-2552/abca18.
- [82] U. Rajendra Acharya, S. Vinitha Sree, G. Swapna, Roshan Joy Martis, and Jasjit S. Suri. Automated EEG analysis of epilepsy: A review. Knowledge-Based Systems, 45:147–165, 2013. doi: https://doi.org/10.1016/j.knosys.2013.02.014.
- [83] Marc R. Nuwer, David A. Hovda, Lara M. Schrader, and Paul M. Vespa. Routine and quantitative eeg in mild traumatic brain injury. Clinical Neurophysiology, 116(9):2001–2025, 2005. doi: 10.1016/j.clinph.2005.05.008.
- [84] Lukas A.W. Gemein, Robin T. Schirrmeister, Patryk Chrabaszcz, Daniel Wilson, Joschka Boedecker, Andreas Schulze-Bonhage, Frank Hutter, and Tonio Ball. Machine-learning-based diagnostics of EEG pathology. NeuroImage, 220:117021, 2020. doi: 10.1016/j.neuroimage. 2020.117021.
- [85] Yaroslav Ganin, Evgeniya Ustinova, Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, Mario March, and Victor Lempitsky. Domain-Adversarial Training of Neural Networks. Journal of Machine Learning Research, 17(59):1–35, 2016.

### Checklist

- 1. For all authors...

- (a) Do the main claims made in the abstract and introduction accurately reﬂect the paper’s contributions and scope? [Yes]
- (b) Did you describe the limitations of your work? [Yes] See section 6
- (c) Did you discuss any potential negative societal impacts of your work? [Yes] See section 6
- (d) Have you read the ethics review guidelines and ensured that your paper conforms to them? [Yes]

- 2. If you are including theoretical results...

- (a) Did you state the full set of assumptions of all theoretical results? [Yes] See paragraph 4 in section3.
- (b) Did you include complete proofs of all theoretical results? [Yes] See appendixA.1 in the supplementary material.

- 3. If you ran experiments...

- (a) Did you include the code, data, and instructions needed to reproduce the main experimental results (either in the supplemental material or as a URL)? [Yes] See Supplementary Material.
- (b) Did you specify all the training details (e.g., data splits, hyperparameters, how they were chosen)? [Yes] See paragraph 2 in section 5 for a brief summary and appendix A.2 for details.
- (c) Did you report error bars (e.g., with respect to the random seed after running experiments multiple times)? [Yes] We provide error bars with respect to the variability across sessions and subjects.
- (d) Did you include the total amount of compute and the type of resources used (e.g., type of GPUs, internal cluster, or cloud provider)? [Yes] See paragraph 3 in section 5.

- 4. If you are using existing assets (e.g., code, data, models) or curating/releasing new assets...

- (a) If your work uses existing assets, did you cite the creators? [Yes] See paragraph 1 in section 5.
- (b) Did you mention the license of the assets? [Yes] See appendix A.2.1 in the Supplementary material.
- (c) Did you include any new assets either in the supplemental material or as a URL? [No]
- (d) Did you discuss whether and how consent was obtained from people whose data you’re using/curating? [Yes] See paragraph 1 in section 5.
- (e) Did you discuss whether the data you are using/curating contains personally identiﬁable information or offensive content? [Yes] See paragraph 1 in section 5.

- 5. If you used crowdsourcing or conducted research with human subjects...

- (a) Did you include the full text of instructions given to participants and screenshots, if applicable? [N/A]
- (b) Did you describe any potential participant risks, with links to Institutional Review Board (IRB) approvals, if applicable? [N/A]
- (c) Did you include the estimated hourly wage paid to participants and the total amount spent on participant compensation? [N/A]

### A Supplementary Material

#### A.1 Proof of proposition 1

In the proof, we will use Theorem 2 of [50] which relates the distance between interpolated points along the geodesic R#γS, connecting points R and S, and point T to the distances between R, S and T. Formally, for all R,S,T ∈ SD+ we have

δ2(R#γS,T) ≤ (1 − γ)δ2(R,T) + γδ2(S,T) − γ(1 − γ)δ2(R,S) (22)

As a last ingredient for the proof, we use Proposition 1 of [50], which states that for a random variable U, following distribution PU deﬁned on SD+ with Fréchet mean GU, we have for any point V ∈ SD+:

E{δ2(U,V)} ≥ δ2(u,GU)dPU(u)

##### +δ2(V,GU) (23)

=:Var(U)

which means that the expected distance between V and U is bounded from below by the variance of U and the distance between V and its Fréchet mean GU. Let us quickly repeat the deﬁnitions, assumptions and proposition 1. We deﬁne a dataset containing the latent representations generated with feature set θk as Zθk

(x)|x ∈ T }, and a minibatch of M iid samples drawn from Zθk

= {fθ

k

as Gθ

at training step k as Bk. We denote the Fréchet mean of Zθk

, the estimated Fréchet mean, deﬁned in (9), as Gk, and the estimated batch mean as Bk. Since the batches are drawn randomly, we consider Bk and Gk as random variables. We assume that the variance Varθ

k

)} of the previous batch mean Bk−1 with respect to the current Fréchet mean Gθ

(Bk−1) = EB

k−1{δ2(Bk−1,Gθ

k

k

is bounded by the current variance Varθ

(Bk) and the norm of the difference in the parameters

k

k

(Bk) (24) Proposition 1 states then that the variance of the running mean Varθ

(Bk−1) ≤ (1 + ||θk − θk−1||)Varθ

Varθ

k

k

(Gk) is bounded by Varθ

k

(Bk) (25) over training steps k, if

(Gk) ≤ Varθ

k

k

1 − γ2 (1 − γ)2 − 1 (26)

||θk − θk−1|| ≤

holds true. Proof of Proposition 1. We prove Proposition 1 via induction. We assume that the variance Varθ

(Gk−1), that is the expected distance between the running mean Gk−1 and the Fréchet mean Gθ

k

, is bounded by the variance of the batch mean Bk−1:

k

k−1{δ2(Gk−1,Gθ

(Bk−1) (27)

(Gk−1) = EG

)} ≤ Varθ

Varθ

k

k

k

and show that this also holds for Gk and Bk. The assumption is trivially satisﬁed for G0 = B0. We start the induction step with (22) and apply it to the update rule for the running estimate Gk. As a result, we have

δ2(Gk,Gθ

) ≤ (1 − γ)δ2(Gk−1,Gθ

) + γδ2(Bk,Gθ

) − γ(1 − γ)δ2(Gk−1,Bk) (28)

k

k

k

where we used Gk = Gk−1#γBk, as deﬁned in algorithm 1. Taking the expectations for the random variables Gk, Gk−1 and Bk, we get

k{δ2(Gk−1,Bk)}} (29) Using (23) to simplify the last term, we obtain

(Bk)−γ(1−γ)EG

k−1{EB

(Gk) ≤ (1−γ)Varθ

Varθ

(Gk−1)+γVarθ

k

k

k

(Gk) ≤ (1 − γ)Varθ

(Bk) − γ(1 − γ)(Varθ

Varθ

(Gk−1) + γVarθ

(Gk−1) + Varθ

(Bk))

k

k

k

k

k

(30) ≤ (1 − γ)2Varθ

(Gk−1) + γ2Varθ

(Bk) (31) Applying assumptions (27) and (24), we get

k

k

(27)

≤ (1 − γ)2Varθ

(Bk−1) + γ2Varθ

(Bk) (32)

Varθ

(Gk)

k

k

k

(24)

≤ (1 − γ)2(1 + ||θk − θk−1||) + γ2 Varθ

(Bk) (33)

k

The resulting inequality holds true, for

1 − γ2 (1 − γ)2 − 1 (34)

!

!

(1 − γ)2(1 + ||θk − θk−1||) + γ2

≤ 1 ⇔ ||θk − θk−1||

≤

and, in turn, results in feasible bounds for the parameter updates for ﬁxed γ ∈ (0,1). This concludes the proof.

| |
|---|

- A.2 Supplementary Methods

- A.2.1 Datasets

A summary of the datasets’ key attributes is listed in Table3. The datasets contain a diverse sample of 154 human subjects, whose data was acquired in Europe (38 subjects; BNCI2014001,BNCI2015001,Lehner2021,Hehenberger2021,Hinss2021), Asia (54 subjects; Lee2019) and North America (62 subjects; Stieger2021).

- A.2.2 Preprocessing

Depending on the dataset, either all or a subset of EEG channels was selected, and then resampled along the temporal dimension to a sampling rate of either 250 or 256 Hz. (see Table 3). Thereafter, an inﬁnite impulse response (IIR) bandpass ﬁlter was used to extract EEG activity in the 4 to 36 Hz range (4th order Butterworth ﬁlter, 4 and 36 Hz cut-off frequencies, zero-phase). Some baseline methods required spectrally resolved input data. For these, we applied a bank of 8 ﬁlters with similar parameters except for the cut-off frequencies ([4, 8], [8, 12], ..., [32, 36] Hz). Finally, short epochs (=segments) were extracted (see Table 3) relative to the task cues (=labels). The labeled data were then extended with a domain index (= unique integer associated to one session of one subject).

- A.2.3 Baseline methods

We considered several established and SoA baseline methods which were previously applied to intersession/-subject TL. They can be broadly categorized as component based, Riemannian geometry aware or deep learning which we denote component, geometric and end-to-end, respectively. For the component category, we considered the popular ﬁlter-bank common spatial patterns (FBCSP+SVM) [71] and a variant [68], designed for MSMTUDA, that applies domain-speciﬁc standardization (DSS) to features before classiﬁcation, denoted FBCSP+DSS+LDA. The geometric category was represented by TSM+SVM [12], a spectrally resolved variant [17] denoted FB+TSM+LR (which was also used as domain-speciﬁc baseline method). We additionally considered two MSUDA methods, denoted URPA+MDM and SPDOT+TSM+SVM here, that align SPD observations (=spatial covariance matrices) of different domains. The former uses Riemannian Procrustes Analysis (RPA) [30] to align domains, and the latter optimal transport (OT) on SD+ [72]. The end-to-end category was represented by EEGNet [73] and ShConvNet [56] two convolutional neural network architectures speciﬁcally designed for EEG data. We additionally considered variants [25] that use domain-adversarial neural networks (DANN) [85] to learn domain-invariant latent representations.

- A.2.4 Domain-speciﬁc reference method

Due to the success of TSM models [14, 10], we considered a spectrally resolved model [13, 17] which consisted of a ﬁlter-bank to separate activity of canonical frequency bands. For each frequency band, PCA was used to reduce the spatial dimensionality and TSM to project the SPD features to the Euclidean vector space. Finally, all features were pooled and submitted to a penalized logistic regression classiﬁer. For further details, see [17].

- A.2.5 TSMNet

Architecture The architecture of TSMNet is outlined in Figure 4 and detailed in Table 4. The feature extractor fθ comprises two convolutional layers, followed by covariance pooling [57], BiMap

- 6We used 20 channels that covered sensorimotor areas.
- 7We used 34 channels that covered sensorimotor areas. 8To reduce computation time, only data from the 4th to last session were considered (inter-session) or last

session (inter-subject). 9We used 30 channels with a dense coverage in frontal areas. 10The dataset is shared on an individual basis by the authors of [68].

[37] and ReEig [37] layers. The ﬁrst convolutional layer performs convolution along the temporal dimension; implementing a ﬁnite impulse response (FIR) ﬁlter bank (4 ﬁlters) with learnable parameters. The second convolutional layer applies spatio-spectral ﬁlters (40 ﬁlters) along the spatial and convolutional channel dimensions. Covariance pooling is then applied along the temporal dimension. A subsequent BiMap layer projects covariance matrices to a subspace via a bilinear mapping (i.e, BiMap(Z) = WθTZWθ) where the parameter matrix Wθ is constrained to have orthogonal rows (i.e., Wθ ∈ {U ∈ RI×O : UTU = IO,I ≥ O}). Next, a ReEig layer rectiﬁes all eigenvalues, lower than a threshold = 10−4 (i.e, ReEig(Z) = Umax(Σ, I)UT with [Σ,U] = eig(Z)).

Domain-speciﬁc tangent space mapping mφ is implemented via combining SPDDSMBN and LogEig layers. In order for mφ to align the domain data and compute TSM, we use SPDDSMBN (18) with shared parameters (i.e., Gφ

= νφ) in (16). The classiﬁer gψ was parametrized as a linear layer with softmax activations.

= Gφ = I,νφ

i

i

Parameter estimation We used the cross entropy loss as training objective, and the standard backpropagation framework with extensions for structured matrices [49] and manifold-constrained gradients [40] to propagate gradients through the layers of TSMNet. Gradients were estimated with mini-batches of ﬁxed size (50 observations; 10 per domain; 5 distinct domains) and converted into parameter updates with the Riemannian ADAM optimizer [58] (10−3 learning rate, 10−4 weight decay applied to unconstrained parameters; β1 = 0.9,β2 = 0.999). For every MSMTUDA problem, comprising source and target domain sets, we split the source domains’ data into training and validation sets (80%/20% splits; randomized; stratiﬁed across domains and labels) and repeatedly iterated through the training set for 50 epochs via exhaustive minibatch sampling. As required by SPDMBN, we implemented a decaying schedule (over epochs) for the training momentum parameter γtrain(k), deﬁned in (11), with γtrain(0) = 1 and γmin = 0.2 attained at epoch K = 40. During training, we monitored the loss on the validation data (at the end of every epoch). Post training, the model with minimal loss on the validation data was selected. For each target domain, the associated data was then passed through this model to estimate the labels. During the forward pass, the domain’s normalization statistics within the SPDMBN layers were computed by solving (4) with the Karcher ﬂow algorithm [42].

- A.3 Supplementary results A.3.1 EEG data

The test set score for each considered EEG dataset is summarized in in Table 5. Signiﬁcant differences between the proposed method (TSMNet with SPDDSMBN) and baseline methods are highlighted.

11Shared Frechet variance parameter νφ2.

- Table 3: Dataset attributes. The epoch indices the temporal window after a task cue (time relative to cue onset) that was extracted from continuous EEG data.

epoch sampling channels subjects sessions obsevations dataset (s) rate (Hz) # # # # (per session) BNCI2014001 0.5 - 3.5 250 22 9 2 288 BNCI2015001 1.0 - 4.0 256 13 12 2-3 200 Lee2019 1.0 - 3.5 250 206 54 2 100 Stieger2021 1.0 - 3.0 250 347 62 4-88 390 Lehner2021 0.5 - 2.5 250 60 1 7 61 Hehenberger2021 1.0 - 3.0 250 32 1 26 105 Hinss2021 0.0 - 2.0 250 309 15 2 447

classes license identiﬁer linked dataset # publication BNCI2014001 4 CC BY-ND 4.0 001-2014 [63] BNCI2015001 2 CC BY-NC-ND 4.0 001-2015 [64] Lee2019 2 unspeciﬁed 100542 [65] Stieger2021 4 CC BY 4.0 m9.ﬁgshare.13123148.v1 [67] Lehner2021 2 InC-NC 10.3929/ethz-b-000458693 [66] Hehenberger2021 4 individual10 - [68] Hinss2021 3 CC BY-SA 4.0 10.5281/zenodo.5055046 [69]

[Figure 4]

Figure 4: Overview of the TSMNet architecture. The network uses observations X and the associated domain index i to estimate the target label yˆ.

- Table 4: TSMNet architecture details. The letters P, T and C refer to the number of input channels, temporal samples and classes.

Block Input (dim) Output (dim) Parameter (dim) Operation Note TempConv 1 x P x T 4 x P x T 4 x 1 x 1 x 25 convolution padding: same, reﬂect SpatConv 4 x P x T 40 x 1 x T 40 x 4 x P x 1 convolution padding: valid CovPool 40 x T 40 x 40 covariance temporal dimension BiMap 40 x 40 20 x 20 40 x 20 bilinear subspace projection ReEig 20 x 20 20 x 20 EV threshold threshold = 0.0001 SPDDSMBN 20 x 20 20 x 20 111 TSM domain alignment LogEig 20 x 20 210 TSM Linear 210 C 211 x C linear softmax activation

- Table 5: Average (standard deviation across sessions or subjects) test set score (balanced accuracy; higher is better) for all BCI datasets and evaluations. Permutation-paired t-test were used to identify signiﬁcant differences between the proposed (highlighted) and baseline methods (1e4 permutations,

10 tests, tmax correction). Signiﬁcant differences are highlighted (

##### p ≤ 0.05, • p ≤ 0.01, • p ≤ 0.001).

•

dataset BNCI2014001 BNCI2015001 evaluation inter-session inter-subject inter-session inter-subject degrees of freedom / # classes 17 / 4 8 / 4 27 / 2 11 / 2

UDA method no FBCSP+SVM

32.3 ( 7.3) • 81.5 ( 4.4) • 58.6 (13.4) TSM+SVM • 61.8 ( 4.1)

60.6 ( 4.9)

•

•

34.7 ( 8.6) • 75.7 ( 5.1) • 56.0 ( 6.0) FB+TSM+LR 69.8 ( 4.8)

•

80.9 ( 6.0) • 60.6 (10.9) EEGNet • 41.8 ( 5.8)

36.5 ( 8.2)

•

•

43.3 (17.0) • 72.4 ( 8.4) • 59.2 ( 9.5) ShConvNet • 51.3 ( 2.3)

•

42.2 (16.2) • 74.1 ( 4.2) • 58.7 ( 5.8)

•

yes FBCSP+DSS+LDA 71.3 ( 1.8) 48.3 (14.3) 84.6 ( 4.8) • 67.7 (14.3) URPA+MDM • 59.5 ( 2.7) 46.8 (14.6) • 79.2 ( 4.6) • 70.3 (16.1) SPDOT+TSM+SVM 66.8 ( 3.8)

38.6 ( 8.6) • 77.5 ( 2.9) • 63.3 ( 8.1) EEGNet+DANN • 50.0 ( 7.7) 45.8 (18.0) • 71.6 ( 5.3) • 63.7 (11.1) ShConvNet+DANN • 51.6 ( 3.2)

•

42.2 (13.6) • 74.1 ( 4.0) • 64.2 (11.6) TSMNet(SPDDSMBN) 69.0 ( 3.6) 51.6 (16.5) 85.8 ( 4.3) 77.0 (13.7)

•

dataset Lee2019 Stieger2021 evaluation inter-session inter-subject inter-session inter-subject degrees of freedom / # classes 107 / 2 53 / 2 411 / 4 61 / 4

UDA method

no FBCSP+SVM • 63.1 ( 4.2) • 63.4 (12.1) • 47.5 ( 7.0) • 37.6 (10.5) TSM+SVM • 62.5 ( 3.3) • 65.3 (13.0) • 49.5 ( 8.1) • 40.2 (12.3) FB+TSM+LR • 65.2 ( 4.5) • 68.5 (12.4) • 57.3 ( 7.3) • 40.3 ( 9.2) EEGNet • 51.2 ( 2.7) • 69.6 (13.8) • 58.3 ( 7.9) • 43.1 (11.0) ShConvNet • 57.8 ( 4.0) • 68.5 (13.6) • 60.1 ( 6.6) • 42.2 (10.4)

yes FBCSP+DSS+LDA 66.8 ( 4.1) • 68.7 (13.8) • 59.4 ( 6.6) • 48.2 (13.4) URPA+MDM • 63.8 ( 4.2) • 66.7 (12.3) • 47.0 ( 6.6) • 38.7 (10.4) SPDOT+TSM+SVM • 65.6 ( 4.2) • 65.4 (10.5) • 50.3 ( 5.8) • 42.1 (10.5) EEGNet+DANN • 55.4 ( 4.4) • 69.4 (13.1) • 60.1 ( 6.9) • 43.6 (10.7) ShConvNet+DANN • 59.1 ( 3.4) • 66.0 (12.4) • 61.3 ( 6.0) • 43.1 (11.5) TSMNet(SPDDSMBN) 68.2 ( 4.1) 74.6 (14.2) 64.8 ( 6.8) 48.9 (14.3)

dataset Lehner2021 Hehen.2021 Hinss2021 evaluation inter-session inter-session inter-session inter-subject degrees of freedom / # classes 6 / 2 25 / 4 29 / 3 14 / 3

UDA method no FBCSP+SVM 68.9 ( 6.0) • 52.5 ( 7.1) • 43.7 ( 8.2) 45.6 ( 6.5)

TSM+SVM 62.7 ( 9.1) • 44.8 ( 7.3) • 36.8 ( 4.5) • 41.7 ( 7.4) FB+TSM+LR 73.0 ( 9.6) • 52.2 ( 6.0) • 40.8 ( 7.1)

45.1 ( 5.0) EEGNet

•

49.6 ( 6.4) • 48.2 ( 6.3) • 46.3 (10.1) 47.8 ( 5.1) ShConvNet

•

56.3 ( 7.3) • 53.0 ( 5.1) 48.9 ( 7.4)

45.9 ( 6.8)

•

•

yes FBCSP+DSS+LDA 77.1 ( 8.4) 56.4 ( 5.3) • 47.1 ( 7.4) 48.4 ( 9.0) URPA+MDM 70.8 ( 8.2) • 46.6 ( 7.2) 51.4 ( 3.7) 48.4 ( 6.1) SPDOT+TSM+SVM

63.0 ( 9.2) • 45.9 ( 6.0) • 42.0 ( 4.7) • 40.4 ( 7.5) EEGNet+DANN

•

49.4 ( 6.8) 50.0 ( 7.3) ShConvNet+DANN

49.8 ( 3.7) • 49.3 ( 6.7)

•

•

54.0 ( 5.1) 51.5 ( 4.9) 48.8 ( 5.7) TSMNet(SPDDSMBN) 77.7 (10.0) 57.8 ( 5.8) 54.7 ( 7.3) 52.4 ( 8.8)

57.5 ( 7.6)

•

•

