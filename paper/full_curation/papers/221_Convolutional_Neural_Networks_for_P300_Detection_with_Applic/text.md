[Figure 1]

### Convolutional Neural Networks for P300 Detection with Application to Brain-Computer Interfaces

Cecotti, H., & Graeser, A. (2011). Convolutional Neural Networks for P300 Detection with Application to BrainComputer Interfaces. IEEE Transactions on Pattern Analysis and Machine Intelligence, 33(3), 433-445. https://doi.org/10.1109/TPAMI.2010.125

Link to publication record in Ulster University Research Portal

Published in: IEEE Transactions on Pattern Analysis and Machine Intelligence

Publication Status: Published (in print/issue): 01/03/2011

DOI: 10.1109/TPAMI.2010.125

Document Version Author Accepted version

For Author Accepted Manuscripts (AAM) published under Ulster University's Rights Retention Policy for Scholarly Works (RRPSW)

When citing an AAM published under Ulster University's RRPSW please use the following citation structure: Author, A. A. (Year). Title of article. Journal Name, [Accepted Author Manuscript]. PURE Portal URL. Licensed under CC BY 4.0. General rights The copyright and moral rights to the output are retained by the output author(s), unless otherwise stated by the document licence. Unless otherwise stated, users are permitted to download a copy of the output for personal study or non-commercial research and are permitted to freely distribute the URL of the output. They are not permitted to alter, reproduce, distribute or make any commercial use of the output without obtaining the permission of the author(s). If the document is licenced under Creative Commons, the rights of users of the documents can be found at https://creativecommons.org/share-your-work/cclicenses/. Take down policy The Research Portal is Ulster University's institutional repository that provides access to Ulster's research outputs. Every effort has been made to ensure that content in the Research Portal does not infringe any person's rights, or applicable UK laws. If you discover content in the Research Portal that you believe breaches copyright or violates any law, please contact pure-support@ulster.ac.uk

Download date: 26/06/2026

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. 33, NO. 3, MARCH 2011 433

## Convolutional Neural Networks for P300 Detection with Application to Brain-Computer Interfaces

Hubert Cecotti and Axel Gra¨ser

Abstract—A Brain-Computer Interface (BCI) is a specific type of human-computer interface that enables the direct communication between human and computers by analyzing brain measurements. Oddball paradigms are used in BCI to generate event-related potentials (ERPs), like the P300 wave, on targets selected by the user. A P300 speller is based on this principle, where the detection of P300 waves allows the user to write characters. The P300 speller is composed of two classification problems. The first classification is to detect the presence of a P300 in the electroencephalogram (EEG). The second one corresponds to the combination of different P300 responses for determining the right character to spell. A new method for the detection of P300 waves is presented. This model is based on a convolutional neural network (CNN). The topology of the network is adapted to the detection of P300 waves in the time domain. Seven classifiers based on the CNN are proposed: four single classifiers with different features set and three multiclassifiers. These models are tested and compared on the Data set II of the third BCI competition. The best result is obtained with a multiclassifier solution with a recognition rate of 95.5 percent, without channel selection before the classification. The proposed approach provides also a new way for analyzing brain activities due to the receptive field of the CNN models.

Index Terms—Neural network, convolution, gradient-based learning, spatial filters, brain-computer interface (BCI), electroencephalogram (EEG), P300.

#### Ç

- 1 INTRODUCTION

# A

Brain-Computer interface (BCI) is a direct commu-

nication pathway between a human brain and an external device. Such systems allow people to communicate through direct measurements of brain activity, without requiring any movement [1], [2], [3]. BCIs may be the only means of communication possible for people who are unable to communicate via conventional means because of severe motor disabilities like spinal cord injuries or like amyotrophic lateral sclerosis (ALS), also called Lou Gehrig’s disease [2], [4]. Among noninvasive methods for monitoring brain activity, we consider in this paper electroencephalography (EEG) techniques. They have several practical qualities: Data can be easily recorded with relatively inexpensive equipment; they are the common solution for noninvasive BCIs.

A BCI is usually decomposed into four main parts that translate the neural signal processing. First, the signal is acquired via an amplifier. Then, the signal is processed and assigned to different classes, which denotes the different stimuli. Finally, the classes are sent to the output device components and the operating protocol links all the components. The signalclassification component iscomposed of the brain signal features extraction and the translation of these

. The authors are with the Institute of Automation, University of Bremen,

Otto-Hahn-Allee, NW1 28359 Bremen, Germany. E-mail: hcecotti@orange.fr, ag@iat.uni-bremen.de.

Manuscript received 28 Nov. 2008; revised 25 Feb. 2009; accepted 3 June 2009; published online 16 June 2010. Recommended for acceptance by L. Bottou. For information on obtaining reprints of this article, please send e-mail to: tpami@computer.org, and reference IEEECS Log Number TPAMI-2008-11-0821. Digital Object Identifier no. 10.1109/TPAMI.2010.125.

signals into device commands. The EEG classification strategy depends on the stimulus and, thereby, the response to detect: event-related potentials, steady-state evoked potentials, motor imagery, or slow cortical potentials. The expected EEG drives the classification to some specific feature extraction methods.

Pattern recognition techniques are used for the classification and the detection of specific brain signals. Most of the effective solutions use machine learning models [5], [6], [7], [8]. Although neuroscience provides knowledge and guidelines about how to process and detect the expected signals, machine learning techniques allow modeling the signal variability over time and over subjects. Neural networks [9], [10], [11], [12], [13], [14], support vector machines (SVMs) [15], [16], and hidden Markov models [17], [18] have already been applied to BCI and EEG classification. Neural networks using backpropagation were used for the first time for readiness potential pattern recognition in [19], proving that neural networks can be used for classifying EEG and for tailoring a brain machine interface.

Most of the current techniques in the BCI community are based on SVMs. Gradient-based learning methods such as convolutional neural networks have been successfully used in character recognition and achieve the best recognition results in database such as MNIST [20], [21]. They are also used in speech processing [22]. In the case of character recognition, such models could offer a tolerance to geometric deformations, to some extent. The evaluation of their performance for the classification of an EEG signal, which possesses a high variability, is one topic of this study. Also, one interesting property of CNN models is the semantic of the weights once the network is trained. The receptive field/ convolution kernel can be easily interpreted and can provide

0162-8828/11/$26.00 2011 IEEE Published by the IEEE Computer Society

a diagnostic about the type of high-level features to detect. We propose using CNN models and their combination, for the first time, for the detection of P300 waves.

The paper is organized as follows: The P300 wave, the oddball paradigm, and the database are presented in Section 2. The neural network is described in Section 3. Section 4describesthedifferentclassifiers.Finally,theresults and their discussion are detailed in Sections 5 and 6.

- 2 BACKGROUND

