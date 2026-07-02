## GCNs-Net: A Graph Convolutional Neural Network Approach for Decoding Time-resolved EEG Motor Imagery Signals

Yimin Hou *, Shuyue Jia *, Student Member, IEEE, Xiangmin Lun, Ziqian Hao, Yan Shi, Yang Li, Senior Member, IEEE, Rui Zeng, and Jinglei Lv

### arXiv:2006.08924v4[eess.SP]26Aug2022

Abstract—Towards developing effective and efﬁcient braincomputer interface (BCI) systems, precise decoding of brain activity measured by electroencephalogram (EEG), is highly demanded. Traditional works classify EEG signals without considering the topological relationship among electrodes. However, neuroscience research has increasingly emphasized network patterns of brain dynamics. Thus, the Euclidean structure of electrodes might not adequately reﬂect the interaction between signals. To ﬁll the gap, a novel deep learning framework based on the graph convolutional neural networks (GCNs) is presented to enhance the decoding performance of raw EEG signals during different types of motor imagery (MI) tasks while cooperating with the functional topological relationship of electrodes. Based on the absolute Pearson’s matrix of overall signals, the graph Laplacian of EEG electrodes is built up. The GCNs-Net constructed by graph convolutional layers learns the generalized features. The followed pooling layers reduce dimensionality, and the fully-connected softmax layer derives the ﬁnal prediction. The introduced approach has been shown to converge for both personalized and group-wise predictions. It has achieved the highest averaged accuracy, 93.06% and 88.57% (PhysioNet Dataset), 96.24% and 80.89% (High Gamma Dataset), at the subject and group level, respectively, compared with existing studies, which suggests adaptability and robustness to individual variability. Moreover, the performance is stably reproducible among repetitive experiments for cross-validation. The excellent performance of our method has shown that it is an important step towards better BCI approaches. To conclude, the GCNs-Net ﬁlters EEG signals based on the functional topological relationship, which manages to decode relevant features for brain motor imagery. A deep learning library for EEG tasks classiﬁcation including the code for this study is open source at https://github.com/SuperBruceJia/EEG-DL for scientiﬁc research.

Index Terms—Electroencephalography, motor imagery, deep learning, graph convolutional neural networks, brain-computer interface.

* indicates co-ﬁrst authorship. Yimin Hou, Xiangmin Lun, and Yan Shi are with the School of Automation

Engineering, Northeast Electric Power University, Jilin 132011, China (e-mail: ymh7821@163.com; xm lun77@163.com; shiyan@neepu.edu.cn).

This work was done while Shuyue Jia was with the School of Automation Engineering, Northeast Electric Power University, Jilin 132011, China. He is now with the Department of Computer Science, City University of Hong Kong, Hong Kong, China (e-mail: shuyuej@ieee.org).

Ziqian Hao is with the Jinan Vocational College of Nursing, Jinan 250102, China (e-mail: ziqhao@163.com).

Yang Li is with the School of Electrical Engineering, Northeast Electric Power University, Jilin 132011, China (e-mail: liyang@neepu.edu.cn).

Rui Zeng and Jinglei Lv are with School of Biomedical Engineering & Brain and Mind Center, University of Sydney, Sydney 2006, NSW, Australia (e-mail: rui.zeng@sydney.edu.au; jinglei.lv@sydney.edu.au).

I. INTRODUCTION

# R

ECENTLY, the brain-computer interface (BCI) has become one of the hottest research topics for broad appli-

cations in the ﬁeld of therapeutic and medical engineering [1]. It refers to the establishment of an innovative technology that exchanges information directly between the brain and the surroundings, which does not rely on traditional methods such as human muscle tissue or peripheral nerves. BCI systems decode brain activity patterns to manipulate assistant devices, such as wheelchairs and artiﬁcial limbs [2]. Electroencephalogram (EEG) is extensively applied because of its high temporal resolution, noninvasiveness, and portability. The principle of EEG is to record spontaneous, event-related, and stimulusevoked electrical signals of the brain on time scales, which reveals variations for different brain activities [3]. EEG decodes discriminable brain patterns while carrying out different types of actual movement or imagery [4], [5]. Motor imagery (MI) based EEG mentally simulates multiple motor motions, such as imagining hand or foot movements. Controlling machines via only the MI without physical movements of the body is one of the elemental jobs in BCI [6]. To realize such BCI systems, accurate classiﬁcation of MI brain activity is of great essence. Although previous studies have shown promising performances, there is still space to improve the classiﬁcation accuracy towards building effective and efﬁcient BCI applications. For instance, the adaptability and robustness to individual variability remain among the challenges of setting up an EEG MI-based wheelchair. Traditional approaches do not consider the topological relationship of electrodes while decoding EEG signals. However, a growing number of neuroscience research has emphasized brain network dynamics [7]–[9]. Thus, the interaction between signals might not be adequately reﬂected and represented via the Euclidean structure of EEG electrodes. To address the concern, the Graph Convolutional Neural Networks (GCNs) are introduced to decode EEG signals, promoting the classiﬁcation performance by cooperating with the functional topological relationship of EEG electrodes and implementing the Convolutional Neural Networks (CNNs) on graphs.

II. LITERATURE SURVEY

Traditional works manually designed features from EEG signals, e.g., via the analytic intrinsic mode functions or

wavelet transform, and then employed machine learningbased approaches to classify features [10]–[14]. Recently, deep learning (DL) has achieved superhuman performances across multiple domains [15]–[17]. The DL-based methods learned the underlying features from signals, which alleviated the need for hands-on feature engineering. The CNNs have been broadly employed to classify the Euclidean-structured signals on account of their ability to learn informative features via the local receptive ﬁelds. The CNNs-based approaches [18]– [29] were implemented to address the challenge of EEG task classiﬁcation. In [20], Hou et al. introduced an innovative approach by combining the Scout EEG Source Imaging (ESI) and CNNs to decode EEG tasks, which achieved competitive results, 94.5% maximum accuracy for 10 subjects, and 92.5% for 14 subjects, on the PhysioNet Dataset [30]. Zhang et al. [31] presented a cascade convolutional recurrent neural network, and obtained 98.31% averaged accuracy on the PhysioNet Dataset. Reference [22] applied one-dimensional convolutional ﬁlters to learn the temporal and spatial features, and it reached 80.38%, 69.82%, and 58.58% accuracy on the PhysioNet Dataset with two, three, and four MI tasks. References [21], [24], [26], [27] utilized variants of CNNs to decode EEG signals from the BCI Competition IV-2a Dataset [32], and achieved 73.70%, 75.70%, 79.90%, and 83.00% accuracy, respectively. References [21], [28], [29] obtained 92.50%, 93.70%, and 95.4% accuracy at the subject level on the High Gamma Dataset [33]. Although the performance of the above CNNs-based models was encouraging, there was still space to promote the classiﬁcation accuracy to build a robust and reliable BCI system. The reasons why we applied the GCNs were as follows. The traditional CNNs cannot directly process the non-Euclidean structured data because the discrete convolutions cannot keep translation invariance on the non-Euclidean signals. However, the GCNs can directly extract features from the non-Euclidean data and process the graph-structured signals since the GCNs consider the relationship properties (e.g., correlations) between nodes [34], [35]. Through a novel Graph Convolutional Neural Networks approach (GCNs-Net) on two EEG MI benchmarks, it has achieved dominant performances, 98.72% accuracy on the PhysioNet Dataset, and 96.24% on the High Gamma Dataset, for EEG MI decoding, which were far ahead than the results produced by the CNNs-based approaches. Moreover, more and more neuroscience research has suggested that the topological information promotes the analysis of brain network dynamics [7]–[9]. Although the Euclidean distance was one of the similarity measurements, it might be superior to decode EEG signals from the non-Euclidean perspective by taking into consideration of the functional topological relationship of electrodes (e.g., the correlations and degree properties between electrodes) to enhance the decoding performance of EEG tasks.

