## Subject-Independent Deep Architecture for EEG-based Motor Imagery Classification

Shadi Sartipi, Student Member, IEEE, and Mujdat Cetin, Fellow, IEEE

### arXiv:2402.09438v1[eess.SP]27Jan2024

Abstract—Motor imagery (MI) classification based on electroencephalogram (EEG) is a widely-used technique in noninvasive brain-computer interface (BCI) systems. Since EEG recordings suffer from heterogeneity across subjects and labeled data insufficiency, designing a classifier that performs the MI independently from the subject with limited labeled samples would be desirable. To overcome these limitations, we propose a novel subject-independent semi-supervised deep architecture (SSDA). The proposed SSDA consists of two parts: an unsupervised and a supervised element. The training set contains both labeled and unlabeled data samples from multiple subjects. First, the unsupervised part, known as the columnar spatiotemporal auto-encoder (CST-AE), extracts latent features from all the training samples by maximizing the similarity between the original and reconstructed data. A dimensional scaling approach is employed to reduce the dimensionality of the representations while preserving their discriminability. Second, a supervised part learns a classifier based on the labeled training samples using the latent features acquired in the unsupervised part. Moreover, we employ center loss in the supervised part to minimize the embedding space distance of each point in a class to its center. The model optimizes both parts of the network in an end-to-end fashion. The performance of the proposed SSDA is evaluated on test subjects who were not seen by the model during the training phase. To assess the performance, we use two benchmark EEG-based MI task datasets. The results demonstrate that SSDA outperforms state-of-the-art methods and that a small number of labeled training samples can be sufficient for strong classification performance.

Index Terms—Brain-Computer Interfaces, Electroencephalography, Motor Imagery, Semi-Supervised Deep Architecture.

I. INTRODUCTION

# M

OTOR imagery (MI) brain-computer interfaces (BCI) enable interpreting the imagination of limb movements.

##### MI BCI has considerable biomedical applications in areas such as neuro-rehabilitation [1]. Electroencephalogram (EEG) as a non-invasive method for recording the human brain’s electrical activity has been widely used in many MI BCI contexts due to its cost-effective and non-invasive nature [2]. Machine learning (ML) approaches have shown great promise in extracting meaningful information from EEG data [3]. Nevertheless, dealing with EEG data involves challenges due to their heterogeneity across different subjects engaged in the same task [4]. Also, these recordings always carry noise and

This work has been partially supported by the National Science Foundation (NSF) under grants CCF-1934962 and DGE-1922591. (corresponding author : Shadi Sartipi)

Shadi Sartipi and Mujdat Cetin are with the Department of Electrical and Computer Engineering, University of Rochester, Rochester, NY 14627, USA (ssartipi@ur.rochester.edu, mujdat.cetin@rochester.edu).

Mujdat Cetin is also with the Goergen Institute for Data Science, University of Rochester, Rochester, NY 14627, USA.

various artifacts which can negatively impact the performance of computational models. As a result, the development of effective models to analyze the imaginary limb movements continues to be an active research topic.

Several articles have been published in the literature to solve the EEG-based MI task [5]. In principle, two approaches can be used to tackle the aforementioned problems. In the first approach, the automated system is calibrated and trained on the specific subject and then the learned network is applied to perform the classification task on the same subject which is called subject-dependent classification. Since each subject has their individual way of reacting to mental tasks and the model is calibrated based on their own way of thinking, this technique leads to acceptable classification performance, as long as we can collect sufficient labeled data and train the classifier for each subject. Despite the effectiveness of this method, generalization to a broad population of users is not in principle guaranteed. The second approach focuses on developing a generalized system capable of application across diverse subjects engaging in a similar task, known as subject-independent classification. While this approach is more practical and desirable in many respects, applying a subject-independent model to individual subjects often results in lower classification accuracy compared to the subjectdependent approach due to individual differences among subjects. Therefore, constructing a subject-independent model that can perform well enough on new subjects would be desirable.

Recently, deep learning models have been shown to exhibit superior performance in EEG recordings compared to traditional machine learning algorithms [6]. Two main drawbacks of the majority of the existing models are the poor performance of the model in the subject-independent scenario and the model’s dependency on a sufficient amount of labeled data in a purely supervised learning setting [7], [8]. However, labeling the EEG recordings is costly, difficult, and time-consuming [9].

In this paper, we propose a new approach for solving left/right-hand, foot, and tongue movement imagination tasks using a novel subject-independent semi-supervised deep architecture (SSDA). The network contains an auto-encoder (AE) which is trained in an unsupervised fashion (i.e., without labels) on training subjects. The AE learns a latent representation through the process of maximizing the similarity between original and reconstructed EEG data. The latent representation extracted by the AE is fed into a classifier trained using a small amount of labeled data in a supervised fashion. The classifier and the AE are trained simultaneously in an endto-end manner. To address the complexity of finding the

best hyper-parameters in deep architectures, we propose a columnar structure for the AE where each column consists of convolutional neural networks (CNN) and recurrent neural networks (RNN) followed by an attention model leading to a columnar spatio-temporal auto-encoder (CST-AE). The CSTAE has the ability to incorporate different spatio-temporal windows to learn the latent representations. We can find a lower dimensional representation without losing the discriminative power via dimensional scaling (DS) in the encoder part [10]. Thus, the reconstruction loss consists of mean-squareerror (MSE) loss and DS loss. The classifier involves both a cross-entropy loss and a center loss [11] to minimize the embedding space distance of each data sample to its class center. During the training phase, the parameters of CST-AE and the classifier are optimized by minimizing the weighted linear combination of reconstruction loss and the classifier loss. As mentioned before, we optimize the CST-AE network without labels (in an unsupervised fashion), thanks to which

- our proposed architecture can perform well even when the number of labeled training samples is limited. We evaluate the proposed model’s performance on test subjects who have not been seen by the model during the training phase, leading to a subject-independent structure. We apply our approach to two of the publicly available datasets, namely, PhysioNet (105 subjects) [12] and BCI Competition IV 2a (9 subjects) [13] in a subject-independent fashion, in order to validate the performance of the proposed method.

The main contributions of this work are highlighted as follows:

- • A novel subject-independent SSDA approach is proposed for EEG-based MI tasks. The model consists of a deep unsupervised CST-AE along with a supervised deep classifier. The CST-AE extracts the spatial, temporal, and attentive information to learn the latent representations without relying on just one fixed spatio-temporal window.
- • Dimensional scaling is applied in the proposed encoder part of the network to obtain the lower dimensional representations while maintaining the discriminative ability to a large extent.
- • A new loss function is defined for the supervised classifier part of the network which not only minimizes the loss based on the given labels but also minimizes the intra-class variability. The comprehensive experiments are performed to show the significance of the defined loss function’s performance with a limited number of labeled trained samples.

The rest of this paper is organized as follows. Section II summarizes the related work. The proposed approach is described in Section III. Details of implementation and datasets are included in Section IV. Section V presents the experimental results and discussions. Section VI concludes the paper.

II. RELATED WORK EEG-based MI classification is the basis of BCI and numer-

- ous approaches have been published [14], [15]. Traditional algorithms commonly consist of two phases, namely, handcrafted feature extraction and classification. The popular approach is to investigate EEG data in specific frequency bands

