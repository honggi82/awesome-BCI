# Spatiotemporal Sparse Bayesian Learning with Applications to Compressed Sensing of Multichannel Physiological Signals

Zhilin Zhang∗, Member, IEEE, Tzyy-Ping Jung, Senior Member, IEEE, Scott Makeig, Member, IEEE Zhouyue Pi, Senior Member, IEEE, Bhaskar D. Rao, Fellow, IEEE

arXiv:1404.5122v2[cs.IT]15Nov2014

Abstract— Energy consumption is an important issue in continuous wireless telemonitoring of physiological signals. Compressed sensing (CS) is a promising framework to address it, due to its energy-efﬁcient data compression procedure. However, most CS algorithms have difﬁculty in data recovery due to nonsparsity characteristic of many physiological signals. Block sparse Bayesian learning (BSBL) is an effective approach to recover such signals with satisfactory recovery quality. However, it is time-consuming in recovering multichannel signals, since its computational load almost linearly increases with the number of channels.

This work proposes a spatiotemporal sparse Bayesian learning algorithm to recover multichannel signals simultaneously. It not only exploits temporal correlation within each channel signal, but also exploits inter-channel correlation among different channel signals. Furthermore, its computational load is not signiﬁcantly affected by the number of channels. The proposed algorithm was applied to brain computer interface (BCI) and EEG-based driver’s drowsiness estimation. Results showed that the algorithm had both better recovery performance and much higher speed than BSBL. Particularly, the proposed algorithm ensured that the BCI classiﬁcation and the drowsiness estimation had little degradation even when data were compressed by 80%, making it very suitable for continuous wireless telemonitoring of multichannel signals.

Index Terms—Sparse Bayesian Learning (SBL), Compressed Sensing (CS), Spatiotemporal Correlation, Telemonitoring, Wireless Body-Area Network (WBAN), Electroencephalography (EEG), Brain-Computer Interface (BCI)

I. INTRODUCTION

Compressed sensing (CS) [1] has been drawing increasing attention in the wireless telemonitoring of physiological sig-

Manuscript received May 7, 2013; revised February 18, 2014; accepted April 13, 2014. The work was supported by NSF grants CCF-0830612, CCF1144258 and DGE-0333451, and was in part supported by Army Research Lab, Army Research Ofﬁce, Ofﬁce of Naval Research and DARPA. Asterisk indicates corresponding author.

Z. Zhang was with the Department of Electrical and Computer Engineering, University of California at San Diego, La Jolla, CA 92093-0407, USA. He is now with the Emerging Technology Lab, Samsung Research America – Dallas, 1301 East Lookout Drive, Richardson, TX 75082, USA. Email: zhilinzhang@ieee.org

T.-P. Jung and S. Makeig are with the Swartz Center for Computational Neuroscience and the Center for Advanced Neurological Engineering, University of California at San Diego, La Jolla, CA 92093-0559, USA.

Z. Pi is with the Emerging Technology Lab, Samsung Research America

– Dallas, 1301 East Lookout Drive, Richardson, TX 75082, USA. University of California at San Diego, La Jolla, CA 92093-0407, USA.

- B.D. Rao is with the Department of Electrical and Computer Engineering,

nals as an emerging data compression methodology 1 [2]– [7]. It has been shown that CS, compared to traditional data compression methodologies, consumes much less energy and power [8], saves lots of on-chip computational resources [9], and is robust to packet loss during wireless transmission [10]. Thus it is attractive to wireless body-area networks for ambulatory monitoring.

A. CS Models

The basic CS framework [1], also called the single measurement vector (SMV) model, can be expressed as

y = Φx + v, (1)

where, in the context of data compression, x ∈ RM×1 is a single-channel signal, Φ ∈ RN×M(N < M) is a userdesigned measurement matrix, v ∈ RN×1 is sensor noise, and y ∈ RN×1 is the compressed signal. This compression task is performed in sensors of a wireless body-area network. Then, the compressed signal y, through Bluetooth and Internet, is sent to a remote terminal. At the terminal, the original signal is recovered by a CS algorithm using the shared measurement matrix Φ, namely 2,

x = arg min

x

y − Φx 22 + λg(x), (2)

where λ is a regularization parameter, and g(x) is a penalty function of x. The most popular penalty may be the ℓ1minimization based penalty, namely g(x) = x 1. This method is called signal recovery in the original domain.

When the original signal x is sufﬁciently sparse (i.e., only a few entries of x are nonzero), many CS algorithm can exactly recover x from y in the absence of noise v or with high quality in the presence of noise 3. If x is not sparse, one can seek a dictionary matrix D such that x can be

- 1The CS technique can be used for data compression and signal sampling

[1]. In this paper the use of CS for data compression/de-compression is considered. But note the proposed algorithm can be also used as a signal recovery method in CS-based sampling.

- 2There are other mathematical expressions, which are equivalent given

suitable values for regularization parameters.

3Admittedly, when x is sparse, it is trivial to use CS for data compression, because one can just send nonzero entries (and associated locations) of x to a remote terminal and then recover it over there. When x is non-sparse, directly using the recovery method (2) results in failure for existing CS algorithms. Thus the recovery method (2) is rarely used by CS algorithms. But the block sparse Bayesian learning can adopt this method (2) to recover a non-sparse x with correlated entries (with very small errors) [6].

sparsely represented under the dictionary matrix, i.e., x = Dz, where the representation coefﬁcients z are sparse. The dictionary matrix D ∈ RM×m(M ≤ m) can be formed from orthonormal bases of known transforms such as discrete wavelet transform or discrete Cosine transform (DCT), or can be learned from data using dictionary learning [11]. Then a CS algorithm recovers the original signal according to:

x = D z with z = arg min

z

y − Ωz 22 + λg(z) (3)

where Ω ΦD. The method is called signal recovery in a transformed domain.

The basic CS framework has been widely studied for data compression/decompression of biosignals [2], [5]–[7], [12]– [14]. For example, Aviyente [2] studied the use of Gabor dictionary matrix for EEG. Later Abdulghani et al. [12] further investigated various kinds of dictionary matrices. Instead of using the popular ℓ1-minimization based penalty, other more effective penalties were proposed, such as the block-sparsity with intra-block correlation [7], [15], the analysis prior formulation [13], and the sparsity on second-order difference [14]. Chen et al. [5] proposed an energy-efﬁcient digital implementation of CS architecture for data compression in wireless sensors. Using a ﬁeld programmable gate array (FPGA) platform, Liu et al. [9] showed that CS, when compared to a low-power wavelet compression procedure, can largely save energy, power, and other on-chip computational resources.

In addition to the SMV model (1), another widely studied CS model is the multiple measurement vector (MMV) model [16], an extension of the SMV model. It can be expressed as follows:

Y = ΦX + V, (4) where Y ∈ RN×L, X ∈ RM×L and V ∈ RN×L are matrices.

- A key assumption in the MMV model is that X is row sparse, namely only a few rows of X are nonzero rows. Similar to

(2) and (3), the estimate of X is given by X = argmin

Y − ΦX 22 + λf(X), (5) or given by

X

X = D Z with Z = arg min

Z

Y − ΩZ 22 + λf(Z) (6)

where Ω ΦD, and D is a dictionary matrix. f(X) is a penalty encouraging row-sparsity of X. One popular penalty is the ℓ1/ℓ2-minimization based penalty, namely f(X) =

M i=1 Xi· 2. In (6) it is assumed that Z is row-sparse.

Compared to recovering X column by column, i.e., treating (5) [or (6)] as L individual sub-problems, the joint recovery as in (5) [or (6)] can greatly improve the recovery quality of X [16], [17]. Aviyente [2] explored this model to jointly recover multichannel EEG signals. Polania et al. [18] explored this model to jointly recover multichannel ECG signals. However, the beneﬁt of the MMV model is largely compromised if columns of X exhibit inter-vector correlation; the beneﬁt even almost disappears when the inter-vector correlation is very high [19].

Recently, by proposing the T-MSBL algorithm [19], we showed that suitably exploiting the inter-vector correlation can

greatly alleviate its negative effect. Particularly, in noiseless environments, under mild conditions the negative effect disappears no matter how large the inter-vector correlation is (as long as the correlation is not ± 1). This algorithm motivated the development of the spatiotemporal algorithm presented in this paper.

B. Challenges in the Use of CS for Wireless Telemonitoring

