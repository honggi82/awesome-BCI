[Figure 1]

IEEE TRANSACTIONS AND JOURNALS TEMPLATE 1

## EEG-Deformer: A Dense Convolutional Transformer for Brain-computer Interfaces

Yi Ding, Member, IEEE, Yong Li, Hao Sun, Rui Liu, Chengxuan Tong, Graduate Student Member, IEEE, Chenyu Liu, Xinliang Zhou, and Cuntai Guan, Fellow, IEEE

Abstract—Effectively learning the temporal dynamics in electroencephalogram (EEG) signals is challenging yet essential for decoding brain activities using brain-computer interfaces (BCIs). Although Transformers are popular for their long-term sequential learning ability in the BCI field, most methods combining Transformers with convolutional neural networks (CNNs) fail to capture the coarse-to-fine temporal dynamics of EEG signals. To overcome this limitation, we introduce EEG-Deformer, which incorporates two main novel components into a CNN-Transformer: (1) a Hierarchical Coarse-to-Fine Transformer (HCT) block that integrates a Fine-grained Temporal Learning (FTL) branch into Transformers, effectively discerning coarseto-fine temporal patterns; and (2) a Dense Information Purification (DIP) module, which utilizes multi-level, purified temporal information to enhance decoding accuracy. Comprehensive experiments on three representative cognitive tasks—cognitive attention, driving fatigue, and mental workload detection—consistently confirm the generalizability of our proposed EEG-Deformer, demonstrating that it either outperforms or performs comparably to existing state-of-the-art methods. Visualization results show that EEG-Deformer learns from neurophysiologically meaningful brain regions for the corresponding cognitive tasks. The source code can be found at https://github.com/yi-dingcs/EEG-Deformer.

|[Figure 2]| |
|---|---|
| | |

EEGViT

... Out

Trans

Trans

Trans

### arXiv:2405.00719v2[eess.SP]29Oct2024

MLP

LP

|[Figure 3]| |
|---|---|
| | |

EEGConformer

... Out MLP

Trans

Trans

Trans

CNN

IP IP ... IP

|[Figure 4]| |
|---|---|
| | |

EEGDeformer (ours)

... C Out

CNN

MLP

HCT

HCT

HCT

Fig. 1. Comparison of network architectures between ViT [7], EEGConformer [8], and our proposed EEG-Deformer. We propose a novel Hierarchical Coarse-to-Fine Transformer (HCT). Additionally, we have designed Information Purification Unit (IP-Unit, denoted by IP in the figure) for each HCT layer with dense connections to further boost EEG decoding performance.

EEG signals, collected through electrodes placed on each subject’s head, comprise spatial and temporal dimensions. The spatial dimension relates to the locations of the EEG electrodes, while the temporal dimension captures fluctuations in brain activity [2]. To ensure accuracy in decoding neural activity, a reliable BCI system must effectively perceive the subtle temporal dynamics encoded in EEG signals, which implicitly represent various cognitive processes. However, this task is quite challenging, as these brain activities vary across subjects and are susceptible to external interference, such as movement artifacts, eye blinks, and environmental factors [9].

Index Terms—Deep learning, electroencephalography, transformer.

I. INTRODUCTION

# B

RAIN-computer interface (BCI) technology facilitates direct communication between the brain and machines

using electroencephalography (EEG) [1]. A standard BCI system usually consists of four key components: data acquisition, pre-processing, classification, and feedback [2]. BCIs are employed in various practical applications, such as stroke rehabilitation [3], sleep stage detection [4], [5], and emotion regulation in mental health treatments [6].

Recently, numerous deep learning-based approaches have been developed for decoding brain activities from EEG signals. These approaches can be broadly categorized into two types: methods using hand-crafted features and methods using EEG directly as input. The former [10]–[14] involve extracting various types of features from EEG signals for neural network input. Meanwhile, CNN-based methods, which leverage automatic feature learning, typically process EEG as 2-D time series [15]–[17]. Given that EEG data is inherently graphstructured, with nodes representing electrodes and connections based on spatial distance, functional connectivity, or learned relationships, graph-based methods have gained popularity [10], [18], [19]. However, using features as input may result

Yi Ding and Yong Li contribute equally to this work. Yi Ding, Yong Li, Rui Liu, Chengxuan Tong, Chenyu Liu, Xinliang Zhou, and Cuntai Guan are with the College of Computing and Data Science, Nanyang Technological University, 50 Nanyang Avenue, Singapore, 639798.

Hao Sun is with the Key Laboratory of Smart Manufacturing in Energy Chemical Process, Ministry of Education, East China University of Science and Technology, Shanghai, China.

Chengxuan Tong is with Wilmar International, Singapore. Cuntai Guan is the Corresponding Author. This work was supported by the RIE2020 AME Programmatic Fund,

Singapore (No. A20G8b0102) and the MoE AcRF Tier 1 Project (No. RT01/21)

in the loss of fine-grained temporal information by averaging data along the temporal dimensions. Additionally, CNN-based methods may fail to capture long-term temporal dependencies by employing CNN kernel along temporal dimension.

In addition to CNNs, transformer-based neural architectures have attracted significant attention in the BCI field due to their inherent ability to perceive global dependencies. Commonly, prior works [8], [20]–[22] adopt a CNN-Transformer architecture, where the CNN part serves as an adaptive feature encoder to preprocess EEG data, and the subsequent transformer part captures long-range temporal characteristics. The CNN-based shallow feature encoder has been verified as essential for preparing EEG data for Transformers [20]. Although previous works can capture either fine-grained (short-period) or coarsegrained (global) temporal dependencies within each layer, they have not explicitly captured both coarse- and fine-grained temporal dynamics within the Transformer layers, which may limit the full utilization of EEG signals’ long-short period temporal dynamics [23]. Moreover, most existing methods overlook the abundant latent features encoded within intermediate neural layers. These layers encapsulate rich temporal information that can be systematically explored to enhance the precise discernment of temporal dynamics inherent in EEG data.

To mitigate the above-mentioned issues and enhance the perception of temporal dynamics in EEG data, we introduce EEG-Deformer, a novel dense convolutional Transformer. We propose a novel Hierarchical Coarse-to-Fine Transformer (HCT) block that integrates a Fine-grained Temporal Learning (FTL) branch into Transformers. Built upon a CNN-based shallow feature encoder comprising collaborative temporal and spatial convolutional layers, HCT concurrently captures coarse- and fine-grained temporal dynamics, as shown in Figure 1. The FTL branch employs a 1-D CNN to sequentially capture short-period temporal dynamics of EEG, generating fine-grained temporal representations. These representations are then adaptively fused with the coarse-grained temporal representations encoded by the Transformers, thereby providing more discriminative long- and short-term temporal information.

