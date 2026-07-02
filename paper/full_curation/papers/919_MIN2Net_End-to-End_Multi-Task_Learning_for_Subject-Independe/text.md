[Figure 1]

GENERIC COLORIZED JOURNAL, VOL. XX, NO. XX, XXXX 2017 1

MIN2Net: End-to-End Multi-Task Learning for Subject-Independent Motor Imagery EEG Classiﬁcation

Phairot Autthasan , Student member, IEEE, Rattanaphon Chaisaen , Student member, IEEE, Thapanun Sudhawiyangkul , Phurin Rangpong, Suktipol Kiatthaveephong, Nat Dilokthanakul, Gun Bhakdisongkhram, Huy Phan , Member, IEEE, Cuntai Guan Fellow, IEEE,

and Theerawit Wilaiprasitporn , Member, IEEE

## arXiv:2102.03814v4[eess.SP]7Jan2022

Abstract—Advances in the motor imagery (MI)-based braincomputer interfaces (BCIs) allow control of several applications by decoding neurophysiological phenomena, which are usually recorded by electroencephalography (EEG) using a non-invasive technique. Despite great advances in MI-based BCI, EEG rhythms are speciﬁc to a subject and various changes over time. These issues point to signiﬁcant challenges to enhance the classiﬁcation performance, especially in a subject-independent manner. To overcome these challenges, we propose MIN2Net, a novel end-toend multi-task learning to tackle this task. We integrate deep metric learning into a multi-task autoencoder to learn a compact and discriminative latent representation from EEG and perform classiﬁcation simultaneously. This approach reduces the complexity in pre-processing, results in signiﬁcant performance improvement on EEG classiﬁcation. Experimental results in a subject-independent manner show that MIN2Net outperforms the state-of-the-art techniques, achieving an F1-score improvement of 6.72%, and 2.23% on the SMR-BCI, and OpenBMI datasets, respectively. We demonstrate that MIN2Net improves discriminative information in the latent representation. This study indicates the possibility and practicality of using this model to develop MI-based BCI applications for new users without the need for calibration.

### Index Terms—Brain-computer interfaces (BCIs), motor imagery (MI), multi-task learning, deep metric learning (DML), autoencoder (AE).

I. INTRODUCTION

# B

RAIN-computer interface (BCI) systems allow users to nonmuscularly communicate with a machine by classifying their

neural activity patterns [1], [2]. Recently, electroencephalography (EEG) has been widely used as a brain-activity recording methods in BCI because it provides a non-invasive and relatively cheaper way of measuring neural activity compared to other neural acquisition techniques. Moreover, EEG offers a higher temporal resolution compared the other brain measurement techniques [3], [4].

This work was supported by PTT Public Company Limited, The SCB Public Company Limited, Thailand Science Research and Innovation (SRI62W1501) and Ofﬁce of National Higher Education Science Research and Innovation Policy Council (C10F630057). (Phairot Autthasan and Rattanaphon Chaisaen contributed equally to this work.) (Corresponding author: Theerawit Wilaiprasitporn.)

P. Autthasan, R. Chaisaen, T. Sudhawiyangkul, P. Rangpong, S. Kiatthaveephong, N. Dilokthanakul, and T. Wilaiprasitporn are with Bio-inspired Robotics and Neural Engineering (BRAIN) Lab, School of Information Science and Technology (IST), Vidyasirimedhi Institute of Science & Technology (VISTEC), Rayong, Thailand (e-mail: theerawit.w@vistec.ac.th).

H. Phan is with the School of Electronic Engineering and Computer Science, Queen Mary University of London, United Kingdom.

C. Guan is with the School of Computer Science and Engineering, Nanyang Technological University, Singapore.

G. Bhakdisongkhram is with the School of Physical Medicine and Rehabilitation, Institute of Medicine, Suranaree University of Technology, Nakhon Ratchasima, Thailand.

Code examples, and other supporting materials are available on https://github.com/IoBT-VISTEC/MIN2Net

Four main types of neurophysiological patterns are widely used to develop EEG-based BCI applications. These include steadystate visual evoked potential (SSVEP), event-related potential (ERP), movement-related cortical potentials (MRCPs), and motor imagery (MI) [5]–[8]. Among these EEG measurements, MI, used in BCI systems, has been gaining more attention because it allows users to generate the suppression of oscillatory neural activity in speciﬁc frequency bands over the motor cortex region without external stimuli [9]. The neurophysiological patterns of MI originate from changing brain areas’ activations in the sensorimotor cortices similar to limb movements. Furthermore, a recent study has demonstrated MI-based BCI as an assistive tool in motor rehabilitation in paralyzed patients, such as post-stroke patients [10].

Most MI-based BCI applications rely on a subject-dependent setting. New users have to participate in the calibration process before using a BCI system, which is time-consuming, inconvenient, and exhausting. Recently, numerous zero-calibration methods have been proposed to diminish the number of calibration trials [11], [12]. One prominent method is a calibration-free, or a subject-independent, where training and testing data are from different subjects. This method exhibits the ability to offer new users to use the BCI system without the calibration phase [13], [14]. It is essential to develop reliable methods based on the subject-independent setting while preserving classiﬁcation performance in an acceptable range. Thus, it is a challenge to ﬁnd discriminative MI-EEG features that generalize across subjects.

One conventional hand-crafted feature is the power spectral density (PSD). Event-related desynchronization/synchronization (ERD/ERS) is the brain activity patterns from particular frequency bands (mu (9–13 Hz) and beta (22–29 Hz)) over the sensorimotor cortex region while performing MI [1], [15]. Therefore we can carry out MI classiﬁcation by considering PSD of EEG [10], [16]. However, there are some limitations of hand-crafted features. The major limitation is the selection of distinguishable information within the raw EEG (e.g., frequency bands and EEG channels), merely depending on the prior knowledge of experts [17].

In recent years, the use of Deep Learning (DL) has been shown promising results and proven itself to be a successful set of models in the ﬁeld of computer vision, speech recognition, and natural language processing [18], [19]. In contrast to hand-crafted features, DL methods can simultaneously learn complicated patterns from multiple dimensions of the data. Thus, many BCI researchers have proposed advanced DL architectures and signiﬁcant improvements have been reported for EEG-MI classiﬁcation. Speciﬁcally, the use of convolutional neural networks (CNNs) have widely applied in EEG-MI classiﬁcation because it offers the ability to efﬁciently learn on both temporal and spatial features from EEG signals [20]–[22]. To extract the temporal and spatial connectivity patterns effectively, the combination of 2D-CNNs and long short-term memory units (LSTMs) has been adopted [23], [24]. Even though existing deep learning works have been considerably successful in EEG decoding

on several MI datasets, these works perform well only in the subjectdependent task, which lacks generalization capabilities on new users.

More recently, the deep learning method based multi-task autoencoder (multi-task AE) has been employed in the ﬁeld of EEG based BCI because it can efﬁciently learn for data compression and classiﬁcation tasks simultaneously [25], [26]. However, to our best knowledge, few researchers have adopted the multi-task AE to learn features from EEG to address the MI classiﬁcation problem because it lacks the ability to maintain discriminative patterns of the original EEG signals. To overcome this issue, we proposed MIN2Net, a novel end-to-end neural network architecture and loss function for training multi-task AE in the MI classiﬁcation task. In this way, the proposed method is able to learn latent representations that preserve discriminative information of the original EEG data by fusing deep metric learning (DML). MIN2Net is optimized by minimizing three different loss functions simultaneously: reconstruction, cross-entropy, and triplet loss functions.

The three main contributions of this paper can be summarized as follows:

- • We proposes a novel end-to-end architecture that can effectively extract the meaningful features from EEG data without using high-complexity EEG pre-processing, resulting in an outstanding performance in the subject-independent MI classiﬁcation. Futhermore, the proposed method demonstrates the excellent performance compared to state-of-the-art algorithms in the subject-independent classiﬁcation over two benchmark datasets.
- • To the best of our knowledge, this is the ﬁrst study proposing deep metric learning to a multi-task AE to improve the MI classiﬁcation performance. The proposed method indicates the possibility to handle with discriminative information in the latent representation.
- • Investigation via visualization of the learned latent features is carried out to interpret the proposed method’s classiﬁcation superiority over other state-of-the-art algorithms.

The remainder of this paper is structured as follows. Section II explains some backgrounds and related work. Section III describes the pre-processing of EEG and the structure of the proposed method. Experimental results of the proposed method are presented in Section IV and discussed in Section V. Finally, the conclusion is explained in Section VI.

II. RELATED WORK

In this section, we review the development of EEG-based MI classiﬁcation and then conclude the limitations on the current MIBCI research. We also describe the concepts of AE and deep metric leaning, which relate to our work. Finally, we give an overview of our proposed method.

A. EEG-based Motor Imagery Classiﬁcation

With the advance of machine learning, BCI researchers have increasingly proposed intelligent algorithms based on a subjectdependent setting to enhance the performance of EEG-based motor imagery decoding. Common Spatial Pattern (CSP) is one of the most popular and commonly used methods in MI-based BCI [27]. Features are effectively extracted via CSP can be achieved by maximizing the differences in the variances for the two classes of EEG signals. Filter Bank Common Spatial Patterns (FBCSP) [28] is one of advanced CSP algorithms, which is based on using multiple frequency bands instead of limiting to a speciﬁc band. FBCSP has been proven to be the state-of-the-art method in EEG-based MI classiﬁcation, owing to its outstanding results [29]. After passing EEG signals through the FBCSP, the meaningful brain features are obtained and then the most

