# arXiv:2605.10111v1[cs.LG]11May2026

## CFSPMNET: CROSS-SUBJECT FOURIER-GUIDED SPATIAL-PATCH MAMBA NETWORK FOR EEG MOTOR IMAGERY DECODING IN STROKE PATIENTS

#### Xiangkai Wang1 , Yun Zhao2 , Dongyi He1,3 , Qingling Xia1 , Gen Li1,4, Xinlai Xing1, Yuchi Pan1 , and Bin Jiang1

- 1School of Artificial Intelligence, Chongqing University of Technology, Chongqing 401135, China; Chongqing Key

Laboratory of Embodied Intelligence Perception and Autonomous Learning for Humanoid Robots; Key Laboratory of Advanced Equipment Intelligence of the Chongqing Education Commission, Chongqing 401135, China

- 2School of Smart Health, Chongqing Polytechnic University of Electronic Technology, Chongqing 401131, China

3Department of Language Science and Technology, The Hong Kong Polytechnic University, Hung Hom, Hong Kong SAR, China 4School of Pharmacy and Bioengineering, Chongqing University of Technology, Chongqing 400054, China kevinwang@stu.cqut.edu.cn; zhaoyun@cqcet.edu.cn; hedongyi6438@gmail.com qingling@cqut.edu.cn; xingxinlai@cqut.edu.cn; m15938072816@163.com; jb20200132@cqut.edu.cn ligen1990@cqut.edu.cn

Corresponding authors: Yun Zhao (zhaoyun@cqcet.edu.cn) and Bin Jiang (jb20200132@cqut.edu.cn)

### ABSTRACT

Motor imagery electroencephalography (MI-EEG) decoding provides a non-invasive approach for post-stroke rehabilitation; however, its cross-patient application remains challenging due to pathological neural reorganization, which disrupts both task-related EEG dynamics and underlying aperiodic brain activity, altering local neural population excitability, cross-regional coordination, and the global trial-level state context. Consequently, source-learned MI representations become unreliable for unseen patients. To address this, this paper proposes CFSPMNet, a novel cross-patient adaptation framework for post-stroke MI-EEG decoding that explicitly models latent neural-state organization. CFSPMNet integrates a Fourier-Reorganized State Mamba Network (FRSM) with a Shared-Private Prototype Matching (SPPM) module. FRSM treats each trial as a latent physiological token sequence, performing Fourier-domain token-state reorganization to capture trial-specific population-state arrangements and leveraging the Fourier-derived context to guide Mamba state-space propagation. SPPM improves target-domain pseudo-label updating by combining semantic confidence with sharedprivate physiological consistency, effectively filtering out confident but physiologically inconsistent target predictions during adaptation. Leave-one-subject-out experiments on two stroke MI-EEG datasets demonstrate that CFSPMNet consistently outperforms representative CNN-, Transformer-, Mamba-, and adaptation-based baselines, achieving average accuracies of 68.23% on XW-Stroke and 73.33% on 2019-Stroke, with improvements of 5.63 and 8.25 percentage points over the strongest competitors, respectively. Comprehensive ablation, sensitivity, feature-alignment, pseudo-label selection, and neurophysiological visualization analyses further validate the critical contributions of Fourier-domain token-state reorganization and calibrated pseudo-label updating. These findings highlight that modeling post-stroke MI-EEG as a latent neural-state organization problem can enhance rehabilitation-oriented cross-patient BCI decoding. The implemented code is available at https://github.com/wxk1224/CFSPMNet.

Keywords Stroke rehabilitation, brain-computer interface (BCI), electroencephalography (EEG), motor imagery (MI), aperiodic EEG activity, shared-private prototype matching

### 1 Introduction

Stroke is a major neurological cause of persistent motor dysfunction, creating an ongoing need for effective rehabilitation technologies [1]. Motor imagery (MI) electroencephalography (EEG) provides a non-invasive brain-computer interface (BCI) signal for detecting motor intention when voluntary movement is weak, delayed, or unavailable [2]. By translating imagined movements into feedback commands, MI-EEG decoding can support closed-loop rehabilitation involving visual feedback, robotic assistance, or neuromodulatory interventions [3]. For clinical application, however, a rehabilitation-oriented BCI must generalize to new patients with minimal recalibration. Therefore, cross-patient post-stroke MI-EEG decoding represents a critical step toward practical neural systems and rehabilitation engineering.

Deep learning-based MI-EEG decoders have advanced this goal through several complementary approaches. CNNbased models, such as EEGNet [4], IFNet [5], and ShallowConvNet [6], extract local spatiotemporal EEG patterns. Transformer-based models, including DBConformer [7], EEGConformer [8], and MSCFormer [9], extend the modeling scope by capturing global token interactions. Additionally, SSM/Mamba-based models, represented by SlimSeiz [10], enable efficient sequence modeling through selective state propagation. Transfer and adaptation methods, such as SSTDA [11], UA-DANN [12], and SSAS [13], further reduce inter-patient variability via domain alignment or pseudolabel updating. While these studies offer valuable tools for transferable EEG decoding, cross-patient variability is still typically addressed as a distributional discrepancy or a feature representation problem. This approach is insufficient for stroke MI-EEG because the recorded signals comprise both structured task-related dynamics and aperiodic background activity, which together reflect the current organization of neural populations.

In post-stroke MI-EEG, the central challenge is more specific. The EEG trial reflects a combination of event-related neural responses, aperiodic electrophysiological activity, and population-level state transitions [14,15]. Aperiodic activity is closely associated with background cortical excitability, neural gain, and the operating point of local neural populations [16,17], while MI-related decoding also depends on how these local states are coordinated across sensorimotor regions and embedded within a global trial-level brain state. Stroke can therefore disrupt the decoding substrate at multiple levels: local population states may become less stable, cross-regional coordination may become less consistently organized, and the global state context of the trial may vary across patients. Under these conditions, the same MI category may correspond to different latent state trajectories even when the task instructions are identical. Consequently, cross-patient transfer is constrained by disrupted latent neural-state organization; local EEG noise or feature insufficiency alone cannot explain this failure.

