arXiv:2210.04172v1[q-bio.NC]9Oct2022

A Transformer-based deep neural network model for SSVEP classiﬁcation

Jianbo Chena, Yangsong Zhanga,∗, Yudong Pana, Peng Xub,∗, Cuntai Guanc

aLaboratory for Brain Science and Medical Artiﬁcial Intelligence, School of Computer Science and Technology, Southwest University of Science and Technology, Mianyang, China bMOE Key Laboratory for NeuroInformation, Clinical Hospital of Chengdu Brain Science Institute, and Center for Information in BioMedicine, School of Life Science and Technology, University of Electronic Science and Technology of China, Chengdu, China cSchool of Computer Science and Engineering, Nanyang Technological University, Singapore

[Figure 1]

Abstract

Steady-state visual evoked potential (SSVEP) is one of the most commonly used control signal in the brain-computer interface (BCI) systems. However, the conventional spatial ﬁltering methods for SSVEP classiﬁcation highly depend on the subject-speciﬁc calibration data. The need for the methods that can alleviate the demand for the calibration data become urgent. In recent years, developing the methods that can work in inter-subject classiﬁcation scenario has become a promising new direction. As the popular deep learning model nowadays, Transformer has excellent performance and has been used in EEG signal classiﬁcation tasks. Therefore, in this study, we propose a deep learning model for SSVEP classiﬁcation based on Transformer structure in inter-subject classiﬁcation scenario, termed as SSVEPformer, which is the ﬁrst application of the transformer to the classiﬁcation of SSVEP. Inspired by previous studies, the model adopts the frequency spectrum of SSVEP data as input, and explores the spectral and spatial domain information for classiﬁcation. Furthermore, to fully utilize the harmonic information, an extended SSVEPformer based on the ﬁlter bank technology (FB-SSVEPformer) is proposed to further improve the classiﬁcation performance. Experiments were conducted using two open datasets

[Figure 2]

∗Corresponding authors: Yangsong Zhang(zhangysacademy@gmail.com); Peng Xu(xupeng@uestc.edu.cn)

Preprint submitted to Neural Networks October 11, 2022

(Dataset 1: 10 subjects, 12-class task; Dataset 2: 35 subjects, 40-class task) in the inter-subject classiﬁcation scenario. The experimental results show that the proposed models could achieve better results in terms of classiﬁcation accuracy and information transfer rate, compared with other baseline methods. The proposed model validates the feasibility of deep learning models based on Transformer structure for SSVEP classiﬁcation task, and could serve as a potential model to alleviate the calibration procedure in the practical application of SSVEP-based BCI systems.

Keywords: Brain-computer interface, Steady-state visual evoked potential, Transformer, Deep learning, Filter bank

[Figure 3]

- 1. Introduction

Brain-computer interface (BCI) has become a popular research direction in human-computer interaction and medical rehabilitation, which can directly connect the brain to external devices without going through the peripheral nervous system, enabling bidirectional information transmission and feedback [42, 47]. Electroencephalogram (EEG)-based BCIs obtain the intentions of the brain through EEG signals, and have attracted attention due to the advantages of convenience, low cost, and non-invasiveness [1]. Among the various EEG paradigms, the high signal-to-noise ratio and low training time of steady-state visual evoked potential (SSVEP) make it one of the most popular paradigms.

SSVEP refers to the EEG in the visual cortex when the subject gazes at a ﬂickering visual stimulus modulated by a constant frequency [56]. The frequencies of SSVEP are the same as the coding frequency of received visual stimuli as well as its harmnoics[33]. By virtue of this characteristic of SSVEP, it is possible to design SSVEP-based BCI system, such as SSVEP-based speller [27], in which diﬀerent targets are encoded by diﬀerent stimulus frequencies. When the subjects need to select a command, they can gaze at the corresponding ﬂickering target stimulus that coding the command on the interface. The generated SSVEP can be identiﬁed by a specially designed decoder to obtain the intention

of the subject.

In the SSVEP-based BCI system, the robust classiﬁcation of the SSVEPs is very important [28]. As the SSVEP frequency is the same as the stimulus frequency, some researches developed the algorithms based on the prior frequency information, such as power spectral density analysis (PSDA) [40] and canonical correlation analysis (CCA) [22], etc. In addition to the fundamental frequency component, SSVEP also contains harmonic components whose frequencies are multiples of the fundamental frequency [25]. Based on this characteristic, ﬁlter bank technology was introduced to extend the original CCA (FBCCA) [5]. FBCCA uses CCA in multiple subbands of SSVEP data, and ﬁnally weights the correlation coeﬃcients calculated from these subbands. The FBCCA improves the classiﬁcation performance by distinguishing the fundamental frequency and harmonics, demonstrating the eﬀectiveness of the ﬁlter bank technique on SSVEP classiﬁcation. Nowadays, ﬁlter bank technology has been widely used in various methods [57, 31].

However, due to the complexity of EEG, SSVEP data always contains noises, such as spontaneous EEG and electromagnetic interference, seriously polluting the signal [17]. Traditional training-free methods (such as PSDA, CCA) have better results only when the data length is long. To address the noise interference in SSVEP, a series of recognition algorithms based on machine learning have been proposed. Such methods perform under the intra-subject classiﬁcation condition, in which the training and testing data are from the same subjects, as shown in Fig. 1(a). In this condition, the model can obtain parameters that are more suitable for a speciﬁc subject, thereby reducing noise interference [50]. For example, individual template based CCA (IT-CCA) calculates the average of the subject’s existing SSVEP signals at each stimulation frequency and uses it as the reference signal for CCA [4]. This method can add subject-speciﬁc patterns to the reference signal, and is widely used in subsequent algorithms. Task-related component analysis (TRCA) method obtains spatial ﬁlters by maximizing the reconstitution between SSVEPs of diﬀerent trials to reduce the noise of SSVEPs and reference signals [26]. Correlated component

Training data

Testing data

[Figure 4]

[Figure 5]

Training Testing

Classifier

- (a)
- (b)

Testing data

Training data

[Figure 6]

[Figure 7]

Training Testing Classifier

Existing subjects

New subjects

- Figure 1: The diagram of two classiﬁcation scenarios. (a) intra-subject classiﬁcation; (b) inter-subject classiﬁcation.

analysis (CORCA) learns spatial ﬁlters by maximizing the correlation between data to reduce background noise [55]. Task-discriminant component analysis (TDCA) uses multi-class linear discriminant analysis to learn spatiotemporal ﬁlters and classify in a discriminant manner [23].

The above method has signiﬁcant eﬀect in the intra-subject classiﬁcation experiment, in which the training data and the testing data belong to the same subject [32]. However, the collection of SSVEP data is a time-consuming and laborious work. Hence, a potential and challenging direction is to transfer the data from existing subjects to new subjects in the inter-subject classiﬁcation scenario, under which a classiﬁer can be obtained with the data from already existing subjects and then used the classiﬁer to test the data from new subjects, as shown in Fig. 1(b). Although many works have improved traditional state-ofthe-art methods to adapt them to inter-subject scenario, the results may be not optimal [46]. Because the brain processes natural sensory stimuli in a dynamic,

non-ﬁxed, and nonlinear manner, SSVEP is non-stationary and varies widely among individuals [18]. Even the data collected by the same subject, the data acquired at diﬀerent times may also have diﬀerent distribution. These situations pose great challenges for inter-subject experiments, and the performance of traditional machine learning-based algorithms under inter-subject condition degrades greatly, which is far from its performance under intra-subject condition.

