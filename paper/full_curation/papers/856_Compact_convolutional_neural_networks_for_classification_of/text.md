# arXiv:1803.04566v2[cs.LG]9Oct2018

## Compact Convolutional Neural Networks for Classiﬁcation of Asynchronous Steady-state Visual Evoked Potentials

Nicholas R. Waytowich1,2,*, Vernon J. Lawhern1, Javier O. Garcia1,3, Jennifer Cummings2, Josef Faller2, Paul Sajda2, and Jean M. Vettel1,3,4 1U.S. Army Research Laboratory, Maryland, USA 2Laboratory for Intelligent Imaging and Neural Computing, Columbia University, New York, USA 3Department of Bioengineering, University of Pennsylvania, Pennsylvania, USA 4Department of Physiological Brain Sciences, University of California, Santa Barbara, California, USA *Corresponding Author

October 10, 2018

Abstract

Objective. Steady-State Visual Evoked Potentials (SSVEPs) are neural oscillations from the parietal and occipital regions of the brain that are evoked from ﬂickering visual stimuli. SSVEPs are robust signals measurable in the electroencephalogram (EEG) and are commonly used in brain-computer interfaces (BCIs). However, methods for high-accuracy decoding of SSVEPs usually require hand-crafted approaches that leverage domain-speciﬁc knowledge of the stimulus signals, such as speciﬁc temporal frequencies in the visual stimuli and their relative spatial arrangement. When this knowledge is unavailable, such as when SSVEP signals are acquired asynchronously, such approaches tend to fail. Approach. In this paper, we show how a compact convolutional neural network (Compact-CNN), which only requires raw EEG signals for automatic feature extraction, can be used to decode signals from a 12-class SSVEP dataset without the need for user-speciﬁc calibration. Main results. The Compact-CNN demonstrates across subject mean accuracy of approximately 80%, out-performing current state-of-the-art, handcrafted approaches using canonical correlation analysis (CCA) and Combined-CCA. Furthermore, the Compact-CNN approach can reveal the underlying feature representation, revealing that the deep learner extracts additional phase- and amplitude-related features associated with the structure of the dataset. Signiﬁcance. We discuss how our Compact-CNN shows promise for BCI applications that allow users to freely gaze/attend to any stimulus at any time (e.g., asynchronous BCI) as well as provides a method for analyzing SSVEP signals in a way that might augment our understanding about the basic processing in the visual cortex.

Keywords: Brain-Computer Interface, EEG, Deep Learning, Convolutional Neural Network, Steady-state visual evoked potentials

### 1 Introduction

Evoked potentials are robust signals in the electroencephalogram (EEG) induced by sensory stimuli, and they have been used to study normal and abnormal function of the sensory cortex [1]. The most well-studied of these are Steady-State Visual Evoked Potentials (SSVEPs), which are neural oscillations in the visual cortex that are evoked from stimuli that temporally ﬂicker in a narrow frequency band [2, 3]. SSVEPs likely arise from a reorganization of spontaneous intrinsic brain oscillations in response to a stimulus [4]. Paradigms leveraging SSVEP responses have been used to investigate the organization of the visual system [5,6], identify biomarkers of disease and sensory function [7–9], and probe visual perception [10,11].

The robustness of SSVEP has enabled its use as a control signal for brain computer interfaces (BCIs) that enable low-bandwith communication for individuals with catastrophic loss of motor functions, bypassing neuro-muscular pathways and establishing a communication link directly to the brain [12,13]. In a typical SSVEP BCI, a patient/subject is presented with a grid of squares on a computer monitor, where each square contains semantic information such as a letter, number, character, or action. Superimposed on these squares are visual ﬂicker frequencies that uniquely ”tag” each square, thus mapping semantics to visual temporal frequency. As one directs their gaze and attention to a particular square with the semantic information they wish to convey, an SSVEP signal at the corresponding frequency can be measured in the EEG with dominant signals in parietal and occipital electrodes. The approach, though seemingly simple, has been important for enabling communication channels for those that are locked-in and have no other means of communication, particularly those with late stage amytrophic-lateral sclerosis (ALS) [14].

Central to using SSVEP, whether as a mechanism for probing vision or enabling a BCI, is the need to accurately decode and analyze the frequency information. Power spectral density analysis (PSDA), for example, is often used to identify spectral peaks in the EEG data that map to the ﬂicker frequency of the stimulus. More recent approaches have used multivariate statistical analysis techniques, such as Canonical Correlation Analysis (CCA), that employ a template matching scheme between the EEG data and a set of hand-crafted, sinusoidal reference signals [15–17]. A recent innovation in this approach, called Combined-CCA, uses a unique combination of sinusoidal templates as well as individual template responses constructed from SSVEP calibration data to improve the standard reference signals used in the CCA [18–20]. While Combined-CCA outperforms CCA, it does so at the cost of requiring user-speciﬁc calibration data to construct the reference signals.

To enable more ﬂexible results without the need for a priori information, deep learning approaches were leveraged for their ability to learn robust feature representations. As such, deep learning techniques have surpassed traditional approaches that rely on manual feature extraction [21,22]. Convolutional Neural Networks (CNNs) in particular have become a very popular deep learning approach for learning rich feature representations for image classiﬁcation problems [23–26], and their ability to learn invariant features has shown promise to advance methods used in EEG signal analysis [27–35]. Deep learning approaches, however, typically require large amounts of training data in order to prevent over-ﬁtting, and this requirement strongly limits their viability for SSVEP BCIs which are constrained by relatively modest sample sizes in typical BCI datasets. As a con-

sequence, previous attempts at applying CNNs to SSVEP classiﬁcation have used domain-speciﬁc representations to reduce the amount of training data required [36–38]. These approaches utilize the fast-fourier transform (FFT) in their deep-learning models, thereby transforming EEG signals from the time-domain to the frequency-domain. These FFT-based approaches constrain the model to learn only frequency-based features which may be insuﬃcient to capture other task-relevant information. Consequently, this approach severely hinders the value of deep learning approaches on SSVEP datasets.

In this paper, we employ a deep learning approach that allows for the discovery of the underlying representations in SSVEP signals that relate ﬂicker to semantics and train on relatively small datasets. Speciﬁcally, our approach utilizes a recently developed deep learning model by our group that is a compact convolutional neural network (Compact-CNN) and operates on broadly-ﬁltered EEG signals. Its compact nature allows it to operate on smaller datasets, while the convolutional structure allows for the automatic extraction of task-relevant EEG features. Our Compact-CNN was applied to a previously collected SSVEP dataset [39] composed of 4 s long EEG epochs of data. Without using any user-speciﬁc calibration, our Compact-CNN results in substantially better classiﬁcation accuracy compared to CCA and Combined-CCA. Furthermore, the underlying feature representations constructed by our Compact-CNN revealed that the deep learner is able to extract additional phase and amplitude related features associated with the SSVEP signals. We discuss how our Compact-CNN shows promise for BCI applications that allow users to be able to freely gaze/attend to any stimulus at any time (e.g., asynchronous BCI) and augments our understanding about the underlying cortical processing in the visual cortex.

### 2 Methods