It is worth pointing out that most CS algorithms may not be used for energy-efﬁcient wireless telemonitoring especially ambulatory monitoring, due to several challenges [20]–[22].

One challenge comes from the strict energy constraint. A wireless telemonitoring system is generally battery-operated. This situation with other constraints (e.g., wearability and device cost) requires that the compression procedure should be as simple as possible. In other words, the pre-processing such as ﬁltering, peak detection, and dynamical thresholding, is not favored, since they increase circuitry complexity and cost extra energy. In fact, the data compression stage should be very simple. Lots of evidence have shown that the energysaving advantage of CS over conventional data compression methods might be true only when the measurement matrix Φ was a sparse binary matrix; when Φ was a random Gaussian matrix or other kinds of matrices, the advantage disappeared.

Another challenge comes from strong artifacts caused by human movement during data recording. The goal of wireless telemonitoring is to allow people to move freely. Thus, the collected physiological signals are inevitably contaminated by strong artifacts caused by muscle movement and electrode motion. As a result, even a sparse signal can become nonsparse in the time domain and also non-sparse in transformed domains [20]. The non-sparsity seriously degrades CS algorithms’ performance, resulting in their failure [6]. Therefore, CS algorithms generally need to remove artifacts before compression. But this greatly increases circuitry complexity, and conﬂicts with the energy constraint. The conﬂict is more sharp in some scenarios such as ambulatory telemonitoring.

Very recently, we proposed using the block sparse Bayesian learning (BSBL) framework [15] for CS of non-sparse physiological signals, and achieved success in telemonitoring of fetal ECG [6] and single-channel EEG [7]. The signiﬁcant innovation in those works is that, instead of using the mentioned preprocessing methods or seeking optimal dictionary matrices, we proposed a completely different approach: namely recovering non-sparse signals directly without resorting to optimal dictionary matrices or pre-processing methods. The key element in BSBL is exploitation of correlation structures of a signal.

However, BSBL is designed for recovering single-channel signals. When recovering multichannel signals, BSBL has to recover the signals channel by channel, which is timeconsuming and thus not suitable for real-time telemonitoring of multichannel signals. Besides, for many multichannel physiological signals, there is strong correlation among signals of different channels. Exploiting the inter-channel correlation is necessary and very beneﬁcial. Unfortunately, BSBL ignores it.

- C. Summary of the Work

The work introduces a spatiotemporal sparse model to the ﬁeld of CS. This model is an extension of the classic multivariate Bayesian variable selection model [23], and was recently used in overdetermined multivariate regression models to identify predictors by exploiting nonlinear relationships between predictors and responses [24]. However, this model has not been studied in CS.

Based on this model, we derive an expectationmaximization based spatiotemporal sparse Bayesian learning algorithm, and apply it to CS of multichannel signals. This algorithm has several advantages.

- • It can efﬁciently exploit temporal correlation of each channel signal and inter-channel correlation among different channel signals to improve recovery performance. As we will see later, exploiting the inter-channel correlation is very important in CS of multichannel signals.
- • It has the ability to recover non-sparse correlated signals, and signals with less-sparse representation coefﬁcients, a desired ability for wireless telemonitoring of physiological signals.
- • Compared to BSBL, it not only has better recovery performance, but also has higher speed. Its computational load is not signiﬁcantly affected by the number of channels, an obvious advantage over BSBL. Thus it is very suitable for CS of multichannel signals.
- • Different from most CS algorithms, which require preprocessing before compressing raw data, the proposed algorithm does not require any preprocessing. Its compression procedure can be implemented by very simple circuits, thus costing ultra-low energy consumption. This is highly desired for long-term wireless telemonitoring of physiological signals.

In experiments on steady-state visual evoked potential (SSVEP) based BCI and EEG-based driver’s drowsiness estimation, the proposed algorithm ensured that the BCI classiﬁcation and the drowsiness estimation on recovered data were almost the same as on original data, even when the original data were compressed by more than 80%.

Some preliminary results were published in [20]. The Matlab code of the proposed algorithm can be downloaded at https://sites.google.com/site/researchbyzhang/stsbl.

- D. Organization and Notations

The rest of the paper is organized as follows. Section II describes the spatiotemporal sparse model. Section III derives a spatiotemporal sparse Bayesian learning algorithm using the expectation-maximization method. Section IV discusses some speciﬁc settings when applying the algorithm for CS of multichannel physiological signals. Section V presents experimental results on BCI and EEG-based driver’s drowsiness estimation. Discussion and conclusion are given in the last two sections.

We introduce the notations used in this paper:

• Bold symbols are reserved for vectors and matrices. Particularly, IL denotes the identity matrix with size L × L. When the dimension is evident from the context, for simplicity, we just use I;

- • x 1, x 2, A F denote the ℓ1 norm of the vector x, the ℓ2 norm of x, and the Frobenius norm of the matrix A, respectively;
- • diag{a1,··· ,aM} denotes a diagonal matrix with principal diagonal elements being a1,··· ,aM in turn; if A1,··· ,AM are square matrices, then diag{A1,··· ,AM} denotes a block diagonal matrix with principal diagonal blocks being A1,··· ,AM in turn;
- • A ⊗ B represents the Kronecker product of the two matrices A and B. vec(A) denotes the vectorization of the matrix A formed by stacking its columns into a single column vector. Tr(A) denotes the trace of A. AT denotes the transpose of A;
- • For a matrix A, Ai· denotes the i-th row, and A·i denotes the i-th column. A[i],j denotes the i-th block in the jth column. Ai,[j] denotes the j-th block in the i-th row. When assuming all columns of A have the same block

partition, A[i]· denotes the i-th block of all columns of A.

II. THE SPATIOTEMPORAL SPARSE MODEL

To enhance the readability of the paper, we ﬁrst describe the spatiotemporal sparse model in this section, and delay the description of the proposed algorithm to the next section.

The spatiotemporal sparse model is described as follows: Y = ΦX + V, (7)

where Y ∈ RN×L, Φ ∈ RN×M 4, and X ∈ RM×L. The matrices Y and Φ are known. The goal is to estimate X. In the context of data compression, the l-th column of X, denoted by X·l, is a segment of an original physiological signal in the l-th channel, and the l-th column of Y is the corresponding compressed segment.

The matrix X is assumed to have the following block structure:





- X[1]·
- X[2]·

(8)

X =

 

 

. X[g]·

where X[i]· ∈ Rdi×L is the i-th block of X, and gi=1 di =

- M. For convenience, {d1,··· ,dg} is called the block partition. Among the g blocks, only a few are nonzero. The key

assumption is that each block X[i]·(∀i) is assumed to have spatiotemporal correlation. In other words, entries in the same

column of X[i]· are correlated 5, and entries in the same row of X[i]· are also correlated 6.

The i-th block X[i]· is assumed to have the parameterized Gaussian distribution p(vec(XT[i]·);γi,B,Ai) = N(0,(γiAi) ⊗ B). Here B ∈ RL×L is an unknown positive

4The model and the developed algorithm does not require N < M or

- N ≥ M. Thus they can be used for many other applications.

- 5In our data compression formulation, the correlation is a kind of temporal

correlation of a channel signal.

- 6In our data compression formulation, the correlation is called inter-channel

correlation, and is also called spatial correlation.

deﬁnite matrix capturing the correlation structure in each row of X[i]·. The matrix Ai ∈ Rdi×di is an unknown positive deﬁnite matrix capturing the correlation structure in each column of X[i]·. The unknown parameter γi is a nonnegative scalar, determining whether the i-th block is a zero block or not. Assuming the blocks {X[i]·}gi=1 are mutually independent, the distribution of the matrix X is

p(vec(XT);B,{γi,Ai}i) = N(0,Π ⊗ B) (9) where Π is a block diagonal matrix deﬁned by





γ1A1

γ2A2

. (10)

Π

 

 

...

γgAg

Besides, each row of the noise matrix V is assumed to have the distribution p(Vi·;λ,B) = N(0,λB), where λ is an unknown scalar. Assuming the rows are mutually independent, we have

p(vec(VT);λ,B) = N(0,λI ⊗ B). (11) Remark 1: Note that X and V share the common matrix

- B for modeling the correlation structure of each row. This is a traditional setting in Bayesian variable selection models [23], which facilitates the use of conjugate priors for multivariate linear regression. Besides, since in our applications the sensor noise V can be ignored, the covariance model of V is not important. It only facilitates the development of our algorithm.