Furthermore, to efficiently utilize multi-level temporal information from intermediate HCT layers, we have designed a Dense Information Purification (DIP) module in our EEGDeformer. This module enables the dense transmission of multi-level representations from HCT layers to the final representation. Differing from the skip connections in DenseNet [24], we introduce an Information Purification Unit (IP-Unit) that transforms the fine-grained representations from FTL branches using a logarithmic (log) power operation [18] and elegantly fuses these latent representations into the final representation. Because log power can represent the amount of activity in filtered signals and reduce dimensions [25], our IPUnit not only retains critical frequency characteristics related to brain activity but also effectively reduces the number of learnable parameters. As illustrated in Figure 1, a series of IPUnits have been added to the intermediate layers. These units progressively encode discriminative temporal representations. We will validate these enhancements in Sec. V-B to V-E.

In summary, the contributions of this work are summarized

as follows:

- • We introduce EEG-Deformer, a novel architecture designed for EEG decoding across various cognitive tasks.
- • A hierarchical coarse-to-fine Transformer is proposed to effectively encode the coarse-to-fine temporal dynamics within EEG data.
- • We develop a dense information purification module to fully exploit abundant intermediate multi-level EEG features and enhance the EEG decoding performance.
- • Through extensive experimentation on three public datasets, encompassing attention, fatigue, and cognitive workload classification tasks, the efficacy of EEGDeformer is demonstrated. Our results show its superiority compared to current state-of-the-art (SOTA) methods.

II. RELATED WORK

- A. CNNs for EEG Decoding

Convolutional Neural Networks (CNNs) have become powerful tools in BCI applications, excelling in learning directly from EEG data [15]–[17], [26]. Schirrmeister et al.

- [15] introduced DeepConvNet, which incorporates a twostage spatial and temporal convolution layer to facilitate EEG feature extraction and classification. Similarly, Lawhern et al.
- [16] developed EEGNet, using depth-wise convolution with a kernel size of (n,1)—where n represents the number of EEG channels—to capture spatial features. Building on these methods, TSception [17] employs multi-scale convolutional kernels to decode temporal dynamics and asymmetric spatial activations within EEG signals. However, the relatively short length of these 1-D CNN kernels in the temporal dimension limits their ability to capture long-term temporal patterns effectively.

- B. Transformers for BCI

Transformers, renowned for capturing long-term dependencies in sequential data, have gained considerable attention in EEG research [8], [20]–[22], [27], [28]. Lee et al. [22] showed that integrating a self-attention module from the Transformer architecture into an EEGNet-based CNN improves classification accuracy for imagined speech from EEG data. EEG-Conformer [8], a streamlined convolutional Transformer model, effectively combines local and global features for EEG decoding within a unified structure. However, most existing convolutional Transformers, which typically leverage CNNs for shallow feature extraction followed by Transformer blocks, may struggle to learn both coarse- and fine-grained temporal patterns in EEG signals. Furthermore, they frequently miss out on capturing multi-level temporal information available across different layers.

III. METHOD

In this work, we propose a novel Transformer, EEGDeformer, for general EEG decoding in the BCI field. The network architecture is shown in Figure 2. EEG-Deformer consists of three main components: (1) a Shallow feature encoder, (2) a Hierarchical Coarse-to-fine Transformer (HCT),

𝑰𝟏: 𝑘 𝑰𝟐: 𝑘 𝑰𝟑: 𝑘 𝑰𝟒: 𝑘

DIP

IP-Unit IP-Unit IP-Unit IP-Unit

| | | | |
|---|---|---|---|
| | | | |

Encoder

𝑿: 𝑐×𝑙

[Figure 5]

𝑙 32

𝑙 4

𝑙 8

𝑙 16

𝑙 2

𝑭𝟓: 𝑘×

𝑭𝟐: 𝑘×

𝑭𝟑: 𝑘×

𝑭𝟒: 𝑘×

𝑭𝟏: 𝑘×

TemporalConv

SpatialConv

Tokenizer

MLP

Output

C

HCT HCT HCT HCT

- Fig. 2. The network structure of EEG-Deformer. EEG-Deformer consists of three main parts: (1) Shallow feature encoder, (2) Hierarchical coarse-tofine-Transformer (HCT), and (3) Dense information purification (DIP). The fine-grained representations from each HCT will be passed to Information Purification Unit (IP-Unit) and concatenated (C) to the final embedding.

Conv2D

Conv2D

BatchNorm

ELU

MaxPool

Rearrange

+ X 𝐹

- Fig. 3. The structure of the shallow feature encoder. After standard CNN layers, the representation is rearranged into kernel by feature, and a position encoding is added onto it.

lasting approximately 100 ms, the temporal CNN kernels are sized at (1,0.1 × fs), where fs denotes the EEG’s sampling rate. For capturing spatial information from EEG, a spatial CNN kernel of size (c,1) is utilized as suggested in [16], where c is the number of EEG channels. Weight normalization is included following the approach in [29]. The number of CNN kernels is denoted by k. After activation by the ELU function, the learned features are max-pooled every two data points without overlapping. The tokenizer includes rearrange operation and a learnable position encoding. The size of the features is then rearranged into k × 0.5l to serve as tokens for the Transformers, which learn coarse-grained temporal information. Subsequently, a learnable position encoding, P ∈ Rk×0.5l, is added to the tokens [7]. Therefore, the encoded tokens can be represented as F ∈ Rk×0.5l. This step can be formularized as

and (3) a Dense Information Purification (DIP) module. Given an input segment of EEG signals, EEG-Deformer utilizes the CNN feature encoder to adaptively encode the shallow temporal and spatial features, which are then set as input into the following HCT blocks to extract the temporal dynamics that happen in different timescales in EEG signals. To effectively perceive the critical multi-level temporal information, the features generated from each HCT block are adaptively fused via progressive IP-Units. Below, we present the details for each of them.

F = Γ(MaxPool(ELU(BN(CNN(X))))) + P, (1)

where Γ(·) is the rearrange operation and BN(·) is the batch normalization layer.

B. Hierarchical Coarse-to-fine Transformer

With the encoded shallow EEG features, we aim to learn the coarse and fine-grained temporal dynamics in EEG data via cascading HCT blocks. The neural structure of a HCT block is shown in Fig. 4. A HCT consists parallel Transformer-based branch that aims to learn the correlations among the given tokens [30] and CNN-based branch that aims to learn finegrained EEG features.

A. Shallow Feature Encoders

To capture the shallow temporal and spatial information of EEG, we utilize a CNN-based shallow feature encoder. It comprises two main components: CNN layers and a tokenizer. CNNs along temporal and spatial dimensions are commonly used as feature extractors for EEG signals [16]. In our proposed EEG-Deformer, a two-layer CNN is adopted as the shallow feature encoder. The architecture of the CNN encoder is shown in Figure 3. It begins with temporal and spatial CNN layers, followed by batch normalization to mitigate the covariate shift issue.

i t the input to the i-th HCT block. To capture the coarse-grained temporal dynamics of EEG signals, we treat the output of each CNN kernel as one token. By doing so, the long-term temporal information is explicitly included when we project the tokens into Qi ∈ Rn

Let us suppose Fi ∈ Rk×l

head×k×dattn, Ki ∈ Rn

