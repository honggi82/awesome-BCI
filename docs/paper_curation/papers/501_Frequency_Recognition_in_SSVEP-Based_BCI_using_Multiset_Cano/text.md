International Journal of Neural Systems, Vol. 0, No. 0 (XX, 2013) 00–00 c World Scientiﬁc Publishing Company

arXiv:1308.5609v2[stat.ML]16Jan2014

# FREQUENCY RECOGNITION IN SSVEP-BASED BCI USING MULTISET CANONICAL CORRELATION ANALYSIS

YU ZHANG Key Laboratory for Advanced Control and Optimization for Chemical Processes East China University of Science and Technology, Shanghai, China E-mail: yuzhang@ecust.edu.cn

GUOXU ZHOU Laboratory for Advanced Brain Signal Processing RIKEN Brain Science Institute, Wako-shi, Japan E-mail: zhouguoxu@brain.riken.jp

JING JIN Key Laboratory for Advanced Control and Optimization for Chemical Processes East China University of Science and Technology, Shanghai, China E-mail: jinjingat@gmail.com

XINGYU WANG Key Laboratory for Advanced Control and Optimization for Chemical Processes East China University of Science and Technology, Shanghai, China E-mail: xywang@ecust.edu.cn

ANDRZEJ CICHOCKI Laboratory for Advanced Brain Signal Processing RIKEN Brain Science Institute, Wako-shi, Japan and Systems Research Institute Polish Academy of Science, Warsaw, Poland E-mail: a.cichocki@riken.jp

Received (to be inserted Revised by Publisher)

Canonical correlation analysis (CCA) has been one of the most popular methods for frequency recognition in steady-state visual evoked potential (SSVEP)-based brain-computer interfaces (BCIs). Despite its eﬃciency, a potential problem is that using pre-constructed sine-cosine waves as the required reference signals in the CCA method often does not result in the optimal recognition accuracy due to their lack of features from the real EEG data. To address this problem, this study proposes a novel method based on multiset canonical correlation analysis (MsetCCA) to optimize the reference signals used in the CCA method for SSVEP frequency recognition. The MsetCCA method learns multiple linear transforms that implement joint spatial ﬁltering to maximize the overall correlation among canonical variates, and hence extracts SSVEP common features from multiple sets of EEG data recorded at the same stimulus frequency. The optimized reference signals are formed by combination of the common features and completely based on training data. Experimental study with EEG data from ten healthy subjects demonstrates that the MsetCCA method improves the recognition accuracy of SSVEP frequency in comparison with the CCA method and other two competing methods (multiway CCA (MwayCCA) and phase constrained CCA (PCCA)), especially for a small number of channels and a short time window length. The superiority indicates that the proposed MsetCCA method is a new promising candidate for frequency recognition in SSVEP-based BCIs.

Keywords: Brain-computer interface (BCI); Electroencephalogram (EEG); Multiset canonical correlation analysis (MsetCCA); Steady-state visual evoked potential (SSVEP).

- 1. Introduction

Brain-computer interfaces (BCIs) are communication systems that translate brain electrical activities typically measured by electroencephalogram (EEG) into computer commands, and hence assist to reconstruct communicative and environmental control abilities for severely disabled people 1−6. Event-related potential (ERP), steadystate visual evoked potential (SSVEP) and eventrelated (de)synchronization (ERD/ERS) are usually adopted for development of BCIs 7−14. In recent years, SSVEP-based BCI has been increasingly studied since it requires less training to the user and provides relatively higher information transfer rate (ITR) 11,15,16.

When subject focuses attention on the repetitive ﬂicker of a visual stimulus, SSVEP is elicited at the same frequency as the ﬂicker frequency and also its harmonics over occipital scalp areas 17,18. Accordingly, SSVEP-based BCI is designed to detect the desired commands through recognizing the SSVEP frequency in EEG. Although original SSVEP responses present relatively stable spectrums over time, they are likely to be contaminated by ongoing EEG activities and other background noises 20,21. Therefore, development of an eﬀective algorithm to recognize the SSVEP frequency with a high accuracy and a short time window length (TW) is consider-

ably important for development of an SSVEP-based BCI with high performance.

So far, various approaches have been proposed to recognize SSVEP frequency for BCI applications 19−23. Among them, a canonical correlation analysis (CCA)-based recognition method 21, ﬁrst introduced by Lin et al., has aroused more interests of researchers. The CCA method implements correlation maximization between the multichannel EEG signals and the pre-constructed reference signals with sinecosine waves at each of the used stimulus frequencies. The stimulus frequency corresponding to the maximal correlation coeﬃcient is then recognized as the SSVEP frequency. The CCA method has shown signiﬁcantly better recognition performance than that of the traditional power spectral density analysis (PSDA) using a single or bipolar channel 21,24. Although the CCA method has been validated by many studies on SSVEP-based BCIs 24,25, a potential problem of this approach is that all parameters for recognition are estimated from test data since the reference signals of sine-cosine waves do not include features from training data. Hence, the CCA method often does not result in the optimal recognition accuracy of SSVEP frequency due to possible overﬁtting, especially using a short TW 26,28. Recently, a multiway extension of CCA (MwayCCA) 26 has been proposed by Zhang et al. to optimize the reference signals used in the CCA method from multiple di-

mensions of EEG tensor data for SSVEP frequency recognition. The MwayCCA method has shown improved recognition performance of SSVEP frequency compared to the CCA method. On the other hand, a phase constrained CCA method (PCCA) 28 has also been proposed for SSVEP frequency recognition. The PCCA method achieved signiﬁcant accuracy improvement in comparison with the CCA method, by embedding the phase information estimated from training data into the reference signals. However, the procedures of reference signal optimization in both the MwayCCA and the PCCA methods are not completely based on training data but still need to resort to the pre-constructed sine-cosine waves.

In the present study, we introduce a multiset canonical correlation analysis (MsetCCA)-based method to reference signal optimization for SSVEP frequency recognition. MsetCCA was developed as an extension of CCA to ﬁnd multiple linear transforms that maximize the overall correlation among canonical variates from multiple sets of random variables 29. Recently, MsetCCA has been successfully applied to the joint blind source separation of multisubject fMRI data 30,31, the functional connectivity analysis of fMRI data 32, and also the fusion of concurrent single trial ERP and fMRI data 33. In this study, the proposed MsetCCA method implements reference signal optimization for SSVEP frequency recognition through extracting SSVEP common features from the joint spatial ﬁltering of multiple sets of EEG data recorded at the same stimulus frequency. Diﬀerent from the MwayCCA and the PCCA methods, the procedure of reference signal optimization in the MsetCCA method is completely based on training data. EEG data recorded from ten healthy subjects are used to validate the MsetCCA method in comparison with the CCA, the MwayCCA and the PCCA methods. Experimental results indicate that the proposed MsetCCA method outperforms the three competing methods for SSVEP recognition, especially for a small number of channels and a short time window length.

