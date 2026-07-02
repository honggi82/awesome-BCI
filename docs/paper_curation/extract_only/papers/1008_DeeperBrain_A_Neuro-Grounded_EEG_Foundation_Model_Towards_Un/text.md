# DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI

[Figure 1]

Jiquan Wang, Sha Zhao, Yangxuan Zhou, Yiming Kang, Shijian Li, Gang Pan, Senior Member, IEEE

## arXiv:2601.06134v2[cs.LG]19Mar2026

Abstract—Electroencephalography (EEG) foundation models hold significant promise for universal Brain-Computer Interfaces (BCIs). However, existing approaches often rely on end-to-end fine-tuning and exhibit limited efficacy under frozen-probing protocols, lacking the intrinsic universality required for broad generalization. This limitation stems from adapting generalpurpose sequence architectures that overlook the biophysical and dynamical principles of neural activity. To bridge this gap, we propose DeeperBrain, a neuro-grounded foundation model integrating domain-specific inductive biases into its model design and learning objectives. Architecturally, DeeperBrain incorporates a volume conduction-aware channel encoding to model spatial mixing via 3D geometry, and a neurodynamicsaware temporal encoding capturing slow adaptations using oscillatory and exponential bases. For pretraining, we introduce a dual-objective strategy combining Masked EEG Reconstruction (MER) for local fidelity and Neurodynamics Statistics Prediction (NSP). NSP enforces alignment with macroscopic brain states by predicting interpretable order parameters, including spectral power, functional connectivity, cross-frequency coupling, and dynamic complexity. Extensive experiments demonstrate that DeeperBrain achieves state-of-the-art or highly competitive performance under end-to-end fine-tuning. Crucially, it maintains superior efficacy under a rigorous frozen-probing protocol, verifying that embedding neuroscientific first principles endows learned representations with the intrinsic universality essential for universal BCI. The code will be publicly available.

Index Terms—EEG, EEG foundation model, EEG decoding, BCI, Neurophysiology.

I. INTRODUCTION

Brain-Computer Interfaces (BCIs) establish direct communication pathways between the central nervous system and external devices [1–3]. Electroencephalography (EEG)

This work was supported in part by STI 2030 Major Projects under Grant 2021ZD0200400, in part by National Natural Science Foundation of China under Grant 62476240, in part by the Key Program of the Natural Science Foundation of Zhejiang Province, China, under Grant LZ24F020004, and in part by the Fundamental Research Funds for the Central Universities under Grant 226-2025-00122. (Jiquan Wang and Sha Zhao contributed equally to this work.) (Corresponding author: Sha Zhao.)

Jiquan Wang is with the State Key Laboratory of Brain-machine Intelligence, Zhejiang University, Hangzhou 311121, Zhejiang, China (e-mail: wangjiquan@zju.edu.cn)

Sha Zhao, Yangxuan Zhou, Yiming Kang, and Shijian Li are with the State Key Laboratory of Brain-machine Intelligence, Zhejiang University, Hangzhou 311121, Zhejiang, China, and the College of Computer Science and Technology, Zhejiang University, Hangzhou 310013, Zhejiang, China (e-mail: szhao@zju.edu.cn; zyangxuan@zju.edu.cn; kangyiming@zju.edu.cn; shijianli@zju.edu.cn).

Gang Pan is with the State Key Laboratory of Brain-machine Intelligence, Zhejiang University, Hangzhou 311121, Zhejiang, China, the College of Computer Science and Technology, Zhejiang University, Hangzhou 310013, Zhejiang, China and the MOE Frontier Science Center for Brain Science and Brain-machine Integration, Hangzhou 310063, Zhejiang, China (e-mail: gpan@zju.edu.cn)

serves as the predominant non-invasive modality for BCI systems, capable of capturing macroscopic cortical activity with millisecond-level temporal resolution, high portability, and cost-efficiency. Consequently, EEG has become the cornerstone of critical applications such as motor imagery [4, 5], affective state recognition [6–8], epilepsy diagnosis [9, 10], sleep staging [11–13], consciousness assessment [14, 15], and depression detection [16, 17]. However, achieving universal BCI remains challenging, impeded by the multifaceted heterogeneity of neural data. At the signal level, recordings are inherently non-stationary and suffer from low signal-tonoise ratios, stemming from anatomical variability [18] and pervasive artifacts like muscle activity and line noise [19–22]. Physically, diverse acquisition hardware employing varying channel counts and reference schemes induces inconsistent spatial alignments across datasets [23]. Compounding these discrepancies is the functional heterogeneity of BCI paradigms themselves, which recruit divergent neural mechanisms ranging from frequency-specific sensorimotor rhythms to complex, widespread network oscillations. These factors collectively prevent cross-scenario generalization, necessitating extensive adaptation to novel deployment contexts and hindering the realization of universal BCI systems.

Inspired by the success of large language and vision models [24–27], the field has increasingly turned toward EEG foundation models to learn universal representations from vast unlabeled corpora [28–32]. These approaches typically employ self-supervised strategies like masked signal reconstruction. Despite their statistical capacity, these data-driven models rely on end-to-end fine-tuning to adapt to downstream tasks yet frequently exhibit limited efficacy under a frozen-probing protocol [33–35]. We argue that establishing robust performance in this frozen setting, where the pretrained backbone remains fixed, is a prerequisite for universal BCI. It serves as a critical benchmark for validating whether learned representations capture genuinely invariant neurophysiological mechanisms rather than scenario-specific statistics. We attribute the current deficiency to the reliance on generic sequence modeling assumptions. By prioritizing data-driven patterns while underutilizing the distinct biophysical and dynamical principles governing neural activity, existing architectures yield representations that lack intrinsic universality.

This limitation stems from neglecting the structured physical processes that define EEG. Two core principles shape this structure. First, spatial organization is dictated by volume conduction, where passive current spread creates spatially blurred, distance-dependent correlations among electrodes [36]. Second, temporal organization exhibits a hier-

archy spanning from millisecond-level oscillations to secondlevel cognitive adaptations [37, 38]. Furthermore, from a dynamical systems perspective, macroscopic brain function is governed by low-dimensional order parameters [39, 40]. Key statistics like spectral power [37], functional connectivity [41], cross-frequency coupling [42], and dynamic complexity [43] constitute the stable, interpretable features of brain states. Neglecting these priors yields neurobiologically agnostic representations, which necessitates extensive parameter updates to recover meaningful features, thereby hindering the emergence of the intrinsic universality required for robust frozen-probing.

To bridge this gap, we propose to integrate neurophysiological principles directly into the foundation model design at both the architectural and objective levels. We introduce DeeperBrain, a neuro-grounded EEG foundation model that leverages domain-specific inductive biases to guide representation learning. Architecturally, DeeperBrain incorporates a channel positional encoding that models volume conduction via 3D electrode geometry and a learnable spatial decay kernel, alongside a temporal positional encoding that uses oscillatory and exponential decay bases to capture slow modulations and adaptation. For pretraining, we devise a dualobjective framework combining Masked EEG Reconstruction (MER) with Neurodynamics Statistics Prediction (NSP). While MER preserves local signal fidelity, NSP enforces alignment with macroscopic brain states by predicting interpretable statistics derived from the full signal. By explicitly modeling these physical and dynamical constraints, DeeperBrain aligns representations with underlying neural dynamics. This fosters intrinsic universality, enabling robust performance even in the frozen-probing setting without further adaptation.

Our main contributions are summarized as follows:

- 1) DeeperBrain: A Neuro-Grounded EEG Foundation Model. We propose DeeperBrain, a foundation model that systematically incorporates neurophysiological principles into its model design and learning objective, facilitating generic representation learning across diverse EEG domains towards universal BCI.
- 2) Neurophysiologically Grounded Model Design. We introduce two inductive biases aligned with EEG biophysics: (i) a volume conduction-aware channel positional encoding that models spatial mixing via 3D geometry, and (ii) a neurodynamics-aware temporal positional encoding that captures slow oscillations and adaptive dynamics via biologically plausible bases.
- 3) Neurodynamics-Guided Pretraining. We introduce a dual-objective strategy optimizing both masked EEG reconstruction and neurodynamics statistics prediction. It ensures the learned representations capture both finegrained waveform details and high-level dynamical order parameters essential for defining brain states.
- 4) Universal Representation. Pretrained on 14 diverse datasets, DeeperBrain achieves state-of-the-art or competitive performance on a wide range of downstream tasks. Notably, it maintains superior performance even under the frozen-probing protocol, verifying the universality and transferability of its learned features.

II. RELATED WORK

- A. Traditional EEG Decoding

Electroencephalography (EEG) decoding aims to infer cognitive, affective, or pathological states from scalp-recorded electrical activity. Early methodologies predominantly relied on handcrafted features, including time-domain statistics, spectral power, and connectivity measures, coupled with classifiers such as support vector machines or linear discriminant analysis [44–47]. These approaches necessitate extensive domain expertise and often exhibit limited generalization across diverse subjects and recording conditions.

The emergence of deep learning has shifted the field toward end-to-end representation learning [48]. Numerous studies now employ deep architectures to automate feature extraction from raw or minimally processed EEG [49–53]. Convolutional Neural Networks (CNNs) have been widely adopted to capture local spatiotemporal patterns, with architectures such as DeepConvNet [54], C2CM [55], EEGNet [56], and TSception [57] demonstrating efficacy in motor imagery, emotion recognition, and seizure detection [58]. To model long-range temporal dependencies, Recurrent Neural Networks (RNNs), particularly Long Short-Term Memory (LSTM) networks, have been applied to tasks including sleep staging and BCI control [59, 60]. Hybrid CNN-LSTM models further combine local feature extraction with sequential modeling for applications such as sleep staging and emotion recognition [61–65].

More recently, the Transformer architecture has been introduced to EEG analysis, utilizing self-attention to model global spatiotemporal interactions without fixed convolutional inductive biases [66–69]. Several works integrate CNNs and Transformers to jointly exploit local invariance and global context [70–74]. Graph Neural Networks (GNNs) have also been explored to explicitly model inter-channel relationships using predefined or learned connectivity structures [75–77]. Despite success on specific benchmarks, these supervised methods face fundamental limitations: the high cost of acquiring labeled data and poor cross-dataset generalization due to variations in hardware, montage, and physiology. This has motivated the shift toward self-supervised pretraining.

- B. EEG Foundation Models

Foundation models have revolutionized vision, language, and multimodal learning [24, 78–83]. Extending this paradigm to time series, general-purpose models have been proposed for domains including climate, finance, and traffic [84–88], with a subset targeting neural signals.

In the EEG domain, early self-supervised efforts focused on pretext tasks to extract invariant representations from unlabeled data [89]. BENDER [90] employs contrastive learning on generic EEG embeddings, while MAEEG [91] utilizes a masked autoencoder framework for signal reconstruction. Subsequent works extended these concepts to intracranial recordings: BrainBERT [92] reconstructs masked spectrograms of stereo-EEG, and Brant [93] introduces a Transformer-based model for long-term dependency modeling. Its extensions, Brant-2 [94] and Brant-X [95], further incorporate scalp EEG and multi-modal physiological alignment.

Patching and Masking Patch and Positional Embedding

Spatiotemporal Transformer Encoder

Dual Pretraining Objectives

Ground Truth EEG

[Figure 2]

[Figure 3]

Volume Conduction

Channel Reorganization

[Figure 4]

[Figure 5]

Transformer Encoder Layers

| |
|---|

Masked EEG Reconstuction

MER Head

Raw EEG

| |
|---|

Patching

Add

3D Electrode Coordinates

Channel PE

Reconstructed Patches

FFN

Channels

| |
|---|

Temporal Conv

Total Loss

Pre-Norm

| |
|---|

| |
|---|

| |
|---|

| |
|---|

seconds

NSP Head

Add

[Figure 6]

Predicted Statistics

Random Masking

Representations

Patch Embeddings

Input Tokens

Multi-Head Attention

Neurodynamics Statistics Prediction

Neurodynamics Statistics

Slow Oscillatory & Adaptive Basis

[Figure 7]

[Figure 8]

[Figure 9]

Pre-Norm

Linear Projection

Phase-Locking Value

Relative Spectral Power

[Figure 10]

[Figure 11]

Masked Patches

Temporal PE

Cross-Frequency Coupling

Sample Entropy

Fig. 1. DeeperBrain overview.

Recent research has increasingly targeted scalp EEG. BIOT [96] employs a linear transformer for joint pretraining across diverse biosignals. EEG2Rep [97] predicts masked segments in a latent space, and LaBraM [98] introduces neural token prediction for EEG patches. Neuro-GPT [99] utilizes a decoder-only architecture with autoregressive pretraining, while EEGPT [100] employs a dual objective for universal feature extraction. Approaches such as NeuroLM [101], UniMind [102], and ELASTIQ [103] explore harnessing Large Language Models (LLMs) by treating EEG as a foreign language. Architecturally, CBraMod [104] uses criss-cross attention with asymmetric positional encoding, EEGMamba [105] and CodeBrain [106] leverage state space models for spatiotemporal dependencies, and LUNA [107] unifies diverse electrode layouts via learned queries. Other innovations include mixture-of-experts in NeurIPT [108], structured sparse attention in CSBrain [109], discrete tokenization in BrainOmni [110], and massive-scale pretraining in REVE [111].

While these models improve transferability, they predominantly adapt generic architectures from vision or language. Lacking explicit biophysical constraints, they rely heavily on end-to-end fine-tuning and typically struggle under frozenprobing protocols [33–35].

III. METHOD A. Overview

DeeperBrain is a neuro-grounded foundation model designed to learn universal representations from unlabeled EEG. As illustrated in Fig. 1, the pipeline begins by partitioning the channel-reorganized EEG signal into non-overlapping spatiotemporal patches. A random subset of these patches is masked, while the visible ones are projected into dense tokens via a temporal convolutional backbone. To inject biophysical inductive biases, we augment these tokens with two domain-

specific positional encodings: a channel encoding that models volume conduction using 3D electrode geometry, and a temporal encoding that captures slow oscillatory and adaptive dynamics. These tokens are then processed by a Transformer encoder to model global dependencies. Finally, DeeperBrain is optimized via a dual-objective strategy: Masked EEG Reconstruction (MER) to preserve local signal fidelity, and Neurodynamics Statistics Prediction (NSP) to enforce alignment with macroscopic neural principles, including spectral organization and functional connectivity.

B. Patching and Masking Strategy

