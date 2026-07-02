CSP-Net: Common Spatial Pattern Empowered Neural Networks for EEG-Based Motor Imagery Classiﬁcation

Xue Jianga,b, Lubin Menga,b, Xinru Chena,b, Yifan Xua,b, Dongrui Wua,b,∗

aKey Laboratory of the Ministry of Education for Image Processing and Intelligent Control, School of Artiﬁcial Intelligence and Automation, Huazhong University of Science and Technology, Wuhan 430074, China bShenzhen Huazhong University of Science and Technology Research Institute, Shenzhen 518063, China

[Figure 1]

Abstract

arXiv:2411.11879v1[eess.SP]4Nov2024

Electroencephalogram-basedmotor imagery (MI) classiﬁcation is an importantparadigm of non-invasivebrain-computerinterfaces. Common spatial pattern (CSP), which exploits different energy distributions on the scalp while performing different MI tasks, is very popular in MI classiﬁcation. Convolutional neural networks (CNNs) have also achieved great success, due to their powerful learning capabilities. This paper proposes two CSP-empowered neural networks (CSP-Nets), which integrate knowledge-driven CSP ﬁlters with data-driven CNNs to enhance the performance in MI classiﬁcation. CSP-Net-1 directly adds a CSP layer before a CNN to improve the input discriminability. CSP-Net-2 replaces a convolutional layer in CNN with a CSP layer. The CSP layer parameters in both CSP-Nets are initialized with CSP ﬁlters designed from the training data. During training, they can either be kept ﬁxed or optimized using gradient descent. Experiments on four public MI datasets demonstrated that the two CSP-Nets consistently improved over their CNN backbones, in both within-subject and cross-subject classiﬁcations. They are particularly useful when the number of training samples is very small. Our work demonstrates the advantage of integrating knowledge-driven traditional machine learning with data-driven deep learning in EEG-based brain-computer interfaces.

Keywords: Brain-computer interfaces, electroencephalogram, motor imagery, common spatial pattern, convolutional neural network

[Figure 2]

- 1. Introduction

Many algorithms have been proposed for EEG-based MI classiﬁcation. Common spatial pattern (CSP) [10, 11] is one of the most widely used and effective approaches, which converts the raw multi-channel EEG signals into more discriminative spatial patterns. It was initially proposed for binary classiﬁcation, by designing spatial ﬁlters that maximize the variance ratio of the ﬁltered signals of different classes [10]. Dornhege et al. [12] extended it to multi-class classiﬁcation using a oneversus-the-rest strategy. Ang et al. [13] proposed ﬁlter bank CSP (FBCSP), which bandpass ﬁlters EEG signals into multiple frequency bands, extracts CSP features from each band, and then selects the most useful features for classiﬁcation. Lotte et al. [14] introduced regularized CSP to enhance the robustness of CSP.

A brain-computer interface (BCI) establishes a direct communication pathway that enables the human brain to interact with external devices [1]. Electroencephalogram (EEG), which records the electrical activities on the scalp of the brain, is the most widely used input signal in non-invasive BCIs due to its affordability and convenience [2]. EEG-based BCIs have been used in controlling robots [3], decoding speech [4], enhancing computer gaming experience [5], and so on.

Motor imagery (MI) [6] is a classical paradigm of EEGbased BCIs, where a subject imagines the movement of a body part, e.g., right hand, left hand, right foot, left foot, both feet, and/or tongue, without actually executing it. An MI induces changes in the sensory-motor rhythms (SMR) of corresponding areas of the cerebral cortex, which primarily involve modulations of the µ rhythm (8-12Hz) and the β rhythm (14-30Hz) [7]. Speciﬁcally, when an MI starts, these rhythmic activities decrease, resulting in event-related desynchronization (ERD); at the end of an MI, these rhythmic activities increase, resulting in event-related synchronization (ERS) [8, 9]. Therefore, the detection of SMR patterns within speciﬁc areas of the cerebral cortex can be used to identify which body part the subject is imagining moving.

Recent years have witnessed signiﬁcant increase in using deep learning for EEG signal decoding [15], which integrates feature extraction and classiﬁcation into a single end-to-end network. Among various deep architectures, convolutionalneural networks (CNNs) are the most prevalent for MI classiﬁcation [16, 17]. For example, Schirrmeister et al. [18] proposed ShallowCNN and DeepCNN for raw EEG classiﬁcation. ShallowCNN is inspired by FBCSP and includes components such as temporal convolution, spatial convolution, log-variance calculation and a classiﬁer, each correspondingto a speciﬁc step in FBCSP. DeepCNN is similar but includes more convolutional and pooling layers. Lawhern et al. [19] introduced a compact EEGNet, which has demonstrated promising performance

[Figure 3]

∗Emails: xuejiang@hust.edu.cn (Xue Jiang), lubinmeng@hust.edu.cn (Lubin Meng), xrchen@hust.edu.cn (Xinru Chen), yfxu@hust.edu.cn (Yifan Xu), drwu@hust.edu.cn (Dongrui Wu). Dongrui Wu is the corresponding author.

Preprint submitted to Elsevier November 20, 2024

across various BCI tasks, including MI classiﬁcation. Inspired also by FBCSP, EEGNet uses a two-step sequence of temporal convolution followed by depthwise convolution. Recently, FBCNet [20] extends the FBCSP approach by utilizing a hierarchical architecture that enhances feature extraction through multi-dimensional ﬁltering, allowing it to capture richer spatial and temporal patterns in EEG data. EEGConformer [21] adopts a transformer-like architecture, combining self-attention mechanisms with convolutional layers, which enables the model to learn long-range dependencies in EEG signals effectively.

Though these data-driven deep models have achieved promising performance in MI classiﬁcation, they usually require a large amount of labeled training data, which may not be always available in practice. This highlights the need to incorporate prior knowledge into EEG networks, as it can help reduce the reliance on extensive labeled datasets. By integrating prior knowledge, models can leverage existing insights about EEG signal characteristics, enhancing their generalization capabilities and performance even in data-scarce environments. This paper proposes CSP empowered neural networks (CSPNet), which more effectively integrate CSP and CNNs. More speciﬁcally, we propose two CSP-Nets, by embedding CSP into different layers of the CNN models. The ﬁrst, CSP-Net-1, places a CSP layer before a CNN to ﬁlter the EEG signals for enhancing their discriminability. The second, CSP-Net-2, replaces a CNN’s convolutional layer with a CSP layer to provide task-speciﬁc prior knowledge initialization. The parameters in the CSP layer of both CSP-Nets are initialized from CSP ﬁlters designed on the training data. They can be ﬁxed or optimized by gradient descent during training. In summary, CSP-Nets integrate the strengths of traditional CSP feature extraction with deep learning by embedding CSP layers in CNN architectures. This approach enhances the model’s ability to capture relevant features from EEG signals, making it a more effective solution for MI classiﬁcation. Our main contributions are:

- • Integration of CSP and CNNs: We propose a novel framework that combines CSP with CNNs for MI classiﬁcation, enhancing EEG feature extraction and improving classiﬁcation performance.
- • Two CSP-Net Variants: We introduce two architectures, CSP-Net-1, which incorporates a CSP layer before the CNN, and CSP-Net-2, which replaces a convolutional layer with a CSP layer for task-speciﬁc prior knowledge initialization. Both variants allow CSP layer parameters to be ﬁxed or further optimized.
- • Performance on Multiple EEG Datasets: CSP-Nets demonstrate strong performance across various scenarios, including within-subject and cross-subject classiﬁcations, as well as in small sample settings. The models demonstrate generalization across different backbone architectures, validated on four public MI datasets.

The rest of this paper is structured as follows. Section 2 introduces the classical CSP and proposes two CSP-Nets. Section 3 presents the experimental settings and experimental results. Finally, Section 4 draws conclusions.

2. Methods

This section introduces the CSP algorithm, ﬁve CNN models for MI classiﬁcation, and our proposed two CSP-Nets to integrate CSP and CNNs.

2.1. CSP

CSP was ﬁrst proposed by Koles et al. [22] to extract discriminative features from EEG signals of two human populations. Mu¨eller-Gerking et al. [23] later extended it to MI classiﬁcation. Since then, it has become one of the most popular and effective algorithms in MI-based BCIs [10, 11].

Fig. 1 shows t-SNE visualization of some real EEG trials before and after CSP ﬁltering from Subject 3 of Dataset 2a in BCI Competition IV [24]. Clearly, after CSP ﬁltering, samples from different classes become more distinguishable.

[Figure 4]

[Figure 5]

(a) (b)

Figure 1: t-SNE visualization of (a) the raw EEG trials; and, (b) the CSPﬁltered trials. Different shapes (colors) represent different classes.

