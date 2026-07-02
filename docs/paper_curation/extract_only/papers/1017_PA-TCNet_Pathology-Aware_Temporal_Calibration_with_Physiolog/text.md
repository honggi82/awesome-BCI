# arXiv:2604.16554v1[cs.CV]17Apr2026

PA-TCNET: PATHOLOGY-AWARE TEMPORAL CALIBRATION WITH PHYSIOLOGY-GUIDED TARGET REFINEMENT FOR CROSS-SUBJECT MOTOR IMAGERY EEG DECODING IN STROKE PATIENTS

Xiangkai Wang1, Yun Zhao2,∗, Dongyi He1,3, Qingling Xia1, Gen Li1,4, Nizhuan Wang3,∗, Ningxiao Peng5, and Bin Jiang1,∗

- 1School of Artificial Intelligence, Chongqing University of Technology, Chongqing 401135, China; Chongqing Key Laboratory of Embodied Intelligence Perception and Autonomous Learning

for Humanoid Robots; Key Laboratory of Advanced Equipment Intelligence of the Chongqing Education Commission, Chongqing 401135, China

- 2School of Smart Health, Chongqing Polytechnic University of Electronic Technology, Chongqing 401131, China

3Department of Language Science and Technology, The Hong Kong Polytechnic University, Hung Hom, Hong Kong SAR, China

- 4School of Pharmacy and Bioengineering, Chongqing University of Technology, Chongqing 400054, China
- 5School of Computer Science and Engineering, Chongqing University of Technology, Chongqing 401135, China

kevinwang@stu.cqut.edu.cn; zhaoyun@cqcet.edu.cn; hedongyi6438@gmail.com qingling@cqut.edu.cn; ligen1990@cqut.edu.cn; wangnizhuan1120@gmail.com xxx_saik@163.com; jb20200132@cqut.edu.cn

∗Corresponding authors: Yun Zhao (zhaoyun@cqcet.edu.cn), Nizhuan Wang (wangnizhuan1120@gmail.com), and Bin Jiang (jb20200132@cqut.edu.cn)

## ABSTRACT

Stroke patient cross-subject electroencephalography (EEG) decoding of motor imagery (MI) braincomputer interface (BCI) is essential for motor rehabilitation, yet lesion-related abnormal temporal dynamics and pronounced inter-patient heterogeneity often undermine generalization. Existing adaptation methods are easily misled by pathological slow-wave activity and unstable target-domain pseudo-labels. To address this challenge, we propose PA-TCNet, a pathology-aware temporal calibration framework with physiology-guided target refinement for stroke motor imagery decoding. PA-TCNet integrates two coordinated components. The Pathology-aware Rhythmic State Mamba (PRSM) module decomposes EEG spatiotemporal features into slowly varying rhythmic context and fast transient perturbations, injecting the fused pathological context into selective state propagation to more effectively capture abnormal temporal dynamics. The Physiology-Guided Target Calibration (PGTC) module constructs source-domain sensorimotor region-of-interest templates, imposing physiological consistency constraints and dynamically refining target-domain pseudo-labels, thereby improving adaptation reliability. Leave-one-subject-out experiments on two independent stroke EEG datasets, XW-Stroke and 2019-Stroke, yielded mean accuracies of 66.56% and 72.75%, respectively, outperforming state-of-the-art baselines. These results indicate that jointly modeling pathological temporal dynamics and physiology-constrained pseudo-supervision can provide more robust crosssubject initialization for personalized post-stroke MI-BCI rehabilitation. The implemented code is available at https://github.com/wxk1224/PA-TCNet.

Keywords Stroke rehabilitation, brain-computer interface (BCI), electroencephalography (EEG), motor imagery (MI), domain adaptation, physiology-guided calibration

## 1 Introduction

Stroke is one of the leading neurological disorders causing long-term motor dysfunction, and it is commonly characterized by impaired upper-limb motor function, reduced coordination, and prolonged recovery duration [1,2]. Motor imagery (MI) electroencephalography (EEG) decoding based on brain-computer interfaces (BCIs) provides important technical support for recognizing patients’ motor intentions and facilitating subsequent rehabilitation training [3,4]. Owing to its non-invasive nature, high temporal resolution, portability, and relatively low cost, EEG has become one of the most important signal carriers for MI decoding in intelligent rehabilitation engineering [5].

Among related tasks, cross-subject decoding is a key prerequisite for clinical translation. In healthy subjects, EEG activity over the sensorimotor cortex during MI exhibits clear rhythmic characteristics: event-related desynchronization (ERD) in the mu (8–13 Hz) and beta (13–30 Hz) bands is typically observed over the hemisphere contralateral to the imagined limb movement, whereas event-related synchronization (ERS) appears over the ipsilateral hemisphere. This spatiotemporal pattern also shows a relatively stable ROI distribution over the sensorimotor area [6]. For local spatiotemporal modeling, EEGNet [7] and ShallowConvNet [8] extract task-relevant features through a compact convolutional architecture and a shallow convolutional pathway, respectively. For temporal and time-frequency modeling, IFNet [9] strengthens the coupled representation of different frequency components through interactive frequency convolution. EEGConformer [10] combines convolutional structures with a Transformer to introduce global dependency modeling while preserving local spatiotemporal feature extraction. MSCFormer [11] and DBConformer [12] further enhance representation capability from the perspectives of multi-scale modeling and dual-branch parallel spatiotemporal modeling, respectively. Building on these advances, SlimSeiz [13] incorporates Mamba-based state-space modeling into a lightweight convolutional backbone. For target-domain adaptation, SSTDA [14] validates the effectiveness of pseudo-label strategies in EEG decoding by jointly exploiting source-domain labels and target-domain pseudolabels. SSAS [15] explicitly selects source domains to preserve more transferable knowledge and alleviate negative transfer. UA-DANN [16] introduces uncertainty awareness into a dynamic adversarial adaptation framework to improve reliability and robustness during domain transfer.

