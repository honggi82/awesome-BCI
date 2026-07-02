# Two-stage frequency recognition method based on correlated component analysis for SSVEP-based BCI

Yangsong Zhang#, Erwei Yin#, Fali Li, Yu Zhang, Toshihisa Tanaka, Qibin Zhao, Yan Cui, Peng Xu, Dezhong Yao, Daqing Guo*

arXiv:1805.02809v3[q-bio.NC]1Jul2018

Abstract— Canonical correlation analysis (CCA) is a state-ofthe-art method for frequency recognition in steady-state visual evoked potential (SSVEP)-based brain-computer interface (BCI) systems. Various extended methods have been developed, and among such methods, a combination method of CCA and individual-template-based CCA (IT-CCA) has achieved the best performance. However, CCA requires the canonical vectors to be orthogonal, which may not be a reasonable assumption for EEG analysis. In the current study, we propose using the correlated component analysis (CORRCA) rather than CCA to implement frequency recognition. CORRCA can relax the constraint of canonical vectors in CCA, and generate the same projection vector for two multichannel EEG signals. Furthermore, we propose a two-stage method based on the basic CORRCA method (termed TSCORRCA). Evaluated on a benchmark dataset of thirty-ﬁve subjects, the experimental results demonstrate that CORRCA signiﬁcantly outperformed CCA, and TSCORRCA obtained the best performance among the compared methods. This study demonstrates that CORRCA-based methods have great potential for implementing high-performance SSVEP-based BCI systems.

Index Terms— Brain-computer interface, steady-state visual evoked potential, correlated component analysis, canonical cor-