discriminative features are selected using a feature selection method such as mutual information-based best individual feature (MIBIF) [28]. In term of classiﬁers, many conventional algorithms such as support vector machine (SVM) and linear discriminant analysis (LDA), can be used to classify these features [14], [29]. In addition, there have been a variety of algorithms extending CSP and leading to good performance [30]–[32]. Some works that utilize minimum training samples have been proposed and validated on several MI datasets [33], [34]. Although these methods have outperformed stateof-the-art methods in the subject-dependent classiﬁcation task, their performance still needs improvement in the subject-independent case.

One potential direction to improve the performance of EEG-MI classiﬁcation is to leverage a large-scale EEG-MI dataset using deep learning models [14], [35]. In a more recent paper, Lee et al. [36] provided an OpenBMI dataset, where EEG data is measured with a large number of subjects, in multiple sessions, using the MI-BCI paradigm. Taking advantage of a large number of training samples, the OpenBMI dataset has become to be one of the benchmark EEG datasets. In the work by Kwon et al. [14], a subject-independent framework based on CNN architectures was proposed using spectralspatial feature representation to improve subject-independent MI classiﬁcation, resulting in a state-of-the-art performance over the OpenBMI dataset.

- B. Deep Metric Learning Model

Deep metric learning (DML) is a method based on a distance metric concept with the goal of learning representation to measure data similarity, depending on the embedding features learned from a metric learning network [37]. Generally, similarity metric functions such as Euclidean distance, Mahalanobis distance, and cosine distance can be directly employed as the distance metric between two points. In recent years, numerous loss functions such as contrastive loss [38], triplet loss [39] and quadruplet loss [40] are developed for DML and to enhance feature discrimination. These loss functions are used to compute similarity measure on correlated samples to enforce samples of the same class closer to each other and push samples of different classes apart from each other. Unlike other losses such as crossentropy loss where a single sample is used to calculate the gradient, the gradient of a DML loss relies on contrastive pairs, triplets, or quadruplets of samples. Recently, DML has been applied to the ﬁeld of EEG-BCI studies and achieved promising results [41], [42]

- C. Autoencoders

Autoencoder (AE) concept is one of the unsupervised learning algorithms introduced in 1986 [43]. AE is typically employed for data compression, denoising, dimensionality reduction, and feature extraction [13], [44], [45]. This network architecture demonstrates an ability to learn meaningful features from either unlabeled or labeled input data to create latent representation. The learned latent representation is then used to reconstruct the original input. The training objective of this network architecture is to minimize the reconstruction loss of input data. The learned latent representation appears to be more efﬁcient when the reconstruction data is closer to the input data.

In recent years, advanced AE architectures have been developed and adopted for EEG. Denoising sparse autoencoder (DSAE) [46] was proposed to improve the EEG-based epileptic seizure detection. The sparsity constraint of the DSAE makes the reconstruction of the original EEG from the corrupted EEG input more efﬁciently. Furthermore, a compressed sensing (CS) method based on AE was proposed to handle the biopotentials and telemonitoring system [25]. They reveal achievements in both ﬁnding the optimal data compression

and classifying electrocardiogram (ECG) and EEG signals. However, most studies only focused on using AE as an unsupervised learning method to extract the salient features of an original data [46], [47]. Their models were not end-to-end learning paradigms, since their classiﬁers need to be trained separately with the learned features and labeled data to identify the actual class.

To address the aforementioned issue, our previous work [26] presented ERPENet, a multi-task autoencoder-based model (multitask AE) to jointly learn multi-task deep features from both unsupervised EEG-based ERP reconstruction and supervised EEG-based ERP classiﬁcation. In particular, we demonstrated that ERPENet obtained a very good performance in extracting information shared across different datasets for an event-related potential (ERP) decoding task. In this study, we propose a new architecture and a loss function for training a multi-task AE, which is capable of handling three tasks simultaneously to deal with the EEG-based MI classiﬁcation, described in the following sections.

III. METHODS

This section ﬁrst describes the three benchmark datasets. After that, we describe the design of the proposed method and discuss its loss function. Finally, we elaborate the EEG-MI classiﬁcation using the proposed method in a comprehensive study.

A. Data Description

We evaluated the proposed method and other baseline methods on the BCIC IV 2a [48], SMR-BCI [49] and OpenBMI [36] datasets. The ﬁrst two public datasets are well-known as the benchmark datasets for MI classiﬁcation, offered by Graz University of Technology. The last one is the largest public MI dataset so far, provided by Korea University. The details of the databases are explained as follows:

- (a) The BCI IV 2a dataset consists of 9 healthy subjects, performing left hand, right hand, feet, and tongue imagery. The EEG signals were collected using 22 Ag/AgCl electrodes at a sampling frequency of 250 Hz. The number of recorded EEG signals were 288 trials in total, obtained from two sessions on two different days (both are in an ofﬂine manner). In this paper, the classiﬁcation tasks were evaluated on 20 channels from the motor cortices area (FC3, FC1, FCz, FC2, FC4, C5, C3, C1, Cz, C2, ,C4, C6, CP3, CP1, CPz, CP2, CP4, P1, Pz, and P2) and only data from right- and left-hand MI were used. Furthermore, the EEG data was downsampled from 250 to 100 Hz. The time period of the EEG-MI data was deﬁned as the time segment between 0s and 4s after stimulus onset, resulting in a dimension of #subjects×#trials×#channels×#sampled time points (9×144×20×400).
- (b) The SMR-BCI dataset contains EEG signals of 15 channels for the two-class MI task (executing the imagination of right hand and feet) recorded from 14 healthy subjects. The EEG data were gathered using a sampling frequency of 512 Hz. There were 160 trials per subject, obtained from two sessions. The ﬁrst session provided 100 trials of the recorded EEG without feedback. The rest of 60 trails was the EEC recorded with feedback, acquired from the last session. Likewise, the EEG data was downsampled from 512 to 100 Hz. The four-second EEG-MI data was identiﬁed as the time interval between 0s and 4s after stimulus onset, leading to a dimension of #subjects×#trials×#channels×#sampled time points (14×160×15×400).
- (c) The OpenBMI dataset comprises 54 healthy subjects, imaging left- and right-hand movements. The recorded EEG contained 62 EEG channels with a sampling frequency of 1000 Hz and

four sessions. Two sessions were deﬁned as an ofﬂine condition because the subjects executed the MI task without feedback. The remaining sessions provided feedback for the subjects while performing the MI task, so-called on-line condition. In this paper, 20 electrodes (FC5, FC3, FC1, FC2, FC4, FC6, C5, C3, C1, Cz, C2, ,C4, C6, CP5, CP3, CP1, CPz, CP2, CP4, and CP6) from the motor cortices region were chosen. Furthermore, the signals were downsampled from 1,000 to 100 Hz. The time interval of EEG between 0s and 4s after stimulus onset was selected as the MI period. Finally, The segmented EEG-MI data contained a collection of #subjects×#trials×#channels×#sampled time points (54×400×20×400).

- B. Time-domain EEG Representation

In this study, the raw EEG data is time-domain signals that change over time. Since the discriminative features of motor imagery are mainly distributed between 8 Hz and 30 Hz [14], [36], a ﬁfth-order Butterworth band-pass ﬁlter is adopted to construct the ﬁltered EEG data in the corresponding frequency bands. Towards this end, the ﬁltered EEG data is used as the input of MIN2Net. Formally, we consider x ∈ RC×T as a single-trial ﬁltered EEG data from k classes, and its corresponding label is deﬁned to be y ∈ {1, 2, ..., k}, where

- C is the number of channels, and T is the number of sampled time points.

C. Proposed Architecture: MIN2Net

An overview of our proposed MIN2Net is illustrated in Fig. 1 and the detail conﬁguration of each layer is shown in Table I. The MIN2Net is composed of three main modules: autoencoder, deep metric learning, and supervised learning.

1) Autoencoder: The autoencoder module in the MIN2Net consists of two major components the encoder z = q(x) and the decoder xˆ = p(z) components. In the encoder component, an input signal x is encoded into a latent vector z by reducing the input signal’s dimension. For the decoder component, the given latent vector z is decoded back to the input signal xˆ.

The encoder has two CNN blocks, each of them consists of a Conv2D layer, a batch normalization (BN) layer, an exponential linear unit (ELU), and an average pooling layer (AveragePooling2D). The ﬁnal CNN layer’s output is considered as the input of a fully connected layer for mapping the latent representation.

Inspired by CSP, this study utilizes the CNN approach as spatial ﬁltering to effectively learn discriminative features from a set of EEG inputs (x). Each CNN block is operated on the channel mixing CNN concept [21], combining all channels of the input signals. The convolution operation is performed based on the linear combination of all the given channels, convoluted along the time dimension. Therefore, the output is constructed as a new time-series signal, simultaneously extracting spatial information from all the feature channels. Here, the encoder’s hidden size is large for the ﬁrst CNN layer but is gradually decreased in the following CNN layers. More details of the layers’ parameters are shown in Table I. The average pooling layers are applied to extract the important features of the given input signals and reduce the number of parameters. The main beneﬁt of applying the average pooling is to exploit layers with local ﬁlters to share weights among all channels of the given input signals. After every CNN layer, a BN layer is used before feeding into the subsequent average pooling layer. The feature maps after the ﬁnal average pooling are transformed into a vector representation via ﬂattening. Finally, the ﬂattened vector is presented to a fully connected (FC) layer with the hidden size of z units to embed and

Encoder

Latent vector Decoder

FC

AveragePooling2D

AveragePooling2D

Conv2DTranspose

Input

FC

Conv2DTranspose

Reconstruction

Conv2D

| |
|---|

Flatten

| |
|---|

Conv2D

C

T

10 (1,64)

250

z

10 (1,32)

T 100

(1,4)

(1, )

C (1,32)

C (1,64)

- A) Autoencoder

- B) Deep Metric learning C) Supervised Learning

