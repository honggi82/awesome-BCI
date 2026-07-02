# Converting Your Thoughts to Texts: Enabling Brain Typing via Deep Feature Learning of EEG Signals

## arXiv:1709.08820v1[cs.HC]26Sep2017

Xiang Zhang

School of Computer Science & Engineering University of New South Wales Sydney, Australia xiang.zhang3@student.unsw.edu.au

Lina Yao

School of Computer Science & Engineering University of New South Wales Sydney, Australia lina.yao@unsw.edu.au

Quan Z. Sheng

Department of Computing Macquarie University Sydney, Australia michael.sheng@mq.edu.au

Salil S. Kanhere

School of Computer Science & Engineering University of New South Wales Sydney, Australia salilk@cse.unsw.edu.au

Tao Gu

School of Science

RMIT University Melbourne, Australia

tao.gu@rmit.edu.au

Dalin Zhang

School of Computer Science & Engineering University of New South Wales Sydney, Australia dalin.zhang@student.unsw.edu.au

Abstract—An electroencephalography (EEG) based Brain Computer Interface (BCI) enables people to communicate with the outside world by interpreting the EEG signals of their brains to interact with devices such as wheelchairs and intelligent robots. More speciﬁcally, motor imagery EEG (MI-EEG), which reﬂects a subject’s active intent, is attracting increasing attention for a variety of BCI applications. Accurate classiﬁcation of MI-EEG signals while essential for effective operation of BCI systems, is challenging due to the signiﬁcant noise inherent in the signals and the lack of informative correlation between the signals and brain activities. In this paper, we propose a novel deep neural network based learning framework that affords perceptive insights into the relationship between the MI-EEG data and brain activities. We design a joint convolutional recurrent neural network that simultaneously learns robust high-level feature presentations through low-dimensional dense embeddings from raw MI-EEG signals. We also employ an Autoencoder layer to eliminate various artifacts such as background activities. The proposed approach has been evaluated extensively on a largescale public MI-EEG dataset and a limited but easy-to-deploy dataset collected in our lab. The results show that our approach outperforms a series of baselines and the competitive state-of-theart methods, yielding a classiﬁcation accuracy of 95.53%. The applicability of our proposed approach is further demonstrated with a practical BCI system for typing.

Index Terms—EEG, deep learning, brain typing, BCI

I. INTRODUCTION

Brain-computer interface (BCI) systems have been widely studied for various real-world applications from mindcontrolled service robots in the healthcare domain [1] to enriched video gaming in the entertainment industry [2]. As an important pathway between human brains and the outside world [3], BCI systems allow people to communicate or interact with external devices such as wheelchairs or service robots, through their brain signals. Among the different types of brain signals, motor imagery Electroencephalography (MIEEG) is especially popular and has demonstrated promising potential in discerning different brain activities in BCI systems. Motor imagery is a mental process where a subject

imagines performing a certain action such as closing eyes or moving feet. Basically, EEG1 is a method to analyze brain activities by measuring the voltage ﬂuctuations of ionic current within the neurons of brains. In practice, electrodes are usually placed on the scalp for the measurement in a non-invasive and non-stationary way [4].

One of the most promising and widely discussed application of EEG-based BCI is to enable people to type via direct brain control [5]. In this paper, we aim at enabling a brain typing system by enhancing the decoding accuracy of EEG signals for wider range of brain activities (e.g., multi-class scenario). We envision a real-world implementation of such a system which can interpret the user’s thoughts to infer typing commands in real-time. Motor disabled people would beneﬁt greatly from such a system to express their thoughts and communicate with the outer world.

However, EEG signals ﬂuctuate rapidly and are subject to various sources of noise including environmental noise such as lighting and electronic equipment. Thus, the key issue concerning an EEG-based BCI system is to accurately interpret EEG signals so as to accurately understand the user’s intent. More speciﬁcally, the design of a practical and effective BCIsystem is faced with the following major challenges. First, EEG signals usually have very low signal-to-noise ratio [6]. As a result, EEG signals inherently lack sufﬁcient spatial resolution and insight on activities of deep brain structures. Second, data pre-processing, parameter selection (e.g., ﬁlter type, pass band, segment window, and overlapping), and feature engineering (e.g., feature selection and extraction both in time domain and frequency domain) are all time-consuming and highly dependent on human expertise in the domain. Third, the state-of-the-art approaches can achieve an accuracy of at most 70∼85%, which though impressive is not sufﬁcient for widespread adoption of this technology. Fourth, existing

1In this paper, we will use the terms EEG and MI-EEG interchangeably.

research mainly focuses on discerning EEG signals under the binary classiﬁcation situation and little work has been conducted on multi-class scenarios. Intuitively, the more scenarios an EEG-based control system can distinguish, the wider is its applicability in the real-world.

To tackle the aforementioned challenges, we propose a novel hybrid deep neural network that combines the beneﬁts of both Convolutional Neural Networks (CNNs) [7] and recurrent neural networks (RNNs) [8] for effective EEG signal decoding. Our model is capable of modeling high-level, robust and salient feature representations hidden in the raw EEG signal streams and capturing complex relationships within data via stacking multiple layers of information processing modules in a hierarchical architecture. Speciﬁcally, RNN is designed to model sequential information while CNN is well suited to extract higher-level spatial variations. In particular, a speciﬁc RNN architecture, named Long Short-Term Memory (LSTM), is designed to model temporal sequences and their long-range dependencies more accurately than conventional RNNs. In comparison, CNN is a typical feed-forward architecture and is able to extract higher-level features that are invariant to local spectral and temporal variations. The main contributions of this paper are highlighted as follows:

- • We design a uniﬁed deep learning framework that leverages recurrent convolutional neural network to capture spatial dependencies of raw EEG signals based on features extracted by convolutional operations and temporal correlations through RNN architecture, respectively. Moreover, an Autoencoder layer is fused to cope with the possible incomplete and corrupted EEG signals to enhance the robustness of EEG classiﬁcation.
- • We extensively evaluate our model using a public dataset and also a limited but easy-to-deploy dataset that we collected using an off-the-shelf EEG device. The experiment results illustrate that the proposed model achieves highlevel of accuracy over both the public dataset (95.53%) and the local dataset (94.27%). This demonstrates the consistent applicability of our proposed model. We have made our local dataset and the source code used in our evaluations available to the research community to encourage further research in this area and foster reproducibility of results.
- • We also present an operational prototype of a brain typing system based on our proposed model, which demonstrates the efﬁcacy and practicality of our approach. A video demonstrating the system is made available 2.

II. EEG CHARACTERISTICS ANALYSIS

The key point of the brain typing system is to precisely classify the user’s intent signals. Although EEG signals have low signal-to-noise ratio and are sensitive to background brain activities and environmental factors, it is possible to recognize human intent by employing appropriate feature representation and classiﬁcation.

2http://1015xzhang.wixsite.com/mysite/demos

