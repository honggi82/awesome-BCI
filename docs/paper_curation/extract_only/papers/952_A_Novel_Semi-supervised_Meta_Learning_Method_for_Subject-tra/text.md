## arXiv:2209.03785v1[eess.SP]7Sep2022

### A Novel Semi-supervised Meta Learning Method for Subject-transfer Brain-computer Interface

##### Jingcong Lia, Fei Wanga,∗∗, Haiyun Huanga, Feifei Qib, Jiahui Pana

aSchool of Software, South China Normal University, Guangzhou, China bSchool of Internet Finance and Information Engineering, Guangdong University of Finance, Guangzhou, China cPazhou Lab, Guangzhou, China

#### Abstract

Brain-computer interface (BCI) provides a direct communication pathway between human brain and external devices. Before a new subject could use BCI, a calibration procedure is usually required. Because the inter- and intra-subject variances are so large that the models trained by the existing subjects perform poorly on new subjects. Therefore, eﬀective subject-transfer and calibration method is essential. In this paper, we propose a semi-supervised meta learning (SSML) method for subject-transfer learning in BCIs. The proposed SSML learns a meta model with the existing subjects ﬁrst, then ﬁne-tunes the model in a semi-supervised learning manner, i.e. using few labeled and many unlabeled samples of target subject for calibration. It is signiﬁcant for BCI applications where the labeled data are scarce or expensive while unlabeled data are readily available. To verify the SSML method, three diﬀerent BCI paradigms are tested: 1) event-related potential detection; 2) emotion recognition; and 3) sleep staging. The SSML achieved signiﬁcant improvements of over 15% on the ﬁrst two paradigms and 4.9% on the third. The experimental results demonstrated the eﬀectiveness and potential of the SSML method in BCI applications.

Keywords: Semi-supervised, Meta learning, Transfer learning, Event-related

∗This work was supported in part by the National Natural Science Foundation of China (Grant No. 61836003, 61573150).

∗∗Corresponding author Email address: scutauwf@foxmail.com (Fei Wang)

Preprint submitted to Elsevier September 9, 2022

potential, Emotion recognition, Sleep staging.

#### 1. Introduction

Brain-computer interface (BCI) is a system to record and decode signals of human brain for the communication with external devices [1]. It provides a direct communication pathway between the paralyzed patients or those with severe motor impairments and the real world. Electroencephalogram (EEG) is widely used in practical BCI systems because EEG is cheap, easy to use, and has relative high temporal resolution among all the other non-invasive techniques. There were many diﬀerent kinds of EEG-based BCI applications, such as eventrelated potential detection [2], emotion recognition [3], sleep stage classiﬁcation [4], etc. For diﬀerent application scenarios, there are many diﬀerent kinds of BCI paradigms and diﬀerent types of EEG signals. For example, aﬀective BCI is to utilize BCI system to detect, process, and respond to the emotional states of subjects [5]. To facilitate the research of EEG-based emotion recognition, SJTU emotion EEG dataset (SEED) was released [6]. Many EEG emotion recognition algorithms were evaluated on the SEED dataset. Moreover, EEGbased BCI system could be applied to record, process and monitor the sleep stages of the chronic insomnia [7]. In order to automatically recognize the sleep stages, many machine learning algorithms were proposed and evaluated on a benchmark dataset, i. e. Sleep-EDF dataset [8]. BCI platform based on eventrelated potential (ERP) could be used to investigate age-related changes in brain function [9], external associate and communicate devices for disabled subjects [2], etc. As a matter of fact, advanced EEG decoding techniques are essential for the application and deployment of BCI systems.

In the current BCI applications, the EEG decoding performance is mainly aﬀected by the various EEG signals of diﬀerent subjects in diﬀerent time. Specifically, EEG signals rapidly change over times due to the inﬂuence of circumstance, the ﬂuctuation of BCI system and physiological/psychological conditions of subjects [1]. In addition, there are large inter-subject and intra-subject

variances of EEG signals of diﬀerent subjects, such as spatial origin, mental conditions, brain shapes, rhythms, feature types, etc [10]. As a result, the models trained by the existing subjects or data are unlikely suitable for the other subjects or the same subject in a diﬀerent time [11]. Therefore, calibration procedure is required for a new subject before using BCI system.

To calibrate EEG decoding models for new subjects, diﬀerent kinds of methods were proposed. For example, transfer Learning methods for cross-subject EEG classiﬁcation in BCI systems had attracted much attention in the past few years [12]. To eﬀectively deploy EEG-based sensorimotor BCI system, a crosssubject EEG decoding method was proposed [13]. Transfer learning method based on riemannian geometry was eﬀective for cross-subject classiﬁcation in BCI applications [14]. A new convolutional neural network, termed DynamicNet, achieved state-of-the-art performance of cross-subject classiﬁcation in motor imagery [15]. Domain adaption technique is able to learn knowledge from source domain and transfer to a new target domain. An easy domain adaptation method was proposed for cross-subject multi-view emotion recognition [16]. However, it is diﬃcult and time-consuming to collect suﬃcient high-quality labeled data for calibration. And the current cross-subject decoding methods could not compensate the large inter- and intra-subject variance of subjects in diﬀerent circumstances. Therefore, eﬀective subject-transfer and calibrating method is signiﬁcant.

Meta learning, known as learning to learn is a speciﬁc machine learning methodology which aims to learn knowledge or experience from meta data or source domain and eﬀectively learn new tasks in the target domain. Recently, meta learning method was proven to be a powerful tool to capture common knowledge or experiences of diﬀerent subjects which could be transferred to a new incoming subject for better decoding performance [17, 18, 19]. Usually, a meta learning method will ﬁrstly train a meta learner with many labeled samples of source subjects and ﬁne-tune/calibrate meta learner with few-shot labeled samples for a new incoming subject [20, 21, 22]. A few-shot relation learning method was proposed for cross-subject motor imagery classiﬁcation

performance [23]. The relation learning method was applied to learn representative features of unseen subject categories and how to classify them with limited number of samples. A prototype network based on SPD matrix was proposed for domain adaptation EEG emotion recognition [24]. The proposed prototype network could transfer knowledge by feature adaptation with distribution confusion and sample adaptation with centroid alignment. Siamese neural network is a speciﬁc meta learning method based on metric between samples. A multimodalSiamese neural network was applied for person veriﬁcation [25]. These studies demonstrated that meta learning methods are promising for subject-transfer EEG decoding and calibration in BCIs.

