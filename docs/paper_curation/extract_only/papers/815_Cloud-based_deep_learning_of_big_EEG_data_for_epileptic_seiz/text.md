## arXiv:1702.05192v1[cs.LG]17Feb2017

# Cloud-based Deep Learning of Big EEG Data for Epileptic Seizure Prediction

Mohammad-Parsa Hosseini1, Hamid Soltanian-Zadeh2,3, Kost Elisevich4,5, and Dario Pompili1 1Dept. of Electrical and Computer Engineering, Rutgers University–New Brunswick, NJ, USA 2Image Analysis Lab, Dept. of Radiology and Research Administration, Henry Ford Health System, MI, USA 4Dept. of Clinical Neuroscience, Spectrum Health System, MI, USA 3Division of Neurosurgery, College of Human Medicine, Michigan State University, MI, USA

1{parsa, pompili}@cac.rutgers.edu, 3hsoltan1@hfhs.org, 4konstantin.Elisevich@spectrumhealth.org

Abstract—Developing a Brain-Computer Interface (BCI) for seizure prediction can help epileptic patients have a better quality of life. However, there are many difﬁculties and challenges in developing such a system as a real-life support for patients. Because of the nonstationary nature of EEG signals, normal and seizure patterns vary across different patients. Thus, ﬁnding a group of manually extracted features for the prediction task is not practical. Moreover, when using implanted electrodes for brain recording massive amounts of data are produced. This big data calls for the need for safe storage and high computational resources for real-time processing. To address these challenges, a cloud-based BCI system for the analysis of this big EEG data is presented. First, a dimensionality-reduction technique is developed to increase classiﬁcation accuracy as well as to decrease the communication bandwidth and computation time. Second, following a deep-learning approach, a stacked autoencoder is trained in two steps for unsupervised feature extraction and classiﬁcation. Third, a cloud-computing solution is proposed for real-time analysis of big EEG data. The results on a benchmark clinical dataset illustrate the superiority of the proposed patientspeciﬁc BCI as an alternative method and its expected usefulness in real-life support of epilepsy patients.

Index Terms—Big Data; Brain-Computer Interface; Cloud Computing; Deep Learning; EEG; Epilepsy; Seizure Prediction.

I. INTRODUCTION

Motivation: Almost one percent of the world’s population suffers from epilepsy [1], a chronic disorder characterized by the occurrence of spontaneous seizures. Although the symptoms of a seizure affect any part of the body, the electrical events that produce the symptoms occur in the brain. For about 30 percent of the patients, medications are not curative and, even after surgery, many patients may have spontaneous seizures [2]. Anxiety due to the possibility of a seizure occurring may affect the quality of life of the patients as well as their safety, relationships, work condition, driving and so much more.

Vision: The use of computers to help physicians in the acquisition, management, storage, and reporting of the biomedical signals is well established [3]–[6]. To this end, BrainComputer Interfaces (BCIs) use Electroencephalogram (EEG) which is a measure of brain waves. For example, a BCI system for seizure forecasting can help epileptic patients have a better quality of life. In order for such a BCI system

to work effectively, computational algorithms must reliably identify periods of increased probability of seizure occurrence. If the occurrence of seizures could be identiﬁed, designing devices to warn patients would be possible and patients could avoid dangerous activities like driving or swimming. Also, medications could be used only when needed to prevent impending seizures.

Challenges: There are many difﬁculties and challenges in developing a seizure-prediction system as a real-life support for epileptic patients. The ﬁrst challenge is due to the fact that EEG is not a stationary signal. Therefore, normal and seizure patterns may vary across different patients. As a result, ﬁnding a group of manually-extracted features might not scale well to new patterns of seizure activity, and supervised feature extraction may not be sufﬁcient for learning algorithms. The second challenge relates to situations of electrodes implanted within the head that provide for intracranial electroencephalography (iEEG). This method of brain-signal recording has potential advantages like high spatio-temporal resolution and electro-optic mapping of the dynamic neuronal activity. However, implanted electrodes generate massive amounts of realtime data leading to the big data problem. This situation calls for a safe storage to save the large volume of data and for high computational resources to process the data in real time.