Let’s denote an EEG sample as X ∈ Rc×l, where c is the number of EEG channels, and l represents the number of data points along the time dimension. Inspired by neurophysiological knowledge that the brain has microstates

##### head×k×dattn, and Vi ∈ Rn

head×k×dattn using the linear projection (LP) layer parameterized by nhead set of Wiqkv ∈ R

li

t

2i−1 ×3dattn. Before the LP layer, a max pooling

CNN layer, followed by a batch normalization layer, an ELU activation, and a max-pooling layer. The fine-grained temporal representations, denoted as Ffgi , can be calculated as follows:

𝑭 𝑭

+

𝑭

FFN

MaxPool

Ffgi = MaxPool(ELU(BN(CNN(DP(Fi)))), (6) where DP(·) is the dropout operation.

LayerNorm

ELU

Add

After learning the coarse- and fine-grained temporal representations, a sum fusion is added to get the final output of the HCT layer

BatchNorm

MSA

Conv1D

K Q V

LP

Dropout

Fi+1 = Fcgi + Ffgi . (7)

MaxPool

For the Ffgi , it is also used to do the information purification process.

𝑭

C. Dense Information Purification

- Fig. 4. The structure of the hierarchical coarse-to-fine Transformer: The right side is capable of learning coarse-grained temporal information through self-attention, while the left side is the newly added FTL.

With the learned fine-grained temporal features from different HCT layers, we further utilize densely connected IP-Units to progressively extract the multi-level temporal information from these layers. It aims to extract discriminative information from a frequency perspective and reduce the size of the bypassed multi-level representations.

layer with a pooling size of 2 and a step of 2 is added to reduce the feature dimension of Fi. The encoding process Φ(·) can be formularized by

Drawing inspiration from neural engineering, where power features of EEG signals in different frequency bands are widely used for brain activity analysis [15], [31], we propose a power layer for information purification and encode frequency information in EEG signals. The power of the learned 1-D hidden representations , Ii ∈ Rk, can be calculated by

{Qi,Ki,Vi} = Φi(Fi) = MaxPool(Fi)Wqkvi . (2)

A multi-head self-attention (MSA) is then utilized to extract the correlations among the different views of the coarsegrained temporal embeddings. The scaled dot-product is utilized as the attention operation along temporal tokens for each attention head.

Ii =IPpower(Ffgi )

(8)

1 lti

(ffgi,j)2) : ffgi,j ∈ Ffgi },

