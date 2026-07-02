# Predicting BCI Subject Performance Using Probabilistic Spatio-Temporal Filters

Heung-Il Suk1, Siamac Fazli1, Jan Mehnert2, Klaus-Robert Mu¨ller1,2*, Seong-Whan Lee1*

1 Department of Brain and Cognitive Engineering, Korea University, Anam-dong, Seongbuk-ku, Seoul, Republic of Korea, 2Machine Learning Group, TU Berlin, Berlin, Germany

|Abstract<br><br>Recently, spatio-temporal filtering to enhance decoding for Brain-Computer-Interfacing (BCI) has become increasingly popular. In this work, we discuss a novel, fully Bayesian–and thereby probabilistic–framework, called Bayesian SpatioSpectral Filter Optimization (BSSFO) and apply it to a large data set of 80 non-invasive EEG-based BCI experiments. Across the full frequency range, the BSSFO framework allows to analyze which spatio-spectral parameters are common and which ones differ across the subject population. As expected, large variability of brain rhythms is observed between subjects. We have clustered subjects according to similarities in their corresponding spectral characteristics from the BSSFO model, which is found to reflect their BCI performances well. In BCI, a considerable percentage of subjects is unable to use a BCI for communication, due to their missing ability to modulate their brain rhythms–a phenomenon sometimes denoted as BCIilliteracy or inability. Predicting individual subjects’ performance preceding the actual, time-consuming BCI-experiment enhances the usage of BCIs, e.g., by detecting users with BCI inability. This work additionally contributes by using the novel BSSFO method to predict the BCI-performance using only 2 minutes and 3 channels of resting-state EEG data recorded before the actual BCI-experiment. Specifically, by grouping the individual frequency characteristics we have nicely classified them into the subject ‘prototypes’ (like m - or b -rhythm type subjects) or users without ability to communicate with a BCI, and then by further building a linear regression model based on the grouping we could predict subjects’ performance with the maximum correlation coefficient of 0.581 with the performance later seen in the actual BCI session.<br><br>Citation: Suk H-I, Fazli S, Mehnert J, Mu¨ller K-R, Lee S-W (2014) Predicting BCI Subject Performance Using Probabilistic Spatio-Temporal Filters. PLoS ONE 9(2): e87056. doi:10.1371/journal.pone.0087056<br><br>Editor: Wang Zhan, University of Maryland, College Park, United States of America Received November 6, 2013; Accepted December 17, 2013; Published February 14, 2014 Copyright: 2014 Suk et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. Funding: This work was supported by the National Research Foundation funded by the Ministry of Science, ICT and Future Planning, under grant 2012-005741. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. Competing Interests: The authors have declared that no competing interests exist.<br><br>* E-mail: klaus-robert.mueller@tu-berlin.de; swlee@image.korea.ac.kr|
|---|

Introduction

Classical Brain Computer Interfaces (BCIs) were based on operant conditioning [1,2,3,4,5], i.e., the subject had to adapt the modulation of his/her brain rhythms. In recent years with the advent of machine learning methods in BCI, both - the subject and the computer - adapt; this has resulted in a reduction of calibration times and increased information transfer rates [6,7,8,9,10,11,12]. Machine-learning can help accurately model the spatio-temporal characteristics of a subject’s brain rhythms to ensure optimal decoding of the user’s intentions during feedback. For Sensory Motor Rhythms (SMR), Common Spatial Pattern (CSP) [13] and its variants are most commonly used [14,15,16,17,18,19].

Within the last decade the performance in non-invasive EEGbased BCI has reached high levels of accuracy (up to 90%) in classifying EEGs into one of the predefined labels, e.g., left-hand vs. right-hand motor imagery, nevertheless around 20% of the subjects show an inability to communicate with a BCI – sometimes also called BCI-illiteracy/inability [20,21,22,23]. The reasons for BCI-inability are still under debate, however, for SMR-controlled BCIs, strong rhythms during resting state are found highly predictive for a later good online BCI performance [20]. Nevertheless, which frequencies will be most discriminative, depends on the individual subject physiology. The most common modulated frequency band used by a SMR-controlled BCI is the

m-rhythm around 10 Hz; a second target frequency band is the bband around 20 Hz. Although most subjects modulate one or both of these frequency bands, they always show specific peakfrequencies while subjects with BCI-inability typically do not show any task-related modulation in these bands [20]. It is important to note that so far, SMR-controlled BCIs have been trained on one or two frequency bands only, the detailed spectrum was not considered until recently, where the first fully Bayesian approach has been introduced to the field: Bayesian SpatioSpectral Filter Optimization (BSSFO) [24]. BSSFO allows to introduce prior knowledge into spatio-temporal filter optimization. It extracts a subject-specific filter distribution that can be analysed to gain a better understanding of individual differences of BCI users.

In this contribution, we will show that BSSFO not only yields a significant increase in classification accuracy over 80 subjects when compared to other spatio-temporal filter algorithms. But BSSFO filters may further be clustered across subjects according to the patterns corresponding to the extracted filter characteristics. We then analyze the resulting grouping in order to gain a better physiological understanding why some subjects perform better than others and what the characteristics of subjects with BCIinability could be.

Our analysis extends [20], since we find an increased predictivity when using the full spectral characteristics of resting-state EEG

measurements prior to the BCI. We further study the dependency of the prediction quality on the number of channels included. It should be noted that our analysis aims to get additional physiological insight to the phenomenon of BCI-inability; other protocols that involve e.g., co-adaptive BCI [25,26,12,27] can indeed help enable illiterates to communicate with BCI.

Methods