Considering the topological relationship of EEG electrodes, the graph in the non-Euclidean space was put forward [34], [36]–[40]. Researchers have explored the CNNs with the graph theory, intending to apply the convolutional operation on graphs. Two strategies were presented to deﬁne convolutions, i.e., either from the spatial domain or the spectral

domain. At ﬁrst, the spatial GCNs were proposed [41]–[44]. However, references [35] and [45] indicated that they faced the challenge of matching the local neighborhoods. On the other hand, the spectral method provided a well-deﬁned localized operator on graphs [46]. Thus, an innovative approach of the GCNs was proposed by implementing the CNNs based on the spectral graph theory. In speciﬁc, Bruna et al. [45] ﬁrst performed the GCNs from the spectral perspective. A few works [36]–[39] have applied the above model to decode EEG tasks in the ﬁeld of EEG-based emotion recognition. In detail, reference [36] combined the GCNs with a broad learning system and put forward the Graph Convolutional Broad Network, which achieved 94.24% accuracy on the SJTU Emotion EEG Dataset [47]. In [37], Wang et al. presented a phase-locking value-based GCNs. The dynamical GCNs were proposed by Song [38], which can dynamically learn the topological relationship of EEG electrodes during training. Reference [39] improved the above method via a broad learning system. Moreover, in [34], Hou et al. introduced a twostage method in which it ﬁrst extracted the spatial-temporal EEG features via an attention-based bidirectional long shortterm memory model, and then employed the graph representation learning to classify deep features. Reference [40] proposed an end-to-end approach, a graph residual network, to classify EEG signals. The highly competitive performance of these approaches [34], [36]–[40] indicated the superiority of applying the graph learning methods.

In this work, a novel structure of the GCNs is introduced to decode EEG MI signals. First of all, based on the absolute Pearson’s matrix (PCC) of overall signals, the graph Laplacian is built up to represent the topological relationship of EEG electrodes. Besides, the GCNs-Net built on the graph convolutional layers learns the generalized features. The followed pooling layers reduce dimensionality. And the fully-connected (FC) softmax layer derives the ﬁnal prediction. Furthermore, the Chebyshev polynomial is applied to approximate the graph convolutional ﬁlters, which signiﬁcantly promotes computational efﬁciency. Last but not least, the GCNs-Net decodes time-resolved EEG MI signals, which paves the road towards effective and efﬁcient BCI applications. The main contributions of this work are summarized as follows.

- 1) A novel structure of the GCNs is introduced to detect four-class MI intentions while cooperating with the functional topological relationship of EEG electrodes.
- 2) The individual and group-wise performance of the GCNsNet on two benchmark datasets of EEG MI outperforms the existing studies, which validates that the method can decode relevant features for brain motor imagination.
- 3) The introduced GCNs-Net framework can be easily transferred and implemented for other MI-related tasks, and potentially for other EEG BCI tasks.

III. MATERIALS AND METHODS A. Overview

The framework of this work is shown in Fig. 1. (i) 64-channel raw EEG signals are acquired as one of the inputs of the GCNs-Net.

(i) EEG Data Acquisition

(ii) Correlations between EEG Electrodes

[Figure 1]

channelSignals

Absolute PCC Matrix

Graph Laplacian

64-

[Figure 2]

PCC Matrix

Adjacency Matrix

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

20 Subjects × 84 Trials × 640 Samples

Graph Weights & Degrees

Real-time 64-channel Raw EEG Signals

(iv) The GCNs-Net

(iii) Graph Representation

[Figure 12]

[Figure 13]

L

Softmax

Flatten

###### Pooling GCN

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

R

N

B

F

4

𝐍 𝟔𝟒× 𝟔𝟒𝐍 ×F6

𝐍 𝟐𝒍×𝟐𝐍𝒍×Fl

𝟐𝒍 𝟏×𝟐𝒍 𝟏𝐍 ×Fl

𝐍

×6

International 10-10 EEG System

N×N

- Fig. 1. The system framework is composed of (i) acquisition of 64-channel raw EEG signals, (ii) correlation analysis for graph weights and degrees by presenting the PCC matrix, absolute PCC matrix, adjacency matrix, and graph Laplacian, (iii) graph representation of the International 10-10 EEG System, and (iv) a novel deep learning framework of the GCNs (the GCNs-Net).

- (ii) The PCC matrix, absolute PCC matrix, adjacency matrix, and graph Laplacian are introduced to represent the correlations between electrodes.
- (iii) The graph representation, another input of the GCNs-Net, is represented by the graph Laplacian.
- (iv) The GCNs-Net is applied to decode EEG MI signals, where N denotes the number of electrodes and l denotes the lth graph pooling layer.

Previous studies apply segments (windows) of time points as samples [34], [48], [49]. However, neuroscience research indicates that the brain is one of the most complicated systems, and its state at every moment is changing. Time-resolved signals can represent the condition of the brain at the instant moment, which reﬂects the network patterns of brain dynamics. Therefore, in this work, every time point is recognized as a sample to map the brain state to the corresponding MI task. Compared with applying the time-window signals as samples, the method is time-resolved, which is superior to pave the road towards developing real-time and efﬁcient EEG MI applications [40].

- B. Dataset Description

In this work, two benchmark datasets are used to evaluate the effectiveness and robustness of our presented method.

The PhysioNet Dataset: The EEG Motor Movement/Imagery Dataset consists of over 1,500 EEG records from 109 subjects [30]. There are 64 electrodes based on the international 10-10 system. Each subject performs 84 trials (3 runs × 7 trials × 4 tasks). 160 Hz sampling rate and 4-second signals, i.e., 640 time points per trail, are utilized considering the duration of the experiments [20]. Four MI tasks are termed as L (image left ﬁst), R (image right ﬁst), B (image both ﬁsts), and F (image both feet), respectively.

In this paper, multiple subjects (S1∼S20, S1∼S50, S1∼S100) from the PhysioNet Dataset and 14 subjects from the High Gamma Dataset are picked up to train and evaluate the GCNsNet [20]. Over all the experiments, 90% of the dataset is chosen as the training set, and the remaining 10% serves as the testing set, following the default subject-dependent scenario [20], [31] for fair performance comparison. And we repeat the above procedure 10 times with different random seeds to validate the stability and reliability of the GCNs-Net and avoid obtaining bias results with pseudo-random. Then, we use the averaged accuracy as the ﬁnal performance of the model. For the group-level analysis, we carefully divide the dataset for each subject to prevent data imbalance and model bias.

The High Gamma Dataset: Collected from 14 subjects, the Public High Gamma Dataset performs four EEG tasks, i.e., left-hand movement, right-hand movement, both feet movement, and rest [33]. The data of 44 electrodes and 0-125 Hz frequency are applied in our experiments, and the dataset is resampled to 250 Hz [24]. Each subject performs approximately 880 trials for training and 160 trials for testing.

- C. Graph Preliminary

1) Graph Representation: An undirected and weighted graph is represented by G = {V,E,A}, in which V denotes a set of nodes with the number |V| = N, E denotes a set of edges connecting nodes, and A ∈ RN×N is a weighted adjacency matrix representing correlations between two nodes.

