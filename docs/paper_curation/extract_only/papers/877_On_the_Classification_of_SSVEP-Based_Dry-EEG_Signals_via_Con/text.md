# On the Classiﬁcation of SSVEP-Based Dry-EEG Signals via Convolutional Neural Networks

Nik Khadijah Nik Aznan∗†, Stephen Bonner∗, Jason D. Connolly‡ Noura Al Moubayed∗ and Toby P. Breckon∗† Department of {∗Computer Science, †Engineering, ‡ Psychology} Durham University, Durham, UK

## arXiv:1805.04157v2[cs.HC]2Aug2018

Abstract—Electroencephalography (EEG) is a common signal acquisition approach employed for Brain-Computer Interface (BCI) research. Nevertheless, the majority of EEG acquisition devices rely on the cumbersome application of conductive gel (so-called wet-EEG) to ensure a high quality signal is obtained. However, this process is unpleasant for the experimental participants and thus limits the practical application of BCI. In this work, we explore the use of a commercially available dryEEG headset to obtain visual cortical ensemble signals. Whilst improving the usability of EEG within the BCI context, dry-EEG suffers from inherently reduced signal quality due to the lack of conduit gel, making the classiﬁcation of such signals signiﬁcantly more challenging.

In this paper, we propose a novel Convolutional Neural Network (CNN) approach for the classiﬁcation of raw dryEEG signals without any data pre-processing. To illustrate the effectiveness of our approach, we utilise the Steady State Visual Evoked Potential (SSVEP) paradigm as our use case. SSVEP can be utilised to allow people with severe physical disabilities such as Complete Locked-In Syndrome or Amyotrophic Lateral Sclerosis to be aided via BCI applications, as it requires only the subject to ﬁxate upon the sensory stimuli of interest. Here we utilise SSVEP ﬂicker frequencies between 10 to 30 Hz, which we record as subject cortical waveforms via the dry-EEG headset. Our proposed end-to-end CNN allows us to automatically and accurately classify SSVEP stimulation directly from the dry-EEG waveforms. Our CNN architecture utilises a common SSVEP Convolutional Unit (SCU), comprising of a 1D convolutional layer, batch normalization and max pooling. Furthermore, we compare several deep learning neural network variants with our primary CNN architecture, in addition to traditional machine learning classiﬁcation approaches. Experimental evaluation shows our CNN architecture to be signiﬁcantly better than competing approaches, achieving a classiﬁcation accuracy of 96% whilst demonstrating superior cross-subject performance and even being able to generalise well to unseen subjects whose data is entirely absent from the training process.

I. INTRODUCTION

Electroencephalography (EEG) is the most prominent data acquisition approach in BCI, owing to its non-invasive nature, relative ease of use and exquisite temporal resolution [1], [2]. Traditionally, the electrodes used for EEG are placed on the scalp with conductive gel (wet-EEG) in order to lower the impedance between the electrodes and the skin [3]. The impedance values in EEG signals are a measurement of how good the conductivity is between the electrode and the skin. The lower the value of impedance, the better the electrode and the skin contact thus improving overall EEG signal quality [4], [5].

The major drawback of wet-EEG is the required gel application owing to the Ag/AgCl electrodes, consequently resulting in relatively substantial preparation time, scalp discomfort and additional time required to remove the gel after the experimental protocol [5]. Furthermore, the gel will dry over a certain time frame, thus somewhat limiting the experimental data acquisition interval [4]. Moreover, classical wet-EEG requires some speciﬁc experimental conditions like a Faraday cage (a physical shield using conductive material) which reduces the effect of external electromagnetic interference in terms of signal noise [3]. This limits the application of BCI using wet-EEG to strict experimental operating conditions. By contrast, a dry-EEG headset offers an alternative approach alleviates these limitations in terms of skin preparation, stable connectivity and comfort during experimentation in addition to ready adaptability to different head sizes [6], [7]. However, the major drawback is the relatively higher impedance values, as compared to wet-EEG [8], thus making it difﬁcult to reduce the EEG signal noise and unwanted artefacts. This results in a substantially more challenging signal decoding and classiﬁcation task.

