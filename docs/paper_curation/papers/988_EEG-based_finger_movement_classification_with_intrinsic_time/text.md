TYPE Original Research PUBLISHED March DOI   .    /fnhum.    .       

OPEN ACCESS

EDITED BY

Kang Hao Cheong, Singapore University of Technology and Design, Singapore

REVIEWED BY

Kun Li, Hebei University of Technology, China Lipeng Pan, Northwest A&F University, China

*CORRESPONDENCE

Yalcin Isler

islerya@yahoo.com

RECEIVED December ACCEPTED February PUBLISHED March

CITATION

Degirmenci M, Yuce YK, Perc M and Isler Y (    ) EEG-based ﬁnger movement classiﬁcation with intrinsic time-scale decomposition.

Front. Hum. Neurosci.   :       . doi:   .    /fnhum.    .       

COPYRIGHT

© Degirmenci, Yuce, Perc and Isler. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

# EEG-based ﬁnger movement classiﬁcation with intrinsic time-scale decomposition

Murside Degirmenci , Yilmaz Kemal Yuce , Matjaž Perc , , ,  and Yalcin Isler *

Department of Biomedical Technologies, Izmir Katip Celebi University, Izmir, Türkiye, Department of Computer Engineering, Alanya Alaaddin Keykubat University, Alanya, Antalya, Türkiye, Faculty of Natural Sciences and Mathematics, University of Maribor, Maribor, Slovenia, Department of Medical Research, China Medical University Hospital, China Medical University, Taichung, Taiwan, Complexity Science Hub Vienna, Vienna, Austria, Department of Physics, Kyung Hee University, Seoul, Republic of Korea, Department of Biomedical Engineering, Izmir Katip Celebi University, Izmir, Türkiye

Introduction: Brain-computer interfaces (BCIs) are systems that acquire the brain’s electrical activity and provide control of external devices. Since electroencephalography (EEG) is the simplest non-invasive method to capture the brain’s electrical activity, EEG-based BCIs are very popular designs. Aside from classifying the extremity movements, recent BCI studies have focused on the accurate coding of the ﬁnger movements on the same hand through their classiﬁcation by employing machine learning techniques. State-of-the-art studies were interested in coding ﬁve ﬁnger movements by neglecting the brain’s idle case (i.e., the state that brain is not performing any mental tasks). This may easily cause more false positives and degrade the classiﬁcation performances dramatically, thus, the performance of BCIs. This study aims to propose a more realistic system to decode the movements of ﬁve ﬁngers and the no mental task (NoMT) case from EEG signals.

Methods: In this study, a novel praxis for feature extraction is utilized. Using Proper Rotational Components (PRCs) computed through Intrinsic Time Scale Decomposition (ITD), which has been successfully applied in di erent biomedical signals recently, features for classiﬁcation are extracted. Subsequently, these features were applied to the inputs of well-known classiﬁers and their di erent implementations to discriminate between these six classes. The highest classiﬁer performances obtained in both subject-independent and subject-dependent cases were reported. In addition, the ANOVA-based feature selection was examined to determine whether statistically signiﬁcant features have an impact on the classiﬁer performances or not.

Results: As a result, the Ensemble Learning classiﬁer achieved the highest accuracy of   . % among the tested classiﬁers, and ANOVA-based feature selection increases the performance of classiﬁers on ﬁve-ﬁnger movement determination in EEG-based BCI systems.

Discussion: When compared with similar studies, proposed praxis achieved a modest yet signiﬁcant improvement in classiﬁcation performance although the number of classes was incremented by one (i.e., NoMT).

KEYWORDS

brain-computer interfaces (BCIs), electroencephalogram (EEG), feature reduction, machine learning, ﬁnger movements (FM) classiﬁcation, intrinsic time-scale decomposition (ITD)

## Introduction

Neuroimaging covers various direct and indirect techniques used to visualize both the structure and the function of the nervous system. These methods include MR (Magnetic Resonance Imaging), CT (Computed Tomography), PET (Positron Emission Tomography), and EEG (electroencephalography). Among them, aside from being non-invasive, EEG retains some advantages over others such as high temporal resolution, easy accessibility, and low cost. Since EEG can capture brain activity in real-time in millisecond precision, it has become popular in neuroscience research, clinical diagnostics, and BCI (Brain-Computer Interface) systems. BCIs translate neural signals into commands for controlling external devices through software applications. In recent developments, researchers have delved into analyzing EEG patterns linked to particular ﬁnger movements. BCIs engineered to decipher these patterns oﬀer the prospect of individuals operating external devices or interfaces solely through brain activity, eliminating the necessity for physical muscle movements. This advancement holds immense promise in crafting prosthetic hands capable of individual ﬁnger control, managing numerous devices, facilitating neurorehabilitation, and extending into applications within gaming and entertainment industries (Aricò et al., 2018). In the following subsections, after a literature review on both brain-computer interfaces and state-of-the-art ﬁnger movement classiﬁcation studies, we mentioned our aim, our contributions to the literature, and the structural organization of this article, respectively.

 .  Brain-computer interfaces

BCIs are computer-assisted systems that record the brain’s electrical signals based on diﬀerent brain monitoring techniques, analyze the signals on the interface, and convert them to speciﬁc commands to control external devices such as computers, wheelchairs, and prostheses without any physical movement (Belkacem et al., 2020). Consequently, BCI technology can help people suﬀering from various motor disabilities such as stroke patients to communicate with the outside, and indirectly perform motor function (Wolpaw et al., 2002). Among several diﬀerent neuroimaging modalities, Electroencephalography (EEG) is widely used to capture brain activities. It is preferred for designing BCI systems due to the fact that EEG has many advantages such as its high temporal resolution, non-invasiveness, easy operation, relatively low cost, and portability (Vidal, 1977; Chen et al., 2015).

EEG-based BCI systems that manipulated motor imagery signals generated through the movements of large body parts such as hands, feet, and tongue have been proposed to control assistive devices throughout the past several decades (Pfurtscheller and Neuper, 2001; Alazrai et al., 2019; Degirmenci et al., 2023). However, such systems propose only limited control dimensions for prosthetic devices, thereby, the potential of utilizing these systems to control further complex assistive devices is restricted (Sciaraﬀa et al., 2022). In the last decade, numerous research studies have examined the decoding of movements of ﬁne body parts to improve such systems (Alazrai et al., 2019).

The decoding of the movements performed by various ﬁngers of a hand may increase the control dimensions of the EEGbased BCI systems. This, in turn, might provide subjects who utilize assistive devices to better carry out numerous skillful tasks. However, the decoding of ﬁnger movements (FM) within the same hand is considered as a demanding research area among motor imagery signal analysis studies (Alazrai et al., 2019). Employing and analyzing diﬀerent kinds of feature extraction methods, feature selection methods, and classiﬁcation algorithms play an important role in order to improve the eﬃciency of EEG-based BCI systems, which analyze FM and generate relevant commands from the recorded EEG data. In the literature, various feature extraction methods, feature reduction methods, and classiﬁcation algorithms have been suggested for decoding FM. Diﬀerent time-domain, frequency-domain, and spatial-domain EEG features have been calculated to predict FM in the past decade. The raw EEG time series (Kaya et al., 2018; Mwata-Velu et al., 2022; Zahra et al., 2022), diﬀerent amplitude-based, and statistical-based EEG signal features (Degirmenci et al., 2024) were utilized to examine the eﬀectiveness of the time domain. As for the spectral-domain features, diﬀerent frequency-domain [Fourier transform (Kaya et al., 2018)] and time-frequency domain [Wavelet transform (Yahya et al., 2019), Short-time Fourier transform (Azizah et al., 2022), Empirical mode decomposition (Mwata-Velu et al., 2021)] representation algorithms and their various versions were investigated to classify FM. Common spatial pattern (Anam et al., 2019, 2020) and its diﬀerent versions (Kato et al., 2020) are one of the most experimented methods for the analysis of spatial domain in FM classiﬁcation. These diﬀerent extracted features have been successfully classiﬁed using various machine learning algorithms. However, it is a challenging scientiﬁc task to determine and choose the most eﬃcient combination of these methods. Providing optimal and relevant features is important for improving classiﬁer performance (Narin et al., 2014; Degirmenci et al., 2023). Therefore, the implementation of eﬀective feature extraction methods and feature reduction methods is essential for facilitating the following task of machine learning algorithms.

 .  State of the art for ﬁnger movement classiﬁcation

In the last decade, various signal processing and classiﬁcation methods have been successful in FM classiﬁcation (up to 91.70%) applied in the classiﬁcation of EEG signals for FM tasks.

Kaya et al. (2018) conducted a Support Vector Machine (SVM) based classiﬁcation study to classify the ﬁve FM of a hand. In their study, they used the data set they collected from a total of eight subjects who agreed to participate. They exploited the power of EEG subbands, Fourier Transform (FT) amplitudes, and EEG time series to represent 19-channel EEG signals as features. An average accuracy of 43.00% was obtained. Moreover, a subject-dependent classiﬁcation study was also carried out and the performances of eight subjects were found to vary in the range of (20.00, 60.00%).

In Anam et al. (2019), the classiﬁcation of ﬁve FM for the subject-dependent condition using the EEG signals of four subjects was aimed. To this purpose, the Common Spatial Pattern

(CSP) based feature extraction process was performed and the Random Forest (RF) algorithm was executed. The classiﬁcation performance was found to be 100% for training accuracy for each subject and the test accuracy performances ranged between 51.00 and 56.00%.

In 2022, Azizah et al. (2022) carried out a subject-dependent FM classiﬁcation study. They performed channel selection based on One vs. Rest Common Spatial Pattern (CSP-OVR) and four out of 19 EEG channels were deﬁned as relevant channels in their study. They extracted the spectrogram features from these selected channels. Their subject-dependent experimental results showed that the accuracy in classiﬁcations employing SVM ranged from 21.20 to 66.60%.

In the study conducted by Kato et al. (2020) in 2020, a multi-class CSP and Complex Fourier amplitudes-based feature extraction process was presented. They extracted features using 19 EEG channels for FM classiﬁcation. According to their subjectdependent results, the training results of classiﬁcations carried out with the SVM algorithm were reported in the range of 23.90– 58.30%.

Recently, deep learning approaches from machine learning methods have been the focus of attention by researchers in many diﬀerent research areas such as disease detection from medical images (Narin and Isler, 2021), emotion recognition from biological signals (Ozdemir et al., 2021) and Electrocardiography (ECG) based arrhythmia detection (Degirmenci et al., 2022a) due to the fact that these architectures provide improved performance of classiﬁcation. In addition, the main reason for this is that feature extraction and classiﬁcation stages can be performed together in the hidden layers of deep learning structures. Considering these structures’ beneﬁts and advantages, deep learning approaches are also included for the classiﬁcation of FM and motor imagery tasks in the literature.

In 2021, Mwata-Velu et al. (2021) performed a feature extraction process based on Empirical. Mode Decomposition (EMD) using four eﬀective EEG channels which were selected from 19 EEG channels. They performed deep learning (BiLSTM) based subject-dependent classiﬁcations for the prediction of FM. Using EMD-based feature extraction and deep learning structure, training accuracy values in eight subjects were calculated in the range of

- 73.47- -98.69%, and test performances were calculated in the range of 66.00–76.13%.