- 2.1 The P300 Speller The P300 wave is an event-related potential (ERP) which can be recorded via EEG. The wave corresponds to a positive deflection in voltage at a latency of about 300 ms in the EEG. In other words, it means that after an event like a flashing light, a deflection in the signal should occur after 300 ms. The signal is typically measured most strongly by the electrodes covering the parietal lobe. However, Krusienski et al. showed that occipital sites are more important [23]. Furthermore, the presence, magnitude, topography, and time of this signal are often used as metrics of cognitive function in decision making processes. If a P300 wave is detected 300 ms after a flashing light in a specific location, it means that the user was paying attention to this same location. The detection of a P300 wave is equivalent to the detection of where the user was looking 300 ms before its detection. In a P300 speller, the main goal is to detect the P300 peaks in the EEG accurately and instantly. The accuracy of this detection will ensure a high information transfer rate between the user and the machine. Farwell and Donchin introduced the first P300-BCI in 1988 [24], [25].
- 2.2 P300 Detection There exist two types of classifications for the problem of P300-based BCI as illustrated in Fig. 1. These classification steps are sequential:

- 1. The detection of P300 responses. It corresponds to a binary classification: One class represents signals that correspond to a P300 wave, the second class is the opposite. For this classification problem, the creation of the ground truth can be quite challenging. Although the paradigm during the experiment allows knowing when a P300 response is expected, this response depends on the user. Indeed, although a P300 response can be expected at one particular moment, it is possible that the user does not produce a P300 response at the right moment as many artifacts can occur. The production of a P300 wave is not a phenomenon of consciousness; it is produced due to the flashing lights.
- 2. The character recognition. The outputs of the previous classification are then combined to classify the main classes of the application (characters, symbols, actions, ...). Whereas the ground truth of the first classification step remains uncertain, the ground truth of the character recognition problem can be created easily as the character to spell is clearly given to the subject. In the oddball paradigm, a character is defined by a couple (x, y). The flashing lights are on each row and column and not on each

[Figure 2]

Fig. 1. The two classification problems. (a) P300 detection. (b) Character recognition.

character. The character is supposed to correspond to the intersection of the accumulation of several P300 waves. The best accumulation of P300 waves for the vertical flashing lights determines the column of the desired character. The principle is the same for the horizontal flashing lights and the rows.

2.3 Database

Data set II from the third BCI competition was used for testing the different models [26]. The database was initially provided by the Wadsworth Center, New York State Department of Health. This data set contains a complete record of P300 evoked potentials from two subjects. The signal was recorded in five sessions with the BCI2000 framework [27]. In these experiments, the subject was presented with a matrix of size 6 6. Each cell of the matrix contains a character: [A-Z], [1-9], and [_]. The main classification problem therefore has 36 classes. The subject’s task was to sequentially focus on characters from a predefined word. The six rows and six columns of this matrix were successively and randomly intensified at a rate of 5.7 Hz. The character to select is defined by a row and a column. Thus, 2 out of 12 intensifications of rows/columns highlighted the expected character, i.e., 2 of the 12 intensifications should produce a P300 response.

During the experiment, the matrix was displayed for a 2.5 s period, and during this time, the matrix was blank: Each character had the same intensity. Then, each row and column in the matrix was randomly intensified for 100 ms. After intensification of a row/column, the matrix was blank for 75 ms. Row/column intensifications were block randomized in blocks of 12. The sets of 12 intensifications were repeated

TABLE 1 Database Size for Each Subject

[Figure 3]

15 times for each character epoch. All of the rows/columns were intensified 15 times. Therefore, 30 possible P300 responses should be detected for the character recognition.

Signals from the two subjects were collected from 64 earreferenced channels. The signal was bandpass filtered from 0.160 Hz and digitized at 240 Hz [28]. The training database is composed of 85 characters, while the test database contains 100 characters. Each character epoch is supposed to contain two P300 signals, one for a row flash and one for the column flash. For the training database, the number of P300 to detect is 85 2 15. The number of samples for both databases and for each subject is presented in Table 1.

- 2.4 Existing Systems This section describes some of the best techniques that have been proposed during the third BCI competition. They also correspond to the state of the art for the P300 speller. These solutions are mostly based on multiclassifiers strategy. Some techniques use advanced signal processing methods for cleaning the data. Furthermore, it is not easy to compare the inner strength of one classifier as the inputs are often different. They vary in size in relation to the number of considered electrodes and the size of the time window describing a P300 wave. The results of the best methods will be compared with the proposed method in the last section.

. The solution proposed by Rakotomamonjy and Guigue [16] is based on an ensemble of SVMs. In this solution, the signal is extracted with a 667 ms time window after each stimulus. Then the signal is bandpass filtered with an 8-order filter with cutoff frequencies between 0.1 and 20 Hz. For each channel, the signal is defined by 14 features. The size of the input is 896 (14 64). The training database is partitioned into groups of 900 patterns. Each group is related to the spelling of five characters. Therefore, the training database is divided into 17 partitions. A linear SVM is trained on each partition and a channel selection procedure is performed. The channel selection algorithm is a recursive channel elimination based on criteria in relation to the confusion matrix of the validation test. The character recognition is achieved by summing all the scores of the SVMs. The row and column that get the highest score are consideredasthe coordinate ofthe characterto detect.

. The method of Li Yandong from the Department of Automation and Department of Biomedical Engineering, Tsinghua University, China, is decomposed into three steps. First, data are preprocessing with bandpass filtering at 0.5-8 Hz. Then, eye movement artifacts are removed by using independent component analysis (ICA) for the whole data set. The classification is based on SVMs and bagging with patterns selected with a time window of 100-850 ms

after a flashing light [29]. A subset of electrodes is selected prior to the classification. The final classification is achieved through the voting of multiple SVM classifiers contrary to other methods, which average the outputs.

. The technique of Zhou Zongtan from the Department of Automatic Control, National University of Defense Technology, China, is based on frequency filtering and principal component analysis (PCA) for the preprocessing steps. The feature selection uses t-statistic values at each data point in each channel. For the data, the author only keeps the extremum points of t-statistic values from each channel. The classification is performed by comparing the different features set.

. Ulrich Hoffmann from the Ecole Polytechnique Federale of Lausanne (EPFL), Switzerland, uses a gradient boosting method that is described in [30].

. Lin Zhonglin, Department of Automation, Tsinghua University, China, uses bagging with component classifier linear discriminant analysis (LDA) [29]. For each subject, the authors first create 150 training sets by drawing about 60 percent samples from the original training set. Then each of these data sets is used to train an LDA classifier. The final classification decision is based on the vote of each component classifier. For the input, the signal is bandpass filtered between 0.5 and 15 Hz and 10 channels are selected before the classification.

3 CONVOLUTIONAL NEURAL NETWORK