- 2. Materials and Methods

2.1. Experiments and EEG recordings The experiments were performed by ten healthy sub-

jects (S1-S10, aged from 21 to 27, all males) who received their remuneration. All of them had normal or corrected to normal vision. In the experiments, the subjects were seated in a comfortable chair 60 cm from a standard 17 inch CRT monitor (85 Hz refresh rate, 1024 × 768 screen resolution) in a shielded room. Four red squares were presented on the screen as stimuli (see Fig. 1 (a)) and ﬂickered at diﬀerent four frequencies 6 Hz, 8 Hz, 9 Hz and 10 Hz, respectively. There were 20 experimental runs completed by each subject. In each run, the subject was asked to focus attention on each of the four stimuli once for 4 s, respectively, preceded by each target cue duration of 2 s. A total of 80 trials (4 trials in each run) were therefore performed by each subject.

EEG signals were recorded by using the Nuamps ampliﬁer (NuAmp, Neuroscan, Inc.) at 250 Hz sampling rate with high-pass and low-pass ﬁlters of 0.1 and 70 Hz from 30 channels arranged according to standard positions of the 10-20 international system (see Fig. 1 (b)). The average of two mastoid electrodes (A1, A2) was used as reference and the electrode on the forehead (GND) as ground. With a sixth-order Butterworth ﬁlter, a band-pass ﬁltering from 4 to 45 Hz was implemented on the recorded EEG signals before further analysis.

2.2. CCA for SSVEP Recognition

As a multivariate statistical method, canonical correlation analysis (CCA) 34 explores the underlying correlation between two sets of data. Given two sets of random variables X ∈ RI

2×J, which are normalized to have zero mean and unit variance, CCA is to seek a pair of linear transforms wx ∈ RI

1×J and Y ∈ RI

and wy ∈ RI

such that the correlation be-

2

1

tween linear combinations ˜x = wxTX and y˜ = wyTY is maximized as

ρ =

max

wx,wy

=

E x˜y˜T E [˜x˜xT]E [˜yy˜T]

[Figure 1]

[Figure 2]

wxTXYTwy wxTXXTwxwyTYYTwy

. (1)

[Figure 3]

[Figure 4]

The maximum of correlation coeﬃcient ρ with respect to wx and wy is the maximum canonical correlation.

A CCA-based frequency recognition method 21 was ﬁrst introduced by Lin et al. to SSVEP-based

(a) (b)

|| |
|---|
<br><br>15cm<br><br>4cm<br><br>11cm<br><br>|
|---|

GND Fp2

Fp1

11cm

F8

F7 FT7

F3 Fz F4

FT8 T8

FC3 FCz FC4

A1

T7 A2

Cz

C3 C4

CP3 CPz CP4

TP7

TP8

P3 Pz P4

P7

P8

O1

O2

Oz

Fig. 1. Experimental layout (a) and channel conﬁguration (b) for EEG recordings.

BCI. The CCA method provided better recognition performance than that of the PSDA since it delivered an optimization for the combination of multiple channels to improve the signal-to-noise ratio (SNR). Assume our aim is to recognize the target frequency (i.e., SSVEP frequency) from M stimulus frequencies in an SSVEP-based BCI. Xˆ ∈ RC×P (C channels × P time points) is a test data set consisted of EEG signals from C channels with P time points in each channel. Ym ∈ R2H×P is a pre-constructed reference signal set at the m-th stimulus frequency fm (m = 1,2,...,M) and is formed by a series of sinecosine waves as





sin(2πfmt) cos(2πfmt)

2 F

P F

1 F

,

,...,

,

Ym =

, t =

. sin(2πHfmt) cos(2πHfmt)

[Figure 5]

[Figure 6]

[Figure 7]

 

 

(2) where H is the number of harmonics and F denotes the sampling rate. Solving the maximal correlation coeﬃcient ρm between Xˆ and Ym (m = 1,2,...,M) by (1), the SSVEP frequency is then recognized by

fˆ= argmax

ρm, m = 1,2,...,M. (3)

fm

- 2.3. MsetCCA for SSVEP Recognition

Good performance of the CCA-based recognition method has been conﬁrmed by many studies on SSVEP-based BCIs 24,25. However, the pre-

constructed reference signals of sine-cosine waves often do not result in the optimal recognition accuracy of SSVEP frequency due to their lack of important information contained in the real EEG data. We consider that some common features should be shared by a set of trials recorded at a certain stimulus frequency on a same subject. Such common features contained in the real EEG data could be more natural reference signals in contrast to sine-cosine waves for SSVEP frequency recognition of a test set. Motivated by this idea, we propose a method based on multiset canonical correlation analysis (MsetCCA) to extract the common features for reference signal optimization as a sophisticated calibration procedure followed by the SSVEP frequency recognition using CCA, and hence to improve the recognition accuracy further. The optimal reference signals are ﬁrst learned by MsetCCA from the joint spatial ﬁltering of multiple sets of EEG training data for each of the stimulus frequencies, and are subsequently used instead of sine-cosine waves in the CCA method for SSVEP frequency recognition.

MsetCCA is a generalization of CCA to more than two sets of data, which maximizes the overall correlation among canonical variates from multiple sets of random variables through optimizing the objective function of correlation matrix of the canonical variates 30,31,33. The ﬁve most discussed objective functions 29,35 for MsetCCA are: (1) SUMCOR, maximize the sum of all entries in the correlation matrix; (2) SSQCOR, maximize the sum of squares

of all entries in the correlation matrix; (3) MAXVAR, maximize the largest eigenvalue of the correlation matrix; (4) MINVAR, minimize the smallest eigenvalue of the correlation matrix; (5) GENVAR, minimize the determinant of the correlation matrix. All of the ﬁve objective functions yield similar results on a group dataset 30. This study adopts the MAXVAR approach to solve MsetCCA, since it provides a natural extension of CCA to multiple sets 32,36.

