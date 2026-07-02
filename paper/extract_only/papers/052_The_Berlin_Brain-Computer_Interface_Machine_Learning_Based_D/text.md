Journal of Universal Computer Science, vol. 12, no. 6 (2006), 581-607 submitted: 31/5/06, accepted: 23/6/06, appeared: 28/6/06 © J.UCS

### The Berlin Brain-Computer Interface: Machine Learning Based Detection of User Speciﬁc Brain States

Benjamin Blankertz, Guido Dornhege, Steven Lemm (Fraunhofer FIRST (IDA), Berlin, Germany {blanker,dornhege,lemm}@ﬁrst.fraunhofer.de)

Matthias Krauledat (Technical University Berlin, Germany matthias.krauledat@ﬁrst.fhg.de)

Gabriel Curio (Dept. of Neurology, Campus Benjamin Franklin, Charité University Medicine Berlin, Berlin, Germany gabriel.curio@charite.de)

Klaus-Robert Müller (Fraunhofer FIRST (IDA), Berlin, Germany and University of Potsdam, Germany klaus@ﬁrst.fhg.de)

Abstract: We outline the Berlin Brain-Computer Interface (BBCI), a system which enables us to translate brain signals from movements or movement intentions into control commands. The main contribution of the BBCI, which is a non-invasive EEG-based BCI system, is the use of advanced machine learning techniques that allow to adapt to the speciﬁc brain signatures of each user with literally no training. In BBCI a calibration session of about 20min is necessary to provide a data basis from which the individualized brain signatures are inferred. This is very much in contrast to conventional BCI approaches that rely on operand conditioning and need extensive subject training of the order 50-100 hours. Our machine learning concept thus allows to achieve high quality feedback already after the very ﬁrst session. This work reviews a broad range of investigations and experiments that have been performed within the BBCI project. In addition to these general paradigmatic BCI results, this work provides a condensed outline of the underlying machine learning and signal processing techniques that make the BBCI succeed. In the ﬁrst experimental paradigm we analyze the predictability of limb movement long before the actual movement takes place using only the movement intention measured from the pre-movement (readiness) EEG potentials. The experiments include both off-line studies and an online feedback paradigm. The limits with respect to the spatial resolution of the somatotopy are explored by contrasting brain patterns of movements of left vs. right hand rsp. foot. In a second complementary paradigm voluntary modulations of sensorimotor rhythms caused by motor imagery (left hand vs. right hand vs. foot) are translated into a continuous feedback signal. Here we report results of a recent feedback study with 6 healthy subjects with no or very little experience with BCI control: half of the subjects achieved an information transfer rate above 35 bits per minute (bpm). Furthermore one subject used the BBCI to operate a mental typewriter in free spelling mode. The overall spelling speed was 4.5-8 letters per minute including the time needed for the correction errors.

Key Words: Brain-Computer Interface, Classiﬁcation, Common Spatial Patterns, EEG, ERD, Event-Related Desynchronization, Feedback, Information Transfer Rate, Readiness Potential, RP, Machine Learning, Single-Trial Analysis

Category: G.1.6, H.1.1, H.1.2, I.2.1, I.2.6, I.5, J.2, J.3, J.7

#### 1 Introduction

A Brain-Computer Interface (BCI) is a man-to-machine communication channel operating solely on brain signatures independent from muscular output, see [Wolpaw et al., 2002,Kübler et al., 2001,Curran and Stokes, 2003,Dornhege et al., 2006c] for a broad overview. The Berlin Brain-Computer Interface (BBCI) is a non-invasive, EEGbased system whose key features are (1) the use of well-established motor competences as control paradigms, (2) high-dimensional features derived from 128-channel EEG, (3) advanced machine learning techniques, and—as a consequence—(4) no need for subject training.

##### 1.1 Why Machine Learning for Brain-Computer Interfacing?

Traditional neurophysiologytypically investigates the average brain. As a simple example, an investigation of the neural correlates of motor preparation of index ﬁnger movements would involve a number of subjects doing repeatedly such movements. A grand average over all trials and all subjects will then reveal the generic result, a pronounced cortical negativation which is focused in the corresponding (contralateral) motor area. On the other hand comparing intra-subject averages, cf. Fig. 1, shows a huge subjectto-subject variability, i.e., a large amount of variance in the grand average that was not explained. (See Section 2.1 for a detailed description of the experiment.) Now let us go one step further restricting the investigation to one subject. Comparing the session-wise averages in two (motor imagery) tasks between the sessions recorded on different days we encounter again a huge variability (session-to-session variability), cf. Fig. 2. (See Section 3.1 for a detailed description of the experiment.) When it comes to real-time feedback as in brain-computer interfaces we still have to go one step further. The system needs to be able to identify the mental state of a subject based on one single-trial (duration ≤ 1 s) of brain signals. Fig. 3 demonstrates the huge trial-to-trial variance in one subject in one session (the experiment being the same as above). Nevertheless our BBCI system was able to classify all those trials correctly.The tackling of the enormous trial-to-trial variability is a major challenge in BCI research. Given the high subject-tosubject variability it seems reasonable to have a system that adapts to the speciﬁc brain signatures of each user. We believe that advanced techniques for machine learning are an essential tool in this endeavor.

This idea contrasts with the operant conditioning variant of BCI, in which the subject learns by neurofeedback to control a speciﬁc EEG feature which is hard-wired in

1 2 3 4 5 6

leftright

- Figure 1: Six subjects performed left vs. right hand index ﬁnger tapping. Even though the kind of movement was very much the same in each subject and the task involves a highly overlearned motor competence, the premovement potantial maps (−200 to −100ms before keypress; blue means negative, red means positive potential) exhibit a great diversity between subjects.

leftright

- Figure 2: One subject imagined left vs. right hand movements on different days. The maps show spectral power in the alpha frequency band. Even though the maps represent averages across 140 trials each, they exhibit an apparent diversity.

the BCI system, [Elbert et al., 1980, Rockstroh et al., 1984, Birbaumer et al., 2000]. According to the motto ‘let the machines learn’ our approach minimizes the need for subject training and copes with all kinds of variabilities demonstrated above.

##### 1.2 Overview of this paper

We present two aspects of the BBCI project. The ﬁrst is based on the discriminability of premovement potentials in voluntary movements. Our initial studies ( [Blankertz et al.,

[Figure 1]

- Figure 3: One subject imagined left (red) vs. right (green) hand movements. The topographies show spectral power in the alpha frequency range during single-trials of 3.5 s duration. These patterns exhibit an extreme diversity although recorded from one subject on one day.

2003]) show that high information transfer rates can be obtained from single-trial classiﬁcation of fast-paced motor commands. Additional investigations – however beyond the scope of this paper – point out ways of improving bit rates further, e.g., by extending the class of detectable movement related brain signals to the ones encountered, e.g. when moving single ﬁngers within one hand.

In a second step we established a BCI system based on motor imagery. A recent feedback study ( [Blankertz et al., 2006]) demonstrated the power of the BBCI approach for 6 healthy subjects with no or very little experience of BCI control : 3 subjects could achieve an information transfer rate above 35 bits per minute (bpm), and further two subjects above 24 and 15 bpm, while one subject had no BCI control. These results indicate that higher transfer rates can be achieved when comparing to classical conditioning approaches, even though our subjects were untrained. We would like to reiterate that the BBCI approach is non-invasive. In Section 2 we present single-trial investigations of premovement potentials including online feedback (2.3). In Section 3 we present our BBCI feedback system based on motor imagery and the results of a systematic feedback study (3.3). Section 3.4 gives evidence that the control is solely dependent on central nervous system activity. Section 4 uses machine learning to not only classify and predict but even to explain the underlying structure of the EEG data. In Section 5 we point out lines of further improvementbefore the concludingdiscussion 6.

#### 2 Premovement Potentials in Executed Movements

In our ﬁrst paradigm we studied the pre-movement potentials in overlearned movements, like typewriting on a computer keyboard. Our aim here was to build a classiﬁer based on the Bereitschaftspotential (BP, or readiness potential) which is capable of detecting movement intentions and predicting the type of intended movement (e.g. left vs. right hand) before EMG onset. The basic rationale behind letting healthy subjects actually perform the movements in contrast to movement imagination is that the latter poses a dual task (motor command preparation plus vetoing the actual movement). This suggests that movement imagination by healthy subjects might not guarantee an appropriate correspondence to paralyzed patients as the latter will emit the motor command without veto (but see [Kübler et al., 2005] for a study showing that ALS patients can indeed use modulations of sensorimotor rhythms for BCI control). In order to allow a safe transfer of the results in our setting to paralyzed patients it is essential to make predictions about imminent movements prior to any EMG activity to exclude a possible confound with afferent feedback from muscle and joint receptors contingent upon an executed movement. Being able to predict movements in real time before the EMG activity starts, opens interesting perspectives for assistance of action control in time-critical behavioral contexts, an idea further pursued in [Krauledat et al., 2004].

##### 2.1 Left vs. Right Hand Finger Movements

Our goal is to predict in single-trials the laterality of imminent left vs. right ﬁnger movements at a time point prior to the start of EMG activity. The speciﬁc feature that we use is the readiness potential (LR, or Bereitschaftspotential),which is a transient postsynaptic responseof main pyramidalperi-centralneurons,see [Kornhuberand Deecke, 1965]. It leads to a pronouncedcortical negativationwhich is focused in the correspondingmotor area, i.e., contralateral to the performing limb reﬂecting movement preparation, see Fig. 4. Neurophysiologically, the RP is well investigated and described, cf. [Kornhuber and Deecke, 1965,Lang et al., 1989,Cui et al., 1999]. New questions that arise in this context are (a) can the lateralization be discriminated on a single-trial basis, and (b) does the refractory behavior allow to observe the RP also in fast motor sequences? Our investigations provided positive answers to both questions.

In a series of experiments healthy volunteers performed self-paced ﬁngermovements on a computer keyboard with approximate tap-rates of 30, 45, 60 and 120 taps per minute (tpm). EEG was recorded from 128 Ag/AgCl scalp electrodes (except for some experiments summarized in Fig. 5 which were recorded with 32 channels). To relate the prediction accuracy with the timing of EMG activity we recorded electromyogram (EMG) from M. ﬂexor digitorum communis from both sides. Also electrooculo-

|CCP3|
|---|
|EMG|

|CCP4|
|---|
|EMG|

|left right<br><br>|
|---|

2

2

0

0

−2

−2

−4

−4

μ[V]

μ[V]

−6

−6

−8

[Figure 2]

−5 0 5

−800 −400 0

−800 −400 0

[uV]

[ms]

[ms]

- Figure 4: Response averaged event-related potentials (ERPs) of one right-handed subject in a left vs. right hand ﬁnger tapping experiment(N =275 resp. 283 trials per class). Finger movements were executed self-paced, i.e., without any external cue, in an approximate inter-trial interval of 2 seconds. The two scalp plots show a topographical mapping of scalp potentials averaged within the interval -220 to -120ms relative to keypress (time interval shaded in the ERP plots). Larger crosses indicate the position of the electrodes CCP3 and CCP4 for which the time course of the ERPs is shown in the subplots at both sides. For comparison time courses of EMG activity for left and right ﬁnger movements are added. EMG activity starts after -120ms and reaches a peak of 70μV at -50ms. The readiness potential is clearly visible, a predominantly contralateral negativation starting about 600ms before movement and raising approximately until EMG onset.

gram (EOG) was recorded to control for the inﬂuence of eye movements, cf. Fig. 8. No trials have been discarded from analysis.

The ﬁrst step towards RP-based feedbackis evaluating the predictability of the laterality of upcoming movements. We determined the time point of EMG onset by inspecting classiﬁcation performance based on EMG-signals (like in Fig. 8) and used it as end point of the windows from which features for the EEG-based classiﬁcation analysis were extracted. For the data set shown in Fig. 4 the chosen time point is -120ms which is in coincidence with the onset seen in averaged EMG activity. The choice of the relative position of the classiﬁcation window with respect to the keypress makes sure that the prediction does not rely on brain signals from afferent nerves. The extraction of the RP features and the classiﬁcation techniques are described in section 2.2. The result of EEG-based classiﬁcation for all subjects is shown in Fig. 5 where the cross-validation performance is quantiﬁed in bits per minute (according to Shannon’s formula) in order to trade-off accuracy vs. decision speed. A discussion of the possible inﬂuence of noncentral nervous system activity on the classﬁcation can be found in the next section 2.3,

60

|best subject other subjects<br><br>|
|---|

50

bitsperminute

40

30

20

10

0

20 40 60 80 100 120 140

taps per minute

- Figure 5: Tapping rates [taps per minute] vs. information transfer rate as calculated by Shannon’s formula from the cross-validation error for different subjects peforming selfpaced tapping at different average tapping rates with ﬁngers of the left and the right hand. The results of the best subject (marked by red dots) were conﬁrmed in several experiments.

especially in Fig. 8.

The results indicate that the refractoryperiod of the RP is short enoughto effectively discriminate pre-movement potentials in ﬁnger movement sequences as fast as 2 taps per second. On the other hand it turned out that the performance of RP-based premovement potential detection in a self-paced paradigm is highly subject-speciﬁc. Further investigations have studied event-related desynchronization (ERD) effects in the μand β frequency range, cf. [Pfurtscheller and da Silva, 1999], compare systematically the discriminability of different features and combined RP+ERD features, cf. [Dornhege et al., 2004], and search for modiﬁcations in the experimental setup in order to gain high performance for a broader range of subjects.

##### 2.2 Preprocessing and Classiﬁcation

The following feature extraction method is speciﬁcally tailored to extract information from the readiness potential. It extracts the low frequency content with an emphasis on the late part of the signal, where the information content can be expected to be largest in pre-movement trials. Starting points are epochs of 128 samples (i.e. 1280ms) of raw EEG data as depicted in Fig. 6 (a) for one channel.To emphasize the late signal content, the signal is convoluted with one-sided cosine window (Fig. 6 (b))

w(n) := 1−cos(nπ/128) for n = 0,...,127,

###### (a) raw EEG signal

###### (b) windowing

20

20

μ[V]

μ[V]

0

0

|windowed signal window|
|---|

−20

−20

−1200 −1000 −800 −600 −400 −200

−1200 −1000 −800 −600 −400 −200

time [ms]

time [ms]

###### (c) Fourier coefficients (mag. shown)

###### (d) filtering and subsampling

150

10

←baselineonly

|discarded bins selected bins|
|---|

5

100

δ ϑ α

μ[V]

0

50

−5

|filtered signal feature values|
|---|

0

−10

0 2 4 6 8 10

−1200 −1000 −800 −600 −400 −200

Frequency [Hz]

time [ms]

- Figure 6: This example shows the feature calculation in one channel of a pre-movement trial [−1400−120] ms with keypress at t = 0ms. The pass-band for the FT ﬁltering is 0.4–3.5Hz and the subsampling rate is 20Hz. Features are extracted only from the last 200ms (shaded) where most information on the upcoming movement is expected.

before applying a Fourier transform (FT) ﬁltering technique: from the complex-valued FT coefﬁcients all are discarded but the ones in the pass-band (including the negative frequencies, which are not shown), (Fig. 6 (c)). Transforming the selected bins back into the time domain gives the smoothed signal of which the last 200ms are subsampled at 20Hz resulting in 4 feature components per channel (Fig. 6 (d)). The full (RP-) feature vector is the concatenation of those values from all channels for the given time window. For online operation those features are calculated every 40ms from sliding windows.

Due to our observation that RP-features under particular movement conditions are normally distributed with equal covariance matrices ( [Blankertz et al., 2003]), the classiﬁcation problem meets the assumption of being optimally separated by a linear hyperplane. The data processing described above preserves gaussianity, hence we classify with regularized linear discriminant analysis (RLDA, see [Friedman, 1989]). Regularization is needed to avoid overﬁtting since we are dealing with a high-dimensional

[−270 ms]

[−220 ms]

[−170 ms]

[−120 ms]

[Figure 3]

[Figure 4]

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

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

[Figure 212]

[Figure 213]

[Figure 214]

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

[Figure 219]

[Figure 220]

[Figure 221]

[Figure 222]

[Figure 223]

[Figure 224]

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

[Figure 238]

[Figure 239]

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

[Figure 247]

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

[Figure 258]

[Figure 259]

[Figure 260]

[Figure 261]

[Figure 262]

[Figure 263]

[Figure 264]

[Figure 265]

[Figure 266]

[Figure 267]

[Figure 268]

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

[Figure 275]

[Figure 276]

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

[Figure 284]

[Figure 285]

[Figure 286]

[Figure 287]

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

[Figure 294]

[Figure 295]

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

[Figure 302]

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

[Figure 316]

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

[Figure 322]

[Figure 323]

[Figure 324]

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

[Figure 333]

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

[Figure 339]

[Figure 340]

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

[Figure 345]

[Figure 346]

[Figure 347]

[Figure 348]

[Figure 349]

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

[Figure 354]

[Figure 355]

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

[Figure 360]

[Figure 361]

[Figure 362]

[Figure 363]

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

[Figure 368]

[Figure 369]

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

[Figure 395]

[Figure 396]

[Figure 397]

[Figure 398]

[Figure 399]

[Figure 400]

[Figure 401]

[Figure 402]

[Figure 403]

[Figure 404]

[Figure 405]

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

[Figure 425]

[Figure 426]

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

[Figure 431]

[Figure 432]

[Figure 433]

[Figure 434]

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

[Figure 440]

[Figure 441]

[Figure 442]

[Figure 443]

[Figure 444]

[Figure 445]

[Figure 446]

[Figure 447]

[Figure 448]

[Figure 449]

[Figure 450]

[Figure 451]

[Figure 452]

[Figure 453]

[Figure 454]

[Figure 455]

[Figure 456]

[Figure 457]

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

[Figure 463]

[Figure 464]

[Figure 465]

[Figure 466]

[Figure 467]

[Figure 468]

[Figure 469]

[Figure 470]

[Figure 471]

[Figure 472]

[Figure 473]

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

[Figure 479]

[Figure 480]

[Figure 481]

[Figure 482]

[Figure 483]

[Figure 484]

[Figure 485]

[Figure 486]

[Figure 487]

[Figure 488]

[Figure 489]

[Figure 490]

[Figure 491]

[Figure 492]

[Figure 493]

[Figure 494]

[Figure 495]

[Figure 496]

[Figure 497]

[Figure 498]

[Figure 499]

[Figure 500]

[Figure 501]

[Figure 502]

[Figure 503]

[Figure 504]

[Figure 505]

[Figure 506]

[Figure 507]

[Figure 508]

[Figure 509]

[Figure 510]

[Figure 511]

[Figure 512]

[Figure 513]

[Figure 514]

[Figure 515]

[Figure 516]

[Figure 517]

[Figure 518]

[Figure 519]

[Figure 520]

[Figure 521]

[Figure 522]

[Figure 523]

[Figure 524]

[Figure 525]

[Figure 526]

[Figure 527]

[Figure 528]

[Figure 529]

[Figure 530]

[Figure 531]

[Figure 532]

[Figure 533]

[Figure 534]

[Figure 535]

[Figure 536]

[Figure 537]

[Figure 538]

[Figure 539]

[Figure 540]

[Figure 541]

[Figure 542]

[Figure 543]

[Figure 544]

[Figure 545]

[Figure 546]

[Figure 547]

[Figure 548]

[Figure 549]

[Figure 550]

[Figure 551]

[Figure 552]

[Figure 553]

[Figure 554]

[Figure 555]

[Figure 556]

[Figure 557]

[Figure 558]

[Figure 559]

[Figure 560]

[Figure 561]

[Figure 562]

[Figure 563]

[Figure 564]

[Figure 565]

[Figure 566]

[Figure 567]

[Figure 568]

[Figure 569]

[Figure 570]

[Figure 571]

[Figure 572]

[Figure 573]

[Figure 574]

[Figure 575]

[Figure 576]

[Figure 577]

[Figure 578]

[Figure 579]

[Figure 580]

[Figure 581]

[Figure 582]

[Figure 583]

[Figure 584]

[Figure 585]

[Figure 586]

[Figure 587]

[Figure 588]

[Figure 589]

[Figure 590]

[Figure 591]

[Figure 592]

[Figure 593]

[Figure 594]

[Figure 595]

[Figure 596]

[Figure 597]

[Figure 598]

[Figure 599]

[Figure 600]

[Figure 601]

[Figure 602]

[Figure 603]

[Figure 604]

[Figure 605]

[Figure 606]

[Figure 607]

[Figure 608]

[Figure 609]

[Figure 610]

[Figure 611]

[Figure 612]

[Figure 613]

[Figure 614]

[Figure 615]

[Figure 616]

[Figure 617]

[Figure 618]

[Figure 619]

[Figure 620]

[Figure 621]

[Figure 622]

[Figure 623]

[Figure 624]

[Figure 625]

[Figure 626]

[Figure 627]

[Figure 628]

[Figure 629]