To address this issue, this paper proposes CFSPMNet for cross-patient post-stroke MI-EEG decoding. The central concept is that each trial is first represented as a latent physiological token sequence, which is then reorganized before state-space propagation. Each token represents a compact observation of local neural population activity, while the token trajectory captures how local states interact across regions and evolve into a global trial state. The Fourier transform is employed as a token-organization operator, providing a global complex-basis perspective on this trajectory. The model projects token trajectories onto complex bases, reorganizes their amplitude-phase structure through learnable spectral mixing, and derives a trial-specific context that summarizes the periodic and aperiodic organization of the current state arrangement. This Fourier-derived context is subsequently injected into Mamba state propagation, enabling context-conditioned state-space propagation that adapts to the local, cross-regional, and global organization of each pathological trial.

CFSPMNet further enhances the reliability of target-domain pseudo-supervision. In cross-patient adaptation, relying solely on prediction confidence is insufficient for accepting target samples, as a target trial may be confidently classified despite its aperiodic background and population-state arrangement being inconsistent with the shared physiological organization of the predicted class [18]. Therefore, pseudo-label updating should be constrained by both semantic confidence and shared-private physiological consistency. In the proposed strategy, shared prototypes serve as class-level anchors representing the local-to-global MI state organization learned from source patients; private physiological signatures preserve individual target-sample state characteristics; and class-wise matching tolerance defines the acceptance boundary for pseudo-label inclusion. This calibrated pseudo-label updating reduces the risk of reinforcing confident but physiologically inconsistent target predictions during adaptation.

The main contributions of this paper are summarized as follows:

- 1. CFSPMNet is proposed for cross-patient post-stroke MI-EEG decoding by formulating pathological transfer as latent neural-state organization across aperiodic activity and local-to-global population states.
- 2. FRSM is developed as a Fourier-context-conditioned Mamba encoder to reorganize physiological tokens over complex bases and inject trial-specific Fourier context into state-space propagation.
- 3. SPPM is designed to jointly leverage semantic confidence and shared-private physiological consistency for gating pseudo-label updates and suppressing physiologically mismatched target supervision.

[Figure 1]

Figure 1: Overall framework of CFSPMNet for cross-patient post-stroke MI-EEG decoding.

The remainder of this paper is organized as follows. Section 2 presents the details of CFSPMNet. Section 3 describes the datasets, preprocessing, evaluation protocol, and implementation settings. Section 4 reports the experimental results and analysis. Section 5 concludes the paper.

### 2 Method

CFSPMNet addresses cross-patient post-stroke MI-EEG decoding by coupling Fourier-domain token-state reorganization with calibrated target-domain adaptation, as shown in Figs. 1–3. The Fourier-Reorganized State Mamba Network (FRSM) converts each EEG trial into spatial-patch physiological tokens, reorganizes their latent state arrangement over complex Fourier bases, and uses the resulting trial-specific context to condition state-space propagation. Shared-Private Prototype Matching (SPPM) constructs source-derived class prototypes in a compact private-signature space and accepts target pseudo-labels only when semantic confidence and shared-private physiological consistency are both satisfied. Training follows two stages: source-supervised initialization with prototype construction, followed by joint source supervision and SPPM-calibrated target pseudo-supervision.

#### 2.1 Problem Formulation

Given labeled source trials from multiple patients and unlabeled trials from an unseen target patient, cross-patient decoding learns a transferable function without target labels:

Ds = {(Xis,yis)}N

i=1, Dt = {Xjt}N

j=1, X ∈ RC×T, yis ∈ {1,...,K},

s

t

(1)

where C, T, and K denote channels, samples, and MI classes. In each LOSO split, one patient is held out as target and all remaining patients form the source domain. The decoder is

z = fθ(X), p(X) = softmax(gϕ(z)), yˆ = arg max

pk(X). (2)

k

Post-stroke transfer is therefore treated as latent-state adaptation: source supervision learns class-discriminative neural-state structure, and unlabeled target trials update the boundary only when their pseudo-labels are accepted into At.

[Figure 2]

Figure 2: Architecture of the Fourier-Reorganized State Mamba Network.

[Figure 3]

Figure 3: Shared-Private Prototype Matching for calibrated target pseudo-label updating.

#### 2.2 Fourier-Reorganized State Mamba Network

FRSM implements fθ(·) by converting each trial into a token trajectory, treating that trajectory as an observation of local-to-global neural-population states, and conditioning selective state propagation on its Fourier-domain organization.

The Fourier representation is used to reorganize token-state arrangement and summarize trial-specific amplitude-phase context, rather than to extract conventional band features.

#### 2.2.1 Physiological Tokenization

Given temporal branches {Tm}Mm=1, spatial mapping S(·), temporal fusion F(·), and patch projection Π(·), the initial token sequence is

Ftemp = Concat(T1(X),...,TM(X)), Femb = F(S(Ftemp)), Z(0) = PE

(3)

√

D Π(Femb) ∈ RL×D,

where L is token length and D is embedding size.

#### 2.2.2 Fourier-domain Token-State Reorganization

For the ℓ-th encoder block, token states are normalized, transformed along the token dimension, reorganized by a learnable complex mixer, sparsified, and reconstructed as

Z(ℓ) = LN(Z(ℓ)), Ω(ℓ) = rFFT(( Z(ℓ))⊤), Ω(ℓ) = SoftShrinkτ

(Mf(Ω(ℓ))) ⊙ Wf + Ω(ℓ), Zenh(ℓ) = iFFT( Ω(ℓ)) + ( Z(ℓ))⊤,

f

(4)

where τf controls sparse shrinkage and Wf denotes learnable filtering. This operation reorganizes the trial-level token-state arrangement while suppressing weak perturbations.

#### 2.2.3 Context-conditioned State Propagation

Non-overlapping masks {Mb}Bb=1 with Bb=1 Mb = 1 decompose the reorganized spectrum into complementary states and generate modulation terms:

Zb(ℓ) = iFFT( Ω(ℓ) ⊙ Mb) + ( Z(ℓ))⊤, C(ℓ) = LN H([Z1(ℓ),...,ZB(ℓ)]) + Zenh(ℓ) , S(ℓ) = σ(WsC(ℓ)), B(ℓ) = WbC(ℓ).

(5)

Here, C(ℓ) is the Fourier-derived context, S(ℓ) scales token states, and B(ℓ) provides residual bias. The Mamba branch is then conditioned by