Ten healthy participants volunteered for an oﬄine SSVEP BCI experiment, and their de-identiﬁed data were downloaded from a publicly available repository [39]. The participants sat 60cm away from a 27-inch LCD monitor (60Hz refresh-rate and 1280x800 resolution) in a dim room, and they looked at 12 ﬂashing stimuli arranged in a 4x3 grid of 6cm x 6cm squares that represented a numeric keypad. As shown in Figure 1, the 12 SSVEP stimuli ﬂashed at frequencies ranging from 9.25Hz to 14.75Hz in steps of 0.5Hz. For each individual trial, a red square was used to cue subjects to visually ﬁxate one of the 12 stimulus squares. Each trial was 4 seconds long and was within a block of 12 trials that included each of 12 unique targets. Each subject underwent 15 blocks of these 12 trials for a total of 180 trials. During the experiment, EEG data was collected from 8 active electrodes placed over occipital-parietal areas using the BioSemi ActiveTwo EEG system (Biosemi B.V., Netherlands) with a sampling frequency of 2048Hz. All data were ﬁrst bandpass ﬁltered bidirectionally between 9 and 30Hz using a Butterworth ﬁlter and then downsampled to 256Hz. The 4s epochs were divided in to 1s segments for subsequent analysis.

Three classiﬁcation methods were compared using a leave-one-subject-out cross validation procedure where data from 9 participants were pooled together for training and the 10th participant was used for testing. In this way, user-independent models were built that did not use any training data from the test participant. The test participant was rotated for each fold so that each participant became a test participant. For classiﬁcation, three methods were compared that do

[Figure 1]

- Figure 1: Methodological Overview. Participants viewed a virtual keypad where each number ﬂickered at a ﬁxed frequency and phase (ﬂicker legend). For each 4s trial, the participant was cued to ﬁxate on a speciﬁc number while EEG was recorded from occipital-parietal areas (left). The trials were then divided into 1s segments and used as input to a deep learner, where subject-independent network models were trained and tested using a leave-one-subject-out classiﬁcation procedure to identify the chosen class (the ﬁxated number). Finally, the deep learning model activations were plotted using the t-SNE method to project the high-dimensional feature representation of the network down to two dimensions, revealing clusters that captured the diagnostic features within the test set (right).

not require user-speciﬁc calibration: our Compact-CNN and two baseline methods derived from the conventional multivariate statistical analysis technique, Canonical Correlation Analysis (CCA). The ﬁrst method tested was the calibration-free CCA that used sinusoidal reference signals [15,16], while the second was our variant of the state-of-the-art Combined-CCA method [18,19] that uses transfer learning to eliminate the user-speciﬁc calibration but maintains the superior classiﬁcation performance of Combined-CCA [20].

Finally, the learned representation was visualized for our Compact-CNN, addressing a scientiﬁc aim within the EEG deep learning community to understand the diagnostic features of the data [32,40]. As depicted in Figure 1, the feature activations of the trained deep learner were shown using t-distributed stochastic neighbor embedding (t-SNE) to project individual SSVEP trials onto two dimensions [41]. The t-SNE projections were then plotted for each layer to visualize how the deep learner separates and clusters EEG trials in a projected feature-space learned by the deep network. The clusters are used to infer the diagnostic features within the test set.

#### 2.1 Classiﬁcation Methods

##### 2.1.1 EEGNet: Compact Convolutional Neural Network (Compact-CNN)

To assess the utility of deep learning approaches for SSVEP BCI, our analysis used our CompactCNN (the EEGNet architecture) that was designed for classifying raw EEG when only limited amounts of data are available, such as in SSVEP BCI experiments [35]. Our Compact-CNN approach eﬃciently represents EEG signals in a compact manner by ﬁrst performing temporal convolutions, with the convolutional kernel weights being identiﬁed from the data. The ﬁrst layer of the network then performs a temporal convolution to mimic a bandpass frequency ﬁlter, a result supported by the Convolution Theorem [42]. Our approach then uses depthwise spatial convolutions that act as spatial ﬁlters to reduce the dimensionality of the data. The main beneﬁt of depthwise convolutions is reducing the number of trainable parameters to ﬁt, as these convolutions are not fully-connected to all previous outputs. When used in EEG-speciﬁc applications, this operation provides a direct way to learn spatial ﬁlters for each temporal ﬁlter, thus enabling the eﬃcient extraction of frequency-speciﬁc spatial ﬁlters. The Compact-CNN also uses separable convolutions to more eﬃciently combine information across ﬁlters [43]. The main beneﬁts of separable convolutions are (1) reducing the number of parameters to ﬁt and (2) explicitly decoupling the relationship within and across outputs by ﬁrst learning a kernel summarizing each output individually, then optimally merging the outputs afterwards. As described in Table 1, each convolution layer is followed by batch normalization, 2D average pooling, and dropout layers. In the ﬁrst two layers, the exponential linear unit (ELU) non-linearity (as opposed to other non-linear activation functions such as sigmoids or rectiﬁed linear units) was employed since it resulted in superior performance for EEG classiﬁcation [35]. The fourth and ﬁnal layer is connected to a dense layer with a softmax activation function for classiﬁcation. Our Compact-CNN is trained using a categorical cross-entropy loss function (shown in Equation 1):

Li = −

j

ti,jlog(pi,j) (1)

where p are the model predictions, t are the true labels, i denotes the sample number, and j denotes the class. The model was implemented in Tensorﬂow [44], using the Keras API [45]. The model was trained for 500 iterations using the Adam [46] optimizer, with a minibatch size of 64 trials. The dropout probability was set to 0.5 for all layers. For this application, the model learned 96 temporalspatial ﬁlter pairs (F1 = 96, F2 = 96 and D = 1). The complete model architecture of our CompactCNN is shown in Table 1; our implementation can be found at https://github.com/vlawhern/arleegmodels.

##### 2.1.2 Standard CCA

Canonical Correlation Analysis (CCA) is a statistical analysis technique that ﬁnds underlying correlations between two multidimensional datasets. Given two multidimensional variables X and Y , CCA seeks to ﬁnd weight vectors Wx and Wy such that their corresponding linear projections

Table 1: Compact-CNN architecture, where C = number of channels, T = number of time points, F1 = number of temporal ﬁlters, F2 = number of separable ﬁlters (here, F1 = F2), D = number of spatial ﬁlters to learn per temporal ﬁlter and N = number of classes, respectively.

