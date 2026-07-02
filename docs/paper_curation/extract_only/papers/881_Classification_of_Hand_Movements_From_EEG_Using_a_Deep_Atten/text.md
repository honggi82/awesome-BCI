# Classiﬁcation of Hand Movements from EEG using a Deep Attention-based LSTM Network

Guangyi Zhang, Student Member, IEEE Vandad Davoodnia, Student Member, IEEE, Alireza Sepas-Moghaddam, Yaoxue Zhang, Senior Member, IEEE, and Ali Etemad, Member, IEEE

## arXiv:1908.02252v2[cs.LG]31Oct2019

Abstract—Classifying limb movements using brain activity is an important task in Brain-computer Interfaces (BCI) that has been successfully used in multiple application domains, ranging from human-computer interaction to medical and biomedical applications. This paper proposes a novel solution for classiﬁcation of left/right hand movement by exploiting a Long Short-Term Memory (LSTM) network with attention mechanism to learn the electroencephalogram (EEG) time-series information. To this end, a wide range of time and frequency domain features are extracted from the EEG signals and used to train an LSTM network to perform the classiﬁcation task. We conduct extensive experiments with the EEG Movement dataset and show that our proposed solution our method achieves improvements over several benchmarks and state-of-the-art methods in both intrasubject and cross-subject validation schemes. Moreover, we utilize the proposed framework to analyze the information as received by the sensors and monitor the activated regions of the brain by tracking EEG topography throughout the experiments.

Index Terms—Brain-Computer Interfaces, Electroencephalogram, Deep Learning, Long Short-Term Memory, Attention Mechanism.

I. INTRODUCTION

Electroencephalogram (EEG) records electrical signals from the brain, thus providing the ability to extract valuable information regarding brain activity. EEG-based Brain-Computer Interfaces (BCI) have been widely used in medical and biomedical applications such as analyzing mental workload and fatigue [1], diagnosing brain tumors [2], and rehabilitation of central nervous system disorders [3]. BCI can also help communicate brain commands and enable the control of artiﬁcial limbs [4], especially for people suffering from amyotrophic lateral sclerosis brainstem stroke, brain or spinal injury, cerebreal palsy, muscular dystrophies, and other diseases impairing the control and feedback system between brain and muscles.

In recent years, EEG-based movement analysis and classiﬁcation have been widely used in various applications, ranging from clinical applications to brain-machine interface and robotics. For example, stroke patients are often asked to make several body movements in response to various visual or electrical stimuli, which allows researchers to monitor the progress of the recovery of the patient’s brain injury by

G. Zhang, V. Davoodnia, A. Sepas-Moghaddam and A. Etemad are with the Department of Electrical and Computer Engineering, Queen’s University, Kingston, ON, Canada (e-mail: guangyi.zhang@queensu.ca, vandad.davoodnia@queensu.ca, alireza.sepasmoghaddam@queensu.ca ali.etemad@queensu.ca).

Y. Zhang is with the Department of Computer Science and Technology, Tsinghua University, Beijing, China. (e-mail: zyx@mail.tsinghua.edu.cn).

analyzing EEG signals [5]. Additionally, such technologies allow for patients with disabilities to control the movements of artiﬁcial limbs or exoskeletons. In particular, in order to perform everyday tasks, the control of hand movements is of critical importance for patients [6].

To tackle the problem of BCI for hand-movement control, a number of solutions have been proposed in the literature [7]– [9]. Generally, two approaches can be used for development of automated methods for BCI, including hand-movement classiﬁcation from EEG. In the ﬁrst approach, the system is trained and/or calibrated on the intended user and then used for BCI applications for that same user (intra-subject). While this approach is effective, it does not result in a generalized off-the-shelf solution for a population of patients. The second approach is to develop a generalized solution that performs across subjects once trained with a dataset (cross-subject). While the latter approach is more desired and convenient, it tends to show lower accuracies, typically below the standards required to employ such systems in real products and solutions.

In this paper, a deep learning solution for Left/Right (L/R) hand movement classiﬁcation using an LSTM network with attention mechanism is proposed. Our proposed method includes three main steps: i) data pre-processing is performed to reduce the negative effects of signal artifacts, including cross-talk, noise, and power-line interference; ii) time and frequency domain features are extracted from EEG, to then be used as inputs to the LSTM input layer; and iii) an attentionbased LSTM network is designed to learn the importance of EEG information varying through time, where discriminative information with higher importance are assigned higher scores to better contribute to the classiﬁcation performance. The architecture of our proposed solution exploits both long and short-term dependencies within the feature manifold. To evaluate the performance and robustness of our solution, we utilize both intra-subject and cross-subject validation schemes in L/R classiﬁcation experiments. The experimental results are compared with a number of benchmarks as well as the stateof-the-art.

Our contributions are as follows: i) The proposed deep model, which has been trained over all the available data (103 subjects) using a 10-fold cross-subject validation scheme, signiﬁcantly outperforms the state-of-the-art solutions for hand movement classiﬁcation. ii) In order to compare our work to previous studies utilizing the same dataset, we also perform intra-subject classiﬁcation (using the same network) for each of the 103 subjects separately, and achieve very high accuracies, outperforming previous studies. iii) Lastly, we perform a

detailed analysis of brain activity through the different stages of stimuli perception and hand movement, and demonstrate that EEG information ﬂow through the senor pairs are in correspondence with the known and expected neurological function of the brain.

II. RELATED WORK

The majority of the related work on hand movement classiﬁcation has focused on intra-subject validation. Employing this approach often stems from the fact that distinguishing between L/R hand movements can be a challenging task due to the highly subject-dependant nature of brain activities in the visual and motor cortex. Several conventional machine learning methods have been employed using this approach, for instance, in [10], an average accuracy of 64.02% was reported using a Common Spatial Patterns (CSP) approach for 10 subjects. In [11], an average accuracy of 88.69% was reported using QDA, while a rough set-based classiﬁer was used in [12] and [13], reporting average accuracies of 60% and 68% respectively. However, the aforementioned traditional classiﬁers often cannot model the non-linearities observed in high-dimensional multi-channel EEG and featuresets extracted from the data. This especially becomes an issue when attempting to model cross-subject relationships within the dataset.

