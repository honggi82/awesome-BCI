## Source Aware Deep Learning Framework for Hand Kinematic Reconstruction using EEG Signal

Sidharth Pancholi∗, Member, IEEE, Amita Giri∗, Student Member, IEEE, Anant Jain, Student Member, IEEE, Lalan Kumar, Member, IEEE, and Sitikantha Roy, Member, IEEE

### arXiv:2103.13862v3[eess.SP]4Jan2022

Abstract—The ability to reconstruct the kinematic parameters of hand movement using non-invasive electroencephalography (EEG) is essential for strength and endurance augmentation using exosuit/exoskeleton. For system development, the conventional classiﬁcation based brain computer interface (BCI) controls external devices by providing discrete control signals to the actuator. A continuous kinematic reconstruction from EEG signal is better suited for practical BCI applications. The state-of-the-art multi-variable linear regression (mLR) method provides a continuous estimate of hand kinematics, achieving maximum correlation of upto 0.67 between the measured and the estimated hand trajectory. In this work, three novel source aware deep learning models are proposed for motion trajectory prediction (MTP). In particular, multi layer perceptron (MLP), convolutional neural network - long short term memory (CNNLSTM), and wavelet packet decomposition (WPD) CNN-LSTM are presented. Additional novelty of the work includes utilization of brain source localization (using sLORETA) for the reliable decoding of motor intention. The information is utilized for channel selection and accurate EEG time segment selection. Performance of the proposed models are compared with the traditionally utilised mLR technique on the real grasp and lift (GAL) dataset. Effectiveness of the proposed framework is established using the Pearson correlation coefﬁcient and trajectory analysis. A signiﬁcant improvement in the correlation coefﬁcient is observed when compared with state-of-the-art mLR model. Our work bridges the gap between the control and the actuator block, enabling real time BCI implementation.

Index Terms—BCI, Deep Learning, EEG, Intention Mapping, Motion Trajectory Prediction, Non-Invasive, Source Localization.

I. INTRODUCTION

# E

Lectroencephalography (EEG) signal has been extensively utilized for brain computer interface (BCI) appli-

cations because of its high temporal resolution, non-invasive nature, portability, and cost-effectiveness [1]–[5]. BCI systems facilitates direct connection between the brain and external devices that do not rely on the peripheral nerves and muscles. Hence, BCI based devices like wearable robots [4], [6],

This work was supported in part by Prime Minister’s Research Fellowship (PMRF), Ministry of Education (MoE), GoI, with project number PLN08/PMRF (to A. Giri) and in part by DRDO - IITD ‘JATC’ with project number RP03830G.

S. Pancholi, A. Giri and A. Jain are with the Department of Electrical Engineering, Indian Institute of Technology, Delhi, India (e-mail: s.pancholi@ieee.org; Amita.Giri@ee.iitd.ac.in; anantjain@ee.iitd.ac.in)

L. Kumar is with the Department of Electrical Engineering and Bharti School of Telecommunication, Indian Institute of Technology, Delhi, India (e-mail: lkumar@ee.iitd.ac.in)

S. Roy is with the Department of Applied Mechanics, Indian Institute of Technology, Delhi, India (e-mail: sroy@am.iitd.ac.in)

∗S. Pancholi and A. Giri contributed equally to this work.

[Figure 1]

Fig. 1: Schematic diagram of EEG signal based BCI system.

exoskeletons [5], [7], [8], and prosthesis [9] have gained focus in the recent years. When such external devices are utilized for strength and endurance augmentation, reconstruction of motion trajectory kinematic parameters from EEG signal becomes important. Reliable decoding of motor intentions and accurate timing of the robotic device actuation is fundamental to optimally enhance the subject’s functional improvement. Since, EEG signal has information about the kinematic parameters prior to the actual movement, this time gain along with correct intention mapping will facilitate the real time control of assistive devices. A schematic diagram of EEG signal based BCI systems is shown in the Fig. 1.

Multi-class classiﬁcation [10], [11] and regression [12] are the two major approaches adopted in EEG based BCI control. Multi-class classiﬁcation based BCI systems utilize feature extraction and classiﬁcation method to maximize the inter-class variance and realize decisive planes that separate distinct classes [13]. However, regression-based techniques provide more natural control of assistive devices through continuous decoding of EEG signal. Brain activity recorded as EEG signal, exhibits non-stationary nature and therefore requires continuous estimation of optimal and stationary features from the signal. Motion trajectory prediction (MTP) from multi-channel EEG signals was proposed in [12] using the multi-variate linear regression (mLR) technique. In particular, Kalman ﬁlter based mLR model was utilized to decode 2D hand movement in the horizontal plane. Mean correlation value of 0.60±0.07 was achieved between the predicted and the measured trajectory. The most adopted hand crafted feature for regression is power spectral density (PSD) from the four

[Figure 2]

Fig. 2: Experimental set-up of reach to grasp movement.

frequency bands that include delta (1-3Hz), theta (5-8Hz), alpha (9-12Hz), and beta (14-31Hz) [14]. In [15], decoding of 3D imagined hand movement trajectory was studied using PSD based band-power time series (BTS) technique. A signiﬁcant improvement in accuracy was observed using BTS input when compared with the standard potentials time-series (PTS) input. The most recent work [16], demonstrated the feasibility of predicting both actual and imagined 3D trajectories of all arm joints from scalp EEG signals using mLR model. However, the limitation of mLR method is that it demands the linear relationship between the independent (observed event) variables and dependent (predicted event) variable. Furthermore, mLR is extremely sensitive to outliers and poor quality data. If the number of outliers relative to the non-outlier data points is greater than a few, the linear regression model deviates from the true underlying relationship.

In the past few years, deep learning a sub-ﬁeld of machine learning has achieved breakthrough accuracies in complex and high dimensional data such as image classiﬁcation [17], emotion recognition [18], and machine translation [19]. Deep learning focuses on computational models that typically learn hierarchical representations of the input data through successive non-linear transformations—termed neural networks. In contrast to mLR, the deep learning models are much more robust to outliers and can access very descriptive (nonlinear) features that deﬁne the underlying relationships fairly well. The convolutional neural network (CNN/ConvNet) has been extensively utilized for BCI applications that include motor imagery (MI) and motor execution (ME) classiﬁcation [20]. The widespread use of CNN algorithms in classiﬁcation application [21], [22] is due to its capability to extract spatial information from EEG signal. However, it intrinsically disregards the temporal information [23]. A very widely known recurrent neural network which effectively utilizes the temporal dependencies based on past information is long short-term memory (LSTM) network [24].

In this work, a basic feed forward neural network called multi layer perceptron (MLP) along with CNN-LSTM based hybrid deep learning framework is proposed for hand kinematics prediction. To the best of authors’ knowledge, CNN itself has not been utilized for MTP. Reconstruction of hand

[Figure 3]

Fig. 3: Time-frequency distribution of FC1, FC5, C3, and CP1 EEG channels.

