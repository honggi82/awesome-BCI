## Federated Transfer Learning for EEG Signal Classiﬁcation

Ce Ju1, Dashan Gao2,3, Ravikiran Mane4, Ben Tan1, Yang liu1 and Cuntai Guan4

# arXiv:2004.12321v5[cs.LG]25Jan2021

Existing federated learning mainly focuses on the homogeneous dataset, where the different parties share the same feature space. For EEG signal collection, even the same equipment manufacturer may develop EEG signal acquisition equipment with varying electrode numbers, position and sampling rate let alone different equipment vendors. Such device diversity further exacerbates the scarcity of training data and yields numerous distributed heterogeneous datasets in EEG classiﬁcation. Heterogeneous domain adaptation by linking different feature spaces based on labels has been studied [6]. However, existing solutions assume a presence of multiple source domains with abundant labeled instances and one target domain with limited labeled instances as well as unlabeled instances. When applied to our problem setting, existing heterogeneous domain adaptation approaches will face accuracy drop. The reason for the accuracy drop is that in our setting, there are numerous clients each with limited labeled data, and none of them can be a source domain in a source-target domain pair.

Abstract—The success of deep learning (DL) methods in the Brain-Computer Interfaces (BCI) ﬁeld for classiﬁcation of electroencephalographic (EEG) recordings has been restricted by the lack of large datasets. Privacy concerns associated with EEG signals limit the possibility of constructing a large EEGBCI dataset by the conglomeration of multiple small ones for jointly training machine learning models. Hence, in this paper, we propose a novel privacy-preserving DL architecture named federated transfer learning (FTL) for EEG classiﬁcation that is based on the federated learning framework. Working with the single-trial covariance matrix, the proposed architecture extracts common discriminative information from multi-subject EEG data with the help of domain adaptation techniques. We evaluate the performance of the proposed architecture on the PhysioNet dataset for 2-class motor imagery classiﬁcation. While avoiding the actual data sharing, our FTL approach achieves 2% higher classiﬁcation accuracy in a subject-adaptive analysis. Also, in the absence of multi-subject data, our architecture provides 6% better accuracy compared to other stateof-the-art DL architectures.

I. INTRODUCTION

In this paper, we propose a novel neural network-based covariance method in BCI for the subject-speciﬁc analysis, and adapt it to the transfer learning setting for crosssubject learning in a subject-adaptive BCI analysis based on a federated learning framework. We call our method as Federated Transfer Learning (FTL). Speciﬁcally, the architecture of our model is of deep neural networks, whose inputs are spatial covariance matrices of EEG signals, with the domain adaptation technique for adaptive analysis.

Brain-Computer Interface systems aim to identify users’ intentions from brain states. BCI has a prominent potential in the medical domain but its use has been limited by moderate decoding accuracies. In the era of deep learning, the success of BCI models for classiﬁcation of electroencephalographic (EEG) recordings have been restricted by the lack of large datasets. Due to the high data collection costs, EEG-BCI data is present in the form of multiple small datasets that are scattered around the globe. Moreover, due to privacy concerns, it is difﬁcult to create a large enough dataset by combining multiple small datasets. As EEG signals reﬂect brain activities in numerous aspects, the potential abuse of EEG data may lead to severe privacy violations and hence acts like General Data Protection Regulation (GDPR) [1] prohibit organizations from exchanging data without explicit user approval. Therefore, it is signiﬁcant to conduct a joint EEG signal analysis while protecting user privacy. Hence, to solve this problem, we propose to use federated learning framework in healthcare [2], [3], [4], [5]. Federated learning is an emerging and powerful technique which enables joint training of machine learning models using data from multiple sources without the need of actual data sharing between sources.

In summary, following are the the major contributions of this paper: we propose a novel DL architecture based on the EEG spatial covariance matrix. Our approach is adapted to multi-devices for transfer learning setting based on the federated learning framework to protect data privacy. We perform subject-speciﬁc and subject-adaptive analysis on PhysioNet EEG Motor Movement/Imagery Dataset. We show that FTL can match the classiﬁcation accuracy of state-ofthe-art methods while avoiding the sharing of EEG data

II. RELATED WORK

