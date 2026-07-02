TYPE Original Research PUBLISHED July DOI   .    /fnhum.    .       

OPEN ACCESS

EDITED BY

Kang Hao Cheong, Singapore University of Technology and Design, Singapore

REVIEWED BY

Qingyun Wang, Beihang University, China Xiaozhuan Gao, Northwest A&F University, China

*CORRESPONDENCE

Yalcin Isler

islerya@yahoo.com

RECEIVED May ACCEPTED June PUBLISHED July

CITATION

Degirmenci M, Yuce YK, Perc M and Isler Y (    ) Statistically signiﬁcant features improve binary and multiple Motor Imagery task predictions from EEGs.

Front. Hum. Neurosci.   :       . doi:   .    /fnhum.    .       

COPYRIGHT

© Degirmenci, Yuce, Perc and Isler. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

# Statistically signiﬁcant features improve binary and multiple Motor Imagery task predictions from EEGs

Murside Degirmenci , Yilmaz Kemal Yuce , Matjaž Perc , , , ,  and Yalcin Isler *

Department of Biomedical Technologies, Izmir Katip Celebi University,˙Izmir, Türkiye, Department of Computer Engineering, Alanya Alaaddin Keykubat University, Antalya, Türkiye, Faculty of Natural Sciences and Mathematics, University of Maribor, Maribor, Slovenia, Department of Medical Research, China Medical University Hospital, China Medical University, Taichung, Taiwan, Alma Mater Europaea, Maribor, Slovenia, Complexity Science Hub Vienna, Vienna, Austria, Department of Physics, Kyung Hee University, Seoul, Republic of Korea, Department of Biomedical Engineering, Izmir Katip Celebi University,˙Izmir, Türkiye

In recent studies, in the ﬁeld of Brain-Computer Interface (BCI), researchers have focused on Motor Imagery tasks. Motor Imagery-based electroencephalogram (EEG) signals provide the interaction and communication between the paralyzed patients and the outside world for moving and controlling external devices such as wheelchair and moving cursors. However, current approaches in the Motor Imagery-BCI system design require e ective feature extraction methods and classiﬁcation algorithms to acquire discriminative features from EEG signals due to the non-linear and non-stationary structure of EEG signals. This study investigates the e ect of statistical signiﬁcance-based feature selection on binary and multi-class Motor Imagery EEG signal classiﬁcations. In the feature extraction process performed di erent time-domain features, di erent frequencydomain features which are energy, variance, and entropy of Fourier transform within ﬁve EEG frequency subbands, di erent time-frequency domain features which are energy, variance, and entropy of Wavelet transform based on ﬁve EEG frequency subbands, and di erent Poincare plot-based non-linear parameters are extracted from each EEG channel. A total of  ,    Motor Imagery EEG features are supplied from channel EEG signals for each input EEG data. In the statistical signiﬁcance-based feature selection process, the best one among all possible combinations of these features is tried to be determined using the independent t-test and one-way analysis of variance (ANOVA) test on binary and multi-class Motor Imagery EEG signal classiﬁcations, respectively. The whole extracted feature set and the feature set that contain statistically signiﬁcant features only are classiﬁed in this study. We implemented and di erent classiﬁers in multi-class and binary (two-class) classiﬁcation tasks, respectively. The classiﬁcation process is evaluated using the ﬁve-fold cross-validation method, and each classiﬁcation algorithm is tested times. These repeated tests provide to check the repeatability of the results. The maximum of   .   and   .  % for the two-class and four-class scenarios, respectively, are obtained with Ensemble Subspace Discriminant among all these classiﬁers using selected features including only statistically signiﬁcant features. The results reveal that the introduced statistical signiﬁcance-based feature selection approach improves the classiﬁer performances by achieving higher classiﬁer performances with fewer relevant components in Motor Imagery task classiﬁcation. In conclusion, the main contribution of the presented study is two-fold evaluation of non-linear

parameters as an alternative to the commonly used features and the prediction of multiple Motor Imagery tasks using statistically signiﬁcant features.

KEYWORDS

brain-computer interfaces (BCIs), electroencephalogram (EEG), feature selection, machine learning, Motor Imagery (MI) task classiﬁcation

##  . Introduction

Brain–computer Interfaces (BCIs) help to establish and realize the interaction between humans and computers using physiological signals acquired from the brain (Tiwari et al., 2022). It allows individuals who can not control a part of their resulting from paralysis or similar diseases but who are conscious to communicate with the outside world and control the robot arm, wheelchair, computer, and similar devices with thought power. The basic concept of BCIs is based on capturing brain’s electrical signals, analyzing them on the artiﬁcial intelligence-powered software, and converting them to emotions and thoughts for particular purposes. The ﬁrst step of BCI system design is data acquisition to obtain physiological signals. A neuron captures the information about any thought, which is passed to the other neurons after being processed. This communication among neurons generates electrical activities that can be measured from the body surface (Tan and Nijholt, 2010; Bansal and Mahajan, 2019). If these activities are originated from the brain, they can be captured using electroencephalography (EEG) visualization devices. EEG is a non-invasive method of placing electrodes over the scalp (just as near to the brain cortex as possible) (Yuan and He, 2014; Tiwari et al., 2022). Motor Imagery (MI) EEG signals are acquired during mental tasks. In the ﬁeld of BCI, MI signals are generated when the subject only imagines a movement of a body part without actually performing it (Musallam et al., 2021). Similar to other BCI systems, MI-based BCI systems’ goal is to control one or more extrinsic devices by translating EEG signals into commands (Tiwari et al., 2022). Hence, the processing of these signals plays an important role in the design of assistive devices for motor-disabled and paralyzed persons (Degirmenci et al., 2022c).

In recent studies, the traditional handcrafted feature extraction processes have been studied to classify MI tasks. These studies analyze EEG signals using traditional machine learning methods. The handcrafted feature extraction process includes some basic and deﬁnite steps after acquiring EEG signals from subjects. These are signal preprocessing, feature extraction, feature selection, and classiﬁcation. Among these steps, the feature extraction and selection processes play an important role in EEG-based studies (Degirmenci et al., 2022b). The preprocessing step includes diﬀerent and signiﬁcant operations such as signal ﬁltering, signal normalization, artifact removal, and signal segmentation (Altaheri

- et al., 2021). In the feature extraction step, various approaches have been introduced to extract task-related intrinsic information from EEG signals by researchers. The MI features are separated into three categories based on the processing domain which are temporal features, spectral features, and spatial features.

Temporal features are supplied from the time domain of signals using time points or diﬀerent time segments and include features such as mean value, kurtosis, variance, skewness, root mean square value, and Hjorth parameters (Pawar and Dhage, 2020; Degirmenci et al., 2022b). Spectral features contain both frequency domain features such as power spectral density and fast Fourier transform (Djamal et al., 2017; Degirmenci et al., 2022c) and time-frequency domain features such as short-time Fourier transform (Ha and Jeong, 2019) and Wavelet transform (Chaudhary et al., 2020). Spatial features supply information about particular electrode locations on the brain cortex. The common spatial patterns (Blanco-Diaz et al., 2022) and its diﬀerent versions such as sparse common spatial patterns (Arvaneh et al., 2011), stationary common spatial patterns (Samek et al., 2012), divergence common spatial patterns (Samek et al., 2013), probabilistic common spatial patterns (Wu et al., 2014), and ﬁlter bank common spatial patterns (Ang et al., 2012) are the mostlystudied feature extraction methods to capture spatial information in MI task classiﬁcation. The compatibility of all these diﬀerent feature categories with the non-stationary structure of the EEG is important in determining the features to be used. According to the non-stationary structure of the EEG signals, the spectral components of the these signals change as a function of time. Thus, signal processing the EEG signals only in the time-domain or the frequency-domain might not be suﬃcient to provide information about the spectral characteristics of the EEG signals (Boashash, 2015). The combination of these diﬀerent categories should be analyzed in accordance with the nature of the EEG signals, using time-frequency domain features and non-linear parameters, in addition to the frequently used time-domain, frequency-domain, and spatial-domain features.

Although there are diﬀerent MI task features to analyze within MI EEG signals, the correlations among these features are signiﬁcant for algorithm performance. The simultaneous combination of a large number of various features unnecessarily increases the complexity of classiﬁers due to confusion caused by redundant information in the feature set. In addition, the classiﬁer performance decreases in some cases due to this confusion (Hart et al., 2000; Isler, 2009; Narin et al., 2014). As one of the solutions to this problem, all possible feature subsets can be deﬁned and the separability of each feature subset can be evaluated based on classiﬁer performance. Then, the relevant feature subset which provides the highest separability between MI tasks can be determined. Unfortunately, when too many features are studied, too many combinations need to be tried to explore the relevant and eﬀective feature set. However, such an approach requires and results in the computational load of classiﬁer algorithms (Narin et al., 2014). These feature

selection algorithms are classiﬁed into two main groups based on whether they consider a certain criterion for classiﬁer performance or not, which are wrapper and ﬁlter approaches, respectively (Blum and Langley, 1997; Kohavi and John, 1997; Guyon and Elisseeﬀ, 2003). Statistical signiﬁcance-based selection, backward elimination, forward selection, principal component analysis (PCA), and genetic algorithms (GAs) are mostly used feature selection algorithms to analyze biomedical signals in the literature (Isler, 2009; Narin et al., 2014; Mousa et al., 2016). In the classiﬁcation process, various machine learning algorithms have been computed to classify MI tasks such as Naive Bayes, k-nearest neighbors (k-NN), linear discriminant analysis, support vector machine, multi-layer perceptron, radial basis function, extreme learning machine, and deep neural network (Meziani et al., 2019; Degirmenci et al., 2022b,c; Tiwari et al., 2022). This study aims to introduce an eﬀective approach for MI task classiﬁcation using various features of EEG signals and diﬀerent machine learning algorithms. The main contributions of this study can be highlighted as follows:

- • We investigated a multi-directional handcrafted feature extraction-based approach that makes use of diﬀerent feature categories including temporal, spectral, and non-linear features.
- • We implemented the non-linear feature extraction method computing Poincare plot measurements of EEG signals to ensure the information about non-linear dynamics of signals in MI task classiﬁcation.
- • We investigated the performance eﬀect of the statistical signiﬁcance-based feature selection method on MI task classiﬁcation.
- • We comparatively evaluated the performance eﬀect of the seven diﬀerent machine learning algorithms with the combination of diﬀerent MI EEG features.