To present the degree matrix of a graph, the scale of the graph weights is analysed regardless of the polar relevance, i.e., whether the correlations are positive or negative. So the absolute Pearson Correlation Coefﬁcient (PCC) matrix |P| ∈ [0,1] is introduced, which is the absolute of the PCC matrix P, to map the linear correlations between signals. A is represented as A = |P| − I, where I is an identity matrix. The PCC matrix, absolute PCC matrix, adjacency matrix, and graph Laplacian for 20 and 100 subjects are given in Fig. 2, respectively.

Fig. 2(a) and Fig. 2(e) demonstrate that there are no apparent differences on the correlations of various sizes of datasets. The reason for this phenomenon is that all the signals of participants are utilized to compute the PCC matrix. Furthermore, the degree matrix D is obtained, which is a diagonal matrix, and the i-th diagonal element can be computed by: Dii = Nj=1 Aij. Finally, the combinatorial Laplacian L ∈ RN×N is represented as L = D − A. The graph Laplacians for 20 and 100 subjects are presented in Fig. 2(d) and Fig. 2(h), respectively. And the normalized graph Laplacian L = IN − D−1/2AD−1/2 represents the correlations between nodes.

2) Spectral Graph Filtering: As L is a real symmetric positive semideﬁnite matrix, its set of eigenvectors, i.e., the graph Fourier modes, {ul}Nl=0−1 ∈ RN, are complete and orthonormal. And the associated eigenvalues, as known as the graph Fourier frequencies, {λl}Nl=0−1 ∈ R, are ordered and real nonnegative. The Fourier basis U = [u0,...,uN−1] ∈ RN×N decomposes the graph Laplacian, i.e., L = UΛUT, where Λ = diag ([λ0,...,λN−1]) ∈ RN×N. The signal x ∈ RN transformed by the graph Fourier is represented as xˆ = UTx ∈ RN, and its inverse graph Fourier transform is x = Uxˆ [46]. It has projected the input signals to an orthonormal space where the bases are formed by the eigenvectors of the normalized graph Laplacian [50].

The convolution on graph G is deﬁned below:

#### x ∗G g = U UTx UTg , (1)

in which denotes the element-wise Hadamard product and g ∈ RN is a convolutional ﬁlter. Here, g is non-parametric and it is denoted as gθ(Λ) = diag(θ), where θ ∈ RN is the vector of the Fourier coefﬁcients. The convolutional operation implemented in the GCNs is in the following.

#### x ∗G gθ = gθ UΛUT x = Ugθ(Λ)UTx. (2)

The difference of the spectral graph convolution lies in the choice of the ﬁlter gθ. Since the non-parametric ﬁlter is not localized in space, and its computational complexity is too high, we use the polynomial approximation to address the problem. The Chebyshev polynomials are popularly utilized

to approximate ﬁlters [51]. gθ is parametrized as a truncated expansion as follows:

gθ(Λ) =

K−1

θkTk(Λ˜), (3)

k=0

in which parameters θ ∈ RK is a set of Chebyshev coefﬁcients, Tk(Λ˜) ∈ RK is the kth order Chebyshev polynomial evaluated at Λ˜ = 2Λ/Λmax−IN, and IN is a diagonal matrix of the scaled eigenvalues.

Then, the signal x is convolutioned by the deﬁned ﬁlter gθ

- as follows:

x ∗G gθ = U

K−1

k=0

θkTk(Λ˜)UTx =

K−1

k=0

θkTk(L˜)x. (4)

Tk(L˜) is the Chebyshev polynomial of order k evaluated

- at the scaled Laplacian L˜ = 2L/λmax − IN. Let x¯k = Tk(L˜)x ∈ RN, a recursive relation is utilized to compute x¯k, i.e., x¯k = 2L˜x¯k−1 − x¯k−2 with x¯0 = x, and x¯1 = Lx˜ . Another reason why the Chebyshev polynomial is applied to approximate convolutional ﬁlters is that it implicitly avoids computations for the graph Fourier basis, thus reducing the computational complexity from O(N2) to O(KN).

3) Graph Coarsening and Fast Pooling: Compared with the pooling operation in CNNs, on graphs, it involves nodes clustering and one-dimensional pooling. To carry out pooling to reduce dimensionality, the Graclus multilevel clustering algorithm is performed [52]. A greedy algorithm is employed to measure the consecutive coarser of the graph and minimize the objective of the spectral clustering [53]. 1) At each level, multiple numbers of the coarser graphs are given. 2) It picks an unmarked node i, and matches with its unmarked neighborhood j, which needs to maximize the local normalized cut Wij (1/di + 1/dj). Wij denotes the edge weight between the node i and node j, and di and dj are the distances between the coarsened node and the node i and node j, respectively [52], [53]. 3) It will mark the two matched nodes, and the sum of their weights will be the coarsened weight. 4) All the nodes will undergo the same procedure. Noticeably, at the coarsest level, the nodes will be arbitrarily ordered. Then, the ordered nodes will be propagated to the ﬁnest level. Finally, the graph signal is pooled in a one-dimensional manner [35]. This algorithm cuts the number of nodes by two between two levels.

D. Model Initialization

A novel structure of the GCNs is introduced to classify EEG MI tasks. Based on the absolute Pearson’s matrix of overall signals, the graph Laplacian is built up to represent the topological relationship of EEG electrodes. The graph convolutional layers learn the generalized features. Built on a maximum of log2 N graph pooling layers regarding N EEG channels, the pooling operation reduces dimensionality, and the FC softmax layer derives the ﬁnal prediction. With regard to 64-channel international 10-10 EEG system, the maximum number of pooling layers is six. The implementation details are listed in Table I, where N denotes the input size of the

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

(a) (b) (c) (d)

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

(e) (f) (g) (h)

- Fig. 2. The PCC matrix, absolute PCC matrix, adjacency matrix, and graph Laplacian for 20 and 100 subjects, respectively, from the PhysioNet Dataset. (a) The PCC matrix for 20 subjects. (b) The absolute PCC matrix for 20 subjects. (c) The adjacency matrix for 20 subjects. (d) The graph Laplacian for 20 subjects. (e) The PCC matrix for 100 subjects. (f) The absolute PCC matrix for 100 subjects. (g) The adjacency matrix for 100 subjects. (h) The graph Laplacian for 100 subjects.

TABLE I IMPLEMENTATION DETAILS OF THE PROPOSED GCNS-NET ON THE PHYSIONET DATASET

Polynomial Order

Pooling Size

Layer Type Maps Size Edges

Activation Weights Bias

###### Softmax Fully-connected − O − − − Softmax 64N × 64N × F6 × O O Flatten Flatten − 64N × 64N × F6 − − − − − −

###### N 32 −1 i=1 i − 2 − − −

P6 Max-pooling F6 32N

###### N 32 −1 i=1 i K − Softplus F5 × F6 × K 32N × F6

C6 Convolution F6 32N

###### N 16 −1 i=1 i − 2 − − −

P5 Max-pooling F5 16N

###### N 16 −1 i=1 i K − Softplus F4 × F5 × K 16N × F5

C5 Convolution F5 16N

N 8 −1

P4 Max-pooling F4 N8

i=1 i − 2 − − − C4 Convolution F4 N8

N 8 −1

i=1 i K − Softplus F3 × F4 × K N8 × F4 P3 Max-pooling F3 N4

N 4 −1

i=1 i − 2 − − − C3 Convolution F3 N4

N 4 −1

i=1 i K − Softplus F2 × F3 × K N4 × F3 P2 Max-pooling F2 N2

N 2 −1

i=1 i − 2 − − − C2 Convolution F2 N2

N 2 −1

i=1 i K − Softplus F1 × F2 × K N2 × F2 P1 Max-pooling F1 N iN=1−1 i − 2 − − − C1 Convolution F1 N Ni=1−1 i K − Softplus 1 × F1 × K N × F1