In recent years, deep learning has been developed signiﬁcantly and has made milestone progress in areas such as computer vision and natural language processing [19, 8]. Deep learning models have powerful feature extraction capabilities and can directly be applied on the raw data[9, 34]. Deep learning models have been used on many EEG classiﬁcation tasks, including convolutional neural networks (CNN) [60], recurrent neural networks (RNN) [12], graph neural networks (GNN) [59], etc. Several studies have used deep learning to process SSVEP data, achieving outstanding performance on classiﬁcation tasks, especially inter-subject classiﬁcation. For instances, EEGNet is a compact convolutional neural network (CNN) that uses CNNs to implement the spatial-temporal ﬁltering and feature extraction, achieving signiﬁcantly better results than traditional methods under inter-subject conditions [41]. The idea of using temporal and spatial convolutions has achieved promising results, which has also inﬂuenced many later algorithms. The subject invariant SSVEP generative adversarial network (SIS-GAN) uses generative adversarial networks to generate artiﬁcial SSVEP data to expand the training dataset [2]. Complex convolutional neural network (CCNN) uses the complex spectrum of SSVEP signal as the input of CNN for classiﬁcation, demonstrating the eﬀectiveness of complex spectral features on SSVEP classiﬁcation [32]. InceptionEEG-Net (IENet) combines Inception with residual connections and uses multi-scale convolution kernels to extract features from receptive ﬁelds of diﬀerent sizes [13]. In addition, ﬁlter bank technology is also applied in deep learning models to extend the existing models, such as FB-EEGNet and FBCNN [48, 58].

Although the deep learning-based SSVEP recognition model has made great

progress compared with the traditional machine learning algorithm in the intersubject environment, it still has large improvement space to meet the actual needs for SSVEP-based BCI. Under the inter-subject condition, the model should have good generalization performance for unseen subjects. In addition, due to the black-box nature of deep learning, the interpretability of existing deep learning-based models still need to investigate for explaining the classiﬁcation mechanisms as the traditional methods. In recent years, Transformer becomes one of the most promising model structures, which was ﬁrst used in machine translation and quickly took natural language processing by storm with its excellent performance [10, 37]. It was then applied to the ﬁeld of computer vision and achieved brilliant results [11]. So far, Transformer based models become very powerful in many ﬁelds with wide applicability, and are more interpretable compared with other neural networks[38]. Transformer has excellent feature extraction ability, and the extracted features have better performance on downstream tasks. In BCI systems, some studies have applied Transformers to the EEG classiﬁcation tasks, and achieved good results [44, 14, 30]. To the best of our knowledge, the Transformer has not been leveraged for SSVEP classiﬁcation.

In this paper, a deep learning model for SSVEP classiﬁcation based on Transformer structure, termed as SSVEPformer, is proposed. Inspired by previous study [32], the complex spectra of the SSVEP data were adopted as the input of the SSVEPformer model, allowing the model to focus on the frequency domain property of SSVEP data. In addition, we presented a extended SSVEPformer based on the ﬁlter bank technology, termed as FB-SSVEPformer, to further improve the classiﬁcation performance by fully utilizing the harmonic information. To validate the performance of the proposed and compared models, we utilized two public SSVEP datasets. Dataset 1 has 12 categories from ten subject [27], and Dataset 2 has 40 categories from 35 subjects [39]. Using 1 s time window, FB-SSVEPformer achieves 88.37% accuracy and 112.45 bits/min information transfer rate (ITR) on Dataset 1, and 83.19% accuracy and 157.65 bits/min ITR on Dataset 2, under inter-subject classiﬁcation scenario.

The rest of the paper is structured as follows: Section 2 introduces the datasets and baseline methods, and presents the proposed SSVEPformer and FB-SSVEPformer. The performance of the baseline methods and the proposed method on the two datasets is presented in the Section 3. Section 4 discusses the performance and limitations of the model. Finally, Section 5 presents the conclusion for this study.

- 2. Materials and methods

- 2.1. Datasets Two public datasets were adopted to evaluate the performance of all the

methods.

- Dataset 1 [27]: This dataset was acquired with 12 visual target stimuli on

a 27-inch LCD monitor, which were modulated by the frequencies ranged from 9.25 Hz to 14.75 Hz with 0.5 Hz steps. Ten subjects with normal or correctedto-normal vision participated in the experiment, sitting in chairs 60 cm from the monitor in a dimly lit room. The BioSemi ActiveTwo EEG system (Biosemi, Inc.) was used to acquire EEG data from eight electrodes in the occipital region.The whole experiment consisted of 15 blocks. In each block, there were 12 trials corresponding to the 12 ﬂickering target stimuli, in each of which the subjects were required to gaze at one of the 12 target stimuli. The gazed target stimulus in each trial was random selected, and each trial lasted for 4 seconds. The EEG signal was sampled at a sampling rate of 2048 Hz, and then downsampled to 256 Hz.

- Dataset 2 [39]: The dataset consisted of 40 visual target stimuli displayed

on an LCD monitor. The 40 targets were encoded using the joint frequency and phase modulation (JFPM) method, with target stimulation frequencies ranged from 8 Hz to 15.8 Hz with 0.2 Hz step, and phases starting at 0 with 0.5 π steps. Thirty-ﬁve subjects with normal or corrected-to-normal vision participated in the experiment, eight of whom had experience using SSVEP-based spell. For each subject, the experiment consisted of 6 blocks. In each block, the subjects

stared at 40 targets in random order according to the prompts, resulting in a total of 40 trials. Each trial lasted for 6 seconds. For the ﬁrst 0.5 seconds, the subjects were asked to move the realization to the target stimulus position according to the prompt, then ﬁxated on the target stimulus for 5 seconds, and ﬁnally the monitor was blank for 0.5 seconds. EEG data were acquired using a Synamps2 EEG system (Neuroscan, Inc.) at a sampling rate of 1000 Hz and down-sampled to 250 Hz. Finally, a 50 Hz notch ﬁlter was used to eliminate power frequency interference.

- 2.2. Data preprocessing As in the previous study, all eight channels (O1, Oz, O2, PO3, POZ, PO4,

PO7, PO8) in Dataset 1 and nine channels (O1, Oz, O2, PO3, POZ, PO4, PZ, PO5 and PO6) in Dataset 2 were adopted for classiﬁcation [32, 26]. For the models that need time-domain data as input, fourth-order Butterworth ﬁlter with 8-64 Hz bandpass range are used to ﬁlter the data and take the ﬁltered data as input. Suppose the time window length for classiﬁcation be d s, considering the visual delay, the data segments in Dataset 1 were extract in the time window [0.135 s,d + 0.135 s] after the stimulus onset [27]; the data segments were extracted in the time window [0.64 s,d + 0.64 s] in the Dataset 2 [39].

For models that require frequency domain data as input, FFT was used to convert EEG data in the time domain into the frequency domain. The result of the FFT can be expressed as:

FFT(x) = Re[FFT(x)] + iIm[FFT(x)] (1) where x represents the preprocessed EEG data in the time domain, i is the imaginary unit, Re and Im represent the real and imaginary parts of complex spectrum, respectively. For frequency domain data, there are two ways to transform it into model input, namely magnitude spectrum Xmag and complex spectrum Xcomp [32]:

[Figure 8]

Xmag = {Re[FFT(x)]}2 + {Im[FFT(x)]}2 (2) Xcomp = Re[FFT(x)]||Im[FFT(x)] (3)

The symbol || denotes the concatenation operation. The magnitude spectrum calculates the sum of the squares of the real and imaginary parts at each frequency point, discarding the phase information of the data and only containing the magnitude information. The complex spectrum concatenates the real and imaginary parts of the complex Fourier spectrum, and both magnitude and phase information are preserved. Previous studies have shown that phase information has a role in SSVEP classiﬁcation [29, 7], and complex spectrum input also outperforms magnitude spectrum in comparative experiments [32]. Therefore, in this study, we used the complex spectrum Xcomp of the data as the input of the proposed model. The complex spectra input denoted as Icomp, is deﬁned as:





- Xcomp(CH1)
- Xcomp(CH2)

Icomp =

(4)

. Xcomp(CHn)

 

 

where CH1,CH2,··· ,CHn represent diﬀerent EEG channels. Speciﬁcally, for dataset 1, the time-domain input data is padded with zeros so that the resolution after FFT is 0.25 Hz; for dataset 2, zero padding is still used so that the frequency resolution after FFT is 0.2 Hz. After that, we selected the complex spectrum in the range of 8 to 64 Hz, and concatenated the real part and the imaginary part as the input of SSVEPformer and FB-SSVEPformer.

- 2.3. The baseline methods

- 2.3.1. TRCA TRCA is a spatial ﬁltering method that learns the spatial ﬁlters by maxi-

mizing the reproducibility between existing data of the same class, which can

extract task-related components in the data [26]. The average of existing data of the same class is then used as the reference signal for that class. With the spatial ﬁlters obtained by TRCA based on the calibration data, the correlation coeﬃcients between the projected features of the test sample and various reference signals can be computed, and then obtained the classiﬁcation result. In the experiment of this study, owing to the inter-subject classiﬁcation scenario, the data of one test subject will be selected as the test sampels, and the data of all other subjects were pooled together as the calibration data to calculate the spatial ﬁlter and the reference signals of each stimulus frequency.

- 2.3.2. EEGNet EEGNet is a deep learning model specially designed for EEG signal process-

ing, and has been widely used in various EEG classiﬁcation tasks since it was proposed, such as motor imagery, P300, SSVEP, etc [41, 20]. Waytowich et al. applied EEGNet to SSVEP classiﬁcation and achieved excellent results in the inter-subject classiﬁcation task [41]. EEGNet consists of four layers. The ﬁrst layer is a convolutional layer that simulates ﬁltering operation on the EEG data in each channel. The second layer is a depth-wise convolutional layer, which is equivalent to a spatial ﬁlter that weights all the channels. The third layer is a separable convolutional layer for extracting categorical features. The fourth layer is a fully connected layer, which outputs the classiﬁcation result.

- 2.3.3. CCNN CCNN transforms the SSVEP to the frequency domain using FFT, using

the complex spectrum of the signal as the input of the model in order to extract frequency and phase information [32]. The model consists of convolutional layers and fully connected layers. Convolutional layers are responsible for spatial ﬁltering, temporal ﬁltering, and feature extraction. The fully connected layer summarizes the extracted features to get the ﬁnal result. CCNN achieves excellent results using complex spectrum input, proving that complex spectrum representation can be beneﬁcial for SSVEP classiﬁcation.

SSVEPformer Encoder

[Figure 9]

Representation

Convolutional

ChannelMLP

Combination

LayerNorm

LayerNorm

MLPHead

Spectrum

Attention

Complex

Channel

Outputs

Inputs

X 2

- Figure 2: The architecture of SSVEPformer model. SSVEPformer consists of six blocks: the input, complex spectrum representation, channel combination, SSVEPformer encoder, MLP head and the output. The “×2” means that two identical and successive operation sub-encoders shown in the red rectangle box constitute the SSVEPformer encoder.

- 2.4. The proposed SSVEPformer The model adapts to the unique characteristics of SSVEP as much as pos-

sible on the basis of the Transformer structure, and can be considered as a Transformer-esque SSVEP recognition model. Fig. 2 illustrates the model architecture diagram. The SSVEPformer consists of six blocks: the input, the complex spectrum representation, channel combination, SSVEPformer encoder, multilayer perceptron (MLP) head and the output. In the complex spectrum representation block, the input EEG was transformed into complex spectrum Icomp as deﬁned in formula (4). As the core components of SSVEPformer, the detailed description of channel combination, SSVEPformer encoder and MLP head is as follows, and the detailed structure is shown in Table 1. In the following description, N is denoted as the total number of classes, C is the number of SSVEP channels, and F is the length of the complex spectrum in each channel.

- 2.4.1. Channel combination block The SSVEP data were usually acquired from multiple channels, and these

data not only contain valuable SSVEP classiﬁcation information, but also include various artifacts that interfere with the classiﬁcation. Since the channels are distributed at diﬀerent locations on the scalp of brain, the background components may be diﬀerent. Using the channel combination to calculate the

Table 1: Detailed architecture and parameters in the core components of SSVEPformer.

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

Block Module Layer Output size Explanation

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

Input (C, F)

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

Conv1d (2 × C, F) ﬁlters = 2 × C, kernalsize = 1, padding = ’same’ LayerNorm (2 × C, F) Activation (2 × C, F) GELU

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

Channel combination

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

Dropout (2 × C, F) dropoutrate = 0.5

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

LayerNorm (2 × C, F)

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

Conv1d (2 × C, F) ﬁlters = 2 × C, kernalsize = 31, padding = ’same’ LayerNorm (2 × C, F) Activation (2 × C, F) GELU

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

[Figure 51]

CNN module

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

Dropout (2 × C, F) dropoutrate = 0.5 Residual1 (2 × C, F) adding the input of this module

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

SSVEPformer encoder Sub-encoders (× 2)

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

LayerNorm (2 × C, F) Linear (2 × C, F)

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

Channel MLP module

Activation (2 × C, F) GELU Dropout (2 × C, F) dropoutrate = 0.5 Residual2 (2 × C, F) adding the input of this module

[Figure 83]

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

[Figure 96]

[Figure 97]

Flatten (2 × C × F) Dropout (2 × C × F) dropoutrate = 0.5

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

Linear (6 × N) LayerNorm (6 × N) Activation (6 × N) GELU

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

MLP head

[Figure 110]

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

Dropout (6 × N) dropoutrate = 0.5 Linear (N)

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

weighted combination of all the channels can suppress the noise and enhance the SSVEP component that helps the classiﬁcation. In addition, the channel combination will be used multiple times to obtain multiple channel weighted combinations. This is because diﬀerent combination methods focus on diﬀerent classiﬁcation information or suppress diﬀerent noises, and multiple combination operations can improve the robustness and performance of the model. The channel combination block uses convolutional layers to perform weighted combination between channels. The convolutional layer convolves the number of data channels from C to 2 × C using a convolution kernel of length 1 with Conv1d function in Pytorch framework. This process is equivalent to learning 2 × C spatial ﬁlters to weight the data of each channel.

- 2.4.2. SSVEPformer encoder block The original Transformer encoder generally consists of two components, an

attention module and a channel MLP module [37]. The former is used to mix information between tokens, and the latter includes channel MLP for feature extraction. Although the attention mechanism was widely used in the original