|Layer<br><br>|Layer Type # ﬁlters size # params Output Activation Options|
|---|---|
|1<br><br>2<br><br>3<br><br><br>Classiﬁer<br><br>|Input (C, T) Reshape (1, C, T) Conv2D F1 (1, 256) 256 ∗ F1 (F1, C, T) Linear mode = same<br><br>BatchNorm 2 ∗ F1 (F1, C, T) DepthwiseConv2D D * F1 (C, 1) C ∗ D ∗ F1 (D * F1, 1, T) Linear mode = valid, depth = D, max norm = 1 BatchNorm 2 ∗ D ∗ F1 (D * F1, 1, T) Activation (D * F1, 1, T) ELU AveragePool2D (1, 4) (D * F1, 1, T // 4) Dropout (D * F1, 1, T // 4) rate = 0.5 SeparableConv2D F2 (1, 16) 16 ∗ D ∗ F1 + F2 ∗ (D ∗ F1) (F2, 1, T // 4) Linear mode = same<br>BatchNorm 2 ∗ F2 (F2, 1, T // 4) Activation (F2, 1, T // 4) ELU AveragePool2D (1, 8) (F2, 1, T // 32) Dropout (F2, 1, T // 32) rate = 0.5 Flatten (F2 * (T // 32)) Dense N * (F2 * T // 32) N Softmax<br>|

x = XTWx and y = Y TWy have maximal mutual correlation. These projections are found by solving the following objective function:

ρ(x,y) = max

max

Ws,Wx

Ws,Wx

E[WxTXY TWy] E[WxTXXTWx]E[WyTY Y TWy]

. (2)

For SSVEP detection, CCA computes the canonical correlation between multichannel EEG

data and a set of reference signals Yk composed of sines and cosines matching the fundamental and harmonic frequencies of the target stimulus. Reference signals are made for each of the K frequency

stimuli where each set contains Nh harmonics of the fundamental frequency fk.

Yk =





sin(2πfkt) cos(2πfkt) .

 

 

sin(2πNhfkt) cos(2πNhfkt)

(3)

EEG data is canonically correlated with each set of reference signals, and SSVEP detection is made on the basis of selecting the frequency set which provides the maximum canonical coeﬃcient, fk = maxk ρ(x,fk), where fk = f1,f2,...fK. In this analysis, K = 12 since data was used from a 12-class SSVEP BCI [39] with numbers on the virtual keypad ﬂashing at frequencies ranging from 9.25Hz to 14.75Hz in steps of 0.5Hz.

##### 2.1.3 State-of-the-art Combined-CCA

Combined-CCA is a recent extension to the CCA method that combines the reference signals from traditional CCA with prototype responses derived from participant EEG data to better account for the imperfect match between actual brain EEG data and the approximate sine and cosine signals [18,19]. In the Combined-CCA method, participants complete a calibration session before using the SSVEP BCI to collect training data for each stimulus frequency, and EEG data for each frequency is averaged across the training trials. In our recent extension of Combined-CCA [20], we introduced a pooled transfer approach that averages SSVEP trial data from other subjects to eliminate a calibration session for the current user.

To create the prototype responses, X¯k, data were taken from 9 of the ten subjects and averaged across trials and subjects for each stimulus frequency k. Using these prototype responses X¯k as well as the sine and cosine reference signals Yk (Equation 3), the Combined-CCA classiﬁes the data from the test subject, X, by fusing together all pairs of canonical correlations between X¯k, Yk and X using a weighted average resulting in a combined correlation coeﬃcient for each class, pk. The frequency that maximizes this weighted correlation value is selected as the SSVEP target:

fk = max

ρ(k), k = 1,2,...K (4)

k

### 3 Results

Our analysis compared three classiﬁcation approaches on a 12-class SSVEP BCI experiment from a publicly available dataset [39]. Participants were cued to ﬁxate one of 12 numbers ﬂickering at frequencies ranging from 9.25 to 14.75Hz on a virtual keypad for four seconds (Figure 1). The

###### 4s epoch was divided into 1s segments to augment the number of trials used in a 10-fold crossvalidation procedure that identiﬁed the dominant frequency in the EEG and thus determined which number was ﬁxated.

#### 3.1 Compact-CNN outperforms CCA and Combined-CCA

To assess whether deep learning approaches improve classiﬁcation of SSVEP signals, performance of the Compact-CNN was compared to the multivariate statistical analysis technique, CCA, and its current state-of-the-art variant, Combined-CCA. The classiﬁcation accuracy for each method is shown for each of the 10 participants in Figure 2, and results demonstrate the robust performance improvement for Compact-CNN relative to the two comparison methods. Compact-CNN proved to be particularly beneﬁcial for subjects whose performance was notably poor when CCA based methods were used (i.e., subjects 1, 3, 9 and 10).

When evaluating the overall mean performance (Figure 2, right), results demonstrated that Compact-CNN signiﬁcantly outperformed CCA and Combined-CCA methods as indicated by

[Figure 2]

- Figure 2: Classiﬁcation Accuracy. The SSVEP BCI classiﬁcation accuracy is shown for each of 10 participants for three methods, Combined-CCA, CCA, and Compact-CNN. The mean accuracy across participants is shown at the right, with signiﬁcant paired t-test diﬀerences between CompactCNN and each of the multivariate methods denoted with ∗∗, representing a p < .0001. Error bars indicate SEM across participants. Nominal chance performance with 12 classes is 8.3%.

paired t-tests (Compact-CNN vs Combined-CCA: t(9) = −10.5,p < 0.0001; Compact-CNN vs CCA: t(9) = −8.7,p < 0.0001). Surprisingly, the state-of-the-art Combined-CCA method performed signiﬁcantly worse than CCA, and as subsequent analyses will show, a likely explanation is that the method is not prepared to work with asynchronous data that is not phase locked.

#### 3.2 Compact-CNN extracts narrow-band frequency activity

Our analysis next examined the underlying learned representation of the Compact-CNN, investigating the diagnostic features of the data that may account for the superior performance. Our ﬁrst analysis along this eﬀort focused on interpreting the learned temporal kernel weights in Layer 1. Figure 3 visualizes a subset of the temporal kernels learned by the Compact-CNN model for one randomly-selected fold and shows the corresponding spectral power of some temporal kernels. Here we see that the Compact-CNN identiﬁes narrow-band frequency activity along a spectrum of frequencies, both slow-wave (Kernel 5, at approx. 9 Hz) and fast-wave (Kernel 95, approx. 14Hz). These frequencies closely align with that of the SSVEP experimental stimulus frequencies, suggesting that the model is capturing task-relevant oscillatory activity.

#### 3.3 Compact-CNN reveals diﬀerences among classes

Our next analysis uses a data reduction and visualization technique (t-SNE) to investigate the hidden unit activation structure across all layers of the Compact-CNN. The activation in each layer was similar, so only the t-SNE projections of the activation in layer 3 of the Compact-CNN were plotted in Figure 4 for all training observations (across the 9 training subjects) in fold 1.

This visualization is a projection of the data down to two dimensions, allowing us to estimate

[Figure 3]

- Figure 3: Visualization of Compact-CNN temporal kernels. (A-F) Representative subset of the derived temporal kernels. In the subplots, the x-axis denotes the length (in msec) of the temporal kernel, and the y-axis denotes the amplitude of the kernel. Kernels selected based on suspected frequency separability. (G) Spectral power of the temporal kernels shown in (D-F) that depict the separability of some kernels based on the frequency content of the temporal kernels. Figure labels denote the suspected stimulus driven responses (including harmonics, e.g., kernel 95, kernel 47).

discriminability among training trials and to infer the properties of the learned representation that account for classiﬁcation performance. Each element of the t-SNE plot represents a single trial with a color that indicates diﬀerent known features. In Figure 4, trials were labeled based on their class (one of 12 numbers on the virtual keypad), the participant ID (one of 10 unique individuals), and the trial order (one of 15 trial bins ordered from ﬁrst to last). Only the class plot revealed coherent clusters of colored elements, indicating that the learner identiﬁed the 12 unique classes of the numeric keypad. The lack of clusters in the subject plot conﬁrmed that the variability between individual participant brain signals does not account for the feature representation, and lack of clusters in the trial plot demonstrated that there was not a time-on-task eﬀect (e.g., fatigue, drowsiness, inattention) that diﬀerentiated the trials across the duration of the experimental session.

Next, our analysis examined the composition of the clusters themselves. Interestingly, the class plot revealed separable clusters that were colored with the same class label. In Figure 4A, elements colored yellow belong to the trials where the participant ﬁxated on the number 8 that ﬂickered at 12.25Hz. This reveals that the learner diﬀerentiated diﬀerent trials from the same class. This unexpected separation is not predicted from the derivation of the model, as the objective function in equation (1) only seeks to separate the 12 classes. Consequently, our analysis investigated whether these within-class clusters may be related to another known feature of the dataset, namely the 1s

[Figure 4]

- Figure 4: t-SNE of Compact-CNN Layer 3. Each element represents a single trial and the color represents membership for three diﬀerent features: (A) the stimulus class of the 12-class SSVEP numeric keypad; (B) one of the 10 participants; and (C) the trial number across the 180 trials. The bottom panels are zoomed-in sections of the top images to illustrate whether the individual clusters consist of the same colored label. Gray points indicate trials that are not visually separable and represent those least likely to be classiﬁed correctly.

segments of the original 4s trial epochs.

#### 3.4 Characterizing features of within-class clusters

In Figure 5A (right), the elements in the 12.25Hz class (yellow trial elements) were recolored according to their segment of the original 4s trial, where 0 to 1s is blue, 1 to 2s is red, 2 to

- 3s is green, and 3 to 4s is orange. The segments account for the separable clusters within-class. This indicates that the deep learner is inﬂuenced (and learns) EEG features other than the trained class-level diﬀerences.

Next, our analysis characterized the signal properties of raw SSVEP responses for each trial with a phase and amplitude analysis shown in Figure 5B and 5C, respectively. The radial phase plot in Figure 5B shows that the EEG trial segments have separable phases with the 3rd and 4th segments clustering at opposite phases to the 1st and 2nd segments of the trial. In contrast, Figure 5C shows similar amplitudes across the four trial segments and only Dim2 values of 5A seem to denote trial segment separability.

While Figure 5 illustrates phase and amplitude features for the 12.25Hz class from channel Oz, the subplots of Figure 6 conﬁrm that these patterns are common across other stimulus classes and channels. The average estimated phase (left column) and amplitude (right column) are depicted for the 9.25Hz class (top row), the 12.25Hz class (middle row), and the 14.75Hz class (bottom row).

[Figure 5]

- Figure 5: Phase and Amplitude of 1s Trial Segments. (A) The yellow 12.25Hz clusters on the left are recolored on the right based on their respective 1s segment of the original 4s SSVEP trial, where blue is the ﬁrst second, red the second, green third, and orange the fourth. (B) The polar angle plot of the estimated phase, where angle is represented in degrees within the circular plot and distance from the center of the plot represents the amplitude of Dim 2 shown in 5A. (C) The estimated amplitude of the phases of 5B plotted against the amplitude of Dim 2 in 5A. Data shown is from channel Oz which is located over the center of the visual cortex.

The bottom diagram in Figure 6 shows the corresponding channel layout and coloring. Phase and amplitude estimations were averaged over each trial and subject for the corresponding stimulus frequency and are shown for each electrode as colored line plots. Segment-wise diﬀerences are strongest for phase, but they can also be seen for amplitude features across all EEG channels. Here, only a few classes were illustrated for brevity, but this pattern is consistent across classes and scalp locations.

[Figure 6]

- Figure 6: Mean Phase and Amplitude Across Channels. Phase (left column) and amplitude (right column) are shown for three classes: the 9.25Hz class (A,B), the 12.25Hz class (C, D), and the 14.75Hz class (E, F). Electrodes are represented as a separate line and mapped onto the scalp in the legend (bottom). Error bars indicate SEM across participants.

### 4 Discussion

In this research, our analysis investigated whether deep learning approaches could improve performance in classiﬁcation of SSVEP BCI trials over state-of-the-art methods. While CNNs have

shown promise for feature extraction and classiﬁcation of EEG signals across a number of domains [27–34], there has been very little work in applying deep learning to classiﬁcation of SSVEP signals [36–38]. We demonstrate on a representative data set that our Compact-CNN approach can outperform both CCA and Combined-CCA. Our approach improved classiﬁcation performance on a group level, but also in individuals who had particularly poor performance when conventional methods were used. An inspection of the learned representation used for classiﬁcation in layer 3 of the Compact-CNN revealed activation clusters that diﬀerentiated the 12 classes of numeric stimuli in the virtual keypad. In contrast, the clusters did not diﬀerentiate individual participants from one another or the trial order that may arise from time-on-task fatigue, inattention, or other nuisance variables. The speciﬁcity of the representation in layer 3 indicates that the superior performance was not dependent on task-irrelevant features (participant, time-on-task), indicating that the Compact-CNN did not merely overﬁt the data in the training phase. Instead, the superior performance of the Compact-CNN likely arose from diagnostic trial features that the deep learner identiﬁed were robust in the data, namely within-class separability.

Unexpectedly, the activation in layer 3 revealed clusters of trials from within the same class, even though the 12-class classiﬁcation task did not require any within-class distinction. After further investigation of the trials in the clusters, results revealed that the variability in phase across the 1s segments of the original 4s SSVEP trial accounted for the within-class cluster diﬀerentiation, and the phase diﬀerences across the four 1s segments were robust across channels and almost all of the stimulus classes. Although unexpected, these within-class clusters highlight the strength of the deep learning approaches to learn diagnostic features directly from the data.

Our original motivation for the 1s segments arose from the aim to provide more training trials for the Compact-CNN. However, the segments led to two unexpected, but likely related, results: (1) the identiﬁcation of phase variability across the EEG response in the original 4s SSVEP trial epoch and (2) the substantial performance impairment in classiﬁcation accuracy for the current state-of-the-art method, Combined-CCA. In general, CCA approaches leverage domain knowledge to extract relevant SSVEP features embedded in the EEG responses, and our results suggest a limitation that may arise from assuming a particular stimulus frequency and phase. Most multivariate approaches, including Combined-CCA, have thus far only proven eﬀective under system-paced or synchronized SSVEP paradigms where precise stimulus onset information is known ahead of time. Our results suggest that this approach may constrain the success of these methods to synchronous SSVEP paradigms, while our Compact-CNN approach shows promise for asynchronous SSVEP classiﬁcation where the users would be able to freely gaze/attend to any stimulus at any time. Here, we discuss how our Compact-CNN approach demonstrates the value of deep learning for SSVEP BCI, provides a potential innovation for asynchronous BCIs, and augments our understanding about the underlying cortical processing in the visual cortex.

#### 4.1 Deep learning allows characterization of EEG features

Deep learning approaches allow computational models to learn representations of data with multiple layers of abstraction. This in turn can allow for the discovery of rich features or structure within large datasets. However, since these layers of features are learned instead of designed by human

engineers, interpreting the meaning of these features remains a critical challenge in the ﬁeld of deep learning [47,48]. In this paper, our analysis utilized the representational learning capabilities of multilayer CNNs and show that the model learned interpretable features from EEG data that are consistent with the SSVEP literature. The Compact-CNN identiﬁes phase features that are invariant to both subject and trial (time-on-task) diﬀerences.

Our results extend previous studies that have applied deep learning to SSVEP BCI paradigms. These prior approaches leveraged domain speciﬁc knowledge when constructing their feature extraction layers [36–38]. The ﬁrst approach applied a CNN for the classiﬁcation of SSVEP signals by using the fast-fourier transform (FFT) to convert time-domain representations into frequencydomain representations [36]. The second, more recent approach transformed SSVEP data into the frequency domain as a pre-processing step before classiﬁcation with a CNN [37]. A similar approach was taken in [38], where the authors used an FFT-based hidden layer for classifying SSVEP signals. These approaches incorporate domain-speciﬁc knowledge of the stimulus frequencies by utilizing the FFT to transform raw time-domain EEG signals to the frequency domain since spectrally focal power diﬀerences are known to be discriminative features in the context of SSVEP-based decoding. All these approaches incorporate frequency speciﬁc knowledge, but no phase information. In contrast, our Compact-CNN operates on broadly-ﬁltered EEG signals, and the relevant features (frequency and phase) are learned and extracted directly from these input signals. This end-toend approach might be particularly advantageous for use-cases where domain-speciﬁc knowledge is unavailable.

Additionally, our results demonstrated that the Compact-CNN was able to discover deeper structure within the SSVEP dataset in the form of phase information that reﬂects features of the 1s segments of the original 4s SSVEP trial epochs. This learned structure is present in the t-SNE projections of the model activations in the hidden layers. Thus, the Compact-CNN provides a powerful tool for interpreting intrinsic structures within EEG datasets, and critically, this type of structure discovery would not be possible using standard linear methods, such as CCA or CombinedCCA.

#### 4.2 Potential beneﬁts of Compact-CNN-based asynchronous classiﬁcation

SSVEP signals can be generated and classiﬁed using either synchronous or asynchronous temporal coding paradigms [49]. In synchronous paradigms, the onset and oﬀset of the user gaze towards the stimulus are known: the user is cued to look at a ﬂashing stimulus in a speciﬁed time-window so that the user’s gaze is synchronized with the onset of stimulus ﬂashing. In contrast, asynchronous SSVEP paradigms allow users to freely gaze/attend to any stimulus at any time. Asynchronous paradigms are generally more ﬂexible and are more amenable to practical BCI. For some applications, asynchronous temporal coding paradigms can make BCI interaction faster, more intuitive, and/or ergonomical as the user can directly communicate a speciﬁc command of choice instead of waiting for the respective system cues in synchronized approaches. EEG-based decoding however, is typically more diﬃcult in asynchronous SSVEP paradigms, particularly if phase information of the stimulus is not known.

Here, our division of the 4s SSVEP trial epoch into 1s segments simulates an asynchronous

SSVEP BCI from a discretized stimulation paradigm. These segments approximate a less-controlled paradigm wherein a participant may randomly attend to a stimulus frequency. A segment length of 1s represents a fast-paced BCI design where classiﬁcations can be made every second. On this data set, the Compact-CNN method outperformed state-of-the-art approaches in simulated asynchronous operation. The Compact-CNN learner extracted relevant frequency and phase features directly from the broadly-ﬁltered EEG signals even when speciﬁc phase information of the SSVEP trials was unknown. This improvement could potentially beneﬁt a variety of asynchronous SSVEP BCI applications including control of wheelchairs [17,50], neuroprosthetics [51], exoskeletons [52], or interaction with virtual [53,54] or augmented reality [55]. The observed performance improvement may also make this asynchronous approach attractive for applications like spellers [19], where synchronous paradigms have been traditionally preferred for their higher information bandwidth at the cost of lower ﬂexibility.

Additionally, achieving calibrationless BCI classiﬁcation is paramount for developing more practical BCI systems as it eliminates the need for time-consuming training sessions for the user [56]. Using a leave-one-subject out transfer protocol, our Compact-CNN approach outperformed the baseline CCA approaches without any user-speciﬁc calibration. This is further reﬂected in t-SNE projections which indicate that our deep learning model is able to learn subject invariant features, which is critical for transfer across subjects. Based on its promise for asynchronous BCI paradigms and the fact that user-speciﬁc calibration is not required, this Compact-CNN approach gives BCI designers additional options to tailor SSVEP BCI systems to the needs of speciﬁc user-groups or other requirements.

#### 4.3 Detecting frequency and phase information with the Compact-CNN

The Convolution Theorem states that convolutions of signals in the time-domain relate to multiplication in the frequency-domain. Since the ﬁrst layer of our Compact-CNN is a temporal convolution (whose weights need to be learned from the data), our network has the capability to learn frequencyspeciﬁc temporal ﬁlters, including EEG features as shown in our previous work [35]. We showed in Figure 3 that the Compact-CNN model is capable of extracting narrow-band task-speciﬁc slowwave and fast-wave frequency activity. We believe that our network is also capturing information correlated to frequency through the use of the average-pooling layer in Layer 1 of our model. The sequence of operations in Layer 1 (temporal convolution, ELU non-linearity then average-pooling) is similar to the methodology of [57] for calculating event-related synchronization and desynchronization features. In their work, they narrow-band ﬁlter, then square, then average over a moving window the signal to obtain an estimate of frequency power. The similarity of this approach to the operations in Layer 1 of the Compact-CNN suggests that our model is calculating features at least correlated to that of frequency power.

In addition, convolutional neural networks have the property of equivariance to local translation [58–60]. In particular, when the data is a time-series signal, local translations correspond to phase oﬀsets in the signal. This means that the output of the convolution operation (a dot product between the convolutional kernel and the signal) will preserve the phase information in the signal relative to the phase of the convolutional kernel (i.e., when the convolutional kernel is in phase or

in anti-phase with the data). The ability of convolutional neural networks to capture translationinvariant features (in the case of a time-series signal, phase-invariant) was proven in [59]; it was also shown that pooling layers and model depth were critical to achieve this (additional theoretical treatment of convolutional neural networks and their ability to extract translation-invariant features can be found in [60]). It is through this property that our Compact-CCN approach was able to extract phase information from the signals of interest. Figure 5, which shows a t-SNE projection of the hidden unit activations in layer 3, provides additional evidence that our network can capture this phenomena.

#### 4.4 Phase discrimination for vision neuroscience

While this paper largely focuses on the relevance for BCI applications, the Compact-CNN’s ability to detect phase holds incredible potential to augment our understanding of visual processing in common SSVEP experimental paradigms. For example, SSVEP experimentation has revealed the temporal dynamics and spatial constraints of spatial attention when divided across locations, reﬁning theories of how we attend to speciﬁc locations in our environment [61]. Likewise, phase information about oscillations of alpha activity within coordinated populations of neurons in the visual cortex has been shown to predict whether stimuli will be detected in the environment, suggesting that phase information drives coordinated excitation that facilitates perception or synchronized inhibition that prevents stimulus detection [62–64].

Here, the Compact-CNN identiﬁed phase information in the SSVEP response that was irrelevant for the 12-class classiﬁcation but robust in the neural response, both across stimulus frequencies as well as channels. The ability to detect nuanced phase variability in EEG signals holds incredible potential to augment our understanding of the role of phase information in neural processing more generally. Variability in phase measured with EEG has been shown to modulate the neural response to a stimulus [65–68], inﬂuence reaction times [69,70], and determine whether multisensory input is bound as a coherent percept [71]. Phase information within the neural response has been suggested to carry precise informational content [72,73] and may even be a component of the neural code [74]. Our results demonstrate that a deep learner may provide an innovative way to reveal robust phase variability between stimuli that underlie the intricate coordination of neural activity that gives rise to cognition.

#### 4.5 Limitations

Within this dataset, the impaired performance of Combined-CCA likely arose from insuﬃcient representation of the precise phase information across the 1s segments. Future research could investigate whether Combined-CCA could be adapted or used diﬀerently to better handle asynchronous operation. For example, provided that the BCI has knowledge of the phase of the stimulus, the template could be shifted so that its phase matches the phase of the stimulus. This may improve performance of Combined-CCA in an asynchronous setup. It is noteworthy though, that phase information of the stimulus is not available in all applications. Our Compact-CNN does not require phase information, suggesting its versatility for both experimental use and novel BCI applications.

Finally, our experimental setup did not include a non-control state, which is typically utilized in self-paced BCI systems. Future work could investigate the eﬃcacy of our method in the presence of a non-control state in a closed-loop setting, which could lead to even more ﬂexible and intuitive SSVEP-based human machine interaction.

### Acknowledgments

This research was supported by mission funding to the U.S. Army Research Laboratory and through Cooperative Agreement Number W911NF-10-2-0022. Support was also provided by the NSF under grant IIS-1527747. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the oﬃcial policies, either expressed or implied, of the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein.

### References

- [1] D. Regan, Human Brain Electrophysiology: Evoked Potentials and Evoked Magnetic Fields in Science and Medicine. Elsevier, 1989.
- [2] C. S. Herrmann, “Human EEG responses to 1-100 Hz ﬂicker: Resonance phenomena in visual cortex and their potential correlation to cognitive phenomena,” Experimental Brain Research, vol. 137, no. 3-4, pp. 346–353, 2001.
- [3] D. Regan, “Steady-state evoked potentials,” JOSA, vol. 67, no. 11, pp. 1475–1489, 1977.
- [4] E. Bas¸ar, EEG-brain dynamics: relation between EEG and brain evoked potentials. ElsevierNorth-Holland Biomedical Press, 1980.
- [5] D. Regan, “Human brain electrophysiology: evoked potentials and evoked magnetic ﬁelds in science and medicine,” 1989.
- [6] R. B. Silberstein, P. L. Nunez, A. Pipingas, P. Harris, and F. Danieli, “Steady state visually evoked potential (ssvep) topography in a graded working memory task,” International Journal of Psychophysiology, vol. 42, no. 2, pp. 219–232, 2001.
- [7] M. Marx, I. Bodis-Wollner, P. Bobak, C. Harnois, L. Mylin, and M. Yahr, “Temporal frequency-dependent vep changes in parkinson’s disease,” Vision research, vol. 26, no. 1, pp. 185–193, 1986.
- [8] B. A. Clementz, A. Keil, and J. Kissler, “Aberrant brain dynamics in schizophrenia: delayed buildup and prolonged decay of the visual steady-state response,” Cognitive brain research, vol. 18, no. 2, pp. 121–129, 2004.
- [9] G. Harding, A. J. Wilkins, G. Erba, G. L. Barkley, and R. S. Fisher, “Photic-and patterninduced seizures: Expert consensus of the epilepsy foundation of america working group,” Epilepsia, vol. 46, no. 9, pp. 1423–1425, 2005.

- [10] G. Tononi, R. Srinivasan, D. P. Russell, and G. M. Edelman, “Investigating neural correlates of conscious perception by frequency-tagged neuromagnetic responses,” Proceedings of the National Academy of Sciences, vol. 95, no. 6, pp. 3198–3203, 1998.
- [11] J. O. Garcia, R. Srinivasan, and J. T. Serences, “Near-real-time feature-selective modulations in human cortex,” Current Biology, vol. 23, no. 6, pp. 515–522, 2013.
- [12] J. R. Wolpaw, N. Birbaumer, D. J. McFarland, G. Pfurtscheller, and T. M. Vaughan, “Braincomputer interfaces for communication and control.” Clinical Neurophysiology, vol. 113, no. 6, pp. 767–91, jun 2002. [Online]. Available: http://www.ncbi.nlm.nih.gov/pubmed/12048038
- [13] N. R. Waytowich and D. J. Krusienski, “Multiclass steady-state visual evoked potential frequency evaluation using chirp-modulated stimuli.” IEEE transactions on Human-Machine Systems, vol. 46, no. 4, pp. 593–600, Aug 2016.
- [14] H. T. Hsu, I. H. Lee, H. T. Tsai, H. C. Chang, K. K. Shyu, C. C. Hsu, H. H. Chang, T. K. Yeh, C. Y. Chang, and P. L. Lee, “Evaluate the feasibility of using frontal ssvep to implement an ssvep-based bci in young, elderly and als groups,” IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 24, no. 5, pp. 603–615, May 2016.
- [15] Z. Lin, C. Zhang, W. Wu, and X. Gao, “Frequency recognition based on canonical correlation analysis for SSVEP-based BCIs.” IEEE Transactions on Bio-medical Engineering, vol. 54, no. 6 Pt 2, pp. 1172–6, jun 2007. [Online]. Available: http://www.ncbi.nlm.nih.gov/pubmed/ 17549911
- [16] G. Bin, X. Gao, Z. Yan, B. Hong, and S. Gao, “An online multi-channel ssvepbased brain-computer interface using a canonical correlation analysis method.” Journal of Neural Engineering, vol. 6, no. 4, p. 046002, Aug 2009. [Online]. Available: http://www.ncbi.nlm.nih.gov/pubmed/19494422
- [17] N. R. Waytowich and D. J. Krusienski, “Development of an extensible ssvep-bci software platform and application to wheelchair control,” in 2017 8th International IEEE/EMBS Conference on Neural Engineering (NER), May 2017, pp. 259–532.
- [18] M. Nakanishi, Y.-T. Y. Wang, Y. Mitsukura, and T.-P. Jung, “A high-speed brain speller using steady-state visual evoked potentials.” International journal of neural systems, vol. 24, no. 6, p. 1450019, sep 2014. [Online]. Available: http://www.ncbi.nlm.nih.gov/pubmed/25081427
- [19] X. Chen, Y. Wang, M. Nakanishi, X. Gao, T.-P. Jung, and S. Gao, “High-speed spelling with a noninvasive brain–computer interface,” Proceedings of the National Academy of Sciences, p. 201508080, 2015. [Online]. Available: http://www.pnas.org/lookup/doi/10.1073/ pnas.1508080112
- [20] N. R. Waytowich, J. Faller, J. O. Garcia, J. M. Vettel, and P. Sajda, “Unsupervised adaptive transfer learning for steady-state visual evoked potential brain-computer interfaces.” 2016 International Conference on Systems, Man, and Cybernetics (SMC), Oct 2016.
- [21] J. Schmidhuber, “Deep learning in neural networks: An overview,” arXiv, vol. abs/1404.7828,

2014. [Online]. Available: http://arxiv.org/abs/1404.7828

- [22] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” 5 2015.
- [23] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classiﬁcation with deep convolutional neural networks,” pp. 1097–1105, 2012. [Online]. Available: http://papers.nips. cc/paper/4824-imagenet-classiﬁcation-with-deep-convolutional-neural-networks.pdf
- [24] K. Simonyan and A. Zisserman, “Very deep convolutional networks for large-scale image recognition,” CoRR, vol. abs/1409.1556, 2014. [Online]. Available: http://arxiv.org/abs/ 1409.1556
- [25] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” CoRR, vol. abs/1512.03385, 2015. [Online]. Available: http://arxiv.org/abs/1512.03385
- [26] G. Huang, Z. Liu, K. Q. Weinberger, and L. van der Maaten, “Densely connected convolutional networks,” CoRR, vol. abs/1608.06993, 2016. [Online]. Available: http: //arxiv.org/abs/1608.06993
- [27] A. Antoniades, L. Spyrou, C. C. Took, and S. Sanei, “Deep learning for epileptic intracranial eeg data,” in 2016 IEEE 26th International Workshop on Machine Learning for Signal Processing (MLSP), Sept 2016, pp. 1–6.
- [28] J. Liang, R. Lu, C. Zhang, and F. Wang, “Predicting seizures from electroencephalography recordings: A knowledge transfer strategy,” in 2016 IEEE International Conference on Healthcare Informatics (ICHI), Oct 2016, pp. 184–191.
- [29] P. Thodoroﬀ, J. Pineau, and A. Lim, “Learning robust features using deep learning for automatic seizure detection,” CoRR, vol. abs/1608.00220, 2016. [Online]. Available: http://arxiv.org/abs/1608.00220
- [30] P. Mirowski, D. Madhavan, Y. LeCun, and R. Kuzniecky, “Classiﬁcation of patterns of {EEG} synchronization for seizure prediction,” Clinical Neurophysiology, vol. 120, no. 11, pp. 1927 – 1940, 2009.
- [31] M. L¨ngkvist, L. Karlsson, and A. Loutﬁ, “Sleep stage classiﬁcation using unsupervised feature learning,” Adv. Artif. Neu. Sys., vol. 2012, pp. 5:5–5:5, Jan. 2012. [Online]. Available: http://dx.doi.org/10.1155/2012/107046
- [32] R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter, K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, and T. Ball, “Deep learning with convolutional neural networks for eeg decoding and visualization,” Human Brain Mapping, vol. 38, no. 11, pp. 5391–5420, 2017. [Online]. Available: http://dx.doi.org/10.1002/hbm.23730
- [33] Y. R. Tabar and U. Halici, “A novel deep learning approach for classiﬁcation of eeg motor imagery signals,” Journal of Neural Engineering, vol. 14, no. 1, p. 016003, 2017. [Online]. Available: http://stacks.iop.org/1741-2552/14/i=1/a=016003
- [34] S. M. Gordon, M. Jaswa, A. J. Solon, and V. J. Lawhern, “Real world bci: Cross-domain learning and practical applications,” in Proceedings of the 2017 ACM Workshop on An Application-oriented Approach to BCI out of the Laboratory, ser. BCIforReal ’17. New York, NY, USA: ACM, 2017, pp. 25–28. [Online]. Available: http://doi.acm.org/10.1145/3038439.3038444

- [35] V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, and B. J. Lance, “Eegnet: a compact convolutional neural network for eeg-based brain–computer interfaces,” Journal of Neural Engineering, vol. 15, no. 5, p. 056013, 2018. [Online]. Available: http://stacks.iop.org/1741-2552/15/i=5/a=056013
- [36] H. Cecotti, “A time–frequency convolutional neural network for the oﬄine classiﬁcation of steady-state visual evoked potential responses,” Pattern Recognition Letters, vol. 32, no. 8, pp. 1145 – 1153, 2011. [Online]. Available: http://www.sciencedirect.com/science/article/pii/ S0167865511000651
- [37] N.-S. Kwak, K.-R. M¨uller, and S.-W. Lee, “A convolutional neural network for steady state visual evoked potential classiﬁcation under ambulatory environment,” PLOS ONE, vol. 12, no. 2, pp. 1–20, 02 2017. [Online]. Available: https://doi.org/10.1371/journal.pone.0172578
- [38] V. Bevilacqua, G. Tattoli, D. Buongiorno, C. Loconsole, D. Leonardis, M. Barsotti, A. Frisoli, and M. Bergamasco, “A novel bci-ssvep based approach for control of walking in virtual environment using a convolutional neural network,” in 2014 International Joint Conference on Neural Networks (IJCNN), July 2014, pp. 4121–4128.
- [39] M. Nakanishi, Y. Wang, Y.-T. Wang, and T.-P. Jung, “A comparison study of canonical correlation analysis based methods for detecting steady-state visual evoked potentials,” Plos One, vol. 10, no. 10, p. e0140703, 2015.
- [40] I. Sturm, S. Lapuschkin, W. Samek, and K.-R. M¨uller, “Interpretable deep neural networks for single-trial eeg classiﬁcation,” Journal of Neuroscience Methods, vol. 274, pp. 141 – 145, 2016. [Online]. Available: http://www.sciencedirect.com/science/article/pii/S0165027016302333
- [41] L. V. D. Maaten and G. Hinton, “Visualizing Data using t-SNE,” Journal of Machine Learning Research, vol. 9, pp. 2579–2605, 2008.
- [42] M. X. Cohen, Analyzing neural time series data: theory and practice. MIT press, 2014.
- [43] F. Chollet, “Xception: Deep learning with depthwise separable convolutions,” CoRR, vol. abs/1610.02357, 2016. [Online]. Available: http://arxiv.org/abs/1610.02357
- [44] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving, M. Isard, M. Kudlur, J. Levenberg, R. Monga, S. Moore, D. G. Murray, B. Steiner, P. Tucker, V. Vasudevan, P. Warden, M. Wicke, Y. Yu, and X. Zheng, “Tensorﬂow: A system for large-scale machine learning,” in Proceedings of the 12th USENIX Conference on Operating Systems Design and Implementation, ser. OSDI’16. Berkeley, CA, USA: USENIX Association, 2016, pp. 265–283. [Online]. Available: http://dl.acm.org/citation.cfm?id=3026877.3026899
- [45] F. Chollet et al., “Keras,” https://github.com/keras-team/keras, 2015.
- [46] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” arXiV, vol. abs/1412.6980, 2014. [Online]. Available: http://arxiv.org/abs/1412.6980
- [47] I. Goodfellow, J. Shlens, and C. Szegedy, “Explaining and harnessing adversarial examples,” 12 2014.

- [48] A. M. Nguyen, J. Yosinski, and J. Clune, “Deep neural networks are easily fooled: High conﬁdence predictions for unrecognizable images,” CoRR, vol. abs/1412.1897, 2014. [Online]. Available: http://arxiv.org/abs/1412.1897
- [49] S. G. Mason, A. Bashashati, M. Fatourechi, K. F. Navarro, and G. E. Birch, “A comprehensive survey of brain interface technology designs,” Annals of Biomedical Engineering, vol. 35, no. 2, pp. 137–169, 2007.
- [50] P. F. Diez, S. M. T. Mu¨ller, V. A. Mut, E. Laciar, E. Avila, T. F. Bastos-Filho, and M. Sarcinelli-Filho, “Commanding a robotic wheelchair with a high-frequency steady state visual evoked potential based brain-computer interface,” Medical Engineering and Physics, vol. 35, no. 8, pp. 1155–1164, 2013.
- [51] G. R. Mu¨ller-Putz, R. Scherer, G. Pfurtscheller, and R. Rupp, “Brain-computer interfaces for control of neuroprostheses: from synchronous to asynchronous mode of operation,” Biomedizinische Technik, vol. 51, no. 2, pp. 57–63, 2006.
- [52] N. S. Kwak, K.-R. Mu¨ller, and S. W. Lee, “A lower limb exoskeleton control system based on steady state visual evoked potentials,” Journal of Neural Engineering, vol. 12, no. 5, p. 056009, 2015.
- [53] J. Leg´eny, R. V. Abad, and A. L´ecuyer, “Navigating in virtual worlds using a self-paced SSVEP-based brain-computer interface with integrated stimulation and real-time feedback,” Presence: Teleoperators and Virtual Environments, vol. 20, no. 6, pp. 529–544, 2011.
- [54] N. R. Waytowich, Y. Yamani, and D. J. Krusienski, “Optimization of checkerboard spatial frequencies for steady-state visual evoked potential brain-computer interfaces.” IEEE transactions on neural systems and rehabilitation engineering : a publication of the IEEE Engineering in Medicine and Biology Society, vol. 25, no. 6, pp. 557–565, Jun 2017. [Online]. Available: http://www.ncbi.nlm.nih.gov/pubmed/27542113
- [55] J. Faller, B. Z. Allison, C. Brunner, and R. Scherer, “A feasibility study on SSVEP-based interaction with motivating and immersive virtual and augmented reality,” Graz University of Technology, Tech. Rep., 2010.
- [56] N. R. Waytowich, V. J. Lawhern, A. W. Bohannon, K. R. Ball, and B. J. Lance, “Spectral transfer learning using information geometry for a user-independent braincomputer interface,” Frontiers in Neuroscience, vol. 10, p. 430, 2016. [Online]. Available: https://www.frontiersin.org/article/10.3389/fnins.2016.00430
- [57] G. Pfurtscheller and F. L. da Silva, “Event-related eeg/meg synchronization and desynchronization: basic principles,” Clinical Neurophysiology, vol. 110, no. 11, pp. 1842 – 1857, 1999. [Online]. Available: http://www.sciencedirect.com/science/article/pii/ S1388245799001418
- [58] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning. MIT Press, 2016, http://www. deeplearningbook.org.

- [59] T. Wiatowski and H. B¨lcskei, “A mathematical theory of deep convolutional neural networks for feature extraction,” IEEE Transactions on Information Theory, vol. 64, no. 3, pp. 1845– 1866, March 2018.
- [60] S. Mallat, “Understanding deep convolutional networks,” Philosophical Transactions of the Royal Society of London A: Mathematical, Physical and Engineering Sciences, vol. 374, no. 2065, 2016. [Online]. Available: http://rsta.royalsocietypublishing.org/content/374/2065/ 20150203
- [61] S. Itthipuripat, J. O. Garcia, and J. T. Serences, “Temporal dynamics of divided spatial attention,” Journal of neurophysiology, vol. 109, no. 9, pp. 2364–2373, 2013.
- [62] S. Hanslmayr, A. Aslan, T. Staudigl, W. Klimesch, C. S. Herrmann, and K.-H. B¨uml, “Prestimulus oscillations predict visual perception performance between and within subjects,” Neuroimage, vol. 37, no. 4, pp. 1465–1473, 2007.
- [63] K. E. Mathewson, G. Gratton, M. Fabiani, D. M. Beck, and T. Ro, “To see or not to see: prestimulus α phase predicts visual awareness,” Journal of Neuroscience, vol. 29, no. 9, pp. 2725–2732, 2009.
- [64] J. R. Brooks, J. O. Garcia, S. E. Kerick, and J. M. Vettel, “Diﬀerential functionality of right and left parietal activity in controlling a motor vehicle,” Frontiers in Systems Neuroscience, vol. 10, Dec 2016. [Online]. Available: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5187452/
- [65] R. J. Barry, J. A. Rushby, S. J. Johnstone, A. R. Clarke, R. J. Croft, and C. A. Lawrence, “Event-related potentials in the auditory oddball as a function of eeg alpha phase at stimulus onset,” Clinical Neurophysiology, vol. 115, no. 11, pp. 2593–2601, 2004.
- [66] S. Makeig, M. Westerﬁeld, T.-P. Jung, S. Enghoﬀ, J. Townsend, E. Courchesne, and T. J. Sejnowski, “Dynamic brain sources of visual evoked responses,” Science, vol. 295, no. 5555, pp. 690–694, 2002.
- [67] B. H. Jansen and M. E. Brandt, “The eﬀect of the phase of prestimulus alpha activity on the averaged visual evoked response,” Electroencephalography and Clinical Neurophysiology/Evoked Potentials Section, vol. 80, no. 4, pp. 241–250, 1991.
- [68] A. R. Haig and E. Gordon, “Prestimulus eeg alpha phase synchronicity inﬂuences n100 amplitude and reaction time,” Psychophysiology, vol. 35, no. 5, pp. 591–595, 1998.
- [69] E. Callaway and C. L. Yeager, “Relationship between reaction time and electroencephalographic alpha phase,” Science, vol. 132, no. 3441, pp. 1765–1766, 1960.
- [70] R. E. Dustman and E. C. Beck, “Phase of alpha brain waves, reaction time and visually evoked potentials,” Electroencephalography and clinical neurophysiology, vol. 18, no. 5, pp. 433–440, 1965.
- [71] N. van Atteveldt, M. M. Murray, G. Thut, and C. E. Schroeder, “Multisensory integration: ﬂexible use of general operations,” Neuron, vol. 81, no. 6, pp. 1240–1253, 2014.
- [72] J. J. Hopﬁeld, “Pattern recognition computation using action potential timing for stimulus representation,” Nature, vol. 376, no. 6535, p. 33, 1995.

- [73] O. Jensen and J. E. Lisman, “Position reconstruction from an ensemble of hippocampal place cells: contribution of theta phase coding,” Journal of neurophysiology, vol. 83, no. 5, pp. 2602–2609, 2000.
- [74] D. H. Perkel and T. H. Bullock, “Neural coding.” Neurosciences Research Program Bulletin, 1968.

