##### ORIGINAL RESEARCH ARTICLE

published: 28 June 2012 doi: 10.3389/fnins.2012.00091

# Decoding ﬁnger ﬂexion from band-speciﬁc ECoG signals in humans

### Nanying Liang1 and Laurent Bougrain1,2*

- 1 Inria, Villers-lès-Nancy, F-54600, France
- 2 Lorraine Research Laboratory in Computer Science and its Applications, UMR 7503, Université de Lorraine, Vandoeuvre-lès-Nancy, F-54506, France

Edited by: MichaelTangermann, Berlin Institute ofTechnology, Germany

Reviewed by: Klaus R. Mueller,Technical University, Germany Gerwin Schalk, Wadsworth Center, USA

*Correspondence: Laurent Bougrain, Lorraine Research Laboratory in Computer Science and its Applications, bat. C, Campus Scientiﬁque, BP 239, 54506 Vandoeuvre-lès-Nancy Cedex, France. e-mail: bougrain@loria.fr

This article presents the method that won the brain-computer interface (BCI) competition IV addressed to the prediction of the ﬁnger ﬂexion from electrocorticogram (ECoG) signals. ECoG-based BCIs have recently drawn the attention from the community. Indeed, ECoG can provide higher spatial resolution and better signal quality than classical EEG recordings. It is also more suitable for long-term use. These characteristics allow to decode precise brain activities and to realize efﬁcient ECoG-based neuroprostheses. Signal processing is a very important task in BCIs research for translating brain signals into commands. Here, we present a linear regression method based on the amplitude modulation of band-speciﬁc ECoG including a short-term memory for individual ﬁnger ﬂexion prediction.The effectiveness of the method was proven by achieving the highest value of correlation coefﬁcient between the predicted and recorded ﬁnger ﬂexion values on data set 4 during the BCI competition IV.

Keywords: brain-machine interface, electrocorticography, neuroprosthetics, feature selection, linear regression, ﬁnger ﬂexion, BCI competition IV

- 1. INTRODUCTION The goal of brain-computer interface (BCI) research is to reinstall control and communication capabilities for people with severe motor disabilities by translating brain signals into commands for a computer application or a neuroprosthesis (Wolpaw et al.,2002).

The neural electrophysiological signals currently being studied in the BCI domain ranges from electroencephalogram (EEG), electrocorticogram (ECoG), to local ﬁeld potential (LFP) and single-unit activity/multi-unit activity (SUA/MUA). These different types of brain signals have their own characteristics and there is still controversy on the type of signals which is the most suitable for the BCI applications.

Electrocorticogram electrodes are placed over the surface of thecortexwithtypically1cminter-electrodedistance(Asanoetal., 2005).Ontheonehand,ECoGprovidesahigherspatialresolution, a higher signal quality,and is more suitable for long-term use than the classical scalp EEG recordings. On the other hand,ECoG is less invasive than intracortical recordings like LFP, SUA/MUA which by far are used in a few BCI systems with human beings (Kennedy et al., 2000, 2004; Hochberg et al., 2006; Chadwick et al., 2011). By recognizing the merit of ECoG recordings, several groups of BCI researchers have carried out tests on the efﬁciency of using ECoG as control signals for human BCIs (Chin et al., 2007; Schalk et al., 2007; Pistohl et al., 2008; Sanchez et al., 2008).

SpatialresolutionplaysanimportantroleinBCI(Sanchezetal., 2008).Theﬁnespatialresolutionof ECoGprovidesabetteropportunityfordirectlydecodingbrainactivities.Therefore,itispossible to implement direct neural interfaces which are difﬁcult to be accomplished through EEG-based BCIs.

To study the usability of ECoG in BCIs, several research groups had recorded ECoG signals from the participants while they are

performing certain kind of tasks related to the brain functional areas where the electrode arrays had been implanted. The tasks include center-out reaching or pointing task (Sanchez et al.,2008), grasping(Acharyaetal.,2010),individualﬁngerﬂexion[(Kubánek et al.,2009;Wang et al.,2010;Flamary and Rakotomamonjy,2012) or (Acharya et al.,2010;Wang et al.,2011b)],and cursor trajectory (Schalk et al., 2007; Pistohl et al., 2008).