Input Input 1 N Ni=1−1 i − − − − −

EEG signals, Fi ∈ [F1,F2,F3,F4,F5,F6] donates the number of ﬁlters at the ith graph convolutional layer, K denotes the polynomial order for ﬁlters, and O is the number of MI tasks.

The hyperparameters in our work (e.g., learning rate, dropout rate, and weight decay rate) are mainly empirically chosen over all the experiments, which are not task-oriented tuned. The network parameters, i.e., weights and biases, are updated by the Adam iterative solver [54] with a 0.01 learning rate. Biases are applied to every node of the graph. The batch size is 1,024 to maximize the usage of GPU resources. For FC layers in Section IV-A, a 50% dropout rate is applied [55]. The batch normalization (BN) is employed for graph convolutions. The BN normalizes the input graph signals by subtracting

the mean and dividing the standard deviation of the minibatch. Then, it scales and shifts the normalized signals to align with the original distribution. It not only alleviates the problem of internal covariate shift but also prevents gradient vanishing [56]. The non-linear Smooth Rectiﬁed Linear Unit (Softplus) activation function is applied to the graph convolutional layers and FC layers to prevent gradient vanishing [57], where x are the input signals.

##### Softplus(x) = log (1 + exp(x)). (5)

The softmax function is utilized to derive the ﬁnal predic-

TABLE II PERFORMANCE COMPARISONS OF THE GCNS-NET

Accuracy w.r.t. 2ndorder

Accuracy w.r.t. 3rdorder

Accuracy w.r.t. 4thorder

Accuracy w.r.t. 5thorder

Accuracy w.r.t. 1storder

Num. of Conv Layers

Num. of Pooling Layers

Num. of Filters

Model

Model Framework

- 1 1 1 16 C-P-S 55.63% 55.30% 56.70% 56.60% 56.04%
- 2 2 1 16, 32 C-C-P-S 57.94% 61.90% 63.17% 63.16% 63.37%
- 3 2 2 16, 32 (C-P)×2-S 60.04% 62.32% 62.55% 62.96% 62.08%
- 4 3 1 16, 32, 64 C-C-C-P-S 58.07% 69.18% 69.86% 71.17% 70.98%
- 5 3 2 16, 32, 64 C-(C-P)×2-S 61.65% 69.73% 70.19% 71.06% 71.45%
- 6 3 3 16, 32, 64 (C-P)×3-S 65.03% 70.50% 69.12% 70.36% 71.30%
- 7 4 2 16, 32, 64, 128 C-C-(C-P)×2-S 63.27% 77.09% 77.04% 78.42% 78.15%
- 8 4 2 16, 32, 64, 128 (C-C-P)×2-S 63.69% 77.59% 77.32% 79.28% 77.43%
- 9 4 3 16, 32, 64, 128 C-(C-P)×3-S 67.50% 77.63% 77.67% 79.60% 78.36%
- 10 4 4 16, 32, 64, 128 (C-P)×4-S 71.22% 77.61% 78.50% 78.22% 78.26%
- 11 5 3 16, 32, 64, 128, 256 C-C-(C-P)×3-S 70.11% 83.06% 82.78% 84.29% 84.19%
- 12 5 3 16, 32, 64, 128, 256 (C-C-P)×2-C-P-S 70.12% 83.05% 82.49% 84.26% 83.45%
- 13 5 4 16, 32, 64, 128, 256 C-(C-P)×4-S 75.93% 84.17% 83.90% 84.74% 84.57%
- 14 5 5 16, 32, 64, 128, 256 (C-P)×5-S 77.79% 84.39% 84.30% 83.90% 85.08%
- 15 6 3 16, 32, 64, 128, 256, 512 C-C-C-(C-P)×3-S 70.73% 86.77% 86.52% 87.62% 87.30%
- 16 6 3 16, 32, 64, 128, 256, 512 (C-C-P)×3-S 73.59% 87.09% 86.71% 87.83% 87.21%
- 17 6 4 16, 32, 64, 128, 256, 512 C-C-(C-P)×4-S 77.69% 87.63% 87.18% 88.18% 87.94%
- 18 6 4 16, 32, 64, 128, 256, 512 C-P-(C-C-P)×2-C-P-S 78.38% 87.65% 87.70% 87.80% 87.36%
- 19 6 5 16, 32, 64, 128, 256, 512 C-(C-P)×5-S 81.89% 88.60% 88.08% 88.45% 88.97%
- 20 6 6 16, 32, 64, 128, 256, 512 (C-P)×6-S 84.88% 88.85% 88.25% 88.37% 87.90%

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

(a) (b) (c) (d)

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

(e) (f) (g) (h)

- Fig. 3. Accuracy of some selected models regarding different polynomial approximation order. The models are selected from Table II. (a) Accuracy of the model C1-P1 (model 1). (b) Accuracy of the model C2-P2 (model 3). (c) Accuracy of the model C3-P3 (model 6). (d) Accuracy of the model C4-P4 (model 10). (e) Accuracy of the model C5-P5 (model 14). (f) Accuracy of the model C6-P3 (model 16). (g) Accuracy of the model C6-P5 (model 19). (h) Accuracy of the model C6-P6 (model 20).

tion.

exp(ˆyi) O

, (6)

Softmax(ˆyi) =

exp(ˆyi)

i=1

where yˆi ∈ [yˆ1,··· ,yˆO] is the predicted probability of the ith MI task. In Eqn. (7), the cross-entropy loss with the L2 regularization (weight decay) is employed as the loss function. Meanwhile, the weight decay rate ρ is set to 1 × 10−2.

O

ρ 2NP

#### W 2. (7)

Loss = −

yi log (ˆyi) +

i=1

yi, W, and NP are the corresponding MI task, network parameters, and the number of parameters, respectively.

E. Evaluation Metrics

To evaluate performance, multiple metrics are adopted, including accuracy, Cohen’s Kappa coefﬁcient (Kappa) [58],

single class accuracy on each task, Macro-averaged precision, recall, F1-score, Receiver Operating Characteristic Curve (ROC curve), and the Area Under ROC Curve (AUC). Besides, to validate whether the performance difference between methods is statistically signiﬁcant, the pair-wise t-test is applied. In this work, the signiﬁcance level of the t-test, i.e., the p-value, is set to 0.05 [59].

IV. RESULTS AND DISCUSSION A. A Novel Deep Learning Framework of the GCNs

To explore an optimal model for the GCNs-Net, as detailed in Table II, the decoding performance of multiple structures is investigated by changing some network hyperparameters, such as the number of graph convolutional (Conv) and pooling layers, the polynomial order of the Chebyshev polynomials for ﬁlters, and the number of convolutional ﬁlters. C denotes a graph convolutional layer, P denotes a graph pooling layer, F denotes an FC layer, and S denotes a softmax layer. The

TABLE III MODEL PERFORMANCE COMPARISONS BY CHANGING THE NUMBER OF FC LAYERS AND THE NUMBER OF FILTERS

Num. of Filters

Num. of FC Layers

Num. of Neurons at FC Layer

Model

Model Framework Accuracy Base 16, 32, 64, 128, 256, 512 1 4 (C-P)×6-S 88.85%

- 1 32, 64, 128, 256, 512, 1024 1 4 (C-P)×6-S 90.60%
- 2 64, 128, 256, 512, 1024, 1536 1 4 (C-P)×6-S 90.89%
- 3 16, 32, 64, 128, 256, 512 2 64, 4 (C-P)×6-F-S 88.08%
- 4 16, 32, 64, 128, 256, 512 2 512, 4 (C-P)×6-F-S 88.64%
- 5 16, 32, 64, 128, 256, 512 3 512, 64, 4 (C-P)×6-F×2-S 87.36%
- 6 16, 32, 64, 128, 256, 512 3 512, 256, 4 (C-P)×6-F×2-S 88.35%
- 7 32, 64, 128, 256, 512, 1024 3 512, 64, 4 (C-P)×6-F×3-S 90.45%

