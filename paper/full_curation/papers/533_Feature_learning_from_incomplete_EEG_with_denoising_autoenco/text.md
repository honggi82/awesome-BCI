# arXiv:1410.0818v1[cs.CV]3Oct2014

## Feature Learning from Incomplete EEG with Denoising Autoencoder

##### Junhua Lia,∗, Zbigniew Struzika, Liqing Zhangb, Andrzej Cichockia

aLaboratory for Advanced Brain Signal Processing, Brain Science Institute, RIKEN, Saitama, 351-0198, Japan bKey Laboratory of Shanghai Education Commission for Intelligent Interaction and Cognitive Engineering, Department of Computer Science and Engineering, Shanghai Jiao Tong University, Shanghai, 200240, China

#### Abstract

An alternative pathway for the human brain to communicate with the outside world is by means of a brain computer interface (BCI). A BCI can decode electroencephalogram (EEG) signals of brain activities, and then send a command or an intent to an external interactive device, such as a wheelchair. The eﬀectiveness of the BCI depends on the performance in decoding the EEG. Usually, the EEG is contaminated by diﬀerent kinds of artefacts (e.g., electromyogram (EMG), background activity), which leads to a low decoding performance. A number of ﬁltering methods can be utilized to remove or weaken the eﬀects of artefacts, but they generally fail when the EEG contains extreme artefacts. In such cases, the most common approach is to discard the whole data segment containing extreme artefacts. This causes the fatal drawback that the BCI cannot output decoding results during that time. In order to solve this problem, we employ the Lomb-Scargle periodogram to estimate the spectral power from incomplete EEG (after removing only parts contaminated by artefacts), and Denoising Autoencoder (DAE) for learning. The proposed method is evaluated with motor imagery EEG data. The results show that our method can successfully decode incomplete EEG to good eﬀect.

Keywords: Brain Computer Interface, Spectral Power Estimation, Denoising

∗Corresponding Author Email address: juhalee.bcmi@gmail.com (Junhua Li )

Preprint submitted to Neurocomputing October 6, 2014

Autoencoder, Motor Imagery, Incomplete EEG

#### 1. Introduction

The combination of advanced neurobiology and engineering creates a new pathway, namely a brain computer interface (BCI). The BCI provides a bridge connecting the human brain to the outside world [1]. This means that people do

5 not have to rely on the conventional pathway of an intent initialized in the brain being passed to muscles through peripheral nerves, and are able to interact directly with the external environment [2]. Due to the lack of involvement of peripheral nerves and muscles, with the aid of a BCI system, disabled people could restore their abilities of communication [3] and the degenerated motor

10 function [4, 5]. During the past two decades, a variety of BCI systems have been created for diﬀerent applications. These BCI systems are generally divided into two types: active BCI and passive BCI, according to the level of interaction with external stimuli. In the case of a passive BCI, when using a steady-state visual evoked potential (SSVEP) BCI [6], the user may, for example, simply

15 stare at an intended digital number shown on a screen to dial a phone number. When a steady-state ﬂicker is replaced with an occasional ﬂicker, a diﬀerent type of BCI called P300 can be used to output letters by hierarchical selections [3]. Compared to the passive BCI, the active BCI is more natural. Users can express their intents whenever they want to, rather than according to a pre-

20 deﬁned timing arrangement or external cooperation, as with the passive BCI. For instance, people with paraplegia can regain movement in a wheelchair by motor imagery [4], or can control a computer cursor in virtual 2D [7] or 3D [8] environments through brain modulation. Moreover, BCI is also used to develop prostheses, with which disabled people can, for example, move an object [9] or

25 drink a cup of coﬀee [10]. More recently, BCI has been applied to facilitate rehabilitation [11, 12]. Besides applications for disabled people, BCI also has promising applications for healthy persons, especially in the ﬁeld of entertainment. BCI is employed to control video games instead of conventional inputs

such as a keyboard and joystick [13]. In this way, healthy people can enjoy the

30 experience of manipulating virtual objects in a manner diﬀerent from that used in daily life. From the application point of view, the user experience is very important. This requires smoothness in the manipulation of the BCI system. In order to meet this requirement, the BCI system needs to translate brain activities into output