- Remark 2: The proposed STSBL model is an extension of the model used by BSBL [15]. Setting L = 1, the STSBL model reduces to the latter. In other words, the STSBL model can be viewed as a set of multiple BSBL models with their solution vectors mutually correlated. In Section VI-C we will see the necessity of modeling the mutual correlation.
- Remark 3: The proposed STSBL model is also closely related to the T-MSBL model [19] 7. When di = 1(∀i), STSBL reduces to the latter. Note that T-MSBL only exploits correlation among entries of the same row in X, while STSBL also exploits correlation among entries of the same column in X. In the context of data compression, T-MSBL only exploits the inter-channel correlation, while STSBL exploits both the inter-channel correlation and the temporal correlation within each channel signal.

The relationships revealed in Remark 2 and Remark 3 inspire us to derive an efﬁcient algorithm, as shown below.

III. THE SPATIOTEMPORAL SBL ALGORITHM

Due to the coupling between Ai(∀i) and B, directly estimating parameters in the model (7) can result in an algorithm with heavy computational load. However, the observations in Remark 2 and Remark 3 imply that we can use B as a spatially whitening matrix, transforming the original model (7) to a spatially whitened model, and use Ai(∀i) to transform the original model to a temporally whitened model 8. Thus,

- 7Due to the difference in problem formulation, the temporal correlation studied in [19] is the inter-channel correlation in this work.
- 8In fact, the block partition is still present. But for convenience, we call the equivalent model a “temporally whitened” model.

we propose an alternating-learning approach, where the parameters {γi,Ai}gi=1 and λ are estimated from the spatially whitened model, and the parameter B is estimated from the temporally whitened model. The resulting algorithm alternates the estimation between the two models until convergence. The alternating-learning approach largely simpliﬁes the algorithm development.

A. Learning in the Spatially Whitened Model

To facilitate algorithm development, we assume B is known. Letting Y YB−12 , X XB−21, and V VB−12, the original STSBL model (7) becomes

[Figure 1]

[Figure 2]

[Figure 3]

Y = Φ X + V, (12)

where the columns of X are independent, and so does V. Thus, the original STSBL model is now spatially whitened, and the algorithm development becomes easier.

First, we have priors for p( X;Π) and p( V;λ) as follows

p( X;Π) =

p( V;λ) =

L

p( X·i) ∼

i=1

L

p( V·i) ∼

i=1

Then we have the likelihood:

i

N(0,Π) (13)

i

N(0,λI) (14)

p( Y·i| X·i;λ) = N(Φ X·i,λI) ∀i (15) Thus, we obtain the posterior:

p( X·i| Y·i;λ,Π) = N(µ·i,Σ) ∀i (16) with the mean µ·i and the covariance matrix Σ given by

µ·i = ΠΦT(λI + ΦΠΦT)−1 Y·i ∀i (17) Σ = (Π−1 +

1 λ

ΦTΦ)−1 (18) = Π − ΠΦT(λI + ΦΠΦT)−1ΦΠ (19)

[Figure 4]

Once the parameters Π and λ are estimated, the maximum-aposteriori (MAP) estimate of X is directly given by the mean of the posterior, i.e.,

X ← ΠΦT(λI + ΦΠΦT)−1 Y, (20)

and the solution matrix X in the original STSBL model (7) can be obtained:

- 1

[Figure 5]

- 2. (21)

X ← XB

Thus, estimating the parameters Π and λ is crucial to the algorithm. There are many optimization methods which can be used to estimate these parameters, such as bound-optimization methods [15], fast marginal likelihood maximization [25], and variational methods [26]. In this work we use the expectation maximization (EM) method to estimate them, since we ﬁnd the resulting algorithm can provide better recovery performance in our application.

Using the EM method, X is treated as a hidden variable. The Q-function for estimating {γi}i and {Ai}i is given by

Q(Π) E X| Y;Θ(old) log p( X;{γi}i,{Ai}i)

L

L 2

- 1

[Figure 6]

- 2

E X| Y;Θ(old) XT·iΠ−1 X·i

= −

log |Π| −

[Figure 7]

i=1

g

L 2

= −

log |γiAi|

[Figure 8]

i=1

L

- 1

[Figure 9]

- 2

Tr Π−1 Σ + µ·lµT·l

−

l=1

g

g

L 2

L 2

di log γi −

log |Ai|

= −

[Figure 10]

[Figure 11]

i=1

i=1

g

L

- 1

[Figure 12]

- 2

1 γj

Tr A−j 1 Σ[j] + µ[j]lµT[j]l ,(22)

−

[Figure 13]

j=1

l=1

where Θ(old) denotes all the parameters estimated in the previous iteration, Σ[j] denotes the j-th diagonal block in Σ which corresponds to the j-th block in X, and µ[j]l denotes the j-th block in the l-th column of µ.

Setting to zero the derivative of (22) w.r.t. γi, we obtain the updating rule for γi:

L

1 Ldi

Tr A−i 1 Σ[i] + µ[i]lµT[i]l . (23) Setting to zero the derivative of (22) w.r.t. Ai, we obtain

γi ←

[Figure 14]

l=1

the updating rule for Ai:

Σ[i] + µ[i]lµT[i]l γi

L

1 L

. (24)

Ai ←

[Figure 15]

[Figure 16]

l=1

The estimate will be further regularized as shown later.

To estimate λ, the Q-function is given by Q(λ) = E X| Y;Θ(old) log p( Y| X;λ)

NL 2

∝ −

log λ

[Figure 17]

L

- 1

[Figure 18]

- 2λ

Y·l − Φ X·l 22

−

E X| Y;Θ(old)

l=1

L

- 1

[Figure 19]

- 2λ

NL 2

Y·l − Φµ·l 22

log λ −

= −

[Figure 20]

l=1

+E X| Y;Θ(old) Φ( X·l − µ·l) 22

1 2λ

NL 2

Y − Φµ 2F −

log λ −

= −

[Figure 21]

[Figure 22]

L 2λ

Tr ΣΦTΦ . (25) Setting its derivative to zero, we have

[Figure 23]

1 NL

1 N

Y − Φµ 2F +

Tr ΣΦTΦ . (26)

λ ←

[Figure 24]

[Figure 25]

Similar to the approach adopted in [15], at low signal-to-noise (SNR) situations the above updating rule is modiﬁed to

g

1 NL

1 N

Y − Φµ 2F +

Tr Σ[i]ΦT·[i]Φ·[i] , (27)

λ ←

[Figure 26]

[Figure 27]

i=1

where Φ·[i] denotes the consecutive columns in Φ which correspond to the i-th block in X. In noiseless situations one can simply set λ = 10−10 or other small values, instead of performing the updating rule (26).

In the above development we have assumed that B is given. This parameter can be estimated in a temporally whitened model discussed below.

B. Learning in the Temporally Whitened Model

To estimate the matrix B, we consider the following equivalent form of the original model (7):

Y = Φ · X + V (28)

[Figure 28]

[Figure 29]

where Φ ΦA21 , X A−21X, and A is deﬁned as A diag{A1,··· ,Ag}. Note that in this model, X maintains the same block partition as X, but its every block has no temporal correlation due to the temporally whitening effect from A−

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

- 1

[Figure 35]

- 2

i (∀i). Thus, estimating B in this model becomes easier.

Following the approach used to derive the T-MSBL algorithm [19] and assuming X, {γi}i and {Ai}i have been obtained from the spatially whitened model (12), we have the following updating rule for the matrix B:

g

γi−1XT[i]·X[i]· + λ−1(Y − ΦX)T(Y − ΦX)

Bˇ ←

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

i=1

XT[i]·A−i 1X[i]· γi

g

(Y − ΦX)T(Y − ΦX) λ

(29)

+

=

[Figure 42]

[Figure 43]

i=1

- B ← Bˇ/ B ˇ F (30)

where X[i]· ∈ Rdi×L is the i-th block in X, and X[i]· A−

[Figure 44]

[Figure 45]

[Figure 46]

- 1

[Figure 47]

- 2

i X[i]·. The second item in (29) is noise-related. When the noise is very small, or does not exist (i.e., λ → 0), it is suggested to remove the second item for robustness.

- C. Regularization

In the proposed spatiotemporal model the number of unknown parameters is much larger than the number of available data. Thus regularization to the estimated B and {Ai}i is very important. Suitable regularization helps to overcome learning difﬁculties resulting from the very limited data.