To reduce the discrepancy between target and source distributions, meta learning method like model agnostic meta-learning (MAML) could be applied for subject-transfer learning [26]. With MAML method, EEG decoding network could be pre-trained by the averaged gradients of source subjects and ﬁne-tune the network with just few-shot labeled samples of a new incoming subject for his/her calibration [4, 27]. However, one major problem of the MAML method is that the calibration procedure using only few samples will cause over-ﬁtting and performance degradation on target subject. Because only a small fraction of labeled samples are unlikely to capture intrinsic data distribution of target subject. Generally, the labeled data are scarce or expensive while unlabeled data are readily available in BCI applications and neuroscience studies. Therefore, semi-supervised learning methods are received much attention.

In this paper, we combine semi-supervised learning and meta learning methods to transfer EEG decoding models for new subjects just with few-shot labeled and many unlabeled samples. The main contributions of this paper can be summarized as follows:

- 1. A novel semi-supervised meta learning (SSML) method is proposed for subject-transfer EEG decoding.
- 2. The proposed method is ﬂexible for diﬀerent BCI paradigms including event-related potential detection, emotion recognition and sleep staging

- tasks.
- 3. The SSML could signiﬁcantly improve EEG decoding performance on new subjects, e.g. improvements of over 15% in ERP and emotion paradigms and 4.9% in the sleep paradigm.

The remainder of this paper is organized as follows. The proposed SSML method is presented in Section II. In Section III, numerical experiments on event-related potential detection, emotion recognition and sleep staging datasets are carried out. And the performance of the current methods and the proposed method are presented and compared. Some discussions and analysis of the proposed method are presented in Section IV. Conclusions of this paper are given in Section V.

#### 2. Proposed Method

As aforementioned, transfer learning cross subjects is signiﬁcant for BCI applications and neuroscience researches. However, it is quite challenging for subject-transfer EEG decoding due to individual variances of EEG signals, such as mental conditions, brain shapes, rhythms, feature types, etc. Here, we proposed a semi-supervised meta learning (SSML) algorithm to train EEG decoding model from source subjects and transfer it to new incoming target subjects.

- 2.1. Model agnostic meta-learning algorithm Meta learning is to learn model for a variety of tasks and achieve best perfor-

mance on a distribution of tasks, including potentially unseen tasks. In practical, the subject-transfer learning in BCI could be considered as a meta learning problem that each task refer to the classiﬁcation of each subjects neural signals.

Meta learning approaches could be categorized into three kinds, i. e. modelbased, metric-based and optimization-based [28]. Model-based method relies on designing suitable models for fast learning on new task. Metric-based approach aims to learn a good kernel of distance metric which is applicable to common tasks as well as the unseen tasks. Optimization-based method could

adjust the optimization algorithm on new task after learning a few examples. Model-agnostic meta-learning (MAML) is a fairly general optimization algorithm, compatible with any model that learns through gradient descent [26]. According to the recent studies [29, 30, 31, 32, 4], MAML method achieved impressive performance in diﬀerent kinds of few-shot learning problems.

Here is a dataset D =< S,Q > where S = {(Xs,Ys)} is a support set of source subjects with EEG samples Xs and the associated labels Ys, and Q = {(Xq)} is a query set of a target subject with unlabeled sample Xq. The subject-transfer learning problem in BCI is to learn a model with the support set and apply the model on target subject to predict the labels of query set. The model’s parameter θ∗ is optimized as follow:

θ∗ = arg max

E(x,y)∈S[pθ(y |x)] (1) where p denotes the posterior probability of the classiﬁer to classify a given sample x to a speciﬁc class y in support set S. By maximizing the expectation E of support set, the model is optimized. Furthermore, the optimized model could be applied on target subject to predict the labels of query set.

θ

As shown in Algorithm 1, MAML algorithm is to learn a meta-learner by a support set with Ns source subjects S = {(Xs,Ys)}N

s=1. Given a model fθ with parameters θ, it could be optimized by gradient descent approach as

s

θi∗ ← θ − α∇θLTi

(fθ) (2) where L denotes the loss between the model’s output probability and the associated label of the given data Ti of the i-th source subject, ∇θ is the gradient computed by the loss, α is the learning rate.

The above optimized parameters θi∗ is just for one subject. For better generalization across the other subjects, we sample a subset of M subjects from source S and train a meta-learner for more eﬃcient subject-transfer learning. The meta-learner’s parameters could be optimized by the averaged gradients of multiple source subjects as

θ ← θ − β∇θ

Ti∈S

LTi

(fθ∗

##### ) (3)

i

- Algorithm 1 Model agnostic meta-learning algorithm Require: Backbone network fθ, base learning rate α, meta learning rate β

Require: Labeled data of source subjects S = {(Xs,Ys)}N

s=1.

s

- 1: while not done do
- 2: Sample a subset of M subjects from source S.
- 3: for all Ti,i ∈ 1,...M do
- 4: Update base learner parameters θ∗:

θi∗ ← θ − α∇θLTi

(fθ)

- 5: end for
- 6: Update meta-learner parameters θ:

θ ← θ − β∇θ Mi=1 LTi

(fθ∗

i

)

- 7: end while

where Ti denotes the i-th subject in support set S, β is the learning rate to train the meta-learner. For calibration on new subjects, the trained meta-learner is ﬁne-tuned by few labeled samples of a new incoming subject with Equation (2).

According to the recent studies [30, 4, 27], meta learning methods including MAML were used for subject-transfer EEG classiﬁcation that they require some labeled data of the unseen subject for fast adaption. However, the EEG signals of a subject vary a lot in diﬀerent sessions/time. Only few labeled samples are unlikely to capture the real distribution of EEG signals of a new incoming subject. Generally, the labeled data are scarce or expensive while unlabeled data are readily available in BCI applications and neuroscience studies. Therefore, we would like to combine semi-supervised learning and meta learning methods to transfer EEG decoding models for new subjects just with few-shot labeled and many unlabeled samples.

- 2.2. Semi-supervised meta learning algorithm In the BCI applications like sleep staging, the labeled data are scarce or

expensive and unlabeled data are readily available for new incoming subjects.

|Backbone Net<br><br>h2}<br><br>h1 hi| |
|---|---|
| | |

