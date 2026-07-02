## EEGDnet: Fusing Non-Local and Local Self-Similarity for 1-D EEG Signal Denoising with 2-D Transformer

# arXiv:2109.04235v1[eess.SP]9Sep2021

Peng Yi 1 *, Kecheng Chen 1 *, Zhaoqi Ma1, Di Zhao 2, Xiaorong Pu 1 †, Yazhou Ren 1, 1School of Computer Science and Engineering, University of Electronic Science and Technology of China, Chengdu, 611731, China 2 Institute of Computing Technology, Chinese Academy of Sciences, Beijing, 100080, China

###### Abstract

Electroencephalogram (EEG) has shown a useful approach to produce a brain-computer interface (BCI). One-dimensional (1-D) EEG signal is yet easily disturbed by certain artifacts (a.k.a. noise) due to the high temporal resolution. Thus, it is crucial to remove the noise in received EEG signal. Recently, deep learning-based EEG signal denoising approaches have achieved impressive performance compared with traditional ones. It is well known that the characteristics of selfsimilarity (including non-local and local ones) of data (e.g., natural images and time-domain signals) are widely leveraged for denoising. However, existing deep learning-based EEG signal denoising methods ignore either the non-local self-similarity (e.g., 1-D convolutional neural network) or local one (e.g., fully connected network and recurrent neural network). To address this issue, we propose a novel 1-D EEG signal denoising network with 2-D transformer, namely EEGDnet. Speciﬁcally, we comprehensively take into account the non-local and local self-similarity of EEG signal through the transformer module. By fusing non-local selfsimilarity in self-attention blocks and local self-similarity in feed forward blocks, the negative impact caused by noises and outliers can be reduced signiﬁcantly. Extensive experiments show that, compared with other state-of-the-art models, EEGDnet achieves much better performance in terms of both quantitative and qualitative metrics.

### Introduction

Brain-computer interface (BCI) provides a communication channel between the brain and external devices, which is widely used in bio-engineering and neuroscience (Birbaumer et al. 2006). According to the mechanism of signal acquisition, BCI can be divided into two streams, i.e., intrusive BCI and non-intrusive BCI. The intrusive BCI is prone to cause the patient’s immune response as the electrodes must be inserted into the patient’s brain, leading to the decline or even disappearance of the signal quality. Researchers thus prefer to use non-invasive BCI due to its lower cost and higher security.

Electroencephalogram (EEG) is a dominant non-invasive BCI (Minguillon, Lopez-Gordo, and Pelayo 2017; Qin and

*These authors contributed equally. †Corresponding author (puxiaor@uestc.edu.cn).

Copyright © 2022, Association for the Advancement of Artiﬁcial Intelligence (www.aaai.org). All rights reserved.

Li 2018). As result of the high temporal resolution, EEG can be easily disturbed by complex noises (Jiang, Bian, and Tian 2019), such as cardiac artifact, ocular artifact, muscle artifact as well as external noise. The effective denoising of EEG signal thus is an urgent and primary step for AI-driven EEG signal understanding. Among a variety of noises, external noise can be removed by reasonable tuning (Cai et al. 2020), including replacing electrodes and using 50Hz (power frequency) traps. In addition, through setting reference channel, removing cardiac artifacts is a convenient operation.

Based on above-mentioned analysis, EEG denoising task would mainly take account into the removals of ocular artifact and muscle artifact. Ocular artifact usually generates obvious artifacts in EEG signal. The origin of ocular artifact is eye movement and blinks, which can propagate over the scalp and be recorded by EEG activity. Muscle artifact can be caused by any muscle proximity to signal recording sites contraction and stretch, the subject talks, sniffs, swallows, etc.

For EEG signal denoising approaches, quite a few traditional and deep learning-based methods have been developed. Traditional approaches have two streams: 1) Regression and ﬁltering-based approaches (e.g., adaptive ﬁlteringbased approaches (He et al. 2006)). 2) Decomposing EEG data and noise data into other domains (e.g., wavelet transform approach (Zhou and Li 2001), blind source separation approach (Klados et al. 2011)). Nevertheless, traditional approaches suffer from some drawbacks. For example, regression-based approaches only work if reference channels can be available. Filtering-based methods may eliminate useful EEG signals during artifact deletion. Meanwhile, decomposing EEG data into other domains are computationally complex and time-consuming, which is not suitable for fast response applications in real-world.

Thanks to the improvement of computing power and large amount of EEG data, researchers tend to utilize deep learning-based approaches to perform noise suppression of EEG signal in recent years. Generally, feedforward neural network (FNN) (Bebis and Georgiopoulos 1994), convolutional neural network (CNN) (Albawi, Mohammed, and AlZawi 2017) or recurrent neural network (RNN) (Zaremba, Sutskever, and Vinyals 2014) are leveraged to construct deep

learning-based EEG signal denoising models. However, existing deep learning-based EEG signal denoising approaches ignore either the non-local self-similarity or local one, although their performance is improved signiﬁcantly compared with traditional methods.