This work was supported in part by the National Natural Science Foundation of China under Grant 81571770, Grant 31771149, Grant 81401484, Grant 61522105, Grant 61527815, Grant 61703407, and Grant 61773129, in part by the Longshan academic talent research supporting program of SWUST under Grant 17LZX692, and in part by JSPS KAKENHI under Grant 17K00326. (Corresponding author: Daqing Guo. # indicates that authors contributed equally to this work.)

Y. Zhang is with the Clinical Hospital of Chengdu Brain Science Institute, MOE Key Lab for Neuroinformation, University of Electronic Science and Technology of China, Chengdu 610054, China, and also with School of Computer Science and Technology, Southwest University of Science and Technology, Mianyang 621010, China. (e-mail: zhangysacademy@gmail.com)

E. Yin is with Unmanned Systems Research Center, National Institute of Defense Technology Innovation, Academy of Military Sciences China, Beijing, 100071 China.

Y. Zhang is with Department of Psychiatry and Behaviour Sciences, Stanford University, CA 94305 USA.

T. Tanaka is with Department of Electronic and Information Engineering, Tokyo University of Agriculture and Technology, Koganei-shi, Tokyo 1848588, Japan, also with Rhythm-Based Brain Information Processing Unit, RIKEN Center for Brain Science (CBS), Saitama 351-0198, Japan and Tensor Learning Unit, RIKEN Center for Advanced Intelligence Project (AIP), Tokyo 103-0027, Japan.

Q. Zhao is with Tensor Learning Unit, RIKEN Center for Advanced Intelligence Project (AIP), Tokyo 103-0027, Japan, and also with School of Automation, Guangdong University of Technology, Guangzhou, Guangdong, 510006, China.

F. Li, Y. Cui, P. Xu, D. Yao and D. Guo are with the Clinical Hospital of Chengdu Brain Science Institute, MOE Key Lab for Neuroinformation, University of Electronic Science and Technology of China, Chengdu 610054, China. (e-mail: xupeng@uestc.edu.cn; dyao@uestc.edu.cn; dqguo@uestc.edu.cn)

relation analysis, electroencephalogram.

I. INTRODUCTION

A brain-computer interface (BCI) could provide an alternative communication pathway between the brain and a device. It can help severely paralyzed people communicate or interact with their environment [1], [2], and it assists healthy people, such as through autonomous driving [3]. When designing a BCI system, noninvasive EEG is the most employed brain imaging technique for extracting brain activity that codes the cognitive states and intentions of the user [4]. The brain control signals include event-related potential (ERP) [5]–[7], sensorimotor rhythm (SMR) [8]–[10], steady-state visual evoked potential (SSVEP) [11]–[13], hybrid BCI [14]–[16], and so forth. SSVEP-based BCI has received increasing interest from researchers because it requires less training of the user and has a relatively high information transfer rate (ITR) [17]–[25].

For SSVEP-based BCIs, developing an effective algorithm to recognize the SSVEP frequency with high accuracy and in a short time window (TW) is of considerable importantance for developing high-performance BCI applications. To date, various approaches have been proposed to recognize the SSVEP frequency. Among such methods, the canonical correlation analysis (CCA)-based recognition method has been widely used to recognize targets due to its efﬁciency reported in the literature [20], [26], [27]. The standard CCA method, introduced by Lin et al., which uses sinusoidal signals as reference signals, was ﬁrst proposed for SSVEP detection without calibration [26]. However, the detection performance can be degraded by the interference from spontaneous EEG activities. Various extended methods have been proposed to incorporate individual EEG calibration data in CCA to improve the detection performance, such as the cluster analysis of CCA coefﬁcient (CACC) [28], a phase-constrained CCA [29], individualtemplate-based CCA (IT-CCA) method [30], a combination method of CCA and IT-CCA [31], L1-regularized multiway CCA (L1-MCCA) [32], the multiset CCA (MsetCCA) method [33], [34], and so forth. A comprehensive comparison among these methods was recently presented by Nakanishi et al., and the results showed that the combination method based on the standard CCA and the IT-CCA achieved the highest performance [31].

CCA is a traditional technique for extracting linear combinations of data with maximal correlation [35], and it requires

the canonical projection vectors (i.e., spatial ﬁlters) to be orthogonal. Unfortunately, this is not a meaningful constraint for EEG analysis. The spatial distributions are not expected to be orthogonal because they are determined by the current source distributions in space and the anatomy of the brain [36]. Moreover, for two multichannel signals, CCA assigns two different projection vectors, thus doubling the number of free parameters and unnecessarily reducing the estimation accuracy. By dropping these constraints, a method named correlated components analysis (CORRCA) could be a promising alternative for designing frequency detection methods. CORRCA is derived from maximizing the Pearson product moment correlation coefﬁcient [37].

In this study, we ﬁrst introduce CORRCA as a standard method to implement frequency recognition, and then we propose a novel two-stage CORRCA method for frequency recognition. To evaluate the performance of the proposed methods, extensive comparisons are implemented among the standard CCA, the combination method of CCA and IT-CCA, standard CORRCA and TCORRCA using a benchmark dataset recorded from thirty-ﬁve healthy subjects. For all methods, the reference signals of each frequency are obtained by averaging the SSVEP data across multiple blocks. The experimental results indicate the promising potential of the proposed methods for accurately recognizing the SSVEP frequency in BCI applications.

The remainder of this paper is organized as follows. Section II presents the methods. Section III describes the experimental study. In Section IV, the experimental results on a benchmark dataset are reported. The discussion and conclusion are provided in the last two sections.

II. METHODS

- A. Standard CCA

CCA is a statistical method for measuring the underlying correlation between two sets of multidimensional variables, and it can ﬁnd the weight vectors to maximize the correlation between the two variables [35]. Given two multidimensional variables X ∈ Rm×k and Y ∈ Rn×k, CCA seeks a pair of weight vectors w ∈ Rm×1 and v ∈ Rn×1 such that the correlation between the resulting linear combinations x = wTX and y = vTY is maximized as:

E xyT E[xxT]E [yyT]

ρ = arg max

[Figure 1]

[Figure 2]

w,v

wTXY Tv √

√

= arg max

[Figure 3]

[Figure 4]

[Figure 5]

wTXXTw

vTY Y Tv

w,v

(1)

Maximizing formula (1) can be achieved by solving a generalized eigenvalue problem. The maximum of ρ with respect to w and v is the maximum canonical correlation.

CCA has been widely used for frequency recognition. In the standard CCA, the reference signals, i.e., Yi ∈ R2Nh×N (i = 1,2,...,Nf), are artiﬁcially created with the sine-cosine reference signals as follows [26]:



Yi =

 

sin(2πfit) cos(2πfit) ...

sin(2πNhfit) cos(2πNhfit)



1 Fs

,

, t =

[Figure 6]

 

2 Fs

N Fs

,...,

[Figure 7]

[Figure 8]

(2)

where Nh denotes the number of harmonics, Fs is the sampling rate, and N denotes the number of time samples.

With CCA, the maximum correlation coefﬁcient ρi can be computed between a test sample X¯ ∈ RC×N and each Yi, i = 1,2,...,Nf, respectively. C denotes the number of signal channels, and Nf is the number of stimulus frequencies. Then, the frequency f of the test sample was the frequency of the reference signals with the maximum correlation, as shown in formula (3):

ftest = max

ρf, f = f1,f2,...,fN

f

f

(3)

B. The combination method of CCA and IT-CCA

In the IT-CCA method, the reference signals are individual templates obtained by averaging across multiple EEG trials from each subject [30]. By replacing the artiﬁcial reference signals with the individual templates, the CCA process in this method is the same as standard CCA. The combination method of CCA and IT-CCA is an extended CCA-based method that combines the standard CCA and the IT-CCA approaches [19], [31]. This method achieved the highest performance among the extended CCA methods. In this method, the feature of each frequency was not the maximum of ρ in formula (1) but rather the correlation coefﬁcient between the linear combination of a test sample X¯ ∈ RC×N and an individual template Zi ∈ RC×N (i = 1,2,...,Nf) using CCA-based spatial ﬁlters. Speciﬁcally, the following three weight vectors were used as spatial ﬁlters: (i) WX¯(XZ¯ i) between the test sample X¯ and the individual template Zi, (ii) WX¯(XY¯ i) between the test sample X¯ and sine-cosine reference signal Yi, and (iii) WX¯(ZiYi) between the individual template Zi and sinecosine reference signal Yi. For the i-th template signal, a correlation vector ri was deﬁned as follows [19]:



ri =

 



=

 



- ri(1)
- ri(2)
- ri(3)
- ri(4)
- ri(5)

 

ρ(X¯TWX¯(XY¯ i),Y TWy(XY¯ i)) ρ(X¯TWX¯(XZ¯ i),ZiTWX¯(XZ¯ i)) ρ(X¯TWX¯(XY¯ i),ZiTWX¯(XY¯ i)) ρ(X¯TWX¯ (ZiYi),ZiTWX¯(ZiYi)) ρ(ZiTWX¯(XZ¯ i),ZiTWZ

(XZ¯ i))

i



 

(4)

where ρ(·,·) indicates the computation of the correlation between two signals. The number of harmonics was set to ﬁve to include the fundamental and harmonic components of SSVEPs. The ﬁve correlation values described in formula

(4) were combined as the feature for target identiﬁcation as follows:

5

sign(ri(k)) · (ri(k))2 (5)

ρi =

k=1

where sign(·) was used to retain discriminative information from negative correlation coefﬁcients. The target frequency of the test sample X¯ was then recognized by formula (3).

C. Standard CORRCA

CORRCA is a technique that can produce the same weight vectors for two sets of multidimensional variables such that the linear components of two data are maximally correlated [36]. Its theoretical basis is to maximize the Pearson product moment correlation coefﬁcient, and the weight vectors can be obtained by solving a generalized eigenvalue problem. CORRCA has been used to investigate cross-subject synchrony of neural processing [38] and intersubject correlation in the evoked encephalographic responses [39], [40].

Given two multidimensional variables X1 ∈ RC×N and X2 ∈ RC×N, where C is the number of channels (i.e., electrodes) and N is the number of time samples, CORRCA seeks to ﬁnd a weight vector w ∈ RC×1 such that the resulting linear combinations x = wTX1 and y = wTX2 exhibit the maximum correlation.

xTy x y

ρˆ = argmax

[Figure 9]

w

wTR12w wTR11w wTR22w

= argmax

[Figure 10]

[Figure 11]

[Figure 12]

w

(6)

where ρˆ denotes the correlation coefﬁcient. The sample covariance matrices are denoted as Rij = N1 XiXjT, where i,j = 1,2. Differentiating formula (6) with respect to w and setting to zero and assuming that wTR11w = wTR22w leads to the following eigenvalue equation [36]:

[Figure 13]

(R12 + R21)w = λ(R11 + R22)w (7)

The maximum of ρˆ corresponds to the principal eigenvector of (R11 +R22)−1(R12 +R21) that maximizes the correlation coefﬁcient between x and y. Moreover, the second strongest correlation is obtained by projecting the data matrices onto the eigenvector corresponding to the second strongest eigenvalue and so on.

In this study, we propose a frequency recognition method based on CORRCA. To recognize the frequency of the SSVEPs with CORRCA, we can calculate the correlation coefﬁcient ρˆi between a test sample X¯ ∈ RC×N and an individual template Zi ∈ RC×N at each stimulus frequency, i = 1,2,...,Nf. The frequency (f) of the reference signal with the maximum correlation coefﬁcient was selected as that of the test sample.

ftest = max

ρˆf, f = f1,f2,...,fN

f

f

(8)

D. Two-stage CORRCA

Previous studies demonstrated that the spatial ﬁlters of different stimulus frequencies are similar to each other, and conﬁrmed that integrating all the spatial ﬁlters could further improve the algorithm performance [25], [41]. Inspired by these studies, we propose a two-stage CORRCA method for frequency recognition based on standard CORRCA, which could utilize the spatial ﬁlters of all stimulus frequencies to yield more discriminative feature. In the ﬁrst stage, we calculate the reference signals of each frequency by averaging the corresponding SSVEP data across multiple blocks with the individual training dataset and learn spatial ﬁlters for each frequency with the standard CORRCA. In the second stage, for each frequency, we ﬁrst calculate the correlation coefﬁcients between a test sample and reference signals, and then we use all the spatial ﬁlters obtained in the ﬁrst stage to calculate the correlation coefﬁcients between a test sample and reference signals using the formula of the standard CORRCA. Then, all the correlation values are combined as the feature for target identiﬁcation. The details of the computation are provided below.

t,i represent Nt EEG trials of size C × N at the i-th stimulus frequency. Here, Nt is the number of trials. Let Ii = {Ii1,Ii2} = {(1,2),(1,3),...,(N − 1,N)} denote the set of all P = N × (N − 1)/2 possible combinations of trial pairs at the i-th frequency, i = 1,2,...,Nf. Then, we can deﬁne two trial-aggregated data matrices as:

Assume that X1,i,X2,i,... and XN

- X¯1,i = [XI

11,i XI

21,i ... XI

P1,i] . (9)

- X¯2,i = [XI

22,i ... XI

P2,i] . (10)

12,i XI

In the ﬁrst stage, for the i-th stimulus frequency, we used the standard CORRCA of formula (6) to learn weight vectors wi ∈ RC×1 with X¯1,i and X¯2,i, i = 1,2,...,Nf. In the second stage, with a test sample X¯ ∈ RC×N and an individual template Zi ∈ RC×N (i = 1,2,...,Nf), we ﬁrst calculated the correlation coefﬁcient between X¯ and Zi with formulas (6)-(7), denoted as βi,0. Then, with the weight vectors wk (k = 1,2,...,Nf), we further calculated the correlation coefﬁcients βi,k between X¯ and Zi using the following formulas:

wkTR12wk wkTR11wk wkTR22wk

βi,k =

, k = 1,2,...,Nf (11)

[Figure 14]

[Figure 15]

[Figure 16]

Here, the four sample covariance matrices are calculated as R11 = N1 X¯X¯T, R22 = N1 ZiZiT, R12 = N1 XZ¯ iT, and R21 = N1 ZiX¯T. For the i-th template signal, with Nf weight vectors, we can obtain a correlation vector βi deﬁned as follows:

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]





