# DBConformer: Dual-Branch Convolutional Transformer for EEG Decoding

Ziwei Wang, Hongbin Wang, Tianwang Jia, Xingyi He, Siyang Li, and Dongrui Wu∗, Fellow, IEEE

## arXiv:2506.21140v2[cs.LG]19Sep2025

Abstract—Electroencephalography (EEG)-based braincomputer interfaces (BCIs) transform spontaneous/evoked neural activity into control commands for external communication. While convolutional neural networks (CNNs) remain the mainstream backbone for EEG decoding, their inherently short receptive ﬁeld makes it difﬁcult to capture long-range temporal dependencies and global inter-channel relationships. Recent CNN-Transformer (Conformer) hybrids partially address this issue, but most adopt a serial design, resulting in suboptimal integration of local and global features, and often overlook explicit channel-wise modeling. To address these limitations, we propose DBConformer, a dual-branch convolutional Transformer network tailored for EEG decoding. It integrates a temporal Conformer to model long-range temporal dependencies and a spatial Conformer to extract inter-channel interactions, capturing both temporal dynamics and spatial patterns in EEG signals. A lightweight channel attention module further reﬁnes spatial representations by assigning data-driven importance to EEG channels. Extensive experiments under four evaluation settings on three paradigms, including motor imagery, seizure detection, and steady-state visual evoked potential, demonstrated that DBConformer consistently outperformed 13 competitive baseline models, with over an eight-fold reduction in parameters than current high-capacity EEG Conformer architecture. Furthermore, the visualization results conﬁrmed that the features extracted by DBConformer are physiologically interpretable and aligned with prior knowledge. The superior performance and interpretability of DBConformer make it reliable for accurate, robust, and explainable EEG decoding. Code is publicized at https://github.com/wzwvv/DBConformer.

Index Terms—Brain-computer interface, electroencephalography, motor imagery, seizure detection, convolutional neural networks, Transformer

I. INTRODUCTION

A brain-computer interface (BCI) provides a direct communication pathway between cortical activity and external devices [1]. Non-invasive BCIs based on electroencephalography (EEG) have gained prominence because EEG sensors are inexpensive, portable, and safe for extended use [2]. Nevertheless, the low signal-to-noise ratio, non-stationarity, and signiﬁcant inter-subject variability of scalp EEG impose stringent requirements on the decoding model that translates raw signals into task-relevant information.

This study focuses on three signiﬁcant EEG decoding tasks:

This research was supported by Major Science and Technology Project of Industry-university-research Cooperation for Colleges and Universities in Hebei Province in Shijiazhuang City 2511303107A.

Z. Wang, H. Wang, T. Jia, X. He, S. Li, and D. Wu are with the Ministry of Education Key Laboratory of Image Processing and Intelligent Control, School of Artiﬁcial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China.

*Corresponding Author: Dongrui Wu (drwu09@gmail.com).

- 1) Motor imagery (MI) classiﬁcation [3], which enables brain-based control of devices/prostheses. During MI, users imagine the movement of speciﬁc body parts, producing event-related desynchronization/synchronization patterns over the brain’s motor cortex [4].
- 2) Epileptic seizure detection [5], a task of automated neurological monitoring. Epilepsy, affecting over 70 million people worldwide [6], is characterized by recurrent seizures. Continuous EEG monitoring remains the gold standard for seizure detection.
- 3) Steady-state visual evoked potential (SSVEP) [7] recognition, which occurs when users ﬁxate on ﬂickering visual stimuli, producing EEG responses at the same stimulus frequency and its harmonics.

The decoding model is essential for effective EEG decoding and has been a research hotspot of BCIs. Three trends have emerged in the design of EEG decoding models:

- 1) Model Type: Classic convolutional neural networks (CNNs), such as EEGNet [8], Shallow CNN (SCNN), and Deep CNN (DCNN) [9], exploit local spatiotemporal patterns but struggle with global temporal dependencies. CNN-Transformer (Conformer) hybrids extend CNN locality with self-attention based global context. Yet, prior work [10]–[13] stacks the two modules serially, restricting interaction between local and global features and neglecting explicit spatial modeling.
- 2) Architecture Parallelism and Depth: Networks evolve from shallow, single-branch (e.g., EEGNet) to deeper, multi-branch designs with more parameters and layers that process frequency bands or multi-resolution inputs in parallel (e.g., FBCNet [14], IFNet [15], and ADFCNN [16]), enhancing feature diversity.
- 3) Multi-View Information Fusion: Recent studies consider incorporating temporal, spatial, or spectral domain priors explicitly, such as EEG data augmentation [17], [18], time-frequency transforms [19], [20], frequency band modeling [15], [21], and spatial ﬁltering initialization [22]. However, existing approaches typically consider these domain priors separately rather than jointly.

Overall, the latest serial Conformer hybrids ﬁrst compress EEG trials into patch embeddings by CNN blocks and then utilize self-attention to capture global long-range dependencies. Although they are effective for certain tasks, this type of architecture forces all spatial information to pass through a temporal bottleneck, preventing interaction between local and global characteristics. Notably, some Conformer hybrids have large model sizes, e.g., EEG Conformer has around

0.8M parameters, which increases computational cost and may overﬁt on limited EEG data. Besides, spatial inter-channel relationships, often captured in early CNN layers, may be overwhelmed in later blocks, limiting the model’s capacity to leverage spatial information crucial for MI classiﬁcation and seizure detection. A balanced, parallel design that treats temporal and spatial patterns symmetrically remains absent.

- classiﬁcation accuracy and interpretability without requiring additional supervision.
- 3) Extensive experiments on three paradigms validated that DBConformer almost always outperforms 13 competitive baseline models. Furthermore, it achieves this superior performance with over an eight-fold reduction in parameters than the high-capacity EEG Conformer baseline, demonstrating both effectiveness and efﬁciency.
- 4) Beyond achieving state-of-the-art performance, DBConformer exhibits biologically interpretability, i.e., its learned channel attention scores consistently emphasize sensorimotor-related electrodes (e.g., C3, Cz, C4), aligning well with known neurophysiological priors.

To address the above limitations, we propose DBConformer, a dual-branch convolutional Transformer architecture that performs parallel spatio-temporal representation learning for EEG decoding. The temporal Conformer (T-Conformer) extracts hierarchical temporal dynamics by integrating depthwise temporal convolutions with multi-head self-attention, whereas the spatial Conformer (S-Conformer) utilizes pointwise convolutions and channel-wise self-attention to model spatial dependencies. A lightweight channel attention module adaptively reﬁnes spatial saliency before branch fusion. In each branch, CNN extracts temporal/spatial local representations, and Transformer captures global dependencies in the temporal or channel horizon. The comparison of network architectures among CNNs, traditional serial Conformers, and the proposed DBConformer, illustrated in Fig. 1.

The remainder of this paper is organized as follows: Section II reviews related works. Section III details the proposed DBConformer. Section IV discusses the experimental results and provides analyses. Section V draws conclusions.

II. RELATED WORKS

EEG decoding has progressed from traditional hand-crafted pipelines to large-scale, end-to-end deep learning architectures. Recent advancements focus on the model design, including CNN-based, CNN-Transformer hybrid, and the emerging CNN-Mamba architectures. A review of current EEG decoding models is shown in Table I.

[Figure 1]

Early approaches to MI classiﬁcation heavily relied on spatial ﬁltering [23] to maximize inter-class variance. In automatic seizure detection, prior features were manually extracted and classiﬁed by classiﬁers such as support vector machines [24] and random forest [25]. These pipelines required substantial domain expertise and manual effort for feature extraction, motivating a shift toward end-to-end deep learning models.

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

- A. CNNs

CNNs are well-suited for modeling the local spatio-temporal characteristics of EEG data. Lightweight CNN models such as EEGNet [8], SCNN [9], FBCNet [14], and IFNet [15] achieve competitive performance with relatively few parameters. FBMSNet [21] employs multi-scale convolutional blocks to enlarge the receptive ﬁeld by parallelizing convolutions across different frequency bands. EEGWaveNet [26] introduces a multi-scale temporal CNN architecture with depthwise ﬁlters that are channel-speciﬁc, extracting multi-scale features from trials of each EEG channel for seizure detection. However, the inherently local nature of convolutional kernels limits their ability to capture long-range temporal dependencies and global spatial patterns.

- B. Serial CNN-Transformer Hybrids

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

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

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

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

- Fig. 1. Comparison of network architectures among CNNs (EEGNet [8], SCNN [9], DCNN [9], etc), traditional serial CNN-Transformer hybrids (EEG Conformer [10], CTNet [11], etc), and the proposed DBConformer. DBConformer has two branches that parallel capture temporal and spatial characteristics.

The main contributions of this work are summarized as follows:

- 1) We propose DBConformer, a dual-branch convolutional Transformer network for EEG decoding. It incorporates a temporal branch T-Conformer and a spatial branch SConformer, enabling simultaneous modeling of temporal dynamics and spatial patterns in EEG signals.
- 2) A lightweight, plug-and-play channel attention module is introduced to learn the relative importance of each EEG channel in a data-driven manner. This module reweights spatial features before fusion, enhancing both

To incorporate global information, recent EEG decoding architectures incorporate Transformers into CNNs, typically following a serial architecture. Speciﬁcally, EEG Conformer [10], CTNet [11], EEG-Deformer [12], SE-TSS-Transformer [13], and DFformer [32] ﬁrst compress EEG trials into patch embeddings using convolutional blocks, and subsequently apply Transformer layers to capture long-range dependencies.

TABLE I A REVIEW OF CURRENT EEG DECODING MODELS.

[Figure 75]

[Figure 76]

Model Type Model Name Model Structure # Branches Explicit Information Fusion Paradigms

[Figure 77]

[Figure 78]

EEGNet [8] Serial 1 No MI SCNN [9] Serial 1 No MI DCNN [9] Serial 1 No MI

[Figure 79]

[Figure 80]

[Figure 81]