Assume we have multiple sets of random variables Xi ∈ RI

i×J (i = 1,2,...,N) that are normalized to have zero mean and unit variance. The MAXVAR objective function for maximization of the overall correlation among canonical variates from them is deﬁned as

max

w1,...,wN

ρ =

s.t. N1

[Figure 8]

N

wiTXiXTj wj

i =j

N

wiTXiXTi wi = 1, (4)

i=1

With the method of Lagrange multipliers, the maximization in (4) can be transformed into the following generalized eigenvalue problem

(R − S)w = ρSw, (5) where

- R =

  

X1XT1 ... X1XTN

.

... . XNXT1 ... XNXTN

  ,

- S =

w =

  

  

X1XT1 ... 0

... . 0 ... XNXTN

.

  .

w1 . wN

  ,

Then, linear transforms w1,w2,...,wN resulting in the largest overall canonical correlation among

the multiple canonical variates z˜i = wiTXi (i = 1,2,...,N) are given by eigenvectors corresponding to the largest generalized eigenvalue.

Assume X1,m,X2,m,...,XN,m ∈ RC×P (C channels × P time points) denote EEG data sets recorded from N experimental training trials at the m-th stimulus frequency fm. MsetCCA is implemented to ﬁnd multiple linear transforms (i.e.,

spatial ﬁlters) w1,m,w2,m,...,wN,m that result in the maximization of overall correlation among the canonical variates ˜z1,m,˜z2,m,...,˜zN,m, with the joint spatial ﬁltering ˜zi,m = wi,mT Xi,m (i = 1,2,...,N). These obtained canonical variates represent the common features shared among multiple sets of training data, which are assumed to reﬂect more accurately the real SSVEP characteristics than the artiﬁcial sine-cosine waves do. The optimized reference signal set at stimulus frequency fm is then constructed by the combination of canonical variates as

Ym = ˜zT1,m,˜zT2,m,...,˜zTN,m T . (6) After the aforementioned calibration procedure of reference signals optimization, the maximal correlation coeﬃcient ρm between a new test data set Xˆ ∈ RC×P and each of the optimized reference signal sets Ym ∈ RN×P (m = 1,2,...,M) is computed by CCA in (1). The SSVEP frequency is then recognized according to (3). Fig. 2 illustrates the proposed frequency recognition method based on MsetCCA. Matlab code is available on request.

2.4. MwayCCA for SSVEP Recognition

One method of multiway canonical correlation analysis (MwayCCA) introduced in our previous study 26,27 also considers to improve the recognition accuracy of SSVEP frequency through a calibration procedure of reference signal optimization. Diﬀerent from the MsetCCA method proposed in this study, the MwayCCA method implements reference signal optimization by collaboratively maximizing correlation between the multiple dimensions of EEG tensor data and the pre-constructed sinecosine waves. Consider a three-way tensor Xm = (X)i

1,i2,i3 ∈ RC×P×N (C channels × P time points × N trials) constructed by EEG data from N experimental training trials at the m-th stimulus frequency (m = 1,2,...,M) and an original reference signal set Ym ∈ R2H×P constructed as (2). The MwayCCA method seeks three linear transforms w1,m ∈ RC, w3,m ∈ RN and vm ∈ R2H to maximize the correlation between linear combinations ˜zm = Xm ×1 w1T,m ×3 w3T,m and y˜m = vmT Ym as

E ˜zmy˜mT E [˜zm˜zTm]E [y˜my˜mT ]

. (7)

ρm =

max

[Figure 9]

[Figure 10]

w1,m,w3,m,vm

X ×k wT denotes the k-th way projection of a tensor

Reference Signal Optimization

Optimization for Reference Signals at the m-th Stimulus Frequency fm by MsetCCA

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

MAXVAR at fm

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

MsetCCA MsetCCA MsetCCA

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

CCA CCA CCA

[Figure 37]

[Figure 38]

SSVEP Frequency Recognition

Fig. 2. Illustration of the MsetCCA-based method for SSVEP frequency recognition. X1,m, . . . , XN,m ∈ RC×P denote the EEG training data sets recorded from N experimental trials at the m-th stimulus frequency fm (m = 1, 2, . . . , M). Multiple linear transforms (i.e., spatial ﬁlters) w1,m, . . . , wN,m are found by MsetCCA with the objective function MAXVAR on the training data. Canonical variates are then computed through z˜i,m = wi,mT Xi,m (i = 1, 2, . . . , N) and combined as formula (6) to form the optimized reference signal set Ym ∈ RN×P at fm. Regarding a new test data set Xˆ ∈ RC×P , the maximal correlation coeﬃcient between Xˆ and each of Ym (m = 1, 2, . . . , M) is computed by CCA in formula (1). The SSVEP frequency in Xˆ is then recognized by formula (3).

with a vector and its deﬁnition can be found in literature 26. The optimization problem in (7) can be solved by alternating CCAs 26.

After obtaining the optimal linear transforms, we compute the canonical variate z˜m as the optimized reference signal at stimulus frequency fm. The maximal correlation coeﬃcient ρm between a new test data set Xˆ ∈ RC×P and each of the optimized reference signal ˜zm (m = 1,2,...,M) is computed by CCA in (1). The SSVEP frequency of a test set is then recognized by (3) again.

- 2.5. PCCA for SSVEP Recognition On the other hand, a phase constrained CCA

method (PCCA) 28 has been recently proposed for SSVEP frequency recognition. In the PCCA method, SSVEP response phase that estimated from the apparent latency of training data is adopted as a constraint on the pre-constructed reference signals in the CCA method. The constrained reference signals more eﬀectively captures the phase information of SSVEP frequency, and hence signiﬁcantly improves recognition accuracy of the CCA method.

The SSVEP response phase φr is proportional to the stimulus frequency

φr(fm) = −L · fm · 360◦, (8)

where L denotes the apparent latency that is ﬁxed for all the stimulus frequencies fm (m = 1,2,...,M)

H = 1

100

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

90

80

70

60

50

40

30

1 2 3 4

H = 3

100

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

90

80

70

60

50

40

30

1 2 3 4

H = 2

100

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

90

80

70

60

50

40

30

1 2 3 4

Accuracy(%)

|CCA<br><br>PCCA<br><br>MwayCCA<br><br>MsetCCA|
|---|

TW (s)