={log(

√

Attn(Q,K,V ) = Softmax(QKT/

d)V , (3)

i

where log(·) is the logarithm, and ffgi,j ∈ Rl

t is one learned representation from the j-th CNN kernel in the FTL.

where d = dattn is a scaling factor. The output of each attention head will be concatenated and linearly projected into

The purified information from all HCT layers is concatenated with the flattened output of the last HCT layer to obtain the final hidden embedding. A linear layer is then utilized as the classifier to project the hidden embedding onto the class labels. Let nhct denote the total number of HCT layers; this process can be formulated as:

a tensor, Fmsai , that has the same size of the input by

Fmsai =MSA(Fi)

(4)

=[Attn(Φ1i(Fi)),...,Attn(Φn

i (Fi))]Wattni ,

head

where [·] is concatenation operation and Wattni ∈ Rn

i t

headdattn× l

2i−1 is the learnable weights.

#### ]W + b, (9)

#### out = [Fn

hct+1,I1,...,In

After the MSA, a residual connection is introduced, followed by layer normalization and a Feedforward Neural Network (FFN). The FFN consists of two layers, utilizing a GELU non-linearity, similar to those used in ViT [7]. Consequently, the coarse-grained embedding, denoted as Fcgi , is generated by:

hct

where [·] is the concatenation operation, W and b are the trainable weights and biases.

IV. EXPERIMENT A. Datasets and Pre-processing

We evaluate the performance of EEG-Deformer with three benchmarking EEG datasets, which are Dataset I [32] for cognitive attention, Dataset II [33] for driving fatigue, and Dataset III [34] for cognitive workload.

Fcgi = FFN(LN(Fmsai + MaxPool(Fi))), (5) where LN(·) is the layer normalization operation.

We further propose a FTL module to capture the shortperiod temporal dynamics of EEG signals. To learn finegrained temporal features, we opt for a 1-D CNN, as its short kernel moves along the temporal dimension step by step, enabling the learning of short-period patterns. After a dropout layer, the learned representations are fed into a 1-D

Dataset I: Dataset I provides EEG signals recorded while subjects perform the Discrimination/Selection Response (DSR) task to assess cognitive attention. The experiment involves a total of 26 participants. Each subject undergoes three sessions, with each session consisting of multiple cycles of attention

TABLE I GENERALIZED CROSS-SUBJECT CLASSIFICATION RESULTS FROM VARIOUS METHODS ON THREE BENCHMARKING DATASETS. THE BEST RESULTS ARE HIGHLIGHTED IN BOLD AND THE NEXT BEST ARE MARKED USING UNDERLINES

Dataset I: Attention Dataset II: Fatigue Dataset III: Mental Workload ACC std F1-macro std ACC std F1-macro std ACC std F1-macro std

Method

DGCNN 60.98 6.05 56.81 9.51 69.56 12.50 64.92 13.08 64.85 17.90 59.42 22.25 LGGNet 67.81 6.38 66.70 7.69 68.16 13.16 65.38 12.40 65.37 12.78 61.91 16.16 EEGNet 75.28 9.77 73.81 12.62 73.95 12.54 71.43 13.45 65.85 14.55 61.89 18.21 TSception 71.60 7.66 69.94 10.88 73.01 12.93 70.18 13.90 69.92 15.07 65.26 20.04 EEG-ViT 67.72 7.03 66.79 8.49 66.95 14.12 64.12 13.89 63.12 15.44 61.19 16.56 SSVEPformer 73.18 7.87 72.7 8.54 55.02 10.95 52.00 9.87 55.17 6.71 54.25 7.01 EEG-Transformer 75.39 7.92 74.93 8.61 65.53 11.2 63.86 12.84 64.46 14.91 64.28 14.94 EEG-Conformer 79.81 9.27 79.01 10.75 74.36 11.82 71.65 12.96 69.40 14.48 65.59 18.68

EEG-Deformer (ours) 82.72 8.00 82.36 8.52 79.32 7.87 75.83 11.54 73.18 15.63 69.99 19.80

TABLE II RESULTS OF THE ABLATION STUDY CONDUCTED ON THREE BENCHMARKING DATASETS, WITH THE BEST RESULTS MARKED IN BOLD.

Dataset I: Attention Dataset II: Fatigue Dataset III: Mental Workload ACC std F1-macro std ACC std F1-macro std ACC std F1-macro std

Method

w/o FTL 70.39 6.89 69.89 7.39 70.48 14.76 68.63 13.97 63.31 11.67 61.79 13.25 w/o Dense connection 75.84 7.24 75.40 7.67 70.85 14.11 68.86 14.22 72.46 14.73 69.30 18.88 w/o IP-Unit 72.01 7.26 71.28 8.06 73.28 12.10 70.98 12.64 67.29 11.75 64.48 14.73 EEG-Deformer (ours) 82.72 8.00 82.36 8.52 79.32 7.87 75.83 11.54 73.18 15.63 69.99 19.80

tasks, each lasting 40 seconds, and alternating with rest periods of 20 seconds. Data collection includes recordings from 28 EEG channels, sampled at a rate of 1000 Hz. BrainAmp EEG amplifier (Brain Products GmbH, Gilching, Germany) was used to collect the EEG signals. For the pre-processing, a band-pass filter ranging from 0.5 to 50 Hz was applied to eliminate low and high-frequency noise, following the methodology in [11]. Eye movement artifacts were removed using the automatic Independent Component Analysis (ICA) Electrooculography (EOG) removal method in the MNE toolbox [35]. The data were then downsampled to 200 Hz. In accordance with [18], only the first half of each attention trial (20 seconds) was used to balance the samples between attention and inattention (rest). Each trial was further segmented into 4-second segments with a 50% overlap. All three sessions are utilized in this study.

Dataset II: Dataset II is designed to evaluate cognitive fatigue states in drivers through EEG signal analysis during a 90minute driving task within a virtual reality (VR) driving environment. This dataset was compiled with the participation of 27 subjects. EEG data were captured using a 32-channel Scan SynAmps2 Express system (Compumedics Ltd., VIC, Australia), with a sampling rate of 500 Hz. The official preprocessed data are used. For pre-processing, the raw EEG signals were filtered by a band-pass filter from 1 to 50 Hz. Eye blinks were manually removed through visual inspection. Ocular and muscular artifacts were removed using the Automatic Artifact Removal (AAR) method in EEGLab [36]. Following [18], the data were downsampled to 128 Hz. For calculating fatigue levels, we also adhered to the approach outlined in [18]. EEG trials were defined as the 3 seconds of EEG data preceding the onset of lane-departure events. Reaction time (RT) was used to measure fatigue levels for these EEG trials.

RT was defined as the interval from the onset of the lanedeparture event to the onset of the counter-steering event. The local RT (RTl) of a trial was defined as the RT for that specific trial. The global RT (RTg) of a trial was the mean of the local RTs of all trials within a 90-second window before the current trial. The 5th percentile of all local RTs in the entire session was selected as the alert RT (RTa). The labeling process was defined as follows:

- 0 RTl > 2.5 ∗ RTa&&RTg > 2.5 ∗ RTa
- 1 RTl < 1.5 ∗ RTa&&RTg < 1.5 ∗ RTa

(10)

y =

where 0 represent the fatigue class and 1 represent the nonfatigue class. Following [18], 11 subjects who had enough samples for each class are utilized.

Dataset III: Dataset III provides 19-channel EEG recordings from 36 subjects engaged in mental cognitive tasks, specifically performing serial subtraction, along with their corresponding baseline EEG for reference. The official artifactfree data are used in this study. The EEG were recorded using a Neurocom EEG 23-channel system (Ukraine, XAIMEDICA). Electrodes were positioned on the scalp according to the International 10-20 system, and all electrodes were referenced to ear reference electrodes. A high-pass filter with a 30 Hz cut-off frequency and a power line notch filter (50 Hz) were applied. ICA was used to eliminate artifacts. Each mental workload trial lasts for 60 seconds, and the last 60 seconds of the rest EEG are used as the low workload data. The trials are segmented using a 4-second sliding window with a moving step of 2 seconds.

B. Baselines

We demonstrate the performance of EEG-Deformer by comparing it with the following baseline methods: 1) two graph-

TABLE III EFFECTS OF DIFFERENT INFORMATION PURIFICATION METHODS ON THREE BENCHMARKING DATASETS, WITH THE BEST RESULTS HIGHLIGHTED IN BOLD.

Dataset I: Attention Dataset II: Fatigue Dataset III: Mental Workload ACC std F1-macro std ACC std F1-macro std ACC std F1-macro std

Method

Using mean 77.35 6.99 76.99 7.33 73.82 12.13 71.72 12.93 68.82 15.44 65.47 18.90 Using std 77.54 7.54 77.04 8.07 73.94 14.42 72.34 14.77 72.27 15.20 69.19 19.00 Using power 82.72 8.00 82.36 8.52 79.32 7.87 75.83 11.54 73.18 15.63 69.99 19.80

TABLE IV EFFECTS OF VARIOUS INFORMATION PURIFICATION LOCATIONS ON THREE BENCHMARKING DATASETS, WITH THE BEST RESULTS HIGHLIGHTED IN BOLD.

Dataset I: Attention Dataset II: Fatigue Dataset III: Mental Workload ACC std F1-macro std ACC std F1-macro std ACC std F1-macro std

Method

At Fi+1 80.28 7.46 79.81 8.03 77.25 7.14 73.98 9.96 69.16 15.46 66.35 18.19 At Fcgi 72.90 7.30 72.05 8.35 44.72 16.48 29.96 8.30 71.41 15.30 68.56 18.50 At Ffgi 82.72 8.00 82.36 8.52 79.32 7.87 75.83 11.54 73.18 15.63 69.99 19.80

based methods, DGCNN [10] and LGGNet [18]; 2) two CNNbased methods, EEGNet [16] and TSception [17]; 3) four Transformers, EEG-ViT, our adapted version of [7], SSVEPformer [21], EEG-Transformer [37], and EEG-Conformer [8].

- 1) DGCNN: DGCNN introduces a learnable adjacency ma-

trix that dynamically captures and updates relationships between EEG channels during training, allowing for a more flexible and accurate representation of the EEG signal.

- 2) LGGNet: LGGNet, a neurology-inspired graph neural

network, captures local-global-graph representations of EEG data. Its input layer uses multi-scale temporal convolutions with attentive fusion to capture EEG dynamics, followed by graph-filtering layers that model complex relationships within and between brain regions.

- 3) EEGNet: EEGNet is a compact convolutional neural

network designed for EEG-based BCIs, using depth-wise and separable convolutions to efficiently integrate EEG feature extraction techniques, making it highly effective for EEG decoding.

- 4) TSception: TSception is a multi-scale convolutional neu-

ral network that combines dynamic temporal layers, asymmetric spatial layers, and advanced fusion to capture complex patterns in EEG signals. This design effectively extracts discriminative features for accurate emotion recognition.

- 5) EEG-ViT: To explore the effects of combining CNNs and

Transformers for decoding EEG signals, we adapt ViT [7], a purely Transformer-based architecture, for EEG data. We partition the EEG into non-overlapping segments along the temporal dimension and convert these segments into tokens using a linear projection layer, enabling ViT to process EEG effectively.

- 6) SSVEPformer: The SSVEPformer is a Transformer-

based method that comprises channel combination, SSVEPformer encoder, multilayer perceptron (MLP) head three core components that can extract spectrum information from the complex spectrum representation of EEG.

- 7) EEG-Transformer: EEG-Transformer is a convolutional

