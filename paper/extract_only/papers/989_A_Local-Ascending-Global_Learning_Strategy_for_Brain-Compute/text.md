# A Local-Ascending-Global Learning Strategy for Brain-Computer Interface

## Dongrui Gao1,2*, Haokai Zhang1*, Pengrui Li1,2, Tian Tang1, Shihong Liu1, Zhihong Zhou1, Shaofei Ying2, Ye Zhu1†, Yongqing Zhang1†

1School of Computer Science, Chengdu University of Information Technology, Chengdu, 610225, China 2 School of Life Sciences and Technology, University of Electronic Science and Technology of China, Chengdu, 611731, China gdr1987@cuit.edu.cn, 1326036086@qq.com, 925189684@qq.com, 2741187967@qq.com, 1585538946@qq.com, zhouzhihong201802@163.com, shaofei9629@163.com, zhuye@cuit.edu.cn, zhangyq@cuit.edu.cn

#### Abstract

Neuroscience research indicates that the interaction among different functional regions of the brain plays a crucial role in driving various cognitive tasks. Existing studies have primarily focused on constructing either local or global functional connectivity maps within the brain, often lacking an adaptive approach to fuse functional brain regions and explore latent relationships between localization during different cognitive tasks. This paper introduces a novel approach called the Local-Ascending-Global Learning Strategy (LAG) to uncover higher-level latent topological patterns among functional brain regions. The strategy initiates from the local connectivity of individual brain functional regions and develops a K-Level Self-Adaptive Ascending Network (SALK) to dynamically capture strong connectivity patterns among brain regions during different cognitive tasks. Through the step-bystep fusion of brain regions, this approach captures higherlevel latent patterns, shedding light on the progressively adaptive fusion of various brain functional regions under different cognitive tasks. Notably, this study represents the first exploration of higher-level latent patterns through progressively adaptive fusion of diverse brain functional regions under different cognitive tasks. The proposed LAG strategy is validated using datasets related to fatigue (SEED-VIG), emotion (SEED-IV), and motor imagery (BCI C IV 2a). The results demonstrate the generalizability of LAG, achieving satisfactory outcomes in independent-subject experiments across all three datasets. This suggests that LAG effectively characterizes higher-level latent patterns associated with different cognitive tasks, presenting a novel approach to understanding brain patterns in varying cognitive contexts.

## Introduction

Brain-computer interface (BCI) technology, as an advanced system, enables the bidirectional transformation of human brain information and computer signals, facilitating direct communication (Zhang et al. 2021a). Various signal sources and modalities, including electroencephalogram (EEG), functional Near-infrared spectroscopy (fNIRS), and Electromyography (EMG), are utilized for the evaluation and analysis of brain signals (Gao et al. 2023a; Kwak, Song,

*These authors contributed equally. †Corresponding author: Ye Zhu, Yongqing Zhang

Copyright © 2024, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.

and Kim 2022; Zhang et al. 2021b). Among these, EEG, known for its non-invasiveness and high temporal resolution, is widely employed (Zhou et al. 2023).

Recent breakthroughs in decoding dynamic changes in brain functions have been achieved through learning strategies that incorporate psychological and biological prior knowledge combined with graph networks. Conventional graph neural networks often utilize prior graph structures like Pearson’s Correlation Coefficient (COR) (Mukaka 2012), Phase Locking Value (PLV) (Vinck et al. 2011) and Partial Directed Coherence (PDC) (Sameshima and Baccal´a 1999) for learning correlations between channels. One study based on mental fatigue used three frequency domain measures to estimate the functional connectivity of the brain (Qi et al. 2020). However, these methods may have limitations in capturing the complexity of the brain under various cognitive tasks, emphasizing the need for exploring local circuits within each brain region and functional connectivity among different regions. Therefore, the study for the learning of local circuits in each brain region and the functional connectivity of different brain regions is lacking. In addition, brain activity in different states requires the joint work of all brain regions, and thus the internal functional changes of each brain region may have a certain activating or suppressing effect on other brain regions. It has been shown that the functional relationships between brain regions are highly localized and sparse, so a new sparse-constrained method for improving Dynamic Graph Convolutional Neural Networks (DGCNN) has been proposed for further exploring the functional relationships between local brain regions (Zhang et al. 2023). However, these methods may eliminate too many important features in localized brain regions when exploring functional relationships between brain regions.

Therefore, an advanced learning strategy for efficiently fitting connectivity within the brain and between various brain functional regions has become a hot research topic. Some works have proposed to learn dynamically changing brain functional networks by developing advanced local and global adjacency matrices (Gao et al. 2022; Li et al. 2023a). It has been found that the functional relationships between electrodes may be highly localized and sparse, thus Sparse Dynamic Graph Convolutional Neural Network (SparseDGCNN) was proposed to learn the dynamic fea-

tures of the brain network both locally and globally (Zhang et al. 2023). In addition, Local Global Graph Neural Network (LGGNet) establishes spatial connectivity within brain regions by dividing brain regions through biological prior knowledges, and combines locally learned spatial features and obtains global connectivity (Ding et al. 2023). However, they failed to recognize the complex connections and latent features in individual brain regions and between multiple brain regions.

To summarize, existing works suffers from these shortcomings: (1) Above-mentioned methods lack exploring the functional connectivity of one-to-one or one-to-multiple brain regions; (2) Existing methods lack research on adaptive step-by-step exploration of global connectivity under different cognitive tasks; (3) The negative impact of complex brain mechanisms on the effectiveness of model recognition has not yet been resolved.

