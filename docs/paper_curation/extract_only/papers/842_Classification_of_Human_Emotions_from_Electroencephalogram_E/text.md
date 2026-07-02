# Classification of Human Emotions from Electroencephalogram (EEG) Signal using Deep Neural Network

Abeer Al-Nafjan

College of Computer and Information Sciences Imam Muhammad bin Saud University Riyadh, Saudi Arabia

Manar Hosny

College of Computer and Information Sciences King Saud University Riyadh, Saudi Arabia

Areej Al-Wabil

Center for Complex Engineering Systems King Abdulaziz City for Science and Technology Riyadh, Saudi Arabia

Yousef Al-Ohali

College of Computer and Information Sciences King Saud University Riyadh, Saudi Arabia

Abstract—Estimation of human emotions from Electroencephalogram (EEG) signals plays a vital role in developing robust Brain-Computer Interface (BCI) systems. In our research, we used Deep Neural Network (DNN) to address EEG-based emotion recognition. This was motivated by the recent advances in accuracy and efficiency from applying deep learning techniques in pattern recognition and classification applications. We adapted DNN to identify human emotions of a given EEG signal (DEAP dataset) from power spectral density (PSD) and frontal asymmetry features. The proposed approach is compared to state-of-the-art emotion detection systems on the same dataset. Results show how EEG based emotion recognition can greatly benefit from using DNNs, especially when a large amount of training data is available.

Keywords—Electroencephalogram (EEG); Brain-Computer Interface (BCI); emotion recognition; affective state; Deep Neural Network (DNN); DEAP dataset

I. INTRODUCTION

Recent developments in BCI (Brain Computer Interface) technologies have facilitated emotion detection and classification. Many BCI studies have investigated, detected and recognized the user‘s affective state and applied the findings in varied contexts including, among other things, communication, education, entertainment, and medical applications. BCI researchers are considering different responses in various frequency bands, ways of eliciting emotions, and various models of affective states. Different techniques and approaches have been used in the processing steps to estimate the emotional state from the acquired signals.

BCI systems based on emotion detection are considered as passive/involuntary control modality. For example, affective computing focuses on developing applications, which automatically adapts to changes in the user‘s states, thereby improving interaction that leads to more natural and effective usability (e.g. with games, adjusting to the interest of the user)

[1]. Recognizing a user‘s affective state can be used to optimize training and enhancement of the BCI operations [2].

EEG is often used in BCI research experimentation because the process is non-invasive to the research subject and minimal risk is involved. The devices‘ usability, reliability, costeffectiveness, and the relative convenience of conducting studies and recruiting participants due to their portability have been cited as factors influencing the increased adoption of this method in applied research contexts [3], [4]. These advantages are often accompanied by challenges such as low spatial resolution and difficulty managing signal-to-noise ratios. Power-line noise and artifacts caused by muscle or eyemovement may be permissible or even exploited as a control signal for certain EEG-based BCI applications. Therefore, signal-processing techniques can be used to eliminate or reduce such artifacts.

This paper explains our research which involves implementing and examining the performance of the Deep Neural Network (DNN) to model a benchmark emotion dataset for classification.

The remainder of this paper is organized as following: In Section 2, we start with background about the emotion models then we briefly review the EEG-based emotion detection systems in Section 3. In Section 4, we describe our proposed method and techniques. In ection 5, we discuss the results and we finally draw conclusions in Section 6.

II. EMOTION MODEL

Emotions can be generally classified on the basis of two models: discrete and dimensional [2], [5]. Dimensional model of emotion proposes that emotional states can be accurately represented by a small number of underlying affective dimensions. It represents the continuous emotional state, represented as a vector in a multidimensional space. Most dimensional models incorporate valence and arousal. Valence

refers to the degree of ‗pleasantness‘ associated with an emotion. It ranges from unpleasant (e.g. sad, stressed) to pleasant (e.g. happy, elated). Whereas, arousal refers to the strength of experienced emotion. This arousal occurs along a continuum and may range from inactive (e.g. uninterested, bored) to active (e.g. alert, excited) [5].

