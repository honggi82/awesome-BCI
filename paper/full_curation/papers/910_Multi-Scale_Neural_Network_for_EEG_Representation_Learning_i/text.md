## Multi-Scale Neural Network for EEG Representation Learning in BCI

Wonjun Ko, Eunjin Jeon, Seungwoo Jeong, and Heung-Il Suk, Member, IEEE

### arXiv:2003.02657v1[eess.SP]2Mar2020

Abstract—Recent advances in deep learning have had a methodological and practical impact on brain–computer interface (BCI) research. Among the various deep network architectures, convolutional neural networks (CNNs) have been well suited for spatio-spectral-temporal electroencephalogram (EEG) signal representation learning. Most of the existing CNN-based methods described in the literature extract features at a sequential level of abstraction with repetitive nonlinear operations and involve densely connected layers for classiﬁcation. However, studies in neurophysiology have revealed that EEG signals carry information in different ranges of frequency components. To better reﬂect these multi-frequency properties in EEGs, we propose a novel deep multi-scale neural network that discovers feature representations in multiple frequency/time ranges and extracts relationships among electrodes, i.e., spatial representations, for subject intention/condition identiﬁcation. Furthermore, by completely representing EEG signals with spatio-spectral-temporal information, the proposed method can be utilized for diverse paradigms in both active and passive BCIs, contrary to existing methods that are primarily focused on single-paradigm BCIs. To demonstrate the validity of our proposed method, we conducted experiments on various paradigms of active/passive BCI datasets. Our experimental results demonstrated that the proposed method achieved performance improvements when judged against comparable state-of-the-art methods. Additionally, we analyzed the proposed method using different techniques, such as PSD curves and relevance score inspection to validate the multi-scale EEG signal information capturing ability, activation pattern maps for investigating the learned spatial ﬁlters, and t-SNE plotting for visualizing represented features. Finally, we also demonstrated our method’s application to real-world problems.

Index Terms—Active/Passive Brain–Computer Interface; Electroencephalogram; Deep Learning; Convolutional Neural Network; Motor Imagery; Steady-State Visually Evoked Potentials; Mental Fatigue; Seizure

I. INTRODUCTION

# B

RAIN–computer interface (BCI) [1] is an emerging technology that enables a communication pathway between