FBCNet [14] Parallel 9 Spectral MI FBMSNet [21] Parallel 4 Spectral MI

CNN

[Figure 82]

[Figure 83]

IFNet [15] Parallel 2 Spectral MI ADFCNN [16] Parallel 2 No MI

[Figure 84]

[Figure 85]

EEGWaveNet [26] Parallel 5 No Seizure detection

[Figure 86]

[Figure 87]

MI, seizure detection, sleep stage classiﬁcation, and emotion recognition MI-Mamba [28] Serial 1 No MI

EEGMamba [27] Serial 1 No

[Figure 88]

[Figure 89]

CNN-Mamba

[Figure 90]

EEG VMamba [29] Serial 1 No Seizure prediction

[Figure 91]

SlimSeiz [30] Serial 1 No Seizure prediction BiT-MamSleep [31] Serial 1 No Sleep stage classiﬁcation

[Figure 92]

[Figure 93]

[Figure 94]

EEG Conformer [10] Serial 1 No MI, emotion recognition CTNet [11] Serial 1 No MI

[Figure 95]

[Figure 96]

EEG-Deformer [12] Serial 1 No Event-related potentials SE-TSS-Transformer [13] Serial 1 No Seizure detection

[Figure 97]

[Figure 98]

DFformer [32] Serial 1 No MI, sleep stage classiﬁcation MI-CAT [33] Serial 1 No MI

[Figure 99]

[Figure 100]

MSCFormer [34] Parallel 3 Temporal MI TMSA-Net [35] Parallel 2 Temporal MI MSVTNet [36] Parallel 4 Temporal MI Dual-TSST [37] Parallel 2 Temporal MI, emotion recognition

[Figure 101]

CNN-Transformer

[Figure 102]

[Figure 103]

[Figure 104]

GAT [38] Serial 1 No MI MVCNet [17] Parallel 2 Temporal, spatial, and spectral MI

[Figure 105]

[Figure 106]

[Figure 107]

DBConformer (Ours) Parallel 2 Temporal, spatial MI, seizure detection

[Figure 108]

In particular, MI-CAT [33] extracts intra-domain and interdomain features through a temporal-spatial CNN module followed by stacked Transformer blocks. GAT [38] combines parallel convolutions with an attention adaptor to enhance domain transferability. Similarly, MSCFormer [34] and TMSANet [35] integrate multi-branch, multi-scale CNNs with Transformer encoders to jointly model local and global EEG representations. MSVTNet [36] further extracts local spatiotemporal features at different ﬁltered scales and introduces an auxiliary branch loss to facilitate effective CNN-Transformer integration.

Other works employ additional data transformations. For instance, Dual-TSST [37] applies a wavelet transform to EEG signals and then extracts temporal-spatial-spectral representations from both raw and transformed data via dual CNN branches, followed by Transformer-based fusion. MVCNet [17] is a multi-view contrastive network utilizing multi-domain EEG data augmentations and incorporating both cross-view and cross-model modules for MI decoding.

However, this serial design constrains information ﬂow to a single pathway, where local and global features are processed sequentially. As a result, spatial inter-channel relationships, often captured in early CNN layers, may be overwhelmed in later blocks, limiting the model’s capacity to leverage spatial information. Neuroscientiﬁc studies further suggest that temporal and spatial information are processed by partly dissociable mechanisms in the brain [39], [40], reinforcing the motivation for architectures that explicitly decouple and then integrate temporal and spatial representations.

C. Other Architectures

Mamba [41], a recently proposed alternative to Transformers, provides efﬁcient modeling of long-range dependencies with reduced computational cost. EEGMamba [27] and MIMamba [28] integrate Mamba blocks following CNN layers, adhering to the same serial structure of CNN-Transformer hybrids. However, parallel architectures that jointly model temporal and spatial patterns remain underexplored.

Some research explores architectures beyond CNNs, including full self-attention mechanisms [42], [43], graph neural networks [44]–[47], and long short term memory layers [48]. Transformer-based models capture long-range dependencies, and graph neural networks leverage electrode topology to reﬁne spatial characteristics. These models are typically parameter-intensive and rarely integrate local feature extraction with global modeling.

Overall, CNNs excel at modeling local spatio-temporal features. CNN-Transformer and CNN-Mamba hybrids offer broader temporal modeling but are limited by the serial design, overlooking the interaction between local and global representations, as well as the spatial patterns.

III. DBCONFORMER A. Overview

This section details the proposed DBConformer, illustrated in Fig. 2. In contrast to conventional single-branch EEG decoding networks, such as CNN-based models or serial CNNTransformer hybrids, DBConformer adopts a parallel dualbranch structure to better leverage the advantages of CNN

| | |
|---|---|
| | |

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

| | |
|---|---|
| | |

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

- Fig. 2. Architecture of the proposed DBConformer for EEG decoding.

1) Motivation of Dual-Branch Design: EEG decoding requires simultaneously modeling ﬁne-grained temporal oscillations and spatially distributed cortical activations. Most existing CNN-Transformer hybrids adopt serial designs, where CNN layers ﬁrst extract embeddings that are subsequently reﬁned by Transformer blocks. Such designs tend to bias the model toward either local feature extraction (when CNN dominates) or global dependency modeling (when Transformer dominates), leading to limited complementarity.

and Transformer. Speciﬁcally, T-Conformer captures longrange temporal dependencies, and S-Conformer models interchannel relations. A lightweight channel attention module is further incorporated to enhance spatial representations by assigning adaptive, data-driven weights to individual EEG channels. The outputs from both branches are concatenated and fed into the classiﬁer to obtain the ﬁnal predictions.

- B. Data Normalization

The raw EEG trials of a batch are X∈RB×C×T, where B is the batch size, C the number of channels, and T the number of time samples. We apply Euclidean alignment (EA) [49] to align the original trials from each subject in the Euclidean space. Assume a subject has n trials, EA can be formulated as the following for the i-th trial:

X˜i = R¯−1/2Xi, (1)

where R¯ is the arithmetic mean of all covariance matrices from a subject:

R¯ =

1 n

[Figure 125]

n

i=1

XiXiT. (2)

After EA, data distribution discrepancies from different subjects are effectively decreased.

- C. Network Architecture

By contrast, DBConformer explicitly decouples temporal and spatial learning into parallel branches with distinct inductive biases:

- • The temporal branch emphasizes local spectral-temporal patterns while also modeling long-range dependencies.
- • The spatial branch emphasizes inter-channel interactions, adaptively weighted by channel attention.

Formally, a batch of input EEG trials is denoted as X ∈ RB×C×T, where B is the number of trials, C the number of channels, and T the number of time samples. DBConformer processes X through two parallel mappings:

Ft = fT-Conformer(X) ∈ RB×D, (3) Fs = fS-Conformer(X) ∈ RB×D, (4)

Ffused = [Ft;Fs] ∈ RB×2D, (5)

where D is the embedding dimension, fT-Conformer(·) captures temporal dependencies, and fS-Conformer(·) captures spatial relations.

This parallel design ensures that temporal and spatial features are learned independently before integration, yielding more disentangled and complementary representations. Unlike prior serial hybrids, this design is further supported by neuroscientiﬁc evidence. For example, neurophysiological studies demonstrated that absolute duration and distance are independently coded by distinct populations of prefrontal neurons [39], whereas behavioral studies showed that tem-

The detailed architecture of DBConformer is summarized in Table II, outlining the composition of each module. As shown in Fig. 2 and Table II, DBConformer is composed of T-Conformer and S-Conformer branches, along with a classiﬁcation module. A channel attention module is integrated in S-Conformer for channel-aware weighting.

TABLE II DBCONFORMER ARCHITECTURE.

[Figure 126]

[Figure 127]

[Figure 128]

Branch Module Layer # Kernels Kernel Size # Parameters Output Shape Options

[Figure 129]

[Figure 130]

[Figure 131]

Separable Conv1D F (1, ) C · F (B, F,T) Spatial ﬁltering BatchNorm1D – – 2F (B, F,T) Normalization Temporal Temporal Conv1D F (K, ) F · K (B, F,T) Temporal depthwise Conv.

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

Patch BatchNorm1D & GELU – – 2F (B, F,T) Normalization and non-linearity

[Figure 138]

[Figure 139]

Embedding Dropout – – 0 (B, F,T) p = 0.5 AvgPool1D – (1, W) 0 (B, F,P) Patch-wise downsampling Permute – – 0 (B, P, F) Patch tokens along time axis Positional Encoding – – P · D (B, P, D) Learnable temporal encoding

[Figure 140]

[Figure 141]

T-Conformer

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

T-Transformer Transformer Encoder – – ∼ (B, P, D) Lt layers, Ht heads Mean Pooling – – 0 (B, D) Mean over patches

[Figure 149]

[Figure 150]

[Figure 151]

- S-Conformer

[Figure 152]

[Figure 153]

Channel-wise Conv1D 16 25 – (B · C, 16, T′) Per-channel temporal ﬁltering Spatial AvgPool1D – – 0 (B · C, 16, 1) Channel-wise downsampling

[Figure 154]

[Figure 155]

[Figure 156]

Patch Flatten – – 0 (B · C, 16) Reshape Embedding Reshape – – 0 (B, C, 16) Channel-token preparation

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

Linear 16 – 16D (B, C, D) Project to embedding space S-Transformer

[Figure 162]

[Figure 163]

[Figure 164]

Positional Encoding – – C · D (B, C, D) Learnable spatial encoding Transformer Encoder – – ∼ (B, C, D) Ls layers, Hs heads

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

Linear – – D · D (B, C, D) Intermediate token projection Tanh – – 0 (B, C, D) Non-linearity

[Figure 170]

[Figure 171]

[Figure 172]

Channel Linear – – D (B, C, 1) Channel-level scoring Attention Softmax – – 0 (B, C, 1) Normalize across channels

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

Weighted Summation – – 0 (B, D) Weighted channel-aware feature /

[Figure 178]

[Figure 179]