To enhance robustness to variable electrode montages and promote generalization across heterogeneous datasets, we introduce a stochastic channel reorganization step. Let the raw EEG be denoted as X ∈ R C×T, where C is the original channel count and T represents time samples. For each training instance, we randomly permute the channel order to eliminate positional bias and select a subset of size C ∈ [1, C] to simulate variable-density recordings. This yields the reorganized signal:

X = channel_reorganization( X) ∈ RC×T. (1)

By treating C as a stochastic variable, the model learns to handle arbitrary channel configurations during both pretraining and inference.

The reorganized signal X is partitioned into nonoverlapping one-second segments. Given a sampling frequency fs, each segment contains P = fs points. We reshape the signal into a 3D tensor:

Xpatch ∈ RC×S×P, (2) where S = T/P denotes the number of temporal segments. Each vector Xc,s,: ∈ RP constitutes a (channel × second) patch, serving as the atomic unit for self-supervised learning.

During pretraining, we employ a random patch-wise masking strategy. For each recording, a fraction µ (default µ = 0.5) of the total C × S patches is selected uniformly across channels and time. Masked patches are replaced with a fixed zero vector 0 ∈ RP in the raw voltage space rather than a learnable token, ensuring compatibility with the temporal convolutional embedding. This operation is defined by a binary mask M ∈ {0,1}C×S, where Mc,s = 1 indicates a masked patch. By masking entire (channel × second) units, we prevent the model from relying on local correlations and force it to reconstruct missing content using global spatiotemporal context, thereby preserving the integrity of unmasked neural dynamics.

C. Patch Embedding via Temporal Convolution

To transform raw voltage patches into dense, semantically rich embeddings, we utilize a lightweight temporal convolutional network. This backbone leverages the insight that each (channel × second) patch contains local temporal structures, such as oscillatory bursts and transient events, effectively captured by 1D convolutions. For efficient implementation, we reshape the masked input Xmask ∈ RC×S×P into R1×(CS)×P, treating the spatiotemporal grid as a set of independent 1D signals.

The embedding architecture comprises three sequential convolutional blocks designed to extract multi-scale features:

Etime = ConvBlock3 ◦ ConvBlock2 ◦ ConvBlock1(Xmask). (3)

Each ConvBlocki consists of a 2D convolution with kernel size (1,Ki) and stride (1,si), followed by Group Normalization (5 groups) and GELU activation. The first block employs a large kernel (K1 = 49, s1 = 25) to capture long-range dependencies and reduce sequence length, effectively mimicking delta–theta bandpass filtering. Subsequent blocks use small kernels (K2 = K3 = 3) with unit stride to refine local structures like alpha or beta bursts without further downsampling. This hierarchical design extracts both coarse and fine temporal features while maintaining computational efficiency.

The resulting feature tensor Etime ∈ RF×(CS)×L, with F = 25 output channels and length L, is flattened to yield the final patch embeddings:

E ∈ RC×S×D, (4)

where D = F ×L is the embedding dimension. These embeddings provide the initial token sequence for the Transformer encoder, encoding rich local temporal context while preserving the original spatiotemporal organization.

- D. Neurophysiologically Grounded Positional Encodings

Standard positional encodings in vision or language models assume either fixed geometric priors (e.g., 2D grid in ViT [112]) or purely learnable embeddings. While sufficient for many domains, EEG is governed by distinct biophysical laws. Explicitly modeling these principles can provide stronger inductive biases than generic learnable embeddings. To address this, we introduce two neurophysiologically grounded positional encodings that explicitly embed the physics of EEG generation into the model architecture.

Channel Positional Encoding: Modeling Volume Conduction. Scalp EEG potentials arise from the passive spread of electrical currents through the head’s conductive tissues, a process known as volume conduction [36]. Under the quasistatic approximation of Maxwell’s equations, the potential ϕ(r) at scalp location r due to a current dipole q at source location rs is:

q · (r − rs) ∥r − rs∥3

1 4πσ

, (5)

ϕ(r) =

where σ is the effective conductivity of head tissues. This implies that signal similarity decays with physical distance between electrodes, inducing strong spatial correlations among nearby sensors.

To model this, we leverage 3D electrode coordinates Pch ∈ RC×3 in a standardized anatomical space (e.g., MNI, in meters). Pairwise Euclidean distances are computed as Dij = ∥pi − pj∥2. Inspired by the exponential decay observed in volume conduction models [113], we define a learnable spatial kernel:

Dij τ

Kij = exp −

, τ = softplus(α) + ϵ, (6)

where α is a learnable parameter controlling the decay scale τ > 0, initialized to correspond to a typical inter-electrode distance (8 cm).

From a biophysical perspective, EEG can be modeled as a linear mixture x = As + ϵ, where A ∈ RC×Q is the lead field matrix and s denotes source activity. Under isotropic and uncorrelated sources (E[ss⊤] = I), the covariance of observed signals satisfies Σij ∝ exp(−∥pi−pj∥/τ) [36]. Our kernel Kij thus approximates this expected spatial correlation structure. To ensure stable aggregation, we normalize each row of the kernel to form a convex combination:

#### Kij

K¯ ij =

. (7)

C k=1 Kik + ϵ

The smoothing operation

p˜i =

C

K¯ ijpj (8)

j=1

embeds each electrode in a functional coordinate system, where its effective position is a weighted average of all electrodes’ anatomical locations, with weights determined by physical proximity. This mimics the volume-conducted mixing of neural sources and produces a spatially contextualized position vector for each channel. Finally, p˜i is projected to the embedding dimension D via a linear layer and added to the patch embeddings, endowing the model with an inductive bias aligned with EEG physics.

Temporal Positional Encoding: Capturing Slow Modulations and Adaptation. While temporal convolutional patch embeddings capture fine-grained oscillations, higher-order brain states involve slower modulations spanning seconds to minutes, including alpha power fluctuations and adaptation to sustained stimuli [37, 38]. These dynamics provide critical temporal context. However, generic positional encodings, including standard sinusoidal and learnable embeddings, treat time indices as symmetric dimensions or arbitrary markers.

They lack inductive biases for the ”arrow of time,” failing to capture the dissipative nature of neural adaptation. To model this cross-second structure, we design a temporal positional encoding operating at second-level granularity that combines two biologically inspired bases:

Slow oscillatory basis: We model periodic modulations in the range of 0.01–0.5 Hz, corresponding to time scales from 2 seconds (0.5 Hz) to 100 seconds (0.01 Hz). For each fixed frequency fk in this range, we include sine and cosine components:

ψkosc(t) = [sin (2πfkt) , cos (2πfkt)] , (9)

where t ∈ {1,...,S} denotes absolute time in seconds. This band captures slow cognitive and experimental-state fluctuations, such as block-wise attentional engagement or sleep stage transitions, that persist even after high-pass filtering of raw EEG. Frequencies are pre-defined on a logarithmic scale to prioritize behaviorally relevant low frequencies, providing a stable inductive bias without learnable parameters.

Adaptive decay basis: To model neural adaptation or temporal forgetting over tens of seconds, we include exponential decay functions with fixed rates dm:

ψmdec(t) = exp (−dmt) . (10)

This is grounded in the observation that neural responses to sustained input often follow r(t) ∝ e−t/τ [38], where τ = 1/dm is the adaptation time constant. The decay rates are pre-defined to span τ ∈ [1,100] seconds, covering sensory adaptation (seconds) to cognitive maintenance (tens of seconds), and are held fixed during training.

The full temporal feature vector for time step t is the concatenation:

ψ(t) = ψ1osc(t), . . . , ψKosc(t), ψ1dec(t), . . . , ψMdec(t) ∈ R2K+M.

(11)

This vector is linearly projected to D dimensions and broadcast across all channels. The fixed bases provide a principled, non-adaptive temporal prior that complements the fast temporal features extracted by the convolutional backbone, enabling the Transformer to jointly model dynamics across multiple time scales. The resulting encoding is both biologically plausible and sufficiently expressive to capture the hierarchical temporal organization of real EEG signals.

- E. Spatiotemporal Transformer Encoder

The embedded spatiotemporal tokens Z(0) ∈ RN×D, with N = C × S patches and embedding dimension D, are processed by a stack of L Transformer encoder layers. While we adopt the standard pre-normalization architecture [114], its suitability for EEG stems from a fundamental alignment with the brain’s own computational principles: neural processing is inherently distributed (across regions) and dynamic (across time scales). The self-attention mechanism naturally models such long-range, flexible interactions, mirroring how distant brain areas coordinate via phase synchronization or crossfrequency coupling during cognition.

Formally, each layer follows the pre-normalization scheme [114]:

Z = Z(l−1) + MHA LN(Z(l−1)) , (12) Z(l) = Z + FFN LN( Z) , (13)

where MHA denotes multi-head self-attention and FFN a two-layer feedforward network with GELU activation. The attention operation enables each (channel,second) token to dynamically integrate information from all other spatiotemporal locations, effectively simulating functional connectivity across the cortical surface and over time. For instance, the model can learn to link frontal theta oscillations (associated with working memory maintenance) with parietal gamma bursts (linked to sensory binding), recapitulating known neurocognitive pathways.

The final output H = Z(L) ∈ RN×D thus yields a contextualized representation where each token encodes not only local neural dynamics (from the temporal convolutional embedding) but also its role within the global brain network. This joint modeling of space and time provides the inductive bias necessary for universal EEG decoding, without requiring explicit graph priors or fixed connectivity assumptions.

F. Masked EEG Reconstruction (MER)

Preserving fine-grained temporal fidelity is critical for identifying transient neural events, such as epileptic spikes, sleep spindles, and muscle artifacts, which are essential for clinical and cognitive decoding. Given the susceptibility of raw EEG to non-stationary noise and high-amplitude transients, we employ a masked signal reconstruction objective to recover local waveform details from global spatiotemporal context.

The contextualized token sequence H ∈ RN×D (N = C × S) from the Transformer encoder is mapped back to the raw voltage space via a lightweight reconstruction head. This head comprises a single linear layer without activation:

Xˆ flat = HWrecon⊤ + brecon ∈ RN×P, (14)

where Wrecon ∈ RP×D and brecon ∈ RP are learnable parameters, and P denotes the number of time samples per patch. The output is reshaped to restore the original spatiotemporal structure:

Xˆ ∈ RC×S×P. (15)

The reconstruction loss is calculated exclusively on masked patches to prevent trivial identity mapping. Let M = {(c,s) | Mc,s = 1} represent the set of masked indices, with M ∈ {0,1}C×S as the binary mask tensor. We utilize the Smooth L1 Loss (Huber loss) [115]:

P

### 1 |M| · P

ρ X ˆ c,s,p − Xc,s,p , (16)

LMER =

p=1

(c,s)∈M

- 1

- 2e2 if |e| < β,

(17)

ρ(e) =

β(|e| − 12β) otherwise,

where β = 1.0. This loss function balances mean squared error (MSE) for small residuals, enabling precise waveform recovery, with mean absolute error (MAE) for large residuals,

ensuring robustness against outliers such as EMG or EOG artifacts commonly found in real-world EEG. Optimizing LMER forces the model to learn representations grounded in the physical signal, capturing essential local details through context.

G. Neurodynamics Statistics Prediction (NSP)

While Masked EEG Reconstruction (MER) ensures local signal fidelity, it does not explicitly enforce the modeling of multi-scale dynamical structures defining brain states. To bridge this gap, we introduce Neurodynamics Statistics Prediction (NSP), a self-supervision paradigm grounded in dynamical systems theory [39, 40]. We conceptualize the brain as a high-dimensional nonlinear system whose macroscopic behavior is governed by a low-dimensional set of order parameters, representing stable, emergent collective variables [116].

Formally, let the latent neural state z(t) ∈ Rd evolve according to:

dz(t) dt

= F(z(t), u(t), t), (18)

where F is a nonlinear vector field and u(t) denotes external inputs. The observed EEG is a noisy projection:

x(t) = H(z(t)) + ϵ(t), (19)

with observation function H(·) and noise ϵ(t). While z(t) is high-dimensional, its emergent dynamics are characterized by macroscopic order parameters y(t) = Φ(z(t)), where Φ extracts stable features robust to microscopic perturbations [116].

Since z(t) is unobservable, we approximate y(t) directly from the EEG signal via a mapping Ψ(x(t)) ≈ y(t). In this work, Ψ(·) computes four neurophysiologically grounded statistics serving as proxies for canonical order parameters:

1. Relative Spectral Power: Local Oscillatory States. Spectral power distribution reflects the attractor landscape, with specific frequency bands linked to cognitive states [37]. We compute the Power Spectral Density (PSD) via real FFT:

2

P−1

x[t]e−j2πft/fs

PSD(f) =

, (20)

t=0

where fs is the sampling rate. Power is integrated over five canonical bands (delta to gamma) and normalized to a probability simplex:

PSD(f) df

pk = f∈bandk

, k = 1, . . . , 5. (21)

k′ f∈bandk′ PSD(f) df

This 5D vector quantifies the oscillatory order parameter.

2. Phase-Locking Value (PLV): Functional Integration. Phase synchronization measures large-scale functional integration [41]. For each band, we extract the analytic signal phase ϕc(t) via the Hilbert transform. The PLV between channels i and j is:

P

1 P

ej(ϕi(t)−ϕj(t)) . (22)

PLVij =

t=1

We summarize the C × C PLV matrix by the mean and standard deviation of its upper-triangular elements, yielding a 10D vector capturing global synchronization strength and variability.

3. Cross-Frequency Coupling (CFC): Hierarchical Coordination. CFC encodes coordination across temporal scales, such as theta–gamma interactions [42]. For canonical pairs (e.g., theta–gamma), we extract the low-frequency phase ϕlow(t) and high-frequency amplitude Ahigh(t), computing the modulation strength:

1 P

CFC =

P

cos(ϕlow(t)) · Ahigh(t). (23)

t=1

This 3D vector quantifies cross-scale coupling per patch.

4. Sample Entropy: Dynamic Complexity. Signal complexity reflects the richness of neural dynamics [43]. Sample entropy quantifies regularity:

SampEn(m, r) = − log

Cm+1(r) Cm(r)

, (24)

where Cm(r) is the fraction of similar m-point templates within tolerance r. With m = 2 and r = 0.2 × std(x), this yields a 1D measure of unpredictability.

These statistics form the target tensor YNS ∈ RC×S×19. The model infers these properties from the masked input Xmask via a linear prediction head:

Yˆ NS = HWNSP⊤ + bNSP ∈ RN×19. (25)

The NSP loss is computed using Smooth L1 Loss:

1 CS · 19 c,s,k

ρ Y ˆ NS,c,s,k − YNS,c,s,k . (26)

LNSP =

By targeting these universal principles, NSP encourages the learning of representations invariant to subject-specific conditions [117]. The total pretraining objective combines NSP with MER:

L = λMERLMER + λNSPLNSP, (27)

where λMER and λNSP are the coefficients of two objectives. This dual approach ensures DeeperBrain captures both physical signal fidelity and interpretable neurodynamical mechanisms.

H. Task-specific Prediction Head

To evaluate the learned representations on downstream tasks, we attach a task-specific prediction head to the Transformer output H ∈ RN×D (N = C × S). This head maps the spatiotemporal token sequence to target outputs, employing either global pooling or full-sequence flattening depending on the task’s temporal structure.

We assess performance under two protocols: (i) end-to-end fine-tuning of the entire model, and (ii) frozen-probing with the backbone frozen. The optimization objective is selected based on the task type. For classification, we minimize the cross-entropy loss. For regression tasks, we employ the Mean Squared Error (MSE) loss. This evaluation strategy enables a direct assessment of representation quality: strong performance in the frozen setting indicates that DeeperBrain learns universal features without relying on task-specific fine-tuning.

TABLE I OVERVIEW OF PRE-TRAINING DATASETS.

Datasets Rate # Channels Duration # Samples Total Duration TUEG (clean subset) [118] 256Hz 19 30s 1,109,545 9,246.2h PhysioNet 2018 [119, 120] 200Hz 6 30s 872,089 7,267.4h Raw EEG Data [121] 256Hz 64 5s 30,978 42.7h Siena Scalp EEG Database [119, 122] 256Hz 27 10s 50,749 140.8h ds006171 [123, 124] 1024Hz 128 5s 29,397 40.8h ds006317 [125, 126] 1000Hz 109 5s 44,708 62.1h ds006367 [127] 1000Hz 28 8s 29,929 66.5h ds006370 [128] 1000Hz 28 5s 67,953 94.4h ds006437 [129] 256Hz 64 5s 12,069 16.8h ds006446 [130–132] 2048Hz 64 5s 12,970 18.0h ds006466 [130, 131, 133] 1000Hz 64 5s 94,392 131.1h ds006480 [134, 135] 1000Hz 64 5s 51,572 71.6h ds006525 [136] 250Hz 128 5s 4,080 5.7h ds006547 [137] 500Hz 63 5s 28,222 39.2h

TABLE II OVERVIEW OF DOWNSTREAM BCI TASKS AND DATASETS.

BCI Tasks Datasets Rate # Channels Duration # Samples Label Train Val Test Emotion Recognition FACED [138] 250Hz 32 10s 10,332 9-class Sub 1-80 Sub 81-100 Sub 101-123

SEED-V [139] 1000Hz 62 1s 117,744 5-class Trials per session split 5:5:5 SEED-VII [140] 1000Hz 62 5s 55,561 7-class Trials per session split 10:5:5

Motor Imagery Classification PhysioNet-MI [1, 141] 160Hz 64 4s 9,837 4-class Sub 1-70 Sub 71-89 Sub 90-109 BCIC-IV-2a [142] 250Hz 22 4s 5,088 4-class Sub 1-5 Sub 6-7 Sub 8-9 SHU-MI [143] 250Hz 32 4s 11,988 2-class Sub 1-15 Sub 16-20 Sub 21-25

Sleep Staging ISRUC [144] 200Hz 6 30s 89,240 5-class Sub 1-80 Sub 81-90 Sub 91-100 Seizure Detection CHB-MIT [141, 145] 256Hz 16 10s 326,993 2-class Sub 1-19 Sub 20-21 Sub 22-23 Imagined Speech Classification BCIC2020-3 [146] 256Hz 64 3s 6,000 5-class Predefined training, validation, and test Mental Disorder Diagnosis MODMA [147] 250Hz 128 15s 1,066 2-class 15MDD+18NC 4MDD+5NC 5MDD+6NC. Vigilance Estimation SEED-VIG [148] 200Hz 17 8s 20,355 regression Sub 1-15 Sub 16-19 Sub 20-23 Workload Estimation MentalArithmetic [141, 149] 500Hz 20 5s 1,707 2-class Sub 1-28 Sub 29-32 Sub 33-36

IV. EXPERIMENTS A. Pretraining Setup

1) Pretraining Datasets and Preprocessing: DeeperBrain is pretrained on a large-scale and highly diverse EEG corpus comprising 14 public datasets, totaling over 17,200 hours of recordings (2,438,653 non-overlapping samples), as summarized in Table I. This collection spans a wide spectrum of domains, including clinical diagnostics, sleep research, cognitive neuroscience, and perceptual tasks. It exhibits substantial heterogeneity in recording protocols, channel configurations (6 to 128 channels), sampling rates (200–2048 Hz), and epoch durations (5–30 seconds). Such diversity ensures that the model learns representations robust to variations in hardware, montage, and experimental design, a critical requirement for universal EEG decoding.

The corpus includes well-established benchmarks as well as recently released datasets:

- • TUEG [118]: A large clinical EEG archive. Due to pervasive artifacts and unmarked noise in the full release, we curated a clean subset of high-quality 30-second segments consistent with CBraMod [104].
- • PhysioNet 2018 [119, 120]: Sleep EEG from 994 subjects (training set only), annotated for sleep staging.
- • Raw EEG Data [121]: Recordings from cognitive task paradigms (information integration and rule-based categorization).
- • Siena Scalp EEG Database [119, 122]: EEG from epilepsy patients, originally recorded with 31 channels

but processed here using the standard 10–20 subset of 27 channels.

• Ten OpenNeuro datasets (ds006171, ds006317, ds006367, ds006370, ds006437, ds006446, ds006466, ds006480, ds006525, ds006547) [150]: A collection of contemporary cognitive and clinical EEG studies from the OpenNeuro platform, covering perceptual decision-making, emotional processing, resting-state, and motor imagery paradigms. These datasets vary widely in channel count (28–128) and sampling rate (250–2048 Hz), reflecting modern high-density and multi-center recording practices.

All recordings are preprocessed uniformly: (i) resampled to 200 Hz (except PhysioNet 2018, which is already at 200 Hz); (ii) band-pass filtered (0.3–75 Hz) to remove slow drifts and high-frequency noise; (iii) notch-filtered at 50/60 Hz to suppress power-line interference; (iv) segmented into nonoverlapping fixed-length samples as specified per dataset; and (v) normalized to a scale of 100 µV (i.e., divided by 100), so that values predominantly lie in [−1,1], following the convention in LaBraM [98].

This extensive and heterogeneous pretraining corpus enables DeeperBrain to internalize both the physical and dynamical principles of EEG, forming the basis for its strong generalization across downstream tasks.

2) Pre-training Settings: DeeperBrain is implemented in Python 3.13.5 using PyTorch 2.8.0 with CUDA 12.9 for GPU acceleration. The model is pretrained on a single machine equipped with an Intel Xeon Gold 6226R CPU and one

TABLE III PERFORMANCE COMPARISON WITH EXISTING METHODS UNDER END-TO-END FINE-TUNING.

##### FACED, 9-class SEED-V, 5-class SEED-VII, 7-class

Methods Bal. Acc. Kappa Weighted F1 Bal. Acc. Kappa Weighted F1 Bal. Acc. Kappa Weighted F1 EEGNet 40.90 ± 1.22 33.42 ± 2.51 41.24 ± 1.41 29.61 ± 1.02 10.06 ± 1.43 27.49 ± 0.98 25.28 ± 0.33 12.85 ± 0.44 25.36 ± 0.36 EEGConformer 45.59 ± 1.25 38.58 ± 1.86 45.14 ± 1.07 35.37 ± 1.12 17.72 ± 1.74 34.87 ± 1.36 28.75 ± 0.28 17.47 ± 0.30 28.02 ± 0.28 LaBraM 52.73 ± 1.07 46.98 ± 1.88 52.88 ± 1.02 39.76 ± 1.38 23.86 ± 2.09 39.74 ± 1.11 33.28 ± 0.33 22.85 ± 0.44 33.36 ± 0.36 CBraMod 55.09 ± 0.89 50.41 ± 1.22 56.18 ± 0.93 40.91 ± 0.97 25.69 ± 1.43 41.01 ± 1.08 32.47 ± 0.36 21.47 ± 0.38 32.77 ± 0.32 CSBrain 57.52 ± 0.42 52.04 ± 0.36 57.96 ± 0.31 41.97 ± 0.33 27.85 ± 0.34 42.80 ± 0.23 32.44 ± 0.38 21.45 ± 0.49 32.74 ± 0.47 REVE 56.46 ± 1.64 50.80 ± 1.91 56.59± 1.72 40.48 ± 0.23 26.22 ± 0.21 41.45± 0.17 32.64 ± 0.34 21.72 ± 0.37 33.02± 0.31 DeeperBrain 60.32 ± 0.34 54.99 ± 0.36 60.58 ± 0.33 40.68 ± 0.31 26.43 ± 0.36 41.54 ± 0.25 33.60 ± 0.25 22.86 ± 0.28 33.95 ± 0.23

PhysioNet-MI, 4-class BCIC-IV-2a, 4-class SHU-MI, 2-class Methods Bal. Acc. Kappa Weighted F1 Bal. Acc. Kappa Weighted F1 Bal. Acc. AUC-PR AUROC

EEGNet 58.14 ± 1.25 44.68 ± 1.99 57.96 ± 1.15 44.82 ± 0.94 26.93 ± 1.21 42.26 ± 1.08 58.89 ± 1.77 63.11 ± 1.42 62.83 ± 1.52 EEGConformer 60.49 ± 1.04 47.36 ± 1.71 60.62 ± 0.95 46.96 ± 1.06 29.24 ± 1.41 45.33 ± 1.28 59.00 ± 1.07 63.70 ± 0.93 63.51 ± 1.01

LaBraM 61.73 ± 1.22 49.12 ± 1.92 61.77 ± 1.41 48.69 ± 0.85 31.59 ± 1.54 47.58 ± 1.03 61.66 ± 1.92 67.61 ± 0.83 66.04 ± 0.91 CBraMod 64.17 ± 0.91 52.22 ± 1.69 64.27 ± 1.00 51.38 ± 0.66 35.18 ± 0.94 49.84 ± 0.85 63.70 ± 1.51 71.39 ± 0.88 69.88 ± 0.68 CSBrain 63.04 ± 0.90 50.71 ± 1.20 63.08 ± 0.95 56.57 ± 0.71 42.09 ± 0.93 56.37 ± 0.87 64.17 ± 0.37 72.30 ± 0.79 72.00 ± 0.58 REVE 64.80 ± 1.40 53.06 ± 1.87 64.84 ± 1.70 63.96 ± 0.95 51.94 ± 1.26 63.39 ± 1.10 63.84 ± 0.34 69.90 ± 0.72 70.63 ± 0.42

DeeperBrain 65.17 ± 0.37 53.56 ± 0.49 65.38 ± 0.34 60.69 ± 1.40 47.59 ± 1.86 60.64 ± 1.50 64.31 ± 0.47 70.99 ± 0.53 70.95 ± 0.43

##### ISRUC, 5-class CHB-MIT, 2-class BCIC2020-3, 5-class

Methods Bal. Acc. Kappa Weighted F1 Bal. Acc. AUC-PR AUROC Bal. Acc. Kappa Weighted F1 EEGNet 71.54 ± 1.21 70.40 ± 1.73 75.13 ± 1.24 56.58 ± 1.06 19.14 ± 1.82 80.48 ± 1.36 44.13 ± 0.96 30.16 ± 1.23 44.13 ± 1.02 EEGConformer 74.00 ± 1.33 71.43 ± 1.62 76.34 ± 1.51 59.76 ± 1.41 22.09 ± 2.15 82.26 ± 1.70 45.06 ± 1.33 31.33 ± 1.83 44.88 ± 1.54 LaBraM 76.33 ± 1.02 72.31 ± 1.82 78.10 ± 1.33 70.75 ± 3.58 32.87 ± 4.02 86.79 ± 1.99 50.60 ± 1.55 38.00 ± 2.42 50.54 ± 2.05 CBraMod 78.65 ± 1.10 74.42 ± 1.52 80.11 ± 0.99 73.98 ± 2.84 36.89 ± 3.82 88.92 ± 1.54 53.73 ± 1.08 42.16 ± 1.63 53.83 ± 0.96 CSBrain 79.25 ± 0.30 74.06 ± 1.02 79.90 ± 0.91 72.62 ± 1.15 51.64 ± 4.49 89.15 ± 3.21 56.05 ± 4.38 45.07 ± 5.47 56.05 ± 4.41 REVE 78.19 ± 0.78 75.00 ± 1.56 80.11 ± 0.99 72.02 ± 4.95 53.97 ± 6.38 90.41 ± 0.97 56.35 ± 1.23 45.43 ± 1.54 56.33 ± 1.24 DeeperBrain 78.75 ± 0.60 75.01 ± 0.32 80.89 ± 0.40 74.34 ± 1.49 65.51 ± 4.27 94.09 ± 0.77 57.06 ± 0.78 46.33 ± 0.97 57.04 ± 0.78

MODMA, 2-class SEED-VIG, regression MentalArithmetic, 2-class Methods Bal. Acc. AUC-PR AUROC Correlation R2 Score RMSE↓ Bal. Acc. AUC-PR AUROC

EEGNet 61.90 ± 2.40 64.50 ± 3.00 62.30 ± 4.70 57.01 ± 1.67 23.66 ± 0.84 28.28 ± 0.74 67.70 ± 1.16 57.63 ± 1.02 73.21 ± 1.08 EEGConformer 63.85 ± 2.20 66.40 ± 3.25 64.70 ± 4.60 57.50 ± 1.39 23.44 ± 0.91 28.50 ± 0.83 68.05 ± 1.23 58.29 ± 1.34 74.24 ± 1.28