This paper describes the method we proposed to contribute to the ECoG data set from the BCI competition IV, which was dedicated to the task of decoding individual ﬁnger ﬂexion in 2008. More precisely, for decoding individual ﬁnger ﬂexion from ECoG, we noticed that a simple linear regression model of amplitude modulation (AM) of band-speciﬁc ECoG signals was efﬁcient (Sanchez et al., 2008). Moreover, we made contribution to this method in two ways: ﬁrstly,we replaced the inverse operator in the solution of the linear model by the pseudo-inverse operator that should improve the stability of the model; secondly, we proposed to use a forward feature selection procedure to select the relevant frequencybandsandelectrodes(Langley,1994).Thismethodwon the competition.

### 2. MATERIALS AND METHODS

2.1. BRAIN-COMPUTER INTERFACE COMPETITION IV – DATA SET 4

The task for data set 4 in BCI competition IV was to predict the ﬁnger ﬂexion from ECoG recordings.1 Detail description about this data set can be found in Miller and Schalk (2008). Here, we only provide a brief summary.

This data set contains data for three subjects who were epileptic patients under surgical planning. Each subject had an electrode

1The dataset is accessible through http://www.bbci.de/competition/iv/

www.frontiersin.org June 2012 | Volume 6 | Article 91 | 1

arrayplacedsubdurallyonthesurfaceof thebraininordertoidentify the epileptic focus. Each subject gave consent to participate in the recording experiments. While he/she performed a ﬁnger ﬂexion task, the corresponding ECoG signals and the ﬁnger ﬂexion time courses were recorded simultaneously. The electrode array was arranged in 8×6 or 8×8 grid (n.b., the exact location of the electrodes was unknown to the competitors because the electrode order had been scrambled during the preparation of this data set). There were 62, 48, and 64 channels for subject 1, 2, and

- 3, respectively. Subjects were asked to ﬂex a particular ﬁnger according to a

visualcue(e.g.,“index”)onacomputermonitor.Typicallyforeach cue, the subjects ﬂexed the ﬁnger 3–5 times lasting 2s followed by a rest period of 2s. There were 30 movement for each ﬁnger resulting in 600-s recordings for each subject. The ﬁrst 400-s recording were used as training set and the last 200-s recording used as testing set. Off-line analysis of the ﬁnger ﬂexion time courses revealed that the movements of the last three ﬁngers (i.e., middle, ring, and little ﬁngers) were correlated in a considerable way.

The ECoG signals were recorded through the general-purpose BCI system BCI2000 (Schalk et al., 2004), bandpass ﬁltered between 0.15 and 200Hz and sampled at 1000Hz. The ﬁnger movementswererecordedusingadatagloveandsampledat25Hz. Figure 1 provides an example of the visualization of the ECoG signals and the corresponding ﬁnger movement time course from subject1.Duetospacelimitation,onlyasubsetof ECoGelectrodes is displayed. The correlation coefﬁcient between the predicted and actual ﬁnger ﬂexion time course has been used as the evaluation criterion for this data set in the competition.

2.2. METHODS

2.2.1. Pre-processing

- 2.2.1.1. Band decomposition. The evidence of sensorimotor ECoG dynamics has been reported in several speciﬁc frequency bands including slow potentials, sub-bands (1–60Hz), gamma band (60–100Hz), fast gamma band (100–300Hz), and ensemble depolarization (300–6kHz) (Sanchez et al., 2008). Therefore, for this data set, the band-speciﬁc ECoG signals were generated using equiripple ﬁnite impulse response (FIR) ﬁlters by setting their band-pass speciﬁcations as: sub-bands (1–60Hz), gamma band (60–100Hz), and fast gamma band (100–200Hz; n.b., considering the frequency content available in this data set,the fast gamma band was deﬁned up to 200Hz and the ensemble depolarization frequency band had not been taken into account). Therefore for each channel, raw ECoG signals were decomposed into three sets of band-speciﬁc ECoG signals.
- 2.2.1.2. Amplitudemodulation. Beinginspiredbytheratecoding approach used in spike train decoding, Sanchez proposed a band-speciﬁc AM as the descriptor for ECoG signal decoding, which is deﬁned as the sum of the square voltage of the band-speciﬁc ECoG signals v in a time window ∆t:

∆t

x (tn) =

t=0

υ2 (tn + t) (1)

where ∆t =tn+1 −tn. We simply let ∆t =40ms such that the resulting band-speciﬁc AM features have the same sampling rate

|464748<br><br>| |
|---|
<br><br>49<br><br>| |
|---|
<br><br>50ThumbIndex<br><br><br>| |
|---|
<br><br>MiddleRing<br><br>0 10 20 30 40 50 60 Time (s)<br><br>Little<br><br>FIGURE 1 | For illustration purposes only, ECoG signals from channel 46 to 50 (at the top) and the corresponding movement time courses for each ﬁnger (at the bottom) for the ﬁrst 60s of the training data set from subject 1 are displayed.|
|---|

(i.e., 25Hz) as that of the dataglove position measurements. For each set of band-speciﬁc ECoG signals v, we applied equation (1) to estimate the band-speciﬁc AM features.

- 2.2.1.3. Feature selection. Since the ECoG electrode array covered quite a large zone of cortical area, only a subset of electrodes was correlated to the task. Moreover, we had no prior information about which frequency band contributed more than the other. Therefore, for each ﬁnger and each subject, we use a forward feature selection procedure in a wrapper approach (Langley,1994) to identify relevant AM features (i.e., good channel/frequency band couples). The whole set of AM features equals to 186, 144, and 192, respectively, for subject 1, 2, and 3 whose had 62, 48, and 64 channels (for three frequency bands). According to the forward selection procedure, we started from the empty set adding one by one the feature that improves the most the correlation among the remaining set of features. So, this procedure is suboptimal but the exhaustive procedure which tests all possible subsets is very time consuming here. Feature selection has been achieved and evaluated by splitting the original training set into a training set (3/5) and a validation set (2/5). The stopping criterion is satisﬁed when the correlation coefﬁcient for the validation set does not increase or when a user predeﬁned maximum number of features is reached (e.g., 10 for the results presented in Figures 2 and 3).

2.2.2. Linear regressor model

The relationship between the features and the target signals or the interaction between features was not clear for this case. We simply applied a linear model as a decoder for its robustness property. Although,wenoticedthatotheradvancedmethodshavebeenused

for ECoG signals decoding,for example,the Kalman ﬁlter (Pistohl et al.,2008),this method is not suited for our case because it needs a ﬁnger model which we do not have. The linear model we used here takes the following form:

d (tn) = WT x (tn) (2)

where d is the ﬁnger position as measured by the dataglove. x(tn) is the short-term memory AM feature vector x(tn) = [x(tn)x(tn−1)...x(tn−k)]T. k is the number of values stored. The best results have achieved when k =25. The coefﬁcients W of the model are trained with the Wiener solution:

W = E xT x

−1

E xT d (3)

where E is the expected mean. In order to improve the stability for estimating the coefﬁcients of the Wiener model, we replaced the inverse operator in equation (3) by the pseudo-inverse operator.

#### 3. RESULTS

First, we present the feature selection results. For the feature selection procedure as described in Section 1, we stop the forward selection when the number of cycles is equal to 10 or when the correlation coefﬁcient for the validation set does not increase.

Figure 2 gives an example on the evolution of the feature selection procedure for the index ﬁnger of subject 1. We found that there is no evident increment of the testing correlation coefﬁcient by increasing the number of features after the ﬁrst four features have been selected.

0.8

|Training Validation Test<br><br>| |
|---|
<br><br>| |
|---|
<br><br>| |
|---|
|
|---|

Correlationcoefficient

0.75

0.7

0.65

0.6

1 2 3 4 5 6 7 8 9 10

Number of features

