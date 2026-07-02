IEEE TRANSACTIONS ON BIOMEDICAL ENGINEERING, VOL. 51, NO. 6, JUNE 2004 1081

BCI Competition 2003—Data Set IV: An Algorithm Based on CSSD and FDA for Classifying Single-Trial EEG

Yijun Wang*, Zhiguang Zhang, Yong Li, Xiaorong Gao, Shangkai Gao, Senior Member, IEEE, and Fusheng Yang

Abstract—This paper presents an algorithm for classifying single-trial electroencephalogram (EEG) during the preparation of self-paced tapping. It combines common spatial subspace decomposition with Fisher discriminant analysis to extract features from multichannel EEG. Three features are obtained based on Bereitschaftspotential and event-related desynchronization. Finally, a perceptron neural network is trained as the classifier. This algorithm was applied to the data set of “BCI Competition 2003” with a classification accuracy of 84% on the test set.

[Figure 1]

[Figure 2]

Index Terms—Brain-computer interface (BCI), common spatial subspace decomposition (CSSD), electroencephalogram (EEG), Fisher discriminant analysis (FDA).

I. INTRODUCTION

# I

N RECENT years, brain-computer interface (BCI) systems based on analysis of single-trial electroencephalogram

(EEG) associated with hand movements have developed rapidly. The physiological studies on movement-evoked potentials indicate that the spatio-temporal pattern of EEG differs between left and right hand movements. In the premovement period, Bereitschaftspotential (BP) can be recorded over the vertex region [1]–[3] and during the movement tasks, mu and beta rhythms are found to reveal event-related synchronization and desynchronization (ERS/ERD) over sensorimotor cortex [3]–[6].

G. Pfurtscheller et al. first used EEG classification based on ERS/ERD during hand movements for a BCI application [5]. B. Blankertz et al. designed a BCI system based on BP prior to voluntary finger movements with Fisher discriminant analysis (FDA) for classifier training, which reached % classification accuracy on a subject [1]. The technique of classifying single-trial EEG during finger movements has become an attractive topic in BCI research due to its advantages such as simple experimental approach, low rejection rate, high classification accuracy, short response time, and easy training for users.

[Figure 3]

[Figure 4]

[Figure 5]

Manuscript received June 29, 2003; revised January 16, 2004. This work was supported in part by the National Natural Science Foundation of China under Grant 60205003, in part by the National 863 Project of China under Grant 2001AA422310, and in part by the Chinese Ministry of Education under Key Project 1041185). Asterisk indicates corresponding author.

*Y. Wang is with the Department of Biomedical Engineering, Tsinghua University, Beijing 100084, China (e-mail: wyj97@mails.tsinghua.edu.cn).

Z. Zhang, Y. Li, X. Gao, S. Gao, and F. Yang are with the Department of Biomedical Engineering, Tsinghua University, Beijing 100084, China.

Digital Object Identifier 10.1109/TBME.2004.826697

In this paper, we propose an algorithm integrating both BP and ERD for classifying movement-evoked EEG during preparation of keystroke. It applies common spatial subspace decomposition (CSSD) to analyze the multichannel EEG signals for two tasks (left and right), and studies the characteristic distributions of BP and ERD in time, frequency, and space domains respectively. The algorithm was employed in off-line analysis of the data set self-paced 1s of “BCI Competition 2003.” These data are single-trial EEGs recorded during voluntary self-paced tapping [7].

II. METHODOLOGY A. Feature Consideration

1) Bereitschaftspotential (BP): Slowly decreasing potentials named movement-related cortical potentials (MRCPs) can be recorded before voluntary limb movements. BP is one of the main components of MRCPs, which can be recorded with the maximum amplitude over the vertex region.