35 information continuously without any interruption. In other words, this requires all the EEG segments to be present for the decoding. If some of the EEG segments are discarded due to extreme noise contamination, the BCI cannot generate the corresponding output during that period. Hence, it would be good to be able to utilize the remaining portion of the aﬀected EEG segment, after

40 only removing the part directly aﬀected by noise. In general, spectral power features are usually utilized to distinguish diﬀerent motor imageries (e.g., lefthand and right-hand motor imageries) [14, 15, 16, 17], as they are considered to be robust for the representation of the contents of motor imageries. If the segment is complete (continuous), the Fourier transform can be well used to

45 transform temporal data points into the spectral domain. This fails in the case of incomplete data, such as an EEG segment with a portion (or portions) of data removed (unevenly spaced). In order still to utilize such segments of EEG with arbitrary portions of data removed and provide users with an experience of smooth manipulation, we employ the Lomb-Scargle periodogram to estimate

50 the spectral power [18, 19], and Denoising Autoencoder (DAE) [20, 21] based neural network or support vector machine (SVM) [22, 23] to predict the classes of motor imageries. The results show that the proposed method is suitable for decoding incomplete EEG in a BCI system.

#### 2. Methodology

55 We ﬁrst employed the Lomb-Scargle periodogram [18, 19] to estimate band powers from incomplete EEG signals. Next, the extracted features were used to train an unsupervised DAE [20, 21] or a supervised SVM with Radial Basis

Function (RBF) kernel [22, 23]. In the case of DAE, the mapping weights of DAE were used to initialize a neural network. After ﬁne-tuning the weights, this

60 trained neural network was used to recognize the classes of motor imageries. Fig. 1 illustrates the proposed method.

Output

### DAE

2

z

L ( , )

f

y

120

120

g2, (y)

g1, ( fˆ)

Initialization

fˆ f

z

qD

56

Input

56

56

Corruption

|External Device|
|---|

|recognition| |
|---|---|
| | |

|SVM|DAE|
|---|---|

| | |
|---|---|
|BCI System| |

|Lomb-Scargle Periodogram|
|---|

Feature Extraction

| | |
|---|---|
|EEG Acquisition| |

| | |
|---|---|
|Preprocessing| |

FPZ

FP1 FP2

AFz AF 4

AF 3

F8

F7

F2 F4 F6

F5 F3 F1

FZ

FC 1 FC 2 FC 4 FC 6 FT 8

FT 7 FC 5 FC 3

FC Z

C2 C4 C6 T8

CZ

T7 C5 C3 C1

CP Z

CP 2 CP 4 CP 6

CP 5 CP 3 CP 1

TP 8

TP 7

P2 P4 P6

P5 P3 P1

PZ

P8

P7

PO4 PO6

PO5 PO3

POZ

PO8 CB 2

PO7

CB 1

O1

O2

OZ

Figure 1: Schematic depiction of the proposed method.

2.1. Lomb-Scargle Periodogram

A four-second trial is divided into 25 segments of one-second length with an overlap of 87.5%. A segment is denoted by X, which is N by T matrix, where

65 N is the number of channels, and T is the number of sampling points. The spectral power of each channel time series y(ti) is estimated by the Lomb-Scargle periodogram [18, 19]. The estimated spectral power at frequency Ωf can be obtained by minimizing the following sum of diﬀerence squares:

Let

min

a>0 φ∈[0, 2π]

T

(y(ti) − α cos(Ωfti + φ))2 . (1)

i=1

- a = α cosφ (2)

70 and

- b = −α sinφ . (3)

We can then rewrite equation (1) as:

min

a, b

T

(y(ti) − acos(Ωfti) − bsin(Ωfti))2. (4)

i=1

The optimal parameters aˆ and ˆb can be obtained through minimizing equation

(4)  

  = R−1r, (5)

aˆ ˆb

where

 

  cos(Ωfti) sin(Ωfti) , (6)

T

cos(Ωfti) sin(Ωfti)

R =

i=1

75 and

  y(ti) . (7)

 

T

cos(Ωfti) sin(Ωfti)