The classifiers that are used for the detection of P300 responses are based on a convolutional neural network (CNN). This type of neural network is a multilayer perceptron (MLP) with a special topology and contains more than one hidden layer. This neural network is used for object recognition [31] and handwriting character recognition [21], [32]. It allows automatic features extraction within its layers and it keeps as input the raw information without specific normalization, except for scaling and centering the input vector. This kind of model has many advantages when the input data contain an inner structure like for images and where invariant features must be discovered. One interest on convolutional neural network is the possibility of including, inside the network, high-level knowledge that is directly relatedtotheproblem,contrarytokernel-basedmethods[20]. One other interest is to avoid hand-designed input features, which are not derived by the general problem. However, the topology of the network remains an empirical choice and depends on the application. The topology translates different successive signal/neural processing steps.

A classifier based on a CNN seems to be a good approach for EEG classification as the signal to detect contains a lot of variations over time and persons. For such a variable signal, architectures based on local kernels can be inefficient at representing functions that must be tolerant to many variations, i.e., functions that are not globally smooth [20]. The interest of the CNN is to directly classify the raw signal and to integrate the signal processing functions within the discriminant steps. Indeed, it is not always possible to know the type of features to extract. It is better to let the network

[Figure 4]

Fig. 2. Electrode map.

extract the most discriminant features by constructing highlevel features throughout the propagation step.

- 3.1 Input Normalization The inputs are the EEG signal values from the electrodes

during TSs, Ii;j, 0 i < Nelec, 0 j < SF TS. SF is the sampling frequency in hertz (Hz). The data are normalized in two steps. First, the EEG signal is subsampled to reduce the size of the data to analyze. The size is divided by two. It is now equivalent to a signal sampled at 120 Hz. Then, the signal is bandpass filtered between 0.1 and 20 Hz to keep

only relevant frequencies but it is kept sampled at 120 Hz. Finally, the signal is normalized as follows:

Ii;j ðIi;j IiÞ=ð iÞ; ð1Þ

where Ii and i are, respectively, the average value and the first deviation of the electrode i at the time j in TSs. The average and the standard deviation are based on each individual pattern and for each electrode. The input of the CNN is a matrix Nelec Nt, where Nt is the number of points that are considered for the analysis: Nt ¼ SF TS. Nt corresponds to the number of recorded samples in TSs with the sampling rate SF. When all of the electrodes are used, Nelec ¼ 64. In the experiments, we set Nt ¼ 78 that represents 650 ms. Each pattern represents a part of the signal starting after a flashing light and during 650 ms.

3.2 Neural Network Topology

The network topology is the key feature in the classifier. The network is composed of five layers, which are themselves composed of one or several maps. A map represents a layer entity, which has a specific semantic: Each map of the first hidden layer is a channel combination. The second hidden layer subsamples and transforms the signal in the time domain. The classifier architecture is presented in Fig. 3. The number of neurons for each map is presented between brackets; the size of the convolution kernel is between hooks. The order of the convolution is chosen in relation to what is traditionally done in BCI. First, optimal spatial filters/ channel combinations are set, then the signal is processed in thetimedomain.Thechoiceofthetopologyisalsojustifiedby the possibility of easily interpreting the trained convolution kernel, i.e., the receptive fields. In the proposed strategy, the kernels are vectors and not matrix, like in CNNs for image recognition. The reason is to not mix in one kernel features related to the space and time domain.

The network topology is described as follows:

. L0: The input layer. Ii;j with 0 i < Nelec and 0 j < Nt.

[Figure 5]

- Fig. 3. Neural network architecture.

- . L1: The first hidden layer is composed of Ns maps. We define L1Mm, the map number m. Each map of L1 has the size Nt.
- . L2: The second hidden layer is composed of 5Ns maps. Each map of L2 has six neurons.
- . L3: The third hidden layer is composed of one map of 100 neurons. This map is fully connected to the different maps of L2.
- . L4: The output layer. This layer has only one map of two neurons, which represents the two classes of the problem (P300 and no P300). This layer is fully connected to L3.

3.3 Learning

A neuron in the network is defined by nðl;m;jÞ, where l, m, and j are the layer, the map, and its position in the map, respectively. Its current value is xlmðjÞ, or xlðjÞ when there is only one map in the layer:

xlmðjÞ ¼ f lmðjÞ ; ð2Þ where f depends on the layer.

. This sigmoid function is almost linear between 1 and 1, fð1Þ ¼ 1 and fð 1Þ ¼ 1. The constants are set according to the recommendations described in [33]. It is used for the first two hidden layers, which represent convolution of the input signal:

fð Þ ¼ 1:7159 tanh

- 2
- 3

: ð3Þ

. The classical sigmoid function is used for the two last layers:

1 1 þ exp

: ð4Þ

fð Þ ¼

l mðjÞ represents the scalar product between a set of input neurons and the weight connections between these neurons and the neuron number j in the map m in the layer l. We define lmðjÞ for the four layers. L1 and L2 are convolutional layers, respectively, in the space and time domain. L2, L3, and L4 can be considered as an MLP, where L2 is the input layer, L3 is the hidden layer, and L4 is the output layer.

For L1 and L2, we can notice that each neuron of the map sharesthesamesetofweights.Theneuronsoftheselayersare connected to a subset of neurons from the previous layer. Instead of learning one set of weights for each neuron, where the weights depend on the neuron position, the weights are learnedindependentlytotheircorrespondingoutputneuron.

. For L1:

1 mðjÞ ¼ wð1;m;0Þ þ i<NX

elec

Ii;jwð1;m;iÞ; ð5Þ

i¼0

where wð1;0;jÞ is a threshold. A set of weights wð1;m;iÞ with m fixed, 0 i < Nelec, corresponds to a spatial filter, i.e., a channel. In this layer, there are Nelec þ 1 weights for each map. This layer aims at finding the best electrodes combination for the

classification. The convolution represents spatial filters. The convolution kernel has a size of ½1 Nelec .

. For L2:

2 mðjÞ ¼ wð2;m;0Þþi<X13

x1mðj 13 þ iÞwð2;m;iÞ; ð6Þ

i¼0

where wð2;0;jÞ is a threshold. This layer transforms the signal of 78 values into six new values in L2. It reduces the size of the signal to analyze while applying an identical linear transformation for the six neurons of each map. This layer translates subsampling and temporal filters. The convolution kernel has a size of ½13 1 .

. For L3:

3ðjÞ ¼ wð3;0;jÞ þ i<X5Ns

Xk<6

x2iðkÞwð4;i;kÞ; ð7Þ

i¼0

k¼0

where wð4;0;jÞ is a threshold. Each neuron of L3 is connected to each neuron of L2. L2 and L3 are fully connected. In this layer, each neuron has NsNf þ 1 input weights. L3 contains 100ð5 6 NsÞ input connections.

. For L4:

4ðjÞ ¼ wð4;0;jÞ þ i<X100

x3ðiÞwð5;iÞ; ð8Þ