# }

|Deep learned Features (h)|
|---|

h1 hi

|Cross-entropy Loss| |
|---|---|
| | |

p h2

- 1

p

- 2

Input

| | |
|---|---|
| | |

Output Prob.(p)

|C1<br><br>C2<br><br>Pre-Train<br><br>fθ|
|---|

|Semi-supervised Adapt.<br><br>C1<br><br>C2<br><br>(p>ε, d<ς)<br><br>(p>ε, d<ς)<br><br>D1<br><br>D2<br><br>}<br><br>ς<br><br>}<br><br>ς<br><br>fθ<br><br>fθ<br><br>,<br><br>(p>ε, d>ς) (p<ε, d<ς)|
|---|

| |λ|
|---|---|
|Center Loss| |

[Figure 1]

[Figure 2]

| |
|---|

[Figure 3]

[Figure 4]

| |
|---|

[Figure 5]

[Figure 6]

| |
|---|

Source Subjects

[Figure 7]

[Figure 8]

| |
|---|

Target Subject

- : Center of Class 1
- : Center of Class 2

: Labeled Samples : Unlabeled Samples

C1 C2

D1 : New Center of Class 1 D2 : New Center of Class 2

Figure 1: Semi-supervised meta learning algorithm for subject-transfer EEG decoding.

Therefore, it is of great interests to develop a semi-supervised learning method which could exploit labeled and unlabeled data to ﬁne-tune the model for target subject. According to the previous research, semi-supervised learning method was used for brain signal feature extraction [33, 34, 35] and improving signal decoding performance for EEG-based emotion recognition, sleep stage classiﬁcation, diagnosis of brain disease, etc [36, 37, 38, 39].

Here, we proposed a semi-supervised meta learning (SSML) algorithm for subject-transfer EEG decoding as shown in Fig. 1. The whole architecture could be divided into two phases, i. e. the pre-training phase and semi-supervised adaption phase.

In the pre-training phase, the backbone network fθ is trained by the labeled EEG signals of source subjects. To enhance inter- and intra-subject discriminative features learned by deep backbone network, we applied an additional loss function (termed center loss) for regulation [40]. The deep learned features are the outputs of the last hidden layer in the backbone network. The center loss function aims to learn a center for features of each class, and penalizes the distances between the features and the corresponding class centers. As a result, the center of each class C1/C2 is pre-trained by source subjects as shown in Fig. 1.

In the semi-supervised adaption phase, the pre-trained network is ﬁne-tuned by the averaged gradient of few-shot labeled and unlabeled samples of the target subject. Here, only the unlabeled samples with high output probabilities (p > ε) and close to the class center (d < ς) are included for ﬁne-tuning while the rest samples (p < ε or d > ς) are ignored. Then, the previous class centers (C1, C2) are transferred to the new ones (D1, D2) for target subject that the network f θ is ﬁne-tuned for the target subject as shown in Fig. 1.

The joint loss function which combines center loss and cross entropy loss is as follows.

m

2 2

LC = 21

hi − cy

i

i=1

m

(4)

LS = −

yi log(pi) L = LS + λLC

i=1

where hi denotes the output feature of the last hidden layer of the backbone network given the i-th input sample, cy

is the yi-th class center, pi is the output of the network, yi is the ground truth, LS is cross-entropy classiﬁcation loss, λ is the weight of center loss LC. The feature center cy

i

for each class is considered as learnable parameters which is learned by gradient descent method [40]. Its gradient is as follows.

i

∂LC ∂hi = hi − cy

i

m i=1 δ(yi=j)·(cj−hi)

cj =

1+ mi=1 δ(yi=j)

(5)

where δ(condition) = 1 if the condition is satisﬁed, and δ(condition) = 0 if not.

Based on the Algorithm 1, the backbone network is pre-trained by the joint loss function as shown in Fig. 1. Then, the pre-trained network is ﬁne-tuned in a semi-supervised manner with few-shot labeled EEG signals Tq = {(xq,yq)}Nq=1q and unlabeled signals Xt = {xj} of the target subject.

In the semi-supervised adaption phase, only part of the unlabeled signals are eligible and selected for ﬁne-tuning. First, each unlabeled signal xi ∈ Xt is fed into the network to obtain its feature hj and the corresponding output oj as shown in Algorithm 2. Second, the argmax function is applied to transform the network output oj into the artiﬁcial label yj and the associated predict

- Algorithm 2 Semi-supervised meta learning algorithm Require: Pre-trained network fθ, base learning rate α, ﬁne-tuning rate γ, con-

ﬁdence and distance thresholds ε, ς.

Require: Few-shot labeled signals Tq = {(xq,yq)}Nq=1q and unlabeled signals

Xt = {xj} of target subject.

- 1: Obtain output of network (oj,hj) = fθ(xj),xj ∈ Xt
- 2: Generate artifact labels (pj,yj) = arg max(oj)
- 3: Calculate distance from center dj = 21n hj − cy

j

2 2

- 4: Construct support set: Q = {(xj,yj)},s.t.pj > ε,dj < ς
- 5: while not done do
- 6: Sample class-balanced support set B = {Tj} from Q
- 7: for all Tj do
- 8: Update base learner parameters θ∗:

θj∗ ← θ − α∇θLTj

(fθ)

- 9: end for
- 10: Update meta-learner parameters θ:

θ ← θ − γ∇θ Tj∈B[LTj

(fθ∗

j

) + LTq

(fθ∗

j

)]

- 11: end while

probability pj. Third, the feature distance of each signal from the corresponding class center is calculated. The feature distance denotes the element-wise averaged center loss of feature vector. Fourth, only the signals with high probabilities and close to the class center are included in the support set. The feature distance from center dj and the support set are deﬁned as follows:

2 2

dj = 21n hj − cy

j

Q = {(xj,yj)},s.t.pj > ε,dj < ς

(6)

where n is the length of each feature vector hj for normalization of feature distance, ε and ς are the conﬁdence threshold and distance threshold, only the samples with high predicting probabilities (pj > ε) and close to the class center

