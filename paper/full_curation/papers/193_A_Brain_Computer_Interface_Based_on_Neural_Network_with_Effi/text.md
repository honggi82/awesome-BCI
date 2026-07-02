# A Brain Computer Interface Based on Neural Network with Efﬁcient Pre-Processing

Kenji Nakayama Kiyoto Inagaki ∗Graduate School of Natural Science and Technology, Kanazawa Univ. Kakuma-machi, Kanazawa, 920-1192, Japan Tel: +81-76-234-4896, Fax: +81-76-234-4900 E-mail: nakayama@t.kanazawa-u.ac.jp

VR world, and to have many kinds of experiences in the VR world. For instance, training to avoid danger situations may be possible by using the BCI technology.

Abstract—Brain Computer Interface (BCI) is one of hopeful interface technologies between human and machine. However, brain waves are very weak and there exist many kinds of noises. Therefore, what kinds of features are useful, how to extract the useful features, how to suppress noises, and so on are very important.

Approaches to the BCI technology includes nonlinear classiﬁcation by using spectrum power, adaptive auto-regressive model and linear classiﬁcation, space patterns and linear classiﬁcation, hidden Markov models, and so on [4]. Furthermore, application of neural networks have been also discussed [3],[5],[7],[10],[11].

On the other hand, neural networks are very useful technology for pattern classiﬁcation. Especially, multilayer neural networks trained through the error back-propagation algorithm have been widely used in a wide variety of ﬁeld.

In this paper, the neural network is applied to the BCI. Amplitude of the FFT of the brain waves are used for the input data. Several kinds of techniques are introduced in this paper. Segmentation along the time axis for fast response, nonlinear normalization for emphasizing important information with small magnitude, averaging samples of the brain waves for suppressing noise effects and reduction in the number of the samples for achieving a small size network, and so on are newly introduced.

In this paper, the multilayer neural network is applied to the BCI. Especially, efﬁcient pre-processing techniques are introduced in order to achieve high probability of correct mental task classiﬁcation. Simulation were carried out by using the brain waves, which are available from the web site of Colorado state university. Estimation results of the proposed method are compared to the conventional methods [12],[13].

Simulation was carried out by using the brain waves, which are available from the web site of Colorado state university. The number of mental tasks is ﬁve. Ten data sets for each mental task are prepared. Among them, 9 data sets are used for training, and the rest one data set is used for testing. Selection of the one data set for testing is changed and accuracy of the correct classiﬁcations are averaged over the possible selections. Approximately, 80% of correct classiﬁcation of the brain waves is obtained, which is higher than the conventional.

II. MENTAL TASKS AND BRAIN WAVE MEASUREMENT

- A. Mental Tasks

In this paper, the brain waves, which are available from the web site of Colorado state university [1], are used. The following ﬁve kinds of mental tasks are used as imaging.

- • Baseline (B)
- • Multiplication (M)
- • Letter-composing (L)
- • Rotation of 3-D object (R)
- • Counting numbers (C)

- B. Brain Wave Measurement

I. INTRODUCTION

Nowadays, several kinds of interfaces between human and computers or machines have been proposed and developed. For persons being in a healthy condition, the keyboard and the mouse are useful and practical interface. On the other hand, for handicapped persons, several interface techniques, which use available organs and functions, have been studied and developed.

Location of the electrodes to measure brain waves is shown in Fig.1. Seven channels including C3, C4, P3, P4, O1, O2, EOG, are used. EOG is used for measuring movement of the eyeballs.

Among the interfaces developed for the handicapped persons, Brain Computer Interface (BCI) has been attractive recently. Brain waves are ﬁrst analyzed and classiﬁed. Mental tasks, which a subject images, are estimated. Furthermore, based on the estimated mental task, computers and machines are controlled [9].

The brain waves are measured for 10 sec and sampled by 250Hz for each mental task. Therefore, 10sec × 250Hz = 2,500 samples are obtained for one channel and one mental task. One data set includes seven cahnnels. One example of the brain wave is shown in Fig.2.

For one application, it can be expected that heavy handicapped persons, who cannot control any parts of their own body, control a wheelchair, computers and other machines through the BCI [6]. Furthermore, in the virtual reality (VR) technology, it may be possible to control a person states in the

III. PRE-PROCESSING A. Segmentation along Time Axis

In order to make the BCI responce fast, the brain wave measured during 10sec is divided into the segments with

front

left C3 C4 right

P3 P4 O1 O2

back

Fig. 1. Location of seven channel electrodes.

20

| |
|---|

15

10

5

amplitude

0

−5

−10

−15

−20

0 2 4 6 8 10

time[sec]

Fig. 2. Example of brain waves.

C. Reduction of Samples by Averaging