In another study conducted in 2022, Mwata-Velu et al. (2022) worked on the classiﬁcation of EEG time series with deep learning (EEGNet) structure. EEG signals of four subjects were used from a dataset that included EEG data of eight subjects, and at the same time, four out of 19 EEG channels were selected for their suggested study. In the subject-dependent analyses performed with four subjects, training successes were reported in the range of 80.10–91.70%.

In Anam et al. (2020), an FM classiﬁcation study, a model that uses CSP algorithm-based feature extraction and Autonomous Deep Learning (ADL) based classiﬁcation was proposed. They used 19-channel EEG signals from four subjects for their experimental process. With respect to the subjectdependent classiﬁcations, training performances ranged from

- 74.73 to 77.61%, and test performances ranged from 74.61 to 77.75%.

In another related paper Zahra et al. (2022), which was published recently in 2022, the performance of a Convolutional Neural Networks (CNN) was evaluated based on an original study design. In their model, EEG time series were combined with sliding window (Dietterich, 2002) and noise enhancement (Mitaim and Kosko, 1998) methods to extract the features. They obtained the features from 19-channel EEG signals of eight subjects. They conducted a subject-independent FM classiﬁcation and achieved a training accuracy of 57.50%.

In their study conducted in 2022, Limbaga et al. (2022) carried out a CNN (EEGNet) based study for feature extraction and signal classiﬁcation of ﬁve motor imagery classes of a hand. They reinforced their suggested model using a transfer learning approach through an EEG data set that includes 19-channel EEG signals of eight subjects. They reduced the EEG channel number to 14 and utilized the EEG signals of only four subjects. In addition to this data set, they recorded EEG signals from a subject while the subject imagined ﬁve diﬀerent hand positions. According to their subject-independent evaluations, they achieved an accuracy of 51.74% success with the transfer learning model which is a reinforced model.

When the studies mentioned above that aimed to classify the motor imagery tasks of FM of a hand are examined, it was observed that the performances remained at relatively low rates in studies using all EEG channels and in subject-independent classiﬁcation studies. The studies showed that the performances got higher with channel selection-based and subject-dependent classiﬁcations. The cause for the low level of performance in the classiﬁcation of FM may be that the movements of the ﬁngers on a hand are actually controlled from the same region of the motor cortex (Kaya et al., 2018). Kaya et al. (2018) investigated the event-related potential (ERP) curves of motor imagery tasks of other body limb movements together with motor imagery tasks of FM. They reported that the curves could not be clearly diﬀerentiated in the motor imagery tasks of FM. Therefore, there is a need to increase the classiﬁcation performance by using eﬀective feature extraction methods, feature selection methods, and classiﬁcation algorithms for the classiﬁcation of FM tasks.

 .  The aim of the study

In 2007, an iterative signal decomposition technique, which is known as intrinsic time-scale decomposition, (ITD) was introduced to analyze nonlinear or non-stationary signals (Frei and Osorio, 2007). Recent studies have performed ITD-based approaches for the analysis of biomedical signals. ITD-based feature extraction processes were conducted in various EEG-based studies for diﬀerent objectives such as epilepsy detection (Martis et al., 2013; Degirmenci and Akan, 2020), and attention deﬁcit hyperactivity disorder (ADHD) recognition (Karabiber Cura et al., 2023). Considering its ability to discriminate diﬀerent classes, we studied to explore whether ITD promises superior use, or not, in classifying other biomedical signals.

In this study, therefore, we suggest new praxis for the classiﬁcation of FM tasks using ITD of EEG signals. The diﬀerent

modes that are deﬁned as Proper Rotation Components (PRCs) and their combinations are acquired through ITD. Various features are evaluated using only modes and their combinations. In addition to the ITD-based feature extraction process, the eﬀectiveness of statistically signiﬁcance-based feature selection (ANOVA) is also investigated. The extracted ITD-based features are classiﬁed by eight diﬀerent machine learning algorithms (Decision Tree, Discriminant Analysis, Naive Bayes, K-Nearest Neighbors, Support Vector Machine, Ensemble Learning, Neural Networks, and Kernel Approximation). Diﬀerent performance evaluation metrics are employed for the accurate evaluation of the outputs of the suggested study.

 .  Contributions

The novel contributions of this research study are summarized as follows:

- • The classiﬁcation of EEG signals of FM tasks is presented, using the ITD signal decomposition, and various feature extraction methods.
- • Modes extracted by the ITD are utilized to evaluate several features, including Power, Mean, Sample Entropy, HighFrequency Moments (First Moment, Second Moment, Third Moment, Fourth Moment), and Hjorth Parameters (Activity, Mobility, Complexity).
- • The ﬁrst 3 modes ({PRC1},{PRC2}, and {PRC3}), and diﬀerent combinations of them ({PRC1,PRC2},{PRC1,PRC3},{PRC2,PRC3}, and {PRC1,PRC2,PRC3}) are used for feature extraction and the eﬀectiveness of only modes and their combinations are investigated with diﬀerent machine learning algorithms, separately.
- • The investigation of an appropriate and sustainable machine learning model for the proposed features to diﬀerentiate the FM tasks, and improve classiﬁcation performance (success rate) as compared with the existing methods.

Finally, it must also be noted that this is the ﬁrst study with a model that brings diﬀerent combinations of PRCs extracted by ITD and various other features to classify FM tasks, to the best of our knowledge.

 .  Paper organization

The rest of the paper is organized as follows: The EEG dataset used in this study, and EEG signal analysis methods are performed by the proposed ITD method which are ITD-based feature acquisition, statistical signiﬁcance-based feature selection, classiﬁer algorithms, and performance evaluation metrics are presented in Section 2. Experimental results are given in Section 3 and the results of the proposed approaches are discussed in Section 4. The outcomes of the study are summarized in Section 5.

## Materials and methods

This study design mainly consists of ﬁve stages that are described in Isler (2009). These are EEG Data Acquisition, ITDbased Feature Extraction, Feature Reduction, Classiﬁcation, and Performance Evaluation. The processes performed in each stage were delineated with details in the sub-headings. Out of these ﬁve stages/steps, the ﬁrst four stages constitute the proposed classiﬁcation model. Figure 1 shows the block diagram for the proposed model with its stages/steps.

 .  EEG dataset description

In this study, the EEG dataset, which is a large electroencephalographic motor imagery dataset for EEG-based BCIs, presented by Kaya et al. (2018) is beneﬁted. The dataset consists of motor imagery EEG signals that were recorded from 13 healthy subjects through 19 channels. 19 EEG electrodes together with two reference electrodes and the ground electrode were placed according to the international 10/20 EEG electrode placement system. The researchers reported that they recorded the EEG signals using an EEG-1200 JE-912A system. They performed an individual motor imagery experiment based on the movements of 10 diﬀerent body limbs for four diﬀerent BCI interaction paradigms. Among these planned paradigms, Paradigm #1-(CLA), which means classical left/right-hand motor imagery includes three imageries, and these are left and right-hand movements, and one passive mental imagery in which subjects remained neutral in no motor imagery. Paradigm #2-(HaLT), which means hand/leg/tongue motor imagery contains six tasks, and it is an extended version of the 3-state CLA paradigm with motor imagery tasks of right and left foot movement and tongue movement. Paradigm #3 (5F), which means 5-ﬁnger motor imagery includes FM imageries of the ﬁve-ﬁnger movement of a hand. During the tasks given for diﬀerent ﬁngers, subjects implemented the corresponding imageries invoking as ﬂexion of the relevant ﬁnger up or down. Finger movement imageries were coded as follows: Thumb (Class 1), Index ﬁnger (Class 2), Middle ﬁnger (Class 3), Ring ﬁnger (Class 4), and Pinkie ﬁnger (Class 5). Paradigm #4 (NoMT), which means no imagery, visual stimuli only is the case in which no visual stimulus is presented to the subjects and they passively watch the computer screen. In this study, we aimed to carry out a 6-class classiﬁcation using the 5F and NoMT paradigms. Whilst recording of EEG signals, the action signal remained on the screen for 1 s to implement the corresponding motor imageries. At the end of the given time, the task was not shown on the screen. Instead, the relevant task was interrupted for 1.5–2.5 s until the next task. In this dataset, two diﬀerent sampling frequencies, 200 and 1,000 Hz, were set for experiments. EEG signals recorded with a 1000 Hz sampling frequency were extracted to be used in this study. In recording of EEG signals acquired at 1,000 Hz, a 0.53–100 Hz band-pass ﬁlter was applied to signals using hardware ﬁlters. In addition, a 50 Hz notch ﬁlter was applied to reduce the electrical grid interface. Before performing the feature extraction and the following steps, to have a balanced distribution among the classes and provide adjusted chance level (Galiotta et al., 2022),

|[Figure 1]<br><br>FIGURE<br><br>The block diagram of the study.|
|---|

100 samples of 1,000 Hz EEG signals for the 5F (ﬁve classes) and NoMT (one class) paradigms were studied for each class as the preprocessing stage. Hence, a total of 600 trials were performed

for one subject. After obtaining the 5F and NoMT EEG signals for each subject, each EEG segment is decomposed to the ﬁnite number of PRCs by applying ITD.

 .  Intrinsic time-scale decomposition (ITD)

ITD is introduced by Frei and Osorio for time-frequencyenergy (TFE) analysis of signals with precision (Frei and Osorio, 2007). The ITD decomposes a signal into (i) a sum of PRCs, and (ii) a monotonic trend without the need for laborious and ineﬀective sifting or splines. It is an iterative decomposition algorithm for the analysis of nonlinear and non-stationary signals, decomposing the original signal into low-frequency, which is known as baseline signal (Lt), and high-frequency, which are known as proper rotation (Ht) components. ITD preserves precise temporal information (Frei and Osorio, 2007; Voznesensky and Kaplun, 2019; Degirmenci and Akan, 2020).

For the application of ITD, suppose there is an EEG signal Xt to be processed. To extract the low-frequency component (“baseline signal”) from the EEG signal, an operator L is introduced and the remainder is the high-frequency component (“proper rotation”). Hence, the EEG signal Xt is deﬁned as in Equation 1.

Xt = LXt + (1 − L)Xt = Lt + Ht (1)

where the baseline signal is indicated as Lt = LXt, and the proper rotation component is indicated as Ht = (1 − L)Xt. The extraction of baseline and proper rotation components are explained in detail with the following three steps (Frei and Osorio, 2007; Martis et al., 2013; Voznesensky and Kaplun, 2019):

Xt = LDt +

D

Htj, j = 0,··· ,D (5)

j=0

where D denotes the number of PRCs that are provided during ITD processing.

An exemplary motor imagery EEG signal decomposition process conducted through the ITD algorithm is given in Figure 2A. To decide which of the separate PRCs to work with, the PRCs were examined in the frequency domain and their energy spectrums were computed. In Figure 2B, a case of energy spectrums of PRCs, decomposed into an EEG signal is provided. Figure 2B shows that the ﬁrst PRC (i.e., PRC1) has the highest frequency content, while the ﬁfth PRC (i.e., PRC5) exhibits the lowest frequency content. Hence, we selected the ﬁrst three PRCs and their diﬀerent combinations for our suggested feature extraction process due to the fact that they include high-frequency contents that best represent the signal characteristic of the original EEG. Various feature extraction methods are implemented to the determined high-frequency PRCs (Ht), which are decomposed through ITD. In our study design, seven diﬀerent sets of high-frequency PRCs which are only PRC1, PRC2, and PRC3, and their diﬀerent combinations [PRC1–PRC2, PRC1–PRC3, PRC2–PRC3, and PRC1–PRC2–PRC3 (denoted as PRC1-to-3)] are acquired and utilized to evaluate 10 features.

 .  ITD features