For binary classiﬁcation, CSP aims to learn spatial ﬁlters that maximize the variance of EEG signals from one class while simultaneously minimizing the variance from the other class. Let Xi ∈ Rc×t be an EEG trial of MI task i, where i ∈ {1, 2} is the class index, c the number of channels, and t the number of time domain samples. CSP generates a spatial ﬁltering matrix W ∈ Rc×f (f < c) that projects the original EEG trials into a lower-dimensional space with higher discriminability. W is obtained by maximizing (or minimizing):

- W⊤X¯1X¯1⊤W

[Figure 6]

- W⊤X¯2X¯2⊤W

J(W) =

- W⊤C¯1W

[Figure 7]

- W⊤C¯2W

, (1)

=

where X¯i ∈ Rc×t is the averaged EEG trial from class i, and C¯i ∈ Rc×c the mean spatial covariance matrix of all EEG trials in class i.

Since J(W) = J(kW) for any arbitrary real constant k, maximizing J(W) is equivalent to maximizing W⊤C¯1W, subject to the constraint W⊤C¯2W = If. This optimization problem can be solved using the Lagrange multiplier method [14], whose Lagrange function is

F(W, λ) = W⊤C¯1W − λ(W⊤C¯2W − If). (2) Setting the derivative of F(W, λ) with respect to W to 0, we

have

∂F(W, λ) ∂W

= 2W⊤C¯1 − 2λW⊤C¯2 = 0 ⇔ C¯1W = λC¯2W ⇔ C¯2−1C¯1W = λW,

[Figure 8]

which becomes a standard eigenvalue decomposition problem. The spatial ﬁltering matrix W consists of eigenvectors cor-

responding to the 2f largest and the 2f smallest eigenvalues of C¯2−1C¯1.

[Figure 9]

[Figure 10]

- 2.2. CNNs for MI Classiﬁcation Five popular CNN models are considered in this paper: EEG-

- Net [19], DeepCNN [18], ShallowCNN [18], FBCNet [20], and EEGConformer [21]. Their architectures are detailed in Tables 1-5, respectively.

- • EEGNet [19], which consists of three convolutionalblocks and a classiﬁer block. The ﬁrst convolutional block performs temporal ﬁltering for capturing frequency information. The second spatial ﬁlter block uses depthwise convolution with size (c, 1) to learn spatial ﬁlters. The third separable convolutional block is used to reduce the number of parameters and decouple the relationships within and across feature maps.
- • DeepCNN [18], compared with EEGNet, it is deeper and hence has much more parameters. It mainly includes a temporal convolutional block, a spatial ﬁlter block, two standard convolutional blocks and a classiﬁer block. The ﬁrst temporal and spatial convolutional blocks are specially designed to handle EEG inputs and the other two are standard ones.
- • ShallowCNN [18], which is a shallow version of DeepCNN, inspired by FBCSP. Its ﬁrst two blocks are similar to the temporal and spatial convolutional blocks of DeepCNN, but with a larger kernel, a different activation function, and a different pooling approach.
- • FBCNet [20], which is a simple yet effective CNN architecture. It begins by applying multiple ﬁxed-parameter band-pass ﬁlters to decompose the EEG into various frequency bands as multi-view inputs. Spatial ﬁlter block is then used to extract spatially discriminative patterns from each frequency band. Finally, a classiﬁer block is designed for classiﬁcation.
- • EEGConformer [21], which is a compact convolutional transformer model. The convolution module also includes a temporal convolutional block and a spatial ﬁlter block for learning the low-level local features. The multiple selfattention modules are used to extract the global correlation within the local features.

Table 1: EEGNet [19]. Block Layer Filter size

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

Number of ﬁlters Temporal Conv2D (1, f2s ) 4

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

convolution Batch normalization - -

[Figure 24]

DepthwiseConv2D (c, 1) 8 Depthwise Batch normalization - -

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

spatial ﬁlter ELU activation - Average pooling (1, 4) Dropout - -

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

SeparableConv2D (1, 16) 8 Batch normalization - -

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

Separable PointwiseCon2D (1, 1) 8 convolution Batch normalization - -

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

ELU activation - Average pooling (1, 8) -

[Figure 51]

[Figure 52]

[Figure 53]

Dropout - Classiﬁer Fully connection - -

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

Table 2: DeepCNN [18]. Block Layer Filter size

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

Number of ﬁlters convolutionTemporal Conv2D (1, 5) 25

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

Conv2D (c, 1) 25 Batch normalization - -

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

Spatial ﬁlter

[Figure 81]

[Figure 82]

[Figure 83]

ELU activation - -

Max pooling (1, 2) Dropout - Conv2D (1, 5) 50

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

Standard Batch normalization - convolution ELU activation - -

[Figure 96]

[Figure 97]

Max pooling (1, 2) Dropout - Conv2D (1, 5) 100

[Figure 98]

[Figure 99]

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

Standard Batch normalization - convolution ELU activation - -

[Figure 110]

[Figure 111]

Max pooling (1, 2) -

[Figure 112]

[Figure 113]

[Figure 114]

Dropout - Classiﬁer Fully connection - -

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

Table 3: ShallowCNN [18]. Block Layer Filter size

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

Number of ﬁlters Temporal

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

convolution Conv2D (1, 13) 40

[Figure 134]

[Figure 135]

[Figure 136]

Conv2D (c, 1) 40

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

Batch Normalization - Squaring Activation - -

Spatial ﬁlter

[Figure 143]

[Figure 144]

[Figure 145]

Average Pooling (1, 35) Logarithmic Activation - -

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

Dropout - Classiﬁer Fully Connection - -

[Figure 151]

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

Table 4: FBCNet [20]. Block Layer Filter size

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

Number of ﬁlters Band-pass

[Figure 163]

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

ﬁlter - - 6

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

DepthwiseConv2D (c, 1) 48 Spatial Batch normalization - -

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

ﬁlter Swish activation - -

[Figure 181]

[Figure 182]

[Figure 183]

Variance layer - Classiﬁer Fully connection - -

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

[Figure 188]

Figure 2: Our proposed CSP-Nets. (a) Traditional CSP ﬁlters are used to initialize the CSP layer in CSP-Nets. (b) CSP-Net-1, which directly adds a CSP layer before a CNN backbone. (c) CSP-Net-2, illustrated using EEGNet [19] (Table 1 in Supplementary Materials); the DepthwiseConv2D layer in its depthwise spatial ﬁlter block is replaced by a CSP layer.

Table 5: EEGConformer [21]. Block Layer Filter size

[Figure 189]

[Figure 190]

[Figure 191]

[Figure 192]

Number of ﬁlters Temporal

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

convolution Conv2D (1, 25) 40

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

Conv2D (c, 1) 40 Batch normalization - -

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

ELU activation - Spatial ﬁlter Average pooling (1, 75) -

[Figure 212]

[Figure 213]

[Figure 214]

Dropout - PointwiseConv2D (1, 1) 40

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

[Figure 219]

[Figure 220]

Rearrange - Layer normalization - -

[Figure 221]

[Figure 222]

[Figure 223]

[Figure 224]

[Figure 225]

[Figure 226]

MHA - Dropout - -

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

6× Residual add - Self-attention Layer normalization - -

[Figure 236]

FFN - Dropout - -

[Figure 237]

[Figure 238]

[Figure 239]

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

Residual add - -

[Figure 246]

- 2.3. CSP-Net-1

Our proposed CSP-Net-1 simply performs CSP before a CNN.

As illustrated in Fig. 2(a), all training EEG samples are used in CSP, resulting in f spatial ﬁlters Wi ∈ Rc×1, i = 1, . . ., f. Then, as shown in Fig. 2(b), CSP-Net-1 uses these ﬁlters to spatially ﬁlter the raw EEG signals, before passing them to a CNN backbone.

There could be two different training approaches: 1) Fix the CSP layer and train the CNN backbone only (CSP-Net-1-ﬁx); and, 2) update the CSP layer and the CNN backbone simultaneously (CSP-Net-1-upd). Their effectivenesswill be discussed in Section 3.3.

CSP-Net-1 applies CSP ﬁltering as a pre-processing step, enabling the model to work with more discriminative input signals. This explicit inclusion of the CSP ﬁlter provides a more structured way to embed expert knowledge into the network, thereby improving the model’s capacity to capture task-relevant spatial features.

Algorithm 1 gives the pseudo-code of CSP-Net-1.

[Figure 247]

Algorithm 1: CSP-Net-1 for MI classiﬁcation. Input: Training data X; a CNN model.

[Figure 248]

- 1 Perform CSP on X to obtain the ﬁlter matrix W;
- 2 Initialize CSP-Net-1, which consists of a CSP layer with weights W and a randomly initialized CNN;
- 3 Train CSP-Net-1 on X;
- 4 return CSP-Net-1.