[Figure 2]

###### Prediction

Concatenate

[Figure 3]

d(a,p) d(a,n) margin

[Figure 4]

[Figure 5]

FC

Learning

|Left| |
|---|---|
|Right| |

Softmax

a Anchor p Positive n Negative Label or

n

2

a

p

- Fig. 1. Overall visualization of MIN2Net Architecture. (a) exhibits the AE network consisting of 3 components: encoder, latent vector, and decoder. The encoder compresses the input data and produces the latent vector then the decoder reconstructs the input data from this latent vector. (b) illustrates metric learning that learns to minimize the distances of embedding vectors of the same label while maximizing different labels. (c) displays the supervised classiﬁer—the latent vector was fed into a FC layer using softmax activation for classiﬁcation. Full details about the network architecture can be found in Table I.

TABLE I MIN2NET ARCHITECTURE, WHERE C IS THE NUMBER OF CHANNELS, T IS THE NUMBER OF TIME POINTS, z IS THE SIZE OF LATENT VECTOR AND N IS THE NUMBER OF CLASSES. NOTED THAT THE DATA FORMAT OF CONV2D IS “CHANNELS LAST”

###### Blocks Layer Filter Size Stride Activation Options Output

Input (1,T,C) (1,T,C) Conv2D C (1,64) 1 ELU padding=same (1,T,C) BatchNormalization (1,T,C) AveragePooling2D (1, T//100) (1,100,C) Conv2D 10 (1,32) 1 ELU padding=same (1,100,10) BatchNormalization (1,100,10) AveragePooling2D (1,4) (1,25,10) Flatten (250)

Encoder

Autoencoder

Latent FC (z) (z)

FC (250) (250) Reshape (1, 25, 10) (1, 25, 10) Conv2DTranspose 10 (1,64) 4 ELU padding=same (1, 100, 10) Conv2DTranspose C (1,32) T//100 ELU padding=same (1,T,C)

Decoder

Input (1) (1) Latent (C) Concatenate [Input,Latent] (C+1)

Metric learning

Latent (C) FC N softmax (N)

Supervised Learning

z is equal to C and 256 for 2- and 3-class classiﬁcation, respectively.

produce the latent vector. The latent vector size of z is expected to preserve the robust features for EEG-MI signals.

For the decoder component, the decoder structure is arranged in a symmetrical way to the encoder component. Since it is essential to match the CNN blocks’ input dimension, the latent vector is passed through a FC layer and then fed into a reshape layer to construct the data in a suitable dimensions. Each of the two CNN blocks of the decoder component makes use of a transpose convolution layer (Conv2DTranspose) with a stride of 4 and an ELU layer. A stride of 4 is employed to upsample the data’s size in a similar way to an upsampling layer. The transpose convolution can extract useful features and reduce useless features, which is beneﬁcial for reconstructing the latent vector. Consequently, the constructed input signal is obtained after passing the two CNN blocks.

The training objective of the AE module is to minimize the reconstruction error between the input and the reconstruction. Here, we employ the mean square error (MSE) as the loss function. Given the input signals xj = {x1, x2, ..., xC}, the loss function

is expressed as:

C

1 C

xj − xˆj 2. (1)

LMSE(x, xˆ) =

j=1

Where xˆj is the reconstruction signal of the channel j.

2) Deep Metric Learning: To preserve the distinguishable patterns in the latent representation of the AE, a deep metric leaning module (DML) was introduced in the AE, extended from the latent vector. With the DML, the network is tasked to learn a distance metric via which the discrimination of the learned features is enhanced. In this paper, we employ a triplet loss in the DML module to reﬂect the relative distances among different classes of the latent vectors. Owing to avoiding a risk of slow convergence and pool local optima, we decide to use a semi-hard triplet constraint, which was demonstrated good performance in [50]. During training, a set of triplets {xa, xp, xn} is randomly sampled from the training data, where the anchor sample xa is closer to the positive sample xp than the negative sample xn. Subsequently, the triplet of three input signals are passed through the encoder component concurrently to

obtain their latent vector za , zp and zn. Thus, the loss function can be formulated as:

- 1

- 2

Ltriplet(za, zp, zn) =

za − zp 2 − za − zn 2 + α

. (2)

+

where [z]+ = max(z, 0). The threshold α is the margin parameter that enforces the Euclidean distance za − zp 2 of positive pairs to be shorter than the Euclidean distance za −zn 2 of negative pairs. Importantly, the margin of the triplet loss plays a signiﬁcant role in training the DML module.

3) Supervised Learning: This module utilizes a standard softmax classiﬁer as a supervised classiﬁer to classify the underlying latent vectors of the input EEG signals. The latent vector z is fed into the FC layer with the softmax activation to obtain the weight of importance for each class, expressed as follows:

#### yˆ(z) = softmax(Wz + b) (3)

Where W and b are the weight matrix and the bias vector respectively. Then, the model is trained using Adam optimizer to minimize the cross-entropy loss, calculated as:

|class|

yk log yˆk. (4)

Lcross-entropy(y, yˆ) = −

k=1

where y and yˆ are the true label and the classiﬁcation probabilities respectively. The class with the maximum classiﬁcation probability is identiﬁed as the predicted class of the single-trial EEG signal.

- D. Training Procedure for MIN2Net

The training objective of the proposed method is optimized by incorporating the three loss functions: LMSE in Equation 1, Ltriplet in Equation 2, and Lcross-entropy in Equation 4. The ﬁnal loss function of our MIN2Net model LMIN2Net is expressed as:

LMIN2Net(x, x, zˆ a, zp, zn, y, yˆ) =

1 N

N

i=1

{β1LMSE(xi, xˆi)

+β2Ltriplet(zia, zip, zin) + β3Lcross-entropy(yi, yˆi)}.

(5)

Where N denotes the total number of input signals. β1, β2 and β3 represent the hyperparameters to weight the contribution of each loss function. As a result of integrating the three loss functions, both the unsupervised and the DML are able to inﬂuence the learning process when the supervised learning occurs.

- E. Network Training

The proposed method was implemented using the Keras framework (TensorFlow v2.2.0 as backend). The training process was implemented using NVIDIA Tesla v100 GPU with 32GB memory. In each training iteration, the loss function was optimized by utilizing Adam optimizer with the learning rate schedule between [10−3, 10−4] for the binary classiﬁcation task and the learning rate schedule between [10−4, 10−5] for the multi-class classiﬁcation task. The learning rate of two considered tasks was decreased with a decay rate of 0.5 when there was no improvement in the validation loss for 5 consecutive epochs. We set a batch size of 10 samples for the subject-dependent classiﬁcation setting and 100 samples for the subject-independent classiﬁcation setting. Finally, the number of training iterations relied on the early stopping strategy so that the training process was stopped if there was no reduction of the validation loss for 20 consecutive epochs.

TABLE II LIST OF THE OPTIMAL SET OF HYPERPARAMETERS FOR MIN2NET

Parameter Subject-dependent Subject-independent β1 β2 β3 β1 β2 β3

Dataset

BCIC IV 2a 1.0 0.1 1.0 0.5 0.1 1.0 SMR-BCI 0.1 0.1 1.0 0.1 1.0 0.1 OpenBMI 0.5 0.5 1.0 0.5 0.5 1.0

- F. Baseline Methods

To demonstrate the effectiveness of our MIN2Net, we implemented four state-of-the-art methods for comparison. All deep learning approaches were implemented using the Keras framework (TensorFlow v2.2.0 as backend).

- 1) FBCSP-SVM: FBCSP was developed upon the idea of the

original CSP algorithm [28]. By using the FBCSP as the feature extraction method, the distinguishable EEG features were extracted from multiple frequency bands. In this paper, the FBCSP was implemented using MNE-Python package (version 0.20) [51] and then applied with 4 spatial ﬁlters to decompose EEG signals into 9 frequency bands with a bandwidth of 4 Hz from 4 to 40 Hz (4–8 Hz, 8–12 Hz, ..., 36–40 Hz). Here, each frequency band was created using bandpass ﬁltering with 5th order non-causal Butterworth ﬁlter. Subsequently, a support vector machine (SVM) was used to classify MI by incorporating a grid search algorithm. For the SVM classiﬁer, the hyperparameters consisted of kernel (linear, radial bias function (RBF), sigmoid), C (0.001, 0.01, 0.1, 1, 10, 100, 1000), and, particularly for RBF kernel, gamma (0.01, 0.001). With respect to the grid search algorithm, the prediction on the validation set of the classiﬁcation was assessed to obtain the optimal set of hyperparameters. Eventually, the SVM classiﬁer with the optimal parameters was used for testing purpose.

- 2) Deep Convnet: Deep Convnet was introduced as a DL model

based on two CNN architectures [20] and proven to be effective for dealing with EEG-MI classiﬁcation. In this study, the Deep Convnet was implemented in the optimal parameters as done in [20]. Moreover, the raw EEG data was band-pass ﬁltered between 8 and 30 Hz (5th order non-causal Butterworth ﬁlter).

- 3) EEGNet-8,2: Inspired by the FBCSP method, EEGNet-8,2

was proposed as a compact CNN architecture to capture discriminative EEG features, which achieved a very good performance in different BCI paradigms [22]. Here, EEGNet-8,2 was reproduced to offer a comparable performance. The network parameters were kept in the optimal set of hyperparameters as recommended in the original publication [22]. Furthermore, the raw EEG data were likewise preprocessed with the same protocol as in the Deep Convnet model to construct the input for the training of EEGNet-8,2.

- 4) Spectral-spatial CNN: The spectral-spatial CNN framework

