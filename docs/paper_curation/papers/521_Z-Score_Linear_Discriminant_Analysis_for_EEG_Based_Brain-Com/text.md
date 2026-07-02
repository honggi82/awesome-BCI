# Z-Score Linear Discriminant Analysis for EEG Based BrainComputer Interfaces

Rui Zhang, Peng Xu*, Lanjin Guo, Yangsong Zhang, Peiyang Li, Dezhong Yao*

Key Laboratory for NeuroInformation of Ministry of Education, School of Life Science and Technology, University of Electronic Science and Technology of China, Chengdu, China

|Abstract<br><br>Linear discriminant analysis (LDA) is one of the most popular classification algorithms for brain-computer interfaces (BCI). LDA assumes Gaussian distribution of the data, with equal covariance matrices for the concerned classes, however, the assumption is not usually held in actual BCI applications, where the heteroscedastic class distributions are usually observed. This paper proposes an enhanced version of LDA, namely z-score linear discriminant analysis (Z-LDA), which introduces a new decision boundary definition strategy to handle with the heteroscedastic class distributions. Z-LDA defines decision boundary through z-score utilizing both mean and standard deviation information of the projected data, which can adaptively adjust the decision boundary to fit for heteroscedastic distribution situation. Results derived from both simulation dataset and two actual BCI datasets consistently show that Z-LDA achieves significantly higher average classification accuracies than conventional LDA, indicating the superiority of the new proposed decision boundary definition strategy.<br><br>Citation: Zhang R, Xu P, Guo L, Zhang Y, Li P, et al. (2013) Z-Score Linear Discriminant Analysis for EEG Based Brain-Computer Interfaces. PLoS ONE 8(9): e74433. doi:10.1371/journal.pone.0074433<br><br>Editor: Momiao Xiong, University of Texas School of Public Health, United States of America Received April 27, 2013; Accepted August 1, 2013; Published September , 2013 Copyright: 2013 Zhang et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.<br><br>Funding: This work was supported by grants from 973 program 2011CB707803, the National Nature Science Foundation of China (#61175117, #31070881 and #31100745), the 863 project 2012AA011601, the program for New Century Excellent Talents in University (#NCET-12-0089), the National Science & Technology Pillar Program 2012BAI16B02 and ‘111’ project. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.<br><br>Competing Interests: The authors have declared that no competing interests exist.<br><br>* E-mail: dyao@uestc.edu.cn (DY); xupeng@uestc.edu.cn (PX)<br><br>13|
|---|

Introduction

Brain-computer interfaces (BCI) provide direct connection channel between brain and external world without any peripheral muscular activity [1]. It translates brain activity to signals that control external devices, and there are many augmentative communication and control systems based on BCI [2–6], which improves lives of people with severe neuromuscular disorders.

Generally an EEG based BCI consists of four modules [1]: 1) signal acquisition module to record and amplify EEG signals; 2) feature extraction module to extract signal features that encode user’s intent; 3) translation module to translate features into device command; 4) feedback and control module to synchronize user’s action and achieve control of external devices. The high performance EEG amplifier with suitable reference strategy [7] will increase quality of the recorded EEG signal, and employing innovative paradigms in the feedback and control module may obtain higher quality features and better control strategies [8–11]. Once EEG amplifier as well as reference strategy, and the feedback and control module are determined, feature extraction and translation algorithms will play important roles in improving the performance of BCI. Currently, the conventional features used in scalp EEG based BCI can be attributed to event related potentials, the sensorimotor rhythm, the transient visual potentials and the steady state potentials (including visual and audio). To refine those specific features, many feature extraction algorithms have been proposed [12–15]. However, as an input-output system, the final translation module directly determines whether the

subject’s intention is correctly decoded [16]. Compared to the conventional pattern recognition problems, BCI system requires the translation module to have ability to handle with the small sample size training problem, the heteroscedastic class distribution problem and the nonstationary physiological signals, etc. Therefore, effective translation algorithms specifically suitable for BCI application are still required in BCI discipline [17] [18].