As in [19], we can regularize the Bˇ in (29) by

g

Bˇ ←

γi−1XT[i]·A−i 1X[i]· + ηI (31)

i=1

where η is a positive scalar. This regularization is shown empirically to increase robustness in noisy environments. In noiseless environments, this regularization is not needed.

To regularize the estimates of {Ai}i, we use the strategy in [15], i.e., modeling the correlation matrix of each column in X[i]· as the correlation matrix of an AR(1) process with the common AR coefﬁcient r for all i. The strategy can be summarized as follows.

• Step 1: From each Ai, calculate the quantity ri by ri ← m

i 1

mi0 (∀i), where mi0 is the average of entries in

[Figure 48]

the main diagonal of Ai and mi1 is the average of entries in the main sub-diagonal of Ai. Note that due to some numerical problems, m

i 1

mi0 may be out of the feasible range (−1,1), and thus further constraints may be imposed; for example, ri ← sign(m

[Figure 49]

i 1

i 1

mi0)min{|m

mi0|,0.99};

[Figure 50]

[Figure 51]

- • Step 2: Average: r ← g1 gi=1 ri

[Figure 52]

- • Step 3: Reconstruct the regularized Ai(∀i):

  

  

i−1

1 r ··· rd

Aˇ i ←

. . . rd

i−1 rd

i−2 ··· 1

Ai ← Aˇ i/ A ˇ i F

The parameter-averaging strategy has been widely used in artiﬁcial neural networks and the machine learning communities to overcome overﬁtting.

Experiments showed these regularization strategies helped further improve the algorithm’s performance. In fact, using the Theorem 1 in [19] it can be proved that in noiseless situations the regularization strategies to Ai and B do not affect the global minimum of the cost function of our algorithm, in the sense that the global minimum corresponds to the true sparse solution. This implies that a good regularization strategy can signiﬁcantly enhance global convergence of our algorithm.

Up to now we have derived the updating rules for X, {Ai}i, {γi}i and λ in the spatially whitened model and the updating rules for B in the temporally whitened model. Combining these updating rules we obtain the EM-based spatiotemporal sparse Bayesian learning algorithm, denoted by STSBL-EM.

IV. PRACTICAL CONSIDERATIONS WHEN APPLYING STSBL-EM

The proposed STSBL-EM algorithm has wide applications. This section discusses some practical considerations when applying it in practice.

In CS of multichannel physiological signals, if the channel signal X·l has strong temporal correlation 9 in the time domain, using the original spatiotemporal model (7) can achieve good recovery performance. A typical signal is ECG signals [6].

When each channel signal X·l does not have strong temporal correlation, exploiting the temporal correlation may not be very beneﬁcial. Thus one can alternatively exploit the sparsity of each channel signal in some transformed domain by using a dictionary matrix in STSBL-EM, as stated in Section I. In particular, one can ﬁrst apply the algorithm to the following model

Y = ΩZ + V (32)

to ﬁnd the solution Z, where Ω ΦD, and D is a dictionary matrix under which X·l(∀l) has sparse representation Z·l. Then one can obtain the original solution by computing X = DZ. Note that in this method Z·l is sparser than X·l, but generally has less correlation than the latter, or the correlation

9Here ‘strong temporal correlation’ means that if modeling the signal by an AR(1) process, the absolute value of the AR coefﬁcient is very large.

structure in Z·l is not well captured by STSBL-EM. Hence, this method mainly exploits each channel signal’s sparsity in a transformed domain instead of exploiting the channel signal’s temporal correlation 10. This method can yield better results than using the original model (7), if each channel signal has no strong temporal correlation. A typical signal is EEG signals [7].

In the following experiments on EEG signals we will adopt the model (32) with the dictionary matrix D formed by the orthogonal DCT bases 11. Due to the “energy compaction” property of DCT, for the l-th channel signal X·l, the DCT coefﬁcients with signiﬁcantly nonzero values are concentrated in the ﬁrst K entries in Z·l. Note that the ﬁrst K nonzero entries (with other coefﬁcients with insigniﬁcantly nonzero values locating at the (K + 1)-th entry, the (K + 2)-th entry, etc.) can be viewed as concatenation of a number of nonzero blocks. In this sense, the value of K does not need to be known a priori, and the block partition in STSBL-EM can be set rather arbitrarily. In our experiments we found STSBL-EM showed stable performance when the block partition di(∀i) chose values from a wide range (15 to 60). (Similar robustness was also observed on BSBL [6].) Thus we simply set di = 16(∀i).

In practice most SBL algorithms implicitly adopt a γipruning mechanism [15], [19], [29]. The mechanism sets a small γi to zero if it is smaller than a threshold, thus speeding up convergence and encouraging solutions to be sparse in the level of entries [29], blocks [15], or rows [19]. However, for raw EEG signals (especially those recorded during ambulatory monitoring) the value of K/M could be very large [20]. Thus the DCT coefﬁcient vectors are not sparse. In this case, better recovery performance can be achieved by setting the γi-pruning threshold to a very small value or even zero and allowing algorithms to iterate only a few times [6], [7]. In our experiments we set this threshold to zero, and terminated the algorithm when the iteration number reached 40 or the maximum change in any entry of the estimated X in two successive iterations was smaller than 10−6. But when used in other applications such as source localization, it may need hundreds of iterations to converge.

In our work the problem of data compression is modeled as a noiseless CS problem (i.e., the sensor noise V is ignored). Therefore, in our experiments STSBL-EM was performed in the noiseless situation with the parameter λ set to λ = 10−10. But this does not mean that artifacts and noise in raw physiological signals are ignored. In fact, in our model X·l is a raw physiological signal contaminated by noise and artifacts.

V. APPLICATION

The proposed STSBL-EM was used for CS of multichannel EEG signals in SSVEP-based BCI and EEG-based driver’s drowsiness estimation.

10Note that when using some dictionary matrices such as wavelet dictionar-

ies, one may exploit both sparsity and wavelet tree structures in Z·l, which is more beneﬁcial than merely exploiting the sparsity [27], [28].

11One may ﬁnd other dictionary matrices which can yield better results than the DCT dictionary matrix on EEG signals [12]. But seeking the optimal dictionary matrix is not the focus of this work.

To show the superior performance of STSBL-EM, we chose the BSBL-BO algorithm, an MMV-model-based CS algorithm, and an SMV-model-based CS algorithm for comparison. We did not choose many algorithms for comparison, since in [6] it has been shown that ten state-of-the-art CS algorithms were inferior to BSBL-BO. Thus, our focus was the comparison between STSBL-EM and BSBL-BO. The three algorithms are brieﬂy described as follows.

- • BSBL-BO [15] 12. To the best of our knowledge, it may be the only algorithm that has the ability to recover both non-sparse physiological signals [6] and the physiological signals with non-sparse representation coefﬁcients [7]. Its block partition was set to d1 = d2 = ··· = 16.
- • ISL0 [30] 13. It is based on the MMV model. When Z is less row-sparse, it has robust performance than many MMV-model-based algorithms.
- • Basis Pursuit (BP) [31] 14. It is a classic CS algorithm based on the SMV model. Some work [12] claimed that it was more suitable for CS of EEG than other classic CS algorithms. We used the SPGL1 software [32] to implement this algorithm.

All the algorithms recovered signals in the transformed domain. The dictionary matrix D was the DCT dictionary matrix. For all algorithms, the measurement matrix Φ was an N × M sparse binary matrix of full row-rank, where M was ﬁxed to 256 and N was varied to meet a desired compression ratio (CR). The CR was deﬁned as

M − N M

× 100. (33)

CR =

[Figure 53]

Irrespective of CR values, each column of the measurement matrix Φ contained only two entries of 1’s with random locations, while other entries were zeros.

Mean square error (MSE) is often used for measuring recovery quality. However, it is shown [33] that MSE is not a reasonable measure for natural signals. Thus it is not suitable for EEG, especially raw EEG signals contaminated by strong noise and artifacts. A smaller MSE does not necessarily mean that a desired task (e.g. EEG classiﬁcation) on the recovered EEG signals can be better accomplished. Therefore, we used a task-oriented performance evaluation method, which was initially suggested in [6], [7].

