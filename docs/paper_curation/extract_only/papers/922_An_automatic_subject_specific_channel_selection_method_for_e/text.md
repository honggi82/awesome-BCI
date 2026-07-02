[Figure 1]

## An Automatic Subject Specific Channel Selection Method for Enhancing Motor Imagery Classification in EEG-BCI using Correlation

Gaur, P., McCreadie, K., Pachori, R. B., Wang, H., & Prasad, G. (2021). An Automatic Subject Specific Channel Selection Method for Enhancing Motor Imagery Classification in EEG-BCI using Correlation. Biomedical Signal Processing and Control, 68, Article 102574. https://doi.org/10.1016/j.bspc.2021.102574

Link to publication record in Ulster University Research Portal

Published in: Biomedical Signal Processing and Control

Publication Status: Published (in print/issue): 31/07/2021

DOI: 10.1016/j.bspc.2021.102574

Document Version Author Accepted version

##### Document Licence: CC BY-NC-ND

For Author Accepted Manuscripts (AAM) published under Ulster University's Rights Retention Policy for Scholarly Works (RRPSW)

When citing an AAM published under Ulster University's RRPSW please use the following citation structure: Author, A. A. (Year). Title of article. Journal Name, [Accepted Author Manuscript]. PURE Portal URL. Licensed under CC BY 4.0. General rights The copyright and moral rights to the output are retained by the output author(s), unless otherwise stated by the document licence. Unless otherwise stated, users are permitted to download a copy of the output for personal study or non-commercial research and are permitted to freely distribute the URL of the output. They are not permitted to alter, reproduce, distribute or make any commercial use of the output without obtaining the permission of the author(s). If the document is licenced under Creative Commons, the rights of users of the documents can be found at https://creativecommons.org/share-your-work/cclicenses/. Take down policy The Research Portal is Ulster University's institutional repository that provides access to Ulster's research outputs. Every effort has been made to ensure that content in the Research Portal does not infringe any person's rights, or applicable UK laws. If you discover content in the Research Portal that you believe breaches copyright or violates any law, please contact pure-support@ulster.ac.uk

Download date: 26/06/2026

# An Automatic Subject Speciﬁc Channel Selection Method for Enhancing Motor Imagery Classiﬁcation in EEG-BCI using Correlation

Pramod Gaur1,, Karl McCreadie2,, Ram Bilas Pachori3,, Hui Wang4,, Girijesh Prasad2,

### Abstract

A motor imagery (MI) based brain-computer interface (BCI) decodes the motor intention from the electroencephalogram (EEG) of a subject and translates this into a control signal. These intentions are hence classiﬁed as different cognitive tasks, e.g. left and right hand movements. A challenge in developing a BCI is handling the high dimensionality of the data recorded from multichannel EEG signals which are highly subject-speciﬁc. Designing a portable BCI whilst minimizing EEG channel number is a challenge. To this end, this paper presents a method to reduce the channel count with the goal of reducing computational complexity whilst maintaining a suﬃcient level of accuracy, by utilising an automatic subject-speciﬁc channel selection method created using the Pearson correlation coeﬃcient. This method computes the correlation between EEG signals and helps to select highly correlated EEG channels for a particular subject without compromising classiﬁcation accuracy (CA). Common spatial patterns (CSP) are used to analyse imagined left and right hand movements and the method is evaluated on both BCI Competition III Dataset IIIa and right hand and foot imagined tasks on BCI Competition III Dataset IVa. For both datasets, a minimum number of EEG channels are identiﬁed with an average channel reduction of 65.45% whilst demonstrating an increase of >5% in CA using channel Cz as a reference.

1Department of Computer Science, BITS Pilani, Dubai Campus, Dubai, UAE. 2Intelligent Systems Research Centre, Ulster University, United Kingdom. 3Department of Electrical Engineering, Indian Institute of Technology Indore, Indore,

India. 4School of Computing, Ulster University, United Kingdom.

Preprint submitted to Biomedical Signal Processing and Control March 17, 2021

Keywords: Brain-computer interface, motor-imagery, common spatial patterns, linear discriminant analysis, channel selection.

### 1. Introduction

A brain-computer interface (BCI) aims to provide a communication pathway for severely motor impaired people whose natural neuromuscular pathways have become damaged [1] and translates neurophysiological signals into commands used to control external mechanisms [2]. One common example of a BCI system is based upon imagined movement or motor imagery (MI) and does not require actual body movement [3] instead using the recorded neurophysiological activity associated with imagined movement as control commands [4]. Some BCI systems record multichannel electroencephalography (EEG)/magnetoencephalography (MEG) data to achieve good performance but many of these recorded channels will contain irrelevant information and noise [5, 6, 7] which requires a preprocessing step to remove [8, 9, 10]. There is often little evidence that exists on the location and number of channels needed for a particular MI task to achieve optimal performance. Additionally, the number of channels and their location is also likely to vary between individuals meaning that even if an optimal subset of channels is found for one subject, this same subset is unlikely to produce the same performance for a diﬀerent subject. Producing a subset of channels enables the rejection of noisy channels whilst allowing for a similar if not higher level of classiﬁcation accuracy with the beneﬁt of reduced processing time, equipment and computational cost. Thus, this paper presents an algorithm which can automatically select subject speciﬁc subsets of channels to enhance classiﬁcation accuracy of MI tasks.