TABLE I THE CORRELATION COEFFICIENTS MATRIX. SELF, CROSS, AND PD SEPARATELY DENOTE SELF-SIMILARITY, CROSS-SIMILARITY AND PERCENTAGE DIFFERENCE.

|Class 0 1 2 3 4<br><br>|Self Cross PD<br><br>|
|---|---|
|0 0.4010 0.2855 0.4146 0.4787 0.3700<br><br>1 0.2855 0.5100 0.0689 0.0162 0.0546<br><br>2 0.4146 0.0689 0.4126 0.2632 0.3950<br><br>3 0.4787 0.0162 0.2632 0.3062 0.2247<br><br>4 0.3700 0.0546 0.3950 0.2247 0.3395<br><br><br>|0.401 0.3872 3.44%<br><br>0.51 0.1063 79.16% 0.4126 0.2854 30.83% 0.3062 0.2457 19.76% 0.3395 0.3156 7.04%|
|Range 0.1932 0.4938 0.3458 0.4625 0.3404 Average 0.3900 0.1870 0.3109 0.2578 0.2768 STD 0.0631 0.1869 0.1334 0.1487 0.1255<br><br>|0.2038 0.2809 75.72% 0.3939 0.2680 28.05% 0.0700 0.0932 27.33%|

To illustrate this point, we brieﬂy analyze the similarities between EEG signals corresponding to different intents and quantify them using Pearson correlation coefﬁcient. To be able to effectively interpret multiple classes of human intents, we assume that the EEG signals should meet the two hypotheses: 1) the intra-intent correlation coefﬁcients should be consistently higher than inter-intent correlation coefﬁcients; 2) the greater the difference between the intra-intent and inter-class correlation coefﬁcients, the better classiﬁcation results.

According to the two hypotheses, we introduce two similarity concepts used in our measurement: the self-similarity and the cross-similarity. Self-similarity measures the similarity of EEG signals within the same intent. We randomly select several EEG data samples from the same intent and calculate the correlation coefﬁcient of each possible pair of samples. The self-similarity for the speciﬁc intent is measured as the average of all the sample pairs’ correlation coefﬁcients. Crosssimilarity is deﬁned to measure the similarity of two samples belonging to different EEG categories. For each speciﬁc intent, we measure the correlation coefﬁcient of each possible intent pairs. In this work, the EEG dataset (discussed in detail in Section IV-A) contains 5 intents, hence there are a total of 20 intent pairs and 4 intent pairs of each speciﬁc intent. Finally, for each speciﬁc intent, the cross-similarity is the average of correlation coefﬁcients of each intent pair. Also, we measure the correlation coefﬁcients matrix for each speciﬁc subject and then calculate the average matrix (by calculating the mean value of all the matrix). For example, if there are 5 intents for a speciﬁc subject, we calculate a 5 ∗ 5 similarity matrix. In the matrix, ρ˘i,˘j denotes the correlation coefﬁcients between the sample of the intent ˘i and the sample of the intent ˘j.

Table I shows the correlation coefﬁcients matrix and the corresponding statistical self- and cross-similarity. The last column (PD) denotes Percentage Difference between the selfsimilarity and cross-similarity. We can observe from the results that the self-similarity is always higher than the crosssimilarity for all intents, which means that the intra-intent cohesion of the samples is stronger than the inter-intent cohesion. Moreover, the percentage difference has a noticeable ﬂuctuation, which demonstrates that the intra-intent cohesion varies between different intents. The above analysis results justify the two hypotheses and lay the foundation for us to design appropriate feature representations and the classiﬁer.

|[Figure 1]<br><br>[Figure 2]<br><br>[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>[Figure 6]<br><br>[Figure 7]<br><br>[Figure 8]<br><br>|
|---|

|[Figure 9]<br><br>[Figure 10]<br><br>[Figure 11]<br><br>[Figure 12]<br><br>[Figure 13]|
|---|

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

|[Figure 21]<br><br>[Figure 22]<br><br>[Figure 23]<br><br>[Figure 24]<br><br>[Figure 25]|
|---|

[Figure 26]

| |
|---|
|[Figure 27]|
| |

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

- Fig. 1. The ﬂow chart of the proposed approach. The input raw EEG data is a single sample vector denoted by E¯i ∈ RK (take K = 64 as an example). The C 1 layer denotes the ﬁrst convolutional layer, the C 2 layer denotes the second convolutional layer, and so on. The same theory, the P 1 layer denotes the ﬁrst pooling layer; the FC 1 layer denotes the ﬁrst fully connected layer; the H 1 layer denotes the ﬁrst hidden layer. The stacked temporal-spatial feature is generated by the FC 2 layer in CNN and the H 5 layer in RNN.

III. THE DEEP INTENT RECOGNITION MODEL

This paper proposes a hybrid deep learning model to classify the raw EEG signal. In this section, we ﬁrst provide an overview of the proposed approach and then present the technical details in subsequent sub-sections.

- A. Overview

Figure 1 illustrates the various steps involved. The essential goal of our approach is to design a deep learning model that precisely classiﬁes the user’s intents based on EEG data. To obtain the useful and robust EEG features, we employ a parallel feature learning method which combines RNN and CNN. RNN is useful in extracting the internal memory to process arbitrary sequences of EEG signal while CNN is well-suited for the dimensional relevance representation. In summary, we propose a hybrid approach which contains several components: the deep feature learning (Section III-B), the feature transformation and the intent recognition (Section III-C).

- B. Deep Feature Learning

We aim to learn the representations of the user’s typing intent signal which is a 1-D vector (collected in one timepoint). Let us represent the single input EEG signal as E¯i ∈ RK (K = 64) with K is the number of dimensions in the EEG raw signal. Next, we feed E¯i to the RNN structure and the CNN structure for temporal and spatial feature learning in parallel. At last, the learned temporal features Xt and the spatial features Xs are combined into the stacked feature X for the latter feature transformation (Section III-C).

1) RNN Feature Learning: In the temporal feature processing part, the RNN structure is employed for its powerful ability for temporal feature extraction in time-series data. RNN, which is one class of deep neutral network, is able to explore the feature dependencies over time through an internal state of the network, which allows it to exhibit dynamic temporal behavior. In this section, we take advantages of this trait to represent the temporal feature of the input EEG signal.

We design an RNN model consisting of three components: one input layer, 5 hidden layers, and one output layer. There

are two layers of Long Short-Term Memory (LSTM) [9] (shown as the rectangles in Figure 1) cells among the hidden layers. Assume a batch of input EEG data contains nbs (generally called batch size) EEG samples and the total input data has the 3-D shape as [nbs,1,64]. Let the data in the ith layer (i = 1,2,··· ,7) be denoted by Xir = {Xijkr |j = 1,2,··· ,nbs,k = 1,2,··· ,Ki},Xir ∈ R[n

bs,1,Ki], where j denotes the j-th EEG sample and Ki denotes the number of dimensions in the i-th layer.