Despite this progress in healthy population, cross-subject MI decoding in stroke patients still faces fundamental challenges because stroke EEG deviates markedly from healthy physiological patterns [17, 18]. On the one hand, lesions induce rhythm reorganization in the sensorimotor cortex, manifested as abnormal increases in low-frequency slow waves, attenuated or even reversed ERD/ERS amplitudes in the mu/beta rhythms, and disrupted interhemispheric balance, with enhanced compensatory activation in the unaffected hemisphere and dominant inhibitory activity in the affected hemisphere [19–21]. On the other hand, local abnormal disturbances, such as pathological spike-and-slow-wave activity and focal slowing, are superimposed on rhythm modulation related to motor intention, so EEG signals contain both neurophysiological responses and pathological noise. In addition, differences in lesion location, lesion size, and impairment severity further amplify the joint-distribution shift across patients, making it difficult for models trained under conventional assumptions to generalize directly [22–24]. Existing domain adaptation methods mainly rely on prediction confidence or statistical distribution alignment while overlooking the neurophysiological nature of EEG signals [25]. In stroke patients, highly confident predictions may not originate from genuine motor intention but instead from pathological noise, such as low-frequency drift or abnormal rhythms [26]. Such noise can exhibit statistical pseudo-certainty, thereby misleading pseudo-label generation and causing cumulative error propagation.

To address pathological temporal mismatch and pseudo-label unreliability, this paper proposes PA-TCNet for crosssubject MI decoding in stroke patients. The central idea is that stroke EEG should not be treated as a temporally homogeneous process. Instead, explicit decomposition of pathological rhythms, especially the separation of slow-wave background and transient disturbances, should be combined with neurophysiological priors from the sensorimotor ROI, such as class-related ERD/ERS templates. On this basis, PA-TCNet improves adaptation through pathology-aware temporal modeling and physiologically constrained pseudo-label calibration.

The main contributions are summarized as follows:

- 1. PA-TCNet, a pathology-aware adaptation framework for cross-subject MI decoding in stroke patients, is proposed to unify pathological dynamic representation and physiology-guided target calibration within a single training framework.
- 2. Pathology-aware Rhythmic State Mamba (PRSM) module: an explicit dual-timescale Mamba-based temporal model, is developed to jointly capture slowly varying rhythmic trends and transient pathological details in stroke EEG.
- 3. Physiology-Guided Target Calibration (PGTC) module: an ROI-based physiological template constraint is introduced to screen and dynamically update target-domain pseudo-labels, thereby improving the reliability of unlabeled target-domain adaptation and reducing cumulative pseudo-labeling errors.

[Figure 1]

- Figure 1: Overall framework of PA-TCNet. The network first extracts local sensorimotor spatiotemporal patterns, then performs pathology-aware temporal calibration through PRSM, and finally refines target-domain pseudo-labels with PGTC for joint adaptation.

The remainder of this paper is organized as follows. Section 2 presents the details of the proposed method. Section 3 describes the experimental setup, including datasets, preprocessing, evaluation protocol, and implementation details. Section 4 reports the results and discussion, including overall performance, ablation analysis, and mechanism-oriented interpretation. Section 5 concludes the paper.

## 2 Method

The proposed PA-TCNet consists of two coordinated components: PRSM and PGTC. PRSM aims to model the abnormal temporal dynamics of stroke EEG and produce pathology-aware temporal representations, whereas PGTC calibrates target-domain pseudo-labels by combining prediction confidence with source-domain physiological templates extracted from the sensorimotor ROI. Given labeled source-domain EEG and unlabeled target-domain EEG, the model first extracts local spatiotemporal patterns and organizes them into temporal tokens, then performs temporal modeling and class prediction through PRSM. For target-domain samples, PGTC further screens and dynamically updates pseudo-labels to provide more reliable adaptation supervision. The overall framework and the PRSM block are illustrated in Figs. 1 and 2, respectively.

### 2.1 Problem Formulation

Cross-subject MI decoding in stroke patients can be formulated as an adaptation problem from labeled source-domain data to unlabeled target-domain data. The source and target domains are denoted by:

Ds = {(Xis,Yis)}N

i=1, Dt = {Xjt}N

j=1, (1)

s

t

where Xis and Yis denote the i-th source-domain EEG sample and its label, respectively; Xjt denotes the j–th unlabeled target-domain EEG sample; and Ns and Nt are the numbers of source and target samples.

For an EEG trial X ∈ RC×T, C denotes the number of EEG channels and T denotes the number of temporal sampling points in each channel. The n-th sample can be represented as Xn = (xn,1,xn,2,...,xn,C), where xn,c ∈ RT denotes the temporal sequence of the c-th channel. The corresponding label yn is assigned to the entire EEG trial rather than to any individual channel.

[Figure 2]

- Figure 2: Architecture of the Pathology-aware Rhythmic State Mamba (PRSM) module. The module decomposes temporal tokens into slow rhythmic context and fast transient details, fuses both branches into a pathology-aware context, and injects that context into selective state propagation.

In cross-subject stroke MI decoding, the source and target domains typically satisfy:

P(Xs,Y s) ̸= P(Xt,Y t), (2)

which indicates a significant joint-distribution shift. This shift is reflected not only in the statistical properties of EEG signals across patients, but also in the inconsistency of class-discriminative structures.

The goal of this study is therefore to learn a target-oriented decoding function:

h = gϕ ◦ fθ, (3)

where fθ denotes the feature encoder, gϕ denotes the classifier, and ◦ denotes the Hadamard product. The model should simultaneously reduce cross-subject temporal representation mismatch under stroke pathology and improve the reliability of target-domain pseudo-supervision.

### 2.2 Pathology-aware Rhythmic State Mamba (PRSM)

To reduce the representation mismatch caused by abnormal temporal dynamics, PRSM, as shown in Fig. 2, explicitly distinguishes slowly varying rhythmic background from fast transient disturbances and injects the resulting rhythmic context into selective state propagation. Given an input trial X ∈ RC×T, PRSM first generates spatiotemporal token sequences, then performs rhythmic decomposition, multi-scale context fusion, and context-guided state modeling to obtain the pathology-aware representation Z∗.

### 2.2.1 Local Sensorimotor Pattern Encoding