[Figure 249]

2.4. CSP-Net-2

Many CNN models have been proposed for MI classiﬁcation, which typically consist of multiple convolution-pooling layers for feature extraction and some fully connected layers for classiﬁcation. Although they differ in architecture, they usually include a spatial ﬁlter layer with spatial convolutional kernels speciﬁcally designed for EEG signals.

CSP-Net-2 replaces their spatial ﬁlter layer with a CSP layer. Fig. 2(c) uses EEGNet as the CNN backbone to illustrate the architecture of CSP-Net-2. For clarity, we primarily depict the

[Figure 250]

Algorithm 2: CSP-Net-2 for MI classiﬁcation. Input: Training data X; a CNN model.

[Figure 251]

- 1 Perform CSP on X to obtain the ﬁlter matrix W;
- 2 Randomly initialize the CNN model;
- 3 Initialize CSP-Net-2, by replacing the convolutional layer in the spatial ﬁlter block of the CNN model by a CSP layer with weights W;
- 4 Train CSP-Net-2 on X;
- 5 return CSP-Net-2.

[Figure 252]

They were downloaded and pre-processed using the MOABB framework [27]. All datasets were pre-processed with an 832Hz bandpass ﬁlter.

Table 6: Summary of the four MI datasets.

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

Datasets # Subjects # Channels # Trials per subject # Classes

[Figure 258]

[Figure 259]

[Figure 260]

[Figure 261]

[Figure 262]

MI4C 9 22 288 4 MI2C 9 22 144 2 MI14S 14 15 100 2

[Figure 263]

[Figure 264]

[Figure 265]

[Figure 266]

[Figure 267]

[Figure 268]

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

MI9S 9 13 200 2

[Figure 275]

connection of the convolutional kernel between inputs and outputs. The depthwise spatial ﬁlter block aims to learn spatial patterns in EEG data. CSP-Net-2 replaces the convolutional kernels in this block with the CSP ﬁlters, and keeps other parts unchanged.

More speciﬁcally, CSP-Net-2 uses the CSP layer to replace the DepthwiseConv2D layer in the spatial ﬁlter block of EEGNet (8 kernels), the Conv2D layer in the spatial ﬁlter block of DeepCNN (25 kernels), the Conv2D layer in the spatial ﬁlter block of ShallowCNN (40 kernels), the DepthwiseConv2D layer in the spatial ﬁlter block of FBCNet (48 kernels), and the Conv2D layer in the spatial ﬁlter block of EEGConformer (40 kernels).

Similar to CSP-Net-1, the CSP ﬁlter layer in CSP-Net-2 can either be ﬁxed (CSP-Net-2-ﬁx) or updated (CSP-Net-2-upd). Furthermore, this replacement is signiﬁcant as it allows CSPNet-2 to explicitly incorporateprior knowledgeaboutspatial ﬁltering, enhancing the model’s ability to capture discriminative features from the EEG signals. The ﬂexibility of using either ﬁxed or updated CSP ﬁlters also provides a balance between stability and adaptability during training, which we discussed in detail in Section 3.3.

Algorithm 2 gives the pseudo-code of CSP-Net-2.

3. Experiments and Results

This section presents the experimental results to validate the effectiveness of our proposed CSP-Nets.

- 3.1. Datasets

Four public MI datasets from BNCI-Horizon 1, summarized in Table 6, were used in our experiments:

- 1. MI4C and MI2C: They were from the 001-2014 dataset. The EEG signals were sampled at 250Hz. MI2C includes only left-hand and right-hand trials. MI4C includes all classes.
- 2. MI14S: This was from the 002-2014 dataset. The EEG signals were sampled at 512Hz.
- 3. MI9S: This was the 001-2015 dataset. The EEG signals were recorded at 512Hz. The last three subjects were discarded due to their poor performance [25, 26].

[Figure 276]

1http://www.bnci-horizon-2020.eu/database/data-sets

3.2. Implementation Details

We evaluated the performance of CSP-Nets in both withinsubject and cross-subject classiﬁcations:

- 1. Within-subject classiﬁcation: For each individual subject, 80% trials were used for training, and the remaining 20% for testing.
- 2. Cross-subject classiﬁcation: Leave-one-subject-out crossvalidation was performed, i.e., one subject was used as the test set and all remaining ones as the training set.

All experiments were repeated 5 times, and the average accuracies are reported.

We used Adam optimizer with batch size 128 and initial learning rate 0.01, and cross-entropy loss with weight decay 0.0005. The maximum number of training epochs was 200. The CSP layer used by default f = 8 spatial ﬁlters (Section 3.6 presents sensitivity analysis). For CSP-Net-2, the number of convolutional kernels in the original spatial ﬁlter layer of the CNN models may be larger than 8. We expanded the CSP ﬁlters to address this mismatch: when the number of convolutional kernels exceeds the number of CSP ﬁlters, we replicate the CSP ﬁlters to match the number of required kernels. Speciﬁcally, we duplicated the 8 CSP ﬁlters 5 times to match the 40 kernels in the spatial ﬁlter block of ShallowCNN and EEGConformer (8 × 5 = 40), duplicated the 8 CSP ﬁlters 6 times to match the 48 kernels in the spatial ﬁlter block of FBCNet (8 × 6 = 48), and duplicated the 8 CSP ﬁlters 3 times and randomly selected one more to match the 25 kernels in the spatial ﬁlter block of DeepCNN (8 × 3 + 1 = 25).

- 3.3. Experimental Results

Table 7 shows the classiﬁcation accuracies for the individual subjects on MI4C, where CSP-LR used logistic regression as the classiﬁer. Tables 8-10 show the average classiﬁcation results across all subjects on the other three datasets, due to page limit. We performed paired t-tests on the results, calculated p-values between the standard backbone models and the CSP-Nets, and adjusted them using Benjamini Hochberg False Discovery Rate correction. Observe that:

1. Both CSP-Nets were generally highly effective on all datasets and backbones. Embedding CSP knowledge in CNN backbones resulted in signiﬁcant performance improvements. For example, in within-subject classiﬁcation

on MI4C, CSP-Net-2-ﬁx increased the average accuracy on all subjects from 63.50% to 71.91% after integrating CSP information into EEGNet as CSP-Net-2-ﬁx. The average accuracies across all ﬁve backbones also exhibited signiﬁcant improvements, from an initial accuracy of 61.32% to as high as 67.33%.

- 2. CSP-Nets with ﬁxed CSP layer parameters generally performed better. Particularly, CSP-Net-2-ﬁx achieved substantial improvements over EEGNet, DeepCNN, and EEGConformer. This validated that the incorporation of CSP prior knowledge can enhance the generalization of CNN models. High number and proportion of parameters of spatial convolutional kernels in ShallowCNN and FBCNet may overshadow the beneﬁts offered by CSP ﬁlters.
- 3. CSP-Nets had larger performance improvements in within-subject classiﬁcation than cross-subject classiﬁcation. This might be because: 1) within-subject classiﬁcation had much fewer training samples than cross-subject classiﬁcation, and hence prior knowledge in CSP is more helpful to the generalization performance; and, 2) crosssubject classiﬁcation is intrinsically more challenging, as there are large individual differences among different subjects. The impact of training data quantity on CSP-Nets is discussed in Section 3.5.
- 4. CSP-Nets achieved better performance on most subjects. However, for some subjects where CSP did not perform well, CSP-Nets also struggled, e.g., Subject 1, 2, 5 and 6 in cross-subject classiﬁcation on MI4C.

- 3.4. Comparative Performance Analysis

We further compared our approaches with nine other approaches, including the state-of-the-art traditional approaches and deep learning approaches: CSP [10], FBCSP [13], MDRM [28], DeepCNN [18], LMDA-Net [29], ShallowCNN [18], EEGConformer [21], EEGNet [19], and FBCNet [20]. Table 11 presents the classiﬁcation accuraciesof CSPNet-1 and CSP-Net-2 compared to these baselines. In CSP-Net1 and CSP-Net-2, the EEGNet was used as the backbone architecture, and the ﬁxed CSP layer was applied. The same training and test data were used for all models.

Both CSP-Net-1 and CSP-Net-2 demonstrated superior performance compared to traditional approaches like CSP and FBCSP, as well as more recent models like FBCNet and EEGConformer. These results highlight their effectiveness for EEG signal classiﬁcation tasks.

- 3.5. Small Sample Setting

Deep CNN models may easily overﬁt when the training dataset is small. Figs. 3-6 show the accuracy improvements compared with the backboneat differenttraining data ratios (the number of training samples used to train the model divided by the total number training samples) on the four datasets, respectively.

Observe that:

- 1. Consistent with previous ﬁndings, CSP-Net-ﬁx generally outperformed CSP-Net-upd, with CSP-Net-2-ﬁx particularly competitive on EEGNet and DeepCNN. For example, in within-subject classiﬁcation, CSP-Net-2-ﬁx achieved a remarkable accuracy improvement of more than 20% over the DeepCNN backbone, when trained with only 50% of the training data on MI4C.
- 2. Overall, the performance improvementsof CSP-Nets were more obvious when the training data size was small. This may be because the embedding of prior knowledge greatly reduces the overﬁtting issue of CNN backbones in small sample scenarios.
- 3.6. Inﬂuence of the Number of CSP Filters

We further investigated the inﬂuence of the number of CSP ﬁlters (f) on the performance of CSP-Nets with three backbones on MI4C. The dataset includes 22-channel EEG signals, so we considered f ∈ {4, 8, 12, 16, 22}. Fig. 7 shows the corresponding accuracies of the two CSP-Nets (ﬁxed CSP layer). As the number of ﬁlters increased, the accuracy ﬁrst increased and then decreases, which is intuitive. Generally, f = 8 seems to be a good choice to balance the performance and computational cost.

- 3.7. Ablation Studies

An ablation study was performed to verify that the performance improvement of CSP-Net-1 was not due to an increase in the number of network parameters.

Speciﬁcally, we trained CSP-Net-1-rad, which replaced the CSP layer of CSP-Net-1 with a randomly initialized layer of the same size. The results on the four MI datasets in within-subject classiﬁcation are shown in Table 12. Generally, CSP-Net-1rad performed similarly to the standard backbone, suggesting that the performance improvement of CSP-Net-1 was due to its incorporation of knowledge from CSP, instead of more parameters.

- 3.8. Training Process Visualization

Fig. 8 shows the average cross-subject training and test accuracy curves of CSP-Nets (ﬁxed CSP layer) and their corresponding backbones (EEGNet) on the four datasets. For all the backbones, there was a large gap between the training and test curves, indicating overﬁtting. Our proposed CSP-Nets effectively leveraged the knowledge from the CSP ﬁlters for better initialization, reducing the gap and achieving better test performance.

- 3.9. Visualization of the CSP Filters

We further visualized the spatial convolutional kernel weights from the CSP-Net-2 and the counterparts from standard backbone. In Fig. 9, we present the eight spatial ﬁlters in the EEGNet model and the CSP ﬁlters in the CSP-Net-2-ﬁx model for within-subject classiﬁcation on Subject 1 of MI2C (binary classiﬁcation on the left hand and right hand). We can observe that the CSP ﬁlters in CSP-Net-2-ﬁx exhibited a more focused and obvious left-right distribution concentrated on a

- Table 7: Classiﬁcation accuracies (%) on MI4C. Average accuracies higher than Standard are marked in bold. Asterisks indicate statistically signiﬁcant differences between standard backbone and CSP-Net under adjusted paired t-test, where * means p < 0.05, ** means p < 0.01, *** means p < 0.001.

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

Scenario Backbone Approach S1 S2 S3 S4 S5 S6 S7 S8 S9 Average acc±std

[Figure 282]

[Figure 283]

[Figure 284]

[Figure 285]

- CSP-LR 71.85 61.27 78.64 48.52 35.32 40.14 69.07 75.00 70.37 61.13

[Figure 286]

[Figure 287]

[Figure 288]

[Figure 289]

[Figure 290]

Standard 72.59 49.35 81.36 44.51 49.31 39.29 65.98 84.19 84.93 63.50

[Figure 291]

[Figure 292]

- CSP-Net-1-upd 83.40 57.31 88.26 50.36 58.36 43.90 75.52 84.01 87.59 69.86***±1.54

[Figure 293]

[Figure 294]

[Figure 295]

[Figure 296]

- CSP-Net-1-ﬁx 81.43 58.73 90.70 53.48 53.73 45.74 82.42 83.95 86.88 70.79***±1.68

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

- CSP-Net-2-upd 77.83 56.85 86.91 47.95 46.24 41.35 74.20 80.74 84.11 66.24±2.89

[Figure 301]

[Figure 302]

[Figure 303]

[Figure 304]

- CSP-Net-2-ﬁx 81.18 63.55 92.36 52.69 56.75 46.27 83.02 82.64 88.76 71.91***±0.74

EEGNet

[Figure 305]

[Figure 306]

[Figure 307]

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

Standard 56.86 45.93 66.55 39.72 25.48 30.14 57.34 68.66 72.93 51.51±1.13

[Figure 312]

[Figure 313]

- CSP-Net-1-upd 69.07 57.07 80.32 50.76 38.34 37.82 68.72 73.76 78.98 61.65***±1.70

[Figure 314]

[Figure 315]

[Figure 316]

[Figure 317]

- CSP-Net-1-ﬁx 70.12 56.24 81.90 52.06 46.05 38.28 69.04 72.94 82.85 63.28***±1.26

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

- CSP-Net-2-upd 62.52 41.36 59.02 43.28 25.64 25.00 54.47 70.01 71.74 50.34±0.95

[Figure 322]

[Figure 323]

[Figure 324]

[Figure 325]

- CSP-Net-2-ﬁx 73.07 55.34 82.59 51.55 45.90 38.18 74.78 76.61 81.52 64.39***±2.46

DeepCNN

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

Standard 69.35 57.51 74.62 53.04 50.74 46.14 76.48 76.33 81.95 65.13±1.38 CSP-Net-1-upd 79.99 57.93 84.78 57.87 54.98 44.48 85.43 80.79 80.92 69.69***±1.58

[Figure 333]

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

- CSP-Net-1-ﬁx 80.15 59.93 86.51 58.04 52.83 44.48 85.14 83.04 83.64 70.42***±1.41

[Figure 339]

[Figure 340]

[Figure 341]

[Figure 342]

- CSP-Net-2-upd 70.21 57.53 79.94 50.79 37.88 40.42 76.08 83.20 80.67 64.08±1.62

ShallowCNN

[Figure 343]

[Figure 344]

[Figure 345]

[Figure 346]

[Figure 347]

[Figure 348]

Within- CSP-Net-2-ﬁx 69.04 63.02 86.55 45.62 31.48 38.89 77.06 79.06 82.27 63.66±2.01 Subject

[Figure 349]

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

Standard 69.27 53.87 83.77 50.17 53.03 43.78 69.61 80.22 83.95 65.30±1.76

[Figure 354]

[Figure 355]

- CSP-Net-1-upd 77.39 53.70 86.65 52.61 60.79 45.62 78.23 86.81 84.71 69.61***±1.23

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

- CSP-Net-1-ﬁx 76.41 56.87 87.44 49.11 53.56 42.79 77.72 86.07 86.01 68.44**±2.04

[Figure 360]

[Figure 361]

[Figure 362]

[Figure 363]

- CSP-Net-2-upd 71.19 54.88 87.29 53.58 54.56 43.96 72.34 83.05 86.46 67.48*±1.85

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

- CSP-Net-2-ﬁx 76.74 57.42 86.45 46.79 53.81 43.64 71.47 82.65 85.98 67.22±1.02

FBCNet

[Figure 368]

[Figure 369]

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

Standard 75.00 46.97 79.81 50.23 37.46 46.05 72.25 77.19 65.42 61.15±1.67

[Figure 375]

[Figure 376]

- CSP-Net-1-upd 81.98 63.81 87.68 58.57 60.62 52.46 88.04 82.96 71.73 71.98***±1.38

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

- CSP-Net-1-ﬁx 84.28 59.84 87.41 61.85 58.49 53.90 90.18 79.96 71.82 71.97***±1.14

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

- CSP-Net-2-upd 80.49 58.97 89.79 60.50 56.39 55.85 84.24 85.14 75.04 71.82***±1.04

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

- CSP-Net-2-ﬁx 82.55 60.73 86.94 45.70 58.18 46.37 78.67 83.13 82.95 69.47***±1.04

EEGConformer

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

[Figure 395]

Standard 68.61 50.73 77.22 47.53 43.20 41.08 68.33 77.32 77.84 61.32±1.57

[Figure 396]

[Figure 397]

- CSP-Net-1-upd 78.37 57.96 85.54 54.03 54.62 44.86 79.19 81.67 80.79 68.56***±1.49

[Figure 398]

[Figure 399]

[Figure 400]

[Figure 401]

- CSP-Net-1-ﬁx 78.48 58.32 86.79 54.91 52.93 45.04 80.90 81.19 82.24 68.98***±1.51

[Figure 402]

[Figure 403]

[Figure 404]

[Figure 405]

- CSP-Net-2-upd 72.45 53.92 80.59 51.22 44.14 41.32 72.27 80.43 79.60 63.99***±1.67

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