Transformer that combines an EEGNet-based CNN feature

extractor with a vanilla Transformer [30] to decode EEG signals effectively.

8) EEG-Conformer: EEG-Conformer, like EEGTransformer, combines CNNs and Transformers to capture spatial-temporal information in EEG signals. It uses 1-D CNNs for local feature extraction and a self-attention module to reveal global correlations in these temporal features.

C. Experiment Settings

In this study, we implement generalized subject-independent settings, ensuring that test data information is not used during the training stage. We adopt a leave-one-subject-out (LOSO) approach for all three datasets. In each LOSO step, one subject’s data is set aside as test data. Of the remaining data, 80% is used for training and the remaining 20% serves as validation (development) data. We employ Accuracy (ACC) and MacroF1 as our evaluation metrics which can be formularized as

TP + TN TP + FP + TN + FN

(11)

Accuracy =

1 N

F1-macro =

N

F1-scorei, (12)

i=1

2 · TPi 2 · TPi + FPi + FNi

F1-scorei =

, (13)

where TP is the true positive, TN is the true negative, FP is the false positive, FN is the false negative, and the subscript indicates the i-th class.

D. Implementation Details

The PyTorch implementation is available on this website1. The cross-entropy loss is utilized to guide the training. We use an Adam optimizer with an initial learning rate of 1e-3 and a weight decent of 1e-5. A cosine annealing schedule is adopted to adjust the learning rate during training. A dropout rate of

1https://github.com/yi-ding-cs/EEG-Deformer

Fp2

Fp1

[Figure 6]

AFz

AFF6 F2

AFF5

F1

FC2 FC6

FC5 FC1

C3 Cz

C4

T8

T7

CP5 CP1

CP2 CP6

P3 Pz

P4

P8

P7

POz O1

O2

(a)

Fp2

Fp1

[Figure 7]

AFz

AFF6 F2

AFF5

F1

FC2 FC6

FC5 FC1

C3 Cz

C4

T8

T7

CP5 CP1

CP2 CP6

P3 Pz

P4

P8

P7

POz O1

O2

(b)

Fp2

Fp1

[Figure 8]

AFz

AFF6 F2

AFF5

F1

FC2 FC6

FC5 FC1

C3 Cz

C4

T8

T7

CP5 CP1

CP2 CP6

P3 Pz

P4

P8

P7

POz O1

O2

(c)

Fp2

Fp1

[Figure 9]

AFz

AFF6 F2

AFF5

F1

FC2 FC6

FC5 FC1

C3 Cz

C4

T8

T7

CP5 CP1

CP2 CP6

P3 Pz

P4

P8

P7

POz O1

O2

(d)

Fp2

Fp1

[Figure 10]

AFz

AFF6 F2

AFF5

F1

FC2 FC6

FC5 FC1

C3 Cz

C4

T8

T7

CP5 CP1

CP2 CP6

P3 Pz

P4

P8

P7

POz O1

O2

(e)

Fp2

Fp1

[Figure 11]

AFz

AFF6 F2

AFF5

F1

FC2 FC6

FC5 FC1

C3 Cz

C4

T8

T7

CP5 CP1

CP2 CP6

P3 Pz

P4

P8

P7

POz O1

O2

(f)

- Fig. 5. Saliency maps of attention classification tasks. (a)-(e) are five representative subjects and (f) is the average of all the subjects. The most informative areas are primarily located in the frontal (Fp1, F1, and AFF6) and parietal (CP5, P7, and P4) regions. The location of each EEG electrode can be found according to its name on the saliency map.

[Figure 12]

Fp1 Fp2

F7 F3 Fz F4 F8

FT7 FC3 FCz FC4 FT8

T3

C3 Cz C4

T4

TP7

CP3 CPz CP4

TP8

T5

P3 Pz P4

T6

O1 Oz O2

(a)

[Figure 13]

Fp1 Fp2

F7 F3 Fz F4 F8

FT7 FC3 FCz FC4 FT8

T3

C3 Cz C4

T4

TP7

CP3 CPz CP4

TP8

T5

P3 Pz P4

T6

O1 Oz O2

(b)

[Figure 14]

Fp1 Fp2

F7 F3 Fz F4 F8

FT7 FC3 FCz FC4 FT8

T3

C3 Cz C4

T4

TP7

CP3 CPz CP4

TP8

T5

P3 Pz P4

T6

O1 Oz O2

(c)

[Figure 15]

Fp1 Fp2

F7 F3 Fz F4 F8

FT7 FC3 FCz FC4 FT8

T3

C3 Cz C4

T4

TP7

CP3 CPz CP4

TP8

T5

P3 Pz P4

T6

O1 Oz O2

(d)

[Figure 16]

Fp1 Fp2

F7 F3 Fz F4 F8

FT7 FC3 FCz FC4 FT8

T3

C3 Cz C4

T4

TP7

CP3 CPz CP4

TP8

T5

P3 Pz P4

T6

O1 Oz O2

(e)

[Figure 17]

Fp1 Fp2

F7 F3 Fz F4 F8

FT7 FC3 FCz FC4 FT8

T3

C3 Cz C4

T4

TP7

CP3 CPz CP4

TP8

T5

P3 Pz P4

T6

O1 Oz O2

(f)

- Fig. 6. Saliency maps of fatigue classification tasks are shown. Figures (a) to (e) represent five representative subjects, and figure (f) is the average of all the subjects. The most informative areas are the frontal (F7, F3, and FCz), temporal (T3 and T5), and parietal (P3) regions. The location of each EEG electrode can be identified by its name on the saliency map.

[Figure 18]

Fp1 Fp2

F7 F3 F4 F8

T3 C3 C4 T4

T5 T6

P3 P4

O1 O2

Fz

Cz

Pz

(a)

[Figure 19]

Fp1 Fp2

F7 F3 F4 F8

T3 C3 C4 T4

T5 T6

P3 P4

O1 O2

Fz

Cz

Pz

(b)

[Figure 20]

Fp1 Fp2

F7 F3 F4 F8

T3 C3 C4 T4

T5 T6

P3 P4

O1 O2

Fz

Cz

Pz

(c)

[Figure 21]

Fp1 Fp2

F7 F3 F4 F8

T3 C3 C4 T4

T5 T6

P3 P4

O1 O2

Fz

Cz

Pz

(d)

[Figure 22]

Fp1 Fp2

F7 F3 F4 F8

T3 C3 C4 T4

T5 T6

P3 P4

O1 O2

Fz

Cz

Pz

(e)

[Figure 23]

Fp1 Fp2

F7 F3 F4 F8

T3 C3 C4 T4

T5 T6

P3 P4

O1 O2

Fz

Cz

Pz

(f)

- Fig. 7. Saliency maps for mental workload classification tasks are presented. Figures (a) to (e) represent five representative subjects, and figure (f) shows the average of all subjects. The frontal (Fz and Fp2) and parietal (P4) areas are found to be more informative. The location of each EEG electrode can be identified by its name on the saliency map.