Addressing the shortcomings of existing approaches, our paper proposes an advanced Local-Ascending-Global Learning Strategy (LAG) to uncover latent local-global topological information among brain functional regions through stepwise incremental learning. Neuroscience research indicates dynamic changes in the functional connectivity of brain regions under different cognitive tasks, and that the strength and positivity of node connectivity within and between brain regions reflect the functional relationships of brain activities. Mapping the functional connectivity of brain regions onto local and global maps can express the complex functional connectivity between different brain functional regions. In order to learn the local node properties and complex features within each brain region, the proposed study employs multi-kernel convolution to generate a multilayer spatial projection map for each brain region, followed by input into a bidirectional gated recurrent unit (BiGRU) to capture temporal dependencies between channels and reinforce the connection between EEG and different cognitive tasks.

To adaptively explore the activity and connectivity of brain regions in different states, we introduce a K-Level Self-Adaptive Ascending Network (SALK). SALK adaptively ascends the fusion of brain regions, selecting the region with the highest internal connectivity at each step. The process continues until a global generative map containing first-level features and higher-level latent patterns among all brain regions is obtained. Classification of different cognitive tasks is performed using Dynamic Graph Convolutional Neural Networks (DGCNN) (Zhang et al. 2023). Our results demonstrate that LAG outperforms existing state-ofthe-art methods on fatigue dataset (Gao et al. 2023a), emotion dataset (Zhang et al. 2023), and motor imagery dataset (Zhang et al. 2019).

In summary, our contributions include:

- (1) Introducing the Local-Ascending-Global Learning

Strategy (LAG) to uncover latent correlations between oneto-one and one-to-multiple brain regions, capturing latent local-global patterns.

- (2) Proposing a K-Level Self-Adaptive Ascending Net-

work (SALK) to dynamically detect active differences in brain regions during different cognitive tasks, gradually fus-

ing from local to global regions to enhance the model’s generalization ability.

(3) Validating the proposed strategy on three datasets with different cognitive tasks, demonstrating LAG’s adaptive characterization of brain patterns and providing a new research direction for BCI development.

## Method

As shown in Fig. 1, The experimental flow in this paper comprises three modules: local feature extraction, K-level self-adaptive ascending learning, and graph learning. Before delving into the details, let’s define some symbols. Represent the features of the three datasets as D = {Dd},d = {1,2,3}. Then, B = {BM},M = {6,10,4} is obtained by dividing each Dd into M subsets of brain regions by function, as shown in Fig. 2. For illustrative purposes, the learning process of the model is presented using the fatigue dataset as an example in the following subsections.

### Local Feature Extraction

The objective is to learn node connections within each brain functional region, capturing local features and intranodal connectivity through fully connected operations. Relational perception is employed to learn local-global attention (Zhang et al. 2020), utilizing pairwise relations associated with inter-channel features to represent local-global structural information. The specific calculations are as follows. For EM = (X1,X2,...,XN) ∈ RB×C×T with N samples, where B, C, and T represent the number of bands, channels, and time points of the samples, respectively. Calculation of multiple frequency band feature node values involve the Ghost module (Han et al. 2020) and are outlined below:

yijstem Bj=1 = Bj=1 Φi,j(X) + bi,j, ∀i = 1,2,...,T,j = 1,2,...,B

(1)

where Φi,j represents the j − th linear operation. Next, T EEG channels of the same length are generated using dot convolution (Cui et al. 2022), which is computed as follows:

 

B j=1

{hp,j}mp=1

= mp=1 Bj=1 wp,j(y) + bp,j, ∀p = 1,2,...,m

- (2)

where m denotes the number of electrode channels contained in a subset. This results in a channel mapping map GMC generated by mapping channels to a new space:

GMC = hi(yp,j) = (feature1p,j,feature2p,j,...,featureNp,j)

- (3)



Next, squeeze GMC using frequency band attention (Zhang et al. 2020) to compress C ∗ T to 1 ∗ 1 to compute the frequency band attention feature node values. At the same time, spatial attention (Zhang et al. 2020) is used to compute spatial attention feature node values by downscaling B in GMC to 1. Finally, the frequency band attention feature node values and spatial attention feature node values are fused to generate the spatial mapping map GMS for each brain functional region.

##### GMS = FA(GMC ) SA(GMC ) (4)