[U(ℓ),R(ℓ)] = Split(Win Z(ℓ)),

U¯(ℓ) = U(ℓ) ⊙ (1 + S(ℓ)), R¯(ℓ) = R(ℓ) + B(ℓ), h(tℓ) = A¯(tℓ)h(t−ℓ)1 + B¯t(ℓ)u(tℓ), o(tℓ) = C¯t(ℓ)h(tℓ) + D(ℓ) ⊙ u(tℓ),

(6)

zt(ℓ,∗) = Wout(ℓ) o(tℓ) ⊙ SiLU(¯rt(ℓ)) , Z(ℓ+1) = Z(ℓ) + Drop(Z(ℓ,∗)),

where A¯(tℓ), B¯t(ℓ), and C¯t(ℓ) are input-dependent selective parameters and lower-case variables denote token-wise states. After L blocks, classification is performed by

p(X) = softmax gϕ(Flatten(LN(Z(L)))) . (7)

#### 2.3 Shared-Private Prototype Matching

SPPM improves pseudo-label reliability by separating transferable class structure from patient-specific physiological signatures. Source trials define class prototypes and matching tolerances, and a target trial is used only when its prediction is semantically confident and physiologically consistent with the predicted shared class.

- 2.3.1 Shared Prototype Memory

Let Ψ(·) be a private-signature extractor and sim(·,·) be cosine similarity. For source signatures ρsi = Ψ(Xis) with ∥ρsi∥2 = 1, SPPM builds

Ik = {i|yis = k}, ck = Norm2

1 |Ik| i∈I

k

ρsi ,

µk =

1 |Ik| i∈I

k

sim(ρsi,ck),

σk = Std{sim(ρsi,ck)}i∈Ik

, δk = max(δmin,µk − σk), C = {(ck,δk)}Kk=1.

(8)

The tolerance δk prevents target updating from being driven by confident predictions outside the source-derived physiological class envelope.

- 2.3.2 Shared-Private Pseudo-label Calibration In this work, Ψ(·) is implemented as a compact sensorimotor channel summary over fixed channel groups {Gq}Qq=1:

aj,q = Avgc∈G

q

Xj,c, dj = |aj,1 − aj,2|, ρj = Norm2([aj,1,...,aj,Q,dj]),

sj,k = sim(ρj,ck).

(9)

For target trial Xjt, classifier confidence and prototype consistency are combined as

qj = p(Xjt), yˆj = arg max

k

qj,k, rj = max

k

qj,k, uj = sj,yˆ

j

, mj = I[rj ≥ τp]I[uj ≥ δyˆ

j

],

y˜jt =

onehot(ˆyj), mj = 1, 0, mj = 0, At = {j |mj = 1}.

(10)

SPPM refreshes qj, uj, y˜jt, and At during adaptation, producing calibrated pseudo-label updating instead of confidenceonly target supervision.

2.4 Two-stage Optimization Strategy CFSPMNet is optimized in two stages. Stage I trains the encoder and classifier on labeled source trials and constructs C; Stage II recomputes target probabilities, private-signature scores, and accepted pseudo-labels, then updates

Lsrc =

1 Ns

Ns

i=1

ℓ(p(Xis),yis),

Ltgt =

1 Nt

Nt

j=1

mj ℓ p(Xjt),y˜jt ,

L = αLsrc + (1 − α)Ltgt,

(11)

where ℓ(·,·) is cross-entropy and α balances source supervision with calibrated target pseudo-supervision. This schedule stabilizes source class structure before target decision-boundary adaptation.

- 3 Experiments

- 3.1 Datasets

Before dataset-specific processing, all EEG signals were uniformly preprocessed to preserve MI-related rhythmic activity and suppress non-neural artifacts. The raw EEG was band-pass filtered between 8 and 30 Hz, downsampled

Table 1: Dataset protocols and model input specifications.

Dataset Subjects System Channels Sampling rate Trials Input samples

XW-Stroke 24 / 50 10–20 30 500 Hz 40 1000 2019-Stroke 15 / 15 10–10 63 512 Hz 80 1708

Table 2: Selected CFSPMNet hyperparameters.

Parameter XW-Stroke 2019-Stroke

Embedding size demo 30 38 Encoder depth L 2 2 Temporal filters Ft 8 8 Source loss weight α 0.98 0.95 Pseudo-label threshold τp 0.60 0.60 Fourier partition ratio rspec 0.45 0.50 Fourier sparsity threshold τf 0.01 0.01 Stage-I epochs EI 25 10

to 250 Hz, re-referenced using common average referencing, baseline corrected, and further denoised by ICA-based artifact removal.

XW-Stroke: The XW-Stroke dataset [19] was collected at Xuanwu Hospital, Capital Medical University. The original dataset contains EEG recordings from 50 acute ischemic stroke patients, including 39 males and 11 females. All subjects performed left-hand and right-hand MI tasks, and EEG was recorded with 30 channels under the international 10–20 system at 500 Hz. To reduce patient-level heterogeneity that was not directly aligned with the cross-subject decoding objective, a clinically defined patient subcohort was further selected according to predefined inclusion criteria: right-handedness, first-ever stroke, NIHSS score below 10, and disease duration below 10 years. These criteria were determined solely by clinical attributes and were applied before model development, independent of training behavior, classification accuracy, or any other experimental outcome. The final cohort included 24 patients, indexed as 2, 5, 8, 9, 11, 12, 14, 17, 21, 23, 24, 26, 27, 28, 30, 32, 33, 37, 38, 43, 44, 47, 49, and 50.

2019-Stroke: The 2019-Stroke dataset was released by Jia et al. [20]. It contains EEG recordings from 15 stroke patients, each performing left-hand and right-hand MI tasks, with both paretic-side and non-paretic-side imagination included in the original acquisition setting. EEG was recorded with 63 channels under the international 10–10 system at 512 Hz. All publicly available subjects were used without additional subject-level exclusion.

#### 3.2 Implementation Details and Hyperparameter Settings

The proposed framework was developed using PyTorch in a Python 3.12 environment. Optimization was performed with Adam, where both the initial learning rate and weight decay were set to 0.001. Each training run was allowed to proceed for a maximum of 200 epochs. All experiments were executed on a workstation equipped with an AMD EPYC processor and an NVIDIA RTX 3090 GPU. The architectural hyperparameters and dataset-specific adaptation settings selected after parameter testing are jointly summarized in Table 2.

