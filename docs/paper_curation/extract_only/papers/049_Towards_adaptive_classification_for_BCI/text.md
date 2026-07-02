INSTITUTE OF PHYSICS PUBLISHING JOURNAL OF NEURAL ENGINEERING J. Neural Eng. 3 (2006) R13–R23 doi:10.1088/1741-2560/3/1/R02

TUTORIAL

# Towards adaptive classiﬁcation for BCI∗

## Pradeep Shenoy1,2, Matthias Krauledat2,3, Benjamin Blankertz2, Rajesh P N Rao1 and Klaus-Robert M¨uller2,3

- 1 Computer Science Department, University of Washington, Box 352350, Seattle, WA 98195, USA
- 2 Fraunhofer FIRST (IDA), Kekul´estr. 7, 12 489 Berlin, Germany
- 3 Department of CS, University of Potsdam, August-Bebel-Str. 89, 14 482 Potsdam, Germany

Received 19 October 2005 Accepted for publication 27 January 2006 Published 1 March 2006 Online at stacks.iop.org/JNE/3/R13

Abstract Non-stationarities are ubiquitous in EEG signals. They are especially apparent in the use of EEG-based brain–computer interfaces (BCIs): (a) in the differences between the initial calibration measurement and the online operation of a BCI, or (b) caused by changes in the subject’s brain processes during an experiment (e.g. due to fatigue, change of task involvement, etc). In this paper, we quantify for the ﬁrst time such systematic evidence of statistical differences in data recorded during ofﬂine and online sessions. Furthermore, we propose novel techniques of investigating and visualizing data distributions, which are particularly useful for the analysis of (non-)stationarities. Our study shows that the brain signals used for control can change substantially from the ofﬂine calibration sessions to online control, and also within a single session. In addition to this general characterization of the signals, we propose several adaptive classiﬁcation schemes and study their performance on data recorded during online experiments. An encouraging result of our study is that surprisingly simple adaptive methods in combination with an ofﬂine feature selection scheme can signiﬁcantly increase BCI performance.

### 1. Introduction

The goal of a brain–computer interface (BCI) is to translate the intent of a subject directly into control commands for a computer application or a neuroprosthesis. This intent is estimated from brain signals measured via signals from the scalp or from invasive techniques, cf [6, 17, 32] for an overview. A signiﬁcant challenge in designing a BCI is to balance the technological complexity of interpreting the user’s brain signals with the amount of user training required for successful operation of the interface.

The BCI scenario involves two (possibly) adaptive parts, the user and the system. The operant conditioning approach [1, 11, 28] uses a ﬁxed translation algorithm to generate a feedback signal from EEG. Users are not equipped with a mental strategy they should use. Rather, they are instructed to watch a feedback signal and to ﬁnd out how to voluntarily

∗ Part of the 3rd Neuro-IT and Neuroengineering Summer School Tutorial Series.

control it. Successful operation is reinforced by a reward stimulus. In such BCI systems, the adaptation of the user is crucial and typically requires extensive training. On the other hand, machine learning techniques allow us to ﬁt many parameters of a general translation algorithm to the speciﬁc characteristics of the user’s brain signals [4, 22, 24, 25]. This is done by a statistical analysis of a calibration measurement in which the subject performs well-deﬁned mental acts such as imagined movements [19, 27]. Here in principle no adaptation of the user is required, but it can be expected that users will adapt their behavior during feedback operation. The idea of the machine learning approach is that a ﬂexible adaptation of the system relieves a good amount of the learning load from the subject. Most BCI systems are somewhere between those extremes. Every system reacts differently to the changes of brain activity of an adapting user. Here we examine the inﬂuence of non-stationary brain signals in the operation of the Berlin BCI (BBCI). This system represents the machine learning approach to BCI and has had considerable success in allowing user operation with bitrates of up to 35 bits per

1741-2560/06/010013+11$30.00 © 2006 IOP Publishing Ltd Printed in the UK R13

minute (bpm) and as little as 30 min of calibration/training, cf [3].

in feature space, due to the different background activity of the brain during the online feedback task (see section 3.2).

The central thesis of our BBCI design is that our ofﬂine classiﬁcation accuracy, coupled with the reliability of the signals generated during motor imagery, should yield a classiﬁer with accurate online performance and no learning on the part of the user. While the system indeed achieves good accuracies in online sessions with no user training, we observed in several cases that the performance can be enhanced by manually adjusting some parameters of the translation algorithm, such as bias or scaling of the classiﬁer output. Further, during online sessions, subjects report phases where the accuracy of BCI control is degraded. Thus, there is considerable evidence of non-stationarity in the BCI classiﬁcation problem.

In the second part of our study, we propose adaptive classiﬁcation techniques for use in BCIs with CSP (common spatial patterns)-based features. We designed our schemes (see section 4) in order to gain a quantitative understanding of the change in performance, and thereby suggest remedial schemes for improving online BCI performance. We applied our adaptive techniques to a variety of datasets collected from ﬁve subjects during online BCI control.

Our results demonstrate that although instabilities in BCI control can be encountered throughout the experiment, the major detrimental inﬂuence on the classiﬁcation performance is caused by the initial shift from training to the test scenario. Hence, simple techniques that relearn only part of the classiﬁer can overcome this change and can thus signiﬁcantly improve BCI control.

Various approaches have been suggested for coping with this non-stationary behavior of EEG signals. In the BCI context, the large variety of methods used for control naturally lead to different schemes for adapting algorithm parameters during a BCI session. As a result, the success and applicability of the adaptation scheme used is heavily dependent on the chosen BCI scenario.

This study focuses on a feature space that is a lowdimensional projection of 128-channel EEG data computed by the CSP algorithm [12, 14]. However, the methods of analysis, measurement and visualization, as well as the questions regarding adaptivity addressed in this paper, are widely applicable and should serve as useful tools in studying adaptivity in the BCI context.