- CSP-Net-2-ﬁx 76.52 60.01 86.98 48.47 49.22 42.67 77.00 80.82 84.30 67.33***±1.45

Average

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

[Figure 414]

[Figure 415]

- CSP-LR 61.46 22.92 72.22 43.06 32.29 39.58 62.50 76.04 62.85 52.55

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

[Figure 420]

Standard 68.96 30.35 71.88 38.06 37.01 36.74 42.01 58.19 61.74 49.44±1.75

[Figure 421]

[Figure 422]

- CSP-Net-1-upd 65.62 32.15 72.92 41.39 34.93 38.68 55.28 65.69 61.74 52.04*±1.48

[Figure 423]

[Figure 424]

[Figure 425]

[Figure 426]

- CSP-Net-1-ﬁx 62.50 32.43 76.32 40.97 34.58 37.43 52.01 67.64 65.62 52.17*±1.13

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

- CSP-Net-2-upd 66.94 32.64 74.17 42.01 35.07 40.97 42.78 67.08 63.82 51.72*±1.59

[Figure 431]

[Figure 432]

[Figure 433]

[Figure 434]

- CSP-Net-2-ﬁx 66.46 31.53 74.44 39.65 31.04 37.29 53.40 63.06 68.61 51.72±1.38

EEGNet

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

[Figure 440]

[Figure 441]

Standard 65.35 34.03 52.99 37.92 38.19 43.40 41.81 59.24 53.47 47.38±2.10

[Figure 442]

[Figure 443]

- CSP-Net-1-upd 61.32 33.40 67.57 41.81 35.56 40.90 43.19 63.19 57.01 49.33±0.70

[Figure 444]

[Figure 445]

[Figure 446]

[Figure 447]

- CSP-Net-1-ﬁx 60.07 34.79 62.22 42.50 35.21 40.97 41.67 67.01 60.14 49.40±0.53

[Figure 448]

[Figure 449]

[Figure 450]

[Figure 451]

- CSP-Net-2-upd 64.93 31.18 65.00 38.96 39.58 41.67 48.61 56.94 57.15 49.34±1.11

[Figure 452]

[Figure 453]

[Figure 454]

[Figure 455]

- CSP-Net-2-ﬁx 62.01 29.93 69.44 37.99 36.32 39.44 52.92 63.33 61.67 50.34*±1.81

DeepCNN

[Figure 456]

[Figure 457]

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

Standard 68.12 33.40 71.04 41.46 36.18 45.49 43.82 69.51 64.17 52.58±0.65 CSP-Net-1-upd 66.25 30.63 70.69 41.53 32.15 40.49 50.00 64.65 59.03 50.60±1.23

[Figure 463]

[Figure 464]

[Figure 465]

[Figure 466]

[Figure 467]

[Figure 468]

- CSP-Net-1-ﬁx 68.12 31.04 72.01 42.71 32.78 39.24 53.96 69.38 61.60 52.31±1.28

[Figure 469]

[Figure 470]

[Figure 471]

[Figure 472]

- CSP-Net-2-upd 66.39 30.63 72.57 43.12 32.29 43.06 47.29 67.57 63.61 51.84±1.25

ShallowCNN

[Figure 473]

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

Cross- CSP-Net-2-ﬁx 62.15 28.47 72.08 39.58 32.36 41.67 54.93 67.64 67.64 51.84±1.04 Subject

[Figure 479]

[Figure 480]

[Figure 481]

[Figure 482]

[Figure 483]

Standard 62.92 31.39 62.22 41.67 31.25 36.25 40.76 55.21 57.01 46.52±1.49

[Figure 484]

[Figure 485]

- CSP-Net-1-upd 66.18 30.90 62.50 42.43 31.53 38.33 43.26 57.43 60.49 48.12±1.31

[Figure 486]

[Figure 487]

[Figure 488]

[Figure 489]

- CSP-Net-1-ﬁx 67.22 31.39 67.43 39.51 31.11 38.06 45.90 60.76 60.28 49.07**±1.11

[Figure 490]

[Figure 491]

[Figure 492]

[Figure 493]

- CSP-Net-2-upd 64.65 30.42 61.94 41.39 30.83 37.92 40.69 56.88 57.64 46.93±1.27

[Figure 494]

[Figure 495]

[Figure 496]

[Figure 497]

- CSP-Net-2-ﬁx 57.50 32.50 64.38 40.35 36.67 36.88 49.79 64.31 65.00 49.71**±1.24

FBCNet

[Figure 498]

[Figure 499]

[Figure 500]

[Figure 501]

[Figure 502]

[Figure 503]

[Figure 504]

Standard 52.64 27.64 49.51 33.68 32.29 39.86 30.14 54.51 41.60 40.21±1.67

[Figure 505]

[Figure 506]

- CSP-Net-1-upd 61.94 35.07 63.06 34.38 32.36 37.85 26.11 61.39 55.76 45.32***±0.90

[Figure 507]

[Figure 508]

[Figure 509]

[Figure 510]

- CSP-Net-1-ﬁx 58.54 35.83 63.33 35.35 32.64 38.19 27.78 64.03 56.18 45.76***±1.09

[Figure 511]

[Figure 512]

[Figure 513]

[Figure 514]

- CSP-Net-2-upd 55.76 33.06 71.67 38.19 33.19 35.14 44.03 61.39 63.75 48.46***±0.62

[Figure 515]

[Figure 516]

[Figure 517]

[Figure 518]

- CSP-Net-2-ﬁx 56.81 33.26 72.92 39.65 31.11 37.57 44.44 67.22 65.83 49.87***±0.94

EEGConformer

[Figure 519]

[Figure 520]

[Figure 521]

[Figure 522]

[Figure 523]

[Figure 524]

[Figure 525]

Standard 63.60 31.36 61.53 38.56 34.98 40.35 39.71 59.33 55.60 47.22±1.53

[Figure 526]

[Figure 527]

- CSP-Net-1-upd 64.26 32.43 67.35 40.31 33.31 39.25 43.57 62.47 58.81 49.08***±1.12

[Figure 528]

[Figure 529]

[Figure 530]

[Figure 531]

- CSP-Net-1-ﬁx 63.29 33.10 68.26 40.21 33.26 38.78 44.26 65.76 60.76 49.74***±1.03

[Figure 532]

[Figure 533]

[Figure 534]

[Figure 535]

- CSP-Net-2-upd 63.73 31.59 69.07 40.73 34.19 39.75 44.68 61.97 61.19 49.66***±1.17

[Figure 536]

[Figure 537]

[Figure 538]

[Figure 539]

- CSP-Net-2-ﬁx 60.99 31.14 70.65 39.44 33.50 38.57 51.10 65.11 65.75 50.69***±1.28

Average

[Figure 540]

[Figure 541]

[Figure 542]

- Table 8: Average classiﬁcation accuracies (%) on MI2C. Those higher than Standard are marked in bold. Asterisks indicate statistically signiﬁcant differences between standard backbone and CSP-Net under adjusted paired t-test, where * means p < 0.05, ** means p < 0.01, *** means p < 0.001.

[Figure 543]

Scenario Approach

[Figure 544]

[Figure 545]

Backbone

[Figure 546]

[Figure 547]

[Figure 548]

EEGNet DeepCNN ShallowCNN FBCNet EEGConformer Average acc±std CSP-LR - - - - - 75.72 Standard 76.38±2.21 61.46±3.28 76.29±2.92 78.11±2.64 75.31±1.45 73.51±2.50

[Figure 549]

[Figure 550]

[Figure 551]

[Figure 552]

[Figure 553]

[Figure 554]

Within- CSP-Net-1-upd 80.02±2.80 70.86***±3.58 82.50**±2.60 80.70*±1.85 81.06***±1.46 79.02***±2.45 subject CSP-Net-1-ﬁx 81.69*±0.49 70.37***±3.41 83.71***±1.45 82.39**±2.70 82.05***±0.88 80.04***±1.78

[Figure 555]

[Figure 556]

[Figure 557]

[Figure 558]

[Figure 559]

CSP-Net-2-upd 75.94±2.24 61.59±1.93 77.33±1.68 79.65±2.48 81.53***±2.80 75.21**±2.23

[Figure 560]

[Figure 561]

CSP-Net-2-ﬁx 79.66*±2.38 75.86***±1.11 75.34±1.81 79.54±0.58 81.18**±1.61 78.32***±1.50 CSP-LR - - - - - 72.92 Standard 71.50±0.87 73.15±1.37 74.32±1.50 69.34±1.50 65.25±1.03 70.71±1.16

[Figure 562]

[Figure 563]

[Figure 564]

[Figure 565]

[Figure 566]

[Figure 567]

[Figure 568]