#### 3.3 Evaluation Protocol

Model evaluation followed a leave-one-subject-out (LOSO) protocol. For each LOSO split, one stroke patient was held out as the target subject, while the remaining patients were used as the source domain. The model was trained using source-domain samples and then tested on the unseen target subject. This process was repeated sequentially until each subject had served once as the target domain. To prevent data leakage, the subject-wise partition was completed before model training, ensuring that labeled data from the target subject were never used during source-domain training and that no label information was transferred between the source and target domains.

The reported results were computed by averaging the evaluation metrics over all LOSO rounds. Cross-subject generalization performance was assessed using classification accuracy, Cohen’s kappa coefficient, recall, precision, and F1-score. Statistical comparisons between competing methods were further conducted using the Wilcoxon signed-rank test to obtain the corresponding p-values.

- Table 3: MI classification performance on XW-Stroke.

Method Accuracy (%) Recall (%) Precision (%) F1-Score (%) Kappa

EEGNet [4]∗∗ 61.56 ± 06.53 61.87 ± 13.83 62.00 ± 07.90 61.11 ± 08.37 0.231 ± 0.131 IFNet [5]∗∗ 61.88 ± 07.15 54.38 ± 17.22 67.20 ± 11.94 57.23 ± 13.25 0.237 ± 0.143 ShallowConvNet [6]∗∗ 62.29 ± 05.44 65.42 ± 14.14 62.32 ± 05.92 62.68 ± 08.57 0.246 ± 0.109 DBConformer [7]∗∗ 61.15 ± 04.89 62.29 ± 26.34 67.49 ± 14.54 58.45 ± 14.19 0.223 ± 0.098 EEGConformer [8]∗∗ 61.67 ± 04.66 65.00 ± 17.38 62.83 ± 06.48 61.68 ± 09.43 0.233 ± 0.093 MSCFormer [9]∗∗ 58.96 ± 05.30 61.88 ± 26.88 61.87 ± 10.33 56.89 ± 14.89 0.179 ± 0.106 SlimSeiz [10]∗∗ 58.75 ± 05.64 53.12 ± 22.68 63.41 ± 11.21 53.70 ± 13.62 0.175 ± 0.113 SSTDA [11]∗∗ 62.60 ± 05.57 54.79 ± 18.00 67.45 ± 11.04 57.98 ± 10.33 0.252 ± 0.111 UA-DANN [12]∗∗ 58.33 ± 03.86 49.17 ± 15.72 60.68 ± 04.52 52.81 ± 09.59 0.167 ± 0.077 SSAS [13]∗∗ 60.42 ± 06.15 57.08 ± 18.59 59.59 ± 14.19 56.98 ± 15.06 0.208 ± 0.123 CFSPMNet 68.23 ± 05.13 67.08 ± 16.83 69.91 ± 05.93 66.78 ± 09.29 0.365 ± 0.103

∗ and ∗∗ indicate statistically significant differences in Accuracy compared with CFSPMNet at p < 0.05 and p < 0.01, respectively.

- Table 4: MI classification performance on 2019-Stroke.

Method Accuracy (%) Recall (%) Precision (%) F1-Score (%) Kappa

EEGNet [4]∗ 55.83 ± 06.61 50.67 ± 31.94 61.09 ± 23.42 46.35 ± 24.93 0.117 ± 0.132 IFNet [5]∗∗ 55.42 ± 04.44 52.00 ± 22.01 60.62 ± 12.74 51.21 ± 13.35 0.108 ± 0.089 ShallowConvNet [6]∗∗ 57.25 ± 07.43 54.67 ± 37.06 58.06 ± 27.49 47.84 ± 26.24 0.145 ± 0.149 DBConformer [7]∗∗ 56.17 ± 07.90 43.00 ± 39.45 63.68 ± 30.54 38.63 ± 28.89 0.123 ± 0.158 EEGConformer [8]∗ 58.17 ± 04.81 58.17 ± 26.39 63.73 ± 12.67 54.67 ± 16.02 0.163 ± 0.096 MSCFormer [9]∗ 60.08 ± 08.07 57.00 ± 35.45 66.58 ± 24.90 52.05 ± 23.17 0.202 ± 0.161 SlimSeiz [10]∗ 57.33 ± 07.50 47.50 ± 32.44 66.70 ± 15.35 46.09 ± 23.24 0.147 ± 0.150 SSTDA [11] 63.50 ± 15.99 53.83 ± 35.61 58.78 ± 26.91 52.20 ± 31.10 0.270 ± 0.320 UA-DANN [12] 61.75 ± 05.45 68.33 ± 18.23 62.11 ± 06.61 62.86 ± 09.94 0.235 ± 0.109 SSAS [13] 65.08 ± 20.12 68.33 ± 26.72 64.27 ± 20.91 64.59 ± 23.55 0.302 ± 0.402 CFSPMNet 73.33 ± 18.71 81.50 ± 21.21 73.28 ± 19.59 75.11 ± 19.38 0.467 ± 0.374

∗ and ∗∗ indicate statistically significant differences in Accuracy compared with CFSPMNet at p < 0.05 and p < 0.01, respectively.

### 4 Results and Discussion

#### 4.1 Experimental Results

To evaluate the cross-patient decoding performance of CFSPMNet in post-stroke MI-EEG, we conducted comprehensive comparisons against various state-of-the-art baselines using the LOSO protocol. The selected baselines encompass a wide range of deep learning architectures and adaptation strategies: (1) Convolutional Neural Network (CNN)-based models, specifically EEGNet [4], IFNet [5], and ShallowConvNet [6]; (2) Transformer-based models, including DBConformer [7], EEGConformer [8], and MSCFormer [9]; (3) a Mamba-based model, SlimSeiz [10]; and (4) transfer learning or domain adaptation methods, such as SSTDA [11], UA-DANN [12], and SSAS [13].

As shown in Tables 3 and 4, CFSPMNet achieved the best average performance on both stroke datasets. On XW-Stroke, CFSPMNet demonstrated an accuracy of 68.23%, marking a substantial improvement of 5.63 percentage points over the strongest competitor, SSTDA. On 2019-Stroke, CFSPMNet reached 73.33% accuracy, exceeding the strongest competing method, SSAS, by 8.25 percentage points. CFSPMNet also achieved the highest F1-score and kappa on both datasets, which robustly confirms its effectiveness in achieving balanced class discrimination and agreement beyond chance.