Contralateral dominance is a significant character of BP. Fig. 1 shows the averaged trials of each channel and the spatial distribution of BP on the scalp at 140 ms and 320 ms before the key press. The declining waveforms of most channels reveal the decreasing nature of BP and the spatial distributions show the pronounced contralateral dominance. As shown in the images [Fig. 1(a)], BP of left finger movement is dominant over right vertex region and it is more obvious at the moment of 140 ms, which is closer to the actual keystroke, than at 320 ms. Moreover, even on the same channel, the responses of different tasks differ greatly in amplitudes. Thus, the remarkable difference of BP’s distributions between the two tasks can be taken as an important basis for classification.

[Figure 6]

[Figure 7]

2) Event-Related Desynchronization (ERD): ERD and ERS represent the changes of the ongoing EEG activity characterized by decrease or increase of power in the given frequency bands. For actual finger movements, ERD/ERS in mu and beta rhythms are obvious over somatosensory or motor cortex, also with contralateral dominance. Preparation of movement is typically accompanied by ERD in mu and beta rhythms. ERS in beta rhythm, considered as the rebound of ERD, occurs after movement.

In our study, the epoch before actual keystroke was analyzed to predict the upcoming task, so only the character of ERD is applicable. Fig. 2 displays the power spectrum on channels C3 and

0018-9294/04$20.00 © 2004 IEEE

[Figure 8]

- Fig. 1. Spatial distribution of BP at 320 ms and 140 ms before keystroke and averaged trials of the 28 channels corresponding to (a) left finger movements and (b) right finger movements. The amplitudes at the beginning of the epoch are normalized to zero.

[Figure 9]

- Fig. 2. Average power spectrum of EEG signals on channels C3 and C4 over motor cortex for the two tasks. Legend “—” stands for left finger movement and “- - -” stands for right finger movement.

The multichannel EEGs are denoted as matrices (left) and (right) with dimension of N (channels) by T (samples). They can be modeled using multiple simultaneously activated sources as follows:

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

where and are task-related source activities corresponding respectively to left and right hand movements, is the source corresponding to background activities that are common to both conditions. Assume that consists of sources and consists of sources, then and consist of and spatial patterns related with and respectively. A spatial pattern is an vector indicating the signal distribution over the N electrodes caused by a specific source. stands for the common spatial patterns related with

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

.

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

The aim of CSSD is to design spatial filters that lead to the estimations of and . This method is based on the simultaneous diagonalization of the spatial covariance matrices of and . Principal component analysis (PCA) and spatial subspace analysis are performed to eliminate the common components and extract the task-related components. More details of the algorithm can be found in [8]. As the result, two spatial filters, and , are constructed corresponding to the two tasks. The estimations of and are given by

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

C4 corresponding to both tasks. High-pass filtered EEG signals (cut off at 5 Hz) show difference in power distribution between the two tasks. For channel C3 [Fig. 2(a)], the power of mu and beta rhythms evoked by right hand movement is lower than that of left hand, which is consistent with the principle of contralateral dominance. Similar conclusion can be drawn from Fig. 2(b) for channel C4. The difference of power distribution derived from ERD implies another choice of feature for classification.

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

and , where is a single-trial EEG. It can be demonstrated that the specific temporal source activities estimated by CSSD are approximately the same as that in the spatio-temporal source model. Theoretically, for left finger movements, will be much stronger than and for right finger movements, the result is just the opposite.

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

## B. Feature Extraction

FDA can linearly project high dimensional data to onedimensional vector so as to facilitate the classification. It bears the advantages of easy implementation and low computational cost. A linear discriminant function is designed by use of FDA on the training set, which reduces the feature space to 1-D vector representing the proximity of the extracted feature belonging to either pattern.

The activities specific to the tasks (left or right finger movement) are usually overwhelmed by the spontaneous EEG and other nontask activities.Here, the method of CSSD is used to extract the task-related components and eliminate the background activities. Y. Wang et al. successfully used it to extract signal components specific to one task from multichannel EEG of multiple tasks [8].

[Figure 188]

- Fig. 3. Flow chart of classification algorithm, including the modules of temporal filtering, CSSD, feature extraction, electrodes selection, and perceptron neural network.