selection procedure. For each step, the three bars from left to right represent the correlation coefﬁcient for the training, validation, and test set, respectively.

FIGURE 2 | Evolution of the performance for the index ﬁnger of subject 1 according to the number of features given by the forward feature

|(1, 3)(40, 3)(1, 2)(43, 2)(21, 3)(2, 2)(42, 2)(23, 1)(44, 1)(13, 2)<br><br>−0.1<br><br>0<br><br>0.1<br><br>0.2<br><br>0.3<br><br>0.4<br><br>0.5<br><br>0.6<br><br>0.7<br><br>Feature ID (channel, frequency band)<br><br>Correlationcoefficient<br><br>Training Validation Test<br><br>| |
|---|
<br><br>| |
|---|
<br><br>| |
|---|
<br><br>FIGURE 3 |The X-axis shows the ﬁrst 10 most relevant selected features, from left to right. Each feature is indicated by two elements: channel index and frequency band (1, sub-bands; 2, gamma band; and 3,<br><br>fast gamma band).TheY -axis indicates the correlation coefﬁcients of training, validation, and test set, respectively, regarding each feature individually.|
|---|

## orrelationcoefficient

Table 1 |The prediction performance of the methods (with and without band-speciﬁc features) is provided in terms of correlation coefﬁcient between the predicted and recorded ﬁnger movement for each ﬁnger and subject.

Subj. Method Thumb Index Middle Ring Little Av.

- 1 ECoG 0.00 0.13 0.01 0.22 0.06 0.08 Band-speciﬁc ECoG 0.58 0.71 0.14 0.53 0.29 0.45
- 2 ECoG 0.26 0.28 0.19 0.34 0.15 0.25 Band-speciﬁc ECoG 0.51 0.37 0.24 0.47 0.35 0.39
- 3 ECoG 0.40 0.25 0.31 0.29 0.27 0.31 Band-speciﬁc ECoG 0.69 0.46 0.58 0.58 0.63 0.59

Av. ECoG 0.22 0.22 0.17 0.28 0.16 0.21 Band-speciﬁc ECoG 0.59 0.51 0.32 0.53 0.42 0.48

The last column represents the correlation coefﬁcient value averaged over all ﬁngers; The last two rows represent the correlation coefﬁcient value averaged over all subjects. Using the band-speciﬁc ECoG approach, all p-values of a paired t-test were less than 10−4.

Figure 3 gives another point of view on the feature selection for the same subject and ﬁnger. This Figure emphasizes the individual prediction power of each feature selected during the ﬁrst 10 cycles. Looking at the ﬁrst three features, we learn that channel 1 was very useful (with two bands selected) and channel 40 was complementary. Last three features had lesser contribution to the task of decoding ﬁnger ﬂexion.

Observing the 10 most relevant selected features over the 15 possible studies (three subjects×ﬁve ﬁngers), we noted that they mainly characterized information in the gamma band (1–60Hz: 27%, 60–100Hz: 44%, and 100–200Hz: 29%).

Next, we summarized the prediction performance of this method using the testing dataset in terms of correlation coefﬁcient between the predicted and recorded ﬁnger movement

in Table 1.2 In order to highlight the effect of frequencyspeciﬁc decomposition, the results based on the original ECoG signals (i.e., without band-pass ﬁltering) are also provided for comparison.

From Table 1, we observed that the method based on bandspeciﬁcAMfeaturesobtainedbetterperformancethanthemethod