In the following section, we preferred to give a brief review of MI task studies separately from this introduction. Then, we gave methods and materials as a new section to explain the dataset used in addition to feature extraction, statistical signiﬁcance-based feature selection, classiﬁer algorithms, and performance evaluation metrics utilized in this study. Next, we introduced all the achieved classiﬁer performances in the Results section. In the last two separate sections, we discussed what these results mean and we concluded the outcomes of the study, respectively.

##  . Related works

The feature extraction and feature selection methods are critical steps for the prediction of MI-based EEG tasks since these steps have a direct impact on the classiﬁcation performance. In the literature, diﬀerent approaches were tested to extract MI features and determine which of them gives higher classiﬁer performances than other feature and classiﬁer combinations. MI EEG signals supply the temporal, spectral, and spatial features from their intrinsic structure. These features extracted diﬀerent features from diﬀerent categories can be combined to classify MI

tasks in research studies. In 2022, Degirmenci et al. presented a temporal feature extraction-based approach that uses 24 diﬀerent time-domain features. They also investigated the eﬀectiveness of the statistical signiﬁcance (ANOVA)-based feature selection process for the classiﬁcation of the four MI tasks (Degirmenci et al., 2022b). In classiﬁcation, 11 various machine learning algorithms were tested, and the maximum average accuracy value was found as 44.00% using linear discriminant analysis. In a study conducted by Hamedi et al., integrated EEG (IEEG) and root mean square (RMS) measures were extracted from the time domain of EEG signals. In the classiﬁcation of the three-class MI task, the eﬀectiveness of neural network-based algorithms, which are multi-layer perceptron and radial basis function neural networks, was investigated. The results revealed that RMS was more capable than IEEG for diﬀerentiating MI tasks, and radial basis function was more accurate and faster than multi-layer perceptron (Hamedi et al., 2014). The fast Fourier transform is one of the most applied methods to extract spectral features. In the study by Jusas and Samuvel (2019), band power, time domain parameters, fast Fourier transform, and channel variance were evaluated for the feature extraction process, and diﬀerent feature selection methods, which are PCA, sequential forward selection, sequential backward selection, locality preserving projections, and local Fisher discriminant analysis, were investigated. They concluded that the combination of fast Fourier transform and covariance matrix-based feature extraction with PCA-based feature selection supplied the best classiﬁcation performance among all combinations. In the literature, recent studies have investigated the eﬀect of EEG sub-bands using fast Fourier transform-based frequency band extraction. In 2019, Isa et al. presented a binary MI task classiﬁcation study based on the EEG frequency band extraction using the fast Fourier transform. The linear discriminant analysis was applied over these spectral features to minimize the number of feature dimensions. They evaluated the maximum accuracy value as 79.23% using the Naive Bayes algorithm for the classiﬁcation of right-hand and left-hand tasks (Isa et al., 2019). The main drawbacks of fast Fourier transform are two-fold: it is non-suitable for the non-stationary characteristic of EEG signals and it does not include time information. Therefore, diﬀerent methods which include time and frequency information were used to extract spectral features. Short-time Fourier transform is one of the time-frequency representation techniques that process the local characteristics of a signal utilizing a window. It supplies the spectral features using the time-frequency domain. In the study by Ha and Jeong (2019), the authors proposed a method for binary classiﬁcation of MI tasks using the short-time Fourier transform, and a capsule network (CapsNet). EEG signals were converted to 2D images using the short-time Fourier transform and these images were classiﬁed with CapsNet and other well-known machine learning algorithms. They concluded that CapsNet-based classiﬁcation outperforms all the other machine learning-based classiﬁcations with an average classiﬁcation accuracy of 78.44% in their presented study. Other time-frequency domain features can be extracted using Wavelet Transform. It supplies multiresolution analysis from EEG signals using several ﬁlters with diﬀerent bandwidths (Ha and Jeong, 2019). In a study presented by Luo et al., the eﬀect of the Wavelet packet decomposition-based

EEG subband extraction approach was investigated for the binary classiﬁcation (right-hand and left-hand movement tasks). They also applied the Dynamic frequency feature selection (DFFS) method to reduce the extracted features. They calculated the average accuracy value of 68.32% using random forest algorithm (Lu et al., 2020). In spatial feature extraction, the common spatial pattern algorithm is the most preferred method which uses spatial ﬁlters. In the study by Kato et al. (2020), a ﬁve-class MI task classiﬁcation study based on the multi-class common spatial patterns method was proposed. Five diﬀerent ﬁnger movements were diﬀerentiated with an accuracy of 40.60% using support vector machine. Unfortunately, the common spatial patterns’ drawback is the manual frequency band selection based on individual structures. The ﬁlter-bank common spatial pattern method, which utilizes several diﬀerent frequency bands in parallel, has been presented to overcome this problem. Adopting the FBSCP method improved the classiﬁcation performance for MI task studies (Ha and Jeong, 2019). In 2008, a common spatial pattern and ﬁlter-bank common spatial patternbased MI task classiﬁcation study is performed using publicly available BCI competition III dataset IVa. In the Naive Bayesian Parzen Window (NBPW)-based classiﬁcation, ﬁlter-bank common spatial pattern yielded superior averaged test accuracy of 81.10%, while the common spatial patterns-based approach yielded an accuracy of 73.30%. They concluded that ﬁlter-bank common spatial patterns supplied statistically outstanding performance than common spatial patterns (Ang et al., 2008).

In recent studies, it has been observed that three diﬀerent feature categories are generally used in the feature extraction process for MI-based EEG signals, but it has been noted that the most studied feature extraction approaches are the spectral domain and spatial domain features. Unfortunately, the eﬀect of non-linear features on MI task classiﬁcation has not been studied much. The Poincare plot measurements are one of the non-linear feature extraction methods that were studied in the analysis of diﬀerent biomedical signals and supplied high classiﬁcation results. Its simple visual interpretation and its proven clinical ability as a predictor of disease and cardiac dysfunction made this technique popular in the analysis of diﬀerent physiological signals (Isler and Kuntalp, 2007; Isler, 2009; Narin et al., 2014; Isler et al., 2019). Taking into account its performance in other studies (Isler and Kuntalp, 2009; Cancioglu et al., 2021), Poincare plot measurements can be an eﬀective method for non-linear dynamics of EEG signals that complicate the processing of them. Considering the contributions and deﬁciencies of the existing studies, in this study, a feature extraction method based on the combination of Poincare plot measurements from the non-linear feature extraction methods with temporal features and spectral features is implemented for MI task classiﬁcation.

##  . Materials and methods

In this section, the EEG dataset and methodologies that are adopted and used for feature extraction, feature selection, and classiﬁcation for MI-based EEG signals are described in detail. The ﬂowcharts of the suggested multi-class and binary class Motor Imagery task classiﬁcation studies are presented in Figures 1, 2, respectively.

 . . Dataset

In this study, the publicly available BCI Competition IV Dataset IIa was used to evaluate the performance of the classiﬁer methods for binary and multiple MI task classiﬁcation (Brunner et al., 2008). The dataset contains the EEG and EOG signals, which were captured and recorded using 22 EEG channels and 3 EOG channels, respectively. EEG signals were recorded using 22 Ag/AgCl electrodes, and the sampling rate was deﬁned as 250 Hz. The signals were collected for four diﬀerent MI tasks which are the imagination of movement of the left hand (LH), right hand (RH), feet (F), and tongue (T) from 9 subjects of which 4 were females and 5 were males. Two sessions were organized to collect EEG signals on diﬀerent days, and each session includes 6 runs separated by breaks. In each run, 48 diﬀerent MI tasks were available, and these trials were designed to be 12 MI tasks for each of the four classes. During the recording, a visual cue was shown to the subject to imagine the movements for four diﬀerent tasks. The preprocessing step of EEG signals includes a band-pass ﬁltering process between 0.5 and 100 Hz and an additional 50 Hz notch ﬁlter application to eliminate line noise for this dataset.

 . . Feature extraction

Initially, the relevant MI EEG segments, where EEG tasks were performed, are decomposed from original EEG signals for the feature extraction process. In this study, we extracted four feature sets of MI EEG features for the classiﬁcation of MI task segments. The ﬁrst set includes temporal features that are supplied from time-domain information of EEG segments. In the second set, spectral features are extracted using the fast Fourier transformbased frequency domain information of EEG segments. As a third set, time-frequency features are calculated based on Wavelet Transform. Finally, in the last set, Poincare plot measurements are calculated to extract non-linear features.

First, the relevant and distinctive temporal features are extracted based on the time-domain information of EEG signals. A total of 24 diﬀerent temporal features, which include information about amplitude and statistical changes of the EEG signals, are supplied for each EEG segment (Sayilgan et al., 2021a; Degirmenci et al., 2022b). These temporal features are minimum, maximum, mean, standard deviation, integrated EEG value, mean absolute value, simple square integral value, variance, root mean square value, waveform length value, average amplitude change value, absolute diﬀerence in standard deviation, mode value of the signal, kurtosis, skewness, Hjorth parameters (activity, mobility, and complexity) inter-quarter intervals (1st quartile, 2nd quartile, and 3rd quartile), zero crossing, slope-change value, and signal range.

Next, the EEG subbands’ energy, variance, and entropy values, and these values are calculated based on the frequency distribution of EEG signals. Hence, these spectral features include the information about frequency distribution embedded in EEG signals (Degirmenci et al., 2022c). The diﬀerent oscillations are embedded in EEG signals which are known to be liable for various cognitive brain functions (Cura and Akan, 2021). These are known as delta (δ), theta (θ), alpha (α), beta (β), and gamma

|[Figure 1]<br><br>FIGURE<br><br>The block diagram of the suggested multi-class Motor Imagery task classiﬁcation study. Three-second segments from EEG signals are used for the feature extraction process. Well-known classiﬁers are tested to discriminate the BCI command using selected features among extracted features (The dashed line representation refers to analyses in which ANOVA-based feature selection is applied, and statistically signiﬁcant features are applied to classiﬁers instead of all features.).|
|---|

(γ) waves. The frequency bands of these waves are identiﬁed