To date, there have been a number of channel selection methods discussed in the literature based with on either manual or automatic techniques. Channels are often simply manually selected based on prior neurophysiological knowledge. For instance, MI based BCI systems generally focus on the sensorimotor cortex and channels around C3, C4, and Cz of the 10-20 system where most movement-related activity tends to occur [8, 11, 12].

If channels are not selected manually, then they may be selected using a ﬁlter-based technique, wrapper-based technique, or a combination of these. In wrapper-based techniques, potentially useful subsets of channels are evaluated and subsequently selected using a speciﬁc classiﬁer through training

and testing. However, this technique does tend to overﬁt and is more expensive in terms of computation when compared against ﬁlter-based methods. He et al. [13] used Common Spatial Patterns (CSP) and a Bayes classiﬁer to reduce their channel count from 59 to an average of 33 whilst reporting an accuracy of approximately 95%. Whereas Wang et al. [14] used a Fisher discriminant classiﬁer and CSP to show accuracies above 90% for two subjects using just four channels.

Filter-based techniques, on the other hand, tend to be faster, do not require a classiﬁer, and are scalable. However, these beneﬁts come with the disadvantage of a generally lower accuracy than wrapper-based methods. Yang et al. [15] were able to reduce their channel count from 118 to 11 without signiﬁcantly aﬀecting accuracy, whilst Yang et al. [16] used a genetic algorithm in combination with an artiﬁcial neural network (ANN) to give an accuracy of 80% with 10 channels and 86% from just 6 channels using another dataset. Recently, Gaur et al. [10, 17] randomly selected ﬁfteen channels from a dataset of twenty-two channels over the motor cortex region. This approach helped them to achieve a better classiﬁcation accuracy than when using all twenty-two channels. In a more recent study, EEG signals were classiﬁed into left hand and right MI task using tangent space based transfer learning to enhance the generalized capability of BCI applications [18]. For a review of channel selection algorithms speciﬁc to EEG, readers can refer to [19] whilst [20] provides a more recent survey of MI speciﬁc ﬁltering techniques.

Various MI related channel selection methods have been proposed [21, 22, 23, 24, 25]. In [21], the CSP-rank identiﬁes the most relevant channels for each MI task in all frequency bands and features are only extracted from selected channels in those frequency bands utilizing the existing capability of the least absolute shrinkage and selection operator (LASSO) algorithm [22]. In another study, Park and Chung [23] performed channel selection using a frequency-optimized local region CSP approach using the variance ratio dispersion score (VRDS) and inter-class feature distance (ICFD) of small EEG channel groups. Another research group [24], applied class correlation, ReliefF, random forest feature ranking, and inﬁnite latent feature selection (ILFS) in multiple frequency bands to identify relevant channels. Using a four-class MEG MI BCI dataset a channel group was formed based on strongly correlated channels whereas Park et al. [25], selected the group with the highest Fisher score as a channel subset using a ﬁlter-bank CSP technique.

This paper aims to implement channel reduction through subject-speciﬁc

channel selection. The study aids in the selection of highly correlated EEG channels against a reference channel for each subject without compromising classiﬁcation accuracy. A subject-speciﬁc subset of channels allows for a more performant classiﬁer whilst allowing for a reduction in both computational complexity and hence time. Three variations of a novel channel selection technique are presented to automatically select these channels, taking as a reference channel C3, C4, or Cz for each subject.

The aims of the paper are thus:

- 1. To eliminate the non-discriminative information from discriminative information present in the EEG channels;
- 2. To implement subject-speciﬁc EEG channel selection where EEG channels are automatically selected based on the Pearson correlation coefﬁcient method using a reference channel;
- 3. To evaluate the performance of the proposed methods on diﬀerent MI tasks because in each task EEG signals are measured from the same cortical areas;
- 4. To ﬁnd whether it is possible to achieve better classiﬁcation accuracy using fewer monopolar EEG channels;
- 5. To report the classiﬁcation accuracy when single trials are classiﬁed.

The paper is organized as follows: Section 2 describes the dataset, signal processing and feature extraction methods including correlation and CSP; Section 3 presents and discusses the results which includes a comparison of results reported in the literature using the same data-sets [26], whilst Section 4 concludes the study.

### 2. Methods

- 2.1. Dataset