by calculating the power spectral density (PSD) as a feature [16]. Mutual-information-based features in spatial and temporal domains were also used to classify EEG data [17]. Edelman et al. applied principal component analysis for the EEGbased MI task [15]. In sensorimotor rhythms, event-related synchronization and desynchronization induced by movement imagination have been widely studied in EEG signals while performing MI tasks [14]. Filter bank common spatial pattern (FBCSP) is a widely used feature extraction method that applies the common spatial patterns (CSP) to different frequency bands and chooses the discriminative features in a subjectdependent fashion [18]. Gaur et al. [19] were able to perform a binary classification via two different sliding window-based CSP, where they consider multiple time segments in each trial. The sparse support matrix machine model is proposed by [20] to consider the structural information and feature selection at the same time in order to improve the EEG classification performance.

Lately, deep neural networks (DNN) have been applied widely in MI classification tasks [6]. DL algorithms bring the possibility of learning the discriminative features from the raw EEG recordings in an end-to-end fashion by combining representation learning and classifier learning. In [21], multilayer perceptron along CSP features is applied to replace the traditional classifiers. CNNs have been shown to be effective in encoding the spatial and structural information in EEG [8]. DeepConvNet [22] and EEGNet [7] are two CNN-based models which demonstrated superiority in multiple EEG-based tasks. In [23], the authors presented a domain-independent semi-supervised approach using EEGNet and DeepConvNet as backbones. CNN with multiple 1D convolutional layers is applied to raw EEG data in [24]. Zhao et al. [25] generated the 3D representation of the EEG data by transforming them into sequences of 2D arrays and applied multi-branch 3D CNN to extract the features. Sakhavi et al. altered the FBCSP to find the temporal features and applied CNN for EEG decoding [26]. Ko et al. extracted spatio-spectral-temporal features and fed them as the input of the CNN network [27]. The network was able to learn complex representations. Another research group proposed an adaptive transfer learning strategy using CNN as a backbone of DNN [28]. During the test phase, they applied a small number of test samples to calibrate the pre-trained network before performing the classification task. RNNs are known for their ability to represent temporal dynamics [8]. In [29] a filter bank was applied to get different spectral EEG representations and the spatial and temporal CNN was used to extract the features. To remove the noise source from EEG data, Hwaidi et al. [30] used an auto-encoder prior to the CNN layer.

Several subject-independent approaches have emerged to tackle the MI task. Zhang et al. [31] presented the graphbased convolutional recurrent model as a deep architecture that uses the graph representation to get the spatial and temporal dynamics. The Multi-subject ensemble CNN was proposed in [32], where K-folds were employed to train K base CNN classifiers using a held-out fold. Nagarajan et al. [33] explored the use of layer-wise relevance propagation and neural network pruning techniques for subject-independent channel selection,

utilized to alert the subject of the trial’s start time and prompt them to engage in the MI task. As illustrated in Fig. 1, during each trial, the focus is on the interested time denoted as T. T represents the MI engagement task, starting after a couple of milliseconds of the appearance of the cue and lasting until the relaxation period, as indicated by the disappearance of the fixation cross. Subjects perform the MI task during this T period, followed by a brief relaxation period as the screen returns to normal.

beep

beep

Cue

Cue Motor Imagery Relax

Time

Interested Time (T)

- Fig. 1. Motor imagery EEG acquisition experiment.

Encoder Decoder Latent Representation

Classifier

|Fully Connected|
|---|

Center Loss Cross-Entropy Loss

MSE Loss

| |
|---|

DS Loss

[Figure 1]

[Figure 2]

- Fig. 2. Block-diagram of the proposed subject-independent semi-supervised deep architecture.

In this section, we explain the proposed subject-independent semi-supervised deep architecture for EEG representation learning and classification (Fig. 2). First, we explain the proposed columnar spatio-temporal auto-encoder (CST-AE). Second, we describe the classifier. Finally, the semi-supervised procedure is explained.

A. Columnar Spatio-Temporal Auto-Encoder

EEG data are recorded over the electrodes which can be shown as Z ∈ RC×T, where C is the number of the EEG electrodes, and T represents the number of time points (interest time). Sliding window with length m with an overlap p is applied on raw EEG data to get the temporal time slices Di ∈ RC×m, where m is the temporal slice length, i = 1,2,...,n, and n = floor((T − m)/p) + 1. For the rest of the paper, we consider l and u as the sets of labeled and unlabeled data samples, respectively. We use N to denote the total number of training data samples, Nl to denote the total number of labeled data samples, and Nu to denote the total number of unlabeled data samples. We assume that l ∩u = ∅.

aiming to enhance decoding performance. The combination of CSP and CNN was used in [34] to get the spatial and spectral EEG features, respectively.

Although DL algorithms improve the classification performance, they require a large number of labeled samples to train on. Semi-supervised learning (SSL) has been widely used to overcome labeled data scarcity issues [35]. Some of the common SSL approaches are graph-based methods, expectation-maximization (EM), pseudo-labeling, generative models, Π model, and temporal ensembling [36]–[38]. Graphbased methods propagate the limited labeled samples to the unlabeled ones which were applied in the MI task with a novel iteration mechanism [39]. EM was also used widely in BCI applications for CSP-based classification and unsupervised adjustment of Gaussian mixture models [40]. Lee et al. proposed the pseudo labeling approach where the network was trained on the limited labeled data and the trained network was used to produce the pseudo labels for unlabeled samples [41]. Then, the network was re-trained on all labeled and pseudo-labeled samples. Generative models were used to generate synthetic data and learn the distributional characteristics of EEG data [37]. The Π model was proposed to deal with the case where the number of labeled samples was limited enough making the pseudo labeling unstable [42]. The idea was to add noise and dropout on the input data and network, respectively. Then, two different outputs would be obtained for each individual input sample and the network would seek to minimize the distance between the two outputs. This would force the network to make equivalent predictions for the same input with different additive noises [42]. To improve the training speed of the Π model, temporal ensembling was introduced which aggregates the network output from previous epochs into an ensemble [43].

The proposed CST-AE is a columnar auto-encoder [44] including the encoder that maps the input EEG data with N samples into a latent space, and a decoder to reconstruct the input from the latent variables. The architecture is illustrated in Fig. 3. The encoder consists of a CNN layer to learn structural and spatial representations and an LSTM layer followed by an attention mechanism to learn temporal representations and attentive information. Since finding the best kernel sizes as model parameters associated with the CNN and LSTM layers is challenging, we design the model in a columnar fashion. In each column the EEG slices are encoded by a 2 dimensional (2D) spatial CNN to get the higher-order representation{Si|Si = Conv(Di), i = [1,n]}. A rectified linear unit (ReLU) activation function and a valid padding option are used in the convolution encoding layers. The output is fed to a maxpooling layer to obtain

#### Qi = MaxPool(Si), i = [1,n] (1)

The output of the last layer is flattened and that leads to n 1D feature vectors. One layer of LSTM with an attention mechanism is applied to get the informative temporal dynamics. Thus, the output of each LSTM cell would be {henci |henci = LSTM(Qi), i = [1,n]}. The attention mechanism is employed to emphasize the temporal slices that the subject pays attention to during task performance. Considering W and b as trainable weights and biases, respectively, the attention weights and the

III. PROPOSED APPROACH

To begin, let us consider a typical timing scheme for an MI experiment, as depicted in Fig. 1. The beep and cue are

Temporal Slices Encoder Latent Representation Decoder Reconstructed Temporal Slices