- as delta (0.5–4 Hz), theta (4–8 Hz), alpha (8–13 Hz), beta (13– 30 Hz), and gamma (30–100 Hz) for this study. The delta, theta, alpha, beta, and gamma bands are decomposed from the frequency distribution of MI EEG signals using the fast Fourier transform, and the energy, variance, and entropy values of these bands are calculated as spectral features. In the various EEGbased classiﬁcation problems, machine learning-based approaches commonly use the energy, variance, and entropy values of EEG subbands, which are calculated from the frequency domain of

signals as spectral features (Sayilgan et al., 2021c). Here, energy, variance, and entropy of frequency bands are calculated in the study by Sayilgan et al. (2021a) and Degirmenci et al. (2022c) as follows:

Energyf =

Variancef =

M

y(i)2 (1)

i=1

M

1 M − 1 ·

(yi − y)2 (2)

i=1

|[Figure 2]<br><br>FIGURE<br><br>The block diagram of the suggested binary class Motor Imagery task classiﬁcation study. Three-second segments from EEG signals are used for the feature extraction process. Well-known classiﬁers are tested to discriminate the BCI command using selected features among extracted features (The dashed line representation refers to analyses in which the independent t-test based feature selection is applied, and statistically signiﬁcant features are applied to classiﬁers instead of all features.).|
|---|

Entropyf =

1 log(M) ·

M