Our Approach: Signal processing, machine learning, and brain-state prediction need to be carried out in big data in order to develop a practical BCI. The next generation BCI systems may be connected to high-performance computing servers to process medical big data in real-time. Cloud computing is a new Information and Communications Technology (ICT) which enables ubiquitous and on-demand access to computational resources through the global Internet. Our approach is to develop new processing and classiﬁcation methods to be implemented as a cloud-based BCI.

Contributions: To address existing challenges, we introduce a cloud-based BCI system for big data problem in epilepsy. Moreover, we have developed a deep-learning unsupervised feature-extraction technique for seizure prediction. Speciﬁcally, our contributions include the development of the following novel methods:

• A dimension reduction using Principal and Independent Component Analysis to increase the classiﬁcation accu-

racy as well as to reduce the computation time and the communication bandwidth.

- • A stacked autoencoder as a deep-learning structure to analyze EEG signals for the epileptic seizure prediction.
- • A BCI system implemented in the cloud as a safe storage with high computational resources for big data problem generated by implanted electrodes.

The proposed system has the ability of pervasive datacollection and analysis, which is useful in real-life support for epileptic patients. To study the accuracy and performance, the system is evaluated and compared to other methods on a benchmark epilepsy dataset.

Paper Outline: The remainder of this paper is organized as follows. In Sect. II, we provide a literature review. In Sect. III, we present our solution including dimensionality reduction, a novel stacked autoencoder as a deep-learning structure to analyze EEG signals, and cloud-computing framework. Then, in Sect. IV, we discuss the proof-of-concept prototype of the proposed BCI seizure predictor and show preliminary results. Finally, in Sect. VI, the paper is concluded.

II. LITERATURE REVIEW

In this section, we provide an overview of the previous studies on seizure prediction systems and big data management of epilepsy. In [7], extracting EEG features for epileptic seizure prediction is followed by an elimination-based feature selection method to improve the efﬁcacy and diminish redundant points. In [8], a support vector machine (SVM) algorithm was developed to identify preictal states in continuous iEEG recordings of dogs with naturally occurring epilepsy. In [9], spectral power and ratios of spectral power extracted from iEEG and processed by a second-order Kalman ﬁlter and then input to a linear SVM classiﬁer for epileptic seizure prediction.

- In [10], for classiﬁcation of preictal and interictal stages, artifact-free preictal and interictal EEG epochs were acquired and characterized with global feature descriptors. In general, existing works have focused on local processing and storage without considering multiple channels and big patient data.
- In [11], our group developed a multi-tier distributed computing structure based on Mobile Device Cloud (MDC) and cloud computing for real-time epileptic seizure detection. In this work, we have developed a deep learning structure in the cloud to address the big data analysis problem in epilepsy. In contrast to the existing methods, the proposed method extracts unsupervised features from iEEG patterns to predict seizures.

III. PROPOSED WORK

We propose a seizure prediction system for real-time big data analysis of EEG that can be implemented as a cloudbased service. In Sect.III-A, the data dimension is reduced by principal and independent component analysis. Decreasing the data dimensions decreases the telecommunication bandwidth needed for sending the data to the cloud, increases the classiﬁcation accuracy by eliminating noise information, and reduces the computational time and energy. In Sect.III-B, a deep learning technique is developed using Stack Autoencoder for unsupervised feature extraction from big unlabeled data. In

Algorithm 1: Dimension Reduction by PCA + I-ICA

Input: D-dimensional EEG raw data d = [d1,··· ,dD]T Output: M-dimensional signal x = [x1,··· ,xM]T,

denotes the element wise multiplication Compute Covariance matrix of D Choose P largest eigenvalues Find Y = WTD , Y is N dimensional for i := 1 → N do

[Y,X,Z,E] = concatenation{yi xi zi ei}Ni=1

end for k := 1 → K do