- βi,0
- βi,1
- βi,2

βi =

(12)

 

 

. βi,N

f

[Figure 21]

Fig. 1. Flowchart of the proposed two-stage CORRCA-based method. For each subject, Nf training data corresponding to all the stimulus frequencies are available, Xi ∈ RNc×Ns×Nt, i = 1, 2, . . . , Nf. In the ﬁrst stage, the spatial ﬁlters for each frequency, i.e., w1, w2, . . . , wNf , are generated with formulas

- (6)-(8), and the reference signals are generated by group averaging across multiple training blocks, Z1, Z2, . . . , ZNf . In the second stage, with a test sample X¯ ∈ RC×N and an individual template Zi ∈ RC×N (i = 1, 2, . . . , Nf), we can ﬁrst calculate the correlation coefﬁcient between Zi and X¯ with formula
- (7), denoted as βi,0. Then, with the weight vector wk, we can further calculate the correlation coefﬁcients βi,k between Zi and X¯ using formula (11). These correlation values are further combined as the feature by formula (??) .

These correlation values described in formula (12) were further combined as the feature by the following formula:

ρ¯i =

Nf

sign(βi,k) · (βi,k)2 (13)

k=0

where sign(·) was used to remain discriminative information from negative correlation coefﬁcients as that in formula (5) . Then, the frequency f of the test sample X¯ was that of the template signals with the maximum correlation:

ftest = max

ρ¯f, f = f1,f2,...,fN

(14) The diagram of the proposed method is shown in Fig. 1.

f

f

- E. The trial of ﬁlter bank technology

Filter bank technology has been widely adopted in algorithm development for recent BCI systems [42]. This technology could enhance the performance of original algorithms, such

- as the common spatial pattern (CSP) algorithm [43], [44], and CCA [42], [45]. Therefore, we further investigate the results when a ﬁlter bank is added in the proposed methods, i.e., CORRCA and TSCORRCA. Here, ﬁve ﬁlter banks were used, and the lower and upper cut-off frequencies of the i-th (i = 1,··· ,5) subband were set to i×8 Hz and 90 Hz, respectively. The zero-phase Chebyshev Type I inﬁnite impulse response (IIR) was used to extract each subband signal. The procedure for combining features in all subbands was similar to that in reference [41].

- F. The exploration on cross-subject classiﬁcation

Exploiting the inter-subject information can reduce the training time [46]. We evaluate the performance of standard

CORRCA when the reference signals were transfered from the other existing subjects. We used the leave-one-out strategy to compute the reference signals for each subject. Concretely, for each subject, the data from the other thirty-four subjects in the benchmark dataset are used for reference signal computation, i.e., by group averaging. Here, standard CCA was used for comparison.

III. EXPERIMENTAL STUDY A. EEG recordings

