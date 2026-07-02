# arXiv:1805.01044v1[cs.LG]2May2018

## Covariate Shift Estimation based Adaptive Ensemble Learning for Handling Non-Stationarity in Motor Imagery related EEG-based Brain-Computer Interface

#### Haider Razaa,∗, Dheeraj Ratheeb, Shang-Ming Zhouc,∗, Hubert Cecottid, Girijesh Prasadb

aSchool of Computer Science and Electronic Engineering, University of Essex, Colchester, UK bSchool of Computing and Intelligent Systems, Ulster University, Magee campus, Derry Londonderry, UK cThe Farr Institute of Health Informatics Research, Swansea University, Swansea, UK dDepartment of Computer Science, California State University Fresno, Fresno, CA, USA

### Abstract

The non-stationary nature of electroencephalography (EEG) signals makes an EEG-based brain-computer interface (BCI) a dynamic system, thus improving its performance is a challenging task. In addition, it is well-known that due to non-stationarity based covariate shifts, the input data distributions of EEG-based BCI systems change during inter- and intra-session transitions, which poses great diﬃculty for developments of online adaptive data-driven systems. Ensemble learning approaches have been used previously to tackle this challenge. However, passive scheme based implementation leads to poor eﬃciency while increasing high computational cost. This paper presents a novel integration of covariate shift estimation and unsupervised adaptive ensemble learning (CSE-UAEL) to tackle nonstationarity in motor-imagery (MI) related EEG classiﬁcation. The proposed method ﬁrst employs an exponentially weighted moving average model to detect the covariate shifts in the common spatial pattern features extracted from MI related brain responses. Then, a classiﬁer ensemble was created and updated over time to account for changes in streaming input data distribution wherein new classiﬁers are added to the ensemble in accordance with estimated shifts. Furthermore, using two publicly available BCI-related EEG datasets, the proposed method was extensively compared with the state-of-the-art single-classiﬁer based passive scheme, single-classiﬁer based active scheme and ensemble based passive schemes. The experimental results show that the proposed active scheme based ensemble learning algorithm signiﬁcantly enhances the BCI performance in MI classiﬁcations.

Keywords: Brain-computer interface (BCI), covariate shift, electroencephalogram (EEG), ensemble learning, non-stationary learning.

∗Haider Raza and Shang-Ming Zhou are the joint corresponding authors

Email addresses: h.raza@essex.ac.uk (Haider Raza), rathee-d@email.ulster.ac.uk (Dheeraj Rathee), s.zhou@swansea.ac.uk (Shang-Ming Zhou), hcecotti@csufresno.edu (Hubert Cecotti), g.prasad@ulster.ac.uk (Girijesh Prasad)

Preprint submitted to Elsevier May 4, 2018

### Acronyms

BCI: Brain-computer-interface CS: Covariate shift CSP: Common spatial pattern CSA: Covariate shift adaptation CSE: Covariate shift estimation CSE-UAEL: CSE-based unsupervised adaptive ensemble learning

- CSV: Covariate shift validation
- CSW: Covariate shift warning DWEC: Dynamically weighted ensemble classiﬁcation EEG: Electroencephalography ERD: Synchronization ERS: Desynchronization FB: Frequency band FBCSP: Filter bank common spatial pattern EWMA: exponential weighted moving average KNN: K-nearest-neighbors LDA: Linear discriminant analysis MI: Motor imagery NSL: Non-stationary learning PCA: Principal component analysis PWKNN: Probabilistic weighted K-nearest neighbour RSM: Random subspace method SSL: Semi-supervised learning

### 1. Introduction

Streaming data analytics has increasingly become the bedrock in many domains, such as bio-medical sciences, healthcare, and ﬁnancial services. However, the majority of streaming data systems assume that the distributions of streaming data do not change over time. In reality, the streaming data obtained from real-world systems often possess non-stationary characteristics [1]. Such systems are often characterized by continuous evolving natures and thus, their behaviours often shift over time due to thermal drifts, aging eﬀects, or other non-stationary environmental factors etc. These characteristics can adversely aﬀect environmental, natural, artiﬁcial and industrial processes [2]. Hence, adaptive learning in a non-stationary environment (NSE), wherein the input data distribution shifts over time, is a challenging task. Developing machine learning models that can be optimized for nonstationary environments is in high demand. Currently machine learning methods for nonstationary systems are majorly categorized into passive and active approaches [2]. In the passive approach to non-stationary learning (NSL), it is assumed that the input distribution should be continuously shifting over time [3, 2]. Thus, passive scheme based methods adapt to new data distributions continuously for each new incoming observation or a new batch

of observations from the streaming data. In contrast, an active scheme based NSL method uses a shift detection test to detect the presence of shifts in the streaming data, and an adaptive action is initiated based upon the time of detected shift[4]. There exits a range of literature on transfer learning and domain adaptation theory, which aims to adapt to NSEs by transferring knowledge between training and test domains. In this case, one can match the features distribution of training and testing by the density ratio estimation approaches such as kernel mean matching [5], Kullback-Leibler importance estimation procedure, and least-squares importance ﬁtting [6]. In addition to density ratio estimation methods, several methods, such as domain adaption with conditional transferable components, try to minimize the domain shift by ﬁnding invariant representation across training and target domains [7]. In fact, to favorably transfer knowledge between domains, one needs to estimate the primary causal mechanism of the data generating process. These methods have, however, a limited applicability in real world problems, where the data in test domain are generated while operating in real-time.

A typical brain-computer-interface (BCI) system aims to provide an alternative means of communication or rehabilitation for the physically challenged population so as to allow them to express their wills without muscle exertion [8]. An electroencephalography (EEG)-based BCI is such a non-stationary system [9] and quasi-stationary segment in EEG signals have duration of nearly 0.25 sec [10]. The non-stationarities of the EEG signals may be caused by various events, such as changes in the user attention levels, electrode placements, or user fatigues [11, 12, 13]. In other words, the basic cause of the non-stationarity in EEG signals is not only associated with the inﬂuences of the external stimuli to the brain mechanisms, but the switching of the cognitive task related inherent metastable states of neural assemblies also contributes towards it [14]. These non-stationarities cause notable variations or shifts in the EEG signals both during trial-to-trial, and session-to-session transfers [15, 13, 16, 17]. As a result, these variations often appear as covariate shifts (CSs) wherein the input data distributions diﬀer signiﬁcantly between training and testing phases while the conditional distribution remains the same [6, 18, 19, 20, 21].

Non-invasive EEG-based BCI systems acquire neural signals at scalp level to be analysed for evaluating activity-speciﬁc features of EEG signals e.g. voluntary imagery/execution tasks, and ﬁnally the output signals are relayed to diﬀerent control devices [8]. The EEG signals are acquired through a multichannel EEG ampliﬁer, and a pre-processing step is performed to remove noise and enhance the signal-to-noise ratio. Then the discriminable features are extracted from the artefact-cleaned signals using feature extraction techniques, such as spatial ﬁltering (e.g., common spatial pattern (CSP)) [22]. Such a system operates typically in two phases, namely the training phase and the testing phase [23]. However, due to the non-stationary nature of the brain response characteristics, it is diﬃcult to accurately classify the EEG patterns in motor imagery (MI) related BCI systems using traditional inductive algorithms [24, 23]. For EEG-based BCI systems that operate online under realtime non-stationary/changing environments, it is required to consider the input features that are invariant to dataset shifts, or the learning approaches that can track the changes

repeating over time, and the learning function can be adapted in a timely fashion. However, the traditional BCI systems are built upon passive approach to NSL for EEG signals. In passive schemes, both single and ensemble classiﬁers have been developed to improve the MI classiﬁcation performance. In contrast, an active scheme based NSL in BCI systems provide a new option by estimating CSs in the streaming EEG features, in which an adaptive action can be initiated once the CS is conﬁrmed. Our previous studies have demonstrated that the active approach to single-trial EEG classiﬁcation outperformed existing passive approaches based BCI system [25, 24, 26, 11, 27, 28].

The aim of this paper is to extend our previous work and present a novel active scheme based unsupervised adaptive ensemble learning algorithm to adapt to CSs under nonstationary environments in EEG-based BCI systems. Diﬀerent from the existing passive scheme based methods, the proposed algorithm is an active ensemble learning approach under non-stationary environments wherein a CS estimation test is used to detect at which point an updated classiﬁer needs to be added to the ensemble during the evaluation phase. The transductive learning is implemented to enrich the training dataset during the evaluation phase using a probabilistic weighted K nearest neighbour (PWKNN) method. Thus, a new classiﬁer is added to the ensemble only when it is necessary, i.e. once the data from a novel distribution has to be processed. Speciﬁcally, we considered an exponential weighted moving average (EWMA) based algorithm for the estimation of CSs in non-stationary conditions [19]. To assess the performance of the proposed algorithm, this study extensively compared the proposed method with various existing passive ensemble learning algorithms: Bagging, Boosting, and Random Subspace; and an active ensemble learning via linear discriminant analysis (LDA)-score based probabilistic classiﬁcation. A series of experimental evaluations have been performed on two publicly available MI related EEG datasets.

The contributions of the paper are summarized as follows:

- • An active adaptive ensemble learning algorithm is proposed wherein new classiﬁers are added online to the ensemble based on covariate shift estimation.
- • The adaptation is performed in unsupervised mode using transduction via PWKNN classiﬁcation.
- • The proposed system is applied to motor imagery based BCI to better characterise the non-stationary changes that occur across and within diﬀerent sessions.