Discrete theories of emotion propose an existence of small numbers of separate emotions. These are characterized by coordinated response patterns in physiology, neural anatomy, and morphological expressions. Six basic emotions frequently advanced in research papers include happiness, sadness, anger, disgust, fear, and surprise [6], [7].

Emotion measurement and assessment methods can be subjective and/or objective affective measures. Subjective measures use different self-report instruments, such as questionnaires, adjective checklists, and pictorial tools to represent any set of emotions, and can be used to measure mixed emotions. Self-reporting techniques, however, do not provide objective measurements, but they do measure conscious emotions and they cannot capture the real-time dynamics of the experience.

Objective measures can be obtained without the user‘s assistance. They use physiological cues derived from the physiology theories of emotion. Instruments that measure blood pressure responses, skin responses, pupillary responses, brain waves, and heart responses are all used as objective measures methods. Moreover, hybrid methods combining both subjective and objective methods have been used to increase accuracy and reliability of affective emotional states [2], [6].

III. EEG-BASED EMOTION DETECTION SYSTEMS

The volumes of studies and publications on EEG based emotion recognition have surged in recent years. Different models and techniques yield a wide range of systems. However, these systems can be easily differentiated owing to the differences in stimulus, features of detection, temporal window, classifiers, number of participants and emotion model, respectively.

Although the number of research studies conducted on EEG-based emotion recognition in recent years has been increasing, EEG-based emotion recognition is still a relatively new area of research. The effectiveness and the efficiency of these algorithms are somewhat limited. Some unsolved issues in current algorithms and approaches include the following: time constraints, accuracy, number of electrodes, number of recognized emotions, and benchmark EEG affective databases [6], [8].

Accuracy and reliability of sensory interfacing and translation algorithms in BCI systems are major challenges, which limit usage of these technologies in clinical settings. Also, engineering challenges have been focused to process the low signal to noise ratio embedded in noninvasive electroencephalography (EEG) signals. Moreover, computational challenges include optimal placement of a reduced number of electrodes and robustness of BCI algorithms to the smaller set of recording sites.

IV. PROPOSED SYSTEM

The performance of EEG recognition systems is based on the method of feature extraction algorithm and classification process. Hence, the aim of our study is to research the possibility of using EEG for the detection of four affective states, namely excitement, meditation, boredom, and frustration using classification and pattern recognition techniques. For this purpose, we conducted rigorous offline analysis for investigating computational intelligence for emotion detection and classification. We used deep learning classification on the DEAP dataset to explore how to employ intelligent computational methods in the form of classification algorithm. This could effectively mirror emotional affective states of subjects. We also compared our classification performance with a Random Forest classifier.

We built our system in an open source programming language, Python, and used Scikit-Learn toolbox for machine learning, along with Scipy for EEG filtering and preprocessing, MNE for EEG-specific signal processing and Keras library for deep learning.

In this section, we illustrate our methodology along with some implementation details of our proposed system. We start with describing the benchmark dataset. Then, describe our extracted features. Finally, we discuss the classification process and model evaluation method.

- A. DEAP Dataset

DEAP is a benchmark affective EEG database for the analysis of spontaneous emotions. DEAP database was prepared by Queen Mary University of London and published in [9]. The database contains physiological signals of 32 participants. It was created with the goal of creating an adaptive music video recommendation system based on user current emotion. DEAP has been used for conducting a number of studies and it has been proved that it is well-suited for testing new algorithms [9], [10].

To evaluate our proposed classification method, we used the preprocessed EEG dataset from DEAP database, where the sampling rate of the original recorded data of 5 Hz was down-sampled to a sampling rate of 128 Hz, with a bandpass frequency filter ranging from 4.0-45.0 Hz, and the EOG artifacts are eliminated from the signals.

- B. Feature Extraction