Fig. 3. Averaged SSVEP recognition accuracies derived by the CCA, PCCA, MwayCCA and MsetCCA methods, respectively, with the number of harmonics H = 1, 2, 3 and time window lengths (TWs) from 1 s to 4 s. Here eight channels P7, P3, Pz, P4, P8, O1, Oz and O2 were used. The errorbar denotes the standard deviation of accuracy on all the ten subjects. Note that recognition accuracies obtained with H = 1, 2, 3 are exactly the same as each other for the MsetCCA method, since it does not require pre-deﬁned H but automatically estimate the optimal SSVEP features from the training data.

and can be estimated from the EEG training data based on SSVEP phase φs 37. The SSVEP phase φs(fm) at the stimulus frequency fm is computed by discrete Fourier transform of EEG signal from channel Oz at fm. The diﬀerence between φs and φr is a multiple of 360◦ as

φr(fm) = φs(fm) − n(fm) · 360◦, (9)

where n(fm) is an integer depending on the stimulus frequency fm. According to (8) and (9), we obtain n(fm) = L·fm+φs(fm)/360◦. The apparent latency L is then determined through an exhaustive search procedure based on weighting least-squares ﬁt. With the estimated L, the SSVEP response phase φr(fm)

(m = 1,2,...,M) can be derived from (8). The Optimized reference signal set at stimulus frequency fm is obtained by adding φr(fm) as a constraint to the pre-constructed sine-cosine waves. The SSVEP frequency of a test set is then recognized by using (1) and (3) again. More details about the PCCA method can be found in literature 28.

2.6. Experimental Evaluation

In this study, the proposed MsetCCA method is compared with the CCA method 21, the MwayCCA method 26 and the PCCA method 28, to validate its eﬀectiveness for SSVEP frequency recognition.

Table 1. Statistical analysis results of accuracy diﬀerence between the MsetCCA and each of the CCA, PCCA, MwayCCA with diﬀerent numbers of harmonics H at various time window lengths (TWs), respectively.

[Figure 39]

Method Comparison TW 1 s 2 s 3 s 4 s

[Figure 40]

- H = 1 MsetCCA vs. CCA p < 0.001 p < 0.001 p < 0.001 p < 0.001 MsetCCA vs. PCCA p < 0.01 p < 0.05 p < 0.01 p < 0.005 MsetCCA vs. MwayCCA p < 0.05 p < 0.05 p = 0.28 p < 0.05
- H = 2 MsetCCA vs. CCA p < 0.005 p < 0.05 p < 0.05 p < 0.005 MsetCCA vs. PCCA p < 0.05 p < 0.01 p < 0.05 p < 0.005 MsetCCA vs. MwayCCA p = 0.19 p = 0.46 p = 0.21 p = 0.51
- H = 3 MsetCCA vs. CCA p < 0.005 p < 0.005 p < 0.005 p < 0.001 MsetCCA vs. PCCA p < 0.01 p < 0.005 p < 0.05 p < 0.005 MsetCCA vs. MwayCCA p = 0.15 p = 0.61 p = 0.23 p = 0.46

[Figure 41]

Since the occipital and parietal scalp areas have been demonstrated to contribute most to the SSVEP frequency recognition 21,24, only eight channels P7, P3, Pz, P4, P8, O1, Oz and O2 are used for analysis in this study.

For the MsetCCA, the MwayCCA and the PCCA methods, leave-one-run-out cross-validation is implemented to evaluate the average recognition accuracy. More speciﬁcally, the data from 19 runs (4 trials in each run) are used as training data for reference signal optimization while the data from the left-out run for validation. This procedure is repeated for 20 times such that each run serves once for validation. For the CCA method, the average recognition accuracy is evaluated on the direct validation of 20 runs.

- 3. Results

Since the number of harmonics H is required to be pre-deﬁned for the CCA, the PCCA and the MwayCCA methods, we ﬁrst investigate eﬀects of varying H on the frequency recognition accuracy. Fig. 3 shows the averaged SSVEP recognition accuracies obtained by the CCA, the PCCA, the MwayCCA and the MsetCCA methods with H from 1 to 3 at various time window lengths (TWs), respectively. Note that the proposed MsetCCA method did not require the pre-deﬁned H, and hence derived the exactly same accuracy for H = 1,2 and 3. The statisti-

cal analysis results of accuracy diﬀerences evaluated by paired-sample t-test are summarized in Table 1. For H = 1,2 and 3, the MsetCCA method achieved the best frequency recognition accuracy at all the four TWs. The CCA, the PCCA and the MwayCCA methods yielded higher accuracies with H = 2 and 3 in contrast to H = 1 while no big accuracy changing was found for the three methods in increasing H from 2 to 3. Thus, we choose H = 2 for the CCA, the PCCA and the MwayCCA methods in further analysis.

With ﬁxed H = 2, eﬀects of varying the number of channels C on the frequency recognition accuracy are further studied. Fig. 4 shows averaged SSVEP recognition accuracies obtained by the four methods with C = 4,6 and 8 at various time window lengths (TWs), respectively. Table 2 summarizes the statistical analysis results of accuracy diﬀerences evaluated by paired-sample t-test. For C = 4,6 and 8, the MsetCCA method derived better frequency recognition accuracies than the other three methods, especially when using a small number of channels and a short TW. For instance, the MsetCCA method signiﬁcantly outperformed the CCA, the PCCA and the MwayCCA methods with C = 4 at the TW of 1 s (MsetCCA > CCA: p < 0.001, MsetCCA > PCCA: p < 0.005, MsetCCA > MwayCCA: p < 0.05).

Fig. 5 depicts the subject-wise accuracy with the number of channels C = 4. For most subjects, the MsetCCA method yielded higher accuracy than the

C = 4

100

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

90

80

70

60

50

40

30

1 2 3 4

C = 8

100

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

90

80

70

60

50

40

30

1 2 3 4

C = 6

100

| | | | | |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

90

80

70

60

50

40

30

1 2 3 4

Accuracy(%)

|CCA<br><br>PCCA<br><br>MwayCCA<br><br>MsetCCA|
|---|

TW (s)

Fig. 4. Averaged SSVEP recognition accuracies derived by the CCA, PCCA, MwayCCA and MsetCCA methods, respectively, with the number of channels C = 4, 6, 8 and time window lengths (TWs) from 1 s to 4 s. C = 4: P3, P4, O1 and O2; C = 6: P7, P3, P4, P8, O1 and O2; C = 8: P7, P3, Pz, P4, P8, O1, Oz and O2. Here the number of harmonics H = 2. The errorbar denotes the standard deviation of accuracy on all the ten subjects.