0.5 is applied on dataset I and II to avoid over-fitting. The dropout rate is changed to 0.25 on dataset III as it achieves a better performance on development set. The batch size is 64 for all the datasets.We train the model for 200 epochs, and the model with the best validation accuracy is used to evaluate the test data. The kernel lengths of CNN layers are calculated by 0.1∗fs, where fs is the sampling rate of the EEG segment. The odd length is need for PyTorch to achieve the same padding. As the fs of three datasets are 200 Hz, 128 Hz, and 500 Hz, the kernel lengths of CNN layers lkernelI = 21, lkernelII = 13, and lkernelIII = 51. We set the number of CNN kernels as 64 for all the datasets as [18]. We set nhead = datten, and tune it based on the performance on the validation (development) set. Hence, we have nIhead = 32 and nIIhead = nIIIhead = 16.

V. RESULTS AND ANALYSES

- A. Classification Results

Attention Classification: The results for attention classification using dataset I, as presented in Table I, reveal that the EEG-Deformer outperforms all baseline methods. It achieves the highest accuracy and macro-F1 score in attention classification with 82.72% accuracy and a 82.36% macro-F1 score.

Compared to EEG-Conformer, the next best performer, EEGDeformer shows an improvement of 2.92% in accuracy and

- 3.35% in macro-F1 score. The results highlight that CNNbased methods generally outperform GNN-based ones and suggest that a combination of CNN and Transformer architectures yields better performance than using either CNN or Transformer alone.

Fatigue Classification: The same observation appears in the fatigue decoding task using dataset II, as detailed in Table I, the EEG-Deformer demonstrates superior performance, leading with an accuracy of 79.32% and a macro-F1 score of 75.83%. These results surpass those of the EEG-Conformer by

- 4.96% in accuracy and 4.18% in macro-F1 score. The same trend is shown here that the CNN-based methods are better than GNNs. And using Transformer without CNN layers yield low classification results.

Mental Workload Classification: Regarding the classification of mental workload using Dataset III, the EEG-Deformer continues to outperform its counterparts, achieving an accuracy of 73.18% and a macro-F1 score of 69.99%. Unlike in other tasks, the CNN-based method TSception ranks second here, closely followed by EEG-Conformer.

As a summary: 1) RNN-based methods is inferior to CNN-

w/o IP-1 w/o IP-2 w/o IP-3 w/o IP-4

8

| |6.51<br><br>5.21| | |
|---|---|---|---|
| |3.3| | |
| |3.19<br><br>1.3 1.29 1.63<br><br>3 2.82| | |
| |1.07 1.18 1.01| | |
| | | | |

DroppedACC(%)

6

4

2

0

Dataset I Dataset II Dataset III

(a) Dropped ACC

w/o IP-1 w/o IP-2 w/o IP-3 w/o IP-4

8

| | | | |
|---|---|---|---|
| |3.32<br><br>5.03<br><br>3.85 3.39| | |
| |1.34 1.28<br><br>3<br><br>1.95| | |
| |1.19 1.03 1.14 0.92| | |
| | | | |

DroppedF1(%)

6

4

2

0

Dataset I Dataset II Dataset III

(b) Dropped F1

- Fig. 8. Dropped ACC (a) and F1 scores (b) resulted from removing each IP-Unit from EEG-Deformer. Removing the first IP-Unit significantly impacted performance on datasets I and II, while the third IP-Unit was vital for dataset III, reflecting their input EEG segment lengths of 800, 384, and 2000, respectively. This indicates that longer EEG inputs require deeper IP-Units.

Transformers, EEG-Conformer, as indicated in [8]. Because EEG-Conformer has a better hierarchical sequence learning ability. 2) GNN-based methods have worse performance as they depend heavily on spatial connectivity patterns, which can vary across subjects [38], and are further constrained by EEG’s high temporal but low spatial resolution. 3) The results show that Convolutional Transformers excel over traditional Transformers in EEG classification tasks, which is consistent with the observations in [20]. 4) Although the EEG-Conformer outpaces other baselines, our model surpasses it by effectively capturing coarse-to-fine temporal information and utilizing multi-layer insights. Our enhancements specifically address these gaps, advancing EEG data analysis by learning coarseto-fine temporal information and utilizing purified information from each Transformer layer.

- B. Ablation

To investigate the individual contributions of the FTL, Dense connections of IP-Units, and IP-Unit, we conduct an ablation study by selectively removing these layers and observing their impact on classification outcomes across three datasets. The findings, detailed in Table II, indicate that the omission of the FTL had the most detrimental effect on performance overall. Additionally, the removal of the IP-Unit results in the second-largest decrease in performance on datasets I and II. Eliminating dense connections also leads to reductions in both classification accuracy and macro-F1 scores across all datasets. These results collectively imply that each module within the EEG-Deformer plays a crucial role, working in unison to enhance its predictive capabilities.

- C. Ablation of IP-Units

To further understand the role of each IP-Unit, we conducted a removal analysis where each IP-Unit was individually omitted to observe its impact. Figure 8 depicts the consequences of this removal, displaying reductions in accuracy (ACC) and F1 score. The results show that eliminating the first IP-Unit

- (a) Dataset I

- (b) Dataset II

- (c) Dataset III

Fig. 9. Comparisons about performance (ACC, on y-axis), model size (size of bubbles), and computational complexity (MACs, on x-axis). Light pink one is Deformer (ours). Our EEG-Deformer strikes a promising balance between accuracy and computational complexity.

resulted in the largest declines on datasets I and II, whereas the third IP-Unit was more crucial for dataset III. These findings seem to correlate with the lengths of the input EEG segments, which are 800, 384, and 2000 for datasets I, II, and III, respectively. This suggests that the importance of deeper IP-Units increases with the length of the input EEG segment. Additionally, removing the last IP-Unit also led to significant reductions in both ACC and macro-F1 on datasets I and II, underscoring that all IP-Units collectively contribute to performance enhancements.

- D. Effect of Different Types of IP-Unit

Table III illustrates the impact of different information purification methods, which are mean, standard deviation (std), and power on the performance across three datasets. For each layer’s output, Fifg ∈ Rk×0.5∗l

i t, we will calculate the mean, std on the last dimension of Fifg, resulting the purified information, Ii ∈ Rk. The comparison focuses on their effects on accuracy and macro-F1 score. Notably, the ’power’ method consistently yields the highest accuracy and macro-F1 scores across all datasets, outperforming the other two methods. These findings underscore the superiority of using the ’power’ method for information purification in this context.

- E. Effect of Different Locations of The IP-Unit

The study assesses the impact of varying the placement of IP-Unit within each HCT block, focusing on three specific locations in Figure 4 : at the fused output, Fi+1; at the coarse-grained representation, Fcgi ; and at the fine-grained representation, Ffgi . The results of this evaluation are presented in Table IV. These findings reveal that applying IPUnit to the output of the FTL leads to the highest decoding performance across all three datasets. This outcome highlights the effectiveness of this particular placement for IP-Unit within the HCT block structure.

- F. The Parameters Comparison of EEG-Deformer and Other Baseline Methods.