The data used in the current study were from an existing database, which was provided in the reference [47]. For the data collection, thirty-ﬁve healthy subjects (seventeen females, mean age 22 years) participated in an ofﬂine 40-target BCI speller experiment. The speller contains 40 stimuli coded at different frequencies (8-15.8 Hz with an interval of 0.2 Hz). For each subject, the experiment included six blocks. Each block contained 40 trials corresponding to all 40 stimuli indicated in a random order. Each trial lasted a total of 6 s, which consisted of 0.5 s for the visual cue and 0.5 s for stimulus offset before the next trial began. In each block, the subjects were asked to avoid eye blinks during the stimulation period. To avoid visual fatigue, there was a rest for several minutes between two consecutive blocks.

EEG data were recorded with a Synamps2 system (Neuroscan, Inc.) at a sampling rate of 1000 Hz with a 0.15 Hz to 200 Hz bandpass ﬁlter and a notch ﬁlter at 50 Hz. All data were recorded from sixty-four channels that were placed on the standard positions according to the international 1020 system. The ground electrode (GND) was placed midway between Fz and FPz. The reference electrode was located on the vertex (Cz). Electrode impedances were maintained below 10 kΩ. Event triggers were generated by the computer to the

ampliﬁer and were recorded on an event channel synchronized to the EEG data. The continuous EEG data were segmented into 6 s epochs (0.5 s prestimulus, 5.5 s poststimulus onset). The epochs were subsequently downsampled to 250 Hz. More detailed information for this dataset can be found in reference [47].

- B. Performance evaluation

In the current study, an extensive comparison was performed among the standard CCA method, the combination method of CCA and IT-CCA (named CCAICT), and the proposed standard CORRCA and two-stage CORRCA methods (named TSCORRCA). A leave-one-out cross validation was employed to evaluate the classiﬁcation accuracy of the four methods. Speciﬁcally, the EEG samples from ﬁve blocks were used for the training set, and the samples from the single left-out block were used for the testing set. The procedure was repeated six times such that each run was used as the testing set once.

For the CCA method, the recognition accuracy is directly evaluated by six runs of validation since no training process is required.

In this study, we also evaluated the feature values for each method using the r-square value, which was deﬁned as the proportion of the variance of the signal feature that is accounted for by the user’s intent [48]. In the current study, the r-square value was calculated with the feature values of the target stimulus and the maximal feature values of the nontarget stimuli [31].

IV. RESULTS

Previous studies have indicated that the selection of the number of harmonics (Nh) plays an important role in the CCA method. Fig. 2 shows the classiﬁcation accuracy of CCAICT

- at different Nh values in the reference signals in formula

(4) with a data length of 0.8 s. Overall, the classiﬁcation accuracy increased as the number of harmonics increased. One-way repeated-measures analysis of variance (ANOVA) showed that there were signiﬁcant differences between different numbers of harmonics. Pairwise comparisons revealed signiﬁcant differences between Nh = 1 and all the other Nh values. For a fair and convincing comparison, in the following computation, the number of harmonics was set to ﬁve as that in the reference [19], which includes the fundamental and harmonic components of SSVEPs.

Fig. 3 shows the average accuracies and simulated ITRs across all subjects with different TWs. The standard CORRCA outperforms the standard CCA method, and TSCORRCA yields the best performance compared with all other methods. One-way repeated-measures ANOVA showed that there were signiﬁcant differences in the classiﬁcation accuracy between these methods at all TWs and signiﬁcant differences in the simulated ITRs. The statistical analysis results are summarized in Table I. Furthermore, for the accuracy and ITR, post hoc paired t-tests showed that there were signiﬁcant differences between all pairs of the four methods at each TW (p < 0.001).

To further evaluate the performance among the four methods, we investigated the effects of different numbers of

90

80

70

Accuracy(%)

60

50

40

30

20

10

1 2 3 4 5 6 Numbers of harmonics

Fig. 2. Average classiﬁcation accuracy for the CCAICT method with different numbers of harmonics. Here, TW is 0.8 s.

channels and training blocks on the classiﬁcation accuracy. Fig. 4(a) shows the classiﬁcation accuracy for each method with different numbers of channels at a 0.8 s TW. For all methods, the classiﬁcation accuracy tended to increase with increasing number of channels. One-way repeated-measures ANOVA showed signiﬁcant differences between different numbers of channels for all methods (CCA: F(6,204)=5.08, p < 0.001; CORRCA: F(6,204)=8.46, p < 0.001; CCAICT: F(6,204) = 8.86, p < 0.001; and TSCORRCA: F(6,204) = 12.61, p < 0.001). As shown in Fig. 4(b), TSCORRCA achieved the best performance, and CORRCA outperformed CCA at all numbers of channels. One-way repeated-measures ANOVA showed signiﬁcant differences between the four methods at each condition (C = 3: F(3,102) = 5.38, p = 0.002; C = 4: F(3,102) = 9.41, p < 0.001; C = 5: F(3,102) = 9.93, p < 0.001; C = 6: F(3,102) = 11.72, p < 0.001; C = 7: F(3,102) = 12.65, p < 0.001; C = 8: F(3,102) = 15.09, p < 0.001; and C = 9: F(3,102) = 16.30, p < 0.001).

Fig. 5(a) shows the classiﬁcation accuracy for each method with different numbers of training blocks at a 0.8 s TW. Overall, the classiﬁcation accuracy increased with increasing number of training blocks. However, one-way repeatedmeasures ANOVA showed that there were no signiﬁcant differences between the numbers of training blocks for CCA (F(3,102) = 1.65, p = 0.18) and CCAICT (F(3,102) = 1.98, p = 0.12), but there were signiﬁcant differences for CORRCA (F(3,102) = 3.05, p = 0.03) and TSCORRCA (F(3,102) = 3.25, p = 0.02). Furthermore, as shown in Fig. 5(b), TSCORRCA has the best performance among the methods, and the standard CORRCA outperformed the standard CCA at all numbers of training blocks. One-way repeated-measures ANOVA showed signiﬁcant differences between the four methods at each condition (Nt=2: F(3,102) = 12.92, p < 0.001; Nt=3: F(3,102) = 14.75, p < 0.001; Nt=4: F(3,102) = 15.20, p < 0.001; and Nt=5: F(3,102) = 16.30, p < 0.001).