[Figure 189]

- Fig. 4. Averaged feature vector consisting of and , denoted as legends “o” and “*”. “—” and “- - -” are used to link the elements of corresponding to the two tasks respectively.

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

Fig. 3 shows the flow chart of the algorithm, which can be summarized as follows: three features are extracted from the single-trial EEG, then a perceptron is trained with the extracted features as input. Note that the data have been subsampled to 100 Hz in order to reduce the computational cost. After the decimation, 50 data points are retained for each trial. For convenience, index of sample point (1 to 50) will be utilized to describe the corresponding time ( 620 ms to 130 ms) infra. Our algorithm only deals with the frequency components in the range of 0 to 33 Hz, because the higher frequency components are less related with BP and ERD.

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

1) Extraction of Feature : The first feature is derived from BP, manifested as a declining slope of EEG with contralateral dominance. A zero-phase low-pass filter (0–7 Hz) is used to preprocess the data, and then a fixed time window (sample points of 44–47) is used to intercept the segment that bears the

[Figure 208]

[Figure 209]

most obvious difference between the two tasks. Then the new data with dimension of 28 (channels) by 4 (samples) will pass through and (with dimension of 1 28) corresponding to the most significant spatial patterns. Define an 8 1 feature vector as , where and . FDA projects to one dimension as

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

, where the weight and the bias are determined by the training set. As shown in Fig. 4, of left trials and of right trials have larger amplitudes than that of the contrary patterns, ensuring an effective classification with feature .

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

2) ExtractionofFeature : Thesecondfeature isderived from ERD. An analogous procedure is applied to the extraction of as that for . However, different parameters are employed due to the different physiological background of ERD and BP. The parameters that significantly influence the classification

[Figure 295]

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

- Fig. 5. (a) Averaged potential and two single trials on channel C4 of left finger movements. Legend “o” indicates the two features and . (b) Differences of all the 28 channels between left and right finger movements.

[Figure 300]

[Figure 301]

result include: passband of temporal filters, time window, number of spatial patterns selected for CSSD, and feature definition on the result of spatial filtering.

It has been mentioned that ERD also shows contralateral dominance though it appears on both hemispheres. A band-pass filter (10–33 Hz) and a time window (sample points of 19–50) are worked out to preprocess the data. As three most important spatial patterns are selected to construct the spatial filters, after spatial filtering, and with dimension of 1 32 are obtained. A 192 1 feature vector is then constructed by concatenating and , i.e.,

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

. Because a high dimensional feature vector is harmful to the stability of FDA, the dimension of is reduced to 24 1 by taking the averaged absolute value of its components consecutively for every eight elements. Absolute values are employed because they are just the parameters that reflect power magnitude. FDA with results in feature .

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

3) Extraction of Feature : Like feature , feature is also derived from BP. The same low-pass filter as that for extraction preprocessesthe signalsbeforethe comparison ofwaveforms of the two tasks. Fig. 5(b) illustrates the contrast of single trials on all the 28 channels by subtracting averaged from averaged . As shown in the figure, differences are less obvious on F3, F1, F4, FC5, FC3, C5, C3, CP5, and CP3 than the other channels, so these channels are rejected. Two features, and , are defined as the mean values of the beginning (sample points of 1–8) and ending (sample points of 41–50) portions of a single trial on one channel [see Fig. 5(a)]. Their difference is a good feature characterizing the declining trend of the waveform. All and of the remaining 19 channels are concatenated into a feature vector , leading to the feature by FDA.

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

## C. Classification

After extraction of the above three features, a perceptron, which is a fast and reliable neural network suited for simple classification problems, is used as the classifier. The

vector is fed as the input, and the output is

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

, where and are the weights and bias of the network determined by the training data. denotes the hard-limit transfer function, which returns 0 or 1 corresponding to left or right finger movements respectively.

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

III. RESULTS