In order to make the neural network compact and to reduce effects of the noises, the FFT samples in some interval are averaged. The averages are used for the neural network input. The number of samples is reduced to 20. The amplitude of the FFT for the reduced samples is also shown in Fig.4.

- D. Nonlinear Normalization

The amplitude of the FFT is widely distributed. Small samples also contain important information for classifying the mental tasks. However, in the neural networks, large inputs play an important role. If large samples do not include important information, correct classiﬁcation will be difﬁcult. For this reason, the nonlinear normalization as shown in Eq.(1) and Fig.5 is employed in this paper. The small samples are expanded and the large samples are compressed.

f(x) =

log(x − min+1) log(max−min+1)

(1)

| |
|---|

- 0
- 1

MIN MAX x

f(x)

- Fig. 5. Nonlinear normalization. Horizontal axis is input and vertical axis is output.

E. Input of Neural Network

Since the amplitude response is symmetrical, only the right hand side is used. Furthermore, the amplitude response of the seven channels are simultaneously applied to the neural network. An example of the neural network input is shown in Fig.6. In this ﬁgure, the left hand side shows the input before the nonlinear normalization, and the right hand side is that after normalization.

|ch1|ch2|ch3|ch4|ch5|ch6|ch7|
|---|---|---|---|---|---|---|

10 20 30 40 50 60 70

0

50

100

150

200

|ch1|ch2|ch3|ch4|ch5|ch6|ch7|
|---|---|---|---|---|---|---|

10 20 30 40 50 60 70

0

0.2

0.4

0.6

- 0.8
- 1

- Fig. 6. Input of neural network including 7-channels. Left hand side: Before normalization, Right hand side: After normalization.

0.5sec length as shown in Fig.3. The segmentation is shifted by 0.25sec. This means the segment with 0.5sec length can be obtained every 0.25sec.

0.5 sec 0.5 sec 0.5 sec 0.5 sec ...