Fusion Concatenation – – 0 (B, 2D) Feature fusion Classiﬁer FC Layers – – 2D → 64 → 32 → Nc (B, Nc) 3-layer MLP (ELU, Dropout)

[Figure 180]

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

B: batch size, C: number of channels, T: number of time points, T′: temporal length after Conv1D, F: number of ﬁlters, K: temporal kernel size, W: pooling window size, P = T/W: number of temporal patches, D: embedding dimension, Lt: number of T-Transformer encoder layers, Ls: number of

S-Transformer encoder layers, Ht: number of T-Transformer encoder heads, Hs: number of S-Transformer encoder heads, Nc: number of classes.

poral and spatial attention recruit separable neural systems [40]. Such ﬁndings suggest that temporal rhythms and spatial topographies are processed by distinct but interacting cortical mechanisms, providing both physiological plausibility and theoretical grounding for our dual-branch architecture.

2) T-Conformer: The temporal branch of DBConformer, termed T-Conformer, is designed to capture ﬁne-grained temporal dependencies in EEG trials. It comprises two primary components: a convolutional patch embedding module and a

- T-Transformer encoder.

- a) Temporal Patch Embedding: Inspired by prior CNN backbones in EEG decoding [15], we design the module with a depthwise separable 1D convolution, a 1D temporal convolution, and an average pooling layer. The ﬁrst separable convolution has F kernels with a stride of (1,), followed with batch normalization. The second temporal convolution applies F ﬁlters, accompanied by batch normalization, a GELU activation, and a dropout with a probability p = 0.5. Then, an average pooling with kernel size (1,W) is applied along the time dimension to form non-overlapping temporal patches Zt. Finally, the patches are reshaped via transposition. The number of ﬁlters F is set equal to the Transformer embedding dimension D, thereby eliminating the need for a separate linear projection.
- b) Temporal Transformer Encoder: The extracted patches Zt pass through a Transformer encoder [50] to model temporal dependencies. We add a learnable positional encod-

ing Epost ∈ R1×P×D to preserve temporal ordering:

Zint = Zt + Epost . (6) A lightweight Transformer encoder with Lt layers and Ht

attention heads is then applied: Zoutt = TransformerEncoder(Zint ) ∈ RB×P×D. (7)

To aggregate temporal patch features into a global representation, we employ mean pooling over the patch dimension:

P

1 P

Zoutt [:,i,:] ∈ RB×D, (8) which is the ﬁnal temporal representations of input EEG trials.

Ft =

[Figure 185]

i=1

3) S-Conformer: The spatial branch of DBConformer, termed S-Conformer, is designed to extract inter-channel spatial patterns. It consists of three components: a convolutional spatial patch embedding, an S-Transformer encoder, and a channel attention module.

a) Spatial Patch Embedding: This module transforms each EEG trial into a spatial token embedding. A depthwise 1D convolution across the time dimension is designed to extract short-range temporal features per channel. Next, average pooling is applied over the temporal dimension to summarize each channel’s temporal response, yielding a compressed representation. Then, patches are ﬂattened and reshaped to restore batch and channel dimensions. Finally, a linear projection layer is applied to map each channel token to the desired embedding dimension D.

b) Spatial Transformer Encoder: To capture global spatial dependencies across EEG channels, the embedded channel tokens Zs are processed by a lightweight Transformer encoder. A learnable positional encoding Eposs ∈ R1×C×D is added to retain channel ordering:

4) Feature Fusion and Classiﬁcation: After obtaining the representations from the temporal and spatial branches, i.e., Ft ∈ RB×D from T-Conformer and Fs ∈ RB×D from SConformer, the two features are concatenated along the feature dimension to form the fused representation:

Ffused = [Ft;Fs] ∈ RB×2D, (14) which is then passed through a multi-layer perceptron classiﬁer to generate the ﬁnal predictions yˆ = softmax MLP(Ffused) . The classiﬁer consists of three fully connected layers with intermediate ELU activations and dropout regularization.

Zins = Zs + Eposs . (9)

Then, a Transformer encoder with Ls layers and Hs heads is applied:

Zouts = TransformerEncoder(Zins ) ∈ RB×C×D. (10) c) Channel Attention: A lightweight channel attention

Given the prediction yˆi and the ground-truth label yi, the classiﬁcation loss is:

module are proposed to adaptively reﬁning the spatial saliency of features from S-Conformer, illustrated in Fig. 3.

B

1 B

CE(ˆyi,yi), (15)

LCLS =

[Figure 186]

i=1

where CE(·,·) denotes the cross-entropy loss function and B is the batch size.

IV. EXPERIMENTS AND RESULTS

This section details the datasets, experiments, and analyses. We implemented and fairly evaluated thirteen state-of-the-art EEG decoding models, including CNN-based models, CNNTransformer hybrids, and CNN-Mamba hybrids. Code for DBConformer, along with all compared baseline models, is available on GitHub1, serving as a benchmark codebase for EEG decoding.

A. Datasets

We conducted experiments on two EEG decoding tasks: MI classiﬁcation and epileptic seizure detection. Characteristics of all datasets are summarized in Table III.

1) MI Datasets: We adopted six publicly available MI datasets from the MOABB benchmark [51] and BCI competitions:

- Fig. 3. The proposed channel attention module.

- • BNCI2014001 [52]: Contains EEG trials from 9 subjects performing left/right hand MI, recorded with 22 EEG channels at 250 Hz. The ﬁrst session was used in the experiments.
- • BNCI2014004 [53]: Contains EEG trials from 9 subjects performing left/right hand MI, recorded with only 3 EEG channels at 250 Hz. The ﬁrst session was used in the experiments.
- • Zhou2016 [54]: Contains EEG trials from 4 subjects performing left/right hand MI, recorded with 14 channels at 250 Hz. The ﬁrst session was used in the experiments.
- • Blankertz2007 [55]: Contains EEG trials from 7 subjects with 59 channels EEG sampled at 250 Hz from BCI Competition IV dataset 1. Subjects 1 and 5 performed left hand/right foot MI, and the other ﬁve subjects performed left/right hand MI.
- • BNCI2014002 [56]: Contains EEG trials from 14 subjects, each performing eight runs right hand/feet MI, using 15 EEG channels recorded at 512 Hz. The ﬁrst ﬁve training runs were used in the experiments.

Speciﬁcally, each token {zic}Cc=1 of Zouts is projected through two fully connected layers:

kic = w2⊤ tanh(W1zic), (11)

where W1 ∈ RD×D and w2 ∈ RD are learnable parameters, and tanh(·) is the non-linear activation function. The attention weights are then obtained via Softmax normalization:

exp(kic)

αci =

, c = 1,...,C. (12)

[Figure 190]

C j=1 exp(kij)

Then, for each sample, the c-th channel token zci is aggregated through an attention-weighted sum:

C

αci · zci. (13)

fs,i =

c=1

This operation is executed independently for each sample, yielding its spatial representation fs,i ∈ RD. By repeating this computation across all B samples in a batch, the batch-level spatial representation Fs ∈ RB×D can be obtained.

1https://github.com/wzwvv/DBConformer

TABLE III SUMMARY OF THE SIX MI DATASETS, TWO SEIZURE DATASETS, AND ONE SSVEP DATASET.

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

Number of Number of Sampling Trial Length Number of

Paradigm Dataset

Task Types Subjects EEG Channels Rate (Hz) (seconds) Total Trials

[Figure 199]

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

- BNCI2014001 9 22 250 4 1,296 left/right hand BNCI2014004 9 3 250 5 1,080 left/right hand

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

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

Zhou2016 4 14 250 5 409 left/right hand Blankertz2007 7 59 250 3 1,400 left/right hand or left hand/right foot

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

- BNCI2014002 14 15 512 5 1,400 right hand/both feet OpenBMI 54 62 1000 4 10,800 left/right hand

MI

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

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

CHSZ 27 19 500 or 1,000 4 21,237 normal/seizure NICU 39 19 256 4 52,534 normal/seizure

Seizure detection

[Figure 257]

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

SSVEP Nakanishi2015 10 8 256 1 1,800 12 different stimuli

[Figure 272]

• OpenBMI [57]: Contains EEG trials from 54 subjects, each performing two sessions of left/right hand MI, using 62 channels recorded at 1,000 Hz. The total number of trials is 10,800.

- 2) Seizure Detection Datasets: Two clinical seizure detec-

tion datasets are evaluated:

- • CHSZ [58]: Contains EEG recordings from 27 pediatric patients aged 3 months to 10 years, recorded with 19 unipolar electrodes at a sampling rate of 500 or 1000 Hz. All recordings were manually annotated by neurologists to mark the onset and termination of seizures.
- • NICU [59]: A large-scale neonatal EEG dataset collected from 79 full-term neonates in the Helsinki University Hospital neonatal intensive care unit. Data were recorded at 256 Hz, with the same electrodes as CHSZ. Seizures were independently annotated by three clinical experts with a 1s window. A consensus set comprising 39 neonates with conﬁrmed seizures was utilized in the experiments.

- 3) SSVEP Dataset: The Nakanishi2015 [60] SSVEP

dataset is evaluated. Data were recorded at 256 Hz from 10 subjects, with eight channels PO7, PO3, POZ, PO4, PO8, O1, Oz and O2 in the occipital area. For each subject, 12-class stimuli were recorded with 15 blocks.

- 4) Data Preprocessing: For the MI paradigm, the standard

preprocessing steps in MOABB, including notch ﬁltering, band-pass ﬁltering, etc., were performed to ensure reproducibility on BNCI2014001, BNCI2014004, Zhou2016, and BNCI2014002 datasets. For the Blankertz2007 dataset, EEG trials were ﬁrst band-pass ﬁltered between 8 and 30 Hz. Then, trials between [0.5, 3.5] seconds after the cue onset were segmented and downsampled to 250 Hz. For the OpenBMI dataset, the raw EEG signals were ﬁrst ﬁltered by a third-order Butterworth band-pass ﬁlter with a passband of [4, 40] Hz to remove low-frequency drifts and high-frequency noise, and then downsampled to 256 Hz. Following previous studies such as FBCNet [14] and FBMSNet [21], 20 motor-related channels {FC5, FC3, FC1, FC2, FC4, FC6, C5, C3, C1, Cz, C2, C4, C6, CP5, CP3, CP1, CPz, CP2, CP4, CP6} were selected for analysis, which cover the sensorimotor cortex regions typically associated with MI tasks. EA was utilized after pre-processing on all MI datasets, and the EA reference matrix was updated online when new test trials arrived on-the-ﬂy, as in [61].