Deﬁne zki as activity of kth source for ith sample Deﬁne mk = Ni=1 zki as the active sources Calculate p(Z|π1,...,πK) by

K k=1 πm

k (1 − πk)N−m

k

k

### for i := 1 → N do Deﬁne gk as the kth column of G Find µ± by g

T k e◦ki±σe2

gkT gk Find σ2 by σ

2 e

gkT gk Find e◦ki by (eki|zki = 0) Calculate p(xki|G,x−ki,yi,zi) by

if xki > 0 then N(xki;µ−,σ2) if xki < 0 then N(xki;µ+,σ2)

end

end Find X by G[X Z] + E Extract x = [x1,··· ,xM]T from X

the end, a softmax layer classiﬁes interictal (baseline) patterns of Preictal (prior to seizure) signals. In Sect.III-C, a cloud based architecture is described for the BCI system.

### A. Dimensionality Reduction: For an efﬁcient analysis

of a complex data set, dimensionality reduction is critical. Given a data space d ∈ RN, dimension reduction methods [12], [13] ﬁnd a mapping x = f(d) : RD → RM (M < D) such that the transformed data vector x ∈ RM preserves most of the information of d. In [11], we proposed a method based on Inﬁnite Independent Component Analysis (I-ICA) [14] for the EEG feature selection task. In this paper, to enhance the dimensionality reduction process, a Principal Component Analysis (PCA) method is applied before I-ICA. PCA generates a diagonal covariance matrix from the input data [15]–[17]. Then, using a transformation each dimension is normalized such that the covariance matrix is equal to the identity matrix [18]. As a result, small trailing eigenvalues are discarded and also computational complexity is decreased by minimizing pairwise dependencies. In this combination, PCA decorrelates the input EEG raw data and the remaining higher-order dependencies are separated by I-ICA. The proposed method for dimensionality reduction is described in Algorithm 1.

#### B. Deep Network: A stacked autoencoder which is a class

of deep neural networks [19] with two sparse encoders as hidden layers is developed. Stacked autoencoder captures the hierarchical grouping of the EEG input for seizure prediction

task. The encoder maps the input to a hidden representation. The size of the second hidden layer is designed less than the ﬁrst hidden layer so the second encoder learns an even smaller representation of the input data. The deep network structure is shown in Fig 1. Hidden layers are trained individually in an unsupervised method. The training data without labels are used to replicate the input from the output in the training step. To enforce a constraint on the sparsity of the output from the hidden layer, the impact of a sparsity regularizer is controlled. The ﬁrst autoencoder tends to learn ﬁrst-order features in the raw EEG input. Using the primary features as the input to second hidden layer, the second-order features are extracted. Then, a softmax layer is trained and the layers are joined to form a deep network. Finally, the deep network is trained one ﬁnal time in a supervised manner. The pseudocode of the proposed classiﬁcation method is shown in Algorithm 2.

The main property of stacked autoencoder is the ability of feature extraction from a large amount of unlabeled data which makes it a suitable solution for the big data problem. A nonlinear transformation is applied to each layer’s input and a representation is provided in the output. Thus, there is no need to extract EEG features by hand-engineering techniques for each patient. In deep architecture, multiple nonlinear transformation layers are stacked together to represent a nonlinear function of EEG data. A gradient-log-normalizer of the categorical probability distribution as softmax layer [20] is used to classify the nonlinear function of EEG as interictal or preictal signal in the last layer.

r)P(x|cr) K

k=1 P(ck)P(x|ck) = exp(a

r)