i¼0

where wð4;0;jÞ is a threshold. Each neuron of L4 is connected to each neuron of L3.

For each neuron, the input weights and the threshold are initialized with a standard distribution around

1=nðl;m;iÞNinput. We define nðl;m;iÞNinput as the number of inputs of nðl;m;iÞ. For layers L1 and L2, the learning rate is defined by

2 nðl;m;0ÞNsharedqﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃnðl;m;iÞNinput ; ð9Þ

¼

where nðl;m;0ÞNshared is the number of neurons that share the same set of weights and is a constant. For L1 and L2, each

neuron on each map shares the same number of weights, the learning rate takes into account the number of neurons that share the same set of weights.

For layers L3 and L4, the learning rate is

¼ q ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃnðl;m;iÞNinput : ð10Þ

The learning algorithm for tuning the weights of the network uses the classical backpropagation. The weights are corrected due to a gradient descent. Each training epoch is composed of 95 percent of the training database which is effectively used for learning, whereas the remaining 5 percent is dedicated to the validation database. The training stops once the least mean square error is minimized on the validation database. The output layer is composed of two neurons, which represent the two classes. x4ð0Þ and x4ð1Þ represent, respectively, the absence and the

presence of a P300 wave. During the test, the detection of a P300 wave is defined by

EðXÞ ¼

1 if x4ð1Þ > x4ð0Þ; 0; otherwise; ð11Þ

where X is the signal to classify and E is the classifier.

- 4 CLASSIFIERS

We present here seven classifiers based on the convolutional neural network that was presented in the previous section. This classifier will be used as the core of the different models. Among the presented classifiers, CNN-1, CNN-2, and CNN-3 are single classifiers whereas MCNN-1, MCNN-2, and MCNN-3 are based on a multiclassifiers strategy, like most of the efficient methods that achieve good results on P300 detection. For an input pattern P, we note E(P) the probability that a classifier determines P as being a P300 response (the values of the output layer are normalized to obtain the probabilities).

The first three classifiers are defined as follows:

- . CNN-1: For the first classifier, the training was achieved with the whole training database. CNN-1 is based on the convolutional neural network described in Section 3. This classifier is the reference for further comparisons.
- . CNN-2a: This classifier is identical to CNN-1, but it only uses eight electrodes instead of 64. The eight prefixed channels correspond to the location: FZ, CZ, PZ, P3, P4, PO7, PO8, and OZ in the international 10-20 system of measurement [28]. These channels were chosen in relation to the guideline provided during the BCI tutorial in Utrecht, Holland, 2008. This classifier aims at providing a realistic view of the accuracy that can be obtained with a relatively small number of electrodes. This classifier translates a more pragmatic approach toward the use of P300-BCIs.

. CNN-2b is identical to CNN-2A. However, the eight prefixed channels are determined in relation to the weight analysis of CNN-1 as described in Section 4.1. CNN-1 must be evaluated first to determine the ideal feature set for CNN-2B, i.e., the ideal set of electrodes.

- . CNN-3: This classifier is identical to CNN-1, but it only has one map in the first hidden layer which translates one single spatial filter. In this case, the classifier is based on only one channel. With this classifier, it is easier to interpret the meaning of the learned weights in the first hidden layer. This classifier can also provide information about the relevance of a multichannels classification scheme, where there exist several spatial filters for improving the classification.

The three multiclassifiers systems are based on the same classifiers: CNN-1. Only the training database differs for the three methods. For each multiclassifiers system, the average is used for fusing the output of each classifier [34].

. MCNN-1: The database is not homogeneous in the distribution of the patterns that represent a P300 and the others. In fact, the database contains five times more patterns that are not a P300. MCNN-1 is

composed of five classifiers. Each classifier is trained on a different database. Each training database contains all the P300 patterns and a fifth of the nonP300patternsfromthemaintrainingdatabase.Theset of patterns that does not represent a P300 is cut into fiveequalparts.Thus,eachclassifieristrainedwithan equal number of P300 and non-P300 patterns.

- . MCNN-2: The signals contained in the database can vary in quality and they can also represent different issues that one single classifier cannot model. For the particular problem of P300 detection, it is possible that the subject was not really focused at some times during the experiment. During these moments, the subject may not produce a reliable P300 or it might produce a P300 at an undesired moment. In such a case, we can expect the presence of outliers and many errors in the labeling. MCNN-2 is also composed of five classifiers. The training database is cut into five equal parts which represent five consecutive sequences in the EEG record. Each classifier of MCNN-2 is trained on one sequence. Such classifiers can model different types of P300 over time.
- . MCNN-3:Thissystemiscomposedofthreeclassifiers, like CNN-1. As the weights are initialized randomly, the creation of different classifiers like CNN-1 may lead to different classifiers. This classifier aims at improving the reliability of CNN-1. In case of nonimprovement, this classifier will show that the random initialization leads to equivalent classifiers.

- 4.1 Feature Selection for CNN-2b The choice of the electrodes in CNN-2b is based on the weight analysis of the first hidden layer in CNN-1. Indeed, as the first hidden layer corresponds to the creation of the channel combination, it is possible to extract information about the most relevant electrodes once the network is trained. When a weight is close to 0, then it means that its discriminant power is low. At the opposite, weights with a high absolute value denote a high discriminant power, and therefore, a relevant electrode for the classification. We define the power of the electrode i by

i ¼ jX¼N

s

j¼0

jwði;jÞj; ð12Þ

where 0 i < Nelec and wði; jÞ represents the weight of a link between any neuron of the map j to the electrode i at any time. i is the combination of the different maps that compose the network. It is possible to create a new classifier with a prefixed number of n electrodes by selecting n electrodes, which correspond to the n higher values. CNN-2b is instantiated with n ¼ 8, to be compared with CNN-2a.

- 4.2 Complexity For each convolutional layer, the weights are shared for every neuron within one map in the first two hidden layers. It therefore reduces the number of free parameters in the network. For each layer, the number of parameters (the number of weights and thresholds for all the neurons) is defined as follows:

- TABLE 2

- Results of the P300 Detection for Subject A

[Figure 6]

TABLE 3

- Results of the P300 Detection for Subject B

[Figure 7]

- . in L1, the number of free variables is NsðNelec þ 1Þ, e.g., 650, 90, and 65 parameters for CNN-1,2,3;
- . in L2, the number of free variables is 5Nsð13 þ 1Þ, e.g., 700, 700, and 70 parameters for CNN-1,2,3;
- . in L3, the number of free variables is 100 ð6 5Ns þ 1Þ, e.g., 30,100, 30,100, 3,010 parameters for CNN-1,2,3; and
- . in L4, the number of free variables is 2 ð100 þ 1Þ,

e.g., 202 parameters for CNN-1,2,3; where Nelec ¼ 64, and Ns ¼ 10.