The main idea of this evaluation method is that a practical task is ﬁrst performed on an original dataset, and then the same task (using the same algorithm with the same initialization) is performed on the recovered dataset, and ﬁnally the results of the two tasks are compared. If the results are the same, this means that the recovered dataset has high ﬁdelity and does not affect the practical task. If the results are far from each other, this means that the recovered dataset is seriously distorted.

Using this idea, in our BCI experiment we compared the classiﬁcation rate on original EEG signals to the classiﬁcation

- 12The Matlab code was downloaded at

https://sites.google.com/site/researchbyzhang/bsbl.

- 13The Matlab code was provided by the ﬁrst author of [30] via private

communication.

- 14The Matlab code was downloaded at

http://www.cs.ubc.ca/˜mpf/spgl1/.

rate on recovered signals. In the experiment on drowsiness estimation, we compared the estimation result using original signals to the estimation result using recovered signals. All the comparisons were repeated with different CR values.

Experiments were carried out on a computer with dual-core 2.8 GHz CPU and 6.0 GiB RAM.

A. SSVEP-Based BCI

In neurology, SSVEP is a response to a visual stimulus modulated at a speciﬁc frequency. The response has a fundamental frequency and several harmonics. The fundamental frequency is the same as that of the visual stimulus. This characteristic has been widely used in BCI [34] to classify stimuli with different frequencies, thereby ﬁnishing some control tasks. A trend in BCI is to develop wearable wireless systems [35], [36]. In such systems developing energy-efﬁcient data acquisition modules is highly desired.

In this experiment the dataset analyzed in [35] was used 15. The dataset was recorded from twelve subjects. We chose the recordings of ‘Subject 1’ for illustration, which corresponded to visual stimuli of 9Hz, 10Hz, 11Hz, 12Hz, and 13Hz. Each stimulus ﬂashed for 4 seconds. The data sampling rate was 256 Hz. The monitor refresh rate was 75Hz. As in [35], canonical correlation analysis (CCA) was used as the classiﬁer. The selected channel indexes were 129, 133, 193, 196, 199, 200, 203, and 210 (all in the occipital area). Detailed descriptions on the dataset, the experiment equipment, and the recording procedure can be found in [35].

The signals were compressed and then recovered by STSBL-EM, BSBL-BO, ISL0, and BP, respectively. CR ranged from 50 to 90. The recovered signals were bandpassﬁltered between 8-35 Hz. Each 8-channel epoch which corresponded to a visual stimulus was classiﬁed by CCA. The classiﬁcation rate was calculated by averaging over all classiﬁcation results on the whole recovered signals. The same bandpass ﬁltering and classiﬁcation were performed on the original signals.

The classiﬁcation rates of all algorithms are given in Table I. Note that the classiﬁcation rate on the original signals was 1.00. We can see that when CR ≤ 60, the classiﬁcation rate on the recovered signals by STSBL-EM was also 1.00. Even if CR = 80, the classiﬁcation rate was very close to 1.00. These results imply that when the signals were compressed by 80%, the recovered signals by our algorithm were still of good quality. In contrast, all the compared algorithms did not recover the signals with satisfactory quality even with CR = 60.

To visually examine the data recovery quality, we randomly chose a time slot which corresponded to a visual stimulus of 10 Hz (duration was 4 seconds). Then we picked signals during this time slot in each channel from the original signals, and averaged their power spectrum densities (PSD’s), shown in Fig. 1(a). We can clearly see the fundamental frequency (10 Hz) and the harmonic frequency (20 Hz). Similarly, we calculated the averaged PSD from the recovered signals by STSBL-EM when CR = 80, shown in Fig. 1(b), and the

15The dataset was downloaded at ftp://sccn.ucsd.edu/pub/SSVEP.

TABLE I CLASSIFICATION RATES OF ALL ALGORITHMS WHEN CR VARIED FROM 50 TO 90. THE CLASSIFICATION RATE ON THE ORIGINAL SIGNALS WAS 1.00.

[Figure 54]

CR 50 60 70 80 85 90

[Figure 55]

STSBL-EM 1.00 1.00 0.984 0.984 0.976 0.672 BSBL-BO 0.992 0.976 0.952 0.864 0.824 0.576

[Figure 56]

[Figure 57]

ISL0 0.888 0.840 0.800 0.704 0.536 0.488 Basis Pursuit 0.944 0.920 0.856 0.728 0.600 0.528

[Figure 58]

[Figure 59]

### Averaged PSD of Original EEG

100

##### (a)

5 10 15 20 25 30 35

Averaged PSD of EEG Recovered by STSBL−EM

100

##### (b)

5 10 15 20 25 30 35

Averaged PSD of EEG Recovered by BSBL−BO

100

##### (c)

5 10 15 20 25 30 35

Frequency (Hz)

Fig. 1. (a) Averaged PSD of signals from the original signals, which corresponded to a visual stimulus of 10 Hz. (b) Averaged PSD of signals from the signals recovered by STSBL-EM when CR = 80. (c) Averaged PSD of signals from the signals recovered by BSBL-BO when CR = 80. Arrows indicate the fundamental frequency (10 Hz). Circles indicate the harmonic frequency (20 Hz).

averaged PSD from the recovered signals by BSBL-BO when CR = 80, shown in Fig. 1(c). We can see both the fundamental frequency and the harmonic frequency in Fig. 1(b). But we do not see the harmonic frequency in Fig. 1(c). This explains why the classiﬁcation rate on the signals recovered by BSBL-BO was lower than the classiﬁcation rate on the signals recovered by STSBL-EM, since CCA exploited both the fundamental frequency and the harmonic frequency for classiﬁcation.

Maintaining harmonic frequencies on recovered signals implies subtle waveforms in original signals are recovered. Therefore, the results shown in Fig. 1 further conﬁrms that STSBL-EM has better data recovery quality than BSBL-BO.

Fig. 2 shows the averaged consumed time of each algorithm in recovering 8-channel signals of 1 second duration at different CR values. STSBL-EM was much faster than BSBLBO. Their speed gap will be more signiﬁcant in the next application, in which the number of EEG channels was 30.

B. EEG-Based Driver’s Drowsiness Estimation

EEG-based driver’s drowsiness estimation and prediction is an emerging technology for driving safety [37]–[39] and an important application of EEG. Such systems are powered by batteries and are generally embedded in a wearable device such as an ordinary hat. Thus it is highly desired to develop

0.7

|STSBL−EM<br><br>BSBL−BO<br><br>ISL0<br><br>Basis Pursuit<br><br>|
|---|

0.6

## ConsumedTime(s.)

0.5

0.4

0.3

0.2

0.1

0

50 60 70 80 90

Compression Ratio (CR)

Fig. 2. Comparison of consumed time in recovery of 8-channel signals of 1 second duration at different CR. Only when the consumed time of an algorithm is far less than 1 second, can it be used for real-time (or near real-time) systems.

wireless EEG systems with low energy consumption [38]. In the following we will show that the proposed algorithm can be used in this application for energy efﬁcient data transmission.

A set of EEG signals used in [38] were used in this experiment. The data were recorded from a subject using a 30channel EEG system, when the subject was driving with some degree of drowsiness in a realistic kinesthetic virtual-reality driving simulator. The sampling rate was 250 Hz. During the driving, the deviation between the center of the vehicle and the center of the cruising lane was recorded, which was viewed as a driving error. The driving error is known to be a good indicator to drowsiness level [38], [39]. Details on the recording system, the recording procedure, and the virtualreality driving simulator are given in [38].

Many methods were proposed to estimate the drowsiness level from recorded EEG signals. One method is given in [38], [39]:

- • Use lowpass ﬁlter with a cut-off frequency of 50 Hz to remove power line noise and other high-frequency noise from raw EEG signals.
- • Perform online independent component analysis (ICA) [40] on the signals, and select an independent component (IC) for further analysis.
- • Calculate log PSD of the selected IC at a frequency every 2 seconds. The time-varying subband log PSD is then used as the drowsiness estimate 16.

To evaluate the quality of the drowsiness estimate, the Pearson correlation between the driving error (an indicator to the drowsiness level) and the time-varying subband log PSD of the selected IC is often evaluated. High Pearson correlation indicates a good drowsiness estimate. Details of the method can be found in [39].

Since our goal is to show that the proposed algorithm can be used in this application, we need to investigate whether the drowsiness estimation accuracy is degraded when using the

16For more robust estimation, one can seek an optimal mapping from the log PSD to the driving error using a training set. Since our goal in this experiment was to show the data recovery quality of the proposed algorithm, we just simply treated the time-varying log PSD as the drowsiness estimate.