The classification accuracy is % on the training set with the leave-one-out method. The accuracy on the test set is 84% ultimately. For comparison, similar algorithm is also applied to the data set of “BCI Competition 2002.” The accuracy is 98.23% due to the fact that BP is more prominent in this data set which greatly improves the effects of the features and .

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

The results demonstrate that the proposed algorithm is reasonable and effective for classifying single-trial EEG during self-paced tapping. High classification accuracy of the algorithm makes it a feasible choice for a practical BCI system.

IV. DISCUSSIONS

## A. Time Window and Frequency Window

The frequency window for temporal filtering and the time window for CSSD in the preprocessing stage should be considered carefully. The prior knowledge that BP appears in the lower frequencyband andERD occurs in mu and beta frequency bands can be utilized to make initial estimates of the parameters. In practice, a sliding window with adjustable bandwidth and cutoff frequency is used to find the appropriate frequency band. The optimal frequency band for BP is found to be 0–7 Hz and that for ERD is 10–33 Hz. The same approach is used to determine the time windows for CSSD and the results are sample points of 44–47 for BP and 19–50 for ERD. Fig. 6 shows the relationship between different time windows and classification accuracy when classifying with feature alone. Here the test is on the training set itself without use of leave-one-out method. The ending point is fixed at point 50, and the starting point leading to the highest accuracy is point 19.

[Figure 504]

[Figure 505]

- Fig. 6. Classification accuracy based on feature with different time windows. The ending point (P2) is 50 and the best starting point (P1) is 19.

[Figure 506]

TABLE I CLASSIFICATION ACCURACY CORRESPONDING TO SINGLE EIGENVALUE FOR SPATIAL FILTER DESIGN

[Figure 507]

## B. Spatial Filter Design

Proper selections of spatial patterns can markedly improve the classification accuracy. The accuracy may be degraded if insignificant spatial patterns are chosen. The selection of proper spatial patterns is determined by the magnitude of eigenvalues of the “whitening transformed” spatial covariance matrices of

and [8]. In principle, the eigenvectors corresponding to the several largest eigenvalues should be chosen. However, in our practice, they are chosen through comparing their contributions to classification accuracy. Each one of these eigenvectors is used individually to design the spatial filter. Features are extracted from the filtering results and classified by FDA. The significant eigenvectors are determined based on their relevant classification accuracy.

[Figure 508]

[Figure 509]

[Figure 510]

[Figure 511]

[Figure 512]

[Figure 513]

[Figure 514]

[Figure 515]

Table I shows the corresponding accuracy of the five largest eigenvalues ( to , in descending order) in the extractions of the features and . For feature , the accuracy of using is 82%, much higher than those of using other eigenvalues (around 50%). Therefore, the spatial filters for feature are worked out with only the largest eigenvalues. For feature , using , or

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

individually leads to an accuracy above 70%, so all the three eigenvalues are accepted to design the spatial filters.

[Figure 532]

[Figure 533]

ACKNOWLEDGMENT

The authors would like to thank B. Blankertz, K. R. Müller, and G. Curio for providing the data.

REFERENCES