Assume that the weights between layer i and layer i+1 can be denoted by Wir(i+1) ∈ R[K

i,Ki+1], for instance, W12r describes the weight between layer 1 and layer 2. bri ∈ RK

i

denotes the biases of i-th layer. The calculation between the i-th layer data and the i + 1-th layer data can be denoted as

Xir+1 = Xir ∗ Wi,ir +1 + bri

Please note the sizes of Xir, Wi,ir +1 and bri must match. For example, in Figure 1, the transformation between H1 layer and H2 layer, the sizes of X3r, X2r, W[2,3], and br2 are separately [1,1,64], [1,1,64], [64,64], and [1,64].

The 5-th and 6-th layers in the designed structure are LSTM layers, so the calculation in these layers are implemented as follows:

fi = sigmoid(T(X(ri−1)j,X(ri)(j−1))) ff = sigmoid(T(X(ri−1)j,X(ri)(j−1))) fo = sigmoid(T(X(ri−1)j,X(ri)(j−1))) fm = tanh(T(X(ri−1)j,X(ri)(j−1))) cij = ff ci(j−1) + fi fm Xijr = fo tanh(cij)

where fi,ff,fo and fm represent the input gate, forget gate, output gate and input modulation gate separately, and

denotes the element-wise multiplication. The cij denotes the state (memory) in the j-th LSTM cell in the i-th layer, which is the most signiﬁcant part to explore the time-series relevance

between samples. The T(X(ri−1)j,X(ri)(j−1)) denotes the operation as follows:

X(ri−1)j ∗ W + X(ri)(j−1) ∗ W + b where W, W and b denote the corresponding weights and biases.

At last, we obtain the RNN prediction results X7r and employ cross-entropy as the cost function. The cost is optimized by the AdamOptimizer algorithm [10]. X6r is the data in the second last layer, which has a directly linear relationship with the output layer and the prediction results. If the predicted results have high accuracy, X6r is enabled to directly map to the sample label space and has the better representative of the input EEG sample. Therefore, we regard X6r as the temporal feature extracted by the RNN structure and call it Xt.

2) CNN Feature Learning: While RNN is good in exploring the temporal (inter-sample) relevance, it is unable to appropriately decode spatial feature (intra-sample) representations. To exploit the spatial connections between different features in each speciﬁc EEG signal, we design a CNN structure. The CNN structure is comprised of three categories of components: the convolutional layer, the pooling layer, and the fully connected layer. The convolutional layer contains a set of ﬁlters to convolve with the EEG data and then through the feature pooling and non-linear transformation to extract the geographical features. CNN is well-suited to extract the spatial relevance of the 2-D input data efﬁciently. In this paper, we implement the CNN on the 1-D EEG data. As shown in Figure 1, the designed CNN is stacked in the following order: the input layer, the ﬁrst convolutional layer, the ﬁrst pooling layer, the second convolutional layer, the second pooling layer, the ﬁrst fully connected layer, the second fully connected layer, and the output layer.

The input is the same EEG data as the RNN. The input EEG single sample E¯i has shape [1,64]. Suppose the data in the ith layer (i = 1,2,··· ,8) is denoted by Xic,Xic ∈ R[1,K

c

i,di],

where Kic and di separately denote the dimension number and the depth in the i-th layer. The data in the ﬁrst layer only has

depth 1 and X1c = E. We choose the convolutional ﬁlter with size [1,1] and the stride size [1,1] in the ﬁrst convolution. The stride denotes the x-movements and y-movements distance of the ﬁlter. The padding method is selected as same shape zeropadding, which results in the sample shape keeping constant in the convolution calculation. The depth of EEG sample transfers to 2 through the ﬁrst convolutional layer, so the shape of X2c is [1,64,2].

The pooling layer is a non-linear down-sampling transformation layer. There are several pooling options, with max pooling being the most popular [11]. The max pooling layer scans through the inputs along with a sliding window with a designed stride. Then it outputs the maximum value in every sub-region that the window is scanned. The pooling layer reduces the spatial size of the input EEG features and also prevents overﬁtting. In the ﬁrst pooling layer (the 3-th layer in CNN), we choose the [1,2] window and [1,2] stride. The maximum in each [1,2] window will be output to the next

layer. The pooling does not change the depth and the shape of X3c is [1,32,2]. Similarly, the second convolutional layer chooses [1,2] ﬁlter and [1,1] stride and gets the shape as [1,32,4]. The second pooling layer selects [1,2] window and [1,2] stride and obtains the shape as [1,16,4].

In the full connected layer, the high-level reasoning features, extracted through previous convolutional and pooling layers, are unfolded to a ﬂattened vector. For example, the data of the second pooling layer (X5c with shape [1,16,4]) is ﬂattened to the vector with shape [1,64] (X6c). Then the output data can be calculated by following the regular neural network operation:

X7c = T(X6c) X8c = softmax(T(X8c))

At last, we have the CNN results X8c and employ the cross-entropy as the cost function. The cost is optimized by the AdamOptimizer algorithm. X7c has a directly linear relationship with the output layer and the predicted results. Therefore, we regard X7c as the spatial feature extracted by the CNN structure and call it Xs.

In summary, the temporal features Xt and the spatial features Xs are learned through the parallel RNN and CNN structures. Both of them have the direct linear relationship with the EEG sample label, which means that they represent the temporal and spatial features of the input EEG sample if both RNN and CNN have high classiﬁcation accuracy. Next, we combine the two feature vectors into a ﬂattened stacked vector, X = {Xt : Xs}.

C. Feature Adaptation

Next, we design a feature adaptation method to map the stacked features to a correlative new feature space which can fuse the temporal and spatial features together and highlight the useful information.

To do so, we introduce the Autoencoder layer [3] to further interpret EEG signals, which is an unsupervised approach to learning effective features. The Autoencoder is trained to learn a compressed and distributed representations for the stacked EEG feature X . The input of Autoencoder is the stacked temporal and spatial feature X . Assume h, X´ denote the hidden layer and output layer data, respectively.

The data transformation procedure is described as the following:

h = WenX + ben

X´ = Wdeh + bde

where Wen, Wde, ben, bde denote the weights and biases in the encoder and the decoder.

The cost function measures the difference between X and X´ as MSE (mean squared error) which is back-propagated to the algorithm to adjust the weights and biases. The error is optimized by the RMSPropOptimizer [12]. The data in the hidden layer h is the transferred feature, which is output to the classiﬁer. Finally, the Extreme Gradient Boosting) classiﬁer

TABLE II THE MOTOR IMAGERY TASKS AND LABELS AND THE CORRESPONDING TYPING COMMAND IN THE BRAIN TYPING SYSTEM

Dataset Item Task 1 Task 2 Task 3 Task 4 Task 5 eegmmidb

intent eye closed left hand right hand both hands both feet label 0 1 2 3 4

intent up arrow down arrow left arrow right arrow eye closed label 0 1 2 3 4 command up down left right conﬁrmation