Linear discriminant analysis (LDA) is one of the most popular classification algorithms for BCI application, and has been successfully used in a great number of BCI systems such as motor imagery based BCI [19], P300 speller [20] and steady state movement related potentials based BCI [21]. The original LDA has two derivations [22], fisher LDA (FLDA) and least square LDA (LSLDA). FLDA is based on Fisher-Rao’s criterion [22–24], which is to find the projection w to maximize the objective function J(w)~DwTSbwD DwTSwwD denoting the ratio of betweenclass to within-class variances. LSLDA is derived from a linear discriminant function y(x)~wTx, where the weight vector w is supposed to minimize the mean squared error between wTx and y(x) [25]. The solution of LSLDA will be equivalent to that of FLDA with a proper label coding scheme adopted in LSLDA [25].

Both the two kind of LDAs are under the homoscedasticity assumption that different classes follow Gaussian distribution with same covariance matrices. However, the EEG data recorded from actual BCI system usually have heteroscedastic class distributions, which violates the fundamental assumption of LDA and notably degrades the recognition performance. Heteroscedastic LDA

Table 1. Classification accuracies (%) of Z-LDA and LDA on simulation dataset.

Difference of SDsa 0 0.1rb 0.2r 0.3r 0.4r 0.5r 0.6r 0.7r 0.8r 0.9r

LDA 99.99±0.05 99.9160.22 99.5160.49 98.7960.77 97.5661.09 96.2761.39 95.1561.39 93.9861.38 92.7061.94 91.7061.72 Z-LDA 99.99±0.05 99.97±0.13 99.78±0.35 99.39±0.63 98.95±0.72 98.16±0.97 97.09±1.18 96.22±1.37 95.01±1.53 93.85±2.19 p-value 0.0153 ,1025 ,1028 ,10220 ,10222 ,10220 ,10223 ,10217 ,10212

adenotes the norm of the difference of SDs between the two simulated dataset. br is a constant value, equals to

p

ﬃﬃﬃ 2

. doi:10.1371/journal.pone.0074433.t001

(HLDA) is an extension of FLDA, whose between-class scatter is generalized from Euclidean distance to Chernoff distance with both effects of the class means and their covariance matrices considered [26], thus HLDA does not need the homoscedasticity assumption. Nonparametric discriminant analysis (NDA) is another extension of FLDA [27], which makes no prior assumption for the class distributions, the parameters can be estimated by k nearest neighbor method and then they are used to define the between-class scatter [28].

In essence, LDA linearly transforms data from high dimensional space to low dimensional space, and finally the decision is made in the low dimensional space, thus the definition of the decision boundary plays an important role on the recognition performance.

Conventional LDA defines the mean of the projected data as the decision boundary due to the homoscedasticity assumption [25]. Nearest neighbor of classes has also been proposed to serve as the decision boundary [29]. Different from LDA, support vector machine (SVM) firstly maps the data to a high dimensional space, and then finds a hyperplane in the high dimensional space so that the distance from the hyperplane to the nearest data point on each side is maximized [30], theoretically the hyperplane is determined only by a small amount of the training data which are called support vectors. During the classification procedure of LDA, the heteroscedastic class distributions will be still kept in the projected space. Therefore, we argue that if the mean and variance of the projected data could be considered for the definition of the

[Figure 1]