a user and an external device (e.g., a computer) through the acquisition and analysis of brain signals. Then these signals are translated into commands that are understood by a device, such as a computer. Owing to its practicality, electroencephalogram (EEG)-based non-invasive BCIs are widely used [1]–[3]. Earlier, Aric`o et al. [4] categorized user-centered BCIs into two types, active/reactive and passive BCIs. In this paper, our focus is not only on active BCIs but also on passive BCIs. Generally, two types of brain signals such as evoked and spontaneous EEG are primarily considered for active/reactive

W. Ko, E. Jeon, and H.-I. Suk are with the Department of Brain and Cognitive Engineering, Korea University, Seoul 02841, Korea. S. Jeong and H.-I. Suk are with the Department of Artiﬁcial Intelligence, Korea University, Seoul 02841, Korea. Correspondence: hisuk@korea.ac.kr (Heung-Il Suk)

BCIs [5]. Evoked BCIs exploit unintentional electrical potentials reacting to external or internal stimuli. Examples of evoked BCIs include steady-state visually evoked potentials (SSVEP) [6], [7] and event-related potentials [6]. Additionally, spontaneous BCIs use an internal cognitive process such as event related desynchronization and event related synchronization (ERD/ERS) in sensorimotor rhythms, e.g., motor imagery (MI) [6], [8] induced by imagining movements in addition to physical movement. Well-known examples of passive BCIs include the use of sleep/drowsy EEG signals for sleep stage classiﬁcation or identifying mental fatigue to alert a driver of a dangerous situation and seizure EEG patterns for onset detection to provide the patient with a warning of a potential seizure.

Generally, machine learning-based BCIs consist of ﬁve main processing stages [3]: (i) an EEG signal acquisition phase based on each paradigm, (ii) signal preprocessing (e.g., channel selection and band-pass ﬁltering), (iii) feature representation learning, (iv) classiﬁer learning, and ﬁnally (v) a feedback stage. Basically, most of machine learning-based BCI methods follow these processes, however, these methods need speciﬁc modiﬁcation to classify a user’s intention/condition for each different paradigm [3]. In other words, machine learningbased methods need to have prior knowledge of different EEG paradigms [1], [3], [6], [7], [11]. Therefore, conventional machine learning-based BCIs have discovered EEG representations through extremely specialized approaches, e.g., a common spatial pattern (CSP) [1] or its variants [12], [13] for MI signals and a canonical correlation analysis (CCA) [7] for SSVEP signals decoding.

While hand-crafted feature representation learning has a pivotal role in a conventional machine learning framework [1], [7], [14], deep learning-based representation has had remarkable results in the BCI community [2], [3], [5]. These deep learning-based methods have integrated a feature extraction step with a classiﬁer learning step such that those steps are jointly optimized, thereby improving performance. Among various deep learning methods, convolutional neural networks (CNNs) have the advantage [3], [15], [16] of maintaining the structural and conﬁgurational information in the original data. In this respect, developing a novel CNN architecture for EEG signal representation has taken a center stage in the BCI studies [2], [15], [17]–[23].

However, some challenges still remain. First, existing CNNbased methods [2], [15], [17], [18], [22], [23] are mostly comprised of stacked convolutional layers. In other words, those existing methods extract features sequentially. But, ignoring multiple ranges of spectral-temporal features can cause

158

𝜇V /Hz(dB)

135

5 10 15 20 25 30 35 40

5 10 15 20 25 30 35 40

Frequency (Hz)

Frequency (Hz)

Fig. 1: Power spectral density (PSD) curves of two different subjects’ MI EEG samples. The solid red line denotes the mean PSD and the shaded region exhibits the standard deviation for all trials. Clearly, these two different subjects show quite different PSD patterns for the same paradigm (motor imagery).

scale spatio-spectral-temporal features. Section IV presents experimental settings and results by comparing the proposed method and comparable baselines. In Section V, we analyze our proposed method from several points of view. Finally, Section VI summarizes the proposed study and suggest future research directions.

II. RELATED WORK

Learning a class-discriminative feature representation of EEG is still challenging in both theory and practice. Numerous prior studies have attempted to extract features from EEGs. In this section, we brieﬂy discuss linear methods and deep learning models used for EEG signal representation.

a critical problem because EEG signal features for different subjects [24], paradigms [3], and types [4] are found in diverse ranges. For example, Fig. 1 depicts two different subjects’ MI EEG power spectral density (PSD) curves. Clearly, these two plots have different distributions from each other even though these PSDs are estimated by the same task. Therefore, it is important to capture multi-scale spectral information in EEGs for general use in BCI, i.e., a generic method applicable to various types of BCIs.

In addition, those stacked CNN-based methods [2], [15], [22], [23] have numerous trainable parameters, thus requiring large amounts of training samples, whereas BCIs generally acquire a limited number of EEG trials [24]. Therefore, generalizing conventional stacked CNN-based methods in BCI is quite difﬁcult because deep learning is a data-hungry problem, i.e., rarely generalized with a lack of data.

Finally, interpreting a learned stacked CNN from a neurophysiologically appropriate standpoint [25] is quite complicated because the CNN identiﬁes complex patterns of data in latent space making a direct explanation difﬁcult [25].

In this study, we propose a novel deep learning-based BCI method to mitigate the previously discussed difﬁculties. The main contributions of our study are as follows:

- • First, we propose a novel CNN architecture, that is applicable independently from the input paradigm or type of EEG and can represent multi-scale spatio-spectraltemporal features.
- • Second, the proposed method achieved positive performance on ﬁve different datasets for four differnt paradigms (two for active BCIs and two for passive BCIs). The proposed method outperformed or was similar to state-of-the-art linear and deep learning methods, which were individually designed for each speciﬁc paradigm.
- • Last, we analyze the proposed network using a variety of techniques.

The rest of this paper is organized as follows: Section II reviews previous research on various EEG representation learning via linear model-based or deep learning-based methods. In Section III, we propose a novel and compact deep CNN that classiﬁes multi-paradigm EEG by representing multi-

A. Linear Models

Over the past decades, CSP [1] and its variants [12], [13] have played an essential role in decoding MI. Blankertz et al. [1] and Ang et al. [13] independently used a spatial ﬁltering-based method for classifying MI. Ang et al. [13] band-pass ﬁltered EEG data before applying CSP, thereby attempting to decode EEG signals in a spatio-spectral manner. They named the proposed method ﬁlter bank CSP (FBCSP). Furthermore, Suk and Lee [12] also decoded MI by jointly optimizing multi spectral ﬁlters in a Bayesian framework.

CCA is commonly utilized for detecting SSVEP [7] owing to its practical ability to be implemented without the calibration stage. The standard CCA method [7] deployed sinusoidal signals as reference signals and estimated canonical correlation between the reference signals and input EEG signals to identify an evoked frequency in SSVEP EEGs.

In addition, to characterize the sleep stage, entropy calculation-based approaches were frequently used. Sanders et al. [26] classiﬁed the sleep stage using the spectral-temporal features of EEGs learned from short-time Fourier transformation. Furthermore, Zheng and Lu [10] focused on identifying a driver’s mental fatigue during driving. They [10] applied ﬁlter banks to EEG signals to extract spectral information, and then transformed the ﬁltered EEG signals to spectral space, i.e., estimated PSD of ﬁltered EEG signals. By doing so, Zheng and Lu [10] effectively assessed the regression score of the driver’s mental states which were labeled using the PERCLOS index, a measure of neurophysiological fatigue.

Earlier, Shoeb and Guttag [14] applied a machine learning approach to extract and classify the spatio-spectral-temporal features of epileptic seizure EEG signals. Speciﬁcally, these authors [14] used ﬁlter banks in a channel-wise manner to capture the spatio-spectral information. Then, by encoding the temporal evolution of extracted spatio-spectral feature vectors, they [14] effectively constructed epileptic seizure EEG signal spatio-spectral-temporal features and classiﬁed the seizure and non-seizure features utilizing a support vector machine (SVM). Recently, spectral features derived from a principal component analysis (PCA) [27] exhibited superior performance for seizure onset detection. In particular, Lee et al. [27] band-pass ﬁltered raw signals and calculated PSD. Then they [27] applied PCA for the extraction of EEG signal spectral features.

These practical linear model-based BCI methods [1], [7], [10], [12], [13], [26], [27] have demonstrated credible performance. However, these methods need to have certain prior neurophysiology knowledge [3], because their feature extraction stages are speciﬁcally designed for each EEG paradigm. Conversely, our method does not need to be specialized for different paradigms.

An input EEG signal 𝐱

1×(𝑓 /2) Conv, lReLU, 𝐹

|Spectral-TemporalFeature<br><br>RepresentationBlock|
|---|

Spectral-TemporalFeature

RepresentationBlock

1×𝑇 SepConv, lReLU, 𝐹

|SpatialFeature RepresentationBlock|
|---|

1×𝑇 SepConv, lReLU, 𝐹

𝑛 ×1 Conv, lReLU, 𝐹

SpatialFeature RepresentationBlock

B. Deep and Hierarchical Models

Recently, deep learning methods, especially CNNs have achieved promising results in EEG signal decoding researches. For instance, Schirrmeister et al. [2] introduced Shallow ConvNet, Deep ConvNet, Hybrid ConvNet, and Residual ConvNet. These authors [2] evaluated how well various proposed CNNs decoded MI. Ko et al. [15] also proposed a novel CNN architecture which is inspired by a recurrent convolutional neural network [28] for MI classiﬁcation, deep recurrent spatio-temporal neural network (RSTNN).

1×𝑇 SepConv, lReLU, 𝐹

𝑛 ×1 Conv, lReLU, 𝐹

𝑛 ×1 Conv, lReLU, 𝐹

|ClassificationBlock|
|---|

Concatenation

ClassificationBlock

Global Average Pooling

While a standard CCA [7] has obtained state-of-the-art performance in SSVEP BCI, Kwak et al. [20] developed a CNN for SSVEP feature representation learning. These authors simply combined spatial and temporal convolution to enable the system to learn data patterns in the latent space, thereby correctly generalizing EEG signal features. Meanwhile, Waytowich et al. [19] applied EEGNet [3] to the SSVEP paradigm and achieved a higher performance than that of the standard CCA [7].

Dense, Softmax, 𝑛

A	prediction of	a user s intention or	condition 𝐲

Fig. 2: Architectural framework of our multi-scale neural network (MSNN). In the proposed network, ﬁrst, an input EEG x is temporally convolved to expand the number of features, where fs, F0, lReLU denote the sampling frequency rate, the number of output ﬁlter maps of the ﬁrst layer, and leaky rectiﬁed linear unit activation function respectively. Then, a set of temporal separable convolutions extracts spectral-temporal features (Tk and Fk respectively denote the kernel size and output feature maps of k-th temporal separable convolution). At the same time, a set of spatial convolutions represents spatial features, where nc denotes the number of acquired EEG channels. Then, the multi-scale features are concatenated and fed into the global average pooling layer [29]. Finally, the dense layer classiﬁes the class of input EEG by exploiting multi-scale features where no denotes the number of output nodes.

Supratak et al. [17] developed a deep neural network for sleep stage detection. More precisely, they combined a CNN for representation learning and a recurrent neural network for sequential residual learning [17]. Furthermore, they trained the deep learning model in two separate steps, optimizing the model by individual pre-training and ﬁne-tuning. In the meantime, Gao et al. [23] proposed an EEG-based spatiotemporal convolutional neural network (ESTCNN) for driver fatigue evaluation. The ESTCNN [23] simply convolved the band-pass ﬁltered EEG to represent temporal dependencies and ﬂattened the extracted features for spatial features fusion. Lastly, densely connected layers were used for the identiﬁcation of a user’s condition [23].

To detect a seizure type, Asif et al. [21] proposed a multispectral deep feature learning using a deep CNN, SeizureNet. These authors [21] transformed the EEG signals to spectral space using saliency-encoded spectrogram generation and fed the extracted spectral features to a deep neural network. In the meantime, Emami et al. [22] independently proposed another CNN-based approach for detecting seizure onset. They [22] band-pass ﬁltered and segmented the input EEG patterns, and then used a deep CNN for classiﬁcation.

stage for their respective paradigm [2], [15], [17], [20]–[23] or even various paradigms [3], [19]. On the other hand, the deep CNNs extracted the EEG features at a sequential level using stacked convolutional layers without exploiting multi-scale spectral representation. Conversely, the proposed method exploits multi-scale spatio-spectral-temporal features irrespective of the input EEG paradigms.

Recently, Lawhern et al. [3], [19] proposed a novel CNN, so-called EEGNet. Unlike other linear or deep learning-based methods, the EEGNet classiﬁed various EEG paradigms using a single architecture, i.e., not speciﬁcally tuned for different paradigms. Further, Lawhern et al. [3] introduced a separable convolution [16] and used it as a parameter reduction method.

III. METHODS

In this section, we propose a deep multi-scale neural network (MSNN), which can represent EEG features from different paradigms by exploiting spatio-spectral-temporal information at multi-scale.

On the one hand, the deep and hierarchical models decoded the EEG signals well without any custom feature extraction

- A. Multi-Scale Neural Network

As mentioned previously, an FBCSP [13] is one of the most successful models to exploit EEG signal multi-scale features, especially for MI. Thus, many successful MI EEG signal decoding algorithms [2], [12] or even other paradigm classiﬁcation algorithms [3] are inspired by the FBCSP [13] model. In this study, the proposed multi-scale neural network (MSNN) also learns multi-scale feature representations. However, the network automatically learns from data through discriminative multiple spectral ﬁlters, rather than manually deﬁning multi-frequency bounds as in FBCSP [13]. Basically, our proposed method consists of three types of blocks: (1) a spectral-temporal feature representation block, (2) a spatial feature representation block, and, (3) a classiﬁcation block, as depicted in Fig 2.

First, in the spectral-temporal feature representation block, stacked convolutional layers extract EEG data spectraltemporal features, such as existing EEG classiﬁcation methods. However, the proposed model exploits intermediate activations for gathering multi-scale spectral information. Then, the spatial feature representation block discovers spatial patterns from the extracted multi-scale features. Finally, these multi-scale spatio-spectral-temporal features are concatenated, pooled, and fed into the densely connected layer for classiﬁcation.

- B. Spectral-Temporal Feature Representation Block

Given an input EEG data x, we reshape it in the form of [nc,nT,1], i.e., x ∈ Rn

c×nt×1, where nc and nT denote the number of electrode channels and timepoints, respectively.

In the MSNN, the input EEG data are temporally convolved in a channel-wise manner by a temporal convolutional layer to expand the number of feature maps. Thus, the activated features have the form [nc,n T,F0], where n T = nT −(fs/2)+1 (fs and F0 are the sampling frequency and the feature map dimension for the ﬁrst temporal convolution layer.). The main beneﬁts of using a separable convolution [3], [16] are a signiﬁcant reduction of tunable weights in the model and, more importantly, an efﬁcient and explicit decoupling of the relationship between the temporal and the feature map dimensions of the input features. This is accomplished by learning kernels independently for each feature map. Thus, as in BCI literature, the separable convolution [16] enables the system to learn temporal kernels individually from the feature map dimensions (using a depthwise convolution [16]), and then optimally re-combine the feature maps (using a pointwise convolution [16]).

In this block, by setting a kernel size of (1 × Tk), where Tk denotes the kernel size of the k-th temporal separable convolution, the k-th temporal separable convolutional layer

represents EEG signal features in the range of Tk/f s sec, hence, f s/Tk Hz, where f s is a frequency property extracted at the ﬁrst temporal convolutional layer. Therefore, the spectraltemporal feature representation layers can deal with different timepoints or frequency ranges by using various kernel sizes for the input EEG data.

Additionally, each different layer that has a different kernel size extracts features in different frequency and timepoint ranges. In other words, a spectral-temporal convolution layer with a larger kernel represents longer-term temporal features, i.e., a lower-range of spectral features and vice versa. Then, the MSNN exploits intermediate activations from each layer, thus learning multi-scale feature representations.

In addition, a separable convolution [16] only operates convolutions in a cross-nT way, thus, the number of parameters is small compared to a conventional convolution. For instance, while a k-th separable temporal convolution has only Tk + Fk−1 · Fk parameters, the conventional convolution with the same size kernel has Tk · Fk−1 · Fk parameters, where Fk denotes the feature maps dimension of k-th layer.

Furthermore, in this processing, as described above, the MSNN uses its intermediate activations to exploit multi-scale representations. In other words, the proposed network obtains N numbers of spectral-temporal features fkST, k = 1,2,··· ,N like:

#### fkST = CkST(x) = Cksep ◦ Cksep−1 ◦ ··· ◦ C0(x), (1)

where Cksep, C0, and Fi ◦ Fj, respectively, denote the kth separable convolution, the ﬁrst temporal convolution, and

a function composition between arbitrary functions Fi and Fj, i.e., Fi ◦ Fj(·) = Fi(Fj(·)). Thus, by extracting features f1ST,f2ST,··· ,fNST, the MSNN effectively represents the spectral-temporal features from the multi-scale viewpoint, thereby automatically enhancing generalization. In addition, as all inputs are zero-padded before each separable temporal convolution, the output features have the same dimension for the channels and timepoints, except for the feature map dimension. Thus, the k-th spectral-temporal feature fkST now has the form [nc,n T,Fk].

C. Spatial Feature Representation Block

In the spatial feature representation block, a common spatial convolution is used for feature extraction. In this block, the kernel size is constrained to be equal to the number of EEG channels, hence, a convolution with a kernel of (nc × 1) is used. Additionally, by setting the kernel size to be the same as the number of electrode channels, similar to many existing deep learning-based BCI methods [2], [3], [15], the proposed MSNN extracts spatial information from the original EEG acquisition channel distributions of multi-scale spectral temporal features. Then, the MSNN can obtain neurophysiologically plausible information from the input data distribution.

Furthermore, the spatial feature representation can be applied unrestrictedly, thus in the proposed method, we add this block after every extracted spectral-temporal features fkST, k = 1,2,··· ,N like,

fkSST = Sk(fkST) = Sk ◦ CkST(x), (2) where Sk denotes the k-th spatial convolution and fkSST is spatio-spectral-temporal features estimated by the Sk and CkST. We use valid paddings for every spatial convolution, thus the k-th spatio-spectral-temporal feature fkSST has the form [1,n T,Fk]. By setting the number of spatial convolutions to be identical to the number of spectral-temporal convolutions,

unlike many previous researches using deep learning for BCI [2], [3], [15], [17], [21], we extract spatial features of each range from spectral-temporal features. In other words, unlike many previous stacked CNNs, the proposed architecture uses every intermediate activated feature set to exploit spatial information, thereby creating the capability to extract various ranges of EEG features at multi-scale.

D. Classiﬁcation Block

For classiﬁer learning, because we have N numbers of different (or same when F1 = F2 = ··· = FN) size of spatiospectral-temporal features fkSST, k = 1,2,··· ,N, the classiﬁer in the proposed method has to concatenate the features in the feature map dimension. Thus, the concatenated feature fconcatSST is represented as:

fconcatSST =

N

fiSST =

i=1

N

Si ◦ CiST(x), (3)

i=1

where denotes the concatenation operation.

For the classiﬁer network, let us assume that the number of output classiﬁcation nodes is denoted by no and we use a single linear mapping layer. Then, we need to train the large

number of Ni=1 no·n T ·Fi parameters (note that we disregard the bias term for a convenient calculation) because fconcatSST has the form [1,n T, Ni=1 Fi], and it would still require a large number of training samples. Therefore, after representing the input EEG data multi-scale spatio-spectral-temporal features, the proposed MSNN has one extra operation for reducing the trainable weights. Unlike the existing deep learning-based BCI methods [2], [3], [15], [17], [20], [21], global average pooling (GAP), which is widely used in the computer vision ﬁeld [29] is performed.

The GAP layer [29], a type of pooling layer, averages nodes from each feature map, thus eliminating the requirement for any window size or stride. By applying GAP [29], our proposed MSNN efﬁciently extracts signiﬁcant features. From the BCI literature, the GAP layer [29] can be understood to be a method that can emphasize an important frequency range and its surrounding area for each feature map dimension. Thus, for the extracted multi-scale features in the MSNN, the GAP layer [29] stresses the crucial spectral-temporal part resulting in concise information for the ﬁnal decision making.

Additionally, the GAP layer [29] signiﬁcantly reduces the number of classiﬁer parameters used in the proposed MSNN. Speciﬁcally, after the GAP layer G(·), the extracted feature is reduced to the form [1,1, Ni=1 Fi], whereas the feature without GAP has the form [1,n T, Ni=1 Fi]. Therefore, we drastically suppress the trainable parameters in the classiﬁer from n T · no · Ni=1 Fi to no · Ni=1 Fi.

Then, the MSNN prediction, yˆ, for the input EEG data, x, is as follows:

yˆ = softmax W o · G fconcatSST + bo

N

Si ◦ CiST(x) + bo , (4)

= softmax W o · G

i=1

N

o respectively denote the weight matrix and bias of the classiﬁer.

where Wo ∈ R

i=1 Fi×n0 and b0 ∈ Rn

Finally, the cross-entropy loss, L, that is used for network training is calculated by the prediction yˆ and the label y:

B

y(b) log yˆ(b), (5)

L = CE(y,yˆ) = −

b=1

where B and CE(·,·) respectively denote the mini-batch sizes and the cross-entropy loss function, and yˆ(b) and y(b) denote the prediction and ground-truth label for the b-th training sample in the mini-batch1.

IV. EXPERIMENTS

In this section, we describe the datasets used for performance evaluation, our experimental settings, and baseline settings. Furthermore, we present the performance of our method and competing methods.

A. Datasets and Preprocessing

In this study, we used ﬁve different publicly available datasets to validate the proposed method on four different EEG data paradigms.

- 1) Motor Imagery: First, we used two big datasets for MI

EEGs, GIST-MI [8]2 and KU-MI [6]3,4. The GIST-MI [8] dataset consists of two different MI tasks: left-hand and righthand MI that are acquired from 52 subjects. All EEG signals were recorded from 64 Ag/AgCl electrode channels according to the standard 10-20 system, sampled at 512Hz. Each class contained 100 or 120 trials, and each trial was a 3 sec long MI task. Because this dataset is not separated into training and test samples, we conducted a ﬁve-fold cross-validation for a fair evaluation. For the MI datasets, we preprocessed signals by applying a large Laplacian ﬁltering5, baseline correction by subtracting the mean value of the ﬁxation signal from each MI trial, and band-pass ﬁltering between 4 and 40Hz. Then, we removed the ﬁrst and last 0.5 sec from each trial, and ﬁnally applied Gaussian normalization. We applied the same mean and standard deviation values for normalization to the test samples. The multi-channel EEG signals were only shifted and scaled by their respective channel-wise mean and standard deviation values. Thus, inter-channel relations inherent in the data were preserved.

- 2) Steady-State Visually Evoked Potentials: We also used

the KU-SSVEP dataset [6]3 for SSVEP decoding experiments in this study. This KU-SSVEP dataset [6] was acquired from 54 subjects and recorded from 62 Ag/AgCl electrode channels using the 10-20 system. The KU-SSVEP dataset [6] contains four EEG classes from target stimuli at 5.45, 6.67, 8.57,

- 1All codes used in our experiments are available at ‘https:

//github.com/DeepBCI/Deep-BCI/tree/master/1 Intelligent BCI/Multi Scale Neural Network for EEG Representation Learning in BCI.’

- 2Available at http://gigadb.org/dataset/100295
- 3Available at http://gigadb.org/dataset/100542 4Experimental results of the KU-MI dataset [6] are reported in Supplemen-

tary B.

5When the target channel does not have four nearest neighbors, we just used available channels and their average value to ﬁlter the target channel.

and 12Hz, and each class has 25 EEG trials of training and testing samples for each session. We preprocessed the SSVEP signals by applying band-pass ﬁltering between 4 and 15Hz and selected eight channels in the occipital region, ‘PO3, POz, PO4, PO9, O1, Oz, O2, and PO10,’ because this region is widely used for SSVEP classiﬁcation [19].

- 3) Drowsiness: With respect to passive BCI [4], we con-

sidered two different paradigms, seizure EEG signals [11] and vigilance EEG signals [10]. Owing to its theoretical and practical beneﬁts, in this study, we conducted experiments identifying drivers’ mental fatigue. We also used a publicly available SEED-VIG EEG dataset [10]6 for the drowsy driving task data. This dataset [10] consists of 23 experiments, i.e., trials, and each trial is recorded for approximately 2 hours while simulated driving occurs. The EEG signals are acquired from 17 electrode channels according to the 10-20 system and sampled at 200Hz [10]. For this dataset, we band-pass ﬁltered EEG signals in the range between 0.5 and 40Hz, each epoch was 8 sec in length. Because the dataset was originally labeled using PERCLOS levels [10], we categorized the label vectors into three classes, awake, tired, and drowsy with two threshold values(0.35 and 0.7) [10]. Then, for every 23 experiments, a ﬁve-fold cross-validation was used for performance estimations.

- 4) Seizure: Finally, we conducted seizure onset detection

experiments with the widely used and publicly available CHBMIT [11]7 dataset. The CHB-MIT dataset [11] contains EEG data from 24 subjects sampled at 256Hz acquired from 23 electrode channels (24 or 26 in a few cases) according to the 10-20 system. In this work, we selected EEG trials that have the same 23 channels montage and removed some trials acquired from the different montage. By following [14], we used a leave-one-record-out cross-validation. More precisely, we trained the proposed method using all non-seizure records and all seizure records but one, and tested the model on the remaining seizure record [14]. Then, we repeated this process for the number of seizure records in the dataset, thus, each seizure record was tested. For training, the test trial epochs were 10 sec in length. During validation and testing session, a 10 sec length EEG signal was input into the proposed network using a 1/256 stride. Then, we observed whether the probability values for each EEG signal timepoint was ictal or normal.

For all datasets, the training samples were randomly selected and split again into training and validation samples for model selection. Speciﬁcally, we divided the training samples at a 9:1 ratio for each subject and used them for training and model selection respectively.

B. Experimental Settings

In our work, we compared our method with paradigmspeciﬁc linear model-based and deep learning-based methods for each EEG paradigm.

- 6Available at: http://bcmi.sjtu.edu.cn/seed/download.html
- 7Avaliable at: https://physionet.org/content/chbmit/1.0.0/

- 1) Linear Models - Motor Imagery: First, we built a CSP

with a linear discriminant analysis (CSP + LDA) [1] and an FBCSP with an LDA (FBCSP + LDA) [13] for MI decoding. We used four ﬁlters and regularized covariance for the CSP [1] and FBCSP [13]. Additionally, we also used nine nonoverlapped ﬁlter banks in the 4∼40Hz range, i.e., 4∼8, 8∼12, ···, 36∼40Hz, and, ﬁnally selected 10 features using the mutual information-based feature selection method FBCSP [13].

- 2) Linear Models - Steady-State Visually Evoked Potentials:

We also built a standard CCA [7] for SSVEP classiﬁcation. We set reference signals for each stimulus including second harmonics. Furthermore, the standard CCA [7] does not require training samples for the optimization, thus we only estimated each session in its entirety from the KU-SSVEP dataset [6] for the CCA performance estimation.

- 3) Linear Models - Drowsiness: For the drowsy state detec-

tion experiment, we estimated the ﬁlter-banked input EEG data PSD in a channel-wise manner for extracting spatio-spectral features and classiﬁed the learned features using an SVM with a radial basis function (RBF) kernel (γ = 1/dinput where dinput denotes the input feature dimension) [10].

- 4) Linear Models - Seizure: In addition, we also reimple-

mented Shoeb and Guttag [14]’s method for the seizure onset detection experiment. We applied the PSD to the EEG data in a channel-wise manner. Then, the 3 sec time window time evolution [14] method was used for capturing temporal information. Finally, the represented spatio-spectral-temporal features were fed into an SVM using an RBF kernel (γ = 1/dinput).

- 5) Deep Neural Networks - Motor Imagery: We also im-

plemented deep learning-based BCI models8 for MI. Basically, most of the existing deep learning models [2], [15], [22], [23] have focused on a paradigm-speciﬁc BCI task. However, we conducted experiments over all types of datasets for each deep learning model to demonstrate the validity of the proposed method. We built a Shallow ConvNet and a Deep ConvNet as proposed by Schirrmeister et al. [2]. The Shallow ConvNet [2] consists of two convolutions, temporal and spatial, with a squaring nonlinear activation, an average pooling, and a logarithmic activation. The Deep ConvNet [2] has ﬁve convolutions, temporal and spatial, and three additional temporal convolutions. The RSTNN [15] is also used for these experiments. This network [15] consists of three recurrent convolutional layers, and each recurrent convolutional layer has three recurrent temporal convolutions [28] with a spatial convolution.

- 6) Deep Neural Networks - Steady-State Visually Evoked

Potentials: For the SSVEP decoding experiment, we exploited another version of EEGNet for SSVEP EEG [19]. We used different kernel sizes for this EEGNet [19] as Waytowich et al. proposed. The SSVEP classiﬁcation performance estimated by this version [19] is marked by † in the classiﬁcation table.

- 7) Deep Neural Networks - Drowsiness: The ESTCNN [23]

which is proposed for mental fatigue classiﬁcation has three core blocks. Each block in the ESTCNN [23] consists of

8See ‘Appendix A: Architectural Details of Deep Models for BCIs’ for more detail architectures and learning schedules.

TABLE I: Performance evaluations. The Method column denotes all used classiﬁcation/detection methods including baselines and the proposed method on the various datasets, GIST-MI [8], KU-SSVEP [6], SEED-VIG [10], and CHB-MIT [11] EEG dataset. Each cell depicts the average performance and the standard deviation of all subjects (or trials for the SEED-VIG [10]). For classiﬁcation performance on the SSVEP dataset, we used different kernel sizes for EEGNet [19] and the proposed method. These values are marked by † and ‡, respectively.

|Method| |GIST-MI [8]<br><br>|KU-SSVEP [6]|SEED-VIG [10]<br><br>|CHB-MIT [11]|
|---|---|---|---|---|---|
| | |Classiﬁcation accuracy| |Number of false detections| |
| | |Mean±Std.| |Mean±Std. False Positive (Drowsy)|Mean (Mean latency)|
|CSP + LDA [1] FBCSP + LDA [13] CCA [7] PSD + SVM [10] Shoeb and Guttag [14]| |.66±.14 .68±.15 -|.94±.09 -<br><br>|- -<br>- -<br>- -<br><br><br>31.20±15.47 6.74<br><br>- -|5.35 (5.11)<br><br>|
|Shallow ConvNet [2] Deep ConvNet [2] RSTNN [15] ESTCNN [23] EEGNet [3], [19]| |.63±.11<br><br>.61±.07 .69±.12 .67±.10<br><br>.64±.07<br>|.52±.20 .96±.08 .65±.20 .79±.17<br><br>.93±.10†<br><br>|34.89±19.13 6.51 41.31±21.04 8.65 39.84±22.56 8.08 41.10±21.31 8.71 46.63±22.10 11.26|19.21 (8.48) 8.74 (7.52) 24.35 (9.31) 6.41 (7.01) 5.40 (6.23)<br><br>|
|MSNN (Proposed)| |.81±.12<br><br>|.93±.08‡|31.10±17.29 5.38|5.35 (4.98)|

three temporal convolutions with a max pooling layer with the exception of the last block that uses an average pooling layer instead of the max pooling.

- 8) Deep Neural Networks - Multi-paradigm: Finally, we

also implemented the EEGNet [3] in our study. As previously mentioned, we used different kernel sizes for two different EEGNets, [3] and [19]. Nevertheless, the basic architecture of the network was the same for various EEG paradigms, having a temporal convolution, depthwise spatial convolution [16], and separable temporal convolution [16].

- 9) Proposed Multi-Scale Neural Network: While training

our proposed network, depicted in Fig. 2, we set a minibatch size of 16, an exponentially decreasing learning rate (initial value: 0.03, decreasing ratio per epoch: 0.001), and an Adam optimizer. For the ﬁrst temporal convolution, we used a conventional temporal convolution with the kernel size of (1 × fs/2) and F0 = 4. Furthermore, we used three spectraltemporal feature representation convolutions, i.e., N = 3, and set T1 = 100, T2 = 60, and T3 = 20 with F1 = 16, F2 = 32, and F3 = 64. Then, for the spatial feature representation block, we used three spatial convolutions because the number of spatial convolutional layers must be the same

- as the number of spectral-temporal separable convolutional layers. The proposed method used different kernel sizes for the SSVEP dataset, similar to the EEGNet [19] due to the fact that SSVEP EEG data is created by target frequencies [6], [7]. For the KU-SSVEP dataset [6], we set T1 = 20, T2 = 10, and T3 = 5 for the spectral-temporal feature representation block, and used the same settings for the others. The SSVEP classiﬁcation performance estimated by this method is marked by ‡. Additionally, batch normalization was performed after every convolution. Finally, for the classiﬁcation block, all activated features from the spatio-spectral-temporal block were concatenated and fed into the GAP [29] layer. Then, after ﬂattening, the multi-scale features were linearly mapped by a dense layer. In this proposed network, a leaky rectiﬁed linear unit (ReLU) activation function, an L1-L2 regularizer

( 1 = 0.01 and 2 = 0.001), and a Xavier initializer [30] are used for all tunable parameters except for the ﬁnal

decision layer that is activated by a softmax activation function instead of a leaky ReLU. We selected model components that demonstrated the best performance for validation, i.e., model selection samples, as mentioned previously.

C. Experimental Results

- 1) Motor Imagery: All experimental results are summa-

rized in TABLE I. Our proposed network clearly outperformed other baselines for MI EEG signal decoding. Importantly, the proposed network achieved a higher accuracy than those methods designed speciﬁcally for MI classiﬁcation: CSP [1], FBCSP [13], Shallow ConvNet [2], Deep ConvNet [2], and RSTNN [15]. With this clear improvement in accuracy, we could expect that our proposed method is one step closer to MI-based BCI commercialization.

- 2) Steady-State Visually Evoked Potentials: Our proposed

MSNN achieved a slightly lower performance than CCA [7], Deep ConvNet [2], and EEGNet [19] in the SSVEP classiﬁcation. However, the difference in performance between our MSNN and the other three baselines, CCA [7], Deep ConvNet [2], and EEGNet [19], was reasonably small and the proposed method performed with a credible accuracy score.

- 3) Drowsiness: The proposed MSNN made the smallest

number of mistakes in decision making for passive BCI [4]. In particular, the proposed method detected a driver’s mental fatigue, i.e., drowsiness, from the EEG signals. Our proposed method predicted 31.10 incorrect trials from a total of 177 samples on average. Furthermore, accurately detecting a drowsy state is one of the most important MSNN capabilities for practical use. Our proposed model only made 5.38 mistakes out of 35 drowsy trials on average, thus exhibiting the highest precision score.

- 4) Seizure: Finally, the MSNN incorrectly identiﬁed 5.35

seizures among 178 total test seizure samples. Furthermore, our proposed network was the fastest for detecting seizures, i.e., it exhibited the shortest latency time (approximately 4.98 sec on average) among various methods. In other words, our proposed method demonstrated the best performance even with the shortest latency time. Additionally, the proposed model

range, not only in the frequency of interest. In other words, while other existing methods gather spatio-spectral-temporal information at the sequential level, the proposed network exploit multi-scale features, thereby improving learning ability9.

158

[Figure 1]

𝒢(𝐟 ) 𝒢(𝐟 ) 𝒢(𝐟 )

𝜇V /Hz(dB)

Subject 48

𝒢(𝐟 ) of subject 48

135

158

[Figure 2]

- B. Activation Patterns

Earlier, Haufe et al. [25] proposed an activation pattern which is based on a forward-backward modeling in signal processing. The activation pattern method [25] provides a way to interpret weight matrices in multivariate neuroimaging, as presented in the signal processing literature.

The proposed method, clearly, decodes the input EEG signal to the corresponding label, i.e., inferring a user’s intention or condition from an observed EEG pattern. Therefore, it is a backward process computational model. Hence, for a concrete and meaningful understanding of learned layers, it is essential to reverse this backward process model to a forward process. Finally, in this work, we estimated and visualized the activation patterns of the learned weights shown in Fig. 4a. We extracted the spatial convolutions of Shallow ConvNet [2], Deep ConvNet [2], RSTNN [15], EEGNet [3], and the proposed model. Then, we estimated activation patterns and visualized them in a topological manner. We do not estimate ESTCNN [23] activation patterns because the ESTCNN [23] does not have any spatial feature representation layers and those visualized patterns are estimated by the ﬁrst subject’s ﬁrst fold data in the GIST-MI dataset [8]. Finally, we normalized the activation patterns in [0, 1] range before visualization.

In this investigation, we observed right-lateralized brain activation/deactivation patterns, and the same patterns in the left hemisphere when a user imagined the movement of lefthand and right-hand respectively. Furthermore, the proposed model shows relatively clearer patterns than the other models, thus, we can conclude that our method thoroughly represents input EEG signal spatial features.

- C. Discriminative Power of EEG Representations

𝒢(𝐟 ) 𝒢(𝐟 ) 𝒢(𝐟 )

Subject 52

𝒢(𝐟 ) of subject 52

135

5 10 15 20 25 30 35 40

Frequency (Hz)

- Fig. 3: PSD curves (left) and relevance scores [32] (right) for subject 48 (top) and subject 52 (bottom) from the GISTMI dataset [8]. For the PSD curves, the solid red line and the shaded region exhibit the mean and standard deviation of PSD values of all trials, respectively. We observed that our proposed MSNN concentrates features from the lower frequency range for subject 48 and a wide range for subject 52.

correctly identiﬁed approximately 92% of the seizures within 4.98 sec. We do not present the standard deviation values for this seizure detection experiment because each test trial consisted of different numbers of seizures.

V. ANALYSES AND DISCUSSIONS

In this section, we analyzed our proposed network. We determined the feature response by estimating PSD values and relevance scores [32] to show the multi-scale learning beneﬁts. We also visualized learned weights and represented features of the proposed method using different methodologies, activation pattern maps [25] and t-SNE plots. Additionally, we observed a practical use for the proposed method, especially for drowsiness and seizure detection experiments.

A. Multi-Scale EEG Feature Extraction

To demonstrate the multi-scale information capture ability of our proposed method, we estimated and plotted PSD values and relevance scores [32] for MI EEG samples. Speciﬁcally, we estimated PSD values for subject 48 and 52 in the GIST-MI dataset [8]’s EEG samples from channels on the motor cortex. Additionally, we calculated relevance scores for those subjects by a layer-wise relevance propagation [32]. In our results, all classiﬁcation methods evenly demonstrated well-generalization (baselines: ∼80% and proposed: ∼85%) for subject 48, whereas only the proposed method achieved superior performance for subject 52 (baselines: <65% and proposed: ∼80%). As Fig. 3 shows, subject 48’s EEG samples are highly activated at the µ range, while subject 52’s samples do not show any clear trend at the µ range, but in a wider range. Our proposed network exhibited a high relevance score

To validate the representation ability of the proposed network, we plotted t-SNE transformed learned features shown in Fig. 4b. Speciﬁcally, we exhibited extracted features from test SSVEP EEG samples from the ﬁrst, second, and third spatiospectral-temporal feature representation layers, i.e., f1SST, f2SST, and f3SST (ﬁrst three ﬁgures in Fig. 4b). Then, we also depicted the ﬁnal learned feature, i.e., G(fconcatSST ). These intermediate features f1SST, f2SST, and f3SST are temporally pooled just for visualization like G(fconcatSST ). We used the ﬁrst subject’s ﬁrst session data in the KU-SSVEP dataset [6], and used a learning rate of 200, a perplexity of 10 for the t-SNE calculation, and visualization.

- at the low-frequency range for subject 48 who exhibited a clear trend at the low-frequency range. Furthermore, the relevance scores for subject 52 were roughly alike for the wider range, where subject 52’s PSD demonstrated a less clearly deﬁned trend.

From these visualized represented features, we could observe that G(fconcatSST ) is more class-discriminative than the other intermediate features. Additionally, we observed a trend, which demonstrated that a feature learned by a deeper layer is more disentangled than others learned by shallower layers.

From this phenomenon, we can conclude that our proposed MSNN can capture important features on the multi-scale

9Randomly selected additional results are reported in Supplementary C.

MSNN Block 1

MSNN Block 2

MSNN Block 3

Shallow ConvNet Deep ConvNet RSTNN EEGNet

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

|[Figure 10]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

|[Figure 11]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

|[Figure 12]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |

|[Figure 13]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

| |[Figure 14]|
|---|---|
| | |
| | |
| | |
| | |
| | |

| |[Figure 15]|
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

| |[Figure 16]|
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

Left hand

[a.u.]

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

1

|[Figure 24]| |
|---|---|
| | |
| | |
| | |
| | |
| | |

|[Figure 25]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

|[Figure 26]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

|[Figure 27]| |
|---|---|
| | |
| | |
| | |
| | |
| | |

|[Figure 28]| |
|---|---|
| | |
| | |
| | |
| | |
| | |

|[Figure 29]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

|[Figure 30]| |
|---|---|
| | |
| | |
| | |
| | |
| | |
| | |
| | |

Right hand

0

- (a) Topologically visualized activation pattern maps [25] of comparable baselines, and three spatial convolutions in the proposed network. All these visualized patterns here are estimated by the ﬁrst subject’s ﬁrst fold EEG signals in the GIST-MI dataset [8] and normalized in a range between 0 and 1. Finally, [a.u.] denotes an arbitrary unit.

|Class 1<br>Class 2<br>Class 3<br>Class 4<br>|
|---|

MSNN block 1, Averaged 𝐟 MSNN block 2, Averaged 𝐟 MSNN block 3, Averaged 𝐟

Multi-scale spatio-spectraltemporal feature, 𝒢(𝐟 )

- (b) Visualization of t-SNE transformed represented features for test SSVEP EEG samples. The ﬁrst three ﬁgures denote extracted features by

the ﬁrst, second, and ﬁnal spatial convolutional layers of the proposed method. The ﬁnal ﬁgure exhibits the GAP [29]-ed feature, G(fconcatSST ) which is used for ﬁnal decision making.

AwakeTiredDrowsy

Awake

Tired

Drowsy

0.81 0.18 0.01

0.10 0.84 0.05

0.06 0.13 0.81

PSD + SVM

AwakeTiredDrowsy

0.80 0.20 0.01

0.15 0.80 0.05

0.05 0.14 0.82

Shallow ConvNet

AwakeTiredDrowsy

0.73 0.26 0.01

0.15 0.80 0.05

0.08 0.17 0.75

Deep ConvNet

AwakeTiredDrowsy

0.74 0.24 0.01

0.15 0.80 0.05

0.07 0.16 0.77

RSTNN

AwakeTiredDrowsy

0.73 0.25 0.02

0.15 0.80 0.05

0.08 0.16 0.75

ESTCNN

AwakeTiredDrowsy

0.71 0.26 0.03

0.16 0.78 0.05

0.14 0.18 0.68

EEGNet

AwakeTiredDrowsy

0.81 0.18 0.01

0.13 0.83 0.04

0.04 0.11 0.85

MSNN

|[Figure 31]| |
|---|---|
| | |
| | |
| | |
| | |

0.0

0.2

0.4

0.6

0.8

1.0

Theratioofpredictions

- (c) Normalized averaged confusion matrices estimated by comparable baselines and the proposed method using the SEED-VIG dataset [10].

|| | |Seizure onset and offset Shoeb and Guttag Shallow ConvNet Deep ConvNet RSTNN ESTCNN EEGNet MSNN|
|---|---|---|
| | | |
<br><br>ProbabilityofwhetherinputEEGisictalornot<br><br>1<br><br>0.5<br><br>0|
|---|

0

Relative time [sec.]

6 46 85

- (d) Changes of probabilities estimated by comparable baselines, and the proposed method. These plots demonstrate the probability of whether input EEG is ictal or not. Two dot-dashed lines (magenta) denote the seizure onset and ending, respectively, labeled by Shoeb [11].

- Fig. 4: Investigation of learned weights (Fig. 4a) and represented features (Fig. 4b), and inspection of the practical usage of the proposed network (Fig. 4d and 4c).

- D. Mental Fatigue Classiﬁcation

For the application analysis of drowsiness detection, we visualized confusion matrices that were estimated by the experimental results of the SEED-VIG dataset [10] in Fig. 4c. Because the labels that identify the mental status were decided using the PERCLOS levels [10], the label at the boundary of the two classes may not be accurate. In this respect, we can conclude that the proposed method is useful for drowsiness state detection because false detections predicted by the proposed method are mostly at the boundaries between classes, e.g., the ‘awake’ vs. ‘tired’ or ‘tired’ vs. ‘drowsy’ case. In addition, for practical application, it is essential to detect the drowsy state accurately to avoid unexpected situations, such as a car accident. The proposed method achieved the highest and most promising result for detecting drowsiness among other baselines, i.e., it achieved the highest precision score for identifying the drowsy state. Therefore, we can also expect that our proposed method can be applied in real-world situations.

- E. Early Seizure Detection

Early detection [27] of seizures is one of the most important potential practical applications for this work. Hence, we also validated tthe beneﬁts of the proposed method in early seizure detection. Speciﬁcally, in the training phase, the MSNN was trained using normal and ictal EEG samples with binary labels (e.g., 0: normal and 1: seizure) similar to a conventional training framework. In the testing phase, we input the EEG samples using a sliding window with a 1/256 stride. Then, we observed the change in the output probability values to determine the character of the input (normal or ictal).

Additionally, we visualized these changes in Fig. 4d (We used the ﬁrst subject’s third EEG trial in the CHB-MIT dataset

- [11] for the visualization). In Fig. 4d, magenta-colored dotdashed lines denote the seizure onset and offset. Colored solid lines denote the probability change of various methods. In this visualization, we observed that the proposed method is more stable for detecting seizures. Speciﬁcally, the proposed method detects the seizure EEG signal as a seizure state with a strong probability (almost 1), whereas the other methods have low conﬁdence values (Shoeb and Guttag [14]’s method and ESTCNN [23]) or even make incorrect decisions regarding the seizure state (Shallow ConvNet [2], Deep ConvNet [2], RSTNN [15], and EEGNet [3]).

VI. CONCLUSION

In this work, we proposed a novel and compact deep multi-scale neural network which can learn multi-scale EEG signal features. In our experiments, we validated our novel architecture’s effectiveness over diverse EEG paradigms, MI, SSVEP, seizure, and drowsy EEG signals. Furthermore, we inspected the relevance scores to demonstrate the beneﬁts of the multi-scale feature extraction ability, investigated activation pattern maps to understand what types of neurophysiological phenomena were learned by our CNN model, and visualized the t-SNE of learned features to examine the ability of our method to differentiate feature classes. Finally, we also

demonstrated that the proposed method can be used for precise drowsiness detection and early seizure detection. In all these respects, we concluded that the proposed deep multi-scale neural network offers signiﬁcant potential for interpreting EEG signals. Additionally, because the proposed network is clearly generalizable to various EEG paradigms, it is expected to have promising beneﬁts that can apply to neural architecture search methods [33], thereby making a deep learning-based BCI adaptable to different paradigms.

From a practical standpoint, many limitations remain with regard to the inter-subject variation [24] in performance. In the present work, we experimented in a subject-dependent manner. In general use, it is important for a BCI system to be useful for any subject operating in a subject-independent way. Thus, in the future, we will focus on developing a subject-neutral multi-paradigm BCI system using adversarial learning [34], [35] or other learning strategies [36].

ACKNOWLEDGMENT

This work was supported by Institute for Information & Communications Technology Promotion (IITP) grant funded by the Korea government (No. 2017-0-00451, Development of BCI based Brain and Cognitive Computing Technology for Recognizing User’s Intentions using Deep Learning).

REFERENCES

- [1] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, and K.-R. Muller, “Optimizing Spatial Filters for Robust EEG Single-trial Analysis,” IEEE Signal Processing Magazine, vol. 25, no. 1, pp. 41–56, 2008.
- [2] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep Learning with Convolutional Neural Networks for EEG Decoding and Visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [3] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: A Compact Convolutional Neural Network for EEG-based Brain–Computer Interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018.
- [4] P. Aric`o, G. Borghini, G. Di Flumeri, N. Sciaraffa, and F. Babiloni, “Passive BCI Beyond the Lab: Current Trends and Future Directions,” Physiological Measurement, vol. 39, no. 8, p. 08TR02, 2018.
- [5] X. Zhang, L. Yao, X. Wang, J. Monaghan, and D. Mcalpine, “A Survey on Deep Learning based Brain Computer Interface: Recent Advances and New Frontiers,” arXiv preprint arXiv:1905.04149, 2019.
- [6] M.-H. Lee, O.-Y. Kwon, Y.-J. Kim, H.-K. Kim, Y.-E. Lee, J. Williamson, S. Fazli, and S.-W. Lee, “EEG Dataset and OpenBMI Toolbox for Three BCI Paradigms: An Investigation into BCI Illiteracy,” GigaScience, vol. 8, no. 5, p. giz002, 2019.
- [7] M. Nakanishi, Y. Wang, Y.-T. Wang, and T.-P. Jung, “A Comparison Study of Canonical Correlation Analysis based Methods for Detecting Steady-State Visual Evoked Potentials,” PLoS One, vol. 10, no. 10, p. e0140703, 2015.
- [8] H. Cho, M. Ahn, S. Ahn, M. Kwon, and S. C. Jun, “EEG Datasets for Motor Imagery Brain–Computer Interface,” GigaScience, vol. 6, no. 7, p. gix034, 2017.
- [9] C. O’Reilly, N. Gosselin, J. Carrier, and T. Nielsen, “Montreal Archive of Sleep Studies: An Open-access Resource for Instrument Benchmarking and Exploratory Research,” Journal of Sleep Research, vol. 23, no. 6, pp. 628–635, 2014.
- [10] W.-L. Zheng and B.-L. Lu, “A Multimodal Approach to Estimating Vigilance using EEG and Forehead EOG,” Journal of Neural Engineering, vol. 14, no. 2, p. 026017, 2017.
- [11] A. H. Shoeb, “Application of Machine Learning to Epileptic Seizure Onset Detection and Treatment,” Ph.D. dissertation, Massachusetts Institute of Technology, 2009.