This observed performance pattern provides critical insights into stroke-patient MI-EEG decoding. While CNN and Transformer baselines can extract local or global EEG dependencies, they often fall short in post-stroke MI-EEG requiring trial-level reorganization of disrupted latent neural-state arrangements. The advantage over SlimSeiz suggests that state-space propagation benefits from explicit Fourier-derived trial context. The improvement over adaptation baselines further indicates that target-domain pseudo-labeling becomes more reliable when semantic confidence is constrained by shared-private physiological consistency. On 2019-Stroke, the standard deviation remains large, likely reflecting pronounced inter-patient variability, yet CFSPMNet still maintains the highest mean values across all reported metrics. On XW-Stroke, all baseline comparisons reached p < 0.01, supporting a stable advantage under the selected stroke-patient cohort.

Table 5: Ablation results across datasets.

Dataset Variant Accuracy (%) ∆Acc. (%)

###### CFSPMNet 73.33 ± 18.71 –

w/o SPPM Strategy 71.00 ± 17.54 -2.33 w/o Dynamic Pseudo Update 64.75 ± 13.59 -8.58 w/o Fourier Context Guidance 69.25 ± 13.10 -4.08 w/o High-Frequency Branch 69.00 ± 17.52 -4.33 w/o Low-Frequency Branch 67.25 ± 17.41 -6.08

2019-Stroke

###### CFSPMNet 68.23 ± 5.13 –

w/o SPPM Strategy 63.96 ± 6.96 -4.27 w/o Dynamic Pseudo Update 63.65 ± 6.57 -4.58 w/o Fourier Context Guidance 63.75 ± 5.73 -4.48 w/o High-Frequency Branch 63.54 ± 7.74 -4.69 w/o Low-Frequency Branch 62.92 ± 5.09 -5.31

XW-Stroke

#### 4.2 Ablation Study

To analyze the contribution of each component, we performed module-level ablation studies on both datasets. As summarized in Table 5, every ablated variant reduced accuracy compared with the full CFSPMNet, indicating that the two proposed modules provide complementary benefits for cross-patient post-stroke MI-EEG decoding.

Removing the SPPM strategy resulted in a decrease in accuracy of 2.33 percentage points on 2019-Stroke and 4.27 percentage points on XW-Stroke. This result indicates that target-sample selection requires two simultaneous criteria: semantic confidence and compatibility between private physiological signatures and shared class prototypes learned from source patients. In post-stroke MI-EEG, altered cortical excitability and network coupling can produce confident predictions whose latent state organization deviates from the shared class structure. SPPM therefore acts as a physiological acceptance boundary: shared prototypes retain cross-patient class anchors, while private signatures preserve target-patient state characteristics. Furthermore, the variant without dynamic pseudo-label updating incurred even larger performance drops, particularly a substantial 8.58 percentage points on 2019-Stroke. This emphatically demonstrates that target supervision must dynamically adapt to the evolving target representation, preventing the model from being locked into patient-specific ambiguities early in the adaptation process. Dynamic updating allows pseudosupervision to be continuously refreshed, aligning with the progressive refinement of the target-patient’s neural-state organization.

The FRSM-related ablations further demonstrate the physiological contribution of Fourier-domain token-state reorganization. Removing Fourier context guidance reduced accuracy by 4.08 percentage points on 2019-Stroke and 4.48 percentage points on XW-Stroke, showing that Mamba state propagation benefits from trial-specific Fourier-derived context. From a neural-state perspective, the Fourier-derived context provides a compact description of how latent physiological tokens are coordinated within the current trial. This is important for stroke patients because changes in aperiodic operating points, cortical excitability, and inter-areal coordination can alter the ordering, coupling, and amplitude-phase coordination of class-related states even for the same MI class. Removing the High-Frequency Branch or Low-Frequency Branch also degraded performance, with drops of 4.33 and 6.08 percentage points on 2019-Stroke and 4.69 and 5.31 percentage points on XW-Stroke. These results indicate that the two Fourier branches provide non-redundant views of the trial-level physiological organization and jointly support context-conditioned state-space propagation.

Taken together, the ablation results support the synergistic design of CFSPMNet. FRSM improves the organization of within-trial latent neural states before state propagation, while SPPM constrains target-domain supervision using shared-private physiological consistency. The full model therefore links physiological token-state reorganization with calibrated pseudo-label updating, which is useful when the decoding substrate is reshaped at local, cross-regional, and global state levels.

#### 4.3 Hyperparameter Sensitivity Analysis

To evaluate sensitivity to key architectural and adaptation parameters, we tested the embedding size demo, temporal filters Ft, Fourier partition ratio rspec, and Fourier sparsity threshold τf. As shown in Fig. 4, the best embedding sizes were 30 for XW-Stroke and 38 for 2019-Stroke, while the best temporal filter number was 8 on both datasets. This pattern indicates that the latent token capacity should match the inherent complexity of each dataset (e.g., varying neurological

[Figure 4]

Figure 4: Hyperparameter sensitivity on XW-Stroke and 2019-Stroke.

heterogeneity or signal characteristics), whereas a moderate temporal front-end is sufficient before Fourier-domain reorganization.

The Fourier parameters also showed clear optima: rspec was 0.45 on XW-Stroke and 0.50 on 2019-Stroke, while τf was 0.01 on both datasets. Performance decreased when the partition ratio or sparsity threshold moved away from these values, suggesting that complementary Fourier states must preserve stable trial-level organization without retaining excessive perturbations. Parameter testing further showed that the remaining settings in Table 2 were optimal under the evaluated grid and were fixed when plotting Fig. 4: L was 2, α was 0.98/0.95, τp was 0.60, and EI was 25/10 for XW-Stroke/2019-Stroke. Overall, CFSPMNet performed best under a balanced configuration of representation capacity, Fourier-state reorganization, source anchoring, and calibrated target adaptation.

#### 4.4 Visualization of Feature Alignment