Transformer, many subsequent studies have found that the attention mechanism is not necessary for the Transformer [36]. Some studies have used convolution, MLP or even pooling to replace the attention module and achieved similar results [49]. Similarly, SSVEPformer keep the channel MLP module unchanged and replace the attention module with a CNN module.

The SSVEPformer encoder consists of two identical and successive subencoders as shown in Fig. 2. Each sub-encoder consists of two modules, the ﬁrst is the CNN module and the second is the channel MLP module. Residual connection is used in each module, the input of each module is also added to the output of this module. In the CNN module, the Conv1d layer extracts features in the channel dimension using a convolution kernel of length 31, and fuses the features of each channel. In the channel MLP module, features are extracted on each channel using a linear transformation. This linear transformation applies the same operation to each channel, mapping from F elements to new F elements, using high computational cost to obtain global ﬁne-grained features.

- 2.4.3. MLP head block The features extracted by the upstream blocks are ﬁnally input into the

MLP head block, which is mainly composed of two fully connected layers. The input data is ﬁrst ﬂattened to facilitate subsequent operations. Followed by two fully connected layers, the data length is gradually mapped to the number of categories of the dataset. Considering that the input data is already the features extracted by the previous blocks, in order to avoid losing useful information, the MLP head uses two linear layers to continuously reﬁne the input features to obtain the ﬁnal result.

The LayerNorm layer, GELU layer, and Dropout layer used in the network are all common components of deep neural networks. The LayerNorm layer regularizes the data in the channel dimension to ensure the stability of the data feature distribution, making training faster and more stable [45]. The GELU layer adds nonlinear operations to the network, making the model capable of nonlinear ﬁtting [16]. Meanwhile, GELU has been proven to be a

Complex Spectrum Representation 1

|Result|
|---|

|Result 1|
|---|

- Subband 1

- Subband 2

- Subnetwork 1

- Subnetwork 2

ConvolutionalFuse

[Figure 123]

Complex Spectrum

|Result 2|
|---|

Result

Representation 2

# · · ·

· · · · · ·

|· · ·|
|---|

Inputs

Complex Spectrum Representation S

|Result S|
|---|

Subnetwork S

Subband S

- Figure 3: The architecture of FB-SSVEPformer, where S is the number of subbands and the subnetwork is SSVEPformer. The input data is transformed into the data of S subbands through the ﬁlter bank, and then transformed into the frequency domain through FFT. Each subnetwork uses the data of corresponding subband to obtain the result, and then obtains the ﬁnal result through the convolutional fusion operation.

high-performance activation function and one of the current state-of-the-art activation functions [53]. Dropout can avoid overﬁtting during model training and improve model generalization [3].

- 2.5. FB-SSVEPformer In the SSVEP data, there are harmonic components whose frequencies are

multiple times of the fundamental frequency, which can also be used as classiﬁcation features. For example, FBCCA ﬁlters the data into several subbands and actively guides the model to pay attention to the information of harmonics, and achieves better results than original CCA [5]. Here, we presented a extended SSVEPformer based on the ﬁlter bank technology (FB-SSVEPformer) to further improve the classiﬁcation performance by fully utilizing the harmonic information. The model structure is shown in Fig. 3. The original EEG data are ﬁltered into S frequency subbands, which are then fed to the corresponding subnetworks as input. FB-SSVEPformer uses SSVEPformer as a subnetwork, and each subnetwork handles data of diﬀerent subbands. The results of each subnetwork(ρs,f,s = 1,2,··· ,S,f = 1,2,··· ,N) are ﬁnally weighted and fused to obtain the ﬁnal result Yf as follows:

Yf = argmax f=1,...,N

S

ws · ρs,f (5)

s=1

where N is the total number of categories, ws(s = 1,2,··· ,S) is the weighted parameters of the convolution kernel, and S is the number of subbands. The fusion operation refers to the method of FBCCA fusing the results of each subband, which gives special weights to the results of each subband, and then weights them as the ﬁnal result. However, the weights in FBCCA are constants obtained by grid search [6]. FB-SSVEPformer uses convolutional layers to implement weighting operation, and the parameters move in the direction of the best classiﬁcation result during training and eventually stabilize.

For the selection of subbands, the lower and upper cutoﬀ frequencies of the m − th subband were set to m × 8 Hz and 80 Hz on Dataset 1, and m × 9 Hz and 80 Hz on Dataset 2. The eﬀect of the subband division method has been veriﬁed [5, 55, 26]. During the implementation of band-pass ﬁltering, the lower limit of each subband was subtracted by an additional 2 Hz bandwidth [5]. In order to verify the relationship between the number of subbands and the classiﬁcation eﬀect, FB-SSVEPformer with diﬀerent numbers of subbands uses data with a data length of 1 s to conduct experiments on Dataset 1, and the results are shown in Fig. 4. When the number of subbands is 4, the accuracy of the model is slightly improved, but the number of parameters is greatly increased compared to when the number of subbands is 3. When the number of subbands is 2, the accuracy of the model is lower than that when the number of subbands is 3. Considering the balance between the performance and model parameters, the number of subbands in the FB-SSVEPformer model is set to 3 in following analysis.

- 2.6. Experimental settings and performance evaluation All the deep learning models were implemented with the Pytorch framework.

For the SSVEPformer and FB-SSVEPformer models, the convolutional and linear layer parameters were initialized with a normal distribution with mean 0

1.0

- 0M

- 1M

- 2M

- 3M

- 4M

- 5M

Accurate

Number of parameters

0.9

0.8

Accurate

0.7

Numberofparameters

0.6

0.5

1 2 3 4

Number of subbands

- Figure 4: The relationship between the number of subbands of the FB-SSVEPformer and the accuracy and parameters of the model. The experiment uses Dataset 1 with the data length of 1 s. The bars represent the average precision, the lines represent the number of parameters, and the ’M’ means the magnitude of millions.

and variance 0.01. During training, cross-entropy was used to calculate the loss, and backpropagation was used to update the parameters. Both models used a stochastic gradient descent(SGD) algorithm to compute parameter updates with the learning rate of 0.001, the momentum of 0.9, and an L2 regularization penalty of 0.001. The batch size was set to 128, and the dropout rate is set to 0.5. Notably, for SSVEPformer, the number of training epochs is 100. For FB-SSVEPformer, the model ﬁrst uses data from diﬀerent frequency bands to train each subnetwork for 100 epochs to stabilize their results, and then trains the entire model for 20 epochs.

Three models of EEGNet, CCNN, TRCA were used as baseline methods to compare with the proposed two models. For the fair comparison, the preprocessing procedures of the input data are the same as the operation described

above. For CCNN method, the EEG data need further transform into complex spectrum [32].

The classiﬁcation accuracy and ITR were used as metrics to evaluate the performance of each method. The accuracy is the ratio of the number of the correctly classiﬁed samples to the number of the total test samples. ITR (bits/minute) is calculated as follows [43]:

ITR =

60 T

1 − P N − 1

× log2N + Plog2P + (1 − P)log2

[Figure 124]

[Figure 125]

(6)

where N is the total number of categories and T is the average time (seconds) for selection. During calculating the ITR, 0.5 s gaze movement time was added into the parameter T as previous studies [26, 6]. For example, when the data length is 1 s, then the T is set to 1.5 s during the ITR calculation with the formula (6).