The BCI Competition III Dataset IVa [22] was used for this study. The dataset contains multichannel EEG recorded from ﬁve healthy subjects seated in a comfortable chair with their arms on armrests. The dataset contains 118 EEG signals which were then band-pass ﬁltered from 0.05 to 200 Hz then sampled at a frequency of 1000 Hz and further down-sampled to 100 Hz. Visual cues were shown to subjects to perform three diﬀerent types of MI tasks for a duration of 3.5 s: (L) left hand, (R) right hand, or (F) foot. An inter-trial interval of approximately 2 s was allowed for participants to take

[Figure 2]

Figure 1: A block diagram detailing the signal processing pipeline from both a training and testing perspective.

#### a short break. For this study, classiﬁcation of right hand and foot MI tasks was used to show the eﬀectiveness of the proposed method compared to the results from a group [26] who studied the same classiﬁcation problem.

Table 1: Trial information for BCI Competition III Dataset IVa.

|Subject|Training trials|Testing trials|
|---|---|---|
|A01<br><br>|168|112|
|A02<br><br>|224<br><br>|56|
|A03|84<br><br>|196|
|A04|56<br><br>|224|
|A05|28<br><br>|252|

A total of 280 trials were available for each of the ﬁve subjects with 118 EEG channels recorded. Table 1 displays the number of training trials (labelled) and test trials (unlabelled) for all ﬁve subjects. A detailed breakdown of the training and testing trials for each subject is given in Table 1.

BCI Competition III Dataset IIIa [27] was also used which comprises EEG signals recorded from three subjects, wherein subjects perform right hand, left hand, tongue, and foot MI tasks. Sixty EEG signals were recorded for each subject. For this study, only EEG signals related to left and right

#### hand MI tasks were considered. For each subject, a training (labelled) and testing (unlabelled) set were used for this classiﬁcation problem.

Table 2: Trial information for BCI Competition III Dataset IIIa.

|Subject|Training trials|Testing trials|
|---|---|---|
|B01|45|45|
|B02|30<br><br>|30|
|B03<br><br>|30|30|

Each set consisted of 45 trials per set for subject B1 whilst subjects B2 and B3 contained 30 trials. A detailed breakdown of the training and testing sets for each subject may be obtained from Table 2.

- 2.2. Signal Processing A BCI consists of several diﬀerent signal processing stages as illustrated

in Fig. 2. This paper will focus on the feature extraction stage by separating and eliminating non-discriminative information from discriminative information present in the EEG channels. This is performed by selecting appropriate EEG channels and hence performing dimensionality reduction, as a higher number of channels means a higher dimensional signal and therefore a higher subsequent number of potential features. As discussed earlier there have been several attempts to reduce this dimensionality as evidenced in the literature. This paper uses the Pearson correlation coeﬃcient to reduce this dimensionality and hence the computational complexity with the aim of preserving or improving classiﬁcation accuracy.

- 2.2.1. Feature Extraction Pearson’s Correlation Coeﬃcient (CC) Features are extracted by

taking of one of three channels, i.e. C3, C4, or Cz, as a reference and its correlation with the remaining channels is calculated. Channels with a correlation value of >0.5, >0.6, >0.7, or >0.8 are selected and the rest of the channels are discarded (Fig. 1). More details about the number of channels selected for each subject are reported in the results section.

The discrete classiﬁcation of each evaluation trial is assigned a class. For each trial in the evaluation data for a particular subject, the features are extracted using a time segment between 0.5 s to 2.5 s following the cue having advised the subject to imagine a particular MI task (similar to the BCI Competition III Dataset IVa winner). With each CSP algorithm, 3 pairs

[Figure 3]

Figure 2: An overview of the brain-computer interface (BCI) closed loop.

of spatial ﬁlters (sf) are used to extract features (sf = 3), as recommended in [26, 28]. The extracted features are classiﬁed using a linear discriminant analysis (LDA) algorithm, more details of which may be obtained from [29].

The algorithm for the proposed method is found below:

Algorithm 1 Proposed subject speciﬁc channel selection algorithm Input: Let X denote the signal in time domain Output: Subject speciﬁc channels selected based on correlation taking

C3/C4/Cz as a reference channels separately

- 1: For each reference channel selected from C3/C4/Cz
- 2: For each subject in time domain
- 3: Using the selected as reference channel, compute correlation with all the remaining channels in training session
- 4: Select all channels with correlation > 0.7 in the training session and simultaneously select the same identiﬁed channels in evaluation session
- 5: return Channels selected for each subject with correlation > 0.7 in training session and evaluation session

Common Spatial Pattern (CSP) The common spatial patterns (CSP) algorithm aims to learn spatial ﬁlters which minimise the variance of a class

while maximising the variance of another. It is often helpful to bandpass ﬁlter the multichannel EEG signals [28, 12]. The band-power in any given frequency band gives the variance of the ﬁltered EEG signals in the selected band. The CSP method obtains optimal discrimination for MI based BCI tasks based on band-power features [12]. The CSP method uses the spatial ﬁlters w by optimizing the function as follows:

wTC1w wTC2w

- wTP1TP1w

- wTP2TP2w

=

(1)

Q(w) =

where T signiﬁes the transpose of the matrix. Pi gives the training data matrix with sample points as rows and channels as columns. The spatial covariance matrix for a particular class i is Ci.

There are many ways to solve this optimisation problem but the optimisation technique used in this work is solved by initially visualising that the function Q(w) is unchanged, if the ﬁlter w is rescaled. In fact Q(kw) = Q(w), where k gives a real constant indicating the rescaling of ﬁlter w is arbitrary. Therefore, minimising Q(w) is comparable to minimising wTC1w subject to the constraint wTC2w = 1 as there is always a possible way to ﬁnd a rescaling factor of w such that wTC2w = 1. This constrained optimisation problem amounts to minimising the following function using the Lagrange multiplier method:

L(β,w) = wTC1w − β(wTC2w − 1) (2)

The derivative of L with regard to w is 0 and the ﬁlters w minimising L are such that :

∂L ∂w

= 2wTC1 − 2βwTC2 = 0 ⇐⇒ C1w = βC2w ⇐⇒ C2−1C1w = βw (3)

Now, this is a standard eigenvalue problem. Hence, the eigenvectors of Z = C2−1C1 are used to obtain the spatial ﬁlters minimising Eq. 1 corresponding to both the largest and the lowest eigenvalues. The features are extracted as the logarithm of EEG signal variance in the selected band after the projection of ﬁlters w using the CSP matrix [26].

### 3. Results and Discussion

Results are presented for classiﬁcation of right hand and foot MI tasks and compared with those from another group [26] who studied the same

classiﬁcation problem.

The calculated feature set was obtained by taking sf=3 after channel selection using the above described method helping to attain highly separable features for all subjects. As an example, Fig. 4 shows the box plot of feature separability (p < 0.05) for subject 5 in the training session using a ﬁve-fold cross validation scheme for right hand and foot MI tasks.

It should be noted that the correlation of 0.7 was identiﬁed after an initial investigation by using one of the channels C3, C4, or Cz as a reference resulting in our three proposed methods: Proposed method 1 (PM1) using C3 as a reference, proposed method 2 (PM2) using C4 as a reference, and proposed method 3 (PM3) using Cz as a reference. Although the correlation coeﬃcient was also computed between the range of 0.5 to 0.8, it was determined that the correlation value of 0.7 gave the best results without compromising the classiﬁcation accuracy (CA). The results obtained in the training session with ﬁve-fold cross-validation with correlation coeﬃcient(>0.7) started showing a decrease in CA except for one of the nine subjects with the proposed methods (PM1-C3 and PM2-C4) as shown in Table 3. For demonstration, the CA and channels selected have been shown in Table 3 and Table 4 respectively for correlation coeﬃcients from 0.5 to 0.8. The bold values show the threshold of 0.7 which gives optimum results without compromising the classiﬁcation ACC. See also Fig. 3 which shows cross-validation classiﬁcation ACC plotted against total channel number (CH) for each correlation coeﬃcient, i.e. 0.5, 0.6, 0.7, 0.8.

- Table 3: Classiﬁcation ACC in training session of proposed method with 5-fold cross validation. CC refers to correlation coeﬃcient.

|Subject|PM1-C3 (CC)<br><br>| | | |PM2-C4 (CC)| | | |PM3-Cz (CC)| | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |0.5<br><br>|0.6|0.7<br><br>|0.8<br><br>|0.5|0.6<br><br>|0.7<br><br>|0.8|0.5<br><br>|0.6<br><br>|0.7<br><br>|0.8|
|A01|90.45|90.52|90.46<br><br>|89.3|92.25<br><br>|92.28|91.07<br><br>|89.29<br><br>|89.88|89.93|89.27|89.29|
|A02<br><br>|96.92<br><br>|96.42|96.42|96.38<br><br>|96.92|96.42<br><br>|96.41<br><br>|95.47|96.47<br><br>|96.42|95.07<br><br>|90.98|
|A03<br><br>|71.22<br><br>|73.09<br><br>|68.1<br><br>|69.9|81.15|78.64<br><br>|75.18|70.17<br><br>|69.15<br><br>|68.17|61.99<br><br>|54.71|
|A04<br><br>|89.24|87.27<br><br>|91.06|87.42|98.18<br><br>|85.45<br><br>|94.55|91.06<br><br>|91.21|85.45<br><br>|87.58|91.21|
|A05<br><br>|100|100<br><br>|100|96.67<br><br>|96.67|92.67<br><br>|96.67|79.33|100<br><br>|100|100<br><br>|88.67|
|B01<br><br>|96.67<br><br>|96.67<br><br>|96.67|94.44|96.67<br><br>|96.67|97.78|86.67<br><br>|97.78|96.67|97.78<br><br>|95.56|
|B02<br><br>|100<br><br>|96.67|98.33|98.33<br><br>|100|98.33<br><br>|98.33<br><br>|98.33|100<br><br>|98.33|98.33<br><br>|96.67|
|B03<br><br>|98.33|96.67|98.33<br><br>|95<br><br>|98.33|96.67|95<br><br>|88.33<br><br>|98.33<br><br>|96.67<br><br>|98.33<br><br>|96.67|
|Average|92.85|92.16<br><br>|92.42|90.93<br><br>|95.02|92.14<br><br>|93.12|87.33<br><br>|92.85<br><br>|91.46<br><br>|91.04<br><br>|87.97|