For seizure datasets, 18 bipolar channels were ﬁrst generated from 19 unipolar channels, following [59]. EEG recordings were segmented into 4s non-overlapping trials. Then, trials from both datasets were preprocessed by a 50 Hz notch ﬁlter and a 0.5-50 Hz bandpass ﬁlter. For CHSZ, 1000 Hz trials were downsampled to 500 Hz for consistency. For NICU, the ground-truth label of each trial was determined by the majority vote of three experts.

For the SSVEP paradigm, EEG trials were ﬁrst downsampled to 256 Hz and [6, 80] Hz band-pass ﬁltered, and then split into 1-second length trials in Nakanishi2015, following the preprocessing steps in [62].

B. Compared Approaches

Thirteen EEG decoding models were compared with the proposed DBConformer in the experiments:

- • EEGNet [8] is a compact CNN tailored for EEG classiﬁcation. It includes two key convolutional blocks: a temporal convolution for capturing frequency-speciﬁc features, followed by a depthwise spatial convolution. A separable convolution and subsequent pointwise convolution are designed to enhance spatio-temporal representations.
- • SCNN [9] is a shallow CNN inspired by the ﬁlter bank common spatial pattern, utilizing temporal and spatial convolutions in two stages to efﬁciently extract discriminative EEG features.
- • DCNN [9] is a deeper version of SCNN with larger parameters, consisting of four convolutional blocks with max pooling layers.
- • FBCNet [14] incorporates spatial convolution and a temporal variance layer to extract spectral-spatial features across multiple EEG frequency bands.
- • ADFCNN [16] is a dual-branch CNN model employing multi-scale temporal convolutions for frequency domain analysis and separable spatial convolutions for global spatial feature extraction. Features from both branches are fused using attention-based fusion before being fed into a fully connected classiﬁcation head.
- • CTNet [11] combines a convolutional front-end, similar to EEGNet, with a Transformer encoder for capturing long-range dependencies in EEG data. This serial structure enhances both local and global feature learning.

- • EEG Conformer [10] integrates a convolutional block, a Transformer encoder block, and a classiﬁer. The convolutional block is equipped with temporal and spatial convolutional layers, followed by an average pooling layer. CNN, Transformer, and the classiﬁer are serially equipped, similar to CTNet.
- • MSCFormer [34] integrates multi-branch, multi-scale CNN modules with Transformer encoders to jointly model local and global EEG representations.
- • TMSA-Net [35] also integrates multi-scale CNNs with the local and global attention modules to enhance the feature extraction.
- • MSVTNet [36] extracts local spatio-temporal features at different ﬁltered scales and introduces an auxiliary branch loss to facilitate effective CNN-Transformer integration.
- • SlimSeiz [30] integrates multiple 1D CNN layers to extract features at various temporal resolutions and a Mamba block to capture long-range temporal dependencies for seizure prediction. SlimSeiz enhances temporal modeling by integrating the Mamba block while avoiding a signiﬁcant parameter overhead.
- • IFNet [15] extends the spectral-spatial approach by decomposing EEG into multiple frequency bands (e.g., 4-16 Hz, 16-40 Hz). For each band, it applies 1D spatial and temporal convolutions, followed by feature concatenation and a fully connected layer for classiﬁcation.
- • EEGWaveNet [26] introduces a multi-scale temporal CNN architecture with depthwise ﬁlters that are channelspeciﬁc, extracting multi-scale features from trials of each EEG channel.

C. Implementation

1) Evaluation Scenarios: To evaluate the performance under different conditions, we performed four experimental settings: chronological order (CO), cross-validation (CV), leaveone-subject-out (LOSO), and cross-dataset (CD), covering within-subject, cross-subject, and cross-device settings, as in [17], [63].

- • CO: Trials from each subject were split according to recording time. The ﬁrst 80% trials were used for training, and the remaining 20% for testing. This scenario reﬂects a within-subject evaluation protocol that mimics real-time deployment.
- • CV: A 5-fold cross-validation was adopted, where the dataset was divided chronologically into ﬁve equal parts with balanced classes. In each iteration, four folds were used for training and one for testing. This also constitutes a within-subject setting, following the protocol in [14].
- • LOSO: EEG trials from a single subject were held out as the test set, while data from all remaining subjects were joint for training. This setting evaluates the model’s cross-subject decoding ability.
- • CD: Cross-dataset validation, where training and testing were performed on distinct EEG datasets, e.g., training on BNCI2014001 and testing on BNCI2014004. The CD results are shown in Table S1 of the supplementary material.

- 2) Evaluation Metrics: Accuracy is employed to evaluate the performance on MI and SSVEP. To evaluate the classiﬁcation performance on class-imbalanced seizure datasets, three additional metrics, area under the receiver operating characteristic curve (AUC), weighted F1 score and balanced classiﬁcation accuracy (BCA), are included in seizure detection.
- 3) Parameter Settings: All experiments were repeated ﬁve times with a random seed list [1,2,3,4,5], and the average results were reported. For all MI datasets, models were trained for 100 epochs using the Adam optimizer with a learning rate 10−3 and a batch size of 32. For seizure datasets, models are trained for 200 epochs using the Adam optimizer with a learning rate 10−3. The batch size was set to 256 for CHSZ and 512 for NICU because of the larger data size. For all baseline models, the model hyperparameters (e.g., kernel sizes, number of convolutional and Transformer layers) were set according to the original papers to ensure a fair comparison and reproducibility. Due to the speciﬁc characteristics of datasets, scenarios, and tasks, we adopted distinct model conﬁgurations accordingly, as summarized in Table S6 of the supplementary Material.

D. Results on MI Classiﬁcation

Table IV presents the average classiﬁcation accuracies of DBConformer and nine baseline models across six MI datasets under three evaluation settings. Observe that:

- • Among the nine baseline models, IFNet achieved the highest average accuracy across all three settings, attributed to its frequency-aware architectural design. EEG Conformer ranked second under the CO and CV settings but exhibits reduced performance in the LOSO scenario, indicating that its large parameter size may cause overﬁtting when generalizing to unseen subjects.
- • Compared to the CO setting, results under CV were generally higher across all models, consistent with ﬁndings in [17], where temporally ordered training limits generalization due to potential signal drift or session variance. CV scenario beneﬁted from more diverse training trials within each subject. This highlights the importance of fair and appropriate partitioning when benchmarking EEG decoding models.
- • In the LOSO setting, DBConformer maintained the best generalization across subjects. This highlights the robustness of DBConformer in cross-subject EEG decoding tasks.
- • DBConformer almost always outperformed all 12 baseline models across all datasets and settings, demonstrating the effectiveness of the dual-branch design in capturing both temporal and spatial characteristics.

Further, we conducted paired t-tests for each comparison and applied Benjamini-Hochberg False Discovery Rate correction to control for multiple comparisons [64]. The adjusted p-values are summarized in Table V, where values below 0.05 are highlighted in bold to indicate statistical signiﬁcance. It is evident that the performance improvements of DBConformer over other competing models were almost always statistically signiﬁcant.

TABLE IV AVERAGE CLASSIFICATION ACCURACIES (%) OF DBCONFORMER AND TWELVE BASELINE MODELS ON SIX MI DATASETS UNDER CO, CV, AND LOSO SCENARIOS. THE BEST AVERAGE PERFORMANCE OF EACH DATASET IS MARKED IN BOLD, AND THE SECOND BEST BY AN UNDERLINE.

[Figure 273]

[Figure 274]

[Figure 275]

Task Dataset EEGNet SCNN DCNN FBCNet ADFCNN CTNet EEG Confor. MSCFor. TMSA-NetMSVTNet SlimSeiz IFNet DBConfor.

[Figure 276]

[Figure 277]

[Figure 278]

2014001 69.05±1.0 73.57±2.4 59.29±1.6 68.97±1.3 73.73±2.3 73.49±2.1 78.57±0.7 75.00±1.2 76.67±2.1 74.60±3.0 68.89±2.1 77.94±0.9 80.16±1.8 2014004 68.43±2.2 68.15±1.4 62.41±1.6 65.46±1.6 69.63±1.2 71.57±1.3 72.04±1.6 72.20±1.8 70.28±2.0 71.30±1.5 68.24±2.7 73.43±1.7 75.09±1.5

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

[Figure 284]

Zhou201680.13±3.4 75.03±6.2 78.03±2.4 63.33±2.3 71.42±2.0 76.81±5.1 73.87±4.5 73.93±4.5 67.94±3.0 70.32±1.4 72.01±4.0 81.70±2.1 82.49±2.4 Blankertz 78.79±2.8 76.71±2.1 70.00±4.1 75.93±1.3 76.07±1.4 79.00±3.4 82.29±2.6 85.29±1.6 78.93±1.0 84.29±0.9 65.64±1.2 84.00±0.6 87.21±1.3 2014002 66.07±2.8 79.07±2.0 64.07±2.7 69.50±1.0 73.00±2.0 71.00±1.8 76.21±1.5 75.79±1.9 76.79±1.9 78.93±1.4 78.71±0.5 78.29±1.7 79.14±0.2

[Figure 285]

[Figure 286]

[Figure 287]

CO

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

OpenBMI 65.54±0.7 71.78±0.3 66.84±1.1 61.31±0.6 71.82±0.8 68.58±0.7 71.84±0.8 70.64±0.6 71.10±0.6 70.06±0.7 61.15±0.4 68.19±0.6 72.12±0.1 Average 71.33 74.05 66.77 67.42 72.61 73.41 75.80 75.47 73.62 74.91 69.11 77.26 79.37