In current study, we focused on the inter-subject classiﬁcation experiment, the leave-one-subject-out(LOSO) strategy was adopted. Speciﬁcally, when evaluating on each of the two datasets, the data of one subject was used as the test set, and the data of all other subjects were used for training set. The procedure repeated until all the subjects were served as the test subject once.

- 3. Result

In order to evaluate all the methods, the experiments were conducted on Dataset 1 and Dataset 2. The TRCA, EEGNet and CCNN were used as the baseline methods, which have achieve excellent performance in previous studies [26, 32, 41].

- 3.1. Dataset 1 Fig. 5(a) and (b) show the average classiﬁcation accuracies and ITRs of the

- ﬁve methods on Dataset 1, respectively. The data length ranges from 0.5 s to 1 s with an interval of 0.1 s. The results show that the proposed SSVEPformer and FB-SSVEPformer outperform other compared baseline methods.

TRCA EEGNet CCNN SSVEPformer FB -SSVEPformer

100

130

120

90

110

80

100

90

70

80

Accuracy(%)

ITR(bits/min)

60

70

60

50

50

40

40

0.5 0.6 0.7 0.8 0.9 1.0

0 .5 0.6 0.7 0.8 0.9 1.0

Data length (s )

Data length (s )

(a)

(b)

- Figure 5: The average classiﬁcation results across subjects of the ﬁve methods with diﬀerent

- data length on Dataset 1. (a) average accuracies; (b) average ITRs. The error bars indicate the standard errors of each results.

FB-SSVEPformer achieves the best results in both average classiﬁcation accuracies and ITRs, and SSVEPformer achieves better results than the three baseline methods, especially when the data length is shorter than 1 s. From 0.5 s to 1 s, the average accuracies of SSVEPformer are 64.93%, 68.61%, 73.72%, 78.61%, 82.33% and 84.16%, and the ITRs are 94.17 bits/min, 95.35 bits/min, 99.90 bits/min, 103.96 bits/min, 105.74 bits/min and 102.25 bits/min, respectively. From 0.5 s to 1 s, the average accuracies of FB-SSVEPformer are 68.00%, 71.72%, 78.22%, 82.44%, 85.00%, and 88.37%, and the ITRs are 103.86 bits/min, 103.91 bits/min, 112.10 bits/min, 113.14 bits/min, 111.73 bits/min and 112.45 bits/min, respectively.

TRCA EEGNet CCNN SSVEPformer FB -SSVEPformer

90

180

80

160

70

140

60

120

50

100

Accuracy(%)

ITR(bits/min)

40

80

30

60

20

40

10

20

0.5 0.6 0.7 0.8 0.9 1.0

0 .5 0.6 0.7 0.8 0.9 1.0

Data length (sec )

Data length (sec )

(a)

(b)

- Figure 6: The average classiﬁcation results across subjects of the ﬁve methods with diﬀerent

- data length on Dataset 2. (a) average accuracies; (b) average ITRs. The error bars indicate the standard errors of each results.
- 3.2. Dataset 2 Fig. 6(a) and (b) show the average classiﬁcation accuracies and ITRs of the

- ﬁve methods on Dataset 2, respectively. As the results on Dataset 1, the experimental results show that the SSVEPformer and FB-SSVEPformer outperform other three methods. FB-SSVEPformer achieves the best results in both average classiﬁcation accuracies and ITRs, and SSVEPformer is also better than the baseline methods. From 0.5 s to 1 s, the average accuracies of SSVEPformer are 51.08%, 58.71%, 66.06%, 73.20%, 78.10 %, and 80.40%, and the ITRs are 113.31 bits/min, 126.83 bits/min, 139.14 bits/min, 149.41 bits/min, 153.68 bits/min and 149.95 bits/min, respectively. From 0.5 s to 1 s, the average accuracies of FB-SSVEPformer are 54.42%, 62.63%, 71.05%, 76.90%, 81.18% and 83.19% and the ITRs are 125.13 bits/min, 140.10 bits/min, 154.36 bits/min, 160.76 bits/min, 162.28 bits/min and 157.65 bits/min, respectively.

Based on the results on the two widely used datasets for the method evalu-

ation, we could ﬁnd that the SSVEPformer and FB-SSVEPformer promote the SSVEP classiﬁcation performance in the inter-subject scenario.

- 4. Discussion

- 4.1. A feasible method in inter-subject scenario for SSVEP classiﬁcation The SSVEP-based BCI could provide enough number of targets to code the

commands or characters for the application. Although lots of methods have been proposed [51], it is still challenging to recognize the target with the EEG signals for the users, especially when dealing with the large number of targets. In recent years, the spatial ﬁltering methods based on the calibration data become a popular solution to achieve high classiﬁcation accuracy, such as the TRCA method and its variant. Whereas, the collection of calibration data is time-consuming and laborious. Therefore, a potential strategy is to utilize the data from existing subjects to train the method for the new subjects in a inter-subject classiﬁcation scenario that can realize the plug-and-play application without new data collection and calibration procedure. Unfortunately, the data distribution may vary largely among diﬀerent subjects, which result in the performance of traditional algorithms under inter-subject scenario degrades greatly. These situations pose great challenges for inter-subject classiﬁcation with the traditional method, such as TRCA [32].

In recent years, deep learning methods have achieved great success for brain signals analysis [54]. Deep learning-based solutions for alleviating the calibration data under diﬀerent BCI paradigms have gradually increased in recent years. For the SSVEP paradigm, the CCNN model provide a option for inter-subject classiﬁcation without the calibration data from a new subject [32]. Even so, it still has large improvement space to meet the practical needs. In recent years, the Transformer and the variants have achieved state-of-the-art performance in various ﬁelds [15, 21]. In this study, we attempted to design a deep learning model with Transformer structure for SSVEP classiﬁcation in calibration-free data condition. We proposed SSVEPformer and a variant FB-SSVEPformer

SSVEPformer FB-SSVEPformer

100

210

200

95

190

90

Accuracy(%)

180

170

ITR(bits/min)

85

160

80

150

75

140

0 1 2 3 4 5

0 1 2 3 4 5

Number of training blocks

Number of blocks

(a)

(b)

- Figure 7: Subject-adaptive experimental results of SSVEPformer and FB-SSVEPformer. The experiments were coducted on Dataset 2 with the duration of 1 second. The horizontal axis is the amount of data used for subject-adaptive training. When the number of blocks is 0, it means that no subject-adaptive training was performed.

with ﬁlter bank technology, which is the ﬁrst application of the Transformer to the SSVEP classiﬁcation. Evaluated on two public datasets with diﬀerent numbers of targets, with data length of 1 s, the SSVEPformer obtains 84.16 % and 80.40 % accuracies, and the FB-SSVEPformer obtains 88.37 % and 83.19 % accuracies, on 12-class and 40-class classiﬁcation task, respectively. The experimental results show that the proposed models could achieve excellent performance in inter-subject classiﬁcation task. The proposed model validates the feasibility of deep learning models based on Transformer structure for calibration-free SSVEP classiﬁcation task, and could serve as a potential model to alleviate the calibration procedure in the practical application of SSVEPbased BCI systems.

- 4.2. Enhancing the performance with subject-adaptive strategy In recent years, deep learning-based methods have been widely used in