P(y(i))log(P(y(i)) (3)

i=1

Here, the energy of each frequency band is calculated based on the power spectrum, and f indicates the type of EEG subbands which are δ, θ, α, β, and γ. Energyf corresponds to the energy of a frequency band, and M corresponds to the maximum frequency. The Fourier Transform of the EEG segment is indicated as y. Variancef corresponds to the variance of a frequency band, and

y denotes the average of the y signal. The spectral entropy measures the regularity of the power spectrum of the EEG signal, and Entropyf corresponds to the entropy of a frequency band. P(y(i)) indicates the probability that the signal is in the given frequency domain.

Then, Wavelet Transform-based feature extraction process is conducted to calculate time-frequency features. EEG signals have non-stationarities and their spectral features do not include any time information. Wavelet Transform uses both time and

frequency information and supplies multi-resolution analysis using several ﬁlters and bandwidths. It is a smooth and fast oscillation function that is well-localized in frequency and time (Sayilgan et al., 2021b). It can be used as a specially prepared dual Finite-Impulse Response (FIR) ﬁlter. The high-frequency and low-frequency components of EEG signals are extracted using frequency responses of FIR ﬁlters. Half of the data sampling rate is known as Nyquist frequency. The dividing point of the signal frequency is generally between 0 Hz and the speciﬁed Nyquist frequency. The same wavelet coeﬃcients are employed in both low-pass (LP) and high-pass (HP) ﬁlters for the multi-resolution algorithm of Wavelet Transform (Gandhi et al., 2011). The LP ﬁlter coeﬃcients are linked with a scaling parameter that deﬁnes the oscillatory frequency and the length of the wavelet, whereas the HP ﬁlter is linked with the wavelet function. The outputs of the LP ﬁlters and HP ﬁlters are denoted as the approximation (a) coeﬃcients and detail (d) coeﬃcients, respectively. EEG time signals can be completely divided into (a) and (d) coeﬃcients depending on the decomposition level. The analysis of diﬀerent statistical and non-statistical parameters over time and frequency can be performed by applying the Wavelet Transform to EEG signals. The subsets of the relevant coeﬃcients of decomposition levels are categorized based on the frequency domain of EEG subbands for the extraction of EEG frequency bands. In this study, the Wavelet packet decomposition-based EEG subband extraction is used to calculate time-frequency features. The MI EEG signals are decomposed into seven decomposition levels. The approximation ai and detail di coeﬃcients were obtained for the decomposition levels of i = 1, 2,..., 7 for 250 Hz sampling frequency.

The various Discrete Wavelet Transform functions (Haar, Db2, Sym4, Coif1, Bior3.5, and Rbior2.8) can be used in Wavelet Transform-based feature extraction. There are several types of mother wavelets; therefore, determining a suitable mother wavelet is an important step. In the study by Sayilgan et al. (2021a), researchers conducted a study to deﬁne the eﬀective wavelet function in steady-state visual-evoked potential (SSVEP) signals. The results of the study showed that the most successful wavelet function was the Haar wavelet. Hence, in this study, the Haar wavelet function was applied to the Wavelet packet decomposition process. MI EEG signals are subdivided into frequency bands (δ, θ, α, β, and γ) from ai and di coeﬃcients. The energy, variance, and entropy of these frequency bands are calculated as time-frequency features. The energy of each decomposition level was computed corresponding to the following equation (Gandhi et al., 2011):

Energydi =

Energyai =

N

|dij|2,i = 1,2,3,...,l (4)

j=1

N

|aij|2,i = 1,2,3,...,l (5)

j=1

In the equations, detail (di) and approximate (ai) coeﬃcients are used to supply subsets of each EEG frequency band (δ, θ, α, β, and γ) from the decomposition tree. The (a) and (d) coeﬃcients of these frequency band subsets are denoted with dij and aij, respectively. i = 1,2,3,l corresponds to the wavelet decomposition level that takes value from 1 to l. The number of d and a coeﬃcients

- at each decomposition level is indicated with N.

By using the following equation, the entropy of each decomposition level is calculated (Isler, 2009).

Entropyi =

N

dij2log(dij2),i = 1,2,3,...,l (6)

j=1

The variance of each decomposition level is computed as follows (Gandhi et al., 2011):

Variancei =

µi =

N

1 N − 1 ·

(dij − µi)2,i = 1,2,3,...,l

j=1

N

1 N ·

dij,i = 1,2,3,...,l (7)

j=1

Hence, µi expresses the mean of the decomposition level. In the last feature extraction process, the non-linear parameters are extracted in addition to the temporal, spectral, and timefrequency features. MI EEG signals have non-linear dynamics in their characteristics. In recent studies, Poincare plot measures were commonly used as non-linear measures to analyze the diﬀerent EEG signals. It characterized the non-linear dynamics inherent in the signal. The Poincare plot is a graph of each EEG sample (xi) on the x-axis and the next EEG sample (xi+lag) on the y-axis (Isler, 2009). In the x and y axes, (xi) and (xi+lag) intervals are placed to ensure the Poincare plot, respectively. The Poincare plot-based feature extraction process is adopted for this study, considering its favorable outcomes in the literature such as its simple visual interpretation and proven clinical ability (Isler and Kuntalp, 2007; Isler, 2009; Narin et al., 2014; Isler et al., 2019; Cancioglu et al., 2021). These drawings are procured from raw MI EEG segment data after deﬁning (xi) and (xi+lag) intervals within EEG segments. An ellipse is ﬁtted to the Poincare plot graph, and the standard deviation of the distance of the points on these plots indicates the width (SD1) and length (SD2) of the ellipse (Brennan et al., 2001). Poincare plot measures can be calculated as follows (Isler, 2009; Isler and Kuntalp, 2009):

xi = (x0,x1,...,XN−m) (8) xi+lag = (xm,xm+1,...,XN) (9)

xi+lag − xi √2 xb =

xa =

xi+lag + xi √2

(10)

SD1 = SD(xa) SD2 = SD(xb) (11)

where xi and xi+lag represent the EEG segment data and the next EEG data interval in the Equations (8) and (9), respectively. With respect to deﬁned intervals, SD1 and SD2 measurements were calculated utilizing Equations (10) and (11). SD indicates

the standard deviation of the extracted time interval vectors in Equation (11). The m-lagged Poincare plot measurements were conducted to deﬁne diﬀerent intervals. SD1 and SD2 measurements are calculated considering lag=m and m was set as 1 and 9 for this study. In this study, Poincare plot measures for lag=9 were also calculated due to the positive eﬀect on MI EEG signal classiﬁcation (Degirmenci et al., 2022a). In our previous study (Degirmenci

- et al., 2022a), we investigated the performances of diﬀerent feature vectors which were extracted from 10 lag values and the feature vector which is the combination of these vectors, separately. The results demonstrated that the most discriminative and eﬀective feature set is the ninth feature vector that includes the features extracted when the lag value is deﬁned as 9. The values of (SD1) and (SD2), for which we determined the m values as 1 and 9, were calculated. In addition, in addition to (SD1) and (SD2) calculations,

the products (SD1SD2) and the rates (SD1/SD2) are calculated to investigate the relationships between these components. A total of four non-linear features were extracted for lag=1 condition. In our Poincare plot process, eight non-linear features were extracted from lag=1 and lag=9 conditions for each EEG segment.

 . . Statistical signiﬁcance-based feature selection

The feature selection process aims to determine the relevant and eﬀective features that will supply the highest discrimination between the classes of interest and also can minimize the complexity of classiﬁers (Isler et al., 2023). In this study, the statistical signiﬁcance-based feature selection is applied to indicate the most eﬀective combination of temporal, spectral, time-frequency, and non-linear features which provides the best discrimination of the MI tasks (Narin et al., 2014; Sayilgan et al.,

- 2021b; Degirmenci et al., 2022b). This statistical signiﬁcancebased feature selection approach is applied for each MI EEG feature set separately. In this study, two diﬀerent classiﬁcation models, which are binary and multi-class MI task classiﬁcations, are studied. Hence, two diﬀerent types of statistical signiﬁcancebased feature selection were used, i.e., the independent t-test and one-way analysis of variance (ANOVA test). The selected tests were determined considering the class number of the classiﬁcation models. In binary classiﬁcation, the independent t-test, which is commonly applied to deﬁne the signiﬁcance of diﬀerences between measures of two diﬀerent classes, is used for feature selection (Narin et al., 2014; Degirmenci et al., 2022c). In multi-class classiﬁcation, the ANOVA test is adopted for feature selection (Bulut et al.,
- 2022; Degirmenci et al., 2022b). ANOVA is a test applied when it is required to determine whether there is a diﬀerence between the means in conditions where there are two or more groups. Thus, the eﬀects of the independent t-test and ANOVA test-based feature selection methods were investigated with temporal, spectral, time-frequency, and non-linear features. The statistical signiﬁcance of every MI EEG feature were deﬁned by calculating p-values. The statistical signiﬁcances are measured based on the statistical signiﬁcance level (α) equal to 0.05. A total of two feature sets containing the features that provide the statistical evidence range were obtained after the signiﬁcant features were determined using

the feature selection models (the independent t-test and ANOVA) for both two classiﬁcation models. These selected feature vectors were given to the classiﬁcation algorithms as input data to predict the MI tasks.

 . . Classiﬁcation

In this study, the MI EEG features described in the previous feature extraction section are used to predict MI tasks of EEG segments. We also compare the performance of the binary (RH and LH) and multi-task (RH, LH, F, and T) classiﬁcations using extracted features from temporal, spectral, time-frequency, and non-linear methods. The diﬀerent versions of six diﬀerent basic classiﬁers are computed to classify the extracted features (Hart et al., 2000). Hence, 24 diﬀerent classiﬁcation methods are tested considering the diﬀerent sub-parameters of 6 classiﬁer algorithms (Sayilgan et al., 2021a; Degirmenci et al., 2022a). The set of classiﬁers contains decision trees (ﬁne, medium, and coarse), discriminant analysis (linear, quadratic), Naive Bayes (Gaussian, Kernel), support vector machine (linear, quadratic, cubic, ﬁne Gaussian, medium Gaussian, and coarse Gaussian), k-NN (ﬁne, medium, coarse, cubic, cosine, and weighted), and ensemble learning (boosted, bagged, subspace discriminant, subspace kNN, and RUSBoosted Trees) algorithms. All these classiﬁcation algorithms with diﬀerent sub-parameters are available in the “Classiﬁcation Learner” application of Matlab. Additionally, the logistic regression algorithm is tested for binary classiﬁcation (Degirmenci et al., 2022c).

 . . . Decisions trees

The decision tree is a machine learning algorithm that can divide the data into several diﬀerent sub-groups and can also be utilized for classiﬁcation outside of the regression process. The characteristic tree-like structure of this algorithm which includes branches and nodes gives the name of the algorithm (Tzallas et al., 2009). The training process is carried out based on learning a set of decision rules. A leaf node is created when the decision is made, whereas a decision node which is another branch is generated when the decision is not deﬁnite (Cura and Akan, 2021). In the decision tree-based classiﬁcation process, the ﬁne, medium, and coarse algorithms are used for this study.

 . . . Discriminant analysis

The discriminant analysis classiﬁer is one of the pattern recognition methods, and its main purpose is to correctly divide the independent variables in the data into homogeneous groups. In this study, the classiﬁcation is carried out using both linear and quadratic algorithms from the discriminant analysis. Linear discriminant analysis from these classiﬁers determines the group elements and calculates the probability that each element belongs to diﬀerent groups. Then, the element is assigned to the group with the highest probability score. Linear discriminant analysis assumes that the predictors are normally distributed (Gaussian distribution). It also creates a linear discrimination function that assumes diﬀerent classes have class-speciﬁc elements and equal variance/covariance.

Unlike the linear discriminant analysis algorithm, in the quadratic discriminant analysis algorithm, variance/covariance equality is not accepted. The covariance matrix for quadratic discriminant analysis may be diﬀerent for each class category. Hence, it conﬁgures the discriminant function to be quadratic (Hart et al., 2000; Lotte et al., 2018).

 . . . Naive Bayes

Naive Bayes is a classiﬁer algorithm that utilizes Bayes’ theorem based on probability which is connected to the relationship between marginal and conditional probabilities (Hart et al., 2000). In the working principle of the algorithm, all features are regarded to be independent, and this is also the reason for using the name “Naive”. However, all features have the same eﬀect value on classiﬁcation, which means each of the features has an equal weight in the training (Tzallas et al., 2009). It is the mostly preferred algorithm in machine learning approaches due to its simple calculation mechanism created by the non-realistic approach (Cura and Akan, 2021; Sayilgan et al., 2021a; Degirmenci et al., 2022b). The Gaussian and Kernel algorithms of this Naive Bayes classiﬁer were computed for this study.

 . . . Support vector machine

Support vector machine is a well-known supervised learning algorithm, which is a non-probabilistic approach that uses the geometric characteristics of input data. It is mostly used in both classiﬁcation and regression studies. N dimensional space is created utilizing the elements of the coordinate systems. These elements consist of the data including n features. The decision boundaries, which are named “hyperplane”, are generated to discriminate the input data into diﬀerent classes. Although many hyperplanes can be deﬁned to categorize the diﬀerent classes in the process, the optimum hyperplane that separates the diﬀerent classes best is selected to provide a more accurate classiﬁcation. The distance between the “support vectors” that belong to diﬀerent class categories is deﬁned as the “margin”. In this algorithm, the maximum margin is a critical parameter. The data placed on diﬀerent parts of the hyperplane are indicated as a component of a diﬀerent class (Vapnik, 1999; Hart et al., 2000; Lotte et al., 2018). All diﬀerent types of support vector machine classiﬁers were computed in this study, i.e., linear, quadratic, cubic, ﬁne Gaussian, medium Gaussian, and coarse Gaussian algorithms.

(Hart et al., 2000). In this study, ﬁne, medium, coarse, cubic, cosine, and weighted algorithms of the k-NN classiﬁer were executed. “Euclidean” distance measurement method is one of the most selected distance calculation methods (Isler, 2009; Cura and Akan, 2021). Hence, it was selected and adopted for the execution of ﬁne, medium, coarse, and weighted algorithms in this study. Additionally, “cubic” and “cosine” distance metrics were used in cubic and cosine algorithms, respectively.

 . . . Logistic regression

The basic concept of logistic regression is the modeling of the probability of an event. The probability value is deﬁned as a continuous variable, and two diﬀerent outputs are available in logistic regression-based classiﬁcations. Hence, this algorithm can be used for binary classiﬁcation studies. In the process, the logistic function which is also deﬁned as the sigmoid function is ﬁtted to the input data utilizing probability (Tzallas et al., 2009). The logistic regression algorithm projects the data points based on a line and all log-odd values evaluated. These log-odd values which are considered inputs are converted to probability values. These calculated probability values are deﬁned as outputs of the algorithm. Hence, the sigmoid function is ﬁtted using this input– output transformation. The diﬀerent line rotations are tested by calculating, logging, and summing conditional probabilities for all steps. Then, the best ﬁtting function which obtained the maximum probability is evaluated (Alkan et al., 2005).

 . . . Ensemble learning

Ensemble learning is a meta-algorithm that combines multiple machine learning techniques into a single prediction model (classiﬁer) to reduce variance (bagging), bias (boosting), and/or improve predictions by preventing the overﬁtting problem. This algorithm generally assumes that a single classiﬁer cannot achieve certain and precise classiﬁcation accuracy due to possible noise, overlapping data distributions, and outliers in the data. Hence, this algorithm supposes that there is no single model (classiﬁer) that works best for every classiﬁcation problem (Sayilgan et al., 2021b). Consequently, recently, ensemble learning methods have become frequently preferred classiﬁcation algorithms in the recent literature. In this study, the algorithms of Boosted, Bagged, Subspace Discriminant, Subspace k-NN, and RUSBoosted Trees which are developed under ensemble learning classiﬁers are tested since they have been implemented in Matlab already.

 . . . K-nearest neighbors (KNN)

KNN is a successful machine learning algorithm that is mostly preferred in classiﬁcation and regression processes. The learning process is carried out based on the data in this algorithm (Isler et al., 2023). As a ﬁrst step, the distance between the sample to be predicted and all input data in the training set is calculated. Among the k-nearest neighbors, those which provide the minimum distance are determined. Then, the class of the new sample is indicated as the most common class among these kNearest Neighbors (Isler, 2009; Tzallas et al., 2009). The distance calculation can be performed using diﬀerent distance measurement methods such as Euclidean, Manhattan, Minkowski, and Hamming

###  . . Performance evaluation metrics

In the performance evaluation of classiﬁcation results, the reel label of MI EEG segments was compared with the predicted label assigned by classiﬁer algorithms. The MI tasks classiﬁcation results of the classiﬁers are calculated using true positive (TP), true negative (TN), false positive (FP), and false negative (FN). These values are calculated from the confusion matrix, and they are used to calculate accuracy (ACC) performance metric.

On the other hand, the k-fold cross-validation (CV) method is computed to evaluate classiﬁer performance. k-fold CV randomly

separated the extracted feature set as k diﬀerent folds with equal sizes. Among these folds, the (k-1) fold is used as training data, and the remaining one-fold is used as test/validation data. In each classiﬁcation, this process is repeated k times, and accuracy values are calculated for each iteration. At the end of the k iterations, the average accuracy value of the classiﬁcation is calculated. In this study, the k value is chosen as 5 to apply the k-fold CV method. Additionally, 10 repeated tests were performed to check the repeatability of classiﬁcation results. The mathematical formulas of performance metric computed to evaluate the classiﬁer performance are expressed in the following equations (Hart et al., 2000; Isler, 2009; Degirmenci et al., 2021):

TP + TN TP + TN + FP + FN × 100 (12)

ACC (%) =

Here, while the number of data that actually belongs to a class and is marked to the same class by the classiﬁer is expressed as TP, the number of data incorrectly marked to a diﬀerent class is also expressed as FN. However, the number of data that actually belongs to a diﬀerent class and is marked to a diﬀerent class by the classiﬁer is expressed as TN, and the number of data incorrectly marked to the same class is expressed as FP.

##  . Results

In this study, we aim to classify MI tasks of EEG segments using all extracted features and statistically signiﬁcance-based selected features only. As the implementation details of this study, the segmentation of EEG signals, feature extraction, and classiﬁcation steps in the study was performed in MATLAB application. In the feature selection process, the software package “IBM SPSS Statistics 25”, which is generally used in statistical analysis, was used to perform the independent t-test for the 2-class task and the ANOVA test for the multiple-class task. The p-values which deﬁne the statistical signiﬁcance are also found using this software program.

EEG signals are supplied from BCI Competition IV Dataset IIa in this study. MI EEG segments are extracted for 22-channel EEG recordings of 9 subjects. The feature set is calculated from temporal, spectral, time-frequency, and non-linear methods. In the time domain, 24 diﬀerent features were extracted from 22 EEG channels for each MI EEG task sample. Hence, a total of 528 temporal features were supplied for each sample. The detailed description of 528 temporal features is “(number of EEG channels) × (number of features)”. The spectral features, energy, entropy, and variance of EEG sub-frequency bands (δ, θ, α, β, and γ) were calculated using fast Fourier transform-based frequency band extraction. These spectral features were extracted from 22 EEG channels for each MI EEG task sample. Hence, a total of 330 spectral features were supplied for each sample. In the time-frequency domain, energy, entropy, and variance of EEG sub-frequency bands (δ, θ, α, β, and γ) were calculated using Wavelet Transform-based frequency band extraction. These time-frequency features were calculated from 22 EEG channels for each MI EEG task sample. Then, a total of 330 spectral features were supplied for each sample. The detailed description for both 330 spectral and 330 time-frequency features

is “(number of EEG channels) × (number of frequency subbands) × (number of features)”. As non-linear features, the values of (SD1) and (SD2), the product (SD1xSD2), and the ratio (SD1/SD2) were calculated from 22 EEG channels for each MI EEG task sample. The non-linear features were calculated for 2 diﬀerent lag conditions, and a total of 176 non-linear features were supplied for each sample in the assumption of both lag=1 and lag=9. The detailed description for 176 non-linear features is “(number of lag conditions) × (number of EEG channels) × (number of features)”. The “(2592 × 1364)” feature vector which includes 2,592 samples and 1,364 features was supplied for multi-task classiﬁcation at the end of the feature extraction process for all subjects. The “(1296 × 1364)” feature vector which includes 1,296 samples and 1,364 features was supplied for binary classiﬁcation at the end of the feature extraction process for all subjects. In addition to the feature extraction process, we also aimed to investigate the eﬀectiveness of the statistical signiﬁcance-based feature selection method for both multi-task and binary classiﬁcation. The statistically signiﬁcant features were deﬁned based on the statistical signiﬁcance level using the ANOVA test and independent t-test for multi-task and binary classiﬁcation processes, respectively. The results of ANOVA-based statistical analysis show that 673 out of 1,364 features yielded a signiﬁcant p-value for multi-task classiﬁcation. The independent t-test-based statistical analysis showed that 91 out of 1,364 features yielded a signiﬁcant p-value for binary classiﬁcation. The extracted and selected feature sets were given to the classiﬁer algorithms using ﬁve-fold cross-validation to predict the MI tasks of samples. Finally, various classiﬁers such as decision tree, discriminant analysis, Naive Bayes, support vector machine, k-NN, logistic regression, and ensemble learning were utilized for the classiﬁcation. The results of each classiﬁer algorithm were evaluated based on the 10 repeated tests. Then, the average accuracy values of these repeated tests were evaluated for each classiﬁcation process.

Tables 1, 2 show the accuracy-based performance evaluation results of the study. In the tables, the highest classiﬁcation result for the related component is indicated with boldface numbers. The performance evaluation of the binary classiﬁcation is presented in Table 1. In the table, “1st Task” indicates that the classiﬁcations were performed using the feature set combining the time-domain, frequency-domain, time-frequency domain features, and nonlinear parameters. On the other hand, “2nd Task” denotes that classiﬁcations were performed using the selected feature set by a statistically signiﬁcant (the independent t-test) based feature selection method. Among all 1st task classiﬁcations, the highest average accuracy value of 57.30% is achieved using the ensemble boosted trees algorithm and all features. In the 1st task, there are N/A results among classiﬁcation results due to the fact that the prepared feature set does not provide suitable parameters for the structure of the classiﬁer. In addition, the highest average accuracy value of 61.86% is achieved using the ensemble subspace discriminant algorithm and selected features by the independent t-test among all 2nd task classiﬁcations.

To investigate the eﬀect of the study on the four-task classiﬁcation task, the feature set is prepared to extract the same features from EEG signals. Additionally, the signiﬁcant features are determined using the statistical signiﬁcance (ANOVA test)-based feature selection method, and the selected feature set is obtained.

The four-task classiﬁcation performance results are presented in Table 2. As the previous table, “1st Task” indicates that the classiﬁcations are performed using the feature set by combining the time-domain, frequency-domain, time-frequency domain features, and non-linear parameters. On the other hand, the “2nd Task” indicates that the classiﬁcations are performed using the selected feature set by statistical signiﬁcance (ANOVA test)-based feature selection method. The highest classiﬁcation average accuracy value of 35.60% is obtained using ensemble boosted trees among all 1st task classiﬁcations. On the other hand, the highest classiﬁcation average accuracy value of 47.36% is obtained with the ensemble subspace discriminant algorithm among all 2nd Task classiﬁcations.

In addition to accuracy-based performance evaluations, the sensitivity and speciﬁcity values were also calculated for only ensemble subspace discriminant algorithm-based classiﬁcation since it provides the highest average accuracy value for both the binary and four-task classiﬁcations. These results are presented in Table 3. SEN and SPE values are calculated as 47.61% and 82.54% for the four-task classiﬁcation in the 2nd Task, respectively. On the other hand, for the binary MI task classiﬁcation, 65.28% SEN and 58.49% SPE values are calculated with the ensemble subspace discriminant classiﬁer in the 2nd Task.

##  . Discussion

In this study, we introduced a multi-directional handcrafted feature extraction-based approach for the representation and classiﬁcation of multi-channel MI EEG signals. In the study, temporal features, spectral features, time-frequency features, and non-linear parameters of EEG signals are extracted. In addition, the eﬀect of the statistical signiﬁcance-based feature selection method is investigated to indicate signiﬁcant and eﬀective features from extracted feature set which includes the combination of various MI EEG features. The binary and multi-task classiﬁcation studies were performed with the same feature extraction approach. In these studies, two diﬀerent scenarios are available. “1st Task” denotes the classiﬁcations of the feature set that includes all features. “2nd Task” denotes the classiﬁcations of the selected feature set that includes statistically signiﬁcant features. The extracted and selected feature sets are classiﬁed using 24 diﬀerent classiﬁer algorithms. In the binary classiﬁcation process, logistic regression is also used. The accuracy, sensitivity, and speciﬁcity-based performance evaluations are performed to analyze the classiﬁer performances implemented in this study.

In the binary classiﬁcation task, classiﬁcation could not be performed in 9 of all classiﬁers, and the highest average accuracy among the remaining classiﬁcations was achieved with ensemble boosted trees for the 1st task. On the other hand, for the 2nd task, it was possible to classify with all classiﬁers and the highest average accuracy value was obtained with the ensemble subspace discriminant algorithm. Moreover, the aim of the study included the investigation of statical signiﬁcance-based feature selection in binary classiﬁcation. To investigate the eﬀectiveness of the independent t-test-based feature selection approach, 1st and 2nd scenarios of Table 1 are compared. It was observed that the feature selection method based on the independent t-test increased the performance in 13 classiﬁers, decreased the performance in 2

TABLE Binary classiﬁcation performance of the time-domain, frequency-domain, time-frequency domain, and non-linear features and the e ectiveness of the independent t-test-based feature selection.

|Classiﬁer algorithms|Classiﬁer accuracies (%)| |
|---|---|---|
| | st Task<br><br>| nd Task|
|Fine Tree<br><br>|54.10<br><br>|56.50|
|Medium Tree<br><br>|56.10|55.20<br><br>|
|Coarse Tree|56.60<br><br>|55.90|
|Linear Discriminant Analysis|N/A<br><br>|52.10|
|Quadratic Discriminant|N/A<br><br>|52.00|
|Logistic Regression|N/A|51.10<br><br>|
|Gaussian Naive Bayes<br><br>|48.20<br><br>|57.10|
|Kernel Naive Bayes|48.50<br><br>|55.70|
|Linear Support Vector Machine<br><br>|N/A|51.40<br><br>|
|Quadratic Support Vector Machine<br><br>|N/A|51.10<br><br>|
|Cubic Support Vector Machine<br><br>|N/A<br><br>|50.70|
|Fine Gaussian Support Vector Machine|N/A<br><br>|49.40|
|Medium Gaussian Support Vector Machine<br><br>|N/A<br><br>|51.20|
|Coarse Gaussian Support Vector Machine|N/A<br><br>|51.20|
|Fine K-Nearest Neighbors|49.80<br><br>|50.20|
|Medium K-Nearest Neighbors<br><br>|49.80|50.30|
|Coarse K-Nearest Neighbors|49.80|49.80<br><br>|
|Cosine K-Nearest Neighbors<br><br>|49.80<br><br>|50.40|
|Cubic K-Nearest Neighbors<br><br>|49.80<br><br>|50.70|
|Weighted K-Nearest Neighbors|49.80<br><br>|50.80|
|Ensemble Boosted Trees<br><br>|57.30|58.40<br><br>|
|Ensemble Bagged Trees|53.14|55.91<br><br>|
|Ensemble Subspace Discriminant<br><br>|51.94<br><br>|61.86|
|Ensemble Subspace K-Nearest Neighbors<br><br>|50.28|50.69<br><br>|
|Ensemble RUSBoosted Trees|55.84|56.32|

The 1st task indicates that all features are used, and the 2nd task shows that only t-testselected features are used in the classiﬁer inputs. Bold values indicate the maximum classiﬁer performances for the given task.

classiﬁers, and did not change the performance in 1 of them. We should note that considering the signiﬁcant improvement in classiﬁer performances, the independent t-test-based feature selection may be used as an eﬀective feature extraction approach for binary classiﬁcation studies.

In multi-task classiﬁcation approaches for the 1st task, two algorithms from all classiﬁers could not be used for the classiﬁcation of MI tasks, and the ensemble boosted trees algorithm yielded the highest average accuracy value among the remaining classiﬁers. In the 2nd Task, all classiﬁers were used for classiﬁcation, and the highest average accuracy value was acquired with the ensemble subspace discriminant algorithms. ANOVA test-based feature selection process was performed to predict statistically signiﬁcant features. Hence, the 1st and 2nd tasks of Table 2 are compared to determine the eﬀectiveness of this

TABLE Multi-task classiﬁcation performance of the time-domain, frequency-domain, time-frequency domain, and non-linear features and the e ectiveness of the independent t-test-based feature selection.

|Classiﬁer algorithms|Classiﬁer accuracies (%)| |
|---|---|---|
| | st Task| nd Task<br><br>|
|Fine Tree|31.80<br><br>|32.51|
|Medium Tree<br><br>|34.50<br><br>|34.50|
|Coarse Tree<br><br>|33.10|33.61|
|Linear Discriminant Analysis<br><br>|N/A|27.31|
|Quadratic Discriminant<br><br>|N/A|25.73|
|Gaussian Naive Bayes<br><br>|27.90|29.09|
|Kernel Naive Bayes<br><br>|27.30<br><br>|29.43|
|Linear Support Vector Machine|25.00<br><br>|27.42|
|Quadratic Support Vector Machine|25.00<br><br>|27.09|
|Cubic Support Vector Machine|25.00<br><br>|27.00|
|Fine Gaussian Support Vector Machine<br><br>|25.00|26.20|
|Medium Gaussian Support Vector Machine<br><br>|25.00|26.78|
|Coarse Gaussian Support Vector Machine|25.00|26.85<br><br>|
|Fine K-Nearest Neighbors|24.90<br><br>|25.65|
|Medium K-Nearest Neighbors|24.90|25.80<br><br>|
|Coarse K-Nearest Neighbors<br><br>|24.90|25.68|
|Cosine K-Nearest Neighbors|24.90<br><br>|26.21|
|Cubic K-Nearest Neighbors<br><br>|24.90|25.67|
|Weighted K-Nearest Neighbors|24.90|26.00<br><br>|
|Ensemble Boosted Trees<br><br>|35.60|36.41|
|Ensemble Bagged Trees|32.83<br><br>|35.28|
|Ensemble Subspace Discriminant<br><br>|27.14<br><br>|47.36|
|Ensemble Subspace K-Nearest Neighbors|25.28<br><br>|28.48|
|Ensemble RUSBoosted Trees|34.92<br><br>|34.77|

The 1st task indicates that all features are used, and the 2nd task shows that only ANOVAselected features are used in the classiﬁer inputs. Bold values indicate the maximum classiﬁer performances for the given task.

statistical signiﬁcance-based feature selection process on multiple MI task classiﬁcation. According to Table 2, the classiﬁcation was performed using ANOVA test selected features for two classiﬁers. It was observed that the feature selection method based on the ANOVA test increased the performance in 20 classiﬁers, decreased the performance in 1 classiﬁer, and did not change the performance in 1 of them. Hence, the ANOVA test-based dimensionality reduction of EEG features approach is an eﬀective feature selection method that provides a signiﬁcant improvement in classiﬁer performances for multiple MI task classiﬁcation studies. In binary and multiple MI task classiﬁcation, experimental results revealed that the selected statistically signiﬁcant features introduced in this study outperform the results achieved using all EEG features.

In Table 3, we summarize some of the previous binary and multiple MI task classiﬁcation studies and compare their performances with the performance of the study. The details of

the studies including dataset, channel selection, feature extraction approaches, feature selection method, classes (binary or multiple), classiﬁer algorithms, and classiﬁcation performances based on the various metrics (ACC, SEN, and SPE) are given in Table 3 for eﬀective comparison of these studies. In the study by Degirmenci et al. (2022b), the multiple (left hand, right hand, feet, and tongue) tasks were tried to be diﬀerentiated using 24 diﬀerent timedomain features which were extracted from 22 channel EEG signals. On the other hand, the eﬀectiveness of ANOVA-based feature selection was investigated, and the highest average accuracy was calculated as 44.30% using only statistically signiﬁcant features. Each introduced feature extraction method of EEG signals is a factor that plays a signiﬁcant role in the classiﬁcation success of the study. In our study, the frequency domain, time-frequency domain, and non-linear parameters are also introduced, and these features provide higher success rates than that of their study. In the study by Degirmenci et al. (2022c), the independent ttest-based feature selection approach was performed using timedomain and frequency-domain features. All EEG channels of the BCI Competition IV Dataset-IIa were used for binary classiﬁcation, and the highest average accuracy value of 62.52% was obtained. Their results revealed that the independent t-test-based feature selection process of that study generally improves the classiﬁer performances. They reported higher average accuracy values than the ones in our study, but in their study, they did not use the timefrequency domain and non-linear features. In another study, Lu et al. (2020) used BCI Competition IV Dataset-IIa, and Wavelet packet decomposition-based binary classiﬁcation was adopted. The accuracy value of 68.32% was achieved with the random forest classiﬁer algorithm, and the reported value is higher than our binary classiﬁcation results. However, in that study, both channel selection (C3 and C4) and DFSS-based feature selection processes were conducted. Since the feature selection provides the important features among all features from all EEG channels, a channel selection process is not adopted in our study. In the study by Kato et al. (2020), ﬁve ﬁnger movements are predicted using 21 EEG channels of the MISCP dataset. Multi-class common spatial pattern-based features were diﬀerentiated using support vector machine, and an accuracy value of 40.60% was achieved. Although more EEG channels were evaluated, the reported accuracy value was lower. If they adopted a feature selection algorithm for their study, they might reach a higher classiﬁer performance. In addition, as the number of classes to be classiﬁed increases, the success of multi-task classiﬁcations remains at lower levels compared to the binary classiﬁcation as in that study and our study. In another study, Sakhavi et al. (2015), ﬁlter-bank common spatial patterns and energy-based features are extracted using 22 EEG channels of BCI Competition IV Dataset-IIa. Then, convolutional neural networks were used to classify four diﬀerent MI tasks, and an accuracy value of 70.60% was achieved. The reported classiﬁcation result was higher than the accuracy achieved in our study. Although convolutional neural network-based approaches might increase the classiﬁcation success, the training time generates a high computational load for the designed system. However, the computational complexity of our feature extraction, feature selection, and classiﬁcation processes is lower than in convolutional neural network-based studies. In the study by Garcia-Laencina et al. (2014), a feature extraction process including band power features,

TABLE Comparison of various multi-class and binary Motor Imagery task classiﬁcation studies with the results of the study.

|Study|Channels|Classes<br><br>|Classiﬁer|ACC (%)<br><br>|
|---|---|---|---|---|
|Degirmenci et al. (2022b)<br><br>|22|4<br><br>|Linear Discriminant Analysis<br><br>|44.00|
|Degirmenci et al. (2022c)<br><br>|22<br><br>|2|Ensemble Subspace Discriminant<br><br>|62.52|
|Lu et al. (2020)|2<br><br>|2|Random Forests|68.32|
|Kato et al. (2020)<br><br>|21|5|Support Vector Machines<br><br>|40.60|
|Sakhavi et al. (2015)|22<br><br>|4|Convolutional Neural Network<br><br>|70.60|
|Garcia-Laencina et al. (2014)|2<br><br>|5<br><br>|Linear Discriminant Analysis|77.30|
|Jusas and Samuvel (2019)<br><br>|8|4<br><br>|Support Vector Machines|56.00<br><br>|
|Nguyen et al. (2018)<br><br>|22|4|Fuzzy Logic System|65.00<br><br>|
|Lindig-Leon and Bougrain (2015)<br><br>|26|4<br><br>|Linear Discriminant Analysis|51.67<br><br>|
|Ma et al. (2018)|64<br><br>|5<br><br>|Recurrent Neural Networks|68.20|
|Xu et al. (2019)<br><br>|3|2|Convolutional Neural Network<br><br>|74.20|
|Zhao et al. (2019)<br><br>|22|2<br><br>|Convolutional Neural Network<br><br>|69.00|
|Lee et al. (2019)<br><br>|64<br><br>|4<br><br>|Linear Discriminant Analysis|58.20|
|This study|22|4<br><br>|Ensemble Subspace Discriminant|47.36|
|This study<br><br>|22|2|Ensemble Subspace Discriminant<br><br>|61.86|

ACC is the highest accuracy achieved in the cited paper. In the list, Kato et al. (2020) used the MISCP dataset, Ma et al. (2018) used EEG Movement/Imagery Database (eegmmidb) dataset, Garcia-Laencina et al. (2014) used 5 diﬀerent BCI-EEG datasets together, Lindig-Leon and Bougrain (2015) and Lee et al. (2019) used their own datasets, Xu et al. (2019) used the BCI Competition IV Dataset-IIb dataset, and other studies used BCI Competition IV Dataset-IIa dataset.

Hjorth parameters, and adaptive auto-regressive coeﬃcients is presented using ﬁve BCI-EEG datasets. Local Fisher discriminant analysis is applied for feature selection. Five-ﬁnger movements are classiﬁed using the linear discriminant analysis algorithm with an accuracy of 77.30%. The reported accuracy value is higher than the accuracy in our study, but the channel reduction process is conducted in addition to the feature selection, and only C3 and C4 channels are evaluated for their proposed methods. In another study by Jusas and Samuvel (2019), the channel reduction and feature selection processes were conducted, and the authors performed an analysis with 8 EEG channels by applying channel selection and also used the PCA-based feature selection process. PCA-based selected fast Fourier transform and channel variance features of EEG signals are classiﬁed with an accuracy of 56.00% using the least squares support vector machine. In the study by Nguyen et al. (2018), common spatial patterns and in the study by Lindig-Leon and Bougrain (2015) common spatial patterns and band power feature extraction methods were applied to classify multiple tasks, achieving higher classiﬁcation performances than the accuracy in our study. Although more EEG channels are evaluated, only the spatial features are considered, and time domain features, time-frequency domain features, and non-linear features were not included in their feature extraction process. Although common spatial pattern-based feature selection was applied, which is known to have a positive eﬀect on MI task classiﬁcation performance success, the performance is still not at very high levels for these studies. In another study by Ma et al. (2018), the sliding window method and transposed matrix were used to represent 64-channel EEG signals. They used EEG signals from Movement/Imagery Database (eegmmidb) for the prediction of ﬁve classes, and these classes were eye closed (baseline), and tasks

imagining moving both feet, both ﬁsts, left ﬁst, and right ﬁst. The accuracy value of 68.20% is yielded with recurrent neural networks. The classiﬁcation accuracy is higher than the accuracy achieved in our multi-task classiﬁcation task. On the other hand, such deep learning approaches have more computational complexity than our study since they combine feature selection and classiﬁcation processes. In a binary task classiﬁcation study by Xu et al. (2019), the time-frequency representations of EEG signals are obtained using the short-time Fourier transform method, and 2D EEG images are given to convolutional neural network structure for classiﬁcation. The accuracy value of 74.20% is calculated by their proposed approach. Although the success of the study appears to be higher than our study, the computational complexity due to image transformation of EEG signals and convolutional neural network-based classiﬁcation should not be ignored. In addition to computational load, less number of channels (C3, Cz, and C4) are only evaluated. Considering the high performance of deep learning approaches and the eﬀectiveness of channel reduction on performance, better classiﬁcation results could be achieved. In another binary classiﬁcation study by Zhao et al. (2019), Wavelet Transform and convolutional neural network-based approach using 22 EEG channels of BCI Competition IV Dataset-IIa are introduced. The classiﬁcation result showed that the accuracy value is calculated as 69.00%. As in the previous study, there is no signiﬁcant performance improvement considering the advantages and drawbacks of convolutional neural network-based approaches, despite the occurred additional computational complexity. In the study by Lee et al. (2019), time-domain parameters are extracted from 64 EEG channels, and a private dataset is used. Four diﬀerent tasks which are Grasp, Spread, Pronation, and Supination are diﬀerentiated with an accuracy of 58.20% using the

shrinkage-regularized linear discriminant analysis algorithm. They used more EEG channels and diﬀerent multiple-task categories, but only temporal features were extracted as EEG features, and the other feature extraction categories were ignored.

Considering the contributions, beneﬁts, and drawbacks of these binary and multiple-task classiﬁcation studies, some parameters play important roles in the MI task classiﬁcation process. These are dataset, number of channels, channel selection, feature extraction methods, feature selection methods, classiﬁer algorithms, and number of classes. The main drawback is computational complexity due to feature extraction methods and the classiﬁcation process of EEG signals. In EEG signal processing, the basic goal is to achieve high-performance values using all channels of EEG signals. Another important aspect is adopting an eﬀective feature selection method that indicates the relevant and discriminative MI EEG features and improves the classiﬁers’ performance. The statistically signiﬁcant feature-based approach we used in the study, which has computational advantages, resulted in an accuracy of 61.86 and 47.36% for binary classiﬁcation and four-task classiﬁcation, respectively. In addition, 22 channels of EEG signals are evaluated for process, and diﬀerent feature categories which are time-domain, frequency-domain, time-frequency domain, and non-linear are used for feature extraction. The classiﬁcation results indicate that the statistically signiﬁcance-based feature selection process is an eﬀective feature selection method that generally improves classiﬁer performances. Therefore, the encouraging performance results of this study with the computational advantages demonstrate that the statistically signiﬁcant feature-based approach may be applied to other EEG-based studies.

##  . Conclusion

Decoding of MI tasks has an important role to provide a reliable and convenient way of information interaction for paralyzed patients to control external devices. EEG signals are commonly used in the classiﬁcation of MI tasks due to ease of recording and low cost. However, the monitoring and analysis of long-term EEG signals are time-consuming and not reliable because of changes in the experiences of experts. Hence, the selection of eﬀective signal processing and classiﬁcation approaches plays an important role in the accurate analysis of MI EEG signals.

In this study, we extracted features using time-domain, frequency-domain, time-frequency domain features, and nonlinear methods. In addition, the eﬀectiveness of the statistically signiﬁcance-based feature selection method is investigated. The statistically signiﬁcant MI EEG features are determined using statistical signiﬁcance (ANOVA test and independent t-test)-based feature selection for four tasks and binary task classiﬁcations. The results showed that the ensemble learning classiﬁers (boosted trees and subspace discriminant algorithms) yielded the maximum classiﬁer performance in four tasks and binary task classiﬁcations. Ensemble subspace discriminant algorithm yielded accuracy values of 47.36 and 61.86% using the selected feature set including statistically signiﬁcant MI EEG features for four-task and binary task classiﬁcations, respectively. The main contribution of this study is the implementation of Poincare plot measures based on non-linear features to commonly use time-domain,

frequency-domain, and time-frequency domain features. In our experiments, we observed that the ANOVA test-based and the independent t-test-based feature selection processes provide signiﬁcant improvements in classiﬁers’ performance. Hence, the statistically signiﬁcance-based selection is a practical feature selection method and may be used to analyze diﬀerent EEG signal-based studies. Additionally, this study has the advantage of low computational complexity in terms of feature extraction, feature selection, and classiﬁcation approaches. Therefore, the statistically signiﬁcant time-domain, frequency-domain, timefrequency domain features, and non-linear parameters are presented as the novel eﬀective features in this study and successfully implemented to predict binary and multiple MI tasks.

## Data availability statement

Publicly available datasets were analyzed in this study. This data can be found here: https://www.bbci.de/competition/iv/#dataset2a.

## Author contributions

YY, MP, and YI contributed to the conception and design of the study. MD implemented all feature extraction, feature selection, and machine learning algorithms in Matlab. MD and YI wrote the ﬁrst draft of the manuscript. All authors wrote sections of the manuscript and contributed to the manuscript revision, read, and approved the submitted version.

## Funding

MP was supported by the Slovenian Research Agency (Grant Nos. P1-0403 and J1-2457). This study was also supported by the Izmir Katip Celebi University Scientiﬁc Research Council Agency as project number 2023-TDR-FEBE-0002 for MD’s doctoral thesis studies. In addition, MD has a research fellowship from the Higher Education Institution within the 100/2000 Higher Education Institution Ph.D. scholarship and the 2211A general doctorate scholarship from the Scientiﬁc and Technological Research Council of Türkiye (TUBITAK).

## Conﬂict of interest

The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their aﬃliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## References

Alkan, A., Koklukaya, E., and Subasi, A. (2005). Automatic seizure detection in EEG using logistic regression and artiﬁcial neural network. J. Neurosci. Methods 148, 167–176. doi: 10.1016/j.jneumeth.2005.04.009

Altaheri, H., Muhammad, G., Alsulaiman, M., Amin S. U., Altuwaijri, G. A., Abdul, W., et al. (2021). Deep learning techniques for classiﬁcation of electroencephalogram (EEG) motor imagery (MI) signals: a review. Neural Comput. Appl. 35, 14681–14722. doi: 10.1007/s00521-021-06352-5

Ang, K. K., Chin, Z. Y., Wang, C., Guan C., and Zhang H. (2012). Filter bank common spatial pattern algorithm on BCI competition IV datasets 2a and 2b. Front. Neurosci. 6, 39. doi: 10.3389/fnins.2012.00039

Ang, K. K., Chin, Z. Y., Zhang, H., and Guan, C. (2008). “Filter bank common spatial pattern (FBCSP) in brain-computer interface,” in 2008 IEEE International Joint Conference on Neural Networks (IEEE World Congress on Computational Intelligence) (Hong Kong: IEEE), 2390–2397. doi: 10.1109/IJCNN.2008.4634130

Arvaneh, M., Guan, C., Ang, K. K., and Quek, C. (2011). Optimizing the channel selection and classiﬁcation accuracy in EEG-based BCI. IEEE Trans. Biomed. Eng. 58, 1865–1873. doi: 10.1109/TBME.2011.2131142

Bansal, D., and Mahajan, R. (2019). EEG-Based Brain-Computer Interfaces: Cognitive Analysis and Control Applications. Academic Press. doi: 10.1016/C2017-0-01267-3

Blanco-Diaz, C. F., Antelis, J. M., and Ruiz-Olaya, A. F. (2022). Comparative analysis of spectral and temporal combinations in CSP-based methods for decoding hand motor imagery tasks. J. Neurosci. Methods 371, 109495. doi: 10.1016/j.jneumeth.2022.109495

Blum, A. L., and Langley, P. (1997). Selection of relevant features and examples in machine learning. Artif. Intell. 97, 245–271. doi: 10.1016/S0004-3702(97)00063-5

Boashash, B. (2015). Time-frequency Signal Analysis and Processing: A Comprehensive Reference. Academic Press.

Brennan, M., Palaniswam, M., and Kamen, P. (2001). Do existing measures of Poincare plot geometry reﬂect nonlinear features of heart rate variability? IEEE Trans. Biomed. Eng. 48, 1342–1347. doi: 10.1109/10.959330

Brunner, C., Leeb, R., Muller-Putz, G., Schlogl, A., and Pfurtscheller, G. (2008). BCI Competition 2008–Graz Data Set A. Institute for Knowledge Discovery (Laboratory of Brain-Computer Interfaces), Graz University of Technology. 1–6. Available online at: http://www.bbci.de/competition/iv/desc_2a.pdf

Bulut, A., Ozturk, G., and Kaya, I. (2022). Classiﬁcation of sleep stages via machine learning algorithms. J. Intell. Syst. Appl. 5, 66–70. doi: 10.54856/jiswa.202205210

Cancioglu, E., Sahin, S., and Isler, Y. (2021). Fault detection and diagnosis on process control systems using ensemble learning algorithms from Poincare plot measures. Eur. J. Sci. Technol. 26, 30–34. doi: 10.31590/ejosat.952761

Chaudhary, S., Taran, S., Bajaj, V., and Siuly, S. (2020). A ﬂexible analytic wavelet transform based approach for motor-imagery tasks classiﬁcation in BCI applications. Comput. Methods Prog. Biomed. 187, 105325. doi: 10.1016/j.cmpb.2020.105325

Cura, O. K., and Akan, A. (2021). Analysis of epileptic EEG signals by using dynamic mode decomposition and spectrum. Biocybernet. Biomed. Eng. 41, 28–44. doi: 10.1016/j.bbe.2020.11.002

Degirmenci, M., Ozdemir, M. A., Izci, E., and Akan, A. (2021). Arrhythmic heartbeat classiﬁcation using 2d convolutional neural networks. Innovat. Res. Biomed. Eng. 43, 422–433. doi: 10.1016/j.irbm.2021.04.002

- Degirmenci, M., Yuce, Y. K., and Isler, Y. (2022a). Classiﬁcation of multi-class motor imaginary tasks using Poincare measurements extracted from EEG signals. J. Intell. Syst. Appl. 5, 74–78. doi: 10.54856/jiswa.202212204
- Degirmenci, M., Yuce, Y. K., and Isler, Y. (2022b). “Motor imaginary task classiﬁcation using statistically signiﬁcant time-domain EEG features,” in 2022 30th Signal Processing and Communications Applications Conference (SIU) (Safranbolu: IEEE), 1–4. doi: 10.1109/SIU55565.2022.9864745
- Degirmenci, M., Yuce, Y. K., and Isler, Y. (2022c). Motor imaginary task classiﬁcation using statistically signiﬁcant time domain and frequency domain eeg features. J. Intell. Syst. Appl. 5, 49–54. doi: 10.54856/jiswa.202205203

Djamal, E. C., Abdullah, M. Y., and Renaldi, F. (2017). Brain computer interface game controlling using fast Fourier transform and learning vector quantization. J. Telecommun. Electron. Comput. Eng. 9, 71–74.

Gandhi, T., Panigrahi, K. B., and Anand, S. (2011). A comparative study of wavelet families for EEG signal classiﬁcation. Neurocomputing 74, 3051–3057. doi: 10.1016/j.neucom.2011.04.029

Garcia-Laencina, P. J., Rodriguez-Bermudez, G., and Roca-Dorda, J. (2014). Exploring dimensionality reduction of EEG features in motor imagery task classiﬁcation. Expert Syst. Appl. 41, 5285–5295. doi: 10.1016/j.eswa.2014.02.043

Guyon, I., and Elisseeﬀ, A. (2003). An introduction to variable and feature selection. J. Mach. Learn. Res. 3, 1157–1182.

Ha, K. W., and Jeong, J. W. (2019). Motor imagery EEG classiﬁcation using capsule networks. Sensors 19, 2854. doi: 10.3390/s19132854

Hamedi, M., Salleh, S. H., Noor, A. M., and Mohammad-Rezazadeh, I. (2014). “Neural network-based three-class motor imagery classiﬁcation using time-domain features for BCI applications,” in 2014 IEEE Region 10 Symposium (Kuala Lumpur: IEEE), 204–207. doi: 10.1109/TENCONSpring.2014.6863026

Hart, P. E., Stork, D. G., and Duda, R. O. (2000). Pattern Classiﬁcation. 2nd Edn. New Jersey, NJ: A Wiley-Interscience Publication.

Isa, N. M., Amir, A., Ilyas, M. Z., and Razalli, M. S. (2019). Motor imagery classiﬁcation in Brain computer interface (BCI) based on EEG signal by using machine learning technique. Bull. Electric. Eng. Inform. 8, 269–275. doi: 10.11591/eei.v8i1.1402

Isler, Y. (2009). A detailed analysis of the eﬀects of various combinations of heart rate variability indices in congestive heart failure (Ph.D. thesis). Dokuz Eylul University, Izmir, Türkiye.

Isler, Y., and Kuntalp, M. (2007). Combining classical HRV indices with wavelet entropy measures improves to performance in diagnosing congestive heart failure. Comput. Biol. Med. 37, 1502–1510. doi: 10.1016/j.compbiomed.2007.01.012

Isler, Y., and Kuntalp, M. (2009). “Diagnosis of congestive heart failure patients using Poincare measures derived from ECG signals,” in 2009 14th National Biomedical Engineering Meeting (Izmir: IEEE), 1–4. doi: 10.1109/BIYOMUT.2009.5130287

Isler, Y., Narin, A., Ozer, M., and Perc, M. (2019). Multi-stage classiﬁcation of congestive heart failure based on short-term heart rate variability. Chaos Solitons Fractals 118, 145–151. doi: 10.1016/j.chaos.2018.11.020

Isler, Y., Ozturk, U., and Sayilgan, E. (2023). Decreasing the running time of the knearest neighbors algorithm with data reduction techniques for diagnosing congestive heart failure. Sadhana Acad. Proc. Eng. Sci. 48, 35. doi: 10.1007/s12046-023-02105-3

Jusas, V., and Samuvel, S. G. (2019). Classiﬁcation of motor imagery using combination of feature extraction and reduction methods for brain-computer interface. Inform. Technol. Control 48, 225–234. doi: 10.5755/j01.itc.48.2.23091

Kato, M., Kanoga, S., Hoshino, T., and Fukami, T. (2020). “Motor imagery classiﬁcation of ﬁnger motions using multiclass CSP,” in 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (Montreal, QC: IEEE), 2991–2994. doi: 10.1109/EMBC44109.2020.9176612

Kohavi, R., and John, G. H. (1997). Wrappers for feature subset selection. Artif. Intell. 97, 273–324. doi: 10.1016/S0004-3702(97)00043-X

Lee, S. B., Kim, H. J., Kim, H., Jeong, J. H., Lee, S. W., and Kim, D. J. (2019). Comparative analysis of features extracted from EEG spatial, spectral and temporal domains for binary and multiclass motor imagery classiﬁcation. Inform. Sci. 502, 190–200. doi: 10.1016/j.ins.2019.06.008

Lindig-Leon, C., and Bougrain, L. (2015). “A multi-label classiﬁcation method for detection of combined motor imageries,” in 2015 IEEE International Conference on Systems, Man, and Cybernetics (IEEE), 3128–3133. doi: 10.1109/SMC.2015.543

Lotte, F., Baugrain, L., Cichocki, A., Clerc, M., Congedo, M., Rakotomamonjy, A., et al. (2018). A review of classiﬁcation algorithms for EEG-based brain-computer interfaces: a 10 year update. J. Neural Eng. 15, 031005. doi: 10.1088/1741-2552/aab2f2

Luo, J., Gao, X., Zhu, X., Wang, B., Lu, N., and Wang, J. (2020). Motor imagery EEG classiﬁcation based on ensemble support vector learning. Comput. Methods Prog. Biomed. 193, 105464. doi: 10.1016/j.cmpb.2020.105464

Ma, X., Qiu, S., Du, C., Xing, J., and He, H. (2018). “Improving EEG-based motor imagery classiﬁcation via spatial and temporal recurrent neural networks,” in 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (Honolulu, HI: IEEE), 1903–1906. doi: 10.1109/EMBC.2018.8512590

Meziani, A., Djouani, K., Medkour, T., and Chibani, A. (2019). A Lasso quantile periodogram based feature extraction for EEG-based motor imagery. J. Neurosci. Methods 328, 108434. doi: 10.1016/j.jneumeth.2019.108434

Mousa, M. A., El-Khoribi, R. A., and Shoman, M. E. (2016). A novel brain computer interface based on principle component analysis. Proc. Comput. Sci. 82, 49–56. doi: 10.1016/j.procs.2016.04.008

Musallam, Y. K., AlFassam, N. I., Muhammad, G., Amin, S. U., Alsulaiman, M., Abdul, W., et al. (2021). Electroencephalography-based motor imagery classiﬁcation using temporal convolutional network fusion. Biomed. Signal Process. Control 69, 102826. doi: 10.1016/j.bspc.2021.102826

Narin, A., Isler, Y., and Ozer, M. (2014). Investigating the performance improvement of HRV Indices in CHF using feature selection methods based on backward elimination and statistical signiﬁcance. Comput. Biol. Med. 45, 72–79. doi: 10.1016/j.compbiomed.2013.11.016

Nguyen, T., Hettiarachchi, I., Khatami, A., Gordon-Brown, L., Lim, C. P., and Nahavandi, S. (2018). Classiﬁcation of multi-class BCI data by common spatial pattern and fuzzy system. IEEE Access 6, 27873–27884. doi: 10.1109/ACCESS.2018. 2841051

Pawar, D., and Dhage, S. (2020). Feature extraction methods for electroencephalography based brain-computer interface: a review. Int. J. Comput. Sci. 47, 501–515.

Sakhavi, S., Guan, C., and Yan, S. (2015, August). Parallel convolutionallinear neural network for motor imagery classiﬁcation,” in 2015 23rd European Signal Processing Conference (EUSIPCO) (Nice: IEEE), 2736–2740. doi: 10.1109/EUSIPCO.2015.7362882

Samek, W., Kawanabe, M., and Muller, K. R. (2013). Divergence-based framework for common spatial patterns algorithms. IEEE Rev. Biomed. Eng. 7, 50–72. doi: 10.1109/RBME.2013.2290621

Samek, W., Vidaurre, C., Muller, K. R., and Kawanabe, M. (2012). Stationary common spatial patterns for brain-computer interfacing. J. Neural Eng. 9, 026013. doi: 10.1088/1741-2560/9/2/026013

Sayilgan, E„ Yuce, Y. K., and Isler, Y. (2021b). Evaluation of wavelet features selected via statistical evidence from steady-state visually-evoked potentials to predict the stimulating frequency. J. Faculty Eng. Arch. Gazi Univ. 36, 593–605. doi: 10.17341/gazimmfd.664583

Sayilgan, E., Yuce, Y. K., and Isler, Y. (2021a). “Evaluating steady-state visually evoked potentials-based brain-computer interface system using wavelet features and various machine learning methods,” in Brain-Computer Interface, ed V. Asadpour (IntechOpen). doi: 10.5772/intechopen.98335

Sayilgan, E., Yuce, Y. K., and Isler, Y. (2021c). Frequency recognition from temporal and frequency depth of the brain-computer interface based on steady-state visual evoked potentials. J. Intell. Syst. Appl. 4, 68–73. doi: 10.54856/jiswa.202105160

Tan, D., and Nijholt, A. (eds.). (2010). “Brain-computer interfaces and humancomputer interaction,” in Brain-Computer Interfaces (London: Springer), 3–19. doi: 10.1007/978-1-84996-272-8_1

Tiwari, S., Goel, S., and Bhardwaj, A. (2022). MIDNN-a classiﬁcation approach for the EEG based motor imagery tasks using deep neural network. Appl. Intell. 52, 4824–4843. doi: 10.1007/s10489-021-02622-w

Tzallas, A. T., Tsipouras, M. G., and Fotiadis, D. I. (2009). Epileptic seizure detection in EEGs using time-frequency analysis. IEEE Trans. Inform. Technol. Biomed. 13, 703–710. doi: 10.1109/TITB.2009.2017939

Vapnik, V. (1999). The Nature of Statistical Learning Theory, 2nd Edn. New York, NY: Springer. doi: 10.1007/978-1-4757-3264-1

Wu, W., Chen, Z., Gao, X., Li, Y., Brown, E. N., and Gao, S. (2014). Probabilistic common spatial patterns for multichannel EEG analysis. IEEE Trans. Pattern Anal. Mach. Intell. 37, 639–653. doi: 10.1109/TPAMI.2014.2330598

Xu, G., Shen, X., Chen, S., Zong, Y., Zhang, C., Yue, H., et al. (2019). A deep transfer convolutional neural network framework for EEG signal classiﬁcation. IEEE Access 7, 112767–112776. doi: 10.1109/ACCESS.2019.2930958

Yuan, H., and He, B. (2014). Brain-computer interfaces using sensorimotor rhythms: current state and future perspectives. IEEE Trans. Biomed. Eng. 61, 1425–

1435. doi: 10.1109/TBME.2014.2312397

Zhao, D., Tang, F., Si, B., and Feng, X. (2019). Learning joint space–time– frequency features for EEG decoding on small labeled data. Neural Netw. 114, 67–77. doi: 10.1016/j.neunet.2019.02.009