Training a single model capable of learning to classify hand movements from EEG and generalizing the learned input-output relationships to the entire dataset (cross-subject) is quite challenging. The results presented in [14] showed that the average accuracy dropped from 87% to chance level (50%), when utilizing a cross-subject scheme instead of an intra-subject one, using the proposed Maximum Discernibility Algorithm (MDA). Moreover, a large-scale synchronization analysis using Phase Locking Value (PLV) in [15], deﬁned a criteria that could successfully distinguish between L/R hand movement and obtained an average accuracy of 78.95%. Other than conventional machine learning classiﬁers and statistic analysis, deep learning techniques have been employed for this task. For instance, in one of the few deep learning solutions, a set of time and frequency domain features were extracted and fed to an Artiﬁcial Neural Network (ANN) [16], achieving an accuracy of 68%.

In addition to the task of hand movement classiﬁcation, the task of imagery classiﬁcation focuses on mental activity when imagining left and right hand movements as opposed to physically performing them. In this context, several classical machine learning methods such as Logistic Regression [17], k-Nearest Neighbor (kNN) [18], and Na¨ıve Bayes (NB) [18] have been used with intra-subject validation. In addition to classical machine learning methods, several deep learning solutions have also been utilized. For example, in [19], [20], a Convolutional Neural Network (CNN) was used. An LSTMbased model was proposed in [21], outperforming the stateof-the-art solutions including methods based on other deep networks. In cross-subject validation, a very high accuracy was achieved using a parallel or cascade combination of CNN and LSTM networks [22]. It should be mentioned that the imagery

EEG classiﬁcation naturally uses a dataset separate from the movement dataset, and hence, a direct comparison between the two tasks is not valid. However, a review of the methods used for imagery classiﬁcation can provide further inspiration for new solutions for movement classiﬁcation.

Table I summarizes the main works in the area and characteristics of the proposed solutions in terms of method and classiﬁcation tasks. The table also includes information about the datasets and validation protocols and schemes considered by these methods for performance assessment. The solutions are sorted according to their publication date. For comparison, the characteristics of our method proposed in this paper are also included in Table I. The Table points to two clear areas in the literature that merit additional investigation and research:

‚ First, most of the works have performed intra-subject validation, while the more challenging task of crosssubject validation (which is also more indicative of generalization) has been largely disregarded.

‚ Second, most of the prior works have utilized classical machine learning models, indicating room for improvement using more advanced deep learning techniques.

III. PROPOSED METHOD

In this section, we present the proposed method, including the pre-processing steps, feature extraction, and the deep learning solution. In the rest of this paper, the description of notations used is as follow: ‘a’ represents a scalar, ‘a’ represents a vector, ‘A’ represents a matrix.

- A. Pre-processing

Data pre-processing was performed to reduce the negative effects of signal artifacts, including cross-talk, noise, and power-line interference. In this context, out of the 64 EEG channels available in the EEG test material, the 10 central sensors were discarded due to their non-symmetric nature [23]. The utilized sensor pairs were selected based on the topology described in [23]. Then, two ﬁlters were applied to the new 27 differential EEG channels: a notch ﬁlter removed 50 Hz power line interference and a band-pass ﬁlter was applied to allow a frequency range of 0.5 ´ 70 Hz to pass through, thus minimizing artifacts such as noise often present in this frequency range [24]. Normalization of EEG amplitude was then carried out as the last step to minimize the difference in EEG amplitudes using min-max normalization with across different subjects.

- B. Time and Frequency Domain Feature Extraction

Successive to pre-processing, a number of time and frequency domain features were extracted in order to be used as inputs for the proposed method. EEG is known as a nonstationary time-series signal where nonlinear features are often used for representation and classiﬁcation tasks. Feature extraction was performed on a 2-second segments for each trial. The effect of different segment sizes on the performance of hand movement classiﬁcation task will be studied in Section 5. Time and frequency domain features were subsequently extracted from each time-step. Time-domain features included: i) mean,

TABLE I THE MAIN CHARACTERISTICS OF THE RELATED WORK

1) M-EEG DENOTES PHYSICAL LEFT/RIGHT HAND MOVEMENTS, WHILE IM-EEG DENOTES IMAGERY LEFT/RIGHT HAND MOVEMENTS IN THE PHYSIONET EEG MOTOR MOVEMENT/IMAGERY DATASET; 2) BCI Comp DENOTES THE IMAGERY DATASET USED IN THE BCI COMPETITION; 3) Comp-IV.2a AND Comp-IV.2b DENOTE DATASET 2A AND DATASET 2B OF THE BCI COMPETITION IV, RESPECTIVELY; 4) Comp-II.III DENOTES DATASET III IN THE BCI COMPETITION II.

Method

Validation Type Selection (No. of Subjects) Scheme

Feature

Validation Protocol

Ref. Year

Method

Task Dataset

- [17] 2007 Classical LR No Imagery BCI Comp Intra-Sub (29) 50:50 Split
- [18] 2011 Classical KNN, NB Yes Imagery BCI Comp-II.III Intra-Sub (1) 50:50 Split

- [10] 2012 Classical CSP No Movement M-EEG Intra-Sub (10) 3-Fold

- [15] 2014 Classical PLV No Movement M-EEG Cross-Sub (103) N/A

[11] 2015 Classical QDA No Movement M-EEG Intra-Sub (103) N/A

- [20] 2015 Deep CNN+SAE No Imagery BCI Comp-IV.2b Intra-Sub (9) 10 ˆ 10-Fold

[12] 2016 Classical Rought set No Movement M-EEG Intra-Sub (106) 50:50 Split [19] 2017 Deep CNN No Imagery N/A Intra-Sub (2) 80:20 Split [22] 2017 Deep CNN+LSTM No Imagery IM-EEG Cross-Sub (108) 75:25 Split [14] 2017 Classical MDA No Movement M-EEG Intra-Sub (106) 65:35 Split [16] 2017 Deep ANN No Movement M-EEG Cross-Sub (109) 10-Fold [13] 2018 Classical Rough set No Movement M-EEG Intra-Sub (106) 65:35 Split