other three methods at various TWs. Fig. 6 further shows the SSVEP recognition accuracy averaged on all subjects at each of the four stimulus frequencies for the four methods, respectively. For all of the four stimulus frequencies, the MsetCCA method consistently outperformed the other three competing methods.

In summary, the aforementioned results indicate that the proposed MsetCCA method is promising for the development of SSVEP-based BCIs with high performance.

- 4. Discussion For EEG classiﬁcation or detection, many researches

have conﬁrmed that a sophisticated calibration with appropriate analysis method could signiﬁcantly improve the accuracy 38−57. In this study, instead of directly using pre-constructed sine-cosine waves as reference signals in the CCA method for SSVEP frequency recognition, all the PCCA, the MwayCCA and the MsetCCA methods consider to improve the accuracy through optimizing the reference signals from training data. The optimization procedure of reference signals in the MsetCCA method is completely based on the training data, whereas those in both the PCCA and the MwayCCA methods still need to resort to the pre-constructed sine-cosine waves. The MsetCCA method learns multiple linear transforms through the maximization of overall cor-

Table 2. Statistical analysis results of accuracy diﬀerence between the MsetCCA and each of the CCA, PCCA, MwayCCA with diﬀerent numbers of channels C at various time window lengths (TWs), respectively.

[Figure 42]

Method Comparison TW

1 s 2 s 3 s 4 s C = 4

[Figure 43]

MsetCCA vs. CCA p < 0.001 p < 0.005 p < 0.005 p < 0.005 MsetCCA vs. PCCA p < 0.005 p < 0.005 p < 0.005 p < 0.005 MsetCCA vs. MwayCCA p < 0.05 p = 0.36 p < 0.05 p < 0.05

C = 6 MsetCCA vs. CCA p < 0.001 p < 0.01 p < 0.005 p < 0.01 MsetCCA vs. PCCA p < 0.01 p = 0.086 p < 0.05 p < 0.005 MsetCCA vs. MwayCCA p < 0.05 p = 0.67 p = 0.10 p < 0.05 C = 8

MsetCCA vs. CCA p < 0.001 p < 0.05 p < 0.05 p < 0.005 MsetCCA vs. PCCA p < 0.005 p < 0.01 p < 0.05 p < 0.005 MsetCCA vs. MwayCCA p < 0.05 p = 0.46 p = 0.21 p = 0.51

[Figure 44]

S1

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

80

Accuracy(%)

70

60

50

40

30

20

1 2 3 4

S6

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

80

Accuracy(%)

70

60

50

40

30

20

1 2 3 4

TW (s)

S2

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

80

70

60

50

40

30

20

1 2 3 4

S3

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

80

70

60

50

40

30

20

1 2 3 4

S4

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

80

70

60

50

40

30

20

1 2 3 4

S5

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

80

70

60

50

40

30

20

1 2 3 4

S7

S8

S9

100

100

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

90

90

80

80

80

70

70

70

60

60

60

50

50

50

40

40

40

30

30

30

20

20

20

1 2 3 4

1 2 3 4

1 2 3 4

TW (s)

TW (s)

TW (s)

|CCA PCCA MwayCCA MsetCCA<br><br>|
|---|

S10

100

| | | |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

90

80

70

60

50

40

30

20

1 2 3 4

TW (s)

Fig. 5. SSVEP recognition accuracies derived by the CCA, PCCA, MwayCCA and MsetCCA methods, respectively, for each of the ten subjects. Here the number of harmonics H is 2 for the CCA, the PCCA, the MwayCCA methods, the number of channels C is 4. The averaged accuracies is shown in the subﬁgure with C = 4 of Fig. 4.

relation among canonical variates, which provides a novel approach to extract SSVEP common features from the joint spatial ﬁltering of multiple experimental trials at the same stimulus frequency. Recently, the positive impact of common features on classiﬁcation has been suggested by Zhou et al. 58. In our study, the extracted common features are combined to form the optimized reference signals for robust recognition of SSVEP frequency. As an example, Fig. 7 illustrates superiority of the reference signals

learned from MsetCCA over the sine-cosine waves for SSVEP recognition. The reference signal set constructed by the common features more accurately captured the harmonic feature in test data than the sine-cosine waves did. This characteristic assisted in accurately recognizing the SSVEP frequency.

Another important advantage of the MsetCCA method is that it does not require the pre-deﬁned number of harmonics H. For the CCA, the PCCA and the MwayCCA methods, the pre-deﬁned H

TW = 1 s

100

| | | | | |
|---|---|---|---|---|
| | | | | |
|6|8 Stimulus|9 frequency|1 (Hz)<br><br>|0|

80

Accuracy(%)

60

40

20

TW = 2 s

100

| | | | | |
|---|---|---|---|---|
| | | | | |
|6|8 Stimulus<br><br>|9 frequency|1 (Hz)|0|

80

Accuracy(%)

60

40

20

TW = 3 s

TW = 4 s

100

100

| | | | | |
|---|---|---|---|---|
| | | | | |
|6|8 Stimulus|9 frequency|1 (Hz)|0<br><br>|

| | | | | |
|---|---|---|---|---|
| | | | | |
|6|8 Stimulus|9 frequency|1 (Hz)<br><br>|0|

80

80

Accuracy(%)

Accuracy(%)

60

60

40

40

20

20

|CCA<br><br>| |
|---|
<br><br>PCCA<br><br>| |
|---|
<br><br>MwayCCA<br><br>| |
|---|
<br><br>MsetCCA<br><br>| |
|---|
|
|---|

Fig. 6. SSVEP recognition accuracies obtained by the CCA, PCCA, MwayCCA and MsetCCA methods, respectively, with diﬀerent time window lengths (TWs), for each of the four stimulus frequencies, averaged on all subjects. Here the number of harmonics H is 2 for the CCA, the PCCA, the MwayCCA methods, the number of channels C is 4.