|[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>[Figure 6]<br><br>[Figure 7]<br><br>[Figure 8]<br><br>[Figure 9]<br><br>[Figure 10]<br><br>[Figure 11]<br><br>[Figure 12]<br><br>[Figure 13]<br><br>[Figure 14]<br><br>[Figure 15]<br><br>[Figure 16]<br><br>[Figure 17]<br><br>[Figure 18]<br><br>[Figure 19]<br><br>[Figure 20]<br><br>[Figure 21]<br><br>[Figure 22]<br><br>[Figure 23]<br><br>[Figure 24]<br><br>[Figure 25]<br><br>[Figure 26]<br><br>[Figure 27]<br><br>[Figure 28]<br><br>[Figure 29]<br><br>[Figure 30]<br><br>[Figure 31]<br><br>[Figure 32]<br><br>[Figure 33]<br><br>[Figure 34]<br><br>[Figure 35]<br><br>[Figure 36]<br><br>[Figure 37]<br><br>[Figure 38]<br><br>[Figure 39]<br><br>[Figure 40]<br><br>[Figure 41]<br><br>[Figure 42]<br><br>[Figure 43]<br><br>[Figure 44]<br><br>[Figure 45]<br><br>[Figure 46]<br><br>[Figure 47]<br><br>[Figure 48]<br><br>[Figure 49]<br><br>[Figure 50]<br><br>[Figure 51]<br><br>[Figure 52]<br><br>[Figure 53]<br><br>[Figure 54]<br><br>[Figure 55]<br><br>[Figure 56]<br><br>[Figure 57]<br><br>[Figure 58]<br><br>[Figure 59]<br><br>[Figure 60]<br><br>[Figure 61]<br><br>[Figure 62]<br><br>...|
|---|

|CNN LSTM<br><br>1<br>2<br>3<br>|
|---|

|LSTM CNN<br><br>|
|---|

|[Figure 63]<br><br>[Figure 64]<br><br>[Figure 65]<br><br>[Figure 66]<br><br>[Figure 67]<br><br>[Figure 68]<br><br>[Figure 69]<br><br>[Figure 70]<br><br>[Figure 71]<br><br>[Figure 72]<br><br>[Figure 73]<br><br>[Figure 74]<br><br>[Figure 75]<br><br>[Figure 76]<br><br>[Figure 77]<br><br>[Figure 78]<br><br>[Figure 79]<br><br>[Figure 80]<br><br>[Figure 81]<br><br>[Figure 82]<br><br>[Figure 83]<br><br>[Figure 84]<br><br>[Figure 85]<br><br>[Figure 86]<br><br>[Figure 87]<br><br>[Figure 88]<br><br>[Figure 89]<br><br>[Figure 90]<br><br>[Figure 91]<br><br>[Figure 92]<br><br>[Figure 93]<br><br>[Figure 94]<br><br>[Figure 95]<br><br>[Figure 96]<br><br>[Figure 97]<br><br>[Figure 98]<br><br>[Figure 99]<br><br>[Figure 100]<br><br>[Figure 101]<br><br>[Figure 102]<br><br>[Figure 103]<br><br>[Figure 104]<br><br>[Figure 105]<br><br>[Figure 106]<br><br>[Figure 107]<br><br>[Figure 108]<br><br>[Figure 109]<br><br>[Figure 110]<br><br>[Figure 111]<br><br>[Figure 112]<br><br>[Figure 113]<br><br>[Figure 114]<br><br>[Figure 115]<br><br>[Figure 116]<br><br>[Figure 117]<br><br>[Figure 118]<br><br>[Figure 119]<br><br>[Figure 120]<br><br>[Figure 121]<br><br>[Figure 122]<br><br>...|
|---|

|Attention|
|---|

col.

Attention

col.

col.

...

...

- Fig. 3. Proposed columnar spatio-temporal auto-encoder (CST-AE) architecture. Yellow and grey blocks represent CNN and LSTM layers, respectively. Orange blocks are the latent representations that are the outputs of the attention mechanism. (col: Column).

TABLE I PARAMETERS OF THE LAYERS USED IN THE COLUMNAR SPATIO-TEMPORAL AUTO-ENCODER. C AND U ARE THE NUMBER OF ELECTRODES AND ROW-WISE UPSAMPLING, RESPECTIVELY. (COL.: COLUMN, POOL: MAXPOOLING, CNN: 2D CNN, SAMPLE: UPSAMPLING, BN: BATCH NORMALIZATION).

Encoder∗ Decoder∗∗

|col. 1|col. 2<br><br>|col.3|col.1|col.2<br><br>|col.3|
|---|---|---|---|---|---|
|layer parameter|layer parameter<br><br>|layer parameter|layer parameter<br><br>|layer parameter<br><br>|layer parameter|
|CNN (64; C, 50) CNN (40; C, 45) CNN (30; C, 15) BN − BN − BN − Pool (1, 80) Pool (1, 75) Pool (1, 35)<br><br>Dropout 0.5 Dropout 0.5 Dropout 0.5 Flatten − Flatten − Flatten − LSTM (64; 0.4) LSTM (40; 0.4) LSTM (30; 0.2)<br><br>| | |LSTM (100; 0.2) LSTM (40; 0.4) LSTM (30; 0.2) Reshape (1, 2, 50) Reshape (1, 2, 20) Reshape (1, 2, 15) Sample (U, 4) Sample (U, 4) Sample (U, 4) BN − BN − BN −<br><br>CNN (64; 7, 7) CNN (40; 7, 7) CNN (30; 7, 7) BN − BN − BN − CNN (1; 1, 1) CNN (1; 1, 1) CNN (1; 1, 1)| | |

- *parameters format: CNN (number of filters; filter size) with Relu activation and valid padding, Pool (pool size), Dropout (dropout rate), LSTM (filter size, dropout rate).
- **parameters format: CNN (number of filters; filter size) with Relu activation and same padding, Sample (row-wise scale, horizontal scale), LSTM (filter size, dropout rate).

output of the attention mechanism, αi and v, are calculated as follows [45]:

exp(Whenci + b) j exp(Whenci + b)

αihenci , αi =

. (2)

v =

i

The decoder part contains an LSTM and two CNN layers. First, the latent variable, v, is fed to the LSTM cell as shown in Eq. 3. Second, the result is upsampled and fed to the first CNN layer (Eq. 4). Finally, a CNN layer with kernel size 1 is applied to get the reconstruction, Dˆi, as shown in Eq. 5.

hdeci = LSTM(v), i = [1,n] (3) D˜i = Conv(UpSample(hdeci )), i = [1,n] (4)

Dˆi = Conv(D˜i), i = [1,n] (5)

Table I shows the set of parameters and implementation details for CST-AE.

In addition, we utilize dimensional scaling (DS) [46] in the last layer of the encoder to reduce the dimensionality of the

extracted features while preserving their discriminative ability. To this end, we define Z as the original EEG data and V as the corresponding extracted features in the attention layer. The DS is formulated as an optimization problem that minimizes the squared difference between the similarity indicators of Z and V , i.e.,

minimize

N

N

[dH(Zi, Zj) − dL(Vi, Vj)]2, (6)

i=1

j=1

where dH and dL represent similarity indicators [10] between the original EEG data and lower-dimensional representations in the attention layer, respectively.

B. Classifier

As shown in Fig. 2, the classifier block is defined to perform supervised classification on labeled training samples, l. The latent representation obtained from the encoder is fed to the classifier, which contains two fully connected (FC) layers with

128 and 2 units, respectively. L2 kernel regularization [47] with factor 0.0005 is applied to the second FC layer.

C. Semi-Supervised Deep Architecture

Two different loss functions are defined, namely, the unsupervised reconstruction loss, Lun, and the supervised classification loss, Ls. In the supervised part of the architecture, Ls consists of two parts, namely cross-entropy loss, Lce, and center loss, Lc, defined as below:

1 Nl

yiln(yi′) (7)

i = 1N

Lce = −

l

- 1

- 2

Lc = −

i = 1N

i|22 (8)

|f(Di,θ) − cy

l

Ls = Lce + γLc (9) Here, y and y′ are the actual and predicted labels, respectively. f(−,θ) denotes the parametric function for latent variable calculation with parameter θ. cy is the yth target class center, and γ is the constant weight. The center loss would be helpful in minimizing intra-class variations.

Lun consists of a mean-square-error (MSE) loss, Lmse, to minimize the differences between the input and the reconstructed input, and a DS loss, Lds, to keep the model discriminative to a large extent. Lmse is defined as follows:

Nl

Nu

M

∥Dj′ − Dˆj′∥22) (10)