Therefore, CNN-1,2,3 contain 31,652, 31,092, and 3,347 free variables, respectively.

The average training time was around 10 min on an Intel Core 2 Duo T7500 CPU for CNN-1. This time depends on the subject and mostly on the initial learning parameter , which was set to 0.2. The model was implemented in C++ without any special hardware optimization (multicore or GPU). Convolutional neural networks can be implemented by using GPU. Such implementation can provide a significant speedup for both learning and testing [35], [36].

- 5 RESULTS 5.1 P300 Detection The analysis of the basic P300 detection is not the main focus in works dedicated to BCI. In P300-BCI, the main task is the speller and the raw classification of the P300 waves is usually not specified. For the first time, we try to find some measurements related to the P300 detection, which could be considered as indexes correlated to the further character recognition. The classification results obtained for the six classifiers are given in Tables 2 and 3. For each method, the following information is provided: the number of true positive (TP), true negative (TN), false positive (FP), false negative (FN) in the test database. If we consider the P300 detection as a binary classification problem, the recognition rate (Reco.), presented in percent, is defined as ðTP þ TNÞ=NP, where NP ¼ TP þ TN þ FP þ FN, i.e., the total number of patterns. Other classical widely used

measures for evaluating the quality of results are presented in Tables 2 and 3:

TP TP þ TN

TP TP þ FP

Recall ¼

; ð13Þ Silence ¼ 1 Recall; Noise ¼ 1 Precision; ð14Þ

; Precision ¼

FP þ FN TP þ FN

Recall:Precision Precision þ Recall

Error ¼

; F-measure ¼ 2

: ð15Þ

The first observation is the large difference between the two subjects. Subject B allows getting better results for the classification. Besides, the methods have about the same ranking in relation to the recognition rate. For subject A, the best recognition and precision are obtained with CNN-1 and MCNN-3, whereas the best recall is achieved with MCNN-1 with a score of 0.69. The results of subject B respect the same dichotomy between the methods. For the single classifiers, the reduction of one channel or the use of only eight electrodes reduces the recognition rate of 0.9 and 2.29 percent, respectively, for subject A. For subject B, the difference is more significant, with a difference of about 4 percent in the recognition rate. The difference between CNN-1 and MCNN-1 is not significant as MCNN-1 is built with several CNN-1. Nevertheless, MCNN-1 offers a slight advantage in the recognition rate.

The main outcome of these first results is the difference between the precision and recall in relation to the methods. One interest is to find a link between one of these measurements and the results obtained in the second step for detecting the characters. One problem to solve is to define if it is the recall or the precision that is the most relevant feature for estimating the character recognition quality in the next classification step.

5.2 Network Analysis

The topology of the classifiers allows extracting information about the location of the best electrodes for each subject. For the layers that are not fully connected, it is possible to extract information from the connection weights. Figs. 5 and 6 represent the weights that define

[Figure 8]

- Fig. 4. Discriminant electrodes for subject A and subject B based on the weights of the first hidden later of CNN-3 and CNN-1 (FS).

[Figure 9]

- Fig. 6. Spatial filters obtained with CNN-1 for subject B.

[Figure 10]

- Fig. 5. Spatial filters obtained with CNN-1 for subject A.

each map of the first hidden layer of CNN-1. The parts in dark represent weights with a high absolute value. The parts in light correspond to weights that are around 0, i.e., the electrodes that correspond to locations that have a very low discriminant power. Although the analysis of the maps of CNN-1 can be difficult as there exist 10 channels, we observe some similarities between some maps of CNN-1 for the subject A and the map obtained with CNN-3. This is particularly evident in maps 3, 4, and 7, where it is possible to distinguish a precise location in the middle of the head that corresponds to PZ. For subject B, the information is more widely spread between CZ and POZ. It is interesting to note the difference of location for the same brain activity between two people. The accuracy of the P300 detection between both subjects could be explained by the location of the P300 response. The information is very dense in a particular location for

- subject A, whereas the dispersion of the information in
- subject B provides probably reliable results. The absolute values of the weights in the first hidden

layer of CNN-3 and the values of CNN-1 are displayed in Fig. 4. As CNN-3 has only one map that describes the channel combination, the weight set for this map is equivalent to the optimal spatial filter according to the gradient-based learning. Thus, it is possible to extract

TABLE 4 Electrode Ranking

[Figure 11]

directly information from the weights to determine the most discriminant electrodes for the classification. It is possible to observe some common points between and the weights from CNN-3. However, is more heterogeneous. The light gray values of CNN-3 show that it not possible to extract precisely the location where the P300 wave occurs.

- Table 4 presents the ranking of the chosen electrodes for creating CNN-2b. The electrodes are sorted from the most to the least discriminant electrode. The set of electrodes is closed to the set that was chosen for CNN-2a. Both subjects share PZ, CZ, CPZ, PO7, and PO8. The common electrodes with CNN-2a are CZ, PZ, PO7, and PO8.
- Table 5 represents the recognition rate in percent for each method and each subject for the character recognition problem. The number of epochs corresponds to the number of times a row/column has to flash on one character. The maximum number is 15, as described in the protocol experiment. When the number of epochs is n, it means that only the n first epochs are considered. With one epoch, there are only two P300 possible responses for determining a character: one for the x-coordinate and another for the y-coordinate. The evolution of the accuracy in relation to the number of epochs is not linear. Most of the characters are recognized within 10 epochs. It is noteworthy that adding more epochs does not necessarily improve accuracy. For example, the MCNN-1 method performed better after 12 epochs than 13 and the MCNN-3 approach performed better after 12 epochs than 11. Furthermore, the marginal benefit of additional epochs after the 10th epoch is minimal

for subject B, but not subject A. These observations may be noteworthy for P300-BCIs that use the variable averaging approach [37].

We note v, the vector containing the cumulated probabilities of the P300 detection for each of the 12 flashes. The first six values represent the six columns. The last six values represent the rows.

vðjÞ ¼ Xi¼n i¼1

EðPði; jÞÞ 1 j 12; ð16Þ

where Pði; jÞ is the pattern at the epoch i corresponding to the subject response for the flash j.

The coordinate of the character are defined by

- x ¼ argmax 1 i 6

vðiÞ; ð17Þ

- y ¼ argmax 7 i 12

vðiÞ: ð18Þ

The best accuracy is achieved by MCNN-1 with 95.5 percent. In the second position, CNN-1 and MCNN-3 both give the same accuracy. Compared to the P300 detection, the rank of the methods for the character recognition rate respects the order given by the recall. A high recall in the P300 detection involves a high accuracy in the character recognition. This observation should be used for further comparisons where only the recall could describe the quality of the classification and its impact for P300-BCIs.

Fig. 7 displays the information transfer rate (ITR), in bits per minute (bpm), in relation to the number of considered epochs, i.e., over the time needed for the recognition of a character. The ITR is common for measuring communication and control systems; it is used in BCI [38] and was first introduced by Shannon and Weaver [39]. The ITR is defined by