100

|Driving Error|
|---|

- (a)

- 2.5

- 3

- (b)

- 2.5

- 3

- (c)

- 2.5

- 3

- (d)

- 2.5

- 3

- (e)

500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000

- 2.5

- 3

- (f)

50

0

|Corr: 0.878|
|---|

|Corr: 0.882|
|---|

|Corr: 0.873|
|---|

|Corr: 0.903|
|---|

|Corr: 0.870|
|---|

Time (seconds)

Fig. 3. Comparison of the driving error, the log PSD of IC0 at f = 5 Hz, and the log PSD of ICrec at f = 5 Hz and at different CR values. ICrec was obtained from recovered signals by STSBL-EM which had the highest correlation with IC0. (a) The driving error. (b) The log PSD of IC0 at f = 5 Hz. (c)-(f) are the log PSD of ICrec at f = 5 Hz when CR = 50, 60, 70, and 80, respectively. Their Pearson correlations with the driving error are shown in each subplot.

recovered signals. Thus, we compared the drowsiness estimate from the recovered signals to the one from the original signals. Particularly, we adopted the following procedure:

- 1) Repeat the above drowsiness estimation using the orig-

inal signals by selecting an IC (denoted by IC0) and a frequency f. Evaluate the Pearson correlation between the driving error and the time-varying log PSD of IC0 at the frequency f. Denote the correlation by r0.

- 2) Perform the same ICA decomposition on the recovered signals, and choose the IC which has the highest Pearson correlation with IC0. Denote the IC by ICrec.
- 3) Calculate the time-varying log PSD of ICrec at the frequency f.
- 4) Evaluate the Pearson correlation between the driving error and the time-varying log PSD calculated in the above step. Denote the Pearson correlation by rrec.
- 5) Compare rrec to r0.

In our experiment, IC0 was the IC whose log PSD at f = 5 (Hz) had the highest correlation with the driving error.

Fig. 3 shows the driving error signal, the time-varying log PSD of IC0 at f = 5 Hz, and the time-varying log PSD of ICrec at f = 5 Hz at different CR values. ICrec was obtained from recovered signals by STSBL-EM. The r0 and the rrec at different CR values are also given in corresponding subplots. Clearly, when CR was no more than 80, the drowsiness estimate from the recovered signals by STSBL-EM was almost the same as the one from the original signals.

Table II further shows the r0 and the rrec’s of all algorithms

- 0

- 0.5
- 1

- 1.5
- 2

||STSBL−EM<br><br>BSBL−BO<br><br>ISL0<br><br>Basis Pursuit<br><br>|
|---|
|
|---|

## ConsumedTime(s.)

50 60 70 80

Compression Ratio (CR)

Fig. 4. Averaged consumed time of all algorithms in recovery of the 30channel signals of 1.024 second duration at different CR values. BSBL-BO was slow, because it had to recover these signals channel by channel.

when f = 4,5,6,7 (Hz) and CR varied from 50 to 80. We can see when CR was small (e.g. 50-60), all the algorithms recovered the signals well. Their drowsiness estimates were almost the same as the estimate from the original signals. However, when CR increased, only STSBL-EM ensured accurate drowsiness estimation; particularly, the drowsiness estimate was almost not affected even if the raw EEG signals were compressed by 80%.

Fig. 4 shows the averaged consumed time of all algorithms in recovery of the 30-channel signals of 1.024 second duration at different CR values. STSBL-EM was much faster than BSBL-BO, suggesting that it is more suitable for real-time applications especially when the channel number is very large.

It is worth pointing out that the raw EEG signals contained strong artifacts due to muscle movement. However, the proposed algorithm did not require any preprocessing before data compression.

VI. DISCUSSIONS A. Energy Consumption

We have mentioned that the proposed algorithm compresses data with ultra-low energy consumption. This is due to the use of the simplest measurement matrix and the algorithm’s powerful data recovery ability.

The measurement matrix Φ is a very simple sparse binary matrix. Its each column contains only two entries of 1’s, while other entries are zeros. Using this matrix has two major beneﬁts,

- • Code execution in data compression is largely reduced. Consequently, the energy dissipated in code execution is very low.
- • Using this measurement matrix largely simpliﬁes circuit design. Therefore the cost and the size of chips can be reduced.

It is worth noting that such a measurement matrix is not suitable for any CS algorithms. Some algorithms may have seriously degraded performance when using the measurement matrix.

TABLE II COMPARISON BETWEEN r0 CALCULATED FROM THE ORIGINAL SIGNALS AND rrec CALCULATED FROM RECOVERED SIGNALS BY ALL ALGORITHMS AT 4-7 HZ AND DIFFERENT CR VALUES. ‘–’ MEANS THE ICA DECOMPOSITION ON THE RECOVERED SIGNALS BY THE CORRESPONDING ALGORITHM DID NOT YIELD THE DESIRED IC.

[Figure 60]

4Hz 5Hz

[Figure 61]

[Figure 62]

CR 50 60 70 80 50 60 70 80 Original Data 0.853 0.878

[Figure 63]

STSBL-EM 0.853 0.842 0.866 0.848 0.882 0.873 0.903 0.870 BSBL-BO 0.853 0.841 0.841 0.793 0.880 0.875 0.874 0.776

ISL0 0.851 0.735 - - 0.885 0.776 - Basis Pursuit 0.839 0.842 0.824 0.780 0.873 0.854 0.840 0.795

[Figure 64]

6Hz 7Hz

[Figure 65]

[Figure 66]

CR 50 60 70 80 50 60 70 80 Original Data 0.881 0.807

[Figure 67]

STSBL-EM 0.879 0.870 0.896 0.867 0.809 0.771 0.849 0.808 BSBL-BO 0.873 0.871 0.882 0.733 0.788 0.801 0.802 0.526

ISL0 0.874 0.783 - - 0.806 0.654 - Basis Pursuit 0.867 0.842 0.808 0.766 0.779 0.753 0.728 0.584

[Figure 68]

Besides, many CS algorithms require preprocessing on raw data before compression, such as dynamic thresholding, ﬁltering, and seeking speciﬁc waveform features. These preprocessing consumes lots of energy 17. In contrast, our proposed algorithm does not require these preprocessing steps.

On the other hand, our algorithm’s powerful recovery ability ensures high recovery performance when the compression ratio is high (e.g. CR=80). Thus, the energy dissipated in wireless transmission can also be largely reduced.

In [9], [10] the compression procedure of BSBL-BO was analyzed. These works showed that BSBL-BO, compared to conventional data compression procedures, dissipated only about 10% to 20% energy, shortened compression time by more than 90%, and largely saved other computational resources. Since the compression procedures of BSBL and STSBL-EM are the same, these analysis results are applicable to STSBL-EM. But it is worth noting that STSBL-EM has more powerful recovery ability than BSBL-BO.

B. Stable Speed Regardless of Channel Numbers

Comparing Fig. 4 with Fig. 2 we ﬁnd that the consumed time of STSBL-EM was relatively stable, although the channel number in Fig. 4 was almost four times of the channel number in Fig. 2. The reason is that to recover multichannel physiological signals, the algorithmic complexity of STSBLEM mainly depends on the computation of (19) and (20), which is totally O(M3+2M2N+MN2+MNL+N3). When L is small compared to M 18, the algorithmic complexity is approximately O(M3 + 2M2N), which does not depends on L. Thus the consumed time of STSBL-EM does not change signiﬁcantly when the channel number dramatically changes. Note that when recovering a single-channel signal,

- 17It is highly doubted that if using such preprocessing, CS still has its

energy-saving advantages over traditional data compression algorithms.

- 18In a typical scenario of telemonitoring of multichannel physiological

signals, L varies from two to dozens, while M varies from 200 to 1000.

the algorithmic complexity of BSBL-BO is also dominated by O(M3 +2M2N). But when recovering L-channel signals, its computation load increases L-fold, since it has to recover the signals channel by channel. This explains why the consumed time by BSBL-BO in Fig. 4 was roughly four times the consumed time in Fig. 2.

C. Exploitation of Inter-Channel Correlation