In Fig. 6, we present the recognition accuracy averaged on all subjects at each of the forty stimulus frequencies for the four methods at a 1 s TW. CORRCA achieves better

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| |CCA<br><br>CORRCA<br><br>| | | |
|CCAICT<br><br>TSCORRCA| | | | |

210

95

200

85

180

160

75

140

ITR(bits/min)

Accuracy(%)

65

120

55

100

45

80

35

60

CCA

25

40

CORRCA

CCAICT

15

20

TSCORRCA

5

0

0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1

Time window (s) (b)

Time window (s) (a)

- Fig. 3. Average results across subjects of the four methods using different time windows. (a) Average classiﬁcation accuracy and (b) simulated ITRs. Error bars indicate standard errors.

TABLE I STATISTICAL ANALYSIS OF THE CLASSIFICATION ACCURACY DIFFERENCES BETWEEN THESE METHODS AT VARIOUS TIME WINDOWS. r DENOTES CORRELATION COEFFICIENTS, AND p DENOTES THE SIGNIFICANCE LEVEL OF THE CORRELATION COEFFICIENTS.

[Figure 22]

Time windows

[Figure 23]

0.2s 0.3s 0.4s 0.5s 0.6s 0.7s 0.8s 0.9s 1s Accuracy

[Figure 24]

F(3,102) 39.51 30.63 25.44 22.25 20.55 18.22 16.30 13.96 13.40

[Figure 25]

p <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 ITR

[Figure 26]

F(3,102) 31.93 27.03 22.78 20.36 19.10 17.82 16.66 14.62 14.16 p <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001 <0.001

[Figure 27]

[Figure 28]

| |C=3|
|---|---|
| |C=4<br><br>|

CCA CORRCA CCAICT TSCORRCA

Methods (a)

15

25

35

45

55

65

75

85

95

100

Accuracy(%)

- C=5
- C=6
- C=7
- C=8
- C=9

|CCA| | | | | | |
|---|---|---|---|---|---|---|
|CORRCA CCAICT TSCORRCA| | | | | | |
| | | | | | | |

3 4 5 6 7 8 9

Numbers of Channels (b)

15

25

35

45

55

65

75

85

95

100

Accuracy(%)

- Fig. 4. Average accuracy across subjects for each method using different numbers of channels. Error bars indicate standard errors. Here, TW is 0.8 s.

100

100

CCA

| |Nt=2<br>Nt=3<br>| | | |
|---|---|---|---|---|
|Nt=4 N =5<br><br>| |
|---|
| | | | |
|t| | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

CORRCA CCAICT

| |
|---|

90

90

TSCORRCA

| |
|---|

80

80

Accuracy(%)

Accuracy(%)

70

70

60

60

50

50

40

40

30

30

CCA CORRCA CCAICT TSCORRCA

2 3 4 5

Methods (a)

Numbers of blocks (b)

- Fig. 5. Average accuracy across subjects with different numbers of training blocks for each method. Error bars indicate standard errors. Here, TW is 0.8 s.

8 9 10 11 12 13 14 15

Frequency (Hz) (a)

0

50

100

Accuracy(%)

CCA

| |
|---|

CORRCA

8 9 10 11 12 13 14 15

Frequency (Hz) (b)

0

50

100

Accuracy(%)

CCAICT

| |
|---|

TSCORRCA

| |
|---|

- Fig. 6. Accuracy averaged across all subjects at each of the forty stimulus frequencies for the four methods at a 1 s time window.

performance than CCA (Fig. 6(a)), and TSCORRCA achieves overall better performance than CCAICT (Fig. 6(b)). To further explore the efﬁciency, r-square values obtained at 8.2 Hz are shown in Fig. 7. The TW was also set to 0.8 s. One-way repeated-measures ANOVA showed a signiﬁcant difference between these methods (F(3,102) = 3.97, p = 0.01), and post hoc paired t-tests showed that there were signiﬁcant differences between the combination method and the other methods. The results indicate that the proposed methods, i.e., CORRCA and TSCORRCA, can enhance the discriminability compared to CCA and CCAICT and then facilitate target classiﬁcation.

Filter bank technology could enhance the performance of algorithms in BCI systems. Here, we investigated the performance of the CORRCA and TSCORRCA with ﬁlter bank at the various TWs. As we expected, we found that the classiﬁcation accuracies of both methods were improved with

0.6

0.5

0.4

0.3

2r

0.2

0.1

0

CCA CORRCA CCAICT TSCORRCA

Methods

Fig. 7. r-square values for SSVEPs at 8.2 Hz. Error bars in each subﬁgure indicate standard errors. Here, TW is 0.8 s.

## ﬁlter bank as shown in Fig. 8.

100

100

| | | | | | |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
|FBCORRCA<br><br>| | | | | |
|CORRCA| | | | | |

95

95

85

85

75

75

Accuracy(%)

Accuracy(%)

65

65

55

55

45

45

35

35

25

25

FBTSCORRCA

15

15

TSCORRCA

5

5

0.2 0.4 0.6 0.8 1 Time window (s) (a)

0.2 0.4 0.6 0.8 1 Time window (s) (b)

- Fig. 8. The average accuracies across all subjects obtained by the CORRCA and TSCORRCA methods with a ﬁlter bank at various time windows. The error bars indicate standard errors. FBCORRCA and FBTSCORRCA denote the CORRCA and TSCORRCA methods with a ﬁlter bank, respectively.

For the results in Fig. 3, the test data and reference are acquired from the same subject. We further evaluated the performance of standard CORRCA when the reference signals were transfered from the other existing subjects. Fig. 9 illustrates the average accuracies at various TWs using the standard CORRCA and CCA methods. As shown, the CORRCA still yields better performance than CCA, although the results are worse than those when the reference signals were obtained from the same subject. These ﬁndings demonstrate that CORRCA could be a promising method for designing and implementing a high-performance method for SSVEP frequency detection. Developing more efﬁcient methods with CORRCA by exploiting intersubject information is beyond the scope of current paper, but we will work on this topic in future studies.

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|

0.2 0.4 0.6 0.8 1 1.2 1.4 1.6 1.8 2

Time window (s)

0

10

20

30

40

50

60

70

80

90

95

Accuracy(%)

CCA CORRCA