In this study, we are using the commercially available Quick-20 dry EEG headset from Cognionics Inc. (San Diego, USA) with 20 dry-EEG sensors (10-20 sensor layout compliant). The system is employed without the need for skin preparation and it is both portable and wireless [6]–[9]. This headset comes with individual local active shields that eliminate the need for the rigid experimental condition [6], [10]. In our experiments, we collect dry-EEG signals with SSVEP as the neuro-physiological responses. SSVEP has the feature of frequency tagging, which enables the measurement of neural activity in response to a ﬂickering stimuli which the subject is ﬁxated upon, even if the subject is not paying full conscious attention to the stimuli [11]. It is considered to be the most suitable type of stimuli to be used for effective high throughput BCI as SSVEP can provide high Information Transfer Rate (ITR) neural signals with minimal subject training [12].

In this study, we investigate the use of a deep neural network, speciﬁcally a CNN, to perform the classiﬁcation of SSVEP frequencies in dry-EEG data. CNN are a subset of neural networks, which learn to differentiate between classes in data by extracting unique features across multiple layers of convolutional transformation [13]. In the convolution layer, the input is convolved via kernels (ﬁlters) to obtain feature maps

[14]. This process removes the requirement for hand-crafted feature extraction as well as common signal pre-processing steps, as raw data samples can be used as a direct input to the model [14], [15]. This property provides a critical advantage as the potential exists for salient EEG signals or features to be excluded or missed when using traditional pre-processing based approaches [16].

We evaluate the performance of our proposed CNN architecture at classifying dry-EEG SSVEP signals across a four class stimuli problem collected from a single subject and highlight the vastly superior performance when compared to baseline classiﬁers including the Support Vector Machine (SVM), Linear Discriminant Analysis (LDA), Minimum Distance to Mean (MDM) and a Recurrent Neural Network (RNN). Furthermore, we explore the use of the same CNN architecture to examine both multiple subject, exploring both within subject and across subject performance [16]. Finally, to test the ability of the CNN to generalise across unseen subjects, we explore the performance when testing upon a subject for which no sample data is present within the training dataset.

In summary, the major contributions of this study are:

- • An end-to-end deep learning CNN architecture to perform the classiﬁcation of raw dry-EEG SSVEP data without the need for manual pre-processing or feature extraction (the ﬁrst study to do so with the accuracy achieved: 96%).
- • A demonstrable model that achieves generalisation across subjects during training in contrast to earlier EEG BCI work in the ﬁeld (accuracy: 78%).
- • An approach with the ability to generalise to entirely unseen subjects with no additional training, raising the potential for subject-independent BCI applications.

II. RELATED WORK

In [7], a 32-channel dry-EEG was used on subjects in which they ﬁxated on 11 and 12 Hz SSVEP stimuli during walking trials. The performance and the quality of cortical signals between the wet-EEG and dry-EEG during locomotion were compared. From their experiments, wet-EEG performed better as compared to the dry-EEG by 4% to 10% in accuracy for standing and walking at different speeds, respectively.

The study of foot motor imagery has been carried out in [9] to trigger a lower limb exoskeleton while using the same 20channel dry-EEG headset we use here. The aim of the paper is to have the quick setup system for asynchronous motor imagery BCI as offered by using the dry-EEG headset.

Deep learning approaches have been used in many different BCI applications, akin to motor imagery [15] as well as the classiﬁcation of SSVEP signals. In [12], the authors control an exoskeleton via a visual stimulus generator that had ﬁve different frequency LEDs to control ﬁve different behaviours for static and ambulatory experiments. They used eight wetEEG electrodes to measure the SSVEP signals with Canonical Correlation Analysis (CCA), Multivariate Synchronization Index (MSI) and CCA with k-Nearest Neighbours (CCA-KNN) used to compare the classiﬁcation result with three proposed Neural Network (NN) methods: CNN-1 (3 layer network),

CNN-2 (4 layer network) and a fully-connected NN. The data from the stimuli is pre-processed for all approaches with the CNN-1 method providing the best accuracy results across both EEG data genres.

A ﬁve class SSVEP signal problem is classiﬁed using both traditional machine learning approaches and deep learning [17]. The authors analyse the dataset from the Physionet [18] which used the traditional wet-EEG with ﬁve ﬂickering stimuli frequencies. These authors proposed CNN and RNN with Long-short Term Memory (LSTM) for the deep learning methods against traditional classiﬁers like k-Nearest Neighbour (kNN), Multi-layer Perceptron (MLP), decision trees and SVM. Within all the classiﬁers, CNN outperformed other approaches with a mean accuracy of 69.03% and within the traditional classiﬁers, SVM provided the best overall accuracy.