- Figure 1. The decision boundaries of Z-LDA and LDA defined from training set. Blue circles are the weight sum y(x) of the first class, blue solid line denotes the Gaussian distribution curve they subject to; red stars are the weight sum y(x) of the second class, red solid line denotes the Gaussian distribution curve they subject to; green dashed line denotes the decision boundary of LDA, c~0, and green solid line denotes the decision boundary of Z-LDA, c ~{0:34.

- doi:10.1371/journal.pone.0074433.g001

[Figure 2]

- Figure 2. The classification performance of Z-LDA and LDA on test samples. Blue circles are the test samples of the first class; red stars are the test samples of the second class; green dashed line denotes the decision boundary of LDA; green solid line denotes the decision boundary of ZLDA.

- doi:10.1371/journal.pone.0074433.g002

decision boundary, it may extend LDA to deal with the practical heteroscedastic distribution data, which is the derivation point for the proposed Z-LDA in this paper.

The paper is organized as follows. Section Methods and Materials provides a detailed description of z-score LDA (Z-LDA); The results of simulation dataset and motor imagery EEG datasets are showed in section Results; In section Discussions, there is a general discussion of the proposed algorithm; Section Conclusion gives a summary of this work.

Materials and Methods

1. Linear Discriminant Analysis

To simplify the description of the algorithm, we only consider the case of two classes. Assume (x11,x12,:::,x1m)[C1 and (x21,x22,:::,x2n)[C2, with m and n being the number of samples, are the samples in the two class sets C1 and C2. LetX~(x11,x12,:::,x1m,x21,x22,:::,x2n), then the simplest representation of a linear discriminant function is obtained by taking a linear function of the input vector so that

y(X)~wTXzw0 ð1Þ

where w is called a weight vector, and w0 is a bias. Using vector notation, equation (1) can be converted to

y(X~)~W~ TX~ ð2Þ

w w0

and X~ is the corresponding augmented input

where W~ ~

vector XT,1 T with a dummy input x0~1. Accordingly, the least square solution of equation (2) is [25]

W~ ~ X~TX~ {1X~Ty ð3Þ

With W~ estimated in equation (3), the corresponding weight sum y(x) can be achieved. For conventional LDA, classification for an input x is based on the comparison of y(x) and threshold, i.e., the decision boundary. If we consider c1 as the label of class C1,c2 as the label of class C2, the corresponding decision boundary can be defined by c~(c1zc2)=2.

2. Z-score Linear Discriminant Analysis

Theoretically, the decision boundary of LDA is derived by assuming the homoscedasticity distribution for the two classes. Thus it may not be competitive to the heteroscedastic distribution, and we will develop the following strategy to define a more robust decision boundary.

- Table 2. Classification accuracies (%) comparison on Dataset IVa of BCI Competition III.

Subjects aa al av aw ay Mean±Std

LDA 76.8 100 67.3 97.8 56.7 79.7618.9 Z-LDA 77.7 100 68.4 99.6 59.9 81.1618.2 SVM 75.9 100 71.9 98.2 53.6 79.9619.4 NDA 75.9 100 64.3 97.8 70.6 81.7616.2 HLDA 57.1 100 46.9 97.3 72.2 74.7623.7

- doi:10.1371/journal.pone.0074433.t002

Table 3. Classification accuracies (%) comparison on Dataset recorded by our BCI system.

Subjects 1 2 3 4 5 6 7 8 9 10 11 12 13 14 Mean±Std

LDA 94 84 95 69 82 63 78 87 70 56 84 81 63 99 78.9613.1 Z-LDA 95 85 95 71 83 66 80 87 73 59 84 82 65 99 80.3612.1 SVM 94 77 93 69 84 61 71 87 75 59 84 83 67 99 78.8612.4 NDA 92 81 96 62 82 63 70 87 67 55 81 81 59 98 76.7614.1 HLDA 51 79 90 51 49 47 48 49 42 48 63 43 55 55 55.0613.7

- doi:10.1371/journal.pone.0074433.t003

Based on the estimated W~ obtained by equation (3), the weight sum y(x) for each training sample can be calculated from equation (2), and then the parameters of the Gaussian distributions of the weight sum y(x) related to the two classes can be estimated as,

1 m Xx[C1

m1~

y(x)

1 n Xx[C2

m2~

y(x)

ð4Þ

- s1~ ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ

1 mXx[C1

r (y(x){m1)2

- s2~ ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ

r (y(x){m2)2

1 n Xx[C2

where mk,sk(k~1,2) are the corresponding mean and standard deviation (SD) of the weight sum y(x) for training set Ck(k~1,2). During classification, when a new sample x is input, firstly calculate the weight sum y(x ) by equation (2), then perform the following normalization procedure,

- z1~

y(x ){m1 s1

- z2~

y(x ){m2 s2

ð5Þ

In essence, z1 and z2 are the transformed z-scores to measure how much the weight sum y(x ) of the newly input sample is close to the two weight sum distributions predefined by the training set, thus the method is called z-score linear discriminant analysis (ZLDA). Finally, if Dz1DvDz2D, the sample is classified into C1, otherwise, the sample belongs to C2. Assume the weight sum of samples in the two classes subject to Gaussian distribution with

parameters mk,sk(k~1,2), then the proposed decision boundary is the intersection of the two Gaussian distribution curves.

The above descriptions are based on LSLDA, since the only difference between LSLDA and FLDA is the way to estimate the weight vector w, and the solutions of them are substantially equal. Therefore, the proposed decision boundary definition strategy can be extended to FLDA, too.

3. Relationship between LDA and Z-LDA

Theoretically, the decision boundary of conventional LDA is defined by

c{c1~c2{c ð6Þ

Based on equation (6), the decision boundary of conventional LDA is the mean of labels of two classes, i.e. c~(c1zc2)=2. Obviously, when the SDs are combined into classification, the decision boundary of Z-LDA is defined as

(c {m1)=s1~{(c {m2)=s2 ð7Þ which deduces a value

c ~(s1m2zs2m1)=(s1zs2) ð8Þ

Apparently, the decision boundary c of Z-LDA is defined by both the mean and SD of the weight sum of two classes.

In the binary classification, the expectation of mean of the

weight sum y(x) for training set is E(m1)~c1and E(m2)~c2, the decision boundary of conventional LDA is theoretically equal to

c~(m1zm2)=2. When the weight sum of two classes have equal SDs, the decision boundary of Z-LDA will also reduce to

c ~(m1zm2)=2. Therefore, the conventional LDA is a particular case of Z-LDA.

Results

1. Evaluation on Simulation Dataset

1.1. Simulation dataset description. In this section, we constructed a simulated dataset in order to investigate the capability of Z-LDA in dealing with the two class classification with heteroscedastic class distributions. The simulation was performed by using the fundamental two 2-dimensional Gaussian distributions, where the samples in the first class follow a Gaussian distribution with mean (21, 20.6) and standard deviation (0.3, 0.3), and the samples in the second class follow a Gaussian distribution with mean (1, 0.6) and standard deviation (0.3, 0.3). To generate datasets with heteroscedastic class distributions, we

[Figure 3]

- Figure 3. Distribution of the weight sum y(x) of subject 1. Blue dashed line is the Gaussian distribution curve according to the characteristic of weight sum y(x) with left hand motor imagery in training set; red dashed line is the Gaussian distribution curve according to the characteristic of weight sum y(x) with right hand motor imagery in training set; blue circles denote the weight sum y(x) with left hand motor imagery in test set; red stars denote the weight sum y(x) with right hand motor imagery in test set; blue solid line is the Gaussian distribution curve derived from the blue circles; red solid line is the Gaussian distribution curve derived from the red stars; green dashed vertical line is the decision boundary defined by LDA from training set; green solid vertical line is the decision boundary defined by Z-LDA from training set; black solid vertical line is the theoretical boundary of test set.

- doi:10.1371/journal.pone.0074433.g003

changed the SD of the second class step by step, and then performed the comparison between LDA and Z-LDA on those datasets. Training set and test set with each consisting of 200 2dimensional samples (100 for each class) were generated respectively.

1.2. Classification performance of LDA and ZLDA. After the simulated datasets with heteroscedastic class distributions are generated, the training model of LDA and ZLDA were estimated from the training set respectively, and the models were then applied to classify the samples in the test set. The above procedure was repeated 100 times to lower the random effect, and paired t-test was performed to investigate whether the statistical difference exists between the two classifiers. Table 1 listed the mean and standard deviation of classification accuracies for the 100 runs. Figure 1 visually gived the decision boundary definition procedure for the two classifiers when the standard deviation of the first class is (0.3, 0.3), and (1.0, 1.0) for the second class. Figure 2 intuitively showed the difference of recognition performance for the test dataset based on the two decision boundaries in Figure 1.

When SDs of two classes are same, LDA and Z-LDA achieved equal classification accuracy. But while we changed the SD of the second class with that of the first class kept, though the classification accuracies for both two classifiers are lowered, Z-

LDA achieved higher classification accuracy than LDA. Paired ttest revealed that when the difference of SD between the two classes exists, Z-LDA would achieve the significantly higher classification accuracy than that of LDA (p,0.05), where the more obvious improvement could be observed for those simulations with more differences in SD.

2. Evaluations on Real BCI Dataset

2.1. BCI dataset description. 1) Dataset IVa of BCI Competition III. This dataset contains EEG signals recorded from five subjects using 118 electrodes [31]. In each trial, a visual cue was shown for 3.5 s, during which three motor imageries were performed, i.e., left hand, right hand and right foot. The motor imageries of right hand and foot were needed to be classified. The total number of EEG trials for each subject was 280. Specifically, 168, 224, 84, 56, and 28 trials were used as training data corresponding to the five subjects: aa, al, av, aw, and ay, respectively. The data were band-pass filtered between 0.05 and 200 Hz and down-sampled at 100 Hz for succedent analysis.

2) Dataset recorded by our BCI system. This dataset comes from our group, consists of EEG data from 14 subjects (11 males and 3 females, right handed, 19–25 years old). The experimental protocol was approved by the Institution Research Ethics Board at University of Electronic Science & Technology of China. All

participants were asked to read and sign an informed consent form before participating in the study. After experiment, all the participants received a monetary compensation for their time and effort. Subjects sat in a comfortable armchair in front of a computer screen, they were asked to perform motor imagery with left hand or right hand according to the instructions appeared on the screen. Motor imagery lasts for 5 seconds, and follows a 5 seconds rest. 15 Ag/AgCl electrodes covers sensorimotor area were used for EEG recordings with Symtop Amplifier (Symtop Instrument, Beijing, China), the signals were sampled with 1000 Hz and band pass filtered between 0.5 Hz and 45 Hz. 4 runs on the same day were recorded for each subject, each run consists of 50 trials, 25 trials for each class, and there is a 3 minutes break between the consecutive two runs. The first 2 runs are treated as training set and the last 2 runs are treated as test set.

2.2. Preprocessing. We used the EEG segments recorded from 0.5 s to 3.75 s after the visual cue for the following analysis according to [32] on the first dataset. For the second dataset, all the EEG segments during motor imagery were selected for analysis, and those trials with absolute amplitude above 300 mv threshold were considered to be contaminated with strong ocular artifacts and will be removed from analysis. Next, the specific optimal frequency band for each subject was obtained by r2 [33], and then it was used to design band pass filter for the selected EEG segments.

- 2.3. Feature extraction. Common spatial pattern (CSP)

analysis was used to estimate the spatial projection matrix, which projects the EEG signal from original sensor space to a surrogate sensor space [13,19]. Each row vector of the projection matrix is a spatial filter, which maximizes the variance of the spatially filtered signal under one task while minimizing the variance of the spatially filtered signal under the other task. The most discriminative 3 pairs of optimal spatial filters in the projection matrix were selected to transform the band pass filtered EEG signal, then the logarithm of the variance of the transformed surrogate channel EEG signals were served as the final features for task recognition. In general, each EEG segment was transformed to a 6dimensional vector feature after the above procedure.

- 2.4. Classification results. In this section, we will compare

the classification performance of Z-LDA to LDA, SVM, NDA and HLDA. LIBSVM with default parameter was served as SVM classifier [34]. NDA in reference [28] with 5 as the number of k nearest neighbors, and HLDA in reference [26] were used for evaluation in current work.

The classification results of Dataset IVa of BCI Competition III

- were summarized in Table 2. Z-LDA and NDA achieved higher average accuracy than LDA, SVM and HLDA. Though the average accuracy of NDA is slightly larger than that of Z-LDA, ZLDA had the better performance for 4 of 5 subjects with exception for subject ay, and the paired t test did not show the statistical difference between them (p =0.4146). There are only 28 training samples for subject ay, which is a small size training problem. NDA is good at dealing with the small size training problem, resulting in the obvious improvement for subject ay. Across the 5 subjects, when LDA is regarded as the baseline for evaluation, only Z-LDA showed the consistent improvement for all the 5 subjects, and the paired t test also revealed that only the accuracies obtained by ZLDA is significantly higher than that of LDA (p =0.0293).

The classification results of Dataset recorded by our BCI system

- were summarized in Table 3. Z-LDA achieved the highest mean accuracy among the tested 5 classifiers. Paired t test also showed that the accuracies obtained by Z-LDA is significantly higher than LDA (p =0.0004), NDA (p =0.0006) and HLDA (p,1025), but no statistical difference between Z-LDA and SVM (p =0.0654).

The overall mean accuracies obtained by Z-LDA are 1.4% higher than that of LDA on both of the two BCI datasets. As shown in Table 2 and 3, we could also see that the accuracies obtained by Z-LDA is consistently better than (or at least equal to) LDA in all of the subjects.

Subject 1 from Dataset recorded by our BCI system was used as an example to briefly reveal why the classification performance of Z-LDA becomes better than conventional LDA in the actual situation. The distribution of weight sum y(x) when subject 1 performed the motor imagery with left hand and right hand were plotted in Figure 3 for the training and test sets, respectively. The decision boundaries of Z-LDA and LDA were also marked in Figure 3.

Discussion

Translation module of BCI receives features from previous feature extraction module and translates them to device command by using certain classification algorithms. In practical BCI situations, the concerned tasks may have heteroscedastic class distributions. Therefore, the consideration of effect of distribution variances may provide more robust ability to recognize the tasks. However, the conventional LDA assumes homoscedastic class distributions, which may not be competitive to handle with actual BCI dataset with heteroscedastic class distributions. Inspired by this, we develop Z-LDA by including the variance information in the classification procedure in order to provide more robust classification for BCI tasks.

As shown in Section Methods and Materials, the decision boundary of conventional LDA is decided by the labels of classes, while the decision boundary of Z-LDA is defined by both mean and SD of the weight sum, which is more potential to capture the distribution information of classes and provide better classification performance for heteroscedastic distribution situation.

The difference of decision boundaries between the two classifiers can be clearly observed in Figure 1. Assume we define the label of the two classes as 21 and 1, the decision boundary of LDA is fixed as c~0, while the decision boundary of Z-LDA is determined by equation (8). If the SD of two classes are same, the decision boundary of Z-LDA is also c ~0, but when the SDs of two classes are different, the decision boundary of Z-LDA will move toward the class with smaller SD. From Figure 1 we can find that because of the small SD of the first class, the SD of weight sum y(x) is also small, resulting in the more concentrated distribution compared to the relatively divergent distribution of class 2 with larger SD. Considering the areas under the two Gaussian curves between the two decision boundaries, the area corresponding to the second class is obviously large than that of that of the first class, which denotes that with the new defined decision boundary, more samples can be correctly recognized. Figure 2 further reveals that if the decision boundary of LDA is used in the test dataset, many samples belong to the second class will be incorrectly assigned to the first class. But if we use the decision boundary of Z-LDA to classify the samples, the number of samples which incorrectly assigned to the first class will be reduced at the cost that some samples belong to the first class will be incorrectly assigned to the second class.

When applied to the actual BCI datasets, Z-LDA consistently shows the best average accuracies among the concerned five classifiers as shown in Table 2 and Table 3. Figure 3 clearly shows us that the weight sum for the two types of tasks actually follow different Gaussian distributions in practical BCI application. In this case, the decision boundary of Z-LDA obtained from the training set is the green solid line, which is smaller than 0, and the

decision boundary of LDA is the green dashed line, which equals to 0. The black solid line in Figure 3 denotes the theoretical boundary for the test dataset. Obviously, the decision boundary of Z-LDA determined by the training set is more close to the theoretical boundary of the test dataset, leading to the better classification achieved by Z-LDA compared to LDA. Therefore, we can conclude that the proposed decision boundary definition strategy outperforms the conventional decision boundary definition strategy in actual BCI applications, where concerned samples usually have the heteroscedastic distribution.

Another concerned aspect is the algorithm complexity for the online BCI system. In current work, the algorithm is implemented with Matlab R2011b running on Windows 7 Ultimate SP1 64 bit with Intel Core i5-3470 CPU 3.2 Ghz. The mean time for 200 2dimensional samples in the simulation study using Z-LDA is 0.0004 s, and 0.0001 s for LDA. It indicates Z-LDA is applicable in the practical real time BCI.

Conclusion

Both the simulation and actual BCI datasets confirm that ZLDA is a more robust classification method. In essence, Z-LDA is an enhanced version of LDA, and it can be reduced to the conventional LDA by assuming homoscedastic class distributions.

References

- 1. Wolpaw JR, Birbaumer N, McFarland DJ, Pfurtscheller G, Vaughan TM (2002) Brain-computer interfaces for communication and control. Clin Neurophysiol 113: 767–791.
- 2. Scherer R, Muller GR, Neuper C, Graimann B, Pfurtscheller G (2004) An asynchronously controlled EEG-based virtual keyboard: improvement of the spelling rate. IEEE Trans Biomed Eng 51: 979–984.
- 3. Galan F, Nuttin M, Lew E, Ferrez PW, Vanacker G, et al. (2008) A brainactuated wheelchair: asynchronous and non-invasive Brain-computer interfaces for continuous control of robots. Clin Neurophysiol 119: 2159–2169.
- 4. Cincotti F, Mattia D, Aloise F, Bufalari S, Schalk G, et al. (2008) Non-invasive brain-computer interface system: towards its application as assistive technology. Brain Res Bull 75: 796–803.
- 5. Buch E, Weber C, Cohen LG, Braun C, Dimyan MA, et al. (2008) Think to move: a neuromagnetic brain-computer interface (BCI) system for chronic stroke. Stroke 39: 910–917.
- 6. Wolpaw JR, McFarland DJ (2004) Control of a two-dimensional movement signal by a noninvasive brain-computer interface in humans. Proc Natl Acad Sci U S A 101: 17849–17854.
- 7. Yao D (2001) A method to standardize a reference of scalp EEG recordings to a point at infinity. Physiol Meas 22: 693–711.
- 8. Jin J, Allison BZ, Kaufmann T, Kubler A, Zhang Y, et al. (2012) The Changing Face of P300 BCIs: A Comparison of Stimulus Changes in a P300 BCI Involving Faces, Emotion, and Movement. PLoS One 7: e49688.
- 9. Bermudez i Badia S, Garcia Morgade A, Samaha H, Verschure P (2013) Using a Hybrid Brain Computer Interface and Virtual Reality System to Monitor and Promote Cortical Reorganization through Motor Activity and Motor Imagery Training. IEEE Trans Neural Syst Rehabil Eng 21: 174–181.
- 10. Qian K, Nikolov P, Huang D, Fei DY, Chen X, et al. (2010) A motor imagerybased online interactive brain-controlled switch: paradigm development and preliminary test. Clin Neurophysiol 121: 1304–1313.
- 11. Royer AS, He B (2009) Goal selection versus process control in a braincomputer interface based on sensorimotor rhythms. J Neural Eng 8: 036012.
- 12. Bashashati A, Fatourechi M, Ward RK, Birch GE (2007) A survey of signal processing algorithms in brain-computer interfaces based on electrical brain signals. J Neural Eng 4: R32–57.
- 13. Muller-Gerking J, Pfurtscheller G, Flyvbjerg H (1999) Designing optimal spatial filters for single-trial EEG classification in a movement task. Clin Neurophysiol 110: 787–798.
- 14. McFarland DJ, Wolpaw JR (2008) Sensorimotor rhythm-based brain-computer interface (BCI): model order selection for autoregressive spectral analysis. J Neural Eng 5: 155–162.
- 15. Shahid S, Prasad G (2011) Bispectrum-based feature extraction technique for devising a practical brain-computer interface. J Neural Eng 8: 025014.
- 16. McFarland DJ, Sarnacki WA, Wolpaw JR (2003) Brain-computer interface (BCI) operation: optimizing information transfer rates. Biol Psychol 63: 237– 251.
- 17. Li Y, Guan C, Li H, Chin Z (2008) A self-training semi-supervised SVM algorithm and its application in an EEG-based brain computer interface speller system. Pattern Recognition Letters 29: 1285–1294.

Moreover, the probability indicates how reliable the classification is performed could be derived from the z-score transformed weight sum, which may be helpful to handle with the adaptive calibration problem [17,33,35].

There are various algorithms have been proposed based on LDA in BCI application, such as regularized LDA [36,37], Bayesian LDA (BLDA) [38] and enhanced BLDA [33]. Unlike ZLDA, these algorithms improved LDA’s performance from other aspects like regularization, Bayesian frameworks. It is possible to combine the proposed decision boundary definition strategy with these algorithms, which is our future work. Moreover, we will also implement the proposed Z-LDA to our online BCI system.

Acknowledgments

The authors would like to thank the Berlin BCI group, Germany for sharing their datasets. We also thank the anonymous reviewers for their insightful comments.

Author Contributions

Conceived and designed the experiments: RZ PX LG. Performed the experiments: RZ LG. Analyzed the data: RZ PL. Contributed reagents/ materials/analysis tools: RZ PX YZ DY. Wrote the paper: RZ PX DY.

- 18. Lotte F, Congedo M, Lecuyer A, Lamarche F, Arnaldi B (2007) A review of classification algorithms for EEG-based brain-computer interfaces. J Neural Eng 4: R1–R13.
- 19. Guger C, Ramoser H, Pfurtscheller G (2000) Real-time EEG analysis with subject-specific spatial patterns for a brain-computer interface (BCI). IEEE Trans Rehabil Eng 8: 447–456.
- 20. Bostanov V (2004) BCI Competition 2003–Data sets Ib and IIb: feature extraction from event-related brain potentials with the continuous wavelet transform and the t-value scalogram. IEEE Trans Biomed Eng 51: 1057–1061.
- 21. Nazarpour K, Praamstra P, Miall RC, Sanei S (2009) Steady-state movement related potentials for brain-computer interfacing. IEEE Trans Biomed Eng 56: 2104–2113.
- 22. Webb AR (2002) Statistical pattern recognition. West Sussex: Wiley.
- 23. Fisher RA (1936) The use of multiple measurements in taxonomic problems. Annals of Eugenics 7: 179–188.
- 24. Rao CR (1948) The utilization of multiple measurements in problems of biological classification. Journal of the Royal Statistical Society Series B (Methodological) 10: 159–203.
- 25. Bishop CM (2006) Pattern recognition and machine learning. New York: Springer.
- 26. Loog M, Duin RP (2004) Linear dimensionality reduction via a heteroscedastic extension of LDA: the Chernoff criterion. IEEE Trans Pattern Anal Mach Intell 26: 732–739.
- 27. Fukunaga K (1990) Introduction to statistical pattern recognition. Boston: Academic Press.
- 28. Li Z, Lin D, Tang X (2009) Nonparametric discriminant analysis for face recognition. IEEE Trans Pattern Anal Mach Intell 31: 755–761.
- 29. Hastie T, Tibshirani R (1996) Discriminant adaptive nearest neighbor classification. IEEE Trans Pattern Anal Mach Intell 18: 607–616.
- 30. Cortes C, Vapnik V (1995) Support-vector networks. Machine Learning 20: 273–297.
- 31. Blankertz B, Muller KR, Krusienski DJ, Schalk G, Wolpaw JR, et al. (2006) The BCI competition. III: Validating alternative approaches to actual BCI problems. IEEE Trans Neural Syst Rehabil Eng 14: 153–159.
- 32. Lotte F, Guan C (2011) Regularizing Common Spatial Patterns to Improve BCI Designs: Unified Theory and New Algorithms. IEEE Trans Biomed Eng 58: 355–362.
- 33. Xu P, Yang P, Lei X, Yao D (2011) An enhanced probabilistic LDA for multiclass brain computer interface. PLoS One 6: e14634.
- 34. Chang C-C, Lin C-J (2001) LIBSVM: a library for support vector machines.
- 35. Vidaurre C, Kawanabe M, von Bunau P, Blankertz B, Muller KR (2011) Toward unsupervised adaptation of LDA for brain-computer interfaces. IEEE Trans Biomed Eng 58: 587–597.
- 36. Friedman JH (1989) Regularized Discriminant Analysis. Journal of the American Statistical Association 84: 165–175.
- 37. Mu¨ller Kr, Krauledat M, Dornhege G, Curio G, Blankertz B (2004) Machine learning techniques for brain-computer interfaces. Biomed Technol 49: 11–22.
- 38. Lei X, Yang P, Yao D (2009) An empirical bayesian framework for braincomputer interfaces. IEEE Trans Neural Syst Rehabil Eng 17: 521–529.