- Fig. 9. The average accuracies across all subjects obtained by the standard CORRCA and CCA methods when the SSVEP reference signals were computed with datasets from other subjects at various time windows. The error bars indicate standard errors. The asterisk indicates the statistically signiﬁcant differences (paired t-test, p < 0.001)

Many algorithms have been proposed for different types of BCI modalities [49]. For the SSVEP-based BCI, CCA is a state-of-the-art frequency recognition method, and it is widely used by the research community. To date, various extended methods have been developed [31], among which a combination method of CCA and IT-CCA achieved the best performance [19]. However, CCA requires the canonical vectors to be orthogonal, which may be not a reasonable assumption for EEG analysis. In fact, the spatial distributions are not expected to be orthogonal because they are determined by the current source distributions in space and the anatomy of the brain [36]. Moreover, the projection vectors for the two multichannel signals obtained by CCA are different. When two signals are generated by the same subjects, it is appropriate that the projection vectors should be the same. For instance, in the current study, the two multichannel signals, i.e., the test sample and the reference signals, were recorded from the same subject. Thus, the projection vectors should be the same. The vectors obtained by CCA were different, which may unnecessarily reduce the classiﬁcation accuracy.

In the current study, we proposed using CORRCA rather than CCA to implement frequency recognition. CORRCA could relax the constraint of canonical vectors in CCA and generate the same projection vector for two multichannel EEG signals. The experimental results show that the standard CORRCA method outperforms the standard CCA method when evaluated on the benchmark dataset and demonstrate the rationality and feasibility of CORRCA for SSVEP frequency recognition. We further extended the standard CORRCA method to a hierarchical method with two-stage operation, and the resulting performance was signiﬁcantly enhanced and better than that of the extended CCA-based method, i.e., IT-CCA. Compared with IT-CCA, the two-stage CORRCA method (TSCORRA) does not require the extra synthetic reference signals and thus does not need to optimize the number of harmonics (Nh). Furthermore, the computational efﬁciency was also compared among the four methods, and the results are shown in Fig. 10. The computational time was evaluated with MATLAB R2014b on a desktop computer with a 3.60 GHz CPU (16 GB RAM) at various TWs. We can ﬁnd that all of the methods can be executed efﬁciently. Additionally, the CORRCA methods can be implemented faster than CCA, and TSCORRCA can be implemented faster than CCAICT.

0.045

| | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
| | | | | | | | | | |

CCA CORRCA CCAICT TSCORRCA

0.04

0.035

Computationaltime(s)

0.03

0.025

0.02

0.015

0.01

0.005

0

0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 Time window (s)

V. DISCUSSION

It is still a challenging issue to design and explore highefﬁciency algorithms to classify EEG signals in BCI systems.

Fig. 10. The average computational complexities of the four methods at various time windows.

CORRCA was ﬁrstly introduced for frequency detection in

our previous study [41]. In that study, we mainly used CORRCA to learn spatial ﬁlters with multiple blocks of individual training data. Then, the spatial ﬁlters were used to remove interference by combining the multichannel EEG signals. The feature extraction procedure needed extra one-dimensional or two-dimensional correlation analysis computation to obtain the features between the test sample and reference signals. Therefore, it was a different method compared to the methods proposed here. Overall, those methods demonstrate the feasibility and efﬁciency of CORRCA for frequency recognition. EEG signals are nonlinear and nonstationary. Thus far, we only considered the linear transformations in all the CORRCAbased methods. We will explore extending the methods to nonlinear versions with kernel methods [50], which may further improve the classiﬁcation performance. In the current study, only the weight vectors corresponding to the maximum correlation coefﬁcients were considered. In the future, we will investigate the performance of the methods with more weight vectors.

In recent years, some elaborately designed methods, such as deep-learning-based methods were developed for frequency detection [51], [52]. In the study [51], the average classiﬁcation rate in the static condition was 99.28% on a 5-class SSVEP dataset. In another study [52], the average accuracy was approximately 80% on a 12-class SSVEP dataset. It seems that the proposed methods may not always exhibit better performance than these methods. However, we can ﬁnd that the number of stimulus frequencies used in the two studies is much smaller than that used in our study. What’s more, our proposed methods have low computational complexity, as shown in Fig. 10, and can easily be implemented. Accordingly, they may be good candidates for the BCI community to use in their BCI applications. It is appropriate and interesting to compare our methods with various deep-learning-based methods. Direct comparison of our method with those methods may be beyond the scope of this paper, we will endeavor on this topic in our future studies.

VI. CONCLUSION

In summary, we proposed novel frequency recognition methods based on the CORRCA method. We conﬁrmed that the standard CORRCA outperformed the standard state-of-theart CCA method for frequency recognition with a large number of stimuli on a benchmark dataset. We further proposed a two-stage CORRCA method, which has the best performance compared to the most efﬁcient method based on CCA. The experimental results suggest that the two-stage CORRCA method is a promising candidate to achieve satisfactory performance for SSVEP frequency recognition in BCI applications.

ACKNOWLEDGMENTS

The authors sincerely thank the reviewers for their insightful comments. The authors also sincerely thank Professor Lucas

- C. Parra and his colleagues generously share the correlated components analysis related codes. The authors acknowledge Dr. Dong Li for valuable comments on an early version of this manuscript.

REFERENCES

