# arXiv:2310.11198v2[cs.HC]21Feb2024

## EEG motor imagery decoding: A framework for comparative analysis with channel attention mechanisms

### Martin Wimpff1, Leonardo Gizzi2, Jan Zerfowski3, Bin Yang1

1Institute of Signal Processing and System Theory, University of Stuttgart, Germany 2Fraunhofer Institute for Manufacturing Engineering and Automation IPA, Germany 3Clinical Neurotechnology Laboratory, Department of Psychiatry and Neurosciences, Charit´e Campus Mitte (CCM), Charit´e - Universit¨tsmedizin Berlin, Germany

E-mail: martin.wimpff@iss.uni-stuttgart.de

Abstract. Objective The objective of this study is to investigate the application of various channel attention mechanisms within the domain of brain-computer interface (BCI) for motor imagery decoding. Channel attention mechanisms can be seen as a powerful evolution of spatial filters traditionally used for motor imagery decoding. This study systematically compares such mechanisms by integrating them into a lightweight architecture framework to evaluate their impact. Approach We carefully construct a straightforward and lightweight baseline architecture designed to seamlessly integrate different channel attention mechanisms. This approach is contrary to previous works which only investigate one attention mechanism and usually build a very complex, sometimes nested architecture. Our framework allows us to evaluate and compare the impact of different attention mechanisms under the same circumstances. The easy integration of different channel attention mechanisms as well as the low computational complexity enables us to conduct a wide range of experiments on four datasets to thoroughly assess the effectiveness of the baseline model and the attention mechanisms. Results Our experiments demonstrate the strength and generalizability of our architecture framework as well as how channel attention mechanisms can improve the performance while maintaining the small memory footprint and low computational complexity of our baseline architecture. Significance Our architecture emphasizes simplicity, offering easy integration of channel attention mechanisms, while maintaining a high degree of generalizability across datasets, making it a versatile and efficient solution for EEG motor imagery decoding within brain-computer interfaces.

### 1. Introduction

In the field of modern neuroscience and technology, researchers and clinicians are exploring innovative approaches to bridge the gap between the human brain and external devices. One avenue of research is electroencephalogram (EEG) motor imagery decoding, which holds great promise for improving neurorehabilitation strategies [1]. EEG has emerged as a key technology for deciphering the intricate relationship between the mind and bodily movements because it is a non-invasive, versatile and

affordable technique for measuring brain activity. Motor imagery, the mental simulation of movement without actual execution, generates EEG patterns similar to those generated during actual execution. These patterns can be decoded and translated into meaningful commands, enabling direct communication between the brain and external devices. Brain-computer-interfaces (BCIs), based on the principles of EEG motor imagery decoding, provide a pathway for individuals with motor impairments to regain lost functionality. Such interfaces offer unprecedented opportunities for people with conditions like spinal cord injuries, stroke or neurodegenerative diseases to restore a degree of independence and improve their quality of life. One critical aspect of BCIs is the decoding algorithm used to translate the measured brain activity into meaningful commands. Our work is centered on understanding and investigating different deep learning solutions for the decoding problem. Since the introduction of AlexNet in 2012, deep neural networks (DNN) have transformed many fields including computer vision, natural language processing and medicine. Throughout the years, the underlying architectures became bigger, wider and deeper to solve increasingly complex tasks at the level of a human and beyond. Currently, generative pre-trained transformer (GPT) models like ChatGPT as well as vision transformers are creating a new hype around the role of attention and especially around the transformer architecture. While the attention mechanism and transformers are well understood and investigated in the natural language processing and computer vision area, attention is still largely unexplored in the context of BCI and EEG.

- [2, 3, 4, 5, 6, 7] all use a squeeze-and-excitation (SE) module in their architecture. [2] builds a complex hybrid architecture with common spatial patterns (CSP), SincNet filters, an SE module, temporal and spatial convolutions as well as gated recurrent units (GRU). [3] created a feature fusion model that uses the SE block to combine deep and multi-spectral features. [4, 5] created multi-branch convolutional neural networks (CNN) in combination with SE modules. The architecture by [5] additionally involves an Inception-Block [8] and a ResNet [9]. [6] and [7] use time-frequency representations instead of raw time series. [10, 11, 12, 13, 14, 15, 16, 17, 18] use other types of attention mechanisms. [10] uses an inception-like CNN together with a kind of attention that is not described further. We believe that it is something within the category of multi-head self-attention (MHSA)

- [19]. [11] built an architecture consisting of a convolutional stage as in ShallowNet
- [20] and EEGNet [21] followed by MHSA blocks attending over the temporal direction. [12] uses a similar convolutional stage followed by an ensemble of blocks consisting of MHSA and temporal convolutional blocks [13]. [14] on the other hand uses a graph-based CNN together with a recurrent attention module composed of long short-term memory cells (LSTM). [15] uses a complex time-distributed attention architecture, where the EEG signal is initially split into non-overlapping segments and further spatially filtered. Afterwards, the segments get classified through parallel attention modules (one for each segment) followed by an LSTM and a fully connected layer. Further, there are some works that combine different attention mechanisms like

[16, 17, 18]. [16] combines a custom lightweight channel recalibration module with the channel attention module from ECA-Net [22]. [17] combines a channel attention module based on the wavelet packet sub-band energy ratio with a temporal attention mechanism followed by a feature fusion architecture. [18] builds a model for emotion recognition that also uses a form of channel-wise attention together with LSTMs and self-attention. We observed that while there is a number of publications about EEG-based BCI using attention, most of them use very complex and taskspecific, computationally inefficient, hybrid/multi-branch/multi-scale/ensemble/timedistributed architectures and all of them investigate only one attention mechanism. The two time-frequency solutions [6, 7] as well as the EEGConformer [11] are an exception by having a simple, non-nested architecture. The insights learned from such specialized and narrow investigations as well as the ability to transfer these learnings to other problems are often limited. An additional problem with complex architectures is their computational complexity as well as comparability. Different models are difficult to compare as each of them uses different layers before and after the layers with attention as well as a different training routine. Those are all reasons that lead to high entry barriers, confusion and mistrust by medical experts towards the deployment of deep learning in BCI. Hence, most of the experts still rely on classical algorithms like CSP [23, 24] or on the somewhat outdated but well explored shallow architectures EEGNet or ShallowNet. To overcome these limitations, we first introduce a simple yet powerful baseline model without any attention mechanism. We will also showcase the process of how we developed this baseline architecture from the well-known EEGNet and ShallowNet to justify our design choices. We then integrate different channel attention mechanisms into this architecture framework while keeping the network and training routine constant across all experiments to allow for a fair comparison. This allows us to measure the real impact and suitability of each attention mechanism. We believe that this fair and systematic comparison is able to increase the understanding of attention in BCIs. Moreover, it serves as a foundational platform for forthcoming research in the realms of attention in BCI. The source code is available at https://github.com/martinwimpff/channel-attention and was developed using the python packages pytorch [25], pytorch-lightning [26], braindecode [20], mne-python [27] and moabb [28].

### 2. Method

- 2.1. Task and datasets

In this study, we will utilize four distinct datasets across two different settings. This aims to encompass a broad spectrum of motor imagery dataset characteristics while also exploring the potential boundaries of our methodology. We will use the 2a [29] and 2b [30] dataset from the BCI competition IV (BCIC IV) and the High Gamma

dataset (HGD) [20]. Additionally we will use the imbalanced dataset IVa from the BCI competition III [31]. The first three datasets are frequently employed in deep learning research and exhibit a range of sensor quantities, spanning from 3 to 44 sensors. Conversely, the BCIC III IVa dataset is typically decoded using traditional methods, given that the training trials can be as minimal as 28 in number. This variety of datasets enables a thorough investigation, allowing for effective comparison and contrast of different methodologies. In the following we will briefly summarize the different datasets. Both datasets from the BCIC IV consist of data from 9 different subjects and were recorded at 250Hz. The 2a dataset was captured using 22 electrodes and consists of trials imagining one of four distinct movements (feet, left hand, right hand and tongue movement). Per subject, two sessions a 288 trials each lasting 4 seconds were acquired. The trials of the first session will be used for training, the trials from the second session will be used for testing. The 2b dataset only uses three electrodes to record the data from two different imagined movements (left hand, right hand). Additionally, the trials last 4.5s instead of 4s and the data was recorded in 5 sessions of which the first three (400 trials) will be used for training and the last two (320 trials) will be used for testing. Thus the first three sessions of the 2b dataset correspond to the first session of the 2a dataset and the last two sessions of the 2b dataset correspond to the second session of the 2a dataset, respectively. The HGD is the biggest dataset used in this investigation and has EEG data from 14 subjects recorded at 250Hz on 128 electrodes of which only 44 sensors covering the motor cortex are used. Similar to the 2a dataset, the trials lasted 4s and four different movements (left hand, right hand, feet, rest) were imagined. The first session consists of approx. 880 trials per subject and will be used for training whereas the second session consists of approx. 160 trials per subject and will be used for testing. To investigate our method for small datasets we also employ experiments with the