- [21] 2018 Deep LSTM No Imagery BCI Comp-IV.2a Intra-Sub (9) 5 ˆ 5-Fold Ours 2019 Deep LSTM+Attention No Movement M-EEG Intra-Sub (103) 10-Fold Ours 2019 Deep LSTM+Attention No Movement M-EEG Cross-Sub (103) 10-Fold

TABLE II TIME AND FREQUENCY DOMAIN FEATURES Method Formula

ÿN

1 N

Mean µ “

xi

i“1

ÿN

1 N

pxi ´ µq2

Variance σ2 “

i“1

ÿN

1 N

pxi ´ µq3

i“1

Skewness S “

ÿN

1 N ´ 1

pxi ´ µq2q3{2

p

i“1

ÿN

1 N

pxi ´ µq4

i“1

Kurtosis K “

´ 3

ÿN

1 N

pxi ´ µq2q2

p

i“1

Nÿ´1

Zero-crossing zc “

1IRă0pxixi´1q Absolute area under signal simps “ ż b

i“1

|fpxq|dx

a

Peak to Peak pk2pk “ maxpxq ´ minpxq Amplitude spectrum density Xˆpωq “

ż T

1 ?

xptq exp´iωt dt Power spectrum density Sxxpωq “ lim

T

E”|Xˆpωq|2ı power of each frequency band P “

0

TÑ8

ż ω2

1 π

Sxxpωqdω

ω1

ii) variance, iii) skewness, iv) kurtosis, v) zero crossings, vi) absolute area under the signal, and vii) peak-to-peak distance. Extracted frequency-domain features consisted of relative band power in four frequency bands, notably i) delta (0.5´4 Hz), ii) theta (4´8 Hz), iii) alpha (8´12 Hz), and iv) beta (12´30 Hz). Table II presents the mathematical equations for these features, where a total of 297 features (27 channels ˆ 11 features per channel) were extracted from each time-step.

C. Proposed Deep Learning Solution

To detect and classify very subtle spatio-temporal changes in our feature space that correspond to the intended movements,

a solution capable of remembering and eventually aggregating these transitions across the dataset is required. Addressing both these requirements formed the intuition behind our proposed solution of using an LSTM network with the attention mechanism. LSTM has been widely utilized for learning and classifying time-series data including bio-signals [22], [25]. Moreover, recent studies have successfully used LSTM architectures for EEG analysis given the time-dependant nature of these signals [21]. Furthermore, attention-based LSTM has been used in other tasks requiring remembering and aggregation of feature embeddings, notably natural language processing (NLP) [26], [27]. In the ﬁeld of NLP, the importance of different words vary depending on context and role in the sentence. Similarly, the importance of information obtained in time-steps of EEG signals are also discrepant and task-dependent. Thus we believe the attention-based LSTM architecture can improve classiﬁcation performance using EEG signals by focusing on essential task-relevant features from different time-steps. In the following subsection we describe the architecture of an LSTM cell as well as the attention mechanism.

1) LSTM Network: RNNs can be used to extract higher dimensional dependencies from sequential data such as EEG time-series [28]. RNN units have connections not only between the subsequent layers, but also among themselves to capture information from previous inputs. Traditional RNNs can easily learn short-term dependencies; however, they have difﬁculties in learning long-term dynamics due to the vanishing and exploding gradient problems. LSTM is a type of RNN that addresses the vanishing and exploding gradient problems by learning both long- and short-term dependencies [29].

An LSTM network is composed of cells, whose outputs evolve through the network based on past memory content. The cells have a common cell state, keeping long-term dependencies along the entire LSTM chain of cells. The ﬂow of information is then controlled by the input gate (it) and forget gate (ft), thus allowing the network to decide whether to forget the previous state (Ct´1) or update the current state (Ct) with new information. The output of each cell (hidden state) is controlled by an output gate (ot), allowing the cell to

[Figure 1]

Output

[Figure 2]

[Figure 3]

[Figure 4]

Ct-1 Ct

Dense (sigmoid)

[Figure 5]

[Figure 6]

[Figure 7]

### +

×

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

+

Attention Mechanism

[Figure 15]

tanh

[Figure 16]

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

α1 α2 α3 αt

×

ƒt

h1 h2 h3 ht

[Figure 22]

[Figure 23]

[Figure 24]

×

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

LSTM LSTM LSTM LSTM

[Figure 33]

[Figure 34]

[Figure 35]

Čt it ot

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

tanh σ σ

σ

[Figure 50]

[Figure 51]

[Figure 52]

LSTM LSTM LSTM LSTM

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

ht-1 ht

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[ , ]

[Figure 66]

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

LSTM LSTM LSTM LSTM

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

xt

s1

s2 s3 st

Input

Fig. 2. The overview of our proposed LSTM+attention solution is presented.

Fig. 1. An LSTM cell architecture is illustrated. [,] denotes array concatenation.

3) Proposed Network: All the 297 features from the 7 time-steps in each segment (as described earlier), were fed to 7 individual cells of the ﬁrst LSTM layer. We employed three stacked 7-cell layers in our network. The ﬁnal LSTM layer was followed by an attention layer, which was in turn followed by a fully connected layer with a sigmoid activation function to predict the probability of each class. This network The architecture is depicted in Figure 2.

compute its output given the updated cell state (see Figure 1).

The formulas describing an LSTM cell architecture are presented as:

it “ σpWi ¨ rht´1,xts ` biq, (1) ft “ σpWf ¨ rht´1,xts ` bfq, (2)

Ct “ ft ˚ Ct´1 ` it ˚ tanhpWc ¨ rht´1,xts ` bcq, (3) ot “ σpWo ¨ rht´1,xts ` boq, (4)

ht “ ot ˚ tanhpCtq, (5) where σpxq “ 1`1e´x

IV. EXPERIMENT SETUP AND EVALUATION