∥Dj − Dˆj∥22 +

Lmse =

βi(

j=1

i=1

j=1

Nl

Nl

M

[dH(Dk, Dl) − dL(Vk, Vl)]2+

Lds =

ηi(

i=1

k=1

l=1

Nu

Nu

[dH(Dk′ , Dl′) − dL(Vk′, Vl′)]2) (11)

k=1

l=1

Lun = Lmse + Lds (12) where M is the number of the columns in CST-AE, D, D′ denote the labeled and unlabeled input data samples, respectively, D,ˆ Dˆ′ correspond to the reconstructed labeled and unlabeled data samples, respectively, and V, V ′ denote the latent variables of labeled and unlabeled input data, V = f(D,θ) and V ′ = f(D′,θ), respectively. Also, dH, dL are Euclidean distances in original data and lower dimension spaces. β and η are constant weights that enable curriculum learning.

Taking both supervised and supervised components into account jointly, the final loss function is calculated as below:

L = Lun + Ls (13)

Grid search in range [0, 0.5] with step-size 0.1 is performed to get the best values for β, η, and γ.

IV. EXPERIMENTAL SETUP A. Dataset

In order to evaluate the proposed method’s performance, we used two publicly available MI benchmarks: PhysioNet MI EEG dataset [12] and BCI Competition IV 2a [13]. These benchmarks include two-class and four-class MI classification tasks, respectively.

TABLE II CLASSIFICATION PERFORMANCE OF THE PROPOSED SSDA ON EACH VALIDATION FOLD (V) WHEN Nl = N.

###### Dataset Fold Accuracy F1 Score

V1 0.81 0.80 V2 0.84 0.83 V3 0.86 0.86 V4 0.87 0.87 V5 0.81 0.80 V6 0.85 0.84 V7 0.84 0.84 V8 0.77 0.77 V9 0.84 0.84 V10 0.81 0.81

PhysioNet

V1 0.58 0.58 V2 0.68 0.68 V3 0.68 0.67 V4 0.47 0.45 V5 0.71 0.70 V6 0.62 0.59 V7 0.51 0.50 V8 0.68 0.66 V9 0.53 0.53

BCIIV2a

- 1) PhysioNet Dataset: This dataset includes EEG record-

ings of 109 healthy subjects. During the experiment, a target appears either on the left or right side of the screen. The participant imagines opening and closing the corresponding fist until the target vanishes, followed by a period of relaxation. BCI2000 instrument with 64 EEG electrodes is used for data collection. The sampling rate is set to 160 Hz and each trial lasts for 3.1 seconds. The recordings related to subjects 88, 89, 92, and 100 are removed due to technical problems and large amounts of rest periods [12]. This resulted in 105 subjects and each subject performed 45 trials roughly. For evaluation, we used 10-fold cross-validation with 10 repetitions. In each repetition, ten randomly selected subjects were used as the test set, and the remaining subjects were used as the training set. The final performance was calculated as the average performance across all repetitions.

- 2) BCI Competition IV 2a Dataset: This dataset comprises

EEG recordings from 9 healthy participants. The cues related to the BCI paradigm correspond to four classes, namely the imagination of movement of the tongue, feet, right hand, and left hand. EEG data are recorded over 22 electrodes with a 250 Hz sampling frequency. Each subject performs the four-class task in two sessions on two different days; a training session and a testing session, respectively. Each session consists of 288 EEG trials, each of which 4 s. Cross-validation was performed using the leave-one-subject-out method. This means that both the training and testing sessions of one subject were used as a test set, while all sessions of the other subjects were used as a training set each time.

B. Implementation Details

Each EEG trial is sliced into temporal fragments. With datasets having sampling frequencies of 160 and 250 Hz, we have chosen the same window length, m, of 400 samples with different step sizes, p. This duration allows sufficient time for the brain to initiate motor imagery execution. p is set to 20 and 50 for the PhysioNet and BCI IV 2a, respectively. Since each

TABLE III COMPARISON OF THE PROPOSED SSDA WITH STATE-OF-THE-ART METHODS FROM RECENT LITERATURE WHEN ALL LABELS OF THE TRAINING SAMPLES ARE AVAILABLE (Nl = N).

###### Dataset Method Accuracy F1 Score

FBCSP [18] 0.59 ± 0.03 0.60 ± 0.03 RCNN [48] 0.57 ± 0.02 0.57 ± 0.01 EEGNet [7] 0.72 ± 0.04 0.72 ± 0.03

PhysioNet

CasCNN [49] 0.63 ± 0.04 0.63 ± 0.03

DG-HAM [50] 0.76 ± 0.02 0.77 ± 0.02 EEG-ARNN [51] 0.82 ± 0.04 0.82 ± 0.04 Proposed SSDA 0.83 ± 0.03 0.83 ± 0.03

FBCSP [18] 0.36 ± 0.08 0.36 ± 0.10 RCNN [48] 0.33 ± 0.04 0.33 ± 0.01 EEGNet [7] 0.51 ± 0.05 0.49 ± 0.03

BCIIV2a

CasCNN [49] 0.32 ± 0.04 0.32 ± 0.03 DG-HAM [50] 0.59 ± 0.10 0.58 ± 0.10

GSAN [52] 0.43 ± 0.09 −

Proposed SSDA 0.61 ± 0.08 0.59 ± 0.08

TABLE IV RESULTS ON TEST SET WHEN THE NUMBER OF LABELED TRAINING DATA SAMPLES ARE LIMITED ( Nl ≪ N).

Dataset Performance Nl = 3%N Nl = 10%N Nl = 30%N

PhysioNet

Nl = 124 Nl = 409 Nl = 1226

Nu = 3961 Nu = 3676 Nu = 2859 Accuracy 0.53 ± 0.04 0.78 ± 0.03 0.80 ± 0.03 F1 Score 0.42 ± 0.03 0.77 ± 0.03 0.80 ± 0.01

BCIIV2a

Nl = 139 Nl = 461 Nl = 1383

Nu = 4469 Nu = 4147 Nu = 3225 Accuracy 0.30 ± 0.03 0.48 ± 0.05 0.55 ± 0.05 F1 Score 0.22 ± 0.02 0.45 ± 0.04 0.53 ± 0.03

dataset has a different number of electrodes, the values for (C,U) pairs mentioned in Table I, are set to (64,4) and (22,2) for PhysioNet and BCI IV 2a, respectively. Implementation is done in Python with Tensorflow 2.8.2.

To optimize the model parameters and avoid over-fitting during the training process, 10% of the training data samples are randomly selected as the validation data. The model parameters with the highest validation classification accuracy are considered the final trained model. The final model is applied to the test set to get the classification performance. The number of epochs and the initial learning rate are set to 250 and 0.00001, respectively. Adam optimizer with default learning-rate decay is used for the optimization process. The β = [β1,β2,β3], η = [η1,η2,η3], and γ values corresponded to the highest classification performance on validation data when Nl = N, and were set to [0.2,0.1,0.2], [0.1,0.1,0.1], and 0.3, respectively.

