# EEG Mouse:A Machine Learning-Based Brain Computer Interface

### Mohammad H. Alomari, Ayman AbuBaker, Aiman Turani, Ali M. Baniyounes, Adnan Manasreh

Electrical and Computer Engineering Department, Applied Science University P.O. Box 166, Amman 11931 Jordan

Abstract—The main idea of the current work is to use a wireless Electroencephalography (EEG) headset as a remote control for the mouse cursor of a personal computer. The proposed system uses EEG signals as a communication link between brains and computers. Signal records obtained from the PhysioNet EEG dataset were analyzed using the Coif lets wavelets and many features were extracted using different amplitude estimators for the wavelet coefficients. The extracted features were inputted into machine learning algorithms to generate the decision rules required for our application. The suggested real time implementation of the system was tested and very good performance was achieved. This system could be helpful for disabled people as they can control computer applications via the imagination of fists and feet movements in addition to closing eyes for a short period of time.

Keywords—EEG; BCI; Data Mining; Machine Learning; SVMs; NNs; DWT; Feature Extraction

I. INTRODUCTION

Brain-Computer Interface (BCI) is a device that enables the use of the brain’s neural activity to communicate with others or to control machines, artificial limbs, or robots without direct physical movements [1-4]. As computerized systems are becoming one of the main tools for making people’s lives easier and with the ongoing growth in the BCI field, it is becoming more important to understand brain waves and analyze EEG signals. Electroencephalography (EEG) is the process of measuring the brain’s neural activity as electrical voltage fluctuations along the scalp as a result of the current flows in brain’s neurons [5]. The brain’s electrical activity is monitored and recorded, in typical EEG tests, using electrodes that are fixed on the scalp [6]. BCI captures EEG signals in conjunction with a specific user activity then uses different signal processing algorithms to translate these records into control commands for different machine and computer applications [7].

BCI was known for its popular use in helping disabled individuals by providing a new channel of communication with the external environment and offering a feasible tool to control artificial limbs [8]. A variety of BCI applications were described in[9] including the control of devices using the translation of thoughts into commands in video games and personal computers. BCI is a highly interdisciplinary research topic that combines medicine, neurology, psychology, rehabilitation engineering, Human-Computer Interaction (HCI), signal processing and machine learning [10].

In our previous research [11-13] we proposed many systems that could efficiently discriminate between executed (or imagined) left and right fist (or feet) movements. In this work, we integrated these systems into one hybrid application that is based on the imagined fists and feet movements.

II. LITERATURE REVIEW

The translation approach used to transform EEG signal patterns into machine commands reflects the strength of BCI applications. In [14], the authors recorded EEG signals for three subjects while imagining either right or left hand movement based on a visual cue stimulus. They were able to classify EEG signals into right and left hand movements using a neural network classifier with an accuracy of 80% and concluded that this accuracy did not improve with increasing number of sessions.

The authors of[15] used features produced by Motor Imagery (MI) to control a robot arm. Features such as the band power in specific frequency bands (alpha: 8-12Hz and beta: 1330Hz) were mapped into right and left limb movements. In addition, they used similar features with MI, which are the Event Related Resynchronization and Synchronization (ERD/ERS) comparing the signal’s energy in specific frequency bands with respect to the mentally relaxed state.

The combination of ERD/ERS and Movement-Related Cortical Potentials (MRCP) was proven to improve the classification of EEG signals as this offers an independent and complimentary information [13, 16]. The authors of [17]presented an approach for the classification of single trial MRCP using a discrete dyadic wavelet transform and Support Vector Machines (SVMs) and they provided a promising classification performance.

A single trial right/left hand movement classification is reported in [18]. The authors analyzed both executed and imagined hand movement EEG signals and created a feature vector consisting of the ERD/ERS patterns of the mu and beta rhythms and the coefficients of the autoregressive model. Artificial Neural Networks (ANNs) is applied to two kinds of testing datasets and an average recognition rate of 93% is achieved.

A three-class BCI system was presented in [19] for the translation of imagined left/right hands and foot movements into commands that operates a wheelchair. This work used many spatial patterns of ERD on mu rhythms along the sensory-motor cortex and the resulting classification accuracy

for online and offline tests was 79.48% and 85.00%, respectively. The authors of [20] proposed an EEG-based BCI system that controls hand prosthesis of paralyzed people by movement thoughts of left and right hands. They reported an accuracy of about 90%.