emotiv

(XGBoost) is employed [13] to classify the EEG streams. It fuses a set of classiﬁcation and regression trees (CART) and exploits detailed information from the input data. It builds multiple trees and each tree has its leaves and corresponding scores.

IV. EXPERIMENTS

In this section, we evaluate the proposed deep learning model using a public dataset and a local dataset collected by ourselves. At ﬁrst, a public EEG dataset (called eegmmidb) is used to assess our proposed deep learning model. The experimental settings (Section IV-A), the overall comparison with the state-of-the-art methods (Section IV-B), the parameter tuning (Section IV-C), and the efﬁciency analysis (Section IV-D) are separately reported in this section. In addition, we evaluate our model on a local dataset for demonstrating the good adaptability of proposed method (the collected EEG dataset is called emotiv) and present the corresponding results (Section IV-E).

- A. Experiment Setting

We select the widely used EEG data from PhysioNet eegmmidb (EEG motor movement/imagery database) database3. This data is collected using the BCI200 EEG system4 [14] which records the brain signals using 64 channels at a sampling rate of 160Hz. The subject is asked to wear the EEG device and sit in front of a computer screen and perform certain typing actions in response to hints that appear on the screen. The researchers have carefully annotated the EEG data to correspond to the actions undertaken by the subject, which are available from the PhysioBank ATM5. For our experiments, we select a total of 280,00 labeled EEG samples collected from 10 subjects (28,000 samples per subject). Each sample is a vector of 64 elements, each of which corresponds to one channel of the EEG data. The subjects performed 5 actions which are labeled as 0 to 4, as shown in Table II.

To evaluate the performance of the classiﬁed results, we use several typical evaluation metrics such as accuracy, precision, recall, F1 score, ROC (Receiver Operating Characteristic) curve, and AUC (Area Under the Curve).

- B. Overall Comparison

In this section, we report the performance study and then demonstrate the efﬁciency of our approach by comparing with the state-of-the-art methods and other independent deep learning algorithms. Recall that the proposed approach is a

- 3https://www.physionet.org/pn4/eegmmidb/
- 4http://www.schalklab.org/research/bci2000
- 5https://www.physionet.org/cgi-bin/atm/ATM

TABLE III THE CONFUSION MATRIX OF 5-CLASS CLASSIFICATION

|Ground Truth<br><br>|Evaluation|
|---|---|
|0 1 2 3 4<br><br>0 2062 19 23 18 22<br><br>1 17 1120 19 15 20<br><br>2 13 13 1146 14 11<br><br>3 10 5 7 1162 10<br><br>Predict Lable<br><br>4 18 21 15 23 1197<br><br><br>Total 2120 1178 1210 1232 1260 Average|Precision Recall F1 AUC<br><br>0.9618 0.9380 0.9497 0.9982 0.9404 0.9084 0.9241 0.9977 0.9574 0.9257 0.9413 0.9990 0.9732 0.9028 0.9367 0.9990 0.9396 0.9392 0.9394 0.9987 4.7723 4.6140 4.6911 4.9926 0.9545 0.9228 0.9382 0.9985<br><br>|

hybrid model which uses RNN and CNN for feature learning, the AE layer for feature transformation, and the XGBoost classiﬁer for intent recognition. In this experiment, the EEG data is randomly divided into two parts: the training dataset (21,000 samples) and the testing dataset (7,000 samples). The accuracy of our method is calculated as the average of 5 runs on 10 subjects.

Firstly, we report that our approach achieves the classiﬁcation accuracy of 0.9553. To take a closer look at the result, the detailed confusion matrix and classiﬁcation reports are presented in Table III. We can observe that for every class, our approach achieves an an average precision no lower than 0.939. Figure 2 shows the ROC curves of the 5 classes.

Additionally, the accuracy comparison between our method and other state-of-the-art and baselines are listed in Table IV. Wavelet transform [2], [15]–[18] and independent component analysis (ICA) [19], [20] are state-of-the-art methods to process EEG signals. The Deep Neural Network [17], [19], [21] and Linear discriminant analysis [20] are applied to classify the EEG data. In addition, the key parameters of the baselines are listed here: KNN (k=3), Linear SVM (C = 1), RF (n = 500), LDA (tol = 10−4), and AdaBoost (n = 500,lr = 0.3). The results show that our method achieves the signiﬁcantly higher accuracy of 0.9553 than all the state-of-the-art methods. Our method also performs better than other deep learning methods such as RNN or CNN. Moreover, compared with the most existing EEG classiﬁcation research which focuses on binary classiﬁcation, our method works in multi-class scenario but still achieves a high-level of accuracy.

To demonstrate the advantage of our proposed hybrid model for better learning of robust features from raw EEG data, we also compare our method (joint RNN and CNN) with the independent deep feature learning method (RNN, CNN). All extracted features are classiﬁed by a XGBoost classiﬁer. The experimental results are listed in Table V, where we can see that our approach outperforms RNN and CNN in classiﬁcation accuracy by 3.38% and 11.44%, respectively. Our approach also achieves the lowest standard deviation and range, implying that it is more stable and reliable. Note that the RNN on its own (RNN works as both feature extract method and classiﬁer) without feature representation achieves a higher accuracy of 0.9325 (in Table IV) than the RNN+AE+XGBoost method (RNN works as feature extract method), which exhibits an accuracy of 0.9215. This shows that the RNN represented features are unsuitable for other classiﬁers and the inappropriate use of AE may decrease the signal quality.

TABLE IV PERFORMANCE COMPARISON WITH THE STATE OF THE ART METHODS. RF DENOTES RANDOM FOREST AND LDA DENOTES LINEAR DISCRIMINANT ANALYSIS.

#### Index Methods Binary/Multi Acc

State of the art

- 1 Almoari [2] Binary

0.7497

- 2 Sun [15] 0.65
- 3 Mohammad [16] 0.845
- 4 Major [19] 0.68
- 5 Shenoy [21] 0.8206
- 6 Tolic [17] 0.6821
- 7 Rashid [18] 0.92
- 8 Ward [22] Multi (3) 0.8
- 9 Sita [20] Multi (3) 0.8724
- 10 Pinheiro [1] Multi (4) 0.8505

Baselines

8 KNN

Multi (5)

0.8769

- 11 SVM 0.5082
- 12 RF 0.7739
- 13 LDA 0.5127
- 14 AdaBoost 0.3431
- 15 RNN 0.9325
- 16 CNN 0.8409
- 17 Ours 0.9553

Figure 3 illustrates separately the accuracy changes along with the training iterations under three categories of feature learning methods. Three curves (in Figure 3) show that the proposed joint method converges to its high accuracy in fewer iterations than independent RNN and CNN. The learned features are fed into the AE for further processing and ﬁnally classiﬁed by the XGBoost classiﬁer.

- C. Parameter Tuning