{{{

...

{

Fig. 3. Segmentation of brain wave along time axis.

- B. Amplitude of FFT of Brain Waves

What kinds of features should be used to classify the brain waves and to estimate the corresponding mental task is very important. In order to avoid effects of time delay, which is not essential, the brain wave is Fourier transformed and its amplitude is used to express feature of the brain wave. The segment of the brain wave with 0.5 sec length includes 125 samples. The amplitude of the FFT of the segment is shown in Fig.4.

500

200

| |
|---|

| |
|---|

400

150

300

100

200

50

100

0

0

−125 0 125

−125 0 125

frequency[Hz]

frequency[Hz]

Fig. 4. Amplitude of FFT of segment with 0.5sec length. Left: 125 samples, Right: 20 samples of averaging.

IV. MENTAL TASK CLASSIFICATION BY USING NEURAL NETWORK

A multilayer neural network having a single hidden layer is used. Activation functions used in the hidden layer and the output layer are sigmoid functions. The number of input nodes is 10samples×7-channels=70. Five output neurons are used for ﬁve mental tasks. Therefore, only one output neuron will respond to the applied input data. In the training phase, the target for the output is binary, like (1, 0, 0, 0, 0). In the testing phase, the maximum output becomes the winner and the corresponding mental task is assigned. However, when the winner have small value, estimation becomes incorrect. Therefore, the answer of the neural network is rejected, that is any mental task cannot be estimated. The error back-propagation algorithm is employed for adjusting the connection weights.

V. SIMULATION CONDITIONS

- A. Training and Testing Brain Waves

The brain waves with 10sec length for ﬁve mental tasks were measured 10 times. Therefore, 10 data sets are available. Among them, 9 data sets are used for training and the rest one data set is used for testing. Five data sets are selected as the testing data set. Thus, 5 independent trials were carried out, and classiﬁcation accuracy is evaluated based on the average over 5 trials [2].

- B. Probability of Correct and Error Classiﬁcations Estimation of the mental tasks is evaluated based on prob-

ability of correct classiﬁcation (Pc) and error classiﬁcation (Pe).

Pc =

Nc Nt

(2)

Pe =

Ne Nt

(3) Nt = Nc + Ne + Nr (4)

Rate =

Pc Pc + Pe

(5)

In the above equations, Nc is the number of correct classiﬁcations, Ne is the number of error classiﬁcations, and Nr is the number of rejections.

- C. Parameters in Neural Network Learning

- • The number of hidden neurons: 20
- • A learning rate: 0.2
- • Initial weights: Random numbers in -0.1∼+0.1
- • The threshold for rejection: 0.8
- • The number of iterations: 5000

VI. SIMULATION RESULTS A. Effects of Number of Samples

Before the segmentation, effects of the number of samples, that is the amplitude of FFT, is investigated. The successive samples are averaged and this average is used to express the amplitude. The number of samples is reduced from 2,500 to 250, 100, 50, 20. Since, the amplitude of FFT for real

signal is symmetrical, then a half number of them is actually used. Figure 7 shows the learning curves for mental task classiﬁcation. In this ﬁgure, fcorrect classiﬁcation ratef, that is Pc, is the average over ﬁve mental tasks. From this result, the number of samples of 20 is best.

- 0.8

- 1

20

50

correctclassificationrate

0.6

100 250

0.4

0.2

0

0 1000 2000 3000 4000 5000

iteration

Fig. 7. Learning curves of mental classiﬁcation for training and testing data. The number of samples is varied from 250 to 20.

Table I shows the number of correct and error classiﬁcations and their probability.

TABLE I NUMBER OF CORRECT AND ERROR CLASSIFICATIONS AND THEIR

PROBABILITY WITH 20 SAMPLES.

|Mental Task| |B<br><br>|M<br><br>|L<br><br>|R|C<br><br>|Reject| |Pc<br><br>|Pe|
|---|---|---|---|---|---|---|---|---|---|---|
|Baseline| |7|0<br><br>|0<br><br>|0<br><br>|0|3| |70.0<br><br>|0.0|
|Multiplication| |0|8<br><br>|0<br><br>|0|0<br><br>|2| |80.0<br><br>|0.0|
|Letter-composing| |0|0<br><br>|7<br><br>|0<br><br>|0|3| |70.0|0.0|
|Rotation| |0<br><br>|0|0<br><br>|8|0<br><br>|2| |80.0<br><br>|0.0|
|Counting| |0<br><br>|0|0<br><br>|0<br><br>|9|1| |90.0<br><br>|0.0|

B. Effects of Segmentation

Aim of the segmentation is to make the BCI response fast. On the other hand, the length is limited to 0.5 sec for example. In this section, effects of this short length is investigated. As described in the previous section, The 10 sec length of the brain waves is divided into 0.5 sec, which has 125 samples. The learning curves are shown in Fig.8.

1.0

Learning Test

correctclassificationrate

0.8

0.6

0.4

0.2

0.0

0 1000 2000 3000 4000 5000 iteration

Fig. 8. Learning curves for segmentation.

Furthermore, the probability of correct and error classiﬁcations and their rate, that is Pc, Pe and Rate, are shown in Tabel II. The probabilies were averaged over the iterations from 4,001 to 5,000. From these results, accuracy of the segmentation is almost the same as that of using all data.

TABLE II PROBABILITY OF CORRECT AND ERROR CLASSIFICATIONS AND THIR

RATES FOR SEGMENTATION.

| | |TRaining data| | | |Testing data| | |
|---|---|---|---|---|---|---|---|---|
| | |Pc<br><br>|Pe|Rate| |Pc|Pe<br><br>|Rate|
|Segmentation| |99.7|0.1<br><br>|0.99| |79.7|10.5|0.88|
|No Segmentation| |100.0<br><br>|0.0|1.00| |78.0<br><br>|0.0<br><br>|1.00|

- C. Effects of Nonlinear Normalization

Effects of the nonlinear normalization given by Eq.(1) on the mental task classiﬁcation accuracy is investigated. For reference, linear normalization, by which the sample values are linearly normalized from 0 to 1, is also used for reference. The segmentation is used, and 125 samples are reduced to 20 samples by averaging.

The learning curves are shown in Fig.9

0.0

0.2

0.4

0.6

0.8

1.0

0 2000 4000 6000 8000 10000

non-linear

linear

iteration

correctclassificationrate

Fig. 9. Learning curves for nonlinear normalization.

Furthermore, the probability of correct and error classiﬁcations and their rate are shown in Table III. From these results, the nonlinear normalization can make convergence of the learning fast, and the probability can be also improved.

TABLE III PROBABILITY OF CORRECT AND ERROR CLASSIFICATIONS AND THIR

RATES FOR NONLINEAR NORMALIZATION.

| | |TRaining data| | | |Testing data| | |
|---|---|---|---|---|---|---|---|---|
|Normalization| |Pc<br><br>|Pe|Rate| |Pc<br><br>|Pe<br><br>|Rate|
|Nonlinear| |99.7|0.1|0.99| |79.7|10.5<br><br>|0.88|
|Linear| |81.8<br><br>|1.9<br><br>|0.98| |68.4<br><br>|9.8<br><br>|0.88|

- D. Threshold for Rejection

When the winner output has small value, the estimation by the neural network is not accurate. Therefore, the result is rejected. In this section, effects of the threshold for rejection is investigated. The probability of correct and error classiﬁcations and their rates are listed in Table IV. By setting the threshold to be low, Pc can be improved, however, Pe is also increased at the same time. In some applications, Pe should be minimized while the rejection can permitted to some extent. In these cases, high threshold is prefered. Like this, the optimum threshold is highly dependent on applications, to which the BCI system is applied.

- E. Comparison to Conventional Methods

The same brain waves were used in [3]. The coefﬁcients of a 6-th order auto-regression model are used for the neural

TABLE IV PROBABILITY OF CORRECT AND ERROR CLASSIFICATIONS AND THIR

RATES BY CHANGING THRESHOLD.

|Threshold| |Pc|Pe<br><br>|Rate|
|---|---|---|---|---|
|0.8| |80.3<br><br>|10.0<br><br>|0.89|
|0.6| |81.7<br><br>|11.9|0.87|
|0.4| |82.9<br><br>|13.2|0.86|
|0.2| |83.7<br><br>|14.2|0.86|
|0.0| |84.5|15.5<br><br>|0.84|

network input. The data length of 10 sec is also divided into 0.5 sec segments. The probability of correct classiﬁcations is from 30% to 60% for four subjects. Therefore, the proposed method, which employs the amplitude response of the FFT, the nonlinear normalization, the averaging and the rejection, can provide higher probability of correct mental classiﬁcation.

VII. CONCLUSION

A neural network has been applied to the BCI problem. In order to improve accuracy of mental task classiﬁcation, several kinds of pre-processing to generate the input data of the neural network. Compared with the conventional methods, the probability of correct classiﬁcation has been increased.

REFERENCES

- [1] Colorado State University: http://www.cs.colostate.edu/eeg/
- [2] C. Anderson and Z. Sijercic, “Classiﬁcation of EEG Signals from Four Subjects During Five Mental Tasks, “EANN’96, ed. by Bulsari, A.B., Kallio, S., and Tsaptsinos, D., Systems Engineering Association, PL 34, FIN-20111 Turku 11, Finland, pp. 407-414, 1996.
- [3] J. R. Millan, J. Mourino, F. Babiloni, F. Cincotti, M. Varsta, and J. Heikkonen,”Local neural classiﬁer for EEG-based recognition of metal tasks,”IEEE-INNS-ENNS Int. Joint Conf. Neural Networks, July 2000.
- [4] G. Pfurtscheller and C. Neuper, “ Motor imagery and direct braincomputer communication, “ Proc. IEEE, vol. 89, no. 7, pp. 1123-1134, July 2001.
- [5] K. R. Muller, C. W. Anderson, and G. E. Birch,” Linear and non-linear methods for brain-computer interfaces,”IEEE Trans. Neural Sys. Rehab. Eng., vol. 11, no. 2, pp. 165-169, 2003.
- [6] B. Obermaier, G. R. Muller, and G. Pfurtscheller, “Virtual keyboard controlled by spontaneous EEG activity, “ IEEE Trans. Neural Sys. Rehab. Eng., vol. 11, no. 4, pp.422-426, Dec. 2003.
- [7] J. R. Millan, “ On the need for on-line learning in brain-computer interfaces, “ Proc. IJCNN, pp. 2877-2882, 2004.
- [8] G. E. Fabiani, D. J. McFarland, J. R. Wolpaw, and G. Pfurtscheller, “Conversion of EEG activity into cursor movement by a brain-computer interface (BCI), “IEEE Trans. Neural Sys. Rehab. Eng., vol. 12, no. 3, pp. 331-338, Sept. 2004.
- [9] G. Pfurtscheller, C. Neuper, C. Guger, W. Harkam, H. Ramoser, A. Schl¨ogl, B. Obermaier, and M. Pregenzer, “Current trends in Graz braincomputer interface (BCI) research,” IEEE Trans. Rehab. Engng., vol.8, pp.216-219, 2000.
- [10] B. Obermaier, C. Neuper, C. Guger, and G. Pfurtscheller, “Information transfer rate in a ﬁve-classes brain-computer interface,” IEEE Trans.Neural Sys. Rehab. Eng., vol.9, no.3, pp.283-288, 2001.
- [11] C.W. Anderson, S.V. Devulapalli, and E.A. Stolz, “Determining mental state from EEG signals using neural networks,” Scientiﬁc Programming, Special Issue on Applications Analysis, Vol.4, No.3, pp.171-183, Fall, 1995.
- [12] K.Inagaki and K.Nakayama, “Mental task classiﬁcation based on brain waves by using neural network”, IEICE, Technical Report, Vol.105, No.174, SIP2005-54, pp.25-30, July 2005. (in Japanese)
- [13] K.Inagaki and K.Nakayama,”On brain computer interface by using multilayer neural network”, IEICE, 20th Signal Processing Symposium, Dec. 2005 (in Japanese).