To qualitatively assess the effectiveness of CFSPMNet in feature space transformation, we visualize the feature distributions using t-SNE [21] in Fig. 5. Fig. 5(A) illustrates the initial representation space, where both source and target samples are broadly scattered, and the two MI classes exhibit weak organization. This indicates that direct cross-patient transfer is affected by patient-specific latent state mismatches. Fig. 5(B) shows the distributions after

[Figure 5]

Figure 5: t-SNE feature distributions on XW-Stroke and 2019-Stroke.

source-supervised representation learning and intermediate adaptation, where class-related structures become more discernible, yet a notable portion of target samples still cluster ambiguously with source regions. This observation aligns perfectly with the inherent difficulty of post-stroke MI-EEG decoding, where identical MI labels can correspond to various trial-level state trajectories across patients.

Fig. 5(C) reveals the final CFSPMNet representation space, where target samples form significantly more compact and well-separated class-specific groups, achieving superior alignment with the corresponding source-domain structures on both datasets. The left-hand and right-hand MI samples are also more clearly separated, especially after the shared-private pseudo-label calibration stage. This progression suggests that Fourier-domain token-state reorganization improves the ordering and coordination of trial-level latent physiological tokens, while SPPM further suppresses target samples whose semantic prediction is inconsistent with the shared physiological class structure. The visualization therefore supports the proposed design: CFSPMNet reorganizes cross-patient neural-state representations into a more discriminative and physiologically consistent feature space, beyond simple statistical discrepancy reduction to address underlying neurophysiological variations.

#### 4.5 Visualization of Fourier-Domain Token-State Reorganization

To further examine the physiological role of FRSM, Fig. 6 visualizes the block-level token modulation and the resulting Fourier-derived context on the two stroke datasets. In post-stroke MI-EEG, trial-to-trial states are shaped by background cortical excitability, aperiodic electrophysiological activity, and network-level coordination after injury [22, 23]. Therefore, an effective rehabilitation-oriented decoder should preserve trial-specific physiological organization before sequential state propagation.

As shown in Fig. 6, the branch-specific modulation maps contain structured variations across token index and embedding dimension, while the Fourier-derived context exhibits more coherent and concentrated organization. This significant difference suggests that FRSM does more than amplify isolated local fluctuations. It reorganizes the

[Figure 6]

Figure 6: Fourier-domain token-state reorganization on XW-Stroke and 2019-Stroke.

latent physiological tokens into a trial-level state arrangement that can condition the subsequent Mamba propagation process. Such context-conditioned propagation is relevant for stroke patients because their unique lesion conditions and compensatory recruitment mechanisms fundamentally alter how motor-imagery-related states are coordinated within each individual trial [24]. The visualization therefore supports the interpretation that the Fourier-domain operation provides a physiologically informed organizational basis for state propagation, helping the model retain motor-intention cues that are useful for cross-patient rehabilitation decoding.

#### 4.6 Analysis of Calibrated Target Pseudo-Label Selection

Fig. 7 illustrates how target-domain samples are accepted or rejected during calibrated pseudo-label updating. For rehabilitation-oriented BCI systems, unreliable pseudo-labels can reinforce incorrect motor-intention feedback for the target patient [25]. This risk is more pronounced in post-stroke MI-EEG, where a confident prediction may still be pathologically inconsistent with the shared physiological class organization because the patient’s latent neural-state trajectory can be reshaped by altered cortical excitability and network coordination.

In both datasets, accepted target samples are mainly distributed in the region where the semantic confidence margin and the physiological-consistency margin are simultaneously positive. Conversely, rejected samples appear in regions where at least one margin is insufficient, including candidates whose predicted class may be confident but whose physiological consistency fails to satisfy the shared-private acceptance criterion. This behavior indicates that SPPM does not rely on prediction confidence alone [26]. Instead, it constrains target-domain supervision by requiring the predicted motor-imagery label to be multi-dimensionally compatible with both global shared class anchors and the patient’s individual private physiological signature. From a rehabilitation perspective, this calibrated updating mechanism is important because adaptive decoding should strengthen target-patient supervision only when the candidate label is consistent with a plausible neural-state organization [18].

#### 4.7 Spatial Neurophysiological Interpretability Analysis

To assess whether the learned representation exhibits physiologically meaningful spatial organization, Fig. 8 presents scalp-level spatial weights and input-gradient responses on both stroke datasets [27]. The spatial weights summarize the channel organization learned by the spatial filtering front-end, whereas the input gradients estimate how sensitive

[Figure 7]

Figure 7: Calibrated target pseudo-label selection on XW-Stroke and 2019-Stroke.

the decoder output is to perturbations in the input EEG. These maps are interpreted as scalp-level model-sensitivity summaries without implying precise anatomical localization.

Across the two datasets, we observe distinct non-uniform spatial distributions in both the spatial weights and inputgradient maps. This strongly suggests that CFSPMNet leverages organized spatial patterns with channel-dependent sensitivity rather than treating all channels equally. The spatial patterns also differ between XW-Stroke and 2019Stroke, which is consistent with evidence that post-stroke motor-state information can involve distributed sensorimotor circuits and recovery-related network interactions [28]. The presence of distributed and dataset-dependent sensitivity reinforces the central motivation of this study that effective cross-patient stroke MI-EEG decoding fundamentally requires accounting for disrupted latent neural-state organization and patient-specific physiological signatures. For rehabilitation applications, such spatially organized sensitivity provides additional evidence that the model’s decisions are linked to neural-system structure relevant to motor-intention decoding.

#### 4.8 Rehabilitation-Oriented Pathophysiological Implications

The compelling results achieved by CFSPMNet extend far beyond mere classification accuracy, carrying profound implications for clinical post-stroke rehabilitation. For MI-based BCI to be truly effective in rehabilitation, the decoder must reliably link attempted motor intention to a stable and therapeutically actionable neural state that can drive meaningful feedback. FRSM supports this requirement by reorganizing latent physiological tokens before state propagation [1], so the sequence model follows the trial-specific state arrangement rather than only local feature responses. SPPM complements this process by accepting target samples only when semantic prediction and sharedprivate physiological consistency are jointly satisfied, reducing the risk that closed-loop adaptation reinforces confident but misaligned pseudo-supervision. Therefore, CFSPMNet provides a stable cross-patient initialization while retaining target-specific state signatures, supporting a rehabilitation view of post-stroke MI-EEG decoding as neural-state calibration between intention-related brain activity, decoder output, and therapeutic feedback.