SSVEP classiﬁcation, showing no less performance than traditional methods in both classiﬁcation performance and generalization. In the SSVEP-based BCI system, when the user uses it for a period of time, some of the user’s own data could be collected. These data can be used to update the model for adapting to the user’s data and improve the performance of the system. This method of adding part of the data from the test subject in inter-subject classiﬁcation scenario is subject-adaptive strategy [52]. Here, in order to investigate the performance of the proposed method under the subject-adaptive strategy, we use the data with 1 second length in dataset 2 for experiment. Speciﬁcally, for SSVEPformer, after the model is trained under the inter-subject rule, it will continue to train for 30 epochs using part of the data from the test subject, and ﬁnally validate on the remaining data from that test subject. For FB-SSVEPformer, after the model is trained under the inter-subject rule, it will ﬁrst use part of the data from the test subject to train each subnetwork for 20 epochs, then train the entire model for 10 epochs, and ﬁnally verify it on the remaining data from that test subject. Furthermore, we checked the inﬂuence of the diﬀerent numbers of data blocks at each frequency from the test subject on the classiﬁcation result for subject-adpative training. The result is shown in the Fig. 7. It can be seen that using the data from test subject for subject-adaptive can signiﬁcantly improve the performance of the model, and the accuracy of both models has increased above 90%. Surprisingly, after subject-adaptive with only one block data at each frequency, the performance was improved by 11.80% and 10.33% for SSVEPformer and FB-SSVEPformer, respectively. Besides, when the number of the data blocks increases from one to ﬁve, the accuracies incease by 2.72% and 2.36% for the two methods, respectively. These results show that the proposed models can achieve satisfactory performance when only a small amount of data are available for subject-adaptive classiﬁcation.

| | |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |
| | |

- 0
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11

(a) (b)

(c) (d)

- Figure 8: The t-SNE visualization results of a representative subject with the four models on Dataset 1. (a) EEGNet; (b) CCNN; (c) SSVEPformer; (d) FB-SSVEPformer. Each dot represents a sample data, and diﬀerent colors indicate the category to which the data belongs.

- 4.3. Model visualization and interpretation To further display the possible reasons that the proposed methods achieve

better results than the baseline methods, we adopted the t-Stochastic Neighborhood Embedding (t-SNE) to visualize the learned embedding features of the four deep learning methods that yield the top 4 accuracies, i.e, EEGNet, CCNN, SSVEPformer, FB-SSVEPformer. Owing to the large number of categories on Dataset 2 that is hard for plotting the results, we only present the experiment results on Dataset 1 in this section. Fig. 8 shows the visualization results of a representative subject(subject No.3) with the four models on Dataset 1. It can be seen that the features extracted by the proposed SSVEPformer and FB-SSVEPformer have smaller intra-category distance and larger

inter-category distance than those of the baseline methods, which can result in better classiﬁcation results.

The classiﬁcation mechanism of the deep learning model is still not as intuitive as the traditional machine learning method. So, the model interpretability is an important property for the deep learning method. In current study, we try to adopt the gradient-weighted Class Activation Mapping (grad-CAM) to investigate the interpretability of the SSVEPformer model [35]. Grad-CAM can visually demonstrate how the deep learning model makes the decision based on the input data. The higher the weights, the greater the contribution of the corresponding data of the input data to the result. Concretely, we calculated the heatmaps(weights) with the grad-CAM to represent the relevance of each position in the input data for the output of SSVEPformer encoder. Fig. 9 shows the grad-CAM visualization results of 11.75 Hz and 12.75 Hz for the representative subject (subject No.4) on Dataset 1, and 8.4 Hz and all 11.6 Hz for the representative subject (subject No.32) on Dataset 2. It can be observed that for both the real part and the imaginary part of the input data, the weights at the stimulation frequency and harmonics points are obviously higher than those of other frequency points. The results of grad-CAM prove that the SSVEPformer can ﬁnd the classiﬁcation features in the input data, and use the basic frequency information of the SSVEP data for classiﬁcation decisions.

- 4.4. Limitation Even though both SSVEPformer and FB-SSVEPformer achieve promising

performance, some limitations still exist in this study. First, we only used two public datasets to test the model, and more datasets such as BETA should be adopted in future experiments [24]. Second, although SSVEPformer and FBSSVEPformer were implemented in inter-subject scenarios, they still require a large amount of data from existing subjects for training. When only limited data are available, how to further compress the amount of training data while maintaining the model performance is a problem worthy of study. Besides, all experiments in this study are performed under oﬄine conditions, and future

Real par

Real par

| | | | | |
|---|---|---|---|---|

| | | | | |
|---|---|---|---|---|

1.0

1.0

0.8

0.8

- 0
- 1

0

0.6

0.6

Weigh

Weigh

Amplitude

Ampliude

0.4

0.4

−1

0.2

0.2

0.0

0.0

8 16 24 32 40 48 56 64

8 16 24 32 40 48 56 64

Frequency

Frequency

Imaginary par

Imaginary par

| | | | | |
|---|---|---|---|---|

| | | | | |
|---|---|---|---|---|

1.0

1.0

- 0
- 1

- 0
- 1

0.8

0.8

0.6

0.6

Weigh

Weigh

Ampliude

Ampliude

0.4

0.4

0.2

0.2

−1

−1

0.0

0.0

8 16 24 32 40 48 56 64

8 16 24 32 40 48 56 64

Frequency

Frequency

(a)

(b)

Real par

Real par

| | | | | |
|---|---|---|---|---|

| | | | | |
|---|---|---|---|---|

1.0

1.0

0.8

0.8

0

0.6

0.6

0

Weigh

Weigh

Ampliude

Ampliude

0.4

0.4

−1

0.2

0.2

−1

0.0

0.0

8 16 24 32 40 48 56 64

8 16 24 32 40 48 56 64

Frequency

Frequency

Imaginary par

Imaginary par

| | | | | |
|---|---|---|---|---|

| | | | | |
|---|---|---|---|---|

1.0

1.0

- 0
- 1

- 0
- 1

0.8

0.8

0.6

0.6

Weigh

Weigh

Ampliude

Ampliude

0.4

0.4

0.2

0.2

−1

−1

0.0

0.0

8 16 24 32 40 48 56 64

8 16 24 32 40 48 56 64

Frequency

Frequency

(c)

(d)

- Figure 9: Visualization results of SSVEPformer using grad-CAM, which represent the correlation of each position in the input data with the output of the SSVEPformer encoder. (a) and (b) are grad-CAM visualization results for 11.75 Hz and all 12.75 Hz, respectively, for the a representative subject in Dataset 1. (c) and (d) are grad-CAM visualization results for 8.4 Hz and 11.6 Hz, respectively, for the a representative subject in Dataset 2. The upper and lower subgraphs in (a), (b), (c) and (d) are the results of the real and imaginary parts of the input data, respectively. The yellow line represents the mean of real or imaginary amplitude in the input data of channel Oz. The blue line denotes the weights from the grad-CAM. The vertical red dotted lines indicate the positions fundamental frequency and harmonics.

work can further investigate the eﬃciency and eﬀectiveness in the online SSVEPbased BCI system.

- 5. Conclusion