[Figure 294]

[Figure 295]

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

2014001 71.86±1.0 78.22±0.2 61.59±1.1 74.74±0.7 77.27±0.6 75.97±0.8 83.62±1.0 81.83±0.7 82.32±0.5 81.28±0.7 75.56±1.5 82.62±0.9 83.66±0.4 2014004 68.91±0.9 68.13±0.6 63.51±0.4 67.17±0.3 69.48±1.2 70.96±1.1 73.15±0.7 72.30±0.4 72.11±0.9 73.59±0.6 69.74±0.5 72.02±0.5 74.17±0.6

[Figure 302]

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

Zhou201685.30±2.1 82.90±0.9 79.68±1.1 80.01±0.5 84.95±1.5 86.38±1.5 85.67±1.5 89.16±0.8 85.54±1.3 88.06±1.2 85.60±1.3 87.78±1.0 91.54±0.2 Blankertz 80.21±0.8 81.11±0.7 69.83±1.5 84.14±0.6 81.10±1.8 83.64±1.0 87.43±0.3 88.41±0.9 74.09±0.6 89.07±0.8 75.37±1.1 88.23±0.5 90.33±0.5 2014002 68.90±1.4 81.24±0.5 67.17±0.3 74.53±0.7 74.63±0.8 75.50±0.9 79.30±0.3 80.29±0.7 80.41±0.6 80.91±0.5 77.93±0.9 80.21±0.5 81.36±0.3

[Figure 308]

[Figure 309]

[Figure 310]

CV

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

[Figure 316]

OpenBMI 65.99±0.4 71.99±0.3 67.68±0.4 63.82±0.2 72.21±0.5 69.50±0.4 72.34±0.3 71.34±0.2 72.07±0.2 71.20±0.2 61.23±0.5 71.75±0.2 72.89±0.2 Average 73.53 77.27 68.24 74.07 76.61 76.99 80.25 80.55 77.76 80.69 74.24 80.44 82.32

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

[Figure 322]

[Figure 323]

[Figure 324]

2014001 73.64±1.1 72.22±1.0 73.21±1.8 72.56±1.0 71.76±0.8 73.40±1.2 73.07±2.0 76.02±0.8 77.32±0.5 77.10±1.3 69.62±1.3 74.52±0.7 77.67±0.6 2014004 67.78±0.9 62.19±0.8 62.56±0.6 67.09±0.7 65.17±0.7 65.28±1.1 64.22±1.1 64.72±0.6 66.02±0.8 67.41±0.8 63.15±1.4 67.69±0.4 69.85±0.5

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

Zhou201683.22±1.8 82.10±0.7 83.84±1.2 82.07±0.9 82.09±1.3 83.88±1.0 82.43±1.5 85.31±2.4 80.78±2.3 84.95±1.4 84.06±1.6 86.21±1.0 85.37±0.9 Blankertz 71.10±0.8 70.64±0.6 72.19±0.9 76.23±1.4 70.59±1.7 69.50±1.8 74.41±1.1 73.66±0.9 72.72±0.9 75.40±1.3 73.21±0.8 73.43±1.1 76.33±0.7 2014002 72.86±0.4 70.57±1.4 74.34±0.8 71.31±0.8 72.67±0.4 74.14±0.8 72.84±1.4 74.09±0.6 73.99±1.1 74.61±1.1 73.01±0.6 73.90±0.7 77.17±0.8

[Figure 331]

[Figure 332]

[Figure 333]

LOSO

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

[Figure 339]

OpenBMI 73.33±0.1 68.98±0.4 73.27±0.2 60.34±0.6 73.18±0.4 70.05±0.1 70.05±0.1 73.25±0.8 72.79±0.7 72.77±0.3 68.89±0.7 70.03±0.5 73.61±0.2 Average 73.65 71.12 73.23 71.60 72.58 72.71 72.84 74.51 73.94 75.37 71.99 74.30 76.67

[Figure 340]

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

[Figure 345]

TABLE V ADJUST p-VALUES BETWEEN DBCONFORMER AND TWELVE BASELINE MODELS UNDER CO, CV, AND LOSO SETTINGS. STATISTICALLY SIGNIFICANT RESULTS (p < 0.05) ARE MARKED IN BOLD.

[Figure 346]

[Figure 347]

[Figure 348]

Task DBConformer vs. BNCI2014001 BNCI2014004 Zhou2016 Blankerz2007 BNCI2014002 OpenBMI

[Figure 349]

EEGNet < 0.001 < 0.01 0.212 < 0.05 < 0.001 < 0.001 SCNN < 0.01 < 0.01 < 0.05 < 0.001 0.183 0.104 DCNN < 0.001 < 0.001 0.198 < 0.001 < 0.001 < 0.01 FBCNet < 0.001 < 0.01 < 0.001 < 0.001 < 0.001 < 0.001 ADFCNet < 0.001 < 0.01 < 0.01 < 0.01 < 0.01 0.081

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

CTNet < 0.01 0.052 0.054 < 0.001 < 0.01 < 0.01 EEG Conformer 0.052 < 0.01 < 0.01 < 0.01 < 0.05 < 0.051

[Figure 360]

[Figure 361]

CO

[Figure 362]

[Figure 363]

MSCFormer < 0.001 0.051 < 0.05 0.13 < 0.001 < 0.05 TMSA-Net < 0.01 < 0.01 < 0.01 < 0.01 < 0.01 0.09 MSVTNet < 0.05 < 0.01 < 0.01 0.073 0.136 < 0.01

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

[Figure 368]

[Figure 369]

SlimSeiz < 0.001 < 0.05 < 0.05 < 0.001 0.116 < 0.001 IFNet < 0.05 < 0.05 0.158 < 0.05 0.128 < 0.001

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

EEGNet < 0.001 < 0.001 < 0.01 < 0.001 < 0.001 < 0.001 SCNN < 0.001 < 0.001 < 0.001 < 0.001 0.16 0.053 DCNN < 0.001 < 0.001 < 0.001 < 0.001 < 0.001 < 0.001

[Figure 375]

[Figure 376]

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

FBCNet < 0.001 < 0.001 < 0.001 < 0.001 < 0.001 < 0.001 ADFCNet < 0.001 < 0.01 < 0.001 < 0.001 < 0.001 0.132

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

CTNet < 0.001 < 0.01 < 0.001 < 0.01 < 0.001 < 0.001 EEG Conformer 0.08 < 0.01 < 0.001 < 0.01 0.099 < 0.05

[Figure 385]

[Figure 386]

CV

[Figure 387]

[Figure 388]

MSCFormer < 0.01 < 0.05 < 0.01 0.089 0.063 < 0.05 TMSA-Net < 0.01 < 0.01 < 0.01 < 0.001 0.075 0.055 MSVTNet < 0.05 0.158 < 0.01 0.094 0.051 < 0.01

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

SlimSeiz < 0.001 < 0.01 < 0.01 < 0.001 < 0.01 < 0.001 IFNet < 0.05 < 0.01 < 0.001 < 0.05 0.064 < 0.01

[Figure 395]

[Figure 396]

[Figure 397]

[Figure 398]

[Figure 399]

EEGNet < 0.001 < 0.05 0.082 < 0.001 < 0.001 < 0.05 SCNN < 0.001 < 0.001 < 0.01 < 0.001 < 0.001 < 0.001 DCNN < 0.001 < 0.001 0.094 < 0.001 < 0.01 < 0.05 FBCNet < 0.001 < 0.001 < 0.001 0.172 < 0.001 < 0.001 ADFCNet < 0.001 < 0.001 < 0.01 < 0.001 < 0.001 0.055

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

CTNet < 0.001 < 0.001 0.082 < 0.001 < 0.01 < 0.001 EEG Conformer < 0.001 < 0.001 < 0.05 < 0.05 < 0.01 < 0.001

[Figure 410]

[Figure 411]

LOSO

[Figure 412]

[Figure 413]

MSCFormer < 0.001 < 0.001 0.172 < 0.01 < 0.01 < 0.05 TMSA-Net 0.059 < 0.001 < 0.05 < 0.001 < 0.05 0.161 MSVTNet 0.14 < 0.001 0.182 0.076 0.054 < 0.05

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

SlimSeiz < 0.001 < 0.001 < 0.05 < 0.01 < 0.001 < 0.001 IFNet < 0.001 < 0.001 < 0.05 < 0.001 < 0.05 < 0.001

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

- E. Results on Seizure Detection

For seizure detection, we compared the proposed DBConformer with seven baseline models: EEGNet, SCNN, DCNN, ADFCNN, EEG Conformer, SlimSeiz, and EEGWaveNet. The ﬁrst ﬁve models were originally designed for tasks such as MI and emotion recognition, rather than seizure detection. But they are general for all EEG decoding tasks; thus, we reimplemented and adapted them to seizure detection. SlimSeiz [30] is a CNN-Mamba hybrid model for seizure prediction that can be easily implemented in the seizure detection task. EEGWaveNet [26] is a multi-scale depthwise CNN speciﬁcally developed for seizure detection, serving as a competitive taskspeciﬁc benchmark. Table VI summarizes the average AUCs, F1 scores, and BCAs of DBConformer and seven baseline models on the CHSZ and NICU datasets. Observe that:

- • Among the baseline approaches, EEG Conformer and ADFCNN achieved competitive performance across most metrics. EEG Conformer beneﬁts from its temporal modeling capacity, while ADFCNN leverages dual-scale convolutions to capture frequency-sensitive patterns.
- • Compared to CHSZ, all models generally exhibited lower performance on the NICU dataset. This degradation can be attributed to differences in recording conditions, subject age, and seizure morphology. The smaller brain volume of neonates introduces greater variability and reduces the signal-to-noise ratio in NICU, underscoring the need for robust generalization across patients.
- • DBConformer achieved the best performance across all evaluation metrics and both datasets. Compared to strong baselines such as EEG Conformer and ADFCNN, DBConformer yielded a 2-4% improvement in BCAs. Results demonstrate the adaptability of DBConformer to clinical EEG decoding tasks. The dual-branch spatiotemporal modeling design provides robust representations for varying patients, making it more reliable for realworld seizure detection.