In [21], a hybrid BCI control strategy is presented. The authors expanded the control functions of a P300 potential based BCI for virtual devices and MI related sensorimotor rhythms to navigate in a virtual environment. Imagined left/right hand movements were translated into movement commands in a virtual apartment and an extremely high testing accuracy results were reached.The Daubechies, Coiflet and Symmlet wavelet families were applied in[22]to a dataset of MI to extract features and describe right and left hand movement imagery. The authors reported that the use of Linear Discriminate Analysis (LDA) and Multilayer Perception (MLP) Neural Networks (NNs) provided good classification results and that LDA classifier achieved higher classification results of up to 88% for different Symmlet wavelets. The authors of[23]used the discrete wavelet transform (DWT) to create inputs for a NNs classifier and the authors reported a very high classification accuracy of 99.87% for the recognition of some mental tasks.

III. THE PROPOSED SYSTEM

The main idea of the current work is to use a wireless EEG headset such as the one designed by NeuroSky[24] as a remote control for the mouse cursor of personal computers and the computer applications. As depicted in Fig. 1, the captured EEG signals have to be pre-processed to filter out the unwanted content and then the content of interest has to be represented using some features that can be inputted into machine learning algorithms. The outcome of this process is a collection of decision rules that can be translated, as required, into PC commands.

[Figure 1]

Fig. 1. A block diagram for the suggested system

A. Eeg Data

The PhysioNetEEG dataset [25] is used in this work. It consists of more than 1500 one or two minutes-duration EEG records obtained from 109 healthy subjects. Subjects were asked to execute and imagine different tasks while 64 channels of EEG signals were recorded from the electrodes that were fitted along the scalp.

In the records of the dataset that are related to the current research, each subject performed the following tasks:

-  One-minute baseline run with eyes open.
-  One-minute baseline run with eyes closed.
-  Three two-minutes experimental runs of imagining moving theright or left fists while the left or right side of a computer screen is showing a target.

 Three two-minute experimental runs of imagining moving both fists or both feet while the top or bottom side of a computer screen is showing a target.

The obtained EEG signals were recorded according to the international 10-20 system as seen in Fig. 2.

[Figure 2]

Fig. 2. Electrode Positions for the C3, Cz, and C4 channels

For this work, we created a subset for 100 subjects including 8 runs per subject. B. Preprocessing

Only channels C3, C4, and Cz were used in our work for two reasons:(1) It is reported in [6] that most EEG channels represent redundant information and (2), it was concludedin[26, 27] that the neural activity that is mostly correlated to the fists movements is almost exclusively contained within these channels as depicted in Fig. 2.

The authors of [28] showed thatEEG signals are noisy and non-stationary signals that have to be filtered to get rid of the unnecessary content. Hence, the channels C3, C4, and Cz were filtered, using a band-pass filter (0.5-50 Hz),for the purpose of removing the DC shifts and minimizing the presence of filtering artifacts at epoch boundaries.

In [29], it was stated that EEG signals are usually masked by physiological artifacts that produce huge amounts of useless data. Eye and muscle movements could be good examples of these artifacts that constitute a challenge in the field of BCI research. The Automatic Artifact Removal (AAR) toolbox [30] was used to process our EEG subset.

A MATLAB script was written to analyze the filtered EEG signals and it was found that a subject imagines opening and closing a fist (or both fists/feet) and keeps doing this for 4.1 seconds then he takes a rest for the duration of 4.2 seconds. This means that each two-minute EEG run includes 15 events that are separated by a short neutral period where the subject relaxes. As the Physionet dataset was sampled at 160 samples per second, each vector includes 656 samples of the original recorded EEG signal. And because we used the available records for 100 subjects, our subset included 18000 vectors representing imagined left fist, right fist, both fists, and both feet movements. An additional 1500 vectors were extracted from the one-minute baseline run (with eyes open) and another 1500 vectors from the one-minute baseline run with eyes closed. So, the total number of extracted samples (events) was 12000 samples.

IV. FEATURE EXTRACTION A. The Discrete Wavelet Transform

The Wavelet transform analysis was used in a wide range of research topics within the field of signal processing. Based on a multi-resolutions process, the wavelet properties of a scalable window allow pinpointing signal components. These properties of dilation and translation enable the extraction of all components for every position by creating different scales and shifted functions (in time domain) of a signal [31, 32]. As a result, wavelet finer and large scaling, permit all information of the signal (the big picture), while small scales shows signal details by zooming into the signal components.