#### Table 5 shows the accuracies of each subject A01-A05 and B01-B03 for the proposed methods PM1-PM3 along with the comparison method 4 with

- Table 4: Channels selected with the proposed method in training session with 5-fold cross validation. CC refers to correlation coeﬃcient.

|Subject<br><br>|PM1-C3 (CC)<br><br>| | | |PM2-C4 (CC)| | | |PM3-Cz (CC)| | | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |0.5<br><br>|0.6|0.7|0.8<br><br>|0.5<br><br>|0.6<br><br>|0.7<br><br>|0.8<br><br>|0.5|0.6|0.7<br><br>|0.8|
|A01|53<br><br>|51|48|40|54<br><br>|51<br><br>|50<br><br>|42|54<br><br>|52|49<br><br>|43|
|A02<br><br>|52|50<br><br>|44<br><br>|42<br><br>|55|50|48|43<br><br>|52|35<br><br>|23|9|
|A03|53|51<br><br>|47|39<br><br>|54<br><br>|52<br><br>|52|44|21|17|12<br><br>|5|
|A04|29<br><br>|23<br><br>|16<br><br>|11|84<br><br>|61|40<br><br>|17|58<br><br>|37|23<br><br>|12|
|A05|25<br><br>|22|13<br><br>|7|87<br><br>|66<br><br>|34|10|78|47<br><br>|28<br><br>|13|
|B01|55<br><br>|49<br><br>|39<br><br>|20<br><br>|59|46<br><br>|33|19|60<br><br>|53|44<br><br>|25|
|B02|60<br><br>|55|45|26<br><br>|60<br><br>|55<br><br>|48|28<br><br>|59<br><br>|50|44<br><br>|35|
|B03<br><br>|53|44<br><br>|34<br><br>|21|51<br><br>|35|21<br><br>|13|54<br><br>|49|43<br><br>|28|
|Average<br><br>|47.5|43.13<br><br>|35.75|25.75<br><br>|63<br><br>|52<br><br>|40.75|27<br><br>|54.5<br><br>|42.5<br><br>|33.25<br><br>|21.25|

[Figure 4]

- Figure 3: Cross-validation CA plotted against total CH for each correlation coeﬃcient value in the training session.

###### Extracted feature(x1) with sf=3 for right hand and foot MI tasks for Subject 5

CSPfeatures

- 0

- 0.5
- 1

1.5

2

- 2.5

- -1
- -0.5

x1: Right hand x1: Foot

- Figure 4: The box plot shows the extracted feature with sf=3 in the training session using ﬁve-fold cross validation for right hand and foot MI tasks.

- Table 5: Classiﬁcation ACC comparison of proposed methods (PM1, PM2, and PM3) with another research group for comparison (Comparison method 4 [26]) in the test session. Bold entries indicate highest classiﬁcation ACC.

|Subject<br><br>|PM1-C3| |PM2-C4<br><br>| |PM3-Cz| |Comparison method 4| |
|---|---|---|---|---|---|---|---|---|
| |Accuracy(%)<br><br>|Channels|Accuracy(%)<br><br>|Channels|Accuracy(%)<br><br>|Channels<br><br>|Accuracy(%)|Channels|
|A01<br><br>|75<br><br>|48<br><br>|65.18|50|75.89<br><br>|49|66.07<br><br>|118|
|A02<br><br>|98.21|44|98.21<br><br>|48|94.64<br><br>|23<br><br>|96.43|118|
|A03<br><br>|48.47|47|63.27<br><br>|52<br><br>|57.14|12<br><br>|47.45<br><br>|118|
|A04<br><br>|70.54|16<br><br>|77.23|40|75.89|23<br><br>|71.88<br><br>|118|
|A05<br><br>|80.56<br><br>|13|65.48<br><br>|34<br><br>|72.22|28|49.60<br><br>|118|
|B01<br><br>|96.67<br><br>|39|94.44|33<br><br>|96.67<br><br>|44<br><br>|95.56|60|
|B02<br><br>|61.67|45|61.67|48|61.67<br><br>|44<br><br>|61.67|60|
|B03|98.34<br><br>|34<br><br>|91.67<br><br>|21<br><br>|93.33|43|93.33<br><br>|60|
|Average<br><br>|78.68|35.75<br><br>|77.14|40.75<br><br>|78.43|33.25<br><br>|72.75<br><br>|96.25|

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