To address those issues, we propose to fuse the non-local and local self-similarity of EEG signal together, which is the intrinsic motivation in this paper. By doing so, we propose a novel EEG signal denoising network with transformer to perform the noise removal of EEG signal, namely EEGDnet. Speciﬁcally, we ﬁrstly propose to leverage the 2-D transformer to comprehensively learn non-local self-similarity in self-attention blocks and local self-similarity in feed forward blocks. Then, we propose to stack multiple transformer modules to explore an optimal denoising pattern with endto-end fashion. Finally, we carefully balance resource consumption and denoising performance to cater the low-power desires of embedded BCI device.

The contributions of this paper can be summarized into three-folds:

- • Compared with existing deep learning-based EEG signal denoising methods, EEGDnet is the ﬁrst attempt to comprehensively take into account the non-local and local self-similarity of EEG signal.
- • EEGDnet is an easy yet effective model to introduce the 2-D transformer into 1-D time-domain signal denoising tasks.
- • EEGDnet enjoys the advantage of lower model parameters and computation consumption on embedded BCI device, which have more competitive edge on real world.

### Related Work

#### Traditional EEG signal denoising approaches

The simplest and most commonly used approach is the regression-based approach (Klados et al. 2011). It is applied under the assumption that each channel is the cumulative sum of pure EEG data and a proportion of artifact (Sweeney, Ward, and McLoone 2012), using exogenous reference channels (i.e., electrooculogram (EOG), electrocardiogram (ECG) ) to omit different artifacts. However, the regression-based approach cannot handle electromyogram (EMG) signals due to the absence of an exogenous reference channel.

Wavelet transform approach (Zhou and Li 2001), transforming a time domain signal into time and frequency domain, has good time-frequency features relative to Fourier transform due to the better tunable time-frequency tradeoff and superiority of non-stationary signal analysis.

The Blind Source Separation (BSS) approach (Klados et al. 2011; Makeig et al. 1996; Corsi-Cabrera et al. 2000; Sweeney, Mcloone, and Ward 2013; Chen, He, and Peng 2014) decomposes the EEG signal into components, distributes them to the neural source and the artifactual source and reconstructs a clean signal by recombining the neural components. However, BSS approach can only be used when a large number of electrodes are available.

Numerous ﬁltering approaches are employed in the cancelation of artifacts from the EEG, for instance, adaptive

ﬁltering, wiener ﬁltering and Bayes ﬁltering, in which different approaches implemented with different principle of optimization (He et al. 2006). The two main types of ﬁlters are the adaptive ﬁltering (Marque et al. 2005), which requires an additional reference channel, and the wiener ﬁltering (Somers, Francart, and Bertrand 2018), which requires calibration.

#### Deep learning-based EEG signal denoising approaches

Deep learning has been widely used in computer vision (Krizhevsky, Sutskever, and Hinton 2012; Simonyan and Zisserman 2015; Szegedy et al. 2016; He et al. 2016) and natural language processing (Mikolov et al. 2013; Vaswani et al. 2017; Sutskever, Vinyals, and Le 2014), and has achieved remarkable success in the last years. Furthermore, deep learning has been applied to other ﬁelds, achieving comparable results with traditional methods including EEG denoising (Yang et al. 2018; Hanrahan 2019; Aynalı 2020; Sun et al. 2020). With the development of computing power and data volume, deep learning can learn essential characteristics of neural oscillations hidden in the data and eliminate artifact from other parts of biology.

Yang et al. (Yang et al. 2018) proposed a fully connected neural network (namely DLN) to remove ocular artifact. The structure of DLN is relatively simple containing only 3 hidden layers and sigmoid activation function. Compared to traditional approaches, DLN is time-saving and do not need manual involvement when reducing noise.

Based on convolutional neural network (CNN), Sun et al. (Sun et al. 2020) presented a one-dimensional residual CNN (1D-ResCNN) model, achieving better performance in some cases compared with traditional methods. In order to better reduce noise, 1D-ResCNN leverages convolution kernels of different scales to process data in parallel. Meanwhile, residual blocks are used to prevent vanishing gradient problem.

Zhang et al. (Zhang et al. 2020) summarizes the previous work and proposes four basic models both for muscle artifact and ocular artifact. The four basic models are based on FNN, CNN, CNN with residual blocks and RNN, respectively.

#### Transformer

In the very recent years, transformer (Vaswani et al. 2017), a type of self-attention-based (Hao et al. 2021) neural networks originally applied for natural language processing tasks (Wang et al. 2021), has attracted the attention of most researchers in AI communities. As it develops, it has almost replaced RNN with its excellent effects, such as exploring long-range relationship, better scalability to highcomplexity models and so on. We can observe that transformer has been applied to image classiﬁcation (Lanchantin et al. 2021; Dosovitskiy et al. 2020), object detection (Yang et al. 2020; Zhu et al. 2021; Carion et al. 2020) and even natural image restoration (Wang et al. 2021; Liang et al. 2021).