The authors in [16] introduce EEGNet, a CNN model for wet-EEG data across paradigms. The paper includes four datasets for four different paradigms (P300 Event-Related Potential, Error-Related Negativity, Movement-Related Cortical Potential, and Sensorimotor Rhythm). All the datasets come from different sources with different data sizes. These authors pre-process the data before training the datasets using different approaches including both shallow CNN and deep CNN for within subject classiﬁcation and across subject classiﬁcation and for all four paradigms. Inconclusively, the results demonstrate that different paradigms perform differently for every approach.

In contrast to these earlier works, we explicitly consider an end-to-end approach, without the need for EEG signal pre-processing, to tackle single subject, multiple subject and unseen subject SSVEP-based dry-EEG signal classiﬁcation challenges.

III. METHODOLOGY

In this section, we explore the creation of a machine learning model, speciﬁcally a deep CNN, in order to perform accurate classiﬁcation of dry-EEG data. We include several baseline studies in order to compare the performance of the classiﬁcation accuracy. We also detail the methodology adopted for the experimental SSVEP data collection.

A. Experimental Setup

In this work, we utilise SSVEP as the neuro-physiological response, measured via dry-EEG. The subjects sit in front of a 60Hz refresh rate LCD monitor whilst wearing the dry-EEG headset. We record the data from a range of SSVEP stimuli frequencies; 10, 12, 15 and, 30 Hz [11] using PsychoPy for SSVEP stimuli presentation [19]. The stimuli corresponding to the different ﬂicker frequencies were presented on the primary computer. In order to assist with real time processing further along the analysis pipeline, the cortical signals were streamed via the data acquisition software to a secondary computer and sent back to the primary computer. The communication between the different hardware components is shown in Figure 1.

The dry-EEG headset provides 19 channels and A2, reference and ground as shown in Figure 1 (highlighted in blue).

[Figure 1]

- Fig. 1: Experiment setup and the location of the electrodes of dry-EEG (highlighted in blue)

The 20-channel (Cognionics Inc.) sensor montage [20] has been coregistered with the MNI Colin27 brain (Montreal Neurological Institute Colin 27 atlas). Average sensor locations were obtained by averaging 3-D digitized (ELPOS, Zebris Medical GmbH) electrode locations from ten individuals. Electrode labels are assigned based on the nearest neighbour mapping to the standard 10/5 montage. Nas, LPA, and RPA denote nasion and left/right preauricular ﬁducials [6].

During the experiments, we collect data over the parietal and occipital cortex (P7, P3, Pz, P4, P8, O1 and O2) [7], frontal centre (Fz) and A2 reference at 500 Hz sampling rate across four subjects. The data for subject one (S01) consists of 100 trials of each of the 4 SSVEP classes investigated. For the additional three subjects, we only record 20 trials instead. Each trial ﬂickers the LCD screen for three seconds. The data acquisition software used to monitor and record the signals provides real-time measurement of the impedances for the entire duration of the experiment, thus ensuring good quality EEG signals are recorded.

[Figure 2]

(a) 10Hz Signal (b) 12Hz Signal

[Figure 3]

[Figure 4]

(c) 15Hz Signal (d) 30Hz Signal

[Figure 5]

- Fig. 2: Illustrative raw signal data as captured from dry-EEG Nevertheless, the primary challenge associated with the

classiﬁcation of dry-EEG signals is the higher noise ratio as compared to the traditional wet-EEG system, owing to the relatively higher impedance values. This noise can be

seen in Figure 2 which shows the seven distinct dry-EEG data channels across the four SSVEP frequencies we are investigating.

B. Convolutional Neural Network Model Design

Signal processing is one of the primary components in the ﬁeld of BCI and it acts as the translation between the raw EEG cortical signals to a speciﬁc desirable decision or application [3]. Traditionally, this requires the use of manual pre-processing and feature extraction stages to transform the data into a format suitable for down-stream prediction tasks. By contrast in this work, we explore the use of a deep convolutional neural network to perform this translation process in an end-to-end fashion1. We explore whether or not a CNN can perform accurate classiﬁcation of SSVEP target class frequencies on raw dry-EEG data, without the need for manual pre-processing nor feature extraction as found in contemporary work [13]. CNN have demonstrated state-ofthe-art results in many image processing tasks, when being used on two dimensional image data [14]. However, there is growing evidence that CNN can be used to process time-series data, when passing a ﬁlter over the time dimension, often outperforming recurrent models designed speciﬁcally for such temporal data tasks [21]. As EEG data represents time-series data, we make use of a 1D CNN model to classify the dryEEG data.