For discrete data, such as the datasets used in the current work, the Discrete Wavelet Transform (DWT) is better fit for analysis. It was shown in [33] that a suitable wavelet function must be used to optimize the analysis performance. A large selection of DWT mother wavelets, such as the Daubechies, Symmlet, and Coif let, is available to be used in our work [22]. But the Coif let(Coif) family of wavelet functions provided the best classification performance in our previous work [11]. So, we decided to calculate the Coif lets wavelets Coif1-Coif5 in this work.

As shown in Fig. 3, the main purpose of the DWT is to decompose the recorded EEG signal into multi-resolution subsets of coefficients: a detailed coefficient subset(cDi) and an approximation coefficient subset (cAi) at theleveli.So, at the first decomposition level we obtain cD1 and cA1 then the first approximation cA1 can be transformed into cD2 and cA2 at the second level, and so on. For our experiments, the decomposition level was set to generate four level details.

[Figure 3]

Fig. 3. The multi-resolution decomposition of a sample EEG signal.

All EEG signals in the subset were sampled at 160Hz. So, the wavelet transformation of each record at four levels results in four details: cD1(40-80Hz), cD2(20-40Hz), cD3(10-20Hz), and cD4(5-10Hz), and a single approximationcA4(0-5Hz). As explained in [11], the details cD2, cD3and cD4 provided proper representation for the activities of interest. So, we decided to extract the vectors of features from these details only.

- B. Amplitude Estimators

Many amplitude estimators for neurological activities were defined mathematically in [34] and some of them were selected based on our previous results obtained in [11].

If we assume that the nth sample of a wavelet decomposed

detail at level i is Di(n), then the following features can be defined:

 Root Mean Square (RMS)

  

 Mean Absolute Value (MAV)

  

 Integrated EEG (IEEG)

  

 Simple Square Integral (SSI)

  

 Variance of EEG (VAR)

  

 Average Amplitude Change (AAC)

  

- C. Feature Vectors

N

1 N

RMSi =

Di2(n)

## å

n=1

N

1 N

MAVi =

Di(n)

å

n=1

N

IEEGi = Di(n)

å

n=1

N

SSIi = Di(n)2

å

n=1

N

1 N -1

VARi =

Di2(n)

å

n=1

N

1 N

AACi =

Di(n+1)-Di(n)

å

n=1

In our experiments, we applied the Coifletswavelets Coif1 to Coif5 for each one of the channels C3, C4, and Cz of an EEG record. This process was repeated for each event in our dataset of 12000 vectors.

Then, all estimators were calculated using (1) through (6) for the details cD2, cD3and cD4 of each instance.At the end of these calculations, 9 features of each estimator (3 channels 3 details) were generated for each Coiflets wavelet. These features were numerically represented in a format that is suitable for use with SVMs and NNs algorithms [35, 36] as described in the next section.

V. MACHINE LEARNING

SVMs and NNs learning algorithms were used in [13, 14, 22, 23, 37] and provided excellent classification performances. A detailed description of SVMs and NNs can be found in[36]. The MATLAB NN toolbox was used for all the training and testing experiments. The training experiments were handled with the aid of the back-propagation learning algorithm [38].

SVM experiments were carried out using the “MySVM” software[39]. SVM can be performed with different kernels and most of them were reported to provide similar results for similar applications [6]. So, the Anova-Kernel SVM was used in this work.

As shown on Fig. 4, NNs and SVMs classifiers were created with 9 inputs, representing features of one estimator. The SVM classifier has one output node representing the target function: closed eyes/opened eyes. The NN classifier has one output node that has five possible classes: opened eyes, left fist, right fist, both fists, and both feet. Both classifiers were integrated such that the NN classifier is only enabled when the eyes are open.

In SVM, each of the degree and gamma parameters were varied from 1 to 10 and the number of hidden layers for the neural network was varied from 1 to 20.

[Figure 4]

Fig. 4. The Hybrid Machine Learning System

At each specific number of hidden layers (or a specific degree-gamma pair), 80% of the samples (9600 events) were randomly selected and used for training and the remaining 20%for testing. This process was repeated 10 times, and in each time the datasets were randomly mixed. For each specific configuration, the average accuracy was calculated for the ten training-testing pairs.