r =

i=1

The power of speciﬁc frequency Ωf is then estimated with respect to optimal parameters aˆ, ˆb as follows:

 

 

 

  a ˆ ˆb

2

cos(Ωfti) sin(Ωfti)

T

1 T

i=1

 

 

(8)

aˆ ˆb

= T1 a ˆ ˆb R

= T1 rT(Ωf)R−1(Ωf)r(Ωf) .

Similarly, the minimization of squares mentioned above is used to estimate spectral powers at all frequencies. After that, spectral estimation for one channel is

80 completed. These steps are repeated for all channels and all segments to obtain the spectral powers. Because the frequency range of 8-30 Hz is mostly related to the motor imagery task [17], we divided this band into four subbands with a bandwidth of 5 Hz (i.e., 8-12 Hz, 13-17 Hz, 18-22 Hz, and 23-27 Hz). Subband powers were obtained by averaging spectral powers within the corresponding

85 frequency band range for each channel. Then, subband powers (four features for each channel) for all channels were concatenated into a feature vector:

F = [f11, f12, f13, f14, f21, f22, f23, f24,···, fN1, fN2, fN3, fN4]T , (9)

where N is the number of channels. Subsequently, features were normalized as:





fqp N

fqp = log

. (10)

 

 

4

fij

i=1

j=1

The normalized features were then fed into a neural network with DAE initialization, or into an SVM classiﬁer to distinguish which class the current EEG

90 segment belongs to.

2.2. DAE-based neural network

For a time, neural networks were less frequently used due to the drawback that they easily became stuck in the local minima, so more use was made of SVM classiﬁer. However, recently neural networks have regained popularity,

95 in particular when using a pre-training strategy [21, 24, 25]. In this paper, we construct a three-layer neural network with DAE initialization (A neural network with more layers might possibly achieve a better performance through in-depth feature learning). The power features extracted by Lomb-Scargle Periodogram was ﬁrst corrupted,

100 denoted as fˆ, by means of a stochastic mapping fˆ∼ qD(fˆ|f). The part enclosed by the orange rectangle in Fig. 1 shows a schematic diagram of the DAE. We

set the corrupted elements to 0. Then, the corrupted features were mapped to a hidden representation (120 units) by the sigmoid function

y = g1, θ(fˆ) = s(W · fˆ+ b). (11)

Consequently, we reconstructed the uncorrupted z as

z = g2, θ (y). (12)

105 The objective was to train parameters θ = {W,b} and θ = {W ,b } for minimization of the average reconstruction error over a training set. In other words, to ﬁnd the parameters to let z be as close as possible to f, we performed the following optimization:

1 n

[θ∗,θ ∗] = arg min

θ, θ

1 n

= arg min

θ, θ

n

L(f(i), z(i))

i=1

n

L(f(i), g2, θ (g1, θ(fˆ(i)))),

i=1

(13)

where L is a squared error loss function L(f,z) = f − z 2, n is the number of

110 training samples, and θ∗,θ ∗ are the optimal values of θ,θ . Once the optimal parameters were obtained, we were able to use those parameters to initialize a neural network. A top layer was added onto the neural network. After that, the parameters were ﬁne-tuned in a supervised way.

#### 3. Evaluation Data

115 Two diﬀerent categories of data are used to prove the feasibility of the proposed method. One is the simulated data and the other is the two-class motor imagery data. We use simulated data to illustrate systematically that spectral power can be correctly estimated when the data become unevenly spaced after removing some data points from them. Further, we use real motor imagery data

120 to demonstrate that classiﬁcation accuracy does not dramatically decrease when increasing the percentage of data within the segment that has been removed, so that the proposed method is useful to process incomplete data in a BCI system. The simulated data were generated by mixing two sinusoidal signals, which were

3 Hz and 6 Hz, respectively. The maximal amplitude of the 3 Hz sinusoidal sig-

125 nal was 1.5 times that of the 6 Hz sinusoidal signal. The motor imagery data came from three subjects. Fourteen electrodes (shown with a green background in the scalp illustration in Fig. 1) were used to record the EEG signal on the sensorimotor cortex while the subject was conducting motor imagery at a sampling rate of 250 Hz. Those electrodes were referenced at the mastoids behind