[Figure 630]

[Figure 631]

[Figure 632]

[Figure 633]

[Figure 634]

[Figure 635]

[Figure 636]

[Figure 637]

[Figure 638]

[Figure 639]

[Figure 640]

[Figure 641]

[Figure 642]

[Figure 643]

[Figure 644]

[Figure 645]

[Figure 646]

[Figure 647]

[Figure 648]

[Figure 649]

[Figure 650]

[Figure 651]

[Figure 652]

[Figure 653]

[Figure 654]

[Figure 655]

[Figure 656]

[Figure 657]

[Figure 658]

[Figure 659]

[Figure 660]

[Figure 661]

[Figure 662]

[Figure 663]

[Figure 664]

[Figure 665]

[Figure 666]

[Figure 667]

[Figure 668]

[Figure 669]

[Figure 670]

[Figure 671]

[Figure 672]

[Figure 673]

[Figure 674]

[Figure 675]

[Figure 676]

[Figure 677]

[Figure 678]

[Figure 679]

[Figure 680]

[Figure 681]

[Figure 682]

[Figure 683]

[Figure 684]

[Figure 685]

[Figure 686]

[Figure 687]

[Figure 688]

[Figure 689]

[Figure 690]

[Figure 691]

[Figure 692]

[Figure 693]

[Figure 694]

[Figure 695]

[Figure 696]

[Figure 697]

[Figure 698]

[Figure 699]

[Figure 700]

[Figure 701]

[Figure 702]

[Figure 703]

[Figure 704]

[Figure 705]

[Figure 706]

[Figure 707]

[Figure 708]

[Figure 709]

[Figure 710]

[Figure 711]

[Figure 712]

[Figure 713]

[Figure 714]

[Figure 715]

[Figure 716]

[Figure 717]

[Figure 718]

[Figure 719]

[Figure 720]

[Figure 721]

[Figure 722]

[Figure 723]

[Figure 724]

[Figure 725]

[Figure 726]

[Figure 727]

[Figure 728]

[Figure 729]

[Figure 730]

[Figure 731]

[Figure 732]

[Figure 733]

[Figure 734]

[Figure 735]

[Figure 736]

[Figure 737]

[Figure 738]

[Figure 739]

[Figure 740]

[Figure 741]

[Figure 742]

[Figure 743]

[Figure 744]

[Figure 745]

[Figure 746]

[Figure 747]

[Figure 748]

[Figure 749]

[Figure 750]

[Figure 751]

[Figure 752]

[Figure 753]

[Figure 754]

[Figure 755]

[Figure 756]

[Figure 757]

[Figure 758]

[Figure 759]

[Figure 760]

[Figure 761]

[Figure 762]

[Figure 763]

[Figure 764]

[Figure 765]

[Figure 766]

[Figure 767]

[Figure 768]

[Figure 769]

[Figure 770]

[Figure 771]

[Figure 772]

[Figure 773]

[Figure 774]

[Figure 775]

[Figure 776]

[Figure 777]

[Figure 778]

[Figure 779]

[Figure 780]

[Figure 781]

[Figure 782]

[Figure 783]

[Figure 784]

[Figure 785]

[Figure 786]

[Figure 787]

[Figure 788]

[Figure 789]

[Figure 790]

[Figure 791]

[Figure 792]

[Figure 793]

[Figure 794]

[Figure 795]

[Figure 796]

[Figure 797]

[Figure 798]

[Figure 799]

[Figure 800]

[Figure 801]

[Figure 802]

[Figure 803]

[Figure 804]

[Figure 805]

[Figure 806]

[Figure 807]

[Figure 808]

[Figure 809]

[Figure 810]

[Figure 811]

[Figure 812]

[Figure 813]

[Figure 814]

[Figure 815]

[Figure 816]

[Figure 817]

[Figure 818]

[Figure 819]

[Figure 820]

[Figure 821]

[Figure 822]

[Figure 823]

[Figure 824]

[Figure 825]

[Figure 826]

[Figure 827]

[Figure 828]

[Figure 829]

[Figure 830]

[Figure 831]

[Figure 832]

[Figure 833]

[Figure 834]

[Figure 835]

[Figure 836]

[Figure 837]

[Figure 838]

[Figure 839]

[Figure 840]

[Figure 841]

[Figure 842]

[Figure 843]

[Figure 844]

[Figure 845]

[Figure 846]

[Figure 847]

[Figure 848]

[Figure 849]

[Figure 850]

[Figure 851]

[Figure 852]

[Figure 853]

[Figure 854]

[Figure 855]

[Figure 856]

[Figure 857]

[Figure 858]

[Figure 859]

[Figure 860]

[Figure 861]

[Figure 862]

[Figure 863]

[Figure 864]

[Figure 865]

[Figure 866]

[Figure 867]

[Figure 868]

[Figure 869]

[Figure 870]

[Figure 871]

[Figure 872]

[Figure 873]

[Figure 874]

[Figure 875]

[Figure 876]

[Figure 877]

[Figure 878]

[Figure 879]

[Figure 880]

[Figure 881]

[Figure 882]

[Figure 883]

[Figure 884]

[Figure 885]

[Figure 886]

[Figure 887]

[Figure 888]

[Figure 889]

[Figure 890]

[Figure 891]

[Figure 892]

[Figure 893]

[Figure 894]

[Figure 895]

[Figure 896]

[Figure 897]

[Figure 898]

[Figure 899]

[Figure 900]

[Figure 901]

[Figure 902]

[Figure 903]

[Figure 904]

[Figure 905]

[Figure 906]

[Figure 907]

[Figure 908]

[Figure 909]

[Figure 910]

[Figure 911]

[Figure 912]

[Figure 913]

[Figure 914]

[Figure 915]

[Figure 916]

[Figure 917]

[Figure 918]

[Figure 919]

[Figure 920]

[Figure 921]

[Figure 922]

[Figure 923]

[Figure 924]

[Figure 925]

[Figure 926]

[Figure 927]

[Figure 928]

[Figure 929]

[Figure 930]

[Figure 931]

[Figure 932]

[Figure 933]

[Figure 934]

[Figure 935]

[Figure 936]

[Figure 937]

[Figure 938]

[Figure 939]

[Figure 940]

[Figure 941]

[Figure 942]

[Figure 943]

[Figure 944]

[Figure 945]

[Figure 946]

[Figure 947]

[Figure 948]

[Figure 949]

[Figure 950]

[Figure 951]

[Figure 952]

[Figure 953]

[Figure 954]

[Figure 955]

[Figure 956]

[Figure 957]

[Figure 958]

[Figure 959]

[Figure 960]

[Figure 961]

[Figure 962]

[Figure 963]

[Figure 964]

[Figure 965]

[Figure 966]

[Figure 967]

[Figure 968]

[Figure 969]

[Figure 970]

[Figure 971]

[Figure 972]

[Figure 973]

[Figure 974]

[Figure 975]

[Figure 976]

[Figure 977]

[Figure 978]

[Figure 979]

[Figure 980]

[Figure 981]

[Figure 982]

[Figure 983]

[Figure 984]

[Figure 985]

[Figure 986]

[Figure 987]

[Figure 988]

[Figure 989]

[Figure 990]

[Figure 991]

[Figure 992]

[Figure 993]

[Figure 994]

[Figure 995]

[Figure 996]

[Figure 997]

[Figure 998]

[Figure 999]

[Figure 1000]

[Figure 1001]

[Figure 1002]

[Figure 1003]

[Figure 1004]

[Figure 1005]

[Figure 1006]

[Figure 1007]

[Figure 1008]

[Figure 1009]

[Figure 1010]

[Figure 1011]

[Figure 1012]

[Figure 1013]

[Figure 1014]

[Figure 1015]

[Figure 1016]

[Figure 1017]

[Figure 1018]

[Figure 1019]

[Figure 1020]

[Figure 1021]

[Figure 1022]

[Figure 1023]

[Figure 1024]

[Figure 1025]

[Figure 1026]

[Figure 1027]

[Figure 1028]

[Figure 1029]

[Figure 1030]

[Figure 1031]

[Figure 1032]

[Figure 1033]

[Figure 1034]

[Figure 1035]

[Figure 1036]

[Figure 1037]

[Figure 1038]

[Figure 1039]

[Figure 1040]

[Figure 1041]

[Figure 1042]

[Figure 1043]

[Figure 1044]

[Figure 1045]

[Figure 1046]

[Figure 1047]

[Figure 1048]

[Figure 1049]

[Figure 1050]

[Figure 1051]

[Figure 1052]

[Figure 1053]

[Figure 1054]

[Figure 1055]

[Figure 1056]

[Figure 1057]

[Figure 1058]

[Figure 1059]

[Figure 1060]

[Figure 1061]

[Figure 1062]

[Figure 1063]

[Figure 1064]

[Figure 1065]

[Figure 1066]

[Figure 1067]

[Figure 1068]

[Figure 1069]

[Figure 1070]

[Figure 1071]

[Figure 1072]

[Figure 1073]

[Figure 1074]

[Figure 1075]

[Figure 1076]

[Figure 1077]

[Figure 1078]

[Figure 1079]

[Figure 1080]

[Figure 1081]

[Figure 1082]

[Figure 1083]

[Figure 1084]

[Figure 1085]

[Figure 1086]

[Figure 1087]

[Figure 1088]

[Figure 1089]

[Figure 1090]

[Figure 1091]

[Figure 1092]

[Figure 1093]

[Figure 1094]

[Figure 1095]

[Figure 1096]

[Figure 1097]

[Figure 1098]

[Figure 1099]

[Figure 1100]

[Figure 1101]

[Figure 1102]

[Figure 1103]

[Figure 1104]

[Figure 1105]

[Figure 1106]

[Figure 1107]

[Figure 1108]

[Figure 1109]

[Figure 1110]

[Figure 1111]

[Figure 1112]

[Figure 1113]

[Figure 1114]

[Figure 1115]

[Figure 1116]

[Figure 1117]

[Figure 1118]

[Figure 1119]

[Figure 1120]

[Figure 1121]

[Figure 1122]

[Figure 1123]

[Figure 1124]

[Figure 1125]

[Figure 1126]

[Figure 1127]

[Figure 1128]

[Figure 1129]

[Figure 1130]

[Figure 1131]

[Figure 1132]

[Figure 1133]

[Figure 1134]

[Figure 1135]

[Figure 1136]

[Figure 1137]

[Figure 1138]

[Figure 1139]

[Figure 1140]

[Figure 1141]

[Figure 1142]

[Figure 1143]

[Figure 1144]

[Figure 1145]

[Figure 1146]

[Figure 1147]

[Figure 1148]

[Figure 1149]

[Figure 1150]

[Figure 1151]

[Figure 1152]

[Figure 1153]

[Figure 1154]

[Figure 1155]

[Figure 1156]

[Figure 1157]

[Figure 1158]

[Figure 1159]

[Figure 1160]

[Figure 1161]

[Figure 1162]

[Figure 1163]

[Figure 1164]

[Figure 1165]

[Figure 1166]

[Figure 1167]

[Figure 1168]

[Figure 1169]

[Figure 1170]

[Figure 1171]

[Figure 1172]

[Figure 1173]

[Figure 1174]

[Figure 1175]

[Figure 1176]

[Figure 1177]

[Figure 1178]

[Figure 1179]

[Figure 1180]

[Figure 1181]

[Figure 1182]

[Figure 1183]

[Figure 1184]

[Figure 1185]

[Figure 1186]

[Figure 1187]

[Figure 1188]

[Figure 1189]

[Figure 1190]

[Figure 1191]

[Figure 1192]

[Figure 1193]

[Figure 1194]

[Figure 1195]

[Figure 1196]

[Figure 1197]

[Figure 1198]

[Figure 1199]

[Figure 1200]

[Figure 1201]

[Figure 1202]

[Figure 1203]

[Figure 1204]

[Figure 1205]

[Figure 1206]

[Figure 1207]

[Figure 1208]

[Figure 1209]

[Figure 1210]

[Figure 1211]

[Figure 1212]

[Figure 1213]

[Figure 1214]

[Figure 1215]

[Figure 1216]

[Figure 1217]

[Figure 1218]

[Figure 1219]

[Figure 1220]

[Figure 1221]

[Figure 1222]

[Figure 1223]

[Figure 1224]

[Figure 1225]

[Figure 1226]

[Figure 1227]

[Figure 1228]

[Figure 1229]

[Figure 1230]

[Figure 1231]

[Figure 1232]

[Figure 1233]

[Figure 1234]

[Figure 1235]

[Figure 1236]

[Figure 1237]

[Figure 1238]

[Figure 1239]

[Figure 1240]

[Figure 1241]

[Figure 1242]

[Figure 1243]

[Figure 1244]

[Figure 1245]

[Figure 1246]

[Figure 1247]

[Figure 1248]

[Figure 1249]

[Figure 1250]

[Figure 1251]

[Figure 1252]

[Figure 1253]

[Figure 1254]

[Figure 1255]

[Figure 1256]

[Figure 1257]

[Figure 1258]

[Figure 1259]

[Figure 1260]

[Figure 1261]

[Figure 1262]

[Figure 1263]

[Figure 1264]

[Figure 1265]

[Figure 1266]

[Figure 1267]

[Figure 1268]

[Figure 1269]

[Figure 1270]

[Figure 1271]

[Figure 1272]

[Figure 1273]

[Figure 1274]

[Figure 1275]

[Figure 1276]

[Figure 1277]

[Figure 1278]

[Figure 1279]

[Figure 1280]

[Figure 1281]

[Figure 1282]

[Figure 1283]

[Figure 1284]

[Figure 1285]

[Figure 1286]

[Figure 1287]

[Figure 1288]

[Figure 1289]

[Figure 1290]

[Figure 1291]

[Figure 1292]

[Figure 1293]

[Figure 1294]

[Figure 1295]

[Figure 1296]

[Figure 1297]

[Figure 1298]

[Figure 1299]

[Figure 1300]

[Figure 1301]

[Figure 1302]

[Figure 1303]

[Figure 1304]

[Figure 1305]

[Figure 1306]

[Figure 1307]

[Figure 1308]

[Figure 1309]

[Figure 1310]

[Figure 1311]

[Figure 1312]

[Figure 1313]

[Figure 1314]

[Figure 1315]

[Figure 1316]

[Figure 1317]

[Figure 1318]

[Figure 1319]

[Figure 1320]

[Figure 1321]

[Figure 1322]

[Figure 1323]

[Figure 1324]

[Figure 1325]

[Figure 1326]

[Figure 1327]

[Figure 1328]

[Figure 1329]

[Figure 1330]

[Figure 1331]

[Figure 1332]

[Figure 1333]

[Figure 1334]

[Figure 1335]

[Figure 1336]

[Figure 1337]

[Figure 1338]

[Figure 1339]

[Figure 1340]

[Figure 1341]

[Figure 1342]

[Figure 1343]

[Figure 1344]

[Figure 1345]

[Figure 1346]

[Figure 1347]

[Figure 1348]

[Figure 1349]

[Figure 1350]

[Figure 1351]

[Figure 1352]

[Figure 1353]

[Figure 1354]

[Figure 1355]

[Figure 1356]

[Figure 1357]

[Figure 1358]

[Figure 1359]

[Figure 1360]

[Figure 1361]

[Figure 1362]

[Figure 1363]

[Figure 1364]

[Figure 1365]

[Figure 1366]

[Figure 1367]

[Figure 1368]

[Figure 1369]

[Figure 1370]

[Figure 1371]

[Figure 1372]

[Figure 1373]

[Figure 1374]

[Figure 1375]

[Figure 1376]

[Figure 1377]

[Figure 1378]

[Figure 1379]

[Figure 1380]

[Figure 1381]

[Figure 1382]

[Figure 1383]

[Figure 1384]

[Figure 1385]

[Figure 1386]

[Figure 1387]

[Figure 1388]

[Figure 1389]

[Figure 1390]

[Figure 1391]

[Figure 1392]

[Figure 1393]

[Figure 1394]

[Figure 1395]

[Figure 1396]

[Figure 1397]

[Figure 1398]

[Figure 1399]

[Figure 1400]

[Figure 1401]

[Figure 1402]

[Figure 1403]

[Figure 1404]

[Figure 1405]

[Figure 1406]

[Figure 1407]

[Figure 1408]

[Figure 1409]

[Figure 1410]

[Figure 1411]

[Figure 1412]

[Figure 1413]

[Figure 1414]

[Figure 1415]

[Figure 1416]

[Figure 1417]

[Figure 1418]

[Figure 1419]

[Figure 1420]

[Figure 1421]

[Figure 1422]

[Figure 1423]

[Figure 1424]

[Figure 1425]

[Figure 1426]

[Figure 1427]

[Figure 1428]

[Figure 1429]

[Figure 1430]

[Figure 1431]

[Figure 1432]

[Figure 1433]

[Figure 1434]

[Figure 1435]

[Figure 1436]

[Figure 1437]

[Figure 1438]

[Figure 1439]

[Figure 1440]

[Figure 1441]

[Figure 1442]

[Figure 1443]

[Figure 1444]

[Figure 1445]

[Figure 1446]

[Figure 1447]

[Figure 1448]

[Figure 1449]

[Figure 1450]

[Figure 1451]

[Figure 1452]

[Figure 1453]

[Figure 1454]

[Figure 1455]

[Figure 1456]

[Figure 1457]

[Figure 1458]

[Figure 1459]

[Figure 1460]

[Figure 1461]

[Figure 1462]

[Figure 1463]

[Figure 1464]

[Figure 1465]

[Figure 1466]

[Figure 1467]

[Figure 1468]

[Figure 1469]

[Figure 1470]

[Figure 1471]

[Figure 1472]

[Figure 1473]

[Figure 1474]

[Figure 1475]

[Figure 1476]

[Figure 1477]

[Figure 1478]

[Figure 1479]

[Figure 1480]

[Figure 1481]

[Figure 1482]

[Figure 1483]

[Figure 1484]

[Figure 1485]

[Figure 1486]

[Figure 1487]

[Figure 1488]

[Figure 1489]

[Figure 1490]

[Figure 1491]

[Figure 1492]

[Figure 1493]

[Figure 1494]

[Figure 1495]

[Figure 1496]

[Figure 1497]

[Figure 1498]

[Figure 1499]

[Figure 1500]

[Figure 1501]

[Figure 1502]

[Figure 1503]

[Figure 1504]

[Figure 1505]

[Figure 1506]

[Figure 1507]

[Figure 1508]

[Figure 1509]

[Figure 1510]

[Figure 1511]

[Figure 1512]

[Figure 1513]

[Figure 1514]

[Figure 1515]

[Figure 1516]

[Figure 1517]

[Figure 1518]

[Figure 1519]

[Figure 1520]

[Figure 1521]

[Figure 1522]

[Figure 1523]

[Figure 1524]

[Figure 1525]

[Figure 1526]

[Figure 1527]

[Figure 1528]

[Figure 1529]

[Figure 1530]

[Figure 1531]

[Figure 1532]

[Figure 1533]

[Figure 1534]

[Figure 1535]

[Figure 1536]

[Figure 1537]

[Figure 1538]

[Figure 1539]

[Figure 1540]

[Figure 1541]

[Figure 1542]

[Figure 1543]

[Figure 1544]

[Figure 1545]

[Figure 1546]

[Figure 1547]

[Figure 1548]

[Figure 1549]

[Figure 1550]

[Figure 1551]

[Figure 1552]

[Figure 1553]

[Figure 1554]

[Figure 1555]

[Figure 1556]

[Figure 1557]

[Figure 1558]

[Figure 1559]

[Figure 1560]

[Figure 1561]

[Figure 1562]

[Figure 1563]

[Figure 1564]

[Figure 1565]

[Figure 1566]

[Figure 1567]

[Figure 1568]

[Figure 1569]

[Figure 1570]

[Figure 1571]

[Figure 1572]

[Figure 1573]

[Figure 1574]

[Figure 1575]

[Figure 1576]

[Figure 1577]

[Figure 1578]

[Figure 1579]

[Figure 1580]

[Figure 1581]

[Figure 1582]

[Figure 1583]

[Figure 1584]

[Figure 1585]

[Figure 1586]

[Figure 1587]

[Figure 1588]

[Figure 1589]

[Figure 1590]

[Figure 1591]

[Figure 1592]

[Figure 1593]

[Figure 1594]

[Figure 1595]

[Figure 1596]

[Figure 1597]

[Figure 1598]

[Figure 1599]

[Figure 1600]

[Figure 1601]

[Figure 1602]

[Figure 1603]

[Figure 1604]

[Figure 1605]

[Figure 1606]

[Figure 1607]

[Figure 1608]

[Figure 1609]

[Figure 1610]

[Figure 1611]

[Figure 1612]

[Figure 1613]

[Figure 1614]

[Figure 1615]

[Figure 1616]

[Figure 1617]

[Figure 1618]

[Figure 1619]

[Figure 1620]

[Figure 1621]

[Figure 1622]