,tanhpxq “ 1`e2´2x ´1, ht is the hidden state at time step t, Ct´1 is the cell state at time step t, xt is the input features fed to the cell, Wf,Wi,Wc,Wo are the weights, and bf,bi,bc,bo are the biases that can be obtained by backpropagation through time.

This section presents the test material, optimal LSTM hyper-parameter setting, validation protocols, and the stateof-the-art and benchmark recognition solutions considered for comparison purposes.

2) Attention Mechanism: Attention mechanism can improve the performance of LSTM by focusing on certain timesteps with the most discriminative information. Unlike conventional LSTM networks that use their last hidden state as output, an LSTM network with attention mechanism multiplies the output hidden states by trainable weights, as shown in Figure 2, thus capturing more discriminative task-related features. This can be formulated as:

A. Dataset

The EEG Movement Dataset1,2 [30], [31] was used in this study. The dataset includes 109 subjects and has been collected using a BCI 2000 system. Participants were asked to perform three actions: rest (T0), left hand movement (T1), and right hand movement (T2). Each experiment consisted of 15 iterations, where T0 was followed by a visual stimulus, randomly selecting either T1 or T2. This 15-pair movement process was repeated 3 times. Accordingly, the dataset contains a total of 103 subjects ˆ 3 experiments ˆ 15 movements, for a total of 4635 movements. The dataset contains 64-channels of EEG, recorded at a sampling frequency of 160 Hz. Figure 3 illustrates a sample EEG recording and the three actions T0, T1, and T2.

hi “ LSTMpsiq,i P r1,Ls, (6)

where, hi is the output hidden state vector for the ith LSTM cell corresponding to the ith input, and L is the number of cells in each recurrent layer of the LSTM network. To capture the importance of each hidden state, attention mechanism is deﬁned as follows:

#### ui “ tanhpWshi ` bsq, (7)

Out of the 109 subjects in the dataset, the data from 6 particular subjects (43, 88, 89, 92, 100, and 104) had low signal to noise ratio. Therefore, they were removed from our dataset. Rejection of poor-quality samples has been performed in the literature for the same dataset [11]–[15].

exppuiq ř

, (8)

αi “

j exppujq

v “ ÿ

αihi, (9)

i

where vector v is the attention layer’s output, and Ws and bs are trainable parameters.

1https://physionet.org/pn4/eegmmidb/ 2www.bci2000.org

Visual s mulus

TABLE III TRAINING HYPER-PARAMETERS

[Figure 87]

[Figure 88]

[Figure 89]

Hyperparamters Cross-Subject Intra-Subject Recurrent depth 3 3

Batch size 32 2 Number of training epochs 100 10 LSTM hidden layer size 256 256

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

D0 “ 0.0 D0 “ 0.7 D1 “ 0.2 D1 “ 0.2 D2 “ 0.1 D2 “ 0.1 D3 “ 0.2 D3 “ 0.1

Dropout rates

Learning L2 “ 0.001, lr “ 0.001

β1 “ 0.9, β2 “ 0.999

[Figure 94]

sliding window

1 2 3 4 5 6 7

T0

- T1
- T2

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

metrics, namely Precision, Recall, and Accuracy, which are formulated as follows:

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

TP TP ` FP

sequences time steps

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

, (10)

Precision “

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

TP TP ` FN

, (11)

Recall “

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

T0

[Figure 133]

-2.0s -1.0s 0s 1.0s 2.0s

TP ` TN TP ` TN ` FP ` FN

. (12)

Accuracy “

- Fig. 3. An overview of the EEG data, the movement segments (2-second long LSTM sequence consists of 7 time steps with 50% overlap between adjacent windows), and the sliding window used during training/classiﬁcation is illustrated.

- 1) Solutions for Cross-Subject Scheme: Solutions from re-

lated works include: PLV [15] and ANN [16], which have been discussed in Section II. As studies performing cross-subject validation on this challenging dataset were not very common, we implemented a number of other techniques including the classical machine learning and deep learning solutions that have been successfully implemented in the imagery task (as mentioned in the related work) to better compare with our proposed solution. The conventional benchmarks include SVM [18], Na¨ıve Bayes [18], decision tree [33], logistic regression [17], and random forest [34]. The SVM used an 8th degree polynomial kernel and the random forest used 30 estimators up to a depth of 2. These parameters were tuned empirically in order to achieve the best results. The benchmarking solutions included deep learning methods as well. First, we used a 3´layer 2D-CNN, accepting a 2D matrix of 297 features as inputs. The network had a kernel size of 3 ˆ 3, and feature maps of 32, 64, and 128, respectively for the ﬁrst, second, and third convolutional layers. A VGG-16 CNN was also used for benchmarking. This model was pre-trained on ImageNet [35] and ﬁne-tuned for our application. This model was presented with inputs in the form of 3D matrices, which were achieved by re-sizing the feature matrices to 180ˆ150ˆ1 using linear interpolation. The output of the VGG-16 convolution layers was followed by 2 fully connected layers that used ReLu activation and a ﬁnal output layer with sigmoid activation for estimating the class probabilities. Lastly, an LSTM network without the attention mechanism was also used for benchmarking. In this model, similar hyperparameters as our proposed attention-based method were used (see Table III).

- 2) Solutions for Intra-Subject Scheme: As discussed earlier,

- B. LSTM Hyper-Parameters Setting