130 the ears and grounded at AFz. Each subject participated in four sessions. Each session consisted of 15 trials, each of which was four seconds long. The subject conducted either left hand motor imagery or right hand motor imagery according to the cue shown on the computer monitor.

#### 4. Results

##### 135 4.1. Simulated data

0 % data points removal

| |
|---|

400

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

30% data points removal

| |
|---|

400

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

60% data points removal

| |
|---|

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

10% data points removal

| |
|---|

400

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

40% data points removal

400

| |
|---|

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

70% data points removal

400

| |
|---|

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

20% data points removal

| |
|---|

400

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

50% data points removal

| |
|---|

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

80% data points removal

| |
|---|

400

300

P(f)

200

100

0

0 1 2 3 4 5 6 7 8

f (Hz)

Figure 2: Spectral power estimations for the complete signal and signals after data point removal.

We ﬁrst evaluated the performance of the spectral power estimation on simulated data. The simulated data was mixed with two sinusoidal signals, which

were 3 Hz and 6 Hz, respectively. The spectral power estimated from the complete signal, and the incomplete signals with diﬀerent proportional removal of

140 data points (from 10% to 80% with an interval of 10%) are shown in Fig. 2. The data points were removed at random. In order to keep the same scale over cases with diﬀerent proportional data removal to facilitate comparisons between them, the powers shown in Fig. 2 were normalized by dividing by a proportional factor (1-p, where p is the percentage of data removed). For example, the esti-

145 mated power is divided by a factor of 0.7 when 30% of data points are removed from the signal. From Fig. 2, we can see that the components at 3 Hz and 6 Hz can be well estimated in all cases with diﬀerent proportions of data removal, even up to removal of 80% of data points.

4.2. Real motor imagery data

150 In general, BCI encounters a common problem that there is no output when the whole segment has to be discarded due to partial noise contamination in that

60% Data Removal (Point Form) CP6

- CP4

- CP2 CPz CP1
- CP3

CP5 C6

- C4 C2 Cz C1 C3
- C5

0 100 200 300 400 500 600 700 800 900 1000

Time (ms)

###### Figure 3: An example of data point removal. The data points shown with a grey background are removed while data points shown with a white background are retained.

segment. If a method can obtain comparable recognition accuracy (the same or slightly worse) by using only the remaining portion of the segment (the portion from which noise contamination has been removed), this method is considered

155 as an eﬀective solution to the aforementioned problem.

60% Data Removal (Block Form) CP6

- CP4

- CP2 CPz CP1
- CP3

CP5 C6

- C4 C2 Cz C1 C3
- C5

0 100 200 300 400 500 600 700 800 900 1000

Time (ms)

Figure 4: An example of block point removal. The data points shown with a grey background are removed, while data points shown with a white background are retained.

For real motor imagery data, two ways were used to randomly remove the partial data from the segment. One is that data points within a segment were randomly removed (see Fig. 3 for an example). The other is that data blocks within a segment were randomly removed (see Fig. 4 for an example). The width of the

160 blocks removed was generated according to a normal distribution with a mean of 20 and a standard deviation of 10. We used the data from the preceding session to train the SVM classiﬁer with a RBF kernel, and tested it with the data from the following session. Two approaches were used for the evaluation of the accuracy (i.e., sliding time window

165 accuracy and trial accuracy). Sliding time window accuracies were calculated as the number of segments classiﬁed as correct divided by the total number

- Subject 1 Session 02 Subject 1 Session 03

Subject 2 Session 02

- Subject 2 Session 03 Subject 2 Session 04
- Subject 3 Session 02 Subject 3 Session 03
- Subject 3 Session 04

100 80 60 40 20 0

100 80 60 40 20 0

|Trial Acc<br><br>STW Acc|
|---|

|Trial Acc<br><br>STW Acc|
|---|

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

Subject 1 Session 04

100 80 60 40 20 0

100 80 60 40 20 0

Trial Acc

STW Acc

|Trial Acc<br><br>STW Acc|
|---|

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

100 80 60 40 20 0