In [33], a visual BCI feedback was described in which the user was able to control a computer cursor in two dimensions, trying to hit one of the eight possible targets. The classiﬁcation algorithm used two distinct band-power features acquired from a small subset of 64 scalp electrodes. Several scaling factors were used to translate these features into positions on the screen, four of which were successively adapted to the individual user during the session. Similarly, [20] investigated a scenario involving a four-class BCI classiﬁcation problem. The estimation of means and covariance matrices for each of the classes was iteratively updated in a simulated online scenario; these parameter changes indicated the possibility of considerable improvement for online control. In this case, several channels from centroparietal scalp regions were used for the extraction of spectral features. In another ofﬂine study, this ﬁnding was backed by [31]; here, the parameters of a quadratic classiﬁer (QDA) were adapted after each trial of a cursor-movement task. After a careful update parameter selection, the resulting classiﬁcation was superior to the static classiﬁer that was used from the start.

### 2. Data from ofﬂine and online experiments

#### 2.1. The Berlin BCI

The Berlin brain–computer interface was developed in cooperation with the data analysis group at Fraunhofer FIRST and neurologists of Campus Benjamin Franklin, Charit´e Berlin (cf http://www.bbci.de). We use event-related (de-)synchronization(ERD/ERS)features[26]inEEGsignals related to hand and foot imagery as classes for control. These phenomena are well-studied and consistently reproducible features in EEG recordings and are used as the basis of a number of BCI systems (e.g. [8, 13]). Our EEG-to-controlsignal translation algorithm consists of two parts. We ﬁrst use a supervised feature selection algorithm called common spatial patterns (CSP) [2, 12–14] that dramatically reduces the dimensionality of the data from about 128 channels to 2–6 CSP projections. In this algorithm, the covariance matrices of the two different classes are diagonalized simultaneously in order to ﬁnd the subspaces which have the largest variances for one class while minimizing the variance for the other class (for extensions see e.g. [8–10, 18]). Thus, the chosen dimensions of the feature space are those that contain maximal discriminative information in terms of amplitude modulations. We then perform further data reduction by using the log variance of a temporal window of data from each CSP channel, i.e., a single feature per channel remains. The power of this feature selection and data reduction scheme is demonstrated by the high separability of the resulting classes of data. In this setup, we use linear discriminant analysis (LDA) to separate data points with high accuracy into classes in the low-dimensional feature space. Note that more elaborate paradigms or other feature extraction techniques may require

In each of these studies, the used method of adaptivity differs slightly and it is hard to transfer these results to other classiﬁcation approaches, since the underlying changes in the models might differ. Also, this body of work so far did not investigate neurophysiological or psychological causes for the changes of the brain patterns.

In this paper, we present a systematic quantitative study of data for multiple subjects recorded during ofﬂine and online sessions. The methods for analysis of the data and visualization thereof are applicable in general, even beyond BCI research, and provide a closer insight into the structure of the—global and local—changes in the EEG data. We study the distributions of task-relevant EEG features and provide evidenceofchangesbothinthetransitionfromofﬂinetoonline settings and in the course of a single online session. We show that the former change can be interpreted as a shift of the data

0 500

Highlighting of the target Labeling starts Target hit–Labeling ends.

- Figure 1. In the feedback session, sliding windows were used for classiﬁcation. For adaptation and evaluation, we select the windows (here colored black) between releasing the cursor and the end of the trial. See the text for details.

the use of non-linear classiﬁers (cf [21, 23, 25, 31]). Previous work [3, 5, 8] has reported on the efﬁcacy of our classiﬁcation scheme. Other physiological paradigms implemented in the BBCI focus on the use of the lateralized readiness potential [4, 15, 16] and the combination of this feature with ERD/ERS [7, 8].

#### 2.2. Experimental protocol

WeinvestigatedatafromaBCIstudyconsistingofexperiments with six subjects4. For one subject, no effective separation of brain pattern distributions could be achieved. Thus, no feedback sessions were recorded and the dataset is left out in this investigation. All experiments were conducted at Fraunhofer FIRST in cooperation with the Department of Neurology of the Charit´e Berlin. The subjects were seated in a comfortable chair with arms lying relaxed on the armrests. In the calibration measurement (also called training or ofﬂine session), every 5.5 (±0.25) s one of three different visual stimuli was presented, indicating the motor imagery task the subject should perform for 3.5 s. The imagery tasks investigated were movements of the left hand (l), the right hand (r) and the right foot (f). Brain activity was recorded from the scalp with multi-channel EEG ampliﬁers using 128 channels. Besides EEG channels, we recorded the electromyograms (EMG) from both forearms and the right leg as well as horizontal and vertical electrooculograms (EOG) from the eyes. The EMG and EOG channels were exclusively used for monitoring to make sure that the subjects performed no real limb or eye movements correlated with the mental tasks that could directly (artifacts) or indirectly (afferent signals from muscles and joint receptors) be reﬂected in the EEG channels and thus be detected by the classiﬁer, which operates on the EEG signals only. One hundred and forty trials were recorded for each class. These data were then used to train a classiﬁer for the two best discriminable classes, using the above classiﬁcation scheme (see [3, 8]). Subsequently, two feedback sessions were recorded where two targets were placed, one at each side of the screen. A 1 s window of data was used to estimate the features, which were classiﬁed over overlapping windows every 40 ms (see ﬁgure 1).

- 4 Three of the authors participated as subjects in the experiments.

The continuous output from the classiﬁer was then used to move the cursor either in a position-controlled (i.e., the scaled classiﬁer output maps directly to the horizontal position on the screen) or in a rate-controlled manner (i.e., the scaled classiﬁer output was used to move the cursor by a small amount in the chosen direction). During each trial, one of the targets was highlighted and the subject attempted to navigate the cursor into the target. Each trial lasted until the subject hit one of the two targets, and as a result the trials were of varying lengths. In a third experimental session, three rectangular targets were located at the bottom of the screen. A cursor was moving downwards with constant speed, while its horizontal position was controlled by the classiﬁer output. Again, one of the targets was highlighted and the subject was instructed to try to hit the target with the cursor. The feedback sessions were recorded in a series of runs of 28 trials each, with short breaks in between runs.

#### 2.3. Analyzing data from online sessions

Since the online sessions were controlled (i.e., the subject was directed to hit a certain target), we can use this information to label the data collected during an online session. When analyzing the data ofﬂine, as we will in the following, we have all the labels from the feedback experiment at our disposal and can use them in our evaluations. For labeling the data from an online session, we take the signals from the start of each trial until its completion and process the signals in a manner similar to the online scenario, i.e., compute features on overlapping windows of the same size and overlap as used in the online protocol. These data points are labeled according to the appropriate target class. Each trial may yield a different number of labeled data points since the trials were of varying length. When using the recorded data for testing various classiﬁcationschemes, wealwaysassignsamplescomingfrom one trial either all to the training or all to the test set.

It should be noted that in a realistic BCI scenario the labels of ongoing trials may not always be available; however, in some applications such as the use of a speller for communicating words, it is possible to estimate the labels a posteriori with high probability. Also, it is important to remember that the data were collected when the subject was using one particular classiﬁer (the optimal classiﬁer for the

|right training left training right feedback left feedback<br><br>|
|---|

|foot training left training foot feedback left feedback|
|---|

−0.5

Feedbackhyperplanenormalvector

Feedbackhyperplanenormalvector

−1

−1.5

−2

−2.5

−3

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

−3.5

−1 −0.5 0 0.5 1 1.5 2

−4 −3.5 −3 −2.5 −2 −1.5 −1 −0.5

Training hyperplane normal vector

Training hyperplane normal vector

(a) (b)

- Figure 2. Changes in the optimal classiﬁer from training to test. The ﬁgure shows, for subjects av and ay, the optimal hyperplane separating the training data classes (ofﬂine) and the test data classes (online). Also shown are the mean and covariance of the respective data distributions. In the case of subject av (a), the original classiﬁer would perform very poorly, whereas for subject ay, as indicated in (b), the change is less severe.

training data, along with any manual adjustments to it) for BCI control. Clearly, the present ofﬂine analysis results will subsequently have to be further investigated in future experiments with online control.

- 3. Changes in the distributions of EEG features

Table 1. Measuring the changes in the optimal classiﬁer for ofﬂine and online distributions. These are the changes necessary for the classiﬁer to perform optimally on feedback data, for every experiment in this study. Part (a) shows the ratio between the optimal shift for correcting the bias and the distance between class means. Part (b) shows the angle between the old hyperplane (calculated from the ofﬂine data) and the optimal hyperplane for the feedback data.

Subject al aw av ay aa

In this section, we examine the changes in performance of the subjects using a variety of measures and new ideas for visualization that help us to characterize the type and degree of changes seen in EEG features used for BCI classiﬁcation. In our study, we use the feature projections chosen by the CSP algorithm (see the previous section). We also strive to link these ﬁndings to possible neurophysiological changes that may cause these observed changes. We use two methods of visualizing the data: (1) by ﬁtting a Gaussian distribution5 on the data over an entire session (or over short-term windows), and (2) by examining the optimal separating hyperplane computed using an LDA classiﬁer on the chosen data.

- (a) Shift/distance 0.11 0.80 0.83 0.07 0.26 0.12 0.94 0.56 0.09 0.26 0.01 0.82 0.61 0.06 0.60
- (b)

Angles (◦) 13.2 26.6 15.1 15.1 9.5 9.7 20.6 28.7 17.7 6.7 36.2 45.4 4.2 40.5 13.3

in subject ay (ﬁgure 2(b)), while the test distributions are different from the training data, the impact of this change on online performance is less severe.

#### 3.1. Differences from calibration measurement to feedback

In order to examine this change more closely across all online datasets, we consider the following two possibilities for modifying the training classiﬁer hyperplane: (1) shift the original classiﬁer’s hyperplane parallel to itself6 in order to get the best performance in the online setting, and (2) in addition, rotate the hyperplane to further improve performance on the online data. We call these two methods REBIAS and RETRAIN. Table 1 summarizes the shift and angle required for optimal performance on each online dataset.

Figure 2 shows a comparison between training data collected ofﬂine and the test data recorded during a subsequent online session. The ﬁgure shows, for two subjects, the hyperplanes of the classiﬁers computed on the training and test data, respectively, along with the means and covariances of the data points from each class. For ease of visualization, we have projected the data onto two speciﬁcally chosen dimensions (see the appendix) containing maximal information. We see from ﬁgure 2(a) that for subject av the test data distributions look very different from the training data, and in fact, the original classiﬁer would perform quite poorly in the online scenario. This is not always the case, though—for example,

In order to understand the scale of the optimal shift, table 1(a) shows this shift as a fraction of the training data’s class mean distance from the training classiﬁer’s hyperplane.

- 5 On the plausibility of the assumption of Gaussian distributions in EEG data, see e.g. [4] and also the discussion in [23].

6 This can be implemented, e.g., by simply adding a bias to the classiﬁer output.

Table 2. Estimating the expected gain in classiﬁcation when adapting the separation as calculated from the ofﬂine distributions to the online distributions. Any linear decision boundary between two normally distributed random variables misclassiﬁes a certain quantile of both distributions. Here we compared the expected error quantiles for the optimal decision boundary for the training set to the decision boundary for the feedback sessions, when applied to the estimated distributions of the feedback data. Part (a) reﬂects the gain when only readapting the bias, and part (b) shows the improvement when the complete decision boundary is recalculated.

parietal α rhythm. Nevertheless, the map of r-values (see the appendix) reveals a difference focused over sensorimotor cortices. The parietal α rhythm is much less pronounced during the online session (middle row), resulting in a very strong difference between ofﬂine and online topographies, see the r-value maps in the lower row. In spite of this strong difference, the relevant difference between the tasks is qualitatively very similar in the ofﬂine and online settings (see the r-value maps in the right column). The topography of the difference between ofﬂine and online situations suggests that in the former case a strong parietal α rhythm (idle rhythm of the visual cortex) is present due to the decreased visual input during the calibration measurement, while that rhythm activity is decreased in online operation due to the increased demand for visual processing. The power spectra shown in ﬁgure 4 corroborate this assumption, since at parietal locations there is an increase in the power of the lower α band (just below 10 Hz).

Subject al aw av ay aa

- (a) REBIAS/ORIG 0.93 0.79 0.67 1.00 0.97

- 0.89 0.74 0.75 0.95 0.93
- 1.00 0.75 0.80 0.99 0.82

- (b) RETRAIN/REBIAS 0.98 0.99 0.99 0.98 0.98 0.98 0.99 0.94 0.71 0.98 0.72 0.87 1.00 0.73 0.97

Thus, there is a difference in background activity of the brain in ofﬂine and feedback settings. This difference also strongly inﬂuences the CSP features chosen for classiﬁcation, cf section 3.3. This shift in feature space implies that the old classiﬁer will perform poorly in these new settings without classiﬁer adaptation.

Note that in some cases the optimal shift is comparable to the distance of one class mean to the decision boundary. This shows that an adaptation of the bias would be necessary for correct classiﬁcation. Table 1(b) shows the angle between training and test classiﬁers’ hyperplanes on each dataset. In most cases, the angle does not change substantially. Table 2 provides an interpretation of these classiﬁer changes in terms of their impact on classiﬁer performance.

#### 3.3. Changes in EEG features during online sessions

We now examine the performance of subjects in the course of a single online session.

At each point of an online session, we consider a window for each class containing all data points from the last ten trials of that class. These data points can be used to get a local estimate of the density of each class at that point in time. We ﬁt a Gaussian distribution to these local windows of data, as well as an overall density estimate for the entire online session.

We show the ratios of estimated error quantiles for the training decision boundary, the bias-adapted decision boundary (table 2(a)) and the readapted decision boundary (table 2(b)). It is evident that the adaptation of the bias results in a signiﬁcantly lower error quantile estimate, which conﬁrms the ﬁndings in table 1, whereas an additional adaptation of the angle only gives a comparatively small gain.

Figure 5 shows for subject av the Kullback–Leibler (KL) divergence between the local density estimate for each class and the overall density estimate of that class over time. Since these curves alone do not provide information about classiﬁability of the data, we also show sample visualizations of data from certain time intervals, along with the classiﬁer hyperplane. We see that the data distribution for the foot class changes over the course of the experiment, and the KL divergence curve reﬂects these changes.

#### 3.2. Explaining the shift in data distributions

- Figure 2 and table 1 together indicate that the primary difference between the ofﬂine and online situations is a shift of the data distributions for both classes in feature space, while not signiﬁcantly changing their orientation. The source of this shift can be deduced from the spatial distributions of the band power on the scalp for the training and feedback situations.

The subject’s success in controlling the BCI was fairly varying, and the short period of time where the KL divergence for the foot class is very high corresponds to a period when the subject gained better control over the BCI. This can also be inferred from the visualizations of the distributions presented in the lower portion of the ﬁgure. A point to be noted is that breaks between runs may also affect performance. For example, one of the breaks coincided with the end of the phase with good performance—it is possible that upon resuming the experiment the subject was unable to regain the control acquired in the previous phase. For a closer look, we plot the data distributions from each uninterrupted run in ﬁgure 6. A further study consisting of new long-term experiments is needed for separating such gradual and sudden changes and

As mentioned in section 2, we use the CSP algorithm for feature extraction and the classiﬁers are trained on these features under the assumption that the spatial distribution of these activation patterns remains fairly stable during feedback.

This assumption can be veriﬁed in ﬁgure 3 which displays task-speciﬁc brain patterns during ofﬂine versus online session for one representative subject. The scalps with red resp. blue circles show band power during left hand resp. right foot motor imagery, calculated from ofﬂine (upper row) and online (middle row) sessions. In the plots of the ofﬂine session, no systematic difference between the mental states can be seen, since the maps are dominated by a strong

|<left hand><br><br>offlinesession|<right foot>|r(left, foot)|
|---|---|---|
|onlinesession| | |
|r(offline,online)| ||[Figure 1]<br><br>|
|---|
<br><br>bandpower[dB]<br><br>3<br>4<br>5<br><br><br>|[Figure 2]<br><br>|
|---|
<br><br>rvalues<br><br>−0.5<br><br>0<br><br>0.5|

offlinesessiononlinesessionr(offline,online)

bandpower[dB]

rvalues

- Figure 3. This ﬁgure shows the task-speciﬁc brain patterns and how they differ between ofﬂine and online sessions. The upper left 2 × 2 matrix of scalps displays topographic scalp maps (view from the top, nose up) of band power (broadband 7–30 Hz as used for calculating the CSP features in this subject). Maps are calculated from the ofﬂine session (upper row) resp. online session (middle row) separately for motor imagery of the left hand (left column) resp. of the right foot (middle column). Maps in the right column show the r-values of the difference between the tasks, and maps in the lower row show the r-values of the difference between ofﬂine and online sessions. While there is a huge and systematic difference between brain activity during ofﬂine and online sessions, the signiﬁcant difference between the tasks stays fairly stable when going from ofﬂine to online operation (compare the r-value maps in the right column).

| |CP|5| | |CP|4| |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| |O|z| |Training left Training right Feedback left Feedback right| | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

- Figure 4. This ﬁgure shows the spectra in the frequency range 5–25 Hz both in training and in feedback, for the two classes separately. The amplitudes are in the range 22–54 dB.

### 4. Adaptive classiﬁcation

We have shown qualitative and quantitative evidence indicating non-stationarity in the BCI classiﬁcation problem; however, two questions remain unanswered so far: (a) what is the impact of this non-stationary behavior on performance in a feedback setting? (b) What remedial measures can we use to address the non-stationary behavior of EEG-related features? In this section, we propose a range of techniques that aim to quantify the nature and impact of non-stationarity on performance, and thereby suggest adaptive methods for improving online control. Accordingly, we describe the various classiﬁers that we compare and the rationale behind each choice, and subsequently discuss their applicability in an online scenario.

#### 4.1. Adaptive methods

The adaptive classiﬁcation methods investigated are as follows:

providing further insight on the highly individual lapses of performance, but is beyond the scope of this paper. It is, however, clear and quantiﬁed in the present paper that the user’s performance over a short period of time (about 30 min) can show considerable changes.

- • ORIG: this is the unmodiﬁed classiﬁer trained on data from the ofﬂine scenario and serves as a baseline.
- • REBIAS: we use the continuous output of the unmodiﬁed classiﬁer and shift the output by an amount that would minimize the error on the labeled feedback data.

- 0

- 0.5

- 1

- 1.5 foot left

0 20 40 60 80 100 120 140 160 180 200

| | |
|---|---|

| | |
|---|---|

| | |
|---|---|

- 0.5
- 1

- 1.5
- 2

- 2.5

- 0.5
- 1

- 1.5
- 2

- 2.5

- 0.5
- 1

- 1.5
- 2

- 2.5

FeatureDistributions

−2 −1.5 −1 −0.5 0

−2 −1.5 −1 −0.5 0

−2 −1.5 −1 −0.5 0

- Figure 5. This ﬁgure shows the change of the Kullback–Leibler divergence during the feedback session. The corresponding feature distributions are displayed below for the shaded intervals. The data are projected on the plane spanned by the normal vector of the optimal separating hyperplane for the feedback and the largest PCA component of the feedback data (see the appendix).

| | |
|---|---|

| | |
|---|---|

| | |
|---|---|

| | |
|---|---|

| | |
|---|---|

−2 −1 0

- 0
- 1
- 2

| | |
|---|---|

| | |
|---|---|

| | |
|---|---|

- Figure 6. The single plots in this ﬁgure represent the development of the feature distributions for subject av throughout one feedback experiment, windows representing each run (consisting of 28 trials each). The data are projected on the feature subspace spanned by the optimal hyperplane and the largest PCA component (see the appendix).

- • RETRAIN: we use the features as chosen from the ofﬂine scenario, but retrain the LDA classiﬁer to choose the hyperplane that minimizes the error on labeled feedback data.
- • RECSP:wecompletelyignoretheofﬂinetrainingdataand perform CSP feature selection and classiﬁcation training solely on the feedback data.

The schemes are listed in increasing order of change to the classiﬁer and correspond to different assumptions on the degree of difference between ofﬂine and online data. In addition, we have the option of using (1) all the labeled online data up to the current point (cumulative), (2) only a window over the immediate past (moving), or (3) only an initial window of data from each session (initial). Each choice

corresponds to different assumptions of the volatility of the online classiﬁcation problem. We thus have C-REBIAS7, C-RETRAIN and C-RECSP, W-REBIAS, W-RETRAIN and W-RECSP, and I-REBIAS, I-RETRAIN and I-RECSP, respectively, for the three cases considered.

#### 4.2. Performance against non-adaptive classiﬁers

Figure 7(a) compares the classiﬁcation error of each adaptive method with the non-adaptive ORIG classiﬁer. The adaptive classiﬁers were trained on a window of 60 s length. This

7 C- denotes cumulative, W- denotes ﬁxed window sizes and I- denotes use of only the initial segment of the session.

50

50

50

50

50

50

| |
|---|

| |
|---|

| |
|---|

| |
|---|

| |
|---|

| |
|---|

40

40

40

40

40

40

Biastemp –kfold

Biastemp–kfold

Biastemp–kfold

30

30

30

30

30

30

ORIG

ORIG

ORIG

20

20

20

20

20

20

10

10

10

10

10

10

0

0

0

0

0

0

0

10 20 30 40 50

0 10 20 30 40 50

0 10 20 30 40 50

0 10 20 30 40 50

0 10 20 30 40 50

0 10 20 30 40 50

C–REBIAS

W–REBIAS

I–REBIAS

C–REBIAS

W–REBIAS

I–REBIAS

50

| |
|---|

40

30

ORIG

ORIG

20

10

0

0 10 20 30 40 50

C–RETRAIN

50

| |
|---|

40

30

ORIG

20

10

0

0 10 20 30 40 50

W–RETRAIN

50

| |
|---|

40

30

20

10

0

0 10 20 30 40 50

I–RETRAIN

50

| |
|---|

40

LDAtemp –kfold

LDAtemp–kfold

30

20

10

0

0 10 20 30 40 50

C–RETRAIN

50

| |
|---|

40

LDAtemp –kfold

30

20

10

0

0 10 20 30 40 50

W–RETRAIN

50

| |
|---|

40

30

20

10

0

0 10 20 30 40 50

I–RETRAIN

50

| |
|---|

40

30

ORIG

ORIG

20

10

0

0 10 20 30 40 50

C–RECSP

50

| |
|---|

40

30

ORIG

20

10

0

0 10 20 30 40 50

W–RESCP

(a)

50

| |
|---|

40

30

20

10

0

0 10 20 30 40 50

I–RECSP

50

| |
|---|

40

CSPtemp –kfold

CSPtemp –kfold

30

20

10

0

0 10 20 30 40 50

C–RECSP

50

| |
|---|

40

CSPtemp –kfold

30

20

10

0

0 10 20 30 40 50

W–RESCP

(b)

50

| |
|---|

40

30

20

10

0

0 10 20 30 40 50

I–RECSP

- Figure 7. Comparison of various adaptive classiﬁcation methods on data recorded from online sessions. Each subplot is a scatter plot, with the error rate of a reference method on the y-axis and the error rate of the method of investigation on the x-axis. The performance of the latter is better for those data points that lie over the diagonal. Error rates are given in percentage. (a) All the REBIAS and RETRAIN variants clearly outperform the unmodiﬁed classiﬁer trained on the ofﬂine data. (b) The adaptive methods are compared against a theoretical cross-validation error baseline that uses labels of future data points in the online session. See the text for more details.

was also the shortest (i.e., ﬁrst) window of the cumulative classiﬁers.

Each row presents the three different possibilities for training data, and each column presents the three adaptation methods considered. Inspecting each column, we see that the schemes REBIAS and RETRAIN clearly outperform the ORIG classiﬁer, since most of the classiﬁcation errors on the feedback data decrease. RECSP, on the other hand, does not improve performance. A possible reason for this is the small training sample size, a question we will revisit in the next section. Further, when examining each row, we see that the I- methods perform better than the W- and C- methods, indicating that the I- methods are more stable than the C- and W- methods.

Also, onexaminingallnineplotsinﬁgure7(a), weseethat the I-REBIAS method is comparable to all the other schemes. This is a very useful result because the I-REBIAS method is a lightweight adjustment that only requires a short initial calibration period and is thus relatively non-intrusive. Thus, ﬁgure 7(a) shows that adaptive methods can indeed improve performance, even with simple adaptive schemes.

#### 4.3. Performance against baseline cross-validation error

We now examine the following question regarding the online BCI scenario: how non-stationary is the data distribution within the online sessions? For each method, we deﬁne an idealized baseline scenario where the method can access the data and labels of both past and future from an online session.

We then compare the temporal8 k-fold cross-validation error of the method in this baseline scenario to the method trained only on data from the past (as in the previous experiment).

This choice of baseline is aimed at examining whether each method suffers from having ‘too much’ training data, or too little data. For example, if the classiﬁcation problem were highly non-stationary, we would then expect the windowed methods to outperform the baseline, since they can adapt to local changes. If the data are fairly stable across an online session, then the baseline cross-validation error would be lower, since it has more training data.

Figure 7(b) shows the results of this comparison. We can make the following inferences from the ﬁgure: ﬁrst, the baseline is better in almost all cases, indicating that the adaptive methods have insufﬁcient data. This is especially true for the RECSP algorithms and is clearly because of the very high dimensional data they deal with. Second, the REBIAS methods do not beneﬁt very much by the addition of more data, and the I-REBIAS error is comparable to the temporal k-fold error on REBIAS. This does not necessarily mean that there are no dynamic changes in the data; in fact, in section 3.3 we see that the data distributions move around considerably. Instead, these results indicate that within the constraints of the chosen feature space and the adaptive algorithm, more training data will not help. Thus, the changes in the data are more in the nature of phases where the separability of the data is poor. The positive result from this experiment is that the performance of

8 That is, the data are divided into k contiguous blocks in order to prevent overﬁtting.

a continually changing interface, or overﬁtting data during the subject’s familiarization phase.

0.38

|C–REBIAS W–REBIAS C–RETRAIN W–RETRAIN C–RECSP W–RESCP<br><br>|
|---|

Our results also indicate that this one-time adjustment is in fact sufﬁcient for the time periods we have considered (up to 1 h of continuous use). The success of the simple adaptive schemes is mainly due to the effectiveness of our ofﬂine feature selection scheme and the fact that the basic neurophysiological processes used for control are similar in the ofﬂine and feedback scenarios.

0.36

0.34

0.32

0.3

0.28

While changes in performance and feature distributions do occur during online sessions (see section 3.3), our classiﬁcation results indicate that on average they do not have a signiﬁcant effect on performance. It remains unclear at this point whether these changes can be affected by a different choice of feature space or the use of additional features; however, a complete relearning of the feature selection is impractical due to the need for large amounts of labeled data. Our planned studies of longer term BCI operation aim to shed further light on the exact nature of the changes during an online setting.

0.26

0.24

0.22

0.2

0.18

20 40 60 80 100 120

- Figure 8. Inﬂuence of parameters on the adaptive classiﬁcation results. This ﬁgure shows the average error across all sessions and subjects as a function of the window of data points (in seconds) used for the windowed classiﬁcation methods. For the C- classiﬁers, this indicates the size of the ﬁrst training window.

the REBIAS algorithm, using only an initial window of data, is comparable to the ideal cross-validation baseline error for the REBIAS algorithm.

#### 4.4. Increasing available training data

We now examine whether our choice of feature space is a factor in the performance of our classiﬁcation algorithm. Figure 8 shows the error averaged across subjects for each dynamic version of the adaptive algorithms (i.e., the C- and W- methods), as a function of the data window used for training. The ﬁgure conﬁrms that the RECSP methods indeed improve on addition of training data; however, they are still considerably worse than the best performing algorithm. Our experiments were not sufﬁciently long to examine whether, with sufﬁcient data, the RECSP algorithms can be competitive.

### 5. Discussion

A proposal for adaptive algorithms in BCI has to address the following issues: (a) the need for adaptivity, (b) the possible sources of the change in the data, (c) an adaptive scheme that can demonstrably improve performance over the nonadaptive baseline algorithm, and (d) the impact of the adaptive algorithm on the subject who is trying to use the BCI for control.

We have shown that an important factor affecting online BCI performance is the neurophysiological change to the mental state of the subjects (as described in section 3.3) between the ofﬂine and online settings. Our results show both that in a CSP-based BCI system adaptive methods are necessary and that simple adaptive schemes can signiﬁcantly improve performance. The adaptive method we recommend speciﬁcally addresses the change from training data to online performance and is in the form of a small one-time bias adjustment. As a result, we do not risk confusing the user with

### 6. Conclusion

EEG-based brain–computer interfaces frequently have to deal with a decrease in performance when going from ofﬂine calibration sessions to online operation of the BCI. One explanation for this decrease is that bad model selection strategies have resulted in overly complex classiﬁcation models that overﬁt the EEG data [23]. The current work has clearly shown that an alternative reason for failure should also be considered: non-stationarities in the EEG statistics. The subject’s brain processes during feedback can cause the distributions to wander astray on a very local time scale. This could in principle make classiﬁcation a difﬁcult problem, perhaps necessitating special statistical modeling that takes into account covariate shifts [29] or even more sophisticated techniques such as transductive inference [30]. However, the successful adaptive methods investigated in this work turn out to be surprisingly simple: a bias adaptation in combination with an ofﬂine feature selection scheme signiﬁcantly increases BCI performance. We clearly demonstrated that the strongest source of non-stationarity stems from the difference between calibration and feedback sessions, whereas during the feedback session the statistics seems rather stable on the scale of up to an hour (depending on the subject). So a practical recommendation of this study is (1) to correct for the bias between calibration and feedback sessions, and (2) either to incorporate intermediate corrections every half hour with a short 2–3 min calibration or to adapt the bias when changes of the statistics, say due to fatigue, are observed. Future research will explore the use of transductive methods and dedicated statistical tests to detect and address non-stationarities automatically.

### Acknowledgments

We thank G Dornhege, A Schwaighofer, F Meinecke, S Harmeling and G Curio for helpful discussions. The work

of MK, BB and KRM was supported in part by grants of the Bundesministerium fur¨ Bildung und Forschung (BMBF), FKZ 01 IBE 01A/B, by the Deutsche Forschungsgemeinschaft (DFG), FOR 375/B1 and MU 987/1-1, and by the IST Programme of the European Community, under the PASCAL Network of Excellence, IST-2002-506778. This publication only reﬂects the authors’ views. Rajesh P N Rao was supported by NSF grant 130705 and the Packard Foundation. We thank the anonymous reviewers for their comments that helped us to improve the quality of this manuscript.

For two n-dimensional random variables X1,X2 with X1 ∼ N(µ1, 1) and X2 ∼ N(µ2, 2), this amounts to

KL PX

#### ,PX

1

2

= − 12 log 1 −1

2 + E(X1 − µ1)t 1 −1(X1 − µ1) −E(X1 − µ2)t 2 −1(X1 − µ2)

= − 12 log 1 −1

2 + trace E(X1 − µ1)(X1 − µ1)t 1 −1 −trace E(X1 − µ1)(X1 − µ1)t 2 −1 −(µ2 − µ1)t 2 −1(µ2 − µ1)

= − 12 log 1 −1

#### 2 + trace I − 1 2 −1 −(µ2 − µ1)t 2 −1(µ2 − µ1) ,

### Appendix

where I denotes the n-dimensional identity matrix.

In ﬁgure 5, we estimated the overall feedback densities of both classes on all trials of the feedback session and displayed their Kullback–Leibler divergence to the local estimates of the densities, which are obtained by averaging over the features from the last ten trials of each class.

#### A.1. Feature distribution projections

The lower part of ﬁgure 5 shows local estimates of the distributions of both classes during one feedback session. We ﬁrst calculated the classiﬁer which is optimal for the feedback session and the largest PCA component wPCA of the features. The x-axis shows the projection of the data on normal vector wFB of that hyperplane of the feature space corresponding to the decision boundary of the classiﬁer. The other dimension is chosen orthogonally to wFB, such that wPCA is contained in this two-dimensional subspace. It is a property of this display mode that the relative location of the distributions to the hyperplane can be seen by orthogonal projection, and the dimension with the largest variance is contained in this plot, while preserving the angles of the original space.

### References

- [1] Birbaumer N, Ghanayim N, Hinterberger T, Iversen I, Kotchoubey B, K¨ubler A, Perelmouter J, Taub E and Flor H 1999 A spelling device for the paralysed Nature

398 297–8

- [2] Blanchard G and Blankertz B 2004 BCI competition 2003–data set IIa: spatial patterns of self-controlled brain rhythm modulations IEEE Trans. Biomed. Eng.

51 1062–6

- [3] Blankertz B, Dornhege G, Krauledat M, M¨uller K-R and Curio G 2005 The Berlin brain–computer interface: report from the feedback sessions Technical Report 1 (Fraunhofer FIRST) http://ida.ﬁrst.fraunhofer.de/publications/ BlaDorKraMueCur05.pdf
- [4] Blankertz B, Dornhege G, Sch¨afer C, Krepki R, Kohlmorgen J, M¨uller K-R, Kunzmann V, Losch F and Curio G 2003 Boosting bit rates and error detection for the classiﬁcation of fast-paced motor commands based on single-trial EEG analysis IEEE Trans. Neural Syst. Rehabil. Eng.

11 127–31

- [5] Blankertz B et al 2004 The BCI competition 2003: progress and perspectives in detection and discrimination of EEG single trials IEEE Trans. Biomed. Eng. 51 1044–51
- [6] Curran E A and Stokes M J 2003 Learning to control brain activity: a review of the production and control of EEG components for driving brain–computer interface (BCI) systems Brain Cogn. 51 326–36
- [7] Dornhege G, Blankertz B, Curio G and M¨uller K-R 2003 Combining features for BCI Advances in Neural Information Processing Systems (NIPS 02) vol 15, ed S Becker, S Thrun and K Obermayer, pp 1115–22
- [8] Dornhege G, Blankertz B, Curio G and M¨uller K-R 2004 Boosting bit rates in non-invasive EEG single-trial classiﬁcations by feature combination and multi-class paradigms IEEE Trans. Biomed. Eng. 51 993–1002
- [9] Dornhege G, Blankertz B, Curio G and M¨uller K-R 2004 Increase information transfer rates in BCI by CSP extension to multi-class Advances in Neural Information Processing Systems vol 16, ed S Thrun, L Saul and B Sch¨olkopf (Cambridge, MA: MIT Press) pp 733–40
- [10] Dornhege G, Blankertz B, Krauledat M, Losch F, Curio G and M¨uller K-R 2006 Optimizing spatio-temporal ﬁlters for improving brain–computer interfacing Advances in Neural Information Processing Systems (NIPS 05) vol 18, at press

Figure 2 is generated similarly, only the dimensions used here are the normal wTR of the original classiﬁer as obtained from the training session and the normal wTR from the feedback classiﬁer hyperplane (as above). The black and gray lines denote the intersections of the decision boundaries of the classiﬁers with the subspace which is shown here. Also in this case, the projection preserves angles.

#### A.2. Bi-serial correlation coefﬁcients

In ﬁgure 3, we show the r-values rch of the band-power values fvch in each channel ch. The bi-serial correlation coefﬁcient r measures how much information one feature carries about the labels. It is computed in the following way:

(µ1 − µ2)√#cl1#cl2 √var(fvch)(#cl1 + #cl2)

rch =

,

where µi is the class-speciﬁc mean of fvch and #cli denotes the number of trials for class i ∈ {1,2}.

#### A.3. Kullback–Leibler distance

The Kullback–Leibler distance (or Kullback–Leibler divergence) of the probability distributions P and Q is deﬁned by

- p(x)

- q(x)

KL(P,Q) := p(x)log

dx.

- [22] Mill´an J D R, Renkens F, J M no and Gerstner W 2004 Non-invasive brain-actuated control of a mobile robot by human EEG IEEE Trans. Biomed. Eng. 51 1026–33
- [23] M¨uller K-R, Anderson C W and Birch G E 2003 Linear and non-linear methods for brain–computer interfaces IEEE Trans. Neural Syst. Rehabil. Eng. 11 165–9
- [24] M¨uller K-R, Krauledat M, Dornhege G, Curio G and Blankertz B 2004 Machine learning techniques for brain–computer interfaces Biomed. Tech. 49 11–22
- [25] M¨uller K-R, Mika S, R¨atsch G, Tsuda K and Sch¨olkopf B 2001 An introduction to kernel-based learning algorithms IEEE Neural Netw. 12 181–201
- [26] Pfurtscheller G and da Silva F H L 1999 Event-related EEG/MEG synchronization and desynchronization: basic principles Clin. Neurophysiol. 110 1842–57
- [27] Pfurtscheller G and Neuper C 1997 Motor imagery activates primary sensorimotor area in humans Neurosci. Lett.

239 65–8

- [28] Rockstroh B, Birbaumer N, Elbert T and Lutzenberger W 1984 Operant control of EEG and event-related and slow brain potentials Biofeedback Self-Regul. 9 139–60
- [29] Sugiyama M and M¨uller K-R 2006 Input-dependent estimation of generalization error under covariate shift Statistics and Decisions at press (http://www.cs.titech.ac.jp/tr/reports/ 2005/TR05-0001.pdf)
- [30] Vapnik V 1998 Statistical Learning Theory (New York: Wiley)
- [31] Vidaurre C, Schl¨ogl A, Cabeza R and Pfurtscheller G 2004 About adaptive classiﬁers for brain–computer interfaces Biomed. Tech. 49 85–6
- [32] Wolpaw J R, Birbaumer N, McFarland D J, Pfurtscheller G and Vaughan T M 2002 Brain–computer interfaces for communication and control Clin. Neurophysiol.

113 767–91

- [33] Wolpaw J R and McFarland D J 2004 Control of a two-dimensional movement signal by a noninvasive brain–computer interface in humans Proc. Natl Acad. Sci. USA 101 17849–54

- [11] Elbert T, Rockstroh B, Lutzenberger W and Birbaumer N 1980 Biofeedback of slow cortical potentials: I Electroencephalogr. Clin. Neurophysiol. 48 293–301
- [12] Fukunaga K 1990 Introduction to Statistical Pattern Recognition 2nd edn (Boston, MA: Academic)
- [13] Guger C, Ramoser H and Pfurtscheller G 2000 Real-time EEG analysis with subject-speciﬁc spatial patterns for a brain–computer interface (BCI) IEEE Trans. Neural Syst. Rehabil. Eng. 8 447–56
- [14] Koles Z J and Soong A C K 1998 EEG source localization: implementing the spatio-temporal decomposition approach Electroencephalogr. Clin. Neurophysiol. 107 343–52
- [15] Krauledat M, Dornhege G, Blankertz B, Curio G and M¨uller K-R 2004 The Berlin brain–computer interface for rapid response Biomed. Tech. 49 61–2
- [16] Krauledat M, Dornhege G, Blankertz B, Losch F, Curio G and M¨uller K-R 2004 Improving speed and accuracy of brain–computer interfaces using readiness potential features Proc. 26th Annual Int. Conf. IEEE EMBS on Biomedicine (San Francisco)
- [17] K¨ubler A, Kotchoubey B, Kaiser J, Wolpaw J and Birbaumer N 2001 Brain–computer communication: unlocking the locked in Psychol. Bull. 127 358–75
- [18] Lemm S, Blankertz B, Curio G and M¨uller K-R 2005 Spatio-spectral ﬁlters for improved classiﬁcation of single trial EEG IEEE Trans. Biomed. Eng. 52 1541–8
- [19] McFarland D J, Miner L A, Vaughan T M and Wolpaw J R 2000 Mu and beta rhythm topographies during motor imagery and actual movements Brain Topogr. 12 177–86
- [20] Mill´an J D R 2004 On the need for on-line learning in brain–computer interfaces Proc. Int. Joint Conf. on Neural Networks (Budapest, Hungary, July 2004) (IDIAP-RR 03-30)
- [21] Mill´an J D R, Mouri˜no J, Franz´e M, Cinotti F, Varsta M, Heikkonen J and Babiloni F 2002 A local neural classiﬁer for the recognition of EEG patterns associated to mental tasks IEEE Trans. Neural Netw. 13 678–86