Cross- CSP-Net-1-upd 73.53*±1.39 74.86*±0.73 74.65±0.63 71.00±1.60 70.94***±0.67 73.00***±1.00 subject CSP-Net-1-ﬁx 74.51**±1.28 74.75±1.36 75.51±0.65 73.09***±1.35 71.20***±0.57 73.81***±1.04

[Figure 569]

[Figure 570]

[Figure 571]

[Figure 572]

[Figure 573]

CSP-Net-2-upd 72.31±1.23 72.93±0.48 70.40±0.87 69.41±1.71 70.76***±1.37 71.16±1.13 CSP-Net-2-ﬁx 75.25***±1.28 73.38±0.91 76.11±0.80 73.61***±0.27 72.95***±0.55 74.26***±0.76

[Figure 574]

[Figure 575]

[Figure 576]

[Figure 577]

- Table 9: Average classiﬁcation accuracies (%) on MI14S. Those higher than Standard are marked in bold. Asterisks indicate statistically signiﬁcant differences between standard backbone and CSP-Net under adjusted paired t-test, where * means p < 0.05, ** means p < 0.01, *** means p < 0.001.

[Figure 578]

Scenario Approach

[Figure 579]

[Figure 580]

Backbone

[Figure 581]

[Figure 582]

[Figure 583]

EEGNet DeepCNN ShallowCNN FBCNet EEGConformer Average acc±std CSP-LR - - - - - 74.95 Standard 75.22±1.94 55.75±2.92 70.70±1.90 78.55±1.75 75.72±1.88 71.19±2.08

[Figure 584]

[Figure 585]

[Figure 586]

[Figure 587]

[Figure 588]

[Figure 589]

Within- CSP-Net-1-upd 76.69±3.23 61.03**±3.12 73.12±2.02 81.25*±1.50 81.07**±2.21 74.6***±2.42 subject CSP-Net-1-ﬁx 78.92*±1.67 61.33**±1.51 74.89*±1.84 81.17±1.98 80.96**±1.23 75.45***±1.61

[Figure 590]

[Figure 591]

[Figure 592]

[Figure 593]

[Figure 594]

CSP-Net-2-upd 76.61±2.37 56.84±1.19 73.94**±1.35 79.43±2.90 79.96*±2.32 73.36***±2.03

[Figure 595]

[Figure 596]

CSP-Net-2-ﬁx 80.01**±1.47 66.81***±2.26 77.14***±2.17 77.51±2.06 78.64±3.25 76.02***±2.25 CSP-LR - - - - - 74.21 Standard 73.37±1.09 68.51±1.26 70.80±0.48 72.91±0.91 63.10±2.41 69.74±1.23

[Figure 597]

[Figure 598]

[Figure 599]

[Figure 600]

[Figure 601]

[Figure 602]

[Figure 603]

Cross- CSP-Net-1-upd 73.19±1.34 71.94***±1.26 73.03**±0.22 73.08±0.93 73.83***±0.61 73.01***±0.76 subject CSP-Net-1-ﬁx 76.60***±0.62 71.56***±0.55 73.87***±0.30 73.91±0.55 73.71***±0.47 73.93***±0.49

[Figure 604]

[Figure 605]

[Figure 606]

[Figure 607]

[Figure 608]

CSP-Net-2-upd 73.07±1.94 70.04±1.28 69.67±1.43 73.11±1.64 70.93***±1.06 71.36***±1.47 CSP-Net-2-ﬁx 75.44*±1.15 71.06***±0.31 69.83±0.97 72.64±0.70 71.21***±0.48 72.04***±0.72

[Figure 609]

[Figure 610]

[Figure 611]

[Figure 612]

- Table 10: Average classiﬁcation accuracies (%) on MI9S. Those higher than Standard are marked in bold. Asterisks indicate statistically signiﬁcant differences between standard backbone and CSP-Net under adjusted paired t-test, where * means p < 0.05, ** means p < 0.01, *** means p < 0.001.

[Figure 613]

[Figure 614]

[Figure 615]

Backbone

[Figure 616]

Scenario Approach

[Figure 617]

[Figure 618]

EEGNet DeepCNN ShallowCNN FBCNet EEGConformer Average acc±std CSP-LR - - - - - 67.84 Standard 70.85±0.88 62.34±3.39 69.03±1.51 72.55±1.49 69.65±1.08 68.88±1.67

[Figure 619]

[Figure 620]

[Figure 621]

[Figure 622]

[Figure 623]

[Figure 624]

[Figure 625]

[Figure 626]

Within- CSP-Net-1-upd 73.01±2.31 62.92±1.53 72.59*±0.98 73.70±1.12 74.91**±2.22 71.43***±1.63 subject CSP-Net-1-ﬁx 73.63*±1.85 63.63±1.78 73.17***±1.43 74.31±2.17 73.22*±0.79 71.59***±±1.61

[Figure 627]

[Figure 628]

[Figure 629]

[Figure 630]

CSP-Net-2-upd 72.01±3.06 62.78±3.09 71.38*±1.07 71.67±2.49 73.55*±2.07 70.28**±2.36 CSP-Net-2-ﬁx 71.83±1.98 65.57±0.96 67.19±1.68 72.41±2.57 72.79±2.76 69.96±1.99 CSP-LR - - - - - 57.72 Standard 62.40±1.26 54.99±1.15 62.26±0.79 63.84±1.35 58.92±1.74 60.48±1.26

[Figure 631]

[Figure 632]

[Figure 633]

[Figure 634]

[Figure 635]

[Figure 636]

[Figure 637]

[Figure 638]

[Figure 639]

[Figure 640]

Cross- CSP-Net-1-upd 64.77*±1.75 59.49**±2.51 61.73±0.70 63.41 ±0.69 62.73**±0.92 62.43***±1.31 subject CSP-Net-1-ﬁx 64.91*±2.28 60.07**±1.91 62.16±1.45 62.88 ±0.95 63.11**±0.59 62.63**±1.44

[Figure 641]

[Figure 642]

[Figure 643]

[Figure 644]

CSP-Net-2-upd 62.03±1.76 61.98***±0.95 63.53±1.78 63.54±1.15 59.96±0.91 62.21**±1.31 CSP-Net-2-ﬁx 64.72±0.59 59.87**±1.70 62.14±0.58 61.14±1.49 59.96±0.69 61.57±1.01

[Figure 645]

[Figure 646]

[Figure 647]

Table 11: Classiﬁcation accuracies (%) for each model, averaged over all subjects.

[Figure 648]

[Figure 649]

[Figure 650]

[Figure 651]

CSP- FBCSP-

Deep- LMDA- Shallow- EEGConLR LR CNN Net CNN former EEGNet FBCNet CSP-Net-1 CSP-Net-2

Scenario Dataset

MDRM

[Figure 652]

[Figure 653]

[Figure 654]

[Figure 655]

[Figure 656]

[Figure 657]

[Figure 658]

MI4C 61.43 66.81 64.21 51.51 56.75 65.13 61.15 63.50 65.30 71.98 71,82 MI2C 75.72 76.72 76.32 61.46 71.19 76.29 75.31 76.38 78.11 81.06 81.53

[Figure 659]

[Figure 660]

[Figure 661]

[Figure 662]

[Figure 663]

[Figure 664]

Within-subject MI14S 74.95 75.39 78.58 55.75 72.04 70.70 75.72 75.22 78.55 81.07 79.96

[Figure 665]

[Figure 666]

[Figure 667]

MI9S 67.84 69.37 67.90 62.34 69.94 69.03 69.65 70.85 72.55 74.91 73.55 Average 69.99 72.07 71.75 57.77 67.48 70.29 70.46 71.49 73.63 76.26 75.85

[Figure 668]

[Figure 669]

[Figure 670]

[Figure 671]

[Figure 672]

[Figure 673]

[Figure 674]

[Figure 675]

MI4C 52.55 49.72 51.08 47.38 48.28 52.58 40.21 49.44 46.52 52.17 51.72 MI2C 72.92 73.62 71.99 73.15 69.10 74.32 65.25 71.50 69.34 74.51 75.25

[Figure 676]

[Figure 677]

[Figure 678]

[Figure 679]

[Figure 680]

[Figure 681]

Cross-subject MI14S 74.21 76.36 71.71 68.51 67.87 70.80 63.10 73.37 72.91 76.60 75.44

[Figure 682]

[Figure 683]

[Figure 684]

MI9S 57.27 63.61 57.39 54.99 63.41 62.26 58.92 62.40 63.84 64.91 64.72 Average 64.24 65.83 63.04 61.01 62.17 64.99 56.87 64.18 63.15 67.05 66.78

[Figure 685]

[Figure 686]

[Figure 687]

[Figure 688]

[Figure 689]