100 80 60 40 20 0

Trial Acc

Trial Acc

STW Acc

STW Acc

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

100 80 60 40 20 0

100 80 60 40 20 0

Trial Acc

Trial Acc

STW Acc

STW Acc

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

100 80 60 40 20 0

Trial Acc

STW Acc

|Trial Acc<br><br>STW Acc|
|---|

0% 10% 20% 30% 40% 50% 60% 70% 80%

Figure 5: Classiﬁcation accuracies for the form of data point removal. The thin red lines represent trial accuracies, and the bold blue lines represent sliding time window accuracies.

of segments. A trial was classiﬁed as belonging to the class to which most of the sliding time windows within that trial belonged. Then trial accuracies were obtained according to the ratio of trials classiﬁed as correct. Fig. 5 and Fig.

170 6 show test accuracies for the conditions of data point removal and data block removal, respectively. In general, the accuracies for all sessions of all subjects did not dramatically decrease. Trial accuracies varied more than sliding time window accuracies across diﬀerent proportional sections of data removal. This is because a trial was classiﬁed as correct even if the number of sliding time

175 windows in the trial classiﬁed as correct was only one more than the number of sliding time windows classiﬁed as incorrect. Likewise, trials with one more incorrect sliding time window than correct sliding time window were classiﬁed

Subject 1 Session 03

Subject 1 Session 02

100

100

Trial Acc

STW Acc

80 60 40 20 0

80 60 40 20 0

|Trial Acc<br><br>STW Acc|
|---|

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

Subject 1 Session 04 Subject 2 Session 02

100

100

Trial Acc

STW Acc

80 60 40 20 0

80 60 40 20 0

|Trial Acc<br><br>STW Acc|
|---|

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

- Subject 2 Session 03 Subject 2 Session 04
- Subject 3 Session 02 Subject 3 Session 03

100

100

Trial Acc

Trial Acc

STW Acc

STW Acc

80 60 40 20 0

80 60 40 20 0

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

100

100

Trial Acc

Trial Acc

STW Acc

STW Acc

80 60 40 20 0

80 60 40 20 0

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

Subject 3 Session 04

100 80 60 40 20 0

Trial Acc

|Trial Acc<br><br>STW Acc|
|---|

STW Acc

0% 10% 20% 30% 40% 50% 60% 70% 80%

Figure 6: Classiﬁcation accuracies for the form of block point removal. The thin red lines represent trial accuracies, and the bold blue lines represent sliding time window accuracies.

as incorrect. Therefore, in some cases, the trial accuracy changed greatly while the accuracy of the sliding time widows did not change much. A comparable

180 classiﬁcation accuracy could be achieved even when 80% of data were removed. High accuracies were retained no matter how many data points were removed - in the range from 10% to 80% - for subject 1, especially for sessions 2 and 3. The accuracies for 80% data removal were substantially worse than those for 70% data removal for subject 1 in the condition of block data removal. It

185 appears that our method is relatively sensitive to data removal in block form.

4.3. Comparison between DAE and SVM

In this section, we show a comparison between DAE and SVM in terms of classiﬁcation accuracy of sliding time windows. SVM has been widely adopted since its conception and has been successfully applied in many ﬁelds. Deep learning

190 is a promising and burgeoning method. DAE is utilized as a building brick to compose a deep learning network. It is meaningful to illustrate the eﬀectiveness of this for EEG feature recognition using our paradigm. The parameters used in the training are listed in Table 1. Fig. 7 shows the accuracy diﬀerence between DAE and SVM for each session of each subject under the condition of

195 data point removal. Asterisks located above the zero horizontal line mean that the accuracy of DAE is higher than that of SVM. The bars shown on the right of each sub-plot are the average diﬀerences. The bottom right plot illustrates the overall diﬀerence averaged across all sessions of all subjects. From Fig. 7, we can see that there is no clear winner - the DAE is better than the SVM in

200 a number of sessions but turns out to be worse in other sessions. The overall average accuracy of DAE is still better than that of SVM. Fig. 8 shows the accuracy comparison under the condition of block point removal. The result is similar to the condition of data point removal. The overall average accuracy of DAE is higher than that of SVM under the condition of block point removal,