1) Covariance Methods in BCI: When we process and classify EEG signals, one cutting edge technology is to directly estimate and manipulate covariance matrices of EEG signal for source extraction instead of subspaces methods, such as principal component analysis (PCA), independent component analysis (ICA) and common spatial pattern (CSP) [7], [8]. The covariance methods, also called Riemannian approach, encapsulates signal energy-based information of EEG signals. Covariance methods in BCI are promising methods to enable the direct manipulation of covariance matrices, and they are

1WeBank Co., Ltd., {ceju, btan, yangliu}@webank.com 2Hong Kong University of Science and Technology,

dgaoaa@connect.ust.hk 3Southern University of Science and Technology. 4Nanyang Technological University, ravikian001@e.ntu.edu.sg,

CTGuan@ntu.edu.sg

*This work is supported by the Joint NTU-WeBank Research Centre.

superior to the classical EEG signal processing approaches based on feature extraction [9], [10], [11]. For example, Minimum Distance to the Mean (MDM) approach is a classiﬁer based on the geodesic distances on SPD manifolds which consists of covariance matrices [10]. Barachant et al. and Yger et al. purpose Log-Euclidean kernel and Stein kernel method to classify SPD matrices based on the Riemannian distance respectively [12], [13].

2) Deep Learning Methods in BCI: Symmetric PositiveDeﬁnite (SPD) matrix is one of the popular research objects encountered in a great variety of areas, such as medical imaging [14] and visual recognition [15]. The paradigm of deep neural networks on SPD matrices has been proposed to interpolate, manipulate and classify SPD matrices in bunch of application areas [16], [17], [18], [19]. For example, the Riemannian network architecture designed by Huang and Goal that includes BiMap layer, ReEig layer and LogEig layer on SPD matrices, has outperformed the existing state-of-the-art methods in three typical visual classiﬁcation tasks [16]. Furthermore, deep learning methods, especially the convolutional neural network (CNN) architectures, have been explored to boost classiﬁcation performance [20], [21], [22], [23].

III. METHODOLOGY

The raw data is represented in the spatial covariance matrix as the input for our FTL architecture. Speciﬁcally, let X ∈ RE·D be a short-time segment trial of EEG signal, where E is the number of electrodes and D is the epoch durations discretized as a number of samples. The spatial covariance matrix S of segment trial X is an E × E SPD matrix given by S := D1−1 · X · XT.

Our proposed architecture consists of following 4 layers: manifold reduction layer (III-B), common embedded space (III-C), tangent projection layer (III-D) and federated layer (III-E). The purpose of each layer is as follows:

- • Manifold reduction layer (M): Spatial covariance matrices are always assumed to be on the high-dimensional SPD manifolds. This layer is the linear map from the high-dimensional SPD manifold to the low-dimensional one with undetermined weights for learning.
- • Common embedded space (C): The common space is the low-dimensional SPD manifold whose elements are reduced from each high-dimensional SPD manifolds, which is designed only for the transfer learning setting.
- • Tangent projection layer (T): This layer is to project the matrices on SPD manifolds to its tangent space, which is a local linear approximation of the curved space.
- • Federated layer (F): Deep neural networks are implemented in this layer. For the transfer learning setting, parameters of neural networks are updated by the federated aggregation.

Based on the above layers, we design transfer version and non-transfer version FTL architectures for subject-adaptive analysis and subject-speciﬁc analysis respectively. For the transfer version, our FTL architecture consists of M, C, T and F. For the non-transfer version, our FTL architecture only

consists of M and T. The outputs of either architecture are predicted labels. The architecture of the transfer version FTL refers to Figure 1.

- A. Notation

EEG device captures signals from m subjects, and we always assume that the EEG signals have been band-pass ﬁltered. For the i th subject, his/her ﬁltered EEG signal is separated as a sequence of trials {Xj}N the number of trials. The basic assumption of Riemannian approach for signal processing is that spatial covariance matrices {Sj}N embedded SPD submanifold Mi → RE

- i
- j=1, where Ni is

- i
- j=1 of trials {Xj}N

- i
- j=1 are distributed on an

i·Di, where " →" represents an embedding map in differential geometry [24],

- [25].

B. Manifold Reduction Layer For spatial covariance matrices {S1,··· ,SN

i} of the i th subject on Mi → RE