Feature extraction plays a critical role in designing an EEGbased BCI system. Different features have been used in literature, including Common Spatial pattern, Higher Order Crossings, Hjorth parameters, time-domain statistics, EEG spectral power, wavelet entropy, and coherence analysis. These EEG features can be extracted by applying signal processing methods; time domain signal analysis, frequency domain signal analysis, and/or time-frequency signal domain analysis [6], [11].

1) Power Spectral Density (PSD)

In this work, we have decided to use frequency domain analysis to extract EEG features. Power Spectral Density (PSD) is one of the most popular features in the frequency

domain in the context of emotion recognition using EEG signals [6], [8]. This method is based on Fast Fourier Transform (FFT), which is an algorithm to compute the Discrete Fourier Transform and its inverse. This transformation converts data in the time domain to the frequency domain and vice versa. Besides EEG applications, it has been widely used for numerous applications in engineering, science, and mathematics. In this study, each EEG signal is decomposed using PSD approach into four distinct frequency ranges: theta (4–8 Hz), alpha (8–13 Hz), beta (13–30 Hz), and gamma (30– 40 Hz). The PSDs were computed using Python Signal Processing Toolbox (mne), and the average of power over a specific frequency range was calculated to construct a feature using the avgpower function in the toolbox. Fig. 1 shows the extracted PSD.

|[Figure 1] Signal using Deep Neural_images/imageFile1.png>)|
|---|

Fig. 1. Feature extraction (a) preprocessed EEG signals in time domain (b) extracted PSD.

2) Frontal EEG Asymmetry

There has been a lot of research that investigated neural correlates of emotion in humans [6], [9], [12], [13]. Frontal activity, which is characterized in terms of decreased power in the alpha band, has been consistently found to be associated with emotional states [11]. Indeed, numerous studies agree on the fact that relatively greater trait left frontal activity is associated with trait tendencies toward a general appetitive approach, or behavioral activation motivational system, and that relatively greater trait right frontal activity is associated with trait tendencies toward a general avoidance or withdrawal system [14].

Therefore, many affective researches proposed that there was a link between asymmetry of frontal alpha activation and the valence of a subject‘s emotional state. It is widely accepted that the left hemisphere presents higher activation on states of positive valence, whereas the right hemisphere presents higher activation on states of negative valence. There have been numerous studies which support the hypothesis that frontal EEG asymmetry is an indicator of arousal and valence of

emotion. At the same time, different frontal asymmetry equations are used to calculate the valence and arousal [12].

In Vamvakousis et al. [13], the Amyotrophic Lateral Sclerosis (ALS) patients were expressing their emotions through music in real time. They used (1) and (2) for detecting valence and arousal, respectively. They have estimated the emotional state of the performer in a gaze-controlled musical interface system, where a positive valence value triggers major chords progressions, while a negative valence triggers minor chord progressions.

Valence=(left_beta /left_alpha) – (right_beta /right_alpha ) (1) Arousal = (2) In Kirke and Eduardo [14], the researchers developed a

tool for unskilled composers, or subjects with problems in emotional expression, in order to better express themselves through music. They built a combined EEG system that takes as input raw EEG data and attempts to output a piano composition and performance, which expresses the estimated emotional content of the EEG data. The subject‘s emotion was estimated based on EEG Frontal Asymmetry where they used (3) and (4) below:

Valence = ln (frontal alpha power(left) – ln (frontal alpha power(right)) (3)

Arousal = - (ln (frontal alpha power(right)) + ln (frontal alpha power(left))) (4)

Hayfa et al. [15] and Ramirez et al. [16] used frontal EEG asymmetry to specify the valence and arousal of emotions by using (5) and (6) below. A fuzzy logic classification method was implemented that was fed with the valence and arousal features. The average classification rate for the seven different emotions was 64.79%.

Ramirez et al. classified emotional states by computing arousal levels as the prefrontal cortex and valence levels using (5) and (6). They applied machine learning techniques (support vector machines with different kernels) to classify the user emotion into high/low arousal and positive/negative valence emotional states, with average accuracies of 77.82, and 80.11%, respectively.

Valence = (5)

Arousal = (6)

In Ramirez et al. [17], researchers introduced a novel neuro-feedback approach. They presented the results of a pilot clinical experiment applying the approach to alleviate depression in elderly people. They used (7) and (8), where the arousal was computed as beta to alpha activity ratio in the frontal cortex, and valence was computed as relative frontal alpha activity in the right lobe compared to the left lobe.

Valence = (7) Arousal = (8)

In order to find which equation for valence and arousal to use, we extracted alpha and beta band powers from the DEAP EEG signals and used those powers to compute valence and arousal scores of all above equations. We applied the different frontal EEG asymmetry equations as moderator and explored the correlation to the DEAP self-assessment measurement. Consequently, we keep only the channels we are interested in (Fz, AF3, F3, AF4, and F4). Afterwards, we performed a timefrequency transform to extract (spectral features) alpha: 8–11 Hz, beta: 12–29 Hz according to Table 1. Finally, we computed the values of Arousal and Valence using four different methods namely, Vamvakousis2012, Kirke2011, Hayfa2013, and Ramirez2015.

TABLE. I. INPUT PARAMETERS FOR COMPUTE VALENCE AROUSAL

|Input Parameter<br><br>|Channel|Frequency (Hz)<br><br>|Input Parameter<br><br>|Channel|Frequency (Hz)<br><br>|
|---|---|---|---|---|---|
|Left_alpha|AF3 & F3|7 – 15|Alpha_F4|F4|7 – 15|
|Left_beta|AF3 & F3|16 – 31|Alpha_F3|F3|7 – 15|
|Right_alpha|AF4 & F4|7 – 15|Alpha_all|AF3, F3,<br>AF4, F4<br>|7 – 15|
|Right_beta|AF4 & F4|16 – 31|Beta_F4|F4|16 – 31|
|Front_alpha|Fz|7 - 15 Hz|Beta_F3|F3|16 – 31|
|Front_beta|Fz|16 – 31|Beta_all|AF3, F3,<br>AF4, F4<br>|7 - 15|

Finally, to compare their result we applied statistics calculation; Mean Absolute Error (MAE), Mean Squared Error (MSE), and Pearson Correlation (Corr) as the following:

3) MAE is the mean ∑ of the absolute errors | | | | where is the prediction and the true value

MAE= ∑ | | (9)

- MSE is the mean ∑ of the square of the errors (( ̂

MSE= ∑ ̂ (10)

4) Corr is a measure of the strength of the linear relationship between two variables

TABLE. II. FRONTAL ASYMMETRY EQUATIONS RESULT (NUMBERS IN THE BRACKETS ARE STANDARD DEVIATIONS)

|Statistic|Method|MSE|MAE|Corr|
|---|---|---|---|---|
|Valence|Vamvakousis2012|10.611 (+/- 4.348)|2.689 (+/- 0.637)|-0.028 (+/- 0.224)|
|Valence|Kirke2011|9.098 (+/- 3.363)|2.448 (+/- 0.478)|0.022 (+/- 0.221)|
|Valence|Hayfa2013|8.490 (+/- 2.770)|2.361 (+/- 0.440)|0.039 (+/- 0.239)|
|Valence|Ramirez2015|9.633 (+/- 4.505)|2.531 (+/- 0.675)|0.088 (+/- 0.249)|
|Arousal|Vamvakousis2012|7.513 (+/- 2.716)|2.220 (+/- 0.415)|0.054 (+/- 0.210)|
|Arousal|Kirke2011|7.987 (+/- 3.129)|2.249 (+/- 0.469)|0.007 (+/- 0.179)|
|Arousal|Hayfa2013|9.092 (+/- 3.200)|2.493 (+/- 0.503)|-0.037 (+/- 0.217)|
|Arousal|Ramirez2015|9.969 (+/- 3.648)|2.655 (+/- 0.529)|0.024 (+/- 0.210)|

Table 2 shows the result after we ran all four different equations on the whole DEAP dataset and observed which equation will produce lower MSE. According to these results, for valence, it is best to use Hayfa2013 equation, and for arousal, Vamvakousis2012 outperforms the other ones.

C. Classification

Deep Learning (also known as deep machine learning, deep structured learning, or hierarchical learning) is a recent machine learning technique that models high-level abstractions in data by using multiple processing layers with complex structures [18]. Deep Learning and Neural Networks have remarkable ability to solve problems in image recognition, speech recognition, and natural language processing [18], [19]. In our work, we investigate the possibility of using EEG for the detection of four affective states (Excitement, Meditation, Boredom, and Frustration) using DNN classification. Therefore, we explore how to employ intelligent computational methods in the form of classification algorithm, which could effectively mirror emotional affective states of subjects. We also compare our classification performance with a Random forest classifier.

1) Data Representation We used the two-dimensional emotion model approach