LaBraM 66.81 ± 7.29 73.43 ± 5.82 68.83 ± 6.22 59.31 ± 0.98 24.32 ± 0.85 27.62 ± 0.48 72.24 ± 2.05 70.78 ± 3.77 84.11 ± 2.46 CBraMod 70.18 ± 2.34 75.92 ± 3.05 72.37 ± 4.91 58.49 ± 2.78 24.82 ± 3.67 27.35 ± 0.83 74.39 ± 2.15 71.68 ± 2.93 83.90 ± 3.27 CSBrain 72.85 ± 2.60 77.90 ± 3.60 75.10 ± 5.00 63.14 ± 3.56 23.63 ± 5.19 27.74 ± 0.94 75.58 ± 1.06 66.96 ± 2.21 84.78 ± 2.97 REVE 72.45 ± 2.10 77.83 ± 3.21 74.62 ± 4.75 58.77 ± 1.17 25.44 ± 1.90 27.42 ± 0.35 76.60 ± 3.55 74.70 ± 8.07 84.50 ± 5.14

DeeperBrain 76.31 ± 2.59 81.55 ± 3.67 78.85 ± 5.19 60.11 ± 0.72 34.14 ± 1.62 25.77 ± 0.32 75.69 ± 2.32 72.04 ± 4.52 86.21 ± 2.19 Results are presented as (mean ± std, %). Bold denotes the best performance, and underline denotes the second best.

NVIDIA RTX A5000 GPU, completing training in approximately 7 hours. The input EEG signal is partitioned into nonoverlapping spatiotemporal patches, each corresponding to a 1-second segment (200 time steps at 200 Hz). The backbone architecture consists of a 12-layer Transformer encoder with the following specifications: embedding dimension D = 200, feed-forward hidden dimension Dff = 800, and 8 heads of self-attention. During pretraining, we adopt a random patchwise masking strategy with a mask ratio of 50%, where masked patches are replaced by zero vectors in the raw voltage space. The model is trained for 2 epochs with a batch size of 16. We set the coefficients of two pretraining objectives as λMER = λNSP = 1.0. Optimization is performed using the AdamW optimizer with a base learning rate of 5 × 10−4, weight decay of 5 × 10−2, and default β1 = 0.9, β2 = 0.999. No learning rate warmup is used, following the pre-normalization design’s stability [114]. Gradient clipping with a maximum norm of 1.0 is applied to stabilize training. The code and pretrained model will be publicly available.

B. Downstream Tasks and Evaluation Protocol

- 1) Downstream Tasks and Datasets: To comprehensively

evaluate the generalization capability of DeeperBrain, we selected 10 diverse downstream BCI tasks. Table II summarizes these tasks along with their corresponding datasets. Consistent with the pretraining configuration, all downstream EEG signals were resampled to 200 Hz, and the patch duration was fixed at 1 second (200 data points). To ensure fair comparison, we adopted standard data splitting protocols from LaBraM [98] or CBraMod [104] whenever available.

- 2) Fine-tuning and Frozen-probing Settings: For end-to-

end fine-tuning, the model is optimized using the AdamW optimizer with a weight decay of 5×10−2. The initial learning rate is selected from {1 × 10−4,3 × 10−4,5 × 10−4} based on validation performance, and is decayed over the course of training via cosine annealing. Training proceeds for 50 epochs with a batch size of either 32 or 64, depending on dataset scale and memory constraints. In the frozen-probing setting, the pretrained DeeperBrain backbone is kept entirely frozen, and only the downstream prediction head is trained.

TABLE IV PERFORMANCE COMPARISON WITH EXISTING METHODS UNDER FROZEN-PROBING.

FACED, 9-class SEED-V, 5-class SEED-VII, 7-class Methods Bal. Acc. Kappa Weighted F1 Bal. Acc. Kappa Weighted F1 Bal. Acc. Kappa Weighted F1

LaBraM 16.13 ± 10.04 5.61 ± 11.21 9.88 ± 13.37 32.63 ± 0.53 15.45 ± 0.69 32.62 ± 0.87 15.35 ± 1.99 1.29 ± 2.42 7.09 ± 6.15 CBraMod 25.84 ± 1.36 16.32 ± 1.60 21.77 ± 1.46 24.36 ± 0.38 5.29 ± 0.47 20.39 ± 1.18 17.32 ± 0.27 3.48 ± 0.35 14.23 ± 1.43 CSBrain 36.59 ± 0.96 28.56 ± 1.07 36.59 ± 0.94 20.00 ± 0.00 0.00 ± 0.00 8.87 ± 0.00 14.28 ± 0.01 -0.01 ± 0.01 4.76 ± 0.72 REVE 37.76 ± 0.54 29.77 ± 0.65 37.63 ± 0.63 27.82 ± 0.72 9.66 ± 0.87 27.56 ± 1.15 14.29 ± 0.00 0.00 ± 0.00 3.76 ± 0.42

DeeperBrain 50.96 ± 0.37 44.38 ± 0.40 50.36 ± 0.36 35.08 ± 0.26 18.75 ± 0.29 35.39 ± 0.29 23.26 ± 0.22 10.71 ± 0.24 22.83 ± 0.53

PhysioNet-MI, 4-class BCIC-IV-2a, 4-class SHU-MI, 2-class Methods Bal. Acc. Kappa Weighted F1 Bal. Acc. Kappa Weighted F1 Bal. Acc. AUC-PR AUROC

LaBraM 46.52 ± 0.58 28.70 ± 0.78 46.62 ± 0.45 38.11 ± 1.04 17.48 ± 1.39 33.50 ± 1.66 59.48 ± 3.31 65.28 ± 1.21 66.92 ± 1.38 CBraMod 53.73 ± 0.39 38.30 ± 0.54 53.91 ± 0.46 33.06 ± 0.63 10.74 ± 0.84 21.73 ± 0.59 57.18 ± 2.22 64.96 ± 0.75 64.85 ± 0.49 CSBrain 26.19 ± 1.60 2.04 ± 2.86 15.52 ± 6.61 26.70 ± 1.05 2.27 ± 1.40 19.29 ± 3.78 53.05 ± 0.82 54.95 ± 1.78 54.69 ± 0.91 REVE 25.01 ± 0.02 0.01 ± 0.03 10.03 ± 0.05 42.73 ± 1.12 23.63 ± 1.49 38.66 ± 1.31 59.38 ± 1.14 66.77 ± 0.35 65.63 ± 0.83

DeeperBrain 56.57 ± 0.73 42.10 ± 0.98 56.74 ± 0.72 51.01 ± 2.23 34.68 ± 2.98 49.23 ± 3.09 60.81 ± 1.80 67.01 ± 0.27 66.57 ± 0.25

ISRUC, 5-class CHB-MIT, 2-class BCIC2020-3, 5-class Methods Bal. Acc. Kappa Weighted F1 Bal. Acc. AUC-PR AUROC Bal. Acc. Kappa Weighted F1 LaBraM 71.79 ± 0.95 67.94 ± 1.08 74.55 ± 0.90 55.31 ± 3.45 28.76 ± 3.90 89.08 ± 1.95 24.83 ± 2.61 6.03 ± 3.26 22.76 ± 5.82 CBraMod 37.27 ± 5.90 24.87 ± 5.63 37.16 ± 3.23 58.93 ± 2.85 36.66 ± 7.10 86.20 ± 2.55 20.24 ± 0.52 0.30 ± 0.65 8.74 ± 2.12 CSBrain 22.24 ± 2.25 3.01 ± 3.18 22.61 ± 3.11 62.68 ± 4.42 8.13 ± 3.45 75.48 ± 4.18 32.19 ± 1.40 15.23 ± 1.75 30.96 ± 2.18 REVE 73.55 ± 0.47 68.78 ± 0.27 75.72 ± 0.42 63.93 ± 3.70 46.68 ± 4.06 92.11 ± 1.30 39.04 ± 9.59 23.80 ± 11.99 36.32 ± 14.87 DeeperBrain 74.10 ± 0.58 70.07 ± 0.60 76.71 ± 0.68 64.95 ± 2.55 38.46 ± 4.84 88.73 ± 3.75 43.33 ± 0.64 29.17 ± 0.80 42.69 ± 0.73

MODMA, 2-class SEED-VIG, regression MentalArithmetic, 2-class Methods Bal. Acc. AUC-PR AUROC Correlation R2 Score RMSE↓ Bal. Acc. AUC-PR AUROC

LaBraM 43.12 ± 7.52 43.41 ± 9.28 30.02 ± 9.01 56.92 ± 1.56 18.51 ± 4.44 28.66 ± 0.80 60.69 ± 9.18 69.67 ± 2.02 83.06 ± 1.94 CBraMod 46.00 ± 3.23 37.55 ± 1.73 36.81 ± 3.62 37.19 ± 3.20 9.12 ± 3.17 30.27 ± 0.53 54.79 ± 1.98 47.15 ± 2.70 65.40 ± 1.73 CSBrain 52.38 ± 10.83 55.94 ± 11.95 52.42 ± 10.82 22.31 ± 3.89 4.38 ± 1.89 31.06 ± 0.31 54.65 ± 3.77 38.53 ± 10.19 59.32 ± 6.29 REVE 53.00 ± 3.48 61.32 ± 9.19 56.75 ± 9.15 50.32 ± 4.35 10.61 ± 13.46 29.94 ± 2.27 67.29 ± 7.89 70.84 ± 2.13 82.69 ± 1.54

DeeperBrain 63.36 ± 2.40 70.37 ± 1.00 70.39 ± 1.13 59.85 ± 1.24 31.43 ± 1.52 27.52 ± 0.30 68.05 ± 0.40 54.57 ± 2.52 74.79 ± 0.87 Results are presented as (mean ± std, %). Bold denotes the best performance, and underline denotes the second best.

The same optimization protocol such as optimizer, learning rate schedule, batch size, and number of epochs, is applied to ensure a fair comparison between the two adaptation strategies.

- 3) Compared Methods: We compare DeeperBrain with

both non-foundation-model and foundation-model baselines on all the downstream BCI tasks. We adopt EEGNet [56] and EEGConformer [70] as non-foundation-model baselines. Concurrently, we use four very strong existing methods, LaBraM [98], CBraMod [104], CSBrain [109] and REVE [111] as the foundation-model baselines.

- 4) Metrics: We employ specific evaluation protocols based

on the task type. For binary classification, we report Balanced Accuracy, AUC-PR, and AUROC, with AUROC serving as the primary monitor score. For multi-class classification, we utilize Balanced Accuracy, Cohen’s Kappa, and Weighted F1, selecting Cohen’s Kappa as the monitor score. For regression tasks, performance is assessed via Pearson’s Correlation, R2 Score, and RMSE, with the R2 score used for monitoring. All reported results represent the mean and standard deviation across five independent random seeds.

C. Performance Comparison with End-to-End Fine-tuning

We evaluate the effectiveness of DeeperBrain under the standard end-to-end fine-tuning protocol. As shown in Table III, DeeperBrain achieves state-of-the-art or highly competitive performance across a comprehensive suite of EEG decoding

benchmarks. The extensive experimental results reveal three key insights regarding the advantages of our methodology.

First, DeeperBrain consistently outperforms traditional supervised baselines, such as EEGNet and EEGConformer, by a significant margin across all datasets. This validates the efficacy of large-scale self-supervised pretraining in extracting generalizable representations, effectively overcoming the generalization bottlenecks inherent in training deep networks on limited task-specific data.

Second, compared to existing foundation models that rely on general-purpose sequence modeling, DeeperBrain demonstrates superior transferability. While purely data-driven approaches implicitly infer structure from vast corpora, our model achieves leading performance by explicitly incorporating domain-specific inductive biases. The consistent superiority across diverse paradigms suggests that the Neurodynamics Statistics Prediction (NSP) objective captures fundamental properties of neural computation. Unlike reconstruction-only objectives that prioritize local waveform fidelity, NSP compels the model to internalize macroscopic order parameters, including spectral organization and functional integration. These dynamical features function as a universal language for brain activity, facilitating effective decoding across distinct cognitive and pathological states.

Third, the robustness observed across heterogeneous datasets highlights the critical utility of our neurophysiologically grounded positional encodings. By modeling volume

Ours

Std. Spatial

Std. Temporal

Baseline

| |
|---|

| |
|---|

| |
|---|

34.0

79.5

|SE<br><br>**| | |
|---|---|---|
| | | |
| | | |
| | | |
| |**<br><br>**| |
| | | |
| | | |
| | | |
| | | |
| |ED-V<br><br>|t<br><br>s<br><br>r<br><br>i|
| | | |
|**|**| |
| |**| |
| | | |
|SEE<br><br>3<br><br>o<br><br>our the is<br><br>und<br><br>f<br><br>its tes<br><br>ersa eep ucc<br><br>a invariant the| | |
| |D-V<br><br>D<br><br>atia decay<br><br>ctiv<br><br>r<br><br>sen atio<br><br>sse<br><br>or of<br><br>-to-e<br><br>ts lly erB essf<br><br>s<br><br><br>ogn| |

|Physio<br><br>**<br><br>| |
|---|---|
| | |
| | |
| | |
| |**|
| |**|
| | |
| | |
| | |
| |Net-MI<br><br>et-MI<br><br>**<br><br>**<br><br>) in<br><br>caused oral ow<br><br>with the<br><br>ica a<br><br>evaluate<br><br>significantly<br><br>which ined<br><br>d<br><br>workload|
| | |
| | |
|**| |
| | |
| | |
| | |
|PhysioN<br><br>std, %<br><br>geometry,<br><br>emp sl<br><br>capability tasks<br><br>aligning ynam<br><br>this a<br><br>often provide ,<br><br>specific etra<br><br>merely an<br><br>alone in| |

- 56

- 57

- 58

- 59

- 60

- 61

41.0

- 70

- 71

- 72

- 73

- 74

- 75

- 76

- 54

- 55

- 56

- 57

- 58

65.5

- 57

- 58

- 59

- 60

- 61

- 62

- 71

- 72

- 73

- 74

- 75

- 76

- 77

- 78

60.5

79.0

33.5

64.5

40.5

65.0

78

60.0

78.5

**

*

*

64.5

**

40.0

33.0

**

*

59.5

*

*

64.0

78.0

**

**

Correlation(%)

*

76

64.0

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

**

39.5

**

32.5

**

59.0

**

77.5

**

63.5

63.5

39.0

58.5

77.0

32.0

74

63.0

38.5

76.5

58.0

63.0

31.5

62.5

76.0

38.0

72

57.5

62.0

31.0

62.5

75.5

37.5

57.0

61.5

FACED

SEED-VII

BCIC-IV-2a

SHU-MI

ISRUC

CHB-MIT

BCIC2020-3

MODMA

SEED-VIG

MentalArithmetic