[Figure 6]

Fig. 3: Our proposed 1D CNN architecture including our proposed SSVEP Convolutional Unit (SCU, highlighted in pink)

The structure of the CNN used in this work is displayed in Figure 3 in which we have our SSVEP Convolutional Unit (SCU) comprising of a triplicate layer of a 1D convolutional layer, batch normalization and max pooling layer operations. These SCU form the common computational building blocks of the CNN architectures used for dry-EEG signal decoding in this study. Our CNN architecture has a large initial ﬁlter to capture the frequencies we are interested in classifying in the dry-EEG data. We also make use of batch normalization to help counterbalance the noisy EEG data. Once the data has been transformed via the convolutional ﬁlter, the actual classiﬁcation of the EEG signal is performed via a softmax

1Implemented using the Pytorch library (http://pytorch.org/).

function (highlighted in black in Figure 3) in the ﬁnal layer. The softmax function takes as input the feature vector x, generated by the CNN fCNN(y|x) and computes the conditional probability of producing the label y as:

exp(fCNN(y|x)) |Y | y ∈Y exp(fCNN(y |x))

, (1)

softmax(y|x) =

where Y is the set of all labels in the dataset. The loss function the model minimised during training is that of categorical cross-entropy (CCE), which will measure the distance between the output distribution of yˆ ∈ fCNN and y ∈ Y as:

N

1 N

(ynlog(ˆyn)+(1−y)log(1−yˆn)), (2)

CCE(y,yˆ) = −

n=1

where N is the total number of training samples. The model is trained using the ADAM gradient descent algorithm [22], for 100 epochs with a mini-batch size of 32. We also utilise L2 weight decay to help prevent over-ﬁtting by penalising the network for having large weights, meaning that the ﬁnal objective of our model for optimising is:

### Loss = CCE(y,yˆ) + λ||fCNN(w)||22, (3)

where w are the weights of the network and λ is a user controllable scaling parameter, set to 10−4 for this work. C. Baselines

To validate the effectiveness of our proposed approach, we compare with traditional classiﬁers and other deep learning models. The traditional classiﬁers used require pre-processing and feature extraction prior to the classiﬁcation stage. As such, the raw signals will process via the following steps:downsampled to 250Hz, referencing to the frontal centre sensor signals (Fz), notch ﬁltered at 50Hz to remove line signal noise and bandpass ﬁltered between 9 to 100 Hz. As a result, pre-processing is used to remove the unwanted signals such as power-line noise, and to focus on the signals between the desirable range [3]. These ﬁltered signals are then utilised as the input for the feature extraction stage. Based on the recent comparative review of [23], we select the Riemannian approach for feature extraction [24] which utilises covariance matrix and tangent space features which estimate a feature vector in R9.

Based on the result from [17], SVM is the optimal traditional classiﬁer for EEG data. Therefore we use SVM as one of our baseline classiﬁers with a Gaussian and linear kernel [1]. For further comparison purposes, we also compare with Linear Discriminant Analysis (LDA) and Minimum Distance to Mean (MDM), both frequent choices for EEG analyses [23]. To compare with other leading neural network approaches, we also compare with several Recurrent Neural Network (RNN) models [25] including vanilla RNN, Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRU), which have also been assessed for EEG classiﬁcation in previous study [17].

IV. RESULTS AND DISCUSSION

In this section, we present detailed experimental evaluation demonstrating the ability of our approach to accurately classify SSVEP signals in dry-EEG data. All the presented results are produced using 10-fold cross validation, with models which were initially optimised using hyperparameters chosen via a grid-search over a validation set. The key hyperparameters which are common across all the networks are L2 weight decay scaling 0.001, dropout level 0.5 and 0.001 for CNN and other deep approaches respectively2. For the CNN, the hyperparameters utilised are: convolution kernel size 1x10, kernel stride 4, maxpool kernel size 2, and ReLU as the activation function. The dataset and experimental setup are detailed previously in Section III-A.

- A. Single Subject Classiﬁcation