###### Figure 5: Channels selected for subject A01, subject A02 and subject A03 with channel C3 as a reference channel using PM1.

[Figure 17]

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

[Figure 28]

###### Figure 6: Channels selected for subject A01, subject A02 and subject A03 with channel C4 as a reference channel using PM2.

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

###### Figure 7: Channels selected for subject A01, subject A02 and subject A03 with channel Cz as a reference channel using PM3.

[Figure 41]

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

[Figure 51]

[Figure 52]

###### Figure 8: All 118 channels selected for subject A01, subject A02 and subject A03 using comparison method 4.

[Figure 53]

- Figure 9: Group CA of proposed methods (PM1-C3, PM2-C4, PM3-Cz) with another research group’s (Method 4) for comparison.

Fig. 9 displaying the average accuracy for each subject for comparison, a full description of which now follows.

Each of the three proposed methods, i.e. PM1, PM2, PM3, on average outperformed comparison method 4 whilst using a substantially reduced channel count. Across eight subjects PM1 shows an increased mean performance of >5% (p<0.08), with PM2 >4% (p<0.2), and PM3 >5% (p<0.09). The performance of each individual subject also improves on average over the three methods compared to the comparison method 4 [26].

- Subject A01, although showing a slight drop in ACC with PM2 (reduced

channels (RC) >50%) compared with Method 4, improved in accuracy in both PM1 (CA >8% and RC >59%) and PM3 (CA >9% and RC >58%). Subject A02 who scored highly in method 4 originally, improved marginally in both PM1 and PM2 (CA >1.5% and RC >62%) and (CA >1.5% and RC >53%), although dropped slightly in accuracy in PM3 (RC >80%). Subject A03 scored similarly to method 4 in PM1 improving by just over 1%, but improved in both PM2 (CA >15%) and PM3 (CA >9%) and an overall average in all three methods of CA >8%. Subject A04 improved in two of the three methods - PM1 (CA <1% and RC >86%), PM2 (CA >5% and RC >61%), and PM3 (CA >4% and RC >80%) with an average improvement of just over 2.6%. Although subject A02 showed little improvement on average

over three methods (CA >0.5%), interestingly, subject A05 shows the most improvement with PM1 (CA >30%), PM2 (CA >15%), and PM3 (>22%) and an improvement on average over all three methods of >23%.

- Subject B01 and B03 have improved by only ca >1% and ca >5% with

signiﬁcant reduction of rc >35% and rc >43% in the channels selected using the PM1 and PM3. Moreover, the same classiﬁcation was achieved with a reduced number of channels using PM1 (rc >25), PM2 (rc >52), and PM3 (rc >26).

With regards to channel reduction, PM2 uses <41 channels on average over all 8 subjects, representing <58% of the original 96.25 channels. PM1 gives a greater improvement with rc <36 channels, or <63% with PM2. PM3 demonstrates the greatest reduction in channel number on average over all subjects rc <65% of the original 96.25 channels.

Thus the PM1 and PM3 show comparable results in terms of average CA but with 35.75 and 33.25 average number of channels. Further analysis is required to determine why the reference taken from Cz produces the best outcomes in this case.

Figures 5 - 8 show the channels selected with PM1, PM2 and PM3, and comparison method 4 respectively in terms of electrode weights from a neurophysiological point of view. Fig. 5 depicts the diﬀerent regions of the brain where subject-speciﬁc channels are selected for subject A01, subject A02 and subject A03 with channel C3 as a reference channel denoted by PM1 in terms of electrode weight. Similarly, Figs. 6 and 7 show the brain region selected in terms of electrode weight when subject-speciﬁc channels are selected for subject A01, subject A02 and subject A03 with channel C4 and channel Cz as a reference channel denoted by PM2 and PM3 respectively. For comparison, Figure 8 shows all 118 channels selected for subject A01, subject A02 and subject A03 denoted by method 4 [26]. Hence, it is possible to visually inspect the location of the automatically selected subject-speciﬁc channels when examined alongside comparison method 4 and it is evident from the ﬁgures that there is a substantial channel reduction using the proposed methods.

To contrast, another research group [25] identiﬁed correlated channels using the Fisher score to select the channel set for MI classiﬁcation in the feature extraction step, and classiﬁed the selected features using the support vector machine (SVM) classiﬁer [30]. In our study, channel selection was performed in the pre-processing stage where pairwise correlation was computed using the Pearson correlation method taking C3, C4, or Cz as a reference

channel. This method is much simpler to understand and has the potential to be implemented for the online classiﬁcation of MI tasks in BCI systems.

It is interesting to note that two out of our three proposed methods have shown a lower variance in CA than the comparison method 4 making our method more robust across multiple datasets.