(a) end-to-end fine-tuning

Ours Std. Spatial Std. Temporal

Baseline

| |
|---|

- 57

- 58

- 59

- 60

- 61

- 62

- 63

68

66

- 53

- 54

- 55

- 56

- 57

- 58

- 59

- 60

- 61

- 39

- 40

- 41

- 42

- 43

- 44

- 51
- 52
- 53
- 54
- 55
- 56
- 57

- 62

- 63

- 64

- 65

- 66

- 67

- 68

- 46

- 47

- 48

- 49

- 50

- 51

74.5

- 31
- 32
- 33
- 34
- 35

- 19

- 20

- 21

- 22

- 23

52

64

66

74.0

*

**

73.5

**

50

**

*

62

*

*

Correlation(%)

**

64

*

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

** **

**

*

**

73.0

**

**

**

**

48

**

**

**

60

72.5

62

**

**

72.0

**

58

46

60

71.5

56

44

71.0

58

FACED

SEED-VII

BCIC-IV-2a

SHU-MI

ISRUC

CHB-MIT

BCIC2020-3

MODMA

SEED-VIG

MentalArithmetic

(b) frozen-probing

- Fig. 2. Performance comparison (mean ± balanced accuracy on positional encoding. “*” indicates p < 0.05 and “**” indicates p < 0.01.

Notably, while fine-tuning generally yields the highest absolute performance by adapting to task-specific nuances, the performance drop observed when switching to frozenprobing is remarkably smaller for DeeperBrain compared to baselines. This resilience suggests that our dual-objective pretraining strategy, which combines signal reconstruction with neurodynamics prediction, effectively forces the model to disentangle meaningful physiological factors from noise during the pretraining phase itself. This characteristic is particularly valuable for practical brain-computer interfaces, as it implies that DeeperBrain can serve as a robust, distinct feature extractor for new tasks with minimal computational overhead and reduced risk of overfitting to small calibration datasets.

conduction via electrode geo DeeperBrain effectively mitigates l domain shifts d by varying electrode montages. Concurrently, the t encoding, utilizing oscillatory and bases, captures neural modulations and adaptation dynamics. This cap enables the model to generalize ely across ta distinct temporal characteristics, regardless of whether target features are transient events continuous state fluctuations. These results substantiate o hypothesis that ali deep learning architectures with t biophysical and d l first principles of neuroscience i ial for constructing truly universal and robust EEG fo n model.

D. Performance Comparison with Frozen-probing

E. Positional Encoding Comparison

To rigorously s the intrinsic generalization capability of the learned representations, we e DeeperBrain under a frozen-probing protocol. In setting, the pretrained backbone remains frozen, and only task-specific prediction head is trained each downstream dataset. As reported in Table IV, DeeperBrain achieves dominant performance across the majority benchmarks, ntly outperforming existing foundation models that o struggle to generalize without extensive parameter adaptation.

To rigorously assess the specific contribution of our neurophysiologically grounded designs against standard deep learning components, we conducted a controlled ablation study. We compare the full DeeperBrain model against three variants: (1) Std. Spatial, where our volume-conduction-aware encoding is replaced by a standard linear projection of 3D electrode coordinates; (2) Std. Temporal, where our dynamic temporal basis is replaced by standard sinusoidal positional embeddings; and (3) Baseline, which utilizes both standard spatial and temporal embeddings, effectively stripping the model of specific neurophysical priors. Figure 2 illustrates the comparative performance across twelve diverse datasets.

The experimental outcomes pro compelling evidence for the semantic richness of our neuro-grounded representations. Unlike nd fine-tuning allows the model to re-optimize parameters for s target distributions, frozen-probing whether the pr features are separable and univ applicable ”out-of-the-box.” The results indicate that D ain does not memorize statistical patterns but s ully encapsulates core neurodynamical properties, such oscillatory states functional connectivity, that are in across different subjects and paradigms. Consequently, frozen features a are sufficient to support high-performance decoding complex tasks ranging from emotion tion to mental oad estimation.

The empirical results consistently demonstrate that DeeperBrain outperforms the Std. Spatial variant. This finding indicates that merely providing geometric coordinates is insufficient. By explicitly modeling volume conduction through a distance-decay kernel, DeeperBrain provides a strong inductive bias reflecting the physical mixing of electrical fields, enabling the Transformer to better disentangle neural sources from blurred sensor observations. Furthermore, the superiority of DeeperBrain over the Std. Temporal variant highlights the

Ours

w/o MER

w/o NSP

| |
|---|

| |
|---|

- 54

- 55

- 56

- 57

- 58

- 57

- 58

- 59

- 60

- 61

41.0

- 70

- 71

- 72

- 73

- 74

- 75

- 76

65.5

- 71

- 72

- 73

- 74

- 75

- 76

- 77

- 78

- 79

- 56

- 57

- 58

- 59

- 60

- 61

- 62

- 70

- 71

- 72

- 73

- 74

- 75

- 76

- 77

- 78

60.5

- 75

- 76

- 77

- 78

- 79

64.5

33.5

*

40.5

**

65.0

**

60.0

**

*

64.0

*

33.0

**

64.5

40.0

59.5

*

Correlation(%)

63.5

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

**

**

**

32.5

64.0

59.0

39.5

**

**

**

**

**

63.0

63.5

58.5

32.0

39.0

62.5

63.0

58.0

31.5

38.5

62.0

62.5

57.5

31.0

38.0

61.5

62.0

57.0

FACED

SEED-V

SEED-VII

PhysioNet-MI

BCIC-IV-2a

SHU-MI

ISRUC

CHB-MIT

BCIC2020-3

MODMA

SEED-VIG

MentalArithmetic

(a) end-to-end fine-tuning

Ours w/o MER w/o NSP

23.5

68

- 56

- 57

- 58

- 59

- 60

- 61

- 62

- 63

- 40

- 41

- 42

- 43

- 44

66

- 55

- 56

- 57

- 58

- 59

- 60

- 61

- 52

- 53

- 54

- 55

- 56

- 57

51.0

- 47

- 48

- 49

- 50

- 51

- 52

- 53

35.0

- 64

- 65

- 66

- 67

- 68

23.0

- 71

- 72

- 73

- 74

66

50.5

*

64

34.5

**

**

**

22.5

50.0

**

**

Correlation(%)

*

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

Bal.Acc.(%)

34.0

64

**

22.0

49.5

**

**

62

**

**

**

33.5

**

49.0

**

21.5

62

48.5

33.0

60

21.0

48.0

60

32.5

20.5

47.5

58

32.0

58

20.0

47.0

FACED

SEED-V

SEED-VII

PhysioNet-MI

BCIC-IV-2a

SHU-MI

ISRUC

CHB-MIT

BCIC2020-3

MODMA

SEED-VIG

MentalArithmetic

(b) frozen-probing

- Fig. 3. Performance comparison (mean ± std, %) in balanced accuracy on pretraining objective. “*” indicates p < 0.05 and “**” indicates p < 0.01.

limitation of generic sinusoidal positional embeddings, which capture sequence order but lack the intrinsic oscillatory and adaptive structure of brain dynamics. Our method aligns the model’s temporal representation with biological timescales. Finally, the significant gap between DeeperBrain and the Baseline confirms that these spatial and temporal priors provide complementary benefits. Collectively, these results substantiate that embedding EEG-specific physics into the architecture yields representations significantly more robust than those derived from generic sequence modeling components.

Ours: Volume Conduction Prior (High-Density 10-5, =8 cm)

Baseline: Discrete Encoding (Target: Cz)

[Figure 12]

[Figure 13]

Fig. 4. Comparison of spatial receptive fields on a high-density 10-5 montage. Unlike the baseline (left) which exhibits a discrete impulse response, DeeperBrain (right) explicitly models volume conduction via a continuous spatial decay kernel (visualized here with τ = 8 cm), aligning with the physics of scalp potentials.

F. Pretraining Objective Comparison

To evaluate the individual contributions of our dualobjective strategy, we performed an ablation study by training DeeperBrain with only Masked EEG Reconstruction (w/o NSP) and only Neurodynamics Statistics Prediction (w/o MER). Figure 3 summarizes the performance under both endto-end fine-tuning and frozen-probing protocols.

to abstract away from raw noise and focus on the emergent dynamical structures that define brain states. The robustness of the full model, particularly in the probing setting, underscores that combining these two perspectives enables DeeperBrain to learn a universal representation that is both physically accurate in the time domain and mechanistically meaningful in the neurodynamical domain.

The results consistently show that the full DeeperBrain model, which jointly optimizes both objectives, achieves the highest performance. This superiority indicates that signal fidelity and dynamical consistency are not redundant but rather complementary goals in EEG representation learning. Specifically, the performance degradation observed in the ”w/o MER” variant suggests that reconstruction is essential for capturing fine-grained morphological details and high-frequency transients. Without the constraint to recover the original waveform, the model may overlook subtle temporal features that are critical for tasks such as seizure detection. Conversely, the decline in performance for the ”w/o NSP” variant highlights the necessity of explicitly enforcing neurophysiological alignment. While reconstruction ensures that the model encodes the ”what” of the signal, the NSP objective guides the model to understand the ”how” and ”why” by predicting macroscopic order parameters like spectral power distribution and functional connectivity. This mechanism encourages the model

G. Visualization Analysis

While quantitative benchmarks demonstrate DeeperBrain’s superior performance, it is equally crucial to verify that these gains stem from genuine modeling of neurophysiological mechanisms rather than statistical overfitting. In this section, we qualitatively analyze the learned spatial and temporal structures, as well as the neurodynamical consistency of the optimization objective.

1) Modeling Volume Conduction in Channel Positional Encoding: Standard EEG modeling typically treats electrodes as discrete, isolated nodes, neglecting the biophysical reality of

###### Standard Sinusoidal PE (Generic & Symmetric)

###### Learnable Absolute PE (Data-driven & Unstructured)

Ours: Neuro-Temporal Basis (Bio-Inductive Bias)

0

0

| |[Figure 14]<br><br>Generic Priors No 'Arrow of Time'| | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

|[Figure 15]<br><br>No Explicit Physics Requires Huge Data| | | | |
|---|---|---|---|---|
| | | | | |

|[Figure 16]<br><br>Slow Oscillations (Quasi-periodic)| | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
|Adaptive Decays (Arrow of Time)| | | | | |
| | | | | | |
| | | | | | |

25

10

50

EmbeddingDimensionIndex

BasisFunctionIndex

75

20

100

125

30

150

40

175

0 20 40 60 80

0 20 40 60 80

0 20 40 60 80

Time (s)

Time (s)

Time (s)

- Fig. 5. Comparison of temporal positional encodings. (Left) Standard sinusoidal PE relies on generic, symmetric spectral priors. (Middle) Learnable absolute PE starts as unstructured noise, lacking explicit physical constraints. (Right) DeeperBrain PE incorporates strong neurophysiological inductive biases: Slow Oscillations for quasi-periodic state maintenance and Adaptive Decays for modeling the dissipative ”arrow of time”.

0.00 0.25 0.50 0.75

0.0

0.2

0.4

0.6

Predicted

r = 0.82

Local Oscillation (Alpha Power)

0.0 0.5 1.0

0.0

0.2

0.4

0.6

0.8

1.0

r = 0.62

Functional Connectivity (Delta PLV Mean)

0.02 0.01 0.00 0.01

Ground Truth

0.020

0.015

0.010

0.005

0.000

0.005

0.010

0.015

Predicted

r = 0.01

Hierarchical Integration ( - CFC)

0 1 2

Ground Truth

0.0

0.5

1.0

1.5

2.0

r = 0.75

Dynamic Complexity (Sample Entropy)

| |0<br><br>0.34|0.49<br><br>.43<br><br>0.49<br><br>0.51<br><br>0|0.62<br><br>0.63<br><br>0.63<br><br>0.62<br><br>.58<br><br>0.7|5| |
|---|---|---|---|---|---|
|0.01 0.01<br><br>0.03| | | | | |
| | | | | | |
| | | | | | |

0.0 0.2 0.4 0.6 0.8 1.0

Pearson Correlation Coefficient (r)

Delta Power Theta Power Alpha Power

Beta Power Gamma Power

Delta PLV Delta PLV

Theta PLV Theta PLV Alpha PLV Alpha PLV

Beta PLV Beta PLV

Gamma PLV Gamma PLV

- - CFC

- - CFC

- - CFC

Sample Entropy

0.84 0.76

0.82 0.78

0.80

Consistency Profile Across 19 Order Parameters

Spectral Connectivity Coupling Complexity

- Fig. 6. Visualization of Neurodynamical Consistency (Zero-shot on FACED). (Left) Scatter density plots compare ground-truth vs. predicted statistics. Strong alignment is observed for robust metrics like Alpha Power (r = 0.82) and Sample Entropy (r = 0.75). (Right) The consistency profile across 19 metrics confirms high performance for spectral and complexity measures. The low correlation for CFC reflects the sparsity of this feature in the target task and the model’s robustness against fitting noise.

volume conduction—the passive spread of electrical currents through head tissues.

To validate DeeperBrain’s ability to capture this physical phenomenon, we visualize the effective spatial receptive field of a central electrode (Cz) in Fig. 4. The baseline (left) displays a discrete ”impulse” response, implying an assumption of sensor independence that contradicts physical laws. In contrast, DeeperBrain (right) generates a smooth, isotropic diffusion pattern. By explicitly modeling distance-dependent decay (shown with a physical prior τ ≈ 8 cm), DeeperBrain acts as a spatial regularizer. This design encourages the Transformer to aggregate information from a physically meaningful neighborhood, effectively disentangling the underlying neural source from the volume-conducted observation.

2) Oscillations and Adaptation in Temporal Positional Encoding: Neural dynamics span multiple timescales, ranging from millisecond-level spiking to minute-level state transitions. However, generic positional encodings, including standard sinusoidal and learnable embeddings, treat time indices as symmetric dimensions or arbitrary markers. They lack inductive biases for the ”arrow of time,” failing to capture the dissipative nature of neural adaptation.

Fig. 5 compares the feature maps of three positional encoding strategies over a 100-second window. The standard encoding (left) relies on generic spectral priors without directionality. The learnable encoding (middle) exhibits an unstructured, high-entropy distribution, implying that the model must learn temporal rules entirely from data, which risks overfitting in data-scarce regimes. In contrast, DeeperBrain’s basis (right)

reveals a structured, disentangled representation aligned with neural dynamics:

- • Slow Oscillations (Top): The upper dimensions encode stable, quasi-periodic structures (periods 2s–100s), providing the necessary context to identify macroscopic rhythms.
- • Adaptive Decays (Bottom): The lower dimensions exhibit a smooth, directional fading gradient. Unlike symmetric sinusoids or random embeddings, these decay bases explicitly model the ”arrow of time,” capturing neural adaptation and the gradual forgetting of past context.

3) Neurodynamical Consistency of Optimization Objective: Beyond local reconstruction, the Neurodynamics Statistics Prediction (NSP) objective forces the model to internalize macroscopic order parameters. To verify this semantic alignment, we evaluate DeeperBrain on the downstream FACED dataset in a zero-shot manner, comparing ground-truth statistics (calculated from full signals) against predictions inferred from 50% masked inputs.

Fig. 6 presents the consistency profile across 19 neurodynamical metrics. DeeperBrain exhibits remarkable consistency for robust physiological markers. Spectral power (e.g., Alpha band r = 0.82) and dynamic complexity (Sample Entropy r = 0.75) show strong linear alignment, indicating that the model successfully identifies oscillatory states and signal regularity even from partial observations. Functional connectivity (PLV) also maintains moderate consistency (r ≈ 0.6), suggesting the capture of global synchronization patterns.

Notably, Cross-Frequency Coupling (CFC) exhibits lower correlation (r ≈ 0.01). This discrepancy offers a valuable neurophysiological insight: (1) Sparsity: CFC is a high-order non-linear statistic that is typically sparse and low-SNR in scalp EEG during passive viewing tasks (like FACED); (2) Phase Uncertainty: Recovering precise instantaneous phase relationships under high masking ratios is an ill-posed problem. The model’s conservative prediction on CFC suggests it prioritizes robust, salient features (e.g., power and entropy) over fitting spurious correlations in noise-dominated metrics.

V. DISCUSSION A. Implications

DeeperBrain advances EEG foundation modeling by bridging the gap between deep learning and established neurophysiological principles. Unlike prior approaches that rely on general-purpose sequence modelers to implicitly infer neural patterns, our framework explicitly integrates volume conduction-aware spatial priors and multi-scale temporal dynamics. These inductive biases align the model structure with the physical and functional organization of the brain. By transcending purely data-driven feature extraction, this principled approach enhances performance across diverse downstream tasks and improves neuroscientific interpretability, ensuring that learned representations intrinsically encode canonical markers including spectral organization, functional connectivity, cross-frequency coordination, and dynamic complexity.

From an engineering perspective, DeeperBrain demonstrates that embedding domain knowledge into foundation models yields superior transferability. The robust performance observed under both end-to-end fine-tuning and frozenprobing protocols indicates that neurodynamics-guided selfsupervision is more effective than reconstruction alone. This finding holds profound implications for the deployment of universal BCIs where labeled data is scarce and inter-subject variability is high. Consequently, a single pretrained DeeperBrain model can serve as a universal encoder for a wide range of BCI tasks, requiring minimal task-specific adaptation and effectively lowering the barrier for real-world application.

B. Limitations and Future Directions

Despite these advancements, we acknowledge specific limitations in the current framework. First, DeeperBrain relies on standardized 3D electrode coordinates which may be absent in some clinical settings. Future iterations could integrate coordinate estimation or learned spatial priors to address geometric uncertainty. Second, the NSP objective currently utilizes four classical statistics. Expanding this set to higher-order dynamics, such as metastability and criticality, may further align representations with complex brain states. Third, while stochastic reorganization accommodates variable channel counts, explicitly modeling montage topology shifts warrants further exploration to enhance robustness.

Furthermore, although our pretraining corpus spans 14 heterogeneous datasets, it retains demographic biases toward specific populations due to the geographic concentration of data sources. Extending DeeperBrain to globally representative EEG data would enhance fairness and generalizability. Finally, the current reliance on fixed-duration patches limits flexibility. Future work will explore streaming or variable-length inference mechanisms to facilitate real-time BCI applications.

VI. CONCLUSION

We have presented DeeperBrain, a neuro-grounded EEG foundation model designed to facilitate universal BCI. By explicitly integrating biophysical inductive biases, specifically spatial volume conduction and temporal multi-scale adaptation, and enforcing global dynamical consistency via neurodynamics statistics prediction, DeeperBrain acquires representations that are both physically grounded and functionally meaningful. Empowered by pretraining on over 17,000 hours of diverse unlabeled EEG, the model achieves state-of-the-art or highly competitive performance across a broad spectrum of downstream tasks, notably maintaining superior efficacy even under a rigorous frozen-probing protocol. These results demonstrate that aligning machine learning architectures with neuroscientific first principles yields significant empirical gains. We envision DeeperBrain as a pivotal step toward universal BCI, marking a paradigm shift from purely datadriven empiricism to principled, neuro-grounded intelligence that fundamentally understands the language of the brain.

REFERENCES

[1] G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw, “Bci2000: a general-purpose brain-computer interface (bci)

system,” IEEE Transactions on biomedical engineering, vol. 51, no. 6, pp. 1034–1043, 2004.

- [2] Z. Wu, G. Pan, and N. Zheng, “Cyborg intelligence,” IEEE Intelligent Systems, vol. 28, no. 5, pp. 31–33, 2013.
- [3] S. Zhang, S. Yuan, L. Huang, X. Zheng, Z. Wu, K. Xu, and G. Pan, “Human mind control of rat cyborg’s continuous locomotion with wireless brain-to-brain interface,” Scientific reports, vol. 9, no. 1, p. 1321, 2019.
- [4] H. Altaheri, G. Muhammad, M. Alsulaiman, S. U. Amin, G. A. Altuwaijri, W. Abdul, M. A. Bencherif, and M. Faisal, “Deep learning techniques for classification of electroencephalogram (eeg) motor imagery (mi) signals: A review,” Neural Computing and Applications, pp. 1–42, 2021.
- [5] G. Dai, J. Zhou, J. Huang, and N. Wang, “Hs-cnn: a cnn with hybrid convolution scale for eeg motor imagery classification,” Journal of neural engineering, vol. 17, no. 1, p. 016025, 2020.
- [6] D. Dadebayev, W. W. Goh, and E. X. Tan, “Eeg-based emotion recognition: Review of commercial eeg devices and machine learning techniques,” Journal of King Saud University-Computer and Information Sciences, vol. 34, no. 7, pp. 4385–4401, 2022.
- [7] P. Gao, T. Liu, J.-W. Liu, B.-L. Lu, and W.-L. Zheng, “Multimodal multi-view spectral-spatial-temporal masked autoencoder for self-supervised emotion recognition,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024, pp. 1926–1930.
- [8] S. Zhao, S. Yi, Y. Zhou, J. Pan, J. Wang, J. Xia, S. Li, S. Dong, and G. Pan, “Wearable music2emotion: Assessing emotions induced by ai-generated music through portable eeg-fnirs fusion,” in Proceedings of the 33rd ACM International Conference on Multimedia, 2025, pp. 5627–5636.
- [9] I. Ahmad, X. Wang, M. Zhu, C. Wang, Y. Pi, J. A. Khan, S. Khan, O. W. Samuel, S. Chen, and G. Li, “Eeg-based epileptic seizure detection via machine/deep learning approaches: A systematic review,” Computational Intelligence and Neuroscience, vol. 2022, 2022.
- [10] ˙I. Yıldız, R. Garner, M. Lai, and D. Duncan, “Unsupervised seizure identification on eeg,” Computer methods and programs in biomedicine, vol. 215, p. 106604, 2022.
- [11] H. Phan, O. Y. Ch´en, M. C. Tran, P. Koch, A. Mertins, and M. De Vos, “Xsleepnet: Multi-view sequential model for automatic sleep staging,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 44, no. 9, pp. 5903–5915, 2021.
- [12] J. Wang, S. Zhao, H. Jiang, S. Li, T. Li, and G. Pan, “Generalizable sleep staging via multi-level domain alignment,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, no. 1, 2024, pp. 265–273.
- [13] Y. Zhou, S. Zhao, J. Wang, H. Jiang, B. Luo, T. Li, G. Pan et al., “Personalized sleep staging leveraging source-free unsupervised domain adaptation,” arXiv preprint arXiv:2412.12159, 2024.
- [14] Y. Bai, Y. Lin, and U. Ziemann, “Managing disorders of consciousness: the role of electroencephalography,” Journal of neurology, vol. 268, no. 11, pp. 4033–4065, 2021.
- [15] S. Zhao, Y. Cao, W. Yang, J. Yu, C. Xu, W. Dai, S. Li, G. Pan, and B. Luo, “Docter: a novel eeg-based diagnosis framework for disorders of consciousness,” Journal of Neural Engineering, vol. 21, no. 5, p. 056021, 2024.
- [16] S. Yasin, S. A. Hussain, S. Aslan, I. Raza, M. Muzammel, and A. Othmani, “Eeg based major depressive disorder and bipolar disorder detection using neural networks: A review,” Computer Methods and Programs in Biomedicine, vol. 202, p. 106007, 2021.
- [17] Y. Wang, S. Zhao, H. Jiang, S. Li, T. Li, and G. Pan, “M-mdd: A multitask deep learning framework for major depressive disorder diagnosis using eeg,” Neurocomputing, vol. 636, p. 130008, 2025.
- [18] S. Saha and M. Baumert, “Intra-and inter-subject variability in eegbased sensorimotor brain computer interface: a review,” Frontiers in computational neuroscience, vol. 13, p. 87, 2020.
- [19] A. Bj¨ork and E. Kugelberg, “The electrical activity of the muscles of the eye and eyelids in various positions and during movement,” Electroencephalography and clinical neurophysiology, vol. 5, no. 4, pp. 595–602, 1953.
- [20] M. M. N. Mannan, M. A. Kamran, and M. Y. Jeong, “Identification and removal of physiological artifacts from electroencephalogram signals: A review,” Ieee Access, vol. 6, pp. 30630–30652, 2018.
- [21] J. A. Urig¨uen and B. Garcia-Zapirain, “Eeg artifact removal—state-ofthe-art and guidelines,” Journal of neural engineering, vol. 12, no. 3, p. 031001, 2015.
- [22] Z. Jamil, A. Jamil, and M. Majid, “Artifact removal from eeg signals recorded in non-restricted environment,” Biocybernetics and Biomedi-

- cal Engineering, vol. 41, no. 2, pp. 503–515, 2021.
- [23] J. N. Acharya and V. J. Acharya, “Overview of eeg montages and principles of localization,” Journal of Clinical Neurophysiology, vol. 36, no. 5, pp. 325–329, 2019.
- [24] R. Bommasani, D. A. Hudson, E. Adeli, R. Altman, S. Arora, S. von Arx, M. S. Bernstein, J. Bohg, A. Bosselut, E. Brunskill et al., “On the opportunities and risks of foundation models,” arXiv preprint arXiv:2108.07258, 2021.
- [25] B. Min, H. Ross, E. Sulem, A. P. B. Veyseh, T. H. Nguyen, O. Sainz, E. Agirre, I. Heintz, and D. Roth, “Recent advances in natural language processing via large pre-trained language models: A survey,” ACM Computing Surveys, vol. 56, no. 2, pp. 1–40, 2023.
- [26] M. Awais, M. Naseer, S. Khan, R. M. Anwer, H. Cholakkal, M. Shah, M.-H. Yang, and F. S. Khan, “Foundation models defining a new era in vision: A survey and outlook,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 47, no. 4, pp. 2245–2264, 2025.
- [27] P. Xu, W. Shao, K. Zhang, P. Gao, S. Liu, M. Lei, F. Meng, S. Huang, Y. Qiao, and P. Luo, “Lvlm-ehub: A comprehensive evaluation benchmark for large vision-language models,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 47, no. 3, pp. 1877–1893, 2025.
- [28] X. Zhou, C. Liu, Z. Chen, K. Wang, Y. Ding, Z. Jia, and Q. Wen, “Brain foundation models: A survey on advancements in neural signal processing and brain discovery,” arXiv preprint arXiv:2503.00580, 2025.
- [29] H. Li, Y. Chen, Y. Wang, W. Ni, and H. Zhang, “Foundation models for cross-domain eeg analysis application: A survey,” arXiv preprint arXiv:2508.15716, 2025.
- [30] X. Gu, Y. Shu, J. Han, Y. Liu, Z. Liu, J. Anibal, V. Sangha, E. Phillips, B. Segal, H. Yuan et al., “Foundation models for biosignals: A survey,” Authorea Preprints, 2025.
- [31] J. Lai, J. Wei, L. Yao, and Y. Wang, “A simple review of eeg foundation models: Datasets, advancements and future perspectives,” arXiv preprint arXiv:2504.20069, 2025.
- [32] S. Yang, X. Huang, D. Bernardo, J.-E. Ding, A. Michael, J. Yang, P. Kwan, A. Raj, and F. Liu, “Foundation and large-scale ai models in neuroscience: A comprehensive review,” arXiv preprint arXiv:2510.16658, 2025.
- [33] N. Lee, K. Barmpas, Y. Panagakis, D. Adamos, N. Laskaris, and S. Zafeiriou, “Are large brainwave foundation models capable yet? insights from fine-tuning,” in Forty-second International Conference on Machine Learning, 2025. [Online]. Available: https: //openreview.net/forum?id=J5SbLoq7Uv
- [34] W. Xiong, J. Li, J. Li, and K. Zhu, “Eeg-fm-bench: A comprehensive benchmark for the systematic evaluation of eeg foundation models,” arXiv preprint arXiv:2508.17742, 2025.
- [35] J. Wu, Z. Ren, J. Wang, P. Zhu, Y. Song, M. Liu, Q. Zheng, L. Bai, W. Ouyang, and C. Song, “Adabrain-bench: Benchmarking brain foundation models for brain-computer interface applications,” arXiv preprint arXiv:2507.09882, 2025.
- [36] P. L. Nunez and R. Srinivasan, Electric fields of the brain: the neurophysics of EEG. Oxford university press, 2006.
- [37] G. Buzs´aki, Rhythms of the Brain. Oxford university press, 2006.
- [38] A. L. Fairhall, G. D. Lewen, W. Bialek, and R. R. de Ruyter van Steveninck, “Efficiency and ambiguity in an adaptive neural code,” Nature, vol. 412, no. 6849, pp. 787–792, 2001.
- [39] S. H. Strogatz, Nonlinear dynamics and chaos: with applications to physics, biology, chemistry, and engineering. Chapman and Hall/CRC, 2024.
- [40] M. Breakspear, “Dynamic models of large-scale brain activity,” Nature neuroscience, vol. 20, no. 3, pp. 340–352, 2017.
- [41] F. Varela, J.-P. Lachaux, E. Rodriguez, and J. Martinerie, “The brainweb: phase synchronization and large-scale integration,” Nature reviews neuroscience, vol. 2, no. 4, pp. 229–239, 2001.
- [42] R. T. Canolty, E. Edwards, S. S. Dalal, M. Soltani, S. S. Nagarajan, H. E. Kirsch, M. S. Berger, N. M. Barbaro, and R. T. Knight, “High gamma power is phase-locked to theta oscillations in human neocortex,” science, vol. 313, no. 5793, pp. 1626–1628, 2006.
- [43] J. S. Richman and J. R. Moorman, “Physiological time-series analysis using approximate entropy and sample entropy,” American journal of physiology-heart and circulatory physiology, vol. 278, no. 6, pp. H2039–H2049, 2000.
- [44] D. J. McFarland, C. W. Anderson, K.-R. Muller, A. Schlogl, and D. J. Krusienski, “Bci meeting 2005-workshop on bci signal processing: feature extraction and translation,” IEEE transactions on neural systems and rehabilitation engineering, vol. 14, no. 2, pp. 135–138, 2006.
- [45] F. Lotte, M. Congedo, A. L´ecuyer, F. Lamarche, and B. Arnaldi, “A review of classification algorithms for eeg-based brain–computer

