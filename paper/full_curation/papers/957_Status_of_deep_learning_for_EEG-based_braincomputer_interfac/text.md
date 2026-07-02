TYPE Review
PUBLISHED 16 January 2023
DOI 10.3389/fncom.2022.1006763
OPEN ACCESS
EDITED BY
Md. Kaﬁul Islam,
Independent University, Bangladesh
REVIEWED BY
Shinji Kawakura,
Osaka City University, Japan
Amir Rastegarnia,
Malayer University, Iran
*CORRESPONDENCE
Md Atiqur Rahman Ahad
mahad@uel.ac.uk
RECEIVED 29 July 2022
ACCEPTED 23 December 2022
PUBLISHED 16 January 2023
CITATION
Hossain KM, Islam MA, Hossain S, Nijholt A and
Ahad MAR (2023) Status of deep learning for
EEG-based brain–computer interface
applications.
Front. Comput. Neurosci. 16:1006763.
doi: 10.3389/fncom.2022.1006763
COPYRIGHT
© 2023 Hossain, Islam, Hossain, Nijholt and
Ahad. This is an open-access article distributed
under the terms of the Creative Commons
Attribution License (CC BY). The use,
distribution or reproduction in other forums is
permitted, provided the original author(s) and
the copyright owner(s) are credited and that
the original publication in this journal is cited, in
accordance with accepted academic practice.
No use, distribution or reproduction is
permitted which does not comply with these
terms.
Status of deep learning for
EEG-based brain–computer
interface applications
Khondoker Murad Hossain1, Md. Ariful Islam2, Shahera Hossain3,
Anton Nijholt4 and Md Atiqur Rahman Ahad5*
1Department of Computer Science and Electrical Engineering, University of Maryland Baltimore County,
Baltimore, MD, United States, 2Department of Robotics and Mechatronics Engineering, University of Dhaka,
Dhaka, Bangladesh, 3Kyushu Institute of Technology, Kitakyushu, Japan, 4Human Media Interaction,
University of Twente, Enschede, Netherlands, 5Department of Computer Science and Digital Technology,
University of East London, London, United Kingdom
In the previous decade, breakthroughs in the central nervous system bioinformatics
and
computational
innovation
have
prompted
signiﬁcant
developments
in
brain–computer interface (BCI), elevating it to the forefront of applied science
and research. BCI revitalization enables neurorehabilitation strategies for physically
disabled patients (e.g., disabled patients and hemiplegia) and patients with brain
injury (e.g., patients with stroke). Diﬀerent methods have been developed for
electroencephalogram (EEG)-based BCI applications. Due to the lack of a large
set of EEG data, methods using matrix factorization and machine learning were
the most popular. However, things have changed recently because a number of
large, high-quality EEG datasets are now being made public and used in deep
learning-based BCI applications. On the other hand, deep learning is demonstrating
great prospects for solving complex relevant tasks such as motor imagery
classiﬁcation, epileptic seizure detection, and driver attention recognition using
EEG data. Researchers are doing a lot of work on deep learning-based approaches in
the BCI ﬁeld right now. Moreover, there is a great demand for a study that emphasizes
only deep learning models for EEG-based BCI applications. Therefore, we introduce
this study to the recent proposed deep learning-based approaches in BCI using
EEG data
(from 2017 to 2022). The main diﬀerences, such as merits, drawbacks,
and applications are introduced. Furthermore, we point out current challenges and
the directions for future studies. We argue that this review study will help the EEG
research community in their future research.
KEYWORDS
deep learning, EEG, BCI, future challenge, convolutional neural network (CNN)
1. Introduction
BCI is a method that uses psychology, electronics, computers, neuroscience, signal
processing, and pattern recognition to work together. It is used to generate various control
signals or commands from recorded brain signals of neural responses in order to determine the
intentions of the medically challenged subject to perform a motor action to restore a quality
of life. In a nutshell, the BCI turns the neural responses of the human brain into control
signals or commands that can be used to control things such as prosthetic limbs, walking,
neurorehabilitation, and movement. It is also used to assist medically challenged people with
severe motor disorders, as well as healthy people, in their daily activities.
A generic BCI system (Schalk et al., 2004; Hassanien and Azar, 2015) comprises: (i)
electrodes to obtain electrophysiological scheme patterns from a human subject; (ii) signal
acquisition devices to record the neural responses of the subject’s brain scheme; (iii) feature
extraction to generate the discriminative nature of brain signals to decrease the size of data
Frontiers in Computational Neuroscience
01
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
needed to classify the neural scheme; (iv) a translation algorithm
to generate operative control signals; (v) a control interface to
convert into output device commands; and (vi) a feedback system to
guide the subject to reﬁne speciﬁc neural activity to ensure a better
control mechanism.
On the other hand, there are two types of signal acquisition
methods to trace neural activity, namely invasive and non-invasive
methods (Schalk et al., 2004). A generic EEG-based BCI architecture
is shown in Figure 1. Microelectrodes are neurosurgically implanted
to the entire surface of the cerebral cortex or over the entire surface
of the cerebrum under the scalp in an invasive method (Abdulkader
et al., 2015). Even though this method gives high-resolution neural
signals, it is not the best way to record neural activity from a human
brain because it can cause scar tissue and infections.
In that case, the non-invasive method is preferred due to its
ﬂexibility and reduced risk. There are many techniques (Lotte
et al., 2018) by which the neural activity is recorded, such as
magnetoencephalography (MEG), functional magnetic resonance
imaging (fMRI) (Acar et al., 2022; Hossain et al., 2022), and
electroencephalography (EEG), and fully functioning near-infrared
spectroscopy (fNIRS). The EEG method is preferred due to its
robustness and user-friendly approach (Bi et al., 2013).
Artiﬁcial intelligence (AI) refers to systems or computers that
imitate human intelligence to carry out tasks and can (iteratively)
improve themselves depending on the information that they acquire.
AI can take several forms, including machine learning and deep
learning. Machine learning refers to the form of AI that can
automatically adapt with only minimal intervention from humans.
On the other hand, deep learning is a subset of machine learning
that learns with large data by exploiting more neural network layers
than classical machine learning schemes. There are several reviews
on EEG-based BCI using signal processing and machine learning
(Craik et al., 2019; Al-Saegh et al., 2021; Alzahab et al., 2021; Rahman
et al., 2021; Wang and Wang, 2021). Nevertheless, machine learning
reviews consist of a small part of deep learning modalities, so no
FIGURE 1
A generic brain–computer interface system.
review has focused exclusively on deep learning. One of the best
things about deep learning is that it can do feature engineering on its
own. In this method, the data are combed through by an algorithm
that searches for features that correlate with one another, and then
combines those features to facilitate faster learning without any
explicit instructions. A comprehensive review is much anticipated
as deep learning is the state-of-the-art classiﬁcation pipeline. In this
review, we report the most recent deep learning-based BCI research
studies for the last 6 years. Figure 2 shows the PRISMA ﬂow diagram
of our literature review process.
We used PubMed, ERIC, JSTOR, IEEE Xplore, and Google
Scholar as the electronic databases to get and retrieve the articles.
As our goal is to include studies that relate to the three keywords:
EEG data, BCI applications, and deep learning, we looked for
studies that included all three keywords. From the 245 studies,
we removed 31 as they were either fully duplicated or subversions
of other articles. After screening the remaining 214 papers, we
excluded 57 because they used deep learning only for related
works or as only a part of the full pipeline, resulting in 157
studies. But we could not fully retrieve 34 studies out of 157,
and this ﬁltering gives us 123 articles, of which ﬁve do not have
a clear dataset description, and the tasks of eight studies are
irrelevant to our review. Finally, we explored
110 articles for
this review.
To show how important this review is, we compare it to review
that have been done recently in Table 1. As the comparison criteria,
we have selected the coverage of the studies, the number of studies
that are included in the review, the presence of dataset-speciﬁc studies
in the review, whether the review is BCI application-speciﬁc, having
future recommendations for the researchers, and whether the review
is based only on deep learning. This study is the most recent study,
which covers the articles until late 2022 and comprises the highest
number of studies for the past 6 years. There has been no other
review study that has done dataset-speciﬁc ﬁltration of EEG-based
BCI research, whereas we show the number of studies and results for
Frontiers in Computational Neuroscience
02
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
FIGURE 2
PRISMA ﬂow diagram of the literature review process for studies on deep learning-based EEG-based BCI.
TABLE 1 Comparison between previous review works and our proposed review study.
References
Coverage
No. of
studies
Dataset speciﬁc
studies
Only BCI
application?
Deep learning
speciﬁc
Future
recommendation
Cao (2020)
2017–2020
Unspeciﬁed
No
Yes
No
No
Abiri et al. (2019)
1991–2017
Unspeciﬁed
No
Yes
No
No
Rahman et al. (2021)
2009–2021
54
No
No
No
Yes
Craik et al. (2019)
2014–2018
90
No
No
Yes
No
Alzahab et al. (2021)
2015–2020
47
No
Yes
Yes (hybrid deep
learning)
No
Al-Saegh et al. (2021)
2016–2020
40
No
No
Yes
No
Wang and Wang (2021)
2016–2020
Unspeciﬁed
No
Yes
No
No
Our study
2017–2022
110
Yes
Yes
Yes
Yes
each dataset separately. Furthermore, with a rich tabular comparison
between the two works, we only consider the EEG data classiﬁcation
for BCI application-speciﬁc. Finally, we only concentrate on the deep
learning algorithms for the EEG classiﬁcation in contrast to most of
the reviews.
The study is organized as follows: After the introduction in
Section 1, we introduce the core elements of EEG-based BCI in
Section 2. Section 3 includes the classical methods, which have
been exploited for EEG-based BCI tasks. Then, we analyzed the
implementation of deep learning and related parts of this domain
Frontiers in Computational Neuroscience
03
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
FIGURE 3
An architecture of BCI based on EEG data.
in Section 4. Sections 5, 6 are the discussion and conclusion of this
article, respectively.
2. EEG-based BCI preliminaries
To translate mortal objectives or aspirations into real-time
equipment control signals, the cognitive responses of humans are
related to the physical world. In Figure 3, we depict the usage of
EEG data in BCI applications. Electrophysiological activity patterns
of human subjects are recorded by the acquisition device. Scalp
electrodes are mounted over the headset to capture the neural
responses of human subjects (Sakkalis, 2011). Furthermore, a pre-
ampliﬁer is used to make the brain signals stronger, and then the
signal that has been strengthened is sent through a ﬁlter to get
rid of unwanted parts, noise, or interference. After that, an analog-
to-digital converter (ADC) converts the ﬁltered analog signal to a
digital signal. The electrical activities that had been recorded were
then standardized to improve the signal-to-noise ratio (SNR) of the
digital signal.
It is important to note that feature extraction gives you the things
that neural activity cannot do. This means that you need less data to
put the neural strategy into a category. Then, the data or information
is put into a speciﬁc group or category of brain patterns. After this
stage, the retrieved feature set is transformed into operational control
signals. The control signals made in the previous step are used to
control the external interface device. Thus, the BCI applications can
be controlled by these command signals.
3. Classical methods for EEG-based BCI
applications
EEG is by far the most prevalent strategy due to its high eﬃciency
and usability (Schalk et al., 2004). Be that as it may, pattern-based
control utilizing EEG signals is troublesome due to being exceedingly
boisterous and containing numerous exceptions. The human neural
impulses acquired from a BCI based on EEG include noise and other
attributes in addition to the signal of neural activity. The challenges
are getting rid of noise, trying to pull out relevant characteristics, and
accurately classifying the signal. By translating the extracted feature
set to give it a proper class label, operational commands can be
made. There are two categories of classiﬁcation algorithms: linear and
non-linear classiﬁers (Guger et al., 2021).
The goal of quantitative classiﬁcation is to ﬁgure out an object’s
system of classiﬁcation based on how it looks. To recognize distinct
types of brain activity, linear classiﬁers subscribe to the regime
of trying to establish a linear relationship/function between both
the dependent and independent variables of a classiﬁcation method
(Schalk et al., 2004). This set of classiﬁers involves linear discriminant
analysis (LDA) and support vector machines (Wang et al., 2009).
It sets up a hyperplane, which is a linear numerical operation that
separates the diﬀerent functions of the brain from the disentangled
collection of characteristics.
Because of its simple, strong, and non-overﬁt operation and
computing needs, the LDA, presuming the Gaussian distribution
of data, has been implemented in several BCI platforms (Wang
et al., 2009). Support Vector Machine (SVM) is a type of artiﬁcial
intelligence that can be used for both regression and classiﬁcation
(Wang et al., 2009). Even though we mention regression issues, it is
best suited for classiﬁcation. The primary goal of the SVM algorithm
is to track down a hyperplane in an N-dimensional space that
evidently summarizes the data points. When no algorithmic solution
can be found between the dependent and independent variables of
the classiﬁcation method, nonlinear classiﬁers are now used. Artiﬁcial
neural networks (ANNs), k-nearest neighbor (KNN), and SVMs are
some of these machine learning approaches (Lotte et al., 2018; Akhter
et al., 2020; Islam et al., 2020).
The ANNs are broadly utilized in an assortment of classiﬁcation
and design acknowledgment assignments as they can memorize from
preparing tests, and, in this way, classify the input tests in a like
manner. These are the most broadly utilized ANNs for eﬃcaciously
Frontiers in Computational Neuroscience
04
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
characterizing multiclass neurological actions. They operate on the
basis of conducting a preparatory calculation to adjust the weights
pertaining to speciﬁc input and hidden layer neurons to minimize
the violent square error (Wang et al., 2009).
Herman et al. (2008) conducted a classiﬁcation of EEG-based
BCI by investigating the type-2 fuzzy logic approach. They claimed
that their model exhibited better classiﬁcation accuracy than the
type-1 model of fuzzy logic. They also compared this method with
a well-known classiﬁer based on LDA. On the other hand, Aznan
and Yang (2013) applied the Kalman ﬁlter to an EEG-based BCI
for recognizing motor visuals in an attempt to optimize the system’s
accuracy and consistency.
The quintessential dispersion (CSP) was used to collect the
necessary information, and the radial basis function (RBF) was
used to categorize the signal. They also compared their results with
the LDA method and claimed that their RBF method showed a
better result.
Zhang H. et al. (2013) linked Bayes classiﬁcation error to spatial
ﬁltering, which is an important tool to extract and classify the EEG
signal. They claimed that by validating the positive relationship
between the Bayes error and the Rayleigh quotient, a spatial ﬁlter with
a lower Rayleigh quotient measuring the ratio of power features could
reduce the Bayes error. Zhang R. et al. (2013) proposed z-score LDA,
an updated version of LDA that introduces a new decision boundary
capable of eﬀectively handling heteroscedastic class distribution-
related classiﬁcation.
Agrawal and Bajaj (2020) proposed a brain state signal measuring
method based on non-muscular channel EEG to record the brain
activity acting as a source to facilitate communication between a
patient and the outside environment. They used fast and short-term
Fourier transforms to decompose the signals obtained from neural
activity into smaller segments. They implemented the classiﬁcation
tasks using a support vector machine. Depending on the values of
the evaluation grades, the overall accuracy of the system was found
to be approximately 92%. Pan et al. (2016) suggested a framework
for a sentiment state detection system based on EEG-based BCI
technology. They categorized two emotional responses, including
happiness and sadness, using SVM. According to their observations,
roughly 74.17% precision was noticed for such two classes.
Bousseta et al. (2018) proposed a BCI system based on EEG
to control a robot arm by decoding the disabled person’s thoughts
obtained from the brain. They combined the principal component
analysis with the fast Fourier transform to perform the feature
extraction and then fed it to the radial basis function-based support
vector machine as a classiﬁer. The outputs of this classiﬁer were
turned into commands that the robot arm followed.
Amarasinghe et al. (2014) proposed a method consisting of three
steps based on self-organizing maps to recognize neural activities
for unsupervised clustering. They identiﬁed two thought patterns,
such as moving forward and resting. They also implemented the
classiﬁcation process based on feed-forward ANNs. They claimed
that their mapping methods showed approximately 8% improvement
over ANN-based classiﬁcation.
Korovesis et al. (2019) established an electroencephalography
BCI system that controls the movement of a mobile robot in response
to the eye blinking of a human operator. They used the EEG signals
of brain activity to ﬁnd the right features and then fed those features
into a well-trained neural network to guide the mobile robot. They
achieved an accuracy of 92.1%. Sulaiman et al. (2011) extracted
distinguishing features for human stress from EEG-based BCI neural
activity. They combined the power spectrum ratio of EEG and
spectral centroid techniques to enhance the accuracy (88.89%) of the
k-nearest neighbor (kNN) classiﬁer, detecting and classifying human
stress in two states, such as close-eye and open-eye.
Wang et al. (2009) conducted a review of various classiﬁcation
approaches for motor imagery (BCI competition III) and ﬁnger
movement (BCI competition IV) on EEG signals. They compared the
results in terms of the accuracy of the classiﬁcation. Gaussian SVM
(GSVM) and k-NN show the desired performance because these
types of classiﬁcation are more vigorous than nonlinear classiﬁers,
as shown in Figure 4. However, learning vector quantization neural
networks (LVQNN) and quadratic discriminant analysis (QDA)
demonstrate the lowest accuracy. In addition, the performances
of linear discriminant analysis (LDA) and linear SVM are almost
identical. These demonstrate that the classical machine learning
methods are not yet optimal for this domain. Therefore, we need
to try out deep learning methods on large datasets in EEG-based
BCI applications.
4. Utilizing deep learning in EEG-based
BCI
Table 2 lists all the EEG-based BCI studies using deep learning
for the last 6 years. We have listed the ﬁve most important parts
of the studies: datasets, number of subjects, deep learning mode,
BCI application, and classiﬁcation result. This table will assist future
researchers in determining the state of the art in this domain.
4.1. Data preprocessing
Due to the presence of artifacts and contamination, EEG data
arestill not being used for large-scale BCI studies (Pedroni et al.,
2019). Even though some deep learning studies for EEG-based
BCI say they did not use any preprocessing steps, most of the
time, preprocessing steps are very important. Some research works
combine the preprocessing steps in their deep learning pipeline and
call it as end-to-end framework (Antoniades et al., 2018; Aznan et al.,
2018; Zhang et al., 2021). Moreover, an additional CNN layer has been
used for the preprocessing in some cases (Amin et al., 2019a; Tang
et al., 2019).
Most of the time, frequency domain ﬁlters were used in research
to limit the bandwidth of the EEG signal. This is useful when there is
a speciﬁc frequency range of interest so that the rest can be safely
ignored (Islam et al., 2016; Kilicarslan et al., 2016). In 30% of the
studies, a signal below 45 Hz, or below a typical low gamma band, was
low-pass ﬁltered. The ﬁltered frequency ranges were grouped by task
type and artifact reduction methods. It shows that most research used
a technique to get rid of artifacts along with lowering the frequency
ranges that were studied.
From our observation, 20% of the studies manually eliminated
artifacts (Rammy et al., 2020; Atilla and Alimardani, 2021;
Sundaresan et al., 2021). It is easy to see unexpected outliers visually,
such as when data are missing or signiﬁcant EEG artifacts are
evident. But it might be hard to tell the diﬀerence between noisy
Frontiers in Computational Neuroscience
05
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
FIGURE 4
Classiﬁcation algorithms and the corresponding accuracies of diﬀerent classical classiﬁcation methods based on a study.
channels that are always on and noisy channels that are only noisy
sometimes. Furthermore, since the way the data are processed is very
random, it is hard for other researchers to copy the methods. In
addition to this, 10% of the studies did not routinely eliminate EEG
artifacts. Independent component analysis (ICA) (Delorme et al.,
2007) and discrete wavelet transformation (DWT) were the most
common artifact removal methods that were utilized in the remaining
two-thirds of the analyzed research (Kline et al., 2015).
The EEG electrodes also take up undesired electrical physiological
signals from eye blinks and neck muscles (Crespo-Garcia et al.,
2008; Amin et al., 2019b). Additionally, there are issues with motion
artifacts brought on by cable motion and electrode displacement
while the individual is moving (Arnau-González et al., 2017; Chen
et al., 2019a; Gao et al., 2019). There have been a lot of studies
performed on how to ﬁnd and remove EEG artifacts (Nathan and
Contreras-Vidal, 2016), but it is not the primary focus of our review
work. In summary, one of the three methods (i.e., manual process,
automated process, or no removal of artifact) is considered in each
study to conduct the artifact removal procedure.
4.2. Datasets
One of the main limitations of the classical EEG-based BCI is
the number of subjects who participated in this study. Within the
course of this review, EEG-based datasets were covered. This scope
was taken into account as keywords to ﬁnd the right research articles
on the Google Scholar and Research Gate websites. For this literature
review, more than 100 research studies were found on these two
websites by using the above criteria. Among these, around 47% of
research has been conducted based on the BCI competition dataset.
Moreover, 9%, 16%, and 7% of the studies have been conducted on
DRYAD, SEED-VIG, and EEG MI datasets, respectively (Figure 5).
Deep learning has enabled larger datasets and more rigorous
experiments in BCI. “How much data is enough data?” remains a
signiﬁcant question when using DL with EEG data. We looked at
numerous descriptive dimensions to investigate this question: the
number of participants, the amount of EEG data collected, and the
task of the datasets. There are few studies that make use of their own
collected datasets (Tang et al., 2017; Vilamala et al., 2017; Antoniades
et al., 2018; Aznan et al., 2018; Behncke et al., 2018; El-Fiqi et al., 2018;
Nguyen and Chung, 2018; Alazrai et al., 2019; Chen et al., 2019b;
Fahimi et al., 2019; Hussein et al., 2019; Zgallai et al., 2019; Gao
et al., 2020b; León et al., 2020; Maiorana, 2020; Penchina et al., 2020;
Tortora et al., 2020; Atilla and Alimardani, 2021; Cai et al., 2021; Cho
et al., 2021; Mai et al., 2021; Mammone et al., 2021; Petoku and Capi,
2021; Reddy et al., 2021; Shoeibi et al., 2021; Sundaresan et al., 2021;
Ak et al., 2022). However, most of the deep learning studies have been
conducted based on publicly available EEG datasets, such as:
• The dataset used to validate the classiﬁcation method and signal
processing for brain–computer interfaces was obtained from the
BCI competition (Tabar and Halici, 2016; Amin et al., 2019b;
Dai et al., 2019; Olivas-Padilla and Chacon-Murguia, 2019; Qiao
and Bi, 2019; Roy et al., 2019; Song et al., 2019; Tang et al.,
2019; Tayeb et al., 2019; Zhao et al., 2019; Li Y. et al., 2020;
Miao et al., 2020; Polat and Özerdem, 2020; Rammy et al., 2020;
Yang et al., 2020; Deng et al., 2021; Huang et al., 2021, 2022;
Tiwari et al., 2021; Zhang et al., 2021). This dataset comprises
EEG data obtained from participants. Class 1 was the left hand,
Class 2 was the dominant hand, Class 3 was both feet, and
Class 4 was the tongue in the cue-based BCI structure. For
each subject, two workouts were captured on interspersing time
frames. Each session consisted of six runs separated by relatively
short pauses. A phase includes 288 eﬀorts, with each eﬀort being
implemented 48 times.
• DRYAD dataset contains ﬁve studies that investigate natural
speech understanding using a diversity of activities along with
acoustic, cinematic, and envisioned verbal sensations (Amber
et al., 2019).
• CHB-MIT dataset contains EEG recordings from children who
have intractable seizures (Dang et al., 2021). After people
stopped taking their seizure medicine, they were watched for up
Frontiers in Computational Neuroscience
06
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
TABLE 2 EEG-based BCI studies using deep learning for the last 6 years.
References
Dataset (No. of subjects)
Deep learning
modality
Application
Classiﬁcation
result
EEG-based BCI with deep learning
Tang et al. (2017)
2 able-body subjects (2)
CNN
Classifying left hand and right hand
movement
86.41%
Aznan et al. (2018)
4 subjects (4)
CNN
Classifying SSVEP frequencies
96.00%
Dose et al. (2018)
Physionet EEG MI Dataset (109)
CNN
Stroke rehabilitation
80.38%
El-Fiqi et al. (2018)
2 datasets (5 and 12)
CNN
Person identiﬁcation
96.80%
Amber et al. (2019)
DRYAD (30)
CNN
Lie detection
99.60%
Nguyen and Chung (2018)
8 healthy subjects (8)
CNN
Developing a speller system
99.20%
Shoeibi et al. (2021)
21 patients with focal epilepsy (21)
CNN, LSTM
Diagnosing epileptic seizures
99.10% (CNN),
100% (LSTM)
Antoniades et al. (2018)
17 subjects (17)
CNN
Detecting epileptic discharges
68.00%
Völker et al. (2018)
Flanker task dataset (31)
CNN
Decoding error
81.70%
Behncke et al. (2018)
5 males and 6 females (11)
CNN
Decoding robot errors
75.00%
Oh et al. (2020)
20 Parkinson patients (20)
CNN
Identifying Parkinson Disease
88.25%
Zeng et al. (2018)
10 healthy subjects (10)
LSTM
Predicting mental states of drivers
91.79%
Hussein et al. (2019)
BCI (7)
LSTM
Detecting epileptic seizures
100%
Vilamala et al. (2017)
10 males and 10 females (20)
CNN
Scoring sleep stage
89–97%
Tabar and Halici (2016)
BCI competition IV dataset 2b (9)
CNN+SAE
Classifying right and left hand
movement
72.40%
Olivas-Padilla and
Chacon-Murguia (2019)
BCI competition IV dataset 2a (9)
CNN
Classifying MI
67.50% - 82.09%
Tayeb et al. (2019)
BCI competition IV dataset 2b (9)
CNN
Decoding MI movements
77.72%
Sundaresan et al. (2021)
8 with autism and 5 healthy subjects (13)
CNN+RNN
Classifying mental stress with autism
93.27%
Cai et al. (2021)
26 healthy subjects (26)
CNN
Classifying attentive state
72.73%
Ieracitano et al. (2021)
15 subjects (15)
CNN
Discriminating hand motion planning
76.21%
Reddy et al. (2021)
27 subjects (27)
CNN
Detecting drowsiness
85.42%
Petoku and Capi (2021)
462 trials of a single subject (1)
CNN
Detecting object movement
60.00%
Zhang et al. (2021)
BCI Competition IV dataset 2a and 2b (18)
CNN
Classifying MI
88.40%
Mai et al. (2021)
4 males and 2 females (6)
CNN
Detecting emotional states
93.34%
Deng et al. (2021)
BCI Competition IV 2a, III (12)
CNN
Classifying MI tasks
85.30%
Huang et al. (2022)
PhysioNet dataset (109)
CNN
Classifying MI
92.00%
Cho et al. (2021)
12 subjects (12)
Bi-LSTM
Classifying MI task
68.00%
Atilla and Alimardani (2021)
14 subjects while driving (14)
CNN
Classifying drivers attention
89.00%
Mammone et al. (2021)
15 participants (15)
CNN
Decoding motion planning
90.77%
Ak et al. (2022)
5 subjects (5)
CNN
Controlling robot manipulator
90.00%
Huang et al. (2021)
BCI competition IV dataset 2a (9)
CNN
Classifying MI
90.00%
Aldayel et al. (2020)
DEAP (32)
CNN
Classifying preference in
neuromarketing
94.00%
León et al. (2020)
10 subjects (10)
CNN, RNN
Classifying SSMVEP signals
96.83%
Miao et al. (2020)
BCI competition IVa (5), right index ﬁnger
MI dataset (10)
CNN
Classifying MI
90.00%
Ko et al. (2020)
SEED-VIG dataset (15)
CNN
Estimating driver vigilance
96.00%
Penchina et al. (2020)
11 subjects (11)
RNN, LSTM
Classifying anxiety in adolescents with
autism
93.27%
Tortora et al. (2020)
11 healthy subjects walking on a
treadmill (8)
LSTM
Decoding gait
AUC=90%
(Continued)
Frontiers in Computational Neuroscience
07
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
TABLE 2 (Continued)
References
Dataset (No. of subjects)
Deep learning
modality
Application
Classiﬁcation
result
Rammy et al. (2020)
BCI Competition IV dataset 2a (9)
LSTM
Recognizing motor imagination
Mean kappa: 0.64
Liu J. et al. (2020)
DEAP (32), SEED (15)
CNN+SAE
Classifying emotion
92.86% (DEAP),
96.77% (SEED)
Li Y. et al. (2020)
EEGMMIDB (109)
Recurrent-CNN
Recognizing intention
97.36%
Maiorana (2020)
40 subjects (40)
RNN, CNN
Recognizing biometric
75.00%
Gao et al. (2020b)
DEAP (32), SEED (15)
CNN
Recognizing emotion
90.63%
Hwang et al. (2020)
SEED dataset (15)
CNN
Recognizing emotion
90.41%
Gao et al. (2020a)
15 right-handed healthy students (15)
CNN
Recognizing emotion
92.44%
Yang et al. (2020)
BCI competition IV dataset 1 (7)
CNN
Decoding MI EEG
86.40%
Fahimi et al. (2019)
120 healthy subjects performed the Stroop
color test (120)
CNN
Detecting attention
79.26%
Tang et al. (2019)
BCI competition data IV 2a (9)
CNN+SAE
Classifying eMI task
79.90%
Roy et al. (2019)
BCI competition IV 2b dataset (9)
CNN
Classifying brain states
80.32%
Fares et al. (2019)
ImageNet-EEG (1)
Bi-LSTM
Classifying image
97.30%
Wilaiprasitporn et al. (2019)
DEAP dataset (32)
CNN, RNN
Identifying person
99.90%
Qiao and Bi (2019)
BCI competition IV 2a dataset (9)
CNN+Bi-GRU
Classifying MI
76.62%
Zgallai et al. (2019)
10 volunteers (10)
CNN
EEG-driven BCI smart wheelchair
70.00 (raw EEG),
96.00% (Fourier)
Gao et al. (2019)
8 subjects in fatigue states (8)
CNN
Evaluating driver fatigue
97.37%
Puengdang et al. (2019)
20 subjects (20)
LSTM
Authenticating person
91.44%
Song et al. (2019)
BCI Competition IV dataset 2a (9)
CNN
Classifying MI
73.40%
Zhao et al. (2019)
BCI Competition IV dataset 2a (9)
CNN
Classifying MI
Mean kappa: 0.64
Chen et al. (2019b)
DEAP dataset (32)
CNN
Recognizing emotion
AUC: 99.88%
Chen et al. (2019a)
157 subjects (157)
CNN
Identifying biometric
96.00%
Dai et al. (2019)
BCI Competition IV dataset 2b (9)
CNN+VAE
Classifying MI
Kappa = 0.60
Amin et al. (2019b)
BCI Competition IV dataset 2a (9)
CNN
Classifying MI
75.7%
Saha et al. (2019)
KARA (14)
CNN+LSTM
Categorizing phonology
77.90%
Ozdemir et al. (2019)
DEAP dataset (32)
CNN
Estimating emotional state
95.96%
Tiwari et al. (2021)
BCI competition V dataset (3), Emotiv
dataset (16)
CNN
Classifying left hand and right hand
task
72.51% (BCI V),
72.00% (Emotiv)
Dang et al. (2021)
CHB-MIT datasets (24)
CNN
Detecting epilepsy
99.56%
Polat and Özerdem (2020)
BCI competition 2003 (1)
CNN
Detecting cursor movements
90.38%
Chakladar et al. (2020)
STEW dataset (48)
Bi-LSTM
Estimating mental workload
82.57%
Li F. et al. (2020)
BCI Competition IV 2b (9)
CNN
Classifying MI
83.20%
Alazrai et al. (2019)
22 subjects (22)
CNN
Decoding MI tasks of the same hand
73.70%
Liu Y. et al. (2020)
DEAP dataset (32)
CNN
Recognizing emotion
95.27%
Arnau-González et al. (2017)
DREAMER dataset (23)
CNN
Identifying subject
94.01%
Zhu et al. (2022)
MBT-42 (42), Med-62 (62)
ConvNet, 3D-CNN
Classifying MI
73.12% (MBT-42),
72.66% (Med-62)
Mattioli et al. (2022)
EEG Motor Movement Dataset V 1.0.0 (109)
1D-CNN
Classifying MI
99.38%
Du and Liu (2022)
MRCP (12)
InceptionEEG-Net
(CNN)
Classifying MI
AUC: 0.91%
It covers the key features, namely: datasets, number of subjects, deep learning modality, BCI application, and classiﬁcation results.
Frontiers in Computational Neuroscience
08
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
FIGURE 5
Distributions of datasets that are explored for EEG-based BCI applications.
to a few days to ﬁnd out more about their seizures and see if
they were good candidates for surgery. There are 23 patients in
the dataset, separated into 24 cases (a patient has 2 recordings,
1.5 years apart). There are 969 h of scalp EEG recordings in this
dataset, comprising 173 seizures. Seizures of various sorts can be
found in the dataset (clonic, atonic, and tonic).
• DEAP dataset (Koelstra et al., 2011) includes 32 individuals
who saw 1-min long music video snippets and judged
arousal/valence/like–dislike/dominance/familiarity, as well as
the frontal facial recording of 22 out of 32 subjects (Chen et al.,
2019b; Ozdemir et al., 2019; Wilaiprasitporn et al., 2019; Aldayel
et al., 2020; Gao et al., 2020a; Liu J. et al., 2020).
• The SEED-VIG dataset integrates EEG data with diligence
indicators throughout a driving virtual environment. In
addition, there are 18 conductive gels and eye-tracking (Ko et al.,
2020).
• SEED dataset wherein EEG was documented over 62 streams
from 15 participants as they regarded short videos eliciting
positive, negative, or neutral feelings (Gao et al., 2020a; Hwang
et al., 2020; Liu J. et al., 2020).
• The STEW dataset includes the raw EEG data of 48 participants
who took part in a multi-threaded workﬂow test using the
SIMKAP experiment (Chakladar et al., 2020).
• One participant observes an arbitrary picture (chosen from 14k
pictures in the ImageNet ILSVRC2013 training dataset) for 3 s,
while their EEG signals are documented. Over 70,000 specimens
are also included (Fares et al., 2019).
4.3. Deep learning modality
Deep Neural Networks (DNNs) are highly structured and
therefore can learn features from unreﬁned or modestly heavily
processed data, minimizing the need for domain-speciﬁc processing
and
feature
extraction
processes.
Furthermore,
DNN-learned
attributes may be even more proﬁcient or evocative than human-
designed attributes. Second, as in many realms where DL has
surpassed the previous condition, it has the potential to improve the
eﬀectiveness of other analyses and classiﬁcations. Third, DL makes
it easier to make tasks such as conceptual sculpting and domain
acclimation, which are not tried as often and fail less often when
using EEG data. Deep learning techniques have made it feasible
to synthesize high-dimensional structured data, such as images
and audio.
Deep learning-based methods have been used to sum up
high-dimensional, well-organized content such as images and
speech. Computational methods could be used by readers to grasp
transitional depictions or complement data. Deep neural networks
combined with techniques such as linkage synchronization make it
easier to learn representations that do not depend on the domain,
while keeping information about the task for domain adaptation.
Similar methods can be implemented with EEG data to obtain more
accurate depictions, and as a result, improve the performance of
EEG-based models across a wide range of subjects and tasks.
Various deep learning algorithms have been employed in EEG-
based BCI applications, whereas CNN is clearly the most frequent
one. For example, Arnau-González et al. (2017), Tang et al. (2017),
Vilamala et al. (2017), Antoniades et al. (2018), Aznan et al. (2018),
Behncke et al. (2018), Dose et al. (2018), El-Fiqi et al. (2018), Nguyen
and Chung (2018), Völker et al. (2018), Alazrai et al. (2019), Amber
et al. (2019), Amin et al. (2019b), Chen et al. (2019a,b), Fahimi
et al. (2019), Gao et al. (2019), Olivas-Padilla and Chacon-Murguia
(2019), Ozdemir et al. (2019), Roy et al. (2019), Song et al. (2019),
Tayeb et al. (2019), Zgallai et al. (2019), Zhao et al. (2019), Aldayel
et al. (2020), Gao et al. (2020a,b), Hwang et al. (2020), Ko et al.
(2020), Li Y. et al. (2020), Liu J. et al. (2020), Miao et al. (2020),
Oh et al. (2020), Polat and Özerdem (2020), Atilla and Alimardani
(2021), Cai et al. (2021), Dang et al. (2021), Deng et al. (2021), Huang
et al. (2021), Ieracitano et al. (2021), Mai et al. (2021), Mammone
et al. (2021), Petoku and Capi (2021), Reddy et al. (2021), Tiwari
et al. (2021), Zhang et al. (2021), Ak et al. (2022), and, Huang
et al. (2022) have explored deep learning-based algorithms. However,
more recent BCI studies have implemented other deep learning
modalities including,
• Long short-term memory (LSTM) (Zeng et al., 2018; Fares et al.,
2019; Hussein et al., 2019; Puengdang et al., 2019; Saha et al.,
Frontiers in Computational Neuroscience
09
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
TABLE 3 Maximum accuracy obtained from diﬀerent algorithms.
References
Dataset
Max.
accuracy
(%)
Algorithms
used
Rammy et al. (2020)
BCI competition IV
100
LSTM
Wilaiprasitporn
et al. (2019)
DEAP
99.90
CNN, RNN
Amber et al. (2019)
DRYAD
99.60
CNN
Dang et al. (2021)
CMB-MIT
99.56
CNN
Li Y. et al. (2020)
EEGMMIDB
97.36
R-CNN
Fares et al. (2019)
ImageNet-EEG
97.30
Bi-LSTM
Hwang et al. (2020)
SEED
96.77
CNN
Arnau-González
et al. (2017)
DREAMER
94.01
CNN
Huang et al. (2022)
Physionet
92.00
CNN
Chakladar et al.
(2020)
STEW
82.57
Bi-LSTM
Völker et al. (2018)
Flanker task
81.70
CNN
Saha et al. (2019)
KARA
77.90
CNN+LSTM
Tiwari et al. (2021)
Emotiv
72.00
CNN
2019; Chakladar et al., 2020; Penchina et al., 2020; Rammy et al.,
2020; Tortora et al., 2020; Cho et al., 2021; Shoeibi et al., 2021),
• Recurrent neural network (RNN) (Wilaiprasitporn et al., 2019;
León et al., 2020; Li F. et al., 2020; Penchina et al., 2020; Mai
et al., 2021; Sundaresan et al., 2021), and
• Autoencoders (AE) and variational AE (VAE) (Tabar and Halici,
2016; Dai et al., 2019; Tang et al., 2019).
5. Results and discussion
5.1. Dataset-speciﬁc studies
Diﬀerent classiﬁcation algorithms give diﬀerent maximum
accuracy values for diﬀerent datasets, as shown in Table 3. The LSTM
algorithm gave the highest accuracy, which was based on the BCI
competition dataset. All researchers achieved an accuracy of over 80%
for this dataset, that is, this dataset has the highest accuracy so far.
We have found the highest classiﬁcation accuracy for any algorithm
on the BCI competition dataset from various studies, as shown in
Figure 6.
For the DEAP dataset (Koelstra et al., 2011), all researchers
achieved an accuracy of roughly over 90% (Figure 7), that is,
this dataset has the highest reliability so far. Unlike the previous
dataset, this one has received little attention in terms of deep
learning applications. As with the previous two datasets, there are a
few works on the SEED dataset. However, the published works have
achieved over 90% accuracy based on CNN or CNN+SAE (Gao et al.,
2020a; Hwang et al., 2020; Liu J. et al., 2020). We can apply smarter
algorithms to this dataset to explore further.
Due to insuﬃcient work on the rest of the datasets shown in
Figure 8, we cannot comment on them. However, we think that
whether the accuracy can be increased on the rest of the dataset, it
can be worked on in future.
5.2. Deep leaning models for BCI studies
Among the 110 publications that have been studied in this
study, discriminative models, particularly CNN, are utilized most
frequently. This is right since almost all BCI problems can
be put into the category of classiﬁcation problems. More than
75% of the models are powered by CNN algorithms, and we
can summarize them as follows: (i) CNN can use EEG data
to ﬁnd hidden features and spatial correlations that can be
used to classify something. As a result, CNN structures are
used for classiﬁcation in certain research while features are
engineered in others; (ii) CNN has had considerable success in
various research areas (especially in imaging and computer vision
domains), making it exceedingly well-known and simple to use
(through the available public code). Surprisingly, several BCI
techniques naturally produce two-dimensional visuals that can be
processed by CNN, and EEG data could be converted into two-
dimensional images in the meantime for additional processing
by CNN.
On the contrary, only 15% of the model-based articles used
a recurrent neural network (RNN), even though RNN is capable
of predicting temporal feature learning. One likely reason for this
is that it takes time for an RNN to process a long sequence,
and EEG signals are often long sequences. EEG signals, for
example, are typically divided into 30-s segments with 2,500
time points at a 120 Hz sampling rate. Moreover, RNN takes
more than 25 times as long to train as CNN for a sequence of
2,500 items.
Furthermore, among the typical models, the deep belief network
(DBN), particularly the DBN-restricted Boltzmann machine (RBM),
is the most often used model for feature extraction. DBN is
commonly utilized in BCI for two reasons: 1) It is an eﬃcient
way to learn the top-down generative parameters that show how
variables in one layer depend on variables in the layer above.
2) The values of the latent variables in each layer can be
guessed by a single bottom-up pass that starts with an observed
data vector in the bottom layer and uses the generative weights
in the opposite direction. But most of the work that used
the DBN-RBM model was published before 2018, which shows
that DBN is not popular right now. Before 2018, researchers
used DBN to learn about features, and then a classiﬁer that
did not use deep learning. Now, more and more studies use
CNN or hybrid models for both learning about features and
classifying them.
Finally, there are nine articles suggesting hybrid models for BCI
research. Combinations of RNN and CNN account for approximately
a third. It is logical to integrate RNN and CNN for both temporal and
spatial feature learning, given that RNN and CNN are renowned for
their exceptional temporal and spatial feature extraction capabilities.
Combining representative and discriminative models is yet another
sort of hybrid model. This is easy to understand since the ﬁrst is
used to pull out features and the second is used to put things into
groups. There are nine articles that use this form of hybrid deep
learning model, which encompasses almost all types of BCI signals.
In addition, 12 studies have presented alternative hybrid models,
including two discriminative ones. Several research, for instance, have
advocated the combination of CNN with MLP in which the CNN
structure is utilized to extract spatial data that are then given to an
MLP for classiﬁcation.
Frontiers in Computational Neuroscience
10
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
FIGURE 6
A comparative schematic of accuracies by various deep learning approaches [i.e., Convolutional neural network (CNN) (Islam et al., 2021), long
short-term memory (LSTM), stacked autoencoder (SAE), and variational autoencoder (VAE)] on the BCI competition dataset.
FIGURE 7
A graph of accuracies by various deep learning approaches on the DEAP dataset.
5.3. BCI applications and deep learning
Deep learning-based BCI systems are mostly used in the
healthcare industry to identify and diagnose mental illnesses,
including epilepsy, Alzheimer’s disease, and other disorders (Dose
et al., 2018). First, research focusing on sleep-stage recognition
based on sleeping spontaneous EEG is utilized to identify sleeping
disorders (Vallabhaneni et al., 2021). As a result, the researchers
do not need to seek out patients with sleeping issues since it is
simple to gather the sleeping EEG signals from healthy people in this
condition. The diagnosis of epileptic seizures has also garnered a great
deal of interest. The majority of seizure detection is dependent on
spontaneous EEG and mental illness signs (Antoniades et al., 2018;
Hussein et al., 2019; Dang et al., 2021; Shoeibi et al., 2021). CNN and
RNN are common deep learning models in this context, as are hybrid
models that combine RNN and CNN. Several methods (Turner et al.,
2014) combined deep learning models for feature extraction with
classical classiﬁers for detection. To diagnose seizures, researchers
used a VAE in feature engineering followed by SVM.
Smart environments are a possible future application scenario
for BCI. With the rise of the Internet of Things (IoT), BCI can
be linked to a growing number of smart settings. For instance, an
aiding robot may be used in a smart house (Zhang et al., 2018c)
in which the robot is controlled by brain impulses. In addition,
Behncke et al. (2018) examined how to operate a robot using
visually stimulated spontaneous EEG and fNIRS data. BCI-controlled
Frontiers in Computational Neuroscience
11
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
FIGURE 8
The accuracies of the SEED dataset based on CNN or CNN+SAE.
exoskeletons might assist individuals with compromised lower limb
motor control in walking and everyday activities (Kwak et al., 2017).
In future, research on brain-controlled equipment may be useful
for developing smart homes and smart hospitals for the elderly and
the crippled.
In comparison to other human–machine interface approaches,
the greatest beneﬁt of BCI is that it allows patients who have
lost most motor functions, such as speaking, to interact with the
outside world (Nguyen and Chung, 2018). Deep learning technology
has considerably enhanced the eﬃciency of the brain’s signal-based
communications. The P300 speller is a common paradigm that allows
individuals to type without a motor system, which can turn the user’s
intent into text (Cecotti and Graser, 2010). In addition, Zhang et al.
(2018b) suggested a hybrid model that combines RNN, CNN, and AE
to extract relevant characteristics from MI EEG to detect the letter the
user intends to write. The suggested interface consists of 27 characters
(26 English alphabets and the space bar) split into three character
blocks (each block containing nine characters) in the ﬁrst interface.
There are three possible choices, and each one leads to a separate
sub-interface with nine characters.
A prominent topic of interest for BCI researchers is the
security industry. A security issue may be broken down into
authentication (also known as “veriﬁcation”) and identity (also
known as “recognition”) components (Arnau-González et al., 2017;
El-Fiqi et al., 2018; Chen et al., 2019b; Puengdang et al., 2019;
Maiorana, 2020). The goal of the former, which is often a multi-
class classiﬁcation task, is to identify the test subject (Zhang et al.,
2017). This is usually a simple yes-or-no question that only looks
at whether the test subject is allowed or not. Existing biometric
identiﬁcation/authentication systems rely primarily on the unique
inherent physiological characteristics of people (e.g., face, iris, retina,
voice, and ﬁngerprint). Anti-surveillance prosthetic masks that may
defy face recognition, contact lenses that can fool iris detection,
vocoders that can compromise speech identiﬁcation, and ﬁngerprint
ﬁlms that can fool ﬁngerprint sensors are all vulnerable. Due to their
great attack resilience, EEG-based biometric person identiﬁcation
systems are emerging as attractive alternatives. Individual EEG
waves are almost impossible for an impostor to replicate, making
this method extremely resistant to spooﬁng assaults faced by other
identiﬁcation methods. Deep neural networks were used by Mao et al.
(2017) to identify the user’s ID based on EEG signals, and CNN was
used for personal identiﬁcation. Zhang et al. (2017) presented and
analyzed an attention-based LSTM model on both public and local
datasets. The researchers (Zhang et al., 2018a) subsequently merged
EEG signals with gait data to develop a dual-authentication system
using a hybrid deep learning model.
Several articles simply aim to categorize the user’s emotional state
as a binary (positive/negative) or three-category (positive, neutral,
and negative) issue using deep learning algorithms (Chen et al.,
2019b; Ozdemir et al., 2019; Gao et al., 2020a,b; Hwang et al., 2020;
Liu J. et al., 2020; Liu Y. et al., 2020; Sundaresan et al., 2021). Diverse
articles employed CNN and its modiﬁcations to identify emotional
EEG data (Li et al., 2016) and lie detection (Amber et al., 2019).
Most of the time, the CNN-RNN deep learning model is used to
ﬁnd hidden traits in spontaneous emotional EEG. Using EEG data,
Xu and Plataniotis (2016) employed a deep belief network (DBN) as
a particular feature extractor for the emotional state categorization
task. Moreover, on a more basic level, some studies seek to identify
a positive/negative condition for each emotional dimension. For
identifying emotions, Yin et al. (2017) suggested a multiple-fusion-
layer-based ensemble classiﬁer of AE. Each AE is made up of three
hidden layers that remove unwanted noise from the physiological
data and give accurate representations of the features.
For traﬃc safety to be assured, a driver must be able to keep up
their best performance and pay close attention. It has been shown that
EEG signals may be beneﬁcial in assessing people’s cognitive status
while doing certain activities (Almogbel et al., 2018). A motorist is
often considered alert if their response time is less than or equal to
0.7 s and weary if their reaction time is more than or equal to 2.1 s. By
extracting the distinctive elements from the EEG data, Hajinoroozi
et al. (2015) investigated the prediction of a driver’s weariness. They
investigated a DBN-based dimensionality reduction strategy. It is
Frontiers in Computational Neuroscience
12
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
important to be able to tell when a driver is tired since that can make
accidents more likely. Furthermore, it is practical to identify driver
weariness in daily life. The technology that is used to record EEG data
is easy to ﬁnd and small enough to use in a car. In addition, the cost
of an EEG headset is reasonable for the majority of individuals. Deep
learning algorithms have greatly improved the accuracy of tiredness
detection. In conclusion, driving sleepiness based on EEG may be
identiﬁed with excellent accuracy (83–98%) (Fahimi et al., 2019; Ko
et al., 2020; Atilla and Alimardani, 2021; Cai et al., 2021). The self-
driving situation is where driver fatigue monitoring will likely be used
in future. Since the human driver is often expected to react correctly
to a request to intervene in most self-driving scenarios, the driver
must always be aware. As a result, we think that using BCI-based drive
fatigue detection can help the development of autonomous vehicles.
Human operators play an important role in automation systems
for decision-making and strategy formulation. Human functional
states, unlike those of machines or computers, cannot always meet
the needs of a task because working memory is limited, and psycho-
physiological experience changes over time. A lot of researchers have
concentrated on this subject. The mental eﬀort may be calculated
using spontaneous EEG. Bashivan et al. (2015) introduced a DBN
model, a statistical technique for predicting cognitive load from single
trial EEG.
5.4. Recommendation for future research
However, there are still plenty of deep learning premises and
domains to be used in EEG-based BCI, which will not only improve
the performance but also make them more generalizable. Here are
a few suggestions for future researchers regarding where they can
uncover novelty utilizing deep learning.
• Graph
Convolutional
Networks
(GCNs):
One
of
the
fundamental functions of the BCI is controlling machines using
only the MI and no physical motions. For the development
of these BCI devices, it is very important to be able to classify
MI brain activity in a reliable way. Even though previous
research has shown promising results, there is still a need to
improve classiﬁcation accuracy to make BCI applications that
are useful and cost-eﬀective. One problem with making an
EEG MI-based wheelchair is that it is still hard to make it
ﬂexible and resistant to diﬀerences between people. Traditional
techniques to decipher EEG data do not include the topological
link between electrodes. So, it is possible that the Euclidean
structure of EEG electrodes does not give a good picture of how
signals interact with each other. To solve the problem, graph
convolutional neural networks (GCNs) are presented to decode
EEG data. GCN is a semi-supervised model that is often used
to get topological properties from data in non-Euclidean space.
GCNs have been used successfully in a number of graph-based
applications. Graphs can show complicated relationships
between entities. GCN not only successfully extracts topological
information from data but also it has interpretability and
operability. Recently, researchers are shifting to GCN from
CNNs for various applications as it can capture relational
data better than CNNs. Though some studies have recently
reported GCN in EEG-based BCI (Hou et al., 2020; Jia et al.,
2020), it is mostly undiscovered. Any research in this domain
using GCN might be the breakthrough needed to trigger deep
learning-based BCI studies.
• Transfer Learning: The study of deep neural network-based
methods for successfully transferring information from relevant
disciplines is known as “deep transfer learning”. Transfer
learning focuses on dealing with facts that defy this notion by
utilizing knowledge acquired while completing one assignment
for a diﬀerent but related job. Transfer learning uses data that
have already been used to increase the size of the dataset.
This means that there is no need to calibrate from scratch,
transferred information is less noisy, and TL can loosen BCI
constraints. Session-to-session transfer learning in BCIs is based
on the idea that features extracted by the training module and
algorithms can be used to help a subject do the same task in a
diﬀerent session. To ﬁnd the best way to divide decisions among
the diﬀerent training sections, it is important to look at what
they all have in common. As TL has a lot more opportunities
in BCI applications, we have a few recommendations for
future researchers.
The majority of TL research has focused on inter-subject
and intersession transfer. Cross-device transfers are beginning
to gain interest, although cross-task transfers are mostly
unexplored. Since 2016, there has, to the best of our knowledge,
been only one similar research (He and Wu, 2020). Transfers
between devices and tasks would make EEG-based BCIs far
more realistic.
Utilizing the transferability of adversarial cases, adversarial
assaults–one of the most recent advancements in EEG-based
BCIs, may be carried out across several machine learning
models. However, speciﬁcally considering TL across domains
may boost the attack’s performance further. In black box attacks,
for example, TL can use publicly available datasets to reduce the
number of queries to the victim model or better approximate the
victim model with the same number of queries.
Regression issues and emotional BCI are two fresh uses
of EEG-based BCIs that have been piquing curiosity among
researchers. It is interesting that they are both passive BCIs.
Although aﬀective BCI may be used to create both classiﬁcation
and regression problems, the majority of past research has been
on classiﬁcation issues.
• Generative Deep Learning : The primary purpose of generative
deep learning models is to produce training samples or
supplement data. In other words, generative deep learning
models help the BCI industry by making the training data
better and giving it more of it. After augmenting the data,
discriminative models will be used for classiﬁcation. This
method is meant to make trained deep learning networks more
reliable and eﬀective, especially when there is not a lot of
training data. In short, the generative models use the input
data to make a set of output data that is similar to the input
data. This section will present two common generative deep
learning models: variational autoencoder (VAE) and generative
adversarial networks (GANs).
VAE is an important type of AE and one of the best
algorithms for making things. The standard AE and its
variations can be used for representation, but they cannot be
used for generation since the learned code (or representation)
Frontiers in Computational Neuroscience
13
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
might not be continuous. Therefore, it is impossible to make a
random sample that is the same as the sample that was put in.
In other words, interpolation is not supported by the standard
AE. Therefore, we can duplicate the input sample but cannot
construct one that is similar. This trait is what makes VAE so
valuable for generative modeling: the latent spaces are meant to
be continuous, which can make a huge contribution to capturing
EEG data features for BCI applications (Lee et al., 2022).
Machine learning and deep learning modules must be
trained on a signiﬁcant amount of real-world data to perform
classiﬁcation tasks; however, there may be restrictions on
obtaining enough real data or the time and resources required
may be simply too great. GANs, have seen an increase in activity
in recent years, and are primarily used for data augmentation
to address the issue of how to produce synthetic yet realistic-
looking samples to mimic real-world data using generative
models so that the training data sample number can be
increased. In comparison to CNNs, GANs have, to the best of
our knowledge, been studied much less in BCIs. This is primarily
due to the incomplete evaluation of the viability of using a
GAN to generate time sequence data. The spatial, spectral, and
temporal properties of the EEG data produced by the GAN are
comparable to those of actual EEG signals (Fahimi et al., 2020).
This opens up new avenues for future research on GANs in
EEG-based BCIs.
6. Conclusion
Deep learning (DL) has historically resulted in signiﬁcant
breakthroughs
in
supervised
classiﬁcation
tasks,
which
were
envisaged to be the concentration of the majority of research
chosen for assessment. Remarkably, numerous studies spotlighted
the new use cases facilitated by the study results. For example,
generating visual eﬀects based on EEG, deriving EEG, learning from
other participants, and learning about attributes are all diﬀerent
ways to learn. One of the main reasons for using DL is that
it can manage raw EEG data without mandating a substantial
preprocessing step, which is alluded to in the literature as an
“end-to-end structure.” Given that EEG is clearly linked to certain
parts of the brain, we thought that RNNs would be much
more widespread than models that do not explicitly take time
into account.
Adding to its prospects is the willingness of deep learning in
the EEG to extrapolate across respondents and facilitate transfer
learning across activities and domains. Regardless of the fact that
intra-subject models are still the most eﬃcacious when only restricted
evidence is accessible, ensemble learning may well be the best way to
overcome this restriction given the obvious determining factor of the
rate of EEG data. Using a predictive model, one can train a neural
network on a sample of subjects before ﬁne-tuning it on a single
individual, which is likely to result in favorable results with less data
from the individual. DNNs are typically regarded as “black boxes”
when likened to more conventional means; therefore, it is crucial
to scrutinize trained DL models. Indeed, simple model inspection
techniques such as showing the weights of a linear classiﬁer do not
apply to deep neural networks, making their decisions far more
diﬃcult to comprehend.
This
study
presents
an
overview
of
EEG-based
BCIs
incorporating
deep
learning,
with
a
concentration
on
the
epistemological advantages and pitfalls, as well as the invaluable
eﬀorts in this area of study. This study shows that more research
needs to be conducted on how much data are needed to use deep
learning in EEG processing to its fullest potential. This type of
research could look at the relationship between performance and
data volume, eﬀectiveness and data augmentation, performance, data
volume, and network depth. For each BCI application, researchers
have examined measurement techniques, control signals, EEG
feature
extraction,
classiﬁcation
techniques,
and
performance
evaluation metrics. Tuning hyper-parameters could have been
the key to increasing the eﬃciency of deeper frameworks in deep
learning mode by adjusting hyper-parameters. As mentioned earlier
about the lack of hyper-parameter search in this domain, this issue
should be addressed in future studies.
Author contributions
KH, SH, and MI contributed the core writing and analysis. AN
and MA edited and partially wrote the paper. All authors contributed
to the article and approved the submitted version.
Conﬂict of interest
The authors declare that the research was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construed as a potential conﬂict of interest.
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the reviewers.
Any product that may be evaluated in this article, or claim that may
be made by its manufacturer, is not guaranteed or endorsed by the
publisher.
References
Abdulkader, S. N., Atia, A., and Mostafa, M.-S. M. (2015). Brain computer interfacing:
applications and challenges. Egyptian Inf. J. 16, 213–230. doi: 10.1016/j.eij.2015.
06.002
Abiri, R., Borhani, S., Sellers, E. W., Jiang, Y., and Zhao, X. (2019). A comprehensive
review of eeg-based brain-computer interface paradigms. J. Neural Eng. 16, 011001.
doi: 10.1088/1741-2552/aaf12e
Acar, E., Roald, M., Hossain, K. M., Calhoun, V. D., and Adali, T. (2022). Tracing
evolving networks using tensor factorizations vs. ica-based approaches. Front. Neurosci.
16, 861402. doi: 10.3389/fnins.2022.861402
Agrawal, R., and Bajaj, P. (2020). “EEG based brain state classiﬁcation technique using
support vector machine-a design approach,” in 2020 3rd International Conference on
Intelligent Sustainable Systems (ICISS) (Thoothukudi: IEEE), 895–900.
Frontiers in Computational Neuroscience
14
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
Ak, A., Topuz, V., and Midi, I. (2022). Motor imagery eeg signal classiﬁcation
using image processing technique over googlenet deep learning algorithm for
controlling the robot manipulator. Biomed. Signal Process. Control. 72, 103295.
doi: 10.1016/j.bspc.2021.103295
Akhter, T., Islam, M. A., and Islam, S. (2020). Artiﬁcial neural network based COVID-
19 suspected area identiﬁcation. J. Eng. Adv. 1, 188–194. doi: 10.38032/jea.2020.04.010
Alazrai, R., Abuhijleh, M., Alwanni, H., and Daoud, M. I. (2019). A deep learning
framework for decoding motor imagery tasks of the same hand using eeg signals. IEEE
Access 7, 109612–109627. doi: 10.1109/ACCESS.2019.2934018
Aldayel,
M.,
Ykhlef,
M.,
and
Al-Nafjan,
A.
(2020).
Deep
learning
for
eeg-based
preference
classiﬁcation
in
neuromarketing.
Appl.
Sci.
10,
1525.
doi: 10.3390/app10041525
Almogbel, M. A., Dang, A. H., and Kameyama, W. (2018). “EEG-signals based
cognitive workload detection of vehicle driver using deep learning,” in 2018 20th
International Conference on Advanced Communication Technology (ICACT) (Chuncheon:
IEEE), 256–259.
Al-Saegh, A., Dawwd, S. A., and Abdul-Jabbar, J. M. (2021). Deep learning for motor
imagery eeg-based classiﬁcation: a review. Biomed. Signal Process. Control 63, 102172.
doi: 10.1016/j.bspc.2020.102172
Alzahab, N. A., Apollonio, L., Di Iorio, A., Alshalak, M., Iarlori, S., Ferracuti, F.,
et al. (2021). Hybrid deep learning (hdl)-based brain-computer interface (bci) systems:
a systematic review. Brain Sci. 11, 75. doi: 10.3390/brainsci11010075
Amarasinghe, K., Wijayasekara, D., and Manic, M. (2014). “EEG based brain activity
monitoring using artiﬁcial neural networks,” in 2014 7th International Conference on
Human System Interactions (HSI) (Costa da Caparica: IEEE), 61–66.
Amber, F., Yousaf, A., Imran, M., and Khurshid, K. (2019). “P300 based deception
detection using convolutional neural network,” in 2019 2nd International Conference on
Communication, Computing and Digital Systems (C-CODE) (Islamabad: IEEE), 201–204.
Amin, S. U., Alsulaiman, M., Muhammad, G., Bencherif, M. A., and Hossain,
M. S. (2019a). Multilevel weighted feature fusion using convolutional neural
networks for EEG motor imagery classiﬁcation. IEEE Access 7, 18940–18950.
doi: 10.1109/ACCESS.2019.2895688
Amin, S. U., Alsulaiman, M., Muhammad, G., Mekhtiche, M. A., and Hossain,
M. S. (2019b). Deep learning for EEG motor imagery classiﬁcation based on
multi-layer cnns feature fusion. Future Generat. Comput. Syst. 101, 542–554.
doi: 10.1016/j.future.2019.06.027
Antoniades, A., Spyrou, L., Martin-Lopez, D., Valentin, A., Alarcon, G., Sanei, S., et al.
(2018). Deep neural architectures for mapping scalp to intracranial EEG. Int. J. Neural
Syst. 28, 1850009. doi: 10.1142/S0129065718500090
Arnau-González, P., Katsigiannis, S., Ramzan, N., Tolson, D., and Arevalillo-Herrez,
M. (2017). “Es1d: a deep network for eeg-based subject identiﬁcation,” in 2017 IEEE 17th
International Conference on Bioinformatics and Bioengineering (BIBE) (Washington, DC:
IEEE), 81–85.
Atilla, F., and Alimardani, M. (2021). “EEG-based classiﬁcation of drivers attention
using convolutional neural network,” in 2021 IEEE 2nd International Conference on
Human-Machine Systems (ICHMS) (Magdeburg: IEEE), 1–4.
Aznan, N. K. N., Bonner, S., Connolly, J., Al Moubayed, N., and Breckon, T. (2018). “On
the classiﬁcation of ssvep-based dry-EEG signals via convolutional neural networks,” in
2018 IEEE International Conference on Systems, Man, and Cybernetics (SMC) (Miyazaki:
IEEE), 3726–3731.
Aznan, N. K. N., and Yang, Y.-M. (2013). “Applying kalman ﬁlter in EEG-based brain
computer interface for motor imagery classiﬁcation,” in 2013 International Conference on
ICT Convergence (ICTC) (Jeju: IEEE), 688–690.
Bashivan, P., Yeasin, M., and Bidelman, G. M. (2015). “Single trial prediction of normal
and excessive cognitive load through eeg feature fusion,” in 2015 IEEE Signal Processing
in Medicine and Biology Symposium (SPMB) (Philadelphia, PA: IEEE), 1–5.
Behncke, J., Schirrmeister, R. T., Burgard, W., and Ball, T. (2018). “The signature
of robot action success in eeg signals of a human observer: decoding and visualization
using deep convolutional neural networks,” in 2018 6th International Conference on
Brain-Computer Interface (BCI) (Gangwon: IEEE), 1–6.
Bi, L., Fan, X.-A., and Liu, Y. (2013). EEG-based brain-controlled mobile robots: a
survey. IEEE Trans. Hum. Mach. Syst. 43, 161–176. doi: 10.1109/TSMCC.2012.2219046
Bousseta, R., El Ouakouak, I., Gharbi, M., and Regragui, F. (2018). Eeg based brain
computer interface for controlling a robot arm movement through thought. Irbm 39,
129–135. doi: 10.1016/j.irbm.2018.02.001
Cai, H., Xia, M., Nie, L., Wu, Y., and Zhang, Y. (2021). “Deep learning models with time
delay embedding for eeg-based attentive state classiﬁcation,” in International Conference
on Neural Information Processing (Springer), 307–314.
Cao, Z. (2020). A review of artiﬁcial intelligence for eeg-based brain- computer
interfaces and applications. Brain Sci. Adv. 6, 162–170. doi: 10.26599/BSA.2020.9050017
Cecotti, H., and Graser, A. (2010). Convolutional neural networks for p300 detection
with application to brain-computer interfaces. IEEE Trans. Pattern Anal. Mach. Intell. 33,
433–445. doi: 10.1109/TPAMI.2010.125
Chakladar, D. D., Dey, S., Roy, P. P., and Dogra, D. P. (2020). Eeg-based mental
workload estimation using deep blstm-lstm network and evolutionary algorithm. Biomed.
Signal Process. Control. 60, 101989. doi: 10.1016/j.bspc.2020.101989
Chen, J., Mao, Z., Yao, W., and Huang, Y. (2019a). “EEG-based biometric identiﬁcation
with convolutional neural network,” in Multimedia Tools and Applications (Dordrecht),
1–21.
Chen, J., Zhang, P., Mao, Z., Huang, Y., Jiang, D., and Zhang, Y. (2019b). Accurate
eeg-based emotion recognition on combined features using deep convolutional neural
networks. IEEE Access 7, 44317–44328. doi: 10.1109/ACCESS.2019.2908285
Cho, J.-H., Jeong, J.-H., and Lee, S.-W. (2021). Neurograsp: Real-time eeg classiﬁcation
of high-level motor imagery tasks using a dual-stage deep learning framework. IEEE
Trans. Cybern. 52, 13279–13292. doi: 10.1109/TCYB.2021.3122969
Craik, A., He, Y., and Contreras-Vidal, J. L. (2019). Deep learning for
electroencephalogram (eeg) classiﬁcation tasks: a review. J. Neural Eng. 16, 031001.
doi: 10.1088/1741-2552/ab0ab5
Crespo-Garcia, M., Atienza, M., and Cantero, J. L. (2008). Muscle artifact removal
from human sleep eeg by using independent component analysis. Ann. Biomed. Eng. 36,
467–475. doi: 10.1007/s10439-008-9442-y
Dai, M., Zheng, D., Na, R., Wang, S., and Zhang, S. (2019). EEG classiﬁcation of motor
imagery using a novel deep learning framework. Sensors 19, 551. doi: 10.3390/s19030551
Dang, W., Lv, D., Rui, L., Liu, Z., Chen, G., and Gao, Z. (2021). Studying multi-
frequency multilayer brain network via deep learning for eeg-based epilepsy detection.
IEEE Sens. J. 21, 27651–27658. doi: 10.1109/JSEN.2021.3119411
Delorme, A., Sejnowski, T., and Makeig, S. (2007). Enhanced detection of artifacts in
EEG data using higher-order statistics and independent component analysis. Neuroimage
34, 1443–1449. doi: 10.1016/j.neuroimage.2006.11.004
Deng, X., Zhang, B., Yu, N., Liu, K., and Sun, K. (2021). Advanced tsgl-eegnet
for motor imagery EEG-based brain-computer interfaces. IEEE Access 9, 25118–25130.
doi: 10.1109/ACCESS.2021.3056088
Dose, H., Møller, J. S., Iversen, H. K., and Puthusserypady, S. (2018). An end-to-end
deep learning approach to mi-eeg signal classiﬁcation for bcis. Expert. Syst. Appl. 114,
532–542. doi: 10.1016/j.eswa.2018.08.031
Du, Y., and Liu, J. (2022). IENet: a robust convolutional neural network for eeg based
brain-computer interfaces. J. Neural Eng. 19, 036031. doi: 10.1088/1741-2552/ac7257
El-Fiqi, H., Wang, M., Salimi, N., Kasmarik, K., Barlow, M., and Abbass, H. (2018).
“Convolution neural networks for person identiﬁcation and veriﬁcation using steady state
visual evoked potential,” in 2018 IEEE International Conference on Systems, Man, and
Cybernetics (SMC) (Miyazaki: IEEE), 1062–1069.
Fahimi, F., Dosen, S., Ang, K. K., Mrachacz-Kersting, N., and Guan, C. (2020).
Generative adversarial networks-based data augmentation for brain-computer interface.
IEEE Trans. Neural Netw. Learn. Syst. 32, 4039–4051. doi: 10.1109/TNNLS.2020.3016666
Fahimi, F., Zhang, Z., Goh, W. B., Lee, T.-S., Ang, K. K., and Guan, C. (2019).
Inter-subject transfer learning with an end-to-end deep convolutional neural network for
eeg-based bci. J. Neural Eng. 16, 026007. doi: 10.1088/1741-2552/aaf3f6
Fares, A., Zhong, S.-H., and Jiang, J. (2019). EEG-based image classiﬁcation via a
region-level stacked bi-directional deep learning framework. BMC Med. Inform. Decis.
Mak. 19, 1–11. doi: 10.1186/s12911-019-0967-9
Gao, Z., Li, Y., Yang, Y., Wang, X., Dong, N., and Chiang, H.-D. (2020a). A
gpso-optimized convolutional neural networks for eeg-based emotion recognition.
Neurocomputing 380, 225–235. doi: 10.1016/j.neucom.2019.10.096
Gao, Z., Wang, X., Yang, Y., Li, Y., Ma, K., and Chen, G. (2020b). A channel-fused
dense convolutional network for EEG-based emotion recognition. IEEE Trans. Cognit.
Dev. Syst. 13, 945–954. doi: 10.1109/TCDS.2020.2976112
Gao, Z., Wang, X., Yang, Y., Mu, C., Cai, Q., Dang, W., et al. (2019). EEG-based spatio-
temporal convolutional neural network for driver fatigue evaluation. IEEE Trans. Neural
Netw. Learn. Syst. 30, 2755–2763. doi: 10.1109/TNNLS.2018.2886414
Guger, C., Allison, B. Z., and Gunduz, A. (2021). “Brain-computer interface research: a
state-of-the-art summary 10,” in Brain-Computer Interface Research (Springer), 1–11.
Hajinoroozi, M., Jung, T.-P., Lin, C.-T., and Huang, Y. (2015). “Feature extraction
with deep belief networks for driver’s cognitive states prediction from EEG data,” in 2015
IEEE China Summit and International Conference on Signal and Information Processing
(ChinaSIP) (Chengdu: IEEE), 812–815.
Hassanien, A. E., and Azar, A. (2015). Brain-Computer Interfaces. Switzerland: Springer
74.
He, H., and Wu, D. (2020). Diﬀerent set domain adaptation for brain-computer
interfaces: A label alignment approach. IEEE Trans. Neural Syst. Rehabil. Eng. 28,
1091–1108. doi: 10.1109/TNSRE.2020.2980299
Herman, P., Prasad, G., McGinnity, T. M., and Coyle, D. (2008). Comparative analysis
of spectral approaches to feature extraction for eeg-based motor imagery classiﬁcation.
IEEE Trans. Neural Syst. Rehabil. Eng. 16, 317–326. doi: 10.1109/TNSRE.2008.926694
Hossain, K. M., Bhinge, S., Long, Q., Calhoun, V. D., and Adali, T. (2022). “Data-
driven spatio-temporal dynamic brain connectivity analysis using falﬀ: application to
sensorimotor task data,” in 2022 56th Annual Conference on Information Sciences and
Systems (CISS) (Princeton, NJ: IEEE), 200–205.
Hou, Y., Jia, S., Lun, X., Shi, Y., and Li, Y. (2020). Deep feature mining via attention-
based bilstm-gcn for human motor imagery recognition. arXiv preprint arXiv:2005.00777.
doi: 10.48550/arXiv.2005.00777
Huang, E., Zheng, X., Fang, Y., and Zhang, Z. (2021). Classiﬁcation of
motor imagery EEG based on time-domain and frequency-domain dual-stream
Frontiers in Computational Neuroscience
15
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
convolutional
neural
network.
IRBM
43,
107–113.
doi:
10.1016/j.irbm.2021.
04.004
Huang, W., Chang, W., Yan, G., Yang, Z., Luo, H., and Pei, H. (2022). EEG-based motor
imagery classiﬁcation using convolutional neural networks with local reparameterization
trick. Expert. Syst. Appl. 187, 115968. doi: 10.1016/j.eswa.2021.115968
Hussein, R., Palangi, H., Ward, R. K., and Wang, Z. J. (2019). Optimized deep neural
network architecture for robust detection of epileptic seizures using eeg signals. Clini.
Neurophysiol. 130, 25–37. doi: 10.1016/j.clinph.2018.10.010
Hwang, S., Hong, K., Son, G., and Byun, H. (2020). Learning cnn features from
de features for EEG-based emotion recognition. Pattern Anal. Appl. 23, 1323–1335.
doi: 10.1007/s10044-019-00860-w
Ieracitano, C., Morabito, F. C., Hussain, A., and Mammone, N. (2021). A hybrid-
domain deep learning-based bci for discriminating hand motion planning from EEG
sources. Int. J. Neural Syst. 31, 2150038. doi: 10.1142/S0129065721500386
Islam, M., Shampa, M., and Alim, T. (2021). Convolutional neural network based
marine cetaceans detection around the swatch of no ground in the bay of bengal. Int.
J. Comput. Digit. Syst. 12, 173. doi: 10.12785/ijcds/120173
Islam, M. A., Hasan, M. R., and Begum, A. (2020). Improvement of the handover
performance and channel allocation scheme using fuzzy logic, artiﬁcial neural network
and neuro-fuzzy system to reduce call drop in cellular network. J. Eng. Adv. 1, 130–138.
doi: 10.38032/jea.2020.04.004
Islam, S., Reza, R., Hasan, M. M., Mishu, N. D., Hossain, K. M., and Mahmood, Z. H.
(2016). Eﬀects of various ﬁlter parameters on the myocardial perfusion with polar plot
image. Int. J. Eng. Res. 4, 1–10.
Jia, S., Hou, Y., Shi, Y., and Li, Y. (2020). Attention-based graph resnet
for motor intent detection from raw eeg signals. arXiv preprint arXiv:2007.13484.
doi: 10.48550/arXiv.2007.13484
Kilicarslan, A., Grossman, R. G., and Contreras-Vidal, J. L. (2016). A robust adaptive
denoising framework for real-time artifact removal in scalp eeg measurements. J. Neural
Eng. 13, 026013. doi: 10.1088/1741-2560/13/2/026013
Kline, J. E., Huang, H. J., Snyder, K. L., and Ferris, D. P. (2015). Isolating gait-related
movement artifacts in electroencephalography during human walking. J. Neural Eng. 12,
046022. doi: 10.1088/1741-2560/12/4/046022
Ko, W., Oh, K., Jeon, E., and Suk, H.-I. (2020). “Vignet: a deep convolutional neural
network for EEG-based driver vigilance estimation,” in 2020 8th International Winter
Conference on Brain-Computer Interface (BCI) (Gangwon: IEEE), 1–3.
Koelstra, S., Muhl, C., Soleymani, M., Lee, J.-S., Yazdani, A., Ebrahimi, T., et al. (2011).
Deap: A database for emotion analysis; using physiological signals. IEEE Trans. Aﬀect.
Comput. 3, 18–31. doi: 10.1109/T-AFFC.2011.15
Korovesis, N., Kandris, D., Koulouras, G., and Alexandridis, A. (2019). Robot motion
control via an eeg-based brain-computer interface by using neural networks and alpha
brainwaves. Electronics 8, 1387. doi: 10.3390/electronics8121387
Kwak, N.-S., Müller, K.-R., and Lee, S.-W. (2017). A convolutional neural network for
steady state visual evoked potential classiﬁcation under ambulatory environment. PLoS
ONE 12, e0172578. doi: 10.1371/journal.pone.0172578
Lee, D.-Y., Jeong, J.-H., Lee, B.-H., and Lee, S.-W. (2022). Motor imagery classiﬁcation
using inter-task transfer learning via a channel-wise variational autoencoder-based
convolutional neural network. IEEE Trans. Neural Syst. Rehabil. Eng. 30, 226–237.
doi: 10.1109/TNSRE.2022.3143836
León, J., Escobar, J. J., Ortiz, A., Ortega, J., González, J., Martín-Smith, P., et al. (2020).
Deep learning for eeg-based motor imagery classiﬁcation: accuracy-cost trade-oﬀ. PLoS
ONE 15, e0234178. doi: 10.1371/journal.pone.0234178
Li, F., He, F., Wang, F., Zhang, D., Xia, Y., and Li, X. (2020). A novel simpliﬁed
convolutional neural network classiﬁcation algorithm of motor imagery eeg signals based
on deep learning. Appl. Sci. 10, 1605. doi: 10.3390/app10051605
Li, J., Zhang, Z., and He, H. (2016). “Implementation of EEG emotion recognition
system based on hierarchical convolutional neural networks,” in International Conference
on Brain Inspired Cognitive Systems (Springer), 22–33.
Li, Y., Yang, H., Li, J., Chen, D., and Du, M. (2020). EEG-based intention
recognition with deep recurrent-convolution neural network: performance and channel
selection by grad-cam. Neurocomputing 415, 225–233. doi: 10.1016/j.neucom.2020.
07.072
Liu, J., Wu, G., Luo, Y., Qiu, S., Yang, S., Li, W., et al. (2020). EEG-based emotion
classiﬁcation using a deep neural network and sparse autoencoder. Front. Syst. Neurosci.
14, 43. doi: 10.3389/fnsys.2020.00043
Liu, Y., Ding, Y., Li, C., Cheng, J., Song, R., Wan, F., et al. (2020). Multi-channel eeg-
based emotion recognition via a multi-level features guided capsule network. Comput.
Biol. Med. 123, 103927. doi: 10.1016/j.compbiomed.2020.103927
Lotte, F., Bougrain, L., Cichocki, A., Clerc, M., Congedo, M., Rakotomamonjy, A., et al.
(2018). A review of classiﬁcation algorithms for eeg-based brain-computer interfaces: a
10 year update. J. Neural Eng. 15, 031005. doi: 10.1088/1741-2552/aab2f2
Mai, N.-D., Long, N. M. H., and Chung, W.-Y. (2021). “1D-CNN-based bci system
for detecting emotional states using a wireless and wearable 8-channel custom-designed
EEG headset,” in 2021 IEEE International Conference on Flexible and Printable Sensors
and Systems (FLEPS) (Manchester: IEEE), 1–4.
Maiorana,
E.
(2020).
Deep
learning
for
eeg-based
biometric
recognition.
Neurocomputing 410, 374–386. doi: 10.1016/j.neucom.2020.06.009
Mammone, N., Ieracitano, C., and Morabito, F. C. (2021). “Mpnnet: a motion planning
decoding convolutional neural network for EEG-based brain computer interfaces,” in
2021 International Joint Conference on Neural Networks (IJCNN) (Shenzhen: IEEE), 1–8.
Mao, Z., Yao, W. X., and Huang, Y. (2017). “EEG-based biometric identiﬁcation with
deep learning,” in 2017 8th International IEEE/EMBS Conference on Neural Engineering
(NER) (Shanghai: IEEE), 609–612.
Mattioli, F., Porcaro, C., and Baldassarre, G. (2022). A 1D CNN for high accuracy
classiﬁcation and transfer learning in motor imagery eeg-based brain-computer interface.
J. Neural Eng. 18, 066053. doi: 10.1088/1741-2552/ac4430
Miao, M., Hu, W., Yin, H., and Zhang, K. (2020). Spatial-frequency feature learning and
classiﬁcation of motor imagery eeg based on deep convolution neural network. Comput.
Math. Methods Med. 2020, 1981728. doi: 10.1155/2020/1981728
Nathan, K., and Contreras-Vidal, J. L. (2016). Negligible motion artifacts in scalp
electroencephalography (eeg) during treadmill walking. Front. Hum. Neurosci. 9, 708.
doi: 10.3389/fnhum.2015.00708
Nguyen, T.-H., and Chung, W.-Y. (2018). A single-channel ssvep-based bci speller
using deep learning. IEEE Access 7, 1752–1763. doi: 10.1109/ACCESS.2018.2886759
Oh, S. L., Hagiwara, Y., Raghavendra, U., Yuvaraj, R., Arunkumar, N., Murugappan,
M., et al. (2020). A deep learning approach for parkinson’s disease diagnosis from EEG
signals. Neural Comput. Appl. 32, 10927–10933. doi: 10.1007/s00521-018-3689-5
Olivas-Padilla, B. E., and Chacon-Murguia, M. I. (2019). Classiﬁcation of multiple
motor imagery using deep convolutional neural networks and spatial ﬁlters. Appl. Soft
Comput. 75, 461–472. doi: 10.1016/j.asoc.2018.11.031
Ozdemir, M. A., Degirmenci, M., Guren, O., and Akan, A. (2019). “EEG based
emotional state estimation using 2-d deep learning technique,” in 2019 Medical
Technologies Congress (TIPTEKNO) (Izmir: IEEE), 1–4.
Pan, J., Li, Y., and Wang, J. (2016). “An EEG-based brain-computer interface for
emotion recognition,” in 2016 International Joint Conference on Neural Networks (IJCNN)
(Vancouver, BC: IEEE), 2063–2067.
Pedroni,
A.,
Bahreini,
A.,
and
Langer,
N.
(2019).
Automagic:
standardized
preprocessing
of
big
eeg
data.
Neuroimage
200,
460–473.
doi: 10.1016/j.neuroimage.2019.06.046
Penchina, B., Sundaresan, A., Cheong, S., Grace, V., Valero-Cabré, A., and
Martel, A. (2020). Evaluating deep learning EEG-based anxiety classiﬁcation in
adolescents with autism for breathing entrainment BCI. Brain Inform. 8, 13.
doi: 10.21203/rs.3.rs-112880/v1
Petoku, E., and Capi, G. (2021). “Object movement motor imagery for EEG based BCI
system using convolutional neural networks,” in 2021 9th International Winter Conference
on Brain-Computer Interface (BCI) (Gangwon: IEEE), 1–5.
Polat, H., and Özerdem, M. S. (2020). “Automatic detection of cursor movements
from the eeg signals via deep learning approach,” in 2020 5th International Conference
on Computer Science and Engineering (UBMK) (Diyarbakir: IEEE), 327–332.
Puengdang, S., Tuarob, S., Sattabongkot, T., and Sakboonyarat, B. (2019). “EEG-based
person authentication method using deep learning with visual stimulation,” in 2019 11th
International Conference on Knowledge and Smart Technology (KST) (Phuket: IEEE),
6–10.
Qiao, W., and Bi, X. (2019). “Deep spatial-temporal neural network for classiﬁcation
of eeg-based motor imagery,” in Proceedings of the 2019 International Conference on
Artiﬁcial Intelligence and Computer Science, 265–272.
Rahman, M. M., Sarkar, A. K., Hossain, M. A., Hossain, M. S., Islam, M. R., Hossain,
M. B., et al. (2021). Recognition of human emotions using eeg signals: a review. Comput.
Biol. Med. 136, 104696. doi: 10.1016/j.compbiomed.2021.104696
Rammy, S. A., Abrar, M., Anwar, S. J., and Zhang, W. (2020). “Recurrent deep learning
for eeg-based motor imagination recognition,” in 2020 3rd International Conference on
Advancements in Computational Sciences (ICACS) (Lahore: IEEE), 1–6.
Reddy, T. K., Arora, V., Gupta, V., Biswas, R., and Behera, L. (2021). EEG-based
drowsiness detection with fuzzy independent phase-locking value representations using
lagrangian-based deep neural networks. IEEE Trans. Syst. Man Cybern. Syst. 52, 101–111.
doi: 10.1109/TSMC.2021.3113823
Roy, S., McCreadie, K., and Prasad, G. (2019). “Can a single model deep learning
approach enhance classiﬁcation accuracy of an EEG-based brain-computer interface?” in
2019 IEEE International Conference on Systems, Man and Cybernetics (SMC) (Bari: IEEE),
1317–1321.
Saha, P., Fels, S., and Abdul-Mageed, M. (2019). “Deep learning the eeg manifold
for phonological categorization from active thoughts,” in ICASSP 2019-2019 IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP) (Brighton,
UK: IEEE), 2762–2766.
Sakkalis, V. (2011). Review of advanced techniques for the estimation of
brain connectivity measured with eeg/meg. Comput. Biol. Med. 41, 1110–1117.
doi: 10.1016/j.compbiomed.2011.06.020
Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N., and Wolpaw, J. R. (2004).
Bci2000: a general-purpose brain-computer interface (BCI) system. IEEE Trans. Biomed.
Eng. 51, 1034–1043. doi: 10.1109/TBME.2004.827072
Frontiers in Computational Neuroscience
16
frontiersin.org