Jointly recovering multichannel biosignals have been studied in a number of works. However, these works were generally based on the MMV model. They only exploited common sparsity proﬁles among channel signals, but did not exploit the inter-channel correlation. It is shown [19] that if ignoring the correlation, most MMV-model based CS algorithms will have degraded recovery performance, especially in the presence of high inter-channel correlation. In the two EEG datasets used in our experiments, the inter-channel correlation between Z·,i and Z·,j is very high, generally above 0.9 (when |i − j| ≤ 5). Thus it is not difﬁcult to understand why ISL0 had poor performance in the experiments. In fact, in the two experiments if STSBL-EM was performed without exploiting the interchannel correlation (i.e. setting B = I), the BCI classiﬁcation rate and the drowsiness estimation were very poor, even poorer than those by BSBL-BO.

Therefore, exploiting the inter-channel correlation is necessary in CS of multichannel signals; ignoring it can seriously deteriorate CS algorithms’ performance. This also indicates the importance of our work in developing the STSBL-EM algorithm which can exploit the correlation.

VII. CONCLUSIONS

We proposed a spatiotemporal sparse Bayesian learning algorithm for energy-efﬁcient compressed sensing of multichannel signals. In contrast to existing compressed sensing algorithms, it not only exploits correlation structures within

a single channel signal, but also exploits inter-channel correlation. It has much better recovery performance than stateof-the-art algorithms. Its speed is relatively stable even when the channel number signiﬁcantly changes. Experiments on SSVEP-based BCI and EEG-based driver’s drowsiness estimation showed that when using the proposed algorithm, the BCI classiﬁcation rate and the drowsiness estimation on recovered signals were almost the same as those on original signals, even when the signals were compressed by 80%.

Since the algorithm takes root in Bayesian basis selection, it can be used in many other applications, such as feature selection, source localization, and sparse representation.

REFERENCES