based on CNN architectures (spectral-spatial CNN) was presented by [14] and demonstrated state-of-the-art performance in a subject–independent MI decoding. The framework learned the spectralspatial input, capturing discriminative features from the EEG signals’ multiple frequency bands. In this paper, the raw EEG signals were similarly constructed the spectral-spatial representation as done in [14]. The spectral-spatial CNN model was implemented in the optimal parameters as deﬁned in the original paper.

- G. Experimental Evaluation

To demonstrate our MIN2Net method as a generalized MI classiﬁcation model, we conducted the experiments with both subjectdependent and subject-independent manners on three benchmark

###### Subject-dependent Manner

Session 1 Session 2

- S01 oﬄine online

SMR-BCI

oﬄine online

oﬄine online

- S02

- S01 oﬄine oﬄine

BCIC IV 2a

oﬄine oﬄine

oﬄine oﬄine

- S02

Pre-processing

Test set: 200 trials from two online sessions

S14

S09

###### K-fold cross-validation: 5 folds

Testing

Validation set: 40 trials

Session 1 Session 2

- a)
- b)

Pre-processing

- S01 oﬄine online

OpenBMI

oﬄine online oﬄine online

oﬄine online oﬄine online

- S02

oﬄine online

Training

The overall 200 trials from two oﬄine sessions

S54

Training set: 160 trials

Session 1 Session 2

- S01 oﬄine online

SMR-BCI

oﬄine online

oﬄine online

- S02

- S01 oﬄine oﬄine

BCIC IV 2a

oﬄine oﬄine

oﬄine oﬄine

- S02

Pre-processing

###### K-fold cross-validation: 5 folds

S14

S09

Testing

Session 1 Session 2

Pre-processing

- S01 oﬄine online

OpenBMI

Subject-independent Manner

Test set: a single test subject

Validation set: 10 subjects

Training set: 43 subjects

The overall 53 subjects with EEG from all sessions

oﬄine online oﬄine online

oﬄine online oﬄine online

- S02

oﬄine online

Training

S54

Training set Validation set Test set 1 Subject 10 Trials

- Fig. 2. Framework of a) subject-dependent and b) subject-independent with stratiﬁed k-fold cross-validation for the classiﬁcation models.

datasets (BCIC IV 2a, SMR-BCI, and OpenBMI). Accuracy and F1-score were used to evaluate the performance of all considered methods.

- Fig. 2(a) exhibits an example of how we divided the training and

testing sets in a subject-dependent manner. For BCI IV 2a dataset, the ofﬂine data from session 1 was used as the training set, and the ofﬂine from session 2 was used as the testing set. Meanwhile, the training and testing sets were obtained from the ofﬂine and online sessions for both SMR-BCI and OpenBMI datasets. The stratiﬁed 5fold CV was then utilized to split the training set into the new training and validation sets for parameter search. Each fold was performed by preserving 50 percent of samples for each class in the new training and validation sets.

The subject-independent manner was conducted with a leaveone(subject)-out cross-validation (LOSO-CV), as illustrated in

- Fig. 2(b). Suppose that there are Ns subjects for a speciﬁc dataset. In each fold of LOSO-CV, a single subject was used as the testing set, and the remaining Ns −1 subjects were employed as the training set to obtain Ns classiﬁcation results. The training set was constructed using all data sessions of all Ns−1 training subjects for each dataset. Meanwhile, we chose the ofﬂine session 2 of the test subject as the test set of BCI IV 2a dataset, and the online session of the test subject as the test set for both SMR-BCI and OpenBMI datasets. Furthermore, the stratiﬁed 5-fold CV scheme was adopted on the training set to ﬁnd an optimal set of all classiﬁer parameters. Finally, we calculated the average classiﬁcation accuracy from the Ns × 5 evaluations as the overall performance of MIN2Net and other baseline methods.

The details of the four experiments of the entire study were described as follows:

1) Experiment I: To ﬁnd the optimal set of hyperparameters of MIN2Net, we conducted initial experiments for parameter search. We ﬁrst experimented with EEG-MI binary classiﬁcation to tune β parameters for the loss function of MIN2Net in Equation 5. The grid search algorithm was carried out in the set of {0.1, 0.5, 1.0} for β1, β2, and β3. As shown in Equation 2, the margin α plays a signiﬁcant role during training MIN2Net. To examine the effect of this hyperparameter, we performed experiments with MIN2Net to search for an optimal value of α in the set {0.1, 0.5, 1.0, 5.0, 10.0, 100.0}.

Furthermore, we conducted an ablation study to examine the effectiveness of each component in MIN2Net. We compared our

TABLE III CLASSIFICATION PERFORMANCE (ACCURACY ± SD AND F1-SCORE ± SD) IN % OF MIN2NET USING THE SUBJECT-DEPENDENT AND SUBJECT-INDEPENDENT MANNERS COMPARISONS ON SIX DIFFERENT MARGINS (α). BOLD DENOTES THE BEST NUMERICAL VALUES.

Margin (α)

Subject-dependent Subject-independent Accuracy F1-score Accuracy F1-score

Dataset

0.1 62.28 ± 13.90 62.61 ± 15.13 58.64 ± 8.57 46.59 ± 23.58

- 0.5 62.25 ± 13.89 63.08 ± 14.70 59.27 ± 8.38 49.01 ± 19.29
- 1.0 63.46 ± 14.33 64.28 ± 15.27 60.03 ± 9.24 49.09 ± 23.28 5.0 63.66 ± 13.65 64.37 ± 14.57 59.61 ± 8.84 49.53 ± 19.56

BCIC IV 2a

10.0 63.87 ± 14.51 64.03 ± 15.66 59.85 ± 8.44 48.39 ± 20.37

- 100.0 65.23 ± 16.14 64.72 ± 18.39 58.78 ± 8.69 46.14 ± 24.29

SMR-BCI

0.1 64.00 ± 15.51 62.47 ± 16.60 56.76 ± 11.19 57.83 ± 20.50

- 0.5 64.31 ± 15.70 62.27 ± 17.07 58.45 ± 12.67 58.41 ± 22.40
- 1.0 65.90 ± 16.50 64.13 ± 17.66 59.79 ± 13.72 61.10 ± 23.64 5.0 65.14 ± 16.08 62.04 ± 18.20 59.69 ± 13.86 58.88 ± 22.48

10.0 65.45 ± 15.81 62.01 ± 17.82 58.81 ± 13.50 58.61 ± 23.43

- 100.0 66.98 ± 17.22 62.77 ± 20.58 60.79 ± 13.73 60.47 ± 24.31

0.1 59.25 ± 14.27 61.79 ± 14.26 72.14 ± 14.22 72.07 ± 15.19

- 0.5 59.85 ± 13.93 62.17 ± 14.17 71.06 ± 13.91 71.23 ± 14.40
- 1.0 61.03 ± 14.47 63.59 ± 14.52 72.03 ± 14.04 72.62 ± 14.14 5.0 59.93 ± 13.77 62.41 ± 14.31 70.43 ± 13.81 71.00 ± 13.90

OpenBMI

10.0 58.97 ± 13.56 61.51 ± 14.14 69.43 ±14.29 69.46 ± 15.32 100.0 57.14 ± 13.96 59.11 ± 15.98 70.48 ± 14.40 70.95 ± 15.25

complete MIN2Net model with two modiﬁcation models:

- • MIN2Net-without triplet: the MIN2Net without the DML module
- • MIN2Net-without decoder: the MIN2Net without decoder part of AE module

We then performed one-way repeated measures analysis of variance (ANOVA) with Bonferroni correction to evaluate the signiﬁcant differences among the classiﬁcation performance of MIN2Net and the aforementioned modiﬁcation models.

2) Experiment II: In this study, we compared the EEG-MI classiﬁcation performance of MIN2Net with the aforementioned baseline methods. This experiment was conducted based on EEG-MI binary classiﬁcation to investigate all methods’ effectiveness over the three aforementioned benchmark datasets in both the subject-dependent and subject-independent scenarios. To make a fair comparison, all methods were evaluated on the same training, validation, and testing sets. We carried out one-way repeated measures analysis of variance (ANOVA) with Bonferroni correction to analyze the classiﬁcation performance’s signiﬁcant differences between our MIN2Net and all

TABLE IV CLASSIFICATION PERFORMANCE (ACCURACY ± SD AND F1-SCORE ± SD) IN % OF MIN2NET COMPARED TO MIN2NET-WITHOUT TRIPLET AND MIN2NET-WITHOUT DECODER USING THE SUBJECT-DEPENDENT AND SUBJECT-INDEPENDENT MANNERS ON ALL DATASETS. BOLD DENOTES THE BEST NUMERICAL VALUES, AND * REPRESENTS THE PERFORMANCE VALUE WHICH WAS SIGNIFICANTLY HIGHER THAN ALL COMPARISON PAIRS, p < 0.05.

Subject-dependent Subject-independent Accuracy F1-score Accuracy F1-score

Dataset Comparison Model

MIN2Net-without triplet 60.76 ± 11.93 61.09 ± 13.83 58.70 ± 8.91 49.36 ± 20.25 MIN2Net-without decoder 65.71 ± 16.16 65.46 ± 18.34 57.55 ± 9.06 44.24 ± 24.89

BCIC IV 2a

MIN2Net 65.23 ± 16.14 64.72 ± 18.39 60.03 ± 9.24 49.09 ± 23.28

MIN2Net-without triplet 63.86 ± 14.13 61.31 ± 16.19 57.95 ± 12.55 60.53 ± 20.33 MIN2Net-without decoder 64.86 ± 16.21 62.65 ± 17.99 57.38 ± 12.22 55.28 ± 22.17

SMR-BCI

###### MIN2Net 65.90 ± 16.50 64.13 ± 17.60 59.79 ± 13.72 61.10 ± 23.64