205 but the increase in accuracy of DAE compared with SVM is less than the case of data point removal.

Table 1: Parameter Settings

|Parameters<br><br>|Values|
|---|---|
|Corrupted fraction Mini-batch size Learning rate for pre-training Number of pre-training epochs Learning rate for ﬁne-tuning Number of ﬁne-tuning epochs|0.3 25 0.9 20 0.9 50<br><br>|

- Subject 1 Session 02 Subject 1 Session 03

Subject 2 Session 02

- Subject 2 Session 03 Subject 2 Session 04
- Subject 3 Session 02 Subject 3 Session 03
- Subject 3 Session 04

- −4

−2

0

2

- 4

−6

−4

−2

0

2

0

- 5

10

15

20

−5

0

5

10

- −5

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

Subject 1 Session 04

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

10

10

5

0

0

−10

−20

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

10

10

5

5

0

0

−5

−5

−10

−10

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

20

- 0

- 1 DAE SVM

10

0

−1

−10

0% 10% 20% 30% 40% 50% 60% 70% 80%

Figure 7: Accuracy comparison between DAE and SVM under the condition of data point removal. Each asterisk represents an accuracy diﬀerence between the DAE and the SVM. The diﬀerence is calculated by the DAE accuracy minus the corresponding SVM accuracy. The bar at the right of each plot illustrates the average diﬀerence in a session.

From the results of comparisons, the DAE is shown to be comparable to the SVM. However, it is possible that the DAE can outperform the SVM when more layers are used and parameters are better tuned. It is not yet clear whether the

210 DAE can signiﬁcantly exceed the SVM in terms of EEG classiﬁcation, but there

- Subject 1 Session 02 Subject 1 Session 03

Subject 2 Session 02

- Subject 2 Session 03 Subject 2 Session 04
- Subject 3 Session 02 Subject 3 Session 03
- Subject 3 Session 04

5

5

0

0

−5

−5

−10

−10

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

Subject 1 Session 04

5

20

15

0

10

−5

5

0

−10

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

10

10

5

0

0

−10

−5

−10

−20

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

20

10

5

10

0

0

−5

−10

−10

0% 10% 20% 30% 40% 50% 60% 70% 80%

0% 10% 20% 30% 40% 50% 60% 70% 80%

10

- 0

- 1 DAE SVM

5

0

−1

−5

0% 10% 20% 30% 40% 50% 60% 70% 80%

Figure 8: Accuracy comparison between DAE and SVM under the condition of block point removal. Graphical symbol expressions are the same as in Fig. 7.

has been a report that stacked DAE (i.e., multiple DAEs combined together to obtain deeper learning of features) performed better than the SVM on the image benchmark dataset named MNIST [20].

#### 5. Conclusion

215 We propose the combination of the Lomb-Scargle periodogram and either SVM or DAE to distinguish incomplete EEG segments (i.e., segments from which a portion of data has been removed due to noise contamination). The results indicate that classiﬁcation accuracy is not dramatically decreased when diﬀerent percentages of data are removed. Therefore, the classiﬁcation performance using

220 the proposed method for incomplete segments is acceptable for a BCI application system. This means that the segment with noise contamination can still be utilized to output commands after only removing the noisy portion, instead of discarding the whole segment, as is conventionally done in BCI systems. In brief, the proposed method can achieve comparable classiﬁcation performance

225 even when most of the data points in a segment have been removed. It provides an alternative solution for the frequent problem occurring in a BCI system that there is no output when a segment is discarded.

#### 6. Acknowledgments

The work of Liqing Zhang was supported by the national natural science foun230 dation of China (Grant No. 91120305, 61272251).

References

References

[1] A. Ortiz-Rosario, H. Adeli, Brain-computer interface technologies: from signal to action, Reviews in the Neurosciences 24 (5) (2013) 537–552.

235 [2] J. R. Wolpaw, N. Birbaumer, W. J. Heetderks, D. J. McFarland, P. H. Peckham, G. Schalk, E. Donchin, L. A. Quatrano, C. J. Robinson, T. M. Vaughan, et al., Brain-computer interface technology: a review of the ﬁrst international meeting, IEEE Transactions on Rehabilitation Engineering 8 (2) (2000) 164–173.