proposed in Russell‘s (1980) and shown in Fig. 2.

In this model, very high or very low values on onedimension (Arousal) are associated with middle values on the second dimension (Valence). The arousal represents the high and low intensity, whereas the valence represents the emotion type if it is positive or negative.

In DEAP subjective emotion, the subjects selected the numbers 1–9 to indicate their emotion states in each category. In our study, as shown in Fig. 3, we mapped the scales (1–9) into two levels of each valence and arousal states (high and low) as following: excitement is a feeling of high arousal in a high valence whereas frustration is a feeling of high arousal in a low valence. Meditation is a feeling of low arousal in a high valence whereas boredom is a feeling of low arousal in a low valence.

|[Figure 2] Signal using Deep Neural_images/imageFile2.png>)|
|---|

Fig. 2. Russell's circumplex model of affect.

|[Figure 3] Signal using Deep Neural_images/imageFile3.png>)|
|---|

The second hidden layer consists of (786) units, and the third hidden layer consists of (472) units. Whereas the output layer dimension(s) corresponds to the number of target emotions states (4) units.

For training DNN classifier, we used Adam gradient descent with a logarithmic loss function, which is called categorical cross-entropy as the objective loss function. For all random weight initialization, we have chosen He-initialization, as described in [21]. For transfer learning, we start with reasonable defaults and follow best practices: 0.02 is chosen as the start learning rate. Then, we linearly reduce it with each epoch, so that the learning rate for the last epoch is 0.001.

Training is evaluated using a validation set, which is roughly 10% of the size of the total dataset (train set + valid set + test set). We set dropout to 0.2 for the input layer and 0.5 for the hidden layers. Stopping criterion of the network training is based on the model‘s performance on a validation set [22]. If the network starts to over-fit, the network training is then stopped. This stopping criterion is helpful in reducing overfitting on the validation data. The network is tested on a test set which also contains about 10% of the data samples in the dataset.

Fig. 3. Proposed emotion model and the classification labels.

2) Neural Network Model

The extracted features are further fed to DNN classifier. The block diagram of our DNN classifier is shown in Fig. 4. In our work, the DNN architecture is a fully connected feedforward neural network with three hidden layers. The hidden layers contain units with rectified linear activation functions (ReLu) [20], [21].

Fig. 5 shows a plot of loss per epoch on the training and validation data over training epochs. From the plot of loss, we conclude that we have over-fit our training set to at most a small extent. When we train for longer than 800 epochs, the training loss does not become significantly less than the validation loss until after roughly 200-800 epochs, and after this point, training loss continues to decrease but validation loss begins to increase. Performance of the test data calculated using confusion matrix and result with Accuracy: 0.825, Recall: 0.825, Precision: 0.68, Misclassification rate = 0.175.