[Figure 1]

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

Noise

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

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

##### EEGDnet

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

Pixel-wise Sum

[Figure 57]

[Figure 58]

Noise-free EEG Signal Denoised EEG Signal

Noisy EEG Signal

[Figure 59]

[Figure 60]

        

Residual Connection

Position Encoding

2-D Matrix

SelfAttention

Feed Forward

Normalization Layer

Reshape ( k , q )

Normalization Layer

Reshape ( 1 , k*q )

- Figure 1: The architecture of the training phase of the EEG denoising model based on the EEGDnet model. First, the noise-free EEG signal and the artifact (ocular artifact or muscle artifact) are pixel-wise summed according to a certain signal-to-noise ratio. The result, namely noisy EEG signal, and corresponding noise-free one form the input and the label of EEGDnet, respectively. Inside the EEGDnet, the signal is transformed into a 2-D matrix through the reshape layer at the beginning. The opposition is true at the end of the network. And then sequentially through the self-attention block, normalization layer, feed forward block and normalization layer. Note that there are residual connections in the network. NDepths indicates the number of selfattention blocks as well as other components. Finally, these features that can distinguish EEG signal and noise are automatically reconstructed by minimizing the objective function (MSE) to get the denoised EEG signal.

### Proposed approach

where F(·) denotes a nonlinear mapping function, speciﬁcally a neural network. θ is the learnable parameters of the neural network. For objective, following widely-adopted image/signal denoising methods (Marmolin 1986), we leverage Mean Square Error (MSE) as the loss function to minimize the difference between estimated the noise-free EEG signal xˆ and corresponding noise-free one x, denoted as L(x,xˆ). The overall EEG signal denoising algorithm is presented in Algorithm 1.

#### The overall framework of proposed EEGDnet

In this paper, we propose a EEG signal denoising model to carry out the one-dimensional (1-D) signal noise reduction task. Note that 1) The proposed model aims to well fuse the non-local and local self-similarity of 1-D EEG signal into a 2-D transformer module. 2) The proposed model can also be extended to other types of 1-D signals.

The overall framework of our approach is shown in Figure 1. It can be seen as an end-to-end model, i.e., giving a noisy EEG signal as the input and outputting the corresponding noise-free one. The degradation process of acquired EEG signal can be represented as:

#### Transformer for EEG Signal Denoising

In this paper, a novel EEG signal denoising model (namely EEGDnet) with transformer is proposed. Speciﬁcally, we follow original 2-D transformer (Vaswani et al. 2017) and incorporate it into the denoising scheme. It should be noted that an advantage of this setup is that scalable natural language processing transformer architectures and their efﬁcient implementations can be leveraged as much as possible.

###### y = x + λn (1)

where y ∈ R1×N (N is the number of signal point in a period) denotes an acquired noisy EEG signal, x ∈ R1×N denotes a theoretical noise-free EEG signal, λ and n ∈ R1×N denote the relative contribution of artifacts and artifact (ocular artifact or muscle artifact), respectively.

The detailed transformer architecture in proposed EEGDnet model (as shown in red dashed box of Figure 1) consists of four parts including reshape layer, selfattention block, feed forward block and normalization layer. Speciﬁcally, the 1-D EEG signal is reshaped into 2-D form ﬁrstly and then it was sent into the 2-D transformer encoder, which consists of alternating layers of self-attention blocks and feed forward blocks. Normalization layer and residual connections are applied after every block. The out-

For deep learning-based EEG signal denoising approaches, the denoising procedure can usually be regarded as a nonlinear mapping function from noisy EEG signal y to the corresponding estimated noise-free one xˆ, which can be formulated as:

xˆ = F(y;θ), (2)

Algorithm 1: EEGDnet

Input: Xs = {xis}i=1,...,n, Ys = {ysi}i=1,...,n denote ground-truth and noisy signal in training dataset, respectively; Xt = {xit}i=1,...,m, Yt = {yti}i=1,...,m denote ground-truth and noisy signal in validation dataset, respectively;

Output: F(;θ) - a well trained transformer model

- 1: Initialize θ with random values
- 2: repeat
- 3: Obtain the estimated noise-free output xˆs by F(ys;θ) on training set;
- 4: Calculate the difference between estimation and ground-truth on training set by L(xs,xˆs);
- 5: Update θ using Adam optimizer;
- 6: Obtain the estimated noise-free output xˆt by F(yt;θ) on validation set;
- 7: Calculate the difference between estimation and ground-truth on validation set L(xt,xˆt);
- 8: until L(xt,xˆt) converges;
- 9: return F(;θ)

put of transformer encoder is reshaped into one dimension as the ﬁnal output. These modules will be described.