TABLE 5 Character Recognition Rate (in Percent) for the Different Classifiers

[Figure 12]

[Figure 13]

- Fig. 7. ITR (in bits per minute) in relation to the number of epochs.

60 P log2ðPÞ þ ð1 PÞ log2ðN1 P 1Þ þ log2ðNÞ T

ITR ¼

; ð19Þ

where p is the probability to recognize a character, N is the number of classes (N ¼ 36), and T is the time needed to recognize one character. T is defined by

T ¼ 2:5 þ 2:1n 1 n 15; ð20Þ

where n is the number of considered epochs. This time is established according to the protocol experiment, where each character epoch starts with a pause of 2.5 s and then each row/column is intensified for 100 ms with a pause of 75 ms (12 ð100 þ 75Þ ¼ 2;100). Contrary to the recognition rate that increases in relation to the number of epochs, the ITR takes into account the time needed for the recognition. The ITR is maximized with six epochs. However, we can observe that a fast ITR usually implies an averagerecognition rate. The question of an optimal recognition versus a fast ITR is opened and depends of the application. For instance, reliability is less important in a speller than in some robotic applications or emergencies.

Table 7 presents a comparison of the presented method with other systems. Among the CNN classifiers, only CNN-1 and MCNN-1 are presented. Each cell of the table contains the couple Reco./ITR that represents the character recognition rate in percent and the average ITR in bits per minute. The best recognition rate is achieved with the solution of Rakotomamonjy with the use of 15 epochs [16]. However, the proposed method offers the best recognition rate when only 10 epochs are used. One first observation is the difference between the methods over the number of epochs. One explanation can come from the number of characters to recognize, only 100, which limits the impact of the results. With a difference of 1 percent between two methods, it is impossible to qualify the impact of the classification quality.

Nevertheless, we can argue that the CNN method does not consider any electrode selection before the classification contrary to the other methods. All of the electrodes are used without any neuroscience knowledge about the best electrodes or some prior features selection. The classification is done directly on the EEG with few preprocessing. This advantage is relevant for its implementation in a real BCI system, where its all embedded approach can highlight the subject particularities without any tuning.

For a pragmatic BCI, the number of electrodes must be reduced. Table 6 presents a comparison between the best SVM solution and the CNN when both methods consider only eight electrodes as input. The selection of the electrodes given by CNN-2b gives about the same results as the predefined set of CNN-2a.

As the database is available for free online [43], we present eacherrorforbothsubjectsforfurthercomparisonsinTable8. We can note that the errors can be explained, as each error is near the expected character in the speller layout. Most of the time, it is either on the same row or the same column. The creation of a new paradigm that would include flashing diagonals, for instance, could improve the character recognition by cross-validating the P300 responses.

TABLE 6 Comparison of the Recognition Rate (in Percent) with Only Eight Electrodes as Input Feature

[Figure 14]

TABLE 7 Comparison of the Recognition Rate and the ITR with Other Results in the Literature

[Figure 15]

- 6 DISCUSSION

The question arises whether the quality of the classification impairs with a real use in a BCI application. It is important to limit the prospects of this paper for BCI. These results were obtained with only two subjects. In addition, these two subjects of the database are not representative for P300-BCI. These two subjects have an average P300 response compared to other studies like the BCI competition 2003 [44]. In this competition, for the same problem, many participants got a perfect accuracy for the character recognition problem for a low number of epochs: 6 or 5.

Therefore, the data from the third BCI competition are noteworthy primarily because they present an excellent challenge. Researchers can explore different approaches and push the limits of classification approaches. The database has two main interests. First, it forces the system to reach the limit of the P300 detection. It can extend the potential number of persons who can use a P300-BCI. Second, it is an excellent challenge for the machine learning community. Unlike a well-known problem like character recognition, the gap between research and real applications is still important for BCI and many improvements shall be done. The current limits come both from the noninvasive input signal and the algorithms used for the detection of particular brain responses.

While many pattern recognition methods are used in the BCI field, the question of the ground truth creation arises. Indeed, the main interest of BCI is to detect brain activity, which can be related to stimuli or not. In the case of mental imagery, the user has to imagine moving the left/right hand, for example. For the detection of visual evoked potential, like the P300 waves or steady-state visual evoked potentials (SSVEPs), the user has to focus on some visual stimuli (flashing light for P300, flickering light for SSVEP).

TABLE 8 Confusion of Character Recognition

[Figure 16]

The ground truth is usually determined on what the subject has to perform. Its creation can therefore be tricky as it is impossible to know what the subject is thinking or where the subject is exactly focusing without the use of an eye tracker. For instance, in the P300 speller, it is possible that the subject may not have always focused on the expected target. In addition, the user can be sensitive to the peripherical lights around the target, where a P300 wave may also occur. This effect is suggested in the errors in the character recognition that are described in the previous section. The possibility of outliers and mislabeled patterns is high. Further works should consider these effects during learning. For instance, the surrounding flashes around a target could not be taken into account during the classifier learning as the probability of mislabeling the corresponding brain response can be high, i.e., a P300 wave can occur when it is not desired.

One of the most important parameters in BCI is the ITR, whichdependsonthetime.TheITRpresentedintheprevious section suggeststhat the optimal number of epochs should be around six. Some investigations should be carried out in the links between the number of classes in the P300 speller and the number of epochs to get the best ITR.

The interest of convolutional neural networks is double. First, it allows a high performance in the classification. The CNN approach can be qualified as almost naive as the preprocessing steps are limited. It just classifies a signal without directly considering the usual shape of the expected signal to detect, i.e., the deflection after 300 ms of the P300 wave is not used. Second, they can allow deeper analysis of brain activity. During the learning step, particular features can be discovered. Whereas most of the other techniques separate the different parts of the classification (features selection, spatial filters, ...), a CNN can extract all of the needed information during its learning. The weight semantic in the network can carry out other relevant information that may still be unknown to neuroscience.

Whereas some of the techniques use specific preprocessing tools for removing artifacts such as eye blinking and other muscle movements, the CNN solution got excellent results while being invariant to such noise. The CNN can still be improved. The differences between CNN-1 and CNN-3 advocate the critical choice of the topology. The spatial filters in the first hidden layer were created in one step and they don’t include any contextual information about the electrode placement. The first hidden layer could be decomposed into several other layers that describe a hierarchical view of the electrodes from Fig. 2. Instead of

processing all of the electrodes together in one layer, several layers could successively reduce the number of channels from 64 to 1. Indeed, models such as LeNet-5 [32] and LeNet-6 [20] have a deep architecture for learning progressively higher level features. One challenge is to determine the key layers and the best topology.

- 7 CONCLUSION