The results for the classiﬁcation of the data of a single subject (S01) are presented in Table I. The table highlights the accuracy of our proposed CNN approach against all the baselines discussed in Section III-C. The results for the traditional approaches, are presented with and without preprocessing. Without pre-processing, we perform feature extraction only before classiﬁcation with the traditional baseline approaches. Overall, the results show that, even without any pre-processing of the data, our CNN approach demonstrates superior performance over the baselines. The confusion matrix obtained from the classiﬁcation of S01 using the CNN is presented in Figure 4a, which shows very strong accuracy across all classes.

Method

Accuracy

Pre-processing Without

CNN - 0.96±0.02 Vanilla RNN - 0.91±0.05

LSTM - 0.57±0.30

GRU - 0.90±0.06 SVMGaussian 0.92±0.01 0.86±0.01

SVMLinear 0.94±0.01 0.83 ±0.02 MDM 0.76±0.01 0.80±0.02 LDA 0.90±0.01 0.83±0.01

TABLE I: Mean accuracy with standard deviation over 10-fold cross validation for subject, S01

- B. Multiple Subject Classiﬁcation

The second results, presented in Table II, demonstrate the classiﬁcation performance across three subjects {S01, S02, S03}, where a new classiﬁcation model is trained for each subject. Due to the known impracticalities of collecting large amounts of data per subject [23], here we reduce the number of SSVEP presentation sessions (trials) per subject for each class to only 20. We also only consider the highest performing classiﬁcation approaches across traditional and deep model approaches from the previous result of Section IV-A (CNN and SVM; Table I). The results highlight, that even with a reduced

2Training time taken for vanilla RNN 600 minutes, GRU 524 minutes, LSTM 619 minutes, CNN 4 minutes on Nvidia GeForce GTX 1060 GPU.

[Figure 7]

[Figure 8]

[Figure 9]

1.0 0.0 0.0 0.0

1.0 0.0 0.0 0.0

0.4706 0.2353 0.1765 0.1176

10

10

10

0.0265 0.9646 0.0088 0.0

0.3333 0.6667 0.0 0.0

0.0667 0.4667 0.4 0.0667

12

12

12

Truelabel

Truelabel

Truelabel

0.0943 0.0 0.9057 0.0

0.0 0.1111 0.5 0.3889

0.2 0.2667 0.4667 0.0667

15

15

15

0.0 0.0 0.0 1.0

0.0 0.0 0.0 1.0

0.0 0.0769 0.2308 0.6923

30

30

30

10 12 15 30 Predicted label

10 12 15 30 Predicted label

10 12 15 30 Predicted label

(a) CNN classifying on single subject (S01)

(b) CNN classifying across subjects

(c) SVMGaussian classifying across subjects

[Figure 10]

[Figure 11]

0.5789 0.2105 0.1053 0.1053

0.7 0.3 0.0 0.0

10

10

0.1 0.6 0.3 0.0

0.0 0.6 0.3 0.1

12

12

Truelabel

Truelabel

0.1176 0.2941 0.2353 0.3529

0.05 0.4 0.35 0.2

15

15

0.0 0.0714 0.2857 0.6429

0.0 0.0 0.0 1.0

30

30

10 12 15 30 Predicted label

10 12 15 30 Predicted label

(d) SVMLinear classifying across subjects

(e) Deep CNN on unseen subject (S04)

Fig. 4: Confusion matrices for the various dataset and model conﬁguration tested highlighting the per-class statistical accuracy (Maximal result being accuracy = 1.0 in the matrix diagonals).

quantity of data available, the CNN approach still signiﬁcantly outperforms the SVM across all subjects. This result highlights the applicability of the proposed CNN approach for BCI applications, where data quantity is often relatively limited [23].

Method S01 S02 S03 Mean

CNN 0.91±0.08 0.92±0.11 0.85±0.10 0.89±0.03 SVMGaussian 0.59±0.08 0.68±0.08 0.67±0.10 0.65±0.04

SVMLinear 0.76±0.05 0.68±0.07 0.58±0.10 0.67±0.07

TABLE II: Mean accuracy with standard deviation over 10fold cross validation for each of the three subjects, mean results across subjects are also presented

C. Classiﬁcation Across Subjects

To assess the ability of a single CNN model to classify a dataset comprising data from all of the subjects {S01, S02, S03}, we classify all the signals from the three subjects together instead of performing individual classiﬁcation. Having a single model trained on EEG data from multiple subjects is known to be challenging [26], potentially due to biological differences between subjects and the variability of the EEG recording process. However, the results presented in Table III show that the CNN is able to signiﬁcantly outperform the SVM based approaches when performing classiﬁcation across subjects. This can be further seen in Figures 4b, 4c and 4d, showing better performance across classes for the CNN.