V. RESULTS AND DISCUSSIONS

- A. Experimental Results

Table II presents the classification accuracy for each fold when all labels of the training samples are available, Nl = N. As shown in Table II, using raw EEG data as the input of subject-independent SSDA results in 0.83 and 0.61 classification accuracies for PhysioNet and BCI IV 2a datasets, respectively.

|0.7|9 0.2|1|
|---|---|---|
|0.2|3 0.7|7|
| | | |

[Figure 123]

0.7

LeftRight

0.6

0.5

0.4

0.3

Left Right

0.8

|0.7|9 0.2|1|
|---|---|---|
|0.1|9 0.8|1|
| | | |

[Figure 124]

0.7

LeftRight

0.6

0.5

0.4

0.3

0.2

Left Right

- Fig. 4. Normalized confusion matrix when Nl ≪ N, (left) 10% and (right) 30% labeled training data samples on the two-class PhysioNet dataset.

|0.4|3 0.1|4 0.1|3 0.|3|
|---|---|---|---|---|
|0.1|5 0.4|6 0.1|4 0.2|5|
|0.1|9 0.1|9 0.|4 0.2|1|
|0.1|5 0.1|1 0.0|9 0.6|5|
| | | | | |

Left Right Foot Tongue

LeftRightFootTongue

0.1

0.2

0.3

0.4

0.5

0.6

[Figure 125]

|0.6|3 0.1|3 0.1|1 0.1|2|
|---|---|---|---|---|
|0.1|6 0.5|4 0.1|4 0.1|5|
|0.1|9 0.1|5 0.5|1 0.1|4|
|0.1|9 0.1|7 0.1|1 0.5|4|
| | | | | |

Left Right Foot Tongue

LeftRightFootTongue

0.2

0.3

0.4

0.5

0.6

[Figure 126]

- Fig. 5. Normalized confusion matrix when Nl ≪ N, (left) 10% and (right) 30% labeled training data samples on the four-class BCI competition IV 2a dataset.

- 1) Comparison results when Nl = N: Since the datasets

used in this paper are roughly balanced, we consider the F1 score along with classification performance. Table III summarizes the comparison results of the proposed method with state-of-the-art approaches. To have a fair comparison, all the mentioned works follow the same EEG data partitioning. First, we compare our proposed method with a traditional FBCSP [18] approach which is a common feature extraction approach that applies CSP in different frequency bands. SVM is used for classification. We also compare our work with several well-known deep learning approaches. The first deep learning approach is RCNN [48] which utilizes spatial, temporal, and spectral information via temporal CNN and LSTM networks. Then, we compare our work with the widely-used EEGNet [7] which is a CNN-based network. CNN blocks of the network consist of depth-wise and separable convolution operations. Furthermore, CasCNN [49], a CNN and RNN-based model that preserves the spatio-temporal representation of the EEG data, is considered for comparison. DG-HAM [50] is also used for comparison. This method uses graph representations and attention mechanism to perform the classification task. EEG-ARNN [51] is a graph convolutional based network that seeks to find the correlation of signals in the temporal and spatial domains. GSAN [52] is an adversarial network that aims to detect domain-invariant features to improve subjectindependent classification performance. Because the original papers for EEG-ARNN and GSAN either lack results for both datasets or employ a different cross-validation process from ours, we cannot report comparison results for both datasets. The experimental results indicate that the proposed SSDA achieves the best average classification accuracy and F1 score on both datasets.

- 2) The performance of SSDA when Nl ≪ N: As men-

tioned earlier, one of the major motivations of the proposed

TABLE V ABLATION STUDY ON THE DEEP BACKBONE.(Nl = N)

###### Dataset Method Accuracy F1 Score

CNN 0.75 ± 0.03 0.74 ± 0.03 LSTM 0.55 ± 0.01 0.53 ± 0.02

PhysioNet

Attention 0.73 ± 0.02 0.73 ± 0.02

CNN-Attention 0.79 ± 0.03 0.78 ± 0.03 LSTM-Attention 0.75 ± 0.09 0.75 ± 0.09

CNN-LSTM 0.73 ± 0.05 0.73 ± 0.02

Proposed SSDA 0.83 ± 0.03 0.83 ± 0.03

CNN 0.31 ± 0.04 0.29 ± 0.04 LSTM 0.33 ± 0.01 0.33 ± 0.01

BCIIV2a

Attention 0.28 ± 0.02 0.28 ± 0.02

CNN-Attention 0.53 ± 0.09 0.52 ± 0.10 LSTM-Attention 0.35 ± 0.02 0.35 ± 0.02

CNN-LSTM 0.56 ± 0.11 0.55 ± 0.12

Proposed SSDA 0.61 ± 0.08 0.59 ± 0.08

TABLE VI ABLATION STUDY ABOUT THE EFFECTIVENESS OF THE SEMI-SUPERVISED LEARNING WITH VARIOUS DEEP NETWORK COMPONENTS.(Nl = 10%N)

###### Dataset Method Accuracy F1 Score

CNN 0.69 ± 0.02 0.69 ± 0.02 LSTM 0.55 ± 0.04 0.53 ± 0.04

PhysioNet

Attention 0.55 ± 0.05 0.53 ± 0.06 CNN-Attention 0.73 ± 0.03 0.73 ± 0.03

LSTM-Attention 0.60 ± 0.05 0.59 ± 0.06 CNN-LSTM 0.72 ± 0.05 0.72 ± 0.04

###### Proposed SSDA 0.78 ± 0.03 0.77 ± 0.03

CNN 0.28 ± 0.03 0.26 ± 0.04 LSTM 0.25 ± 0.03 0.24 ± 0.02

BCIIV2a

Attention 0.29 ± 0.03 0.28 ± 0.03 CNN-Attention 0.28 ± 0.03 0.27 ± 0.03 LSTM-Attention 0.29 ± 0.01 0.28 ± 0.042

CNN-LSTM 0.29 ± 0.03 0.26 ± 0.03

Proposed SSDA 0.48 ± 0.05 0.45 ± 0.04

framework is dealing with a common EEG challenge namely, a limited number of labeled training samples. To explore the robustness of the proposed approach, we perform experiments where a small number of training samples are labeled (Nl ≪ N). We randomly select 3%, 10%, and 30% of the training samples as labeled samples and perform the same aforementioned classification procedure in each partition. The results for each scenario are presented in Table IV. Considering two class MI classification and PhysioNet dataset, the classification accuracies are 0.53±0.04, 0.78±0.03, and 0.80±0.03 when 3%, 10%, and 30% of training samples are labeled. Four class task and BCI IV 2a reaches to 0.30 ± 0.03, 0.48 ± 0.05, and 0.55 ± 0.05 when 3%, 10%, and 30% of training samples are labeled.

The normalized confusion matrices produced by SSDA with 10% and 30% labeled training samples for two class and four class problems are presented in Fig. 4 and Fig. 5, respectively. Row labels and column labels refer to the ground truth and predicted labels, respectively.

- B. Ablation Study

1) Analyzing the role of deep network components and semi-supervised learning: In this section, we examine the

TABLE VII STATISTICAL SIGNIFICANCE OF THE PERFORMANCE IMPROVEMENTS PROVIDED BY THE PROPOSED METHOD OVER OTHER METHODS CONSIDERED IN THE ABLATION STUDY. WILCOXON SIGNED-RANK TEST P-VALUE.(Nl = 10%N)

Method PhysioNet BCI IV 2a

CNN 0.002 0.004 LSTM 0.002 0.004

Attention 0.002 0.004 CNN-Attention 0.002 0.004