The output is configured as a soft-max layer with a crossentropy cost function. The input layer consists of (2184) units. Each hidden layer contains 60% units from its ―predecessor‖ previous layer; the first hidden layer consists of (1310) units.

[Figure 4] Signal using Deep Neural_images/imageFile4.png>)

Fig. 4. Block diagram of DNN classifier.

[Figure 5] Signal using Deep Neural_images/imageFile5.png>)

Fig. 5. Loss per epoch on training and validation set.

Our research can be compared with one of the traditional EEG signal classification methods, Random Forest (RF) classification. RF constructs a combination of many unpruned decision trees (Breiman, 2001). The output class is the mode of the classes output by individual trees. We achieved 48.5% classification accuracy.

V. RESULTS AND DISCUSSIONS

In addition to the confusion matrix results which show that DNN classification accuracy outperforms the RF method, the classification accuracy of our model was also compared to other previous studies that use similar approaches, where they used the same dataset and the same extracted features but different classification techniques as shown in Table 3.

Chung and Yoon [23] proposed the weighted-log-posterior function based Bayes classifier as an affective recognition method. The affective states are divided into two and three classes in valence dimension and arousal dimension. The accuracies for two classes are 66.6 % for valence, 66.4 % for arousal classification, 53.4 % and 51.0 % for three classes, respectively. Moreover, they compared their proposed method with the method used in [9] and reported that they got better performance than the ordinary Bayes classifier.

Zhang et al. [24] proposed an ontological model for representation and integration of EEG data. The idea was the use of an ontology for modeling low-level biometric features and mapping them to high-level human emotions. Similarity, to evaluate the effectiveness of their model, they used DEAP dataset. Their model achieved an average recognition ratio of 75.19% on valence and 81.74% on arousal for eight selected participants.

Suwicha et al. in [19] proposed an algorithm for classification of EEG signals in human emotion. They used deep learning network (DLN) classifiers to distinguish between feelings of happiness, pleasure, relaxation, excitement, neutral, calm, distressed, miserable and depressed. Power Spectral Density (SPD) was calculated using FFT and principal component analysis PCA and covariate shift adaptation of the PCA implemented to minimize features. Their experimental results showed that DLN is capable of classifying three different levels of valences and arousals with accuracy of 49.52% and 46.03%, respectively. They have reported that DLN provides better performance compared to SVM (Support Vector Machine) and Naïve Bayes classifiers.

TABLE. III. COMPARISON OF VARIOUS STUDIES USING EEG-DEAP DATASET

|Research|Features|Classifier|Result|
|---|---|---|---|
|Chung and Yoon, 2012 [23]<br><br>|PSD and power asymmetry<br><br>|Bayes|Detect: Two\ three classes per dimension valence and arousal Result: 53.4 % for two classes 51.0 % for three classes<br><br>|
|Koelstra et al., 2012 [9]<br><br>|PSD and power asymmetry<br><br>|Naïve Bayes (NB)<br><br>|Detect: Two different levels of valence, arousal, and liking Result: 57.0% for valence 62.0% for arousal<br><br>|
|Zhang et al., 2013 [24]<br><br>|PSD|ontological model<br><br>|Detect: Two classes per dimension valence and arousal Result: 75.19% for valence 81.74% for arousal<br><br>|
|Suwicha et al., 2014 [19]<br><br>|- PSD<br><br>- Covariate shift adaptation of PCA<br><br><br>|DLN with a stacked auto-encoder (SAE)<br><br>|Detect: Three different levels of valence and arousal Result: 49.52% for valence 46.03% for arousal<br><br>|
|Atkinsona and Camposb. 2016 [25]<br><br>|Statistical features, band power, Hjorth parameters and fractal dimension<br><br>|Kernel<br><br>|Detect: Three classes per dimension (valence and arousal) Result: 60.7% for valence 62.33% for arousal.<br><br>|
|Proposed method<br><br>|PSD Frontal asymmetry<br><br>|DNN|Detect: Two classes per dimension (valence and arousal) Result: 82.0% for two classes<br><br>|