movement proﬁles using low frequency EEG have been reported in 2D [25] and 3D spaces [26]. These results indicate that detailed limb kinematic information could be present in the low frequency components of EEG, and could be decoded using the proposed models. Hence, an advanced version of CNN-LSTM based on wavelet packet decomposition (WPD) is proposed that decompose the EEG signal into sub-bands with increasing resolution towards the lower frequency band [27], [28]. Additional novelty of the work includes utilization of brain source localization (BSL) for the reliable decoding of motor intention. The information is utilized for channel selection and accurate EEG time segment selection. Electrodes placed over the active brain region corresponding to the hand movement are utilized, rather than all the available sensors data for efﬁcient computation. The selected EEG segment is then utilized in the training and testing of the proposed deep learning model. Hence, the proposed framework is called the source aware deep learning framework for hand kinematics prediction.

The rest of the paper is organized as follows. The details of the experimental data and signal pre-processing steps are covered in Section II. The description of existing state-of-the-art model is presented in Section III. The three proposed source aware deep learning models along with the role of brain source localization in MTP is presented in Section IV. Performance evaluation metric is reported in Section V. Section VI provides a detailed discussion of the results followed by conclusions of our work.

II. EXPERIMENTAL DATA AND PRE-PROCESSING

In this work, WAY-EEG-GAL (Wearable interfaces for hAnd function recoverY- EEG - grasp and lift) data-set [29] is utilized for MTP. Scalp EEG recordings were collected from twelve healthy subjects for right hand movement. In this experiment, the task to be executed was to reach and grasp the object and lift it stably for a couple of seconds. The participant can then lower the object at its initial position and retract the arm back to resting position. The data acquisition set up for the same is illustrated in Fig. 2. A series of such reach to grasp and lift trials were executed for various loads and surface

frictions. The beginning of the task and lowering of the object was cued by an LED. The kinematic data was obtained using a position sensor p4 (as shown in Fig. 2) normalized between 0 to 1 with initial position as 0 and maximum as 1. This was done to get rid of error due to initial position perturbation. The pre-processing steps followed is detailed next.

The kinematics and EEG data were down sampled from 500 Hz to 100 Hz. The time-frequency distribution of EEG signal for a particular subject is shown in the Fig. 3 for FC1, FC5, C3, and CP1 channel. It may be noted that the maximum power related to right hand movement is present in the delta (0.5-3 Hz), theta (3-7 Hz), and lower alpha (7-12 Hz) range. Hence, the EEG time series was ﬁrst ﬁltered using zero-phase 4th order Hamming-windowed sinc FIR (ﬁnite impulse response) ﬁlter in the range of delta, theta, and lower alpha bands. Subsequently, ICA algorithm was applied to remove artifacts such as eye movement, eye blink, and power line interference. The common average referencing method was used for rereferencing. The EEG signal was ﬁnally standardized as

vn[t] − νn σn

(1)

Vn[t] =

where Vn[t] is the standardized EEG voltage at time t and at sensor n. There are total N number of EEG electrodes. The mean and standard deviation of vn is represented by νn and σn respectively.

III. THE EXISTING MLR MODEL FOR KINEMATIC DECODING

Multi-variate linear regression has been the state-of-the-art technique for BCI based MTP [12], [16], [26]. In this section, application of mLR in mapping the EEG time series signal to the kinematic parameters in continuous manner, is brieﬂy detailed. The mLR equations for the mapping are as follows [26].

- Px[t] =ax +

N

n=1

L

l=0

b(xnl)Vn[t − l] (2)

- Py[t] =ay +

N

n=1

L

l=0

b(ynl)Vn[t − l] (3)

- Pz[t] =az +

N

n=1

L

b(znl)Vn[t − l] (4)

l=0

Here, Px[t], Py[t], and Pz[t] are the horizontal, vertical, and depth positions of the hand at time sample t, respectively. Vn[t − l] is the standardized voltage at time lag l, where the number of time lags is varied from 0 to L. The regression coefﬁcient a and b are estimated by minimizing the loss function during the training phase. In mLR, the multiple independent variables (Vn[t − l]) contribute to a dependent kinematic variable (Px[t], Py[t], and Pz[t]).

IV. SOURCE AWARE DEEP LEARNING MODELS FOR HAND KINEMATIC RECONSTRUCTION

In this Section, source aware deep learning models for hand kinematic reconstruction are proposed. In particular, MLP,

CNN-LSTM and WPD CNN-LSTM are proposed for the kinematic parameter estimation. As the kinematic movement is embedded in the EEG signature, early detection of intended movement is essential for controlling an external BCI devices for positive real time augmentation. Source localization plays a key role in motor intention mapping. The information is utilized for channel selection and accurate EEG time segment selection. Hence, role of brain source localization on MTP is detailed ﬁrst followed by the model description.

A. Role of Brain Source Localization in MTP

Brain source localization refers to the estimation of active dipole location from noninvasive scalp measurements. It is an ill-posed inverse problem, where the relationship between the EEG scalp potential and neural sources is non-unique, and the solution is highly sensitive to the artifacts. Dipole-ﬁtting and dipole imaging (distributed source model) are two approaches to solve the inverse problem. In the dipole ﬁtting method, small number of active regions are considered in the brain and can be modeled using equivalent dipoles [30], [31]. The dipole ﬁtting is an over-determined approach to BSL and is solved using a nonlinear optimization technique. This includes subspace-based multiple signal classiﬁcation (MUSIC) [32], [33], beamforming [34], and genetic [35] algorithms. On the other hand, the distributed source model assumes that there are a large number of sources conﬁned in an active region of the brain and is solved using linear optimization techniques, such as minimum norm estimation (MNE) [36], weighted MNE (WMNE) [37], low resolution electromagnetic tomography (LORETA) [38], and standardized low resolution brain electromagnetic tomography (sLORETA) [39]. EEG signals have been found to be effective for monitoring changes in the human brain state and behavior [40].

In the present work, sLORETA dipole imaging method is opted for the inverse source localization. In this method, localization inference is performed using images of standardized current density under the constraint of smoothly distributed sources. Source localization plots for the activity under consideration (right hand grasp and lift execution task) are given in Fig. 4. There are total 11 images of cortical surface activation sliced temporally. The result shown corresponds to single trial EEG of the subject 3 and is reproducible for the other trials

- as well. Visual cue for the start of the activity was presented
- at 0ms. It may be noted that the brain region responsible for visual processing (occipital lobe) shows neural activation after 80-120ms of the visual cue (Fig. 4(b)-(c)). Prompted hand movement information was transferred to the sensory motor region at around 200-300ms (Fig. 4(d)-(e)). In response to right hand movement, contralateral motor cortex i.e. left motor cortex gets elucidated at 370-400ms (Fig. 4(f)-(g)). Motor related neural activity is observed thereafter (Fig. 4(h)-(k)). It was observed that the Subject actually performed hand movement at 620-650ms after the cue was shown. Hence, it may be concluded that the EEG source localization can provide the intended hand movement information approximately 350ms prior to the actual hand movement.

The transfer delay of visual cue intention to movement onset is 620-650ms including 350ms delay of sensory motor

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

(a) (b) (c) (d)

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

(e) (f) (g) (h)

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

(i) (j) (k) (l)

- Fig. 4: Brain source localization using sLORETA at different time stamps : (a) 0ms (b) 80ms (c) 100ms (d) 200ms (e) 300ms (f) 370ms (g) 400ms (h) 500ms (i) 600ms (j) 700ms (k) 800ms. (l) Selected 18 channels of maximum activity using BSL.

[Figure 16]

- Fig. 5: Multi-layer perceptron based regression modeling