(dj < ς) are included in the support set Q. Fifth, we down-sample and obtain a class-balanced subset B from the support set for eﬀective training and unbias classiﬁcation on each class. Then, the backbone network is ﬁne-tuned by the averaged gradient of the artiﬁcial support set B and few-shot labeled samples Tq.

Consequently, the ﬁne-tuned model could be applied for classiﬁcation tasks of the target subject. With a semi-supervised adaption, the proposed SSML method utilizes labeled and unlabeled data to achieve better EEG decoding performance for new incoming target subject. Next, we will conduct a series of experiments to evaluate the proposed SSML method and compare it with the other methods.

#### 3. Experiments

In this section, we present the details of the experiments on the proposed method. In addition, the corresponding results of the other state-of-the-art methods are also present for comparison. In our experiments, the hardware and software conﬁguration used in our experiments are based on a platform with an Nvidia RTX 2080Ti, Ubuntu 16.04, PyTorch 1.9.0.

- 3.1. Datasets In the experiments, the proposed method is veriﬁed by three diﬀerent EEG

paradigms including ERP detection, emotion recognition and sleep staging. The feasibility of the proposed method on diﬀerent kinds of paradigms are signiﬁcant.

ERP is a fundamental technique in BCI applications and neuroscience. The 32-channel EEG signals of four severely disabled and four able-bodied subjects were recorded and released as benchmark dataset for ERP detection [2]. The ERP/NoERP signals were extracted and averaged to enhance signal-to-noise rate. Then, there are 24 ERP and 120 NoERP signals for each subject. Each ERP/NoERP signal is represented by a 32 ∗ 128 matrix which denotes 32 channels and 128 time points in 1 second.

The SJTU emotion EEG dataset (SEED) is a benchmark dataset for evaluating EEG emotion recognition algorithms [6]. The 62-channel EEG signals stimulated by happy, sad and neutral ﬁlm clips were recorded. We extracted the diﬀerential entropy features of 5 frequency channels in every 10 second frame that each sample is represented by a 62 ∗ 10 ∗ 5 matrix. There are total 15 subjects and 993 samples for each subject in the dataset.

Sleep-EDF dataset from MCH-Westeinde Hospital was a benchmark dataset for EEG sleep staging methods [8]. Here, the sleep EEG signals in Fpz-Cz channel of 20 healthy subjects in Sleep-EDF dataset were used for experiments. Each EEG signal is segmented into 30-second frames, totally 3000 time-points in one frame. There are ﬁve sleep stages, i.e. wake(W), non-rapid eye movement (NREM: N1, N2, and N3), rapid eye movement (REM). The number of sleep EEG signals of each subject varies from 2000 to 6000.

Based on the meta learning methodology, the model could be pre-trained by labeled data of the existed source subjects and ﬁne-tuned for a new incoming subject with only few labeled data. Therefore, leave-one-subject-out (LOSO) cross-validation strategy was applied for evaluating subject-transfer EEG decoding performance. For example, seven of the eight subjects in ERP dataset are selected as source subjects for training while the rest one is the target subject for testing. A few labeled samples of target subject are collected for ﬁne-tuning the model. Then, the classiﬁcation accuracies of the eight runs of LOSO experiments are averaged as ﬁnal testing performance.

- 3.2. Model As a variant of model-agnostic meta-learning, the proposed SSML method is

also feasible on diﬀerent network structures. To study the performance variances of the proposed method on diﬀerent network structures, we built three kinds of networks including multi-layer perception (MLP), spatial-temporal ﬁltering neural network (STNN) and convolutional neural network (CNN).

In Table 1, three backbone models for ERP detection dataset are presented as examples. In the MLP model, the 32 × 128 input signal is ﬁrstly ﬂattened

into a 1×4096 vector and fed into a linear hidden layer with 300 Relu activation units and an output layer with 2 Softmax activation units. In the STNN model, a linear spatial ﬁltering layer with 16 ﬁlters and a temporal ﬁltering layer with 64 ﬁlters are used to extract spatial and temporal features, respectively. Then the obtained 16 × 64 feature is ﬂattened into a 1 × 1024 vector and fed into the output layer. In the CNN model, convolutional (Conv) layers with Relu activation, Max-pooling (Pool) layers and a linear output layer with Softmax activation are used. As for emotion and sleep datasets, the backbone models are similar to those for ERP that needs to modify the structure to ﬁt the signals with diﬀerent number of channels or time lengths.

Table 1: Backbone models for ERP detection includes MLP, STNN and CNN.

MLP CNN Layer Settings Output Layer Settings Output Input 32 × 128 Input 32 × 128

Flatten 1 × 4096 Conv (1 × 16)*16 (16, 32 × 113) Hidden 4096 × 300 1 × 300 Pool 1 × 2 (16, 32 × 56) Output 300 × 2 2 Conv (1 × 3)*32 (32, 32 × 54)

Pool 1 × 2 (32, 32 × 27)

STNN Conv (1 × 3)*64 (64, 32 × 25) Layer Settings Output Pool 1 × 2 (64, 32 × 12) Input 32 × 128 Conv (1 × 3)*128 (128, 32 × 10)

Spatial 16 × 32 16 × 128 Conv

(32 × 1)*256 (256, 1 × 10)

Temporal 128 × 64 16 × 64 (Spatial) Flatten 1 × 1024 Flatten 1 × 2560 Output 1024 × 2 2 Output 2560 × 2 2

To train the backbone network, we applied Adam optimizer with base learning rate of 0.001 and meta learning rate of 0.0001. To learn feature centers for diﬀerent classes, stochastic gradient descent optimizer is applied with a learning rate of 0.001 and a center-loss weight of 0.001. The conﬁdence threshold and distance threshold are 0.9 and 1 which are used to generate support set for ﬁne-tuning the backbone network.

In the pre-training phase, 90 percent of source subjects are used to train the backbone network while the rest 10 percent is the validation set for monitoring. Once the classiﬁcation performance of the validation set is maximized, the training procedure will be stopped. For the target subject of LOSO experiment, few-shot labeled samples of each class are randomly selected for ﬁne-tuning the pre-trained network. The network is ﬁne-tuned by 10 epochs using Adam optimizer with learning rate of 0.001 and weight decay of 0.001.