MIN2Net-without triplet 59.66 ± 14.02 61.64 ± 14.44 71.10 ± 13.58 69.28 ± 16.10 MIN2Net-without decoder 58.76 ± 13.79 61.70 ± 13.64 70.59 ± 14.23 70.69 ± 14.48

OpenBMI

MIN2Net 61.03 ± 14.47* 63.59 ± 14.52* 72.03 ± 14.04* 72.62 ± 14.14*

baseline methods.

3) Experiment III: To demonstrate the practicality of MIN2Net in developing real-world applications, we conducted an experiment with three-class EEG-MI classiﬁcation task (right hand MI vs. left hand MI vs. resting EEG) over the OpenBMI dataset. This experiment was designed to compare the effectiveness of MIN2Net against the aforementioned baseline methods in pseudo-online situations. Since MIN2Net on the subject-independent scenario demonstrated prominent performance from Experiment I and II, we used this scenario in this experiment. Here, both the right and left hand MI signals were likewise segmented with the same protocol as in subsection III-A(c). Meanwhile, we chose the time interval of EEG between 4s and 8s after stimulus onset as the resting EEG period. Since the resting EEG was obtained from all EEG recordings, the number of trials in each MI class was less than the resting EEG class. We decided to randomly select half of all resting EEG trials to overcome the imbalance issue. To compare all the used methods, an ANOVA with Bonferroni correction was employed for statistical analysis.

H. Visualization

To compare the abilities of deep learning methods in extraction of the highly discriminative features from the EEG signals, we used the t-SNE method [52] to visualize the generalized brain features learned by different deep learning methods in the 2-dimensional embedding space. By applying the t-SNE, the high dimensional embedding space at the input of the ﬁnal fully connected layer in all trained model was used as the learned features for visualization.

IV. RESULTS

This section reports the results and statistical analysis of Experiment I, II, and III to validate the effectiveness of MIN2Net. Furthermore, we visualize of the learned EEG features, to demonstrate the discriminative power of the features learned by the MIN2Net. The performance of each experiment was reported as accuracy and F1-score with standard deviation (Accuracy ± SD and F1-score ± SD).

A. Experiment I: Parameters Adjustment

Table II presents the optimal hyperparameters to adjust each module’s weight (β1, β2 and β3) for the loss function of MIN2Net in Equation 5, resulting in the optimal performance of classifying EEG-MI data. Note that, the average classiﬁcation performance of

MIN2Net on all β combinations of each dataset is reported in the supplementary materials1. Table III illustrates the classiﬁcation results when different value of the margin parameters (α) are contributed in the DML module of MIN2Net. We observed that the margin parameter’s size had a signiﬁcant impact on the ﬁnal classiﬁcation performance, and when marking the margin value as 1.0, the MIN2Net achieved the best performance in the subject-independent manner for all datasets. For the subject-dependent manner, the margin value of 100.0 contributed to the best performance of MIN2Net on BCIC IV 2a dataset, whereas the best performance of MIN2Net on both SMR-BCI and OpenBMI datasets were obtained by setting the margin value as 1.0.

The results of the ablation study are summarized in Table IV. It can be seen that the classiﬁcation performance of MIN2Net outperformed both MIN2Net-without triplet and MIN2Net-without decoder models in terms of accuracy and F1-score on both subject-dependent and subject-independent manners for both SMR-BCI and OpenBMI datasets. In a paired t-test, MIN2Net was signiﬁcantly higher than these modiﬁcation models in both manners for the OpenBMI dataset, p < 0.05. However, on the BCIC IV 2a dataset, the performance improvement of MIN2Net to its modiﬁcation models was not found in both manners.

B. Experiment II: Binary MI classiﬁcation

Table V presents the overall performance of our MIN2Net and four baseline methods across all subjects for both subject-dependent and subject-independent settings. It is observed that in the subjectindependent manner, MIN2Net achieved the highest performance in terms of accuracy on the OpenBMI dataset and terms of F1-score on both SMR-BCI and OpenBMI datasets. Speciﬁcally, signiﬁcant differences were seen among the accuracy and F1-score provided by MIN2Net and the other baseline methods in the OpenBMI dataset, p < 0.05. Considering the SMR-BCI dataset, the F1-score improvement of MIN2Net to the baseline methods was signiﬁcant (p < 0.05) except for the Deep Convnet and Spectal-spatial CNN models. However, the overall performance of MIN2Net was lower than some baseline methods in the subject-independent over the BCIC IV 2a dataset. Furthermore, in the subject-dependent setting, the performance improvement of MIN2Net to the baseline methods was not found on three considered datasets.

Moreover, we reveal the average training and prediction times for all subjects per epoch on all considered datasets as shown in Table VI. Note that the training time was identiﬁed as the duration time in each training iteration. Meanwhile, the prediction time was deﬁned as the

1https://github.com/IoBT-VISTEC/MIN2Net

TABLE V CLASSIFICATION PERFORMANCE (ACCURACY ± SD AND F1-SCORE ± SD) IN % FOR THE SUBJECT-DEPENDENT AND SUBJECT-INDEPENDENT SCHEMES ON BCIC IV 2A, SMR-BCI, AND OPENBMI COMPARED TO SIX DIFFERENT METHODS. BOLD DENOTES THE BEST NUMERICAL VALUES, AND * REPRESENTS THE PERFORMANCE VALUE WHICH WAS SIGNIFICANTLY HIGHER THAN ALL COMPARISON PAIRS, p < 0.05.

Subject-dependent Subject-independent Accuracy F1-score Accuracy F1-score

Datasets Comparison Model End-to-end

FBCSP-SVM No 75.93 ± 14.93 74.49 ± 18.68 58.09 ± 9.91 51.53 ± 24.01 Deep Convnet Yes 63.72 ± 17.18 59.85 ± 22.17 56.34 ± 8.86 30.62 ± 28.96

BCIC IV 2a (9 subjects, 288 trials/subject)

EEGNet-8,2 Yes 65.93 ± 18.44 64.45 ± 26.23 64.26 ± 11.03 60.19 ± 19.96 Spectral-Spatial CNN No 76.91 ± 13.75 77.03 ± 15.41 66.05 ± 13.70 61.91 ± 20.31 MIN2Net Yes 65.23 ± 16.14 64.72 ± 18.39 60.03 ± 9.24 49.09 ± 23.28

FBCSP-SVM No 74.50 ± 18.14 70.65 ± 23.64 62.64 ± 15.43 45.07 ± 34.93 Deep Convnet Yes 61.40 ± 15.66 55.27 ± 22.00 65.26 ± 16.83 54.38 ± 32.58

SMR-BCI (14 subjects, 160 trials/subject)

EEGNet-8,2 Yes 67.76 ± 18.09 68.05 ± 21.11 58.07 ± 11.45 34.43 ± 31.35 Spectral-Spatial CNN No 76.76 ± 16.66 69.87 ± 28.15 66.21 ± 15.15 54.36 ± 31.21

MIN2Net Yes 65.90 ± 16.50 64.13 ± 17.66 59.79 ± 13.72 61.10 ± 23.64

FBCSP-SVM No 66.06 ± 16.58 64.66 ± 19.47 64.96 ± 12.70 65.25 ± 15.14 Deep Convnet Yes 60.31 ± 16.76 61.66 ± 18.17 68.33 ± 15.33 70.20 ± 15.18

OpenBMI (54 subjects, 400 trials/subject)

EEGNet-8,2 Yes 60.41 ± 17.12 56.80 ± 23.54 68.84 ± 13.87 70.39 ± 14.30 Spectral-Spatial CNN No 65.19 ± 15.94 66.97 ± 16.71* 68.27 ± 13.56 65.86 ± 17.37

MIN2Net Yes 61.03 ± 14.47 63.59 ± 14.52 72.03 ± 14.04* 72.62 ± 14.14*

|Dataset|Raw EEG|Deep Convnet|EEGNet-8,2|Spectral-spatial CNNs|MIN2Net|
|---|---|---|---|---|---|
|s<br><br>BCIC IV 2a|[Figure 6]|[Figure 7]|[Figure 8]|[Figure 9]|[Figure 10]|
|SMRBCI|[Figure 11]|[Figure 12]|[Figure 13]|[Figure 14]|[Figure 15]|
|Largescale MI|[Figure 16]|[Figure 17]|[Figure 18]|[Figure 19]|[Figure 20]|

[Figure 21]

[Figure 22]

[Figure 23]

###### Left hand MI Right hand MI Both feet MI

- Fig. 3. Visualization of EEG features using two-dimensional t-SNE projection on the binary classiﬁcation of EEG-MI data in the subject-independent manner. We picked one leaned EEG feature from one subject for each dataset.

duration time in each fold to classify all testing samples. The results also present the number of trainable parameters for MIN2Net and all baseline methods.

F1-score of MIN2Net was shown to be higher in comparison to the F1-score of the two baseline methods when trained with a large number of training samples.

- Fig. 3 illustrates the t-SNE projection of the learned embedding

features of all the datasets. The results display the 2-dimensional embedding features of MIN2Net and all baseline methods, considering all trials of one testing subject of each dataset. It can be seen that the embedding features from each class were more likely to be compactly clustered as well as attempted to preserve the relative distances among different clusters.

- Fig. 4 displays the variations of the classiﬁcation F1-score with

C. Experiment III: Multi-class MI classiﬁcation

Table VII exhibits the entire performance of the thee-class MI classiﬁcation on OpenBMI dataset by comparing MIN2Net and all baseline approaches. It was found that on the subject-independent manner, MIN2Net outperformed all baseline methods with the accuracy and F1-score of 68.81 ± 12.44% and 68.04 ± 12.97%, respectively. Moreover, there were signiﬁcant differences in the accuracy and F1-score between MIN2Net and all baseline methods, p < 0.05. Fig. 5 shows the confusion matrix of MIN2Net in the threeclass MI classiﬁcation on OpenBMI dataset. It was observed that in the subject-independent scenario, MIN2Net yielded the highest recall of resting EEG class and the lowest of right hand MI.