i·Di, we build its own reduction Ri to map SPD submanifold Mi to the common SPD manifold N → Rd, where d is the embedding dimension of N. Figure 1 illustrates the manifold reduction layer. We approximate these reductions Ri with neural networks approach. Suppose Wi ∈ Rd·E

i is the weight matrix of neural network, the manifold reduction layer is constructed as a bilinear mapping,

Ri(Sj) := Wi · Sj · WiT. C. Common Embedded Space

Upon the establishment of manifold reductions, we require that spatial covariance matrices from different subjects should fall closely onto the common embedded space N. One way to measure the distances between two probability distributions of reduced spatial covariance matrices on common embedded space N is maximum mean discrepancy (MMD)

- [26]. Suppose each projected matrices Ri {S1,··· ,SN

- D. Tangent Projection Layer For any reference matrix P on common embedded SPD

i} ∼ Qi, where Qi is the probability distribution over common manifold N. For a feature map ψ : N −→ H, where H is a reproducing kernel Hilbert space (RKHS). Hence, the MMD distance between two probability distributions is as follows,

MMDψ(Qi,Qj) :=||ER

i(S)∼Qiψ(Ri(S)) − ER

j(S)∼Qjψ(Rj(S))||H, where random variable S ∈ {S1,··· ,SN

i} (i = 1,··· ,m). Notice that the small MMD yields closed reduced matrices on N.

manifold N, we consider the associated tangent space TPN. Let V1 and V2 be two tangent vectors on tangent space TPN with the inner product deﬁned as V1,V2 P := tr V1 · P−1·V2·P−1 . Logarithmic map LOG on manifolds locally project the spatial covariance matrix P˜ onto the tangent space of reference matrix P by

V : = LOGP(P˜)

- 1

- 2

- 1

- 2

· log P−

= P

- 1

- 2

· P˜ · P−

- 1

- 2 ,

· P

Mj → RE

j·Dj

Mi → RE

Mk → RE

i·Di

k·Dk

Sj

Sk

Si

1

D−1 · Xi · XiT

Rj

Rk

Ri

Xi

F : wk+1 ← mi=1 wti/m

Y¯

p

TpN ∼= Rd N → Rd

- Fig. 1: Architecture of the transfer version FTL: Spatial covariance matrix Si ∈ Mi is derived from short-time segment trial Xi ∈ REi×Di. In manifold reduction layer (III-B), neural networks Ri, Rj and Rk reduce SPD manifolds Mi, Mj and Mk, respectively, on common space N, also an SPD manifold (III-C). We then project the signals from N to tangent space TpN in tangent projection layer (III-D). Finally, we have neural networks in federated layer (III-E) for the classiﬁcation, which yields predicted labels Y¯ ∈ {1, · · · , K}. The parameters of neural networks in this layer is updated by federated aggregation F in each round.

where log is the logarithm of SPD matrix P = U · diag σ1,··· ,σE · UT, such that

### log(P) := U · diag log(σ1),··· ,log(σE) · UT.

Speciﬁcally, the reference matrix P = IE yields a compact expression of tangent vector V = log(P˜). Hence, we let the tangent projection layer PN on common space N be PN(X) := log(X), where X is the set of all reduced spatial covariance matrices from different subjects on N.

E. Federated layer

The tangent space of common manifold N is locally homeomorphic in the Euclidean space of dimension d. Hence, we establish typical neural networks as the classiﬁer from tangent space. The architectures of each subject’s classiﬁer in federated layer are assumed to be the same including fully connected layer, ﬂatten layer and activation function.

At training round t, we adopt federated averaging method[27] to train the model weights wt in federated layer. Federated averaging is conducted over clients of each subject for feature map aggregation and over all the clients for classiﬁer aggregation. Speciﬁcally, the techniques of federated learning follows a server-client setting. A server acts as model aggregator. In each round, the server collects updated local models from each client for model aggregation. After model aggregation, the server sends the updated global model to each client as follows,

m

1 m ·

wti

F : wt+1 ←

i=1

When a client receives the model sent by server, it updates the model with its local data distributed on the reduced common manifold Ri(Mi) ⊂ N → Rd. The training process continues until the model converges.

F. Architecture and Loss

There are two classes of loss in our approach including the classiﬁcation loss and the domain loss as follows,