[Figure 1623]

[Figure 1624]

[Figure 1625]

[Figure 1626]

[Figure 1627]

[Figure 1628]

[Figure 1629]

[Figure 1630]

[Figure 1631]

[Figure 1632]

[Figure 1633]

[Figure 1634]

[Figure 1635]

[Figure 1636]

[Figure 1637]

[Figure 1638]

[Figure 1639]

[Figure 1640]

[Figure 1641]

[Figure 1642]

[Figure 1643]

[Figure 1644]

[Figure 1645]

[Figure 1646]

[Figure 1647]

[Figure 1648]

[Figure 1649]

[Figure 1650]

[Figure 1651]

[Figure 1652]

[Figure 1653]

[Figure 1654]

[Figure 1655]

[Figure 1656]

[Figure 1657]

[Figure 1658]

[Figure 1659]

[Figure 1660]

[Figure 1661]

[Figure 1662]

[Figure 1663]

[Figure 1664]

[Figure 1665]

[Figure 1666]

[Figure 1667]

[Figure 1668]

[Figure 1669]

[Figure 1670]

[Figure 1671]

[Figure 1672]

[Figure 1673]

[Figure 1674]

[Figure 1675]

[Figure 1676]

[Figure 1677]

[Figure 1678]

[Figure 1679]

[Figure 1680]

[Figure 1681]

[Figure 1682]

[Figure 1683]

[Figure 1684]

[Figure 1685]

[Figure 1686]

[Figure 1687]

[Figure 1688]

[Figure 1689]

[Figure 1690]

[Figure 1691]

[Figure 1692]

[Figure 1693]

[Figure 1694]

[Figure 1695]

[Figure 1696]

[Figure 1697]

[Figure 1698]

[Figure 1699]

[Figure 1700]

[Figure 1701]

[Figure 1702]

[Figure 1703]

[Figure 1704]

[Figure 1705]

[Figure 1706]

[Figure 1707]

[Figure 1708]

[Figure 1709]

[Figure 1710]

[Figure 1711]

[Figure 1712]

[Figure 1713]

[Figure 1714]

[Figure 1715]

[Figure 1716]

[Figure 1717]

[Figure 1718]

[Figure 1719]

[Figure 1720]

[Figure 1721]

[Figure 1722]

[Figure 1723]

[Figure 1724]

[Figure 1725]

[Figure 1726]

[Figure 1727]

[Figure 1728]

[Figure 1729]

[Figure 1730]

[Figure 1731]

[Figure 1732]

[Figure 1733]

[Figure 1734]

[Figure 1735]

[Figure 1736]

[Figure 1737]

[Figure 1738]

[Figure 1739]

[Figure 1740]

[Figure 1741]

[Figure 1742]

[Figure 1743]

[Figure 1744]

[Figure 1745]

[Figure 1746]

[Figure 1747]

[Figure 1748]

[Figure 1749]

[Figure 1750]

[Figure 1751]

[Figure 1752]

[Figure 1753]

[Figure 1754]

[Figure 1755]

[Figure 1756]

[Figure 1757]

[Figure 1758]

[Figure 1759]

[Figure 1760]

[Figure 1761]

[Figure 1762]

[Figure 1763]

[Figure 1764]

[Figure 1765]

[Figure 1766]

[Figure 1767]

[Figure 1768]

[Figure 1769]

[Figure 1770]

[Figure 1771]

[Figure 1772]

[Figure 1773]

[Figure 1774]

[Figure 1775]

[Figure 1776]

[Figure 1777]

[Figure 1778]

[Figure 1779]

[Figure 1780]

[Figure 1781]

[Figure 1782]

[Figure 1783]

[Figure 1784]

[Figure 1785]

[Figure 1786]

[Figure 1787]

[Figure 1788]

[Figure 1789]

[Figure 1790]

[Figure 1791]

[Figure 1792]

[Figure 1793]

[Figure 1794]

[Figure 1795]

[Figure 1796]

[Figure 1797]

[Figure 1798]

[Figure 1799]

[Figure 1800]

[Figure 1801]

[Figure 1802]

[Figure 1803]

[Figure 1804]

[Figure 1805]

[Figure 1806]

[Figure 1807]

[Figure 1808]

[Figure 1809]

[Figure 1810]

[Figure 1811]

[Figure 1812]

[Figure 1813]

[Figure 1814]

[Figure 1815]

[Figure 1816]

[Figure 1817]

[Figure 1818]

[Figure 1819]

[Figure 1820]

[Figure 1821]

[Figure 1822]

[Figure 1823]

[Figure 1824]

[Figure 1825]

[Figure 1826]

[Figure 1827]

[Figure 1828]

[Figure 1829]

[Figure 1830]

[Figure 1831]

[Figure 1832]

[Figure 1833]

[Figure 1834]

[Figure 1835]

[Figure 1836]

[Figure 1837]

[Figure 1838]

[Figure 1839]

[Figure 1840]

[Figure 1841]

[Figure 1842]

[Figure 1843]

[Figure 1844]

[Figure 1845]

[Figure 1846]

[Figure 1847]

[Figure 1848]

[Figure 1849]

[Figure 1850]

[Figure 1851]

[Figure 1852]

[Figure 1853]

[Figure 1854]

[Figure 1855]

[Figure 1856]

[Figure 1857]

[Figure 1858]

[Figure 1859]

[Figure 1860]

[Figure 1861]

[Figure 1862]

[Figure 1863]

[Figure 1864]

[Figure 1865]

[Figure 1866]

[Figure 1867]

[Figure 1868]

[Figure 1869]

[Figure 1870]

[Figure 1871]

[Figure 1872]

[Figure 1873]

[Figure 1874]

[Figure 1875]

[Figure 1876]

[Figure 1877]

[Figure 1878]

[Figure 1879]

[Figure 1880]

[Figure 1881]

[Figure 1882]

[Figure 1883]

[Figure 1884]

[Figure 1885]

[Figure 1886]

[Figure 1887]

[Figure 1888]

[Figure 1889]

[Figure 1890]

[Figure 1891]

[Figure 1892]

[Figure 1893]

[Figure 1894]

[Figure 1895]

[Figure 1896]

[Figure 1897]

[Figure 1898]

[Figure 1899]

[Figure 1900]

[Figure 1901]

[Figure 1902]

[Figure 1903]

[Figure 1904]

[Figure 1905]

[Figure 1906]

[Figure 1907]

[Figure 1908]

[Figure 1909]

[Figure 1910]

[Figure 1911]

[Figure 1912]

[Figure 1913]

[Figure 1914]

[Figure 1915]

[Figure 1916]

[Figure 1917]

[Figure 1918]

[Figure 1919]

[Figure 1920]

[Figure 1921]

[Figure 1922]

[Figure 1923]

[Figure 1924]

[Figure 1925]

[Figure 1926]

[Figure 1927]

[Figure 1928]

[Figure 1929]

[Figure 1930]

[Figure 1931]

[Figure 1932]

[Figure 1933]

[Figure 1934]

[Figure 1935]

[Figure 1936]

[Figure 1937]

[Figure 1938]

[Figure 1939]

[Figure 1940]

[Figure 1941]

[Figure 1942]

[Figure 1943]

[Figure 1944]

[Figure 1945]

[Figure 1946]

[Figure 1947]

[Figure 1948]

[Figure 1949]

[Figure 1950]

[Figure 1951]

[Figure 1952]

[Figure 1953]

[Figure 1954]

[Figure 1955]

[Figure 1956]

[Figure 1957]

[Figure 1958]

[Figure 1959]

[Figure 1960]

[Figure 1961]

[Figure 1962]

[Figure 1963]

[Figure 1964]

[Figure 1965]

[Figure 1966]

[Figure 1967]

[Figure 1968]

[Figure 1969]

[Figure 1970]

[Figure 1971]

[Figure 1972]

[Figure 1973]

[Figure 1974]

[Figure 1975]

[Figure 1976]

[Figure 1977]

[Figure 1978]

[Figure 1979]

[Figure 1980]

[Figure 1981]

[Figure 1982]

[Figure 1983]

[Figure 1984]

[Figure 1985]

[Figure 1986]

[Figure 1987]

[Figure 1988]

[Figure 1989]

[Figure 1990]

[Figure 1991]

[Figure 1992]

[Figure 1993]

[Figure 1994]

[Figure 1995]

[Figure 1996]

[Figure 1997]

[Figure 1998]

[Figure 1999]

[Figure 2000]

[Figure 2001]

[Figure 2002]

[Figure 2003]

[Figure 2004]

[Figure 2005]

[Figure 2006]

[Figure 2007]

[Figure 2008]

[Figure 2009]

[Figure 2010]

[Figure 2011]

[Figure 2012]

[Figure 2013]

[Figure 2014]

[Figure 2015]

[Figure 2016]

[Figure 2017]

[Figure 2018]

[Figure 2019]

[Figure 2020]

[Figure 2021]

[Figure 2022]

[Figure 2023]

[Figure 2024]

[Figure 2025]

[Figure 2026]

[Figure 2027]

[Figure 2028]

[Figure 2029]

[Figure 2030]

[Figure 2031]

[Figure 2032]

[Figure 2033]

[Figure 2034]

[Figure 2035]

[Figure 2036]

[Figure 2037]

[Figure 2038]

[Figure 2039]

[Figure 2040]

[Figure 2041]

[Figure 2042]

[Figure 2043]

[Figure 2044]

[Figure 2045]

[Figure 2046]

[Figure 2047]

[Figure 2048]

[Figure 2049]

[Figure 2050]

[Figure 2051]

[Figure 2052]

[Figure 2053]

[Figure 2054]

[Figure 2055]

[Figure 2056]

[Figure 2057]

[Figure 2058]

[Figure 2059]

[Figure 2060]

[Figure 2061]

[Figure 2062]

[Figure 2063]

[Figure 2064]

[Figure 2065]

[Figure 2066]

[Figure 2067]

[Figure 2068]

[Figure 2069]

[Figure 2070]

[Figure 2071]

[Figure 2072]

[Figure 2073]

[Figure 2074]

[Figure 2075]

[Figure 2076]

[Figure 2077]

[Figure 2078]

[Figure 2079]

[Figure 2080]

[Figure 2081]

[Figure 2082]

[Figure 2083]

[Figure 2084]

[Figure 2085]

[Figure 2086]

[Figure 2087]

[Figure 2088]

[Figure 2089]

[Figure 2090]

[Figure 2091]

[Figure 2092]

[Figure 2093]

[Figure 2094]

[Figure 2095]

[Figure 2096]

[Figure 2097]

[Figure 2098]

[Figure 2099]

[Figure 2100]

[Figure 2101]

[Figure 2102]

[Figure 2103]

[Figure 2104]

[Figure 2105]

[Figure 2106]

[Figure 2107]

[Figure 2108]

[Figure 2109]

[Figure 2110]

[Figure 2111]

[Figure 2112]

[Figure 2113]

[Figure 2114]

[Figure 2115]

[Figure 2116]

[Figure 2117]

[Figure 2118]

[Figure 2119]

[Figure 2120]

[Figure 2121]

[Figure 2122]

[Figure 2123]

[Figure 2124]

[Figure 2125]

[Figure 2126]

[Figure 2127]

[Figure 2128]

[Figure 2129]

[Figure 2130]

[Figure 2131]

[Figure 2132]

[Figure 2133]

[Figure 2134]

[Figure 2135]

[Figure 2136]

[Figure 2137]

[Figure 2138]

[Figure 2139]

[Figure 2140]

[Figure 2141]

[Figure 2142]

[Figure 2143]

[Figure 2144]

[Figure 2145]

[Figure 2146]

[Figure 2147]

[Figure 2148]

[Figure 2149]

[Figure 2150]

[Figure 2151]

[Figure 2152]

[Figure 2153]

[Figure 2154]

[Figure 2155]

[Figure 2156]

[Figure 2157]

[Figure 2158]

[Figure 2159]

[Figure 2160]

[Figure 2161]

[Figure 2162]

[Figure 2163]

[Figure 2164]

[Figure 2165]

[Figure 2166]

[Figure 2167]

[Figure 2168]

[Figure 2169]

[Figure 2170]

[Figure 2171]

[Figure 2172]

[Figure 2173]

[Figure 2174]

[Figure 2175]

[Figure 2176]

[Figure 2177]

[Figure 2178]

[Figure 2179]

[Figure 2180]

[Figure 2181]

[Figure 2182]

[Figure 2183]

[Figure 2184]

[Figure 2185]

[Figure 2186]

[Figure 2187]

[Figure 2188]

[Figure 2189]

[Figure 2190]

[Figure 2191]

[Figure 2192]

[Figure 2193]

[Figure 2194]

[Figure 2195]

[Figure 2196]

[Figure 2197]

[Figure 2198]

[Figure 2199]

[Figure 2200]

[Figure 2201]

[Figure 2202]

|[Figure 2203]<br><br>|
|---|

|[Figure 2204]<br><br>|
|---|

|[Figure 2205]<br><br>|
|---|

|[Figure 2206]<br><br>|
|---|

−0.05 0 0.05

−0.05 0 0.05

−0.05 0 0.05

−0.05 0 0.05

- Figure 7: Projection vectors of linear classiﬁers are instructive. In the case RP-features (see text) they correspondto a temporal sequence of scalp topographies.The weights on both hemispheres get the opposite sign (red vs. green) reﬂecting the lateralized nature of the readiness potential and the magnitude of the weights is increasing with time reﬂecting the greater conﬁdence of the potential distribution shortly before keypress.

dataset with only few samples available. Without regularization the estimates of covariance matrices may be inacccurate leading to degraded classiﬁcation results. The choice of linear classiﬁers has the advantage that the learned projection vector of the classiﬁer can be visualized and neurophysiologically validated. In the case of RP-features

- as calculated above the projection vector corresponds to a temporal sequence of scalp topographies, see Fig. 7. See Section 4 for more advanced classiﬁcation techniques and a discussion of how these techniques can help to explain underlying structures of the analyzed data.

##### 2.3 RP-based feedback in asynchronous mode

The general setting is the following. An experimental session starts with a short period during which the subject performs self-paced ﬁnger movements. This session is called calibration session, and the data is used to train a classiﬁer which is then used to make instantaneous predictions on whether the subject intends a hand movement and what its laterality will be.

Although the results of the preceding section demonstrate that an effective discrimination of left vs. right hand ﬁnger movements is possible well before keypress, it remains a challenge to build a system that predicts movement intentions from ongoing EEG. One point that made the previous classiﬁcation task easier was that the single

trials were taken from intervals in ﬁxed time relation to the keypress. For the implementation of a useful continuous feedback in an asynchronous mode (meaning without externally controlled timing) we need two more things: (1) the classiﬁer must work reasonably well not only for one exact time point but for a broader interval of time, and (2) the system needs to detect the build up of movement intentions such that it can trigger BCI commands without externally controlled timing.

With respect to the ﬁrst issue we foundthat a quite simple strategy (jittering)leads to satisfying results: instead of taking only one window as training samples ones extracts several with some time jitter between them. More speciﬁcally we extracted two samples per keypress of the calibration measurement, one from a window ending at 150ms the other at 50ms before keypress. This method makes the resulting classiﬁer somewhat invariant to time shifts of the samples to be classiﬁed, i.e., better suited for the online applicationto sliding windows. Using more than two samples per keypress event did not improve classiﬁcation performance further. Extracting samples from windows ending

- at 50ms before keypress may seem critical since EMG activity starts at about 120ms beforekeypress.But what matters is that the trainedclassiﬁer is able to make predictions before EMG activity starts no matter what signals it was trained on. This can be seen in Fig. 8 in which EEG-, EMG- and EOG-based classiﬁcation is compared in relation to the time point of classiﬁcation. The left plot shows a leave-one-out validation of the calibration measurement, while the right plot shows the accuracy of a classifer trained on the calibration measurement applied to signals of the feedback session, both using jittered training.

To implement the detection of upcoming movements we train a second classiﬁer as outlined in [Blankertz et al., 2002]. Technically, the detector of movement intentions was implemented as a classiﬁer that distinguishes between motor preparation intervals (for left and right taps) and ‘rest’ intervals that were extracted from intervals between movements. To study the interplay of the two classiﬁers we pursued exploratory feedback experiments with one subject, selected for his good ofﬂine results. Fig. 9 shows a statistical evaluation of the two classiﬁers when applied in sliding windows to the continuous EEG.

The movement discriminator in the left plot of Fig. 9 shows a pronounced separation during the movement (preparation and execution) period. In other regions there is a considereable overlap. From this plot it becomes evident that the left/right classiﬁer alone does not distinguish reliably between movement intention and rest condition by the magnitude of its output, which explains the need for a movement detector. The elevation for the left class is a little less pronounced (e.g., the median is −1 at t =0ms compared to 1.25 for right events). The movement intention detector in the right plot of Fig. 9 brings up the movement phase while giving (mainly) negative output to the post movement period.

50

50

5

40

40

5

[bitsperminute]

[bitsperminute]

error[%]

error[%]

10

30

30

10

15

15

20

20

20

20

EEG EMG EOG

EEG EMG EOG

10

10

30

40

30

0

0

−600 −500 −400 −300 −200 −100 0 100

−600 −500 −400 −300 −200 −100 0 100

time point of causal classification [ms]

time point of causal classification [ms]

- Figure 8: Comparison of EEG, EMG and EOG based classiﬁcation with respect to the endpointof the classiﬁcation interval witht = 0ms being the time point of keypress.For the left plot classiﬁers were trained in a leave-one-out fashion and applied to a window sliding over the respective left out trials on data of the calibration measurement. For the right plot a classiﬁer (for each type of signal) was trained on data of the calibration measurement and applied to a window sliding over all trials of a feedback session. Note that the scale of the information transfer rate [bits per minute] on the right is different due to a higher average tapping speed in the feedback session.

These two classiﬁers were used for an exploratory feedback in which a cross was moving in two dimensions, see left plot of Fig. 10. The position on the x-axis was controlled by the left/right movement discriminator and the vertical position was determined by the movement intention detector. Obviously this is not an independent control of two dimensions. Rather the cursor was expected to stay in a middle of the lower half during rest and it should move to the upper left or right ﬁeld when a movement of the left resp. right hand was prepared. The red and green colored ﬁelds are the decision areas which only have a symbolic meaning in this application, because no further actions are triggered. In a case study with one subject the expected behavior was indeed found. Although the full ﬂavor of the feeback can only be experienced by watching it, we tried to demonstrate its dynamics by showing the traces of the ﬁrst 100 trials of the feedback in the right plot of Fig. 10. Each trace displays an interval of the feedback signal -160 to -80ms relative to keypress. The last 40ms are intensiﬁed and the end point of each trace is marked by a dot.

#### 3 BCI Control based on Imagined Movements

The RP feature presented in the previous section allows an early distinction between motor related mental activities since it reﬂects movement intent. But even in repetitive movements the discrimination decays already after about 1 second, cf. [Dornhege, 2006]. Accordingly we take an alternative approach for the design of proportional BCI-

- 0.5

- 1

action

left right

classifieroutput

classifieroutput

0

- 0

- 0.5

- 1

1.5

2

- 2.5

−0.5

−0.5

−1

−1

−1.5

−1.5

−2

−600 −500 −400 −300 −200 −100 0 100 200

−600 −500 −400 −300 −200 −100 0 100 200

time relative to keypress [ms]

time relative to keypress [ms]

- Figure 9: Classiﬁers were trained in a leave-one-out fashion and applied to windows sliding over unseen epochs yielding traces of graded classiﬁer outputs. The tubes show the 10, 20, 30 resp. 90, 80, and 70 percentile values of those traces. On the left the result is shown of the left vs. right classiﬁer with tubes calculated separately for left and right ﬁnger tapping. The subplot on the right shows the result for the movement detection classiﬁer.

| | |
|---|---|
| | |

- Figure 10: Left panel: In a BCI feedback experiment a cursor was controlled by two classiﬁers. The output of a classiﬁer trained to discriminate left vs. right hand ﬁnger movements determined the x-coordinate, while a classiﬁer trained to detect upcoming ﬁnger movements determined the y-coordinate. Accordingly the cursor should stay in the lower center area when the subject is at rest while approaching one of the target ﬁelds upon movement intentions. This behavior was indeed achieved as can be seen in the right panel: Traces of feedback control. Each trace displays an interval of the feedback signal -160 to -80ms relative to keypress. The last 40ms are intensiﬁed and the end point of each trace is marked by a dot. Traces are colored red or green for subsequent left resp. right hand ﬁnger taps.

control, like continuous cursor control. Here we focus on modulations of sensorimotor rhythms evoked by imagined movements. The neurophysiological feature that is exploited here is the event-related desynchronization (ERD): When a subject is at rest (sensori-) motor cortices exhibit a so-called idling rhythm typically with a fundamental frequency at about 12Hz and a harmonic at 24Hz. During motor preparation, imagination or execution this rhythm is attenuated or even total blocked in the area of the cortex that corresponds to the respective limb, an effect termed ERD, cf. [Pfurtscheller and Lopes da Silva, 1999]. The (sensori-) motor area of the left hand is in the center of the right hemisphere, the area of the right hand on the left hemisphere and the area of the foot is in the middle of the vertex.The opposite effect of enhancmentof brain rhythmsis called event-related synchronization and can, e.g., by observed after movement offset.