A huge number of training and testing experiments were carried out. Table I and Table II list the best average accuracies with their associated classifier configurations. It can be noted that the use of a SVMs classifier of gamma = 9 and degree = 6 with inputs that were generated by a Coif4 wavelet and MAV features provided the optimum classification performance of an accuracy of 74.97%. In addition, a NNs classifier of 15 hidden layers with inputs that were generated by a Coif2 wavelet and IEEG features provided an accuracy of 71.6%. These are very promising results as they were obtained while most of the available data are for imagined movements.

- TABLE I. OPTIMUM CLASSIFICATION RESULTS ACHIEVED USING DIFFERENT COIFLETSWAVELETS WITH SVMS.

|Features|MAV| | |RMS| | |AAC| | |IEEG| | |SSI| | |VAR| | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Coiflets wavelet|gam|deg|AvgAcc|gam|deg|AvgAcc|gam|deg|AvgAcc|gam|deg|AvgAcc|gam|deg|AvgAcc|gam|deg|AvgAcc|
|Coif1|3|6|0.7011|3|5|0.6911|9|7|0.6821|5|8|0.6930|4|6|0.6183|8|8|0.6011|
|Coif2|8|5|0.6903|9|2|0.6857|3|6|0.6532|6|5|0.6814|3|5|0.6634|5|2|0.6122|
|Coif3|3|4|0.7152|6|2|0.7033|6|9|0.6642|8|7|0.6598|3|7|0.6120|6|5|0.5984|
|Coif4|9|6|0.7497|8|7|0.7112|8|3|0.6803|3|4|0.6786|8|3|0.6045|4|6|0.6103|
|Coif5|9|5|0.7325|4|5|0.7058|2|2|0.6792|6|3|0.6133|8|4|0.6143|5|7|0.6002|

- TABLE II. OPTIMUM CLASSIFICATION RESULTS ACHIEVED USING DIFFERENT COIFLETSWAVELETS WITH NNS.

|Features|MAV| |RMS| |AAC| |IEEG| |SSI| |VAR| |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Coiflets wavelet|HL|AvgAcc|HL|AvgAcc|HL|AvgAcc|HL|AvgAcc|HL|AvgAcc|HL|AvgAcc|
|Coif1|16|0.6166|14|0.6186|17|0.5801|19|0.6612|19|0.6247|13|0.5781|
|Coif2|20|0.6470|19|0.6430|13|0.5821|15|0.7160|19|0.5862|12|0.5801|
|Coif3|16|0.5882|19|0.6349|18|0.5923|20|0.6207|13|0.5578|18|0.6491|
|Coif4|16|0.5984|16|0.6186|19|0.6045|18|0.6065|9|0.5538|15|0.5538|
|Coif5|11|0.6247|18|0.6045|20|0.5984|19|0.6227|13|0.5335|17|0.5396|

VI. REAL TIME IMPLEMENTATION

A simple software interface was designed as show in Fig. 5. This software reads streams of EEG signals from a test EEG record or from an EEG mouse (if available).

The system extracts the features needed for the SVM and NN decision rules and provides near-real time actions. The default configurations of this system are to translate the “closing eyes for 2s” activity into a mouse click and the

imagined left/right fists, both fists, and both feet movements into computer cursor movements as seen in Fig. 6. These configurations can be reprogrammed to run different computer applications instead of simple cursor movements.

[Figure 5]

- Fig. 5. EEG Mouse Control Panel
- Fig. 6. The Suggested Real-Time Implementation of the System

[Figure 6]

VII. CONCLUSIONS

The objective of this work was to enable the use of the available commercial EEG headsets as a remote control for computer applications. Disabled people may use this system as a channel of communication with computers and they can provide some simple computer commands by imagination. Signal records obtained from the PhysioNet EEG dataset were analyzed using the Coiflets wavelets and machine learning algorithms and promising classification performances were obtained.

REFERENCES