In this section, we first describe the experimental data sets used to test the proposed fully Bayesian approach 1) for BCI classification and 2) for the prediction of subjects’ individual performance. We leave the mathematical background of the Bayesian framework to Appendix, in particular and how it constructs individual spatial and temporal filters used for the BCI classification. The proposed framework is compared to four competing methods. Furthermore, clustering of the derived patterns allows a physiological interpretation of the results. For the second aim of the study, i.e., the prediction of the subjects’ performance, we formulate an application of the Bayesian framework for resting-state EEG data. In combination with a clustering of the derived spatio-temporal patterns, it enables us to analyze the predictability of these patterns for the subjects’ performance during the actual BCI and a physiological interpretation. In Fig. 1, we present flowcharts that outline the steps in data processing for each study, respectively. The detailed explanation for the steps is described below.

- 2.1 EEG Acquisition and Preprocessing The EEG data used to evaluate the BSSFO algorithm has been

acquired during a SMR-controlled BCI in a previous study [23], where 83 subjects performed motor imagery of three classes: Lefthand motor imagery (L), Right-hand motor imagery (R), and Foot motor imagery (F) to control a BCI. (The study was approved by

the Ethical Review Board of the Medical Faculty, University of Tu¨bingen. Each subject gave a written informed consent after having been informed about the purpose of the study.) Due to technical problems during the acquisition, 3 participants were excluded from the analysis. Subjects were seated in a comfortable chair and instructed to relax their arms, while these were lying on armrests. The recording was carried out with multichannel EEG amplifiers (BrainAmp DC by Brain Products, Munich, Germany) with 119 Ag/Ag/Cl electrodes and a nasion reference, and sampled at 1000 Hz with a band-pass of 0.05 Hz to 200 Hz. Vertical as well as horizontal ElectroOculoGram (EOG) and ElectroMyoGram (EMG) at both forearms and right leg were recorded, to ensure absence of artifacts within the EEG.

To test BFSSO for BCI in an off-line analysis (as described in Section 2.2), we only used data from motor imagery of the left and right hand recorded during three calibration sessions acquired during the described experiment, each consisting of 25 trials per class per subject, resulting in a total of 75 trials per class per subject. A single trial lasted for 8 seconds. At the beginning of each trial a crosshair appeared at the center of the screen for two seconds. After this initial 2 seconds, one of three possible visual cues in the form of an arrow pointing to the left, right, or downwards showed up for 4 seconds in a randomized order. The visual cues indicated the type of movement imagination to be performed by the participant. After the arrow disappeared, the screen was left blank for 2 seconds and then a new trial began. After every 20 trials a short 15-second break was given. The EEG data was downsampled to 100 Hz with a digital Chebyshev lowpass filter. Two sets of channels were defined and used for further analysis: a set of 39 LAPlacian (LAP)-filtered channels (Fig. 2(a)) and a second set of 16 LAP-filtered motor-related channels (Fig. 2(b)).

The study of Blankertz et al. further contained resting-state periods at the beginning of each of the 3 calibration sessions. In

[Figure 1]

[Figure 2]

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

- Figure 1. Flowcharts of the proposed method for BCI classification and BCI performance prediction, respectively.

- doi:10.1371/journal.pone.0087056.g001

- Figure 2. Electrode montages.

- doi:10.1371/journal.pone.0087056.g002

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

Figure 3. An illustration of estimating p(BDX,V) that represents how likely the EEGs X is correctly classified into the corresponding label V for each of the frequency bands in B.

- doi:10.1371/journal.pone.0087056.g003

total, 10 periods of 15 seconds were recorded with the alternating tasks ‘relax with eyes open’ and ‘relax with eyes closed’. We pooled this resting-state data and used it to train BSSFO to predict the subjects’ BCI performance (see Section 2.3). We consider two channel arrangement schemes, namely, small channel arrangement (3-LAP: ‘C3’, ‘Cz’, ‘C4’.), large channel arrangement (16LAP: the same channels used for the motor imagery experiment). For further details on the experimental and recording setup, please refer to [20].

2.2 Bayesian Spatio-spectral Filter Optimization for Decoding in Brain Computer Interfaces

A schematic overview of the BSSFO method (see Appendix and [24]) is given in Fig. 3. Given a set of the preprocessed motor imagery EEG signals and a set of particles - each representing a specific frequency band sampled from a prior distribution - the BSSFO algorithm first filters the EEG signals for each frequency band. All the ensuing processes are based on information from this individual particle. The spectral filtering is followed by a spatial

[Figure 761]

- Figure 4. Estimation of a 1-dimensional pdffrom a 2-dimensional pdfestimated by BSSFO. (Left) A 2-dimensional pdf estimated by BSSFO. (Middle) The red line represents the 1-dimensional pdf of the estimated 2-dimensional pdf and the blue straight line is the 1-dimensional pdf of a uniform 2-dimensional pdf. (Right) The red line is the uniform pdf subtracted version of the 1-dimensional pdf.

- doi:10.1371/journal.pone.0087056.g004

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

Figure 5. A schematic diagram of the BCI illiteracy prediction in a probabilistic framework.

- doi:10.1371/journal.pone.0087056.g005

filtering, where a CSP is trained with the spectrally-filtered signals. The likelihood and the posterior pdf are then estimated on feature vectors extracted from the resulting filtered signals. This whole process is iterated until convergence or a predefined stopping criterion. We estimated class-discriminative pdfs for several frequency bands between 4 Hz and 40 Hz with an interval of 0.5 Hz. The result is then a 2 dimensional pdf, in which each dimension corresponds to a start and an end frequency, respectively (see e.g., Fig. 4).

We applied the described process on experimental SMRcontrolled BCI data and compared two channel configurations, already described in Section 2.1 to extract spatio-temporal filters for the BCI classification. The classification followed the same strategy as proposed by [24] except for the classifier. In the present study, we employed a Linear Discriminant Analysis (LDA) for classification. The resulting accuracies are compared with the the conventional CSP [16] on different band-pass filtering strategies. For the competing method, we also used a LDA as a classifier.