In this section, we conduct a series of empirical studies for analyzing the impact of various parameters on the classiﬁcation accuracy of the proposed approach. We extensively explore the impact of the following key factors: the training data size, the RNN learning rate, the CNN learning rate, the AE learning rate, the XGBoost learning rate, the AE hidden neuron size, and the classiﬁer. We next investigate the impact of varying the data used for training on the accuracy of our model. The results are illustrated in Figure 4. As expected, the accuracy increases as more data is available for training. Our method achieves an accuracy of 95% when 55% of the available data set is used for training. There is a only a marginal improvement in accuracy with the inclusion of additional training data. Also observe that we can achieve an accuracy of 87% with only 15% of training data. This indicates that our approach is less dependent on the training data size. The time required for training the model is shown on the right vertical axis in Figure 4 and as expected varies linearly with the size of the training data.

Figure 5(a) to Figure 5(d) show that the proposed approach performs differently under different learning rates in each component. We choose the appropriate learning rates as 0.005,

- 0.004, 0.002, and 0.5 for RNN, CNN, AE, and XGBoost, respectively. Figure 5(e) illustrates that the more hidden neurons in AE, the better classiﬁcation results. Therefore, we choose 800 neurons as a trade-off between the accuracy and efﬁciency. Figure 5(f) shows that the XGBoost classiﬁer outperforms other classiﬁers and achieves the highest classiﬁcation accuracy over the same features reﬁned by RNN+CNN+AE. It

should be noted that all the not mentioned hyper-parameters are set as default value except those shown in Table VI.

- D. Efﬁciency Analysis

Generally, deep learning algorithms require substantial time to execute. This can limit their suitability for BCI applications (e.g., typing) which typically require close to real-time performance. For instance, the practical deployment of a BCI system could be limited by its recognition time-delay if it takes two minutes to recognize the user’s intent. In this section, we will focus on the running time of our approach and compare it to the widely used baselines. The results are shown in Figure 6.

We ﬁrst illustrate the time required to train the model in Figure 6(a). Our model requires 2,000 seconds for training, which is signiﬁcantly longer than other baseline approaches. A breakdown of the training time required for the 3 components, namely, RNN, CNN and XGBoost is also shown. XGBoost requires the most training time as the result of its gradient boosting structure. However, training is a one-time operation. For practical considerations, the execution time of an algorithm during testing is what matters most. Figure 6(b) shows that the testing time of our approach is less than 1 second, which is similar with other baselines (except KNN which requires 9 seconds). In summary, the proposed approach takes very short testing time although it requires more time to train the model. Reducing the training time of our approach will be part of our future work.

- E. Adaptability Evaluation on Local EEG Dataset

To examine the adaptability and consistency of our model, we further evaluate our proposed model on a limited but easy-to-deploy dataset. We conduct the EEG collection by using a portable and easy-to-use commercialized EEG headset, Emotiv Epoc+ headset. The headset contains 14 channels and the sampling rate is 128 Hz. The local dataset can be accessed from this link6. Compared to the BCI 2000 system (64 channels) used for construct the eegmmidb dataset, our local equipment (Emotiv headset) only contains 14 channels and is much easier to be deployed in a natural environment.

- 1) Experimental Setting: This experiment is carried on

by 7 subjects (4 males and 3 females) aged from 23 to 26. During the experiment, the subject wearing the Emotiv Epoc+7 EEG collection headset, faces the computer screen and focuses on the corresponding hint which appears on the screen (shown in Figure 7). The brain activities and labels used in this paper are listed in Table II. In summary, this experiment contains 241,920 samples with 34,560 samples for each subject. In order to distinguish with the aforementioned eegmmidb dataset, we name this dataset as emotiv.

- 2) Recognition Results and Comparison: For each partici-

pant, the training set contains 25,920 samples and the testing set contains 8,640 samples. The experiment parameters are the same as listed in Table VI. The proposed approach achieves

- 6https://drive.google.com/open?id=0B9MuJb6Xx2PIM0otakxuVHpkWkk
- 7https://www.emotiv.com/product/emotiv-epoc-14-channel-mobile-eeg/

TABLE V THE RECOGNITION ACCURACY OF 10 SUBJECTS UNDER DIFFERENT FEATURE LEARNING METHODS. THE IMPROVEMENT REPRESENTS THE INCREASE AMPLITUDE OF OUR METHOD OVER THE MAXIMUM OF RNN AND CNN FEATURE LEARNING METHODS.

#### Feature learning S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 Range average std

RNN 0.9005 0.8928 0.9506 0.9264 0.9487 0.9427 0.9098 0.9293 0.9643 0.8498 0.1145 0.9215 0.0341 CNN 0.9021 0.5938 0.9395 0.9659 0.9013 0.9942 0.9273 0.6177 0.9310 0.6358 0.4004 0.8409 0.1580 RNN+CNN 0.9390 0.9186 0.9784 0.9736 0.9967 0.9832 0.9675 0.9245 0.9758 0.8954 0.1013 0.9553 0.0335 Improvement 0.0369 0.0258 0.0278 0.0077 0.0480 -0.0110 0.0402 -0.0048 0.0115 0.0456 0.0590 0.0228 0.0209

1

| | | | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |
| | | | | | | | | | | | | |

- class 0
- class 1
- class 2
- class 3
- class 4

0.95

0.9

0.85

TruePositiveRate

0.8

0.75

0.7

0.65

0.6

10 -3 10 -2 10 -1 10 0

log(False Positive Rate)

1

| |
|---|
| |
| |
| |
| |
| |
| |
| |

0.9

0.8

0.7

Accuracy

0.6

0.5

Joint RNN CNN

0.4

0.3

0.2

0 500 1000 1500 2000 2500

The number of iterations

1200

0.96

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

0.95

1100

0.94

1000

0.93

900

Trainingtime(s)

0.92

800

Accuracy

0.91

700

0.9

600

0.89

500

0.88

400

0.87

300

0.86

200

10 20 30 40 50 60 70 80 90 100

The training data proportion

- Fig. 2. The ROC curves of the 5-class classiﬁcation. Note that X-axis is the logarithmic of the False Positive Rate.

Fig. 3. The relationship between the testing accuracy and the number of iterations.

### Fig. 4. The relationship between the classiﬁcation accuracy and the training data proportion.

0.95

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

0.9

Accuracy

0.85

0.8

0.75

0 0.005 0.01 0.015 0.02 0.025

RNN learning rate

(a) RNN learning rate

0.95

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

0.9

Accuracy

0.85

0.8

0.75

0 0.005 0.01 0.015 0.02 0.025 0.03 0.035 0.04 0.045 0.05

CNN learning rate

### (b) CNN learning rate

0.97

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

0.965

0.96

0.955

Accuracy

0.95

0.945

0.94

0.935

0 0.02 0.04 0.06 0.08 0.1 0.12 0.14 0.16 0.18 0.2

AE learning rate

(c) AE learning rate

0.966

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

0.964

0.962

