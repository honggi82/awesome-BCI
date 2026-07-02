# arXiv:2105.14278v3[cs.LG]5Sep2022

An overview of deep learning techniques for epileptic seizures detection and prediction based on neuroimaging modalities: Methods, challenges, and future works

Afshin Shoeibia,∗, Parisa Moridianb, Marjane Khodatarsc, Navid Ghassemid, Mahboobeh Jafarie, Roohallah Alizadehsanif, Yinan Kongg, Juan Manuel Gorriza, Javier Ramı´rezh, Abbas Khosravif, Saeid Nahavandif, U. Rajendra Acharyai,j,k

aData Science and Computational Intelligence Institute, University of Granada, Spain. bFaculty of Engineering, Science and Research Branch, Islamic Azad University, Tehran, Iran. cDepartment of Medical Engineering, Mashhad Branch, Islamic Azad University, Mashhad, Iran. dComputer Engineering department, Ferdowsi University of Mashhad, Mashhad, Iran. eElectrical and Computer Engineering Faculty, Semnan University, Semnan, Iran. fIntelligent for Systems Research and Innovation (IISRI), Deakin University, Victoria 3217, Australia. gSchool of Engineering, Macquarie University, Sydney 2109, Australia. hDepartment of Signal Theory, Networking and Communications, Universidad de Granada, Spain. iNgee Ann Polytechnic, Singapore 599489, Singapore. jDept. of Biomedical Informatics and Medical Engineering, Asia University, Taichung, Taiwan. kDept. of Biomedical Engineering, School of Science and Technology, Singapore University of Social Sciences, Singapore.

## Abstract

Epilepsy is a disorder of the brain denoted by frequent seizures. The symptoms of seizure include confusion, abnormal staring, and rapid, sudden, and uncontrollable hand movements. Epileptic seizure detection methods involve neurological exams, blood tests, neuropsychological tests, and neuroimaging modalities. Among these, neuroimaging modalities have received considerable attention from specialist physicians. One method to facilitate the accurate and fast diagnosis of epileptic seizures is to employ computer-aided diagnosis systems

∗Corresponding author

Email addresses: afshin.shoeibi@gmail.com (Afshin Shoeibi ), parisamoridian@yahoo.com (Parisa Moridian), khodatars1marjane@gmail.com (Marjane Khodatars), navidghassemi@mail.um.ac.ir (Navid Ghassemi), mahbube.jafari@yahoo.com (Mahboobeh Jafari), ralizadehsani@deakin.edu.au (Roohallah Alizadehsani), yinan.kong@mq.edu.au (Yinan Kong), gorriz@ugr.es (Juan Manuel Gorriz), javierrp@ugr.es (Javier Ramı´rez), abbas.khosravi@deakin.edu.au (Abbas Khosravi), saeid.nahavandi@deakin.edu.au (Saeid Nahavandi), Rajendra_Udyavara_ACHARYA@np.edu.sg (U. Rajendra Acharya)

Preprint submitted to Elsevier September 7, 2022

(CADS) based on deep learning (DL) and neuroimaging modalities. This paper has studied a comprehensive overview of DL methods employed for epileptic seizures detection and prediction using neuroimaging modalities. First, DLbased CADS for epileptic seizures detection and prediction using neuroimaging modalities are discussed. Also, descriptions of various datasets, preprocessing algorithms, and DL models which have been used for epileptic seizures detection and prediction have been included. Then, research on rehabilitation tools has been presented, which contains brain-computer interface (BCI), cloud computing, internet of things (IoT), hardware implementation of DL techniques on ﬁeld-programmable gate array (FPGA), etc. In the discussion section, a comparison has been carried out between research on epileptic seizure detection and prediction. The challenges in epileptic seizures detection and prediction using neuroimaging modalities and DL models have been described. In addition, possible directions for future works in this ﬁeld, speciﬁcally for solving challenges in datasets, DL, rehabilitation, and hardware models, have been proposed. The ﬁnal section is dedicated to the conclusion which summarizes the signiﬁcant ﬁndings of the paper.

Keywords: Epileptic Seizures, Neuroimaging, Deep Learning, Detection, Prediction, Rehabilitation, Cloud-Computing.

## 1. Introduction

Epileptic seizures are a non-communicable disease and are one of the most prevalent disorders of the nervous system. Epileptic disorders usually occur with sudden attacks that result from abnormal activity of the cortical or membrane nerve in the brain (Iasemidis, 2003; Shoeb and Guttag, 2010; Tzallas et al., 2012; Subasi, 2005; Shoeb, 2009a). More than 60 million people worldwide have various types of epileptic seizures and suﬀer from them (Pachori and Bajaj, 2011; Siddiqui et al., 2020; Wong and Kuhlmann, 2020). Figure 1 displays the number of people with epileptic seizures in various parts of the world (Abramovici and Bagi´c, 2016). As shown in the ﬁgure, the number of people with this type of neurological disorder is greater in underdeveloped countries than in other countries (Abramovici and Bagic´, 2016).

Epilepsy is a rapid and early abnormality in the brain’s electrical activity,

[Figure 1]

- Figure 1: Graph of the number of people with epileptic seizures worldwide (Abramovici and Bagi´c, 2016).

disrupting part or all of the human body (Duncan et al., 2006; Noachtar and Peters, 2009). Medical researchers have divided epileptic seizures into three categories: generalized (Hussein et al., 2018a; Gloor and Fariello, 1988), focal (Nair et al., 2020; Frauscher and Gotman, 2019), and epilepsy with unknown onset (Ngoh and Parker, 2017), each of which has various types.

General epilepsy involves the whole brain and causes disruption of the activity of all neurons in the brain, eventually may lead to the impairment of all parts of the brain (Cerulli Irelli et al., 2020; Liu et al., 2017; Clarke et al., 2019). In partial epilepsy, a small group of neurons form a focal epilepsy and are conﬁned to a hemisphere of the brain. 60% of patients with epilepsy have focal seizures that are mostly drug-resistant (Misi¯unas et al., 2019; Boran et al., 2019; Pellegrino et al., 2018). The classiﬁcation of epileptic seizure types is shown in Figure 2. In this ﬁgure, the classiﬁcation of epileptic seizures before 2011 is depicted in darker color, and the classiﬁcation of epileptic seizures from 2016 onwards is highlighted in lighter color. More information is available in reference (Ngoh and Parker, 2017).

People with epileptic seizures may sometimes experience severe psychological trauma due to embarrassment and lack of proper social status (Sharma

[Figure 2]

- Figure 2: Showing diﬀerent types of general and focal epileptic seizures (Ngoh and Parker, 2017).

and Pachori, 2015; Gupta et al., 2020). Given the above, accurate and rapid diagnosis of these neurological disorders in the early stages is crucially pivotal.

Specialist physicians usually use functional and structural neuroimaging techniques to diagnose epileptic seizures. Electroencephalogram (EEG) (Yuan

- et al., 2018a; Fan and Chou, 2018), functional magnetic resonance imaging (fMRI) (Vaughan and Jackson, 2020; Garner et al., 2019), magnetoencephalography (MEG) (Colon et al., 2018; Rampp et al., 2019), electrocorticography (ECoG) (Mohammadpoory et al., 2019; Siddiqui et al., 2019), functional nearinfrared spectroscopy (fNIRS) (Rosas-Romero et al., 2019; Guevara et al., 2020), positron emission tomography (PET) (Oldan et al., 2018; Wang et al., 2019), and SPECT (El Tahry et al., 2018) are the most substantial functional neuroimaging modalities. In contrast, structural MRI (sMRI) (Ru¨ber et al., 2018; Xu et al., 2020b) and diﬀusion tensor imaging (DTI) (Bao et al., 2018; Chapman et al., 2005) are in the category of structural neuroimaging modalities. In

### ﬁgure 3, neuroimaging modalities for epileptic seizures detection are described.

[Figure 3]

[Figure 4]

(a) (b)

Figure 3: Neuroimaging modalities for epileptic seizures detection.

As shown in Figure 3, structural neuroimaging modalities include sMRI and DTI approaches. By using the sMRI modality, structural abnormalities and brain lesions caused by epileptic seizures can be identiﬁed (Woermann and Vollmar, 2009; Bell et al., 2009). Additionally, this modality can be used to identify the anatomical zone of the epileptogenic region that is responsible for the seizure, which is a pivotally signiﬁcant step for presurgical evaluations of epilepsy (Woermann and Vollmar, 2009; Bell et al., 2009). sMRI is also employed after surgery to evaluate the success or failure of the epileptic region removal and to assess the need for reoperation (Woermann and Vollmar, 2009; Bell et al., 2009). Disadvantages of sMRI include its widespread unavailability, high cost, and the necessity for long-term scans.

The DTI modality provides information on the structural anatomy of the white matter tracts and makes it possible to investigate the microstructural status of the white matter. Although the advantages of applying DTI in the diagnosis of the lesions for epilepsy are still being examined, modeling and reconstructing hidden pathways in white matter is of utmost importance as a presurgical evaluation step (Zhang et al., 2020d).

In EEG modality, the measurement of voltage ﬂuctuations produced by the ionic current of neurons in the brain is performed, indicating the bioelectric activity of the brain and containing the physiological information of people with

epileptic seizures (Acharya et al., 2013; Sharmila, 2018). The investigations reviewed in this paper demonstrates the eﬀectiveness of EEG modality performance in diagnosing epileptic seizures. EEG incorporates two methods of non-invasive scalp (sEEG) (Saab and Gotman, 2005; Fergus et al., 2015) and intracranial (IEEG) recording (Liu et al., 2012; Aarabi et al., 2009). The sEEG method is widely used by specialist physicians and neurologists compared to IEEG due to its lower risks and more straightforward recording. Additionally, considering that these signal recordings are economically inexpensive and the fact that the frequency and rhythm of brain activity vary during seizures, EEG has become one of the foremost epileptic seizures diagnostic methods (Birjandtalab et al., 2017; Weng and Khorasani, 1996). Compared to EEG, ECoG, fNIRS, and MEG functional modalities are less eﬀective in diagnosing epileptic seizures.

fMRI modality is another neuroimaging technique for epileptic seizures detection and includes two methods based on task (T-fMRI) (Gaillard et al., 2002) and resting state (rs-fMRI) (Centeno and Carmichael, 2014). fMRI is adapted to detect changes in regional blood ﬂow and metabolism due to the activation of brain regions (Gaillard et al., 2002; Centeno and Carmichael, 2014). One of the fMRI applications in epilepsy is identifying ictal and interictal phenomena given rise to the localization of the focal seizures (Gaillard et al., 2002; Centeno and Carmichael, 2014). During seizures, brain function changes in the epileptogenic region, which can be detected using fMRI (Gaillard et al., 2002; Centeno and Carmichael, 2014). fMRI can also be exploited to assess brain function before surgery in patients with drug-resistant epilepsy (Gaillard et al., 2002; Centeno and Carmichael, 2014). One of the drawbacks of fMRI is that the patient has to be in the scanner for a long period to seizure occur and the scan to be completed.

Detecting epileptic seizures from neuroimaging modalities with all the beneﬁts that are sometimes challenging. Epileptic seizure detection using neuroimaging modalities requires a considerable amount of recording data in order for the specialist doctors to make the appropriate decisions. Big data analysis of neuroimaging modalities in most cases beget incorrect epileptic seizures diagnosis by physicians. This is due to eye fatigue when interpreting many structural or functional imaging modalities. Additionally, the presence of diverse noises

in neuroimaging modalities is another cause of misdiagnosis. In order to conquer these dilemmas, CADS for epileptic seizures detection using neuroimaging modalities and AI are of considerable help to specialists in the epileptic seizures detection ﬁeld.

So far, many research works have been conducted to diagnose epileptic seizures using AI. Until quite a few years ago, most examinations were performed in the ﬁeld of conventional machine learning (Abbasi and Goldenholz, 2019; Rasheed et al., 2020). In traditional machine learning, the selection of the feature extraction, reduction and classiﬁcation techniques is dependent on the characteristics of the data (Dey, 2016; Naik et al., 2020). However, in DL approaches, all these steps are fulﬁlled via integrated layers and automatically (Dash et al., 2020; Goodfellow et al., 2016). Various DL methods have promptly received a tremendous amount of attention from numerous experts in the brain signal processing domain (Wainberg et al., 2018). This has made the diagnosis of epileptic seizures based on functional and structural brain modalities along with DL techniques one of the most novel areas of research. In this paper, a complete review of conducted research in the epileptic seizures ﬁeld from neuroimaging modalities along with DL methods, along with challenges and future work in this ﬁeld has been presented.

In order to search for papers in the scope of diagnosis of epileptic seizures, various citation databases such as IEEE Xplore, ScienceDirect, SpringerLink, and Wiley have been exploited. In addition, Google Scholar has been used to ﬁnd papers with the keywords ”Epileptic Seizure,” ”EEG,” ”fMRI,” ”ECoG’, ”MEG,” ”fNIRS,” ”MRI,” ”PET” and ”Deep Learning.” The latest articles were reviewed by the authors on December 30th, 2020. The number of papers accepted each year in diﬀerent citation sites for the diagnosis of epileptic seizures is illustrated in Figure 4.

In the following, the outline of this investigation is introduced. The second section concisely presents the DL networks exploited in diagnosing epileptic seizures. Recent CADS for epileptic seizures using DL techniques are examined in Section three. Several research works in the ﬁeld of rehabilitation systems, cloud computing, and diagnostic epilepsy procedures using non-neural modalities are presented in the fourth section. The discussion is introduced in Section

[Figure 5]

Figure 4: Number of papers published for automated detection of epileptic seizures using DL techniques.

ﬁve. In the sixth section, the challenges in diagnosing epileptic seizures are fully described. Finally, conclusions and recommendations for future work are provided in the seventh section.

## 2. Epileptic Seizures Detection Using DL Techniques

In this section, DL networks used in the diagnosis of epileptic seizures are presented. Convolutional neural networks (CNNs) are the ﬁrst category of DL architectures involving a variety of one-dimensional (1D), two-dimensional (2D), and three-dimensional (3D) models (Goodfellow et al., 2016; Sadeghi et al., 2021). These networks follow supervised learning and have three main layers: convolutional, pooling, and fully connected (FC) layers (Goodfellow et al., 2016). Recurrent neural networks (RNNs) are another paradigm of DL networks that are based on supervised learning widely applied in time series tasks (Goodfellow et al., 2016; Shoeibi et al., 2020). Autoencoders (AEs) models (Goodfellow et al., 2016; Burda et al., 2015) and deep belief networks (DBNs) (Goodfellow et al., 2016; Hinton, 2009) are other types of DL networks based on unsupervised learning. In addition to these models, improved methods from CNN named generative adversarial networks (GANs) (Goodfellow et al., 2014) architectures have been proposed for various applications that are based on unsupervised learning. It should be pointed out that generative adversarial networks (GANs)

architectures are adopted as supervised techniques in some issues (Goodfellow et al., 2014; Yi et al., 2019; Alizadehsani et al., 2021; Ghassemi et al., 2020). CNN-RNN and CNN-AE are two other categories of DL systems created by combining two diﬀerent architectures (Chen et al., 2017a). The CNN-RNN and CNN-AE architectures follow supervised and unsupervised learning, respectively (Keren and Schuller, 2016). Details of the types of DL networks in the diagnosis of epileptic seizures are manifested in Figure 5.

[Figure 6]

Figure 5: Illustration of various DL methods used for epileptic seizures detection.

## 3. CAD Based on DL techniques for Epileptic Seizures using Neuroimaging Modalities

Diagnosis of epileptic seizures from functional and structural neuroimaging modalities of the brain along with AI algorithms has a long history. Until recently, the diagnosis of epileptic seizures using CADS was based on conventional machine learning techniques that have been the subject of much research (Paul, 2018; Boonyakitanont et al., 2020a; Dhull et al., 2021; Mei et al., 2018). The most signiﬁcant weaknesses of these systems were the process of selecting the best feature extraction and dimensional reduction algorithms (feature selection or reduction) using trial and error that required a considerable amount of knowledge in the AI ﬁelds (Mohammadpoor et al., 2016). To resolve these issues, from

- 2016 onwards, DL methods in CADS for epileptic seizures detection were considered and quickly replaced the conventional machine learning approaches. In

### CADS based-DL, the feature extraction and selection steps are accomplished entirely automatically. The CADS for epileptic seizures detection based on DL techniques are represented in ﬁgure 6.

[Figure 7]

Figure 6: Illustration of block diagram for epileptic seizures detection using DL methods.

According to ﬁgure 6, a variety of structural and functional neuroimaging modalities are ﬁrst considered as DL input. In the following, low-level and high-level preprocessing methods are applied to the input data. Then, feature extraction up to classiﬁcation steps are performed by the desired DL networks (DL networks for epileptic seizures detection research papers are displayed in Appendix A). Finally, various evaluation parameters such as accuracy, sensitivity, and precision are calculated.

- 3.1. Epileptic Seizures Datasets In this section, the most notable datasets on diagnosing epileptic seizures are

reviewed, all of which are freely accessible. Without proper datasets, developing accurate and robust CADS is not possible. Several EEG datasets and an ECoG dataset are currently available to researchers freely; however, datasets on other neuroimaging modalities such as MRI have not yet been made freely available. Multiple EEG datasets, namely Freiburg (Ihle et al., 2012), CHB-MIT (Shoeb, 2009b), Kaggle (George et al., 2020), Bonn (Andrzejak et al., 2001), Flint-Hills (Assi et al., 2017), Bern-Barcelona (Andrzejak et al., 2012), Hauz Khas (Assi et al., 2017), and Zenodo (Stevenson et al., 2019) are the main ones for developing automatic systems for epileptic seizure detection. The signals forming each datapoint of these datasets are recorded either intracranial or from the scalp of humans or animals. Table 1 provides the supplementary information on each dataset, and also, the types of EEG datasets for epileptic seizures diagnosis using DL are listed in table 2.

Table 1: List of popular epileptic seizure datasets.

|Dataset|Number of Patient<br><br>|Number of Seizures<br><br>|Recording<br><br>|Total Duration (hour)|Sampling Frequency (Hz)|
|---|---|---|---|---|---|
|Flint-Hills (Assi et al., 2017)|10<br><br>|59<br><br>|Continues intracranial ling term ECoG|1419<br><br>|249|
|Hauz Khas (Assi et al., 2017)<br><br>|10|NA<br><br>|Scalp EEG (sEEG)<br><br>|NA|200|
|Freiburg (Ihle et al., 2012)<br><br>|21|87<br><br>|Intracranial Electroencephalography (IEEG)|708<br><br>|256|
|CHB-MIT (Shoeb, 2009b)<br><br>|22<br><br>|163<br><br>|sEEG<br><br>|844|256|
|Kaggle (George et al., 2020)<br><br>|5 Dogs 2 Patients<br><br>|48|IEEG|622<br><br>|400 5000<br><br>|
|Bonn (Andrzejak et al., 2001)<br><br>|10|NA<br><br>|Surface and IEEG<br><br>|39m|173.61|
|Bern Barcelona (Andrzejak et al., 2012)|5<br><br>|3750<br><br>|IEEG|83|512|
|Zenodo (Stevenson et al., 2019)|79 Neonatal<br><br>|460<br><br>|sEEG|74m<br><br>|256|

- 3.2. Preprocessing

- 3.2.1. EEG Preprocessing Preprocessing is the ﬁrst step in DL-based CADS for epileptic seizures de-

tection. The presence of diﬀerent artifacts in EEG signals always poses a severe challenge to physicians and neurologists in accurately diagnosing epileptic seizures. Artifacts from eye blinks, eye movements, muscle expansion and contraction, and municipal electricity noise are among the most important EEG data noises that should be eliminated from the signals in the preprocessing step (Shoka et al., 2019; Kim, 2018; Peng, 2019; Jiang et al., 2019b). In some cases, the presence of multiple artifacts begets loss of EEG signals’ substantial information between various noises and makes it challenging to diagnose epileptic seizures. EEG signal preprocessing in the diagnosis of epileptic seizures is divided into two types of low-level and high-level approaches, which are explained following. Table 2 shows the low-level and high-level preprocessing techniques of EEG signals in epileptic diagnostic research.

## A. Low Level EEG Preprocessing

In this section, low-level preprocessing methods are presented in the DLbased CADS for epileptic seizure detection. Low-level preprocessing in EEG signals involves noise removal, normalization, down-sampling, and segmenta-

tion. In order to remove noise from EEG signals, various types of low-pass, high-pass, and band-pass based Butterworth and or Chebyshev ﬁlters with different orders are widely employed (these ﬁlters are of ﬁnite impulse response (FIR) or Inﬁnite impulse response (IIR) types) (Gao et al., 2009; Lai et al., 2018; Patro and Sahu, 2015). Raw EEG signals have variable voltage amplitude degrading the eﬃciency of CADS in diagnosing epileptic seizures. To obviate this problem, it is recommended to utilize diﬀerent normalization methods such as Z-Score (Sayem et al., 2021). Storing and processing EEG signals requires a lot of memory space. By using down-sampling, EEG signals sampling frequency is decreased by half, which halves the storage space of EEG signals. Windowing or segmentation of EEG signals is the last part of low-level preprocessing. Segmentation assists in decomposing EEG data into more detailed sections to extract more signiﬁcant information from each signal frame (Tuncer

- et al., 2020). B. High Level EEG Preprocessing High-level preprocessing techniques play a pivotal role in enhancing the eﬃ-

ciency of CADS in diagnosing epileptic seizures. In this section, Data augmentation (DA) models are stated as the ﬁrst category of high-level preprocessing (Lashgari et al., 2020; Hartmann et al., 2018). The deﬁciency of EEG signals usually causes overﬁtting of DL networks during training, and the exploiting of DA techniques is a proper approach to address this problem. Discrete wavelet transform (DWT) (Ocak, 2009), continues wavelet transform (CWT) (Abibullaev et al., 2010), fast Fourier transform (FFT) (Polat and Gu¨nes¸, 2007), and empirical mode decomposition (EMD) (Alam and Bhuiyan, 2013) are other highlevel preprocessing techniques employed to eliminate noise and extract meaningful frequency bands from EEG signals. In addition, some improved FFT techniques such as short-time Fourier transform (STFT) to transform EEG signals to 2D images for application to CNNs have been investigated in research (Samiee et al., 2014). Also, some studies have selected independent component analysis (ICA)-based techniques to preprocess the EEG signals of epileptic seizures and have achieved satisfactory results (LeVan et al., 2006). Feature extraction procedures have also been considered in research as a crucial step in high-level preprocessing (Shoeibi et al., 2021).

C. Medical Imaging Modalities Preprocessing Medical imaging modalities are another method of diagnosing epileptic seizures

that possesses a special place among specialist physicians. In imaging techniques, applying preprocessing techniques is of great signiﬁcance. According to Table 3, epileptic seizure detection using MRI modalities is more signiﬁcant than other techniques. MRI neuroimaging modalities contain structural (sMRI) and functional (fMRI) techniques (Khodatars et al., 2020a). In sMRI modalities, the most important low-level preprocessing techniques include denoising, inhomogeneity correction, brain extraction, registration, intensity standardization, and re-orientation (Manj´n, 2017; Park et al., 2019). Also, slice timing correction, motion correction, normalization, smoothing, and ﬁltering are the most important low-level fMRI preprocessing methods (Jaber et al., 2019; Behroozi et al.,

- 2011). Some of the high-level preprocessing methods that have been surveyed in investigations for sMRI and fMRI modalities are segmentation (Makropoulos et al., 2018) and functional connectivity matrix (FCM) (Luo et al., 2011), respectively. Other research has focused on using PET imaging modality for diagnosis (Jiang et al., 2019a; Shiri et al., 2019). ROI, normalization, Ordered subset expectation maximization (OSEM), and down-sampling are some of the PET modality preprocessing methods (Jiang et al., 2019a; Shiri et al., 2019).

D. Other Modalities Preprocessing fNIRS and ECoG are two other modalities for functional neuroimaging of

the brain employed by researchers for epileptic seizures detection (Modir et al.,

- 2017; Sirpal et al., 2019; Chen et al., 2017b). Essential preprocessing steps in these modalities are similar to those of EEG signals and include noise reduction, normalization, and windowing of signals.

- 3.2.2. Review of Deep Learning Techniques In recent years, with the increased availability of large datasets, methodolo-

gies rooted in DL techniques are poised for making a signiﬁcant improvement in the diagnosis of various neurological disorders, including epileptic seizures. The DL-based CAD systems enable physicians to make better-informed decisions based on the recorded patient neuroimaging modalities. Figure 5 illustrates different types of DL architecture. It shows that CNNs (Goodfellow et al., 2016), GANs (Goodfellow et al., 2014), RNNs (Goodfellow et al., 2016), AEs (Good-

fellow et al., 2016), DBNs (Hinton, 2009), CNN-AE (Chen et al., 2017a), and CNN-RNN (Keren and Schuller, 2016) are the main DL architectures used for epileptic seizures detection. Among those, 2D-CNN and 1D-CNN are the most widely used DL architecture in the ﬁeld of epileptic seizures (Tables 2 and 3). This is due to the impressive achievements of CNNs architectures in other ﬁelds, including biomedical signal processing and medical imaging. In the rest of this section, we review the major DL network architectures and their variants.

## A. 1D and 2D-CNNs

The idea of using neural net like algorithms has been around for decades, yet many limitations have stopped them from being useful in machine learning. With the famous AlexNet paper (Goodfellow et al., 2016), neural nets have resurfaced once again in the past decade. Adding some knowledge to the network structure, i.e., the fact that patterns are presented in spatial localities, led to convolutional layers, and by ﬁxing the convolutional ﬁlters, the decrement in parameters made it possible for networks to train properly (Goodfellow et al., 2016; Khodatars et al., 2020b; Sharifrazi et al., 2021). 2D-CNNs have been widely used since their ﬁrst introduction, and their variant, 1D-CNNs, have also been applied vastly for signal processing tasks (Giudice et al., 2020; Bird

- et al., 2021). Figure 7 shows a general form of a 2D-CNN used for epileptic seizure detection.

[Figure 8]

Figure 7: A typical 1D-CNN for epileptic seizure detection.

## B. Generative Adversarial Networks (GANs)

In 2014, Goodfellow et al. (Goodfellow et al., 2016) revolutionized the ﬁeld of generative models by introducing Generative Adversarial Nets (GANs). The main contribution of GANs is their capability of generating high-quality images

similar to the training dataset; GANs have been applied to signal (Hazra and Byun, 2020; Abdelfattah et al., 2018), image (Schlegl et al., 2019; Yang et al., 2017), and many other data types in the past years (Ghassemi et al., 2020). Given the quality of generated data, GANs can be used for data augmentation and model pre-training (Goodfellow et al., 2016), helping to overcome one of the main issues in biomedical machine learning, the limited size of datasets. The general GAN architecture is shown in Figure 8.

[Figure 9]

Figure 8: A typical GAN architecture for epileptic seizure detection.

## C. Pre-Train Networks

Deep neural nets usually have a tremendous amount of parameters; thus, they require enormous datasets for proper training. This is generally challenging in biomedical data processing due to small dataset sizes. However, one method used commonly to overcome this issue is to ﬁne-tune previously trained networks. In this method, ﬁrst, a DNN is trained on a big dataset, such as ImageNet, then the last layer, classiﬁer, is removed. After that, as illustrated in ﬁgure 9, its weights are ﬁne-tuned using the primary dataset, or it is merely used as a feature extractor (Goodfellow et al., 2016).

[Figure 10]

Figure 9: A typical deep pre-train network for epileptic seizure detection.

AlexNet

As the ﬁrst famous DL network, AlexNet is still the center of attention in many studies (Iandola et al., 2016). In this network, two new perspectives dropout, and local response normalization (LRN), are used to help the network learn better. Dropout is applied in two FC layers employed in the end. On the other hand, LRN, utilized in convolutional layers, can be employed in two diﬀerent ways: Firstly, applying single channel or feature maps, where the same feature map normalizes depending on the neighborhood values and selects the N×N patch. Secondly, LRN can be exploited across the channels or feature maps (Goodfellow et al., 2016; Iandola et al., 2016).

VGG

Created by Visual Geometry Group in 2014, VGG is one of the pioneers of deep neural net structures; however, this famous structure is still extensively used and popular among researchers (Wang et al., 2015). Many argue that this is due to its straight forward design and also ease of applying this network for transfer learning (Wang et al., 2015). Two variants of VGG are mostly used for transfer learning, namely, VGG-16 and VGG-19 (number stands for the number of layers); also, they are applied in various ﬁelds, ranging from face recognition (Sun et al., 2015) to brain tumor classiﬁcation (Sajjad et al., 2019). GoogleNet

Diﬀerent receptive ﬁelds, generated by various kernel sizes, form layers called ”Inception layers,” which are the building block of these networks. Operations generated by these receptive ﬁelds ﬁnd correlation patterns in the novel feature map stack (Ballester and Araujo, 2016). In GoogLeNet, a stack of inception layers is used to enhance recognition accuracy. The diﬀerence between the ﬁnal inception layer and the naı¨ve inception layer is the inclusion of 1x1 convolution kernels, which performs a dimensionality reduction, consequently reducing the computational cost. Another idea in GoogleNet is the gradient injection, which aims to overcome the gradient vanishing problem. GoogLeNet comprises a total of 22 layers that is greater than any previous network. However, GoogLeNet uses much fewer parameters compared to its predecessors VGG or AlexNet (Ballester and Araujo, 2016; Goodfellow et al., 2016).