- 3.3. Results

Table 2: Performance of diﬀerent methods on three EEG benchmark datasets.

ERP Detection Emotion Recognition Sleep Staging

Methods Accuracy Method Accuracy Method Accuracy BLDA [2] 0.8511 DGCNN [41] 0.6639 Stack SAE [42] 0.7890 STDA [43] 0.8279 DAN [44] 0.7134 SVM [45] 0.8272 KNN [46] 0.8564 BiHDM [47] 0.7722 CNN [42] 0.7480 SVM [48] 0.8420 RGNN [49] 0.7957 Multi-task CNN [50] 0.8190 CNN [51] 0.8547 SOGNN [52] 0.8104 DeepSleepNet [53] 0.8200 W/O Meta 0.8329 W/O Meta 0.7694 W/O Meta 0.7942 MAML [26] 0.8912 MAML[26] 0.8355 MAML[26, 4] 0.8086 SSML(ours) 0.9521 SSML(ours) 0.8859 SSML(ours) 0.8331

In Table 2, we present the performance of state-of-the-art methods and the

proposed method on the benchmark datasets including ERP detection, emotion recognition and sleep staging tasks. According to the previous research [4, 27], MAML could be used for subject-transfer EEG classiﬁcation, such as sleep staging. Here, we used convolutional neural network as backbone network for MAML method and the proposed SSML method. In the MAML method, the labeled data of many source subjects were used to pre-train a backbone network by Algorithm 1. Then, the pre-trained backbone network will be ﬁne-tuned by few labeled samples of target subject to achieve better performance. The baseline method W/O Meta denotes the pre-trained network without using any data from target subject for ﬁne-tuning. In the ERP detection paradigm, we obtained the performance of the other methods by using sklearn toolbox or rebuilding the model with source subjects and labeled samples of target subject. For emotion recognition and sleep staging, we referred to the state-of-the-art performance recently.

In the proposed SSML method, the backbone network is pre-trained by the source subjects, then ﬁne-tuned by few-shot labeled samples and unlabeled samples of target subject. For the emotion recognition and sleep staging paradigms, 10-shot labeled samples of each class are selected for ﬁne-tuning in the MAML and SSML method. For the ERP paradigms with less samples of each subject, 5-shot setting is used in the experiments. The proposed SSML method achieved better performance than the other methods and MAML method in diﬀerent EEG paradigms.

Moreover, we would like to study how much the classiﬁcation performances are improved when using few labeled samples for ﬁne-tuning with the MAML and the proposed SSML methods. The classiﬁcation performance of the W/O meta method is considered as the baseline performance for each paradigm. Compared with the baseline, the SSML method achieved great improvements with only 1-shot labeled sample of each class as shown in Table 3. As the increase of labeled samples, the MAML and SSML methods achieved much higher performance. That is to say, using more labeled samples is helpful to model real distribution of the target subject’s EEG signals that the EEG decoding performance

Table 3: Classiﬁcation performance improvements of MAML and SSML compared with W/O meta method.

Paradigm Method 1-shot 3-shot 5-shot 10-shot

#### MAML 4.80% 6.30% 7.00% 9.52% SSML 10.00% 12.60% 14.31% 16.10%

ERP

#### MAML 4.40% 4.00% 6.70% 8.59% SSML 5.90% 10.90% 10.30% 15.14%

Emotion

#### MAML 0.80% 1.50% 1.60% 1.80% SSML 2.20% 3.80% 3.40% 4.90%

Sleep

could be substantially improved. Consequently, the proposed SSML method with 10-shot labeled samples achieved over 15% improvement in the ERP and emotion recognition paradigms and 4.9% in sleep staging paradigm. Moreover, the proposed SSML method achieved higher improvements than MAML in different few-shot settings.

Table 4: Wilcoxon signed rank test between SSML and the baseline methods.

Paradigm SSML VS # 1-shot 3-shot 5-shot 10-shot

W/O Meta †† †† †† †† MAML † † †† ††

ERP

W/O Meta †† † †† †† MAML † †† † ††

Emotion

W/O Meta ∼ † †† †† MAML ∼ ∼ †† ††

Sleep

Note: ∼ nonsigniﬁcant, †p < 0.05, ††p < 0.01

Furthermore, we wonder whether the performance improvements of the proposed SSML method are statistically signiﬁcant. Therefore, the performance diﬀerences between the proposed method and the other methods should be stud-

ied by statistical analysis method. As shown in Table 4, the Wilcoxon signed rank test results between the proposed SSML and the W/O meta method or MAML method are presented. In the ERP detection and Emotion recognition paradigms, the proposed SSML method achieved signiﬁcant higher performance than the other two methods in diﬀerent few-shot settings. In the sleep staging paradigm, signiﬁcant improvements are found in 5-shot and 10-shot settings. The experimental results demonstrated the eﬀectiveness and potential of the proposed SSML method in improving subject-transfer EEG decoding performance.

#### 4. Discussion

Here, the proposed method is discussed in qualitative and quantitative manner. First, to analyse the convergence procedure of diﬀerent methods with different backbone networks on diﬀerent EEG paradigms, the learning curves are present. Second, we discuss the subject-transfer decoding performance when changing the number of labeled samples of target subject. Third, we change the weight of center loss and analyse its contribution for improving classiﬁcation performance. Finally, we utilized the t-SNE technique to analyse how the proposed SSML method inﬂuences the classiﬁcation in the feature domain.

- 4.1. Comparison of Learning Curves Three diﬀerent backbone models are trained by diﬀerent meta-learning meth-

ods and evaluated on three datasets. The convergence procedure of diﬀerent methods could be visualized by their learning curves as the increase of iteration epochs [54]. In Fig. 2, the learning curves of three diﬀerent models trained by diﬀerent meta-learning methods on three EEG datasets are presented. Here, each learning curve denotes the averaged classiﬁcation accuracy in the LOSO cross-validation experiments.

Firstly, we evaluated three diﬀerent kinds of neural networks including MLP, STNN and CNN. The signal of sleep dataset is one-channel EEG signal that

ERP Emotion Sleep

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

MLPSTNNCNN

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

W/O Meta

MAML

SSML

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

Figure 2: Learning curves of three methods with diﬀerent networks on diﬀerent EEG paradigms.