[Figure 691]

(b)

- Figure 3: Accuracy improvements of CSP-Nets at different training data ratios on MI4C. (a) within-subject classiﬁcation; and, (b) cross-subject classiﬁcation.

[Figure 692]

- (a)

[Figure 693]

- (b)

- Figure 4: Accuracy improvements of CSP-Nets at different training data ratios on MI2C. (a) within-subject classiﬁcation; and, (b) cross-subject classiﬁcation.

[Figure 695]

- (b)
- Figure 5: Accuracy improvements of CSP-Nets at different training data ratios on MI14S. (a) within-subject classiﬁcation; and, (b) cross-subject classiﬁcation.

[Figure 696]

- (a)

[Figure 697]

- (b)

- Figure 6: Accuracy improvements of CSP-Nets at different training data ratios on MI9S. (a) within-subject classiﬁcation; and, (b) cross-subject classiﬁcation.

f

f

(a)

(b)

- Figure 7: Classiﬁcation accuracies of CSP-Nets using different number of CSP ﬁlters on MI4C. (a) within-subject classiﬁcation; and, (b) cross-subject classiﬁcation.

Table 12: Ablation study results of CSP-Net-1. Average accuracies higher than Standard are marked in bold.

[Figure 698]

[Figure 699]

[Figure 700]

[Figure 701]

Training data ratio (%) 10 30 50 70 100

Dataset Backbone Approach

[Figure 702]

[Figure 703]

[Figure 704]

[Figure 705]

[Figure 706]

[Figure 707]

[Figure 708]

[Figure 709]

Standard 37.67 45.60 54.29 57.61 63.50 CSP-Net-1-rad 37.60 47.19 54.37 57.62 65.60 CSP-Net-1-ﬁx 43.39 57.75 62.28 65.72 70.79

[Figure 710]

[Figure 711]

[Figure 712]

EEGNet

[Figure 713]

[Figure 714]

[Figure 715]

[Figure 716]

[Figure 717]

[Figure 718]

[Figure 719]

Standard 27.17 28.90 32.13 44.66 51.51 CSP-Net-1-rad 27.33 31.40 32.84 47.53 53.51 CSP-Net-1-ﬁx 30.97 36.95 43.56 56.09 63.28

[Figure 720]

[Figure 721]

[Figure 722]

DeepCNN

[Figure 723]

[Figure 724]

[Figure 725]

MI4C

[Figure 726]

[Figure 727]

[Figure 728]

[Figure 729]

Standard 34.98 48.69 55.42 59.01 65.13 CSP-Net-1-rad 36.78 47.59 54.16 60.68 64.69 CSP-Net-1-ﬁx 40.73 55.44 60.00 66.47 70.42

[Figure 730]

[Figure 731]

[Figure 732]

ShallowCNN

[Figure 733]

[Figure 734]

[Figure 735]

[Figure 736]

[Figure 737]

[Figure 738]

[Figure 739]

Standard 33.27 41.06 47.28 53.76 60.05 CSP-Net-1-rad 33.90 42.06 47.12 55.28 61.27 CSP-Net-1-ﬁx 38.36 50.05 55.28 62.76 68.16

[Figure 740]

[Figure 741]

[Figure 742]

Average

[Figure 743]

[Figure 744]

[Figure 745]

[Figure 746]

[Figure 747]

[Figure 748]

[Figure 749]

Standard 56.77 67.53 69.37 70.61 76.38 CSP-Net-1-rad 57.77 66.76 68.51 71.85 77.11 CSP-Net-1-ﬁx 62.12 71.73 75.29 78.45 81.69

[Figure 750]

[Figure 751]

[Figure 752]

EEGNet

[Figure 753]

[Figure 754]

[Figure 755]

[Figure 756]

[Figure 757]

[Figure 758]

[Figure 759]

Standard 51.04 50.78 51.74 55.13 61.46 CSP-Net-1-rad 51.97 52.50 54.14 56.94 62.69 CSP-Net-1-ﬁx 52.07 60.04 63.82 68.17 70.37

[Figure 760]

[Figure 761]

[Figure 762]

DeepCNN

[Figure 763]

[Figure 764]

[Figure 765]

MI2C

[Figure 766]

[Figure 767]

[Figure 768]

[Figure 769]

Standard 51.38 62.34 68.36 71.70 76.29 CSP-Net-1-rad 54.24 64.55 69.45 71.21 77.44 CSP-Net-1-ﬁx 62.42 72.12 76.69 81.37 83.71

[Figure 770]

[Figure 771]

[Figure 772]

ShallowCNN

[Figure 773]

[Figure 774]

[Figure 775]

[Figure 776]

[Figure 777]

[Figure 778]

[Figure 779]

Standard 53.06 60.22 63.16 65.81 71.38 CSP-Net-1-rad 54.66 61.27 64.03 66.67 72.41 CSP-Net-1-ﬁx 58.87 67.96 71.93 76.00 78.59

[Figure 780]

[Figure 781]

[Figure 782]

Average

[Figure 783]

[Figure 784]

[Figure 785]

[Figure 786]

[Figure 787]

[Figure 788]

[Figure 789]

Standard 59.10 66.99 72.25 73.59 75.22 CSP-Net-1-rad 57.55 68.00 71.30 71.79 74.40 CSP-Net-1-ﬁx 61.79 73.53 75.72 78.76 78.92

[Figure 790]

[Figure 791]

[Figure 792]

EEGNet

[Figure 793]

[Figure 794]

[Figure 795]

[Figure 796]

[Figure 797]

[Figure 798]

[Figure 799]

Standard 51.11 50.80 53.92 56.64 55.75 CSP-Net-1-rad 49.64 53.58 55.95 57.04 55.99 CSP-Net-1-ﬁx 49.33 53.99 55.40 56.87 61.33

[Figure 800]

[Figure 801]

[Figure 802]

DeepCNN

[Figure 803]

[Figure 804]

[Figure 805]

MI14S

[Figure 806]

[Figure 807]

[Figure 808]

[Figure 809]

Standard 53.05 57.86 62.07 65.42 70.70 CSP-Net-1-rad 53.08 57.48 61.79 66.19 71.56

[Figure 810]

[Figure 811]

[Figure 812]

ShallowCNN

[Figure 813]

[Figure 814]

- CSP-Net-1-ﬁx 54.00 66.40 71.24 72.82 74.89

[Figure 815]

[Figure 816]

[Figure 817]

Average

[Figure 818]

Standard 54.42 58.55 62.75 65.22 67.22 CSP-Net-1-rad 53.42 59.69 63.01 65.01 67.32

[Figure 819]

[Figure 820]

[Figure 821]

[Figure 822]

[Figure 823]

[Figure 824]

- CSP-Net-1-ﬁx 55.04 64.64 67.45 69.48 71.71

[Figure 825]

[Figure 826]

[Figure 827]

[Figure 828]

[Figure 829]

Standard 57.47 65.43 68.11 70.85 70.85 CSP-Net-1-rad 59.03 64.89 67.19 69.97 69.57 CSP-Net-1-ﬁx 61.64 67.39 69.93 71.41 73.63

[Figure 830]

[Figure 831]

[Figure 832]

EEGNet

[Figure 833]

[Figure 834]

[Figure 835]

[Figure 836]

[Figure 837]

[Figure 838]

[Figure 839]

Standard 52.06 52.53 54.28 59.09 62.34 CSP-Net-1-rad 51.93 53.01 54.22 56.45 61.92 CSP-Net-1-ﬁx 52.56 56.00 55.96 57.06 63.63

[Figure 840]

[Figure 841]

[Figure 842]

DeepCNN

[Figure 843]

[Figure 844]

[Figure 845]

MI9S

[Figure 846]

[Figure 847]

[Figure 848]

[Figure 849]

Standard 51.89 57.55 61.90 66.04 69.03 CSP-Net-1-rad 52.45 57.89 62.16 64.19 69.28

[Figure 850]

[Figure 851]

[Figure 852]

ShallowCNN

[Figure 853]

[Figure 854]

- CSP-Net-1-ﬁx 55.54 63.96 67.90 70.70 73.17

[Figure 855]

[Figure 856]

[Figure 857]

Average

[Figure 858]

Standard 53.81 58.50 61.43 65.33 67.41 CSP-Net-1-rad 54.47 58.60 61.19 63.54 66.92

[Figure 859]

[Figure 860]

[Figure 861]

[Figure 862]

[Figure 863]

[Figure 864]

- CSP-Net-1-ﬁx 56.58 62.45 64.60 66.39 70.14

[Figure 865]

[Figure 866]

[Figure 867]

(a)

Figure 8: The training and test curves of different models on (a) MI4C; (b) MI2C; (c) MI14S; and, (d) MI9S.