The preprocessed EEG is first mapped into a token sequence by a local sensorimotor pattern encoder. Let {Tm}Mm=1 denote a set of local temporal filters with different receptive fields. Temporal pattern extraction is expressed as:

Ftemp = At {Tm(X)}Mm=1 , (4)

where At(·) denotes the aggregation operator over multi-scale temporal responses. A cross-channel spatial mapping S(·) is then used to model coordinated activation in the sensorimotor area, followed by a compact fusion mapping F(·) to remove redundant coupling:

Femb = F S(Ftemp) (5) After temporal compression and serialization, the model obtains a spatiotemporal token sequence:

Z = [z1,z2,...,zL] ∈ RL×D, (6) where L is the number of tokens and D is the embedding dimension.

### 2.2.2 Rhythmic Context Construction

To explicitly model pathological dynamics across different timescales in stroke MI-EEG, PRSM performs temporal rhythmic decomposition. Stroke EEG is often accompanied by enhanced low-frequency slow-wave activity. Let the normalized token sequence be Z˜ and let L(·) denote a feature-level low-frequency extraction operator. The slowly varying rhythmic component Zlow and the local transient component Zhigh are defined as:

Zlow = L(Z˜), Zhigh = Z˜ − Zlow (7)

This decomposition enables the model to isolate abnormal low-frequency drift from transient pathological fluctuations. Multi-scale temporal mappings are then applied to the slow-rhythm branch and the fast-detail branch to produce Flow and Fhigh, respectively. The rhythmic context is finally defined as:

Cr = H(Flow,Fhigh) + Ar(Flow,Fhigh), (8) where H(·,·) denotes the context fusion mapping and Ar(·,·) denotes a residual aggregation term.

### 2.2.3 Context-guided Selective State Modeling

The rhythmic context Cr directly participates in state-propagation parameterization. Given the normalized token sequence Z˜, an input projection first generates the main branch and the residual branch:

[U,R] = Split WinZ˜ , U,R ∈ RL×D

, (9)

i

where Di is the internal state dimension. The rhythmic context then produces an adaptive scaling term and an additive bias term for both branches:

S = σ(WsCr), B = WbCr, (10) U¯ = U ⊙ (1 + S), R¯ = R + B (11)

Through this operation, pathology-related rhythmic information modulates both the input drive and residual gating in a context-dependent manner.

After local temporal pre-encoding, U¯ is fed into the selective state-space model. At the l-th position, the state recursion is written as:

hl = A¯lhl−1 + B¯lul, ol = C¯lhl + Dul, (12)

where ul is the input at the l-th position of U¯ and A¯l, B¯l, and C¯l are input-dependent selective state parameters. The final output representation is:

zl∗ = Wout(ol ⊙ φ(¯rl)), (13)

where φ(·) is a nonlinear activation function and r¯l is the gating term at the l-th position of R¯. Stacking all positions yields:

Z∗ = PRSM(Z;Cr) (14)

In this way, slow rhythmic background and fast transient disturbances are fused into Cr and jointly regulate state updates and residual pathways, thereby improving representation stability under abnormal rhythmic drift, local transient perturbations, and cross-subject temporal heterogeneity.

### 2.3 Physiology-Guided Target Calibration (PGTC)

As shown in Fig. 1, PGTC is proposed to enforce a joint criterion of semantic confidence and physiological plausibility. It first derives class-specific ROI templates from the source domain, and then combines prediction probabilities with ROI-template matching to filter and dynamically update pseudo-labels for the target domain.

### 2.3.1 Source ROI Template Construction

PGTC first constructs class-related ROI physiological templates in the source domain. Let R(·) denote the ROI feature extractor. For any source-domain sample Xis, its ROI representation is:

ris = R(Xis) ∈ Rd

, (15)

r

where dr is the dimension of the ROI feature vector. In this work, R(·) is built from fixed sensorimotor electrodes. The left ROI, middle ROI, and right ROI are composed of {FC3,C3,CP3}, {FCz,Cz,CPz}, and {FC4,C4,CP4},

respectively. For the i-th source-domain sample, the trial-level average temporal sequences of the three groups are denoted by Lsi, Mis, and Ris. A bilateral asymmetry term is then defined as:

Bis = |Lsi − Ris| (16) The source ROI representation is obtained by concatenating the left, right, asymmetry, and middle terms and then applying L2 normalization:

ris = Norm2([Lsi,Ris,Bis,Mis]) (17) Given the index set of source samples from the k-th class, Ik = {i|Yis = k}, the class template is defined as:

1 |Ik| i∈I

ris , k ∈ {1,...,K}, (18)

Tk = Norm2

k

which provides the prototype of the k-th MI class in ROI space. To characterize intra-class physiological variability, an adaptive template-matching threshold is further defined through cosine similarity:

1 |Ik| i∈I

sim(ris,Tk)

δk = max δmind,

(19)

k

− Std {sim(ris,Tk)}i∈Ik

,

where sim(·,·) denotes cosine similarity and δmin is the lower bound of the threshold. The resulting source template set is:

T = {(Tk,δk)}Kk=1 (20)

In subsequent target calibration, Tk provides the class-related physiological prototype and δk defines the acceptable level of physiological consistency.

### 2.3.2 Pseudo-label Calibration

After the source ROI template set T is constructed, PGTC calibrates the target pseudo-labels. For a target-domain sample Xjt, the classifier first outputs class probabilities and a candidate class, while the ROI representation is extracted simultaneously:

pj = gϕ(fθ(Xjt)) ∈ RK, yˆj = arg max

pj,k, rjt = R(Xjt)

(21)

k

The acceptance condition is then defined by combining semantic confidence and physiological matching:

pj,k > τp, sim(rjt,Tyˆ

, (22) where τp is the confidence threshold and δyˆ

max

) > δyˆ

j

j

k

is the class-specific physiological threshold. The calibrated pseudo-label is defined as:

j

onehot(ˆyj), if Xjt satisfies the joint criterion, 0, otherwise.

y˜jt =

(23)

Here, 0 means that the sample is excluded from target-domain supervision at the current iteration. PGTC further refreshes y˜jt dynamically during training, so the target supervision set becomes:

D˜t = {(Xjt,y˜jt)}N

j=1 (24)

t

This formulation transforms target-domain pseudo-supervision into a joint constraint process wherein class probabilities propose candidate labels, ROI templates assess their physiological plausibility, and dynamic updates suppress the early mislabel accumulation.

### 2.4 Optimization Strategy

With pathology-aware representations and calibrated target supervision, model training is formulated as a joint optimization problem that combines explicit source-domain supervision with constrained target-domain pseudosupervision. Because target pseudo-labels are unstable at the beginning of training, a two-stage strategy is adopted: source-only warm-up followed by joint adaptation.

Table 1: Summary of dataset protocols and model input specifications used in this study.

##### Dataset Task System Sampling rate Trials per subject Model input shape

XW-Stroke Left- vs. right-hand MI 10–20 500 Hz 40 (20 per class) 30 × 1000 2019-Stroke Left- vs. right-hand MI 10–10 512 Hz 80 (40 per class) 63 × 1708

- 2.4.1 Warm-up

During warm-up, only labeled source-domain samples are used to optimize the encoder fθ and classifier gϕ. The objective is:

Lsrc =

1 Ns

Ns

i=1

ℓ(gϕ(fθ(Xis)),Yis), (25)

where ℓ(·,·) denotes the cross-entropy loss. This stage avoids unstable target predictions from interfering with early parameter updates.

- 2.4.2 Joint Adaptation

After warm-up, the model introduces PGTC-calibrated target pseudo-labels for joint adaptation. The target-domain loss is defined as:

Ltgt =

1 Nt

Nt

j=1

1 y ˜jt ̸= 0 ℓ gϕ(fθ(Xjt)),y˜jt , (26)

where 1(·) denotes the indicator function. The overall objective is:

L = αLsrc + (1 − α)Ltgt, (27) where α ∈ (0,1) controls the trade-off between source-domain supervision and calibrated target-domain pseudosupervision. After each training round, the model recomputes pj and rjt and refreshes D˜t dynamically so that the target supervision evolves together with representation quality.

- 3 Experiments

- 3.1 Datasets

XW-Stroke: The XW-Stroke dataset [27] was collected at Xuanwu Hospital, Capital Medical University. The original dataset contains 50 acute ischemic stroke patients (39 males and 11 females). All subjects performed left-hand and right-hand MI tasks, and EEG was recorded with 30 channels under the international 10–20 system at 500 Hz. To reduce clinical heterogeneity that was not directly aligned with the cross-subject modeling objective, a well-defined patient subcohort was further selected according to predefined clinical inclusion criteria: right-handedness, first-ever stroke, NIHSS score below 10, and disease duration below 10 years. These criteria were determined solely by clinical attributes and were independent of the model training and classification outcomes. The final cohort included 24 patients, indexed as 2, 5, 8, 9, 11, 12, 14, 17, 21, 23, 24, 26, 27, 28, 30, 32, 33, 37, 38, 43, 44, 47, 49, and 50.

2019-Stroke: The 2019-Stroke dataset was collected by Jia et al. [28]. It contains 15 stroke patients, each performing left-hand and right-hand MI tasks, with both paretic-side and non-paretic-side imagination included in the original acquisition setting. EEG was recorded with 63 channels under the international 10–10 system at 512 Hz. All publicly available subjects were used without additional subject-level exclusion.

- 3.2 Preprocessing

To preserve MI-related rhythms while suppressing interference, the raw EEG signals were first band-pass filtered between 8 and 30 Hz and then downsampled to 250 Hz. All channels were subsequently re-referenced by common average referencing and baseline corrected to reduce common noise and slow drift. Finally, independent component analysis (ICA) was applied to separate and remove artifact-related components.

Table 2: Detailed architectural hyperparameters of PA-TCNet.

Parameter Value

Embedding size 30 Encoder depth 2 Temporal filters per branch 10 Spatial multiplier 3 Temporal kernel sizes {36, 24, 18} Pooling size 8 Frequency kernel setting {5, 9, 13}, {3, 5, 7}

Table 3: Dataset-specific default adaptation hyperparameters of PA-TCNet.

Hyperparameter XW-Stroke 2019-Stroke

Source loss weight α 0.98 0.95 Confidence threshold τp 0.60 0.60 ROI threshold floor δmin 0.50 0.45 Warm-up epochs Ew 25 10

### 3.3 Evaluation Protocol and Metrics

In this study, Leave-one-subject-out (LOSO) protocol was adopted to evaluate model performance. In each round, one stroke patient was selected as the target subject and all remaining subjects were treated as the source domain. The model was trained on the source-domain data and evaluated on the held-out target subject. This procedure was repeated until every subject had been used once as the target domain. To avoid data leakage, subject-level splitting was performed before training so that the target subject did not participate in source training with labels and no labeled information was shared across source and target domains.

The final performance was obtained by averaging all evaluation metrics across all LOSO rounds. Specifically, classification accuracy (Accuracy), Cohen’s kappa coefficient, recall, precision, and F1-score were used to assess cross-subject generalization performance. In addition, Wilcoxon signed-rank tests were used to compute p-values for significance analysis between competing methods.

### 3.4 Implementation Details and Hyperparameter Settings

The proposed PA-TCNet was implemented via PyTorch under Python 3.12. Training used the Adam optimizer with an initial learning rate of 0.001, a weight decay of 0.001, and a maximum of 200 epochs. All experiments were conducted on an AMD EPYC CPU and an NVIDIA RTX 3090 GPU. The architectural hyperparameters of PA-TCNet are summarized in Table 2, and the dataset-specific default adaptation settings are listed in Table 3.

## 4 Results and Discussion

### 4.1 Overall Performance

To evaluate the effectiveness of proposed PA-TCNet on cross-subject MI classification in stroke patients, this study compared it with representative baselines on XW-Stroke and 2019-Stroke. The baselines included three CNN-based models, EEGNet [7], ShallowConvNet [8], and IFNet [9]; three Transformer-based models, EEGConformer [10], MSCFormer [11], and DBConformer [12]; one Mamba-based model, SlimSeiz [13]; and three transfer or adaptation methods, UA-DANN [16], SSTDA [14], and SSAS [15].