times more than 700ms are excluded from this study. In a trial, kinematic data is taken from the movement onset and EEG data was taken starting from the LED cue (0ms). The length of EEG and kinematic data were made equal by removing the EEG samples from the end of a trial. In addition to that, electrodes placed over the maximal neural activation region corresponding to the hand movement were utilized. In particular, electrodes on the left hemisphere (Fp1, F7, FC1, T7, C3, TP9, CP1, P7, O1), near the midline (Fz, Cz, Pz) and on the right hemisphere (F8, FC6, C4, CP6, P8, O2) were utilised as shown in Fig. 4(l). Hence, rather than using all the 32 EEG channels for kinematics reconstruction, only 18 channels of maximum activity were chosen. The selected EEG data was utilized in the training and testing of the proposed deep learning model.

B. Model I : Multi-layer Perceptron Model based

Deep learning based models are not much explored in the literature for MTP using EEG signal. However, MLP has been utilized for EEG classiﬁcation [41]. Multi-layer perceptron is ﬁrst proposed herein for trajectory prediction using EEG signal. The model is illustrated in the Fig.5. The building blocks

region activation to actual hand movement. This information is utilized to select trials with a delay of up to 700ms between the LED cue and the actual movement. Trials with response

[Figure 17]

- Fig. 6: Proposed source aware hybrid model I utilizes EEG time series as an input and hybrid model II takes wavelet coefﬁcients for predicting the kinematics of upper limb.

[Figure 18]

Fig. 7: Unfold structure of LSTM network.

of a neural networks are neurons (or perceptron), weights and activation functions. For activation function, rectiﬁed linear unit (ReLU) is employed herein and is deﬁned as

#### F(Ω) = max(0,Ω) (5)

where Ω is the input parameter to the activation function F. The MLP model utilizes a feed-forward neural network consisting of input, hidden and output layers. In particular, there are 3 hidden layers having 300, 100 and 50 perceptrons, in addition to input and output layer. The output of the dth neuron at the ﬁrst hidden layer is given by

D0

h1d = F(b1d +

wi,d0 Vi), d = 1,··· ,D1 (6)

i=1

where b1d is the input bias, D0 is the size of input vector and D1 represents the total number of neuron at ﬁrst hidden layer. wi,d0 is the weight between the ith element of the input Vi to the dth neuron at the ﬁrst hidden layer. Since, every perceptron in each layer of the neural network is connected to every other

perceptron in the adjacent layer, the output of the dth neuron at kth hidden layer can be expressed as

Dk−1

wi,dk−1 hki−1), d = 1,···Dk, (7)

hkd = F(bkd +

i=1

where k = 2,···K represents the hidden layer with a total of K hidden layers. wi,dk−1 is the weight between the ith neuron in the (k − 1)th hidden layer to the dth neuron at the kth hidden layer. The neural network weights are updated using the Adam optimizer. The output of the kth hidden layer can be expressed as

T (8)

#### hk = hk1 hk2 ···hkD

k

The output layer y of the model yields the desired kinematic parameters. The jth element of the output is given by

DK

wi,jK hKi ) (9)