LSTM-Attention 0.002 0.004 CNN-LSTM 0.002 0.004

effectiveness of each component of the proposed SSDA architecture by reporting accuracy and F1 score values on both PhysioNet and BCI IV 2a datasets. Table V summarizes the results.

CNN, LSTM, and Attention methods indicate a single layer of each individual model which are responsible for extracting the spatial, temporal, and attentive features, respectively. CNN-Attention and LSTM-Attention investigate the attentive information on top of CNN encoding and temporal dynamics, respectively.

In the PhysioNet dataset, the CNN-Attention and CNNLSTM models achieve the highest accuracy and F1 score among the baseline models. However, the proposed SSDA method outperforms all the baseline models with a significant margin, achieving an accuracy of 0.83 and an F1 score of 0.83. In the BCI IV 2a dataset, the CNN-LSTM model achieves the highest accuracy and F1 score among the baseline models. However, the proposed SSDA method outperforms all the baseline models, achieving an accuracy of 0.61 and an F1 score of 0.59.

Comparing CNN, LSTM, and Attention models individually with combined models shows the importance of the combination of spatial and temporal encoding models. Our proposed SSDA that relies on spatial encoding, temporal dynamics, and attentive information represents not only the positive effect of each deep network backbones but also the effectiveness of the columnar structure of CST-AE. CST-AE consists of columns of CNN-RNN which helps with the performance improvement as shown in Table V.

To study the semi-supervised learning performance using various components of the deep network architecture, we apply the same limited labeled training samples to the aforementioned methods. As presented in Table VI, with 10% labeled training samples, the proposed SSDA gives a performance higher than the chance level due to the semisupervised learning process. These results indicate that the proposed SSDA outperforms other methods by attaining an accuracy of 0.78 ± 0.03 and an F1 score of 0.77 ± 0.03 on the PhysioNet dataset, as well as an accuracy of 0.48 ± 0.05 and an F1 score of 0.45±0.04 on the BCI IV 2a dataset. This demonstrates the effectiveness of the proposed SSDA method in leveraging both labeled and unlabeled data to enhance classification performance.

On the other hand, the results also show that traditional deep learning models such as CNN, LSTM, and their combinations

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

(a) (b) (c) (d)

- Fig. 6. The distribution of the learned features in the last fully connected layer during (a) training phase with Ls = Lce, (b) testing phase with Ls = Lce, (c) training phase with Ls = Lce + Lc, and (d) testing phase with Ls = Lce + Lc for the PhysioNet dataset. (Nl = N).

[Figure 131]

(a) (b) (c) (d)

[Figure 132]

[Figure 133]

[Figure 134]

- Fig. 7. The distribution of the learned features in the last fully connected layer during (a) training phase with Ls = Lce, (b) testing phase with Ls = Lce, (c) training phase with Ls = Lce + Lc, and (d) testing phase with Ls = Lce + Lc for the BCI Competition IV 2a dataset. (Nl = N).

did not perform well on both datasets, especially on the BCI IV 2a dataset, which is a challenging dataset due to the small number of labeled samples and more number of the classes. The Attention mechanism also did not improve the classification performance significantly. These results emphasize the importance of utilizing semi-supervised learning methods, such as the proposed SSDA, to improve the performance of deep learning models, especially on datasets with limited labeled data.

Also, by comparing the results in Table VI and Table V, the positive effect of our full SSDA architecture on semisupervised learning in four-class classification performance is vivid since leaving out some of the components of the architecture results in significant performance drops in the case of limited training samples.

2) The effect of center loss on the learned features: As shown in Table V, the SSDA method outperforms other baselines. One major reason for this is the loss function, L, used for training SSDA. To explore the effectiveness of optimizing the model with L, we present the learned representations of the last layer of the network in Figs. 6 and 7, which show the distribution of the learned features in the last FC layer with and without considering the center loss in the classification part of the proposed network during the training phase for PhysioNet and BCI IV 2a datasets, respectively. From Figs. 6 and 7, we can observe that the learned features under L have clearer boundaries between two and four MI classes compared to the ones that do not have a center loss in the defined loss function.

- C. Discussion

In this study, we introduce a novel subject-independent approach for EEG-based MI tasks. The use of automated EEG-based motor imagery is crucial in neuroscience and brain-computer interfaces because it helps improve assistive

technology and neurorehabilitation. It does this by reading people’s thoughts from their brain signals, making it easier for them to control devices and systems effectively. Our model is composed of a deep unsupervised CST-AE in conjunction with a supervised deep classifier, which works well even when there’s not much labeled data. It improves brain-computer interfaces and has potential in various applications.

For the Nl = N scenario, as shown in Table III, the proposed SSDA reaches 0.83 ± 0.03 and 0.61 ± 0.08 classification accuracy for PhysioNet and BCI IV 2a datasets, respectively, which outperforms the state-of-the-art works. The major reason that our proposed deep architecture performs better than the traditional FBCSP approach is its ability to learn high-level features from complex EEG data. This also removes the need to find suitable features for a specific domain. Comparing our work with other deep learning models reveals several key strengths. Firstly, the high degree of similarity between the original and reconstructed data indicates that our model successfully captures and retains relevant spatiotemporal patterns from the input EEG signals that are crucial for reconstruction [53], [54]. Secondly, CST-AE allows the utilization of different spatio-temporal windows to learn latent representations. This eliminates the challenge of determining the best kernel size, filter size, and the number of hidden states for CNN and LSTM architectures. Thirdly, unlike other deep learning algorithms, our DS approach facilitates learning representations in a lower dimension while maintaining discriminative ability. This fidelity in representation is especially crucial for subject-independent tasks, indicating the model’s capacity to extract and generalize features indicative of taskrelated neural activities. Fourthly, Lc helps to optimize the problem by minimizing intra-class variation which improves the training process. Since the proposed approach optimizes both parts of the model in an end-to-end fashion, the classification goal influences the optimization of CST-AE, ensuring that

the latent features extracted are relevant to the MI task. Despite the positive aspects associated with using these loss functions as demonstrated in the presented results, it is acknowledged that the computation of the loss may increase the training time, as a function of the amount of data. However, given that our method performs effectively with a small amount of labeled data, the time spent by the supervised components is reduced. In essence, this represents a minor trade-off between performance and time complexity.

One primary motivation behind the presented framework is addressing a prevalent challenge in EEG analysis: the scarcity of labeled training data (Nl ≪ N). As presented in Table IV and considering 0.50 and 0.25 as chance levels for two class and four class classification scenarios, the results indicate that only 10% labeled training samples reach a performance much higher than the chance level. When analyzing the confusion matrices shown in Figs 4 and 5, we find that even with only 10% of labeled training samples, SSDA can still detect all four classes with significantly higher accuracy than the chance level. Moreover, training the proposed network with only 30% of the labeled training samples outperforms most of the supervised state-of-the-art methods listed in Table III.

Statistical analysis is crucial to confirm the significance of the experimental findings when Nl ≪ N [55]. To achieve this, we employ the Wilcoxon signed-rank test for each of the models considered in the ablation study alongside the proposed method. The results are presented in Table VII. Considering a p-value threshold of 0.05 as the significance level, the results show that almost all of the performance differences between the proposed method and other methods considered in the ablation study are statistically significant.

In all experiments presented in this paper, we used raw EEG measurements without any preprocessing. Accordingly, the results presented demonstrate the performance of our approach on noisy data involving potential outliers collected within the context of particular motor imagery experimental paradigms. Future work could examine the robustness of our approach to other types of perturbations, possibly including adversarial examples. For further research directions, we can explore the performance of the proposed SSDA on different BCI modalities, such as P300, which could benefit from the CST-AE structure to find the attentive temporal dynamics. Additionally, SSDA’s capability to train well with a small number of training samples could be tested on EEG-based emotion recognition, which is a complex BCI task that requires expert labeling.