[Figure 34]

[Figure 35]

(a) (b)

[Figure 36]

[Figure 37]

(c) (d)

- Fig. 4. Accuracy of different models while applying the same polynomial order. (1) Accuracy of different models regarding the 1st order Chebyshev polynomial. (b) Accuracy of different models regarding the 2nd order Chebyshev polynomial. (c) Accuracy of different models regarding the 5th order Chebyshev polynomial. (d) Accuracy of the top ten models.

PhysioNet Dataset is used to compare the performance of different architectures, as it contains the largest number of participants in the ﬁeld of EEG MI. The amount of data makes it particularly well suited for training DL models. The dataset of 20 subjects (S1∼S20) with 64-channel 1,075,200 samples (640 time points × 84 trials × 20 subjects) is utilized to train and evaluate different architectures.

First of all, while holding the number of graph Conv and pooling layers, experiments are carried out by changing the Chebyshev polynomial order from 1st to 5th as described in Table II. Fig. 3(a) displays that when there is only one graph Conv layer followed by a graph pooling layer, the order of the Chebyshev does not make a difference. The accuracy regarding each order is less than 58%. They overlap with each other and ﬂuctuate during training. Additionally, when the number of graph Conv layers is greater than one, the accuracy of the model with the 1st order approximation ascends. In the later epochs, it enters a period of dormancy. The accuracy of models with the 1st order witnesses a rugged and abrupt ascent when there are more graph Conv layers. Apart from the number of graph Conv layers, the accuracies of models move upward

smoothly with the increasing number of pooling layers.

As illustrated in Fig. 3, the accuracy regarding models with the 1st polynomial order is unsatisfactory. By contrast, the accuracies of models regarding the 2nd to 5th polynomial orders are making a different climb. But they almost overlap and parallel with each other during training. It indicates that when the order of polynomial approximation is greater than one, there is a minor impact on the EEG MI decoding. As a result, 2nd order Chebyshev approximation for ﬁlters is employed to not only achieve a superior performance but also reduce the model complexity.

Besides, the impacts of performance by changing the number of graph Conv and pooling layers are ablated at a speciﬁc polynomial approximation order. Fig. 4 demonstrates that when the number of graph Conv layers increases, the accuracies take a steep climb. Notably, as for the 2nd polynomial order in Fig. 4(b), it illustrates that the number of Conv layers does affect performance. While applying a deeper model, including extra Conv layers, features can be better extracted from EEG signals. Meanwhile, the effects of the number of graph pooling layers are also investigated. The number of pooling layers promotes and enhances the decoding performance, but with a modest increment. As detailed in Fig. 4(d), when the polynomial order is 2nd, the accuracies are 88.60% (Model C6-P5-K2) and 88.85% (Model C6-P6-K2), respectively.

Furthermore, based on the optimal C6-P6-K2 model which contains six graph Conv layers with the 2nd polynomial order for ﬁlters and six graph pooling layers, the inﬂuence on performances by changing the number of convolutional ﬁlters at every Conv layer and the number of FC layers is also explored in Table III.

[Figure 38]

[Figure 39]

(a) (b)

Fig. 5. Accuracy and loss of models with different numbers of FC layers and ﬁlters. (a) Accuracy of models with different numbers of FC layers and ﬁlters. (b) Loss of models with different numbers of FC layers and ﬁlters.

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

(a) (b) (c) (d)

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

(e) (f) (g) (h)

- Fig. 6. The PCC matrix, absolute PCC matrix, adjacency matrix, and graph Laplacian for Subject 10 and 5 from the PhysioNet Dataset. (a) The PCC matrix for Subject 10. (b) The absolute PCC matrix for Subject 10. (c) The adjacency matrix for Subject 10. (d) The graph Laplacian for Subject 10. (e) The PCC matrix for Subject 5. (f) The absolute PCC matrix for Subject 5. (g) The adjacency matrix for Subject 5. (h) The graph Laplacian for Subject 5.

In Fig. 5, it shows that when there are more ﬁlters at the graph Conv layers, the accuracy ascends marginally. However, as indicated in Fig. 5(b), the loss value rises slightly after a fall. It means that the model with more ﬁlters has caused overﬁtting. The reason is that the model structure becomes much more complicated while applying more ﬁlters. Consequently, regarding the PhysioNet Dataset, 16, 32, 64, 128, 256, and 512 ﬁlters are used for the six-layer GCNs-Net to prevent overﬁtting. Meanwhile, there is a gentle descent of performances while adding more FC layers. As a result, a softmax layer is directly implemented without applying extra FC layers.

B. Subject-level Validation

The GCNs-Net is validated on 10 subjects from the PhysioNet Dataset, each with 64-channel 53,760 samples (640 time points × 84 trials × 1 subjects). The decoding accuracies are listed as follows: S1 (97.08%), S2 (90.70%), S3 (97.92%), S4 (96.86%), S5 (80.49%), S6 (89.55%), S7 (84.82%), S8 (97.40%), S9 (97.02%), and S10 (98.72%).

According to Fig. 6, the PCC matrix, absolute PCC matrix, adjacency matrix, and graph Laplacian for Subject 10 and 5 are shown, which achieve the highest and the lowest accuracy. There are quite a lot of variations underlying the intersubject EEG signals. For each one of the 10 subjects, 98.72% maximum accuracy is achieved. As for the model of Subject 10, the AUC is 0.99. The single class accuracies on the L, R, B, and F are 99.92%, 97.96%, 98.08%, and 98.93%, respectively. For 10 subjects, the highest F1-score is 98.71%, and the lowest is 80.19%.

Meanwhile, the presented GCNs-Net is validated on the High Gamma Dataset. The model containing 14 subjects is separately trained and evaluated. Since there are 44 electrodes [24], the maximum number of pooling layers is 2. We use the (C-C-C-P)×2 architecture of the GCNs-Net to decode

EEG tasks. From Subject 1 to Subject 14, 96.43%, 95.63%, 93.04%, 99.18%, 98.65%, 94.77%, 93.49%, 97.91%, 95.48%, 96.77%, 98.55%, 98.69%, 98.34%, and 90.43% accuracies are achieved, respectively. The mean accuracy is 96.24%. The results indicate that the GCNs-Net manages to handle the individual variability due to its robustness and effectiveness.

C. Classiﬁcation at the Group Level

Next, the GCNs-Net is evaluated at a group of 20 subjects (S1∼S20) from the PhysioNet Dataset. The accuracy, Kappa, precision, recall, and F1-score are 88.35%, 84.47%, 88.39%, 88.35%, and 88.34%, respectively. Further, the single class accuracies on the L, R, B, and F are 83.45%, 86.72%, 83.96%, and 99.42%, separately. The method performs well in classes F and B on the PhysioNet Dataset. The AUC is 0.92. Besides, it is evaluated on the High Gamma Dataset. The data of 14 subjects is used in the experiment. 80.89% accuracy and 80.78% F1-score are achieved. The reason for the accomplishment is that the GCNs-Net converges for the groupwise predictions, and succeeds in extracting relevant features from EEG signals.

D. 10-fold Cross-validation for Reliability

The GCNs-Net is trained at the group level of 20 subjects (S1∼S20) from the PhysioNet Dataset, following the 10-fold cross-validation to validate the stability and reliability. We divide the dataset into ten pieces and use one of them as the testing set, and the left nine pieces as the training set in turn.