Accuracy

0.96

0.958

0.956

0.954

0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

XGBoost learning rate

### (d) XGBoost learning rate

1

0.955

| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

0.95

0.9

0.945

0.8

0.94

0.7

Accuracy

Accuracy

0.935

0.6

0.93

0.5

0.925

0.4

0.92

0.3

0.915

0.2

0.91

KNN SVM RF LDA AdaBoost RNN CNN XGBoost

0 200 400 600 800 1000 1200 1400 1600

AE hidden neuron size

### (f) Classiﬁer Fig. 5. The classiﬁcation accuracy with different hyper-parameter settings

(e) AE hidden neuron size

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

2500

RNN CNN XGBoost

2000

Trainingtime(s)

Testingtime(s)

1500

1000

500

0

KNN SVM RF LDA AdaBoost RNN CNN Ours

KNN SVM RF LDA AdaBoost RNN CNN Ours

(b) Testing time Fig. 6. The training time and testing time comparison

(a) Training time

TABLE VI HYPER-PARAMETER SETTING. FOR INSTANCE, RNN CONTAINS ONE INPUT LAYER (64 NEURONS), 5 HIDDEN LAYERS (64 NEURONS EACH LAYER), AND ONE OUTPUT LAYER (5 NEURONS).

Hyper-parameter Value Layer 7=1+5+1 Neuron size 64*1+64*5+5*1 Iterations 2500 Batch size 7000 Learning rate 0.005 Activation function Soft-max Cost function Cross entropy

RNN

Regularization 2 norm (λ = 0.004) Layer 8 Input neuron size 64 1st convolutional Filter [1,1],stride [1,1], depth 2 1st pooling Window [1,2], stride [1,2] 2nd convolutional Filter [1,2],stride [1,1], depth 4 2nd pooling Window [1,2], stride [1,2] Padding method Zero-padding Pooling methods Max Activation function ReLU 1st fully connected 64 2nd fully connected 120 Output neuron size 5 Iterations 2500 Batch size 7000 Learning rate 0.004 Activation function Softmax Cost function Cross entropy

CNN

Regularization 2 norm (λ = 0.001) Layer 1+1+1 Neuron size 184+800+184 Iterations 400 Learning rate 0.01

AE

Cost function MSE Objective Multi:softmax Learning rate 0.5 max depth 6

Classiﬁer

Iterations 500

the 5-class classiﬁcation accuracy of 0.9427. The confusion matrix and evaluation is reported in Table VII.

Subsequently, to demonstrate the efﬁciency of the proposed approach, we compare our method with the state-of-the-art methods and report the accuracy and testing time in Figure 8.

To conclude, our model still achieves good performance with EEG signals collected from hardware with fewer channels

[Figure 42]

[Figure 43]

(a) EEG collection (b) EEG raw data

Fig. 7. EEG collection and the raw data. The emotiv dataset only consists of the imagination task data since the rest state data is contaminated by eye blink and other noises.

TABLE VII THE CONFUSION MATRIX AND THE EVALUATION OVER emotiv DATASET

Ground truth Evaluation

0 1 2 3 4 Precision Recall F1 AUC

- 0 1608 35 51 21 18 0.9279 0.9415 0.9346 0.9982

- 1 18 1602 21 29 15 0.9507 0.9357 0.9432 0.9977

- 2 29 31 1642 27 22 0.9377 0.9437 0.9407 0.9990

- 3 19 25 11 1615 36 0.9467 0.9428 0.9447 0.9990

Predicted Label

- 4 34 19 15 21 1676 0.9496 0.9485 0.9490 0.9987

Total 1708 1712 1740 1713 1767 4.7126 4.7122 4.7123 4.9926 Average 0.9425 0.9424 0.9425 0.9985

- 10 0
- 10 1

- 0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

- 1

Testingtime(s)

Accuracy

10 -1

10 -2

10 -3

SVM RF KNN LDA AdaBoost CNN RNN Ours

SVM RF KNN LDA AdaBoost CNN RNN ours

(b) Testing time Fig. 8. The accuracy and testing time comparison over emotiv dataset

(a) Accuracy

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

- Fig. 9. Overview of the brain typing system. The user’s typing intent is collected by headset and sent to the server through client 1. The server uses the pre-trained deep leaning model to recognize the intent, which is used to control the typing interface through client 2. The server and clients are connected using TCP connections.

and in a more natural setting. V. APPLICATION: BRAIN TYPING SYSTEM

Based on the high EEG signals classiﬁcation accuracy of the proposed deep learning approach, in this section, we develop an online brain typing system to convert user’s thoughts to texts.

The brain typing system (as shown in Figure 9) consists of two components: the pre-trained deep learning model and the online BCI system. The pre-trained deep learning model, which

is trained ofﬂine, aims to accurately and recognize the user’s typing intent in real time. This model (introduced in detail in Section III) is central to the operation of the brain typing system, and is the main contribution of this paper. The online system contains 5 components: the EEG headset, the client 1 (data collector), the server, the client 2 (typing command receiver), and the typing interface.

The user wears the Emotiv EPOC+ headset (introduced in Section IV-E) which collects EEG signals and sends the data to client 1 through a bluetooth connection. The raw EEG signals are transported to the server through a TCP connection. The server feeds the incoming EEG signals to the pre-trained deep learning model. The model produces a classiﬁcation decision and converts it to the corresponding typing command which is sent to client 2 through a TCP connection. The typing interface receives the command and manifests the appropriate typing action.

Speciﬁcally, the typing interface (Figure 10) can be divided into three levels: the initial interface, the sub-interface, and the bottom interface. All the interfaces have similar structure: three character blocks (separately distributed in left, up, and down directions), a display block, and a cancel button. The display block shows the typed output and the cancel button is used to cancel the last operation. All interfaces include the display block and cancel button but differ in character blocks. The typing system totally includes 27 = 3∗9 characters (26 English alphabets and the space bar) and all of them are separated by 3 character blocks (each block contains 9 characters) in the initial interface. Overall, there are 3 alternative selections and each selection will lead to a speciﬁc sub-interface which contains 9 characters. Again, the 9 = 3 ∗ 3 characters are divided into 3 character blocks and each of them is connected to a bottom interface. In the bottom interface, each block represents only one character. As an example, Figure 10 shows the procedure to type the character ‘I’.

In the brain typing system, there are 5 commands to control the interface: ‘left’, ‘up’, ‘right’, ‘cancel’, and ‘conﬁrm’. Each command corresponds to a speciﬁc motor imagery EEG category (as shown in Table II). To type each single character, the interface is supposed to accept 6 commands. Consider typing the letter ‘I’ as an example (see Figure 10). The sequence of commands to be entered is as follows: ‘left’, ‘conﬁrm’, ‘right’, ‘conﬁrm’, ‘right’, ‘conﬁrm’. In our practical deployment, the sampling rate of Emotiv EPOC+ headset is set as 128Hz, which means the server can receive 128 EEG recordings each second. Since the brainwave signal varies rapidly and is very easy to be affected by noises, the EEG data stream is sent to server each half second, which means that the server receives 64 EEG samples each time. The 64 EEG samples are classiﬁed by the deep learning framework and generates 64 categories of intents. we calculate the mode of 64 intents and regard the mode as the ﬁnal intent decision. Furthermore, to achieve steadiness and reliability, the server sends command to client 2 only if three consecutive decisions remain consistent. After the command is sent, the command list will be reset and the system will wait until 3 consistent