PSD (Power Spectral Density), PCA (Principal Component Analysis), DNN (Deep Learning Neural Network)

In one of the recent studies [25], the authors developed an emotion detection system. They explored a wider set of features by extracting statistical features, band power for different frequencies, Hjorth parameters (HP) and fractal dimension (FD) for each channel. Then, in order to select a relevant set of features from the extracted features so that further classification can be more accurate, the MinimumRedundancy-Maximum-Relevance (mRMR) method was used. The researchers categorized 2, 3, and 5 classes per valence and arousal dimensions. This model was capable of recognizing arousal (valence) with rates of 73.06% (73.14%), 60.7% (62.33%), and 46.69% (45.32%) for 2, 3, and 5 classes, respectively. They reported that kernel-based classifier acquired higher accuracy when compared with other computational methods such as SVM and Naïve Bayes.

The comparison shows that our model exhibits very promising results when dealing with varying sizes of datasets and different classes of emotions. For example, Zhang et al. [24] achieved high accuracy by applied their method on only eight selected participants. Additionally, for the same number of classes per dimension, an improvement of 28.6% and 12% was achieved with our proposed method when compared to [23] and [25], respectively.

VI. CONCLUSION

In this paper, we described our proposed method to detect emotions from EEG signals, where we used the pre-processed DEAP dataset. Two different types of features were extracted from the EEG; PSD features and pre-frontal asymmetry features. This resulted in a set of 2184 unique features describing the EEG activity during each trial. These extracted features were used to train a DNN classifier and Random Forest classifier. We found that the DNN classifier outperformed the Random Forest classifier. Moreover, we compared our result with previous researches. Our results show that the DNN method provides better classification performance compared to other state-of-the-art approaches and suggest that this method can be applied successfully to EEG based I systems where the amount of data is large.

REFERENCES

- [1] F. Nijboer, S. P. Carmien, E. Leon, F. O. Morin, R. A. Koene, and U. Hoffmann, ―Affective rain-Computer Interfaces: Psychophysiological Markers of Emotion in Healthy Persons and in Persons with Amyotrophic Lateral clerosis,‖ in Affective omputing & Intelligent Interaction ACII2009, 2009.
- [2] G. G. Molina, T. Tsoneva, and A. Nijholt, ―Emotional brain-computer interfaces,‖ in 3rd International onference on Affective omputing and Intelligent Interaction and Workshops ACII 2009, 2009, pp. 138–146.
- [3] . Graimann, rendan Allison, and G. Pfurtscheller, ― rain-Computer Interfaces: A Gentle Introduction,‖ in rain-Computer Interfaces: Revolutionizing Human-Computer Interaction, Springer, 2010, pp. 1– 27.
- [4] A. Roman-Gonzalez, ―EEG ignal Processing for I Applications,‖ Human-Computer Systems Interaction: Backgrounds and Applications 2, Advances in Intelligent and Soft Computing, vol. 98, no. 1, pp. 51–72, 2012.
- [5] J. Posner, J. A. Russell, and . . Peterson., ―The circumplex model of affect: An integrative approach to affective neuroscience, cognitive development, and psychopathology.,‖ Development and psychopathology, vol. 17, no. 3, pp. 715–734, 2005.
- [6] M.-K. Kim, M. Kim, E. Oh, and S.-P. Kim, ―A review on the computational methods for emotional state estimation from the human EEG.,‖ omputational and mathematical methods in medicine, vol. 2013, 2013.
- [7] D. Heger, R. Mutter, . Herff, F. Putze, and T. chultz, ― ontinuous recognition of affective states by functional near infrared spectroscopy signals,‖ in Humaine Association onference on Affective omputing and Intelligent Interaction, ACII 2013, 2013, pp. 832–837.
- [8] C. Mühl, . Allison, A. Nijholt, and G. hanel, ―A survey of affective brain computer interfaces: principles, state-of-the-art, and challenges,‖ Brain-Computer Interfaces, vol. 1, no. 2, pp. 66–84, 2014.
- [9] S. Koelstra, C. Mühl, M. Soleymani, J. S. Lee, A. Yazdani, T. Ebrahimi, T. Pun, A. Nijholt, and I. Patras, ―DEAP: A database for emotion