With the results from Section IV-A (88.85% accuracy, Model C6-P6-K2), 11 results are listed in Fig. 7. 89.39% maximum accuracy is achieved, and the lowest is 87.90%. The averaged accuracy and F1-score are both 88.57%. At the group level, the performance is stably reproducible through repetitive experiments for cross-validation, showing the reliability and stability of the GCNs-Net.

TABLE IV PERFORMANCE COMPARISONS ON THE PHYSIONET DATASET Related Work Max. Accuracy Avg. Accuracy p-value Level Approach Num. of Subjects Dose et al. (2018) [22] − 58.58% − Group

105

CNNs

80.38% 68.51% < 0.05 Subject 1 Ma et al. (2018) [60] 82.65% 68.20% − Group RNNs 12 Hou et al. (2020) [20]

94.50% − − Group

10 96.00% − > 0.05 Subject 1

ESI-CNNs

94.64% − − Group

20 98.81% 95.48% > 0.05 Subject 1

Hou et al. (2022) [34]

BiLSTM-GCN

94.16% 93.78% − Group

20 98.08% 94.18% > 0.05 Subject 1

Jia et al. (2022) [40]

Graph ResNet

20 88.14% − 100 98.72% 93.06% Subject 1

89.39% 88.57%

Group

Author

GCNs-Net

−

[Figure 48]

[Figure 49]

(a) (b)

- Fig. 7. Accuracy and F1-score of the repetitive experiments for 20 subjects from the PhysioNet Dataset. (a) Accuracy of the repetitive experiments for 20 subjects. (b) F1-score of the repetitive experiments for 20 subjects.

E. Robustness to Data Size

It has also been trained and evaluated on different amounts of participants on the PhysioNet Dataset. The dataset of 50 subjects (S1∼S50) with 64-channel 2,688,000 samples (640 time points × 84 trials × 50 subjects) and the dataset of 100 subjects (S1∼S100) with 64-channel 5,376,000 samples (640 time points × 84 trials × 100 subjects) are used. Accuracies and losses are illustrated in Fig. 8.

[Figure 50]

(a) (b)

[Figure 51]

- Fig. 8. Accuracy and loss regarding various sizes of datasets, i.e., 20, 50, and 100 subjects, from the PhysioNet Dataset. (a) Accuracy regarding various sizes of datasets. (b) Loss regarding various sizes of datasets.

The GCNs-Net has achieved 89.75% (testing set) and 94.99% (training set) accuracies for a group of 50 subjects. Further, it also achieves 88.14% (testing set) and 93.24% (training set) accuracies for 100 subjects. The results have shown that it learns the generalized features from subjects at a larger scale. The reason for this phenomenon is that the GCNsNet handles a larger amount of subjects, suggesting the adaptability and robustness to individual variability. The presented method is much more effective and robust in processing the

graph-structured EEG-based MI signals since it has considered the functional topological relationship of EEG electrodes.

F. Comparison with State-of-the-art

Two-level experiments are applied to compare the performance of the current models, i.e., either from the subject level or the group level 1. The decoding performance is mainly measured by the maximum accuracy (Max. Accuracy) and the averaged accuracy (Avg. Accuracy) on two datasets. First of all, the performance on the PhysioNet Dataset is compared in Table IV.

The ESI-CNNs approach has achieved 94.50% maximum accuracy at the group level (10 subjects) [20]. Lately, the graph learning-based methods, e.g., BiLSTM-GCN and Graph ResNet, achieve highly competitive performances. This phenomenon is due to the superiority of the graph representation learning for EEG signal processing [34], [40]. The GCNsNet also obtains competing performances, 89.39% maximum accuracy for a group of 20 participants, and 88.14% for 100 participants. Meanwhile, at the subject level, the pvalue between the GCNs-Net and the CNNs model [22] is signiﬁcantly less than 0.05. It indicates a signiﬁcant difference in the predictive performance between two models, and the GCNs-Net is superior to predict EEG tasks, with a 30.21% maximum accuracy increment. However, compared with the ESI-CNNs approach [20], there is no signiﬁcant difference in classiﬁcation performance at a 95% conﬁdence interval as the p-value is greater than 0.05. Furthermore, the GCNs-Net attains the best state-of-the-art performance at the hundredsubject level on the PhysioNet Dataset, which far exceeds current studies. The reason for the outcome is that the presented approach maintains robust and effective on the dataset with a larger amount of participants, regardless of the inter-trial and inter-subject variations.

In Table V, we compare the classiﬁcation performance of some representative works [24], [29], [61] on the High Gamma Dataset. Evaluated on the High Gamma Dataset, the p-values are both less than 0.05 while comparing the introduced method with the CNNs-based methods [24], [61]. The performance is

1The reported results are derived from the corresponding papers. The ESICNNs (2020) [20] method was re-implemented via the source codes provided by the authors: https://github.com/SuperBruceJia/EEG-Motor-ImageryClassiﬁcation-CNNs-TensorFlow.

###### TABLE V PERFORMANCE COMPARISONS ON THE HIGH GAMMA DATASET

Related Work Avg. Accuracy p-value Level Approach Dataset Schirrmeister et al. (2017) [24] 92.50% < 0.05

CNNs Li et al. (2019) [61] 93.70% < 0.05 CP-MixedNet 1 subjects Tang et al. (2020) [29] 95.30% > 0.05 DAN

Subject

14 subject 96.24% Subject 1 subject

80.89%

Group

Author

GCNs-Net

−

signiﬁcantly different among the models. The GCNs-Net successfully predicts MI tasks with dominant performances, i.e., 99.18% maximum accuracy, and 96.24% averaged accuracy. The p-value compared with the DAN approach [29] is greater than 0.05. The performance of the two models is statistically less different, and both models achieve competing performances. Last but not least, the dominant classiﬁcation accuracy has veriﬁed the robustness and effectiveness of our presented GCNs-Net.

V. CONCLUSION

In order to deeply extract network patterns of brain dynamics, the GCNs-Net, a novel deep learning framework based on the GCNs, is presented to distinguish four-class MI intentions by cooperating with the functional topological relationship of EEG electrodes. The introduced method has been proven to converge for both personalized and groupwise predictions. Trained with individual data, the approach has achieved an averaged accuracy of 93.06% (PhysioNet Dataset) and 96.24% (High Gamma Dataset) in predicting the independent trials of the same participant, which is dominant in existing studies, indicating that the GCNs-Net converges well for individuals. Moreover, it has reached the uppermost accuracy on numerous sizes of group-level prediction on the PhysioNet Dataset, i.e., with 89.39% accuracy for 20 subjects, 89.75% for 50 subjects, and 88.14% for 100 subjects, which implies that it is considerably robust to individual variability. Further, it holds an averaged accuracy of 88.57% after 10-fold cross-validation showing reliability and stability. On the other hand, it predicts all four MI tasks with superior accuracy, the best among which is the two feet prediction with an accuracy of 99.42%. It indicates that the introduced method is able to build a generalized representation against both personalized and group-wise variations. In conclusion, we have developed a novel GCNs-Net method for EEG data classiﬁcation. The outstanding performance of our method in MI identiﬁcation is an important step towards better BCI approaches and neuroscience research.

VI. ACKNOWLEDGMENT

The authors appreciate the anonymous reviewers for their constructive comments to substantially improve this work. S. Jia personally would like to thank Prof. Y. Hou, Dr. J. Lv, Prof. Y. Li, Dr. Y. Shi, Prof. S. Zhang, and Prof. H. Yang for their patient guidance, encouragement, and helpful discussions, and this research paper would not have happened without them.

REFERENCES