Hossain et al.
10.3389/fncom.2022.1006763
Shoeibi, A., Khodatars, M., Ghassemi, N., Jafari, M., Moridian, P., Alizadehsani, R.,
et al. (2021). Epileptic seizures detection using deep learning techniques: a review. Int. J.
Environ. Res. Public Health 18, 5780. doi: 10.3390/ijerph18115780
Song, Y., Wang, D., Yue, K., Zheng, N., and Shen, Z.-J. M. (2019). “EEG-based
motor imagery classiﬁcation with deep multi-task learning,” in 2019 International Joint
Conference on Neural Networks (IJCNN) (Budapest: IEEE), 1–8.
Sulaiman, N., Taib, M. N., Lias, S., Murat, Z. H., Aris, S. A. M., and Hamid, N. H.
A. (2011). “EEG-based stress features using spectral centroids technique and k-nearest
neighbor classiﬁer,” in 2011 UkSim 13th International Conference on Computer Modelling
and Simulation (Cambridge, UK: IEEE), 69–74.
Sundaresan, A., Penchina, B., Cheong, S., Grace, V., Valero-Cabré, A., and
Martel, A. (2021). Evaluating deep learning eeg-based mental stress classiﬁcation
in adolescents with autism for breathing entrainment bci. Brain Inform. 8, 1–12.
doi: 10.1186/s40708-021-00133-5
Tabar, Y. R., and Halici, U. (2016). A novel deep learning approach for classiﬁcation of
eeg motor imagery signals. J. Neural Eng. 14, 016003. doi: 10.1088/1741-2560/14/1/016003
Tang, X., Zhao, J., Fu, W., Pan, J., and Zhou, H. (2019). “A novel classiﬁcation algorithm
for MI-EEG based on deep learning,” in 2019 IEEE 8th Joint International Information
Technology and Artiﬁcial Intelligence Conference (ITAIC) (Chongqing: IEEE), 606–611.
Tang, Z., Li, C., and Sun, S. (2017). Single-trial eeg classiﬁcation of motor imagery using
deep convolutional neural networks. Optik 130, 11–18. doi: 10.1016/j.ijleo.2016.10.117
Tayeb, Z., Fedjaev, J., Ghaboosi, N., Richter, C., Everding, L., Qu, X., et al. (2019).
Validating deep neural networks for online decoding of motor imagery movements from
eeg signals. Sensors 19, 210. doi: 10.3390/s19010210
Tiwari, S., Goel, S., and Bhardwaj, A. (2021). Midnn-a classiﬁcation approach for the
eeg based motor imagery tasks using deep neural network. Appl. Intell. 52, 4824–4843.
doi: 10.1007/s10489-021-02622-w
Tortora, S., Ghidoni, S., Chisari, C., Micera, S., and Artoni, F. (2020). Deep learning-
based bci for gait decoding from eeg with lstm recurrent neural network. J. Neural Eng.
17, 046011. doi: 10.1088/1741-2552/ab9842
Turner, J., Page, A., Mohsenin, T., and Oates, T. (2014). “Deep belief networks used on
high resolution multichannel electroencephalography data for seizure detection,” in 2014
AAAI Spring Symposium Series.
Vallabhaneni, R. B., Sharma, P., Kumar, V., Kulshreshtha, V., Reddy, K. J., Kumar, S. S.,
et al. (2021). Deep learning algorithms in eeg signal decoding application: a review. IEEE
Access 9, 125778–125786. doi: 10.1109/ACCESS.2021.3105917
Vilamala, A., Madsen, K. H., and Hansen, L. K. (2017). “Deep convolutional neural
networks for interpretable analysis of EEG sleep stage scoring,” in 2017 IEEE 27th
International Workshop on Machine Learning For Signal Processing (MLSP) (Tokyo:
IEEE), 1–6.
Völker, M., Schirrmeister, R. T., Fiederer, L. D., Burgard, W., and Ball, T. (2018). “Deep
transfer learning for error decoding from non-invasive EEG,” in 2018 6th International
Conference on Brain-Computer Interface (BCI) (Gangwon: IEEE), 1–6.
Wang, B., Wong, C. M., Wan, F., Mak, P. U., Mak, P. I., and Vai, M. I. (2009).
“Comparison of diﬀerent classiﬁcation methods for eeg-based brain computer interfaces:
a case study,” in 2009 International Conference on Information and Automation (Zhuhai;
Macau: IEEE), 1416–1421.
Wang, J., and Wang, M. (2021). Review of the emotional feature extraction and
classiﬁcation using eeg signals. Cognit. Rob. 1, 29–40. doi: 10.1016/j.cogr.2021.04.001
Wilaiprasitporn,
T.,
Ditthapron,
A.,
Matchaparn,
K.,
Tongbuasirilai,
T.,
Banluesombatkul, N., and Chuangsuwanich, E. (2019). Aﬀective eeg-based person
identiﬁcation using the deep learning approach. IEEE Trans. Cognit. Dev. Syst. 12,
486–496. doi: 10.1109/TCDS.2019.2924648
Xu, H., and Plataniotis, K. N. (2016). “Aﬀective states classiﬁcation using EEG and
semi-supervised deep learning approaches,” in 2016 IEEE 18th International Workshop
on Multimedia Signal Processing (MMSP) (Montreal, QC: IEEE), 1–6.
Yang, J., Ma, Z., Wang, J., and Fu, Y. (2020). A novel deep learning scheme for
motor imagery EEG decoding based on spatial representation fusion. IEEE Access 8,
202100–202110. doi: 10.1109/ACCESS.2020.3035347
Yin, Z., Zhao, M., Wang, Y., Yang, J., and Zhang, J. (2017). Recognition of emotions
using multimodal physiological signals and an ensemble deep learning model. Comput.
Methods Programs Biomed. 140, 93–110. doi: 10.1016/j.cmpb.2016.12.005
Zeng, H., Yang, C., Dai, G., Qin, F., Zhang, J., and Kong, W. (2018). Eeg
classiﬁcation of driver mental states by deep learning. Cogn. Neurodyn. 12, 597–606.
doi: 10.1007/s11571-018-9496-y
Zgallai, W., Brown, J. T., Ibrahim, A., Mahmood, F., Mohammad, K., Khalfan, M.,
et al. (2019). “Deep learning ai application to an EEG driven BCI smart wheelchair,” in
2019 Advances in Science and Engineering Technology International Conferences (ASET)
(Dubai: IEEE), 1–5.
Zhang, C., Kim, Y.-K., and Eskandarian, A. (2021). Eeg-inception: an accurate and
robust end-to-end neural network for EEG-based motor imagery classiﬁcation. J. Neural
Eng. 18, 046014. doi: 10.1088/1741-2552/abed81
Zhang, H., Yang, H., and Guan, C. (2013). Bayesian learning for spatial ﬁltering
in an EEG-based brain-computer interface. IEEE Trans. Neural Netw. Learni. Syst. 24,
1049–1060. doi: 10.1109/TNNLS.2013.2249087
Zhang, R., Xu, P., Guo, L., Zhang, Y., Li, P., and Yao, D. (2013). Z-score linear
discriminant analysis for eeg based brain-computer interfaces. PLoS ONE 8, e74433.
doi: 10.1371/journal.pone.0074433
Zhang, X., Yao, L., Huang, C., Gu, T., Yang, Z., and Liu, Y. (2017). Deepkey:
an EEG and gait based dual-authentication system. arXiv preprint arXiv:1706.01606.
doi: 10.48550/arXiv.1706.01606
Zhang, X., Yao, L., Kanhere, S. S., Liu, Y., Gu, T., and Chen, K. (2018a). Mindid: Person
identiﬁcation from brain waves through attention-based recurrent neural network. Proc.
ACM Interact. Mobile Wearable Ubiquitous Technol. 2, 1–23. doi: 10.1145/3264959
Zhang, X., Yao, L., Sheng, Q. Z., Kanhere, S. S., Gu, T., and Zhang, D. (2018b).
“Converting your thoughts to texts: Enabling brain typing via deep feature learning
of EEG signals,” in 2018 IEEE International Conference on Pervasive Computing and
Communications (PerCom) (Athens: IEEE), 1–10.
Zhang, X., Yao, L., Zhang, S., Kanhere, S., Sheng, M., and Liu, Y. (2018c). Internet
of things meets brain-computer interface: A uniﬁed deep learning framework for
enabling human-thing cognitive interactivity. IEEE Internet Things J. 6, 2084–2092.
doi: 10.1109/JIOT.2018.2877786
Zhao, X., Zhang, H., Zhu, G., You, F., Kuang, S., and Sun, L. (2019). A multi-branch 3d
convolutional neural network for EEG-based motor imagery classiﬁcation. IEEE Trans.
Neural Syst. Rehabil. Eng. 27, 2164–2177. doi: 10.1109/TNSRE.2019.2938295
Zhu, H., Forenzo, D., and He, B. (2022). On the deep learning models for EEG-based
brain-computer interface using motor imagery. IEEE Trans. Neural Syst. Rehabil. Eng. 30,
2283–2291. doi: 10.1109/TNSRE.2022.3198041
Frontiers in Computational Neuroscience
17
frontiersin.org