is necessary since their recognition procedures are based on the pre-constructed sine-cosine waves. Bin et al. 24 reported that the second and third harmonics of SSVEP had no signiﬁcant impact on the recognition accuracy, whereas M¨uller-Putz et al. 17 conﬁrmed that the use of higher harmonics as features indeed improved the recognition accuracy. Some existing SSVEP-based BCIs 20,21,25 adopted more than one harmonic (i.e., fundamental frequency) for SSVEP frequency recognition while some others used the fundamental frequency only 11,23,28. It can be seen that decision of the optimal H is still based on experience, which may hardly give the best recognition accuracy for all subjects. In this study, the proposed MsetCCA method provided an eﬀective optimization procedure for automatical estimation of the subject-speciﬁc SSVEP features with accurate harmonics from multi-trial EEG training data.

It is worth noting that reference signal optimization using the MsetCCA method can be eﬃciently implemented without complicated pre-processing. Under the computation environment of Matlab R2011a on a laptop with 1.20 GHz CPU, the com-

putational time of optimization procedure is 0.357 s for the MsetCCA method, 1.475 s for the MwayCCA method and 3.091 s for the PCCA methods method, when using a TW of 4 s on four candidate stimulus frequencies. The computational cost is negligible in contrast to the time cost for training data recording. After optimizing the reference signals, SSVEP frequency recognition based on CCA can be eﬃciently executed in 0.0056 s.

The number of reference signals learned from the proposed MsetCCA method depends on the number of trials used in the training stage. Use of insuﬃcient training trials could hardly learn eﬀective reference signals, whereas use of too many training trials could introduce unavoidable redundancy into reference signals as well as additional memory and computational requirements for SSVEP recognition. To investigate this potential problem, Fig. 8 shows the averaged accuracy and computational time for SSVEP recognition in using CCA with diﬀerent numbers of training trials for reference signal optimization by MsetCCA. The overall trend of accuracy was improved with the increase in the number of training trials. However,

### MsetCCA CCA

Reference signal set learned from MsetCCA Reference signal set constructed by sine-cosine waves

0.3

Averaged Power Spectrum

0.25

PowerSpectrum

0.2

0.15

0.1

0.05

0

0 250 500 750 1000 Time (ms)

0 10 20 30 40

0 250 500 750 1000 Time (ms)

Frequency (Hz)

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

CCA with test data CCA with test data

Canonical variate transformed from test data Canonical variate transformed from test data

10

10

- 0.8

- 1

- 0.8

- 1

PowerSpectrum

PowerSpectrum

Amplitude(V)µ

Amplitude(V)µ

5

5

0.6

0.6

0

0

0.4

0.4

- -10

- -5

- -10

- -5

0.2

0.2

0

0

0 250 500 750 1000

0 250 500 750 1000

0 10 20 30 40

0 10 20 30 40

Time (ms)

Time (ms)

Frequency (Hz)

Frequency (Hz)

Fig. 7. Illustration for superiority of the reference signals learned from MsetCCA over the sine-cosine waves for SSVEP recognition. The reference signals (i.e., common features) extracted by MsetCCA more accurately captured the harmonic feature in test data than the sine-cosine waves did.

the accuracy did not change too much when more than ten training trials were used. This result implies an appropriate selection of the number of reference signals (i.e., the number of training trials) could eﬀectively reduce the requirement for training data without signiﬁcant decrease in recognition accuracy. Hence, how to decide the optimal number of reference signals in the MsetCCA method is worthy of our further study. On the other hand, the computational time was still in several milliseconds due to the high eﬃciency of CCA although it increased with the increase in the number of training trials. Therefore, the computational time of recognition procedure in the MsetCCA method is negligible with an appropriate number of training trials.

nal optimization. However, we strongly prefer the MsetCCA method in development of an improved SSVEP-based BCI with high performance, especially when the recognition accuracy is considered as the primary factor.

95

- 3

- 4

- 5

- 6

- 7

90

Computationaltime(ms)

Accuracy(%)

85

80

In summary, with a sophisticated calibration of reference signals from training data, the proposed MsetCCA method signiﬁcantly improved the recognition accuracy of SSVEP frequency in contrast to the popularly used CCA method. It should be noted that the CCA method is still preferred for development of a zero-training SSVEP-based BCI when training time reduction is considered more important than recognition accuracy improvement, since it does not require training data for reference sig-

Accuracy

Computational time

75

2 4 6 8 10 12 14 16 18

No. training trials

Fig. 8. Averaged accuracy and computational time for SSVEP recognition in using CCA with diﬀerent numbers of reference signals learned from MsetCCA (i.e., by using diﬀerent numbers of training trials). Here, the number of channels C = 4, time window length (TW) is 4 s.

- 5. Conclusions

In this study, we introduced a novel method based on multiset canonical correlation analysis (MsetCCA) to improve the SSVEP frequency recognition for BCI application. The MsetCCA method learned multiple linear transforms through maximizing the overall correlation among canonical variates to extract common features from the joint spatial ﬁltering of multiple sets of EEG data recorded at the same stimulus frequency. Such common features reﬂected more accurately the SSVEP characteristics and were used instead of pre-constructed sine-cosine waves to form the optimized reference signals in the CCA method for SSVEP frequency recognition. Experimental results with EEG data from ten healthy subjects demonstrated that the proposed MsetCCA method outperformed the CCA method at the cost of using training data, and also performed better than the other two competing methods, i.e., MwayCCA and PCCA. Future study will investigate eﬀectiveness of the MsetCCA method on a wide range of stimulus frequencies.

Acknowledgements

The authors sincerely thank the editor and the anonymous reviewers for their insightful comments and suggestions that helped improve the paper. This study was supported in part by the Nation Nature Science Foundation of China under Grant 61305028, Grant 61074113, Grant 61203127, Grant 61103122, Grant 61202155, Fundamental Research Funds for the Central Universities Grant WH1314023, Grant WH1114038, and Shanghai Leading Academic Discipline Project B504.

References

- 1. J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfutscheller and T. M. Vaughan, Brain-computer interfaces for communication and control, Clin. Neurophysiol. 113(6) (2002) 767–791.
- 2. A. Ortiz-Rosario and H. Adeli, Brain-Computer Interface Technologies: From signal to action, Rev. Neurosci. 24(5) (2013) 537–552.
- 3. J. Li, J. Liang, Q. Zhao, J. Li, K. Hong and L. Zhang, Design of assistive wheelchair system directly steered

- by human thoughts, Int. J. Neural Syst. 23(3) (2013) 1350013.
- 4. W. Y. Hsu, Continuous EEG signal analysis for asynchronous BCI application, Int. J. Neural Syst. 21(4)

(2011) 335–350.