[Figure 50]

[Figure 51]

[Figure 52]

- Fig. 10. The brain typing procedure to type the character ‘I’. Firstly, select the left character block (contains ‘ABCDEFGHI’ characters) in the initial interface and then conﬁrm the selection to step in the corresponding subinterface; then, select the right character block (contains ‘GHI’ characters) in the sub-interface and conﬁrm to jump to the bottom interface; at last, select the right character block (only contains ‘I’) and the character ‘I’ will appear in the display block after the conﬁrmation.

decisions are made. Therefore, client 2 must wait for at least

- 1.5 seconds for a command and the entire process of typing each character takes at least 9 (6∗1.5) seconds. In other words, theoretically, the proposed brain typing system can achieve the highest typing speed of 6.67 = 60/9 characters per minute.

VI. DISCUSION

The proposed deep learning framework achieves the highest accuracy compared to the state-of-the-art EEG classiﬁcation methods. The classiﬁcation accuracy of the public dataset (eegmmidb) is consistently higher than the local real-world dataset (emotiv). The possible reason may be due to the different channels of two datasets (eegmmidb contains 64 channels and emotiv only takes 14 channels). In general, our framework can achieve high classiﬁcation accuracy with both datasets.

The accuracy in the online mode is however lower than what can be achieved in an ofﬂine setting (over 95%), which could be attributed to a number of reasons. At ﬁrst, the user’s mental state and ﬂuctuations in emotions may affect the quality of the EEG signals. For example, if the ofﬂine dataset used to train the deep learning model is collected when the user is in an excited emotion state but then applied in an online setting when the user is upset, would lead to low accuracy. In addition, subtle variations in the way the EEG headset is mounted on the subject’s head may also impact online decision making. Speciﬁcally, the position of each of the electrodes (e.g.. the 14 electrodes in the Emotiv headset) on the scalp may vary during training and testing. Moreover, the EEG signals vary from person to person, which makes it difﬁcult to construct a common model that applies to all individuals. One of our future work is to identify the intra-class variabilities shared by all the activities of different subjects. Last but not least, some limitations are caused by the intrinsic attributes of the headset. For instance, the headset used in our case study is too tight for the user to wear longer than 30 minutes and the conductive quality of the wet electrodes decreases after prolonged usage.

VII. RELATED WORK

In EEG decoding and interpretation area, there are mainly two research directions: the EEG feature representation and the EEG classiﬁer.

Effectively representing features from EEG raw data is critical for the classiﬁcation accuracy for the complexity and high dimensionality of EEG signals. Vzard et al. [23] employ

common spatial pattern (CSP) along with LDA to pre-process the EEG data and obtain an accuracy of 71.59% to binary alertness states. The autoregressive (AR) modeling approach, a widely used algorithm for EEG feature extraction, is also broadly combined with other feature extraction techniques to gain a better performance [24], [25]. Duan et al. [26] introduce the Autoencoder method for feature extraction and ﬁnally obtain a classiﬁcation accuracy of 86.69%. Wavelet analysis [27] is employed to carry on a diagnosis of Traumatic Brain Injury (TBI) by quantitative EEG (qEEG) data and reaches 87.85% accuracy. Power spectral density [28] is extracted as EEG data features to input into SVM. The work achieves 76% accuracy with the data from FC4 ∼ AF8 channels and 92% with the data from CPz ∼ CP2 channels.

Recently, more and more studies exploit deep learning [29], [30] to classify EEG signals. The work in [31] builds one deep belief net (DBN) classiﬁer and achieves the accuracy of 83% on binary classiﬁcation. The algorithm combined CNN and stacked Autoencoder (SAE) is investigated in [32] to classify EEG Motor Imagery signals and results in 90% accuracy.

Based on the EEG signal decoding, a few researches start to explore the non-invasive brain typing method. The approach in

- [33] enables ALS patients to type through BCI and achieves the typing rate of 6 characters per minute. The authors in
- [34] investigate three kinds of typing interfaces and illustrates that both matrix presentation and RSVP (rapid serial visual presentation) can work well.

VIII. CONCLUSION AND FUTUREWORK

In this paper, we present a hybrid deep learning model to decode the raw EEG signals for the aim of converting the user’s thoughts to texts. The model employs the RNN and CNN to learn the temporal and spatial dependency features from the input EEG raw data and then stack them together. Our proposed approach adopts an Autoencoder to recognize the stacked feature and to eliminate the artifacts and employs the XGBoost classiﬁer for the intent recognition. We evaluate our approach on a public MI-EEG dataset and also a real world dataset collected by ourselves. Both results (95.53% and 94.27%) outperform the state-of-the-art methods.

Our future work will focus on improving the accuracy in the person-independent scenario, wherein some subjects participate in the training and the rest of subjects involve in the testing. Our recent study on human activity recognition atop multi-task learning based framework [35] shows the capability to capture certain underlying local commonalities under the intra-class variabilities shared by all the activities of different subjects.

REFERENCES

- [1] O. R. Pinheiro, L. R. Alves, M. Romero, and J. R. de Souza, “Wheelchair simulator game for training people with severe disabilities,” in Technology and Innovation in Sports, Health and Wellbeing (TISHW), International Conference on. IEEE, 2016.
- [2] M. H. Alomari, A. Abubaker, A. Turani, A. M. Baniyounes, and A. Manasreh, “EEG Mouse : A Machine Learning-Based Brain Computer Interface,” vol. 5, no. 4, pp. 193–198, 2014.