the STNN with spatial ﬁltering is infeasible and ignored. Apparently, the CNN achieved the higher performance than MLP or STNN. That is to say, the network structure also plays an important role in subject-transfer EEG decoding. Secondly, we could ﬁnd that the proposed SSML method achieved better performance than the other meta-learning methods. Speciﬁcally, its learning curve (red) is higher than the other methods within the same model and dataset. Thirdly, the SSML method could achieve faster convergence than the other two methods in the experiments of three diﬀerent networks. The comparison of learning curves demonstrated the eﬀectiveness of the SSML with CNN network in diﬀerent paradigms.

- 4.2. Consideration of N-shot Learning The calibration procedure of BCI for new subjects could be considered as

few-shot learning problem. In the meta learning methods, few labeled samples of target subject are obtained for calibration, i.e. ﬁne-tuning the EEG decoding model for this subject. In the SSML method, few labeled samples and many

##### unlabeled samples are jointly used for ﬁne-tuning.

Figure 3: Performance of SSML method with diﬀerent shots of labeled samples.

Here, we would like to analyse the inﬂuence of the number of labeled samples for calibration. In Fig. 3, the classiﬁcation accuracies of the SSML method with 0, 1, 2, 3, 5 and 10-shot settings are presented. The SSML in 0-shot setting denotes that only unlabeled samples are used for ﬁne-tuning for target subject. Without labeled data of target subject, the classiﬁcation performance is relatively poor. As the increase of the number of shots, the EEG decoding model is calibrated more accurately for the target subject. As a result, the classiﬁcation accuracies are improved, especially in the ERP and emotion paradigms. The improved classiﬁcation performance demonstrated the eﬀectiveness of the proposed SSML for few-shot learning and calibration on new subjects.

- 4.3. Eﬀect of Center Loss weights As aforementioned, the center loss and the associated feature distance are

essential in the pre-training phase and semi-supervised adaption phase of SSML. Here, we would like to analyse the contribution and inﬂuence of center loss in decoding diﬀerent EEG signals. The center loss function plays important role in dominating the intra-class variations in the joint loss function. It is intuitive to compare the classiﬁcation performance when using joint loss function with

Figure 4: Performance of SSML method with diﬀerent center weights.

diﬀerent center weights. As shown in Fig. 4, the center weights between 1e − 4 and 1e−2 have higher performance than the other weights that is similar to the previous research [40]. The center weight of 1e − 3 is used in our experiments.

- 4.4. T-SNE Analysis As shown in the Fig. 1, the EEG features of diﬀerent subjects are learned

by the backbone network. We would like to analyse the diﬀerences of features obtained by diﬀerent methods. To visualize high-dimensional features, t-distributed stochastic neighbor embedding (t-SNE) method is widely used. In Fig. 5, the t-SNE results of features learned by diﬀerent method with CNN as backbone network are presented. Here, we chose one subject from each dataset for presentation. In each subﬁgure, the t-SNE results are presented in scatterplot in which the diﬀerent colors denote the labels of samples. The samples of ERP and NoERP, three emotion classes, ﬁve sleep stages are presented.

In the t-SNE maps of the W/O meta method, the points from diﬀerent classes are mixed with each other that the classiﬁcation performance is not well. With MAML, a few labeled samples are used for fast adaption that the pre-trained network could be ﬁne-tuned for the target subject. Based on the proposed SSML method, few labeled and many unlabeled samples are combined

w/o Meta MAML SSML

| | | |
|---|---|---|
| | | |
| | | |

ERP

NoERP

Emotion

Negative Neutral Positive

Sleep W

- N1
- N2
- N3 REM

Figure 5: T-SNE results of diﬀerent methods in diﬀerent paradigms.

for semi-supervised adaption. Compared with the other methods, the samples of ERP class, three emotion class and wake (W) stage are likely separated by the SSML method. The t-SNE results veriﬁed that the proposed SSML method achieved better subject-transfer EEG decoding performance.

- 4.5. Limitations The limitations of this study are as follows. First, the proposed method is

only veriﬁed by three EEG paradigms with three backbone network structures in the experiments. Further researches on the other kinds of paradigms and networks should be conducted to verify the feasibility of the proposed method. Second, given a backbone network with relatively low performance, its performance will be even worse after apply semi-supervised adaption. That is to say, the proposed SSML method depends heavily on the eﬀective network structures. Third, the proposed SSML method will be invalid if the features of the target subject are completely diﬀerent with source subjects. Because

the semi-supervised adaption phase of SSML is based on the backbone network pre-trained by the source subjects. Fourth, it also takes much times to collect few-shot labeled and many unlabeled samples for the calibration procedure of the proposed method. Further work is thus required to improve subject-transfer and calibration methods for EEG decoding in BCI as well as neuroscience.

#### 5. Conclusion

In this paper, we propose a semi-supervised meta learning (SSML) method for subject-transfer EEG decoding in brain-computer interfaces. In a semisupervised manner, the proposed method could eﬀectively transfer the model trained by source subjects to new incoming subject. To verify the method, three diﬀerent EEG paradigms including event-related potential, emotion recognition and sleep staging are tested. By using few-shot labeled and many unlabeled samples for ﬁne-tuning, the proposed method could obviate inter- and intra-subject variability between source subjects and target subject. With a semi-supervised adaption procedure, the SSML achieved signiﬁcantly improvements of target subjects. Moreover, the proposed method achieved better performance than the existing methods. Therefore, the proposed semi-supervised meta-learning method has much potentials in improving EEG decoding performance which is signiﬁcant for practical BCI applications as well as neuroscience research.

#### References

- [1] F. Lotte, Signal processing approaches to minimize or suppress calibration time in oscillatory activity-based brain–computer interfaces, Proceedings of the IEEE 103 (6) (2015) 871–890.
- [2] U. Hoﬀmann, J.-M. Vesin, T. Ebrahimi, K. Diserens, An eﬃcient p300based brain–computer interface for disabled subjects, Journal of Neuroscience methods 167 (1) (2008) 115–125.