- 5. M. A. Lopez-Gordo, F. Pelayo, A. Prieto and E. Fernandez, An Auditory Brain-Computer Interface with Accuracy Prediction, Int. J. Neural Syst. 22(3) (2012) 1250009.
- 6. X. Wang, J. Jin, Y. Zhang, B. Wang, Brain control: Human-computer integration control based on braincomputer interface approach, Acta Autom. Sin. 39(3)

(2013) 208–211.

- 7. Y. Zhang, Q. Zhao, J. Jin, X. Wang and A. Cichocki, A novel BCI based on ERP components sensitive to conﬁgural processing of human faces, J. Neural Eng. 9(2) (2012) 026018.
- 8. Y. Zhang, G. Zhou, Q. Zhao, J. Jin, X. Wang and A. Cichocki, Spatial-temporal discriminant analysis for ERP-based brain-computer interface, IEEE Trans. Neural Syst. Rehabil. Eng. 21(2) (2013) 233–243.
- 9. E. Sellers and E. Donchin, A P300-based braincomputer interface: Initial tests by ALS patients, Clin. Neurophysiol. 117(3) (2006) 538–548.
- 10. Y. Wang, R. Wang, X. Gao, B. Hong and S. Gao, A practical VEPbased brain-computer interface, IEEE Trans. Neural Syst. Rehabil. Eng. 14(2) (2006) 234– 239.
- 11. N. V. Manyakov, N. Chumerin and M. M. V. Hulle, Multichannel decoding for phase-coded SSVEP braincomputer interface, Int. J. Neural Syst. 22(5) (2012) 1250022.
- 12. Y. Li, J. Long, T. Yu, Z. Yu, C. Wang, H. Zhang and C. Guan, An EEG-based BCI system for 2-D cursor control by combining Mu/Beta rhythm and P300 potential, IEEE Trans. Biomed. Eng. 57(10) (2010) 2495–2505.
- 13. G. R. Mu¨ller-Putz, C. Pokorny, D. S. Klobassa and P. Horki, A single-switch BCI based on passive and imagined movements: toward restoring communication in minimally conscious patents, Int. J. Neural Syst. 23(2) (2013) 1250037.
- 14. H. Lee, Y. Kim, A. Cichocki and S. Choi, Nonnegative tensor factorization for continuous EEG classiﬁcation, Int. J. Neural Syst. 17(4) (2007) 305–317.
- 15. B. Z. Allison, D. J. McFarland, G. Schalk, S. Zheng, M. Jackson and J. R. Wolpaw, Towards an independent brain-computer interface using steady state visual evoked potentials, Clin. Neurophysiol. 119(2)

(2008) 399–408.

- 16. J. Pan, Y. Li, R. Zhang, Z. Gu and F. Li, Discrimination between control and idle states in asynchronous SSVEP-based brain switches: a pseudo-key-based approach, IEEE Trans. Neural Syst. Rehabil. Eng. 21(3)

(2013) 435–443.

- 17. G. R. Mu¨ller-Putz, R. Scherer, C. Brauneis and G. Pfurtscheller, Steady-state visual evoked potential

- (SSVEP)-based communication: impact of harmonic frequency components, J. Neural Eng. 2(4) (2005) 123–130.
- 18. M. Cheng, X. Gao, S. Gao and D. Xu, Design and implementation of a brain-computer interface with high transfer rates, IEEE Trans. Biomed. Eng. 49(10)

(2002) 1181–1186.

- 19. X. Gao, D. Xu, M. Cheng and S. Gao, A BCI-based environmental controller for the motion-disabled, IEEE Trans. Neural Syst. Rehabil. Eng. 11(2) (2003) 137–140.
- 20. O. Friman, I. Volosyak and A. Graser, Multiple channel detection of steady-state visual evoked potentials for brain-computer interfaces, IEEE Trans. Biomed. Eng. 54(4) (2007) 742–750.
- 21. Z. Lin, C. Zhang, W. Wu and X. Gao, Frequency recognition based on canonical correlation analysis for SSVEP-based BCIs, IEEE Trans. Biomed. Eng. 53(12) (2006) 2610–2614.
- 22. C. Wu, H. Chang, P. Lee, K. Li, J. Sie, C. Sun, C. Yang, P. Li, H. Deng and K. Shyu, Frequency recognition in an SSVEP-based brain computer interface using empirical mode decomposition and reﬁned generalized zero-crossing, J. Neurosci. Meth. 196(1) (2011) 170–181.
- 23. Z. Wu and D. Yao, Frequency detection with stability coeﬃcient for steady-state visual evoked potential (SSVEP)-based BCIs, J. Neural Eng. 5(1) (2008) 36– 43.
- 24. G. Bin, X. Gao, Z. Yan, B. Hong and S. Gao, An online multi-channel SSVEP-based brain-computer interface using a canonical correlation anaylsis method, J. Neural Eng. 6(4) (2009) 046002.
- 25. Y. Zhang, P. Xu, T. Liu, J. Hu, R. Zhang and D. Yao, Multiple frequencies sequential coding for SSVEP-based brain-computer interface, PLoS One 7(3) (2012) e29519.
- 26. Y. Zhang, G. Zhou, Q. Zhao, A. Onishi, J. Jin, X. Wang and A. Cichocki, Multiway canonical correlation analysis for frequency components recognition in SSVEP-Based BCIs, In: 18th Intl Conf. on Neural Information Processing (ICONIP 2011) (Shanghai, China, 2011), pp. 287–295.
- 27. Y. Zhang, G. Zhou, J. Jin, M. Wang, X. Wang, A. Cichocki, L1-regularized multiway canonical correlation analysis for SSVEP-based BCI, IEEE Trans. Neural Syst. Rehabil. Eng. 21(6) (2013) 887–896.
- 28. J. Pan, X. Gao, F. Duan, Z. Yan and S. Gao, Enhancing the classiﬁcation accuracy of steady-state visual evoked potential-based brain-computer interfaces using phase constrained canonical correlation analysis, J. Neural Eng. 8(3) (2011) 036027.
- 29. J. Kettenring, Canonical analysis of several sets of variables, Biometrika 53(3) (1971) 433–451.
- 30. Y.-O. Li, T. Adali, W. Wang and V. Calhoun, Joint blind source separation by multiset canonical correlation analysis, IEEE Trans. Signal Process. 57(10)