As reported in Table 4 and Table 5, PA-TCNet achieved the best performance on both datasets. On XW-Stroke, it improved the best competing method by 3.96%. On 2019-Stroke, the gain reached 7.67%. Relative to classical convolutional models, PA-TCNet improved accuracy by 5.00% and 4.27% over EEGNet and ShallowConvNet on XW-Stroke, and by 16.92% and 15.50% on 2019-Stroke. The consistent advantage over Transformer-based and adaptation-based baselines indicates that jointly modeling pathological temporal dynamics and physiology-guided pseudo-supervision yields stronger cross-subject generalization under stroke-specific distribution shifts.

Overall, PA-TCNet obtained the highest accuracy and kappa on both datasets. The significance analysis further showed that, except for the comparisons with UA-DANN, SSTDA, and SSAS on 2019-Stroke, the performance differences

Table 4: Comparison of MI classification performance on the XW-Stroke dataset.

Method Accuracy (%) Recall (%) Precision (%) F1-Score (%) Kappa

EEGNet [7]∗∗ 61.56 ± 06.53 61.87 ± 13.83 62.00 ± 07.90 61.11 ± 08.37 0.231 ± 0.131 ShallowConvNet [8]∗∗ 62.29 ± 05.44 65.42 ± 14.14 62.32 ± 05.92 62.68 ± 08.57 0.246 ± 0.109 IFNet [9]∗ 61.88 ± 07.15 54.38 ± 17.22 67.20 ± 11.94 57.23 ± 13.25 0.237 ± 0.143 EEGConformer [10]∗∗ 61.67 ± 04.66 65.00 ± 17.38 62.83 ± 06.48 61.68 ± 09.43 0.233 ± 0.093 MSCFormer [11]∗∗ 58.96 ± 05.30 61.88 ± 26.88 61.87 ± 10.33 56.89 ± 14.89 0.179 ± 0.106 DBConformer [12]∗∗ 61.15 ± 04.89 62.29 ± 26.34 67.49 ± 14.54 58.45 ± 14.19 0.223 ± 0.098 SlimSeiz [13]∗∗ 58.75 ± 05.64 53.12 ± 22.68 63.41 ± 11.21 53.70 ± 13.62 0.175 ± 0.113 UA-DANN [16]∗∗ 58.33 ± 03.86 49.17 ± 15.72 60.68 ± 04.52 52.81 ± 09.59 0.167 ± 0.077 SSTDA [14]∗∗ 62.60 ± 05.57 54.79 ± 18.00 67.45 ± 11.04 57.98 ± 10.33 0.252 ± 0.111 SSAS [15]∗∗ 60.42 ± 06.15 57.08 ± 18.59 59.59 ± 14.19 56.98 ± 15.06 0.208 ± 0.123 PA-TCNet 66.56 ± 06.61 63.12 ± 15.86 69.57 ± 09.55 64.30 ± 10.92 0.331 ± 0.132

∗ and ∗∗ indicate statistically significant differences in Accuracy compared with PA-TCNet at p < 0.05 and p < 0.01, respectively.

Table 5: Comparison of MI classification performance on the 2019-Stroke dataset.

Method Accuracy (%) Recall (%) Precision (%) F1-Score (%) Kappa

EEGNet [7]∗ 55.83 ± 06.61 50.67 ± 31.94 61.09 ± 23.42 46.35 ± 24.93 0.117 ± 0.132 ShallowConvNet [8]∗∗ 57.25 ± 07.43 54.67 ± 37.06 58.06 ± 27.49 47.84 ± 26.24 0.145 ± 0.149 IFNet [9]∗∗ 55.42 ± 04.44 52.00 ± 22.01 60.62 ± 12.74 51.21 ± 13.35 0.108 ± 0.089 EEGConformer [10]∗ 58.17 ± 04.81 58.17 ± 26.39 63.73 ± 12.67 54.67 ± 16.02 0.163 ± 0.096 MSCFormer [11]∗ 60.08 ± 08.07 57.00 ± 35.45 66.58 ± 24.90 52.05 ± 23.17 0.202 ± 0.161 DBConformer [12]∗∗ 56.17 ± 07.90 43.00 ± 39.45 63.68 ± 30.54 38.63 ± 28.89 0.123 ± 0.158 SlimSeiz [13]∗ 57.33 ± 07.50 47.50 ± 32.44 66.70 ± 15.35 46.09 ± 23.24 0.147 ± 0.150 UA-DANN [16] 61.75 ± 05.45 68.33 ± 18.23 62.11 ± 06.61 62.86 ± 09.94 0.235 ± 0.109 SSTDA [14] 63.50 ± 15.99 53.83 ± 35.61 58.78 ± 26.91 52.20 ± 31.10 0.270 ± 0.320 SSAS [15] 65.08 ± 20.12 68.33 ± 26.72 64.27 ± 20.91 64.59 ± 23.55 0.302 ± 0.402 PA-TCNet 72.75 ± 17.36 71.67 ± 23.62 75.25 ± 18.23 71.50 ± 19.24 0.455 ± 0.347

∗ and ∗∗ indicate statistically significant differences in Accuracy compared with PA-TCNet at p < 0.05 and p < 0.01, respectively.

between PA-TCNet and the remaining baselines reached statistical significance (p < 0.05). These results confirm that PA-TCNet maintains a stable performance advantage across different stroke data distributions.

### 4.2 Visualization of Feature Alignment

- Fig. 3 provides an intuitive view of the working mechanism of PA-TCNet using t-SNE [29]. In the original EEG space, source-domain data (semi-transparent points) and target-domain data (solid points) are irregularly interwoven, indicating severe cross-domain distribution shift and weak class-wise aggregation across patients. After PGTC screening, the accepted target samples begin to contract toward class-related regions with clearer physiological meaning, suggesting that physiology-guided pseudo-labeling effectively filters unreliable target samples while retaining a more discriminative target subset. In the final PRSM output space, the source and target features become better aligned and form more clearly separated left-hand and right-hand MI clusters. This progressive evolution shows that physiology-guided adaptation can map disordered pathological EEG features into a more separable semantic space.