- • Classiﬁcation Loss: the cross entropy loss between

predicted label and ground truth, write as LC(Y¯,Y ), where Y¯,Y ∈ {1,··· ,K} is predicted label and ground truth respectively.

- • Domain Loss: MMDψ(QYi ,QYj ) is MMD distance with pre-set feature map ψ between any two of probability

### distributions QYi and QYj , for 1 ≤ i < j ≤ m and Y ∈ {1,··· ,K}.

For the non-transfer version, the architecture includes repeated manifold reduction layer, tangent projection layer and typical neural networks with only the classiﬁcation loss, i.e.

m

LC(Y¯i,Y ),

L :=

i=1

where subscript i represents each subject.

For the transfer version, the architecture includes two classes of losses as follows,

m

K

LC(Y¯i,Y ) +

λYi,j · MMDψ(QYi ,QYj ),

L :=

1≤i<j≤m

i=1

Y =1

where λYi,j are pre-set weights for each domain loss term.

IV. EXPERIMENTS A. Experimental Setup

The EEG data used in our experiments is from PhysioNet EEG Motor Imagery(MI) Dataset [28].

1) MI Dataset Description: The PhysioNet EEG dataset is recorded from 109 subjects. In our experiments, we consider the 2-class MI data, i.e. imagined left and right hand movements. The EEG data is recorded using 64 electrodes at 160Hz sampling frequency.

[Figure 1]

- Fig. 2: Average accuracy of classiﬁers on 109 subject in subject-speciﬁc analysis: horizontal axis represents the subject number from 1 to 109, and vertical axis represents the average accuracy.

- 2) Evaluated Algorithms: We evaluated FTL against the

following subspaces methods, covariance methods and DL methods:

- • CSP + linear discriminant analysis (LDA)/support vector machines (SVM): CSP spatial ﬁltering algorithm with an LDA/SVM classiﬁer [7], [11].
- • FBCSP: Best-performing CSP method for motor imagery classiﬁcation [29], [30].
- • MDM: Classiﬁcation algorithm based on computing the geodesic distances on SPD manifolds [11].
- • Tangent Space Mapping (TSM): Classiﬁcation algorithm on the tangent space of SPD manifolds [11].
- • Riemannian-based Kernel Method (R-Kernal): Kernel method with the speciﬁc kernel derived from Riemannian geometry of SPD matrices [12].
- • EEGNet: A compact CNN architecture for EEG-based BCIs [23].
- • DeepConvNet: A new discriminative spectral–spatial input to represent a diversity of brain signal patterns across the subjects and sessions [31].

- 3) Architecture of FTL in Experiments: All the experiments

are conducted on a machine with 2.6 GHz 6-Core Intel Core i7 with Memory 16 GB 2400 MHz DDR4.

- • Subject-speciﬁc Analysis: The architecture of FTL in this analysis includes three-manifold reduction layers (i.e.

W1 ∈ R32×4, W2 ∈ R4×4 and W3 ∈ R4×4), tangent projection layer and federated layer without federated aggregation. The learning rate is initialized to 0.1 with a decay after 50 epochs. We stop the training procedure when the training loss is less than 0.1.

- • Subject-adaptive Analysis: The architecture of FTL in this analysis includes two clients, i.e. source domain (good subjects) and target domain (bad subjects). For the source domain (27 good subjects), we design threemanifold reduction layers (i.e. W1 ∈ R32×16, W2 ∈ R16×8 and W3 ∈ R8×4). For the target domain (1 bad subject), we design a small two-manifold reduction

layers (i.e. W1 ∈ R32×8 and W2 ∈ R8×4). According to our construction, common space N is a SPD manifold with dimension 4 × 4. The kernel in RKHS of N is Gaussian kernel with a mean of 0 and a population standard deviation 2. The federated layer is a simple

|Subspace Methods|CSP+LDA|CSP+SVM<br><br>|FBCSP|
|---|---|---|---|
|Avg Acc.|0.654<br><br>|0.653|0.631|

|Covariance Methods<br><br>|MDM|TSM|R-Kernel|
|---|---|---|---|
|Avg Acc.|0.627<br><br>|0.663<br><br>|0.644|