A new approach for P300-BCI classification has been presented. This model is based on a convolutional neural network. Its accuracy is equivalent to the best current method on the Data set II of the third BCI competition [16]. It outperforms the best method in two situations: first, when the number of electrodes is restricted to 8; second, when the number of considered epochs is 10. In addition, the classifier does not consider a prior set of selected features or high-level features as input, contrary to the other solution, and it provides some tools throughout the learned weights for interpreting the brain signals. As expected, the combination of different classifiers is the best strategy for obtaining the best results. The recall of the P300 detection is the main feature that dictates the overall performance of the P300 speller. The detection of P300 waves remains a very challenging problem for both the machine learning and neuroscience communities. It possesses a large variability over subjects. As its presence is unsure, it presents high potential of outliers for the classification. Further works will deal with the links between the P300 detection and its impact for the character recognition problem in relation to the number of epochs.

ACKNOWLEDGMENTS

The authors would like to thank Dr. Brendan Allison and the reviewers for their comments. This research was supported by a Marie Curie European Transfer of Knowledge grant BrainRobot, MTKD-CT-2004-014211, within the Sixth European Community Framework Program.

REFERENCES

- [1] B.Z. Allison, E.W. Wolpaw, and J.R. Wolpaw, “Brain-Computer Interface Systems: Progress and Prospects,” Expert Rev. Medical Devices, vol. 4, no. 4, pp. 463-474, 2007.
- [2] N. Birbaumer and L.G. Cohen, “Brain-Computer Interfaces: Communication and Restoration of Movement in Paralysis,” J. Physiology—London, vol. 579, no. 3, pp. 621-636, 2007.
- [3] A. Kostov and M. Polak, “Parallel Man-Machine Training in Development of EEG-Based Cursor Control,” IEEE Trans. Rehabilitation Eng., vol. 8, no. 2, pp. 203-205, June 2000.
- [4] N. Birbaumer, N. Ghanayim, T. Hinterberger, I. Iversen, B. Kotchoubey, A. Ku¨bler, J. Perelmouter, E. Taub, and H. Flor, “A Spelling Device for the Paralysed,” Nature, vol. 398, pp. 297-298, 1999.
- [5] B. Blankertz, G. Dornhege, S. Lemm, M. Krauledat, G. Curio, and K.-R. Mu¨ller, “The Berlin Brain-Computer Interface: EEG-Based Communication without Subject Training,” IEEE Trans. Neural Systems and Rehabilitation Eng., vol. 14, no. 2, pp. 147-152, June 2006.
- [6] F. Lotte, M. Congedo, A. Lecuyer, F. Lamarche, and B. Arnaldi, “A Review of Classification Algorithms for EEG-Based Brain-Computer Interfaces,” J. Neural Eng., vol. 4, pp. R1-R13, 2007.
- [7] K.-R. Mu¨ller, M. Krauledat, G. Dornhege, G. Curio, and B. Blankertz, “Machine Learning Techniques for Brain-Computer Interfaces,” Biomedical Technology, vol. 49, no. 1, pp. 11-22, 2004.

- [8] K.-R. Mu¨ller, M. Tangermann, G. Dornhege, M. Krauledat, G. Curio, and B. Blankertz, “Machine Learning for Real-Time SingleTrial EEG-Analysis: From Brain-Computer Interfacing to Mental State Monitoring,” J. Neuroscience Methods, vol. 167, no. 1 pp. 82-90, 2008.
- [9] C.W. Anderson, S.V. Devulapalli, and E.A. Stolz, “Determining Mental State from EEG Signals Using Parallel Implementations of Neural Networks,” Proc. IEEE Workshop Neural Networks for Signal in Processing, pp. 475-483, 1995.
- [10] H. Cecotti and A. Gra¨ser, “Time Delay Neural Network with Fourier Transform for Multiple Channel Detection of Steady-State Visual Evoked Potential for Brain-Computer Interfaces,” Proc. European Signal Processing Conf., 2008.
- [11] T. Felzer and B. Freisieben, “Analyzing EEG Signals Using the Probability Estimating Guarded Neural Classifier,” IEEE Trans. Neural Systems and Rehabilitation Eng., vol. 11, no. 4, pp. 361-371, Dec. 2003.
- [12] E. Haselsteiner and G. Pfurtscheller, “Using Time Dependent Neural Networks for EEG Classification,” IEEE Trans. Rehabilitation Eng., vol. 8, no. 4, pp. 457-463, Dec. 2000.
- [13] N. Masic and G. Pfurtscheller, “Neural Network Based Classification of Single-Trial EEG Data,” Artificial Intelligence in Medicine, vol. 5, no. 6, pp. 503-513, 1993.
- [14] N. Masic, G. Pfurtscheller, and D. Flotzinger, “Neural NetworkBased Predictions of Hand Movements Using Simulated and Real EEG Data,” Neurocomputing, vol. 7, no. 3, pp. 259-274, 1995.
- [15] B. Blankertz, G. Curio, and K.-R. Mu¨ller, “Classifying Single Trial EEG: Towards Brain Computer Interfacing,” Advances in Neural Information Processing Systems, T.G. Diettrich, S. Becker, and Z. Ghahramani, eds., vol. 14, pp. 157-164, MIT Press, 2002.
- [16] A. Rakotomamonjy and V. Guigue, “BCI Competition III: Data Set II—Ensemble of SVMs for BCI p300 Speller,” IEEE Trans. Biomedical Eng., vol. 55, no. 3, pp. 1147-1154, Mar. 2008.
- [17] B. Obermaier, C. Guger, C. Neuper, and G. Pfurtscheller, “Hidden Markov Models for Online Classification of Single Trial EEG data,” Pattern Recognition Letters, vol. 22, no. 12, pp. 1299-1309, 2001.
- [18] S. Zhong and J. Gosh, “HMMs and Coupled HMMs for MultiChannel EEG Classification,” Proc. IEEE Int’l Joint Conf. Neural Networks, vol. 2, pp. 1154-1159, 2002.
- [19] A. Hiraiwa, K. Shimohara, and Y. Tokunaga, “EEG Topography Recognition by Neural Networks,” IEEE Eng. in Medicine and Biology Magazine, vol. 9, no. 3, pp. 39-42, Sept. 1990.
- [20] Y. Bengio and Y. LeCun, “Scaling Learning Algorithms towards AI,” Large-Scale Kernel Machines, L. Bottou, O. Chapelle, D. DeCoste, and J. Weston, eds., MIT Press, 2007.
- [21] P.Y. Simard, D. Steinkraus, and J.C. Platt, “Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis,” Proc. Seventh Int’l Conf. Document Analysis and Recognition, pp. 958-962, 2003.
- [22] S. Sukittanon, A.C. Surendran, J.C. Platt, and C.J.C. Burges, “Convolutional Networks for Speech Detection,” Proc. Eighth Int’l Conf. Spoken Language Processing, pp. 1077-1080, 2004.
- [23] D.J. Krusienski, E.W. Sellers, D. McFarland, T.M. Vaughan, and J.R. Wolpaw, “Toward Enhanced P300 Speller Performance,” J. Neuroscience Methods, vol. 167, pp. 15-21, 2008.
- [24] E. Donchin, K.M. Spencer, and R. Wijesinghe, “Assessing the Speed of a P300-Based Brain-Computer Interface,” IEEE Trans. Neural Systems and Rehabilitation Eng., vol. 8, no. 2, pp. 174-179, June 2000.
- [25] L. Farwell and E. Donchin, “Talking Off the Top of Your Head: Toward a Mental Prosthesis Utilizing Event-Related Brain Potentials,” Electroencephalography and Clinical Neurophysiology, vol. 70, pp. 510-523, 1988.
- [26] B. Blankertz, K.-R. Mu¨ller, D.J. Krusienski, G. Schalk, J.R. Wolpaw, A. Schlo¨gl, G. Pfurtscheller, J.R. Milla´n, M. Schro¨der, and N. Birbaumer, “The BCI Competition. III: Validating Alternative Approaches to Actual BCI Problems,” IEEE Trans. Neural Systems and Rehabilitation Eng., vol. 14, no. 2, pp. 153-159, June 2006.
- [27] G. Schalk, D.J. McFarland, T. Hinterberger, N. Birbaumer, and J. Wolpaw, “BCI2000: A General-Purpose Brain-Computer Interface (BCI) System,” IEEE Trans. Biomedical Eng., vol. 51, no. 6, pp. 10341043, June 2004.
- [28] G.-E. Sharbrough, R.P. Chatrian, H. Lesser, M. Luders, T.W. Nuwer, and T.W. Picton, “American Electroencephalographic Society Guidelines for Standard Electrode Position Nomenclature,” J. Clinical Neurophysiology, vol. 8, pp. 200-202, 1991.