- • A real-valued signal is assumed as Xt,t ≥ 0 and τk,k = 1,2,··· denotes the its local extremes. Let the value of the signal at τk is denoted as X(τk) and the value of its baseline at τk is denoted as L(τk).
- • We assume that Lt, and Ht have been deﬁned over the interval [0,τk], and Xt is available for [0,τk+2]. The baseline extraction operator, L is provided as a piece-wise linear function on the

interval (τk,τk + 1] between the two extrema as deﬁned in Equations 2, 3.

Lt = Lk + (

- Lk+1 − Lk

- Lk+2 − Lk

)(Xt − Xk), tǫ(τk,τk + 1] (2)

where

Lk+1 = α[Xk +(

- τk+1 − τk

- τk+2 − τk

)(Xk+2 −Xk)]+(1−α)Xk+1, (3)

and 0 < α < 1, is typically set with α = 12. The baseline signal, Lt is constructed in this way to obtain the monotonicity of Xt between extrema. Hence, the baseline signal is reconstructed as a linearly transformed contraction of the original signal in conformity with Equations 2, 3.

- • Once the baseline signal is deﬁned, the residual or highfrequency component, PRC is computed as deﬁned in Equation 4.

HXt = (1 − L)Xt = Ht = Xt − Lt (4)

Using the baseline Lt, and the high frequency Ht modes, the original signal Xt can be reconstructed using Equation 5.

Following the extraction of low-frequency baseline signal and high-frequency PRCs by running the ITD algorithm, EEG signal properties including the power, mean value, sample entropy, highfrequency moments (ﬁrst moment, second moment, third moment, and fourth moment), and Hjorth parameters (activity, mobility, and complexity) were computed from various combinations of PRCs. Their details are described below:

- • The mean value was calculated based on time-domain information for 3 PRCs. It is deﬁned as in Equation 6.

µ =

1 N

N−1

n=0

X[n] (6)

where PRCs are denoted as X[k], the mean value is denoted as µ and the size of PRCs is described as N.

- • The total power of PRCs was obtained using the spectrum of signals. The spectrum of PRCs was evaluated by implementing the periodogram method, which allows for analysis of the frequency content of a signal (Iscan et al., 2011; Karabiber Cura et al., 2023). From deﬁnitions of k-th frequency (Equation 7) and power power spectral desity estimation of the k-th frequency component (Equation 8), the total power is deﬁned as in Equation 9 (Iscan et al., 2011):

wk =

2π N

k,k = 0,1,··· ,N − 1 (7)

S(wk) =

1 N

|X(wk)|2 (8)

|[Figure 2]<br><br>FIGURE<br><br>(A) PRCs extracted by the intrinsic time-scale decomposition (ITD) from a  -s segment of EEG signals, (B) Energies of each PRCs (the ﬁrst ﬁve modes are given as examples).|
|---|

ST =

N−1

S(wk) (9)

k=0

where S(wk) indicates the power spectral density of the signal provided by the periodogram method, X(wk) indicates the discrete Fourier transform of the PRC x[n], and ST is the total power of PRCs. N shown in Equations 8, 9, refers to the size of the corresponding signal.

- • The higher order spectral moments (1st, 2nd, 3rd, and 4th) were computed using the spectrum of signals like total power. These moments are deﬁned as in Equations 10–13, respectively (Degirmenci et al., 2018):

M1 =

N−1

k=0

(wk)1S(wk) (10)

M2 =

N−1

k=0

(wk)2S(wk) (11)

M3 =

N−1

k=0

(wk)3S(wk) (12)

M4 =

N−1

k=0

(wk)4S(wk) (13)

Here, M1, M2, M3, and M4 represent the 1st, 2nd, 3rd, and 4th higher order spectral moments of the corresponding PRCs, respectively.

- • Hjorth parameters were introduced by Hjorth (1970) in 1970, and these are time-domain statistical features used in signal processing. These parameters include the Activity parameter (Ax), Mobility parameter (Mx), and Complexity parameter (Cx) of the signal. In the following mathematical equations for Activity, Mobility, and Complexity parameters, y(n) indicates the auto-correlation function of one PRC after the ITD application. y[n] = [y1,y2,··· ,yN], and N indicates the length of the signal.

Activity parameter, deﬁnes the power of vibration signal and can be evaluated using the variance of signal amplitude. It is formulated in Equation 14 (Hjorth, 1970; Yu and Fang, 2022):

Ax = (y(n)) = σy2 (14)

where σy denotes the standard deviation of y(n) and it can be described with the Equation 15.

σy =

N

1 N − 1

[y(n) − µ]2 (15)

n=1

Here, the mean value of the signal is represented with µ. Mobility parameter describes the ratio of standard

deviations of ﬁrst-order derivatives, and it can be evaluated using the slope of the signal. It is deﬁned as in Equation 16.

Mx =

σy2′ σy2

σy′ σy

=

(16)

where σy′ indicates the ﬁrst-order standard deviation of signals.

Complexity parameter denotes the similarity of signal to sinusoidal signal and it is expressed as the ratio between the mobility of the ﬁrst derivative of the EEG signal and the mobility of the EEG signal itself (Hjorth, 1970; Yu and Fang, 2022). The mathematical expression of complexity parameters is given in Equation 17.

Mx(y′(t)) Mx(y(t))

Cx =

=

Mx(dydt(t)) Mx(y(t))

=

σy2′′ σy2′ σy2′ σy2

(17)

Here, the second-order standard deviation of signal y(t) is expressed as σy′′.

• The sample entropy indicates a time series complexity measure that represents the probability of a system generating

new patterns. It can be deﬁned as the embedding theory that utilizes the time series directly instead of probability values. The original time series is deﬁned as Lt(i),i = 1,2,··· ,N. The new vector sequences which each of size m, u(1) by u(N−m+1) are created, and expressed as u(i) = {Lt(i),Lt(i+ 1),··· ,Lt(i + m − 1)} (Higuchi, 1988; Martis et al., 2013). The deﬁned length m indicates the embedding dimension. The distance d[u(i),u(j)] between vectors u(i), and u(j) is described in Equation 18 (Higuchi, 1988):

d(u(i),u(j)) = max{|u(i+k)−u(j+k)|},0 ≤ k ≤ m−1 (18)

Here, k is an index. The probability of providing another vector within a distance r from vector u(i) is deﬁned as in Equation 19 (Higuchi, 1988):

1 N − m + 1

Ci′m(r) =

(19)

The number of j, j  = i, j ≤ N − m + 1 such that d(u(i), u(j)) ≤ r

The entropy can be deﬁned in Equation 20.

N−m+1

Ci′m(r) (20)

∅m(r) = (N − m + 1)−1

i=1

Then, the sample entropy is described in Equation 21 (Martis et al., 2013):

∅′m(r) ∅′m+1(r)

SampEn(m,r,N) = −ln[

] (21)

 .  Feature reduction using statistical signiﬁcance (ANOVA)

Applying too many features to classiﬁers could unnecessarily complicate the implementation of classiﬁers. The application of redundant information in EEG signals can cause confusion, which is deﬁned as the curse of dimensionality (Hart et al., 2000). Trying diﬀerent combinations one by one and ﬁnding the most suitable classiﬁcation causes computational load (Narin et al., 2014). Feature reduction algorithms can be used instead of feature selection based on trying diﬀerent combinations. The purpose of feature reduction is to investigate small-size subsets of features that can provide the same or better optimal classiﬁcation performances (Yesilkaya et al., 2023). Using fewer data presenting some relevant features of motor imagery EEG signals is important to obtain optimal classiﬁer performance without computational load.

In this study, a feature reduction method based on statistical signiﬁcance was applied to determine relevant ITD features that provide the best discrimination of the FM imageries for each sample. The statistical signiﬁcance-based feature selection method used in this study was also performed in other BCI studies (Bulut et al., 2022; Degirmenci et al., 2022c, 2023). One-way variance analysis (ANOVA test), which is mainly used to indicate whether there is a diﬀerence between the means in conditions where there are two or more groups was used in this study. We preferred the ANOVA test from statistical signiﬁcance-based feature selection methods since

TABLE List of adopted classiﬁers with their implemented algorithms.

|Classiﬁer|Algorithms<br><br>|
|---|---|
|Decision Tree<br><br>|Fine, medium, and coarse|
|Discriminant Analysis|Linear, and quadratic|
|Naive Bayes<br><br>|Gaussian, kernel|
|Support Vector Machine (SVM)<br><br>|Linear, quadratic, cubic, ﬁne Gaussian, medium Gaussian, coarse Gaussian|
|k-Nearest Neighbor (kNN)<br><br>|Cubic, cosine|
|Ensemble Learning<br><br>|Boosted, Bagged, Subspace Discriminant, Subspace k-NN, RUSBoosted Trees|
|Neural Networks|Narrow, medium, wide, bi-layered, tri-layered<br><br>|
|Kernel Approximation|Support vector machine, logistic regression|

a total of six motor imagery tasks including ﬁve FM imageries and NoMT cases tried to be classiﬁed. Thus, the eﬀect of the ANOVA test-based feature selection method was investigated with ITD features. The statistical signiﬁcance of all extracted EEG features was determined by calculating p-values. The statistical signiﬁcance level (α) is deﬁned as 0.05 and the features that ensure the statistical evidence range were indicated and selected as statistically signiﬁcant features. In addition to the classiﬁcations performed without the feature selection process in our study, the feature vector including selected statistically signiﬁcant ITD features were also given to the classiﬁcation algorithms as input data to diﬀerentiate FM imageries. The eﬀectiveness of the ANOVAbased feature selection process is investigated by comparing the results of classiﬁcations with all features and selecting statistically signiﬁcant features.

 .  Classiﬁcation

In this study for diﬀerentiation of FM imageries, the provided ITD-based EEG features have been evaluated using eight wellknown machine learning algorithms, such as Decision Tree (Tzallas et al., 2009; Sharma et al., 2022), Discriminant Analysis (Hart et al., 2000; Chakrabarti et al., 2003; Lotte et al., 2018), Naive Bayes (Hart et al., 2000; Miao et al., 2017), Support Vector Machine (Vapnik, 1999; Hart et al., 2000; Bascil et al., 2016), k-Nearest Neighbor (Hart et al., 2000; Isler, 2009; Tzallas et al., 2009), Ensemble Learning (Sayilgan et al., 2019, 2020, 2021a,b, 2022; Degirmenci et al., 2022b,c; Karabiber Cura et al., 2023), Neural Networks (Richard and Lippmann, 1991; Pan et al., 2012; Narin and Isler, 2021; Ozdemir et al., 2021; Degirmenci et al., 2022a), and Kernel Approximation (Maji et al., 2008; Lei et al., 2019). The classiﬁers and corresponding algorithms that were adopted in this study are listed below in Table 1. Each of these algorithms was implemented via utilizing the Classiﬁcation Learner Toolbox, which is part of the Statistics and Machine Learning Toolbox available in the Matlab software package (Matlab, 2023). Since the technical details of these classiﬁers have become so trivial that inherited details are not explained. For further details regarding the classiﬁers, studies that are cited in the table can be accessed.

 .  Performance evaluation