- [1] Y. Li, J. Pan, J. Long, T. Yu, F. Wang, Z. Yu, and W. Wu, “Multimodal BCIs: Target detection, multidimensional control, and awareness evaluation in patients with disorder of consciousness,” Proc. IEEE, vol. 104, no. 2, pp. 332–352, 2016.
- [2] U. Chaudhary, N. Birbaumer, and A. Ramos-Murguialday, “Braincomputer interfaces for communication and rehabilitation,” Nature Reviews Neurology, vol. 12, no. 9, pp. 513–525, 2016.
- [3] T. O. Zander, L. M. Andreessen, A. Berg, M. Bleuel, J. Pawlitzki, L. Zawallich, L. R. Krol, and K. Gramann, “Evaluation of a dry EEG system for application of passive brain-computer interfaces in autonomous driving,” Frontiers Hum. Neurosci., vol. 11, p. 78, 2017.
- [4] B. He, B. Baxter, B. Edelman, C. Cline, and W. Ye, “Noninvasive braincomputer interfaces based on sensorimotor rhythms,” Proc. IEEE, vol. 103, no. 6, pp. 907–925, 2015.
- [5] J. Jin, B. Z. Allison, E. W. Sellers, C. Brunner, P. Horki, X. Wang, and C. Neuper, “An adaptive P300-based control system,” J. Neural Eng., vol. 8, no. 3, p. 036006, 2011.
- [6] J. Jin, B. Z. Allison, Y. Zhang, X. Wang, and A. Cichocki, “An ERPbased BCI using an oddball paradigm with different faces and reduced errors in critical functions,” Int. J. Neural Syst., vol. 24, no. 08, p. 1450027, 2014.
- [7] E. Yin, T. Zeyl, R. Saab, D. Hu, Z. Zhou, and T. Chau, “An auditorytactile visual saccade-independent P300 brain-computer interface,” Int. J. Neural Syst., vol. 26, no. 01, p. 1650001, 2016.
- [8] F. Qi, Y. Li, and W. Wu, “RSTFC: A novel algorithm for spatio-temporal ﬁltering and classiﬁcation of single-trial EEG,” IEEE Trans. Neural Netw. Learn. Syst., vol. 26, no. 12, pp. 3070–3082, 2015.
- [9] Y. Zhang, Y. Wang, J. Jin, and X. Wang, “Sparse bayesian learning for obtaining sparsity of eeg frequency bands based feature vectors in motor imagery classiﬁcation,” Int. J. Neural Syst., vol. 27, no. 02, p. 1650032, 2017.
- [10] J. Feng, E. Yin, J. Jin, R. Saab, I. Daly, X. Wang, D. Hu, and A. Cichocki, “Towards correlation-based time window selection method for motor imagery BCIs,” Neural Networks, vol. 102, pp. 87–95, 2018.
- [11] Y. Zhang, P. Xu, T. Liu, J. Hu, R. Zhang, and D. Yao, “Multiple frequencies sequential coding for SSVEP-based brain-computer interface,” PLoS ONE, vol. 7, no. 3, p. e29519, 2012.
- [12] E. Yin, Z. Zhou, J. Jiang, Y. Yu, and D. Hu, “A dynamically optimized SSVEP brain-computer interface (BCI) speller,” IEEE Trans. Biomed. Eng., vol. 62, no. 6, pp. 1447–1456, 2015.
- [13] Y. Jiao, Y. Zhang, Y. Wang, B. Wang, J. Jin, and X. Wang, “A novel multilayer correlation maximization model for improving CCAbased frequency recognition in SSVEP brain-computer interface,” Int. J. Neural Syst., vol. 0, no. 0, p. 1750039, 2017.
- [14] Y. Li, J. Pan, F. Wang, and Z. Yu, “A hybrid BCI system combining P300 and SSVEP and its application to wheelchair control,” IEEE Trans. Biomed. Eng., vol. 60, no. 11, pp. 3156–3166, Nov 2013.
- [15] E. Yin, Z. Zhou, J. Jiang, F. Chen, Y. Liu, and D. Hu, “A speedy hybrid BCI spelling approach combining P300 and SSVEP,” IEEE Trans. Biomed. Eng., vol. 61, no. 2, pp. 473–483, Feb 2014.
- [16] B. J. Edelman, J. Meng, N. Gulachek, C. C. Cline, and B. He, “Exploring cognitive ﬂexibility with a noninvasive BCI using simultaneous steadystate visual evoked potentials and sensorimotor rhythms,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 26, no. 5, pp. 936–947, May 2018.
- [17] H. Bakardjian, T. Tanaka, and A. Cichocki, “Optimization of SSVEP brain responses with application to eight-command brain-computer interface,” Neuroscience Letters, vol. 469, no. 1, pp. 34 – 38, 2010.
- [18] Y. Zhang, P. Xu, K. Cheng, and D. Yao, “Multivariate synchronization index for frequency recognition of SSVEP-based brain-computer interface,” J. Neurosci. Meth., vol. 221, pp. 32–40, 2014.
- [19] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao, “Highspeed spelling with a noninvasive brain-computer interface,” Proc. Natl. Acad. Sci. USA., vol. 112, no. 44, pp. E6058–E6067, 2015.
- [20] X. Chen, Z. Chen, S. Gao, and X. Gao, “A high-ITR SSVEP-based BCI speller,” Brain-Comp.Interfaces, vol. 1, no. 3-4, pp. 181–191, 2014.
- [21] Y. Zhang, D. Guo, P. Xu, Y. Zhang, and D. Yao, “Robust frequency recognition for SSVEP-based BCI with temporally local multivariate synchronization index,” Cognitive Neurodynamics, vol. 10, no. 6, pp. 505–511, 2016.
- [22] H. Wang, Y. Zhang, N. R. Waytowich, D. J. Krusienski, G. Zhou, J. Jin, X. Wang, and A. Cichocki, “Discriminative feature extraction via multivariate linear regression for SSVEP-based BCI,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 24, no. 5, pp. 532–541, 2016.