### 4.3 Ablation Study

To verify the contribution of each component, module-level ablation studies are conducted on both datasets, with the results summarizing in Table 6. Compared with the full model, the Source Only setting decreased by 8.33% on 2019-Stroke and 2.71% on XW-Stroke, showing that source supervision alone is insufficient to overcome cross-subject distribution shift in stroke EEG. Removing PGTC caused accuracy drops of 6.08% and 1.98%, respectively, indicating that physiology-guided pseudo-label calibration is important for stabilizing target-domain supervision. Removing

Table 6: Ablation results of PA-TCNet across different datasets.

Dataset Variant Accuracy (%) Change (%)

###### PA-TCNet 72.75 ± 17.36 –

Source Only 64.42 ± 11.84 -8.33 w/o PGTC 66.67 ± 12.33 -6.08 w/o ROI Consistency 67.50 ± 15.82 -5.25 w/o Dynamic Pseudo Update 66.83 ± 15.66 -5.92 w/o Rhythmic State Calibration 67.92 ± 15.54 -4.83

2019-Stroke

###### PA-TCNet 66.56 ± 06.61 –

Source Only 63.85 ± 05.86 -2.71 w/o PGTC 64.58 ± 06.80 -1.98 w/o ROI Consistency 64.90 ± 04.36 -1.66 w/o Dynamic Pseudo Update 65.31 ± 08.67 -1.25 w/o Rhythmic State Calibration 66.15 ± 05.64 -0.41

XW-Stroke

ROI consistency reduced performance by 5.25% on 2019-Stroke and 1.66% on XW-Stroke, while removing dynamic pseudo-label updates caused drops of 5.92% and 1.25%, respectively. These observations confirm that physiological template matching and dynamic pseudo-label refresh jointly suppress cumulative pseudo-supervision errors.

Removing rhythmic state calibration reduced the model to a standard Mamba-style temporal state model and led to decreases of 4.83% on 2019-Stroke and 0.41% on XW-Stroke. This result supports our hypothesis that stroke EEG exhibits pronounced frequency-scale heterogeneity, namely slowly varying pathological trends together with transient ERD-related perturbations, and that explicitly injecting slowly evolving pathological context into state propagation helps preserve informative motor-intention cues under strong low-frequency drift.

### 4.4 Hyperparameter Sensitivity Analysis

To evaluate the stability of PA-TCNet with respect to key parameters, we analyzed the pseudo-label confidence threshold τp, the warm-up duration Ew, and the lower bound of the physiological threshold δmin on both datasets. We also compared different network depths and embedding dimensions.

- Fig. 4 shows that both τp and δmin exhibit an approximately inverted-U performance trend. A smaller τp relaxes pseudo-label activation too much, whereas a larger τp reduces target-domain supervision coverage. This trade-off motivates the default value of 0.60. For δmin, overly small values make physiological filtering too permissive, while overly large values reject too many genuine stroke samples whose ERD patterns are naturally weakened by pathology. The relatively stable performance region around 0.4–0.6 indicates that the model must balance physiological priors against pathological variability. For warm-up duration, a too-small Ew introduces unstable pseudo-labels too early, whereas a too-large Ew delays target adaptation. The best settings were 25 epochs for XW-Stroke and 10 epochs for 2019-Stroke. In addition, the best-performing model depth was 2 and the best embedding dimension was 30, suggesting that the effective information flow in post-stroke EEG remains relatively low-dimensional and that overly complex models are more prone to overfitting patient-specific noise.

### 4.5 Noise Robustness Test

In real rehabilitation scenarios, stroke patients are often accompanied by limb spasticity, sweating-induced impedance changes, and other sources of signal contamination. To assess robustness, we injected baseline drift that simulates polarization-voltage offset and transient spike noise that simulates muscle spasm into the test data. As shown in Fig. 5, all performance metrics inevitably decreased as disturbance intensity increased, but PA-TCNet exhibited a relatively smooth degradation trend. In particular, the model remained highly resistant to transient spike noise. This behavior can be attributed to the dual-branch decomposition in PRSM, where high-frequency spikes are largely isolated in the fast-detail pathway instead of causing global hidden-state collapse. By contrast, drift noise caused slightly stronger degradation because low-frequency drift is more easily entangled with the intrinsic pathological slow waves of stroke EEG, increasing the difficulty of rhythmic decomposition. Overall, the results indicate that PA-TCNet preserves continuous and interpretable performance evolution under disturbed conditions.

### 4.6 Physiological Interpretability Analysis

Because 2019-Stroke does not provide demographic metadata, this analysis is mainly based on XW-Stroke. Higher decoding performance of PA-TCNet was primarily observed in patients with shorter disease duration and milder

[Figure 3]

- Figure 3: t-SNE visualizations of feature distributions on the XW-Stroke (top) and 2019-Stroke (bottom) datasets at different stages of PA-TCNet.

neurological deficit: the group with disease duration ≤ 3 years achieved 68.67%, compared with 63.06% for the group with disease duration > 3 years; the group with NIHSS ≤ 3 reached 67.50%, compared with 64.29% for NIHSS > 3. Moreover, the five best-performing patients all fell within the range of 1–3 years of disease duration and NIHSS scores between 1 and 3. These results suggest that the model is particularly effective when residual sensorimotor discriminative structure is still preserved in stroke EEG.

This tendency is consistent with the roles of the two proposed modules. PRSM is designed to recover weak lateralized ERD cues when post-stroke µ/β desynchronization is weakened and partially masked by slowly varying pathological rhythms. PGTC incorporates left, midline, right, and asymmetry patterns into the ROI constraint, thereby suppressing high-confidence pseudo-labels that do not match plausible sensorimotor topology. As a result, the gain of PA-TCNet mainly comes from extracting and amplifying residual sensorimotor discriminative structure rather than from purely statistical alignment.

### 4.7 Limitations and Future Directions