The remainder of this paper proceeds as follows: Section II presents background information for CS, NSL methods in BCI and ensemble learning methods. Section III details the proposed methodology for estimating the CSs and related adaptive ensemble algorithm. Section IV describes the proposed MI related BCI system, and gives a description of the datasets and the signal processing pipeline. Next, Section V presents the performance analysis. Finally, the results are discussed in Section VI and Section VII summarises the ﬁndings of this study.

###### Covariate Shift in CSP features

|TrC1 TrC2 TsC1 TsC2 Tr Plain Ts Plain<br><br>|
|---|

(a) (b)

- Figure 1: Covariate shift (CS) between the training (Tr) and test (Ts) distributions of subject A07 in dataset-2A. (a) illustrates the CS in the mu (µ) band and (b) shows the CS in the beta (β) band.

### 2. Background

- 2.1. Covariate Shift in EEG Signals In a typical BCI system, CS is a case where the input distribution of the data shifts i.e.

(Ptrain(x) = Ptest(x)), whereas the conditional probability remains the same i.e. (Ptrain(y|x) =

Ptest(y|x), while transitioning from the training to testing stage. Fig. 1 illustrates the CS presence in EEG data of the subject A07 in dataset-2A (the description of the dataset is present in section IV). The blue solid ellipse shows the training distribution Ptrain(x) and blue solid line presents the classiﬁcation hyperplane for training dataset. Similarly, the red dashed ellipse shows the test distribution Ptest(x) and the red dash line presents the classiﬁcation hyperplane for the test dataset. Fig.1.(a) and Fig.1.(b) provide the CSP features for (µ) band [8 − 12] Hz and beta (β) band [14 − 30] Hz, respectively.

- 2.2. Non-Stationary Learning in EEG-based BCI

The low classiﬁcation accuracy of the existing BCI systems has been one of the main concerns in their rather low uptake among people with a severe physical disability [29]. To enhance the performance of MI related BCI systems, various signal processing methods have been proposed to extract eﬀective features in the temporal and spatial domains that can characterise the non-stationarity in EEG signals. For example, in the temporal domain, band-power and band-pass based ﬁltering methods are commonly used [15], whereas in the spatial domain, common averaging, current source density [30], and CSP-based features have been examined for the detection of MI related responses [22, 31].

Machine learning researchers have made eﬀorts to devise adaptive BCI systems by incorporating NSL mechanisms into adaptation to improve the performances. Vidaurre et al. [25] have developed a classiﬁer using an adaptive estimation of information matrix. Shenoy et al. [24] have provided quantiﬁed systematic evidence of statistical diﬀerences in data recorded during multiple sessions and various adaptive schemes were evaluated to enhance the BCI performance. A CS minimization method was proposed for the non-stationary adaptation

to reduce feature set overlap and unbalance for diﬀerent classes in the feature set domain [26]. More interestingly, Li et al.(2010) has proposed an unsupervised CS adaptation based on a density ratio estimation technique[11]. There exists a limitation that the density ratio based adaptation method requires all the testing unlabeled data before starting the testing phase to estimate the importance for the non-stationarity adaptation. This makes the approach impractical in real-time BCI applications such as communication or rehabilitation [32]. To tackle these challenges, ensemble machine learning has emerged for NSL, where a set of classiﬁers is coupled to provide an overall decision. The generalization of an ensemble is much better than that of a single classiﬁer [33], which has strong theoretical support due to the following reasons. First, in case where the training data does not provide adequate information for selecting a single optimal learner, combining classiﬁers in the ensemble may be a better choice. Second, the search method of best hypothesis in the source domain of a single classiﬁer may be sub-optimal. An ensemble may compensate for such sub-optimal search process by building multiple classiﬁers. Third, searching true target function in the hypothesis space may not result in single optimal function, ensembles provide more acceptable approximations. In the EEG-based BCI systems, ensemble learning methods have been evaluated to improve the classiﬁcation performance (e.g. bagging, boosting, and random subspace [34]). Impressively, a dynamically weighted ensemble classiﬁcation (DWEC) method has been proposed to handle the issue of non-stationarity adaptation [27]. The DWEC method partitions the EEG data using clustering analysis and subsequently train multiple classiﬁers using the partitioned datasets. The ﬁnal decision of the ensemble is then obtained by appropriately weighting the classiﬁcation decisions of the individual classiﬁers. In a recent study, the ensemble of common spatial pattern patches has shown a potential for improving online MI related BCI system performance[35].

The above-mentioned methods were all based on the passive scheme to NSL for EEG signals. Moreover, both single classiﬁer and classiﬁer ensemble based approaches were developed using the passive mechanism to improve the MI detection performance. However, in passive scheme based ensemble learning, devising the right number of required classiﬁers to achieve an optimal performance and reducing the computational cost for adding a classiﬁer in the ensemble during the evaluation phase are still major open challenges. Our previous study [28, 13] demonstrated that the active scheme based learning BCI system has the potential of improving its performance. We have shown that a single active inductive classiﬁer in single-trial EEG classiﬁcation outperformed the existing passive scheme, although the developed system was only applicable for the rehabilitative BCI systems.

- 2.3. Ensemble Learning Methods in BCI Systems

This study compare the proposed method with ﬁve state-of-the-art ensemble learning methods, namely Bagging, AdaBoost, TotalBoost, RUSboost, and Random Subspace. These ensemble learning methods are brieﬂy described thereafter.

- 2.3.1. Bagging Bagging is an ensemble machine learning meta-algorithm that involves the process of

Bootstrap Aggregation [36]. This algorithm is a special case of the model averaging technique wherein each of the sampled datasets is used to create a diﬀerent model in the ensemble and the output generated from each model is then combined by averaging (in the case of regression) or voting (in the case of classiﬁcation) to create a single output. Nevertheless, bagging has the disadvantage of being ineﬀective in dealing with unstable nonlinear models (i.e. when a small change in the training set can cause a signiﬁcant change in the model). Ensemble classiﬁcation with Bagging algorithm has been applied to a P300-based BCI, and demonstrated some improvement in performance of the ensemble classiﬁer with overlapped partitioning that requires less training data than with naive partitioning [37].

- 2.3.2. AdaBoost Boosting is a widely used approach to ensemble learning. It aims to create an accurate

predictive model by combining various moderately weak classiﬁers. In the family of boosting methods, a powerful ensemble algorithm is Adaptive Boosting (i.e. AdaBoost) [38]. It explicitly alters the distribution of training data and feeds to each classiﬁer independently. Initially, the weights for the training samples are uniformly distributed across the training dataset. However, during the boosting procedure, the weights corresponding to the contributions of each classiﬁer are updated in relation to the performance of each individual classiﬁer on the partitioned training dataset. Recently, the boosting method has been employed for enhancement of MI related classiﬁcation of EEG in a BCI system [39]. It used a two-stage procedure: (i) training of weak classiﬁers using a deep belief network (DBN) and (ii) utilizing AdaBoost algorithm for combining several trained classiﬁers to form one powerful classiﬁer. During the process of constructing DBN structure, many RBMs (Restrict Boltzmann Machine) are combined to create the ensemble. It can be less prone to the over-ﬁtting that most learning algorithms suﬀer from [40]. An improvement of 4% in classiﬁcation accuracy was achieved for certain cases by using the DBN based AdaBoost method. Nevertheless, AdaBoost has several shortcomings, such as its sensitivity to noisy data and outliers.

- 2.3.3. TotalBoost TotalBoost generates ensemble with innumerable learners having weighting factor that

are orders of magnitude smaller than those of other learners [41]. It manages the members of the ensemble by removing the least important member and then reshuﬄe the ensemble reordering from largest to smallest. In particular, the number of learners is self-adjusted.

- 2.3.4. RUSBoost RUSBoost is a boosting algorithm based on the AdaBoost.M2 algorithm [42]. This

method combines random under-sampling (RUS) and boosting for improving classiﬁcation performance. It is one of the most popular and eﬀective techniques for learning nonstationary data. Recently, its application to automatic sleep staging from EEG signals using wavelet transform and spectral features has been proposed wherein the RUSBoost method

has outperformed bagging and other boosting methods [43]. However, bagging and boosting methods both have the disadvantage of being sensitive to noisy data and non-stationary environments.

- 2.3.5. Random Subspace Method The Random Subspace Method (RSM) is an ensemble machine learning technique that

involves the modiﬁcation of training data in the feature space [44, 40]. RSM is beneﬁcial for data with many redundant features wherein better classiﬁers can be obtained in random subspaces than in the original feature space. Recently, RSM method has been used in real-time epileptic seizure detection from EEG signals [44], where the feature space has been divided into random subspaces and the results of diﬀerent classiﬁers are combined by majority voting to ﬁnd the ﬁnal output. However, RSM has a drawback as the features selection does not guarantee that the selected features have the necessary discriminant information. In this way, poor classiﬁers are obtained that may deteriorate the performance of ensemble learning.

The above-mentioned ensemble methods for the EEG classiﬁcation somehow manage non-stationarity in EEG signals, but they are suitable only for passive scheme based settings wherein the ensemble has to be updated continuously over time.

### 3. The Proposed Methodology

- 3.1. Problem Formulation

Given a set of training samples XTrain = xtraini ,yitrain , where i ∈ 1...n is the number of training samples, xtraini ∈ RD (D denotes the input dimensionality) is a set of training input features drawn from a probability distribution with density Ptrain(x), and yitrain ∈

C1,C2 is a set of training labels, where yi = C1, if xi belongs to class ω1, and yi = C2, if xi belongs to class ω2. We assumed that the input training data distribution remains stationary during the training phase. In addition to the labeled training samples, let’s

assume unlabeled test input observations XTest = xtesti , where i ∈ 1...m is the number of testing observations, xtesti ∈ RD is a set of test input features, drawn independently from a probability distribution with density Ptest(x). Note that we consider the CS presence in the data and thus, the input distributions may be diﬀerent during the training and testing phases (i.e. Ptrain(x) = Ptest(x)).

- 3.2. Covariate Shift Estimation

The CS estimation (CSE) is an unsupervised method for identifying non-stationary changes in the unlabeled testing data (XTest) during the evaluation phase [13]. The pseudo code is presented in Algorithm 1. The parameters for the CSE are predetermined during the training phase. The CSE algorithm works in two stages. The ﬁrst stage is a retrospective stage wherein an (EWMA) model is used for the identiﬁcation of the non-stationarity changes in the streaming data. The EWMA is a type of inﬁnite impulse response ﬁlter that applies weighting factors which decrease exponentially. The weight of each older observation decreases exponentially, however, never reaching zero values. The weighting factor is one

of the strengths of the EWMA model. The EWMA control chart overtakes other control charts because it pools together the present and the past data in such a way that even small shifts in the time-series can be identiﬁed more easily and quickly. Furthermore, the incoming observations are continuously examined to provide 1-step-ahead predictions and consequently, 1-step-ahead prediction errors are generated. Next, if the estimated error fell outside the control limits (L), the point is assessed to be a CS point. The EWMA model presented in Eq. (1), is used to provide a 1-step-ahead prediction for each input feature vector of the EEG signals.

z(i) = λx(i) + (1 − λ)z(i−1) (1)

where λ is a smoothing constant to be selected based on minimizing 1-step-aheadprediction error on the training dataset (XTrain). The selection of the value of λ is a key issue in the CSE procedure. Speciﬁcally for the auto-correlated time series data, it was suggested to select a value of λ that minimized the sum of the squares of the 1-step ahead prediction (1-SAP) errors [45]. However, we incorporated data-driven approach and thus, the optimum value of λ was obtained by testing diﬀerent values of λ in the range of [01] with a step of 0.01 on the training dataset. The second stage was a validation stage wherein the CS warning issued at ﬁrst stage was further validated. A multivariate two-sample Hotelling’s T-Square statistical hypothesis test was used to compare two distinct samples of equal number of observations generated before at the CS warning time point. If the test rejected the null hypothesis, the existence of CS was conﬁrmed via this stage, otherwise, it was considered as a false alarm [16].

- 3.3. CSE-based unsupervised adaptive ensemble learning (CSE-UAEL)

The CSE-UAEL algorithm combined the aforementioned CSE procedure and an unsupervised adaptation method using a combination of transductive-inductive approach. The pseudo code of CSE-UAEL is described in the Algorithm 2. The core idea of the proposed algorithm is to adapt to the non-stationary changes by using both the information from the training dataset and the new knowledge obtained in unsupervised mode from the testing phase.

The transductive method is used to add new knowledge in the existing training dataset (XTrain) during the testing phase, wherein a probabilistic weighted K nearest neighbour (PWKNN) method (i.e. instance based learning) [46] is implemented and the ensemble of inductive classiﬁers (E) is used for predicting the BCI outputs. Each time a CS is identiﬁed using the CSE procedure (Algorithm 2, step 8), a new classiﬁer is added to the ensemble based on the updated training dataset (Algorithm 2, step 22). The training dataset is updated at step 20 (Algorithm 2) without considering the actual labels of the testing data and to adapt to the evolution of CS over time in the feature set of the testing phase. The output from the PWKNN method (i.e. CR at step 13) is used to determine whether a trial and its corresponding estimated label can be added to the training dataset and subsequently, the learning model is updated. If the CR is greater than the previously estimated threshold Γ (cf. 4.3) then only the features of the current trial and estimated label are added to the

#### Algorithm 1 Covariate Shift Estimation (CSE) [13]

Input : XTrain, XTest Output : p − value

##### Set the following parameters on training dataset:

- 1: Set the following parameters on training dataset :- z0: arithmetic mean of training input,

λ: smoothing constant , σerr2

0

: standard deviation of the 1-step-ahead-predicted error using unlabeled training data, and PW: transformation matrix from principal component analysis (PCA). For more details (see [13]) Start testing phase:

- 2: for i = 1 to m in XTest do
- 3: x(i)=PW × x(i) # Get the 1st component
- 4: z(i) = λ.x(i) + (1 − λ).z(i−1) # Compute the z-statistics
- 5: err(i) = x(i) + z(i−1) # Compute 1-SAP error
- 6: σerr2

(i)

= ϑ.err(i) + (1 − ϑ). σerr2

(i−1)

# Compute smoothed variance

- 7: UCL(i) = z(i−1) + L. σerr2

(i−1)

- 8: LCL(i) = z(i−1) − L. σerr2

(i−1)

- 9: if LCL(i) ≤ x(i) ≤ UCL(i) then
- 10: no shift
- 11: else
- 12: Issue CS warning and go to stage-II (i.e. CSV)
- 13: Stage-II: execute Hotelling T-squared test on the current feature vector and average feature vector of XTrain to get p-value
- 14: end if
- 15: end for
- 16: return p-value

### Algorithm 2 CSE-UAEL

Input : XTrain = xtraini ,yitrain , where i ∈ 1...n

: XTest = xtesti where i ∈ 1...m

Output : Y Test and MeanSquareError TRAINING:

- 1: E ← ∅
- 2: f1 ← Train(XTrain)
- 3: E ← E ∪ f1 TEST:
- 4: Start evaluation using testing dataset XTest
- 5: Set i,k = 1, where k is the cardinality of ensemble E
- 6: yˆik = E(xi)
- 7: for i = 2 to m do
- 8: if (CSE(XiTest)< 0.05) # See Algorithm 1 then
- 9: k = k + 1
- 10: XNew ← ∅
- 11: XTemp = xtestv v=1:i
- 12: for j = 1 to i do
- 13: [CR] ← PWKNN(XjTemp, XTrain, K, κ) # See Algorithm 3
- 14: if (CR > Γ) then
- 15: Add XjTemp and Predicted label to XNew
- 16: else
- 17: Reject trial XjTemp
- 18: end if
- 19: end for
- 20: XTrain = (XTrain ∪ XNew)
- 21: fk ← Train(XTrain)
- 22: E ← E ∪ fk
- 23: end if
- 24: yˆik = E(xi)
- 25: yˆitest = endk=1 yˆik
- 26: end for
- 27: return Y Test

### Algorithm 3 PWKNN

Input : xp,XTrain,K,κ Output : CR

- 1: Select K-nearest neighbour from XTrain into Xq = xz,yz , where z ∈ 1...K
- 2: CRω(1) :: P(ω(1)|xp) =

K j=1 κ(xp,xj)∗(yj==ω(1))

K

j=1 κ(i) # κ was a function, see Eq. 6.

- 3: CRω(2) :: P(ω(2)|xp) = 1 − CRω(2)
- 4: return CR = max(CRω(1), CRω(2))

XNew at step 15 and the end of the for loop the new classiﬁer is trained on the updated XTrain (step 21). This procedure is repeated at each identiﬁed CS point and trials are added to the initial training dataset along with addition of a new and updated classiﬁer to the current ensemble at step 22. Transductive learning via PWKNN combines induction and deduction in a single step and is related to the ﬁeld of semi-supervised learning (SSL), which used both labeled and unlabeled data during learning process [47, 48]. Thus, by eliminating the need to construct a global model, transductive method oﬀerd viable solution to achieve a higher accuracy. However, in order to make use of unlabeled data, it is necessary to assume some structure to its underlying distribution. Additionally, it is essential that the SSL approach must satisfy at least one of the following assumptions such as smoothness, cluster, or manifold assumption [49]. The proposed algorithm makes use of the smoothness assumption (i.e. the points which are close to each other are more likely to share the same label) to implement the PWKNN algorithm. The pseudo code of the PWKNN algorithm is given in Algorithm 3.

Probabilistic Weighted K Nearest Neighbor. A K-nearest-neighbors (KNN) (i.e. a transductive learning method) based non-parametric method is used to assess current test observations. The KNN algorithm belonged to a family of instance-based learning methods. In this case, a small sphere centered at the point x is used, where the data density P(x) should be estimated. The radius of the sphere is allowed to grow until it contained K data points and the estimate of the density is given by:

K N · V

(2)

P(x) =

where the value of V is set to equal to the volume of the sphere, and N is the total number of data points. The parameter K governed the degree of smoothing. The technique of KNN density estimation can be extended to the classiﬁcation task in which the KNN density estimation is obtained for each class and the Bayes’ theorem is used to perform a classiﬁcation task. Now, assuming that a dataset comprised of N ω

#### points in the class ωi within the set of classes ω, where i ∈ {1,2}, so that N = i N ω

i

#### . To classify a new point x, a sphere centered on x containing precisely K points is used irrespective of their classes. Now suppose this sphere has the volume V and contains Kω

i

from class ωi. Then, an estimate of the density associated with each class or likelihood can be obtained by:

i

Kω

i

P(x|ωi) =

(3)

· V

#### N ω

i

Similarly, the unconditional density is given by P(x) = K/(N · V ), whereas the class prior probability is given by:

N ω

i

(4)

P(ωi) =

N

Now, using the Bayes’ theorem, we can obtain the posterior probability of the class membership by using following equation:

P(x|ωi)P(ωi) P(x)

P(ωi|x) =

Kω

i

=

K

(5)

To minimize the probability of misclassiﬁcation, one needed to assign the test point x to the class ωi with the largest posterior probability, i.e. corresponding to the largest value of Kω

/K. Thus, to classify a new point, one needed to identify the K-nearest points from the training dataset and then assign the new point to the set having the largest number of representatives. This posterior probability is known as the Bayesian belief or conﬁdence ratio (CR). However, the overall estimate obtained by the KNN method may not be satisfactory, because the resulting density is not a true probability density since its integral over all the samples space diverges [50]. Another drawback is that it considers only the K points to build the density and thus, all neighbors have equal weights. An extension to the above KNN method is to assign a weight to each sample that depends on its distance to x. Thus, a radial basis function (RBF) kernel (κ) can be used to obtain the weights, which assigns higher weights to the nearest points than furthest points (see Eq. 6).

i

(||xp − xq||)2 2σ2

κ(xp,xq) = exp(−

) (6)

where (||xp − xq||)2 is the squared Euclidean distance from the data point xp to the data point xq and σ is a free parameter. For binary detection, the conﬁdence ratio of CRω

of the class ωi, for a data point xp, is deﬁned by:

i

CRω

1

K

κ(xp,xq) · (yq == ω1)

q=1

=

K

κ(xp,xq)

q=1

(7)

#### = 1 − CRω

CRω

(8)

2

1

where 1 ≤ q ≤ k, corresponds to the qth nearest neighbor of xp. The outputs of PWKNN include the overall conﬁdence of the decision given by:

CR = max(CRω

#### ,CRω

) (9) and the output class y is equals to 1 if xp is assigned to ω1 otherwise equals to 0.

1

2

- 3.4. Complexity Analysis The core idea behind the proposed technique is to take advantage of an active scheme

based NSL for initiating unsupervised adaptation by adding new classiﬁers to the ensemble each time a CS is identiﬁed. The choice of the classiﬁer to be used may depend on its complexity. By considering m labeled examples and n examples to test, the PWKNN method requires a linear time (i.e. O(nmD)) to predict the labels during testing phase as it belongs to the family of an instance based learning, whereas in other approaches such

- as LDA, a quadratic time is required to predict the score (i.e. O(mD2)) for training the

|Time<br><br>Sensor<br><br>EEGTestingDataEEGTrainingData<br><br>[Figure 1]<br><br>[Figure 2]<br><br>[Figure 3]<br><br>[Figure 4]<br><br>[Figure 5]<br><br>[Figure 6]<br><br>|FB1: [8-12] Hz|
|---|
|FB2: [10-14] Hz|
|FB2: [12-16] Hz|
| |
|FB2: [26-30] Hz|
<br><br>Bandpass Filtering<br><br>W<br><br>CSP A<br><br>A=W-1<br><br>Spatial Filters<br><br>Spatial Pattern<br><br>Spatial Filtering<br><br>λ L<br><br>Get CSE parameters<br><br>Covariate Shift Estimation (CSE)<br><br>Smoothing<br><br>Constant<br><br>Control Limit<br><br>Multiplier<br><br>CSE p<0.05<br><br>fk(x)<br><br>W<br><br>Unsupervised Adaptation using PWKNN<br><br>f(x)<br><br>Train New Classifier Ensemble<br><br>Yes<br><br>No<br><br>Train Classifier f(x)<br><br>f1(x)<br><br>fk(x)<br><br>Output<br><br>Classification<br><br>Training Phase<br><br>Testing Phase<br><br>|
|---|

EEGTestingDataEEGTrainingData

Sensor

- Figure 2: Block diagram of the signal processing and machine learning pipeline implemented in the study. The system consists of two phases. During the training phase, the features were extracted in the temporal and spatial domains from the raw EEG signals, followed by the estimation of covariate shift parameter (i.e. λ and L, smoothing constant and control limit multiplier, respectively) and a classiﬁer is trained on the labeled examples (i.e. XTrain). In the evaluation phase, a similar signal processing method is applied initially and CSP features were monitored by the CSE and adaptation block. In the CSA block, the CSE

procedure identiﬁes the CSs and initiates adaptation by adding the kth classiﬁer fk to the ensemble E, where k counts the number of identiﬁed CSs during the evaluation phase. Finally, the k classiﬁer outputs from E are combined to predict the class label.

classiﬁer, if (m > D), where D is the dimensionality [51]. For the test, LDA requires a linear time (i.e. O(nD)). Therefore, depending on the number of trials to test after training, PWKNN is less computationally expensive than LDA if n < mD/(m − 1).

### 4. Application to Motor-Imagery related BCI System

- 4.1. MI related EEG Datasets

To assess the performance of the proposed CSE-UAEL algorithm, a series of experimental evaluations are performed on the following publicly available MI related EEG datasets.

- 4.1.1. BCI Competition IV dataset-2A The BCI Competition-IV dataset-2A [52] comprising of EEG signals was acquired from

nine healthy participants , namely [A01−A09]. The data were recorded during two sessions on separate days for each subject using a cue-based paradigm. Each data acquisition session consisted of 6 runs where each run comprised of 48 trials (12 trials for each class). Thus, the complete study involved 576 trials from both sessions of the dataset. The total trial length is 7.5 s with variable inter-trial durations. The data were acquired from 25 channels (22 EEG channels along with three monopolar EOG channels) with a sampling frequency of 250 Hz and bandpass ﬁltered between 0.5 Hz to 100 Hz (notch ﬁlter at 50 Hz). Reference

and ground were placed at the left and right mastoid, respectively. Among the 22 EEG channels, 10 channels, responsible for capturing most of the MI related activations, were selected for this study (i.e. channels: C3, FC3, CP3, C5, C1, C4, FC4, CP4, C2, and C6). The dataset consisted of four diﬀerent MI tasks: left hand (class 1), right hand (class 2), both feet (class 3), and tongue (class 4). Only the classes corresponding to the left hand and right hand were considered in the present study. The MI data from the session-I was used for training phase and the MI data from the session-II was used for evaluation phase.

- 4.1.2. BCI Competition IV dataset-2B BCI competition 2008-Graz dataset 2B [52] comprising of EEG data of nine subjects,

namely [B01−B09] was acquired over three channels (i.e. C3, Cz, and C4) with a sampling frequency of 250 Hz. EEG signals were recorded in monopolar montage with the left mastoid serving as reference and the right mastoid as ground. For each subject, data corresponding to ﬁve sessions was collected, with the trial length of 8 s. The MI data using the 3 channels from session-I, II, and III were used to train the classiﬁers and the data from sessions IV and V were merged and used for evaluation phase.

- 4.2. Signal Processing and Feature Extraction

Fig. 2 depicted the complete signal processing pipeline proposed in this study for CS estimation and adaptation of MI related EEG patterns. The following steps were executed for task detection: raw EEG signal acquisition, signal processing (i.e. temporal ﬁltering), feature extraction (i.e. spatial ﬁltering), estimation of CSs, adaptation of the ensemble, and ﬁnally classiﬁcation.

Temporal Filtering. In the signal processing and feature extraction stage, a set of bandpass ﬁlters was used to decompose the EEG signals into diﬀerent frequency bands (FBs) by employing an 8th order, zero-phase forward and reverse band-pass Butterworth ﬁlter. A combination total of 10 band-pass ﬁlters (i.e. ﬁlter bank) with overlapping bandwidths, including [8 − 12], [10 − 14], [12 − 16], [14 − 18], [16 − 20], [18 − 22], [20 − 24], [22 − 26], [24 − 28], and [26 − 30] Hz was used to process the data.

Spatial Filtering. In MI-related BCI systems, both physical and imaginary movements performed by subjects cause a growth of bounded neural rhythmic activity known as event related synchronization/desynchronization (ERD/ERS). Spatial ﬁltering was performed using CSP algorithm to maximize the divergence of band-pass ﬁltered signals under one class and minimize the divergence for the other class. The CSP algorithm has been widely implemented for estimation of spatial patterns related to ERD/ERS [27]. In summary, the spatially ﬁltered signal Z of a single trial EEG is given as:

Z = WE (10)

where E is an C × T matrix representing the raw EEG of single trial, C is number of EEG channels and T is the number of samples for trial. In eq.( 11), W is a projection matrix,

where rows of W were spatial ﬁlters and columns of W−1 were the common spatial patterns. The spatial ﬁltered signal Z given in the above equations maximizes the diﬀerences in the variance of the two classes of EEG measurements. Next to CSP ﬁltering, the discriminating features were extracted using a moving window of 3 s starting from the cue onsets so as to continue our further analysis on the MI-related features only. However, the variances of only a small number h of the spatial ﬁltered signal were generally used as features for classiﬁcation.The ﬁrst h and last h rows of Z i.e. Zp, p ∈ {1...2h} from the feature vector Xp given as input to the classiﬁer (i.e. extreme left and right components of the CSP ﬁlter). Finally, the obtained features from all FBs were merged to create the set of input features for the classiﬁcation.

Xp = log

var(Zp)

2h

i=1 var(Zp)

(11)

- 4.3. Feature Selection and Parameter Selection The existing training dataset was further partitioned into 70% for training data subsets

and 30% for validation data subsets, where validation samples were used to estimate the parameters of the proposed method. In order to estimate the CSs with the obtained multivariate inputs features, the PCA was used to reduce the dimensionality of the feature set [53]. PCA provided fewer components, containing most of the variability in the data. Next, the CSE method was applied to the PCA output features for identifying CS points at the ﬁrst stage of the CSE procedure. A moving window of 3 s of CSP features after the cue onset in the current trial was extracted to use as a ﬁrst sample and a window of averaged CSP features from training data was used as the second sample in the multivariate two-sample Hotelling’s T-Square statistical hypothesis test. In the CSE-UAEL algorithm, the subject speciﬁc parameters such as K and T were selected on validation dataset using grid search method to maximize the accuracy.

- 4.4. Evaluation of Performance The performances of CSE-UAEL algorithm with both single and ensemble of classi-

ﬁers were evaluated with the passive and active schemes to NSL in unsupervised adaptation scheme. With single classiﬁer and ensemble based methods, both active and passive schemes were employed with the unsupervised adaptation. In the passive scheme, adaptation was performed after every 10 trials, whereas in the active scheme, the adaptation was achieved after each CS conﬁrmation. In both passive and active schemes, unsupervised adaptation was performed using three possible combinations of classiﬁers. First, combination-1 (C-1) used PWKNN method in both stages i.e., for enriching the training dataset and classiﬁcation during testing phase. Second, combination-2 (C-2) used inductive LDA classiﬁer for the BCI output, where the posterior probability of two classes obtained using LDA was used to determine if the trial needed to be added to enrich the training data at each CSs identiﬁcation in active scheme. In C-2, the ensemble of LDA classiﬁers gave the combined decision using weighted majority voting scheme. Finally, combination-3 (C-3) used transductive method, where the CR of two classes against the T, obtained using PWKNN method, was used to

determine if the trial needed to be added to enrich the training dataset and the ensemble of LDA classiﬁers gave the combined decision using weighted majority voting scheme. Thus, C-3 was a combination of transductive-inductive learning. Likewise, ensemble method was implemented for both the passive and active schemes, where the ensemble was updated with a new classiﬁer after every 10 trials (in case of passive scheme) or at the instances of identifying CS (in case of active scheme). The parameter estimation remained same for all the combinations. Moreover, the results obtained by the proposed method for the dataset2A was compared with the state-of-the-art methods for non-stationary adaptation in EEG such as common spatial pattern (CSP) [22], common spatial spectral pattern (CSSP) [54], ﬁlter bank CSP (FBCSP) [55], optimal spatio-spectral ﬁlter network with FBCSP (OSSFNFBCSP) [56], and recurrent quantum neural network (RQNN) [57].

[Figure 7]

- Figure 3: The plot showed the eﬀect of lambda (λ) on the performance of CSE at CSV stage. The average CSs identiﬁed for all the nine subjects were presented for dataset-2A.

Table 1: Results for CSE procedure in dataset-2A AND dataset-2B on BCI-Competition-IV.

CSE for 2A CSE for 2B Subject λ CSW CSV Subject λ CSW CSV

- A01 0.50 12 6 B01 0.28 14 10

- A02 0.55 15 8 B02 0.17 18 13

- A03 0.60 7 6 B03 0.60 19 12

- A04 0.61 10 3 B04 0.20 11 6

- A05 0.72 13 8 B05 0.10 12 8

- A06 0.54 12 6 B06 0.33 22 12

- A07 0.57 11 4 B07 0.30 17 11

- A08 0.50 11 5 B08 0.21 27 14

- A09 0.70 6 4 B09 0.45 18 7

Mean 0.58 10.77 5.55 Mean 0.29 17.55 10.33

The performance analysis was based on classiﬁcation accuracies (in %) for binary classiﬁcation tasks (i.e. Left vs Right Hand MI). Moreover, for the CSE, the number of classiﬁers

added to the ensemble for each subject at stage-I and stage-II has been measured along with the values of λ. A two-sided Wilcoxon signed rank test was used to assess the statistical signiﬁcance of the improvement at a conﬁdence level of 0.05 in all the pairwise comparisons. The system was implemented in MATLAB V8.1 (The Mathworks, Natick, MA) and tested on an Intel Core i7 − 4790 with 16 GB of memory.

### 5. Experimental Results

- 5.1. CSE Evaluation on Datasets-2A and -2B To evaluate the eﬃciency of the CSE procedure, a sequence of exploratory assessments

was conducted on dataset-2A and -2B. Table I provides the estimated values of λ and the corresponding number of CSs identiﬁed for both datasets during stage-I (i.e. CSW) and stage-II (i.e. CSV). The values of λ were obtained by minimizing the sum of squares of 1SAP errors. Moreover, Fig. 3 shows the performance of CSE at diﬀerent values of λ, where the average CSs identiﬁed for all the nine subjects are presented for dataset-2A. The average number of identiﬁed CSs is 5.2, where the average of selected λ values is 0.60. In dataset-2A, the maximum and minimum number of identiﬁed CSs are obtained with subject A02 (i.e. 15), and subject A09 (i.e. 6), respectively. After the validation procedure at stage-II (i.e., CSV stage), the number of CSW for subject A02 decreased from 15 to 8, and for subject A09, the amount was reduced from 6 to 4. On an average 10.77 CSW were received, which were further reduced to an average of 5.55 at the CSV stage. For dataset-2B, with the combined trials from session IV and V for the evaluation phase, the maximum number of CSs were identiﬁed for subject B08 (i.e. 27) and minimum for subject B04 (i.e. 11). After the validation procedure at stage-II, the identiﬁed CSs for subject B08 were decreased from 27 to 14, and for subject B04, from 11 to 6. The average identiﬁed CSs (across all subjects)

- at stage-II for dataset-2A and -2B, have been reduced from 10.77 to 5.55 and 17.55 to 10.33, respectively as compared to stage-I. On an average 17.55 CSW were received, which were further reduced to an average of 10.33 at the CSV stage. It can be seen that the CSV procedure at stage-II assisted to signiﬁcantly reduce the number of false CSs based on the information provided by CSW at the stage-I. In this way, the attempt of initiating adaptation by adding classiﬁers to the ensemble became worthless without implementing stage-II. Nevertheless, for each dataset, the number of CSV at stage-II denoted the number of classiﬁers added to the ensemble from the beginning to the end of the evaluation phase.

- 5.2. Classiﬁcation based Evaluation on Dataset-2A and -2B As mentioned in section 4.B, FBCSP based features were used for various binary classi-

ﬁcations to evaluate the performances of all the competing methods and the proposed combinations. The ﬁrst analysis involved implementation of a single classiﬁer at the evaluation stage. For dataset-2A, the classiﬁcation accuracies (%) for C-1 (i.e. PWKNN-PWKNN), C-2 (i.e. LDA-LDA), and C-3 (i.e. PWKNN-LDA) were presented in Table 2 for both passive and active schemes. Similarly, for the dataset-2B, classiﬁcation accuracies (%) were provided for this analysis in Table 3. In single classiﬁer based method, combination-3 (i.e.

combination of PWKNN-LDA) provided higher average binary classiﬁcation accuracies for both the datasets i.e 2A (cf. Table 2) and 2B (cf. Table 3) and for both passive and active schemes. In contrast, combination-1 (i.e. PWKNN-PWKNN) provided lowest average binary classiﬁcation accuracies in all cases. The results clearly showed better performance of PWKNN-LDA combination for both datasets and schemes.

Furthermore, the second analysis involved the proposed method (i.e. CSE-UAEL) using ensemble of classiﬁers at the evaluation stage. The results were obtained using the CSE-UAEL algorithm in both passive and active schemes against other baseline methods (i.e. Bagging, AdaBoost, TotalBoost, RUSBoost, and RSM) are presented in Table 5 for dataset-2A and Table 6 for dataset-2B.

The average binary classiﬁcation accuracies (i.e. mean ± SD) provided by unsupervised

- adaptation methods for dataset-2A (cf. Table 4) are: Bagging (BAG: 73.46 ± 14.42), AdaBoost (AB:71.53±11.76), TotalBoost (TB:75.15±13.44), RUSBoost (RUSB:75.08±13.67), and RSM (71.68 ± 16.53). For the same dataset, the average binary classiﬁcation accuracies (i.e. mean ± SD) provided by CSE-UAEL in passive scheme are: C-1:52.60 ± 6.86, C-2:79.09 ± 12.83, and C-3:80.86 ± 11.44 and CSE-UAEL in active scheme were : C1:52.31 ± 7.32, C-2:77.78 ± 12.87, and C-3:81.48 ± 11.33. The performances of the C-3 (i.e. LDA + PWKNN ) were better than the existing ensemble methods and other classiﬁer combinations for both passive and active schemes.

The average binary classiﬁcation accuracies (i.e. mean ± SD) provided by unsupervised

- adaptation methods for dataset-2B (cf. Table 5) were: Bagging (BAG: 60.43 ± 8.66), AdaBoost (AB:60.42±8.22), TotalBoost (TB:62.08±10.21), RUSBoost (RUSB:60.75±13.21), and RSM (51.26 ± 1.42). For the same dataset, the average binary classiﬁcation accuracies (i.e. mean ± SD) provided by CSE-UAEL in passive scheme were: C-1:51.78 ± 2.39, C-2:66.22 ± 12.68, and C-3:74.26 ± 13.57 and CSE-UAEL in active scheme were : C1:51.98 ± 2.47, C-2:66.76 ± 12.11, and C-3:74.65 ± 13.36. Similar to dataset-2A, the performances of the C-3 (i.e. LDA + PWKNN ) were better than the existing ensemble methods and other classiﬁer combinations for both passive and active schemes.

Table 6 and 7 presented the p-values obtained from the statistical comparison of the CSE-UAEL in active scheme with other single-classiﬁer and ensemble of classiﬁers based methods for dataset-2A and 2B, respectively. The performance of the proposed method (i.e. CSE-UAEL in C-3) was found signiﬁcantly better than Bagging, AdaBoost, TotalBoost, RUSboost and RSM. The proposed method was also found signiﬁcantly better than single classiﬁer based setting for both passive and active schemes. In dataset-2A, CSEUAEL algorithm in active mode for C-3 was not statistically signiﬁcant against CSE-UAEL algorithm in passive scheme with combination C-2 and C-3. However, the same method on dataset-2B showed signiﬁcantly better result (p<0.05). Such analysis provided strong evidence that both CSE-UAEL algorithm with combination of inductive-transductive classiﬁers (i.e. PWKNN-LDA) performed better than the other passive and active scheme.

- Table 2: Classiﬁcation Accuracy in (%) for dataset-2A in both passive and active schemes. C-1: a combination of PWKNN-PWKNN classiﬁers; C-2: a combination of inductive-inductive classiﬁers (i.e. LDA-LDA); and C-3: a combination of inductive-transductive classiﬁers (i.e. PWKNN-LDA).

Subjects

Single Classiﬁer Passive Scheme Active Scheme C-1 C-2 C-3 C-1 C-2 C-3

- A01 58.33 87.50 90.28 58.33 91.67 88.89

- A02 54.17 58.33 64.58 54.17 63.19 63.89

- A03 54.17 95.83 94.44 54.17 91.67 95.14

- A04 51.39 67.36 69.44 51.39 69.44 69.44

- A05 66.67 69.44 71.53 65.28 70.14 74.31

- A06 47.22 65.28 66.67 49.31 68.06 65.97

- A07 53.47 77.08 72.92 53.47 72.92 72.92

- A08 45.83 86.81 91.67 45.83 91.67 92.36

- A09 43.06 88.89 88.19 41.67 88.89 88.19

Mean 52.70 77.39 78.86 52.62 78.63 79.01 Std 7.10 12.93 12.01 6.86 12.01 12.09

- Table 3: Classiﬁcation Accuracy in (%) for dataset-2B in both passive and active schemes. C-1: a combination of PWKNN-PWKNN classiﬁers; C-2: a combination of inductive-inductive classiﬁers (i.e. LDA-LDA); and C-3: a combination of inductive-transductive classiﬁers (i.e. PWKNN-LDA).

Single Classiﬁer Passive Scheme Active Scheme C-1 C-2 C-3 C-1 C-2 C-3

Subjects

- B01 50.31 70.31 74.06 51.25 66.56 75.63

- B02 51.35 50.31 50.31 52.81 51.15 51.15

- B03 48.13 46.88 51.88 48.13 50.31 51.88

- B04 50.00 90.00 92.50 49.06 89.06 92.50

- B05 54.38 80.31 78.13 55.94 74.38 72.50

- B06 50.63 67.50 78.13 50.94 68.75 78.75

- B07 55.63 68.75 68.13 54.06 70.63 68.75

- B08 53.75 59.69 73.75 53.75 62.50 73.75

- B09 51.88 66.88 71.25 51.88 69.06 71.56

Mean 51.78 66.74 70.90 51.98 66.93 70.72 Std 2.39 13.49 13.15 2.47 11.79 12.84

- Table 4: Classiﬁcation Accuracy in (%) for dataset-2A. C-1: a combination of PWKNN-PWKNN classiﬁers; C-2: a combination of inductive-inductive classiﬁers (i.e. LDA-LDA); and C-3:performance a combination of inductive-transductive classiﬁers (i.e. PWKNN-LDA).

Subjects

Baseline Methods Proposed Methods (CSE-UAEL) Passive Scheme Active Scheme BAG AB TB RUSB RSM C-1 C-2 C-3 C-1 C-2 C-3

- A01 86.81 71.53 81.94 84.72 84.72 58.33 88.89 91.67 58.33 87.50 91.67

- A02 47.92 50.69 50.69 52.08 59.03 54.17 59.03 63.89 54.17 60.42 63.89

- A03 90.97 71.53 90.28 90.28 90.97 54.17 96.53 94.44 54.17 95.83 94.44

- A04 66.67 65.28 68.06 67.36 67.36 51.39 68.06 70.80 51.39 66.67 72.22

- A05 65.97 70.83 70.83 65.97 54.86 65.28 73.61 77.78 65.97 72.22 77.08

- A06 63.89 63.19 63.19 64.58 44.44 49.31 66.67 73.61 45.83 64.58 75.69

- A07 74.31 75.00 74.31 72.92 70.83 53.47 80.56 72.92 53.47 74.31 73.61

- A08 72.92 90.97 88.19 90.28 85.42 45.83 89.58 93.75 45.83 88.89 94.44

- A09 91.67 84.72 88.89 87.50 87.50 41.67 88.89 88.89 41.67 89.58 90.28

Mean 73.46 71.53 75.15 75.08 71.68 52.62 79.09 80.86 52.31 77.78 81.48 Std 14.42 11.76 13.44 13.67 16.53 6.86 12.83 11.44 7.32 12.87 11.33

- Table 5: Classiﬁcation Accuracy in (%) for dataset-2B. C-1: a combination of PWKNN-PWKNN classiﬁers; C-2: a combination of inductive-inductive classiﬁers (i.e. LDA-LDA); and C-3: a combination of inductivetransductive classiﬁers (i.e. PWKNN-LDA).

Subjects

Baseline Methods Proposed Methods (CSE-UAEL) Passive Scheme Active Scheme BAG AB TB RUSB RSM C-1 C-2 C-3 C-1 C-2 C-3

- B01 69.69 67.50 66.25 53.13 51.56 50.31 65.31 77.81 51.25 64.69 78.13

- B02 52.60 52.50 55.00 50.83 49.79 51.35 50.31 54.27 52.81 51.15 54.69

- B03 50.63 50.00 51.56 50.00 50.00 48.13 47.50 52.50 48.13 49.38 53.13

- B04 76.25 74.38 81.56 87.81 52.19 50.00 89.69 94.38 49.06 90.63 94.38

- B05 67.50 68.75 72.81 71.56 53.13 54.38 73.44 85.63 55.94 71.56 85.31

- B06 56.88 56.56 59.69 71.56 51.88 50.63 69.38 80.00 50.94 68.75 80.31

- B07 58.13 54.38 50.00 53.75 50.00 55.63 70.00 71.56 54.06 70.94 72.81

- B08 56.88 58.75 59.06 50.94 53.13 53.75 60.00 77.81 53.75 64.69 78.75

- B09 55.31 60.94 62.81 57.19 49.69 51.88 70.31 74.38 51.88 69.06 74.38

Mean 60.43 60.42 62.08 60.75 51.26 51.78 66.22 74.26 51.98 66.76 74.65 Std 8.66 8.22 10.21 13.21 1.42 2.39 12.68 13.57 2.47 12.11 13.36

- Table 6: Comparison of CSE-UAEL Algorithm using p-values on dataset-2A. The p-value denotes the Wilcoxon signed-rank test:∗p< 0.01, p< 0.05.

Single Classiﬁer Ensemble Passive Active Baseline Methods CSE-UAEL (Passive)

C-3 C-3 BAG AB TB RUSB RSM C1 C2 C3

CSE-UAEL C-1 0.0039∗ 0.0039∗ 0.0156 0.0078∗ 0.0078∗ 0.0156 0.0273 1 0.0039∗ 0.0039∗ (Active) C-2 0.1016 0.1484 0.0781 0.0447 0.0447 0.0469 0.0078∗ 0.0039∗ 0.0781 0.0408

C-3 0.0234 0.0234 0.0195 0.0078∗ 0.0078∗ 0.0039∗ 0.0039∗ 0.0039∗ 0.1562 0.1562

- Table 7: Comparison of CSE-UAEL Algorithm using p-values on dataset-2B. The p-value denotes the Wilcoxon signed-rank test:∗p< 0.01, p< 0.05.

Single Classiﬁer Ensemble Passive Active Baseline Methods CSE-UAEL (Passive)

C-3 C-3 BAG AB TB RUSB RSM C1 C2 C3

CSE-UAEL C-1 0.0078∗ 0.0078∗ 0.0078∗ 0.0078∗ 0.0195 0.1641 0.4961 0.75 0.0195 0.0039∗ (Active) C-2 0.0447 0.0391 0.0742 0.0486 0.1641 0.0781 0.0078∗ 0.0078∗ 0.5234 0.0039∗

C-3 0.0039∗ 0.0039∗ 0.0039∗ 0.0039∗ 0.0078∗ 0.0039∗ 0.0039∗ 0.0039∗ 0.0039∗ 0.0425

Table 8: Classiﬁcation Accuracy in (%) Comparison with the state-of-the-art method in dataset-2A.

CSP [22] CCSP [54] FBCSP [55] OSSFN-FBCSP [56] RQNN [57] CSE-UAEL (Active) (C-3)

73.46 79.78 76.31 76.31 66.59 81.48

Furthermore, the performance of the proposed method was compared with other previously published state-of-the-art-methods for dataset-2A. Table 8 presents the average classiﬁcation accuracies (%) for CSP, CCSP, FBCSP, OSSSFN-FBCSP, RQNN, and CSE-UAEL (in active scheme). Evidently, CSE-UAEL outperformed all these previously proposed methods with the highest average classiﬁcation accuracy of 81.48.

### 6. Discussions

The development of eﬃcient machine learning methods for non-stationarity of streaming data has been considered as a challenging task. To improve the performance of MI-based BCI systems, the majority of the exiting studies have focused on techniques that extract features invariant to changes of the data without the use of time speciﬁc discriminant features. Moreover, the existing non-stationarity based machine learning methods incorporated passive schemes based on the assumption of continuous existence of non-stationarity in the streaming data.

In this study, we have shown how an active scheme based ensemble learning can be employed to address non-stationarities of EEG signals, wherein the data distributions shift between training and evaluation phases. The main idea behind the proposed system was to take advantage of an active scheme based NSL for initiating adaptation by adding new classiﬁers to the ensemble each time a CS was identiﬁed instead of assuming the need to update the system at regular intervals. The CSE based active scheme assists to optimize and add new classiﬁers to the ensemble adaptively based upon the identiﬁed changes in the input data distribution, it does not require a trial-and-error or grid search method to select a suitable number of classiﬁers for obtaining an enhanced classiﬁcation accuracy. More importantly, the unsupervised adaption via transduction (i.e. adaption without knowing the true labels) enables this system applicable to long sessions typically considered in the practical applications of BCIs used for both communication and rehabilitation problems.

Indeed, the transductive learning step during the evaluation phase involved the addition

of the predicted labels to the existing training dataset. This approach ensures a continuous enrichment of the existing training dataset, which can be highly crucial to a learning algorithm suﬀering from a high variance. The issue of a high variance was commonly found in the EEG features of poor BCI users [31, 58]. To manage the high variability issue, adding predicted labels with high conﬁdence may improve the prediction performance as demonstrated in the study.

The proposed algorithm has been extensively compared with diﬀerent passive scheme based ensemble learning methods: Bagging, AdaBoost, TotalBoost, RUSBoost, and RSM. The CSE-UAEL algorithm with transductive method was used to improve classiﬁcation performance against single-classiﬁer based passive and active schemes and ensemble based passive scheme. We have shown that the CSE-UAEL algorithm provided an improvement of approximately 6 − 10% in classiﬁcation accuracies compared to other ensemble based methods for dataset-2A. And the performance improvements were statistically signiﬁcant in 18 out of 20 pair-wise comparisons for the CSE-AUEL algorithm in C-3 setting. It was worth noting that the proposed methodology was not limited to BCI applications as the active scheme based ensemble learning can be applied to a wide range of dynamic learning systems where the input signals evolve over time, for example, neuro-rehabilitation and communication systems. A key challenge remains the deﬁnition of a reliable function that can determine a shift detection, and classiﬁers that can reliably classify the training data.

Although the proposed method outperforms other passive schemes, there are limitations to be considered. First, the CSE procedure has been applied to the combined CSP features of multiple frequency bands, which creates a high dimensional input vector and may aﬀect the robustness of the CSE process. This confounding factor can be handled either by using dimensionality reduction methods or by employing multiple CSE procedures at each frequency feature vector. Second, the performance of the proposed system may be adversely aﬀected if applied to data obtained from a large number of sessions or days of recording. In this case, a recurrent concept handling method could help to dynamically manage the number of classiﬁers, e.g., by replacing the old classiﬁers with the updated classiﬁer in the ensemble.

### 7. Conclusion

A new active scheme based non-stationarity adaptation algorithm has been proposed to eﬀectively account for the covariate shifts inﬂuence in an EEG-based BCI system. A synergistic scheme was deﬁned to integrate the CS estimation procedure and ensemble learning approach with transduction to determine when new classiﬁers should be added to the classiﬁer ensemble. The performance of the proposed algorithm has been extensively evaluated through comparisons with state-of-the-art ensemble learning methods in both passive and active settings. The performance analysis on two BCI competition datasets has shown that the proposed method outperforms other passive methods in addressing non-stationarities of EEG signals.

Acknowledgment

S.M.Z. were supported by The Farr Institute of Health Informatics Research- CIPHER (Centre for Improvement in Population Health through E-records Research) (MR /K006525/1), the National Centre for Population Health and Wellbeing Research (CA02), and Swansea University Medical School. D.R., G.P., and H.C. were supported by the Northern Ireland Functional Brain Mapping Facility project (1303/101154803), funded by InvestNI and the Ulster University.

### Appendix A. Symbols and Notations

###### Table A.9: Symbols and Notations

Symbols and Notations Description

- x Input vector

- y Output label

XTrain Training dataset including input data x and output label y XTest Test dataset including input data x and output label y

XTemp Temporary variable to store data in testing phase n Number of training samples in training data m Number of training samples in testing data D Input dimensionality

Ptrain(x) Probability distribution of input x

Ptrain(y|x) Probability of y given x in training data µ Mu frequency band [8-12] Hz β Beta frequency band [14-30] Hz

C1, C2 Set of labels for Class 1 and Class 2

ω1 and ω2 Class 1 and Class 2 R Real number λ lambda was a smoothing constant in covariate shift estimation z EWMA statistics E Ensemble of classiﬁers f Classiﬁer K K for K nearest neighbour k Counter for the number of classiﬁer in ensemble κ A radial basis function (RBF) kernel p p-value v Number of samples from starting of the testing phase to the current sample Γ Threshold ∪ Union operation

Np Total number of points

- V Volume E EEG signal C Number of channels in EEG dataset T Number of samples per trial in EEG dataset

- W CSP projection matrix Z spatially ﬁltered signal O Big-O notation

### References

- [1] C. Alippi, M. Roveri, Just-in-time adaptive classiﬁerspart i: Detecting nonstationary changes, IEEE Transactions on Neural Networks 19 (7) (2008) 1145–1153.
- [2] G. Ditzler, M. Roveri, C. Alippi, R. Polikar, Learning in nonstationary environments: A survey, IEEE Computational Intelligence Magazine 10 (4) (2015) 12–25.
- [3] C. Alippi, G. Boracchi, M. Roveri, Just-in-time classiﬁers for recurrent concepts, IEEE transactions on neural networks and learning systems 24 (4) (2013) 620–634.
- [4] C. Alippi, M. Roveri, Just-in-time adaptive classiﬁerspart ii: Designing the classiﬁer, IEEE Transactions on Neural Networks 19 (12) (2008) 2053–2064.
- [5] S. J. Pan, Q. Yang, A survey on transfer learning, IEEE Transactions on knowledge and data engineering 22 (10) (2010) 1345–1359.
- [6] M. Sugiyama, M. Krauledat, K.-R. MAˇzller,˜ Covariate shift adaptation by importance weighted cross validation, Journal of Machine Learning Research 8 (2007) 985–1005.
- [7] M. Gong, K. Zhang, T. Liu, D. Tao, C. Glymour, B. Sch¨lkopf, Domain adaptation with conditional transferable components, in: International Conference on Machine Learning, 2016, pp. 2839–2848.
- [8] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, T. M. Vaughan, Brain-computer interfaces for communication and control, Clinical neurophysiology 113 (6) (2002) 767–791.
- [9] S.-M. Zhou, J. Q. Gan, F. Sepulveda, Classifying mental tasks based on features of higher-order statistics from eeg signals in brain-computer interface, Information Sciences 178 (6) (2008) 1629–1640.
- [10] P. Celka, Neuronal coordination in the brain: A signal processing perspective (2005).
- [11] Y. Li, H. Kambara, Y. Koike, M. Sugiyama, Application of covariate shift adaptation techniques in brain-computer interfaces, IEEE Transactions on Biomedical Engineering 57 (6) (2010) 1318–1324.
- [12] M. Arvaneh, C. Guan, K. K. Ang, C. Quek, Optimizing spatial ﬁlters by minimizing within-class dissimilarities in electroencephalogram-based brain-computer interface, IEEE transactions on neural networks and learning systems 24 (4) (2013) 610–619.
- [13] H. Raza, G. Prasad, Y. Li, Ewma model based shift-detection methods for detecting covariate shifts in non-stationary environments, Pattern Recognition 48 (3) (2015) 659–669.
- [14] D. Rathee, H. Cecotti, G. Prasad, Single-trial eﬀective brain connectivity patterns enhance discriminability of mental imagery tasks, Journal of neural engineering 14 (5) (2017) 056005.
- [15] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, K.-R. Muller, Optimizing spatial ﬁlters for robust eeg single-trial analysis, IEEE Signal processing magazine 25 (1) (2008) 41–56.
- [16] H. Raza, H. Cecotti, Y. Li, G. Prasad, Adaptive learning with covariate shift-detection for motor imagery-based brain-computer interface, Soft Computing 20 (8) (2016) 3085–3096.
- [17] A. Chowdhury, H. Raza, Y. K. Meena, A. Dutta, G. Prasad, Online covariate shift detection based adaptive brain-computer interface to trigger hand exoskeleton feedback for neuro-rehabilitation, IEEE Transactions on Cognitive and Developmental Systems.
- [18] H. Raza, G. Prasad, Y. Li, Dataset shift detection in non-stationary environments using ewma charts, in: Systems, Man, and Cybernetics (SMC), 2013 IEEE International Conference on, IEEE, 2013, pp. 3151–3156.
- [19] H. Raza, G. Prasad, Y. Li, Ewma based two-stage dataset shift-detection in non-stationary environments, in: IFIP International Conference on Artiﬁcial Intelligence Applications and Innovations, Springer, 2013, pp. 625–635.
- [20] H. Raza, G. Prasad, Y. Li, Adaptive learning with covariate shift-detection for non-stationary environments, in: Computational Intelligence (UKCI), 2014 14th UK Workshop on, IEEE, 2014, pp. 1–8.
- [21] H. Raza, Adaptive learning for modelling non-stationarity in eeg-based brain-computer interfacing, Ph.D. thesis, Ulster University (2016). URL http://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.695308
- [22] H. Ramoser, J. Muller-Gerking, G. Pfurtscheller, Optimal spatial ﬁltering of single trial eeg during imagined hand movement, IEEE transactions on rehabilitation engineering 8 (4) (2000) 441–446.
- [23] F. Lotte, M. Congedo, A. L´ecuyer, F. Lamarche, B. Arnaldi, A review of classiﬁcation algorithms for eeg-based brain-computer interfaces, Journal of neural engineering 4 (2) (2007) R1.

- [24] P. Shenoy, M. Krauledat, B. Blankertz, R. P. Rao, K.-R. Mu¨ller, Towards adaptive classiﬁcation for bci, Journal of neural engineering 3 (1) (2006) R13.
- [25] C. Vidaurre, A. Schlogl, R. Cabeza, R. Scherer, G. Pfurtscheller, A fully on-line adaptive bci, IEEE Transactions on Biomedical Engineering 53 (6) (2006) 1214–1219.
- [26] A. Satti, C. Guan, D. Coyle, G. Prasad, A covariate shift minimisation method to alleviate nonstationarity eﬀects for an adaptive brain-computer interface, in: Pattern Recognition (ICPR), 2010 20th International Conference on, IEEE, 2010, pp. 105–108.
- [27] S. R. Liyanage, C. Guan, H. Zhang, K. K. Ang, J. Xu, T. H. Lee, Dynamically weighted ensemble classiﬁcation for non-stationary eeg processing, Journal of neural engineering 10 (3) (2013) 036007.
- [28] H. Raza, H. Cecotti, Y. Li, G. Prasad, Learning with covariate shift-detection and adaptation in nonstationary environments: Application to brain-computer interface, in: Neural Networks (IJCNN), 2015 International Joint Conference on, IEEE, 2015, pp. 1–8.
- [29] H.-I. Suk, S.-W. Lee, A novel bayesian framework for discriminative feature extraction in braincomputer interfaces, IEEE Transactions on Pattern Analysis and Machine Intelligence 35 (2) (2013) 286–299.
- [30] D. Rathee, H. Raza, G. Prasad, H. Cecotti, Current source density estimation enhances the performance of motor-imagery-related brain-computer interface, IEEE Transactions on Neural Systems and Rehabilitation Engineering 25 (12) (2017) 2461–2471.
- [31] H. Raza, H. Cecotti, G. Prasad, Optimising frequency band selection with forward-addition and backward-elimination algorithms in eeg-based brain-computer interfaces, in: Neural Networks (IJCNN), 2015 International Joint Conference on, IEEE, 2015, pp. 1–7.
- [32] A. Chowdhury, H. Raza, A. Dutta, G. Prasad, Eeg-emg based hybrid brain computer interface for triggering hand exoskeleton for neuro-rehabilitation, in: Proceedings of the Advances in Robotics, ACM, 2017, p. 45.
- [33] T. G. Dietterich, Ensemble methods in machine learning, in: International workshop on multiple classiﬁer systems, Springer, 2000, pp. 1–15.
- [34] S. Sun, C. Zhang, D. Zhang, An experimental evaluation of ensemble methods for eeg signal classiﬁcation, Pattern Recognition Letters 28 (15) (2007) 2157–2163.
- [35] C. Sannelli, C. Vidaurre, K.-R. Mu¨ller, B. Blankertz, Ensembles of adaptive spatial ﬁlters increase bci performance: an online evaluation, Journal of neural engineering 13 (4) (2016) 046003.
- [36] L. Breiman, Bagging predictors, Machine learning 24 (2) (1996) 123–140.
- [37] A. Onishi, K. Natsume, Overlapped partitioning for ensemble classiﬁers of p300-based brain-computer interfaces, PloS one 9 (4) (2014) e93045.
- [38] Y. Freund, R. E. Schapire, A decision-theoretic generalization of online learning and an application to boosting, Journal of computer and system sciences 55 (1) (1997) 119–139.
- [39] X. An, D. Kuang, X. Guo, Y. Zhao, L. He, A deep learning method for classiﬁcation of eeg data based on motor imagery, in: International Conference on Intelligent Computing, Springer, 2014, pp. 203–210.
- [40] M. Skurichina, R. P. Duin, Bagging, boosting and the random subspace method for linear classiﬁers, Pattern Analysis & Applications 5 (2) (2002) 121–135.
- [41] G. R¨tsch, M. K. Warmuth, K. A. Glocer, Boosting algorithms for maximizing the soft margin, in: Advances in neural information processing systems, 2008, pp. 1585–1592.
- [42] C. Seiﬀert, T. M. Khoshgoftaar, J. Van Hulse, A. N. R. Boost, A hybrid approach to alleviating class imbalance, IEEE Transactions On Systems, Man, And CyberneticsPart A: Systems And Humans 40 (1).
- [43] A. R. Hassan, M. I. H. Bhuiyan, A decision support system for automatic sleep staging from eeg signals using tunable q-factor wavelet transform and spectral features, Journal of neuroscience methods 271

(2016) 107–118.

- [44] M.-P. Hosseini, A. Hajisami, D. Pompili, Real-time epileptic seizure detection from eeg signals via random subspace ensemble learning, in: Autonomic Computing (ICAC), 2016 IEEE International Conference on, IEEE, 2016, pp. 209–218.
- [45] D. C. Montgomery, C. M. Mastrangelo, Some statistical process control methods for autocorrelated data, Journal of Quality Technology 23 (3) (1991) 179–193.

- [46] N. Kasabov, S. Pang, Transductive support vector machines and applications in bioinformatics for promoter recognition, in: Neural networks and signal processing, 2003. proceedings of the 2003 international conference on, Vol. 1, IEEE, 2003, pp. 1–6.
- [47] H. Raza, G. Prasad, Y. Li, H. Cecotti, Toward transductive learning classiﬁers for non-stationary eeg, in: Engineering in Medicine and Biology Society (EMBC), 2014 35th Annual International Conference of the IEEE, 2014, p. 1.
- [48] H. Raza, H. Cecotti, G. Prasad, A combination of transductive and inductive learning for handling non-stationarities in motor imagery classiﬁcation, in: Neural Networks (IJCNN), 2016 International Joint Conference on, IEEE, 2016, pp. 763–770.
- [49] X. Zhu, Semi-supervised learning literature survey.
- [50] M. B. Christopher, Pattern Recognition and Machine Learning., Springer-Verlag New York, 2006.
- [51] D. Cai, X. He, J. Han, Srda: An eﬃcient algorithm for large-scale discriminant analysis, IEEE transactions on knowledge and data engineering 20 (1) (2008) 1–12.
- [52] M. Tangermann, K.-R. M¨uller, A. Aertsen, N. Birbaumer, C. Braun, C. Brunner, R. Leeb, C. Mehring, K. J. Miller, G. Mueller-Putz, et al., Review of the bci competition iv, Frontiers in neuroscience 6

(2012) 55.

- [53] J. Z. Kolter, M. A. Maloof, Dynamic weighted majority: A new ensemble method for tracking concept drift, in: Data Mining, 2003. ICDM 2003. Third IEEE International Conference on, IEEE, 2003, pp. 123–130.
- [54] S. Lemm, B. Blankertz, G. Curio, K.-R. Muller, Spatio-spectral ﬁlters for improving the classiﬁcation of single trial eeg, IEEE transactions on biomedical engineering 52 (9) (2005) 1541–1548.
- [55] K. K. Ang, Z. Y. Chin, H. Zhang, C. Guan, Filter bank common spatial pattern (fbcsp) in braincomputer interface, in: IEEE International Joint Conference on Neural Networks, IEEE, 2008, pp. 2390–2397.
- [56] H. Zhang, Z. Y. Chin, K. K. Ang, C. Guan, C. Wang, Optimum spatio-spectral ﬁltering network for brain-computer interface, IEEE Transactions on Neural Networks 22 (1) (2011) 52–63.
- [57] V. Gandhi, G. Prasad, D. Coyle, L. Behera, T. M. McGinnity, Quantum neural network-based eeg ﬁltering for a brain-computer interface, IEEE transactions on neural networks and learning systems 25 (2) (2014) 278–288.
- [58] D. Gao, R. Zhang, T. Liu, F. Li, T. Ma, X. Lv, P. Li, D. Yao, P. Xu, Enhanced z-lda for small sample size training in brain-computer interface systems, Computational and mathematical methods in medicine 2015.