Reshape layer: In computer vision ﬁelds, an 2-D image can be split into a variety of patches in order to leverage the non-local self-similarity. Inspired by this (Dosovitskiy et al. 2020), we propose to split an epoch of EEG signal into several segments. In other words, an EEG signal x ∈ R1×N is split into ﬁxed-size segments s ∈ Rk×q. Note that N is the length of an epoch, k denotes the input sequence length and q denotes the dimensions of each segment. Correspondingly, at the end of the EEGDnet model, the data will be reverted to original one-dimensional form. Standard learnable 1D position embeddings are then added to the segments embeddings to retain positional information. The resulting sequence of embedding vectors serves as input to the transformer encoder.

Self-attention blocks: In self-attention blocks, each segment of the signal corresponds to a learnable query and a set of learnable key values. An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. In simple terms, the attention function allows ﬁnding the weight of any segment on any segment, thus exploiting the non-local self-similarity between segments.

Furthermore, to enhance the ability of self-attention blocks, multi-head attention (Vaswani et al. 2017) are introduced as an expansion and can be artiﬁcially set. When the number of heads, noted as NHeads, equals to one, multihead attention degenerates into a single attention head.

Feed forward blocks: To take full advantage of the local self-similarity, feed forward blocks use fully connected layers and nonlinear activation function to process each segment. That is, from an epoch perspective, the feed forward blocks exploit local self-similarity within each segment. Besides, dropout regularization (Srivastava et al. 2014) is utilized to enhance the robustness of EEGDnet model.

It should also be noted that different from original transformer, we replace Rectiﬁer Linear Unit (ReLU) (Glorot, Bordes, and Bengio 2011) with Parametric Rectiﬁed Linear Unit (PReLU) (He et al. 2015) in feed forward blocks. Unlike words or image embedding, EEG signal contains both positive and negative values. Consequently, feeding values that are beyond the usual range of features can cause large gradients to back propagate (Haldar et al. 2019). This can permanently shut activation functions like ReLU due to vanishing gradients (Clevert, Unterthiner, and Hochreiter 2016), which is unacceptable to the network.

Compared with ReLU, PReLU has one more parameter a, which represents the derivative if the input is less than zero. This ensures that PReLU has a non-zero output regardless of the input, easing the problem of neuronal death.

Normalization layer and residual connection: Training state-of-the-art deep neural networks is computationally expensive. One way to reduce the training time is to normalize the activities of the neurons. Generally speaking, batch normalization (Ioffe and Szegedy 2015) is adopted for image processing while layer normalization (Ba, Kiros, and Hinton 2016) for natural language processing. Given the 1-D nature of the EEG signal, the EEGDnet model uses layer normalization as the normalization layer.

Vanishing gradients and exploding gradients are commonly encountered problem in the ﬁeld of deep learning. The EEGDnet model alleviates this problem using a simple residual structure (He et al. 2016).

### Experiments and results

#### Experimental Setup

Data set: To evaluate the effectiveness of the proposed EEGDnet model, a widely-adopted EEG signal data set (Zhang et al. 2020) is used in this paper. Speciﬁcally, this data set consists of 4514 EEG epochs, 3400 ocular artifact epochs and 5598 muscle artifact epochs. The sampling time of each epoch is 2 seconds with 256 sampling rate. During the training, simulated mixed signals can be generated according to Eq. 1 with a uniformly distributed signal-to-noise ratio (SNR) from -7dB to 2dB. To enhance the diversity of data, EEG epochs are randomly combined with ocular artifact epochs and muscle artifact epochs for ten times, respectively.

Training details: The deep learning framework (PyTorch) is applied to construct our EEGDnet model. The entire model is optimized by Adam (Kingma and Ba 2015) optimizer for 10K epochs with a learning rate of 5e−5 and betas of (0.5,0.9). The batch size is 1K.

Table 1: Average performances of all SNRs (from -7dB to 2dB). The smaller RRMSEtemporal and RRMSEspectral, and the larger CC, the better denoising effect. The baseline of EEGDnet consists of 6 Depths and 1 Head with k × q equals to

8 × 64. Note that all the models are trained and tested on the same data set. For RRMSEtemporal, RRMSEspectral, the lower the better. For CC, the higher the better. The best result is shown in bold.

Self-Similarity Ocular Artifact Muscle Artifact

Model

local non-local RRMSEtemporal RRMSEspectral CC RRMSEtemporal RRMSEspectral CC

DLN (Yang et al. 2018) 0.699 0.579 0.720 0.917 1.081 0.609 SCNN (Zhang et al. 2020) 0.620 0.526 0.791 0.750 0.697 0.706

1D-ResCNN (Sun et al. 2020) 0.630 0.588 0.776 0.746 0.680 0.692 RNN (Zhang et al. 2020) 0.740 0.696 0.677 0.785 0.775 0.636 EEGDnet 0.497 0.491 0.868 0.677 0.626 0.732

Comparing methods: We compare the proposed EEGDnet model with four existing state-of-the-art deep learning-based EEG denoising methods:

- • Deep learning network (DLN) (Yang et al. 2018): A fully connected neural network with three hidden layers and sigmoid function.
- • Recurrent neural network (RNN) (Zhang et al. 2020): The network contains in order a Long Short-Term Memory (Hochreiter and Schmidhuber 1997) network and three fully connected layers with the ReLU activation function and dropout regularization.
- • Simple convolutional neural networks (SCNN) (Zhang et al. 2020): The network contains four 1D-convolution layers with small 1 ∗ 3 kernels, 1 stride, and 64 feature maps. Each 1D-convolution layer was followed by a batch normalization layer and a ReLU activation function. At the end of the network, there is a fully connected layer to reconstruct the signal.
- • One-dimensional residual convolutional neural networks (1D-ResCNN) (Sun et al. 2020): The structure of the network mainly has three parallel sub-modules which have different convolutional kernels and residual connections. Each 1-D convolution layer was followed by a batch normalization layer and a ReLU activation function. Data from three sub-modules are merged.

Evaluation measures: In terms of differences and correlations both in time and frequency domains, three quantitative metrics (Zhang et al. 2020) are applied to evaluate the performance of different models, including Relative Root Mean Square Error in the temporal domain (RRMSEtemporal), Relative Root Mean Square Error in the spectral domain (RRMSEspectral) and the correlation coefﬁcient (CC).

With the development of the EEG equipment towards miniaturization (Minguillon, Lopez-Gordo, and Pelayo 2017), the computational and parametric quantities of the model must be considered due to the limited computational and storage resources. Therefore, we utilize the amount of calculation(FLOPs), number of parameters(Param) and storage size to reﬂect the actual usability of the models.

Table 2: The amount of computation, number of parameters and storage size of models. The baseline of EEGDnet consists of 6 Depths and 1 Head with k × q equals to 8 × 64. For ﬂops, parameters and storage size, the lower the better. The best result is shown in bold.

Model FLOPs(M) Param(M) StorageSize(MB) DLN (Yang et al. 2018) 1.05 1.05 64.1 SCNN (Zhang et al. 2020) 36.14 16.81 1026.3 1D-ResCNN (Sun et al. 2020) 42.33 8.42 514.2

RNN (Zhang et al. 2020) 0.79 0.53 32.1 EEGDnet 1.44 0.18 11.1

#### Results

Quantitative Results Table 1 shows the quantitative performance of denoising results for both ocular and muscle artifacts. Some observations can be obtained as following.

- • From the perspective of DLN and RNN, they can only leverage non-local self-similarity resulting worst performance in denoising.
- • Stacking of convolutional layers in both SCNN and 1D-ResCNN allows network have large receptive ﬁeld, which means non-local self-similarity can be exploited to some extent implicitly.
- • By fusing non-local self-similarity and local one explicitly, EEGDnet can have better performance.

Meanwhile, there are strict requirements on the amount of operations and the number of parameters of the model, since EEG noise reduction is usually applied to microchips on brain-computer interface devices. It is desirable for the model to have a low number of model parameters as well as computational consumption. Table 2 illustrates the amount of computation, number of parameters and storage size of models. We can notice that EEGDnet model, compared with other deep learning-based denoising methods, not only has a smaller number of parameters and storage size but also achieves state-of-the-art denoising effects. The proposed EEGDnet will be a better choice in real-world application.

Qualitative Results The time-domain order waveforms image can reﬂect the EEG characteristics with the ﬂuctua-

- Table 3: The effect of k × q on the noise reduction performance of EEGDnet. Note k × q must be equal to N = 512 with

- 1 Head and 6 Depths.

k × q Params(K)

Ocular artifact Muscle artifact

RRMSEtemporal RRMSEspectral CC RRMSEtemporal RRMSEspectral CC

- 2 × 256 2889 0.636 0.568 0.769 0.727 0.674 0.690 4 × 128 724 0.554 0.529 0.832 0.698 0.648 0.715

8 × 64 182 0.497 0.491 0.868 0.677 0.626 0.732 16 × 32 46 0.469 0.476 0.882 0.652 0.600 0.749 32 × 16 12 0.459 0.476 0.885 0.642 0.597 0.743 128 × 4 1.3 0.691 0.770 0.711 0.776 0.804 0.646

- Table 4: The effect of the depths of EEGDnet on the noise reduction performance. Note that k × q and N Heads equal to 8 × 64 and 1 Head, respectively.

N Depths Params(K)

Ocular artifact Muscle artifact

RRMSEtemporal RRMSEspectral CC RRMSEtemporal RRMSEspectral CC

2 67 0.492 0.509 0.872 0.663 0.608 0.742 4 124 0.487 0.491 0.873 0.669 0.620 0.737 6 182 0.497 0.491 0.868 0.677 0.626 0.732 8 240 0.512 0.490 0.859 0.680 0.639 0.729

10 298 0.526 0.495 0.850 0.681 0.633 0.727

- Table 5: The effect of number of heads, denoted as N Heads, in self-attention blocks on the noise reduction performance. Note that k × q and N Depths equal to 8 × 64 and 6 Depths, respectively.