|EEG<br><br>Eigen feature<br><br>Ghost feature<br><br>Feature<br><br>B C<br><br>T embeding max<br><br>mean<br><br>T B<br><br>B<br><br>T<br><br>T B<br><br>Cat<br><br>Conv<br><br>B<br><br>T<br><br>C<br><br><br>1<br><br>Avg_pool<br><br>Feature Max_pool<br><br>g<br><br>a<br>b q d<br><br><br>GRU<br><br>GRU<br><br>Local Feature Extraction<br><br>B<br><br>B 1<br><br>B<br><br>B| |
|---|---|
|[Figure 1]<br><br>[Figure 2]<br><br>[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>[Figure 6]<br><br>[Figure 7]<br><br>[Figure 8]<br><br>[Figure 9]<br><br>[Figure 10]<br><br>[Figure 11]<br><br>[Figure 12]<br><br>[Figure 13]<br><br>[Figure 14]<br><br>[Figure 15]<br><br>[Figure 16]<br><br>[Figure 17]<br><br>[Figure 18]<br><br>[Figure 19]<br><br>[Figure 20]<br><br>[Figure 21]<br><br>[Figure 22]<br><br>[Figure 23]<br><br>[Figure 24]<br><br>[Figure 25]<br><br>[Figure 26]<br><br>[Figure 27]<br><br>[Figure 28]<br><br>[Figure 29]<br><br>[Figure 30]<br><br>[Figure 31]<br><br>[Figure 32]<br><br>[Figure 33]<br><br>[Figure 34]<br><br>[Figure 35]<br><br>Conv<br><br>[Figure 36]<br><br>[Figure 37]<br><br>[Figure 38]<br><br>[Figure 39]<br><br>[Figure 40]<br><br>Conv<br><br>[Figure 41]<br><br>[Figure 42]<br><br>[Figure 43]<br><br>[Figure 44]<br><br>[Figure 45]<br><br>[Figure 46]<br><br>[Figure 47]<br><br>[Figure 48]<br><br>[Figure 49]<br><br>[Figure 50]<br><br>[Figure 51]<br><br>[Figure 52]<br><br>[Figure 53]<br><br>[Figure 54]<br><br>[Figure 55]<br><br>[Figure 56]<br><br>[Figure 57]<br><br>[Figure 58]<br><br>[Figure 59]<br><br>[Figure 60]<br><br>[Figure 61]<br><br>[Figure 62]<br><br>[Figure 63]<br><br>[Figure 64]<br><br>[Figure 65]<br><br>[Figure 66]<br><br>[Figure 67]<br><br>[Figure 68]<br><br>[Figure 69]<br><br>[Figure 70]<br><br>[Figure 71]<br><br>[Figure 72]<br><br>[Figure 73]<br><br>[Figure 74]<br><br>[Figure 75]<br><br>[Figure 76]<br><br>[Figure 77]<br><br>[Figure 78]<br><br>[Figure 79]<br><br>[Figure 80]<br><br>[Figure 81]<br><br>[Figure 82]<br><br>[Figure 83]<br><br>[Figure 84]<br><br>[Figure 85]<br><br>[Figure 86]<br><br>[Figure 87]<br><br>[Figure 88]<br><br>[Figure 89]<br><br>[Figure 90]<br><br>[Figure 91]<br><br>[Figure 92]<br><br>[Figure 93]<br><br>[Figure 94]<br><br>[Figure 95]<br><br>[Figure 96]<br><br>[Figure 97]<br><br>[Figure 98]<br><br>[Figure 99]<br><br>[Figure 100]<br><br>[Figure 101]<br><br>[Figure 102]<br><br>[Figure 103]<br><br>[Figure 104]<br><br>[Figure 105]<br><br>[Figure 106]<br><br>[Figure 107]<br><br>[Figure 108]<br><br>[Figure 109]<br><br>[Figure 110]<br><br>[Figure 111]<br><br>[Figure 112]<br><br>[Figure 113]<br><br>[Figure 114]<br><br>[Figure 115]<br><br>[Figure 116]<br><br>[Figure 117]<br><br>[Figure 118]<br><br>[Figure 119]<br><br>[Figure 120]<br><br>[Figure 121]<br><br>[Figure 122]<br><br>[Figure 123]<br><br>[Figure 124]<br><br>[Figure 125]<br><br>[Figure 126]<br><br>[Figure 127]<br><br>[Figure 128]<br><br>[Figure 129]<br><br>[Figure 130]<br><br>[Figure 131]<br><br>[Figure 132]<br><br>[Figure 133]<br><br>[Figure 134]<br><br>[Figure 135]<br><br>[Figure 136]<br><br>[Figure 137]<br><br>[Figure 138]<br><br>[Figure 139]<br><br>[Figure 140]<br><br>Continue ascending<br><br>Select brain<br><br>Calulate Score<br><br>[Figure 141]<br><br>[Figure 142]<br><br>[Figure 143]<br><br>[Figure 144]<br><br>[Figure 145]<br><br>[Figure 146]<br><br>[Figure 147]<br><br>[Figure 148]<br><br>[Figure 149]<br><br>[Figure 150]<br><br>[Figure 151]<br><br>[Figure 152]<br><br>K-Level Adaptive Ascending Learning<br><br>|Fully connected layer<br><br>Softmax<br><br>DGCNN<br><br>Output<br><br>Predicted label<br><br>Graph Learning Module<br><br>| |
|---|
|

Figure 1: The experimental flow of LAG.

FT7

FT8

T7

T8

CP1 CPZ CP2

TP7

TP8

P1 PZ P2

PO3 POZ PO4

O1

O2

OZ

FPZ

FP1 AF3

FP2 AF4

F7

F8 F3 F1

F5

F6

FZ F2 F4

FT7

FC5 FC3 FC1 FCZ FC2 FC4 FC6 FT8

T7

C5 C3 C1 CZ C2 C4 C6 T8

CPZ

CP2 CP4 CP6

CP5 CP3 CP1

TP7

TP8

P5 P3 P1 P2 P4 P6

PZ

P7

P8

PO5 PO3 PO4 PO6

POZ

PO7

PO8

O1 CB1 CB2

O2

OZ

FZ

FC3 FC1 FCZ FC2 FC4

C5 C3 C1 CZ C2 C4 C6

CP3 CP1 CPZ CP2 CP4

P1 P2

PZ

POZ

(a) SEED-VIG

(b) SEED-IV

(c) BCI C IV 2a

Figure 2: Presentation of brain region division on different datasets.

where FA and SA represent frequency band attention and spatial attention, respectively. After obtaining the GMS , input them to BiGRU to capture the temporal dependence between channels to reinforce the link between EEG and different cognitive tasks, thereby capturing the reinforced spatial mapping map RGMS for each brain functional region:

l

GRU(GMS ),l = 1 GRUl(GRUl−1),l>1

RGMS =

(5)

l=1

where l represents the number of layers of the GRU. Ultimately, the GMC and RGMS are fused at the nucleus level of the full connectivity layer to capture node-localized features within each brain functional region.

LM = Gfuse(GMC ,RGMS ;θ) (6) where θ represents the parameters of the fusion layer at the nucleus level. Thus the localized feature node values for each brain functional region can be obtained:

L = (L1,L2,...,LM) (7)

### K-Level Self-Adaptive Ascending Learning

Brain Fusion In order to gradually extend the obtained local features of each brain region to the global features, all the two-by-two brain regions are firstly fused with the features and the first-level hidden features between the two-by-two brain regions are extracted to obtain the first-level generative graph features. Given a subclassification task, for the i − th and j − th brain regions, BC consists of paired local brain region feature node values.

BC1 = {(Li,Lj)},with

- i = 1,2,..., (M − 1)
- j = (i + 1),...,M

(8)

Firstly, the local feature node values L of each brain region are eliminated from redundant data by Singular Value Decomposition (SVD) for better feature fusion. Then the frequency domain features U of the two brain regions are extracted and feature fusion is performed on these two fea-

tures, which is calculated as follows:

 

- Ui,Ai = SV D(Li),with

i = 1,2,..., (M − 1)

- Ai = σiVi

Uj,Aj = SV D(Lj),with

j = (i + 1),...,M

- Aj = σjVj



(9)

Uij = Ui Uj (10) where the U, σ, V obtained by SVD is transformed into two parts, U and A. U is the frequency domain feature information extracted from SVD, and A is the channel importance weight inside the brain region. At this point, the obtained first-level frequency-domain fusion information Uij is then used to update the internal channel importance weights of the two brain regions under the influence of the frequencydomain information, respectively, and the calculation process is as follows:

L ˆi = UijAi Lˆj = UijAj

,with

- i = 1,2,..., (M − 1)
- j = (i + 1),...,M

(11)

Then, the brain region feature maps Lˆi and Lˆj obtained from the frequency domain update are again decomposed to extract the time domain information by SVD. Firstly, the extracted first-level time domain information is fused, and secondly, the channel importance weights of the decomposed two brain areas are merged to obtain the global channel information of the two brain regions. Next, the fused first-level time domain information is used to update the global channel information of the merged two brain regions to obtain the first-level brain region hidden features. Finally, the learned first-level joint brain region hidden features and the original brain functional region feature maps are fused to obtain complete first-level joint brain functional region feature maps, and the specific computational process is as follows:

 

- Uˆi,Aˆi = SV D(LˆTi ),with

i = 1,2,..., (M − 1)

- Aˆi = σˆiVˆi

Uˆj,Aˆj = SV D(LˆTj ),with

j = (i + 1),...,M

- Aˆj = σˆjVˆj



(12) Lˆij = (Uˆi U ˆj)(Aˆi A ˆj) (13)

Lij = Lˆij Li Lj (14) Ln = {Lij},with{n = 1,2,...,M(M − 1)/2} (15)

Self-Adaptive Ascending Learning To identify the main active regions of the brain in different states under different cognitive tasks, a correlation score is proposed, calculating the strength of connectivity within a brain region. A correlation score for each channel within each joint brain region is computed, and the joint brain regions with the strongest internal connectivity are selected through comparison. The relevance scores of each channel are calculated, and the joint brain regions with strong relevance are selected. This process continues until the optimal joint brain regions are obtained.

The correlation score of each channel within each joint brain region is first calculated, and the weight matrix W ∈ RBT×T is used to nonlinearly transform the joint brain region’s feature Lnc for that channel. Then the time-domain shared attention vector qt ∈ RT×1 is applied to obtain the feature attention value of each channel, which is used to update the raw map features of each channel. Here, both negative correlations and weights are considered as the strength of connectivity within the brain regions, so absolute value is used to obtain positive values. Next, the updated graph relevance features of each channel are fused to obtain the relevance scores of each channel, and the joint brain regions with the strongest internal connectivity are selected through comparison by applying the channel shared attention vector qc ∈ RC×1 to obtain the fused channel feature attention values after normalization to limit the scores to between [0,1]. The specific calculation formulas are as follows:

ωcn = qt · tanh(abs(W) · abs(Lnc ))b + b, with{c = 1,2,...,C}

(16)

Scn =

ωcn Lnc (17)

T

Sn = σsig((qc · Sci)b + b),with{i = 1,2,...,n} (18) B1 = Ln | argmax[S1,S2,...,Sn] ⇒ (B1 = Ln), with{n = 1,2,...,M(M − 1)/2}

(19) where abs and b represent the absolute value and bias vector, respectively. In order to adapt to the batch processing in deep learning training, after calculating the relevance scores of a batch, the average of the data within the three-sigma rule of thumb in the batch is taken for selecting the strong relevance brain regions of the batch, while a small amount of data outside the range of three-sigma rule of thumb can be used as the noise to increase the robustness of the model. The formula is as follows:

##### Pr(µ − 3σ ≤ S ≤ µ + 3σ) ≈ 0.95 (20)

Based on the optimal joint brain regions obtained from the computation, we continue to fuse the remaining brain regions to find the higher-level hidden features, and finally obtain the global brain functional feature maps. The whole ascending process is as follows:



G ⇒ AscendingStage ⇒ 

BCk = (Bk−1,Li)

(Uk−1,Ak−1),(Ui,Ai) = SV D(BCk) BCˆ k = (Uk−1 Ui) (Ak−1,Ai)



(Uˆk−1,Aˆk−1),(Uˆi,Aˆi) = SV D(BCˆ k) {Lk−1,i} = (Uˆk−1 U ˆi)(Aˆk−1 A ˆi) (Bk−1,Li) Bk = {{Ln | argmax[S({Lk−1,i})]}





⇒ (Bk = Ln)

 

k = 2,3,..., (M − 1) i = 1,2,..., (M − 2) n = 1,2,...,M(M − 1)/2

with





(21)

### Graph Learning Module

The global brain functional region feature node values learned after the above feature learning process, i.e., the pairwise relationship values between the B × C feature nodes, and the inter-correlation between the channels of the global brain region is obtained by dimensionality transformation feature fusion. The calculation formula is as follows:

G = Bk(Bk)T ∈ RB×C×C (22)

The global brain functional region feature node values learned are used to construct a graph learning module based on DGCNN (Song et al. 2020). The original node features are updated with the learned global structure G.

Graph = DGCNN(G,DE) (23)

The graph learning module is then updated using the attention mechanism.

Graph score = Softmax Fc1∗1[Fc1∗C(Graph;θ1);θ2]

(24) AG = Graph score ∗ Graph (25)

where θ1 and θ2 represent the parameters of the two fully connected layers respectively. The final input is classified in the fully connected layer.

′

′′

ypred = Fc1∗class σsig[Fc1∗C(AG;θ

)];θ

(26)

where class and σsig represent the category and the Sigmoid function. θ

′

′′

represent the parameters of the two fully connected layers, respectively.

and θ

### Training Process

The loss functions used for binary classification and multiclassification tasks are cross entropy (CE) and the mean square error function (MSE). The training process involves the backpropagation algorithm to optimize the model. The network update process is as follows:

Loss = CE&MSE(ytrue,ypred) + α∥Θ∥ (27)

where ytrue and ypred represent the true label and the predicted label. Θ is the model parameters, and α is the tradeoff regularization weights to prevent model overfitting in parameter learning. To summarize, the training process of LAG is shown in Algorithm 1.

## Experimental Result

This paper presents validation experiments conducted on three EEG datasets (SEED-VIG, SEED-IV, BCI C IV 2a) each associated with distinct cognitive tasks (Gao et al. 2023a; Peng et al. 2023; Zhang et al. 2019). These experiments aim to substantiate the robustness and generalizability of the proposed learning strategy in decoding cognitive tasks. EEG signals are filtered into five frequency bands (δ: 0.5-4Hz, θ: 4-8Hz, α: 8-14Hz, β: 14-30Hz, γ: 30-50Hz). The graph convolution order is set to 2, and a dropout rate of 0.5 is applied. Model parameters are optimized using the Adam optimizer, with a learning rate search range of [1e-3, 1e-1] and an L2 regularization search range of [5e-3, 3e-1].

Algorithm 1: Training Stage Input: Train set G = {BM} Output: {ypred,Loss}

- 1: Initialization:
- 2: Extract local features:
- 3: for n ← 1 to N do
- 4: GMC ← hi(yijstem(Xn));
- 5: RGMS ← GMS ← [BA(GMC ) SA(GMC )];
- 6: L ← Gfuse(GMC ,RGMS ;θ);
- 7: end for
- 8: Self-Adaptive Ascending:
- 9: for n ← 1 to M(M − 1)/2 do
- 10: Lˆ ← (U,A) ← SV D(BC1);
- 11: Lˆij ← (U,ˆ Aˆ) ← SV D(Lˆ); Ln ← (Lˆij BC1);
- 12: end for
- 13: for k ← 1 to M − 2 do
- 14: Bk ← Sn ← SCORE({Ln});
- 15: Bk+1 ← (Bk L);
- 16: end for
- 17: Graph learning module:
- 18: G ← Bk(Bk)T
- 19: Graph score ← Graph ← (G,DE);

- 20: ypred ← AG ← (Graph score,Graph);

- 21: Loss ← (ytrue,ypred);
- 22: Update LAG parameters.
- 23: return {ypred,Loss}

### Comparison with State-of-The-Art Methods

To validate the efficacy of the proposed learning strategy, independent-subject experiments were conducted based on established studies (Gao et al. 2023a; Peng et al. 2023; Zhang et al. 2019). For methods not utilizing these datasets, we reproduced them and compared their performance with the proposed Local-Ascending-Global Learning Strategy (LAG) presented in this paper. Tables 1, 2 and 3 present the cross-subject comparison results of the LAG on SEED-VIG, SEED-IV and BCI C IV 2a, respectively. From the tables, it is evident that the recognition effectiveness of LAG on SEED-VIG and SEED-IV surpasses that of existing stateof-the-art methods by approximately 3% and 4% on average, respectively. Additionally, Table 2 indicates that the standard deviation of LAG is lower than that of other methods, signifying better stability in emotion recognition. Furthermore, LAG’s recognition performance on BCI C IV 2a outperforms the majority of state-of-the-art methods, falling marginally behind R-SPD (Fan et al. 2022) by 0.25%. Overall, the heightened generalization ability of LAG underscores that exploring hidden relationships between localities to ascend to global pattern representations is effective in characterizing brain patterns for diverse cognitive tasks.

### Ablation Study

This study conducts an ablation analysis to underscore the indispensability of the K-Level Self-Adaptive Ascending Network (SALK), employing a case study on the optimal brain region combination for fatigue recognition in the

Method ACC / F1-score (%) CSF-GTNet (Gao et al. 2023a) 81.48 / 78.23

Interpretable CNN (Cui et al. 2022) 79.62 / 80.51

SFTNet (Gao et al. 2023b) 83.18 / 86.97 E-5-D-BCDRNet (Li et al. 2023b) 80.34 / 77.02

LGGNet (Ding et al. 2023) 83.89 / 85.48 LAG (proposed) 85.15 / 87.56

- Table 1: Recognition accuracy and F1-score on the SEEDVIG dataset.

Method ACC / STD (%) RGNN (Zhong, Wang, and Miao 2022) 73.84 / 08.02

JTSR (Peng et al. 2023) 77.73 / -

FGI (Liu et al. 2023) 77.53 / 07.57 RGCBNet (Li et al. 2022) 73.69 / 09.07 PGCN (Zhou et al. 2023) 69.44 / 10.16

LAG (proposed) 78.03 / 07.38

- Table 2: Recognition accuracy and standard deviation on the SEED-IV dataset.

Method ACC (%) OVR-FBCSP (Zhang et al. 2019) 46.68

R-SPD (Fan et al. 2022) 51.2

TS-SEFFNet (Li et al. 2021) 43.76 C-LSTM (Freer and Yang 2020) 45.13

DWT-CNN (Ma et al. 2020) 49.54 LAG (proposed) 50.95

- Table 3: Recognition accuracy on the BCI C IV 2a dataset. Numbers SALK Local Global

- 1 78.38 / 79.24 74.29 / 76.94 72.15 / 75.58
- 2 81.40 / 83.92 77.89 / 75.27 76.63 / 76.67
- 3 83.09 / 85.78 78.30 / 79.46 78.04 / 77.50
- 4 84.52 / 85.67 80.01 / 79.52 79.07 / 80.98
- 5 84.98 / 84.16 81.28 / 80.19 81.73 / 83.02
- 6 85.15 / 87.56 81.93 / 84.85 82.99 / 84.64

- Table 4: SALK-based ablation studies (results are displayed in the form of ACC / F1-score (%)).

SEED-VIG dataset. Table 4 presents results, with SALK denoting the adaptive ascending strategy proposed in this paper. Comparative approaches, denoted as Local and Global, signify computations where local brain regions are processed first and then upgraded, or brain regions are directly fused and then computed, respectively (refer to Fig. 2 and Fig. 3).

The results indicate that when the model directly learns global features, the recognition performance is inferior, particularly with fewer brain regions, compared to learning by fusing local brain regions initially. As the number of brain regions increases, the advantage of the global approach becomes more apparent. However, both the Local and Global approaches directly fuse brain regions without explicitly extracting hidden relationships between them.

In contrast, SALK, as proposed in this paper, effectively learns potential relationship patterns between local brain regions. Consequently, fatigue recognition accuracy and F1score are notably higher than both the Local and Global approaches, exhibiting improvements of 3.2%, 2.15%, and 2.7%, 2.9%, respectively. For a clearer comparison, changes in connectivity strength within and between brain regions are visualized in Fig. 3.

To provide a more intuitive understanding of the model’s ascending process in SEED-VIG, Tables 5-9 showcases the attention scores assigned to brain regions at each level learned by the model. This additional insight aids in elucidating the model’s cognitive hierarchy as it processes information for fatigue recognition.

### Model Interpretability

Brain patterns learned by LAG in different cognitive tasks are presented here, as shown in Fig. 4. Take the emotion for an example, it can be found that parts of the brain are significantly activated (centered in the frontal, temporal, central, and occipital lobes) when subjected to positive and negative

stimuli, which is consistent with (Peng et al. 2023). In contrast, only occipital region of the brain is activated when the brain is not stimulated. This also suggests that brain dynamics are able to perceive and respond to external stimuli in a timely manner.

Neurophysiology shows that the brain’s perceptual functions in response to external stimuli can trigger a cascade of specific cortical responses (Candia-Rivera et al. 2022). By observing the brain patterns learned from the model for three different cognitive tasks, it is possible to identify significant differences in the functional brain regions required to accomplish each cognitive task, as reflected in the strength of neural information flow activity. Therefore, the LAG can effectively differentiate the brain patterns corresponding to different cognitive tasks, and has a strong generalization ability.

The acquired brain patterns by LAG across various cognitive tasks are elucidated in Fig. 4. Taking emotion as an example (motor imagery and fatigue are detailed in Fig. 5 and Fig. 6), it’s discernible that specific brain regions, primarily in the frontal, temporal, central, and occipital lobes, exhibit significant activation when exposed to positive and negative stimuli. This observation aligns with findings from (Peng et al. 2023). In contrast, only the occipital region of the brain is activated when there is no external stimulation, implying that the brain dynamically perceives and responds to stimuli promptly.

Neurophysiological principles indicate that the brain’s perceptual functions, triggered by external stimuli, initiate a cascade of specific cortical responses (Candia-Rivera et al. 2022). By examining the brain patterns learned by the model across three distinct cognitive tasks, notable differences in the functional brain regions required for each task become apparent, as reflected in the strength of neural information flow activity. Consequently, LAG effectively distinguishes brain patterns corresponding to different cognitive tasks, showcasing robust generalization capabilities.

[Figure 153]

[Figure 154]

[Figure 155]

(a) SALK-1 (b) SALK-2 (c) SALK-3

[Figure 156]

[Figure 157]

(d) SALK-4 (e) SALK-5

[Figure 158]

[Figure 159]

[Figure 160]

(f) Local-1 (g) Local-2 (h) Local-3

[Figure 161]

[Figure 162]

(i) Local-4 (j) Local-5

[Figure 163]

[Figure 164]

[Figure 165]

(k) Global-1 (l) Global-2 (m) Global-3

[Figure 166]

[Figure 167]

(n) Global-4 (o) Global-5

0.0-0.25 0.25-0.5 0.5-0.75 0.75-1.0

(p)

Figure 3: The ascending process of the proposed SALK and previous methods.

[Figure 168]

[Figure 169]

(a) neutral (b) sad

[Figure 170]

[Figure 171]

[Figure 172]

(c) fear (d) happy

- Figure 4: The brain patterns learned by LAG on the SEEDIV dataset.

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

(a) left_hand (b) right_hand

(c) feet (d) tongue

[Figure 177]

- Figure 5: The brain patterns learned by LAG on the BCI C IV 2a dataset.

[Figure 178]

[Figure 179]

(a) alterness (b) fatigue

[Figure 180]

- Figure 6: The brain patterns learned by LAG on the SEEDVIG dataset.

Alert Fatigue Alert Fatigue

LTL-RTL 0.46 0.18 RTL-OL 0.55 0.30 LTL-CPL 0.27 0.33 CPL-PL 0.42 0.57

LTL-PL 0.73 0.15 CPL-POL 0.62 0.65 LTL-POL 0.85 0.68 CPL-OL 0.58 0.44

LTL-OL 0.67 0.71 PL-POL 0.65 0.78 RTL-CPL 0.51 0.70 PL-OL 0.59 0.82

RTL-PL 0.47 0.38 POL-OL 0.63 0.81 RTL-POL 0.23 0.43

- Table 5: The first-level brain region attention scores learned by LAG on SEED-VIG.

Alert Fatigue

LTL-POL-RTL 0.50 PL-OL-LTL 0.67 LTL-POL-CPL 0.71 PL-OL-RTL 0.62

LTL-POL-PL 0.53 PL-OL-CPL 0.70 LTL-POL-OL 0.87 PL-OL-POL 0.83

- Table 6: The second-level brain region attention scores learned by LAG on SEED-VIG.

Alert Fatigue

LTL-POL-OL-RTL 0.82 PL-OL-POL-FTL 0.85 LTL-POL-OL-CPL 0.79 PL-OL-POL-RTL 0.72

LTL-POL-OL-PL 0.87 PL-OL-POL-CPL 0.77

- Table 7: The third-level brain region attention scores learned by LAG on SEED-VIG.

Alert Fatigue LTL-POL-OLPL-RTL

0.88

LTL-POL-OLPL-CPL

0.84 PL-OL-POLFTL-RTL

0.81

PL-OL-POLFTL-CPL

0.85

- Table 8: The fourth-level brain region attention scores learned by LAG on SEED-VIG.

Alert Fatigue LTL-POL-OLPL-RTL-CPL

0.88

PL-OL-POLFTL-CPL-RTL

0.86

- Table 9: The fifth-level brain region attention scores learned by LAG on SEED-VIG.

## Conclusion

This paper introduces a novel Local-Ascending-Global Learning Strategy (LAG). The strategy commences with the local connectivity of individual brain functional regions, constructing a K-Level Self-Adaptive Ascending Network (SALK) to dynamically capture strong connectivity patterns

among brain regions during diverse cognitive tasks. The incremental fusion of brain regions captures higher-level latent patterns between brain functional regions. Experimental results across three publicly available datasets underscore the robust generalization of LAG, affirming the learning strategy’s adaptability to various cognitive tasks. This presents a promising direction for the advancement of brain-computer interfaces.

## Acknowledgments

This work is supported by National key research and development program (2021YFF1200605), Sichuan Science and Technology Program No.2023YFG0018, and National Natural Science Foundation of China under Grant No. 62272067.

## References

Candia-Rivera, D.; Catrambone, V.; Thayer, J. F.; Gentili, C.; and Valenza, G. 2022. Cardiac sympathetic-vagal activity initiates a functional brain–body response to emotional arousal. Proceedings of the National Academy of Sciences, 119(21): e2119599119.

Cui, J.; Lan, Z.; Sourina, O.; and M¨uller-Wittig, W. 2022. EEG-Based Cross-Subject Driver Drowsiness Recognition With an Interpretable Convolutional Neural Network. IEEE Transactions on Neural Networks and Learning Systems, 1– 13.

Ding, Y.; Robinson, N.; Tong, C.; Zeng, Q.; and Guan, C. 2023. LGGNet: Learning From Local-Global-Graph Representations for Brain–Computer Interface. IEEE Transactions on Neural Networks and Learning Systems, 1–14.

Fan, M.; Tang, F.; Guo, Y.; and Zhao, X. 2022. Riemannian dynamic generalized space quantization learning. Pattern Recognition, 132: 108932.

Freer, D.; and Yang, G.-Z. 2020. Data augmentation for selfpaced motor imagery classification with C-LSTM. Journal of Neural Engineering, 17(1): 016041.

Gao, D.; Li, P.; Wang, M.; Liang, Y.; Liu, S.; Zhou, J.; Wang, L.; and Zhang, Y. 2023a. CSF-GTNet: A novel multidimensional feature fusion network based on ConvnextGeLU-BiLSTM for EEG-signals-enabled fatigue driving detection. IEEE Journal of Biomedical and Health Informatics.

Gao, D.; Wang, K.; Wang, M.; Zhou, J.; and Zhang, Y. 2023b. SFT-Net: A Network for Detecting Fatigue From EEG Signals by Combining 4D Feature Flow and Attention Mechanism. IEEE Journal of Biomedical and Health Informatics, 1–12.

Gao, L.; Yu, J.; Zhu, L.; Wang, S.; Yuan, J.; Li, G.; Cai, J.; Qi, X.; Sun, Y.; and Sun, Y. 2022. Dynamic Reorganization of Functional Connectivity During Post-Break Task Reengagement. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 30: 157–166.

Han, K.; Wang, Y.; Tian, Q.; Guo, J.; Xu, C.; and Xu, C. 2020. GhostNet: More Features From Cheap Operations.

In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).

Kwak, Y.; Song, W.-J.; and Kim, S.-E. 2022. FGANet: fNIRS-Guided Attention Network for Hybrid EEG-fNIRS Brain-Computer Interfaces. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 30: 329–339.

Li, C.; Li, P.; Zhang, Y.; Li, N.; Si, Y.; Li, F.; Cao, Z.; Chen, H.; Chen, B.; Yao, D.; and Xu, P. 2023a. Effective Emotion Recognition by Learning Discriminative Graph Topologies in EEG Brain Networks. IEEE Transactions on Neural Networks and Learning Systems, 1–15.

- Li, P.; Zhang, Y.; Liu, S.; Lin, L.; Zhang, H.; Tang, T.; and Gao, D. 2023b. An EEG-based Brain Cognitive Dynamic Recognition Network for representations of brain fatigue. Applied Soft Computing, 146: 110613.
- Li, Q.; Zhang, T.; Chen, C. L. P.; Yi, K.; and Chen, L. 2022. Residual GCB-Net: Residual Graph Convolutional Broad Network on Emotion Recognition. IEEE Transactions on Cognitive and Developmental Systems, 1–1. Li, Y.; Guo, L.; Liu, Y.; Liu, J.; and Meng, F. 2021. A Temporal-Spectral-Based Squeeze-and- Excitation Feature Fusion Network for Motor Imagery EEG Decoding. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 29: 1534–1545. Liu, B.; Guo, J.; Chen, C. L. P.; Wu, X.; and Zhang, T. 2023. Fine-grained Interpretability for EEG Emotion Recognition: Concat-aided Grad-CAM and Systematic Brain Functional Network. IEEE Transactions on Affective Computing, 1–14. Ma, X.; Wang, D.; Liu, D.; and Yang, J. 2020. DWT and CNN based multi-class motor imagery electroencephalographic signal recognition. Journal of Neural Engineering, 17(1): 016073. Mukaka, M. 2012. Statistics corner: A guide to appropriate use of correlation coefficient in medical research. Malawi medical journal : the journal of Medical Association of Malawi, 24 3: 69–71. Peng, Y.; Liu, H.; Kong, W.; Nie, F.; Lu, B.-L.; and Cichocki, A. 2023. Joint EEG Feature Transfer and Semisupervised Cross-Subject Emotion Recognition. IEEE Transactions on Industrial Informatics, 19(7): 8104–8115. Qi, P.; Hu, H.; Zhu, L.; Gao, L.; Yuan, J.; Thakor, N.; Bezerianos, A.; and Sun, Y. 2020. EEG Functional Connectivity Predicts Individual Behavioural Impairment During Mental Fatigue. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 28(9): 2080–2089. Sameshima, K.; and Baccal´a, L. A. 1999. Using partial directed coherence to describe neuronal ensemble interactions. Journal of Neuroscience Methods, 94(1): 93–103. Song, T.; Zheng, W.; Song, P.; and Cui, Z. 2020. EEG Emotion Recognition Using Dynamical Graph Convolutional Neural Networks. IEEE Transactions on Affective Computing, 11(3): 532–541. Vinck, M.; Oostenveld, R.; van Wingerden, M.; Battaglia, F.; and Pennartz, C. M. 2011. An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. NeuroImage, 55(4): 1548–1565.

Zhang, G.; Yu, M.; Liu, Y.-J.; Zhao, G.; Zhang, D.; and Zheng, W. 2023. SparseDGCNN: Recognizing Emotion From Multichannel EEG Signals. IEEE Transactions on Affective Computing, 14(1): 537–548.

Zhang, R.; Zong, Q.; Dou, L.; and Zhao, X. 2019. A novel hybrid deep learning scheme for four-class motor imagery classification. Journal of Neural Engineering, 16(6): 066004.

- Zhang, X.; Liu, J.; Shen, J.; Li, S.; Hou, K.; Hu, B.; Gao, J.; Zhang, T.; and Hu, B. 2021a. Emotion Recognition From Multimodal Physiological Signals Using a Regularized Deep Fusion of Kernel Machine. IEEE Transactions on Cybernetics, 51(9): 4386–4399.
- Zhang, Y.; Chen, S.; Cao, W.; Guo, P.; Gao, D.; Wang, M.; Zhou, J.; and Wang, T. 2021b. MFFNet: Multi-dimensional Feature Fusion Network based on attention mechanism for sEMG analysis to detect muscle fatigue. Expert Systems with Applications, 185: 115639.
- Zhang, Z.; Lan, C.; Zeng, W.; Jin, X.; and Chen, Z.

2020. Relation-Aware Global Attention for Person ReIdentification. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).

Zhong, P.; Wang, D.; and Miao, C. 2022. EEG-Based Emotion Recognition Using Regularized Graph Neural Networks. IEEE Transactions on Affective Computing, 13(3): 1290–1301.

Zhou, Y.; Li, F.; Li, Y.; Ji, Y.; Shi, G.; Zheng, W.; Zhang, L.; Chen, Y.; and Cheng, R. 2023. Progressive graph convolution network for EEG emotion recognition. Neurocomputing, 544: 126262.