- D. Limitations

Even though the proposed study has introduced a novel and enhanced framework that surpasses the performance of previous methods, it still exhibits specific limitations. Firstly, there is the issue of the DS loss. The DS loss is defined among every pair of samples, leading to an increase in computation time. To mitigate this complexity, we can employ a random selection of pairs, thereby reducing the training time. Secondly, the use of fully connected layers could result in an increased number of parameters. To address this issue, future work

could reduce the number of model parameters by incorporating global pooling layers while ensuring the maintenance of high motor imagery EEG decoding accuracy.

VI. CONCLUSION

In this paper, we proposed a novel semi-supervised deep architecture to improve the subject-independent MI classification task. The proposed method consists of two parts: an unsupervised component and a supervised component. The unsupervised part, the CST-AE, extracts latent features by maximizing the similarity between original and reconstructed EEG data. The supervised part learns a classifier based on labeled samples using the latent features obtained from the unsupervised part. Additionally, center loss is employed to minimize the embedding space distance within each class. Our experimental results on two publicly available benchmarks, one with two-class and the other with four-class MI tasks, show superior performance compared to state-of-the-art works. Additionally, the distribution of the learned representations also demonstrates the positive effect of using center loss along with the classification loss. We also demonstrate that even a small portion of labeled training data samples can lead to effective classification performance due to the unsupervised part of SSDA. This work has the potential to reduce the need for a large number of labels in EEG tasks and eliminate the calibration stage for each subject.

REFERENCES

- [1] J. N. Mak and J. R. Wolpaw, “Clinical applications of brain-computer interfaces: current state and future prospects,” IEEE reviews in biomedical engineering, vol. 2, pp. 187–199, 2009.
- [2] K. K. Ang, C. Guan, K. S. G. Chua, B. T. Ang, C. W. K. Kuah, C. Wang, K. S. Phua, Z. Y. Chin, and H. Zhang, “A large clinical study on the ability of stroke patients to use an EEG-based motor imagery brain-computer interface,” Clinical EEG and Neuroscience, vol. 42, no. 4, pp. 253–258, 2011.
- [3] R. Sharma, M. Kim, and A. Gupta, “Motor imagery classification in brain-machine interface with machine learning algorithms: Classical approach to multi-layer perceptron model,” Biomedical Signal Processing and Control, vol. 71, pp. 103101, 2022.
- [4] H.-I. Suk and S.-W. Lee, “A novel bayesian framework for discriminative feature extraction in brain-computer interfaces,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 35, no. 2, pp. 286–299, 2012.
- [5] J. Cantillo-Negrete, J. Gutierrez-Martinez, R. I. Carino-Escobar, P. Carrillo-Mora, and D. Elias-Vinas, “An approach to improve the performance of subject-independent BCIs-based on motor imagery allocating subjects by gender,” Biomedical engineering online, vol. 13, no. 1, pp. 1–15, 2014.
- [6] A. Craik, Y. He, and J. L. Contreras-Vidal, “Deep learning for electroencephalogram (EEG) classification tasks: a review,” Journal of neural engineering, vol. 16, no. 3, pp. 031001, 2019.
- [7] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGnet: a compact convolutional neural network for EEG-based brain–computer interfaces,” Journal of neural engineering, vol. 15, no. 5, pp. 056013, 2018.
- [8] D. Zhang, L. Yao, X. Zhang, S. Wang, W. Chen, R. Boots, and B. Benatallah, “Cascade and parallel convolutional recurrent neural networks on EEG-based intention recognition for brain computer interface,” in Proceedings of the AAAI Conference on Artificial Intelligence, 2018, vol. 32.
- [9] W.-L. Zheng, W. Liu, Y. Lu, B.-L. Lu, and A. Cichocki, “Emotionmeter: A multimodal framework for recognizing human emotions,” IEEE transactions on cybernetics, vol. 49, no. 3, pp. 1110–1122, 2018.
- [10] S. Gong, V. N. Boddeti, and A. K. Jain, “On the intrinsic dimensionality of image representations,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2019, pp. 3987–3996.

- [11] P. Ghosh and L. S. Davis, “Understanding center loss based network for image retrieval with few training data,” in Proceedings of the European Conference on Computer Vision (ECCV) Workshops, 2018, pp. 0–0.
- [12] A. L. Goldberger, L. A. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, “Physiobank, physiotoolkit, and physionet: components of a new research resource for complex physiologic signals,” circulation, vol. 101, no. 23, pp. e215–e220, 2000.
- [13] C. Brunner, R. Leeb, G. M¨uller-Putz, A. Schl¨ogl, and G. Pfurtscheller, “BCI competition 2008–graz data set a,” Institute for Knowledge Discovery (Laboratory of Brain-Computer Interfaces), Graz University of Technology, vol. 16, pp. 1–6, 2008.
- [14] M. Hamedi, S.-H. Salleh, and A. M. Noor, “Electroencephalographic motor imagery brain connectivity analysis for BCI: a review,” Neural computation, vol. 28, no. 6, pp. 999–1041, 2016.
- [15] B. J. Edelman, B. Baxter, and B. He, “EEG source imaging enhances the decoding of complex right-hand motor imagery tasks,” IEEE Transactions on Biomedical Engineering, vol. 63, no. 1, pp. 4–14, 2015.
- [16] F. Lotte and C. Guan, “Regularizing common spatial patterns to improve BCI designs: unified theory and new algorithms,” IEEE Transactions on biomedical Engineering, vol. 58, no. 2, pp. 355–362, 2010.
- [17] J. Meng, L. Yao, X. Sheng, D. Zhang, and X. Zhu, “Simultaneously optimizing spatial spectral features based on mutual information for EEG classification,” IEEE transactions on biomedical engineering, vol. 62, no. 1, pp. 227–240, 2014.
- [18] K. K. Ang, Z. Y. Chin, H. Zhang, and C. Guan, “Filter bank common spatial pattern (FBCSP) in brain-computer interface,” in 2008 IEEE international joint conference on neural networks (IEEE world congress on computational intelligence). IEEE, 2008, pp. 2390–2397.
- [19] P. Gaur, H. Gupta, A. Chowdhury, K. McCreadie, R. B. Pachori, and H. Wang, “A sliding window common spatial pattern for enhancing motor imagery classification in EEG-BCI,” IEEE Transactions on Instrumentation and Measurement, vol. 70, pp. 1–9, 2021.
- [20] Q. Zheng, F. Zhu, J. Qin, B. Chen, and P.-A. Heng, “Sparse support matrix machine,” Pattern Recognition, vol. 76, pp. 715–726, 2018.
- [21] S. Kumar, A. Sharma, K. Mamun, and T. Tsunoda, “A deep learning approach for motor imagery EEG signal classification,” in 2016 3rd Asia-Pacific World Congress on Computer Science and Engineering (APWC on CSE). IEEE, 2016, pp. 34–39.
- [22] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for EEG decoding and visualization,” Human brain mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [23] J. Han, X. Gu, and B. Lo, “Semi-supervised contrastive learning for generalizable motor imagery EEG classification,” in 2021 IEEE 17th International Conference on Wearable and Implantable Body Sensor Networks (BSN). IEEE, 2021, pp. 1–4.
- [24] Z. Tang, C. Li, and S. Sun, “Single-trial EEG classification of motor imagery using deep convolutional neural networks,” Optik, vol. 130, pp. 11–18, 2017.
- [25] X. Zhao, H. Zhang, G. Zhu, F. You, S. Kuang, and L. Sun, “A multibranch 3d convolutional neural network for EEG-based motor imagery classification,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 27, no. 10, pp. 2164–2177, 2019.
- [26] S. Sakhavi, C. Guan, and S. Yan, “Learning temporal information for brain-computer interface using convolutional neural networks,” IEEE transactions on neural networks and learning systems, vol. 29, no. 11, pp. 5619–5629, 2018.
- [27] W. Ko, E. Jeon, S. Jeong, and H.-I. Suk, “Multi-scale neural network for EEG representation learning in BCI,” IEEE Computational Intelligence Magazine, vol. 16, no. 2, pp. 31–45, 2021.
- [28] K. Zhang, N. Robinson, S.-W. Lee, and C. Guan, “Adaptive transfer learning for EEG motor imagery classification with deep convolutional neural network,” Neural Networks, vol. 136, pp. 1–10, 2021.
- [29] K. Liu, M. Yang, Z. Yu, G. Wang, and W. Wu, “FBMSNet: A filter-bank multi-scale convolutional neural network for EEG-based motor imagery decoding,” IEEE Transactions on Biomedical Engineering, 2022.
- [30] J. F. Hwaidi and T. M. Chen, “Classification of motor imagery EEG signals based on deep autoencoder and convolutional neural network approach,” IEEE Access, vol. 10, pp. 48071–48081, 2022.
- [31] D. Zhang, K. Chen, D. Jian, and L. Yao, “Motor imagery classification via temporal attention cues of graph embedded EEG signals,” IEEE journal of biomedical and health informatics, vol. 24, no. 9, pp. 2570– 2579, 2020.