|DL Methods|EEGNet<br><br>|DeepConvNet<br><br>|FTL|
|---|---|---|---|
|Avg Acc.<br><br>|0.567|0.574|0.633|

- TABLE I: Cross-validation average accuracy (Avg Acc.) of 9 classiﬁers on 109 subjects. We have 3 subspaces methods, 3 covariance methods and 3 DL methods in the table.

|Alg. /Setting<br><br>|Bad Subject<br><br>|Good Subject|Transfer Learning|
|---|---|---|---|
|CSP+LDA<br><br>|0.489|0.869<br><br>|0.528|
|CSP+SVM<br><br>|0.488|0.876<br><br>|0.527|
|FBCSP<br><br>|0.532<br><br>|0.805|0.525|

|MDM<br><br>|0.478<br><br>|0.842|0.522|
|---|---|---|---|
|TSM<br><br>|0.519|0.868<br><br>|0.547|
|R-Kernel|0.514<br><br>|0.840|0.537|

|EEGNet|0.487<br><br>|0.719|0.513|
|---|---|---|---|
|DeepConvNet|0.505|0.721<br><br>|0.520|
|FTL|0.513<br><br>|0.837|0.549|

- TABLE II: Cross-validation accuracy of 9 classiﬁers on three experimental settings. The results in ﬁrst and second columns are average accuracies of 27 good subjects and 28 bad subjects derived from the subject-speciﬁc analysis respectively.

fully-connected structure W ∈ R16×2 with federated aggregation. In the loss, the pre-set weights are as follows: λ11,2 = λ21,2 = 0.1. Additionally, the learning rates are initialized to 0.1 with a 2% decay after 50 epochs. We stop the training procedure when the training loss is less than 1.5.

B. Experimental Results and Analysis

Our experimental section includes a subject-speciﬁc analysis and a subject-adaptive analysis. All experiments are evaluated in 5-fold cross-validation settings with 4 folds being used for training and 1 fold for testing. Trials were randomly assigned to different folds and this allocation was maintained constant across the classiﬁcation methods. The result is plotted in Figure 2, and it demonstrates that no competing classiﬁer outperforms others. The speciﬁc experimental setting is as follows,

1) Subject-speciﬁc Analysis for 2-class MI Classiﬁcation: Table I demonstrates that the average performance for each classiﬁers of 109 subjects is around 0.60. It is worthy to

mention that subspace methods and covariance methods usually perform better than DL methods on a small sample size dataset. However, our approach FTL takes advantage of the covariance methods, and outperforms other two state-ofthe-art DL methods in this experiment.

We pick good and bad subjects from 109 subjects for the following subject adaptive analysis, where the word good and bad are in the following sense that the classiﬁcation accuracy of CSP+LDA classiﬁers is in Top 25% and Bottom 25% of 109 subjects respectively. According to this construction, we have 27 good subjects and 28 bad subjects.

2) Subject-adaptive Analysis for 2-class MI Classiﬁcation: In subject-adaptive analysis experiment, we have three experimental settings, i.e. bad subject setting, good subject setting and transfer learning setting. Bad and good subject settings refers to the average of results in subject-speciﬁc analysis for bad and good subjects respectively. Transfer learning setting refers to the subject-adaptive analysis in BCI that the training data for every bad subject is good subject data combined with

- 4 folds of the bad subjects data, and the testing data is the rest 1 fold. The results of the transfer learning setting, listed in the third column of Table II, demonstrates that modeling with signals from good subjects yields better accuracy than modeling only with the bad subject (the results in the ﬁrst column). Furthermore, FTL is an effective classiﬁer, which is equipped with the techniques of domain adaptation, for transfer learning setting.

C. Discussion

Lack of adequate training data is a major challenge in the adaption of DL methods for EEG-BCI classiﬁcation. In this paper, to mitigate this issue, we proposed a federated transfer learning based deep learning architectures for subjectadaptive EEG-MI classiﬁcation. Furthermore, following the successful Riemannian approach [8], [9], [10], [11], [12], our architecture used signal covariance matrix as an input. With this architectures, in a subject-speciﬁc analysis, we achieved 6% better classiﬁcation accuracy compared to the other two state-of-the-art DL architectures. This indicates that the covariance-based representation of EEG can be an effective input for DL architectures, particularly in the absence of adequate training data. Furthermore, in a subject-adaptive analysis, the proposed method achieved the best classiﬁcation accuracy which shows that the use of domain adaptation in the FTL architecture can boost classiﬁcation performance. Lastly, as done in this work, the federated learning framework can be effectively used to enable distributed training of EEG classiﬁers from multiple heterogeneous data conﬁgurations.