- BCIC III IVa dataset which involves data from five subjects. This dataset has 280 trials per subject recorded at 100Hz using 118 electrodes and consists of trials from two distinct classes (right hand, foot). What differentiates this dataset from the others is the imbalanced split into trials used for training and trials used for testing. The number of training trials ranges from 28 trials to 224 trials depending on the subject (aa: 168, al: 224, av: 84, aw: 56, ay: 28) and the remaining trials are used for testing. Each trial lasted 3.5s. To reduce the number of data points per trial to prevent overfitting we selected the three channels shared between the BCIC IV 2b dataset and the BCIC III IVa dataset (C3, Cz and C4). We investigate two different scenarios, within-subject classification and cross-subject leave-one-subject-out classification. For both settings we train one model per subject and use the data from the second session of the target subject for testing. For the within-subject classification, the data from the first session of the target subject is used for training such that the model is trained and tested on data from the same subject.

- In the cross-subject scenario, the model is trained using data from the first session of all subjects except the target subject, aiming to assess its generalization capability to previously unseen subjects. As we employ single-trial classification we always use the full trial at the original sampling frequency to allow a fair comparison to other approaches. However, for the
- BCIC IV 2b dataset, we only utilize the initial 4 seconds of the entire 4.5-second trial, a practice more commonly observed in the literature.

- 2.2. BaseNet

Previous publications [20, 21, 3, 4, 11, 12, 13] working on EEG motor imagery decoding have shown that it is helpful to use a stem-block as a first layer of the architecture. This block is usually composed of a temporal convolutional layer and a spatial convolutional layer along with normalization layers, nonlinearity and pooling layers. Since EEGNet and ShallowNet, most of the successive deep learning architectures used a somewhat similar approach. The problem, however, is that every publication tends to use a slightly different stem-block, some are closer to the one used in ShallowNet, some are more similar to the one in EEGNet. Different kernel sizes, number of filters, normalizations, nonlinearities, pooling layers and weight initializations between different architectures impair the comparability as it is not clear to which part of the network a possible improvement can be attributed to. Moreover, comparing a very complex and specialized architecture to a somewhat dated architecture like EEGNet or ShallowNet without adjusting the hyperparameters and training routine raises concerns about the validity of the comparison. To overcome this limitation, we decided to develop a unified shallow neural network called BaseNet, which aims to be parameter-efficient and expressive with plausible and simple hyperparameter choices. To do so, we gradually combined, simplified and modernized the design choices from EEGNet and ShallowNet to create a strong baseline model. The architecture is visualized in Figure 2a. The first step is the simplification of the training routine. We use the full 4s trial at 250Hz instead of a shortened trial at a lower sampling frequency to provide the full original information to the network to allow a fair comparison to other approaches. Further, we train the model for a fixed number of epochs using a learning rate scheduler with a linear warmup followed by a cosine decay instead of using early stopping to reduce loss oscillations while avoiding an additional data split. The second step involves the simplification of the architecture. To simplify, we use a linear classification layer and always use the default initialization and batch normalization of pytorch. Further, our model does not use bias in the convolutional layers and does not use any kernel weight constraints. We use the grouped convolutions from EEGNet as well as their intermediate batch normalization layer between the first two layers to reduce the number of parameters and to regularize the training. The next step involves the choice of activation function, kernel sizes and pool sizes. We chose the ELU activation function from EEGNet instead of the square-log function

from ShallowNet as it resulted in better performance. We used the kernel and pool sizes of ShallowNet as it was originally developed for trials at 250Hz in contrast to EEGNet, which was developed for trials at 128Hz. We chose to use the depthwise separable convolution from EEGNet to add depth to the model while keeping a low memory footprint. To decouple the channel dimension in the spatial layer from the channel dimension in the depthwise separable convolution, we further added a 1 × 1 convolutional channel projection layer as in EEGConformer [11]. We then used the filter sizes from EEGNet for the depthwise separable convolution and the filter sizes from ShallowNet for the first two convolutional layers. To investigate the use of the different channel attention mechanisms, the attention mechanisms introduced in the next section have to be integrated into the BaseNet architecture. We do this by simply adding the channel attention block between the nonlinearity of the depthwise separable convolution and the pooling layer. This position is visualized by a red dot in Figure 2a.

- 2.3. Attention

Attention enables humans to selectively process and prioritize information from a multitude of sensory stimuli, focusing on those that are relevant to specific goals and cognitive processes. The deep learning community has tried to include different kinds of attention mechanisms for many years (see [32] for a review). The different attention mechanisms can be macroscopically categorized by the domain they are operating in. [32] distinguishes between channel, spatial, temporal and branch attention as well as combinations where the attention mechanism operates on two domains. The success and wide use of spatial filters for motor imagery decoding highlights the importance of the spatial distribution of brain activity. The areas of interest for motor imagery decoding (namely, the motor and sensory cortices) are somatotopically organized, and different cortical areas can be associated with different functions or areas of the body. We will therefore focus on the spatial dimension and compare different channel attention mechanisms in this paper. As EEG data and images have different dimensions, we first want to clarify the terms ”spatial” and ”channel” to avoid further confusion. EEG data typically consists of multiple time series (temporal dimension) from different sensors (spatial dimension) and can be described by a tensor Xeeg ∈ RC×T where C is the number of EEG sensors and T is the number of time points. Images, on the other hand, are three-dimensional tensors Ximg ∈ RC×H×W where C describes the number of color channels of the input image and later the number of feature channels of intermediate tensors, H the height and W the width. As we investigate the use of channel attention mechanisms originating from the image domain for EEG data, the dimension of the color channels C from images Ximg corresponds to the spatial dimension (C) of the EEG tensor Xeeg. We also examine two architectures with additional attention in the spatial domain in images (H and W) which transfers to the temporal domain T in EEG data. It

is worth noting that the attention mechanisms attend over feature channels rather than EEG channels as the second layer (spatial convolution) as well as the channel projector already filter the original input spatially. This is similar to images where the color channels become feature channels after the first convolutional layer. In the following sections we will only use the terms ”channel” and ”temporal” for clarity.

- 2.3.1. General form The general process of attending to a specific region can be formulated as

Attention = f(a(x),x) (1)

where a(x) represents the function that generates the attention. f(a(x),x) means that the input x is processed based on the attention generated by a(x) (cf. [32]). This general form allows us to describe different attention mechanisms in a unified manner.

- 2.3.2. Squeeze-and-excitation Squeeze-and-excitation network (SENet) [33] is a simple yet powerful way to enhance feature representations by adaptively re-calibrating channel-wise information. SENet can be seen as the pioneer of channel attention on which most of the subsequent works are founded. It can be formulated as

a(x) = σ(MLP(GAP(x))) = σ(W2ϕ(W1GAP(x))) (2) f(a(x),x) = a(x) ⊗ x (3)

where global average pooling (GAP) calculates the average of T samples for each channel (RC×T → RC) and the multi-layer-perceptron (MLP) learns adaptive attention weights (∈ RC) per channel. The MLP consists of two fully connected Layers (FC) connected by a ReLU activation function (ϕ) to enable nonlinearity. The first FC projects the channel dimension C to a lower dimension C′ = C/r by multiplying with W1 ∈ RC′×C, where r ≥ 1 is called the reduction rate. The second FC projects the attention weights back to the initial channel dimension C by multiplying with W2 ∈ RC×C′ followed by a sigmoid activation function σ mapping each value to a range between 0 and 1. Finally, each channel of the original input x gets multiplied elementwise by a(x). The GAP layer represents the squeeze module, whereas the excitation module comprises of the MLP and the sigmoid function. The SE block is visualized in Figure 1a. The following channel attention mechanisms try to improve the SE block in different ways. We arranged the following sections based on the improved part of SE. All channel attention mechanisms studied in this paper are visualized in Figure 1.

- 2.3.3. Improving the squeeze module [34, 35, 36] try to improve the original SE module by changing the squeeze module which is a GAP layer in SE to something more expressive. [34] argue that a GAP layer is limited because it only calculates firstorder statistics. Therefore they introduce a global second-order pooling (GSoP) block

to model second-order statistics. Mathematically, the attention part of a GSoP block is given by

a(x) = σ(FC(RwConv(Cov(Conv(x))))) (4)

The initial 1 × 1 convolution reduces the number of channels C to C′. Afterwards, a C′ × C′ covariance matrix is computed. Subsequently, a row-wise normalization is performed through a row-wise convolution which results in a one dimensional feature vector ∈ RC′. The fully-connected layer as well as the sigmoid function is similar to SE.