240 [3] K.-R. Mu¨ller, M. Tangermann, G. Dornhege, M. Krauledat, G. Curio, B. Blankertz, Machine learning for real-time single-trial EEG-analysis: from brain–computer interfacing to mental state monitoring, Journal of Neuroscience methods 167 (1) (2008) 82–90.

- [4] J. Li, J. Liang, Q. Zhao, J. Li, K. Hong, L. Zhang, Design of assistive

245 wheelchair system directly steered by human thoughts, International journal of Neural Systems 23 (3) (2013) 1350013.

- [5] G. Pfurtscheller, G. R. Mu¨ller, J. Pfurtscheller, H. J. Gerner, R. Rupp, Thought–control of functional electrical stimulation to restore hand grasp in a patient with tetraplegia, Neuroscience Letters 351 (1) (2003) 33–36.

250 [6] G. Bin, X. Gao, Z. Yan, B. Hong, S. Gao, An online multi-channel SSVEP-based brain–computer interface using a canonical correlation analysis method, Journal of Neural Engineering 6 (4) (2009) 046002.

[7] D. J. McFarland, G. W. Neat, R. F. Read, J. R. Wolpaw, An EEG-based method for graded cursor control, Psychobiology 21 (1) (1993) 77–81.

255 [8] D. J. McFarland, W. A. Sarnacki, J. R. Wolpaw, Electroencephalographic (EEG) control of three-dimensional movement, Journal of Neural Engineering 7 (3) (2010) 036007.

[9] G. R. Mu¨ller-Putz, R. Scherer, G. Pfurtscheller, R. Rupp, EEG-based neu-

roprosthesis control: a step towards clinical practice, Neuroscience Letters 260 382 (1) (2005) 169–174.

[10] L. R. Hochberg, D. Bacher, B. Jarosiewicz, N. Y. Masse, J. D. Simeral, J. Vogel, S. Haddadin, J. Liu, S. S. Cash, P. van der Smagt, et al., Reach and grasp by people with tetraplegia using a neurally controlled robotic arm, Nature 485 (7398) (2012) 372–375.

265 [11] J. J. Daly, J. R. Wolpaw, Brain–computer interfaces in neurological rehabilitation, The Lancet Neurology 7 (11) (2008) 1032–1043.

[12] Y. Liu, M. Li, H. Zhang, H. Wang, J. Li, J. Jia, Y. Wu, L. Zhang, A tensor-based scheme for stroke patients motor imagery EEG analysis in bci-fes rehabilitation training, Journal of Neuroscience Methods 222 (2014)

270 238–249.

[13] J. Li, Y. Liu, Z. Lu, L. Zhang, A competitive brain computer interface: Multi-person car racing system, in: Engineering in Medicine and Biology Society (EMBC), 2013 35th Annual International Conference of the IEEE, IEEE, 2013, pp. 2200–2203.

275 [14] R. Palaniappan, Utilizing gamma band to improve mental task based braincomputer interface design, Neural Systems and Rehabilitation Engineering, IEEE Transactions on 14 (3) (2006) 299–303.

[15] G. Pfurtscheller, C. Guger, G. Mu¨ller, G. Krausz, C. Neuper, Brain oscil-

lations control hand orthosis in a tetraplegic, Neuroscience Letters 292 (3) 280 (2000) 211–214.

- [16] J. Li, L. Zhang, Bilateral adaptation and neurofeedback for brain computer interface system, Journal of Neuroscience Methods 193 (2) (2010) 373–379.
- [17] J. Li, L. Zhang, Active training paradigm for motor imagery BCI, Experimental Brain Research 219 (2) (2012) 245–254.

285 [18] N. R. Lomb, Least-squares frequency analysis of unequally spaced data, Astrophysics and Space Science 39 (2) (1976) 447–462.

[19] P. Stoica, J. Li, H. He, Spectral analysis of nonuniformly sampled data: a new approach versus the periodogram, Signal Processing, IEEE Transactions on 57 (3) (2009) 843–858.