#### 4.9 Limitations and Future Directions

This study remains an initial exploration of latent-state-organization-based cross-patient decoding. The available public stroke EEG resources are limited, and the XW-Stroke experiments used a clinically screened subcohort; although this improves cohort definition, the complete cohort and broader stroke populations still require evaluation. The relatively large standard deviations also indicate that performance remains sensitive to inter-patient variability, calling for larger and more clinically diverse validation.

The public datasets further lack complete clinical and neuroimaging metadata, which prevents model performance from being stratified according to lesion hemisphere, lesion location, lesion volume, corticospinal tract involvement, disease stage, medication status, rehabilitation history, and quantitative motor-function scores. As a result, the current framework can only adapt from EEG observations, without explicitly modeling how patient-specific pathological factors modulate MI-related rhythms and cross-patient transferability. Future work should therefore move beyond EEG-only adaptation by incorporating structured clinical variables and neuroimaging-derived descriptors into the decoding framework. For example, lesion profiles and motor impairment scores could be used to define clinically

[Figure 8]

Figure 8: Spatial neurophysiological interpretability on XW-Stroke and 2019-Stroke.

meaningful patient subgroups, guide source-patient selection, or regularize pseudo-label updating according to the expected degree of physiological similarity. In addition, prospective multi-center validation should be conducted under harmonized acquisition protocols to examine whether the proposed adaptation mechanism remains stable across hospitals, devices, therapists, and rehabilitation stages. Finally, online pseudo-label updating should be evaluated in repeated rehabilitation sessions, where the key outcome should not be limited to offline decoding accuracy but should also include session-to-session calibration stability, false-feedback reduction, user engagement, and measurable improvement in motor-function recovery. Such analyses would clarify whether improved cross-patient decoding can be translated into more reliable and clinically meaningful therapeutic feedback [29–31].

### 5 Conclusion

This paper proposes CFSPMNet for cross-patient post-stroke MI-EEG decoding by treating pathological transfer as a latent neural-state organization problem involving task-related dynamics, aperiodic activity, and local-to-global population states. FRSM reorganizes physiological tokens in the Fourier domain and injects trial-specific Fourier-

derived context into Mamba state propagation, while SPPM constrains target pseudo-label updating through semantic confidence and shared-private physiological consistency. Under the leave-one-subject-out protocol, CFSPMNet achieved accuracies of 68.23% on XW-Stroke and 73.33% on 2019-Stroke, outperforming representative CNN-, Transformer-, Mamba-, and adaptation-based baselines. Ablation, sensitivity, feature-alignment, pseudo-label selection, and spatial interpretability analyses further supported the contributions of Fourier-domain token-state reorganization and calibrated target adaptation. These findings suggest that rehabilitation-oriented post-stroke MI-EEG decoding can benefit from modeling neural-state calibration across patients, and future work should validate this framework in larger multi-center and online rehabilitation settings.

### Reference References

- [1] Madalena Valente, Diogo Branco, Sergi Bermúdez i Badia, Jean-Claude Fernandes, Patrícia Figueiredo, and Athanasios Vourvopoulos. Eeg-based predictors of motor recovery during immersive vr-bci rehabilitation. Scientific Reports, 16(1):7870, Feb 2026.
- [2] Hyunmi Lim, Hyoseon Choi, Bilal Ahmed, Yoonghil Park, and Jeonghun Ku. Attention-adaptive bci-aot system enhances motor recovery and neural engagement after stroke. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 34:686–698, 2026.
- [3] Bin Jiang, Xiangkai Wang, Dongyi He, Siyu Cheng, Maoyu Liao, Duoqian Miao, Qingling Xia, Yun Zhao, and Gen Li. A comprehensive review of deep learning for motor imagery eeg: From healthy subjects to patients. Biomedical Signal Processing and Control, 117:109680, 2026.
- [4] Vernon J Lawhern, Amelia J Solon, Nicholas R Waytowich, Stephen M Gordon, Chou P Hung, and Brent J Lance. Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces. Journal of Neural Engineering, 15(5):056013, jul 2018.
- [5] Jiaheng Wang, Lin Yao, and Yueming Wang. Ifnet: An interactive frequency convolutional neural network for enhancing motor imagery decoding from eeg. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31:1900–1911, 2023.
- [6] Robin Tibor Schirrmeister, Jost Tobias Springenberg, Lukas Dominique Josef Fiederer, Martin Glasstetter, Katharina Eggensperger, Michael Tangermann, Frank Hutter, Wolfram Burgard, and Tonio Ball. Deep learning with convolutional neural networks for eeg decoding and visualization. Human Brain Mapping, 38(11):5391–5420, 2017.
- [7] Ziwei Wang, Hongbin Wang, Tianwang Jia, Xingyi He, Siyang Li, and Dongrui Wu. Dbconformer: Dual-branch convolutional transformer for eeg decoding. IEEE Journal of Biomedical and Health Informatics, pages 1–14, 2025.
- [8] Yonghao Song, Qingqing Zheng, Bingchuan Liu, and Xiaorong Gao. Eeg conformer: Convolutional transformer for eeg decoding and visualization. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31:710–719, 2023.
- [9] Wei Zhao, Baocan Zhang, Haifeng Zhou, Dezhi Wei, Chenxi Huang, and Quan Lan. Multi-scale convolutional transformer network for motor imagery brain-computer interface. Scientific Reports, 15(1):12935, Apr 2025.
- [10] Guorui Lu, Jing Peng, Bingyuan Huang, Chang Gao, Todor Stefanov, Yong Hao, and Qinyu Chen. Slimseiz: Efficient channel-adaptive seizure prediction using a mamba-enhanced network. In 2025 IEEE International Symposium on Circuits and Systems (ISCAS), pages 1–5, 2025.
- [11] Peiyin Chen, Xiaofeng Liu, Chao Ma, He Wang, Xiong Yang, Celso Grebogi, Xiao Gu, and Zhongke Gao. Unsupervised domain adaptation with synchronized self-training for cross- domain motor imagery recognition. IEEE Journal of Biomedical and Health Informatics, 29(5):3664–3677, 2025.
- [12] Jian Shen, Lechun You, Yu Ma, Zeguang Zhao, Huajian Liang, Yanan Zhang, and Bin Hu. Ua-daan: An uncertaintyaware dynamic adversarial adaptation network for eeg-based depression recognition. IEEE Transactions on Affective Computing, 16(3):2130–2141, 2025.
- [13] Yici Liu, Qi Wei Oung, and Hoi Leong Lee. Ssas: Cross-subject eeg-based emotion recognition through source selection with adversarial strategy. Expert Systems with Applications, 308:130843, 2026.
- [14] Niklas Brake, Flavie Duc, Alexander Rokos, Francis Arseneau, Shiva Shahiri, Anmar Khadra, and Gilles Plourde. A neurophysiological basis for aperiodic eeg and the background spectral trend. Nature Communications, 15(1):1514, Feb 2024.