[1] G. Santhanam, S. I. Ryu, M. Y. Byron, A. Afshar, and K. V. Shenoy, “A high-performance brain-computer interface,” Nature, vol. 442, no. 7099, pp. 195–198, July 2006.

- [2] M. A. Silver, D. Ress, and D. J. Heeger, “Topographic maps of visual spatial attention in human parietal cortex,” J. Neurophysiol., vol. 94, no. 2, pp. 1358–1371, Feb. 2006.
- [3] D. L. Schomer and F. H. L. da Silva, Niedermeyer’s electroencephalography basic principles, clinical applications, and related ﬁelds: Basic principles, clinical applications, and related ﬁelds. Oxford, UK: Oxford University Press, Nov. 2017.
- [4] J. Hubbard, A. Kikumoto, and U. Mayr, “Eeg decoding reveals the strength and temporal dynamics of goal-relevant representations,” Sci. Rep., vol. 9, no. 1, pp. 1–11, June 2019.
- [5] D. J. McFarland, L. A. Miner, T. M. Vaughan, and J. R. Wolpaw, “Mu and beta rhythm topographies during motor imagery and actual movements,” Brain Topogr., vol. 12, no. 3, pp. 177–186, Mar. 2000.
- [6] H. K. Lee and Y.-S. Choi, “A convolution neural networks scheme for classiﬁcation of motor imagery eeg based on wavelet time-frequecy image,” in Int. Conf. Inf. Commun. Syst., pp. 906–909, Jan. 2018.
- [7] D. S. Bassett and O. Sporns, “Network neuroscience,” Nat. Neurosci., vol. 20, no. 3, pp. 353–364, Feb. 2017.
- [8] J. Lv, X. Jiang, X. Li, D. Zhu, S. Zhang, S. Zhao, H. Chen, T. Zhang, X. Hu, J. Han, J. Ye, L. Guo, and T. Liu, “Holistic atlases of functional networks and interactions reveal reciprocal organizational architecture of cortical function,” IEEE Trans. Biomed. Eng., vol. 62, no. 4, pp. 1120– 1131, Apr. 2015.
- [9] J. Lv, V. T. Nguyen, J. van der Meer, M. Breakspear, and C. C. Guo, “Nway decomposition: Towards linking concurrent eeg and fmri analysis during natural stimulus,” in Med. Image Comput. Comput. Assist. Interv., pp. 382–389, Springer, Springer International Publishing, Sept. 2017.
- [10] S. Taran, V. Bajaj, D. Sharma, S. Siuly, and A. Sengur, “Features based on analytic imf for classifying motor imagery eeg signals in bci applications,” Measurement, vol. 116, pp. 68–76, Feb. 2018.
- [11] T. Yu, J. Xiao, F. Wang, R. Zhang, Z. Gu, A. Cichocki, and Y. Li, “Enhanced motor imagery training using a hybrid bci with feedback,” IEEE Trans. Biomed. Eng., vol. 62, no. 7, pp. 1706–1717, Feb. 2015.
- [12] B. J. Edelman, B. Baxter, and B. He, “Eeg source imaging enhances the decoding of complex right-hand motor imagery tasks,” IEEE Trans. Biomed. Eng., vol. 63, no. 1, pp. 4–14, July 2015.
- [13] W. Wu, X. Gao, B. Hong, and S. Gao, “Classifying single-trial eeg during motor imagery by iterative spatio-spectral patterns learning (ISSPL),” IEEE Trans. Biomed. Eng., vol. 55, no. 6, pp. 1733–1743, June 2008.
- [14] H. He and D. Wu, “Transfer learning for brain-computer interfaces: A euclidean space data alignment approach,” IEEE Trans. Biomed. Eng., vol. 67, no. 2, pp. 399–410, Apr. 2019.
- [15] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature, vol. 521, no. 7553, pp. 436–444, May 2015.
- [16] H. Lin, H. Chen, C. Yin, Q. Zhang, Z. Li, Y. Shi, and H. Men, “Lightweight residual convolutional neural network for soybean classiﬁcation combined with electronic nose,” IEEE Sens. J., vol. 22, no. 12, pp. 11463–11473, May 2022.
- [17] Q. Zhang, S. Kang, C. Yin, Z. Li, and Y. Shi, “An adaptive learning method for the fusion information of electronic nose and hyperspectral system to identify the egg quality,” Sens. Actuators, A, vol. 346, p. 113824, Oct. 2022.
- [18] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “EEGNet: A compact convolutional neural network for eeg-based brain-computer interfaces,” J. Neural Eng., vol. 15, no. 5, p. 056013, July 2018.
- [19] O. Faust, Y. Hagiwara, T. J. Hong, O. S. Lih, and U. R. Acharya, “Deep learning for healthcare applications based on physiological signals: A review,” Comput. Methods Programs Biomed., vol. 161, pp. 1–13, July 2018.
- [20] Y. Hou, L. Zhou, S. Jia, and X. Lun, “A novel approach of decoding eeg four-class motor imagery tasks via scout esi and cnn,” J. Neural Eng., vol. 17, no. 1, p. 016048, Feb. 2020.
- [21] S. U. Amin, M. Alsulaiman, G. Muhammad, M. A. Mekhtiche, and M. Shamim Hossain, “Deep learning for eeg motor imagery classiﬁcation based on multi-layer cnns feature fusion,” Future Gener. Comput. Syst., vol. 101, pp. 542–554, Dec. 2019.
- [22] H. Dose, J. S. Møller, H. K. Iversen, and S. Puthusserypady, “An endto-end deep learning approach to mi-eeg signal classiﬁcation for bcis,” Expert Syst. Appl., vol. 114, pp. 532–542, Dec. 2018.
- [23] S. Chaudhary, S. Taran, V. Bajaj, and A. Sengur, “Convolutional neural network based approach towards motor imagery tasks eeg signals classiﬁcation,” IEEE Sens. J., vol. 19, no. 12, pp. 4494–4500, June 2019.
- [24] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for eeg decoding and