- [1] B. Blankertz, G. Curio, and K. R. Müller, “Classifying single trial EEG: Toward brain computer interfacing,” in Advances in Neural Information Processing Systems (NIPS01), T. G.Diettrich, S.Becker,and Z. Ghahramani, Eds. Cambridge, MA, 2002, vol. 14, pp. 157–164.
- [2] M. Kukleta and M. Lamarche, “Steep early negative slopes can be demonstrated in pre-movement bereitschaftspotential,” Clin. Neurophysiol., vol. 112, pp. 1642–1649, 2001.
- [3] J. A. Pineda, B. Z. Allison, and A. Vankov, “The effects of self-movement, observation, and imagination on mu rhythms and readiness potentials (RP’s): Toward a brain-computer interface (BCI),” IEEE Trans. Rehab. Eng., vol. 8, pp. 219–222, June 2000.
- [4] G. Pfurtscheller and F. H. Lopes da Silva, “Event-related EEG/MEG synchronization and desynchronization: Basic principles,” Clin. Neurophysiol., vol. 110, pp. 1842–1857, 1999.
- [5] G. Pfurtscheller, J. Kalcher, C. Neuper, D. Flotzinger, and M. Pregenzer, “On-line EEG classification during externally-paced hand movements using a neural network-based classifier,” Electroenceph. Clin. Neurophysiol., vol. 99, pp. 416–425, 1996.
- [6] J. Müller-Gerking, G. Pfurtscheller, and H. Flyvbjerg, “Classification of movement-related EEG in a memorized delay task experiment,” Clin. Neurophysiol., vol. 8, pp. 1353–1365, 2000.
- [7] B. Blankertz, K. R. Müller, G. Curio, T. M. Vaughan, G. Schalk, J. R. Wolpaw, A. Schloegl, C. Neuper, G. Pfurtscheller, T. Hinterberger, M. Schroeder, and N. Birbaumer, “The BCI competition 2003: Progress and perspectives in detection and Discrimination of EEG single trials,” IEEE Trans. Biomed. Eng., vol. 51, pp. 1044–1051, June 2004.
- [8] Y. Wang, P. Berg, and M. Scherg, “Common spatial subspace decomposition applied to analysis of brain responses under multiple task conditions: A simulation study,” Clin. Neurophysiol., vol. 110, pp. 604–614, 1999.

[Figure 534]

Yijun Wang was born in Fukien, China, in 1979. He received the B.E. degree in biomedical engineering from Tsinghua University, Beijing, China, in 2001. He is currently working towards the M.E. degree in the Department of Biomedical Engineering, Tsinghua University.

His research interests are brain-computer interface and biomedical signal processing.

Xiaorong Gao was born in Beijing, China, in 1963. He received the B.S. degree in biomedical engineering from Zhejiang University Hangzhou, China, in 1986, the M.S. degree in biomedical engineering from Peking Union Medical College, Peking, China, in 1989, and the Ph.D. degree in biomedical engineering from Tsinghua University, Beijing, China, in 1992.

[Figure 535]

He has been with the Department of Electrical Engineering, Tsinghua University since 1992. His current research interests are in biomedical signal

processing and medical instrumentation.

[Figure 536]

Zhiguang Zhang graduated from the Department of Precision Instruments and Mechanology, Tsinghua University, Beijing, China, in 1970.

He is currently an Associate Professor with the Department of Biomedical Engineering, Tsinghua University. His research interests include biomedical image and signal processing, pattern recognition.

[Figure 537]

Shangkai Gao (SM’94) graduated from the Department of electrical engineering of Tsinghua University, Beijing, China, in 1970, and received the M.E. degree of biomedical engineering in 1982 in same department.

She is currently a Professor with the Department of Biomedical Engineering, Tsinghua University. Her research interests include biomedical signal processing and medical ultrasound.

Prof. Gao is now an Associate Editor of IEEE TRANSACTION ON BIOMEDICAL ENGINEERING.

[Figure 538]

Yong Li was born in Hunan, China, in 1976. He received the B.E. degree and Ph.D. degree in biomedical engineering from Tsinghua University, Beijing, China, in 1998 and 2003, respectively.

His research interests include biomedical signal processing and medical ultrasound.

Fusheng Yang received the B.Sc. degree of electrical engineering from AmoyUniversity, Fukien, China, in 1949.

[Figure 539]

Since 1951, he has been a faculty member ithe the Department of Electrical Engineering, Tsinghua University, Beijing, China, where he has been Professor since 1980. He is the author of Biomedical Signal Processing (Beijing, China: Higher Education Press, 1989) and Engineering Analysis of Wavelet Transform and its Application (Beijing, China: Science Press, 1998). His current research interest

lies mainly in the application of spatial analysis, time-frequency, time-scale analysis and nonlinear dynamics analysis to biomedical signals.