P(cr|x) = P(c

K k=1 exp(ak) (1) where ak = ln(P(ck)P(x|ck)), P(ck) is the class prior probability, and P(x|ck) is the conditional probability of the sample given class k.

C. Cloud Computing: Cloud computing provides a limitless scale of computing power that can be made available on demand and by way of the Internet makes it ubiquitously available for an extensive global reach. There are many cloud platforms including Microsoft, Google and Amazon AWS. But for the purposes of our study and based on proven use-cases for large scale processing, we will base our reference of cloud usage to the Amazon Cloud, otherwise called Amazon Web Services (AWS). The cloud is generally broken into three layers based on the service provided: (1) Infrastructure as a Service (IaaS); (2) Platform as a Service (PaaS); and (3) Software as a Service (SaaS). These 3 layers will all lend to the different infrastructural setup of the BCI as follows:

IaaS provides computing power, networking, storage and virtual orchestrators and operating systems. It is available at large scale and on demand with the ability to deliver High Performance Computing (HPC) which lends itself well to the processing required with rapid real-time epilepsy monitoring. An applicable BCI system dealing with large amounts of data from distributed electrodes requires storage capability and both rapid and timely event-related mining to produce intelligence in the forms of trends, predictions and recommendations. With a low cost of entry and ease of setup, the core engine of the BCI can be effectively deployed using the AWS HPC. High Performance Computing processors allow the BCI system

[Figure 1]

Fig. 1. The encoders from the autoencoders have been used to extract features. To form a deep network, the encoders from the autoencoders are stacked together followed by a softmax layer.

Algorithm 2: Deep learning by Stacked Autoencoder

Input: M-dimensional data, x = [x1,··· ,xM]T Output: Classiﬁcation result as preictal (0) or interictal

(1) signal; output → (0,1)

begin for i := 1 →#HiddenLayers do

Decrease the size of the ith hidden layer, P(i)<P(i-1) Train unsupervised the ith autoencoder Set explicitly the random number generator seed Control the impact of an L2 regularizer for weights Control the impact of a sparsity regularizer Control the output sparsity from the hidden layer Use the ith feature set for training in the next layer

end Train supervised a softmax layer to classify ith features Stack the encoders from the autoencoders with softmax Compute the results on the test set output → (0,1) Do ﬁne tuning by retraining on the training data

to function above a teraﬂop capacity or 1012 ﬂoating-point operations per second allowing for realtime results inspite of large data entry. The Health Insurance Portability and Accountability Act (HIPAA) and its Protected Health Information (PHI) provision also requires service providers to adhere to strict assurrances regarding protection of personal data. A need for encryption and use of AWS HIPAA eligible [21] services are required to host the BCI system.

PaaS uses an open source allowing developers from different constituencies to leverage the BCI to continue developing modules and customized features for their local environment in order to adapt the application to their practices and needs. SaaS uses a cloud-based BCI application allowing a good deal of processing power to be made available and distributed globally with decreased reliance on local extensive computer infrastructure in order to complete predictions. Aside from the standard electroencephalographic recording units and other specialized detection tools; run analysis, simulations, and other high-end processes can be initiated from relatively light client applications including smartphone apps.

IV. RESULTS

A proof-of-concept prototype of the proposed BCI seizure predictor was developed in the cloud and Autonomic Computing Center (CAC), Rutgers University. In this testbed, we chose to use a benchmark dataset of epilepsy, an HP laptop with intel i5 processor, 8 GB RAM and battery capacity of 4400 mAh, and a supercluster of computers hosted by Amazon

[Figure 2]

Fig. 2. A comparison of interictal (baseline) iEEG segment on top and preictal (before seizure) iEEG segment on the bottom.

Elastic Compute Cloud (EC2). Message Queuing Telemetry Transport (QMTT) and RESTful Web Service protocols are used for sending data in cloud [22]. The clinical iEEG dataset of two epileptic patients (60 interictal and 60 preictal segments) with temporal and extratemporal lobe epilepsy has been used, which was jointly developed by the University of Pennsylvania and the Mayo Clinic, and sponsored by the American Epilepsy Society [23].1 Fig. 2 compares the patterns of the interictal and preictal segments.

The database consists of a few independent cases with a big data problem. Therefore, algorithms should be regulated against over ﬁtting, and some techniques such as KNN or tree-based algorithms did not work well. However, since the proposed solution extracts the features in an unsupervised manner, the risk of overﬁtting is decreased. Moreover, to evaluate the generality of the results, we used leave-one-out as an exhaustive cross validation technique [24]–[26]. Using this technique, the model is ﬁtted to subsets of EEG data and the accuracy of the model is found using the held-out sample [27].

TABLE I CONFUSION MATRIX. THE DIAGONAL ELEMENTS SHOW THE CORRECT DECISIONS

Output interictal Output preictal Total

|Target interictal|56<br><br>|3|59<br><br>|
|---|---|---|---|
|Target preictal|4<br><br>|57|61<br><br>|
|Total<br><br>|60|60|120|

The confusion matrix of the proposed method is shown in Table I. To evaluate the classiﬁcation ability of the proposed unsupervised feature extraction, the EEG feature sets are used for classiﬁcation by other methods listed in Table II. The extracted features are based on fast Fourier transform, general energy average, and energy STDV over time for each channel, power spectral density correlation coefﬁcients, partial directed coherence of the coefﬁcients, power in band, low-gamma phase sync, and log of energy in different frequency bands for each channel [28]. Experimental results in Table II show that the proposed deep learning method outperforms previous methods for the EEG seizure prediction task. The feasibility of using cloud computing is analyzed by the network latency

1The Dataset recorded by 15 electrodes. Preicatl and interictal data are segmented in 10 minute long clips. The sampling rate is 5000 Hz and the reference recorded voltage is an electrode outside the brain. Preictal data segments covered one hour prior to seizure and seizure horizon is ﬁve minutes. The pre-seizure horizon grantees that seizures could be foretasted with enough warning to allow using medications for preventing seizure occurring.

offered by Amazon EC2 cloud servers. The Round Trip Time (RTT) for servers located at different geographical locations (Virginia, Oregon, Singapore, and Ireland) is calculated for 64B EEG segments at 10 days using the ping command. The shortest RTT is 15 ms for Virginia server and the longest RTT is 97 ms for Oregon server.

TABLE II ACCURACY, PRECISION, SENSITIVITY, SPECIFICITY, FPR, AND FNR FOR PROPOSED CLASSIFICATION COMPARED WITH THE OTHER METHODS

Methods Accuracy Precision Sensitivity FPR FNR Proposed Method 0.94 0.95 0.93 0.05 0.06 Random Forest 0.75 0.78 0.74 0.22 0.25 Linear SVM 0.71 0.73 0.70 0.27 0.29 Non-linear SVM 0.78 0.80 0.77 0.20 0.22 MLP Neural Network 0.68 0.70 0.67 0.31 0.32

V. CONCLUSION

Efﬁciently handling and processing of medical big data can provide useful information about a patient and about diseases. This is now a high-focus area in data science. Intracranially implanted electrodes can be used for seizure prediction preparatory to stimulus delivery for aborting the event. Such electrodes generate considerable amounts of data, calling for safe storage and high computational resources to process big data. On the other hand, iEEG records a larger variety of patterns with ﬂuctuations in amplitude and frequency, making feature extraction a challenging problem. In order to address these two broad issues, we introduced a novel cloud-based BCI to provide real-time seizure prediction from iEEG data. The proposed preprocessing step as a dimensionality reduction provides more accurate classiﬁcation and decreases energy, computation time, and communication bandwidth. The developed deep-learning methods have the capability for unsupervised feature extraction and, therefore, represent a suitable substitute to manual feature-extraction techniques for classiﬁcation purposes. These methods extract high-level, complex abstractions for data representations through a hierarchical learning process. The key beneﬁt of the proposed method centers upon the analysis and learning allowed from massive amounts of unsupervised data, making it a practical method for developing a patient-based seizure prediction system. A cloud-based deep-learning method that is able to perform seizure prediction under such circumstances has immediate applicability in the present day.

VI. HOW TO CITE ITEM

M.P. Hosseini, H. Soltanian-Zadeh, K. Elisevich, D. Pompili Cloud-based Deep Learning of Big EEG Data for Epileptic Seizure Prediction, IEEE Global Conference on Signal and Information Processing (GlobalSIP), IEEE, 2016.

REFERENCES

- [1] “World health organization.” [Online]. Available: https://http://www. who.int/mediacentre/factsheets/fs999/en/,RetrievedonSept14,2016.
- [2] M.-P. Hosseini, M. R. Nazem-Zadeh, D. Pompili, and H. SoltanianZadeh, “Statistical validation of automatic methods for hippocampus segmentation in mr images of epileptic patients,” in Proc. of IEEE International Conference of Engineering in Medicine and Biology Society (EMBC), 2014, pp. 4707–4710.

- [3] M. P. Hosseini, H. Soltanian-Zadeh, and S. Akhlaghpoor, “Detection and severity scoring of chronic obstructive pulmonary disease using volumetric analysis of lung ct images,” Iranian Journal of Radiology, vol. 9, no. 1, pp. 22–27, 2012.
- [4] M.-P. Hosseini, H. Soltanian-Zadeh, and S. Akhlaghpoor, “Three cuts method for identiﬁcation of copd.” Acta Medica Iranica Journal, vol. 51, no. 11, pp. 771–778, 2013.
- [5] M.-P. Hosseini, H. Soltanian-Zadeh, S. Akhlaghpoor, A. Jalali, and M. Bakhshayesh Karam, “Designing a new cad system for pulmonary nodule detection in high resolution computed tomography (hrct) images,” Tehran University Medical Journal (TUMJ), vol. 70, no. 4, pp. 250–256, 2012.
- [6] M. P. Hosseini, H. Soltanian-Zadeh, and S. Akhlaghpoor, “Computeraided diagnosis system for the evaluation of chronic obstructive pulmonary disease on ct images,” Tehran University Medical Journal TUMS Publications, vol. 68, no. 12, pp. 718–725, 2011.
- [7] N. Wang and M. R. Lyu, “Extracting and selecting distinctive eeg features for efﬁcient epileptic seizure prediction,” IEEE Journal of Biomedical and Health Informatics, vol. 19, no. 5, pp. 1648–1659, 2015.
- [8] B. H. Brinkmann, E. E. Patterson, C. Vite, V. M. Vasoli, D. Crepeau, M. Stead, J. J. Howbert, V. Cherkassky, J. B. Wagenaar, B. Litt et al., “Forecasting seizures using intracranial eeg measures and svm in naturally occurring canine epilepsy,” PloS one, vol. 10, no. 8, 2015.
- [9] Z. Zhang and K. K. Parhi, “Low-complexity seizure prediction from ieeg/seeg using spectral power and ratios of spectral power,” IEEE transactions on biomedical circuits and systems, vol. 10, no. 3, pp. 693– 706, 2016.
- [10] L.-C. Lin, S. C.-J. Chen, C.-T. Chiang, H.-C. Wu, R.-C. Yang, and C.S. Ouyang, “Classiﬁcation preictal and interictal stages via integrating interchannel and time-domain analysis of eeg features,” Clinical EEG and neuroscience, 2016.
- [11] M.-P. Hosseini, A. Hajisami, and D. Pompili, “Real-time epileptic seizure detection from eeg signals via random subspace ensemble learning,” IEEE International Conference on Autonomic Computing (ICAC), pp. 209–218, 2016.
- [12] B. Babagholami-Mohamadabadi, A. Zarghami, M. Zolfaghari, and M. S. Baghshah, “Pssdl: Probabilistic semi-supervised dictionary learning,” in Joint European Conference on Machine Learning and Knowledge Discovery in Databases. Springer, 2013, pp. 192–207.
- [13] M. Rahmani and G. Atia, “A subspace learning approach for high dimensional matrix decomposition with efﬁcient column/row sampling,” in Proceedings of The 33rd International Conference on Machine Learning, 2016, pp. 1206–1214.
- [14] D. Knowles and Z. Ghahramani, “Inﬁnite sparse factor analysis and inﬁnite independent components analysis,” in Independent Component Analysis and Signal Separation. Springer Berlin Heidelberg, 2007, pp. 381–388.
- [15] S. Minaee and Y. Wang, “Screen content image segmentation using least absolute deviation ﬁtting,” in IEEE International Conference on Image Processing 2015, 2015.
- [16] M. Rahmani and G. Atia, “Randomized robust subspace recovery

- for high dimensional data matrices,” arXiv preprint arXiv:1505.05901, 2015.
- [17] M. Joneidi, P. Ahmadi, M. Sadeghi, and N. Rahnavard, “Union of lowrank subspaces detector,” IET Signal Processing, vol. 10, no. 1, pp. 55–62, 2016.
- [18] S. Minaee and Y. Wang, “Fingerprint recognition using translation invariant scattering network,” in IEEE Signal Processing in Medicine and Biology Symposium 2015, 2015.
- [19] Y. Chen, Z. Lin, X. Zhao, G. Wang, and Y. Gu, “Deep learning-based classiﬁcation of hyperspectral data,” IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 7, no. 6, pp. 2094–2107, 2014.
- [20] R. Guo, L. Liu, W. Wang, A. Taalimi, C. Zhang, and H. Qi, “Deep tree-structured face: A uniﬁed representation for multi-task facial biometrics,” in 2016 IEEE Winter Conference on Applications of Computer Vision (WACV). IEEE, 2016, pp. 1–8.
- [21] “Amazon web services.” [Online]. Available: https://aws.amazon.com/ hpc/
- [22] J. K. Zao, T. Gan, C. You, C. Chung, Y. Wang, S. J. Mndez, T. Mullen, C. Yu, C. Kothe, C. Hsiao, and al., “Pervasive brain monitoring and data sharing based on multi-tier distributed computing and linked data technology,” Frontiers in human neuroscience, vol. 8, 2014.
- [23] B. H. Brinkmann, M. R. Bower, K. A. Stengel, G. A. Worrell, and M. Stead, “Large-scale electrophysiology: acquisition, compression, encryption, and storage of big data,” Journal of neuroscience methods, vol. 180, no. 1, pp. 185–192, 2009.
- [24] M.-P. Hosseini, M. R. Nazem-Zadeh, F. Mahmoudi, H. Ying, and H. Soltanian-Zadeh, “Support vector machine with nonlinear-kernel optimization for lateralization of epileptogenic hippocampus in mr images,” in Proc. of IEEE International Conference of Engineering in Medicine and Biology Society (EMBC), 2014, pp. 1047–1050.
- [25] M.-R. Nazem-Zadeh, J. M. Schwalb, H. Bagher-Ebadian, F. Mahmoudi, M.-P. Hosseini, K. Jafari-Khouzani, K. V. Elisevich, and H. SoltanianZadeh, “Lateralization of temporal lobe epilepsy by imaging-based response-driven multinomial multivariate models,” in Proc. of IEEE International Conference of Engineering in Medicine and Biology Society (EMBC). IEEE, 2014, pp. 5595–5598.
- [26] M.-P. Hosseini, M. R. Nazem-Zadeh, D. Pompili, K. Jafari-Khouzani, K. Elisevich, and H. Soltanian-Zadeh, “Automatic and manual segmentation of hippocampus in epileptic patients mri,” in 6th annual New York Medical Imaging Informatics Symposium (NYMIIS). Staten Island University Hospital, NY, USA, 2015.
- [27] M.-P. Hosseini, M.-R. Nazem-Zadeh, D. Pompili, K. Jafari-Khouzani, K. Elisevich, and H. Soltanian-Zadeh, “Comparative performance evaluation of automated segmentation methods of hippocampus from magnetic resonance images of temporal lobe epilepsy patients,” Medical Physics, vol. 43, no. 1, pp. 538–553, 2016.
- [28] J. Ge and G. Zhang, “Novel images extraction model using improved delay vector variance feature extraction and multi-kernel neural network for eeg detection and prediction,” Technology and Health Care, vol. 23, no. s1, pp. S151–S155, 2015.