- [15] Megan E. McDonnell, Akash Umakantha, Ryan C. Williamson, Matthew A. Smith, and Byron M. Yu. Interactions across hemispheres in prefrontal cortex reflect global cognitive processing. Nature Communications, Apr 2026.
- [16] Niklas Brake, Flavie Duc, Alexander Rokos, F. Arseneau, Shiva Shahiri, A. Khadra, and G. Plourde. A neurophysiological basis for aperiodic eeg and the background spectral trend. Nature Communications, 15, 2024.
- [17] Zachariah R. Cross, Samantha M. Gray, Adam J. O. Dede, Yessenia M. Rivera, Q. Yin, Parisa Vahidi, E. M. Rau, Christopher Cyr, A. M. Holubecki, E. Asano, Jack J. Lin, Olivia Kim McManus, Shifteh Sattar, Ignacio Saez, Fady Girgis, David King-Stephens, Peter B. Weber, Stephan U Schuele, Joshua Rosenow, Joyce Y. Wu, Sandi K. Lam, Jeffrey S. Raskin, E. Chang, Ammar Shaikhouni, P. Brunner, Jarod L Roland, R. M. Braga, Robert T. Knight, N. Ofen, and E. Johnson. The development of aperiodic neural activity in the human brain. Nature human behaviour, 2025.
- [18] Zhanhui Lin, Yonglin Wu, Chenyun Dai, and Yao Guo. Enhancing real-time cross-subject eeg decoding via pseudo-label tuning and adaptation. Applied Soft Computing, 197:115150, 2026.
- [19] Haijie Liu, Penghu Wei, Haochong Wang, Xiaodong Lv, Wei Duan, Meijie Li, Yan Zhao, Qingmei Wang, Xinyuan Chen, Gaige Shi, Bo Han, and Junwei Hao. An eeg motor imagery dataset for brain computer interface in acute stroke patients. Scientific Data, 11(1):131, Jan 2024.
- [20] Tianyu Jia. Eeg data of motor imagery for stroke, 2 2019.
- [21] Laurens van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. Journal of Machine Learning Research, 9(86):2579–2605, 2008.
- [22] Asher J. Albertson, Eric C. Landsness, Margaret Eisfelder, Brittany M. Young, Bradley Judge, Matthew R. Brier, Matthew J. Euler, Steven C. Cramer, Jin-Moo Lee, and Keith R. Lohse. Stroke and motor outcomes are associated with regional and age-specific changes in periodic and aperiodic cortical activity. Experimental Physiology, 111(3):1210–1227, 2026.
- [23] N. Monchy, J. Duprez, J-F. Houvenaghel, A. Legros, B. Voytek, and J. Modolo. Functional connectivity is dominated by aperiodic, rather than oscillatory, coupling. Journal of Neuroscience, 45(45), 2025.
- [24] Kaichao Wu, Beth Jelfs, Qiang Fang, and Leonardo L. Gollo. Criticality and increased intrinsic neural timescales in stroke. npj Systems Biology and Applications, 12(1):4, Dec 2025.
- [25] Siqi Yang, Zhihua Huang, and Tian jian Luo. Joint spatial feature adaption and confident pseudo-label selection for cross-subject motor imagery eeg signals classification. Expert Systems with Applications, 278:127312, 2025.
- [26] Yong Peng, Jiangchuan Liu, Honggang Liu, Natasha Padfield, Junhua Li, Wanzeng Kong, Bao-Liang Lu, and Andrzej Cichocki. Prediction consistency and confidence-based proxy domain construction for privacy-preserving in cross-subject eeg classification. IEEE Journal of Biomedical and Health Informatics, 30(2):1115–1127, 2026.
- [27] Ga-Young Choi, Jeong-Kweon Seo, Kyoung Tae Kim, Won Kee Chang, Sung Whan Yoon, Nam-Jong Paik, Won-Seok Kim, and Han-Jeong Hwang. Clinical feasibility of motor hotspot localization based on electroencephalography using convolutional neural networks in stroke. Journal of NeuroEngineering and Rehabilitation, 22(1):193, Sep 2025.
- [28] Ke Deng, Jie Zhao, Yuqi Liu, Chune Tian, Xiaofei Lin, Xiaoqing Wei, Rui Li, and Weiping Liu. Task-state eeg reveals fine hand motor impairment in acute ischemic stroke: A multidimensional analysis of cortical dynamics. NeuroRehabilitation, 0(0):10538135261441843, 2026. PMID: 42053233.
- [29] Dongyi He, Wai Ting Siok, and Nizhuan Wang. Toward robust, reproducible, and widely accessible intracranial language brain-computer interfaces: A comprehensive review of neural mechanisms, hardware, algorithms, evaluation, clinical pathways and future directions, 2026.
- [30] Yueyang Li, Weiming Zeng, Wenhao Dong, Di Han, Lei Chen, Hongyu Chen, Zijian Kang, Shengyu Gong, Hongjie Yan, Wai Ting Siok, and Nizhuan Wang. A tale of single-channel electroencephalography: Devices, datasets, signal processing, applications, and future directions. IEEE Transactions on Instrumentation and Measurement, 74:1–20, 2025.
- [31] Junlin Wang, Xiaodong Li, Xingyu Lu, Ningbo Fei, Wei Huang, and Yong Hu. A somatosensory erp-bci system for post-stroke hand function rehabilitation applications. IEEE Transactions on Instrumentation and Measurement, 75:1–12, 2026.