- [1] J. P. Donoghue, "Connecting cortex to machines: recent advances in brain interfaces," Nature Neuroscience Supplement, vol. 5, pp. 1085– 1088, 2002.
- [2] S. Levine, J. Huggins, S. BeMent, R. Kushwaha, L. Schuh, E. Passaro, M. Rohde, and D. Ross, "Identification of electrocorticogram patterns as the basis for a direct brain interface," Journal of Clinical Neurophysiology, vol. 16, pp. 439-447, 1999.
- [3] A. Vallabhaneni, T. Wang, and B. He, "Brain—Computer Interface," in Neural Engineering, B. He, Ed.: Springer US, 2005, pp. 85-121.
- [4] [4] J. Wolpaw, N. Birbaumer, D. McFarland, G. Pfurtscheller, and T. Vaughan, "Brain-computer interfaces for communication and control," Clinical Neurophysiology, vol. 113, pp. 767-791, 2002.
- [5] E. Niedermeyer and F. H. L. da Silva, Electroencephalography: Basic Principles, Clinical Applications, and Related Fields: Lippincott Williams & Wilkins, 2005.
- [6] J. Sleight, P. Pillai, and S. Mohan, "Classification of Executed and Imagined Motor Movement EEG Signals," Ann Arbor: University of Michigan, 2009, pp. 1-10.
- [7] B. Graimann, G. Pfurtscheller, and B. Allison, "Brain-Computer Interfaces: A Gentle Introduction," in Brain-Computer Interfaces: Springer Berlin Heidelberg, 2010, pp. 1-27.
- [8] A. E. Selim, M. A. Wahed, and Y. M. Kadah, "Machine Learning Methodologies in Brain-Computer Interface Systems," in Biomedical Engineering Conference, 2008. CIBEC 2008. Cairo International, 2008, pp. 1-5.
- [9] E. Grabianowski, "How Brain-computer Interfaces Work," HowStuffWorks, Inc, 2007.
- [10] M. Smith, G. Salvendy, K. R. M√ºller, M. Krauledat, G. Dornhege, G. Curio, and B. Blankertz, "Machine Learning and Applications for BrainComputer Interfacing," in Human Interface and the Management of Information. Methods, Techniques and Tools in Information Design. vol. 4557: Springer Berlin Heidelberg, 2007, pp. 705-714.
- [11] M. H. Alomari, E. A. Awada, A. Samaha, and K. Alkamha, "WaveletBased Feature Extraction for the Analysis of EEG Signals Associated with Imagined Fists and Feet Movements," Computer and Information Science, vol. 7, pp. 17-27, 2014.
- [12] M. H. Alomari, E. A. Awada, and O. Younis, "Subject-Independent EEG-Based Discrimination Between Imagined and Executed, Right and Left Fists Movements," European Journal of Scientific Research, vol. 118, pp. 364-373, 2014.
- [13] M. H. Alomari, A. Samaha, and K. AlKamha, "Automated Classification of L/R Hand Movement EEG Signals using Advanced Feature Extraction and Machine Learning," International Journal of Advanced Computer Science and Applications, vol. 4, pp. 207-212, 2013.
- [14] G. Pfurtscheller, C. Neuper, D. Flotzinger, and M. Pregenzer, "EEGbased discrimination between imagination of right and left hand movement," Electroencephalography and Clinical Neurophysiology, vol. 103, pp. 642-651, 1997.
- [15] F. Sepulveda, "Brain-Actuated Control of Robot Navigation," in Advances in Robot Navigation, A. Barrera, Ed.: InTech, 2011.
- [16] A.-K. Mohamed, "Towards improved EEG interpretation in a sensorimotor BCI for the control of a prosthetic or orthotic hand," in Faculty of Engineering. vol. Thesis: Master of Science in Engineering Johannesburg: University of Witwatersrand, 2011, p. http://hdl.handle.net/10539/10546.
- [17] D. Farina, O. F. d. Nascimento, M.-F. Lucas, and C. Doncarli, "Optimization of wavelets for classification of movement-related cortical potentials generated by variation of force-related parameters," Journal of Neuroscience Methods, vol. 162, pp. 357-363, 5/15/ 2007.
- [18] J. A. Kim, D. U. Hwang, S. Y. Cho, and S. K. Han, "Single trial discrimination between right and left hand movement with EEG signal," in Proceedings of the 25th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, Cancun, Mexico, 2003, pp. 3321-3324 Vol.4.
- [19] Y. Wang, B. Hong, X. Gao, and S. Gao, "Implementation of a BrainComputer Interface Based on Three States of Motor Imagery," in 29th