2The last element in Table 1 indicates the correlation coefﬁcient value averaged over all ﬁngers and subjects for the method based on band-speciﬁc ECoG, which is slightly different from the result of value 0.46 announced in the competition (http://www.bbci.de/competition/iv/results/index.html#dataset4) because ring ﬁngerwasremovedfromtheevaluationinthecompetitionduetotheﬁngermovements of ring ﬁnger, through off-line inspection, were quite correlated with middle ﬁnger and little ﬁnger.

|| |
|---|
<br><br>Thumb<br><br>| |
|---|
<br><br>IndexMiddleRing<br><br>0 10 20 30 40 50 60 Time (s)<br><br>Little<br><br>FIGURE 4 |Time course of the predicted (solid red) and actual (dash blue) ﬁnger ﬂexion for the ﬁrst 60s of the testing data set from subject 3.|
|---|

IndexleThumb

using the original ECoG signals (i.e., without band-speciﬁc ﬁltering). It explains that the decoding square voltage of brain signals liesincertainfrequencybandsandotherfrequencybandsaremore likely to be background noise.

We also provided in Figure 4 an example for the predicted ﬁnger movement for subject 3 using the method based on bandspeciﬁc ECoG AM features. For comparison, the corresponding time course of the recorded ﬁnger movement is plotted in the same ﬁgure.

- 4. DISCUSSION This article presents the method that won the BCI competition IV addressed to the prediction of the ﬁnger ﬂexion from ECoG signals. This method used a linear decoding scheme based on band-speciﬁc AM for decoding individual ﬁnger ﬂexion from ECoG signals in humans. The correlation between the predicted and recorded ﬁnger ﬂexion shows that ECoG-based BCIs was a promising solution for implementing a practical and apt neuroprosthesis. In particular, we can conﬁrm from the experimental results that the sensitivity proﬁle of ECoG signals is band-speciﬁc. However it is not clear if the frequency selection scheme used here

is optimal. In the forward feature selection procedure, we found thatsomefeaturesdidnotcontributetoomuchtothepredictionof ﬁnger ﬂexion alone but ranked high in the sequence of the feature selection procedure. This inspires us to consider the correlation between band-speciﬁc ECoG signals. It suggests that incorporatingthefeaturecorrelationintofeatureselection,forexample,using correlation feature selection (CFS) method (Hall, 2000), may produce an optimal compact feature set. Furthermore in a recent study (Wang et al., 2010), a sparse Gaussian process (SPGP) has been applied for decoding ﬁnger ﬂexion and a set of important features has been deduced from the length scale parameters in the trained SPGP.

We noticed that our method failed in some cases, especially for the middle ﬁnger of subject 1. It might be due to the considerable correlation between middle,ring,and little ﬁngers. This draws our attention to the natural constraints that governs the movements of ﬁngers (Wang et al., 2011a). In Wang et al. (2011a), it incorporates the prior knowledge about constraints that govern ﬁnger ﬂexion through a prior model to improve the prediction accuracy.Theirworkachievedthehighercorrelationcoefﬁcientforthis problem.

#### REFERENCES

Acharya, S., Fifer, M. S., Benz, H. L., Crone, N. E., and Thakor, N. V. (2010). Electrocorticographic amplitude predicts ﬁnger positions during slow grasping motions of the hand. J. Neural Eng. 7, 046002.

Asano, E., Juhász, C., Shah, A., Muzik, O., Chugani, D. C., Shah, J., Sood, S., and Chugani, H. T. (2005). Origin and propagation of epileptic spasms delineated on electrocorticography. Epilepsia 46, 1086–1097.

Chadwick, E. K., Blana, D., Simeral, J. D., Lambrecht, J., Kim, S. P., Cornwell, A. S., Taylor, D. M., Hochberg, L. R., Donoghue, J. P., and Kirsch, R. F. (2011). Continuous neuronal ensemble control of simulated arm reaching by a human with tetraplegia. J. Neural Eng. 8, 034003.

Chin, C., Popovic, M., Cameron, T., Lozano, A., and Chen, R. (2007). “Identiﬁcation of arm movements using electrocorticographic signals,” in 3rd International IEEE/EMBS Conference on Neural Engineering, Kohala Coast, Hawaii, 196–199.

Flamary, R., and Rakotomamonjy, A. (2012). Decoding ﬁnger movements from ECoG signals using switching linear models. Front. Neurosci. 6:29. doi:10.3389/fnins.2012.00029

Hall, M. A. (2000). “Correlation-based feature selection for discrete and numeric class machine learning,” in 7th International Conference on

Machine Learning (Morgan Kaufmann), 359–366.

Hochberg, L. R., Serruya, M. D., Friehs, G. M., Mukand, J. A., Saleh, M., Caplan, A. H., Branner, A., Chen, D., Penn, R. D., and Donoghue, J. P. (2006). Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442, 164–171.

Kennedy, P., Bakay, R., Moore, M., Adams, K., and Goldwaithe, J. (2000). Direct control of a computer fromthehumancentralnervoussystem. IEEE Trans. Rehabil. Eng. 8, 198–202.

Kennedy,P.,Kirby,M.,Moore,M.,King, B., and Mallory, A. (2004). Computer control using human intracortical local ﬁeld potentials. IEEE Trans. Neural Syst. Rehabil. Eng. 12, 339–344.

Kubánek,J.,Miller,K. J.,Ojemann,J. G., Wolpaw, J. R., and Schalk, G. (2009). Decoding ﬂexion of individual ﬁngers using electrocorticographic signals in humans. J. Neural Eng. 6, 066001.

Langley, P. (1994). “Selection of relevant features in machine learning,” in Proceedings of the AAAI Fall Symposium on Relevance (AAAI Press), New Orleans, 140–144.

Miller, K. J., and Schalk, G. (2008). Prediction of Finger Flexion 4th Brain-Computer Interface Data Competition. Available at: http://www.bbci.de/competition/iv/ desc-4.pdf

Pistohl,T.,Ball,T.,Schulze-Bonhage,A., Aertsen,A., and Mehring, C. (2008). Prediction of arm movement trajectories from ECoG-recordings in humans. J. Neurosci. Methods 167, 105–114.

Sanchez,J. C.,Gunduz,A.,Carney,P. R., and Principe, J. C. (2008). Extraction and localization of mesoscopic motor control signals for human ECoG neuroprosthetics. J. Neurosci. Methods 167, 63–81.

Schalk, G., Kubánek, J., Miller, K. J., Anderson, N. R., Leuthardt, E. C., Ojemann,J.G.,Limbrick,D.,Moran, D.,Gerhardt,L.A.,andWolpaw,J. R. (2007). Decoding two-dimensional movementtrajectoriesusingelectrocorticographic signals in humans. J. Neural Eng. 4, 264–275.

Schalk,G.,McFarland,D.,Hinterberger, T., Birbaumer, N., and Wolpaw, J. (2004). BCI2000: a general-purpose brain-computer interface (BCI) system. IEEE Trans. Biomed. Eng. 51, 1034–1043.

Wang, Z., Ji, Q., Miller, K., and Schalk, G. (2010). “Decoding ﬁnger ﬂexion from electrocorticographic signals using a sparse Gaussian process,” in 20thInternationalConferenceonPattern Recognition (ICPR), 2010,Istanbul, 3756–3759.

Wang, Z., Ji, Q., Miller, K. J., and Schalk, G. (2011a). Prior knowledge improves decoding of ﬁnger ﬂexion from electrocorticographic (ECoG) signals. Front. Neurosci. 5:127. doi:10.3389/fnins.2011.00127

Wang, Z., Schalk, G., and Ji, Q. (2011b). “Anatomically constrained decoding of ﬁngerﬂexionfromelectrocorticographic signals,” in Annual Conference on Neural Information Processing Systems (NIPS), Granada.

Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Braincomputer interfaces for communication and control. Clin. Neurophysiol. 113, 767–791.

Conﬂict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or ﬁnancial relationships that could be construed as a potential conﬂict of interest.

Received: 20 January 2012; accepted: 05 June 2012; published online: 28 June 2012. Citation: Liang N and Bougrain L (2012) Decoding ﬁnger ﬂexion from band-speciﬁc ECoG signals in humans. Front. Neurosci. 6:91. doi: 10.3389/fnins.2012.00091 This article was submitted to Frontiers in Neuroprosthetics, a specialty of Frontiers in Neuroscience. Copyright © 2012 Liang and Bougrain. This is an open-access article distributed under the terms of the Creative Commons Attribution Non Commercial License, which permits non-commercial use, distribution, and reproduction in other forums,providedtheoriginalauthorsand source are credited.