Although PA-TCNet was validated on two public stroke EEG datasets, the present study should still be regarded as an initial exploration of stroke-physiology-constrained cross-subject decoding. First, publicly available stroke EEG data remain limited in scale. In particular, XW-Stroke consists of acute-stroke recordings with substantial heterogeneity, and the current study could only validate the method on a screened subcohort rather than on the entire population. The relatively large standard deviations observed in some cross-subject results also suggest that decoding performance remains sensitive to inter-patient variability, which is consistent with the marked heterogeneity of stroke populations in terms of lesion condition, functional impairment, and neurophysiological reorganization. Therefore, the current conclusions still have limited external validity across broader ranges of disease duration, severity, and functional status.

[Figure 4]

Figure 4: Hyperparameter sensitivity analysis of PA-TCNet on XW-Stroke and 2019-Stroke.

Second, because the public datasets do not provide sufficiently complete metadata, this study is not able to perform a more systematic stratified analysis involving lesion hemisphere, lesion location, lesion volume, and finer-grained functional scores, nor could we build a more direct lesion-aware individualized modeling framework. Third, although the method was evaluated on two heterogeneous public datasets, rigorous cross-center validation, stability analysis under different acquisition devices and protocols, and long-term online adaptation in closed-loop rehabilitation settings all remain to be investigated. Finally, the present work uses a fixed sensorimotor ROI template as the physiological prior. This design provides an interpretable and stable weak constraint for target-domain supervision, but it cannot fully capture the complex individualized functional reorganization that occurs after stroke. The practical value of PA-TCNet lies in providing a more stable cross-subject initialization for patient-specific rehabilitation BCIs, rather than replacing clinical assessment or neurological judgment. Future work should therefore combine larger multi-center datasets, richer lesion-level information, online rehabilitation paradigms, more comprehensive evaluation protocols, and lower-burden wearable EEG acquisition settings to further advance clinically usable and deployable stroke MI-BCI systems [30–32].

## 5 Conclusion

This paper proposed PA-TCNet for cross-subject MI-BCI decoding in stroke patients to address two coupled challenges: pathology-induced temporal representation mismatch and unreliable target-domain pseudo-supervision. PRSM enhances the representation of abnormal temporal dynamics through rhythmic decomposition, context construction, and state modulation, whereas PGTC improves the reliability of target supervision by screening and dynamically updating pseudolabels using source-domain ROI physiological templates. Experimental results showed that PA-TCNet achieved the best performance under the LOSO protocol and maintained consistent advantages in ablation analysis, hyperparameter sensitivity evaluation, noise robustness testing, and feature visualization. Overall, the study shows that pathology-aware temporal modeling and physiology-guided target refinement synergistically enhance the discriminability, stability, and practical robustness of cross-subject stroke MI decoding. This framework further offers a clinically meaningful approach for integrating neurophysiological priors into deep learning-based BCI systems for post-stroke rehabilitation.

[Figure 5]

Figure 5: Noise robustness of PA-TCNet under drift and spike perturbations.

## References

- [1] Valery L Feigin, Michael Brainin, Bo Norrving, Sheila Martins, Ralph L Sacco, Werner Hacke, Marc Fisher, Jeyaraj Pandian, and Patrice Lindsay. World stroke organization (wso): Global stroke fact sheet 2022. International

- Journal of Stroke, 17(1):18–29, 2022. PMID: 34986727.
- [2] Richard D. Wilson, Stephen J. Page, Michael Delahanty, Jayme S. Knutson, Douglas D. Gunzler, Lynne R. Sheffler, and John Chae. Upper-limb recovery after stroke: A randomized controlled trial comparing emg-triggered, cyclic, and sensory electrical stimulation. Neurorehabilitation and Neural Repair, 30(10):978–987, 2016. PMID: 27225977.
- [3] Bin Jiang, Xiangkai Wang, Dongyi He, Siyu Cheng, Maoyu Liao, Duoqian Miao, Qingling Xia, Yun Zhao, and Gen Li. A comprehensive review of deep learning for motor imagery eeg: From healthy subjects to patients. Biomedical Signal Processing and Control, 117:109680, 2026.
- [4] Yuhuang Lin, Yong Yuan, Jingjing Chen, and Xiangfu Lin. Motor imagery combined with brain-computer interface for stroke patients: a meta-analysis. Frontiers in Neurology, Volume 17 - 2026, 2026.
- [5] Reza Abiri, Soheil Borhani, Eric W Sellers, Yang Jiang, and Xiaopeng Zhao. A comprehensive review of eeg-based brain–computer interface paradigms. Journal of Neural Engineering, 16(1):011001, jan 2019.
- [6] G. Pfurtscheller and C. Neuper. Motor imagery and direct brain-computer communication. Proceedings of the IEEE, 89(7):1123–1134, 2001.
- [7] Vernon J Lawhern, Amelia J Solon, Nicholas R Waytowich, Stephen M Gordon, Chou P Hung, and Brent J Lance. Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces. Journal of Neural Engineering, 15(5):056013, jul 2018.
- [8] Robin Tibor Schirrmeister, Jost Tobias Springenberg, Lukas Dominique Josef Fiederer, Martin Glasstetter, Katharina Eggensperger, Michael Tangermann, Frank Hutter, Wolfram Burgard, and Tonio Ball. Deep learning with convolutional neural networks for eeg decoding and visualization. Human Brain Mapping, 38(11):5391–5420, 2017.
- [9] Jiaheng Wang, Lin Yao, and Yueming Wang. Ifnet: An interactive frequency convolutional neural network for enhancing motor imagery decoding from eeg. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31:1900–1911, 2023.
- [10] Yonghao Song, Qingqing Zheng, Bingchuan Liu, and Xiaorong Gao. Eeg conformer: Convolutional transformer for eeg decoding and visualization. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 31:710–719, 2023.
- [11] Wei Zhao, Baocan Zhang, Haifeng Zhou, Dezhi Wei, Chenxi Huang, and Quan Lan. Multi-scale convolutional transformer network for motor imagery brain-computer interface. Scientific Reports, 15(1):12935, Apr 2025.
- [12] Ziwei Wang, Hongbin Wang, Tianwang Jia, Xingyi He, Siyang Li, and Dongrui Wu. Dbconformer: Dual-branch convolutional transformer for eeg decoding. IEEE Journal of Biomedical and Health Informatics, pages 1–14, 2025.
- [13] Guorui Lu, Jing Peng, Bingyuan Huang, Chang Gao, Todor Stefanov, Yong Hao, and Qinyu Chen. Slimseiz: Efficient channel-adaptive seizure prediction using a mamba-enhanced network. In 2025 IEEE International Symposium on Circuits and Systems (ISCAS), pages 1–5, 2025.
- [14] Peiyin Chen, Xiaofeng Liu, Chao Ma, He Wang, Xiong Yang, Celso Grebogi, Xiao Gu, and Zhongke Gao. Unsupervised domain adaptation with synchronized self-training for cross- domain motor imagery recognition. IEEE Journal of Biomedical and Health Informatics, 29(5):3664–3677, 2025.
- [15] Yici Liu, Qi Wei Oung, and Hoi Leong Lee. Ssas: Cross-subject eeg-based emotion recognition through source selection with adversarial strategy. Expert Systems with Applications, 308:130843, 2026.
- [16] Jian Shen, Lechun You, Yu Ma, Zeguang Zhao, Huajian Liang, Yanan Zhang, and Bin Hu. Ua-daan: An uncertaintyaware dynamic adversarial adaptation network for eeg-based depression recognition. IEEE Transactions on Affective Computing, 16(3):2130–2141, 2025.
- [17] Rongrong Lu, Wenchang Deng, Tianhao Gao, Songhua Huang, Zhi Zhang, Yan Liu, and Sheng-hua Zhong. Mutual generation for cross-domain challenge in stroke patients’ motor imagery classification and functional recovery prediction. IEEE Journal of Biomedical and Health Informatics, pages 1–14, 2025.
- [18] Milakul Hasana Mim, Debjoty Roy Pranto, and Md Mehedi Hasan. Fa-eegnet: Enhancing eegnet with frequencyadaptive kernels for the classification of stroke rehabilitation movements. In 2026 5th International Conference on Electrical, Computer & Telecommunication Engineering (ICECTE), pages 1–6, 2026.
- [19] Ivana Kancheva, Sandra M. A. van der Salm, N. Ramsey, and M. Vansteensel. Association between lesion location and sensorimotor rhythms in stroke – a systematic review with narrative synthesis. Neurological Sciences, 44:4263