290 [20] P. Vincent, H. Larochelle, Y. Bengio, P.-A. Manzagol, Extracting and composing robust features with denoising autoencoders, in: Proceedings of the 25th International Conference on Machine Learning, ACM, 2008, pp. 1096– 1103.

- [21] P. Vincent, H. Larochelle, I. Lajoie, Y. Bengio, P.-A. Manzagol, Stacked

295 denoising autoencoders: Learning useful representations in a deep network with a local denoising criterion, The Journal of Machine Learning Research 11 (2010) 3371–3408.

- [22] V. Vapnik, The nature of statistical learning theory, Springer, 2000.
- [23] M. A. Hearst, S. Dumais, E. Osman, J. Platt, B. Scholkopf, Support vector

300 machines, Intelligent Systems and their Applications, IEEE 13 (4) (1998) 18–28.

- [24] D. Erhan, Y. Bengio, A. Courville, P.-A. Manzagol, P. Vincent, S. Bengio, Why does unsupervised pre-training help deep learning?, The Journal of Machine Learning Research 11 (2010) 625–660.

305 [25] X. Glorot, A. Bordes, Y. Bengio, Domain adaptation for large-scale sentiment classiﬁcation: A deep learning approach, in: Proceedings of the 28th International Conference on Machine Learning (ICML-11), 2011, pp. 513–520.

Junhua Li received his Ph.D. degree from the Department of Computer

310 Science and Engineering, Shanghai Jiao Tong University, Shanghai, China, in March 2013. He is currently a research scientist at the Laboratory for Advanced Brain Signal Processing, Brain Science Institute, RIKEN, Japan. His research interests include signal processing, brain computer interface, and machine learning. He has been a member of IEEE since 2013, and was a student member of

315 IEEE in 2012.

Zbigniew R. Struzik received a Master of Science in Engineering degree in technical physics from the Warsaw University of Technology, Poland, in 1986, and a Doctor degree from the faculty of Mathematics, Computer Sci-

320 ence, Physics and Astronomy at the University of Amsterdam, the Netherlands, in 1996. From 1997 to 2003, he worked at the Centre for Mathematics and Computer Science (CWI), Amsterdam, and since 2003 has worked at the University

of Tokyo, Japan, where he is currently aﬃliated. From 2012, his main position has been at RIKEN Brain Science Institute in Wakoshi, Japan. His scientiﬁc

325 work contributed to the amalgamation of (multi-)fractal analysis, wavelet analysis and time series data mining. His current research interests include applications of information science and statistical physics in life sciences, complexity and emergence, time series processing and mining, and recently, analytic approaches to elucidating the nature of creative processes in art and science, in

330 particular in neuroscience. He is on the editorial board of the Fractals Journal, the Open Medical Informatics Journal, Frontiers in Fractal Physiology, Frontiers in Computational Physiology and Medicine, Frontiers in Human Neuroscience, International Journal of Statistical Mechanics, Journal of Neuroscience Methods and Integrative Medicine International Journal. He has co-authored over one

335 hundred journal papers and book chapters.

Liqing Zhang received the Ph.D. degree from Zhongshan University, Guangzhou,

China, in 1988. He was promoted in 1995 to the position of full professor at South China University of Technology. He worked as a research scientist at

340 RIKEN Brain Science Institute, Japan from 1997 to 2002. He is now a Professor with Department of Computer Science and Engineering, Shanghai Jiao Tong University, Shanghai, China. His current research interests cover computational theory for cortical networks, brain-computer interface, perception and cognition computing model, statistical learning and inference. He has published

345 more than 170 papers in international journals and at conferences.

Andrzej Cichocki received Ph.D. and Dr.Sc. (Habilitation) degrees, in electrical engineering, from Warsaw University of Technology (Poland). He is currently the senior team leader head of the laboratory for Advanced Brain

350 Signal Processing, at RIKEN Brain Science Institute (JAPAN).

He is a co-author of more than 250 technical papers and 4 monographs (two of them translated to Chinese). According to a 2011 analysis, he is a co-author of one of the top 1% most highly cited papers in his ﬁeld worldwide.