- [23] N. R. Waytowich, Y. Yamani, and D. J. Krusienski, “Optimization of checkerboard spatial frequencies for steady-state visual evoked potential brain-computer interfaces,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 25, no. 6, pp. 557–565, 2017.
- [24] Y. Zhang, D. Guo, D. Yao, and P. Xu, “The extension of multivariate synchronization index method for SSVEP-based BCI,” Neurocomputing, vol. 269, pp. 226 – 231, 2017.
- [25] M. Nakanishi, Y. Wang, X. Chen, Y. T. Wang, X. Gao, and T. P. Jung, “Enhancing detection of SSVEPs for a high-speed brain speller using task-related component analysis,” IEEE Trans. Biomed. Eng., vol. 65, no. 1, pp. 104–112, Jan 2018.
- [26] Z. Lin, C. Zhang, W. Wu, and X. Gao, “Frequency recognition based on canonical correlation analysis for SSVEP-based BCIs,” IEEE Trans. Biomed. Eng., vol. 54, no. 6, pp. 1172–1176, 2007.
- [27] A. Maye, D. Zhang, and A. K. Engel, “Utilizing retinotopic mapping for a multi-target SSVEP BCI with a single ﬂicker frequency,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 25, no. 7, pp. 1026–1036, 2017.
- [28] P. Poryzala and A. Materka, “Cluster analysis of cca coefﬁcients for robust detection of the asynchronous ssveps in brain–computer interfaces,” Biomed Sig Proc Cont., vol. 10, pp. 201–208, 2014.
- [29] J. Pan, X. Gao, F. Duan, Z. Yan, and S. Gao, “Enhancing the classiﬁcation accuracy of steady-state visual evoked potential-based brain-computer interfaces using phase constrained canonical correlation analysis,” J. Neural Eng., vol. 8, no. 3, p. 036027, 2011.
- [30] G. Bin, X. Gao, Y. Wang, Y. Li, B. Hong, and S. Gao, “A high-speed BCI based on code modulation VEP,” J. Neural Eng., vol. 8, no. 2, p. 025015, 2011.
- [31] M. Nakanishi, Y. Wang, Y.-T. Wang, and T.-P. Jung, “A comparison study of canonical correlation analysis based methods for detecting steady-state visual evoked potentials,” PLoS ONE, vol. 10, no. 10, p. e0140703, 2015.
- [32] Y. Zhang, G. Zhou, J. Jin, M. Wang, X. Wang, and A. Cichocki, “L1regularized multiway canonical correlation analysis for SSVEP-based BCI,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 21, no. 6, pp. 887– 896, 2013.
- [33] Y. Zhang, G. Zhou, J. Jin, X. Wang, and A. Cichocki, “Frequency recognition in SSVEP-based BCI using multiset canonical correlation analysis,” Int. J. Neural Syst., vol. 24, no. 3, p. 1450013, 2014.
- [34] K. Suefusa and T. Tanaka, “Asynchronous brain-computer interfacing based on mixed-coded visual stimuli,” IEEE Trans. Biomed. Eng., in press, 2017.
- [35] H. Hotelling, “Relations between two sets of variates,” Biometrika, vol. 28, no. 3/4, pp. 321–377, 1936.
- [36] J. Dmochowski, P. Sajda, J. Dias, and L. Parra, “Correlated components of ongoing EEG point to emotionally laden attention-a possible marker of engagement,” Frontiers Hum. Neurosci., vol. 6, p. 112, 2012.
- [37] K. Pearson, “Vii. mathematical contributions to the theory of evolution.—iii. regression, heredity, and panmixia,” Philos. Trans. R. Soc. Lond. A, vol. 187, pp. 253–318, 1896.
- [38] S. S. Cohen and L. C. Parra, “Memorable audiovisual narratives synchronize sensory and supramodal neural responses,” eNeuro, vol. 3, no. 6, 2016.
- [39] J. P. Dmochowski, M. A. Bezdek, B. P. Abelson, J. S. Johnson, E. H. Schumacher, and L. C. Parra, “Audience preferences are predicted by temporal reliability of neural processing,” Nature Commun., vol. 5, p. 4567, 2014.
- [40] J. J. Ki, S. P. Kelly, and L. C. Parra, “Attention strongly modulates reliability of neural responses to naturalistic narrative stimuli,” Journal of Neuroscience, vol. 36, no. 10, pp. 3092–3101, 2016.
- [41] Y. Zhang, D. Guo, F. Li, E. Yin, Y. Zhang, P. Li, Q. Zhao, T. Tanaka, D. Yao, and P. Xu, “Correlated component analysis for enhancing the performance of SSVEP-based brain-computer interface,” IEEE Trans. Neural Syst. Rehabil. Eng., vol. 26, no. 5, pp. 948–956, May 2018.
- [42] M. R. Islam, M. K. I. Molla, M. Nakanishi, and T. Tanaka, “Unsupervised frequency-recognition method of SSVEPs using a ﬁlter bank implementation of binary subband CCA,” J. Neural Eng., vol. 14, no. 2, p. 026007, 2017.
- [43] K. K. Ang, Z. Y. Chin, C. Wang, C. Guan, and H. Zhang, “Filter bank common spatial pattern algorithm on BCI competition IV datasets 2a and 2b,” Front. Neurosci., vol. 6, p. 39, 2012.
- [44] Y. Zhang, G. Zhou, J. Jin, X. Wang, and A. Cichocki, “Optimizing spatial patterns with sparse ﬁlter bands for motor-imagery based brain– computer interface,” J. Neurosci. Methods, vol. 255, pp. 85–91, 2015.
- [45] X. Chen, Y. Wang, S. Gao, T.-P. Jung, and X. Gao, “Filter bank canonical correlation analysis for implementing a high-speed SSVEP-based braincomputer interface,” J. Neural Eng., vol. 12, no. 4, p. 046008, 2015.

- [46] P. Yuan, X. Chen, Y. Wang, X. Gao, and S. Gao, “Enhancing performances of SSVEP-based brain-computer interfaces via exploiting intersubject information,” J. Neural Eng., vol. 12, no. 4, p. 046006, 2015.
- [47] Y. Wang, X. Chen, X. Gao, and S. Gao, “A benchmark dataset for SSVEP-based brain-computer interfaces,” IEEE Trans.Neural Syst. Rehabil.Eng., vol. 25, no. 10, pp. 1746–1752, Oct 2017.
- [48] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Brain-computer interfaces for communication and control,” Clinical neurophysiology, vol. 113, no. 6, pp. 767–791, 2002.
- [49] F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotomamonjy, and F. Yger, “A review of classiﬁcation algorithms for EEG-based brain-computer interfaces: A 10-year update,” J. Neural Eng., vol. 15, no. 3, p. 031005, 2018. [Online]. Available: http://stacks.iop.org/1741-2552/15/i=3/a=031005
- [50] L. C. Parra, S. Haufe, and J. P. Dmochowski, “Correlated components analysis-extracting reliable dimensions in multivariate data,” arXiv preprint arXiv:1801.08881, 2018.
- [51] N.-S. Kwak, K.-R. Mller, and S.-W. Lee, “A convolutional neural network for steady state visual evoked potential classiﬁcation under ambulatory environment,” PLOS ONE, vol. 12, no. 2, pp. 1–20, 02 2017.
- [52] N. R. Waytowich, V. Lawhern, J. O. Garcia, J. Cummings, J. Faller, P. Sajda, and J. M. Vettel, “Compact convolutional neural networks for classiﬁcation of asynchronous steady-state visual evoked potentials,” arXiv preprint arXiv:1803.04566, 2018.