- [12] H.-I. Suk and S.-W. Lee, “A Novel Bayesian Framework for Discriminative Feature Extraction in Brain-Computer Interfaces,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 35, no. 2, pp. 286–299, 2012.
- [13] K. K. Ang, Z. Y. Chin, H. Zhang, and C. Guan, “Filter Bank Common Spatial Pattern (FBCSP) in Brain-Computer Interface,” in IEEE International Joint Conference on Neural Networks, 2008, pp. 2390–2397.
- [14] A. H. Shoeb and J. V. Guttag, “Application of Machine Learning to Epileptic Seizure Detection,” in Proceedings of the 27th International Conference on Machine Learning, 2010, pp. 975–982.
- [15] W. Ko, J. Yoon, E. Kang, E. Jun, J.-S. Choi, and H.-I. Suk, “Deep Recurrent Spatio-Temporal Neural Network for Motor Imagery based BCI,” in 2018 6th International Conference on Brain-Computer Interface (BCI), 2018, pp. 1–3.
- [16] F. Chollet, “Xception: Deep Learning with Depthwise Separable Convolutions,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2017, pp. 1251–1258.
- [17] A. Supratak, H. Dong, C. Wu, and Y. Guo, “DeepSleepNet: A Model for Automatic Sleep Stage Scoring based on Raw Single-channel EEG,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 11, pp. 1998–2008, 2017.
- [18] S. Sakhavi, C. Guan, and S. Yan, “Learning Temporal Information for Brain-Computer Interface Using Convolutional Neural Networks,” IEEE Transactions on Neural Networks and Learning Systems, 2018.
- [19] N. Waytowich, V. J. Lawhern, J. O. Garcia, J. Cummings, J. Faller, P. Sajda, and J. M. Vettel, “Compact Convolutional Neural Networks for Classiﬁcation of Asynchronous Steady-State Visual Evoked Potentials,” Journal of Neural Engineering, vol. 15, no. 6, p. 066031, 2018.
- [20] N.-S. Kwak, K.-R. M¨uller, and S.-W. Lee, “A Convolutional Neural Network for Steady State Visual Evoked Potential Classiﬁcation Under Ambulatory Environment,” PLoS one, vol. 12, no. 2, p. e0172578, 2017.
- [21] U. Asif, S. Roy, J. Tang, and S. Harrer, “SeizureNet: A Deep Convolutional Neural Network for Accurate Seizure Type Classiﬁcation and Seizure Detection,” arXiv preprint arXiv:1903.03232, 2019.
- [22] A. Emami, N. Kunii, T. Matsuo, T. Shinozaki, K. Kawai, and H. Takahashi, “Seizure Detection by Convolutional Neural Network-based Analysis of Scalp Electroencephalography Plot Images,” NeuroImage: Clinical, vol. 22, p. 101684, 2019.
- [23] Z. Gao, X. Wang, Y. Yang, C. Mu, Q. Cai, W. Dang, and S. Zuo, “EEG-Based Spatio-Temporal Convolutional Neural Network for Driver Fatigue Evaluation,” IEEE Transactions on Neural Networks and Learning Systems, 2019.
- [24] V. Jayaram, M. Alamgir, Y. Altun, B. Scholkopf, and M. GrosseWentrup, “Transfer Learning in Brain-Computer Interfaces,” IEEE Computational Intelligence Magazine, vol. 11, no. 1, pp. 20–31, 2016.
- [25] S. Haufe, F. Meinecke, K. G¨orgen, S. D¨ahne, J.-D. Haynes, B. Blankertz, and F. Bießmann, “On the Interpretation of Weight Vectors of Linear Models in Multivariate Neuroimaging,” NeuroImage, vol. 87, pp. 96– 110, 2014.
- [26] T. H. Sanders, M. McCurry, and M. A. Clements, “Sleep Stage Classiﬁcation with Cross Frequency Coupling,” in 2014 36th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, 2014, pp. 4579–4582.
- [27] J. Lee, J. Park, S. Yang, H. Kim, Y. S. Choi, H. J. Kim, H. W. Lee, and B.-U. Lee, “Early Seizure Detection by Applying Frequency-based Algorithm Derived from the Principal Component Analysis,” Frontiers in Neuroinformatics, vol. 11, p. 52, 2017.
- [28] M. Liang and X. Hu, “Recurrent Convolutional Neural Network for Object Recognition,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2015, pp. 3367–3375.
- [29] M. Lin, Q. Chen, and S. Yan, “Network in Network,” arXiv preprint arXiv:1312.4400, 2013.
- [30] X. Glorot and Y. Bengio, “Understanding the Difﬁculty of Training Deep Feedforward Neural Networks,” in Proceedings of the thirteenth International Conference on aAtiﬁcial Intelligence and Statistics, 2010, pp. 249–256.
- [31] A. Binder, S. Bach, G. Montavon, K.-R. M¨uller, and W. Samek, “LayerWise Relevance Propagation for Deep Neural Network Architectures,” in Information Science and Applications. Springer, 2016, pp. 913–922.
- [32] G. Montavon, S. Lapuschkin, A. Binder, W. Samek, and K.-R. M¨uller, “Explaining Nonlinear Classiﬁcation Decisions with Deep Taylor Decomposition,” Pattern Recognition, vol. 65, pp. 211–222, 2017.
- [33] E. Rapaport, O. Shriki, and R. Puzis, “EEGNAS: Neural Architecture Search for Electroencephalography Data Analysis and Decoding,” in International Workshop on Human Brain and Artiﬁcial Intelligence. Springer, 2019, pp. 3–20.

- [34] Y. Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle, F. Laviolette, M. Marchand, and V. Lempitsky, “Domain-Adversarial Training of Neural Networks,” The Journal of Machine Learning Research, vol. 17, no. 1, pp. 2096–2030, 2016.
- [35] E. Jeon, W. Ko, and H.-I. Suk, “Domain Adaptation with Source Selection for Motor-Imagery based BCI,” in 2019 7th International Winter Conference on Brain-Computer Interface (BCI), 2019, pp. 1–4.
- [36] Z. Li and D. Hoiem, “Learning without Forgetting,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 40, no. 12, pp. 2935– 2947, 2017.