##### 3.1 Experimental Setup

We designeda setup for a feedbackstudy with 6 subjects who all had no or very little experience with BCI feedback.Brain signals were measured from 118 electrodes mounted on the scalp. To exclude the possibility of inﬂuence from non central nervous system activity, EOG and EMG were recorded additionally, see Section 3.4. Those channels were not used to generate the feedback signal.

Each experiment began with a calibration measurement (also called training session but note that this refers to machine training) in which labeled trials of EEG data during motor imagery were gathered. This data is used by signal processing and machine learning techniques to estimate parameters of a brain-signalto control-signaltranslation algorithm. The learning machine can then be applied online to continuously decode incoming signals for producing an instantaneous feedback control signal.

In the training sessions visual stimuli indicated for 3.5s which of the following 3 motor imageries the subject should perform: (L) left hand, (R) right hand, or (F) right foot. The presentation of target cues was interrupted by periods of random length, 1.75 to 2.25s, in which the subject could relax.

Then the experimenter investigated the data to adjust subject-speciﬁc parameters of the data processing methods and identiﬁed the two classes that gave best discrimination. See Fig. 11 for band-energy mappings of 5 successful subjects and r 2 maps showing that discriminative activity is found over (sensori-) motor cortices only. When the discrimination was satisfactory, a binary classiﬁer was trained and three different kinds of feedback applications followed. This was the case for 5 of 6 subjects who typically performed 8 runs of 25 trials each for each type of feedback applications

During preliminary feedback experiments we realized that the initial classiﬁer was often performingsuboptimal, such that the bias and scaling of the linear classiﬁer had to be adjusted. Later investigations have shown that this adaption is needed to account for

subject 1 subject 3 subject 4 subject 5 subject 6

###### μpowerofrhythm

|left right foot<br><br>|
|---|

2rdifference

- Figure 11: The upper two rows show a topographic display of the energy in the speciﬁc frequency band that was used for feedback (as baseline the energy in the inter-stimuli intervals was subtracted). Darker shades indicate lower energy resp. ERD. From the calibration measurement with three types of motor imagery, two were selected for feedback. Energy plots are shown only of those two selected conditions. The type of motor imagery is indicated by the color of the scalp outline. The lower row shows the r 2 differences between the band energy values of the two classes demonstrating that distictive information found over from (sensori-) motor cortices.

the different experimental condition of the (exciting) feedback situation as compared to the calibration session (see e.g. [Shenoy et al., 2006]).

In the ﬁrst feedback application (‘position controlled cursor’), the output of the classiﬁer was directly translated to a horizontal position of a cursor. Out of two target ﬁelds at both sides, one was highlighted at the beginning of a trial. The cursor started in a deactivated mode (in which it could move but not trigger a target ﬁeld) and became activated after the user has held the cursor in a central position for 500ms. The trial

position controlled cursor rate controlled cursor basket game

###### subject: 6, feedback: 1drfb, session: 5 subject: 6, feedback: basketfb, session: 9

subject: 3, feedback: 1dfb, session: 4

−1 −0.8 −0.6 −0.4 −0.2 0 0.2 0.4 0.6 0.8 1 0

−1 −0.8 −0.6 −0.4 −0.2 0 0.2 0.4 0.6 0.8 1 0

1000

500

2000

3000

1000

4000

1500

5000

6000

2000

7000

subject: 1, feedback: 1drfb, session: 6 subject: 5, feedback: basketfb, session: 2

subject: 4, feedback: 1dfb, session: 6

−1 −0.8 −0.6 −0.4 −0.2 0 0.2 0.4 0.6 0.8 1 0

−1 −0.8 −0.6 −0.4 −0.2 0 0.2 0.4 0.6 0.8 1 0

500 1000 1500 2000 2500 3000 3500 4000 4500 5000

500

1000

1500

2000

2500

- Figure 12: This plots shows the single trial feedback traces from two runs for each type of feedback with time on the vertical axis and BCI control on the horizontal axis. Data sets were chosen from all 5 subjects. For the cursor control, green and blue code correct trials with left resp. right target while erroneous trials are shown in red. For the basket game feedback erroneous trials are coded by dotted lines. The upper row shows examples of very good performance, while performance in the lower row was a bit degraded.

ended when the activated cursor touched a target ﬁeld which was then colored green or red, depending on whether it was the correct target or not. The cursor was deactivated and the next target appeared.

The second feedback application (‘rate controlled cursor’) was very similar, but the control of the cursor was relative to the actual position, i.e., at each update step a fraction of the classiﬁer output was added to the actual cursor position. Each trial started by setting the cursor to the middle of the screen and releasing it after 750ms.

The last feedback application (‘basket game’) operated in a synchronous mode and is similar to what is used in Graz, cf. [Krausz et al., 2003]. A ball fell at constant speed while its horizontal position was controlled by the classiﬁer output. At the bottom of the screen there were three target ﬁelds, the outer having half the width of the middle ﬁelds to account for the fact that outer positions were easier to hit.

Fig. 12 shows the trajetories of the selected feedback runs for each of the three types of feedback. The upper row shows examples of very good performance, while performance in the lower row was a bit degraded.

##### 3.2 Processing and Classiﬁcation

A crucial point in the data processing is to extract appropriate spatial ﬁlters that optimize the discriminability of multi-channel brain signals based on ERD/ERS effects of the (sensori-) motor rhythms. Once these ﬁlters have been determined, features are extracted as the log of the variance in those surrogate channels. In our experience those features can best be classiﬁed by linear methods; we use linear discriminant analysis (LDA). For online operation, features are calculated every 40ms from sliding windows of 250 to 1000ms (subject-speciﬁc). The spatial ﬁlters are calculated individually for each subject on the data of the calibration measurement by Common Spatial Pattern (CSP) analysis, see [Fukunaga, 1990,Lemm et al., 2005,Dornhege et al., 2006d]. The objective of the CSP technique is to ﬁnd spatial ﬁlters that the maximize variance of signals of one condition and at the same time minimize variance of singals of another condition. Since variance of band-pass ﬁltered signals is equal to band-power, CSP ﬁlters can be used to discriminate conditions that a characterized by ERD/ERS effects.

Technically CSP analysis goes as follows. Let Σ1 and Σ2 be estimates of the covariance matrices of the band-pass ﬁltered EEG signals under the two conditions. These two matrices are simultaneously diagonalized in a way that the eigenvalues of Σ1 and Σ2 sum to 1. Practically this can be done by caluclating the generalized eigenvectorsV:

Σ1V = (Σ1 +Σ2)VD. (1)

Then the diagonal matrix D contains the eigenvalues ofΣ1 and the column vectors ofV are the ﬁlters of the common spatial patterns. Best contrast is provided by ﬁlters with

high eigenvalues (large variance for condition 1 and small variance for condition 2) and by ﬁlters with low eigenvalues (vice versa).

Further details about the processing methods and the selection of parameters can be found in [Blankertz et al., 2005].

##### 3.3 Results

To compare the results of different feedback sessions we use the information transfer rate (ITR, [Wolpaw et al., 2002]) measured in bits per minute (bpm). We calculated this measure for each run according to the following formula:

# of decisions duration in minutes · plog2(p)+(1− p)log(

1− p N −1

ITR =

)+log2(N) (2)

[Figure 2207]

[Figure 2208]

where p is the accuracy in decisions between N classes (N = 2 for cursor control and N = 3 for the basket game). Note that the duration in minutes refers to the total duration of the run including all inter-trial intervals. In contrast to error rates or ROC curves the ITR takes different duration of trials and different number of classes into account. The

Table 1: The ﬁrst two columns compare the accuracy as calculated by cross-validation on the calibration data with the accuracy obtained online in the feedback application ‘rate controlled cursor’. Columns three to eight report the information transfer rates (ITR) measured in bits per minute as obtained by Shannon’s formula, cf. (2). For each feedback application the ﬁrst column reports the average ITR of all runs (of 25 trials each), while the second column reports the peak ITR of all runs. Subject 2 did not achieve BCI control (64.6% accuracy in the calibration data).

[Figure 2209]

acc [%] cursor pos. ctrl cursor rate ctrl basket cal. fb. overall peak overall peak overall peak

[Figure 2210]

1 95.4 80.5 7.1 15.1 5.9 11.0 2.6 5.5

- 3 98.0 98.0 12.7 20.3 24.4 35.4 9.6 16.1
- 4 78.2 88.5 8.9 15.5 17.4 37.1 6.6 9.7
- 5 78.1 90.5 7.9 13.1 9.0 24.5 6.0 8.8
- 6 97.6 95.0 13.4 21.1 22.6 31.5 16.4 35.0 ∅ 89.5 90.5 10.0 17.0 15.9 27.9 8.2 15.0

[Figure 2211]

[Figure 2212]

ITR of a random classiﬁer is 0. Table 1 summarizes the information transfer rates that were obtained by the 5 subjects in the three feedback sessions. Highest ITRs were obtained in the ‘rate controlled cursor’ scenario which has a asynchronous protocol.

One point that is to our knowledge special about the BBCI is that it can be operated at a high decision speed, not only theoretically, but also in practice. In the absolute cursor control the average trial length was 3 seconds, in rate controlled cursor 2.5 seconds. In the basket feedback the trial length is constant (synchronous protocol) but was individually selected for each subject, ranging from 2.1 to 3s. The fastest subject was no. 4 which performed at an average speed of one decision every 1.7s. The most reliable performance was achieved by subject 3: only 2% of the total 200 trials in the rate controlled cursor were misclassiﬁed at an average speed of one decision per 2.1s. Note that in our notion a trial is ranging from one target presentation to the next including the ‘non-control’ period during which the selected ﬁeld was highlighted.

In a later experiment subject 3 operated a mental typewriter based the second feedback application. The alphabet (including a space and a deletion symbol) was split into two parts and those groups of characters were placed on the left resp. right side of the screen. The user selects one subgroup by moving the cursor to the respective side and the process is iterated until a ‘group’of one character is selected. The splitting was done alphabetically based on the probabilities of the German alphabet, but no elaborated lan-

guage model was used. In a free spelling mode subject 3 spelled 3 german sentences with a total of 135 characters in 30 minutes, which is a typing speed of 4.5 letters per minutes. Note that all erros have been corrected by using the deletion symbol. For details, see [Dornhege, 2006]. Note that with a novel mental typewriter that is based on principles of human-computer interaction the same subject achieved a typing speed of more than 7 letters per minute, cf. [Müller and Blankertz, 2006].

##### 3.4 Investigating the Dependency of BCI Control

The fact that it is in principle possible to voluntarily modulate motorsensory rhythms without concurrent EMG activity was studied in [Vaughan et al., 1998]. Nevertheless it has to be checked for every BCI experiment involving healthy subjects. For this reason we always record EMG signals even though they are not used in the online system. On one hand we investigated classwise averaged spectra, their statistical signiﬁcant differences and the scalp distributions and time courses of the power of the μand β rhythm. The results substantiated that differences of the motor imagery classes indeed were located in sensorimotor cortices and had the typical time courses (except for subject 2 in whom no consistent differences were found), cf. Fig. 11. On the other hand we compared how much variance of the classiﬁer output and how much variance of the EMG signals can be explained by the target class. Much in the spirit of [Vaughan et al., 1998] we made the following analysis using the squared bi-serial correlation coefﬁcient r 2. The r2-value was calculated for the classiﬁer output and for the band-pass ﬁltered and rectiﬁed EMG signals of the feedback sessions. Then the maximum of those time series was determined resulting in one r2-value per subject and feedback session for EMG resp. for the BCI classiﬁer signal. The r2 for EMG was in the range 0.01 to 0.08 (mean 0.04±0.03) which is very low compared to the r2 for the BCI classiﬁer signal which was in the range 0.36 to 0.79 (mean 0.52±0.15).

The fact that the BBCI works without being dependent on eye movements or visual input was additionally veriﬁed by letting two subjects control the BBCI with closed eyes which resulted in a comparable performance as in the closed loop feedback.

#### 4 Explaining Underlying Structures by Machine Learning Techniques

When analyzing high dimensional data it is not only important to visualize, predict or classify with low error, but it is essential that exploratory data analysis tools allow to explain the underlying structure in order to contribute to a better understanding of data.

The ability to generate excellent and interpretable results is a long standing problem for general nonlinear methods. Decision trees such as CART [Breiman et al., 1984] or MARS [Friedman, 1991] or more recent tree-algorithms offer a ﬁrst reasonable compromise. Here the classiﬁcation can be translated into a set of rules, which, however,

due to their large number, might still not be overly illuminating. Using vanilla neural network approaches (e.g. [Bishop, 1995]), the hidden units nonlinearly combine the measured data and thus interpretation also becomes hard in terms of input variables. Methods like input pruning can alleviate this problem to some extent since such pruning algorithms give rise to solutions which are sparse in the number of input variables ( [Bishop, 1995]).

In contrast, linear methods reveal explanatory power. (See e.g. [Müller et al., 2003] for a discussion of linear vs. nonlinear classiﬁcation.) In the linear separating hyperplane formulation (w x+b= 0), the estimated label {1, −1} of an input vector x ∈ N is yˆ= sign(w x+b). If no a-priori knowledge on the probability distribution of the data is available, a typical objective is to minimize a combination of the empirical risk function and a regularization term that restrains the algorithm from overﬁtting to the training set {(xk,yk)|k = 1,...,K}. Taking a soft margin loss function yields the empirical risk function ∑Kk=1max(0,1−yk(w xk +b)). In most approaches of this type there is a hyper-parameter that determines the trade-off between risk and regularization, which has to be chosen by model selection on the training set, e.g. similar to [Rätsch et al., 2001,Müller et al., 2001]. When classifying with a linear hyperplane classiﬁer w we can easily rank and thus quantify the contribution of every dimension x i to the classiﬁer’s decision for a given data point x. For instance, the more positive the contribution to the scalar product w x for a certain dimension i, the higher its relative contribution to the overall decision to label the point x as positive.

Nonlinear kernel-based methods (e.g. [Vapnik, 1995,Müller et al., 2001,Schölkopf et al., 1998,Rosipal and Trejo, 2001]) could in principle assess such individual contributions in some appropriate high dimensional feature space F, but when projecting back to the original input space, single feature space dimensions typically correspond to an uninterpretable nonlinear mix of input variables ( [Schölkopf et al., 1999]), most similar to the above discussed neural network scenario.

Thus, an ideal strategy should simultaneously construct a good classiﬁer and select features for explaining. This integrative approach is in contrast to common sequential methods that ﬁrst use dimensionality reduction such as PCA and later on build a classiﬁer on the reduced space. Recently, mathematical programming machines especially linear programs (rsp. sparse regularized ﬁsher’s discriminant, [Mika et al., 2001,Mika et al., 2000]) have become popular since they can exactly fulﬁll this integrative task, see e.g. [Blankertz et al., 2002] for a ﬁrst application of this technique in the context of BCI data analysis.

Let us introduce some mathematical programming machines that are based on the above linear classiﬁer (w,b). The mathematical programming formulation of Regular-

ized Fisher Discriminant (RFD) is [Mika et al., 2001]: min

1/2||w||22 + C/K||ξ||22 subject to (3) yk(w xk +b) = 1−ξk and ξk 0, for k = 1,...,K (4)

w,b,ξ

where ||·||2 denotes the 2-norm (||w||22 = w w) and C is a model parameter. The constraint yk(w xk + b) = 1−ξk ensures that the class means are projected to the corresponding class labels, i.e., 1 and −1. Minimizing the length of w maximizes the margin between the projected class means relative to the intra class variance. A reformulation of eqs. (4) and (4) allows to consider some interesting variants, e.g., Sparse Fisher Discriminant (SFD), which uses the 1-norm (||w||1 = Σ|wn|) on the regularizer, i.e., the goal function is ||w||1 +C/K||ξ||22. This choice favours solutions with sparse vectors w, such that it automatically also yields integrated feature selection in input space while providing excellent classiﬁcation. Our implementation of SFD uses the cplex optimizer [ILOG, 1999].

A further mathematical programming technique are Linear programming machines (LPMs) that are well known for their sparseness [Bennett and Mangasarian, 1992,Vapnik, 1995,Müller et al., 2001]

1/2||w||1 + C/K||ξ||1 subject to yk(w xk +b) 1−ξk, and ξk 0 for k = 1,...,K.

min

w,b,ξ

Note that an interesting class of sparse mathematical programmingmachines are implemented by minimizing partial least squares problems; also here sparsity and accuracy can be provided in an integrative manner (e.g. [Rosipal and Trejo, 2001]).

When applied to one of our EEG measurements from an imagined movementexperiment as presented in Section 3.1, the LPM selects less than 4% of the feature dimensions that allow for a left vs. right classiﬁcation with good generalization. The outcome of the algorithm coincides nicely with what we would expect from neurophysiology, i.e., high loadings for electrodes close to sensorimotor cortices in the left and right hemisphere with a strong focus at 12Hz, i.e., the frequency range of the μ-rhythm, cf. Fig. 13. Note that the feature selection is an integrative part of the learning process and is automatically adapted to subject, electrode placement, etc.

Thus, the use of state-of-the-art learning machines enables us not only to achieve high decision accuracies for BCI (e.g. [Blankertz et al., 2002,Blankertz et al., 2003, Dornhege et al., 2004]), but also, as a by-product of the classiﬁcation, the few most prominent features that are found match nicely with neurophysiological intuition: the most salient information can be gained in the frequency range of sensorimotor rhythms with a focus over motor cortices, cf. Fig. 13. For the aboveparadigmit was clear what to

Fp

|[Figure 2213]|
|---|

F

FC

C

CP

P

PO O

- 5 10 15 20 25 30

|[Figure 2214]|
|---|

|[Figure 2215]|
|---|

|[Figure 2216]<br><br>|
|---|

15

[Figure 2217]

[Figure 2218]

[Figure 2219]

[Figure 2220]

[Figure 2221]

[Figure 2222]

[Figure 2223]

[Figure 2224]

[Figure 2225]

[Figure 2226]

[Figure 2227]

[Figure 2228]

[Figure 2229]

[Figure 2230]

[Figure 2231]

[Figure 2232]

[Figure 2233]

[Figure 2234]

[Figure 2235]

[Figure 2236]

[Figure 2237]

[Figure 2238]

[Figure 2239]

[Figure 2240]

[Figure 2241]

[Figure 2242]

[Figure 2243]

[Figure 2244]

[Figure 2245]

[Figure 2246]

[Figure 2247]

[Figure 2248]

[Figure 2249]

[Figure 2250]

[Figure 2251]

[Figure 2252]

[Figure 2253]

[Figure 2254]

[Figure 2255]

[Figure 2256]

[Figure 2257]

[Figure 2258]

[Figure 2259]

[Figure 2260]

[Figure 2261]

[Figure 2262]

[Figure 2263]

[Figure 2264]

[Figure 2265]

[Figure 2266]

[Figure 2267]

[Figure 2268]

[Figure 2269]

[Figure 2270]

[Figure 2271]

[Figure 2272]

[Figure 2273]

[Figure 2274]

[Figure 2275]

[Figure 2276]

[Figure 2277]

[Figure 2278]

[Figure 2279]

[Figure 2280]

[Figure 2281]

[Figure 2282]

[Figure 2283]

[Figure 2284]

[Figure 2285]

[Figure 2286]

[Figure 2287]

[Figure 2288]

[Figure 2289]

[Figure 2290]

[Figure 2291]

[Figure 2292]

[Figure 2293]

[Figure 2294]

[Figure 2295]

[Figure 2296]

[Figure 2297]

[Figure 2298]

[Figure 2299]

[Figure 2300]

[Figure 2301]

[Figure 2302]

[Figure 2303]

[Figure 2304]

[Figure 2305]

[Figure 2306]

[Figure 2307]

[Figure 2308]

[Figure 2309]

[Figure 2310]

[Figure 2311]

[Figure 2312]

[Figure 2313]

[Figure 2314]

[Figure 2315]

[Figure 2316]

[Figure 2317]

[Figure 2318]

[Figure 2319]

[Figure 2320]

[Figure 2321]

[Figure 2322]

[Figure 2323]

[Figure 2324]

[Figure 2325]

[Figure 2326]

[Figure 2327]

[Figure 2328]

[Figure 2329]

[Figure 2330]

[Figure 2331]

[Figure 2332]

[Figure 2333]

[Figure 2334]

[Figure 2335]

[Figure 2336]

[Figure 2337]

[Figure 2338]

[Figure 2339]

[Figure 2340]

[Figure 2341]

[Figure 2342]

[Figure 2343]