- interfaces,” Journal of neural engineering, vol. 4, no. 2, p. R1, 2007.
- [46] W. Wu, Z. Chen, X. Gao, Y. Li, E. N. Brown, and S. Gao, “Probabilistic common spatial patterns for multichannel eeg analysis,” IEEE transactions on pattern analysis and machine intelligence, vol. 37, no. 3, pp. 639–653, 2014.
- [47] W. Wang, F. Qi, D. P. Wipf, C. Cai, T. Yu, Y. Li, Y. Zhang, Z. Yu, and W. Wu, “Sparse bayesian learning for end-to-end eeg decoding,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 45, no. 12, pp. 15632–15649, 2023.
- [48] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” nature, vol. 521, no. 7553, pp. 436–444, 2015.
- [49] S. Parvaneh, J. Rubin, S. Babaeizadeh, and M. Xu-Wilson, “Cardiac arrhythmia detection using deep learning: A review,” Journal of electrocardiology, vol. 57, pp. S70–S74, 2019.
- [50] A. Craik, Y. He, and J. L. Contreras-Vidal, “Deep learning for electroencephalogram (eeg) classification tasks: a review,” Journal of neural engineering, vol. 16, no. 3, p. 031001, 2019.
- [51] A. Al-Saegh, S. A. Dawwd, and J. M. Abdul-Jabbar, “Deep learning for motor imagery eeg-based classification: A review,” Biomedical Signal Processing and Control, vol. 63, p. 102172, 2021.
- [52] R. N. Sekkal, F. Bereksi-Reguig, D. Ruiz-Fernandez, N. Dib, and S. Sekkal, “Automatic sleep stage classification: From classical machine learning methods to deep learning,” Biomedical Signal Processing and Control, vol. 77, p. 103751, 2022.
- [53] C. Yang, Z. Wu, P. Jiang, Z. Lin, and J. Sun, “Pyhealth: A deep learning toolkit for healthcare predictive modeling, 09 2022,” URL https://github. com/sunlabuiuc/PyHealth, 2022.
- [54] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for eeg decoding and visualization,” Human brain mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [55] S. Sakhavi, C. Guan, and S. Yan, “Learning temporal information for brain-computer interface using convolutional neural networks,” IEEE transactions on neural networks and learning systems, vol. 29, no. 11, pp. 5619–5629, 2018.
- [56] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces,” Journal of neural engineering, vol. 15, no. 5, p. 056013, 2018.
- [57] Y. Ding, N. Robinson, S. Zhang, Q. Zeng, and C. Guan, “Tsception: Capturing temporal dynamics and spatial asymmetry from eeg for emotion recognition,” IEEE Transactions on Affective Computing, vol. 14, no. 3, pp. 2238–2250, 2022.
- [58] A. Abdelhameed and M. Bayoumi, “A deep learning approach for automatic seizure detection in children with epilepsy,” Frontiers in Computational Neuroscience, vol. 15, p. 650050, 2021.
- [59] P. Wang, A. Jiang, X. Liu, J. Shang, and L. Zhang, “Lstm-based eeg classification in motor imagery tasks,” IEEE transactions on neural systems and rehabilitation engineering, vol. 26, no. 11, pp. 2086–2095, 2018.
- [60] H. Phan, F. Andreotti, N. Cooray, O. Y. Ch´en, and M. De Vos, “Seqsleepnet: end-to-end hierarchical recurrent neural network for sequence-to-sequence automatic sleep staging,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 27, no. 3, pp. 400–410, 2019.
- [61] A. Supratak, H. Dong, C. Wu, and Y. Guo, “Deepsleepnet: A model for automatic sleep stage scoring based on raw single-channel eeg,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 11, pp. 1998–2008, 2017.
- [62] R. Zhang, Q. Zong, L. Dou, and X. Zhao, “A novel hybrid deep learning scheme for four-class motor imagery classification,” Journal of neural engineering, vol. 16, no. 6, p. 066004, 2019.
- [63] M. N. Dar, M. U. Akram, S. G. Khawaja, and A. N. Pujari, “Cnn and lstm-based emotion charting using physiological signals,” Sensors, vol. 20, no. 16, p. 4551, 2020.
- [64] H. Li, M. Ding, R. Zhang, and C. Xiu, “Motor imagery eeg classification algorithm based on cnn-lstm feature fusion network,” Biomedical signal processing and control, vol. 72, p. 103342, 2022.
- [65] J. Wang, S. Cheng, J. Tian, and Y. Gao, “A 2d cnn-lstm hybrid algorithm using time series segments of eeg data for motor imagery classification,” Biomedical Signal Processing and Control, vol. 83, p. 104627, 2023.
- [66] Y. Song, X. Jia, L. Yang, and L. Xie, “Transformer-based spatial-temporal feature learning for eeg decoding,” arXiv preprint arXiv:2106.11170, 2021.
- [67] J. Liu, L. Zhang, H. Wu, and H. Zhao, “Transformers for eeg emotion

- recognition,” arXiv preprint arXiv:2110.06553, 2021.
- [68] Y. Du, Y. Xu, X. Wang, L. Liu, and P. Ma, “Eeg temporal–spatial transformer for person identification,” Scientific Reports, vol. 12, no. 1, p. 14378, 2022.
- [69] H. Phan, K. Mikkelsen, O. Y. Ch´en, P. Koch, A. Mertins, and M. De Vos, “Sleeptransformer: Automatic sleep staging with interpretability and uncertainty quantification,” IEEE Transactions on Biomedical Engineering, vol. 69, no. 8, pp. 2456–2467, 2022.
- [70] Y. Song, Q. Zheng, B. Liu, and X. Gao, “Eeg conformer: Convolutional transformer for eeg decoding and visualization,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 710–719, 2022.
- [71] W. Y. Peh, Y. Yao, and J. Dauwels, “Transformer convolutional neural networks for automated artifact detection in scalp eeg,” in 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC). IEEE, 2022, pp. 3599–3602.
- [72] J. Wang, S. Zhao, Y. Zhou, H. Jiang, Z. Yu, T. Li, S. Li, and G. Pan, “Narcolepsy diagnosis with sleep stage features using psg recordings,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 3619–3629, 2023.
- [73] Y. Zhou, S. Zhao, J. Wang, H. Jiang, Z. Yu, S. Li, T. Li, and G. Pan, “Simplifying multimodal with single eog modality for automatic sleep staging,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 32, pp. 1668–1678, 2024.
- [74] J. Wang, S. Zhao, H. Jiang, Y. Zhou, Z. Yu, T. Li, S. Li, and G. Pan, “Caresleepnet: A hybrid deep learning network for automatic sleep staging,” IEEE Journal of Biomedical and Health Informatics, 2024.
- [75] Z. Jia, Y. Lin, J. Wang, R. Zhou, X. Ning, Y. He, and Y. Zhao, “Graphsleepnet: Adaptive spatial-temporal graph convolutional networks for sleep stage classification.” in IJCAI, vol. 2021, 2020, pp. 1324–1330.
- [76] Z. Jia, Y. Lin, J. Wang, X. Ning, Y. He, R. Zhou, Y. Zhou, and H. L. Liwei, “Multi-view spatial-temporal graph convolutional networks with domain generalization for sleep stage classification,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 29, pp. 1977–1986, 2021.
- [77] Y. Ding, N. Robinson, C. Tong, Q. Zeng, and C. Guan, “Lggnet: Learning from local-global-graph representations for brain–computer interface,” IEEE Transactions on Neural Networks and Learning Systems, pp. 1–14, 2023.
- [78] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep bidirectional transformers for language understanding,” arXiv preprint arXiv:1810.04805, 2018.
- [79] K. He, X. Chen, S. Xie, Y. Li, P. Doll´ar, and R. Girshick, “Masked autoencoders are scalable vision learners,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2022, pp. 16000–16009.
- [80] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark et al., “Learning transferable visual models from natural language supervision,” in Proceedings of the 38th International Conference on Machine Learning, ser. Proceedings of Machine Learning Research, M. Meila and T. Zhang, Eds., vol. 139. PMLR, 18–24 Jul 2021, pp. 8748–8763.
- [81] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “Gpt-4 technical report,” arXiv preprint arXiv:2303.08774, 2023.
- [82] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W.-Y. Lo et al., “Segment anything,” in Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023, pp. 4015–4026.
- [83] T. Brooks, B. Peebles, C. Holmes, W. DePue, Y. Guo, L. Jing, D. Schnurr, J. Taylor, T. Luhman, E. Luhman, C. Ng, R. Wang, and A. Ramesh, “Video generation models as world simulators,” 2024. [Online]. Available: https: //openai.com/research/video-generation-models-as-world-simulators
- [84] E. Eldele, M. Ragab, Z. Chen, M. Wu, C. K. Kwoh, X. Li, and C. Guan, “Time-series representation learning via temporal and contextual contrasting,” arXiv preprint arXiv:2106.14112, 2021.
- [85] X. Zhang, Z. Zhao, T. Tsiligkaridis, and M. Zitnik, “Self-supervised contrastive pre-training for time series via time-frequency consistency,” in Advances in Neural Information Processing Systems, S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh, Eds., vol. 35. Curran Associates, Inc., 2022, pp. 3988–4003.
- [86] G. Woo, C. Liu, A. Kumar, C. Xiong, S. Savarese, and D. Sahoo, “Unified training of universal time series forecasting transformers,” arXiv preprint arXiv:2402.02592, 2024.
- [87] M. Chen, L. Shen, Z. Li, X. J. Wang, J. Sun, and C. Liu, “Visionts: Visual masked autoencoders are free-lunch zero-shot time series fore-

- casters,” arXiv preprint arXiv:2408.17253, 2024.
- [88] G. Deng, M. Niu, Y. Luo, S. Rao, J. Sun, J. Xie, Z. Yu, W. Liu, S. Zhao, G. Pan, X. Li, W. Deng, W. Guo, T. Li, and H. Jiang, “Lpsgm: A unified flexible large psg model for sleep staging and mental disorder diagnosis,” medRxiv, 2024. [Online]. Available: https: //www.medrxiv.org/content/early/2024/12/11/2024.12.11.24318815
- [89] H. Banville, O. Chehab, A. Hyv¨arinen, D.-A. Engemann, and A. Gramfort, “Uncovering the structure of clinical eeg signals with selfsupervised learning,” Journal of Neural Engineering, vol. 18, no. 4, p. 046020, 2021.
- [90] D. Kostas, S. Aroca-Ouellette, and F. Rudzicz, “Bendr: using transformers and a contrastive self-supervised learning task to learn from massive amounts of eeg data,” Frontiers in Human Neuroscience, vol. 15, p. 653659, 2021.
- [91] H.-Y. S. Chien, H. Goh, C. M. Sandino, and J. Y. Cheng, “Maeeg: Masked auto-encoder for eeg representation learning,” arXiv preprint arXiv:2211.02625, 2022.
- [92] C. Wang, V. Subramaniam, A. U. Yaari, G. Kreiman, B. Katz, I. Cases, and A. Barbu, “Brainbert: Self-supervised representation learning for intracranial recordings,” in The Eleventh International Conference on Learning Representations, 2022.
- [93] D. Zhang, Z. Yuan, Y. Yang, J. Chen, J. Wang, and Y. Li, “Brant: Foundation model for intracranial neural signal,” in Advances in Neural Information Processing Systems, 2023.
- [94] Z. Yuan, D. Zhang, J. Chen, G. Gu, and Y. Yang, “Brant-2: Foundation model for brain signals,” arXiv preprint arXiv:2402.10251, 2024.
- [95] D. Zhang, Z. Yuan, J. Chen, K. Chen, and Y. Yang, “Brant-x: A unified physiological signal alignment framework,” in Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, 2024, pp. 4155–4166.
- [96] C. Yang, M. Westover, and J. Sun, “Biot: Biosignal transformer for cross-data learning in the wild,” in Advances in Neural Information Processing Systems, vol. 36, 2023, pp. 78240–78260.
- [97] N. M. Foumani, G. Mackellar, S. Ghane, S. Irtza, N. Nguyen, and M. Salehi, “Eeg2rep: Enhancing self-supervised eeg representation through informative masked inputs,” arXiv preprint arXiv:2402.17772, 2024.
- [98] W. Jiang, L. Zhao, and B. liang Lu, “Large brain model for learning generic representations with tremendous EEG data in BCI,” in The Twelfth International Conference on Learning Representations, 2024. [Online]. Available: https://openreview.net/forum?id=QzTpTRVtrP
- [99] W. Cui, W. Jeong, P. Th¨olke, T. Medani, K. Jerbi, A. A. Joshi, and R. M. Leahy, “Neuro-gpt: Towards a foundation model for eeg,” in 2024 IEEE International Symposium on Biomedical Imaging (ISBI). IEEE, 2024, pp. 1–5.
- [100] G. Wang, W. Liu, Y. He, C. Xu, L. Ma, and H. Li, “EEGPT: Pretrained transformer for universal and reliable representation of EEG signals,” in The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024. [Online]. Available: https://openreview.net/forum?id=lvS2b8CjG5
- [101] W.-B. Jiang, Y. Wang, B.-L. Lu, and D. Li, “NeuroLM: A universal multi-task foundation model for bridging the gap between language and EEG signals,” in The Thirteenth International Conference on Learning Representations, 2025. [Online]. Available: https://openreview.net/forum?id=Io9yFt7XH7
- [102] W. Lu, C. Song, J. Wu, P. Zhu, Y. Zhou, W. Mai, Q. Zheng, and W. Ouyang, “Unimind: Unleashing the power of llms for unified multitask brain decoding,” arXiv preprint arXiv:2506.18962, 2025.
- [103] M. Jiang, S. Zhang, Z. Yang, M. Wu, W. Jiang, Z. Guo, W. Zhang, R. Liu, S. Zhang, Y. Li et al., “Elastiq: Eeg-language alignment with semantic task instruction and querying,” arXiv preprint arXiv:2509.24302, 2025.
- [104] J. Wang, S. Zhao, Z. Luo, Y. Zhou, H. Jiang, S. Li, T. Li, and G. Pan, “CBramod: A criss-cross brain foundation model for EEG decoding,” in The Thirteenth International Conference on Learning Representations, 2025. [Online]. Available: https: //openreview.net/forum?id=NPNUHgHF2w
- [105] J. Wang, S. Zhao, Z. Luo, Y. Zhou, S. Li, and G. Pan, “Eegmamba: An eeg foundation model with mamba,” Neural Networks, p. 107816, 2025.
- [106] J. Ma, F. Wu, Q. Lin, Y. Xing, C. Liu, Z. Jia, and M. Feng, “Codebrain: Bridging decoupled tokenizer and multi-scale architecture for eeg foundation model,” arXiv preprint arXiv:2506.09110, 2025.
- [107] B. D¨oner, T. M. Ingolfsson, L. Benini, and Y. Li, “LUNA: Efficient and topology-agnostic foundation model for EEG signal analysis,” in The Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025. [Online]. Available: https:

- //openreview.net/forum?id=uazfjnFL0G
- [108] Z. Fang, C. Li, H. Zhou, S. Yu, G. Du, A. Qasem, Y. Lu, J. Li, J. Zhang, and S. K. Goh, “Neuript: Foundation model for neural interfaces,” arXiv preprint arXiv:2510.16548, 2025.
- [109] Y. Zhou, J. Wu, Z. Ren, Z. Yao, W. Lu, K. Peng, Q. Zheng, C. Song, W. Ouyang, and C. Gou, “Csbrain: A cross-scale spatiotemporal brain foundation model for eeg decoding,” arXiv preprint arXiv:2506.23075, 2025.
- [110] Q. Xiao, Z. Cui, C. Zhang, S. Chen, W. Wu, A. Thwaites, A. Woolgar, B. Zhou, and C. Zhang, “Brainomni: A brain foundation model for unified eeg and meg signals,” arXiv preprint arXiv:2505.18185, 2025.
- [111] Y. E. Ouahidi, J. Lys, P. Th¨olke, N. Farrugia, B. Pasdeloup, V. Gripon, K. Jerbi, and G. Lioi, “Reve: A foundation model for eeg–adapting to any setup with large-scale pretraining on 25,000 subjects,” arXiv preprint arXiv:2510.21585, 2025.
- [112] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly et al., “An image is worth 16x16 words: Transformers for image recognition at scale,” arXiv preprint arXiv:2010.11929, 2020.
- [113] R. Grech, T. Cassar, J. Muscat, K. P. Camilleri, S. G. Fabri, M. Zervakis, P. Xanthopoulos, V. Sakkalis, and B. Vanrumste, “Review on solving the inverse problem in eeg source analysis,” Journal of neuroengineering and rehabilitation, vol. 5, no. 1, p. 25, 2008.
- [114] Q. Wang, B. Li, T. Xiao, J. Zhu, C. Li, D. F. Wong, and L. S. Chao, “Learning deep transformer models for machine translation,” in Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, 2019, pp. 1810–1822.
- [115] P. J. Huber, “Robust estimation of a location parameter,” in Breakthroughs in statistics: Methodology and distribution. Springer, 1992, pp. 492–518.
- [116] G. Buzs´aki, “Neural syntax: cell assemblies, synapsembles, and readers,” Neuron, vol. 68, no. 3, pp. 362–385, 2010.
- [117] M. Arjovsky, L. Bottou, I. Gulrajani, and D. Lopez-Paz, “Invariant risk minimization,” arXiv preprint arXiv:1907.02893, 2019.
- [118] I. Obeid and J. Picone, “The temple university hospital eeg data corpus,” Frontiers in neuroscience, vol. 10, p. 196, 2016.
- [119] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, “Physiobank, physiotoolkit, and physionet: components of a new research resource for complex physiologic signals.” Circulation, vol. 101 23, pp. E215–20, 2000.
- [120] M. M. Ghassemi, B. E. Moody, L.-W. H. Lehman, C. Song, Q. Li, H. Sun, R. G. Mark, M. B. Westover, and G. D. Clifford, “You snooze, you win: the physionet/computing in cardiology challenge 2018,” in 2018 Computing in Cardiology Conference (CinC), vol. 45. IEEE, 2018, pp. 1–4.
- [121] L. Trujillo, “Raw EEG Data,” 2020. [Online]. Available: https: //doi.org/10.18738/T8/SS2NHB
- [122] P. Detti, G. Vatti, and G. Zabalo Manrique de Lara, “Eeg synchronization analysis for seizure prediction: A study on data of noninvasive recordings,” Processes, vol. 8, no. 7, p. 846, 2020.
- [123] M. Melc´on, E. Stern, D. Kessel, L. Arana, C. Poch, P. Campo, and A. Capilla, “Perception of near-threshold visual stimuli is influenced by prestimulus alpha-band amplitude but not by alpha phase,” Psychophysiology, vol. 61, no. 5, p. e14525, 2024.
- [124] M. Melc´on, E. Stern, L. Arana, and A. Capilla, “Eeg data during three near-threshold visual detection tasks: a no-cue task, a noninformative cue task (50% validity), and an informative cue task (100% validity),” 2025.
- [125] Z. Zhang, X. Ding, Y. Bao, Y. Zhao, X. Liang, B. Qin, and T. Liu, “Chisco: An eeg-based bci dataset for decoding of imagined speech,” Scientific Data, vol. 11, no. 1, p. 1265, 2024.
- [126] Z. Zhang, Y. Bao, T. Jiang, X. Ding, X. Liang, J. Du, Y. Zhao, K. Xiong, B. Qin, and T. Liu, “Chisco-2.0,” 2025.
- [127] xx, “Memory reactivation levels remain unaffected by anticipated interference,” 2025.
- [128] X, “Memory reactivation levels remain unaffected by anticipated interference experiment 2 dataset,” 2025.
- [129] anonymous, “Light hypnotherapy,” 2025.
- [130] K. Nashiro, H. J. Yoo, C. Cho, A. J. Kim, P. Nasseri, J. Min, M. J. Dahl, N. Mercer, J. Choupan, P. Choi et al., “Heart rate and breathing effects on attention and memory (heartbeam): Study protocol for a randomized controlled trial in older adults,” Trials, vol. 25, no. 1, p. 190, 2024.
- [131] A. J. Kim, S. Morales, J. Senior, and M. Mather, “Electroencephalography, pupillometry, and behavioral evidence for locus coeruleusnoradrenaline system related tonic hyperactivity in older adults,”

- bioRxiv, pp. 2025–10, 2025.
- [132] I. Kinley and S. Becker, “Cueing the future to reduce temporal discounting,” 2025.
- [133] A. J. Kim, S. Morales, J. Senior, and M. Mather, “Heartbeam: Older adult resting state and auditory oddball task eeg data,” 2025.
- [134] G. Shou, H. Yuan, C. Li, Y. Chen, Y. Chen, and L. Ding, “Whole-brain electrophysiological functional connectivity dynamics in resting-state eeg,” Journal of neural engineering, vol. 17, no. 2, p. 026016, 2020.
- [135] A. J. Kim, M. Mather, S. Morales, and J. Senior, “Young adult resting state and auditory oddball task eeg data,” 2025.
- [136] C. Neuroimaging and N. L. ar the University of Oklahoma, “Resting eeg,” 2025.
- [137] S. Ghaffari, A. Yavari, S. Bonyadian, A. Ghofrani, and R. Butler, “Visual eeg study (brainvision → bids),” 2025.
- [138] J. Chen, X. Wang, C. Huang, X. Hu, X. Shen, and D. Zhang, “A large finer-grained affective computing eeg dataset,” Scientific Data, vol. 10, no. 1, p. 740, 2023.
- [139] W. Liu, J.-L. Qiu, W.-L. Zheng, and B.-L. Lu, “Comparing recognition performance and robustness of multimodal deep learning models for multimodal emotion recognition,” IEEE Transactions on Cognitive and Developmental Systems, vol. 14, no. 2, pp. 715–729, 2021.
- [140] W.-B. Jiang, X.-H. Liu, W.-L. Zheng, and B.-L. Lu, “Seed-vii: A multimodal dataset of six basic emotions with continuous labels for emotion recognition,” IEEE Transactions on Affective Computing, 2024.
- [141] A. L. Goldberger, L. A. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, “Physiobank, physiotoolkit, and physionet: components of a new research resource for complex physiologic signals,” circulation, vol. 101, no. 23, pp. e215–e220, 2000.
- [142] C. Brunner, R. Leeb, G. M¨uller-Putz, A. Schl¨ogl, and G. Pfurtscheller, “Bci competition 2008–graz data set a,” Institute for knowledge discovery (laboratory of brain-computer interfaces), Graz University of Technology, vol. 16, pp. 1–6, 2008.
- [143] J. Ma, B. Yang, W. Qiu, Y. Li, S. Gao, and X. Xia, “A large eeg dataset for studying cross-session variability in motor imagery brain-computer interface,” Scientific Data, vol. 9, no. 1, p. 531, 2022.
- [144] S. Khalighi, T. Sousa, J. M. Santos, and U. Nunes, “Isruc-sleep: A comprehensive public dataset for sleep researchers,” Computer methods and programs in biomedicine, vol. 124, pp. 180–192, 2016.
- [145] A. H. Shoeb, “Application of machine learning to epileptic seizure onset detection and treatment,” Ph.D. dissertation, Massachusetts Institute of Technology, 2009.
- [146] J.-H. Jeong, J.-H. Cho, Y.-E. Lee, S.-H. Lee, G.-H. Shin, Y.-S. Kweon, J. d. R. Mill´an, K.-R. M¨uller, and S.-W. Lee, “2020 international brain–computer interface competition: A review,” Frontiers in Human Neuroscience, vol. 16, p. 898300, 2022.
- [147] H. Cai, Z. Yuan, Y. Gao, S. Sun, N. Li, F. Tian, H. Xiao, J. Li, Z. Yang, X. Li et al., “A multi-modal open dataset for mental-disorder analysis,” Scientific Data, vol. 9, no. 1, p. 178, 2022.
- [148] J. Min, P. Wang, and J. Hu, “Driver fatigue detection through multiple entropy fusion analysis in an eeg-based system,” PLoS one, vol. 12, no. 12, p. e0188756, 2017.
- [149] I. Zyma, S. Tukaev, I. Seleznov, K. Kiyono, A. Popov, M. Chernykh, and O. Shpenkov, “Electroencephalograms during mental arithmetic task performance,” Data, vol. 4, no. 1, p. 14, 2019.
- [150] OpenNeuro, “Openneuro: A free and open platform for validating and sharing bids-compliant mri, pet, meg, eeg, and ieeg data,” 2025. [Online]. Available: https://openneuro.org

[Figure 17]

Jiquan Wang received the Ph.D. degree in Computer Science and Technology from Zhejiang University, Hangzhou, China, in 2025.

He is currently a research fellow at the State Key Laboratory of Brain-Machine Intelligence, Zhejiang University. His research interests include EEG decoding, brain-computer interfaces and artificial intelligence. He received the 2025 ACM Hangzhou Outstanding Doctoral Dissertation Award.

[Figure 18]

Sha Zhao received the Ph.D. degree from Zhejiang University, Hangzhou, China, in 2017.

She is currently a research professor with the College of Computer Science and Technology, Zhejiang University. She visited the Human-Computer Interaction Institute, Carnegie Mellon University, Pittsburgh, PA, USA, as a visiting Ph.D. student from 2015 to 2016. Her research interests include brain-machine interfaces, data mining and machine learning. Dr. Zhao received the Best Paper Award of ACM UbiComp’16.

[Figure 19]

Yangxuan Zhou received the B.S. degree in Electronic Information from Shanghai University, Shanghai, China, in 2022.

He is currently working toward the Ph.D. degree of Computer Science and Technology with Zhejiang University, Hangzhou, China. His research interests include EEG decoding, Brain-Computer Interfaces, Deep Learning, and Artificial Intelligence.

[Figure 20]

Yiming Kang received the B.S. degree in Artificial Intelligence from Soochow University, Suzhou, China, in 2024.

He has been pursuing the M.S. degree in Electronic Information with Zhejiang University, Hangzhou, China, since 2025. His research primarily focuses on multimodal brain foundation model in the field of non-invasive brain-computer interfaces (BCI).

VII. BIOGRAPHY SECTION

[Figure 21]

Shijian Li received the Ph.D. degree from Zhejiang University, Hangzhou, China, in 2006.

In 2010, he was a Visiting Scholar with the Institute Telecom SudParis, Evry,´ France. He is currently with the College of Computer Science and Technology, Zhejiang University. He has published over 40 papers. His research interests include sensor networks, ubiquitous computing, and social computing. Dr. Li serves as an Editor for the International Journal of Distributed Sensor Networks and as a reviewer or the PC member of over ten conferences.

[Figure 22]

Gang Pan (Senior Member, IEEE) received the B.Eng. and Ph.D. degrees from Zhejiang University, Hangzhou, China, in 1998 and 2004, respectively.

He is currently a Professor with the Department of Computer Science, and the Director of the State Key Laboratory of Brain-Machine Intelligence, Zhejiang University. From 2007 to 2008, he was a Visiting Scholar with the University of California, Los Angeles, CA, USA. His current interests include brain-inspired computing, brain-machine interfaces and artificial intelligence.