- [32] I. Dolzhikova, B. Abibullaev, R. Sameni, and A. Zollanvari, “Subjectindependent classification of motor imagery tasks in EEG using multisubject ensemble cnn,” IEEE Access, vol. 10, pp. 81355–81363, 2022.
- [33] A. Nagarajan, N. Robinson, and C. Guan, “Relevance based channel selection in motor imagery brain-computer interface,” Journal of Neural Engineering, 2022.
- [34] M. Nouri, F. Moradi, H. Ghaemi, and A. M. Nasrabadi, “Towards real-world BCI: Ccspnet, a compact subject-independent motor imagery framework,” Digital Signal Processing, vol. 133, pp. 103816, 2023.
- [35] L. F. Nicolas-Alonso, R. Corralejo, J. Gomez-Pilar, D. Alvarez,´ and R. Hornero, “Adaptive semi-supervised classification to reduce intersession non-stationarity in multiclass motor imagery-based brain–computer interfaces,” Neurocomputing, vol. 159, pp. 186–196, 2015.
- [36] X. J. Zhu, “Semi-supervised learning literature survey,” 2005.
- [37] W. Ko, E. Jeon, J. S. Yoon, and H.-I. Suk, “Semi-supervised generative and discriminative adversarial learning for motor imagery-based brain– computer interface,” Scientific reports, vol. 12, no. 1, pp. 1–14, 2022.
- [38] G. Zhang and A. Etemad, “Deep recurrent semi-supervised EEG representation learning for emotion recognition,” in 2021 9th International Conference on Affective Computing and Intelligent Interaction (ACII). IEEE, 2021, pp. 1–8.
- [39] G. Guan, Y. Hu, Q. He, B. Leng, H. Wang, H. Zou, and W. Wu, “Joint rayleigh coefficient maximization and graph based semi-supervised for the classification of motor imagery EEG,” in 2013 IEEE International Conference on Information and Automation (ICIA). IEEE, 2013, pp. 379–383.
- [40] G. Liu, G. Huang, J. Meng, D. Zhang, and X. Zhu, “Improved gmm with parameter initialization for unsupervised adaptation of brain–computer interface,” International Journal for Numerical Methods in Biomedical Engineering, vol. 26, no. 6, pp. 681–691, 2010.
- [41] D.-H. Lee et al., “Pseudo-label: The simple and efficient semi-supervised learning method for deep neural networks,” in Workshop on challenges in representation learning, ICML, 2013, vol. 3, p. 896.
- [42] A. Oliver, A. Odena, C. A. Raffel, E. D. Cubuk, and I. Goodfellow, “Realistic evaluation of deep semi-supervised learning algorithms,” Advances in neural information processing systems, vol. 31, 2018.
- [43] S. Laine and T. Aila, “Temporal ensembling for semi-supervised learning,” arXiv preprint arXiv:1610.02242, 2016.
- [44] B. Li and A. Sano, “Extraction and interpretation of deep autoencoderbased temporal features from wearables for forecasting personalized mood, health, and stress,” Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, vol. 4, no. 2, pp. 1– 26, 2020.
- [45] S. Sartipi, M. Torkamani-Azar, and M. Cetin, “A hybrid end-to-end spatio-temporal attention neural network with graph-smooth signals for EEG emotion recognition,” IEEE Transactions on Cognitive and Developmental Systems, 2023.
- [46] J. B. Kruskal, “Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis,” Psychometrika, vol. 29, no. 1, pp. 1–27, 1964.
- [47] C. Cortes, M. Mohri, and A. Rostamizadeh, “L2 regularization for learning kernels,” arXiv preprint arXiv:1205.2653, 2012.
- [48] P. Bashivan, I. Rish, M. Yeasin, and N. Codella, “Learning representations from EEG with deep recurrent-convolutional neural networks,” arXiv preprint arXiv:1511.06448, 2015.
- [49] D. Zhang, L. Yao, K. Chen, S. Wang, X. Chang, and Y. Liu, “Making sense of spatio-temporal preserving representations for EEG-based human intention recognition,” IEEE transactions on cybernetics, vol. 50, no. 7, pp. 3033–3044, 2019.
- [50] D. Zhang, L. Yao, K. Chen, S. Wang, P. D. Haghighi, and C. Sullivan, “A graph-based hierarchical attention model for movement intention detection from EEG signals,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 27, no. 11, pp. 2247–2253, 2019.
- [51] B. Sun, Z. Liu, Z. Wu, C. Mu, and T. Li, “Graph convolution neural network based end-to-end channel selection and classification for motor imagery brain-computer interfaces,” IEEE transactions on industrial informatics, 2022.
- [52] X. Li, X. Tang, S. Qiu, X. Deng, H. Wang, and Y. Tian, “Subdomain adversarial network for motor imagery EEG classification using graph data,” IEEE Transactions on Emerging Topics in Computational Intelligence, 2023.
- [53] P. Nejedly, V. Kremen, K. Lepkova, F. Mivalt, V. Sladky, T. Pridalova, F. Plesinger, P. Jurak, M. Pail, M. Brazdil, et al., “Utilization of temporal autoencoder for semi-supervised intracranial EEG clustering and classification,” Scientific reports, vol. 13, no. 1, pp. 744, 2023.
- [54] X. Li, Z. Zhao, D. Song, Y. Zhang, J. Pan, L. Wu, J. Huo, C. Niu, and D. Wang, “Latent factor decoding of multi-channel EEG for emotion

recognition through autoencoder-like neural networks,” Frontiers in neuroscience, vol. 14, pp. 87, 2020.

[55] P. Zhang, X. Wang, W. Zhang, and J. Chen, “Learning spatial–spectral– temporal EEG features with recurrent 3d convolutional neural networks for cross-task mental workload assessment,” IEEE Transactions on neural systems and rehabilitation engineering, vol. 27, no. 1, pp. 31–42, 2018.