TABLE VI AVERAGE CLASSIFICATION AUCS (%), F1S (%), AND BCAS (%) ON CHSZ AND NICU DATASETS UNDER THE LOSO SETTING. THE BEST AVERAGE PERFORMANCE IS MARKED IN BOLD, AND THE SECOND-BEST BY AN UNDERLINE.

[Figure 425]

Model

[Figure 426]

CHSZ NICU AUC F1 BCA AUC F1 BCA

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

[Figure 431]

EEGNet 84.36 87.54 74.93 71.87 71.03 64.79 SCNN 49.17 70.18 50.15 68.86 76.54 63.52 DCNN 52.88 67.84 50.41 66.65 72.28 60.93

[Figure 432]

[Figure 433]

[Figure 434]

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

ADFCNet 86.49 90.22 76.92 70.48 69.45 62.60 EEG Conformer 89.23 88.01 74.33 71.46 77.43 64.04

[Figure 440]

[Figure 441]

[Figure 442]

[Figure 443]

[Figure 444]

[Figure 445]

[Figure 446]

[Figure 447]

SlimSeiz 86.94 87.56 76.30 71.78 70.01 64.25 EEGWaveNet 87.38 87.71 75.56 68.68 59.00 58.14 DBConformer 91.75 90.31 79.01 72.08 79.23 65.21

[Figure 448]

[Figure 449]

[Figure 450]

[Figure 451]

[Figure 452]

[Figure 453]

[Figure 454]

- F. Results on SSVEP Classiﬁcation

To further evaluate the generalizability of DBConformer, we conducted experiments on the Nakanishi2015 SSVEP dataset. As shown in Table VII, DBConformer consistently

outperformed recent CNN and CNN-Transformer baselines, including Conformer, MSCFormer, TMSA-Net, and IFNet. In particular, DBConformer achieved the highest average accuracy of 87.59%, surpassing the second-best IFNet by a substantial margin, highlighting its adaptability across diverse EEG paradigms.

TABLE VII AVERAGE CLASSIFICATION ACCURACIES (%) ON NAKANISHI2015 DATASET UNDER THE CO SETTING. THE BEST AVERAGE PERFORMANCE IS MARKED IN BOLD, AND THE SECOND-BEST BY AN UNDERLINE.

[Figure 455]

[Figure 456]

Subject Conformer MSCFormer TMSA-Net IFNet DBConformer

[Figure 457]

- S1 12.03 13.89 46.30 56.48 62.04

[Figure 458]

[Figure 459]

- S2 8.33 12.96 24.07 32.41 46.30

[Figure 460]

[Figure 461]

- S3 8.33 13.89 57.41 70.37 88.89

[Figure 462]

[Figure 463]

- S4 30.55 14.81 78.70 93.52 96.29

[Figure 464]

[Figure 465]

- S5 20.37 22.22 92.59 98.15 100.00

[Figure 466]

[Figure 467]

- S6 35.18 15.74 87.04 92.59 100.00

[Figure 468]

[Figure 469]

- S7 15.74 8.33 85.19 93.52 100.00

[Figure 470]

[Figure 471]

- S8 16.66 19.44 91.67 100.00 100.00

[Figure 472]

- S9 32.41 20.37 88.89 91.67 96.29

[Figure 473]

[Figure 474]

- S10 10.18 11.11 54.63 65.74 86.11

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

Average 18.98 15.28 70.65 79.44 87.59

[Figure 479]

[Figure 480]

- G. Ablation Study

To further validate the effectiveness of DBConformer’s key components, we conducted ablation studies on the parallel spatio-temporal design, positional encoding, and the channel attention module. Experiments were performed on six MI datasets under three settings, shown in Fig. 4. Observe that:

- • Parallel Spatio-Temporal Modeling. We compared the full DBConformer with its T-Conformer-only variant. Adding the S-Conformer branch consistently improved performance across all settings. Results conﬁrmed the effectiveness of incorporating spatial features via the auxiliary S-Conformer, which complemented the dominant temporal modeling of T-Conformer.
- • Positional Encoding. Disabling the learnable positional embeddings for both temporal and spatial tokens resulted in performance drops under all settings. This validated the importance of explicit temporal/channel ordering when modeling patch and channel tokens.
- • Channel Attention Module. Replacing the channel attention module with naı¨ve mean pooling degraded performance, conﬁrming that adaptively reweighting EEG channels beneﬁted enhancing spatial features.

- H. Effect of Dual-Branch Modeling

To further evaluate the impact of dual-branch architecture, we conducted feature visualization experiments using t-SNE [65]. Features extracted by T-Conformer (temporal branch only) and DBConformer (dual-branch) were compared on four MI datasets, shown in Fig. 5. Observe that:

• T-Conformer alone exhibited limited separability. Although T-Conformer captured meaningful temporal structures, its extracted features tended to form overlapping

#### BNCI2014001

BNCI2014004

Zhou2016

| | |
|---|---|
|CO CV<br><br>Blankertz2007|LOSO|
| | |
|CO CV<br><br>4. Abla encoding, and<br><br>cluster and<br><br>• DBCo separa coding the int across<br>• The of MI catego<br>|LOSO<br><br>tion studies the channel<br><br>s across Blankertz2007, nformer ted<br><br>from the er-class<br><br>all datasets. improvement<br><br>classiﬁcation spatio-temporal<br><br>ries (e.g.,|

| | |
|---|---|
| | |
|CO CV<br><br>BNCI2014002|LOSO<br><br>|
|CO CV<br><br>the paral attention mo<br><br>classes in d<br><br>which extracted<br><br>. With S-Confor margins and<br><br>was co<br><br>tasks modeling<br><br>hand vs.<br><br>robustn Spatio-Temporal<br><br>the self-at|LOSO<br><br>lel dule.<br><br>atasets limited more<br><br>the mer, promotes<br><br>nsistent<br><br>. The was hand/foot), ess of the<br><br>interpretability tention|

85

90

75

80

85

70

80

75

75

CO CV LOSO

85

90

w/o S-Conformer

85

80

w/o Pos. Encoding

w/o C annel Attention

80

75

DBConformer

75

Fig. on spatio-temporal design, positional enc l a

cla such as BNCI2014004 07, class discriminability. ex structured and well-

features integration of spatial en-

e DBConformer enhanced mar cluster compactness

ts.

nt across various types tion beneﬁt of dual-branch m observable regardless of

h ), demonstrating the generalization and proposed design.

- I. Visualization of Spa Self-Attention

To further examine y of DBConformer, Fig. 6 visualized the matrices learned in both temporal and spatial branches on BNCI2014001, BNCI2014002, and OpenBMI datasets. Observe that:

- • The temporal self-attention maps in Fig. 6(a) exhibited diagonal activations, which corresponded to the model’s focus on local neighboring time windows, as well as noticeable off-diagonal activations that captured longrange temporal dependencies. Across three datasets, DBConformer emphasized short-term EEG dynamics and integrated global temporal information, enabling a more comprehensive representation of MI.
- • The spatial self-attention maps in Fig. 6(b) revealed both diagonal activations corresponding to self-focus on individual channels, and distinct off-diagonal activations reﬂecting inter-channel interactions. In three datasets, channels over the sensorimotor cortex (e.g., C3, Cz, C4) exhibited the top attention intensities, indicating that DBConformer effectively captured physiologically meaningful intra-channel and inter-channel dependencies.
- • Furthermore, channel importance based on incoming offdiagonal attention weights is quantiﬁed in Fig. 6(c). Motor-related channels consistently dominated the importance ranking, conﬁrming that DBConformer robustly identiﬁes physiologically relevant channels.

- J. Model Complexity and Performance Analysis

Table VIII presents a comparative analysis of trainable parameter counts, training duration, and classiﬁcation accuracy

across DBConformer and nine baseline models. Observe that:

- • Compared to lightweight CNN models, DBConformer introduced additional complexity due to the dual branches. Nonetheless, the trade-off in model size and training time was well-compensated by superior performance.
- • DBConformer achieved the highest classiﬁcation accuracy, surpassing all competing baseline models. Despite incorporating a dual-branch Conformer design, it maintained a moderate number of parameters, with over 8× fewer than the high-capacity EEG Conformer.
- • IFNet and EEGNet achieved the shortest inference times among CNN-based models. Importantly, DBConformer achieved the fastest inference speed among CNNTransformer hybrids, requiring only 8.7 ms per batch, which meets the real-time requirements for online BCI applications.

K. Sensitivity Analysis on Architectural Design

We further conducted a sensitivity analysis to explore how architectural design affects the DBConformer performance.

- 1) Effect of Depth of T-Conformer and S-Conformer: We

varied the number of Transformer encoder layers in both T-Conformer and S-Conformer from 1 to 8, and evaluated the classiﬁcation accuracy on BNCI2014001 and Zhou2016 datasets. Results in Fig. 7(a) showed that performance does not monotonically increase with depth. Instead, both datasets achieve the best performance with two Transformer layers. When the depth exceeds 4 layers, accuracy tends to decrease slightly, suggesting that excessive stacking of attention layers may lead to overﬁtting on the limited training samples in MI datasets. In contrast, shallow conﬁgurations achieve a favorable trade-off between model complexity and generalization.

- 2) Effect of the Number of Attention Heads: Constrained

by the embedding size of D = 40, which requires the number of heads to be a divisor of 40, we evaluated the number of attention heads 1,2,4,5,8,10 on BNCI2014001 and Zhou2016 datasets. As shown in Fig. 7(b), the results remain relatively stable across different settings, with DBConformer consistently outperforming baseline models. Notably, 2 heads achieved the highest accuracy on both datasets. Increasing the number of heads beyond 4 did not yield further improvements and sometimes led to a slight decrease in performance, suggesting that excessive partitioning of the embedding dimension may dilute feature representations.