- [3] J. Li, S. Qiu, Y.-Y. Shen, C.-L. Liu, H. He, Multisource Transfer Learning for Cross-Subject EEG Emotion Recognition, IEEE Transactions on Cybernetics (2019) 1–13.
- [4] N. Banluesombatkul, P. Ouppaphan, P. Leelaarporn, P. Lakhan, B. Chaitusaney, N. Jaimchariyatam, E. Chuangsuwanich, W. Chen, H. Phan, N. Dilokthanakul, T. Wilaiprasitporn, MetaSleepLearner: A Pilot Study on Fast Adaptation of Bio-Signals-Based Sleep Stage Classiﬁer to New Individual Subject Using Meta-Learning, IEEE Journal of Biomedical and Health Informatics 25 (6) (2021) 1949–1963.
- [5] C. Mu¨hl, B. Allison, A. Nijholt, G. Chanel, A survey of aﬀective brain computer interfaces: principles, state-of-the-art, and challenges, BrainComputer Interfaces 1 (2) (2014) 66–84.
- [6] R.-N. Duan, J.-Y. Zhu, B.-L. Lu, Diﬀerential entropy feature for EEGbased emotion classiﬁcation, in: 2013 6th International IEEE/EMBS Conference on Neural Engineering (NER), 2013, pp. 81–84.
- [7] P. Chriskos, C. A. Frantzidis, C. M. Nday, P. T. Gkivogkli, P. D. Bamidis, C. Kourtidou-Papadeli, A review on current trends in automatic sleep staging through bio-signal recordings and future challenges, Sleep medicine reviews 55 (2021) 101377.
- [8] B. Kemp, A. Zwinderman, B. Tuk, H. Kamphuisen, J. Oberye, Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the EEG, IEEE Transactions on Biomedical Engineering 47 (9) (2000) 1185–1194.
- [9] P. D. Kieﬀaber, H. R. Okhravi, J. N. Hershaw, E. C. Cunningham, Evaluation of a clinically practical, erp-based neurometric battery: application to age-related changes in brain function, Clinical Neurophysiology 127 (5)

(2016) 2192–2199.

- [10] C.-S. Wei, Y.-P. Lin, Y.-T. Wang, C.-T. Lin, T.-P. Jung, A subject-transfer framework for obviating inter-and intra-subject variability in EEG-based drowsiness detection, NeuroImage 174 (2018) 407–419.
- [11] O.-Y. Kwon, M.-H. Lee, C. Guan, S.-W. Lee, Subject-Independent BraincComputer Interfaces Based on Deep Convolutional Neural Networks, IEEE Transactions on Neural Networks and Learning Systems 31 (10) (2020) 3839–3852.
- [12] D. Wu, Y. Xu, B.-L. Lu, Transfer learning for EEG-based brain-computer interfaces: A review of progress made since 2016, IEEE Transactions on Cognitive and Developmental Systems (2020) 1–1.
- [13] S. Saha, M. Baumert, Intra-and inter-subject variability in EEG-based sensorimotor brain computer interface: a review, Frontiers in computational neuroscience 13 (2020) 87.
- [14] M. Congedo, A. Barachant, R. Bhatia, Riemannian geometry for EEGbased brain-computer interfaces; a primer and a review, Brain-Computer Interfaces 4 (3) (2017) 155–174, number: 3.
- [15] A. Zancanaro, G. Cisotto, J. R. Paulo, G. Pires, U. J. Nunes, CNN-based approaches for cross-subject classiﬁcation in motor imagery: From the state-of-the-art to dynamicnet, arXiv preprint arXiv:2105.07917.
- [16] C. Chen, C.-M. Vong, S. Wang, H. Wang, M. Pang, Easy domain adaptation for cross-subject multi-view emotion recognition, Knowledge-Based Systems 239 (2022) 107982.
- [17] R. Ning, C. Philip Chen, T. Zhang, Cross-subject EEG emotion recognition using domain adaptive few-shot learning networks, in: IEEE International Conference on Bioinformatics and Biomedicine (BIBM), 2021, pp. 1468– 1472.

- [18] D. Li, P. Ortega, X. Wei, A. Faisal, Model-agnostic meta-learning for EEG motor imagery decoding in brain-computer-interfacing, in: IEEE/EMBS Conference on Neural Engineering (NER), 2021, pp. 527–530.
- [19] S. Choi, Meta-learning: Towards fast adaptation in multi-subject EEG classiﬁcation, in: 2021 9th International Winter Conference on BrainComputer Interface (BCI), 2021, pp. 1–1.
- [20] T. Duan, M. Chauhan, M. A. Shaikh, J. Chu, S. Srihari, Ultra eﬃcient transfer learning with meta update for cross subject EEG classiﬁcation, arXiv preprint arXiv:2003.06113.
- [21] S. Choi, Meta-learning: Towards fast adaptation in multi-subject EEG classiﬁcation, in: 2021 9th International Winter Conference on BrainComputer Interface (BCI), IEEE, 2021, pp. 1–1.
- [22] S. Bhosale, R. Chakraborty, S. K. Kopparapu, Calibration free meta learning based approach for subject independent EEG emotion recognition, Biomedical Signal Processing and Control 72 (2022) 103289.
- [23] S. An, S. Kim, P. Chikontwe, S. H. Park, Few-shot relation learning with attention for EEG-based motor imagery classiﬁcation, in: 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), IEEE, pp. 10933–10938.
- [24] Y. Wang, S. Qiu, X. Ma, H. He, A prototype-based SPD matrix network for domain adaptation EEG emotion recognition, Pattern Recognition 110

(2021) 107626.

- [25] D. D. Chakladar, P. Kumar, P. P. Roy, D. P. Dogra, E. Scheme, V. Chang, A multimodal-siamese neural network (msnn) for person veriﬁcation using signatures and EEG, Information Fusion 71 (2021) 17–27.
- [26] C. Finn, P. Abbeel, S. Levine, Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks, arXivArXiv: 1703.03400.