- [3] T. Nguyen, S. Nahavandi, A. Khosravi, D. Creighton, and I. Hettiarachchi, “Eeg signal analysis for bci application using fuzzy system,” in Neural Networks (IJCNN), 2015 International Joint Conference on. IEEE, 2015, pp. 1–8.
- [4] E. Niedermeyer and F. L. da Silva, Electroencephalography: basic principles, clinical applications, and related ﬁelds, 2005.
- [5] F. Akram, S. M. Han, and T.-S. Kim, “An efﬁcient word typing p300bci system using a modiﬁed t9 interface and random forest classiﬁer,” Computers in biology and medicine, vol. 56, pp. 30–36, 2015.
- [6] G. Repovs, “Dealing with noise in eeg recording and data analysis,” in Informatica Medica Slovenica, vol. 15, no. 1, 2010, pp. 18–25.
- [7] H. Sak, A. W. Senior, and F. Beaufays, “Long short-term memory recurrent neural network architectures for large scale acoustic modeling.” in Interspeech, 2014.
- [8] T. Mikolov, M. Karaﬁ´at, L. Burget, J. Cernock`y, and S. Khudanpur, “Recurrent neural network based language model.” in Interspeech, vol. 2, 2010, p. 3.
- [9] W. Zaremba, I. Sutskever, and O. Vinyals, “Recurrent neural network regularization,” arXiv preprint arXiv:1409.2329, 2014.
- [10] D. Kingma and J. Ba, “Adam: A method for stochastic optimization,” arXiv preprint arXiv:1412.6980, 2014.
- [11] J. Nagi, F. Ducatelle, G. A. Di Caro, D. Cire¸san, U. Meier, A. Giusti, F. Nagi, J. Schmidhuber, and L. M. Gambardella, “Max-pooling convolutional neural networks for vision-based hand gesture recognition,” in Signal and Image Processing Applications (ICSIPA), 2011 IEEE International Conference on. IEEE, 2011, pp. 342–347.
- [12] G. Hinton, N. Srivastava, and K. Swersky, “Rmsprop: Divide the gradient by a running average of its recent magnitude,” Neural networks for machine learning, Coursera lecture 6e, 2012.
- [13] T. Chen and C. Guestrin, “Xgboost: A scalable tree boosting system,” in Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. ACM, 2016.
- [14] G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw, “Bci2000: a general-purpose brain-computer interface (bci) system,” IEEE Transactions on biomedical engineering, vol. 51, no. 6, pp. 1034–1043, 2004.
- [15] L. Sun et al., “Classiﬁcation of imagery motor eeg data with wavelet denoising and features selection,” in Wavelet Analysis and Pattern Recognition (ICWAPR), 2016 International Conference on, 2016.
- [16] M. H. Alomari, A. M. Baniyounes, and E. A. Awada, “Eeg-based classiﬁcation of imagined ﬁsts movements using machine learning and wavelet transform analysis,” 2014.
- [17] M. Toli´c and F. Jovi´c, “Classiﬁcation of wavelet transformed eeg signals with neural network for imagined mental and motor tasks,” Kineziologija, vol. 45, no. 1, pp. 130–138, 2013.
- [18] M. M. or Rashid and M. Ahmad, “Classiﬁcation of motor imagery hands movement using levenberg-marquardt algorithm based on statistical features of eeg signal,” in Electrical Engineering and Information Communication Technology (ICEEICT), 2016 3rd International Conference on. IEEE, 2016, pp. 1–6.
- [19] T. C. Major and J. M. Conrad, “The effects of pre-ﬁltering and individualizing components for electroencephalography neural network classiﬁcation,” in SoutheastCon, 2017. IEEE, 2017.
- [20] J. Sita and G. Nair, “Feature extraction and classiﬁcation of eeg signals for mapping motor area of the brain,” in Control Communication and

- Computing (ICCC), 2013 International Conference on. IEEE, 2013, pp. 463–468.
- [21] H. V. Shenoy, A. Vinod, and C. Guan, “Shrinkage estimator based regularization for eeg motor imagery classiﬁcation,” in Information, Communications and Signal Processing (ICICS), 2015 10th International Conference on. IEEE, 2015.
- [22] C. R. Ward, J. Picone, and I. Obeid, “Applications of UBMs and IVectors in EEG Subject Veriﬁcation,” 2016 IEEE 38th Annual International Conference of the Engineering in Medicine and Biology Society (EMBC), pp. 748–751, 2016.
- [23] L. V´ezard, P. Legrand, M. Chavent, F. Fa¨ıta-A¨ınseba, and L. Trujillo, “Eeg classiﬁcation for the detection of mental states,” Applied Soft Computing, vol. 32, pp. 113–131, 2015.
- [24] M. Rahman, W. Ma, D. Tran, and J. Campbell, “A comprehensive survey of the feature extraction methods in the eeg research,” Algorithms and architectures for parallel processing, pp. 274–283, 2012.
- [25] Y. Zhang, B. Liu, X. Ji, and D. Huang, “Classiﬁcation of eeg signals based on autoregressive model and wavelet packet decomposition,” Neural Processing Letters, pp. 1–14, 2016.
- [26] L. Duan, Y. Xu, S. Cui, J. Chen, and M. Bao, “Feature extraction of motor imagery eeg based on extreme learning machine auto-encoder,” in Proceedings of ELM-2015 volume 1, 2016, pp. 361–370.
- [27] B. Albert, J. Zhang, A. Noyvirt, R. Setchi, H. Sjaaheim, S. Velikova, and F. Strisland, “Automatic eeg processing for the early diagnosis of traumatic brain injury,” in World Automation Congress (WAC), 2016.
- [28] A. M. Al-Kaysi, A. Al-Ani, C. K. Loo, T. Y. Powell, D. M. Martin, M. Breakspear, and T. W. Boonstra, “Predicting tdcs treatment outcomes of patients with major depressive disorder using automated eeg classiﬁcation,” Journal of Affective Disorders, vol. 208, pp. 597–603, 2017.
- [29] S. Jirayucharoensak, S. Pan-Ngum, and P. Israsena, “Eeg-based emotion recognition using deep learning network with principal component based covariate shift adaptation,” The Scientiﬁc World Journal, vol. 2014, 2014.
- [30] Y. Ren and Y. Wu, “Convolutional deep belief networks for feature extraction of eeg signal,” in Neural Networks (IJCNN), 2014 International Joint Conference on. IEEE, 2014, pp. 2850–2853.
- [31] X. An, D. P. Kuang, X. J. Guo, Y. L. Zhao, and L. H. He, “A Deep Learning Method for Classiﬁcation of EEG Data Based on Motor Imagery,” Intelligent Computing in Bioinformatics, vol. 8590, pp. 203– 210, 2014.
- [32] Y. R. Tabar and U. Halici, “A novel deep learning approach for classiﬁcation of eeg motor imagery signals,” Journal of neural engineering, vol. 14, no. 1, p. 016003, 2016.
- [33] W. Speier, N. Chandravadia, D. Roberts, S. Pendekanti, and N. Pouratian, “Online bci typing using language model classiﬁers by als patients in their homes,” Brain-Computer Interfaces, vol. 4, no. 1-2, pp. 114–121, 2017.
- [34] M. Moghadamfalahi, U. Orhan, M. Akcakaya, H. Nezamfar, M. FriedOken, and D. Erdogmus, “Language-model assisted brain computer interface for typing: A comparison of matrix and rapid serial visual presentation,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 23, no. 5, pp. 910–920, 2015.
- [35] L. Yao, F. Nie, Q. Z. Sheng, T. Gu, X. Li, and S. Wang, “Learning from less for better: semi-supervised activity recognition via shared structure discovery,” in Proceedings of the 2016 ACM International Joint Conference on Pervasive and Ubiquitous Computing. ACM, 2016.