V. CONCLUSION

This paper proposed DBConformer, a dual-branch convolutional Transformer network tailored for EEG decoding. It integrates a T-Conformer to model long-range temporal dependencies and an S-Conformer to enhance inter-channel interactions, capturing both temporal dynamics and spatial patterns in EEG data. Comprehensive experiments conﬁrmed its effectiveness. In future work, DBConformer can be extended to support multi-view information fusion and plug-and-play real-time BCIs. Its superior performance and interpretability make it reliable for robust and explainable EEG decoding.

[Figure 481]

[Figure 482]

[Figure 483]

[Figure 484]

(a) (b)

[Figure 485]

[Figure 486]

[Figure 487]

[Figure 488]

(c) (d)

- Fig. 5. t-SNE visualizations of features extracted from T-Conformer and DBConformer on (a) BNCI2014001, (b) BNCI2014004, (c) Blankertz2007, and (d) Zhou2016 datasets. Different categories are encoded by colors.

[Figure 489]

[Figure 490]

[Figure 491]

- (a)

[Figure 492]

[Figure 493]

[Figure 494]

- (b)

[Figure 495]

[Figure 496]

[Figure 497]

- (c)

- Fig. 6. Visualizations of temporal and spatial self-attention across three MI datasets. (a) Temporal attention heatmap of time windows; (b) Spatial attention heatmap of EEG channels; (c) Channel importance of electrodes.

TABLE VIII COMPARISON OF MODEL COMPLEXITY AND PERFORMANCE METRICS ACROSS DBCONFORMER AND TWELVE BASELINE MODELS ON THE BNCI2014001 DATASET.

[Figure 498]

[Figure 499]

[Figure 500]

[Figure 501]

CNN CNN-Mamba CNN-Transformer EEGNet SCNN DCNN FBCNetADFCNN IFNet SlimSeiz CTNet EEG Confor. MSCFor.TMSA-NetMSVTNetDBConformer

Metric

[Figure 502]

[Figure 503]

[Figure 504]

[Figure 505]

[Figure 506]

[Figure 507]

[Figure 508]

[Figure 509]

# Model Parameters 1,406 46,084 320,479 7,042 4,322 7,748 27,650 27,284 789,668 150,626 17,869 72,892 92,066 Training Duration (s) 73.64 76.44 90.97 70.45 97.84 61.89 88.89 105.95 223.36 151.63 96.33 159.80 203.79 Inference Latency (s) 4.5e−3 1.3e−2 4.8e−3 1.3e−2 7.8e−3 4.2 e−3 1.7e−2 1.3e−2 1.9e−2 1.6e−2 8.8e−3 9.0e−3 8.7e−3

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

Accuracy (%) 73.64 72.22 73.21 72.56 71.76 74.52 69.62 73.40 73.07 75.00 76.67 74.60 77.67

[Figure 525]

[Figure 526]

[Figure 527]

86

86

BNCI2014001

BNCI2014001

84

84

Zho 2016

Zho 2016

82

82

80

80

78

78

Accracy(%)

Accracy(%)

76

76

74

74

72

72

1 2 3 4 5 6 7 8

1 2 3 4 5 6

Number of Transformer layers

Number of Transformer layers

(a)

(b)

- Fig. 7. Sensitivity analysis on architectural design: (a) Number of Transformer layers in T-Conformer and S-Conformer, (b) Number of attention heads in T-Conformer and S-Conformer. Each bar represents the mean accuracy across subjects, with error bars denoting the standard deviation.

REFERENCES

- [13] Z. Li, B. Chen, N. Zhu, W. Li, T. Liu, L. Guo, J. Han, T. Zhang, and Z. Yan, “Epileptic seizure detection in SEEG signals using a signal embedding temporal-spatial-spectral Transformer model,” IEEE Trans. on Instrumentation and Measurement, vol. 74, pp. 1–11, 2025.
- [14] R. Mane, E. Chew, K. Chua, K. K. Ang, N. Robinson, A. P. Vinod, S.-W. Lee, and C. Guan, “FBCNet: A multi-view convolutional neural network for brain-computer interface,” arXiv preprint arXiv:2104.01233, 2021.
- [15] J. Wang, L. Yao, and Y. Wang, “IFNet: An interactive frequency convolutional neural network for enhancing motor imagery decoding from EEG,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 1900–1911, 2023.
- [16] W. Tao, Z. Wang, C. M. Wong, Z. Jia, C. Li, X. Chen, C. P. Chen, and F. Wan, “ADFCNN: Attention-based dual-scale fusion convolutional neural network for motor imagery brain–computer interface,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 32, pp. 154–165, 2023.
- [17] Z. Wang, S. Li, X. Chen, W. Li, and D. Wu, “MVCNet: Multi-view contrastive network for motor imagery classiﬁcation,” Knowledge-Based Systems, vol. 328, p. 114205, 2025.
- [18] Z. Wang, S. Li, J. Luo, J. Liu, and D. Wu, “Channel reﬂection: Knowledge-driven data augmentation for EEG-based brain-computer interfaces,” Neural Networks, vol. 176, p. 106351, 2024.
- [19] Q. Dong, Z. Wang, and M. Gao, “Noise-aware epileptic seizure prediction network via self-attention feature alignment,” IEEE Journal of Biomedical and Health Informatics, pp. 1–13, 2025, early access.
- [20] Z. Wang, S. Li, X. Chen, and D. Wu, “Time-frequency transform based EEG data augmentation for brain-computer interfaces,” KnowledgeBased Systems, vol. 311, p. 113074, 2025.
- [21] K. Liu, M. Yang, Z. Yu, G. Wang, and W. Wu, “FBMSNet: A ﬁlter-bank multi-scale convolutional neural network for EEG-based motor imagery decoding,” IEEE Trans. on Biomedical Engineering, vol. 70, no. 2, pp. 436–445, 2022.
- [22] X. Jiang, L. Meng, X. Chen, Y. Xu, and D. Wu, “CSP-Net: Common spatial pattern empowered neural networks for EEG-based motor imagery classiﬁcation,” Knowledge-Based Systems, vol. 305, p. 112668, 2024.
- [23] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K.-r. Muller, “Optimizing spatial ﬁlters for robust EEG single-trial analysis,” IEEE Signal Processing Magazine, vol. 25, no. 1, pp. 41–56, 2008.
- [24] K. Fu, J. Qu, Y. Chai, and Y. Dong, “Classiﬁcation of seizure based on the time-frequency image of EEG signals using HHT and SVM,” Biomedical Signal Processing and Control, vol. 13, pp. 15–22, 2014.
- [25] M. Mursalin, Y. Zhang, Y. Chen, and N. V. Chawla, “Automated epileptic

- [1] J. V. Rosenfeld and Y. T. Wong, “Neurobionics and the brain-computer interface: current applications and future horizons,” Medical Journal of Australia, vol. 206, no. 8, pp. 363–368, 2017.
- [2] D. Wu, Y. Xu, and B.-L. Lu, “Transfer learning for EEG-based braincomputer interfaces: A review of progress made since 2016,” IEEE Trans. on Cognitive and Developmental Systems, vol. 14, no. 1, pp. 4–19, 2020.
- [3] G. Pfurtscheller and C. Neuper, “Motor imagery and direct braincomputer communication,” Proc. of the IEEE, vol. 89, no. 7, pp. 1123– 1134, 2001.
- [4] D. Wu, X. Jiang, and R. Peng, “Transfer learning for motor imagery based brain-computer interfaces: A tutorial,” Neural Networks, vol. 153, pp. 235–253, 2022.
- [5] U. R. Acharya, S. V. Sree, G. Swapna, R. J. Martis, and J. S. Suri, “Automated EEG analysis of epilepsy: A review,” Knowledge-Based Systems, vol. 45, pp. 147–165, 2013.
- [6] R. D. Thijs, R. Surges, T. J. O’Brien, and J. W. Sander, “Epilepsy in adults,” The Lancet, vol. 393, no. 10172, pp. 689–701, 2019.
- [7] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao, “High-speed spelling with a noninvasive brain–computer interface,” Proc. National Academy of Sciences, vol. 112, no. 44, pp. E6058–E6067, 2015.
- [8] V. J. Lawhern, N. R. Solon, Amelia J .and Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: A compact convolutional neural network for EEG-based brain-computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018.
- [9] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for EEG decoding and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [10] Y. Song, Q. Zheng, B. Liu, and X. Gao, “EEG Conformer: Convolutional Transformer for EEG decoding and visualization,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 710–719, 2022.
- [11] W. Zhao, X. Jiang, B. Zhang, S. Xiao, and S. Weng, “CTNet: A convolutional Transformer network for EEG-based motor imagery classiﬁcation,” Scientiﬁc Reports, vol. 14, no. 1, p. 20237, 2024.
- [12] Y. Ding, Y. Li, H. Sun, R. Liu, C. Tong, C. Liu, X. Zhou, and C. Guan, “EEG-Deformer: A dense convolutional Transformer for brain-computer interfaces,” IEEE Journal of Biomedical and Health Informatics, vol. 29, no. 3, pp. 1909–1918, 2024.