We visualize the comparison between different methods with respect to parameters, Multiply-Accumulate Operations (MACs), and accuracy. The results are shown in Fig. 9. We only compare models that use EEG as input, as the hand-crafted features have fewer data points in each input. On dataset I, the EEG-Deformer requires fewer MACs than models of similar size, while achieving higher accuracy than smaller models. On dataset II, the EEG-Deformer has the highest performance with a relatively smaller model size and fewer MACs compared to other baselines. On dataset III, although the EEG-Deformer uses more MACs, it has a smaller model size than those requiring more MACs. Generally, our EEGDeformer achieves a promising balance between accuracy and computational efficiency.

- G. Visualization

In this study, we use saliency maps [39] to visualize the regions that the neural networks identify as most informative. Figures 5 to 7 show saliency maps for five randomly selected subjects, as well as the averaged map across all subjects, for three datasets corresponding to attention, fatigue, and mental workload classification tasks. To improve clarity, these saliency maps are normalized to a range between 0 and 1. The brain is functionally divided into frontal, temporal, parietal, and occipital regions. According to Figure 5, the areas most informative for attention classification are primarily located in the frontal (Fp1, F1, and AFF6) and parietal (CP5, P7, and P4) regions, which are known to be related to cognitive attention [40]. Figure 6 shows that for fatigue classification, the

neural network primarily focuses on the frontal (F7, F3, and FCz), temporal (T3 and T5), and parietal (P3) areas, consistent with [41]. In the case of mental workload classification, we find consistent findings with those reported in [42]: the frontal (Fz and Fp2) and parietal (P4) areas are more informative for neural networks, as shown in Figure 7. These visualizations align with known brain activity patterns related to these cognitive processes and demonstrate the neural network’s ability to identify relevant brain regions for each task. As shown in the figures, the saliency maps display generally consistent patterns for each task, indicating that our model consistently learns from task-related brain regions.

H. Limitations and future work

While the model demonstrates strong performance on the selected tasks, the evaluation does not cover all commonly used tasks in EEG-based classification. Expanding the range of tasks could provide a more comprehensive assessment of the model’s generalizability across different applications. In some datasets, the standard deviation of the model’s performance is higher compared to certain baseline methods. This suggests that, although the model performs well on average, it may exhibit greater variability across different subjects or trials, potentially affecting its reliability in certain cases. In the future, efforts should focus on improving the model’s robustness.

VI. CONCLUSION

In this paper, we introduce EEG-Deformer, a novel convolutional Transformer designed for cross-subject EEG classification tasks. The model begins with a shallow CNN encoder, followed by a series of HCT blocks. These blocks are specifically designed to capture both coarse- and finegrained temporal dynamics from EEG signals, achieved by integrating a FTL into the Transformers. To leverage multilevel temporal information effectively, the model performs information purification on the fine-grained temporal representations extracted by all HCT layers. These purified signals are then densely connected to the final embeddings. We evaluate EEG-Deformer against various baselines across three benchmark datasets. The results consistently demonstrate that EEG-Deformer outperforms these baselines, showcasing its effectiveness in EEG decoding tasks. These findings suggest that EEG-Deformer can serve as a robust and versatile backbone for a wide range of EEG decoding tasks.

REFERENCES

- [1] X. Zhang, J. Liu, J. Shen, S. Li, K. Hou, B. Hu, J. Gao, T. Zhang, and B. Hu, “Emotion recognition from multimodal physiological signals using a regularized deep fusion of kernel machine,” IEEE Transactions on Cybernetics, pp. 1–14, 2020.
- [2] F. Lotte and C. Guan, “Regularizing common spatial patterns to improve BCI designs: unified theory and new algorithms,” IEEE Transactions on biomedical Engineering, vol. 58, no. 2, pp. 355–362, 2010.
- [3] R. Foong, K. K. Ang, C. Quek, C. Guan, K. S. Phua, C. W. K. Kuah, V. A. Deshmukh, L. H. L. Yam, D. K. Rajeswaran, N. Tang et al., “Assessment of the efficacy of EEG-based MI-BCI with visual feedback and EEG correlates of mental fatigue for upper-limb stroke rehabilitation,” IEEE Transactions on Biomedical Engineering, vol. 67, no. 3, pp. 786–795, 2019.

- [4] Z. Jia, H. Liang, Y. Liu, H. Wang, and T. Jiang, “DistillSleepNet: Heterogeneous multi-level knowledge distillation via teacher assistant for sleep staging,” IEEE Transactions on Big Data, pp. 1–13, 2024.
- [5] Z. Jia, H. Wang, Y. Liu, and T. Jiang, “Mutual distillation extracting spatial-temporal knowledge for lightweight multi-channel sleep stage classification,” in Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, ser. KDD ’24. New York, NY, USA: Association for Computing Machinery, 2024, p. 1279–1289.
- [6] V. Zotev, A. Mayeli, M. Misaki, and J. Bodurka, “Emotion selfregulation training in major depressive disorder using simultaneous realtime fMRI and EEG neurofeedback,” NeuroImage: Clinical, vol. 27, p. 102331, 2020.
- [7] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, and N. Houlsby, “An image is worth 16x16 words: Transformers for image recognition at scale,” in International Conference on Learning Representations, 2021.
- [8] Y. Song, Q. Zheng, B. Liu, and X. Gao, “EEG Conformer: Convolutional transformer for EEG decoding and visualization,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 710–719, 2023.
- [9] P. Autthasan, R. Chaisaen, T. Sudhawiyangkul, P. Rangpong, S. Kiatthaveephong, N. Dilokthanakul, G. Bhakdisongkhram, H. Phan, C. Guan, and T. Wilaiprasitporn, “MIN2Net: End-to-end multi-task learning for subject-independent motor imagery EEG classification,” IEEE Transactions on Biomedical Engineering, vol. 69, no. 6, pp. 2105– 2118, 2022.
- [10] T. Song, W. Zheng, P. Song, and Z. Cui, “EEG emotion recognition using dynamical graph convolutional neural networks,” IEEE Transactions on Affective Computing, vol. 11, no. 3, pp. 532–541, 2020.
- [11] V. Delvigne, H. Wannous, T. Dutoit, L. Ris, and J.-P. Vandeborre, “PhyDAA: Physiological dataset assessing attention,” IEEE Transactions on Circuits and Systems for Video Technology, vol. 32, no. 5, pp. 2612– 2623, 2022.
- [12] Y. Ding and C. Guan, “GIGN: Learning graph-in-graph representations of EEG signals for continuous emotion recognition,” in 2023 45th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), 2023, pp. 1–5.
- [13] Y. Ding, S. Zhang, C. Tang, and C. Guan, “MASA-TCN: Multi-anchor space-aware temporal convolutional neural networks for continuous and discrete EEG emotion recognition,” IEEE Journal of Biomedical and Health Informatics, pp. 1–12, 2024.
- [14] Z. Jia, Y. Lin, X. Cai, H. Chen, H. Gou, and J. Wang, “SST-EmotionNet: Spatial-spectral-temporal based attention 3D dense network for EEG emotion recognition,” in Proceedings of the 28th ACM International Conference on Multimedia, ser. MM ’20. New York, NY, USA: Association for Computing Machinery, 2020, p. 2909–2917.
- [15] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for EEG decoding and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [16] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, Jul 2018.
- [17] Y. Ding, N. Robinson, S. Zhang, Q. Zeng, and C. Guan, “TSception: Capturing temporal dynamics and spatial asymmetry from EEG for emotion recognition,” IEEE Transactions on Affective Computing, vol. 14, no. 3, pp. 2238–2250, 2023.
- [18] Y. Ding, N. Robinson, C. Tong, Q. Zeng, and C. Guan, “LGGNet: Learning from local-global-graph representations for brain–computer interface,” IEEE Transactions on Neural Networks and Learning Systems, pp. 1–14, 2023.
- [19] Z. Jia, Y. Lin, J. Wang, Z. Feng, X. Xie, and C. Chen, “HetEmotionNet: Two-stream heterogeneous graph recurrent neural network for multimodal emotion recognition,” in Proceedings of the 29th ACM International Conference on Multimedia, ser. MM ’21. New York, NY, USA: Association for Computing Machinery, 2021, p. 1047–1056.
- [20] J. Xie, J. Zhang, J. Sun, Z. Ma, L. Qin, G. Li, H. Zhou, and Y. Zhan, “A transformer-based approach combining deep learning network and spatial-temporal information for raw EEG classification,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 2126–2136, 2022.
- [21] J. Chen, Y. Zhang, Y. Pan, P. Xu, and C. Guan, “A transformer-based deep neural network model for SSVEP classification,” Neural Networks, vol. 164, pp. 521–534, 2023.