respect to the number of training samples. The number of training samples in all the datasets is represented on the x-axis, while the y-axis expresses the binary classiﬁcation F1-score of MIN2Net and the two best baseline methods. It is demonstrated that increasing the number of training samples from 100 to 21200 samples can provide better classiﬁcation F1-score, recommending as a signiﬁcant factor to boost the ﬁnal classiﬁcation F1-score. Therefore, the classiﬁcation

Fig. 6 reveals the scatter plots of the learned embedding features using t-SNE of the OpenBMI dataset. Results of our MIN2Net and

[Figure 24]

a) Raw EEG b) Deep Convnet c) EEGNet-8,2

[Figure 25]

[Figure 26]

[Figure 27]

d) Spectral-spatial CNN e) MIN2Net

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

Left hand MI Right hand MI Resting EEG

- Fig. 4. Effect of the number of training samples on the binary classiﬁcation performance across three considered methods.

Right hand MI Left hand MI Resting EEG

RighthandMILefthandMIRestingEEG

Predicted label

Truelabel

[Figure 33]

- Fig. 5. Confusion matrix of three-class MI classiﬁcation.

Fig. 6. Visualization of EEG features using two-dimensional t-SNE projection on the three-class classiﬁcation of EEG-MI data in the subjectindependent manner. We picked learned EEG features from one subject on OpenBMI dataset for visualization purpose.

artifacts and offers higher classiﬁcation results than the other baseline methods, utilizing simplistic EEG pre-processing only once.

To give insight into an internal perspective behind the optimization process of MIN2Net, we examined the changes of both training and validation losses in the binary classiﬁcation during the training process of the OpenBMI dataset in a subject-independent manner. Four different losses of MIN2Net (MSE, triplet, cross-entropy, and the total losses) were monitored for 60 epochs from all subjects. It was observed that all the four losses converged around 15 epochs, as shown in Fig. 7. Similar to the convergence process on the OpenBMI dataset, we also found signs of the convergence of these four losses within 60 epochs over the BCIC IV 2a and SMR-BCI datasets. As the results in Table VI, MIN2Net has the 2nd smallest size of trainable parameters on all considered datasets. Furthermore, the MIN2Net has a speed of training and prediction similar to the compact baseline models such as EEGNet-8,2 and Deep Convnet.

the others are considered the three-class MI classiﬁcation task from all trials of one representative subject. Similar to the t-SNE projection results in the binary classiﬁcation, the learned embedding features from three different classes tended to be separated into three compact clusters and made an effort to maintain the relative distances among different clusters.

Regarding the module’s weight (β1, β2 and β3) for the loss function of MIN2Net shown in Table II, we can observe that the optimal performance obtains from different sets of the module’s weight. The reason is related to the difference in the amount of data among all considered datasets, where the small dataset requires the small values in the module’s weight to prevent overﬁtting. Meanwhile, all the module’s weight values close to 1 are desirable for the large dataset to achieve optimal performance. We also found that when all three β have the same value, there is a slight difference between the small and the large values on the large dataset. However, using the small dataset shows a considerable difference between the small and the large values as shown in the supplementary materials.

V. DISCUSSION

- A. Effectiveness of Deep Metric Learning

Deep learning (DL) has considerably contributed to the development of efﬁcient MI-based BCI applications. Among the DL techniques, end-to-end multi-task AE is a powerful one to process raw EEG data due to the combination of feature extraction and classiﬁcation. However, AE can recognize instances rather than discriminating among classes. The current study investigated incorporating DML to a multi-task AE named MIN2Net. The role of DML is to solve the aforementioned limitation of AE. As the results in Table IV, DML using the triplet loss considerably affects the MIN2Net’s performance, resulting in the classiﬁcation results which are signiﬁcantly higher than the MIN2Net–without triplet over two benchmark datasets. This suggests that DML can learn and improve discriminating of EEG data among different classes.

- B. Analysis of the Proposed Method

C. Analysis of the Comparison Performance

The binary classiﬁcation results on three benchmark datasets are listed in Table V. It can be observed that on SMR-BCI and OpenBMI datasets, MIN2Net outperforms all baseline methods in a subjectindependent setting. Even though the SMR-BCI dataset’s accuracy of MIN2Net is lower than some baseline methods, the F1-score of MIN2Net is higher than all baseline methods. According to the claims in [54] that F1-score is more valuable than accuracy because it allows for both false positives and false negatives. Additionally, although the two benchmark datasets have different training samples, MIN2Net still results in the best performance in MI classiﬁcation for both datasets. This investigation suggests that incorporating multi-task AE and DML, as done in MIN2Net, plays a vital role in extracting generalized EEG features for MI classiﬁcation, resulting in excellent generalization performance on new subjects.

Recently, the deep learning technique has attained popularity in BCI because it is capable of effectively learning the brain activity patterns from EEG data without using high complexity in EEG preprocessing [53]. In this paper, our MIN2Net method’s input is the time-domain EEG signals, ﬁltered using a particular frequency band to eliminate high- and low-frequency artifacts. Based on Experiment I and II results, MIN2Net performs with higher accuracy than FBCSP and spectral-spatial CNN, which use multiple frequency bands to ﬁlter out artifacts. These results suggest that MIN2Net is robust to

TABLE VI TIME COMPLEXITY (SECONDS PER EPOCH) FOR ALL METHODS AND NUMBER OF TRAINABLE PARAMETERS FOR ALL DEEP LEARNING APPROACHES.

Subject-dependent Subject-independent Training Time Prediction Time Training Time Prediction Time

Datasets Comparison Model #trainable params

FBCSP-SVM - - 0.0008 - 0.0112 Deep Convnet 151,027 0.1709 0.1617 0.2748 0.1739

BCIC IV 2a

EEGNet-8,2 5,162 0.1476 0.1173 0.3735 0.0920 Spectral-Spatial CNN 77,577,714 10.2031 0.7600 8.1334 0.7444 MIN2Net 55,232 0.2320 0.1803 0.4724 0.2373

FBCSP-SVM - - 0.0005 - 0.0047 Deep Convnet 150,302 0.1352 0.1519 0.2412 0.1906

SMR-BCI

EEGNet-8,2 5,082 0.1164 0.1296 0.3210 0.1105 Spectral-Spatial CNN 54,076,914 2.1321 1.0257 5.8785 0.6688 MIN2Net 38,297 0.1463 0.2433 0.4948 0.2966

FBCSP-SVM - - 0.0020 - 0.1906 Deep Convnet 153,427 0.1804 0.1618 1.7497 0.47345 EEGNet-8,2 5,162 0.1882 0.1439 3.0951 0.1372

OpenBMI

Spectral-Spatial CNN 77,577,714 2.2476 1.0934 11.9067 0.8560 MIN2Net 55,232 0.3527 0.2851 1.3626 0.1043

TABLE VII CLASSIFICATION ACCURACY AND F1-SCORE (IN %, ± SD) ON THE OPENBMI DATASET FOR THE THREE-CLASS CLASSIFICATION OF MI IN THE SUBJECT-INDEPENDENT MANNER. BOLD DENOTES THE BEST NUMERICAL VALUES, AND * REPRESENTS THE PERFORMANCE VALUE WHICH WAS SIGNIFICANTLY HIGHER THAN ALL COMPARISON PAIRS, p < 0.05.

###### Algorithms Accuracy F1-score

FBCSP-SVM 50.71 ± 9.99 46.29 ± 12.40 Deep Convnet 54.04 ± 10.12 49.77 ± 12.58

EEGNet-8,2 67.93 ± 11.94 66.41 ± 13.23 Spectral-spatial CNN 64.67 ± 11.63 63.16 ± 12.53

###### MIN2Net 68.81 ± 12.44* 68.04 ± 12.97*

However, in the subject-dependent setting, the results reveal suboptimal classiﬁcation performance of MIN2Net on three benchmark datasets. The reason is that MIN2Net has a small number of training samples where the few training samples are from only one subject, so that this leads to an overﬁtting problem. Generally, the deep learning approach requires a large amount of data to efﬁciently train a generalized model for preventing an overﬁtting problem [55]. As illustrated in Fig. 4, the result conﬁrmed that MIN2Net performed with higher accuracy than the others when using a large number of training samples. Therefore, one suggestive solution to alleviate this overﬁtting issue is to increase training samples in the subject-dependent setting by data augmentation methods. We believed that more training samples could help the model capture generalized features and improve the MI classiﬁcation performance. To prove this, we experimented with how the subject-dependent setting with data augmentation enhanced the MIN2Net performance on all considered datasets. When we applied the data augmentation methods for the EEG data in the subject-dependent setting, it was found that signiﬁcantly higher classiﬁcation performance, as shown in Table VIII in Appendix.

D. Visualization of the Learned Latent Representation

Fig. 3 shows the t-SNE visualization results from the binary MI classiﬁcation in the subject-independent setting. The 2D embedding features from raw EEG data in each dataset demonstrates the nonrelative features among MI classes, as depicted in Fig. 3 (2nd column). Fig. 3 (3rd column), (4th column), and (5th column) present the 2D embedding features of high dimensional embedding features at the input of the ﬁnal FC layer for the baseline DeepConvNet, EEGNet-8,2, and Spectral-spatial CNN methods, indicating that their