[Figure 2344]

[Figure 2345]

[Figure 2346]

[Figure 2347]

[Figure 2348]

[Figure 2349]

[Figure 2350]

[Figure 2351]

[Figure 2352]

[Figure 2353]

[Figure 2354]

[Figure 2355]

[Figure 2356]

[Figure 2357]

[Figure 2358]

[Figure 2359]

[Figure 2360]

[Figure 2361]

[Figure 2362]

[Figure 2363]

[Figure 2364]

[Figure 2365]

[Figure 2366]

[Figure 2367]

[Figure 2368]

[Figure 2369]

[Figure 2370]

[Figure 2371]

[Figure 2372]

[Figure 2373]

[Figure 2374]

[Figure 2375]

[Figure 2376]

[Figure 2377]

[Figure 2378]

[Figure 2379]

[Figure 2380]

[Figure 2381]

[Figure 2382]

[Figure 2383]

[Figure 2384]

[Figure 2385]

[Figure 2386]

[Figure 2387]

[Figure 2388]

[Figure 2389]

[Figure 2390]

[Figure 2391]

[Figure 2392]

[Figure 2393]

[Figure 2394]

[Figure 2395]

[Figure 2396]

[Figure 2397]

[Figure 2398]

[Figure 2399]

[Figure 2400]

[Figure 2401]

[Figure 2402]

[Figure 2403]

[Figure 2404]

[Figure 2405]

[Figure 2406]

[Figure 2407]

[Figure 2408]

[Figure 2409]

[Figure 2410]

[Figure 2411]

[Figure 2412]

[Figure 2413]

[Figure 2414]

[Figure 2415]

[Figure 2416]

[Figure 2417]

[Figure 2418]

[Figure 2419]

[Figure 2420]

[Figure 2421]

[Figure 2422]

[Figure 2423]

[Figure 2424]

[Figure 2425]

[Figure 2426]

[Figure 2427]

[Figure 2428]

[Figure 2429]

[Figure 2430]

[Figure 2431]

[Figure 2432]

[Figure 2433]

[Figure 2434]

[Figure 2435]

[Figure 2436]

[Figure 2437]

[Figure 2438]

[Figure 2439]

[Figure 2440]

[Figure 2441]

[Figure 2442]

[Figure 2443]

[Figure 2444]

[Figure 2445]

[Figure 2446]

[Figure 2447]

[Figure 2448]

[Figure 2449]

[Figure 2450]

[Figure 2451]

[Figure 2452]

[Figure 2453]

[Figure 2454]

[Figure 2455]

[Figure 2456]

[Figure 2457]

[Figure 2458]

[Figure 2459]

[Figure 2460]

[Figure 2461]

[Figure 2462]

[Figure 2463]

[Figure 2464]

[Figure 2465]

[Figure 2466]

[Figure 2467]

[Figure 2468]

[Figure 2469]

[Figure 2470]

[Figure 2471]

[Figure 2472]

[Figure 2473]

[Figure 2474]

[Figure 2475]

[Figure 2476]

[Figure 2477]

[Figure 2478]

[Figure 2479]

[Figure 2480]

[Figure 2481]

[Figure 2482]

[Figure 2483]

[Figure 2484]

[Figure 2485]

[Figure 2486]

[Figure 2487]

[Figure 2488]

[Figure 2489]

[Figure 2490]

[Figure 2491]

[Figure 2492]

[Figure 2493]

[Figure 2494]

[Figure 2495]

[Figure 2496]

[Figure 2497]

[Figure 2498]

[Figure 2499]

[Figure 2500]

[Figure 2501]

[Figure 2502]

[Figure 2503]

[Figure 2504]

[Figure 2505]

[Figure 2506]

[Figure 2507]

[Figure 2508]

[Figure 2509]

[Figure 2510]

[Figure 2511]

[Figure 2512]

[Figure 2513]

[Figure 2514]

[Figure 2515]

[Figure 2516]

[Figure 2517]

[Figure 2518]

[Figure 2519]

[Figure 2520]

[Figure 2521]

[Figure 2522]

[Figure 2523]

[Figure 2524]

[Figure 2525]

[Figure 2526]

[Figure 2527]

[Figure 2528]

[Figure 2529]

[Figure 2530]

[Figure 2531]

[Figure 2532]

[Figure 2533]

[Figure 2534]

[Figure 2535]

[Figure 2536]

[Figure 2537]

[Figure 2538]

[Figure 2539]

[Figure 2540]

[Figure 2541]

[Figure 2542]

[Figure 2543]

[Figure 2544]

[Figure 2545]

[Figure 2546]

[Figure 2547]

[Figure 2548]

[Figure 2549]

[Figure 2550]

[Figure 2551]

[Figure 2552]

[Figure 2553]

[Figure 2554]

[Figure 2555]

[Figure 2556]

[Figure 2557]

[Figure 2558]

[Figure 2559]

[Figure 2560]

[Figure 2561]

[Figure 2562]

[Figure 2563]

[Figure 2564]

[Figure 2565]

[Figure 2566]

[Figure 2567]

[Figure 2568]

[Figure 2569]

[Figure 2570]

[Figure 2571]

[Figure 2572]

[Figure 2573]

[Figure 2574]

[Figure 2575]

[Figure 2576]

[Figure 2577]

[Figure 2578]

[Figure 2579]

[Figure 2580]

[Figure 2581]

[Figure 2582]

[Figure 2583]

[Figure 2584]

[Figure 2585]

[Figure 2586]

[Figure 2587]

[Figure 2588]

[Figure 2589]

[Figure 2590]

[Figure 2591]

[Figure 2592]

[Figure 2593]

[Figure 2594]

[Figure 2595]

[Figure 2596]

[Figure 2597]

[Figure 2598]

[Figure 2599]

[Figure 2600]

[Figure 2601]

[Figure 2602]

[Figure 2603]

[Figure 2604]

[Figure 2605]

[Figure 2606]

[Figure 2607]

[Figure 2608]

[Figure 2609]

[Figure 2610]

[Figure 2611]

[Figure 2612]

[Figure 2613]

[Figure 2614]

[Figure 2615]

[Figure 2616]

[Figure 2617]

[Figure 2618]

[Figure 2619]

[Figure 2620]

[Figure 2621]

[Figure 2622]

[Figure 2623]

[Figure 2624]

[Figure 2625]

[Figure 2626]

[Figure 2627]

[Figure 2628]

[Figure 2629]

[Figure 2630]

[Figure 2631]

[Figure 2632]

[Figure 2633]

[Figure 2634]

[Figure 2635]

[Figure 2636]

[Figure 2637]

[Figure 2638]

[Figure 2639]

[Figure 2640]

[Figure 2641]

[Figure 2642]

[Figure 2643]

[Figure 2644]

[Figure 2645]

[Figure 2646]

[Figure 2647]

[Figure 2648]

[Figure 2649]

[Figure 2650]

[Figure 2651]

[Figure 2652]

[Figure 2653]

[Figure 2654]

[Figure 2655]

[Figure 2656]

[Figure 2657]

[Figure 2658]

[Figure 2659]

[Figure 2660]

[Figure 2661]

[Figure 2662]

[Figure 2663]

[Figure 2664]

[Figure 2665]

[Figure 2666]

[Figure 2667]

[Figure 2668]

[Figure 2669]

[Figure 2670]

[Figure 2671]

[Figure 2672]

[Figure 2673]

[Figure 2674]

[Figure 2675]

[Figure 2676]

[Figure 2677]

[Figure 2678]

[Figure 2679]

[Figure 2680]

[Figure 2681]

[Figure 2682]

[Figure 2683]

[Figure 2684]

[Figure 2685]

[Figure 2686]

[Figure 2687]

[Figure 2688]

[Figure 2689]

[Figure 2690]

[Figure 2691]

[Figure 2692]

[Figure 2693]

[Figure 2694]

[Figure 2695]

[Figure 2696]

[Figure 2697]

[Figure 2698]

[Figure 2699]

[Figure 2700]

[Figure 2701]

[Figure 2702]

[Figure 2703]

[Figure 2704]

[Figure 2705]

[Figure 2706]

[Figure 2707]

[Figure 2708]

[Figure 2709]

[Figure 2710]

[Figure 2711]

[Figure 2712]

[Figure 2713]

[Figure 2714]

[Figure 2715]

[Figure 2716]

[Figure 2717]

[Figure 2718]

[Figure 2719]

[Figure 2720]

[Figure 2721]

[Figure 2722]

[Figure 2723]

[Figure 2724]

[Figure 2725]

[Figure 2726]

[Figure 2727]

[Figure 2728]

[Figure 2729]

[Figure 2730]

[Figure 2731]

[Figure 2732]

[Figure 2733]

[Figure 2734]

[Figure 2735]

[Figure 2736]

[Figure 2737]

[Figure 2738]

[Figure 2739]

[Figure 2740]

[Figure 2741]

[Figure 2742]

[Figure 2743]

[Figure 2744]

[Figure 2745]

[Figure 2746]

[Figure 2747]

[Figure 2748]

[Figure 2749]

[Figure 2750]

[Figure 2751]

[Figure 2752]

[Figure 2753]

[Figure 2754]

[Figure 2755]

[Figure 2756]

[Figure 2757]

[Figure 2758]

[Figure 2759]

[Figure 2760]

[Figure 2761]

[Figure 2762]

[Figure 2763]

[Figure 2764]

[Figure 2765]

[Figure 2766]

[Figure 2767]

[Figure 2768]

[Figure 2769]

[Figure 2770]

[Figure 2771]

[Figure 2772]

[Figure 2773]

[Figure 2774]

[Figure 2775]

[Figure 2776]

[Figure 2777]

[Figure 2778]

[Figure 2779]

[Figure 2780]

[Figure 2781]

[Figure 2782]

[Figure 2783]

[Figure 2784]

[Figure 2785]

[Figure 2786]

[Figure 2787]

[Figure 2788]

[Figure 2789]

[Figure 2790]

[Figure 2791]

[Figure 2792]

[Figure 2793]

[Figure 2794]

[Figure 2795]

[Figure 2796]

[Figure 2797]

[Figure 2798]

[Figure 2799]

[Figure 2800]

[Figure 2801]

[Figure 2802]

[Figure 2803]

[Figure 2804]

[Figure 2805]

[Figure 2806]

[Figure 2807]

[Figure 2808]

[Figure 2809]

[Figure 2810]

[Figure 2811]

[Figure 2812]

[Figure 2813]

[Figure 2814]

[Figure 2815]

[Figure 2816]

[Figure 2817]

[Figure 2818]

[Figure 2819]

[Figure 2820]

[Figure 2821]

[Figure 2822]

[Figure 2823]

[Figure 2824]

[Figure 2825]

[Figure 2826]

[Figure 2827]

[Figure 2828]

[Figure 2829]

[Figure 2830]

[Figure 2831]

[Figure 2832]

[Figure 2833]

[Figure 2834]

[Figure 2835]

[Figure 2836]

[Figure 2837]

[Figure 2838]

[Figure 2839]

[Figure 2840]

[Figure 2841]

[Figure 2842]

[Figure 2843]

[Figure 2844]

[Figure 2845]

[Figure 2846]

[Figure 2847]

[Figure 2848]

[Figure 2849]

[Figure 2850]

[Figure 2851]

[Figure 2852]

[Figure 2853]

[Figure 2854]

[Figure 2855]

[Figure 2856]

[Figure 2857]

[Figure 2858]

[Figure 2859]

[Figure 2860]

[Figure 2861]

[Figure 2862]

[Figure 2863]

[Figure 2864]

[Figure 2865]

[Figure 2866]

[Figure 2867]

[Figure 2868]

[Figure 2869]

[Figure 2870]

[Figure 2871]

[Figure 2872]

[Figure 2873]

[Figure 2874]

[Figure 2875]

[Figure 2876]

[Figure 2877]

[Figure 2878]

[Figure 2879]

[Figure 2880]

[Figure 2881]

[Figure 2882]

[Figure 2883]

[Figure 2884]

[Figure 2885]

[Figure 2886]

[Figure 2887]

[Figure 2888]

[Figure 2889]

[Figure 2890]

[Figure 2891]

[Figure 2892]

[Figure 2893]

[Figure 2894]

[Figure 2895]

10

[Figure 2896]

[Figure 2897]

[Figure 2898]

[Figure 2899]

[Figure 2900]

[Figure 2901]

[Figure 2902]

[Figure 2903]

[Figure 2904]

[Figure 2905]

[Figure 2906]

[Figure 2907]

[Figure 2908]

[Figure 2909]

[Figure 2910]

[Figure 2911]

[Figure 2912]

[Figure 2913]

[Figure 2914]

[Figure 2915]

[Figure 2916]

[Figure 2917]

[Figure 2918]

[Figure 2919]

[Figure 2920]

[Figure 2921]

[Figure 2922]

[Figure 2923]

[Figure 2924]

[Figure 2925]

[Figure 2926]

[Figure 2927]

[Figure 2928]

[Figure 2929]

[Figure 2930]

[Figure 2931]

[Figure 2932]

[Figure 2933]

[Figure 2934]

[Figure 2935]

[Figure 2936]

[Figure 2937]

[Figure 2938]

[Figure 2939]

[Figure 2940]

[Figure 2941]

[Figure 2942]

[Figure 2943]

[Figure 2944]

[Figure 2945]

[Figure 2946]

[Figure 2947]

[Figure 2948]

[Figure 2949]

[Figure 2950]

[Figure 2951]

[Figure 2952]

[Figure 2953]

[Figure 2954]

[Figure 2955]

[Figure 2956]

[Figure 2957]

[Figure 2958]

[Figure 2959]

[Figure 2960]

[Figure 2961]

[Figure 2962]

[Figure 2963]

[Figure 2964]

[Figure 2965]

[Figure 2966]

[Figure 2967]

[Figure 2968]

[Figure 2969]

[Figure 2970]

[Figure 2971]

[Figure 2972]

[Figure 2973]

[Figure 2974]

[Figure 2975]

[Figure 2976]

[Figure 2977]

[Figure 2978]

[Figure 2979]

[Figure 2980]

[Figure 2981]

[Figure 2982]

[Figure 2983]

[Figure 2984]

[Figure 2985]

[Figure 2986]

[Figure 2987]

[Figure 2988]

[Figure 2989]

[Figure 2990]

[Figure 2991]

[Figure 2992]

[Figure 2993]

[Figure 2994]

[Figure 2995]

[Figure 2996]

[Figure 2997]

[Figure 2998]

[Figure 2999]

[Figure 3000]

[Figure 3001]

[Figure 3002]

[Figure 3003]

[Figure 3004]

[Figure 3005]

[Figure 3006]

[Figure 3007]

[Figure 3008]

[Figure 3009]

[Figure 3010]

[Figure 3011]

[Figure 3012]

[Figure 3013]

[Figure 3014]

[Figure 3015]

[Figure 3016]

[Figure 3017]

[Figure 3018]

[Figure 3019]

[Figure 3020]

[Figure 3021]

[Figure 3022]

[Figure 3023]

[Figure 3024]

[Figure 3025]

[Figure 3026]

[Figure 3027]

[Figure 3028]

[Figure 3029]

[Figure 3030]

[Figure 3031]

[Figure 3032]

[Figure 3033]

[Figure 3034]

[Figure 3035]

[Figure 3036]

[Figure 3037]

[Figure 3038]

[Figure 3039]

[Figure 3040]

[Figure 3041]

[Figure 3042]

[Figure 3043]

[Figure 3044]

[Figure 3045]

[Figure 3046]

[Figure 3047]

[Figure 3048]

[Figure 3049]

[Figure 3050]

[Figure 3051]

[Figure 3052]

[Figure 3053]

[Figure 3054]

[Figure 3055]

[Figure 3056]

[Figure 3057]

[Figure 3058]

[Figure 3059]

[Figure 3060]

[Figure 3061]

[Figure 3062]

[Figure 3063]

[Figure 3064]

[Figure 3065]

[Figure 3066]

[Figure 3067]

[Figure 3068]

[Figure 3069]

[Figure 3070]

[Figure 3071]

[Figure 3072]

[Figure 3073]

[Figure 3074]

[Figure 3075]

[Figure 3076]

[Figure 3077]

[Figure 3078]

[Figure 3079]

[Figure 3080]

[Figure 3081]

[Figure 3082]

[Figure 3083]

[Figure 3084]

[Figure 3085]

[Figure 3086]

[Figure 3087]

[Figure 3088]

[Figure 3089]

[Figure 3090]

[Figure 3091]

[Figure 3092]

[Figure 3093]

[Figure 3094]

[Figure 3095]

[Figure 3096]

[Figure 3097]

[Figure 3098]

[Figure 3099]

[Figure 3100]

[Figure 3101]

[Figure 3102]

[Figure 3103]

[Figure 3104]

[Figure 3105]

[Figure 3106]

[Figure 3107]

[Figure 3108]

[Figure 3109]

[Figure 3110]

[Figure 3111]

[Figure 3112]

[Figure 3113]

[Figure 3114]

[Figure 3115]

[Figure 3116]

[Figure 3117]

[Figure 3118]

[Figure 3119]

[Figure 3120]

[Figure 3121]

[Figure 3122]

[Figure 3123]

[Figure 3124]

[Figure 3125]

[Figure 3126]

[Figure 3127]

[Figure 3128]

[Figure 3129]

[Figure 3130]

[Figure 3131]

[Figure 3132]

[Figure 3133]

[Figure 3134]

[Figure 3135]

[Figure 3136]

[Figure 3137]

[Figure 3138]

[Figure 3139]

[Figure 3140]

[Figure 3141]

[Figure 3142]

[Figure 3143]

[Figure 3144]

[Figure 3145]

[Figure 3146]

[Figure 3147]

[Figure 3148]

[Figure 3149]

[Figure 3150]

[Figure 3151]

[Figure 3152]

[Figure 3153]

[Figure 3154]

[Figure 3155]

[Figure 3156]

[Figure 3157]

[Figure 3158]

[Figure 3159]

[Figure 3160]

[Figure 3161]

[Figure 3162]

[Figure 3163]

[Figure 3164]

[Figure 3165]

[Figure 3166]

[Figure 3167]

[Figure 3168]

[Figure 3169]

[Figure 3170]

[Figure 3171]

[Figure 3172]

[Figure 3173]

[Figure 3174]

[Figure 3175]

[Figure 3176]

[Figure 3177]

[Figure 3178]

[Figure 3179]

[Figure 3180]

[Figure 3181]

[Figure 3182]

[Figure 3183]

[Figure 3184]

[Figure 3185]

[Figure 3186]

[Figure 3187]

[Figure 3188]

[Figure 3189]

[Figure 3190]

[Figure 3191]

[Figure 3192]

[Figure 3193]

[Figure 3194]

[Figure 3195]

[Figure 3196]

[Figure 3197]

[Figure 3198]

[Figure 3199]

[Figure 3200]

[Figure 3201]

[Figure 3202]

[Figure 3203]

[Figure 3204]

[Figure 3205]

[Figure 3206]

[Figure 3207]

[Figure 3208]

[Figure 3209]

[Figure 3210]

[Figure 3211]

[Figure 3212]

[Figure 3213]

[Figure 3214]

[Figure 3215]

[Figure 3216]

[Figure 3217]

[Figure 3218]

[Figure 3219]

[Figure 3220]

[Figure 3221]

[Figure 3222]

[Figure 3223]

[Figure 3224]

[Figure 3225]

[Figure 3226]

[Figure 3227]

[Figure 3228]

[Figure 3229]

[Figure 3230]

[Figure 3231]

[Figure 3232]

[Figure 3233]

[Figure 3234]

[Figure 3235]

[Figure 3236]

[Figure 3237]

[Figure 3238]

[Figure 3239]

[Figure 3240]

[Figure 3241]

[Figure 3242]

[Figure 3243]

[Figure 3244]

[Figure 3245]

[Figure 3246]

[Figure 3247]

[Figure 3248]

[Figure 3249]

[Figure 3250]

[Figure 3251]

[Figure 3252]

[Figure 3253]

[Figure 3254]

[Figure 3255]

[Figure 3256]

[Figure 3257]

[Figure 3258]

[Figure 3259]

[Figure 3260]

[Figure 3261]

[Figure 3262]

[Figure 3263]

[Figure 3264]

[Figure 3265]

[Figure 3266]

[Figure 3267]

[Figure 3268]

[Figure 3269]

[Figure 3270]

[Figure 3271]

[Figure 3272]

[Figure 3273]

[Figure 3274]

[Figure 3275]

[Figure 3276]

[Figure 3277]

[Figure 3278]

[Figure 3279]

[Figure 3280]

[Figure 3281]

[Figure 3282]

[Figure 3283]

[Figure 3284]

[Figure 3285]

[Figure 3286]

[Figure 3287]

[Figure 3288]

[Figure 3289]

[Figure 3290]

[Figure 3291]

[Figure 3292]

[Figure 3293]

[Figure 3294]

[Figure 3295]