- [27] M. Bontonou, G. Lioi, N. Farrugia, V. Gripon, Few-Shot Decoding of Brain Activation Maps, in: 2021 29th European Signal Processing Conference (EUSIPCO), IEEE, Dublin, Ireland, 2021, pp. 1326–1330.
- [28] T. M. Hospedales, A. Antoniou, P. Micaelli, A. J. Storkey, Meta-learning in neural networks: A survey, CoRR abs/2004.05439. arXiv:2004.05439.
- [29] R. Boney, A. Ilin, Semi-supervised few-shot learning with maml (2018) 4.
- [30] Y. Zhu, M. Saqib, E. Ham, S. Belhareth, R. Hoﬀman, M. D. Wang, Mitigating Patient-to-Patient Variation in EEG Seizure Detection using Meta Transfer Learning, in: IEEE International Conference on Bioinformatics and Bioengineering (BIBE), IEEE, 2020, pp. 548–555.
- [31] T. Jeong, H. Kim, OOD-MAML: Meta-Learning for Few-Shot Out-ofDistribution Detection and Classiﬁcation, in: H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, H. Lin (Eds.), Advances in Neural Information Processing Systems, Vol. 33, Curran Associates, Inc., 2020, pp. 3907–3916.
- [32] P. Zhong, D. Wang, C. Miao, EEG-Based Emotion Recognition Using Regularized Graph Neural Networks, IEEE Transactions on Aﬀective Computing (2020) 1–1.
- [33] G. Singh, L. Samavedham, Unsupervised learning based feature extraction for diﬀerential diagnosis of neurodegenerative diseases: A case study on early-stage diagnosis of Parkinson disease, Journal of Neuroscience Methods 256 (2015) 30–40.
- [34] L. Sun, B. Jin, H. Yang, J. Tong, C. Liu, H. Xiong, Unsupervised EEG feature extraction based on echo state network, Information Sciences 475

(2019) 1–17.

- [35] H. Xu, K. N. Plataniotis, Aﬀective states classiﬁcation using EEG and semisupervised deep learning approaches, in: IEEE International Workshop on Multimedia Signal Processing (MMSP), IEEE, 2016, pp. 1–6.

- [36] M. Langkvist, L. Karlsson, A. Loutﬁ, Sleep Stage Classiﬁcation Using Unsupervised Feature Learning, Adv. Artif. Neu. Sys. 2012 (2012) 5.
- [37] X. Chai, Q. Wang, Y. Zhao, X. Liu, O. Bai, Y. Li, Unsupervised domain adaptation techniques based on auto-encoder for non-stationary EEGbased emotion recognition, Computers in Biology and Medicine 79 (2016) 205–214.
- [38] S.-H. Hsu, Y. Lin, J. Onton, T.-P. Jung, S. Makeig, Unsupervised learning of brain state dynamics during emotion imagination using high-density EEG, NeuroImage 249 (2022) 118873.
- [39] Y. Dan, J. Tao, J. Fu, D. Zhou, Possibilistic clustering-promoting semisupervised learning for EEG-based emotion recognition, Frontiers in Neuroscience 15.
- [40] Y. Wen, K. Zhang, Z. Li, Y. Qiao, (Center loss) A Discriminative Feature Learning Approach for Deep Face Recognition, in: Computer Vision C ECCV 2016, Vol. 9911, 2016, pp. 499–515.
- [41] T. Song, W. Zheng, P. Song, Z. Cui, EEG emotion recognition using dynamical graph convolutional neural networks, IEEE Transactions on Aﬀective Computing 11 (3) (2018) 532–541.
- [42] O. Tsinalis, P. M. Matthews, Y. Guo, Automatic sleep stage scoring using time-frequency analysis and stacked sparse autoencoders, Annals of biomedical engineering 44 (5) (2016) 1587–1597.
- [43] Y. Zhang, G. Zhou, Q. Zhao, J. Jin, X. Wang, A. Cichocki, Spatialtemporal discriminant analysis for erp-based brain-computer interface, IEEE Transactions on Neural Systems and Rehabilitation Engineering 21 (2) (2013) 233–243.
- [44] H. Li, Y.-M. Jin, W.-L. Zheng, B.-L. Lu, Cross-subject emotion recognition using deep adaptation networks, in: International conference on neural information processing, Springer, 2018, pp. 403–413.

- [45] G.-R. Liu, Y.-L. Lo, J. Malik, Y.-C. Sheu, H.-T. Wu, Diﬀuse to fuse EEG spectra–intrinsic geometry of sleep dynamics for classiﬁcation, Biomedical Signal Processing and Control 55 (2020) 101576.
- [46] M. K. Alom, S. M. R. Islam, Classiﬁcation for the p300-based brain computer interface (BCI), in: International Conference on Advanced Information and Communication Technology (ICAICT), IEEE, 2020, pp. 387–391.
- [47] Y. Li, L. Wang, W. Zheng, Y. Zong, L. Qi, Z. Cui, T. Zhang, T. Song, A novel bi-hemispheric discrepancy model for EEG emotion recognition, IEEE Transactions on Cognitive and Developmental Systems 13 (2) (2020) 354–367.
- [48] A. Rakotomamonjy, V. Guigue, BCI Competition III: dataset II-ensemble of SVMs for BCI P300 speller, IEEE Trans. Biomed. Eng. 55 (3) (2008) 1147–1154.
- [49] P. Zhong, D. Wang, C. Miao, EEG-based emotion recognition using regularized graph neural networks, IEEE Transactions on Aﬀective Computing.
- [50] H. Phan, F. Andreotti, N. Cooray, O. Y. Ch´en, M. De Vos, Joint classiﬁcation and prediction cnn framework for automatic sleep stage classiﬁcation, IEEE Transactions on Biomedical Engineering 66 (5) (2018) 1285–1296.
- [51] H. Cecotti, A. Graser, Convolutional neural networks for p300 detection with application to brain-computer interfaces, IEEE transactions on pattern analysis and machine intelligence 33 (3) (2010) 433–445.
- [52] J. Li, S. Li, J. Pan, F. Wang, Cross-subject EEG emotion recognition with self-organized graph neural network, Frontiers in Neuroscience (2021) 689.
- [53] A. Supratak, H. Dong, C. Wu, Y. Guo, Deepsleepnet: A model for automatic sleep stage scoring based on raw single-channel EEG, IEEE Transactions on Neural Systems and Rehabilitation Engineering 25 (11) (2017) 1998–2008.

##### [54] T. Domhan, J. T. Springenberg, F. Hutter, Speeding up automatic hyperparameter optimization of deep neural networks by extrapolation of learning curves, in: IJCAI, 2015, pp. 3460–3468.