V. CONCLUSIONS

In this paper, we investigated the feasibility of the federated learning framework to enable a distributed training of BCI models from multiple datasets with heterogeneous conﬁgurations. The experimental results conﬁrm the effectiveness of our approach and demonstrate the prominent potential of extracting knowledge from the heterogeneous BCI data.

VI. AKNOWLEDGEMENT

We would like to thank WeBank FATE developer community, Tianjian Chen (WeBank Co., Ltd.), Yuan Jin (Shenzhen Gradient Technology Co., Ltd.) and Ruihui Zhao (Tencent Jarvis Lab) for their useful suggestions and contributions.

REFERENCES

- [1] General Data Protection Regulation. Regulation (eu) 2016/679 of the european parliament and of the council of 27 april 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing directive 95/46. Ofﬁcial Journal of the European Union (OJ), 59(1-88):294, 2016.
- [2] H Brendan McMahan, Eider Moore, Daniel Ramage, Seth Hampson, et al. Communication-efﬁcient learning of deep networks from decentralized data. arXiv preprint arXiv:1602.05629, 2016.
- [3] Qiang Yang, Yang Liu, Yong Cheng, Yan Kang, Tianjian Chen, and Han Yu. Federated learning. Synthesis Lectures on Artiﬁcial Intelligence and Machine Learning, 13(3):1–207, 2019.
- [4] Dashan Gao, Yang Liu, Anbu Huang, Ce Ju, Han Yu, and Qiang Yang. Privacy-preserving heterogeneous federated transfer learning. In 2019 IEEE International Conference on Big Data (Big Data), pages 2552–2559. IEEE, 2019.
- [5] Ce Ju, Ruihui Zhao, Jichao Sun, Xiguang Wei, Bo Zhao, Yang Liu, Hongshan Li, Tianjian Chen, Xinwei Zhang, Dashan Gao, et al. Privacypreserving technology to help millions of people: Federated prediction model for stroke prevention. Workshop on Federated Learning for Data Privacy and Conﬁdentiality in Conjunction with IJCAI 2020 (FL-IJCAI’20), 2020.
- [6] Chang Wang and Sridhar Mahadevan. Heterogeneous domain adaptation using manifold alignment. In Twenty-Second International Joint Conference on Artiﬁcial Intelligence, 2011.
- [7] Fabien Lotte, Marco Congedo, Anatole Lécuyer, Fabrice Lamarche, and Bruno Arnaldi. A review of classiﬁcation algorithms for eeg-based brain–computer interfaces. Journal of neural engineering, 4(2):R1, 2007.
- [8] Florian Yger, Maxime Berar, and Fabien Lotte. Riemannian approaches in brain-computer interfaces: a review. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 25(10):1753–1762, 2016.
- [9] Marco Congedo, Alexandre Barachant, and Anton Andreev. A new generation of brain-computer interface based on riemannian geometry. arXiv preprint arXiv:1310.8115, 2013.
- [10] Florian Yger, Fabien Lotte, and Masashi Sugiyama. Averaging covariance matrices for eeg signal classiﬁcation based on the csp: An empirical study. In 2015 23rd European Signal Processing Conference (EUSIPCO), pages 2721–2725. IEEE, 2015.
- [11] Alexandre Barachant, Stéphane Bonnet, Marco Congedo, and Christian Jutten. Multiclass brain–computer interface classiﬁcation by riemannian geometry. IEEE Transactions on Biomedical Engineering, 59(4):920– 928, 2011.
- [12] Alexandre Barachant, Stéphane Bonnet, Marco Congedo, and Christian Jutten. Classiﬁcation of covariance matrices using a riemannian-based kernel for bci applications. Neurocomputing, 112:172–178, 2013.
- [13] Bernhard Schölkopf, Patrice Simard, Alex J Smola, and Vladimir Vapnik. Prior knowledge in support vector kernels. In Advances in neural information processing systems, pages 640–646, 1998.
- [14] Sadeep Jayasumana, Richard Hartley, Mathieu Salzmann, Hongdong Li, and Mehrtash Harandi. Kernel methods on the riemannian manifold of symmetric positive deﬁnite matrices. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 73–80, 2013.
- [15] Zhiwu Huang, Ruiping Wang, Shiguang Shan, and Xilin Chen. Learning euclidean-to-riemannian metric for point-to-set classiﬁcation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 1677–1684, 2014.
- [16] Zhiwu Huang and Luc Van Gool. A riemannian network for spd matrix learning. In Thirty-First AAAI Conference on Artiﬁcial Intelligence, 2017.
- [17] Zhen Dong, Su Jia, Chi Zhang, Mingtao Pei, and Yuwei Wu. Deep manifold learning of symmetric positive deﬁnite matrices with application to face recognition. In Thirty-First AAAI Conference on Artiﬁcial Intelligence, 2017.