A number of hyper-parameters for the network were explored and tuned to achieve the best results for our proposed model. Notably, these hyper-parameters include: recurrent depth, batch size, number of training epochs, LSTM hidden layer size, dropout rates applied after input layer and the following three stacked LSTM layers (D0,D1,D2,D3), and the weight matrix L2 regularization coefﬁcient of each LSTM layer. Additionally, some hyper-parameters were tuned for the stochastic Adam optimizer [32], such as learning rate (lr) and exponential decay rates for the ﬁrst and second movement estimates (β1 and β2). The optimum values for these parameters are presented in Table III. A different set of parameters was assigned for each validation scheme (crosssubject and intra-subject) to maximize performance. A binary cross-entropy loss function L “ ´y logppq`p1´yqlogp1´pq was employed for training.

vspace-2mm

- C. Validation Protocols and Benchmarking

To rigorously evaluate the performance for our proposed solution, we utilized both intra-subject and cross-subject validation schemes. Both schemes used 10-fold cross-validation, where no overlap existed in the training and testing segments at each fold, as previous studies with such overlaps have shown to yield very high accuracies as expected [22]. True Positive (TP), False Negative (FN), False Positive (FP), and True Negative (TN) were used to calculate the performance

the main goal for this work is to tackle the more challenging task of cross-subject generalization. However, to further test our method and compare to the state-of-the-art, we compared

TABLE IV EFFECT OF SEGMENT SIZE

##### Size (seconds) 0.25 0.5 0.75 1.0 1.25 1.5 1.75 2.0 Accuracy ˘ SD 82.18 ˘ 2.1 80.23 ˘ 1.8 79.1 ˘ 1.5 80.3 ˘ 1.9 80.8 ˘ 1.7 81.1 ˘ 0.9 81.2 ˘ 2.0 83.2 ˘ 1.2

TABLE V COMPARISON OF DIFFERENT METHODS USING CROSS-SUBJECT SCHEME

TABLE VI COMPARISON OF DIFFERENT METHODS USING INTRA-SUBJECT SCHEME

Methods Accuracy ˘ SD Precision ˘ SD Recall ˘ SD

Method Accuracy ˘ SD Precision ˘ SD Recall ˘ SD

PLV [15] 78.9 ´ ´ ANN [16] 68.0 ´ ´

CSP [10] 64.0 ´ ´ QDA [11] 88.6 ´ ´

- Rough set [12] 60.0 ´ ´
- Rough set [13] 68.0 ´ ´ MDA [14] 87.0 ´ ´

SVM 62.4 ˘ 2.1 61.5 ˘ 1.7 62.4 ˘ 2.1 Logistic Regression 52.9 ˘ 1.4 52.4 ˘ 2.1 51.1 ˘ 1.3

Decision Tree 51.0 ˘ 1.3 50.3 ˘ 1.3 50.3 ˘ 1.3 Random Forest 53.0 ˘ 1.2 52.9 ˘ 1.6 61.5 ˘ 1.4

LSTM + Attention 98.3 ˘ 0.9 94.7 ˘ 1.1 95.9 ˘ 1.7

Naive Bayes 51.1 ˘ 1.3 50.7 ˘ 1.2 51.2 ˘ 1.9 3-layer 2D-CNN 63.2 ˘ 1.3 63.1 ˘ 1.5 63.1 ˘ 1.2

VGG-16 53.2 ˘ 1.3 53.1 ˘ 2.1 53.2 ˘ 1.3 LSTM 77.2 ˘ 2.5 77.2 ˘ 1.5 76.9 ˘ 1.1

The Receiver Operating Characteristic (ROC) curve, which shows the changes of the TP rate with respect to the FP rate, for the proposed model and the top three benchmarking solutions (in the cross-subject scheme) is illustrated in Figure 4. This ﬁgure also includes the Area Under the Curve (AUC) values that reveal the superiority of our proposed approach over the top three benchmarks with an AUC of 0.908.

LSTM + Attention 83.2 ˘ 1.2 83.7 ˘ 1.2 82.2 ˘ 2.1

our proposed method with solutions from previous studies namely CSP [10], QDA [11], rough set-based [12], [13], and MDA [14] described in Section II. We did not attempt to utilize more benchmarking solutions in this scheme, as most of the related works in this area utilize intra-subject validation, thus comparing to those works was deemed sufﬁcient.

Discussion: Here, we analyze the distribution and contribution of the different features used in this study. In order to analyze the contribution of different features, we calculated the importance of each feature by employing Random Forest (RF) [36] for feature ranking. We did not use alternative feature importance measures such as Chi-Squared and Fmeasure [37] since the features did not follow a normal distribution (one-sample Kolmogorov-Smirnov test: p ă 0297.05). Figure 5.A shows the three top features ranked using RF, namely skewness, mean, and area of F7-F8 sensor pair, where difference between the means of the two classes (L/R) can be observed. Further, Figure 5.B illustrates the importance scores calculated using RF, along with the signiﬁcance of each feature measured by non-parametric t-test at p ă 0297.05. Finally, we select the top-30 signiﬁcant subject-independent features and utilize them in the following paragraphs to explore the ﬂow of information relevant to L/R hand movement through the sensors over time. The image in Table VII shows the sensor distribution based on the international 10-10 system [38]. The table presents the ranking of the sensor pairs based on the number of features selected using the feature extraction and ranking method when the highest accuracy is achieved with our proposed solution. It can be observed that the FT7-FT8 sensor pair in the frontal-temporal lobe is the most dominant with 5 features, followed by the T9-T10 sensor pair in the temporal lobe with 4 features. The F7-F8 and T7-T8 sensor pairs, in the frontal and temporal lobes respectively, both have 3 selected features, followed by F5-F6 with 2, and the remaining sensor pairs with 1 or 0 features.

V. RESULTS AND DISCUSSION

In this section, we report the conducted experiments and performance. First, we study the effect of segment size. Then, we demonstrate the performance of our proposed method along with comparisons to other machine learning techniques and previous studies. Next, we perform a feature analysis, and ﬁnally, we discuss the most dominant sensors when maximum accuracy is achieved using our method, followed by an analysis of the ﬂow of information during the experiments.

Effect of Segment Size: In order to select the optimum segment size for feature extraction, we experimented with different segment sizes (0.25,0.5,0.75,1.0,1.25,1.5,1.75, and 2.0 seconds), and evaluated the performance of the model with cross-subject validation. Table IV presents that the highest classiﬁcation accuracy and minimum standard deviation with 10-fold cross-validation were achieved when the segment size was 2 seconds long. As a result, in this study, the segment size was set to 2 seconds for feature extraction and classiﬁcation.

Performance: Table V shows the average accuracy, precision, and recall along with their standard deviations for the proposed method and other benchmarking solutions in the cross-subject scheme setting. These results demonstrate the robust performance of our proposed model compared to other methods. The results show that our proposed model signiﬁcantly outperforms the best performing benchmark, i.e., PLV, by a considerable 5% accuracy. Additionally, Table VI reports the accuracy, precision, and recall rates obtained for the intra-subject scheme, showing near-perfect performance, while the previous work with the best performance achieved an accuracy of 88.6% [11].

Next we analyze the ﬂow of information at different times during the experiment. In Figure 6, the accuracy of the proposed method is depicted along with the standard deviation. The experiment started at t “ 0s with the visual stimulus being presented to the subjects. As shown in the ﬁgure, in this stage, sensor pairs in the anterior-frontal (AF3-AF4 and AF7-

ROC curve

1.0

0.8

Truepositiverate

0.6

0.4

0.2

LSTM+Attention (area = 0.908)

LSTM (area = 0.866)

2D-CNN (area = 0.635)

SVM (area = 0.638)

0.0

0.0 0.2 0.4 0.6 0.8 1.0 False positive rate

- Fig. 4. The ROC curves and corresponding AUCs are presented for our proposed LSTM network and the top-3 benchmarking solutions.

AF8), parietal-occipital (PO3-PO4 and PO7-PO8), as well as occipital (O1-O2) lobes displayed the strongest features. This phenomenon is consistent with previous studies reporting that the visual cortex plays an important role in receiving and processing visual stimuli [39], [40]. The visual cortex occupies approximately 20% space of the cerebral-cortex and is located in the occipital, parietal-posterior, and temporal lobes [41]. Moreover, the information ﬂow in the parietaloccipital and occipital regions were also consistent with the activities reported in [41].

The P300 wave is a type of Event-Related Potential (ERP) that is believed to be dominant in decision-making [42], and is usually within the range of 250ms to 500ms of the onset of visual stimulus [43]. Similar to the P300 wave, Simple Reaction Time (SRT) represents the delay between visual stimulus and response, during which the usage of the sensor pairs at t “ 0.25s and t “ 0.50s shows brain activity. This is consistent with [44], reporting an average and standard deviation of 231 ˘ 27ms for SRT. During SRT, the previous highly informative sensor pairs in the parietal-occipital and occipital lobes gradually disappeared, and at t “ 0.25s sensor pairs in the frontal-temporal (FT7-FT8) and temporal-parietal (TP7-TP8) lobes became more prevalent. The phenomenon is consistent with previous studies, stating that after the receipt of visual stimulus in the visual cortex, visual information is transferred through two disparate streams, notably ventral stream and dorsal stream. Ventral stream eventually reaches the temporal cortex, commonly known for image recognition [45]. The visual stimulus is therefore processed to make the association between experiment instructions and performing L/R hand movement with the help of the relevant memory. Moreover, at t “ 0.25s sensor pairs in the central-parietal (CP3-CP4 and CP5-CP6) lobes, as well as all the sensor pairs in the parietal lobe (P1-P2, P3-P4 and P5-P6) became more informative compared to t “ 0s. This activity is also consistent with the phenomenon reported in previous studies, stating that the dorsal stream eventually reaches the parietal-

- A.
- B.

###### Rank 1 Feature

###### Rank 2 Feature

###### Rank 3 Feature

4

FeatureValue

2

0

- -4
- -2

R L

R L

R L

F7-F8 Sk

F7-F8 Mean

F7-F8 Area

10-4 Feature Importance Plot

|Significant mark<br><br>Not significant mark|
|---|

RandomForestImportanceScore

- 0

- 0.5
- 1

1.5

2

- 2.5

DeltaRelPower ThetaRelPower AlphaRelPower BetaRelPower Mean Var Skewness Kurtosis ZC Area Pk2Pk

Features Grouped by Channels

Fig. 5. An overview of the extracted features is presented. (A) shows the box-plots of the top three features. (B) shows the feature importance scores measured by RF in addition to the signiﬁcant features between the two classes, measured by non-parametric t-test.

cortex, which contains action-relevant information [45]. This is also supported by previous studies claiming that parietal lobe contributes predominantly to visual imagery and episodic memory [46].

At t “ 0.5s, the active effect of sensor pairs in the parietal lobe diminished, which represents the completion of information ﬂow in the dorsal stream. Consequently, sensor pairs in the central-parietal lobe (CP1-CP2, CP3-CP4 and CP5CP6) became even more informative. This observed pattern is also consistent with previous related work claiming that the parietal lobe also contributes to hand and upper limb control and eye movements with visual information [47].

At t “ 0.75s, sensor pairs in temporal (T7-T8 and T9T10), frontal (F7-F8) and anterior-frontal (AF7-AF8) lobes reached their highest degree of use, thus having the highest discriminability for L/R hand movements. This phenomenon was consistent with the fact explained by previous studies that the frontal lobe contains pre-motor cortex and primary motor cortex (M1), where the pre-motor cortex ﬁrst concatenates information from the parietal and frontal lobes, which is then delivered to M1. M1 is believed to be a generator of movement-speciﬁc commands [48]. Therefore, the classiﬁcation rate reached its highest peak because of the completed information streams in occipital-temporal and occipital-parietal-frontal [45]. Then, due to the high usage of sensor pairs in M1, the classiﬁcation rate remained relatively stable until the movement ended [48].

Lastly, from t “ 0.75s to t “ 2.0s, the sensor pairs in the temporal and frontal lobes maintained the highest degree of usage, while those in the parietal lobe were much less frequently used. The other sensor pairs in the occipital lobe barely contributed to the classiﬁcation task.

[Figure 134]

VI. SUMMARY AND FUTURE WORK

A novel solution for classiﬁcation of L/R hand movements from EEG signals was proposed. First the negative effects of signal artifacts was reduced, improving the quality of data. In the next step, a wide range of time and frequency domain features were exploited and used as inputs to an attention-based LSTM network. After studying the optimal LSTM hyperparameter settings, extensive experiments were conducted with the EEG Movement Database over a large number of subjects (103). The performance evaluation with both intra-subject and cross-subject validation schemes showed very effective results with a high generalization capability, demonstrating the superiority of the proposed approach when compared to other benchmarking models and previous state-of-the-art methods. The robust performance achieved in this paper suggests that the proposed approach can be used in future research for a broad range of EEG-related classiﬁcation tasks. Finally, a detailed analysis of the EEG information ﬂow through the sensors over time is presented, reﬂecting the brain activity throughout the experiment.

Future work will focus on models capable of early detection or prediction of hand movements rather than classiﬁcation using deep neural networks. Moreover, a possible limitation

of our work is the use of hand-crafted features. As a result, in future work, feature extraction using CNNs will be explored, which may lead to a simpler and more robust solution. Lastly, to tackle the challenges in cross-subject classiﬁcation, we will employ domain adaption techniques such as Wasserstein Generative Adversarial Network Domain Adaptation [49] in order to distinguish and minimize the differences among subjects with adversarial training.

ACKNOWLEDGMENT

The Titan XP GPU used for this research was donated by the NVIDIA Corporation.

REFERENCES

- [1] I. K¨athner, S. C. Wriessnegger, G. R. M¨uller-Putz, A. K¨ubler, and S. Halder, “Effects of mental workload and fatigue on the p300, alpha and theta band power during operation of an erp (p300) brain–computer interface,” Biological Psychology, vol. 102, pp. 118–129, 2014.
- [2] S. N. Abdulkader, A. Atia, and M.-S. M. Mostafa, “Brain computer interfacing: Applications and challenges,” Egyptian Informatics Journal, vol. 16, no. 2, pp. 213–230, 2015.
- [3] J. J. Daly and J. R. Wolpaw, “Brain–computer interfaces in neurological rehabilitation,” The Lancet Neurology, vol. 7, no. 11, pp. 1032–1043, 2008.
- [4] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain–computer interfaces for communication and control,” Clinical Neurophysiology, vol. 113, no. 6, pp. 767–791, 2002.

- [5] M. Takahashi, K. Takeda, Y. Otaka, R. Osu, T. Hanakawa, M. Gouko, and K. Ito, “Event related desynchronization-modulated functional electrical stimulation system for stroke rehabilitation: a feasibility study,” Journal of neuroengineering and rehabilitation, vol. 9, no. 1, p. 56, 2012.
- [6] L. R. Hochberg, M. D. Serruya, G. M. Friehs, J. A. Mukand, M. Saleh, A. H. Caplan, A. Branner, D. Chen, R. D. Penn, and J. P. Donoghue, “Neuronal ensemble control of prosthetic devices by a human with tetraplegia,” Nature, vol. 442, no. 7099, p. 164, 2006.
- [7] G. Pfurtscheller, C. Neuper, C. Guger, W. Harkam, H. Ramoser, A. Schlogl, B. Obermaier, and M. Pregenzer, “Current trends in graz brain-computer interface (bci) research,” IEEE transactions on Rehabilitation Engineering, vol. 8, no. 2, pp. 216–219, 2000.
- [8] J. Cantillo-Negrete, J. Gutierrez-Martinez, R. I. Carino-Escobar, P. Carrillo-Mora, and D. Elias-Vinas, “An approach to improve the performance of subject-independent bcis-based on motor imagery allocating subjects by gender,” Biomedical Engineering Online, vol. 13, no. 1, p. 158, 2014.
- [9] F. Lotte, C. Guan, and K. K. Ang, “Comparison of designs towards a subject-independent brain-computer interface based on motor imagery,” in 2009 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, pp. 4543–4546.
- [10] H. Wang and D. Xu, “Comprehensive common spatial patterns with temporal structure information of EEG data: minimizing nontask related EEG component,” IEEE Transactions on Biomedical Engineering, vol. 59, no. 9, pp. 2496–2505, 2012.
- [11] O. D. Eva and A. M. Lazar, “Comparison of classiﬁers and statistical analysis for EEG signals used in brain computer interface motor task paradigm,” International Journal of Advanced Research in Artiﬁcial Intelligence, vol. 4, no. 1, pp. 8–12, 2015.
- [12] P. Szczuko, “Rough set-based classiﬁcation of EEG signals related to real and imagery motion,” in IEEE Signal Processing: Algorithms, Architectures, Arrangements, and Applications (SPA), 2016, pp. 34–39.
- [13] P. Szczuko, M. Lech, and A. Czy˙zewski, “Comparison of classiﬁcation ,ethods for EEG signals of real and imaginary motion,” in Advances in Feature Selection for Data and Pattern Recognition. Springer, 2018, pp. 227–239.
- [14] P. Szczuko, “Real and imaginary motion classiﬁcation based on rough set analysis of EEG signals for multimedia applications,” Multimedia Tools and Applications, vol. 76, no. 24, pp. 25697–25711, 2017.
- [15] A. Loboda, A. Margineanu, G. Rotariu, and A. M. Lazar, “Discrimination of EEG-based motor imagery tasks by means of a simple phase information method,” International Journal of Advanced Research in Artiﬁcial Intelligence, vol. 3, no. 10, 2014.
- [16] N. T. M. Huong, H. Q. Linh, and L. Q. Khai, “Classiﬁcation of left/right hand movement EEG signals using event related potentials and advanced features,” in International Conference on the Development of Biomedical Engineering in Vietnam. Springer, 2017, pp. 209–215.
- [17] R. Tomioka, K. Aihara, and K.-R. M¨uller, “Logistic regression for single trial EEG classiﬁcation,” in Advances in Neural Information Processing Systems, 2007, pp. 1377–1384.
- [18] S. Bhattacharyya, A. Khasnobish, A. Konar, D. Tibarewala, and A. K. Nagar, “Performance analysis of left/right hand movement classiﬁcation from EEG signal by intelligent algorithms,” in IEEE Symposium on Computational Intelligence, Cognitive Algorithms, Mind, and Brain (CCMB), 2011, pp. 1–8.
- [19] Z. Tang, C. Li, and S. Sun, “Single-trial EEG classiﬁcation of motor imagery using deep convolutional neural networks,” Optik-International Journal for Light and Electron Optics, vol. 130, pp. 11–18, 2017.
- [20] Y. R. Tabar and U. Halici, “A novel deep learning approach for classiﬁcation of eeg motor imagery signals,” Journal of neural engineering, vol. 14, no. 1, p. 016003, 2016.
- [21] P. Wang, A. Jiang, X. Liu, J. Shang, and L. Zhang, “Lstm-based EEG classiﬁcation in motor imagery tasks,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 26, no. 11, pp. 2086–2095, 2018.
- [22] D. Zhang, L. Yao, X. Zhang, S. Wang, W. Chen, and R. Boots, “Eegbased intention recognition from spatio-temporal representations via cascade and parallel convolutional recurrent neural networks,” arXiv preprint arXiv:1708.06578, 2017.
- [23] Y.-P. Lin, C.-H. Wang, T.-P. Jung, T.-L. Wu, S.-K. Jeng, J.-R. Duann, and J.-H. Chen, “EEG-based emotion recognition in music listening,” IEEE Transactions on Biomedical Engineering, vol. 57, no. 7, pp. 1798–1806, 2010.
- [24] M. H. Alomari, A. Samaha, and K. AlKamha, “Automated classiﬁcation of l/r hand movement EEG signals using advanced feature extraction and machine learning,” arXiv preprint arXiv:1312.2877, 2013.

- [25] K. M. Tsiouris, V. C. Pezoulas, M. Zervakis, S. Konitsiotis, D. D. Koutsouris, and D. I. Fotiadis, “A long short-term memory deep learning network for the prediction of epileptic seizures using EEG signals,” Computers in Biology and Medicine, vol. 99, pp. 24–37, 2018.
- [26] P. Zhou, W. Shi, J. Tian, Z. Qi, B. Li, H. Hao, and B. Xu, “Attentionbased bidirectional long short-term memory networks for relation classiﬁcation,” in Proceedings of Association for Computational Linguistics, vol. 2, 2016, pp. 207–212.
- [27] Y. Wang, M. Huang, L. Zhao et al., “Attention-based lstm for aspectlevel sentiment classiﬁcation,” in Proceedings of the 2016 conference on empirical methods in natural language processing, 2016, pp. 606–615.
- [28] Z. C. Lipton, J. Berkowitz, and C. Elkan, “A critical review of recurrent neural networks for sequence learning,” arXiv preprint arXiv:1506.00019, 2015.
- [29] K. Greff, R. K. Srivastava, J. Koutn´ık, B. R. Steunebrink, and J. Schmidhuber, “Lstm: A search space odyssey,” IEEE Transactions on Neural Networks and Learning Systems, vol. 28, no. 10, pp. 2222–2232, 2017.
- [30] G. Schalk, D. J. McFarland, T. Hinterberger, N. Birbaumer, and J. R. Wolpaw, “Bci2000: a general-purpose brain-computer interface (BCI) system,” IEEE Transactions on Biomedical Engineering, vol. 51, no. 6, pp. 1034–1043, 2004.
- [31] P. PhysioToolkit, “Physionet: components of a new research resource for complex physiologic signals,” Circulation. v101 i23. e215-e220.
- [32] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” arXiv preprint arXiv:1412.6980, 2014.
- [33] O. Aydemir and T. Kayikcioglu, “Decision tree structure based classiﬁcation of eeg signals recorded during two dimensional cursor movement imagery,” Journal of neuroscience methods, vol. 229, pp. 68–75, 2014.
- [34] M. Bentlemsan, E.-T. Zemouri, D. Bouchaffra, B. Yahya-Zoubir, and K. Ferroudji, “Random forest and ﬁlter bank common spatial patterns for eeg-based motor imagery classiﬁcation,” in 2014 5th International Conference on Intelligent Systems, Modelling and Simulation. IEEE, 2014, pp. 235–238.
- [35] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “Imagenet: A large-scale hierarchical image database,” in IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2009, pp. 248–255.
- [36] L. Breiman, “Random forests,” Machine learning, vol. 45, no. 1, pp. 5–32, 2001.
- [37] G. Forman, “An extensive empirical study of feature selection metrics for text classiﬁcation,” Journal of Machine Learning Research, vol. 3, no. Mar, pp. 1289–1305, 2003.
- [38] F. Lotte, A. Van Langhenhove, F. Lamarche, T. Ernest, Y. Renard, B. Arnaldi, and A. L´ecuyer, “Exploring large virtual environments by thoughts using a brain–computer interface based on motor imagery and high-level commands,” Presence: Teleoperators and Virtual Environments, vol. 19, no. 1, pp. 54–70, 2010.
- [39] S. Zeki, J. Watson, C. Lueck, K. J. Friston, C. Kennard, and R. Frackowiak, “A direct demonstration of functional specialization in human visual cortex,” Journal of neuroscience, vol. 11, no. 3, pp. 641–649, 1991.
- [40] A. D. Milner and M. A. Goodale, “Two visual systems re-viewed,” Neuropsychologia, vol. 46, no. 3, pp. 774–785, 2008.
- [41] B. A. Wandell, S. O. Dumoulin, and A. A. Brewer, “Visual ﬁeld maps in human cortex,” Neuron, vol. 56, no. 2, pp. 366–383, 2007.
- [42] E. Donchin, K. M. Spencer, and R. Wijesinghe, “The mental prosthesis: assessing the speed of a p300-based brain-computer interface,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 8, no. 2, pp. 174–179, 2000.
- [43] S. Yang and F. Deravi, “On the usability of electroencephalographic signals for biometric recognition: A survey,” IEEE Transactions on Human-Machine Systems (HMS), vol. 47, no. 6, pp. 958–969, 2017.
- [44] D. L. Woods, J. M. Wyma, E. W. Yund, T. J. Herron, and B. Reed, “Factors inﬂuencing the latency of simple reaction time,” Human Neuroscience, vol. 9, p. 131, 2015.
- [45] M. A. Goodale and A. D. Milner, “Separate visual pathways for perception and action,” Trends in Neurosciences, vol. 15, no. 1, pp. 20–25, 1992.
- [46] T. Pﬂugshaupt, M. N¨osberger, K. Gutbrod, K. P. Weber, M. Linnebank, and P. Brugger, “Bottom-up visual integration in the medial parietal lobe,” Cerebral Cortex, vol. 26, no. 3, pp. 943–949, 2014.
- [47] L. Fogassi and G. Luppino, “Motor functions of the parietal lobe,” Current Opinion in Neurobiology, vol. 15, no. 6, pp. 626–631, 2005.
- [48] R. P. Dum and P. L. Strick, “Motor areas in the frontal lobe of the primate,” Physiology & Behavior, vol. 77, no. 4-5, pp. 677–682, 2002.
- [49] Y. Luo, S.-Y. Zhang, W.-L. Zheng, and B.-L. Lu, “Wgan domain adaptation for eeg-based emotion recognition,” in International Conference on Neural Information Processing. Springer, 2018, pp. 275–286.