- visualization,” Hum. Brain Mapp., vol. 38, no. 11, pp. 5391–5420, Nov. 2017.
- [25] C. J. Ortiz-Echeverri, S. Salazar-Colores, J. Rodr´ıguez-Res´endiz, and R. A. G´omez-Loenzo, “A new approach for motor imagery classiﬁcation based on sorted blind source separation, continuous wavelet transform, and convolutional neural network,” Sensors, vol. 19, no. 20, p. 4541, Oct. 2019.
- [26] D. Li, J. Wang, J. Xu, and X. Fang, “Densely feature fusion based on convolutional neural networks for motor imagery eeg classiﬁcation,” IEEE Access, vol. 7, pp. 132720–132730, Sept. 2019.
- [27] R. Zhang, Q. Zong, L. Dou, and X. Zhao, “A novel hybrid deep learning scheme for four-class motor imagery classiﬁcation,” J. Neural Eng., vol. 16, no. 6, p. 066004, Oct. 2019.
- [28] R. Alazrai, M. Abuhijleh, H. Alwanni, and M. I. Daoud, “A deep learning framework for decoding motor imagery tasks of the same hand using eeg signals,” IEEE Access, vol. 7, pp. 109612–109627, Aug. 2019.
- [29] X. Tang and X. Zhang, “Conditional adversarial domain adaptation neural network for motor imagery eeg decoding,” Entropy, vol. 22, no. 1, p. 96, Jan. 2020.
- [30] A. L. Goldberger, L. A. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, and et al., “PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals,” Circ., vol. 101, no. 23, pp. e215–e220, June 2000.
- [31] D. Zhang, L. Yao, K. Chen, S. Wang, X. Chang, and Y. Liu, “Making sense of spatio-temporal preserving representations for eeg-based human intention recognition,” IEEE Trans. Cybern., vol. 50, no. 7, pp. 3033– 3044, July 2020.
- [32] C. Brunner, R. Leeb, G. M¨uller-Putz, A. Schl¨ogl, and G. Pfurtscheller, “BCI Competition 2008-Graz data set A,” Inst. for Knowl. Discov., Lab. of Brain Comput. Interfaces, Graz Univ. of Technol., vol. 16, 2008.
- [33] M. Tangermann, K.-R. M¨uller, A. Aertsen, N. Birbaumer, C. Braun, C. Brunner, R. Leeb, C. Mehring, K. Miller, G. Mueller-Putz, G. Nolte, G. Pfurtscheller, H. Preissl, G. Schalk, A. Schl¨ogl, C. Vidaurre, S. Waldert, and B. Blankertz, “Review of the BCI Competition IV,” Front. Neurosci., vol. 6, July 2012.
- [34] Y. Hou, S. Jia, X. Lun, S. Zhang, T. Chen, F. Wang, and J. Lv, “Deep feature mining via the attention-based bidirectional long short term memory graph convolutional neural network for human motor imagery recognition,” Front. Bioeng. Biotechnol., vol. 9, Feb. 2022.
- [35] M. Defferrard, X. Bresson, and P. Vandergheynst, “Convolutional neural networks on graphs with fast localized spectral ﬁltering,” in Adv. Neural Inf. Process. Syst., vol. 29, pp. 3844–3852, Curran Associates, Inc., Dec. 2016.
- [36] T. Zhang, X. Wang, X. Xu, and C. L. P. Chen, “GCB-Net: Graph convolutional broad network and its application in emotion recognition,” IEEE Trans. Affective Comput., vol. 13, no. 1, pp. 379–388, Jan. 2022.
- [37] Z. Wang, Y. Tong, and X. Heng, “Phase-locking value based graph convolutional neural networks for emotion recognition,” IEEE Access, vol. 7, pp. 93711–93722, July 2019.
- [38] T. Song, W. Zheng, P. Song, and Z. Cui, “Eeg emotion recognition using dynamical graph convolutional neural networks,” IEEE Trans. Affective Comput., vol. 11, no. 3, pp. 532–541, July 2020.
- [39] X. Wang, T. Zhang, X. Xu, L. Chen, X. Xing, and P. Chen, “Eeg emotion recognition using dynamical graph convolutional neural networks and broad learning system,” in IEEE Int. Conf. Bioinformatics Biomed., pp. 1240–1244, Dec. 2018.
- [40] S. Jia, Y. Hou, Y. Shi, and Y. Li, “Attention-based graph resnet for motor intent detection from raw eeg signals,” arXiv preprint arXiv:2007.13484, 2022.
- [41] W. Hamilton, Z. Ying, and J. Leskovec, “Inductive representation learning on large graphs,” in Adv. Neural. Inf. Process. Syst., vol. 30, pp. 1024–1034, Curran Associates, Inc., Dec. 2017.
- [42] F. Monti, D. Boscaini, J. Masci, E. Rodola, J. Svoboda, and M. M. Bronstein, “Geometric deep learning on graphs and manifolds using mixture model cnns,” in Proc. IEEE Comput. Soc. Conf. Comput. Vis., pp. 5115–5124, July 2017.
- [43] M. Niepert, M. Ahmed, and K. Kutzkov, “Learning convolutional neural networks for graphs,” in Proc. Int. Conf. Mach. Learn., vol. 48 of Proceedings of Machine Learning Research, (New York, NY, USA), pp. 2014–2023, PMLR, June 2016.
- [44] H. Gao, Z. Wang, and S. Ji, “Large-scale learnable graph convolutional networks,” in Proc. ACM SIGKDD Int. Conf. on Knowl. Discov. and Data Min., KDD ’18, (New York, NY, USA), pp. 1416–1424, Association for Computing Machinery, July 2018.
- [45] J. Bruna, W. Zaremba, A. Szlam, and Y. LeCun, “Spectral networks and locally connected networks on graphs,” in Proc. Int. Conf. Learn. Represent., 2014.

- [46] D. I. Shuman, S. K. Narang, P. Frossard, A. Ortega, and P. Vandergheynst, “The emerging ﬁeld of signal processing on graphs: Extending high-dimensional data analysis to networks and other irregular domains,” IEEE Signal Process Mag., vol. 30, no. 3, pp. 83–98, May 2013.
- [47] W. Zheng and B. Lu, “Investigating critical frequency bands and channels for eeg-based emotion recognition with deep neural networks,” IEEE Trans. Auton. Ment. Dev., vol. 7, no. 3, pp. 162–175, May 2015.
- [48] Z. Jiao, X. Gao, Y. Wang, J. Li, and H. Xu, “Deep convolutional neural networks for mental load classiﬁcation based on eeg data,” Pattern Recognit., vol. 76, pp. 582–595, Apr. 2018.
- [49] R. Chai, S. H. Ling, P. P. San, G. R. Naik, T. N. Nguyen, Y. Tran, A. Craig, and H. T. Nguyen, “Improving eeg-based driver fatigue classiﬁcation using sparse-deep belief networks,” Front. Neurosci., vol. 11, Mar. 2017.
- [50] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu, “A comprehensive survey on graph neural networks,” IEEE Trans. Neural Networks Learn. Syst., vol. 32, no. 1, pp. 4–24, Jan. 2021.
- [51] D. K. Hammond, P. Vandergheynst, and R. Gribonval, “Wavelets on graphs via spectral graph theory,” Appl. Comput. Harmon. Anal., vol. 30, no. 2, pp. 129–150, Mar. 2011.
- [52] I. S. Dhillon, Y. Guan, and B. Kulis, “Weighted graph cuts without eigenvectors: A multilevel approach,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 29, no. 11, pp. 1944–1957, Sept. 2007.
- [53] J. Shi and J. Malik, “Normalized cuts and image segmentation,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 22, no. 8, pp. 888–905, Aug. 2000.
- [54] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in Proc. Int. Conf. Learn. Represent., 2015.
- [55] N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, “Dropout: A simple way to prevent neural networks from overﬁtting,” J. Mach. Learn. Res., vol. 15, no. 1, pp. 1929–1958, Jan. 2014.
- [56] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by reducing internal covariate shift,” in Proc. Int. Conf. Mach. Learn., pp. 448–456, PMLR, July 2015.
- [57] H. Zheng, Z. Yang, W. Liu, J. Liang, and Y. Li, “Improving deep neural networks using softplus units,” in Proc. Int. Jt. Conf. Neural Netw., pp. 1–4, July 2015.
- [58] J. Cohen, “A coefﬁcient of agreement for nominal scales,” Educ. Psychol. Meas., vol. 20, no. 1, pp. 37–46, Apr. 1960.
- [59] P. Zhang, X. Wang, W. Zhang, and J. Chen, “Learning spatial-spectraltemporal eeg features with recurrent 3d convolutional neural networks for cross-task mental workload assessment,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 27, no. 1, pp. 31–42, Dec. 2018.
- [60] X. Ma, S. Qiu, C. Du, J. Xing, and H. He, “Improving eeg-based motor imagery classiﬁcation via spatial and temporal recurrent neural networks,” in Conf. Proc. IEEE Eng. Med. Biol. Soc., pp. 1903–1906, July 2018.
- [61] Y. Li, X. Zhang, B. Zhang, M. Lei, W. Cui, and Y. Guo, “A channelprojection mixed-scale convolutional neural network for motor imagery eeg decoding,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 27, no. 6, pp. 1170–1180, June 2019.