[Figure 3296]

[Figure 3297]

[Figure 3298]

[Figure 3299]

[Figure 3300]

[Figure 3301]

[Figure 3302]

[Figure 3303]

[Figure 3304]

[Figure 3305]

[Figure 3306]

[Figure 3307]

[Figure 3308]

[Figure 3309]

[Figure 3310]

[Figure 3311]

[Figure 3312]

[Figure 3313]

[Figure 3314]

[Figure 3315]

[Figure 3316]

[Figure 3317]

[Figure 3318]

[Figure 3319]

[Figure 3320]

[Figure 3321]

[Figure 3322]

[Figure 3323]

[Figure 3324]

[Figure 3325]

[Figure 3326]

[Figure 3327]

[Figure 3328]

[Figure 3329]

[Figure 3330]

[Figure 3331]

[Figure 3332]

[Figure 3333]

[Figure 3334]

[Figure 3335]

[Figure 3336]

[Figure 3337]

[Figure 3338]

[Figure 3339]

[Figure 3340]

[Figure 3341]

[Figure 3342]

[Figure 3343]

[Figure 3344]

[Figure 3345]

[Figure 3346]

[Figure 3347]

[Figure 3348]

[Figure 3349]

[Figure 3350]

[Figure 3351]

[Figure 3352]

[Figure 3353]

[Figure 3354]

[Figure 3355]

[Figure 3356]

[Figure 3357]

[Figure 3358]

[Figure 3359]

[Figure 3360]

[Figure 3361]

[Figure 3362]

[Figure 3363]

[Figure 3364]

[Figure 3365]

[Figure 3366]

[Figure 3367]

[Figure 3368]

[Figure 3369]

[Figure 3370]

[Figure 3371]

[Figure 3372]

[Figure 3373]

[Figure 3374]

[Figure 3375]

[Figure 3376]

[Figure 3377]

[Figure 3378]

[Figure 3379]

[Figure 3380]

[Figure 3381]

[Figure 3382]

[Figure 3383]

[Figure 3384]

[Figure 3385]

[Figure 3386]

[Figure 3387]

[Figure 3388]

[Figure 3389]

[Figure 3390]

[Figure 3391]

[Figure 3392]

[Figure 3393]

[Figure 3394]

[Figure 3395]

[Figure 3396]

[Figure 3397]

[Figure 3398]

[Figure 3399]

[Figure 3400]

[Figure 3401]

[Figure 3402]

[Figure 3403]

[Figure 3404]

[Figure 3405]

[Figure 3406]

[Figure 3407]

[Figure 3408]

[Figure 3409]

[Figure 3410]

[Figure 3411]

[Figure 3412]

[Figure 3413]

[Figure 3414]

[Figure 3415]

[Figure 3416]

[Figure 3417]

[Figure 3418]

[Figure 3419]

[Figure 3420]

[Figure 3421]

[Figure 3422]

[Figure 3423]

[Figure 3424]

[Figure 3425]

[Figure 3426]

[Figure 3427]

[Figure 3428]

[Figure 3429]

[Figure 3430]

[Figure 3431]

[Figure 3432]

[Figure 3433]

[Figure 3434]

[Figure 3435]

[Figure 3436]

[Figure 3437]

[Figure 3438]

[Figure 3439]

[Figure 3440]

[Figure 3441]

[Figure 3442]

[Figure 3443]

[Figure 3444]

[Figure 3445]

[Figure 3446]

[Figure 3447]

[Figure 3448]

[Figure 3449]

[Figure 3450]

[Figure 3451]

[Figure 3452]

[Figure 3453]

[Figure 3454]

[Figure 3455]

[Figure 3456]

[Figure 3457]

[Figure 3458]

[Figure 3459]

[Figure 3460]

[Figure 3461]

[Figure 3462]

[Figure 3463]

[Figure 3464]

[Figure 3465]

[Figure 3466]

[Figure 3467]

[Figure 3468]

[Figure 3469]

[Figure 3470]

[Figure 3471]

[Figure 3472]

[Figure 3473]

[Figure 3474]

[Figure 3475]

[Figure 3476]

[Figure 3477]

[Figure 3478]

[Figure 3479]

[Figure 3480]

[Figure 3481]

[Figure 3482]

[Figure 3483]

[Figure 3484]

[Figure 3485]

[Figure 3486]

[Figure 3487]

[Figure 3488]

[Figure 3489]

[Figure 3490]

[Figure 3491]

[Figure 3492]

[Figure 3493]

[Figure 3494]

[Figure 3495]

[Figure 3496]

[Figure 3497]

[Figure 3498]

[Figure 3499]

[Figure 3500]

[Figure 3501]

[Figure 3502]

[Figure 3503]

[Figure 3504]

[Figure 3505]

[Figure 3506]

[Figure 3507]

[Figure 3508]

[Figure 3509]

[Figure 3510]

[Figure 3511]

[Figure 3512]

[Figure 3513]

[Figure 3514]

[Figure 3515]

[Figure 3516]

[Figure 3517]

[Figure 3518]

[Figure 3519]

[Figure 3520]

[Figure 3521]

[Figure 3522]

[Figure 3523]

[Figure 3524]

[Figure 3525]

[Figure 3526]

[Figure 3527]

[Figure 3528]

[Figure 3529]

[Figure 3530]

[Figure 3531]

[Figure 3532]

[Figure 3533]

[Figure 3534]

[Figure 3535]

[Figure 3536]

[Figure 3537]

[Figure 3538]

[Figure 3539]

[Figure 3540]

[Figure 3541]

[Figure 3542]

[Figure 3543]

[Figure 3544]

[Figure 3545]

[Figure 3546]

[Figure 3547]

[Figure 3548]

[Figure 3549]

[Figure 3550]

[Figure 3551]

[Figure 3552]

[Figure 3553]

[Figure 3554]

[Figure 3555]

[Figure 3556]

[Figure 3557]

[Figure 3558]

[Figure 3559]

[Figure 3560]

[Figure 3561]

[Figure 3562]

[Figure 3563]

[Figure 3564]

[Figure 3565]

[Figure 3566]

[Figure 3567]

[Figure 3568]

[Figure 3569]

[Figure 3570]

[Figure 3571]

[Figure 3572]

[Figure 3573]

[Figure 3574]

[Figure 3575]

[Figure 3576]

[Figure 3577]

[Figure 3578]

[Figure 3579]

[Figure 3580]

[Figure 3581]

[Figure 3582]

[Figure 3583]

[Figure 3584]

[Figure 3585]

[Figure 3586]

[Figure 3587]

[Figure 3588]

[Figure 3589]

[Figure 3590]

[Figure 3591]

[Figure 3592]

[Figure 3593]

[Figure 3594]

[Figure 3595]

[Figure 3596]

[Figure 3597]

[Figure 3598]

[Figure 3599]

[Figure 3600]

[Figure 3601]

[Figure 3602]

[Figure 3603]

[Figure 3604]

[Figure 3605]

[Figure 3606]

[Figure 3607]

[Figure 3608]

[Figure 3609]

[Figure 3610]

[Figure 3611]

[Figure 3612]

[Figure 3613]

[Figure 3614]

[Figure 3615]

[Figure 3616]

[Figure 3617]

[Figure 3618]

[Figure 3619]

[Figure 3620]

[Figure 3621]

[Figure 3622]

[Figure 3623]

[Figure 3624]

[Figure 3625]

[Figure 3626]

[Figure 3627]

[Figure 3628]

[Figure 3629]

[Figure 3630]

[Figure 3631]

[Figure 3632]

[Figure 3633]

[Figure 3634]

[Figure 3635]

[Figure 3636]

[Figure 3637]

[Figure 3638]

[Figure 3639]

[Figure 3640]

[Figure 3641]

[Figure 3642]

[Figure 3643]

[Figure 3644]

[Figure 3645]

[Figure 3646]

[Figure 3647]

[Figure 3648]

[Figure 3649]

[Figure 3650]

[Figure 3651]

[Figure 3652]

[Figure 3653]

[Figure 3654]

[Figure 3655]

[Figure 3656]

[Figure 3657]

[Figure 3658]

[Figure 3659]

[Figure 3660]

[Figure 3661]

[Figure 3662]

[Figure 3663]

[Figure 3664]

[Figure 3665]

[Figure 3666]

[Figure 3667]

[Figure 3668]

[Figure 3669]

[Figure 3670]

[Figure 3671]

[Figure 3672]

[Figure 3673]

[Figure 3674]

[Figure 3675]

[Figure 3676]

[Figure 3677]

[Figure 3678]

[Figure 3679]

[Figure 3680]

[Figure 3681]

[Figure 3682]

[Figure 3683]

[Figure 3684]

[Figure 3685]

[Figure 3686]

[Figure 3687]

[Figure 3688]

[Figure 3689]

[Figure 3690]

[Figure 3691]

[Figure 3692]

[Figure 3693]

[Figure 3694]

[Figure 3695]

[Figure 3696]

[Figure 3697]

[Figure 3698]

[Figure 3699]

[Figure 3700]

[Figure 3701]

[Figure 3702]

[Figure 3703]

[Figure 3704]

[Figure 3705]

[Figure 3706]

[Figure 3707]

[Figure 3708]

[Figure 3709]

[Figure 3710]

[Figure 3711]

[Figure 3712]

[Figure 3713]

[Figure 3714]

[Figure 3715]

[Figure 3716]

[Figure 3717]

[Figure 3718]

[Figure 3719]

[Figure 3720]

[Figure 3721]

[Figure 3722]

[Figure 3723]

[Figure 3724]

[Figure 3725]

[Figure 3726]

[Figure 3727]

[Figure 3728]

[Figure 3729]

[Figure 3730]

[Figure 3731]

[Figure 3732]

[Figure 3733]

[Figure 3734]

[Figure 3735]

[Figure 3736]

[Figure 3737]

[Figure 3738]

[Figure 3739]

[Figure 3740]

[Figure 3741]

[Figure 3742]

[Figure 3743]

[Figure 3744]

[Figure 3745]

[Figure 3746]

[Figure 3747]

[Figure 3748]

[Figure 3749]

[Figure 3750]

[Figure 3751]

[Figure 3752]

[Figure 3753]

[Figure 3754]

[Figure 3755]

[Figure 3756]

[Figure 3757]

[Figure 3758]

[Figure 3759]

[Figure 3760]

[Figure 3761]

[Figure 3762]

[Figure 3763]

[Figure 3764]

[Figure 3765]

[Figure 3766]

[Figure 3767]

[Figure 3768]

[Figure 3769]

[Figure 3770]

[Figure 3771]

[Figure 3772]

[Figure 3773]

[Figure 3774]

[Figure 3775]

[Figure 3776]

[Figure 3777]

[Figure 3778]

[Figure 3779]

[Figure 3780]

[Figure 3781]

[Figure 3782]

[Figure 3783]

[Figure 3784]

[Figure 3785]

[Figure 3786]

[Figure 3787]

[Figure 3788]

[Figure 3789]

[Figure 3790]

[Figure 3791]

[Figure 3792]

[Figure 3793]

[Figure 3794]

[Figure 3795]

[Figure 3796]

[Figure 3797]

[Figure 3798]

[Figure 3799]

[Figure 3800]

[Figure 3801]

[Figure 3802]

[Figure 3803]

[Figure 3804]

[Figure 3805]

[Figure 3806]

[Figure 3807]

[Figure 3808]

[Figure 3809]

[Figure 3810]

[Figure 3811]

[Figure 3812]

[Figure 3813]

[Figure 3814]

[Figure 3815]

[Figure 3816]

[Figure 3817]

[Figure 3818]

[Figure 3819]

[Figure 3820]

[Figure 3821]

[Figure 3822]

[Figure 3823]

[Figure 3824]

[Figure 3825]

[Figure 3826]

[Figure 3827]

[Figure 3828]

[Figure 3829]

[Figure 3830]

[Figure 3831]

[Figure 3832]

[Figure 3833]

[Figure 3834]

[Figure 3835]

[Figure 3836]

[Figure 3837]

[Figure 3838]

[Figure 3839]

[Figure 3840]

[Figure 3841]

[Figure 3842]

[Figure 3843]

[Figure 3844]

[Figure 3845]

[Figure 3846]

[Figure 3847]

[Figure 3848]

[Figure 3849]

[Figure 3850]

[Figure 3851]

[Figure 3852]

[Figure 3853]

[Figure 3854]

[Figure 3855]

[Figure 3856]

[Figure 3857]

[Figure 3858]

[Figure 3859]

[Figure 3860]

[Figure 3861]

[Figure 3862]

[Figure 3863]

[Figure 3864]

[Figure 3865]

[Figure 3866]

[Figure 3867]

[Figure 3868]

[Figure 3869]

[Figure 3870]

[Figure 3871]

[Figure 3872]

[Figure 3873]

[Figure 3874]

[Figure 3875]

[Figure 3876]

[Figure 3877]

[Figure 3878]

[Figure 3879]

[Figure 3880]

[Figure 3881]

[Figure 3882]

[Figure 3883]

[Figure 3884]

[Figure 3885]

[Figure 3886]

[Figure 3887]

[Figure 3888]

[Figure 3889]

[Figure 3890]

[Figure 3891]

[Figure 3892]

[Figure 3893]

[Figure 3894]

[Figure 3895]

[Figure 3896]

[Figure 3897]

[Figure 3898]

[Figure 3899]

[Figure 3900]

[Figure 3901]

[Figure 3902]

[Figure 3903]

[Figure 3904]

[Figure 3905]

[Figure 3906]

[Figure 3907]

[Figure 3908]

[Figure 3909]

[Figure 3910]

[Figure 3911]

[Figure 3912]

[Figure 3913]

[Figure 3914]

[Figure 3915]

[Figure 3916]

[Figure 3917]

[Figure 3918]

[Figure 3919]

[Figure 3920]

[Figure 3921]

[Figure 3922]

[Figure 3923]

[Figure 3924]

[Figure 3925]

[Figure 3926]

[Figure 3927]

[Figure 3928]

[Figure 3929]

[Figure 3930]

[Figure 3931]

[Figure 3932]

[Figure 3933]

[Figure 3934]

[Figure 3935]

[Figure 3936]

[Figure 3937]

[Figure 3938]

[Figure 3939]

[Figure 3940]

[Figure 3941]

[Figure 3942]

[Figure 3943]

[Figure 3944]

[Figure 3945]

[Figure 3946]

[Figure 3947]

[Figure 3948]

[Figure 3949]

[Figure 3950]

[Figure 3951]

[Figure 3952]

[Figure 3953]

[Figure 3954]

[Figure 3955]

[Figure 3956]

[Figure 3957]

[Figure 3958]

[Figure 3959]

[Figure 3960]

[Figure 3961]

[Figure 3962]

[Figure 3963]

[Figure 3964]

[Figure 3965]

[Figure 3966]

[Figure 3967]

[Figure 3968]

[Figure 3969]

[Figure 3970]

[Figure 3971]

[Figure 3972]

[Figure 3973]

[Figure 3974]

[Figure 3975]

[Figure 3976]

[Figure 3977]

[Figure 3978]

[Figure 3979]

[Figure 3980]

[Figure 3981]

[Figure 3982]

[Figure 3983]

[Figure 3984]

[Figure 3985]

[Figure 3986]

[Figure 3987]

[Figure 3988]

[Figure 3989]

[Figure 3990]

[Figure 3991]

[Figure 3992]

[Figure 3993]

[Figure 3994]

[Figure 3995]

[Figure 3996]

[Figure 3997]

[Figure 3998]

[Figure 3999]

[Figure 4000]

[Figure 4001]

[Figure 4002]

[Figure 4003]

[Figure 4004]

[Figure 4005]

[Figure 4006]

[Figure 4007]

[Figure 4008]

[Figure 4009]

[Figure 4010]

[Figure 4011]

[Figure 4012]

[Figure 4013]

[Figure 4014]

[Figure 4015]

[Figure 4016]

[Figure 4017]

[Figure 4018]

[Figure 4019]

[Figure 4020]

[Figure 4021]

[Figure 4022]

[Figure 4023]

[Figure 4024]

[Figure 4025]

[Figure 4026]

[Figure 4027]

[Figure 4028]

[Figure 4029]

[Figure 4030]

[Figure 4031]

[Figure 4032]

[Figure 4033]

[Figure 4034]

[Figure 4035]

[Figure 4036]

[Figure 4037]

[Figure 4038]

[Figure 4039]

[Figure 4040]

[Figure 4041]

[Figure 4042]

[Figure 4043]

[Figure 4044]

[Figure 4045]

[Figure 4046]

[Figure 4047]

[Figure 4048]

[Figure 4049]

[Figure 4050]

[Figure 4051]

[Figure 4052]

[Figure 4053]

[Figure 4054]

[Figure 4055]

[Figure 4056]

[Figure 4057]

[Figure 4058]

[Figure 4059]

[Figure 4060]

[Figure 4061]

[Figure 4062]

[Figure 4063]

[Figure 4064]

[Figure 4065]

[Figure 4066]

[Figure 4067]

[Figure 4068]

[Figure 4069]

[Figure 4070]

[Figure 4071]

[Figure 4072]

[Figure 4073]

[Figure 4074]

[Figure 4075]

[Figure 4076]

[Figure 4077]

[Figure 4078]

[Figure 4079]

[Figure 4080]

[Figure 4081]

[Figure 4082]

[Figure 4083]

[Figure 4084]

[Figure 4085]

[Figure 4086]

[Figure 4087]

[Figure 4088]

[Figure 4089]

[Figure 4090]

[Figure 4091]

[Figure 4092]

[Figure 4093]

[Figure 4094]

[Figure 4095]

[Figure 4096]

[Figure 4097]

[Figure 4098]

[Figure 4099]

[Figure 4100]

[Figure 4101]

[Figure 4102]

[Figure 4103]

[Figure 4104]

[Figure 4105]

[Figure 4106]

[Figure 4107]

[Figure 4108]

[Figure 4109]

[Figure 4110]

[Figure 4111]

[Figure 4112]

[Figure 4113]

[Figure 4114]

[Figure 4115]

[Figure 4116]

[Figure 4117]

[Figure 4118]

[Figure 4119]

[Figure 4120]

[Figure 4121]

[Figure 4122]

[Figure 4123]

[Figure 4124]

[Figure 4125]

[Figure 4126]

[Figure 4127]

[Figure 4128]

[Figure 4129]

[Figure 4130]

[Figure 4131]

[Figure 4132]

[Figure 4133]

[Figure 4134]

[Figure 4135]

[Figure 4136]

[Figure 4137]

[Figure 4138]

[Figure 4139]

[Figure 4140]

[Figure 4141]

[Figure 4142]

[Figure 4143]

[Figure 4144]

[Figure 4145]

[Figure 4146]

[Figure 4147]

[Figure 4148]

[Figure 4149]

[Figure 4150]

[Figure 4151]

[Figure 4152]

[Figure 4153]

[Figure 4154]

[Figure 4155]

[Figure 4156]

[Figure 4157]

[Figure 4158]

[Figure 4159]

[Figure 4160]

[Figure 4161]

[Figure 4162]

[Figure 4163]

[Figure 4164]

[Figure 4165]

[Figure 4166]

[Figure 4167]

[Figure 4168]

[Figure 4169]

[Figure 4170]

[Figure 4171]

[Figure 4172]

[Figure 4173]

[Figure 4174]

[Figure 4175]

[Figure 4176]

[Figure 4177]

[Figure 4178]

[Figure 4179]

[Figure 4180]

[Figure 4181]

[Figure 4182]

[Figure 4183]

[Figure 4184]

[Figure 4185]

[Figure 4186]

[Figure 4187]

[Figure 4188]

[Figure 4189]

[Figure 4190]

[Figure 4191]

[Figure 4192]

[Figure 4193]

[Figure 4194]

[Figure 4195]

[Figure 4196]

[Figure 4197]

[Figure 4198]

[Figure 4199]

[Figure 4200]

[Figure 4201]

[Figure 4202]

[Figure 4203]

[Figure 4204]

[Figure 4205]

[Figure 4206]

[Figure 4207]

[Figure 4208]

[Figure 4209]

[Figure 4210]

[Figure 4211]

[Figure 4212]

[Figure 4213]

[Figure 4214]

[Figure 4215]

[Figure 4216]

[Figure 4217]

[Figure 4218]

[Figure 4219]

[Figure 4220]

[Figure 4221]

[Figure 4222]

[Figure 4223]

[Figure 4224]

[Figure 4225]

[Figure 4226]

[Figure 4227]

[Figure 4228]

[Figure 4229]

[Figure 4230]

[Figure 4231]

[Figure 4232]

[Figure 4233]

[Figure 4234]

[Figure 4235]

[Figure 4236]

[Figure 4237]

[Figure 4238]

[Figure 4239]

[Figure 4240]

[Figure 4241]

[Figure 4242]

[Figure 4243]

[Figure 4244]

[Figure 4245]

[Figure 4246]