- [18] Zhiwu Huang, Jiqing Wu, and Luc Van Gool. Building deep networks on grassmann manifolds. In Thirty-Second AAAI Conference on Artiﬁcial Intelligence, 2018.
- [19] Zhiwu Huang, Chengde Wan, Thomas Probst, and Luc Van Gool. Deep learning on lie groups for skeleton-based action recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 6099–6108, 2017.
- [20] Boris Reuderink, Jason Farquhar, Mannes Poel, and Anton Nijholt. A subject-independent brain-computer interface based on smoothed, second-order baselining. In 2011 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, pages 4600–4604. IEEE, 2011.
- [21] R Schirrmeister, Lukas Gemein, Katharina Eggensperger, Frank Hutter, and Tonio Ball. Deep learning with convolutional neural networks for decoding and visualization of eeg pathology. In 2017 IEEE Signal Processing in Medicine and Biology Symposium (SPMB), pages 1–7. IEEE, 2017.
- [22] Siavash Sakhavi, Cuntai Guan, and Shuicheng Yan. Learning temporal information for brain-computer interface using convolutional neural networks. IEEE transactions on neural networks and learning systems, 29(11):5619–5629, 2018.
- [23] Vernon J Lawhern, Amelia J Solon, Nicholas R Waytowich, Stephen M Gordon, Chou P Hung, and Brent J Lance. Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces. Journal of neural engineering, 15(5):056013, 2018.
- [24] Peter Petersen, S Axler, and KA Ribet. Riemannian geometry, volume

171. Springer, 2006.

- [25] Ce Ju. Geometric foundations of data reduction. arXiv preprint arXiv:2008.06853, 2020.
- [26] Arthur Gretton, Karsten Borgwardt, Malte Rasch, Bernhard Schölkopf, and Alex J Smola. A kernel method for the two-sample-problem. In Advances in neural information processing systems, pages 513–520, 2007.
- [27] H. Brendan McMahan, Eider Moore, Daniel Ramage, and Blaise Agüera y Arcas. Federated learning of deep networks using model averaging. CoRR, abs/1602.05629, 2016.
- [28] Gerwin Schalk, Dennis J McFarland, Thilo Hinterberger, Niels Birbaumer, and Jonathan R Wolpaw. Bci2000: a general-purpose braincomputer interface (bci) system. IEEE Transactions on biomedical engineering, 51(6):1034–1043, 2004.
- [29] Kai Keng Ang, Zheng Yang Chin, Haihong Zhang, and Cuntai Guan. Filter bank common spatial pattern (fbcsp) in brain-computer interface. In 2008 IEEE International Joint Conference on Neural Networks (IEEE World Congress on Computational Intelligence), pages 2390–

2397. IEEE, 2008.

- [30] Zheng Yang Chin, Kai Keng Ang, Chuanchu Wang, Cuntai Guan, and Haihong Zhang. Multi-class ﬁlter bank common spatial pattern for fourclass motor imagery bci. In 2009 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, pages 571–574. IEEE, 2009.
- [31] O-Yeon Kwon, Min-Ho Lee, Cuntai Guan, and Seong-Whan Lee. Subject-independent brain-computer interfaces based on deep convolutional neural networks. IEEE transactions on neural networks and learning systems, 2019.