- (2009) 3918–3929.
- 31. Y.-O. Li, T. Eichele, V. Calhoun and T. Adali, Group study of stimulated driving fMRI data by multiset canonical correlation analysis, J. Sign. Process. Syst. 68(1) (2012) 31–48.
- 32. F. Deleus and M. Van Hulle, Functional connectivity analysis of fMRI data based on regularized multiset canonical correlation analysis, J. Neurosci. Meth. 197(1) (2011) 143–157.
- 33. N. Correa, T. Eichele, T. Adali, Y.-O. Li and V. Calhoun, Multi-set canonical correlation analysis for the fusion of concurrent single trial ERP and functional MRI, NeuroImage 50(4) (2010) 1438–1445.
- 34. H. Hotelling, Relations between two sets of variates, Biometrika 28(3/4) (1936) 321–377.
- 35. A. Nielsen, Multiset canonical correlations analysis and multispectral, truly multitemporal remote sensing data, IEEE Trans. Image Process. 11(3) (2002) 293–305.
- 36. J. Via, I. Santamaria and J. Perez, A learning algorithm for adaptive canonical correlation analysis of several data sets, Neural Netw. 20(1) (2007) 139–152.
- 37. M. S. John and T. W. Picton, Human auditory steady-state responses to amplitude-modulated tones: phase and latency measurements, Hear. Res. 141(1)

(2000) 57–59.

- 38. M. Cabrerizo, M. Ayala, M. Goryawala, P. Jayakar and M. Adjouadi, A new parametric feature descriptor for the classiﬁcation of epileptic and control EEG records in pediatric population, Int. J. Neural Syst. 22(2) (2012) 1250001.
- 39. H. Adeli, S. Ghosh-Dastidar, N. Dadmehr, A spatiotemporal wavelet-chaos methodology for EEG-based diagnosis of Alzheimers disease, Neurosci. Lett. 444(2) (2008) 190–194.
- 40. S. Ghosh-Dastidar and H. Adeli, A new supervised learning algorithm for multiple spiking neural networks with application in epilepsy and seizure detection, Neural Netw. 22(10) (2009) 1419–1431.
- 41. M. Ahmadlou and H. Adeli, Wavelet-synchronization methodology: a new approach for EEG-based diagnosis of ADHD, Clin. EEG Neurosci. 41(1) (2010) 1–10.
- 42. M. Ahmadlou, H. Adeli and A. Adeli, New diagnostic EEG markers of the Alzheimer’s disease using visibility graph, J. Neural Transm. 117(9) (2010) 1099– 1109.
- 43. M. Ahmadlou and H. Adeli, Fuzzy synchronization likelihood with application to attentiondeﬁcit/hyperactivity disorder, Clin. EEG Neurosci. 42(1) (2011) 6–13.
- 44. M. Ahmadlou, H. Adeli and A. Adeli, Fractality and a wavelet-chaos-neural network methodology for EEGbased diagnosis of autistic spectrum disorder, J. Clin. Neurophysiol. 27(5) (2010) 328–333.
- 45. Z. Sankari and H. Adeli, Probabilistic neural networks for diagnosis of Alzheimer’s disease using conventional and wavelet coherence, J. Neurosci. Meth.

- 197(1) (2011) 165–170.
- 46. Z. Sankari, H. Adeli and A. Adeli, Intrahemispheric, interhemispheric, and distal EEG coherence in Alzheimer’s disease, Clin. Neurophysiol. 122(5)

(2011) 897–906.

- 47. M. Ahmadlou and H. Adeli, Functional community analysis of brain: a new approach for EEG-based investigation of the brain pathology, NeuroImage 58(2)

(2011) 401–408.

- 48. M. Ahmadlou, H. Adeli and A. Adeli, Graph theoretical analysis of organization of functional brain networks in ADHD, Clin. EEG Neurosci. 43(1) (2012) 5–13.
- 49. M. Ahmadlou, H. Adeli and A. Adeli, Spatiotemporal analysis of relative convergence of EEGs reveals differences between brain dynamics of depressive women and men, Clin. EEG Neurosci. 44 (2013) 175–181.
- 50. R. J. Martis, U. R. Acharya, J. H. Tan, A. Petznick, R. Yanti, C.K. Chua, E. Y. K. Ng and L. Tong, Application of empirical mode decomposition (EMD) for automated detection of epilepsy using EEG signals, Int. J. Neural Syst. 22(6) (2012) 1250027.
- 51. Y. Zhang, G. Zhou, J. Jin, Q. Zhao, X. Wang and A. Cichocki, Aggregation of sparse linear discriminant analysis for event-related potential classiﬁcation in brain-computer interface, Int. J. Neural Syst. 24(1)

(2014) 1450003.

- 52. Y. Li and C. Guan, An extended EM algorithm for joint feature extraction and classiﬁcation in braincomputer interfaces, Neural Comput. 18(11) (2006)

- 2730–2761.
- 53. Y. Li and C. Guan, Joint feature re-extraction and classiﬁcation using an iterative semi-supervised support vector machine algorithm, Mach. Learn. 71(1)

(2008) 33–53.

- 54. Y. Li, C. Guan, H. Li and Z. Chin, A self-training semi-supervised SVM algorithm and its application in an EEG-based brain computer interface speller system, Pattern Recognit. Lett. 29(9) (2008) 1285–1294.
- 55. F. Cong, A.-H. Phan, P. Astikainen, Q. Zhao, Q. Wu, J. Hietanen, T. Ristaniemi and A. Cichocki, Multidomain feature extraction for small event-related ptentials through nonnegative multi-way array decomposition from low dense array EEG, Int. J. Neural Syst. 23(2) (2013) 1350006.
- 56. F. Cong, A.-H. Phan, Q. Zhao, T. Huttunen-Scott, J. Kaartinen, T. Ristaniemi, H. Lyytinen and A. Cichocki, Beneﬁts of multi-domain feature of mismatch negativity extracted by non-negative tensor factorization from EEG collected by low-density array, Int. J. Neural Syst. 22(6) (2012) 1250025.
- 57. F. Cong, I. Kalyakin, T. Huttunen-Scott, H. Li, H. Lyytinen, T. Ristaniemi, Single-trial based independent component analysis on mismatch negativity in children, Int. J. Neural Syst. 20(04) (2010) 279–292.
- 58. G. Zhou, A. Cichocki and S. Xie, Common and individual features analysis: Beyond canonical correlation analysis, ArXiv e-prints (2013) Available: http://arxiv.org/abs/1212.3913