[Figure 868]

[Figure 869]

[Figure 870]

[Figure 871]

- (a)

[Figure 872]

[Figure 873]

[Figure 874]

[Figure 875]

- (b)

Figure 9: Visualization of eight (a) spatial ﬁlters in EEGNet and (b) the CSP ﬁlters in CSP-Net-2-ﬁx for the within-subject classiﬁcation on the Subject 1 of MI2C.

speciﬁc sensorimotor area, which aligned well with the spatial characteristics of MI. In contrast, the standard EEGNet struggled to learn effective spatial information due to the absence of prior knowledge provided by CSP. This alignment suggests that CSP ﬁlters effectively capture the relevant spatial patterns inherent in the EEG data, enhancing the interpretability of the model.

- 4. Conclusions

Spatial information, which can be well captured by CSP ﬁlters, is critical in EEG-based MI classiﬁcation. This paper has introduced two CSP-Nets, which integrate the knowledgedriven CSP ﬁlters with data-driven CNN models. CSP-Net-1 directly adds a CSP layer before a CNN, utilizing CSP-ﬁltered signals as input to enhance the discriminability. CSP-Net-2 replaces a convolutional layer in CNN with a CSP layer. Experiments on four public MI datasets demonstrated that the two CSP-Nets consistently improved over their CNN backbones, in both within-subject and cross-subject classiﬁcations. They are particularly useful when the number of training samples is very small. Remarkably, CSP-Net-1-ﬁx, whose CSP layer uses ﬁxed weights calculated using the traditional CSP algorithm, is the simplest yet demonstrates overall best performance.

Our work demonstrates the advantage of integrating knowledge-driven CSP ﬁlters with data-driven CNNs, or traditional machine learning with deep learning, in EEG-based BCIs.

References

- [1] B. Graimann, B. Allison, G. Pfurtscheller, Brain-Computer Interfaces: A Gentle Introduction, Springer, Berlin, Heidelberg, 2009, pp. 1–27.
- [2] L. F. Nicolas-Alonso, J. Gomez-Gil, Brain computer interfaces, a review, Sensors 12 (2) (2012) 1211–1279.
- [3] L. R. Hochberg, D. Bacher, B. Jarosiewicz, N. Y. Masse, J. D. Simeral, J. Vogel, S. Haddadin, J. Liu, S. S. Cash, P. Van Der Smagt, et al., Reach and grasp by people with tetraplegia using a neurally controlled robotic arm, Nature 485 (7398) (2012) 372–375.
- [4] G. K. Anumanchipalli, J. Chartier, E. F. Chang, Speech synthesis from neural decoding of spoken sentences, Nature 568 (7753) (2019) 493–498.
- [5] M. Krauledat, K. Grzeska, M. Sagebaum, B. Blankertz, C. Vidaurre, K.R. Mu¨ller, M. Schro¨der, Playing pinball with non-invasive BCI, Advances in Neural Information Processing Systems 21 (2008) 1641–1648.
- [6] G. Pfurtscheller, C. Neuper, Motor imagery and direct brain-computer communication, Proc. of the IEEE 89 (7) (2001) 1123–1134.
- [7] M. Jeannerod, Mental imagery in the motor context, Neuropsychologia 33 (11) (1995) 1419–1432.
- [8] G. Pfurtscheller, C. Neuper, D. Flotzinger, M. Pregenzer, EEG-based discrimination between imagination of right and left hand movement, Electroencephalography and Clinical Neurophysiology 103 (6) (1997) 642– 651.
- [9] B. Blankertz, C. Sannelli, S. Halder, E. M. Hammer, A. Ku¨bler, K.-R. Mu¨ller, G. Curio, T. Dickhaus, Neurophysiological predictor of SMRbased BCI performance, NeuroImage 51 (4) (2010) 1303–1309.
- [10] H. Ramoser, J. Muller-Gerking, G. Pfurtscheller, Optimal spatial ﬁltering of single trial EEG during imagined hand movement, IEEE Trans. on Neural Systems and Rehabilitation Engineering 8 (4) (2000) 441–446.
- [11] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, K.-r. Muller, Optimizing spatial ﬁlters for robust EEG single-trial analysis, IEEE Signal Processing Magazine 25 (1) (2008) 41–56.
- [12] G. Dornhege, B. Blankertz, G. Curio, K.-R. Muller, Boosting bit rates in noninvasive EEG single-trial classiﬁcations by feature combination and multiclass paradigms, IEEE Trans. on Biomedical Engineering 51 (6)

(2004) 993–1002.

- [13] K. K. Ang, Z. Y. Chin, H. Zhang, C. Guan, Filter bank common spatial

- pattern (FBCSP) in brain-computer interface, in: Proc. IEEE Int’l Joint Conf. on Neural Networks, Hong Kong, China, 2008, pp. 2390–2397.
- [14] F. Lotte, C. Guan, Regularizing common spatial patterns to improve BCI designs: uniﬁed theory and new algorithms, IEEE Trans. on Biomedical Engineering 58 (2) (2010) 355–362.
- [15] A. Craik, Y. He, J. L. Contreras-Vidal, Deep learning for electroencephalogram (EEG) classiﬁcation tasks: a review, Journal of Neural Engineering 16 (3) (2019) 031001.
- [16] H. Altaheri, G. Muhammad, M. Alsulaiman, S. U. Amin, G. A. Altuwaijri, W. Abdul, M. A. Bencherif, M. Faisal, Deep learning techniques for classiﬁcation of electroencephalogram (EEG) motor imagery (MI) signals: A review, Neural Computing and Applications 35 (20) (2023) 14681–14722.
- [17] A. Al-Saegh, S. A. Dawwd, J. M. Abdul-Jabbar, Deep learning for motor imagery EEG-based classiﬁcation: A review, Biomedical Signal Processing and Control 63 (2021) 102172.
- [18] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, T. Ball, Deep learning with convolutional neural networks for EEG decoding and visualization, Human Brain Mapping 38 (11) (2017) 5391–5420.
- [19] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, B. J. Lance, EEGNet: a compact convolutional neural network for EEGbased brain-computer interfaces, Journal of Neural Engineering 15 (5)

(2018) 056013.

- [20] R. Mane, E. Chew, K. Chua, K. K. Ang, N. Robinson, A. P. Vinod, S.-W. Lee, C. Guan, FBCNet: A multi-view convolutional neural network for brain-computer interface, arXiv preprint arXiv:2104.01233 (2021).
- [21] Y. Song, Q. Zheng, B. Liu, X. Gao, EEG Conformer: Convolutional transformer for EEG decoding and visualization, IEEE Trans. on Neural Systems and Rehabilitation Engineering 31 (2023) 710–719.
- [22] Z. J. Koles, M. S. Lazar, S. Z. Zhou, Spatial patterns underlying population differences in the background EEG, Brain Topography 2 (1990) 275–284.
- [23] J. Mu¨ller-Gerking, G. Pfurtscheller, H. Flyvbjerg, Designing optimal spatial ﬁlters for single-trial EEG classiﬁcation in a movement task, Clinical Neurophysiology 110 (5) (1999) 787–798.
- [24] M. Tangermann, K.-R. Mu¨ller, A. Aertsen, N. Birbaumer, C. Braun, C. Brunner, R. Leeb, C. Mehring, K. Miller, G. Mueller-Putz, G. Nolte, G. Pfurtscheller, H. Preissl, G. Schalk, A. Schlo¨gl, C. Vidaurre, S. Waldert, B. Blankertz, Review of the BCI Competition IV, Frontiers in Neuroscience 6 (2012) 55.
- [25] J. Faller, C. Vidaurre, T. Solis-Escalante, C. Neuper, R. Scherer, Autocalibration and recurrent adaptation: Towards a plug and play online ERD-BCI, IEEE Trans. on Neural Systems and Rehabilitation Engineering 20 (3) (2012) 313–319.
- [26] K. Xia, L. Deng, W. Duch, D. Wu, Privacy-preserving domain adaptation for motor imagery-based brain-computer interfaces, IEEE Trans. on Biomedical Engineering 69 (11) (2022) 3365–3376.
- [27] V. Jayaram, A. Barachant, MOABB: trustworthy algorithm benchmarking for BCIs, Journal of Neural Engineering 15 (6) (2018) 066011.
- [28] A. Barachant, S. Bonnet, M. Congedo, C. Jutten, Multiclass braincomputer interface classiﬁcation by Riemannian geometry, IEEE Trans. on Biomedical Engineering 59 (4) (2012) 920–928.
- [29] Z. Miao, M. Zhao, X. Zhang, D. Ming, LMDA-Net: A lightweight multidimensional attention network for general EEG-based brain-computer interfaces and interpretability, NeuroImage (2023) 120209.