yj = F(bj +

i=1

where bj is the output bias. C. Hybrid Model I : CNN-LSTM based

In this Section, a hybrid deep learning based model is proposed for MTP on the GAL dataset. In particular, CNN and LSTM [42] based deep learning model along with a dense layer is utilized and is shown in Fig. 6. Hybrid model I utilizes the pre-processed EEG with time lag l varying from 0 to L = 10. This is done to enhance the probability of EEG segment corresponding to the observed kinematic data. It is to be noted that the visual stimulus gets reﬂected in occipital lobe only after ∼80ms. Thus, feeding the delayed

EEG segments to the CNN-LSTM model allows the model to learn the weighting parameters correctly. The CNN algorithm is seen to be useful for feature engineering/extraction through layer-by-layer processing [43]. The proposed model makes use of CNN to extract inherent spatial information present in EEG time series. More speciﬁcally, relevant combination of sensors is extracted.

The proposed CNN architecture consists of two 1D convolutional layers with 64 and 32 ﬁlters having kernel size of 15 and 7 respectively. The 1D forward propagation (1D-FP) for the dth neuron of the kth CNN layer is expressed as

Zdk = qdk +

Dk−1

conv1D(Ji,dk−1,Sik−1) (10)

i=1

where qdk is the bias, Dk−1 is the total number of neuron at layer k − 1 and conv1D represents the one dimensional

convolution. The Ji,dk−1 denotes the kernel from the ith neuron at layer k − 1 to the dth neuron at layer k. The output of ith

neuron at (k − 1)th layer is represented by Sik−1. Intermediate output feature is now given by

#### ydk = F(Zdk) (11)

where ydk represents output of dth neuron at layer k. A maxpooling layer for sub-sampling is employed between the two

layers.

Output of the CNN module is fed to the ﬂatten layer for generating the intermediate deep features. The deep features are in turn, input to the LSTM layer. Total 50 cells are used in the LSTM layer for creating enhanced temporal features. The structure of LSTM network for an input feature sequence [f1,f2...fg] is illustrated in the Fig. 7. The hidden state he and activation vector ce at time-step (e = 1,2...g). The LSTM unit utilizes the past state he−1, ce−1 and current state features (fe) to predict the current state output ye. In the whole loop of LSTM, previous information is utilized recursively. The input gate (ie), forget gate (me) and the output gate (oe) parameters of LSTM are deﬁned as

ie = δ(Wi [he−1,fe + ψi]) (12)

me = δ(Wm [he−1,fe + ψm]) (13)

oe = δ(W0 [he−1,fe + ψ0]) (14)

where δ is the logistic sigmoid function, W is the weight matrix and ψ is the bias of each gate. Activation vector and hidden state can now be computed as

ce = ie tanh(Wc [he−1,fe + ψc]) + me ce−1 (15)

he = oe tanh(ce) (16)

where, the represents the point wise multiplication. The ﬁnal output of LSTM layer

#### ye = Wyhe + ψy (17)

becomes the input to the Dense layer. The initial state parameter will be derived after model training for subsequent

predictions. The output of the dense layer neurons could be given by equation (6) with LSTM layer output as the input. The kinematics parameters output can be obtained by the equation (9).

D. Hybrid Model II : WPD CNN-LSTM based

Reconstruction of hand movement proﬁles using low frequency EEG have been reported in 2D [25] and 3D spaces [26]. These results indicate that detailed limb kinematic information could be present in the low frequency components of EEG, and could be decoded using the proposed model. Therefore, an advanced version of CNN-LSTM based on wavelet packet decomposition is proposed that decompose the EEG signal into sub-bands with increasing resolution towards the lower frequency band. It may be noted from Fig. 6 that rather than utilising directly the pre-processed time domain EEG signal, wavelet coefﬁcients of the EEG signal are utilized in hybrid model II by employing wavelet packet decomposition [27], [44]. The WPD, also known as optimal sub-band tree structuring, consists of a tree kind of structure with α0,0 representing the root node or original signal of the tree as shown in Fig. 8. In the generalized node notation αp,r, p denotes the scale and r denotes the sub-band index within the scale. The node αp,r can be decomposed into two orthogonal parts: an approximation space αp,r to αp+1,2r and detailed space αp,r to αp+1,2r+1. This can be performed by dividing orthogonal basis {θp(t − 2pr)}r∈Z of αp,r into two new orthogonal bases {θp+1(t − 2p+1r)}r∈Z of αp+1,2r and {φp+1(t − 2p+1r)}r∈Z of αp+1,2r+1. The scaling function θp,r(t) and the wavelet function φp,r(t) are deﬁned as

1 |2p|

θ

θp,r(t) =

t − 2pr 2p

(18)

t − 2pr 2p

1 |2p|

(19)

φ

φp,r(t) =

The dilation factor 2p, also known as the scaling parameters, measures the degree of compression or scaling. On the other hand, the location parameters 2pr determines the time location of the wavelet function. This method is repeated P times. Total number of samples in the original signal is taken to be T, where P ≤ log2T. This results in P × T coefﬁcients. Therefore, at the level of resolution p, where p = 1,2,...,P, the tree has T coefﬁcients divided into 2p coefﬁcient blocks or crystals. In this work, Daubechies (db1) is selected as mother wavelet. Total 5 decomposition level are utilized for getting better frequency resolution. WPD coefﬁcients generated at each of the WPD tree subspaces corresponding to approx 120 trials are utilised as feature matrix. Thereafter, the same deep learning architecture of CNN-LSTM is utilized as discussed in Subsection IV-C.

To prevent the model from overﬁtting and underﬁtting Kfold cross-validation is the most commonly used technique. In the present work, the number of training samples 65000 (120 trials) are divided into three parts : (i) training data for training

TABLE I: PCC analysis of (a) mLR, (b) MLP, (c) CNN-LSTM model in different frequency bands. WPD CNN-LSTM correlation coefﬁcient is presented in the end coloumn labeled as WPD.

|Subject ID<br><br>|Direction| |Frequency Band<br><br>| | | | | | | | | | | | | | |WPD|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | |Delta (0.5-3 Hz)| | | |Theta (3-7 Hz)| | | |Alpha (7-12 Hz)<br><br>| | | |Entire (0.5-12 Hz)| | | |
| | | |(a)<br><br>|(b)<br><br>|(c)| |(a)<br><br>|(b)<br><br>|(c)| |(a)<br><br>|(b)<br><br>|(c)| |(a)<br><br>|(b)<br><br>|(c)| |

|1|x| |0.36|0.81<br><br>|0.83| |0.35|0.74<br><br>|0.75| |0.21<br><br>|0.54|0.54| |0.43<br><br>|0.78|0.84<br><br>|0.82 0.84|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.42|0.82<br><br>|0.88| |0.24|0.75|0.78| |0.24<br><br>|0.45|0.54| |0.41<br><br>|0.80<br><br>|0.83| |
| |z| |0.18<br><br>|0.75<br><br>|0.80| |0.21|0.68<br><br>|0.61| |0.12|0.22<br><br>|0.22| |0.21|0.62<br><br>|0.81<br><br>|0.81|

|3|x| |0.34<br><br>|0.82|0.81| |0.32|0.77<br><br>|0.74| |0.21<br><br>|0.50|0.51| |0.45<br><br>|0.78|0.84 0.90<br><br>|0.85|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.41<br><br>|0.80<br><br>|0.86| |0.20<br><br>|0.75<br><br>|0.73| |0.25|0.42|0.50| |0.41|0.80<br><br>| |0.89|
| |z| |0.17|0.77|0.80| |0.22|0.66|0.62| |0.11|0.21<br><br>|0.21| |0.23<br><br>|0.63<br><br>|0.82|0.84|

|4|x| |0.32<br><br>|0.82|0.89| |0.35<br><br>|0.72<br><br>|0.78| |0.21|0.54<br><br>|0.52| |0.43<br><br>|0.74<br><br>|0.85 0.91|0.85|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.42<br><br>|0.81|0.87| |0.23|0.74|0.77| |0.23<br><br>|0.46|0.53| |0.42<br><br>|0.74| |0.90|
| |z| |0.18<br><br>|0.70<br><br>|0.77| |0.21|0.68<br><br>|0.60| |0.12|0.22<br><br>|0.21| |0.22<br><br>|0.62<br><br>|0.80<br><br>|0.83|

|5<br><br>|x| |0.33<br><br>|0.79<br><br>|0.83| |0.35<br><br>|0.75|0.76| |0.22<br><br>|0.54|0.53| |0.44<br><br>|0.79|0.85 0.90<br><br>|0.85|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.39|0.80|0.85| |0.23|0.73|0.79| |0.26|0.46<br><br>|0.54| |0.40<br><br>|0.81<br><br>| |0.89|
| |z| |0.19<br><br>|0.70<br><br>|0.75| |0.20<br><br>|0.62<br><br>|0.61| |0.11|0.23|0.21| |0.20<br><br>|0.63<br><br>|0.75<br><br>|0.78|

|6|x| |0.28|0.83<br><br>|0.85| |0.25|0.78<br><br>|0.83| |0.12<br><br>|0.54|0.52| |0.40<br><br>|0.80|0.87 0.91<br><br>|0.86|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.32|0.84<br><br>|0.87| |0.25<br><br>|0.82|0.77| |0.22|0.53<br><br>|0.56| |0.43<br><br>|0.84<br><br>| |0.89|
| |z| |0.13<br><br>|0.53|0.80| |0.11<br><br>|0.51|0.61| |0.06<br><br>|0.30|0.24| |0.12<br><br>|0.61|0.81<br><br>|0.84|

|7<br><br>|x| |0.32|0.71<br><br>|0.83| |0.23|0.56|0.80| |0.23<br><br>|0.54<br><br>|0.57| |0.38|0.77<br><br>|0.83 0.88|0.84 0.88|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.28|0.76<br><br>|0.82| |0.24<br><br>|0.66<br><br>|0.78| |0.25|0.32<br><br>|0.44| |0.41<br><br>|0.74<br><br>| | |
| |z| |0.29<br><br>|0.53|0.78| |0.31<br><br>|0.53|0.62| |0.09<br><br>|0.15<br><br>|0.26| |0.21<br><br>|0.58|0.76<br><br>|0.79|

|10|x| |0.30<br><br>|0.81<br><br>|0.86| |0.32<br><br>|0.61<br><br>|0.82| |0.23|0.46<br><br>|0.51| |0.46<br><br>|0.79<br><br>|0.92|0.91 0.92|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.38|0.82<br><br>|0.89| |0.31<br><br>|0.72<br><br>|0.79| |0.26|0.41|0.50| |0.52<br><br>|0.83<br><br>|0.91| |
| |z| |0.31<br><br>|0.64|0.80| |0.32|0.63<br><br>|0.60| |0.12<br><br>|0.21|0.24| |0.25<br><br>|0.64|0.82|0.86|

|11<br><br>|x| |0.37<br><br>|0.83<br><br>|0.88| |0.40|0.78<br><br>|0.70| |0.26<br><br>|0.64|0.53| |0.44<br><br>|0.82|0.86 0.93<br><br>|0.87|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.43<br><br>|0.83|0.92| |0.41<br><br>|0.80|0.78| |0.28<br><br>|0.52|0.59| |0.43|0.84| |0.91|
| |z| |0.17|0.74<br><br>|0.78| |0.15<br><br>|0.64|0.65| |0.12|0.25<br><br>|0.23| |0.20<br><br>|0.71<br><br>|0.82|0.85|

|12|x| |0.48<br><br>|0.81|0.87| |0.36<br><br>|0.75|0.77| |0.26|0.53|0.49| |0.46<br><br>|0.84|0.87 0.91|0.88|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.52<br><br>|0.81<br><br>|0.85| |0.23<br><br>|0.76<br><br>|0.79| |0.27|0.51<br><br>|0.54| |0.52<br><br>|0.85| |0.89|
| |z| |0.32<br><br>|0.64|0.74| |0.22<br><br>|0.67|0.61| |0.16<br><br>|0.23<br><br>|0.10| |0.28<br><br>|0.74|0.81<br><br>|0.83|

|Average|x| |0.34|0.80|0.85| |0.32<br><br>|0.72|0.77| |0.22|0.54<br><br>|0.52| |0.43<br><br>|0.79<br><br>|0.86 0.90<br><br>|0.86|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| |y| |0.40<br><br>|0.81|0.87| |0.26|0.75<br><br>|0.77| |0.25<br><br>|0.45|0.53| |0.44<br><br>|0.80<br><br>| |0.89|
| |z| |0.21<br><br>|0.67<br><br>|0.78| |0.22<br><br>|0.62<br><br>|0.61| |0.11|0.22<br><br>|0.21| |0.21<br><br>|0.64|0.80|0.82|

the model (70% of the total data), (ii) validation data for hyperparameter tuning (15% of the total data), and (iii) test data for performance evaluation (15% of the total data). To compare the performance of our proposed method (MLP, CNN-LSTM, WPD CNN-LSTM) with existing state-of-the-art techniques (mLR), each model was fed with the same training data. The validation data for all four algorithms were also same. The training and validation data is used to tune the parameters. Once the model was trained, the performance of the model was evaluated on the same test data to ensure that the comparison is fair. Additionally, to make the comparison between the proposed CNN-LSTM and WPD CNN-LSTM model fair, the respective models were built of the same architecture i.e. same number of hidden layers, number of epochs and batch size.

V. PERFORMANCE EVALUATION

Performance of the three proposed source aware deep learning models are compared with the state-of-the-art mLR technique. Effectiveness of the proposed framework is established

[Figure 19]

Fig. 8: Illustration of the three level wavelet packet decomposition.

using the Pearson correlation coefﬁcient (PCC) evaluation metric. Additionally, hand trajectory estimation in 3D space

TABLE II: Comparison with state-of-the-art techniques.

Variation Variation Decoding

References Space

Correlation (mean)

in Load in SF Method Robinson et. al [12] 2D N.A. N.A. mLR (0.60±0.07) Korik et. al. [15] 3D N.A. N.A. mLR x=0.39, y=0.56, z=0.59 Sosnik et. al. [16] 3D N.A. N.A. mLR x=0.25, y=0.50, z=0.48 Model I 3D Yes Yes MLP x=0.79, y=0.80, z=0.64

- Hybrid Model I 3D Yes Yes CNN-LSTM x=0.86, y=0.90, z=0.80
- Hybrid Model II 3D Yes Yes WPD CNN-LSTM x=0.86, y=0.89, z=0.82 Note: Surface Friction (SF), Not Available (N.A.).

[Figure 20]

[Figure 21]

[Figure 22]

(a) (b) (c)

[Figure 23]

[Figure 24]

[Figure 25]

(d) (e) (f)

[Figure 26]

[Figure 27]

[Figure 28]

(g) (h) (i)

Fig. 9: Trajectory estimation in x, y and z direction using the mLR is presented in (a)-(c) respectively, the CNN-LSTM is presented in (d)-(f) respectively, and using the WPD CNN-LSTM is presented in (g)-(i) respectively.

is presented and compared with the ground truth trajectory. A. Pearson Correlation Coefﬁcient Analysis

Pearson correlation coefﬁcient is a linear correlation coefﬁcient that returns a value between −1 to +1. A −1, +1

and 0 PCC value means there is a strong negative, strong positive and zero correlation respectively. Pearson correlation coefﬁcient between measured (A) and estimated (B) kinematic

[Figure 29]

[Figure 30]

(a) (b)

Fig. 10: Trajectory visualization in 3D space: (a) ground truth and (b) predicted trajectory from WPD CNN-LSTM method

parameters of total samples T is expressed as

T

Ai − υA σA

Bi − υB σB

1 T − 1

(20)

Π(A,B) =

i=1

where, υx and σx are the mean and standard deviation of x with x ∈ {A,B}. The PCC analysis for the various approaches to hand kinematics prediction utilizing EEG signal is presented in Table I for the 5 subjects from WAY-EEGGAL dataset. The correlation is presented along the three directions x, y and z. The time-frequency distribution plot for the dataset in Fig. 3 suggests that the EEG frequency power is dominant up to the alpha band. Hence, the PCC analysis is presented in three different frequency bands (Delta, Theta, and Alpha). The correlation was additionally analysed for the entire frequency band. The result is presented for each subject individually along with the average behavior. WPD CNNLSTM utilises the entire frequency spectrum. The three deep learning based models are compared with the state-of-the-art mLR approach. It may be noted that all the deep learning based models performs reasonably well when compared to mLR method for all the subjects and in all the direction. The low correlation in z direction for all the methods is attributed to short and transit movement along this direction.

- The performance of the hybrid model I (CNN-LSTM based) is seen to be better when compared to mLR and MLP techniques.
- The performance of the hybrid model II (WPD CNN-LSTM based) is similar to hybrid model I (CNN-LSTM based) along x and y directions. However, it outperforms all the methods in z direction, achieving higher correlation. Higher correlation in WPD based approach may be attributed to the fact that WPD decomposes the EEG signal into sub-bands with increasing resolution towards lower frequency band.

Source aware deep learning based models (MLP, CNNLSTM and WPD CNN-LSTM) have been additionally compared with existing mLR variants [12], [15], [16]. The comparison is presented in Table II. The three deep learning based models shows superior performance when compared to the

existing mLR variants. The utilised WAY-EEG-GAL dataset in the present study, additionally has higher complexity that includes different load variations and surface frictions (SF).

- B. Trajectory Analysis

Comparative analysis of the true and predicted kinematic trajectories using existing and proposed approaches is presented herein. (x,y,z) coordinate location (or trajectory) of the subject’s hand during the task is utilised as kinematic parameter. The measured and predicted trajectories of hand along x,y,z direction are plotted in Fig.9 (a)-(c) for mLR, Fig. 9 (d)-(f) for CNN-LSTM and Fig. 9 (g)-(i) for WPD CNNLSTM. In CNN-LSTM model, lower trajectory mismatch is observed along the three x,y,z direction when compared to existing mLR technique. However, the two models suffers with greater trajectory mismatch in z direction. This is overcome in WPD CNN-LSTM model to a greater extent. Reasonably high correlation can be observed for all the three co-ordinates, making it more suitable for real-time application. The hand trajectory visualization of the true and estimated trajectory from WPD CNN-LSTM method in 3D space is additionally, presented in Fig.10. True trajectory (Fig. 10 (a)) and predicted trajectory (Fig. 10 (b)) were observed to be nearly equivalent.

- C. Statistical Analysis

To quantify the signiﬁcance of the three proposed deep learning methods over the existing mLR method, statistical analysis is performed in the entire (0.5-12 Hz) frequency band. We apply the two-sample t-test on the two sets of correlation values in x, y, z direction and overall for each type of proposed method with the existing mLR technique. Statistical test analysis results with α = 0.05 are presented in Table III. It can be observed that the improvements of the three proposed methods are statistically signiﬁcant as compared to the mLR method. Additionally, the statistical test of the proposed methods among themselves is also presented in Table III. The improvements in correlation value from

CNN-LSTM and WPD CNN-LSTM methods are statistically signiﬁcant compared to MLP. The improvement in correlation value from WPD CNN-LSTM found not to be statistical signiﬁcant compared to CNN-LSTM in x, y direction and overall. However the results are signiﬁcant in z direction suggesting better trajectory prediction of WPD CNN-LSTM method in z direction. Overall, the results show that our proposed approach outperforms the existing mLR technique with the best performance observed with the CNN-LSTM and WPD CNN-LSTM method.

VI. DISCUSSION

- A. Decoding Performance of the Proposed Methods

In the literature, the mLR linear decoder has been widely used to reconstruct movement kinematics. A major limitation of linear decoder is that it demands the linear relationship between the independent (observed event) variables and dependent (predicted event) variable. Human brain is a complex non-linear system. It is therefore more natural to use nonlinear methods to analyze the signals generated by such a complex non-linear system. In the present work, three neural networks based methods MLP, CNN-LSTM and WPD CNNLSTM are proposed. Neural networks infuse non-linearity by adding non-linear activation functions in the hidden and output nodes. Thus the resulting deep learning models can access very descriptive (non-linear) features that deﬁne the underlying relationships fairly well and are responsible for the high accuracy in decoding the kinematic parameters. Other than nonlinearity, it is also important that the model extracts quality features in spatial, temporal and spectral domain. Generally, the MLP and CNN models work well with the data that has a spatial relationship. Hybrid CNN-LSTM is proposed to extract spatio-temporal quality features from the input data as LSTM has shown excellent performance in extracting temporal information. An advanced version of CNN-LSTM based on wavelet packet decomposition is proposed that decompose the EEG signal into sub-bands with increasing resolution towards the lower frequency band. The WPD CNN-LSTM method thus extracts spatio-temporal and spectral information from the data. This results in superior performance by the proposed three methods compared to the state-of-the-art mLR technique based on their inherent feature extraction capability.

- B. Online Trajectory Prediction

During the training phase (which includes most of the computational burden), the model parameters such as coefﬁcients and weights are estimated. The proposed models have been trained on a system with six core Intel(R) Core(TM) i98950HK @2.90GHz CPU and 16 GB RAM. The proposed MLP model took an average execution time of 1.2 seconds per iteration. The average training time of proposed CNNLSTM and WPD CNN-LSTM model is 19 seconds and 21 seconds per epoch respectively, that is longer than the existing linear mLR models. In addition, the model demands a large amount of input training data to learn its weight parameters. It is to note that the ability of the proposed models to describe

a wide range of phenomena and outperform existing stateof-the-art models makes it computationally expensive in the training phase. However, the testing phase of the model in which the hand kinematic trajectory is decoded, is a fast procedure and can be implemented in real time and online BCI system. To get the predicted trajectory in real time, the model parameters are optimized followed by the translation of model into the embedded system’s friendly language e.g. C/ C++. Since, the aim of our work is to lay a foundation of building accurate motion decoders from EEG signals. Implementation of strength augmentation from estimated kinematic parameter is beyond the scope of present work. But, It may be noted that the current framework can be used to predict trajectory estimation for the application of strength augmentation using exoskeleton/ soft exosuit. To date, the majority of available strength augmentation using exoskeleton utilize inertial measurement units (IMU) [45]–[47]. IMU sensors measure position and velocity which are then combined to reconstruct the trajectory of the movement.

In the current work the output of model is a 3D position coordinates Px[t],Py[t], and Pz[t] corresponding to input EEG signals. First derivative of position parameter Px[t] − Px[t − 1],Py[t]−Py[t−1]. and Pz[t]−Pz[t−1] represents respectively, the horizontal, vertical and depth velocities of the hand at time sample t. The continuous estimation of position and velocity enable strength augmentation using exoskeleton/ soft exosuit in real time.

C. Potential Applications

In the present work, signiﬁcance of the proposed models (MLP, CNN-LSTM and WPD CNN-LSTM) in estimating the hand kinematic trajectory is well established. Continuous estimation of hand kinematic trajectories from brain EEG signals has potential in real-time BCI applications for healthy and disabled subjects. The methods for estimating hand position in 3D can provide beneﬁts in stroke rehabilitation therapies (neurorehabilitation) and in controlling external arm movement (neuro-prosthetics) to patients with reduced or nonexistent muscle activities due to limb loss or neurological dysfunction. Decoding motor activity directly from brain signals has also attracted attention in muscle power augmentation using neural driven exosuit or exoskeleton devices. This can additionally be utilized by the Army soldiers (healthy subjects) for improved endurance and reduced fatigue.

D. Limitation and Future Work

The GAL dataset used in our work consists of EEG signals that correspond to the executed hand movement. The four frequency bands : delta (0.5-3 Hz), theta (3-7 Hz), low alpha (7-12 Hz) and entire (0.5-12 Hz) used in the proposed method of the executed movement limit the usage of brain activity information from the marked frequency ranges. It would be interesting to explore the performance of proposed model for the imagined/executed movement in the beta (12-28 HZ) and low gamma (28-40 Hz) bands, in addition to the delta, theta and low alpha band. Another possible extension of the present work is to replace the time-resolved band-pass ﬁltered EEG

TABLE III: P value of two-sample Statistical t-test

|Direction|A vs B<br><br>|A vs C<br><br>|A vs D<br><br>|B vs C|B vs D|C vs D|
|---|---|---|---|---|---|---|
|x<br><br>y<br><br>z<br><br><br>|7.49 × 10−15 6.90 × 10−12 1.65 × 10−12|2.56 × 10−16 2.97 × 10−14 1.87 × 10−16<br><br>|1.93 × 10−16 1.62 × 10−14 1.04 × 10−16<br><br>|7.57 × 10−05 4.76 × 10−05 3.37 × 10−07|6.36 × 10−05 5.92 × 10−05 4.73 × 10−08<br><br>|1 0.52 0.05|
|Overall|2.11 × 10−19<br><br>|1.02 × 10−26|1.08 × 10−27<br><br>|6.79 × 10−7|5.78 × 10−8|0.61|

Note: A - mLR; B - MLP; C - CNN-LSTM; and D - WPD CNN-LSTM

potential based potential time-series (PTS) input with a timeresolved power spectral density (PSD) based bandpower timeseries (BTS).

In the present work, signiﬁcance of the MLP, CNN-LSTM and WPD CNN-LSTM proposed models in estimating the hand kinematic trajectory is well established. The improvements in correlation value between the true kinematic trajectory and the estimated kinematic trajectory from the three three proposed methods are statistically signiﬁcant compared to the state-of-the-art mLR method. However the improvement in correlation value from WPD CNN-LSTM method found not to be statistical signiﬁcant compared to CNN-LSTM in x, y direction. But the results are signiﬁcant in z direction suggesting better trajectory prediction of WPD CNN-LSTM method in z direction. To study the particular characteristic traits of each directional kinematic trajectory from advanced deep learning model WPD CNN-LSTM which results in low correlation in x, y direction but not in z direction, requires a large number of trials. A major limitation of the proposed deep learning models is the high computational complexity resulting in long training times. The GAL dataset utilized in our work consists of only 120 trials with 12 subject EEG data out of which 3 Subjects data was excluded due to quality issue. The available trials to optimize the proposed model for low computational cost and to characterize the directional kinematic trajectory are quite less. Therefore, in future, we intend to record large number of trials with large set of subjects.

VII. CONCLUSIONS

In this work, source aware deep learning framework is proposed for hand kinematics parameter estimation from noninvasive EEG time series. In particular, MLP, CNN-LSTM and WPD CNN-LSTM models are proposed. An additional novelty of the work is to utilize brain source localization (using sLORETA) for motor intention mapping. The information is utilized for channel selection and accurate EEG time segment selection. Electrodes placed over the active brain region corresponding to the hand movement are utilized, rather than all the available sensors data for efﬁcient computation. It has been observed that the EEG signal can provide the intended hand movement information approximately 350ms prior to actual hand movement. Early detection of intended hand movement is essential in communicating or controlling an external BCI devices. The performance of the proposed models are compared with the state-of-the-art mLR technique on the real GAL dataset. Effectiveness of the proposed framework is established using the Pearson correlation coefﬁcient analysis. Additionally,

hand trajectory estimation is presented and compared with the ground truth. Our proposed source aware deep learning models show signiﬁcant improvement in correlation coefﬁcient when compared with traditionally utilised mLR model. Our current study provides continuous decoding of brain activities that facilitate real time communication between the control block and the actuators block in BCI.

ACKNOWLEDGMENT

The authors would like to thank Prof. Shubhendu Bhasin, and Prof. Sushma Santapuri from Indian Institute of Technology Delhi (IITD), and Dr. Suriya Prakash from All India Institute of Medical Sciences (AIIMS) Delhi for their discussion and constructive comments during the preparation of the manuscript.

REFERENCES

- [1] D. Zhang, L. Yao, K. Chen, S. Wang, X. Chang, and Y. Liu, “Making sense of spatio-temporal preserving representations for EEG-based human intention recognition,” IEEE transactions on cybernetics, vol. 50, no. 7, pp. 3033–3044, 2019.
- [2] N.-S. Kwak and S.-W. Lee, “Error correction regression framework for enhancing the decoding accuracies of ear-EEG brain–computer interfaces,” IEEE transactions on cybernetics, vol. 50, no. 8, pp. 3654– 3667, 2019.
- [3] Y. Zhang, C. S. Nam, G. Zhou, J. Jin, X. Wang, and A. Cichocki, “Temporally constrained sparse group spatial patterns for motor imagery BCI,” IEEE transactions on cybernetics, vol. 49, no. 9, pp. 3322–3332, 2018.
- [4] J. Zhang, B. Wang, C. Zhang, Y. Xiao, and M. Y. Wang, “An EEG/EMG/EOG-based multimodal human-machine interface to realtime control of a soft robot hand,” Frontiers in neurorobotics, vol. 13, p. 7, 2019.
- [5] N. A. Bhagat, A. Venkatakrishnan, B. Abibullaev, E. J. Artz, N. Yozbatiran, A. A. Blank, J. French, C. Karmonik, R. G. Grossman, M. K. O’Malley et al., “Design and optimization of an EEG-based brain machine interface (BMI) to an upper-limb exoskeleton for stroke survivors,” Frontiers in neuroscience, vol. 10, p. 122, 2016.
- [6] W. He, Y. Zhao, H. Tang, C. Sun, and W. Fu, “A wireless BCI and BMI system for wearable robots,” IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 46, no. 7, pp. 936–946, 2015.
- [7] M. Deng, Z. Li, Y. Kang, C. P. Chen, and X. Chu, “A learning-based hierarchical control scheme for an exoskeleton robot in human–robot cooperative manipulation,” IEEE transactions on cybernetics, vol. 50, no. 1, pp. 112–125, 2018.
- [8] Z. Gao, W. Dang, M. Liu, W. Guo, K. Ma, and G. Chen, “Classiﬁcation of EEG signals on VEP-based BCI systems with broad learning,” IEEE Transactions on Systems, Man, and Cybernetics: Systems, 2020.
- [9] Y. Li, Q. Huang, Z. Zhang, T. Yu, and S. He, “An EEG-/EOGBased Hybrid Brain-Computer Interface: Application on Controlling an Integrated Wheelchair Robotic Arm System,” Frontiers in Neuroscience, vol. 13, p. 1243, 2019.
- [10] R. Alazrai, H. Alwanni, and M. I. Daoud, “EEG-based BCI system for decoding ﬁnger movements within the same hand,” Neuroscience letters, vol. 698, pp. 113–120, 2019.

- [11] L. He, D. Hu, M. Wan, Y. Wen, K. M. Von Deneen, and M. Zhou, “Common Bayesian network for classiﬁcation of EEG-based multiclass motor imagery BCI,” IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 46, no. 6, pp. 843–854, 2015.
- [12] N. Robinson, C. Guan, and A. Vinod, “Adaptive estimation of hand movement trajectory in an EEG based brain–computer interface system,” Journal of neural engineering, vol. 12, no. 6, p. 066019, 2015.
- [13] N. Shajil, S. Mohan, P. Srinivasan, J. Arivudaiyanambi, and A. A. Murrugesan, “Multiclass Classiﬁcation of Spatially Filtered Motor Imagery EEG Signals Using Convolutional Neural Network for BCI Based Applications,” Journal of Medical and Biological Engineering, pp. 1–10, 2020.
- [14] R. M. Rangayyan, Biomedical signal analysis. John Wiley & Sons, 2015.
- [15] A. Korik, R. Sosnik, N. Siddique, and D. Coyle, “Decoding imagined 3D hand movement trajectories from EEG: evidence to support the use of mu, beta, and low gamma oscillations,” Frontiers in neuroscience, vol. 12, p. 130, 2018.
- [16] R. Sosnik and O. B. Zur, “Reconstruction of hand, elbow and shoulder actual and imagined trajectories in 3D space using EEG slow cortical potentials,” Journal of Neural Engineering, vol. 17, no. 1, p. 016065, 2020.
- [17] X. Liu, L. Jiao, L. Li, L. Cheng, F. Liu, S. Yang, and B. Hou, “Deep Multiview Union Learning Network for Multisource Image Classiﬁcation,” IEEE Transactions on Cybernetics, 2020.
- [18] T. Zhang, W. Zheng, Z. Cui, Y. Zong, and Y. Li, “Spatial–temporal recurrent neural network for emotion recognition,” IEEE transactions on cybernetics, vol. 49, no. 3, pp. 839–847, 2018.
- [19] J. Zhang, C. Zong et al., “Deep Neural Networks in Machine Translation: An Overview.” IEEE Intell. Syst., vol. 30, no. 5, pp. 16–25, 2015.
- [20] D. Borra, S. Fantozzi, and E. Magosso, “Interpretable and lightweight convolutional neural network for EEG decoding: Application to movement execution and imagination,” Neural Networks, 2020.
- [21] Y. Sun, B. Xue, M. Zhang, G. G. Yen, and J. Lv, “Automatically designing CNN architectures using the genetic algorithm for image classiﬁcation,” IEEE transactions on cybernetics, vol. 50, no. 9, pp. 3840–3854, 2020.
- [22] S. Yang, W. Wang, C. Liu, and W. Deng, “Scene understanding in deep learning-based end-to-end controllers for autonomous vehicles,” IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 49, no. 1, pp. 53–63, 2018.
- [23] S. U. Amin, M. Alsulaiman, G. Muhammad, M. A. Mekhtiche, and M. S. Hossain, “Deep Learning for EEG motor imagery classiﬁcation based on multi-layer CNNs feature fusion,” Future Generation computer systems, vol. 101, pp. 542–554, 2019.
- [24] J. Du, C.-M. Vong, and C. P. Chen, “Novel efﬁcient RNN and LSTMlike architectures: Recurrent and gated broad learning systems and their applications for text classiﬁcation,” IEEE transactions on cybernetics, 2020.
- [25] A. Presacco, R. Goodman, L. Forrester, and J. L. Contreras-Vidal, “Neural decoding of treadmill walking from noninvasive electroencephalographic signals,” Journal of neurophysiology, vol. 106, no. 4, pp. 1875–1887, 2011.
- [26] T. J. Bradberry, R. J. Gentili, and J. L. Contreras-Vidal, “Reconstructing three-dimensional hand movements from noninvasive electroencephalographic signals,” Journal of Neuroscience, vol. 30, no. 9, pp. 3432–3437, 2010.
- [27] Y. Zhang, B. Liu, X. Ji, and D. Huang, “Classiﬁcation of EEG signals based on autoregressive model and wavelet packet decomposition,” Neural Processing Letters, vol. 45, no. 2, pp. 365–378, 2017.
- [28] M. T. Sadiq, X. Yu, Z. Yuan, Z. Fan, A. U. Rehman, G. Li, and G. Xiao, “Motor imagery EEG signals classiﬁcation based on mode amplitude and frequency components using empirical wavelet transform,” IEEE Access, vol. 7, pp. 127678–127692, 2019.
- [29] M. D. Luciw, E. Jarocka, and B. B. Edin, “Multi-channel EEG recordings during 3,936 grasp and lift trials with varying weight and friction,” Scientiﬁc data, vol. 1, no. 1, pp. 1–11, 2014.

- [30] R. Grech, T. Cassar, J. Muscat, K. P. Camilleri, S. G. Fabri, M. Zervakis, P. Xanthopoulos, V. Sakkalis, and B. Vanrumste, “Review on solving the inverse problem in EEG source analysis,” Journal of neuroengineering and rehabilitation, vol. 5, no. 1, p. 25, 2008.
- [31] A. Giri, L. Kumar, and T. Gandhi, “Head Harmonics Based EEG Dipole Source Localization,” in 2019 53rd Asilomar Conference on Signals, Systems, and Computers. IEEE, 2019, pp. 2149–2153.
- [32] J. C. Mosher, P. S. Lewis, and R. M. Leahy, “Multiple dipole modeling and localization from spatio-temporal MEG data,” IEEE Transactions on Biomedical Engineering, vol. 39, no. 6, pp. 541–557, 1992.
- [33] A. Giri, L. Kumar, and T. K. Gandhi, “Brain source localization in head harmonics domain,” IEEE Transactions on Instrumentation and Measurement, vol. 70, pp. 1–10, 2020.
- [34] S. Baillet, J. C. Mosher, and R. M. Leahy, “Electromagnetic brain mapping,” IEEE Signal Processing Magazine, vol. 18, no. 6, pp. 14– 30, Nov 2001.
- [35] K. Uutela, M. Hamalainen, and R. Salmelin, “Global optimization in the localization of neuromagnetic sources,” IEEE Transactions on Biomedical Engineering, vol. 45, no. 6, pp. 716–723, 1998.
- [36] M. S. H¨am¨al¨ainen, “Interpreting measured magnetic ﬁelds of the brain : Estimates of current distributions,” Univ. Helsinki, Finland Tech. Rep. TKK-F-A559, 1984.
- [37] M. S. H¨am¨al¨ainen and R. J. Ilmoniemi, “Interpreting magnetic ﬁelds of the brain: minimum norm estimates,” Medical and biological engineering and computing, vol. 32, no. 1, pp. 35–42, 1994.
- [38] R. D. Pascual-Marqui, D. Lehmann, T. Koenig, K. Kochi, M. C. Merlo, D. Hell, and M. Koukkou, “Low resolution brain electromagnetic tomography (LORETA) functional imaging in acute, neuroleptic-naive, ﬁrstepisode, productive schizophrenia,” Psychiatry Research: Neuroimaging, vol. 90, no. 3, pp. 169–179, 1999.
- [39] R. D. Pascual-Marqui et al., “Standardized low-resolution brain electromagnetic tomography (sLORETA): technical details,” Methods Find Exp Clin Pharmacol, vol. 24, no. Suppl D, pp. 5–12, 2002.
- [40] C.-T. Lin, C.-H. Chuang, Y.-C. Hung, C.-N. Fang, D. Wu, and Y.K. Wang, “A driving performance forecasting system based on brain dynamic state analysis using 4-D convolutional neural networks,” IEEE transactions on cybernetics, 2020.
- [41] A. Narang, B. Batra, A. Ahuja, J. Yadav, and N. Pachauri, “Classiﬁcation of EEG signals for epileptic seizures using Levenberg-Marquardt algorithm based Multilayer Perceptron Neural Network,” Journal of Intelligent & Fuzzy Systems, vol. 34, no. 3, pp. 1669–1677, 2018.
- [42] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural computation, vol. 9, no. 8, pp. 1735–1780, 1997.
- [43] X. Ma, D. Wang, D. Liu, and J. Yang, “DWT and CNN based multi-class motor imagery electroencephalographic signal recognition,” Journal of Neural Engineering, vol. 17, no. 1, p. 016073, 2020.
- [44] R. N. Khushaba, S. Kodagoda, S. Lal, and G. Dissanayake, “Driver drowsiness classiﬁcation using fuzzy wavelet-packet-based featureextraction algorithm,” IEEE transactions on biomedical engineering, vol. 58, no. 1, pp. 121–131, 2010.
- [45] K. Little, C. W. Antuvan, M. Xiloyannis, B. A. De Noronha, Y. G. Kim, L. Masia, and D. Accoto, “IMU-based assistance modulation in upper limb soft wearable exosuits,” in 2019 IEEE 16th International Conference on Rehabilitation Robotics (ICORR). IEEE, 2019, pp. 1197–1202.
- [46] J. Chen, C. Yang, and J. Hofschulte, “Improvement of an Arm Exoskeleton by Data Fusion with an Inertial Measurement Unit,” in 2nd International Symposium on Computer, Communication, Control and Automation. Citeseer, 2013, pp. 445–448.
- [47] T. Beravs, P. Reberˇsek, D. Novak, J. Podobnik, and M. Munih, “Development and validation of a wearable inertial measurement system for use with lower limb exoskeletons,” in 2011 11th IEEE-RAS International Conference on Humanoid Robots. IEEE, 2011, pp. 212–217.