ResNet

The idea behind ResNet was to overcome the issue of vanishing gradient by utilizing skip connections between blocks. This allowed the Residual nets to go deeper than regular networks; many varieties of these networks, with various sizes, such as 34, 50, and 152 have been created and applied in many tasks (Targ

- et al., 2016). ResNet’s main contribution was not the network or its state-ofthe-art performance, but the network’s building blocks, and similar blocks have been widely used in many other deep NN structures; as an example, Res2Net is an image segmentation network with a similar design to ResNet.

## D. 3D-CNN

To overcome this, 3D-CNN was introduced. In 2D-CNN, many well-known structures such as VGG and GoogLeNet are available as a great starting point to construct the new structure upon them. However, creating 3D-CNNs can be challenging, considering there are not many famous 3D-CNN structures (Zhao

- et al., 2019; Kwak et al., 2020). Nevertheless, designed and trained properly, 3D-CNNs can ﬁnd 3D patterns and achieve state-of-the-art performances. A typical 3D-CNN for epileptic seizure detection is shown in ﬁgure 10.

[Figure 11]

Figure 10: A typical 3D-CNN for epileptic seizure detection.

## E. Recurrent Neural Networks (RNNs)

Many data forms, such as signal, have embedded patterns that cannot be characterized by local or spatial patterns. To create a model suitable for these datasets, researchers have created recurrent neural nets that, as stressed by the name, use the same group of neurons with a recurring scheme to process these data properly. Few variants of these networks, such as LSTM (long short term memory) and GRU, are created to ﬁnd local and global patterns eﬃciently (Li et al., 2018; Hsu et al., 1990). The standard type of these networks is usually

used as a baseline for creating models on signal processing and time-dependent datasets (Khalifa et al., 2020; Zihlmann et al., 2017). However, a combination of these networks with convolutional layers is popular among researchers aiming to reach high performances with more complex models. A typical RNN for epileptic seizure detection is shown in ﬁgure 11.

[Figure 12]

Figure 11: A typical RNN for epileptic seizure detection.

## F. Deep Belief Networks (DBNs)

Restricted Boltzmann Machine (RBM), the building block of Deep Boltzmann Machine (DBM), is an undirected graphical model (Hinton, 2009). The unrestricted Boltzmann machines are also similar; however, they may also have connections between the hidden units. DBNs are unsupervised probabilistic hybrid generative DL models comprising of latent and stochastic variables in multiple layers (Hinton, 2009). Moreover, a variation of DBN is called Convolutional DBN (CDBN), which is more suitable for images and signals, as it uses the spatial information of data (Krizhevsky and Hinton, 2010).

## G. Autoencoders

AEs were one of the ﬁrst groups of neural networks with practical use in machine learning (Goodfellow et al., 2016). Even with new advancements in DL, AEs have never lost researchers’ attention and are widely used for dimensionality reduction and representation learning. The main idea behind AE is to map data to a smaller latent space and then back to the starting space with a minimum loss, thus reaching a mechanism to preserve essential aspects of data while reducing its dimensionality. Nowadays, many variations of AEs have

been introduced with the goal of improving the base AE performance, such as stacked AE (SAE), denoising AE (DAE), and sparse AE (SpAE) (Sønderby et al., 2016; Bank et al., 2020; Holden et al., 2015). A typical AE for epileptic seizure detection is shown in ﬁgure 12.

[Figure 13]

Figure 12: A typical AE for epileptic seizure detection.

## H. CNN-RNN

To combine RNNs and CNNs, researchers usually use convolutional layers in the ﬁrst layers of the model to extract features and ﬁnd local patterns, and they feed the output of these layers to RNNs to use their superiority for global pattern recognition (Keren and Schuller, 2016). The reasoning behind the noble performances of these models is a two-fold. First, convolutional layers empirically ﬁnd local and spatial patterns considerably better than RNNs in signals. Second, adding convolutional layers allows RNN to see data with stride, hence ﬁnding more distanced patterns. By combining the output of convolutional layers and handcrafted features, CNN-RNNs are allowed to reach a state-of-the-art performance, in addition to learning a representation of data that overcomes handcrafted features’ deﬁciencies (Keren and Schuller, 2016). A typical CNN-RNN for epileptic seizure detection is shown in ﬁgure 13.

## I. CNN-AE

Convolutional Autoencoder, or CNN-AE, is a DL based model that uses superiorities of convolutional layers to learn a representation of input unsupervised (Chen et al., 2017a). Base AEs are not suitable for raw representation learning, i.e., learn a representation of data without any added knowledge. This is due to the large number of learnable parameters that stops the network from learning anything useful. However, using convolutional layers, parameters are

[Figure 14]

- Figure 13: A typical CNN-RNN for epileptic seizure detection.

reduced dramatically, and networks can be appropriately trained (Chen et al.,

- 2017a). A combination of this model with other ones, such as DAE, can lead to complex models with state-of-the-art performances (Li et al., 2015; Makhzani

- et al., 2015). A typical CNN-AE for epileptic seizure detection is shown in ﬁgure 14.

[Figure 15]

- Figure 14: A typical CNN-AE for epileptic seizure detection.

- 3.2.3. Other Neuroimaging Modalities for Epileptic Seizure Detection A. Medical Imaging In the medical imaging literature, many researchers have focused on the

application of fMRI, sMRI, and PET modalities for epileptic seizure detection using DL methods. sMRI and fMRI neuroimaging modalities are more popular than PET among physicians and neurologists for detecting epileptic seizures

(van Lanen et al., 2021; Ma et al., 2020). This has led to more research papers be conducted on fMRI and sMRI modalities for epileptic seizures detection. Therefore, we summarize the relevant works that leverage various PET and MRI-based modalities in table 3.

## B. EEG-fMRI

Multimodal neuroimaging techniques give physicians very detailed information about the type of neurological disorders and their location on the brain. As such, it is essential to use these modalities to identify the central location (focus) of epilepsy in the brain. EEG-fMRI is one of the best multimodal techniques for epileptic seizures detection (Gotman, 2008; Ebrahimzadeh et al., 2019). The modality of EEG-fMRI along with the ResNet network was investigated for epileptic seizures detection in (Hao et al., 2018). In the proposed ResNet architecture, the Softmax and Triplet functions are used for supervised classiﬁcation, achieving 84.40% speciﬁcity.

C. EEG - fNIRS fNIRS uses infrared waves to monitor changes in blood oxygen levels in

the brain, allowing imaging and analysis of active brain areas (Pouliot et al.,

- 2012). In this method, using special electrodes on the scalp, variations in oxyhemoglobin (HbO) and deoxy-hemoglobin (HbR) are measured, which can be helpful in diagnosing a variety of brain diseases. In (Mao et al., 2020), EEGfNIRS combination modalities have been employed to detect epileptic seizures. The proposed LSTM-based based approach, with a Softmax classiﬁer as the last layer, achieved 98.30% accuracy in their case study.

## D. ECoG

RaviPrakash et al. (RaviPrakash et al., 2020) introduced an algorithm based on DL for Electrocorticography based functional mapping (ECoG-FM) for eloquent language cortex identiﬁcation. ECoG-FM’s success rate is low compared to Electro-cortical Stimulation Mapping (ESM). The algorithm showed an improvement of 34% over the existing ECoG-FM method with an accuracy of approximately 89%. ECoG-FM method coupled with DL has the potential for state-of-the-art performances. This method can help the surgeons performing epilepsy surgery by removing the ESM hazards. Also, in part of the (Hosseini

- et al., 2017), an ECoG modality has been considered for the detection of epileptic

seizures. 2D-CNN and SVM were used for feature extraction and classiﬁcation steps, respectively.

## E. MEG

MEG is a functional neuroimaging technique used to evaluate and analyze the structure of the brain to diagnose a variety of brain disorders. Due to its high operational costs, it is only used in exceptional cases. (Zheng et al., 2019) Proposed a new technique, EMS-Net, for detecting epileptic spikes from MEG modality, with satisfactory results.

## 4. Rehabilitation Systems Based DL Techniques

In recent years, research in the ﬁeld of design and construction of rehabilitation systems aimed at assisting people with a variety of neurological disorders has advanced signiﬁcantly. Rehabilitation systems are of particular signiﬁcance to assist patients. The major objective of these systems is to achieve real and accessible tools for diﬀerent patients. These systems are important in two aspects: First, they continuously monitor the patient’s condition and, in the occurrence of disease, perform some necessary work to improve the disease. In the second case, there is another category of these systems that constantly report the patient’s vital signs to the specialist so that the patient is at lower risk of disease. In this section, various rehabilitation systems are presented to help patients with epileptic seizures. These tools include programs to diagnose epileptic seizures from non-medical modalities (Ahmedt-Aristizabal et al.,

- 2018a; Achilles et al., 2018), Brain Computer Interface (BCI) systems (Hosseini

- et al., 2016), Implantable (Kiral-Kornek et al., 2018), and Cloud-Computing (Singh and Malhotra, 2018; Ali et al., 2020; Amin et al., 2019; Alhussein et al.,

- 2018) are discussed below.

- 4.1. Non Neuroimaging Modality for Epileptic Seizure Detection In a study by Ahmedt et al. (Ahmedt-Aristizabal et al., 2018a), facial images

have been used to diagnose epileptic seizures. To collect the dataset, epileptic patients were monitored for 2 to 7 days, and eventually, 16 patients with MTLE were randomly selected from the general data set by default. The DL architecture in this investigation is CNN-RNN and, the results reveal that they have achieved promising results.

- 4.2. Brain Computer Interface BCI based on DL to detect epileptic seizures has been recommended in

Hosseini et al.’s study (Hosseini et al., 2016). In the proposed technique, SSAE and Softmax methods have been exploited to perform feature extraction and classiﬁcation steps, respectively. In this study, they achieved 94% accuracy.

- 4.3. Implantable Based DL Kiral-Kornek et al. (Kiral-Kornek et al., 2018) proposed an online and wear-

able system in the body for epileptic seizures detection based on DL. The proposed system has low power consumption, long life, and high reliability. In the proposed approach system, the DL method is trained to distinguish pre-ictal signals from ictal and has a sensitivity of 69%.

- 4.4. Cloud Computing Based DL for Epileptic Seizures Detection With the advancement of information technology, performing heavy compu-

tational tasks at diﬀerent times and places becomes a necessity. There is also a need for people to be able to easily fulﬁll their heavy computing tasks without owning expensive hardware and software. Cloud computing plays an important role in allowing users to process various data and store information outside of personal computers. The advantages of cloud computing have led to its accelerated application in various medical ﬁelds. An overview of cloud computing to help diagnose epileptic seizures is exhibited in Figure 15. In the epileptic seizure detection ﬁeld, research has been carried out using cloud computing, which we will describe below (Singh and Malhotra, 2018; Ali et al., 2020; Amin et al.,

- 2019; Alhussein et al., 2018; Muhammad et al., 2018).

- 4.4.1. Cloud System Design Based DL and Smartphone Singh et al. (Singh and Malhotra, 2018) developed a commercial product for

epileptic seizures detection, which involves user and cloud sections. The user section includes EEG headset, smartphone, WiFi system or, 4G network. The cloud segment also contains the dataset and the SAE algorithm for classifying EEG signals. EEG signals are recorded via a 14-channel Bluetooth headset and then transmitted to the patient’s smartphone. Then, Android-based software transmits the recorded data to the cloud via WiFi or 4G internet connection. If

[Figure 16]

Figure 15: Cloud computing in helping patients with epileptic seizures.

the output of the classiﬁer is pre-ictal, an alarm message containing the patient’s geographical location is sent by the alarm system to the patient’s telephone, family members’ telephone, and the nearest hospital.

- 4.4.2. Cloud System Based DL and Mobile Edge Computing Ali et al. (Ali et al., 2020) used the combination of DL with mobile edge

computing to detect epileptic seizures. The objective of Edge Computing is to lessen the communication load of the cloud server and the edge device, which is speciﬁcally the main focus of this article. The proposed design assumes that the data has already been recorded and provided to the edge device, which is mobile. Next, receiving the raw data by mobile phone, they are partially processed and then sent to the cloud. Other processes continue to epileptic seizures detection in the cloud, and then the result is sent to the mobile phone.

- 4.4.3. IoT Based Healthcare An IoT-based healthcare framework and DL to help patients with epileptic

seizures are introduced in (Amin et al., 2019; Alhussein et al., 2018). In (Amin et al., 2019), the function of two adopted cloud systems is employed, one of which sends EEG signals, and the other sends other vital information such as movements and emotions. With the cognitive module, the patient’s vital signs are supervised online and then fed to the CNN network input. Finally, patient status and EEG signal analysis results are shared with medical providers. In the recommended approach, emergency help is provided if the patient is in critical

condition.

- 4.4.4. Mobile Multimedia Framework In a study by Muhammad et al. (Muhammad et al., 2018), a technique based

on mobile multimedia healthcare was proposed to help patients with epileptic seizures. In the proposed method, DL and the CHB-MIT dataset are utilized to detect epileptic seizures. Finally, the algorithms adopted are implemented on a module. Experimental results show the achievement of 99.02% accuracy and 92.35% sensitivity parameters.

- 5. Discussion

Today, many people worldwide suﬀer from epileptic seizures, and their daily activities are faced with serious challenges. So far, numerous clinical and screening procedures have been proposed to treat and diagnose epileptic seizures. Among the screening methods, EEG, fMRI, sMRI, and PET modalities are more important for epileptic seizures detection for physicians than other techniques. Applying DL techniques and neuroimaging modalities are crucially signiﬁcant in epileptic seizure detection. In this paper, conducted researches on the diagnosis of epileptic seizures using DL methods are studied. Also, in the papers reviewed, practical applications in this ﬁeld have been mentioned.

Diagnosis of epileptic seizures based on EEG modalities as well as medical imaging techniques are summarized in Tables 2 and 3. These tables provide each research information, including dataset, modality, preprocessing techniques, DL network input, DL network, classiﬁcation algorithm, K-Fold evaluation, and ﬁnally, various evaluation parameters.

The most important datasets available used for diagnosing epileptic seizures are provided in Table 1. It is observable that the majority of them take advantage of EEG modalities. The total number of datasets utilized in epileptic seizure investigations is shown in Figure 16. As can be observed, the Bonn dataset is the most widely used by researchers. This is because this database is preprocessed and can be easily employed for research.

Diﬀerent neuroimaging modalities are applied to diagnose epileptic seizures. Detailed information on the types of neural modalities for diagnosing epilep-

[Figure 17]

- Figure 16: Number of studies published for epileptic seizures detection using diﬀerent datasets.

tic seizures is given in the diagram 17. According to diagram 17, the sEEG modality has dedicated to itself the highest use in the research. This is due to the non-invasive nature of the sEEG modality, which exposes patients to fewer risks. Moreover, according to Figure 17, IEEG modality is considered the second epileptic seizures detection approach.

Numerous tools have been proposed to implement a variety of DL architectures, the main objective of which is to facilitate the simulation of these networks. Matlab, Keras, TensorFlow, PyTorch, Caﬀe, and Theano are the most well-known tools for the implementation of DL networks (Peng et al., 2016; Nguyen et al., 2012). The number of times each DL tool is used for epileptic seizure detection is illustrated in Figure 18. The TensorFlow and Keras libraries are widely applied due to their continuous updating, high ﬂexibility, and ease of use in implementing CADS epileptic seizures.

In tables 2 and 3, the DL network types are discussed for epileptic seizures detection based on neuroimaging modalities. A variety of CNN models in various medical applications, especially the diagnosis of epileptic seizures, have reached promising results. Figure 19 display the total number of DL techniques for epileptic seizures detection.

Also, ﬁgure 19 shows the number of annual researches on the utilization of DL networks for epileptic seizures detection. Based on Figure 19, the researchers

[Figure 18]

- Figure 17: Number of studies published for epileptic seizures detection using diﬀerent neuroimaging modalities.

have concentrated on diﬀerent models of 2D-CNN and 1D-CNN. CNN architectures discover local spatial dependencies well; thus, these networks can be used to extract the necessary patterns from various modalities, including EEG signals. Furthermore, the patterns that CNNs learn are unchanged from relocation, and on the other hand, they can well train the hierarchy of feature space. In this article, not only the type of DL network in each research is discussed, but also in the table 4, the implementation details of DL networks in each research are mentioned.

Classiﬁcation algorithms are the last part of the DL network. Figure 20 shows the number of classiﬁcation algorithms used in DL networks based on Tables 2 and 3. As can be seen, the Softmax algorithm (Zeng et al., 2014) is the most popular in DL applications as a classiﬁcation approach. Regarding the superiority of Softmax compared to other classiﬁers such as SVM (Noble, 2006), we can remark its easy derivability, which makes it possible to apply it in the backpropagation algorithm. Also, compared to gradient descent methods, such as exploiting Sigmoid for classiﬁcation purposes, Softmax provides better performance due to the weights normalization between diﬀerent classes.

[Figure 19]

- Figure 18: Number of DL tools used for epileptic seizures detection based on the published papers.

## 6. Challenges

In this section, the challenges in epileptic seizures diagnosis using DL techniques have been described. The most important challenges concerning datasets, DL methods, and hardware resources are explained in detail below.

Available datasets for diagnosing epileptic seizures are mostly EEG type. However, available datasets from other functional and structural neural modalities have not been provided for investigations until now. For example, the fNIRS modality is one of the most inexpensive and most accurate procedures to diagnose a variety of neurological disorders (Tak and Ye, 2014; Peng et al., 2014). The lack of available fNIRS datasets for the diagnosis of epileptic seizures has given rise to conﬁned research in this ﬁeld. Additionally, sMRI and fMRI modalities are recognized as some of the most signiﬁcant and accurate tools for diagnosing brain disorders (Del Gaizo et al., 2017; Bharath et al., 2019). So far, no dataset on sMRI or fMRI modalities has been made freely available to researchers for epileptic seizures detection. Multimodality techniques such as EEG-fMRI or EEG-fNIRS have been investigated in the diagnosis of mental and neural disorders and, noteworthy results have been achieved (Zijlmans et al., 2007; Kowalczyk et al., 2020; Peng et al., 2016; Nguyen et al., 2012). In

[Figure 20]

- Figure 19: Number of DL architectures used for epileptic seizures detection based on published papers.

order to diagnose epileptic seizures using multimodality approaches, insuﬃcient research has been performed, the main reason being the deﬁciency of available and free datasets.

Available EEG datasets commonly follow two approaches to distinguishing seizures from normal or when they occur. However, there are diﬀerent types of epileptic seizures, and diagnosing their type is a troublesome task for physicians. Therefore, contributing datasets with functional or structural neuronal modalities to diagnose diﬀerent types of epileptic seizures is profoundly felt.

Regarding the utilization of DL models for epileptic seizures detection, several challenges must be examined before implementing these models for clinical applications. The ﬁrst challenge of this category is the extensiveness and diﬀerences of seizure patterns in signals. This issue leads to collect very large datasets to make these models more robust to new patterns or a more feasible solution to apply few-shot learning techniques to improve these models’ robustness. Another challenge is to investigate the transferability of the model implemented on various datasets. Various studies have succeeded in achieving very high accuracy on particular datasets, but before adopting these models in real-world applications, their performance requires to be evaluated with a diﬀerent distribution of the training data. The ﬁnal challenge in this scope is the lack of

[Figure 21]

- Figure 20: Illustration of the number of various classiﬁer algorithms used in DL networks for automated detection of epileptic seizures.

networks with a dedicated structure for diagnosing epileptic seizures performing as a benchmark. In the image processing ﬁeld, networks such as VGG and AlexNet have served as benchmarks and, in addition to providing researchers with a highly eﬀective evaluation tool, allowing them to easily track their work to evolve and improve on previous work, while most of the networks used in this ﬁeld are modiﬁed derivatives of networks presented for ImageNet and not speciﬁcally designed to diagnose epileptic seizures.

The following challenges category refers to the presentation of rehabilitation systems in the diagnosis of epileptic seizures with the help of DL. Unfortunately, much concentration has not been carried out on designing rehabilitation systems like BCI. In some research papers, cloud computing technologies, IoT and, Healthcare have been studied to address the diﬃculties of patients with epileptic seizures using neuroimaging modalities. The most substantial research challenges in this ﬁeld are the deﬁciency of multimodality datasets for these systems’ better performance.

Furthermore, dedicated hardware design platforms for this research have not been yielded till then, which is another challenge. To date, most researchers have developed the hardware implementation of conventional machine learning algorithms to detect epileptic seizures timely. This issue has led to these hardware

circuits can not be employed for epileptic seizures detection seriously. Hardware implementation of DL algorithms to diagnose epileptic seizures can give specialist physicians the hope that they can accurately and real-time diagnose epileptic seizures and their type. Hardware implementation of DL algorithms on ﬁeld-programmable gate array (FPGA), application-speciﬁc integrated circuit (ASIC), etc. can address many diﬃculties and challenges for medical professionals. However, when designing hardware based on DL, a number of existing challenges can be addressed, such as reducing hardware resources, minimizing power consumption, and so on.

## 7. Conclusion and Future Works

Early detection of epileptic seizures is of particular importance to specialist physicians, and research in this ﬁeld has grown signiﬁcantly in recent years. In this paper, a comprehensive review of the diagnosis of epileptic seizures using neuroimaging modalities coupled with DL methods has been performed. In the discussion section, it was observed that sEEG datasets are most applied in epileptic seizures detection. In another section, it was perceived that diﬀerent models of DL have been employed to diagnose this type of neurological disorder, among which CNNs have the highest number of studies. In most investigations, small datasets have often been used to diagnose epileptic seizures alongside pretrain deep networks. To improve the performance of these DL networks, it is better to provide a comprehensive dataset of medical signals. This enhances the performance of pre-train deep networks for diagnosing epileptic seizures. Increasing the eﬃciency and accuracy of CAD systems in epileptic seizures detection is of particular signiﬁcance, but aforementioned, the data deﬁciency is a serious challenge. Another novel ﬁeld for research is applying Zero-Shot learning techniques, which can result in promising results for the implementation of real epileptic seizure detection systems.

In another part of the paper, the types of hardware and applied programs for detecting epileptic seizures were presented. Cloud Computing, IoT, Healthcare, and wearable implants have recently been introduced coupled with DL techniques to aid people with epileptic seizures, and it is encouraging that more applied research will be conducted in the near future. Lack of adequate hard-

ware resources is another reason hardening the practical implementation of these systems. For future work, it is expected that CADS based on DL will be implemented on a variety of dedicated hardware such as FPGA and ASIC for epileptic seizures detection.

Responsive neurostimulation (RNS) and vagus nerve stimulation (VNS) diagnostic systems are a type of invasive implants that can be implanted in the human body and are programmed to detect and neutralize the onset of epileptic seizures (Fisher, 2012; Skarpaas et al., 2019). These systems still have open problems in accurately diagnosing epileptic seizures. Enhancing the accuracy of RNS and VNS based diagnosis and treatment systems based on DL techniques can be noteworthy as one of the future tasks.

Another procedure of diagnosis and prediction is from other vital human signals such as the heart. Designing and manufacturing invasive and non-invasive implants based on other vital signals of the human body along with DL methods is another recommendation for future work.

In addition to other future directions, the use of more sophisticated methods in deep neural networks can itself be a path for future works. The use of deep metric (Schroﬀ et al., 2015) methods to increase the informativeness of learned representations, few-shot learning (Sung et al., 2018) methods and scalable networks (Tan and Le, 2019) for small dataset tasks, and newer data augmentation methods such as simple copy-paste (Ghiasi et al., 2020) can all be investigated.

#### Table 2: Summary of DL methods employed for automated detection of epileptic seizures.

|Work|Dataset|Modality<br><br>|Preprocessing| |Input Network|Deep Tools<br><br>|Network<br><br>|K-fold|Classiﬁer<br><br>|Performance Criteria (%)| | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | |Low Level<br><br>|High Level| | | | | |ACC|Sens<br><br>|Spec|F1-S|
|(Antoniades et al., 2016)<br><br>|Clinical<br><br>|IEEG|Standard Preprocessing<br><br>|Spectrogram|2D Spectrograms<br><br>|NA|2D-CNN<br><br>|–|LR|87.51<br><br>|–<br><br>|–|–|
|(Qin et al., 2020b)|CHB-MIT|sEEG<br><br>|Segmentation|STFT<br><br>|2D Spectrograms|PyTorch<br><br>|2D-CNN<br><br>|–<br><br>|ELM<br><br>|95.65|95.85|–<br><br>|–|
|(Park et al., 2018)<br><br>|SNUH|sEEG|Segmentation, Filtering<br><br>|DA|Preprocessed Data<br><br>|NA<br><br>|1D with<br>2D-CNN<br><br><br>|–<br><br>|Sigmoid|90.58|89.20<br><br>|91.90|–<br><br>|
| |CHB-MIT|sEEG| | | | | | | | | | | |
|(Tjepkema-Cloostermans et al., 2018)|Clinical<br><br>|sEEG|Filtering, DownSampling|–|the preprocessed 2 s epochs<br><br>|Keras<br><br>|2D-CNN|–|Softmax|–|47.40<br><br>|98.00|–|
| | | | | | |Theano| | | | | | | |
|(Avcu et al., 2019)|Clinical|sEEG<br><br>|Down Sampling, ZNormalization|DA<br><br>|Preprocessed Data|Keras<br><br>|SeizNet|–|NA|–<br><br>|95.80|–<br><br>|–|
|(Zhan and Hu, 2020)<br><br>|Freiburg|IEEG<br><br>|–|Fourier Transform (FT), Wavelet Transform (DWT)<br><br>|Spectrograms, Time Domain Signal, and Time Frequency Signal<br><br>|NA|DCNN<br><br>|NA|Multi-view Fuzzy Clustering<br><br>|97.38|96.26|–<br><br>|–|
|(Nejedly et al., 2019)|Clinical|IEEG<br><br>|Z-Normalization|STFT<br><br>|Raw IEEG Signals|PyTorch<br><br>|CNN<br><br>|–<br><br>|Softmax|–<br><br>|79.00<br><br>|–|–|
| | | | | |Spectrogram Images| | | | | | | | |
|(Hossain et al., 2019)|CHB-MIT|sEEG<br><br>|–|Visualization<br><br>|Raw EEG as 2D Array|PyTorch<br><br>|2D-CNN<br><br>|–<br><br>|Softmax<br><br>|98.05|90|91.65<br><br>|–|
|(Mao et al., 2020)|UCI<br><br>|sEEG<br><br>|–|CWT|2D Scalograms|MATLAB<br><br>|2D-CNN|–|Softmax<br><br>|72.49<br><br>|–<br><br>|–<br><br>|–|
|(Zuo et al., 2019)|Clinical<br><br>|IEEG<br><br>|Filtering, Normalization<br><br>|Visualization|Input Images 4*1,024 Pixels in Size|NA<br><br>|2D-CNN|10<br><br>|Softmax<br><br>|87.65|83.23<br><br>|79.36|–|
| | | | | | | | | | |90.83|77.04|72.27<br><br>|–|
|(Asif et al., 2019)<br><br>|TUH<br><br>|sEEG|–<br><br>|DivSpec|3D Visual Representation<br><br>|PyTorch<br><br>|SeizureNet|5<br><br>|Softmax|–|–<br><br>|–|90|
|(Iesˇmantas and Alzbutas, 2020)<br><br>|TUH<br><br>|sEEG|Feature Extraction| |Pattern Matrices<br><br>|TensorFlow<br><br>|2D-CNN|10<br><br>|Softmax|74|68<br><br>|67|–|
|(Zeng et al., 2021)|Bonn<br><br>|sEEG and IEEG|Filtering, Segmentation using FNSW|Conversion Module (GRP Transformation)<br><br>|2D-GRPs|TensorFlow<br><br>|GRP-DNet<br><br>|10|Majority Voting|100<br><br>|–|–|–|
|(San-Segundo et al., 2019)|Bern Barcelona<br><br>|IEEG<br><br>|Filtering|EMD, FWT, FT<br><br>|Raw IEEG Signals|Keras<br><br>|2D-CNN<br><br>|5|Sigmoid<br><br>|99.80|–|–|–<br><br>|
| |Clinical|sEEG| | |IMFs| | | |Softmax<br><br>| | | | |
| | | | | |Wavelet Coefficients| | | | | | | | |
| | | | | |Module Values| | | | | | | | |
|(Sui et al., 2019)<br><br>|Bern Barcelona|IEEG|Z-Normalization<br><br>|STFT|2D Spectrograms<br><br>|TensorFlow<br><br>|2D-CNN<br><br>|10<br><br>|Softmax|91.80|–<br><br>|–|–|
|(Chatzichristos et al., 2020)<br><br>|TUH|sEEG<br><br>|Multi-Channel Subspace Filters|IC Label<br><br>|Raw EEG Signals|NA|Multiple Attention-Gated U-Net<br><br>|10<br><br>|Bi-LSTM + FC Layer<br><br>|–|–<br><br>|–<br><br>|–|
| | | | | |Subspace Filtering| | | | | | | | |
| | | | | |ICLabel| | | | | | | | |
|(Covert et al., 2019)|Clinical<br><br>|sEEG<br><br>|–<br><br>|STFT|2D Spectrograms|NA<br><br>|TGCN<br><br>|–<br><br>|Sigmoid|92.80<br><br>|–<br><br>|–|–|
|(Akut, 2019)|Bonn<br><br>|sEEG and IEEG<br><br>|–|DWT<br><br>|Wavelet Coefficients<br><br>|NA<br><br>|2D-CNN|–<br><br>|Sigmoid|100<br><br>|100<br><br>|100|–|