Ocular artifact Muscle artifact

N Heads Params(K)

###### RRMSEtemporal RRMSEspectral CC RRMSEtemporal RRMSEspectral CC

- 1 182 0.497 0.491 0.868 0.677 0.626 0.732

- 2 305 0.501 0.492 0.866 0.678 0.636 0.731 4 502 0.526 0.508 0.850 0.687 0.651 0.724 8 895 0.562 0.526 0.828 0.695 0.659 0.716

16 1682 0.577 0.549 0.820 0.696 0.654 0.715

tion of the waveform. Figure 2 shows the qualitative results for noisy EEG signal. We have the following observations.

- • All the methods have certain denoising effects on the noisy EEG signal, while remarkable differences can be noticed in detail.
- • Notice that both DLN and RNN differ signiﬁcantly in detail from the noise-free EEG signal. This may result from their inability to effectively exploit local self-similarity.
- • SCNN and 1D-ResCNN are at a disadvantage in tracking the overall changes of the noise-free EEG signal, although they retain more local details. This is due to the almost fully convolutional network structure, which cannot exploit the non-local self-similarity.
- • Overall, the EEGDnet model uses both non-local selfsimilarity to track overall changes in the signal and local self-similarity to retain detailed information.

Ablation study As the ﬁrst work to apply transformer to 1-D EEG signal noise reduction, ablation experiments are used to explored the effect of some hyperparameters on the noise reduction performance.

We are interested in how the segmentation of different EEG signals (i.e., the shape of 2-D matrix) affects the noise reduction performance. According to the results in Table 3, we have the following observations:

- • As q becomes smaller, the number of parameters is signiﬁcantly reduced, mainly due to the reduction in the number of parameters required for the fully connected layer in the feed forward blocks.
- • When k is extremely small, self-attention blocks can not play its role. Also, when q is extremely small, the segment is similar to a point. Both of the above cases lead to degradation of the network to a fully connected neural network which can not exploit local similarity.
- • The noise reduction effect is best when k and q are close to each other, due to the ability to balance local selfsimilarity and non-local one well.

Table 4 and Table 5 illustrate the effect of different depths and different numbers of heads on the noise reduction effect, respectively. Both hyperparameters (i.e., N Depths and N Heads), to a certain extent, can describe the complexity of EEGDnet model. It can be found that as the com-

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

- (a)

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

- (b)

- Figure 2: Visualized examples of denoising results with different state-of-the-art methods. a) Denoising on Ocular Artifact b) Denoising on Muscle Artifact. For each sub-ﬁgure, an easily-observed window (red box and corresponding zoomed-in view) is selected for better comparison. Note that the amplitude is normalized and the time domain sampling rate is 256 SPS. Regarding two examples, we can observe that the denoising results of our proposed EEGDnet are closer to the ground-truth signals. Please zoom in for better view.

plexity of the network decreases, the noise reduction effect becomes progressively better instead. This may be owing to the fact that the data set we use is relative small and the complex network tends to be overﬁtting.

### Conclusion

Ocular and muscle artifacts denoising is an acknowledged difﬁcult task in EEG-based BCI. In this paper, by fusing non-local self-similarity in self-attention blocks and local self-similarity in feed forward blocks, transformer is ﬁrst im-

posed to EEG denoising task. The proposed method can not only signiﬁcantly reduce the model parameters, but also improve the overall performance for EEG denoising. Extensive experiments have demonstrated that our model outperforms existing denoising methods both in quantitative and qualitative results. It is worth noting that EEGDnet model is a general model that can be also applied to other 1-D signal processing. In the future work, we will extend the proposed model to other applications such as EEG features extraction and classiﬁcation.

### References

Albawi, S.; Mohammed, T. A.; and Al-Zawi, S. 2017. Understanding of a convolutional neural network. In 2017 International Conference on Engineering and Technology (ICET), 1–6. Ieee.

Aynalı, E. 2020. Noise Reduction of EEG Signals Using Autoencoders Built Upon GRU based RNN Layers. Ba, L. J.; Kiros, J. R.; and Hinton, G. E. 2016. Layer Normalization. CoRR, abs/1607.06450. Bebis, G.; and Georgiopoulos, M. 1994. Feed-forward neural networks. IEEE Potentials, 13(4): 27–31.

Birbaumer, N.; Weber, C.; Neuper, C.; Buch, E.; Haapen, K.; and Cohen, L. 2006. Physiological regulation of thinking: brain–computer interface (BCI) research. Progress in brain research, 159: 369–391.

Cai, H.; Qu, Z.; Li, Z.; Zhang, Y.; Hu, X.; and Hu, B. 2020. Feature-level fusion approaches based on multimodal EEG data for depression recognition. Information Fusion, 59: 127–138.