Method Accuracy

CNN 0.78±0.10 SVMGaussian 0.51±0.06

SVMLinear 0.50±0.06

TABLE III: Test Accuracy across subjects D. Generalisation Capability to an Unseen Subject

A strongly desirable quality for any model performing the classiﬁcation of EEG is that of unseen subject generalisation - whereby the model is able to correctly classify data from a subject whose data is absent from a priori model training. To test this on our CNN model, we introduce the data of the unseen subject S04. We then attempt to classify these data using a model which was trained only on the data of the other three subjects, {S01, S02, S03}. Using the same CNN architecture for this task as depicted in Figure 3, we only achieve an accuracy of 0.59 on S04 without any additional training. We also attempt to classify the new test subject using SVM, however the SVM only displays random classiﬁcation performance (≈ 0.25 accuracy; i.e 1/4 for 4 classes).

To overcome this performance issue, we explore a deeper architectural network variant as deeper networks have been shown to learn more complex features in order to determine the correlation between subjects [14]. Figure 5 illustrates the deeper architecture where empirically, we repeat our SCU blocks (each dashed pink box represents a SCU block) to a maximum number of ﬁve. This deeper architecture, introduced to classify subject S04 data, demonstrates a substantially

[Figure 12]

Fig. 5: Our deeper CNN architecture for unseen subjects better classiﬁcation accuracy of 0.69, perhaps suggesting that a deeper model is required to perform the unseen subject generalisation task. The confusion matrix for this result is presented in Figure 4e. This ﬁgure demonstrates that the CNN has varying performance across the different classes, with the 30Hz signal being the best performing for this extended CNN model.

V. CONCLUSION

In this paper we introduce deep convolutional neural network architectures constructed around a common computational building block, for the classiﬁcation of raw dry-EEG SSVEP data - the ﬁrst such study to do so. We evaluate the performance of our model on SSVEP data recorded from four subjects using the noise-prone dry-EEG methodology. As compared with current state-of-the-art methods, our approach requires no pre-processing to the data, demonstrates higher overall classiﬁcation accuracy across subjects and generalises signiﬁcantly better to entirely unseen test subjects. These key results demonstrate that CNN based approaches should become the new benchmark method for SSVEP dry-EEG classiﬁcation.

Future work would involve larger datasets to further study the classiﬁcation and generalisation performance across subjects. The combination of the CNN and RNN models may also offer a way to increase overall performance.

ACKNOWLEDGMENT

The authors would like to thank the Ministry of Higher Education Malaysia and Technical University of Malaysia Malacca (UTeM) as the sponsors of the ﬁrst author.

REFERENCES

- [1] R. P. Rao, Brain-Computer Interfacing: an Introduction. New York, NY, USA: Cambridge University Press, 2013.
- [2] V. P. Oikonomou, G. Liaros, K. Georgiadis, E. Chatzilari, K. Adam, S. Nikolopoulos, and I. Kompatsiaris, “Comparative Evaluation of State-of-the-art Algorithms for SSVEP-based BCIs,” arXiv preprint arXiv:1602.00904, 2016.
- [3] J. Minguillon, M. A. Lopez-Gordo, and F. Pelayo, “Trends in EEG-BCI for Daily-life: Requirements for Artifact Removal,” Biomedical Signal Processing and Control, vol. 31, pp. 407–418, 2017.
- [4] M. A. Lopez-Gordo, D. Sanchez-Morillo, and F. Pelayo Valle, “Dry EEG electrodes,” Sensors, vol. 14, no. 7, pp. 12847–12870, 2014.
- [5] G. Edlinger and C. Guger, “Can Dry EEG Sensors Improve the Usability of SMR, P300 and SSVEP Based BCIs?” in Towards Practical BrainComputer Interfaces. Springer, 2012, pp. 281–300.