This paper’s ﬁndings demonstrate that it is possible to simultaneously reduce the number of channels whilst maintaining a suﬃcient (and in fact an increased) level of accuracy. The variation in the number and position of channels selected in each case highlights the inherent diﬀerences in the human brain and the subsequent diﬃculty involved in designing a MI BCI adding to the already challenging problem of non-stationarity present in the signals again highlighting the need for the technique presented within this paper.

It would be interesting to perform further analysis to ascertain whether correlation values to two decimal places would yield a higher CA whilst further reducing the number of necessary channels. Additionally, although on average a balance was struck between the correlation coeﬃcient value and the number of channels rejected, this correlation value was ﬁxed at 0.7 for all participants and it would be interesting to select a subject-speciﬁc correlation coeﬃcient as there were certainly diﬀerences in CA between participants.

A future study could, for example, use a method to search all permutations of the correlation coeﬃcient to a ﬁner degree of resolution to ﬁnd the optimal value whilst maintaining a set threshold CA level. Additionally, this dimensionality reduction has implications not only for the speed at which a dataset can be processed but also with regard the eﬃciency at which on online implementation of the system could be realised.

Ultimately, the techniques presented in this work could potentially lead to a fully automated and personalised BCI - one which is more adept at shaping to individual users’ cortical physiology and hence to the highly individualised brainwaves produced therein.

### 4. Conclusion

In this study, an automatic subject speciﬁc channel selection technique was proposed to select channels for a MI-based BCI. These channels are selected automatically based on correlations computed between one of C3, C4, or Cz as a reference and other EEG channels. The results were presented

using a correlation of 0.7, which demonstrates not only an improved overall CA but also a signiﬁcant reduction in the number of channels, due to the well-documented association with the sensorimotor areas. This study oﬀers two contributions to the research ﬁeld. Firstly, the number of channels were signiﬁcantly reduced using the proposed algorithms without compromising performance. This reduction in the number of channels makes it more suitable for the practical real-time application of BCI. Secondly, the idea of channel selection was introduced using the standard EEG channel distribution and an intelligent algorithm for automatic selection of channels for each subject. In future studies, a thorough analysis may reveal better selection criteria which should allow for a further reduction in channels whilst maintaining CA.

### References

- [1] J. R. Wolpaw, D. J. McFarland, G. W. Neat, C. A. Forneris, An EEGbased brain-computer interface for cursor control, Electroencephalography and clinical neurophysiology 78 (3) (1991) 252–259.
- [2] J. Wolpaw, E. W. Wolpaw, Brain-computer interfaces: principles and practice, OUP USA, 2012.
- [3] H. Yuan, B. He, Brain–computer interfaces using sensorimotor rhythms: current state and future perspectives, IEEE Transactions on Biomedical Engineering 61 (5) (2014) 1425–1435.
- [4] B. He, B. Baxter, B. J. Edelman, C. C. Cline, W. Y. Wenjing, Noninvasive brain-computer interfaces based on sensorimotor rhythms, Proceedings of the IEEE 103 (6) (2015) 907–925.
- [5] M. Arvaneh, C. Guan, K. K. Ang, C. Quek, Optimizing the channel selection and classiﬁcation accuracy in EEG-based BCI, IEEE Transactions on Biomedical Engineering 58 (6) (2011) 1865–1873.
- [6] F. Popescu, S. Fazli, Y. Badower, B. Blankertz, K.-R. Mu¨ller, Single trial classiﬁcation of motor imagination using 6 dry EEG electrodes, PloS one 2 (7) (2007) e637.

- [7] P. Gaur, R. B. Pachori, H. Wang, G. Prasad, A multi-class EEGbased BCI classiﬁcation using multivariate empirical mode decomposition based ﬁltering and Riemannian geometry, Expert Systems with Applications 95 (2018) 201–211.
- [8] P. Gaur, R. B. Pachori, H. Wang, G. Prasad, An empirical mode decomposition based ﬁltering method for classiﬁcation of motor-imagery EEG signals for enhancing brain-computer interface, in: Neural Networks (IJCNN), 2015 International Joint Conference on, IEEE, 2015, pp. 1–7.
- [9] P. Gaur, R. B. Pachori, H. Wang, G. Prasad, A multivariate empirical mode decomposition based ﬁltering for subject independent BCI, in: Signals and Systems Conference (ISSC), 2016 27th Irish, IEEE, 2016, pp. 1–7.
- [10] P. Gaur, R. B. Pachori, H. Wang, G. Prasad, An Automatic Subject Speciﬁc Intrinsic Mode Function Selection for Enhancing Two-Class EEG based Motor Imagery-Brain Computer Interface, IEEE Sensors Journal.
- [11] V. Gandhi, G. Prasad, D. Coyle, L. Behera, T. M. McGinnity, Evaluating Quantum Neural Network ﬁltered motor imagery brain-computer interface using multiple classiﬁcation techniques, Neurocomputing 170

(2015) 161–167.