embedding features of MI signals from different classes were more likely to overlap with each other. It can be seen that the latent features produced by our MIN2Net method, as depicted in Fig. 3 (6th column), reveal highly discriminative patterns over SMR-BCI and OpenBMI datasets. Similarly, in the multi-class classiﬁcation, the latent features extracted by MIN2Net also provide predominantly discriminative patterns on the OpenBMI dataset compared to the other baseline methods, as shown in Fig. 6. Thus, this provides evidence that our MIN2Net method produces superior performance owing to the greater quality representation of the MI in the learned latent features.

E. Feasibility in online BCI systems

To further evaluate the feasibility and pseudo-online performance of MIN2Net, we established an experiment on the OpenBMI dataset, exhibiting the classiﬁcation among resting EEG, left hand MI, and right hand MI. The results demonstrate that MIN2Net signiﬁcantly outperforms all baseline methods in the subject-independent setting, as depicted in Table VII. Additionally, MIN2Net yields an acceptable misclassiﬁcation rate in the classiﬁcation of three-class MI, as depicted in Fig. 5. The present results conﬁrm the possibility of using the MIN2Net in two promising aspects. First, MIN2Net has the capability of classifying multi-class MI-EEG. Second, MIN2Net could integrate with online BCI applications, providing various movement intentions for users, such as stop moving, left-hand grasping, or righthand grasping.

Moreover, these research ﬁndings provide foundations in developing BCI applications based on a calibration-free method. The proposed method can be used as a pre-trained model, where the model is pre-trained before being applied by a new user. The latency of the proposed method is considered as a prediction time in the testing session. With the subject-independent setting, the BCI application considers the prediction time rather than the training time. According to Table VI, it is found that the prediction time to classify all testing trials is 0.2373 s, 0.2966 s, and 0.1043 s for BCIC IV 2a, SMR-BCI, and OpenBMI datasets, respectively. As shown in Fig. 4, when few subjects are used for training, we could observe that the proposed model provides suboptimal performance. On the other hand, training with more subjects could improve the overall performance of the proposed method. Therefore, once we perceive a new user as an outstanding BCI user, we can include that user in our dataset to retrain the proposed model to achieve better classiﬁcation performance.

a) Mean Square Error Loss b) Triplet Loss

[Figure 34]

[Figure 35]

c) Cross-entropy Loss

d) Total Loss

[Figure 36]

[Figure 37]

Fig. 7. Training and validation losses of our proposed MIN2Net on OpenBMI dataset. The plots show averaged losses with standard error of 54 subjects while d) total loss was weighed by 0.5, 0.5, 1.0 for a) mean square error b) triplet and c) cross-entropy loss respectively.

F. Future Direction

Although MIN2Net achieves a promising classiﬁcation result, there are still several rooms for further improvement. Firstly, the DML module is based on triplet loss, and there are numerous new loss functions developed for DML that are more attractive to investigate [38], [40]. Thus, in the future study, we will focus on incorporating these new loss functions into multi-task AE to further improve classiﬁcation performance. Secondly, we can explore the utilization of MIN2Net on other EEG measurements, such as SSVEP, MRCPs, and ERP. MIN2Nets might be helpful in the extraction of the most discriminative features for classiﬁcation. Finally, a transfer learning framework based on a fast adaptation procedure will be considered in our future work to thoroughly investigate the possibility of our MIN2Net [10], [12].

VI. CONCLUSION

This study proposed MIN2Net, a novel end-to-end multi-task learning, for classifying motor imagery EEG signals. MIN2Net is developed by integrating an autoencoder, a deep metric learning, and a supervised classiﬁer, which learns to compress, discriminate embedded EEG, and classify EEG simultaneously. We compared the binary classiﬁcation performance of MIN2Net with four different deep learning algorithms on three benchmark datasets. The classiﬁcation results revealed that MIN2Net signiﬁcantly outperformed the developed baselines in the subject-independent experiments on SMR-BCI and OpenBMI datasets. Moreover, we obtained promising experimental results from three-class EEG-MI classiﬁcation (left hand MI vs. right hand MI vs. resting EEG). This indicates the possibility and practicality of using this model toward developing real-world applications.

APPENDIX

As the results from Table V, MIN2Net provided suboptimal classiﬁcation performance in the subject-independent manners owing to training with few training samples from one subject. To overcome this issue, data augmentation methods were adopted to increase the training samples in the subject-independent manners. Jittering (Jitter), Magnitude-Warping (MagW), Scaling (Scale), Time-Warping (TimeW) and Permutation (Perm), which were introduced by [56] for bio-signals, were applied to create new ones. The results from using data augmentation methods are illustrated in Table VIII.

TABLE VIII CLASSIFICATION ACCURACY AND F1-SCORE (IN %, ± SD) OF MIN2NET USING DIFFERENT SUBJECT-DEPENDENT MANNERS. BOLD DENOTES THE BEST NUMERICAL VALUES, AND * REPRESENTS THE PERFORMANCE VALUE WHICH WAS SIGNIFICANTLY HIGHER THAN ALL COMPARISON PAIRS, p < 0.05.

Dataset Comparison Manner Accuracy F1-score BCIC IV 2a

without aug. 65.23 ± 16.14 64.72 ± 18.39

with aug. 70.09 ± 16.87* 70.44 ± 16.49* SMR-BCI

without aug. 65.90 ± 16.50 64.13 ± 17.66

with aug. 72.95 ± 15.76* 69.51 ± 20.00* OpenBMI

without aug. 61.03 ± 14.47 63.59 ± 14.52 with aug. 66.51 ± 15.53* 68.47 ± 14.65*

REFERENCES

- [1] D. McFarland and J. Wolpaw, “Eeg-based brain–computer interfaces,” Current Opinion in Biomedical Engineering, vol. 4, pp. 194–200, 2017.
- [2] P. Sawangjai, S. Hompoonsup, P. Leelaarporn, S. Kongwudhikunakorn, and T. Wilaiprasitporn, “Consumer grade eeg measuring sensors as research tools: A review,” IEEE Sensors Journal, vol. 20, no. 8, pp. 3996–4024, 2020.
- [3] H. Cecotti, M. P. Eckstein, and B. Giesbrecht, “Single-trial classiﬁcation of event-related potentials in rapid serial visual presentation tasks using supervised spatial ﬁltering,” IEEE Transactions on Neural Networks and Learning Systems, vol. 25, no. 11, pp. 2030–2042, 2014.
- [4] R. Chai, S. H. Ling, G. P. Hunter, Y. Tran, and H. T. Nguyen, “Brain–computer interface classiﬁer for wheelchair commands using neural network with fuzzy particle swarm optimization,” IEEE Journal of Biomedical and Health Informatics, vol. 18, no. 5, pp. 1614–1624, 2014.
- [5] P. Autthasan, X. Du, J. Arnin, S. Lamyai, M. Perera, S. Itthipuripat, T. Yagi, P. Manoonpong, and T. Wilaiprasitporn, “A single-channel consumer-grade eeg device for brain–computer interface: Enhancing detection of ssvep and its amplitude modulation,” IEEE Sensors Journal, vol. 20, no. 6, pp. 3366–3378, 2020.
- [6] Y. Zou, V. Nathan, and R. Jafari, “Automatic identiﬁcation of artifactrelated independent components for artifact removal in eeg recordings,” IEEE Journal of Biomedical and Health Informatics, vol. 20, no. 1, pp. 73–81, 2016.
- [7] J. Jeong, N. Kwak, C. Guan, and S. Lee, “Decoding movement-related cortical potentials based on subject-dependent and section-wise spectral ﬁltering,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 28, no. 3, pp. 687–698, 2020.
- [8] R. Chaisaen, P. Autthasan, N. Mingchinda, P. Leelaarporn, N. Kunaseth, S. Tammajarung, P. Manoonpong, S. C. Mukhopadhyay, and T. Wilaiprasitporn, “Decoding eeg rhythms during action observation, motor imagery, and execution for standing and sitting,” IEEE Sensors Journal, vol. 20, no. 22, pp. 13776–13786, 2020.
- [9] G. Pfurtscheller and F. Lopes da Silva, “Event-related eeg/meg synchronization and desynchronization: basic principles,” Clinical Neurophysiology, vol. 110, no. 11, pp. 1842 – 1857, 1999.
- [10] K. K. Ang and C. Guan, “Eeg-based strategies to detect motor imagery for control and rehabilitation,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 25, no. 4, pp. 392–401, 2017.
- [11] A. M. Azab, L. Mihaylova, K. K. Ang, and M. Arvaneh, “Weighted transfer learning for improving motor imagery-based brain–computer interface,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 27, no. 7, pp. 1352–1359, 2019.
- [12] K. Zhang, N. Robinson, S.-W. Lee, and C. Guan, “Adaptive transfer learning for eeg motor imagery classiﬁcation with deep convolutional neural network,” Neural Networks, vol. 136, pp. 1 – 10, 2021.
- [13] G. E. Hinton and R. R. Salakhutdinov, “Reducing the dimensionality of data with neural networks,” Science, vol. 313, no. 5786, pp. 504–507, 2006.
- [14] O. Y. Kwon, M. H. Lee, C. Guan, and S. W. Lee, “Subject-independent brain–computer interfaces based on deep convolutional neural networks,” IEEE Transactions on Neural Networks and Learning Systems, vol. 31, no. 10, pp. 3839–3852, 2020.
- [15] D. J. McFarland and J. R. Wolpaw, “Sensorimotor rhythm-based braincomputer interface (bci): feature selection by regression improves performance,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 13, no. 3, pp. 372–379, 2005.