- [6] T. R. Mullen, C. A. Kothe, Y. M. Chi, A. Ojeda, T. Kerth, S. Makeig, T.P. Jung, and G. Cauwenberghs, “Real-time Neuroimaging and Cognitive Monitoring using Wearable Dry EEG,” IEEE Transactions on Biomedical Engineering, vol. 62, no. 11, pp. 2553–2567, 2015.
- [7] Y.-P. Lin, Y. Wang, C.-S. Wei, and T.-P. Jung, “Assessing the Quality of Steady-State Visual-Evoked Potentials for Moving Humans using a Mobile Electroencephalogram Headset,” Frontiers in Human Neuroscience, vol. 8, no. March, pp. 1–10, 2014.
- [8] T. Mullen, C. Kothe, Y. M. Chi, A. Ojeda, T. Kerth, S. Makeig, G. Cauwenberghs, and T.-P. Jung, “Real-time Modeling and 3D Visualization of Source Dynamics and Connectivity using Wearable EEG,” in International Conference of Engineering in Medicine and Biology Society. IEEE, 2013, pp. 2184–2187.
- [9] G. Lisi, M. Hamaya, T. Noda, and J. Morimoto, “Dry-wireless EEG and Asynchronous Adaptive Feature Extraction Towards a Plug-and-play Coadaptive Brain Robot Interface,” in IEEE International Conference on Robotics and Automation. IEEE, 2016, pp. 959–966.
- [10] D. E. Callan, G. Durantin, and C. Terzibas, “Classiﬁcation of Single-trial Auditory Events using Dry-wireless EEG during Real and Motion Simulated Flight,” Frontiers in Systems Neuroscience, vol. 9, no. February, pp. 1–12, 2015.
- [11] A. M. Norcia, L. G. Appelbaum, J. M. Ales, B. R. Cottereau, and B. Rossion, “The Steady-state Visual Evoked Potential in Vision Research: A Review,” Journal of vision, vol. 15, no. 6, pp. 4–4, 2015.
- [12] N. S. Kwak, K. R. M¨uller, and S. W. Lee, “A Convolutional Neural Network for Steady State Visual Evoked Potential Classiﬁcation under Ambulatory Environment,” PLoS ONE, vol. 12, no. 2, pp. 1–20, 2017.
- [13] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” nature, vol. 521, no. 7553, p. 436, 2015.
- [14] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning. MIT Press, 2016.
- [15] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with Convolutional Neural Networks for EEG Decoding and Visualization,” Human brain mapping, vol. 38, no. 11, pp. 5391– 5420, 2017.
- [16] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “Eegnet: A compact Convolutional Network for EEGbased Brain-Computer Interfaces,” arXiv preprint arXiv:1611.08024, 2016.
- [17] J. Thomas, T. Maszczyk, N. Sinha, T. Kluge, and J. Dauwels, “Deep learning-based classiﬁcation for brain-computer interfaces,” in IEEE International Conference on Systems, Man, and Cybernetics. IEEE, 2017, pp. 234–239.
- [18] A. L. Goldberger, L. A. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, “Physiobank, Physiotoolkit, and Physionet,” Circulation, vol. 101, no. 23, pp. e215–e220, 2000.
- [19] J. W. Peirce, “PsychoPypsychophysics Software in Python,” Journal of neuroscience methods, vol. 162, no. 1-2, pp. 8–13, 2007.
- [20] G. Gargiulo, R. A. Calvo, P. Bifulco, M. Cesarelli, C. Jin, A. Mohamed, and A. van Schaik, “A New EEG Recording System for Passive Dry Electrodes,” Clinical Neurophysiology, vol. 121, no. 5, pp. 686–693, 2010.
- [21] S. Bai, J. Z. Kolter, and V. Koltun, “An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling,” arXiv preprint arXiv:1803.01271, 2018.
- [22] D. P. Kingma and J. Ba, “Adam: A method for Stochastic Optimization,” arXiv preprint arXiv:1412.6980, 2014.
- [23] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotomamonjy, and F. Yger, “A Review of Classiﬁcation Algorithms for EEG-based Brain-Computer Interfaces: A 10-year Update,” Journal of neural engineering, 2018.
- [24] A. Barachant, S. Bonnet, M. Congedo, and C. Jutten, “Classiﬁcation of Covariance Matrices using a Riemannian-based Kernel for BCI Applications,” Neurocomputing, vol. 112, pp. 172–178, 2013.
- [25] Z. C. Lipton, J. Berkowitz, and C. Elkan, “A Critical Review of Recurrent Neural Networks for Sequence Learning,” arXiv preprint arXiv:1506.00019, 2015.
- [26] O. Dehzangi and M. Farooq, “Portable Brain-Computer Interface for the Intensive Care Unit Patient Communication Using Subject-Dependent SSVEP Identiﬁcation,” BioMed Research International, vol. 2018, 2018.