- [35], on the other hand, view the squeeze module as a compression problem and use the discrete cosine transform (DCT) to decompose the features in the frequency domain. The GAP layer of SE is replaced by a grouped DCT module that divides the original

input with C channels into ngroups groups with each C′ = C/ngroups channels and then multiplies each group of channels element-wise with different DCT bases corresponding to different frequencies. DCT0 is the DCT base with lowest frequency component and is equivalent to a scaled GAP layer (cf. [35] for mathematical derivation). The MLP and the sigmoid function stay the same as in SE. Formally, the attention of their Frequency Channel Attention Network (FCA) can be formulated as

a(x) = σ(MLP(DCT(Group(x)))) (5)

- [36] proposed a method particularly suited to semantic segmentation. Their attention mechanism has K learnable codewords or visual centers di ∈ RC with corresponding

learnable smoothing factors si ∈ R. Soft-assignment weights ek = Ti=1 eik are calculated with

exp(−sk||rik||2)

rik, rik = xi − dk, xi ∈ RC (6)

eik =

K

j=1 exp(−sj||rij||2)

The soft-assignment weights are further aggregated by e = Kk=1 ϕ(ek) where ϕ represents a batch normalization and a ReLU activation function. The final attention function is then given by a(e) = σ(FC(e)). They additionally use a second loss function especially tailored for semantic segmentation which we will not use, as we don’t do semantic segmentation and only have one class per trial.

- 2.3.4. Improving the excitation module The ECA-Net [22] is the only method in this comparison that soley relies on improving the excitation module. In the original SE module the excitation module consists of two FC layers with C2/r parameters each. To reduce the number of parameters, they proposed a method called local cross-channel attention that tries to balance the trade-off between cross-channel interaction and parameter efficiency by using a 1D convolution in the channel dimension after the GAP layer. The attention mechanism of ECA-Net can be formulated as

a(x) = σ(Conv1D(GAP(x))) (7) which only needs k parameters where k is the kernel size of the 1D convolution.

- 2.3.5. Improving the squeeze and the excitation module An early follow-up by the original authors called gather-excite (GE) [37] investigated the parameterization of the squeeze and the deparameterization of the excitation module. Originally, the squeeze module (GAP layer) has zero parameters. GE proposes a gather module that gathers information through a grouped convolution with a variable extent. If the kernel size k equals the length of the sequence (k = T), the extent is called global. A global gather module introduces Ck = CT new parameters. They further investigate a parameter-free excitation module that simply scales each channel based on the sigmoid of its average value without any MLP (a(x) = σ(GAP(x))). Another method trying to reduce the number of parameters is the gated channel transformation (GCT) [38]. This method aggregates channel information by computing the l2-norm per channel instead of the average. There are three learnable parameters αc,βc and γc per channel c controlling the gating mechanism. Instead of a sigmoid function, tanh is used. GCT is given by

sc = αc · ||xc||2, sˆc =

√

Csc [( Cc=1 s2c) + ϵ]

- 1

- 2

, ϵ = 10−5 (8)

a(x) = 1 + tanh(γsˆ+ β) (9)

which reduces the number of parameters from 2C2/r (SENet) to 3C. While the previous approaches (except the parameter-free version from GE) all rely on cross-channel interaction, the style-based recalibration module (SRM) [39] investigates a channel-independent attention mechanism. They first collect d = 2 style features (average and standard deviation) per channel, which they call style pooling. The following step is called style integration which linearly combines the style features per channel through a channel-wise fully connected (CFC) layer. The attention mechanism can be formulated by

a(x) = σ(BN(CFC(Concat([GAP(x),STD(x)])))) (10) where BN is a batch normalization layer and the CFC layer has dC learnable parameters.

- 2.3.6. Channel and temporal attention mechanisms SENet and the subsequent approaches used the attention mechanism only in the channel domain. However, there are combinations which attend over the temporal and channel domain. The pioneering work for combining both types of attention is the convolutional block attention module (CBAM) [40]. CBAM is divided into a channel attention module and a temporal attention module. The channel attention module is almost similar to SENet and the attention mechanism is given by

ach(x) = σ(MLP(GAP(x)) + MLP(GMP(x))) ∈ RC (11) where the MLP is shared and the only difference to SENet is the additional (parameterfree) global max pooling (GMP) layer. Afterwards, nearly the same process is repeated in the temporal domain:

atemp(x) = σ(Conv2D(Concat([GAP(x),GMP(x)]))) ∈ RT (12)

The GAP and GMP layer now calculate the average and the maximum respectively over all channels, resulting in a concatenated feature map f ∈ R2×T. This feature map is then processed by a 2D convolutional layer resulting in a temporal attention map atemp(x) ∈ RT. The complete attention mechanism of CBAM is given by

f(x,ach(x),atemp(x)) = atemp(ach(x) ⊗ x) ⊗ (ach(x) ⊗ x) (13) While the temporal and channel attention module in CBAM do not cooperate explicitly, [41] introduced a mechanism called CAT specifically designed to allow collaboration between the two types of attention. In addition to the GAP and GMP layer in CBAM, they use a global entropy layer (GEP). Instead of concatenating the different feature maps, they use a weighted sum to get one feature map per direction of attention