Carion, N.; Massa, F.; Synnaeve, G.; Usunier, N.; Kirillov, A.; and Zagoruyko, S. 2020. End-to-End Object Detection with Transformers. In Vedaldi, A.; Bischof, H.; Brox, T.; and Frahm, J., eds., Computer Vision - ECCV 2020 - 16th European Conference, Glasgow, UK, August 23-28, 2020, Proceedings, Part I, volume 12346 of Lecture Notes in Computer Science, 213–229. Springer.

Chen, X.; He, C.; and Peng, H. 2014. Removal of Muscle Artifacts from Single-Channel EEG Based on Ensemble Empirical Mode Decomposition and Multiset Canonical Correlation Analysis. Journal of Applied Mathematics, 2014.

Clevert, D.; Unterthiner, T.; and Hochreiter, S. 2016. Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs). In 4th International Conference on Learning Representations, ICLR 2016, San Juan, Puerto Rico, May 2-4, 2016, Conference Track Proceedings.

Corsi-Cabrera, M.; Guevara, M. A.; R´ıo-Portilla, Y. D.; Arce, C.; and Villanueva-Hern´andez, Y. 2000. EEG bands during wakefulness, slow-wave, and paradoxical sleep as a result of principal component analysis in the rat. Sleep, 24(6): 738–744.

Dosovitskiy, A.; Beyer, L.; Kolesnikov, A.; Weissenborn, D.; Zhai, X.; Unterthiner, T.; Dehghani, M.; Minderer, M.; Heigold, G.; Gelly, S.; Uszkoreit, J.; and Houlsby, N. 2020. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. CoRR, abs/2010.11929.

Glorot, X.; Bordes, A.; and Bengio, Y. 2011. Deep Sparse Rectiﬁer Neural Networks. Journal of Machine Learning Research, 15: 315–323.

Haldar, M.; Abdool, M.; Ramanathan, P.; Xu, T.; Yang, S.; Duan, H.; Zhang, Q.; Barrow-Williams, N.; Turnbull, B. C.; Collins, B. M.; et al. 2019. Applying deep learning to Airbnb search. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, 1927–1935.

Hanrahan, C. 2019. Noise Reduction in EEG Signals using Convolutional Autoencoding Techniques.

Hao, Y.; Dong, L.; Wei, F.; and Xu, K. 2021. SelfAttention Attribution: Interpreting Information Interactions Inside Transformer. In Thirty-Fifth AAAI Conference on Artiﬁcial Intelligence, AAAI 2021, Thirty-Third Conference on Innovative Applications of Artiﬁcial Intelligence, IAAI 2021, The Eleventh Symposium on Educational Advances in Artiﬁcial Intelligence, EAAI 2021, Virtual Event, February 2-9, 2021, 12963–12971. AAAI Press.

- He, K.; Zhang, X.; Ren, S.; and Sun, J. 2015. Delving deep into rectiﬁers: Surpassing human-level performance on imagenet classiﬁcation. In Proceedings of the IEEE international conference on computer vision, 1026–1034.
- He, K.; Zhang, X.; Ren, S.; and Sun, J. 2016. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, 770–778.

He, P.; Kahle, M.; Wilson, G.; and Russell, C. 2006. Removal of ocular artifacts from EEG: a comparison of adaptive ﬁltering method and regression method using simulated data. In 2005 IEEE Engineering in Medicine and Biology 27th Annual Conference, 1110–1113. IEEE.

Hochreiter, S.; and Schmidhuber, J. 1997. Long short-term memory. Neural computation, 9(8): 1735–1780.

Ioffe, S.; and Szegedy, C. 2015. Batch normalization: Accelerating deep network training by reducing internal covariate shift. In International conference on machine learning, 448– 456. PMLR.

Jiang, X.; Bian, G.-B.; and Tian, Z. 2019. Removal of artifacts from EEG signals: a review. Sensors, 19(5): 987.

Kingma, D. P.; and Ba, J. 2015. Adam: A Method for Stochastic Optimization. In Bengio, Y.; and LeCun, Y., eds., 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings.

Klados, M. A.; Papadelis, C.; Braun, C.; and Bamidis, P. D. 2011. REG-ICA: a hybrid methodology combining blind source separation and regression techniques for the rejection of ocular artifacts. Biomedical Signal Processing and Control, 6(3): 291–300.

Krizhevsky, A.; Sutskever, I.; and Hinton, G. E. 2012. Imagenet classiﬁcation with deep convolutional neural networks. Advances in neural information processing systems, 25: 1097–1105.

Lanchantin, J.; Wang, T.; Ordonez, V.; and Qi, Y. 2021. General Multi-Label Image Classiﬁcation With Transformers. In IEEE Conference on Computer Vision and Pattern Recognition, CVPR 2021, virtual, June 19-25, 2021, 16478–16488. Computer Vision Foundation / IEEE.

Liang, J.; Cao, J.; Sun, G.; Zhang, K.; Gool, L. V.; and Timofte, R. 2021. SwinIR: Image Restoration Using Swin Transformer. CoRR, abs/2108.10257.