- [16] G. Pfurtscheller and C. Neuper, “Motor imagery and direct braincomputer communication,” Proceedings of the IEEE, vol. 89, no. 7, pp. 1123–1134, 2001.
- [17] Z. Jiao, X. Gao, Y. Wang, J. Li, and H. Xu, “Deep convolutional neural networks for mental load classiﬁcation based on eeg data,” Pattern Recognition, vol. 76, pp. 582 – 595, 2018.
- [18] F. Schroff, D. Kalenichenko, and J. Philbin, “Facenet: A uniﬁed embedding for face recognition and clustering,” in 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 815–823.
- [19] X. Wang, X. Han, W. Huang, D. Dong, and M. R. Scott, “Multisimilarity loss with general pair weighting for deep metric learning,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), June 2019.
- [20] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for eeg decoding and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391–5420, 2017.
- [21] S. Sakhavi, C. Guan, and S. Yan, “Learning temporal information for brain-computer interface using convolutional neural networks,” IEEE Transactions on Neural Networks and Learning Systems, vol. 29, no. 11, pp. 5619–5629, 2018.
- [22] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, jul 2018.
- [23] T. Wilaiprasitporn, A. Ditthapron, K. Matchaparn, T. Tongbuasirilai, N. Banluesombatkul, and E. Chuangsuwanich, “Affective eeg-based person identiﬁcation using the deep learning approach,” IEEE Transactions on Cognitive and Developmental Systems, vol. 12, no. 3, pp. 486–496, 2020.
- [24] P. Zhang, X. Wang, W. Zhang, and J. Chen, “Learning spatial–spectral–temporal eeg features with recurrent 3d convolutional neural networks for cross-task mental workload assessment,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 27, no. 1, pp. 31–42, 2019.
- [25] A. Gogna, A. Majumdar, and R. Ward, “Semi-supervised stacked label consistent autoencoder for reconstruction and analysis of biomedical signals,” IEEE Transactions on Biomedical Engineering, vol. 64, no. 9, pp. 2196–2205, 2017.
- [26] A. Ditthapron, N. Banluesombatkul, S. Ketrat, E. Chuangsuwanich, and T. Wilaiprasitporn, “Universal joint feature extraction for p300 eeg classiﬁcation using multi-task autoencoder,” IEEE Access, vol. 7, pp. 68415–68428, 2019.
- [27] H. Ramoser, J. Muller-Gerking, and G. Pfurtscheller, “Optimal spatial ﬁltering of single trial eeg during imagined hand movement,” IEEE Transactions on Rehabilitation Engineering, vol. 8, no. 4, pp. 441–446, 2000.
- [28] Kai Keng Ang, Zheng Yang Chin, Haihong Zhang, and Cuntai Guan, “Filter bank common spatial pattern (fbcsp) in brain-computer interface,” in 2008 IEEE International Joint Conference on Neural Networks (IEEE World Congress on Computational Intelligence), 2008, pp. 2390–2397.
- [29] K. K. Ang, Z. Y. Chin, C. Wang, C. Guan, and H. Zhang, “Filter bank common spatial pattern algorithm on bci competition iv datasets 2a and 2b,” Frontiers in Neuroscience, vol. 6, p. 39, 2012.
- [30] F. Lotte and C. Guan, “Regularizing common spatial patterns to improve bci designs: Uniﬁed theory and new algorithms,” IEEE Transactions on Biomedical Engineering, vol. 58, no. 2, pp. 355–362, 2011.
- [31] Y. Jiao, T. Zhou, L. Yao, G. Zhou, X. Wang, and Y. Zhang, “Multi-view multi-scale optimization of feature representation for eeg classiﬁcation improvement,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 28, no. 12, pp. 2589–2597, 2020.
- [32] Y. Zhang, T. Zhou, W. Wu, H. Xie, H. Zhu, G. Zhou, and A. Cichocki, “Improving eeg decoding via clustering-based multitask feature learning,” IEEE Transactions on Neural Networks and Learning Systems, pp. 1–11, 2021.
- [33] A. Llera, V. G´omez, and H. J. Kappen, “Adaptive Multiclass Classiﬁcation for Brain Computer Interfaces,” Neural Computation, vol. 26, no. 6, pp. 1108–1127, 06 2014.
- [34] Y. Jiao, Y. Zhang, X. Chen, E. Yin, J. Jin, X. Wang, and A. Cichocki, “Sparse group representation model for motor imagery eeg classiﬁcation,” IEEE Journal of Biomedical and Health Informatics, vol. 23, no. 2, pp. 631–641, 2019.
- [35] R. Mane, N. Robinson, A. P. Vinod, S. W. Lee, and C. Guan, “A multiview cnn with novel variance layer for motor imagery brain computer interface,” in 2020 42nd Annual International Conference of the IEEE Engineering in Medicine Biology Society (EMBC), 2020, pp. 2950–2953.

- [36] M.-H. Lee, O.-Y. Kwon, Y.-J. Kim, H.-K. Kim, Y.-E. Lee, J. Williamson, S. Fazli, and S.-W. Lee, “EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy,” GigaScience, vol. 8, no. 5, 01 2019.
- [37] W. Ge, “Deep metric learning with hierarchical triplet loss,” in Proceedings of the European Conference on Computer Vision (ECCV), September 2018.
- [38] K. Prannay, T. Piotr, W. Chen, S. Aaron, T. Yonglong, I. Phillip, M. Aaron, L. Ce, and K. Dilip, “Supervised contrastive learning,” NeurIPS 2020, 2020.
- [39] F. Schroff, D. Kalenichenko, and J. Philbin, “Facenet: A uniﬁed embedding for face recognition and clustering,” in 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 815–823.
- [40] W. Chen, X. Chen, J. Zhang, and K. Huang, “Beyond triplet loss: a deep quadruplet network for person re-identiﬁcation,” in Proceedings of IEEE International Conference on Computer Vision and Pattern Recognition. IEEE, 2017, pp. 1320–1329.
- [41] R. Thiyagarajan, C. Curro, and S. Keene, “A learned embedding space for eeg signal clustering,” in 2017 IEEE Signal Processing in Medicine and Biology Symposium (SPMB), 2017, pp. 1–4.
- [42] H. Alwasiti, M. Z. Yusoff, and K. Raza, “Motor imagery classiﬁcation for brain computer interface using deep metric learning,” IEEE Access, vol. 8, pp. 109949–109963, 2020.
- [43] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, Learning Internal Representations by Error Propagation. Cambridge, MA, USA: MIT Press, 1986, p. 318–362.
- [44] G. Antoniol and P. Tonella, “Eeg data compression techniques,” IEEE Transactions on Biomedical Engineering, vol. 44, no. 2, pp. 105–114, 1997.
- [45] P. Vincent, H. Larochelle, I. Lajoie, Y. Bengio, and P.-A. Manzagol, “Stacked denoising autoencoders: Learning useful representations in a deep network with a local denoising criterion,” J. Mach. Learn. Res., vol. 11, p. 3371–3408, Dec. 2010.
- [46] Y. Qiu, W. Zhou, N. Yu, and P. Du, “Denoising sparse autoencoderbased ictal eeg classiﬁcation,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 26, no. 9, pp. 1717–1726, 2018.
- [47] M. Wang, S. Abdelfattah, N. Moustafa, and J. Hu, “Deep gaussian mixture-hidden markov model for classiﬁcation of eeg signals,” IEEE Transactions on Emerging Topics in Computational Intelligence, vol. 2, no. 4, pp. 278–287, 2018.
- [48] M. Tangermann, K.-R. M¨uller, A. Aertsen, N. Birbaumer, C. Braun, C. Brunner, R. Leeb, C. Mehring, K. Miller, G. Mueller-Putz, G. Nolte, G. Pfurtscheller, H. Preissl, G. Schalk, A. Schl¨ogl, C. Vidaurre, S. Waldert, and B. Blankertz, “Review of the bci competition iv,” Frontiers in Neuroscience, vol. 6, p. 55, 2012.
- [49] D. Steyrl, R. Scherer, O. F¨orstner, and G. M¨uller-Putz, “Motor imagery brain-computer interfaces: Random forests vs regularized lda - non-linear beats linear,” in Proceedings of the 6th International Brain-Computer Interface Conference Graz 2014, 2014, pp. 061–1–061–4.
- [50] F. Schroff, D. Kalenichenko, and J. Philbin, “Facenet: A uniﬁed embedding for face recognition and clustering,” 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Jun 2015.
- [51] A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, R. Goj, M. Jas, T. Brooks, L. Parkkonen, and M. H¨am¨al¨ainen, “Meg and eeg data analysis with mne-python,” Frontiers in Neuroscience, vol. 7, p. 267, 2013.
- [52] L. van der Maaten and G. Hinton, “Visualizing data using t-sne,” Journal of Machine Learning Research, vol. 9, no. 86, pp. 2579–2605, 2008.
- [53] D. Zhang, L. Yao, K. Chen, S. Wang, X. Chang, and Y. Liu, “Making sense of spatio-temporal preserving representations for eeg-based human intention recognition,” IEEE Transactions on Cybernetics, vol. 50, no. 7, pp. 3033–3044, 2020.
- [54] S. Bhattacharyya, A. Konar, D. N. Tibarewala, and M. Hayashibe, “A generic transferable eeg decoder for online detection of error potential in target selection,” Frontiers in Neuroscience, vol. 11, p. 226, 2017.
- [55] F. Fahimi, S. Dosen, K. K. Ang, N. Mrachacz-Kersting, and C. Guan, “Generative adversarial networks-based data augmentation for braincomputer interface,” IEEE Transactions on Neural Networks and Learning Systems, pp. 1–13, 2020.
- [56] T. T. Um, F. M. J. Pﬁster, D. Pichler, S. Endo, M. Lang, S. Hirche, U. Fietzek, and D. Kuli´c, “Data augmentation of wearable sensor data for parkinson’s disease monitoring using convolutional neural networks,” in Proceedings of the 19th ACM International Conference on Multimodal Interaction, 2017, p. 216–220.