- [12] H. Ramoser, J. Muller-Gerking, G. Pfurtscheller, Optimal spatial ﬁltering of single trial EEG during imagined hand movement, IEEE transactions on rehabilitation engineering 8 (4) (2000) 441–446.
- [13] L. He, Z. Yu, Z. Gu, Y. Li, Bhattacharyya bound based channel selection for classiﬁcation of motor imageries in EEG signals, in: 2009 Chinese Control and Decision Conference, IEEE, 2009, pp. 2353–2356.
- [14] Y. Wang, S. Gao, X. Gao, Common spatial pattern method for channel selelction in motor imagery based brain-computer interface, in: 2005 IEEE Engineering in Medicine and Biology 27th Annual Conference, IEEE, 2006, pp. 5392–5395.
- [15] Y. Yang, O. Kyrgyzov, J. Wiart, I. Bloch, Subject-speciﬁc channel selection for classiﬁcation of motor imagery electroencephalographic data,

- in: 2013 IEEE International Conference on Acoustics, Speech and Signal Processing, IEEE, 2013, pp. 1277–1280.
- [16] J. Yang, H. Singh, E. L. Hines, F. Schlaghecken, D. D. Iliescu, M. S. Leeson, N. G. Stocks, Channel selection and classiﬁcation of electroencephalogram signals: an artiﬁcial neural network and genetic algorithmbased approach, Artiﬁcial intelligence in medicine 55 (2) (2012) 117–126.
- [17] P. Gaur, R. B. Pachori, H. Wang, G. Prasad, Enhanced motor imagery classiﬁcation in EEG-BCI using multivariate EMD based ﬁltering and CSP features, in: International Brain-Computer Interface (BCI) Meeting 2016, 2016.
- [18] P. Gaur, K. McCreadie, R. B. Pachori, H. Wang, G. Prasad, Tangent Space Features-Based Transfer Learning Classiﬁcation Model for TwoClass Motor Imagery Brain–Computer Interface, International Journal of Neural Systems 29 (10) (2019) 1950025.
- [19] T. Alotaiby, F. E. A. El-Samie, S. A. Alshebeili, I. Ahmad, A review of channel selection algorithms for EEG signal processing, EURASIP Journal on Advances in Signal Processing 2015 (1) (2015) 66.
- [20] M. Z. Baig, N. Aslam, H. P. H. Shum, Filtering techniques for channel selection in motor imagery EEG applications: a survey, Artiﬁcial Intelligence Review 53 (2) (2020) 1207–1232.
- [21] J. K. Feng, J. Jin, I. Daly, J. Zhou, Y. Niu, X. Wang, A. Cichocki, An optimized channel selection method based on multifrequency CSP-rank for motor imagery-based BCI system, Computational Intelligence and Neuroscience 2019.
- [22] K. Belwaﬁ, O. Romain, S. Gannouni, F. Ghaﬀari, R. Djemal, B. Ouni, An embedded implementation based on adaptive ﬁlter bank for brain– computer interface systems, Journal of neuroscience methods 305 (2018) 1–16.
- [23] Y. Park, W. Chung, Frequency-optimized local region common spatial pattern approach for motor imagery classiﬁcation, IEEE Transactions on Neural Systems and Rehabilitation Engineering 27 (7) (2019) 1378– 1388.

- [24] S. Roy, D. Rathee, A. Chowdhury, K. McCreadie, G. Prasad, Assessing impact of channel selection on decoding of motor and cognitive imagery from MEG data, Journal of Neural Engineering 17 (5) (2020) 056037.
- [25] Y. Park, W. Chung, Optimal Channel Selection Using Correlation Coefﬁcient for CSP Based EEG Classiﬁcation, IEEE Access 8 (2020) 111514– 111521.
- [26] F. Lotte, C. Guan, Regularizing common spatial patterns to improve BCI designs: uniﬁed theory and new algorithms, IEEE Transactions on biomedical Engineering 58 (2) (2011) 355–362.
- [27] B. Blankertz, K.-R. Muller, D. J. Krusienski, G. Schalk, J. R. Wolpaw, A. Schlogl, G. Pfurtscheller, J. R. Millan, M. Schroder, N. Birbaumer, The BCI competition III: Validating alternative approaches to actual BCI problems, IEEE transactions on neural systems and rehabilitation engineering 14 (2) (2006) 153–159.
- [28] B. Blankertz, R. Tomioka, S. Lemm, M. Kawanabe, K.-R. Muller, Optimizing spatial ﬁlters for robust EEG single-trial analysis, IEEE Signal processing magazine 25 (1) (2008) 41–56.
- [29] F. Lotte, M. Congedo, A. Le´cuyer, F. Lamarche, B. Arnaldi, A review of classiﬁcation algorithms for EEG-based brain–computer interfaces, Journal of neural engineering 4 (2) (2007) R1.
- [30] J. Ye, T. Xiong, SVM versus least squares SVM, in: Artiﬁcial intelligence and statistics, 2007, pp. 644–651.