Makeig, S.; Bell, A. J.; Jung, T. P.; and Sejnowski, T. J. 1996. Independent Component Analysis of Electroencephalographic Data. Adv.neural Inf.process.syst, 8(8): 1548–1551 vol.2.

Marmolin, H. 1986. Subjective MSE measures. IEEE transactions on systems, man, and cybernetics, 16(3): 486–489.

Marque, C.; Bisch, C.; Dantas, R.; Elayoubi, S.; Brosse, V.; and Perot, C. 2005. Adaptive ﬁltering for ECG rejection from surface EMG recordings. Journal of electromyography and kinesiology, 15(3): 310–315.

Mikolov, T.; Chen, K.; Corrado, G.; and Dean, J. 2013. Efﬁcient Estimation of Word Representations in Vector Space. In Bengio, Y.; and LeCun, Y., eds., 1st International Conference on Learning Representations, ICLR 2013, Scottsdale, Arizona, USA, May 2-4, 2013, Workshop Track Proceedings. Minguillon, J.; Lopez-Gordo, M. A.; and Pelayo, F. 2017. Trends in EEG-BCI for daily-life: Requirements for artifact removal. Biomedical Signal Processing and Control, 31: 407–418. Qin, Z.; and Li, Q. 2018. High rate BCI with portable devices based on EEG. Smart Health, 9: 115–128.

Simonyan, K.; and Zisserman, A. 2015. Very Deep Convolutional Networks for Large-Scale Image Recognition. In 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings.

Somers, B.; Francart, T.; and Bertrand, A. 2018. A generic EEG artifact removal algorithm based on the multi-channel Wiener ﬁlter. Journal of neural engineering, 15(3): 036007. Srivastava, N.; Hinton, G.; Krizhevsky, A.; Sutskever, I.; and Salakhutdinov, R. 2014. Dropout: a simple way to prevent neural networks from overﬁtting. The journal of machine learning research, 15(1): 1929–1958.

Sun, W.; Su, Y.; Wu, X.; and Wu, X. 2020. A novel endto-end 1D-ResCNN model to remove artifact from EEG signals. Neurocomputing, 404: 108–121.

Sutskever, I.; Vinyals, O.; and Le, Q. V. 2014. Sequence to sequence learning with neural networks. In Proceedings of the 27th International Conference on Neural Information Processing Systems-Volume 2, 3104–3112.

Sweeney, K. T.; Mcloone, S. F.; and Ward, T. E. 2013. The use of Ensemble Empirical Mode Decomposition with Canonical Correlation Analysis as a Novel Artifact Removal Technique. IEEE Transactions on Biomedical Engineering, 60(1): 97–105.

Sweeney, K. T.; Ward, T. E.; and McLoone, S. F. 2012. Artifact removal in physiological signals—Practices and pos-

sibilities. IEEE transactions on information technology in biomedicine, 16(3): 488–500.

Szegedy, C.; Vanhoucke, V.; Ioffe, S.; Shlens, J.; and Wojna, Z. 2016. Rethinking the inception architecture for computer vision. In Proceedings of the IEEE conference on computer vision and pattern recognition, 2818–2826.

Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A. N.; Kaiser, L.; and Polosukhin, I. 2017. Attention is All you Need. In Guyon, I.; von Luxburg, U.; Bengio, S.; Wallach, H. M.; Fergus, R.; Vishwanathan, S. V. N.; and Garnett, R., eds., Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA, 5998–6008.

Wang, Z.; Cun, X.; Bao, J.; and Liu, J. 2021. Uformer: A General U-Shaped Transformer for Image Restoration. CoRR, abs/2106.03106.

Yang, B.; Duan, K.; Fan, C.; Hu, C.; and Wang, J. 2018. Automatic ocular artifacts removal in EEG using deep learning. Biomedical Signal Processing and Control, 43: 148–158.

Yang, Z.; Wang, Y.; Chen, X.; Liu, J.; and Qiao, Y. 2020. Context-Transformer: Tackling Object Confusion for FewShot Detection. In The Thirty-Fourth AAAI Conference on Artiﬁcial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artiﬁcial Intelligence Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artiﬁcial Intelligence, EAAI 2020, New York, NY, USA, February 7-12, 2020, 12653–12660. AAAI Press.

Zaremba, W.; Sutskever, I.; and Vinyals, O. 2014. Recurrent neural network regularization. arXiv preprint arXiv:1409.2329.

Zhang, H.; Zhao, M.; Wei, C.; Mantini, D.; Li, Z.; and Liu, Q. 2020. EEGdenoiseNet: A benchmark dataset for deep learning solutions of EEG denoising. arXiv preprint arXiv:2009.11662.

Zhou, W.; and Li, Y. 2001. EEG multiresolution analysis using wavelet transform. In International Conference of the IEEE Engineering in Medicine & Biology Society.

Zhu, X.; Su, W.; Lu, L.; Li, B.; Wang, X.; and Dai, J. 2021. Deformable DETR: Deformable Transformers for End-toEnd Object Detection. In 9th International Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021. OpenReview.net.