|(Tu¨rk and Ozerdem,¨ 2019)|Bonn|sEEG and IEEG<br><br>|–|CWT<br><br>|2D Scalograms|Keras<br><br>|2D-CNN|10|Softmax<br><br>|100|100|100<br><br>|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|(Liu and Woodson, 2019)|Bonn<br><br>|sEEG and IEEG|Filtering<br><br>|–|Black and White Plots of The Amplitude Scaled Wave Files<br><br>|MATLAB|2D-CNN|–<br><br>|Softmax|99.60<br><br>|–<br><br>|–|–|
|(Tian et al., 2019)<br><br>|CHB-MIT|sEEG<br><br>|Over Sampling Method|FFT, WPD|Time Domain<br><br>|MATLAB|2D-CNN<br><br>|5|MV-TSK-FS<br><br>|98.33|96.66|99.14<br><br>|–|
| | | | | |Frequency Domain|TensorFlow<br><br>|3D-CNN| | | | | | |
|(Bouaziz et al., 2019)<br><br>|CHB-MIT|sEEG<br><br>|Segmentation<br><br>|Spatial Representation by Producing A Set of Intensity Images<br><br>|2D Data<br><br>|NA<br><br>|2D-CNN<br><br>|–|Softmax<br><br>|99.49|–|–<br><br>|99.49|
|(Prasanth et al., 2020)<br><br>|Clinical|sEEG|Down-Sampling, Filtering, Artifact Rejection Based on Noise Statistics, Decomposition, Segmentation|–<br><br>|Combination of Raw EEG and Frequency Sub-Bands<br><br>|NA|1D-CNN,<br>2D-CNN<br><br><br>|5|NA| | | | |
|(Ansari et al., 2019)<br><br>|Clinical<br><br>|sEEG<br><br>|–|Different Methods|2D Data<br><br>|MATLAB<br><br>|2D-CNN|10<br><br>|Sigmoid|89.00|82.00<br><br>|90.00|–|
| | | | | | | | | |RF| | | | |
|(Cao et al., 2019)|CHB-MIT<br><br>|sEEG<br><br>|–<br><br>|Sub-band Mean Amplitude of Spectrum (MAS) Map of Multichannel EEGs<br><br>|MAS Map Image|NA<br><br>|SCNN (4 CNNs)<br><br>|5|AWF fusion scheme, KELM classification|99.33<br><br>|–|–<br><br>|–|
| |Clinical| | | | | | | | |98.86|–|–<br><br>|–|
|(Taqi et al., 2017)|Bern Barcelona<br><br>|IEEG|NA<br><br>|–|2D Data<br><br>|Caffe|AlexNet|–<br><br>|Softmax|100<br><br>|–<br><br>|–|–|
| | | | | | | |GoogleNet| | | | | | |
| | | | | | | |LeNet| | | | | | |
|(Emami et al., 2019b)<br><br>|Clinical|sEEG<br><br>|Filtering, Segmentation<br><br>|Visualization<br><br>|2D Data<br><br>|Chainer|2D-CNN<br><br>|–|Softmax<br><br>|80<br><br>|–|–<br><br>|–|
|(Bizopoulos et al., 2019)|UCI<br><br>|sEEG|–<br><br>|Signal2Image|2D Data|PyTorch<br><br>|2D onelayer CNN<br><br>|–|DenseNet<br><br>|85.30<br><br>|–|–|–|
|(Thanaraj et al., 2020)<br><br>|Bern Barcelona|IEEG|Segmentation<br><br>|GASF, DA<br><br>|GASF Images<br><br>|MATLAB|Different PreTrain Networks<br><br>|–|Softmax<br><br>|92.00|–<br><br>|–|–|
| | | |–|Textural Features Extraction from the GASF Images, PSO Feature Selection|Different Features<br><br>|Keras<br><br>|Deep ANN| | | | | | |
| | | | | | |TensorFlow| | | | | | | |

|(Zhang et al., 2020a)<br><br>|CHB-MIT|sEEG|Segmentation, Resizing|STFT<br><br>|2D Spectrograms|NA|VGG-16<br><br>|–<br><br>|Softmax<br><br>|98.26|–|–<br><br>|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | |VGG-19| | | | | | |
| | | | | | | |ResNet-50| | | | | | |
|(Cho and Jang, 2020)|Clinical|IEEG|Segmentation, Down-Sampling, Raw EEG time series<br><br>|Periodogram, STFT Gray Image, Black and White Image of Raw EEG Waveform, Concatenation of 3 Black and White images<br><br>|Raw EEG Signals|TensorFlow<br><br>|2D-CNN<br><br>|10|NA|99.90<br><br>|96.70|99.90<br><br>|–|
| |Kaggle| | | |Periodogram| | | | | | | | |
| | | | | |2D Spectrograms| |FCNN, 1D-CNN| | | | | | |
| | | | | |40 X 250 Image of EEG Signals| | | | | | | | |
| | | | | |40 X 750 Image of EEG Signals| |LSTM| | | | | | |
|(Liu et al., 2020a)|Freiburg|IEEG<br><br>|Segmentation, Normalization|DWT, S-Transform Spectrogram<br><br>|2D Spectrograms|MATLAB<br><br>|2D-CNN|10<br><br>|Softmax<br><br>|98.12|97.01<br><br>|98.12<br><br>|–|
|(Bouallegue et al., 2020)<br><br>|Bonn, CHB-MIT|sEEG<br><br>|Segmentation<br><br>|Filter EEG using FastICA Network, Feature Extraction using GRU|Matrix of Size 16 x 400<br><br>|Keras, TensorFlow|2D-CNN<br><br>|10|Softmax<br><br>|100<br><br>|–<br><br>|–|–|
| | |IEEG| | | | | | | | | | | |
|(Raghu et al., 2020)|TUH<br><br>|sEEG<br><br>|Filtering|STFT|2D Spectrograms<br><br>|MATLAB|Inception-V3<br><br>|10<br><br>|SVM|88.3|–|–<br><br>|–|
|(Li et al., 2020a)<br><br>|Bonn<br><br>|sEEG and IEEG|Segmentation, Resampling, Transformation into 20 Common Channels, Baseline Removal and Detrending, Filtering|–<br><br>|Spectral-Temporal Features|PyTorch<br><br>|CE-stSENet<br><br>|5|MLP<br><br>|99.80|–|–|–|
| |TUSZ<br><br>|sEEG| | | | | | | | | | | |
| |CHB-MIT<br><br>|sEEG| | | | | | | | | | | |
|(Usman et al., 2020)<br><br>|CHB-MIT<br><br>|sEEG|Filtering, Segmentation<br><br>|STFT|2D Spectrograms<br><br>|MATLAB<br><br>|2D-CNN|–<br><br>|SVM|–<br><br>|92.7<br><br>|90.8|–|
|(Ilakiyaselvan et al., 2020)<br><br>|Bonn<br><br>|sEEG and IEEG|Filtering, Segmentation<br><br>|RPS representation|RPS Images<br><br>|Caffe|AlexNet<br><br>|10<br><br>|Softmax|98.5<br><br>|100<br><br>|97.83|–|
|(Bhagat et al., 2020)|CHB-MIT<br><br>|sEEG<br><br>|–<br><br>|Converting 1D EEG Data into 2D EEG Images|224×224 Images|NA<br><br>|ResNet-50<br><br>|–|Softmax<br><br>|94.98|–<br><br>|–<br><br>|–|
|(George et al., 2020)|CHB-MIT<br><br>|sEEG<br><br>|–|Backpropagation Auto Stack Encoder (BP-ASE)<br><br>|–<br><br>|NA|ResNet<br><br>|–<br><br>|Softmax|99.4<br><br>|99|96|96.8|

|(Gao et al., 2020b)<br><br>|CHB-MIT|sEEG|Segmentation<br><br>|DWT Threshold Denoising Method, PSD Analysis, PSDED<br><br>|PSDED|NA<br><br>|InceptionResNet-v2|–|Softmax<br><br>|92.60|92.60<br><br>|97.10|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | |Inception-v3| | | | | | |
| | | | | | | |ResNet152| | | | | | |
|(Singh et al., 2020)<br><br>|Bonn|sEEG and IEEG<br><br>|Filtering, Segmentation|DWT<br><br>|Features from 2D Data|NA|2D-CNN<br><br>|–|Softmax|97.74<br><br>|–<br><br>|–|–|
|(Bhattacherjee, 2020)|Bonn<br><br>|sEEG and IEEG<br><br>|–|Bi-Linear Interpolation, Concatenation of DWT and Power Spectrum Band|2D Data<br><br>|NA|Multi Column CNN<br><br>|–|Softmax<br><br>|99.99<br><br>|–|–|–|
|(Lian et al., 2020)<br><br>|Bonn|sEEG and IEEG<br><br>|Filtering|–<br><br>|Raw EEG Signals<br><br>|NA|Combination of 1D-CNN and 2D-CNN<br><br>|10|Softmax|99.3<br><br>|99.5|99.6<br><br>|–|
|(Madhavan et al., 2019)|Bern-Barcelona<br><br>|IEEG|–|FSST, WSST<br><br>|Time-Frequency Matrix|PyTorch<br><br>|2D-CNN|5<br><br>|Softmax<br><br>|99.94|99.94|99.94<br><br>|–|
|(Sakai et al., 2020)<br><br>|Clinical<br><br>|sEEG|Filtering, Segmentation<br><br>|–|EEG Signals Segment|Keras|ScalpNet<br><br>|–<br><br>|Sigmoid|99.9<br><br>|–|–<br><br>|94.4|
|(Hussein et al., 2020)|Clinical|IEEG<br><br>|Segmentation|CWT|2D Scalograms<br><br>|NA<br><br>|SDCN<br><br>|–<br><br>|Sigmoid|92.80<br><br>|88.45<br><br>|–|–|
| |Clinical<br><br>|IEEG| | | | | | | |88.30|89.52<br><br>|–<br><br>|–|
|(Kaya, 2020)|Bonn<br><br>|sEEG and IEEG|Normalization<br><br>|CWT, mRMR Algorithm|2D Scalograms|NA<br><br>|Combination of AlexNet and VGG16<br><br>|10<br><br>|KNN<br><br>|98.78|99.15<br><br>|–|98.46|
|(Shankar et al., 2020)<br><br>|Bonn<br><br>|sEEG and IEEG|Noise Removal, Instantaneous Power Calculation, Segmentation<br><br>|Gramian Angular Summation Field (GASF) and Gramian Angular Difference field (GADF)<br><br>|2D Data|NA<br><br>|2D-CNN<br><br>|–|Sigmoid<br><br>|98<br><br>|99|98.9|–|
|(Rashed-Al-Mahfuz et al., 2021)<br><br>|Bonn<br><br>|sEEG and IEEG|Segmentation<br><br>|STFT and CWT, RGB Representation, DA|2D Data (Spectrogram, Scalogram)|Keras<br><br>|FT-VGG16|–<br><br>|Softmax|99.21<br><br>|99.04<br><br>|99.38<br><br>|–|

|(Hu et al., 2020a)<br><br>|CHB-MIT and the iNeuro<br><br>|sEEG|Filtering, Segmentation<br><br>|Mean Amplitude Spectrum (MAS), Mean Power Spectral Density (MPSD), and Wavelet Packet Features (WPFs)<br><br>|Fused into a Single Image<br><br>|–|AlexNet, VGG19, Inception-v3, ResNet152, InceptionResNet-v2<br><br>|–<br><br>|Softmax|98.97<br><br>|–|–|–<br><br>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | |Hierarchical Neural Network (HNN)| | | | | | |
|(Glory et al., 2020)|Bonn|sEEG and IEEG<br><br>|–<br><br>|DWT, Nonlinear, and Entropybased features|Different Features<br><br>|Keras, TensorFlow|Hybridizes Adaptive Haar Wavelet-based Binary Grasshopper Optimization Algorithm and Deep Neural Network (AHWBGOA-DNN)<br><br>|10|Softmax<br><br>|–<br><br>|–<br><br>|–|–<br><br>|
| |Bern|IEEG| | | | | | | | | | | |
| |CHB-MIT|sEEG| | | | | | | | | | | |
|(MohanBabu et al., 2020)<br><br>|CHB-MIT|sEEG<br><br>|Filtering, Differentiating|Hilbert Transform, Segmentation, PhaseSynchronization Measures, Graph Model<br><br>|643 × 5 and up to 643 × 50<br><br>|Keras, TensorFlow<br><br>|Optimized Deep Learning Network Model (ODLN)|–<br><br>|Softmax|–<br><br>|100|–<br><br>|–|
|(You et al., 2020)|Clinical<br><br>|sEEG<br><br>|Reviewed Separately by 2 Epileptologists, Filtering|Segmentation, STFT, Normalization, Rescaling, Stack 3 Images to form a Data Structure|2D Spectrograms<br><br>|TensorFlow|AnoGAN<br><br>|–<br><br>|Combination of Anomaly Loss and a Gram Matrix|–<br><br>|96.6<br><br>|–|–|
|(Truong et al., 2019)<br><br>|CHB-MIT|sEEG<br><br>|Segmentation<br><br>|STFT|2D Spectrograms|TensorFlow<br><br>|DCGAN|–<br><br>|Softmax<br><br>|77.68|–<br><br>|–<br><br>|–|
| |EPILEPSIAE|sEEG| | | | | | | | | | | |
| |Freiburg|IEEG| | | | | | | | | | | |

|(Pascual et al., 2019)|EPILEPSIAE<br><br>|sEEG|Segmentation<br><br>|DWT, Power and Non-Linearity per Electrode Features Extraction|Non-Seizure (inter-ictal) EEG Samples|NA<br><br>|Conditional GAN|–|RF<br><br>|–|–<br><br>|–|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|(Torfi and Fox, 2020)<br><br>|UCI|sEEG<br><br>|NA|Different Methods|Matrix<br><br>|NA|CorGAN|–|Softmax<br><br>|–<br><br>|–<br><br>|–|21|
|(Sharan and Berkovsky, 2020)<br><br>|CHB-MIT<br><br>|sEEG<br><br>|Segmentation, Filtering|FFT and WT|135×1×54 with FFT and 132×1×54 with WT<br><br>|NA|1D-CNN|10<br><br>|Softmax|97.25|97.25|97.25<br><br>|–|
|(Hu et al., 2020b)<br><br>|CHB-MIT and iNeuro<br><br>|sEEG|Filtering, Decomposition|Feature Extraction (MAS, MPSD, WPFs)<br><br>|Multiple Fused EEG Features<br><br>|NA|Different PreTrain Nets<br><br>|NA<br><br>|Hierarchical Neural Network (HNN)<br><br>|98.97|–|–<br><br>|–|
|(Ullah et al., 2018)<br><br>|Bonn|sEEG and IEEG<br><br>|–<br><br>|DA|EEG Signals Segment<br><br>|TensorFlow|P-1D-CNN<br><br>|10<br><br>|Majority Voting<br><br>|99.1|–<br><br>|–<br><br>|–|
|(Acharya et al., 2018)<br><br>|Bonn<br><br>|sEEG and IEEG<br><br>|Z- Normalization|–<br><br>|Normalized EEG Signals<br><br>|MATLAB|1D-CNN|10<br><br>|Softmax<br><br>|88.67<br><br>|95|90<br><br>|–|
|(Wang et al., 2020b)<br><br>|Berne-Barcelona<br><br>|EEG|NA|–<br><br>|Raw EEG Signals<br><br>|NA|Time-ResNeXt<br><br>|–<br><br>|Softmax<br><br>|91.5|–|–<br><br>|–|
|(Page et al., 2016)|CHB-MIT|sEEG|Filtering|DA<br><br>|EEG Signals Segment<br><br>|NA<br><br>|MPCNN<br><br>|–|Softmax|96<br><br>|100<br><br>|–|–|
|(Zhang et al., 2020b)<br><br>|Bonn<br><br>|sEEG and IEEG|Normalization|–|Raw EEG Signals<br><br>|Keras|Multi-Scale Non-Local (MNL) Network<br><br>|10|Softmax| | | | |
|(O’Shea et al., 2017a)<br><br>|Clinical|sEEG<br><br>|Down-Sampling, Filtering|–|EEG Signals Segment|Keras<br><br>|1D-FCNN|5|Softmax<br><br>|97.1|–|–|–|
|(Thomas et al., 2020b)|Clinical<br><br>|sEEG<br><br>|Filtering, Down Sampling, Artifact Rejection Based on Noise Statistics, Segmentation|–|EEG Signals Segment|TensorFlow<br><br>|1D-CNN|5<br><br>|Softmax|–<br><br>|80<br><br>|–|–|
|(O’Shea et al., 2017b)|Clinical|sEEG<br><br>|Filtering<br><br>|–|Raw EEG Signals<br><br>|Theano|1D-CNN|–|Binary LR<br><br>|94.70|–<br><br>|–<br><br>|–|
| | | | | | |Lasagne| | | | | | | |
|(Yıldırım et al., 2018)<br><br>|TUH|EEG|Segmentation, Normalization, and Standardization|–<br><br>|EEG Signals Segment|Keras<br><br>|1D-CNN|–|Softmax|79.34<br><br>|–|79.64<br><br>|78.92|
|(Zhao and Wang, 2020)<br><br>|Bonn<br><br>|sEEG and IEEG<br><br>|Normalization|–<br><br>|Raw EEG Signals|Keras, TensorFlow|SeizureNet|10<br><br>|Softmax|98.5<br><br>|97<br><br>|100<br><br>|–|

|(Akyol, 2020)<br><br>|Bonn<br><br>|sEEG and IEEG<br><br>|Normalization|–|Raw EEG Signals<br><br>|Keras, TensorFlow<br><br>|Stacked Ensemble based DNN Modeling<br><br>|10|Meta Learner|97.17|93.11<br><br>|98.18|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|(Thomas et al., 2018)<br><br>|MGH Epileptic Dataset|sEEG|Filtering, Down Sampling|CAR montage<br><br>|Raw EEG Signals|TensorFlow<br><br>|1D-CNN<br><br>|4|SVM<br><br>|83.86|–<br><br>|–|–|
|(Uyttenhove et al., 2020)<br><br>|TUH|sEEG<br><br>|Filtering, Segmentation|–<br><br>|EEG Signals Segment<br><br>|NA|Tiny-Visual Geometry Group (T-VGG)|5<br><br>|NA|70.38| |82.98| |
|(Boonyakitanont et al., 2019)|CHB-MIT<br><br>|sEEG<br><br>|Segmentation, Normalization|–<br><br>|Raw Multi-Channel EEG Signals|NA|1D-CNN|10<br><br>|NA|99.07<br><br>|66.76<br><br>|99.63|65.69|
|(Chen et al., 2018)<br><br>|Bonn|sEEG and IEEG<br><br>|DWT, Segmentation, Normalization| |Preprocessed EEG Signals|NA<br><br>|1D-CNN<br><br>|5<br><br>|Sigmoid|97.27<br><br>|–<br><br>|–|–|
|(Zhang et al., 2020e)<br><br>|TUSZ|sEEG<br><br>|Montage Selection, Segmentation|Denoising, Normalization, DWT, SMOTE<br><br>|4 Wavelet Coefficient Packages|PyTorch<br><br>|DWT-Net|5<br><br>|Softmax|–<br><br>|25.24|97.05<br><br>|–|
|(Zhang et al., 2018)<br><br>|Bonn|sEEG and IEEG|Normalization<br><br>|–<br><br>|Raw EEG Signals|NA|1D-TCNN<br><br>|–<br><br>|NA|100|100<br><br>|100|100|
|(Zhao et al., 2020a)<br><br>|CHB-MIT and Another Dataset|sEEG<br><br>|NA|–<br><br>|Raw EEG Signals|Keras, TensorFlow|Binary SingleDimensional Convolutional Neural Network (BSDCNN)|–<br><br>|Sigmoid|–<br><br>|94.69<br><br>|–|–|
|(Daoud et al., 2018)|Bonn<br><br>|sEEG and IEEG|–<br><br>|EMD Feature Extraction|IMFs of EMD|NA<br><br>|1D-CNN|10<br><br>|Softmax|100<br><br>|100|100<br><br>|100|
|(Daoud et al., 2020)|CHB-MIT<br><br>|sEEG<br><br>|EEG Channel Selection|–|Raw EEG signals<br><br>|NA|DCNN<br><br>|–|NA|96.1<br><br>|97.41<br><br>|94.8|–|
|(Lu and Triesch, 2019)|Bonn|sEEG and IEEG<br><br>|Filtering, Z-Normalization|–|Raw EEG signals<br><br>|TensorFlow|1D-CNN<br><br>|–|Softmax|99.00<br><br>|–|–<br><br>|–|
| | | | | | | | | | |91.80<br><br>|–<br><br>|–<br><br>|–|
|(Craley et al., 2019)|CHB-MIT<br><br>|sEEG|Filtering|–<br><br>|Raw EEG signals|PyTorch|1D-PGMCNN<br><br>|5<br><br>|Softmax<br><br>|80.00|–|–<br><br>|67.00|
| |JHH<br><br>|sEEG| | | | | | | | | | | |
|(Wei et al., 2019)<br><br>|CHB-MIT<br><br>|sEEG|–<br><br>|MIDS, WGANs|5s length EEG Signals|NA|1D-CNN<br><br>|–|Softmax<br><br>|–|74.08<br><br>|92.46<br><br>|–|
|(Qin et al., 2020a)<br><br>|Bonn|sEEG and IEEG|NA<br><br>|–|Raw EEG signals<br><br>|TensorFlow|1D-CNN<br><br>|10<br><br>|Softmax<br><br>|98.67|99<br><br>|98|–|
|(Meisel et al., 2019)<br><br>|Clinical|Multi Modal Wristband Sensor Data<br><br>|Segmentation Down Sampling|–<br><br>|Raw EEG signals|NA<br><br>|1D-CNN<br><br>|4<br><br>|Sigmoid<br><br>|71.4|–|–<br><br>|–|

|(Zhang et al., 2020c)|TUH<br><br>|sEEG|EEG Decomposition to Seizure and Patient Components|–<br><br>|Latten Seizure and Patient Representation|NA<br><br>|CNN|14<br><br>|Sigmoid|80.5<br><br>|97.4|88.1<br><br>|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|(Yuvaraj et al., 2018)<br><br>|CHB-MIT|sEEG<br><br>|Filtering, Segmentation<br><br>|–<br><br>|EEG Signals Segment<br><br>|TensorFlow|1D-CNN<br><br>|4|Softmax|–<br><br>|86.29|–<br><br>|–|
|(Abou Jaoude et al., 2020)<br><br>|Clinical<br><br>|IEEG|Down Sampling, Filtering<br><br>|DA<br><br>|1 Second Epoch from a Single FO-EEG Bipolar Channel|Keras<br><br>|CNN-BP|5|Sigmoid<br><br>|99.60|84.00<br><br>|–<br><br>|–|
| | | | | | |TensorFlow| | | | | | | |
| | | | | | |MATLAB| | | | | | | |
|(Fukumori et al., 2019)<br><br>|Clinical|sEEG|Filtering<br><br>|DWT|Raw EEG signals<br><br>|NA<br><br>|1D-CNN<br><br>|–<br><br>|Sigmoid<br><br>|96.10|–<br><br>|–|–|
| | | | | |Coefficients Subbands D6, D5, D4| |LSTM| |RF| | | | |
| | | | | | | |GRU| |SVM| | | | |
|(Guha et al., 2020)|UC Irvine Machine Learning Repository<br><br>|sEEG<br><br>|Normalization|Feature Extraction, Data Cleaning<br><br>|NA|TensorFlow<br><br>|DNN|–|NA<br><br>|80.00|–<br><br>|–<br><br>|71.00|
| |Bonn|sEEG and IEEG| | | | | | | | | | | |
|(Kaziha and Bonny, 2020)<br><br>|CHB-MIT|sEEG|Segmentation| |EEG Signals Segment<br><br>|Keras|1D-CNN<br><br>|5|Sigmoid<br><br>|96.74|82.35<br><br>|100|–|
|(Truong et al., 2020)|EPILEPSIAE<br><br>|sEEG|NA<br><br>|–|n×59×114|NA<br><br>|Bayesian Convolutional Neural Network (BCNN)|–|Softmax<br><br>|–<br><br>|–|–<br><br>|–|
|(Zhao et al., 2020c)|Bern-Barcelona<br><br>|IEEG|Filtering|DA<br><br>|Augmented EEG Signals|NA<br><br>|1D-CNN|10|NA<br><br>|89.28|–|–<br><br>|–|
|(Boonyakitanont et al., 2020b)|CHB-MIT<br><br>|sEEG<br><br>|Segmentation|–|EEG Signals Segment<br><br>|NA<br><br>|1D-CNN|–<br><br>|Onset-offset Detection Method|99.72<br><br>|72.78<br><br>|99.82|64.4|
|(Khalilpour et al., 2020)<br><br>|CHB-MIT|sEEG<br><br>|Segmentation, Normalization<br><br>|–<br><br>|EEG Signals Segment<br><br>|NA|1D-CNN<br><br>|–|Softmax<br><br>|97<br><br>|98.5|98.47<br><br>|–|
|(Zhao et al., 2020b)<br><br>|Bonn<br><br>|sEEG and IEEG|Segmentation, Normalization<br><br>|–<br><br>|EEG Signals Segment|Keras<br><br>|1D-CNN|10|Softmax<br><br>|99.52<br><br>|–|–|–|
| | | | | | |TensorFlow| | | |98.06|–<br><br>|–|–|
|(Abiyev et al., 2020)<br><br>|Bonn<br><br>|sEEG and IEEG|Normalization<br><br>|–|Raw EEG signals<br><br>|Keras|1D-CNN|10<br><br>|Softmax|98.67|97.67<br><br>|98.83|–|
| | | | | | |TensorFlow| | | | | | | |
|(Pisano et al., 2020)|Clinical<br><br>|sEEG<br><br>|Segmentation, Standard Thresholding, Filtering<br><br>|DA|Augmented EEG Signals<br><br>|MATLAB|1D-CNN<br><br>|–<br><br>|Softmax|96.39<br><br>|93.2<br><br>|96.81|–|
|(Lu et al., 2020)<br><br>|Clinical (Mice)<br><br>|IEEG|Filtering, Segmentation<br><br>|CAM<br><br>|EEG Signals Segment|MATLAB<br><br>|DNN<br><br>|7|Softmax<br><br>|73.00|–<br><br>|–<br><br>|78.00|
| | | | | | |TensorFlow| | | | | | | |