In the case of time-consuming and laborious data collection, designing a model that can yield excellent classiﬁcation result under inter-subject conditions is a realistic requirement for SSVEP-based BCI systems. According to the structure of Transformer and the characteristics of SSVEP data, we proposed a SSVEPformer model and its variant FB-SSVEPformer with the ﬁlter bank techonolgy. To validate the model performance, we conducted extensive experiments on two public datasets under inter-subject conditions with data lengths ranging from 0.5 s to 1 s. Experimental results show that the proposed model outperforms three popular baseline methods on both datasets. The FBSSVEPformer model can achieve the best results. Furthermore, we used gradCAM to visualize the impact of diﬀerent locations of the input data on the output results, demonstrating the interpretability of the model. The proposed model has high interpretability, and holds promising potential to promote the practical applications of SSVEP-based BCI systems.

Acknowledgments

This work was supported in part by the National Natural Science Foundation of China under Grant No.62076209 and No.61871423.

References

- [1] Abiri, R., Borhani, S., Sellers, E.W., Jiang, Y., Zhao, X., 2019. A comprehensive review of EEG-based brain–computer interface paradigms. Journal of neural engineering 16, 011001.

- [2] Aznan, N.K.N., Atapour-Abarghouei, A., Bonner, S., Connolly, J.D., Breckon, T.P., 2021. Leveraging Synthetic Subject Invariant EEG Signals for Zero Calibration BCI, in: 2020 25th International Conference on Pattern Recognition (ICPR), IEEE. pp. 10418–10425.
- [3] Baldi, P., Sadowski, P.J., 2013. Understanding dropout. Advances in neural information processing systems 26.
- [4] Bin, G., Gao, X., Wang, Y., Li, Y., Hong, B., Gao, S., 2011. A highspeed BCI based on code modulation VEP. Journal of neural engineering 8, 025015.
- [5] Chen, X., Wang, Y., Gao, S., Jung, T.P., Gao, X., 2015a. Filter bank canonical correlation analysis for implementing a high-speed ssvep-based brain-computer interface. Journal of neural engineering 12, 046008.
- [6] Chen, X., Wang, Y., Nakanishi, M., Gao, X., Jung, T.P., Gao, S., 2015b. High-speed spelling with a noninvasive brain–computer interface. Proceedings of the national academy of sciences 112, E6058–E6067.
- [7] Chen, X., Wang, Y., Nakanishi, M., Jung, T.P., Gao, X., 2014. Hybrid frequency and phase coding for a high-speed SSVEP-based BCI speller, in: 2014 36th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, IEEE. pp. 3993–3996.
- [8] Collobert, R., Weston, J., Bottou, L., Karlen, M., Kavukcuoglu, K., Kuksa, P., 2011. Natural language processing (almost) from scratch. Journal of machine learning research 12, 2493–2537.
- [9] Craik, A., He, Y., Contreras-Vidal, J.L., 2019. Deep learning for electroencephalogram (EEG) classiﬁcation tasks: a review. Journal of neural engineering 16, 031001.
- [10] Devlin, J., Chang, M.W., Lee, K., Toutanova, K., 2018. Bert: Pretraining of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805 .

- [11] Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., et al.,

2020. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929 .

- [12] Du, X., Ma, C., Zhang, G., Li, J., Lai, Y.K., Zhao, G., Deng, X., Liu, Y.J., Wang, H., 2020. An eﬃcient LSTM network for emotion recognition from multichannel EEG signals. IEEE Transactions on Aﬀective Computing .
- [13] Du, Y., Liu, J., 2022. IENet: a robust convolutional neural network for EEG based brain-computer interfaces. Journal of Neural Engineering .
- [14] Guo, J.Y., Cai, Q., An, J.P., Chen, P.Y., Ma, C., Wan, J.H., Gao, Z.K.,

2022. A Transformer based neural network for emotion recognition and visualizations of crucial EEG channels. Physica A: Statistical Mechanics and its Applications 603, 127700.

- [15] Han, K., Wang, Y., Chen, H., Chen, X., Guo, J., Liu, Z., Tang, Y., Xiao, A., Xu, C., Xu, Y., Yang, Z., Zhang, Y., Tao, D., 2022. A survey on vision transformer. IEEE Transactions on Pattern Analysis and Machine Intelligence , 1–1doi:10.1109/TPAMI.2022.3152247.
- [16] Hendrycks, D., Gimpel, K., 2016. Gaussian error linear units (gelus). arXiv preprint arXiv:1606.08415 .
- [17] Hsu, H.T., Lee, I.H., Tsai, H.T., Chang, H.C., Shyu, K.K., Hsu, C.C., Chang, H.H., Yeh, T.K., Chang, C.Y., Lee, P.L., 2015. Evaluate the feasibility of using frontal SSVEP to implement an SSVEP-based BCI in young, elderly and ALS groups. IEEE Transactions on Neural Systems and Rehabilitation Engineering 24, 603–615.
- [18] Ibanez-Soria, D., Soria-Frisch, A., Garcia-Ojalvo, J., Ruﬃni, G., 2019. Characterization of the non-stationary nature of steady-state visual evoked potentials using echo state networks. PloS one 14, e0218771.

- [19] Krizhevsky, A., Sutskever, I., Hinton, G.E., 2017. Imagenet classiﬁcation with deep convolutional neural networks. Communications of the ACM 60, 84–90.
- [20] Lawhern, V.J., Solon, A.J., Waytowich, N.R., Gordon, S.M., Hung, C.P., Lance, B.J., 2018. EEGNet: a compact convolutional neural network for EEG-based brain-computer interfaces. Journal of neural engineering 15, 056013.
- [21] Lin, T., Wang, Y., Liu, X., Qiu, X., 2021. A survey of transformers. arXiv preprint arXiv:2106.04554 .
- [22] Lin, Z., Zhang, C., Wu, W., Gao, X., 2006. Frequency recognition based on canonical correlation analysis for SSVEP-based BCIs. IEEE transactions on biomedical engineering 53, 2610–2614.
- [23] Liu, B., Chen, X., Shi, N., Wang, Y., Gao, S., Gao, X., 2021. Improving the performance of individually calibrated SSVEP-BCI by task-discriminant component analysis. IEEE Transactions on Neural Systems and Rehabilitation Engineering 29, 1998–2007.
- [24] Liu, B., Huang, X., Wang, Y., Chen, X., Gao, X., 2020. BETA: A large benchmark database toward SSVEP-BCI application. Frontiers in neuroscience 14, 627.
- [25] M¨uller-Putz, G.R., Scherer, R., Brauneis, C., Pfurtscheller, G., 2005. Steady-state visual evoked potential (SSVEP)-based communication: impact of harmonic frequency components. Journal of neural engineering 2, 123.
- [26] Nakanishi, M., Wang, Y., Chen, X., Wang, Y.T., Gao, X., Jung, T.P., 2017. Enhancing detection of SSVEPs for a high-speed brain speller using taskrelated component analysis. IEEE Transactions on Biomedical Engineering 65, 104–112.

- [27] Nakanishi, M., Wang, Y., Wang, Y.T., Jung, T.P., 2015. A comparison study of canonical correlation analysis based methods for detecting steadystate visual evoked potentials. PloS one 10, e0140703.
- [28] Nakanishi, M., Wang, Y., Wang, Y.T., Mitsukura, Y., Jung, T.P., 2014. A high-speed brain speller using steady-state visual evoked potentials. International journal of neural systems 24, 1450019.
- [29] Pan, J., Gao, X., Duan, F., Yan, Z., Gao, S., 2011. Enhancing the classiﬁcation accuracy of steady-state visual evoked potential-based brain–computer interfaces using phase constrained canonical correlation analysis. Journal of neural engineering 8, 036027.
- [30] Phan, H., Mikkelsen, K., Ch´en, O.Y., Koch, P., Mertins, A., De Vos, M.,