Training is deﬁned as updating the classiﬁer-speciﬁc parameters according to the available data. Testing is determining the performance of classiﬁers by the correct decisions made on the unseen data before. For this reason, the feature set was divided into two groups as train data (80%) and test data (20%) using the random splitting method (Hart et al., 2000).

In addition, during training, classiﬁers are expected to generalize rather than over-ﬁt (or memorize) the available data. However, it may be diﬃcult to make generalizations, especially when the size of the data is not large enough. Cross-validation (CV) is a method employed to evaluate the predictive performance of a model on data it has not processed (classiﬁed) before. Several crossvalidation methods, including hold-out, leave-one-out, k-fold, and Monte-Carlo (MC) exist. All in all, hold-out (k equals 2) and leaveone-out (k equals the number of samples) methods are special cases of the k-fold method (Hart et al., 2000; Isler et al., 2015; Patro, 2021).

Diﬀerences between k-fold and MC methods are emphasized in the recent literature: (a) the k-fold uses each data in the validation although MC uses samples arbitrary times (0 or more), (b) the k-fold divides the data into k parts, although MC separates large number data parts, (c) the k-fold results in unbiased accuracy with a high variance where the MC results in highly biased accuracy with low variance. These diﬀerences cause a trade-oﬀ among CV methods (Patro, 2021). A recent study emphasizes that a large number of simulated data may cause over-ﬁtting and using independent data for extra validation is necessary (Labriﬀe et al., 2022).

Therefore, we preferred the k-fold CV method as in our similar studies (Isler, 2009; Isler and Kuntalp, 2009; Degirmenci et al., 2022a,b) and the recent literature (Anam et al., 2019, 2020; Kato et al., 2020; Mwata-Velu et al., 2021, 2022; Azizah et al., 2022; Zahra et al., 2022). Using k-fold cross-validation (CV), the training data set was divided into k equal-sized subsets. One subset was used as test data, other subsets (k − 1) were determined as training data, and this classiﬁcation process was repeated k times (Hart et al., 2000). Regarding Brownlee’s article on the Machine Learning Mastery website (Brownlee, 2023), there is no general rule for choosing the k value, but as the k value decreases, the bias value also decreases (Kuhn and Johnson, 2013). Additionally, it is stated that empirically selected values of 5 or 10 give a balanced bias-variance test error (James et al., 2013). The average classiﬁcation performance of these iterations is deﬁned as the training performance (Hart et al., 2000). In conclusion, k was set as 5 for this study as in similar studies.

The accuracy (ACC) performance criterion is used in this study to evaluate the performance of various machine learning algorithms. The mathematical expression of the accuracy performance criterion is given in Equation 22 (Hart et al., 2000).

TP + TN TP + FN + TN + FP

ACC =

(22)

Here, TP and TN indicate the number of correctly assigned samples into the true class. In addition, FP and FN indicate the number of incorrectly assigned samples into positive class and negative class, respectively.

## Results

The suggested methods were applied to EEG segments of 19channel EEG signals collected from 8 subjects. Firstly, the ITD approach was used to decompose EEG signals into PRCs. Then the power, mean value, sample entropy, high-frequency moments (ﬁrst moment, second moment, third moment, and fourth moment), and Hjorth parameters (activity, mobility, and complexity) were evaluated as features utilizing distinct combinations of PRCs. In the feature extraction process performed in this study, both the ﬁrst three components (PRC1, PRC2, and PRC3) and their diﬀerent combinations (PRCs1-2, PRCs1-3, PRCs2-3 and PRC1-to-3) were used and their eﬀectiveness was investigated, individually. The same feature extraction process was also performed on EEG signals without any ITD approach to show the eﬀectiveness of the ITD algorithm in FM classiﬁcation. Additionally, the ANOVA-based feature selection process was carried out on the PRC1-to-3 feature set and its eﬀectiveness was investigated. Finally, a variety of classiﬁers including Decision Tree, Discriminant Analysis, Naive Bayes, Support Vector Machine, k-Nearest Neighbor, Ensemble Learning, Neural Networks, and Kernel Approximation were used to classify FM imagery of EEG segments, and the experimental results of each were analyzed.

The classiﬁcation performances of the ITD-based features computed using the diﬀerent components and EEG-based features were evaluated to compare and analyze the eﬀectiveness of the suggested ITD-based process. The classiﬁcation performances of features acquired through our suggested ITD-based approaches with various classiﬁers are given in Tables 2–9. These classiﬁcation performances were evaluated using both feature sets provided using single PRCs (PRC1, PRC2, and PRC3), their combinations (PRCs1-2, PRCs1-3, and PRC1-to-3), and ANOVA-selected PRC1to-3 combination. In tables, EEG indicates that the feature set utilized in the classiﬁcation step is generated using the EEG signal itself without applying ITD. Additionally, boldface characters show which feature set obtained the highest accuracy performance in subject-dependent and subject-independent analyses separately.

Decision Tree classiﬁcation performances evaluated using ITDbased features are presented in Table 2. With respect to these results, the ﬁrst three PRCs combined with an ANOVA-based feature selection process obtain the highest accuracy value of 44.17% in S4 (Subject E). The performance comparison of the ITD-based approach with the EEG-based case (without the ITD process), shows that the highest performance values were obtained with the use of ITD-based features in all subjects except S2 (Subject B). The results for S2 (Subject B) were further investigated and it was noticed that the highest accuracy value reported was 30.83% in classiﬁcations performed using both PRCs1-3 combination and EEG features with an ANOVA-based feature selection process.

Linear Discriminant Analysis classiﬁcation performances were evaluated using ITD-based features presented in Table 3. When the results are compared, the ﬁrst three PRCs combined with the ANOVA-based feature selection process obtain the highest accuracy value of 47.50% in S4 (Subject E). The comparison of classiﬁer performances with the features extracted through the ITD-based approach and the performances of the same classiﬁers with the features of the EEG-based case (without the ITD process)

TABLE All components’ performances were tested in this study using the Decision Tree classiﬁer.

|Components<br><br>|S |S |S <br><br>|S |S <br><br>|S |S <br><br>|S |SI|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|29.17|27.50|35.00<br><br>|32.50|29.17<br><br>|25.83|31.67<br><br>|27.50<br><br>|25.83|
|PRC2<br><br>|26.67|28.33|26.67<br><br>|30.00|26.67<br><br>|30.83|30.00|32.50<br><br>|20.63|
|PRC3<br><br>|24.17<br><br>|28.33<br><br>|26.67<br><br>|34.17|29.17<br><br>|20.83|28.33<br><br>|27.50|21.77|
|PRCs1-2|26.67<br><br>|26.67<br><br>|26.67|37.50<br><br>|27.50|29.17<br><br>|32.50|30.00|23.13<br><br>|
|PRCs1-3|26.67|30.83<br><br>|30.00<br><br>|34.17<br><br>|27.50|29.17|29.17<br><br>|30.00|24.79<br><br>|
|PRCs2-3|35.83<br><br>|26.67<br><br>|26.67|35.83<br><br>|25.00|25.83<br><br>|23.33|24.17<br><br>|22.71|
|PRCs1-to-3<br><br>|27.50<br><br>|30.00<br><br>|28.33|36.67<br><br>|26.67|27.50<br><br>|36.67<br><br>|22.50|23.54|
|ANOVA+PRCs1-to-3|30.83|30.00<br><br>|35.83<br><br>|44.17<br><br>|26.67|27.50|34.17<br><br>|27.50|24.06|
|EEG<br><br>|30.00|26.67<br><br>|32.50|35.83<br><br>|25.00|30.00<br><br>|25.83<br><br>|27.50|25.31|
|ANOVA+EEG|23.33|30.83|35.00|38.33<br><br>|21.67|30.00<br><br>|25.00|30.83|23.33|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

TABLE All components’ performances were tested in this study using the Linear Discriminant Analysis classiﬁer.

|Components<br><br>|S <br><br>|S <br><br>|S |S |S <br><br>|S <br><br>|S <br><br>|S <br><br>|SI|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|25.83|28.33|33.33|27.50<br><br>|24.17<br><br>|30.83|27.50<br><br>|26.67|26.25|
|PRC2<br><br>|24.17|28.33<br><br>|30.00<br><br>|40.00|24.17<br><br>|30.83|27.50<br><br>|27.50|24.79|
|PRC3<br><br>|27.50<br><br>|25.00|32.50<br><br>|27.50|31.67<br><br>|31.67|21.67<br><br>|25.83<br><br>|29.17|
|PRCs1-2|31.67|25.83|35.00<br><br>|34.17|27.50<br><br>|26.67|21.67|22.50<br><br>|29.38|
|PRCs1-3<br><br>|31.67<br><br>|26.67|38.33<br><br>|43.33|35.83<br><br>|30.83|25.00|29.17|29.90<br><br>|
|PRCs2-3<br><br>|32.50<br><br>|25.83|28.33|27.50|25.83<br><br>|25.83<br><br>|32.50|25.83<br><br>|28.85|
|PRCs1-to-3<br><br>|31.67|25.00<br><br>|26.67|33.33<br><br>|29.17|25.00<br><br>|20.83<br><br>|25.00<br><br>|30.83|
|ANOVA+PRCs1-to-3|38.33<br><br>|40.00|37.50|47.50|35.83<br><br>|28.33<br><br>|28.33|30.00<br><br>|33.54|
|EEG<br><br>|N/A<br><br>|N/A|N/A|N/A|N/A<br><br>|N/A<br><br>|N/A|N/A<br><br>|N/A|
|ANOVA+EEG|N/A|N/A<br><br>|N/A|N/A<br><br>|N/A|N/A<br><br>|N/A|N/A<br><br>|N/A|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

could not be conducted clearly since the results of the EEG-based case could not be computed. The EEG-based feature set could not be classiﬁed because they do not ﬁt the Linear Discriminant Analysis classiﬁer’s parameters.

Naive Bayes classiﬁcation performances evaluated using ITDbased features are presented in Table 4. According to these results, EEG features with an ANOVA-based feature selection process obtain the highest accuracy value of 40.00% in S4 (Subject E). The performances of the ITD-based approach were compared with the performances of the EEG-based case (without the ITD process), and the comparison reﬂects that the highest performance values were obtained with the use of ITD-based features in all subjects except three subjects. The analyses performed for S3 (Subject C) were further investigated, it was found that the highest accuracy value was 34.17% in classiﬁcations performed using both the ﬁrst three PRCs combination with ANOVA-based feature selection and EEG features with ANOVA-based feature selection process.

Support Vector Machine classiﬁcation performances evaluated using ITD-based features are presented in Table 5. The results expose that the ﬁrst three PRCs combined with an ANOVA-based feature selection process and without an ANOVA-based feature selection process obtain the highest accuracy value of 49.17% in

S4 (Subject E). On the other hand, the same highest accuracy value is also found for the ﬁrst three PRCs in combination with the ANOVA-based feature selection process in S3 (Subject C). The performances of the ITD-based approach were compared with the performances of the EEG-based case (without the ITD process) and the comparison shows that the highest performance values were obtained with the use of ITD-based features in all subjects.