|(Xu et al., 2020c)|Kaggle<br><br>|IEEG<br><br>|Segmentation|–<br><br>|EEG Signals Segment|Keras<br><br>|CNN|–<br><br>|Softmax|98.80|98.80|–<br><br>|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |CHB-MIT|sEEG| | | |TensorFlow| | | | | | | |
|(Lin et al., 2020)|Clinical<br><br>|sEEG<br><br>|Filtering, Normalization, Segmentation, Resampling Strategies|–<br><br>|EEG Signals Segment|NA|Deep ConvNet<br><br>|10|Softmax<br><br>|80<br><br>|70<br><br>|90|77.77|
|(Jana et al., 2020)<br><br>|CHB-MIT|sEEG<br><br>|Filtering, Segmentation|Spectrogram Generation|2D Spectrograms<br><br>|Keras|1D-CNN<br><br>|–<br><br>|Softmax|77.57|75.59|79.54<br><br>|–|
| | | | | | |TensorFlow| | | | | | | |
|(Gao et al., 2020a)<br><br>|Bonn<br><br>|sEEG and IEEG|Segmentation|ApEn and RQA Features<br><br>|Feature Vectors|MATLAB<br><br>|1D-CNN|–<br><br>|Softmax<br><br>|99.26|98.84<br><br>|99.35<br><br>|–|
|(Thomas et al., 2020a)<br><br>|CHB-MIT|sEEG|Segmentation, Resample, Rescale<br><br>|–<br><br>|Raw EEG signals|TensorFlow, Keras<br><br>|1D-CNN|–|NA<br><br>|84.1|–<br><br>|–|–|
|(Vance et al., 2020)|Clinical<br><br>|sEEG<br><br>|Sequence Generation, Resampling|Online Augmentations|Sequence Length of 10 Seconds<br><br>|TensorFlow, Keras|1D-CNN<br><br>|–<br><br>|Sigmoid|77<br><br>|60.6<br><br>|82.8|–|
|(Liu and Richardson, 2020)|CHB-MIT|sEEG<br><br>|Segmentation|–<br><br>|Raw EEG signals|TensorFlow|1D-CNN<br><br>|10|Weighted Majority Voting (WMV)<br><br>|89.21|89.50<br><br>|94.86<br><br>|–|
| | | | | | | |LSTM| | |90.94<br><br>|91.53<br><br>|95.75|–|
|(Vidyaratne et al., 2016)|CHB-MIT<br><br>|sEEG|Filtering<br><br>|Montage Mapping|2D Grid|MATLAB<br><br>|DRNN|–|MLP<br><br>|–|100|–<br><br>|–|
|(Hussein et al., 2018c)|Bonn<br><br>|sEEG and IEEG|Filtering, Segmentation|–|EEG Signals Segment<br><br>|Keras<br><br>|LSTM|10<br><br>|Softmax<br><br>|100|100<br><br>|100<br><br>|–|
| | | | | | |TensorFlow| | | | | | | |
| | | | | | |MATLAB| | | | | | | |
|(Ahmedt-Aristizabal et al., 2018b)|Bonn<br><br>|sEEG and IEEG<br><br>|Segmentation|–|Raw EEG signals<br><br>|Keras|LSTM<br><br>|10|Sigmoid|95.54<br><br>|–<br><br>|–|–|
|(Yao et al., 2019b)<br><br>|CHB-MIT|sEEG<br><br>|Segmentation|–<br><br>|EEG Signals Segment|NA<br><br>|IndRNN<br><br>|10|NA<br><br>|87<br><br>|87.3|86.7<br><br>|87.07|
|(Verma and Janghel, 2021)|Bonn<br><br>|sEEG and IEEG|–<br><br>|DWT|Wavelet Coefficients<br><br>|Keras|RNN<br><br>|NA<br><br>|LR|98.5<br><br>|–|–<br><br>|–|
|(Hussein et al., 2019)|Bonn<br><br>|sEEG and IEEG|Filtering, Segmentation|DA<br><br>|Augmented EEG Signals<br><br>|TensorFlow<br><br>|LSTM|10<br><br>|Softmax<br><br>|100|100<br><br>|100<br><br>|–|
| | | | | | |Keras| | | | | | | |
|(Jaafar and Mohammadi, 2019)<br><br>|Freiburg|IEEG|Normalization, Filtering, Shuffling, Segmenting and Reshaping<br><br>|–|EEG Signals Segment<br><br>|NA|LSTM<br><br>|5<br><br>|Softmax|97.75<br><br>|–|–|–|
|(Hu et al., 2020c)|CHB-MIT|sEEG<br><br>|Segmentation<br><br>|Local Mean Decomposition (LMD), 10 Statistical Features Extraction|Feature Vectors<br><br>|Python|Bi-LSTM<br><br>|NA|Softmax|–<br><br>|93.61|91.85<br><br>|–|
|(Yao et al., 2019a)<br><br>|CHB-MIT|sEEG|Segmentation<br><br>|–|EEG Signals Segment<br><br>|NA|ADIndRNN<br><br>|10<br><br>|NA<br><br>|88.7|88.8<br><br>|88.6|88.71|

|(Talathi, 2017)<br><br>|Bonn|sEEG and IEEG<br><br>|–<br><br>|Auto-Correlation<br><br>|EEG Signals Segment|Keras<br><br>|GRU<br><br>|–|LR<br><br>|98|–<br><br>|–|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|(Roy et al., 2019)|TUH<br><br>|EEG|–<br><br>|TCP|Raw EEG signals<br><br>|NA|ChronoNet<br><br>|–<br><br>|Softmax<br><br>|86.57|–|–<br><br>|–|
|(Hussein et al., 2018b)<br><br>|Bonn<br><br>|sEEG and IEEG<br><br>|Filtering|–|EEG Signals Segment<br><br>|NA|LSTM|–<br><br>|Softmax<br><br>|100|100|100<br><br>|–|
|(Geng et al., 2020)|Freiburg<br><br>|IEEG<br><br>|Segmentation|DA, Stockwell Transform|2D Spectrograms<br><br>|TensorFlow<br><br>|Bi-LSTM|–<br><br>|Softmax|98.91<br><br>|98.08<br><br>|98.91|–|
| | | | | | |MATLAB| | | | | | | |
|(Fraiwan and Alkhodari, 2020)<br><br>|Bern-Barcelona|IEEG|Normalization, Filtering<br><br>|–<br><br>|EEG Signals Segment|MATLAB<br><br>|Bi-LSTM<br><br>|10|Softmax<br><br>|99.6|99.55<br><br>|99.65|–|
|(Hu and Yuan, 2019)<br><br>|Bonn|sEEG and IEEG|Filtering<br><br>|Linear Feature Extraction<br><br>|Linear Features<br><br>|MATLAB|Bi-LSTM<br><br>|–<br><br>|Softmax|98.56<br><br>|100<br><br>|97.14|–|
|(Abbasi et al., 2019)<br><br>|Bonn<br><br>|sEEG and IEEG|Segmentation, Normalization, Standardization|DCT, Hurst Exponent and ARMA Features Extraction<br><br>|Feature Vectors<br><br>|NA|LSTM<br><br>|–<br><br>|Softmax|99.17<br><br>|98.88<br><br>|99.45|–|
|(Yao et al., 2021)<br><br>|CHB-MIT|sEEG<br><br>|Segmentation<br><br>|–|EEG Signals Segment|–<br><br>|Attention Bi-LSTM|10|Softmax|87.8|87.3<br><br>|88.3|87.74|
|(Patan and Rutkowski, 2021)<br><br>|Clinical<br><br>|sEEG<br><br>|Segmentation<br><br>|–|EEG Signals Segment<br><br>|MATLAB<br><br>|LSTM|–<br><br>|Softmax<br><br>|97.9|–|–<br><br>|–|
|(Rajaguru and Prabhakar, 2018)|Clinical<br><br>|EEG|Segmentation|–<br><br>|EEG Signals Segment<br><br>|NA|AE with EM-PCA|–<br><br>|GA|93.92<br><br>|96.11|91.73<br><br>|–|
|(Sharathappriyaa et al., 2018)<br><br>|Bonn|sEEG and IEEG<br><br>|Filtering|HWPT, FD<br><br>|Feature Vectors<br><br>|MATLAB<br><br>|AE|–<br><br>|Softmax<br><br>|98.67|98.18|100<br><br>|–|
|(Emami et al., 2019a)<br><br>|Clinical|sEEG|Down Sampling, Filtering, Normalization<br><br>|–<br><br>|EEG Signals Segment<br><br>|TensorFlow|AE<br><br>|–<br><br>|Sigmoid|–<br><br>|100<br><br>|–|–|
|(Yuan et al., 2017)|CHB-MIT<br><br>|sEEG|–<br><br>|STFT|2D Spectrograms|NA<br><br>|SSDA|–|Softmax|93.82<br><br>|–|–| |
|(Qiu et al., 2018)|Bonn<br><br>|sEEG and IEEG<br><br>|Segmentation, Z-Normalization, Standardization|–<br><br>|EEG Signals Segment<br><br>|MATLAB|DSAE<br><br>|–<br><br>|LR<br><br>|100|100<br><br>|100<br><br>|–|
|(Golmohammadi et al., 2019)<br><br>|TUH<br><br>|sEEG<br><br>|–|Different Methods<br><br>|A Vector of 6 Posterior Probabilities<br><br>|Theano|SDA|–<br><br>|LR<br><br>|–<br><br>|90|–<br><br>|–|
|(Yan et al., 2016)<br><br>|Bonn|sEEG and IEEG<br><br>|Filtering|–<br><br>|Raw EEG signals|NA<br><br>|SAE<br><br>|–|SVM|100<br><br>|100|100<br><br>|–|
|(Lin et al., 2016)<br><br>|Bonn|sEEG and IEEG<br><br>|Segmentation, Normalization|–<br><br>|EEG Signals Segment|NA|SSAE<br><br>|–|Softmax|100<br><br>|100|100<br><br>|–|
|(Yuan et al., 2019)<br><br>|CHB-MIT<br><br>|sEEG|Segmentation<br><br>|Scalogram|2D Scalograms<br><br>|Theano<br><br>|Wave2Vec|–<br><br>|Softmax<br><br>|93.92<br><br>|–|–<br><br>|96.05|
|(Gasparini et al., 2018)|Clinical<br><br>|EEG|Filtering|CWT, Feature Extraction<br><br>|Feature Vectors<br><br>|NA|SAE<br><br>|–<br><br>|Softmax|86.5<br><br>|88.8<br><br>|90.7<br><br>|–|

|(Karim et al., 2018a)|Bonn<br><br>|sEEG and IEEG|–|Taguchi Method<br><br>|Raw EEG signals|NA<br><br>|SSAE<br><br>|–|Softmax|99.8|–|–<br><br>|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|(Karim et al., 2019)<br><br>|Clinical|EEG<br><br>|–|Dimension Reduction, ESD<br><br>|Feature Vectors|NA<br><br>|DSAEs|–<br><br>|Softmax<br><br>|100<br><br>|–|–<br><br>|–|
|(Karim et al., 2018b)<br><br>|Bonn<br><br>|sEEG and IEEG|–<br><br>|DWT|Feature Vectors|NA|SAE<br><br>|–|Softmax|96<br><br>|–<br><br>|–<br><br>|–|
|(Yuan et al., 2018c)<br><br>|CHB-MIT|sEEG<br><br>|–|Different Methods<br><br>|2D Spectrograms|NA|SAEs|–<br><br>|Softmax|96.61<br><br>|–<br><br>|–|97.85|
|(Sharma et al., 2020)|Bonn<br><br>|sEEG and IEEG|–<br><br>|Raw EEG Signals in to 2D Space using the Third-Order Cumulant|ToC Coefficients|NA|SAE<br><br>|–|Softmax|100<br><br>|100<br><br>|100<br><br>|–|
|(Siddharth et al., 2020)<br><br>|Bern-Barcelona<br><br>|IEEG<br><br>|Standard Preprocessing|FBSE-EWT<br><br>|Raw EEG signals|NA<br><br>|SAE|5<br><br>|SVM|100<br><br>|100|100|–|
|(Le et al., 2018)<br><br>|Clinical|EEG<br><br>|–|DWT<br><br>|Waveform Features<br><br>|MATLAB|DBN<br><br>|–|NA|–<br><br>|87.35<br><br>|97.89|–|
|(Turner et al., 2017)<br><br>|Clinical|EEG|Normalization, Standardization|Feature Extraction<br><br>|Feature Vectors|Theano<br><br>|DBN|–<br><br>|LR<br><br>|85<br><br>|–|–<br><br>|–|
|(Tang et al., 2020)<br><br>|CHB-MIT|sEEG|Segmentation|Decomposition, Multi-View Feature Extraction<br><br>|3 Feature Sets (Local Fractal Spectrum, Relative Band Energy, Synchronization Modularity)|NA<br><br>|Multi-View CNN-GRU|–<br><br>|Softmax|–<br><br>|94.5<br><br>|–|–|
|(Thodoroff et al., 2016)|CHB-MIT|sEEG<br><br>|–|Image Based Representation|2D Data<br><br>|NA|2D CNN-LSTM|–|NA<br><br>|–|–|–|–|
|(Saqib et al., 2020)<br><br>|TUSZ| |Resampling, Filtering, Segmentation|DA|1000×21<br><br>|NA|2D CNN-LSTM|–|Softmax<br><br>|–<br><br>|86<br><br>|–|65.1|
|(Choi et al., 2019)<br><br>|CHB-MIT<br><br>|sEEG|–<br><br>|STFT, 2D-mapping|2D Spectrograms<br><br>|NA|3D-CNN Bi GRU<br><br>|–|NA<br><br>|99.40|89.00<br><br>|99.50|–|
| |SNUH| | | | | | | | | | | | |
|(Liang et al., 2020)<br><br>|CHB-MIT<br><br>|sEEG|–<br><br>|Converted Into a Series of Two Seconds Waveform Images|EEG Signals Segment<br><br>|NA|LRCN<br><br>|–|Softmax<br><br>|99|84<br><br>|99|–|
|(Roy et al., 2018)<br><br>|TUH|sEEG<br><br>|Various Preprocessing Technique|–<br><br>|EEG Signals Segment|NA|1D-CNN-RNN<br><br>|–<br><br>|Softmax<br><br>|70.39|–|–<br><br>|–|
|(Golmohammadi et al., 2017)<br><br>|TUH<br><br>|sEEG|Segmentation, Filtering<br><br>|Feature Extraction, left to right channel independent GMMHMM, PCA, IPCA|EEG Signals Segment (210 frames of EEGs)<br><br>|NA|CNN-LSTM<br><br>|–|Different Activation Functions<br><br>|–|39.09<br><br>|76.84|–|
| |Clinical| | | | | | | | | | | | |

|(Li et al., 2020b)<br><br>|Bonn<br><br>|sEEG and IEEG|Segmentation, Resizing<br><br>|–<br><br>|EEG Signals Segment|Keras<br><br>|FC-NLSTM<br><br>|10|Softmax<br><br>|100|100<br><br>|100|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |Freiburg CHB–MIT<br><br>|IEEG sEEG| | | |TensorFlow| | | | | | | |
|(Liu et al., 2020b)<br><br>|UCI|sEEG|Segmentation<br><br>|–|EEG Signals Segment<br><br>|NA|C-LSTM|–<br><br>|Softmax<br><br>|98.8<br><br>|100<br><br>|–|100|
|(Yang et al., 2021)<br><br>|Clinical<br><br>|Long-Term Video-EEG Monitoring|Segmentation, Resizing<br><br>|–|224 x 224-Pixel Resolutions|Keras, TensorFlow<br><br>|CNN-LSTM<br><br>|–|Sigmoid<br><br>|–|88<br><br>|92<br><br>|–|
|(Xu et al., 2020a)<br><br>|UCI|sEEG<br><br>|Normalization|–<br><br>|Raw EEG signals|–<br><br>|1D CNN-LSTM|–<br><br>|Softmax|99.39<br><br>|–<br><br>|–|98.59|
|(Yuan et al., 2018b)<br><br>|CHB-MIT<br><br>|sEEG|–|DA, STFT|2D Spectrograms<br><br>|PyTorch<br><br>|CNN-AE|5<br><br>|Softmax|94.37|–<br><br>|–<br><br>|85.34|
|(Wen and Zhang, 2018)<br><br>|Bonn|sEEG and IEEG<br><br>|Channel Selection|–|Raw EEG signals<br><br>|NA<br><br>|CNN-AE<br><br>|10|Different Methods|92.00<br><br>|–<br><br>|–|–|
| |CHB-MIT<br><br>|sEEG| | | | | |5| | | | | |
|(Abdelhameed et al., 2018)<br><br>|Bonn<br><br>|sEEG and IEEG|Segmentation<br><br>|–|EEG Signals Segment<br><br>|NA<br><br>|1D-CNN-AE|–<br><br>|MLP/LSTM/ Bi-LSTM<br><br>|100|100|100<br><br>|–|
|(Antoniades et al., 2018)|Clinical<br><br>|sEEG<br><br>|–<br><br>|Mapping<br><br>|EEG Signals Segment|Theano|ASAE-CNN<br><br>|–<br><br>|LR|68.00<br><br>|67.00<br><br>|68.00|68.00|
| | | | | | | |AAE-CNN| | | | | | |
|(Yuan and Jia, 2019)<br><br>|CHB-MIT<br><br>|sEEG|–<br><br>|STFT|2D Spectrograms|PyTorch<br><br>|CNN-AE|5<br><br>|Softmax|96.22<br><br>|–|–<br><br>|89.53|
|(Daoud and Bayoumi, 2019)<br><br>|Bonn|sEEG and IEEG<br><br>|Segmentation, Filtering, Normalization|DA<br><br>|EEG Signals Segment<br><br>|NA<br><br>|DCAE|10<br><br>|MLP<br><br>|96.00|93.00|99.00<br><br>|–|
| |Bern Barcelona<br><br>|IEEG| | | | |DCVAE| |K-means clustering| | | | |
|(Shoeibi et al., 2021)<br><br>|Bonn<br><br>|sEEG and IEEG|Filtering, Segmentation<br><br>|Feature Extraction (Time, Statistical, Non-Linear), Feature Selection (Fisher Feature Scoring Algorithm)|Feature Vectors (20 Most Important Features)<br><br>|TensorFlow|CNN-AE|–<br><br>|Softmax<br><br>|99.53<br><br>|–|–|–|
|(Takahashi et al., 2020)<br><br>|Clinical<br><br>|sEEG|Filtering, Segmentation<br><br>|–|EEG Signals Segment|–<br><br>|CNN-AE|–|Softmax<br><br>|99.6|–<br><br>|–|52.6|

#### Table 3: Summary of related works done using medical imaging methods and DL.

|Work<br><br>|Dataset|Modalities|Preprocessing<br><br>|Preprocessing Toolbox|Input Network|DNN<br><br>|DNN toolbox|Classifier|K-fold<br><br>|Performance criteria (%)| | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |Acc<br><br>|Sens<br><br>|Spec<br><br>|F1-S|
|(Dev et al., 2019)|SCTIMST<br><br>|MRI|Noise Reduction with BM3D Algorithm, Skull-Stripping, FCD Lesion Segmentation<br><br>|FSL|256 × 256 Image Size|FCN<br><br>|Keras|Sigmoid|5<br><br>|–<br><br>|–<br><br>|–|–|
| | | | | | | |TensorFlow| | | | | | |
|(Gill et al., 2018)<br><br>|Clinical<br><br>|MRI|Different Methods<br><br>|NA|3D Patches<br><br>|Two-Stage CNNx Cascade|NA<br><br>|Softmax<br><br>|5|–<br><br>|87|90|–|
|(Hao et al., 2018)|Clinical<br><br>|EEG-fMRI|Filtering, ICA, BCG, GLM, MCS|Brain Vision Analyzer Software<br><br>|IEDs|ResNet<br><br>|NA<br><br>|Triplet|–<br><br>|–<br><br>|–<br><br>|84.40|–|
| | | | | | | | | |Softmax| | | | |
|(Hosseini et al., 2017)|Clinical<br><br>|EEG/ECoG<br><br>|Different Methods|NA<br><br>|Preprocessed EEG and fMRI Data<br><br>|2D-CNN|NA<br><br>|SVM|–<br><br>|–|–<br><br>|–|–|
| | |rs-fMRI| | | | | | | | | | | |
|(Yan et al., 2018)|Clinical<br><br>|MRI<br><br>|Scaling Down|NA<br><br>|Raw MRI Data|3D-CNN<br><br>|NA|Softmax|5<br><br>|98.8<br><br>|–|–|–|
|(Gleichgerrcht et al., 2018)<br><br>|Clinical|MRI<br><br>|Preprocessing the Connectivity Matrix, Construction of The SZ And SZF Binary Masks, Applying Masks to Reduce Dimensionality of Input Connectivity Matrix<br><br>|NA|SZ and SZF Binary Masks|2D-CNN<br><br>|NA|Softmax|–<br><br>|–<br><br>|–|–<br><br>|–|
|(Jiang et al., 2019a)|Clinical|PET<br><br>|ROI, Normalization, AAL, CNNI, Down-sampling, NNI (3D images)<br><br>|NA<br><br>|2D ROI<br>3D ROI<br><br><br>|2D-ResNet 50|TensorFlow|Sigmoid|–<br><br>|98.22|97.27|98.86<br><br>|–|
| | | | | | |2D-VGG 16| | | | | | | |
| | | | | | |2D-Inception V3|Keras| | | | | | |
| | | | | | |3D-SVGG-C3D| | | | | | | |
|(Shiri et al., 2019)|Clinical<br><br>|PET|OSEM, DA Radionics Features|NA<br><br>|Non-AttenuationCorrected (NAC) 2D PET Image Slices|Deep-DAC<br><br>|TensorFlow|Tanh|–<br><br>|–|–<br><br>|–|–|
|(Wang et al., 2020a)<br><br>|Clinical<br><br>|MRI|Bias Field Correction, SkullStripping, Intensity Normalization, Patch Extraction, DA|NA|Patches<br><br>|CNN|MATLAB<br><br>|Softmax<br><br>|–|88<br><br>|90<br><br>|85|–|
|(Shakeri et al., 2016)<br><br>|a Rolandic Epilepsy (RE) study|MRI<br><br>|Resizing, DA|NA<br><br>|Single 2D Slice<br><br>|FCN|MATLAB|Softmax|–<br><br>|–<br><br>|–|–|–|
|(Figini et al., 2020)<br><br>|HCP Dataset|MRI<br><br>|Simulated LF Images from HF References<br><br>|NA<br><br>|Paired HF and Simulated LF Images|Aniso-U-Net|NA<br><br>|–<br><br>|–|–<br><br>|–|–<br><br>|–|
|(Pominova et al., 2018)<br><br>|Clinical|sMRI, rsfMRI<br><br>|Resizing, Denoising|SPM, FSL<br><br>|3D Scans|VoxCNN-B<br><br>|NA|Softmax|5<br><br>|–<br><br>|–|–|–|

|(Xu et al., 2019)|Clinical<br><br>|DWI, fMRI|Different Methods<br><br>|SPM, FSL|DWI Streamline Coordinate|DCNN-CL-ATT|PyTorch<br><br>|Softmax<br><br>|–|–<br><br>|–|–<br><br>|–|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|(Torres-Vela´zquez et al., 2020)<br><br>|ECP Project<br><br>|sMRI, rsfMRI and task-fMRI, PDC data|Minimal Pre-Processing Pipelines For The Human Connectome Project (HCP) Version 3.4.0<br><br>|FSL|sMRI Features, rs-fMRI and task-fMRI Based ROI Correlation Matrices, and PDC<br><br>|Multi-Channel Deep Neural Network (mDNN)|Keras<br><br>|Output Layer|10|72.86<br><br>|–<br><br>|–<br><br>|–|
|(Rebsamen et al., 2020)|Inselspital|MRI|Ground Truth Generation using FreeSurfer, Skull-Stripping, ReSampled and Cropped, Re-Scaled, DA<br><br>|FreeSurfer<br><br>|Preprocessed MRI|3D-CNN<br><br>|TensorFlow|–|–|–|–<br><br>|–<br><br>|–|
|(Si et al., 2020)<br><br>|Clinical|Diffusion MRI<br><br>|Standard Preprocessing, Generate The Connectivity Matrix using HARDI and (NODDI) Methods|MRIcro, MRtrix3, DSI studio, NODDI toolbox<br><br>|Connectivity-Strength Based Weight ICVF<br><br>|Inception ResNet v2<br><br>|NA<br><br>|Softmax<br><br>|–<br><br>|75.2|–|–<br><br>|–|
|(Huang et al., 2020)|Clinical|MRI|Series of Standard Preprocessing Procedures, Hippocampus Mask, FA, MD, and MK of Hippocampus<br><br>|SPM8, MATLAB R2017a<br><br>|FA, MD, and MK Slice-Level|VGG16<br><br>|–|SVM|5|90.8<br><br>|89.29|93.5<br><br>|–|
|(Lee et al., 2020)|Clinical|DWI<br><br>|Series of Different Preprocessing Procedures|FreeSurfer, FSL, MRtrix3 package, ANTs package, QuickBundles package<br><br>|14 ESM<br><br>|DCNN<br><br>|PyTorch<br><br>|Softmax|–<br><br>|92<br><br>|–|–|99.3|

#### Table 4: Details for DL Networks for Epileptic Seizures Detection.

|Work<br><br>|Networks|Network Details<br><br>|Classiﬁer|Optimizer<br><br>|Loss Function|
|---|---|---|---|---|---|
|(Antoniades et al., 2016)|2D-CNN<br><br>|1 Conv Layer + 1 FC Layer<br>2 Conv Layers + 1 FC Layer<br>|LR<br><br>|NA|NA|
|(Qin et al., 2020b)<br><br>|2D-CNN|3 Conv Layers + 3 Max Pooling Layers + 3 BN Layers + 1 FC Layer + ReLU activation function<br><br>|ELM<br><br>|NA|NA|
|(Park et al., 2018)<br><br>|Combination of 1D-CNN and 2D-CNN<br><br>|6 1D Conv Layers + 3 2D Conv Layers + 3 Max Pooling Layers + 2 FC Layers<br><br>|Sigmoid<br><br>|Sum-Squared Error|Proposed Loss Function|
|(Tjepkema-Cloostermans et al., 2018)|2D-CNN<br><br>|6 Conv Layers + 6 Dropout Layers + 3 Max Pooling Layers + 2 FC Layers<br><br>|Softmax|Adam|Categorical Cross Entropy (CCE)|

|(Avcu et al., 2019)<br><br>|SeizNet|4 Conv Layers + 4 Max Pooling Layers + 5 Dropout Layers + 4 BN Layers + 1 FC Layer<br><br>|Dense Layer<br><br>|Adam|Binary Cross Entropy (BCE)|
|---|---|---|---|---|---|
|(Zhan and Hu, 2020)<br><br>|DCNN<br><br>|4 Conv Layers + 4 FC Layers|Multiview Fuzzy Clustering Method<br><br>|NA<br><br>|NA|
|(Nejedly et al., 2019)<br><br>|CNN|6 Conv Layers + 6 BN Layers + 3 Dropout Layers + 3 FC Layers<br><br>|Softmax<br><br>|Adam<br><br>|CE|
|(Hossain et al., 2019)|2D-CNN|4 Conv layers + 2 Max Pooling Layers + 4 BN Layers + 1 Dropout Layer<br><br>|Softmax|Minibatch SGD|NA|
|(Mao et al., 2020)<br><br>|2D-CNN|3 Conv layers + 3 pooling layers + ReLU activation function|Softmax<br><br>|NA<br><br>|NA|
|(Zuo et al., 2019)|2D-CNN<br><br>|4 Conv Layers + 4 BN Layers + 3 Max Pooling Layers + 1 Dropout Layer + 2 FC Layers<br><br>|Softmax|Minibatch SGD<br><br>|CE|
|(Asif et al., 2019)|SeizureNet<br><br>|52 Conv Layers + 5 Pooling Layers + 51 BN Layers + 24 Dropout Layers|Softmax<br><br>|Adam|Proposed Loss Function|
|(Iesˇmantas and Alzbutas, 2020)<br><br>|2D-CNN<br><br>|1 Conv Layer + 1 subsampling Layer+ 1 FC layer|Softmax|Adam<br><br>|CE|
|(Zeng et al., 2021)<br><br>|GRP-DNet|DenseNet: 1 Conv Layer + 3 Dense Blocks + 2 Transition Layers + 3 Global Average Pooling Layers + 1 FC Layer<br><br>|Softmax|Adam<br><br>|CE|
|(San-Segundo et al., 2019)|2D-CNN<br><br>|2 Conv Layers + 1 Max Pooling Layer +4 Dropout Layers + 2 FC Layers|Softmax<br><br>|Root-Mean Square Propagation Method<br><br>|CCE|
| | | |Sigmoid| | |
|(Sui et al., 2019)<br><br>|2D-CNN|5 Conv Layers + 5 Max Pooling Layers + 5 FC Layers<br><br>|Softmax<br><br>|NA<br><br>|NA|
|(Chatzichristos et al., 2020)<br><br>|Attention-Gated U-Net<br><br>|15 Conv Layers + 6 Max Pooling Layers + 5 Average Pooling Layers + 6 Up Sampling Layers + 5 Gating Signals + 5 Attention Gates|Bi-LSTM + FC Layer| |Regular Cross-Entropy, Weighted Cross-Entropy|
|(Covert et al., 2019)|TGCN<br><br>|4 STC Layers + 5 Pooling Layers + 4 BN Layers + 2 FC Layers + 1 Dropout Layer<br><br>|Sigmoid|SGD<br><br>|CE|
| | |8 STC Layers + 5 Pooling Layers + 4 BN Layers + 2 FC Layers + 1 Dropout Layer| | | |
| | |12 STC Layers + 5 Pooling Layers + 4 BN Layers + 2 FC Layers + 1 Dropout Layer| | | |
| | |16 STC Layers + 5 Pooling Layers + 4 BN Layers + 2 FC Layers + 1 Dropout Layer| | | |
|(Akut, 2019)<br><br>|2D-CNN|4 Conv Layers + 2 Max Pooling Layers+ 8 BN Layers + 4 Dropout Layers + 4 FC Layers<br><br>|Softmax|NA|NA|
|(Tu¨rk and Ozerdem,¨ 2019)<br><br>|2D-CNN<br><br>|2 Conv Layers + 2 Max Pooling Layers|Softmax<br><br>|Adadelta<br><br>|NA|
|(Liu and Woodson, 2019)<br><br>|2D-CNN|3 Conv Layers + 3 BN Layers + 2 Max Pooling Layers + 1 FC Layer<br><br>|Softmax<br><br>|NA|NA|
|(Tian et al., 2019)|2D-CNN<br><br>|4 Conv Layers + 3 FC Layers|MV-TSK-FS<br><br>|NA<br><br>|CE|
| | |2 Conv Layers + 3 FC Layers| | | |
| |3D-CNN|4 Conv Layers + 4 FC Layers| | | |
|(Bouaziz et al., 2019)|2D-CNN|3 Conv Layers + 2 Max Pooling Layers + 1 FC Layer<br><br>|Softmax<br><br>|SGD| |
|(Prasanth et al., 2020)<br><br>|1D-CNN,<br>2D-CNN<br>|NA<br><br>|NA|NA<br><br>|NA|
|(Ansari et al., 2019)<br><br>|2D-CNN|7 Conv Layers + 8 Pooling Layers + 2 FC Layers|Sigmoid<br><br>|NA|NA<br><br>|
| | |5 Conv Layers + 8 Pooling Layers<br><br>|RF| | |
|(Cao et al., 2019)<br><br>|SCNN|2 Conv Layers + 2 Max Pooling Layers + 1 Dropout Layer + 2 FC Layers<br><br>|KELM|SGD<br><br>|NA|