[Figure 4247]

[Figure 4248]

[Figure 4249]

[Figure 4250]

[Figure 4251]

5

[Figure 4252]

[Figure 4253]

[Figure 4254]

[Figure 4255]

[Figure 4256]

[Figure 4257]

[Figure 4258]

[Figure 4259]

[Figure 4260]

[Figure 4261]

[Figure 4262]

[Figure 4263]

[Figure 4264]

[Figure 4265]

[Figure 4266]

[Figure 4267]

[Figure 4268]

[Figure 4269]

[Figure 4270]

[Figure 4271]

[Figure 4272]

[Figure 4273]

[Figure 4274]

[Figure 4275]

[Figure 4276]

[Figure 4277]

[Figure 4278]

[Figure 4279]

[Figure 4280]

[Figure 4281]

[Figure 4282]

[Figure 4283]

[Figure 4284]

[Figure 4285]

[Figure 4286]

[Figure 4287]

[Figure 4288]

[Figure 4289]

[Figure 4290]

[Figure 4291]

[Figure 4292]

[Figure 4293]

[Figure 4294]

[Figure 4295]

[Figure 4296]

[Figure 4297]

[Figure 4298]

[Figure 4299]

[Figure 4300]

[Figure 4301]

[Figure 4302]

[Figure 4303]

[Figure 4304]

[Figure 4305]

[Figure 4306]

[Figure 4307]

[Figure 4308]

[Figure 4309]

[Figure 4310]

[Figure 4311]

[Figure 4312]

[Figure 4313]

[Figure 4314]

[Figure 4315]

[Figure 4316]

[Figure 4317]

[Figure 4318]

[Figure 4319]

[Figure 4320]

[Figure 4321]

[Figure 4322]

[Figure 4323]

[Figure 4324]

[Figure 4325]

[Figure 4326]

[Figure 4327]

[Figure 4328]

[Figure 4329]

[Figure 4330]

[Figure 4331]

[Figure 4332]

[Figure 4333]

[Figure 4334]

[Figure 4335]

[Figure 4336]

[Figure 4337]

[Figure 4338]

[Figure 4339]

[Figure 4340]

[Figure 4341]

[Figure 4342]

[Figure 4343]

[Figure 4344]

[Figure 4345]

[Figure 4346]

[Figure 4347]

[Figure 4348]

[Figure 4349]

[Figure 4350]

[Figure 4351]

[Figure 4352]

[Figure 4353]

[Figure 4354]

[Figure 4355]

[Figure 4356]

[Figure 4357]

[Figure 4358]

[Figure 4359]

[Figure 4360]

[Figure 4361]

[Figure 4362]

[Figure 4363]

[Figure 4364]

[Figure 4365]

[Figure 4366]

[Figure 4367]

[Figure 4368]

[Figure 4369]

[Figure 4370]

[Figure 4371]

[Figure 4372]

[Figure 4373]

[Figure 4374]

[Figure 4375]

[Figure 4376]

[Figure 4377]

[Figure 4378]

[Figure 4379]

[Figure 4380]

[Figure 4381]

[Figure 4382]

[Figure 4383]

[Figure 4384]

[Figure 4385]

[Figure 4386]

[Figure 4387]

[Figure 4388]

[Figure 4389]

[Figure 4390]

[Figure 4391]

[Figure 4392]

[Figure 4393]

[Figure 4394]

[Figure 4395]

[Figure 4396]

[Figure 4397]

[Figure 4398]

[Figure 4399]

[Figure 4400]

[Figure 4401]

[Figure 4402]

[Figure 4403]

[Figure 4404]

[Figure 4405]

[Figure 4406]

[Figure 4407]

[Figure 4408]

[Figure 4409]

[Figure 4410]

[Figure 4411]

[Figure 4412]

[Figure 4413]

[Figure 4414]

[Figure 4415]

[Figure 4416]

[Figure 4417]

[Figure 4418]

[Figure 4419]

[Figure 4420]

[Figure 4421]

[Figure 4422]

[Figure 4423]

[Figure 4424]

[Figure 4425]

[Figure 4426]

[Figure 4427]

[Figure 4428]

[Figure 4429]

[Figure 4430]

[Figure 4431]

[Figure 4432]

[Figure 4433]

[Figure 4434]

[Figure 4435]

[Figure 4436]

[Figure 4437]

[Figure 4438]

[Figure 4439]

[Figure 4440]

[Figure 4441]

[Figure 4442]

[Figure 4443]

[Figure 4444]

[Figure 4445]

[Figure 4446]

[Figure 4447]

[Figure 4448]

[Figure 4449]

[Figure 4450]

[Figure 4451]

[Figure 4452]

[Figure 4453]

[Figure 4454]

[Figure 4455]

[Figure 4456]

[Figure 4457]

[Figure 4458]

[Figure 4459]

[Figure 4460]

[Figure 4461]

[Figure 4462]

[Figure 4463]

[Figure 4464]

[Figure 4465]

[Figure 4466]

[Figure 4467]

[Figure 4468]

[Figure 4469]

[Figure 4470]

[Figure 4471]

[Figure 4472]

[Figure 4473]

[Figure 4474]

[Figure 4475]

[Figure 4476]

[Figure 4477]

[Figure 4478]

[Figure 4479]

[Figure 4480]

[Figure 4481]

[Figure 4482]

[Figure 4483]

[Figure 4484]

[Figure 4485]

[Figure 4486]

[Figure 4487]

[Figure 4488]

[Figure 4489]

[Figure 4490]

[Figure 4491]

[Figure 4492]

[Figure 4493]

[Figure 4494]

[Figure 4495]

[Figure 4496]

[Figure 4497]

[Figure 4498]

[Figure 4499]

[Figure 4500]

[Figure 4501]

[Figure 4502]

[Figure 4503]

[Figure 4504]

[Figure 4505]

[Figure 4506]

[Figure 4507]

[Figure 4508]

[Figure 4509]

[Figure 4510]

[Figure 4511]

[Figure 4512]

[Figure 4513]

[Figure 4514]

[Figure 4515]

[Figure 4516]

[Figure 4517]

[Figure 4518]

[Figure 4519]

[Figure 4520]

[Figure 4521]

[Figure 4522]

[Figure 4523]

[Figure 4524]

[Figure 4525]

[Figure 4526]

[Figure 4527]

[Figure 4528]

[Figure 4529]

[Figure 4530]

[Figure 4531]

[Figure 4532]

[Figure 4533]

[Figure 4534]

[Figure 4535]

[Figure 4536]

[Figure 4537]

[Figure 4538]

[Figure 4539]

[Figure 4540]

[Figure 4541]

[Figure 4542]

[Figure 4543]

[Figure 4544]

[Figure 4545]

[Figure 4546]

[Figure 4547]

[Figure 4548]

[Figure 4549]

[Figure 4550]

[Figure 4551]

[Figure 4552]

[Figure 4553]

[Figure 4554]

[Figure 4555]

[Figure 4556]

[Figure 4557]

[Figure 4558]

[Figure 4559]

[Figure 4560]

[Figure 4561]

[Figure 4562]

[Figure 4563]

[Figure 4564]

[Figure 4565]

[Figure 4566]

[Figure 4567]

[Figure 4568]

[Figure 4569]

[Figure 4570]

[Figure 4571]

[Figure 4572]

[Figure 4573]

[Figure 4574]

[Figure 4575]

[Figure 4576]

[Figure 4577]

[Figure 4578]

[Figure 4579]

[Figure 4580]

[Figure 4581]

[Figure 4582]

[Figure 4583]

[Figure 4584]

[Figure 4585]

[Figure 4586]

[Figure 4587]

[Figure 4588]

[Figure 4589]

[Figure 4590]

[Figure 4591]

[Figure 4592]

[Figure 4593]

[Figure 4594]

[Figure 4595]

[Figure 4596]

[Figure 4597]

[Figure 4598]

[Figure 4599]

[Figure 4600]

[Figure 4601]

[Figure 4602]

[Figure 4603]

[Figure 4604]

[Figure 4605]

[Figure 4606]

[Figure 4607]

[Figure 4608]

[Figure 4609]

[Figure 4610]

[Figure 4611]

[Figure 4612]

[Figure 4613]

[Figure 4614]

[Figure 4615]

[Figure 4616]

[Figure 4617]

[Figure 4618]

[Figure 4619]

[Figure 4620]

[Figure 4621]

[Figure 4622]

[Figure 4623]

[Figure 4624]

[Figure 4625]

[Figure 4626]

[Figure 4627]

[Figure 4628]

[Figure 4629]

[Figure 4630]

[Figure 4631]

[Figure 4632]

[Figure 4633]

[Figure 4634]

[Figure 4635]

[Figure 4636]

[Figure 4637]

[Figure 4638]

[Figure 4639]

[Figure 4640]

[Figure 4641]

[Figure 4642]

[Figure 4643]

[Figure 4644]

[Figure 4645]

[Figure 4646]

[Figure 4647]

[Figure 4648]

[Figure 4649]

[Figure 4650]

[Figure 4651]

[Figure 4652]

[Figure 4653]

[Figure 4654]

[Figure 4655]

[Figure 4656]

[Figure 4657]

[Figure 4658]

[Figure 4659]

[Figure 4660]

[Figure 4661]

[Figure 4662]

[Figure 4663]

[Figure 4664]

[Figure 4665]

[Figure 4666]

[Figure 4667]

[Figure 4668]

[Figure 4669]

[Figure 4670]

[Figure 4671]

[Figure 4672]

[Figure 4673]

[Figure 4674]

[Figure 4675]

[Figure 4676]

[Figure 4677]

[Figure 4678]

[Figure 4679]

[Figure 4680]

[Figure 4681]

[Figure 4682]

[Figure 4683]

[Figure 4684]

[Figure 4685]

[Figure 4686]

[Figure 4687]

[Figure 4688]

[Figure 4689]

[Figure 4690]

[Figure 4691]

[Figure 4692]

[Figure 4693]

[Figure 4694]

[Figure 4695]

[Figure 4696]

[Figure 4697]

[Figure 4698]

[Figure 4699]

[Figure 4700]

[Figure 4701]

[Figure 4702]

[Figure 4703]

[Figure 4704]

[Figure 4705]

[Figure 4706]

[Figure 4707]

[Figure 4708]

[Figure 4709]

[Figure 4710]

[Figure 4711]

[Figure 4712]

[Figure 4713]

[Figure 4714]

[Figure 4715]

[Figure 4716]

[Figure 4717]

[Figure 4718]

[Figure 4719]

[Figure 4720]

[Figure 4721]

[Figure 4722]

[Figure 4723]

[Figure 4724]

[Figure 4725]

[Figure 4726]

[Figure 4727]

[Figure 4728]

[Figure 4729]

[Figure 4730]

[Figure 4731]

[Figure 4732]

[Figure 4733]

[Figure 4734]

[Figure 4735]

[Figure 4736]

[Figure 4737]

[Figure 4738]

[Figure 4739]

[Figure 4740]

[Figure 4741]

[Figure 4742]

[Figure 4743]

[Figure 4744]

[Figure 4745]

[Figure 4746]

[Figure 4747]

[Figure 4748]

[Figure 4749]

[Figure 4750]

[Figure 4751]

[Figure 4752]

[Figure 4753]

[Figure 4754]

[Figure 4755]

[Figure 4756]

[Figure 4757]

[Figure 4758]

[Figure 4759]

[Figure 4760]

[Figure 4761]

[Figure 4762]

[Figure 4763]

[Figure 4764]

[Figure 4765]

[Figure 4766]

[Figure 4767]

[Figure 4768]

[Figure 4769]

[Figure 4770]

[Figure 4771]

[Figure 4772]

[Figure 4773]

[Figure 4774]

[Figure 4775]

[Figure 4776]

[Figure 4777]

[Figure 4778]

[Figure 4779]

[Figure 4780]

[Figure 4781]

[Figure 4782]

[Figure 4783]

[Figure 4784]

[Figure 4785]

[Figure 4786]

[Figure 4787]

[Figure 4788]

[Figure 4789]

[Figure 4790]

[Figure 4791]

[Figure 4792]

[Figure 4793]

[Figure 4794]

[Figure 4795]

[Figure 4796]

[Figure 4797]

[Figure 4798]

[Figure 4799]

[Figure 4800]

[Figure 4801]

[Figure 4802]

[Figure 4803]

[Figure 4804]

[Figure 4805]

[Figure 4806]

[Figure 4807]

[Figure 4808]

[Figure 4809]

[Figure 4810]

[Figure 4811]

[Figure 4812]

[Figure 4813]

[Figure 4814]

[Figure 4815]

[Figure 4816]

[Figure 4817]

[Figure 4818]

[Figure 4819]

[Figure 4820]

[Figure 4821]

[Figure 4822]

[Figure 4823]

[Figure 4824]

[Figure 4825]

[Figure 4826]

[Figure 4827]

[Figure 4828]

[Figure 4829]

[Figure 4830]

[Figure 4831]

[Figure 4832]

[Figure 4833]

[Figure 4834]

[Figure 4835]

[Figure 4836]

[Figure 4837]

[Figure 4838]

[Figure 4839]

[Figure 4840]

[Figure 4841]

[Figure 4842]

[Figure 4843]

[Figure 4844]

[Figure 4845]

[Figure 4846]

[Figure 4847]

[Figure 4848]

[Figure 4849]

[Figure 4850]

[Figure 4851]

[Figure 4852]

[Figure 4853]

[Figure 4854]

[Figure 4855]

[Figure 4856]

[Figure 4857]

[Figure 4858]

[Figure 4859]

[Figure 4860]

[Figure 4861]

[Figure 4862]

[Figure 4863]

[Figure 4864]

[Figure 4865]

[Figure 4866]

[Figure 4867]

[Figure 4868]

[Figure 4869]

[Figure 4870]

[Figure 4871]

[Figure 4872]

[Figure 4873]

[Figure 4874]

[Figure 4875]

[Figure 4876]

[Figure 4877]

[Figure 4878]

[Figure 4879]

[Figure 4880]

[Figure 4881]

[Figure 4882]

[Figure 4883]

[Figure 4884]

[Figure 4885]

[Figure 4886]

[Figure 4887]

[Figure 4888]

[Figure 4889]

[Figure 4890]

[Figure 4891]

[Figure 4892]

[Figure 4893]

[Figure 4894]

[Figure 4895]

[Figure 4896]

[Figure 4897]

[Figure 4898]

[Figure 4899]

[Figure 4900]

[Figure 4901]

[Figure 4902]

[Figure 4903]

[Figure 4904]

[Figure 4905]

[Figure 4906]

[Figure 4907]

[Figure 4908]

[Figure 4909]

[Figure 4910]

[Figure 4911]

[Figure 4912]

[Figure 4913]

[Figure 4914]

[Figure 4915]

[Figure 4916]

[Figure 4917]

[Figure 4918]

[Figure 4919]

[Figure 4920]

[Figure 4921]

[Figure 4922]

[Figure 4923]

[Figure 4924]

[Figure 4925]

[Figure 4926]

[Figure 4927]

[Figure 4928]

[Figure 4929]

[Figure 4930]

[Figure 4931]

[Figure 4932]

[Figure 4933]

[Figure 4934]

[Figure 4935]

[Figure 4936]

[Figure 4937]

[Figure 4938]

[Figure 4939]

[Figure 4940]

[Figure 4941]

[Figure 4942]

[Figure 4943]

[Figure 4944]

[Figure 4945]

[Figure 4946]

[Figure 4947]

[Figure 4948]

[Figure 4949]

[Figure 4950]

[Figure 4951]

[Figure 4952]

[Figure 4953]

[Figure 4954]

[Figure 4955]

[Figure 4956]

[Figure 4957]

[Figure 4958]

[Figure 4959]

[Figure 4960]

[Figure 4961]

[Figure 4962]

[Figure 4963]

[Figure 4964]

[Figure 4965]

[Figure 4966]

[Figure 4967]

[Figure 4968]

[Figure 4969]

[Figure 4970]

[Figure 4971]

[Figure 4972]

[Figure 4973]

[Figure 4974]

[Figure 4975]

[Figure 4976]

[Figure 4977]

[Figure 4978]

[Figure 4979]

[Figure 4980]

[Figure 4981]

[Figure 4982]

[Figure 4983]

[Figure 4984]

[Figure 4985]

[Figure 4986]

[Figure 4987]

[Figure 4988]

[Figure 4989]

[Figure 4990]

[Figure 4991]

[Figure 4992]

[Figure 4993]

[Figure 4994]

[Figure 4995]

[Figure 4996]

[Figure 4997]

[Figure 4998]

[Figure 4999]

[Figure 5000]

[Figure 5001]

[Figure 5002]

[Figure 5003]

[Figure 5004]

[Figure 5005]

[Figure 5006]

[Figure 5007]

[Figure 5008]

[Figure 5009]

[Figure 5010]

[Figure 5011]

[Figure 5012]

[Figure 5013]

[Figure 5014]

[Figure 5015]

[Figure 5016]

[Figure 5017]

[Figure 5018]

[Figure 5019]

[Figure 5020]

[Figure 5021]

[Figure 5022]

[Figure 5023]

[Figure 5024]

[Figure 5025]

[Figure 5026]

[Figure 5027]

[Figure 5028]

[Figure 5029]

[Figure 5030]

[Figure 5031]

[Figure 5032]

[Figure 5033]

[Figure 5034]

[Figure 5035]

[Figure 5036]

[Figure 5037]

[Figure 5038]

[Figure 5039]

[Figure 5040]

[Figure 5041]

[Figure 5042]

[Figure 5043]

[Figure 5044]

[Figure 5045]

[Figure 5046]

[Figure 5047]

[Figure 5048]

[Figure 5049]

[Figure 5050]

[Figure 5051]

[Figure 5052]

[Figure 5053]

[Figure 5054]

[Figure 5055]

[Figure 5056]

[Figure 5057]

[Figure 5058]

[Figure 5059]

[Figure 5060]

[Figure 5061]

[Figure 5062]

[Figure 5063]

[Figure 5064]

[Figure 5065]

[Figure 5066]

[Figure 5067]

[Figure 5068]

[Figure 5069]

[Figure 5070]

[Figure 5071]

[Figure 5072]

[Figure 5073]

[Figure 5074]

[Figure 5075]

[Figure 5076]

[Figure 5077]

[Figure 5078]

[Figure 5079]

[Figure 5080]

[Figure 5081]

[Figure 5082]

[Figure 5083]

[Figure 5084]

[Figure 5085]

[Figure 5086]

[Figure 5087]

[Figure 5088]

[Figure 5089]

[Figure 5090]

[Figure 5091]

[Figure 5092]

[Figure 5093]

[Figure 5094]

[Figure 5095]

[Figure 5096]

[Figure 5097]

[Figure 5098]

[Figure 5099]

[Figure 5100]

[Figure 5101]

[Figure 5102]

[Figure 5103]

[Figure 5104]

[Figure 5105]

[Figure 5106]

[Figure 5107]

[Figure 5108]

[Figure 5109]

[Figure 5110]

[Figure 5111]

[Figure 5112]

[Figure 5113]

[Figure 5114]

[Figure 5115]

[Figure 5116]

[Figure 5117]

[Figure 5118]

[Figure 5119]

[Figure 5120]

[Figure 5121]

[Figure 5122]

[Figure 5123]

[Figure 5124]

[Figure 5125]

[Figure 5126]

[Figure 5127]

[Figure 5128]

[Figure 5129]

[Figure 5130]

[Figure 5131]

[Figure 5132]

[Figure 5133]

[Figure 5134]

[Figure 5135]

[Figure 5136]

[Figure 5137]

[Figure 5138]

[Figure 5139]

[Figure 5140]

[Figure 5141]

[Figure 5142]

[Figure 5143]

[Figure 5144]

[Figure 5145]

[Figure 5146]

[Figure 5147]

[Figure 5148]

[Figure 5149]

[Figure 5150]

[Figure 5151]

[Figure 5152]

[Figure 5153]

[Figure 5154]

[Figure 5155]

[Figure 5156]

[Figure 5157]

[Figure 5158]

[Figure 5159]

[Figure 5160]

[Figure 5161]

[Figure 5162]

[Figure 5163]

[Figure 5164]

[Figure 5165]

[Figure 5166]

[Figure 5167]

[Figure 5168]

[Figure 5169]

[Figure 5170]

[Figure 5171]

[Figure 5172]

[Figure 5173]

[Figure 5174]

[Figure 5175]

[Figure 5176]

[Figure 5177]

[Figure 5178]

[Figure 5179]

[Figure 5180]

[Figure 5181]

[Figure 5182]

[Figure 5183]

[Figure 5184]

[Figure 5185]

[Figure 5186]

[Figure 5187]

[Figure 5188]

[Figure 5189]

[Figure 5190]

[Figure 5191]

[Figure 5192]

[Figure 5193]

[Figure 5194]

[Figure 5195]

[Figure 5196]

[Figure 5197]

[Figure 5198]