- [22] Y.-E. Lee and S.-H. Lee, “EEG-Transformer: Self-attention from transformer architecture for decoding EEG of imagined speech,” in 2022 10th International Winter Conference on Brain-Computer Interface (BCI), 2022, pp. 1–4.
- [23] A. Sikka, H. Jamalabadi, M. Krylova, S. Alizadeh, J. N. van der Meer, L. Danyeli, M. Deliano, P. Vicheva, T. Hahn, T. Koenig, D. R. Bathula, and M. Walter, “Investigating the temporal dynamics of electroencephalogram (EEG) microstates using recurrent neural networks,” Human Brain Mapping, vol. 41, no. 9, pp. 2334–2346, 2020.
- [24] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, “Densely connected convolutional networks,” in 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 2261–2269.
- [25] P. L. Nunez and R. Srinivasan, Electric fields of the brain: the neurophysics of EEG. Oxford University Press, USA, 2006.
- [26] X. Wang, Y. Wang, W. Qi, D. Kong, and W. Wang, “BrainGridNet: A two-branch depthwise CNN for decoding EEG-based multi-class motor imagery,” Neural Networks, vol. 170, pp. 312–324, 2024.
- [27] C. Cheng, W. Liu, L. Feng, and Z. Jia, “Emotion recognition using hierarchical spatial–temporal learning transformer from regional to global brain,” Neural Networks, vol. 179, p. 106624, 2024.
- [28] Y. Xu, Y. Du, L. Li, H. Lai, J. Zou, T. Zhou, L. Xiao, L. Liu, and P. Ma, “AMDET: Attention based multiple dimensions EEG transformer for emotion recognition,” IEEE Transactions on Affective Computing, vol. 15, no. 3, pp. 1067–1077, 2024.
- [29] R. Mane, N. Robinson, A. P. Vinod, S.-W. Lee, and C. Guan, “A multiview CNN with novel variance layer for motor imagery brain computer interface,” in 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), 2020, pp. 2950– 2953.
- [30] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. u. Kaiser, and I. Polosukhin, “Attention is all you need,” in Advances in Neural Information Processing Systems, vol. 30, 2017.
- [31] T.-P. Jung, S. Makeig, M. Stensmo, and T. Sejnowski, “Estimating alertness from the EEG power spectrum,” IEEE Transactions on Biomedical Engineering, vol. 44, no. 1, pp. 60–69, 1997.
- [32] J. Shin, A. von L¨uhmann, D.-W. Kim, J. Mehnert, H.-J. Hwang, and K.R. M¨uller, “Simultaneous acquisition of EEG and NIRS during cognitive tasks for an open access dataset,” Scientific Data, vol. 5, no. 1, p. 180003, 2018.
- [33] Z. Cao, C.-H. Chuang, J.-K. King, and C.-T. Lin, “Multi-channel EEG recordings during a sustained-attention driving task,” Scientific data, vol. 6, no. 1, pp. 1–8, 2019.
- [34] I. Zyma, S. Tukaev, I. Seleznov, K. Kiyono, A. Popov, M. Chernykh, and O. Shpenkov, “Electroencephalograms during mental arithmetic task performance,” Data, vol. 4, no. 1, 2019.
- [35] A. Gramfort, M. Luessi, E. Larson, D. A. Engemann, D. Strohmeier, C. Brodbeck, L. Parkkonen, and M. S. H¨am¨al¨ainen, “MNE software for processing MEG and EEG data,” NeuroImage, vol. 86, pp. 446–460, 2014.
- [36] A. Delorme and S. Makeig, “EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis,” Journal of Neuroscience Methods, vol. 134, no. 1, pp. 9–21, 2004.
- [37] Y.-E. Lee and S.-H. Lee, “EEG-transformer: Self-attention from transformer architecture for decoding EEG of imagined speech,” in 2022 10th International winter conference on brain-computer interface (BCI). IEEE, 2022, pp. 1–4.
- [38] S. H. Tompson, E. B. Falk, J. M. Vettel, and D. S. Bassett, “Network approaches to understand individual differences in brain connectivity: opportunities for personality neuroscience,” Personality neuroscience, vol. 1, p. e5, 2018.
- [39] K. Simonyan, A. Vedaldi, and A. Zisserman, “Deep inside convolutional networks: Visualising image classification models and saliency maps,” arXiv preprint arXiv:1312.6034, 2013.
- [40] Y. Liu, J. Bengson, H. Huang, G. R. Mangun, and M. Ding, “Top-down Modulation of Neural Activity in Anticipatory Visual Attention: Control Mechanisms Revealed by Simultaneous EEG-fMRI,” Cerebral Cortex, vol. 26, no. 2, pp. 517–529, 09 2014.
- [41] P. Flor-Henry, J. C. Lind, and Z. J. Koles, “EEG source analysis of chronic fatigue syndrome,” Psychiatry Research: Neuroimaging, vol. 181, no. 2, pp. 155–164, 2010.
- [42] I. Kakkos, G. N. Dimitrakopoulos, Y. Sun, J. Yuan, G. K. Matsopoulos, A. Bezerianos, and Y. Sun, “EEG fingerprints of task-independent mental workload discrimination,” IEEE Journal of Biomedical and Health Informatics, vol. 25, no. 10, pp. 3824–3833, 2021.