CA′ = CαMLP(GAP(x)) + CβMLP(GMP(x)) + CγMLP(GEP(x)) (14) TA′ = Conv2D(TαGAP(x) + TβGMP(x) + TγGEP(x) (15)

where the parameters Cα/β/γ,Tα/β/γ ∈ R control the collaboration between the aggregated features in the channel attention and temporal attention respectively. The final attention mechanism is then given by

a(x) = σ(CW · CA′ ) + σ(TW · TA′ ), f(x,a(x)) = a(x) ⊗ x (16) where CW,TW ∈ R control the collaboration between the channel and temporal attention. To investigate the use of collaboration weights for channel attention without temporal attention, we propose a modified version of CAT which we call CATLite. The attention mechanism of CATLite is given by a(x) = CA′ .

- 2.4. Training

We train all of our models with the same training routine for each subject. To preprocess the EEG data, we use a 40Hz lowpass filter for the BCIC datasets and a 4Hz highpass filter for the High Gamma dataset. For the other models used in this comparison

- [3, 11, 12, 13, 20, 21] we used the filters they reported for the BCIC datasets while we kept the 4Hz highpass filter for all experiments with the HGD. We further normalize each channel to have zero mean and unit deviation. We then train all models for a fixed number of 1000 epochs and optimize via the Adam optimizer with a learning rate of 10−3 for the within-subject setting. We further use a learning rate scheduler with a linear warmup of 20 epochs followed by a cosine decay to reduce oscillations of the loss. For the cross-subject experiments, we train for 125 epochs for the BCIC datasets and for 77 epochs for the HGD as there is more training data. For the BCIC IV datasets, for example, there is eight times more training data available compared to the withinsubject setting since each model is trained using data from eight subjects. For the BCIC III IVa dataset, the amount of training data increases by a factor of 1.5-19 compared to the within-subject setting depending on the subject. Therefore, we’ve decided on a compromise, training all models for 125 epochs, also motivated by the pursuit of consistency. The number of warmup epochs was reduced to 3 and 2 respectively.

|x| |
|---|---|
|× T<br><br>C/r<br><br>C/r| |

###### a(x)

||GAP| |
|---|---|
| | |
<br><br>|FC| |
|---|---|
| | |
<br><br>|ReLU| |
|---|---|
| | |
<br><br>|FC| |
|---|---|
| | |
<br><br>|σ|
|---|
|
|---|

C

C

C

C

C

|x| |
|---|---|
|× T<br><br>′ × T<br><br>′ ×C′<br><br>′| |

a(x)

||Conv| |
|---|---|
| | |
<br><br>|Cov, BN| |
|---|---|
| | |
<br><br>|Rw Conv| |
|---|---|
| | |
<br><br>|FC| |
|---|---|
| | |
<br><br>|σ|
|---|
|
|---|

C

C

C

C

C

|x| |
|---|---|
|× T<br><br>C/r<br><br>C/r| |

a(x)

||DCTgroup| |
|---|---|
| | |
<br><br>|FC| |
|---|---|
| | |
<br><br>|ReLU| |
|---|---|
| | |
<br><br>|FC| |
|---|---|
| | |
<br><br>|σ|
|---|
|
|---|

C

C

C

C

C

|x| |
|---|---|
|× T<br><br>× K<br><br>× K| |

a(x)

||Enc| |
|---|---|
| | |
<br><br>|ϕ| |
|---|---|
| | |
<br><br>| | |
|---|---|
| | |
<br><br>|FC| |
|---|---|
| | |
<br><br>|σ|
|---|
|
|---|

C

C

C

C

C

(a) SE Block

|x| |
|---|---|
|× T| |

###### a(x)

||GAP| |
|---|---|
| | |
<br><br>|Conv1D| |
|---|---|
| | |
<br><br>|σ|
|---|
|
|---|

C

C

C

(b) GSoP Block

(c) FCA Block

|x| |
|---|---|
|× T| |

a(x)

||l2-norm| |
|---|---|
| | |
<br><br>|CN| |
|---|---|
| | |
<br><br>|tanh|
|---|
<br><br>α<br><br>β<br><br>γ|
|---|

C

C

C

##### (d) EncNet Block

|x| |
|---|---|
|||GAP|
|---|
<br><br>|STD|
|---|
<br><br>|CFC| |
|---|---|
| | |
<br><br>|BN| |
|---|---|
| | |
<br><br>|σ|
|---|
<br><br>C × T<br><br>C<br><br>C<br><br>C<br><br>× 2|
|---|
| |

a(x)

||GAP|
|---|
<br><br>|STD|
|---|
<br><br>|CFC| |
|---|---|
| | |
<br><br>|BN| |
|---|---|
| | |
<br><br>|σ|
|---|
<br><br>C × T<br><br>C<br><br>C<br><br>C<br><br>× 2|
|---|

(e) ECA Block

(f) GCT Block

(g) SRM Block

#### Figure 1: Channel attention mechanisms. GAP = global average pooling, FC = fullyconnected layer, Cov=covariance pooling, BN=batch normalization, RW Conv = row-

#### wise convolution, DCTgroup=grouped discrete cosine transform, Enc=encoder block, CN=channel normalization, STD = global standard deviation, CFC= channel-wise fully-connected layer. Adapted from [32].

1 × 22 × 1000

Conv(40, (1, 25))

40 × 22 × 1000

BN

Conv(40, (22, 1), g=40)

58.8 73.7

ShallowNet

40 × 1 × 1000

BN, ELU

+ training routine

61.7

AvgPool((1, 75), (1, 15))

+ simplification

60.79

40 × 1 × 62

Dropout(0.5)

+ ELU

66.21

Conv(16, (1, 1))

75.63

BaseNet

16 × 1 × 62

BN, ELU

Conv(16, (1, 15), g=16)

+ kernel/pool sizes

74.93

16 × 1 × 62

+ simplification

71.13

Conv(16, (1, 1))

+ training routine

71.36

16 × 1 × 62

BN, ELU

71.06

EEGNet

AvgPool((1, 8), (1, 8))

16 × 1 × 7

Dropout(0.5)

50 55 60 65 70 75 80

Linear(4)

test accuracy in %

(a) Architecture

(b) Development

- Figure 2: Architecture and development of BaseNet. (a): g = number of groups, BN

= batch normalization. The red dot indicates the position of the optional channel attention mechanism. (b): Accuracies for the BCIC IV 2a dataset in the within-subject scenario. The dashed bar represents the reported accuracy of ShallowNet with their cropped training strategy. The black error bars indicate the standard deviation for five runs with different random seeds.

The test accuracy is evaluated on the last checkpoint. Each experiment is conducted five times with five different random seeds. The reported average accuracy is the average of these five runs. The reported standard deviation is the standard deviation of the average test accuracy (over all subjects) between these five runs. This is done because the training process still involves a fair amount of randomness as the datasets are small and noisy and the dropout rate is very high (50%).

- 3. Results The development of BaseNet from ShallowNet and EEGNet is visualized in Figure

- 2b. Developing BaseNet from ShallowNet, the introduction of the ELU function as well as the introduction of the depthwise separable convolution block along with the channel projector have the greatest impact on the performance. For the evolution from EEGNet to BaseNet on the other hand, changing the kernel and pool sizes shows the greatest impact. Developing BaseNet from ShallowNet and EEGNet, the performance improves with each design change except the simplification step. We therefore also ran experiments without this simplification step. The final performance however was worse,

- Table 1: Results (in %) of all models for the BCIC IV 2a dataset in both settings along with their configuration and number of parameters.

|model| |configuration|parameters<br><br>|within-subject<br><br>|cross-subject|
|---|---|---|---|---|---|

|EEGNet [21] ShallowNet [20] ShallowNet*[20] BaseNet BaseNet + SE| |cropped training<br><br>r=4<br><br><br>|1,716 44,644 44,644<br><br>3,692 3,820|71.06 ± 1.0 58.8 ± 0.51 73.7<br><br>75.63 ± 0.75<br><br>76.9 ± 0.61<br><br><br>|52.74 ± 1.34 47.79 ± 0.84 57.49 ± 0.52 57.55 ± 0.66|
|---|---|---|---|---|---|
|BaseNet + GSoP BaseNet + FCA BaseNet + EncNet| |r=4 r=4, DCT0 4 codewords|4,120 4,812 4,040<br><br>|76.28 ± 1.05 76.33 ± 0.82 76.37 ± 0.76|57.63 ± 0.36<br><br>57.44 ± 0.6<br><br>57.94 ± 0.69<br><br>|
|BaseNet + ECANet| |k=9<br><br>|3,695|76.86 ± 0.63<br><br>|57.11 ± 0.72|
|BaseNet + GE-θ− BaseNet + GE-θ BaseNet + GE-θ+ BaseNet + GCT BaseNet + GCTGAP BaseNet + SE-l2 BaseNet + SRM BaseNet + SRMcross| |e=global e=global, r=4<br>r=4<br>r=4<br>|3,692<br><br>4,716<br><br><br>4,844 3,740 3,740 3,820<br><br>3,756<br><br>4,108<br>|75.57 ± 0.35 75.69 ± 0.84<br><br>74.95 ± 0.87<br><br>75.96 ± 1.04<br><br><br>75.92 ± 0.82 75.89 ± 0.65<br><br>75.65 ± 0.41<br><br>76.19 ± 0.64<br><br><br>|56.97 ± 1.05<br><br>56.96 ± 0.89<br>57.56 ± 0.49<br><br><br>57.76 ± 0.63 57.71 ± 0.63 57.28 ± 0.73 57.04 ± 0.97 56.75 ± 0.79<br>|
|BaseNet + CBAM BaseNet + CAT BaseNet + CATLite| |k=15, r=8 k=3, r=4 r=4<br><br>|3,787 5,641 3,848|76.75 ± 0.65 76.88 ± 1.05 76.91 ± 0.9<br><br>|57.18 ± 0.96 57.99 ± 1.1 57.14 ± 0.6|
|TS-SEFFNet [3] EEGConformer [11] ATCNet [12] EEGTCNet [13]| |act=ELU<br><br>|334,824 789,572 113,732<br><br>4,096|73.5 ± 0.42<br><br>75.79 ± 0.26<br><br>79.08 ± 0.43<br><br>75.62 ± 0.66|55.21 ± 0.36 44.78 ± 0.73 57.81 ± 2.0 54.51 ± 2.46<br><br>|

indicating that those specialized design choices only suit their original architectures and training routine but can easily be removed for BaseNet. In the upcoming sections, we will begin by presenting the results of the different channel attention mechanisms, along with the corresponding ablations. Next, we will assess these results against state-of-the-art approaches, both at the dataset level and on a per-subject basis. Finally, we will examine the models in terms of their computational cost.

- 3.1. Channel attention mechanisms

Table 1-4 display the test accuracies of all tested models for all four datasets in both settings. The best model from the literature as well as our best model is indicated in bold. All results in the tables were produced by us except the ShallowNet* which is the reported result by [20] with their cropped training strategy. To investigate the design

- Table 2: Results (in %) of all models for the BCIC IV 2b dataset in both settings along with their configuration.

|model| |configuration<br><br>|within-subject<br><br>|cross-subject|
|---|---|---|---|---|

|EEGNet [21] ShallowNet [20] BaseNet BaseNet + SE| |r=1|83.54 ± 0.46<br><br>78.41 ± 0.99<br><br>84.34 ± 0.36<br><br><br>84.56 ± 0.43<br><br>|77.57 ± 0.62 74.63 ± 0.56<br>78.52 ± 0.76 78.98 ± 0.94<br>|
|---|---|---|---|---|
|BaseNet + GSoP BaseNet + FCA BaseNet + EncNet| |r=1 r=1, DCT0 2 codewords<br><br>|81.64 ± 0.44<br><br>83.78 ± 0.53<br><br>84.33 ± 0.41<br><br><br>|77.13 ± 0.75 77.77 ± 1.25 77.87 ± 0.66|
|BaseNet + ECANet| |k=11<br><br>|84.51 ± 0.31|78.74 ± 0.43|
|BaseNet + GE-θ− BaseNet + GE-θ BaseNet + GE-θ+ BaseNet + GCT BaseNet + GCTGAP BaseNet + SE-l2 BaseNet + SRM BaseNet + SRMcross<br><br>| |e=global e=global, r=1<br><br>r=1<br><br>r=1<br><br><br>|84.38 ± 0.15<br><br>85.32 ± 0.37<br><br><br>83.5 ± 0.74<br><br>84.52 ± 0.45 84.58 ± 0.23 84.21 ± 0.39 84.84 ± 0.69 83.13 ± 0.52<br><br><br>|77.94 ± 0.42 77.68 ± 0.71<br><br>77.64 ± 0.76<br>78.47 ± 0.79<br><br><br>77.94 ± 0.89<br>78.42 ± 0.95 77.88 ± 0.6 77.39 ± 0.82<br>|
|BaseNet + CBAM BaseNet + CAT BaseNet + CATLite| |r=1, k=15<br><br>r=2, k=9 r=1<br><br><br>|84.61 ± 0.55 84.96 ± 0.44 84.84 ± 0.42|78.58 ± 0.49<br><br>78.8 ± 0.57<br><br>78.26 ± 0.86|
|TS-SEFFNet [3] EEGConformer [11] ATCNet [12] EEGTCNet [13]| |act=ELU|83.27 ± 0.27 81.02 ± 0.53 85.52 ± 0.44<br><br>85.51 ± 0.42|78.15 ± 0.3<br><br>73.41 ± 0.52 78.78 ± 0.77 78.83 ± 0.46<br><br>|

choices of the GCT block, we introduce two modifications GCTGAP and SE-l2. GCTGAP replaces the original l2 layer of GCT by a GAP layer, whereas SE-l2 replaces the original GAP layer of SE by an l2 layer. Additionally we introduce SRMcross where the original CFC layer is replaced by two FC layers and a ReLU function to allow cross-channel interaction. The hyperparameters reduction rate and kernel size were selected based on the ablations performed in section 3.2. The number of codewords of EncNet was set to the number of classes in the particular dataset. For FCA, our preliminary experiments showed that higher DCT components did not lead to any improvements and we therefore used the DCT0 configuration across all experiments. This indicates that the element-wise multiplication with DCT components is not a powerful channel compression strategy for EEG decoding.

- Table 3: Results (in %) of all models for the HGD in both settings along with their configuration.

|model| |configuration<br><br>|within-subject<br><br>|cross-subject|
|---|---|---|---|---|

|EEGNet [21] ShallowNet [20] ShallowNet* [20] BaseNet BaseNet + SE<br><br>| |cropped training<br>r=8<br>|84.68 ± 0.91 88.72 ± 0.85 93.9<br><br>93.94 ± 0.44<br><br>94.45 ± 0.5<br>|57.51 ± 2.39<br><br>72.47 ± 0.94<br><br>-<br><br>68.55 ± 1.74 67.53 ± 1.62<br><br>|
|---|---|---|---|---|
|BaseNet + GSoP BaseNet + FCA BaseNet + EncNet| |r=8 r=8, DCT0 4 codewords|93.66 ± 0.87<br><br>94.17 ± 0.51<br><br><br>93.97 ± 1.08<br><br>|67.77 ± 1.11 67.55 ± 2.12 67.29 ± 0.76|
|BaseNet + ECANet| |k=15|94.88 ± 0.85<br><br>|67.4 ± 1.95|
|BaseNet + GE-θ− BaseNet + GE-θ BaseNet + GE-θ+ BaseNet + GCT BaseNet + GCTGAP BaseNet + SE-l2 BaseNet + SRM BaseNet + SRMcross| |e=global e=global, r=8<br><br>r=8<br><br>r=8<br><br><br>|94.21 ± 0.6 94.3 ± 0.42<br><br>93.77 ± 1.162<br><br>94.19 ± 0.53 94.27 ± 0.37 94.62 ± 0.35 93.3 ± 0.39 93.86 ± 0.82<br><br><br>|68.21 ± 1.29<br><br>67.44 ± 0.53<br><br>67.39 ± 1.56<br>68.95 ± 1.24<br><br><br>68.55 ± 1.34 67.77 ± 1.05 66.65 ± 1.92 66.13 ± 1.11<br>|
|BaseNet + CBAM BaseNet + CAT BaseNet + CATLite| |r=4, k=7 r=4, k=7 r=8<br><br>|94.77 ± 0.4 94.73 ± 0.43 94.49 ± 0.39<br><br>|67.02 ± 1.29 67.24 ± 1.98 66.91 ± 1.77|
|TS-SEFFNet [3] EEGConformer [11] ATCNet [12] EEGTCNet [13]| |act=ELU|91.99 ± 0.52<br><br>95.32 ± 0.4<br><br>92.61 ± 0.67<br><br><br>92.24 ± 1.2<br><br>|69.99 ± 0.57<br>70.63 ± 1.28 65.95 ± 1.51 60.59 ± 1.98<br>|

- 3.1.1. BCIC IV 2a For the BCIC IV 2a dataset (Table 1), CATLite, SE, CAT and ECANet showed the best results in the within-subject setting. For the cross-subject setting, CAT and EncNet performed well, but the overall improvements compared to BaseNet were smaller in contrast to the within-subject setting. Importantly, for the within-subject setting all attention modules performed at the level or above the level of BaseNet. Improving the squeeze module (GSoP, FCA, EncNet) resulted in a performance degradation compared to SE, while there was still an improvement compared to BaseNet.

Among the solutions improving the squeeze and the excitation module, SRMcross showed the best results, indicating that cross-channel interaction is an important aspect of channel attention. As the results of GCT, GCTGAP and SE-l2 are quite similar, we assume that both design choices of GCT have a similar impact on the performance.

- Table 4: Results (in %) of all models for the BCIC III IVa dataset in both settings along with their configuration.

|model| |configuration<br><br>|within-subject<br><br>|cross-subject|
|---|---|---|---|---|

|EEGNet [21] ShallowNet [20] BaseNet BaseNet + SE| |r=1|71.39 ± 1.59<br><br>72.64 ± 0.77<br><br><br>76.82 ± 1.25<br><br>77.35 ± 0.99<br><br><br>|64.96 ± 1.37 68.32 ± 1.57<br>65.82 ± 2.93<br>66.63 ± 2.63<br>|
|---|---|---|---|---|
|BaseNet + GSoP BaseNet + FCA BaseNet + EncNet| |r=1 r=1, DCT0 2 codewords<br><br>|71.66 ± 1.74<br><br>75.64 ± 1.02<br><br>75.65 ± 1.86<br><br><br>|66.21 ± 1.8 66.81 ± 2.51 66.71 ± 2.16|
|BaseNet + ECANet| |k=7<br><br>|78.35 ± 1.23|65.88 ± 1.18|
|BaseNet + GE-θ− BaseNet + GE-θ BaseNet + GE-θ+ BaseNet + GCT BaseNet + GCTGAP BaseNet + SE-l2 BaseNet + SRM BaseNet + SRMcross<br><br>| |e=global e=global, r=1<br><br>r=8<br><br>r=8<br><br><br>|77.31 ± 0.97<br><br>75.91 ± 1.28<br><br>74.99 ± 1.22<br><br>76.29 ± 1.13<br><br>76.49 ± 1.29<br><br>77.29 ± 0.98<br><br><br>77.26 ± 0.92<br><br><br>75.07 ± 1.7<br><br><br><br><br>|66.3 ± 2.42 66.72 ± 1.99 66.69 ± 0.84<br><br>65.76 ± 2.87<br><br>65.52 ± 2.77<br>66.36 ± 2.79<br><br><br>66.55 ± 1.26<br><br><br>66.04 ± 1.74<br>|
|BaseNet + CBAM BaseNet + CAT BaseNet + CATLite| |r=4, k=3 r=8, k=7 r=1<br><br>|77.08 ± 0.91 77.57 ± 1.66 76.95 ± 1.34|65.54 ± 2.82<br><br>66.61 ± 1.33<br><br><br>66.24 ± 1.38|
|EEGConformer [11] ATCNet [12] EEGTCNet [13]<br><br>| |act=ELU|81.71 ± 0.54<br><br>72.16 ± 1.02 74.47 ± 1.55<br><br>|73.37 ± 0.58<br><br>60.88 ± 0.53 62.23 ± 1.65|

CBAM, CAT and CATLite yield good results for both settings. This reflects that temporal attention as well as other compression strategies (maximum, entropy) can be useful. However, as CBAM and CAT do not outperform the other models systematically or by large margins, one could argue that temporal attenton is useful but not necessary.

- 3.1.2. BCIC IV 2b For the BCIC IV 2b dataset (Table 2) solutions without crosschannel interaction (GE-θ, SRM) performed better than their cross-channel counterparts

(GE-θ+, SRMcross) in the within-subject setting. For the cross-subject setting, most approaches performed at the level or below the level of BaseNet. SE and CAT showed slightly better results than BaseNet. Apart from that, elaborating on additional observations is challenging as the differences between the attention modules are quite small.

- 3.1.3. HGD For the HGD (Table 3), ECANet is the best performing channel attention mechanism in the within-subject setting. The kernel size (k=15) is very large (compare Figure 3b) which indicates the importance of a larger degree of cross-channel interaction. For the cross-subject setting, the GCT module yields the best results. As GCTGAP performs better than SE and SE-l2 the superior performance of GCT can be attributed to the gating mechanism rather than the l2 layer.
- 3.1.4. BCIC III IVa The ECANet shows the best results for the BCIC III IVa dataset (Table 4) in the within-subject scenario. The configuration (k=3), however, differs from the one used for the HGD dataset, indicating a lower degree of cross-channel interaction which is confirmed by the results of the different GE and SRM modules. For the crosssubject scenario the results of all attention modules are very similar and it is therefore difficult to make a statement about their performances.

- 3.2. Ablations

To investigate the importance of the two most common hyperparameters reduction rate r and kernel size k, we performed ablations for the within-subject setting for all four datasets for SE, ECANet, CBAM and CAT. The reduction rate r determines the number of parameters (2C2/r) and the degree of information reduction of an SE module for a given number of channels C. We evaluated different reduction rates in Figure 3a. For all datasets, the difference between the configurations is low but the SE module performs better than the BaseNet (indicated by the black line) for almost every configuration. For the BCIC IV 2a dataset, the improvement compared to the baseline is the largest. Additionally, every configuration works better than the BaseNet without attention. To investigate the degree of cross-channel interaction, we varied the kernel size of ECANet and present the results in Figure 3b. For the 2a dataset a medium size kernel works best, whereas a large kernel works best for the HGD. For the 2b dataset, the performance of ECANet is below or at the level of the baseline. In the BCIC III IVa dataset, the findings are varied, making it challenging to derive a clear observation. As CBAM and CAT both showed good performance but their best configurations regarding the reduction ratio r and the kernel size k differed, we decided to investigate this relationship closer. The results of these investigations are shown in Figure 4 and Figure 5 for CBAM and CAT respectively. The best configuration is marked with a red frame. Comparing all eight ablation studies, it is difficult to find signs that certain configurations generally work better than others. Interestingly, for the 2a dataset, the best configuration of CAT (r=4, k=3) marks the worst configuration for CBAM. For the HGD, on the other hand, the best configurations of CBAM and CAT match.

| | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | |

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

(a) SENet

(b) ECANet

#### Figure 3: Ablation studies investigating the influence of the reduction rate and the kernel size for SENet and ECANet respectively. The black lines indicate the average test accuracy of BaseNet.

|±|±|±|±|
|---|---|---|---|
|±|±|±|[Figure 1]<br><br>±|
|±|±|±|±|
|±|±|±|±|

|±|±|±|±|
|---|---|---|---|
|[Figure 2]<br><br>±|±|±|±|
|±|±|±|±|
|±|±|±|±|

|±|±|±|±|
|---|---|---|---|
|±|±|±|[Figure 3]<br><br>±|
|±|±|±|±|
|±|±|±|±|

|±|±|±|±|
|---|---|---|---|
|±|±|[Figure 4]<br><br>±|±|
|±|±|±|±|
|±|±|±|±|

#### Figure 4: Ablation studies investigating the relationship between the reduction rate r in the channel attention module and the kernel size k in the temporal attention module of CBAM. The best configuration is indicated by a red frame.

|±|±|±|±|
|---|---|---|---|
|±|[Figure 5]<br><br>±|±|±|
|±|±|±|±|
|±|±|±|±|

|±|±|±|±|
|---|---|---|---|
|±|±|[Figure 6]<br><br>±|±|
|±|±|±|±|
|±|±|±|±|

|±|±|±|±|
|---|---|---|---|
|±|±|±|[Figure 7]<br><br>±|
|±|±|±|±|
|±|±|±|±|

|±|±|±|±|
|---|---|---|---|
|±|±|[Figure 8]<br><br>±|±|
|±|±|±|±|
|±|±|±|±|

#### Figure 5: Ablation studies investigating the relationship between the reduction rate r in the channel attention module and the kernel size k in the temporal attention module of CAT. The best configuration is indicated by a red frame.

- 3.3. Comparison with state of the art approaches

We also compared our models with four state-of-the-art approaches for the same EEG motor imagery decoding task. We included a lighweight architecture without attention (EEGTCNet), a model using the SE block (TS-SEFFNet) and two different approaches of using MHSA in the temporal domain to cover as many research directions as possible. For EEGTCNet we used only a 4s window instead of the reported 4.5s window and the ELU activation function instead of ReLU, as it showed better results than their reported configuration. Apart from that, we used the same learning rate scheduler as in our experiments for TS-SEFFNet, EEGConformer and EEGTCNet as it also improved the results. All other hyperparameters were kept identical to the reported ones. It is worth noting that we train the EEGConformer twice as long (2000 epochs) and with their data augmentation method (segmentation and reconstruction) because the authors originally also trained the model like that. As the BCIC III IVa dataset uses a smaller sampling rate than the other datasets, TS-SEFFNet, which employs wavelet convolutions specifically defined for a sampling rate of 250Hz, could not be used for this dataset. Our simple BaseNet compares very well against more sophisticated and significantly larger (see number of paramters in Table 1) architectures like TS-SEFFNet, EEGConformer, ATCNet and EEGTCNet. Although it rarely being the absolute best model, it consistently ranks among the highest-performing models across all datasets and settings. The strongest models out of the state-of-the-art models, namely EEGConformer and ATCNet on the other hand, perform very well in some settings at the cost of clearly underperforming in the remaining settings. EEGConformer for instance performs well for the BCIC IV 2a dataset in the within-subject setting and yields very good results for the HGD and BCIC III IVa dataset in both settings. For the remaining three settings on the other hand, it performs up to 13% below BaseNet. For ATCNet, the opposite behavior is true: it performs very well for both BCIC IV datasets but clearly underperforms our models for the remaining two datasets. Compared to traditional DL approaches (ShallowNet, EEGNet), BaseNet outperforms EEGNet in all settings and ShallowNet in 6 out of 8 settings. Only for the cross-subject setting of the HGD and the BCIC III IVa dataset, ShallowNet outperforms BaseNet at the cost of underperforming it in other settings. Across all datasets the channel attention modules are able to further improve the performance of BaseNet by a small margin.

- 3.4. Results per subject

The Tables 1-4 only display the mean performance averaged over all subjects. However, to assess the applicability and robustness of an algorithm, the performance per subject is also important. Therefore we additionally present the results of the best traditional DL model, BaseNet, the best model using channel attention and the best state-of-theart model for the within-subject setting and the cross-subject setting in Figure 6 and

Figure 7, respectively. For the BCIC IV 2a dataset in the within-subject setting, the overall differences are quite consistent with the improvements per subject. Subject 6 and subject 9 are the only clear outliers, where ATCNet outperforms the other models by a large margin. For the BCIC IV 2b dataset, there are no outliers and the improvements are distributed very evenly across all subjects. For the HGD in the within-subject setting, only the results of ShallowNet exhibit irregularities as the performance is excessively low for subject 1 and subject 7 compared to the other models. Due to the imbalanced number of training samples per subject in the BCIC III IVa dataset, the results between the subjects differ a lot from each other. The results for subject al (80-20 split) are almost perfect whereas the performance of subjects with less training data (av: 30-70 split, ay: 10-90 split) is significantly lower. Interestingly, the subject aw performs quite well compared to subject aa which has twice the amount of training data. Additionally, it is worth noting that the EEGConformer is able to achieve a significantly higher performance on the subject ay than all other models. For the cross-subject scenario, the BCIC IV 2a results are consistent. However, ATCNet exhibits a very large standard deviation between the runs for subject 5 which generally is among the most challenging subjects to decode. The results for the BCIC IV 2b dataset and the HGD display no irregularities. For the BCIC III IVa dataset, the results are very mixed and the differences between the models are only partially consistent with the overall differences. Surprisingly, the differences between the subjects are somewhat in line with the previous results from the within-subject scenario despite the significantly different distribution of training data.

- 3.5. Computational cost

As BCI systems typically operate in online or closed-loop mode [42, 43, 44, 45, 46] on devices with limited computational resources, it is crucial to examine the computational expense of new algorithms. Clinicians tasked with developing online BCI systems with feedback must understand whether and how they can integrate advances in single-trial classification into their specific scenario. Figure 8 displays the model size, inference time and the classification accuracy for the BCIC IV 2a dataset in the within-subject scenario. ATCNet and EEGConformer exhibit the longest inference times, while EEGNet demonstrates the lowest. Our BaseNet typically operates with an inference time ranging from 5 to 6ms, contingent on the attention layer employed. In terms of model size or memory footprint, ShallowNet, ATCNet, TS-SEFFNet, and EEGConformer are the four largest models. Conversely, the remaining models, including the proposed BaseNet, have significantly reduced memory footprints, as evidenced by the smaller radii of their respective circles. Considering classification accuracy as well as inference time and memory footprint, three winners emerge: EEGTCNet, BaseNet, and BaseNet+SE. These models achieve high performance while maintaining a small memory footprint and reasonable inference time.

(a) BCIC IV 2a (b) BCIC IV 2b

| | | |
|---|---|---|
| | | |
| | | |
|(c) HG<br><br>6: Results per subject fo indicates the standard devia<br><br>for systems equipped w| |D<br><br>r all datasets in the tion between the five runs<br><br>ith greater computational|

| | |
|---|---|
| | |
| | |
| | |
| | |
|(d) BCIC<br><br>setting. model.<br><br>or tho|III IVa<br><br>The black<br><br>se tolerant|

Figure within-subject bar per mo

However, resources of larger inference times, ATCNet stands out as the optimal choice due to its superior performance. Taking into consideration the classification accuracy shifts the ultimate selection based on the dataset and setting as discussed earlier. What remains constant is our framework’s ability to deliver high performance while keeping memory usage small and inference time reasonable. It’s worth underlining that ATCNet utilizes a temporally stacked ensemble model, which is inefficient to optimize. Consequently, there is a 20x increase in training time compared to BaseNet with any attention layer (on a NVIDIA RTX A6000: 6 hours and 15 minutes versus 18.5 minutes for the 2a dataset). Depending on the available resources during training, this aspect should be taken into consideration.

(a) BCIC IV 2a (b) BCIC IV 2b

| | |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
|(d) BCIC<br><br>setting. Th|III IVa<br><br>e black bar|

(c) HGD

- Figure 7: Results per subject for all datasets in the cross-subject s indicates the standard deviation between the five runs per model.

### 4. Discussion

The results across all four datasets show that our proposed BaseNet is a very strong, yet lightweight, architecture that results in a good performance under different motor imagery decoding settings. The two strongest competitors EEGConformer and ATCNet produce the best results for some settings, at the cost of producing poor results on the remaining settings which limits their potential applicability to other datasets. As pointed out in the previous section, these two models have much larger computational demands during training and inference which further limits their applicability. So the lightweight architectures proposed by us might be the optimal choice if computational resources matter. In addition, our framework has better generalization capability across different datasets and settings. The results of the channel attention mechanisms along with the ablations show that while there is room for improvement, the improvements between the mechanisms and

- Figure 8: Inference time (measured on Intel i7-1195G7 with 4-cores), model size and test accuracy for the BCIC IV 2a dataset in the within-subject setting. The size of the circle indicates the number of parameters of each model. An ideal model would be given by a small dot in the upper left corner of the plot.

configurations are quite small compared to the differences due to major changes in the architecture (cf. Figure 2b). As we used the best configuration from the withinsubject settings for the cross-subject settings, these configurations are suboptimal and we suppose that there is still some room for improvements. Larger improvements, however, can probably be achieved by tailoring the BaseNet architecture towards the datasets, e.g. by using more or less convolutional filters. The overall high performance across all datasets shows that our framework can be a solid starting point for new datasets and problems. One surprising insight from our investigations is that the channel-independent SRM performed better than the cross-channel counterpart on the two datasets with only three sensors in the within-subject setting. On the 2a dataset with 22 sensors and the HGD with 44 sensors, however, the cross-channel version yields better results. This result indicates that the importance of cross-channel interaction might depend on the number of sensors. Using temporal and channel attention together, as in CBAM and CAT, resulted in good but not superior performance, suggesting that channel attention alone is sufficient and the combination with temporal attention is not necessary.

- 4.1. Limitations

To test the limits of our method, we also employed experiments under very challenging conditions with the BCIC III IVa dataset. The results were highly dependent on the subject and the amount of training data available. Compared to the other DL models applied in this study, our framework achieved good results in both settings. However, it is worth noting that the winners of the competition achieved far better results by employing traditional machine learning algorithms instead of deep learning. The results support our expectation that a carefully designed conventional machine learning algorithm still performs better for very small training datasets leveraging handcrafted feature engineering grounded in extensive domain expertise. Automated feature learning via a DL model on the other hand, requires more training data to become effective. Another limitation of our approach is the use of single-trial classification. Although our examination of memory footprint and inference time suggests that our framework may be suitable for real-time classification from a computational perspective, this aspect requires further investigation in future studies. It remains questionable how effectively the DL models can extract useful features from significantly shorter sequences which would be required for real-time applications. Additionally it is evident, that the classification accuracies for the cross-subject setting are substantially lower than for the within-subject setting across all datasets because of the distribution shift between training data and test data. This is expected and consistent across all models and datasets. These distributions shifts need to be addressed by domain adaptation methods to apply such models in practice.

- 5. Conclusion

We developed a simple and lightweight yet powerful framework for EEG motor imagery decoding which clearly outperforms the standard deep learning models EEGNet and ShallowNet. Further, it performs very well across all four datasets compared to more sophisticated, computationally demanding state of the art approaches. Additionally, we systematically investigated and compared a wide range of channel attention mechanisms which can be integrated seamlessly into our BaseNet while maintaining a low complexity and a small memory footprint. The results show that additional channel attention can further improve the performance of the proposed BaseNet.

### Acknowledgments

This paper has been generated within the BMBF-funded Quantum Human Machine Interfaces (QHMI) project, a component of the QSens - Quantum Sensors of the Future cluster. We gratefully acknowledge the financial support provided by the BMBF, which was instrumental in advancing our research efforts. We also extend our deepest appreciation to our dedicated project partners, whose collaborative efforts were indispensable to the accomplishment of this study.

### Conflict of Interest Statement

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

### References

- [1] M. A. Khan, R. Das, H. K. Iversen, and S. Puthusserypady, “Review on motor imagery based bci systems for upper limb post-stroke neurorehabilitation: From designing to application,” Computers in biology and medicine, vol. 123, p. 103843, 2020.
- [2] C. Liu, J. Jin, I. Daly, S. Li, H. Sun, Y. Huang, X. Wang, and A. Cichocki, “Sincnet-based hybrid neural network for motor imagery EEG decoding,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 540–549, 2022.
- [3] Y. Li, L. Guo, Y. Liu, J. Liu, and F. Meng, “A temporal-spectral-based squeeze-and-excitation feature fusion network for motor imagery EEG decoding,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 29, pp. 1534–1545, 2021.
- [4] G. A. Altuwaijri, G. Muhammad, H. Altaheri, and M. Alsulaiman, “A multi-branch convolutional neural network with squeeze-and-excitation attention blocks for EEG-based motor imagery signals classification,” Diagnostics, vol. 12, no. 4, p. 995, 2022.
- [5] Z. Jia, Y. Lin, J. Wang, K. Yang, T. Liu, and X. Zhang, “Mmcnn: A multi-branch multiscale convolutional neural network for motor imagery classification,” in Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2020, Ghent, Belgium, September 14–18, 2020, Proceedings, Part III, pp. 736–751, Springer, 2021.
- [6] H. Zhang, X. Zhao, Z. Wu, B. Sun, and T. Li, “Motor imagery recognition with automatic EEG channel selection and deep learning,” Journal of Neural Engineering, vol. 18, no. 1, p. 016004, 2021.
- [7] B. Sun, X. Zhao, H. Zhang, R. Bai, and T. Li, “EEG motor imagery classification with sparse spectrotemporal decomposition and deep learning,” IEEE Transactions on Automation Science and Engineering, vol. 18, no. 2, pp. 541–551, 2020.
- [8] C. Szegedy, S. Ioffe, V. Vanhoucke, and A. Alemi, “Inception-v4, inception-resnet and the impact of residual connections on learning,” in Proceedings of the AAAI conference on artificial intelligence, vol. 31, 2017.
- [9] K. He, X. Zhang, S. Ren, and J. Sun, “Identity mappings in deep residual networks,” in Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part IV 14, pp. 630–645, Springer, 2016.
- [10] S. U. Amin, H. Altaheri, G. Muhammad, M. Alsulaiman, and W. Abdul, “Attention based inception model for robust EEG motor imagery classification,” in 2021 IEEE international instrumentation and measurement technology conference (I2MTC), pp. 1–6, IEEE, 2021.
- [11] Y. Song, Q. Zheng, B. Liu, and X. Gao, “EEG Conformer: Convolutional transformer for EEG decoding and visualization,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31, pp. 710–719, 2022.
- [12] H. Altaheri, G. Muhammad, and M. Alsulaiman, “Physics-informed attention temporal convolutional network for EEG-based motor imagery classification,” IEEE Transactions on Industrial Informatics, vol. 19, no. 2, pp. 2249–2258, 2022.
- [13] T. M. Ingolfsson, M. Hersche, X. Wang, N. Kobayashi, L. Cavigelli, and L. Benini, “EEGTCNet: An accurate temporal convolutional network for embedded motor-imagery brain– machine interfaces,” in 2020 IEEE International Conference on Systems, Man, and Cybernetics (SMC), pp. 2958–2965, IEEE, 2020.
- [14] D. Zhang, K. Chen, D. Jian, and L. Yao, “Motor imagery classification via temporal attention cues

- of graph embedded EEG signals,” IEEE journal of biomedical and health informatics, vol. 24, no. 9, pp. 2570–2579, 2020.
- [15] X. Ma, S. Qiu, and H. He, “Time-distributed attention network for EEG-based motor imagery decoding from the same limb,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 496–508, 2022.
- [16] Z. Miao, M. Zhao, X. Zhang, and D. Ming, “Lmda-net: A lightweight multi-dimensional attention network for general EEG-based brain-computer interfaces and interpretability,” NeuroImage, p. 120209, 2023.
- [17] X. Liu, R. Shi, Q. Hui, S. Xu, S. Wang, R. Na, Y. Sun, W. Ding, D. Zheng, and X. Chen, “Tcacnet: Temporal and channel attention convolutional network for motor imagery classification of EEGbased bci,” Information Processing & Management, vol. 59, no. 5, p. 103001, 2022.
- [18] W. Tao, C. Li, R. Song, J. Cheng, Y. Liu, F. Wan, and X. Chen, “EEG-based emotion recognition via channel-wise attention and self attention,” IEEE Transactions on Affective Computing, 2020.
- [19] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,  L. Kaiser, and

I. Polosukhin, “Attention is all you need,” Advances in neural information processing systems, vol. 30, 2017.

- [20] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for EEG decoding and visualization,” Human brain mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [21] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: A compact convolutional neural network for EEG-based brain–computer interfaces,” Journal of neural engineering, vol. 15, no. 5, p. 056013, 2018.
- [22] Q. Wang, B. Wu, P. Zhu, P. Li, W. Zuo, and Q. Hu, “Eca-net: Efficient channel attention for deep convolutional neural networks,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 11534–11542, 2020.
- [23] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K.-R. Muller, “Optimizing spatial filters for robust EEG single-trial analysis,” IEEE Signal processing magazine, vol. 25, no. 1, pp. 41–56, 2007.
- [24] K. K. Ang, Z. Y. Chin, H. Zhang, and C. Guan, “Filter bank common spatial pattern (FBCSP) in brain-computer interface,” in 2008 IEEE international joint conference on neural networks (IEEE world congress on computational intelligence), pp. 2390–2397, IEEE, 2008.
- [25] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga, A. Desmaison, A. Kopf, E. Yang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai, and S. Chintala, “PyTorch: An Imperative Style, High-Performance Deep Learning Library,” in Advances in Neural Information Processing Systems 32 (H. Wallach, H. Larochelle, A. Beygelzimer, F. d’Alch´e Buc, E. Fox, and R. Garnett, eds.), pp. 8024–8035, Curran Associates, Inc., 2019.
- [26] W. Falcon and The PyTorch Lightning team, “PyTorch Lightning,” Mar. 2019.
- [27] A. Gramfort, M. Luessi, E. Larson, D. A. Engemann, D. Strohmeier, C. Brodbeck, R. Goj, M. Jas, T. Brooks, L. Parkkonen, et al., “Meg and eeg data analysis with mne-python,” Frontiers in neuroscience, p. 267, 2013.
- [28] V. Jayaram and A. Barachant, “Moabb: trustworthy algorithm benchmarking for bcis,” Journal of neural engineering, vol. 15, no. 6, p. 066011, 2018.
- [29] C. Brunner, R. Leeb, G. Mu¨ller-Putz, A. Schl¨gl, and G. Pfurtscheller, “Bci competition 2008–graz data set a,” Institute for Knowledge Discovery (Laboratory of Brain-Computer Interfaces), Graz University of Technology, vol. 16, pp. 1–6, 2008.
- [30] R. Leeb, C. Brunner, G. Mu¨ller-Putz, A. Schl¨gl, and G. Pfurtscheller, “Bci competition 2008–graz data set b,” Graz University of Technology, Austria, vol. 16, pp. 1–6, 2008.
- [31] B. Blankertz, K.-R. Muller, D. J. Krusienski, G. Schalk, J. R. Wolpaw, A. Schlogl, G. Pfurtscheller, J. R. Millan, M. Schroder, and N. Birbaumer, “The bci competition iii: Validating alternative

- approaches to actual bci problems,” IEEE transactions on neural systems and rehabilitation engineering, vol. 14, no. 2, pp. 153–159, 2006.
- [32] M.-H. Guo, T.-X. Xu, J.-J. Liu, Z.-N. Liu, P.-T. Jiang, T.-J. Mu, S.-H. Zhang, R. R. Martin, M.-M. Cheng, and S.-M. Hu, “Attention mechanisms in computer vision: A survey,” Computational visual media, vol. 8, no. 3, pp. 331–368, 2022.
- [33] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” in Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 7132–7141, 2018.
- [34] Z. Gao, J. Xie, Q. Wang, and P. Li, “Global second-order pooling convolutional networks,” in Proceedings of the IEEE/CVF Conference on computer vision and pattern recognition, pp. 3024– 3033, 2019.
- [35] Z. Qin, P. Zhang, F. Wu, and X. Li, “Fcanet: Frequency channel attention networks,” in Proceedings of the IEEE/CVF international conference on computer vision, pp. 783–792, 2021.
- [36] H. Zhang, K. Dana, J. Shi, Z. Zhang, X. Wang, A. Tyagi, and A. Agrawal, “Context encoding for semantic segmentation,” in Proceedings of the IEEE conference on Computer Vision and Pattern Recognition, pp. 7151–7160, 2018.
- [37] J. Hu, L. Shen, S. Albanie, G. Sun, and A. Vedaldi, “Gather-excite: Exploiting feature context in convolutional neural networks,” Advances in neural information processing systems, vol. 31, 2018.
- [38] Z. Yang, L. Zhu, Y. Wu, and Y. Yang, “Gated channel transformation for visual recognition,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 11794– 11803, 2020.
- [39] H. Lee, H.-E. Kim, and H. Nam, “Srm: A style-based recalibration module for convolutional neural networks,” in Proceedings of the IEEE/CVF International conference on computer vision, pp. 1854–1862, 2019.
- [40] S. Woo, J. Park, J.-Y. Lee, and I. S. Kweon, “Cbam: Convolutional block attention module,” in Proceedings of the European conference on computer vision (ECCV), pp. 3–19, 2018.
- [41] Z. Wu, M. Wang, W. Sun, Y. Li, T. Xu, F. Wang, and K. Huang, “Cat: Learning to collaborate channel and spatial attention from multi-information fusion,” IET Computer Vision, vol. 17, no. 3, pp. 309–318, 2023.
- [42] M. A. Romero-Laiseca, D. Delisle-Rodriguez, V. Cardoso, D. Gurve, F. Loterio, J. H. P. Nascimento, S. Krishnan, A. Frizera-Neto, and T. Bastos-Filho, “A low-cost lower-limb brainmachine interface triggered by pedaling motor imagery for post-stroke patients rehabilitation,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 28, no. 4, pp. 988– 996, 2020.
- [43] R. Xu, N. Jiang, C. Lin, N. Mrachacz-Kersting, K. Dremstrup, and D. Farina, “Enhanced low-latency detection of motor intention from eeg for closed-loop brain-computer interface applications,” IEEE Transactions on biomedical engineering, vol. 61, no. 2, pp. 288–296, 2013.
- [44] N. Mrachacz-Kersting, N. Jiang, A. J. T. Stevenson, I. K. Niazi, V. Kostic, A. Pavlovic, S. Radovanovic, M. Djuric-Jovicic, F. Agosta, K. Dremstrup, et al., “Efficient neuroplasticity induction in chronic stroke patients by an associative brain-computer interface,” Journal of neurophysiology, vol. 115, no. 3, pp. 1410–1421, 2016.
- [45] D. Delisle-Rodriguez, V. Cardoso, D. Gurve, F. Loterio, M. A. Romero-Laiseca, S. Krishnan, and T. Bastos-Filho, “System based on subject-specific bands to recognize pedaling motor imagery: towards a bci for lower-limb rehabilitation,” Journal of neural engineering, vol. 16, no. 5, p. 056005, 2019.
- [46] C. A. Stefano Filho, R. Attux, and G. Castellano, “Motor imagery practice and feedback effects on functional connectivity,” Journal of neural engineering, vol. 18, no. 6, p. 066048, 2022.