- [29] L. Breiman, “Bagging Predictors,” Machine Learning, vol. 26, no. 2 pp. 123-140, 1996.
- [30] U. Hoffmann, G. Garcia, J.-M. Vesin, K. Diserens, and T. Ebrahimi, “Boosting Approach to p300 Detection with Application to BrainComputer Interfaces,” Proc. IEEE Conf. Neural Eng., pp. 97-100, 2005.
- [31] Y. LeCun, F.-J. Huang, and L. Bottou, “Learning Methods for Generic Object Recognition with Invariance to Pose and Lighting,” Proc. IEEE CS Conf. Computer Vision and Pattern Recognition, 2004.
- [32] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-Based Learning Applied to Document Recognition,” Proc. IEEE, vol. 86, no. 11, pp. 2278-2324, Nov. 1998.
- [33] Y. LeCun, L. Bottou, G. Orr, and K.-R. Mu¨ller, “Efficient Backprop,” Neural Networks: Tricks of the Trade, G. Orr and K. Muller, eds., Springer, 1998.
- [34] J. Kittler, M. Hatef, R.P.W. Duin, and J. Matas, “On Combining Classifiers,” IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 20, no. 3, pp. 226-239, Mar. 1998.
- [35] K. Chellapilla, S. Puri, and P.Y. Simard, “High Performance Convolutional Neural Networks for Document Processing,” Proc. 10th Int’l Workshop Frontiers in Handwriting Recognition, 2006.
- [36] R.J. Meuth and D.C. Wunsch, “Approximate Dynamic Programming and Neural Networks on Game Hardware,” Proc. Int’l Joint Conf. Neural Networks, 2007.
- [37] H. Serby, E. Yom-Toy, and G.F. Inbar, “An Improved P300-Based Brain-Computer Interface,” IEEE Trans. Neural Systems and Rehabilitation Eng., vol. 13, no. 1, pp. 89-98, Mar. 2005.
- [38] J.R. Wolpaw, N. Birbaumer, D.J. McFarland, G. Pfurtscheller, and T.M. Vaughan, “Brain-Computer Interfaces for Communication and Control,” Clinical Neurophysiology, vol. 113, pp. 767-791, 2002.
- [39] C.E. Shannon and W. Weaver, The Mathematical Theory of Communication. Univ. of Illinois Press, 1964.
- [40] B. Blankertz, “BCI Competition III—Final Results,” http:// ida.first.fraunhofer.de/projects/bci/competition_iii/results/, 2008.
- [41] U. Hoffmann, G. Garcia, J.M. Vesin, and T. Ebrahimi, “Application of the Evidence Framework to Brain-Computer Interfaces,” Proc. Conf. IEEE Eng. Medicine and Biology Soc., vol. 1, pp. 446-449, 2004.
- [42] N. Liang and L. Bougrain, “Averaging Techniques for Single-Trial Analysis of Oddball Event-Related Potentials,” Proc. Fourth Int’l BCI Workshop and Training Course, pp. 44-49, 2008.
- [43] B. Blankertz, “BCI Competition III Webpage,” http://ida.first. fraunhofer.de/projects/bci/competition_iii, 2008.
- [44] B. Blankertz, K.-R. Mu¨ller, G. Curio, T.M. Vaughan, G. Schalk, J.R. Wolpaw, A. Schlo¨gl, C. Neuper, G. Pfurtscheller, T. Hinterberger, M. Schro¨der, and N. Birbaumer, “The BCI Competition 2003: Progress and Perspectives in Detection and Discrimination of EEG Single Trials,” IEEE Trans. Biomedical Eng., vol. 51, no. 6, pp. 10441051, June 2004.

[Figure 17]

Hubert Cecotti received the MSc and PhD degrees in computer science from the Universities of Nancy, France, in 2002 and 2005, respectively. Since 2008, he has been a research scientist in the Institute of Automation, Bremen University, Germany, where he has worked on EEG signal processing and braincomputer interfacing on the European project Brainrobot. In 2006 and 2007, he was a lecturer in computer science at the University Henri

Poincare´ and ESIAL, Nancy, France. His research interests include neural networks, multiclassifiers systems, character recognition, and brain-computer interfaces.

[Figure 18]

Axel Gra¨ser received the diploma degree in electrical engineering from the University of Karlsruhe, Germany, in 1976, and the PhD degree in control theory from the Technical University of Darmstadt, Germany, in 1982. Since 1994, he has been the head of the Institute of Automation, University of Bremen, Germany. From 1982 to 1990, he was the head of the Control and Software Department of Lippke GmbH, Germany. From 1990 to 1994,

he was a professor of control systems, process automation, and realtime systems at the University of Applied Sciences, Koblenz, Germany. He is the manager and coordinator of the European Union Project BRAIN. His research interests include service robotics, brain-computer interfaces, visual servoing, digital image processing, and augmented reality.

. For more information on this or any other computing topic, please visit our Digital Library at www.computer.org/publications/dlib.