2022. SleepTransformer: Automatic sleep staging with interpretability and uncertainty quantiﬁcation. IEEE Transactions on Biomedical Engineering 69, 2456–2467.

- [31] Qin, K., Wang, R., Zhang, Y., 2021. Filter Bank-Driven Multivariate Synchronization Index for Training-Free SSVEP BCI. IEEE Transactions on Neural Systems and Rehabilitation Engineering 29, 934–943. doi:10.1109/TNSRE.2021.3073165.
- [32] Ravi, A., Beni, N.H., Manuel, J., Jiang, N., 2020. Comparing userdependent and user-independent training of CNN for SSVEP BCI. Journal of neural engineering 17, 026028.
- [33] Regan, D., 1989. Evoked potentials and evoked magnetic ﬁelds in science and medicine. Human brain electrophysiology , 59–61.
- [34] Schmidhuber, J., 2015. Deep learning in neural networks: An overview. Neural networks 61, 85–117.
- [35] Selvaraju, R.R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., Batra, D., 2017. Grad-cam: Visual explanations from deep networks via gradient-

- based localization, in: Proceedings of the IEEE international conference on computer vision, pp. 618–626.
- [36] Tay, Y., Bahri, D., Metzler, D., Juan, D.C., Zhao, Z., Zheng, C., 2021. Synthesizer:rethinking self-attention for transformer models, in: International conference on machine learning, PMLR. pp. 10183–10192.
- [37] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., Polosukhin, I., 2017. Attention is all you need, in: Advances in neural information processing systems, pp. 6000–6010.
- [38] Vig, J., 2019. A multiscale visualization of attention in the transformer model. arXiv preprint arXiv:1906.05714 .
- [39] Wang, Y., Chen, X., Gao, X., Gao, S., 2016. A benchmark dataset for SSVEP-based brain-computer interfaces. IEEE Transactions on Neural Systems and Rehabilitation Engineering 25, 1746–1752.
- [40] Wang, Y., Wang, R., Gao, X., Hong, B., Gao, S., 2006. A practical VEPbased brain-computer interface. IEEE Transactions on neural systems and rehabilitation engineering 14, 234–240.
- [41] Waytowich, N., Lawhern, V.J., Garcia, J.O., Cummings, J., Faller, J., Sajda, P., Vettel, J.M., 2018. Compact convolutional neural networks for classiﬁcation of asynchronous steady-state visual evoked potentials. Journal of neural engineering 15, 066031.
- [42] Wolpaw, J.R., 2007. Brain-computer interfaces (BCIs) for communication and control, in: Proceedings of the 9th international ACM SIGACCESS conference on Computers and accessibility, pp. 1–2.
- [43] Wolpaw, J.R., Birbaumer, N., McFarland, D.J., Pfurtscheller, G., Vaughan, T.M., 2002. Brain-computer interfaces for communication and control. Clinical neurophysiology 113, 767–791.

- [44] Xie, J., Zhang, J., Sun, J., Ma, Z., Qin, L., Li, G., Zhou, H., Zhan, Y., 2022. A Transformer-Based Approach Combining Deep Learning Network and Spatial-Temporal Information for Raw EEG Classiﬁcation. IEEE Transactions on Neural Systems and Rehabilitation Engineering 30, 2126–2136.
- [45] Xu, J., Sun, X., Zhang, Z., Zhao, G., Lin, J., 2019. Understanding and improving layer normalization. Advances in Neural Information Processing Systems 32.
- [46] Yan, W., Wu, Y., Du, C., Xu, G., 2022. Cross-subject spatial ﬁlter transfer method for SSVEP-EEG feature recognition. Journal of Neural Engineering 19, 036008.
- [47] Yao, D., Zhang, Y., Liu, T., Xu, P., Gong, D., Lu, J., Xia, Y., Luo, C., Guo, D., Dong, L., et al., 2020. Bacomics: a comprehensive cross area originating in the studies of various brain–apparatus conversations. Cognitive Neurodynamics 14, 425–442.
- [48] Yao, H., Liu, K., Deng, X., Tang, X., Yu, H., 2022. FB-EEGNet: A fusion neural network across multi-stimulus for SSVEP target detection. Journal of Neuroscience Methods 379, 109674.
- [49] Yu, W., Luo, M., Zhou, P., Si, C., Zhou, Y., Wang, X., Feng, J., Yan, S.,

2022. Metaformer is actually what you need for vision, in: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 10819–10829.

- [50] Zerafa, R., Camilleri, T., Falzon, O., Camilleri, K.P., 2018a. To train or not to train? A survey on training of feature extraction methods for SSVEP-based BCIs. Journal of Neural Engineering 15, 051001.
- [51] Zerafa, R., Camilleri, T., Falzon, O., Camilleri, K.P., 2018b. To train or not to train? A survey on training of feature extraction methods for SSVEP-based BCIs. Journal of Neural Engineering 15, 051001.

- [52] Zhang, K., Robinson, N., Lee, S.W., Guan, C., 2021a. Adaptive transfer learning for eeg motor imagery classiﬁcation with deep convolutional neural network. Neural Networks 136, 1–10.
- [53] Zhang, X., Chang, D., Qi, W., Zhan, Z., 2021b. A study on diﬀerent functionalities and performances among diﬀerent activation functions across diﬀerent ANNs for image classiﬁcation. Journal of Physics: Conference Series 1732, 012026.
- [54] Zhang, X., Yao, L., Wang, X., Monaghan, J., Mcalpine, D., Zhang, Y., 2021c. A survey on deep learning-based non-invasive brain signals: recent advances and new frontiers. Journal of Neural Engineering 18, 031002.
- [55] Zhang, Y., Guo, D., Li, F., Yin, E., Zhang, Y., Li, P., Zhao, Q., Tanaka, T., Yao, D., Xu, P., 2018. Correlated component analysis for enhancing the performance of SSVEP-based brain-computer interface. IEEE Transactions on Neural Systems and Rehabilitation Engineering 26, 948–956.
- [56] Zhang, Y., Xu, P., Liu, T., Hu, J., Zhang, R., Yao, D., 2012. Multiple frequencies sequential coding for SSVEP-based brain-computer interface. PLoS ONE 7, e29519.
- [57] Zhang, Y., Yin, E., Li, F., Zhang, Y., Guo, D., Yao, D., Xu, P., 2019. Hierarchical feature fusion framework for frequency recognition in SSVEPbased BCIs. Neural Networks 119, 1–9.
- [58] Zhao, D., Wang, T., Tian, Y., Jiang, X., 2021. Filter Bank Convolutional Neural Network for SSVEP Classiﬁcation. IEEE Access 9, 147129–147141.
- [59] Zhong, P., Wang, D., Miao, C., 2020. EEG-based emotion recognition using regularized graph neural networks. IEEE Transactions on Aﬀective Computing .
- [60] Zhou, M., Tian, C., Cao, R., Wang, B., Niu, Y., Hu, T., Guo, H., Xiang, J.,

2018. Epileptic seizure detection based on EEG signals and CNN. Frontiers in neuroinformatics 12, 95.