- Annual International Conference of the IEEE Engineering in Medicine and Biology Society, 2007. EMBS 2007., 2007, pp. 5059-5062.
- [20] C. Guger, W. Harkam, C. Hertnaes, and G. Pfurtscheller, "Prosthetic Control by an EEG-based Brain- Computer Interface (BCI)," in AAATE 5th European Conference for the Advancement of Assistive Technology, Düsseldorf, Germany, 1999.
- [21] Y. Su, Y. Qi, J.-x. Luo, B. Wu, F. Yang, Y. Li, Y.-t. Zhuang, X.-x. Zheng, and W.-d. Chen, "A hybrid brain-computer interface control strategy in a virtual environment," Journal of Zhejiang University SCIENCE C, vol. 12, pp. 351-361, 2011.
- [22] I. Homri, S. Yacoub, and N. Ellouze, "Optimal segments selection for EEG classification," in 6th International Conference on Sciences of Electronics, Technologies of Information and Telecommunications (SETIT), Sousse, Tunisia, 2012, pp. 817-821.
- [23] M. Tolić and F. Jović, "Classification of Wavelet Transformed EEG Signals with Neural Network for Imagined Mental and Motor Tasks," International Journal of Fundamental and Applied Kinesiology, vol. 45, pp. 130-138, 2013.
- [24] NeuroSky, "MindWave Mobile: MyndPlay Bundle," in EEG Biosensor Solutions: http://neurosky.com/products-markets/eeg-biosensors, 2014.
- [25] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, P. C. Ivanov, R. G. Mark, J. E. Mietus, G. B. Moody, C.-K. Peng, and H. E. Stanley, "PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals," Circulation, vol. 101, pp. e215-e220, June 13, 2000 2000.
- [26] L. Deecke, H. Weinberg, and P. Brickett, "Magnetic fields of the human brain accompanying voluntary movements: Bereitschaftsmagnetfeld," Experimental Brain Research, vol. 48, pp. 144-148, 1982.
- [27] C. Neuper and G. Pfurtscheller, "Evidence for distinct beta resonance frequencies in human EEG related to specific sensorimotor cortical areas," Clinical Neurophysiology, vol. 112, pp. 2084-2097, 2001.
- [28] R. Romo-Vazquez, R. Ranta, V. Louis-Dorr, and D. Maquin, "EEG Ocular Artefacts and Noise Removal," in 29th Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS 2007. , Lyon, 2007, pp. 5445-5448.
- [29] G. Bartels, S. Li-Chen, and L. Bao-Liang, "Automatic artifact removal

- from EEG - a mixed approach based on double blind source separation and support vector machine," in 2010 Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), 2010, pp. 5383-5386.
- [30] G. Gómez-Herrero, "Automatic Artifact Removal (AAR) toolbox for MATLAB," in Transform methods for Electroencephalography (EEG): http://kasku.org/projects/eeg/aar.htm, 2008.
- [31] S. Tuntisak and S. Premrudeepreechacharn, "Harmonic Detection in Distribution Systems Using Wavelet Transform and Support Vector Machine," in 2007 IEEE Lausanne Power Tech, Lausanne, 2007, pp. 1540-1545.
- [32] L. Qingyang and S. Zhe, "Method of Harmonic Detection Based On the Wavelet Transform," in International Conference on Information and Computer Applications (ICICA), Hong Kong, 2012, pp. 213-217.
- [33] A. Phinyomark, C. Limsakul, and P. Phukpattaranont, "Optimal Wavelet Functions in Wavelet Denoising for Multifunction Myoelectric Control," ECTI Transactions on Electrical Eng., Electronics, and Communications, vol. 8, pp. 43-52, 2010.
- [34] A. Phinyomark, F. Quaine, Y. Laurillau, S. Thongpanja, C. Limsakul, and P. Phukpattaranont, "EMG Amplitude Estimators Based on Probability Distribution for Muscle-Computer Interface," Fluctuation and Noise Letters, vol. 12, p. 1350016, 2013.
- [35] M. Al-Omari, R. Qahwaji, T. Colak, and S. Ipson, "Machine learningbased investigation of the associations between cmes and filaments," Solar Physics, vol. 262, pp. 511-539, 2010.
- [36] R. Qahwaji, T. Colak, M. Al-Omari, and S. Ipson, "Automated Prediction of CMEs Using Machine Learning of CME – Flare Associations," Sol. Phys, vol. 248, pp. 471-483 2008.
- [37] P. A. Kharat and S. V. Dudul, "Daubechies Wavelet Neural Network Classifier for the Diagnosis of Epilepsy," Wseas Transactions on Biology and Biomedicine, vol. 9, pp. 103-113, 2012.
- [38] S. E. Fahlmann and C. Lebiere, "The cascade-correlation learning architecture," in Advances in Neural Information Processing Systems 2 (NIPS-2) Denver, Colorado, 1989.
- [39] S. Rüping, "mySVM-Manual ": University of Dortmund, Lehrstuhl Informatik 8, 2000.