- [1] E. Cande`s and M. Wakin, “An introduction to compressive sampling,” IEEE Signal Processing Magazine, vol. 25, no. 2, pp. 21–30, 2008.
- [2] S. Aviyente, “Compressed sensing framework for EEG compression,” in Statistical Signal Processing, 2007. SSP’07. IEEE/SP 14th Workshop on, 2007, pp. 181–184.
- [3] E. C. Pinheiro, O. A. Postolache, and P. S. Girao, “Implementation of compressed sensing in telecardiology sensor networks,” International Journal of Telemedicine and Applications, vol. 2010, 2010.
- [4] A. M. Dixon, E. G. Allstot, D. Gangopadhyay, and D. J. Allstot, “Compressed sensing system considerations for ECG and EMG wireless biosensors,” IEEE Trans. on Biomedical Circuits and Systems, vol. 6, no. 2, pp. 156–166, 2012.
- [5] F. Chen, A. Chandrakasan, and V. Stojanovic, “Design and analysis of a hardware-efﬁcient compressed sensing architecture for data compression in wireless sensors,” IEEE Journal of Solid-State Circuits, vol. 47, no. 3, pp. 744–756, 2012.
- [6] Z. Zhang, T.-P. Jung, S. Makeig, and B. D. Rao, “Compressed sensing for energy-efﬁcient wireless telemonitoring of noninvasive fetal ECG via block sparse Bayesian learning,” IEEE Trans. on Biomedical Engineering, vol. 60, no. 2, pp. 300–309, 2013.
- [7] ——, “Compressed sensing of EEG for wireless telemonitoring with low energy consumption and inexpensive hardware,” IEEE Trans. on Biomedical Engineering, vol. 60, no. 1, pp. 221–224, 2013.
- [8] H. Mamaghanian, N. Khaled, D. Atienza, and P. Vandergheynst, “Compressed sensing for real-time energy-efﬁcient ECG compression on wireless body sensor nodes,” IEEE Transactions on Biomedical Engineering, vol. 58, no. 9, pp. 2456–2466, 2011.
- [9] B. Liu, Z. Zhang, G. Xu, H. Fan, and Q. Fu, “Energy efﬁcient telemonitoring of physiological signals via compressed sensing: A fast algorithm and power consumption evaluation,” Biomedical Signal Processing and Control, vol. 11, pp. 80–88, 2014.
- [10] S. Fauvel and R. K. Ward, “An energy efﬁcient compressed sensing framework for the compression of electroencephalogram signals,” Sensors, vol. 14, no. 1, pp. 1474–1496, 2014.
- [11] K. Kreutz-Delgado, J. F. Murray, B. D. Rao, K. Engan, T.-W. Lee, and T. J. Sejnowski, “Dictionary learning algorithms for sparse representation,” Neural computation, vol. 15, no. 2, pp. 349–396, 2003.
- [12] A. M. Abdulghani, A. J. Casson, and E. Rodriguez-Villegas, “Compressive sensing scalp EEG signals: implementations and practical performance,” Medical and Biological Engineering and Computing, vol. 50, no. 11, pp. 1137–1145, 2012.
- [13] M. Mohsina and A. Majumdar, “Gabor based analysis prior formulation for EEG signal reconstruction,” Biomedical Signal Processing and Control, vol. 8, no. 6, pp. 951–955, 2013.
- [14] J. K. Pant and S. Krishnan, “Compressive sensing of electrocardiogram signals by promoting sparsity on the second-order difference and by using dictionary learning,” IEEE Transactions on Biomedical Circuits and Systems, 2014.
- [15] Z. Zhang and B. D. Rao, “Extension of SBL algorithms for the recovery of block sparse signals with intra-block correlation,” IEEE Trans. on Signal Processing, vol. 61, no. 8, pp. 2009–2015, 2013.
- [16] S. F. Cotter, B. D. Rao, K. Engan, and K. Kreutz-Delgado, “Sparse solutions to linear inverse problems with multiple measurement vectors,” IEEE Trans. on Signal Processing, vol. 53, no. 7, pp. 2477–2488, 2005.
- [17] Y. Eldar and H. Rauhut, “Average case analysis of multichannel sparse recovery using convex relaxation,” IEEE Transactions on Information Theory, vol. 56, no. 1, pp. 505–519, 2010.

- [18] L. F. Polania, R. E. Carrillo, M. Blanco-Velasco, and K. E. Barner, “Compressed sensing based method for ECG compression,” in Acoustics, Speech and Signal Processing (ICASSP), 2011 IEEE International Conference on, 2011, pp. 761–764.
- [19] Z. Zhang and B. D. Rao, “Sparse signal recovery with temporally correlated source vectors using sparse Bayesian learning,” IEEE Journal of Selected Topics in Signal Processing, vol. 5, no. 5, pp. 912–926, 2011.
- [20] Z. Zhang, B. D. Rao, and T.-P. Jung, “Compressed sensing for energyefﬁcient wireless telemonitoring: Challenges and opportunities,” in Asilomar Conference on Signals, Systems, and Computers (Asilomar 2013), 2013.
- [21] A. Milenkovic, C. Otto, and E. Jovanov, “Wireless sensor networks for personal health monitoring: Issues and an implementation,” Computer communications, vol. 29, no. 13-14, pp. 2521–2533, 2006.
- [22] T. Martin, E. Jovanov, and D. Raskovic, “Issues in wearable computing for medical monitoring applications: a case study of a wearable ECG monitoring device,” in Wearable Computers, The Fourth International Symposium on, 2000, pp. 43–49.
- [23] P. Brown, M. Vannucci, and T. Fearn, “Multivariate Bayesian variable selection and prediction,” Journal of the Royal Statistical Society: Series B (Statistical Methodology), vol. 60, no. 3, pp. 627–641, 1998.
- [24] J. Wan, Z. Zhang, B. Rao, S. Fang, J. Yan, A. Saykin, and L. Shen, “Identifying the neuroanatomical basis of cognitive impairment in Alzheimer’s disease by correlation-and nonlinearity-aware sparse Bayesian learning.” IEEE Transactions on medical imaging, DOI: 10.1109/TMI.2014.2314712.
- [25] M. Tipping, A. Faul et al., “Fast marginal likelihood maximisation for sparse Bayesian models,” in Proceedings of the ninth international workshop on artiﬁcial intelligence and statistics, vol. 1, no. 3, 2003.
- [26] D. Shutin, T. Buchgraber, S. Kulkarni, and H. Poor, “Fast variational sparse Bayesian learning with automatic relevance determination for superimposed signals,” Signal Processing, IEEE Transactions on, vol. 59, no. 12, pp. 6257–6261, 2011.
- [27] L. He and L. Carin, “Exploiting structure in wavelet-based bayesian compressive sensing,” Signal Processing, IEEE Transactions on, vol. 57, no. 9, pp. 3488–3497, 2009.
- [28] C. Chen, Y. Li, and J. Huang, “Forest sparsity for multi-channel compressive sensing,” IEEE Transactions on Signal Processing, 2014.
- [29] M. Tipping, “Sparse Bayesian learning and the relevance vector machine,” The Journal of Machine Learning Research, vol. 1, pp. 211–244, 2001.
- [30] M. M. Hyder and K. Mahata, “A robust algorithm for joint-sparse recovery,” IEEE Signal Processing Letters, vol. 16, no. 12, pp. 1091– 1094, 2009.
- [31] S. S. Chen, D. L. Donoho, and M. A. Saunders, “Atomic decomposition by basis pursuit,” SIAM J. Sci. Comput., vol. 20, no. 1, pp. 33–61, 1998.
- [32] E. Van Den Berg and M. Friedlander, “Probing the pareto frontier for basis pursuit solutions,” SIAM Journal on Scientiﬁc Computing, vol. 31, no. 2, pp. 890–912, 2008.
- [33] Z. Wang and A. C. Bovik, “Mean squared error: love it or leave it? a new look at signal ﬁdelity measures,” IEEE Signal Processing Magazine, vol. 26, no. 1, pp. 98–117, 2009.
- [34] Y. Wang, X. Gao, B. Hong, C. Jia, and S. Gao, “Brain-computer interfaces based on visual evoked potentials,” IEEE Engineering in Medicine and Biology Magazine, vol. 27, no. 5, pp. 64–71, 2008.
- [35] Y. M. Chi, Y.-T. Wang, Y. Wang, C. Maier, T.-P. Jung, and G. Cauwenberghs, “Dry and noncontact EEG sensors for mobile brain–computer interfaces,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 20, no. 2, pp. 228–235, 2012.
- [36] L.-D. Liao, C.-Y. Chen, I.-J. Wang, S.-F. Chen, S.-Y. Li, B.-W. Chen, J.Y. Chang, and C.-T. Lin, “Gaming control using a wearable and wireless EEG-based brain-computer interface device with novel dry foam-based sensors,” Journal of neuroengineering and rehabilitation, vol. 9, no. 1, p. 5, 2012.
- [37] T.-P. Jung, S. Makeig, M. Stensmo, and T. J. Sejnowski, “Estimating alertness from the EEG power spectrum,” Biomedical Engineering, IEEE Transactions on, vol. 44, no. 1, pp. 60–69, 1997.
- [38] C. Lin, L. Ko, J. Chiou, J. Duann, R. Huang, S. Liang, T. Chiu, and T. Jung, “Noninvasive neural prostheses using mobile and wireless EEG,” Proceedings of the IEEE, vol. 96, no. 7, pp. 1167–1183, 2008.
- [39] C.-T. Lin, R.-C. Wu, S.-F. Liang, W.-H. Chao, Y.-J. Chen, and T.-P. Jung, “EEG-based drowsiness estimation for safety driving using independent component analysis,” Circuits and Systems I: Regular Papers, IEEE Transactions on, vol. 52, no. 12, pp. 2726–2738, 2005.
- [40] T.-W. Lee, M. Girolami, and T. J. Sejnowski, “Independent component analysis using an extended infomax algorithm for mixed subgaussian and

supergaussian sources,” Neural computation, vol. 11, no. 2, pp. 417–441, 1999.

Zhilin Zhang received the Ph.D. degree in electrical engineering from University of California at San Diego in 2012. He is currently a senior research engineer in the Emerging Technology Lab in Samsung Research America – Dallas.

[Figure 69]

His research interests include sparse Bayesian learning, sparse signal recovery, signal separation and decomposition, machine learning, and their applications to biomedicine, healthcare, and smarthome. He has authored or coauthored about 40 peerreviewed journal and conference papers.

He is a technical committee member in Bio-Imaging and Signal Processing of the IEEE Signal Processing Society (from January 2014 to December 2016), and a technical program committee member of a number of international conferences.

He received Excellent Master Thesis Award in 2005, Second Prize in College Student Entrepreneur Competition (on fetal heart rate monitor) in 2005, and Samsung Achievement Award in 2013 and 2014.

Zhouyue Pi is a Senior Director at Samsung Research America in Dallas, Texas, where he leads the Emerging Technology Lab doing research in next generation mobile devices, smart home solutions, and mobile health technologies.

[Figure 70]

Before joining Samsung in 2006, he was with Nokia Research Center in Dallas and San Diego, where he led 3G wireless standardization and modem development for 3GPP2 1xEV-DV, 1xEV-DO, and Ultra Mobile Broadband (UMB). In 2006 – 2009, he was a leading contributor to Samsung’s

4G standardization efforts in 3GPP LTE and IEEE 802.16m, and to IEEE 802.11ad for 60 GHz communication. In 2009 – 2012, he pioneered 5G mmwave massive MIMO technology and led the development of the world’s ﬁrst baseband and RF system that demonstrated the feasibility of Gbps mobile communication at 28 GHz.

He has authored more than 30 technical journal and conference papers and is the inventor of more than 150 patents and applications. He holds a B.E. degree from Tsinghua University (with honor), a M.S. degree from the Ohio State University, and an MBA degree from Cornell University (with distinction). He is a Senior Member of IEEE.

Tzyy-Ping Jung received the B.S. degree in electronics engineering from National Chiao-Tung University, Taiwan, in 1984, and the M.S. and Ph.D. degrees in electrical engineering from The Ohio State University, Columbus, in 1989 and 1993, respectively.

[Figure 71]

He is currently a research scientist and the codirector of the Center for Advanced Neurological Engineering, Institute of Engineering in Medicine, University of California at San Diego (UCSD). He is also an associate director of the Swartz Center

for Computational Neuroscience, Institute for Neural Computation, and an adjunct professor of the Department of Bioengineering at UCSD. In addition, he is a professor of Department of Computer Science, National Chiao Tung University, Hsinchu, Taiwan.

His research interests are in the areas of biomedical signal processing, cognitive neuroscience, machine learning, time-frequency analysis of human EEG, functional neuroimaging, and brain computer interfaces and interactions.

He received the Unsupervised Learning Pioneer Award from the Society for Photo-Optical Instrumentation Engineers in 2008. He is currently an Associate Editor of IEEE Transactions on Biomedical Circuits and Systems.

Scott Makeig received the B.S. degree, “Self in Experience”, from the University of California Berkeley, Berkeley, in 1972 and the Ph.D. degree in music psychobiology from the University of California at San Diego (UCSD), La Jolla, in 1985.

[Figure 72]

After spending a year in Ahmednagar, India, as a American India Foundation Research Fellow, he became a psychobiologist at UCSD, and then a research psychologist at the Naval Health Research Center, San Diego. In 1999, he became a staff scientist at the Salk Institute, La Jolla, CA, and

moved to UCSD as a research scientist in 2002 to develop and direct the Swartz Center for Computational Neuroscience.

His research interests are in high-density electrophysiological signal processing and mobile brain/body imaging to learn more about how distributed brain activity supports human experience and behavior.

Bhaskar D. Rao received the Ph.D. degree from the University of Southern California in 1983. Since 1983, he has been with the University of California at San Diego (UCSD), where he is currently a professor with the Department of Electrical and Computer Engineering and the holder of the Ericsson endowed chair in wireless access networks.

[Figure 73]

His interests are in the areas of digital signal processing, estimation theory, and optimization theory, with applications to digital communications, speech signal processing, and human-computer interactions.

He has been a member of the Statistical Signal and Array Processing Technical Committee, the Signal Processing Theory and Methods Technical Committee, the Communications Technical Committee of the IEEE Signal Processing Society.

His work has received several paper awards. His paper received the Best Paper Award at the 2000 Speech Coding Workshop and his students have received the Best Student Paper Awards at both the 2005 and 2006 International Conference on Acoustics, Speech and Signal Processing (ICASSP), as well as the Best Student Paper Award at Neural Information Processing Systems Conference (NIPS) in 2006. A paper he co-authored with B. Song and R. Cruz received the 2008 Stephen O. Rice Prize Paper Award in the Field of Communications Systems. A paper co-authored by him and his student received the 2012 Signal Processing Society (SPS) Best Paper Award. He was elected to the IEEE Fellow in 2000 for his contributions to the statistical analysis of subspace algorithms for harmonic retrieval.