|(Taqi et al., 2017)|GoogleNet<br><br>|Standard Network<br><br>|Softmax|NA<br><br>|CE|
|---|---|---|---|---|---|
| |AlexNet| | | | |
| |LeNet| | | | |
|(Emami et al., 2019b)|2D-CNN|VGG-16<br><br>|Softmax|Adam|NA|
|(Bizopoulos et al., 2019)<br><br>|2D-CNN|Standard Networks<br><br>|Softmax|NA<br><br>|NA|
| |1D-CNN| | | | |
|(Thanaraj et al., 2020)<br><br>|AlexNet, VGG16, VGG-19|Standard Network|Softmax<br><br>|NA|NA|
| |Custom CNN|3 Conv Layers, 1 BN Layer + 1 Max-Pooling Layer + 2 FC Layers|Softmax| | |
|(Zhang et al., 2020a)|VGG-16<br><br>|Standard Network + 2 Trainable FC Layers<br><br>|Softmax<br><br>|SGD|Softmax Cross Entropy (SCE)<br><br>|
| |VGG-19| | | | |
| |ResNet-50| | | | |
|(Cho and Jang, 2020)<br><br>|2D-CNN|2 Conv Layers + 2 Max Pooling Layers + 2 FC Layers + 2 Dropout Layers<br><br>|Output Layer<br><br>|Adam<br><br>|NA|
| |1D-CNN<br><br>|2 Conv Layers + 2 Max Pooling Layers + 2 FC Layers + 2 Dropout Layers| | | |
| |LSTM|1 LSTM Layer + 1 Pooling Layer + 1 FC Layer| | | |
|(Liu et al., 2020a)<br><br>|2D-CNN|4 Conv Layers + 4 BN Layers + 3 Max Pooling Layers + 1 FC Layer + 2 Dropout Layers<br><br>|Softmax|Adam|CE|
|(Bouallegue et al., 2020)<br><br>|2D-CNN|Conv Layers + Max Pooling Layers + FC Layers + Dropout Layer + ReLU Activation Function<br><br>|Softmax<br><br>|Adam<br><br>|MSE|
| |RNN-GRU|2 GRU Layers + 1 FC Layer + ReLU Activation Function<br><br>|NA| | |
|(Raghu et al., 2020)<br><br>|Inception-V3|Standard Network + Final Three Layers Replaced<br><br>|SVM<br><br>|SGDM, RMSProp, Adam|NA|
|(Li et al., 2020a)<br><br>|CE-stSENet<br><br>|Proposed Architecture|MLP<br><br>|Adam<br><br>|CE|
|(Usman et al., 2020)<br><br>|2D-CNN|3 Conv Layers + 3 BN Layers + 3 Max Pooling Layers + 1 Dropout Layer<br><br>|SVM<br><br>|NA|NA|
|(Ilakiyaselvan et al., 2020)|AlexNet<br><br>|Standard Network|Softmax<br><br>|SGD<br><br>|CE|
|(Bhagat et al., 2020)<br><br>|ResNet-50<br><br>|Modified<br><br>|Softmax<br><br>|Adam|Categorical CE|
|(George et al., 2020)|ResNet<br><br>|Standard Network<br><br>|Softmax|NA<br><br>|NA|
|(Gao et al., 2020b)|InceptionResNet-v2<br><br>|Standard Network + 2 FC Layers|Softmax<br><br>|NA<br><br>|OHEM|
| |Inception-v3| | | | |
| |ResNet152| | | | |
|(Singh et al., 2020)<br><br>|2D-CNN<br><br>|2 Conv Layers + 2 BN Layers + 1 Max-Pooling Layer + 1 FC Layer<br><br>|Softmax|SGD<br><br>|NA|
|(Bhattacherjee, 2020)<br><br>|Multi Column CNN|–<br><br>|Softmax<br><br>|NA|NA|
|(Lian et al., 2020)|Combination of 1D-CNN and 2D-CNN<br><br>|2 1D-Conv Layers + 3 2D-Conv Layers + 1 FC Layer<br><br>|Softmax|NA|SLF|

|(Madhavan et al., 2019)|2D-CNN<br><br>|5 Conv Layers + 5 Pooling Layers + 5 FC Layers<br><br>|Softmax|SGD|CE|
|---|---|---|---|---|---|
|(Sakai et al., 2020)<br><br>|ScalpNet|11 Conv Layers + 10 Dropout Layers + 1 FC Layer<br><br>|Sigmoid|NA<br><br>|Focal Loss|
|(Hussein et al., 2020)<br><br>|SDCN|6 SDC Blocks+ 2 FC Layers<br><br>|Sigmoid|Adam|BCE|
|(Kaya, 2020)|Combination of AlexNet and VGG16|Standard Networks<br><br>|KNN|NA<br><br>|NA|
|(Shankar et al., 2020)|2D-CNN|3 Conv Layers + 4 BN Layers + 1 Dropout Layer + 3 Max Pooling Layers + 1 FC Layer<br><br>|Sigmoid<br><br>|SGD|BCE|
|(Rashed-Al-Mahfuz et al., 2021)|FT-VGG16<br><br>|Fine-tuning VGG16|Softmax|RMSprop|–|
|(Hu et al., 2020a)|Different PreTrain Nets<br><br>|Standard Versions|Softmax<br><br>|Mini-Batch Gradient Descent (MBGD)|CE|
| |HNN<br><br>|3 Cascaded Learning Blocks| | | |
|(Glory et al., 2020)|AHW-BGOADNN<br><br>|NA|Softmax|Adaptive Optimization, SGD with CLRA<br><br>|CCE|
|(MohanBabu et al., 2020)<br><br>|ODLN|2 ODLN Layers + 2 Dropout Layers + Avg Pooling Layer|Softmax|Adam|CCE|
|(You et al., 2020)<br><br>|AnoGAN<br><br>|Generator: 4 Transposed Conv Layers + 4 BN layers, Discriminator: 4 Conv Layers+ 4 BN Layers|Combination of Anomaly Loss and a Gram matrix<br><br>|SGD<br><br>|Sigmoid Cross Entropy (SCE)|
| | | | |Adam| |
|(Truong et al., 2019)<br><br>|DCGAN|Generator: FC Layer+ Reshape Layer+ 3 de-Conv Layers, Discriminator: 3 Conv Layers + Flatten Layer+ FC Layer, Classifier: 2 FC Layers + 2 Dropout Layers<br><br>|Softmax<br><br>|Adam<br><br>|NA|
|(Pascual et al., 2019)|conditional GAN<br><br>|Generator: 8 Conv Layers + 8 Max Pooling Layers + 8 de-Conv Layers + 8 Dilations Layers, Discriminator: 8 Conv Layers + 8 Max Pooling Layers + 8 deConv Layers + 8 Dilations Layers + 1 FC Layer|RF<br><br>|Adam|LSGAN|
|(Torfi and Fox, 2020)<br><br>|CorGAN|CorGAN with Proposed Layers<br><br>| |NA<br><br>|BCE|
|(Sharan and Berkovsky, 2020)|1D-CNN<br><br>|3 Conv Layers + 3 Max Pooling Layers + 1 FC Layer + ReLU Activation Function<br><br>|Softmax<br><br>|Adam| |
|(Hu et al., 2020b)|Different PreTrain Nets|Modified models<br><br>| |7-Layer HNN<br><br>|Mini-Batch Gradient Descent (MBGD)|
|(Ullah et al., 2018)<br><br>|P-1D-CNN<br><br>|3 Conv Layers + 3 BN Layers + 1 Dropout Layer + 2 FC Layers|majority voting|Adam<br><br>|CE|
|(Acharya et al., 2018)<br><br>|1D-CNN|5 Conv Layers + 5 Max Pooling Layers + 2 FC Layers<br><br>|Softmax|NA<br><br>|NA|
|(Wang et al., 2020b)<br><br>|Time-ResNeXt|Not Reported<br><br>|Softmax<br><br>|Adam|CE|
|(Page et al., 2016)|MPCNN|1-3 pairs of Conv and Max Pooling Layers + 1-3 FC Layers + Dropout<br><br>|Softmax<br><br>|NA<br><br>|NA|
|(Zhang et al., 2020b)|MNLN|3 Conv Layers + 3 BN Layers + 2 Max Pooling Layers + 1 Signal Pooling Layer + 1 Multi-Scale Non-Local Layer + 2 FC Layers + RELU Activation Function<br><br>|Softmax<br><br>|Adam|CE|
|(O’Shea et al., 2017a)<br><br>|1D-FCNN|6 Conv Layers + 1 BN Layer + 3 Pooling Layers|Softmax<br><br>|SGD<br><br>|CCE|

|(Thomas et al., 2020b)|1D-CNN<br><br>|2 Conv Layers + Max Pooling Layer + 2 FC Layers + Dropout Layer + ReLU Activation Function|Softmax|Adam<br><br>|CE|
|---|---|---|---|---|---|
|(O’Shea et al., 2017b)<br><br>|1D-CNN|3 Conv Layers + 1 FC Layer + 1 Dropout Layer<br><br>|Binary LR|SGD<br><br>|BCE|
|(Yıldırım et al., 2018)|1D-CNN<br><br>|10 Conv Layers + 5 Max Pooling Layers + 2 Dropout Layers + 1 BN Layer + 1 FC Layer|Softmax<br><br>|Adam|CCE|
|(Zhao and Wang, 2020)|SeizureNet<br><br>|10 Conv Layers + 10 BN Layers + 6 Max Pooling Layers + 1 FC Layer + 1 Dropout Layer + ReLU Activation Function|Softmax<br><br>|Adam|Binary CE|
|(Akyol, 2020)<br><br>|Stacked Ensemble based DNN modeling|3 Hidden Layers + ReLU Activation Function<br><br>|Meta Learner|Adam<br><br>|NA|
|(Thomas et al., 2018)<br><br>|1D-CNN|1 Conv Layer + 1 Pooling Layer + 1 FC Layer + 1 Dropout Layer<br><br>|SVM|Adam|NA|
|(Uyttenhove et al., 2020)<br><br>|T-VGG|6 Conv Layers + 6 BN Layers + 3 Max Pooling Layers + 1 FC Layer + ReLU Activation Function<br><br>|Output Layer|Adam|Binary Cross-Entropy|
|(Boonyakitanont et al., 2019)<br><br>|1D-CNN|11 Conv Layers + 5 BN Layers + 5 Max Pooling Layers + 3 Dropout Layers + 8 FC Layers<br><br>|NA<br><br>|NA|NA|
|(Chen et al., 2018)|1D-CNN<br><br>|1 Conv Layer+ 1 Max Pooling Layer + 1 FC Layer<br><br>|Sigmoid|Adam<br><br>|CE|
|(Zhang et al., 2020e)<br><br>|DWT-Net<br><br>|8 2D-Conv Layers + 8 1D-Conv Layers + 4 Max Pooling Layers + 4 Dropout Layers + Concatenation + 3D- Conv Layer + Max Pooling Layer + 2 FC Layers + ReLu Activation Function|Softmax<br><br>|Adam<br><br>|Weighted Cross-Entropy|
|(Zhang et al., 2018)|1D-TCNN<br><br>|NA|NA<br><br>|NA|NA|
|(Zhao et al., 2020a)|BSDCNN<br><br>|5 Conv Blocks + 5 BN Layers + 2 FC Layers|Sigmoid<br><br>|NA|NA|
|(Daoud et al., 2018)<br><br>|1D-CNN|5 Conv Layers + 5 Max Pooling Layers + 1 FC Layer<br><br>|Softmax|Gradient Descent Algorithm|BCE|
|(Daoud et al., 2020)|DCNN<br><br>|4 Conv Layers + 3 Max Pooling Layers + 4 BN Layers + RELU Activation Function|NA<br><br>|NA<br><br>|NA|
|(Lu and Triesch, 2019)<br><br>|1D-CNN with Residual connections|5 Conv Layers + 3 Max Pooling Layers + 3 BN Layers + 4 Dropout Layers + 1 FC Layer<br><br>|Softmax|Adam<br><br>|NA|
|(Craley et al., 2019)<br><br>|1D-PGM-CNN|4 Conv Layers + 4 Max Pooling Layers + 1 FC Layer<br><br>|Softmax|Adam<br><br>|CE|
|(Wei et al., 2019)|1D-CNN<br><br>|5 Conv Layers + 5 Max Pooling Layers + 3 Dropout Layers + 1 FC Layer|Softmax|Adam<br><br>|NA|
|(Qin et al., 2020a)<br><br>|1D-CNN|3 Conv Layers + 2 Dilated Conv Layers + 3 Max Pooling Layers + 3 FC Layers + 3 Dropout Layers + ReLU Activation Function<br><br>|Softmax|Adam<br><br>|CE|
|(Meisel et al., 2019)|1D-CNN|4 Conv Layers + 2 Pooling Layers + 3 Dropout Layers<br><br>|Sigmoid|NA<br><br>|NA|

|(Zhang et al., 2020c)<br><br>|CNN<br><br>|1 Conv Layer + 1 Max Pooling Layer + ReLU Activation Function + de-Conv Layer|–<br><br>|Adam<br><br>|MSE|
|---|---|---|---|---|---|
| | |4 Conv Layers + 4 Max Pooling Layers + 2 FC Layers + 1 Dropout Layer + Attention Mechanism|Sigmoid<br><br>| |CE Multi-Class CE|
|(Yuvaraj et al., 2018)|1D-CNN<br><br>|5 Conv Layers + 5 Pooling Layers + 1 FC Layer|Softmax<br><br>|Adam|CE|
|(Abou Jaoude et al., 2020)<br><br>|CNN-BP|3 Conv Layers + 3 Max Pooling Layers + 3 Dropout Layers + 1 GC Layers|Sigmoid|Adam<br><br>|Log (CE)|
|(Fukumori et al., 2019)|LSTM GRU<br><br>|Reshape Layer + 4 LSTM/GRU + 1 FC Layer|Sigmoid<br><br>|NA|NA|
| |1D-CNN<br><br>|Primary Conv Layer + 4 Conv Layers + 4 Max Pooling Layers + 1 FC Layer|Sigmoid<br><br>|NA|NA|
|(Guha et al., 2020)|DNN<br><br>|5 Hidden Layers|NA<br><br>|NA|NA|
|(Kaziha and Bonny, 2020)<br><br>|1D-CNN|5 Conv Layers + 5 BN Layers + 5 Avg Pooling Layers + 2 FC Layers|Sigmoid|RMSprop<br><br>|NA|
|(Truong et al., 2020)|BCNN<br><br>|3 Conv Blocks + 2 FC Layers|Softmax<br><br>|ELBO|Negative of ELBO|
|(Zhao et al., 2020c)|1D-CNN<br><br>|4 Conv Layers + 3 Max Pooling Layers + 1 FC Layer|NA<br><br>|NA<br><br>|NA|
|(Boonyakitanont et al., 2020b)<br><br>|1D-CNN<br><br>|14 Conv Layers + 7 BN Layers + 7 Max Pooling Layers + 2 Dropout Layers + 2 FC Layers|Onset-offset Detection Method|NA<br><br>|NA|
|(Khalilpour et al., 2020)<br><br>|1D-CNN|2 Conv Layers + 2 Pooling Layers + 1 Dropout Layer + 1 FC Layer|Softmax<br><br>|NA|NA|
|(Zhao et al., 2020b)|1D-CNN<br><br>|3 Conv Layers + 3 BN Layers + 5 Dropout Layers + 3 Max Pooling Layers + 2 FC Layers|Softmax<br><br>|Adam<br><br>|CE|
|(Abiyev et al., 2020)|1D-CNN<br><br>|8 Conv Layers + 4 Pooling Layers + 1 Dropout Layer + 2 FC Layers<br><br>|Softmax|RMSprop<br><br>|Proposed Loss Function|
|(Pisano et al., 2020)|1D-CNN|4 Convolutional Units + 2 Pooling Layers + 1 FC Layer<br><br>|Softmax|SGD|NA|
|(Lu et al., 2020)<br><br>|DNN|16 Blocks with Residual Connections<br><br>|Softmax|NA<br><br>|NA|
|(Xu et al., 2020c)<br><br>|CNN|5 Conv Layers + 5 Max Pooling Layers + 1 Dropout Layer + 2 FC Layers<br><br>|Softmax|Adam<br><br>|BCE|
|(Lin et al., 2020)|Deep ConvNet<br><br>|5 Conv Layers + 5 Max Pooling Layers + 2 BN Layers + 2 FC Layers|Softmax<br><br>|NA|NA|
|(Jana et al., 2020)<br><br>|1D-CNN|3 Conv Layers + 3 BN Layers + 2 Pooling Layers + 1 Dropout Layer<br><br>|Softmax|NA<br><br>|NA|
|(Gao et al., 2020a)<br><br>|1D-CNN|2 Conv Layers + 2 Subsampling Layers + 2 FC Layers<br><br>|Gaussian Connection|Adam|BCE|
|(Thomas et al., 2020a)<br><br>|1D-CNN|2 Conv Layers + 1 Max Pooling Layer+ 2 FC Layers<br><br>|NA<br><br>|Adam<br><br>|NA|
|(Vance et al., 2020)|1D-CNN<br><br>|2 Conv Layers + 1 BN Layer + 1 DownSampling Layer + 5 Pre-Activation Residual Blocks + 1 MaxGlobal Pooling Layer|Sigmoid<br><br>|SGD|BCE|
|(Liu and Richardson, 2020)<br><br>|LSTM|1 Conv Layer + 1 Max Pooling Layer + 1 Dropout Layer + Bi LSTM Layer + 3 FC Layers<br><br>|Sliding WMV|NA|NA|
| |1D-CNN|3 Conv Layers + 3 Max Pooling Layers + 2 Dropout Layers + 3 FC Layers| | | |

|(Vidyaratne et al., 2016)|DRNN<br><br>|DRNN Layers|MLP with 2 Layers|Jacobian free Unscented Kalman filerbased parameter optimization method<br><br>|NA|
|---|---|---|---|---|---|
|(Hussein et al., 2018c)|LSTM|1 LSTM Layer + 1 Time Distributed Dense Layer + 1 Average Pooling Layer<br><br>|Softmax<br><br>|Adam|CCE|
|(Ahmedt-Aristizabal et al., 2018b)|LSTM|1 LSTM Layer + 1 Dropout Layer + 1 FC Layer<br><br>|Sigmoid<br><br>|Adam<br><br>|BCE|
| | |2 LSTM Layers + 2 Dropout Layers + 2 FC Layers| | | |
|(Yao et al., 2019b)|1D-CNN<br><br>|5 Conv Layers + 5 Max Pooling Layers + 3 FC Layers|NA<br><br>|Adam<br><br>|NA|
| |IndRNN<br><br>|15 IndRNN Layers+ 15 BN Layers + 15 Max Pooling Layers + 1 Average Pooling + 2 FC Layers|NA<br><br>|Adam<br><br>|NA|
| |LSTM|1 LSTM Layer + 1 Time Distributed Computing Layer + 1 Average Pooling layer + 1 FC Layer<br><br>|NA|Adam<br><br>|NA|
|(Verma and Janghel, 2021)<br><br>|RNN|2 GRU Layers + 1 FC Layer<br><br>|LR<br><br>|NA|NA|
|(Hussein et al., 2019)|LSTM|1 LSTM Layer + 1 Time Distributed FC Layer + 1 Average Pooling Layer<br><br>|Softmax|Adam<br><br>|CCE|
|(Jaafar and Mohammadi, 2019)<br><br>|LSTM|1 LSTM Layer + 1 Time Distributed FC Layer<br><br>|Softmax<br><br>|NA|NA|
|(Hu et al., 2020c)|Bi-LSTM|Bi-LSTM Layer + dropout Layer<br><br>|Softmax|Adam<br><br>|Cross Entropy|
|(Yao et al., 2019a)|ADIndRNN<br><br>|Attention Layer + 9 IndRNN Layers + 9 BN Layers+3 Max Pooling Layers+ 1 Avg Pooling Layers + 2 FC Layers<br><br>|NA|Adam<br><br>|NA|
|(Talathi, 2017)|GRU<br><br>|2 GRU Layers + 1 Time Distributed FC Layer<br><br>|LR<br><br>|Adam<br><br>|NA|
|(Roy et al., 2019)|GRU<br><br>|4 GRU Layers|Softmax<br><br>|Adam|NA|
| |C-RNN<br><br>|3 Conv Layers + 4 GRU Layers| | | |
| |IC-RNN<br><br>|9 Conv Layers + 4 GRU Layers| | | |
| |C-DRNN<br><br>|3 Conv Layers + 4 GRU Layers| | | |
| |ChronoNet<br><br>|9 Conv Layers + 4 GRU Layers| | | |
|(Hussein et al., 2018b)<br><br>|LSTM<br><br>|1 LSTM Layer + 1 FC Layer + 1 Max Pooling Layer<br><br>|Softmax<br><br>|SGD|CE|
|(Geng et al., 2020)<br><br>|Bi-LSTM<br><br>|1 Bi-LSTM Layer<br><br>|Softmax|Adam|NA|
|(Fraiwan and Alkhodari, 2020)<br><br>|Bi-LSTM<br><br>|1 LSTM Layer + 2 FC Layers<br><br>|Softmax<br><br>|Adam|NA|
|(Hu and Yuan, 2019)<br><br>|Bi-LSTM|Bi-LSTM Layer<br><br>|Softmax|Adagrad<br><br>|NA|
|(Abbasi et al., 2019)<br><br>|LSTM<br><br>|2 LSTM Layers + 2 Dropout Layers + FC Layer<br><br>|Softmax|Adam|NA|
|(Yao et al., 2021)<br><br>|Attention Bi-LSTM<br><br>|Attention Layer + Bi LSTM Layer + Time-Distributed Fully-Connected Layer + Global Average Pooling Layer + Fully Connected Layer|Softmax<br><br>|RMSprop|NA|
|(Patan and Rutkowski, 2021)|LSTM<br><br>|4 LSTM layers + 4 dropout layers + 1 FC Layer|Softmax<br><br>|Adam<br><br>|NA|
|(Rajaguru and Prabhakar, 2018)<br><br>|MAE|NA<br><br>|GA<br><br>|NA|NA|
|(Sharathappriyaa et al., 2018)|AE<br><br>|2 Hidden Layers|Softmax|NA|MSE|

|(Emami et al., 2019a)|AE<br><br>|1-layer AE consisting of an Encoder and a Decoder|Sigmoid<br><br>|Adam<br><br>|L2 Loss function|
|---|---|---|---|---|---|
|(Yuan et al., 2017)<br><br>|SSDA|2 hidden layers (intra channel) & 3 hidden layer (cross channel) + 2 FC layers<br><br>|Softmax<br><br>|NA|CE|
|(Qiu et al., 2018)<br><br>|DSAE|1 Hidden Layer<br><br>|LR|SGD<br><br>|NA|
|(Golmohammadi et al., 2019)<br><br>(Yan et al., 2016)<br><br>|SPSW-SDA<br><br>|Each Model has 3 Hidden Layers<br><br>Single Layer|LR<br><br>SVM|Mini Batch SGD<br><br>Batch Gradient Descent<br><br>|Cross Entropy<br><br>NA|
| |6W-SDA| | | | |
| |EYEM-SDA<br><br>SAE| | | | |
|(Lin et al., 2016)|SSAE<br><br>|3 Hidden Layers|Softmax|L-BFGS|Proposed Loss Function|
|(Yuan et al., 2019)<br><br>|Wave2Vec|SAE Layer<br><br>|Softmax|Adadelta<br><br>|CE|
| |SSDAE<br><br>|2 Hidden Layers|Softmax| | |
|(Gasparini et al., 2018)|SAE<br><br>|2 Hidden Layers|Softmax<br><br>|NA|NA|
|(Karim et al., 2018a)<br><br>|SSAE|2 Autoencoders<br><br>|Softmax|Taguchi Method| |
|(Karim et al., 2019)|DSAEs<br><br>|2 Autoencoders|Softmax<br><br>|NA|MSE|
|(Karim et al., 2018b)|SAE<br><br>|2 Autoencoders|Softmax<br><br>|NA<br><br>|NA|
|(Yuan et al., 2018c)<br><br>|SAEs<br><br>|2 Layers|Softmax<br><br>|Adam|CE|
|(Sharma et al., 2020)|SAE<br><br>|2 Hidden Layers|Softmax<br><br>|NA|Proposed Loss Function|
|(Siddharth et al., 2020)|SAE|2 Hidden Layers<br><br>|SVM|Proposed Optimization<br><br>|NA|
|(Le et al., 2018)<br><br>|DBN|1 Input Layer + 3 Hidden Layers + 1 Output Layer<br><br>|NA<br><br>|NA|NA|
|(Turner et al., 2017)|DBN<br><br>|1 Input Layer + 2 Hidden Layers + 1 Output Layer|LR|NA<br><br>|NA|
|(Tang et al., 2020)<br><br>|MV CNN-GRU|9 Conv Layers + 9 BN Layers + 6 Max Pooling Layers + ReLU Activation Function + Attention Layer + GRU Layer + 1 FC Layer|Softmax|NA|CE|
|(Thodoroff et al., 2016)<br><br>|2D-CNNLSTM|4 Conv Layers + 2 Pooling Layers + 1 LSTM Layer + 1FC Layer<br><br>|NA|RMSProp<br><br>|Gradient Descent (GD)|
|(Saqib et al., 2020)<br><br>|2D CNNLSTM|6 Conv Layer + 6 Max Pooling Layers + 6 BN Layers + ReLU activation function + LSTM Layer + FC Layer + Dropout Layer<br><br>|Softmax|Adam<br><br>|NA|
|(Choi et al., 2019)|3D-CNNBiGRU<br><br>|–|NA|Adam<br><br>|NA|
|(Liang et al., 2020)<br><br>|LRCN|10 Conv layers + 5 Max-pooling layers + 1 LSTM Layer<br><br>|Softmax<br><br>|Adam|NA|
|(Roy et al., 2018)|2D-CNN<br><br>|3 Conv Layers + 3 Max Pooling Layers + 1 FC Layer|Softmax|Adam<br><br>|NA|
| |1D-CNN<br><br>|5 Conv Layers| | | |
| |1D-CNN-RNN<br><br>|3 Conv Layers + 3 GRU Layers| | | |
| |TCNN-RNN|3 Conv Layers + 3 Max Pooling + 2 GRU + FC Layers| | | |