– 4289, 2023.

- [20] Fangzhou Xu, Yuandong Wang, Han Li, Xin Yu, Chongfeng Wang, Ming Liu, Lin Jiang, Chao Feng, Jianfei Li, De quan Wang, Zhiguo Yan, Yang Zhang, and Jiancai Leng. Time-varying effective connectivity for describing the dynamic brain networks of post-stroke rehabilitation. Frontiers in Aging Neuroscience, 14, 2022.
- [21] N. Rustamov, Joseph B. Humphries, A. Carter, and E. Leuthardt. Theta–gamma coupling as a cortical biomarker of brain–computer interface-mediated motor recovery in chronic stroke. Brain Communications, 4, 2022.
- [22] Vera Kaiser, Ian Daly, Floriana Pichiorri, Donatella Mattia, Gernot R. Müller-Putz, and Christa Neuper. Relationship between electrical brain responses to motor imagery and motor impairment in stroke. Stroke, 43(10):2735– 2740, 2012.
- [23] Chayanin Tangwiriyasakul, Victor Mocioiu, Michel J A M van Putten, and Wim L C Rutten. Classification of motor imagery performance in acute stroke. Journal of Neural Engineering, 11(3):036001, apr 2014.
- [24] Ivana Kancheva, Sandra M. A. van der Salm, Nick F. Ramsey, and Mariska J. Vansteensel. Association between lesion location and sensorimotor rhythms in stroke – a systematic review with narrative synthesis. Neurological Sciences, 44(12):4263–4289, Dec 2023.
- [25] Aaqib Raza and Mohd Zuki Yusoff. An maml-based lightweight neural network with domain adaptation for cross-subject and generalized eeg-based motor imagery classification. IEEE Sensors Letters, 10(2):1–4, 2026.
- [26] Zafer Keser, Samuel C. Buchl, Nathan A. Seven, M. Markota, H. Clark, David T. Jones, G. Lanzino, Robert D. Brown, G. Worrell, and B. Lundstrom. Electroencephalogram (eeg) with or without transcranial magnetic stimulation (tms) as biomarkers for post-stroke recovery: A narrative review. Frontiers in Neurology, 13, 2022.
- [27] Haijie Liu, Penghu Wei, Haochong Wang, Xiaodong Lv, Wei Duan, Meijie Li, Yan Zhao, Qingmei Wang, Xinyuan Chen, Gaige Shi, Bo Han, and Junwei Hao. An eeg motor imagery dataset for brain computer interface in acute stroke patients. Scientific Data, 11(1):131, Jan 2024.
- [28] Tianyu Jia. Eeg data of motor imagery for stroke, 2 2019.
- [29] Laurens van der Maaten and Geoffrey Hinton. Visualizing data using t-sne. Journal of Machine Learning Research, 9(86):2579–2605, 2008.
- [30] Dongyi He, Wai Ting Siok, and Nizhuan Wang. Toward robust, reproducible, and widely accessible intracranial language brain-computer interfaces: A comprehensive review of neural mechanisms, hardware, algorithms, evaluation, clinical pathways and future directions, 2026.
- [31] Yueyang Li, Weiming Zeng, Wenhao Dong, Di Han, Lei Chen, Hongyu Chen, Zijian Kang, Shengyu Gong, Hongjie Yan, Wai Ting Siok, and Nizhuan Wang. A tale of single-channel electroencephalography: Devices, datasets, signal processing, applications, and future directions. IEEE Transactions on Instrumentation and Measurement, 74:1–20, 2025.
- [32] Junlin Wang, Xiaodong Li, Xingyu Lu, Ningbo Fei, Wei Huang, and Yong Hu. A somatosensory erp-bci system for post-stroke hand function rehabilitation applications. IEEE Transactions on Instrumentation and Measurement, 75:1–12, 2026.