2.2.1 Towards physiological interpretation of results from BSSFO. To enable a physiological understanding of the patterns resulting from BSSFO, we converted the estimated 2dimensional pdfs into 1-dimensional pdfs as follows:

gM(s)~ X

M(s,e){ X

U(s,e) ð1Þ

es:t:ews

es:t:ews

where M(s,e) and U(s,e) denote, respectively, the estimated 2dimensional pdf and a uniform 2-dimensional pdf, and s and e are, respectively, the start and the end frequency for a band (see Fig. 4). The estimated 1-dimensional pdf is then weighted with a neurophysiological knowledge, represented by a mixture of

- 1
- 2

- 1
- 2

N f ;b,s2b , where f denotes a frequency. This final 1-dimensional pdf is used as input for a hierarchical clustering over all subjects. For each cluster, we derived a topographical map representing the average spatial

N f ;m,s2m z

Gaussians as v(f )~

patterns of the subjects belonging to the cluster. In addition to the clustering, we also computed the Pearson correlation between the Area Under the Curve (AUC) of the 1-dimensional pdf and the classification accuracy for each subject.

2.3 Prediction of BCI Performance from Resting-state Data

The second aim of our study is to find spatio-temporal patterns in resting-state EEG data, which are predictive for the individuals BCI performance and, furthermore, allows to sort subjects along their frequency-type, i.e., m - and/or b-rhythm types, and ‘BCIilliterates’. The basic principle follows the one described above: We first estimate a frequency pdf from a Power Spectral Density (PSD) of channels for each subject in an unsupervised manner (Section 2.3.1). A data clustering over the estimated pdf follows and finally we build a linear regression model using the cluster information (Section 2.3.2). A schematic diagram of building our BCI predictor is presented in Fig. 5.

2.3.1 Unsupervised pdf estimation. In order to estimate a pdf of a frequency band, we first calculated the PSD in each channel individually with the preprocessed resting-state EEGs as follows:

p ðT 0

1

XE(t)exp({ivt)dt ð2Þ

PE~

ﬃﬃﬃﬃT

where t denotes a time index, E denotes an electrode, and XE is a temporal EEG at the electrode E. For each PSD, the corresponding noise model is fitted as done in [20]:

k2 f l ð3Þ

NE~k1z

where f denotes a frequency, and k1, k2, and l are model parameters.

[Figure 1054]

[Figure 1055]

[Figure 1056]

[Figure 1057]

[Figure 1058]

[Figure 1059]

- Figure 6. Estimation of the frequency-related resting-state EEG pdfwith 3-LAP channels. In (c) and (d), the ‘Transformed’ pdfs are the uniform pdf subtracted version of the respective 1D-PDFs.

- doi:10.1371/journal.pone.0087056.g006

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

Figure 7. An example of constructing a cluster-distance vector for a subject i , which is the input to the linear regression function in BCI-performance prediction. The colored ovals represent a rough distribution of feature vectors labeled to the clusters and the dots represent the mean of each cluster.

- doi:10.1371/journal.pone.0087056.g007

Based on those two ingredients, we extract the Frequency-

Related Information (FRI) SE for each channel by taking the difference between a PSD and a noise model.

SE~PE{NE: ð4Þ

From an information theory point of view, Eq. (4) means that

the smaller the value of SE, the less informative the frequency in the channel E is. This fact is utilized directly in our probability model described below.

Since the selection of a frequency band related to motor imagery tasks is one of the key issues in determining the classification performance, we build a pdf in terms of a frequency band. Following Suk et al.’s work [24], we represent a frequency band with a continuous random vector B. The problem is to

estimate the pdf of this random variable B~½bsbe {, where bs and be denote, respectively, the start and the end point of a frequency band, and { is a transpose operator.

We should note that given a set of preprocessed resting-state EEGs X, the posterior probability of a frequency band B, p(BDX), can be estimated indirectly from the set of FRIs S~fSEgNE~1, where N denotes the number of channels under consideration, as follows:

Table 1. Comparison of the classification performance error among the competing methods for motor imagery.

Band [Hz] 16 Channels [%] 39 Channels [%]

Broad-band (5–3) 27.65615.53 27.14615.92 m-band (8–12) 28.31615.65 29.82614.27 b-band (16–22) 39.09612.51 38.45612.56 Heuristic [12] 26.12615.89 26.33614.61 BSSFO [32] 24.88±15.62 26.07615.27

doi:10.1371/journal.pone.0087056.t001

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

- Figure 8. Results of the hierarchical clustering on 1D pdfsof the subjects on motor imagery tasks. The topographies present an average of the trained spatial patterns of the subjects belonging to the same cluster.

- doi:10.1371/journal.pone.0087056.g008

p(BDX)~p(BDS): ð5Þ

Taking into account channels, we can rewrite p(BDS) by a sum rule in a probability theory and a Bayes rule as follows:

p(BDS)~X

p(B,EDS)

E

p(SDB,E)p(BDE)p(E) p(S)

~X

E

!X

p(SDB,E): ð6Þ

E

With the application of a chain rule and the assumption of the uniform distributions for p(BDE) and p(E), the last proportional relation can be derived.

From Eq. (6), all we need to do is to estimate the likelihood p(SDB,E). We define a likelihood for a frequency band B of the

range bs and be as follows:

exp½SE(B) W(B) ð7Þ

p(SDB,E)~

Ðbe bs SE and W(B) denotes a bandwidth.

where SE(B)~

At this moment, we should note that due to a computational issue, in this work, the PSDs and the corresponding noise models are computed and fitted every 0.5 Hz between 2 and 34 Hz, which covers both m (8–12 Hz) and b (16–22 Hz) rhythms. Therefore, the domain for a start frequency is bs[f2,2:5,3, ,33:5g and that for an end frequency is be[f2:5,3,3:5, ,34g.

Let L(s,e) be the likelihood for the frequency band of bs and be estimated from the resting-state EEGs, where s and e are, respectively, an index of the frequency value. The likelihood is computed by Eq. (7). Fig. 6(a) and Fig. 6(b) illustrate the examples of likelihood of three different electrodes for two different subjects. From the figures, we can see that a high power spectrum results in a high likelihood. From the likelihood we can naturally compute a pdf R(s,e) by normalization as follows:

[Figure 1347]

[Figure 1348]

[Figure 1349]

- Figure 9. Illustration of the common spatial patterns of the subjects belonging to each cluster from Fig. 8. The results were obtained from the 16-LAP channel arrangement (see online color version of the figure).

- doi:10.1371/journal.pone.0087056.g009

[Figure 1350]

- Figure 10. Pearson correlation of the frequency weighted area under curve (AUC) of 1D pdf with BCI performance. Each dot corresponds to a subject. The color of dots represents a cluster label in Fig. 8. The two lines represent a linear regression function for the values; the red solid line (correlation 1) is fitted to all the values considered and the black dotted line (correlation 2) is fitted for the values with outliers excluded.

- doi:10.1371/journal.pone.0087056.g010

[Figure 1351]

[Figure 1352]

Figure 11. Global mean and a standard error of the resting-state EEGpdfsover all subjects for two channel configurations: 3 and 16 Laplacian EEG-channels. See Section 2.1 for a description of the difference between both.

- doi:10.1371/journal.pone.0087056.g011

L(s,e) P

: ð8Þ

R(s,e)~

P

j L(i,j)

i

It is noteworthy that the probability represents the relative importance of a frequency band in a subject.

Although we can compute the probability of a frequency band from resting-state EEGs following the steps mentioned above, we cannot directly quantify the significance of the specific frequency band in terms of SMR-controlled BCI prediction, since the

learning problem is now an unsupervised one. We, therefore, compute the likelihood for a noise model and contrast it to the likelihood from resting-state EEGs. In Eq. (7), SE(B) is defined as the difference between a PSD and the corresponding noise model. That is, the likelihood for a noise model becomes uniform U(s,e) over all frequency bands. Then we can convert the 2D pdf into a 1D pdf gR(s) as done in motor imagery tasks:

gR(s)~ X

R(s,e){ X

U(s,e) ð9Þ

es:t:ews

es:t:ews

where the indices s and e denote, respectively, a start and an end point of a frequency band.

However, once we convert a likelihood into a probability distribution, the original spectral power information disappears. Consequently, the probability distribution of different likelihoods can become similar between subjects even though their likelihoods are very different as exemplified in the leftmost matrix of Fig. 6(c) and Fig. 6(d). That is, while the likelihood of three electrodes for the two subjects are different from each other as shown in Fig. 6(a) and Fig. 6(b), after normalization of the probability density, the difference disappears. The probability represents the relative differences among values within a subject. Therefore, it is not meaningful to directly compare them between subjects for SMRcontrolled BCI performance prediction. Therefore, to reflect the individual information of the PSD into the pdf, we multiply with a weight g, which we call a ‘subject-weight’, defined as the sum of the maximum power of each channel as follows:

g~X

maxSE: ð10Þ

E

With the introduction of the subject-weight into the pdf, we can get a spectral power reflected density as shown at the rightmost matrix in Fig. 6(c) and Fig. 6(d). Note that after multiplication of the subject-weight, the resulting pdf does not meet the probability property anymore, i.e., the sum of the values is not one. From the figures, we can clearly see the density differences between subjects while still keeping the relative significance of frequency within a subject. In addition, we also reflect the prior neurophysiological knowledge that m - and b -rhythms are helpful for SMR-controlled BCI illiteracy prediction as proved in Blankertz et al.’s work [20].

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

- Figure 12. An example of a clustering result obtained by BSSFO from the resting-state EEG. (a,b) show hierarchical clustering results for a small (3) and large (16) channel configuration. For the same channel configurations, we show the corresponding cluster-wise linear regression models (c,d) between the BSSFO’s pdfs and the classification accuracy in the actual BCI. The BSSFO combines the cluster-wise linear regression models in performance prediction.

- doi:10.1371/journal.pone.0087056.g012

Therefore, the pdf J, which will be used for prediction, can be obtained as follows:

J~g|X

gR(f )v(f ) ð11Þ

f

where g denotes a subject-weight in Eq. (10) and v(f )~

- 1
- 2

- 1
- 2

N f ;b,s2b is a frequency-weight borrowed from the neurophysiological knowledge on motor imagery. that the spectral features with regard to the motor imagery are highly variable across subjects and a similar phenomenon can be observed in resting-state EEGs. We assume that if the spectral features of the resting-state among subjects are similar to each other, then their SMR-controlled BCI performance would be also similar. Therefore, we combine a clustering method with a linear regression method, but another possibility would be the use of a mixed effects model similar to [28]. For constructing the predictor, we first cluster the subjects based on their spectral feature vectors, and then learn a linear regression model based on the distance from the center of each cluster and the feature vectors. In this paper, we apply a hierarchical clustering method [29].

N f ;m,s2m z

- 2.3.2 Cluster-based linear regression. It is well-known

½ ,gi {, gi is a spectral pdf of the subject i, AJ

We utilize an augmented feature vector v(i)~ gi,AJ

i

and gi are, respectively, an AUC of Ji and a weight of the subject i. Due to the high dimension of the augmented vector and a small number of samples compared to the dimension, a principal component analysis technique is applied to

i

reduce the dimension. We use the dimension-reduced feature vectors v(i) that include the information available from restingstate EEGs for clustering and the SMR-controlled BCI performance prediction.

In a hierarchical clustering, we use a ward criterion, which chooses the pair of clusters to merge at each step based on the optimal value of an objective function, i.e., squared Euclidean distance:

D(i,j)~DD^v(i){^v(j)DD2 ð12Þ

where ^v(i) and ^v(j) denote the dimension-reduced augmented feature vectors of the subject i and j, respectively. Since the hierarchical clustering method builds a hierarchy of clusters, it allows us to investigate the results from a physiological perspective.

In order for linear regression model fitting, we construct a new

vector di for each subject i, which consists of the distances from the center of clusters.

di~½di(1) di(k) di(K) { ð13Þ

where di(k)~DD^v(i){c(k)DD2, c(k) denotes the center of the cluster k, and K is the number of clusters. Fig. 7 illustrates the construction of a cluster distance vector. In the figure, each oval represents a rough distribution of the feature vectors ^v labeled to the respective cluster, and colors denote cluster labels. The dots in the center of

[Figure 1365]

[Figure 1366]

[Figure 1367]

[Figure 1368]

[Figure 1369]

[Figure 1370]

- Figure 13. 3-LAP-channel resting-state EEG pdfsassigned to each cluster and the corresponding two-largest Principal Components (PCs). The colors denote cluster labels from Fig. 12(a).

- doi:10.1371/journal.pone.0087056.g013

[Figure 1371]

[Figure 1372]

[Figure 1373]

[Figure 1374]

[Figure 1375]

[Figure 1376]

- Figure 14. 16-LAP-channel resting-state EEG pdfs assigned to each cluster and the corresponding two-largest Principal Components (PCs). The colors denote cluster labels from Fig. 12(b).

- doi:10.1371/journal.pone.0087056.g014

each oval are the mean of the feature vectors assigned to the cluster.

With the cluster distance vectors D~½d1, ,di, ,dn [RK|n, where n is the total number of subjects for training, we fit a linear regression model.

Y~D{wze ð14Þ

where Y~½y1 yi yn { is a concatenated vector of the motor imagery accuracies over subjects, and w and e are, respectively, a regression parameter and a bias.

Given a new subject’s EEG signal x^, the SMR-controlled BCI performance for the subject can be predicted by.

^y~dxwze ð15Þ

where dx^ and ^y denote, respectively, a vector of distances between the dimension-reduced feature vector of the new subject and the center of clusters, and the predicted SMR-controlled BCI performance.

We used the same clustering method on the pdfs of the restingstate EEG data derived from Section 2.3 for a small and a large

[Figure 1377]

- Figure 15. The changes of the correlation between the proposed predictor and the classification performance according to the number of clusters and the number of channels considered in prediction.

- doi:10.1371/journal.pone.0087056.g015

[Figure 1378]

[Figure 1379]

Figure 16. Mean and standard error of resting state EEG pdfsover the subjects assigned to each cluster of motor imagery pdfs. The cluster labels denoted with different colors are from Fig. 10.

- doi:10.1371/journal.pone.0087056.g016

channel arrangement (see Section 2.1) to test whether also a small number of channels can lead to meaningful results. We then calculated a cluster-wise regression of the pdfs AUC and the subject’s performance in the later actual BCI session from Section

- 2.2, which gives insight whether belonging to a cluster can predict the BCI performance.

To gain further insight into the physiological features derived from the clustering, we calculated the first two principal components within the subjects belonging to each cluster. These principal components show the frequency pattern most common within a cluster. This was also done for small and large number of EEG channels to check whether a small number of channels still reveals meaningful results.

To find an appropriate number of clusters, we calculated the correlation between the resting-state predictor given by the clustering method and the actual BCI performance of the subject. We tested this for up to 20 clusters and for different channel arrangements.

Finally, we compared the clusters derived from the analysis of the actual BCI paradigm with the pdfs gained from the restingstate EEG data, in other words the discriminative and generative settings. As the clustering within the motor imagery sorted the subjects according to their performance, we are hereby able to show whether the resting-state pdfs show physiological meaningful predictor for the BCI performance.

Results

3.1 Motor Imagery Classification and Physiological Interpretation of BSSFO Results

First, BSSFO is evaluated off-line for a large BCI data corpus of 80 subjects from [20]. (We performed 8-fold chronological crossvalidation. In chronological cross-validation, since the time structure of the data is largely preserved, it can thus be considered as a relatively conservative measure. All parameters for temporal and spatial filters were estimated from training data in each of the cross-validation splits and applied to the test data. Regarding a loss function, 0–1 loss was applied.) BSSFO compares favorably to CSP with various strategies of band-power estimation (see Table 1). The band-pass filter strategies considered in this work were namely a broad-band filter (5–30 Hz), an m-band filter (8–12 Hz), a b-band filter (16–22 Hz), and they were combined with CSP [16]. We also considered an established heuristic method for optimizing subject-dependent temporal filters [16]. Specifically, the log band-power of LAP-filtered EEG channels were computed from 5 to 35 Hz. Then the correlation coefficient of the bandpower and the labels were calculated across all trials. We determine the frequency (fmax) with the highest correlation coefficient. Based on this frequency, the band-pass frequency interval ½f0,f1 was increased, starting at fmax until f0 and f1 were smaller or equal to 5% of fmax.

In order to gain a physiological interpretation of these encouraging results, a hierarchical clustering based on the 1 dimensional pdf s that are derived from the BSSFO’s 2 dimensional pdf of all subjects is computed. The resulting clustering into 3 groups is shown in Fig. 8 including an average of the 1D pdfs of the subjects belonging to one cluster shown as a topographical map. The first cluster (red) (Fig. 8, left hand side) has a very clear pattern with a strong lateralization between left- and right-hand motor imagery, which is also stable in the subgroups of this cluster. The pattern of the second cluster (green) (Fig. 8, middle) is less strongly lateralized and more occipital channels appear modulated only during right-hand imagery. They are contaminated by strong arhythms in the occipital cortex, which shares the frequency range of the m-rhythm that we are actually interested in. Also subjects that belong to the second cluster show an overall smaller modulation than the one of the first cluster. The third cluster (blue) (Fig. 8, right hand side) exhibits considerable within-clustervariance. This is already a first hint that a lower classification accuracy could be expected for the third group when compared to the others.

To further investigate inter- and intra-cluster differences, we computed the mean spatial patterns of the 3 clusters. The results for each subject are shown in Fig. 9. Here, we gain a similar result as already mentioned above: Within the first cluster, we see a strong lateralization among nearly all subjects. This lateralization

weakens in the second cluster and only exists among a few subjects of the third cluster.

We further computed Pearson’s correlation between the AUC of the 1 dimensional pdf and the classification accuracy. As shown in Fig. 10, the results are promising with a clear correlation between them: 0.769 with 16-LAP channels. If we remove outliers, the correlation increases to 0.860. From the figure, we can see that the clusters are also highly correlated with the accuracy. The subjects belonging to the red cluster mostly represent a high classification accuracy. Whereas, the subjects belonging to the blue cluster are distributed on the left-low corner of the graph indicating a low accuracy. The subjects in the green cluster are in the middle.

- 3.2 Prediction of BCI Performance with Resting-state EEG A second aim of our study is to evaluate whether BSSFO is

capable of predicting subjects’ BCI performance using resting-state EEG data preceding an actual BCI paradigm. Using the 1D pdfs of the same preprocessed resting-state EEG data (see Section 2.3), we study the dependence on the number of channels necessary for a meaningful clustering and whether the derived groups have physiologically reliable spatial and temporal features allowing for a typecasting of the subjects. Fig. 11 shows a grand mean and its standard error of the resting state pdfs for two different channel arrangements (3-LAP and 16-LAP).

Although the scale is different between Fig. 10 and Fig. 10, the global shapes are similar between the small and large channel arrangement. Both present a global peak around the m-band and the second largest global peak around the b-band (in line with [20]).

In Fig. 12, we illustrate the clustering results and the linear regression functions fitted to the data of each cluster. Fig. 12(a) and Fig. 12(b) show the results of the hierarchical clustering method with 3-LAP and 16-LAP channel arrangements, respectively. We selected 5 clusters for both small and large channel arrangements. The linear regression models for each cluster are given in Fig. 12(c) and Fig. 12(d).

For both channel arrangements, we can identify 2–3 high performing groups, one containing only small number of subjects. At least one cluster contains subjects with mixed performances although the predictor obtained from the resting-state EEG data has similar AUCs. Neither in the large nor the small channel arrangement a clear group of users unable of BCI communication appears. Also a small channel arrangement does not lead to significantly worse results, which is encouraging from the practical point of view.

A close look into the cluster-wise spectral properties is given in Fig. 13 for the small channel arrangement. Here, we display each subject’s pdf assigned to each cluster as well as their principal components of the two largest eigenvalues. Considering the spectral features within each cluster for the 3-LAP channel arrangement, it can be stated that cluster 3 and 4 show clear peaks around the m-band within each of the subject. While cluster 1 consists of subjects having either a high m-, a high b-band or both, cluster 2 and 5 contain subjects with either no or only slight mbands. Nevertheless, the first principal component show that the mband is most prominent in all clusters, but has a specific maximum in each cluster. The second principal component shows the bband again with a specific peak frequency in every cluster. For the same analysis with the large channel arrangement see Fig. 14, clearly the results are less pronounced.

In Fig. 15, we contrast the predictors from the resting-state EEG data and the classification performance in the BCI for different numbers of channels and numbers of clusters. The maximum

correlation of 0.581 for sixteen clusters was obtained. Clearly, the small number of channels positioned on the sensorimotor cortex gives rise to better correlation results when compared to the larger and more unspecific channel number that covers the whole brain.

Finally, we come back to the clustering of the pdfs acquired for the BCI experiment. Ideally the clusters may tell whether the resting-state pdfs have physiologically meaningful information especially when comparing to the pdfs from motor imagery. We computed the mean of the resting-state pdfs for each cluster trained from the motor imagery pdfs over the subjects. The clusters presented in Fig. 10 revealed three groups of different performance levels. While the red cluster shows the high performance group, the blue one is the worst, and the green one exhibits mediocre performance. From Fig. 16, we can clearly see that the higher the classification performance, the larger values are found in the pdf around the m- and b-bands. Therefore, based on our prediction and grouping analysis, it is expected that a subject who falls into the blue group can be a potential BCI-illiteracy.

Conclusion

In this work, we show that BSSFO evaluates favorably compared to prototypical spatio(-temporal) filtering methods like CSP [16] in terms of classification performance across a large corpus of 80 subjects from [20], and BSSFO can also infer subjectspecific spatio-temporal patterns, which are shown physiologically meaningful. Individual BSSFO patterns can be clustered to form groups of subjects with similar physiological characteristics. It, therefore, may allow to gain further insight into the characteristics responsible for the performance of subjects beyond the mere amplitudes of m- and b-bands. We could show that a clustering into three groups of subjects exhibit different spatial topographies and is highly predictive for the subjects BCI performance.

Moreover, we study the prediction of a subject’s future BCI performance based on resting-state EEG data acquired prior to a BCI session. Using only 3-Laplacian channels, we could obtain the maximum correlation coefficient of 0.581 with the performance later seen in the actual BCI feedback session; this result compares favorably with previous results [20]. A clustering of the resulting BSSFO patterns shows interesting task-independent physiological characteristics discriminative for ‘‘good’’ and ‘‘bad’’ BCI performers. It is noteworthy that unlike the earlier study [20] that assumed a statistical model of resting-state EEG, BSSFO extracts a full spectral characteristics along with the spatial properties for a subject in a data-driven manner without a-priori assuming a specific role of particular frequency bands. Therefore, it is expected that the BSSFO can be a potential tool for BCIs to care the patients who might have unusual spatio-temporal characteristics due to neurological disorder or brain injury.

Although we have performed the validation of the BSSFO framework here within an offline study, our methods may be readily applied in feedback BCI experiments, both for prescreening subjects and for improving the spatio-temporal signal processing. The subject groupings extracted by our approach could in the future also contribute to create improved subjectindependent classifiers [30,31,28] or better co-adaptive BCI training protocols [12].

While we focused on the SMR-controlled BCI, we would like to emphasize that the BSSFO is also applicable to other kinds of single-trial EEG signal recognition problems that are based on the modulations of brain rhythms. Therefore, it is by no means limited to SMR-controlled BCIs. Furthermore, regarding ECoG-based BCIs, which are also of great interests in the field, it has been studied that the spectral amplitudes of the ECoG signals in the

various frequency bands are task-related, e.g., motor movement [32,33] or auditory processing [34]. Hence, it is natural to extend the current study to the ECoG-based BCI studies using the same framework, in which the task-related frequency bands can be effectively represented in a probabilistic manner.

Appendix

To implement our prior knowledge of common characteristic frequency bands, we first denote B~½bs,be { as a continuous random vector for a frequency band, where bs and be are, respectively, the start and the end frequency of this band with the constraint of bsvbe. We define the probability of a frequency band b, p(b), as the probability that the b bandpass-filtered signals can be correctly classified between two classes.

Since we are presumably uncertain about the discriminative frequency band, we encode this uncertainty as a prior distribution p(B) over a random variable B. Given a set of single-trial EEGs

X~fxigDi~1 and the corresponding class labels V~fvigDi~1, where D is the number of trials, we can compute the posterior pdf, p(BDX,V), by a Bayes rule as follows:

p(X,VDB)p(B) p(X,V)

p(BDX,V)~

: ð16Þ

The prior, p(B), describes the relative probabilities of different states, i.e., frequency bands, in which single-trial EEG responses to motor imagery are correctly discriminated. The term p(X,VDB) is called the likelihood function. If the hypothesis B, i.e., the chosen frequency band, were true, this term indicates the probability that the single-trial EEG responses X are in conjunction with the class labels V. In other words, given a particular frequency band, this likelihood function describes the probability that the single-trial EEGs X can be correctly classified into V. The posterior distribution p(BDX,V) defines the probability that the frequency band B is discriminative when the observations of X and V are

References

- 1. Rockstroh B, Birbaumer N, Elbert T, Lutzenberger W (1984) Operant control of EEG and event-related and slow brain potentials. Biofeedback and Selfregulation 9: 139–160.
- 2. Farwell L, Donchin E (1988) Talking off the top of your head: toward a mental prosthesis utilizing event-related brain potentials. Electroencephalography and clinical Neurophysiology 70: 510–523.
- 3. Birbaumer N, Ghanayim N, Hinterberger T, Iversen I, Kotchoubey B, et al.

(1999) A spelling device for the paralysed. Nature 398: 297–298.

- 4. Wolpaw J, Birbaumer N, McFarland D, Pfurtscheller G, Vaughan T (2002) Brain-computer interfaces for communication and control. Clinical neurophysiology 113: 767–791.
- 5. Pfurtscheller G, Mu¨ller G, Pfurtscheller J, Gerner H, Rupp R (2003) ‘Thought’control of functional electrical stimulation to restore hand grasp in a patient with tetraplegia. Neuroscience Letters 351: 33–36.
- 6. Blankertz B, Curio G, Mu¨ller KR (2002) Classifying single trial EEG: Towards brain computer interfacing. In: Diettrich TG, Becker S, Ghahramani Z, editors, Advances in Neural Information Processing Systems (NIPS 01). volume 14, 157– 164.
- 7. Cheng M, Gao X, Gao S, Xu D (2002) Design and implementation of a braincomputer interface with high transfer rates. IEEE Transactions on Biomedical Engineering 49: 1181–1186.
- 8. Buttfield A, Ferrez PW, Millan J (2006) Towards a robust BCI: error potentials and online learning. IEEE Transactions on Neural Systems and Rehabilitation Engineering 14: 164–168.
- 9. Parra L, Christoforou C, Gerson A, Dyrholm M, Luo A, et al. (2008) Spatiotemporal linear decoding of brain state. IEEE Signal Processing Magazine 28: 107–115.
- 10. Blankertz B, Dornhege G, Krauledat M, Mu¨ller KR, Curio G (2007) The noninvasive berlin brain- computer interface: fast acquisition of effective performance in untrained subjects. NeuroImage 37: 539–550.
- 11. Blankertz B, Losch F, Krauledat M, Dornhege G, Curio G, et al. (2008) The Berlin Brain-Computer Interface: Accurate performance from first-session in

given. Thus, it indicates the relative likelihood of the single-trial EEG responses X being correctly classified into V by B bandpass filtering along with the ensuing computational processes. Note that, in this paper, we do not make any functional assumption about the densities p(B) and p(BDX,V), which could be linearity, Gaussianity, unimodality, etc.

Given a frequency band B and raw EEG signals X, the bandpass-filtered signals Z are deterministically obtained. Furthermore, a spatial filter W is found from Z via a standard CSP algorithm [12] or its variants [8,36,25], in which W is analytically obtained by optimization. In the prevalent processing chain of SMR-controlled BCIs, a feature vector is extracted by computing simple matrix multiplication between Z and W and the secondorder statistics followed by a monotonically increasing logarithmic function. This means, that the posterior p(BDZ,V) can be indirectly estimated from p(BDF,V), where F~log var W{Z , without losing information.

Hence, we can rewrite Eq. (16) as follows.

p(BDX,V) ¼D p(BDF,V)

p(F,VDB)p(B)

p(F,V) ð17Þ where p(F,V)~

~

B p(F,VDB)p(B)dB. Thus, the goal of finding the optimal spatio-spectral filter to extract discriminative features and, thereby, to ultimately improve classification accuracy, can be defined as an estimation of the posterior pdf p(BDF,V) in Eq. (17) (see [24] for details and implementation).

Ð

Author Contributions

Performed the experiments: HIS. Analyzed the data: HIS SF JM KRM. Contributed reagents/materials/analysis tools: SWL. Wrote the paper: HIS SF JM KRM SWL.

- BCI-naive subjects. IEEE Transactions on Biomedical Engineering 55: 2452– 2462.
- 12. Vidaurre C, Sannelli C, Mu¨ller KR, Blankertz B (2011) Machine-learning-based coadaptive calibration for brain-computer interfaces. Neural computation 23: 791–816.
- 13. Koles ZJ, Soong ACK (1998) EEG source localization: implementing the spatiotemporal decomposition approach. Electroencephalography and Clinical Neurophysiology 107: 343–352.
- 14. Lemm S, Blankertz B, Curio G, Mu¨ller KR (2005) Spatio-spectral filters for improving classification of single trial EEG. IEEE Transactions on Biomedical Engineering 52: 1541–1548.
- 15. Dornhege G, Blankertz B, Krauledat M, Losch F, Curio G, et al. (2006) Combined optimization of spatial and temporal filters for improving BrainComputer Interfacing. IEEE Transactions on Biomedical Engineering 53: 2274–2281.
- 16. Blankertz B, Tomioka R, Lemm S, Kawanabe M, Mu¨ller KR (2008) Optimizing spatial filters for robust EEG single-trial analysis. IEEE Signal Processing Megazine 25: 41–56.
- 17. Ang KK, Chin ZY, Zhang H, Guan C (2009) Robust filter bank common spatial pattern (RFBCSP) in motor-imagery-based brain-computer interface. Conf Proc IEEE Eng Med Biol Soc 2009: 578–581.
- 18. Blankertz B, Lemm S, Treder M, Haufe S, Mu¨ller KR (2011) Single-trial analysis and classification of erp componentsa tutorial. NeuroImage 56: 814– 825.
- 19. Lemm S, Blankertz B, Dickhaus T, Mu¨ller KR (2011) Introduction to machine learning for brain imaging. Neuroimage 56: 387–399.
- 20. Blankertz B, Sannelli C, Halder S, Hammer EM, Ku¨bler A, et al. (2010) Neurophysiological predictor of SMR-based BCI performance. NeuroImage 51: 1303–1309.
- 21. Allison B, Luth T, Valbuena D, Teymourian A, Volosyak I, et al. (2010) BCI demographics: how many (and what kinds of) people can use an SSVEP BCI?

- IEEE Transactions on Neural Systems and Rehabilitation Engineering 18: 107– 116.
- 22. Allison B, Neuper C (2010) Could anyone use a BCI? In: Tan D, Nijholt A, editors, Brain-Computer Interfaces, Springer London, Human-Computer Interaction Series. 35–54.
- 23. Hammer E, Halder S, Blankertz B, Sannelli C, Dickhaus T, et al. (2012) Psychological predictors of SMR-BCI performance. Biological Psychology 89: 80–86.
- 24. Suk HI, Lee SW (2013) A novel bayesian framework for discriminative feature extraction in braincomputer interfaces. IEEE Transactions on Pattern Analysis and Machine Intelligence 35: 286–299.
- 25. Vidaurre C, Blankertz B (2010) Towards a cure for BCI illiteracy. Brain Topography 23: 194–198.
- 26. Vidaurre C, Sannelli C, Mu¨ller KR, Blankertz B (2011) Co-adaptive calibration to improve BCI efficiency. Journal of Neural Engineering 8: 025009.
- 27. Ang KK, Guan C (2013) Brain-computer interface in stroke rehabilitation. Journal of Computing Science and Engineering 7: 139–146.
- 28. Fazli S, Dano´czy M, Schelldorfer J, Mu¨ller KR (2011) L1-penalized linear mixed-effects models for high dimensional data with application to BCI. NeuroImage 56: 2100–2108.
- 29. Defays D (1977) An efficient algorithm for a complete link method. The Computer Journal (British Computer Society) 20: 364–366.
- 30. Fazli S, Popescu F, Dano´czy M, Blankertz B, Mu¨ller KR, et al. (2009) Subjectindependent mental state classification in single trials 22: 1305–1312.

- 31. Fazli S, Grozea C, Dano´czy M, Blankertz B, Popescu F, et al. (2009) Subject independent EEGbased BCI decoding. In: Bengio Y, Schuurmans D, Lafferty J, Williams CKI, Culotta A, editors, Advances in Neural Information Processing Systems 22. 513–521.
- 32. Miller KJ, Leuthardt EC, Schalk G, Rao RP, Anderson NR, et al. (2007) Spectral changes in cortical surface potentials during motor movement 27: 2424–2432.
- 33. Schalk G, Kuba´nek J, Miller KJ, Anderson NR, Leuthardt EC, et al. (2007) Decoding twodimensional movement trajectories using electrocorticographic signals in humans. Journal of Neural Engineering 4: 264.
- 34. Pasley BN, David SV, Mesgarani N, Flinker A, Shamma SA, et al. (2012) Reconstructing speech from human auditory cortex. PLoS Biol 10: e1001251.
- 35. Blankertz B, Kawanabe M, Tomioka R, Hohlefeld F, Nikulin V, et al. (2008) Invariant Common Spatial Patterns: Alleviating Nonstationarities in BrainComputer Interfacing’’. In: Platt J, Koller D, Singer Y, Roweis S, editors, Advances in Neural Information Processing Systems 20, Cambridge, MA: MIT Press. 113–120.
- 36. Wang H, Zheng W (2008) Local temporal common spatial patterns for robust single-trial EEG classification. IEEE Transactions on Neural Systems and Rehabilitation Engineering 16: 131–139.
- 37. Lotte F, Guan C (2011) Regularizing common spatial patterns to improve BCI designs: unified theory and new algorithms. IEEE Transactions on Biomedical Engineering 58: 355–362.