- seizure detection using improved correlation-based feature selection with random forest classiﬁer,” Neurocomputing, vol. 241, pp. 204–214, 2017.
- [26] P. Thuwajit, P. Rangpong, P. Sawangjai, P. Autthasan, R. Chaisaen, N. Banluesombatkul, P. Boonchit, N. Tatsaringkansakul, T. Sudhawiyangkul, and T. Wilaiprasitporn, “EEGWaveNet: Multiscale CNNbased spatiotemporal feature extraction for EEG seizure detection,” IEEE Trans. on Industrial Informatics, vol. 18, no. 8, pp. 5547–5557, 2022.
- [27] Y. Gui, M. Chen, Y. Su, G. Luo, and Y. Yang, “EEGMamba: Bidirectional state space model with mixture of experts for EEG multi-task classiﬁcation,” arXiv preprint arXiv:2407.20254, 2024.
- [28] M. Guo, X. Han, H. Liu, J. Zhu, J. Zhang, Y. Bai, and G. Ni, “MIMamba: A hybrid motor imagery electroencephalograph classiﬁcation model with Mamba’s global scanning,” Annals of the New York Academy of Sciences, vol. 1544, no. 1, pp. 242–253, 2025.
- [29] Q. Deng, Q. Wang, W. Liu, and Y. Xue, “EEG VMamba: Vision Mamba for seizure prediction based on EEG,” in Procs. of the Int’l Conf. on Video, Signal and Image Processing, Ningbo, China, Nov. 2024, pp. 119–124.
- [30] G. Lu, J. Peng, B. Huang, C. Gao, T. Stefanov, Y. Hao, and Q. Chen, “SlimSeiz: Efﬁcient channel-adaptive seizure prediction using a Mambaenhanced network,” arXiv preprint arXiv:2410.09998, 2024.
- [31] X. Zhou, Y. Han, Z. Chen, C. Liu, Y. Ding, Z. Jia, and Y. Liu, “BiTMamSleep: Bidirectional temporal Mamba for EEG sleep staging,” arXiv preprint arXiv:2411.01589, 2024.
- [32] S.-J. Kim, D.-H. Lee, H.-G. Kwak, and S.-W. Lee, “Toward domain-free Transformer for generalized EEG pre-training,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 32, pp. 482–492, 2024.
- [33] D. Zhang, H. Li, and J. Xie, “MI-CAT: A Transformer-based domain adaptation network for motor imagery classiﬁcation,” Neural Networks, vol. 165, pp. 451–462, 2023.
- [34] W. Zhao, B. Zhang, H. Zhou, D. Wei, C. Huang, and Q. Lan, “Multiscale convolutional Transformer network for motor imagery braincomputer interface,” Scientiﬁc Reports, vol. 15, no. 1, p. 12935, 2025.
- [35] Q. Zhao and W. Zhu, “TMSA-Net: A novel attention mechanism for improved motor imagery EEG signal processing,” Biomedical Signal Processing and Control, vol. 102, p. 107189, 2025.
- [36] K. Liu, T. Yang, Z. Yu, W. Yi, H. Yu, G. Wang, and W. Wu, “MSVTNet: Multi-scale vision Transformer neural network for EEG-based motor imagery decoding,” IEEE Journal of Biomedical and Health Informatics, vol. 28, no. 12, pp. 7126–7137, 2024.
- [37] H. Li, H. Zhang, and Y. Chen, “Dual-TSST: A dual-branch temporalspectral-spatial Transformer model for EEG decoding,” IEEE Journal of Biomedical and Health Informatics, pp. 1–14, 2025.
- [38] Y. Song, Q. Zheng, Q. Wang, X. Gao, and P.-A. Heng, “Global adaptive Transformer for cross-subject enhanced EEG classiﬁcation,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 2767– 2777, 2023.
- [39] E. Marcos, S. Tsujimoto, and A. Genovesio, “Independent coding of absolute duration and distance magnitudes in the prefrontal cortex,” Journal of Neurophysiology, vol. 117, no. 1, pp. 195–203, 2017.
- [40] F. Faugeras and L. Naccache, “Dissociating temporal attention from spatial attention and motor response preparation: A high-density EEG study,” NeuroImage, vol. 124, pp. 947–957, 2016.
- [41] A. Gu and T. Dao, “Mamba: Linear-time sequence modeling with selective state spaces,” arXiv preprint arXiv:2312.00752, 2023.
- [42] J. Xie, J. Zhang, J. Sun, Z. Ma, L. Qin, G. Li, H. Zhou, and Y. Zhan, “A Transformer-based approach combining deep learning network and spatial-temporal information for raw EEG classiﬁcation,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 2126– 2136, 2022.
- [43] A. Hameed, R. Fourati, B. Ammar, A. Ksibi, A. S. Alluhaidan, M. B. Ayed, and H. K. Khleaf, “Temporal-spatial Transformer based motor imagery classiﬁcation for BCI using independent component analysis,” Biomedical Signal Processing and Control, vol. 87, p. 105359, 2024.
- [44] C. Ju and C. Guan, “Graph neural networks on spd manifolds for motor imagery classiﬁcation: A perspective from the time-frequency analysis,” IEEE Trans. on Neural Networks and Learning Systems, vol. 35, no. 12, pp. 17 701–17 715, 2023.
- [45] S. Cai, H. Li, Q. Wu, J. Liu, and Y. Zhang, “Motor imagery decoding in the presence of distraction using graph sequence neural networks,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 1716–1726, 2022.
- [46] D. Zhang, K. Chen, D. Jian, and L. Yao, “Motor imagery classiﬁcation via temporal attention cues of graph embedded EEG signals,” IEEE Journal of Biomedical and Health Informatics, vol. 24, no. 9, pp. 2570– 2579, 2020.

- [47] A. R. W. Sait and Y. Alkhurayyif, “Lightweight hybrid Transformersbased dyslexia detection using cross-modality data,” Scientiﬁc Reports, vol. 15, no. 1, p. 17054, 2025.
- [48] M. J. Ahmed, U. Afridi, H. A. Shah, H. Khan, M. W. Bhatt, A. Alwabli, and I. Ullah, “CardioGuard: AI-driven ECG authentication hybrid neural network for predictive health monitoring in telehealth systems,” SLAS Technology, vol. 29, no. 5, p. 100193, 2024.
- [49] H. He and D. Wu, “Transfer learning for brain-computer interfaces: A Euclidean space data alignment approach,” IEEE Trans. on Biomedical Engineering, vol. 67, no. 2, pp. 399–410, 2020.
- [50] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” in Proc. Advances in Neural Information Processing Systems, Long Beach, CA, USA, Dec. 2017.
- [51] S. Chevallier, I. Carrara, B. Aristimunha, P. Guetschel, S. Sedlar, B. Lopes, S. Velut, S. Khazem, and T. Moreau, “The largest EEG-based BCI reproducibility study for open science: the MOABB benchmark,” arXiv preprint arXiv:2404.15319, 2024.
- [52] M. Tangermann, K.-R. Mu¨ller, A. Aertsen, N. Birbaumer, C. Braun, C. Brunner, R. Leeb, C. Mehring, K. J. Miller, G. R. Mu¨ller-Putz et al., “Review of the BCI competition IV,” Frontiers in Neuroscience, vol. 6, p. 55, 2012.
- [53] R. Leeb, F. Lee, C. Keinrath, R. Scherer, H. Bischof, and G. Pfurtscheller, “Brain–computer communication: motivation, aim, and impact of exploring a virtual apartment,” IEEE Trans. on Neural Systems and Rehabilitation Engineering, vol. 15, no. 4, pp. 473–482, 2007.
- [54] B. Zhou, X. Wu, Z. Lv, L. Zhang, and X. Guo, “A fully automated trial selection method for optimization of motor imagery based braincomputer interface,” PloS One, vol. 11, no. 9, p. e0162657, 2016.
- [55] B. Blankertz, G. Dornhege, M. Krauledat, K.-R. Mu¨ller, and G. Curio, “The non-invasive Berlin brain–computer interface: fast acquisition of effective performance in untrained subjects,” NeuroImage, vol. 37, no. 2, pp. 539–550, 2007.
- [56] D. Steyrl, R. Scherer, J. Faller, and G. R. Mu¨ller-Putz, “Random forests in non-invasive sensorimotor rhythm brain-computer interfaces: A practical and convenient non-linear classiﬁer,” Biomedical Engineering/Biomedizinische Technik, vol. 61, no. 1, pp. 77–86, 2016.
- [57] M. H. Lee, O. Y. Kwon, Y. J. Kim, H. K. Kim, Y. E. Lee, J. Williamson, S. Fazli, and S. W. Lee, “EEG dataset and OpenBMI toolbox for three BCI paradigms: An investigation into BCI illiteracy,” GigaScience, vol. 8, no. 5, p. giz002, 2019.
- [58] Z. Wang, W. Zhang, S. Li, X. Chen, and D. Wu, “Unsupervised domain adaptation for cross-patient seizure classiﬁcation,” Journal of Neural Engineering, vol. 20, no. 6, p. 066002, 2023.
- [59] N. J. Stevenson, K. Tapani, L. Lauronen, and S. Vanhatalo, “A dataset of neonatal EEG recordings with seizure annotations,” Scientiﬁc Data, vol. 6, no. 1, pp. 1–8, 2019.
- [60] M. Nakanishi, Y. Wang, Y. T. Wang, and T. P. Jung, “A comparison study of canonical correlation analysis based methods for detecting steadystate visual evoked potentials,” PloS One, vol. 10, no. 10, pp. 1–18, 2015.
- [61] S. Li, Z. Wang, H. Luo, L. Ding, and D. Wu, “T-TIME: Test-time information maximization ensemble for plug-and-play BCIs,” IEEE Trans. on Biomedical Engineering, vol. 71, no. 2, pp. 423–432, 2024.
- [62] Y. Pan, J. Chen, Y. Zhang, and Y. Zhang, “An efﬁcient CNN-LSTM network with spectral normalization and label smoothing technologies for SSVEP frequency recognition,” Journal of Neural Engineering, vol. 19, no. 5, p. 056014, 2022.
- [63] Z. Wang, S. Li, and D. Wu, “Canine EEG helps human: Crossspecies and cross-modality epileptic seizure detection via multi-space alignment,” National Science Review, vol. 12, no. 6, p. nwaf086, 2025.
- [64] Y. Benjamini and Y. Hochberg, “Controlling the false discovery rate: A practical and powerful approach to multiple testing,” Journal of the Royal Statistical Society: Series B, vol. 57, no. 1, pp. 289–300, 1995.
- [65] L. Van der Maaten and G. Hinton, “Visualizing data using t-SNE,” Journal of Machine Learning Research, vol. 9, no. 11, pp. 2579–2605, 2008.