k-Nearest Neighbors classiﬁcation performances acquired using ITD-based features are presented in Table 6. According to these results, the PRCs1-3 combination obtains the highest accuracy value of 46.67% in S3 (Subject C). The performances of the ITD-based approach were compared with the performances of the EEG-based case (without the ITD process) and the highest performance values were obtained with the use of ITD-based features in all subjects.

Ensemble Learning classiﬁcation performances evaluated using ITD-based features are presented in Table 7. With regard to these results, the ﬁrst three PRCs combined with an ANOVA-based feature selection process obtained the highest accuracy value of 55.00% for S4 (Subject E). When the performances of the ITDbased approach were compared with the performances of the EEGbased case (without the ITD process), it was evident that the highest

TABLE All components’ performances were tested in this study using the Naive Bayes classiﬁer.

|Components<br><br>|S |S |S <br><br>|S |S <br><br>|S |S <br><br>|S |SI|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|22.50|30.83|32.50<br><br>|35.00|25.00<br><br>|27.50|30.00<br><br>|31.67<br><br>|20.94|
|PRC2<br><br>|27.50|25.00|29.17<br><br>|34.17|24.17<br><br>|24.17|24.17|25.83<br><br>|19.38|
|PRC3<br><br>|26.67<br><br>|22.50<br><br>|25.00<br><br>|32.50|30.83<br><br>|25.00|23.33<br><br>|32.50|20.31|
|PRCs1-2|24.17<br><br>|26.67<br><br>|29.17|30.83<br><br>|27.50|22.50<br><br>|30.83|25.00|22.19<br><br>|
|PRCs1-3|26.67|26.67<br><br>|33.33<br><br>|37.50<br><br>|38.33|30.00|29.17<br><br>|23.33|20.94<br><br>|
|PRCs2-3|29.17<br><br>|25.00<br><br>|30.83|30.00<br><br>|31.67|25.00<br><br>|21.67|27.50<br><br>|21.15|
|PRCs1-to-3<br><br>|23.33<br><br>|30.00<br><br>|30.83|35.83<br><br>|23.33|27.50<br><br>|23.33<br><br>|27.50|23.96|
|ANOVA+PRCs1-to-3|30.83|35.00<br><br>|34.17<br><br>|39.17<br><br>|31.67|35.83|30.83<br><br>|30.83|22.81|
|EEG<br><br>|31.67|30.83<br><br>|28.33|40.83<br><br>|26.67|22.50<br><br>|20.83<br><br>|21.67|25.42|
|ANOVA+EEG|32.50|25.83|34.17|40.00<br><br>|27.50|29.17<br><br>|19.17|21.67|23.23|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

TABLE All components’ performances were tested in this study using the Support Vector Machine classiﬁer.

|Components<br><br>|S <br><br>|S <br><br>|S |S |S <br><br>|S <br><br>|S <br><br>|S <br><br>|SI|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|29.17|35.83|40.83|40.00<br><br>|30.00<br><br>|38.33|40.00<br><br>|32.50|30.00|
|PRC2<br><br>|22.50|25.83<br><br>|34.17<br><br>|35.00|30.00<br><br>|35.83|31.67<br><br>|24.17|25.73|
|PRC3<br><br>|31.67<br><br>|29.17|30.00<br><br>|40.00|33.33<br><br>|29.17|28.33<br><br>|26.67<br><br>|27.08|
|PRCs1-2|31.67|31.67|44.17<br><br>|40.00|24.17<br><br>|33.33|39.17|27.50<br><br>|30.52|
|PRCs1-3<br><br>|35.83<br><br>|38.33|41.67<br><br>|47.50|38.33<br><br>|35.00|31.67|29.17|32.19<br><br>|
|PRCs2-3<br><br>|29.17<br><br>|32.50|39.17|37.50|38.33<br><br>|30.83<br><br>|35.00|32.50<br><br>|28.13|
|PRCs1-to-3<br><br>|27.50|37.50<br><br>|45.00|49.17<br><br>|33.33|38.33<br><br>|35.00<br><br>|35.83<br><br>|30.63|
|ANOVA+PRCs1-to-3|40.00<br><br>|45.00|49.17|49.17|35.83<br><br>|36.67<br><br>|39.17|36.67<br><br>|34.48|
|EEG<br><br>|30.00<br><br>|41.67|38.33|45.00|32.50<br><br>|33.33<br><br>|29.17|29.17<br><br>|31.46|
|ANOVA+EEG|27.50|41.67<br><br>|43.33|47.50<br><br>|34.17|33.33<br><br>|30.00|29.17<br><br>|33.65|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

performance values were obtained with the use of ITD-based features in all subjects.

Neural Networks classiﬁcation performances evaluated using ITD-based features are presented in Table 8. The results indicate that the ﬁrst three PRCs combined with an ANOVA-based feature selection process achieved the highest accuracy value of 53.00% for S3 (Subject C). Comparison of the performances of the ITD-based approach with the performances of the EEG-based case (without the ITD process) shows that the highest performance values were realized with the use of ITD-based features in all subjects except S6 (Subject G) and S8 (Subject I). Further analyses performed for S6 (Subject G) showed that the highest accuracy value attained was 38.33% in classiﬁcations performed using both the ﬁrst three PRCs’ combination with ANOVA-based feature selection process and EEG features with ANOVA-based feature selection process. On the other hand, the analyses performed for S8 (Subject I) revealed that the highest accuracy value reached was 35.00% using EEG features with an ANOVA-based feature selection process.

Kernel Approximation classiﬁcation performances evaluated using ITD-based features are presented in Table 9. In reference to the results, one can infer that the ﬁrst three PRCs combination without an ANOVA-based feature selection process obtained

the highest accuracy value of 40.83% in S4 (Subject E). The performances of the ITD-based approach and the performances of the EEG-based case (without the ITD process) were compared and it was apparent that the highest performance values were obtained with the use of ITD-based features in only S4 (Subject E) and S7 (Subject H). In S1 (Subject A), S3 (Subject C), S6 (Subject G), and S8 (Subject I), the highest performance values were obtained with the use of EEG-based features with or without an ANOVA-based feature selection process. In other subjects, the highest performance values were obtained with the use of both ITD-based features and EEG-based features.

## Discussion

The observed results reveal that the ITD algorithm mostly yields a considerable improvement in classiﬁcation performance when the classiﬁcation performance of ITD-based approaches are compared with the classiﬁcation performance of EEG-based analysis conducted without utilizing the ITD algorithm. The highest accuracy values are obtained using the ITD algorithm for most of all classiﬁcation algorithms except the Naive Bayes

TABLE All components’ performances were tested in this study using the k-Nearest Neighbors classiﬁer.

|Components<br><br>|S |S |S <br><br>|S |S <br><br>|S |S <br><br>|S |SI|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|24.17|38.33|35.00<br><br>|35.83|29.17<br><br>|34.17|32.50<br><br>|37.50<br><br>|29.90|
|PRC2<br><br>|23.33|25.00|26.67<br><br>|33.33|31.67<br><br>|30.00|28.33|23.33<br><br>|23.02|
|PRC3<br><br>|33.33<br><br>|25.00<br><br>|34.17<br><br>|38.33|28.33<br><br>|30.00|25.83<br><br>|30.00|26.88|
|PRCs1-2|32.50<br><br>|30.83<br><br>|34.17|36.67<br><br>|26.67|32.50<br><br>|30.83|30.83|28.54<br><br>|
|PRCs1-3|31.67|29.17<br><br>|39.17<br><br>|46.67<br><br>|32.50|34.17|29.17<br><br>|30.83|29.48<br><br>|
|PRCs2-3|32.50<br><br>|26.67<br><br>|32.50|35.83<br><br>|32.50|35.00<br><br>|28.33|26.67<br><br>|26.25|
|PRCs1-to-3<br><br>|28.33<br><br>|30.83<br><br>|35.00|44.17<br><br>|25.83|31.67<br><br>|30.83<br><br>|32.50|26.88|
|ANOVA+PRCs1-to-3|35.83|39.17<br><br>|43.33<br><br>|45.83<br><br>|35.00|34.17|36.67<br><br>|35.83|30.00|
|EEG<br><br>|30.00|33.33<br><br>|33.33|43.33<br><br>|26.67|29.17<br><br>|31.67<br><br>|30.00|27.81|
|ANOVA+EEG|30.00|33.33|40.83|40.00<br><br>|31.67|31.67<br><br>|29.17|32.50|28.64|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

TABLE All components’ performances were tested in this study using the Ensemble Learning classiﬁer.

|Components<br><br>|S <br><br>|S <br><br>|S |S |S <br><br>|S <br><br>|S <br><br>|S <br><br>|SI|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|29.17|32.50|41.67|35.83<br><br>|29.17<br><br>|35.00|37.50<br><br>|34.17|29.69|
|PRC2<br><br>|30.83|30.00<br><br>|36.67<br><br>|38.33|28.33<br><br>|31.67|29.17<br><br>|30.00|25.10|
|PRC3<br><br>|29.17<br><br>|32.50|34.17<br><br>|41.67|27.50<br><br>|32.50|27.50<br><br>|29.17<br><br>|26.46|
|PRCs1-2|32.50|34.17|40.00<br><br>|41.67|33.33<br><br>|29.17|33.33|32.50<br><br>|28.85|
|PRCs1-3<br><br>|35.83<br><br>|36.67|40.00<br><br>|43.33|34.17<br><br>|34.17|38.33|35.83|31.56<br><br>|
|PRCs2-3<br><br>|36.67<br><br>|29.17|37.50|45.00|31.67<br><br>|30.00<br><br>|28.33|30.83<br><br>|29.06|
|PRCs1-to-3<br><br>|34.17|35.00<br><br>|40.83|47.50<br><br>|32.50|30.83<br><br>|36.67<br><br>|31.67<br><br>|32.08|
|ANOVA+PRCs1-to-3|35.83<br><br>|40.83|50.83|55.00|37.50<br><br>|36.70<br><br>|41.67|39.17<br><br>|32.60|
|EEG<br><br>|30.83<br><br>|40.00|43.33|39.17|35.83<br><br>|36.67<br><br>|26.67|31.67<br><br>|29.06|
|ANOVA+EEG|29.17|38.33<br><br>|45.83|39.17<br><br>|35.00|35.00<br><br>|27.50|35.00<br><br>|27.60|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

algorithm. Among all ITD-based feature sets, all PRCs and their combinations provide a higher classiﬁcation performance compared to the EEG case in most of the classiﬁcations except the Naive Bayes and Kernel Approximation classiﬁcations. The classiﬁcation performance of a single PRC is lower compared to their combinations. The most successful component is the ﬁrst three PRC combinations (PRC1-to-3). In addition to using PRCs1-to-3, the classiﬁcation performance is further improved with the implementation of an ANOVA-based feature selection process. The experimental results revealed that the evaluation of diﬀerent components together provides the highest performance and improves the classiﬁcation performance.

Next, the component-based and EEG-based classiﬁcation accuracies in the Ensemble Learning classiﬁer for subjectdependent and subject-independent cases have been investigated to reveal the eﬃcacy of the proposed ITD-based method more accurately. The performances that are obtained using both feature sets generated utilizing EEGs, single PRCs (PRC1, PRC2, and PRC3), and their combinations (PRCs1-2, PRCs1-3, and PRC1to-3) by running Ensemble Learning are given in Figure 3. The results reveal that the ITD algorithm provides a signiﬁcant improvement in terms of accuracy performance compared to the