[Figure 5199]

0

40

| |
|---|

relativeweight[%]

30

20

10

↑

← Σ

0

5

10 15 20 25 [Hz]

- Figure 13: This ﬁgure shows the weight vector (display as a channel × frequency matrix) of a sparse classiﬁer (absolute values) that was trained to discriminate left .vs right hand motor imagery. The bar on the bottom shows the sum across all channels and is displayed also in the lower right plot. The focus in the frequency range lies on the αband (here 11–14Hz). The bar on the right side of the matrix show the sum across all frequency bands and is displayed as scalp topography in the upper right plot. Note that less than 4% of the features were assigned non-zero weights.

expect from a physiological point of view and the mathematical programming method could match perfectly with neurophysiological intuition. More interesting and realistic is an exploratory scenario, where (1) a new paradigm is tested that could generate also unexpected neurophysiological signatures, (2) a hypothesis about underlying task relevant brain processes is generated automatically by the learning machine, and (3) ﬁnally the paradigm is adapted, so in principle a better understanding of the brain processes could be inferred. In this sense a machine learning method offering explanation, can be of great use in the semi-automatic exploration loop for testing new paradigms.

#### 5 Lines of Further Improvement

##### 5.1 CSSP: CSP with simultaneous spectral optimization

One drawback of the classical CSP algorithm from eqn. 1 is that its performance strongly depends on the appropriate choice of the band-pass ﬁlter that needs to be applied to the EEG data in advance. Although [Müller-Gerking et al., 1999] found evidence that a broad band ﬁlter is the best general choice, a subject-speciﬁc ﬁne tuned ﬁlter that is adapted to the individual spectral properties can enhance the results.

The idea of our Common Spatio-Spectral Pattern (CSSP) algorithm ( [Lemm et al.,

- 2005]) is to simultaneously optimize the spatial ﬁlter in conjunction with very simple frequency ﬁlters (one tapped delay FIR ﬁlter) for each channel.

Therefore CSSP solves the standard CSP problem in state space, given by the concatenation of the original signal x and its off τms delayed version xτ. More intuitively, we are optimizing a spatial ﬁlter in an extended spatial domain, were the delayed signals are treated as new channels (x,xτ) . Consequently this yields spatial projections

w0,wτ , that correspond to vectors in this extended spatial domain. Any spatial projection in state space can be expressed as a combination of a pure spatial and spectral ﬁlter applied to the original data x, as follow:

# (w0,wτ) ,(x,xτ) = ∑

w(c0)xc,· +wc(τ)xτc,·

c=1

wc(τ) γc

w(c0) γc

# = ∑

γc

xc,· +

[Figure 5200]

[Figure 5201]

c=1

xτc,· , (5)

τ−1

(τ) c

(0) c

where (γc)c=1,...,C deﬁnes a pure spatial ﬁlter, whereas (w

0,... ,0, w

[Figure 5202]

[Figure 5203]

γc ) deﬁnes a Finite Impulse Response (FIR) ﬁlter at each electrode c. This decomposition into a spatial and a FIR ﬁlter is not unique, but there exists a very intuitive partitioning, i.e.

γc ,

[Figure 5204]

[Figure 5205]

[Figure 5206]

w(c0)2 +wc(τ)2 s ign w(c0)

γc :=

. (6)

[Figure 5207]

The use of the signed norm as spatial ﬁlterγenables us to examine the spatial origin of the projected source signals. In addition it allows us a one-dimensional parameterization of the FIR ﬁlter at each electrode

φc(τ) := atan

w(c0) wc(τ) ∈ −

π

π

,

[Figure 5208]

[Figure 5209]

[Figure 5210]

2

2

, (7)

and consequently the opportunity for easy visualization of the spatial distribution of the utilized spectral information.

Summarizing, to solve the CSP analysis in the state space, allows us to neglect or emphasize speciﬁc frequency bands at each electrode position. However, the performance of a classiﬁcation method using CSSP-based extracted features will explicitly depend on the speciﬁc choice of τ which can be accomplished by some validation approach on the calibration data. More complex frequency ﬁlters can be found by concatenating more EEG-signals with several delays. However, as pointed out in [Lemm et al., 2005] in typical BCI situations where only small training sets are available, the

[Figure 5211]

2[signedr−values]

0.5

[Figure 5212]

0.01

2[signedr−values]

0.005

0

0

−0.005

−0.5

−0.01

(a) Differences of feedback runs to calibration measurement

(b) Differences of one feedback run to the previous run

- Figure 14: Subﬁgure (a) shows the differences in band energy from three feedback runs to the data of the calibration measurement as signed r2-values. The decrease of occipital alpha is most likely due to the increase visual input during BCI feedback. Subﬁgure (b) shows the difference in band energy of one feedback run (2 and 3) to its predecessor run. The important obervation here is that the r2-values for the differences between runs is 50 times smaller compared to (a).

choice of a single delay parameter is most effective. Different approaches that implement one global but more complex spectral ﬁlter into CSP are currently under investigation [Dornhege, 2006,Dornhege et al., 2006a].

##### 5.2 Investigating the need for adaptvity

Non-stationarities are ubiquitous in EEG signals. The question that is relevant in BCI research is (a) how much of this nonstationarity is reﬂected in the EEG features, that are used for BCI control, (b) how strongly is the classifer output affected by this change in class distributions, and (c) how this can be remedied. We quantiﬁed the shifting of the statistical distributions in particular in view of band energy values and the features one gets from CSP analysis. In contrast to several studies [del R. Millán, 2004,Vidaurre et al., 2004,Wolpaw and McFarland, 2004] that found substantial nonstationarities that need to be accounted for by adaptive classiﬁcation, our investigations lead to results of somewhat different ﬂavor. Notably the most serious shift of the distributions of band energy features occurred between the initial calibration measurement and online feedback operation of BCI. In contrast the differences during online operation from one run to another were rather inconsequential in most subjects, see Fig. 14. In other subjects those shifts were largely compensated by the CSP ﬁlters or the ﬁnal classiﬁer. The good news with respect the observed shift of distributions is that a simple adaption of classiﬁcation bias can successfully cure the problem. A thorough description of this study including new techniques for visualization and a systematic comparison of different classiﬁcation methods coping with shifting distributions can be found in [Shenoy et al.,

- 2006] and forthcoming papers.

#### 6 Discussion and Outlook

The Berlin Brain-Computer Interface makes use of a machine learning approach towards BCI. Working with high dimensional, complex features obtained from 128 channel EEG allows the system a distinguished ﬂexibility for adapting to the speciﬁc individual characteristics of each user’s brain. This way the BBCI system can provide feedback control even for untrained users typically after a 20 minutes calibration measurement which is then used for the training of the machine learning algorithms.

In one line of investigation we studied the detectability of premovement potentials in healthy subjects. It was shown that high bit rates in single-trial classiﬁcations can be achieved by fast-paced motor commands. An analysis of motor potentials during movementswith differentlimbs, e.g. ﬁngerII andV within one hand,exposeda possible way of further enhancement. A preliminary study involving patients with traumatic amputations showed that the results can be expected to transfer to phantom movements. Details will be published in a forthcoming paper.

In a second approach we investigate the possibility of establishing BCI control based on motor imagery without subject training. The result from a feedback study with six subjects impressively demonstrates that our system (1) robustly transfers the discrimination of mental states from the calibration to the feedback sessions, (2) allows a very fast switching between mental states, and (3) provides reliable feedback directly after a short calibration measurement and machine training without the need that the subject adapts to the system, all at high information transfer rates, see Table 1.

Recent BBCI activities comprise (a) mental typewriter experiments, with an integrated detector for the error potential, an idea that has be investigated off-line in several studies, cf. [Blankertz et al., 2003,Schalk et al., 2000,Parra et al., 2003,Ferrez and del R. Millán, 2005,Müller and Blankertz, 2006], (b) the online use of combined feature and multi-class paradigms (c) exploration of feature extraction for BCI and (d) realtime analysis of mental workload in subjects engaged in real world cognitive tasks, e.g., in driving situations [Dornhege et al., 2006b].

Our future studies will strive for 2D cursor control and robot arm control, still maintaining our philosophy of minimal subject training.

#### Acknowledgments

We would like to thank Siamac Fazli, Florin Popescu, Christin Schäfer, Ryota Tomioka, and Andreas Ziehe for fruitful discussions.

This work was supportedin part by grants of the Bundesministeriumfür Bildungund Forschung (BMBF), FKZ 01IBE01A/B and 01IGQ0414, by the Deutsche Forschungsgemeinschaft (DFG), FOR 375/B1, and by the IST Programme of the European Com-

munity, under the PASCAL Network of Excellence, IST-2002-506778.This publication only reﬂects the authors’ views.

#### References

[Bennett and Mangasarian, 1992] Bennett, K. and Mangasarian, O. (1992). Robust linear programming discrimination of two linearly inseparable sets. Optimization Methods and Software, 1:23–34.

[Birbaumer et al., 2000] Birbaumer, N., Kübler, A., Ghanayim, N., Hinterberger, T., Perelmouter, J., Kaiser, J., Iversen, I., Kotchoubey, B., Neumann, N., and Flor, H. (2000). The though translation device (TTD) for completly paralyzed patients. IEEE Trans. Rehab. Eng., 8(2):190–193.

[Bishop, 1995] Bishop, C. (1995). Neural Networks for Pattern Recognition. Oxford University Press.

- [Blankertz et al., 2002] Blankertz, B., Curio, G., and Müller, K.-R. (2002). Classifying single trial EEG: Towards brain computer interfacing. In Diettrich, T. G., Becker, S., and Ghahramani, Z., editors, Advances in Neural Inf. Proc. Systems (NIPS 01), volume 14, pages 157–164.

- [Blankertz et al., 2005] Blankertz, B., Dornhege, G., Krauledat, M., Müller, K.-R., and Curio, G.

(2005). The Berlin Brain-Computer Interface: Report from the feedback sessions. Technical Report 1, Fraunhofer FIRST.

- [Blankertz et al., 2006] Blankertz, B., Dornhege, G., Krauledat, M., Müller, K.-R., Kunzmann, V., Losch, F., and Curio, G. (2006). The Berlin Brain-Computer Interface: EEG-based communication without subject training. IEEE Trans. Neural Sys. Rehab. Eng., 14(2). in press.

- [Blankertz et al., 2003] Blankertz, B., Dornhege, G., Schäfer, C., Krepki, R., Kohlmorgen, J., Müller, K.-R., Kunzmann, V., Losch, F., and Curio, G. (2003). Boosting bit rates and error detection for the classiﬁcation of fast-paced motor commands based on single-trial EEG analysis. IEEE Trans. Neural Sys. Rehab. Eng., 11(2):127–131.

[Breiman et al., 1984] Breiman, L., Friedman, J., Olshen, J., and Stone, C. (1984). Classiﬁcation and Regression Trees. Wadsworth.

[Cui et al., 1999] Cui, R. Q., Huter, D., Lang, W., and Deecke, L. (1999). Neuroimage of voluntary movement: topography of the Bereitschaftspotential, a 64-channel DC current source density study. Neuroimage, 9(1):124–134.

[Curran and Stokes, 2003] Curran, E. A. and Stokes, M. J. (2003). Learning to control brain activity: A review of the production and control of EEG components for driving brain-computer interface (BCI) systems. Brain Cogn., 51:326–336.

[del R. Millán, 2004] del R. Millán, J. (2004). On the need for on-line learning in braincomputer interfaces. In Proceedings of the International Joint Conference on Neural Networks, Budapest, Hungary. IDIAP-RR 03-30.

[Dornhege, 2006] Dornhege, G. (2006). Increasing Information Transfer Rates for BrainComputer Interfacing. PhD thesis, University of Potsdam.

[Dornhege et al., 2004] Dornhege, G., Blankertz, B., Curio, G., and Müller, K.-R. (2004). Boosting bit rates in non-invasive EEG single-trial classiﬁcations by feature combination and multi-class paradigms. IEEE Trans. Biomed. Eng., 51(6):993–1002.

- [Dornhege et al., 2006a] Dornhege, G., Blankertz, B., Krauledat, M., Losch, F., Curio, G., and Müller, K.-R. (2006a). Combined optimization of spatial and temporal ﬁlters for improving brain-computer interfacing. IEEE Trans. Biomed. Eng. accepted.
- [Dornhege et al., 2006b] Dornhege, G., Braun, M., Kohlmorgen, J., Blankertz, B., Müller, K.-R., Curio, G., Hagemann, K., ns, A. B., Schrauf, M., and Kincses, W. (2006b). Improving human performance in a real operating environment through real-time mental workload detection. In Dornhege, G., del R. Millán, J., Hinterberger, T., McFarland, D., and Müller, K.-R., editors, Towards Brain-Computer Interfacing. MIT press. accepted.

- [Dornhege et al., 2006c] Dornhege, G., del R. Millán, J., Hinterberger, T., McFarland, D., and Müller, K.-R., editors (2006c). Towards Brain-Computer Interfacing. MIT Press. in preparation.
- [Dornhege et al., 2006d] Dornhege, G., Krauledat, M., Müller, K.-R., and Blankertz, B. (2006d). Towards Brain-Computer Interfacing, chapter General signal processing and machine learning tools for BCI. MIT Press. accepted.

[Elbert et al., 1980] Elbert, T., Rockstroh, B., Lutzenberger, W., and Birbaumer, N. (1980). Biofeedback of slow cortical potentials. I. Electroencephalogr. Clin. Neurophysiol., 48:293– 301.

[Ferrez and del R. Millán, 2005] Ferrez, P. and del R. Millán, J. (2005). You are wrong! – automatic detection of interaction errors from brain waves. In 19th International Joint Conference on Artiﬁcial Intelligence, pages 1413–1418.

[Friedman, 1991] Friedman, J. (1991). Multivariate adaptive regression splines. Annals of Statistics, 19(1):1–141. [Friedman, 1989] Friedman, J. H. (1989). Regularized discriminant analysis. J. Amer. Statist. Assoc., 84(405):165–175. [Fukunaga, 1990] Fukunaga, K. (1990). Introduction to Statistical Pattern Recognition. Aca-

demic Press, San Diego, 2nd edition. [ILOG, 1999] ILOG (1999). Ilog solver, ilog cplex 6.5 reference manual. . [Kornhuber and Deecke, 1965] Kornhuber, H. H. and Deecke, L. (1965). Hirnpotentialänderun-

gen bei Willkürbewegungen und passiven Bewegungen des Menschen: Bereitschaftspotential und reafferente Potentiale. Pﬂügers Arch., 284:1–17.

[Krauledat et al., 2004] Krauledat, M., Dornhege, G., Blankertz, B., Curio, G., and Müller, K.-R. (2004). The Berlin brain-computer interface for rapid response. Biomed. Tech., 49(1):61–62. [Krausz et al., 2003] Krausz, G., Scherer, R., Korisek, G., and Pfurtscheller, G. (2003). Critical decision-speed and information transfer in the "Graz Brain-Computer Interface". Appl. Psychophysiol. Biofeedback, 28(3):233–240.

[Kübler et al., 2001] Kübler, A., Kotchoubey, B., Kaiser, J., Wolpaw, J., and Birbaumer, N.

(2001). Brain-computer communication: Unlocking the locked in. Psychol. Bull., 127(3):358– 375.

[Kübler et al., 2005] Kübler, A., Nijboer, F., Mellinger, J., Vaughan, T. M., Pawelzik, H., Schalk, G., McFarland, D. J., Birbaumer, N., and Wolpaw, J. R. (2005). Patients with ALS can use sensorimotor rhythms to operate a brain-computer interface. Neurology, 64(10):1775–1777. [Lang et al., 1989] Lang, W., Lang, M., Uhl, F., Koska, C., Kornhuber, A., and Deecke, L.

(1989). Negative cortical DC shifts preceding and accompanying simultaneous and sequential movements. Exp. Brain Res., 74(1):99–104.

[Lemm et al., 2005] Lemm, S., Blankertz, B., Curio, G., and Müller, K.-R. (2005). Spatiospectral ﬁlters for improved classiﬁcation of single trial EEG. IEEE Trans. Biomed. Eng., 52(9):1541–1548.

[Mika et al., 2001] Mika, S., Rätsch, G., and Müller, K.-R. (2001). A mathematical programming approach to the Kernel Fisher algorithm. In Leen, T., Dietterich, T., and Tresp, V., editors, Advances in Neural Information Processing Systems, volume 13, pages 591–597. MIT Press.

[Mika et al., 2000] Mika, S., Rätsch, G., Weston, J., Schölkopf, B., Smola, A., and Müller, K.-R.

(2000). Learning discriminative and invariant nonlinear features. unpublished manuscript.

[Müller et al., 2003] Müller, K.-R., Anderson, C. W., and Birch, G. E. (2003). Linear and nonlinear methods for brain-computer interfaces. IEEE Trans. Neural Sys. Rehab. Eng., 11(2):165– 169.

[Müller and Blankertz, 2006] Müller, K.-R. and Blankertz, B. (2006). Toward non-invasive brain-computer interfaces. IEEE Signal Proc. Magazine. accepted.

[Müller et al., 2001] Müller, K.-R., Mika, S., Rätsch, G., Tsuda, K., and Schölkopf, B. (2001). An introduction to kernel-based learning algorithms. IEEE Neural Networks, 12(2):181–201.

[Müller-Gerking et al., 1999] Müller-Gerking, J., Pfurtscheller, G., and Flyvbjerg, H. (1999). Designing optimal spatial ﬁlters for single-trial EEG classiﬁcation in a movement task. Clin. Neurophysiol., 110:787–798.

[Parra et al., 2003] Parra, L., Spence, C., Gerson, A., and Sajda, P. (2003). Response error correction - a demonstration of improved human-machine performance using real-time EEG monitoring. IEEE Trans. Neural Sys. Rehab. Eng., 11(2):173–177.

[Pfurtscheller and da Silva, 1999] Pfurtscheller, G. and da Silva, F. H. L. (1999). Event-related EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol., 110(11):1842–1857.

[Pfurtscheller and Lopes da Silva, 1999] Pfurtscheller, G. and Lopes da Silva, F. (1999). Eventrelated EEG/MEG synchronization and desynchronization: basic principles. Clin. Neurophysiol., 110(11):1842–1857.

[Rätsch et al., 2001] Rätsch, G., Onoda, T., and Müller, K.-R. (2001). Soft margins for AdaBoost. Machine Learning, 42(3):287–320.

[Rockstroh et al., 1984] Rockstroh, B., Birbaumer, N., Elbert, T., and Lutzenberger, W. (1984). Operant control of EEG and event-related and slow brain potentials. Biofeedback and SelfRegulation, 9(2):139–160.

[Rosipal and Trejo, 2001] Rosipal, R. and Trejo, L. (2001). Kernel partial least squares regression in reproducing kernel hilbert space. J. Machine Learning Res., 2:97–123.

[Schalk et al., 2000] Schalk, G., Wolpaw, J. R., McFarland, D. J., and Pfurtscheller, G. (2000). EEG-based communication: presence of an error potential. Clin. Neurophysiol., 111:2138– 2144.

[Schölkopf et al., 1999] Schölkopf, B., Mika, S., Burges, C., Knirsch, P., Müller, K.-R., Rätsch, G., and Smola, A. (1999). Input space vs. feature space in kernel-based methods. IEEE Transactions on Neural Networks, 10(5):1000–1017.

[Schölkopf et al., 1998] Schölkopf, B., Smola, A., and Müller, K.-R. (1998). Nonlinear component analysis as a kernel eigenvalue problem. Neural Computation, 10:1299–1319. [Shenoy et al., 2006] Shenoy, P., Krauledat, M., Blankertz, B., Rao, R. P. N., and Müller, K.-R.

(2006). Towards adaptive classiﬁcation for bci. J. Neural Eng., 3:R13–R23. [Vapnik, 1995] Vapnik, V. (1995). The nature of statistical learning theory. Springer Verlag, New York. [Vaughan et al., 1998] Vaughan, T. M., Miner, L. A., McFarland, D. J., and Wolpaw, J. R.

(1998). EEG-based communication: analysis of concurrent EMG activity. Electroencephalogr. Clin. Neurophysiol., 107:428–433.

[Vidaurre et al., 2004] Vidaurre, C., Schlögl, A., Cabeza, R., and Pfurtscheller, G. (2004). About adaptive classiﬁers for brain computer interfaces. Biomed. Tech., 49(1):85–86.

[Wolpaw et al., 2002] Wolpaw, J. R., Birbaumer, N., McFarland, D. J., Pfurtscheller, G., and Vaughan, T. M. (2002). Brain-computer interfaces for communication and control. Clin. Neurophysiol., 113:767–791.

[Wolpaw and McFarland, 2004] Wolpaw, J. R. and McFarland, D. J. (2004). Control of a twodimensional movement signal by a noninvasive brain-computer interface in humans. Proc. Natl. Acad. Sci. USA, 101(51):17849–17854.