|(Golmohammadi et al., 2017)|2D-CNNBiLSTM<br><br>|3 2D-Conv Layers + 3 2D-Max Pooling layers + 1D-Conv Layer + 1D-Max Pooling Layer +2 Bi-LSTM<br><br>|Sigmoid|Adam<br><br>|MSE|
|---|---|---|---|---|---|
| |LSTM<br><br>|1 LSTM Layer<br><br>|LR|MSGD<br><br>|CE|
| |SdA|3 Hidden Layers|Sigmoid<br><br>|NA<br><br>|NA|
|(Li et al., 2020b)|FC-NLSTM<br><br>|3 Conv Layers + 2 Pooling Layers + 1 NLSTM Layer + 1 FC Layer<br><br>|Softmax<br><br>|Adam|CCE|
|(Liu et al., 2020b)|C-LSTM<br><br>|2 Conv Layers + 2 BN Layers + 2 Dropout Layers + 1 LSTM Layer + 2 FC Layers|Softmax<br><br>|Adam|NA|
|(Yang et al., 2021)|CNN-LSTM|3 Conv Layers + 3 BN Layers + 2 Max Pooling Layers + 4 Dropout Layers + 3 FC Layers + 1 LSTM Layer<br><br>|Sigmoid<br><br>|Adam|BCE|
|(Xu et al., 2020a)|1D CNNLSTM<br><br>|4 Conv Layers + 1 Pooling Layer + 1 Dropout Layer + 2 LSTM Layers + 3 FC Layers|Softmax<br><br>|NA<br><br>|NA|
|(Yuan et al., 2018b)|CNN-AE<br><br>|Encoder: 2 Conv Layers + 2 Pooling Layers, Decoder: 2 de-Conv Layers + 2 Unpooling Layers<br><br>|Softmax<br><br>|Adadelta|CE|
|(Wen and Zhang, 2018)|CNN-AE<br><br>|Encoder: 3 Conv Layers + 3 Pooling Layers + 1 FC Layer, Decoder: 1 FC Layer + 4 de-Conv Layers + 3 de-Pooling Layers<br><br>|Different Classifiers<br><br>|Adam<br><br>|Proposed Loss Function|
|(Abdelhameed et al., 2018)<br><br>|1D-CNN-AE|8 Conv Layers + 3 Max Pooling Layers + 12 BN Layers + 3 Up sampling Layers<br><br>|LSTM|Adam|BCE<br><br>|
| | | |Bi-LSTM| | |
| | | |MLP|Adadelta<br><br>|MSE|
|(Antoniades et al., 2018)|CNN-ASAE|4 Conv Layers + 2 FC layers + 2 ASAE Hidden layers<br><br>|LR<br><br>|SGD<br><br>|CE|
| |CNN-AAE<br><br>|4 Conv Layers + 2 FC layers + 1 AAE Hidden layer| | | |
|(Yuan and Jia, 2019)|CNN-AE<br><br>|16 Conv Layers + 15 Pooling Layers<br><br>|Softmax|Adadelta<br><br>|CE|
|(Daoud and Bayoumi, 2019)|DCAE|Encoder: 2 Conv Layers + 2 Pooling Layers + 2BN Layers, Decoder: 2 de-Conv Layers + 2 Upsamplign Layers + 2 BN Layers<br><br>|MLP|RMSprop<br><br>|MSE|
| |DCVAE<br><br>|Encoder: 4 Conv Layers + 4 Pooling Layers + 4 BN Layers 2 FC Layers, Probabilistic Model Parameter Layer Decoder: 2 FC Layers + 4 de-Conv Layers + 4 Upsampling Layers + 4 BN Layers<br><br>|K-means clustering<br><br>|RMSprop|BCE|
|(Shoeibi et al., 2021)<br><br>|CNN-AE|5 Conv Layers + 4 Pooling Layers + 3 BN Layers + 1 Dropout Layer<br><br>|Softmax|Adadelta, SGD|NA|
|(Takahashi et al., 2020)<br><br>|CNN-AE|1 AE Layer + VGG16|Softmax<br><br>|NA<br><br>|NA|
|(Dev et al., 2019)<br><br>|FCN|15 Conv Layers + 7 BN Layers + 3 Max Pooling Layers + 3 de-Conv Layers+ 1 Dropout Layer<br><br>|Sigmoid|Adam<br><br>|Combination of BCE and the Dice Loss|
|(Gill et al., 2018)|Two-Stage CNNx Cascade<br><br>|3 Conv Layers + 2 BN Layers + 3 Max Pooling Layers + 1 Dropout Layer|Softmax<br><br>|Adadelta<br><br>|BCE|
|(Hao et al., 2018)<br><br>|ResNet<br><br>|29 Conv Layers + 1 Dropout Layer + 1 FC Layer<br><br>|Softmax|NA<br><br>|NA|
| | | |Triplet| | |
|(Hosseini et al., 2017)<br><br>|2D-CNN|NA<br><br>|SVM|NA<br><br>|NA|
|(Yan et al., 2018)<br><br>|2D-CNN<br><br>|5 Conv Layers + 3 Max Pooling Layers + 1 BN Layer + 1 FC Layer<br><br>|Softmax|Adam<br><br>|NA|
| |3D-CNN<br><br>|5 Conv Layers + 3 Max Pooling Layers + 1 BN Layer + 1 FC Layer| | | |

|(Gleichgerrcht et al., 2018)<br><br>|2D-CNN|Proposed Architecture<br><br>|NA|NA<br><br>|NA|
|---|---|---|---|---|---|
|(Jiang et al., 2019a)<br><br>|Combination of ResNet50, VGG16, Inception-V3, SVGG-C3D<br><br>|VGG16 + Global Average Pooling 2D Layer<br><br>|Different DL Layers<br><br>|RMSprop|CE|
| | |ResNet50 + Global Average Pooling 2D Layer| | | |
| | |Inception-V3 + Global Average Pooling 2D Layer| | | |
| | |SVGG-C3D + Global Average Pooling 2D Layer| | | |
|(Shiri et al., 2019)<br><br>|Deep-DAC<br><br>|9 Conv Layers + 11 BN Layers + 3 Max Pooling Layers +3 De-Conv Layers + 3 Dropout Layers|Tanh<br><br>|Adam<br><br>|MSE|
|(Wang et al., 2020a)<br><br>|CNN|5 Convolutional Layers + 5 BN Layers + 1 Max Pooling Layer + 1 Dropout Layer + 2 FC Layers<br><br>|Softmax|SGDM<br><br>|CE|
|(Shakeri et al., 2016)|FCN<br><br>|7 Conv Layers + 7 holes + 5 Pooling Layers + 4 Dropout (0.5)|Softmax<br><br>|SGD<br><br>|Softmax loss|
|(Figini et al., 2020)<br><br>|Aniso-U-Net<br><br>|Proposed U-Net Architecture|–|–<br><br>|mean voxel-wise square error (MVWSE)|
|(Pominova et al., 2018)<br><br>|VoxCNN-B|4 Volumetric Convolutional Blocks + 4 Max Pooling Layers + 2 FC Layers + 1 Dropout Layer<br><br>|Softmax|Adam|CE|
|(Xu et al., 2019)<br><br>|DCNN-CL-ATT<br><br>|1 Conv Layer + 1 BN Layer + 1 Max Pooling Layer + 4 ResBlocks + 1 Avg Pooling + 1 FC Layer + Dropout Layers + 4 Attention Units<br><br>|Softmax|Adam<br><br>|Focal loss, Center loss|
|(Torres-Vela´zquez et al., 2020)|mDNN<br><br>|5 Parallel Neural Network Blocks + 1 Additional Neural Network Block + 2 Concatenation Blocks<br><br>|Output Layer<br><br>|Adam|BCE|
|(Rebsamen et al., 2020)<br><br>|3D-CNN<br><br>|3 Conv Layers + 3 Max Pooling Layers + 2 Dropout (0.4) + 3 FC Layers + ReLU Activation Function<br><br>|–|Adam<br><br>|MSE|
|(Si et al., 2020)<br><br>|Inception<br><br>ResNet v2<br><br>|Modified Version<br><br>|Softmax|Adam<br><br>|CE|
|(Huang et al., 2020)<br><br>|CNN|VGG16<br><br>|SVM|NA<br><br>|NA|
|(Lee et al., 2020)<br><br>|DCNN<br><br>|ResNet 18<br><br>|Softmax<br><br>|Adam|Proposed Loss|

## References

Aarabi, A., Fazel-Rezai, R., and Aghakhani, Y. (2009). A fuzzy rule-based system for epileptic seizure detection in intracranial eeg. Clinical Neurophysiology, 120(9):1648–1657.

Abbasi, B. and Goldenholz, D. M. (2019). Machine learning applications in epilepsy. Epilepsia, 60(10):2037–2047.

Abbasi, M. U., Rashad, A., Basalamah, A., and Tariq, M. (2019). Detection of epilepsy seizures in neo-natal eeg using lstm architecture. IEEE Access, 7:179074–179085.

Abdelfattah, S. M., Abdelrahman, G. M., and Wang, M. (2018). Augmenting the size of eeg datasets using generative adversarial networks. In 2018 International Joint Conference on Neural Networks (IJCNN), pages 1–6. IEEE.

Abdelhameed, A. M., Daoud, H. G., and Bayoumi, M. (2018). Epileptic seizure detection using deep convolutional autoencoder. In 2018 IEEE International Workshop on Signal Processing Systems (SiPS), pages 223–228. IEEE.

Abibullaev, B., Seo, H. D., and Kim, M. S. (2010). Epileptic spike detection using continuous wavelet transforms and artiﬁcial neural networks. International journal of wavelets, multiresolution and information processing, 8(01):33–48.

Abiyev, R., Arslan, M., Idoko, J. B., Sekeroglu, B., and Ilhan, A. (2020). Identiﬁcation of epileptic eeg signals using convolutional neural networks. Applied Sciences, 10(12):4089.

Abou Jaoude, M., Jing, J., Sun, H., Jacobs, C. S., Pellerin, K. R., Westover, M. B., Cash, S. S., and Lam, A. D. (2020). Detection of mesial temporal lobe epileptiform discharges on intracranial electrodes using deep learning. Clinical Neurophysiology, 131(1):133–141.

Abramovici, S. and Bagic´, A. (2016). Epidemiology of epilepsy. Handbook of clinical neurology, 138:159–171.

Acharya, U. R., Oh, S. L., Hagiwara, Y., Tan, J. H., and Adeli, H. (2018). Deep convolutional neural network for the automated detection and diagnosis of seizure using eeg signals. Computers in biology and medicine, 100:270–278.

Acharya, U. R., Sree, S. V., Swapna, G., Martis, R. J., and Suri, J. S. (2013). Automated eeg analysis of epilepsy: a review. Knowledge-Based Systems, 45:147–165.

Achilles, F., Tombari, F., Belagiannis, V., Loesch, A. M., Noachtar, S., and Navab, N. (2018). Convolutional neural networks for real-time epileptic seizure detection. Computer Methods in Biomechanics and Biomedical Engineering: Imaging & Visualization, 6(3):264–269.

Ahmedt-Aristizabal, D., Fookes, C., Nguyen, K., Denman, S., Sridharan, S., and Dionisio, S. (2018a). Deep facial analysis: A new phase i epilepsy evaluation using computer vision. Epilepsy & Behavior, 82:17–24.

Ahmedt-Aristizabal, D., Fookes, C., Nguyen, K., and Sridharan, S. (2018b). Deep classiﬁcation of epileptic signals. In 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pages 332–335. IEEE.

Akut, R. (2019). Wavelet based deep learning approach for epilepsy detection. Health information science and systems, 7(1):1–9.

Akyol, K. (2020). Stacking ensemble based deep neural networks modeling for eﬀective epileptic seizure detection. Expert Systems with Applications, 148:113239.

Alam, S. S. and Bhuiyan, M. I. H. (2013). Detection of seizure and epilepsy using higher order statistics in the emd domain. IEEE journal of biomedical and health informatics, 17(2):312–318.

Alhussein, M., Muhammad, G., Hossain, M. S., and Amin, S. U. (2018). Cognitive iot-cloud integration for smart healthcare: case study for epileptic seizure detection and monitoring. Mobile Networks and Applications, 23(6):1624– 1635.

Ali, Z. S., Subramanian, N., and Erbad, A. (2020). Smart health monitoring for seizure detection using mobile edge computing. In 2020 International Wireless Communications and Mobile Computing (IWCMC), pages 1903–1908. IEEE.

Alizadehsani, R., Sharifrazi, D., Izadi, N. H., Joloudari, J. H., Shoeibi, A., Gorriz, J. M., Hussain, S., Arco, J. E., Sani, Z. A., Khozeimeh, F., et al. (2021). Uncertainty-aware semi-supervised method using large unlabelled and limited labeled covid-19 data. arXiv preprint arXiv:2102.06388.

Amin, S. U., Hossain, M. S., Muhammad, G., Alhussein, M., and Rahman, M. A.

(2019). Cognitive smart healthcare for pathology detection and monitoring. IEEE Access, 7:10745–10753.

Andrzejak, R. G., Lehnertz, K., Mormann, F., Rieke, C., David, P., and Elger, C. E. (2001). Indications of nonlinear deterministic and ﬁnite-dimensional structures in time series of brain electrical activity: Dependence on recording region and brain state. Physical Review E, 64(6):061907.

Andrzejak, R. G., Schindler, K., and Rummel, C. (2012). Nonrandomness, nonlinear dependence, and nonstationarity of electroencephalographic recordings from epilepsy patients. Physical Review E, 86(4):046206.

Ansari, A. H., Cherian, P. J., Caicedo, A., Naulaers, G., De Vos, M., and Van Huﬀel, S. (2019). Neonatal seizure detection using deep convolutional neural networks. International journal of neural systems, 29(04):1850011.

Antoniades, A., Spyrou, L., Martin-Lopez, D., Valentin, A., Alarcon, G., Sanei, S., and Took, C. C. (2018). Deep neural architectures for mapping scalp to intracranial eeg. International journal of neural systems, 28(08):1850009.

Antoniades, A., Spyrou, L., Took, C. C., and Sanei, S. (2016). Deep learning for epileptic intracranial eeg data. In 2016 IEEE 26th International Workshop on Machine Learning for Signal Processing (MLSP), pages 1–6. IEEE.

Asif, U., Roy, S., Tang, J., and Harrer, S. (2019). Seizurenet: a deep convolutional neural network for accurate seizure type classiﬁcation and seizure detection. arXiv preprint arXiv:1903.03232.

Assi, E. B., Nguyen, D. K., Rihana, S., and Sawan, M. (2017). Towards accurate prediction of epileptic seizures: A review. Biomedical Signal Processing and Control, 34:144–157.

Avcu, M. T., Zhang, Z., and Chan, D. W. S. (2019). Seizure detection using least eeg channels by deep convolutional neural network. In ICASSP 20192019 IEEE international conference on acoustics, speech and signal processing (ICASSP), pages 1120–1124. IEEE.

Ballester, P. and Araujo, R. (2016). On the performance of googlenet and alexnet applied to sketches. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence, volume 30.

Bank, D., Koenigstein, N., and Giryes, R. (2020). Autoencoders. arXiv preprint arXiv:2003.05991.

Bao, Y., He, R., Zeng, Q., Zhu, P., Zheng, R., and Xu, H. (2018). Investigation of microstructural abnormalities in white and gray matter around hippocampus with diﬀusion tensor imaging (dti) in temporal lobe epilepsy (tle). Epilepsy & Behavior, 83:44–49.

Behroozi, M., Daliri, M. R., and Boyaci, H. (2011). Statistical analysis methods for the fmri data. Basic and Clinical Neuroscience, 2(4):67–74.

Bell, M. L., Rao, S., So, E. L., Trenerry, M., Kazemi, N., Matt Stead, S., Cascino, G., Marsh, R., Meyer, F. B., Watson, R. E., et al. (2009). Epilepsy surgery outcomes in temporal lobe epilepsy with a normal mri. Epilepsia, 50(9):2053–2060.

Bhagat, P. N., Ramesh, K., Matcha, V. G. R., and Patil, S. (2020). Robust prior stage epileptic seizure diagnosis system using resnet and backpropagation techniques. International Journal, 8(5).

Bharath, R. D., Panda, R., Raj, J., Bhardwaj, S., Sinha, S., Chaitanya, G., Raghavendra, K., Mundlamuri, R. C., Arimappamagan, A., Rao, M. B., et al. (2019). Machine learning identiﬁes “rsfmri epilepsy networks” in temporal lobe epilepsy. European radiology, 29(7):3496–3505.

Bhattacherjee, I. (2020). Epileptic seizure detection using multicolumn convolutional neural network. In 2020 7th International Conference on Computing for Sustainable Global Development (INDIACom), pages 58–63. IEEE.

Bird, J. J., Faria, D. R., Manso, L. J., Ayrosa, P. P., and Ekart, A. (2021). A study on cnn image classiﬁcation of eeg signals represented in 2d and 3d. Journal of Neural Engineering, 18(2):026005.

Birjandtalab, J., Pouyan, M. B., Cogan, D., Nourani, M., and Harvey, J. (2017). Automated seizure detection using limited-channel eeg and non-linear dimension reduction. Computers in biology and medicine, 82:49–58.

Bizopoulos, P., Lambrou, G. I., and Koutsouris, D. (2019). Signal2image modules in deep neural networks for eeg classiﬁcation. In 2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pages 702–705. IEEE.

Boonyakitanont, P., Lek-uthai, A., Chomtho, K., and Songsiri, J. (2019). A comparison of deep neural networks for seizure detection in eeg signals. bioRxiv, page 702654.

Boonyakitanont, P., Lek-Uthai, A., Chomtho, K., and Songsiri, J. (2020a). A review of feature extraction and performance evaluation in epileptic seizure detection using eeg. Biomedical Signal Processing and Control, 57:101702.

Boonyakitanont, P., Lek-uthai, A., and Songsiri, J. (2020b). Automatic epileptic seizure onset-oﬀset detection based on cnn in scalp eeg. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 1225–1229. IEEE.

Boran, E., Sarnthein, J., Krayenbu¨hl, N., Ramantani, G., and Fedele, T. (2019). High-frequency oscillations in scalp eeg mirror seizure frequency in pediatric focal epilepsy. Scientiﬁc reports, 9(1):1–10.

Bouallegue, G., Djemal, R., Alshebeili, S. A., and Aldhalaan, H. (2020). A dynamic ﬁltering df-rnn deep-learning-based approach for eeg-based neurological disorders diagnosis. IEEE Access, 8:206992–207007.

Bouaziz, B., Chaari, L., Batatia, H., and Quintero-Rinc´n, A. (2019). Epileptic seizure detection using a convolutional neural network. In Digital Health Approach for Predictive, Preventive, Personalised and Participatory Medicine, pages 79–86. Springer.

Burda, Y., Grosse, R., and Salakhutdinov, R. (2015). Importance weighted autoencoders. arXiv preprint arXiv:1509.00519.

Cao, J., Zhu, J., Hu, W., and Kummert, A. (2019). Epileptic signal classiﬁcation with deep eeg features by stacked cnns. IEEE Transactions on Cognitive and Developmental Systems, 12(4):709–722.

Centeno, M. and Carmichael, D. W. (2014). Network connectivity in epilepsy: resting state fmri and eeg–fmri contributions. Frontiers in neurology, 5:93.

Cerulli Irelli, E., Morano, A., Cocchi, E., Casciato, S., Fanella, M., Albini, M., Avorio, F., Basili, L. M., Fisco, G., Barone, F. A., et al. (2020). Doing without valproate in women of childbearing potential with idiopathic generalized epilepsy: Implications on seizure outcome. Epilepsia, 61(1):107–114.

Chapman, K., Wyllie, E., Najm, I., Ruggieri, P., Bingaman, W., Lu¨ders, J., Kotagal, P., Lachhwani, D., Dinner, D., and L¨uders, H. (2005). Seizure outcome after epilepsy surgery in patients with normal preoperative mri. Journal of Neurology, Neurosurgery & Psychiatry, 76(5):710–713.

Chatzichristos, C., Dan, J., Narayanan, A. M., Seeuws, N., Vandecasteele, K., De Vos, M., Bertrand, A., and Van Huﬀel, S. (2020). Epileptic seizure detection in eeg via fusion of multi-view attention-gated u-net deep neural networks. In Proceedings of the IEEE Signal Processing in Medicine and Biology Symposium (SPMB), page 7.

Chen, M., Shi, X., Zhang, Y., Wu, D., and Guizani, M. (2017a). Deep features learning for medical image analysis with convolutional autoencoder neural network. IEEE Transactions on Big Data.

Chen, X., Ji, J., Ji, T., and Li, P. (2018). Cost-sensitive deep active learning for epileptic seizure detection. In Proceedings of the 2018 ACM International

Conference on Bioinformatics, Computational Biology, and Health Informatics, pages 226–235.

Chen, Z., Huang, L., Shen, Y., Wang, J., Zhao, R., and Dai, J. (2017b). A new algorithm for classiﬁcation of ictal and pre-ictal epilepsy ecog using mi and svm. In 2017 International Conference on Signals and Systems (ICSigSys), pages 212–216. IEEE.

Cho, K.-O. and Jang, H.-J. (2020). Comparison of diﬀerent input modalities and network structures for deep learning-based seizure detection. Scientiﬁc reports, 10(1):1–11.

Choi, G., Park, C., Kim, J., Cho, K., Kim, T.-J., Bae, H., Min, K., Jung, K.-Y., and Chong, J. (2019). A novel multi-scale 3d cnn with deep neural network for epileptic seizure detection. In 2019 IEEE International Conference on Consumer Electronics (ICCE), pages 1–2. IEEE.

Clarke, S., Karoly, P. J., Nurse, E., Seneviratne, U., Taylor, J., Knight-Sadler, R., Kerr, R., Moore, B., Hennessy, P., Mendis, D., et al. (2019). Computerassisted eeg diagnostic review for idiopathic generalized epilepsy. Epilepsy & Behavior, page 106556.

Colon, A., van Osch, M., Buijs, M., Grond, J., Hillebrand, A., Schijns, O., Wagner, G., Ossenblok, P., Hofman, P., Buchem, M., et al. (2018). Megguided analysis of 7t-mri in patients with epilepsy. Seizure, 60:29–38.

Covert, I. C., Krishnan, B., Najm, I., Zhan, J., Shore, M., Hixson, J., and Po, M. J. (2019). Temporal graph convolutional networks for automatic seizure detection. In Machine Learning for Healthcare Conference, pages 160–180. PMLR.

Craley, J., Johnson, E., and Venkataraman, A. (2019). Integrating convolutional neural networks and probabilistic graphical modeling for epileptic seizure detection in multichannel eeg. In International Conference on Information Processing in Medical Imaging, pages 291–303. Springer.

Daoud, H. and Bayoumi, M. (2019). Deep learning approach for epileptic focus localization. IEEE transactions on biomedical circuits and systems, 14(2):209– 220.

Daoud, H., Williams, P., and Bayoumi, M. (2020). Iot based eﬃcient epileptic seizure prediction system using deep learning. In 2020 IEEE 6th World Forum on Internet of Things (WF-IoT), pages 1–6. IEEE.

Daoud, H. G., Abdelhameed, A. M., and Bayoumi, M. (2018). Automatic epileptic seizure detection based on empirical mode decomposition and deep neural network. In 2018 IEEE 14th International Colloquium on Signal Processing & Its Applications (CSPA), pages 182–186. IEEE.

Dash, S., Acharya, B. R., Mittal, M., Abraham, A., and Kelemen, A. G. (2020). Deep learning techniques for biomedical and health informatics. Springer.

Del Gaizo, J., Mofrad, N., Jensen, J. H., Clark, D., Glenn, R., Helpern, J., and Bonilha, L. (2017). Using machine learning to classify temporal lobe epilepsy based on diﬀusion mri. Brain and behavior, 7(10):e00801.

Dev, K. B., Jogi, P. S., Niyas, S., Vinayagamani, S., Kesavadas, C., and Rajan, J. (2019). Automatic detection and localization of focal cortical dysplasia lesions in mri using fully convolutional neural network. Biomedical Signal Processing and Control, 52:218–225.

Dey, N. (2016). Classiﬁcation and clustering in biomedical signal processing. IGI global.

Dhull, S. K., Singh, K. K., et al. (2021). A review on automatic epilepsy detection from eeg signals. In Advances in Communication and Computational Technology, pages 1441–1454. Springer.

Duncan, J. S., Sander, J. W., Sisodiya, S. M., and Walker, M. C. (2006). Adult epilepsy. The Lancet, 367(9516):1087–1100.

Ebrahimzadeh, E., Shams, M., Fayaz, F., Rajabion, L., Mirbagheri, M., Araabi, B. N., and Soltanian-Zadeh, H. (2019). Quantitative determination of concordance in localizing epileptic focus by component-based eeg-fmri. Computer methods and programs in biomedicine, 177:231–241.

El Tahry, R., Wang, Z. I., Thandar, A., Podkorytova, I., Krishnan, B., Tousseyn, S., Guiyun, W., Burgess, R. C., and Alexopoulos, A. V. (2018). Magnetoen-

cephalography and ictal spect in patients with failed epilepsy surgery. Clinical Neurophysiology, 129(8):1651–1657.

Emami, A., Kunii, N., Matsuo, T., Shinozaki, T., Kawai, K., and Takahashi, H. (2019a). Autoencoding of long-term scalp electroencephalogram to detect epileptic seizure for diagnosis support system. Computers in biology and medicine, 110:227–233.

Emami, A., Kunii, N., Matsuo, T., Shinozaki, T., Kawai, K., and Takahashi, H. (2019b). Seizure detection by convolutional neural network-based analysis of scalp electroencephalography plot images. NeuroImage: Clinical, 22:101684.

Fan, M. and Chou, C.-A. (2018). Detecting abnormal pattern of epileptic seizures via temporal synchronization of eeg signals. IEEE Transactions on Biomedical Engineering, 66(3):601–608.

Fergus, P., Hignett, D., Hussain, A., Al-Jumeily, D., and Abdel-Aziz, K. (2015). Automatic epileptic seizure detection using scalp eeg and advanced artiﬁcial intelligence techniques. BioMed research international, 2015.

Figini, M., Lin, H., Ogbole, G., Arco, F. D., Blumberg, S. B., Carmichael, D. W., Tanno, R., Kaden, E., Brown, B. J., Lagunju, I., et al. (2020). Image quality transfer enhances contrast and resolution of low-ﬁeld brain mri in african paediatric epilepsy patients. arXiv preprint arXiv:2003.07216.

Fisher, R. S. (2012). Therapeutic devices for epilepsy. Annals of neurology, 71(2):157–168.

Fraiwan, L. and Alkhodari, M. (2020). Classiﬁcation of focal and non-focal epileptic patients using single channel eeg and long short-term memory learning system. IEEE Access, 8:77255–77262.

Frauscher, B. and Gotman, J. (2019). Sleep, oscillations, interictal discharges, and seizures in human focal epilepsy. Neurobiology of disease, 127:545–553.

Fukumori, K., Nguyen, H. T. T., Yoshida, N., and Tanaka, T. (2019). Fully data-driven convolutional ﬁlters with deep learning models for epileptic spike detection. In ICASSP 2019-2019 IEEE international conference on acoustics, speech and signal processing (ICASSP), pages 2772–2776. IEEE.

Gaillard, W. D., Balsamo, L., Xu, B., Grandin, C., Braniecki, S., Papero, P., Weinstein, S., Conry, J., Pearl, P., Sachs, B., et al. (2002). Language dominance in partial epilepsy patients identiﬁed with an fmri reading task. Neurology, 59(2):256–265.

Gao, J., Sultan, H., Hu, J., and Tung, W.-W. (2009). Denoising nonlinear time series by adaptive ﬁltering and wavelet shrinkage: a comparison. IEEE signal processing letters, 17(3):237–240.

- Gao, X., Yan, X., Gao, P., Gao, X., and Zhang, S. (2020a). Automatic detection of epileptic seizure based on approximate entropy, recurrence quantiﬁcation analysis and convolutional neural networks. Artiﬁcial intelligence in medicine, 102:101711.
- Gao, Y., Gao, B., Chen, Q., Liu, J., and Zhang, Y. (2020b). Deep convolutional neural network-based epileptic electroencephalogram (eeg) signal classiﬁcation. Frontiers in neurology, 11.

Garner, R., La Rocca, M., Barisano, G., Toga, A. W., Duncan, D., and Vespa, P. (2019). A machine learning model to predict seizure susceptibility from resting-state fmri connectivity. In 2019 Spring Simulation Conference (SpringSim), pages 1–11. IEEE.

Gasparini, S., Campolo, M., Ieracitano, C., Mammone, N., Ferlazzo, E., Sueri, C., Tripodi, G. G., Aguglia, U., and Morabito, F. C. (2018). Information theoretic-based interpretation of a deep neural network approach in diagnosing psychogenic non-epileptic seizures. Entropy, 20(2):43.

Geng, M., Zhou, W., Liu, G., Li, C., and Zhang, Y. (2020). Epileptic seizure detection based on stockwell transform and bidirectional long short-term memory. Ieee Transactions on Neural Systems and Rehabilitation Engineering, 28(3):573–580.

George, F., Joseph, A., Baby, B., John, A., John, T., Deepak, M., Nithin, G., and Sathidevi, P. (2020). Epileptic seizure prediction using eeg images. In 2020 International Conference on Communication and Signal Processing (ICCSP), pages 1595–1598. IEEE.

Ghassemi, N., Shoeibi, A., and Rouhani, M. (2020). Deep neural network with generative adversarial networks pre-training for brain tumor classiﬁcation based on mr images. Biomedical Signal Processing and Control, 57:101678.

Ghiasi, G., Cui, Y., Srinivas, A., Qian, R., Lin, T.-Y., Cubuk, E. D., Le, Q. V., and Zoph, B. (2020). Simple copy-paste is a strong data augmentation method for instance segmentation. arXiv preprint arXiv:2012.07177.

Gill, R. S., Hong, S.-J., Fadaie, F., Caldairou, B., Bernhardt, B. C., Barba, C., Brandt, A., Coelho, V. C., d’Incerti, L., Lenge, M., et al. (2018). Deep convolutional networks for automated detection of epileptogenic brain malformations. In International Conference on Medical Image Computing and Computer-Assisted Intervention, pages 490–497. Springer.

Giudice, M. L., Varone, G., Ieracitano, C., Mammone, N., Bruna, A. R., Tomaselli, V., and Morabito, F. C. (2020). 1d convolutional neural network approach to classify voluntary eye blinks in eeg signals for bci applications. In 2020 International Joint Conference on Neural Networks (IJCNN), pages 1–7. IEEE.

Gleichgerrcht, E., Munsell, B., Bhatia, S., Vandergrift III, W. A., Rorden, C., McDonald, C., Edwards, J., Kuzniecky, R., and Bonilha, L. (2018). Deep learning applied to whole-brain connectome to determine seizure control after epilepsy surgery. Epilepsia, 59(9):1643–1654.