classiﬁcation performed without using the algorithm. Additionally, the combinations of diﬀerent components achieved the highest classiﬁcation performance for subject-dependent and subjectindependent cases. Moreover, ANOVA-selected the ﬁrst three PRC combinations (PRC1-to-3) realized the highest classiﬁcation performance in analyses for all subjects except S1 (Subject A).

The classiﬁcation performance of ITD-based features from diﬀerent PRCs with ANOVA-based feature selection and without feature selection process were compared on the basis of providing more accurate information about the performance of the suggested ANOVA-selected ITD features. The classiﬁcation accuracies for the PRC1-to-3 combination and ANOVA-selected PRC1-to-3 combination achieved by the Ensemble Learning classiﬁer are presented in Figure 4. It can be noticed that the ANOVAselected PRC1-to-3 combination succeeded in higher classiﬁcation accuracies than the PRC1-to-3 combination for both subjectdependent and subject-independent cases. The observed results reveal that the suggested statistical signiﬁcance-based feature reduction process obtains considerably noticeable diﬀerences and improves the classiﬁers’ performance.

The results of our study are compared to the state-of-the-art studies, which conducted FM classiﬁcation based on EEG signals.

TABLE All components’ performances were tested in this study using the Neural Networks classiﬁer.

|Components<br><br>|S |S |S <br><br>|S |S <br><br>|S |S <br><br>|S |SI|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|33.33|29.17|30.83<br><br>|39.17|23.33<br><br>|33.33|31.67<br><br>|29.17<br><br>|26.25|
|PRC2<br><br>|25.00|25.00|31.67<br><br>|31.67|25.83<br><br>|25.83|25.83|30.00<br><br>|24.48|
|PRC3<br><br>|32.50<br><br>|20.83<br><br>|35.83<br><br>|35.00|30.00<br><br>|25.83|32.50<br><br>|28.33|25.94|
|PRCs1-2|27.50<br><br>|30.00<br><br>|43.33|42.50<br><br>|33.33|30.83<br><br>|27.50|26.67|28.75<br><br>|
|PRCs1-3|34.17|32.50<br><br>|40.83<br><br>|42.50<br><br>|35.00|30.00|31.67<br><br>|31.67|30.94<br><br>|
|PRCs2-3|29.17<br><br>|29.17<br><br>|37.50|35.00<br><br>|34.17|35.83<br><br>|31.67|30.83<br><br>|28.96|
|PRCs1-to-3<br><br>|30.00<br><br>|33.33<br><br>|45.83|48.33<br><br>|37.50|32.50<br><br>|30.00<br><br>|34.17|29.27|
|ANOVA+PRCs1-to-3|34.17|42.50<br><br>|53.33<br><br>|45.83<br><br>|37.50|38.33|35.00<br><br>|31.67|31.88|
|EEG<br><br>|28.33|35.83<br><br>|42.50|39.17<br><br>|35.00|29.17<br><br>|26.67<br><br>|32.50|28.96|
|ANOVA+EEG|25.83<br><br>|35.00|41.67<br><br>|42.50<br><br>|36.67|38.33|23.33|35.00|30.42|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

TABLE All components’ performances were tested in this study using the Kernel Approximation classiﬁer.

|Components<br><br>|S <br><br>|S |S <br><br>|S |S <br><br>|S |S |S |SI<br><br>|
|---|---|---|---|---|---|---|---|---|---|
|PRC1<br><br>|20.00<br><br>|25.00|25.83<br><br>|24.17|26.67<br><br>|25.83|30.83|20.83<br><br>|23.23|
|PRC2<br><br>|26.67<br><br>|25.00<br><br>|23.33|30.00<br><br>|23.33|17.50<br><br>|23.33|24.17<br><br>|19.27|
|PRC3<br><br>|27.50<br><br>|20.00|27.50<br><br>|35.83|21.67<br><br>|22.50|21.67|22.50<br><br>|21.88|
|PRCs1-2|22.50<br><br>|21.67|20.83|22.50<br><br>|19.17|19.17<br><br>|26.67<br><br>|25.00|19.58|
|PRCs1-3|25.83<br><br>|24.17<br><br>|27.50<br><br>|39.17|27.50<br><br>|22.50|29.17<br><br>|20.00<br><br>|24.48|
|PRCs2-3<br><br>|25.00<br><br>|20.83|27.50|33.33<br><br>|20.00|23.33|21.67<br><br>|19.17|24.27|
|PRCs1-to-3|24.17|24.17<br><br>|27.50|40.83|15.00<br><br>|25.83|25.00<br><br>|25.83<br><br>|23.23|
|ANOVA+PRCs1-to-3|21.67|18.33<br><br>|26.67|31.67<br><br>|19.17|22.50<br><br>|22.50|25.83<br><br>|21.88|
|EEG<br><br>|25.83|25.00|38.33<br><br>|32.50|25.00<br><br>|30.00|27.50|29.17<br><br>|24.17|
|ANOVA+EEG<br><br>|29.17<br><br>|22.50|34.17|36.67<br><br>|27.50|26.67|20.00<br><br>|26.67<br><br>|25.31|

The maximum component accuracies are shown in boldface for each subject where SI means (subject-independent).

|[Figure 3]<br><br>FIGURE<br><br>The component-based classiﬁcation accuracies in Ensemble Learning classiﬁer for all subjects.|
|---|

|[Figure 4]<br><br>FIGURE<br><br>Comparison of accuracy values evaluated using PRCs -to-  features and ANOVA-selected PRCs -to-  features as regards Ensemble Learning classiﬁer.|
|---|

Table 10 presents a comparison of the suggested study to relevant prior studies. Clearly, both subject-dependent (Kaya et al., 2018; Anam et al., 2019, 2020; Kato et al., 2020; Mwata-Velu et al., 2021, 2022; Azizah et al., 2022) and subject-independent (Kaya et al., 2018; Zahra et al., 2022) studies were conducted for FM classiﬁcation in literature. In general, the highest performance values were achieved in subject-dependent classiﬁcation as in our study. An important distinction between studies regarding FM classiﬁcation was the number of subjects. In some studies (Anam et al., 2019, 2020; Mwata-Velu et al., 2022), classiﬁcation was computed over the EEG data of four subjects. In contrast, some studies computed and reported using data from eight subjects. As an example of four-subject studies, Anam et al. (2019) reports on the analysis of the data of only four subjects and the classiﬁcation performance varied between 51.00 and 56.00%. To make a meaningful comparison between the results of Anam et al. (2019) and our study, the sample sizes must be equal. Hence, we think that the two results are incomparable. In Anam et al. (2020), in addition to working with only four subjects, classiﬁcation was carried out with deep learning structures. Despite the fact that the hidden layers in deep learning structures create a signiﬁcant amount of workload and necessitate a signiﬁcant amount of time for training, the reported classiﬁcation performance in all subjects was not as high as expected (over 90.00%). In another study (Zahra et al., 2022), another deep learning-based classiﬁcation with very high training time was adopted and considering the same drawbacks of the previous study (Anam et al., 2020), although a signiﬁcant improvement in performance was achieved since the sample size of this study (i.e., only four subjects) and number of EEG channels (i.e., only four channels) were limited when compared with the sample size and number of EEG channels in our study. Thus, a comparison between the results of this study (Anam et al., 2020) and ours would not be meaningful. On the other hand, some of these prior studies (Mwata-Velu et al., 2021, 2022; Azizah et al., 2022) performed channel reduction. In these studies, four out

of all 19 channels were deﬁned as eﬀective channels and used for the feature extraction stage. Among these studies, although deep learning-based classiﬁcation was performed in addition to channel reduction in the Mwata-Velu et al. (2021), the performance values were only as high as 76%. In one of the studies of the same set (Mwata-Velu et al., 2022), EEG signals of 4 subjects were included, and deep learning-based classiﬁcation was performed together with the channel reduction process. When their classiﬁcation results are examined and compared, it is clear that high performances were obtained with regard to already noted certain limitations in the study design. However, our study uses passive condition (NoMT case) EEG signals in addition to EEG signals of FM. Prior studies had focused only on FM and classiﬁed them without considering the passive state of the subjects. The 6-class FM classiﬁcation study we propose appears to be more suitable for the real BCI design and applications. In this study, we used ITD-based features for FM classiﬁcation. According to our experimental results, 55.00% is the highest accuracy achieved using the pair of the ANOVA-selected ﬁrst three PRC combinations and the Ensemble Learning classiﬁer.

There are a few aspects that distinguish this study from previous studies in this ﬁeld. These distinctional aspects to it, together with the contributions of this study to the literature can be explained as follows:

• ITD-based feature extraction study is conducted for FM classiﬁcation. The ﬁrst three higher frequency components and their diﬀerent combinations were evaluated and their success rates were investigated with respect to diﬀerent classiﬁers separately. In addition to the ITD-based features, EEG-based features have been evaluated without ITD decomposition to analyze the impact of the suggested ITD-based process. The observed results reveal that the highest performance values are mostly achieved in ITD-based approaches. Among ITD approaches, the most successful feature set is the ﬁrst three PRC combinations (PRCs1-to-3).

TABLE Comparison of classiﬁer performances with the state-of-the-art studies for both subject-independent and subject-dependent cases from the literature.

|Study|N<br><br>|n<br><br>|Classiﬁer|c|CV|Accuracy (%)|
|---|---|---|---|---|---|---|
|Subject-independent task<br><br>| | | | | | |
|Kaya et al. (2018)|8<br><br>|19<br><br>|SVM|5|Random split (63-27-10%)<br><br>|43.00|
|Zahra et al. (2022)<br><br>|8|19|CNN<br><br>|5|10-fold<br><br>|57.50|
|This study<br><br>|8<br><br>|19|SVM<br><br>|6|5-fold<br><br>|34.48|
|Subject-dependent task<br><br>| | | | | | |
|Kaya et al. (2018)|8|19<br><br>|SVM|5<br><br>|Random split (63-27-10%)<br><br>|20.00–60.00|
|Anam et al. (2019)<br><br>|4|19<br><br>|RF|5<br><br>|5-fold<br><br>|51.00–56.00|
|Anam et al. (2020)|4|19<br><br>|ADL<br><br>|5<br><br>|5-fold|74.61–77.75|
|Kato et al. (2020)|8<br><br>|19|SVM<br><br>|5|10-fold|23.90–58.30|
|Mwata-Velu et al. (2021)<br><br>|8|4<br><br>|BLS|5<br><br>|200-fold<br><br>|66.00–76.13|
|Azizah et al. (2022)<br><br>|8|4<br><br>|SVM<br><br>|5|10-fold|21.20–66.60<br><br>|
|Mwata-Velu et al. (2022)<br><br>|4<br><br>|4|EEGNet<br><br>|5|200-fold<br><br>|80.10–91.70|
|This study<br><br>|8<br><br>|19|EL|6<br><br>|5-fold<br><br>|35.83–55.00|

N stands for the “number of subjects,” n stands for the “number of EEG channels,” c stands for the “number of classes,” and CV stands for the “Cross-Validation Method.” Classiﬁers are CNN, convolutional neural network; RF, random forest; ADL, autonomous deep learning; SVM, support vector machine; EEGNet, EEGNet deep learning model; BLS, bi-layered long-short classiﬁer; EL, ensemble learning.