- analysis; Using physiological signals,‖ IEEE Transactions on Affective Computing, vol. 3, no. 1, pp. 18–31, 2012.
- [10] Y. Liu and O. ourina, ―EEG databases for emotion recognition,‖ in International Conference on Cyberworlds, CW 2013, 2013, pp. 302– 309.
- [11] M. ingh, M. ingh, . Gangwar, and I. Engineering, ―Feature Extraction from EEG for Emotion lassification,‖ International Journal of IT & Knowledge Management (IJITKM), vol. 7, no. 1, pp. 6–10, 2013.
- [12] G. Liberati, . Federici, and E. Pasqualotto, ―Extracting neurophysiological signals reflecting users‘ emotional and affective responses to I use: A systematic literature review,‖ NeuroRehabilitation, vol. 37, no. 3, pp. 341–358, 2015.
- [13] Z. Vamvakousis and R. Ramirez, ―A rain-Gaze Controlled Musical Interface.,‖ Advances in Neurotechnology, vol. 4, 0 .
- [14] A. Kirke and E. R. Miranda, ― ombining EEG Frontal Asymmetry Studies with Affective Algorithmic Composition and Expressive Performance Models,‖ Proceedings of 37th International omputer Music Conference (ICMC), pp. 1–4, 2011.
- [15] H. laiech, M. Neji, A. Wall, and A. M. Alimi, ―Emotion Recognition by Analysis of EEG ignals,‖ in 3th International onference on Hybrid Intelligent Systems ( HIS ), 2013, pp. 312–318.
- [16] R. Ramirez and Z. Vamvakousis, ―Detecting Emotion from EEG ignals Using the Emotive Epoc Device,‖ in International onference on rain Informatics., 2012, pp. 175–184.
- [17] R. Ramirez, M. Palencia-lefler, S. Giraldo, Z. Vamvakousis, and E. Miller, ―Musical neurofeedback for treating depression in elderly people,‖ METHOD , vol. 9, no. October, pp. –10, 2015.
- [18] L. Deng, ―Three lasses of Deep Learning Architectures and Their Applications : A Tutorial urvey,‖ AP IPA transactions on signal and information processing, 2012.
- [19] . Jirayucharoensak and P. Israsena, ―EEG-based Emotion Recognition using Deep Learning Network with Principal Component based

ovariate hift Adaptation,‖ vol. 0 4, 0 4.

- [20] D. Kingma and J. a, ―Adam: A method for stochastic optimization,‖ in arXiv preprint arXiv:1412.6980, 2014.
- [21] K. He, X. Zhang, . Ren, and J. un, ―Delving Deep into Rectifiers : Surpassing Human-Level Performance on ImageNet lassification,‖ in IEEE international conference on computer vision., 2015, pp. 1026– 1034.
- [22] L. Prechelt, ―Early stopping—but when?.,‖ Neural Networks: Tricks of the trade, pp. 53–67, 2012.
- [23] . Y. hung and H. J. Yoon, ―Affective classification using ayesian classifier and supervised learning,‖ ontrol, Automation and ystems (ICCAS), pp. 1768–1771, 2012.
- [24] X. Zhang, . Hu, J. hen, and Philip Moore, ―Ontology-based context modeling for emotion recognition in an intelligent web,‖ World Wide Web, vol. 16, no. 4, pp. 497–513, 2013.
- [25] J. Atkinsona and D. amposb, ―Improving I-based emotion recognition by combining EEG feature selection and kernel classifiers.,‖ Expert Systems with Applications, vol. 47, pp. 35–41, 2016.