Gloor, P. and Fariello, R. (1988). Generalized epilepsy: some of its cellular mechanisms diﬀer from those of focal epilepsy. Trends in neurosciences, 11(2):63– 68.

Glory, H. A., Vigneswaran, C., Jagtap, S. S., Shruthi, R., Hariharan, G., and Sriram, V. S. (2020). Ahw-bgoa-dnn: a novel deep learning model for epileptic seizure detection. Neural Computing and Applications, pages 1–29.

Golmohammadi, M., Harati Nejad Torbati, A. H., Lopez de Diego, S., Obeid, I., and Picone, J. (2019). Automatic analysis of eegs using big data and hybrid deep learning architectures. Frontiers in human neuroscience, 13:76.

Golmohammadi, M., Ziyabari, S., Shah, V., de Diego, S. L., Obeid, I., and Picone, J. (2017). Deep architectures for automated seizure detection in scalp eegs. arXiv preprint arXiv:1712.09776.

Goodfellow, I., Bengio, Y., Courville, A., and Bengio, Y. (2016). Deep learning, volume 1. MIT press Cambridge.

Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., and Bengio, Y. (2014). Generative adversarial networks. arXiv preprint arXiv:1406.2661.

Gotman, J. (2008). Epileptic networks studied with eeg-fmri. Epilepsia, 49:42– 51.

Guevara, E., Flores-Castro, J.-A., Peng, K., Nguyen, D. K., Lesage, F., Pouliot, P., and Rosas-Romero, R. (2020). Prediction of epileptic seizures using fnirs and machine learning. Journal of Intelligent & Fuzzy Systems, 38(2):2055– 2068.

Guha, A., Ghosh, S., Roy, A., and Chatterjee, S. (2020). Epileptic seizure recognition using deep neural network. In Emerging Technology in Modelling and Graphics, pages 21–28. Springer.

Gupta, V., Bhattacharyya, A., and Pachori, R. B. (2020). Automated identiﬁcation of epileptic seizures from eeg signals using fbse-ewt method. In Biomedical Signal Processing, pages 157–179. Springer.

Hao, Y., Khoo, H. M., von Ellenrieder, N., Zazubovits, N., and Gotman, J.

(2018). Deepied: An epileptic discharge detector for eeg-fmri based on deep learning. NeuroImage: Clinical, 17:962–975.

Hartmann, K. G., Schirrmeister, R. T., and Ball, T. (2018). Eeg-gan: Generative adversarial networks for electroencephalograhic (eeg) brain signals. arXiv preprint arXiv:1806.01875.

Hazra, D. and Byun, Y.-C. (2020). Synsiggan: Generative adversarial networks for synthetic biomedical signal generation. Biology, 9(12):441.

Hinton, G. E. (2009). Deep belief networks. Scholarpedia, 4(5):5947.

Holden, D., Saito, J., Komura, T., and Joyce, T. (2015). Learning motion manifolds with convolutional autoencoders. In SIGGRAPH Asia 2015 Technical Briefs, pages 1–4.

Hossain, M. S., Amin, S. U., Alsulaiman, M., and Muhammad, G. (2019). Applying deep learning for epilepsy seizure detection and brain mapping visualization. ACM Transactions on Multimedia Computing, Communications, and Applications (TOMM), 15(1s):1–17.

Hosseini, M.-P., Soltanian-Zadeh, H., Elisevich, K., and Pompili, D. (2016). Cloud-based deep learning of big eeg data for epileptic seizure prediction. In 2016 IEEE global conference on signal and information processing (GlobalSIP), pages 1151–1155. IEEE.

Hosseini, M.-P., Tran, T. X., Pompili, D., Elisevich, K., and Soltanian-Zadeh, H. (2017). Deep learning with edge computing for localization of epileptogenicity using multimodal rs-fmri and eeg big data. In 2017 IEEE international conference on autonomic computing (ICAC), pages 83–92. IEEE.

Hsu, K.-Y., Li, H.-Y., and Psaltis, D. (1990). Holographic implementation of a fully connected neural network. Proceedings of the IEEE, 78(10):1637–1645.

- Hu, D., Cao, J., Lai, X., Wang, Y., Wang, S., and Ding, Y. (2020a). Epileptic state classiﬁcation by fusing hand-crafted and deep learning eeg features. IEEE Transactions on Circuits and Systems II: Express Briefs.
- Hu, D., Cao, J., Lai, X., Wang, Y., Wang, S., and Ding, Y. (2020b). Epileptic state classiﬁcation by fusing hand-crafted and deep learning eeg features. IEEE Transactions on Circuits and Systems II: Express Briefs.

Hu, X. and Yuan, Q. (2019). Epileptic eeg identiﬁcation based on deep bi-lstm network. In 2019 IEEE 11th International Conference on Advanced Infocomm Technology (ICAIT), pages 63–66. IEEE.

Hu, X., Yuan, S., Xu, F., Leng, Y., Yuan, K., and Yuan, Q. (2020c). Scalp eeg classiﬁcation using deep bi-lstm network for seizure detection. Computers in Biology and Medicine, 124:103919.

Huang, J., Xu, J., Kang, L., and Zhang, T. (2020). Identifying epilepsy based on deep learning using dki images. Frontiers in Human Neuroscience, 14:465.

Hussein, A. F., Arunkumar, N., Gomes, C., Alzubaidi, A. K., Habash, Q. A., Santamaria-Granados, L., Mendoza-Moreno, J. F., and Ramirez-Gonzalez, G. (2018a). Focal and non-focal epilepsy localization: A review. IEEE Access, 6:49306–49324.

Hussein, R., Lee, S., Ward, R., and McKeown, M. J. (2020). Epileptic seizure prediction: A semi-dilated convolutional neural network architecture. arXiv preprint arXiv:2007.11716.

Hussein, R., Palangi, H., Wang, Z. J., and Ward, R. (2018b). Robust detection of epileptic seizures using deep neural networks. In 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 2546–2550. IEEE.

Hussein, R., Palangi, H., Ward, R., and Wang, Z. J. (2018c). Epileptic seizure detection: A deep learning approach. arXiv preprint arXiv:1803.09848.

Hussein, R., Palangi, H., Ward, R. K., and Wang, Z. J. (2019). Optimized deep neural network architecture for robust detection of epileptic seizures using eeg signals. Clinical Neurophysiology, 130(1):25–37.

Iandola, F. N., Han, S., Moskewicz, M. W., Ashraf, K., Dally, W. J., and Keutzer, K. (2016). Squeezenet: Alexnet-level accuracy with 50x fewer parameters and¡ 0.5 mb model size. arXiv preprint arXiv:1602.07360.

Iasemidis, L. D. (2003). Epileptic seizure prediction and control. IEEE Transactions on Biomedical Engineering, 50(5):549–558.

Ieˇsmantas, T. and Alzbutas, R. (2020). Convolutional neural network for detection and classiﬁcation of seizures in clinical data. Medical & Biological Engineering & Computing, 58(9):1919–1932.

Ihle, M., Feldwisch-Drentrup, H., Teixeira, C. A., Witon, A., Schelter, B., Timmer, J., and Schulze-Bonhage, A. (2012). Epilepsiae–a european epilepsy database. Computer methods and programs in biomedicine, 106(3):127–138.

Ilakiyaselvan, N., Khan, A. N., and Shahina, A. (2020). Deep learning approach to detect seizure using reconstructed phase space images. Journal of Biomedical Research, 34(3):240.

Jaafar, S. T. and Mohammadi, M. (2019). Epileptic seizure detection using deep learning approach. UHD Journal of Science and Technology, 3(2):41–50.

Jaber, H. A., Aljobouri, H. K., ¸Cankaya, I.,˙ Ko¸cak, O. M., and Algin, O. (2019). Preparing fmri data for postprocessing: Conversion modalities, preprocessing pipeline, and parametric and nonparametric approaches. IEEE Access, 7:122864–122877.

Jana, G. C., Sharma, R., and Agrawal, A. (2020). A 1d-cnn-spectrogram based approach for seizure detection from eeg signal. Procedia Computer Science, 167:403–412.

Jiang, H., Gao, F., Duan, X., Bai, Z., Wang, Z., Ma, X., and Chen, Y.-W. (2019a). Transfer learning and fusion model for classiﬁcation of epileptic pet images. In Innovation in Medicine and Healthcare Systems, and Multimedia, pages 71–79. Springer.

Jiang, X., Bian, G.-B., and Tian, Z. (2019b). Removal of artifacts from eeg signals: a review. Sensors, 19(5):987.

Karim, A. M., Gu¨zel, M. S., Tolun, M. R., Kaya, H., and C¸elebi, F. V. (2018a). A new generalized deep learning framework combining sparse autoencoder and taguchi method for novel data classiﬁcation and processing. Mathematical Problems in Engineering, 2018.

Karim, A. M., Gu¨zel, M. S., Tolun, M. R., Kaya, H., and ¸Celebi, F. V. (2019). A new framework using deep auto-encoder and energy spectral density for medical waveform data classiﬁcation and processing. Biocybernetics and Biomedical Engineering, 39(1):148–159.

Karim, A. M., Karal, O.,¨ and C¸elebi, F. (2018b). A new automatic epilepsy serious detection method by using deep learning based on discrete wavelet transform. no, 4:15–18.

Kaya, D. (2020). The mrmr-cnn based inﬂuential support decision system approach to classify eeg signals. Measurement, 156:107602.

Kaziha, O. and Bonny, T. (2020). A convolutional neural network for seizure detection. In 2020 Advances in Science and Engineering Technology International Conferences (ASET), pages 1–5. IEEE.

Keren, G. and Schuller, B. (2016). Convolutional rnn: an enhanced model for extracting features from sequential data. In 2016 International Joint Conference on Neural Networks (IJCNN), pages 3412–3419. IEEE.

Khalifa, Y., Mandic, D., and Sejdi´c, E. (2020). A review of hidden markov models and recurrent neural networks for event detection and localization in biomedical signals. Information Fusion.

Khalilpour, S., Ranjbar, A., Menhaj, M. B., and Sandooghdar, A. (2020). Application of 1-d cnn to predict epileptic seizures using eeg records. In 2020 6th International Conference on Web Research (ICWR), pages 314–318. IEEE.

Khodatars, M., Shoeibi, A., Ghassemi, N., Jafari, M., Khadem, A., Sadeghi, D., Moridian, P., Hussain, S., Alizadehsani, R., Zare, A., et al. (2020a). Deep learning for neuroimaging-based diagnosis and rehabilitation of autism spectrum disorder: A review. arXiv preprint arXiv:2007.01285.

Khodatars, M., Shoeibi, A., Ghassemi, N., Jafari, M., Khadem, A., Sadeghi, D., Moridian, P., Hussain, S., Alizadehsani, R., Zare, A., et al. (2020b). Deep learning for neuroimaging-based diagnosis and rehabilitation of autism spectrum disorder: A review. arXiv preprint arXiv:2007.01285.

Kim, S.-P. (2018). Preprocessing of eeg. In Computational EEG Analysis, pages 15–33. Springer.

Kiral-Kornek, I., Roy, S., Nurse, E., Mashford, B., Karoly, P., Carroll, T., Payne, D., Saha, S., Baldassano, S., O’Brien, T., et al. (2018). Epileptic seizure prediction using big data and deep learning: toward a mobile system. EBioMedicine, 27:103–111.

Kowalczyk, M. A., Omidvarnia, A., Abbott, D. F., Tailby, C., Vaughan, D. N., and Jackson, G. D. (2020). Clinical beneﬁt of presurgical eeg-fmri in diﬃcult-

to-localize focal epilepsy: A single-institution retrospective review. Epilepsia, 61(1):49–60.

Krizhevsky, A. and Hinton, G. (2010). Convolutional deep belief networks on cifar-10. Unpublished manuscript, 40(7):1–9.

Kwak, Y., Kong, K., Song, W.-J., Min, B.-K., and Kim, S.-E. (2020). Multilevel feature fusion with 3d convolutional neural network for eeg-based workload estimation. IEEE Access, 8:16009–16021.

Lai, C. Q., Ibrahim, H., Abdullah, M. Z., Abdullah, J. M., Suandi, S. A., and Azman, A. (2018). Artifacts and noise removal for electroencephalogram (eeg): A literature review. In 2018 IEEE Symposium on Computer Applications & Industrial Electronics (ISCAIE), pages 326–332. IEEE.

Lashgari, E., Liang, D., and Maoz, U. (2020). Data augmentation for deeplearning-based electroencephalography. Journal of Neuroscience Methods, page 108885.

Le, T. X., Le, T. T., Dinh, V. V., Tran, Q. L., Nguyen, L. T., and Nguyen, D. T. (2018). Deep learning for epileptic spike detection. VNU Journal of Science: Computer Science and Communication Engineering, 33(2):1–13.

Lee, M.-H., O’Hara, N., Sonoda, M., Kuroda, N., Juhasz, C., Asano, E., Dong, M., and Jeong, J.-W. (2020). Novel deep learning network analysis of electrical stimulation mapping-driven diﬀusion mri tractography to improve preoperative evaluation of pediatric epilepsy. IEEE Transactions on Biomedical Engineering, 67(11):3151–3162.

LeVan, P., Urrestarazu, E., and Gotman, J. (2006). A system for automatic artifact removal in ictal scalp eeg based on independent component analysis and bayesian classiﬁcation. Clinical neurophysiology, 117(4):912–927.

Li, J., Li, B., Xu, J., Xiong, R., and Gao, W. (2018). Fully connected networkbased intra prediction for image coding. IEEE Transactions on Image Processing, 27(7):3236–3247.

Li, S., Kawale, J., and Fu, Y. (2015). Deep collaborative ﬁltering via marginalized denoising auto-encoder. In Proceedings of the 24th ACM international on conference on information and knowledge management, pages 811–820.

Li, Y., Liu, Y., Cui, W.-G., Guo, Y.-Z., Huang, H., and Hu, Z.-Y. (2020a). Epileptic seizure detection in eeg signals using a uniﬁed temporal-spectral squeeze-and-excitation network. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 28(4):782–794.

Li, Y., Yu, Z., Chen, Y., Yang, C., Li, Y., Allen Li, X., and Li, B. (2020b). Automatic seizure detection using fully convolutional nested lstm. International journal of neural systems, 30(04):2050019.

Lian, J., Zhang, Y., Luo, R., Han, G., Jia, W., and Li, C. (2020). Pair-wise matching of eeg signals for epileptic identiﬁcation via convolutional neural network. IEEE Access, 8:40008–40017.

Liang, W., Pei, H., Cai, Q., and Wang, Y. (2020). Scalp eeg epileptogenic zone recognition and localization based on long-term recurrent convolutional network. Neurocomputing, 396:569–576.

Lin, L.-C., Ouyang, C.-S., Wu, R.-C., Yang, R.-C., and Chiang, C.-T. (2020). Alternative diagnosis of epilepsy in children without epileptiform discharges using deep convolutional neural networks. International journal of neural systems, 30(05):1850060.

Lin, Q., Ye, S.-q., Huang, X.-m., Li, S.-y., Zhang, M.-z., Xue, Y., and Chen, W.-S. (2016). Classiﬁcation of epileptic eeg signals with stacked sparse autoencoder based on deep learning. In International Conference on Intelligent Computing, pages 802–810. Springer.

- Liu, F., Wang, Y., Li, M., Wang, W., Li, R., Zhang, Z., Lu, G., and Chen, H. (2017). Dynamic functional network connectivity in idiopathic generalized epilepsy with generalized tonic–clonic seizure. Human brain mapping, 38(2):957–973.
- Liu, G., Zhou, W., and Geng, M. (2020a). Automatic seizure detection based on s-transform and deep convolutional neural network. International journal of neural systems, 30(04):1950024.

Liu, J. and Woodson, B. (2019). Deep learning classiﬁcation for epilepsy detection using a single channel electroencephalography (eeg). In Proceedings of the 2019 3rd International Conference on Deep Learning Technologies, pages 23–26.

- Liu, X. and Richardson, A. G. (2020). Embedded deep learning for neural implants. arXiv preprint arXiv:2012.00307.
- Liu, Y., Huang, Y.-X., Zhang, X., Qi, W., Guo, J., Hu, Y., Zhang, L., and Su, H. (2020b). Deep c-lstm neural network for epileptic seizure and tumor detection using high-dimension eeg signals. IEEE Access, 8:37495–37504.

Liu, Y., Zhou, W., Yuan, Q., and Chen, S. (2012). Automatic seizure detection using wavelet transform and svm in long-term intracranial eeg. IEEE transactions on neural systems and rehabilitation engineering, 20(6):749–755.

Lu, D., Bauer, S., Neubert, V., Costard, L. S., Rosenow, F., and Triesch, J. (2020). Staging epileptogenesis with deep neural networks. In Proceedings of the 11th ACM International Conference on Bioinformatics, Computational Biology and Health Informatics, pages 1–10.

Lu, D. and Triesch, J. (2019). Residual deep convolutional neural network for eeg signal classiﬁcation in epilepsy. arXiv preprint arXiv:1903.08100.

Luo, C., Li, Q., Lai, Y., Xia, Y., Qin, Y., Liao, W., Li, S., Zhou, D., Yao, D., and Gong, Q. (2011). Altered functional connectivity in default mode network in absence epilepsy: a resting-state fmri study. Human brain mapping, 32(3):438–449.

Ma, K., Zhang, X., Zhang, H., Yan, X., Gao, A., Song, C., Wang, S., Lian, Y., and Cheng, J. (2020). Mean apparent propagator-mri: a new diﬀusion model which improves temporal lobe epilepsy lateralization. European journal of radiology, 126:108914.

Madhavan, S., Tripathy, R. K., and Pachori, R. B. (2019). Time-frequency domain deep convolutional neural network for the classiﬁcation of focal and non-focal eeg signals. IEEE Sensors Journal, 20(6):3078–3086.

Makhzani, A., Shlens, J., Jaitly, N., Goodfellow, I., and Frey, B. (2015). Adversarial autoencoders. arXiv preprint arXiv:1511.05644.

Makropoulos, A., Counsell, S. J., and Rueckert, D. (2018). A review on automatic fetal and neonatal brain mri segmentation. NeuroImage, 170:231–248.

Manj´n, J. V. (2017). Mri preprocessing. In Imaging Biomarkers, pages 53–63. Springer.

Mao, W., Fathurrahman, H., Lee, Y., and Chang, T. (2020). Eeg dataset classiﬁcation using cnn method. In Journal of Physics: Conference Series, volume 1456, page 012017. IOP Publishing.

Mei, Z., Zhao, X., Chen, H., and Chen, W. (2018). Bio-signal complexity analysis in epileptic seizure monitoring: A topic review. Sensors, 18(6):1720.

Meisel, C., Atrache, R. E., Jackson, M., Schubach, S., Ufongene, C., and Loddenkemper, T. (2019). Deep learning from wristband sensor data: towards wearable, non-invasive seizure forecasting. arXiv preprint arXiv:1906.00511.

Misiu¯nas, A. V. M., Mesˇkauskas, T., and Samaitien˙e, R. (2019). Algorithm for automatic eeg classiﬁcation according to the epilepsy type: Benign focal childhood epilepsy and structural focal epilepsy. Biomedical signal processing and control, 48:118–127.

Modir, A., Khalilzadeh, M. A., and Gorji, A. (2017). Detection of focal epileptic seizure using nirs signal based on discrete wavelet transform. International Clinical Neuroscience Journal, 4(4):134.

Mohammadpoor, M., Shoeibi, A., Shojaee, H., et al. (2016). A hierarchical classiﬁcation method for breast tumor detection. Iranian Journal of Medical Physics, 13(4):261–268.

Mohammadpoory, Z., Nasrolahzadeh, M., Mahmoodian, N., Sayyah, M., and Haddadnia, J. (2019). Complex network based models of ecog signals for detection of induced epileptic seizures in rats. Cognitive neurodynamics, 13(4):325–339.

MohanBabu, G., Anupallavi, S., and Ashokkumar, S. (2020). An optimized deep learning network model for eeg based seizure classiﬁcation using synchronization and functional connectivity measures. Journal of Ambient Intelligence and Humanized Computing, pages 1–13.

Muhammad, G., Masud, M., Amin, S. U., Alrobaea, R., and Alhamid, M. F.

(2018). Automatic seizure detection in a mobile multimedia framework. IEEE Access, 6:45372–45383.

Naik, G., Chai, R., Su, S., Rong, S., and Nguyen, H. T. (2020). Comparison of independence of triceps brachii and biceps brachii between paretic and non-paretic side during diﬀerent mvcs—a case study. In Biomedical Signal Processing, pages 71–79. Springer.

Nair, D. R., Laxer, K. D., Weber, P. B., Murro, A. M., Park, Y. D., Barkley, G. L., Smith, B. J., Gwinn, R. P., Doherty, M. J., Noe, K. H., et al. (2020). Nine-year prospective eﬃcacy and safety of brain-responsive neurostimulation for focal epilepsy. Neurology, 95(9):e1244–e1256.

Nejedly, P., Kremen, V., Sladky, V., Nasseri, M., Guragain, H., Klimes, P., Cimbalnik, J., Varatharajah, Y., Brinkmann, B. H., and Worrell, G. A. (2019). Deep-learning for seizure forecasting in canines with epilepsy. Journal of neural engineering, 16(3):036031.

Ngoh, A. and Parker, A. P. (2017). New developments in epilepsy management. Paediatrics and Child Health, 27(6):281–286.

Nguyen, D. K., Tremblay, J., Pouliot, P., Vannasing, P., Florea, O., Carmant, L., Lepore, F., Sawan, M., Lesage, F., and Lassonde, M. (2012). Non-invasive continuous eeg-fnirs recording of temporal lobe seizures. Epilepsy research, 99(1-2):112–126.

Noachtar, S. and Peters, A. S. (2009). Semiology of epileptic seizures: a critical review. Epilepsy & Behavior, 15(1):2–9.

Noble, W. S. (2006). What is a support vector machine? Nature biotechnology, 24(12):1565–1567.

Ocak, H. (2009). Automatic detection of epileptic seizures in eeg using discrete wavelet transform and approximate entropy. Expert Systems with Applications, 36(2):2027–2036.

Oldan, J. D., Shin, H. W., Khandani, A. H., Zamora, C., Beneﬁeld, T., and Jewells, V. (2018). Subsequent experience in hybrid pet-mri for evaluation of refractory focal onset epilepsy. Seizure, 61:128–134.

- O’Shea, A., Lightbody, G., Boylan, G., and Temko, A. (2017a). Neonatal seizure detection using convolutional neural networks. In 2017 IEEE 27th International Workshop on Machine Learning for Signal Processing (MLSP), pages 1–6. IEEE.
- O’Shea, A., Lightbody, G., Boylan, G., and Temko, A. (2017b). Neonatal seizure detection using convolutional neural networks. In 2017 IEEE 27th International Workshop on Machine Learning for Signal Processing (MLSP), pages 1–6. IEEE.

Pachori, R. B. and Bajaj, V. (2011). Analysis of normal and epileptic seizure eeg signals using empirical mode decomposition. Computer methods and programs in biomedicine, 104(3):373–381.

Page, A., Shea, C., and Mohsenin, T. (2016). Wearable seizure detection using convolutional neural networks with transfer learning. In 2016 IEEE International Symposium on Circuits and Systems (ISCAS), pages 1086–1089. IEEE.

- Park, B.-y., Byeon, K., and Park, H. (2019). Funp (fusion of neuroimaging preprocessing) pipelines: a fully automated preprocessing software for functional magnetic resonance imaging. Frontiers in neuroinformatics, 13:5.
- Park, C., Choi, G., Kim, J., Kim, S., Kim, T.-J., Min, K., Jung, K.-Y., and Chong, J. (2018). Epileptic seizure detection for multi-channel eeg with deep convolutional neural network. In 2018 International Conference on Electronics, Information, and Communication (ICEIC), pages 1–5. IEEE.

Pascual, D., Aminifar, A., Atienza, D., Ryvlin, P., and Wattenhofer, R. (2019). Synthetic epileptic brain activities using gans. In Machine Learning for Health (ML4H) at the 33rd Conf. on Neural Information Processing Systems.

Patan, K. and Rutkowski, G. (2021). Application of deep learning to seizure classiﬁcation. In Advances in Diagnostics of Processes and Systems, pages 157–172. Springer.

Patro, S. and Sahu, K. K. (2015). Normalization: A preprocessing stage. arXiv preprint arXiv:1503.06462.

Paul, Y. (2018). Various epileptic seizure detection techniques using biomedical signals: a review. Brain informatics, 5(2):1–19.

Pellegrino, G., Mecarelli, O., Pulitano, P., Tombini, M., Ricci, L., Lanzone, J., Brienza, M., Davassi, C., Di Lazzaro, V., and Assenza, G. (2018). Eslicarbazepine acetate modulates eeg activity and connectivity in focal epilepsy. Frontiers in neurology, 9:1054.

Peng, K., Nguyen, D. K., Tayah, T., Vannasing, P., Tremblay, J., Sawan, M., Lassonde, M., Lesage, F., and Pouliot, P. (2014). fnirs-eeg study of focal interictal epileptiform discharges. Epilepsy research, 108(3):491–505.

Peng, K., Nguyen, D. K., Vannasing, P., Tremblay, J., Lesage, F., and Pouliot, P. (2016). Using patient-speciﬁc hemodynamic response function in epileptic spike analysis of human epilepsy: a study based on eeg–fnirs. NeuroImage, 126:239–255.

Peng, W. (2019). Eeg preprocessing and denoising. In EEG Signal Processing and Feature Extraction, pages 71–87. Springer.

Pisano, F., Sias, G., Fanni, A., Cannas, B., Dourado, A., Pisano, B., and Teixeira, C. A. (2020). Convolutional neural network for seizure detection of nocturnal frontal lobe epilepsy. Complexity, 2020.

Polat, K. and G¨unes¸, S. (2007). Classiﬁcation of epileptiform eeg using a hybrid system based on decision tree classiﬁer and fast fourier transform. Applied Mathematics and Computation, 187(2):1017–1026.

Pominova, M., Artemov, A., Sharaev, M., Kondrateva, E., Bernstein, A., and Burnaev, E. (2018). Voxelwise 3d convolutional and recurrent neural networks for epilepsy and depression diagnostics from structural and functional mri

data. In 2018 IEEE International Conference on Data Mining Workshops (ICDMW), pages 299–307. IEEE.

Pouliot, P., Tremblay, J., Robert, M., Vannasing, P., Lepore, F., Lassonde, M., Sawan, M., Nguyen, D. K., and Lesage, F. (2012). Nonlinear hemodynamic responses in human epilepsy: a multimodal analysis with fnirs-eeg and fmrieeg. Journal of neuroscience methods, 204(2):326–340.

Prasanth, T., Thomas, J., Yuvaraj, R., Jing, J., Cash, S. S., Chaudhari, R., Leng, T. Y., Rathakrishnan, R., Rohit, S., Saini, V., et al. (2020). Deep learning for interictal epileptiform spike detection from scalp eeg frequency sub bands. In 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), pages 3703–3706. IEEE.

Qin, H., Deng, B., Wang, J., Yi, G., Wang, R., and Zhang, Z. (2020a). Deep multi-scale feature fusion convolutional neural network for automatic epilepsy detection using eeg signals. In 2020 39th Chinese Control Conference (CCC), pages 7061–7066. IEEE.

Qin, Y., Zheng, H., Chen, W., Qin, Q., Han, C., and Che, Y. (2020b). Patientspeciﬁc seizure prediction with scalp eeg using convolutional neural network and extreme learning machine. In 2020 39th Chinese Control Conference (CCC), pages 7622–7625. IEEE.

Qiu, Y., Zhou, W., Yu, N., and Du, P. (2018). Denoising sparse autoencoderbased ictal eeg classiﬁcation. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 26(9):1717–1726.

Raghu, S., Sriraam, N., Temel, Y., Rao, S. V., and Kubben, P. L. (2020). Eeg based multi-class seizure type classiﬁcation using convolutional neural network and transfer learning. Neural Networks, 124:202–212.

Rajaguru, H. and Prabhakar, S. K. (2018). Multilayer autoencoders and empca with genetic algorithm for epilepsy classiﬁcation from eeg. In 2018 Second International Conference on Electronics, Communication and Aerospace Technology (ICECA), pages 353–358. IEEE.

Rampp, S., Stefan, H., Wu, X., Kaltenh¨user, M., Maess, B., Schmitt, F. C., Wolters, C. H., Hamer, H., Kasper, B. S., Schwab, S., et al. (2019). Magnetoencephalography for epileptic focus localization in a series of 1000 cases. Brain, 142(10):3059–3071.

Rashed-Al-Mahfuz, M., Moni, M. A., Uddin, S., Alyami, S. A., Summers, M. A., and Eapen, V. (2021). A deep convolutional neural network method to detect seizures and characteristic frequencies using epileptic electroencephalogram (eeg) data. IEEE Journal of Translational Engineering in Health and Medicine, 9:1–12.

Rasheed, K., Qayyum, A., Qadir, J., Sivathamboo, S., Kwan, P., Kuhlmann, L., O’Brien, T., and Razi, A. (2020). Machine learning for predicting epileptic seizures using eeg signals: A review. IEEE Reviews in Biomedical Engineering.