- • Additionally, the statistical signiﬁcance-based feature selection process was applied to the ﬁrst three PRC combinations. It has been observed that the performance of the classiﬁer increases further in classiﬁcations performed using the ﬁrst three PRC combinations. Thereby, in this study, the highest accuracy value was obtained by applying the combination of the ﬁrst three modes to the Ensemble Learning classiﬁer with ANOVA-based feature selection.
- • To the best of our knowledge, our study presents the ﬁrst approach where diﬀerent combinations of PRCs were decomposed through ITD, and various features are utilized together to classify FM of EEG signals,
- • We used both EEG signals of all subjects (eight subjects) and all channels (19 channels) of their EEG data in analyses, hence, excluding study design limitations (e.g., number of channels) to perform eﬀective comparisons,
- • Furthermore, this study is advantageous in all its stages (ITD-based feature extraction, and classiﬁcation) in terms of workload and does not contain any complexity in the classiﬁcation stage as in deep learning structures.
- • Finally, we carried out a 6-class classiﬁcation of FM by including the NoMT condition in FM in order to realize a more realistic BCI design and application for paralyzed patients. Such a design choice is crucial since it does not exclude occurrences of the Midas Touch Problem (Velichkovsky et al., 1997), which is actually the misinterpreted intention of interactive action ﬁred by the interface. In the case of BCI development, when NoMT is

discarded, it might easily cause Midas Touch occurrences to become the source of false positives and cause classiﬁcation performance to degrade dramatically.

## Conclusion

The accurate decoding of FM is accepted as a challenging task because the ﬁngers are smaller than other limbs such as arms and hands and have a noisy signal nature. As a result, it is a more complicated task to discriminate among FM. In this study, an ITD-based machine learning approach is proposed for rapid and accurate classiﬁcation of FM by using multi-channel EEG signals. Nineteen channel EEG data collected from eight subjects are used in our analysis. Firstly, the diﬀerent modes are extracted from EEG signals using the ITD. The diﬀerent features such as power, mean, sample entropy, high-frequency moments (ﬁrst moment, second moment, third moment, fourth moment), and Hjorth parameters (activity, mobility, complexity) are evaluated using the ﬁrst three modes of EEG signals. The single version of these modes and their diﬀerent combinations are investigated in our suggested study, separately. Finally, FM classiﬁcation through these extracted feature sets is performed using eight diﬀerent machine-learning algorithms. Basically, we compared the performances of EEG-based features and the features extracted using the ITD algorithm. The experimental results reveal that the highest performance values are mostly (six out of eight classiﬁer algorithms) acquired in ITD-based approaches. Additionally, the combinations of diﬀerent modes mostly obtain the highest performance. Among all the

diﬀerent combinations, the ﬁrst three combinations form the most successful feature set, and the highest accuracy values are achieved using this combination. On the other hand, the eﬀectiveness of the ANOVA-based feature selection method is also investigated in this study. The results demonstrate that ANOVA-based feature selection improves the classiﬁer performance by making it possible to ﬁnd out the more discriminatory and relevant features. Among the classiﬁer algorithms, the Ensemble Learning classiﬁer appears to be the most successful classiﬁer algorithm tested in this study. Therefore, in this study, the highest accuracy value of 55.00% is obtained in S4 (Subject E) by applying the combination of the ﬁrst three modes to the Ensemble Learning classiﬁer with ANOVA-based feature selection. The accuracy rates of subjectdependent analyses performed according to the Ensemble Learning classiﬁer are found between 35.83 and 55.00% using the ﬁrst three modes’ combination (PRCs1-to-3) with ANOVA-based feature selection.

## Data availability statement

Publicly available datasets were analyzed in this study. This data can be found here: https://www.nature.com/articles/sdata2018211.

## Ethics statement

Ethical approval was not required for the study involving humans in accordance with the local legislation and institutional requirements. Written informed consent to participate in this study was not required from the participants or the participants’ legal guardians/next of kin in accordance with the national legislation and the institutional requirements.

## Author contributions

MD: Formal analysis, Investigation, Methodology, Validation, Writing—original draft. YY: Formal analysis, Investigation,

Supervision, Writing—original draft, Writing—review & editing. MP: Writing—original draft, Writing—review & editing, Funding acquisition. YI: Conceptualization, Methodology, Supervision, Writing—original draft, Writing—review & editing.

## Funding

The author(s) declare that ﬁnancial support was received for the research, authorship, and/or publication of this article. MP was supported by the Slovenian Research and Innovation Agency (Javna agencija za znanstvenoraziskovalno in inovacijsko dejavnost Republike Slovenije) (Grant No. P1-0403). This study was also supported by Izmir Katip Celebi University Scientiﬁc Research Council Agency as project number 2023-TDR-FEBE-0002 for MD’s doctoral thesis studies. In addition, MD has a research fellowship from the Higher Education Institution 100/2000 Ph.D. scholarship and the 2211A general doctorate scholarship from the Scientiﬁc and Technological Research Council of Turkey (TUBITAK).

## Conﬂict of interest

The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

The author(s) declared that they were an editorial board member of Frontiers, at the time of submission. This had no impact on the peer review process and the ﬁnal decision.

## Publisher’s note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their aﬃliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## References

Alazrai, R., Alwanni, H., and Daoud, M. I. (2019). EEG-based BCI system for decoding ﬁnger movements within the same hand. Neurosci. Lett. 698, 113–120. doi: 10.1016/j.neulet.2018.12.045

Anam, K., Bukhori, S., Hanggara, F. S., and Pratama, M. (2020). “Subjectindependent classiﬁcation on brain-computer interface using autonomous deep learning for ﬁnger movement recognition,” in 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (Montreal, QC), 447–450.

Anam, K., Nuh, M., and Al-Jumaily, A. (2019). “Comparison of EEG pattern recognition of motor imagery for ﬁnger movement classiﬁcation,” in 6th International Conference on Electrical Engineering, Computer Science and Informatics (EECSI) (Bandung), 24–27.

Aricò, P., Borghini, G., Di Flumeri, G., Sciaraﬀa, N., and Babiloni, F. (2018). Passive BCI beyond the lab: current trends and future directions. Physiol. Meas. 39:08TR02. doi: 10.1088/1361-6579/aad57e

Azizah, R. N., Zakaria, H., and Hermanto, B. R. (2022). Channels selection for pattern recognition of ﬁve ﬁngers motor imagery electroencephalography signals. J. Phys. 2312:012019. doi: 10.1088/1742-6596/2312/1/012019

Bascil, M. S., Tesneli, A. Y., and Temurtas, F. (2016). Spectral feature extraction of EEG signals and pattern recognition during mental tasks of 2-D cursor movements for BCI using SVM and ANN. Aust. Phys. Eng. Sci. Med. 39, 665–676. doi: 10.1007/s13246-016-0462-x

Belkacem, A. N., Jamil, N., Palmer, J. A., Ouhbi, S., and Chen, C. (2020). Brain computer interfaces for improving the quality of life of older adults and elderly patients. Front. Neurosci. 14:692. doi: 10.3389/fnins.2020. 00692

Brownlee, J. (2023). A Gentle Introduction to k-Fold Cross-Validation. Machine Learning Mastery. Available online at: https://machinelearningmastery.com/k-foldcross-validation/ (accessed February 07, 2024).

Bulut, A., Ozturk, G., and Kaya, I. (2022). Classiﬁcation of sleep stages via machine learning algorithms. J. Intell. Syst. Appl. 5, 66–70. doi: 10.54856/jiswa.2022 05210

Chakrabarti, S., Roy, S., and Soundalgekar, M. V. (2003). Fast and accurate text classiﬁcation via multiple linear discriminant projections. VLDB J. 12, 170–185. doi: 10.1007/s00778-003-0098-9

Chen, X., Wang, Y., Nakanishi, M., Gao, X., Jung, T., and Gao, S. (2015). High-speed spelling with a noninvasive brain-computer interface. Proc. Nat. Acad. Sci. U. S. A. 112, E6058–E6067. doi: 10.1073/pnas.1508080112

Degirmenci, M., and Akan, A. (2020). “EEG based epileptic seizures detection using intrinsic time-scale decomposition,” in 2020 Medical Technologies Congress (TIPTEKNO) (Antalya), 1–4.

Degirmenci, M., Ozdemir, M. A., Izci, E., and Akan, A. (2022a). Arrhythmic heartbeat classiﬁcation using 2D convolutional neural networks. Innovat. Res. BioMed. Eng. 43, 422–433. doi: 10.1016/j.irbm.2021.04.002

Degirmenci, M., Ozdemir, M. A., Sadighzadeh, R., and Akan, A. (2018). “Emotion recognition from EEG signals by using empirical mode decomposition,” in 2018 Medical Technologies National Congress (TIPTEKNO) (Magusa), 1–4.

- Degirmenci, M., Yuce, Y. K., and Isler, Y. (2022b). Classiﬁcation of multi-class

motor imaginary tasks using poincare measurements extracted from EEG signals. J. Intell. Syst. Appl. 5, 74–78. doi: 10.54856/jiswa.202212204

- Degirmenci, M., Yuce, Y. K., and Isler, Y. (2022c). “Motor imaginary task

classiﬁcation using statistically signiﬁcant time-domain EEG features,” in 2022 30th Signal Processing and Communications Applications Conference (SIU) (Safranbolu: IEEE), 1–4.

Degirmenci, M., Yuce, Y. K., and Isler, Y. (2024). Classiﬁcation of ﬁnger movements from statistically-signiﬁcant time-domain EEG features. J. Fac. Eng. Arch. Gazi Univ. 39, 1597–1609. doi: 10.17341/gazimmfd.1241334

Degirmenci, M., Yuce, Y. K., Perc, M., and Isler, Y. (2023). Statistically signiﬁcant features improve binary and multiple motor imagery tasks predictions from EEGs. Front. Hum. Neurosci. 17:1223307. doi: 10.3389/fnhum.2023.1223307

Dietterich, T. G. (2002). “Structural, syntactic, and statistical pattern recognition,” in Lecture Notes in Computer Science, Vol. 2396, eds T. Caelli, A. Amin, R. P.W. Duin, D. de Ridder, and M. Kamel (Berlin; Heidelberg: Springer). doi: 10.1007/3-540-70659-3_2

Frei, M. G., and Osorio, I. (2007). Intrinsic time-scale decomposition: time—frequency—energy analysis and real-time ﬁltering of non-stationary signals. Proc. R. Soc. A Math. Phys. Eng. Sci. 463, 321–342. doi: 10.1098/rspa. 2006.1761

Galiotta, V., Quattrociocchi, I., D’Ippolito, M., Schettini, F., Aricò, P., Sdoia, S., et al. (2022). EEG-based brain-computer interfaces for people with disorders of consciousness: features and applications. A systematic review. Front. Hum. Neurosci. 16:1040816. doi: 10.3389/fnhum.2022.1040816

Hart, P. E., Stork, D. G., and Duda, R. O. (2000). Pattern Classiﬁcation, 2nd Edn. New York, NY: A Wiley-Interscience Publication.

Higuchi, T. (1988). Approach to an irregular time series on the basis of the fractal theory. Phys. D Nonlinear Phenomena 31, 277–283. doi: 10.1016/0167-2789(88)90081-4

Hjorth, B. (1970). EEG analysis based on time domain properties. Electroencephalogr. Clin. Neurophysiol. 29, 306–310. doi: 10.1016/0013-4694(70)90143-4

Iscan, Z., Dokur, Z., and Demiralp, T. (2011). Classiﬁcation of electroencephalogram signals with combined time and frequency features. Expert Syst. Appl. 38, 10499–10505. doi: 10.1016/j.eswa.2011.02.110

Isler, Y. (2009). A Detailed Analysis of the Eﬀects of Various Combinations of Heart Rate Variability Indices in Congestive Heart Failure (Ph.D. thesis). Dokuz Eylul University, Izmir.

Isler, Y., and Kuntalp, M. (2009). “Diagnosis of congestive heart failure patients using Poincare measures derived from ECG signals,” in 2009 14th National Biomedical Engineering Meeting (IEEE), 1–4.

Isler, Y., Narin, A., and Ozer, M. (2015). Comparison of the eﬀects of crossvalidation methods on determining performances of classiﬁers used in diagnosing congestive heart failure. Meas. Sci. Rev. 15, 196–201. doi: 10.1515/msr-2015-0027

James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013). An Introduction to Statistical Learning: with Applications in R. 1st Edn (Springer), 181–184.

Karabiber Cura, O., Kocaaslan Atli, S., and Akan, A. (2023). Attention deﬁcit hyperactivity disorder recognition based on intrinsic time-scale decomposition of EEG signals. Biomed. Signal Process. Control 81:104512. doi: 10.1016/j.bspc.2022. 104512

Kato, M., Kanoga, S., Hoshino, T., and Fukami, T. (2020). “Motor imagery classiﬁcation of ﬁnger motions using multiclass CSP,” in 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE), 2991–2994.

Kaya, M., Binli, M. K., Ozbay, E., Yanar, H., and Mishchenko, Y. (2018). A large electroencephalographic motor imagery dataset for electroencephalographic brain computer interfaces. Sci. Data 5, 1–16. doi: 10.1038/sdata.2018.211

Kuhn, M., and Johnson, K. (2013). Applied Predictive Modeling. 1st Edn. New York, NY: Springer, 70.

Labriﬀe, M., Woillard, J.-B., Debord, J., and Marquet, P. (2022). Machine learning algorithms to estimate everolimus exposure trained on simulated

and patient pharmacokinetic proﬁles. Pharm. Syst. Pharmacol. 11, 1018–1028. doi: 10.1002/psp4.12810

Lei, D., Tang, J., Li, Z., and Wu, Y. (2019). Using low-rank approximations to speed up kernel logistic regression algorithm. IEEE Access 7, 84242–84252. doi: 10.1109/ACCESS.2019.2924542

Limbaga, N. J., Mallari, K. L., Yeung, N. R., and Monje, J. C. (2022). “Development of an EEG-based brain-controlled system for a virtual prosthetic hand,” in 2022 IEEE International Conference on Bioinformatics and Biomedicine (BIBM) (Las Vegas, NV), 1714–1717.

Lotte, F., Baugrain, L., Cichocki, A., Clerc, M., Congedo, M., Rakotomamonjy, A., et al. (2018). A review of classiﬁcation algorithms for EEG-based brain-computer interfaces: a 10 year update. J. Neural Eng. 15:031005. doi: 10.1088/1741-2552/aab2f2

Maji, S., Berg, A. C., and Malik, J. (2008). “Classiﬁcation using intersection kernel support vector machines is eﬃcient,” in 2008 IEEE Conference on Computer Vision and Pattern Recognition (Anchorage, AK), 1–8.

Martis, R. J., Acharya, U. R., Tan, J. H., Petznick, A., Tong, L., Chua, C. K., et al. (2013). Application of intrinsic time-scale decomposition (ITD) to EEG signals for automated seizure prediction. Int. J. Neural Syst. 23:1350023. doi: 10.1142/S0129065713500238

Mathworks Matlab 2023b (2023). Train Classiﬁcation Models in Classiﬁcation Learner App. Book Chapter 23 in Statistics and Machine Learning Toolbox User’s Guide, 23.1–23.22. Available online at: https://www.mathworks.com/help/pdf_doc/stats/stats. pdf (accessed February 07, 2024).

Miao, M., Zeng, H., Wang, A., Zhao, C., and Liu, F. (2017). Discriminative spatialfrequency-temporal feature extraction and classiﬁcation of motor imagery EEG: an sparse regression and Weighted Naïve Bayesian Classiﬁer-based approach. J. Neurosci. Methods 278, 13–24. doi: 10.1016/j.jneumeth.2016.12.010

Mitaim, S., and Kosko, B. (1998). Adaptive stochastic resonance. Proc. IEEE 86, 2152–2183. doi: 10.1109/5.726785

Mwata-Velu, T. Y., Avina-Cervantes, J. G., Cruz-Duarte, J. M., Rostro-Gonzalez, H., and Ruiz-Pinales, J. (2021). Imaginary ﬁnger movements decoding using empirical mode decomposition and a stacked BiLSTM architecture. Mathematics 9:3297. doi: 10.3390/math9243297

Mwata-Velu, T. Y., Avina-Cervantes, J. G., Ruiz-Pinales, J., Garcia-Calva, T. A., González-Barbosa, E. A., Hurtado-Ramos, J. B., et al. (2022). Improving motor imagery EEG classiﬁcation based on channel selection using a deep learning architecture. Mathematics 10:2302. doi: 10.3390/math10132302

Narin, A., and Isler, Y. (2021). Detection of new coronavirus disease from chest xray images using pre-trained convolutional neural networks. J. Fac. Eng. Archit. Gazi Univ. 36, 2095–2107. doi: 10.17341/gazimmfd.827921

Narin, A., Isler, Y., and Ozer, M. (2014). Investigating the performance improvement of HRV Indices in CHF using feature selection methods based on backward elimination and statistical signiﬁcance. Comput. Biol. Med. 45, 72–79. doi: 10.1016/j.compbiomed.2013.11.016

Ozdemir, M. A., Degirmenci, M., Izci, E., and Akan, A. (2021). EEG-based emotion recognition with deep convolutional neural networks. Biomed. Eng. 66, 43–57. doi: 10.1515/bmt-2019-0306

Pan, S., Iplikci, S., Warwick, K., and Aziz, T. Z. (2012). Parkinson’s disease tremor classiﬁcation-A comparison between support vector machines and neural networks. Expert Syst. Appl. 39, 10764–10771. doi: 10.1016/j.eswa.2012.02.189

Patro, R. (2021). Cross-Validation: K Fold vs Monte Carlo. Towards Data Science. Available online at: https://towardsdatascience.com/cross-validation-k-foldvs-monte-carlo-e54df2fc179b (accessed February 07, 2024).

Pfurtscheller, G., and Neuper, C. (2001). Motor imagery and direct brain-computer communication. Proc. IEEE 89, 1123–1134. doi: 10.1109/5.939829

Richard, M. D., and Lippmann, R. P. (1991). Neural network classiﬁers estimate Bayesian a posteriori probabilities. Neural Comput. 3, 461–483. doi: 10.1162/neco.1991.3.4.461

- Sayilgan, E., Yuce, Y. K., and Isler, Y. (2019). Prediction of evoking frequency from

steady-state visual evoked frequency. Nat. Eng. Sci. 4, 91–99.

- Sayilgan, E., Yuce, Y. K., and Isler, Y. (2020). Determining gaze information

from steady-state visually-evoked potentials. Karaelmas Sci. Eng. J. 10, 151–157. doi: 10.7212/zkufbd.v10i2.1588

- Sayilgan, E., Yuce, Y. K., and Isler, Y. (2021a). Evaluation of mother wavelets on

steady-state visually-evoked potentials for triple-command brain-computer interfaces. Turk. J. Elect. Eng. Comp. Sci. 29, 2263–2279. doi: 10.3906/elk-2010-26

- Sayilgan, E., Yuce, Y. K., and Isler, Y. (2021b). Evaluation of wavelet features

selected via statistical evidence from steady-state visually-evoked potentials to predict the stimulating frequency. J. Fac. Eng. Archit. Gazi Univ. 36, 593–605. doi: 10.17341/gazimmfd.664583

Sayilgan, E., Yuce, Y. K., and Isler, Y. (2022). Investigating the eﬀect of ﬂickering frequency pair and mother wavelet selection in steady-state visually-evoked potentials on two-command brain-computer interfaces. Innovat. Res. BioMedical Eng. 43, 594–603. doi: 10.1016/j.irbm.2022.04.006

Sciaraﬀa, N., Di Flumeri, G., Germano, D., Giorgi, A., Di Florio, A., Borghini, G., et al. (2022). Evaluation of a new lightweight EEG technology for translational applications of passive brain-computer interfaces. Front. Hum. Neurosci. 16:901387. doi: 10.3389/fnhum.2022.901387

Sharma, R., Kim, M., and Gupta, A. (2022). Motor imagery classiﬁcation in brain-machine interface with machine learning algorithms: classical approach to multi-layer perceptron model. Biomed. Signal Process. Control 71:103101. doi: 10.1016/j.bspc.2021.103101

Tzallas, A. T., Tsipouras, M. G., and Fotiadis, D. I. (2009). Epileptic seizure detection in EEGs using time–frequency analysis. IEEE Transact. Inf. Technol. Biomed. 13, 703–710. doi: 10.1109/TITB.2009.20 17939

Vapnik, V. (1999). The Nature of Statistical Learning Theory. 2nd Edn. New York, NY: Springer.

Velichkovsky, B., Sprenger, A., and Unema, P. (1997). “Towards gaze-mediated interaction: collecting solutions of the “Midas touch problem”,” in Human-Computer Interaction INTERACT’97, IFIP—The International Federation for Information Processing (Boston, MA: Springer).

Vidal, J. J. (1977). Real-time detection of brain events in EEG. Proc. IEEE 65, 633–641. doi: 10.1109/PROC.1977.10542

Voznesensky, A., and Kaplun, D. (2019). Adaptive signal processing algorithms based on EMD and ITD. IEEE Access 7, 171313–171321. doi: 10.1109/ACCESS.2019.2956077

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M.

(2002). Brain–computer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791. doi: 10.1016/S1388-2457(02)00057-3

Yahya, N., Musa, H., Ong, Z. Y., and Elamvazuthi, I. (2019). Classiﬁcation of motor functions from electroencephalogram (EEG) signals based on an integrated method comprised of common spatial pattern and wavelet transform framework. Sensors 19:4878. doi: 10.3390/s19224878

Yesilkaya, B., Sayilgan, E., Yuce, Y. K., Perc, M., and Isler, Y. (2023). Principal component analysis and manifold learning techniques for the design of braincomputer interfaces based on steady-state visually evoked potentials. J. Comput. Sci. 68:102000. doi: 10.1016/j.jocs.2023.102000

Yu, M., and Fang, M. (2022). Feature extraction of rolling bearing multiple faults based on correlation coeﬃcient and Hjorth parameter. ISA Trans. 129, 442–458. doi: 10.1016/j.isatra.2022.02.015

Zahra, H. N., Zakaria, H., and Hermanto, B. R. (2022). Exploration of pattern recognition methods for motor imagery EEG signal with convolutional neural network approach. J. Phys. 2312:012064. doi: 10.1088/1742-6596/2312/1/012064