RaviPrakash, H., Korostenskaja, M., Castillo, E. M., Lee, K. H., Salinas, C. M., Baumgartner, J., Anwar, S. M., Spampinato, C., and Bagci, U. (2020). Deep learning provides exceptional accuracy to ecog-based functional language mapping for epilepsy surgery. Frontiers in Neuroscience, 14:409.

Rebsamen, M., Suter, Y., Wiest, R., Reyes, M., and Rummel, C. (2020). Brain morphometry estimation: From hours to seconds using deep learning. Frontiers in neurology, 11:244.

Rosas-Romero, R., Guevara, E., Peng, K., Nguyen, D. K., Lesage, F., Pouliot, P., and Lima-Saad, W.-E. (2019). Prediction of epileptic seizures with convolutional neural networks and functional near-infrared spectroscopy signals. Computers in biology and medicine, 111:103355.

- Roy, S., Kiral-Kornek, I., and Harrer, S. (2018). Deep learning enabled automatic abnormal eeg identiﬁcation. In 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pages 2756–2759. IEEE.
- Roy, S., Kiral-Kornek, I., and Harrer, S. (2019). Chrononet: a deep recurrent neural network for abnormal eeg identiﬁcation. In Conference on Artiﬁcial Intelligence in Medicine in Europe, pages 47–56. Springer.

Ru¨ber, T., David, B., and Elger, C. E. (2018). Mri in epilepsy: clinical standard and evolution. Current opinion in neurology, 31(2):223–231.

Saab, M. and Gotman, J. (2005). A system to detect the onset of epileptic seizures in scalp eeg. Clinical Neurophysiology, 116(2):427–442.

Sadeghi, D., Shoeibi, A., Ghassemi, N., Moridian, P., Khadem, A., Alizadehsani, R., Teshnehlab, M., Gorriz, J. M., and Nahavandi, S. (2021). An overview on artiﬁcial intelligence techniques for diagnosis of schizophrenia based on magnetic resonance imaging modalities: Methods, challenges, and future works. arXiv preprint arXiv:2103.03081.

Sajjad, M., Khan, S., Muhammad, K., Wu, W., Ullah, A., and Baik, S. W.

(2019). Multi-grade brain tumor classiﬁcation using deep cnn with extensive data augmentation. Journal of computational science, 30:174–182.

Sakai, T., Shoji, T., Yoshida, N., Fukumori, K., Tanaka, Y., and Tanaka, T. (2020). Scalpnet: Detection of spatiotemporal abnormal intervals in epileptic eeg using convolutional neural networks. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 1244–1248. IEEE.

Samiee, K., Kovacs, P., and Gabbouj, M. (2014). Epileptic seizure classiﬁcation of eeg time-series using rational discrete short-time fourier transform. IEEE transactions on Biomedical Engineering, 62(2):541–552.

San-Segundo, R., Gil-Martı´n, M., D’Haro-Enriquez, L. F., and Pardo, J. M. (2019). Classiﬁcation of epileptic eeg recordings using signal transforms and convolutional neural networks. Computers in biology and medicine, 109:148– 158.

Saqib, M., Zhu, Y., Wang, M., and Beaulieu-Jones, B. (2020). Regularization of deep neural networks for eeg seizure detection to mitigate overﬁtting. In 2020 IEEE 44th Annual Computers, Software, and Applications Conference (COMPSAC), pages 664–673. IEEE.

Sayem, M. A., Sarker, M. S. R., Ahad, M. A. R., and Ahmed, M. U. (2021). Automatic epileptic seizures detection and eeg signals classiﬁcation based on

multi-domain feature extraction and multiscale entropy analysis. In Signal Processing Techniques for Computational Health Informatics, pages 315–334. Springer.

Schlegl, T., Seeb¨ck, P., Waldstein, S. M., Langs, G., and Schmidt-Erfurth, U. (2019). f-anogan: Fast unsupervised anomaly detection with generative adversarial networks. Medical image analysis, 54:30–44.

Schroﬀ, F., Kalenichenko, D., and Philbin, J. (2015). Facenet: A uniﬁed embedding for face recognition and clustering. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 815–823.

Shakeri, M., Tsogkas, S., Ferrante, E., Lippe, S., Kadoury, S., Paragios, N., and Kokkinos, I. (2016). Sub-cortical brain structure segmentation using f-cnn’s. In 2016 IEEE 13th International Symposium on Biomedical Imaging (ISBI), pages 269–272. IEEE.

Shankar, A., Khaing, H. K., Dandapat, S., and Barma, S. (2020). Epileptic seizure classiﬁcation based on gramian angular ﬁeld transformation and deep learning. In 2020 IEEE Applied Signal Processing Conference (ASPCON), pages 147–151. IEEE.

Sharan, R. V. and Berkovsky, S. (2020). Epileptic seizure detection using multichannel eeg wavelet power spectra and 1-d convolutional neural networks. In 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), pages 545–548. IEEE.

Sharathappriyaa, V., Gautham, S., and Lavanya, R. (2018). Auto-encoder based automated epilepsy diagnosis. In 2018 International Conference on Advances in Computing, Communications and Informatics (ICACCI), pages 976–982. IEEE.

Sharifrazi, D., Alizadehsani, R., Roshanzamir, M., Joloudari, J. H., Shoeibi, A., Jafari, M., Hussain, S., Sani, Z. A., Hasanzadeh, F., Khozeimeh, F., et al. (2021). Fusion of convolution neural network, support vector machine and sobel ﬁlter for accurate detection of covid-19 patients using x-ray images. Biomedical Signal Processing and Control, page 102622.

Sharma, R. and Pachori, R. B. (2015). Classiﬁcation of epileptic seizures in eeg signals based on phase space representation of intrinsic mode functions. Expert Systems with Applications, 42(3):1106–1117.

Sharma, R., Pachori, R. B., and Sircar, P. (2020). Seizures classiﬁcation based on higher order statistics and deep neural network. Biomedical Signal Processing and Control, 59:101921.

Sharmila, A. (2018). Epilepsy detection from eeg signals: a review. Journal of medical engineering & technology, 42(5):368–380.

Shiri, I., Ghafarian, P., Geramifar, P., Leung, K. H.-Y., Ghelichoghli, M., Oveisi, M., Rahmim, A., and Ay, M. R. (2019). Direct attenuation correction of brain pet images using only emission data via a deep convolutional encoder-decoder (deep-dac). European radiology, 29(12):6867–6879.

- Shoeb, A. H. (2009a). Application of machine learning to epileptic seizure onset detection and treatment. PhD thesis, Massachusetts Institute of Technology.
- Shoeb, A. H. (2009b). Application of machine learning to epileptic seizure onset detection and treatment. PhD thesis, Massachusetts Institute of Technology.

Shoeb, A. H. and Guttag, J. V. (2010). Application of machine learning to epileptic seizure detection. In Proceedings of the 27th International Conference on Machine Learning (ICML-10), pages 975–982.

Shoeibi, A., Ghassemi, N., Alizadehsani, R., Rouhani, M., Hosseini-Nejad, H., Khosravi, A., Panahiazar, M., and Nahavandi, S. (2021). A comprehensive comparison of handcrafted features and convolutional autoencoders for epileptic seizures detection in eeg signals. Expert Systems with Applications, 163:113788.

Shoeibi, A., Khodatars, M., Alizadehsani, R., Ghassemi, N., Jafari, M., Moridian, P., Khadem, A., Sadeghi, D., Hussain, S., Zare, A., et al. (2020). Automated detection and forecasting of covid-19 using deep learning techniques: A review. arXiv preprint arXiv:2007.10785.

Shoka, A., Dessouky, M., El-Sherbeny, A., and El-Sayed, A. (2019). Literature review on eeg preprocessing, feature extraction, and classiﬁcations techniques. Menouﬁa J. Electron. Eng. Res, 28(1):292–299.

Si, X., Zhang, X., Zhou, Y., Sun, Y., Jin, W., Yin, S., Zhao, X., Li, Q., and Ming, D. (2020). Automated detection of juvenile myoclonic epilepsy using cnn based transfer learning in diﬀusion mri. In 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), pages 1679–1682. IEEE.

Siddharth, T., Gajbhiye, P., Tripathy, R. K., and Pachori, R. B. (2020). Eegbased detection of focal seizure area using fbse-ewt rhythm and sae-svm network. IEEE Sensors Journal, 20(19):11421–11428.

Siddiqui, M. K., Islam, M. Z., and Kabir, M. A. (2019). A novel quick seizure detection and localization through brain data mining on ecog dataset. Neural Computing and Applications, 31(9):5595–5608.

Siddiqui, M. K., Morales-Menendez, R., Huang, X., and Hussain, N. (2020). A review of epileptic seizure detection using machine learning classiﬁers. Brain informatics, 7:1–18.

Singh, A., Pusarla, N., Sharma, S., and Kumar, T. (2020). Cnn-based epilepsy detection using image like features of eeg signals. In 2020 International Conference on Electrical and Electronics Engineering (ICE3), pages 280–284. IEEE.

Singh, K. and Malhotra, J. (2018). Stacked autoencoders based deep learning approach for automatic epileptic seizure detection. In 2018 First International Conference on Secure Cyber Computing and Communication (ICSCCC), pages 249–254. IEEE.

Sirpal, P., Kassab, A., Pouliot, P., Nguyen, D. K., and Lesage, F. (2019). fnirs improves seizure detection in multimodal eeg-fnirs recordings. Journal of biomedical optics, 24(5):051408.

Skarpaas, T. L., Jarosiewicz, B., and Morrell, M. J. (2019). Brain-responsive neurostimulation for epilepsy (rns® system). Epilepsy research, 153:68–70.

Sønderby, C. K., Raiko, T., Maaløe, L., Sønderby, S. K., and Winther, O. (2016). Ladder variational autoencoders. arXiv preprint arXiv:1602.02282.

Stevenson, N., Tapani, K., Lauronen, L., and Vanhatalo, S. (2019). A dataset of neonatal eeg recordings with seizure annotations. Scientiﬁc data, 6(1):1–8.

Subasi, A. (2005). Epileptic seizure detection using dynamic wavelet network. Expert Systems with Applications, 29(2):343–355.

Sui, L., Zhao, X., Zhao, Q., Tanaka, T., and Cao, J. (2019). Localization of epileptic foci by using convolutional neural network based on ieeg. In IFIP International Conference on Artiﬁcial Intelligence Applications and Innovations, pages 331–339. Springer.

Sun, Y., Liang, D., Wang, X., and Tang, X. (2015). Deepid3: Face recognition with very deep neural networks. arXiv preprint arXiv:1502.00873.

Sung, F., Yang, Y., Zhang, L., Xiang, T., Torr, P. H., and Hospedales, T. M. (2018). Learning to compare: Relation network for few-shot learning. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 1199–1208.

Tak, S. and Ye, J. C. (2014). Statistical analysis of fnirs data: a comprehensive review. Neuroimage, 85:72–91.

Takahashi, H., Emami, A., Shinozaki, T., Kunii, N., Matsuo, T., and Kawai, K. (2020). Convolutional neural network with autoencoder-assisted multiclass labelling for seizure detection based on scalp electroencephalography. Computers in Biology and Medicine, 125:104016.

Talathi, S. S. (2017). Deep recurrent neural networks for seizure detection and early seizure detection systems. arXiv preprint arXiv:1706.03283.

Tan, M. and Le, Q. (2019). Eﬃcientnet: Rethinking model scaling for convolutional neural networks. In International Conference on Machine Learning, pages 6105–6114. PMLR.

Tang, L., Xie, N., Zhao, M., and Wu, X. (2020). Seizure prediction using multiview features and improved convolutional gated recurrent network. IEEE Access, 8:172352–172361.

Taqi, A. M., Al-Azzo, F., Mariofanna, M., and Al-Saadi, J. M. (2017). Classiﬁcation and discrimination of focal and non-focal eeg signals based on deep neural network. In 2017 international conference on current research in computer science and information technology (ICCIT), pages 86–92. IEEE.

Targ, S., Almeida, D., and Lyman, K. (2016). Resnet in resnet: Generalizing residual architectures. arXiv preprint arXiv:1603.08029.

Thanaraj, K. P., Parvathavarthini, B., Tanik, U. J., Rajinikanth, V., Kadry, S., and Kamalanand, K. (2020). Implementation of deep neural networks to classify eeg signals using gramian angular summation ﬁeld for epilepsy diagnosis. arXiv preprint arXiv:2003.04534.

Thodoroﬀ, P., Pineau, J., and Lim, A. (2016). Learning robust features using deep learning for automatic seizure detection. In Machine learning for healthcare conference, pages 178–190. PMLR.

Thomas, A. H., Aminifar, A., and Atienza, D. (2020a). Noise-resilient and interpretable epileptic seizure detection. In 2020 IEEE International Symposium on Circuits and Systems (ISCAS), pages 1–5. IEEE.

Thomas, J., Comoretto, L., Jin, J., Dauwels, J., Cash, S. S., and Westover, M. B. (2018). Eeg classiﬁcation via convolutional neural network-based interictal epileptiform event detection. In 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pages 3148–3151. IEEE.

Thomas, J., Jin, J., Thangavel, P., Bagheri, E., Yuvaraj, R., Dauwels, J., Rathakrishnan, R., Halford, J. J., Cash, S. S., and Westover, B. (2020b). Automated detection of interictal epileptiform discharges from scalp electroencephalograms by convolutional neural networks. International journal of neural systems, 30(11):2050030.

Tian, X., Deng, Z., Ying, W., Choi, K.-S., Wu, D., Qin, B., Wang, J., Shen, H., and Wang, S. (2019). Deep multi-view feature learning for eeg-based epileptic seizure detection. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 27(10):1962–1972.

Tjepkema-Cloostermans, M. C., de Carvalho, R. C., and van Putten, M. J.

(2018). Deep learning for detection of focal epileptiform discharges from scalp eeg recordings. Clinical neurophysiology, 129(10):2191–2196.

Torﬁ, A. and Fox, E. A. (2020). Corgan: Correlation-capturing convolutional generative adversarial networks for generating synthetic healthcare records. arXiv e-prints, pages arXiv–2001.

Torres-Vel´zquez, M., Hwang, G., Cook, C. J., Hermann, B., Prabhakaran, V., Meyerand, M. E., and McMillan, A. B. (2020). Multi-channel deep neural network for temporal lobe epilepsy classiﬁcation using multimodal mri data. In 2020 IEEE 17th International Symposium on Biomedical Imaging Workshops (ISBI Workshops), pages 1–4. IEEE.

Truong, N. D., Kuhlmann, L., Bonyadi, M. R., Querlioz, D., Zhou, L., and Kavehei, O. (2019). Epileptic seizure forecasting with generative adversarial networks. IEEE Access, 7:143999–144009.

Truong, N. D., Yang, Y., Maher, C., Nikpour, A., and Kavehei, O. (2020). Epileptic seizure forecasting: Probabilistic seizure-risk assessment and datafusion. arXiv preprint arXiv:2005.07196.

Tuncer, T., Dogan, S., Ertam, F., and Subasi, A. (2020). A novel ensemble local graph structure based feature extraction network for eeg signal analysis. Biomedical Signal Processing and Control, 61:102006.

Tu¨rk, O.¨ and Ozerdem,¨ M. S. (2019). Epilepsy detection by using scalogram based convolutional neural network from eeg signals. Brain sciences, 9(5):115.

Turner, J., Page, A., Mohsenin, T., and Oates, T. (2017). Deep belief networks used on high resolution multichannel electroencephalography data for seizure detection. arXiv preprint arXiv:1708.08430.

Tzallas, A. T., Tsipouras, M. G., Tsalikakis, D. G., Karvounis, E. C., Astrakas, L., Konitsiotis, S., and Tzaphlidou, M. (2012). Automated epileptic seizure detection methods: a review study. Epilepsy-histological, electroencephalographic and psychological aspects, pages 75–98.

Ullah, I., Hussain, M., Aboalsamh, H., et al. (2018). An automated system for epilepsy detection using eeg brain signals based on deep learning approach. Expert Systems with Applications, 107:61–71.

Usman, S. M., Khalid, S., and Aslam, M. H. (2020). Epileptic seizures prediction using deep learning techniques. Ieee Access, 8:39998–40007.

Uyttenhove, T., Maes, A., Van Steenkiste, T., Deschrijver, D., and Dhaene, T.

(2020). Interpretable epilepsy detection in routine, interictal eeg data using deep learning. In Machine Learning for Health, pages 355–366. PMLR.

van Lanen, R., Colon, A., Wiggins, C., Hoeberigs, M., Hoogland, G., Roebroeck, A., Ivanov, D., Poser, B., Rouhl, R., Hofman, P., et al. (2021). Ultra-high ﬁeld magnetic resonance imaging in human epilepsy: A systematic review. NeuroImage: Clinical, page 102602.

Vance, C., Kim, Y., Zhang, G., Lhatoo, S., Tao, S., Cui, L., Li, X., and Jiang, X.

(2020). Learning to detect the onset of slow activity after a generalized tonic– clonic seizure. BMC Medical Informatics and Decision Making, 20(12):1–8.

Vaughan, D. N. and Jackson, G. D. (2020). Imaging epileptic seizures using fmri. In fMRI, pages 193–216. Springer.

Verma, A. and Janghel, R. R. (2021). Epileptic seizure detection using deep recurrent neural networks in eeg signals. In Advances in Biomedical Engineering and Technology, pages 189–198. Springer.

Vidyaratne, L., Glandon, A., Alam, M., and Iftekharuddin, K. M. (2016). Deep recurrent neural network for seizure detection. In 2016 International Joint Conference on Neural Networks (IJCNN), pages 1202–1207. IEEE.

Wainberg, M., Merico, D., Delong, A., and Frey, B. J. (2018). Deep learning in biomedicine. Nature biotechnology, 36(9):829–838.

Wang, H., Ahmed, S. N., and Mandal, M. (2020a). Automated detection of focal cortical dysplasia using a deep convolutional neural network. Computerized Medical Imaging and Graphics, 79:101662.

Wang, L., Guo, S., Huang, W., and Qiao, Y. (2015). Places205-vggnet models for scene recognition. arXiv preprint arXiv:1508.01667.

Wang, S., Wang, S., Zhang, S., and Wang, Y. (2020b). Time-resnext for epilepsy recognition based on eeg signals in wireless networks. EURASIP Journal on Wireless Communications and Networking, 2020(1):1–12.

Wang, X., Hu, W., McGonigal, A., Zhang, C., Sang, L., Zhao, B., Sun, T., Wang, F., Zhang, J.-g., Shao, X., et al. (2019). Electroclinical features of insulo-opercular epilepsy: an seeg and pet study. Annals of clinical and translational neurology, 6(7):1165–1177.

Wei, Z., Zou, J., Zhang, J., and Xu, J. (2019). Automatic epileptic eeg detection using convolutional neural network with improvements in time-domain. Biomedical Signal Processing and Control, 53:101551.

Wen, T. and Zhang, Z. (2018). Deep convolution neural network and autoencoders-based unsupervised feature learning of eeg signals. IEEE Access, 6:25399–25410.

Weng, W. and Khorasani, K. (1996). An adaptive structure neural networks with application to eeg automatic seizure detection. Neural Networks, 9(7):1223–1240.

Woermann, F. G. and Vollmar, C. (2009). Clinical mri in children and adults with focal epilepsy: a critical review. Epilepsy & Behavior, 15(1):40–49.

Wong, S. and Kuhlmann, L. (2020). Computationally eﬃcient epileptic seizure prediction based on extremely randomised trees. In Proceedings of the Australasian Computer Science Week Multiconference, pages 1–3.

- Xu, G., Ren, T., Chen, Y., and Che, W. (2020a). A one-dimensional cnn-lstm model for epileptic seizure recognition using eeg signal analysis. Frontiers in Neuroscience, 14:1253.
- Xu, H., Dong, M., Lee, M.-H., O’Hara, N., Asano, E., and Jeong, J.-W. (2019). Objective detection of eloquent axonal pathways to minimize postoperative deﬁcits in pediatric epilepsy surgery using diﬀusion tractography and convolutional neural networks. IEEE transactions on medical imaging, 38(8):1910– 1922.

Xu, H., Zhu, H., Luo, L., and Zhang, R. (2020b). Altered gray matter volume in mri-negative focal to bilateral tonic–clonic seizures. Acta Neurologica Belgica, pages 1–9.

Xu, Y., Yang, J., Zhao, S., Wu, H., and Sawan, M. (2020c). An end-to-end deep learning approach for epileptic seizure prediction. In 2020 2nd IEEE International Conference on Artiﬁcial Intelligence Circuits and Systems (AICAS), pages 266–270. IEEE.

- Yan, B., Wang, Y., Li, Y., Gong, Y., Guan, L., and Yu, S. (2016). An eeg signal classiﬁcation method based on sparse auto-encoders and support vector machine. In 2016 IEEE/CIC International Conference on Communications in China (ICCC), pages 1–6. IEEE.

- Yan, M., Liu, L., Chen, S., and Pan, Y. (2018). A deep learning method for prediction of benign epilepsy with centrotemporal spikes. In International Symposium on Bioinformatics Research and Applications, pages 253–

258. Springer.

Yang, G., Yu, S., Dong, H., Slabaugh, G., Dragotti, P. L., Ye, X., Liu, F., Arridge, S., Keegan, J., Guo, Y., et al. (2017). Dagan: Deep de-aliasing generative adversarial networks for fast compressed sensing mri reconstruction. IEEE transactions on medical imaging, 37(6):1310–1321.

Yang, Y., Sarkis, R., El Atrache, R., Loddenkemper, T., and Meisel, C. (2021). Video-based detection of generalized tonic-clonic seizures using deep learning. IEEE Journal of Biomedical and Health Informatics.

- Yao, X., Cheng, Q., and Zhang, G.-Q. (2019a). Automated classiﬁcation of seizures against nonseizures: A deep learning approach. arXiv preprint arXiv:1906.02745.

- Yao, X., Cheng, Q., and Zhang, G.-Q. (2019b). A novel independent rnn approach to classiﬁcation of seizures against non-seizures. arXiv preprint arXiv:1903.09326.

Yao, X., Li, X., Ye, Q., Huang, Y., Cheng, Q., and Zhang, G.-Q. (2021). A robust deep learning approach for automatic classiﬁcation of seizures against non-seizures. Biomedical Signal Processing and Control, 64:102215.

Yi, X., Walia, E., and Babyn, P. (2019). Generative adversarial network in medical imaging: A review. Medical image analysis, 58:101552.

Yıldırım, O.,¨ Baloglu, U. B., and Acharya, U. R. (2018). A deep convolutional neural network model for automated identiﬁcation of abnormal eeg signals. Neural Computing and Applications, pages 1–12.

You, S., Cho, B. H., Yook, S., Kim, J. Y., Shon, Y.-M., Seo, D.-W., and Kim, I. Y. (2020). Unsupervised automatic seizure detection for focal-onset seizures recorded with behind-the-ear eeg using an anomaly-detecting generative adversarial network. Computer methods and programs in biomedicine, 193:105472.

Yuan, Y. and Jia, K. (2019). Fusionatt: deep fusional attention networks for multi-channel biomedical signals. Sensors, 19(11):2429.

- Yuan, Y., Xun, G., Jia, K., and Zhang, A. (2017). A multi-view deep learning method for epileptic seizure detection using short-time fourier transform. In Proceedings of the 8th ACM International Conference on Bioinformatics, Computational Biology, and Health Informatics, pages 213–222.
- Yuan, Y., Xun, G., Jia, K., and Zhang, A. (2018a). A multi-context learning approach for eeg epileptic seizure detection. BMC systems biology, 12(6):47– 57.

Yuan, Y., Xun, G., Jia, K., and Zhang, A. (2018b). A multi-view deep learning framework for eeg seizure detection. IEEE journal of biomedical and health informatics, 23(1):83–94.

Yuan, Y., Xun, G., Ma, F., Suo, Q., Xue, H., Jia, K., and Zhang, A. (2018c). A novel channel-aware attention framework for multi-channel eeg seizure detection via multi-view deep learning. In 2018 IEEE EMBS International Conference on Biomedical & Health Informatics (BHI), pages 206–209. IEEE.

Yuan, Y., Xun, G., Suo, Q., Jia, K., and Zhang, A. (2019). Wave2vec: Deep representation learning for clinical temporal data. Neurocomputing, 324:31– 42.

Yuvaraj, R., Thomas, J., Kluge, T., and Dauwels, J. (2018). A deep learning scheme for automatic seizure detection from long-term scalp eeg. In 2018 52nd Asilomar Conference on Signals, Systems, and Computers, pages 368– 372. IEEE.

Zeng, M., Zhang, X., Zhao, C., Lu, X., and Meng, Q. (2021). Grp-dnet: A gray recurrence plot-based densely connected convolutional network for classiﬁcation of epileptiform eeg. Journal of Neuroscience Methods, 347:108953.

Zeng, R., Wu, J., Shao, Z., Senhadji, L., and Shu, H. (2014). Quaternion softmax classiﬁer. Electronics letters, 50(25):1929–1931.

- Zhan, Q. and Hu, W. (2020). An epilepsy detection method using multiview clustering algorithm and deep features. Computational and Mathematical Methods in Medicine, 2020.

Zhang, B., Wang, W., Xiao, Y., Xiao, S., Chen, S., Chen, S., Xu, G., and Che, W. (2020a). Cross-subject seizure detection in eegs using deep transfer learning. Computational and Mathematical Methods in Medicine, 2020.

Zhang, G., Le Yang, B. L., Lu, Y., Liu, Q., Zhao, W., Ren, T., Zhou, J., Wang, S.-H., and Che, W. (2020b). Mnl-network: A multi-scale non-local network for epilepsy detection from eeg signals. Frontiers in Neuroscience, 14.

Zhang, J., Wu, H., Su, W., Wang, X., Yang, M., and Wu, J. (2018). A new approach for classiﬁcation of epilepsy eeg signals based on temporal convolutional neural networks. In 2018 11th International Symposium on Computational Intelligence and Design (ISCID), volume 2, pages 80–84. IEEE.

- Zhang, X., Yao, L., Dong, M., Liu, Z., Zhang, Y., and Li, Y. (2020c). Adversarial representation learning for robust patient-independent epileptic seizure detection. IEEE journal of biomedical and health informatics, 24(10):2852– 2859.
- Zhang, Y., Jiang, L., Zhang, D., Wang, L., Fei, X., Liu, X., Fu, X., Niu, C., Wang, Y., and Qian, R. (2020d). Thalamocortical structural connectivity abnormalities in drug-resistant generalized epilepsy: A diﬀusion tensor imaging study. Brain research, 1727:146558.

- Zhang, Z., Ren, Y., Sabor, N., Pan, J., Luo, X., Li, Y., Chen, Y., and Wang, G. (2020e). Dwt-net: Seizure detection system with structured eeg montage and multiple feature extractor in convolution neural network. Journal of Sensors, 2020.

- Zhao, S., Yang, J., Xu, Y., and Sawan, M. (2020a). Binary single-dimensional convolutional neural network for seizure prediction. In 2020 IEEE International Symposium on Circuits and Systems (ISCAS), pages 1–5. IEEE.

- Zhao, W. and Wang, W. (2020). Seizurenet: a model for robust detection of epileptic seizures based on convolutional neural network. Cognitive Computation and Systems, 2(3):119–124.

- Zhao, W., Zhao, W., Wang, W., Jiang, X., Zhang, X., Peng, Y., Zhang, B., and Zhang, G. (2020b). A novel deep neural network for robust detection of seizures using eeg signals. Computational and mathematical methods in medicine, 2020.
- Zhao, X., Sol´e-Casals, J., Li, B., Huang, Z., Wang, A., Cao, J., Tanaka, T., and Zhao, Q. (2020c). Classiﬁcation of epileptic ieeg signals by cnn and data augmentation. In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 926–930. IEEE.

- Zhao, X., Zhang, H., Zhu, G., You, F., Kuang, S., and Sun, L. (2019). A multi-branch 3d convolutional neural network for eeg-based motor imagery classiﬁcation. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 27(10):2164–2177.

Zheng, L., Liao, P., Luo, S., Sheng, J., Teng, P., Luan, G., and Gao, J.-H. (2019). Ems-net: A deep learning method for autodetecting epileptic magnetoencephalography spikes. IEEE transactions on medical imaging, 39(6):1833– 1844.

Zihlmann, M., Perekrestenko, D., and Tschannen, M. (2017). Convolutional recurrent neural networks for electrocardiogram classiﬁcation. In 2017 Computing in Cardiology (CinC), pages 1–4. IEEE.

Zijlmans, M., Huiskamp, G., Hersevoort, M., Seppenwoolde, J.-H., van Huﬀelen, A. C., and Leijten, F. S. (2007). Eeg-fmri in the preoperative work-up for epilepsy surgery. Brain, 130(9):2343–2353.

Zuo, R., Wei, J., Li, X., Li, C., Zhao, C., Ren, Z., Liang, Y., Geng, X., Jiang, C., Yang, X., et al. (2019). Automated detection of high-frequency oscillations in epilepsy based on a convolutional neural network. Frontiers in computational neuroscience, 13:6.

